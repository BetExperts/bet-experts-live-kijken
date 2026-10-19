# -*- coding: utf-8 -*-
"""TOTO 50x-banners automatisch up-to-date houden (19-10-2026).

Per wedstrijd met een voorbeschouwing (komende 5 dagen) of een live-kijken-artikel (Champions/Europa League) maakt dit
script de banner (variant A, desktop + mobiel) en schrijft site-static/files/toto50x.json (vaste naam, 10 min cache):
  {"actief": bool, "link": <TOTO 50x-affiliatelink>, "paginas": {pad: {"f": fid, "t": "vb"|"lk", "ko": iso}},
   "fix": {fid: {"u": desktop-url, "m": mobiel-url, "alt": tekst}}}
Het footer-script t50-cta.js leest dat bestand en toont de banner op de juiste pagina, tot de aftrap.
Is de TOTO 50x-promo niet (meer) live, dan "actief": false en verdwijnt alles. Draait elk half uur mee in
linking-agent/run_boost_links.sh; deployt alleen als er iets veranderd is.
  python3 sync.py [--dry]
"""
import hashlib, io, json, os, re, subprocess, sys, time, urllib.request
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
FILES = os.path.join(ROOT, "site-static", "files")
STATE = os.path.join(HERE, "state.json")
NL = ZoneInfo("Europe/Amsterdam")
NIEUWS, PROMOTIES = "64ff0fbd5a8f205b05d54656", "65e6fb5b08aed95b983b590f"
TOTO_50X = "https://partner.toto.nl/C.ashx?btag=a_375b_445c_&affid=184&siteid=375&adid=445&c="   # TOTO 50x-promo
LK_LEAGUES = {"champions-league", "europa-league"}
DAGEN_VOORUIT = 5
BASE = "https://www.bet-experts.nl/be-static/"
DAG = ["ma", "di", "wo", "do", "vr", "za", "zo"]
MND = ["jan", "feb", "mrt", "apr", "mei", "jun", "jul", "aug", "sep", "okt", "nov", "dec"]


def env():
    for line in open(os.path.join(ROOT, "superodd-agent", ".env"), encoding="utf-8"):
        if "=" in line and not line.startswith("#"):
            k, v = line.strip().split("=", 1); os.environ.setdefault(k, v)


def get_json(url, auth=False):
    h = {"User-Agent": "Mozilla/5.0 (bet-experts t50-sync)", "accept": "application/json"}
    if auth:
        h["Authorization"] = "Bearer " + os.environ["WEBFLOW_TOKEN"]
    for poging in range(4):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=40))
        except Exception:
            time.sleep(3 * (poging + 1))
    return None


def promo_actief():
    r = get_json(f"https://api.webflow.com/v2/collections/{PROMOTIES}/items/live?slug=toto-50x-je-inzet", auth=True) or {}
    it = (r.get("items") or [None])[0]
    if not it or it.get("isArchived") or it.get("isDraft"):
        return False
    tot = (it.get("fieldData") or {}).get("wanneer-toegevoegd")
    return not tot or datetime.fromisoformat(tot.replace("Z", "+00:00")) > datetime.now(timezone.utc)


def pagina_s(now):
    """{pad: (fid, soort, kickoff)} van voorbeschouwingen en live-kijken-artikelen."""
    out = {}
    items = []
    for off in (0, 100, 200):
        r = get_json(f"https://api.webflow.com/v2/collections/{NIEUWS}/items/live?limit=100&offset={off}"
                     f"&sortBy=createdOn&sortOrder=desc", auth=True) or {}
        items += r.get("items") or []
    for it in items:
        f = it["fieldData"]; ko = f.get("datum-tijd-van-wedstrijd"); fid = f.get("fixture-id")
        if not ko or not fid or not re.search(r"wedtips|voorspelling", f.get("slug", "")):
            continue
        k = datetime.fromisoformat(ko.replace("Z", "+00:00"))
        if now < k <= now + timedelta(days=DAGEN_VOORUIT):
            out[f"/nieuws/{f['slug']}"] = (str(fid).strip(), "vb", k)
    lk = json.load(open(os.path.join(ROOT, "live-kijken-agent", "state", "live-kijken.json"), encoding="utf-8"))
    for fid, e in lk.items():
        if not isinstance(e, dict) or e.get("hub") or e.get("league") not in LK_LEAGUES or not e.get("slug"):
            continue
        if e.get("date", "") >= now.astimezone(NL).date().isoformat():
            out[f"/nieuws/{e['slug']}"] = (str(fid), "lk", None)
    return out


def wedstrijd(fid):
    d = get_json(f"https://www.bet-experts.nl/api/match/{fid}") or {}
    r = (d.get("response") or [None])[0]
    if not r:
        return None
    ko = datetime.fromisoformat(r["fixture"]["date"].replace("Z", "+00:00"))
    l = ko.astimezone(NL)
    comp = re.sub(r"^UEFA\s+", "", (r.get("league") or {}).get("name") or "Voetbal")
    return {"comp": comp, "thuis": r["teams"]["home"]["name"], "uit": r["teams"]["away"]["name"],
            "thuis_logo": r["teams"]["home"]["logo"], "uit_logo": r["teams"]["away"]["logo"],
            "datum": f"{DAG[l.weekday()]} {l.day} {MND[l.month - 1]} · {l:%H:%M}", "ko": ko}


def main():
    dry = "--dry" in sys.argv
    env()
    sys.path.insert(0, HERE)
    import banner
    from PIL import Image
    now = datetime.now(timezone.utc)
    st = json.load(open(STATE, encoding="utf-8")) if os.path.exists(STATE) else {"fix": {}}
    actief = promo_actief()
    paginas, fixinfo, nieuw = {}, {}, []
    if actief:
        pag = pagina_s(now)
        fids = sorted({v[0] for v in pag.values()})
        info = {}
        for fid in fids:
            w = wedstrijd(fid)
            if w and w["ko"] > now:
                info[fid] = w
        todo = []
        for fid, w in info.items():
            sig = hashlib.sha1(json.dumps([w["comp"], w["thuis"], w["uit"], w["datum"], w["thuis_logo"], w["uit_logo"],
                                           os.path.getmtime(os.path.join(HERE, "banner.py"))]).encode()).hexdigest()[:8]
            rec = st["fix"].get(fid)
            if not rec or rec.get("sig") != sig or not os.path.exists(os.path.join(FILES, rec["u"])):
                todo.append((fid, w, sig))
        if todo and not dry:
            from playwright.sync_api import sync_playwright
            with sync_playwright() as pw:
                b = pw.chromium.launch()
                for fid, w, sig in todo:
                    namen = {}
                    for mob, achter in ((False, ""), (True, "-m")):
                        png = os.path.join(HERE, f".t50-{fid}{achter}.png")
                        banner.render(w, "A", png, mobiel=mob, browser=b)
                        naam = f"t50-{fid}{achter}-{sig}.webp"
                        Image.open(png).convert("RGB").save(os.path.join(FILES, naam), "WEBP", quality=86, method=6)
                        os.remove(png); namen[achter or "d"] = naam
                    oud = st["fix"].get(fid) or {}
                    for k in ("u", "m"):
                        if oud.get(k) and oud[k] not in namen.values():
                            try: os.remove(os.path.join(FILES, oud[k]))
                            except OSError: pass
                    st["fix"][fid] = {"sig": sig, "u": namen["d"], "m": namen["-m"]}
                    nieuw.append(f"{w['thuis']} – {w['uit']}")
                b.close()
        for pad, (fid, soort, _) in pag.items():
            if fid in info and fid in st["fix"]:
                paginas[pad] = {"f": fid, "t": soort, "ko": info[fid]["ko"].isoformat()}
                w = info[fid]
                fixinfo[fid] = {"u": BASE + st["fix"][fid]["u"], "m": BASE + st["fix"][fid]["m"],
                                "alt": f"TOTO 50x je inzet: {w['thuis']} of {w['uit']}, kies jouw favoriet. Zet €1 in, krijg €50 aan "
                                       f"Free Bets. Alleen voor nieuwe spelers van 24+, voorwaarden van toepassing."}
    # oude banners (wedstrijd voorbij) opruimen
    for fid in list(st["fix"]):
        if fid not in fixinfo:
            rec = st["fix"].pop(fid)
            if not dry:
                for k in ("u", "m"):
                    try: os.remove(os.path.join(FILES, rec[k]))
                    except OSError: pass
    manifest = {"actief": bool(actief and paginas), "link": TOTO_50X, "paginas": paginas, "fix": fixinfo}
    pad = os.path.join(FILES, "toto50x.json")
    oud = open(pad, encoding="utf-8").read() if os.path.exists(pad) else ""
    tekst = json.dumps(manifest, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
    veranderd = tekst != oud
    print(f"TOTO 50x {'actief' if actief else 'NIET actief'} | pagina's: {len(paginas)} | wedstrijden: {len(fixinfo)} | "
          f"nieuwe banners: {len(nieuw)} {nieuw[:6]} | manifest {'gewijzigd' if veranderd else 'gelijk'}")
    if dry:
        return
    json.dump(st, open(STATE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if veranderd or nieuw:
        open(pad, "w", encoding="utf-8").write(tekst)
        r = subprocess.run([os.path.join(ROOT, "superodd-agent", ".venv", "bin", "python"), os.path.join(ROOT, "site-static", "deploy.py")],
                           capture_output=True, text=True, timeout=900)
        print("deploy:", (r.stdout.strip().splitlines() or ["?"])[-1], r.stderr.strip()[-300:])


if __name__ == "__main__":
    main()
