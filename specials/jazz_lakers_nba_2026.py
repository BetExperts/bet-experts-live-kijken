# -*- coding: utf-8 -*-
"""Los artikel: Jazz – Lakers voorspelling, NBA 25 oktober 2026 (22:00 NL, wintertijd), Delta Center Salt Lake City.
Feiten nagelopen op 25-10-2026 (ESPN-API: summary 401909861, boxscores en play-by-play 401909838, 401909849,
401909092 en 401909851, teamschema's 2025/26 en 2026/27, rosters en coaches, standen 2025/26, spelersgemiddelden,
onderlinge duels 2025/26 (401810108, 401810137, 401810234, 401811053); officiële NBA-blessurelijst 25-10 04:30 ET;
berichtgeving over de ruil Jackson Jr. (3-2-2026) en zijn knieoperatie, de sign-and-trade van Kessler en de komst
van Hayes (1-7-2026) en de draft van Peterson (nr. 2, 23-6-2026)).
- Jazz: 103-123 in Memphis (achterstand tot 27 punten, Ty Jerome 45), 120-119 tegen New Orleans (Peterson vrije worpen 0:50,5).
- Lakers: 127-105 tegen Golden State, 125-117 tegen de Clippers (Reaves 28 en 9 assists, Kessler 22, Dončić 11 balverliezen).
- Onderling 2025/26: 140-126 en 131-107 in LA, 108-106 en 143-135 in Utah (4-0 Lakers); in april speelde Utah met reserves.
- Beide ploegen speelden vrijdag (US-tijd) en hadden zaterdag rust. Utah speelt maandag (US) alweer thuis tegen Memphis.
- Odds: alleen TOTO, uit specials/nba_feiten_2026_10_26.md (±09:45 NL op 25-10). Handicap en totaal incl. verlenging.
- Eén wedtip (eis eigenaar): Jazz +7,5 @1,67, onze kans 62% (markt 59,9%, zonder marge ±55%).
  python3 specials/jazz_lakers_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "Jazz – Lakers voorspelling: wedtip en odds voor Kesslers terugkeer in Utah (25 oktober, 22:00)"
SLUG = "jazz-lakers-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("De ongeslagen Lakers spelen hun eerste uitwedstrijd, bij een vernieuwd Utah. Voorspelling, onze wedtip, "
                "TOTO-odds, blessures en opstellingen.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet-experts.nl/go/bet365"
DATUM = "2026-10-25T21:00:00.000Z"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>Zondagavond om 22:00 Nederlandse tijd spelen de Los Angeles Lakers hun eerste uitwedstrijd van het seizoen, in Salt Lake City tegen de Utah Jazz. De Lakers wonnen hun twee thuisduels overtuigend, Utah staat op één zege en één nederlaag. Voor Walker Kessler is het een weerzien met de club die hem deze zomer naar Los Angeles liet gaan. Onze voorspelling: Jazz – Lakers 116-121. Onze wedtip: Utah Jazz +7,5 punten (inclusief verlenging) tegen een quotering van 1,67 bij TOTO.</strong></p>
<p>Hieronder lees je alles over vorm, blessures, de odds van <a href="/bookmakers/toto">TOTO</a> en onze onderbouwing.</p>
<h3><strong>Jazz – Lakers: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "Utah Jazz – Los Angeles Lakers"),
    ("Datum", "Zondag 25 oktober 2026"),
    ("Aanvang", "22:00 Nederlandse tijd (15:00 in Salt Lake City)"),
    ("Arena", "Delta Center, Salt Lake City"),
    ("Competitie", "NBA, reguliere competitie 2026/27"),
    ("Stand 2026/27", "Jazz 1-1, Lakers 2-0"),
    ("Onderlinge duels 2025/26", "4-0 voor de Lakers"),
])}
<p>Nederland staat sinds de nacht van zaterdag op zondag op wintertijd, in de Verenigde Staten gaat de klok pas op 1 november terug. Beide ploegen speelden vrijdag en hadden zaterdag een rustdag.</p>
<h3><strong>De eerste week: Lakers op dreef, Utah wisselvallig</strong></h3>
<p><strong>Utah Jazz: zware nederlaag, daarna een nipte zege</strong></p>
<p>Utah opende in Memphis met een 123-103 nederlaag. Memphis stond in het derde kwart 27 punten voor, Ty Jerome scoorde 45 punten. Vrijdag volgde in Salt Lake City een 120-119 zege op New Orleans. Jaren Jackson Jr. maakte 24 punten en 10 rebounds, George had 19 punten en 10 assists en invaller Jaxson Hayes 17 punten. Rookie Darryn Peterson, de nummer twee van de draft van juni, zette Utah 50 seconden voor tijd met twee vrije worpen op voorsprong.</p>
<p><strong>Los Angeles Lakers: twee thuiszeges</strong></p>
<p>De Lakers versloegen Golden State met 127-105. Kessler maakte bij zijn debuut 26 punten, met alle 12 schoten raak. Vrijdag won de ploeg van coach JJ Redick met 125-117 de stadsderby tegen de Clippers, die het zonder Bradley Beal, Brandon Ingram en Max Strus moesten doen. Austin Reaves had 28 punten en 9 assists, Kessler 22 punten. Luka Dončić kwam tot 23 punten en 7 assists, maar verloor de bal 11 keer. De Lakers schoten in beide duels 57 procent of beter uit het veld, maar verloren de bal samen 39 keer.</p>
<h3><strong>Vorig seizoen en de onderlinge duels</strong></h3>
<p>De Lakers wonnen 53 wedstrijden, versloegen Houston in de eerste ronde van de play-offs (4-2) en gingen daarna met 0-4 onderuit tegen Oklahoma City. Utah werd laatste in het Westen en kreeg de meeste punten tegen van alle dertig ploegen.</p>
{tabel(["2025/26", "Utah Jazz", "Los Angeles Lakers"], [
    ("Eindstand", "22-60 (nr. 15 West)", "53-29 (nr. 4 West)"),
    ("Thuis / uit", "14-27 / 8-33", "28-13 / 25-16"),
    ("Punten voor / tegen", "117,6 / 126,0", "116,3 / 114,6"),
    ("Na het seizoen", "Play-offs niet gehaald", "Tweede ronde (0-4 tegen OKC)"),
])}
<p>Let wel: de Lakers wonnen 53 keer met een puntensaldo van maar +1,7 per wedstrijd. Dat past eerder bij een subtopper dan bij een topploeg. Alle vier de onderlinge duels gingen naar Los Angeles: 140-126 en 131-107 thuis, 108-106 en 143-135 in Salt Lake City. In Utah was het verschil dus 2 en 8 punten. Dončić scoorde 37, 33 en 45 punten; in het vierde duel, in april, ontbrak hij en speelde Utah met reserves.</p>"""

content2 = f"""<h3><strong>Zo zijn beide selecties veranderd</strong></h3>
<p><strong>Utah Jazz: van wederopbouw naar een nieuwe kern</strong></p>
<p>In februari haalde Utah Jaren Jackson Jr. uit Memphis, de Defensive Player of the Year van 2023. Bij de medische keuring na de ruil werd een goedaardig gezwel in zijn linkerknie gevonden; na drie wedstrijden werd hij geopereerd en miste hij de rest van het seizoen. Nu is hij terug, naast Lauri Markkanen en George. In juni koos Utah met de tweede keuze in de draft Peterson uit Kansas, en Ace Bailey (vorig jaar de nummer vijf) begint aan zijn tweede seizoen. Kessler vertrok in een sign-and-trade naar de Lakers, voor draftkeuzes. Als vervanger tekende Hayes, die de afgelopen seizoenen bij de Lakers speelde. Will Hardy is nog altijd de coach.</p>
<p><strong>Los Angeles Lakers: alles om Dončić</strong></p>
<p>LeBron James tekende bij Philadelphia, en ook Rui Hachimura, Deandre Ayton, Marcus Smart en Hayes vertrokken. Daarvoor kwamen Kessler, Quentin Grimes, Collin Sexton, Kevon Looney en Matisse Thybulle.</p>
<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("Jusuf Nurkić", "Utah", "Speelt niet (scheur in de plantaire plaat, rechtervoet)"),
    ("Trey Alexander, Harrison Ingram", "Utah", "Niet bij de ploeg (G League)"),
    ("Cameron Carr", "LA Lakers", "Speelt niet (schuine buikspier)"),
    ("Adou Thiero", "LA Lakers", "Speelt niet (vocht in de linkerknie)"),
    ("Walker Kessler", "LA Lakers", "Inzetbaar (spalk om een vinger van de linkerhand)"),
    ("Jake LaRavia", "LA Lakers", "Miste vrijdag de derby (enkel), staat niet meer op de lijst"),
])}
<p><em>Stand van de officiële NBA-blessurelijst op zondag 25 oktober, 09:30 Nederlandse tijd.</em></p>
<p><strong>Verwachte basisvijf Utah:</strong> Keyonte George, Darryn Peterson, Ace Bailey, Jaren Jackson Jr., Lauri Markkanen. Dat was de vijf van vrijdag; in Memphis begon Hayes in plaats van Bailey. Hayes, Kyle Filipowski en Isaiah Collier zijn de belangrijkste wissels.</p>
<p><strong>Verwachte basisvijf Lakers:</strong> Luka Dončić, Austin Reaves, Matisse Thybulle, Ziaire Williams, Walker Kessler. Dezelfde vijf als in de eerste twee wedstrijden. Grimes, Sandro Mamukelashvili en Sexton zijn de belangrijkste wissels.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "2026/27 tot nu toe"], [
    ("Luka Dončić (LAL)", "33,5", "7,7", "8,3", "25,5 ptn, 7 ast, 17 balverliezen"),
    ("Austin Reaves (LAL)", "23,3", "4,7", "5,5", "25,5 ptn, 7,5 ast"),
    ("Walker Kessler (LAL)", "14,4", "10,8", "3,0", "24 ptn, 22 van de 26 raak"),
    ("Keyonte George (UTA)", "23,6", "3,7", "6,1", "20,5 ptn, 7,5 ast"),
    ("Lauri Markkanen (UTA)", "26,7", "6,9", "2,1", "17 ptn, 38,5% uit het veld"),
    ("Jaren Jackson Jr. (UTA)", "19,4*", "5,7*", "2,0*", "19,5 ptn, 7,5 reb"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26. * Jackson Jr.: alle 48 duels van vorig seizoen, waarvan 45 voor Memphis. Kessler speelde in 2025/26 maar vijf wedstrijden.</em></p>
<p><strong>Luka Dončić</strong> scoorde vorig seizoen gemiddeld ruim 38 punten tegen Utah, maar schiet dit seizoen nog maar 38,5 procent en gaat slordig met de bal om. <strong>Walker Kessler</strong> kent zijn oude club door en door en treft in <strong>Jaren Jackson Jr.</strong> een van de beste verdedigers rond de ring. <strong>Keyonte George</strong> maakte vorig seizoen 34, 27 en 34 punten tegen de Lakers.</p>
<h3><strong>Odds Jazz – Lakers bij TOTO</strong></h3>
<p>TOTO ziet de Lakers als duidelijke favoriet: een quotering van 1,41 staat voor ongeveer 71 procent winkans. De handicap ligt rond de 6,5 punten in het voordeel van Los Angeles, het verwachte puntentotaal op 237,5.</p>
{tabel(["Markt (TOTO)", "Jazz", "Lakers"], [
    ("Winnaar (incl. verlenging)", "2,95", "1,41"),
    ("1X2 (reguliere speeltijd, gelijk 18,00)", "3,15", "1,40"),
    ("Handicap +5,5 / -5,5 (incl. verlenging)", "1,93", "1,77"),
    ("Handicap +6,5 / -6,5 (incl. verlenging)", "1,87", "1,95"),
    ("Handicap +7,5 / -7,5 (incl. verlenging)", "1,67", "2,05"),
])}
<p>Op het totaal biedt TOTO 236,5 punten (Over 1,77 / Under 1,93), 237,5 (1,91 / 1,91) en 238,5 (Over 1,93 / Under 1,77). Odds gelezen op zondag rond 09:45 uur; vergelijk ze vlak voor de start nog even.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op Jazz – Lakers</strong></a></p>"""

content3 = f"""<h3><strong>Onze voorspelling: Lakers winnen, maar Utah blijft in de buurt</strong></h3>
<p>Los Angeles heeft de betere ploeg en met Dončić de beste speler op het veld. Toch zijn de cijfers van de eerste week minder overtuigend dan ze lijken. Golden State en de Clippers misten allebei belangrijke spelers, en in beide duels verloren de Lakers de bal vaak.</p>
<p>Utah is niet meer de ploeg die vorig seizoen 60 keer verloor. Met Jackson Jr. erbij, Markkanen en George fit en Peterson als nieuwe aanwinst heeft Hardy meer kwaliteit dan in heel 2025/26. De zware nederlaag in Memphis was vooral het werk van één speler die alles raak schoot. En ook vorig seizoen, toen Utah veel zwakker was, wonnen de Lakers in Salt Lake City maar met 2 en 8 punten verschil. Onze voorspelling: <strong>Utah Jazz – Los Angeles Lakers 116-121</strong>.</p>
<h3><strong>Onze wedtip: Jazz +7,5 (1,67)</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Onze kans"], [
    ("Utah Jazz +7,5 punten (incl. verlenging)", "1,67", "TOTO", "Ongeveer 62 procent"),
])}
<p><strong>Waarom deze tip?</strong> De tip is goed als Utah wint, of verliest met maximaal zeven punten verschil. Een odd van 1,67 staat voor een kans van 60 procent; zonder de marge van de bookmaker is dat ongeveer 55 procent. Wij schatten de kans op ongeveer 62 procent. De onderbouwing:</p>
<p><strong>1. Utah is sterker dan het record van vorig jaar.</strong> Jackson Jr. speelde vorig seizoen maar drie duels voor Utah, Peterson zat nog op de universiteit en in het laatste onderlinge duel, in april, stond er een ploeg vol reserves. Nu staan Jackson Jr., Markkanen, George en Peterson samen op het veld.</p>
<p><strong>2. De Lakers wonnen vaak krap.</strong> Vorig seizoen kwamen ze aan 53 zeges met een puntensaldo van maar +1,7 per wedstrijd. In Utah won Los Angeles beide keren met hooguit acht punten, toen nog met LeBron James in de ploeg.</p>
<p><strong>3. De eerste week vertekent.</strong> De Lakers speelden twee keer thuis tegen tegenstanders die belangrijke spelers misten, en maakten toch 39 balverliezen. Vandaag spelen ze voor het eerst uit, tegen een ploeg met lengte en een publiek in de rug.</p>
<p><strong>Waarom niet een andere markt?</strong> Een zege van de Lakers (1,41) vraagt om 71 procent kans; wij komen uit op ongeveer 66 procent, dus die odd is te laag. Bij Lakers -5,5 (1,77) en -6,5 (1,95) moet Los Angeles ruimer winnen dan wij verwachten. Jazz +6,5 (1,87) of +5,5 (1,93) levert meer op, maar onze voorspelde marge van vijf punten zit daar te dicht tegenaan. Het puntentotaal laten we liggen: onze voorspelling komt uit op 237 punten, precies op de lijn. De onderlinge duels van vorig seizoen (266, 214 en 278 punten met beide basisploegen) waren te wisselend om houvast te geven.</p>
<p><strong>Het risico.</strong> Schiet Dončić zoals vorig seizoen tegen Utah, dan kan het verschil snel oplopen. En Utah kreeg vorig seizoen de meeste punten tegen van de competitie. Let ook op: de handicap telt een eventuele verlenging mee. Meer uitleg vind je in onze gidsen over <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap wedden</a> en de <a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">money line</a>.</p>
<h3><strong>Jazz – Lakers live kijken in Nederland</strong></h3>
<p>Bij <a href="/bookmakers/bet365">Bet365</a> kun je NBA-wedstrijden live volgen via de livestream. Je hebt daarvoor een account met een storting nodig. ESPN zendt in Nederland een deel van de NBA-wedstrijden uit; in de programmagids zie je of deze erbij zit. Met <strong>NBA League Pass</strong>, de betaalde dienst van de competitie, kun je alle wedstrijden volgen. Meer opties vind je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk Jazz – Lakers live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Lees ook onze voorspellingen voor <a href="/nieuws/lakers-clippers-voorspelling-wedtips-nba-2026">Lakers – Clippers</a> en <a href="/nieuws/lakers-warriors-voorspelling-wedtips-nba-2026">Lakers – Warriors</a>, en de <a href="/nieuws/nba-voorspellingen-vannacht-25-oktober-2026">NBA-voorspellingen van 25 oktober</a>. Benieuwd <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">welke Nederlanders in de NBA spelen</a>? Nieuw met basketbal? Lees <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels in de NBA</a>. Alle tips staan op <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Jazz – Lakers?</strong><br>Zondag 25 oktober 2026 om 22:00 Nederlandse tijd. In Salt Lake City is het dan 15:00.</p>
<p><strong>Speelt Walker Kessler mee?</strong><br>Ja. Hij staat met een spalk om een vinger van zijn linkerhand op de blessurelijst, maar wel als inzetbaar. Voor Kessler is het de eerste wedstrijd tegen Utah sinds zijn vertrek deze zomer.</p>
<p><strong>Wie is favoriet: Jazz of Lakers?</strong><br>De Lakers, met een quotering van 1,41 bij TOTO. Utah staat op 2,95.</p>
<p><strong>Wat is onze voorspelling voor Jazz – Lakers?</strong><br>De Lakers winnen met 116-121. Onze wedtip is Utah Jazz +7,5 punten, inclusief verlenging (1,67 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

KAART = {"home": "Jazz", "away": "Lakers", "home_abbr": "utah", "away_abbr": "lal", "home_pos": "22-60 · nr. 15 West 2025/26", "away_pos": "53-29 · nr. 4 West 2025/26", "hs": 116, "as": 121, "datum": "Zo 25 okt", "tijd": "22:00", "odd_home": "2,95", "odd_away": "1,41"}
WEDTIPS = {"wedtip-1-2": "Utah Jazz +7,5 punten (incl. verlenging)", "quotering-wedtip-1": "1.67",
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
    toegestaan = {"/nieuws/nba-voorspellingen-vannacht-25-oktober-2026", "/nieuws/nba-voorspellingen-vannacht-24-oktober-2026",
                  "/nieuws/76ers-bucks-voorspelling-wedtips-nba-2026", "/nieuws/heat-pistons-voorspelling-wedtips-nba-2026",
                  "/nieuws/lakers-clippers-voorspelling-wedtips-nba-2026", "/nieuws/thunder-nuggets-voorspelling-wedtips-nba-2026",
                  "/nieuws/lakers-warriors-voorspelling-wedtips-nba-2026", "/nieuws/76ers-cavaliers-voorspelling-wedtips-nba-2026",
                  "/nieuws/welke-nederlanders-spelen-in-de-nba",
                  "/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders",
                  "/nieuws/wat-is-handicap-wedden-de-complete-gids",
                  "/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners",
                  "/wedden-op-nba-voorspellingen-en-wedtips---basketbal", "/bookmakers/toto", "/bookmakers/bet365",
                  "/live-kijken", BET365}
    assert set(hrefs) <= toegestaan, set(hrefs) - toegestaan
    assert "<table" not in html.replace(f"<table {T}>", ""), "tabellen alleen via tabel()"
    verboden = ["BetCity", "ESPN-API", "ESPN.com", "Associated Press", "DraftKings", "Rotowire", "Betfans"]
    assert not any(v.lower() in html.lower() for v in verboden), "geen bronnen/concurrenten"
    # Wedtip en consistentie
    assert set(WEDTIPS) == {"wedtip-1-2", "quotering-wedtip-1", "bookmaker-wedtips"}
    assert WEDTIPS["bookmaker-wedtips"] == "669ab9f5aceb8b717cea24c3"
    q = float(WEDTIPS["quotering-wedtip-1"])
    toto_odds = {2.95, 1.41, 3.15, 18.0, 1.40, 1.93, 1.77, 1.87, 1.95, 1.67, 2.05, 1.91}
    assert q in toto_odds and q >= 1.40
    assert KAART["hs"] + 7.5 > KAART["as"], "voorspelde score moet Jazz +7,5 laten winnen"
    assert KAART["as"] > KAART["hs"], "voorspelling: Lakers winnen"
    assert f"{KAART['hs']}-{KAART['as']}" in content and f"{KAART['hs']}-{KAART['as']}" in content3
    assert KAART["odd_home"] == "2,95" and KAART["odd_away"] == "1,41" and KAART["tijd"] == "22:00"
    assert "1,67" in content and "1,67" in content3
    assert SLUG == "jazz-lakers-voorspelling-wedtips-nba-2026" and DATUM == "2026-10-25T21:00:00.000Z"
    tekst = re.sub(r"<[^>]+>", " ", html)
    print(len(TITEL), "tekens titel |", len(SAMENVATTING), "tekens samenvatting |", len(tekst.split()), "woorden")
    print("Alle asserts geslaagd (dry run, niets gepubliceerd).")
