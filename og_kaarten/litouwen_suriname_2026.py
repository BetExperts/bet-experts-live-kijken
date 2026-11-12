"""Deelkaart 'Litouwen – Suriname live kijken' (kaartstijl kaart.py)."""
import io, sys, uuid, pathlib
sys.path.insert(0, "/Users/jaspervandenboogaard/bet-experts/preview-images-agent")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "specials"))
import kaart
import litouwen_suriname_2026 as M
from PIL import Image
from playwright.sync_api import sync_playwright
A = pathlib.Path(kaart.ASSETS)
OUT = pathlib.Path(__file__).resolve().parent.parent / "og" / "nieuws" / f"nieuws-{M.SLUG}.webp"
G = "#2FD46E"
rij = lambda k, v: f'<div class="rw"><span class="k">{k}</span><span class="v">{v}</span></div>'
css = kaart.CSS + f"""
.eb{{font:700 14px 'Plus Jakarta Sans';letter-spacing:3px;color:#6CC08B;text-transform:uppercase}}
.tt{{font:800 56px/1.04 'Poppins';letter-spacing:-1.5px}} .tt em{{font-style:normal;color:{G}}}
.dt{{font:700 19px 'Plus Jakarta Sans';color:#C9D3DB}}
.big{{border-radius:20px;padding:16px 22px;background:linear-gradient(135deg,rgba(47,212,110,.22),rgba(22,154,71,.10));border:1.5px solid rgba(47,212,110,.65)}}
.big .k{{font:700 12px 'Plus Jakarta Sans';letter-spacing:2px;color:#8A97A3;text-transform:uppercase}}
.big .v{{font:800 40px/1.05 'Poppins';color:#F5F9FA;margin-top:4px}} .big .s{{font:600 15px 'Plus Jakarta Sans';color:#C9D3DB}}
.rw{{display:flex;justify-content:space-between;align-items:center;height:54px;border-radius:14px;padding:0 18px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.10)}}
.rw .k{{font:700 14px 'Plus Jakarta Sans';color:#8A97A3}} .rw .v{{font:800 18px 'Poppins';color:#F5F9FA;white-space:nowrap}}
"""
body = f'''<div class="b">
  <div class="glow" style="width:760px;height:560px;left:-220px;top:-300px;background:rgba(22,154,71,.50)"></div>
  <img src="betexperts_logo.png" style="position:absolute;left:56px;top:44px;height:28px">
  <div style="position:absolute;left:56px;top:150px;width:470px">
    <div class="eb">Oefeninterland · live kijken</div>
    <div class="tt" style="margin-top:14px">Litouwen – Suriname <em>live kijken</em></div>
    <div class="dt" style="margin-top:16px">S. Darius en S. Girėnas-stadion, Kaunas</div>
  </div>
  <div class="col" style="position:absolute;right:56px;top:56px;width:540px;display:flex;flex-direction:column;gap:10px">
    <div class="big"><div class="k">Aftrap</div><div class="v">18:00 uur</div><div class="s">donderdag 12 november · Nederlandse tijd</div></div>
    {rij("Nederlandse tv", "Niet te zien")}
    {rij("Stream", "LRT.lt (mogelijk geblokkeerd)")}
    {rij("Live volgen", "Live-tracker Bet365")}
    {rij("Odds 1 · X · 2", "2.85 · 3.10 · 2.50")}
  </div>
  <div style="position:absolute;left:56px;right:56px;bottom:52px;height:1px;background:rgba(255,255,255,.08)"></div>
  <div style="position:absolute;left:56px;bottom:20px;font-size:13px;color:#8A97A3">Wat kost gokken jou? Stop op tijd. 18+</div>
  <div style="position:absolute;right:56px;bottom:20px;font:700 13px 'Plus Jakarta Sans';color:#6CC08B">bet-experts.nl</div>
</div>'''
CHECK = """(() => { const r=[]; const l=[...document.querySelectorAll('.b > div')].find(d=>d.style.height==='1px').getBoundingClientRect();
 const c=document.querySelector('.col').getBoundingClientRect(); if(c.bottom>l.top-8) r.push('kolom raakt footer');
 if(document.querySelector('.tt').getBoundingClientRect().right>c.left-20) r.push('kop raakt kolom'); return r; })()"""
html = f"<!doctype html><html lang='nl'><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"
f = A / f".ltsr-{uuid.uuid4().hex[:8]}.html"; f.write_text(html, encoding="utf-8")
try:
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--font-render-hinting=none"]); pg = b.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=2)
        pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300); fout = pg.evaluate(CHECK); png = pg.screenshot(); b.close()
finally:
    f.unlink(missing_ok=True)
Image.open(io.BytesIO(png)).convert("RGB").resize((1200, 630), Image.LANCZOS).save(OUT, "WEBP", quality=84, method=6)
print(OUT, "| overloop:", fout or "geen")
