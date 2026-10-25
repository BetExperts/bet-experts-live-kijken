"""Telegram-afbeelding 'NBA vannacht' (1200x630, nieuwe kaartstijl) voor het groepsbericht met de voorbeschouwingen:
NBA-logo, kop, tegel met het resultaat van gisteren en per topper een rij met beide teamlogo's, aanvangstijd en de
Winnaar-odds. Bewust zonder wedtips (Telegram-teaser). Logo's: og_kaarten/nba-<abbr>.png (ESPN, lokaal).
  ../superodd-agent/.venv/bin/python og_kaarten/nba_programma.py [uit.jpg]"""
import io, sys, uuid, pathlib
sys.path.insert(0, "/Users/jaspervandenboogaard/bet-experts/preview-images-agent")
import kaart
from PIL import Image
from playwright.sync_api import sync_playwright

A = pathlib.Path(kaart.ASSETS)
HIER = pathlib.Path(__file__).resolve().parent
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else HIER.parent / "og" / "nba-programma-2026-10-25.jpg")
GROEN, ORANJE = "#2FD46E", "#F58426"
EYEBROW = "Basketbal · nacht van 24 op 25 oktober"
TEGEL = ("Gisteren", "4/4", "Alle 4 tips uit ons NBA-artikel raak")
# (tijd NL, thuis, abbr, uit, abbr, odd thuis, odd uit)  TOTO Winnaar incl. verlenging
WEDSTRIJDEN = [
    ("01:30", "76ers", "phi", "Bucks", "mil", 1.14, 5.95),
    ("02:00", "Mavericks", "dal", "Spurs", "sa", 5.15, 1.18),
    ("02:30", "Hawks", "atl", "Rockets", "hou", 1.83, 2.00),
    ("03:00*", "Suns", "phx", "Warriors", "gs", 1.26, 4.05),
]
EMOJI, PH = "✅", "De toppers van vannacht (Nederlandse tijd)"
NOOT = "* wintertijd: om 03:00 gaat de klok een uur terug · 4 voorbeschouwingen + onze 4 beste tips op bet-experts.nl"
if len(sys.argv) > 2:   # andere avond: JSON met eyebrow, tegel [3], wedstrijden [[tijd, thuis, abbr, uit, abbr, odd, odd]], noot
    import json
    _d = json.loads(pathlib.Path(sys.argv[2]).read_text(encoding="utf-8"))
    EYEBROW, TEGEL, NOOT, EMOJI, PH = _d["eyebrow"], tuple(_d["tegel"]), _d.get("noot", ""), _d.get("emoji", ""), _d.get("kop_lijst", PH)
    WEDSTRIJDEN = [tuple(w) for w in _d["wedstrijden"]]
COMPACT = len(WEDSTRIJDEN) > 4
PROG_TOP = 250 if COMPACT else 262
logo = lambda a: (HIER / f"nba-{a}.png").as_uri()
q = lambda x: f"{x:.2f}".replace(".", ",")


def rij(w):
    t, h, ha, u, ua, oh, ou = w
    fh, fu = ("", "") if oh == ou else (("fav", "") if oh < ou else ("", "fav"))
    return (f'<div class="w"><div class="tm">{t}</div>'
            f'<div class="tt"><img src="{logo(ha)}"><span>{h}</span></div><div class="vs">–</div>'
            f'<div class="tt r"><span>{u}</span><img src="{logo(ua)}"></div>'
            f'<div class="od"><b class="{fh}">{q(oh)}</b><b class="{fu}">{q(ou)}</b></div></div>')


rijen = "".join(rij(w) for w in WEDSTRIJDEN)

css = kaart.CSS + f"""
.or{{position:absolute;border-radius:50%;filter:blur(120px)}}
.eb{{font:700 14px 'Plus Jakarta Sans';letter-spacing:3px;color:#6CC08B;text-transform:uppercase;white-space:nowrap}}
.kop{{font:800 58px/1.0 'Poppins';letter-spacing:-2px;color:#F5F9FA}}
.kop em{{font-style:normal;color:{GROEN}}}
.crest{{width:108px;height:108px;border-radius:26px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);
  display:flex;align-items:center;justify-content:center}}
.crest img{{width:76px;height:76px;object-fit:contain}}
.bt{{position:absolute;right:56px;top:96px;width:380px;padding:16px 24px;border-radius:22px;
  background:linear-gradient(160deg,rgba(47,212,110,.20),rgba(47,212,110,.05));border:1px solid rgba(47,212,110,.55)}}
.bt .l{{font:700 12px 'Plus Jakarta Sans';letter-spacing:2.4px;color:{GROEN};text-transform:uppercase}}
.bt .rg{{margin-top:8px;display:flex;align-items:center;gap:14px}}
.bt .rg b{{font:800 48px/1 'Poppins';color:{GROEN};letter-spacing:-1px}}
.bt .rg i{{font-style:normal;font-size:34px}}
.bt .wd{{margin-top:6px;font:600 14px/1.35 'Plus Jakarta Sans';color:#AEB9C2}}
.ph{{font:700 12px 'Plus Jakarta Sans';letter-spacing:2.4px;color:#8A97A3;text-transform:uppercase;white-space:nowrap}}
.w{{display:grid;grid-template-columns:78px 1fr 24px 1fr 170px;align-items:center;gap:12px;height:56px;padding:0 20px;
  border-radius:16px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.10);margin-bottom:9px}}
.tm{{font:800 19px 'Poppins';color:#F5F9FA}}
.tt{{display:flex;align-items:center;gap:12px;font:700 19px 'Poppins';color:#F5F9FA;white-space:nowrap;overflow:hidden}}
.tt.r{{justify-content:flex-end}}
.tt img{{width:38px;height:38px;object-fit:contain}}
.vs{{text-align:center;color:#8A97A3;font:700 18px 'Poppins'}}
.od{{display:flex;gap:8px;justify-content:flex-end}}
.od b{{min-width:72px;text-align:center;padding:7px 0;border-radius:11px;background:rgba(255,255,255,.06);font:800 16px 'Poppins';color:#DDE4EA}}
.od b.fav{{background:rgba(47,212,110,.16);color:{GROEN}}}
.nt{{font:600 12px 'Plus Jakarta Sans';color:#8A97A3}}
""" + ("""
.w{height:34px;margin-bottom:5px;border-radius:11px} .tm{font-size:16px} .tt{font-size:16px}
.tt img{width:28px;height:28px} .od b{padding:4px 0;font-size:14px;border-radius:9px}
.bt{top:90px;padding:14px 22px} .bt .rg b{font-size:42px}
""" if COMPACT else "")

body = f'''<div class="b">
  <div class="glow" style="width:760px;height:560px;left:-260px;top:-320px;background:rgba(22,154,71,.48)"></div>
  <div class="or" style="width:620px;height:460px;right:-240px;top:-300px;background:rgba(245,132,38,.16)"></div>
  <div class="glow" style="width:640px;height:420px;left:300px;bottom:-340px;background:rgba(22,154,71,.18)"></div>
  <img src="betexperts_logo.png" style="position:absolute;left:56px;top:44px;height:28px">
  <div style="position:absolute;left:56px;top:104px;display:flex;align-items:center;gap:22px">
    <div class="crest"><img src="{logo('nba')}"></div>
    <div><div class="eb">{EYEBROW}</div>
      <div class="kop" style="margin-top:12px">NBA<br><em>vannacht</em></div></div>
  </div>
  <div class="bt"><div class="l">{TEGEL[0]}</div>
    <div class="rg"><b>{TEGEL[1]}</b>{"<i>" + EMOJI + "</i>" if EMOJI else ""}</div>
    <div class="wd">{TEGEL[2]}</div></div>
  <div style="position:absolute;left:56px;right:56px;top:{PROG_TOP}px">
    <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:10px">
      <div class="ph">{PH}</div><div class="ph" style="letter-spacing:1.6px">Winnaar incl. verlenging</div></div>
    {rijen}
    <div class="nt">{NOOT}</div>
  </div>
  <div style="position:absolute;left:56px;right:56px;bottom:52px;height:1px;background:rgba(255,255,255,.08)"></div>
  <div style="position:absolute;left:56px;bottom:20px;font-size:13px;color:#8A97A3">Wat kost gokken jou? Stop op tijd. 18+</div>
  <div style="position:absolute;right:56px;bottom:20px;font:700 13px 'Plus Jakarta Sans';color:#6CC08B">bet-experts.nl</div>
</div>'''

CHECK_JS = ("const PROG_TOP = " + str(PROG_TOP) + ";") + """(() => { const r = []; const b = document.querySelector('.b').getBoundingClientRect();
  const lijn = [...document.querySelectorAll('.b > div')].find(d => d.style.height === '1px').getBoundingClientRect();
  document.querySelectorAll('.b *').forEach(el => { if (el.classList.contains('glow') || el.classList.contains('or')) return;
    const q = el.getBoundingClientRect(); if (q.width && (q.right > b.right - 40 || q.bottom > b.bottom + 1)) r.push('buiten:' + el.className);
    if (el.classList.contains('tt') && el.scrollWidth > el.clientWidth + 1) r.push('naam te lang:' + el.textContent);
    if ((el.classList.contains('w') || el.classList.contains('nt')) && q.bottom > lijn.top - 8) r.push('raakt footer:' + el.className); });
  const kop = document.querySelector('.kop').getBoundingClientRect(), bt = document.querySelector('.bt').getBoundingClientRect();
  if (kop.right > bt.left - 20) r.push('kop raakt tegel'); if (bt.bottom > PROG_TOP - 8) r.push('tegel raakt programma: ' + Math.round(bt.bottom));
  document.querySelectorAll('img').forEach(i => { if (!i.complete || !i.naturalWidth) r.push('img niet geladen ' + i.src.slice(-20)); });
  return r; })()"""

html = f"<!doctype html><html lang='nl'><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"
f = A / f".nbaprog-{uuid.uuid4().hex[:8]}.html"
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
img.save(OUT, "JPEG", quality=92)
print(OUT, img.size, f"{OUT.stat().st_size // 1024} KB", "| overloop:", fouten or "geen")
