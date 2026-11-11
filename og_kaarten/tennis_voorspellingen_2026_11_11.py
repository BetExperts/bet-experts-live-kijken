# -*- coding: utf-8 -*-
"""Deelkaart 'Tennis voorspellingen vandaag woensdag 11 november 2026' (ATP Stockholm + WTA Finals, 4 tips + combinatie) in de
kaartstijl van preview-images-agent/kaart.py. Compacte tipregels, omdat er vijf tips op moeten.
  ../superodd-agent/.venv/bin/python og_kaarten/tennis_voorspellingen_2026_11_11.py   -> og/nieuws/nieuws-<slug>.webp"""
import io, sys, uuid, pathlib
sys.path.insert(0, "/Users/jaspervandenboogaard/bet-experts/preview-images-agent")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "specials"))
import kaart
import tennis_voorspellingen_2026_11_11 as M
from PIL import Image
from playwright.sync_api import sync_playwright

A = pathlib.Path(kaart.ASSETS)
HIER = pathlib.Path(__file__).resolve().parent
OUT = HIER.parent / "og" / "nieuws" / f"nieuws-{M.SLUG}.webp"
BAL, GOUD = "#D9F24B", "#E8C46B"

# (toernooi, tijd, wedstrijd, tip, odd) in speelvolgorde
TIPS = [("Stockholm", "14:30", "Fritz – Norrie", "Fritz -2,5 games", "1.54"),
        ("Stockholm", "16:00", "Gojo – Humbert", "Gojo +3,5 games", "1.58"),
        ("WTA Finals", "21:00", "Muchova – Svitolina", "Muchova wint", "1.66"),
        ("WTA Finals", "±22:30", "Andreeva – Sabalenka", "Andreeva +2,5 games", "1.60")]

rijen = "".join(f'''<div class="tip"><div class="l"><div class="tn">{t} · {tijd}</div><div class="vs">{w}</div></div>
  <div class="r"><span class="wt">{tip}</span><span class="q">{o}</span></div></div>''' for t, tijd, w, tip, o in TIPS)

css = kaart.CSS + f"""
.eb{{font:700 14px 'Plus Jakarta Sans';letter-spacing:3px;color:#6CC08B;text-transform:uppercase}}
.tt{{font:800 58px/1.02 'Poppins';letter-spacing:-1.4px}}
.tt em{{font-style:normal;color:#2FD46E}}
.dt{{font:700 20px 'Plus Jakarta Sans';color:#C9D3DB}}
.ball{{width:76px;height:76px;border-radius:50%;position:relative;overflow:hidden;flex:none;
  background:radial-gradient(circle at 34% 30%,#F1FF8A 0%,{BAL} 45%,#AFC92E 100%);
  box-shadow:0 14px 34px rgba(0,0,0,.45),0 0 0 6px rgba(217,242,75,.08)}}
.ball:before,.ball:after{{content:'';position:absolute;width:76px;height:76px;border-radius:50%;border:5px solid rgba(255,255,255,.92)}}
.ball:before{{left:-51px;top:0}} .ball:after{{right:-51px;top:0}}
.chip{{display:inline-flex;align-items:center;gap:8px;height:36px;padding:0 15px;border-radius:999px;
  background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);font:700 14px 'Plus Jakarta Sans';color:#DDE4EA}}
.chip i{{width:7px;height:7px;border-radius:50%;background:{BAL}}}
.tip{{display:flex;justify-content:space-between;align-items:center;gap:14px;height:62px;border-radius:16px;padding:0 16px 0 18px;
  background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.10)}}
.tip .l{{min-width:0}}
.tn{{font:800 11px 'Poppins';letter-spacing:1.6px;color:#8A97A3;text-transform:uppercase}}
.vs{{margin-top:3px;font:800 19px 'Poppins';color:#F5F9FA;white-space:nowrap}}
.tip .r{{display:flex;align-items:center;gap:12px;flex:none}}
.wt{{font:700 14px 'Plus Jakarta Sans';color:#C9D3DB;white-space:nowrap}}
.q{{font:800 20px 'Poppins';color:#0B1117;background:#2FD46E;border-radius:10px;padding:2px 11px}}
.combi{{display:flex;justify-content:space-between;align-items:center;height:60px;border-radius:16px;padding:0 18px;
  background:rgba(232,196,107,.10);border:1px solid rgba(232,196,107,.42)}}
.combi .k{{font:700 12px 'Plus Jakarta Sans';letter-spacing:2px;color:{GOUD};text-transform:uppercase}}
.combi .s{{font:600 14px 'Plus Jakarta Sans';color:#C9D3DB;margin-top:2px}}
.combi .v{{font:800 32px 'Poppins';color:{GOUD};line-height:1}}
"""

body = f'''<div class="b">
  <div class="glow" style="width:760px;height:560px;left:-220px;top:-300px;background:rgba(22,154,71,.50)"></div>
  <div class="glow" style="width:520px;height:420px;right:-160px;top:-240px;background:rgba(217,242,75,.12)"></div>
  <div class="glow" style="width:600px;height:460px;right:-160px;bottom:-280px;background:rgba(22,154,71,.24)"></div>
  <img src="betexperts_logo.png" style="position:absolute;left:56px;top:44px;height:28px">
  <div style="position:absolute;left:56px;top:118px;width:470px">
    <div class="ball"></div>
    <div class="eb" style="margin-top:24px">ATP Stockholm · WTA Finals</div>
    <div class="tt" style="margin-top:12px">Tennis voorspellingen <em>vandaag</em></div>
    <div class="dt" style="margin-top:16px">Woensdag 11 november 2026</div>
    <div style="margin-top:20px;display:flex;gap:10px"><span class="chip"><i></i>Stockholm</span><span class="chip"><i></i>Indian Wells</span></div>
  </div>
  <div class="col" style="position:absolute;right:56px;top:44px;width:560px;display:flex;flex-direction:column;gap:8px">
    {rijen}
    <div class="combi"><div><div class="k">Combinatie</div><div class="s">Alle vier de tips · games: hele wedstrijd</div></div><div class="v">{M.COMBI.replace(",", ".")}</div></div>
  </div>
  <div style="position:absolute;left:56px;right:56px;bottom:52px;height:1px;background:rgba(255,255,255,.08)"></div>
  <div style="position:absolute;left:56px;bottom:20px;font-size:13px;color:#8A97A3">Wat kost gokken jou? Stop op tijd. 18+</div>
  <div style="position:absolute;right:56px;bottom:20px;font:700 13px 'Plus Jakarta Sans';color:#6CC08B">bet-experts.nl</div>
</div>'''

CHECK = """(() => { const r = [], b = document.querySelector('.b').getBoundingClientRect();
  const lijn = [...document.querySelectorAll('.b > div')].find(d => d.style.height === '1px').getBoundingClientRect();
  const col = document.querySelector('.col').getBoundingClientRect();
  if (col.bottom > lijn.top - 10) r.push('tips raken footer');
  document.querySelectorAll('.tip').forEach(t => { const l = t.querySelector('.l').getBoundingClientRect(), q = t.querySelector('.r').getBoundingClientRect();
    if (l.right > q.left - 8) r.push('tip te breed: ' + t.querySelector('.vs').textContent); });
  if (document.querySelector('.tt').getBoundingClientRect().right > col.left - 20) r.push('kop raakt tips');
  return r; })()"""

html = f"<!doctype html><html lang='nl'><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"
f = A / f".tv1111-{uuid.uuid4().hex[:8]}.html"
f.write_text(html, encoding="utf-8")
try:
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--font-render-hinting=none"])
        pg = b.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=2)
        pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
        fout = pg.evaluate(CHECK); png = pg.screenshot()
        b.close()
finally:
    f.unlink(missing_ok=True)
img = Image.open(io.BytesIO(png)).convert("RGB").resize((1200, 630), Image.LANCZOS)
img.save(OUT, "WEBP", quality=84, method=6)
print(OUT, f"{OUT.stat().st_size // 1024} KB", "| overloop:", fout or "geen")
