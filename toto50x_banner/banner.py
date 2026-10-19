# -*- coding: utf-8 -*-
"""TOTO 50x-banners in Bet-Experts-huisstijl (1200x400, 2x scherp) voor topwedstrijden zonder gratis livestream.

Drie varianten:  A = spotlight (vraag als kop + clublogo's), B = odds-ticket (normale odd -> 50.00),
                 C = split (groen 50x-vlak + wedstrijd).
  python3 banner.py                      # voorbeeld: FC Porto - PSV, alle drie
  render(data, variant, uitpad)          # vanuit een agent

data: comp, thuis, uit, thuis_logo, uit_logo, odd_thuis, odd_uit (normale odds bij TOTO), datum ('di 20 okt · 21:00')
De TOTO 50x geldt op winst van een ploeg naar keuze -> de banner zegt 'kies jouw favoriet'.
"""
import html, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
KSA = "Alleen voor nieuwe spelers van 24+ · max. €1 inzet · uitbetaling in Free Bets · Wat kost gokken jou? Stop op tijd. 18+"

CSS = """
@import url('fonts.css');
*{box-sizing:border-box;margin:0;padding:0}
body{background:transparent;font-family:'Plus Jakarta Sans',sans-serif;-webkit-font-smoothing:antialiased}
.b{width:1200px;height:400px;position:relative;overflow:hidden;border-radius:22px;background:#0B1117;color:#F5F9FA}
.glow{position:absolute;border-radius:50%;filter:blur(90px);pointer-events:none}
.logo-be{position:absolute;height:26px}
.ksa{position:absolute;left:56px;right:56px;bottom:20px;font-size:12.5px;color:#8A97A3;letter-spacing:.1px}
.pill{display:inline-flex;align-items:center;gap:10px;border:1.5px solid rgba(255,255,255,.55);border-radius:999px;padding:7px 16px;
      font:700 13px 'Plus Jakarta Sans';letter-spacing:2.2px;text-transform:uppercase}
.tag{font:700 13px 'Plus Jakarta Sans';letter-spacing:2.2px;text-transform:uppercase;color:#C9D3DB}
.cta{display:inline-flex;align-items:center;gap:12px;background:#169A47;color:#fff;border-radius:999px;padding:16px 30px;
     font:700 17px 'Plus Jakarta Sans';letter-spacing:1.4px;text-transform:uppercase;box-shadow:0 10px 30px rgba(22,154,71,.35)}
.g{color:#2FD46E}
.club{width:118px;height:118px;border-radius:28px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.10);
      display:flex;align-items:center;justify-content:center}
.club img{width:78px;height:78px;object-fit:contain}
.vs{font:800 22px 'Poppins';color:#6CC08B}
"""

def _club(src):
    return f'<div class="club"><img src="{html.escape(src)}"></div>'

def variant_a(d):
    vraag = f"{d['thuis']} of {d['uit']}: wie wint?"
    return f"""
<div class="b">
  <div class="glow" style="width:620px;height:520px;left:-160px;top:-260px;background:rgba(22,154,71,.55)"></div>
  <div class="glow" style="width:520px;height:420px;right:-120px;bottom:-240px;background:rgba(22,154,71,.30)"></div>
  <div style="position:absolute;left:56px;top:46px;display:flex;align-items:center;gap:16px">
    <span class="pill">{html.escape(d['comp'])}</span><span class="tag">Actie bij</span>
    <img src="toto.png" style="height:24px">
  </div>
  <div style="position:absolute;left:56px;top:100px;width:780px">
    <div style="font:800 50px/1.04 'Poppins';letter-spacing:-1px;white-space:nowrap">{html.escape(vraag)}</div>
    <div style="font:700 30px 'Poppins';margin-top:14px">Kies jouw favoriet: zet <span class="g">€1</span> in, krijg <span class="g">€50</span></div>
    <div style="font:600 16px 'Plus Jakarta Sans';color:#C9D3DB;margin-top:8px">Wint jouw ploeg? Dan ontvang je €50 aan Free Bets</div>
    <div style="margin-top:22px" class="cta">Pak 50x je inzet bij TOTO <span>→</span></div>
  </div>
  <div style="position:absolute;right:64px;top:92px;display:flex;flex-direction:column;align-items:center;gap:16px">
    <div style="display:flex;align-items:center;gap:22px">{_club(d['thuis_logo'])}<span class="vs">VS</span>{_club(d['uit_logo'])}</div>
    <div style="font:600 15px 'Plus Jakarta Sans';color:#C9D3DB">{html.escape(d['thuis'])} – {html.escape(d['uit'])}</div>
    <div style="font:700 14px 'Plus Jakarta Sans';color:#6CC08B;letter-spacing:1.5px;text-transform:uppercase">{html.escape(d['datum'])}</div>
  </div>
  <img class="logo-be" src="betexperts_logo.png" style="right:64px;top:44px">
  <div class="ksa">{KSA}</div>
</div>"""

def variant_b(d):
    return f"""
<div class="b" style="background:linear-gradient(115deg,#0B1117 0%,#0E1A15 55%,#0B1117 100%)">
  <div class="glow" style="width:560px;height:420px;left:380px;top:-200px;background:rgba(47,212,110,.30)"></div>
  <div style="position:absolute;left:56px;top:46px;display:flex;align-items:center;gap:16px">
    <span class="pill">50x je inzet</span><span class="tag">{html.escape(d['comp'])}</span>
  </div>
  <img class="logo-be" src="betexperts_logo.png" style="right:56px;top:44px">
  <div style="position:absolute;left:56px;top:112px;display:flex;align-items:center;gap:18px">
    {_club(d['thuis_logo'])}<span class="vs">VS</span>{_club(d['uit_logo'])}
  </div>
  <div style="position:absolute;left:56px;top:250px;font:700 17px 'Plus Jakarta Sans'">{html.escape(d['thuis'])} – {html.escape(d['uit'])}
     <span style="color:#6CC08B;margin-left:10px;font-weight:600">{html.escape(d['datum'])}</span></div>
  <div style="position:absolute;left:470px;top:96px;width:360px;height:196px;border-radius:22px;background:rgba(255,255,255,.04);
              border:1px dashed rgba(108,192,139,.55);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px">
    <div style="font:700 13px 'Plus Jakarta Sans';letter-spacing:2px;text-transform:uppercase;color:#C9D3DB;margin-bottom:4px">Kies jouw favoriet</div>
    <div style="display:flex;align-items:baseline;gap:14px;width:300px;justify-content:space-between">
      <span style="font:700 17px 'Plus Jakarta Sans';width:120px">{html.escape(d['thuis'])}</span>
      <span style="font:700 22px 'Poppins';color:#8A97A3;text-decoration:line-through;text-decoration-thickness:2px">{html.escape(d['odd_thuis'])}</span>
      <span style="font:700 18px 'Poppins';color:#6CC08B">→</span>
      <span style="font:800 40px/1.1 'Poppins';color:#2FD46E">50.00</span>
    </div>
    <div style="display:flex;align-items:baseline;gap:14px;width:300px;justify-content:space-between">
      <span style="font:700 17px 'Plus Jakarta Sans';width:120px">{html.escape(d['uit'])}</span>
      <span style="font:700 22px 'Poppins';color:#8A97A3;text-decoration:line-through;text-decoration-thickness:2px">{html.escape(d['odd_uit'])}</span>
      <span style="font:700 18px 'Poppins';color:#6CC08B">→</span>
      <span style="font:800 40px/1.1 'Poppins';color:#2FD46E">50.00</span>
    </div>
    <div style="font:600 14px 'Plus Jakarta Sans';color:#C9D3DB;margin-top:4px">€1 op de winnaar = €50 aan Free Bets</div>
  </div>
  <div style="position:absolute;right:56px;top:132px;display:flex;flex-direction:column;align-items:flex-end;gap:16px">
    <img src="toto.png" style="height:34px">
    <div class="cta">Claim bij TOTO <span>→</span></div>
  </div>
  <div class="ksa">{KSA}</div>
</div>"""

def variant_c(d):
    return f"""
<div class="b">
  <div style="position:absolute;left:0;top:0;bottom:0;width:430px;background:linear-gradient(160deg,#1DB257 0%,#169A47 55%,#0F7A37 100%)"></div>
  <div style="position:absolute;left:0;top:0;bottom:0;width:430px;background:radial-gradient(circle at 20% 15%,rgba(255,255,255,.22),transparent 55%)"></div>
  <div style="position:absolute;left:52px;top:44px;font:700 13px 'Plus Jakarta Sans';letter-spacing:2.2px;text-transform:uppercase;color:#E8FFF0">Actie bij</div>
  <img src="toto.png" style="position:absolute;left:150px;top:40px;height:24px">
  <div style="position:absolute;left:48px;top:86px;font:800 150px/1 'Poppins';letter-spacing:-4px;color:#fff">50x</div>
  <div style="position:absolute;left:54px;top:246px;font:700 26px 'Poppins';color:#fff">je inzet bij TOTO</div>
  <div class="glow" style="width:480px;height:380px;right:-140px;top:-180px;background:rgba(22,154,71,.35)"></div>
  <img class="logo-be" src="betexperts_logo.png" style="right:56px;top:44px">
  <div style="position:absolute;left:480px;top:96px;display:flex;align-items:center;gap:18px">
    {_club(d['thuis_logo']).replace('118px', '96px')}<span class="vs">VS</span>{_club(d['uit_logo']).replace('118px', '96px')}
    <div style="margin-left:10px">
      <div style="font:700 13px 'Plus Jakarta Sans';letter-spacing:2px;text-transform:uppercase;color:#6CC08B">{html.escape(d['comp'])}</div>
      <div style="font:700 19px 'Plus Jakarta Sans';margin-top:4px">{html.escape(d['thuis'])} – {html.escape(d['uit'])}</div>
      <div style="font:600 14px 'Plus Jakarta Sans';color:#C9D3DB;margin-top:2px">{html.escape(d['datum'])}</div>
    </div>
  </div>
  <div style="position:absolute;left:480px;top:236px;font:800 30px 'Poppins'">Zet €1 op <span class="g">jouw favoriet</span></div>
  <div style="position:absolute;left:480px;top:280px;font:600 17px 'Plus Jakarta Sans';color:#C9D3DB">
    Wint jouw ploeg? Dan krijg je <b style="color:#fff">€50 aan Free Bets</b> (normaal {html.escape(d['odd_thuis'])} of {html.escape(d['odd_uit'])}).</div>
  <div style="position:absolute;right:56px;top:224px" class="cta">Claim <span>→</span></div>
  <div class="ksa" style="left:480px;right:40px;font-size:11.5px;color:#8A97A3">{KSA}</div>
</div>"""

VARIANTEN = {"A": variant_a, "B": variant_b, "C": variant_c}

def render(data, variant, uitpad):
    from playwright.sync_api import sync_playwright
    d = dict(data)
    page_html = f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{VARIANTEN[variant](d)}</body></html>"
    tmp = os.path.join(HERE, f".tmp-{variant}.html")
    open(tmp, "w", encoding="utf-8").write(page_html)
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        p = b.new_page(viewport={"width": 1200, "height": 400}, device_scale_factor=2)
        p.goto("file://" + tmp); p.wait_for_load_state("networkidle")
        p.evaluate("document.fonts.ready")
        p.locator(".b").screenshot(path=uitpad, omit_background=True)
        b.close()
    os.remove(tmp)
    return uitpad

if __name__ == "__main__":
    voorbeeld = {"comp": "Champions League", "thuis": "FC Porto", "uit": "PSV", "odd_thuis": "1.57", "odd_uit": "4.50",
                 "thuis_logo": "https://media.api-sports.io/football/teams/212.png",
                 "uit_logo": "https://media.api-sports.io/football/teams/197.png", "datum": "di 20 okt · 21:00"}
    for v in (sys.argv[1:] or ["A", "B", "C"]):
        print(render(voorbeeld, v, os.path.join(HERE, f"voorbeeld-{v}.png")))
