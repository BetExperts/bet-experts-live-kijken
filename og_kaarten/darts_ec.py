"""Deelkaart 'Darts vandaag' (1200x630, nieuwe kaartstijl): darts-icoon, kop, de vier wedtips per wedstrijd (tijd, spelers,
tip, odd) en de combinatie. Data uit specials/darts_ec_kwartfinales_2026.py (TIPS, INZET, UITBETALING, SLUG).
  ../superodd-agent/.venv/bin/python og_kaarten/darts_ec.py [uit.webp]"""
import io, sys, uuid, pathlib
sys.path.insert(0, "/Users/jaspervandenboogaard/bet-experts/preview-images-agent")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "specials"))
import kaart
import darts_ec_kwartfinales_2026 as M
from PIL import Image
from playwright.sync_api import sync_playwright

A = pathlib.Path(kaart.ASSETS)
SP = pathlib.Path(__file__).resolve().parent.parent
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else SP / "og" / "nieuws" / f"nieuws-{M.SLUG}.webp")
G = "#2FD46E"; R = "#E5484D"
q = lambda x: f"{x:.2f}".replace(".", ",")

rijen = "".join(f'''<div class="w"><div class="tm">{t}</div><div class="sp">{s1} <i>–</i> {s2}</div>
  <div class="tip">{tip}</div><div class="od">{q(o)}</div></div>''' for t, s1, s2, tip, o in M.TIPS)

css = kaart.CSS + f"""
.tint{{position:absolute;border-radius:50%;filter:blur(120px)}}
.eb{{font:700 14px 'Plus Jakarta Sans';letter-spacing:3px;color:#6CC08B;text-transform:uppercase;white-space:nowrap}}
.kop{{font:800 58px/1.0 'Poppins';letter-spacing:-2px;color:#F5F9FA}} .kop em{{font-style:normal;color:{G}}}
.crest{{width:104px;height:104px;border-radius:26px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);
  display:flex;align-items:center;justify-content:center;font-size:62px}}
.combo{{position:absolute;right:56px;top:92px;width:360px;padding:16px 22px;border-radius:22px;
  background:linear-gradient(160deg,rgba(47,212,110,.20),rgba(47,212,110,.05));border:1px solid rgba(47,212,110,.55)}}
.combo .l{{font:700 12px 'Plus Jakarta Sans';letter-spacing:2.4px;color:{G};text-transform:uppercase}}
.combo .bb{{margin-top:8px;display:flex;align-items:baseline;gap:12px}}
.combo .bb b{{font:800 46px/1 'Poppins';color:{G};letter-spacing:-1px}} .combo .bb span{{font:600 15px 'Plus Jakarta Sans';color:#AEB9C2}}
.combo .s{{margin-top:6px;font:600 14px 'Plus Jakarta Sans';color:#AEB9C2}}
.ph{{font:700 12px 'Plus Jakarta Sans';letter-spacing:2.4px;color:#8A97A3;text-transform:uppercase;white-space:nowrap}}
.w{{display:grid;grid-template-columns:72px 330px 1fr 82px;align-items:center;gap:14px;height:58px;padding:0 18px;margin-bottom:9px;
  border-radius:16px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.10)}}
.tm{{font:800 18px 'Poppins';color:#F5F9FA}}
.sp{{font:700 18px 'Poppins';color:#F5F9FA;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}} .sp i{{font-style:normal;color:#8A97A3}}
.tip{{font:600 15px 'Plus Jakarta Sans';color:#DDE4EA;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.od{{text-align:center;padding:8px 0;border-radius:11px;background:rgba(47,212,110,.16);color:{G};font:800 17px 'Poppins'}}
"""

body = f'''<div class="b">
  <div class="glow" style="width:760px;height:560px;left:-260px;top:-320px;background:rgba(22,154,71,.48)"></div>
  <div class="tint" style="width:620px;height:460px;right:-240px;top:-300px;background:rgba(229,72,77,.16)"></div>
  <div class="glow" style="width:640px;height:420px;left:300px;bottom:-340px;background:rgba(22,154,71,.18)"></div>
  <img src="betexperts_logo.png" style="position:absolute;left:56px;top:44px;height:28px">
  <div style="position:absolute;left:56px;top:100px;display:flex;align-items:center;gap:22px">
    <div class="crest">🎯</div>
    <div><div class="eb">European Championship · kwartfinales</div>
      <div class="kop" style="margin-top:10px">Darts <em>vandaag</em></div></div></div>
  <div class="combo"><div class="l">Combinatie van de 4 tips</div>
    <div class="bb"><b>€{q(M.UITBETALING)}</b><span>bij €{M.INZET} inzet</span></div>
    <div class="s">Bet365 · zondag 25 oktober · Dortmund</div></div>
  <div style="position:absolute;left:56px;right:56px;top:256px">
    <div style="display:flex;justify-content:space-between;margin-bottom:10px"><div class="ph">Onze wedtips (Nederlandse tijd)</div>
      <div class="ph" style="letter-spacing:1.6px">Odd</div></div>{rijen}</div>
  <div style="position:absolute;left:56px;right:56px;bottom:52px;height:1px;background:rgba(255,255,255,.08)"></div>
  <div style="position:absolute;left:56px;bottom:20px;font-size:13px;color:#8A97A3">Wat kost gokken jou? Stop op tijd. 18+</div>
  <div style="position:absolute;right:56px;bottom:20px;font:700 13px 'Plus Jakarta Sans';color:#6CC08B">bet-experts.nl</div>
</div>'''

CHECK_JS = """(() => { const r = []; const lijn = [...document.querySelectorAll('.b > div')].find(d => d.style.height === '1px').getBoundingClientRect();
  document.querySelectorAll('.w').forEach(el => { if (el.getBoundingClientRect().bottom > lijn.top - 6) r.push('raakt footer'); });
  document.querySelectorAll('.sp,.tip').forEach(el => { if (el.scrollWidth > el.clientWidth + 1) r.push('te lang: ' + el.textContent); });
  const kop = document.querySelector('.kop').getBoundingClientRect(), c = document.querySelector('.combo').getBoundingClientRect();
  if (kop.right > c.left - 16) r.push('kop raakt combo'); if (c.bottom > 256 - 8) r.push('combo raakt lijst');
  return r; })()"""

html = f"<!doctype html><html lang='nl'><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"
f = A / f".darts-{uuid.uuid4().hex[:8]}.html"
f.write_text(html, encoding="utf-8")
try:
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--font-render-hinting=none", "--allow-file-access-from-files"])
        pg = b.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=2)
        pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(400)
        fouten = pg.evaluate(CHECK_JS); png = pg.screenshot(); b.close()
finally:
    f.unlink(missing_ok=True)
OUT.parent.mkdir(parents=True, exist_ok=True)
img = Image.open(io.BytesIO(png)).convert("RGB")
if OUT.suffix.lower() == ".webp":
    img.resize((1200, 630), Image.LANCZOS).save(OUT, "WEBP", quality=84, method=6)
else:
    img.save(OUT, "JPEG", quality=92)
print(OUT, "| overloop:", fouten or "geen")
