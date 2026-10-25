# -*- coding: utf-8 -*-
"""Los artikel: NBA voorspellingen vannacht, zondagavond 25 en nacht van zondag op maandag 26 oktober 2026 (7 wedstrijden).
Feiten nagelopen op 25-10-2026 (±09:30-12:00 NL):
- programma, uitslagen en odds: specials/nba_feiten_2026_10_26.md; overige 4 duels: nba_feiten_overig_2026_10_26.md
  (ESPN-scoreboards/box scores/teamschema's, officieel NBA-injury report 25-10 04:30 ET). Nets 0-2 (niet 0-3).
- de 3 toppers hebben een eigen voorbeschouwing (jazz_lakers, sixers_pistons, thunder_clippers); de tips hier sluiten
  daarop aan (Thunder -14,5 en Pistons +2,5; Jazz +7,5 staat alleen in de voorbeschouwing: kleinere waarde).
- 4 beste tips = grootste verschil tussen onze kans en de kans volgens de odd: Wolves +1,5 (59/55,6), Thunder -14,5
  (58/54,6), Under 236,5 Kings – Grizzlies (55/51,8), Pistons +2,5 (56/53,5).
- Vorige nacht (artikel 25 oktober): 2 van 4 raak (Spurs -11,5 en Bucks +12,5 wel, Hawks wint en Under 218,5 niet).
- Odds: TOTO (sport.toto.nl, wedstrijdpagina's) om ±09:45 NL op 25-10. 'Winnaar' = incl. verlenging. Wintertijd (CET).
  python3 specials/nba_vannacht_2026_10_26.py   (alleen dry run, publiceert niets)
  publiceren: specials/nba_vannacht_publiceer.py nba_vannacht_2026_10_26 --live"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "nba-voorspellingen-vannacht-26-oktober-2026"
RUBRIEK = "672293e14a76d88272bc0b61"   # Basketball
TITEL = "NBA voorspellingen vannacht: 4 beste wedtips (26 oktober)"
SAMENVATTING = ("Zeven NBA-wedstrijden vanavond en vannacht: speeltijden in Nederlandse tijd, korte voorbeschouwing per duel "
                "en onze 4 beste tips.")
DATUM = "2026-10-25T21:00:00.000Z"     # eerste wedstrijd: Jazz – Lakers, zondag 22:00 NL

OG_KOP = "NBA <span>voorspellingen</span> vannacht"
OG_EYEBROW = "Basketbal · 26 oktober"
OG_CHIPS = ["7 wedstrijden", "4 beste tips"]
OG_MOTIEF = "tabel"
OG_DATA = ["MIN-TOR · Wolves +1,5 @1,80", "OKC-LAC · Thunder -14,5 @1,83", "SAC-MEM · Under 236,5 @1,93",
           "PHI-DET · Pistons +2,5 @1,87"]

NAMEN = ["Wolves vieren de thuisopener!", "Thunder walsen over de Clippers!", "Weinig punten in Sacramento!",
         "Pistons profiteren van de vermoeide 76ers!"]
STAKE = [4, 4, 3, 3]

L = {"jazz": '<a href="/nieuws/jazz-lakers-voorspelling-wedtips-nba-2026">Jazz – Lakers</a>',
     "okc": '<a href="/nieuws/thunder-clippers-voorspelling-wedtips-nba-2026">Thunder – Clippers</a>',
     "phi": '<a href="/nieuws/76ers-pistons-voorspelling-wedtips-nba-2026">76ers – Pistons</a>'}

# (tijd NL, thuis, uit, odd thuis, odd uit)  TOTO 'Winnaar' (incl. verlenging), 25-10 ±09:45
PROGRAMMA = [
    ("22:00", "Utah Jazz", "Los Angeles Lakers", 2.95, 1.41),
    ("23:00", "Brooklyn Nets", "Indiana Pacers", 3.10, 1.38),
    ("00:00", "New York Knicks", "Orlando Magic", 1.34, 3.35),
    ("00:00", "Minnesota Timberwolves", "Toronto Raptors", 1.91, 1.91),
    ("00:00", "Oklahoma City Thunder", "LA Clippers", 1.09, 8.20),
    ("00:30", "Philadelphia 76ers", "Detroit Pistons", 1.74, 2.15),
    ("02:00", "Sacramento Kings", "Memphis Grizzlies", 2.50, 1.56),
]


def q(x):
    return f"{x:.2f}".replace(".", ",")


def fav(t, u, ot, ou):
    if ot == ou:
        return f"Gelijk ({q(ot)} – {q(ou)})"
    return f"{t} ({q(ot)})" if ot < ou else f"{u} ({q(ou)})"


assert len(PROGRAMMA) == 7

TIPS = [
    {"wedstrijd": "Minnesota Timberwolves vs. Toronto Raptors", "competitie": "NBA", "speeltijd_utc": "2026-10-25T23:00:00Z",
     "tijd_nl": "00:00", "tip": "Minnesota Timberwolves +1,5 (handicap incl. verlenging)", "odds": "1.80", "bookmaker": "toto",
     "analyse": "Thuisopener van de Wolves, die allebei hun uitduels ruim wonnen en vorig seizoen beide onderlinge duels pakten."},
    {"wedstrijd": "Oklahoma City Thunder vs. LA Clippers", "competitie": "NBA", "speeltijd_utc": "2026-10-25T23:00:00Z",
     "tijd_nl": "00:00", "tip": "Oklahoma City Thunder -14,5 (handicap incl. verlenging)", "odds": "1.83", "bookmaker": "toto",
     "analyse": "OKC won vorig seizoen alle drie de duels met minstens 18 punten; de Clippers missen Beal, Ingram en Strus."},
    {"wedstrijd": "Sacramento Kings vs. Memphis Grizzlies", "competitie": "NBA", "speeltijd_utc": "2026-10-26T01:00:00Z",
     "tijd_nl": "02:00", "tip": "Minder dan 236,5 punten (incl. verlenging)", "odds": "1.93", "bookmaker": "toto",
     "analyse": "De lijn ligt zes punten boven het gemiddelde van dit seizoen; Memphis kreeg pas 103 en 108 punten tegen."},
    {"wedstrijd": "Philadelphia 76ers vs. Detroit Pistons", "competitie": "NBA", "speeltijd_utc": "2026-10-25T23:30:00Z",
     "tijd_nl": "00:30", "tip": "Detroit Pistons +2,5 (handicap incl. verlenging)", "odds": "1.87", "bookmaker": "toto",
     "analyse": "Philadelphia speelt de tweede avond op rij, Detroit is uitgerust en won vorig seizoen alle vier de onderlinge duels."},
]

content = f"""<p><strong>Vanavond om 22:00 begint Utah Jazz – Los Angeles Lakers, en daarna volgen in de nacht van zondag op maandag nog zes NBA-wedstrijden, tot 02:00 Nederlandse tijd. Toppers zijn Jazz – Lakers met Luka Dončić, Thunder – Clippers met MVP Shai Gilgeous-Alexander en het duel tussen de ongeslagen 76ers en Pistons. Onze vier beste voorspellingen: Minnesota Timberwolves +1,5, Oklahoma City Thunder -14,5, minder dan 236,5 punten bij Kings – Grizzlies en Detroit Pistons +2,5.</strong></p>
<p>Vannacht kwamen twee van onze vier tips uit: Spurs -11,5 (122-106) en Bucks +12,5 (116-127) wel, de zege van de Hawks en minder dan 218,5 punten bij Suns – Warriors niet. Ook vandaag kiezen we per wedstrijd maar één markt, alleen waar onze eigen inschatting hoger ligt dan de kans in de odd. Let op de vermoeidheid: de 76ers en de Nets speelden zaterdag ook al. Hieronder vind je het hele programma, per wedstrijd een korte voorbeschouwing en onze vier beste tips met de odds bij TOTO. Voor de drie grootste wedstrijden hebben we een uitgebreide voorbeschouwing geschreven.</p>
<p><strong>Kijken?</strong> Heb je een account bij <a href="/bookmakers/bet365">Bet365</a>, dan kun je NBA-wedstrijden daar live streamen. In Nederland zendt ESPN een deel van de NBA-wedstrijden uit en met NBA League Pass, de betaalde dienst van de competitie, zie je ze allemaal. Meer opties lees je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<h3><strong>Het NBA-programma van vanavond en vannacht (Nederlandse tijd)</strong></h3>
{tabel(["Tijd", "Wedstrijd", "Favoriet volgens de markt"], [
    (f"<strong>{t}</strong>", f"{h} – {u}", fav(h, u, oh, ou)) for t, h, u, oh, ou in PROGRAMMA
])}
<p><em>Jazz – Lakers en Nets – Pacers beginnen zondagavond, de andere vijf wedstrijden in de nacht van zondag op maandag 26 oktober. Odds: TOTO, markt Winnaar (inclusief verlenging), stand zondag 25 oktober rond 10:00. Odds kunnen tot de start nog veranderen.</em></p>
<h3><strong>De 4 beste NBA-voorspellingen van vannacht</strong></h3>
{tabel(["Wedstrijd", "Tip", "Odd", "Markt"], [
    ("Timberwolves – Raptors (00:00)", "<strong>Timberwolves +1,5</strong>", "1,80", "Handicap, incl. verlenging"),
    ("Thunder – Clippers (00:00)", "<strong>Thunder -14,5</strong>", "1,83", "Handicap, incl. verlenging"),
    ("Kings – Grizzlies (02:00)", "<strong>Minder dan 236,5 punten</strong>", "1,93", "Totaal, incl. verlenging"),
    ("76ers – Pistons (00:30)", "<strong>Pistons +2,5</strong>", "1,87", "Handicap, incl. verlenging"),
])}
<p><em>Alle odds bij <a href="/bookmakers/toto">TOTO</a>, gelezen op zondag 25 oktober rond 10:00. Losse tips, geen combinatie: elke tip staat op zichzelf.</em></p>
<h3><strong>1. Minnesota Timberwolves – Toronto Raptors: Timberwolves +1,5 (1,80)</strong></h3>
<p>Twee ploegen met 2-0, maar TOTO ziet een fiftyfifty en maakt de Raptors op de handicap zelfs lichte favoriet. Dat vinden wij te weinig voor Minnesota. De Wolves spelen hun eerste thuiswedstrijd van het seizoen en wonnen hun twee uitduels met 25 en 22 punten verschil: 106-131 in Miami, met 45 punten en negen driepunters van Anthony Edwards, en 93-115 in Orlando. Naast Edwards staan nu ook LaMelo Ball en Jonathan Kuminga in de selectie, en alleen Donte DiVincenzo ontbreekt. Vorig seizoen won Minnesota beide duels met Toronto. De Raptors zijn met Kawhi Leonard en Scottie Barnes wel sterk begonnen (135-92 tegen Chicago en 102-112 in Washington). Met +1,5 is ook een nederlaag met één punt goed. Wij schatten de kans op 59 procent; de odd gaat uit van 56 procent. Het risico: Toronto is uitgerust en Minnesota speelt maandag alweer in Cleveland.</p>
<h3><strong>2. Oklahoma City Thunder – LA Clippers: Thunder -14,5 (1,83)</strong></h3>
<p>Met 1,09 is de winnaar-odd te laag, maar op de handicap zien we wel waarde. Oklahoma City had vorig seizoen met 64-18 het beste record van de NBA en won alle drie de duels met de Clippers met minstens 18 punten verschil, terwijl de Clippers toen nog Kawhi Leonard of James Harden hadden. Dit seizoen gaf OKC in twee wedstrijden gemiddeld maar 94 punten weg. De Clippers missen Bradley Beal, Brandon Ingram en Max Strus, verloren in twee duels 44 keer de bal en spelen hun derde wedstrijd in vijf dagen. Wij schatten de kans dat OKC met 15 punten of meer wint op 58 procent, tegen 55 procent in de odd. Het risico: de Thunder spelen maandag alweer, dus de basisspelers kunnen in een beslist slotkwart op de bank zitten. Alles over dit duel lees je in onze voorbeschouwing van {L['okc']}.</p>
<h3><strong>3. Sacramento Kings – Memphis Grizzlies: minder dan 236,5 punten (1,93)</strong></h3>
<p>Dit is het hoogste totaal van de nacht, terwijl de NBA-wedstrijden dit seizoen gemiddeld op ongeveer 230 punten uitkomen. Memphis is met 2-0 begonnen en kreeg pas 103 en 108 punten tegen; de wedstrijden van de Grizzlies eindigden op 226 en 219 punten. Sacramento scoorde bij de Clippers maar 96 punten, rookie Darius Acuff jr. raakte in twee duels 15 van zijn 50 schoten en achter Keegan Murray staat een vraagteken. Bij Memphis ontbreekt center Zach Edey, die rust op de eerste avond van een back-to-back. Dat kan meer minuten opleveren voor Quinten Post, die in beide wedstrijden van de bank kwam. Wij schatten de kans op minder dan 236,5 punten op 55 procent, tegen 52 procent in de odd. Het risico: de Kings kregen in hun twee duels 121 en 128 punten tegen.</p>
<h3><strong>4. Philadelphia 76ers – Detroit Pistons: Pistons +2,5 (1,87)</strong></h3>
<p>De 76ers zijn met 3-0 begonnen, maar spelen de tweede avond op rij: zaterdag versloegen ze Milwaukee met 127-116, met 36 minuten van Joel Embiid. Die zei vooraf dat hij maar één van de twee wedstrijden dit weekend speelt. Detroit, vorig seizoen met 60-22 de nummer één van het Oosten, had zaterdag rust en won vorig seizoen alle vier de duels met Philadelphia. De Pistons missen wel Jalen Duren (hamstring) en achter Ausar Thompson staat een vraagteken. Met +2,5 winnen we bij een zege van Detroit en bij een nederlaag met één of twee punten. Wij schatten de kans op 56 procent, tegen 53,5 procent in de odd. Het risico: speelt Embiid toch, dan is Philadelphia thuis sterker. Meer in onze voorbeschouwing van {L['phi']}.</p>"""

content2 = f"""<h3><strong>Alle wedstrijden van vanavond en vannacht in het kort</strong></h3>
<p><strong>22:00 Utah Jazz – Los Angeles Lakers</strong><br>De vroegste wedstrijd van de avond, en de eerste uitwedstrijd van de Lakers. Los Angeles won thuis van Golden State (127-105) en de Clippers (125-117), Utah verloor in Memphis en won vrijdag met 120-119 van New Orleans. Voor Walker Kessler, die deze zomer van Utah naar de Lakers ging, is het een weerzien met zijn oude club. De Lakers zijn favoriet met 1,41. Wij kiezen in onze voorbeschouwing voor Utah +7,5 (1,67), maar die odd biedt minder waarde dan onze vier tips. Lees alles in {L['jazz']}.</p>
<p><strong>23:00 Brooklyn Nets – Indiana Pacers</strong><br>De Nets staan op 0-2 en spelen de tweede avond op rij, na een 125-121 nederlaag in Cleveland. Rookie Mikel Brown jr. rust daarom. Indiana won in New Orleans met 123-120 dankzij 30 punten van Pascal Siakam, maar mist T.J. McConnell en Ben Sheppard. Beide ploegen eindigden vorig seizoen onderaan (20-62 en 19-63). De Pacers zijn favoriet met 1,38. De drie onderlinge duels van vorig seizoen bleven allemaal onder de 226 punten; de lijn staat nu op 231,5.</p>
<p><strong>00:00 New York Knicks – Orlando Magic</strong><br>De regerend kampioen staat nog op 0-2. New York verloor van Philadelphia (100-106) en in Boston (103-107), en Mikal Bridges raakte in die twee wedstrijden maar 2 van zijn 16 schoten. Orlando mist Paolo Banchero met een enkelblessure en ook achter Anthony Black staat een vraagteken. De Knicks zijn favoriet met 1,34. Vorig seizoen won Orlando zonder Banchero wel zeven van de tien wedstrijden, dus onderschat de Magic niet.</p>
<p><strong>00:00 Minnesota Timberwolves – Toronto Raptors</strong><br>Allebei 2-0 en allebei uitgerust. De thuisopener van Minnesota, met Edwards, Ball en Rudy Gobert tegen Leonard, Barnes en Jakob Pöltl. TOTO zet beide ploegen op 1,91. Onze tip: Timberwolves +1,5.</p>
<p><strong>00:00 Oklahoma City Thunder – LA Clippers</strong><br>De ploeg van MVP Gilgeous-Alexander tegen een uitgedunde Clippers-selectie, waarin Darius Garland nu de aanval leidt. Met 1,09 de grootste favoriet van de nacht. Onze tip: Thunder -14,5. Meer in {L['okc']}.</p>
<p><strong>00:30 Philadelphia 76ers – Detroit Pistons</strong><br>Twee ongeslagen ploegen uit het Oosten tegen elkaar. Philadelphia is favoriet met 1,74, maar speelt de tweede avond op rij. Onze tip: Pistons +2,5. De volledige analyse lees je in {L['phi']}.</p>"""

content3 = f"""<p><strong>02:00 Sacramento Kings – Memphis Grizzlies</strong><br>Memphis staat op 2-0 dankzij Ty Jerome, die 45 en 28 punten maakte. Voor Nederlanders is dit de wedstrijd van de nacht: Quinten Post speelt sinds deze zomer voor Memphis en kan zonder Edey meer minuten krijgen. Sacramento staat op 0-2 en mist naast Ben Simmons ook de centers Dylan Cardwell en Maxime Raynaud. De Grizzlies zijn favoriet met 1,56. Onze tip: minder dan 236,5 punten. Meer over de Nederlanders lees je in ons overzicht <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">welke Nederlanders in de NBA spelen</a>.</p>
<h3><strong>Wedden op de NBA: zo werkt het</strong></h3>
<p>Bij basketbal is het belangrijk dat je let op de markt waarop je speelt. Bij de markt <strong>Winnaar</strong> (de <a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">moneyline</a>) telt een eventuele verlenging mee: er is altijd een winnaar. Bij de markt <strong>Wedstrijd - Resultaat (excl. OT)</strong> telt alleen de reguliere speeltijd van 48 minuten. Daar kun je ook op een gelijkspel wedden, en staat het na vier kwarten gelijk, dan verlies je een weddenschap op een van beide teams.</p>
<p>Bij een <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap</a> krijgt het ene team punten voorsprong en het andere achterstand. Bij Thunder -14,5 moet Oklahoma City met minstens 15 punten winnen. Bij Pistons +2,5 krijgt Detroit 2,5 punt voorsprong: je wint als de Pistons winnen of met maximaal twee punten verliezen. Bij een puntentotaal (over/under) speel je op het totaal aantal punten van beide teams samen, inclusief een eventuele verlenging. De belangrijkste spelregels lees je in <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de regels van de NBA uitgelegd</a>.</p>
<p>Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit. Twijfel je? Lees <a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>. Alle basketbaltips en voorspellingen vind je op onze pagina <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>, en de tips van vannacht lees je terug in <a href="/nieuws/nba-voorspellingen-vannacht-25-oktober-2026">NBA voorspellingen van 25 oktober</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat beginnen de NBA-wedstrijden vanavond en vannacht?</strong><br>De eerste wedstrijd, Jazz – Lakers, begint zondagavond om 22:00 Nederlandse tijd, Nets – Pacers om 23:00. Daarna volgen drie wedstrijden om 00:00, 76ers – Pistons om 00:30 en als laatste Kings – Grizzlies om 02:00.</p>
<p><strong>Waar kan ik de NBA vannacht live zien?</strong><br>Met een account bij Bet365 kun je NBA-wedstrijden live streamen. Daarnaast zendt ESPN in Nederland een deel van de wedstrijden uit en kun je met NBA League Pass alle wedstrijden volgen.</p>
<p><strong>Speelt Joel Embiid tegen Detroit?</strong><br>Dat is nog niet zeker. Embiid speelde zaterdag 36 minuten tegen Milwaukee en zei vooraf dat hij maar één van de twee wedstrijden dit weekend speelt. De officiële blessurelijst van Philadelphia volgt later op de dag.</p>
<p><strong>Speelt er een Nederlander vannacht?</strong><br>Ja. Quinten Post speelt om 02:00 met Memphis Grizzlies in Sacramento. Zonder de geblesseerde Zach Edey kan hij meer minuten krijgen.</p>
<p><strong>Wat is de beste NBA-tip van vannacht?</strong><br>Onze favoriete tip is Minnesota Timberwolves +1,5 tegen Toronto, met een odd van 1,80 bij TOTO. Een tip blijft een inschatting: zet alleen in wat je kunt missen.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    alles = content + content2 + content3
    tekst = re.sub(r"<[^>]+>", " ", alles)
    woorden = len(tekst.split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", woorden, "woorden |", len(TIPS), "tips")
    assert len(TITEL) <= 60 and 120 <= len(SAMENVATTING) <= 155
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
    print("dry run ok – niets gepubliceerd")
