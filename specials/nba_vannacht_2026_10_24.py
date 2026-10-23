# -*- coding: utf-8 -*-
"""Los artikel: NBA voorspellingen vannacht, vrijdagavond 23 en nacht van vrijdag op zaterdag 24 oktober 2026 (12 wedstrijden).
Feiten nagelopen op 23-10-2026 (±12:00 NL):
- programma, uitslagen speelronde 1 en blessures: specials/nba_feiten_2026_10_24.md + nba_feiten_overig_2026_10_24.md
  (ESPN-scoreboard/box scores, officieel NBA-injury report 23-10 06:00 ET);
- de 5 toppers hebben een eigen voorbeschouwing (celtics_knicks, pacers_mavericks, heat_pistons, spurs_rockets, lakers_clippers);
  de tips hier sluiten daarop aan (Pistons wint, Under 223,5 bij Celtics – Knicks).
- Odds: TOTO (sport.toto.nl, overzicht + wedstrijdpagina's) om ±12:00 NL op 23-10. 'Winnaar' = incl. verlenging.
  python3 specials/nba_vannacht_2026_10_24.py   (alleen dry run, publiceert niets)
  publiceren: specials/nba_vannacht_publiceer.py nba_vannacht_2026_10_24 --live"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "nba-voorspellingen-vannacht-24-oktober-2026"
RUBRIEK = "672293e14a76d88272bc0b61"   # Basketball
TITEL = "NBA voorspellingen vannacht: 4 beste wedtips (24 oktober)"
SAMENVATTING = ("Twaalf NBA-wedstrijden vanavond en vannacht: speeltijden in Nederlandse tijd, korte voorbeschouwing per duel "
                "en onze 4 beste tips.")
DATUM = "2026-10-23T20:00:00.000Z"     # eerste wedstrijd: Bucks – Bulls, vrijdag 22:00 NL

OG_KOP = "NBA <span>voorspellingen</span> vannacht"
OG_EYEBROW = "Basketbal · 24 oktober"
OG_CHIPS = ["12 wedstrijden", "4 beste tips"]
OG_MOTIEF = "tabel"
OG_DATA = ["CHA-ATL · Hawks -2,5 @1,87", "MIA-DET · Pistons wint @1,91", "BOS-NYK · Under 223,5 @1,91",
           "UTA-NOP · Over 238,5 @1,87"]

NAMEN = ["Hawks pakken Charlotte zonder Knueppel!", "Cade wint het duel met Giannis!", "Weinig punten in Boston!",
         "Puntenfestijn in Salt Lake City!"]
STAKE = [4, 4, 4, 3]

L = {"bos": '<a href="/nieuws/celtics-knicks-voorspelling-wedtips-nba-2026">Celtics – Knicks</a>',
     "ind": '<a href="/nieuws/pacers-mavericks-voorspelling-wedtips-nba-2026">Pacers – Mavericks</a>',
     "mia": '<a href="/nieuws/heat-pistons-voorspelling-wedtips-nba-2026">Heat – Pistons</a>',
     "sa": '<a href="/nieuws/spurs-rockets-voorspelling-wedtips-nba-2026">Spurs – Rockets</a>',
     "lal": '<a href="/nieuws/lakers-clippers-voorspelling-wedtips-nba-2026">Lakers – Clippers</a>'}

# (tijd NL, thuis, uit, odd thuis, odd uit)  TOTO 'Winnaar' (incl. verlenging), 23-10 ±12:00
PROGRAMMA = [
    ("22:00", "Milwaukee Bucks", "Chicago Bulls", 1.87, 1.95),
    ("01:00", "Boston Celtics", "New York Knicks", 1.74, 2.15),
    ("01:00", "Charlotte Hornets", "Atlanta Hawks", 2.20, 1.71),
    ("01:00", "Indiana Pacers", "Dallas Mavericks", 1.45, 2.80),
    ("01:00", "Orlando Magic", "Minnesota Timberwolves", 2.05, 1.80),
    ("01:00", "Washington Wizards", "Toronto Raptors", 2.95, 1.41),
    ("02:00", "Miami Heat", "Detroit Pistons", 1.91, 1.91),
    ("03:30", "San Antonio Spurs", "Houston Rockets", 1.50, 2.70),
    ("03:30", "Utah Jazz", "New Orleans Pelicans", 1.74, 2.15),
    ("04:00", "Golden State Warriors", "Memphis Grizzlies", 1.69, 2.25),
    ("04:00", "Los Angeles Lakers", "LA Clippers", 1.25, 4.10),
    ("04:00", "Sacramento Kings", "Portland Trail Blazers", 3.60, 1.31),
]


def q(x):
    return f"{x:.2f}".replace(".", ",")


def fav(t, u, ot, ou):
    if ot == ou:
        return f"Gelijk ({q(ot)} – {q(ou)})"
    return f"{t} ({q(ot)})" if ot < ou else f"{u} ({q(ou)})"


assert len(PROGRAMMA) == 12

TIPS = [
    {"wedstrijd": "Charlotte Hornets vs. Atlanta Hawks", "competitie": "NBA", "speeltijd_utc": "2026-10-23T23:00:00Z",
     "tijd_nl": "01:00", "tip": "Atlanta Hawks -2,5 (handicap incl. verlenging)", "odds": "1.87", "bookmaker": "toto",
     "analyse": "Charlotte mist opnieuw Knueppel, White en Grant Williams; Atlanta won de opener in Orlando met 132-125."},
    {"wedstrijd": "Miami Heat vs. Detroit Pistons", "competitie": "NBA", "speeltijd_utc": "2026-10-24T00:00:00Z",
     "tijd_nl": "02:00", "tip": "Detroit Pistons wint (incl. verlenging)", "odds": "1.91", "bookmaker": "toto",
     "analyse": "De nummer één van het Oosten van vorig seizoen tegen een Heat-ploeg die met 106-131 verloor en zaterdag alweer in Charlotte speelt."},
    {"wedstrijd": "Boston Celtics vs. New York Knicks", "competitie": "NBA", "speeltijd_utc": "2026-10-23T23:00:00Z",
     "tijd_nl": "01:00", "tip": "Minder dan 223,5 punten (incl. verlenging)", "odds": "1.91", "bookmaker": "toto",
     "analyse": "Twee sterke verdedigingen; de Knicks scoorden in hun opener maar 100 punten tegen Philadelphia."},
    {"wedstrijd": "Utah Jazz vs. New Orleans Pelicans", "competitie": "NBA", "speeltijd_utc": "2026-10-24T01:30:00Z",
     "tijd_nl": "03:30", "tip": "Meer dan 238,5 punten (incl. verlenging)", "odds": "1.87", "bookmaker": "toto",
     "analyse": "De drie onderlinge duels van vorig seizoen leverden gemiddeld 253 punten op; Utah kreeg in 2025/26 gemiddeld 126 punten tegen."},
]

content = f"""<p><strong>Vanavond om 22:00 begint Milwaukee Bucks – Chicago Bulls, en daarna volgen in de nacht van vrijdag op zaterdag nog elf NBA-wedstrijden, tot 04:00 Nederlandse tijd. Toppers zijn Celtics – Knicks, Heat – Pistons met Giannis Antetokounmpo tegen Cade Cunningham, de Texas-derby Spurs – Rockets in Austin en de stadsderby Lakers – Clippers. Onze vier beste voorspellingen: Atlanta Hawks -2,5, een zege van de Detroit Pistons, minder dan 223,5 punten in Boston en meer dan 238,5 punten bij Jazz – Pelicans.</strong></p>
<p>Iedereen heeft zijn eerste wedstrijd van het seizoen gespeeld, dus vannacht zie je voor het eerst hoe de nieuwe selecties het doen na een eerste test. Vermoeidheid speelt mee bij elf van de 24 ploegen. Bucks, Bulls, Hornets, Hawks, Wizards, Heat, Mavericks, Spurs, Rockets, Pelicans en Warriors spelen zaterdag (Amerikaanse tijd) alweer, dus vannacht spelen ze het eerste duel van een back-to-back. Hieronder vind je het hele programma, per wedstrijd een korte voorbeschouwing en onze vier beste tips met de odds bij TOTO. Voor de vijf grootste wedstrijden hebben we een uitgebreide voorbeschouwing geschreven.</p>
<p><strong>Kijken?</strong> Heb je een account bij <a href="/bookmakers/bet365">Bet365</a>, dan kun je NBA-wedstrijden daar live streamen. In Nederland zendt ESPN een deel van de NBA-wedstrijden uit en met NBA League Pass, de betaalde dienst van de competitie, zie je ze allemaal. Meer opties lees je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<h3><strong>Het NBA-programma van vanavond en vannacht (Nederlandse tijd)</strong></h3>
{tabel(["Tijd", "Wedstrijd", "Favoriet volgens de markt"], [
    (f"<strong>{t}</strong>", f"{h} – {u}", fav(h, u, oh, ou)) for t, h, u, oh, ou in PROGRAMMA
])}
<p><em>Bucks – Bulls begint vrijdag 23 oktober om 22:00, alle andere wedstrijden zijn op zaterdag 24 oktober. Odds: TOTO, markt Winnaar (inclusief verlenging), stand vrijdag 23 oktober rond 12:00. Odds kunnen tot de start nog veranderen.</em></p>
<h3><strong>De 4 beste NBA-voorspellingen van vannacht</strong></h3>
{tabel(["Wedstrijd", "Tip", "Odd", "Markt"], [
    ("Hornets – Hawks (01:00)", "<strong>Atlanta Hawks -2,5</strong>", "1,87", "Handicap, incl. verlenging"),
    ("Heat – Pistons (02:00)", "<strong>Detroit Pistons wint</strong>", "1,91", "Winnaar, incl. verlenging"),
    ("Celtics – Knicks (01:00)", "<strong>Minder dan 223,5 punten</strong>", "1,91", "Totaal, incl. verlenging"),
    ("Jazz – Pelicans (03:30)", "<strong>Meer dan 238,5 punten</strong>", "1,87", "Totaal, incl. verlenging"),
])}
<p><em>Alle odds bij <a href="/bookmakers/toto">TOTO</a>, gelezen op vrijdag 23 oktober rond 12:00. Losse tips, geen combinatie: elke tip staat op zichzelf.</em></p>
<h3><strong>1. Charlotte Hornets – Atlanta Hawks: Hawks -2,5 (1,87)</strong></h3>
<p>Beide ploegen wonnen hun opener, maar onder heel andere omstandigheden. Atlanta won met 132-125 in Orlando, met 31 punten van Nickeil Alexander-Walker en 20 punten, 14 rebounds en 6 assists van Jalen Johnson. Charlotte won met 110-103 in Brooklyn, maar mist ook vannacht Kon Knueppel (hamstring, 18,5 punten per wedstrijd vorig seizoen), nieuwe spelverdeler Coby White (kuit), Grant Williams en Kylan Boswell. In de voorbereiding verloren de Hornets nog ruim van de Nets, de Celtics en de Grizzlies. Met Dyson Daniels en nieuwkomer Luguentz Dort heeft Atlanta bovendien twee van de beste verdedigers op de guardposities. Wij schatten de kans dat de Hawks met minstens drie punten winnen op zo'n 57%; de odd van 1,87 gaat uit van 53%. Het risico: Charlotte won vorig seizoen drie van de vier onderlinge duels, en beide ploegen spelen zaterdag alweer, Atlanta thuis tegen Houston.</p>
<h3><strong>2. Miami Heat – Detroit Pistons: Pistons wint (1,91)</strong></h3>
<p>De bookmakers zien een echte fiftyfifty, maar wij geven Detroit de voorkeur. De Pistons waren vorig seizoen met 60-22 de beste ploeg van het Oosten en openden dit seizoen met 121-113 tegen Boston. Miami kreeg in de eerste wedstrijd met Giannis Antetokounmpo thuis 131 punten tegen van Minnesota, ondanks 35 punten van de Griek. De Heat moeten na de grote ruil van deze zomer nog een ploeg worden, en spelen zaterdag om 18:00 Amerikaanse tijd alweer in Charlotte. Detroit speelt pas zondag weer. Wij schatten de winkans van de Pistons op ongeveer 56%, tegen 52% in de odd. Wat kan er misgaan? Giannis kan in zijn eentje een wedstrijd beslissen en het thuispubliek in Miami wil een reactie zien na de pijnlijke opener. Alles over dit duel lees je in onze voorbeschouwing van {L['mia']}.</p>
<h3><strong>3. Boston Celtics – New York Knicks: minder dan 223,5 punten (1,91)</strong></h3>
<p>De thuisopener van Boston tegen de regerend kampioen. Beide ploegen verloren hun eerste wedstrijd: de Celtics met 113-121 in Detroit, ondanks 38 punten van Paul George, en de Knicks thuis met 100-106 van Philadelphia. Vooral bij New York liep de aanval nog niet: honderd punten is weinig in de huidige NBA. Twee ervaren ploegen die hun eerste nederlaag willen goedmaken, gaan bovendien eerder voor controle dan voor tempo. Met 223,5 punten ligt dit totaal al lager dan bij de meeste andere wedstrijden van vannacht, maar wij schatten de kans op minder punten op ongeveer 55%. Het risico: één avond met veel driepunters is genoeg om eroverheen te gaan. Onze volledige voorspelling, met blessures en opstellingen, lees je in {L['bos']}.</p>
<h3><strong>4. Utah Jazz – New Orleans Pelicans: meer dan 238,5 punten (1,87)</strong></h3>
<p>Dit is het hoogste totaal van de nacht, maar ook de wedstrijd met het meeste aanvalsgeweld tegenover de zwakste verdedigingen. Utah kreeg vorig seizoen gemiddeld 126 punten per wedstrijd tegen, en de drie onderlinge duels eindigden op 247, 220 en zelfs 293 punten: gemiddeld 253. Beide ploegen verloren hun opener: de Jazz met 103-123 in Memphis, de Pelicans met 120-123 thuis tegen Indiana. New Orleans scoorde dus wel. Met Lauri Markkanen, Keyonte George, Jaren Jackson jr. en de nummer twee van de draft, Darryn Peterson, aan de ene kant en Zion Williamson, Trey Murphy III en Dejounte Murray aan de andere kant verwachten wij een open wedstrijd. Kans volgens ons: zo'n 55%, tegen 53% in de odd. Het risico: Markkanen schoot in de opener maar 4 uit 13, en als het schot bij beide ploegen niet valt, haalt zelfs deze wedstrijd de lijn niet.</p>"""

content2 = f"""<h3><strong>Alle wedstrijden van vanavond en vannacht in het kort</strong></h3>
<p><strong>22:00 Milwaukee Bucks – Chicago Bulls</strong><br>Ongewoon vroeg: de Bucks verplaatsten hun eerste thuiswedstrijd naar 15:00 lokale tijd, omdat de Milwaukee Brewers vanavond hun eerste World Series-wedstrijd sinds 1982 spelen. Milwaukee begint zonder Giannis en met nieuwe coach Taylor Jenkins, en verloor de opener met 116-128 in Washington (Tyler Herro 24 punten). Chicago verloor met 92-135 in Toronto en mist Nic Claxton; Jordan Hawkins en Dailyn Swain zijn twijfelachtig. In de voorbereiding wonnen de Bulls nog met 125-104 in Milwaukee. Een kansspel volgens TOTO (1,87 tegen 1,95). Het totaal van 238,5 punten vinden wij hoog: de Bucks scoorden vorig seizoen maar 110,6 punten per wedstrijd.</p>
<p><strong>01:00 Boston Celtics – New York Knicks</strong><br>De eerste thuiswedstrijd van Boston, tegen de kampioen van vorig seizoen. Boston mist alleen Devin Carter, die ziek is; bij New York staat niemand van de vaste rotatie op de blessurelijst. TOTO ziet de Celtics als lichte favoriet (1,74). Onze tip: minder dan 223,5 punten. Meer in onze voorbeschouwing van {L['bos']}.</p>
<p><strong>01:00 Charlotte Hornets – Atlanta Hawks</strong><br>Allebei 1-0, maar Charlotte speelt met een uitgedunde selectie: Knueppel, White, Grant Williams en Boswell ontbreken. LaMelo Ball speelt inmiddels in Minnesota; Brandon Miller, Naz Reid en Dennis Schröder dragen nu de aanval. Atlanta speelt al sinds januari zonder Trae Young en draait om Jalen Johnson. De Hawks zijn favoriet met 1,71. Onze tip: Hawks -2,5.</p>
<p><strong>01:00 Indiana Pacers – Dallas Mavericks</strong><br>Tyrese Haliburton tegen Cooper Flagg. Indiana won de opener met 123-120 in New Orleans (Pascal Siakam 30 punten), Dallas verloor met 110-128 in Houston ondanks 32 punten van Flagg. De Mavericks missen vier spelers, onder wie hun lange mannen Dereck Lively II en Santi Aldama, en spelen zaterdag alweer thuis tegen de Spurs. Indiana is favoriet met 1,45. Lees alles in {L['ind']}.</p>
<p><strong>01:00 Orlando Magic – Minnesota Timberwolves</strong><br>Orlando kreeg in de opener thuis 132 punten tegen van Atlanta, ondanks 35 punten en 10 assists van Paolo Banchero. Minnesota won met 131-106 in Miami: Anthony Edwards scoorde 45 punten met negen driepunters, naast het nieuwe duo met LaMelo Ball. Orlando mist Anthony Black, Jonathan Isaac en Noah Penda, maar won vorig seizoen beide duels met de Wolves. Minnesota is favoriet met 1,80; geen van beide ploegen speelt zaterdag. Wij verwachten veel punten, maar de lijn van 235,5 is al hoog genoeg.</p>
<p><strong>01:00 Washington Wizards – Toronto Raptors</strong><br>Ook allebei 1-0. Anthony Davis scoorde in zijn eerste wedstrijd voor Washington 34 punten en Trae Young had er 20, met 13 assists. Toronto won met 135-92 van Chicago, met Kawhi Leonard (23 punten) naast Scottie Barnes. Bij de Wizards mist nummer één van de draft AJ Dybantsa opnieuw met een enkelblessure, en de ploeg speelt zaterdag alweer in Chicago. De Raptors zijn duidelijk favoriet met 1,41. Washington had vorig seizoen de slechtste verdediging van de competitie, en dat is na één wedstrijd nog niet opgelost.</p>
<p><strong>02:00 Miami Heat – Detroit Pistons</strong><br>De tweede wedstrijd van Giannis Antetokounmpo voor Miami, tegen de ploeg van Cade Cunningham en Jalen Duren. TOTO kan geen favoriet kiezen: beide ploegen staan op 1,91. Wij kiezen voor Detroit. De volledige analyse lees je in {L['mia']}.</p>"""

content3 = f"""<p><strong>03:30 San Antonio Spurs – Houston Rockets</strong><br>Een Texas-derby, maar niet in San Antonio: de Spurs spelen deze thuiswedstrijd in het Moody Center in Austin. San Antonio verloor de opener met 104-116 van Oklahoma City; De'Aaron Fox (pols) is twijfelachtig en Tobias Harris (kuit) mist het duel. Houston won met 128-110 van Dallas, met 30 punten van Kevin Durant. Beide ploegen spelen zaterdag alweer, de Spurs in Dallas en de Rockets in Atlanta. De Spurs zijn favoriet met 1,50. Alles over dit duel lees je in {L['sa']}.</p>
<p><strong>03:30 Utah Jazz – New Orleans Pelicans</strong><br>Twee ploegen die vorig seizoen ver onderaan eindigden (22-60 en 26-56) en hun opener verloren. Utah mist center Jusuf Nurkić en Tony Bradley is twijfelachtig; bij New Orleans ontbreekt niemand van de vaste rotatie. De Jazz zijn lichte favoriet met 1,74; de Pelicans spelen zaterdag alweer in Denver. Onze tip: meer dan 238,5 punten.</p>
<p><strong>04:00 Golden State Warriors – Memphis Grizzlies</strong><br>Voor Nederlanders de wedstrijd van de nacht: Quinten Post, die deze zomer van Golden State naar Memphis vertrok, speelt tegen zijn oude club, en bij de Warriors staat Malevy Leons op de selectie. In de opener speelde Post 19 minuten (7 punten) en Leons 9 minuten. Golden State verloor met 105-127 bij de Lakers en mist nog altijd Jimmy Butler, Moses Moody en Kristaps Porziņģis; Brandin Podziemski is twijfelachtig. Memphis won met 123-103 van Utah dankzij 45 punten van Ty Jerome, maar het meedoen van Cedric Coward (pols) is onzeker. De Warriors zijn favoriet met 1,69 en spelen zaterdag alweer in Phoenix. Meer over de Nederlanders lees je in ons overzicht <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">welke Nederlanders in de NBA spelen</a>.</p>
<p><strong>04:00 Los Angeles Lakers – LA Clippers</strong><br>De stadsderby. De Lakers wonnen hun opener met 127-105 van Golden State (Luka Dončić 28 punten), de Clippers wonnen met 121-96 van Sacramento dankzij 30 punten van Darius Garland. De Clippers missen Bradley Beal, Brandon Ingram en Max Strus. De Lakers zijn met 1,25 de grootste favoriet van de nacht. Lees alles in {L['lal']}.</p>
<p><strong>04:00 Sacramento Kings – Portland Trail Blazers</strong><br>Portland begon met 124-83 tegen Phoenix, met 25 punten van Damian Lillard in zijn eerste wedstrijd na een jaar blessureleed en een debuut van Ja Morant. Sacramento verloor met 96-121 bij de Clippers en mist de centers Dylan Cardwell en Maxime Raynaud, plus Ben Simmons. De Blazers wonnen vorig seizoen alle vier de onderlinge duels, maar vaak krap: maar één keer was het verschil groter dan 8,5 punten. Portland is favoriet met 1,31. Wij laten de handicap van -8,5 liggen.</p>
<h3><strong>Wedden op de NBA: zo werkt het</strong></h3>
<p>Bij basketbal is het belangrijk dat je let op de markt waarop je speelt. Bij de markt <strong>Winnaar</strong> (de <a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">moneyline</a>) telt een eventuele verlenging mee: er is altijd een winnaar. Bij de markt <strong>Wedstrijd - Resultaat (excl. OT)</strong> telt alleen de reguliere speeltijd van 48 minuten. Daar kun je ook op een gelijkspel wedden, en staat het na vier kwarten gelijk, dan verlies je een weddenschap op een van beide teams. Vannacht staan de Lakers bijvoorbeeld op 1,25 inclusief verlenging en op 1,23 zonder verlenging, met een gelijkspel op 19,00.</p>
<p>Bij een <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap</a> krijgt het ene team punten voorsprong en het andere achterstand. Bij Hawks -2,5 trekt de bookmaker 2,5 punt af van de score van Atlanta: je wint als de Hawks met drie punten of meer winnen. Bij een puntentotaal (over/under) speel je op het totaal aantal punten van beide teams samen, inclusief een eventuele verlenging. De belangrijkste spelregels lees je in <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de regels van de NBA uitgelegd</a>.</p>
<p>Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit. Twijfel je? Lees <a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>. Alle basketbaltips en voorspellingen vind je op onze pagina <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat beginnen de NBA-wedstrijden vannacht?</strong><br>De eerste wedstrijd, Bucks – Bulls, begint al vrijdagavond om 22:00 Nederlandse tijd. Daarna starten vijf wedstrijden om 01:00 en de laatste drie om 04:00, op zaterdag 24 oktober.</p>
<p><strong>Waarom begint Bucks – Bulls al om 22:00?</strong><br>De Bucks verplaatsten hun thuiswedstrijd naar 15:00 lokale tijd, zodat die niet samenvalt met de eerste World Series-wedstrijd van de Milwaukee Brewers op vrijdagavond.</p>
<p><strong>Waar kan ik de NBA vannacht live zien?</strong><br>Met een account bij Bet365 kun je NBA-wedstrijden live streamen. Daarnaast zendt ESPN in Nederland een deel van de wedstrijden uit en kun je met NBA League Pass alle wedstrijden volgen.</p>
<p><strong>Waar wordt Spurs – Rockets gespeeld?</strong><br>In het Moody Center in Austin. De Spurs zijn wel de thuisploeg: ze spelen sinds 2023 elk seizoen een paar thuiswedstrijden in Austin.</p>
<p><strong>Speelt er een Nederlander vannacht?</strong><br>Ja. Quinten Post speelt met Memphis om 04:00 bij Golden State, waar Malevy Leons onder contract staat. Er kunnen dus twee Nederlanders in dezelfde wedstrijd spelen.</p>
<p><strong>Wat is de beste NBA-tip van vannacht?</strong><br>Onze favoriete tip is Atlanta Hawks -2,5 in Charlotte, met een odd van 1,87 bij TOTO. Een tip blijft een inschatting: zet alleen in wat je kunt missen.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    alles = content + content2 + content3
    tekst = re.sub(r"<[^>]+>", " ", alles)
    woorden = len(tekst.split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", woorden, "woorden |", len(TIPS), "tips")
    assert len(TITEL) <= 60 and 120 <= len(SAMENVATTING) <= 155
    assert 1400 <= woorden <= 2600, woorden   # 12 wedstrijden + 2 tabellen
    assert 1 <= len(TIPS) <= 4 and len(OG_DATA) == 4 and len(OG_CHIPS) == 2 and len(NAMEN) == len(STAKE) == len(TIPS)
    assert all(float(t["odds"]) >= 1.40 for t in TIPS)
    assert not re.search(r"<(ul|ol|/li)>\s+<", alles) and not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert "<h2" not in alles and "<h4" not in alles and "affiliate" not in alles
    assert all(f"<strong>{t} {h} – {u}</strong>" in alles for t, h, u, _, _ in PROGRAMMA)
    assert "<p><strong>Kijken?</strong>" in content
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    print("dry run ok – niets gepubliceerd")
