# -*- coding: utf-8 -*-
"""Los artikel: Heat – Mavericks voorspelling, NBA 27 oktober 2026 (00:30 NL, wintertijd), Kaseya Center Miami.
Feiten nagelopen op 26-10-2026 (ESPN-API: summary 401909871, boxscores 401909091, 401909847, 401909853, 401909840,
401909844 en 401909858, teamschema's 2025/26 en 2026/27, rosters en coaches, spelersgemiddelden, onderlinge duels
2025/26 (401810141, 401810187); officiële NBA-blessurelijst 26-10 07:00 ET (12:00 NL); berichtgeving over de
Giannis-ruil (akkoord 22-6-2026, officieel 6-7-2026) en de wedstrijdverslagen van 23, 24 en 25 oktober).
- Heat: 106-131 tegen Minnesota, 111-128 tegen Detroit (geen moment voorgestaan), 110-115 in Charlotte (back-to-back,
  Giannis 14 punten en eruit met zes fouten; Miami kwam terug van 70-92 tot 104-104). Zondag rust.
- Mavericks: 110-128 in Houston, 121-105 in Indianapolis, 106-122 thuis tegen San Antonio op zaterdag (US) zonder Flagg
  en Irving (tweede avond van een back-to-back). Zondag rust: vannacht is GEEN back-to-back voor Dallas.
- Officiële lijst: Flagg twijfelachtig (schouder), Martin onwaarschijnlijk, Marshall, Lively, Aldama, Biberović out.
- Onderling 2025/26: 106-102 Heat in Miami (november), 118-108 Mavericks in Dallas (december).
- Odds: alleen TOTO, uit specials/nba_feiten_2026_10_27.md (±12:45 NL op 26-10). Handicap en totaal incl. verlenging.
- Eén wedtip (eis eigenaar): Heat -7,5 @1,73, onze kans 61% (markt 57,8%, zonder marge ±53%).
  python3 specials/heat_mavericks_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "Heat – Mavericks voorspelling: wedtip en odds voor Giannis' jacht op de eerste zege (27 oktober, 00:30)"
SLUG = "heat-mavericks-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("Miami wacht met Giannis Antetokounmpo nog op de eerste zege en ontvangt een gehavend Dallas. "
                "Voorspelling, onze wedtip, TOTO-odds, blessures en opstellingen.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet-experts.nl/go/bet365"
DATUM = "2026-10-26T23:30:00.000Z"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>In de nacht van maandag op dinsdag om 00:30 Nederlandse tijd jaagt Miami op zijn eerste zege van het seizoen. Met Giannis Antetokounmpo in de ploeg begon de Heat met drie nederlagen. Tegenstander Dallas komt naar Miami met een lange blessurelijst: Naji Marshall, Dereck Lively II en Santi Aldama spelen niet en achter Cooper Flagg staat een vraagteken. Onze voorspelling: Heat – Mavericks 124-112. Onze wedtip: Miami Heat -7,5 punten (inclusief verlenging) tegen een quotering van 1,73 bij TOTO.</strong></p>
<p>Hieronder lees je alles over vorm, blessures, de odds van <a href="/bookmakers/toto">TOTO</a> en onze onderbouwing.</p>
<h3><strong>Heat – Mavericks: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "Miami Heat – Dallas Mavericks"),
    ("Datum", "Dinsdag 27 oktober 2026 (nacht van maandag op dinsdag)"),
    ("Aanvang", "00:30 Nederlandse tijd (maandag 19:30 in Miami)"),
    ("Arena", "Kaseya Center, Miami"),
    ("Competitie", "NBA, reguliere competitie 2026/27"),
    ("Stand 2026/27", "Heat 0-3, Mavericks 1-2"),
    ("Onderlinge duels 2025/26", "1-1"),
])}
<p>Beide ploegen speelden vrijdag en zaterdag en hadden zondag rust. Voor geen van beide teams is dit dus een back-to-back.</p>
<h3><strong>De eerste week: Miami zoekt, Dallas mist zijn sterren</strong></h3>
<p><strong>Miami Heat: drie nederlagen, veel tegenpunten</strong></p>
<p>Miami opende met een 106-131 nederlaag tegen Minnesota. Antetokounmpo scoorde 35 punten (13 van de 19 schoten raak), maar de Heat maakten maar 8 van hun 33 driepunters. Vrijdag volgde een 111-128 nederlaag tegen Detroit, waarin Miami geen moment voorstond. Antetokounmpo had 36 punten en 12 rebounds, maar Bam Adebayo kwam in foutenproblemen (4 punten) en Klay Thompson miste 9 van zijn 11 schoten. Na twee duels had Miami 259 punten tegen gekregen, het slechtste begin in de clubgeschiedenis.</p>
<p>Zaterdag, op de tweede avond van een back-to-back, verloor de ploeg van coach Erik Spoelstra met 110-115 in Charlotte. Antetokounmpo bleef steken op 14 punten en moest met zes persoonlijke fouten naar de kant. Toch kwam Miami terug van 70-92 tot 104-104, met Davion Mitchell (22 punten, 10 assists) en Adebayo (20 punten) als drijvende krachten. In de slotminuten trok Charlotte de wedstrijd alsnog naar zich toe.</p>
<p><strong>Dallas Mavericks: één zege, en zaterdag zonder Flagg en Irving</strong></p>
<p>Dallas verloor in Houston met 110-128, ondanks 32 punten van Flagg. Vrijdag won de ploeg van de nieuwe coach Dusty May overtuigend met 121-105 in Indianapolis: Kyrie Irving maakte 24 punten in 25 minuten, P.J. Washington 20 punten en 13 rebounds. Flagg viel in die wedstrijd hard op zijn linkerschouder. Zaterdag speelde Dallas thuis tegen San Antonio zonder Flagg en zonder Irving, die op de tweede avond van de back-to-back rust kreeg. Het werd 106-122. Rookie Sergio de Larrea was met 21 punten topscorer, de vijf basisspelers maakten samen maar 50 punten.</p>
<h3><strong>Vorig seizoen en de onderlinge duels</strong></h3>
<p>Miami eindigde op 43-39 als tiende in het Oosten en ging in de play-in na verlenging met 126-127 onderuit in Charlotte. Dallas speelde het hele seizoen zonder Irving, deed in februari Anthony Davis van de hand en werd twaalfde in het Westen. Flagg werd wel Rookie of the Year.</p>
{tabel(["2025/26", "Miami Heat", "Dallas Mavericks"], [
    ("Eindstand", "43-39 (nr. 10 Oost)", "26-56 (nr. 12 West)"),
    ("Thuis / uit", "26-15 / 17-24", "16-25 / 10-31"),
    ("Punten voor / tegen", "120,9 / 118,5", "114,1 / 119,6"),
    ("Na het seizoen", "Uitgeschakeld in de play-in", "Play-offs niet gehaald"),
])}
<p>Gemiddelden per wedstrijd in de reguliere competitie. De onderlinge duels waren spannend: Miami won in november thuis met 106-102, Dallas won in december met 118-108. Veel uitblinkers van toen zijn weg: Tyler Herro (24 en 20 punten) en Kel'el Ware (20 en 22) spelen nu in Milwaukee. Klay Thompson stond toen nog aan de kant van Dallas.</p>"""

content2 = f"""<h3><strong>Zo zijn beide selecties veranderd</strong></h3>
<p><strong>Miami Heat: Giannis erbij, Herro weg</strong></p>
<p>Op 22 juni werden Miami en Milwaukee het eens over de grootste ruil van de zomer; op 6 juli werd die officieel. Antetokounmpo en Bobby Portis gingen naar Miami. Milwaukee kreeg Herro, Ware, Jaime Jaquez jr. en Kasparas Jakučionis, de nummer 13 van de draft van 2026, eerste-ronde-keuzes in 2031 en 2033, een ruil van keuzes in 2030 en een tweede-ronde-keuze in 2033. Norman Powell vertrok naar Chicago; Klay Thompson kwam over van Dallas en Tim Hardaway jr. van Denver.</p>
<p><strong>Dallas Mavericks: nieuwe coach, Irving terug</strong></p>
<p>Jason Kidd vertrok als coach, Dusty May volgde hem op. Dallas koos Morez Johnson jr. als nummer negen in de draft en haalde via ruilen Aldama, Marcus Sasser en Zaccharie Risacher binnen. Khris Middleton vertrok naar Washington, Thompson naar Miami. Irving speelt weer na negentien maanden herstel van een gescheurde kruisband.</p>
<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("Cooper Flagg", "Dallas", "Twijfelachtig (verstuikte linkerschouder)"),
    ("Caleb Martin", "Dallas", "Onwaarschijnlijk (verstuikte rechterduim)"),
    ("Naji Marshall", "Dallas", "Speelt niet (ziek)"),
    ("Dereck Lively II", "Dallas", "Speelt niet (voetoperatie)"),
    ("Santi Aldama", "Dallas", "Speelt niet (knieoperatie)"),
    ("Tarik Biberović", "Dallas", "Speelt niet (ontstoken slijmbeurs in de hiel)"),
    ("Pelle Larsson", "Miami", "Inzetbaar (verstuikte vinger)"),
])}
<p><em>Stand van de officiële NBA-blessurelijst op maandag 26 oktober, 12:00 Nederlandse tijd. Irving staat er niet op en is dus inzetbaar.</em></p>
<p><strong>Verwachte basisvijf Heat:</strong> Davion Mitchell, Klay Thompson, Andrew Wiggins, Giannis Antetokounmpo, Bam Adebayo. Dat was de vijf in alle drie de wedstrijden. Bobby Portis, Tim Hardaway jr., Pelle Larsson en Nikola Jović zijn de belangrijkste wissels.</p>
<p><strong>Verwachte basisvijf Mavericks:</strong> Kyrie Irving, Max Christie, Zaccharie Risacher, P.J. Washington, Daniel Gafford. Speelt Flagg, dan neemt hij waarschijnlijk de plek van Risacher in. Sasser, De Larrea en Johnson komen als eersten van de bank.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "2026/27 tot nu toe"], [
    ("Giannis Antetokounmpo (MIA)", "27,6", "9,8", "5,4", "28,3 ptn, 8,0 reb"),
    ("Bam Adebayo (MIA)", "20,1", "10,0", "3,2", "13,0 ptn, 7,0 reb"),
    ("Davion Mitchell (MIA)", "9,3", "2,7", "6,5", "17,0 ptn, 8,7 ast"),
    ("Kyrie Irving (DAL)", "24,7*", "4,8*", "4,6*", "19,5 ptn in 24,5 minuten"),
    ("P.J. Washington (DAL)", "14,2", "7,0", "1,8", "14,0 ptn, 7,0 reb"),
    ("Cooper Flagg (DAL)", "21,0", "6,7", "4,5", "23,0 ptn; twijfelachtig"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26. Antetokounmpo speelde dat seizoen 36 duels, voor Milwaukee. * Irving speelde in 2025/26 niet; bij hem staan de cijfers van 2024/25.</em></p>
<p><strong>Giannis Antetokounmpo</strong> scoort zoals verwacht, maar de rest van Miami moet meer doen. Tegen een Dallas zonder Lively en Aldama krijgt hij ruimte onder de ring, zolang hij uit de foutenproblemen blijft. <strong>Davion Mitchell</strong> is de verrassing van de eerste week: hij verdubbelde zijn scoringsgemiddelde bijna en deelt bijna negen assists per wedstrijd uit. Bij Dallas draait alles om <strong>Kyrie Irving</strong>, die na een rustdag fris is, maar tot nu toe niet langer dan 25 minuten per wedstrijd speelde.</p>
<h3><strong>Odds Heat – Mavericks bij TOTO</strong></h3>
<p>TOTO ziet Miami ondanks de 0-3 als duidelijke favoriet: een quotering van 1,30 staat voor ongeveer 77 procent winkans. De handicap ligt rond de 8,5 punten in het voordeel van de Heat, het verwachte puntentotaal tussen 236,5 en 237,5.</p>
{tabel(["Markt (TOTO)", "Heat", "Mavericks"], [
    ("Winnaar (incl. verlenging)", "1,30", "3,65"),
    ("1X2 (reguliere speeltijd, gelijk 18,00)", "1,29", "3,85"),
    ("Handicap -6,5 / +6,5 (incl. verlenging)", "1,63", "2,10"),
    ("Handicap -7,5 / +7,5 (incl. verlenging)", "1,73", "1,93"),
    ("Handicap -8,5 / +8,5 (incl. verlenging)", "1,95", "1,87"),
    ("Handicap -9,5 / +9,5 (incl. verlenging)", "2,00", "1,69"),
    ("Handicap -10,5 / +10,5 (incl. verlenging)", "2,20", "1,59"),
])}
<p>Op het totaal biedt TOTO 235,5 punten (Over 1,65 / Under 2,05), 236,5 (1,73 / 1,95) en 237,5 (1,87 / 1,93). Odds gelezen op maandag rond 12:45 uur; vergelijk ze vlak voor de start nog even, zeker als duidelijk wordt of Flagg speelt.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op Heat – Mavericks</strong></a></p>"""

content3 = f"""<h3><strong>Onze voorspelling: de eerste zege voor Miami</strong></h3>
<p>De 0-3 oogt slecht, maar de tegenstanders waren sterk. Minnesota won al zijn drie wedstrijden, Detroit was vorig seizoen de beste ploeg van het Oosten en in Charlotte speelde Miami op de tweede avond van een back-to-back, met Antetokounmpo vroeg in foutenproblemen. Ook toen kwam de ploeg nog terug van 22 punten achterstand.</p>
<p>Dallas is een ander verhaal. Marshall, Lively, Aldama en waarschijnlijk Martin ontbreken, en of Flagg na zijn val in Indianapolis kan spelen, is onzeker. Irving is terug na een rustdag, maar speelt nog beperkte minuten. Zaterdag lieten de Spurs zien hoe kwetsbaar Dallas onder de ring is. Miami heeft met Antetokounmpo, Adebayo en Portis precies de spelers om dat uit te buiten. Onze voorspelling: <strong>Miami Heat – Dallas Mavericks 124-112</strong>.</p>
<h3><strong>Onze wedtip: Heat -7,5 (1,73)</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Onze kans"], [
    ("Miami Heat -7,5 punten (incl. verlenging)", "1,73", "TOTO", "Ongeveer 61 procent"),
])}
<p><strong>Waarom deze tip?</strong> De tip is goed als Miami met minstens acht punten verschil wint. Een odd van 1,73 staat voor een kans van 58 procent; zonder de marge van de bookmaker is dat ongeveer 53 procent. Wij schatten de kans op ongeveer 61 procent. De onderbouwing:</p>
<p><strong>1. Dallas mist te veel.</strong> Met Marshall (13,7 punten en 5,7 assists dit seizoen) valt een vaste waarde weg, Lively en Aldama zijn al langer uit de roulatie. Zaterdag, zonder Flagg en Irving, kwamen de vijf basisspelers samen niet verder dan 50 punten. Zelfs als Flagg speelt, is het zijn eerste wedstrijd na een verstuikte schouder.</p>
<p><strong>2. Thuis tegen uit.</strong> Miami won vorig seizoen 26 van zijn 41 thuisduels, Dallas won er buiten de deur maar 10. Na een rustdag speelt Miami weer in eigen huis.</p>
<p><strong>3. Lengte en balverlies.</strong> San Antonio pakte zaterdag 15 aanvallende rebounds tegen Dallas, en de Mavericks verloren in hun drie duels gemiddeld 19 keer de bal. Met Antetokounmpo en Adebayo heeft Miami twee spelers die van dat soort fouten leven.</p>
<p><strong>Waarom niet een andere markt?</strong> Een zege van Miami (1,30) schatten wij op ongeveer 80 procent. Dat is nauwelijks meer dan de odd aangeeft, en de opbrengst is klein. Bij Heat -8,5 (1,95), -9,5 (2,00) en -10,5 (2,20) krijg je meer, maar onze voorspelde marge van twaalf punten ligt daar te dicht tegenaan. Bij -7,5 heb je een buffer van vier punten. Het puntentotaal laten we liggen: onze voorspelling komt uit op 236 punten, precies rond de lijn van TOTO.</p>
<p><strong>Het risico.</strong> Miami kreeg dit seizoen gemiddeld bijna 125 punten tegen en raakte maar 30 procent van zijn driepunters. Irving kan op een goede avond een wedstrijd alleen openbreken, en als Flagg toch speelt, is Dallas een stuk sterker. Let ook op: de handicap telt een eventuele verlenging mee. Meer uitleg vind je in onze gidsen over <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap wedden</a> en de <a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">money line</a>.</p>
<h3><strong>Heat – Mavericks live kijken in Nederland</strong></h3>
<p>Bij <a href="/bookmakers/bet365">Bet365</a> kun je NBA-wedstrijden live volgen via de livestream. Je hebt daarvoor een account met een storting nodig. ESPN zendt in Nederland een deel van de NBA-wedstrijden uit; in de programmagids zie je of deze erbij zit. Met <strong>NBA League Pass</strong>, de betaalde dienst van de competitie, kun je alle wedstrijden volgen. Meer opties vind je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk Heat – Mavericks live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Lees ook onze voorspellingen voor <a href="/nieuws/cavaliers-timberwolves-voorspelling-wedtips-nba-2026">Cavaliers – Timberwolves</a>, <a href="/nieuws/thunder-suns-voorspelling-wedtips-nba-2026">Thunder – Suns</a> en <a href="/nieuws/rockets-hawks-voorspelling-wedtips-nba-2026">Rockets – Hawks</a>, en de <a href="/nieuws/nba-voorspellingen-vannacht-27-oktober-2026">NBA-voorspellingen van 27 oktober</a>. Benieuwd <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">welke Nederlanders in de NBA spelen</a>? Nieuw met basketbal? Lees <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels in de NBA</a>. Alle tips staan op <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Heat – Mavericks?</strong><br>Dinsdag 27 oktober 2026 om 00:30 Nederlandse tijd, in de nacht van maandag op dinsdag. In Miami is het dan maandagavond 19:30.</p>
<p><strong>Speelt Cooper Flagg mee?</strong><br>Dat is onzeker. Flagg staat als twijfelachtig op de officiële blessurelijst, met een verstuikte linkerschouder. Hij viel vrijdag in Indianapolis hard en miste zaterdag de wedstrijd tegen San Antonio. Kyrie Irving staat niet op de lijst en speelt dus mee.</p>
<p><strong>Wie is favoriet: Heat of Mavericks?</strong><br>Miami, met een quotering van 1,30 bij TOTO. Dallas staat op 3,65.</p>
<p><strong>Wat is onze voorspelling voor Heat – Mavericks?</strong><br>Miami wint met 124-112. Onze wedtip is Miami Heat -7,5 punten, inclusief verlenging (1,73 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

KAART = {"home": "Heat", "away": "Mavericks", "home_abbr": "mia", "away_abbr": "dal", "home_pos": "43-39 · nr. 10 Oost 2025/26", "away_pos": "26-56 · nr. 12 West 2025/26", "hs": 124, "as": 112, "datum": "Di 27 okt", "tijd": "00:30", "odd_home": "1,30", "odd_away": "3,65"}
WEDTIPS = {"wedtip-1-2": "Miami Heat -7,5 punten (incl. verlenging)", "quotering-wedtip-1": "1.73",
           "bookmaker-wedtips": "669ab9f5aceb8b717cea24c3"}

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_BASKETBAL, "competitie": COMPETITIE_NBA,
          "datum-tijd-van-wedstrijd": DATUM,
          "publicatiedatum": datetime.now(timezone.utc).isoformat(), **WEDTIPS}
    # Alleen dry run: dit script publiceert niets.
    import re
    html = content + content2 + content3
    # Opmaak
    assert not re.search(r"<h[1245]", html), "alleen h3 gebruiken"
    assert all(m.startswith("<h3><strong>") for m in re.findall(r"<h3>.{0,8}", html)), "h3 altijd met strong"
    assert content.startswith("<p><strong>"), "vetgedrukte intro"
    assert not re.search(r"<(ul|ol|li)\b", html) or not re.search(r"(</?(ul|ol|li)>)\s+(?=<)", html), "witruimte in lijsten"
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"), "slotregel"
    hrefs = re.findall(r'href="([^"]+)"', html)
    assert hrefs and all(h.startswith("/") or h == BET365 for h in hrefs), [h for h in hrefs if not h.startswith("/")]
    toegestaan = {"/nieuws/nba-voorspellingen-vannacht-27-oktober-2026", "/nieuws/nba-voorspellingen-vannacht-26-oktober-2026",
                  "/nieuws/nba-voorspellingen-vannacht-25-oktober-2026", "/nieuws/nba-voorspellingen-vannacht-24-oktober-2026",
                  "/nieuws/thunder-clippers-voorspelling-wedtips-nba-2026", "/nieuws/jazz-lakers-voorspelling-wedtips-nba-2026",
                  "/nieuws/76ers-pistons-voorspelling-wedtips-nba-2026", "/nieuws/hawks-rockets-voorspelling-wedtips-nba-2026",
                  "/nieuws/thunder-nuggets-voorspelling-wedtips-nba-2026", "/nieuws/lakers-warriors-voorspelling-wedtips-nba-2026",
                  "/nieuws/76ers-cavaliers-voorspelling-wedtips-nba-2026",
                  "/nieuws/cavaliers-timberwolves-voorspelling-wedtips-nba-2026",
                  "/nieuws/thunder-suns-voorspelling-wedtips-nba-2026", "/nieuws/rockets-hawks-voorspelling-wedtips-nba-2026",
                  "/nieuws/nuggets-warriors-voorspelling-wedtips-nba-2026",
                  "/nieuws/welke-nederlanders-spelen-in-de-nba",
                  "/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders",
                  "/nieuws/wat-is-handicap-wedden-de-complete-gids",
                  "/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners",
                  "/wedden-op-nba-voorspellingen-en-wedtips---basketbal", "/bookmakers/toto", "/bookmakers/bet365",
                  "/live-kijken", BET365}
    assert set(hrefs) <= toegestaan, set(hrefs) - toegestaan
    vannacht = {h for h in hrefs if h.endswith("-voorspelling-wedtips-nba-2026") and h.split("/")[-1].split("-voorspelling")[0]
                in ("cavaliers-timberwolves", "thunder-suns", "rockets-hawks", "nuggets-warriors")}
    assert 2 <= len(vannacht) <= 4, vannacht
    assert "/nieuws/nba-voorspellingen-vannacht-27-oktober-2026" in hrefs
    assert hrefs.count(BET365) == 2
    assert "<table" not in html.replace(f"<table {T}>", ""), "tabellen alleen via tabel()"
    verboden = ["BetCity", "ESPN-API", "ESPN.com", "Associated Press", "DraftKings", "Rotowire", "Betfans", "Elias", " AP "]
    assert not any(v.lower() in html.lower() for v in verboden), "geen bronnen/concurrenten"
    assert "back-to-back" not in html.lower().replace("geen van beide teams is dit dus een back-to-back", "").replace(
        "tweede avond van een back-to-back", "").replace("tweede avond van de back-to-back", ""), "Dallas speelt geen back-to-back"
    # Wedtip en consistentie
    assert set(WEDTIPS) == {"wedtip-1-2", "quotering-wedtip-1", "bookmaker-wedtips"}
    assert WEDTIPS["bookmaker-wedtips"] == "669ab9f5aceb8b717cea24c3"
    q = float(WEDTIPS["quotering-wedtip-1"])
    toto_odds = {1.30, 3.65, 1.29, 18.0, 3.85, 2.20, 1.59, 2.00, 1.69, 1.95, 1.87, 1.73, 1.93, 1.63, 2.10,
                 1.65, 2.05, 1.91, 1.78, 1.98, 1.71}
    assert q == 1.73 and q in toto_odds
    assert KAART["hs"] - 7.5 > KAART["as"], "voorspelde score moet Heat -7,5 laten winnen"
    assert KAART["hs"] > KAART["as"], "voorspelling: Heat winnen"
    assert f"{KAART['hs']}-{KAART['as']}" in content and f"{KAART['hs']}-{KAART['as']}" in content3
    assert KAART["odd_home"] == "1,30" and KAART["odd_away"] == "3,65" and KAART["tijd"] == "00:30"
    assert KAART["home_abbr"] == "mia" and KAART["away_abbr"] == "dal" and KAART["datum"] == "Di 27 okt"
    assert "1,73" in content and "1,73" in content3 and "Heat -7,5" in content3
    assert html.count("Veelgestelde vragen") == 1 and content3.count("<br>") == 4, "4 FAQ-vragen"
    assert all(f"<p><strong>{i}. " in content3 for i in (1, 2, 3)) and "Waarom niet een andere markt?" in content3
    assert "maandag rond 12:45 uur" in content2
    assert SLUG == "heat-mavericks-voorspelling-wedtips-nba-2026" and DATUM == "2026-10-26T23:30:00.000Z"
    tekst = re.sub(r"<[^>]+>", " ", html)
    print(len(TITEL), "tekens titel |", len(SAMENVATTING), "tekens samenvatting |", len(tekst.split()), "woorden")
    print("Alle asserts geslaagd (dry run, niets gepubliceerd).")
