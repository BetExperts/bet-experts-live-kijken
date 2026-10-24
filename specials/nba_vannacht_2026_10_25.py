# -*- coding: utf-8 -*-
"""Los artikel: NBA voorspellingen vannacht, nacht van zaterdag 24 op zondag 25 oktober 2026 (8 wedstrijden).
Feiten nagelopen op 24-10-2026 (±13:00 NL):
- programma, uitslagen en blessures: specials/nba_feiten_2026_10_25.md + nba_feiten_overig_2026_10_25.md
  (ESPN-scoreboard/box scores, officieel NBA-injury report 24-10 07:00 ET);
- de 4 toppers hebben een eigen voorbeschouwing (sixers_bucks, mavericks_spurs, hawks_rockets, suns_warriors);
  de 4 tips hier zijn precies die tips (grootste verschil tussen onze kans en de odd; de overige 4 duels 1-3 procentpunt).
- Wintertijd: om 03:00 gaat de klok terug naar 02:00. Nuggets – Pelicans (01:00 UTC) = 02:00 wintertijd,
  Suns – Warriors (02:00 UTC) = 03:00 wintertijd; de rest begint nog in zomertijd.
- Odds: TOTO (sport.toto.nl, wedstrijdpagina's) om ±13:00 NL op 24-10. 'Winnaar' = incl. verlenging.
  python3 specials/nba_vannacht_2026_10_25.py   (alleen dry run, publiceert niets)
  publiceren: specials/nba_vannacht_publiceer.py nba_vannacht_2026_10_25 --live"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "nba-voorspellingen-vannacht-25-oktober-2026"
RUBRIEK = "672293e14a76d88272bc0b61"   # Basketball
TITEL = "NBA voorspellingen vannacht: 4 beste wedtips (25 oktober)"
SAMENVATTING = ("Acht NBA-wedstrijden vannacht: speeltijden in Nederlandse tijd (let op de wintertijd), korte voorbeschouwing "
                "per duel en onze 4 beste tips.")
DATUM = "2026-10-24T22:00:00.000Z"     # eerste wedstrijd: Hornets – Heat, zondag 00:00 NL

OG_KOP = "NBA <span>voorspellingen</span> vannacht"
OG_EYEBROW = "Basketbal · 25 oktober"
OG_CHIPS = ["8 wedstrijden", "4 beste tips"]
OG_MOTIEF = "tabel"
OG_DATA = ["PHX-GSW · Under 218,5 @1,93", "DAL-SAS · Spurs -11,5 @1,78", "PHI-MIL · Bucks +12,5 @1,91",
           "ATL-HOU · Hawks wint @1,83"]

NAMEN = ["Weinig punten in Phoenix zonder Curry!", "Spurs walsen over Dallas!", "Bucks blijven binnen bereik in Philly!",
         "Hawks hebben de frissere benen!"]
STAKE = [4, 4, 3, 3]

L = {"phi": '<a href="/nieuws/76ers-bucks-voorspelling-wedtips-nba-2026">76ers – Bucks</a>',
     "dal": '<a href="/nieuws/mavericks-spurs-voorspelling-wedtips-nba-2026">Mavericks – Spurs</a>',
     "atl": '<a href="/nieuws/hawks-rockets-voorspelling-wedtips-nba-2026">Hawks – Rockets</a>',
     "phx": '<a href="/nieuws/suns-warriors-voorspelling-wedtips-nba-2026">Suns – Warriors</a>'}

# (tijd NL, thuis, uit, odd thuis, odd uit)  TOTO 'Winnaar' (incl. verlenging), 24-10 ±13:00
PROGRAMMA = [
    ("00:00", "Charlotte Hornets", "Miami Heat", 2.30, 1.67),
    ("01:30", "Cleveland Cavaliers", "Brooklyn Nets", 1.18, 5.00),
    ("01:30", "Philadelphia 76ers", "Milwaukee Bucks", 1.14, 5.95),
    ("02:00", "Chicago Bulls", "Washington Wizards", 2.00, 1.83),
    ("02:00", "Dallas Mavericks", "San Antonio Spurs", 5.15, 1.18),
    ("02:30", "Atlanta Hawks", "Houston Rockets", 1.83, 2.00),
    ("02:00 (wintertijd)", "Denver Nuggets", "New Orleans Pelicans", 1.20, 4.75),
    ("03:00 (wintertijd)", "Phoenix Suns", "Golden State Warriors", 1.26, 4.05),
]


def q(x):
    return f"{x:.2f}".replace(".", ",")


def fav(t, u, ot, ou):
    if ot == ou:
        return f"Gelijk ({q(ot)} – {q(ou)})"
    return f"{t} ({q(ot)})" if ot < ou else f"{u} ({q(ou)})"


assert len(PROGRAMMA) == 8

TIPS = [
    {"wedstrijd": "Phoenix Suns vs. Golden State Warriors", "competitie": "NBA", "speeltijd_utc": "2026-10-25T02:00:00Z",
     "tijd_nl": "03:00", "tip": "Minder dan 218,5 punten (incl. verlenging)", "odds": "1.93", "bookmaker": "toto",
     "analyse": "Golden State speelt de tweede avond op rij en waarschijnlijk zonder Curry en Podziemski; drie van de vijf duels van vorig seizoen bleven onder de 210 punten."},
    {"wedstrijd": "Dallas Mavericks vs. San Antonio Spurs", "competitie": "NBA", "speeltijd_utc": "2026-10-25T00:00:00Z",
     "tijd_nl": "02:00", "tip": "San Antonio Spurs -11,5 (handicap incl. verlenging)", "odds": "1.78", "bookmaker": "toto",
     "analyse": "De Spurs wonnen alle vier de duels van vorig seizoen met minstens twaalf punten; Dallas mist waarschijnlijk Flagg en zeker Lively en Aldama."},
    {"wedstrijd": "Philadelphia 76ers vs. Milwaukee Bucks", "competitie": "NBA", "speeltijd_utc": "2026-10-24T23:30:00Z",
     "tijd_nl": "01:30", "tip": "Milwaukee Bucks +12,5 (handicap incl. verlenging)", "odds": "1.91", "bookmaker": "toto",
     "analyse": "James is twijfelachtig en Embiid speelt maar één van de twee duels dit weekend; Philadelphia won zijn eerste twee wedstrijden met zes en acht punten."},
    {"wedstrijd": "Atlanta Hawks vs. Houston Rockets", "competitie": "NBA", "speeltijd_utc": "2026-10-25T00:30:00Z",
     "tijd_nl": "02:30", "tip": "Atlanta Hawks wint (incl. verlenging)", "odds": "1.83", "bookmaker": "toto",
     "analyse": "Atlanta spaarde vrijdag bij 128-81 in Charlotte zijn basisspelers, Houston moest in Austin tot de laatste seconde knokken en vloog daarna ver."},
]

content = f"""<p><strong>In de nacht van zaterdag op zondag staan er acht NBA-wedstrijden op het programma, van 00:00 tot 03:00 Nederlandse tijd. Let op: om 03:00 gaat de klok een uur terug, dus de laatste twee wedstrijden beginnen in wintertijd. Toppers zijn 76ers – Bucks, de Texas-derby Mavericks – Spurs, Hawks – Rockets met twee ongeslagen ploegen en Suns – Warriors. Onze vier beste voorspellingen: minder dan 218,5 punten in Phoenix, Spurs -11,5 in Dallas, Bucks +12,5 in Philadelphia en een zege van de Atlanta Hawks.</strong></p>
<p>Gisteren kwamen al onze vier tips uit. Ook vannacht kiezen we per wedstrijd maar één markt, en alleen waar onze eigen inschatting duidelijk hoger ligt dan de kans in de odd. Vermoeidheid speelt vannacht een grote rol: Hornets, Heat, Bucks, Bulls, Wizards, Mavericks, Spurs, Hawks, Rockets, Pelicans en Warriors speelden vrijdag ook al. Hieronder vind je het hele programma, per wedstrijd een korte voorbeschouwing en onze vier beste tips met de odds bij TOTO. Voor de vier grootste wedstrijden hebben we een uitgebreide voorbeschouwing geschreven.</p>
<p><strong>Kijken?</strong> Heb je een account bij <a href="/bookmakers/bet365">Bet365</a>, dan kun je NBA-wedstrijden daar live streamen. In Nederland zendt ESPN een deel van de NBA-wedstrijden uit en met NBA League Pass, de betaalde dienst van de competitie, zie je ze allemaal. Meer opties lees je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<h3><strong>Het NBA-programma van vannacht (Nederlandse tijd)</strong></h3>
{tabel(["Tijd", "Wedstrijd", "Favoriet volgens de markt"], [
    (f"<strong>{t}</strong>", f"{h} – {u}", fav(h, u, oh, ou)) for t, h, u, oh, ou in PROGRAMMA
])}
<p><em>Alle wedstrijden zijn op zondag 25 oktober. Tot 03:00 geldt de zomertijd; Nuggets – Pelicans en Suns – Warriors beginnen na de omschakeling, om 02:00 en 03:00 wintertijd. Odds: TOTO, markt Winnaar (inclusief verlenging), stand zaterdag 24 oktober rond 13:00. Odds kunnen tot de start nog veranderen.</em></p>
<h3><strong>De 4 beste NBA-voorspellingen van vannacht</strong></h3>
{tabel(["Wedstrijd", "Tip", "Odd", "Markt"], [
    ("Suns – Warriors (03:00, wintertijd)", "<strong>Minder dan 218,5 punten</strong>", "1,93", "Totaal, incl. verlenging"),
    ("Mavericks – Spurs (02:00)", "<strong>Spurs -11,5</strong>", "1,78", "Handicap, incl. verlenging"),
    ("76ers – Bucks (01:30)", "<strong>Bucks +12,5</strong>", "1,91", "Handicap, incl. verlenging"),
    ("Hawks – Rockets (02:30)", "<strong>Atlanta Hawks wint</strong>", "1,83", "Winnaar, incl. verlenging"),
])}
<p><em>Alle odds bij <a href="/bookmakers/toto">TOTO</a>, gelezen op zaterdag 24 oktober rond 13:00. Losse tips, geen combinatie: elke tip staat op zichzelf.</em></p>
<h3><strong>1. Phoenix Suns – Golden State Warriors: minder dan 218,5 punten (1,93)</strong></h3>
<p>Golden State speelt de tweede avond op rij en doet dat waarschijnlijk zonder Stephen Curry en Brandin Podziemski. Curry liet na de nederlaag tegen Memphis doorschemeren dat hij in Phoenix rust neemt; Podziemski (rug) zei zelf al dat hij niet speelt. Samen waren ze vorig seizoen goed voor 40,4 punten per wedstrijd. Ook met Curry raakte Golden State in de opener maar 22 procent van zijn driepunters. Phoenix scoort evenmin makkelijk: de Suns gingen in hun enige wedstrijd met 83-124 onderuit in Portland en raakten maar 6 van de 32 driepunters. Drie van de vijf duels tussen deze ploegen bleven vorig seizoen ver onder de lijn, met 197, 198 en 207 punten. Wij schatten de kans op minder dan 218,5 punten op 57 procent; de odd gaat uit van zo'n 52 procent. Het risico: speelt Curry toch, dan kan hij het totaal in zijn eentje opdrijven. Alles over dit duel lees je in onze voorbeschouwing van {L['phx']}.</p>
<h3><strong>2. Dallas Mavericks – San Antonio Spurs: Spurs -11,5 (1,78)</strong></h3>
<p>De Spurs staan nog op 0-2, maar zijn met 1,18 een van de grootste favorieten van de nacht. Dat heeft een reden. Dallas moet het in zijn thuisopener waarschijnlijk zonder Cooper Flagg doen, die vrijdag in Indianapolis hard op zijn linkerschouder viel na een flagrant foul en na rust niet meer terugkwam. Ook Dereck Lively II en Santi Aldama ontbreken, waardoor Dallas weinig lengte heeft tegen Victor Wembanyama. Kyrie Irving speelt met een beperkt aantal minuten. San Antonio won alle vier de duels van vorig seizoen met minstens twaalf punten verschil (33, 12, 13 en 19), en toen speelde Flagg wel. Bovendien won San Antonio vorig seizoen 12 van zijn 15 tweede wedstrijden van een back-to-back. Wij schatten de kans op een Spurs-zege met twaalf punten of meer op 61 procent, tegen 56 procent in de odd. Het risico: speelt Flagg toch, of krijgt Wembanyama rust, dan verandert het beeld. Controleer de opstellingen vlak voor het begin. Meer in onze voorbeschouwing van {L['dal']}.</p>
<h3><strong>3. Philadelphia 76ers – Milwaukee Bucks: Bucks +12,5 (1,91)</strong></h3>
<p>Philadelphia is met 1,14 zwaar favoriet, maar wij verwachten geen afgang. De 76ers wonnen hun eerste twee wedstrijden met zes en acht punten verschil en raakten maar 26,5 procent van hun driepunters. LeBron James staat als twijfelachtig op de officiële blessurelijst (onderrug) en Joel Embiid speelt naar eigen zeggen maar één van de twee wedstrijden dit weekend; zondag wacht Detroit al. Milwaukee, na het vertrek van Giannis Antetokounmpo aan een nieuwe start bezig, scoorde 116 en 125 punten met Tyler Herro en Jaime Jaquez jr. Hun wedstrijd van vrijdag tegen Chicago werd naar de middag verplaatst, dus de Bucks hadden extra tijd om bij te komen. Wij schatten de kans dat de Bucks binnen twaalf punten blijven (of winnen) op 56 procent, tegen ruim 52 procent in de odd. Het risico: de verdediging van Milwaukee kreeg in twee wedstrijden 260 punten tegen. Spelen James en Embiid allebei en valt het schot van Philadelphia wel, dan kan het hard gaan. Lees alles in {L['phi']}.</p>
<h3><strong>4. Atlanta Hawks – Houston Rockets: Hawks wint (1,83)</strong></h3>
<p>Twee ploegen met 2-0, maar met een heel andere vrijdagavond. Atlanta won met 128-81 in Charlotte en geen enkele basisspeler stond langer dan 29 minuten op het veld. Houston won in Austin met 114-110 van de Spurs, pas na een block van Amen Thompson op Wembanyama in de slotseconde. Kevin Durant speelde 37 minuten, Alperen Şengün en Thompson 36, en daarna volgde een vlucht van ruim 1.300 kilometer. Atlanta heeft bovendien de bredere selectie, en de verdediging met Dyson Daniels en Luguentz Dort dwong in twee wedstrijden samen 47 balverliezen af. Wij schatten de winkans van de Hawks op 58 procent; de odd van 1,83 gaat zonder de marge van de bookmaker uit van zo'n 52 procent. Het risico: Houston was vorig seizoen de betere ploeg en won beide onderlinge duels, en Durant kan een slotfase in zijn eentje beslissen. Meer in onze voorbeschouwing van {L['atl']}.</p>"""

content2 = f"""<h3><strong>Alle wedstrijden van vannacht in het kort</strong></h3>
<p><strong>00:00 Charlotte Hornets – Miami Heat</strong><br>Beide ploegen speelden vrijdag ook al. Charlotte verloor thuis met 81-128 van Atlanta en mist mogelijk opnieuw Kon Knueppel, Coby White en Grant Williams, die vrijdag ontbraken. Brandon Miller raakte in twee wedstrijden maar 9 van zijn 35 schoten. Miami verloor met 111-128 van Detroit en staat op 0-2, ondanks 35 en 36 punten van Giannis Antetokounmpo. De Heat speelden vrijdagavond nog thuis en moesten daarna reizen; of Giannis op de tweede avond speelt, is niet bekend. Miami is favoriet met 1,67. Wij verwachten weinig punten, maar de waarde op de lijn van 230,5 is te klein voor onze top 4.</p>
<p><strong>01:30 Cleveland Cavaliers – Brooklyn Nets</strong><br>De thuisopener van Cleveland, dat donderdag met 106-114 in Philadelphia verloor ondanks 32 punten van Donovan Mitchell. Brooklyn verloor thuis met 103-110 van Charlotte (Julius Randle 33 punten) en eindigde vorig seizoen op 20-62. Beide ploegen zijn uitgerust, en bij geen van beide ontbreekt een vaste basisspeler. Met 1,18 zijn de Cavaliers de grote favoriet; die odd is ons te laag. Voor Nederlanders: Tristan Enaruna staat met een two-waycontract op de selectie van Cleveland, maar kreeg in de opener geen speeltijd.</p>
<p><strong>01:30 Philadelphia 76ers – Milwaukee Bucks</strong><br>Philadelphia (2-0) tegen Milwaukee (0-2). De 76ers wonnen vorig seizoen alle vier de onderlinge duels, maar achter James en Embiid staat een vraagteken. Onze tip: Bucks +12,5. Meer in {L['phi']}.</p>
<p><strong>02:00 Chicago Bulls – Washington Wizards</strong><br>Ook dit is een thuisopener, en ook hier spelen beide ploegen de tweede avond op rij. Chicago won vrijdag met 132-125 in Milwaukee, in een wedstrijd die al 's middags begon en op korte afstand van huis. Washington speelde vrijdagavond nog thuis (102-112 tegen Toronto) en vloog daarna. De Bulls wonnen vorig seizoen alle drie de onderlinge duels. Anthony Davis scoorde in de opener 34 punten voor de Wizards, maar vrijdag maar 9; nummer één van de draft AJ Dybantsa (enkel) is onzeker. TOTO ziet Washington als lichte favoriet (1,83 tegen 2,00 op Chicago). Wij geven de Bulls een kleine voorkeur, maar het verschil is te klein voor onze top 4.</p>
<p><strong>02:00 Dallas Mavericks – San Antonio Spurs</strong><br>De thuisopener van Dallas, waarschijnlijk zonder Cooper Flagg. De Spurs wachten na 0-2 nog op hun eerste zege. Onze tip: Spurs -11,5. Alles over dit duel lees je in {L['dal']}.</p>
<p><strong>02:30 Atlanta Hawks – Houston Rockets</strong><br>Twee ploegen met 2-0. Atlanta is uitgeruster na een ruime zege in Charlotte, Houston moest vrijdag tot het einde knokken in Austin. Onze tip: Hawks wint. Meer in {L['atl']}.</p>"""

content3 = f"""<p><strong>02:00 (wintertijd) Denver Nuggets – New Orleans Pelicans</strong><br>Door de omschakeling naar de wintertijd begint deze wedstrijd in werkelijkheid na Hawks – Rockets. Denver speelt zijn thuisopener na een 84-96 nederlaag in Oklahoma City, waarin Nikola Jokić maar 5 van zijn 19 schoten raakte. Cameron Johnson (enkel) ontbreekt. New Orleans staat op 0-2, verloor vrijdag laat met 119-120 in Utah en speelt nu de tweede avond op rij, op 1.600 meter hoogte. Center Yves Missi viel vrijdag uit met een knieblessure. De Nuggets wonnen vorig seizoen alle drie de onderlinge duels en zijn favoriet met 1,20. De handicap van -11,5 vinden we interessant, maar de waarde is kleiner dan bij onze vier tips.</p>
<p><strong>03:00 (wintertijd) Phoenix Suns – Golden State Warriors</strong><br>De laatste wedstrijd van de nacht. Phoenix had twee rustdagen, Golden State speelt de tweede avond op rij en waarschijnlijk zonder Curry. Onze tip: minder dan 218,5 punten. De volledige analyse lees je in {L['phx']}.</p>
<h3><strong>Wedden op de NBA: zo werkt het</strong></h3>
<p>Bij basketbal is het belangrijk dat je let op de markt waarop je speelt. Bij de markt <strong>Winnaar</strong> (de <a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">moneyline</a>) telt een eventuele verlenging mee: er is altijd een winnaar. Bij de markt <strong>Wedstrijd - Resultaat (excl. OT)</strong> telt alleen de reguliere speeltijd van 48 minuten. Daar kun je ook op een gelijkspel wedden, en staat het na vier kwarten gelijk, dan verlies je een weddenschap op een van beide teams. Daarom kiezen we bij Hawks – Rockets voor de markt Winnaar.</p>
<p>Bij een <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap</a> krijgt het ene team punten voorsprong en het andere achterstand. Bij Bucks +12,5 krijgt Milwaukee 12,5 punten voorsprong: je wint als de Bucks winnen of met maximaal twaalf punten verliezen. Bij Spurs -11,5 moet San Antonio juist met minstens twaalf punten winnen. Bij een puntentotaal (over/under) speel je op het totaal aantal punten van beide teams samen, inclusief een eventuele verlenging. De belangrijkste spelregels lees je in <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de regels van de NBA uitgelegd</a>.</p>
<p>Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit. Twijfel je? Lees <a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>. Alle basketbaltips en voorspellingen vind je op onze pagina <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>, en de tips van gisteren lees je terug in <a href="/nieuws/nba-voorspellingen-vannacht-24-oktober-2026">NBA voorspellingen van 24 oktober</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat beginnen de NBA-wedstrijden vannacht?</strong><br>De eerste wedstrijd, Hornets – Heat, begint om 00:00 Nederlandse tijd. Daarna volgen wedstrijden om 01:30, 02:00 en 02:30. Na de omschakeling naar de wintertijd beginnen Nuggets – Pelicans om 02:00 en Suns – Warriors om 03:00.</p>
<p><strong>Wat betekent de wintertijd voor de aanvangstijden?</strong><br>Om 03:00 zomertijd gaat de klok terug naar 02:00. Daardoor begint Nuggets – Pelicans om 02:00 wintertijd, een uur na Bulls – Wizards en Mavericks – Spurs, die om 02:00 zomertijd beginnen.</p>
<p><strong>Waar kan ik de NBA vannacht live zien?</strong><br>Met een account bij Bet365 kun je NBA-wedstrijden live streamen. Daarnaast zendt ESPN in Nederland een deel van de wedstrijden uit en kun je met NBA League Pass alle wedstrijden volgen.</p>
<p><strong>Speelt Stephen Curry vannacht?</strong><br>Waarschijnlijk niet. Curry zei na de nederlaag tegen Memphis dat hij in Phoenix waarschijnlijk rust neemt. De officiële blessurelijst van Golden State volgt later op de dag.</p>
<p><strong>Speelt er een Nederlander vannacht?</strong><br>Mogelijk. Malevy Leons heeft een two-waycontract bij Golden State, dat om 03:00 in Phoenix speelt; met zoveel afwezigen is de kans op minuten groter dan normaal. Tristan Enaruna staat met een two-waycontract op de selectie van Cleveland (01:30 tegen Brooklyn), maar kreeg in de opener geen speeltijd. Meer lees je in ons overzicht <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">welke Nederlanders in de NBA spelen</a>.</p>
<p><strong>Wat is de beste NBA-tip van vannacht?</strong><br>Onze favoriete tip is minder dan 218,5 punten bij Suns – Warriors, met een odd van 1,93 bij TOTO. Een tip blijft een inschatting: zet alleen in wat je kunt missen.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    alles = content + content2 + content3
    tekst = re.sub(r"<[^>]+>", " ", alles)
    woorden = len(tekst.split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", woorden, "woorden |", len(TIPS), "tips")
    assert len(TITEL) <= 60 and 120 <= len(SAMENVATTING) <= 155
    assert 1400 <= woorden <= 2600, woorden   # 8 wedstrijden + 2 tabellen
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
