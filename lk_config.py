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

# Opschonen: artikelen ouder dan zoveel dagen NA de wedstrijd worden verwijderd
RETENTION_DAYS = 21

# --- Affiliate-aanbieders (afwisselen per wedstrijd) ---
PROVIDERS = {
    "toto": {
        "naam": "TOTO",
        "link": "https://partner.toto.nl/C.ashx?btag=a_375b_619c_&affid=184&siteid=375&adid=619&c=",
        "cast": False,
    },
    "bet365": {
        "naam": "Bet365",
        "link": "https://www.bet365.nl/hub/nl-nl/open-account?affiliate=365_02599619",
        "cast": True,   # Bet365 -> Chromecast/AirPlay-alinea toevoegen
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
    {"worker_slug": "efl-cup", "comp_slug": "efl-cup", "naam": "EFL Cup",
     "comp_id": "66cc403600c5cbae73af3c82", "tv": "Viaplay",
     "force_provider": "bet365", "toppers_only": True,
     "top_teams": ["manchester city", "manchester united", "liverpool", "arsenal", "chelsea",
                   "tottenham", "newcastle", "aston villa", "west ham"],
     "angle": ("De EFL Cup (Carabao Cup) wordt in Nederland uitgezonden door Viaplay, waarvoor je een "
               "abonnement nodig hebt. Zonder abonnement volg je dit Engelse bekerduel gewoon gratis.")},
]

# --- Data-mappings (hergebruikt uit opstellingen-agent) ---
def _load(fn):
    try:
        return json.load(open(os.path.join(DATA, fn), encoding="utf-8"))
    except Exception:
        return {}

TID_SLUG  = _load("tid_slug.json")               # API team-id -> website club-slug
CLUB_NAME = _load("club_name_slug_filled.json")  # clubnaam -> slug (gevulde clubs)

def club_slug(team_id, name=None):
    s = TID_SLUG.get(str(team_id))
    if s:
        return s
    if name and name in CLUB_NAME:
        return CLUB_NAME[name]
    return None
