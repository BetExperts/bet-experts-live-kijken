"""Deelkaarten voor de drie artikelen over de F1 GP van São Paulo 2026 (stijl van og_kaarten/f1_austin_2026.py).
Data uit specials/f1_brazilie_2026_data.py. Bijgewerkt 10-11-2026 na de race: uitslag, terugkijken + Las Vegas,
odds vooraf tegenover uitslag. kader/kop/CSS blijven ongewijzigd (gebruikt door bookmakers_hub.py en vechtsport_6_8_nov.py). Geen officieel F1-logo: tekstkop. Accent geel-groen (Brazilië) spaarzaam.
  ../superodd-agent/.venv/bin/python og_kaarten/f1_brazilie_2026.py   -> og/nieuws/nieuws-<slug>.webp (3 stuks)"""
import io, sys, uuid, pathlib
sys.path.insert(0, "/Users/jaspervandenboogaard/bet-experts/preview-images-agent")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "specials"))
import kaart
import f1_brazilie_2026_data as D
import f1_brazilie_2026_tijden as T1, f1_brazilie_2026_kijken as T2, f1_brazilie_2026_wiewint as T3
from PIL import Image
from playwright.sync_api import sync_playwright

A = pathlib.Path(kaart.ASSETS)
OG = pathlib.Path(__file__).resolve().parent.parent / "og" / "nieuws"
GEEL, GROEN, ROOD = "#F2C230", "#2FD46E", "#FF6B6B"
LABEL = {"VT1": "Training 1", "VT2": "Training 2", "VT3": "Training 3", "KWALI": "Kwalificatie", "RACE": "Race"}

CSS = kaart.CSS + f"""
.geel{{position:absolute;border-radius:50%;filter:blur(120px)}}
.eb{{font:700 14px 'Plus Jakarta Sans';letter-spacing:3px;color:#6CC08B;text-transform:uppercase}}
.tt{{font:800 62px/1.02 'Poppins';letter-spacing:-1.6px}}
.tt em{{font-style:normal;color:{GROEN}}}
.sub{{font:600 19px/1.4 'Plus Jakarta Sans';color:#C9D3DB}}
.chk{{width:46px;height:18px;border-radius:4px;opacity:.9;background:repeating-conic-gradient(#F5F9FA 0 25%, transparent 0 50%) 0 0/9px 9px}}
.chip{{display:inline-flex;align-items:center;gap:8px;border-radius:999px;padding:10px 16px;background:rgba(255,255,255,.06);
  border:1px solid rgba(255,255,255,.12);font:700 15px/1 'Plus Jakarta Sans';white-space:nowrap}}
.wt{{display:flex;gap:14px;align-items:flex-start;border-radius:18px;padding:16px 18px;background:rgba(242,194,48,.08);border:1px solid rgba(242,194,48,.34)}}
.wt .k{{font:800 13px 'Poppins';letter-spacing:1.6px;color:{GEEL};text-transform:uppercase}}
.wt .v{{font:600 16px/1.4 'Plus Jakarta Sans';color:#DDE4EA;margin-top:3px}}
.dg{{display:flex;flex-direction:column;gap:7px}}
.dk{{font:700 12px 'Plus Jakarta Sans';letter-spacing:2.4px;color:#8A97A3;text-transform:uppercase}}
.tw{{display:flex;gap:10px}}
.tg{{flex:1;border-radius:16px;padding:11px 16px 12px;background:rgba(255,255,255,.055);border:1px solid rgba(255,255,255,.10)}}
.tk{{font:700 13px 'Plus Jakarta Sans';color:#C9D3DB;white-space:nowrap}}
.tt2{{font:800 32px/1.05 'Poppins';color:#F5F9FA;margin-top:3px;letter-spacing:-.5px}}
.tl{{font:600 12px 'Plus Jakarta Sans';color:#8A97A3;white-space:nowrap}}
.race{{display:flex;justify-content:space-between;align-items:center;border-radius:20px;padding:14px 22px 14px 20px;
  background:linear-gradient(135deg,rgba(47,212,110,.22),rgba(22,154,71,.10));border:1.5px solid rgba(47,212,110,.65);
  box-shadow:0 0 0 5px rgba(47,212,110,.07),0 16px 40px rgba(0,0,0,.35)}}
.rk{{display:flex;align-items:center;gap:8px;font:800 13px 'Poppins';letter-spacing:1.6px;color:{GROEN};text-transform:uppercase}}
.vl{{width:22px;height:12px;border-radius:2px;background:repeating-conic-gradient(#F5F9FA 0 25%, transparent 0 50%) 0 0/6px 6px}}
.rt{{font:800 52px/1 'Poppins';color:#F5F9FA;margin-top:6px;letter-spacing:-1px}}
.rt span{{font:700 18px 'Plus Jakarta Sans';color:#C9D3DB;margin-left:8px;letter-spacing:0}}
.rb{{display:inline-block;border-radius:999px;padding:5px 12px;background:{GEEL};color:#0B1117;font:800 11px 'Poppins';letter-spacing:1.3px;text-transform:uppercase}}
.op{{display:grid;grid-template-columns:1fr auto;align-items:center;gap:14px;border-radius:16px;padding:9px 18px;
  background:rgba(255,255,255,.055);border:1px solid rgba(255,255,255,.10)}}
.op .n{{font:800 18px 'Poppins';color:#F5F9FA}} .op .x{{font:600 13px 'Plus Jakarta Sans';color:#8A97A3;margin-top:2px}}
.st{{font:800 12px 'Poppins';letter-spacing:1.2px;text-transform:uppercase;border-radius:999px;padding:6px 12px;white-space:nowrap}}
.st.ja{{background:rgba(47,212,110,.16);color:{GROEN}}} .st.nee{{background:rgba(255,107,107,.14);color:{ROOD}}} .st.later{{background:rgba(242,194,48,.14);color:{GEEL}}}
.od{{display:grid;grid-template-columns:200px 1fr 70px;align-items:center;gap:14px;height:50px}}
.od .n{{font:800 19px 'Poppins';color:#F5F9FA;white-space:nowrap}} .od .t{{font:600 12px 'Plus Jakarta Sans';color:#8A97A3}}
.od .br{{height:12px;border-radius:99px;background:rgba(255,255,255,.07);overflow:hidden}}
.od .br i{{display:block;height:100%;border-radius:99px;background:linear-gradient(90deg,#169A47,{GROEN})}}
.od.top .br i{{background:linear-gradient(90deg,#B98F35,{GEEL})}}
.od b{{font:800 24px 'Poppins';color:#F5F9FA;text-align:right}} .od.top b{{color:{GEEL}}}
.pn{{border-radius:22px;padding:18px 22px;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.10)}}
.ph{{font:700 12px 'Plus Jakarta Sans';letter-spacing:2.4px;color:#8A97A3;text-transform:uppercase;display:flex;justify-content:space-between}}
"""


def kader(links, rechts, eyebrow_rechts):
    return f'''<div class="b">
  <div class="glow" style="width:760px;height:560px;left:-240px;top:-300px;background:rgba(22,154,71,.50)"></div>
  <div class="geel" style="width:560px;height:420px;left:240px;bottom:-330px;background:rgba(242,194,48,.12)"></div>
  <div class="glow" style="width:620px;height:500px;right:-200px;top:-200px;background:rgba(22,154,71,.22)"></div>
  <img src="betexperts_logo.png" style="position:absolute;left:56px;top:44px;height:28px">
  <div style="position:absolute;right:56px;top:40px;display:flex;align-items:center;gap:10px">
    <span style="width:8px;height:8px;border-radius:50%;background:{GROEN}"></span>
    <span style="font:700 15px 'Plus Jakarta Sans'">Formule 1</span>
    <span style="font:600 13px 'Plus Jakarta Sans';color:#8A97A3">· {eyebrow_rechts}</span></div>
  <div style="position:absolute;left:56px;right:56px;top:118px;display:flex;gap:44px;align-items:flex-start">
    <div style="flex:1;min-width:0">{links}</div>
    <div style="width:480px;flex:none;display:flex;flex-direction:column;gap:14px">{rechts}</div>
  </div>
  <div style="position:absolute;left:56px;right:56px;bottom:52px;height:1px;background:rgba(255,255,255,.08)"></div>
  <div style="position:absolute;left:56px;bottom:20px;font-size:13px;color:#8A97A3">Wat kost gokken jou? Stop op tijd. 18+</div>
  <div style="position:absolute;right:56px;bottom:20px;font:700 13px 'Plus Jakarta Sans';color:#6CC08B">bet-experts.nl</div>
</div>'''


def kop(eyebrow, titel, sub, chips, waarschuwing=None):
    w = (f'<div class="wt" style="margin-top:22px;max-width:520px"><div><div class="k">{waarschuwing[0]}</div>'
         f'<div class="v">{waarschuwing[1]}</div></div></div>') if waarschuwing else ""
    return (f'<div style="display:flex;align-items:center;gap:12px"><span class="chk"></span><span class="eb">{eyebrow}</span></div>'
            f'<div class="tt" style="margin-top:18px">{titel}</div><div class="sub" style="margin-top:14px">{sub}</div>'
            f'<div style="margin-top:20px;display:flex;gap:10px;flex-wrap:wrap">{"".join(f"<span class=chip>{c}</span>" for c in chips)}</div>{w}')


def per_dag():
    d = {}
    for c, naam, u, _ in D.SESSIES:
        n, s = D.tijden(u); d.setdefault(n.weekday(), []).append((c, n, s))
    return d


def kaart_tijden():
    pod = D.UITSLAG[:3]
    r = '<div class="pn"><div class="ph"><span>Uitslag race</span><span>Zondag 8 nov</span></div>' + "".join(
        f'<div class="od{" top" if p == 1 else ""}" style="grid-template-columns:44px 1fr auto"><b style="text-align:left">{p}</b>'
        f'<div><div class="n">{n}</div><div class="t">{t} · start {st}</div></div><div class="t" style="font-size:14px">{v}</div></div>'
        for p, n, t, st, v, _ in pod) + "</div>"
    r += ('<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px">'
          + "".join(f'<div class="tg"><div class="tk">{k}</div><div class="tt2" style="font-size:22px">{w}</div><div class="tl">{x}</div></div>'
                    for k, w, x in [("Pole", "Norris", "1:27,470"), ("Snelste ronde", "Antonelli", D.SNELSTE[1]),
                                    ("Constructeurs", "Mercedes", "kampioen")])
          + "</div>")
    l = kop("GP van São Paulo 2026", "F1 Brazilië:<br><em>uitslag</em>", "Interlagos · nat, droog en weer nat",
            ["<b>Norris wint</b>", "Verstappen van P21 naar P2", "Mercedes kampioen"],
            ("Volgende race", "Las Vegas: <b style='color:#F5F9FA'>zondag 22 nov, 05:00 uur</b> (NL)."))
    return kader(l, r, "Ronde 20 · São Paulo")


def kaart_kijken():
    opties = [("Viaplay", "Live en terugkijken, NL-commentaar", "ja", "Ja"), ("F1 TV Pro", "Live en terugkijken + onboard", "ja", "Ja"),
              ("Videoland", "Sport later als apart pakket", "later", "Later"), ("NOS / Ziggo Sport", "Geen Formule 1", "nee", "Nee")]
    r = "".join(f'<div class="op"><div><div class="n">{n}</div><div class="x">{x}</div></div><span class="st {k}">{t}</span></div>' for n, x, k, t in opties)
    r = f'<div style="display:flex;flex-direction:column;gap:9px">{r}</div>'
    r += ('<div class="race" style="padding:10px 22px 10px 20px"><div><div class="rk"><span class="vl"></span>Las Vegas · zondag 22 nov</div>'
          '<div class="rt" style="font-size:44px">05:00<span>uur</span></div></div><div style="text-align:right"><div class="rb">Kwali za 05:00</div></div></div>')
    l = kop("Na de GP van São Paulo", "F1 terugkijken<br>en <em>live kijken</em>", "Brazilië gemist? Zo kijk je terug, en zo zie je Las Vegas",
            ["<b>Viaplay</b>", "F1 TV Pro", "Geen gratis tv"])
    return kader(l, r, "Volgende: ronde 21 · Las Vegas")


def kaart_wiewint():
    pos = {n: p for p, n, *_r in D.UITSLAG}
    top = [r for r in D.ODDS if r[0] in ("Max Verstappen", "Kimi Antonelli", "Charles Leclerc", "Lewis Hamilton", "Lando Norris")]
    rij = lambda n, t, w: (f'<div class="od{" top" if pos.get(n) == 1 else ""}" style="grid-template-columns:1fr 70px 64px">'
                           f'<div><div class="n">{n}</div><div class="t">{t}</div></div><b style="font-size:20px;color:#C9D3DB">{D.o(w)}</b>'
                           f'<b>P{pos[n]}</b></div>')
    r = (f'<div class="pn"><div class="ph"><span>Odd vooraf → uitslag</span><span>Unibet · 5 nov</span></div>'
         + "".join(rij(n, t, w) for n, t, w, *_r in top) + "</div>")
    v = D.ODDS[0]
    r += ('<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px">'
          + "".join(f'<div class="tg"><div class="tk">{k}</div><div class="tt2" style="font-size:24px">{w}</div><div class="tl">{x}</div></div>'
                    for k, w, x in [("Winnaar", D.o(10.00), "Norris"), ("Podium VER", D.o(v[3]), "raak"), ("Hadjar P3", D.o(D.ODDS[6][3]), "podium-odd")])
          + "</div>")
    l = kop("GP van São Paulo 2026", "Wie won<br>in <em>Brazilië</em>?", "De uitslag tegenover de odds van vooraf",
            ["<b>Norris wint</b>", "Favoriet Verstappen 2e", "Antonelli 5e"])
    return kader(l, r, "Ronde 20 · Interlagos")


CHECK_JS = """(() => { const r = []; const b = document.querySelector('.b').getBoundingClientRect();
  const lijn = document.querySelector('.b > div[style*="bottom:52px"]').getBoundingClientRect().top;
  document.querySelectorAll('.b *').forEach(el => { if (['glow','geel'].some(c => el.classList.contains(c))) return;
    const q = el.getBoundingClientRect(); if (q.width && (q.right > b.right - 40 || q.bottom > b.bottom + 1)) r.push('buiten:' + el.className);
    if (q.width && q.bottom > lijn - 8 && q.top < lijn && !el.closest('[style*="bottom:52px"]')) r.push('raakt footerlijn:' + el.className);
    if (['tk','tl','n','chip'].some(c => el.classList.contains(c)) && el.scrollWidth > el.clientWidth + 1) r.push('tekst te lang:' + el.textContent); });
  return [...new Set(r)]; })()"""


if __name__ == "__main__":
    with sync_playwright() as p:
        br = p.chromium.launch(args=["--font-render-hinting=none"])
        pg = br.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=2)
        for mod, body in ((T1, kaart_tijden()), (T2, kaart_kijken()), (T3, kaart_wiewint())):
            f = A / f".f1bra-{uuid.uuid4().hex[:8]}.html"
            f.write_text(f"<!doctype html><html lang='nl'><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>", encoding="utf-8")
            try:
                pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
                fouten = pg.evaluate(CHECK_JS); png = pg.screenshot()
            finally:
                f.unlink(missing_ok=True)
            out = OG / f"nieuws-{mod.SLUG}.webp"
            Image.open(io.BytesIO(png)).convert("RGB").resize((1200, 630), Image.LANCZOS).save(out, "WEBP", quality=84, method=6)
            print(out.name, "| overloop:", fouten or "geen")
        br.close()
