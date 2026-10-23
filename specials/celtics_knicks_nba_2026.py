# -*- coding: utf-8 -*-
"""Los artikel: Celtics – Knicks voorspelling, NBA 24 oktober 2026 (01:00 NL). Feiten nagelopen op 23-10-2026
(ESPN-scoreboard/summary/schedule/standings/roster-API, officiele NBA-blessurelijst 23-10 06:00 ET, AP-verslagen
van speelronde 1, Fantasy Alarm/SI/ABC7 over de zomertransfers).
- Pistons-Celtics 121-113 op 20-10 (George 38, Tatum 13/4/11, Boston leidde 72-50); Knicks-76ers 100-106 op 20-10.
- Onderling 2025/26: 3-1 Knicks (105-95 MSG, 123-117 TD Garden, 111-89 TD Garden, 112-106 MSG); geen play-offduel.
- Odds: TOTO uit specials/nba_feiten_2026_10_24.md (sport.toto.nl, 23-10 rond 12:00 NL).
  'Winnaar' = incl. verlenging; '1X2 excl. OT' = na 48 minuten.
  python3 specials/celtics_knicks_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "Celtics – Knicks voorspelling: wedtips en odds voor de thuisopener van Boston (24 oktober, 01:00)"
SLUG = "celtics-knicks-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("Boston speelt zijn eerste thuisduel tegen kampioen New York. Voorspelling, wedtips, TOTO-odds, "
                "blessures en opstellingen van Celtics – Knicks.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet-experts.nl/go/bet365"
DATUM = "2026-10-23T23:00:00.000Z"

# Deelkaart (maatwerk-kaart in de nieuwe stijl)
OG_KOP = "Celtics – Knicks <span>voorspelling</span>"
OG_EYEBROW = "NBA · zaterdag 24 oktober, 01:00"
OG_CHIPS = ["Thuisopener Boston", "3 wedtips"]
OG_MOTIEF = "tabel"
OG_DATA = ["Aftrap · 01:00", "Arena · TD Garden", "Onderling 25/26 · 3-1 Knicks", "Favoriet · Celtics"]

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>In de nacht van vrijdag op zaterdag om 01:00 Nederlandse tijd speelt Boston Celtics zijn eerste thuiswedstrijd van het seizoen, en de tegenstander is meteen regerend kampioen New York Knicks. Beide ploegen verloren hun eerste wedstrijd, dus er moet iemand van de 0-1 af. Onze voorspelling: Boston wint nipt met 110-107. Hoofdtip: minder dan 223,5 punten, met de Knicks +3,5 als tweede tip.</strong></p>
<p>Deze rivaliteit is beladen. In de play-offs van 2025 scheurde Jayson Tatum tegen de Knicks zijn achillespees, en vorig seizoen won New York drie van de vier onderlinge duels. Er is ook een nieuw verhaal: center Mitchell Robinson speelde jarenlang voor New York en staat nu bij Boston, terwijl Paul George zijn eerste wedstrijd in TD Garden speelt in het groen.</p>
<h3><strong>Celtics – Knicks: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "Boston Celtics – New York Knicks"),
    ("Datum", "Zaterdag 24 oktober 2026 (nacht van vrijdag op zaterdag)"),
    ("Aanvang", "01:00 Nederlandse tijd (vrijdag 19:00 in Boston)"),
    ("Arena", "TD Garden, Boston"),
    ("Competitie", "NBA, reguliere competitie 2026/27"),
    ("Stand 2026/27", "Celtics 0-1, Knicks 0-1"),
    ("Onderlinge duels 2025/26", "3-1 voor de Knicks"),
    ("Coaches", "Joe Mazzulla (Boston), Mike Brown (New York)"),
])}
<p>Het is de eerste van vier onderlinge duels dit seizoen. Geen van beide ploegen speelde donderdag.</p>
<h3><strong>Speelronde 1: twee nederlagen, heel verschillend</strong></h3>
<p>Boston begon dinsdagmiddag in Detroit en leek lang op weg naar een zege. Begin derde kwart stond het 72-50 voor de Celtics, nadat Paul George binnen een minuut drie driepunters raakte. Detroit won het laatste kwart met 39-25 en zegevierde met 121-113. George scoorde 38 punten (7 van 12 driepunters), het hoogste aantal ooit van een Celtic in zijn eerste wedstrijd voor de club. Tatum had een moeilijke avond: 13 punten bij 6 van 23 schoten en 0 van 7 achter de lijn, al gaf hij wel 11 assists.</p>
<p>De Knicks hesen dinsdag in Madison Square Garden hun kampioensvlag, maar verloren daarna met 100-106 van Philadelphia. New York schoot 37 procent uit het veld en maakte maar 11 van zijn 33 driepunters. Jalen Brunson scoorde 21 punten, maar raakte slechts 6 van zijn 19 schoten. Karl-Anthony Towns kwam tot 19 punten en 12 rebounds, en nieuwkomer Andre Drummond pakte vanaf de bank 14 rebounds.</p>
<h3><strong>Vorig seizoen: Knicks kampioen, Boston vroeg klaar</strong></h3>
<p>New York beleefde in 2025/26 een historisch seizoen. De ploeg won in december de NBA Cup (124-113 tegen San Antonio), eindigde als derde in het Oosten met 53-29 en ging daarna door de play-offs met 16 zeges en 3 nederlagen. Atlanta (4-2), Philadelphia (4-0), Cleveland (4-0) en in de finale San Antonio (4-1) werden uitgeschakeld. Het was de eerste titel sinds 1973 en Brunson werd MVP van de Finals.</p>
<p>Boston werd tweede in het Oosten met 56-26 en kreeg van alle NBA-ploegen de minste punten tegen. In de play-offs ging het mis: tegen Philadelphia gaven de Celtics in de eerste ronde een 3-1 voorsprong weg, en in de beslissende zevende wedstrijd ontbrak Tatum met een knieblessure.</p>
{tabel(["2025/26", "Boston Celtics", "New York Knicks"], [
    ("Eindstand", "56-26 (nr. 2 Oost)", "53-29 (nr. 3 Oost)"),
    ("Thuisrecord", "30-11", "30-10"),
    ("Punten voor / tegen", "114,9 / 107,2", "116,5 / 110,1"),
    ("Onderling", "1-3", "3-1"),
    ("Play-offs", "Eerste ronde (3-4 tegen Philadelphia)", "Kampioen (16-3)"),
])}
<p><em>De onderlinge duels: 95-105 in New York, 123-117 voor Boston in TD Garden, 89-111 in TD Garden en 106-112 in New York. Drie van de vier wedstrijden bleven onder de 220 punten.</em></p>"""

content2 = f"""<h3><strong>Zo zijn beide selecties veranderd</strong></h3>
<p><strong>Boston Celtics: Brown weg, George en Robinson erbij</strong></p>
<p>De grote transfer van de zomer: Boston ruilde Jaylen Brown begin juli naar Philadelphia. In ruil kwamen Paul George, twee keuzes in de eerste ronde van de draft (2028 en 2031) en twee in de tweede ronde. Daarnaast tekende Mitchell Robinson, vorig seizoen nog bij de Knicks, een contract van drie jaar en ruim 47 miljoen dollar, en kwam routinier Mike Conley voor één seizoen. Backup-center Nikola Vučević vertrok naar Orlando. Joe Mazzulla blijft de coach.</p>
<p>Het belangrijkste is dat Tatum voor het eerst sinds zijn achillespeesblessure een volledig seizoen kan spelen. Vorig seizoen kwam hij pas laat terug en speelde hij 16 wedstrijden in de reguliere competitie.</p>
<p><strong>New York Knicks: de kampioensploeg blijft grotendeels bij elkaar</strong></p>
<p>De Knicks hielden hun basisvijf intact. Het grootste verlies is Robinson: New York wilde niet boven de zogenoemde tweede salarisgrens uitkomen en liet hem vertrekken. Als vervanger kwam Andre Drummond over van Philadelphia, voor één jaar. Landry Shamet (vier jaar), Jose Alvarado (drie jaar), Mohamed Diawara (vier jaar) en Jordan Clarkson (één jaar) tekenden opnieuw. Mike Brown begint aan zijn tweede seizoen als coach.</p>
<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("Devin Carter", "Boston", "Speelt niet (ziek)"),
    ("Jaden Akins, Kevin McCullar jr., Tyler Nickel", "New York", "Twijfelachtig (two-way-spelers, G League)"),
])}
<p><em>Stand van de officiële NBA-blessurelijst op vrijdag 23 oktober, 12:00 Nederlandse tijd.</em></p>
<p><strong>Verwachte basisvijf Celtics:</strong> Derrick White, Jordan Walsh, Paul George, Jayson Tatum, Mitchell Robinson. Dat was de basis in Detroit. Mazzulla wisselt vaak; Neemias Queta (vorig seizoen 75 keer in de basis) of Payton Pritchard kan ook beginnen.</p>
<p><strong>Verwachte basisvijf Knicks:</strong> Jalen Brunson, Mikal Bridges, Josh Hart, OG Anunoby, Karl-Anthony Towns. Dezelfde vijf als tegen Philadelphia.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "Eerste duel 2026/27"], [
    ("Jalen Brunson (NYK)", "26,0", "3,3", "6,8", "21 punten, 6 van 19 schoten"),
    ("Karl-Anthony Towns (NYK)", "20,1", "11,9", "3,0", "19 punten, 12 rebounds"),
    ("OG Anunoby (NYK)", "16,7", "5,2", "2,2", "10 punten, 1 van 9 driepunters"),
    ("Josh Hart (NYK)", "12,0", "7,4", "4,8", "14 punten, 7 rebounds"),
    ("Jayson Tatum (BOS)", "21,8", "10,0", "5,3", "13 punten, 4 rebounds, 11 assists"),
    ("Paul George (BOS, vorig seizoen PHI)", "17,3", "5,3", "3,6", "38 punten, 7 van 12 driepunters"),
    ("Derrick White (BOS)", "16,5", "4,4", "5,4", "17 punten, 8 assists"),
    ("Payton Pritchard (BOS)", "17,0", "3,9", "5,2", "17 punten vanaf de bank"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26. Tatum speelde toen 16 wedstrijden, George 37.</em></p>
<p>Let ook op Robinson tegen zijn oude club: bij New York pakte hij vorig seizoen 8,8 rebounds in nog geen 20 minuten per wedstrijd.</p>
<h3><strong>Odds Celtics – Knicks bij TOTO</strong></h3>
<p>De bookmakers zien Boston als lichte favoriet, vooral door het thuisvoordeel. Bij <a href="/bookmakers/toto">TOTO</a> ligt de handicap op 2,5 punten in het voordeel van de Celtics en het verwachte puntentotaal op 223,5.</p>
{tabel(["Markt", "Celtics", "Knicks"], [
    ("Winnaar (incl. verlenging)", "1,74", "2,15"),
    ("1X2 (reguliere speeltijd, gelijk 17,00)", "1,73", "2,20"),
    ("Handicap -2,5 / +2,5 (incl. verlenging)", "1,93", "1,87"),
    ("Handicap -3,5 / +3,5 (incl. verlenging)", "1,98", "1,71"),
])}
<p>Op het totaal van 223,5 punten biedt TOTO Over 1,91 en Under 1,91. Wij lazen de odds op vrijdag 23 oktober rond 12:00 uur; vergelijk ze vlak voor de start nog even.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op Celtics – Knicks</strong></a></p>"""

content3 = f"""<h3><strong>Onze voorspelling: een krappe thuiszege voor Boston</strong></h3>
<p>We kiezen voor Boston, maar verwachten geen ruim verschil. De Celtics spelen thuis, waar ze vorig seizoen 30 van de 41 wedstrijden wonnen, en zagen in Detroit drie kwarten lang hoe goed George in deze ploeg past. Tatum zal na zijn 6 van 23 bijna zeker beter schieten.</p>
<p>Toch zijn er genoeg redenen om voorzichtig te zijn. New York won vorig seizoen drie van de vier onderlinge duels, waaronder een 89-111 in TD Garden, en heeft een ingespeelde kampioensploeg. Boston gaf in Detroit een voorsprong van 22 punten weg en moet zonder Brown nog uitvinden wie in de slotfase de bal krijgt. Ook verwachten we geen hoge score: Boston kreeg vorig seizoen de minste punten tegen van de hele NBA, de Knicks stonden met 110,1 punten tegen op de vijfde plaats, en de onderlinge duels eindigden gemiddeld op 214,5 punten. Onze voorspelling: <strong>Boston Celtics – New York Knicks 110-107</strong>.</p>
<h3><strong>Wedtips voor Celtics – Knicks</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Inzet"], [
    ("Minder dan 223,5 punten (incl. verlenging)", "1,91", "TOTO", "Hoofdtip"),
    ("New York Knicks +3,5 punten (incl. verlenging)", "1,71", "TOTO", "Tweede tip"),
    ("Boston Celtics wint (incl. verlenging)", "1,74", "TOTO", "Kleinere inzet"),
])}
<p><strong>1. Minder dan 223,5 punten (1,91).</strong> TOTO rekent hier met ongeveer 50 procent kans; wij schatten de kans op de Under op zo'n 55 procent. Drie van de vier onderlinge duels vorig seizoen bleven ruim onder deze lijn (200, 200 en 218 punten), en beide ploegen hoorden bij de beste verdedigingen van de competitie. Het risico: Boston kreeg in Detroit 121 punten tegen en een verlenging kan het totaal flink opdrijven. Dit is daarom een tip met een gemiddeld risico.</p>
<p><strong>2. Knicks +3,5 (1,71).</strong> Hiermee win je als New York wint of met maximaal drie punten verliest. TOTO rekent met iets meer dan 50 procent kans, wij komen uit op zo'n 60 procent. Het risico zit in een avond waarop George en Tatum allebei goed schieten: dan kan Boston ook met tien punten winnen.</p>
<p><strong>3. Celtics wint (1,74).</strong> Dit past bij onze voorspelling: thuisvoordeel, een Boston dat na de nederlaag in Detroit iets recht te zetten heeft en Knicks die nog op zoek zijn naar hun ritme. TOTO rekent met zo'n 55 procent kans, wij schatten die op ongeveer 58 procent. Het verschil is klein, dus speel deze tip met een kleinere inzet. Tip 2 en 3 gaan prima samen: wint Boston met één tot drie punten, dan zijn ze allebei raak.</p>
<h3><strong>Celtics – Knicks live kijken in Nederland</strong></h3>
<p>De makkelijkste manier om de wedstrijd te zien: bij <a href="/bookmakers/bet365">Bet365</a> kun je NBA-wedstrijden live streamen. Je hebt alleen een account met een kleine storting nodig, en die storting kun je daarna gewoon weer opnemen. In Nederland heeft ESPN de NBA-rechten, maar niet elke wedstrijd staat op een van de Nederlandse ESPN-kanalen. Met <strong>NBA League Pass</strong>, de betaalde streamingdienst van de competitie, kun je ook alle wedstrijden volgen.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk Celtics – Knicks live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Lees ook onze voorspellingen voor <a href="/nieuws/pistons-celtics-voorspelling-wedtips-nba-opening-2026">Pistons – Celtics</a>, <a href="/nieuws/76ers-cavaliers-voorspelling-wedtips-nba-2026">76ers – Cavaliers</a> en <a href="/nieuws/lakers-warriors-voorspelling-wedtips-nba-2026">Lakers – Warriors</a>, en het artikel <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">Welke Nederlanders spelen in de NBA</a>. Nieuw met wedden op basketbal? Lees eerst <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels in de NBA</a> en onze uitleg over <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap wedden</a>. Alle basketbaltips vind je op onze pagina <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Celtics – Knicks?</strong><br>Zaterdag 24 oktober 2026 om 01:00 Nederlandse tijd, in de nacht van vrijdag op zaterdag. In Boston is het dan vrijdagavond 19:00.</p>
<p><strong>Waar wordt Celtics – Knicks gespeeld?</strong><br>In TD Garden in Boston. Het is de eerste thuiswedstrijd van de Celtics dit seizoen.</p>
<p><strong>Wie is favoriet: Celtics of Knicks?</strong><br>Boston, met een quotering van 1,74 bij TOTO. De Knicks staan op 2,15.</p>
<p><strong>Hoe ging het vorig seizoen tussen deze ploegen?</strong><br>New York won drie van de vier duels in de reguliere competitie, Boston won alleen thuis met 123-117. In de play-offs troffen ze elkaar niet.</p>
<p><strong>Speelt Mitchell Robinson tegen zijn oude club?</strong><br>Ja, hij staat niet op de blessurelijst. Robinson tekende deze zomer bij Boston, nadat hij jarenlang voor de Knicks speelde.</p>
<p><strong>Wat is onze voorspelling voor Celtics – Knicks?</strong><br>Boston wint met 110-107. Onze hoofdtip is minder dan 223,5 punten (1,91 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

KAART = {"home": "Celtics", "away": "Knicks", "home_abbr": "bos", "away_abbr": "ny", "home_pos": "56-26 · nr. 2 Oost 2025/26", "away_pos": "53-29 · nr. 3 Oost 2025/26", "hs": 110, "as": 107, "datum": "Za 24 okt", "tijd": "01:00", "odd_home": "1,74", "odd_away": "2,15"}
WEDTIPS = {"wedtip-1-2": "Minder dan 223,5 punten (incl. verlenging)", "quotering-wedtip-1": "1.91",
           "wedtip-2-2": "New York Knicks +3,5 punten (incl. verlenging)", "quotering-wedtip-2": "1.71",
           "wedtip-3-2": "Boston Celtics wint (incl. verlenging)", "quotering-wedtip-3": "1.74",
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
