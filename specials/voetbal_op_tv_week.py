# -*- coding: utf-8 -*-
"""Evergreen artikel: 'Voetbal op tv deze week' (/nieuws/voetbal-op-tv-deze-week), 17-11-2026.

BRON: uitsluitend onze EIGEN data.
 - wedstrijden: /api/fixtures/<worker_slug> via lk_api, voor de 21 competities in lk_config.LEAGUES
 - zender: lk_config.tv_match() (data/tv_wedstrijden.json, exacte zender per fixture-id) -> anders de
   competitiezender uit lk_config.LEAGUES -> anders lk_config.tv_for() uit data/tv_zenders.json
 - bookmakerstream: bet365_streams.py (het officiele Bet365-schema, xlsx)
GEEN externe tv-gids. waaroptv.nl en opstellingvandaag.nl zijn sinds 28-10-2026 uit (zelfde eigenaar,
voorwaarden 4.3); tvgids.py heeft daarom BASE = "". Niet opnieuw aansluiten.

Het artikel bouwt zichzelf bij elke run opnieuw op uit de live API, dus bijwerken =
opnieuw draaien + bijwerk_live.py. Daardoor blijft het een evergreen URL in plaats van
elke week een nieuw artikel (en dus een nieuwe, zwakke URL).

Bewust: alleen wedstrijden waarvan wij de Nederlandse zender kennen komen in de dagtabellen.
De rest (vooral Afrika Cup-kwalificatie en oefeninterlands) staat geteld in de tekst, niet
als 'niet op tv' - dat weten we niet zeker, we weten alleen dat onze config er niets over zegt.
  python3 specials/voetbal_op_tv_week.py        (dry run)
  publiceren: specials/concept_publiceer.py voetbal_op_tv_week --live
  bijwerken:  specials/bijwerk_live.py voetbal_op_tv_week <item-id>"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from datetime import datetime, timedelta, timezone
from legaal_data import tabel
import lk_config as C, lk_api, lk_build, bet365_streams as B365

SLUG = "voetbal-op-tv-deze-week"
RUBRIEK = C.RUBRIEK_ID   # live kijken
TITEL = "Voetbal op tv deze week: alle wedstrijden en zenders"
SAMENVATTING = ("Welke voetbalwedstrijden zijn er deze week op tv? Het complete weekoverzicht met aanvangstijden, "
                "competities en de Nederlandse zender per duel.")

DAGNAAM = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]
MAAND = ["januari", "februari", "maart", "april", "mei", "juni", "juli",
         "augustus", "september", "oktober", "november", "december"]

L = {"kijken": '<a href="/live-kijken">live kijken</a>',
     "espn": '<a href="/zenders/espn">ESPN</a>',
     "ziggo": '<a href="/zenders/ziggo-sport">Ziggo Sport</a>',
     "viaplay": '<a href="/zenders/viaplay">Viaplay</a>',
     "bet365": '<a href="/bookmakers/bet365">Bet365</a>',
     "legaal": '<a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>'}


def _naam(n):
    """Engelse API-naam -> Nederlandse naam waar wij die kennen (landen; clubs houden hun eigen naam)."""
    return C.LANDEN_NL.get(n, n)


def haal(dagen=8):
    """Alle wedstrijden van de komende <dagen> dagen uit onze eigen bronnen."""
    nu = datetime.now(timezone.utc)
    eind = nu + timedelta(days=dagen)
    uit = []
    for lg in C.LEAGUES:
        ws = lg.get("worker_slug")
        if not ws:
            continue
        try:
            data = lk_api.fixtures(ws) or {}
        except Exception:
            continue
        for f in (data.get("upcoming") or []):
            fi = f.get("fixture", {})
            iso = fi.get("date")
            if not iso:
                continue
            dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
            if not (nu <= dt <= eind):
                continue
            eigen = C.tv_match(fi.get("id")) or {}      # data/tv_wedstrijden.json, sleutel = str(fixture-id)
            zender = eigen.get("tv") or lg.get("tv") or C.tv_for(lg["naam"])
            uit.append({"lokaal": lk_build._local(iso), "comp": lg["naam"], "zender": zender,
                        "home": _naam(f["teams"]["home"]["name"]), "away": _naam(f["teams"]["away"]["name"]),
                        "id": fi.get("id"), "gratis": bool(eigen.get("gratis"))})
    uit.sort(key=lambda r: (r["lokaal"], r["comp"], r["home"]))
    return uit


ALLES = haal()
OP_TV = [r for r in ALLES if r["zender"]]
ZONDER = len(ALLES) - len(OP_TV)

# Bet365-stream alleen opvragen voor wat niet op de Nederlandse tv staat
STREAM = []
for r in ALLES:
    if r["zender"]:
        continue
    try:
        if B365.status(r["home"], r["away"], r["lokaal"]) == "ja":
            STREAM.append(r)
    except Exception:
        pass

# per dag groeperen
DAGEN = []
for r in OP_TV:
    d = r["lokaal"].date()
    if not DAGEN or DAGEN[-1][0] != d:
        DAGEN.append((d, []))
    DAGEN[-1][1].append(r)

VANDAAG = datetime.now().date()

# --- deelkaart (og_kaarten/strategie.py) ---
OG_HEADER, OG_HEADER_SUB = "Live kijken", "voetbal op tv"
OG_EYEBROW = "Weekoverzicht &middot; Nederlandse tv"
OG_KOP = "Voetbal op tv<br><span>deze week</span>"
OG_MOTIEF = "lijst"



def dagkop(d):
    if d == VANDAAG:
        return f"Vandaag, {DAGNAAM[d.weekday()]} {d.day} {MAAND[d.month - 1]}"
    if d == VANDAAG + timedelta(days=1):
        return f"Morgen, {DAGNAAM[d.weekday()]} {d.day} {MAAND[d.month - 1]}"
    return f"{DAGNAAM[d.weekday().real].capitalize()} {d.day} {MAAND[d.month - 1]}"


def dagtabel(rijen):
    return tabel(["Tijd", "Wedstrijd", "Competitie", "Zender"],
                 [(f"<strong>{r['lokaal'].strftime('%H:%M')}</strong>",
                   f"{r['home']} &ndash; {r['away']}", r["comp"], f"<strong>{r['zender']}</strong>")
                  for r in rijen])


# zenderoverzicht: per AANBIEDER (ESPN 2 / ESPN Extra -> ESPN), niet per los kanaal
def aanbieder(z):
    for naam in ("Ziggo Sport", "ESPN", "Viaplay", "DAZN", "Apple TV", "NPO"):
        if z.startswith(naam):
            return naam
    return z.split(" en ")[0].split(",")[0].strip()


PER_ZENDER, TELLER = {}, {}
for r in OP_TV:
    a = aanbieder(r["zender"])
    PER_ZENDER.setdefault(a, set()).add(r["comp"])
    TELLER[a] = TELLER.get(a, 0) + 1
ZENDERS = sorted(PER_ZENDER.items(), key=lambda kv: (-TELLER[kv[0]], kv[0]))

AANTAL_COMP = len({r["comp"] for r in OP_TV})
OG_CHIPS = [f"{len(OP_TV)} wedstrijden", f"{len(DAGEN)} dagen"]
OG_DATA = [f"{z} &middot; {TELLER[z]}" for z, _ in ZENDERS[:5]]

PERIODE = (f"{DAGEN[0][0].day} {MAAND[DAGEN[0][0].month - 1]}"
           f" tot en met {DAGEN[-1][0].day} {MAAND[DAGEN[-1][0].month - 1]}") if DAGEN else "deze week"

content = f"""<p><strong>Deze week staan er <strong>{len(OP_TV)} voetbalwedstrijden</strong> op de Nederlandse televisie, verdeeld over {AANTAL_COMP} competities en {len(DAGEN)} speeldagen, van {PERIODE}. Hieronder staat per dag welke wedstrijd hoe laat begint en op welke zender je hem ziet. Alle tijden zijn Nederlandse tijd.</strong></p>
<p>Dit overzicht maken we met onze eigen wedstrijddata en onze eigen zenderlijst, en we werken het elke week bij. Het gaat om de competities die wij volgen: de Eredivisie en de Keuken Kampioen Divisie, de vijf grote Europese competities, de Europese clubtoernooien, de Jupiler Pro League en de interlandtoernooien. Staat een wedstrijd er niet bij, dan weten wij niet zeker of er een Nederlandse zender is &mdash; we zetten liever niets neer dan iets wat niet klopt.</p>
<p><strong>Let op bij de zender.</strong> Bij een deel van de wedstrijden weten we het exacte kanaal (bijvoorbeeld ESPN 2 of Ziggo Sport 5); bij de rest staat alleen de aanbieder. Welk kanaal het precies wordt, maakt de aanbieder vaak pas een paar dagen van tevoren bekend. Meer kijkopties, inclusief de gratis manieren, staan op onze pagina {L['kijken']}.</p>
<h3><strong>Welke zender heb je nodig?</strong></h3>
{tabel(["Zender", "Wedstrijden", "Competities deze week"],
       [(f"<strong>{z}</strong>", str(TELLER[z]), ", ".join(sorted(comps))) for z, comps in ZENDERS])}
<p>In Nederland zitten de rechten verdeeld over een handvol partijen. {L['espn']} heeft het Nederlandse voetbal, {L['ziggo']} de Europese clubtoernooien en de Spaanse en Italiaanse competitie, en {L['viaplay']} de Premier League, de Bundesliga en de Ligue 1. Voor de Belgische competitie heb je DAZN nodig.</p>"""

_dagen_html = "".join(
    f"<h3><strong>{dagkop(d)}</strong></h3>"
    f"<p>{len(rs)} wedstrijd{'en' if len(rs) != 1 else ''} op tv.</p>{dagtabel(rs)}"
    for d, rs in DAGEN)

_stream_html = ""
if STREAM:
    _stream_html = (
        "<h3><strong>Niet op tv, wel te volgen via een stream</strong></h3>"
        f"<p>Van de wedstrijden die deze week niet op de Nederlandse televisie staan, zitten er "
        f"<strong>{len(STREAM)}</strong> in het streamingschema van {L['bet365']}. Met saldo op je account, of een "
        "weddenschap in de afgelopen 24 uur, kijk je die live mee in de app of op de site.</p>"
        + tabel(["Dag", "Tijd", "Wedstrijd", "Competitie"],
                [(DAGNAAM[r["lokaal"].weekday()].capitalize(), r["lokaal"].strftime("%H:%M"),
                  f"{r['home']} &ndash; {r['away']}", r["comp"]) for r in STREAM]))

content2 = f"""{_dagen_html}{_stream_html}"""

content3 = f"""<h3><strong>Hoe dit overzicht tot stand komt</strong></h3>
<p>De wedstrijden en aanvangstijden komen uit onze eigen wedstrijdendatabase, die rechtstreeks op de officiële competitiekalenders is aangesloten. De zender per wedstrijd komt uit onze eigen rechtenlijst, die we bijhouden per competitie en waar nodig per wedstrijd aanpassen. We nemen geen gegevens over van andere tv-gidsen.</p>
<p>Dat heeft één nadeel en één voordeel. Het nadeel: wij geven niet van élke wedstrijd ter wereld het exacte kanaalnummer. Het voordeel: wat er staat, klopt, en we vullen niets aan met gokwerk. Zie je een fout, laat het ons weten.</p>
<p>Aanvangstijden kunnen tot vlak voor de aftrap nog verschuiven, zeker bij wedstrijden die voor televisie worden verplaatst. Controleer bij twijfel de zender zelf.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoeveel voetbalwedstrijden zijn er deze week op tv?</strong><br>{len(OP_TV)} wedstrijden uit {AANTAL_COMP} competities, verdeeld over {len(DAGEN)} dagen. Het volledige overzicht per dag staat hierboven.</p>
<p><strong>Op welke zender is de Eredivisie?</strong><br>Alle Eredivisie-wedstrijden worden in Nederland uitgezonden door ESPN. Welk ESPN-kanaal het precies wordt, hangt af van hoeveel wedstrijden er tegelijk spelen.</p>
<p><strong>Waar kan ik de Champions League kijken?</strong><br>Bij Ziggo Sport, dat de rechten heeft tot en met het seizoen 2030/31. De belangrijkste wedstrijd staat meestal op het hoofdkanaal, de rest op de extra kanalen.</p>
<p><strong>Waar is de Premier League te zien?</strong><br>Bij Viaplay. Dat geldt ook voor de Bundesliga en de Ligue 1.</p>
<p><strong>Kan ik voetbal gratis kijken?</strong><br>Een deel van de wedstrijden is te zien op kanalen die in een standaard tv-pakket zitten. Daarnaast bieden sommige bookmakers met een Nederlandse vergunning livestreams aan voor klanten met saldo op hun account. Alle opties staan op onze pagina {L['kijken']}.</p>
<p><strong>Wanneer wordt dit overzicht bijgewerkt?</strong><br>Elke week. De tijden en zenders hierboven zijn de meest recente die wij hebben.</p>
<p>Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit; in {L['legaal']} leggen we uit waar je dat aan ziet.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    alles = content + content2 + content3
    w = len(re.sub(r"<[^>]+>", " ", alles).split())
    print(f"titel {len(TITEL)} | samenvatting {len(SAMENVATTING)} | {w} woorden")
    print(f"wedstrijden: {len(ALLES)} totaal, {len(OP_TV)} met zender, {ZONDER} zonder, {len(STREAM)} Bet365-stream")
    print(f"dagen: {len(DAGEN)} | competities op tv: {AANTAL_COMP}")
    for z, comps in ZENDERS:
        print(f"   {z:<16} {len(comps)} competities")
    assert len(TITEL) <= 60 and 120 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert len(OP_TV) >= 20, f"te weinig wedstrijden met zender ({len(OP_TV)}) - API-probleem?"
    assert len(DAGEN) >= 5, f"te weinig speeldagen ({len(DAGEN)})"
    assert all(r["zender"] for r in OP_TV)
    assert "<h2" not in alles and "<h4" not in alles and "/go/" not in alles
    for verboden in ("betcity", "waaroptv", "opstellingvandaag", "footymetrics", "squawka"):
        assert verboden not in alles.lower(), verboden
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    print("dry run ok")
