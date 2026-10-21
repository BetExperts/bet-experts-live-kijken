# -*- coding: utf-8 -*-
"""Nieuw Nieuws-artikel: hoeveel punten heb je nodig om te overwinteren (top 24) en voor de top 8 in de
Europa League? Nieuwe league-fase sinds 2024/25.

Geverifieerd op 21-10-2026:
- Eindstanden league-fase 2024/25 en 2025/26: officiele UEFA-standen
  (standings.uefa.com/v1/standings?competitionId=14&seasonYear=2025 / 2026, status OFFICIAL).
- Tiebreakers: Reglement UEFA Europa League 2026/27, artikel 18.01 (in werking 29-07-2026).
- Tussenronde/achtste finales: zelfde reglement, artikel 19.02-19.04 (9/10-23/24 enz.; geplaatste club in principe
  thuis in de return; kwartfinale top 4, halve finale top 2 thuis in de return).
- Data 2026/27: uefa.com (bijgewerkt 21-10-2026): speelronde 1 16/17 sep ... speelronde 8 donderdag 28-01-2027
  (alle 18 duels 21.00 uur); tussenronde 18 + 25 feb 2027; achtste finales 11 + 18 mrt; kwart 8 + 15 apr;
  halve 29 apr + 6 mei; finale 26 mei 2027 Frankfurt. Winnaar krijgt een plek in de league-fase CL 2027/28.
- Coefficient: reglement 2026/27 bijlage D.5 (EL: plek 25-36 0; 24e 0,25 ... 1e 6,000; per KO-ronde vanaf achtste
  finales 1 punt) en UEFA-uitleg coefficienten (winst 2, gelijk 1).
- Nederlandse clubs 2026/27 na speelronde 2: UEFA-wedstrijddata, 21-10-2026.
  python3 specials/punten_overwinteren_el.py   (alleen dry run)"""
import os, sys, re
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "hoeveel-punten-nodig-overwinteren-europa-league"
TITEL = "Hoeveel punten nodig om te overwinteren in de Europa League?"
SAMENVATTING = ("Hoeveel punten heb je nodig voor de top 24 en de top 8 van de Europa League? De echte grenzen van "
                "2024/25 en 2025/26, met tiebreakers en vuistregel.")
RUBRIEK = "66a0fc334152a2dd17b16634"      # Europa League
COMPETITIE = "65de4be481512ad1b77740b1"   # Europa League

# Deelkaart (maatwerk)
OG_KOP = "Europa League: punten voor de <span>top 24</span>"
OG_EYEBROW = "Europa League · league-fase"
OG_CHIPS = ["8 duels · 36 clubs", "Grens op doelsaldo"]
OG_MOTIEF = "tabel"
OG_DATA = ["Top 8 · 16 à 17 punten", "Top 24 · ±10 punten", "2024/25 nr. 24 · 10 pnt", "2025/26 nr. 24 · 9 pnt"]

KSA = "<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"
EL = "/competities/europa-league"
FORMAT = ("/nieuws/champions-league-2025-uitleg-over-het-nieuwe-format-tussenronde-en-knock-outs-"
          "hoe-nu-verder-na-speelronde-8")
CL_ART = "/nieuws/hoeveel-punten-nodig-overwinteren-champions-league"

# Officiele eindstanden league-fase (plek, club, punten, doelsaldo, doelpunten voor) - UEFA, gelezen 21-10-2026
STAND = {
    "2024/25": [(1, 'Lazio', 19, 12, 17), (2, 'Athletic Bilbao', 19, 8, 15), (3, 'Manchester United', 18, 7, 16), (4, 'Tottenham', 17, 8, 17), (5, 'Eintracht Frankfurt', 16, 4, 14), (6, 'Olympique Lyon', 15, 8, 16), (7, 'Olympiacos', 15, 6, 9), (8, 'Rangers', 14, 6, 16), (9, 'Bodø/Glimt', 14, 3, 14), (10, 'Anderlecht', 14, 2, 14), (11, 'FCSB', 14, 1, 10), (12, 'Ajax', 13, 8, 16), (13, 'Real Sociedad', 13, 4, 13), (14, 'Galatasaray', 13, 3, 19), (15, 'AS Roma', 12, 4, 10), (16, 'Viktoria Plzeň', 12, 1, 13), (17, 'Ferencváros', 12, 0, 15), (18, 'Porto', 11, 2, 13), (19, 'AZ', 11, 0, 13), (20, 'Midtjylland', 11, 0, 9), (21, 'Union Sint-Gillis', 11, 0, 8), (22, 'PAOK', 10, 2, 12), (23, 'Twente', 10, -1, 8), (24, 'Fenerbahçe', 10, -2, 9), (25, 'Braga', 10, -3, 9), (26, 'Elfsborg', 10, -5, 9), (27, 'TSG Hoffenheim', 9, -3, 11), (28, 'Beşiktaş', 9, -5, 10), (29, 'Maccabi Tel Aviv', 6, -9, 8), (30, 'Slavia Praag', 5, -4, 7), (31, 'Malmö FF', 5, -7, 10), (32, 'RFS', 5, -7, 6), (33, 'Ludogorets', 4, -7, 4), (34, 'Dynamo Kiev', 4, -13, 5), (35, 'OGC Nice', 3, -9, 7), (36, 'Qarabağ', 3, -14, 6)],
    "2025/26": [(1, 'Olympique Lyon', 21, 13, 18), (2, 'Aston Villa', 21, 8, 14), (3, 'Midtjylland', 19, 10, 18), (4, 'Real Betis', 17, 6, 13), (5, 'Porto', 17, 6, 13), (6, 'Braga', 17, 6, 11), (7, 'SC Freiburg', 17, 6, 10), (8, 'AS Roma', 16, 7, 13), (9, 'Genk', 16, 4, 11), (10, 'Bologna', 15, 7, 14), (11, 'VfB Stuttgart', 15, 6, 15), (12, 'Ferencváros', 15, 1, 12), (13, 'Nottingham Forest', 14, 8, 15), (14, 'Viktoria Plzeň', 14, 5, 8), (15, 'Rode Ster Belgrado', 14, 1, 7), (16, 'Celta de Vigo', 13, 4, 15), (17, 'PAOK', 12, 3, 17), (18, 'Lille OSC', 12, 3, 12), (19, 'Fenerbahçe', 12, 3, 10), (20, 'Panathinaikos', 12, 2, 11), (21, 'Celtic', 11, -2, 13), (22, 'Ludogorets', 10, -3, 12), (23, 'Dinamo Zagreb', 10, -4, 12), (24, 'Brann', 9, -2, 9), (25, 'Young Boys', 9, -6, 10), (26, 'Sturm Graz', 7, -6, 5), (27, 'FCSB', 7, -7, 9), (28, 'Go Ahead Eagles', 7, -8, 6), (29, 'Feyenoord', 6, -4, 11), (30, 'Basel', 6, -4, 9), (31, 'RB Salzburg', 6, -5, 10), (32, 'Rangers', 4, -9, 5), (33, 'OGC Nice', 3, -8, 7), (34, 'Utrecht', 1, -10, 5), (35, 'Malmö FF', 1, -11, 4), (36, 'Maccabi Tel Aviv', 1, -20, 2)],
}
for s, rij in STAND.items():
    assert len(rij) == 36 and [r[0] for r in rij] == list(range(1, 37))
    assert all(a[2] >= b[2] for a, b in zip(rij, rij[1:])), s
# Ter vergelijking: Champions League (UEFA, zelfde bron) plek 8 en plek 24
CL_GRENS = {"2024/25": (16, 11), "2025/26": (16, 9)}


def plek(seizoen, p):
    return STAND[seizoen][p - 1]


def sd(x):
    return f"+{x}" if x > 0 else str(x)


def telling(punten, grens, tot=None):
    tot = punten if tot is None else tot
    rijen = [r for s in STAND for r in STAND[s] if punten <= r[2] <= tot]
    return sum(1 for r in rijen if r[0] <= grens), len(rijen)


def cel(seizoen, p):
    n, club, pt, d, g = plek(seizoen, p)
    return f"<strong>{pt} punten</strong><br>{club} ({sd(d)})"


def gelijk(seizoen, punten):
    return [r[1] for r in STAND[seizoen] if r[2] == punten]


# Controles op de officiele standen
assert [plek("2024/25", p)[2] for p in (8, 9, 24, 25)] == [14, 14, 10, 10]
assert [plek("2025/26", p)[2] for p in (8, 9, 24, 25)] == [16, 16, 9, 9]
assert gelijk("2024/25", 14) == ["Rangers", "Bodø/Glimt", "Anderlecht", "FCSB"]
assert gelijk("2024/25", 10) == ["PAOK", "Twente", "Fenerbahçe", "Braga", "Elfsborg"]
assert [plek("2024/25", p)[3:] for p in (19, 20, 21)] == [(0, 13), (0, 9), (0, 8)]   # AZ boven op doelpunten

PT = list(range(17, 8, -1))
VR = {p: (telling(p, 24), telling(p, 8)) for p in PT}
assert VR[11][0] == (5, 5) and VR[10][0] == (5, 7) and VR[9][0] == (1, 4)
assert VR[17][1] == (5, 5) and VR[16][1] == (2, 3) and VR[15][1] == (2, 5) and VR[14][1] == (1, 7)
assert telling(11, 24, 99)[0] == telling(11, 24, 99)[1] and telling(0, 24, 8)[0] == 0
assert telling(17, 8, 99)[0] == telling(17, 8, 99)[1] and telling(0, 8, 13)[0] == 0


def oordeel24(p):
    return "<strong>Zeker</strong>" if p >= 11 else ("Meestal genoeg" if p == 10 else "Meestal te weinig")


def oordeel8(p):
    return ("<strong>Zeker</strong>" if p >= 17 else "Meestal genoeg" if p == 16 else
            "Twijfelachtig" if p == 15 else "Meestal te weinig" if p == 14 else "Te weinig")


# Coefficient-bonus EL (bijlage D.5): plek 25-36 niets; plek 24 0,25 ... plek 1 6,000
def bonus(p):
    return 0.0 if p >= 25 else (25 - p) * 0.25


assert bonus(1) == 6 and bonus(8) == 4.25 and bonus(9) == 4 and bonus(24) == 0.25 and bonus(25) == 0
TOP8_R16 = bonus(8) + 1          # top 8 + bonus voor de achtste finales
assert TOP8_R16 == 5.25


def nl(x):
    return f"{x:.2f}".rstrip("0").rstrip(".").replace(".", ",")


content = f"""<p><strong>Om te overwinteren in de Europa League, dus om bij de beste 24 van de league-fase te eindigen, heb je meestal 10 punten nodig. Met 11 punten ging tot nu toe elke club door, met 9 punten lukte het bijna nooit. Voor de top 8, en dus een direct ticket voor de achtste finales, moet je rekenen op 16 à 17 punten. Dat is minder ruim dan veel mensen denken.</strong></p>
<p>Die vuistregel is gebaseerd op de officiële eindstanden van de eerste twee seizoenen met het nieuwe format, 2024/25 en 2025/26. De <a href="{EL}">Europa League</a> 2026/27 speelt op donderdag 22 oktober speelronde 3, met <a href="/clubs/az">AZ</a> en <a href="/clubs/nec-nijmegen">NEC</a> als Nederlandse deelnemers. De laatste speelronde is op donderdag 28 januari 2027. Pas dan weet je wie er overwintert.</p>
<h3><strong>Wat betekent overwinteren in de Europa League nu nog?</strong></h3>
<p>Vroeger speelde je in de Europa League zes duels in een poule van vier. De groepswinnaar ging direct naar de achtste finales, de nummer 2 naar een tussenronde tegen clubs die uit de Champions League waren afgezakt. De nummer 3 zakte zelf weer af naar de Conference League. Half december wist iedereen waar hij stond.</p>
<p>Sinds 2024/25 werkt het anders. Er is één ranglijst met 36 clubs en niemand stroomt nog in of uit. Er komen geen clubs uit de Champions League bij en wie als 25e of lager eindigt, gaat niet naar de Conference League. Die is gewoon klaar. Overwinteren betekent nu dus: <strong>bij de beste 24 eindigen</strong> en in februari of maart nog Europees spelen.</p>
<h3><strong>Zo werkt de league-fase van de Europa League</strong></h3>
<p>Net als in de Champions League speelt elke club <strong>8 wedstrijden tegen 8 verschillende tegenstanders</strong> uit vier potten, vier thuis en vier uit. Alle duels zijn op donderdag. Het deelnemersveld is breder dan in de Champions League: naast clubs uit de grote competities doen er veel clubs mee uit landen als Noorwegen, Bulgarije, Kroatië, Griekenland en Zwitserland. Het niveau ligt daardoor dichter bij elkaar. Dat zie je terug in de stand: veel clubs eindigen op hetzelfde aantal punten.</p>
{tabel(["Eindplek", "Gevolg in de Europa League"], [
    ("<strong>1 t/m 8</strong>", "Rechtstreeks naar de achtste finales (11 en 18 maart 2027)"),
    ("<strong>9 t/m 24</strong>", "Tussenronde over twee duels (18 en 25 februari 2027)"),
    ("<strong>25 t/m 36</strong>", "Klaar in Europa, ook geen overstap naar de Conference League"),
])}
<h3><strong>Hoeveel punten hadden de nummers 8, 9, 24 en 25?</strong></h3>
{tabel(["Plek", "2024/25", "2025/26"], [
    (f"<strong>Plek {p}</strong>", cel("2024/25", p), cel("2025/26", p)) for p in (8, 9, 24, 25)
])}
<p>In 2024/25 lagen de grenzen opvallend laag. Voor de top 8 was 14 punten genoeg, maar alleen voor Rangers. Vier clubs eindigden op 14 punten: Rangers had het beste doelsaldo (+6) en pakte plek 8. Bodø/Glimt, Anderlecht en FCSB moesten de tussenronde in.</p>
<p>Rond plek 24 was het nog voller. Vijf clubs eindigden op 10 punten. PAOK, <a href="/clubs/fc-twente">FC Twente</a> en Fenerbahçe gingen door, Braga en Elfsborg vielen af. Het doelsaldo besliste: Fenerbahçe -2, Braga -3. Eén doelpunt dus.</p>
<p>In 2025/26 lag alles hoger. Roma en Genk eindigden allebei op 16 punten, Roma pakte op doelsaldo de laatste plek in de top 8. Onderin waren 9 punten net genoeg voor Brann (-2), terwijl Young Boys met ook 9 punten maar een slechter doelsaldo (-6) afviel.</p>"""

content2 = f"""<h3><strong>Vuistregel: hoeveel punten heb je nodig in de Europa League?</strong></h3>
<p>In deze tabel zie je per puntentotaal hoeveel clubs in de twee seizoenen bij de beste 24 en bij de beste 8 eindigden.</p>
{tabel(["Punten", "Top 24", "Oordeel top 24", "Top 8", "Oordeel top 8"], [
    (f"<strong>{p}</strong>", f"{VR[p][0][0]} van {VR[p][0][1]}", oordeel24(p), f"{VR[p][1][0]} van {VR[p][1][1]}", oordeel8(p))
    for p in PT
])}
<p>Samengevat:</p>
<ul><li><strong>Top 24 zeker:</strong> 11 punten of meer. Elke club met 11 punten of meer ging door.</li><li><strong>Top 24 meestal genoeg:</strong> 10 punten. Vijf van de zeven clubs met 10 punten overwinterden.</li><li><strong>Top 24 te weinig:</strong> 9 punten of minder. Van de vier clubs met 9 punten ging er maar één door.</li><li><strong>Top 8 zeker:</strong> 17 punten of meer.</li><li><strong>Top 8 meestal genoeg:</strong> 16 punten. Met 14 of 15 punten heb je vooral geluk nodig.</li></ul>
<p>Tien punten haal je bijvoorbeeld met drie zeges en één gelijkspel, of met twee zeges en vier gelijke spelen. Voor 16 punten heb je vijf zeges en één gelijkspel nodig.</p>
<h3><strong>Is de Europa League makkelijker dan de Champions League?</strong></h3>
<p>Je zou denken dat je in de Europa League met minder punten toekunt. Dat klopt maar half. Voor de top 24 lag de grens hooguit één punt lager. Voor de top 8 wisselde het: in 2024/25 was 14 punten genoeg, in 2025/26 had je net als in de Champions League 16 punten nodig.</p>
{tabel(["Grens", "Champions League", "Europa League"], [
    ("<strong>Plek 8 in 2024/25</strong>", f"{CL_GRENS['2024/25'][0]} punten", f"{plek('2024/25', 8)[2]} punten"),
    ("<strong>Plek 8 in 2025/26</strong>", f"{CL_GRENS['2025/26'][0]} punten", f"{plek('2025/26', 8)[2]} punten"),
    ("<strong>Plek 24 in 2024/25</strong>", f"{CL_GRENS['2024/25'][1]} punten", f"{plek('2024/25', 24)[2]} punten"),
    ("<strong>Plek 24 in 2025/26</strong>", f"{CL_GRENS['2025/26'][1]} punten", f"{plek('2025/26', 24)[2]} punten"),
])}
<p>Het grote verschil zit in de spreiding. In de Champions League zijn er meer echte toppers die veel punten pakken en meer clubs die onderaan bijna niets halen. In de Europa League eindigen veel clubs in het midden, dicht bij elkaar. Daardoor beslist het doelsaldo daar vaker. Een 0-3 nederlaag in plaats van 0-1 kan in januari het verschil maken. Wil je de grenzen van de Champions League in detail zien, lees dan <a href="{CL_ART}">hoeveel punten je nodig hebt om te overwinteren in de Champions League</a>.</p>
<h3><strong>Welke tiebreakers gelden in de Europa League?</strong></h3>
<p>Het reglement van de UEFA voor de Europa League 2026/27 gebruikt bij gelijke punten deze volgorde. Een onderling duel telt niet mee.</p>
<ol><li>Doelsaldo</li><li>Gescoorde doelpunten</li><li>Gescoorde uitdoelpunten</li><li>Aantal zeges</li><li>Aantal uitzeges</li><li>Totaal aantal punten van je acht tegenstanders</li><li>Doelsaldo van je tegenstanders</li><li>Doelpunten van je tegenstanders</li><li>Minste kaarten (geel 1 punt, rood of twee keer geel 3 punten)</li><li>Clubcoëfficiënt</li></ol>
<p>Een mooi voorbeeld is 2024/25. AZ, Midtjylland en Union Sint-Gillis eindigden alle drie op 11 punten met een doelsaldo van 0. Toen beslisten de gescoorde doelpunten: AZ 13, Midtjylland 9 en Union 8. Daardoor werd AZ 19e. Dat lijkt een detail, maar je eindplek bepaalt je tegenstander in de tussenronde.</p>"""

content3 = f"""<h3><strong>Hoe werkt de tussenronde van de Europa League?</strong></h3>
<p>De nummers 9 tot en met 16 zijn geplaatst en spelen in principe de return thuis. Zij loten tegen de nummers 17 tot en met 24 volgens vaste paren: 9/10 tegen 23/24, 11/12 tegen 21/22, 13/14 tegen 19/20 en 15/16 tegen 17/18. De winnaars gaan naar de achtste finales tegen de top 8. Die top 8 speelt daar de return thuis. In de kwartfinale hebben de nummers 1 tot en met 4 dat voordeel, in de halve finale de nummers 1 en 2.</p>
{tabel(["Ronde", "Datum (donderdag)"], [
    ("Speelronde 1 en 2", "16/17 september en 15 oktober 2026"),
    ("<strong>Speelronde 3</strong>", "<strong>22 oktober 2026</strong>"),
    ("Speelronde 4, 5 en 6", "5 november, 26 november en 10 december 2026"),
    ("Speelronde 7", "21 januari 2027"),
    ("<strong>Speelronde 8</strong>", "<strong>28 januari 2027</strong>, alle 18 duels om 21.00 uur"),
    ("Tussenronde", "18 en 25 februari 2027"),
    ("Achtste finales", "11 en 18 maart 2027"),
    ("Finale", "woensdag 26 mei 2027 in Frankfurt"),
])}
<p>De winnaar van de Europa League krijgt een plek in de league-fase van de Champions League 2027/28. Aan het format verandert dit seizoen niets.</p>
<h3><strong>Waarom de eindplek telt voor de coëfficiënt</strong></h3>
<p>Voor de landenranking van de UEFA levert een zege 2 punten op en een gelijkspel 1 punt. In de Europa League krijg je, anders dan in de Champions League, geen bonus voor alleen meedoen. Bonuspunten krijg je pas vanaf plek 24: {nl(bonus(24))} punt. Per plek hoger komt daar 0,25 bij, tot {nl(bonus(1))} punten voor de nummer 1. Wie 25e of lager eindigt, krijgt niets extra.</p>
<p>Rekenvoorbeeld: een club die als 8e eindigt, krijgt {nl(bonus(8))} bonuspunten en daarna nog 1 punt voor het halen van de achtste finales. Samen {nl(TOP8_R16)} punten, zonder in februari te spelen. Een club op plek 24 krijgt {nl(bonus(24))} punt, maar kan in de tussenronde wel nog wedstrijdpunten pakken. Voor Nederland telt elk punt, want de punten van alle Nederlandse clubs in Europa worden opgeteld en gedeeld door het aantal clubs.</p>
<h3><strong>Hoe deden Nederlandse clubs het in de Europa League?</strong></h3>
{tabel(["Seizoen", "Club", "Punten", "Plek", "Afloop"], [
    ("2024/25", '<a href="/clubs/ajax">Ajax</a>', "13", "12e", "Won de tussenronde van Union Sint-Gillis, achtste finale verloren van Eintracht Frankfurt"),
    ("2024/25", "AZ", "11", "19e", "Won de tussenronde van Galatasaray, achtste finale verloren van Tottenham"),
    ("2024/25", "FC Twente", "10", "23e", "Tussenronde verloren van Bodø/Glimt"),
    ("2025/26", '<a href="/clubs/go-ahead-eagles">Go Ahead Eagles</a>', "7", "28e", "Uitgeschakeld"),
    ("2025/26", '<a href="/clubs/feyenoord">Feyenoord</a>', "6", "29e", "Uitgeschakeld"),
    ("2025/26", '<a href="/clubs/fc-utrecht">FC Utrecht</a>', "1", "34e", "Uitgeschakeld"),
])}
<p>FC Twente is het bewijs dat 10 punten genoeg kan zijn: met precies die 10 punten en een doelsaldo van -1 werd Twente in 2024/25 nog 23e. Vorig seizoen kwam geen enkele Nederlandse club in de buurt van de grens.</p>
<p>Dit seizoen heeft AZ na twee duels 3 punten (0-1 verlies bij Sunderland, 2-1 winst op Hapoel Beer-Sheva). NEC staat op 1 punt (5-0 verlies bij Juventus, 1-1 tegen Levski Sofia). Op 22 oktober speelt AZ bij Ararat-Armenia en NEC bij Dinamo Zagreb. Met de vuistregel van 10 punten heeft AZ nog zo'n 7 punten nodig uit zes duels, NEC zo'n 9.</p>
<h3><strong>Wedden op de top 24 of de winnaar van de Europa League</strong></h3>
<p>Omdat de stand in de Europa League zo dicht op elkaar zit, is wedden op de eindstand lastig te voorspellen. Bij een deel van de legale bookmakers vind je markten als "plaatst zich voor de knock-outfase", "eindigt in de top 8" of de toernooiwinnaar. Kijk vooral naar het resterende programma en het doelsaldo. Twee clubs met evenveel punten kunnen er heel anders voor staan. Vergelijk de odds, zet nooit meer in dan je kunt missen en lees in onze <a href="/wedgids">wedgids</a> hoe zulke langetermijnweddenschappen werken. Hoe de knock-outfase na speelronde 8 verloopt, lees je in onze <a href="{FORMAT}">uitleg over het nieuwe format en de tussenronde</a>.</p>
<p>In de Conference League speel je maar zes duels en valt de beslissing al op 17 december; daar was 7 à 8 punten genoeg. Lees <a href="/nieuws/hoeveel-punten-nodig-overwinteren-conference-league">hoeveel punten je nodig hebt om te overwinteren in de Conference League</a>.</p>
<h3><strong>Veelgestelde vragen over overwinteren in de Europa League</strong></h3>
<p><strong>Hoeveel punten heb je nodig om te overwinteren in de Europa League?</strong><br>Meestal 10 punten. Met 11 punten of meer ging tot nu toe elke club door. In 2024/25 had de nummer 24 10 punten, in 2025/26 9 punten.</p>
<p><strong>Hoeveel punten heb je nodig voor de top 8 van de Europa League?</strong><br>Reken op 16 à 17 punten. In 2024/25 was 14 punten net genoeg voor plek 8, in 2025/26 was 16 punten nodig.</p>
<p><strong>Ga je als nummer 25 naar de Conference League?</strong><br>Nee. Sinds 2024/25 zakt niemand meer af. De nummers 25 tot en met 36 zijn uitgeschakeld.</p>
<p><strong>Hoeveel wedstrijden speel je in de league-fase van de Europa League?</strong><br>Acht, net als in de Champions League. Vier thuis en vier uit, tegen acht verschillende tegenstanders uit vier potten.</p>
<p><strong>Wanneer weet je of je overwintert?</strong><br>Na speelronde 8 op donderdag 28 januari 2027. Alle duels beginnen dan tegelijk om 21.00 uur.</p>
<p><strong>Wat beslist bij gelijke punten?</strong><br>Eerst het doelsaldo, dan het aantal gescoorde doelpunten en daarna de uitdoelpunten.</p>
{KSA}"""

if __name__ == "__main__":
    html = content + content2 + content3
    assert not re.search(r"<(ul|ol|/li)>\s+<", html), "witruimte tussen lijsttags"
    assert "<h2" not in html and "/kennisbank/" not in html
    assert html.rstrip().endswith(KSA), "KSA-regel niet als laatste"
    assert len(TITEL) <= 65 and 120 <= len(SAMENVATTING) <= 155
    assert len(OG_CHIPS) == 2 and len(OG_DATA) == 4 and OG_MOTIEF == "tabel"
    faq = len(re.findall(r"<p><strong>[^<]+\?</strong><br>", html))
    assert 5 <= faq <= 7, faq
    tekst = re.sub(r"<[^>]+>", " ", html)
    w = len(tekst.split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", w, "woorden |", faq, "faq |",
          len(content), len(content2), len(content3), "tekens per veld")
    assert 1300 <= w <= 2100, w
    print("Dry run: er is niets gepubliceerd.")
