# -*- coding: utf-8 -*-
"""Deelafbeelding per illegaal casino (collectie Illegale casino's), stijl: kaart.py + hero-ontwerp 'Is X legaal? Nee.'
  from og_kaarten.illegaal_casino import render_kaarten; render_kaarten([{name, bedrijf, vergunning_elders, crypto, ideal, ksa_maatregel}], uitmap)"""
import sys, uuid, pathlib, html
sys.path.insert(0, "/Users/jaspervandenboogaard/bet-experts/preview-images-agent")
import kaart
from playwright.sync_api import sync_playwright

A = pathlib.Path(kaart.ASSETS)
G, R = "#2FD46E", "#FF5A6E"
E = html.escape

CSS = kaart.CSS + f"""
.eb{{font:700 14px 'Plus Jakarta Sans';letter-spacing:3px;color:#FF8FA3;text-transform:uppercase}}
.tt{{font:800 62px/1.0 'Poppins';letter-spacing:-1.6px}} .tt em{{font-style:normal;color:{R}}}
.mono{{width:64px;height:64px;border-radius:16px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.14);
  display:flex;align-items:center;justify-content:center;font:800 24px 'Poppins';color:#F5F9FA}}
.pill{{display:inline-flex;align-items:center;gap:8px;border-radius:999px;padding:7px 14px;font:700 14px 'Plus Jakarta Sans';
  background:rgba(255,90,110,.14);color:#FF8FA3;border:1px solid rgba(255,90,110,.35)}} .pill i{{width:7px;height:7px;border-radius:50%;background:{R}}}
.card{{border-radius:22px;background:#F5F7F8;color:#0B1117;overflow:hidden;box-shadow:0 24px 60px rgba(0,0,0,.45)}}
.ch{{background:linear-gradient(135deg,#E5394F,#C92A40);padding:18px 22px;display:flex;align-items:center;gap:14px;color:#fff}}
.ch .x{{width:40px;height:40px;border-radius:12px;background:rgba(255,255,255,.18);display:flex;align-items:center;justify-content:center;font:800 20px 'Poppins'}}
.ch .k{{font:700 11px 'Plus Jakarta Sans';letter-spacing:2px;text-transform:uppercase;opacity:.85}} .ch .t{{font:800 21px 'Poppins'}}
.row{{display:flex;justify-content:space-between;align-items:center;padding:12px 22px;border-top:1px solid #E3E8EB;font:600 15px 'Plus Jakarta Sans';color:#5E6B76}}
.row b{{font:700 15px 'Plus Jakarta Sans';color:#0B1117;max-width:230px;text-align:right;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.row b.n{{color:#D92C43}} .row b.n:before{{content:'';display:inline-block;width:8px;height:8px;border-radius:50%;background:#D92C43;margin-right:7px;vertical-align:1px}}
"""


def body(c):
    naam = c["name"]
    w = [x for x in naam.replace("-", " ").split() if x.lower() not in ("casino", "bet")] or naam.split()
    mono = (w[0][:2] if len(w) == 1 else w[0][0] + w[1][0]) if w else naam[:2]
    mono = mono[0].upper() + mono[1:] if mono else "?"
    tt = 62 if len(naam) <= 12 else 54
    rows = [("Vergunning Kansspelautoriteit", "Nee", True), ("In de Kansspelwijzer", "Nee", True), ("Cruks-controle", "Nee", True),
            ("Vergunning elders", c.get("vergunning_elders") or "Onbekend", False), ("Bedrijf", c.get("bedrijf") or "Onbekend", False),
            ("Crypto", "Ja" if c.get("crypto") else "Nee", False)]
    rr = "".join(f'<div class="row">{k}<b class="{"n" if n else ""}">{E(v)}</b></div>' for k, v, n in rows)
    return f'''<div class="b">
  <div class="glow" style="width:760px;height:560px;left:-220px;top:-300px;background:rgba(229,57,79,.30)"></div>
  <div class="glow" style="width:600px;height:460px;right:-160px;bottom:-280px;background:rgba(22,154,71,.20)"></div>
  <img src="betexperts_logo.png" style="position:absolute;left:56px;top:44px;height:28px">
  <div style="position:absolute;right:56px;top:40px;display:flex;align-items:center;gap:10px">
    <span style="width:8px;height:8px;border-radius:50%;background:{R}"></span>
    <span style="font:700 15px 'Plus Jakarta Sans'">Illegale casino's</span>
    <span style="font:600 13px 'Plus Jakarta Sans';color:#8A97A3">· Gecontroleerd 2026</span></div>
  <div style="position:absolute;left:56px;right:56px;top:118px;display:flex;gap:44px;align-items:center">
    <div style="flex:1;min-width:0">
      <div style="display:flex;align-items:center;gap:16px"><div class="mono">{E(mono)}</div><span class="pill"><i></i>Illegaal in Nederland</span></div>
      <div class="tt" style="margin-top:22px;font-size:{tt}px">Is {E(naam)} legaal in Nederland? <em>Nee.</em></div>
      <div style="margin-top:18px;font:600 18px/1.4 'Plus Jakarta Sans';color:#C9D3DB;max-width:520px">Geen vergunning van de Kansspelautoriteit. Kies een casino met een Nederlandse vergunning.</div>
    </div>
    <div style="width:430px;flex:none" class="card">
      <div class="ch"><div class="x">✕</div><div><div class="k">Ons oordeel</div><div class="t">Niet spelen bij {E(naam)}</div></div></div>
      {rr}</div>
  </div>
  <div style="position:absolute;left:56px;right:56px;bottom:52px;height:1px;background:rgba(255,255,255,.08)"></div>
  <div style="position:absolute;left:56px;bottom:20px;font-size:13px;color:#8A97A3">Wat kost gokken jou? Stop op tijd. 18+</div>
  <div style="position:absolute;right:56px;bottom:20px;font:700 13px 'Plus Jakarta Sans';color:#6CC08B">bet-experts.nl</div>
</div>'''


def render_kaarten(casinos, uitmap):
    uit = pathlib.Path(uitmap); uit.mkdir(parents=True, exist_ok=True)
    tmp, paden = [], {}
    try:
        with sync_playwright() as p:
            b = p.chromium.launch(args=["--font-render-hinting=none"])
            pg = b.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=2)
            for c in casinos:
                f = A / f".ic-{uuid.uuid4().hex[:8]}.html"; tmp.append(f)
                f.write_text(f"<!doctype html><html lang='nl'><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body(c)}</body></html>", encoding="utf-8")
                pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(200)
                out = uit / f"{c['slug']}.png"; pg.screenshot(path=str(out)); paden[c["slug"]] = out
            b.close()
    finally:
        for f in tmp: f.unlink(missing_ok=True)
    return paden


if __name__ == "__main__":
    print(render_kaarten([{"name": "FgFox", "slug": "fgfox", "bedrijf": "Onbekend", "vergunning_elders": "Geen", "crypto": True}],
                         sys.argv[1] if len(sys.argv) > 1 else "."))
