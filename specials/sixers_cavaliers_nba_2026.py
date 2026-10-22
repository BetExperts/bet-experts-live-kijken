# -*- coding: utf-8 -*-
"""Los artikel: 76ers – Cavaliers voorspelling, NBA 23 oktober 2026 (01:00 NL). Feiten nagelopen op 22-10-2026
(NBA.com, officiele NBA-blessurelijst 22-10 03:00 ET, ESPN, AP/Reuters, Yahoo Sports, PhillyVoice, StatMuse, Wikipedia).
- 76ers-Knicks 106-100 op 20-10 (Maxey 28, Brown 19, James 14/9/7, Embiid 13/11/6). Cleveland speelt zijn eerste duel.
- Odds: TOTO gelezen op sport.toto.nl/wedden/wedstrijd/12223938 om 09:18 NL op 22-10; Circus om 09:20 NL.
  'Winnaar' = incl. verlenging; 'Wedstrijd - Resultaat (excl. OT)' = 1X2 na 48 minuten.
  python3 specials/sixers_cavaliers_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "76ers – Cavaliers voorspelling: wedtips en odds bij thuisdebuut LeBron (23 oktober, 01:00)"
SLUG = "76ers-cavaliers-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("LeBron James speelt zijn eerste thuisduel voor de 76ers, tegen Cleveland. Voorspelling, wedtips, odds, "
                "blessures en opstellingen.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet365.nl/hub/nl-nl/open-account?affiliate=365_02599619"

# Deelkaart (maatwerk-kaart in de nieuwe stijl)
OG_KOP = "76ers – Cavaliers <span>voorspelling</span>"
OG_EYEBROW = "NBA · vrijdag 23 oktober, 01:00"
OG_CHIPS = ["Thuisdebuut LeBron", "3 wedtips"]
OG_MOTIEF = "tabel"
OG_DATA = ["Aftrap · 01:00", "Arena · Xfinity Mobile Arena", "Onderling 25/26 · 4-0 Cavs", "Favoriet · 76ers"]

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>In de nacht van donderdag op vrijdag om 01:00 Nederlandse tijd speelt LeBron James zijn eerste thuiswedstrijd voor de Philadelphia 76ers. De tegenstander is uitgerekend Cleveland, de club waar hij groot werd. Philadelphia won dinsdag al bij kampioen New York, voor de Cavaliers is het de eerste wedstrijd van het seizoen. Onze voorspelling: de 76ers winnen met 115-108. Hoofdtip: Philadelphia wint, met minder dan 235,5 punten als tweede tip.</strong></p>
<p>Weinig ploegen veranderden deze zomer zo sterk als Philadelphia. Naast Tyrese Maxey en Joel Embiid staan nu ook Jaylen Brown en LeBron James in de basis. Cleveland koos voor rust: de kern met Donovan Mitchell, James Harden, Evan Mobley en Jarrett Allen bleef bij elkaar. Vorig seizoen won Cleveland alle vier de onderlinge duels. Hieronder lees je wat er veranderd is, wie er speelt, wat de bookmakers verwachten en welke weddenschappen wij interessant vinden.</p>
<h3><strong>76ers – Cavaliers: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "Philadelphia 76ers – Cleveland Cavaliers"),
    ("Datum", "Vrijdag 23 oktober 2026 (nacht van donderdag op vrijdag)"),
    ("Aanvang", "01:00 Nederlandse tijd (19:00 in Philadelphia)"),
    ("Arena", "Xfinity Mobile Arena, Philadelphia"),
    ("Competitie", "NBA, reguliere competitie 2026/27"),
    ("Stand 2026/27", "76ers 1-0, Cavaliers nog geen wedstrijd gespeeld"),
    ("Onderlinge duels 2025/26", "4-0 voor de Cavaliers"),
])}
<p>De 76ers zijn de thuisploeg. Beide ploegen treffen elkaar dit seizoen nog twee keer, allebei in Cleveland: op 7 november (01:30 Nederlandse tijd) en op 2 maart 2027 (01:00).</p>
<p>Philadelphia begon het seizoen dinsdag met een 100-106 zege in Madison Square Garden, op de avond dat de Knicks hun kampioensvlag hesen. Het was geen mooie wedstrijd: de 76ers stonden bij rust 58-54 achter en maakten maar 11 van hun 40 driepunters. Met een 11-0 run aan het eind van het derde kwart trok de ploeg de wedstrijd toch naar zich toe. Maxey scoorde 28 punten, Brown had 19 punten, 8 rebounds en 6 assists. James kwam in zijn 24e NBA-seizoen tot 14 punten, 9 rebounds en 7 assists. Embiid pakte 11 rebounds, maar raakte maar 4 van zijn 15 schoten.</p>
<h3><strong>Vorig seizoen: Cleveland sterker, beide gestopt door de Knicks</strong></h3>
<p>Cleveland won in 2025/26 52 van de 82 wedstrijden en werd vierde in het Oosten. In de play-offs won de ploeg twee keer een zevende wedstrijd, tegen Toronto en Detroit, maar in de finale van het Oosten was New York met 4-0 te sterk. In februari ruilde Cleveland Darius Garland voor James Harden.</p>
<p>Philadelphia eindigde op 45-37 en moest via de play-in. Daar won de ploeg van Orlando (109-97). In de eerste ronde kwamen de 76ers tegen Boston terug van een 1-3 achterstand, maar in de tweede ronde volgde een 0-4 tegen de Knicks. Embiid speelde in de reguliere competitie maar 38 wedstrijden.</p>
{tabel(["2025/26", "Philadelphia 76ers", "Cleveland Cavaliers"], [
    ("Eindstand", "45-37 (nr. 7 Oost)", "52-30 (nr. 4 Oost)"),
    ("Thuis / uit", "23-18 / 22-19", "27-14 / 25-16"),
    ("Punten voor / tegen", "115,9 / 116,1", "119,5 / 115,4"),
    ("Aanvallende / verdedigende rating", "115,4 / 115,5", "119,2 / 115,1"),
    ("Onderling", "0-4", "4-0"),
    ("Play-offs", "Tweede ronde (0-4 tegen New York)", "Finale Oost (0-4 tegen New York)"),
])}
<p><em>Ratings per 100 balbezittingen. De onderlinge duels eindigden op 121-132, 107-133, 115-117 en 101-115, steeds in het voordeel van Cleveland.</em></p>"""

content2 = f"""<h3><strong>Zo zijn beide selecties veranderd</strong></h3>
<p><strong>Philadelphia 76ers: twee grote namen erbij</strong></p>
<p>Philadelphia haalde begin juli Jaylen Brown, MVP van de Finals in 2024, uit Boston. Daarvoor gingen Paul George, twee keuzes in de eerste ronde van de draft en twee in de tweede ronde naar de Celtics. Eind juli volgde de grootste verrassing: LeBron James tekende voor twee jaar en ongeveer 8 miljoen dollar, na acht seizoenen bij de Lakers. Ook schutters Anfernee Simons en Kentavious Caldwell-Pope en forward Dean Wade, vorig seizoen nog bij Cleveland, kwamen erbij. Quentin Grimes, Kelly Oubre en Andre Drummond vertrokken en Kyle Lowry stopte. Nick Nurse blijft de coach.</p>
<p><strong>Cleveland Cavaliers: de kern blijft</strong></p>
<p>Cleveland gaf Donovan Mitchell in juli een contractverlenging van vier jaar en 273 miljoen dollar, en James Harden tekende opnieuw voor drie jaar. De belangrijkste nieuwkomer is Peyton Watson, die via een ruil met vijf clubs uit Denver kwam. Hij scoorde vorig seizoen 14,6 punten per wedstrijd en raakte 41,1 procent van zijn driepunters. Ook Mario Hezonja (Real Madrid) en rookie Meleek Thomas kwamen erbij. Max Strus, Dennis Schröder, Dean Wade, Keon Ellis en Larry Nance jr. vertrokken. Kenny Atkinson begint aan zijn derde seizoen als coach.</p>
<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("Jarrett Allen", "Cleveland", "Twijfelachtig (rechterknie, peesklachten)"),
    ("Khalifa Diop", "Cleveland", "Speelt niet (linkerknie)"),
    ("Nae'Qwan Tomlin", "Cleveland", "Speelt niet (onderrug)"),
    ("Dean Wade", "Philadelphia", "Twijfelachtig (linkerenkel)"),
    ("Dominick Barlow", "Philadelphia", "Speelt niet (onderrug)"),
    ("Tacko Fall", "Philadelphia", "Speelt niet (bovenbeen)"),
    ("Ariel Hukporti", "Philadelphia", "Speelt dit seizoen niet meer (achillespees)"),
])}
<p><em>Stand van de officiële NBA-blessurelijst op donderdag 22 oktober, 09:00 Nederlandse tijd.</em></p>
<p><strong>Verwachte basisvijf 76ers:</strong> Tyrese Maxey, VJ Edgecombe, Jaylen Brown, LeBron James, Joel Embiid. Dezelfde vijf als in New York.</p>
<p><strong>Verwachte basisvijf Cavaliers:</strong> James Harden, Donovan Mitchell, Peyton Watson, Evan Mobley, Jarrett Allen. Kan Allen niet spelen, dan schuift Mobley door naar center en is Jaylon Tyson de logische vervanger. Achter Mobley zijn Thomas Bryant en two-way-speler Ernest Udeh jr. dan de enige fitte centers, want ook Diop ontbreekt.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "Bijzonderheid"], [
    ("Tyrese Maxey (PHI)", "28,3", "4,1", "6,6", "Topscorer in de opener met 28 punten"),
    ("Jaylen Brown (PHI)", "28,7", "6,9", "5,1", "Cijfers bij Boston, nu de tweede scorer"),
    ("LeBron James (PHI)", "20,9", "6,1", "7,2", "Cijfers bij de Lakers, wordt eind december 42"),
    ("Joel Embiid (PHI)", "26,9", "7,7", "3,9", "Speelde vorig seizoen maar 38 wedstrijden"),
    ("Donovan Mitchell (CLE)", "27,9", "4,5", "5,7", "Leider en topscorer van Cleveland"),
    ("James Harden (CLE)", "23,6", "4,8", "8,0", "43,5% driepunters na zijn komst naar Cleveland"),
    ("Evan Mobley (CLE)", "18,2", "9,0", "3,6", "Belangrijkste verdediger, mogelijk als center"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26.</em></p>
<h3><strong>Odds 76ers – Cavaliers bij Nederlandse bookmakers</strong></h3>
<p>De bookmakers zien Philadelphia als favoriet, maar niet met grote marge. Bij <a href="/bookmakers/toto">TOTO</a> ligt de handicap op 3,5 punten in het voordeel van de 76ers, en het verwachte puntentotaal op 235,5. In de Amerikaanse markt schommelt de handicap tussen 2,5 en 3,5 punten, met hetzelfde totaal.</p>
{tabel(["Markt", "Bookmaker", "76ers", "Cavaliers"], [
    ("Winnaar (incl. verlenging)", "TOTO", "1,67", "2,30"),
    ("Winnaar (incl. verlenging)", "<a href=\"/bookmakers/circus\">Circus</a>", "1,65", "2,31"),
    ("1X2 (reguliere speeltijd, gelijk 17,0)", "TOTO", "1,65", "2,35"),
    ("Handicap -3,5 / +3,5 (incl. verlenging)", "TOTO", "1,93", "1,87"),
    ("Handicap -4,5 / +4,5 (incl. verlenging)", "TOTO", "1,98", "1,71"),
])}
<p>Op het totaal van 235,5 punten (incl. verlenging) biedt TOTO Over 1,87 en Under 1,93. Wij lazen de odds op donderdag 22 oktober om 09:20 uur. Odds kunnen tot het begin nog veranderen, zeker als duidelijk wordt of Allen speelt; vergelijk ze vlak voor de start nog even.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op 76ers – Cavaliers</strong></a></p>"""

content3 = f"""<h3><strong>Onze voorspelling: 76ers winnen hun thuisdebuut</strong></h3>
<p>We kiezen voor Philadelphia, maar zonder grote zekerheid. De 76ers spelen thuis, hebben al één wedstrijd met de nieuwe ploeg achter de rug en hebben met Maxey, Brown, James en Embiid meer sterren dan Cleveland. Bovendien is het twijfelachtig of Allen speelt. Zonder hem mist Cleveland zijn vaste center en wordt het onder de ring lastiger om Embiid af te stoppen.</p>
<p>Toch is er genoeg reden voor voorzichtigheid. Cleveland won vorig seizoen alle vier de onderlinge duels, drie daarvan ruim, en had de betere aanval en verdediging. Met Harden en Mitchell heeft Cleveland twee spelers die in hun eentje een wedstrijd kunnen beslissen. Bij de 76ers moeten de nieuwe spelers nog aan elkaar wennen; dat was in New York goed te zien. Ook het puntentotaal schatten we lager in dan de bookmakers. Onze voorspelling: <strong>Philadelphia 76ers – Cleveland Cavaliers 115-108</strong>.</p>
<h3><strong>Wedtips voor 76ers – Cavaliers</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Inzet"], [
    ("Philadelphia 76ers wint (incl. verlenging)", "1,67", "TOTO", "Hoofdtip"),
    ("Minder dan 235,5 punten (incl. verlenging)", "1,93", "TOTO", "Tweede tip"),
    ("Philadelphia 76ers -4,5 punten (incl. verlenging)", "1,98", "TOTO", "Gedurfde tip"),
])}
<p><strong>1. 76ers wint (1,67).</strong> De logische uitkomst: thuis, met al een wedstrijd ervaring met elkaar, tegen een ploeg die zijn eerste duel speelt en misschien zonder zijn starting center moet. Houd er wel rekening mee dat de bookmakers Philadelphia maar zo'n 58 procent kans geven. Een zekerheidje is dit dus niet.</p>
<p><strong>2. Minder dan 235,5 punten (1,93).</strong> De opener van Philadelphia eindigde op 206 punten, met veel missers van afstand en een rustig tempo. Met James en Embiid speelt Philadelphia eerder met beleid dan op snelheid. Eerlijk is eerlijk: Cleveland scoorde vorig seizoen 119,5 punten per wedstrijd en twee van de vier onderlinge duels gingen ruim over deze lijn (253 en 240 punten). Speelt Allen niet, dan wordt Cleveland ook verdedigend kwetsbaarder. Dit is daarom een tip met een gemiddeld risico.</p>
<p><strong>3. 76ers -4,5 (1,98).</strong> Hiervoor moet Philadelphia met minstens vijf punten winnen. Dat past bij onze voorspelling, maar het risico is groter dan bij tip 1: wint Philadelphia nipt, met bijvoorbeeld twee of drie punten verschil, dan verlies je deze weddenschap. Speel dit alleen met een kleine inzet.</p>
<p>Wil je tip 1 en 2 combineren? Bij Circus kun je in één weddenschap spelen op 'Philadelphia wint én minder dan 235,5 punten' (incl. verlenging), tegen een quotering van 3,20.</p>
<h3><strong>76ers – Cavaliers live kijken in Nederland</strong></h3>
<p>De makkelijkste manier om de wedstrijd te zien: bij <a href="/bookmakers/bet365">Bet365</a> kijk je NBA-wedstrijden gratis live. Je hebt alleen een account met een kleine storting nodig, en die storting kun je daarna gewoon weer opnemen. In de Verenigde Staten zendt ESPN de wedstrijd uit; in Nederland heeft ESPN de NBA-rechten, maar niet elke wedstrijd staat op een van de Nederlandse ESPN-kanalen. Met <strong>NBA League Pass</strong>, de betaalde streamingdienst van de competitie, kun je ook alle wedstrijden volgen.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk 76ers – Cavaliers live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Lees ook onze voorspelling voor <a href="/nieuws/lakers-warriors-voorspelling-wedtips-nba-2026">Lakers – Warriors</a>, ons overzicht van de <a href="/nieuws/nba-voorspellingen-vannacht-22-oktober-2026">NBA-voorspellingen van 22 oktober</a> en het artikel <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">Welke Nederlanders spelen in de NBA</a>. Nieuw met wedden op basketbal? Lees eerst <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels in de NBA</a>. Alle basketbaltips vind je op onze pagina <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint 76ers – Cavaliers?</strong><br>Vrijdag 23 oktober 2026 om 01:00 Nederlandse tijd, in de nacht van donderdag op vrijdag. In Philadelphia is het dan donderdagavond 19:00.</p>
<p><strong>Waar wordt 76ers – Cavaliers gespeeld?</strong><br>In de Xfinity Mobile Arena in Philadelphia. De 76ers zijn de thuisploeg.</p>
<p><strong>Speelt LeBron James mee?</strong><br>Ja, hij staat niet op de blessurelijst. Het is zijn eerste thuiswedstrijd voor Philadelphia, en dat tegen de club waarvoor hij twee keer speelde en waarmee hij in 2016 kampioen werd.</p>
<p><strong>Speelt Jarrett Allen mee?</strong><br>Dat is nog onzeker. Allen staat als twijfelachtig op de blessurelijst met peesklachten in zijn rechterknie. Valt hij af, dan speelt Evan Mobley waarschijnlijk als center.</p>
<p><strong>Wie is favoriet: 76ers of Cavaliers?</strong><br>De 76ers, met een quotering van 1,67 bij TOTO. Cleveland staat op 2,30.</p>
<p><strong>Hoe ging het vorig seizoen tussen deze ploegen?</strong><br>Cleveland won alle vier de onderlinge duels. Drie wedstrijden eindigden in een ruime zege, één keer won Cleveland met twee punten verschil (117-115).</p>
<p><strong>Speelt er een Nederlander mee?</strong><br>Tristan Enaruna staat met een two-way-contract onder contract bij Cleveland. Of hij speelminuten krijgt, is nog niet bekend.</p>
<p><strong>Wat is onze voorspelling voor 76ers – Cavaliers?</strong><br>De 76ers winnen met 115-108. Onze hoofdtip is een zege van Philadelphia (1,67 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

KAART = {"home": "76ers", "away": "Cavaliers", "home_abbr": "phi", "away_abbr": "cle", "home_pos": "45-37 · nr. 7 Oost 2025/26", "away_pos": "52-30 · nr. 4 Oost 2025/26", "hs": 115, "as": 108, "datum": "Vr 23 okt", "tijd": "01:00", "odd_home": "1,67", "odd_away": "2,30"}
WEDTIPS = {"wedtip-1-2": "Philadelphia 76ers wint (incl. verlenging)", "quotering-wedtip-1": "1.67",
           "wedtip-2-2": "Minder dan 235,5 punten (incl. verlenging)", "quotering-wedtip-2": "1.93",
           "wedtip-3-2": "Philadelphia 76ers -4,5 punten (incl. verlenging)", "quotering-wedtip-3": "1.98",
           "bookmaker-wedtips": "669ab9f5aceb8b717cea24c3"}

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_BASKETBAL, "competitie": COMPETITIE_NBA,
          "datum-tijd-van-wedstrijd": "2026-10-22T23:00:00.000Z",
          "publicatiedatum": datetime.now(timezone.utc).isoformat(), **WEDTIPS}
    # Alleen dry run: dit script publiceert niets.
    import re
    tekst = re.sub(r"<[^>]+>", " ", content + content2 + content3)
    print(len(TITEL), "tekens titel |", len(SAMENVATTING), "tekens samenvatting |", len(tekst.split()), "woorden")
