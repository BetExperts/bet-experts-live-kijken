# -*- coding: utf-8 -*-
"""Los artikel: Celtics – Nets voorspelling, NBA 28 oktober 2026 (00:30 NL, wintertijd; dinsdag 19:30 ET), TD Garden Boston.
Feiten nagelopen op 27-10-2026 (ESPN-API: summary 401909877, box scores en linescores 401909088, 401909095, 401909870,
401909836, 401909854 en 401909862, teamschema's 2025/26 en 2026/27, play-offschema Boston 2025/26, rosters en coaches,
standen 2025/26, spelersgemiddelden; onderlinge duels 2025/26 (401810105, 401809791, 401810492, 401810714);
officiële NBA-blessurelijst 27-10 05:45 ET (Boston nog niet ingediend); berichtgeving over de ruil van Randle
(aangekondigd 10-7-2026, Claxton naar Chicago), de draft van Mikel Brown Jr. (nr. 6) en de contracten van Ellis,
Wagner en Sharpe).
- Boston: 113-121 in Detroit (72-50 voor), 107-103 tegen New York (Tatum 36), 134-99 tegen Chicago op maandag (US),
  voorsprong tot 40, Tatum 28 minuten, Pritchard 28 punten (7 van 10 driepunters). Back-to-back, beide thuis.
- Brooklyn: 103-110 tegen Charlotte, 121-125 in Cleveland (22 punten achter, laatste kwart 41-29), 109-136 tegen Indiana.
- Onderling 2025/26: 113-99 (BKN), 105-113 (BOS), 130-126 na twee verlengingen (BKN), 148-111 (BOS): 3-1 Boston.
- 2025/26: Boston 30-11 thuis, 16 van de 41 thuisduels met 12 of meer gewonnen; Brooklyn verloor 19 van de 41
  uitduels met 12 of meer. Boston na een back-to-back (tweede avond) 8-5.
- Odds: alleen TOTO, uit specials/nba_feiten_2026_10_28.md (dinsdag ±10:45 NL). Handicap en totaal incl. verlenging.
- Eén wedtip (eis eigenaar): Nets +11,5 @1,93, onze kans ±56% (markt 51,8%, zonder marge ±49%).
  python3 specials/celtics_nets_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "Celtics – Nets voorspelling: wedtip en odds voor de back-to-back van Boston (28 oktober, 00:30)"
SLUG = "celtics-nets-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("Celtics – Nets voorspelling: Boston speelt een back-to-back tegen het zegeloze Brooklyn. "
                "Onze wedtip, TOTO-odds, blessures en opstellingen.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet-experts.nl/go/bet365"
DATUM = "2026-10-27T23:30:00.000Z"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>Onze Celtics – Nets voorspelling voor de nacht van dinsdag op woensdag: Boston wint, maar niet zo ruim als de bookmakers verwachten. Om 00:30 Nederlandse tijd ontvangen de Celtics in TD Garden de Brooklyn Nets, nog geen 24 uur nadat ze Chicago met 134-99 versloegen. Brooklyn staat op 0-3, maar liet in Cleveland zien dat het kan terugvechten. Onze voorspelling: Celtics – Nets 115-105. Onze wedtip: Brooklyn Nets +11,5 punten (inclusief verlenging) tegen een quotering van 1,93 bij TOTO.</strong></p>
<p>Hieronder lees je alles over vorm, blessures, de odds van <a href="/bookmakers/toto">TOTO</a> en onze onderbouwing.</p>
<h3><strong>Celtics – Nets: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "Boston Celtics – Brooklyn Nets"),
    ("Datum", "Woensdag 28 oktober 2026 (nacht van dinsdag op woensdag)"),
    ("Aanvang", "00:30 Nederlandse tijd (dinsdag 19:30 in Boston)"),
    ("Arena", "TD Garden, Boston"),
    ("Competitie", "NBA, reguliere competitie 2026/27"),
    ("Stand 2026/27", "Celtics 2-1, Nets 0-3"),
    ("Onderlinge duels 2025/26", "3-1 voor Boston"),
    ("Coaches", "Joe Mazzulla (Boston), Jordi Fernández (Brooklyn)"),
])}
<p>Nederland staat inmiddels op wintertijd, in de Verenigde Staten gaat de klok pas op 1 november terug. Boston speelde maandag nog, Brooklyn had maandag rust.</p>
<h3><strong>De eerste week: Boston op stoom, Brooklyn nog zonder zege</strong></h3>
<p><strong>Boston Celtics: twee thuiszeges na een valse start</strong></p>
<p>Boston begon in Detroit met een 121-113 nederlaag, nadat het begin derde kwart nog met 72-50 voorstond. Daarna volgden twee zeges in TD Garden. Tegen New York (107-103) maakte Jayson Tatum 36 punten, 9 rebounds en 7 assists. Maandag werd Chicago met 134-99 weggespeeld: Boston leidde met 40 punten, raakte 21 driepunters en Payton Pritchard maakte vanaf de bank 28 punten, met 7 van zijn 10 driepogingen raak. Tatum speelde maar 28 minuten, Paul George 25.</p>
<p>Opvallend is de nieuwe rol van Tatum. Zonder Jaylen Brown is hij niet alleen de topscorer, maar ook de spelverdeler: gemiddeld 24,0 punten en 8,0 assists.</p>
<p><strong>Brooklyn Nets: drie nederlagen, één met opgeheven hoofd</strong></p>
<p>Brooklyn verloor de thuisopener met 103-110 van Charlotte, ondanks 33 punten van nieuwkomer Julius Randle. Vrijdag in Cleveland stonden de Nets 22 punten achter, maar ze wonnen het laatste kwart met 41-29 en verloren uiteindelijk maar met 121-125. Michael Porter Jr. scoorde 28 punten, Randle 23 en Egor Demin 22, met 5 driepunters. Zondag volgde wel een harde klap: Indiana won in Brooklyn met 136-109. Porter Jr. maakte toen maar 10 punten (4 van 13), en de Nets kregen 78 punten tegen in het tweede en derde kwart.</p>
<h3><strong>Vorig seizoen en de onderlinge duels</strong></h3>
<p>Boston werd tweede in het Oosten en kreeg van alle dertig ploegen de minste punten tegen. In de play-offs ging het mis: tegen Philadelphia gaven de Celtics een 3-1 voorsprong weg en verloren ze de serie met 3-4. Brooklyn beleefde een zwaar jaar: 20 zeges, plaats dertien in het Oosten en het minst aantal gescoorde punten van de hele competitie.</p>
{tabel(["2025/26", "Boston Celtics", "Brooklyn Nets"], [
    ("Eindstand", "56-26 (nr. 2 Oost)", "20-62 (nr. 13 Oost)"),
    ("Thuis / uit", "30-11 / 26-15", "12-29 / 8-33"),
    ("Punten voor / tegen", "114,9 / 107,2", "105,9 / 115,9"),
    ("Na het seizoen", "Eerste ronde (3-4 tegen Philadelphia)", "Play-offs niet gehaald"),
])}
<p>Boston won drie van de vier onderlinge duels, maar ze waren minder eenzijdig dan de cijfers doen vermoeden. In november won Boston met 113-99 in Brooklyn, drie dagen later wonnen de Nets met 113-105 in TD Garden. In januari had Boston in Brooklyn twee verlengingen nodig (130-126). Alleen in februari was het verschil echt groot: 148-111 in Boston.</p>"""

content2 = f"""<h3><strong>Zo zijn beide selecties veranderd</strong></h3>
<p><strong>Boston Celtics: Brown weg, George en Robinson erbij</strong></p>
<p>Boston ruilde Jaylen Brown deze zomer naar Philadelphia en kreeg daar onder meer Paul George voor terug. Center Mitchell Robinson kwam over van de Knicks en routinier Mike Conley tekende voor één seizoen. Nikola Vučević vertrok naar Orlando. Tatum, die na zijn gescheurde achillespees in 2025 vorig seizoen maar 16 duels speelde, is weer volledig fit. Joe Mazzulla is nog altijd de coach.</p>
<p><strong>Brooklyn Nets: Randle als nieuwe leider</strong></p>
<p>Brooklyn haalde Julius Randle uit Minnesota in een ruil met vier clubs, waarbij center Nic Claxton na zijn hele loopbaan in Brooklyn naar Chicago vertrok. Met de zesde keuze in de draft koos Brooklyn guard Mikel Brown Jr. Verder kwamen verdediger Keon Ellis (vorig seizoen Sacramento en Cleveland) en center Moritz Wagner (Orlando), en tekende Day'Ron Sharpe een nieuw contract. Ziaire Williams vertrok. Josh Minott speelde begin vorig seizoen nog voor Boston en treft zijn oude club. Jordi Fernández begint aan zijn derde seizoen als coach.</p>
<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("Devin Carter", "Boston", "Speelt niet (ziek), miste alle duels van dit seizoen"),
    ("Tyler Bilodeau, Grant Nelson", "Brooklyn", "Niet bij de ploeg (two-way, G League)"),
    ("Joshua Jefferson, Drake Powell, Ben Saraf", "Brooklyn", "Niet bij de ploeg (G League)"),
])}
<p><em>Stand van de officiële NBA-blessurelijst op dinsdag 27 oktober, 10:45 Nederlandse tijd. Boston had zijn lijst toen nog niet ingediend. Na een back-to-back kan Mazzulla spelers rust geven; kijk vlak voor de start nog even.</em></p>
<p><strong>Verwachte basisvijf Celtics:</strong> Derrick White, Jordan Walsh, Paul George, Jayson Tatum, Mitchell Robinson. Dat was de vijf in alle drie de wedstrijden. Pritchard, Neemias Queta en Sam Hauser zijn de belangrijkste wissels.</p>
<p><strong>Verwachte basisvijf Nets:</strong> Egor Demin, Keon Ellis, Michael Porter Jr., Julius Randle, Day'Ron Sharpe. Ook deze vijf begonnen alle drie de duels. Nolan Traore, Minott, Wagner, Noah Clowney en Brown Jr. komen van de bank.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "2026/27 tot nu toe"], [
    ("Jayson Tatum (BOS)", "21,8*", "10,0*", "5,3*", "24,0 ptn, 6,7 reb, 8,0 ast"),
    ("Paul George (BOS)", "17,3**", "5,3**", "3,6**", "23,0 ptn, 5,7 reb"),
    ("Payton Pritchard (BOS)", "17,0", "3,9", "5,2", "16,3 ptn vanaf de bank"),
    ("Julius Randle (BKN)", "21,1***", "6,7***", "5,0***", "22,0 ptn, 7,0 reb, 6,3 ast"),
    ("Michael Porter Jr. (BKN)", "24,2", "7,1", "3,0", "21,3 ptn, 5,3 reb"),
    ("Egor Demin (BKN)", "10,3", "3,2", "3,3", "9,7 ptn, 3,0 ast"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26. * Tatum speelde toen 16 wedstrijden. ** George: 37 duels voor Philadelphia. *** Randle: voor Minnesota.</em></p>
<p><strong>Jayson Tatum</strong> is het middelpunt van alles bij Boston, als scorer en als aangever. <strong>Paul George</strong> opende met 38 punten in Detroit en is de tweede optie. Bij Brooklyn moeten <strong>Julius Randle</strong> en <strong>Michael Porter Jr.</strong> het doen: samen goed voor 43 punten per wedstrijd. Porter Jr. scoorde vorig seizoen 25, 33, 30 en 18 punten tegen Boston.</p>
<h3><strong>Odds Celtics – Nets bij TOTO</strong></h3>
<p>TOTO ziet Boston als grote favoriet: een quotering van 1,18 staat voor ongeveer 85 procent winkans. De handicap ligt rond de 11,5 punten in het voordeel van de Celtics, het verwachte puntentotaal op 221,5.</p>
{tabel(["Markt (TOTO)", "Celtics", "Nets"], [
    ("Winnaar (incl. verlenging)", "1,18", "5,20"),
    ("1X2 (reguliere speeltijd, gelijk 21,00)", "1,14", "5,75"),
    ("Handicap -10,5 / +10,5 (incl. verlenging)", "1,71", "1,98"),
    ("Handicap -11,5 / +11,5 (incl. verlenging)", "1,87", "1,93"),
    ("Handicap -12,5 / +12,5 (incl. verlenging)", "1,95", "1,73"),
])}
<p>Op het totaal biedt TOTO 220,5 punten (Over 1,83 / Under 1,98), 221,5 (1,93 / 1,87) en 222,5 (Over 2,05 / Under 1,80). Odds gelezen op dinsdag rond 10:45 uur; vergelijk ze vlak voor de start nog even.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op Celtics – Nets</strong></a></p>"""

content3 = f"""<h3><strong>Celtics – Nets voorspelling: Boston wint, Brooklyn blijft binnen de handicap</strong></h3>
<p>Boston is op papier veel sterker. De Celtics hebben de betere spelers, spelen thuis en wonnen vorig seizoen 30 van de 41 thuisduels.</p>
<p>Maar elf punten verschil is veel. Boston speelt voor de tweede avond op rij, en Mazzulla zal zijn sterren na een week met vier wedstrijden niet onnodig lang laten spelen als de wedstrijd in het slotkwart nog niet beslist is. Brooklyn heeft met Randle en Porter Jr. nu twee spelers die zelf hun punten kunnen maken, iets wat vorig seizoen ontbrak. En de onderlinge duels van vorig jaar laten zien dat de Nets vaker in de buurt bleven dan je zou denken. Onze voorspelling: <strong>Boston Celtics – Brooklyn Nets 115-105</strong>.</p>
<h3><strong>Onze wedtip: Nets +11,5 (1,93)</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Onze kans"], [
    ("Brooklyn Nets +11,5 punten (incl. verlenging)", "1,93", "TOTO", "Ongeveer 56 procent"),
])}
<p><strong>Waarom deze tip?</strong> De tip is goed als Brooklyn wint, of verliest met maximaal elf punten verschil. Een odd van 1,93 staat voor een kans van ongeveer 52 procent; zonder de marge van de bookmaker is dat ongeveer 49 procent. Wij schatten de kans op ongeveer 56 procent. De onderbouwing:</p>
<p><strong>1. Boston speelt een back-to-back.</strong> Maandag tegen Chicago, dinsdag tegen Brooklyn, de vierde wedstrijd in acht dagen. De Celtics wonnen vorig seizoen 8 van hun 13 wedstrijden op de tweede avond van een back-to-back, dus vermoeidheid is geen garantie op een nederlaag. Maar het maakt een ruime zege minder waarschijnlijk.</p>
<p><strong>2. Brooklyn heeft meer aanvalskracht dan vorig seizoen.</strong> Met 105,9 punten per duel was Brooklyn in 2025/26 de zwakste aanval van de NBA. Nu scoort de ploeg 111,0 punten per wedstrijd, met Randle (22,0) en Porter Jr. (21,3) als duo. In Cleveland maakten de Nets 41 punten in het laatste kwart en 20 driepunters in totaal.</p>
<p><strong>3. Boston wint thuis zelden met twaalf of meer.</strong> Vorig seizoen won Boston 16 van zijn 41 thuisduels met minstens twaalf punten verschil, minder dan 40 procent. Van de vier onderlinge duels eindigden er twee binnen de elf punten, en één werd zelfs door Brooklyn gewonnen in TD Garden.</p>
<p><strong>Waarom niet een andere markt?</strong> Een zege van Brooklyn (5,20) vraagt om ongeveer 19 procent kans; wij komen uit op zo'n 17 procent, dus die odd is te laag. Nets +12,5 (1,73) is veiliger, maar daarvoor heb je een kans van bijna 58 procent nodig, en dat extra punt is die lagere odd niet waard. Nets +10,5 (1,98) levert meer op, maar onze voorspelde marge van tien punten zit daar precies tegenaan. Het puntentotaal laten we liggen: onze voorspelling komt uit op 220 punten, vlak bij de lijn van 220,5.</p>
<p><strong>Het risico.</strong> Brooklyn kreeg tegen Indiana 136 punten tegen en verloor vorig seizoen 19 van zijn 41 uitwedstrijden met twaalf punten of meer. Schiet Boston weer zoals maandag (21 driepunters), dan loopt het verschil snel op. Let ook op: de handicap telt een eventuele verlenging mee. Meer uitleg vind je in onze gidsen over <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap wedden</a> en de <a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">money line</a>.</p>
<h3><strong>Celtics – Nets live kijken in Nederland</strong></h3>
<p>Bij <a href="/bookmakers/bet365">Bet365</a> kun je NBA-wedstrijden live volgen via de livestream. Je hebt daarvoor een account met een storting nodig. ESPN zendt in Nederland een deel van de NBA-wedstrijden uit; in de programmagids zie je of deze erbij zit. Met <strong>NBA League Pass</strong>, de betaalde dienst van de competitie, kun je alle wedstrijden volgen. Meer opties vind je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk Celtics – Nets live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Vannacht staan er nog drie wedstrijden op het programma. Lees ook onze voorspellingen voor <a href="/nieuws/knicks-pistons-voorspelling-wedtips-nba-2026">Knicks – Pistons</a>, <a href="/nieuws/spurs-kings-voorspelling-wedtips-nba-2026">Spurs – Kings</a> en <a href="/nieuws/lakers-trail-blazers-voorspelling-wedtips-nba-2026">Lakers – Trail Blazers</a>. Eerder schreven we over <a href="/nieuws/pistons-celtics-voorspelling-wedtips-nba-opening-2026">Pistons – Celtics</a>, en de tips van maandagnacht staan in de <a href="/nieuws/nba-voorspellingen-vannacht-27-oktober-2026">NBA-voorspellingen van 27 oktober</a>. Benieuwd <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">welke Nederlanders in de NBA spelen</a>? Nieuw met basketbal? Lees <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels in de NBA</a>. Alle tips staan op <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Celtics – Nets?</strong><br>Woensdag 28 oktober 2026 om 00:30 Nederlandse tijd, in de nacht van dinsdag op woensdag. In Boston is het dan dinsdagavond 19:30.</p>
<p><strong>Speelt Jayson Tatum mee?</strong><br>Naar verwachting wel. Hij speelde maandag 28 minuten tegen Chicago en stond dinsdagochtend niet op een blessurelijst. Boston had zijn blessurelijst toen nog niet ingediend.</p>
<p><strong>Wie is favoriet: Celtics of Nets?</strong><br>Boston, met een quotering van 1,18 bij TOTO. Brooklyn staat op 5,20.</p>
<p><strong>Wat is onze voorspelling voor Celtics – Nets?</strong><br>Boston wint met 115-105. Onze wedtip is Brooklyn Nets +11,5 punten, inclusief verlenging (1,93 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

KAART = {"home": "Celtics", "away": "Nets", "home_abbr": "bos", "away_abbr": "bkn", "home_pos": "56-26 · nr. 2 Oost 2025/26", "away_pos": "20-62 · nr. 13 Oost 2025/26", "hs": 115, "as": 105, "datum": "Wo 28 okt", "tijd": "00:30", "odd_home": "1,18", "odd_away": "5,20"}
WEDTIPS = {"wedtip-1-2": "Brooklyn Nets +11,5 punten (incl. verlenging)", "quotering-wedtip-1": "1.93",
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
                  "/nieuws/pistons-celtics-voorspelling-wedtips-nba-opening-2026",
                  "/nieuws/spurs-thunder-voorspelling-wedtips-nba-opening-2026",
                  "/nieuws/76ers-pistons-voorspelling-wedtips-nba-2026", "/nieuws/jazz-lakers-voorspelling-wedtips-nba-2026",
                  "/nieuws/lakers-warriors-voorspelling-wedtips-nba-2026",
                  "/nieuws/cavaliers-timberwolves-voorspelling-wedtips-nba-2026",
                  "/nieuws/nuggets-warriors-voorspelling-wedtips-nba-2026",
                  "/nieuws/knicks-pistons-voorspelling-wedtips-nba-2026", "/nieuws/spurs-kings-voorspelling-wedtips-nba-2026",
                  "/nieuws/lakers-trail-blazers-voorspelling-wedtips-nba-2026",
                  "/nieuws/welke-nederlanders-spelen-in-de-nba",
                  "/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders",
                  "/nieuws/wat-is-handicap-wedden-de-complete-gids",
                  "/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners",
                  "/wedden-op-nba-voorspellingen-en-wedtips---basketbal", "/bookmakers/toto", "/bookmakers/bet365",
                  "/live-kijken", BET365}
    assert set(hrefs) <= toegestaan, set(hrefs) - toegestaan
    for s in ("knicks-pistons", "spurs-kings", "lakers-trail-blazers"):
        assert f"/nieuws/{s}-voorspelling-wedtips-nba-2026" in hrefs, f"link naar {s} ontbreekt"
    assert "nba-voorspellingen-vannacht-28-oktober-2026" not in html, "geen algemeen artikel vannacht"
    assert "<table" not in html.replace(f"<table {T}>", ""), "tabellen alleen via tabel()"
    verboden = ["BetCity", "ESPN-API", "ESPN.com", "Associated Press", "DraftKings", "Rotowire", "Betfans"]
    assert not any(v.lower() in html.lower() for v in verboden), "geen bronnen/concurrenten"
    # SEO: focuskeyword
    fk = "Celtics – Nets voorspelling"
    assert fk in TITEL and fk in SAMENVATTING and len(SAMENVATTING) <= 160
    assert fk in content.split(".")[0], "focuskeyword in eerste zin"
    assert any(fk in h for h in re.findall(r"<h3>(.*?)</h3>", html)), "focuskeyword in een h3"
    # Wedtip en consistentie
    assert set(WEDTIPS) == {"wedtip-1-2", "quotering-wedtip-1", "bookmaker-wedtips"}
    assert WEDTIPS["bookmaker-wedtips"] == "669ab9f5aceb8b717cea24c3"
    q = float(WEDTIPS["quotering-wedtip-1"])
    toto_odds = {1.18, 5.20, 1.14, 21.0, 5.75, 1.95, 1.73, 1.87, 1.93, 1.71, 1.98, 1.83, 2.05, 1.80}
    assert q in toto_odds and q == 1.93
    assert KAART["as"] + 11.5 > KAART["hs"], "voorspelde score moet Nets +11,5 laten winnen"
    assert KAART["hs"] > KAART["as"], "voorspelling: Celtics winnen"
    assert f"{KAART['hs']}-{KAART['as']}" in content and f"{KAART['hs']}-{KAART['as']}" in content3
    assert KAART["odd_home"] == "1,18" and KAART["odd_away"] == "5,20" and KAART["tijd"] == "00:30"
    assert "1,93" in content and "1,93" in content3
    assert SLUG == "celtics-nets-voorspelling-wedtips-nba-2026" and DATUM == "2026-10-27T23:30:00.000Z"
    assert html.count("👉 Klik hier: maak je Bet365-account aan en wed live mee op") == 1
    tekst = re.sub(r"<[^>]+>", " ", html)
    print(len(TITEL), "tekens titel |", len(SAMENVATTING), "tekens samenvatting |", len(tekst.split()), "woorden")
    print("Alle asserts geslaagd (dry run, niets gepubliceerd).")
