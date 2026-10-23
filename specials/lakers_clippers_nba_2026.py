# -*- coding: utf-8 -*-
"""Los artikel: Lakers – Clippers voorspelling, NBA 24 oktober 2026 (04:00 NL). Feiten nagelopen op 23-10-2026
(ESPN-API: boxscores 401909092 en 401909842, rosters, standen en onderlinge duels 2025/26; officiele NBA-blessurelijst
23-10 05:00 ET; AP/NBA.com over de ruilen Harden-Garland (3-2-2026) en Zubac (5-2-2026); berichtgeving over de
Leonard-ruil met Toronto en de NBA-straf van 2-9-2026).
- Lakers-Warriors 127-105 (Doncic 28/8/7, Kessler 26 met 12/12, Reaves 23); Clippers-Kings 121-96 (Garland 30, Lopez 17/11).
- Onderling 2025/26: 2-2, steeds won de thuisploeg (135-118 LAL, 103-88 LAC, 112-104 LAC, 125-122 LAL).
- Collin Sexton miste de opener (soleus), staat niet meer op de lijst van 23-10 05:00 ET.
- Doncic 2025/26: 30+ in 44 van 65 duels (gamelog); Kessler 2024/25: 28 double-doubles in 58 duels.
- Odds: alleen TOTO, uit specials/nba_feiten_2026_10_24.md (±12:00 NL op 23-10).
  python3 specials/lakers_clippers_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "Lakers – Clippers voorspelling: wedtips en odds voor de LA-derby (24 oktober, 04:00)"
SLUG = "lakers-clippers-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("De Lakers ontvangen een gehavend Clippers in de eerste LA-derby van het seizoen. Voorspelling, wedtips, "
                "TOTO-odds, blessures en opstellingen.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet-experts.nl/go/bet365"
DATUM = "2026-10-24T02:00:00.000Z"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>In de nacht van vrijdag op zaterdag om 04:00 Nederlandse tijd staat de eerste stadsderby van het seizoen op het programma: de Los Angeles Lakers ontvangen de LA Clippers. Beide ploegen wonnen hun openingsduel ruim, maar de Clippers missen Bradley Beal, Brandon Ingram en Max Strus. Onze voorspelling: de Lakers winnen met 118-108. Hoofdtip: Luka Dončić scoort 30 punten of meer.</strong></p>
<p>De derby heeft dit seizoen een heel ander gezicht. Bij de Lakers draait alles om Dončić, Austin Reaves en nieuwe center Walker Kessler. De Clippers zijn bijna volledig omgebouwd: Kawhi Leonard speelt weer in Toronto, James Harden in Cleveland en Darius Garland is nu de leider. Hieronder lees je alles over selecties, blessures, de odds van <a href="/bookmakers/toto">TOTO</a> en onze tips.</p>
<h3><strong>Lakers – Clippers: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "Los Angeles Lakers – LA Clippers"),
    ("Datum", "Zaterdag 24 oktober 2026 (nacht van vrijdag op zaterdag)"),
    ("Aanvang", "04:00 Nederlandse tijd (vrijdag 19:00 in Los Angeles)"),
    ("Arena", "Crypto.com Arena, Los Angeles"),
    ("Competitie", "NBA, reguliere competitie 2026/27"),
    ("Stand 2026/27", "Lakers 1-0, Clippers 1-0"),
    ("Onderlinge duels 2025/26", "2-2"),
])}
<p>De Lakers zijn de thuisploeg en beide teams hadden donderdag een rustdag. Al op 28 oktober volgt de return in de Intuit Dome van de Clippers (in Nederland donderdag 29 oktober om 03:30); daarna treffen ze elkaar nog op 12 januari en 11 februari 2027.</p>
<h3><strong>Speelronde 1: twee ruime overwinningen</strong></h3>
<p>De Lakers versloegen Golden State met 127-105 en stonden maximaal 35 punten voor. Dončić had genoeg aan 30 minuten voor 28 punten, 8 rebounds en 7 assists. Uitblinker was Kessler: 26 punten en 9 rebounds bij zijn debuut, met alle 12 schoten raak. Reaves scoorde 23 punten.</p>
<p>De Clippers wonnen met 121-96 van Sacramento. Garland scoorde 30 punten, bankspeler Brook Lopez had 17 punten en 11 rebounds en rookie Keaton Wagler, de nummer vijf van de draft, kwam tot 15 punten. Wel eindigden de Kings vorig seizoen op 22-60 en de Warriors misten onder anderen Jimmy Butler en Kristaps Porziņģis.</p>
<h3><strong>Vorig seizoen: Lakers vierde, Clippers in de play-in</strong></h3>
<p>De Lakers wonnen in 2025/26 53 van de 82 wedstrijden, versloegen Houston in de eerste ronde van de play-offs (4-2) en gingen daarna met 0-4 onderuit tegen Oklahoma City. De Clippers werden met 42-40 negende in het Westen en verloren in de play-in thuis van Golden State (121-126).</p>
{tabel(["2025/26", "Los Angeles Lakers", "LA Clippers"], [
    ("Eindstand", "53-29 (nr. 4 West)", "42-40 (nr. 9 West)"),
    ("Thuis / uit", "28-13 / 25-16", "23-18 / 19-22"),
    ("Punten voor / tegen", "116,3 / 114,6", "113,8 / 112,6"),
    ("Na het seizoen", "Tweede ronde (0-4 tegen OKC)", "Uitgeschakeld in de play-in"),
])}
<p>De vier derby's van vorig seizoen werden allemaal gewonnen door de thuisploeg: de Lakers wonnen thuis met 135-118 en 125-122, de Clippers met 103-88 en 112-104. Dončić scoorde in die duels 43, 12, 32 en 38 punten.</p>"""

content2 = f"""<h3><strong>Zo zijn beide selecties veranderd</strong></h3>
<p><strong>LA Clippers: een nieuwe ploeg rond Garland</strong></p>
<p>De ombouw begon in februari. Harden werd geruild met Cleveland voor Garland, die daarna nog 19 duels speelde voor de Clippers (19,9 punten, 6,4 assists). Center Ivica Zubac vertrok naar Indiana voor Bennedict Mathurin, Isaiah Jackson en draftkeuzes; een daarvan werd de vijfde keuze, Wagler. Deze zomer ging Leonard terug naar Toronto, in ruil voor Ingram, Gradey Dick en draftkeuzes. Rui Hachimura kwam over van de Lakers, Max Strus sloot aan en Beal en Lopez bleven. Mathurin, John Collins en Bogdan Bogdanović vertrokken. Tyronn Lue blijft de coach.</p>
<p><strong>Los Angeles Lakers: alles om Dončić</strong></p>
<p>LeBron James tekende bij Philadelphia, en naast Hachimura vertrokken onder anderen Deandre Ayton, Marcus Smart en Luke Kennard. Kessler kwam via een sign-and-trade uit Utah, en ook Quentin Grimes, Collin Sexton, Kevon Looney en Matisse Thybulle sloten aan. JJ Redick begint aan zijn derde seizoen als coach.</p>
<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("Bradley Beal", "LA Clippers", "Speelt niet (rechterknie)"),
    ("Brandon Ingram", "LA Clippers", "Speelt niet (herstel na operatie aan de rechterhiel)"),
    ("Max Strus", "LA Clippers", "Speelt niet (scheur in de voetzoolpees, rechtervoet)"),
    ("Yanic Konan Niederhauser", "LA Clippers", "Speelt niet (voetoperatie)"),
    ("Jordan Miller", "LA Clippers", "Speelt niet (schouderoperatie)"),
    ("Jake LaRavia", "LA Lakers", "Twijfelachtig (rechterenkel)"),
    ("Cameron Carr", "LA Lakers", "Speelt niet (schuine buikspier)"),
    ("Adou Thiero", "LA Lakers", "Speelt niet (linkerknie)"),
    ("Collin Sexton", "LA Lakers", "Miste de opener (kuit), staat niet meer op de lijst"),
])}
<p><em>Stand van de officiële NBA-blessurelijst op vrijdag 23 oktober, 11:00 Nederlandse tijd.</em></p>
<p><strong>Verwachte basisvijf Lakers:</strong> Luka Dončić, Austin Reaves, Matisse Thybulle, Ziaire Williams, Walker Kessler. Dezelfde vijf als tegen Golden State.</p>
<p><strong>Verwachte basisvijf Clippers:</strong> Darius Garland, Kris Dunn, Derrick Jones Jr., Rui Hachimura, Isaiah Jackson. Lopez, Wagler en Dick zijn de belangrijkste wissels. Voor Hachimura is het meteen een weerzien met zijn oude club.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "Bijzonderheid"], [
    ("Luka Dončić (LAL)", "33,5", "7,7", "8,3", "Drie keer 32+ punten in vier derby's"),
    ("Austin Reaves (LAL)", "23,3", "4,7", "5,5", "23 punten in de opener"),
    ("Walker Kessler (LAL)", "14,4", "10,8", "3,0", "Vorig seizoen 5 duels (schouder)"),
    ("Darius Garland (LAC)", "19,9", "2,3", "6,4", "Cijfers bij de Clippers"),
    ("Rui Hachimura (LAC)", "11,5", "3,3", "0,8", "Cijfers bij de Lakers"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26.</em></p>
<h3><strong>Odds Lakers – Clippers bij TOTO</strong></h3>
<p>TOTO ziet de Lakers als grote favoriet: een quotering van 1,25 staat voor ongeveer 78 procent kans. De handicap ligt op 9,5 punten en het verwachte puntentotaal op 228,5.</p>
{tabel(["Markt", "Lakers", "Clippers"], [
    ("Winnaar (incl. verlenging)", "1,25", "4,10"),
    ("1X2 (reguliere speeltijd, gelijk 19,00)", "1,23", "4,50"),
    ("Handicap -8,5 / +8,5", "1,73", "1,95"),
    ("Handicap -9,5 / +9,5", "1,93", "1,87"),
    ("Handicap -10,5 / +10,5", "2,00", "1,71"),
])}
<p>Op het totaal biedt TOTO 227,5 (Over 1,77 / Under 1,93), 228,5 (1,91 / 1,91) en 229,5 (Over 1,93 / Under 1,77). Dončić staat op 2,15 voor 30 punten of meer en op 3,80 voor 35 of meer; een double-double van Kessler levert 1,56 op. Odds gelezen op vrijdag rond 12:00 uur; vergelijk ze vlak voor de start nog even.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op Lakers – Clippers</strong></a></p>"""

content3 = f"""<h3><strong>Onze voorspelling: Lakers winnen, maar geen walk-over</strong></h3>
<p>De Lakers spelen thuis, hebben met Dončić de beste speler op het veld en het samenspel met Kessler werkte meteen. De Clippers missen drie spelers die voor punten moeten zorgen en hebben buiten Garland weinig spelers die zelf een kans creëren. Toch verwachten we geen herhaling van woensdag. De Clippers kregen vorig seizoen minder punten tegen dan de Lakers (112,6 tegen 114,6 per wedstrijd), en met Dunn en Jones Jr. heeft Lue twee verdedigers die Dončić het leven zuur kunnen maken. Onze voorspelling: <strong>Los Angeles Lakers – LA Clippers 118-108</strong>.</p>
<h3><strong>Wedtips voor Lakers – Clippers</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Inzet"], [
    ("Luka Dončić scoort 30 punten of meer", "2,15", "TOTO", "Hoofdtip"),
    ("Los Angeles Lakers -8,5 punten (incl. verlenging)", "1,73", "TOTO", "Tweede tip"),
    ("Minder dan 229,5 punten (incl. verlenging)", "1,77", "TOTO", "Derde tip"),
])}
<p><strong>1. Dončić 30+ punten (2,15).</strong> TOTO geeft hem zo'n 47 procent kans. Vorig seizoen haalde hij de 30 punten in ongeveer twee derde van zijn wedstrijden, en tegen de Clippers drie keer in vier duels. Wij schatten de kans op ruim 55 procent. Risico: loopt de wedstrijd vroeg uit de hand, dan zit hij in het laatste kwart op de bank, zoals woensdag.</p>
<p><strong>2. Lakers -8,5 (1,73).</strong> De Lakers moeten met minstens negen punten winnen. De bookmaker schat die kans op 58 procent, wij op ruim 60, omdat de Clippers zonder drie aanvallers komen. Maar vorig seizoen wonnen de Lakers hun thuisderby's met 17 en met maar 3 punten verschil: een nipte zege kost je deze tip.</p>
<p><strong>3. Minder dan 229,5 punten (1,77).</strong> Onze voorspelling komt uit op 226 punten en de opener van de Clippers eindigde op 217. Zonder hun aanvallers zakt de puntenproductie van de Clippers, terwijl hun verdediging bij de betere van het Westen hoorde. Eerlijk is eerlijk: twee derby's van vorig seizoen gingen ruim over deze lijn (253 en 247 punten). Gemiddeld risico; wij schatten de kans op 58 procent.</p>
<p>Een double-double van Kessler (1,56) laten we liggen. In zijn laatste volledige seizoen bij Utah haalde hij er in iets minder dan de helft van zijn wedstrijden een, terwijl deze quotering voor bijna 64 procent kans staat.</p>
<h3><strong>Lakers – Clippers live kijken in Nederland</strong></h3>
<p>De makkelijkste manier: bij <a href="/bookmakers/bet365">Bet365</a> kijk je NBA-wedstrijden gratis live. Je hebt alleen een account met een kleine storting nodig, en die storting kun je daarna gewoon weer opnemen. ESPN heeft in Nederland de NBA-rechten, maar zendt maar een deel van de wedstrijden uit; check vooraf de gids. Met <strong>NBA League Pass</strong>, de betaalde streamingdienst van de competitie, volg je alle wedstrijden. Meer opties vind je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk Lakers – Clippers live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Lees ook onze voorspellingen voor <a href="/nieuws/lakers-warriors-voorspelling-wedtips-nba-2026">Lakers – Warriors</a>, <a href="/nieuws/76ers-cavaliers-voorspelling-wedtips-nba-2026">76ers – Cavaliers</a>, <a href="/nieuws/thunder-nuggets-voorspelling-wedtips-nba-2026">Thunder – Nuggets</a>, <a href="/nieuws/pistons-celtics-voorspelling-wedtips-nba-opening-2026">Pistons – Celtics</a> en <a href="/nieuws/spurs-thunder-voorspelling-wedtips-nba-opening-2026">Spurs – Thunder</a>, en de <a href="/nieuws/nba-voorspellingen-vannacht-22-oktober-2026">NBA-voorspellingen van 22 oktober</a>. Benieuwd naar <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">welke Nederlanders in de NBA spelen</a>? Nieuw met wedden op basketbal? Lees <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels in de NBA</a>, <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">wat handicap wedden is</a> en <a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">hoe een money line werkt</a>. Alle basketbaltips vind je op <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Lakers – Clippers?</strong><br>Zaterdag 24 oktober 2026 om 04:00 Nederlandse tijd. In Los Angeles is het dan vrijdagavond 19:00.</p>
<p><strong>Waar wordt Lakers – Clippers gespeeld?</strong><br>In de Crypto.com Arena in Los Angeles. De Lakers zijn de thuisploeg.</p>
<p><strong>Speelt Kawhi Leonard nog voor de Clippers?</strong><br>Nee. Leonard werd deze zomer geruild met Toronto, waar hij in 2019 kampioen werd. Ook James Harden is weg: hij speelt sinds februari 2026 voor Cleveland.</p>
<p><strong>Welke Clippers ontbreken?</strong><br>Bradley Beal, Brandon Ingram, Max Strus, Yanic Konan Niederhauser en Jordan Miller staan allemaal als afwezig op de blessurelijst.</p>
<p><strong>Wie is favoriet: Lakers of Clippers?</strong><br>De Lakers, met een quotering van 1,25 bij TOTO. De Clippers staan op 4,10.</p>
<p><strong>Wat is onze voorspelling voor Lakers – Clippers?</strong><br>De Lakers winnen met 118-108. Onze hoofdtip is Dončić 30 punten of meer (2,15 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

KAART = {"home": "Lakers", "away": "Clippers", "home_abbr": "lal", "away_abbr": "lac", "home_pos": "53-29 · nr. 4 West 2025/26", "away_pos": "42-40 · nr. 9 West 2025/26", "hs": 118, "as": 108, "datum": "Za 24 okt", "tijd": "04:00", "odd_home": "1,25", "odd_away": "4,10"}
WEDTIPS = {"wedtip-1-2": "Luka Dončić scoort 30 punten of meer", "quotering-wedtip-1": "2.15",
           "wedtip-2-2": "Los Angeles Lakers -8,5 punten (incl. verlenging)", "quotering-wedtip-2": "1.73",
           "wedtip-3-2": "Minder dan 229,5 punten (incl. verlenging)", "quotering-wedtip-3": "1.77",
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
