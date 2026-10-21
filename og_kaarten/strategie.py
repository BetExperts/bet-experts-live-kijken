# -*- coding: utf-8 -*-
"""Deelkaarten (1200x630) voor de uitleg-/strategie-artikelen (specials/strategie_<key>.py).
Leest OG_KOP, OG_EYEBROW, OG_CHIPS, OG_MOTIEF en OG_DATA uit het artikelscript en schrijft og/nieuws/strategie-<key>.webp.
  ../superodd-agent/.venv/bin/python og_kaarten/strategie.py <key> [<key> ...]"""
import sys, uuid, pathlib, importlib, io
sys.path.insert(0, "/Users/jaspervandenboogaard/bet-experts/preview-images-agent")
HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER)); sys.path.insert(0, str(HIER.parent)); sys.path.insert(0, str(HIER.parent / "specials"))
import kaart
from asian import BASE, GLOW, G
from playwright.sync_api import sync_playwright
from PIL import Image

A = pathlib.Path(kaart.ASSETS)
UIT = HIER.parent / "og" / "nieuws"
CHIP = "border-radius:999px;padding:9px 16px;font:700 15px Plus Jakarta Sans;"


def visual(motief, data):
    """Mini-visual rechts: rijen uit OG_DATA, per motief anders vormgegeven."""
    n = max(len(data), 1)
    if motief == "reeks":   # oplopende inzetten als staafjes
        hoog = [round(60 + 230 * k / max(n - 1, 1)) for k in range(n)]
        staaf = "".join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px;flex:1">'
                        f'<div style="font:800 15px Plus Jakarta Sans;color:#F5F9FA;white-space:nowrap">{d}</div>'
                        f'<div style="width:100%;height:{h}px;border-radius:10px 10px 4px 4px;background:linear-gradient(180deg,{G},rgba(47,212,110,.35))"></div></div>'
                        for d, h in zip(data, hoog))
        return f'<div style="display:flex;align-items:flex-end;gap:10px;height:330px">{staaf}</div>'
    rijen = []
    for k, d in enumerate(data):
        links, _, rechts = d.partition("·")
        accent = k == 0 if motief == "odds" else False
        rijen.append(f'<div style="display:flex;justify-content:space-between;align-items:center;border-radius:12px;padding:0 18px;height:{min(64, 300 // n)}px;'
                     f'background:{"rgba(47,212,110,.16)" if accent else "rgba(255,255,255,.06)"};border:1px solid {"rgba(47,212,110,.5)" if accent else "rgba(255,255,255,.09)"}">'
                     f'<span style="font:700 17px Plus Jakarta Sans;color:#DDE4EA">{"" if motief != "lijst" else "<b style=\'color:" + G + ";margin-right:10px\'>" + str(k + 1).zfill(2) + "</b>"}{links.strip()}</span>'
                     f'<span style="font:800 19px Poppins;color:{G if rechts.strip() else "#F5F9FA"}">{rechts.strip()}</span></div>')
    return f'<div style="display:flex;flex-direction:column;gap:9px">{"".join(rijen)}</div>'


def kaart_html(m):
    chips = "".join(f'<span style="{CHIP}{"background:" + G + ";color:#0B1117" if i else "background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12)"}">{c}</span>'
                    for i, c in enumerate(m.OG_CHIPS[:2]))
    kop = m.OG_KOP.replace("<span>", f'<span style="color:{G}">')
    grootte = 62 if len(kop) < 90 else 54
    return f'''<div class="b">{GLOW}
  <img src="betexperts_logo.png" style="position:absolute;left:56px;top:44px;height:28px">
  <div style="position:absolute;right:56px;top:40px;font:700 15px 'Plus Jakarta Sans'">Wedgids <span style="color:#8A97A3;font-weight:600">· uitleg met voorbeelden</span></div>
  <div style="position:absolute;left:56px;right:56px;top:140px;bottom:90px;display:flex;gap:44px;align-items:center">
    <div style="flex:1;min-width:0"><div class="eb">{m.OG_EYEBROW}</div>
      <div style="font:800 {grootte}px/1.02 'Poppins';letter-spacing:-1.6px;margin-top:14px">{kop}</div>
      <div style="margin-top:26px;display:flex;gap:10px;flex-wrap:wrap">{chips}</div></div>
    <div style="width:430px;flex:none" class="box">{visual(m.OG_MOTIEF, m.OG_DATA)}</div></div>
  <div style="position:absolute;left:56px;right:56px;bottom:52px;height:1px;background:rgba(255,255,255,.08)"></div>
  <div style="position:absolute;left:56px;bottom:20px;font-size:13px;color:#8A97A3">Wat kost gokken jou? Stop op tijd. 18+</div>
  <div style="position:absolute;right:56px;bottom:20px;font:700 13px 'Plus Jakarta Sans';color:#6CC08B">bet-experts.nl</div></div>'''


def render(keys):
    UIT.mkdir(parents=True, exist_ok=True); tmp = []; uit = {}
    try:
        with sync_playwright() as p:
            b = p.chromium.launch(args=["--font-render-hinting=none"])
            for key in keys:
                m = importlib.import_module(f"strategie_{key}")
                f = A / f".st-{uuid.uuid4().hex[:8]}.html"; tmp.append(f)
                f.write_text(f"<!doctype html><html lang='nl'><head><meta charset='utf-8'><style>{BASE}</style></head><body>{kaart_html(m)}</body></html>", encoding="utf-8")
                pg = b.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=2)
                pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
                png = pg.screenshot()
                doel = UIT / f"strategie-{key}.webp"
                Image.open(io.BytesIO(png)).convert("RGB").save(doel, "WEBP", quality=88, method=6)
                uit[key] = doel
            b.close()
    finally:
        for f in tmp: f.unlink(missing_ok=True)
    for k, v in uit.items(): print(k, v)
    return uit


if __name__ == "__main__":
    render(sys.argv[1:])
