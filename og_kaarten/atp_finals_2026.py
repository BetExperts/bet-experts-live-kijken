"""Deelkaart 'ATP Finals 2026: wie is er al zeker?' (Race to Turin top 8, zonder de afgemelde Sinner).
Data uit specials/atp_finals_2026_gekwalificeerd.py (SPELERS). Geen officieel logo: tekstkop.
  python3 og_kaarten/atp_finals_2026.py [uit.png]"""
import sys, uuid, pathlib
sys.path.insert(0, "/Users/jaspervandenboogaard/bet-experts/preview-images-agent")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "specials"))
import kaart
from atp_finals_2026_gekwalificeerd import SPELERS, PEILDATUM, race_pos, pt
from playwright.sync_api import sync_playwright

A = pathlib.Path(kaart.ASSETS)
SP = pathlib.Path(__file__).parent.parent
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else SP / "og_atp_finals_2026.png")

BLAUW = "#6FA8FF"  # koele accentkleur (indoor hardcourt), naast het huisgroen
VINK = ('<svg width="12" height="12" viewBox="0 0 12 12"><path d="M2.2 6.4l2.4 2.4 5.2-5.6" fill="none" '
        'stroke="#0B1117" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>')

top8 = SPELERS[:8]
zeker = sum(1 for s in SPELERS if s[2] == "Zeker")
rijen = "".join(
    f'<div class="rw{" z" if st == "Zeker" else ""}"><span class="ps">{race_pos(i)}</span><span class="cc">{c}</span>'
    f'<span class="nm">{n}</span><span class="pt">{pt(p)}</span>'
    + (f'<span class="zk">{VINK}zeker</span>' if st == "Zeker" else '<span class="zk leeg"></span>') + "</div>"
    for i, (n, c, st, p) in enumerate(top8))
dag = PEILDATUM.replace(" 2026", "").replace("oktober", "okt")

css = kaart.CSS + f"""
.blauw{{position:absolute;border-radius:50%;filter:blur(110px)}}
.eb{{font:700 14px 'Plus Jakarta Sans';letter-spacing:3px;color:#6CC08B;text-transform:uppercase}}
.tt{{font:800 60px/1.04 'Poppins';letter-spacing:-1.5px}}
.tt em{{font-style:normal;color:#2FD46E}}
.st{{flex:1;border-radius:18px;padding:14px 18px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.10)}}
.st .k{{font:700 12px 'Plus Jakarta Sans';letter-spacing:2px;color:#8A97A3;text-transform:uppercase;white-space:nowrap}}
.st .v{{font:800 27px 'Poppins';color:#F5F9FA;margin-top:4px;white-space:nowrap}}
.st.g{{background:rgba(47,212,110,.10);border-color:rgba(47,212,110,.40)}}
.st.g .v{{color:#2FD46E}}
.rw{{display:flex;align-items:center;gap:10px;height:44px;padding:0 14px;border-radius:13px;
  background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.09)}}
.rw.z{{background:rgba(47,212,110,.09);border-color:rgba(47,212,110,.35)}}
.ps{{font:800 15px 'Poppins';color:#C9D3DB;width:22px;text-align:right}}
.cc{{font:800 11px 'Poppins';letter-spacing:1px;color:#8A97A3;width:32px}}
.nm{{font:700 17px 'Plus Jakarta Sans';color:#F5F9FA;white-space:nowrap;flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis}}
.pt{{font:800 16px 'Poppins';color:#F5F9FA;width:58px;text-align:right}}
.zk{{width:74px;display:inline-flex;align-items:center;justify-content:center;gap:4px;height:22px;border-radius:999px;
  background:#2FD46E;color:#0B1117;font:800 11px 'Poppins';letter-spacing:1px;text-transform:uppercase}}
.zk.leeg{{background:none}}
"""

body = f'''<div class="b">
  <div class="glow" style="width:760px;height:560px;left:-220px;top:-300px;background:rgba(22,154,71,.50)"></div>
  <div class="blauw" style="width:620px;height:480px;right:-200px;top:-260px;background:rgba(111,168,255,.16)"></div>
  <div class="glow" style="width:600px;height:460px;right:-160px;bottom:-280px;background:rgba(22,154,71,.24)"></div>
  <img src="betexperts_logo.png" style="position:absolute;left:56px;top:44px;height:28px">
  <div style="position:absolute;right:56px;top:40px;display:flex;align-items:center;gap:10px">
    <span style="width:8px;height:8px;border-radius:50%;background:#2FD46E"></span>
    <span style="font:700 15px 'Plus Jakarta Sans'">Tennis</span>
    <span style="font:600 13px 'Plus Jakarta Sans';color:#8A97A3">· Turijn · 15–22 november</span></div>

  <div style="position:absolute;left:56px;right:56px;top:118px;display:flex;gap:40px;align-items:flex-start">
    <div style="flex:1;min-width:0">
      <div class="eb">Nitto ATP Finals · Race to Turin</div>
      <div class="tt" style="margin-top:18px">ATP Finals 2026:<br><em>wie is er al zeker?</em></div>
      <div style="margin-top:22px;font:600 18px/1.45 'Plus Jakarta Sans';color:#C9D3DB;max-width:520px">
        Sinner (2e in de Race) is afgemeld met een knieblessure. Zijn plek gaat naar de nummer 9.</div>
      <div style="margin-top:26px;display:flex;gap:12px">
        <div class="st g"><div class="k">Zeker</div><div class="v">{zeker} spelers</div></div>
        <div class="st"><div class="k">Nog vrij</div><div class="v">{8 - zeker} plekken</div></div>
        <div class="st"><div class="k">Beslissing</div><div class="v">Parijs</div></div>
      </div>
    </div>
    <div style="width:470px;flex:none">
      <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:10px">
        <span style="font:700 12px 'Plus Jakarta Sans';letter-spacing:2.5px;color:#8A97A3;text-transform:uppercase">Race to Turin · top 8</span>
        <span style="font:600 12px 'Plus Jakarta Sans';color:#8A97A3">stand {dag}</span></div>
      <div style="display:flex;flex-direction:column;gap:6px">{rijen}</div>
    </div>
  </div>

  <div style="position:absolute;left:56px;right:56px;bottom:52px;height:1px;background:rgba(255,255,255,.08)"></div>
  <div style="position:absolute;left:56px;bottom:20px;font-size:13px;color:#8A97A3">Wat kost gokken jou? Stop op tijd. 18+</div>
  <div style="position:absolute;right:56px;bottom:20px;font:700 13px 'Plus Jakarta Sans';color:#6CC08B">bet-experts.nl</div>
</div>'''

CHECK_JS = """(() => { const r = []; const b = document.querySelector('.b').getBoundingClientRect();
  document.querySelectorAll('.b *').forEach(el => { if (el.classList.contains('glow') || el.classList.contains('blauw')) return;
    if (el.scrollWidth > el.clientWidth + 1 && getComputedStyle(el).overflow !== 'visible') r.push('scroll:' + el.className);
    const q = el.getBoundingClientRect(); if (q.width && (q.right > b.right + 1 || q.bottom > b.bottom + 1)) r.push('buiten:' + el.className);
    if (el.classList.contains('nm') && el.scrollWidth > el.clientWidth) r.push('naam:' + el.textContent); });
  return r; })()"""

html = f"<!doctype html><html lang='nl'><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"
f = A / f".atpf-{uuid.uuid4().hex[:8]}.html"
f.write_text(html, encoding="utf-8")
try:
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--font-render-hinting=none"])
        pg = b.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=2)
        pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
        fouten = pg.evaluate(CHECK_JS)
        pg.screenshot(path=str(OUT))
        b.close()
finally:
    f.unlink(missing_ok=True)
print(OUT, "| overloop:", fouten or "geen")
