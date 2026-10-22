# -*- coding: utf-8 -*-
"""Publiceert losse NBA-voorbeschouwingen (scripts in het formaat van lakers_warriors_nba_2026.py):
deelkaart in het VOORBESCHOUWING-ontwerp (preview-images-agent/kaart.py, zoals Lakers – Warriors: logo's, record vorig
seizoen, onze voorspelling, aftrap, odds Winnaar incl. verlenging) + Nieuws-item live (rubriek Basketball, competitie NBA,
wedtip-velden). Het script moet een dict KAART hebben:
  KAART = {"home": "76ers", "away": "Cavaliers", "home_abbr": "phi", "away_abbr": "cle",      # ESPN-afkortingen (logo's)
           "home_pos": "45-37 · nr. 7 Oost 2025/26", "away_pos": "52-30 · nr. 4 Oost 2025/26",
           "hs": 115, "as": 108, "datum": "Vr 23 okt", "tijd": "01:00", "odd_home": "1,67", "odd_away": "2,30"}
  set -a; . ../superodd-agent/.env; set +a; ../superodd-agent/.venv/bin/python specials/nba_preview_publiceer.py sixers_cavaliers_nba_2026 [...] [--live]"""
import os, sys, re, time, subprocess, urllib.request, importlib
from datetime import datetime, timezone
HIER = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HIER, "..")
sys.path.insert(0, ROOT); sys.path.insert(0, HIER); sys.path.insert(0, os.path.join(ROOT, "og_kaarten"))
import lk_webflow as WF

RAW_MAIN = "https://raw.githubusercontent.com/BetExperts/bet-experts-live-kijken/main/"
PIA = os.path.join(ROOT, "..", "preview-images-agent")


def kaart_render(m):
    """Deelkaart in het voorbeschouwing-ontwerp -> og/<slug-zonder-wedtips>-<hash>.webp (relatief pad)."""
    import io, hashlib, shutil
    from PIL import Image
    from playwright.sync_api import sync_playwright
    sys.path.insert(0, PIA); import kaart
    k = m.KAART
    logos = {"logo-nba.png": "https://a.espncdn.com/i/teamlogos/leagues/500/nba.png",
             f"logo-{k['home_abbr']}.png": f"https://a.espncdn.com/i/teamlogos/nba/500/{k['home_abbr']}.png",
             f"logo-{k['away_abbr']}.png": f"https://a.espncdn.com/i/teamlogos/nba/500/{k['away_abbr']}.png"}
    for f, u in logos.items():
        urllib.request.urlretrieve(u, kaart.ASSETS / f)
    d = {"comp": "NBA", "ronde": "Reguliere competitie 2026/27", "comp_logo": "logo-nba.png",
         "home": k["home"], "away": k["away"], "home_logo": f"logo-{k['home_abbr']}.png", "away_logo": f"logo-{k['away_abbr']}.png",
         "home_pos": k["home_pos"], "away_pos": k["away_pos"], "home_form": "", "away_form": "", "hs": k["hs"], "as": k["as"],
         "datum": k["datum"], "tijd": k["tijd"],
         "odds": [("1", k["home"].split()[-1], k["odd_home"], "hit" if k["hs"] > k["as"] else ""),
                  ("2", k["away"].split()[-1], k["odd_away"], "hit" if k["as"] > k["hs"] else "")]}
    body = kaart.kaart(d).replace("Odds 1 · X · 2", "Winnaar incl. verlenging")
    p = kaart.ASSETS / f".{m.SLUG}.html"
    p.write_text(f"<!doctype html><html lang='nl'><head><meta charset='utf-8'><style>{kaart.CSS}</style></head><body>{body}</body></html>", encoding="utf-8")
    try:
        with sync_playwright() as pw:
            b = pw.chromium.launch(args=["--font-render-hinting=none"])
            pg = b.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=2)
            pg.goto(p.as_uri(), wait_until="networkidle"); pg.evaluate("document.fonts.ready"); pg.evaluate(kaart.FIT_JS); pg.wait_for_timeout(300)
            png = pg.screenshot(); b.close()
    finally:
        p.unlink(missing_ok=True)
        for f in logos: (kaart.ASSETS / f).unlink(missing_ok=True)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).convert("RGB").resize((1200, 630), Image.LANCZOS).save(buf, "WEBP", quality=88, method=6)
    rel = f"og/{m.SLUG.replace('-wedtips', '')}-{hashlib.md5(buf.getvalue()).hexdigest()[:6]}.webp"
    open(os.path.join(ROOT, rel), "wb").write(buf.getvalue())
    return rel


def datum(m):
    for naam in ("DATUM", "DATUM_TIJD", "AFTRAP"):
        if getattr(m, naam, None): return getattr(m, naam)
    s = open(m.__file__).read()
    return re.search(r'"datum-tijd-van-wedstrijd":\s*"([^"]+)"', s).group(1)


def main(namen, live):
    mods = {n: importlib.import_module(n) for n in namen}
    for n, m in mods.items():
        assert hasattr(m, "KAART"), f"{n}: KAART-dict ontbreekt (zie docstring)"
        print(n, "|", len(m.TITEL), m.TITEL, "|", m.SLUG, "|", datum(m))
    if not live:
        return
    rel = {n: kaart_render(m) for n, m in mods.items()}
    paden = " ".join(rel.values()) + " " + " ".join(f"specials/{n}.py" for n in mods)
    subprocess.run(f"git add {paden} && git commit -qm 'NBA-voorbeschouwingen: deelkaarten' && "
                   "git stash -q; git pull -q --rebase; git push -q; git stash pop -q", shell=True, cwd=ROOT)
    for n, m in mods.items():
        url = RAW_MAIN + rel[n]
        for _ in range(20):
            try:
                if urllib.request.urlopen(url, timeout=20).status == 200: break
            except Exception: time.sleep(6)
        k = m.KAART
        beeld = {"url": url, "alt": f"{k['home']} – {k['away']} voorspelling: {k['hs']}-{k['as']}, {k['datum']} {k['tijd']}"}
        fd = {"name": m.TITEL, "slug": m.SLUG, "content": m.content, "content-2": m.content2, "content-3": m.content3,
              "samenvatting": m.SAMENVATTING, "rubriek": m.RUBRIEK_BASKETBAL, "competitie": m.COMPETITIE_NBA,
              "datum-tijd-van-wedstrijd": datum(m), "publicatiedatum": datetime.now(timezone.utc).isoformat(),
              "afbeelding": beeld, "seo-afbeelding": beeld, **m.WEDTIPS}
        print(n, "nieuws:", WF.create_live(fd))


if __name__ == "__main__":
    main([a for a in sys.argv[1:] if not a.startswith("--")], "--live" in sys.argv)
