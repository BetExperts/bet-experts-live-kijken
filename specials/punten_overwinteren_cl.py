# -*- coding: utf-8 -*-
"""Nieuw Nieuws-artikel: hoeveel punten heb je nodig om te overwinteren (top 24) en voor de top 8 in de
Champions League? Nieuwe league-fase sinds 2024/25.

Geverifieerd op 21-10-2026:
- Eindstanden league-fase 2024/25 en 2025/26: officiele UEFA-standen
  (standings.uefa.com/v1/standings?competitionId=1&seasonYear=2025 / 2026, status OFFICIAL).
- Tiebreakers: Reglement UEFA Champions League 2026/27, artikel 18.01 (in werking 29-07-2026).
- Tussenronde/achtste finales: zelfde reglement, artikel 19.02-19.04 (9/10-23/24, 11/12-21/22, 13/14-19/20,
  15/16-17/18; geplaatste club in principe thuis in de return; kwartfinale top 4, halve finale top 2 thuis in return).
- Data 2026/27: uefa.com (speelronde 1 8-10 sep ... speelronde 8 woensdag 27-01-2027, alle 18 duels om 21.00 uur;
  tussenronde 16/17 + 23/24 feb 2027; achtste finales 9/10 + 16/17 mrt 2027; finale 5 juni 2027 Madrid).
- Coefficient: reglement 2026/27 bijlage D.5 (league-fase 25-36: 6,000; 24e 6,250 ... 1e 12,000; per KO-ronde vanaf
  achtste finales 1,5) en UEFA-uitleg coefficienten (winst 2, gelijk 1).
- Nederlandse clubs 2026/27 na speelronde 3 (PSV) / 2 (Feyenoord): UEFA-wedstrijddata, 21-10-2026 20.30 uur.
  python3 specials/punten_overwinteren_cl.py   (alleen dry run)"""
import os, sys, re
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "hoeveel-punten-nodig-overwinteren-champions-league"
TITEL = "Hoeveel punten nodig om te overwinteren in de Champions League?"
SAMENVATTING = ("Hoeveel punten heb je nodig voor de top 24 en de top 8 van de Champions League? Met de echte grenzen "
                "van 2024/25 en 2025/26 en een vuistregel.")
RUBRIEK = "669fc3ef5bd43f5dfd4b9146"      # Champions League
COMPETITIE = "65de4adac046f4488dfdebc2"   # Champions League

# Deelkaart (maatwerk)
OG_KOP = "Hoeveel punten voor de <span>top 24</span>?"
OG_EYEBROW = "Champions League · league-fase"
OG_CHIPS = ["Top 8 · direct door", "Plek 25 · eruit"]
OG_MOTIEF = "tabel"
OG_DATA = ["Top 8 · 16 punten", "Top 24 · 10 à 11 punten", "2024/25 nr. 24 · 11 pnt", "2025/26 nr. 24 · 9 pnt"]

KSA = "<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"
CL = "/competities/champions-league"
FORMAT = ("/nieuws/champions-league-2025-uitleg-over-het-nieuwe-format-tussenronde-en-knock-outs-"
          "hoe-nu-verder-na-speelronde-8")
EL_ART = "/nieuws/hoeveel-punten-nodig-overwinteren-europa-league"

# Officiele eindstanden league-fase (plek, club, punten, doelsaldo, doelpunten voor) - UEFA, gelezen 21-10-2026
STAND = {
    "2024/25": [(1, 'Liverpool', 21, 12, 17), (2, 'Barcelona', 19, 15, 28), (3, 'Arsenal', 19, 13, 16), (4, 'Inter', 19, 10, 11), (5, 'Atlético Madrid', 18, 8, 20), (6, 'Bayer Leverkusen', 16, 8, 15), (7, 'Lille OSC', 16, 7, 17), (8, 'Aston Villa', 16, 7, 13), (9, 'Atalanta', 15, 14, 20), (10, 'Borussia Dortmund', 15, 10, 22), (11, 'Real Madrid', 15, 8, 20), (12, 'Bayern München', 15, 8, 20), (13, 'AC Milan', 15, 3, 14), (14, 'PSV', 14, 4, 16), (15, 'PSG', 13, 5, 14), (16, 'Benfica', 13, 4, 16), (17, 'AS Monaco', 13, 0, 13), (18, 'Stade Brest', 13, -1, 10), (19, 'Feyenoord', 13, -3, 18), (20, 'Juventus', 12, 2, 9), (21, 'Celtic', 12, -1, 13), (22, 'Manchester City', 11, 4, 18), (23, 'Sporting Portugal', 11, 1, 13), (24, 'Club Brugge', 11, -4, 7), (25, 'Dinamo Zagreb', 11, -7, 12), (26, 'VfB Stuttgart', 10, -4, 13), (27, 'Sjachtar Donetsk', 7, -8, 8), (28, 'Bologna', 6, -5, 4), (29, 'Rode Ster Belgrado', 6, -9, 13), (30, 'Sturm Graz', 6, -9, 5), (31, 'Sparta Praag', 4, -14, 7), (32, 'RB Leipzig', 3, -7, 8), (33, 'Girona', 3, -8, 5), (34, 'RB Salzburg', 3, -22, 5), (35, 'Slovan Bratislava', 0, -20, 7), (36, 'Young Boys', 0, -21, 3)],
    "2025/26": [(1, 'Arsenal', 24, 19, 23), (2, 'Bayern München', 21, 14, 22), (3, 'Liverpool', 18, 12, 20), (4, 'Tottenham', 17, 10, 17), (5, 'Barcelona', 16, 8, 22), (6, 'Chelsea', 16, 7, 17), (7, 'Sporting Portugal', 16, 6, 17), (8, 'Manchester City', 16, 6, 15), (9, 'Real Madrid', 15, 9, 21), (10, 'Inter', 15, 8, 15), (11, 'PSG', 14, 10, 21), (12, 'Newcastle', 14, 10, 17), (13, 'Juventus', 13, 4, 14), (14, 'Atlético Madrid', 13, 2, 17), (15, 'Atalanta', 13, 0, 10), (16, 'Bayer Leverkusen', 12, -1, 13), (17, 'Borussia Dortmund', 11, 2, 19), (18, 'Olympiacos', 11, -4, 10), (19, 'Club Brugge', 10, -2, 15), (20, 'Galatasaray', 10, -2, 9), (21, 'AS Monaco', 10, -6, 8), (22, 'Qarabağ', 10, -8, 13), (23, 'Bodø/Glimt', 9, -1, 14), (24, 'Benfica', 9, -2, 10), (25, 'Olympique Marseille', 9, -3, 11), (26, 'Pafos', 9, -3, 8), (27, 'Union Sint-Gillis', 9, -9, 8), (28, 'PSV', 8, 0, 16), (29, 'Athletic Bilbao', 8, -5, 9), (30, 'Napoli', 8, -6, 9), (31, 'FC Kopenhagen', 8, -9, 12), (32, 'Ajax', 6, -13, 8), (33, 'Eintracht Frankfurt', 4, -11, 10), (34, 'Slavia Praag', 3, -14, 5), (35, 'Villarreal', 1, -13, 5), (36, 'Kairat Almaty', 1, -15, 7)],
}
for s, rij in STAND.items():
    assert len(rij) == 36 and [r[0] for r in rij] == list(range(1, 37))
    assert all(a[2] >= b[2] for a, b in zip(rij, rij[1:])), s


def plek(seizoen, p):
    return STAND[seizoen][p - 1]


def sd(x):
    return f"+{x}" if x > 0 else str(x)


def telling(punten, grens, tot=None):
    """Hoeveel clubs met (punten t/m tot) eindigden in beide seizoenen bij de beste `grens`? -> (door, totaal)"""
    tot = punten if tot is None else tot
    rijen = [r for s in STAND for r in STAND[s] if punten <= r[2] <= tot]
    return sum(1 for r in rijen if r[0] <= grens), len(rijen)


def rij_grens(seizoen, p, wat):
    n, club, pt, d, g = plek(seizoen, p)
    return (f"<strong>Plek {p}</strong>", f"<strong>{pt} punten</strong> ({club})", f"{sd(d)} ({g} gescoord)", wat)


# Controles op de officiele standen
assert plek("2024/25", 8)[2] == 16 and plek("2024/25", 9)[2] == 15
assert plek("2024/25", 24)[1:3] == ("Club Brugge", 11) and plek("2024/25", 25)[1:3] == ("Dinamo Zagreb", 11)
assert plek("2025/26", 8)[2] == 16 and plek("2025/26", 9)[2] == 15
assert plek("2025/26", 24)[1:3] == ("Benfica", 9) and plek("2025/26", 25)[1:3] == ("Olympique Marseille", 9)
# Benfica - Real Madrid 4-2 (28-01-2026), 4-2 van Trubin in 90+8: zonder die goal 9-12 (-3, 9 goals) -> onder Marseille (-3, 11)
assert (plek("2025/26", 24)[3] - 1, plek("2025/26", 24)[4] - 1) < (plek("2025/26", 25)[3], plek("2025/26", 25)[4])
# Real Madrid en Bayern 2024/25: gelijk op punten, doelsaldo en goals; uitgoals 6-6, zeges 5-5, uitzeges 2-1
assert plek("2024/25", 11)[2:] == plek("2024/25", 12)[2:]

T24 = {p: telling(p, 24) for p in (9, 10, 11)}
T24_12 = telling(12, 24, 99)
T24_8 = telling(0, 24, 8)
T8 = {p: telling(p, 8) for p in (14, 15, 16)}
T8_17 = telling(17, 8, 99)
assert T24 == {9: (2, 5), 10: (4, 5), 11: (5, 6)} and T24_12[0] == T24_12[1] and T24_8[0] == 0
assert T8 == {14: (0, 3), 15: (0, 7), 16: (7, 7)} and T8_17[0] == T8_17[1]


def uit(t):
    return f"{t[0]} van de {t[1]}"


# Coefficient-bonus (bijlage D.5): plek 25-36 6,000; vanaf plek 24 telkens +0,25 tot 12,000 voor plek 1
def bonus(p):
    return 6.0 if p >= 25 else 6.0 + (25 - p) * 0.25


assert bonus(1) == 12 and bonus(8) == 10.25 and bonus(9) == 10 and bonus(24) == 6.25 and bonus(25) == 6


def nl(x):
    return f"{x:.2f}".rstrip("0").rstrip(".").replace(".", ",")


content = f"""<p><strong>Om te overwinteren in de Champions League, dus om bij de beste 24 te eindigen, heb je in de nieuwe league-fase meestal 10 à 11 punten nodig. Met 12 punten of meer ging tot nu toe elke club door. Met 9 punten is het een gok op doelsaldo. Voor de top 8, en dus een rechtstreeks ticket voor de achtste finales, heb je ongeveer 16 punten nodig.</strong></p>
<p>Die getallen komen uit de officiële eindstanden van de eerste twee seizoenen met het nieuwe format: 2024/25 en 2025/26. Hieronder zie je per seizoen de punten van de nummers 8, 9, 24 en 25 en welke tiebreakers beslisten. De <a href="{CL}">Champions League</a> 2026/27 zit nu in speelronde 3. De beslissing valt op 27 januari 2027.</p>
<h3><strong>Bestaat overwinteren in de Champions League nog?</strong></h3>
<p>Officieel niet meer zoals vroeger. In het oude format speelde je zes duels in een poule van vier. Half december wist je waar je stond: de nummers 1 en 2 gingen naar de achtste finales, de nummer 3 zakte af naar de Europa League. Ook dat telde als overwinteren, want je speelde in februari nog Europees voetbal.</p>
<p>Sinds 2024/25 zijn er geen poules meer. Alle 36 clubs staan in één ranglijst, de league-fase. Die loopt door tot eind januari. Je weet dus pas na speelronde 8 of je overwintert. Afzakken naar de Europa League bestaat niet meer: wie als 25e of lager eindigt, is klaar in Europa.</p>
<p>Met overwinteren bedoelen we nu daarom: <strong>bij de beste 24 eindigen</strong> en na de winter nog meedoen. Grappig detail: de top 8 speelt in februari juist níet, want die clubs slaan de tussenronde over.</p>
<h3><strong>Hoe werkt de league-fase van de Champions League?</strong></h3>
<p>Elke club speelt <strong>8 wedstrijden tegen 8 verschillende tegenstanders</strong>, uit vier potten: twee per pot, één thuis en één uit. Clubs uit je eigen land kom je niet tegen. Een zege levert 3 punten op, dus het maximum is 24 punten.</p>
{tabel(["Eindplek", "Wat betekent het?"], [
    ("<strong>1 t/m 8</strong>", "Direct naar de achtste finales. Geen wedstrijden in februari, de return van de achtste finale thuis."),
    ("<strong>9 t/m 24</strong>", "Tussenronde (knock-out play-offs) in februari, over twee wedstrijden. De winnaar gaat naar de achtste finales."),
    ("<strong>25 t/m 36</strong>", "Uitgeschakeld. Geen plek in de Europa League of Conference League."),
])}
<h3><strong>Hoeveel punten had je nodig in 2024/25?</strong></h3>
<p>In het eerste seizoen met het nieuwe format lag de grens voor de top 24 op 11 punten. Maar 11 punten was niet genoeg voor iedereen. Vier clubs eindigden op 11 punten: Manchester City, Sporting Portugal en Club Brugge gingen door, Dinamo Zagreb viel als 25e af op doelsaldo.</p>
{tabel(["Plek", "Punten (club)", "Doelsaldo", "Gevolg"], [
    rij_grens("2024/25", 8, "Laatste club in de top 8"),
    rij_grens("2024/25", 9, "Eerste club in de tussenronde"),
    rij_grens("2024/25", 24, "Laatste club in de tussenronde"),
    rij_grens("2024/25", 25, "Eerste club die uitgeschakeld is"),
])}
<p>Voor de top 8 had je in 2024/25 precies 16 punten nodig: Bayer Leverkusen, Lille en Aston Villa eindigden daarmee op 6, 7 en 8. Daaronder stonden vijf clubs met 15 punten, met Atalanta (doelsaldo +{plek("2024/25", 9)[3]}) als pechvogel op plek 9.</p>
<p>Opvallend: Real Madrid en Bayern München eindigden gelijk op punten (15), doelsaldo (+8), doelpunten (20) en uitdoelpunten (6). Ook het aantal zeges was gelijk (5). Pas het vijfde criterium, het aantal uitzeges, gaf de doorslag: Real Madrid 2, Bayern 1.</p>
<h3><strong>Hoeveel punten had je nodig in 2025/26?</strong></h3>
<p>Vorig seizoen lag de grens voor de top 24 lager: 9 punten. Vijf clubs eindigden op 9 punten. Alleen Bodø/Glimt en Benfica gingen door. Olympique Marseille, Pafos en Union Sint-Gillis vielen af.</p>
{tabel(["Plek", "Punten (club)", "Doelsaldo", "Gevolg"], [
    rij_grens("2025/26", 8, "Laatste club in de top 8"),
    rij_grens("2025/26", 9, "Eerste club in de tussenronde"),
    rij_grens("2025/26", 24, "Laatste club in de tussenronde"),
    rij_grens("2025/26", 25, "Eerste club die uitgeschakeld is"),
])}
<p>Het scheelde één doelpunt. Benfica won op de laatste avond met 4-2 van Real Madrid, en die 4-2 maakte doelman Anatoliy Trubin diep in blessuretijd. Zonder die goal had Benfica net als Marseille een doelsaldo van -3 gehad, en was Marseille op meer gescoorde doelpunten (11) doorgegaan.</p>
<p>Ook voor de top 8 was het opnieuw 16 punten. Barcelona, Chelsea, Sporting Portugal en Manchester City eindigden op 16 punten en de plekken 5 tot en met 8. Real Madrid en Inter strandden met 15 punten op 9 en 10.</p>"""

content2 = f"""<h3><strong>Vuistregel: hoeveel punten heb je nodig voor de top 24?</strong></h3>
<p>Zo vaak eindigden clubs met een bepaald aantal punten in de twee seizoenen bij de beste 24:</p>
{tabel(["Punten na 8 duels", "Bij de beste 24 (2024/25 + 2025/26)", "Oordeel"], [
    ("<strong>12 of meer</strong>", f"{uit(T24_12)} clubs", "<strong>Zeker</strong>"),
    ("<strong>11</strong>", f"{uit(T24[11])} clubs", "Meestal genoeg"),
    ("<strong>10</strong>", f"{uit(T24[10])} clubs", "Meestal genoeg"),
    ("<strong>9</strong>", f"{uit(T24[9])} clubs", "Gok, doelsaldo beslist"),
    ("<strong>8 of minder</strong>", f"{uit(T24_8)} clubs", "<strong>Te weinig</strong>"),
])}
<p>Kort gezegd: <strong>met 10 of 11 punten ben je er bijna altijd, met 12 punten ben je zeker.</strong> Tien punten haal je bijvoorbeeld met drie zeges en één gelijkspel. Met 9 punten, bijvoorbeeld drie zeges en vijf nederlagen, hangt alles af van je doelsaldo en van de uitslagen op andere velden.</p>
<h3><strong>Hoeveel punten heb je nodig voor de top 8?</strong></h3>
{tabel(["Punten na 8 duels", "In de top 8 (2024/25 + 2025/26)", "Oordeel"], [
    ("<strong>17 of meer</strong>", f"{uit(T8_17)} clubs", "<strong>Zeker</strong>"),
    ("<strong>16</strong>", f"{uit(T8[16])} clubs", "Tot nu toe altijd genoeg"),
    ("<strong>15</strong>", f"{uit(T8[15])} clubs", "<strong>Te weinig</strong>"),
    ("<strong>14</strong>", f"{uit(T8[14])} clubs", "Te weinig"),
])}
<p>De grens voor de top 8 lag in beide seizoenen precies op 16 punten, bijvoorbeeld vijf zeges en één gelijkspel. Met 15 punten werd je twee keer de nummer 9. Houd er rekening mee dat het ooit 17 punten kan worden.</p>
<h3><strong>Wanneer weet je of je overwintert? Het schema van 2026/27</strong></h3>
{tabel(["Ronde", "Datum"], [
    ("Speelronde 1 t/m 3", "8-10 september, 13/14 oktober en <strong>20/21 oktober 2026</strong>"),
    ("Speelronde 4 t/m 6", "3/4 november, 24/25 november en 8/9 december 2026"),
    ("Speelronde 7", "19/20 januari 2027"),
    ("<strong>Speelronde 8</strong>", "<strong>woensdag 27 januari 2027</strong>, alle 18 duels tegelijk om 21.00 uur"),
    ("Tussenronde", "16/17 en 23/24 februari 2027"),
    ("Achtste finales", "9/10 en 16/17 maart 2027"),
    ("Finale", "zaterdag 5 juni 2027, Estadio Metropolitano in Madrid"),
])}
<p>Op de laatste avond kan de stand rond de grens per doelpunt veranderen. Aan het format verandert dit seizoen niets: de grenzen 8 en 24 en de opzet van de tussenronde zijn hetzelfde als vorig jaar.</p>
<h3><strong>Wat als clubs gelijk eindigen? De tiebreakers</strong></h3>
<p>Eindigen clubs na speelronde 8 gelijk op punten, dan kijkt de UEFA volgens het reglement van 2026/27 naar deze criteria, in deze volgorde:</p>
<ol><li><strong>Doelsaldo</strong> in de league-fase</li><li><strong>Aantal gescoorde doelpunten</strong></li><li><strong>Aantal uitdoelpunten</strong></li><li><strong>Aantal zeges</strong></li><li><strong>Aantal uitzeges</strong></li><li><strong>Punten van alle tegenstanders</strong> samen</li><li><strong>Doelsaldo van alle tegenstanders</strong> samen</li><li><strong>Doelpunten van alle tegenstanders</strong> samen</li><li><strong>Fair play:</strong> minste strafpunten (gele kaart 1, rode kaart 3, twee keer geel in één duel 3)</li><li><strong>Clubcoëfficiënt</strong> van de UEFA</li></ol>
<p>Een onderling resultaat telt niet mee, want niet iedereen speelt tegen elkaar. In de praktijk beslist bijna altijd het doelsaldo.</p>"""

content3 = f"""<h3><strong>Hoe werkt de tussenronde van de Champions League?</strong></h3>
<p>De clubs op de plekken 9 tot en met 16 zijn in de tussenronde geplaatst, de clubs op 17 tot en met 24 niet. Een geplaatste club speelt in principe de return thuis. De loting werkt met vaste paren, zodat je eindplek bepaalt tegen wie je kunt loten:</p>
{tabel(["Geplaatst (9-16)", "Tegen (17-24)", "Winnaar treft in de achtste finale"], [
    ("Plek 9 of 10", "Plek 23 of 24", "Plek 7 of 8"),
    ("Plek 11 of 12", "Plek 21 of 22", "Plek 5 of 6"),
    ("Plek 13 of 14", "Plek 19 of 20", "Plek 3 of 4"),
    ("Plek 15 of 16", "Plek 17 of 18", "Plek 1 of 2"),
])}
<p>Wie bij de top 8 eindigt, speelt in de achtste finale de return thuis. Ook later telt je eindplek: in de kwartfinale spelen de nummers 1 tot en met 4 de return thuis, in de halve finale de nummers 1 en 2.</p>
<h3><strong>Waarom elk punt telt voor Nederland: de coëfficiënt</strong></h3>
<p>Voor de landenranking van de UEFA levert een zege in de league-fase 2 punten op en een gelijkspel 1 punt. Daarbovenop komen bonuspunten voor je eindplek. In de Champions League krijgt elke club in de league-fase minimaal {nl(bonus(25))} bonuspunten. Vanaf plek 24 komt daar per plek 0,25 bij.</p>
{tabel(["Eindplek", "Bonus voor de coëfficiënt"], [
    ("<strong>Plek 1</strong>", f"{nl(bonus(1))} punten"),
    ("<strong>Plek 8</strong>", f"{nl(bonus(8))} punten"),
    ("<strong>Plek 9</strong>", f"{nl(bonus(9))} punten"),
    ("<strong>Plek 24</strong>", f"{nl(bonus(24))} punten"),
    ("<strong>Plek 25 t/m 36</strong>", f"{nl(bonus(25))} punten"),
    ("<strong>Elke knock-outronde vanaf de achtste finales</strong>", "+1,5 punt"),
])}
<p>De punten van alle Nederlandse clubs in Europa worden opgeteld en gedeeld door het aantal clubs. Een goede Champions League-campagne helpt dus het hele land aan betere Europese tickets, en levert de club zelf veel meer prijzengeld op dan de Europa League.</p>
<h3><strong>Hoe deden Nederlandse clubs het in de league-fase?</strong></h3>
{tabel(["Seizoen", "Club", "Punten", "Eindplek", "Afloop"], [
    ("2024/25", '<a href="/clubs/psv">PSV</a>', "14", "14e", "Won de tussenronde van Juventus, verloor in de achtste finale van Arsenal"),
    ("2024/25", '<a href="/clubs/feyenoord">Feyenoord</a>', "13", "19e", "Won de tussenronde van AC Milan, verloor in de achtste finale van Inter"),
    ("2025/26", "PSV", "8", "28e", "Uitgeschakeld, één punt te weinig"),
    ("2025/26", '<a href="/clubs/ajax">Ajax</a>', "6", "32e", "Uitgeschakeld"),
])}
<p>In 2024/25 haalden PSV en Feyenoord allebei de laatste 16. Vorig seizoen bleef PSV steken op 8 punten en een doelsaldo van 0. Met 9 punten had PSV op doelsaldo boven alle clubs met 9 punten gestaan.</p>
<p>Dit seizoen spelen PSV en Feyenoord weer in de Champions League. PSV heeft na drie duels 4 punten: 1-1 tegen Sjachtar Donetsk, 1-0 verlies bij RB Leipzig en een 0-1 zege bij FC Porto. Feyenoord had na twee duels 3 punten (5-1 verlies bij Barcelona, 3-2 winst op Como) en speelt op woensdag 21 oktober bij Real Betis. Met de vuistregel in je achterhoofd heeft PSV na speelronde 3 nog zo'n 6 à 7 punten nodig uit vijf duels.</p>
<h3><strong>Wedden op de top 8 en de top 24</strong></h3>
<p>Bij een deel van de legale bookmakers kun je ook op de eindstand wedden, met markten als "eindigt in de top 8: ja of nee" of de toernooiwinnaar. Kijk dan vooral naar het resterende programma: welke tegenstanders en hoeveel thuisduels komen er nog? Met de grenzen van 16 en 10 à 11 punten schat je de kans realistischer in. Vergelijk de odds en speel binnen je limieten. Meer uitleg over soorten weddenschappen vind je in onze <a href="/wedgids">wedgids</a>. Hoe de knock-outfase precies verloopt, lees je in onze <a href="{FORMAT}">uitleg over het nieuwe format en de tussenronde</a>. En in de Europa League liggen de grenzen weer net anders: lees <a href="{EL_ART}">hoeveel punten je nodig hebt om te overwinteren in de Europa League</a>.</p>
<h3><strong>Veelgestelde vragen over overwinteren in de Champions League</strong></h3>
<p><strong>Hoeveel punten heb je nodig om te overwinteren in de Champions League?</strong><br>Voor de top 24 meestal 10 à 11 punten. De nummer 24 had 11 punten (2024/25) en 9 punten (2025/26).</p>
<p><strong>Hoeveel punten heb je nodig voor de top 8 van de Champions League?</strong><br>Ongeveer 16 punten. In 2024/25 en 2025/26 had de nummer 8 precies 16 punten en de nummer 9 precies 15.</p>
<p><strong>Kun je nog afzakken naar de Europa League?</strong><br>Nee. Sinds 2024/25 is de Champions League voorbij voor de nummers 25 tot en met 36. Zij stromen niet meer door naar de Europa League of de Conference League.</p>
<p><strong>Wanneer is de laatste speelronde van de league-fase?</strong><br>Speelronde 8 is op woensdag 27 januari 2027. Alle 18 wedstrijden beginnen tegelijk om 21.00 uur.</p>
<p><strong>Wat telt als eerste bij gelijke punten?</strong><br>Het doelsaldo, daarna het aantal gescoorde doelpunten en uitdoelpunten.</p>
<p><strong>Wanneer is de tussenronde?</strong><br>Op 16/17 en 23/24 februari 2027. De geplaatste clubs (plek 9 tot en met 16) spelen in principe de return thuis.</p>
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
    assert 1300 <= w <= 2000, w
    print("Dry run: er is niets gepubliceerd.")
