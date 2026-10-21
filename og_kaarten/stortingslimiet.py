# -*- coding: utf-8 -*-
"""Infographic (A4, png + pdf) en deelkaart 'Netto stortingslimiet' in de kaartstijl van preview-images-agent/kaart.py.
Feiten: Beleidsregel verantwoord spelen 2024 (Stcrt. 2024, 18177), Regeling speellimieten (Stcrt. 2024, 19648),
art. 4.14 Bkoa, Ksa good/bad practices draagkrachttoetsen 2026, Rijksoverheid 12-06-2026.
  ../superodd-agent/.venv/bin/python og_kaarten/stortingslimiet.py <uitmap>"""
import sys, uuid, pathlib
sys.path.insert(0, "/Users/jaspervandenboogaard/bet-experts/preview-images-agent")
import kaart
from playwright.sync_api import sync_playwright

A = pathlib.Path(kaart.ASSETS)
UIT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(__file__).parent)
G = "#2FD46E"

BASIS = kaart.CSS + """
.eb{font:700 15px 'Plus Jakarta Sans';letter-spacing:3.5px;color:#6CC08B;text-transform:uppercase}
.k{font:700 13px 'Plus Jakarta Sans';letter-spacing:2.5px;color:#8A97A3;text-transform:uppercase}
.card{border-radius:28px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.10)}
"""

# ---------------------------------------------------------------- infographic A4 (1240 x 1754)
STAPPEN = [("Storten geblokkeerd", "De aanbieder blokkeert nieuwe stortingen voor de rest van de kalendermaand."),
           ("Draagkrachttoets", "Meer storten mag alleen als je met loonstroken of je belastingaangifte aantoont dat je het kunt dragen."),
           ("Bonusstop", "Na een blokkade krijg je minimaal 30 dagen geen bonussen meer."),
           ("Nieuwe maand", "Op de 1e van de maand begint de telling weer bij nul.")]
VERGELIJK = [("Wie bepaalt het?", "De Kansspelautoriteit (norm)", "Jij, verplicht bij inschrijving"),
             ("Wat telt mee?", "Stortingen <b>min</b> opnames", "Alle stortingen (bruto)"),
             ("Periode", "Per kalendermaand", "Per dag, week of maand"),
             ("Verhogen?", "Alleen na een draagkrachttoets", "Na 7 dagen wachttijd; vanaf €350 (tot 24 jaar €150) eerst een gesprek"),
             ("Verlagen?", "Niet van toepassing", "Gaat direct in")]

stappen = "".join(
    f'<div class="st"><div class="nr">{i}</div><div><div class="sth">{t}</div><div class="sts">{s}</div></div></div>'
    for i, (t, s) in enumerate(STAPPEN, 1))
vgl = "".join(f'<div class="vr"><div class="vk">{k}</div><div class="va">{a}</div><div class="vb">{b}</div></div>'
              for k, a, b in VERGELIJK)

INFO_CSS = BASIS + f"""
.p{{width:1240px;height:1754px;position:relative;overflow:hidden;background:#0B1117}}
.diag{{position:absolute;inset:0;background:
  linear-gradient(115deg,transparent 0 58%,rgba(47,212,110,.035) 58% 72%,transparent 72%),
  linear-gradient(115deg,transparent 0 18%,rgba(255,255,255,.025) 18% 30%,transparent 30%)}}
.col{{position:absolute;inset:52px 60px 40px;display:flex;flex-direction:column}}
.tt{{font:800 112px/0.95 'Poppins';letter-spacing:-3px;color:{G};text-transform:uppercase;text-align:center}}
.pre{{display:inline-block;font:800 28px 'Poppins';letter-spacing:10px;color:#0B1117;background:{G};border-radius:10px;padding:5px 14px 5px 24px;text-transform:uppercase}}
.sub{{font:600 24px/1.35 'Plus Jakarta Sans';color:#DDE4EA;text-align:center}}
.age{{flex:1;padding:24px 32px 22px;position:relative;overflow:hidden}}
.age .lft{{font:800 24px 'Poppins';color:#F5F9FA}}
.age .bed{{font:800 128px/1 'Poppins';letter-spacing:-4px;color:#F5F9FA;margin-top:6px}}
.age .bed small{{font-size:66px;letter-spacing:-2px;vertical-align:top;margin-right:4px;color:{G}}}
.age .pm{{font:700 20px 'Plus Jakarta Sans';color:#C9D3DB;margin-top:4px}}
.age.y{{border-color:rgba(47,212,110,.45);background:linear-gradient(160deg,rgba(47,212,110,.16),rgba(47,212,110,.04))}}
.chip{{display:inline-flex;align-items:center;gap:10px;border-radius:999px;padding:10px 18px;font:700 17px 'Plus Jakarta Sans';
  background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);color:#F5F9FA;white-space:nowrap}}
.chip i{{width:10px;height:10px;border-radius:50%;background:{G}}}
.fx{{display:flex;align-items:center;justify-content:center;gap:18px}}
.fb{{border-radius:20px;padding:14px 24px;text-align:center;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);min-width:220px}}
.fb .v{{font:800 46px/1.05 'Poppins';color:#F5F9FA}}
.fb.r{{background:{G};border-color:{G}}} .fb.r .v,.fb.r .k{{color:#0B1117}}
.op{{font:800 54px 'Poppins';color:#8A97A3}}
.sg{{display:grid;grid-template-columns:1fr 1fr;gap:14px}}
.st{{display:flex;align-items:flex-start;gap:18px;padding:18px 20px;border-radius:22px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.10)}}
.nr{{width:50px;height:50px;border-radius:50%;background:{G};color:#0B1117;font:800 26px 'Poppins';display:flex;align-items:center;justify-content:center;flex:none}}
.sth{{font:800 25px/1.05 'Poppins';text-transform:uppercase;letter-spacing:-.3px}}
.sts{{font:600 16.5px/1.35 'Plus Jakarta Sans';color:#C9D3DB;margin-top:6px}}
.vt{{border-radius:22px;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.10);padding:16px 24px 6px}}
.vh,.vr{{display:grid;grid-template-columns:190px 1fr 1fr;gap:20px;align-items:center}}
.vh{{padding-bottom:10px}}
.vh div{{font:800 18px/1.15 'Poppins';text-transform:uppercase}}
.vr{{padding:10px 0;border-top:1px solid rgba(255,255,255,.08)}}
.vk{{font:700 16px 'Plus Jakarta Sans';color:#8A97A3}}
.va,.vb{{font:700 17px/1.3 'Plus Jakarta Sans';color:#F5F9FA}}
.va b{{color:{G}}}
"""

INFO = f'''<div class="p"><div class="diag"></div>
  <div class="glow" style="width:900px;height:700px;left:-300px;top:-380px;background:rgba(22,154,71,.50)"></div>
  <div class="glow" style="width:800px;height:700px;right:-320px;bottom:-360px;background:rgba(22,154,71,.30)"></div>
  <div class="col">
    <div style="text-align:center">
      <img src="betexperts_logo.png" style="height:46px">
      <div style="margin-top:30px"><span class="pre">Netto</span></div>
      <div class="tt" style="margin-top:12px">Stortingslimiet</div>
      <div class="sub" style="margin-top:18px">Hoeveel mag je per maand netto storten bij een legaal online casino<br>of een legale bookmaker? Zo werkt de grens van de Kansspelautoriteit.</div>
    </div>

    <div style="display:flex;gap:22px;margin-top:34px">
      <div class="card age y"><div class="k">18 t/m 23 jaar</div><div class="lft" style="margin-top:4px">Jongvolwassenen</div>
        <div class="bed"><small>€</small>300</div><div class="pm">netto per kalendermaand</div></div>
      <div class="card age"><div class="k">24 jaar en ouder</div><div class="lft" style="margin-top:4px">Volwassenen</div>
        <div class="bed"><small>€</small>700</div><div class="pm">netto per kalendermaand</div></div>
    </div>
    <div style="display:flex;justify-content:center;gap:10px;margin-top:16px">
      <span class="chip"><i></i>Per aanbieder</span><span class="chip"><i></i>Per kalendermaand</span>
      <span class="chip"><i></i>Sinds 1 oktober 2024</span><span class="chip"><i></i>Inkomen bekend? Dan 30% ervan</span>
    </div>

    <div style="margin-top:30px">
      <div class="eb" style="text-align:center">Zo reken je het uit</div>
      <div class="fx" style="margin-top:14px">
        <div class="fb"><div class="k">Gestort</div><div class="v">€900</div></div><div class="op">−</div>
        <div class="fb"><div class="k">Opgenomen</div><div class="v">€400</div></div><div class="op">=</div>
        <div class="fb r"><div class="k">Netto gestort</div><div class="v">€500</div></div>
      </div>
      <div style="font:600 16px 'Plus Jakarta Sans';color:#8A97A3;text-align:center;margin-top:10px">Rekenvoorbeeld van de Kansspelautoriteit: €500 netto blijft onder de €700, dus storten mag weer.</div>
    </div>

    <div style="margin-top:30px">
      <div class="eb">Over de grens? Dit gebeurt er</div>
      <div class="sg" style="margin-top:12px">{stappen}</div>
    </div>

    <div style="margin-top:30px">
      <div class="eb">Niet verwarren met je eigen stortingslimiet</div>
      <div class="vt" style="margin-top:12px">
        <div class="vh"><div></div><div style="color:{G}">Netto stortingsgrens</div><div>Eigen stortingslimiet</div></div>
        {vgl}
      </div>
    </div>

    <div style="margin-top:auto">
      <div style="height:1px;background:rgba(255,255,255,.10)"></div>
      <div style="display:flex;justify-content:space-between;align-items:center;margin-top:16px">
        <div><div style="font:800 19px 'Poppins'">Hulp nodig? Bel gratis <span style="color:{G}">0800 24 000 22</span></div>
          <div style="font:600 14.5px 'Plus Jakarta Sans';color:#8A97A3;margin-top:4px">Open over Gokken, dag en nacht · Gokstop via cruksregister.nl · Wat kost gokken jou? Stop op tijd. 18+</div></div>
        <div style="text-align:right"><div style="font:800 19px 'Poppins';color:#6CC08B">bet-experts.nl</div>
          <div style="font:600 13px 'Plus Jakarta Sans';color:#5E6B76;margin-top:4px">Stand oktober 2026 · bron: Kansspelautoriteit</div></div>
      </div>
    </div>
  </div>
</div>'''

# ---------------------------------------------------------------- deelkaart 1200 x 630
OG_CSS = BASIS + f"""
.tt{{font:800 60px/1.0 'Poppins';letter-spacing:-1.5px}}
.tt em{{font-style:normal;color:{G}}}
.age{{flex:1;min-width:0;padding:22px 22px 20px}}
.age .bed{{font:800 74px/1 'Poppins';letter-spacing:-3px;color:#F5F9FA;margin-top:8px}}
.age .bed small{{font-size:40px;vertical-align:top;color:{G};margin-right:2px}}
.age .pm{{font:700 15px 'Plus Jakarta Sans';color:#C9D3DB;margin-top:6px}}
.age.y{{border-color:rgba(47,212,110,.45);background:linear-gradient(160deg,rgba(47,212,110,.16),rgba(47,212,110,.04))}}
.fm{{display:inline-flex;align-items:center;gap:10px;border-radius:999px;padding:10px 18px;font:700 16px 'Plus Jakarta Sans';
  background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12)}}
.fm b{{font:800 17px 'Poppins';color:{G}}}
"""
OG = f'''<div class="b">
  <div class="glow" style="width:760px;height:560px;left:-220px;top:-300px;background:rgba(22,154,71,.50)"></div>
  <div class="glow" style="width:600px;height:460px;right:-160px;bottom:-280px;background:rgba(22,154,71,.28)"></div>
  <img src="betexperts_logo.png" style="position:absolute;left:56px;top:44px;height:28px">
  <div style="position:absolute;right:56px;top:40px;display:flex;align-items:center;gap:10px">
    <span style="width:8px;height:8px;border-radius:50%;background:{G}"></span>
    <span style="font:700 15px 'Plus Jakarta Sans'">Verantwoord spelen</span>
    <span style="font:600 13px 'Plus Jakarta Sans';color:#8A97A3">· Stand oktober 2026</span></div>
  <div style="position:absolute;left:56px;right:56px;top:192px;display:flex;gap:36px;align-items:center">
    <div style="flex:1;min-width:0">
      <div class="eb">Alles wat je moet weten</div>
      <div class="tt" style="margin-top:14px">De netto<br><em>stortingslimiet</em></div>
      <div style="margin-top:28px" class="fm">Stortingen <b>−</b> opnames <b>=</b> netto, per maand</div>
      <div style="margin-top:14px;display:flex;gap:10px"><span class="fm" style="font-size:14px;padding:8px 14px">Per aanbieder</span><span class="fm" style="font-size:14px;padding:8px 14px">Sinds 1 oktober 2024</span><span class="fm" style="font-size:14px;padding:8px 14px">Daarboven: draagkrachttoets</span></div>
    </div>
    <div style="width:460px;flex:none;display:flex;gap:14px">
      <div class="card age y"><div class="k">18 t/m 23 jaar</div><div class="bed"><small>€</small>300</div><div class="pm">netto per maand</div></div>
      <div class="card age"><div class="k">24 jaar en ouder</div><div class="bed"><small>€</small>700</div><div class="pm">netto per maand</div></div>
    </div>
  </div>
  <div style="position:absolute;left:56px;right:56px;bottom:52px;height:1px;background:rgba(255,255,255,.08)"></div>
  <div style="position:absolute;left:56px;bottom:20px;font-size:13px;color:#8A97A3">Wat kost gokken jou? Stop op tijd. 18+</div>
  <div style="position:absolute;right:56px;bottom:20px;font:700 13px 'Plus Jakarta Sans';color:#6CC08B">bet-experts.nl</div>
</div>'''


def doc(css, body):
    return f"<!doctype html><html lang='nl'><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"


def render():
    UIT.mkdir(parents=True, exist_ok=True)
    tmp = []
    try:
        with sync_playwright() as p:
            b = p.chromium.launch(args=["--font-render-hinting=none"])
            for naam, css, body, w, h in (("infographic", INFO_CSS, INFO, 1240, 1754), ("og", OG_CSS, OG, 1200, 630)):
                f = A / f".nsl-{uuid.uuid4().hex[:8]}.html"; f.write_text(doc(css, body), encoding="utf-8"); tmp.append(f)
                pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=2)
                pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
                pg.screenshot(path=str(UIT / f"{naam}.png"))
                if naam == "infographic":
                    pg.emulate_media(media="screen")
                    pg.pdf(path=str(UIT / "infographic.pdf"), width=f"{w}px", height=f"{h}px", print_background=True,
                           margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
            b.close()
    finally:
        for f in tmp: f.unlink(missing_ok=True)
    print(UIT)


if __name__ == "__main__":
    render()
