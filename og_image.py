# -*- coding: utf-8 -*-
"""Deelafbeeldingen (1200x630 .webp) voor live-kijken- en opstellingen-artikelen.

Gedeelde module (identiek in live-kijken-agent en opstellingen-agent). Tekent met Pillow,
dus geen browser nodig in GitHub Actions. Ontwerp: templates van de designer (sep 2026).

  render_live(info)       -> bytes (webp)
  render_opstelling(info) -> bytes (webp)

Logo's: landenteams krijgen de vlag (flagcdn.com, PNG), clubs het clublogo uit de API.
"""
import io, json, os, re, urllib.request
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets", "og")
S = 2                                  # alles op 2x tekenen, daarna verkleinen (anti-aliasing)
W, H = 1200, 630

BG = (9, 14, 19)
GREEN = (111, 207, 143)
WHITE = (245, 249, 250)
GREY = (138, 148, 158)
GREY_D = (111, 122, 133)
LIGHT = (197, 204, 211)
CARD = (17, 23, 29)
CARD_BORDER = (37, 46, 55)
LINE = (29, 37, 45)

KSA = "Wat kost gokken jou? Stop op tijd. 18+"
DAGEN = ["Ma", "Di", "Wo", "Do", "Vr", "Za", "Zo"]
MAAND = ["jan", "feb", "mrt", "apr", "mei", "jun", "jul", "aug", "sep", "okt", "nov", "dec"]

# ------------------------------------------------------------------ helpers
_fonts = {}
def font(name, size):
    key = (name, size)
    if key not in _fonts:
        _fonts[key] = ImageFont.truetype(os.path.join(ASSETS, "fonts", name + ".ttf"), int(size * S))
    return _fonts[key]

POP_B, POP_SB = "Poppins-Bold", "Poppins-SemiBold"
PJ_M, PJ_SB, PJ_B = "PlusJakartaSans-Medium", "PlusJakartaSans-SemiBold", "PlusJakartaSans-Bold"

def _s(v): return int(round(v * S))

def text_w(txt, f, spacing=0):
    return (f.getlength(txt) + spacing * S * max(len(txt) - 1, 0)) / S

def draw_text(d, xy, txt, f, fill, anchor="lm", spacing=0):
    """xy in 1x-coördinaten. spacing = letterafstand in px (1x)."""
    x, y = xy
    if not spacing:
        d.text((_s(x), _s(y)), txt, font=f, fill=fill, anchor=anchor)
        return
    total = text_w(txt, f, spacing)
    if anchor[0] == "m":
        x -= total / 2
    elif anchor[0] == "r":
        x -= total
    for ch in txt:
        d.text((_s(x), _s(y)), ch, font=f, fill=fill, anchor="l" + anchor[1])
        x += f.getlength(ch) / S + spacing

def fit_font(txt, name, size, max_w, min_size):
    while size > min_size and text_w(txt, font(name, size)) > max_w:
        size -= 1
    return font(name, size)

def rrect(d, box, r, fill=None, outline=None, width=1):
    x0, y0, x1, y1 = box
    d.rounded_rectangle((_s(x0), _s(y0), _s(x1), _s(y1)), radius=_s(r), fill=fill,
                        outline=outline, width=_s(width) if outline else 0)

def paste_fit(img, logo, box, radius=0):
    """Logo passend (contain) en gecentreerd in box plakken."""
    x0, y0, x1, y1 = [_s(v) for v in box]
    bw, bh = x1 - x0, y1 - y0
    lg = logo.copy(); lg.thumbnail((bw, bh), Image.LANCZOS)
    px, py = x0 + (bw - lg.width) // 2, y0 + (bh - lg.height) // 2
    if radius:
        m = Image.new("L", lg.size, 0)
        ImageDraw.Draw(m).rounded_rectangle((0, 0, lg.width - 1, lg.height - 1), radius=_s(radius), fill=255)
        a = lg.getchannel("A") if lg.mode == "RGBA" else Image.new("L", lg.size, 255)
        from PIL import ImageChops
        lg.putalpha(ImageChops.multiply(a, m))
    img.alpha_composite(lg.convert("RGBA"), (px, py))
    return (px / S, py / S, (px + lg.width) / S, (py + lg.height) / S)

def _get(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (bet-experts og-image)"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()

_codes = None
def land_code(api_name):
    """Engelse API-landnaam (evt. met ' U21') -> ISO-code voor de vlag, of None."""
    global _codes
    if _codes is None:
        try:
            _codes = json.load(open(os.path.join(ASSETS, "landcodes.json"), encoding="utf-8"))
        except Exception:
            _codes = {}
    base = re.sub(r"\s+U(17|19|20|21|23)$", "", api_name or "").strip()
    return _codes.get(base)

def team_logo(team_id=None, api_name=None, national=False):
    """Vlag (landenteam) of clublogo. Lokale override: assets/og/flags/<code>.png."""
    try:
        if national:
            code = land_code(api_name)
            if code:
                local = os.path.join(ASSETS, "flags", code + ".png")
                if os.path.exists(local):
                    return Image.open(local).convert("RGBA"), "flag"
                return Image.open(io.BytesIO(_get(f"https://flagcdn.com/w320/{code}.png"))).convert("RGBA"), "flag"
        if team_id:
            return Image.open(io.BytesIO(_get(f"https://media.api-sports.io/football/teams/{team_id}.png"))).convert("RGBA"), "crest"
    except Exception:
        pass
    return None, None

def datum_kort(dt):
    return f"{DAGEN[dt.weekday()]} {dt.day} {MAAND[dt.month - 1]} · {dt:%H:%M}"

def base_canvas():
    img = Image.new("RGBA", (_s(W), _s(H)), BG + (255,))
    glow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    g = ImageDraw.Draw(glow)
    g.ellipse((_s(-420), _s(-380), _s(520), _s(360)), fill=(22, 120, 60, 120))
    g.ellipse((_s(820), _s(420), _s(1500), _s(900)), fill=(22, 110, 55, 40))
    glow = glow.filter(ImageFilter.GaussianBlur(_s(150)))
    img.alpha_composite(glow)
    return img

def header(img, d, comp, ronde=None):
    logo = Image.open(os.path.join(ASSETS, "betexperts-logo.png")).convert("RGBA")
    paste_fit(img, logo, (60, 38, 60 + 176, 68))
    x = 1140
    if ronde:
        f = font(PJ_M, 16); draw_text(d, (x, 53), ronde, f, GREY_D, "rm"); x -= text_w(ronde, f) + 14
    if comp:
        draw_text(d, (x, 53), comp, font(PJ_SB, 16), (154, 163, 173), "rm")

def footer(d):
    d.line((_s(60), _s(580), _s(1140), _s(580)), fill=LINE, width=_s(1))
    draw_text(d, (60, 604), KSA, font(PJ_B, 14), (200, 207, 214), "lm")
    draw_text(d, (1140, 604), "Loketkansspel.nl", font(PJ_M, 13), GREY_D, "rm")

def finish(img):
    out = img.resize((W, H), Image.LANCZOS).convert("RGB")
    b = io.BytesIO(); out.save(b, "WEBP", quality=88, method=6)
    return b.getvalue()

def team_block(img, d, logo, kind, box, name, name_x, align, max_w, size=40, min_size=24):
    """Logo in box (vlag gevuld met afgeronde hoeken, clublogo 'contain') + naam."""
    x0, y0, x1, y1 = box
    if logo is not None:
        if kind == "flag":
            r = paste_fit(img, logo, box, radius=4)
            rrect(d, r, 4, outline=(255, 255, 255, 40), width=1)
        else:
            cy = (y0 + y1) / 2; hh = (y1 - y0) / 2 + 6
            paste_fit(img, logo, ((x0 + x1) / 2 - hh, cy - hh, (x0 + x1) / 2 + hh, cy + hh))
    cy = (y0 + y1) / 2
    f = fit_font(name, POP_B, size, max_w, min_size)
    if text_w(name, f) > max_w and " " in name:          # nog te lang: twee regels
        words = name.split(); best = None
        for i in range(1, len(words)):
            a, b = " ".join(words[:i]), " ".join(words[i:])
            wmax = max(text_w(a, f), text_w(b, f))
            if best is None or wmax < best[0]:
                best = (wmax, a, b)
        _, a, b = best
        f = fit_font(max(a, b, key=lambda t: text_w(t, f)), POP_B, min(size, 30), max_w, 18)
        lh = f.size / S * 1.08
        anc = "lm" if align == "l" else "rm"
        draw_text(d, (name_x, cy - lh / 2), a, f, WHITE, anc)
        draw_text(d, (name_x, cy + lh / 2), b, f, WHITE, anc)
        return
    draw_text(d, (name_x, cy), name, f, WHITE, "lm" if align == "l" else "rm")

# ------------------------------------------------------------------ live kijken
PROV_LOGO = {"toto": "prov-toto.png", "bet365": "prov-bet365.png", "711": "prov-711.png",
             "starcasino": "prov-starcasino.png"}

def render_live(info):
    """info: comp, ronde, home, away (namen), home_logo/away_logo ((img, kind) of None),
    dt (datetime NL-tijd), eyebrow, via_naam, via_sub, via_logo (key in PROV_LOGO) of via_tekst."""
    img = base_canvas(); d = ImageDraw.Draw(img)
    header(img, d, info.get("comp"), info.get("ronde"))
    dt = info["dt"]
    draw_text(d, (600, 230), info.get("eyebrow", "GRATIS LIVESTREAM"), font(PJ_B, 13), GREEN, "mm", spacing=3)
    draw_text(d, (600, 288), f"{dt:%H:%M}", font(POP_B, 84), GREEN, "mm")
    draw_text(d, (600, 348), "aftrap", font(PJ_M, 16), GREY, "mm")
    hl, hk = info.get("home_logo") or (None, None)
    al, ak = info.get("away_logo") or (None, None)
    team_block(img, d, hl, hk, (100, 259, 196, 319), info["home"], 216, "l", 250)
    team_block(img, d, al, ak, (1004, 259, 1100, 319), info["away"], 984, "r", 250)
    # 'Kijk via'-kaart
    naam, sub = info.get("via_naam", ""), info.get("via_sub", "")
    label = info.get("via_label", "KIJK VIA")
    tw = max(text_w(naam, font(PJ_B, 20)), text_w(sub, font(PJ_M, 13)), text_w(label, font(PJ_B, 12), 2))
    cw = max(250, 115 + tw + 26)
    rrect(d, (100, 455, 100 + cw, 547), 14, fill=CARD, outline=CARD_BORDER, width=1)
    rrect(d, (113, 473, 197, 529), 10, fill=(255, 255, 255))
    lg = info.get("via_logo")
    if lg and lg in PROV_LOGO:
        paste_fit(img, Image.open(os.path.join(ASSETS, PROV_LOGO[lg])).convert("RGBA"), (121, 481, 189, 521))
    else:
        t = info.get("via_tekst") or naam
        draw_text(d, (155, 501), t, fit_font(t, POP_B, 16, 70, 10), (20, 26, 33), "mm")
    draw_text(d, (215, 475), label, font(PJ_B, 12), GREY, "lm", spacing=2)
    draw_text(d, (215, 501), naam, font(PJ_B, 20), WHITE, "lm")
    draw_text(d, (215, 527), sub, font(PJ_M, 13), GREY, "lm")
    draw_text(d, (1100, 502), datum_kort(dt), font(PJ_M, 18), LIGHT, "rm")
    draw_text(d, (1100, 536), "bet-experts.nl", font(PJ_B, 18), GREEN, "rm")
    footer(d)
    return finish(img)

def league_logo(slug, league_id=None):
    """Competitielogo: lokale versie (assets/og/leagues/<slug>.png) of het logo uit de API."""
    local = os.path.join(ASSETS, "leagues", f"{slug}.png")
    try:
        if os.path.exists(local):
            return Image.open(local).convert("RGBA")
        if league_id:
            return Image.open(io.BytesIO(_get(f"https://media.api-sports.io/football/leagues/{league_id}.png"))).convert("RGBA")
    except Exception:
        pass
    return None

def _wrap2(txt, name, size, max_w, min_size):
    """Eén regel als het past, anders twee regels (bij voorkeur na ':'), met passende grootte."""
    if text_w(txt, font(name, size)) <= max_w:
        return [txt], font(name, size)
    if ": " in txt:
        a, b = txt.split(": ", 1); parts = [a + ":", b]
    else:
        w = txt.split(); best = None
        for i in range(1, len(w)):
            a, b = " ".join(w[:i]), " ".join(w[i:])
            m = max(text_w(a, font(name, size)), text_w(b, font(name, size)))
            if best is None or m < best[0]:
                best = (m, a, b)
        parts = [best[1], best[2]]
    f = fit_font(max(parts, key=lambda t: text_w(t, font(name, size))), name, size, max_w, min_size)
    return parts, f

def render_hub(info):
    """Deelafbeelding voor een speelronde-hub (template van Jasper, okt 2026):
    logo + periode-pil, competitielogo op witte kaart, eyebrow, titel, ondertitel en onderaan
    óf kaarten per speeldag + 'LIVE OP'-kaart (info['dagen'] + info['live_op']),
    óf zender-labels 'TE ZIEN BIJ' (info['chips'] = [(tekst, 'tv'|'stream')])."""
    img = base_canvas(); d = ImageDraw.Draw(img)
    # groene lijn bovenaan
    line = Image.new("RGBA", img.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(line)
    for x in range(0, _s(760), 2):
        a = int(255 * max(0.0, 1 - x / _s(760)) ** 1.3)
        ld.rectangle((x, 0, x + 1, _s(4)), fill=(32, 160, 80, a))
    img.alpha_composite(line)
    paste_fit(img, Image.open(os.path.join(ASSETS, "betexperts-logo.png")).convert("RGBA"), (100, 54, 100 + 186, 87))
    pill = info.get("pill")
    if pill:
        fp = font(PJ_B, 14); pw = text_w(pill, fp, 1.5) + 34
        rrect(d, (1100 - pw, 52, 1100, 88), 18, fill=(14, 22, 25), outline=(52, 84, 66), width=1)
        draw_text(d, (1100 - pw / 2, 70), pill, fp, (150, 214, 172), "mm", spacing=1.5)
    # competitielogo op witte kaart
    cy = 228
    rrect(d, (100, cy - 90, 280, cy + 90), 30, fill=(255, 255, 255))
    lg = info.get("logo")
    if lg is not None:                                   # passend maken, ook vergroten (paste_fit verkleint alleen)
        bw, bh = _s(132), _s(132) if lg.width / lg.height < 2.5 else _s(60)
        k = min(bw / lg.width, bh / lg.height)
        paste_fit(img, lg.resize((max(1, int(lg.width * k)), max(1, int(lg.height * k))), Image.LANCZOS),
                  (124, cy - 66, 256, cy + 66))
    else:
        t = info.get("comp", "")
        draw_text(d, (190, cy), t, fit_font(t, POP_B, 26, 150, 12), (20, 26, 33), "mm")
    # tekstblok, verticaal gecentreerd naast de kaart
    lines, ft = _wrap2(info["titel"], POP_B, 58, 780, 38)
    lh = ft.size / S * 1.06
    sub = info.get("sub", "")
    fs = fit_font(sub, PJ_M, 21, 780, 16)
    blok = 18 + 20 + lh * len(lines) + 16 + 24
    y = cy - blok / 2
    rrect(d, (320, y, 324, y + 18), 1, fill=GREEN)
    draw_text(d, (337, y + 9), info.get("eyebrow", "OP TV"), font(PJ_B, 15), GREEN, "lm", spacing=2.5)
    y += 18 + 20
    for ln in lines:
        draw_text(d, (318, y + lh / 2), ln, ft, WHITE, "lm"); y += lh
    draw_text(d, (320, y + 16 + 12), sub, fs, (190, 198, 206), "lm")
    # onderste rij
    if info.get("dagen"):
        kaarten = [(lab.upper(), tijden, False) for lab, tijden in info["dagen"]] + [(info.get("live_label", "LIVE OP"), [info.get("live_op", "")], True)]
        gap = 18; cw = (1000 - gap * (len(kaarten) - 1)) / len(kaarten)
        for i, (lab, waarden, accent) in enumerate(kaarten):
            x0 = 100 + i * (cw + gap)
            rrect(d, (x0, 382, x0 + cw, 494), 16, fill=(18, 25, 32), outline=(40, 50, 60), width=1)
            if accent:
                rrect(d, (x0, 382, x0 + 4, 494), 2, fill=(32, 160, 80))
            draw_text(d, (x0 + 23, 410), lab, font(PJ_B, 12), GREEN if accent else GREY_D, "lm", spacing=1.6)
            fv = font(POP_B, 30); sep = 26
            if accent:
                fv = fit_font(waarden[0], POP_B, 30, cw - 46, 18)
                draw_text(d, (x0 + 23, 451), waarden[0], fv, WHITE, "lm")
                continue
            tot = sum(text_w(t, fv) for t in waarden) + sep * (len(waarden) - 1)
            while tot > cw - 46 and fv.size / S > 18:
                fv = font(POP_B, fv.size / S - 1); sep = max(16, sep - 1)
                tot = sum(text_w(t, fv) for t in waarden) + sep * (len(waarden) - 1)
            x = x0 + 23
            for j, t in enumerate(waarden):
                if j:
                    d.ellipse((_s(x + sep / 2 - 2.5), _s(451 - 2.5), _s(x + sep / 2 + 2.5), _s(451 + 2.5)), fill=GREY_D)
                    x += sep
                draw_text(d, (x, 451), t, fv, WHITE, "lm"); x += text_w(t, fv)
    elif info.get("chips"):
        draw_text(d, (100, 388), info.get("chips_label", "TE ZIEN BIJ"), font(PJ_B, 12), GREY_D, "lm", spacing=1.6)
        x, fc = 100, font(POP_SB, 19)
        for tekst, soort in info["chips"]:
            w = 20 + 8 + 11 + text_w(tekst, fc) + 20
            if x + w > 1100:
                break
            stream = soort == "stream"
            rrect(d, (x, 407, x + w, 461), 12, fill=(19, 36, 34) if stream else (24, 31, 38),
                  outline=(46, 92, 72) if stream else (48, 57, 66), width=1)
            dot = (98, 200, 132) if stream else (138, 148, 158)
            d.ellipse((_s(x + 20), _s(434 - 4), _s(x + 28), _s(434 + 4)), fill=dot)
            draw_text(d, (x + 39, 434), tekst, fc, WHITE, "lm")
            x += w + 14
    # voet
    d.line((_s(100), _s(543), _s(1100), _s(543)), fill=LINE, width=_s(1))
    draw_text(d, (100, 576), "bet-experts.nl", font(PJ_B, 18), GREEN, "lm")
    draw_text(d, (1100, 576), "18+ · Wat kost gokken jou? Stop op tijd.", font(PJ_M, 14), GREY, "rm")
    return finish(img)

# ------------------------------------------------------------------ opstelling
FALLBACK = ("4-3-3", "4-2-3-1")
SPAN = {1: 0, 2: 96, 3: 144, 4: 172, 5: 220, 6: 240}

def parse_formation(f, fallback):
    try:
        parts = [int(x) for x in re.findall(r"\d", f or "")]
        if sum(parts) == 10 and 2 <= len(parts) <= 5 and max(parts) <= 6:
            return f, parts
    except Exception:
        pass
    return fallback, [int(x) for x in fallback.split("-")]

def _pill(d, x, cy, txt, f, align, fill, border, color, padx=12, h=32, r=8):
    w = text_w(txt, f) + 2 * padx
    x0 = x if align == "l" else x - w
    rrect(d, (x0, cy - h / 2, x0 + w, cy + h / 2), r, fill=fill, outline=border, width=1)
    draw_text(d, (x0 + w / 2, cy), txt, f, color, "mm")
    return w

def render_opstelling(info):
    """info: comp, ronde, home, away, home_logo/away_logo, dt, definitief (bool),
    home_formatie/away_formatie (str of None -> fallback)."""
    img = base_canvas(); d = ImageDraw.Draw(img)
    header(img, d, info.get("comp"), info.get("ronde"))
    hf, hparts = parse_formation(info.get("home_formatie"), FALLBACK[0])
    af, aparts = parse_formation(info.get("away_formatie"), FALLBACK[1])
    cy = 125
    # status in het midden
    stat = "Definitief" if info.get("definitief") else "Verwacht"
    fs = font(PJ_SB, 16)
    if info.get("definitief"):
        _pill(d, 600 + (text_w(stat, fs) + 36) / 2, cy, stat, fs, "r", (18, 48, 31), (47, 143, 85), (126, 224, 160), 18, 38, 19)
    else:
        _pill(d, 600 + (text_w(stat, fs) + 36) / 2, cy, stat, fs, "r", (27, 34, 41), (58, 67, 76), (228, 232, 236), 18, 38, 19)
    fp = font(PJ_SB, 16)
    pw_h, pw_a = text_w(hf, fp) + 24, text_w(af, fp) + 24
    room = 600 - 70 - 162 - 14                          # ruimte tot de statuspil
    # thuis
    hl, hk = info.get("home_logo") or (None, None)
    if hl is not None:
        r = paste_fit(img, hl, (100, 110, 148, 140) if hk == "flag" else (104, 105, 144, 145), radius=3 if hk == "flag" else 0)
        if hk == "flag":
            rrect(d, r, 3, outline=(255, 255, 255, 40), width=1)
    fh = fit_font(info["home"], POP_B, 28, room - pw_h, 16)
    draw_text(d, (162, cy), info["home"], fh, WHITE, "lm")
    _pill(d, 162 + text_w(info["home"], fh) + 14, cy, hf, fp, "l", (18, 24, 30), (46, 55, 64), LIGHT)
    # uit
    al, ak = info.get("away_logo") or (None, None)
    if al is not None:
        r = paste_fit(img, al, (1052, 110, 1100, 140) if ak == "flag" else (1056, 105, 1096, 145), radius=3 if ak == "flag" else 0)
        if ak == "flag":
            rrect(d, r, 3, outline=(255, 255, 255, 40), width=1)
    fa = fit_font(info["away"], POP_B, 28, room - pw_a, 16)
    draw_text(d, (1038, cy), info["away"], fa, WHITE, "rm")
    _pill(d, 1038 - text_w(info["away"], fa) - 14, cy, af, fp, "r", (18, 24, 30), (46, 55, 64), LIGHT)
    # veld
    rrect(d, (100, 170, 1100, 460), 18, fill=(15, 23, 30), outline=(31, 41, 50), width=1)
    lc = (37, 48, 58); lw = _s(1)
    d.rectangle((_s(117), _s(187), _s(1083), _s(443)), outline=lc, width=lw)
    d.line((_s(600), _s(187), _s(600), _s(443)), fill=lc, width=lw)
    d.ellipse((_s(555), _s(270), _s(645), _s(360)), outline=lc, width=lw)
    d.rectangle((_s(117), _s(240), _s(186), _s(389)), outline=lc, width=lw)
    d.rectangle((_s(1014), _s(240), _s(1083), _s(389)), outline=lc, width=lw)

    def dots(parts, gk_x, first_x, last_x, color):
        pts = [(gk_x, 315)]
        n = len(parts)
        for i, cnt in enumerate(parts):
            x = first_x if n == 1 else first_x + (last_x - first_x) * i / (n - 1)
            span = SPAN.get(cnt, 240)
            for j in range(cnt):
                y = 315 if cnt == 1 else 315 - span / 2 + span * j / (cnt - 1)
                pts.append((x, y))
        for x, y in pts:
            d.ellipse((_s(x - 10), _s(y - 10), _s(x + 10), _s(y + 10)), fill=(15, 23, 30), outline=color, width=_s(2))

    dots(hparts, 160, 287, 540, GREEN)
    dots(aparts, 1039, 943, 659, (213, 219, 224))
    draw_text(d, (100, 542), datum_kort(info["dt"]), font(PJ_M, 18), LIGHT, "lm")
    draw_text(d, (1100, 542), "bet-experts.nl", font(PJ_B, 18), GREEN, "rm")
    footer(d)
    return finish(img)
