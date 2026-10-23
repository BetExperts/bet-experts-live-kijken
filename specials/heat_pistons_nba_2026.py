# -*- coding: utf-8 -*-
"""Los artikel: Heat – Pistons voorspelling, NBA 24 oktober 2026 (02:00 NL). Feiten nagelopen op 23-10-2026
(ESPN-API: scoreboard, summary/boxscores 401909091 en 401909088, schema's en stand 2025/26, rosters; ESPN, AP, NBA.com).
- Heat-Timberwolves 106-131 op 21-10 (Giannis 35, 13/19; Adebayo 15; Edwards 45). Pistons-Celtics 121-113 op 20-10.
- Giannis-ruil: akkoord 22-06-2026, officieel 06-07-2026. Herro, Ware, Jaquez jr., Jakucionis, nr. 13 van de draft 2026,
  eerste ronde 2031 en 2033 (onbeschermd), pickswap 2030 en tweede ronde 2033 naar Milwaukee; Giannis en Portis naar Miami.
- Odds: TOTO volgens het feitenblad specials/nba_feiten_2026_10_24.md (±12:00 NL op 23-10).
  'Winnaar' = incl. verlenging; '1X2 excl. OT' = na 48 minuten.
  python3 specials/heat_pistons_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "Heat – Pistons voorspelling: wedtips en odds voor Giannis tegen Cade (24 oktober, 02:00)"
SLUG = "heat-pistons-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("Giannis Antetokounmpo en Miami ontvangen het Detroit van Cade Cunningham. Voorspelling, wedtips, "
                "TOTO-odds, blessures en opstellingen.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet-experts.nl/go/bet365"
DATUM = "2026-10-24T00:00:00.000Z"

# Deelkaart (maatwerk-kaart in de nieuwe stijl)
OG_KOP = "Heat – Pistons <span>voorspelling</span>"
OG_EYEBROW = "NBA · zaterdag 24 oktober, 02:00"
OG_CHIPS = ["Giannis tegen Cade", "3 wedtips"]
OG_MOTIEF = "tabel"
OG_DATA = ["Aftrap · 02:00", "Arena · Kaseya Center", "Onderling 25/26 · 2-1 Heat", "Odds · 1,91 / 1,91"]

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>In de nacht van vrijdag op zaterdag om 02:00 Nederlandse tijd speelt Giannis Antetokounmpo zijn tweede wedstrijd voor de Miami Heat, en zijn eerste tegen een topploeg uit het Oosten. Tegenstander Detroit, met spelverdeler Cade Cunningham, won dinsdag de seizoensopener van Boston. Miami verloor woensdag met ruime cijfers van Minnesota. De bookmakers zien een volledig gelijkopgaande wedstrijd. Onze voorspelling: Detroit wint met 116-110. Hoofdtip: de Pistons winnen, met minder dan 236,5 punten als tweede tip.</strong></p>
<h3><strong>Heat – Pistons: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "Miami Heat – Detroit Pistons"),
    ("Datum", "Zaterdag 24 oktober 2026 (nacht van vrijdag op zaterdag)"),
    ("Aanvang", "02:00 Nederlandse tijd (vrijdag 20:00 in Miami)"),
    ("Arena", "Kaseya Center, Miami"),
    ("Competitie", "NBA, reguliere competitie 2026/27"),
    ("Stand 2026/27", "Heat 0-1, Pistons 1-0"),
    ("Onderlinge duels 2025/26", "2-1 voor de Heat"),
])}
<p>Dit seizoen volgen nog drie onderlinge duels: op 15 november (02:00 Nederlandse tijd) opnieuw in Miami, en op 26 februari (01:00) en 4 april 2027 (21:00) in Detroit.</p>
<h3><strong>Speelronde 1: Detroit herstelt, Miami onderuit</strong></h3>
<p>Detroit won dinsdag met 121-113 van Boston. Bij rust stonden de Pistons nog 45-58 achter, vroeg in het derde kwart zelfs 50-72, maar na rust won Detroit met 76-55. Jalen Duren (22 punten, 9 rebounds) en Cunningham (22 punten, 8 assists) waren de topscorers, Duncan Robinson maakte 21 punten met vijf driepunters en invaller Javonte Green scoorde 19 punten in de tweede helft.</p>
<p>Miami verloor woensdag met 106-131 van Minnesota. Antetokounmpo scoorde 35 punten (13 van 19 uit het veld), maar kreeg weinig hulp. Bam Adebayo kwam tot 15 punten. Het grootste probleem lag buiten de driepuntslijn: de Heat maakten 8 van hun 33 driepunters, Minnesota 21 van de 50. Anthony Edwards scoorde in zijn eentje 45 punten. Ook de rebounds gingen met 52-34 naar Minnesota.</p>
<h3><strong>Vorig seizoen: Detroit de beste van het Oosten, Miami strandde in de play-in</strong></h3>
<p>Detroit won in 2025/26 60 van de 82 wedstrijden en werd eerste in de Eastern Conference. In de play-offs kwam de ploeg van coach J.B. Bickerstaff in de eerste ronde terug van een 1-3 achterstand tegen Orlando. In de tweede ronde was Cleveland na zeven wedstrijden te sterk; de beslissende wedstrijd in Detroit ging met 94-125 verloren.</p>
<p>Miami eindigde op 43-39 en als nummer tien van het Oosten. In de play-in verloor de ploeg van coach Erik Spoelstra met 126-127 in Charlotte. Thuis was Miami sterk (26-15), uit won de ploeg maar 17 keer.</p>
{tabel(["2025/26", "Miami Heat", "Detroit Pistons"], [
    ("Eindstand", "43-39 (nr. 10 Oost)", "60-22 (nr. 1 Oost)"),
    ("Thuis / uit", "26-15 / 17-24", "32-9 / 28-13"),
    ("Punten voor / tegen", "120,9 / 118,5", "117,8 / 109,6"),
    ("Onderling", "2-1", "1-2"),
    ("Play-offs", "Uitgeschakeld in de play-in (126-127 in Charlotte)", "Tweede ronde (3-4 tegen Cleveland)"),
])}
<p><em>Gemiddelde punten per wedstrijd in de reguliere competitie. De onderlinge duels: Heat – Pistons 135-138 (29 november), Pistons – Heat 112-118 (1 januari) en Heat – Pistons 121-110 (8 maart).</em></p>"""

content2 = f"""<h3><strong>Zo zijn beide selecties veranderd</strong></h3>
<p><strong>Miami Heat: Giannis erbij, Herro weg</strong></p>
<p>Op 22 juni werden Miami en Milwaukee het eens over de grootste ruil van de zomer, op 6 juli werd die officieel. Antetokounmpo en Bobby Portis gingen naar Miami. Milwaukee kreeg Tyler Herro, Kel'el Ware, Jaime Jaquez jr. en Kasparas Jakučionis, plus de nummer 13 van de draft van 2026, onbeschermde keuzes in de eerste ronde van 2031 en 2033, een ruil van keuzes in 2030 en een keuze in de tweede ronde van 2033. Ook Norman Powell, vorig seizoen een van de topscorers van Miami, vertrok: hij koos als vrije speler voor Chicago.</p>
<p>Voor meer schotkracht rond Antetokounmpo en Adebayo tekende de 36-jarige Klay Thompson, viervoudig kampioen, na zijn vertrek bij Dallas voor twee jaar. Tim Hardaway jr. kwam over van Denver en in augustus tekende center Nick Richards. Andrew Wiggins en Simone Fontecchio bleven.</p>
<p><strong>Detroit Pistons: kleine aanpassingen</strong></p>
<p>Detroit bouwde verder op de ploeg van vorig seizoen. John Collins kwam via een sign-and-trade van de Clippers, schutter Isaiah Joe van Oklahoma City en Taurean Prince van Milwaukee. Tobias Harris, Isaiah Stewart, Caris LeVert en Marcus Sasser vertrokken. Center Duren tekende pas begin oktober een nieuw contract. Duncan Robinson, tot 2025 zeven seizoenen bij Miami, speelt tegen zijn oude club.</p>
<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("Taurean Prince", "Detroit", "Waarschijnlijk inzetbaar (persoonlijke redenen)"),
    ("Geen meldingen", "Miami", "Volledige selectie beschikbaar"),
])}
<p><em>Stand van de blessurelijst op vrijdag 23 oktober, 12:00 Nederlandse tijd. Center Vladislav Goldin staat niet op de lijst, maar kwam in de opener niet in actie.</em></p>
<p><strong>Verwachte basisvijf Heat:</strong> Davion Mitchell, Klay Thompson, Andrew Wiggins, Giannis Antetokounmpo, Bam Adebayo. Dezelfde vijf als tegen Minnesota.</p>
<p><strong>Verwachte basisvijf Pistons:</strong> Cade Cunningham, Duncan Robinson, Ausar Thompson, John Collins, Jalen Duren. Dezelfde vijf als tegen Boston; Paul Reed, Javonte Green en Isaiah Joe komen als eersten van de bank.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "Bijzonderheid"], [
    ("Giannis Antetokounmpo (MIA)", "27,6", "9,8", "5,4", "Cijfers bij Milwaukee, maar 36 wedstrijden gespeeld"),
    ("Bam Adebayo (MIA)", "20,1", "10,0", "3,2", "Moet onder de ring Duren afstoppen"),
    ("Andrew Wiggins (MIA)", "15,4", "4,8", "2,7", "41,4% driepunters"),
    ("Cade Cunningham (DET)", "23,9", "5,5", "9,9", "Spelverdeler en leider van de Pistons"),
    ("Jalen Duren (DET)", "19,5", "10,5", "2,0", "65% van zijn schoten raak"),
    ("Ausar Thompson (DET)", "9,9", "5,7", "3,1", "2,0 steals, waarschijnlijk op Giannis"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26.</em></p>
<p>De sleutel: kan Detroit Antetokounmpo uit de buurt van de ring houden, met Ausar Thompson en Collins op hem en Duren als laatste man? Tegen Minnesota kwam Antetokounmpo in foulproblemen (vijf persoonlijke fouten in 30 minuten); gebeurt dat opnieuw, dan heeft Miami weinig andere creatieve spelers.</p>
<h3><strong>Odds Heat – Pistons bij TOTO</strong></h3>
<p>Een echte fiftyfifty volgens <a href="/bookmakers/toto">TOTO</a>: beide ploegen staan op 1,91. In de handicapmarkt is Miami heel licht favoriet (-1,5).</p>
{tabel(["Markt", "Heat", "Pistons"], [
    ("Winnaar (incl. verlenging)", "1,91", "1,91"),
    ("1X2 (reguliere speeltijd, gelijk 16,00)", "1,95", "1,95"),
    ("Handicap Heat -1,5 / Pistons +1,5", "2,00", "1,80"),
    ("Handicap Heat -2,5 / Pistons +2,5", "2,05", "1,65"),
    ("Handicap Heat -3,5 / Pistons +3,5", "2,25", "1,56"),
])}
<p>Op het totaal van 236,5 punten biedt TOTO Over 1,93 en Under 1,87; op 235,5 punten is dat Over 1,78 en Under 1,91. Alle handicaps en totalen zijn inclusief verlenging. Odds gelezen op 23 oktober rond 12:00 uur; vergelijk ze vlak voor de start nog even. Uitleg vind je in <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">wat is handicap wedden</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op Heat – Pistons</strong></a></p>"""

content3 = f"""<h3><strong>Onze voorspelling: Detroit wint in Miami</strong></h3>
<p>Wij kiezen voor Detroit. De Pistons zijn een ingespeelde ploeg met een van de beste verdedigingen van vorig seizoen, en lieten in Boston zien dat ze ook na een grote achterstand blijven knokken. Tegen Boston won Detroit de reboundstrijd (49-39) en kreeg het 32 vrije worpen; juist onder de borden kwam Miami tegen Minnesota tekort. En Detroit had sinds dinsdag drie dagen rust.</p>
<p>Miami heeft wel thuisvoordeel, won twee van de drie onderlinge duels en heeft een speler die in zijn eentje een wedstrijd kan beslissen. Maar de ploeg is nieuw en het schot van afstand was in de opener zwak. Daar komt bij dat Miami zaterdag (Amerikaanse tijd) alweer in Charlotte speelt: een back-to-back, dus Spoelstra moet de minuten verdelen. Detroit speelt pas zondag weer, in Philadelphia. Onze voorspelling: <strong>Miami Heat – Detroit Pistons 110-116</strong>.</p>
<h3><strong>Wedtips voor Heat – Pistons</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Inzet"], [
    ("Detroit Pistons wint (incl. verlenging)", "1,91", "TOTO", "Hoofdtip"),
    ("Minder dan 236,5 punten (incl. verlenging)", "1,87", "TOTO", "Tweede tip"),
    ("Detroit Pistons +3,5 punten (incl. verlenging)", "1,56", "TOTO", "Veiligere tip"),
])}
<p><strong>1. Pistons winnen (1,91).</strong> De odds rekenen met ongeveer 50 procent kans, wij schatten de kans van Detroit op zo'n 56 procent. Het risico: Antetokounmpo heeft genoeg aan één grote avond, en thuis speelt Miami een stuk beter dan uit.</p>
<p><strong>2. Minder dan 236,5 punten (1,87).</strong> Detroit kreeg vorig seizoen maar 109,6 punten per wedstrijd tegen en Miami schoot in de opener slecht van afstand. Het risico: Heat-wedstrijden waren vorig seizoen vaak hoog scorend. Twee van de drie onderlinge duels bleven onder deze lijn (230 en 231 punten), het derde ging er ruim overheen (273). Wij schatten de kans op ongeveer 54 procent.</p>
<p><strong>3. Pistons +3,5 (1,56).</strong> Hiervoor moet Detroit winnen of met maximaal drie punten verliezen. Een buffer voor een nipte thuiszege van Miami. Onze kansinschatting: ongeveer 65 procent, met een lager risico dan tip 1.</p>
<h3><strong>Heat – Pistons live kijken in Nederland</strong></h3>
<p>De makkelijkste manier om de wedstrijd te zien: bij <a href="/bookmakers/bet365">Bet365</a> kijk je NBA-wedstrijden gratis live. Je hebt alleen een account met een kleine storting nodig, die je daarna weer kunt opnemen. In Nederland heeft ESPN de NBA-rechten, maar niet elke wedstrijd staat op een van de Nederlandse ESPN-kanalen; check vooraf de programmering. Met <strong>NBA League Pass</strong>, de betaalde streamingdienst van de competitie, kun je ook alle wedstrijden volgen. Meer opties vind je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk Heat – Pistons live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Lees ook onze voorspellingen voor <a href="/nieuws/pistons-celtics-voorspelling-wedtips-nba-opening-2026">Pistons – Celtics</a>, <a href="/nieuws/76ers-cavaliers-voorspelling-wedtips-nba-2026">76ers – Cavaliers</a> en <a href="/nieuws/lakers-warriors-voorspelling-wedtips-nba-2026">Lakers – Warriors</a>, en ons overzicht van de <a href="/nieuws/nba-voorspellingen-vannacht-22-oktober-2026">NBA-voorspellingen van 22 oktober</a>. Lees ook <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">Welke Nederlanders spelen in de NBA</a>, <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels in de NBA</a> en <a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">de uitleg over de money line</a>. Alle basketbaltips vind je op onze pagina <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Heat – Pistons?</strong><br>Zaterdag 24 oktober 2026 om 02:00 Nederlandse tijd, in de nacht van vrijdag op zaterdag. In Miami is het dan vrijdagavond 20:00.</p>
<p><strong>Waar wordt Heat – Pistons gespeeld?</strong><br>In het Kaseya Center in Miami. De Heat zijn de thuisploeg.</p>
<p><strong>Hoe kwam Giannis Antetokounmpo bij Miami terecht?</strong><br>Via een ruil met Milwaukee, die op 22 juni werd afgesproken en op 6 juli officieel werd. Miami leverde onder meer Tyler Herro en meerdere draftpicks in; Bobby Portis kwam mee.</p>
<p><strong>Wie is favoriet: Heat of Pistons?</strong><br>Niemand. Bij TOTO staan beide ploegen op 1,91. In de handicapmarkt is Miami heel licht favoriet (-1,5).</p>
<p><strong>Hoe ging het vorig seizoen tussen deze ploegen?</strong><br>Miami won twee van de drie onderlinge duels (118-112 in Detroit en 121-110 in Miami). Detroit won in november met 138-135 in Miami.</p>
<p><strong>Wat is onze voorspelling voor Heat – Pistons?</strong><br>Detroit wint met 116-110. Onze hoofdtip is een zege van de Pistons (1,91 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

KAART = {"home": "Heat", "away": "Pistons", "home_abbr": "mia", "away_abbr": "det", "home_pos": "43-39 · nr. 10 Oost 2025/26", "away_pos": "60-22 · nr. 1 Oost 2025/26", "hs": 110, "as": 116, "datum": "Za 24 okt", "tijd": "02:00", "odd_home": "1,91", "odd_away": "1,91"}
WEDTIPS = {"wedtip-1-2": "Detroit Pistons wint (incl. verlenging)", "quotering-wedtip-1": "1.91",
           "wedtip-2-2": "Minder dan 236,5 punten (incl. verlenging)", "quotering-wedtip-2": "1.87",
           "wedtip-3-2": "Detroit Pistons +3,5 punten (incl. verlenging)", "quotering-wedtip-3": "1.56",
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
