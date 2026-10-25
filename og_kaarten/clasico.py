"""Deelkaart 'Wie wint El Clásico?' (1200x630, nieuwe kaartstijl): logo's Barcelona en Real Madrid, kop, de winkansen
volgens de odds als balk, de onderlinge balans en de wedtip. Data uit specials/clasico_barcelona_real_2026_10_25.py.
Logo's: og_kaarten/team-529.png (Barcelona) en team-541.png (Real Madrid), lokale kopieën van media.api-sports.io.
  ../superodd-agent/.venv/bin/python og_kaarten/clasico.py [uit.webp] -> og/nieuws/nieuws-<slug>.webp"""
import io, sys, uuid, pathlib
sys.path.insert(0, "/Users/jaspervandenboogaard/bet-experts/preview-images-agent")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "specials"))
import kaart
import clasico_barcelona_real_2026_10_25 as M
from PIL import Image
from playwright.sync_api import sync_playwright

A = pathlib.Path(kaart.ASSETS)
HIER = pathlib.Path(__file__).resolve().parent
SP = HIER.parent
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else SP / "og" / "nieuws" / f"nieuws-{M.SLUG}.webp")
BAR, RMA = (HIER / "team-529.png").as_uri(), (HIER / "team-541.png").as_uri()
GROEN, BLAUW, GOUD = "#2FD46E", "#3D6FE0", "#E8C46A"
KB, KG, KR = M.KANS_B, M.KANS_G, M.KANS_R

css = kaart.CSS + f"""
.tint{{position:absolute;border-radius:50%;filter:blur(120px)}}
.eb{{font:700 14px 'Plus Jakarta Sans';letter-spacing:3px;color:#6CC08B;text-transform:uppercase;white-space:nowrap}}
.kop{{font:800 60px/1.0 'Poppins';letter-spacing:-2px;color:#F5F9FA}}
.kop em{{font-style:normal;color:{GROEN}}}
.crest{{width:96px;height:96px;border-radius:24px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);
  display:flex;align-items:center;justify-content:center}}
.crest img{{width:68px;height:68px;object-fit:contain}}
.vs{{font:800 22px 'Poppins';color:#8A97A3}}
.bt{{position:absolute;right:56px;top:92px;width:432px;padding:18px 24px;border-radius:22px;
  background:linear-gradient(160deg,rgba(47,212,110,.20),rgba(47,212,110,.05));border:1px solid rgba(47,212,110,.55)}}
.bt .l{{font:700 12px 'Plus Jakarta Sans';letter-spacing:2.4px;color:{GROEN};text-transform:uppercase}}
.bt .tip{{margin-top:10px;font:800 26px/1.15 'Poppins';color:#F5F9FA;letter-spacing:-.5px}}
.bt .wd{{margin-top:6px;font:600 14px 'Plus Jakarta Sans';color:#AEB9C2}}
.bt .rg{{margin-top:10px;display:flex;align-items:baseline;gap:16px}}
.bt .rg b{{font:800 40px/1 'Poppins';color:{GROEN}}}
.bt .rg span{{font:600 14px 'Plus Jakarta Sans';color:#AEB9C2}}
.ph{{font:700 12px 'Plus Jakarta Sans';letter-spacing:2.4px;color:#8A97A3;text-transform:uppercase;white-space:nowrap}}
.bar{{display:flex;height:58px;border-radius:16px;overflow:hidden;border:1px solid rgba(255,255,255,.10)}}
.bar div{{display:flex;align-items:center;justify-content:space-between;padding:0 18px;font:800 20px 'Poppins';color:#F5F9FA;white-space:nowrap}}
.bar span{{font:600 14px 'Plus Jakarta Sans';color:rgba(245,249,250,.85)}}
.ft{{display:flex;flex-direction:column;justify-content:center;gap:6px;height:74px;padding:0 18px;border-radius:18px;
  background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.10)}}
.ft b{{font:800 28px/1 'Poppins';color:#F5F9FA;letter-spacing:-.5px}}
.ft span{{font:600 13px 'Plus Jakarta Sans';color:#8A97A3;white-space:nowrap}}
"""

body = f'''<div class="b">
  <div class="glow" style="width:760px;height:560px;left:-260px;top:-320px;background:rgba(22,154,71,.48)"></div>
  <div class="tint" style="width:600px;height:460px;right:-240px;top:-300px;background:rgba(61,111,224,.20)"></div>
  <div class="glow" style="width:640px;height:420px;left:300px;bottom:-340px;background:rgba(22,154,71,.18)"></div>
  <img src="betexperts_logo.png" style="position:absolute;left:56px;top:44px;height:28px">
  <div style="position:absolute;left:56px;top:100px;display:flex;align-items:center;gap:14px">
    <div class="crest"><img src="{BAR}"></div><div class="vs">vs</div><div class="crest"><img src="{RMA}"></div>
  </div>
  <div style="position:absolute;left:56px;top:216px">
    <div class="eb">La Liga · zo 25 okt · 21:00</div>
    <div class="kop" style="margin-top:10px">Wie wint<br><em>El Clásico?</em></div>
  </div>
  <div class="bt"><div class="l">Onze wedtip</div><div class="tip">Minder dan 14,5<br>schoten op doel</div>
    <div class="wd">Barcelona – Real Madrid · Bet365</div>
    <div class="rg"><b>@1,86</b><span>Onze kans: 60%</span></div></div>
  <div style="position:absolute;right:56px;top:334px;width:480px;display:flex;gap:12px">
    <div class="ft" style="flex:1"><b>106-52-106</b><span>Onderlinge balans (officieel)</span></div>
    <div class="ft" style="width:170px"><b>6 / 10</b><span>Laatste 10 voor Barça</span></div>
  </div>
  <div style="position:absolute;left:56px;right:56px;top:444px">
    <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:12px">
      <div class="ph">Winkans volgens de odds</div><div class="ph" style="letter-spacing:1.6px">15 Nederlandse bookmakers</div></div>
    <div class="bar">
      <div style="width:{KB}%;background:linear-gradient(90deg,rgba(165,0,68,.85),rgba(0,77,152,.85))">Barcelona<span>{KB}%</span></div>
      <div style="width:{KG}%;background:rgba(255,255,255,.12)">Gelijk<span>{KG}%</span></div>
      <div style="width:{KR}%;background:linear-gradient(90deg,rgba(232,196,106,.55),rgba(232,196,106,.30))">Real<span>{KR}%</span></div>
    </div>
  </div>
  <div style="position:absolute;left:56px;right:56px;bottom:52px;height:1px;background:rgba(255,255,255,.08)"></div>
  <div style="position:absolute;left:56px;bottom:20px;font-size:13px;color:#8A97A3">Wat kost gokken jou? Stop op tijd. 18+</div>
  <div style="position:absolute;right:56px;bottom:20px;font:700 13px 'Plus Jakarta Sans';color:#6CC08B">bet-experts.nl</div>
</div>'''

CHECK_JS = """(() => { const r = []; const b = document.querySelector('.b').getBoundingClientRect();
  const lijn = [...document.querySelectorAll('.b > div')].find(d => d.style.height === '1px').getBoundingClientRect();
  document.querySelectorAll('.b *').forEach(el => { if (el.classList.contains('glow') || el.classList.contains('tint')) return;
    const q = el.getBoundingClientRect(); if (q.width && (q.right > b.right - 40 || q.bottom > b.bottom + 1)) r.push('buiten:' + el.className);
    if (el.parentElement && el.parentElement.classList.contains('bar') && el.scrollWidth > el.clientWidth + 1) r.push('balk te smal:' + el.textContent);
    if (el.classList.contains('bar') && q.bottom > lijn.top - 10) r.push('raakt footer'); });
  const kop = document.querySelector('.kop').getBoundingClientRect(), bt = document.querySelector('.bt').getBoundingClientRect();
  if (kop.right > bt.left - 20) r.push('kop raakt tip'); const ft = document.querySelector('.ft').getBoundingClientRect();
  if (bt.bottom > ft.top - 8) r.push('tip raakt feiten'); if (ft.bottom > 444 - 12) r.push('feiten raken balk');
  document.querySelectorAll('img').forEach(i => { if (!i.complete || !i.naturalWidth) r.push('img niet geladen ' + i.src.slice(-20)); });
  return r; })()"""

html = f"<!doctype html><html lang='nl'><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"
f = A / f".clasico-{uuid.uuid4().hex[:8]}.html"
f.write_text(html, encoding="utf-8")
try:
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--font-render-hinting=none", "--allow-file-access-from-files"])
        pg = b.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=2)
        pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(400)
        fouten = pg.evaluate(CHECK_JS)
        png = pg.screenshot()
        b.close()
finally:
    f.unlink(missing_ok=True)
OUT.parent.mkdir(parents=True, exist_ok=True)
img = Image.open(io.BytesIO(png)).convert("RGB")
if OUT.suffix.lower() == ".webp":
    img = img.resize((1200, 630), Image.LANCZOS)
    img.save(OUT, "WEBP", quality=84, method=6)
else:
    img.save(OUT)
print(OUT, img.size, f"{OUT.stat().st_size // 1024} KB", "| overloop:", fouten or "geen")
