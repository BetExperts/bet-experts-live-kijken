# -*- coding: utf-8 -*-
"""Los artikel: NBA voorspellingen vannacht, nacht van woensdag 21 op donderdag 22 oktober 2026 (11 wedstrijden).
Feiten nagelopen op 21-10-2026 (20:30 NL):
- Tweede speelavond van 2026/27: op 20-10 speelden Pistons-Celtics 121-113, Knicks-76ers 100-106, Spurs-Thunder 104-116.
  Alle 22 ploegen van vannacht spelen hun eerste wedstrijd: geen back-to-backs.
- Blessures: officiele teamberichten/blessurelijst stand 20/21-10 (zie tabel BLESSURES hieronder).
- Selecties, records 2025/26 en onderlinge duels 2025/26 nagelopen per team.
- Odds: TOTO, gelezen op sport.toto.nl (NBA-overzicht + wedstrijdpagina's) om 20:23-20:28 NL op 21-10.
  'Winnaar' = incl. verlenging; 'Handicap - Winnaar (Inc OT)'; 'Wedstrijd - Resultaat (excl. OT)' = 1X2 na 48 minuten.
  python3 specials/nba_vannacht_2026_10_22.py   (alleen dry run, publiceert niets)"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "nba-voorspellingen-vannacht-22-oktober-2026"
RUBRIEK = "672293e14a76d88272bc0b61"   # Basketball
TITEL = "NBA voorspellingen vannacht: 4 beste wedtips (22 oktober)"
SAMENVATTING = ("Elf NBA-wedstrijden vannacht: korte voorbeschouwing per duel, speeltijden in Nederlandse tijd en onze "
                "4 beste voorspellingen met odds.")

OG_KOP = "NBA <span>voorspellingen</span> vannacht"
OG_EYEBROW = "Basketbal · 22 oktober"
OG_CHIPS = ["11 wedstrijden", "4 beste tips"]
OG_MOTIEF = "tabel"
OG_DATA = ["MEM-UTA · Jazz +1,5 @1,91", "ORL-ATL · Hawks +2,5 @1,87", "NOP-IND · Pacers wint @1,67",
           "WAS-MIL · Wizards wint @1,54"]

LW = '<a href="/nieuws/lakers-warriors-voorspelling-wedtips-nba-2026">Lakers – Warriors</a>'

# (tijd NL, thuis, uit, odd thuis, odd uit)  TOTO 'Winnaar' (incl. verlenging), 21-10 20:23
PROGRAMMA = [
    ("01:00", "Orlando Magic", "Atlanta Hawks", 1.77, 2.10),
    ("01:00", "Washington Wizards", "Milwaukee Bucks", 1.54, 2.55),
    ("01:30", "Brooklyn Nets", "Charlotte Hornets", 2.00, 1.83),
    ("01:30", "Miami Heat", "Minnesota Timberwolves", 1.83, 2.00),
    ("01:30", "Toronto Raptors", "Chicago Bulls", 1.22, 4.50),
    ("02:00", "Memphis Grizzlies", "Utah Jazz", 1.83, 2.00),
    ("02:00", "New Orleans Pelicans", "Indiana Pacers", 2.30, 1.67),
    ("02:30", "Houston Rockets", "Dallas Mavericks", 1.24, 4.25),
    ("04:00", "Los Angeles Lakers", "Golden State Warriors", 1.43, 2.90),
    ("04:00", "Portland Trail Blazers", "Phoenix Suns", 1.71, 2.20),
    ("04:30", "Los Angeles Clippers", "Sacramento Kings", 1.54, 2.55),
]


def q(x):
    return f"{x:.2f}".replace(".", ",")


def fav(t, u, ot, ou):
    return f"{t} ({q(ot)})" if ot < ou else f"{u} ({q(ou)})"


assert len(PROGRAMMA) == 11

TIPS = [
    {"wedstrijd": "Memphis Grizzlies vs. Utah Jazz", "competitie": "NBA", "speeltijd_utc": "2026-10-22T00:00:00Z",
     "tijd_nl": "02:00", "tip": "Utah Jazz +1,5 (handicap incl. verlenging)", "odds": "1.91", "bookmaker": "toto",
     "analyse": "Bijna een kansspel volgens de markt, maar Utah heeft met Markkanen, George, Jackson jr. en Peterson meer aanvallend talent."},
    {"wedstrijd": "Orlando Magic vs. Atlanta Hawks", "competitie": "NBA", "speeltijd_utc": "2026-10-21T23:00:00Z",
     "tijd_nl": "01:00", "tip": "Atlanta Hawks +2,5 (handicap incl. verlenging)", "odds": "1.87", "bookmaker": "toto",
     "analyse": "Atlanta won vorig seizoen alle vier de duels en Orlando mist Jonathan Isaac en Anthony Black."},
    {"wedstrijd": "New Orleans Pelicans vs. Indiana Pacers", "competitie": "NBA", "speeltijd_utc": "2026-10-22T00:00:00Z",
     "tijd_nl": "02:00", "tip": "Indiana Pacers wint (incl. verlenging)", "odds": "1.67", "bookmaker": "toto",
     "analyse": "Met Haliburton terug na 487 dagen is Indiana een ander team dan de ploeg die vorig seizoen 19 keer won."},
    {"wedstrijd": "Washington Wizards vs. Milwaukee Bucks", "competitie": "NBA", "speeltijd_utc": "2026-10-21T23:00:00Z",
     "tijd_nl": "01:00", "tip": "Washington Wizards wint (incl. verlenging)", "odds": "1.54", "bookmaker": "toto",
     "analyse": "Trae Young en Anthony Davis spelen voor het eerst samen, tegen een Bucks-ploeg die voor het eerst in dertien seizoenen zonder Giannis begint."},
]

content = f"""<p><strong>In de nacht van woensdag op donderdag staan er elf NBA-wedstrijden op het programma, van 01:00 tot 04:30 Nederlandse tijd. Voor 22 van de 30 teams is het de eerste wedstrijd van het seizoen. Giannis Antetokounmpo debuteert voor Miami, Kawhi Leonard voor Toronto en Ja Morant voor Portland, en Tyrese Haliburton speelt na 487 dagen weer een officiële wedstrijd. Onze vier beste voorspellingen: Utah Jazz +1,5, Atlanta Hawks +2,5, een zege van de Indiana Pacers en een zege van de Washington Wizards.</strong></p>
<p>Na de openingsavond van dinsdag, met zeges voor Detroit, Philadelphia en Oklahoma City, gaat de NBA vannacht pas echt los. Elf duels, veel nieuwe gezichten en een paar teams die er na de zomer totaal anders uitzien. Omdat iedereen vannacht aan zijn eerste wedstrijd begint, speelt niemand een back-to-back: vermoeidheid is dus geen factor. Blessures wel. Hieronder vind je per wedstrijd een korte voorbeschouwing, de favoriet volgens de bookmakers en onze vier beste tips, met de odds bij TOTO.</p>
<p><strong>Kijken?</strong> Heb je een account bij <a href="/bookmakers/bet365">Bet365</a>, dan kun je NBA-wedstrijden daar live streamen. In Nederland zendt ESPN een deel van de NBA-wedstrijden uit en met NBA League Pass, de betaalde dienst van de competitie, zie je ze allemaal. Meer opties lees je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<h3><strong>Het NBA-programma van vannacht (Nederlandse tijd)</strong></h3>
{tabel(["Tijd", "Wedstrijd", "Favoriet volgens de markt"], [
    (f"<strong>{t}</strong>", f"{h} – {u}", fav(h, u, oh, ou)) for t, h, u, oh, ou in PROGRAMMA
])}
<p><em>Alle tijden op donderdag 22 oktober. Odds: TOTO, markt Winnaar (inclusief verlenging), stand woensdagavond 21 oktober 20:30. Odds kunnen tot de start nog veranderen.</em></p>
<h3><strong>De 4 beste NBA-voorspellingen van vannacht</strong></h3>
{tabel(["Wedstrijd", "Tip", "Odd", "Markt"], [
    ("Grizzlies – Jazz (02:00)", "<strong>Utah Jazz +1,5</strong>", "1,91", "Handicap, incl. verlenging"),
    ("Magic – Hawks (01:00)", "<strong>Atlanta Hawks +2,5</strong>", "1,87", "Handicap, incl. verlenging"),
    ("Pelicans – Pacers (02:00)", "<strong>Indiana Pacers wint</strong>", "1,67", "Winnaar, incl. verlenging"),
    ("Wizards – Bucks (01:00)", "<strong>Washington Wizards wint</strong>", "1,54", "Winnaar, incl. verlenging"),
])}
<p><em>Alle odds bij <a href="/bookmakers/toto">TOTO</a>, gelezen op woensdag 21 oktober om 20:30. Losse tips, geen combinatie: elke tip staat op zichzelf.</em></p>
<h3><strong>1. Memphis Grizzlies – Utah Jazz: Jazz +1,5 (1,91)</strong></h3>
<p>De bookmakers zien hier bijna een kansspel (Memphis 1,83, Utah 2,00), maar op papier heeft Utah meer aanvallend talent. Lauri Markkanen, Keyonte George (23,6 punten per wedstrijd vorig seizoen), oud-Grizzlies-ster Jaren Jackson jr. en de nummer twee van de draft, Darryn Peterson: dat is een flinke aanvalslinie voor een team dat dit jaar weer echt wil winnen. Wij schatten de kans dat Utah wint of met maximaal één punt verliest op ruim 55%, terwijl een odd van 1,91 uitgaat van 52%. Wat kan er misgaan? De Jazz missen hun centers Jusuf Nurkić en Tony Bradley en moeten het opnemen tegen de 2,24 meter lange Zach Edey. Bovendien had Utah de afgelopen drie seizoenen een van de slechtste verdedigingen van de competitie.</p>
<h3><strong>2. Orlando Magic – Atlanta Hawks: Hawks +2,5 (1,87)</strong></h3>
<p>Atlanta won vorig seizoen alle vier de onderlinge duels, waarvan twee in Orlando (111-107 en 130-101). Orlando begint nu zonder twee belangrijke verdedigers: Jonathan Isaac (knie) en Anthony Black (enkel) zijn uitgeschakeld. De Hawks, met All-Star Jalen Johnson, verdediger Dyson Daniels en nieuwkomer Luguentz Dort, wonnen vier van hun vijf oefenduels, onder meer in San Antonio en tegen Oklahoma City. Met +2,5 heb je ook nog winst als Atlanta met één of twee punten verliest; wij schatten die kans op zo'n 55%, tegen 53% in de odd. Het risico: Orlando heeft met Paolo Banchero, Franz Wagner, Wendell Carter jr. en Nikola Vučević veel meer lengte, en rimbescherming is precies het zwakke punt van Atlanta.</p>
<h3><strong>3. New Orleans Pelicans – Indiana Pacers: Pacers wint (1,67)</strong></h3>
<p>Zonder Tyrese Haliburton, die in de finale van 2025 zijn achillespees scheurde, won Indiana vorig seizoen maar 19 keer. Nu is de spelverdeler terug, met Pascal Siakam, Andrew Nembhard en nieuwe center Ivica Zubac om zich heen. New Orleans kreeg vorig seizoen gemiddeld 120,0 punten tegen en begint onder een nieuwe coach, Jamahl Mosley. Wij schatten de winkans van Indiana op ongeveer 61%; de odd van 1,67 gaat uit van 60%, dus dit is vooral een tip met een redelijke kans en een eerlijke prijs. Wat kan er misgaan? Indiana mist T.J. McConnell en Aaron Nesmith, Haliburton moet zijn ritme nog vinden en een fitte Zion Williamson kan in zijn eentje een wedstrijd beslissen.</p>
<h3><strong>4. Washington Wizards – Milwaukee Bucks: Wizards wint (1,54)</strong></h3>
<p>Vorig seizoen won Washington maar 17 wedstrijden, maar dit is een andere ploeg. Trae Young kwam in januari over, Anthony Davis kwam in februari maar speelde nog geen minuut voor de club, en ook Deandre Ayton en Khris Middleton staan in de selectie. Milwaukee begint voor het eerst in dertien seizoenen zonder Giannis Antetokounmpo, met Tyler Herro, Myles Turner en Kyle Kuzma als dragende spelers. Washington won ook drie van de vier duels vorig seizoen. Wij schatten de winkans op ongeveer 65%. Dat is precies wat de odd van 1,54 aangeeft: weinig extra waarde, wel de grootste kans van onze vier tips. Het risico: de nummer één van de draft, AJ Dybantsa, mist het duel met een enkelblessure, de nieuwe Wizards hebben nog weinig samen gespeeld en de breedte van de Bucks kan in een lange wedstrijd het verschil maken.</p>"""

content2 = f"""<h3><strong>Alle wedstrijden van vannacht in het kort</strong></h3>
<p><strong>01:00 Orlando Magic – Atlanta Hawks</strong><br>De eerste wedstrijd onder de nieuwe Magic-coach Sean Sweeney, die de ploeg na het verlies van een 3-1-voorsprong tegen Detroit in de play-offs naar een hoger plan moet tillen. Isaac en Black ontbreken, bij Atlanta zijn alleen Mouhamed Gueye en Henri Veesaar afwezig. TOTO ziet Orlando als lichte favoriet (1,77). Onze tip: Hawks +2,5.</p>
<p><strong>01:00 Washington Wizards – Milwaukee Bucks</strong><br>Twee ploegen die vorig seizoen ver onder de streep eindigden (17-65 en 32-50), maar met een totaal nieuwe selectie. Bij Milwaukee is rookie Nate Ament (enkel) waarschijnlijk inzetbaar. De Wizards zijn favoriet met 1,54, de Bucks staan op 2,55. Onze tip: Wizards wint.</p>
<p><strong>01:30 Brooklyn Nets – Charlotte Hornets</strong><br>Charlotte is favoriet (1,83), maar mist vannacht vier spelers: Kon Knueppel, nieuwe spelverdeler Coby White, Grant Williams en Kylan Boswell. Brooklyn, vorig seizoen goed voor 20 zeges, heeft met Julius Randle en Michael Porter jr. twee scorers en won in de voorbereiding met 124-90 in Charlotte. De markt verwacht met 220,5 het laagste puntentotaal van de avond. Wij blijven hier weg: te veel onzekerheid.</p>
<p><strong>01:30 Miami Heat – Minnesota Timberwolves</strong><br>Misschien wel de leukste affiche van de avond: Giannis Antetokounmpo speelt zijn eerste officiële wedstrijd voor Miami, naast Bam Adebayo. Daar tegenover staat het nieuwe Wolves-duo Anthony Edwards en LaMelo Ball. Minnesota mist Donte DiVincenzo (achillespees), bij Miami is center Vladislav Goldin twijfelachtig. Met 1,83 tegen 2,00 en een totaal van 240,5 punten is dit een open wedstrijd met veel punten.</p>
<p><strong>01:30 Toronto Raptors – Chicago Bulls</strong><br>Kawhi Leonard keert terug in Toronto, waar hij in 2019 kampioen werd, en vormt nu een duo met Scottie Barnes. De Raptors zijn met 1,22 de grootste favoriet van de avond. Chicago mist Nic Claxton, Jordan Hawkins en Dailyn Swain en begint onder de nieuwe coach Tiago Splitter. Een handicap van -10,5 vinden wij veel voor een eerste wedstrijd, met een nieuwe ster die nog moet inpassen in het team.</p>
<p><strong>02:00 Memphis Grizzlies – Utah Jazz</strong><br>Voor Nederlanders interessant: Quinten Post staat bij Memphis onder contract. De Grizzlies begonnen na het vertrek van Morant, Jackson jr. en Desmond Bane aan een nieuwe opbouw, met nummer drie van de draft Cameron Boozer en een fitte Zach Edey. Isaiah Stewart is twijfelachtig. Onze tip: Jazz +1,5.</p>
<p><strong>02:00 New Orleans Pelicans – Indiana Pacers</strong><br>De terugkeer van Haliburton is het verhaal van deze wedstrijd. De Pacers zijn met 1,67 favoriet in New Orleans, waar Zion Williamson, Trey Murphy III en nieuwkomer Bennedict Mathurin de dienst uitmaken. Vorig seizoen won elke ploeg haar thuiswedstrijd. Onze tip: Pacers wint.</p>"""

content3 = f"""<p><strong>02:30 Houston Rockets – Dallas Mavericks</strong><br>Houston (52-30 vorig seizoen) krijgt Fred VanVleet terug na een gescheurde kruisband, naast Kevin Durant en Alperen Şengün. Dallas mist Dereck Lively II, Santi Aldama, Caleb Martin en Tarik Biberović, wat onder de ring gevaarlijk is tegen het team dat al twee seizoenen de meeste aanvallende rebounds pakt. Steven Adams (kuit) is twijfelachtig bij Houston. Houston is favoriet met 1,24; Cooper Flagg en Kyrie Irving moeten het verschil voor Dallas maken.</p>
<p><strong>04:00 Los Angeles Lakers – Golden State Warriors</strong><br>De Lakers beginnen hun eerste seizoen zonder LeBron James sinds 2018 en zijn met 1,43 duidelijk favoriet tegen een Golden State dat veel afwezigen heeft. Alles over deze klassieker, met blessures, opstellingen en wedtips, lees je in onze uitgebreide voorbeschouwing van {LW}.</p>
<p><strong>04:00 Portland Trail Blazers – Phoenix Suns</strong><br>Ja Morant debuteert voor Portland en Damian Lillard keert terug na een seizoen zonder wedstrijden door een achillespeesblessure. Deni Avdija (enkel) is twijfelachtig en Shaedon Sharpe is maanden uitgeschakeld. Bij Phoenix ontbreekt center Mark Williams en is Luke Kennard twijfelachtig. Portland is favoriet met 1,71, maar vorig seizoen won Phoenix twee van de drie duels.</p>
<p><strong>04:30 Los Angeles Clippers – Sacramento Kings</strong><br>Twee ploegen in de wederopbouw. De Clippers missen Bradley Beal, Brandon Ingram en Max Strus en draaien om Darius Garland, Sacramento begint met rookie Darius Acuff jr. als spelverdeler naast Domantas Sabonis en Zach LaVine. De Kings verloren al hun vijf oefenduels en wonnen vorig seizoen maar 7 van hun 41 uitwedstrijden. De Clippers zijn favoriet met 1,54.</p>
<h3><strong>Wedden op de NBA: zo werkt het</strong></h3>
<p>Bij basketbal is het belangrijk dat je let op de markt waarop je speelt. Bij de markt <strong>Winnaar</strong> (de <a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">moneyline</a>) telt een eventuele verlenging mee: er is altijd een winnaar. Bij de markt <strong>Wedstrijd - Resultaat (excl. OT)</strong> telt alleen de reguliere speeltijd van 48 minuten. Daar kun je dus ook op een gelijkspel wedden, en staat het na vier kwarten gelijk, dan verlies je een weddenschap op een van beide teams. Daarom is de odd op de winnaar excl. verlenging vaak iets hoger. Vannacht staan de Clippers bijvoorbeeld op 1,54 incl. verlenging en op 1,53 excl. verlenging, met een gelijkspel op 20,00.</p>
<p>Bij een <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap</a> krijgt het ene team punten voorsprong en het andere achterstand. Bij Jazz +1,5 telt de bookmaker 1,5 punt op bij de score van Utah: je wint als Utah wint of met één punt verliest. Bij een puntentotaal (over/under) speel je op het totaal aantal punten van beide teams samen. De belangrijkste spelregels, zoals de duur van een verlenging, lees je in <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de regels van de NBA uitgelegd</a>.</p>
<p>Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit. Twijfel je? Lees <a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>. Alle basketbaltips en voorspellingen vind je op onze pagina <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>, en wil je weten wie er van Nederlandse bodem meedoet, lees dan <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">welke Nederlanders in de NBA spelen</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat beginnen de NBA-wedstrijden vannacht?</strong><br>De eerste twee wedstrijden beginnen op donderdag 22 oktober om 01:00 Nederlandse tijd, de laatste (Clippers – Kings) om 04:30.</p>
<p><strong>Waar kan ik de NBA vannacht live zien?</strong><br>Met een account bij Bet365 kun je NBA-wedstrijden live streamen. Daarnaast zendt ESPN in Nederland een deel van de wedstrijden uit en kun je met NBA League Pass alle wedstrijden volgen.</p>
<p><strong>Wat is het verschil tussen winnaar incl. en excl. verlenging?</strong><br>Bij incl. verlenging telt de verlenging mee en is er altijd een winnaar. Bij excl. verlenging telt alleen de reguliere speeltijd, en verlies je als het na 48 minuten gelijk staat.</p>
<p><strong>Speelt Tyrese Haliburton vannacht?</strong><br>Ja, hij staat niet op de blessurelijst. Het is zijn eerste officiële wedstrijd sinds Game 7 van de NBA Finals in juni 2025.</p>
<p><strong>Speelt er een Nederlander vannacht?</strong><br>Quinten Post staat onder contract bij Memphis, dat om 02:00 Utah ontvangt. Malevy Leons heeft een two-way-contract bij Golden State, dat om 04:00 bij de Lakers speelt.</p>
<p><strong>Wat is de beste NBA-tip van vannacht?</strong><br>Onze favoriete tip is Utah Jazz +1,5 tegen Memphis, met een odd van 1,91 bij TOTO. Een tip blijft een inschatting: zet alleen in wat je kunt missen.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    alles = content + content2 + content3
    tekst = re.sub(r"<[^>]+>", " ", alles)
    woorden = len(tekst.split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", woorden, "woorden |", len(TIPS), "tips")
    assert len(TITEL) <= 60 and 120 <= len(SAMENVATTING) <= 155
    assert 1400 <= woorden <= 2200, woorden
    assert 1 <= len(TIPS) <= 4 and len(OG_DATA) == 4 and len(OG_CHIPS) == 2
    assert all(float(t["odds"]) >= 1.40 for t in TIPS)
    assert not re.search(r"<(ul|ol|/li)>\s+<", alles) and not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert "<h2" not in alles and "<h4" not in alles and "affiliate" not in alles
    assert all(f"<strong>{t} {h} – {u}</strong>" in alles for t, h, u, _, _ in PROGRAMMA)
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    print("dry run ok – niets gepubliceerd")
