# -*- coding: utf-8 -*-
"""Deelkaart (1200x630) voor het artikel Asian totaal / Asian over-under, met mini-matrix (uitkomsten via asian_rekenen).
  ../superodd-agent/.venv/bin/python og_kaarten/asian_totaal_og.py  -> og/nieuws/asian-totaal.webp"""
import sys, uuid, pathlib, io
HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))
from asian import BASE, GLOW, G, A, cel, nl
from asian_rekenen import totaal
from playwright.sync_api import sync_playwright
from PIL import Image

LIJNEN = [2, 2.25, 2.5, 2.75, 3]
GOALS = [1, 2, 3, 4]
kop = "".join(f'<div class="h" style="font-size:11px">{g} goal{"s" if g != 1 else ""}</div>' for g in GOALS)
rijen = "".join(f'<div class="rl" style="font-size:15px">{nl(l, False)}</div>' +
                "".join(cel(totaal(l, g)).replace('class="c"', 'class="c" style="font-size:12px;').replace('style="font-size:12px; style="', 'style="font-size:12px;') for g in GOALS)
                for l in LIJNEN)
HTML = f'''<div class="b">{GLOW}
  <img src="betexperts_logo.png" style="position:absolute;left:56px;top:44px;height:28px">
  <div style="position:absolute;right:56px;top:40px;font:700 15px 'Plus Jakarta Sans'">Wedgids <span style="color:#8A97A3;font-weight:600">· met tabel + gratis pdf</span></div>
  <div style="position:absolute;left:56px;right:56px;top:150px;display:flex;gap:36px;align-items:center">
    <div style="flex:1;min-width:0"><div class="eb">Meer dan / minder dan</div>
      <div style="font:800 60px/1.0 'Poppins';letter-spacing:-1.6px;margin-top:14px">Wat is <span style="color:{G}">Asian over/under</span>?</div>
      <div style="margin-top:24px;display:flex;gap:10px;flex-wrap:wrap">
        <span style="border-radius:999px;padding:9px 16px;font:700 15px Plus Jakarta Sans;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12)">Asian totaal uitgelegd</span>
        <span style="border-radius:999px;padding:9px 16px;font:700 15px Plus Jakarta Sans;background:{G};color:#0B1117">Inzet terug of halve winst</span></div></div>
    <div style="width:430px;flex:none" class="box"><div style="font:700 12px Plus Jakarta Sans;letter-spacing:2px;color:#8A97A3;text-transform:uppercase;margin-bottom:8px">Meer dan … doelpunten</div>
      <div class="grid" style="grid-template-columns:70px repeat(4,1fr);grid-auto-rows:40px">
      <div class="h" style="font-size:11px">Lijn</div>{kop}{rijen}</div></div></div>
  <div style="position:absolute;left:56px;right:56px;bottom:52px;height:1px;background:rgba(255,255,255,.08)"></div>
  <div style="position:absolute;left:56px;bottom:20px;font-size:13px;color:#8A97A3">Wat kost gokken jou? Stop op tijd. 18+</div>
  <div style="position:absolute;right:56px;bottom:20px;font:700 13px 'Plus Jakarta Sans';color:#6CC08B">bet-experts.nl</div></div>'''

if __name__ == "__main__":
    uit = HIER.parent / "og" / "nieuws" / "asian-totaal.webp"; uit.parent.mkdir(parents=True, exist_ok=True)
    f = A / f".at-{uuid.uuid4().hex[:8]}.html"
    f.write_text(f"<!doctype html><html lang='nl'><head><meta charset='utf-8'><style>{BASE}</style></head><body>{HTML}</body></html>", encoding="utf-8")
    try:
        with sync_playwright() as p:
            b = p.chromium.launch(args=["--font-render-hinting=none"])
            pg = b.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=2)
            pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
            Image.open(io.BytesIO(pg.screenshot())).convert("RGB").save(uit, "WEBP", quality=88, method=6)
            b.close()
    finally:
        f.unlink(missing_ok=True)
    print(uit)
