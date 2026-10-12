# -*- coding: utf-8 -*-
"""CTA-afbeeldingen (1400x514 .webp) per bookmaker voor de live-kijken-artikelen.

Ontwerp (gebruiker, 12 okt 2026): 'GRATIS LIVESTREAM'-label, logo op een afgeronde kaart, 'Kijk live via X',
korte uitleg, knop, 'Zo werkt het' in drie stappen, onderaan 18+-regel en KSA-vergunning.
Twee varianten per bookmaker, zodat de afbeelding altijd klopt met de tekst van het artikel:
  stream  -> 'Kijk live via X'      (de bookmaker zendt de wedstrijd uit)
  wedden  -> 'Wed live mee bij X'   (wedstrijd alleen op tv, bv. Champions League op Ziggo Sport)

De bestanden gaan naar ../site-static/files/ (Cloudflare, telt niet mee voor Webflow-bandbreedte) en
data/cta_afbeeldingen.json koppelt (aanbieder, variant) aan de URL; lk_build.cta_html() leest die.

  python3 lk_cta.py            # alle 8 renderen + json bijwerken (daarna site-static/deploy.py draaien)
"""
import hashlib, json, os
from PIL import Image, ImageDraw, ImageFilter
import og_image as O
from og_image import S, font, text_w, draw_text, fit_font, rrect, paste_fit, POP_B, PJ_M, PJ_SB, PJ_B
from lk_config import PROVIDERS

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "site-static", "files")
DATA = os.path.join(HERE, "data", "cta_afbeeldingen.json")
BASE_URL = "https://www.bet-experts.nl/be-static/"
W, H = 1400, 514
DONKER = {"711"}                   # logo met witte delen -> donkere kaart (bet365 wit: gebruiker 12 okt)
GROEN = (22, 154, 71)


def _s(v):
    return int(round(v * S))


def teksten(slug, variant):
    p = PROVIDERS[slug]; naam = p["naam"]; dep = p.get("deposit", True)
    if variant == "wedden":
        return {"label": "LIVE MEEWEDDEN", "titel": f"Wed live mee bij {naam}",
                "sub": "Volg de live-odds en speel in op het wedstrijdverloop, in de app of op de site.",
                "stappen": ["Maak een account aan", "Open Live wedden", "Kies je wedstrijd"],
                "knop": "Account aanmaken & live wedden",
                "alt": f"Wed live mee bij {naam}: klik om een account aan te maken"}
    if dep:
        return {"label": "LIVESTREAM", "titel": f"Kijk live via {naam}",
                "sub": "Met een gestort account kijk je live mee. Je storting kun je daarna weer opnemen.",
                "stappen": ["Maak een account aan", "Stort €10 en open Live", "Kies je wedstrijd"],
                "knop": "Account aanmaken & live kijken",
                "alt": f"Kijk live via {naam}: klik om een account aan te maken en live te kijken"}
    return {"label": "GRATIS LIVESTREAM", "titel": f"Kijk live via {naam}",
            "sub": "Met een gratis account volg je de wedstrijd live in de app of op de site.",
            "stappen": ["Maak gratis een account aan", "Log in en open Live", "Kies je wedstrijd"],
            "knop": "Gratis account & live kijken",
            "alt": f"Kijk live via {naam}: klik om gratis een account aan te maken en live te kijken"}


def _wrap(txt, f, maxw):
    regels, cur = [], ""
    for w in txt.split():
        t = (cur + " " + w).strip()
        if text_w(t, f) <= maxw or not cur:
            cur = t
        else:
            regels.append(cur); cur = w
    return regels + ([cur] if cur else [])


def canvas():
    img = Image.new("RGBA", (_s(W), _s(H)), O.BG + (255,))
    glow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    g = ImageDraw.Draw(glow)
    g.ellipse((_s(-380), _s(-420), _s(560), _s(330)), fill=(22, 120, 60, 125))
    g.ellipse((_s(1050), _s(330), _s(1700), _s(800)), fill=(22, 110, 55, 50))
    img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(_s(140))))
    # dunne groene lijn bovenaan, uitlopend naar transparant
    lijn = Image.new("RGBA", (_s(W), _s(4)), (0, 0, 0, 0))
    ld = ImageDraw.Draw(lijn)
    for x in range(lijn.width):
        ld.line((x, 0, x, lijn.height), fill=(34, 160, 80, int(255 * max(0.0, 1 - x / lijn.width) ** 0.7)))
    img.alpha_composite(lijn)
    return img


def logo_kaart(img, slug, box):
    lg = Image.open(os.path.join(HERE, "assets", "zenders", slug + ".webp")).convert("RGBA")
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([_s(v) for v in (box[0], box[1] + 12, box[2], box[3] + 12)],
                                         radius=_s(38), fill=(0, 0, 0, 150))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(_s(16))))
    d = ImageDraw.Draw(img)
    donker = slug in DONKER
    rrect(d, box, 38, fill=(24, 33, 42) if donker else (255, 255, 255),
          outline=(48, 60, 70) if donker else None, width=1.5)
    bb = lg.getchannel("A").getbbox()
    if bb:
        lg = lg.crop(bb)
    pad = 26 if lg.width > 2.2 * lg.height else 40
    paste_fit(img, lg, (box[0] + pad, box[1] + pad, box[2] - pad, box[3] - pad))


def render(slug, variant):
    t = teksten(slug, variant)
    img = canvas(); d = ImageDraw.Draw(img)
    X = 70
    # label met stip
    d.ellipse((_s(X - 2), _s(56), _s(X + 26), _s(84)), fill=(22, 60, 38))
    d.ellipse((_s(X + 5), _s(63), _s(X + 19), _s(77)), fill=O.GREEN)
    draw_text(d, (X + 40, 70), t["label"], font(PJ_B, 19), O.GREEN, "lm", spacing=2.6)
    # betexperts-logo rechtsboven
    paste_fit(img, Image.open(os.path.join(O.ASSETS, "betexperts-logo.png")).convert("RGBA"), (1140, 52, 1330, 88))
    # logo-kaart
    logo_kaart(img, slug, (X, 122, X + 236, 358))
    d = ImageDraw.Draw(img)
    # titel, uitleg, knop
    tx, maxw = 350, 500
    draw_text(d, (tx - 2, 172), t["titel"], fit_font(t["titel"], POP_B, 58, maxw, 36), O.WHITE, "lm")
    fs = font(PJ_M, 21)
    for i, r in enumerate(_wrap(t["sub"], fs, maxw)[:2]):
        draw_text(d, (tx, 228 + i * 31), r, fs, O.LIGHT, "lm")
    fk = font(PJ_B, 19)
    kw = text_w(t["knop"], fk) + 92
    rrect(d, (tx, 296, tx + kw, 348), 26, fill=GROEN)
    draw_text(d, (tx + 28, 322), t["knop"], fk, (255, 255, 255), "lm")
    ax = tx + kw - 40                                  # pijltje in de knop
    d.line((_s(ax), _s(322), _s(ax + 16), _s(322)), fill=(255, 255, 255), width=_s(2.6))
    d.line((_s(ax + 9), _s(315), _s(ax + 16), _s(322), _s(ax + 9), _s(329)), fill=(255, 255, 255), width=_s(2.6), joint="curve")
    # 'Zo werkt het'
    bx = (910, 122, 1330, 358)
    rrect(d, bx, 26, fill=(15, 23, 29), outline=(40, 52, 60), width=1.5)
    d.rounded_rectangle((_s(bx[0]), _s(bx[1] + 18), _s(bx[0] + 5), _s(bx[3] - 18)), radius=_s(3), fill=GROEN)
    draw_text(d, (bx[0] + 36, 160), "ZO WERKT HET", font(PJ_B, 15), O.GREEN, "lm", spacing=2.2)
    fn, ft = font(PJ_B, 17), fit_font(max(t["stappen"], key=len), PJ_M, 20, bx[2] - bx[0] - 110, 15)
    for i, stap in enumerate(t["stappen"]):
        y = 212 + i * 52
        rrect(d, (bx[0] + 36, y - 18, bx[0] + 72, y + 18), 9, fill=(18, 42, 28), outline=(44, 110, 70), width=1.5)
        draw_text(d, (bx[0] + 54, y), str(i + 1), fn, O.GREEN, "mm")
        draw_text(d, (bx[0] + 90, y), stap, ft, O.WHITE, "lm")
    # voet
    d.line((_s(X), _s(410), _s(1330), _s(410)), fill=O.LINE, width=_s(1))
    rrect(d, (X, 438, X + 58, 474), 18, outline=(70, 82, 92), width=1.5)
    draw_text(d, (X + 29, 456), "18+", font(PJ_B, 16), (215, 222, 228), "mm")
    draw_text(d, (X + 76, 456), "Wat kost gokken jou? Stop op tijd.", font(PJ_M, 18), (175, 184, 192), "lm")
    draw_text(d, (1330, 456), "Vergund door de Kansspelautoriteit", font(PJ_M, 17), O.GREY, "rm")
    out = img.resize((W, H), Image.LANCZOS).convert("RGB")
    import io
    b = io.BytesIO(); out.save(b, "WEBP", quality=88, method=6)
    return b.getvalue(), t["alt"]


MW, MH = 720, 640                    # mobiele variant (wordt op 2x getekend en zo opgeslagen: scherp op retina)


def render_mobiel(slug, variant):
    """Staande variant voor smalle schermen: zelfde inhoud, groter lettertype na verkleinen."""
    t = teksten(slug, variant)
    img = Image.new("RGBA", (_s(MW), _s(MH)), O.BG + (255,))
    glow = Image.new("RGBA", img.size, (0, 0, 0, 0)); g = ImageDraw.Draw(glow)
    g.ellipse((_s(-300), _s(-320), _s(420), _s(260)), fill=(22, 120, 60, 130))
    g.ellipse((_s(420), _s(420), _s(1000), _s(900)), fill=(22, 110, 55, 45))
    img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(_s(110))))
    d = ImageDraw.Draw(img); X = 36
    d.ellipse((_s(X - 2), _s(30), _s(X + 22), _s(54)), fill=(22, 60, 38))
    d.ellipse((_s(X + 4), _s(36), _s(X + 16), _s(48)), fill=O.GREEN)
    draw_text(d, (X + 34, 42), t["label"], font(PJ_B, 17), O.GREEN, "lm", spacing=2.2)
    paste_fit(img, Image.open(os.path.join(O.ASSETS, "betexperts-logo.png")).convert("RGBA"), (MW - 36 - 160, 28, MW - 36, 56))
    logo_kaart(img, slug, (X, 84, X + 168, 252))
    d = ImageDraw.Draw(img)
    tx, maxw = X + 196, MW - 36 - (X + 196)
    draw_text(d, (tx - 2, 124), t["titel"], fit_font(t["titel"], POP_B, 40, maxw, 26), O.WHITE, "lm")
    fs = font(PJ_M, 21)
    for i, r in enumerate(_wrap(t["sub"], fs, maxw)[:3]):
        draw_text(d, (tx, 168 + i * 29), r, fs, O.LIGHT, "lm")
    rrect(d, (X, 280, MW - X, 340), 30, fill=GROEN)
    fk = font(PJ_B, 23)
    kw = text_w(t["knop"], fk)
    draw_text(d, (MW / 2 - 14, 310), t["knop"], fk, (255, 255, 255), "mm")
    ax = MW / 2 - 14 + kw / 2 + 16
    d.line((_s(ax), _s(310), _s(ax + 18), _s(310)), fill=(255, 255, 255), width=_s(2.8))
    d.line((_s(ax + 10), _s(302), _s(ax + 18), _s(310), _s(ax + 10), _s(318)), fill=(255, 255, 255), width=_s(2.8), joint="curve")
    bx = (X, 364, MW - X, 552)
    rrect(d, bx, 22, fill=(15, 23, 29), outline=(40, 52, 60), width=1.5)
    d.rounded_rectangle((_s(bx[0]), _s(bx[1] + 16), _s(bx[0] + 5), _s(bx[3] - 16)), radius=_s(3), fill=GROEN)
    draw_text(d, (bx[0] + 30, 394), "ZO WERKT HET", font(PJ_B, 16), O.GREEN, "lm", spacing=2.2)
    fn, ft = font(PJ_B, 18), font(PJ_M, 22)
    for i, stap in enumerate(t["stappen"]):
        y = 438 + i * 40
        rrect(d, (bx[0] + 30, y - 16, bx[0] + 62, y + 16), 8, fill=(18, 42, 28), outline=(44, 110, 70), width=1.5)
        draw_text(d, (bx[0] + 46, y), str(i + 1), fn, O.GREEN, "mm")
        draw_text(d, (bx[0] + 78, y), stap, ft, O.WHITE, "lm")
    rrect(d, (X, 578, X + 54, 612), 17, outline=(70, 82, 92), width=1.5)
    draw_text(d, (X + 27, 595), "18+", font(PJ_B, 16), (215, 222, 228), "mm")
    draw_text(d, (X + 68, 595), "Wat kost gokken jou? Stop op tijd.", font(PJ_M, 18), (175, 184, 192), "lm")
    draw_text(d, (MW - X, 595), "KSA-vergund", font(PJ_M, 17), O.GREY, "rm")
    out = img.resize((int(MW * 1.5), int(MH * 1.5)), Image.LANCZOS).convert("RGB")   # 1080x960: scherp genoeg, lichter
    import io
    b = io.BytesIO(); out.save(b, "WEBP", quality=82, method=6)
    return b.getvalue()


def main():
    os.makedirs(OUT, exist_ok=True)
    kaart = {}
    for slug in PROVIDERS:
        for variant in ("stream", "wedden"):
            data, alt = render(slug, variant)
            naam = f"cta-{slug}-{variant}-{hashlib.sha256(data).hexdigest()[:8]}.webp"
            open(os.path.join(OUT, naam), "wb").write(data)
            mdata = render_mobiel(slug, variant)
            mnaam = f"cta-{slug}-{variant}-m-{hashlib.sha256(mdata).hexdigest()[:8]}.webp"
            open(os.path.join(OUT, mnaam), "wb").write(mdata)
            kaart[f"{slug}|{variant}"] = {"url": BASE_URL + naam, "mobiel": BASE_URL + mnaam, "alt": alt,
                                          "w": W, "h": H, "mw": int(MW * 1.5), "mh": int(MH * 1.5)}
            print(f"  {naam} {len(data) // 1024} KB · {mnaam} {len(mdata) // 1024} KB")
    json.dump(kaart, open(DATA, "w"), ensure_ascii=False, indent=1)
    schrijf_js(kaart)


def schrijf_js(kaart):
    """Klein script (Cloudflare, gecachet) dat de CTA-afbeelding boven de link '👉 Klik hier: …' in een
    artikel zet. Zo komt de afbeelding niet in de Webflow-CMS (die host plaatjes zelf -> bandbreedte)."""
    linkjes = {slug: PROVIDERS[slug]["link"].split("//", 1)[1].split("/", 1)[0] for slug in PROVIDERS}
    js = """(function(){
var K=%s,D=%s;
var css=".lkcta{display:block;position:relative;margin:22px 0 10px;border-radius:18px;overflow:hidden;line-height:0;text-decoration:none!important;box-shadow:0 6px 20px rgba(0,0,0,.18);transition:transform .25s ease,box-shadow .25s ease}"+
".lkcta img{display:block;width:100%%;height:auto;border-radius:18px;transition:transform .45s ease,filter .3s ease}"+
".lkcta:after{content:'';position:absolute;inset:0;background:linear-gradient(110deg,transparent 35%%,rgba(255,255,255,.16) 50%%,transparent 65%%);transform:translateX(-130%%);pointer-events:none}"+
".lkcta:hover{transform:translateY(-3px);box-shadow:0 14px 34px rgba(22,154,71,.30),0 0 0 2px rgba(111,207,143,.65)}"+
".lkcta:hover img{transform:scale(1.012);filter:brightness(1.06)}"+
".lkcta:hover:after{transform:translateX(130%%);transition:transform .9s ease}"+
".lkcta.in:after{animation:lkctaShine 1.4s ease .6s 1}"+
"@keyframes lkctaShine{from{transform:translateX(-130%%)}to{transform:translateX(130%%)}}"+
"@media (prefers-reduced-motion:reduce){.lkcta,.lkcta img{transition:none}.lkcta:after{display:none}}";
var st=document.createElement('style');st.textContent=css;document.head.appendChild(st);
function slug(h){for(var s in D){if(h.indexOf(D[s])>-1)return s;}return null;}
var links=document.querySelectorAll('.w-richtext p > a');
for(var i=0;i<links.length;i++){var a=links[i],t=(a.textContent||'').trim();
 if(t.indexOf('\\ud83d\\udc49 Klik hier')!==0)continue;
 var s=slug(a.href||''); if(!s)continue;
 var v=/wed live mee/i.test(t)?'wedden':'stream', c=K[s+'|'+v]; if(!c)continue;
 var p=a.parentNode; if(p.previousElementSibling&&p.previousElementSibling.classList.contains('lkcta'))continue;
 var w=document.createElement('a'); w.className='lkcta'; w.href=a.href; w.target='_blank'; w.rel='sponsored noopener';
 w.setAttribute('aria-label',c.alt);
 w.innerHTML='<picture><source media="(max-width: 640px)" srcset="'+c.mobiel+'" width="'+c.mw+'" height="'+c.mh+'"><img src="'+c.url+'" alt="'+c.alt.replace(/"/g,'&quot;')+'" width="'+c.w+'" height="'+c.h+'" loading="lazy" decoding="async"></picture>';
 p.parentNode.insertBefore(w,p);
 if('IntersectionObserver' in window){(function(el){var io=new IntersectionObserver(function(e){if(e[0].isIntersecting){el.classList.add('in');io.disconnect();}},{threshold:.5});io.observe(el);})(w);}
}
})();
""" % (json.dumps(kaart, ensure_ascii=False), json.dumps(linkjes))
    naam = f"lk-cta-{hashlib.sha256(js.encode()).hexdigest()[:10]}.js"
    open(os.path.join(OUT, naam), "w", encoding="utf-8").write(js)
    print("  script:", BASE_URL + naam)


if __name__ == "__main__":
    main()
