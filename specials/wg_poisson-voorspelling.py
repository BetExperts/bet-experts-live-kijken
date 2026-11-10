# -*- coding: utf-8 -*-
"""NIEUW wedgids-artikel (Nieuws, nog geen item): voetbaluitslag voorspellen met het Poisson-model.
Slug voetbaluitslag-voorspellen-met-poisson (gaf HTTP 404 op 10-11-2026 met curl, dus vrij).
Rubriek Speluitleg, wedgids-categorie 'Wedstrategieën'. Onderwerp: Engelstalige analysesite (alleen het onderwerp).
Zoekwoorden: 'voetbaluitslag voorspellen' / 'poisson voetbal' (hoofd), 'poisson verdeling voetbal', 'uitslag voorspellen
excel', 'poisson excel voetbal', 'aanvalskracht verdedigingskracht', 'kans op over 2,5 berekenen', 'dixon coles',
'voorspellingsmodel voetbal', 'eerlijke odds berekenen'.

Feiten (bron + datum):
- STAND EREDIVISIE 2026/27: eigen API https://www.bet-experts.nl/api/standings/eredivisie (API-Football league 88,
  season 2026), opgehaald 10-11-2026 15:25 CET (last-modified 10-11-2026 12:25 UTC, 'update' 2026-11-10). Alle 18 clubs
  12 duels gespeeld: 420 doelpunten in 108 wedstrijden (som voor = som tegen = 420); thuis 200, uit 220.
  Sparta Rotterdam 21 voor / 29 tegen; AZ Alkmaar 24 voor / 16 tegen. Andere clubs: zie STAND hieronder (alleen voor de
  vergelijkingstabel). Draws dit seizoen: 30 van de 108 duels.
- STAND EREDIVISIE 2025/26 (eindstand): https://www.bet-experts.nl/api/standings/eredivisie/2025 (season 2025, 'update'
  2026-05-27), opgehaald 10-11-2026: 306 duels, thuis 551 doelpunten, uit 421 (som 972), 80 gelijke spelen.
- ODDS 711 (publieke Kambi-feed sevelevnl), gelezen 10-11-2026 15:27 CET: Sparta Rotterdam - AZ (zo 22-11-2026 14:30 uur NL,
  event 1027976488): 1X2 4,60 / 4,40 / 1,71; over/onder 2,5 1,43 / 2,75; beide teams scoren ja 1,45 / nee 2,55.
  1X2 van de andere 8 duels van speelronde 13 (listView eredivisie, 15:25): zie MARKT hieronder.
- Excel: Microsoft-ondersteuning (support.microsoft.com/nl-nl/office/poisson-verd-functie-8fe148ff-39a2-46cb-abf3-7772695d9636,
  gelezen 10-11-2026): 'POISSON.VERD(x;gemiddelde;cumulatief)'; ONWAAR = kans op precies x, WAAR = ten hoogste x.
  SOMPRODUCT = Nederlandse naam van SUMPRODUCT. Engelse Excel: POISSON.DIST.
- Literatuur: M.J. Maher (1982), 'Modelling association football scores', Statistica Neerlandica 36(3), 109-118
  (aanvals- en verdedigingsparameters per team, Poisson); M.J. Dixon & S.G. Coles (1997), 'Modelling association football
  scores and inefficiencies in the football betting market', JRSS Series C (Applied Statistics) 46(2), 265-280
  (correctie voor lage scores + tijdsweging). Gecontroleerd via econpapers.repec.org en research-information.bris.ac.uk
  op 10-11-2026. De rho-waarde -0,10 in het voorbeeld is ILLUSTRATIEF (niet uit het artikel; staat zo in de tekst).
- 'Poisson onderschat gelijke spelen' is hier met eigen data onderbouwd: in alle 9 duels van speelronde 13 ligt de
  modelkans op gelijk lager dan de 711-kans zonder marge; Eredivisie 2025/26 26,1% gelijk vs 23,0% volgens Poisson met
  competitiegemiddelden; 2026/27 tot nu 27,8% vs 20,9%. (Een gemiddelde-lambda-berekening overschat het aantal gelijke
  spelen eerder dan dat ze het onderschat, dus het verschil is eerder groter.)
Alle getallen hieronder berekend en ge-assert.

Bewust weggelaten:
- Geen 'tip' op Sparta - AZ: de afwijking model vs markt wordt in de tekst juist als waarschuwing gebruikt.
- Geen bivariate Poisson-formules en geen schattingsmethode (maximum likelihood) voor Dixon-Coles: te technisch.
- Geen claims over hoe goed bookmakermodellen zijn of welke data ze gebruiken (niet te controleren).
- Geen xG-cijfers per club (geen openbare bron die we mogen gebruiken voor alle clubs) -> xG alleen als idee.
- Geen bron van het onderwerp genoemd.
Interne links gecontroleerd met curl op 10-11-2026: allemaal HTTP 200 (zie LINKS / asserts). Geen INFOGRAPHIC.
  ../superodd-agent/.venv/bin/python specials/wg_publiceer.py poisson-voorspelling   (dry run)"""
import os, sys, re
from math import exp, factorial
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

ITEM_ID = None   # nieuw artikel
SLUG = "voetbaluitslag-voorspellen-met-poisson"
RUBRIEK = "6502b66cd9992658b4037cf5"   # Speluitleg
WEDGIDS_CAT = "Wedstrategieën"
TITEL = "Voetbaluitslag voorspellen met Poisson: zo werkt het"
SAMENVATTING = ("Voetbaluitslag voorspellen met Poisson: zo bereken je verwachte goals, een scorematrix, 1X2, over 2,5 en "
                "BTTS. Met Excel-recept en eerlijke grenzen.")

OG_KOP = "Uitslag voorspellen met <span>Poisson</span>"
OG_EYEBROW = "Rekenmodel voor voetbal"
OG_CHIPS = ["Met scorematrix", "Excel: POISSON.VERD"]
OG_MOTIEF = "tabel"

XG = "/nieuws/wat-is-xg-expected-goals"
KANS = "/nieuws/kans-berekenen-uit-odds-impliciete-kans"
EV = "/nieuws/wat-is-expected-value-ev-bij-wedden"
CLV = "/nieuws/wat-is-closing-line-value-clv"
VALUE = "/nieuws/wat-is-de-wedstrategie-value-betting"
OU = "/nieuws/over-under-uitleg-over-2-5-goals"
BTTS = "/nieuws/beide-teams-scoren-btts-betekenis"
BANK = "/nieuws/bankroll-management-wedden"
LIMIET = "/nieuws/netto-stortingslimiet"
LINKS = (XG, KANS, EV, CLV, VALUE, OU, BTTS, BANK, LIMIET, "/speel-bewust/verantwoord-wedden", "/wedgids")


def k(x, n=2):
    return f"{x:.{n}f}".replace(".", ",")


def pct(x, n=1):
    return f"{100 * x:.{n}f}".replace(".", ",") + "%"


def P(lam, n):
    return exp(-lam) * lam ** n / factorial(n)


# ---- data: eigen API, 10-11-2026 ----
WEDSTR = 12
STAND = {"Sparta Rotterdam": (21, 29), "AZ": (24, 16), "NEC": (20, 21), "PSV": (40, 15), "FC Utrecht": (21, 34),
         "Cambuur": (25, 27), "Feyenoord": (36, 17), "Excelsior": (16, 29), "FC Groningen": (29, 28), "Heerenveen": (24, 16),
         "Telstar": (18, 25), "PEC Zwolle": (13, 24), "FC Twente": (30, 12), "Willem II": (11, 40), "Ajax": (32, 15),
         "ADO Den Haag": (16, 25), "Go Ahead Eagles": (24, 27), "Fortuna Sittard": (20, 20)}
assert len(STAND) == 18 and sum(v for v, _ in STAND.values()) == 420 == sum(t for _, t in STAND.values())
DUELS_NU, THUIS_NU, UIT_NU, GELIJK_NU = 108, 200, 220, 30
DUELS_VJ, THUIS_VJ, UIT_VJ, GELIJK_VJ = 306, 551, 421, 80
G = 420 / (2 * DUELS_NU)                      # doelpunten per team per wedstrijd, dit seizoen
GEM_VJ = (THUIS_VJ + UIT_VJ) / (2 * DUELS_VJ)
THUISF, UITF = (THUIS_VJ / DUELS_VJ) / GEM_VJ, (UIT_VJ / DUELS_VJ) / GEM_VJ
assert (k(G, 3), k(420 / DUELS_NU), k(THUIS_NU / DUELS_NU), k(UIT_NU / DUELS_NU)) == ("1,944", "3,89", "1,85", "2,04")
assert (k(THUIS_VJ / DUELS_VJ), k(UIT_VJ / DUELS_VJ), k(THUISF, 3), k(UITF, 3)) == ("1,80", "1,38", "1,134", "0,866")


def kracht(team):
    v, t = STAND[team]
    return v / WEDSTR / G, t / WEDSTR / G     # aanvalskracht, verdedigingszwakte (1 = gemiddeld)


def lambdas(thuis, uit):
    at, dt = kracht(thuis)
    au, du = kracht(uit)
    return at * du * G * THUISF, au * dt * G * UITF


def matrix(lt, lu, n=16):
    return [[P(lt, i) * P(lu, j) for j in range(n)] for i in range(n)]


def markten(M):
    n = len(M)
    p1 = sum(M[i][j] for i in range(n) for j in range(n) if i > j)
    px = sum(M[i][i] for i in range(n))
    p2 = sum(M[i][j] for i in range(n) for j in range(n) if i < j)
    o25 = sum(M[i][j] for i in range(n) for j in range(n) if i + j >= 3)
    btts = sum(M[i][j] for i in range(1, n) for j in range(1, n))
    return p1, px, p2, o25, btts


def eerlijk(odds):
    s = sum(1 / o for o in odds)
    return [(1 / o) / s for o in odds]


# ---- het voorbeeld: Sparta Rotterdam - AZ ----
AT, DT = kracht("Sparta Rotterdam")
AU, DU = kracht("AZ")
assert (k(AT), k(DT), k(AU), k(DU)) == ("0,90", "1,24", "1,03", "0,69")
LT, LU = lambdas("Sparta Rotterdam", "AZ")
assert (k(LT), k(LU)) == ("1,36", "2,15")
M = matrix(LT, LU)
P1, PX, P2, O25, BT = markten(M)
assert abs(P1 + PX + P2 - 1) < 1e-6 and abs(BT - (1 - P(LT, 0)) * (1 - P(LU, 0))) < 1e-6
assert (pct(P1), pct(PX), pct(P2), pct(O25), pct(BT)) == ("23,8%", "20,6%", "55,6%", "68,2%", "65,7%")
assert (k(1 / P1), k(1 / PX), k(1 / P2), k(1 / O25), k(1 / BT)) == ("4,20", "4,85", "1,80", "1,47", "1,52")
M6 = [r[:6] for r in M[:6]]
DEKKING = sum(map(sum, M6))
assert pct(DEKKING) == "97,5%"
TOP = sorted(((M[i][j], f"{i}-{j}") for i in range(6) for j in range(6)), reverse=True)[:3]
assert [s for _, s in TOP] == ["1-2", "1-1", "0-2"] and [pct(p) for p, _ in TOP] == ["9,4%", "8,7%", "6,9%"]
RIJEN_P = [(str(n), pct(P(LT, n)), pct(P(LU, n))) for n in range(6)]
assert pct(P(LT, 0)) == "25,7%" and pct(P(LU, 0)) == "11,6%"
RIJEN_M = [(f"<strong>Sparta {i}</strong>",) + tuple(
    (f"<strong>{pct(M[i][j])}</strong>" if (M[i][j], f"{i}-{j}") == TOP[0] else pct(M[i][j])) for j in range(6)) for i in range(6)]

# ---- markt (711) ----
ODDS_1X2, ODDS_OU, ODDS_BT = (4.60, 4.40, 1.71), (1.43, 2.75), (1.45, 2.55)
M1X2, MOU, MBT = eerlijk(ODDS_1X2), eerlijk(ODDS_OU), eerlijk(ODDS_BT)
assert [pct(p) for p in M1X2] == ["21,1%", "22,1%", "56,8%"] and (pct(MOU[0]), pct(MBT[0])) == ("65,8%", "63,8%")
RIJEN_VGL = [("Sparta wint", pct(P1), k(1 / P1), k(ODDS_1X2[0]), pct(M1X2[0])),
             ("Gelijkspel", pct(PX), k(1 / PX), k(ODDS_1X2[1]), pct(M1X2[1])),
             ("AZ wint", pct(P2), k(1 / P2), k(ODDS_1X2[2]), pct(M1X2[2])),
             ("Meer dan 2,5 doelpunten", pct(O25), k(1 / O25), k(ODDS_OU[0]), pct(MOU[0])),
             ("Beide teams scoren", pct(BT), k(1 / BT), k(ODDS_BT[0]), pct(MBT[0]))]
EV_SPARTA = P1 * ODDS_1X2[0] - 1
assert pct(EV_SPARTA, 0) == "10%"

# ---- gelijkspel: model vs markt, alle 9 duels van speelronde 13 ----
MARKT = [("NEC", "PSV", (4.30, 4.60, 1.71)), ("FC Utrecht", "Cambuur", (2.00, 3.95, 3.55)),
         ("Feyenoord", "Excelsior", (1.19, 8.00, 14.00)), ("FC Groningen", "Heerenveen", (2.45, 4.00, 2.65)),
         ("Telstar", "PEC Zwolle", (2.08, 3.85, 3.40)), ("FC Twente", "Willem II", (1.09, 12.50, 31.00)),
         ("Ajax", "ADO Den Haag", (1.19, 8.50, 15.00)), ("Sparta Rotterdam", "AZ", ODDS_1X2),
         ("Go Ahead Eagles", "Fortuna Sittard", (1.67, 4.40, 4.90))]
VGL_X = [(f"{t} – {u}", markten(matrix(*lambdas(t, u)))[1], eerlijk(o)[1]) for t, u, o in MARKT]
assert all(m < b for _, m, b in VGL_X)
RIJEN_X = [(w, pct(m), pct(b)) for w, m, b in VGL_X]
assert [pct(m) for _, m, _ in VGL_X] == ["17,0%", "18,3%", "5,8%", "20,7%", "23,5%", "2,2%", "9,9%", "20,6%", "21,7%"]
GX_VJ = sum(P(THUIS_VJ / DUELS_VJ, n) * P(UIT_VJ / DUELS_VJ, n) for n in range(15))
GX_NU = sum(P(THUIS_NU / DUELS_NU, n) * P(UIT_NU / DUELS_NU, n) for n in range(15))
assert (pct(GELIJK_VJ / DUELS_VJ), pct(GX_VJ), pct(GELIJK_NU / DUELS_NU), pct(GX_NU)) == ("26,1%", "23,0%", "27,8%", "20,9%")

# ---- Dixon-Coles ter illustratie: rho = -0,10 ----
RHO = -0.10
TAU = {(0, 0): 1 - LT * LU * RHO, (0, 1): 1 + LT * RHO, (1, 0): 1 + LU * RHO, (1, 1): 1 - RHO}
MDC = [[M[i][j] * TAU.get((i, j), 1) for j in range(len(M))] for i in range(len(M))]
assert abs(sum(map(sum, MDC)) - 1) < 1e-6
DC1, DCX, DC2, _, _ = markten(MDC)
assert (pct(DC1), pct(DCX), pct(DC2), k(1 / DCX)) == ("22,9%", "22,3%", "54,7%", "4,47")

OG_DATA = [f"Sparta · {k(LT)} verwachte goals", f"AZ · {k(LU)} verwachte goals", f"Meest waarschijnlijk · {TOP[0][1]}",
           f"Gelijkspel · {pct(PX, 0)} (markt {pct(M1X2[1], 0)})"]

content = f"""<p><strong>Met het Poisson-model voorspel je een voetbaluitslag door eerst per team het verwachte aantal doelpunten te berekenen, uit de aanvals- en verdedigingskracht ten opzichte van het competitiegemiddelde plus thuisvoordeel. De Poisson-verdeling zet dat getal om in de kans op 0, 1, 2 of meer goals. Combineer je beide teams in een scorematrix, dan heb je de kans op elke uitslag, op winst, gelijk en verlies, op over 2,5 en op beide teams scoren.</strong></p>
<p>Het is een van de oudste en eenvoudigste voetbalmodellen, en een goed begin om te begrijpen hoe odds tot stand komen. Hieronder rekenen we een echte Eredivisie-wedstrijd stap voor stap door, met een recept voor Excel. Daarna lees je eerlijk waar het model tekortschiet.</p>
<h3><strong>Wat is de Poisson-verdeling?</strong></h3>
<p>De Poisson-verdeling geeft de kans dat iets een bepaald aantal keer gebeurt, als het gemiddeld een vast aantal keer voorkomt en de gebeurtenissen los van elkaar staan. Doelpunten passen daar redelijk bij: ze zijn zeldzaam en kunnen op elk moment vallen. De formule:</p>
<p><strong>kans op precies k doelpunten = λ<sup>k</sup> × e<sup>−λ</sup> ÷ k!</strong></p>
<p>Hierin is λ (lambda) het verwachte aantal doelpunten, e is ongeveer 2,718 en k! betekent 1 × 2 × … × k (0! is 1). Je hoeft dat niet uit je hoofd te doen: Excel rekent het voor je uit. De statisticus M.J. Maher beschreef in 1982 al een voetbalmodel met een aanvals- en verdedigingswaarde per team, in het Nederlandse vakblad Statistica Neerlandica. Bijna elk voetbalmodel bouwt daarop voort.</p>
<h3><strong>Stap 1: wat is het competitiegemiddelde en het thuisvoordeel?</strong></h3>
<p>Ons voorbeeld is <strong>Sparta Rotterdam – AZ</strong> op zondag 22 november 2026. We gebruiken de Eredivisie-stand uit onze eigen data van 10 november 2026: alle clubs hebben 12 wedstrijden gespeeld en er vielen 420 doelpunten in 108 duels. Dat is {k(420 / DUELS_NU)} per wedstrijd, ofwel <strong>{k(G, 3)} per team per wedstrijd</strong>. Dat getal is ons ijkpunt.</p>
<p>Voor het thuisvoordeel is dit seizoen een te kleine steekproef: uitploegen scoorden tot nu toe zelfs vaker ({k(UIT_NU / DUELS_NU)} per duel) dan thuisploegen ({k(THUIS_NU / DUELS_NU)}). Dat is vrijwel zeker toeval. Daarom nemen we het hele vorige seizoen: in 2025/26 scoorden thuisploegen gemiddeld {k(THUIS_VJ / DUELS_VJ)} keer en uitploegen {k(UIT_VJ / DUELS_VJ)} keer per wedstrijd. Gedeeld door het gemiddelde per team geeft dat een <strong>thuisfactor van {k(THUISF, 3)}</strong> en een <strong>uitfactor van {k(UITF, 3)}</strong>.</p>
<h3><strong>Stap 2: hoe bereken je aanvals- en verdedigingskracht?</strong></h3>
<p>Deel de doelpunten per wedstrijd van een team door het competitiegemiddelde. Boven 1 is beter dan gemiddeld in de aanval; bij de verdediging betekent boven 1 dat een team méér tegengoals krijgt dan gemiddeld.</p>
{tabel(["Team", "Voor / tegen (12 duels)", "Aanvalskracht", "Verdedigingszwakte"], [
    ("Sparta Rotterdam", f"{STAND['Sparta Rotterdam'][0]} / {STAND['Sparta Rotterdam'][1]}", f"{STAND['Sparta Rotterdam'][0]} ÷ 12 ÷ {k(G, 3)} = {k(AT)}", f"{STAND['Sparta Rotterdam'][1]} ÷ 12 ÷ {k(G, 3)} = {k(DT)}"),
    ("AZ", f"{STAND['AZ'][0]} / {STAND['AZ'][1]}", f"{STAND['AZ'][0]} ÷ 12 ÷ {k(G, 3)} = {k(AU)}", f"{STAND['AZ'][1]} ÷ 12 ÷ {k(G, 3)} = {k(DU)}"),
])}
<p>Sparta scoort dus iets minder dan gemiddeld en krijgt er een kwart meer tegen. AZ scoort iets boven het gemiddelde en krijgt een derde minder tegen.</p>
<h3><strong>Stap 3: hoeveel doelpunten verwacht je per team?</strong></h3>
<p>Vermenigvuldig de aanvalskracht van het ene team met de verdedigingszwakte van het andere, met het competitiegemiddelde en met de thuis- of uitfactor:</p>
<ul><li><strong>Sparta (thuis):</strong> {k(AT)} × {k(DU)} × {k(G, 3)} × {k(THUISF, 3)} = <strong>{k(LT)} doelpunten</strong></li><li><strong>AZ (uit):</strong> {k(AU)} × {k(DT)} × {k(G, 3)} × {k(UITF, 3)} = <strong>{k(LU)} doelpunten</strong></li></ul>
<p>Met die twee lambda's bereken je per team de kans op elk aantal doelpunten:</p>
{tabel(["Doelpunten", f"Sparta (λ = {k(LT)})", f"AZ (λ = {k(LU)})"], RIJEN_P)}"""

content2 = f"""<h3><strong>Stap 4: hoe maak je een scorematrix?</strong></h3>
<p>Het model gaat ervan uit dat de doelpunten van beide teams los van elkaar vallen. De kans op een uitslag is dan de kans op het aantal goals van Sparta maal de kans op het aantal goals van AZ. Voor 1-2 is dat {pct(P(LT, 1))} × {pct(P(LU, 2))} = {pct(M[1][2])}. Doe je dat voor elke uitslag van 0-0 tot 5-5, dan krijg je deze matrix (rijen: goals Sparta, kolommen: goals AZ):</p>
{tabel(["", "AZ 0", "AZ 1", "AZ 2", "AZ 3", "AZ 4", "AZ 5"], RIJEN_M)}
<p>De meest waarschijnlijke uitslag is {TOP[0][1]} ({pct(TOP[0][0])}), gevolgd door {TOP[1][1]} ({pct(TOP[1][0])}) en {TOP[2][1]} ({pct(TOP[2][0])}). Let op hoe klein die kansen zijn: zelfs de meest waarschijnlijke uitslag komt nog geen één op de tien keer uit. Samen dekt de tabel {pct(DEKKING)} van alle mogelijkheden; de rest zijn uitslagen met zes of meer goals voor één team. Voor de berekeningen hieronder nemen we die ook mee.</p>
<h3><strong>Stap 5: hoe bereken je 1X2, over 2,5 en BTTS?</strong></h3>
<ul><li><strong>Thuiswinst:</strong> tel alle vakjes op waar Sparta meer goals heeft (onder de diagonaal).</li><li><strong>Gelijkspel:</strong> tel de diagonaal op: 0-0, 1-1, 2-2 enzovoort.</li><li><strong>Uitwinst:</strong> tel alle vakjes boven de diagonaal op.</li><li><strong>Meer dan 2,5 doelpunten:</strong> 1 min de vakjes met samen 0, 1 of 2 goals. Meer over deze markt lees je in <a href="{OU}">over/under uitgelegd</a>.</li><li><strong>Beide teams scoren:</strong> (1 − kans dat Sparta 0 scoort) × (1 − kans dat AZ 0 scoort) = (1 − {pct(P(LT, 0))}) × (1 − {pct(P(LU, 0))}). Zie ook <a href="{BTTS}">beide teams scoren</a>.</li></ul>
<p>De <strong>eerlijke odd</strong> is 1 gedeeld door de kans. Daarnaast zetten we de odds van 711 van 10 november 2026, met de marge eruit gehaald (zo doe je dat: <a href="{KANS}">kans berekenen uit odds</a>):</p>
{tabel(["Uitkomst", "Kans model", "Eerlijke odd model", "Odd 711", "Kans 711 zonder marge"], RIJEN_VGL)}
<p>Model en markt liggen dicht bij elkaar: beide zien AZ als duidelijke favoriet. Het grootste verschil zit bij Sparta en het gelijkspel. Volgens het model zou Sparta op {k(ODDS_1X2[0])} een verwacht rendement van ongeveer {pct(EV_SPARTA, 0)} hebben. Toch is dat géén tip. De waarschijnlijkste verklaring is dat het model iets mist, zoals je hieronder leest.</p>
<h3><strong>Zo bouw je het model in Excel</strong></h3>
<p>In de Nederlandse versie van Excel heet de functie <strong>POISSON.VERD</strong> (in het Engels POISSON.DIST). De opbouw is POISSON.VERD(x;gemiddelde;cumulatief). Met ONWAAR krijg je de kans op precies x doelpunten, met WAAR de kans op ten hoogste x.</p>
<ul><li><strong>Invoer:</strong> zet de lambda van de thuisploeg in J1 ({k(LT)}) en die van de uitploeg in J2 ({k(LU)}).</li><li><strong>Assen:</strong> zet 0 tot en met 5 in A2:A7 (goals thuis) en in B1:G1 (goals uit).</li><li><strong>Matrix:</strong> typ in B2 =POISSON.VERD($A2;$J$1;ONWAAR)*POISSON.VERD(B$1;$J$2;ONWAAR) en trek de formule door tot G7.</li><li><strong>Thuiswinst:</strong> =SOMPRODUCT((A2:A7&gt;B1:G1)*B2:G7). Gelijk: verander &gt; in =, uitwinst: in &lt;.</li><li><strong>Meer dan 2,5:</strong> =1-SOMPRODUCT((A2:A7+B1:G1&lt;=2)*B2:G7)</li><li><strong>Beide teams scoren:</strong> =(1-POISSON.VERD(0;J1;ONWAAR))*(1-POISSON.VERD(0;J2;ONWAAR))</li><li><strong>Eerlijke odd:</strong> =1/kans</li></ul>
<p>Omdat dit raster stopt bij 5 goals, tellen de kansen samen op tot iets minder dan 100% (hier {pct(DEKKING)}). Wil je het preciezer, maak het raster dan 0 tot en met 10.</p>"""

content3 = f"""<h3><strong>Waar gaat het Poisson-model de mist in?</strong></h3>
<p><strong>1. Het onderschat gelijke spelen.</strong> Het basismodel behandelt de goals van beide teams als onafhankelijk. In het echt is dat niet zo: een ploeg die voorstaat, gaat vaak verdedigen, en bij een gelijke stand spelen beide teams anders dan bij 2-0. Gevolg: te weinig 0-0's en 1-1's. Dat zie je terug in onze eigen cijfers. In 2025/26 eindigde {pct(GELIJK_VJ / DUELS_VJ)} van de Eredivisieduels gelijk, terwijl een Poisson-model met de gemiddelden van dat seizoen op {pct(GX_VJ)} uitkomt. Ook in alle negen duels van de volgende speelronde geeft ons model een lagere kans op gelijk dan 711:</p>
{tabel(["Wedstrijd", "Gelijk volgens model", "Gelijk volgens 711 (zonder marge)"], RIJEN_X)}
<p><strong>2. De Dixon-Coles-correctie.</strong> De statistici Mark Dixon en Stuart Coles stelden in 1997 een aanpassing voor: een extra factor (rho) die de kansen op 0-0, 1-0, 0-1 en 1-1 corrigeert. Daarnaast lieten ze recente wedstrijden zwaarder meetellen dan oude. Met een rho van −0,10 (een waarde ter illustratie) stijgt de kans op gelijk bij Sparta – AZ van {pct(PX)} naar {pct(DCX)}, een eerlijke odd van {k(1 / DCX)}. Daarmee schuift het model al flink op richting de markt.</p>
<p><strong>3. Doelpunten zijn grillig, xG minder.</strong> Een paar afgeweken ballen of een gemiste penalty vertekenen de stand na 12 duels. Daarom gebruiken betere modellen <a href="{XG}">expected goals (xG)</a> in plaats van echte doelpunten, of een mix van beide. Het principe blijft hetzelfde: je vervangt alleen de doelpunten voor en tegen door xG voor en tegen.</p>
<p><strong>4. Kleine steekproeven.</strong> Twaalf wedstrijden is weinig. Dat zag je al bij het thuisvoordeel, dat dit seizoen omgekeerd lijkt. Bij uitersten wordt het model ook te extreem: FC Twente krijgt bijna niets tegen en Willem II heel veel, dus het model geeft Twente thuis bijna vijf verwachte goals en maar {RIJEN_X[5][1]} kans op gelijk, tegen {RIJEN_X[5][2]} bij de bookmaker. Combineer daarom een paar seizoenen, laat oude duels minder zwaar wegen en trek extreme waarden richting het gemiddelde.</p>
<p><strong>5. Het model kent het nieuws niet.</strong> Blessures, schorsingen, een nieuwe trainer, rotatie voor een Europese wedstrijd of de stand in de competitie zitten er niet in. Bookmakers verwerken dat wel. Ook het verschil tussen thuis- en uitvorm per club en de sterkte van de tegenstanders tot nu toe laat dit eenvoudige model buiten beschouwing.</p>
<h3><strong>Kun je met een Poisson-model winst maken?</strong></h3>
<p>Verwacht het niet. Bookmakers werken met veel uitgebreidere modellen en verwerken nieuws en geld in hun prijzen. Een verschil tussen jouw model en de odds betekent daarom vaker dat jouw model iets mist dan dat de bookmaker zich vergist, zoals bij Sparta hierboven. Het model is wel nuttig om te begrijpen hoe odds werken, om je eigen inschatting te controleren en als basis die je verder uitbouwt.</p>
<p>Wil je het model echt gebruiken, test het dan eerst op honderden oude wedstrijden: hoe vaak kwam een kans van 60% echt uit? Vergelijk je kansen daarna met de slotkoers, zoals uitgelegd bij <a href="{CLV}">closing line value</a>. Hoe je een kans vertaalt naar verwacht rendement, lees je bij <a href="{EV}">expected value</a> en <a href="{VALUE}">value betting</a>. Zet nooit meer in dan je kunt missen, werk met <a href="{BANK}">bankroll management</a> en een <a href="{LIMIET}">netto-stortingslimiet</a>, en lees onze tips over <a href="/speel-bewust/verantwoord-wedden">verantwoord wedden</a>. Meer uitleg vind je in de <a href="/wedgids">wedgids</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe voorspel je een voetbaluitslag met Poisson?</strong><br>Bereken per team het verwachte aantal doelpunten (aanvalskracht × verdedigingszwakte tegenstander × competitiegemiddelde × thuis- of uitfactor), zet dat met de Poisson-formule om in kansen op 0, 1, 2 … goals en vermenigvuldig die in een scorematrix.</p>
<p><strong>Welke Excel-functie gebruik je voor Poisson?</strong><br>In de Nederlandse Excel is dat POISSON.VERD(x;gemiddelde;ONWAAR) voor de kans op precies x doelpunten. In de Engelse versie heet hij POISSON.DIST.</p>
<p><strong>Hoe nauwkeurig is het Poisson-model?</strong><br>Redelijk als basis, maar het onderschat gelijke spelen en kent geen blessures, opstellingen of vorm. Bij weinig wedstrijden of grote niveauverschillen wordt het snel te extreem.</p>
<p><strong>Wat is de Dixon-Coles-correctie?</strong><br>Een aanpassing uit 1997 die de kansen op lage uitslagen (0-0, 1-0, 0-1 en 1-1) corrigeert en recente wedstrijden zwaarder laat wegen. Daardoor schat het model gelijke spelen beter in.</p>
<p><strong>Kan ik xG gebruiken in plaats van doelpunten?</strong><br>Ja. Je vervangt de doelpunten voor en tegen door de xG voor en tegen. Dat is vaak stabieler, omdat xG minder afhankelijk is van toeval.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    html = content + content2 + content3
    assert re.search(r"<(ul|ol|/li)>\s+<", html) is None
    assert "/kennisbank/" not in html and "<h2" not in html and "<h4" not in html and "/go/" not in html
    assert html.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert content.startswith("<p><strong>")
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert len(OG_CHIPS) == 2 and len(OG_DATA) == 4
    for link in LINKS:
        assert f'href="{link}"' in html, link
    assert set(re.findall(r'href="([^"]+)"', html)) <= set(LINKS)
    for verboden in ("FootyMetrics", "BetCity", "opstellingvandaag", "waaroptv"):
        assert verboden.lower() not in html.lower(), verboden
    faq = content3.split("Veelgestelde vragen")[1]
    assert 4 <= faq.count("<p><strong>") <= 6
    woorden = len(re.sub(r"<[^>]+>", " ", html).split())
    assert 1200 <= woorden <= 2200, woorden
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", woorden, "woorden")
