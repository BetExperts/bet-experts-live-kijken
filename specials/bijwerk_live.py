# -*- coding: utf-8 -*-
"""Bestaand LIVE special-artikel bijwerken vanuit zijn module (10-11-2026).
Zet de titel, samenvatting en content/content-2/content-3 van specials/<module>.py over naar het live item en publiceert opnieuw.
- Eerst een back-up van het live item naar ../backups/nieuws-<slug>-<datum>.json.
- Het 'Meer over'-blok (crosslink) blijft behouden.
- Met --kaart gaat de deelkaart og/nieuws/nieuws-<SLUG>.webp mee, via GitHub raw met een hash in de bestandsnaam
  (nooit een gecachte oude versie). Webflow importeert de kaart naar zijn eigen CDN.
- Daarna draait linking-agent/link_ids.py <id> voor de automatische interne links.
  set -a; . ../superodd-agent/.env; set +a; ../superodd-agent/.venv/bin/python specials/bijwerk_live.py <module> <item-id> [--kaart] [--dry]
Afbeeldingen IN de content (infographics) moeten al als publieke URL in de module staan, bijvoorbeeld via een env-variabele."""
import hashlib, importlib, json, os, shutil, subprocess, sys, time, urllib.error, urllib.request
from datetime import date
HIER = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HIER, "..")
sys.path.insert(0, ROOT); sys.path.insert(0, HIER)
import lk_webflow as WF

RAW = "https://raw.githubusercontent.com/BetExperts/bet-experts-live-kijken/main/"


def raw_upload(pad_rel):
    """Bestand (relatief aan ROOT) committen + pushen; geeft de raw-URL zodra die bereikbaar is."""
    subprocess.run(f"git add '{pad_rel}' && git commit -qm 'upd {os.path.basename(pad_rel)}'; git pull -q --rebase --autostash; git push -q",
                   shell=True, cwd=ROOT)
    url = RAW + pad_rel
    for _ in range(30):
        try:
            if urllib.request.urlopen(url, timeout=20).status == 200:
                return url
        except urllib.error.HTTPError:
            time.sleep(5)
    raise SystemExit(f"STOP: {url} niet bereikbaar")


def main(naam, iid, kaart=False, dry=False):
    A = importlib.import_module(naam)
    oud = WF.get_item(iid, live=True) or {}
    ofd = oud.get("fieldData") or {}
    if ofd.get("slug") != A.SLUG:
        raise SystemExit(f"STOP: item {iid} heeft slug {ofd.get('slug')!r}, module {A.SLUG!r}")
    fd = {"name": A.TITEL, "samenvatting": A.SAMENVATTING, "content": A.content, "content-2": A.content2, "content-3": A.content3}
    WF.behoud_meer_over(iid, fd)
    if dry:
        print("DRY", iid, A.TITEL, {k: len(v) for k, v in fd.items()}); return
    os.makedirs(os.path.join(ROOT, "..", "backups"), exist_ok=True)
    bk = os.path.join(ROOT, "..", "backups", f"nieuws-{A.SLUG[:70]}-{date.today()}.json")
    if not os.path.exists(bk):
        json.dump(oud, open(bk, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if kaart:
        src = os.path.join(ROOT, "og", "nieuws", f"nieuws-{A.SLUG}.webp")
        h = hashlib.md5(open(src, "rb").read()).hexdigest()[:8]
        rel = f"og/nieuws/upd/nieuws-{A.SLUG[:70]}-{h}.webp"
        os.makedirs(os.path.join(ROOT, "og", "nieuws", "upd"), exist_ok=True)
        shutil.copy(src, os.path.join(ROOT, rel))
        beeld = {"url": raw_upload(rel), "alt": A.TITEL}
        fd.update({"afbeelding": beeld, "seo-afbeelding": beeld})
    WF.update_live(iid, fd)
    print("bijgewerkt + live:", iid, A.TITEL)
    try:
        subprocess.run([sys.executable, os.path.join(ROOT, "..", "linking-agent", "link_ids.py"), iid], check=False,
                       cwd=os.path.join(ROOT, "..", "linking-agent"), timeout=300)
    except Exception as e:
        print("linking-agent overgeslagen:", e)


if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    main(a[0], a[1], "--kaart" in sys.argv, "--dry" in sys.argv)
