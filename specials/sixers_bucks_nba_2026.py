# -*- coding: utf-8 -*-
"""Los artikel: 76ers – Bucks voorspelling, NBA 25 oktober 2026 (01:30 NL, zaterdag 19:30 ET). Feiten nagelopen op 24-10-2026
(ESPN-API: summary 401909855 en boxscores 401909089, 401909835, 401909093, 401909848; standen en onderlinge duels 2025/26
(401810121, 401810203, 401810521, 401811046); officiele NBA-blessurelijst 24-10 06:45 ET; berichtgeving over de ruil
Antetokounmpo-Heat (juni 2026) en over Embiid/James en de back-to-back (23-10)).
- 76ers: 106-100 in New York (Maxey 28), 114-106 tegen Cleveland na 29 punten achterstand (Maxey 32, Embiid 24, Brown 21, James 17/10).
- Bucks: 116-128 in Washington (Herro 24, Jaquez 22); 125-132 thuis tegen Chicago (Herro 34, Jaquez 19/11). Die wedstrijd werd
  vier uur vervroegd (15:00 lokale tijd) vanwege World Series-duel 1 van de Brewers. Dus GEEN uitwedstrijd in Chicago.
- Blessurelijst 24-10 06:45 ET: PHI James (low back/sciatica management) en Wade (enkel) twijfelachtig; Barlow, Fall, Hukporti out.
  Bucks: nog niets ingediend (ook vrijdag geen namen). Embiid niet op de lijst, maar speelt maar een van de twee duels (za MIL / zo DET).
- Onderling 2025/26: 4-0 PHI (123-114, 116-101, 139-122, 126-106), Giannis speelde in geen van de vier.
- Odds: alleen TOTO, uit specials/nba_feiten_2026_10_25.md (±12:50 NL op 24-10). De regel 234,5 (O 1,87 / U 1,78) is weggelaten (onlogisch t.o.v. 233,5).
  ../superodd-agent/.venv/bin/python specials/sixers_bucks_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "76ers – Bucks voorspelling: onze wedtip en odds, Philadelphia zwaar favoriet (25 oktober, 01:30)"
SLUG = "76ers-bucks-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("Philadelphia (2-0) ontvangt het nieuwe Milwaukee zonder Giannis. Voorspelling, onze wedtip, TOTO-odds, "
                "blessures en de status van LeBron James.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet-experts.nl/go/bet365"
DATUM = "2026-10-24T23:30:00.000Z"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>In de nacht van zaterdag op zondag om 01:30 Nederlandse tijd ontvangen de Philadelphia 76ers de Milwaukee Bucks. Philadelphia won zijn eerste twee wedstrijden, Milwaukee verloor er twee en speelde vrijdag nog. De bookmakers maken van de 76ers een zware favoriet, maar achter LeBron James en Joel Embiid staat een vraagteken. Onze voorspelling: de 76ers winnen met 121-112. Onze wedtip: Milwaukee Bucks +12,5 punten (1,91 bij TOTO).</strong></p>
<p>Milwaukee begint opnieuw: Giannis Antetokounmpo speelt sinds de zomer voor Miami. Philadelphia heeft met Tyrese Maxey, Jaylen Brown, James en Embiid juist een van de sterkste basisvijven van het Oosten. Hieronder lees je wie er speelt, wat <a href="/bookmakers/toto">TOTO</a> verwacht en waarom wij toch op de underdog wedden.</p>
<h3><strong>76ers – Bucks: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "Philadelphia 76ers – Milwaukee Bucks"),
    ("Datum", "Zondag 25 oktober 2026 (nacht van zaterdag op zondag)"),
    ("Aanvang", "01:30 Nederlandse tijd (zaterdag 19:30 in Philadelphia)"),
    ("Arena", "Xfinity Mobile Arena, Philadelphia"),
    ("Competitie", "NBA, reguliere competitie 2026/27"),
    ("Stand 2026/27", "76ers 2-0, Bucks 0-2"),
    ("Onderlinge duels 2025/26", "4-0 voor de 76ers"),
])}
<p>De wedstrijd begint vóór de overgang naar de wintertijd. Voor beide ploegen hoort deze wedstrijd bij een back-to-back. Milwaukee speelde vrijdag, Philadelphia speelt zondag alweer thuis tegen Detroit.</p>
<h3><strong>Seizoen tot nu toe: 76ers 2-0, Bucks 0-2</strong></h3>
<p>Philadelphia opende met een 100-106 zege bij kampioen New York (Maxey 28 punten). Tegen Cleveland stond de ploeg donderdag met 29 punten achter. Met een 15-0 run in het vierde kwart won Philadelphia toch nog met 114-106. Maxey scoorde 32 punten, Embiid 24 en Brown 21; James kwam tot 17 punten en 10 rebounds. Opvallend: de 76ers raakten in twee wedstrijden maar 18 van hun 68 driepunters (26,5 procent).</p>
<p>Milwaukee begon woensdag met een 128-116 nederlaag in Washington. De Bucks stonden lang voor, maar zakten in het vierde kwart weg tegen Anthony Davis (34 punten). Herro scoorde 24 punten, Jaquez 22. Vrijdag verloor Milwaukee thuis met 125-132 van Chicago. Die wedstrijd werd vier uur vervroegd naar de middag, omdat de Milwaukee Brewers 's avonds in de World Series speelden. Herro maakte 34 punten, Jaquez had 19 punten en 11 rebounds. Aanvallend draait het, maar Milwaukee kreeg in twee wedstrijden 260 punten tegen.</p>
<h3><strong>Vorig seizoen: 76ers in de play-offs, Bucks er voor het eerst sinds 2016 naast</strong></h3>
<p>Philadelphia eindigde in 2025/26 op 45-37, overleefde de play-in en de eerste ronde, en verloor in de tweede ronde met 0-4 van New York. Milwaukee won maar 32 van de 82 wedstrijden en miste voor het eerst sinds 2015/16 de play-offs. Antetokounmpo speelde maar 36 wedstrijden. Doc Rivers stapte op; nieuwe coach is Taylor Jenkins, eerder bij Memphis.</p>
{tabel(["2025/26", "Philadelphia 76ers", "Milwaukee Bucks"], [
    ("Eindstand", "45-37 (nr. 7 Oost)", "32-50 (nr. 11 Oost)"),
    ("Thuis / uit", "23-18 / 22-19", "19-22 / 13-28"),
    ("Punten voor / tegen", "115,9 / 116,1", "110,6 / 116,8"),
    ("Onderling", "4-0", "0-4"),
    ("Na het seizoen", "Tweede ronde (0-4 tegen New York)", "Geen play-offs"),
])}
<p>Philadelphia won de vier onderlinge duels met 123-114, 116-101, 139-122 en 126-106. Antetokounmpo speelde in geen van die wedstrijden mee, Embiid maar in één. In november 2025 scoorde Maxey in Milwaukee 54 punten.</p>"""

content2 = f"""<h3><strong>Selecties en blessures</strong></h3>
<p><strong>Milwaukee Bucks: een nieuwe ploeg rond Herro</strong></p>
<p>Antetokounmpo en Bobby Portis gingen naar Miami. Daarvoor kreeg Milwaukee Tyler Herro, Jaime Jaquez Jr., Kel'el Ware, Kasparas Jakučionis en drie eerste-ronde-keuzes in de draft. Myles Turner, Kyle Kuzma en Ryan Rollins bleven. Ware, Jakučionis, AJ Green, Ousmane Dieng en rookie Brayden Burries zijn de belangrijkste wissels.</p>
<p><strong>Philadelphia 76ers: hoe gaat Nurse met zijn sterren om?</strong></p>
<p>James (41) staat als twijfelachtig op de blessurelijst vanwege ischiasklachten in zijn onderrug; de club wil zijn belasting beperken. Embiid staat niet op de lijst, maar zei zelf dat hij maar één van de twee wedstrijden van dit weekend speelt, en dat hij nog niet weet welke.</p>
{tabel(["Speler", "Team", "Status"], [
    ("LeBron James", "Philadelphia", "Twijfelachtig (onderrug, ischias)"),
    ("Dean Wade", "Philadelphia", "Twijfelachtig (linkerenkel)"),
    ("Dominick Barlow", "Philadelphia", "Speelt niet (onderrug)"),
    ("Tacko Fall", "Philadelphia", "Speelt niet (bovenbeen)"),
    ("Ariel Hukporti", "Philadelphia", "Speelt niet (achillespees)"),
    ("Milwaukee Bucks", "Milwaukee", "Nog geen blessures gemeld"),
])}
<p><em>Officiële NBA-blessurelijst van zaterdag 24 oktober, 12:45 Nederlandse tijd. Milwaukee had toen nog niets ingediend; vrijdag stond er geen Bucks-speler op.</em></p>
<p><strong>Verwachte basisvijf 76ers:</strong> Tyrese Maxey, VJ Edgecombe, Jaylen Brown, LeBron James, Joel Embiid. Speelt James niet, dan krijgen Kentavious Caldwell-Pope en Anfernee Simons meer minuten. Rust Embiid, dan is Adem Bona de logische center.</p>
<p><strong>Verwachte basisvijf Bucks:</strong> Tyler Herro, Ryan Rollins, Jaime Jaquez Jr., Kyle Kuzma, Myles Turner. Dezelfde vijf als in de eerste twee wedstrijden.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "Bijzonderheid"], [
    ("Tyrese Maxey (PHI)", "28,3", "4,1", "6,6", "30,0 punten per wedstrijd dit seizoen"),
    ("Jaylen Brown (PHI)", "28,7", "6,9", "5,1", "Cijfers bij Boston"),
    ("Joel Embiid (PHI)", "26,9", "7,7", "3,9", "Speelt maar één duel dit weekend"),
    ("LeBron James (PHI)", "20,9", "6,1", "7,2", "Cijfers bij de Lakers, twijfelachtig"),
    ("Tyler Herro (MIL)", "20,5", "4,8", "4,1", "Cijfers bij Miami (33 duels), nu 28,0 punten"),
    ("Jaime Jaquez Jr. (MIL)", "15,4", "5,0", "4,7", "Cijfers bij Miami, nu 20,5 punten"),
    ("Ryan Rollins (MIL)", "17,3", "4,6", "5,6", "40,6% driepunters vorig seizoen"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26, tenzij anders vermeld.</em></p>
<h3><strong>Odds 76ers – Bucks bij TOTO</strong></h3>
<p>Een quotering van 1,14 staat voor ongeveer 88 procent kans; zonder de marge van de bookmaker is dat zo'n 84 procent. De handicap ligt op 12,5 punten, het verwachte puntentotaal op 233,5.</p>
{tabel(["Markt", "76ers", "Bucks"], [
    ("Winnaar (incl. verlenging)", "1,14", "5,95"),
    ("1X2 (reguliere speeltijd, gelijk 22,00)", "1,11", "6,75"),
    ("Handicap -11,5 / +11,5", "1,71", "1,98"),
    ("Handicap -12,5 / +12,5", "1,91", "1,91"),
    ("Handicap -13,5 / +13,5", "1,98", "1,71"),
])}
<p>Op het totaal van 233,5 punten biedt TOTO Over 1,87 en Under 1,95. Odds gelezen op zaterdag rond 12:50 uur. Wordt bekend dat James of Embiid niet speelt, dan verschuiven de lijnen.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op 76ers – Bucks</strong></a></p>"""

content3 = f"""<h3><strong>Onze voorspelling: 76ers winnen, maar minder ruim dan verwacht</strong></h3>
<p>Waarom is Philadelphia zo'n grote favoriet? De 76ers spelen thuis, hebben veel meer sterren en wonnen vorig seizoen alle onderlinge duels met minstens negen punten verschil. Milwaukee bouwt opnieuw op, verdedigde zwak en speelde vrijdag al.</p>
<p>Toch verwachten we geen afgang. Philadelphia won zijn twee wedstrijden met zes en acht punten verschil, en Maxey speelde al 40 en 42 minuten. Met Detroit op zondag ligt het voor de hand dat coach Nick Nurse de belasting verdeelt. Milwaukee kan scoren: 116 en 125 punten in de eerste twee wedstrijden. Onze voorspelling: <strong>Philadelphia 76ers – Milwaukee Bucks 121-112</strong>.</p>
<h3><strong>Onze wedtip: Milwaukee Bucks +12,5 punten (1,91)</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Onze kans", "Kans volgens odds"], [
    ("Milwaukee Bucks +12,5 punten (incl. verlenging)", "1,91", "TOTO", "56%", "52%"),
])}
<p>Met deze weddenschap krijgt Milwaukee 12,5 punten voorsprong. Je wint als de Bucks winnen of met maximaal 12 punten verschil verliezen. Een quotering van 1,91 staat voor ruim 52 procent kans; wij schatten die kans op 56 procent. Om drie redenen:</p>
<p><strong>1. De sterren van Philadelphia krijgen mogelijk rust.</strong> James is twijfelachtig en Embiid speelt maar één van de twee wedstrijden dit weekend. Mist een van beiden de wedstrijd of speelt hij minder minuten, dan wordt een zege met dertien punten of meer lastiger. Spelen ze allebei, dan klopt de huidige lijn. De onzekerheid werkt dus in het voordeel van de Bucks.</p>
<p><strong>2. De 76ers winnen nog niet ruim.</strong> Philadelphia had in beide wedstrijden een slechte periode en leunt op een kleine bank: Caldwell-Pope, Simons, Bona en Jabari Walker zijn de enige vaste invallers. Juist in deze wedstrijd krijgen zij waarschijnlijk meer minuten.</p>
<p><strong>3. De vermoeidheid valt mee bij Milwaukee.</strong> De Bucks speelden vrijdag wel, maar 's middags en thuis, en hadden dus extra tijd om bij te komen en te reizen. Aanvallend loopt het met Herro en Jaquez.</p>
<p><strong>Het risico:</strong> de verdediging van Milwaukee. Washington en Chicago, vorig seizoen twee van de zwakste ploegen, scoorden 128 en 132 punten. Valt het schot van Philadelphia (tot nu toe 26,5 procent driepunters) vannacht wel en spelen James en Embiid allebei, dan kan de wedstrijd vroeg uit de hand lopen. Kies daarom geen grote inzet.</p>
<p>Waarom geen andere tip? Een zege van Philadelphia (1,14) levert te weinig op. Op het puntentotaal zien we geen duidelijke kant: de wedstrijden van Milwaukee gingen ruim over 233,5, die van Philadelphia ruim eronder.</p>
<h3><strong>76ers – Bucks live kijken in Nederland</strong></h3>
<p>De makkelijkste manier: bij <a href="/bookmakers/bet365">Bet365</a> kijk je NBA-wedstrijden gratis live. Je hebt alleen een account met een kleine storting nodig, die je daarna weer kunt opnemen. ESPN heeft in Nederland de NBA-rechten, maar zendt maar een deel van de wedstrijden uit; check vooraf de gids. Met <strong>NBA League Pass</strong>, de betaalde streamingdienst van de competitie, volg je alle wedstrijden. Meer opties vind je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk 76ers – Bucks live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Lees ook onze voorspellingen voor <a href="/nieuws/76ers-cavaliers-voorspelling-wedtips-nba-2026">76ers – Cavaliers</a>, <a href="/nieuws/spurs-rockets-voorspelling-wedtips-nba-2026">Spurs – Rockets</a> en <a href="/nieuws/pacers-mavericks-voorspelling-wedtips-nba-2026">Pacers – Mavericks</a>, en de <a href="/nieuws/nba-voorspellingen-vannacht-24-oktober-2026">NBA-voorspellingen van 24 oktober</a>. Nieuw met wedden op basketbal? Lees <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels in de NBA</a> en <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">wat handicap wedden is</a>. Alle basketbaltips vind je op <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint 76ers – Bucks?</strong><br>Zondag 25 oktober 2026 om 01:30 Nederlandse tijd, in de nacht van zaterdag op zondag en nog vóór de overgang naar de wintertijd. In Philadelphia is het dan 19:30.</p>
<p><strong>Speelt LeBron James mee?</strong><br>Dat is nog niet zeker. James staat als twijfelachtig op de blessurelijst vanwege zijn onderrug (ischias). Philadelphia wil zijn belasting beperken en speelt zondag ook nog tegen Detroit.</p>
<p><strong>Speelt Joel Embiid mee?</strong><br>Embiid staat niet op de blessurelijst, maar speelt dit weekend maar één van de twee wedstrijden. Welke dat is, maakt de club pas later bekend.</p>
<p><strong>Waar speelt Giannis Antetokounmpo nu?</strong><br>Bij de Miami Heat. Milwaukee ruilde hem deze zomer, samen met Bobby Portis, voor Tyler Herro, Jaime Jaquez Jr., Kel'el Ware, Kasparas Jakučionis en draftkeuzes.</p>
<p><strong>Wat is onze voorspelling en wedtip voor 76ers – Bucks?</strong><br>De 76ers winnen met 121-112. Onze wedtip is Milwaukee Bucks +12,5 punten (1,91 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

KAART = {"home": "76ers", "away": "Bucks", "home_abbr": "phi", "away_abbr": "mil", "home_pos": "45-37 · nr. 7 Oost 2025/26", "away_pos": "32-50 · nr. 11 Oost 2025/26", "hs": 121, "as": 112, "datum": "Zo 25 okt", "tijd": "01:30", "odd_home": "1,14", "odd_away": "5,95"}
WEDTIPS = {"wedtip-1-2": "Milwaukee Bucks +12,5 punten (incl. verlenging)", "quotering-wedtip-1": "1.91",
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
