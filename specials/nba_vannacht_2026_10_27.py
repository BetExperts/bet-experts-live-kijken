# -*- coding: utf-8 -*-
"""Los artikel: NBA voorspellingen vannacht, nacht van maandag 26 op dinsdag 27 oktober 2026 (9 wedstrijden).
Feiten nagelopen op 26-10-2026 (±12:00-13:00 NL): specials/nba_feiten_2026_10_27.md (ESPN-scoreboards, summaries,
teamschema's en box scores 2026/27; blessures ESPN ±12:00 NL; TOTO-odds ±12:45 NL, wedstrijdpagina's).
- 5 toppers hebben een eigen voorbeschouwing (cavaliers_timberwolves, heat_mavericks, thunder_suns, rockets_hawks,
  nuggets_warriors). De tips hier sluiten daarop aan (Wolves +3,5, Under 219,5, Rockets -4,5); Heat -7,5 en
  Nuggets -6,5 staan alleen in hun voorbeschouwing.
- 4 beste tips = grootste verschil tussen onze kans en de kans zonder marge: Wolves +3,5 (56/50,0), Under 219,5
  Thunder – Suns (55/50,8), Grizzlies +1,5 (56/50,8), Rockets -4,5 (59/51,9).
- Vorige nacht (artikel 26 oktober): 3 van 4 raak (Wolves +1,5, Under 236,5 en Pistons +2,5 wel, Thunder -14,5 niet).
- Back-to-back: Timberwolves, Thunder, Pacers, Jazz en Grizzlies speelden zondag (US) ook (Dallas NIET: zaterdag).
  python3 specials/nba_vannacht_2026_10_27.py   (alleen dry run, publiceert niets)
  publiceren: specials/nba_vannacht_publiceer.py nba_vannacht_2026_10_27 --live"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "nba-voorspellingen-vannacht-27-oktober-2026"
RUBRIEK = "672293e14a76d88272bc0b61"   # Basketball
TITEL = "NBA voorspellingen vannacht: 4 beste wedtips (27 oktober)"
SAMENVATTING = ("Negen NBA-wedstrijden vannacht: speeltijden in Nederlandse tijd, korte voorbeschouwing per duel, "
                "onze 4 beste tips en de vijf toppers.")
DATUM = "2026-10-26T23:00:00.000Z"     # eerste wedstrijden: dinsdag 00:00 NL

OG_KOP = "NBA <span>voorspellingen</span> vannacht"
OG_EYEBROW = "Basketbal · 27 oktober"
OG_CHIPS = ["9 wedstrijden", "4 beste tips"]
OG_MOTIEF = "tabel"
OG_DATA = ["CLE-MIN · Wolves +3,5 @1,91", "OKC-PHX · Under 219,5 @1,87", "UTA-MEM · Grizzlies +1,5 @1,87",
           "HOU-ATL · Rockets -4,5 @1,77"]

NAMEN = ["Wolves blijven ongeslagen!", "Thunder smoren de Suns!", "Grizzlies houden stand in Utah!",
         "Rockets doen het opnieuw tegen Atlanta!"]
STAKE = [4, 4, 3, 3]

L = {"cle": '<a href="/nieuws/cavaliers-timberwolves-voorspelling-wedtips-nba-2026">Cavaliers – Timberwolves</a>',
     "mia": '<a href="/nieuws/heat-mavericks-voorspelling-wedtips-nba-2026">Heat – Mavericks</a>',
     "okc": '<a href="/nieuws/thunder-suns-voorspelling-wedtips-nba-2026">Thunder – Suns</a>',
     "hou": '<a href="/nieuws/rockets-hawks-voorspelling-wedtips-nba-2026">Rockets – Hawks</a>',
     "den": '<a href="/nieuws/nuggets-warriors-voorspelling-wedtips-nba-2026">Nuggets – Warriors</a>'}

# (tijd NL, thuis, uit, odd thuis, odd uit)  TOTO 'Winnaar' (incl. verlenging), 26-10 ±12:45
PROGRAMMA = [
    ("00:00", "Charlotte Hornets", "Washington Wizards", 1.80, 2.05),
    ("00:00", "Cleveland Cavaliers", "Minnesota Timberwolves", 1.63, 2.35),
    ("00:30", "Boston Celtics", "Chicago Bulls", 1.13, 6.25),
    ("00:30", "Miami Heat", "Dallas Mavericks", 1.30, 3.65),
    ("01:00", "Milwaukee Bucks", "Indiana Pacers", 2.50, 1.56),
    ("01:00", "Oklahoma City Thunder", "Phoenix Suns", 1.24, 4.15),
    ("01:30", "Houston Rockets", "Atlanta Hawks", 1.51, 2.65),
    ("02:00", "Utah Jazz", "Memphis Grizzlies", 1.83, 2.00),
    ("03:00", "Denver Nuggets", "Golden State Warriors", 1.34, 3.35),
]


def q(x):
    return f"{x:.2f}".replace(".", ",")


def fav(t, u, ot, ou):
    if ot == ou:
        return f"Gelijk ({q(ot)} – {q(ou)})"
    return f"{t} ({q(ot)})" if ot < ou else f"{u} ({q(ou)})"


assert len(PROGRAMMA) == 9

TIPS = [
    {"wedstrijd": "Cleveland Cavaliers vs. Minnesota Timberwolves", "competitie": "NBA", "speeltijd_utc": "2026-10-26T23:00:00Z",
     "tijd_nl": "00:00", "tip": "Minnesota Timberwolves +3,5 (handicap incl. verlenging)", "odds": "1.91", "bookmaker": "toto",
     "analyse": "De Wolves wonnen hun drie duels met gemiddeld 23 punten verschil; Cleveland staat op 1-1."},
    {"wedstrijd": "Oklahoma City Thunder vs. Phoenix Suns", "competitie": "NBA", "speeltijd_utc": "2026-10-27T00:00:00Z",
     "tijd_nl": "01:00", "tip": "Minder dan 219,5 punten (incl. verlenging)", "odds": "1.87", "bookmaker": "toto",
     "analyse": "OKC kreeg gemiddeld 96 punten tegen; de drie Thunder-duels eindigden op 220, 180 en 209 punten."},
    {"wedstrijd": "Utah Jazz vs. Memphis Grizzlies", "competitie": "NBA", "speeltijd_utc": "2026-10-27T01:00:00Z",
     "tijd_nl": "02:00", "tip": "Memphis Grizzlies +1,5 (handicap incl. verlenging)", "odds": "1.87", "bookmaker": "toto",
     "analyse": "Memphis is ongeslagen en won vorige week met 123-103 van Utah; beide ploegen spelen de tweede avond op rij."},
    {"wedstrijd": "Houston Rockets vs. Atlanta Hawks", "competitie": "NBA", "speeltijd_utc": "2026-10-27T00:30:00Z",
     "tijd_nl": "01:30", "tip": "Houston Rockets -4,5 (handicap incl. verlenging)", "odds": "1.77", "bookmaker": "toto",
     "analyse": "Houston won zaterdag al met 121-114 in Atlanta en speelt nu thuis, met een dag rust."},
]

content = f"""<p><strong>In de nacht van maandag op dinsdag staan er negen NBA-wedstrijden op het programma, van 00:00 tot 03:00 Nederlandse tijd. Toppers zijn het duel tussen de ongeslagen Timberwolves en de Cavaliers, Thunder – Suns met Shai Gilgeous-Alexander tegen Devin Booker, de revanche tussen Rockets en Hawks en Jokić tegen Curry in Denver. Onze vier beste voorspellingen: Minnesota Timberwolves +3,5, minder dan 219,5 punten bij Thunder – Suns, Memphis Grizzlies +1,5 en Houston Rockets -4,5.</strong></p>
<p>Vorige nacht kwamen drie van onze vier tips uit: Timberwolves +1,5 (117-94 tegen Toronto), minder dan 236,5 punten bij Kings – Grizzlies (112-123, samen 235) en Pistons +2,5 (Detroit won met 106-93 in Philadelphia). Alleen Thunder -14,5 ging mis: Oklahoma City won met 108-101 van de Clippers. Ook vannacht kiezen we per wedstrijd maar één markt, alleen waar onze eigen inschatting hoger ligt dan de kans in de odd. Let op de vermoeidheid: Minnesota, Oklahoma City, Indiana, Utah en Memphis speelden zondag ook al. Voor de vijf grootste wedstrijden hebben we een uitgebreide voorbeschouwing geschreven.</p>
<p><strong>Kijken?</strong> Heb je een account bij <a href="/bookmakers/bet365">Bet365</a>, dan kun je NBA-wedstrijden daar live streamen. In Nederland zendt ESPN een deel van de NBA-wedstrijden uit en met NBA League Pass, de betaalde dienst van de competitie, zie je ze allemaal. Meer opties lees je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<h3><strong>Het NBA-programma van vannacht (Nederlandse tijd)</strong></h3>
{tabel(["Tijd", "Wedstrijd", "Favoriet volgens de markt"], [
    (f"<strong>{t}</strong>", f"{h} – {u}", fav(h, u, oh, ou)) for t, h, u, oh, ou in PROGRAMMA
])}
<p><em>Alle wedstrijden beginnen in de nacht van maandag op dinsdag 27 oktober. Odds: TOTO, markt Winnaar (inclusief verlenging), stand maandag 26 oktober rond 12:45. Odds kunnen tot de start nog veranderen.</em></p>
<h3><strong>De 4 beste NBA-voorspellingen van vannacht</strong></h3>
{tabel(["Wedstrijd", "Tip", "Odd", "Markt"], [
    ("Cavaliers – Timberwolves (00:00)", "<strong>Timberwolves +3,5</strong>", "1,91", "Handicap, incl. verlenging"),
    ("Thunder – Suns (01:00)", "<strong>Minder dan 219,5 punten</strong>", "1,87", "Totaal, incl. verlenging"),
    ("Jazz – Grizzlies (02:00)", "<strong>Grizzlies +1,5</strong>", "1,87", "Handicap, incl. verlenging"),
    ("Rockets – Hawks (01:30)", "<strong>Rockets -4,5</strong>", "1,77", "Handicap, incl. verlenging"),
])}
<p><em>Alle odds bij <a href="/bookmakers/toto">TOTO</a>, gelezen op maandag 26 oktober rond 12:45. Losse tips, geen combinatie: elke tip staat op zichzelf.</em></p>
<h3><strong>1. Cleveland Cavaliers – Minnesota Timberwolves: Timberwolves +3,5 (1,91)</strong></h3>
<p>Minnesota is indrukwekkend begonnen: drie zeges met gemiddeld 23 punten verschil, 131-106 in Miami, 115-93 in Orlando en zondag 117-94 tegen Toronto. Anthony Edwards scoort 28,7 punten per wedstrijd en LaMelo Ball geeft 6,3 assists in maar 23 minuten. Cleveland staat op 1-1: verlies in Philadelphia (106-114), winst tegen de zwakke Nets (125-121). Donovan Mitchell (27 punten) en James Harden zijn gevaarlijk, maar de Cavaliers zijn verdedigend nog niet op dreef. TOTO maakt Cleveland favoriet met 3,5 punten, vooral omdat Minnesota de tweede avond op rij speelt en Donte DiVincenzo mist. Met +3,5 is de tip ook goed als de Wolves met maximaal drie punten verliezen. De odd staat voor een kans van 50 procent zonder marge; wij schatten die op 56 procent. Het risico: vermoeide benen in het slotkwart. Alles over dit duel lees je in onze voorbeschouwing van {L['cle']}.</p>
<h3><strong>2. Oklahoma City Thunder – Phoenix Suns: minder dan 219,5 punten (1,87)</strong></h3>
<p>Oklahoma City verdedigt weer op topniveau: in drie wedstrijden kreeg de ploeg gemiddeld 96 punten tegen. De Thunder-duels eindigden op 220, 180 en 209 punten. Gilgeous-Alexander maakt 27,7 punten per wedstrijd, maar ook OKC zelf haalde maar één keer meer dan 108. Phoenix leunt zwaar op Devin Booker (33 punten per duel) en ging in Portland met 83-124 onderuit. Daar komt bij dat Oklahoma City zondag nog tegen de Clippers speelde: een vermoeide ploeg speelt vaak langzamer. De odd voor minder dan 219,5 punten staat voor 51 procent zonder marge; wij schatten de kans op 55 procent. Het risico: Booker scoort veel en in een verlenging komen er al snel twintig punten bij. Meer in onze voorbeschouwing van {L['okc']}.</p>
<h3><strong>3. Utah Jazz – Memphis Grizzlies: Grizzlies +1,5 (1,87)</strong></h3>
<p>Memphis is net als Minnesota en Houston nog ongeslagen. Vorige week won de ploeg thuis met 123-103 van Utah, met 45 punten van Ty Jerome, en zondag volgde een 123-112 zege in Sacramento. Jerome staat nu op 34,7 punten per wedstrijd. Utah won pas één keer, met 120-119 tegen New Orleans, en verloor zondag met 123-132 van de Lakers. Beide ploegen spelen de tweede avond op rij, dus vermoeidheid valt tegen elkaar weg. Memphis mist wel center Zach Edey (enkel). Met +1,5 winnen we bij een zege van Memphis en bij een nederlaag met één punt. De odd staat voor 51 procent zonder marge, wij schatten de kans op 56 procent. Het risico: Utah speelt thuis en heeft met Lauri Markkanen, Keyonte George en Jaren Jackson Jr. genoeg scorend vermogen.</p>
<h3><strong>4. Houston Rockets – Atlanta Hawks: Rockets -4,5 (1,77)</strong></h3>
<p>Drie dagen na hun eerste ontmoeting treffen deze ploegen elkaar opnieuw, nu in Houston. Zaterdag won Houston in Atlanta met 121-114, de derde zege in drie wedstrijden. Kevin Durant (24 punten), Alperen Şengün (23 punten, 9 rebounds) en Amen Thompson (17,7 punten, 10,3 rebounds) vormen een sterke kern. Atlanta speelt goed: Jalen Johnson haalt gemiddeld een triple-double (21,7 punten, 10 rebounds, 10 assists) en de Hawks wonnen met 128-81 in Charlotte en met 132-125 in Orlando. Thuis tegen deze Rockets ging het wel mis. Beide ploegen hadden zondag rust. Houston won zaterdag zonder Fred VanVleet, die nu niet meer op de blessurelijst staat. Center Steven Adams ontbreekt wel en achter Marcus Smart staat een vraagteken. De odd staat voor 52 procent zonder marge, wij schatten de kans op een zege met minstens vijf punten op 59 procent. Het risico: Atlanta kent de Rockets nu en kan zich aanpassen. Lees alles in {L['hou']}.</p>"""

content2 = f"""<h3><strong>Alle wedstrijden van vannacht in het kort</strong></h3>
<p><strong>00:00 Charlotte Hornets – Washington Wizards</strong><br>Twee ploegen met 2-1. Charlotte won van Brooklyn en Miami, maar ging thuis met 81-128 onderuit tegen Atlanta. De Hornets missen Kon Knueppel, Coby White en Grant Williams; Naz Reid (20 punten per duel) en Brandon Miller dragen de aanval. Washington heeft met Trae Young (22,3 punten, 11,3 assists) en Anthony Davis (20,7 punten) twee sterren en won zaterdag in Chicago. Charlotte is lichte favoriet met 1,80. Wij zien hier geen duidelijke waarde.</p>
<p><strong>00:00 Cleveland Cavaliers – Minnesota Timberwolves</strong><br>Het ongeslagen Minnesota tegen een uitgerust Cleveland. De Cavaliers zijn favoriet met 1,63, vooral omdat de Wolves de tweede avond op rij spelen. Onze tip: Timberwolves +3,5. Meer in {L['cle']}.</p>
<p><strong>00:30 Boston Celtics – Chicago Bulls</strong><br>Boston staat op 1-1, met Paul George (26,5 punten) en Jayson Tatum (24,5 punten). Chicago won één van de drie wedstrijden en verloor in Toronto met 92-135. De Bulls missen Nic Claxton en achter Patrick Williams staat een vraagteken. Boston is met 1,13 de grootste favoriet van de nacht en moet met 15 punten verschil winnen op de handicap van -14,5. Dat vinden wij een te grote marge om op te spelen.</p>
<p><strong>00:30 Miami Heat – Dallas Mavericks</strong><br>Miami wacht met 0-3 nog op de eerste zege, ondanks 28,3 punten per wedstrijd van Giannis Antetokounmpo. Dallas mist Naji Marshall, Santi Aldama en Dereck Lively II, en achter Cooper Flagg (schouder) staat een vraagteken. De Heat zijn favoriet met 1,30. In onze voorbeschouwing kiezen we voor Heat -7,5 (1,73), maar die tip biedt minder waarde dan onze vier beste. Lees alles in {L['mia']}.</p>
<p><strong>01:00 Milwaukee Bucks – Indiana Pacers</strong><br>Milwaukee staat op 0-3 en verloor van Washington, Chicago en Philadelphia. Tyler Herro (23,7 punten) is de topscorer. Indiana won zondag met 136-109 bij de Nets, dankzij Pascal Siakam (24,7 punten) en Tyrese Haliburton (21,7 punten, 9,7 assists), maar speelt ook de tweede avond op rij en mist T.J. McConnell. De Pacers zijn favoriet met 1,56. Het puntentotaal van 239,5 is het hoogste van de nacht.</p>
<p><strong>01:00 Oklahoma City Thunder – Phoenix Suns</strong><br>De ongeslagen Thunder tegen Booker, die tot nu toe 33 punten per wedstrijd scoort. OKC is favoriet met 1,24. Onze tip: minder dan 219,5 punten. Meer in {L['okc']}.</p>"""

content3 = f"""<p><strong>01:30 Houston Rockets – Atlanta Hawks</strong><br>De tweede ontmoeting in drie dagen, nu in Houston. De Rockets zijn favoriet met 1,51. Onze tip: Rockets -4,5. De volledige analyse lees je in {L['hou']}; het eerste duel bespraken we in <a href="/nieuws/hawks-rockets-voorspelling-wedtips-nba-2026">Hawks – Rockets</a>.</p>
<p><strong>02:00 Utah Jazz – Memphis Grizzlies</strong><br>Ongeslagen Memphis, met Ty Jerome in grootse vorm, in Salt Lake City. Voor Nederlanders is dit de wedstrijd van de nacht: Quinten Post speelt sinds deze zomer voor Memphis en kan zonder de geblesseerde Edey minuten krijgen onder de ring. Beide ploegen spelen de tweede avond op rij. TOTO ziet een bijna gelijk duel: Utah 1,83, Memphis 2,00. Onze tip: Grizzlies +1,5. Meer over de Nederlanders lees je in ons overzicht <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">welke Nederlanders in de NBA spelen</a>.</p>
<p><strong>03:00 Denver Nuggets – Golden State Warriors</strong><br>De laatste wedstrijd van de nacht: Nikola Jokić (24 punten, 11 rebounds, 7,5 assists) en Jamal Murray thuis op hoogte tegen Golden State, dat nog niet won (0-3). De Warriors missen Kristaps Porziņģis en Moses Moody. Denver is favoriet met 1,34. In onze voorbeschouwing kiezen we voor Nuggets -6,5 (1,69). Lees alles in {L['den']}.</p>
<h3><strong>Wedden op de NBA: zo werkt het</strong></h3>
<p>Bij basketbal is het belangrijk dat je let op de markt waarop je speelt. Bij de markt <strong>Winnaar</strong> (de <a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">moneyline</a>) telt een eventuele verlenging mee: er is altijd een winnaar. Bij de markt <strong>Wedstrijd - Resultaat (excl. OT)</strong> telt alleen de reguliere speeltijd van 48 minuten. Daar kun je ook op een gelijkspel wedden, en staat het na vier kwarten gelijk, dan verlies je een weddenschap op een van beide teams.</p>
<p>Bij een <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap</a> krijgt het ene team punten voorsprong en het andere achterstand. Bij Rockets -4,5 moet Houston met minstens vijf punten winnen. Bij Timberwolves +3,5 krijgt Minnesota 3,5 punt voorsprong: je wint als de Wolves winnen of met maximaal drie punten verliezen. Bij een puntentotaal (over/under) speel je op het totaal aantal punten van beide teams samen, inclusief een eventuele verlenging. De belangrijkste spelregels lees je in <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de regels van de NBA uitgelegd</a>.</p>
<p>Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit. Twijfel je? Lees <a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>. Alle basketbaltips en voorspellingen vind je op onze pagina <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>, en de tips van gisteren lees je terug in <a href="/nieuws/nba-voorspellingen-vannacht-26-oktober-2026">NBA voorspellingen van 26 oktober</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat beginnen de NBA-wedstrijden vannacht?</strong><br>De eerste twee wedstrijden, Hornets – Wizards en Cavaliers – Timberwolves, beginnen dinsdag om 00:00 Nederlandse tijd. Daarna volgen er twee om 00:30, twee om 01:00, Rockets – Hawks om 01:30, Jazz – Grizzlies om 02:00 en als laatste Nuggets – Warriors om 03:00.</p>
<p><strong>Waar kan ik de NBA vannacht live zien?</strong><br>Met een account bij Bet365 kun je NBA-wedstrijden live streamen. Daarnaast zendt ESPN in Nederland een deel van de wedstrijden uit en kun je met NBA League Pass alle wedstrijden volgen.</p>
<p><strong>Welke ploegen spelen vannacht de tweede avond op rij?</strong><br>Minnesota Timberwolves, Oklahoma City Thunder, Indiana Pacers, Utah Jazz en Memphis Grizzlies speelden zondag (Amerikaanse tijd) ook al.</p>
<p><strong>Speelt er een Nederlander vannacht?</strong><br>Ja. Quinten Post speelt om 02:00 met Memphis Grizzlies in Utah. Zonder de geblesseerde Zach Edey kan hij meer minuten krijgen.</p>
<p><strong>Wat is de beste NBA-tip van vannacht?</strong><br>Onze favoriete tip is Minnesota Timberwolves +3,5 in Cleveland, met een odd van 1,91 bij TOTO. Een tip blijft een inschatting: zet alleen in wat je kunt missen.</p>
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
    print("dry run ok – niets gepubliceerd")
