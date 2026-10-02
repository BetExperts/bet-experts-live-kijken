# -*- coding: utf-8 -*-
"""Configuratie voor de live-kijken-agent (gratis livestream-artikelen)."""
import os, json

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "data")

# --- Webflow ---
WEBFLOW_TOKEN = os.environ.get("WEBFLOW_TOKEN", "").strip()
NIEUWS_COLLECTION = "64ff0fbd5a8f205b05d54656"
WF_API = "https://api.webflow.com/v2"

# Rubriek 'Algemeen' — live-kijken-artikelen indexeren daar (naar wens gebruiker)
# beter dan onder de rubriek 'Live kijken'. Leeg laten ("") = geen rubriek.
RUBRIEK_ID = "6502b65d49bc032ba533e7a2"

# --- Bet-Experts API-proxy (Cloudflare Worker) ---
API = "https://www.bet-experts.nl/api"

# Hub-pagina waar alle live-kijken-artikelen onder vallen (backlink in elk artikel)
HUB_PATH = "/live-kijken"

# Opschonen: artikelen ouder dan zoveel dagen NA de wedstrijd worden verwijderd
RETENTION_DAYS = 21

# --- Affiliate-aanbieders (afwisselen per wedstrijd) ---
# deposit=True  -> flow met €10 storten (en €10 weer opnemen)
# deposit=False -> alleen een gratis account, geen storting
# cast=True     -> extra alinea over casten naar groot scherm
PROVIDERS = {
    "toto": {
        "naam": "TOTO",
        "link": "https://partner.toto.nl/C.ashx?btag=a_375b_619c_&affid=184&siteid=375&adid=619&c=",
        "cast": False, "deposit": True,
    },
    "bet365": {
        "naam": "Bet365",
        "link": "https://www.bet365.nl/hub/nl-nl/open-account?affiliate=365_02599619",
        "cast": True, "deposit": True,
    },
    "711": {
        "naam": "711",
        "link": "https://media1.711affiliates.nl/redirect.aspx?pid=2395&bid=1505",
        "cast": False, "deposit": False,
    },
}

def provider_for(fixture_id, force=None):
    """Kies aanbieder. `force` ('toto'/'bet365') = vast per competitie; anders
    deterministisch afwisselen op fixture-id-pariteit (~50/50)."""
    if force in PROVIDERS:
        return PROVIDERS[force]
    try:
        even = int(str(fixture_id)) % 2 == 0
    except Exception:
        even = sum(ord(c) for c in str(fixture_id)) % 2 == 0
    return PROVIDERS["toto"] if even else PROVIDERS["bet365"]

# --- Op welke NL-zender is een competitie te zien? (uit data/tv_zenders.json) ---
def _tv_map():
    try:
        raw = json.load(open(os.path.join(DATA, "tv_zenders.json"), encoding="utf-8"))
    except Exception:
        return {}
    m = {}
    for zender, comps in raw.items():
        if zender.startswith("_") or not isinstance(comps, list):
            continue
        for c in comps:
            key = c.split("(")[0].strip().lower()
            m.setdefault(key, zender)
    return m
TV_ZENDERS = _tv_map()

# Handmatige aliassen naar de namen in tv_zenders.json
TV_ALIASES = {
    "la liga": "laliga", "champions league": "uefa champions league",
    "europa league": "uefa europa league", "conference league": "uefa conference league",
}

def tv_for(naam):
    """Retourneert de NL-zender voor een competitienaam, of None (= niet op reguliere NL-tv)."""
    if not naam:
        return None
    key = naam.strip().lower()
    key = TV_ALIASES.get(key, key)
    return TV_ZENDERS.get(key)

def is_topper(fx, cfg):
    """True als de wedstrijd een 'topper' is (of als de competitie geen filter kent)."""
    if not cfg.get("toppers_only"):
        return True
    tops = [t.lower() for t in cfg.get("top_teams", [])]
    t = fx.get("teams", {})
    names = ((t.get("home", {}) or {}).get("name", "") + " | " +
             (t.get("away", {}) or {}).get("name", "")).lower()
    return any(top in names for top in tops)

# --- Competities die de agent verwerkt ---
# worker_slug = slug in de Cloudflare Worker (voor /api/fixtures/{slug})
# comp_slug   = slug van de competitiepagina op de site (/competities/<slug>)
# naam        = weergavenaam in de tekst
# comp_id     = item-id in de Competities-collectie (referentieveld 'competitie')
# force_provider : 'toto'/'bet365' = vaste aanbieder voor die competitie (anders afwisselen)
# toppers_only   : True = alleen wedstrijden met een 'groot team' (top_teams) krijgen een artikel
# angle          : introzin die de competitie-invalshoek zet
LEAGUES = [
    {"worker_slug": "super-lig", "comp_slug": "super-lig", "naam": "Süper Lig",
     "comp_id": "66ed7d481dc85d2ca649595c", "tv": None,
     "angle": ("Veel Turkse voetbalfans in Nederland willen dit duel live volgen, maar de Süper Lig "
               "is hier niet op de reguliere tv te zien.")},
    {"worker_slug": "la-liga", "comp_slug": "la-liga", "naam": "La Liga",
     "comp_id": "65eafa89159aadee0c5d81d2", "tv": "Ziggo Sport",
     "force_provider": "toto", "toppers_only": True,
     "top_teams": ["real madrid", "barcelona", "atletico madrid", "atlético madrid", "athletic",
                   "real sociedad", "sevilla", "real betis", "villarreal", "valencia"],
     "angle": ("La Liga is in Nederland te zien op Ziggo Sport, maar daarvoor heb je een betaald "
               "abonnement nodig. Zonder abonnement kun je dit Spaanse topduel ook gratis live meekijken.")},
    {"worker_slug": "jupiler-pro-league", "comp_slug": "jupiler-pro-league", "naam": "Jupiler Pro League",
     "comp_id": "65de4c16dd6eb829e1867f4b", "tv": "DAZN",
     "force_provider": "711", "toppers_only": True,
     "top_teams": ["club brugge", "anderlecht", "genk", "antwerp", "gent", "standard", "union st"],
     "angle": ("De Jupiler Pro League is in Nederland alleen te zien op DAZN, waarvoor je een betaald "
               "account nodig hebt. Bij 711 kijk je dit Belgische topduel gratis mee met een account.")},
    {"worker_slug": "serie-a", "comp_slug": "serie-a", "naam": "Serie A",
     "comp_id": "65de2f987de877fdf6583d0c", "tv": "Ziggo Sport",
     "force_provider": "bet365", "toppers_only": True,
     "top_teams": ["juventus", "inter", "milan", "napoli", "roma", "lazio", "atalanta", "fiorentina"],
     "angle": ("Serie A is in Nederland te zien op Ziggo Sport, maar daarvoor heb je een betaald "
               "abonnement nodig. Bet365 streamt de Serie A live: met een gestort account kijk je dit "
               "Italiaanse topduel zonder abonnement mee.")},
    {"worker_slug": "efl-cup", "comp_slug": "efl-cup", "naam": "EFL Cup",
     "comp_id": "66cc403600c5cbae73af3c82", "tv": "Viaplay",
     "force_provider": "bet365", "toppers_only": True,
     "top_teams": ["manchester city", "manchester united", "liverpool", "arsenal", "chelsea",
                   "tottenham", "newcastle", "aston villa", "west ham"],
     "angle": ("De EFL Cup (Carabao Cup) wordt in Nederland uitgezonden door Viaplay, waarvoor je een "
               "abonnement nodig hebt. Zonder abonnement volg je dit Engelse bekerduel gewoon gratis.")},
    # Nations League: alle duels zijn te zien op Ziggo Sport (betaald); Oranje gratis op NPO.
    # bookmaker_stream=False: standaard geen stream beloven en de aanbieder alleen voor live
    # meewedden noemen. Uitzondering: noemt de tv-gids (waaroptv) een van onze aanbieders als
    # stream bij die wedstrijd, dan tonen we die stream wel (zie lk_match.build_fielddata).
    # We schrijven nooit dat 'geen enkele bookmaker' een duel uitzendt.
    # tv_per_match: afwijkende zender per wedstrijd uit data/tv_wedstrijden.json (NPO, Ziggo Sport 1),
    # anders tv_default.
    {"worker_slug": "nations-league", "landen": True, "comp_slug": "uefa-nations-league", "naam": "Nations League",
     "comp_id": "66d5a7f7fb9f23ce90376ef4", "force_provider": "bet365",
     "tv_per_match": True, "tv_default": {"tv": "Ziggo Sport"}, "bookmaker_stream": False},
    # Afrika Cup-kwalificatie: alleen Marokko; niet op NL-tv, wel live bij Bet365 (volgens gebruiker)
    {"worker_slug": "afrika-cup-kwalificatie", "landen": True, "comp_slug": "afrika-cup-of-nations",
     "naam": "Afrika Cup-kwalificatie", "comp_id": "6926ce5a5247b7619744eb7c", "tv": None,
     "force_provider": "bet365", "toppers_only": True, "top_teams": ["morocco"], "top_teams_nl": ["marokko"],
     "angle": ("Veel Marokkaanse voetbalfans in Nederland willen de Leeuwen van de Atlas live volgen, "
               "maar de kwalificatie voor de Afrika Cup is hier niet op de reguliere tv te zien."),
     "angle_other": ("De kwalificatie voor de Afrika Cup is in Nederland niet op de reguliere tv te zien, "
                     "maar je kunt dit duel wel gratis live streamen.")},
    # CONCACAF Nations League: alleen op verzoek (manual_only). Niet op NL-tv; stream per wedstrijd via --provider.
    {"worker_slug": "concacaf-nations-league", "landen": True, "comp_slug": "concacaf-nations-league",
     "naam": "CONCACAF Nations League", "comp_id": "67d94eb39a4451a4d52c444c", "tv": None,
     "force_provider": "bet365", "manual_only": True,
     "angle": ("Met onder meer Suriname, Curaçao, Aruba en Bonaire spelen er in de CONCACAF Nations League "
               "meerdere landen met een sterke band met Nederland. Toch is het toernooi hier niet op de "
               "reguliere tv te zien.")},
    # EK onder 21-kwalificatie: alleen Jong Oranje. Live op ESPN 1 (basispakket bij de meeste
    # tv-aanbieders). Geen bookmaker-stream beloven; aanbieder alleen voor live meewedden.
    {"worker_slug": "u21-ek-kwalificatie", "landen": True, "comp_slug": "ek-onder-21-kwalificatie",
     "naam": "EK onder 21-kwalificatie", "comp_id": "6abaf551b3633bce07b3312c", "tv": "ESPN 1",
     "bookmaker_stream": False, "tv_basis": True, "geen_ronde": True,
     "toppers_only": True, "top_teams": ["netherlands u21"],
     "angle": ("De EK-kwalificatieduels van Jong Oranje worden in Nederland live uitgezonden door ESPN.")},
    # Oefeninterlands: alleen op verzoek (manual_only -> niet in de nachtelijke run),
    # via --league friendlies --fixture <id>. Aanbieder volgt waaroptv.nl (bv. 711).
    {"worker_slug": "friendlies", "landen": True, "comp_slug": "int-vriendschappelijke-wedstrijden",
     "naam": "oefeninterland", "comp_id": "65f9b20c402bb844e2ad0bf4", "tv": None,
     "force_provider": "711", "manual_only": True, "lidwoord": "een", "geen_ronde": True,
     "angle": ("Deze oefeninterland is in Nederland niet op de reguliere tv te zien, "
               "maar je kunt hem wel gratis live streamen.")},
]

# --- Tv-zender per wedstrijd (data/tv_wedstrijden.json, sleutel = fixture-id) ---
def _tv_match_map():
    try:
        raw = json.load(open(os.path.join(DATA, "tv_wedstrijden.json"), encoding="utf-8"))
    except Exception:
        return {}
    return {k: v for k, v in raw.items() if not k.startswith("_") and isinstance(v, dict)}
TV_MATCH = _tv_match_map()

def tv_match(fixture_id):
    """Tv-info voor één wedstrijd ({'tv','gratis','extra','voorbeschouwing'}) of None als onbekend."""
    return TV_MATCH.get(str(fixture_id))

def angle_for_match(info, comp):
    """Introzin voor een competitie met tv per wedstrijd."""
    tv = (info or {}).get("tv")
    if not tv:
        return (f"Dit {comp}-duel wordt in Nederland niet door een reguliere tv-zender uitgezonden.")
    if (info or {}).get("gratis"):
        return "Voor deze wedstrijd heb je geen abonnement of betaalde dienst nodig."
    return f"Het duel is in Nederland live te zien op {tv}; daarvoor heb je wel een abonnement nodig."

def is_ziggo(tv):
    return "ziggo" in (tv or "").lower()

# --- Data-mappings (hergebruikt uit opstellingen-agent) ---
def _load(fn):
    try:
        return json.load(open(os.path.join(DATA, fn), encoding="utf-8"))
    except Exception:
        return {}

TID_SLUG  = _load("tid_slug.json")               # API team-id -> website club-slug
CLUB_NAME = _load("club_name_slug_filled.json")  # clubnaam -> slug (gevulde clubs)
LANDEN_NL = _load("landen_nl.json")              # Engelse API-landnaam -> Nederlandse naam
_LANDEN_LOW = {k.lower(): v for k, v in LANDEN_NL.items()}   # API levert soms 'andorra'
# API-stadionnaam -> Nederlandse naam (null = onbetrouwbaar, weglaten). Zelfde bestand als in
# ../opstellingen-agent/data/stadions_nl.json.
STADIONS_NL = {k: v for k, v in _load("stadions_nl.json").items() if not k.startswith("_")}

def _stadion_key(s):
    import unicodedata, re
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()
_STADIONS_KEY = {_stadion_key(k): v for k, v in STADIONS_NL.items()}

def stadion_nl(name):
    """Stadionnaam zoals Nederlanders hem kennen; None als de API-naam als onbetrouwbaar is
    gemarkeerd (dan valt de tekst terug op de stad). Onbekend -> ongewijzigd."""
    name = (name or "").strip()
    if not name:
        return None
    if name in STADIONS_NL:
        return STADIONS_NL[name] or None
    key = _stadion_key(name)
    if key in _STADIONS_KEY:
        return _STADIONS_KEY[key] or None
    return name

def nl_name(name):
    """Vertaal een landenteam-naam naar het Nederlands (clubs blijven ongemoeid).
    Jeugdelftallen: 'Slovenia U21' -> 'Jong Slovenië', 'Netherlands U21' -> 'Jong Oranje'."""
    if name and name.endswith(" U21"):
        base = name[:-4]
        if base == "Netherlands":
            return "Jong Oranje"
        return "Jong " + LANDEN_NL.get(base, LANDEN_NL.get(base.replace("-", " & "), base))
    return LANDEN_NL.get(name) or _LANDEN_LOW.get((name or "").lower(), name)

def club_slug(team_id, name=None):
    s = TID_SLUG.get(str(team_id))
    if s:
        return s
    if name and name in CLUB_NAME:
        return CLUB_NAME[name]
    return None
