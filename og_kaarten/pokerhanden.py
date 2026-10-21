# -*- coding: utf-8 -*-
"""Infographic (A4, png + pdf) en deelkaart 'Pokerhanden op volgorde' in de kaartstijl van preview-images-agent/kaart.py.
Kansen = kans dat dit je beste vijfkaartshand is uit 7 kaarten (Texas Hold'em), 133.784.560 combinaties.
  ../superodd-agent/.venv/bin/python og_kaarten/pokerhanden.py <uitmap>"""
import sys, uuid, pathlib
sys.path.insert(0, "/Users/jaspervandenboogaard/bet-experts/preview-images-agent")
import kaart
from playwright.sync_api import sync_playwright

A = pathlib.Path(kaart.ASSETS)
UIT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(__file__).parent)
G = "#2FD46E"
SYM = {"s": "♠", "h": "♥", "d": "♦", "c": "♣"}

# (naam, uitleg, kaarten [rang, kleur, telt mee], kans 7 kaarten)
HANDEN = [
    ("Royal flush", "10, boer, vrouw, heer en aas van dezelfde kleur",
     [("A", "h", 1), ("K", "h", 1), ("Q", "h", 1), ("J", "h", 1), ("10", "h", 1)], "0,003%"),
    ("Straight flush", "Vijf opeenvolgende kaarten van dezelfde kleur",
     [("9", "s", 1), ("8", "s", 1), ("7", "s", 1), ("6", "s", 1), ("5", "s", 1)], "0,03%"),
    ("Four of a kind", "Vier kaarten van dezelfde waarde (carré)",
     [("Q", "c", 1), ("Q", "d", 1), ("Q", "h", 1), ("Q", "s", 1), ("7", "d", 0)], "0,17%"),
    ("Full house", "Drie van dezelfde waarde plus een paar",
     [("8", "d", 1), ("8", "s", 1), ("8", "c", 1), ("K", "h", 1), ("K", "c", 1)], "2,6%"),
    ("Flush", "Vijf kaarten van dezelfde kleur, niet op volgorde",
     [("A", "d", 1), ("J", "d", 1), ("9", "d", 1), ("6", "d", 1), ("2", "d", 1)], "3,0%"),
    ("Straight", "Vijf opeenvolgende kaarten, verschillende kleuren",
     [("10", "c", 1), ("9", "d", 1), ("8", "s", 1), ("7", "h", 1), ("6", "c", 1)], "4,6%"),
    ("Three of a kind", "Drie kaarten van dezelfde waarde",
     [("5", "h", 1), ("5", "c", 1), ("5", "s", 1), ("K", "d", 0), ("2", "c", 0)], "4,8%"),
    ("Two pair", "Twee verschillende paren",
     [("J", "s", 1), ("J", "h", 1), ("4", "c", 1), ("4", "d", 1), ("A", "s", 0)], "23,5%"),
    ("One pair", "Twee kaarten van dezelfde waarde",
     [("10", "h", 1), ("10", "s", 1), ("K", "c", 0), ("7", "d", 0), ("3", "s", 0)], "43,8%"),
    ("High card", "Geen combinatie? Dan telt je hoogste kaart",
     [("A", "c", 1), ("Q", "d", 0), ("9", "h", 0), ("6", "s", 0), ("3", "d", 0)], "17,4%"),
]


def kaartje(r, k, telt, cls="c"):
    rood = " red" if k in "hd" else ""
    dim = "" if telt else " dim"
    return (f'<div class="{cls}{rood}{dim}"><div class="ix"><b>{r}</b><i>{SYM[k]}</i></div>'
            f'<div class="mid">{SYM[k]}</div><div class="ix bt"><b>{r}</b><i>{SYM[k]}</i></div></div>')


KAART_CSS = """
.c{width:76px;height:106px;border-radius:9px;background:linear-gradient(170deg,#FFFFFF,#E9EEF1);position:relative;
  box-shadow:0 6px 14px rgba(0,0,0,.35),inset 0 0 0 1px rgba(0,0,0,.06);color:#121821;flex:none}
.c.red{color:#E1344A}
.c.dim{opacity:.26;filter:saturate(.4)}
.c .ix{position:absolute;left:7px;top:5px;display:flex;flex-direction:column;align-items:center;line-height:1}
.c .ix b{font:800 21px/1 'Poppins';letter-spacing:-1px}
.c .ix i{font-style:normal;font-size:16px;margin-top:1px}
.c .ix.bt{left:auto;top:auto;right:7px;bottom:5px;transform:rotate(180deg)}
.c .mid{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:44px;line-height:1}
"""

BASIS = kaart.CSS + KAART_CSS + """
.eb{font:700 15px 'Plus Jakarta Sans';letter-spacing:3.5px;color:#6CC08B;text-transform:uppercase}
.k{font:700 13px 'Plus Jakarta Sans';letter-spacing:2.5px;color:#8A97A3;text-transform:uppercase}
"""

rijen = "".join(
    f'<div class="rij"><div class="cs">{"".join(kaartje(*c) for c in kaarten)}</div>'
    f'<div class="nr">{i}</div><div class="nm"><div class="hn">{naam}</div><div class="hu">{uitleg}</div></div>'
    f'<div class="kn">{kans}</div></div>'
    for i, (naam, uitleg, kaarten, kans) in enumerate(HANDEN, 1))

INFO_CSS = BASIS + f"""
.p{{width:1240px;height:1754px;position:relative;overflow:hidden;background:#0B1117}}
.diag{{position:absolute;inset:0;background:
  linear-gradient(115deg,transparent 0 58%,rgba(47,212,110,.035) 58% 72%,transparent 72%),
  linear-gradient(115deg,transparent 0 18%,rgba(255,255,255,.025) 18% 30%,transparent 30%)}}
.col{{position:absolute;inset:52px 56px 40px;display:flex;flex-direction:column}}
.tt{{font:800 150px/0.9 'Poppins';letter-spacing:-4px;color:{G};text-transform:uppercase;text-align:center}}
.sub{{font:600 25px/1.35 'Plus Jakarta Sans';color:#DDE4EA;text-align:center}}
.lijst{{position:relative;padding-left:62px;margin-top:34px}}
.as{{position:absolute;left:8px;top:0;bottom:0;width:34px;display:flex;flex-direction:column;align-items:center}}
.as .lbl{{font:800 22px 'Poppins';letter-spacing:4px;color:#F5F9FA;writing-mode:vertical-rl;transform:rotate(180deg)}}
.as .ln{{flex:1;width:3px;background:linear-gradient({G},rgba(47,212,110,.25));margin:12px 0;position:relative}}
.as .up:before{{content:'';position:absolute;left:50%;top:-2px;transform:translateX(-50%);border:9px solid transparent;border-bottom:13px solid {G};border-top:0}}
.as .dn:after{{content:'';position:absolute;left:50%;bottom:-2px;transform:translateX(-50%);border:9px solid transparent;border-top:13px solid rgba(47,212,110,.45);border-bottom:0}}
.kh{{display:grid;grid-template-columns:440px 64px 1fr 120px;align-items:end;padding-bottom:8px}}
.rij{{display:grid;grid-template-columns:440px 64px 1fr 120px;align-items:center;height:121px;border-top:1px solid rgba(255,255,255,.07)}}
.cs{{display:flex;gap:8px}}
.nr{{width:50px;height:50px;border-radius:50%;background:{G};color:#0B1117;font:800 24px 'Poppins';display:flex;align-items:center;justify-content:center}}
.hn{{font:800 40px/1 'Poppins';text-transform:uppercase;letter-spacing:-1px;white-space:nowrap}}
.hu{{font:600 17px/1.3 'Plus Jakarta Sans';color:#C9D3DB;margin-top:6px}}
.kn{{justify-self:end;font:800 22px 'Poppins';color:#F5F9FA;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);
  border-radius:999px;padding:8px 14px;white-space:nowrap}}
"""

INFO = f'''<div class="p"><div class="diag"></div>
  <div class="glow" style="width:900px;height:700px;left:-300px;top:-380px;background:rgba(22,154,71,.50)"></div>
  <div class="glow" style="width:800px;height:700px;right:-320px;bottom:-360px;background:rgba(22,154,71,.30)"></div>
  <div class="col">
    <div style="text-align:center">
      <img src="betexperts_logo.png" style="height:46px">
      <div class="tt" style="margin-top:30px">Pokerhanden</div>
      <div class="sub" style="margin-top:18px">Welke hand wint? Alle pokercombinaties op volgorde, van sterk naar zwak</div>
    </div>
    <div class="lijst">
      <div class="as"><div class="lbl">STERK</div><div class="ln up dn" style="background:linear-gradient({G},rgba(47,212,110,.30))"></div><div class="lbl">ZWAK</div></div>
      <div class="kh"><div class="k">Voorbeeld</div><div></div><div class="k">Hand</div><div class="k" style="text-align:right">Kans*</div></div>
      {rijen}
    </div>
    <div style="margin-top:auto">
      <div style="height:1px;background:rgba(255,255,255,.10)"></div>
      <div style="display:flex;justify-content:space-between;align-items:center;margin-top:16px;gap:24px">
        <div><div style="font:800 19px 'Poppins'">Gelijke hand? Dan beslist de hoogste kaart <span style="color:{G}">(de kicker)</span>. De kleur telt nooit mee.</div>
          <div style="font:600 14.5px 'Plus Jakarta Sans';color:#8A97A3;margin-top:4px">*Kans dat dit je beste hand is met 7 kaarten (Texas Hold'em) · Wat kost gokken jou? Stop op tijd. 18+</div></div>
        <div style="text-align:right;flex:none"><div style="font:800 19px 'Poppins';color:#6CC08B">bet-experts.nl</div></div>
      </div>
    </div>
  </div>
</div>'''

OG_CSS = BASIS + f"""
.tt{{font:800 66px/1.0 'Poppins';letter-spacing:-1.8px}}
.tt em{{font-style:normal;color:{G}}}
.fm{{display:inline-flex;align-items:center;gap:10px;border-radius:999px;padding:10px 18px;font:700 16px 'Plus Jakarta Sans';
  background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12)}}
.fm b{{font:800 17px 'Poppins';color:{G}}}
.fan{{position:relative;width:470px;height:330px}}
.fan .c{{position:absolute;left:180px;top:40px;width:118px;height:166px;border-radius:13px;transform-origin:50% 120%}}
.fan .c .ix b{{font-size:31px}} .fan .c .ix i{{font-size:24px}} .fan .c .mid{{font-size:70px}}
.fan .c .ix{{left:10px;top:8px}} .fan .c .ix.bt{{right:10px;bottom:8px}}
"""
fan = "".join(kaartje(r, k, 1).replace('<div class="c', f'<div style="transform:rotate({rot}deg) translateX({dx}px)" class="c', 1)
              for (r, k, rot, dx) in (("10", "h", -24, -40), ("J", "h", -12, -20), ("Q", "h", 0, 0), ("K", "h", 12, 20), ("A", "h", 24, 40)))
OG = f'''<div class="b">
  <div class="glow" style="width:760px;height:560px;left:-220px;top:-300px;background:rgba(22,154,71,.50)"></div>
  <div class="glow" style="width:600px;height:460px;right:-160px;bottom:-280px;background:rgba(22,154,71,.28)"></div>
  <img src="betexperts_logo.png" style="position:absolute;left:56px;top:44px;height:28px">
  <div style="position:absolute;right:56px;top:40px;display:flex;align-items:center;gap:10px">
    <span style="width:8px;height:8px;border-radius:50%;background:{G}"></span>
    <span style="font:700 15px 'Plus Jakarta Sans'">Poker</span>
    <span style="font:600 13px 'Plus Jakarta Sans';color:#8A97A3">· Uitleg + gratis pdf</span></div>
  <div style="position:absolute;left:56px;right:40px;top:150px;display:flex;gap:20px;align-items:center">
    <div style="flex:1;min-width:0">
      <div class="eb">Alle combinaties uitgelegd</div>
      <div class="tt" style="margin-top:14px">Pokerhanden<br><em>op volgorde</em></div>
      <div style="margin-top:26px;display:flex;gap:10px"><span class="fm"><b>10</b> handen van sterk naar zwak</span><span class="fm">Met <b>kansen</b></span></div>
    </div>
    <div class="fan">{fan}</div>
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
                f = A / f".ph-{uuid.uuid4().hex[:8]}.html"; f.write_text(doc(css, body), encoding="utf-8"); tmp.append(f)
                pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=2)
                pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
                pg.screenshot(path=str(UIT / f"{naam}.png"))
                if naam == "infographic":
                    pg.emulate_media(media="screen")
                    pg.add_style_tag(content=".c{box-shadow:none!important;border:1px solid rgba(255,255,255,.25)}"
                                             ".c.dim{filter:none!important;opacity:1!important;background:#3A424B!important;color:#5E6873!important}"
                                             ".c.dim.red{color:#7A4650!important}")
                    pg.pdf(path=str(UIT / "infographic.pdf"), width=f"{w}px", height=f"{h}px", print_background=True,
                           margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
            b.close()
    finally:
        for f in tmp: f.unlink(missing_ok=True)
    print(UIT)


if __name__ == "__main__":
    render()
