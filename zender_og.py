# -*- coding: utf-8 -*-
"""Deelafbeeldingen (1200x630 .webp) voor de zenderpagina's (/zenders/<slug>), volledig gevuld uit data/zenders.json.

Ontwerp (gebruiker, 9 okt 2026): logo op een afgeronde kaart links, 'WAAR KIJK JE WAT', naam, korte onderregel,
chips met de belangrijkste competities, onderaan prijs + bet-experts.nl + KSA-regel.

  python3 zender_og.py                 # alle zenders renderen naar og/zenders/<slug>.webp
  python3 zender_og.py --upload        # + committen/pushen en het veld 'og-afbeelding' in de CMS vullen (live)
  python3 zender_og.py --only espn     # één zender
"""
import io, json, os, sys, subprocess
from PIL import Image, ImageDraw, ImageFilter
import og_image as O
from og_image import S, W, H, font, text_w, draw_text, fit_font, rrect, paste_fit, finish, POP_B, PJ_M, PJ_SB, PJ_B

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "og", "zenders")
LOGOS = os.path.join(HERE, "assets", "zenders")
X = 100                                   # linkermarge (1x)
DONKERE_KAART = {"711"}                   # logo met witte delen -> donkere kaart

LABEL = {"Tv-zender": "TV-ZENDER", "Tv-provider": "TV-PROVIDER", "Streamingdienst": "STREAMINGDIENST",
         "Tv-zender en streamingdienst": "TV & STREAMING", "Gratis tv-zender": "GRATIS TV-ZENDER",
         "Pay-per-view": "PAY-PER-VIEW", "Bookmaker met livestream": "LIVESTREAM BOOKMAKER"}


def _s(v):
    return int(round(v * S))


def comps(z):
    return [c.strip() for c in (z.get("competities-kort") or "").split("|") if c.strip()]


def prijs(z):
    v = (z.get("prijs-vanaf") or "").replace("€ ", "€").strip()
    badge = (z.get("prijs-badge") or "").strip()
    if v and v.lower() != "gratis":
        vanaf = f"{v} {z.get('prijs-eenheid') or ''}".strip()
        if "gratis" in badge.lower():                      # bv. ESPN: 'ESPN 1 gratis'
            return f"{badge} · rest vanaf {vanaf}"
        return f"Vanaf {vanaf}"
    if z.get("account-18-plus"):
        return "Gratis met account (18+)"
    b = (z.get("prijs-badge") or "Gratis").strip()
    return b[:1].upper() + b[1:]


def onderregel(z):
    c = comps(z)
    n = int(z.get("aantal-competities") or len(c))
    if not c:
        return "Zo kijk je het."
    if len(c) == 1:
        lijst = c[0]
    else:
        lijst = ", ".join(c[:3]) if n > 3 or len(c) > 3 else ", ".join(c[:-1]) + " en " + c[-1]
    return f"{lijst}{' en meer' if n > 3 else ''}: zo kijk je het."


def logo_kaart(img, slug):
    """Logo op een afgeronde kaart; licht logo -> donkere kaart, logo met eigen achtergrond -> volle kaart."""
    lg = Image.open(os.path.join(LOGOS, slug + ".webp")).convert("RGBA")
    box = (X, 150, X + 220, 370)
    # schaduw
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([_s(v) for v in (box[0], box[1] + 14, box[2], box[3] + 14)], radius=_s(40),
                                         fill=(0, 0, 0, 150))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(_s(18))))
    a = lg.getchannel("A")
    vol = a.getextrema()[0] > 200                      # ondoorzichtig vierkant (eigen achtergrond)
    k = lg.resize((64, 64)); kp = k.load()
    px = [kp[i, j] for i in range(64) for j in range(64) if kp[i, j][3] > 128]
    licht = px and sum(0.299 * r + 0.587 * g + 0.114 * b for r, g, b, _ in px) / len(px) > 200
    d = ImageDraw.Draw(img)
    if vol:
        paste_fit(img, lg, box, radius=40)
        return
    rrect(d, box, 40, fill=(27, 36, 45) if (licht or slug in DONKERE_KAART) else (255, 255, 255))
    bb = a.getbbox()
    if bb:
        lg = lg.crop(bb)
    pad = 18 if lg.width > 2.4 * lg.height else 34      # brede logo's (Eurosport, OneFootball) groter
    paste_fit(img, lg, (box[0] + pad, box[1] + pad, box[2] - pad, box[3] - pad))


def render(z):
    img = O.base_canvas()
    d = ImageDraw.Draw(img)
    # groene lijn bovenaan (verloop naar transparant)
    lijn = Image.new("RGBA", (_s(W), _s(4)), (0, 0, 0, 0))
    for x in range(lijn.width):
        a = int(255 * max(0.0, 1 - x / lijn.width) ** 0.6)
        ImageDraw.Draw(lijn).line((x, 0, x, lijn.height), fill=(34, 160, 80, a))
    img.alpha_composite(lijn, (0, 0))
    # betexperts-logo + label rechtsboven
    paste_fit(img, Image.open(os.path.join(O.ASSETS, "betexperts-logo.png")).convert("RGBA"), (X, 56, X + 186, 88))
    lab = LABEL.get(z.get("soort-dienst"), (z.get("soort-dienst") or "ZENDER").upper())
    f = font(PJ_B, 14)
    w = text_w(lab, f, 1.6) + 36
    rrect(d, (1100 - w, 53, 1100, 91), 19, outline=(52, 104, 72), width=1.5)
    draw_text(d, (1100 - w / 2, 72), lab, f, O.GREEN, "mm", spacing=1.6)
    # logo
    logo_kaart(img, z["slug"])
    d = ImageDraw.Draw(img)
    # tekstblok
    tx, maxw = 365, 1100 - 365
    d.rectangle((_s(tx), _s(184), _s(tx + 4), _s(200)), fill=O.GREEN)
    draw_text(d, (tx + 15, 192), "WAAR KIJK JE WAT", font(PJ_B, 16), O.GREEN, "lm", spacing=2.4)
    draw_text(d, (tx - 3, 258), z["name"], fit_font(z["name"], POP_B, 76, maxw, 44), O.WHITE, "lm")
    sub = onderregel(z)
    draw_text(d, (tx, 324), sub, fit_font(sub, PJ_M, 21, maxw, 15), O.LIGHT, "lm")
    # chips
    c, n = comps(z), int(z.get("aantal-competities") or 0)
    x, fc = X, font(PJ_SB, 18)
    shown = 0
    for naam in c[:4]:
        w = text_w(naam, fc) + 36
        if x + w > 1100 - 130:
            break
        rrect(d, (x, 420, x + w, 466), 23, fill=(22, 29, 36), outline=(44, 53, 62), width=1.5)
        draw_text(d, (x + w / 2, 443), naam, fc, O.WHITE, "mm")
        x += w + 10; shown += 1
    rest = max(n, len(c)) - shown
    if rest > 0:
        t = f"+{rest} meer"
        w = text_w(t, fc) + 36
        rrect(d, (x, 420, x + w, 466), 23, outline=(44, 53, 62), width=1.5)
        draw_text(d, (x + w / 2, 443), t, fc, O.GREY_D, "mm")
    # voet
    d.line((_s(X), _s(537), _s(1100), _s(537)), fill=O.LINE, width=_s(1))
    p = prijs(z)
    fp = font(PJ_B, 19)
    draw_text(d, (X, 571), p, fp, O.WHITE, "lm")
    x2 = X + text_w(p, fp) + 22
    d.ellipse((_s(x2 - 2), _s(569), _s(x2 + 2), _s(573)), fill=O.GREY_D)
    draw_text(d, (x2 + 22, 571), "bet-experts.nl", fp, O.GREEN, "lm")
    draw_text(d, (1100, 571), "18+ · Wat kost gokken jou? Stop op tijd.", font(PJ_M, 14), O.GREY, "rm")
    return finish(img)


def main():
    data = json.load(open(os.path.join(HERE, "data", "zenders.json"), encoding="utf-8"))
    only = sys.argv[sys.argv.index("--only") + 1] if "--only" in sys.argv else None
    os.makedirs(OUT, exist_ok=True)
    gemaakt = []
    for z in data:
        if only and z["slug"] != only:
            continue
        p = os.path.join(OUT, z["slug"] + ".webp")
        open(p, "wb").write(render(z)); gemaakt.append(z); print("  ✔", p)
    if "--upload" not in sys.argv:
        return
    subprocess.run(["git", "add", OUT], cwd=HERE)
    subprocess.run(["git", "commit", "-qm", "Deelafbeeldingen zenderpagina's"], cwd=HERE)
    subprocess.run(["git", "pull", "-q", "--rebase", "--autostash"], cwd=HERE)
    subprocess.run(["git", "push", "-q"], cwd=HERE)
    import time, hashlib, urllib.request
    import lk_webflow as WF
    from zenders_import import CID, bestaande
    bestaand = bestaande()
    ids = []
    for z in gemaakt:
        it = bestaand.get(z["slug"])
        if not it:
            continue
        rel = f"og/zenders/{z['slug']}.webp"
        v = hashlib.md5(open(os.path.join(HERE, rel), "rb").read()).hexdigest()[:8]
        url = f"{O_RAW()}{rel}?v={v}"
        for _ in range(10):
            try:
                if urllib.request.urlopen(url, timeout=20).status == 200:
                    break
            except Exception:
                time.sleep(4)
        WF._req("PATCH", f"{WF.WF_API}/collections/{CID}/items/{it['id']}",
                {"fieldData": {"og-afbeelding": {"url": url, "alt": f"{z['name']}: welke sport kijk je waar?"}}})
        ids.append(it["id"]); print("  ↻ CMS", z["slug"])
    if ids:
        WF._req("POST", f"{WF.WF_API}/collections/{CID}/items/publish", {"itemIds": ids})
        print(f"  {len(ids)} zenderpagina's gepubliceerd")


def O_RAW():
    from lk_og import RAW
    return RAW


if __name__ == "__main__":
    main()
