"""Deelkaart 'Pochettino naar Manchester United' (kaartstijl kaart.py, clublogo United uit og_kaarten/manutd-logo.png)."""
import io, sys, uuid, pathlib
sys.path.insert(0, "/Users/jaspervandenboogaard/bet-experts/preview-images-agent")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "specials"))
import kaart
import pochettino_united_2026 as M
from PIL import Image
from playwright.sync_api import sync_playwright
A = pathlib.Path(kaart.ASSETS); HIER = pathlib.Path(__file__).resolve().parent
OUT = HIER.parent / "og" / "nieuws" / f"nieuws-{M.SLUG}.webp"
LOGO = (HIER / "manutd-logo.png").as_uri()
G, R = "#2FD46E", "#DA291C"
(k1, v1), *rest = M.OG_RIJEN
rij = "".join(f'<div class="rw"><span class="k">{k}</span><span class="v">{v}</span></div>' for k, v in rest)
css = kaart.CSS + f"""
.eb{{font:700 14px 'Plus Jakarta Sans';letter-spacing:3px;color:#6CC08B;text-transform:uppercase}}
.tt{{font:800 58px/1.03 'Poppins';letter-spacing:-1.6px}} .tt em{{font-style:normal;color:{G}}}
.crest{{width:96px;height:96px;border-radius:24px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);display:flex;align-items:center;justify-content:center}}
.crest img{{width:70px;height:70px;object-fit:contain}}
.big{{border-radius:20px;padding:16px 22px;background:linear-gradient(135deg,rgba(218,41,28,.22),rgba(218,41,28,.06));border:1.5px solid rgba(218,41,28,.6)}}
.big .k{{font:700 12px 'Plus Jakarta Sans';letter-spacing:2px;color:#C9A9A6;text-transform:uppercase}} .big .v{{font:800 38px/1.05 'Poppins';color:#F5F9FA;margin-top:4px}}
.rw{{display:flex;justify-content:space-between;align-items:center;height:56px;border-radius:14px;padding:0 18px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.10)}}
.rw .k{{font:700 14px 'Plus Jakarta Sans';color:#8A97A3}} .rw .v{{font:800 18px 'Poppins';color:#F5F9FA;white-space:nowrap}}
"""
body = f'''<div class="b">
  <div class="glow" style="width:760px;height:560px;left:-220px;top:-300px;background:rgba(22,154,71,.45)"></div>
  <div class="glow" style="width:560px;height:440px;right:-160px;bottom:-260px;background:rgba(218,41,28,.20)"></div>
  <img src="betexperts_logo.png" style="position:absolute;left:56px;top:44px;height:28px">
  <div style="position:absolute;left:56px;top:118px;width:480px">
    <div class="crest"><img src="{LOGO}"></div>
    <div class="eb" style="margin-top:22px">{M.OG_EB}</div>
    <div class="tt" style="margin-top:12px">{M.OG_KOP}</div>
  </div>
  <div class="col" style="position:absolute;right:56px;top:84px;width:520px;display:flex;flex-direction:column;gap:10px">
    <div class="big"><div class="k">{k1}</div><div class="v">{v1}</div></div>{rij}
  </div>
  <div style="position:absolute;left:56px;right:56px;bottom:52px;height:1px;background:rgba(255,255,255,.08)"></div>
  <div style="position:absolute;left:56px;bottom:20px;font-size:13px;color:#8A97A3">Wat kost gokken jou? Stop op tijd. 18+</div>
  <div style="position:absolute;right:56px;bottom:20px;font:700 13px 'Plus Jakarta Sans';color:#6CC08B">bet-experts.nl</div>
</div>'''
CHECK = """(() => { const r=[]; const l=[...document.querySelectorAll('.b > div')].find(d=>d.style.height==='1px').getBoundingClientRect();
 const c=document.querySelector('.col').getBoundingClientRect(); if(c.bottom>l.top-8) r.push('kolom raakt footer');
 if(document.querySelector('.tt').getBoundingClientRect().right>c.left-20) r.push('kop raakt kolom');
 document.querySelectorAll('img').forEach(i=>{ if(!i.naturalWidth) r.push('img niet geladen '+i.src.slice(-30)); }); return r; })()"""
html = f"<!doctype html><html lang='nl'><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"
f = A / f".poch-{uuid.uuid4().hex[:8]}.html"; f.write_text(html, encoding="utf-8")
try:
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--font-render-hinting=none", "--allow-file-access-from-files"]); pg = b.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=2)
        pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(400); fout = pg.evaluate(CHECK); png = pg.screenshot(); b.close()
finally:
    f.unlink(missing_ok=True)
Image.open(io.BytesIO(png)).convert("RGB").resize((1200, 630), Image.LANCZOS).save(OUT, "WEBP", quality=84, method=6)
print(OUT.name, "| overloop:", fout or "geen")
