# -*- coding: utf-8 -*-
"""Deelkaarten voor de legaal-artikelen (legale casino's, bookmaker legaal, casino zonder stortingslimiet).
  ../superodd-agent/.venv/bin/python og_kaarten/legaal.py <uitmap>"""
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
.tt{{font:800 58px/1.02 'Poppins';letter-spacing:-1.5px}}
.tt em{{font-style:normal;color:{G}}} .tt i{{font-style:normal;color:{R}}}
.fm{{display:inline-flex;align-items:center;gap:8px;border-radius:999px;padding:9px 16px;font:700 15px 'Plus Jakarta Sans';
  background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);white-space:nowrap}}
.fm b{{font:800 16px 'Poppins';color:{G}}}
.pan{{border-radius:24px;padding:20px 22px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.10)}}
.li{{display:flex;align-items:center;gap:12px;font:700 17px/1.25 'Plus Jakarta Sans';padding:9px 0;border-top:1px solid rgba(255,255,255,.07)}}
.li:first-of-type{{border-top:none}}
.ok,.no{{width:28px;height:28px;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center;font:800 16px 'Poppins'}}
.ok{{background:{G};color:#0B1117}} .no{{background:rgba(255,107,129,.16);color:{R};box-shadow:inset 0 0 0 1px rgba(255,107,129,.45)}}
.big{{font:800 120px/0.9 'Poppins';letter-spacing:-4px;color:{G}}}
.mk{{display:inline-flex;border-radius:10px;padding:8px 12px;font:700 15px 'Plus Jakarta Sans';background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.10);white-space:nowrap}}
"""


def frame(rechtsboven, links, rechts, top=150):
    return f'''<div class="b">
  <div class="glow" style="width:760px;height:560px;left:-220px;top:-300px;background:rgba(22,154,71,.50)"></div>
  <div class="glow" style="width:600px;height:460px;right:-160px;bottom:-280px;background:rgba(22,154,71,.28)"></div>
  <img src="betexperts_logo.png" style="position:absolute;left:56px;top:44px;height:28px">
  <div style="position:absolute;right:56px;top:40px;display:flex;align-items:center;gap:10px">
    <span style="width:8px;height:8px;border-radius:50%;background:{G}"></span>
    <span style="font:700 15px 'Plus Jakarta Sans'">Legaal gokken</span>
    <span style="font:600 13px 'Plus Jakarta Sans';color:#8A97A3">· {rechtsboven}</span></div>
  <div style="position:absolute;left:56px;right:56px;top:{top}px;display:flex;gap:40px;align-items:center">
    <div style="flex:1;min-width:0">{links}</div><div style="width:470px;flex:none">{rechts}</div></div>
  <div style="position:absolute;left:56px;right:56px;bottom:52px;height:1px;background:rgba(255,255,255,.08)"></div>
  <div style="position:absolute;left:56px;bottom:20px;font-size:13px;color:#8A97A3">Wat kost gokken jou? Stop op tijd. 18+</div>
  <div style="position:absolute;right:56px;bottom:20px;font:700 13px 'Plus Jakarta Sans';color:#6CC08B">bet-experts.nl</div>
</div>'''


def lijst(items):
    return "".join(f'<div class="li"><span class="{c}">{"✓" if c == "ok" else "✕"}</span>{t}</div>' for c, t in items)


MERKEN = ["Holland Casino", "TOTO", "BetCity", "JACKS.NL", "Unibet", "bet365", "BetMGM", "LeoVegas", "Circus",
          "Starcasino", "888", "711", "Bingoal", "Kansino", "Fair Play", "+ 14 meer"]

KAARTEN = {
    "casinos": frame("Stand oktober 2026",
        f'''<div class="eb">Actuele lijst Kansspelautoriteit</div>
        <div class="tt" style="margin-top:14px">Legale online<br>casino's in <em>Nederland</em></div>
        <div style="margin-top:26px;display:flex;gap:10px;flex-wrap:wrap"><span class="fm"><b>8</b> verlengd tot 2031</span><span class="fm">Check: <b>Kansspelwijzer</b></span></div>''',
        f'''<div class="pan"><div style="display:flex;align-items:flex-end;gap:16px"><div class="big">31</div>
          <div style="font:700 18px/1.25 'Plus Jakarta Sans';color:#C9D3DB;padding-bottom:8px">vergunninghouders<br>voor online gokken</div></div>
          <div style="margin-top:18px;display:flex;flex-wrap:wrap;gap:8px">{"".join(f'<span class="mk">{m}</span>' for m in MERKEN)}</div></div>''', top=128),
    "bookmaker": frame("Check in 1 minuut",
        f'''<div class="eb">Zo herken je het</div>
        <div class="tt" style="margin-top:14px">Is deze bookmaker<br><em>legaal</em>?</div>
        <div style="margin-top:26px;display:flex;gap:10px;flex-wrap:wrap"><span class="fm"><b>25</b> legale wedsites</span><span class="fm">Officiële check: <b>Kansspelwijzer</b></span></div>''',
        '<div class="pan"><div class="k" style="margin-bottom:6px">Legale bookmaker</div>' + lijst([
            ("ok", "Staat in de Kansspelwijzer van de Ksa"), ("ok", "Ksa-logo met link naar de Ksa"),
            ("ok", "Cruks-, leeftijds- en ID-check"), ("ok", "Verplichte stortingslimieten"),
            ("no", "Wedden op kaarten of corners"), ("no", "Alleen crypto, bonus zonder voorwaarden")]) + '</div>', top=150),
    "zonderlimiet": frame("Risico's en alternatieven",
        f'''<div class="eb">Altijd illegaal in Nederland</div>
        <div class="tt" style="margin-top:14px">Casino zonder<br><i>stortingslimiet</i>?</div>
        <div style="margin-top:26px;display:flex;gap:10px;flex-wrap:wrap"><span class="fm">Legaal: <b>€300</b> / <b>€700</b> netto per maand</span></div>''',
        '<div class="pan"><div class="k" style="margin-bottom:6px">Bij een casino zonder limiet</div>' + lijst([
            ("no", "Geen toezicht en geen Cruks"), ("no", "Geen garantie op uitbetaling"),
            ("no", "Verlies niet terug te vorderen"), ("no", "Strafbaar, boete tot €11.000"),
            ("ok", "Kies een casino met Ksa-vergunning")]) + '</div>', top=150),
    "corners": frame("Regels Kansspelautoriteit",
        f'''<div class="eb">Verboden in Nederland</div>
        <div class="tt" style="margin-top:14px">Wedden op<br><i>corners</i>?</div>
        <div style="margin-top:26px;display:flex;gap:10px;flex-wrap:wrap"><span class="fm">Waarom: <b>matchfixing</b></span><span class="fm">Sinds <b>2021</b></span></div>''',
        '<div class="pan"><div class="k" style="margin-bottom:6px">Bij legale bookmakers</div>' + lijst([
            ("no", "Corners, gele en rode kaarten"), ("no", "Inworpen, overtredingen, buitenspel"),
            ("no", "Wedstrijden onder 21 jaar"), ("ok", "Schoten op doel en doelpunten"),
            ("ok", "Over/under, BTTS, handicap, bet builder")]) + '</div>', top=150),
}


def render():
    UIT.mkdir(parents=True, exist_ok=True)
    tmp = []
    try:
        with sync_playwright() as p:
            b = p.chromium.launch(args=["--font-render-hinting=none"])
            for naam, body in KAARTEN.items():
                f = A / f".lg-{uuid.uuid4().hex[:8]}.html"; tmp.append(f)
                f.write_text(f"<!doctype html><html lang='nl'><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>", encoding="utf-8")
                pg = b.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=2)
                pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
                pg.screenshot(path=str(UIT / f"{naam}.png"))
            b.close()
    finally:
        for f in tmp: f.unlink(missing_ok=True)
    print(UIT)


if __name__ == "__main__":
    render()
