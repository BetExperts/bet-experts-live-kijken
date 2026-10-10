# -*- coding: utf-8 -*-
"""Deelafbeeldingen (1200x630 .webp) voor de clubpagina's (/clubs/<slug>) -> CMS-veld 'og-afbeelding'.

Twee varianten (ontwerp gebruiker, 10 okt 2026):
- dynamisch: vorm (laatste 5), positie, punten, doelsaldo en de volgende wedstrijd, uit de API-proxy per competitie
  (2 calls per competitie: stand + programma);
- statisch: 'Programma / Uitslagen / Beste odds / Selectie' voor clubs zonder stand (bv. toernooien).

Alleen clubs die geïndexeerd worden (robots-meta zonder 'noindex'). Een afbeelding wordt alleen opnieuw gemaakt en
geüpload als de gegevens veranderd zijn (state/club_og.json). Hosting: de gewijzigde bestanden gaan als orphan-commit
naar branch 'og-clubs' (force-push, dus geen groeiende repo); Webflow kopieert de afbeelding naar zijn eigen CDN.

  python3 club_og.py --only ado-den-haag --preview   # één afbeelding naar /tmp, niets uploaden
  python3 club_og.py                                  # gewijzigde clubs renderen + uploaden + live zetten
  python3 club_og.py --alles                          # alles opnieuw (bv. na een ontwerpwijziging)
"""
import hashlib, io, json, os, re, shutil, subprocess, sys, tempfile, time, urllib.request
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from PIL import Image, ImageDraw, ImageFilter

import og_image as O
from og_image import S, W, H, font, text_w, draw_text, fit_font, rrect, paste_fit, finish, POP_B, PJ_M, PJ_SB, PJ_B
import lk_api as A
import lk_webflow as WF

HERE = os.path.dirname(os.path.abspath(__file__))
CID = "65de2291746345c7cd323dc5"                 # Clubs-collectie
STATE = os.path.join(HERE, "state", "club_og.json")
CACHE = os.path.join(HERE, ".cache", "club_logos")
BRANCH = "og-clubs"
RAW = "https://raw.githubusercontent.com/BetExperts/bet-experts-live-kijken/" + BRANCH + "/"
VERSIE = "v1"                                    # ophogen bij een ontwerpwijziging -> alles opnieuw
NL = ZoneInfo("Europe/Amsterdam")
X = 100
NATIONAAL = {"afrika-cup-kwalificatie", "concacaf-nations-league", "nations-league", "world-cup"}
LAND = {"Netherlands": "Nederland", "England": "Engeland", "Spain": "Spanje", "Italy": "Italië", "Germany": "Duitsland",
        "France": "Frankrijk", "Portugal": "Portugal", "Belgium": "België", "Turkey": "Turkije", "Türkiye": "Turkije",
        "USA": "Verenigde Staten", "Brazil": "Brazilië", "Saudi-Arabia": "Saudi-Arabië", "Norway": "Noorwegen",
        "Sweden": "Zweden", "Denmark": "Denemarken", "Ukraine": "Oekraïne", "Czech-Republic": "Tsjechië",
        "Poland": "Polen", "Greece": "Griekenland", "Bulgaria": "Bulgarije", "Slovakia": "Slowakije",
        "Hungary": "Hongarije", "Austria": "Oostenrijk", "Scotland": "Schotland", "Finland": "Finland",
        "Iceland": "IJsland", "Switzerland": "Zwitserland"}
DAG = ["ma", "di", "wo", "do", "vr", "za", "zo"]
MND = ["jan", "feb", "mrt", "apr", "mei", "jun", "jul", "aug", "sep", "okt", "nov", "dec"]
VORM = {"W": ("W", (22, 150, 72)), "D": ("G", (52, 60, 70)), "L": ("V", (176, 96, 88))}


def _s(v):
    return int(round(v * S))


# ------------------------------------------------------------------ data
def clubs(alle=False):
    items, off = [], 0
    while True:
        r = WF._req("GET", f"{WF.WF_API}/collections/{CID}/items?limit=100&offset={off}")
        items += r.get("items", []); off += 100
        if off >= r["pagination"]["total"]:
            break
    return [i for i in items if not i.get("isDraft") and i.get("lastPublished")
            and (alle or "noindex" not in (i["fieldData"].get("robots-meta") or ""))]


_lg = {}
def competitie(slug):
    if slug not in _lg:
        st = A.standings(slug) if slug else {}
        fx = A.fixtures(slug) if slug else {}
        _lg[slug] = (st or {}, (fx or {}).get("upcoming") or [], (fx or {}).get("recent") or [])
    return _lg[slug]


def data_voor(fd, namen):
    slug = (fd.get("league-slug") or "").strip().lower()
    tid = str(fd.get("team-id") or "").strip()
    st, up, rec = competitie(slug) if tid else ({}, [], [])
    row = st.get(tid)
    nu = datetime.now(timezone.utc)
    volgende = None
    for f in sorted(up, key=lambda f: f["fixture"]["date"]):
        if tid in (str(f["teams"]["home"]["id"]), str(f["teams"]["away"]["id"])):
            ko = datetime.fromisoformat(f["fixture"]["date"])
            if ko > nu:
                h = namen.get(str(f["teams"]["home"]["id"])) or f["teams"]["home"]["name"]
                a = namen.get(str(f["teams"]["away"]["id"])) or f["teams"]["away"]["name"]
                volgende = {"titel": f"{h} – {a}", "ko": ko.astimezone(NL)}
                break
    land = None
    for f in up + rec:
        land = LAND.get((f.get("league") or {}).get("country"))
        if land:
            break
    return {"row": row, "volgende": volgende, "land": land, "nationaal": slug in NATIONAAL}


def _logo_pad(fd):
    url = (fd.get("logo") or {}).get("url")
    if not url:
        return None
    os.makedirs(CACHE, exist_ok=True)
    p = os.path.join(CACHE, hashlib.md5(url.encode()).hexdigest()[:16] + ".png")
    if not os.path.exists(p):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            Image.open(io.BytesIO(urllib.request.urlopen(req, timeout=30).read())).convert("RGBA").save(p)
        except Exception:
            return None
    return p


def _vinger(im):
    """Kleine grijswaardenafdruk op witte achtergrond, om het 'image not available'-plaatje te herkennen."""
    bg = Image.new("RGBA", im.size, (255, 255, 255, 255)); bg.alpha_composite(im.convert("RGBA"))
    return list(bg.convert("L").resize((24, 24)).tobytes())


_REF = None
def is_placeholder(im):
    global _REF
    if _REF is None:
        _REF = _vinger(Image.open(os.path.join(O.ASSETS, "logo-placeholder.png")))
    v = _vinger(im)
    return sum(abs(a - b) for a, b in zip(v, _REF)) / len(v) < 12


def logo(fd):
    p = _logo_pad(fd)
    if not p:
        return None
    im = Image.open(p).convert("RGBA")
    return None if is_placeholder(im) else im


# ------------------------------------------------------------------ tekenen
def _kop(img, d, fd, info):
    lijn = Image.new("RGBA", (_s(W), _s(4)), (0, 0, 0, 0))
    ld = ImageDraw.Draw(lijn)
    for x in range(lijn.width):
        ld.line((x, 0, x, lijn.height), fill=(34, 160, 80, int(255 * max(0.0, 1 - x / lijn.width) ** 0.6)))
    img.alpha_composite(lijn, (0, 0))
    paste_fit(img, Image.open(os.path.join(O.ASSETS, "betexperts-logo.png")).convert("RGBA"), (X, 56, X + 186, 88))
    lab = (fd.get("competitie-eigen-land") or "").upper()
    if lab:
        f = font(PJ_B, 14)
        lab = lab if text_w(lab, f, 1.6) < 420 else lab[:28] + "…"
        w = text_w(lab, f, 1.6) + 36
        rrect(d, (1100 - w, 53, 1100, 91), 19, outline=(52, 104, 72), width=1.5)
        draw_text(d, (1100 - w / 2, 72), lab, f, O.GREEN, "mm", spacing=1.6)


def _logo_kaart(img, fd, box):
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([_s(v) for v in (box[0], box[1] + 14, box[2], box[3] + 14)],
                                         radius=_s(36), fill=(0, 0, 0, 150))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(_s(18))))
    d = ImageDraw.Draw(img)
    rrect(d, box, 36, fill=(255, 255, 255))
    lg = logo(fd)
    if lg is not None:
        bb = lg.getchannel("A").getbbox()
        lg = lg.crop(bb) if bb else lg
        pad = 30                                       # ook kleine logo's vergroten (paste_fit verkleint alleen)
        bw, bh = _s(box[2] - box[0] - 2 * pad), _s(box[3] - box[1] - 2 * pad)
        f = min(bw / lg.width, bh / lg.height)
        lg = lg.resize((max(1, int(lg.width * f)), max(1, int(lg.height * f))), Image.LANCZOS)
        img.alpha_composite(lg, (_s(box[0] + pad) + (bw - lg.width) // 2, _s(box[1] + pad) + (bh - lg.height) // 2))
    else:
        woorden = [w for w in re.findall(r"[A-Za-zÀ-ÿ]+", re.sub(r"\(.*?\)", "", fd["name"]))
                   if w.upper() not in {"FC", "SC", "AFC", "CF", "AC", "SV", "VV", "FK", "SK", "KV"}]
        ini = (woorden[0][:3] if len(woorden) == 1 else "".join(w[0] for w in woorden[:3])).upper() or "?"
        kleur = _kleur(fd.get("club-kleur"))
        draw_text(d, ((box[0] + box[2]) / 2, (box[1] + box[3]) / 2), ini, font(POP_B, 52), kleur, "mm")


def _kleur(v):
    """CMS-kleur (#hex, rgb(a) of hsl(a)) -> RGB; anders het Bet-Experts-groen."""
    import colorsys
    v = (v or "").strip().lower()
    try:
        if v.startswith("#"):
            from PIL import ImageColor
            return ImageColor.getrgb(v)[:3]
        n = [float(x) for x in re.findall(r"[\d.]+", v)]
        if v.startswith("rgb") and len(n) >= 3:
            return tuple(int(x) for x in n[:3])
        if v.startswith("hsl") and len(n) >= 3:
            r, g, b = colorsys.hls_to_rgb(n[0] / 360, n[2] / 100, n[1] / 100)
            return (int(r * 255), int(g * 255), int(b * 255))
    except Exception:
        pass
    return (22, 154, 71)


def _eyebrow(info):
    if info["nationaal"]:
        return "NATIONAAL ELFTAL"
    return "CLUB · " + info["land"].upper() if info.get("land") else "CLUB"


def render_dynamisch(fd, info):
    img = O.base_canvas(); d = ImageDraw.Draw(img)
    _kop(img, d, fd, info)
    _logo_kaart(img, fd, (X, 140, X + 200, 340))
    d = ImageDraw.Draw(img)
    tx, maxw = 340, 1100 - 340
    d.rectangle((_s(tx), _s(161), _s(tx + 4), _s(177)), fill=O.GREEN)
    draw_text(d, (tx + 15, 169), _eyebrow(info), font(PJ_B, 16), O.GREEN, "lm", spacing=2.2)
    draw_text(d, (tx - 3, 232), fd["name"], fit_font(fd["name"], POP_B, 72, maxw, 40), O.WHITE, "lm")
    row = info["row"]
    vorm = [c for c in (row.get("form") or "").upper() if c in VORM][-5:]
    x = tx
    for c in vorm:
        letter, kleur = VORM[c]
        rrect(d, (x, 287, x + 34, 321), 7, fill=kleur)
        draw_text(d, (x + 17, 304), letter, font(PJ_B, 15), O.WHITE, "mm")
        x += 40
    if vorm:
        zeges = vorm.count("W")
        t = f"{zeges} {'zege' if zeges == 1 else 'zeges'} uit de laatste {len(vorm)}"
        draw_text(d, (x + 10, 304), t, font(PJ_M, 19), O.LIGHT, "lm")
    # statkaarten
    gd = row.get("goalsDiff")
    stats = [("POSITIE", f"{row.get('rank')}e"), ("PUNTEN", str(row.get("points", "–"))),
             ("DOELSALDO", (f"+{gd}" if isinstance(gd, int) and gd > 0 else str(gd)) if gd is not None else "–")]
    x0, w = X, 167
    for lab, waarde in stats:
        rrect(d, (x0, 390, x0 + w, 488), 14, fill=(17, 23, 29), outline=(37, 46, 55), width=1.2)
        draw_text(d, (x0 + 19, 414), lab, font(PJ_B, 12), O.GREY, "lm", spacing=1.6)
        draw_text(d, (x0 + 19, 452), waarde, font(POP_B, 26), O.WHITE, "lm")
        x0 += w + 14
    # volgende wedstrijd
    kx = x0
    rrect(d, (kx, 390, 1100, 488), 14, fill=(17, 23, 29), outline=(37, 46, 55), width=1.2)
    d.rounded_rectangle((_s(kx), _s(390), _s(kx + 5), _s(488)), radius=_s(3), fill=O.GREEN)
    vw = info["volgende"]
    if vw:
        draw_text(d, (kx + 22, 413), "VOLGENDE WEDSTRIJD", font(PJ_B, 12), O.GREEN, "lm", spacing=1.6)
        draw_text(d, (kx + 22, 440), vw["titel"], fit_font(vw["titel"], POP_B, 18, 1100 - kx - 44, 12), O.WHITE, "lm")
        ko = vw["ko"]
        draw_text(d, (kx + 22, 464), f"{DAG[ko.weekday()]} {ko.day} {MND[ko.month - 1]} · {ko:%H:%M}",
                  font(PJ_M, 14), O.GREY, "lm")
    else:
        al = row.get("all") or {}
        draw_text(d, (kx + 22, 413), "DIT SEIZOEN", font(PJ_B, 12), O.GREEN, "lm", spacing=1.6)
        draw_text(d, (kx + 22, 442), f"{al.get('win', 0)} gewonnen · {al.get('draw', 0)} gelijk · {al.get('lose', 0)} verloren",
                  font(POP_B, 17), O.WHITE, "lm")
    _voet(d)
    return finish(img)


def render_statisch(fd, info):
    img = O.base_canvas(); d = ImageDraw.Draw(img)
    _kop(img, d, fd, info)
    _logo_kaart(img, fd, (X, 140, X + 200, 340))
    d = ImageDraw.Draw(img)
    tx, maxw = 340, 1100 - 340
    d.rectangle((_s(tx), _s(169), _s(tx + 4), _s(185)), fill=O.GREEN)
    draw_text(d, (tx + 15, 177), _eyebrow(info), font(PJ_B, 16), O.GREEN, "lm", spacing=2.2)
    draw_text(d, (tx - 3, 240), fd["name"], fit_font(fd["name"], POP_B, 72, maxw, 40), O.WHITE, "lm")
    kort = fd["name"] if len(fd["name"]) <= 22 else fd["name"].split()[0]
    sub = f"Programma, uitslagen, odds en wedtips van {kort} op één plek."
    draw_text(d, (tx, 303), sub, fit_font(sub, PJ_M, 21, maxw, 15), O.LIGHT, "lm")
    tegels = [("Programma", "alle wedstrijden"), ("Uitslagen", "en recente vorm"),
              ("Beste odds", "per wedstrijd"), ("Selectie", "en statistieken")]
    w, x0 = (1000 - 3 * 12) / 4, X
    for t, s in tegels:
        rrect(d, (x0, 400, x0 + w, 487), 16, fill=(17, 23, 29), outline=(37, 46, 55), width=1.2)
        d.rounded_rectangle((_s(x0), _s(400), _s(x0 + 5), _s(487)), radius=_s(3), fill=O.GREEN)
        draw_text(d, (x0 + 22, 431), t, font(POP_B, 20), O.WHITE, "lm")
        draw_text(d, (x0 + 22, 461), s, font(PJ_M, 14), O.GREY, "lm")
        x0 += w + 12
    _voet(d)
    return finish(img)


def _voet(d):
    d.line((_s(X), _s(543), _s(1100), _s(543)), fill=O.LINE, width=_s(1))
    draw_text(d, (X, 576), "bet-experts.nl", font(PJ_B, 19), O.GREEN, "lm")
    draw_text(d, (1100, 576), "18+ · Wat kost gokken jou? Stop op tijd.", font(PJ_M, 14), O.GREY, "rm")


def handtekening(fd, info):
    row, vw = info["row"] or {}, info["volgende"]
    deel = [VERSIE, fd["name"], (fd.get("logo") or {}).get("url"), fd.get("competitie-eigen-land"), info.get("land"),
            row.get("rank"), row.get("points"), row.get("goalsDiff"), row.get("form"),
            (row.get("all") or {}).get("played"), vw["titel"] if vw else None, vw["ko"].isoformat() if vw else None]
    return hashlib.md5(json.dumps(deel, default=str).encode()).hexdigest()


# ------------------------------------------------------------------ upload
def push_branch(bestanden):
    """Orphan-commit met alleen de gewijzigde afbeeldingen naar branch og-clubs (force)."""
    url = subprocess.check_output(["git", "remote", "get-url", "origin"], cwd=HERE, text=True).strip()
    tok = os.environ.get("GITHUB_TOKEN")
    if tok and os.environ.get("GITHUB_REPOSITORY"):       # GitHub Actions: tijdelijke repo heeft geen credentials
        url = f"https://x-access-token:{tok}@github.com/{os.environ['GITHUB_REPOSITORY']}.git"
    tmp = tempfile.mkdtemp()
    for naam, data in bestanden.items():
        open(os.path.join(tmp, naam), "wb").write(data)
    cmd = lambda *a: subprocess.run(["git", *a], cwd=tmp, check=True, capture_output=True)
    cmd("init", "-q"); cmd("checkout", "-q", "-b", BRANCH); cmd("add", ".")
    cmd("-c", "user.name=club-og", "-c", "user.email=club-og@bet-experts.nl", "commit", "-qm", "club-og")
    cmd("push", "-q", "-f", url, f"{BRANCH}:{BRANCH}")
    shutil.rmtree(tmp, ignore_errors=True)


def main():
    a = sys.argv
    only = a[a.index("--only") + 1] if "--only" in a else None
    alle_items = clubs(alle=True)                    # namen ook van niet-geïndexeerde clubs (Nederlandse schrijfwijze)
    items = alle_items if "--alle-clubs" in a else [i for i in alle_items
                                                     if "noindex" not in (i["fieldData"].get("robots-meta") or "")]
    namen = {str(i["fieldData"].get("team-id")): i["fieldData"]["name"] for i in alle_items if i["fieldData"].get("team-id")}
    try:
        state = json.load(open(STATE, encoding="utf-8"))
    except Exception:
        state = {}
    nieuw, updates = {}, []
    for it in items:
        fd = it["fieldData"]
        if only and fd["slug"] != only:
            continue
        info = data_voor(fd, namen)
        sig = handtekening(fd, info)
        if not ("--alles" in a or only) and state.get(fd["slug"]) == sig:
            continue
        img = render_dynamisch(fd, info) if info["row"] else render_statisch(fd, info)
        if "--preview" in a:
            p = os.path.join(os.environ.get("CLUB_OG_PREVIEW", tempfile.gettempdir()), f"club_og_{fd['slug']}.webp"); open(p, "wb").write(img); print("preview:", p); continue
        nieuw[fd["slug"] + ".webp"] = img
        updates.append((it["id"], fd, sig, "dynamisch" if info["row"] else "statisch"))
    if "--preview" in a or not updates:
        print(f"club-og: {len(updates)} gewijzigd van {len(items)} clubs"); return
    push_branch(nieuw)
    time.sleep(8)
    for i in range(0, len(updates), 100):
        blok = updates[i:i + 100]
        body = {"items": [{"id": iid, "fieldData": {"og-afbeelding": {
            "url": f"{RAW}{fd['slug']}.webp?v={sig[:8]}", "alt": f"{fd['name']}: programma, vorm en wedtips"}}}
            for iid, fd, sig, _ in blok]}
        WF._req("PATCH", f"{WF.WF_API}/collections/{CID}/items/live", body)
        for _, fd, sig, _ in blok:
            state[fd["slug"]] = sig
        json.dump(state, open(STATE, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
        print(f"  {i + len(blok)}/{len(updates)} live bijgewerkt")
    soort = {}
    for *_, s in updates:
        soort[s] = soort.get(s, 0) + 1
    print(f"club-og: {len(updates)} gewijzigd van {len(items)} clubs ({soort})")


if __name__ == "__main__":
    main()
