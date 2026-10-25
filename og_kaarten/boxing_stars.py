"""Boxing Stars 2026: (1) visueel schema voor in het artikel (1200x1240) en (2) deelkaart (1200x630), nieuwe kaartstijl
met een rood boks-accent. Data uit specials/boxing_stars_2026.py (AVONDEN, POULES, SLUG).
  ../superodd-agent/.venv/bin/python og_kaarten/boxing_stars.py   -> og/nieuws/boxing-stars-schema.webp + nieuws-<slug>.webp"""
import io, sys, uuid, pathlib
sys.path.insert(0, "/Users/jaspervandenboogaard/bet-experts/preview-images-agent")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "specials"))
import kaart
import boxing_stars_2026 as M
from PIL import Image
from playwright.sync_api import sync_playwright

A = pathlib.Path(kaart.ASSETS)
SP = pathlib.Path(__file__).resolve().parent.parent
G, RD, GD = "#2FD46E", "#E5484D", "#F2C14E"

CSS = kaart.CSS + f"""
.b.lang{{height:1190px}}
.tint{{position:absolute;border-radius:50%;filter:blur(120px)}}
.eb{{font:700 14px 'Plus Jakarta Sans';letter-spacing:3px;color:#6CC08B;text-transform:uppercase;white-space:nowrap}}
.kop{{font:800 60px/1.0 'Poppins';letter-spacing:-2px;color:#F5F9FA}} .kop em{{font-style:normal;color:{RD}}}
.crest{{width:104px;height:104px;border-radius:26px;background:rgba(229,72,77,.12);border:1px solid rgba(229,72,77,.45);
  display:flex;align-items:center;justify-content:center;font-size:58px}}
.chip{{display:inline-flex;align-items:center;gap:8px;padding:8px 14px;border-radius:999px;background:rgba(255,255,255,.07);
  border:1px solid rgba(255,255,255,.12);font:700 14px 'Plus Jakarta Sans';color:#DDE4EA;white-space:nowrap}}
.chip.r{{background:rgba(229,72,77,.14);border-color:rgba(229,72,77,.5);color:#FF8A8D}}
.ph{{font:700 12px 'Plus Jakarta Sans';letter-spacing:2.4px;color:#8A97A3;text-transform:uppercase;white-space:nowrap}}
.av{{border-radius:22px;padding:20px 20px 16px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.10);display:flex;flex-direction:column}}
.av.f{{background:linear-gradient(160deg,rgba(242,193,78,.16),rgba(242,193,78,.04));border-color:rgba(242,193,78,.5)}}
.av .n{{font:700 12px 'Plus Jakarta Sans';letter-spacing:2.2px;color:#8A97A3;text-transform:uppercase}}
.av.f .n{{color:{GD}}}
.av .d{{margin-top:6px;font:800 34px/1 'Poppins';color:#F5F9FA;letter-spacing:-1px}}
.av .t{{margin-top:6px;font:600 14px 'Plus Jakarta Sans';color:#AEB9C2}}
.bout{{margin-top:12px;padding:10px 12px;border-radius:14px;background:rgba(0,0,0,.22);border:1px solid rgba(255,255,255,.06)}}
.bout .p{{font:700 10px 'Plus Jakarta Sans';letter-spacing:1.6px;color:#8A97A3;text-transform:uppercase}}
.bout .v{{margin-top:3px;font:700 16px/1.25 'Poppins';color:#F5F9FA}} .bout .v i{{font-style:normal;color:{RD}}}
.po{{border-radius:20px;padding:16px 18px;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.09)}}
.po .h{{font:800 18px 'Poppins';color:#F5F9FA}} .po .s{{font:600 12px 'Plus Jakarta Sans';color:#8A97A3;margin-top:2px}}
.po ul{{list-style:none;margin-top:10px}} .po li{{font:600 15px/1.9 'Plus Jakarta Sans';color:#DDE4EA}}
.po li::before{{content:'🥊';margin-right:8px;font-size:13px}}
.inf{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}}
.inf div{{border-radius:16px;padding:12px 14px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.10)}}
.inf b{{display:block;font:800 22px 'Poppins';color:#F5F9FA}} .inf span{{font:600 12px 'Plus Jakarta Sans';color:#8A97A3}}
.nt{{font:600 12px 'Plus Jakarta Sans';color:#8A97A3}}
"""
GLOW = f'''<div class="glow" style="width:760px;height:560px;left:-260px;top:-320px;background:rgba(22,154,71,.40)"></div>
  <div class="tint" style="width:640px;height:480px;right:-240px;top:-300px;background:rgba(229,72,77,.22)"></div>
  <img src="betexperts_logo.png" style="position:absolute;left:56px;top:44px;height:28px">'''
FOOT = '''<div style="position:absolute;left:56px;right:56px;bottom:52px;height:1px;background:rgba(255,255,255,.08)"></div>
  <div style="position:absolute;left:56px;bottom:20px;font-size:13px;color:#8A97A3">Live bij Videoland · Mediahaven Amsterdam</div>
  <div style="position:absolute;right:56px;bottom:20px;font:700 13px 'Plus Jakarta Sans';color:#6CC08B">bet-experts.nl</div>'''


def avond(a):
    bouts = "".join(f'<div class="bout"><div class="p">{p}</div><div class="v">{x} <i>vs</i> {y}</div></div>' for p, x, y in a["duels"])
    if not bouts:   # finale-avond: per poule winnaar avond 1 tegen winnaar avond 2
        bouts = "".join(f'<div class="bout"><div class="p">Finale {p["naam"].lower()}</div><div class="v">Winnaar 31 okt <i>vs</i> winnaar 7 nov</div></div>'
                        for p in M.POULES)
    return (f'<div class="av{" f" if a["finale"] else ""}"><div class="n">{a["naam"]}</div><div class="d">{a["datum"]}</div>'
            f'<div class="t">Live om 20:00 uur · deuren 17:30</div>{bouts}</div>')


poules = "".join(f'<div class="po"><div class="h">{p["naam"]}</div><div class="s">{p["sub"]}</div><ul>'
                 + "".join(f"<li>{n}</li>" for n in p["namen"]) + "</ul></div>" for p in M.POULES)

SCHEMA = f'''<div class="b lang">{GLOW}
  <div style="position:absolute;left:56px;top:100px;display:flex;align-items:center;gap:22px">
    <div class="crest">🥊</div>
    <div><div class="eb">Videoland · 31 oktober t/m 14 november 2026</div>
      <div class="kop" style="margin-top:10px">Boxing Stars <em>schema</em></div></div></div>
  <div style="position:absolute;left:56px;right:56px;top:250px">
    <div class="ph" style="margin-bottom:12px">De drie Fight Nights</div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px">{"".join(avond(a) for a in M.AVONDEN)}</div>
    <div class="nt" style="margin-top:10px">Indeling van de partijen volgens de laatste berichten; Videoland heeft nog geen officiële fightcard gepubliceerd.</div>
    <div class="ph" style="margin:30px 0 12px">De drie poules</div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px">{poules}</div>
    <div class="ph" style="margin:30px 0 12px">Praktisch</div>
    <div class="inf"><div><b>17:30</b><span>Deuren open + voorprogramma</span></div><div><b>18:45</b><span>Laatste entree</span></div>
      <div><b>20:00</b><span>Live-uitzending Videoland</span></div><div><b>€35</b><span>Ticket incl. 2 drankjes</span></div></div>
  </div>{FOOT}</div>'''

DEEL = f'''<div class="b">{GLOW}
  <div style="position:absolute;left:56px;top:100px;display:flex;align-items:center;gap:22px">
    <div class="crest">🥊</div>
    <div><div class="eb">Videoland · Mediahaven Amsterdam</div>
      <div class="kop" style="margin-top:10px">Boxing Stars <em>2026</em></div></div></div>
  <div style="position:absolute;right:56px;top:112px;display:flex;flex-direction:column;align-items:flex-end;gap:10px">
    <span class="chip r">12 BN'ers · 3 poules</span><span class="chip">Live om 20:00 uur</span></div>
  <div style="position:absolute;left:56px;right:56px;top:262px;display:grid;grid-template-columns:repeat(3,1fr);gap:16px">
    {"".join(f'<div class="av{" f" if a["finale"] else ""}"><div class="n">{a["naam"]}</div><div class="d">{a["datum"]}</div><div class="t">{a["kort"]}</div></div>' for a in M.AVONDEN)}
  </div>
  <div style="position:absolute;left:56px;right:56px;top:410px;padding:18px 24px;border-radius:20px;display:flex;align-items:center;gap:18px;
    background:linear-gradient(90deg,rgba(229,72,77,.18),rgba(229,72,77,.04));border:1px solid rgba(229,72,77,.45)">
    <div style="font:700 12px 'Plus Jakarta Sans';letter-spacing:2.4px;color:#FF8A8D;text-transform:uppercase;white-space:nowrap">Blikvanger 31 oktober</div>
    <div style="font:800 30px 'Poppins';color:#F5F9FA;letter-spacing:-.5px;white-space:nowrap">Donny Roelvink <span style="color:#E5484D">vs</span> Carlos Platier Luna</div>
  </div>{FOOT}</div>'''


def render(body, h, out, webp=True):
    html = f"<!doctype html><html lang='nl'><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>"
    f = A / f".bs-{uuid.uuid4().hex[:8]}.html"
    f.write_text(html, encoding="utf-8")
    try:
        with sync_playwright() as p:
            b = p.chromium.launch(args=["--font-render-hinting=none", "--allow-file-access-from-files"])
            pg = b.new_page(viewport={"width": 1200, "height": h}, device_scale_factor=2)
            pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(400)
            over = pg.evaluate("""(() => { const r=[]; const b=document.querySelector('.b').getBoundingClientRect();
              const l=[...document.querySelectorAll('.b > div')].find(d=>d.style.height==='1px').getBoundingClientRect();
              document.querySelectorAll('.av,.po,.inf div').forEach(e=>{ if(e.getBoundingClientRect().bottom>l.top-6) r.push('raakt footer'); });
              document.querySelectorAll('.bout .v').forEach(e=>{ if(e.scrollWidth>e.clientWidth+1) r.push('te lang '+e.textContent); });
              return r; })()""")
            png = pg.screenshot(); b.close()
    finally:
        f.unlink(missing_ok=True)
    img = Image.open(io.BytesIO(png)).convert("RGB").resize((1200, h), Image.LANCZOS)
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, "WEBP", quality=86, method=6)
    print(out, "| overloop:", over or "geen")


if __name__ == "__main__":
    render(SCHEMA, 1190, SP / "og" / "nieuws" / "boxing-stars-schema.webp")
    render(DEEL, 630, SP / "og" / "nieuws" / f"nieuws-{M.SLUG}.webp")
