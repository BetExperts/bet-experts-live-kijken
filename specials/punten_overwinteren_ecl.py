# -*- coding: utf-8 -*-
"""Nieuw Nieuws-artikel: hoeveel punten heb je nodig om te overwinteren (top 24) en voor de top 8 in de
UEFA Conference League? League-fase met 36 clubs en 6 duels sinds 2024/25.

Geverifieerd op 21-10-2026:
- Eindstanden league-fase 2024/25 en 2025/26: officiele UEFA-standen
  (standings.uefa.com/v1/standings?competitionId=2019&seasonYear=2025 / 2026, status OFFICIAL; 6 duels per club).
- Lotingsysteem: uefa.com (loting 28-08-2026): 6 potten van 6, een tegenstander per pot; potten 1+2, 3+4, 5+6
  gekoppeld (een thuis, een uit) -> 3 thuis, 3 uit; geen clubs uit eigen land, max. 2 uit hetzelfde andere land.
- Tiebreakers: Reglement UEFA Conference League 2026/27, art. 18.01 (in werking 29-07-2026), gelijk aan CL/EL.
- Tussenronde: zelfde reglement, art. 19.02-19.04 (9/10-23/24, 11/12-21/22, 13/14-19/20, 15/16-17/18; geplaatste
  club in principe thuis in de return; achtste finales top 8, kwart top 4, halve top 2 thuis in de return).
- Data 2026/27: uefa.com (bijgewerkt 21-10-2026): speelronde 1 15-10 ... speelronde 6 do 17-12-2026 (alle duels
  21.00 uur); tussenronde 18 + 25 feb 2027; achtste finales 11 + 18 mrt; kwart 8 + 15 apr; halve 29 apr + 6 mei;
  finale wo 2 juni 2027, Besiktas Stadion Istanbul. Winnaar: plek in league-fase Europa League 2027/28.
- Coefficient: reglement 2026/27 bijlage D.5 (UECL: 1e 4,000 ... 8e 2,250, 9e 2,000 ... 24e 0,125, 25-36 0;
  per KO-ronde vanaf achtste finales 0,5) en UEFA-uitleg coefficienten (winst 2, gelijk 1).
- Nederlandse clubs: 2024/25 geen in de league-fase; 2025/26 AZ (UEFA-standen + wedstrijddata);
  2026/27 na speelronde 1 (Ajax, Twente), speelronde 2 op 22-10-2026 nog niet gespeeld.
  python3 specials/punten_overwinteren_ecl.py   (alleen dry run)"""
import os, sys, re
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "hoeveel-punten-nodig-overwinteren-conference-league"
TITEL = "Hoeveel punten nodig om te overwinteren in de Conference League?"
SAMENVATTING = ("Hoeveel punten heb je nodig voor de top 24 en top 8 van de Conference League? Zes duels, lagere "
                "grenzen: de echte cijfers van 2024/25 en 2025/26.")
RUBRIEK = "66a10267c938b248756d886d"      # Conference League
COMPETITIE = "65de4bf0f348c222f01bed83"   # Conference League

# Deelkaart (maatwerk)
OG_KOP = "Conference League: punten voor de <span>top 24</span>"
OG_EYEBROW = "Conference League · 6 duels"
OG_CHIPS = ["Max. 18 punten", "Beslissing 17 december"]
OG_MOTIEF = "tabel"
OG_DATA = ["Top 8 · 12 punten", "Top 24 · 7 à 8 punten", "2024/25 nr. 24 · 7 pnt", "2025/26 nr. 24 · 7 pnt"]

KSA = "<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"
ECL = "/competities/conference-league"
CL_ART = "/nieuws/hoeveel-punten-nodig-overwinteren-champions-league"
EL_ART = "/nieuws/hoeveel-punten-nodig-overwinteren-europa-league"

DUELS = 6
MAX = DUELS * 3

# Officiele eindstanden league-fase (plek, club, punten, doelsaldo, doelpunten voor) - UEFA, gelezen 21-10-2026
STAND = {
    "2024/25": [(1, 'Chelsea', 18, 21, 26), (2, 'Vitória Guimarães', 14, 7, 13), (3, 'Fiorentina', 13, 11, 18), (4, 'Rapid Wien', 13, 6, 11), (5, 'Djurgårdens IF', 13, 4, 11), (6, 'Lugano', 13, 4, 11), (7, 'Legia Warschau', 12, 8, 13), (8, 'Cercle Brugge', 11, 7, 14), (9, 'Jagiellonia Białystok', 11, 5, 10), (10, 'Shamrock Rovers', 11, 3, 12), (11, 'APOEL', 11, 3, 8), (12, 'Pafos', 10, 4, 11), (13, 'Panathinaikos', 10, 3, 10), (14, 'Olimpija Ljubljana', 10, 1, 7), (15, 'Real Betis', 10, 1, 6), (16, '1. FC Heidenheim', 10, 0, 7), (17, 'KAA Gent', 9, 0, 8), (18, 'FC Kopenhagen', 8, -1, 8), (19, 'Víkingur Reykjavík', 8, -1, 7), (20, 'Borac Banja Luka', 8, -3, 4), (21, 'NK Celje', 7, 0, 13), (22, 'Omonia Nicosia', 7, 0, 7), (23, 'Molde', 7, -1, 10), (24, 'TSC Bačka Topola', 7, -3, 10), (25, 'Heart of Midlothian', 7, -3, 6), (26, 'Başakşehir', 6, -3, 9), (27, 'Mladá Boleslav', 6, -3, 7), (28, 'Astana', 5, -4, 4), (29, 'FC St. Gallen', 5, -8, 10), (30, 'HJK Helsinki', 4, -6, 3), (31, 'FC Noah', 4, -10, 6), (32, 'The New Saints', 3, -5, 5), (33, 'Dinamo Minsk', 3, -9, 4), (34, 'Larne', 3, -9, 3), (35, 'LASK', 3, -10, 4), (36, 'Petrocub Hîncești', 2, -9, 4)],
    "2025/26": [(1, 'Strasbourg', 16, 6, 11), (2, 'Raków Częstochowa', 14, 7, 9), (3, 'AEK Athene', 13, 7, 14), (4, 'Sparta Praag', 13, 7, 10), (5, 'Rayo Vallecano', 13, 6, 13), (6, 'Sjachtar Donetsk', 13, 5, 10), (7, 'Mainz 05', 13, 4, 7), (8, 'AEK Larnaca', 12, 6, 7), (9, 'Lausanne-Sport', 11, 3, 6), (10, 'Crystal Palace', 10, 5, 11), (11, 'Lech Poznań', 10, 4, 12), (12, 'Samsunspor', 10, 4, 10), (13, 'NK Celje', 10, 1, 8), (14, 'AZ', 10, 0, 7), (15, 'Fiorentina', 9, 3, 8), (16, 'HNK Rijeka', 9, 3, 5), (17, 'Jagiellonia Białystok', 9, 1, 5), (18, 'Omonia Nicosia', 8, 1, 5), (19, 'FC Noah', 8, -1, 6), (20, 'FC Drita', 8, -4, 4), (21, 'KuPS Kuopio', 7, 1, 6), (22, 'Shkëndija', 7, -1, 4), (23, 'Zrinjski Mostar', 7, -2, 8), (24, 'Sigma Olomouc', 7, -2, 7), (25, 'Universitatea Craiova', 7, -2, 6), (26, 'Lincoln Red Imps', 7, -8, 7), (27, 'Dynamo Kiev', 6, 0, 9), (28, 'Legia Warschau', 6, 0, 8), (29, 'Slovan Bratislava', 6, -4, 5), (30, 'Breiðablik', 5, -5, 6), (31, 'Shamrock Rovers', 4, -6, 7), (32, 'BK Häcken', 3, -3, 5), (33, 'Ħamrun Spartans', 3, -7, 4), (34, 'Shelbourne', 2, -7, 0), (35, 'Aberdeen', 2, -11, 3), (36, 'Rapid Wien', 1, -11, 3)],
}
for s, rij in STAND.items():
    assert len(rij) == 36 and [r[0] for r in rij] == list(range(1, 37))
    assert all(a[2] >= b[2] for a, b in zip(rij, rij[1:])), s
    assert max(r[2] for r in rij) <= MAX
# Ter vergelijking (UEFA, zelfde bron): punten van de nummer 8 en 24 in CL en EL (8 duels)
ANDERS = {"Champions League": {"2024/25": (16, 11), "2025/26": (16, 9)},
          "Europa League": {"2024/25": (14, 10), "2025/26": (16, 9)}}


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
    return f"<strong>{pt} punten</strong><br>{club} ({sd(d)}, {g} goals)"


def nl(x, dec=3):
    return f"{x:.{dec}f}".rstrip("0").rstrip(".").replace(".", ",")


# Controles op de officiele standen
assert [plek("2024/25", p)[2] for p in (8, 9, 24, 25)] == [11, 11, 7, 7]
assert [plek("2025/26", p)[2] for p in (8, 9, 24, 25)] == [12, 11, 7, 7]
# 2024/25: TSC en Hearts gelijk op punten en doelsaldo, TSC door op gescoorde doelpunten
assert plek("2024/25", 24)[2:4] == plek("2024/25", 25)[2:4] and plek("2024/25", 24)[4] > plek("2024/25", 25)[4]
# 2025/26: Zrinjski, Sigma Olomouc en Craiova alle drie 7 punten en -2; doelpunten 8, 7, 6
assert [plek("2025/26", p)[2:] for p in (23, 24, 25)] == [(7, -2, 8), (7, -2, 7), (7, -2, 6)]
# 2024/25 top 8: Cercle Brugge en Jagiellonia 11 punten, doelsaldo +7 tegen +5
assert plek("2024/25", 8)[2] == plek("2024/25", 9)[2] and plek("2024/25", 8)[3] > plek("2024/25", 9)[3]

PT = list(range(13, 5, -1))
VR = {p: (telling(p, 24), telling(p, 8)) for p in PT}
assert telling(8, 24, 99)[0] == telling(8, 24, 99)[1]          # 8+ punten: altijd top 24
assert VR[7][0] == (8, 11) and telling(0, 24, 6)[0] == 0        # 7: 8 van 11; 6 of minder: nooit
assert telling(12, 8, 99)[0] == telling(12, 8, 99)[1]          # 12+ punten: altijd top 8
assert VR[11][1] == (1, 5) and telling(0, 8, 10)[0] == 0
N7 = VR[7][0]


def oordeel24(p):
    return "<strong>Zeker</strong>" if p >= 8 else ("Meestal genoeg" if p == 7 else "<strong>Te weinig</strong>")


def oordeel8(p):
    return "<strong>Zeker</strong>" if p >= 12 else ("Meestal te weinig" if p == 11 else "Te weinig")


# Punten per duel: grens top 24 in verhouding tot het aantal duels
PPD = {"CL/EL (8 duels)": 10 / 8, "Conference League (6 duels)": 7.5 / 6}
assert round(PPD["CL/EL (8 duels)"], 2) == 1.25 and round(PPD["Conference League (6 duels)"], 2) == 1.25


# Coefficient-bonus UECL (bijlage D.5)
def bonus(p):
    if p >= 25:
        return 0.0
    if p >= 9:
        return 2.0 - (p - 9) * 0.125
    return 4.0 - (p - 1) * 0.25


assert bonus(1) == 4 and bonus(8) == 2.25 and bonus(9) == 2 and bonus(24) == 0.125 and bonus(25) == 0
AZ_BONUS = bonus(14) + 2 * 0.5      # AZ 2025/26: plek 14, achtste finale + kwartfinale
assert bonus(14) == 1.375 and AZ_BONUS == 2.375

content = f"""<p><strong>Om te overwinteren in de Conference League, dus om bij de beste 24 van de league-fase te eindigen, heb je meestal 7 à 8 punten nodig. Met 8 punten of meer ging tot nu toe elke club door, met 7 punten lukte het {N7[0]} van de {N7[1]} keer. Voor de top 8 heb je ongeveer 12 punten nodig. De grenzen liggen lager dan in de Champions League en Europa League, omdat je maar zes duels speelt.</strong></p>
<p>Die getallen komen uit de officiële eindstanden van de eerste twee seizoenen met het nieuwe format, 2024/25 en 2025/26. De <a href="{ECL}">Conference League</a> 2026/27 speelt op donderdag 22 oktober speelronde 2, met <a href="/clubs/ajax">Ajax</a> en <a href="/clubs/fc-twente">FC Twente</a> als Nederlandse deelnemers. De laatste speelronde is al op donderdag 17 december 2026.</p>
<h3><strong>Waarom liggen de grenzen lager in de Conference League?</strong></h3>
<p>Ook de Conference League heeft één ranglijst met 36 clubs. Maar elke club speelt er <strong>zes wedstrijden</strong> in plaats van acht. De loting werkt met zes potten van zes clubs. Je krijgt <strong>één tegenstander uit elke pot</strong>. De potten zijn per twee gekoppeld (1 en 2, 3 en 4, 5 en 6): tegen de ene club uit zo'n koppel speel je thuis, tegen de andere uit. Zo kom je op drie thuis- en drie uitduels. Clubs uit je eigen land kom je niet tegen.</p>
<p>Met zes duels kun je maximaal {MAX} punten halen, tegen 24 in de andere twee toernooien. Logisch dus dat de grenzen lager liggen.</p>
{tabel(["", "Champions League", "Europa League", "Conference League"], [
    ("<strong>Wedstrijden</strong>", "8", "8", f"<strong>{DUELS}</strong>"),
    ("<strong>Potten</strong>", "4 (twee tegenstanders per pot)", "4 (twee tegenstanders per pot)", "<strong>6 (één tegenstander per pot)</strong>"),
    ("<strong>Maximaal aantal punten</strong>", "24", "24", f"<strong>{MAX}</strong>"),
    ("<strong>Laatste speelronde 2026/27</strong>", "27 januari 2027", "28 januari 2027", "<strong>17 december 2026</strong>"),
    ("<strong>Nummer 24 in 2024/25 / 2025/26</strong>", "{0} / {1} punten".format(*[ANDERS["Champions League"][s][1] for s in STAND]),
     "{0} / {1} punten".format(*[ANDERS["Europa League"][s][1] for s in STAND]),
     "<strong>{0} / {1} punten</strong>".format(*[plek(s, 24)[2] for s in STAND])),
])}
<p>Reken je het om naar punten per wedstrijd, dan is de lat ongeveer even hoog. In de Champions League en Europa League heb je voor de top 24 zo'n 10 punten uit 8 duels nodig: {nl(PPD["CL/EL (8 duels)"], 2)} per duel. In de Conference League is dat 7 à 8 punten uit 6 duels, gemiddeld ook {nl(PPD["Conference League (6 duels)"], 2)} per duel.</p>
<h3><strong>Overwinteren in de Conference League: weer zoals vroeger?</strong></h3>
<p>In de Champions League en Europa League loopt de league-fase door tot eind januari. Daar weet je pas ná de winter of je "overwintert". In de Conference League is dat anders. De zesde en laatste speelronde is op <strong>donderdag 17 december 2026</strong>. Net als vroeger in het poulesysteem weet je dus vóór de winterstop of je in het voorjaar nog Europees voetbal speelt.</p>
<p>Toch is er één groot verschil met vroeger. In het oude format van de Conference League kwamen er na de winter clubs bij: de nummers 3 uit de Europa League-poules zakten af en speelden een tussenronde tegen de nummers 2. Dat bestaat niet meer. Er komen geen clubs bij uit de Europa League, en wie als 25e of lager eindigt, zakt nergens naartoe. Die is gewoon klaar. Overwinteren betekent dus: <strong>bij de beste 24 eindigen</strong>. Daarna volgt een lange pauze tot de tussenronde op 18 februari 2027.</p>
<h3><strong>Hoeveel punten hadden de nummers 8, 9, 24 en 25?</strong></h3>
{tabel(["Plek", "2024/25", "2025/26"], [
    (f"<strong>Plek {p}</strong>", cel("2024/25", p), cel("2025/26", p)) for p in (8, 9, 24, 25)
])}
<p>In beide seizoenen besliste rond plek 24 niet het doelsaldo, maar het tweede criterium: het aantal gescoorde doelpunten. In 2024/25 eindigden TSC Bačka Topola en Heart of Midlothian allebei op 7 punten en een doelsaldo van -3. TSC had 10 keer gescoord, Hearts 6 keer. TSC ging door.</p>
<p>In 2025/26 was het nog krapper. Zrinjski Mostar, Sigma Olomouc en Universitatea Craiova eindigden alle drie op 7 punten en -2. Zrinjski scoorde 8 keer, Sigma 7 keer en Craiova 6 keer. Craiova viel daardoor als nummer 25 af, met precies één doelpunt minder dan Sigma.</p>
<p>Ook om de top 8 werd het spannend. In 2024/25 hadden Cercle Brugge en Jagiellonia Białystok allebei 11 punten. Cercle had het betere doelsaldo (+7 tegen +5) en ging direct naar de achtste finales. In 2025/26 lag de grens een punt hoger: AEK Larnaca werd met 12 punten achtste.</p>"""

content2 = f"""<h3><strong>Vuistregel: hoeveel punten heb je nodig?</strong></h3>
<p>In deze tabel zie je per puntentotaal hoeveel clubs in de twee seizoenen bij de beste 24 en bij de beste 8 eindigden.</p>
{tabel(["Punten na 6 duels", "Top 24", "Oordeel top 24", "Top 8", "Oordeel top 8"], [
    (f"<strong>{p}</strong>", f"{VR[p][0][0]} van {VR[p][0][1]}", oordeel24(p), f"{VR[p][1][0]} van {VR[p][1][1]}", oordeel8(p))
    for p in PT
])}
<ul><li><strong>Top 24 zeker:</strong> 8 punten of meer. Elke club met minstens 8 punten ging door. Dat zijn bijvoorbeeld twee zeges en twee gelijke spelen.</li><li><strong>Top 24 meestal genoeg:</strong> 7 punten. Van de {N7[1]} clubs met 7 punten overwinterden er {N7[0]}. Dan beslissen doelsaldo en doelpunten.</li><li><strong>Top 24 te weinig:</strong> 6 punten of minder. Geen enkele club met 6 punten haalde de tussenronde.</li><li><strong>Top 8 zeker:</strong> 12 punten of meer, bijvoorbeeld vier zeges uit zes duels.</li><li><strong>Top 8 meestal te weinig:</strong> 11 punten. Van de {VR[11][1][1]} clubs met 11 punten haalde er maar {VR[11][1][0]} de top 8.</li></ul>
<p>Met maar zes duels telt elke wedstrijd zwaarder, en is een slechte start lastiger goed te maken.</p>
<h3><strong>Welke tiebreakers gelden in de Conference League?</strong></h3>
<p>De volgorde is precies dezelfde als in de Champions League en de Europa League. Volgens het reglement van de UEFA voor 2026/27 kijk je bij gelijke punten na zes speelronden naar:</p>
<ol><li>Doelsaldo</li><li>Gescoorde doelpunten</li><li>Gescoorde uitdoelpunten</li><li>Aantal zeges</li><li>Aantal uitzeges</li><li>Totaal aantal punten van je tegenstanders</li><li>Doelsaldo van je tegenstanders</li><li>Doelpunten van je tegenstanders</li><li>Minste strafpunten voor kaarten (geel 1, rood of twee keer geel 3)</li><li>Clubcoëfficiënt</li></ol>
<p>Een onderling duel telt niet mee. In de Conference League vallen er per duel vaak weinig doelpunten, en dan beslist het tweede criterium sneller dan je denkt. Dat zag je in beide seizoenen bij plek 24.</p>
<h3><strong>Het schema van de Conference League 2026/27</strong></h3>
{tabel(["Ronde", "Datum (donderdag, tenzij anders vermeld)"], [
    ("Speelronde 1", "15 oktober 2026"),
    ("<strong>Speelronde 2</strong>", "<strong>22 oktober 2026</strong>"),
    ("Speelronde 3 en 4", "5 november en 26 november 2026"),
    ("Speelronde 5", "10 december 2026"),
    ("<strong>Speelronde 6</strong>", "<strong>17 december 2026</strong>, alle 18 duels om 21.00 uur"),
    ("Tussenronde", "18 en 25 februari 2027"),
    ("Achtste finales", "11 en 18 maart 2027"),
    ("Kwartfinales", "8 en 15 april 2027"),
    ("Halve finales", "29 april en 6 mei 2027"),
    ("Finale", "woensdag 2 juni 2027, Beşiktaş Stadion in Istanbul"),
])}
<p>De winnaar van de Conference League krijgt een plek in de league-fase van de Europa League 2027/28, als die club zich niet al via de eigen competitie voor de Champions League of Europa League heeft geplaatst.</p>"""

content3 = f"""<h3><strong>Hoe werkt de tussenronde van de Conference League?</strong></h3>
<p>Ook hier gaan de nummers 1 tot en met 8 direct naar de achtste finales en spelen de nummers 9 tot en met 24 eerst een tussenronde over twee duels. De nummers 9 tot en met 16 zijn geplaatst en spelen in principe de return thuis. De loting werkt met vaste paren:</p>
{tabel(["Geplaatst", "Loot tegen"], [
    ("Plek 9 of 10", "Plek 23 of 24"),
    ("Plek 11 of 12", "Plek 21 of 22"),
    ("Plek 13 of 14", "Plek 19 of 20"),
    ("Plek 15 of 16", "Plek 17 of 18"),
])}
<p>De top 8 speelt in de achtste finale de return thuis. In de kwartfinale hebben de nummers 1 tot en met 4 dat voordeel, in de halve finale de nummers 1 en 2.</p>
<h3><strong>Wat levert de eindplek op voor de coëfficiënt?</strong></h3>
<p>Voor de landenranking van de UEFA levert een zege 2 punten op en een gelijkspel 1 punt. Daarnaast zijn er bonuspunten voor je eindplek, maar die zijn in de Conference League kleiner dan in de andere twee toernooien.</p>
{tabel(["Eindplek", "Bonus voor de coëfficiënt"], [
    ("<strong>Plek 1</strong>", f"{nl(bonus(1))} punten"),
    ("<strong>Plek 8</strong>", f"{nl(bonus(8))} punten"),
    ("<strong>Plek 9</strong>", f"{nl(bonus(9))} punten"),
    ("<strong>Plek 24</strong>", f"{nl(bonus(24))} punt"),
    ("<strong>Plek 25 t/m 36</strong>", "geen bonus"),
    ("<strong>Elke knock-outronde vanaf de achtste finales</strong>", "+0,5 punt"),
])}
<p>Voorbeeld: AZ werd in 2025/26 veertiende en kreeg daarvoor {nl(bonus(14))} bonuspunten. Door de achtste finales en de kwartfinales te halen kwam daar 2 keer 0,5 bij. Samen {nl(AZ_BONUS)} bonuspunten, bovenop de punten voor zeges en gelijke spelen. Al die punten tellen mee voor de Nederlandse coëfficiënt: de punten van alle Nederlandse clubs in Europa worden opgeteld en gedeeld door het aantal clubs.</p>
<h3><strong>Hoe deden Nederlandse clubs het in de Conference League?</strong></h3>
{tabel(["Seizoen", "Club", "Punten", "Plek", "Afloop"], [
    ("2024/25", "Geen Nederlandse club", "-", "-", "-"),
    ("2025/26", '<a href="/clubs/az">AZ</a>', "10", "14e", "Won de tussenronde van FC Noah en de achtste finale van Sparta Praag, kwartfinale verloren van Sjachtar Donetsk"),
    ("2026/27", "FC Twente", "3 na 1 duel", "-", "1-0 winst op FC Thun, speelt op 22 oktober bij Lincoln Red Imps"),
    ("2026/27", "Ajax", "0 na 1 duel", "-", "2-1 verlies bij Hajduk Split, speelt op 22 oktober thuis tegen Atalanta"),
])}
<p>AZ liet vorig seizoen zien wat een plek tussen 9 en 16 waard is. Als veertiende speelde AZ de return van de tussenronde thuis: na een 1-0 nederlaag bij FC Noah won AZ in Alkmaar met 4-0. Daarna werd Sparta Praag, nummer 4 van de league-fase, over twee duels verslagen.</p>
<p>Met de vuistregel van 8 punten heeft Twente na de zege op Thun nog 5 punten nodig uit vijf duels. Ajax moet na de nederlaag in Split nog 8 punten halen uit vijf duels, bijvoorbeeld twee zeges en twee gelijke spelen.</p>
<h3><strong>Wedden op de Conference League</strong></h3>
<p>Met maar zes duels is de league-fase grillig. Bij een deel van de legale bookmakers vind je naast losse wedstrijden ook markten als "plaatst zich voor de knock-outfase" of de toernooiwinnaar. Kijk dan vooral naar het resterende programma en naar het doelsaldo, want bij 7 punten beslissen vaak een paar doelpunten. Vergelijk de odds en speel binnen je limieten. Hoe zulke weddenschappen werken, lees je in onze <a href="/wedgids">wedgids</a>.</p>
<p>Wil je weten hoe de grenzen liggen in de grotere toernooien? Lees <a href="{CL_ART}">hoeveel punten je nodig hebt om te overwinteren in de Champions League</a> en <a href="{EL_ART}">hoeveel punten je nodig hebt om te overwinteren in de Europa League</a>.</p>
<h3><strong>Veelgestelde vragen over overwinteren in de Conference League</strong></h3>
<p><strong>Hoeveel punten heb je nodig om te overwinteren in de Conference League?</strong><br>Meestal 7 à 8 punten. Met 8 punten of meer ging tot nu toe elke club door. In 2024/25 en 2025/26 had de nummer 24 precies 7 punten.</p>
<p><strong>Hoeveel punten heb je nodig voor de top 8 van de Conference League?</strong><br>Ongeveer 12 punten. De nummer 8 had 11 punten in 2024/25 en 12 punten in 2025/26.</p>
<p><strong>Hoeveel wedstrijden speel je in de league-fase van de Conference League?</strong><br>Zes: drie thuis en drie uit, tegen één tegenstander uit elk van de zes potten.</p>
<p><strong>Wanneer weet je of je overwintert in de Conference League?</strong><br>Na speelronde 6 op donderdag 17 december 2026, dus nog vóór de winterstop.</p>
<p><strong>Kun je vanuit de Conference League ergens naartoe afzakken?</strong><br>Nee. De nummers 25 tot en met 36 zijn uitgeschakeld. Er komen ook geen clubs meer bij uit de Europa League.</p>
<p><strong>Wat beslist bij gelijke punten?</strong><br>Eerst het doelsaldo, daarna het aantal gescoorde doelpunten. Dat tweede criterium besliste in beide seizoenen wie als 24e doorging.</p>
{KSA}"""

if __name__ == "__main__":
    html = content + content2 + content3
    assert not re.search(r"<(ul|ol|/li)>\s+<", html), "witruimte tussen lijsttags"
    assert "<h2" not in html and "/kennisbank/" not in html
    assert html.rstrip().endswith(KSA), "KSA-regel niet als laatste"
    assert len(TITEL) <= 65 and 120 <= len(SAMENVATTING) <= 155
    assert len(OG_CHIPS) == 2 and len(OG_DATA) == 4 and OG_MOTIEF == "tabel"
    assert CL_ART in html and EL_ART in html and "/wedgids" in html
    faq = len(re.findall(r"<p><strong>[^<]+\?</strong><br>", html))
    assert 5 <= faq <= 7, faq
    tekst = re.sub(r"<[^>]+>", " ", html)
    w = len(tekst.split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", w, "woorden |", faq, "faq |",
          len(content), len(content2), len(content3), "tekens per veld")
    assert 1300 <= w <= 2000, w
    print("Dry run: er is niets gepubliceerd.")
