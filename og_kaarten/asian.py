# -*- coding: utf-8 -*-
"""Infographics (A4 png+pdf) Asian Handicap-tabel en Asian Totaal-tabel, voorbeeldvisual en deelkaart.
Uitkomsten berekend met asian_rekenen.py (geen handwerk).  ../superodd-agent/.venv/bin/python og_kaarten/asian.py <uitmap>"""
import sys, uuid, pathlib
sys.path.insert(0, "/Users/jaspervandenboogaard/bet-experts/preview-images-agent")
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import kaart
from asian_rekenen import handicap, totaal, uitbetaling
from playwright.sync_api import sync_playwright

A = pathlib.Path(kaart.ASSETS)
UIT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(__file__).parent)
G = "#2FD46E"
KL = {1: ("Winst", "#2FD46E", "#0B1117"), 0.5: ("½ winst", "#A6EBC0", "#0B1117"), 0: ("Terug", "#4A535D", "#F5F9FA"),
      -0.5: ("½ verlies", "#FFB7C1", "#5A0F1B"), -1: ("Verlies", "#E5394F", "#FFFFFF")}


def nl(x, plus=True):
    s = f"{abs(x):.2f}".rstrip("0").rstrip(".").replace(".", ",")
    if x > 0 and plus: return "+" + s
    if x < 0: return "−" + s
    return s


def cel(u):
    t, bg, fg = KL[u]
    return f'<div class="c" style="background:{bg};color:{fg}">{t}</div>'


BASE = kaart.CSS + f"""
.eb{{font:700 15px 'Plus Jakarta Sans';letter-spacing:3.5px;color:#6CC08B;text-transform:uppercase}}
.k{{font:700 12px 'Plus Jakarta Sans';letter-spacing:2px;color:#8A97A3;text-transform:uppercase}}
.p{{width:1240px;height:1754px;position:relative;overflow:hidden;background:#0B1117}}
.col{{position:absolute;inset:50px 56px 38px;display:flex;flex-direction:column}}
.pre{{display:inline-block;font:800 24px 'Poppins';letter-spacing:8px;color:#0B1117;background:{G};border-radius:10px;padding:5px 12px 5px 20px;text-transform:uppercase}}
.tt{{font:800 96px/0.92 'Poppins';letter-spacing:-3px;text-transform:uppercase;text-align:center}} .tt em{{font-style:normal;color:{G}}}
.sub{{font:600 21px/1.4 'Plus Jakarta Sans';color:#DDE4EA;text-align:center}}
.leg{{display:flex;justify-content:center;gap:10px;flex-wrap:wrap}}
.lg{{display:inline-flex;align-items:center;gap:9px;font:700 16px 'Plus Jakarta Sans';color:#DDE4EA}}
.lg i{{width:26px;height:18px;border-radius:5px;display:inline-block}}
.grid{{display:grid;gap:5px;align-items:stretch}}
.h{{font:800 14px/1.15 'Poppins';color:#C9D3DB;text-align:center;display:flex;align-items:flex-end;justify-content:center;padding-bottom:6px;text-transform:uppercase;letter-spacing:.3px}}
.rl{{display:flex;align-items:center;justify-content:center;border-radius:9px;background:rgba(255,255,255,.07);font:800 22px 'Poppins';color:#F5F9FA}}
.c{{display:flex;align-items:center;justify-content:center;border-radius:9px;font:800 16px 'Plus Jakarta Sans'}}
.sec{{grid-column:1/-1;font:800 15px 'Poppins';letter-spacing:1.5px;text-transform:uppercase;color:#6CC08B;padding:12px 2px 4px}}
.box{{border-radius:20px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.10);padding:18px 22px}}
.box b{{color:#F5F9FA}} .box .t{{font:800 19px 'Poppins'}} .box .s{{font:600 16px/1.45 'Plus Jakarta Sans';color:#C9D3DB;margin-top:6px}}
.foot{{display:flex;justify-content:space-between;align-items:center;margin-top:16px}}
"""
GLOW = '''<div class="glow" style="width:900px;height:700px;left:-300px;top:-380px;background:rgba(22,154,71,.50)"></div>
<div class="glow" style="width:800px;height:700px;right:-320px;bottom:-360px;background:rgba(22,154,71,.30)"></div>'''


def voet():
    return f'''<div style="margin-top:auto"><div style="height:1px;background:rgba(255,255,255,.10)"></div>
  <div class="foot"><div style="font:600 15px 'Plus Jakarta Sans';color:#8A97A3">Wat kost gokken jou? Stop op tijd. 18+</div>
  <div style="font:800 19px 'Poppins';color:#6CC08B">bet-experts.nl</div></div></div>'''


def legenda():
    return '<div class="leg">' + "".join(f'<span class="lg"><i style="background:{bg}"></i>{t}</span>' for u, (t, bg, fg) in sorted(KL.items(), reverse=True)) + "</div>"


# ---------- infographic 1: Asian Handicap
KOL = [(3, "Wint met<br>3+"), (2, "Wint met<br>2"), (1, "Wint met<br>1"), (0, "Gelijk-<br>spel"), (-1, "Verliest<br>met 1"), (-2, "Verliest<br>met 2"), (-3, "Verliest<br>met 3+")]
LIJNEN_H = [-2, -1.75, -1.5, -1.25, -1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]


def ah_rij(l):
    return f'<div class="rl">{nl(l)}</div>' + "".join(cel(handicap(l, ds)) for ds, _ in KOL)


gh = '<div class="h">Jouw<br>handicap</div>' + "".join(f'<div class="h">{t}</div>' for _, t in KOL)
rows = '<div class="sec">Je team is favoriet: begint met een achterstand</div>' + "".join(ah_rij(l) for l in LIJNEN_H if l < 0)
rows += '<div class="sec">Gelijk: draw no bet</div>' + ah_rij(0)
rows += '<div class="sec">Je team is underdog: begint met een voorsprong</div>' + "".join(ah_rij(l) for l in LIJNEN_H if l > 0)
ex = uitbetaling(0.5, 10, 1.90)
INFO_AH = f'''<div class="p">{GLOW}<div class="col">
  <div style="text-align:center"><img src="betexperts_logo.png" style="height:42px">
    <div style="margin-top:22px"><span class="pre">Asian</span></div>
    <div class="tt" style="margin-top:10px">Handicap <em>tabel</em></div>
    <div class="sub" style="margin-top:14px">Kies je handicap (rij) en kijk naar de uitslag van <b style="color:#fff">jouw team</b> (kolom).<br>Dan zie je direct wat er met je inzet gebeurt.</div></div>
  <div style="margin-top:18px">{legenda()}</div>
  <div class="grid" style="margin-top:14px;grid-template-columns:140px repeat(7,1fr);grid-auto-rows:48px">
    <div style="display:contents">{gh.replace('class="h"','class="h" style="height:44px"')}</div>{rows}</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:20px">
    <div class="box"><div class="t">Kwartlijn = inzet in tweeën</div><div class="s">Bij <b>−0,75</b> gaat de helft van je inzet op <b>−0,5</b> en de helft op <b>−1</b>. Wint je team met 1 doelpunt, dan win je de ene helft en krijg je de andere helft terug.</div></div>
    <div class="box"><div class="t">Voorbeeld: €10 op −0,75 (odd 1,90)</div><div class="s">Je team wint <b>2-1</b>: ½ winst. Je krijgt €5 × 1,90 = €9,50 + €5 terug = <b>€{ex:.2f}</b>.<br>Wint je team met 2 of meer: <b>€19,00</b>.</div></div>
  </div>
  {voet()}</div></div>'''.replace("€14.50", "€14,50")

# ---------- infographic 2: Asian Totaal
GOALS = [(0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5+")]
LIJNEN_T = [1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5]


def at_rij(l, over):
    return f'<div class="rl" style="font-size:19px">{"Meer" if over else "Minder"} dan {nl(l, False)}</div>' + "".join(cel(totaal(l, g, over)) for g, _ in GOALS)


gh2 = '<div class="h">Lijn</div>' + "".join(f'<div class="h">{t} goal{"s" if t != "1" else ""}</div>' for _, t in GOALS)
rows2 = '<div class="sec">Over: meer dan … doelpunten</div>' + "".join(at_rij(l, True) for l in LIJNEN_T)
rows2 += '<div class="sec">Under: minder dan … doelpunten</div>' + "".join(at_rij(l, False) for l in LIJNEN_T)
ex2 = uitbetaling(-0.5, 10, 1.85)
INFO_AT = f'''<div class="p">{GLOW}<div class="col">
  <div style="text-align:center"><img src="betexperts_logo.png" style="height:42px">
    <div style="margin-top:22px"><span class="pre">Asian</span></div>
    <div class="tt" style="margin-top:10px">Totaal <em>tabel</em></div>
    <div class="sub" style="margin-top:14px">Asian over/under op het aantal doelpunten in de wedstrijd.<br>Kies je lijn (rij) en kijk hoeveel goals er vallen (kolom).</div></div>
  <div style="margin-top:18px">{legenda()}</div>
  <div class="grid" style="margin-top:14px;grid-template-columns:200px repeat(6,1fr);grid-auto-rows:46px">
    <div style="display:contents">{gh2.replace('class="h"','class="h" style="height:34px"')}</div>{rows2}</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:18px">
    <div class="box"><div class="t">Hele lijn: geld terug mogelijk</div><div class="s">Bij <b>meer dan 2</b> en precies 2 doelpunten krijg je je <b>volledige inzet terug</b>. Bij 3 of meer win je.</div></div>
    <div class="box"><div class="t">Voorbeeld: €10 op meer dan 2,25 (odd 1,85)</div><div class="s">Er vallen <b>2 goals</b>: ½ verlies, je krijgt <b>€{ex2:.2f}</b> terug.<br>Vallen er 3 of meer: <b>€18,50</b>.</div></div>
  </div>
  {voet()}</div></div>'''.replace("€5.00", "€5,00")

# ---------- uitlegvisual: voorbeeld met bedragen
SC = [("PSV wint met 2 of meer", "bv. 2-0 of 3-1", 1), ("PSV wint met 1", "bv. 2-1", 0.5), ("Gelijk of PSV verliest", "bv. 1-1 of 0-1", -1)]
def scen(t, s, u, odd=1.90):
    lab, bg, fg = KL[u]; b = uitbetaling(u, 10, odd); w = b - 10
    eur = lambda x: f"€{x:.2f}".replace(".", ",")
    return (f'<div class="box" style="padding:20px"><div class="k">{s}</div><div class="t" style="margin-top:6px">{t}</div>'
            f'<div style="margin-top:14px;display:inline-flex;border-radius:8px;padding:6px 12px;font:800 16px Plus Jakarta Sans;background:{bg};color:{fg}">{lab}</div>'
            f'<div style="margin-top:14px;font:800 34px Poppins">{eur(b)}</div><div class="s" style="margin-top:2px">je krijgt terug · {"winst +" + eur(w) if w > 0 else "verlies −" + eur(-w)}</div></div>')
def vis(kop, sub, verdeel, kaarten):
    return f'''<div class="b" style="height:580px">{GLOW}
  <img src="betexperts_logo.png" style="position:absolute;left:56px;top:44px;height:28px">
  <div style="position:absolute;right:56px;top:40px;font:700 15px 'Plus Jakarta Sans'">{sub} <span style="color:#8A97A3;font-weight:600">· voorbeeld</span></div>
  <div style="position:absolute;left:56px;right:56px;top:108px">
    <div class="eb">Rekenvoorbeeld</div>
    <div style="font:800 40px/1.1 'Poppins';letter-spacing:-.8px;margin-top:8px">{kop}</div>
    <div style="margin-top:22px;display:flex;align-items:center;gap:12px;font:700 17px 'Plus Jakarta Sans';color:#C9D3DB">Je inzet wordt verdeeld:
      {"+".join(f'<span style="border-radius:10px;padding:8px 14px;background:rgba(47,212,110,.14);border:1px solid rgba(47,212,110,.45);color:#fff">{v}</span>' for v in verdeel)}</div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:24px">{kaarten}</div>
  </div>
  <div style="position:absolute;left:56px;right:56px;bottom:52px;height:1px;background:rgba(255,255,255,.08)"></div>
  <div style="position:absolute;left:56px;bottom:20px;font-size:13px;color:#8A97A3">Wat kost gokken jou? Stop op tijd. 18+ · Voorbeeldquotering</div>
  <div style="position:absolute;right:56px;bottom:20px;font:700 13px 'Plus Jakarta Sans';color:#6CC08B">bet-experts.nl</div></div>'''
VIS = vis(f'€10 op <span style="color:{G}">PSV −0,75</span> tegen Feyenoord, odd 1,90', "Asian Handicap",
          ["€5 op −0,5", "€5 op −1"], "".join(scen(*x) for x in SC))
SC_T = [("0 of 1 doelpunt", "bv. 0-0 of 1-0", -1), ("Precies 2 doelpunten", "bv. 1-1 of 2-0", -0.5), ("3 doelpunten of meer", "bv. 2-1 of 3-1", 1)]
VIS_T = vis(f'€10 op <span style="color:{G}">meer dan 2,25</span> doelpunten, odd 1,85', "Asian totaal",
            ["€5 op meer dan 2", "€5 op meer dan 2,5"], "".join(scen(t, s_, u, 1.85) for t, s_, u in SC_T))

# ---------- deelkaart
mini_l = [-1, -0.75, -0.5, -0.25, 0]
mini = "".join(f'<div class="rl" style="font-size:16px">{nl(l)}</div>' + "".join(cel(handicap(l, ds)).replace('class="c"', 'class="c" style="font-size:12px;') .replace('style="font-size:12px; style="', 'style="font-size:12px;') for ds in (2, 1, 0, -1)) for l in mini_l)
OG = f'''<div class="b">{GLOW}
  <img src="betexperts_logo.png" style="position:absolute;left:56px;top:44px;height:28px">
  <div style="position:absolute;right:56px;top:40px;font:700 15px 'Plus Jakarta Sans'">Kennisbank <span style="color:#8A97A3;font-weight:600">· met tabel + gratis pdf</span></div>
  <div style="position:absolute;left:56px;right:56px;top:152px;display:flex;gap:36px;align-items:center">
    <div style="flex:1;min-width:0"><div class="eb">Uitleg met voorbeelden</div>
      <div style="font:800 62px/1.0 'Poppins';letter-spacing:-1.6px;margin-top:14px">Wat is een<br><span style="color:{G}">Asian Handicap</span>?</div>
      <div style="margin-top:24px;display:flex;gap:10px;flex-wrap:wrap">
        <span style="border-radius:999px;padding:9px 16px;font:700 15px Plus Jakarta Sans;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12)">Handicap + Asian totaal</span>
        <span style="border-radius:999px;padding:9px 16px;font:700 15px Plus Jakarta Sans;background:{G};color:#0B1117">Halve winst uitgelegd</span></div></div>
    <div style="width:440px;flex:none" class="box"><div class="grid" style="grid-template-columns:70px repeat(4,1fr);grid-auto-rows:40px">
      <div class="h" style="font-size:11px">Lijn</div><div class="h" style="font-size:11px">Wint 2+</div><div class="h" style="font-size:11px">Wint 1</div><div class="h" style="font-size:11px">Gelijk</div><div class="h" style="font-size:11px">Verlies 1</div>
      {mini}</div></div></div>
  <div style="position:absolute;left:56px;right:56px;bottom:52px;height:1px;background:rgba(255,255,255,.08)"></div>
  <div style="position:absolute;left:56px;bottom:20px;font-size:13px;color:#8A97A3">Wat kost gokken jou? Stop op tijd. 18+</div>
  <div style="position:absolute;right:56px;bottom:20px;font:700 13px 'Plus Jakarta Sans';color:#6CC08B">bet-experts.nl</div></div>'''

PDF_CSS = ".glow{display:none}.p{background:linear-gradient(160deg,#0F2A1C 0%,#0B1117 35%,#0B1117 70%,#0E2418 100%)}"


def render():
    UIT.mkdir(parents=True, exist_ok=True); tmp = []
    docs = [("ah-tabel", INFO_AH, 1240, 1754, True), ("at-tabel", INFO_AT, 1240, 1754, True), ("vis-voorbeeld", VIS, 1200, 580, False), ("vis-totaal", VIS_T, 1200, 580, False), ("og", OG, 1200, 630, False)]
    try:
        with sync_playwright() as p:
            b = p.chromium.launch(args=["--font-render-hinting=none"])
            for naam, body, w, h, pdf in docs:
                f = A / f".as-{uuid.uuid4().hex[:8]}.html"; tmp.append(f)
                f.write_text(f"<!doctype html><html lang='nl'><head><meta charset='utf-8'><style>{BASE}</style></head><body>{body}</body></html>", encoding="utf-8")
                pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=2)
                pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
                pg.screenshot(path=str(UIT / f"{naam}.png"))
                if pdf:
                    pg.emulate_media(media="screen"); pg.add_style_tag(content=PDF_CSS)
                    pg.pdf(path=str(UIT / f"{naam}.pdf"), width=f"{w}px", height=f"{h}px", print_background=True, margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
            b.close()
    finally:
        for f in tmp: f.unlink(missing_ok=True)
    print(UIT)


if __name__ == "__main__":
    render()
