# -*- coding: utf-8 -*-
"""Los artikel: NBA voorspellingen vannacht, nacht van woensdag 28 op donderdag 29 oktober 2026 (12 wedstrijden).
Feiten nagelopen op 28-10-2026 (±11:00-12:00 NL): specials/nba_feiten_2026_10_29.md (ESPN-scoreboards, summaries,
box scores 2026/27; blessures ESPN ±10:45 NL en opnieuw gecontroleerd ±12:00 NL; TOTO-odds ±10:50 NL, wedstrijdpagina's).
- 4 toppers hebben een eigen voorbeschouwing (pacers_76ers, bucks_rockets, mavericks_thunder, clippers_lakers).
  De tips hier sluiten daarop aan (Over 228,5, Bucks +8,5, Thunder -4,5); 76ers -4,5 staat alleen in de voorbeschouwing.
- 4 beste tips (vast, eigenaar): Warriors +3,5 (57/51,0), Over 228,5 Clippers – Lakers (56/50,8), Bucks +8,5 (56/51,0),
  Thunder -4,5 (60/54,2). Geen unders (eigenaar).
- Vorige nacht (voorbeschouwingen 28 oktober): 3 van 4 raak (Nets +11,5, Over 230,5 Spurs – Kings en Over 236,5
  Lakers – Blazers wel, Pistons +3,5 niet).
- Back-to-back: Detroit, New York, San Antonio en de Lakers speelden dinsdag (US) ook.
- Extra (ESPN-box scores): Edwards 47 ptn in de verloren OT-wedstrijd in Cleveland; Lendeborg 31 ptn/12 reb in Denver;
  MIN-gemiddelden McDaniels 15,0, Ball 14,8/6,2 ast, Gobert 14,2 reb; Malevy Leons (GS) en Tristan Enaruna (CLE) in de selectie.
  python3 specials/nba_vannacht_2026_10_29.py   (alleen dry run, publiceert niets)
  publiceren: specials/nba_vannacht_publiceer.py nba_vannacht_2026_10_29 --live"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "nba-voorspellingen-vannacht-29-oktober-2026"
RUBRIEK = "672293e14a76d88272bc0b61"   # Basketball
TITEL = "NBA voorspellingen vannacht: 4 beste wedtips (29 oktober)"
SAMENVATTING = ("Twaalf NBA-wedstrijden vannacht: speeltijden in Nederlandse tijd, korte voorbeschouwing per duel, "
                "onze 4 beste tips en de vier toppers.")
DATUM = "2026-10-28T23:00:00.000Z"     # eerste wedstrijden: donderdag 00:00 NL

OG_KOP = "NBA <span>voorspellingen</span> vannacht"
OG_EYEBROW = "Basketbal · 29 oktober"
OG_CHIPS = ["12 wedstrijden", "4 beste tips"]
OG_MOTIEF = "tabel"
OG_DATA = ["MIN-GSW · Warriors +3,5 @1,87", "LAC-LAL · Over 228,5 @1,87", "MIL-HOU · Bucks +8,5 @1,87",
           "DAL-OKC · Thunder -4,5 @1,69"]

NAMEN = ["Warriors profiteren zonder Edwards!", "Dončić zorgt weer voor punten!", "Bucks houden het spannend!",
         "Thunder blijven ongeslagen!"]
STAKE = [4, 4, 3, 3]

L = {"ind": '<a href="/nieuws/pacers-76ers-voorspelling-wedtips-nba-2026">Pacers – 76ers</a>',
     "mil": '<a href="/nieuws/bucks-rockets-voorspelling-wedtips-nba-2026">Bucks – Rockets</a>',
     "dal": '<a href="/nieuws/mavericks-thunder-voorspelling-wedtips-nba-2026">Mavericks – Thunder</a>',
     "lac": '<a href="/nieuws/clippers-lakers-voorspelling-wedtips-nba-2026">Clippers – Lakers</a>'}

# (tijd NL, thuis, uit, odd thuis, odd uit)  TOTO 'Winnaar' (incl. verlenging), 28-10 ±10:50
PROGRAMMA = [
    ("00:00", "Atlanta Hawks", "Miami Heat", 1.67, 2.30),
    ("00:00", "Cleveland Cavaliers", "Washington Wizards", 1.26, 4.00),
    ("00:00", "Detroit Pistons", "Charlotte Hornets", 1.41, 2.95),
    ("00:00", "Indiana Pacers", "Philadelphia 76ers", 2.55, 1.54),
    ("00:30", "Toronto Raptors", "Orlando Magic", 1.56, 2.50),
    ("01:00", "Chicago Bulls", "New York Knicks", 3.10, 1.38),
    ("01:00", "Milwaukee Bucks", "Houston Rockets", 3.65, 1.30),
    ("01:00", "Minnesota Timberwolves", "Golden State Warriors", 1.69, 2.25),
    ("01:00", "New Orleans Pelicans", "Denver Nuggets", 2.60, 1.53),
    ("02:00", "Utah Jazz", "San Antonio Spurs", 5.50, 1.17),
    ("02:30", "Dallas Mavericks", "Oklahoma City Thunder", 2.75, 1.48),
    ("03:30", "Los Angeles Clippers", "Los Angeles Lakers", 2.55, 1.54),
]


def q(x):
    return f"{x:.2f}".replace(".", ",")


def fav(t, u, ot, ou):
    if ot == ou:
        return f"Gelijk ({q(ot)} – {q(ou)})"
    return f"{t} ({q(ot)})" if ot < ou else f"{u} ({q(ou)})"


assert len(PROGRAMMA) == 12

TIPS = [
    {"wedstrijd": "Minnesota Timberwolves vs. Golden State Warriors", "competitie": "NBA", "speeltijd_utc": "2026-10-29T00:00:00Z",
     "tijd_nl": "01:00", "tip": "Golden State Warriors +3,5 (handicap incl. verlenging)", "odds": "1.87", "bookmaker": "toto",
     "analyse": "Minnesota mist Anthony Edwards (33,2 punten per duel); Golden State won zijn laatste wedstrijd met 134-114 in Denver."},
    {"wedstrijd": "Los Angeles Clippers vs. Los Angeles Lakers", "competitie": "NBA", "speeltijd_utc": "2026-10-29T02:30:00Z",
     "tijd_nl": "03:30", "tip": "Meer dan 228,5 punten (incl. verlenging)", "odds": "1.87", "bookmaker": "toto",
     "analyse": "Alle vier Lakers-duels gingen erover: 232, 242, 255 en 265 punten. Het eerste stadsduel eindigde 125-117."},
    {"wedstrijd": "Milwaukee Bucks vs. Houston Rockets", "competitie": "NBA", "speeltijd_utc": "2026-10-29T00:00:00Z",
     "tijd_nl": "01:00", "tip": "Milwaukee Bucks +8,5 (handicap incl. verlenging)", "odds": "1.87", "bookmaker": "toto",
     "analyse": "Houston mist Alperen Şengün (24,5 punten, 9 rebounds, 7 assists) en Steven Adams; Milwaukee won zijn laatste duel."},
    {"wedstrijd": "Dallas Mavericks vs. Oklahoma City Thunder", "competitie": "NBA", "speeltijd_utc": "2026-10-29T01:30:00Z",
     "tijd_nl": "02:30", "tip": "Oklahoma City Thunder -4,5 (handicap incl. verlenging)", "odds": "1.69", "bookmaker": "toto",
     "analyse": "De Thunder wonnen alle vier hun duels met minstens zeven punten verschil; Dallas verloor zijn enige thuisduel met 106-122."},
]

content = f"""<p><strong>In de nacht van woensdag op donderdag staan er twaalf NBA-wedstrijden op het programma, van 00:00 tot 03:30 Nederlandse tijd. Toppers zijn de stadsderby tussen de Clippers en de Lakers van Luka Dončić, het ongeslagen Oklahoma City in Dallas tegen Cooper Flagg, de ongeslagen Rockets zonder Alperen Şengün in Milwaukee en Golden State in Minnesota, waar Anthony Edwards ontbreekt. Onze vier beste voorspellingen: Golden State Warriors +3,5, meer dan 228,5 punten bij Clippers – Lakers, Milwaukee Bucks +8,5 en Oklahoma City Thunder -4,5.</strong></p>
<p>In onze voorbeschouwingen van vorige nacht kwamen drie van de vier tips uit. Brooklyn verloor pas na verlenging met 124-125 in Boston, dus Nets +11,5 was raak (<a href="/nieuws/celtics-nets-voorspelling-wedtips-nba-2026">Celtics – Nets</a>). Ook meer dan 230,5 punten bij <a href="/nieuws/spurs-kings-voorspelling-wedtips-nba-2026">Spurs – Kings</a> (130-103, samen 233) en meer dan 236,5 punten bij <a href="/nieuws/lakers-trail-blazers-voorspelling-wedtips-nba-2026">Lakers – Trail Blazers</a> (129-136, samen 265) kwamen uit. Pistons +3,5 ging mis: Detroit verloor met 97-111 in New York (<a href="/nieuws/knicks-pistons-voorspelling-wedtips-nba-2026">Knicks – Pistons</a>). Ook vannacht kiezen we per wedstrijd maar één markt, alleen waar onze eigen inschatting hoger ligt dan de kans in de odd. Let op de vermoeidheid: Detroit, New York, San Antonio en de Lakers speelden dinsdagavond (Amerikaanse tijd) ook al en staan dus de tweede avond op rij op de vloer. Voor de vier grootste wedstrijden hebben we een uitgebreide voorbeschouwing geschreven.</p>
<p><strong>Kijken?</strong> Heb je een account bij <a href="/bookmakers/bet365">Bet365</a>, dan kun je NBA-wedstrijden daar live streamen. In Nederland zendt ESPN een deel van de NBA-wedstrijden uit en met NBA League Pass, de betaalde dienst van de competitie, zie je ze allemaal. Meer opties lees je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<h3><strong>Het NBA-programma van vannacht (Nederlandse tijd)</strong></h3>
{tabel(["Tijd", "Wedstrijd", "Favoriet volgens de markt"], [
    (f"<strong>{t}</strong>", f"{h} – {u}", fav(h, u, oh, ou)) for t, h, u, oh, ou in PROGRAMMA
])}
<p><em>Alle wedstrijden beginnen in de nacht van woensdag op donderdag 29 oktober. Odds: TOTO, markt Winnaar (inclusief verlenging), stand woensdag 28 oktober rond 10:50. Odds kunnen tot de start nog veranderen.</em></p>
<h3><strong>De 4 beste NBA-voorspellingen van vannacht</strong></h3>
{tabel(["Wedstrijd", "Tip", "Odd", "Markt"], [
    ("Timberwolves – Warriors (01:00)", "<strong>Warriors +3,5</strong>", "1,87", "Handicap, incl. verlenging"),
    ("Clippers – Lakers (03:30)", "<strong>Meer dan 228,5 punten</strong>", "1,87", "Totaal, incl. verlenging"),
    ("Bucks – Rockets (01:00)", "<strong>Bucks +8,5</strong>", "1,87", "Handicap, incl. verlenging"),
    ("Mavericks – Thunder (02:30)", "<strong>Thunder -4,5</strong>", "1,69", "Handicap, incl. verlenging"),
])}
<p><em>Alle odds bij <a href="/bookmakers/toto">TOTO</a>, gelezen op woensdag 28 oktober rond 10:50. Losse tips, geen combinatie: elke tip staat op zichzelf.</em></p>
<h3><strong>1. Minnesota Timberwolves – Golden State Warriors: Warriors +3,5 (1,87)</strong></h3>
<p>Minnesota begon met drie ruime zeges (131-106 in Miami, 115-93 in Orlando en 117-94 tegen Toronto) en verloor daarna pas na verlenging met 125-127 in Cleveland, ondanks 47 punten van Anthony Edwards. Juist Edwards ontbreekt nu met een knieblessure, en ook Donte DiVincenzo is er niet bij. Dat is een flinke aderlating: Edwards maakte gemiddeld 33,2 punten, ruim twee keer zoveel als de nummer twee, Jaden McDaniels (15,0). LaMelo Ball (14,8 punten, 6,2 assists) en Terrence Shannon Jr. moeten het gat vullen. Golden State staat op 1-3, maar won zijn laatste wedstrijd met 134-114 in Denver. Yaxel Lendeborg maakte daar 31 punten en 12 rebounds en Stephen Curry scoort 23,7 punten per wedstrijd. De Warriors missen wel Kristaps Porziņģis, Moses Moody en Jimmy Butler, en achter Lendeborg (voet) staat een vraagteken. Beide ploegen hadden dinsdag rust. TOTO maakt Minnesota favoriet met 1,69. Met +3,5 is de tip ook goed als Golden State met maximaal drie punten verliest. De odd staat voor een kans van 51 procent zonder marge; wij schatten die op 57 procent. Het risico: Rudy Gobert (14,2 rebounds per duel) heerst onder de ring, en als Lendeborg niet kan spelen, wordt het dun bij Golden State.</p>
<h3><strong>2. Los Angeles Clippers – Los Angeles Lakers: meer dan 228,5 punten (1,87)</strong></h3>
<p>Wedstrijden van de Lakers leveren veel punten op. Hun vier duels eindigden op 232, 242, 255 en 265 punten: steeds meer dan 228,5. Luka Dončić scoort gemiddeld 36,0 punten (52 in Utah, 41 tegen Portland) en Austin Reaves 26,5. Verdedigend gaat het minder: dinsdag kreeg Los Angeles thuis 136 punten tegen van Portland. Het eerste stadsduel, vorige week, eindigde 125-117 voor de Lakers, samen 242 punten. De Clippers spelen behoudender (hun duels eindigden op 217, 242 en 209 punten) en missen Rui Hachimura, Bradley Beal, Max Strus en Brandon Ingram. Darius Garland (24,0 punten, 7,0 assists) en Brook Lopez (18,0) moeten de punten maken. De odd voor meer dan 228,5 punten staat voor 51 procent zonder marge; wij schatten de kans op 56 procent. Een verlenging telt mee, wat in ons voordeel werkt. Het risico: de Lakers spelen de tweede avond op rij, wat het tempo kan drukken, en de Clippers missen veel scorend vermogen. Alles over dit duel lees je in onze voorbeschouwing van {L['lac']}.</p>
<h3><strong>3. Milwaukee Bucks – Houston Rockets: Bucks +8,5 (1,87)</strong></h3>
<p>Houston is met 4-0 een van de ongeslagen ploegen, maar moet het vannacht zonder Alperen Şengün (rug) doen. De Turkse center is de motor van de ploeg: 24,5 punten, 9 rebounds en 7 assists per wedstrijd. Ook Steven Adams ontbreekt en achter Marcus Smart staat een vraagteken. Kevin Durant (23,5 punten), Amen Thompson (17,0 punten, 9 rebounds) en Jabari Smith Jr. dragen de last. De vier zeges van Houston kwamen tot stand met 18, 4, 7 en 10 punten verschil: twee keer was het verschil kleiner dan negen punten, en dat was mét Şengün. Milwaukee staat op 1-3, maar won zijn laatste wedstrijd met 110-102 van Indiana. Tyler Herro (23,5 punten) is de leider, Kel'el Ware pakte in dat duel 14 rebounds. De Bucks hebben geen blessures en beide ploegen hadden dinsdag rust. De odd staat voor 51 procent zonder marge, wij schatten de kans op 56 procent. Het risico: Milwaukee kreeg gemiddeld 122,2 punten tegen en verloor drie keer met 7 tot 12 punten verschil. Lees alles in {L['mil']}.</p>
<h3><strong>4. Dallas Mavericks – Oklahoma City Thunder: Thunder -4,5 (1,69)</strong></h3>
<p>Oklahoma City is ongeslagen en won alle vier de wedstrijden met minstens zeven punten verschil: 116-104 in San Antonio, 96-84 tegen Denver, 108-101 tegen de Clippers en 125-114 tegen Phoenix. De Thunder kregen gemiddeld maar 100,8 punten tegen. Shai Gilgeous-Alexander scoort 27,2 punten per wedstrijd. Toch is de selectie flink uitgedund: Chet Holmgren (knie), Jalen Williams (enkel), Cason Wallace (schouder) en Alex Caruso (enkel) ontbreken, en achter Ajay Mitchell (16,0 punten, 30 tegen Phoenix) staat een vraagteken. Maandag won Oklahoma City zonder drie basisspelers nog met 125-114 van Phoenix. Dallas staat op 2-2 en verloor zijn enige thuiswedstrijd met 106-122 van San Antonio. Cooper Flagg (25,0 punten, 6,3 assists) en Kyrie Irving (19,0) zijn de gevaarlijkste namen; Santi Aldama en Caleb Martin zijn er niet bij en Naji Marshall is ziek. Met 1,69 is dit de laagste odd van onze vier tips. De odd staat voor 54 procent zonder marge; wij schatten de kans op een zege met minstens vijf punten op 60 procent. Het risico: zonder Holmgren en Caruso is de Thunder-verdediging kwetsbaarder. Meer in onze voorbeschouwing van {L['dal']}.</p>"""

content2 = f"""<h3><strong>Alle wedstrijden van vannacht in het kort</strong></h3>
<p><strong>00:00 Atlanta Hawks – Miami Heat</strong><br>Miami wacht met 0-4 nog op de eerste zege, ondanks 28,5 punten en 9,5 rebounds per wedstrijd van Giannis Antetokounmpo. Atlanta begon sterk met zeges in Orlando (132-125) en Charlotte (128-81), maar verloor daarna twee keer van Houston. Jalen Johnson haalt gemiddeld 21,5 punten, 9,8 rebounds en 8,2 assists. De Hawks zijn favoriet met 1,67. Het puntentotaal van 240,5 is samen met dat van Pelicans – Nuggets het hoogste van de nacht. Wij zien hier geen duidelijke waarde.</p>
<p><strong>00:00 Cleveland Cavaliers – Washington Wizards</strong><br>Cleveland staat op 2-1 en won de laatste wedstrijd na verlenging met 127-125 van Minnesota. Donovan Mitchell maakt 26,7 punten per duel. Washington (2-2) heeft met Anthony Davis (22,8 punten, 9,2 rebounds) en Trae Young (22,2 punten, 11,0 assists) twee sterren, maar mist AJ Dybantsa. De Cavaliers zijn favoriet met 1,26 en moeten op de handicap van -9,5 met tien punten verschil winnen. Bij Cleveland zit de Nederlander Tristan Enaruna in de selectie.</p>
<p><strong>00:00 Detroit Pistons – Charlotte Hornets</strong><br>Detroit speelt de tweede avond op rij, na een 97-111 nederlaag in New York, en mist center Jalen Duren. Cade Cunningham (20,8 punten, 8,0 assists) is de leider. Charlotte staat verrassend op 3-1, met Brandon Miller in vorm: 24,2 punten gemiddeld en 39 in zijn laatste wedstrijd tegen Washington. De Hornets missen wel Kon Knueppel, Coby White en Grant Williams. De Pistons zijn favoriet met 1,41. Met 215,5 punten verwacht de bookmaker hier de minste punten van de nacht.</p>
<p><strong>00:00 Indiana Pacers – Philadelphia 76ers</strong><br>Philadelphia (3-1) heeft met Tyrese Maxey (28,8 punten), Joel Embiid, Jaylen Brown en LeBron James veel aanvallend talent en is uitgerust. Indiana (2-2) verloor de laatste wedstrijd met 102-110 in Milwaukee. Bij de Pacers ontbreken center Ivica Zubac (enkel) en T.J. McConnell, en zijn Tyrese Haliburton en Andrew Nembhard twijfelachtig. De 76ers zijn favoriet met 1,54. In onze voorbeschouwing kiezen we voor 76ers -4,5 (1,87), een tip die net buiten onze top vier valt. Lees alles in {L['ind']}.</p>
<p><strong>00:30 Toronto Raptors – Orlando Magic</strong><br>Toronto (2-1) won thuis met 135-92 van Chicago en verloor in Minnesota (94-117). RJ Barrett maakt 21,0 punten per wedstrijd; Kawhi Leonard ontbreekt nog. Orlando (1-2) mist Paolo Banchero, Jalen Suggs en Jonathan Isaac, waardoor Franz Wagner (21,0 punten) de aanval moet dragen. De Raptors zijn favoriet met 1,56. Opvallend: twee dagen later treffen deze ploegen elkaar opnieuw in Toronto.</p>
<p><strong>01:00 Chicago Bulls – New York Knicks</strong><br>New York boekte dinsdag de eerste zege van het seizoen (111-97 tegen Detroit), met 27 punten en 20 rebounds van Karl-Anthony Towns, en speelt nu de tweede avond op rij. Jalen Brunson scoort 22,8 punten per wedstrijd. Chicago (1-3) verloor de laatste wedstrijd met 99-134 in Boston, kreeg gemiddeld 129,5 punten tegen en mist Nic Claxton. De Knicks zijn favoriet met 1,38.</p>"""

content3 = f"""<p><strong>01:00 Milwaukee Bucks – Houston Rockets</strong><br>Het ongeslagen Houston zonder Şengün tegen een Milwaukee dat net zijn eerste zege boekte. De Rockets zijn favoriet met 1,30. Onze tip: Bucks +8,5. De volledige analyse lees je in {L['mil']}; Houston bespraken we eerder ook in <a href="/nieuws/rockets-hawks-voorspelling-wedtips-nba-2026">Rockets – Hawks</a>.</p>
<p><strong>01:00 Minnesota Timberwolves – Golden State Warriors</strong><br>Minnesota zonder Anthony Edwards tegen een Golden State dat in Denver met 134-114 zijn eerste zege boekte. TOTO maakt de Wolves favoriet met 1,69. Onze tip: Warriors +3,5. Bij Golden State staat de Nederlander Malevy Leons in de selectie; hij speelde in Denver drie minuten. Meer over de Nederlanders lees je in ons overzicht <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">welke Nederlanders in de NBA spelen</a>.</p>
<p><strong>01:00 New Orleans Pelicans – Denver Nuggets</strong><br>New Orleans staat op 0-3, maar verloor steeds nipt: met 3 punten van Indiana, met 1 punt in Utah en na verlenging met 135-141 in Denver. Diezelfde Nuggets komen nu op bezoek. Denver (1-2) ging in de laatste wedstrijd thuis met 114-134 onderuit tegen Golden State. Nikola Jokić (22,3 punten, 9,7 rebounds, 8,7 assists) en Jamal Murray (22,3 punten) zijn de smaakmakers, bij New Orleans zijn dat Zion Williamson (20,7) en Dejounte Murray (20,3). De Nuggets zijn favoriet met 1,53.</p>
<p><strong>02:00 Utah Jazz – San Antonio Spurs</strong><br>San Antonio speelt de tweede avond op rij, na een 130-103 zege op Sacramento waarin Victor Wembanyama in 27 minuten 29 punten en 10 rebounds verzamelde. Utah (1-3) mist Jaren Jackson Jr. en Jusuf Nurkić, en achter Lauri Markkanen (pols) staat een vraagteken. Keyonte George (22,8 punten, 7,8 assists) is de vaste waarde. Met 1,17 zijn de Spurs de grootste favoriet van de nacht, maar op de handicap moeten ze met minstens 13 punten winnen (-12,5). Dat vinden wij een te grote marge, zeker voor een vermoeide ploeg.</p>
<p><strong>02:30 Dallas Mavericks – Oklahoma City Thunder</strong><br>Cooper Flagg tegen de ongeslagen Thunder, die het zonder Chet Holmgren en Alex Caruso moeten doen. OKC is favoriet met 1,48. Onze tip: Thunder -4,5. Meer in {L['dal']}.</p>
<p><strong>03:30 Los Angeles Clippers – Los Angeles Lakers</strong><br>De tweede stadsderby in een week, nu in de Intuit Dome. De Lakers wonnen de eerste met 125-117, maar spelen de tweede avond op rij na het verlies tegen Portland. De Clippers missen vijf spelers, onder wie Bradley Beal en Brandon Ingram. De Lakers zijn favoriet met 1,54. Onze tip: meer dan 228,5 punten. Meer in {L['lac']}.</p>
<h3><strong>Wedden op de NBA: zo werkt het</strong></h3>
<p>Bij basketbal is het belangrijk dat je let op de markt waarop je speelt. Bij de markt <strong>Winnaar</strong> (de <a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">moneyline</a>) telt een eventuele verlenging mee: er is altijd een winnaar. Bij de markt <strong>Wedstrijd - Resultaat (excl. OT)</strong> telt alleen de reguliere speeltijd van 48 minuten. Daar kun je ook op een gelijkspel wedden, en staat het na vier kwarten gelijk, dan verlies je een weddenschap op een van beide teams.</p>
<p>Bij een <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap</a> krijgt het ene team punten voorsprong en het andere achterstand. Bij Thunder -4,5 moet Oklahoma City met minstens vijf punten winnen. Bij Bucks +8,5 krijgt Milwaukee 8,5 punt voorsprong: je wint als de Bucks winnen of met maximaal acht punten verliezen. Bij een puntentotaal speel je op het totaal aantal punten van beide teams samen, inclusief een eventuele verlenging. De belangrijkste spelregels lees je in <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de regels van de NBA uitgelegd</a>.</p>
<p>Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit. Twijfel je? Lees <a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>. Alle basketbaltips en voorspellingen vind je op onze pagina <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>, en eerdere tips lees je terug in <a href="/nieuws/nba-voorspellingen-vannacht-27-oktober-2026">NBA voorspellingen van 27 oktober</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat beginnen de NBA-wedstrijden vannacht?</strong><br>De eerste vier wedstrijden, waaronder Pacers – 76ers, beginnen donderdag om 00:00 Nederlandse tijd. Daarna volgen Raptors – Magic om 00:30, vijf wedstrijden om 01:00, Jazz – Spurs om 02:00, Mavericks – Thunder om 02:30 en als laatste Clippers – Lakers om 03:30.</p>
<p><strong>Waar kan ik de NBA vannacht live zien?</strong><br>Met een account bij Bet365 kun je NBA-wedstrijden live streamen. Daarnaast zendt ESPN in Nederland een deel van de wedstrijden uit en kun je met NBA League Pass alle wedstrijden volgen.</p>
<p><strong>Welke ploegen spelen vannacht de tweede avond op rij?</strong><br>Detroit Pistons, New York Knicks, San Antonio Spurs en Los Angeles Lakers speelden dinsdagavond (Amerikaanse tijd) ook al. De andere ploegen hadden minstens één rustdag.</p>
<p><strong>Speelt er een Nederlander vannacht?</strong><br>Er zitten twee Nederlanders in een selectie die vannacht speelt: Malevy Leons bij Golden State (01:00 in Minnesota) en Tristan Enaruna bij Cleveland (00:00 tegen Washington). Beiden hebben een two-way-contract; of ze speeltijd krijgen, is onzeker.</p>
<p><strong>Wat is de beste NBA-tip van vannacht?</strong><br>Onze favoriete tip is Golden State Warriors +3,5 in Minnesota, met een odd van 1,87 bij TOTO. De Wolves missen Anthony Edwards. Een tip blijft een inschatting: zet alleen in wat je kunt missen.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    alles = content + content2 + content3
    tekst = re.sub(r"<[^>]+>", " ", alles)
    woorden = len(tekst.split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", woorden, "woorden |", len(TIPS), "tips")
    assert len(TITEL) <= 60 and 120 <= len(SAMENVATTING) <= 155, (len(TITEL), len(SAMENVATTING))
    assert 1400 <= woorden <= 2600, woorden
    assert 1 <= len(TIPS) <= 4 and len(OG_DATA) == 4 and len(OG_CHIPS) == 2 and len(NAMEN) == len(STAKE) == len(TIPS)
    assert all(float(t["odds"]) >= 1.40 for t in TIPS)
    assert not re.search(r"<(ul|ol|/li)>\s+<", alles) and not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert "<h2" not in alles and "<h4" not in alles and "affiliate" not in alles and "betcity" not in alles.lower()
    assert all(f"<strong>{t} {h} – {u}</strong>" in alles for t, h, u, _, _ in PROGRAMMA)
    assert "<p><strong>Kijken?</strong>" in content and alles.count("<table") == 2
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    # tips consistent met de tabel en de feiten
    for t in TIPS:
        assert q(float(t["odds"])) in content, t["odds"]
    # eigenaar: nooit een under als tip
    assert not any(re.search(r"minder dan|\bunder\b", t["tip"], re.I) for t in TIPS)
    assert not re.search(r"\bunder\b", alles, re.I)
    # de vier voorbeschouwingen van vannacht en de back-to-backs staan erin
    for s in ("pacers-76ers", "bucks-rockets", "mavericks-thunder", "clippers-lakers"):
        assert f'href="/nieuws/{s}-voorspelling-wedtips-nba-2026"' in alles, s
    assert all(p in content for p in ("Detroit", "New York", "San Antonio", "Lakers")) and "drie van de vier" in content
    assert [t["odds"] for t in TIPS] == ["1.87", "1.87", "1.87", "1.69"]
    print("dry run ok – niets gepubliceerd")
