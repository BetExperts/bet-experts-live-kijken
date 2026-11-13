"""Deelkaarten voor de drie Suriname – Eswatini-artikelen (OG_EB, OG_KOP, OG_RIJEN uit elke module)."""
import io, sys, uuid, pathlib, importlib
sys.path.insert(0, "/Users/jaspervandenboogaard/bet-experts/preview-images-agent")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "specials"))
import kaart
from PIL import Image
from playwright.sync_api import sync_playwright
A = pathlib.Path(kaart.ASSETS); OG = pathlib.Path(__file__).resolve().parent.parent / "og" / "nieuws"
G = "#2FD46E"
css = kaart.CSS + f"""
.eb{{font:700 14px 'Plus Jakarta Sans';letter-spacing:3px;color:#6CC08B;text-transform:uppercase}}
.tt{{font:800 56px/1.04 'Poppins';letter-spacing:-1.5px}} .tt em{{font-style:normal;color:{G}}}
.dt{{font:700 19px 'Plus Jakarta Sans';color:#C9D3DB}}
.vl{{display:flex;gap:10px}} .vl span{{width:64px;height:42px;border-radius:8px;overflow:hidden;box-shadow:0 6px 18px rgba(0,0,0,.4)}}
.big{{border-radius:20px;padding:16px 22px;background:linear-gradient(135deg,rgba(47,212,110,.22),rgba(22,154,71,.10));border:1.5px solid rgba(47,212,110,.65)}}
.big .k{{font:700 12px 'Plus Jakarta Sans';letter-spacing:2px;color:#8A97A3;text-transform:uppercase}}
.big .v{{font:800 40px/1.05 'Poppins';color:#F5F9FA;margin-top:4px}} .big .s{{font:600 15px 'Plus Jakarta Sans';color:#C9D3DB}}
.rw{{display:flex;justify-content:space-between;align-items:center;height:54px;border-radius:14px;padding:0 18px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.10)}}
.rw .k{{font:700 14px 'Plus Jakarta Sans';color:#8A97A3}} .rw .v{{font:800 18px 'Poppins';color:#F5F9FA;white-space:nowrap}}
"""
SUR = ('<svg viewBox="0 0 30 20"><rect width="30" height="20" fill="#377E3F"/><rect y="4" width="30" height="12" fill="#fff"/>'
       '<rect y="5.3" width="30" height="9.4" fill="#B40A2D"/><polygon fill="#ECC81D" points="15,6.2 16.1,9.4 19.5,9.4 16.8,11.4 17.8,14.6 15,12.6 12.2,14.6 13.2,11.4 10.5,9.4 13.9,9.4"/></svg>')
ESW = ('<svg viewBox="0 0 30 20"><rect width="30" height="20" fill="#3E5EB9"/><rect y="3.5" width="30" height="13" fill="#FFD900"/>'
       '<rect y="5" width="30" height="10" fill="#B10C0C"/><ellipse cx="15" cy="10" rx="7" ry="4" fill="#fff"/><path d="M8 10c3-4 11-4 14 0c-3 4-11 4-14 0z" fill="#000" opacity=".9"/>'
       '<path d="M15 6c3 0 6 2 7 4c-1 2-4 4-7 4z" fill="#fff"/></svg>')
CHECK = """(() => { const r=[]; const l=[...document.querySelectorAll('.b > div')].find(d=>d.style.height==='1px').getBoundingClientRect();
 const c=document.querySelector('.col').getBoundingClientRect(); if(c.bottom>l.top-8) r.push('kolom raakt footer');
 if(document.querySelector('.tt').getBoundingClientRect().right>c.left-20) r.push('kop raakt kolom'); return r; })()"""
for naam in ("suriname_eswatini_kijken", "suriname_eswatini_tickets", "suriname_eswatini_voorspelling"):
    M = importlib.import_module(naam)
    (k1, v1), *rest = M.OG_RIJEN
    rij = "".join(f'<div class="rw"><span class="k">{k}</span><span class="v">{v}</span></div>' for k, v in rest)
    body = f'''<div class="b">
  <div class="glow" style="width:760px;height:560px;left:-220px;top:-300px;background:rgba(22,154,71,.50)"></div>
  <div class="glow" style="width:520px;height:420px;right:-160px;bottom:-260px;background:rgba(180,10,45,.16)"></div>
  <img src="betexperts_logo.png" style="position:absolute;left:56px;top:44px;height:28px">
  <div style="position:absolute;left:56px;top:128px;width:480px">
    <div class="vl"><span>{SUR}</span><span>{ESW}</span></div>
    <div class="eb" style="margin-top:22px">{M.OG_EB}</div>
    <div class="tt" style="margin-top:12px">{M.OG_KOP}</div>
    <div class="dt" style="margin-top:16px">Zondag 15 november · De Vliert, Den Bosch</div>
  </div>
  <div class="col" style="position:absolute;right:56px;top:72px;width:520px;display:flex;flex-direction:column;gap:10px">
    <div class="big"><div class="k">{k1}</div><div class="v">{v1}</div></div>{rij}
  </div>
  <div style="position:absolute;left:56px;right:56px;bottom:52px;height:1px;background:rgba(255,255,255,.08)"></div>
  <div style="position:absolute;left:56px;bottom:20px;font-size:13px;color:#8A97A3">Wat kost gokken jou? Stop op tijd. 18+</div>
  <div style="position:absolute;right:56px;bottom:20px;font:700 13px 'Plus Jakarta Sans';color:#6CC08B">bet-experts.nl</div>
</div>'''
    html = f"<!doctype html><html lang='nl'><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"
    f = A / f".sesw-{uuid.uuid4().hex[:8]}.html"; f.write_text(html, encoding="utf-8")
    try:
        with sync_playwright() as p:
            b = p.chromium.launch(args=["--font-render-hinting=none"]); pg = b.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=2)
            pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300); fout = pg.evaluate(CHECK); png = pg.screenshot(); b.close()
    finally:
        f.unlink(missing_ok=True)
    out = OG / f"nieuws-{M.SLUG}.webp"
    Image.open(io.BytesIO(png)).convert("RGB").resize((1200, 630), Image.LANCZOS).save(out, "WEBP", quality=84, method=6)
    print(out.name, "| overloop:", fout or "geen")
