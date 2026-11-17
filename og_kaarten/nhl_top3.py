"""Deelkaart 'NHL: 3 beste wedtips vannacht' (1200x630, nieuwe kaartstijl): NHL-logo, kop, tegel met de kernfeiten
(3 tips, combi-odd, score van gisteren) en per tip een rij met beide teamlogo's, aanvangstijd, de tip en de odd.
Data uit specials/<module>.py (TOP3, OG_EYEBROW_DATUM, SLUG). Logo's: og_kaarten/nhl-<abbr>.png (ESPN teamlogo's, lokaal).
  ../superodd-agent/.venv/bin/python og_kaarten/nhl_top3.py <module> [uit.webp] -> og/nieuws/nieuws-<slug>.webp"""
import io, sys, uuid, pathlib, importlib
sys.path.insert(0, "/Users/jaspervandenboogaard/bet-experts/preview-images-agent")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "specials"))
import kaart
from PIL import Image
from playwright.sync_api import sync_playwright

M = importlib.import_module(sys.argv[1])
A = pathlib.Path(kaart.ASSETS)
HIER = pathlib.Path(__file__).resolve().parent
OUT = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else HIER.parent / "og" / "nieuws" / f"nieuws-{M.SLUG}.webp")
GROEN = "#2FD46E"
LIGA = getattr(M, "OG_LIGA", "nhl")   # ook voor NBA: OG_LIGA = "nba", OG_SPORT = "Basketbal" (logo's nba-<abbr>.png)
logo = lambda a: (HIER / f"{LIGA}-{a}.png").as_uri()
combi = 1.0
for t in M.TOP3:
    combi *= float(t[6].replace(",", "."))
EXTRA = getattr(M, "OG_EXTRA", ("Combi-odd", f"{combi:.2f}".replace(".", ",")))
GISTEREN = getattr(M, "OG_GISTEREN", ("Tips vannacht", str(len(M.TOP3))))   # bv. ("Gisteren raak", "3/3")


def rij(i, w):
    t, h, ha, u, ua, tip, odd, kans = w
    return (f'<div class="w"><div class="nr">{i}</div><div class="tm">{t}</div>'
            f'<div class="tt"><img src="{logo(ha)}"><span>{h}</span><i>–</i><span>{u}</span><img src="{logo(ua)}"></div>'
            f'<div class="tip">{tip}</div><div class="od">@{odd}</div></div>')


css = kaart.CSS + f"""
.ijs{{position:absolute;border-radius:50%;filter:blur(120px)}}
.eb{{font:700 14px 'Plus Jakarta Sans';letter-spacing:3px;color:#6CC08B;text-transform:uppercase;white-space:nowrap}}
.kop{{font:800 56px/1.0 'Poppins';letter-spacing:-2px;color:#F5F9FA}} .kop em{{font-style:normal;color:{GROEN}}}
.crest{{width:104px;height:104px;border-radius:26px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);
  display:flex;align-items:center;justify-content:center}} .crest img{{width:74px;height:74px;object-fit:contain}}
.bt{{position:absolute;right:56px;top:104px;width:360px;display:flex;gap:12px}}
.st{{flex:1;padding:18px 18px 16px;border-radius:20px;background:linear-gradient(160deg,rgba(47,212,110,.20),rgba(47,212,110,.05));
  border:1px solid rgba(47,212,110,.55)}} .st.g{{background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.12)}}
.st .l{{font:700 11px 'Plus Jakarta Sans';letter-spacing:2px;color:#8A97A3;text-transform:uppercase;white-space:nowrap}}
.st b{{display:block;margin-top:8px;font:800 40px/1 'Poppins';color:{GROEN};letter-spacing:-1px}} .st.g b{{color:#F5F9FA}}
.ph{{font:700 12px 'Plus Jakarta Sans';letter-spacing:2.4px;color:#8A97A3;text-transform:uppercase;white-space:nowrap}}
.w{{display:grid;grid-template-columns:40px 64px 1fr 230px 100px;align-items:center;gap:14px;height:62px;padding:0 20px;
  border-radius:18px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.10);margin-bottom:10px}}
.nr{{width:34px;height:34px;border-radius:50%;background:rgba(47,212,110,.16);color:{GROEN};font:800 17px 'Poppins';
  display:flex;align-items:center;justify-content:center}}
.tm{{font:800 19px 'Poppins';color:#AEB9C2}}
.tt{{display:flex;align-items:center;gap:10px;font:700 19px 'Poppins';color:#F5F9FA;white-space:nowrap;overflow:hidden}}
.tt img{{width:40px;height:40px;object-fit:contain;padding:4px;border-radius:50%;background:rgba(245,249,250,.92)}} .tt i{{font-style:normal;color:#8A97A3}}
.tip{{font:800 18px 'Plus Jakarta Sans';color:#F5F9FA;white-space:nowrap;text-align:right}}
.od{{text-align:center;padding:9px 0;border-radius:12px;background:rgba(47,212,110,.16);font:800 20px 'Poppins';color:{GROEN}}}
"""

body = f'''<div class="b">
  <div class="glow" style="width:760px;height:560px;left:-260px;top:-320px;background:rgba(22,154,71,.48)"></div>
  <div class="ijs" style="width:620px;height:460px;right:-240px;top:-300px;background:rgba(124,196,255,.16)"></div>
  <div class="glow" style="width:640px;height:420px;left:300px;bottom:-340px;background:rgba(22,154,71,.18)"></div>
  <img src="betexperts_logo.png" style="position:absolute;left:56px;top:44px;height:28px">
  <div style="position:absolute;left:56px;top:104px;display:flex;align-items:center;gap:22px">
    <div class="crest"><img src="{logo(LIGA)}"></div>
    <div><div class="eb">{getattr(M, "OG_SPORT", "IJshockey")} · {M.OG_EYEBROW_DATUM}</div>
      <div class="kop" style="margin-top:12px">{LIGA.upper()} vannacht:<br><em>{len(M.TOP3)} beste wedtips</em></div></div>
  </div>
  <div class="bt"><div class="st"><div class="l">{GISTEREN[0]}</div><b>{GISTEREN[1]}</b></div>
    <div class="st g"><div class="l">{EXTRA[0]}</div><b>{EXTRA[1]}</b></div></div>
  <div style="position:absolute;left:56px;right:56px;top:300px">
    <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:12px">
      <div class="ph">Onze tips (Nederlandse tijd)</div><div class="ph" style="letter-spacing:1.6px">{getattr(M, "OG_RECHTS", "Winnaar incl. verlenging · TOTO")}</div></div>
    {"".join(rij(i, w) for i, w in enumerate(M.TOP3, 1))}
  </div>
  <div style="position:absolute;left:56px;right:56px;bottom:52px;height:1px;background:rgba(255,255,255,.08)"></div>
  <div style="position:absolute;left:56px;bottom:20px;font-size:13px;color:#8A97A3">Wat kost gokken jou? Stop op tijd. 18+</div>
  <div style="position:absolute;right:56px;bottom:20px;font:700 13px 'Plus Jakarta Sans';color:#6CC08B">bet-experts.nl</div>
</div>'''

CHECK_JS = """(() => { const r = []; const b = document.querySelector('.b').getBoundingClientRect();
  const lijn = [...document.querySelectorAll('.b > div')].find(d => d.style.height === '1px').getBoundingClientRect();
  document.querySelectorAll('.b *').forEach(el => { if (el.classList.contains('glow') || el.classList.contains('ijs')) return;
    const q = el.getBoundingClientRect(); if (q.width && (q.right > b.right - 40 || q.bottom > b.bottom + 1)) r.push('buiten:' + el.className);
    if ((el.classList.contains('tt') || el.classList.contains('tip')) && el.scrollWidth > el.clientWidth + 1) r.push('te lang:' + el.textContent);
    if (el.classList.contains('w') && q.bottom > lijn.top - 10) r.push('raakt footer'); });
  const kop = document.querySelector('.kop').getBoundingClientRect(), bt = document.querySelector('.bt').getBoundingClientRect();
  if (kop.right > bt.left - 20) r.push('kop raakt tegels'); if (bt.bottom > 300 - 12) r.push('tegels raken tips: ' + Math.round(bt.bottom));
  document.querySelectorAll('img').forEach(i => { if (!i.complete || !i.naturalWidth) r.push('img niet geladen ' + i.src.slice(-20)); });
  return r; })()"""

html = f"<!doctype html><html lang='nl'><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"
f = A / f".nhl3-{uuid.uuid4().hex[:8]}.html"
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
