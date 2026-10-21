# -*- coding: utf-8 -*-
"""Deelkaart 'Hoelang duurt een tenniswedstrijd?' in de kaartstijl van preview-images-agent/kaart.py.
  ../superodd-agent/.venv/bin/python og_kaarten/tennis_duur.py <uit.png>"""
import sys, uuid, pathlib
sys.path.insert(0, "/Users/jaspervandenboogaard/bet-experts/preview-images-agent")
import kaart
from playwright.sync_api import sync_playwright

A = pathlib.Path(kaart.ASSETS)
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(__file__).parent / "tennis-duur.png")
BAL = "#D9F24B"
MAX = 6.0  # uur op de schaal

# (label, sub, van, tot, tekst)
RIJEN = [("Best of three", "ATP / WTA", 1.5, 2.0, "1u30 – 2u"),
         ("Grandslam vrouwen", "best of three", 0, 1.75, "± 1u45"),
         ("Grandslam mannen", "best of five", 0, 2.9, "± 2u54"),
         ("Grandslamfinale", "mannen, gem. 2022–26", 0, 3.47, "± 3u28"),
         ("Vijfsetter", "volle vijf sets", 4.0, 6.0, "4u – 6u")]


def balk(van, tot):
    l = van / MAX * 100; w = (tot - van) / MAX * 100
    cls = "rng" if van else "val"
    return f'<i class="{cls}" style="left:{l:.1f}%;width:{w:.1f}%"></i>'


rijen = "".join(
    f'<div class="r"><div class="l">{n}<span>{s}</span></div><div class="tr">{balk(v, t)}</div><div class="v">{x}</div></div>'
    for n, s, v, t, x in RIJEN)
ticks = "".join(f'<span style="left:{h / MAX * 100:.1f}%">{h}u</span>' for h in range(0, 7))

css = kaart.CSS + f"""
.eb{{font:700 14px 'Plus Jakarta Sans';letter-spacing:3px;color:#6CC08B;text-transform:uppercase}}
.tt{{font:800 54px/1.04 'Poppins';letter-spacing:-1.2px}}
.tt em{{font-style:normal;color:#2FD46E}}
.ball{{width:88px;height:88px;border-radius:50%;position:relative;overflow:hidden;flex:none;
  background:radial-gradient(circle at 34% 30%,#F1FF8A 0%,{BAL} 45%,#AFC92E 100%);
  box-shadow:0 14px 34px rgba(0,0,0,.45),0 0 0 6px rgba(217,242,75,.08)}}
.ball:before,.ball:after{{content:'';position:absolute;width:88px;height:88px;border-radius:50%;border:5px solid rgba(255,255,255,.92)}}
.ball:before{{left:-58px;top:0}} .ball:after{{right:-58px;top:0}}
.rec{{display:inline-flex;align-items:center;gap:12px;border-radius:18px;padding:14px 20px;
  background:rgba(232,196,107,.10);border:1px solid rgba(232,196,107,.40)}}
.rec .k{{font:700 12px 'Plus Jakarta Sans';letter-spacing:2px;color:#8A97A3;text-transform:uppercase}}
.rec .v{{font:800 30px 'Poppins';color:#E8C46B;line-height:1}}
.rec .s{{font:600 15px 'Plus Jakarta Sans';color:#C9D3DB}}
.pan{{border-radius:24px;padding:22px 24px 16px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.10)}}
.r{{display:grid;grid-template-columns:170px 1fr 82px;align-items:center;gap:14px;height:56px}}
.r .l{{font:700 15px/1.15 'Plus Jakarta Sans';color:#F5F9FA;white-space:nowrap}}
.r .l span{{display:block;font:600 12px 'Plus Jakarta Sans';color:#8A97A3}}
.tr{{position:relative;height:14px;border-radius:999px;background:rgba(255,255,255,.07)}}
.tr i{{position:absolute;top:0;bottom:0;border-radius:999px}}
.tr i.val{{background:linear-gradient(90deg,rgba(47,212,110,.35),#2FD46E)}}
.tr i.rng{{background:#2FD46E;box-shadow:0 0 0 3px rgba(47,212,110,.18)}}
.r .v{{font:800 16px 'Poppins';color:#F5F9FA;text-align:right;white-space:nowrap}}
.as{{position:relative;height:16px;margin:4px 96px 0 184px}}
.as span{{position:absolute;transform:translateX(-50%);font:600 11.5px 'Plus Jakarta Sans';color:#5E6B76}}
"""

body = f'''<div class="b">
  <div class="glow" style="width:760px;height:560px;left:-220px;top:-300px;background:rgba(22,154,71,.50)"></div>
  <div class="glow" style="width:520px;height:420px;right:-160px;top:-240px;background:rgba(217,242,75,.12)"></div>
  <div class="glow" style="width:600px;height:460px;right:-160px;bottom:-280px;background:rgba(22,154,71,.24)"></div>
  <img src="betexperts_logo.png" style="position:absolute;left:56px;top:44px;height:28px">
  <div style="position:absolute;right:56px;top:40px;display:flex;align-items:center;gap:10px">
    <span style="width:8px;height:8px;border-radius:50%;background:{BAL}"></span>
    <span style="font:700 15px 'Plus Jakarta Sans'">Tennis</span>
    <span style="font:600 13px 'Plus Jakarta Sans';color:#8A97A3">· Uitleg</span></div>

  <div style="position:absolute;left:56px;right:56px;top:132px;display:flex;gap:40px;align-items:center">
    <div style="flex:1;min-width:0">
      <div class="ball"></div>
      <div class="eb" style="margin-top:28px">Van snelle partij tot vijfsetter</div>
      <div class="tt" style="margin-top:12px">Hoelang duurt een <em>tenniswedstrijd?</em></div>
      <div class="rec" style="margin-top:28px">
        <div><div class="k">Record</div><div class="v">11u05</div></div>
        <div class="s">Isner – Mahut<br>Wimbledon 2010</div>
      </div>
    </div>
    <div style="width:540px;flex:none">
      <div class="pan">
        <div style="font:700 12px 'Plus Jakarta Sans';letter-spacing:2.5px;color:#8A97A3;text-transform:uppercase;margin-bottom:6px">Gemiddelde wedstrijdduur</div>
        {rijen}
        <div class="as">{ticks}</div>
      </div>
    </div>
  </div>

  <div style="position:absolute;left:56px;right:56px;bottom:52px;height:1px;background:rgba(255,255,255,.08)"></div>
  <div style="position:absolute;left:56px;bottom:20px;font-size:13px;color:#8A97A3">Wat kost gokken jou? Stop op tijd. 18+</div>
  <div style="position:absolute;right:56px;bottom:20px;font:700 13px 'Plus Jakarta Sans';color:#6CC08B">bet-experts.nl</div>
</div>'''

html = f"<!doctype html><html lang='nl'><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"
f = A / f".td-{uuid.uuid4().hex[:8]}.html"
f.write_text(html, encoding="utf-8")
try:
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--font-render-hinting=none"])
        pg = b.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=2)
        pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
        pg.screenshot(path=str(OUT))
        b.close()
finally:
    f.unlink(missing_ok=True)
print(OUT)
