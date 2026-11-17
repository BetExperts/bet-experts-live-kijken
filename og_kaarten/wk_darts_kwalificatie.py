"""Deelkaart voor de WK-kwalificatie-artikelen (1200x630, nieuwe kaartstijl): dartbord-icoon, kop met de
spelersnaam, een opvallend blok met het tekort in ponden en de drie ranglijstregels die het verhaal dragen.
Data uit de artikelmodule zelf (KAART-dict in specials/<module>.py).
  ../superodd-agent/.venv/bin/python og_kaarten/wk_darts_kwalificatie.py <module> [uit.webp]"""
import io, sys, uuid, pathlib
sys.path.insert(0, "/Users/jaspervandenboogaard/bet-experts/preview-images-agent")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "specials"))
import importlib
import kaart
from PIL import Image
from playwright.sync_api import sync_playwright

MOD = sys.argv[1]
M = importlib.import_module(MOD)
K = M.KAART
A = pathlib.Path(kaart.ASSETS)
SP = pathlib.Path(__file__).resolve().parent.parent
rest = [a for a in sys.argv[2:] if not a.startswith("-")]
OUT = pathlib.Path(rest[0] if rest else SP / "og" / "nieuws" / f"nieuws-{M.SLUG}.webp")
G = "#2FD46E"; R = "#E5484D"

rijen = "".join(f'''<div class="w"><div class="lb">{l}</div><div class="vl">{v}</div><div class="nt">{n}</div></div>'''
                for l, v, n in K["regels"])

css = kaart.CSS + f"""
.tint{{position:absolute;border-radius:50%;filter:blur(120px)}}
.eb{{font:700 14px 'Plus Jakarta Sans';letter-spacing:3px;color:#6CC08B;text-transform:uppercase;white-space:nowrap}}
.kop{{font:800 46px/1.06 'Poppins';letter-spacing:-1.6px;color:#F5F9FA;max-width:560px}} .kop em{{font-style:normal;color:{G}}}
.crest{{width:104px;height:104px;border-radius:26px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);
  display:flex;align-items:center;justify-content:center;font-size:62px}}
.gap{{position:absolute;right:56px;top:96px;width:330px;padding:18px 24px;border-radius:22px;
  background:linear-gradient(160deg,rgba(229,72,77,.22),rgba(229,72,77,.05));border:1px solid rgba(229,72,77,.55)}}
.gap .l{{font:700 12px 'Plus Jakarta Sans';letter-spacing:2.4px;color:#FF8E91;text-transform:uppercase}}
.gap .bb{{margin-top:6px;display:flex;align-items:baseline;gap:12px}}
.gap .bb b{{font:800 52px/1 'Poppins';color:{R};letter-spacing:-2px}}
.gap .s{{margin-top:8px;font:600 14px/1.35 'Plus Jakarta Sans';color:#AEB9C2}}
.ph{{font:700 12px 'Plus Jakarta Sans';letter-spacing:2.4px;color:#8A97A3;text-transform:uppercase;white-space:nowrap}}
.w{{display:grid;grid-template-columns:400px 118px 1fr;align-items:center;gap:16px;height:60px;padding:0 20px;margin-bottom:10px;
  border-radius:16px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.10)}}
.lb{{font:700 18px 'Poppins';color:#F5F9FA;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.vl{{text-align:center;padding:8px 0;border-radius:11px;background:rgba(255,255,255,.10);color:#F5F9FA;font:800 17px 'Poppins'}}
.nt{{font:600 15px 'Plus Jakarta Sans';color:#AEB9C2;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
"""

body = f'''<div class="b">
  <div class="glow" style="width:760px;height:560px;left:-260px;top:-320px;background:rgba(22,154,71,.44)"></div>
  <div class="tint" style="width:620px;height:460px;right:-240px;top:-300px;background:rgba(229,72,77,.18)"></div>
  <div class="glow" style="width:640px;height:420px;left:300px;bottom:-340px;background:rgba(22,154,71,.16)"></div>
  <img src="betexperts_logo.png" style="position:absolute;left:56px;top:44px;height:28px">
  <div style="position:absolute;left:56px;top:100px;display:flex;align-items:center;gap:22px">
    <div class="crest">&#127919;</div>
    <div><div class="eb">{K["eyebrow"]}</div>
      <div class="kop" style="margin-top:10px">{K["kop"]}</div></div></div>
  <div class="gap"><div class="l">{K["gap_label"]}</div>
    <div class="bb"><b>{K["gap"]}</b></div>
    <div class="s">{K["gap_sub"]}</div></div>
  <div style="position:absolute;left:56px;right:56px;top:268px">
    <div style="display:flex;justify-content:space-between;margin-bottom:10px"><div class="ph">{K["kolom"]}</div>
      <div class="ph" style="letter-spacing:1.6px">{K.get("stand", "Stand 16 november")}</div></div>{rijen}</div>
  <div style="position:absolute;left:56px;right:56px;bottom:52px;height:1px;background:rgba(255,255,255,.08)"></div>
  <div style="position:absolute;left:56px;bottom:20px;font-size:13px;color:#8A97A3">Wat kost gokken jou? Stop op tijd. 18+</div>
  <div style="position:absolute;right:56px;bottom:20px;font:700 13px 'Plus Jakarta Sans';color:#6CC08B">bet-experts.nl</div>
</div>'''

CHECK_JS = """(() => { const r = []; const lijn = [...document.querySelectorAll('.b > div')].find(d => d.style.height === '1px').getBoundingClientRect();
  document.querySelectorAll('.w').forEach(el => { if (el.getBoundingClientRect().bottom > lijn.top - 6) r.push('raakt footer'); });
  document.querySelectorAll('.lb,.nt').forEach(el => { if (el.scrollWidth > el.clientWidth + 1) r.push('te lang: ' + el.textContent); });
  const kop = document.querySelector('.kop').getBoundingClientRect(), c = document.querySelector('.gap').getBoundingClientRect();
  if (kop.right > c.left - 16) r.push('kop raakt blok'); if (c.bottom > 268 - 8) r.push('blok raakt lijst');
  return r; })()"""

html = f"<!doctype html><html lang='nl'><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"
f = A / f".wkdk-{uuid.uuid4().hex[:8]}.html"
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
