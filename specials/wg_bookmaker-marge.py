# -*- coding: utf-8 -*-
"""NIEUW wedgids-artikel (Nieuws, nog geen item): wat is de marge van een bookmaker (overround en uitbetalingspercentage)?
Slug marge-bookmaker-overround-uitbetalingspercentage (gaf HTTP 404 op 10-11-2026, dus vrij). Rubriek Speluitleg,
wedgids-categorie 'Wedden uitgelegd'. Onderwerp: Engelstalige analysesite (alleen het onderwerp, niets overgenomen).
Zoekwoorden: 'marge bookmaker' (hoofd), 'overround', 'uitbetalingspercentage bookmaker', 'marge berekenen odds',
'bookmaker marge berekenen', 'payout percentage wedden', 'marge combinatieweddenschap', 'welke bookmaker laagste marge'.

Afbakening t.o.v. /nieuws/odds-uitgelegd-quotering-lezen (gecontroleerd met curl op 10-11-2026, HTTP 200): dat artikel
legt odds lezen, breuken/Amerikaans en in één blok de marge met een fictieve 1X2 uit. Dit artikel gaat dieper: hoe de marge
wordt ingebouwd, twee definities (overround vs houdmarge), formule tweeweg, echte odds, verschil per markt, combi's die de
marge vermenigvuldigen, bookmakers vergelijken, wat het je op lange termijn kost. Basis wordt naar dat artikel gelinkt.

Feiten (bron + datum):
- ECHTE ODDS 711: publieke Kambi-feed van 711 (brand sevelevnl), gelezen op 10-11-2026 om 14:34 uur (CET):
  eu-offering-api.kambicdn.com/offering/v2018/sevelevnl/listView/football/netherlands/eredivisie.json?lang=nl_NL&market=NL&useCombined=true
  -> 9 Eredivisie-duels van 21/22-11-2026, markt 'Reguliere Speeltijd' (1X2) en 'Totaal Aantal Doelpunten' (zie ELF hieronder).
  Wedstrijdmarkten FC Groningen - SC Heerenveen (21-11-2026, 20:00 UTC = 21:00 uur NL) uit
  .../sevelevnl/betoffer/event/1027976500.json?lang=nl_NL&market=NL (zelfde moment): zie MARKTEN, CS en EERSTE_DM.
  Op de spelersmarkten ('Scoort', 'Schoten van speler op doel', '1e Doelpuntenmaker') biedt 711 alleen de Ja/Meer-kant aan,
  dus daar is per markt geen overround te berekenen; bij '1e Doelpuntenmaker' sluiten de uitkomsten elkaar uit, dus de som
  over de 25 aangeboden spelers is te vergelijken met 100%.
- Kansspelbelasting: Wet op de kansspelbelasting, wetten.overheid.nl/BWBR0002359/2026-01-01 (gelezen 10-11-2026,
  'Geldend van 01-01-2026'): art. 5 lid 1 'De belasting bedraagt 37,8 percent.'; art. 3 lid 1 a: grondslag = verschil
  tussen ontvangen inzetten en ter beschikking gestelde prijzen (bruto spelresultaat). Winnaars bij een vergunde
  online aanbieder betalen zelf niets (zie ook specials/wg_kansspelbelasting.py, art. 1 i).
- Rekenvoorbeelden (inbouwen marge, 'bookmaker B', 100 weddenschappen) zijn fictief en als zodanig gemarkeerd; alle
  getallen hieronder berekend en ge-assert. De combi-berekening gaat uit van onafhankelijke duels en een marge die
  evenredig over de uitkomsten is verdeeld (staat in de tekst).

Bewust weggelaten:
- Geen ranglijst 'bookmaker met de laagste marge': we hebben alleen 711 gemeten, dus geen vergelijkende claims.
- Geen uitspraken over de marge van bet builders (prijs per bookmaker niet na te rekenen), alleen dat je hem niet kunt narekenen.
- Geen betting exchanges (vergunningsituatie niet nagelopen), geen Shin-/power-methode (staat in het artikel kans-uit-odds).
- Geen bron van het onderwerp genoemd.
Interne links gecontroleerd op 10-11-2026 (curl, allemaal HTTP 200): zie de asserts onderaan.
Geen INFOGRAPHIC (de tabellen volstaan).
  ../superodd-agent/.venv/bin/python specials/wg_publiceer.py bookmaker-marge [--live]"""
import os, sys, re
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
import lk_webflow as WF
from legaal_data import tabel

ITEM_ID = None   # nieuw artikel
SLUG = "marge-bookmaker-overround-uitbetalingspercentage"
RUBRIEK = "6502b66cd9992658b4037cf5"   # Speluitleg
WEDGIDS_CAT = "Wedden uitgelegd"
TITEL = "Marge bookmaker: zo bereken je overround en uitbetaling"
SAMENVATTING = ("Wat is de marge van een bookmaker? Zo bereken je overround en uitbetalingspercentage, met echte odds, "
                "het verschil per markt en waarom combi's duurder zijn.")

ODDS = "/nieuws/odds-uitgelegd-quotering-lezen"
VALUE = "/nieuws/wat-is-de-wedstrategie-value-betting"
ARB = "/nieuws/wat-is-arbitrage-wedden-de-kunst-van-de-risicovrije-winst"
ACCA = "/nieuws/uitleg-wedstrategie-accumulator-weddenschappen"
BUILDER = "/nieuws/wat-is-een-bet-builder"
COMBIBOOST = "/nieuws/wat-is-een-combi-boost"
SUPERBOOST = "/nieuws/wat-is-een-superboost-of-superodd"
VERGELIJK = "/odds-vergelijken-bij-alle-bookmakers-beste-odds-vandaag"
KSB = "/nieuws/kansspelbelasting-gokwinst-belasting"
LEGAAL = "/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland"
BEWUST = "/speel-bewust/verantwoord-wedden"
OU = "/nieuws/over-under-uitleg-over-2-5-goals"
BTTS = "/nieuws/beide-teams-scoren-btts-betekenis"
DM = "/nieuws/doelpuntenmaker-wedden-regels"
BM711 = '<a href="/bookmakers/711">711</a>'
GELEZEN = "10 november 2026 om 14:34 uur"


def q(x):
    return f"{x:.2f}".replace(".", ",")


def pct(x, d=1):
    return f"{100 * x:.{d}f}%".replace(".", ",")


def eur(x):
    return f"€{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def som(odds):
    return sum(1 / o for o in odds)


# ---- 1. zo bouwt een bookmaker de marge in (fictief) ----
SCHAT = [0.40, 0.25, 0.35]                    # eigen inschatting bookmaker: thuis / gelijk / uit
OPSLAG = 1.04
EERLIJK_IN = [1 / p for p in SCHAT]
MET_MARGE = [1 / (p * OPSLAG) for p in SCHAT]
assert [q(o) for o in EERLIJK_IN] == ["2,50", "4,00", "2,86"]
assert [q(o) for o in MET_MARGE] == ["2,40", "3,85", "2,75"]
assert pct(som(MET_MARGE)) == "104,0%"

# muntworp: 2,00/2,00 eerlijk, 1,90/1,90 aangeboden; €1.000 per kant
assert pct(som([1.90, 1.90])) == "105,3%" and pct(1 / som([1.90, 1.90])) == "95,0%"
assert eur(2000 - 1000 * 1.90) == "€100,00" and pct(100 / 2000) == "5,0%"

# ---- 2. echte odds 711, Eredivisie 21/22-11-2026 (gelezen 10-11-2026 14:34) ----
ELF = [  # (wedstrijd, aftrap NL-tijd, 1, X, 2, lijn over/onder, over, onder)
    ("NEC - PSV", "za 21-11, 16:30", 4.30, 4.60, 1.71, 3.5, 1.74, 2.06),
    ("FC Utrecht - Cambuur", "za 21-11, 18:45", 2.00, 3.95, 3.55, 3.5, 2.18, 1.66),
    ("Feyenoord - Excelsior", "za 21-11, 18:45", 1.19, 8.00, 14.00, 3.5, 1.73, 2.06),
    ("FC Groningen - sc Heerenveen", "za 21-11, 21:00", 2.45, 4.00, 2.65, 3.5, 1.96, 1.81),
    ("Telstar - PEC Zwolle", "za 21-11, 21:00", 2.08, 3.85, 3.40, 3.5, 2.35, 1.57),
    ("FC Twente - Willem II", "zo 22-11, 12:15", 1.09, 12.50, 31.00, 4.5, 2.38, 1.55),
    ("Ajax - ADO Den Haag", "zo 22-11, 14:30", 1.19, 8.50, 15.00, 3.5, 1.66, 2.18),
    ("Sparta - AZ", "zo 22-11, 14:30", 4.60, 4.40, 1.71, 3.5, 2.10, 1.71),
    ("Go Ahead Eagles - Fortuna Sittard", "zo 22-11, 16:45", 1.67, 4.40, 4.90, 3.5, 2.12, 1.68),
]
G = ELF[3]
G1X2 = G[2:5]
GSOM = som(G1X2)
assert [pct(1 / o) for o in G1X2] == ["40,8%", "25,0%", "37,7%"]
assert pct(GSOM, 2) == "103,55%" and pct(GSOM - 1) == "3,6%" and pct(1 / GSOM) == "96,6%" and pct(1 - 1 / GSOM) == "3,4%"
RIJEN_G = [(f"<strong>{u}</strong>", q(o), pct(1 / o)) for u, o in zip(("1 (FC Groningen)", "X (gelijk)", "2 (sc Heerenveen)"), G1X2)]
RIJEN_G.append(("<strong>Totaal (overround)</strong>", "", f"<strong>{pct(GSOM)}</strong>"))

# tweeweg: over/onder 3,5 bij Groningen - Heerenveen
OV, ON = G[6], G[7]
assert pct(som([OV, ON])) == "106,3%" and pct(OV * ON / (OV + ON)) == "94,1%"
assert abs(OV * ON / (OV + ON) - 1 / som([OV, ON])) < 1e-12

MARGES_1X2 = [som(r[2:5]) - 1 for r in ELF]
MARGES_OU = [som(r[6:8]) - 1 for r in ELF]
assert (pct(min(MARGES_1X2)), pct(max(MARGES_1X2))) == ("2,5%", "3,7%")
assert (pct(min(MARGES_OU)), pct(max(MARGES_OU))) == ("6,0%", "6,7%")
RIJEN_ELF = [(f"<strong>{w}</strong>", t, " / ".join(q(o) for o in r[2:5]), pct(m1), pct(1 / (1 + m1)), pct(m2))
             for (w, t, *_), r, m1, m2 in zip(ELF, ELF, MARGES_1X2, MARGES_OU)]

# ---- 3. marge per markt, FC Groningen - sc Heerenveen ----
MARKTEN = [  # (markt, odds van alle uitkomsten, link)
    ("1X2 (uitslag na 90 minuten)", [2.45, 4.00, 2.65], None),
    ("Over/onder 3,5 doelpunten", [1.96, 1.81], OU),
    ("Beide teams scoren (ja/nee)", [1.34, 3.00], BTTS),
    ("Draw no bet (geld terug bij gelijkspel)", [1.76, 1.91], None),
    ("Ruststand (1X2 na 45 minuten)", [2.75, 2.55, 2.95], None),
    ("Totaal schoten op doel over/onder 10,5", [1.98, 1.68], None),
]
CS = [11.0, 7.5, 46.0, 20.0, 21.0, 61.0, 51.0, 11.0, 11.5, 21.0, 31.0, 21.0, 67.0, 35.0, 11.5, 56.0, 36.0, 46.0, 11.0,
      31.0, 10.5, 67.0, 10.5, 11.0, 91.0, 8.0, 29.0, 16.0, 15.0, 46.0, 7.0, 18.0, 16.0, 8.0]   # 34 open uitslagen
EERSTE_DM = [6.10, 6.75, 6.10, 26.0, 11.0, 6.75, 13.0, 12.5, 29.0, 25.0, 20.0, 8.0, 7.5, 7.5, 26.0, 5.8, 14.0, 11.5, 26.0,
             23.0, 5.8, 11.5, 14.0, 25.0, 25.0]   # 25 spelers, '1e Doelpuntenmaker'
assert len(CS) == 34 and len(EERSTE_DM) == 25
SOMMEN = [som(o) for _, o, _ in MARKTEN]
assert [pct(s - 1) for s in SOMMEN] == ["3,6%", "6,3%", "8,0%", "9,2%", "9,5%", "10,0%"]
assert pct(som(CS), 0) == "201%" and pct(som(EERSTE_DM), 0) == "229%"
RIJEN_MARKT = [(f'<strong><a href="{l}">{n}</a></strong>' if l else f"<strong>{n}</strong>", " / ".join(q(x) for x in o),
                pct(s), pct(s - 1), pct(1 / s)) for (n, o, l), s in zip(MARKTEN, SOMMEN)]
RIJEN_MARKT.append(("<strong>Correcte score</strong> (34 uitslagen)", "7,00 tot 91,00", pct(som(CS), 0), "zie tekst", "zie tekst"))

# ---- 4. combi's: uitbetaling vermenigvuldigt ----
COMBI = [ELF[2], ELF[6], ELF[5]]   # Feyenoord, Ajax, Twente
C_ODD = COMBI[0][2] * COMBI[1][2] * COMBI[2][2]
C_UIT = 1.0
for r in COMBI:
    C_UIT /= som(r[2:5])
assert q(C_ODD) == "1,54" and [pct(1 / som(r[2:5])) for r in COMBI] == ["96,5%", "97,6%", "97,1%"]
assert pct(C_UIT) == "91,4%" and pct(1 - C_UIT) == "8,6%"
BENEN = [1, 2, 3, 5, 8, 10]
M_LAAG, M_HOOG = 0.035, 0.08
RIJEN_COMBI = [(f"<strong>{n}</strong>", pct((1 / (1 + M_LAAG)) ** n), pct((1 / (1 + M_HOOG)) ** n)) for n in BENEN]
assert [r[1] for r in RIJEN_COMBI] == ["96,6%", "93,4%", "90,2%", "84,2%", "75,9%", "70,9%"]
assert [r[2] for r in RIJEN_COMBI] == ["92,6%", "85,7%", "79,4%", "68,1%", "54,0%", "46,3%"]

# ---- 5. bookmakers vergelijken: 711 vs fictieve bookmaker B ----
B = [2.50, 3.80, 2.70]
BEST = [max(a, b) for a, b in zip(G1X2, B)]
assert pct(som(B), 2) == "103,35%" and pct(som(B) - 1) == "3,4%"
assert BEST == [2.50, 4.00, 2.70] and pct(som(BEST)) == "102,0%"
RIJEN_VERGELIJK = [("<strong>711</strong> (echt)", *(q(o) for o in G1X2), pct(GSOM - 1)),
                   ("<strong>Bookmaker B</strong> (fictief)", *(q(o) for o in B), pct(som(B) - 1)),
                   ("<strong>Beste odd per uitkomst</strong>", *(f"<strong>{q(o)}</strong>" for o in BEST), pct(som(BEST) - 1))]

# ---- 6. wat kost de marge je: 100 weddenschappen van €10 (fictief, willekeurige keuzes) ----
INZET, AANTAL = 10, 100
KOST_1X2 = INZET * AANTAL * (1 - 1 / GSOM)
KOST_5 = INZET * AANTAL * (1 - 0.842)
assert eur(KOST_1X2) == "€34,30" and eur(INZET * AANTAL) == "€1.000,00" and eur(KOST_5) == "€158,00"

OG_KOP = "Wat is de <span>marge</span> van een bookmaker?"
OG_EYEBROW = "Overround en uitbetaling"
OG_CHIPS = ["Met echte odds", "Combi's stapelen marge"]
OG_MOTIEF = "tabel"
OG_DATA = [f"1X2 · {pct(SOMMEN[0] - 1)}", f"Over/onder · {pct(SOMMEN[1] - 1)}", f"Beide teams scoren · {pct(SOMMEN[2] - 1)}",
           f"Combi van 5 · {pct(0.842, 0)} terug"]
assert OG_DATA == ["1X2 · 3,6%", "Over/onder · 6,3%", "Beide teams scoren · 8,0%", "Combi van 5 · 84% terug"]

content = f"""<p><strong>De marge van een bookmaker is het stukje dat hij in de odds inbouwt, zodat hij op lange termijn verdient, wie er ook wint. Je berekent hem door van elke uitkomst 1 gedeeld door de odd op te tellen: alles boven de 100% is de marge, ook wel overround genoemd. 1 gedeeld door dat totaal is het uitbetalingspercentage: het deel van alle inzetten dat gemiddeld terugvloeit naar de wedders.</strong></p>
<p>Een voorbeeld met echte odds: bij {BM711} stond FC Groningen - sc Heerenveen op {q(G1X2[0])}, {q(G1X2[1])} en {q(G1X2[2])}. Dat telt op tot {pct(GSOM)}, een marge van {pct(GSOM - 1)} en een uitbetaling van {pct(1 / GSOM)}. Hieronder lees je hoe die marge in de odds komt, hoe je hem voor elke markt uitrekent, waarom hij bij spelersmarkten en combinaties veel hoger is en hoe je bookmakers vergelijkt. Ken je de basis van odds nog niet, lees dan eerst <a href="{ODDS}">odds uitgelegd</a>.</p>
<h3><strong>Hoe bouwt een bookmaker de marge in de odds?</strong></h3>
<p>Een bookmaker schat eerst zelf de kansen in. Stel: {pct(SCHAT[0], 0)} thuiswinst, {pct(SCHAT[1], 0)} gelijkspel en {pct(SCHAT[2], 0)} uitwinst. De eerlijke odds zijn dan 1 gedeeld door die kansen: {q(EERLIJK_IN[0])}, {q(EERLIJK_IN[1])} en {q(EERLIJK_IN[2])}. Met die odds zou hij gemiddeld precies quitte spelen.</p>
<p>Daarom maakt hij elke kans iets groter, bijvoorbeeld {pct(OPSLAG - 1, 0)}. De odds worden dan {q(MET_MARGE[0])}, {q(MET_MARGE[1])} en {q(MET_MARGE[2])}. Samen tellen de kansen nu op tot {pct(som(MET_MARGE))}. <em>Deze kansen zijn fictief.</em></p>
<p>Het simpelste voorbeeld is een muntworp. Eerlijk is 2,00 op kop en 2,00 op munt. Een bookmaker biedt 1,90 op allebei. Zet iemand {eur(1000)} op kop en iemand anders {eur(1000)} op munt, dan betaalt hij één kant {eur(1000 * 1.90)} uit en houdt hij {eur(2000 - 1900)} over, wat er ook valt. Dat is {pct(100 / 2000)} van alle inzetten.</p>
<h3><strong>Hoe bereken je de overround en het uitbetalingspercentage?</strong></h3>
<ol><li>Reken elke odd om naar een kans: 1 ÷ odd.</li><li>Tel de kansen van alle uitkomsten van de markt op. Dat is de overround (ook wel 'boek' genoemd).</li><li>Marge = overround − 100%.</li><li>Uitbetalingspercentage = 1 ÷ overround.</li></ol>
<p>Voor de 1X2-markt van FC Groningen - sc Heerenveen ziet dat er zo uit (odds van 711, gelezen op {GELEZEN}, aftrap zaterdag 21 november om 21:00 uur):</p>
{tabel(["Uitkomst", "Odd", "Kans (1 ÷ odd)"], RIJEN_G)}
<p>De marge is {pct(GSOM - 1)} en de uitbetaling {pct(1 / GSOM)}. Let op: je ziet de marge op twee manieren. {pct(GSOM - 1)} is het deel boven de 100%. Kijk je naar wat de bookmaker van elke ingezette euro houdt, dan is dat 100% − {pct(1 / GSOM)} = {pct(1 - 1 / GSOM)}. Beide getallen kloppen, ze rekenen alleen vanaf een ander startpunt. Vergelijk dus altijd hetzelfde getal.</p>
<p><strong>Markt met twee uitkomsten?</strong> Dan kan het nog korter: uitbetaling = (odd A × odd B) ÷ (odd A + odd B). Over 3,5 doelpunten stond in dezelfde wedstrijd op {q(OV)}, onder op {q(ON)}. Dat geeft ({q(OV)} × {q(ON)}) ÷ ({q(OV)} + {q(ON)}) = {pct(OV * ON / (OV + ON))} uitbetaling, een overround van {pct(som([OV, ON]))}.</p>
<h3><strong>Hoe hoog is de marge in de Eredivisie?</strong></h3>
<p>We hebben de odds van alle negen duels van de speelronde van 21 en 22 november bij 711 op dezelfde manier doorgerekend:</p>
{tabel(["Wedstrijd", "Aftrap", "Odds 1 / X / 2", "Marge 1X2", "Uitbetaling 1X2", "Marge over/onder"], RIJEN_ELF)}
<p>Op de uitslag schommelt de marge tussen {pct(min(MARGES_1X2))} en {pct(max(MARGES_1X2))}, op over/onder tussen {pct(min(MARGES_OU))} en {pct(max(MARGES_OU))}. Bij FC Twente - Willem II gaat over/onder over 4,5 doelpunten, bij de rest over 3,5. Dit is een momentopname: odds veranderen tot de aftrap, en daarmee ook de marge.</p>"""

content2 = f"""<h3><strong>Waarom verschilt de marge per markt?</strong></h3>
<p>Dezelfde bookmaker rekent op dezelfde wedstrijd niet overal dezelfde marge. Zo zag het eruit bij FC Groningen - sc Heerenveen op {GELEZEN}:</p>
{tabel(["Markt", "Odds", "Overround", "Marge", "Uitbetaling"], RIJEN_MARKT)}
<p>Hoe verder je van de hoofdmarkt afgaat, hoe hoger de marge. Daar zijn drie redenen voor:</p>
<ul><li><strong>Concurrentie.</strong> Op de uitslag vergelijkt iedereen de odds. Een dure 1X2 valt direct op, een dure ruststand veel minder.</li><li><strong>Onzekerheid.</strong> Schoten op doel of een eerste doelpuntenmaker zijn lastiger in te schatten dan de uitslag. Een bookmaker die minder zeker is van zijn prijs, bouwt meer buffer in.</li><li><strong>Veel uitkomsten.</strong> Bij een markt met tientallen uitkomsten krijgt elke uitkomst een stukje marge, en die stukjes stapelen op.</li></ul>
<p>Dat laatste geldt bij vrijwel elke bookmaker voor de <strong>correcte score</strong>: markten met veel uitkomsten zijn in de hele branche het duurst. In ons voorbeeld telden de kansen van de 34 aangeboden uitslagen op tot {pct(som(CS), 0)}, terwijl er maar één uitslag kan uitkomen. Bij de <a href="{DM}">eerste doelpuntenmaker</a> was het nog sterker: de 25 aangeboden spelers samen kwamen uit op {pct(som(EERSTE_DM), 0)}, terwijl er hooguit één speler de eerste goal maakt. Hoeveel de bookmaker hier precies inhoudt, kun je niet exact zeggen, maar wel dat het een veelvoud is van de marge op de uitslag.</p>
<p><strong>Spelersmarkten met maar één kant.</strong> Bij markten als 'scoort' of 'schoten van speler op doel' bood 711 alleen 'ja' of 'meer dan' aan. Zonder de andere kant kun je geen overround uitrekenen. Dat betekent niet dat er geen marge in zit, alleen dat je hem niet ziet. Wil je zo'n odd toch beoordelen, dan moet je zelf een kans inschatten.</p>
<h3><strong>Waarom vermenigvuldigt een combi de marge?</strong></h3>
<p>Bij een <a href="{ACCA}">combinatieweddenschap</a> worden de odds vermenigvuldigd. Daarmee vermenigvuldig je ook de uitbetalingspercentages. Een voorbeeld met drie favorieten van dezelfde speelronde, odds van 711:</p>
<ul><li>Feyenoord tegen Excelsior: {q(COMBI[0][2])}, uitbetaling van die markt {pct(1 / som(COMBI[0][2:5]))}</li><li>Ajax tegen ADO Den Haag: {q(COMBI[1][2])}, uitbetaling {pct(1 / som(COMBI[1][2:5]))}</li><li>FC Twente tegen Willem II: {q(COMBI[2][2])}, uitbetaling {pct(1 / som(COMBI[2][2:5]))}</li></ul>
<p>De combi-odd is {q(COMBI[0][2])} × {q(COMBI[1][2])} × {q(COMBI[2][2])} = {q(C_ODD)}. De uitbetaling is {pct(1 / som(COMBI[0][2:5]))} × {pct(1 / som(COMBI[1][2:5]))} × {pct(1 / som(COMBI[2][2:5]))} = {pct(C_UIT)}. Op losse duels houdt de bookmaker zo'n 3 cent per euro, op deze combi {pct(1 - C_UIT)}. Dit gaat ervan uit dat de duels los van elkaar staan en dat de marge evenredig over de uitkomsten is verdeeld. Zo loopt het op bij meer selecties:</p>
{tabel(["Aantal selecties", f"Uitbetaling bij {pct(M_LAAG)} marge per selectie", f"Uitbetaling bij {pct(M_HOOG, 0)} marge per selectie"], RIJEN_COMBI)}
<p>Een combi van vijf uitslagen met een gewone 1X2-marge betaalt gemiddeld nog maar {RIJEN_COMBI[3][1]} van de inzet terug. Neem je markten met een hogere marge, zoals beide teams scoren, dan zakt dat bij acht selecties naar {RIJEN_COMBI[4][2]}. Een <a href="{COMBIBOOST}">combi boost</a> verhoogt de winst van een combi en compenseert zo een deel van die opgestapelde marge. Bij een <a href="{BUILDER}">bet builder</a> combineer je selecties uit één wedstrijd. Die hangen met elkaar samen, dus de bookmaker bepaalt zelf de prijs en de marge daarin kun je niet narekenen.</p>"""

content3 = f"""<h3><strong>Hoe vergelijk je bookmakers op marge?</strong></h3>
<p>Vergelijk altijd dezelfde wedstrijd, dezelfde markt en hetzelfde moment. Een marge op de uitslag van een topduel zegt weinig over de marge op schoten op doel in de Keuken Kampioen Divisie. Kijk daarna niet alleen naar de marge per bookmaker, maar vooral naar de odd per uitkomst:</p>
{tabel(["Bookmaker", "1", "X", "2", "Marge"], RIJEN_VERGELIJK)}
<p>Bookmaker B rekent hier een iets lagere marge ({pct(som(B) - 1)}), maar biedt op het gelijkspel toch minder dan 711. Wie per uitkomst de hoogste odd pakt, speelt tegen een marge van maar {pct(som(BEST) - 1)}. Zakt het totaal van de beste odds onder de 100%, dan kun je op alle uitkomsten inzetten en altijd winst maken. Dat heet <a href="{ARB}">arbitrage</a>, al komt het zelden voor en verdwijnt het meestal snel. Met onze <a href="{VERGELIJK}">odds vergelijker</a> zie je per wedstrijd de hoogste odd bij legale bookmakers. Ook een <a href="{SUPERBOOST}">superboost</a> kan een odd tijdelijk boven de normale prijs tillen.</p>
<h3><strong>Wat kost de marge jou op lange termijn?</strong></h3>
<p>Stel dat je {AANTAL} weddenschappen van {eur(INZET)} plaatst op uitslagen met een uitbetaling van {pct(1 / GSOM)}, zonder dat je beter voorspelt dan de bookmaker. Dan verwacht je van je {eur(INZET * AANTAL)} gemiddeld {eur(INZET * AANTAL - KOST_1X2)} terug te krijgen: {eur(KOST_1X2)} verlies. Speel je dezelfde {AANTAL} keer combi's van vijf, dan is dat ongeveer {eur(KOST_5)}. <em>Dit zijn gemiddelden, een echte reeks kan flink afwijken.</em></p>
<p>De marge is dus de drempel die je moet overwinnen. Dat lukt alleen als jouw inschatting van de kans beter is dan die van de bookmaker en je die kans ook terugziet in een te hoge odd. Dat is het idee achter <a href="{VALUE}">value betting</a>. Een lage marge maakt die drempel lager, maar is geen garantie op winst.</p>
<h3><strong>Wat gebeurt er in Nederland met de marge?</strong></h3>
<p>Wat een bookmaker overhoudt, inzetten min uitbetaalde prijzen, heet het bruto spelresultaat. Een legale Nederlandse aanbieder betaalt daarover kansspelbelasting: sinds 1 januari 2026 is dat 37,8%. Jij betaalt als speler bij een bookmaker met een Nederlandse vergunning zelf geen belasting over je winst. Meer daarover lees je in ons artikel over <a href="{KSB}">kansspelbelasting</a>. Speel alleen bij een <a href="{LEGAAL}">legale bookmaker</a> en zet in wat je kunt missen. Tips daarvoor vind je bij <a href="{BEWUST}">verantwoord wedden</a>, en meer uitleg in de <a href="/wedgids">wedgids</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wat is de marge van een bookmaker?</strong><br>Het deel dat de bookmaker in de odds inbouwt om op lange termijn te verdienen. Je ziet het doordat de kansen van alle uitkomsten samen boven de 100% uitkomen. Alles boven de 100% is de marge.</p>
<p><strong>Hoe bereken je het uitbetalingspercentage?</strong><br>Tel van elke uitkomst 1 ÷ odd op en deel 1 door dat totaal. Bij {q(G1X2[0])}, {q(G1X2[1])} en {q(G1X2[2])} is het totaal {pct(GSOM)} en de uitbetaling {pct(1 / GSOM)}.</p>
<p><strong>Wat is het verschil tussen overround en marge?</strong><br>De overround is het totaal van de kansen, bijvoorbeeld {pct(GSOM)}. De marge is wat boven de 100% uitkomt: {pct(GSOM - 1)}. Soms wordt de marge ook gegeven als het deel van de inzet dat de bookmaker houdt, hier {pct(1 - 1 / GSOM)}.</p>
<p><strong>Waarom is de marge op een combi hoger?</strong><br>Omdat de uitbetalingspercentages van de losse selecties met elkaar worden vermenigvuldigd. Drie selecties met elk {pct(1 / (1 + M_LAAG))} uitbetaling geven samen {RIJEN_COMBI[2][1]}.</p>
<p><strong>Welke markt heeft de laagste marge?</strong><br>Meestal de hoofdmarkt: de uitslag van een grote wedstrijd. In onze meting zat de uitslag rond de 3%, over/onder rond de 6% en markten met veel uitkomsten, zoals de correcte score, vele malen hoger. Dat patroon zie je bij alle bookmakers.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    html = content + content2 + content3
    assert re.search(r"<(ul|ol|/li)>\s+<", html) is None
    assert "/kennisbank/" not in html and "<h2" not in html and "<h4" not in html and "/go/" not in html
    assert html.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert content.startswith("<p><strong>")
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert len(OG_CHIPS) == 2 and len(OG_DATA) == 4 and html.count("<table") >= 4
    for link in (ODDS, VALUE, ARB, ACCA, BUILDER, COMBIBOOST, SUPERBOOST, VERGELIJK, KSB, LEGAAL, BEWUST, OU, BTTS, DM,
                 "/bookmakers/711", "/wedgids"):
        assert f'href="{link}"' in html, link
    assert not re.search(r'href="(?!/)', html), "alleen relatieve links"
    assert all(h.startswith("<strong>") for h in re.findall(r"<h3>(.*?)</h3>", html))
    faq = content3.split("Veelgestelde vragen")[1]
    assert 4 <= faq.count("<p><strong>") <= 6
    tekst = re.sub(r"<[^>]+>", " ", html)
    woorden = len(tekst.split())
    assert 1200 <= woorden <= 2200, woorden
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", woorden, "woorden |",
          [len(re.sub(r"<[^>]+>", " ", c).split()) for c in (content, content2, content3)])
    # ---- --live: NIET zelf draaien; alleen na akkoord van Jasper (bij voorkeur via wg_publiceer.py bookmaker-marge --live,
    #      dat ook de deelkaart en wedgids-categorie regelt) ----
    if "--live" in sys.argv:
        fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
              "samenvatting": SAMENVATTING, "rubriek": RUBRIEK, "wedgids": True,
              "publicatiedatum": datetime.now(timezone.utc).isoformat()}
        print("item:", WF.create_live(fd), "https://www.bet-experts.nl/nieuws/" + SLUG)
