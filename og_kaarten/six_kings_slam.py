import shutil, sys, uuid, pathlib
sys.path.insert(0, "/Users/jaspervandenboogaard/bet-experts/preview-images-agent")
import kaart
from playwright.sync_api import sync_playwright

A = pathlib.Path(kaart.ASSETS)
SP = pathlib.Path(__file__).parent.parent
shutil.copy(pathlib.Path(__file__).parent / "sks-logo-breed.webp", A / ".sks-logo.webp")
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else SP / "og_sks2.png")

GOUD = "#E8C46B"
spelers = [("Carlos Alcaraz", "ESP", "bye"), ("Novak Djokovic", "SRB", "bye"), ("Alexander Zverev", "GER", ""),
           ("Taylor Fritz", "USA", ""), ("Alex de Minaur", "AUS", ""), ("Learner Tien", "USA", "")]
chips = "".join(
    f'<div class="sp"><span class="cc">{c}</span><span class="nm">{n}</span>'
    + (f'<span class="bye">bye</span>' if b else "") + "</div>" for n, c, b in spelers)

css = kaart.CSS + f"""
.gold{{position:absolute;border-radius:50%;filter:blur(110px)}}
.lt{{width:132px;height:132px;border-radius:30px;background:linear-gradient(160deg,#1A1610,#0F0D09);
  border:1.5px solid rgba(232,196,107,.55);box-shadow:0 0 0 6px rgba(232,196,107,.06),0 18px 40px rgba(0,0,0,.45);
  display:flex;align-items:center;justify-content:center}}
.lt img{{width:104px;height:104px;object-fit:contain}}
.eb{{font:700 14px 'Plus Jakarta Sans';letter-spacing:3px;color:{GOUD};text-transform:uppercase}}
.tt{{font:800 66px/1.0 'Poppins';letter-spacing:-1.5px}}
.tt em{{font-style:normal;color:{GOUD}}}
.sub{{font:600 19px 'Plus Jakarta Sans';color:#C9D3DB}}
.vp{{display:inline-flex;align-items:center;gap:10px;border-radius:999px;padding:10px 20px;background:#2FD46E;color:#0B1117;
  font:800 18px 'Poppins'}}
.vp s{{text-decoration:line-through;font:600 15px 'Plus Jakarta Sans';opacity:.65}}
.sp{{display:flex;align-items:center;gap:10px;height:54px;padding:0 16px;border-radius:16px;
  background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.10)}}
.cc{{font:800 12px 'Poppins';letter-spacing:1px;color:#8A97A3;width:34px}}
.nm{{font:700 18px 'Plus Jakarta Sans';color:#F5F9FA;white-space:nowrap}}
.bye{{margin-left:auto;font:800 11px 'Poppins';letter-spacing:1.2px;text-transform:uppercase;color:{GOUD};
  border:1px solid rgba(232,196,107,.45);border-radius:999px;padding:3px 9px}}
.st{{flex:1;border-radius:18px;padding:16px 20px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.10)}}
.st .k{{font:700 12px 'Plus Jakarta Sans';letter-spacing:2px;color:#8A97A3;text-transform:uppercase}}
.st .v{{font:800 27px 'Poppins';color:#F5F9FA;margin-top:4px;white-space:nowrap}}
.st.g{{background:rgba(232,196,107,.10);border-color:rgba(232,196,107,.40)}}
.st.g .v{{color:{GOUD}}}
"""

body = f'''<div class="b">
  <div class="glow" style="width:760px;height:560px;left:-220px;top:-300px;background:rgba(22,154,71,.50)"></div>
  <div class="gold" style="width:620px;height:480px;right:-180px;top:-240px;background:rgba(232,196,107,.20)"></div>
  <div class="glow" style="width:600px;height:460px;right:-160px;bottom:-280px;background:rgba(22,154,71,.24)"></div>
  <img src="betexperts_logo.png" style="position:absolute;left:56px;top:44px;height:28px">
  <div style="position:absolute;right:56px;top:40px;display:flex;align-items:center;gap:10px">
    <span style="width:8px;height:8px;border-radius:50%;background:{GOUD}"></span>
    <span style="font:700 15px 'Plus Jakarta Sans'">Tennis</span>
    <span style="font:600 13px 'Plus Jakarta Sans';color:#8A97A3">· Exhibitie · Riyad</span></div>

  <div style="position:absolute;left:56px;right:56px;top:132px;display:flex;gap:44px;align-items:flex-start">
    <div style="flex:1;min-width:0">
      <div class="eb">3e editie · ANB Arena</div>
      <img src=".sks-logo.webp" style="display:block;height:112px;margin-top:18px;filter:drop-shadow(0 8px 24px rgba(232,196,107,.22))">
      <div style="margin-top:34px;display:flex;align-items:center;gap:14px">
        <span class="vp">Verplaatst naar 27–30 december</span>
        <span class="sub"><s style="color:#8A97A3">21–24 okt</s></span>
      </div>
      <div style="margin-top:30px;display:flex;gap:14px">
        <div class="st g"><div class="k">Winnaar</div><div class="v">$6 miljoen</div></div>
        <div class="st"><div class="k">Prijzenpot</div><div class="v">$13,5 mln</div></div>
        <div class="st"><div class="k">Live op</div><div class="v">Netflix</div></div>
      </div>
    </div>
    <div style="width:356px;flex:none">
      <div style="font:700 12px 'Plus Jakarta Sans';letter-spacing:2.5px;color:#8A97A3;text-transform:uppercase;margin-bottom:12px">Aangekondigde spelers</div>
      <div style="display:flex;flex-direction:column;gap:10px">{chips}</div>
    </div>
  </div>

  <div style="position:absolute;left:56px;right:56px;bottom:52px;height:1px;background:rgba(255,255,255,.08)"></div>
  <div style="position:absolute;left:56px;bottom:20px;font-size:13px;color:#8A97A3">Wat kost gokken jou? Stop op tijd. 18+</div>
  <div style="position:absolute;right:56px;bottom:20px;font:700 13px 'Plus Jakarta Sans';color:#6CC08B">bet-experts.nl</div>
</div>'''

html = f"<!doctype html><html lang='nl'><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"
f = A / f".sks-{uuid.uuid4().hex[:8]}.html"
f.write_text(html, encoding="utf-8")
try:
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--font-render-hinting=none"])
        pg = b.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=2)
        pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
        pg.screenshot(path=str(OUT))
        b.close()
finally:
    f.unlink(missing_ok=True); (A / ".sks-logo.webp").unlink(missing_ok=True)
print(OUT)
