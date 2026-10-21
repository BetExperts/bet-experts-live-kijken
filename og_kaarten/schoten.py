# -*- coding: utf-8 -*-
"""Visuals + deelkaarten voor de artikelen over schoten op doel en Opta-gegevens (kaartstijl preview-images-agent).
  ../superodd-agent/.venv/bin/python og_kaarten/schoten.py <uitmap>"""
import sys, uuid, pathlib
sys.path.insert(0, "/Users/jaspervandenboogaard/bet-experts/preview-images-agent")
import kaart
from playwright.sync_api import sync_playwright

A = pathlib.Path(kaart.ASSETS)
UIT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(__file__).parent)
G, R = "#2FD46E", "#FF6B81"

CSS = kaart.CSS + f"""
.eb{{font:700 14px 'Plus Jakarta Sans';letter-spacing:3px;color:#6CC08B;text-transform:uppercase}}
.k{{font:700 12px 'Plus Jakarta Sans';letter-spacing:2.5px;color:#8A97A3;text-transform:uppercase}}
.tt{{font:800 54px/1.02 'Poppins';letter-spacing:-1.4px}} .tt em{{font-style:normal;color:{G}}}
.h2{{font:800 38px/1.05 'Poppins';letter-spacing:-.8px}} .h2 em{{font-style:normal;color:{G}}}
.pan{{border-radius:24px;padding:20px 22px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.10)}}
.ok,.no,.nr{{width:30px;height:30px;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center;font:800 15px 'Poppins'}}
.ok{{background:{G};color:#0B1117}} .no{{background:rgba(255,107,129,.16);color:{R};box-shadow:inset 0 0 0 1.5px rgba(255,107,129,.6)}}
.li{{display:flex;align-items:center;gap:12px;padding:10px 0;border-top:1px solid rgba(255,255,255,.07)}}
.li:first-of-type{{border-top:none}}
.li .t{{font:700 17px/1.2 'Plus Jakarta Sans'}} .li .s{{font:600 13.5px/1.3 'Plus Jakarta Sans';color:#8A97A3;margin-top:2px}}
.fm{{display:inline-flex;align-items:center;gap:8px;border-radius:999px;padding:9px 16px;font:700 15px 'Plus Jakarta Sans';
  background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);white-space:nowrap}} .fm b{{font:800 16px 'Poppins';color:{G}}}
.box{{border-radius:18px;padding:16px 18px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.10)}}
.box.g{{border-color:rgba(47,212,110,.45);background:rgba(47,212,110,.08)}} .box.r{{border-color:rgba(255,107,129,.40);background:rgba(255,107,129,.06)}}
.box .t{{font:800 20px 'Poppins'}} .box .s{{font:600 14px/1.35 'Plus Jakarta Sans';color:#C9D3DB;margin-top:4px}}
"""

GLOW = '''<div class="glow" style="width:760px;height:560px;left:-220px;top:-300px;background:rgba(22,154,71,.50)"></div>
  <div class="glow" style="width:600px;height:460px;right:-160px;bottom:-280px;background:rgba(22,154,71,.26)"></div>'''


def kop(rechts):
    return f'''<img src="betexperts_logo.png" style="position:absolute;left:56px;top:44px;height:28px">
  <div style="position:absolute;right:56px;top:40px;display:flex;align-items:center;gap:10px">
    <span style="width:8px;height:8px;border-radius:50%;background:{G}"></span>
    <span style="font:700 15px 'Plus Jakarta Sans'">Voetbal wedden</span>
    <span style="font:600 13px 'Plus Jakarta Sans';color:#8A97A3">· {rechts}</span></div>'''


def voet(h):
    return f'''<div style="position:absolute;left:56px;right:56px;bottom:52px;height:1px;background:rgba(255,255,255,.08)"></div>
  <div style="position:absolute;left:56px;bottom:20px;font-size:13px;color:#8A97A3">Wat kost gokken jou? Stop op tijd. 18+</div>
  <div style="position:absolute;right:56px;bottom:20px;font:700 13px 'Plus Jakarta Sans';color:#6CC08B">bet-experts.nl</div>'''


def doel_svg(w=520, h=300):
    # doel met net, paal/lat en genummerde markers
    net = "".join(f'<line x1="{x}" y1="40" x2="{x}" y2="230" stroke="rgba(255,255,255,.10)"/>' for x in range(80, 460, 22))
    net += "".join(f'<line x1="60" y1="{y}" x2="460" y2="{y}" stroke="rgba(255,255,255,.10)"/>' for y in range(56, 230, 22))
    def m(x, y, n, ok):
        c = G if ok else R
        fill = G if ok else "rgba(255,107,129,.18)"
        tc = "#0B1117" if ok else R
        return (f'<circle cx="{x}" cy="{y}" r="17" fill="{fill}" stroke="{c}" stroke-width="2"/>'
                f'<text x="{x}" y="{y+6}" text-anchor="middle" font-family="Poppins" font-weight="800" font-size="17" fill="{tc}">{n}</text>')
    return f'''<svg width="{w}" height="{h}" viewBox="0 0 520 300" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="230" width="520" height="70" fill="rgba(47,212,110,.07)"/>
  <line x1="0" y1="230" x2="520" y2="230" stroke="rgba(255,255,255,.55)" stroke-width="3"/>
  {net}
  <path d="M60 230 V40 H460 V230" fill="none" stroke="#F5F9FA" stroke-width="9" stroke-linejoin="round"/>
  <g transform="translate(230,150)"><circle r="16" fill="#C9D3DB"/><rect x="-14" y="16" width="28" height="44" rx="10" fill="#C9D3DB"/>
    <rect x="-46" y="20" width="32" height="10" rx="5" fill="#C9D3DB" transform="rotate(-25 -14 25)"/><rect x="14" y="20" width="32" height="10" rx="5" fill="#C9D3DB" transform="rotate(25 14 25)"/></g>
  {m(390, 95, 1, True)}{m(185, 120, 2, True)}{m(330, 222, 3, True)}{m(460, 140, 4, False)}{m(500, 70, 5, False)}{m(110, 272, 6, False)}
</svg>'''


LEGENDA = [("ok", "Doelpunt", "Ook via paal of lat, of een (afgebogen) bal die erin gaat"),
           ("ok", "Redding van de keeper", "Een schot dat erin zou gaan, maar wordt gestopt"),
           ("ok", "Gestopt door de laatste man", "Van de lijn gehaald, de keeper is al verslagen"),
           ("no", "Paal of lat", "Telt niet, tenzij de bal daarna in het doel gaat"),
           ("no", "Naast of over", "Een gemiste poging zonder tussenkomst"),
           ("no", "Geblokt door een verdediger", "Als er nog spelers of de keeper achter staan")]
leg = "".join(f'<div class="li"><span class="{c}">{i}</span><div><div class="t">{t}</div><div class="s">{s}</div></div></div>'
              for i, (c, t, s) in enumerate(LEGENDA, 1))

VIS_DOEL = f'''<div class="b" style="height:720px">{GLOW}{kop("Volgens Opta")}
  <div style="position:absolute;left:56px;right:56px;top:112px">
    <div class="eb">Uitgelegd met voorbeelden</div>
    <div class="h2" style="margin-top:10px">Wat telt als <em>schot op doel</em>?</div></div>
  <div style="position:absolute;left:56px;top:226px;width:540px">
    <div class="pan" style="padding:14px 10px 6px">{doel_svg()}</div>
    <div style="display:flex;gap:10px;margin-top:16px;flex-wrap:wrap"><span class="fm">Kopbal <b>telt</b></span><span class="fm">Penalty <b>telt</b></span><span class="fm">Verlenging <b style="color:{R}">telt niet</b></span></div>
  </div>
  <div style="position:absolute;right:56px;top:226px;width:520px" class="pan">{leg}</div>
  {voet(820)}</div>'''

# Opta-stroomschema
VIS_OPTA = f'''<div class="b" style="height:660px">{GLOW}{kop("Opta-definities")}
  <div style="position:absolute;left:56px;right:56px;top:112px">
    <div class="eb">Zo registreert Opta een schot</div>
    <div class="h2" style="margin-top:10px">Van <em>doelpoging</em> tot schot op doel</div></div>
  <div style="position:absolute;left:56px;right:56px;top:232px">
    <div class="box" style="width:440px;margin:0 auto;text-align:center"><div class="t">Bewuste doelpoging</div><div class="s">Elke poging om te scoren, ook een kopbal of penalty</div></div>
    <div style="height:30px;width:2px;background:rgba(255,255,255,.25);margin:0 auto"></div>
    <div style="height:2px;background:rgba(255,255,255,.25);margin:0 135px"></div>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px">
      {"".join(f'<div style="display:flex;flex-direction:column;align-items:center"><div style="height:24px;width:2px;background:rgba(255,255,255,.25)"></div><div class="box {c}" style="width:100%;min-height:150px"><div class="t">{t}</div><div class="s">{s}</div><div style="margin-top:10px;font:800 13px Poppins;letter-spacing:1px;color:{G if c=="g" else R}">{lab}</div></div></div>' for c,t,s,lab in [
        ("g","Doelpunt","Ook als de bal via paal, lat of een verdediger erin gaat","OP DOEL ✓"),
        ("g","Op doel, gestopt","Gered door de keeper of van de lijn gehaald door de laatste man","OP DOEL ✓"),
        ("r","Naast","Naast, over of tegen paal of lat zonder doelpunt","GEEN SCHOT OP DOEL"),
        ("r","Geblokt","Tegengehouden door een speler met nog iemand achter zich","GEEN SCHOT OP DOEL")])}
    </div>
    <div style="margin-top:22px;text-align:center;font:600 15px 'Plus Jakarta Sans';color:#8A97A3">Alle vier tellen wél als <b style="color:#F5F9FA">schot</b> (totaal). Alleen de groene tellen als <b style="color:{G}">schot op doel</b>.</div>
  </div>
  {voet(760)}</div>'''

# Lijnen 1+ / 2+ / 3+
LIJNEN = [("1+", "Meer dan 0,5", "Minimaal 1 schot op doel"), ("2+", "Meer dan 1,5", "Minimaal 2 schoten op doel"),
          ("3+", "Meer dan 2,5", "Minimaal 3 schoten op doel")]
VIS_LIJN = f'''<div class="b" style="height:560px">{GLOW}{kop("Over/under uitgelegd")}
  <div style="position:absolute;left:56px;right:56px;top:112px">
    <div class="eb">Wat betekent 1+ schoten op doel?</div>
    <div class="h2" style="margin-top:10px">De lijnen bij <em>spelersweddenschappen</em></div></div>
  <div style="position:absolute;left:56px;right:56px;top:240px;display:grid;grid-template-columns:repeat(3,1fr);gap:18px">
    {"".join(f'<div class="box g" style="padding:20px 22px"><div style="font:800 54px/1 Poppins;color:{G}">{a}</div><div class="t" style="margin-top:10px">{b}</div><div class="s">{c}</div></div>' for a,b,c in LIJNEN)}
  </div>
  <div style="position:absolute;left:56px;right:56px;top:432px;font:600 15px 'Plus Jakarta Sans';color:#8A97A3">Under (minder dan) is het omgekeerde: <b style="color:#F5F9FA">minder dan 1,5</b> wint bij 0 of 1 schot op doel.</div>
  {voet(560)}</div>'''

OG_A = f'''<div class="b">{GLOW}{kop("Complete uitleg")}
  <div style="position:absolute;left:56px;right:56px;top:168px;display:flex;gap:30px;align-items:center">
    <div style="flex:1;min-width:0"><div class="eb">Regels, markten en tips</div>
      <div class="tt" style="margin-top:14px">Wedden op<br><em>schoten op doel</em></div>
      <div style="margin-top:26px;display:flex;gap:10px;flex-wrap:wrap"><span class="fm">Afgehandeld op <b>Opta</b></span><span class="fm">Gem. <b>10,4</b> per Eredivisie-duel</span></div></div>
    <div style="width:470px;flex:none" class="pan">{doel_svg(426,246)}</div></div>
  {voet(630)}</div>'''

OG_B = f'''<div class="b">{GLOW}{kop("Uitleg")}
  <div style="position:absolute;left:56px;right:56px;top:160px;display:flex;gap:36px;align-items:center">
    <div style="flex:1;min-width:0"><div class="eb">Alles over Opta-gegevens</div>
      <div class="tt" style="margin-top:14px">Wat zijn<br><em>Opta-gegevens</em>?</div>
      <div style="margin-top:26px;display:flex;gap:10px;flex-wrap:wrap"><span class="fm">Sinds <b>1996</b></span><span class="fm"><b>13.000</b> datapunten per duel</span></div></div>
    <div style="width:460px;flex:none" class="pan">
      <div class="k" style="margin-bottom:6px">Schot op doel volgens Opta</div>
      <div class="li"><span class="ok">✓</span><div class="t">Doelpunt of redding keeper</div></div>
      <div class="li"><span class="ok">✓</span><div class="t">Gestopt door de laatste man</div></div>
      <div class="li"><span class="no">✕</span><div class="t">Paal of lat zonder doelpunt</div></div>
      <div class="li"><span class="no">✕</span><div class="t">Geblokt door een verdediger</div></div>
      <div class="li"><span class="ok">✓</span><div class="t">Gebruikt door TOTO en Unibet</div></div></div></div>
  {voet(630)}</div>'''

DOCS = {"vis-schot-op-doel": (VIS_DOEL, 720), "vis-opta-schema": (VIS_OPTA, 660), "vis-lijnen": (VIS_LIJN, 560),
        "og-schoten": (OG_A, 630), "og-opta": (OG_B, 630)}


def render():
    UIT.mkdir(parents=True, exist_ok=True)
    tmp = []
    try:
        with sync_playwright() as p:
            b = p.chromium.launch(args=["--font-render-hinting=none"])
            for naam, (body, h) in DOCS.items():
                f = A / f".sc-{uuid.uuid4().hex[:8]}.html"; tmp.append(f)
                f.write_text(f"<!doctype html><html lang='nl'><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>", encoding="utf-8")
                pg = b.new_page(viewport={"width": 1200, "height": h}, device_scale_factor=2)
                pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
                pg.screenshot(path=str(UIT / f"{naam}.png"))
            b.close()
    finally:
        for f in tmp: f.unlink(missing_ok=True)
    print(UIT)


if __name__ == "__main__":
    render()
