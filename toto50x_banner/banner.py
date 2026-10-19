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
.club{width:132px;height:132px;border-radius:30px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.10);
      display:flex;align-items:center;justify-content:center}
.club img{width:88px;height:88px;object-fit:contain}
.vs{font:800 22px 'Poppins';color:#6CC08B}
"""

KORT = {"borussia monchengladbach": "Gladbach", "borussia mönchengladbach": "Gladbach", "1899 hoffenheim": "Hoffenheim",
        "tsg hoffenheim": "Hoffenheim", "borussia dortmund": "Dortmund", "bayer leverkusen": "Leverkusen", "bayern münchen": "Bayern",
        "bayern munich": "Bayern", "eintracht frankfurt": "Frankfurt", "vfb stuttgart": "Stuttgart", "rb leipzig": "Leipzig",
        "paris saint germain": "PSG", "paris saint-germain": "PSG", "manchester united": "Man United", "manchester city": "Man City",
        "tottenham hotspur": "Tottenham", "wolverhampton wanderers": "Wolves", "nottingham forest": "Forest",
        "brighton & hove albion": "Brighton", "west ham united": "West Ham", "newcastle united": "Newcastle",
        "atletico madrid": "Atlético", "atlético madrid": "Atlético", "athletic club": "Athletic", "real sociedad": "Sociedad",
        "psv eindhoven": "PSV", "az alkmaar": "AZ", "fc twente": "Twente", "fc utrecht": "Utrecht", "fc groningen": "Groningen",
        "sporting cp": "Sporting", "sporting lisbon": "Sporting", "olympique marseille": "Marseille", "olympique lyonnais": "Lyon",
        "inter milan": "Inter", "internazionale": "Inter", "ac milan": "Milan", "as roma": "Roma", "ss lazio": "Lazio"}

def kort(naam):
    """Korte clubnaam voor de kop (lange namen maken de banner onleesbaar)."""
    n = (naam or "").strip(); k = KORT.get(n.lower())
    if k:
        return k
    if len(n) > 14:
        for weg in ("FC ", "AFC ", "SC ", "SV ", "AS ", "SS ", "VfB ", "VfL ", "1. FC ", "Club "):
            if n.startswith(weg): n = n[len(weg):]
        for weg in (" FC", " CF", " SC", " AC"):
            if n.endswith(weg): n = n[: -len(weg)]
    return n

def _club(src):
    return f'<div class="club"><img src="{html.escape(src)}"></div>'

def variant_a(d, mobiel=False):
    """Gekozen ontwerp (19-10-2026). Desktop 1400x514 (zelfde maat als de andere CTA's), mobiel 1080x960."""
    th, ut = kort(d['thuis']), kort(d['uit'])
    vraag = f"{th} of {ut}: wie wint?"
    w, h = (1080, 960) if mobiel else (1400, 514)
    clubs = f'''<div style="display:flex;align-items:center;gap:{26 if mobiel else 22}px">{_club(d['thuis_logo'])}<span class="vs">VS</span>{_club(d['uit_logo'])}</div>'''
    wedstrijd = f'''<div style="font:600 {24 if mobiel else 17}px 'Plus Jakarta Sans';color:#C9D3DB;margin-top:16px;max-width:330px;text-align:center">{html.escape(th)} – {html.escape(ut)}</div>
      <div style="font:700 {19 if mobiel else 15}px 'Plus Jakarta Sans';color:#6CC08B;letter-spacing:1.5px;text-transform:uppercase;margin-top:8px">{html.escape(d['datum'])}</div>'''
    tags = f'''<div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap">
      <span class="pill">{html.escape(d['comp'])}</span><span class="tag">Actie bij</span><img src="toto.png" style="height:{30 if mobiel else 26}px"></div>'''
    tekst = f'''<div class="fit" style="font:800 {66 if mobiel else 58}px/1.05 'Poppins';letter-spacing:-1px;white-space:nowrap">{html.escape(vraag)}</div>
      <div style="font:700 {38 if mobiel else 32}px 'Poppins';margin-top:16px">Kies jouw favoriet: zet <span class="g">€1</span> in, krijg <span class="g">€50</span></div>
      <div style="font:600 {22 if mobiel else 18}px 'Plus Jakarta Sans';color:#C9D3DB;margin-top:10px">Wint jouw ploeg? Dan ontvang je €50 aan Free Bets</div>
      <div style="margin-top:{34 if mobiel else 28}px" class="cta">Pak 50x je inzet bij TOTO <span>→</span></div>'''
    if mobiel:
        binnen = f'''
  <div style="position:absolute;left:64px;right:64px;top:60px;display:flex;justify-content:space-between;align-items:center">
    {tags}<img src="betexperts_logo.png" style="height:34px"></div>
  <div style="position:absolute;left:64px;right:64px;top:180px;display:flex;flex-direction:column;align-items:center">{clubs.replace('class="club"', 'class="club" style="width:170px;height:170px"').replace('<img src', '<img style="width:112px;height:112px" src')}{wedstrijd}</div>
  <div class="vak" style="position:absolute;left:64px;right:64px;top:530px">{tekst}</div>
  <div class="ksa" style="left:64px;right:64px;bottom:34px;font-size:17px;line-height:1.45">{KSA}</div>'''
    else:
        binnen = f'''
  <div style="position:absolute;left:64px;top:60px">{tags}</div>
  <img class="logo-be" src="betexperts_logo.png" style="right:72px;top:54px;height:30px">
  <div class="vak" style="position:absolute;left:64px;top:150px;width:860px">{tekst}</div>
  <div style="position:absolute;right:72px;top:162px;display:flex;flex-direction:column;align-items:center">{clubs}{wedstrijd}</div>
  <div class="ksa" style="left:64px;bottom:26px;font-size:14px">{KSA}</div>'''
    return f'''
<div class="b" style="width:{w}px;height:{h}px">
  <div class="glow" style="width:{720 if not mobiel else 900}px;height:600px;left:-180px;top:-300px;background:rgba(22,154,71,.55)"></div>
  <div class="glow" style="width:600px;height:480px;right:-140px;bottom:-260px;background:rgba(22,154,71,.30)"></div>{binnen}
</div>'''

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

FIT_JS = """for (const el of document.querySelectorAll('.fit')) { const box = el.closest('.vak');
  let fs = parseFloat(getComputedStyle(el).fontSize); while (el.scrollWidth > box.clientWidth && fs > 30) { fs -= 1; el.style.fontSize = fs + 'px'; } }"""

def render(data, variant, uitpad, mobiel=False, browser=None):
    """Rendert één banner naar PNG (2x). variant 'A' (gekozen) ondersteunt mobiel=True. Geef een open Playwright-browser mee
    om bij veel banners niet steeds opnieuw te starten."""
    d = dict(data)
    body = variant_a(d, mobiel) if variant == "A" else VARIANTEN[variant](d)
    w, h = ((1080, 960) if mobiel else (1400, 514)) if variant == "A" else (1200, 400)
    page_html = f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>"
    tmp = os.path.join(HERE, f".tmp-{os.getpid()}-{variant}{'m' if mobiel else ''}.html")
    open(tmp, "w", encoding="utf-8").write(page_html)
    def _doe(b):
        p = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=2 if not mobiel else 1.5)
        p.goto("file://" + tmp); p.wait_for_load_state("networkidle")
        p.evaluate("document.fonts.ready"); p.evaluate(FIT_JS)
        p.locator(".b").screenshot(path=uitpad, omit_background=True)
        p.close()
    try:
        if browser:
            _doe(browser)
        else:
            from playwright.sync_api import sync_playwright
            with sync_playwright() as pw:
                b = pw.chromium.launch(); _doe(b); b.close()
    finally:
        os.remove(tmp)
    return uitpad

if __name__ == "__main__":
    voorbeeld = {"comp": "Champions League", "thuis": "FC Porto", "uit": "PSV", "odd_thuis": "1.57", "odd_uit": "4.50",
                 "thuis_logo": "https://media.api-sports.io/football/teams/212.png",
                 "uit_logo": "https://media.api-sports.io/football/teams/197.png", "datum": "di 20 okt · 21:00"}
    print(render(voorbeeld, "A", os.path.join(HERE, "voorbeeld-A.png")))
    print(render(voorbeeld, "A", os.path.join(HERE, "voorbeeld-A-mobiel.png"), mobiel=True))
    lang = dict(voorbeeld, thuis="Borussia Mönchengladbach", uit="1899 Hoffenheim", comp="Bundesliga")
    print(render(lang, "A", os.path.join(HERE, "voorbeeld-A-lang.png")))
