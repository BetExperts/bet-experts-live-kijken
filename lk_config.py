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

def provider_for(fixture_id):
    """Deterministisch afwisselen TOTO/Bet365 op basis van fixture-id (~50/50)."""
    try:
        even = int(str(fixture_id)) % 2 == 0
    except Exception:
        even = sum(ord(c) for c in str(fixture_id)) % 2 == 0
    return PROVIDERS["toto"] if even else PROVIDERS["bet365"]

# --- Competities die de agent verwerkt ---
# worker_slug = slug in de Cloudflare Worker (voor /api/fixtures/{slug})
# comp_slug   = slug van de competitiepagina op de site (/competities/<slug>)
# naam        = weergavenaam in de tekst
# comp_id     = item-id in de Competities-collectie (referentieveld 'competitie')
LEAGUES = [
    {"worker_slug": "super-lig", "comp_slug": "super-lig", "naam": "Süper Lig",
     "comp_id": "66ed7d481dc85d2ca649595c"},
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
