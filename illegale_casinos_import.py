# -*- coding: utf-8 -*-
"""Importeert onderzoeksresultaten (JSON-arrays) als DRAFT-items in de collectie Illegale casino's (6ad8a3c0a569b45d16344503)
en maakt per casino een deelafbeelding (og/illegale-casinos/<slug>-<hash>.webp, via GitHub raw).
Bestaande slugs worden bijgewerkt (staged), niet dubbel aangemaakt. Publiceren gebeurt pas als de templatepagina er is.
  set -a; . ../superodd-agent/.env; set +a; ../superodd-agent/.venv/bin/python illegale_casinos_import.py batch1.json [...] [--dry]"""
import sys, json, re, io, hashlib, urllib.request, urllib.error, pathlib, subprocess
from datetime import datetime, timezone
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import lk_webflow as WF
from og_kaarten.illegaal_casino import render_kaarten

COLL = "6ad8a3c0a569b45d16344503"
OPTIES = {"Curaçao": "939c0d6dca2ad7f0e4bdc116be39bb9b", "Anjouan": "32eecb213826c11e8d10ecc7ce6bebe3",
          "Malta (MGA)": "1bdc46e3ec2663a8314a44e4fac79aa3", "Kahnawake": "8be3ac203ab80601a706fec52a8164a5",
          "Costa Rica": "5dd21b407febf7ca0b71da7f885b17ed", "Overig": "e7b88a87caa931db1f4af0352b60dfef",
          "Geen": "d6d008bc81ae4ff478345d1073192352", "Onbekend": "d5c1cc01eea4efe7bb91234da6d4076c"}
# bestaande nieuwsartikelen 'is X legaal' (slug-sleutel -> nieuws-item-id, publicatiedatum wordt opgehaald)
ARTIKELEN = {"shakebet": "6980d42a720c86ab8fc5e8fb", "carlospin": "68c01951e9893007b2877483", "kaasino": "68b03bf15d4a560930ced6f9",
             "polymarket": "68b039d13cdb4c6b57256c78", "booms-bet": "68b038127ff021e1c1cc70bb", "lalabet": "6866a0f99d2dc6e972789f93",
             "skyhills-casino": "67fcd38c8d108dd1aeeac70d", "betsixty": "67ed203c9b86ca65e31bad88", "instant-casino": "67c9b0641d70c2ffc863e614",
             "bof-casino": "6673ee5e5dad8d0af8d09c04", "happy-slots": "6673ec8f9c3837d3e2c7eff9", "slots-hammer": "6673eac23ec9dc874341045d",
             "scarabet": "6673e7c2b6d4f1053eaf1ef6", "qbet": "6672925af55c54d79b52e682"}
RAW = "https://raw.githubusercontent.com/BetExperts/bet-experts-live-kijken/main/"
H = {"Authorization": "Bearer " + WF.WEBFLOW_TOKEN, "Content-Type": "application/json"}


def api(method, url, body=None):
    r = urllib.request.Request(url, data=json.dumps(body).encode() if body is not None else None, method=method, headers=H)
    with urllib.request.urlopen(r, timeout=60) as resp:
        return json.load(resp)


def bestaande():
    out, off = {}, 0
    while True:
        d = api("GET", f"{WF.WF_API}/collections/{COLL}/items?limit=100&offset={off}")
        for it in d["items"]:
            out[it["fieldData"]["slug"]] = it["id"]
        off += 100
        if len(d["items"]) < 100: return out


def main(paden, dry):
    rijen = []
    for p in paden:
        rijen += json.load(open(p))
    nu = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    # deelafbeeldingen
    og = pathlib.Path(__file__).parent / "og" / "illegale-casinos"; og.mkdir(parents=True, exist_ok=True)
    LOGOS = pathlib.Path(__file__).parent / "og" / "illegale-casinos" / "logos"
    for c in rijen:
        lf = LOGOS / f"{c['slug']}.png"
        if lf.exists(): c["logo_file"] = str(lf)
    pngs = render_kaarten(rijen, "/tmp/ic_og")
    from PIL import Image
    rel = {}
    for c in rijen:
        im = Image.open(pngs[c["slug"]]).convert("RGB").resize((1200, 630), Image.LANCZOS); buf = io.BytesIO(); im.save(buf, "WEBP", quality=88, method=6)
        f = og / f"{c['slug']}-{hashlib.md5(buf.getvalue()).hexdigest()[:6]}.webp"
        for oud in og.glob(f"{c['slug']}-*.webp"):
            if oud != f: oud.unlink()
        f.write_bytes(buf.getvalue()); rel[c["slug"]] = str(f.relative_to(pathlib.Path(__file__).parent))
    if dry:
        print("dry:", len(rijen), "items;", list(rel.values())[:3]); return
    subprocess.run(["git", "add", "-A", "og/illegale-casinos"], cwd=pathlib.Path(__file__).parent, check=True)
    subprocess.run(["git", "commit", "-q", "-m", "Deelafbeeldingen illegale casino's\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"], cwd=pathlib.Path(__file__).parent)
    subprocess.run("git stash -q; git pull -q --rebase; git push -q; git stash pop -q", shell=True, cwd=pathlib.Path(__file__).parent)
    have = bestaande()
    nieuw, upd = [], []
    for c in rijen:
        sinds = nu
        art = ARTIKELEN.get(c["slug"])
        if art:
            try: sinds = WF.get_item(art)["fieldData"].get("publicatiedatum") or nu
            except Exception: pass
        fd = {"name": c["name"], "slug": c["slug"], "bedrijf": c.get("bedrijf") or "Onbekend",
              "vergunning-elders": OPTIES.get(c.get("vergunning_elders"), OPTIES["Onbekend"]),
              "vergunning-toelichting": c.get("vergunning_toelichting", ""), "website": c.get("website", ""),
              "ideal": bool(c.get("ideal")), "crypto": bool(c.get("crypto")), "op-de-lijst-sinds": sinds, "gecontroleerd-op": nu,
              "ksa-maatregel": c.get("ksa_maatregel", ""), "korte-omschrijving": c.get("korte_omschrijving", ""),
              "waarom-illegaal": c.get("waarom_illegaal_html", ""), "uitbetalen-en-bonus": c.get("uitbetalen_en_bonus_html", ""),
              "faq": c.get("faq", ""), "seo-titel": c.get("seo_titel", ""), "meta-omschrijving": c.get("meta_omschrijving", ""),
              "deel-afbeelding": RAW + rel[c["slug"]]}
        if art: fd["nieuwsartikel"] = art
        if c.get("logo_file"): fd["logo"] = RAW + "og/illegale-casinos/logos/" + c["slug"] + ".png"
        try:
            if c["slug"] in have:
                api("PATCH", f"{WF.WF_API}/collections/{COLL}/items/{have[c['slug']]}", {"fieldData": fd}); upd.append(c["slug"])
            else:
                r = api("POST", f"{WF.WF_API}/collections/{COLL}/items", {"isDraft": True, "fieldData": fd}); nieuw.append(c["slug"])
        except urllib.error.HTTPError as e:
            print("FOUT", c["slug"], e.code, e.read().decode()[:400])
    print("nieuw:", len(nieuw), nieuw); print("bijgewerkt:", len(upd), upd)


if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    main(a, "--dry" in sys.argv)
