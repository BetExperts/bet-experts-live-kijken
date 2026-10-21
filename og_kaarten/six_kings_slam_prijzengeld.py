# -*- coding: utf-8 -*-
"""Deelkaart 'Six Kings Slam prijzengeld 2026' in de kaartstijl van preview-images-agent/kaart.py.
  ../superodd-agent/.venv/bin/python og_kaarten/six_kings_slam_prijzengeld.py <uit.png>"""
import shutil, sys, uuid, pathlib
sys.path.insert(0, "/Users/jaspervandenboogaard/bet-experts/preview-images-agent")
import kaart
from playwright.sync_api import sync_playwright

HIER = pathlib.Path(__file__).parent
A = pathlib.Path(kaart.ASSETS)
LOGO = HIER / "sks-logo-breed.webp"
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else HIER / "sks-prijzengeld.png")
GOUD = "#E8C46B"

# winnaarsbedrag enkelspel in miljoen USD (ECB 20-10-2026 voor GBP/EUR/AUD)
RIJEN = [("Six Kings Slam", 6.0, "$6,0 mln", True), ("US Open", 5.5, "$5,5 mln", False),
         ("ATP Finals*", 5.07, "$5,1 mln", False), ("Wimbledon", 4.80, "$4,8 mln", False),
         ("Roland Garros", 3.14, "$3,1 mln", False), ("Australian Open", 2.90, "$2,9 mln", False)]
balken = "".join(
    f'<div class="r{" top" if t else ""}"><div class="l">{n}</div><div class="bar"><i style="width:{v / 6.0 * 100:.1f}%"></i></div>'
    f'<div class="v">{s}</div></div>' for n, v, s, t in RIJEN)

css = kaart.CSS + f"""
.gold{{position:absolute;border-radius:50%;filter:blur(110px)}}
.lt{{width:96px;height:96px;border-radius:24px;background:linear-gradient(160deg,#1A1610,#0F0D09);
  border:1.5px solid rgba(232,196,107,.55);box-shadow:0 0 0 5px rgba(232,196,107,.06),0 14px 32px rgba(0,0,0,.45);
  display:flex;align-items:center;justify-content:center;flex:none}}
.lt img{{width:76px;height:76px;object-fit:contain}}
.eb{{font:700 14px 'Plus Jakarta Sans';letter-spacing:3px;color:{GOUD};text-transform:uppercase}}
.tt{{font:800 40px/1.05 'Poppins';letter-spacing:-.8px}}
.big{{font:800 104px/1 'Poppins';letter-spacing:-3px;color:{GOUD}}}
.lab{{font:600 20px 'Plus Jakarta Sans';color:#C9D3DB}}
.lab b{{color:#F5F9FA}}
.ch{{display:inline-flex;align-items:center;gap:8px;border-radius:999px;padding:9px 16px;font:700 15px 'Plus Jakarta Sans';
  background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.10);color:#DDE4EA}}
.ch b{{font:800 16px 'Poppins';color:#F5F9FA}}
.ch.g{{background:#2FD46E;border-color:#2FD46E;color:#0B1117}} .ch.g b{{color:#0B1117}}
.pan{{border-radius:24px;padding:22px 24px 18px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.10)}}
.r{{display:grid;grid-template-columns:132px 1fr 84px;align-items:center;gap:12px;height:44px}}
.r .l{{font:700 15px 'Plus Jakarta Sans';color:#C9D3DB;white-space:nowrap}}
.r .bar{{height:14px;border-radius:999px;background:rgba(255,255,255,.07);overflow:hidden}}
.r .bar i{{display:block;height:100%;border-radius:999px;background:rgba(201,211,219,.55)}}
.r .v{{font:800 17px 'Poppins';color:#F5F9FA;text-align:right;white-space:nowrap}}
.r.top .l{{color:{GOUD}}} .r.top .bar i{{background:linear-gradient(90deg,#B8913A,{GOUD})}} .r.top .v{{color:{GOUD}}}
"""

body = f'''<div class="b">
  <div class="glow" style="width:760px;height:560px;left:-220px;top:-300px;background:rgba(22,154,71,.50)"></div>
  <div class="gold" style="width:620px;height:480px;right:-180px;top:-240px;background:rgba(232,196,107,.18)"></div>
  <div class="glow" style="width:600px;height:460px;right:-160px;bottom:-280px;background:rgba(22,154,71,.24)"></div>
  <img src="betexperts_logo.png" style="position:absolute;left:56px;top:44px;height:28px">
  <div style="position:absolute;right:56px;top:40px;display:flex;align-items:center;gap:10px">
    <span style="width:8px;height:8px;border-radius:50%;background:{GOUD}"></span>
    <span style="font:700 15px 'Plus Jakarta Sans'">Tennis</span>
    <span style="font:600 13px 'Plus Jakarta Sans';color:#8A97A3">· Riyad · 27–30 december</span></div>

  <div style="position:absolute;left:56px;right:56px;top:146px;display:flex;gap:40px;align-items:center">
    <div style="flex:1;min-width:0">
      <div class="eb">Prijzengeld 2026</div>
      <img src=".sks-logo.webp" style="display:block;height:76px;margin-top:16px;filter:drop-shadow(0 8px 24px rgba(232,196,107,.22))">
      <div class="big" style="margin-top:26px">$6 miljoen</div>
      <div class="lab" style="margin-top:12px">voor de winnaar · <b>± €5,35 miljoen</b></div>
      <div style="margin-top:26px;display:flex;gap:10px;flex-wrap:wrap">
        <span class="ch g">Startgeld <b>$1,5 mln</b> p.p.</span>
        <span class="ch">Pot <b>$13,5 mln</b></span>
        <span class="ch">Max. <b>3</b> duels</span>
      </div>
    </div>
    <div style="width:470px;flex:none">
      <div class="pan">
        <div style="font:700 12px 'Plus Jakarta Sans';letter-spacing:2.5px;color:#8A97A3;text-transform:uppercase;margin-bottom:8px">Winnaar enkelspel 2026 · in dollar</div>
        {balken}
        <div style="font:600 11.5px 'Plus Jakarta Sans';color:#5E6B76;margin-top:6px">*ATP Finals: bedrag 2025 · omgerekend tegen ECB-koers 20-10-2026</div>
      </div>
    </div>
  </div>

  <div style="position:absolute;left:56px;right:56px;bottom:52px;height:1px;background:rgba(255,255,255,.08)"></div>
  <div style="position:absolute;left:56px;bottom:20px;font-size:13px;color:#8A97A3">Wat kost gokken jou? Stop op tijd. 18+</div>
  <div style="position:absolute;right:56px;bottom:20px;font:700 13px 'Plus Jakarta Sans';color:#6CC08B">bet-experts.nl</div>
</div>'''

html = f"<!doctype html><html lang='nl'><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"
shutil.copy(LOGO, A / ".sks-logo.webp")
f = A / f".sks-{uuid.uuid4().hex[:8]}.html"
f.write_text(html, encoding="utf-8")
try:
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--font-render-hinting=none"])
        pg = b.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=2)
        pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
        pg.screenshot(path=str(OUT))
        b.close()
finally:
    f.unlink(missing_ok=True); (A / ".sks-logo.webp").unlink(missing_ok=True)
print(OUT)
