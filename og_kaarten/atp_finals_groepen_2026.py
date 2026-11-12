"""Deelkaart 'ATP Finals 2026: de groepen' (McEnroe + Lendl) in de kaartstijl van kaart.py.
  ../superodd-agent/.venv/bin/python og_kaarten/atp_finals_groepen_2026.py  -> og/nieuws/nieuws-<slug>.webp"""
import io, sys, uuid, pathlib
sys.path.insert(0, "/Users/jaspervandenboogaard/bet-experts/preview-images-agent")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "specials"))
import kaart
import atp_finals_groepen_2026 as M
from PIL import Image
from playwright.sync_api import sync_playwright

A = pathlib.Path(kaart.ASSETS)
OUT = pathlib.Path(__file__).resolve().parent.parent / "og" / "nieuws" / f"nieuws-{M.SLUG}.webp"
BAL = "#D9F24B"


def blok(naam, rijen):
    r = "".join(f'<div class="sp"><span class="sd">{s}</span><span class="nm">{n}</span></div>' for s, n, *_ in rijen)
    return f'<div class="gr"><div class="gk">{naam}</div>{r}</div>'


css = kaart.CSS + f"""
.eb{{font:700 14px 'Plus Jakarta Sans';letter-spacing:3px;color:#6CC08B;text-transform:uppercase}}
.tt{{font:800 60px/1.02 'Poppins';letter-spacing:-1.6px}} .tt em{{font-style:normal;color:#2FD46E}}
.dt{{font:700 20px 'Plus Jakarta Sans';color:#C9D3DB}}
.ball{{width:76px;height:76px;border-radius:50%;position:relative;overflow:hidden;
  background:radial-gradient(circle at 34% 30%,#F1FF8A 0%,{BAL} 45%,#AFC92E 100%);box-shadow:0 14px 34px rgba(0,0,0,.45)}}
.ball:before,.ball:after{{content:'';position:absolute;width:76px;height:76px;border-radius:50%;border:5px solid rgba(255,255,255,.92)}}
.ball:before{{left:-51px;top:0}} .ball:after{{right:-51px;top:0}}
.gr{{border-radius:18px;padding:16px 20px 12px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.10)}}
.gk{{font:800 13px 'Poppins';letter-spacing:2px;color:#2FD46E;text-transform:uppercase;margin-bottom:8px}}
.sp{{display:flex;align-items:center;gap:14px;height:42px;border-top:1px solid rgba(255,255,255,.06)}}
.sd{{width:30px;height:30px;border-radius:9px;background:rgba(47,212,110,.16);color:#2FD46E;font:800 15px 'Poppins';
  display:flex;align-items:center;justify-content:center}}
.nm{{font:800 21px 'Poppins';color:#F5F9FA;white-space:nowrap}}
"""
body = f'''<div class="b">
  <div class="glow" style="width:760px;height:560px;left:-220px;top:-300px;background:rgba(22,154,71,.50)"></div>
  <div class="glow" style="width:600px;height:460px;right:-160px;bottom:-280px;background:rgba(22,154,71,.24)"></div>
  <img src="betexperts_logo.png" style="position:absolute;left:56px;top:44px;height:28px">
  <div style="position:absolute;left:56px;top:124px;width:440px">
    <div class="ball"></div>
    <div class="eb" style="margin-top:24px">Nitto ATP Finals · Turijn</div>
    <div class="tt" style="margin-top:12px">ATP Finals 2026: <em>de groepen</em></div>
    <div class="dt" style="margin-top:16px">15 t/m 22 november · Inalpi Arena</div>
  </div>
  <div class="col" style="position:absolute;right:56px;top:56px;width:600px;display:flex;flex-direction:column;gap:14px">
    {blok("John McEnroe Group", M.MCENROE)}
    {blok("Ivan Lendl Group", M.LENDL)}
  </div>
  <div style="position:absolute;left:56px;right:56px;bottom:52px;height:1px;background:rgba(255,255,255,.08)"></div>
  <div style="position:absolute;left:56px;bottom:20px;font-size:13px;color:#8A97A3">Wat kost gokken jou? Stop op tijd. 18+</div>
  <div style="position:absolute;right:56px;bottom:20px;font:700 13px 'Plus Jakarta Sans';color:#6CC08B">bet-experts.nl</div>
</div>'''
CHECK = """(() => { const r = [];
  const lijn = [...document.querySelectorAll('.b > div')].find(d => d.style.height === '1px').getBoundingClientRect();
  const col = document.querySelector('.col').getBoundingClientRect();
  if (col.bottom > lijn.top - 8) r.push('groepen raken footer');
  if (document.querySelector('.tt').getBoundingClientRect().right > col.left - 20) r.push('kop raakt groepen');
  return r; })()"""
html = f"<!doctype html><html lang='nl'><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"
f = A / f".atpgr-{uuid.uuid4().hex[:8]}.html"
f.write_text(html, encoding="utf-8")
try:
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--font-render-hinting=none"])
        pg = b.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=2)
        pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
        fout = pg.evaluate(CHECK); png = pg.screenshot(); b.close()
finally:
    f.unlink(missing_ok=True)
img = Image.open(io.BytesIO(png)).convert("RGB").resize((1200, 630), Image.LANCZOS)
img.save(OUT, "WEBP", quality=84, method=6)
print(OUT, f"{OUT.stat().st_size // 1024} KB", "| overloop:", fout or "geen")
