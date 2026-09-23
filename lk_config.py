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
               "abonnement nodig. Zonder abonnement kun je dit Spaanse topduel ook volledig gratis streamen.")},
    {"worker_slug": "jupiler-pro-league", "comp_slug": "jupiler-pro-league", "naam": "Jupiler Pro League",
     "comp_id": "65de4c16dd6eb829e1867f4b", "tv": "DAZN",
     "force_provider": "711", "toppers_only": True,
     "top_teams": ["club brugge", "anderlecht", "genk", "antwerp", "gent", "standard", "union st"],
     "angle": ("De Jupiler Pro League is in Nederland alleen te zien op DAZN, waarvoor je een betaald "
               "account nodig hebt. Bij 711 kijk je dit Belgische topduel volledig gratis met een account.")},
    {"worker_slug": "serie-a", "comp_slug": "serie-a", "naam": "Serie A",
     "comp_id": "65de2f987de877fdf6583d0c", "tv": "Ziggo Sport",
     "force_provider": "bet365", "toppers_only": True,
     "top_teams": ["juventus", "inter", "milan", "napoli", "roma", "lazio", "atalanta", "fiorentina"],
     "angle": ("Serie A is in Nederland te zien op Ziggo Sport, maar daarvoor heb je een betaald "
               "abonnement nodig. Bet365 is de enige bookmaker in Nederland die álle Serie A-wedstrijden "
               "gratis livestreamt — zo kijk je dit Italiaanse topduel zonder abonnement en zonder kosten.")},
    {"worker_slug": "efl-cup", "comp_slug": "efl-cup", "naam": "EFL Cup",
     "comp_id": "66cc403600c5cbae73af3c82", "tv": "Viaplay",
     "force_provider": "bet365", "toppers_only": True,
     "top_teams": ["manchester city", "manchester united", "liverpool", "arsenal", "chelsea",
                   "tottenham", "newcastle", "aston villa", "west ham"],
     "angle": ("De EFL Cup (Carabao Cup) wordt in Nederland uitgezonden door Viaplay, waarvoor je een "
               "abonnement nodig hebt. Zonder abonnement volg je dit Engelse bekerduel gewoon gratis.")},
    # Nations League: alle duels zijn te zien op Ziggo Sport (betaald); Oranje gratis op NPO.
    # GEEN bookmaker streamt de Nations League -> bookmaker_stream=False: nooit 'gratis via
    # {aanbieder}' beloven; de aanbieder staat er alleen voor live meewedden.
    # tv_per_match: afwijkende zender per wedstrijd uit data/tv_wedstrijden.json (NPO, Ziggo Sport 1),
    # anders tv_default.
    {"worker_slug": "nations-league", "comp_slug": "uefa-nations-league", "naam": "Nations League",
     "comp_id": "66d5a7f7fb9f23ce90376ef4", "force_provider": "bet365",
     "tv_per_match": True, "tv_default": {"tv": "Ziggo Sport"}, "bookmaker_stream": False},
    # Afrika Cup-kwalificatie: alleen Marokko; niet op NL-tv, wel live bij Bet365 (volgens gebruiker)
    {"worker_slug": "afrika-cup-kwalificatie", "comp_slug": "afrika-cup-of-nations",
     "naam": "Afrika Cup-kwalificatie", "comp_id": "6926ce5a5247b7619744eb7c", "tv": None,
     "force_provider": "bet365", "toppers_only": True, "top_teams": ["morocco"],
     "angle": ("Veel Marokkaanse voetbalfans in Nederland willen de Leeuwen van de Atlas live volgen, "
               "maar de kwalificatie voor de Afrika Cup is hier niet op de reguliere tv te zien.")},
    # Oefeninterlands: alleen op verzoek (manual_only -> niet in de nachtelijke run),
    # via --league friendlies --fixture <id>. Aanbieder volgt waaroptv.nl (bv. 711).
    {"worker_slug": "friendlies", "comp_slug": "int-vriendschappelijke-wedstrijden",
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

def nl_name(name):
    """Vertaal een landenteam-naam naar het Nederlands (clubs blijven ongemoeid)."""
    return LANDEN_NL.get(name, name)

def club_slug(team_id, name=None):
    s = TID_SLUG.get(str(team_id))
    if s:
        return s
    if name and name in CLUB_NAME:
        return CLUB_NAME[name]
    return None
