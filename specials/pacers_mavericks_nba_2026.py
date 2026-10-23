# -*- coding: utf-8 -*-
"""Los artikel: Pacers – Mavericks voorspelling, NBA 24 oktober 2026 (01:00 NL). Feiten nagelopen op 23-10-2026
(ESPN-API: boxscores 21-10, stand 2025/26, onderlinge duels, selecties, blessurelijst 22-10; Wikipedia seizoenspagina's
2026/27; NBA.com trade tracker; AP-preview; Hoops Rumors/RotoWire blessurenieuws 22-10).
- Pelicans-Pacers 120-123 en Rockets-Mavericks 128-110 op 21-10 (US-tijd). Dallas speelt 24-10 (US) thuis tegen de Spurs.
- Odds: TOTO uit het feitenblad (sport.toto.nl, ±12:00 NL op 23-10). 'Winnaar' = incl. verlenging.
  ../superodd-agent/.venv/bin/python specials/pacers_mavericks_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "Pacers – Mavericks voorspelling: wedtips en odds voor Haliburton tegen Flagg (24 oktober, 01:00)"
SLUG = "pacers-mavericks-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("Haliburton speelt zijn eerste officiële thuisduel na zijn blessure, tegen Flagg en Dallas. Voorspelling, "
                "wedtips, odds en opstellingen.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet-experts.nl/go/bet365"
DATUM = "2026-10-23T23:00:00.000Z"

# Deelkaart (maatwerk-kaart in de nieuwe stijl)
OG_KOP = "Pacers – Mavericks <span>voorspelling</span>"
OG_EYEBROW = "NBA · zaterdag 24 oktober, 01:00"
OG_CHIPS = ["Haliburton vs Flagg", "3 wedtips"]
OG_MOTIEF = "tabel"
OG_DATA = ["Aftrap · 01:00", "Arena · Gainbridge Fieldhouse", "Onderling 25/26 · 2-0 Mavs", "Favoriet · Pacers"]

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>In de nacht van vrijdag op zaterdag om 01:00 Nederlandse tijd spelen de Indiana Pacers hun eerste thuiswedstrijd van het seizoen, tegen de Dallas Mavericks. Tyrese Haliburton is na een jaar blessureleed terug, Dallas komt met Rookie of the Year Cooper Flagg. Indiana won zijn opener in New Orleans, Dallas ging hard onderuit in Houston. Onze voorspelling: de Pacers winnen met 120-111. Hoofdtip: Indiana wint, met de Pacers -4,5 als tweede tip.</strong></p>
<p>Vorig seizoen eindigden beide ploegen ver onder de streep: Indiana op 19-63, Dallas op 26-56. Hieronder lees je wat er veranderd is, wie er speelt, wat de bookmakers verwachten en welke weddenschappen wij interessant vinden.</p>
<h3><strong>Pacers – Mavericks: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "Indiana Pacers – Dallas Mavericks"),
    ("Datum", "Zaterdag 24 oktober 2026 (nacht van vrijdag op zaterdag)"),
    ("Aanvang", "01:00 Nederlandse tijd (vrijdag 19:00 in Indianapolis)"),
    ("Arena", "Gainbridge Fieldhouse, Indianapolis"),
    ("Competitie", "NBA, reguliere competitie 2026/27"),
    ("Stand 2026/27", "Pacers 1-0, Mavericks 0-1"),
    ("Onderlinge duels 2025/26", "2-0 voor de Mavericks"),
])}
<h3><strong>Speelronde 1: Indiana komt terug, Dallas kansloos</strong></h3>
<p>Indiana won woensdagnacht met 120-123 bij de New Orleans Pelicans. Bij rust stonden de Pacers nog met 66-56 achter, maar met een laatste kwart van 37-28 trokken ze de wedstrijd naar zich toe. Indiana scoorde 64 punten in de zone en 27 uit snelle aanvallen. Pascal Siakam was met 30 punten topscorer, Haliburton had 23 punten en 12 assists in zijn eerste officiële wedstrijd in bijna zestien maanden.</p>
<p>Dallas begon een stuk slechter. In Houston stond de ploeg bij rust met 70-38 achter; uiteindelijk werd het 128-110. De Mavericks verloren 21 keer de bal, waar de Rockets 32 punten uit haalden. Cooper Flagg maakte 32 punten, maar kon de nederlaag niet voorkomen.</p>
<h3><strong>Vorig seizoen: twee ploegen in de onderste regionen</strong></h3>
<p>Haliburton scheurde in de zevende wedstrijd van de Finale van 2025 zijn achillespees en miste het hele seizoen 2025/26. Zonder hem wonnen de Pacers maar 19 wedstrijden, thuis maar 11. Alleen Washington deed het in het Oosten slechter. In februari haalde Indiana center Ivica Zubac van de LA Clippers, onder meer in ruil voor Bennedict Mathurin, Isaiah Jackson en draftkeuzes.</p>
<p>Dallas speelde het hele seizoen zonder Kyrie Irving, die herstelde van een gescheurde kruisband. In februari ging Anthony Davis naar Washington en de Mavericks eindigden als twaalfde in het Westen. Flagg werd wel Rookie of the Year.</p>
{tabel(["2025/26", "Indiana Pacers", "Dallas Mavericks"], [
    ("Eindstand", "19-63 (nr. 14 Oost)", "26-56 (nr. 12 West)"),
    ("Punten voor / tegen", "112,4 / 120,4", "114,1 / 119,6"),
    ("Onderling", "0-2", "2-0"),
    ("Play-offs", "Niet gehaald", "Niet gehaald"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie. De onderlinge duels eindigden op 107-105 in Dallas (oktober 2025) en 130-134 in Indianapolis (februari 2026). Beide keren speelde Indiana zonder Haliburton.</em></p>"""

content2 = f"""<h3><strong>Zo zijn beide selecties veranderd</strong></h3>
<p><strong>Indiana Pacers: Haliburton is de grootste aanwinst</strong></p>
<p>De grootste versterking is een speler die er al was: Haliburton. Daarnaast kwamen Kelly Oubre jr. (Philadelphia) en Larry Nance jr. (Cleveland) erbij, en in ruil voor Kam Jones haalde Indiana uit Chicago de rechten op Braden Smith, de nummer 38 van de draft. Zubac speelt zijn eerste volledige seizoen in Indianapolis. Rick Carlisle blijft de coach.</p>
<p><strong>Dallas Mavericks: nieuwe coach, nieuwe ploeg</strong></p>
<p>Jason Kidd vertrok als coach; zijn opvolger is Dusty May. Dallas koos zijn speler Morez Johnson jr. als nummer 9 in de draft. Via ruilen kwamen Santi Aldama (Memphis), Marcus Sasser (Detroit) en Zaccharie Risacher (Atlanta) erbij. Khris Middleton vertrok naar Washington, Klay Thompson naar Miami.</p>
<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("T.J. McConnell", "Indiana", "Speelt niet (hamstring)"),
    ("Aaron Nesmith", "Indiana", "Twijfelachtig (linkerhamstring)"),
    ("Ben Sheppard", "Indiana", "Twijfelachtig (linkerknie)"),
    ("Johnny Furphy", "Indiana", "Speelt niet (kruisband, langdurig)"),
    ("Dereck Lively II", "Dallas", "Speelt niet (voetoperatie)"),
    ("Santi Aldama", "Dallas", "Speelt niet (knieoperatie)"),
    ("Caleb Martin", "Dallas", "Speelt niet (duim)"),
    ("Tarik Biberović", "Dallas", "Speelt niet (hiel)"),
    ("Jett Howard", "Dallas", "Onwaarschijnlijk (kuit)"),
])}
<p><em>Stand van de blessurelijst op donderdag 22 oktober, 's avonds Nederlandse tijd.</em></p>
<p><strong>Verwachte basisvijf Pacers:</strong> Tyrese Haliburton, Andrew Nembhard, Kelly Oubre jr., Pascal Siakam, Ivica Zubac. Dat is dezelfde vijf als in New Orleans. Is Nesmith fit, dan kan hij de plek van Oubre innemen. Obi Toppin is de belangrijkste invaller.</p>
<p><strong>Verwachte basisvijf Mavericks:</strong> Kyrie Irving, Max Christie, Cooper Flagg, P.J. Washington, Daniel Gafford. Ook dit is de vijf van de opener. Zonder Lively en Aldama is Dallas dun bezet onder de ring: achter Gafford zijn Johnson en Moussa Cissé de opties.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Ptn", "Reb", "Ast", "Opener 2026/27"], [
    ("Pascal Siakam (IND)", "24,0", "6,6", "3,8", "30 punten, 8 rebounds"),
    ("Tyrese Haliburton (IND)", "18,6*", "3,5*", "9,2*", "23 punten, 12 assists"),
    ("Andrew Nembhard (IND)", "16,9", "2,8", "7,7", "18 punten, 9 assists"),
    ("Ivica Zubac (IND)", "14,1", "10,6", "2,2", "16 punten, 15 rebounds"),
    ("Cooper Flagg (DAL)", "21,0", "6,7", "4,5", "32 punten, 3 steals"),
    ("Kyrie Irving (DAL)", "24,7*", "4,8*", "4,6*", "15 punten in 24 minuten"),
    ("Naji Marshall (DAL)", "15,2", "4,7", "3,3", "16 punten, 6 assists"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26. * Haliburton en Irving speelden in 2025/26 niet; bij hen staan de cijfers van 2024/25. Zubacs cijfers zijn grotendeels bij de Clippers gemaakt.</em></p>
<p><strong>Cooper Flagg</strong> is pas 19, maar nu al het gezicht van Dallas. In april maakte hij als rookie 51 punten tegen Orlando, in Houston raakte hij 10 van de 17 schoten en 11 van de 13 vrije worpen. Zijn zwakke punt is het schot van afstand: vorig seizoen 29,5 procent van zijn driepunters.</p>
<p><strong>Tyrese Haliburton</strong> is de motor van Indiana. Met hem haalden de Pacers in 2025 de Finale, zonder hem zakten ze naar de onderkant van het Oosten. Zijn rentree was meteen goed: 8 van de 15 schoten raak, 12 assists en een hoog tempo, waar ook Siakam van profiteerde.</p>
<h3><strong>Odds Pacers – Mavericks bij TOTO</strong></h3>
<p>De bookmakers zien Indiana als duidelijke favoriet. Bij <a href="/bookmakers/toto">TOTO</a> ligt de handicap op 5,5 punten in het voordeel van de Pacers en het verwachte puntentotaal op 237,5. Een quotering van 1,45 komt neer op een kans van ongeveer twee op drie.</p>
{tabel(["Markt", "Pacers", "Mavericks"], [
    ("Winnaar (incl. verlenging)", "1,45", "2,80"),
    ("1X2 (reguliere speeltijd, gelijk 19,00)", "1,44", "2,90"),
    ("Handicap -4,5 / +4,5 (incl. verlenging)", "1,67", "2,05"),
    ("Handicap -5,5 / +5,5 (incl. verlenging)", "1,77", "1,91"),
    ("Handicap -6,5 / +6,5 (incl. verlenging)", "1,91", "1,77"),
])}
<p>Op het totaal van 237,5 punten (incl. verlenging) biedt TOTO Over 1,87 en Under 1,93. Wij lazen de odds op vrijdag 23 oktober rond 12:00 uur. Odds kunnen tot het begin nog veranderen, zeker als duidelijk wordt of Nesmith speelt; vergelijk ze vlak voor de start nog even.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op Pacers – Mavericks</strong></a></p>"""

content3 = f"""<h3><strong>Onze voorspelling: Pacers winnen hun thuisopener</strong></h3>
<p>We kiezen voor Indiana. De Pacers spelen thuis, Haliburton, Nembhard, Siakam en Zubac vormen een sterke kern, en in New Orleans kwam de ploeg terug na een slechte helft. Dallas mist bovendien twee lange spelers: zonder Lively en Aldama staat Gafford er vrijwel alleen voor tegen Zubac, die in de opener 15 rebounds pakte.</p>
<p>Toch is Dallas niet kansloos. Flagg kan in zijn eentje een wedstrijd kantelen, Irving is terug en de Mavericks wonnen vorig seizoen beide onderlinge duels. Ook de planning speelt mee: Dallas speelt zaterdagavond Amerikaanse tijd alweer thuis tegen de San Antonio Spurs (zondag 02:00 Nederlandse tijd). Dit is dus het eerste duel van een back-to-back. Vermoeidheid speelt vannacht nog geen rol, maar het is afwachten hoeveel minuten de 34-jarige Irving in twee opeenvolgende dagen krijgt. Onze voorspelling: <strong>Indiana Pacers – Dallas Mavericks 120-111</strong>.</p>
<h3><strong>Wedtips voor Pacers – Mavericks</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Inzet"], [
    ("Indiana Pacers wint (incl. verlenging)", "1,45", "TOTO", "Hoofdtip"),
    ("Indiana Pacers -4,5 punten (incl. verlenging)", "1,67", "TOTO", "Tweede tip"),
    ("Minder dan 237,5 punten (incl. verlenging)", "1,93", "TOTO", "Gedurfde tip"),
])}
<p><strong>1. Pacers wint (1,45).</strong> De logische uitkomst. Wij schatten de kans op een zege van Indiana op ongeveer 70 procent, iets hoger dan de bookmakers. Het risico: Dallas heeft met Flagg en Irving twee spelers die een wedstrijd kunnen beslissen, en na de opener weten we nog weinig over de nieuwe ploeg van Dusty May.</p>
<p><strong>2. Pacers -4,5 (1,67).</strong> Indiana moet met minstens vijf punten winnen. Dat past bij onze voorspelling; wij schatten de kans op ongeveer 60 procent. Het risico is groter dan bij tip 1: de onderlinge duels van vorig seizoen werden met twee en vier punten verschil beslist.</p>
<p><strong>3. Minder dan 237,5 punten (1,93).</strong> Vorig seizoen kwamen de wedstrijden van beide ploegen gemiddeld uit op zo'n 233 punten, en Dallas scoorde in Houston maar 110. Eerlijk is eerlijk: beide openers gingen over deze lijn (243 en 238 punten) en met Haliburton ligt het tempo hoger. Wij schatten de kans net boven de 50 procent. Speel dit alleen met een kleine inzet.</p>
<h3><strong>Pacers – Mavericks live kijken in Nederland</strong></h3>
<p>Bij <a href="/bookmakers/bet365">Bet365</a> kun je NBA-wedstrijden live streamen. Je hebt alleen een account met een kleine storting nodig, en die storting kun je daarna gewoon weer opnemen. ESPN zendt in Nederland een deel van de NBA-wedstrijden uit, maar niet elke wedstrijd; check vooraf het programma. Met <strong>NBA League Pass</strong>, de betaalde streamingdienst van de competitie, kun je alle wedstrijden volgen.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk Pacers – Mavericks live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Lees ook onze voorspellingen voor <a href="/nieuws/lakers-warriors-voorspelling-wedtips-nba-2026">Lakers – Warriors</a>, <a href="/nieuws/76ers-cavaliers-voorspelling-wedtips-nba-2026">76ers – Cavaliers</a> en <a href="/nieuws/thunder-nuggets-voorspelling-wedtips-nba-2026">Thunder – Nuggets</a>, en ons overzicht van de <a href="/nieuws/nba-voorspellingen-vannacht-22-oktober-2026">NBA-voorspellingen van 22 oktober</a>. Nieuw met wedden op basketbal? Lees eerst <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels in de NBA</a>, of ontdek <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">hoe handicap wedden werkt</a>. Alle basketbaltips vind je op onze pagina <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Pacers – Mavericks?</strong><br>Zaterdag 24 oktober 2026 om 01:00 Nederlandse tijd, in de nacht van vrijdag op zaterdag. In Indianapolis is het dan vrijdagavond 19:00.</p>
<p><strong>Speelt Tyrese Haliburton mee?</strong><br>Ja, hij staat niet op de blessurelijst. In de opener in New Orleans had hij 23 punten en 12 assists, in zijn eerste officiële wedstrijd sinds zijn achillespeesblessure in de Finale van 2025.</p>
<p><strong>Speelt Kyrie Irving mee?</strong><br>Ja, ook Irving staat niet op de blessurelijst. Hij maakte in Houston 15 punten in 24 minuten, na een heel seizoen afwezigheid door een kruisbandblessure.</p>
<p><strong>Wie is favoriet: Pacers of Mavericks?</strong><br>De Pacers, met een quotering van 1,45 bij TOTO. Dallas staat op 2,80.</p>
<p><strong>Wat is onze voorspelling voor Pacers – Mavericks?</strong><br>De Pacers winnen met 120-111. Onze hoofdtip is een zege van Indiana (1,45 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

KAART = {"home": "Pacers", "away": "Mavericks", "home_abbr": "ind", "away_abbr": "dal", "home_pos": "19-63 · nr. 14 Oost 2025/26", "away_pos": "26-56 · nr. 12 West 2025/26", "hs": 120, "as": 111, "datum": "Za 24 okt", "tijd": "01:00", "odd_home": "1,45", "odd_away": "2,80"}
WEDTIPS = {"wedtip-1-2": "Indiana Pacers wint (incl. verlenging)", "quotering-wedtip-1": "1.45",
           "wedtip-2-2": "Indiana Pacers -4,5 punten (incl. verlenging)", "quotering-wedtip-2": "1.67",
           "wedtip-3-2": "Minder dan 237,5 punten (incl. verlenging)", "quotering-wedtip-3": "1.93",
           "bookmaker-wedtips": "669ab9f5aceb8b717cea24c3"}

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_BASKETBAL, "competitie": COMPETITIE_NBA,
          "datum-tijd-van-wedstrijd": DATUM,
          "publicatiedatum": datetime.now(timezone.utc).isoformat(), **WEDTIPS}
    # Alleen dry run: dit script publiceert niets.
    import re
    tekst = re.sub(r"<[^>]+>", " ", content + content2 + content3)
    print(len(TITEL), "tekens titel |", len(SAMENVATTING), "tekens samenvatting |", len(tekst.split()), "woorden")
