# -*- coding: utf-8 -*-
"""Bouwt titel, samenvatting en de 3 rich-text delen voor een 'live gratis
kijken'-artikel. Alleen Webflow-compatibele HTML: <p> <h3> <ul> <ol> <li>
<strong> <br> <a>. GEEN tabellen."""
import random, html, re, unicodedata
from datetime import datetime, timedelta
try:
    from zoneinfo import ZoneInfo
    TZ = ZoneInfo("Europe/Amsterdam")
except Exception:
    TZ = None

from lk_config import HUB_PATH, nl_name, PROVIDERS

DAGEN = ["maandag","dinsdag","woensdag","donderdag","vrijdag","zaterdag","zondag"]
MAAND = ["januari","februari","maart","april","mei","juni","juli","augustus",
         "september","oktober","november","december"]

def _local(dt_iso):
    dt = datetime.fromisoformat(dt_iso.replace("Z","+00:00"))
    if TZ: dt = dt.astimezone(TZ)
    return dt

def nl_datum(dt): return f"{DAGEN[dt.weekday()]} {dt.day} {MAAND[dt.month-1]} {dt.year}"
def nl_datum_kort(dt): return f"{dt.day} {MAAND[dt.month-1]}"
def nl_tijd(dt):  return f"{dt.hour:02d}:{dt.minute:02d}"

# ---------- nachtwedstrijden (aftrap 00:00-05:00, bv. CONCACAF) ----------
def is_nacht(dt): return dt.hour < 5

def nl_nacht(dt, jaar=True, dag=True):
    """'vrijdag 2 op zaterdag 3 oktober 2026' (ook over maand-/jaargrens heen)."""
    v = dt - timedelta(days=1)
    dv = f"{DAGEN[v.weekday()]} " if dag else ""
    dn = f"{DAGEN[dt.weekday()]} " if dag else ""
    y = f" {dt.year}" if jaar else ""
    if v.month == dt.month:
        return f"{dv}{v.day} op {dn}{dt.day} {MAAND[dt.month-1]}{y}"
    if v.year == dt.year:
        return f"{dv}{v.day} {MAAND[v.month-1]} op {dn}{dt.day} {MAAND[dt.month-1]}{y}"
    return f"{dv}{v.day} {MAAND[v.month-1]} {v.year} op {dn}{dt.day} {MAAND[dt.month-1]}{y}"

def nl_wanneer(dt, jaar=True, dag=True):
    """'op zondag 4 oktober 2026 om 20:00 uur' of, bij een aftrap tussen 00:00 en 05:00,
    'in de nacht van vrijdag 2 op zaterdag 3 oktober 2026 om 00:00 uur'."""
    if is_nacht(dt):
        return f"in de nacht van {nl_nacht(dt, jaar, dag)} om {nl_tijd(dt)} uur"
    d = f"{DAGEN[dt.weekday()]} " if dag else ""
    return f"op {d}{dt.day} {MAAND[dt.month-1]}{f' {dt.year}' if jaar else ''} om {nl_tijd(dt)} uur"

def nl_datum_info(dt):
    """Datumregel in het infoblok: 'zondag 4 oktober 2026' of 'nacht van vrijdag 2 op zaterdag 3 oktober 2026'."""
    return f"nacht van {nl_nacht(dt)}" if is_nacht(dt) else nl_datum(dt)

def esc(s): return html.escape(str(s or ""), quote=False)

_BIJV = None
def bijv_elftal(naam):
    """'Marokko' -> 'het Marokkaans voetbalelftal' (zoekvorm in Google), anders None (clubs)."""
    global _BIJV
    if _BIJV is None:
        import json, os
        try:
            _BIJV = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "landen_bijv.json"), encoding="utf-8"))
        except Exception:
            _BIJV = {}
    a = _BIJV.get(naam)
    return f"het {a} voetbalelftal" if a else None

def zoek_zin(homeN, awayN):
    """Korte zin in de woorden waarmee mensen zoeken ('waar kun je … kijken')."""
    bh, ba = bijv_elftal(homeN), bijv_elftal(awayN)
    if bh and ba:
        return (f"Zoek je waar je {esc(bh)} tegen {esc(ba)} kunt kijken? Hieronder lees je op welke zender "
                f"{esc(homeN)} – {esc(awayN)} live te zien is, hoe laat de aftrap is en hoe je de livestream vindt.")
    return (f"Zoek je waar je {esc(homeN)} – {esc(awayN)} kunt kijken? Hieronder lees je op welke zender het duel "
            f"live te zien is, hoe laat de aftrap is en hoe je de livestream vindt.")

_TR = {"ı":"i","İ":"I","ş":"s","Ş":"S","ğ":"g","Ğ":"G","ç":"c","Ç":"C","ö":"o","Ö":"O","ü":"u","Ü":"U"}
def slugify(s):
    s = "".join(_TR.get(c, c) for c in (s or ""))
    s = unicodedata.normalize("NFKD", s).encode("ascii","ignore").decode()
    return re.sub(r"-+","-", re.sub(r"[^a-z0-9]+","-", s.lower())).strip("-")

def build_slug(home_slug, away_slug, dt, gratis=True):
    soort = "live-gratis-kijken" if gratis else "live-kijken"
    return f"{home_slug}-{away_slug}-{soort}-{dt.day:02d}-{dt.month:02d}-{dt.year}"

# ---------- titel (gevarieerd, deterministisch per fixture) ----------
TITEL_MAX = 70

def _kies(varianten):
    """Willekeurige variant die binnen TITEL_MAX past (lange teamnamen), anders de kortste."""
    past = [v for v in varianten if len(v) <= TITEL_MAX]
    return random.choice(past) if past else min(varianten, key=len)

def build_title(homeN, awayN, dt, paid_tv=None, free_tv=None):
    """Korte titel met 'gratis' precies één keer, steeds net iets anders (deterministisch per
    wedstrijd). Geen 'op tv' als het duel alleen via een stream te zien is."""
    M = f"{homeN} – {awayN}"
    datum = nl_datum_kort(dt)
    if paid_tv:   # alleen via betaalde tv: 'gratis' als vraag (gebruiker wil 'gratis' in elke titel),
                  # het artikel beantwoordt eerlijk dat het op {paid_tv} te zien is
        return _kies([
            f"Op welke zender is {M}? Gratis kijken en hoe laat",
            f"{M}: welke zender, hoe laat en gratis kijken?",
            f"Welke zender zendt {M} uit? Gratis kijken en aftrap",
            f"{M} gratis kijken? Zender en hoe laat ({datum})",
            f"{M} live op {paid_tv}: hoe laat en gratis kijken?",
        ])
    if free_tv:   # vrij te ontvangen tv (NPO)
        return _kies([
            f"{M} gratis op {free_tv}: welke zender en hoe laat?",
            f"Op welke zender is {M}? Gratis op {free_tv}",
            f"{M} gratis op tv: welke zender en hoe laat?",
            f"Welke zender zendt {M} uit? Gratis en hoe laat",
            f"{M} gratis kijken ({datum}): zender en hoe laat",
        ])
    return _kies([   # gratis meekijken via een bookmaker-stream
        f"Op welke zender is {M}? Gratis live kijken en hoe laat",
        f"{M} gratis live kijken: welke zender en hoe laat?",
        f"Welke zender zendt {M} uit? Gratis livestream en aftrap",
        f"{M} gratis kijken: zender, livestream en hoe laat",
        f"{M} live gratis kijken ({datum}): zender en hoe laat",
    ])

META_MAX = 155   # meta-description / samenvatting: max. ~155 tekens

def _kort(varianten, n=META_MAX):
    """Eerste variant die binnen n tekens past; anders de laatste, afgekapt op een woordgrens."""
    for v in varianten:
        if len(v) <= n:
            return v
    v = varianten[-1]
    return v[:n].rsplit(" ", 1)[0].rstrip(",;:") + "."

def build_samenvatting(homeN, awayN, comp, dt, prov_naam, free_tv=None, paid_tv=None,
                       stream_tv=None, deposit=True):
    """Meta-omschrijving (max. ~155 tekens). stream_tv = betaalde zender naast een bookmaker-stream;
    zonder zender noemen we 'op tv' niet (het artikel zegt dan dat het duel niet op tv is)."""
    M = f"{homeN} – {awayN}"
    w_lang, w_kort = nl_wanneer(dt), nl_wanneer(dt, jaar=False, dag=False)
    if paid_tv:   # alleen via betaalde tv: antwoord eerst (zender + tijd), dan de zoekwoorden
        return _kort([f"{M} kijk je {w} live op {paid_tv}. Welke zender, hoe laat en of je gratis kunt meekijken: "
                      f"alles op een rij." for w in (w_lang, w_kort)]
                     + [f"{M} kijk je {w_kort} live op {paid_tv}. Zender, aftraptijd en online meekijken.",
                        f"{M} kijk je {w_kort} live op {paid_tv}."])
    if free_tv:   # gratis tv (bv. NPO)
        return _kort([f"{M} kijk je {w} gratis op {free_tv}. Welke zender, hoe laat en waar de livestream staat: "
                      f"alles op een rij." for w in (w_lang, w_kort)]
                     + [f"{M} kijk je {w_kort} gratis op {free_tv}. Zender, aftraptijd en livestream.",
                        f"{M} kijk je {w_kort} gratis op {free_tv}."])
    acc = (f"met een gestort {prov_naam}-account kijk je gratis mee" if deposit
           else f"met een gratis {prov_naam}-account kijk je mee")
    if stream_tv:
        return _kort([f"{M} is {w} live te zien op {stream_tv}, maar ook zonder abonnement: {acc}. Zender, aftrap en livestream."
                      for w in (w_lang, w_kort)]
                     + [f"{M} is {w_kort} live op {stream_tv}; zonder abonnement {acc}.",
                        f"{M} live kijken zonder {stream_tv}-abonnement: {acc}."])
    return _kort([f"{M} is {w} niet op de Nederlandse tv, maar {acc}. Zender, aftraptijd en livestream." for w in (w_lang, w_kort)]
                 + [f"{M} is {w_kort} niet op tv, maar {acc}.",
                    f"{M} live kijken: niet op tv, maar {acc}."])

# ---------- vorm ----------
def form_dashes(f):
    m = {"W":"W","D":"G","L":"V"}
    return "–".join(m.get(c, c) for c in (f or "")[:5]) or "n.n.b."

def form_zin(f):
    w=(f or "").count("W"); l=(f or "").count("L")
    if w>=3: return "De vorm zit er de laatste weken goed in."
    if l>=3: return "De resultaten vielen de laatste weken tegen."
    return "De vorm is wisselvallig met winst en verlies door elkaar."

# ---------- 'over de club' op basis van de competitiestand ----------
def _ordinal(n):
    return f"{n}e"

def _join_nl(parts):
    if not parts: return ""
    if len(parts) == 1: return parts[0]
    return ", ".join(parts[:-1]) + " en " + parts[-1]

def _mv(n, enk, mv):
    """'1 punt' / '3 punten', '1 wedstrijd' / '2 wedstrijden'."""
    return f"{n} {enk if n == 1 else mv}"

# Landen die in een lopende zin een lidwoord krijgen ('bij de Verenigde Staten').
_MET_DE = {"Verenigde Staten", "Dominicaanse Republiek", "Kaaimaneilanden", "Faeröer", "Bahama's",
           "Verenigde Arabische Emiraten", "Centraal-Afrikaanse Republiek", "Filipijnen", "Malediven",
           "Comoren", "Seychellen", "Salomonseilanden", "Cookeilanden", "Britse Maagdeneilanden",
           "Amerikaanse Maagdeneilanden", "Turks- en Caicoseilanden", "Faeröereilanden"}

def met_lidwoord(naam):
    """Zet 'de' voor landnamen die dat in een lopende zin nodig hebben (namen via nl_name)."""
    n = str(naam or "")
    if n in _MET_DE or n.endswith("eilanden") or n.startswith("Verenigde "):
        return "de " + n
    return n

def _result_phrase(r):
    """Menselijke uitslag-omschrijving vanuit het team gezien."""
    opp = esc(met_lidwoord(r["opp"])); s = f'{r["my"]}-{r["og"]}'
    if r["outcome"] == "W":
        return f'een {s}-zege {"tegen" if r["home"] else "bij"} {opp}'
    if r["outcome"] == "L":
        return f'een {s}-nederlaag {"tegen" if r["home"] else "bij"} {opp}'
    return f'een {s}-gelijkspel {"tegen" if r["home"] else "bij"} {opp}'

_TELWOORD = {1: "het laatste duel", 2: "de laatste twee duels", 3: "de laatste drie duels",
             4: "de laatste vier duels", 5: "de laatste vijf duels"}

def _form_verhaal(team, form, results, compN):
    """Kort menselijk stukje over de vorm, met echte uitslagen."""
    results = results or []
    last5 = results[-5:]
    pts = sum(3 if r["outcome"] == "W" else (1 if r["outcome"] == "D" else 0) for r in last5)
    w = sum(1 for r in last5 if r["outcome"] == "W")
    l = sum(1 for r in last5 if r["outcome"] == "L")
    recent = list(reversed(last5))  # recentste eerst
    if not recent:
        return f"Recente resultaten van <strong>{esc(team)}</strong> zijn nog niet beschikbaar."
    # openingszin over de reeks
    if w >= 3:
        kop = f"<strong>{esc(team)}</strong> is uitstekend op dreef"
    elif l >= 3:
        kop = f"<strong>{esc(team)}</strong> is de laatste weken zoekende"
    elif w == 0:
        kop = f"<strong>{esc(team)}</strong> wacht nog op een overwinning"
    else:
        kop = f"<strong>{esc(team)}</strong> kent een wisselvallige reeks"
    laatste = recent[0]; opp = esc(met_lidwoord(laatste["opp"])); s = f'{laatste["my"]}-{laatste["og"]}'
    if laatste["outcome"] == "W":
        slot = f'won de ploeg met {s} {"van" if laatste["home"] else "bij"} {opp}'
    elif laatste["outcome"] == "L":
        slot = f'verloor de ploeg met {s} {"van" if laatste["home"] else "bij"} {opp}'
    else:
        slot = f'speelde de ploeg met {s} gelijk {"tegen" if laatste["home"] else "bij"} {opp}'
    phrases = [_result_phrase(r) for r in recent[1:4]]   # de duels dáárvoor
    verhaal = (f"{kop}: uit {_TELWOORD[len(last5)]} pakte de ploeg {_mv(pts, 'punt', 'punten')}. "
               f"In de meest recente wedstrijd {slot}")
    verhaal += (f"; daarvoor stonden onder meer {_join_nl(phrases)} op de teller." if phrases else ".")
    return verhaal

# 'League A - Group A' (huidige API) en 'League A, Group 1' (oud formaat)
_GROEP_RE = re.compile(r"League\s+([A-D])\s*[-,]\s*Group\s+([A-Z0-9]+)", re.I)

def team_focus(team, row, form, results, compN="de competitie"):
    parts = []
    if row:
        alld = row.get("all", {}) or {}
        g = alld.get("goals", {}) or {}
        rank = row.get("rank"); pnt = row.get("points") or 0
        pl = alld.get("played"); gf = g.get("for"); ga = g.get("against")
        if pl:   # bij 0 gespeelde duels zegt de stand nog niets (bv. speelronde 1)
            waar = f"de {esc(compN)}"
            grp = _GROEP_RE.search(row.get("group") or "")
            if grp:   # groepscompetitie (Nations League)
                waar = f"groep {grp.group(2).upper()} van League {grp.group(1).upper()}"
            parts.append(f"Met {_mv(pnt, 'punt', 'punten')} uit {_mv(pl, 'wedstrijd', 'wedstrijden')} "
                         f"staat <strong>{esc(team)}</strong> op dit moment {_ordinal(rank)} in {waar} "
                         f"(doelsaldo {gf}-{ga}).")
    parts.append(_form_verhaal(team, form, results, compN))
    return "<p>" + " ".join(parts) + "</p>"

# ---------- H2H ----------
def _h2h_line(m):
    fx=m.get("fixture",{}); dt=(fx.get("date","") or "")[:10]
    t=m.get("teams",{}); g=m.get("goals",{})
    try:
        y,mo,d = dt.split("-"); dts=f"{int(d)} {MAAND[int(mo)-1]} {y}"
    except Exception:
        dts=dt
    return (f"{dts}: {nl_name(t.get('home',{}).get('name'))} {g.get('home')}-{g.get('away')} "
            f"{nl_name(t.get('away',{}).get('name'))}")

# ---------- het gratis-kijken-blok (provider-afhankelijk) ----------
def _kijk_blok(prov, homeN, awayN, comp, tv=None, tv_free=False):
    """Stream via een bookmaker. Geen 'volledig gratis'-claims: bij een storting-aanbieder kijk je
    gratis mee met een gestort account en kun je de storting weer opnemen."""
    naam = prov["naam"]; link = prov["link"]; M = f"{esc(homeN)} vs {esc(awayN)}"
    deposit = prov.get("deposit", True)
    account = "een gestort account" if deposit else "een gratis account"
    if tv and tv_free:
        out = [f"<h3>Op welke zender is {esc(homeN)} – {esc(awayN)}? Gratis op {esc(tv)} en via {esc(naam)}</h3>"]
        out.append(f"<p>{M} is gratis live te zien op {esc(tv)}: daarvoor heb je geen abonnement nodig. "
                   f"Ben je niet in de buurt van een tv? Met {account} bij {esc(naam)} kijk je ook live mee via de "
                   f"livestream op je telefoon, tablet of laptop.</p>")
    else:
        out = [f"<h3>Op welke zender is {esc(homeN)} – {esc(awayN)}? Gratis live kijken via {esc(naam)}</h3>"]
    if tv and tv_free:
        pass                                   # uitleg staat hierboven al
    elif tv and tv.strip().lower() == "ziggo sport 1":
        out.append(f"<p>{M} is live te zien op Ziggo Sport 1: Ziggo-klanten kijken daar zonder extra kosten mee. "
                    f"Geen Ziggo? Met {account} bij {esc(naam)} kijk je het duel toch live mee via de livestream, "
                    f"zonder tv-abonnement.</p>")
    elif tv:
        out.append(f"<p>Met {account} bij {esc(naam)} kijk je {M} live mee. In Nederland is de "
                    f"{esc(comp)} wel te zien op {esc(tv)}, maar daarvoor heb je een betaald abonnement nodig. "
                    f"Via {esc(naam)} heb je voor dit duel geen abonnement nodig.</p>")
    else:
        out.append(f"<p>De wedstrijd tussen {esc(homeN)} en {esc(awayN)} is niet live te zien op de Nederlandse "
                    f"televisie. Je kunt dit {esc(comp)}-duel wel live volgen via {esc(naam)}, met "
                    f"{account}.</p>")
    out.append(f"<p><strong>Zo werkt gratis meekijken via {esc(naam)}:</strong></p>")
    if deposit:
        out.append("<ol>"
                   f"<li>Maak een account aan bij {esc(naam)} via de link hieronder</li>"
                   "<li>Stort €10 op je account; met een gestort account krijg je toegang tot de livestream</li>"
                   f"<li>Kijk {M} live mee in HD</li>"
                   "<li>Je storting kun je daarna weer opnemen</li>"
                   "</ol>")
        out.append("<p>Het meekijken zelf is gratis met een gestort account; je storting kun je weer opnemen.</p>")
    else:
        out.append("<ol>"
                   f"<li>Maak een gratis account aan bij {esc(naam)} via de link hieronder</li>"
                   "<li>Log in op je account</li>"
                   f"<li>Kijk {M} live mee in HD</li>"
                   "</ol>")
        out.append("<p>Je hebt alleen een gratis account nodig; een storting is niet nodig.</p>")
    if naam.lower() == "starcasino":      # verzoek Starcasino: aanbod onder voorbehoud (9 okt 2026)
        out.append("<p><em>Let op: het streamaanbod van Starcasino is onder voorbehoud van wijzigingen. Niet elke "
                   "wedstrijd wordt uitgezonden; tijdens het duel zie je in het live-gedeelte of er een stream is.</em></p>")
    bm = BOOKMAKER_PAGINAS.get(naam.lower())
    if bm:
        u = f"/zenders/{bm}"
        varianten = [
            f'<p>Welke wedstrijden {esc(naam)} nog meer uitzendt, lees je op onze pagina over '
            f'<a href="{u}">de livestreams van {esc(naam)}</a>.</p>',
            f'<p>Benieuwd hoe kijken bij {esc(naam)} precies werkt? Op <a href="{u}">onze {esc(naam)}-pagina</a> staan '
            f'alle voorwaarden en het aanbod.</p>',
            f'<p>Meer over het aanbod en de voorwaarden: <a href="{u}">{esc(naam)} livestream</a>.</p>',
            "",
        ]
        zin = varianten[_variant(f"bm|{homeN}|{awayN}", len(varianten))]
        if zin:
            out.append(zin)
    if prov.get("cast"):
        out.append(f"<p><strong>Wil je op groot scherm kijken?</strong> Cast de {esc(naam)}-stream via "
                    f"Chromecast, AirPlay of een HDMI-kabel naar je televisie.</p>")
    out.append(f'<p><a href="{link}"><strong>Open een {esc(naam)}-account en kijk '
               f'{esc(homeN)} – {esc(awayN)} live</strong></a></p>')
    return "\n".join(out)

# ---------- 'Waar te zien op tv': opsomming van alle zenders + streaming-bookmakers ----------
# ---------- zenderpagina's (/zenders/<slug>) en organische variatie ----------
ZENDER_PAGINAS = [   # (patroon op zendernaam, slug van de zenderpagina)
    (r"^espn", "espn"), (r"^ziggo sport", "ziggo-sport"), (r"^viaplay", "viaplay"), (r"^dazn", "dazn"),
    (r"^prime video", "prime-video"), (r"^apple tv", "apple-tv"), (r"^(npo|nos)", "nos"),
    (r"^eurosport", "eurosport"), (r"^hbo max", "hbo-max"), (r"^kijk$", "kijk"), (r"^canal\+", "canal-plus"),
    (r"^f1 tv", "f1-tv"), (r"^eyecons", "eyecons"), (r"^onefootball", "onefootball"),
]
BOOKMAKER_PAGINAS = {"toto": "toto", "bet365": "bet365", "711": "711", "starcasino": "starcasino"}

def zender_pagina(naam):
    t = (naam or "").strip().lower()
    for pat, slug in ZENDER_PAGINAS:
        if re.search(pat, t):
            return f"/zenders/{slug}"
    return None

def _variant(sleutel, n):
    """Vaste keuze per wedstrijd (zelfde artikel = zelfde tekst bij elke update), verschillend tussen artikelen."""
    import hashlib
    return int(hashlib.md5(sleutel.encode()).hexdigest(), 16) % n

def kanaal_label(tv):
    """Korte uitleg per zender: wat heb je nodig om te kijken."""
    t = (tv or "").strip().lower()
    if t.startswith("npo"):
        return "gratis"
    if t == "ziggo sport 1":
        return "gratis voor Ziggo-klanten"
    if t == "espn 1":
        return "gratis, zit in elk tv-pakket"
    if re.fullmatch(r"espn [234]", t):
        return "bij Ziggo standaard in het tv-pakket, bij KPN en Odido met ESPN Compleet"
    if t == "espn extra":
        return "in de ESPN-app, met een ESPN-abonnement"
    if re.fullmatch(r"ziggo sport [2-6]", t):
        return "met Ziggo Sport Totaal, via Ziggo, KPN of Odido"
    if t in ("viaplay", "dazn", "apple tv", "prime video", "fanatiz") or "viaplay" in t:
        return "met een abonnement"
    return "met een abonnement"

def _streams(ctx):
    """[(naam, link of None)] — bookmakers waar deze wedstrijd live te volgen is."""
    out, seen = [], set()
    def add(naam, link):
        k = naam.lower().replace(" sport", "")
        if k not in seen:
            seen.add(k); out.append((naam, link))
    if ctx.get("stream_ok"):
        add(ctx["prov"]["naam"], ctx["prov"]["link"])
    card = ctx.get("tvgids") or {}
    for b in card.get("bookmakers") or []:
        key = b.lower().replace(" sport", "").strip()
        pv = PROVIDERS.get(key)
        add(pv["naam"] if pv else b, pv["link"] if pv else None)
    return out

try:
    import json as _json, os as _os
    KANAALNUMMERS = {k: v for k, v in _json.load(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)),
                     "data", "kanaalnummers.json"), encoding="utf-8")).items() if not k.startswith("_")}
except Exception:
    KANAALNUMMERS = {}

_T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
_TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
_TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'

def kanaal_tabel(zender):
    """Tabel 'Provider | Kanaalnummer <zender>' (alleen als we de nummers kennen)."""
    rij = KANAALNUMMERS.get(zender)
    if not rij:
        return ""
    body = "".join(f"<tr><td {_TD}>{esc(p)}</td><td {_TD}>{esc(n)}</td></tr>" for p, n in rij.items())
    return (f"<table {_T}><thead><tr><th {_TH}>Provider</th><th {_TH}>Kanaalnummer {esc(zender)}</th></tr></thead>"
            f"<tbody>{body}</tbody></table>")

def waar_te_zien(ctx):
    homeN, awayN, dt = ctx["homeN"], ctx["awayN"], ctx["dt"]
    tvs = [z.strip() for z in re.split(r"\s+en\s+|,", ctx.get("tv") or "") if z.strip()]
    items, gelinkt = [], set()
    for z in tvs:
        url = zender_pagina(z)
        naam = esc(z)
        if url and url not in gelinkt:                  # elke zenderpagina één keer linken
            gelinkt.add(url); naam = f'<a href="{url}">{naam}</a>'
        items.append(f"<li><strong>{naam}</strong> ({esc(kanaal_label(z))}): live vanaf {nl_tijd(dt)} uur</li>")
    if not tvs:
        items.append("<li><strong>Nederlandse tv</strong>: niet te zien</li>")
    for naam, link in _streams(ctx):
        pv = next((p for p in PROVIDERS.values() if p["naam"].lower() == naam.lower()), None)
        acc = ("met een gestort account" if pv.get("deposit", True) else "met een gratis account") if pv else "met een account"
        n = f'<a href="{link}">{esc(naam)}</a>' if link else esc(naam)
        items.append(f"<li><strong>Livestream {n}</strong> ({acc}, 18+)</li>")
    tabellen = "".join(kanaal_tabel(z) for z in tvs)
    H = "/nieuws/sportzenders-kanaalnummers"
    hub_varianten = [
        f'<p>Alle kanaalnummers per provider staan in ons <a href="{H}">overzicht van sportzenders</a>.</p>',
        f'<p>Zoek je het kanaalnummer bij een andere provider? Kijk dan in onze <a href="{H}">lijst met sportzenders '
        f'en kanaalnummers</a>.</p>',
        f'<p>Welke sportzender bij jouw tv-pakket hoort, zie je in het <a href="{H}">overzicht van alle '
        f'sportzenders</a>.</p>',
        "",                                            # niet elk artikel linkt naar het overzicht
    ]
    hub = hub_varianten[_variant(f"hub|{homeN}|{awayN}|{dt.date()}", len(hub_varianten))] if tvs else ""
    return (f"<h3>Waar is {esc(homeN)} – {esc(awayN)} op tv?</h3>"
            "<ul>" + "".join(items) + "</ul>" + tabellen + hub)

# ---------- variant voor gratis tv (bv. Oranje op NPO) ----------
# Hier beloven we GEEN bookmaker-stream (rechten liggen bij de NOS); de aanbieder
# wordt alleen genoemd voor live meewedden tijdens de wedstrijd.
def _kijk_blok_gratis(prov, homeN, awayN, tv, dt, extra=None, voorbeschouwing=None):
    M = f"{esc(homeN)} – {esc(awayN)}"
    out = [f"<h3>Op welke zender is {esc(homeN)} – {esc(awayN)}? Gratis op {esc(tv)}</h3>"]
    out.append(f"<p>{M} is gewoon gratis live te zien op {esc(tv)}. Je hebt geen abonnement of account "
               f"nodig: zet om {nl_tijd(dt)} uur de tv aan en je bent erbij."
               + (f" Niet in de buurt van een tv? Dan kijk je live mee via {esc(extra)}, ook gratis." if extra else "")
               + "</p>")
    out.append("<p><strong>Zo kijk je gratis mee:</strong></p>")
    stappen = []
    if voorbeschouwing:
        stappen.append(f"<li>Schakel om {esc(voorbeschouwing)} uur in voor de voorbeschouwing op {esc(tv)}</li>")
    stappen.append(f"<li>De aftrap is om {nl_tijd(dt)} uur, live op {esc(tv)}</li>")
    if extra:
        stappen.append(f"<li>Onderweg? Kijk via {esc(extra)} naar de gratis livestream</li>")
    if (tv or "").upper().startswith("NPO"):
        stappen.append("<li>Via NPO Start kun je de uitzending ook op je laptop of tablet volgen</li>")
    out.append("<ol>" + "".join(stappen) + "</ol>")
    out.append(f"<h3>Live meewedden op {M}</h3>")
    out.append(f"<p>Wil je tijdens de wedstrijd live meewedden? Bij {esc(prov['naam'])} volg je de actuele "
               f"live-odds van {M} en speel je in op het wedstrijdverloop.</p>")
    out.append(f'<p><a href="{prov["link"]}"><strong>Open een account bij {esc(prov["naam"])} en wed live '
               f'mee op {M}</strong></a></p>')
    return "\n".join(out)

def _kijk_blok_betaald(prov, homeN, awayN, tv, dt, comp, extra=None):
    """Alleen via betaalde tv te zien en geen bookmaker-stream bekend in de tv-gids (bv. Nations League
    op Ziggo Sport). We beweren niet dat géén bookmaker het duel uitzendt; de aanbieder staat er alleen
    voor live meewedden."""
    M = f"{esc(homeN)} – {esc(awayN)}"
    ziggo = "ziggo" in (tv or "").lower()
    out = [f"<h3>Op welke zender is {esc(homeN)} – {esc(awayN)}? Live op {esc(tv)}</h3>"]
    out.append(f"<p>{M} is in Nederland live te zien op {esc(tv)}. Daarvoor heb je wel een abonnement nodig"
               + (" bij Ziggo" if ziggo else "") + ".</p>")
    out.append("<p><strong>Zo kijk je live mee:</strong></p>")
    stappen = [f"<li>Zet om {nl_tijd(dt)} uur {esc(tv)} aan voor de aftrap</li>"]
    if ziggo:
        stappen.append("<li>Onderweg? Met je Ziggo-abonnement kijk je ook mee via de Ziggo GO-app</li>")
    elif extra:
        stappen.append(f"<li>Onderweg? Met een abonnement kijk je online mee via {esc(extra)}</li>")
    stappen.append("<li>Geen abonnement? Volg de wedstrijd dan via een liveticker of de live-odds</li>")
    out.append("<ol>" + "".join(stappen) + "</ol>")
    out.append(f"<h3>Live meewedden op {M}</h3>")
    out.append(f"<p>Wil je tijdens de wedstrijd live meewedden? Bij {esc(prov['naam'])} volg je de actuele "
               f"live-odds van {M} en speel je in op het wedstrijdverloop.</p>")
    out.append(f'<p><a href="{prov["link"]}"><strong>Open een account bij {esc(prov["naam"])} en wed live '
               f'mee op {M}</strong></a></p>')
    return "\n".join(out)

def _kijk_blok_basis(prov, homeN, awayN, tv, dt, comp):
    """Te zien op een zender uit het basispakket (bv. Jong Oranje op ESPN 1), geen bookmaker-stream."""
    M = f"{esc(homeN)} – {esc(awayN)}"
    out = [f"<h3>Op welke zender is {esc(homeN)} – {esc(awayN)}? Live op {esc(tv)}</h3>"]
    out.append(f"<p>{M} is in Nederland live te zien op {esc(tv)}. Die zender zit bij de meeste "
               f"Nederlandse tv-aanbieders in het basispakket, dus met een gewoon tv-abonnement kijk je "
               f"zonder extra kosten mee. Twijfel je? Controleer dan even de zenderlijst van je aanbieder.</p>")
    out.append("<p><strong>Zo kijk je live mee:</strong></p>")
    out.append("<ol>"
               f"<li>Zet om {nl_tijd(dt)} uur {esc(tv)} aan voor de aftrap</li>"
               "<li>Onderweg? Via de tv-app van je aanbieder kijk je ook op je telefoon of tablet mee</li>"
               "<li>Geen tv in de buurt? Volg de wedstrijd dan via een liveticker of de live-odds</li>"
               "</ol>")
    out.append(f"<h3>Live meewedden op {M}</h3>")
    out.append(f"<p>Wil je tijdens de wedstrijd live meewedden? Bij {esc(prov['naam'])} volg je de actuele "
               f"live-odds van {M} en speel je in op het wedstrijdverloop.</p>")
    out.append(f'<p><a href="{prov["link"]}"><strong>Open een account bij {esc(prov["naam"])} en wed live '
               f'mee op {M}</strong></a></p>')
    return "\n".join(out)

# ---------- precieze zenderuitleg per competitie (ESPN / Ziggo Sport UEFA) ----------
def zender_uitleg(soort, tv, comp, nl_club=False, competitiefase=False):
    """Geeft (alinea's, gratis_antwoord, online_antwoord) voor de exacte zender van deze wedstrijd.
    Feiten per oktober 2026; bij een algemene zender ('ESPN', 'Ziggo Sport') staat het kanaal nog niet vast."""
    t = (tv or "").lower()
    if soort == "espn":
        if "espn 1" in t:
            zin = ("ESPN 1 is gratis: de zender zit bij elke Nederlandse tv-aanbieder standaard in het tv-pakket, "
                   "dus je kijkt zonder extra abonnement mee.")
            gratis = "Ja, ESPN 1 is gratis: de zender zit standaard in elk tv-pakket."
        elif re.search(r"espn [234]", t):
            zin = (f"Bij Ziggo zit {tv} sinds juli 2026 standaard in elk tv-pakket. Bij KPN en Odido boek je de "
                   "ESPN-kanalen erbij met ESPN Compleet; een los abonnement rechtstreeks bij ESPN bestaat niet.")
            gratis = (f"Voor Ziggo-klanten wel: {tv} zit daar standaard in het tv-pakket. Bij KPN en Odido heb je "
                      "ESPN Compleet nodig.")
        elif "extra" in t:
            zin = ("Deze wedstrijd staat niet op een vast ESPN-kanaal, maar wordt live uitgezonden als extra stream "
                   "(ESPN Extra) in de ESPN-app. Daarvoor heb je een ESPN-abonnement nodig.")
            gratis = "Nee, ESPN Extra kijk je met een ESPN-abonnement in de ESPN-app."
        else:
            zin = (f"Alle {comp}-wedstrijden worden uitgezonden door ESPN, op ESPN 1 tot en met 4 en in de ESPN-app. "
                   "Welk kanaal deze wedstrijd krijgt, maakt ESPN ongeveer een week van tevoren bekend; we werken dit "
                   "artikel bij zodra dat bekend is. ESPN 1 zit bij vrijwel elke aanbieder in het basispakket, bij "
                   "Ziggo zitten ook ESPN 2, 3 en 4 standaard in het pakket.")
            gratis = ("Dat hangt af van het kanaal: ESPN 1 zit bij vrijwel elke aanbieder in het basispakket, en bij "
                      "Ziggo zitten ook ESPN 2, 3 en 4 standaard in het tv-pakket.")
        online = ("Ja, via de ESPN-app of de app van je tv-aanbieder, afhankelijk van je abonnement. Bij Ziggo stream "
                  "je ESPN in de Ziggo GO-app met ESPN Premium.")
        extra = ("Samenvattingen van alle Eredivisie-wedstrijden zie je gratis bij NOS Studio Sport op NPO 1."
                 if "eredivisie" in comp.lower() else
                 "Op vrijdagavond zendt ESPN 1 ook het schakelprogramma Voetbal op Vrijdag uit, dat live tussen "
                 "de wedstrijden wisselt." if "kampioen" in comp.lower() else "")
        return [zin] + ([extra] if extra else []), gratis, online
    if soort == "ziggo-uefa":
        delen = []
        if nl_club and competitiefase:
            delen.append("Omdat er een Nederlandse club speelt, is deze wedstrijd in de competitiefase voor iedereen "
                         "gratis te zien via Ziggo Sport Free, op ziggo.nl/uefa en in de Ziggo GO-app. Daarvoor heb "
                         "je geen Ziggo-abonnement nodig.")
            gratis = ("Ja. Wedstrijden van Nederlandse clubs in de competitiefase zijn voor iedereen gratis via "
                      "Ziggo Sport Free (ziggo.nl/uefa en de Ziggo GO-app).")
        else:
            gratis = None
        if re.search(r"ziggo sport 1\b", t):
            delen.append("Ziggo Sport 1 is het open kanaal (kanaal 14 bij Ziggo): Ziggo-klanten kijken daar zonder "
                         "extra kosten mee met hun gewone tv-pakket.")
            gratis = gratis or "Voor Ziggo-klanten wel: Ziggo Sport 1 is het open kanaal en zit in elk tv-pakket."
        elif re.search(r"ziggo sport [2-6]", t):
            delen.append(f"Voor {tv} heb je Ziggo Sport Totaal nodig, te boeken bij Ziggo, KPN en Odido.")
            gratis = gratis or f"Nee, voor {tv} heb je Ziggo Sport Totaal nodig."
        else:
            delen.append(f"Ziggo Sport heeft de rechten van de {comp} en maakt ongeveer een week vooraf per wedstrijd "
                         "het kanaal bekend; we werken dit artikel bij zodra dat bekend is. Elke speelavond staat minstens "
                         "één wedstrijd op het open kanaal Ziggo Sport 1, de overige zie je met Ziggo Sport Totaal.")
            gratis = gratis or ("Dat hangt af van het kanaal: Ziggo Sport 1 is gratis voor Ziggo-klanten, voor de "
                                "andere kanalen heb je Ziggo Sport Totaal nodig.")
        delen.append(f"Wil je alle doelpunten van de avond tegelijk volgen? Het Switch-programma op Ziggo Sport 4 "
                     f"schakelt live tussen de wedstrijden.")
        online = "Ja, via de Ziggo GO-app (of de Ziggo Sport Totaal GO-app) op je telefoon, tablet of laptop."
        return delen, gratis, online
    return [], None, None

def _kijk_blok_zender(prov, homeN, awayN, tv, dt, comp, soort, nl_club=False, competitiefase=False):
    M = f"{esc(homeN)} – {esc(awayN)}"
    delen, _, _ = zender_uitleg(soort, tv, comp, nl_club, competitiefase)
    out = [f"<h3>Op welke zender is {esc(homeN)} – {esc(awayN)}? Live op {esc(tv)}</h3>",
           f"<p>{M} is in Nederland live te zien op <strong>{esc(tv)}</strong>, {esc(nl_wanneer(dt))}.</p>"]
    out += [f"<p>{esc(d)}</p>" for d in delen]
    stappen = [f"<li>Zet om {nl_tijd(dt)} uur {esc(tv)} aan voor de aftrap</li>"]
    if soort == "ziggo-uefa" and nl_club and competitiefase:
        stappen.append("<li>Geen Ziggo? Kijk gratis via Ziggo Sport Free op ziggo.nl/uefa of in de Ziggo GO-app</li>")
    stappen.append("<li>Onderweg? Kijk mee via de app van je tv-aanbieder"
                   + (" of de ESPN-app" if soort == "espn" else " of de Ziggo GO-app") + "</li>")
    out.append("<p><strong>Zo kijk je live mee:</strong></p><ol>" + "".join(stappen) + "</ol>")
    out.append(f"<h3>Live meewedden op {M}</h3>")
    out.append(f"<p>Wil je tijdens de wedstrijd live meewedden? Bij {esc(prov['naam'])} volg je de actuele "
               f"live-odds van {M} en speel je in op het wedstrijdverloop.</p>")
    out.append(f'<p><a href="{prov["link"]}"><strong>Open een account bij {esc(prov["naam"])} en wed live '
               f'mee op {M}</strong></a></p>')
    return "\n".join(out)

def _faq_zender(homeN, awayN, comp, dt, tv, soort, nl_club=False, competitiefase=False):
    _, gratis, online = zender_uitleg(soort, tv, comp, nl_club, competitiefase)
    q = [
        (f"Waar kun je {homeN} – {awayN} kijken?", f"Op {tv}, {nl_wanneer(dt)}."),
        (f"Hoe laat begint {homeN} – {awayN}?", _aftrap_antwoord(dt)),
        (f"Op welke zender is {homeN} – {awayN} te zien?", f"Het {comp}-duel is in Nederland live te zien op {tv}."),
        (f"Is {homeN} – {awayN} gratis te kijken?", gratis),
        ("Kan ik de wedstrijd ook online kijken?", online),
    ]
    return "\n".join(f"<p><strong>{esc(a)}</strong><br>{esc(b)}</p>" for a, b in q if b)

def _aftrap_antwoord(dt):
    if is_nacht(dt):
        return f"De aftrap is {nl_wanneer(dt)} Nederlandse tijd."
    return f"De aftrap is om {nl_tijd(dt)} uur Nederlandse tijd op {nl_datum(dt)}."

def _faq_basis(homeN, awayN, comp, dt, tv):
    q = [
        (f"Waar kun je {homeN} – {awayN} kijken?",
         f"Op {tv}, {nl_wanneer(dt)}. De zender zit bij de meeste tv-aanbieders in het basispakket."),
        (f"Hoe laat begint {homeN} – {awayN}?",
         _aftrap_antwoord(dt)),
        (f"Op welke zender is {homeN} – {awayN} te zien?",
         f"Het duel is in Nederland live te zien op {tv}."),
        (f"Is {homeN} – {awayN} gratis te kijken?",
         f"Met een gewoon tv-abonnement wel: {tv} zit bij de meeste aanbieders in het basispakket, "
         f"zonder extra kosten. Vrij te ontvangen zoals NPO is de zender niet."),
        ("Kan ik de wedstrijd ook online kijken?",
         f"Ja, via de tv-app van je aanbieder, als {tv} in je pakket zit."),
    ]
    return "\n".join(f"<p><strong>{esc(a)}</strong><br>{esc(b)}</p>" for a, b in q)

def _faq_betaald(homeN, awayN, comp, dt, tv, extra=None):
    ziggo = "ziggo" in (tv or "").lower()
    q = [
        (f"Waar kun je {homeN} – {awayN} kijken?",
         f"Op {tv}, {nl_wanneer(dt)}. Daarvoor heb je een abonnement nodig{' bij Ziggo' if ziggo else ''}."),
        (f"Hoe laat begint {homeN} – {awayN}?",
         _aftrap_antwoord(dt)),
        (f"Op welke zender is {homeN} – {awayN} te zien?",
         f"Het {comp}-duel is in Nederland live te zien op {tv}."),
        (f"Is {homeN} – {awayN} gratis te kijken?",
         f"Op tv niet: voor {tv} heb je een abonnement nodig{' bij Ziggo' if ziggo else ''}."),
        ("Kan ik de wedstrijd ook online kijken?",
         ("Ja, met een Ziggo-abonnement kijk je via de Ziggo GO-app op je telefoon, tablet of laptop."
          if ziggo else (f"Ja, via {extra}, als je een abonnement hebt." if extra
                          else f"Ja, via de online dienst van {tv}, als je een abonnement hebt."))),
    ]
    return "\n".join(f"<p><strong>{esc(a)}</strong><br>{esc(b)}</p>" for a, b in q)

def _faq_gratis(homeN, awayN, comp, dt, tv, extra=None):
    q = [
        (f"Waar kun je {homeN} – {awayN} kijken?",
         f"Gratis op {tv}, {nl_wanneer(dt)}" + (f", en online via {extra}." if extra else ".")),
        (f"Hoe laat begint {homeN} – {awayN}?",
         _aftrap_antwoord(dt)),
        (f"Op welke zender is {homeN} – {awayN} te zien?",
         f"Het {comp}-duel is live en gratis te zien op {tv}."
         + (f" Je kunt ook meekijken via {extra}." if extra else "")),
        (f"Is {homeN} – {awayN} gratis te kijken?",
         f"Ja, {tv} is gratis te zien. Je hebt geen abonnement nodig."),
        ("Kan ik de wedstrijd ook online kijken?",
         ("Ja, via NPO Start" + (f" en {extra}" if extra else "") + " kijk je gratis live mee op je telefoon, tablet of laptop.")
         if (tv or "").upper().startswith("NPO") else
         "Ja, via de app van je tv-aanbieder kijk je ook op je telefoon, tablet of laptop mee."),
    ]
    return "\n".join(f"<p><strong>{esc(a)}</strong><br>{esc(b)}</p>" for a, b in q)

# ---------- FAQ ----------
def _faq(homeN, awayN, comp, dt, prov, tv=None, tv_free=False):
    naam = prov["naam"]; deposit = prov.get("deposit", True)
    account = f"een gestort {naam}-account" if deposit else f"een gratis {naam}-account"
    if tv and tv_free:
        q = [(f"Waar kun je {homeN} – {awayN} kijken?",
              f"Gratis op {tv}, en online via de livestream van {naam} met {account}."),
             (f"Hoe laat begint {homeN} – {awayN}?", _aftrap_antwoord(dt)),
             (f"Is {homeN} – {awayN} gratis te kijken?", f"Ja, {tv} is gratis te zien; je hebt geen abonnement nodig."),
             (f"Op welke zender is {homeN} – {awayN} te zien?", f"Op {tv}, gratis.")]
        return "\n".join(f"<p><strong>{esc(a)}</strong><br>{esc(b)}</p>" for a, b in q)
    zs1 = (tv or "").strip().lower() == "ziggo sport 1"
    if zs1:
        waar = (f"Op welke zender is {homeN} – {awayN} te zien?",
                f"Op Ziggo Sport 1: gratis voor Ziggo-klanten. Zonder Ziggo kijk je mee met {account}.")
    elif tv:
        waar = (f"Op welke zender is {homeN} – {awayN} te zien?",
                f"In Nederland zendt {tv} de {comp} uit, maar daarvoor heb je een betaald abonnement nodig. "
                f"Zonder abonnement kijk je mee met {account}.")
    else:
        waar = (f"Op welke zender is {homeN} – {awayN} te zien?",
                f"Geen enkele Nederlandse tv-zender zendt dit {comp}-duel uit. Met "
                f"{account} kun je de wedstrijd wel live volgen via de livestream van {naam}.")
    q = [
        (f"Waar kun je {homeN} – {awayN} kijken?",
         (f"Op Ziggo Sport 1 (gratis voor Ziggo-klanten), of via de livestream van {naam} met {account}." if zs1 else
          f"Op {tv} met een abonnement, of zonder abonnement via de livestream van {naam} met {account}." if tv else
          f"Niet op de Nederlandse tv, wel via de livestream van {naam} met {account}.")),
        (f"Hoe laat begint {homeN} – {awayN}?", _aftrap_antwoord(dt)),
        (f"Is {homeN} – {awayN} gratis te kijken?",
         (f"Ja, met een gestort account bij {naam} kijk je gratis mee in HD. Daarvoor stort je eerst "
          f"€10; die storting kun je daarna weer opnemen.") if deposit else
         (f"Ja, met een gratis account bij {naam} kijk je de wedstrijd live in HD. "
          f"Een storting is niet nodig.")),
    ]
    if prov.get("cast"):   # alleen als de aanbieder casten ondersteunt
        q.append(("Kan ik de stream op groot scherm bekijken?",
                  "Ja, via Chromecast, AirPlay of een HDMI-kabel zet je de stream op je televisie."))
    q.append(waar)
    return "\n".join(f"<p><strong>{esc(a)}</strong><br>{esc(b)}</p>" for a,b in q)

DISCLAIMER = ("<p><em>Gokken is alleen toegestaan voor personen van 18 jaar en ouder. "
              "Wat kost gokken jou? Stop op tijd. 18+ | Speel bewust.</em></p>")

# ---------- content-delen ----------
def build_content(ctx):
    homeN, awayN = ctx["homeN"], ctx["awayN"]
    hSlug, aSlug = ctx["hSlug"], ctx["aSlug"]
    compN, compSlug = ctx["compN"], ctx["compSlug"]
    dt = ctx["dt"]; venue = ctx["venue"]; city = ctx["city"]
    ronde_txt = ctx.get("ronde_txt") or "Wedstrijd"
    referee = ctx.get("referee"); prov = ctx["prov"]
    kickoff = nl_tijd(dt)

    def clublink(slug, name):
        return f'<a href="/clubs/{slug}">{esc(name)}</a>' if slug else f"<strong>{esc(name)}</strong>"
    hLink, aLink = clublink(hSlug, homeN), clublink(aSlug, awayN)
    compLink = f'<a href="/competities/{compSlug}">{esc(compN)}</a>' if compSlug else f"<strong>{esc(compN)}</strong>"

    # ---- CONTENT (deel 1/3): intro + gratis-kijken-blok + CTA ----
    c1 = []
    free = ctx.get("tv_free")
    paid = ctx.get("tv_paid_only")   # alleen via betaalde tv, geen bookmaker-stream
    hub_txt = ("Alle wedstrijden live kijken: zenders en tijden" if paid
               else "Alle wedstrijden die je gratis live kunt kijken")
    c1.append(f'<p><a href="{HUB_PATH}">‹ {hub_txt}</a></p>')
    angle = ctx.get("angle") or f"De {esc(compN)} is in Nederland niet op de reguliere tv te zien."
    if paid:
        slot = "Hieronder lees je op welke zender je het duel live volgt en hoe laat de aftrap is."
    elif free:
        slot = f"Goed nieuws: je kijkt {esc(homeN)} – {esc(awayN)} gewoon gratis op {esc(ctx.get('tv'))}."
    else:
        acc = "gestort" if prov.get("deposit", True) else "gratis"
        slot = (f"Goed nieuws: met een {acc} {esc(prov['naam'])}-account kijk je {esc(homeN)} – {esc(awayN)} "
                f"gratis live mee.")
    c1.append(f"<p><strong>{hLink} treft {aLink} {nl_wanneer(dt)} in {ctx.get('comp_lidwoord', 'de')} "
              f"{compLink}. {angle} {slot}</strong></p>")
    c1.append(f"<p>{zoek_zin(homeN, awayN)}</p>")
    c1.append(waar_te_zien(ctx))
    vb_url = ctx.get("vb_url")
    if vb_url:
        c1.append(f'<p><strong>Lees ook:</strong> onze <a href="{vb_url}">uitgebreide voorbeschouwing van '
                  f'{esc(homeN)} – {esc(awayN)}</a> met voorspelling, odds en de vermoedelijke opstellingen.</p>')
    if ctx.get("zender_soort") and paid:
        c1.append(_kijk_blok_zender(prov, homeN, awayN, ctx.get("tv"), dt, compN, ctx["zender_soort"],
                                    ctx.get("nl_club"), ctx.get("competitiefase")))
    elif paid and ctx.get("tv_basis"):
        c1.append(_kijk_blok_basis(prov, homeN, awayN, ctx.get("tv"), dt, compN))
    elif paid:
        c1.append(_kijk_blok_betaald(prov, homeN, awayN, ctx.get("tv"), dt, compN, ctx.get("tv_extra")))
    elif free and ctx.get("stream_ok"):
        c1.append(_kijk_blok(prov, homeN, awayN, compN, ctx.get("tv"), tv_free=True))
    elif free:
        c1.append(_kijk_blok_gratis(prov, homeN, awayN, ctx.get("tv"), dt,
                                    ctx.get("tv_extra"), ctx.get("tv_voorbeschouwing")))
    else:
        c1.append(_kijk_blok(prov, homeN, awayN, compN, ctx.get("tv")))
    content = "\n".join(c1)

    # ---- CONTENT-2 (deel 2/3): wedstrijdinfo + over beide clubs ----
    c2 = []
    c2.append("<h3>Wedstrijdinformatie</h3>")
    info = (f"<strong>Wedstrijd:</strong> {esc(homeN)} – {esc(awayN)}<br>"
            f"<strong>Competitie:</strong> {esc(compN[:1].upper() + compN[1:])}{' – ' + esc(ctx['ronde_txt']) if ctx.get('ronde_txt') else ''}<br>"
            f"<strong>Datum:</strong> {nl_datum_info(dt)}<br>"
            f"<strong>Aftrap:</strong> {kickoff} uur (Nederlandse tijd{', in de nacht' if is_nacht(dt) else ''})<br>"
            f"<strong>Stadion:</strong> {esc(venue or city or 'n.n.b.')}")
    if referee:
        info += f"<br><strong>Scheidsrechter:</strong> {esc(referee)}"
    c2.append(f"<p>{info}</p>")
    c2.append(f"<h3>Over {esc(homeN)}</h3>")
    c2.append(team_focus(homeN, ctx.get("hRow"), ctx.get("hForm"), ctx.get("hResults"), compN))
    c2.append(f"<h3>Over {esc(awayN)}</h3>")
    c2.append(team_focus(awayN, ctx.get("aRow"), ctx.get("aForm"), ctx.get("aResults"), compN))
    content2 = "\n".join(c2)

    # ---- CONTENT-3 (deel 3/3): H2H + FAQ + disclaimer ----
    c3 = []
    h2h_ok = [m for m in (ctx.get("h2h") or [])
              if (m.get("goals") or {}).get("home") is not None
              and (m.get("goals") or {}).get("away") is not None]
    if h2h_ok:
        c3.append("<h3>Onderlinge duels</h3>")
        c3.append("<p>De recente onderlinge geschiedenis tussen beide ploegen:</p>")
        c3.append("<ul>" + "".join("<li>"+esc(_h2h_line(m))+"</li>" for m in h2h_ok[:5]) + "</ul>")
    if vb_url:
        c3.append(f'<p>Meer analyse? Bekijk de <a href="{vb_url}">voorbeschouwing van '
                  f'{esc(homeN)} – {esc(awayN)}</a> met onze voorspelling en de opstellingen.</p>')
    c3.append("<h3>Veelgestelde vragen</h3>")
    if (free and not ctx.get("stream_ok")) or paid:
        c3.append(_faq_zender(homeN, awayN, compN, dt, ctx.get("tv"), ctx["zender_soort"], ctx.get("nl_club"),
                              ctx.get("competitiefase")) if (paid and ctx.get("zender_soort"))
                  else _faq_gratis(homeN, awayN, compN, dt, ctx.get("tv"), ctx.get("tv_extra")) if free
                  else _faq_basis(homeN, awayN, compN, dt, ctx.get("tv")) if ctx.get("tv_basis")
                  else _faq_betaald(homeN, awayN, compN, dt, ctx.get("tv"), ctx.get("tv_extra")))
        c3.append(f'<p><a href="{prov["link"]}"><strong>Wed live mee op {esc(homeN)} – {esc(awayN)} bij '
                  f'{esc(prov["naam"])}</strong></a></p>')
    else:
        c3.append(_faq(homeN, awayN, compN, dt, prov, ctx.get("tv"), tv_free=bool(free)))
        c3.append(f'<p><a href="{prov["link"]}"><strong>Kijk {esc(homeN)} – {esc(awayN)} live via '
                  f'{esc(prov["naam"])}</strong></a></p>')
    c3.append(f'<p><a href="{HUB_PATH}"><strong>'
              + ("Bekijk alle wedstrijden die je live kunt kijken" if paid
                 else "Bekijk alle wedstrijden die je gratis live kunt kijken")
              + '</strong></a></p>')
    c3.append(DISCLAIMER)
    content3 = "\n".join(c3)

    return content, content2, content3
