# -*- coding: utf-8 -*-
"""Los artikel: Spurs – Rockets voorspelling, NBA 24 oktober 2026 (03:30 NL), Moody Center in Austin (I-35 Series).
Feiten nagelopen op 23-10-2026 (ESPN-API: scoreboard, boxscores 401909090 en 401909840, preview 401909096, standen en
schema's 2025/26, spelersgemiddelden; NBA-blessurelijst 22-10; Spurs- en Rockets-schema 2026/27; offseason-overzichten).
- Spurs – Thunder 104-116 (20-10), Rockets – Mavericks 128-110 (21-10).
- Onderling 2025/26: 121-110 SAS (8 nov, NBA Cup), 111-106 HOU (21 jan), 99-111 SAS (29 jan), 145-120 SAS (9 mrt).
- Odds: TOTO uit specials/nba_feiten_2026_10_24.md (±12:00 NL op 23-10). 'Winnaar' = incl. verlenging.
  ../superodd-agent/.venv/bin/python specials/spurs_rockets_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "Spurs – Rockets voorspelling: wedtips en odds voor de Texas-derby in Austin (24 oktober, 03:30)"
SLUG = "spurs-rockets-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("Wembanyama tegen Şengün: de Spurs ontvangen Houston in Austin. Voorspelling, wedtips, TOTO-odds, "
                "blessures en opstellingen.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet-experts.nl/go/bet365"
DATUM = "2026-10-24T01:30:00.000Z"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>In de nacht van vrijdag op zaterdag om 03:30 Nederlandse tijd staat de eerste Texas-derby van het NBA-seizoen op het programma: San Antonio Spurs – Houston Rockets. De Spurs zijn de thuisploeg, maar spelen niet in San Antonio: de wedstrijd is in het Moody Center in Austin. San Antonio verloor de opener van Oklahoma City, Houston won overtuigend van Dallas. Onze voorspelling: de Spurs winnen met 114-108. Hoofdtip: een zege van San Antonio, met minder dan 227,5 punten als tweede tip.</strong></p>
<p>Het duel draait om Victor Wembanyama tegen Alperen Şengün, twee van de beste big men van het Westen, in de eerste van vier onderlinge ontmoetingen dit seizoen.</p>
<h3><strong>Spurs – Rockets: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "San Antonio Spurs – Houston Rockets"),
    ("Datum", "Zaterdag 24 oktober 2026 (nacht van vrijdag op zaterdag)"),
    ("Aanvang", "03:30 Nederlandse tijd (vrijdag 20:30 in Texas)"),
    ("Arena", "Moody Center, Austin (Texas)"),
    ("Thuisploeg", "San Antonio Spurs"),
    ("Competitie", "NBA, reguliere competitie 2026/27"),
    ("Stand 2026/27", "Spurs 0-1, Rockets 1-0"),
    ("Onderlinge duels 2025/26", "3-1 voor de Spurs"),
])}
<h3><strong>Waarom spelen de Spurs in Austin?</strong></h3>
<p>Sinds 2023 speelt San Antonio elk seizoen thuiswedstrijden in Austin, onder de naam I-35 Series, naar de snelweg tussen beide steden. Austin ligt zo'n 130 kilometer ten noordoosten van San Antonio en hoort voor de NBA bij het marktgebied van de Spurs; de club wil daar zijn achterban vergroten. Dit seizoen speelt San Antonio drie keer in het Moody Center, de arena van de universiteit van Texas: na Houston volgen Memphis (26 februari) en Denver (28 februari). Officieel is het een gewone thuiswedstrijd, maar zonder het eigen Frost Bank Center is het thuisvoordeel wat kleiner.</p>
<h3><strong>Speelronde 1: Wembanyama koud, Houston op stoom</strong></h3>
<p>San Antonio begon het seizoen dinsdag met een 104-116 thuisnederlaag tegen Oklahoma City. Bij rust stond het al 44-65. Wembanyama raakte maar 1 van zijn 13 schoten (12 punten), al pakte hij wel 13 rebounds en 6 blocks. Stephon Castle was met 24 punten topscorer, Dylan Harper maakte er 18 en De'Aaron Fox had 14 punten en 7 assists. San Antonio raakte maar 10 van de 37 driepunters.</p>
<p>Houston opende een dag later met een ruime 128-110 zege op Dallas. Durant en Jabari Smith Jr. scoorden allebei 30 punten, Şengün had 23 punten, 10 rebounds en 5 assists. VanVleet, die het hele vorige seizoen miste met een gescheurde kruisband, kwam bij zijn rentree tot 6 punten en 11 assists. Houston gaf 32 assists en stond op een gegeven moment 37 punten voor.</p>
<h3><strong>Vorig seizoen: twee play-offploegen uit het Westen</strong></h3>
<p>San Antonio won in 2025/26 62 van de 82 wedstrijden en werd tweede in het Westen. Na Portland, Minnesota en Oklahoma City was in de NBA Finals New York met 4-1 te sterk. Houston eindigde met 52-30 als vijfde en verloor in de eerste ronde met 2-4 van de Lakers. De Rockets speelden dat hele seizoen zonder VanVleet.</p>
{tabel(["2025/26", "San Antonio Spurs", "Houston Rockets"], [
    ("Eindstand", "62-20 (nr. 2 West)", "52-30 (nr. 5 West)"),
    ("Thuis / uit", "32-8 thuis", "30-11 / 22-19"),
    ("Punten voor / tegen", "119,8 / 111,5", "115,2 / 110,0"),
    ("Onderling", "3-1", "1-3"),
    ("Play-offs", "Finale verloren van New York (1-4)", "Eerste ronde verloren van de Lakers (2-4)"),
])}
<p>De onderlinge duels eindigden op 121-110 (San Antonio, NBA Cup), 111-106 (Houston), 99-111 en 145-120 (beide San Antonio). Gemiddeld vielen er 230,8 punten; twee van de vier wedstrijden gingen over de 227,5 punten.</p>"""

content2 = f"""<h3><strong>Zo zijn beide selecties veranderd</strong></h3>
<p><strong>San Antonio Spurs: vooral continuïteit</strong></p>
<p>San Antonio hield de kern van de finaleploeg bij elkaar. De belangrijkste nieuwkomer is Tobias Harris, die in juli tekende maar met een kuitblessure nog niet heeft gespeeld. Verder kwamen rookie-center Tarris Reed Jr. en Jayden Quaintance (herstelt van een knieoperatie) erbij. Coach Mitch Johnson kiest voor drie guards: Fox, Castle en Harper.</p>
<p><strong>Houston Rockets: VanVleet terug, ervaring erbij</strong></p>
<p>De grootste 'versterking' is VanVleet zelf, terug na een jaar blessureleed. Verder kwamen Marcus Smart (vorig seizoen Lakers) en schutter Bogdan Bogdanović. Tari Eason tekende voor vijf jaar bij en Amen Thompson kreeg in september een verlenging van vijf jaar en 208 miljoen dollar. Dorian Finney-Smith, Josh Okogie, Jeff Green en Aaron Holiday vertrokken. Ime Udoka blijft coach.</p>
<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("De'Aaron Fox", "San Antonio", "Twijfelachtig (verstuikte rechterpols)"),
    ("Keldon Johnson", "San Antonio", "Twijfelachtig (snijwond in de mond, gehecht)"),
    ("Tobias Harris", "San Antonio", "Speelt niet (kuit)"),
    ("Jayden Quaintance", "San Antonio", "Speelt niet (herstel na knieoperatie)"),
    ("Steven Adams", "Houston", "Twijfelachtig (kuit)"),
    ("Reed Sheppard", "Houston", "Twijfelachtig (kneuzing linkerknie)"),
])}
<p><em>Stand van de blessurelijst op vrijdag 23 oktober, 12:00 Nederlandse tijd. Over Fox valt de beslissing waarschijnlijk pas vlak voor de wedstrijd.</em></p>
<p><strong>Verwachte basisvijf San Antonio:</strong> De'Aaron Fox, Stephon Castle, Dylan Harper, Devin Vassell, Victor Wembanyama. Speelt Fox niet, dan nemen Castle en Harper de opbouw over en is Julian Champagnie de logische vervanger in de basis.</p>
<p><strong>Verwachte basisvijf Houston:</strong> Fred VanVleet, Amen Thompson, Kevin Durant, Jabari Smith Jr., Alperen Şengün, net als tegen Dallas. Clint Capela is de reservecenter.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "Bijzonderheid"], [
    ("Victor Wembanyama (SAS)", "25,0", "11,5", "3,1", "3,1 blocks; 1 op 13 in de opener"),
    ("Stephon Castle (SAS)", "16,7", "5,3", "7,4", "Topscorer in de opener (24)"),
    ("De'Aaron Fox (SAS)", "18,6", "3,8", "6,2", "Twijfelachtig met zijn pols"),
    ("Kevin Durant (HOU)", "26,0", "5,5", "4,8", "52% uit het veld, 41% driepunters"),
    ("Alperen Şengün (HOU)", "20,4", "8,9", "6,2", "Spelmaker vanuit de center-positie"),
    ("Amen Thompson (HOU)", "18,3", "7,8", "5,3", "Kreeg in september een verlenging van vijf jaar"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26.</em></p>
<p>Het duel onder de ring is de sleutel. In de vier onderlinge wedstrijden van vorig seizoen kwam Wembanyama gemiddeld tot 23,3 punten, 10,5 rebounds en 2,8 blocks; Şengün noteerde 19,8 punten, 9,3 rebounds en 6,8 assists. Wie van de twee zijn stempel drukt, bepaalt in grote mate de uitslag.</p>
<h3><strong>Odds Spurs – Rockets bij TOTO</strong></h3>
<p>De bookmakers zien San Antonio als duidelijke favoriet, ondanks de twijfels rond Fox. Bij <a href="/bookmakers/toto">TOTO</a> ligt de handicap op 5,5 punten en het verwachte puntentotaal op 227,5.</p>
{tabel(["Markt (TOTO)", "Spurs", "Rockets"], [
    ("Winnaar (incl. verlenging)", "1,50", "2,70"),
    ("1X2 (reguliere speeltijd, gelijk 19,00)", "1,47", "2,80"),
    ("Handicap -6,5 / +6,5 (incl. verlenging)", "2,00", "1,69"),
    ("Handicap -5,5 / +5,5 (incl. verlenging)", "1,93", "1,87"),
    ("Handicap -4,5 / +4,5 (incl. verlenging)", "1,73", "1,95"),
])}
<p>Totaal 227,5 punten (incl. verlenging): Over 1,87, Under 1,93. Bij 228,5 punten: Over 1,95, Under 1,87. Gelezen op vrijdag 23 oktober rond 12:00 uur; odds kunnen nog veranderen, zeker rond het nieuws over Fox.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op Spurs – Rockets</strong></a></p>"""

content3 = f"""<h3><strong>Onze voorspelling: Spurs winnen, maar niet ruim</strong></h3>
<p>We kiezen voor San Antonio. Een avond als tegen Oklahoma City, met 1 op 13 voor Wembanyama en 27 procent uit de driepunters, zien we niet snel terugkomen. De Spurs wonnen vorig seizoen drie van de vier duels met Houston en waren over het hele seizoen een stuk sterker.</p>
<p>Toch verwachten we geen ruime zege. Houston oogde tegen Dallas als een geoliede ploeg, heeft met VanVleet weer een echte spelverdeler en kreeg vorig seizoen alleen minder punten tegen dan Boston, Oklahoma City en Detroit. Het thuisvoordeel in Austin is kleiner, en zonder Fox mist de Spurs-aanval creativiteit. Het puntentotaal schatten we iets lager in dan de bookmakers. Onze voorspelling: <strong>San Antonio Spurs – Houston Rockets 114-108</strong>.</p>
<h3><strong>Wedtips voor Spurs – Rockets</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Inzet"], [
    ("San Antonio Spurs wint (incl. verlenging)", "1,50", "TOTO", "Hoofdtip"),
    ("Minder dan 227,5 punten (incl. verlenging)", "1,93", "TOTO", "Tweede tip"),
    ("Houston Rockets +6,5 punten (incl. verlenging)", "1,69", "TOTO", "Alternatief met kleine inzet"),
])}
<p><strong>1. San Antonio wint (1,50).</strong> De sterkere ploeg, een onderlinge reeks van 3-1 en een Wembanyama met iets recht te zetten. Wij schatten de kans op ongeveer 67 procent, vrijwel gelijk aan de quotering: weinig extra waarde, wel de betrouwbaarste uitkomst. Risico: Fox valt af en Houston zet de vorm van de opener door.</p>
<p><strong>2. Minder dan 227,5 punten (1,93).</strong> Twee van de beste verdedigingen van vorig seizoen, een Spurs-aanval die nog zoekende is en mogelijk geen Fox. Wij schatten de kans op zo'n 55 procent. Eerlijk is eerlijk: Houston scoorde tegen Dallas 128 punten en het laatste onderlinge duel eindigde op 265 punten. Gemiddeld risico dus.</p>
<p><strong>3. Houston +6,5 (1,69).</strong> Houston mag met maximaal zes punten verliezen. Dat past bij onze verwachting van een Spurs-zege zonder grote marge, zeker als Fox ontbreekt. Wij schatten de kans op ongeveer 60 procent. Het risico: Wembanyama domineert en de Spurs winnen alsnog ruim, zoals in maart (145-120). Speel dit alleen met een kleine inzet.</p>
<p>Let op bij TOTO: de 1X2-markt gaat alleen over de reguliere speeltijd, 'Winnaar' telt de verlenging wel mee. Meer uitleg vind je in onze gidsen over <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap wedden</a> en de <a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">money line</a>.</p>
<h3><strong>Beide ploegen spelen zaterdag alweer</strong></h3>
<p>Voor allebei is dit het eerste duel van een back-to-back: zaterdagavond Amerikaanse tijd speelt San Antonio in Dallas (zondag 25 oktober, 02:00 Nederlandse tijd) en Houston in Atlanta (02:30). Twijfelgevallen als Fox, Keldon Johnson, Adams en Sheppard worden dan vaak extra voorzichtig behandeld.</p>
<h3><strong>Spurs – Rockets live kijken in Nederland</strong></h3>
<p>Bij <a href="/bookmakers/bet365">Bet365</a> kun je NBA-wedstrijden live volgen via de livestream; je hebt daarvoor een account met een storting nodig. ESPN zendt in Nederland een deel van de NBA-wedstrijden uit; of deze erbij zit, zie je in de programmagids. Met <strong>NBA League Pass</strong>, de betaalde dienst van de competitie, kun je alle wedstrijden volgen. Meer opties op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk Spurs – Rockets live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Lees ook onze voorspellingen voor <a href="/nieuws/spurs-thunder-voorspelling-wedtips-nba-opening-2026">Spurs – Thunder</a>, <a href="/nieuws/pistons-celtics-voorspelling-wedtips-nba-opening-2026">Pistons – Celtics</a>, <a href="/nieuws/lakers-warriors-voorspelling-wedtips-nba-2026">Lakers – Warriors</a>, <a href="/nieuws/76ers-cavaliers-voorspelling-wedtips-nba-2026">76ers – Cavaliers</a>, <a href="/nieuws/thunder-nuggets-voorspelling-wedtips-nba-2026">Thunder – Nuggets</a> en de <a href="/nieuws/nba-voorspellingen-vannacht-22-oktober-2026">NBA-voorspellingen van 22 oktober</a>, en <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">welke Nederlanders er in de NBA spelen</a>. Nieuw met basketbal? Lees <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels in de NBA</a>. Alle tips staan op <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Spurs – Rockets?</strong><br>Zaterdag 24 oktober 2026 om 03:30 Nederlandse tijd, in de nacht van vrijdag op zaterdag. In Texas is het dan vrijdagavond 20:30.</p>
<p><strong>Waar wordt Spurs – Rockets gespeeld?</strong><br>In het Moody Center in Austin. De Spurs zijn de thuisploeg; het is hun eerste van drie thuisduels in Austin dit seizoen.</p>
<p><strong>Speelt De'Aaron Fox mee?</strong><br>Dat is nog onzeker. Fox staat als twijfelachtig op de blessurelijst met een verstuikte rechterpols. Valt hij af, dan nemen Castle en Harper de opbouw over.</p>
<p><strong>Wie is favoriet: Spurs of Rockets?</strong><br>De Spurs, met een quotering van 1,50 bij TOTO. Houston staat op 2,70.</p>
<p><strong>Wat is onze voorspelling voor Spurs – Rockets?</strong><br>De Spurs winnen met 114-108. Onze hoofdtip is een zege van San Antonio (1,50 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

KAART = {"home": "Spurs", "away": "Rockets", "home_abbr": "sa", "away_abbr": "hou", "home_pos": "62-20 · nr. 2 West 2025/26", "away_pos": "52-30 · nr. 5 West 2025/26", "hs": 114, "as": 108, "datum": "Za 24 okt", "tijd": "03:30", "odd_home": "1,50", "odd_away": "2,70"}
WEDTIPS = {"wedtip-1-2": "San Antonio Spurs wint (incl. verlenging)", "quotering-wedtip-1": "1.50",
           "wedtip-2-2": "Minder dan 227,5 punten (incl. verlenging)", "quotering-wedtip-2": "1.93",
           "wedtip-3-2": "Houston Rockets +6,5 punten (incl. verlenging)", "quotering-wedtip-3": "1.69",
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
