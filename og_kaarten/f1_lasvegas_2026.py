"""Deelkaart 'F1 GP Las Vegas 2026' (tijden + top 4 odds), kaartstijl kaart.py. Geen officieel F1-logo: tekstkop.
  ../superodd-agent/.venv/bin/python og_kaarten/f1_lasvegas_2026.py -> og/nieuws/nieuws-<slug>.webp"""
import io, sys, uuid, pathlib
sys.path.insert(0, "/Users/jaspervandenboogaard/bet-experts/preview-images-agent")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "specials"))
import kaart
import f1_lasvegas_2026 as M
from PIL import Image
from playwright.sync_api import sync_playwright

A = pathlib.Path(kaart.ASSETS)
OUT = pathlib.Path(__file__).resolve().parent.parent / "og" / "nieuws" / f"nieuws-{M.SLUG}.webp"
GOUD, GROEN = "#E8C46B", "#2FD46E"
odds = "".join(f'<div class="od"><span class="nm">{n}</span><span class="tm">{t}</span><span class="q">{f"{w:.2f}"}</span></div>'
               for n, t, w, _ in M.ODDS[:4])
css = kaart.CSS + f"""
.eb{{font:700 14px 'Plus Jakarta Sans';letter-spacing:3px;color:#6CC08B;text-transform:uppercase}}
.tt{{font:800 58px/1.02 'Poppins';letter-spacing:-1.6px}} .tt em{{font-style:normal;color:{GROEN}}}
.dt{{font:700 19px 'Plus Jakarta Sans';color:#C9D3DB}}
.chk{{width:54px;height:20px;border-radius:4px;opacity:.9;background:repeating-conic-gradient(#F5F9FA 0 25%, transparent 0 50%) 0 0/10px 10px}}
.tw{{display:flex;gap:12px}}
.tg{{flex:1;border-radius:18px;padding:14px 18px;background:rgba(255,255,255,.055);border:1px solid rgba(255,255,255,.10)}}
.tg.r{{background:linear-gradient(135deg,rgba(47,212,110,.22),rgba(22,154,71,.10));border:1.5px solid rgba(47,212,110,.65)}}
.tk{{font:700 12px 'Plus Jakarta Sans';letter-spacing:2px;color:#8A97A3;text-transform:uppercase}}
.tv{{font:800 34px/1.05 'Poppins';color:#F5F9FA;margin-top:4px}} .tl{{font:600 14px 'Plus Jakarta Sans';color:#C9D3DB;margin-top:2px}}
.ok{{font:700 12px 'Plus Jakarta Sans';letter-spacing:2.4px;color:#8A97A3;text-transform:uppercase;display:flex;justify-content:space-between}}
.od{{display:grid;grid-template-columns:1fr 120px 74px;align-items:center;height:50px;border-radius:14px;padding:0 10px 0 18px;
  background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.10)}}
.nm{{font:800 19px 'Poppins';color:#F5F9FA;white-space:nowrap}} .tm{{font:600 14px 'Plus Jakarta Sans';color:#8A97A3}}
.q{{font:800 20px 'Poppins';color:#0B1117;background:{GROEN};border-radius:10px;padding:3px 0;text-align:center}}
"""
body = f'''<div class="b">
  <div class="glow" style="width:760px;height:560px;left:-220px;top:-300px;background:rgba(22,154,71,.50)"></div>
  <div class="glow" style="width:560px;height:440px;right:-160px;top:-260px;background:rgba(232,196,107,.12)"></div>
  <img src="betexperts_logo.png" style="position:absolute;left:56px;top:44px;height:28px">
  <div style="position:absolute;left:56px;top:126px;width:470px">
    <div class="chk"></div>
    <div class="eb" style="margin-top:22px">Formule 1 · ronde 21 van 23</div>
    <div class="tt" style="margin-top:12px">GP Las Vegas <em>2026</em></div>
    <div class="dt" style="margin-top:14px">Las Vegas Strip Circuit · 50 ronden</div>
    <div class="dt" style="margin-top:6px">Live bij Viaplay</div>
  </div>
  <div class="col" style="position:absolute;right:56px;top:48px;width:560px;display:flex;flex-direction:column;gap:9px">
    <div class="tw">
      <div class="tg"><div class="tk">Kwalificatie</div><div class="tv">05:00</div><div class="tl">zaterdag 21 november</div></div>
      <div class="tg r"><div class="tk">Race</div><div class="tv">05:00</div><div class="tl">zondag 22 november</div></div>
    </div>
    <div class="ok" style="margin-top:8px"><span>Wie wint? Odds</span><span>Unibet</span></div>
    {odds}
  </div>
  <div style="position:absolute;left:56px;right:56px;bottom:52px;height:1px;background:rgba(255,255,255,.08)"></div>
  <div style="position:absolute;left:56px;bottom:20px;font-size:13px;color:#8A97A3">Wat kost gokken jou? Stop op tijd. 18+ · Nederlandse tijden</div>
  <div style="position:absolute;right:56px;bottom:20px;font:700 13px 'Plus Jakarta Sans';color:#6CC08B">bet-experts.nl</div>
</div>'''
CHECK = """(() => { const r = [];
  const lijn = [...document.querySelectorAll('.b > div')].find(d => d.style.height === '1px').getBoundingClientRect();
  const col = document.querySelector('.col').getBoundingClientRect();
  if (col.bottom > lijn.top - 8) r.push('kolom raakt footer');
  if (document.querySelector('.tt').getBoundingClientRect().right > col.left - 20) r.push('kop raakt kolom');
  return r; })()"""
html = f"<!doctype html><html lang='nl'><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"
f = A / f".lv-{uuid.uuid4().hex[:8]}.html"
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
