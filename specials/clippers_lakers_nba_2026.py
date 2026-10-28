# -*- coding: utf-8 -*-
"""Los artikel: Clippers – Lakers voorspelling, NBA 29 oktober 2026 (03:30 NL, wintertijd; woensdag 19:30 PT),
Intuit Dome Inglewood/Los Angeles. Feiten nagelopen op 28-10-2026 (ESPN-API: summary 401909892, boxscores 401909842,
401909851, 401909865, 401909092, 401909861 en 401909880, teamschema's 2025/26 en 2026/27, play-in 2025/26,
spelersgemiddelden 2025/26 en 2026/27, onderlinge duels 2025/26 (401809801, 401810250, 401810488, 401810664);
officiële NBA-blessurelijst 28-10 05:45 ET (Lakers nog niet ingeleverd); selectiewijzigingen en coaches zoals
nagelopen voor lakers_clippers_nba_2026.py op 23-10).
- Derby 24-10: Lakers 125-117 (Reaves 28/9 ast, Kessler 22, Dončić 23 met 11 balverliezen, Lopez 22 met 8/9, Garland 26
  met 9 balverliezen); Clippers 25 balverliezen.
- Lakers 2026/27: totalen 232, 242, 255, 265; tegenpunten 105, 117, 123, 136. Dinsdag 129-136 tegen Portland (Dončić 41).
- Clippers 2026/27: 121-96 Kings (217), 117-125 Lakers (242), 101-108 in OKC (209, 26 balverliezen).
- Onderling 2025/26: 135-118 en 125-122 Lakers thuis, 103-88 en 112-104 Clippers thuis (Intuit Dome: 191 en 216 punten).
- Odds: alleen TOTO, uit specials/nba_feiten_2026_10_29.md (±10:50 NL op 28-10). Winnaar/handicap/totaal incl. verlenging.
- Eén wedtip (eis eigenaar): Over 228,5 punten @1,87, onze kans 56% (markt 53,5%, zonder marge ±51%).
  python3 specials/clippers_lakers_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "Clippers – Lakers voorspelling: wedtip en odds voor de tweede LA-derby in vijf dagen (29 oktober, 03:30)"
SLUG = "clippers-lakers-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("Clippers – Lakers voorspelling: tweede LA-derby in vijf dagen, de Lakers op een back-to-back. "
                "Wedtip, TOTO-odds, blessures en opstellingen.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet-experts.nl/go/bet365"
DATUM = "2026-10-29T02:30:00.000Z"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>Clippers – Lakers voorspelling: in de nacht van woensdag op donderdag spelen de LA Clippers om 03:30 Nederlandse tijd thuis in de Intuit Dome tegen de Los Angeles Lakers. Het is de tweede stadsderby in vijf dagen: in de nacht van vrijdag op zaterdag wonnen de Lakers de eerste met 125-117. Nu spelen ze op een back-to-back, een dag na hun eerste nederlaag van het seizoen. Luka Dončić scoort 36 punten per duel, de Clippers missen zes spelers. Onze voorspelling: Clippers – Lakers 113-119. Onze wedtip: Over 228,5 punten (inclusief verlenging) tegen een quotering van 1,87 bij TOTO.</strong></p>
<p>Hieronder lees je alles over vorm, blessures, de odds van <a href="/bookmakers/toto">TOTO</a> en onze onderbouwing.</p>
<h3><strong>Clippers – Lakers: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "LA Clippers – Los Angeles Lakers"),
    ("Datum", "Donderdag 29 oktober 2026 (nacht van woensdag op donderdag)"),
    ("Aanvang", "03:30 Nederlandse tijd (woensdag 19:30 in Los Angeles)"),
    ("Arena", "Intuit Dome, Inglewood (Los Angeles)"),
    ("Competitie", "NBA, reguliere competitie 2026/27"),
    ("Stand 2026/27", "Clippers 1-2, Lakers 3-1"),
    ("Onderling dit seizoen", "1-0 voor de Lakers (125-117)"),
])}
<p>De VS gaan pas op 1 november naar wintertijd, dus het verschil met Los Angeles is deze week acht uur. De Lakers speelden dinsdagavond (Amerikaanse tijd) nog thuis tegen Portland en hebben minder dan 24 uur rust. De Clippers hadden twee rustdagen.</p>
<h3><strong>De eerste week: Lakers scoren veel, Clippers verliezen de bal</strong></h3>
<p><strong>Los Angeles Lakers: drie zeges, dan de eerste nederlaag</strong></p>
<p>De ploeg van coach JJ Redick versloeg Golden State (127-105), de Clippers (125-117) en Utah (132-123), waar Dončić 52 punten maakte. Dinsdag ging het voor het eerst mis: Portland won met 136-129 in Los Angeles. Dončić had 41 punten en 9 assists, Reaves 26 punten. Portland maakte 18 driepunters. Opvallend: de Lakers kregen per wedstrijd meer punten tegen, van 105 via 117 en 123 naar 136. Hun vier duels eindigden op 232, 242, 255 en 265 punten.</p>
<p><strong>LA Clippers: één zege, twee nederlagen en veel balverlies</strong></p>
<p>De ploeg van Tyronn Lue opende met 121-96 tegen Sacramento (Darius Garland 30 punten). Daarna volgden de 117-125 in de derby en een 101-108 nederlaag in Oklahoma City. Brook Lopez maakt van de bank 18 punten per duel. Het grote probleem: de Clippers verloren de bal in de derby 25 keer en in Oklahoma City 26 keer.</p>
<p>In de eerste derby (242 punten) had Reaves 28 punten en 9 assists en Walker Kessler 22. Dončić kwam tot 23 punten, maar verloor de bal 11 keer. Bij de Clippers maakten Garland 26 en Lopez 22 punten.</p>
<h3><strong>Vorig seizoen en de onderlinge duels</strong></h3>
<p>De Lakers wonnen in 2025/26 53 wedstrijden, versloegen Houston in de eerste ronde van de play-offs (4-2) en gingen daarna met 0-4 onderuit tegen Oklahoma City. De Clippers werden met 42-40 negende in het Westen en verloren in de play-in thuis van Golden State (121-126).</p>
{tabel(["2025/26", "LA Clippers", "Los Angeles Lakers"], [
    ("Eindstand", "42-40 (nr. 9 West)", "53-29 (nr. 4 West)"),
    ("Thuis / uit", "23-18 / 19-22", "28-13 / 25-16"),
    ("Punten voor / tegen", "113,8 / 112,6", "116,3 / 114,6"),
    ("Na het seizoen", "Uitgeschakeld in de play-in", "Tweede ronde (0-4 tegen OKC)"),
])}
<p>Vorig seizoen won steeds de thuisploeg. De Lakers wonnen thuis met 135-118 en 125-122, de Clippers in hun eigen arena met 103-88 en 112-104. Let op dat verschil: de derby's in de Intuit Dome eindigden op 191 en 216 punten, die in de arena van de Lakers op 253 en 247.</p>"""

content2 = f"""<h3><strong>Zo zijn beide selecties veranderd</strong></h3>
<p><strong>LA Clippers: een nieuwe ploeg rond Garland</strong></p>
<p>In februari ruilden de Clippers James Harden met Cleveland voor Garland. Center Ivica Zubac vertrok naar Indiana, voor onder anderen Isaiah Jackson en de draftkeuze waarmee de Clippers in juni Keaton Wagler kozen. Deze zomer ging Kawhi Leonard terug naar Toronto, in ruil voor Brandon Ingram, Gradey Dick en draftkeuzes. Rui Hachimura kwam over van de Lakers en ook Max Strus sloot aan, maar Ingram en Strus speelden nog geen minuut voor de Clippers.</p>
<p><strong>Los Angeles Lakers: alles om Dončić</strong></p>
<p>LeBron James tekende bij Philadelphia, en ook Hachimura, Deandre Ayton, Marcus Smart en Jaxson Hayes vertrokken. Daarvoor kwamen Kessler, Quentin Grimes, Collin Sexton, Kevon Looney en Matisse Thybulle.</p>
<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("Rui Hachimura", "LA Clippers", "Speelt niet (pijnlijke linkerdijbeenspier)"),
    ("Bradley Beal", "LA Clippers", "Speelt niet (rechterknie)"),
    ("Brandon Ingram", "LA Clippers", "Speelt niet (herstel na operatie aan de rechterhiel)"),
    ("Max Strus", "LA Clippers", "Speelt niet (scheur in de voetzoolpees, rechtervoet)"),
    ("Yanic Konan Niederhauser", "LA Clippers", "Speelt niet (voetoperatie)"),
    ("Jordan Miller", "LA Clippers", "Speelt niet (schouderoperatie)"),
    ("Cameron Carr", "LA Lakers", "Speelde dinsdag niet (schuine buikspier)"),
    ("Adou Thiero", "LA Lakers", "Speelde dinsdag niet (linkerknie)"),
])}
<p><em>Stand van de officiële NBA-blessurelijst op woensdag 28 oktober, 10:45 Nederlandse tijd. De Lakers hadden hun lijst voor deze wedstrijd toen nog niet ingeleverd.</em></p>
<p><strong>Verwachte basisvijf Clippers:</strong> Darius Garland, Kris Dunn, Derrick Jones Jr., Isaiah Jackson en een vervanger voor Hachimura, die in alle drie de wedstrijden begon. Lopez en Wagler liggen het meest voor de hand; Dick en Kobe Sanders zijn de andere vaste wissels.</p>
<p><strong>Verwachte basisvijf Lakers:</strong> Luka Dončić, Austin Reaves, Matisse Thybulle, Ziaire Williams, Walker Kessler. Dezelfde vijf als in alle vier de wedstrijden. Grimes, Sandro Mamukelashvili, Sexton en Jake LaRavia zijn de belangrijkste wissels.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "2026/27 tot nu toe"], [
    ("Luka Dončić (LAL)", "33,5", "7,7", "8,3", "36 ptn, 8,2 ast, 52 en 41 in de laatste twee"),
    ("Austin Reaves (LAL)", "23,3", "4,7", "5,5", "26,5 ptn, 6,5 ast"),
    ("Walker Kessler (LAL)", "14,4*", "10,8*", "3,0*", "15,8 ptn, 8 reb"),
    ("Darius Garland (LAC)", "19,9*", "2,3*", "6,4*", "24 ptn, 7 ast, 18 balverliezen"),
    ("Brook Lopez (LAC)", "8,5", "3,6", "1,3", "18 ptn, 20 van de 31 raak"),
    ("Keaton Wagler (LAC)", "-", "-", "-", "13 ptn, 4,3 reb, 4 ast"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26. * Kessler speelde vorig seizoen vijf wedstrijden voor Utah, Garland negentien voor de Clippers (cijfers bij de Clippers). Wagler is rookie.</em></p>
<p><strong>Brook Lopez</strong> maakt op zijn 38e een sterke start en kan de basisplaats van Hachimura overnemen. <strong>Darius Garland</strong> moet de Clippers dragen, maar verloor in drie duels al 18 keer de bal.</p>
<h3><strong>Odds Clippers – Lakers bij TOTO</strong></h3>
<p>TOTO ziet de Lakers als favoriet: een quotering van 1,54 staat voor ongeveer 65 procent winkans. De handicap ligt rond de 4,5 punten in het voordeel van de Lakers, het verwachte puntentotaal op 228,5.</p>
{tabel(["Markt (TOTO)", "Clippers", "Lakers"], [
    ("Winnaar (incl. verlenging)", "2,55", "1,54"),
    ("1X2 (reguliere speeltijd, gelijk 18,00)", "2,60", "1,53"),
    ("Handicap +3,5 / -3,5 (incl. verlenging)", "1,95", "1,73"),
    ("Handicap +4,5 / -4,5 (incl. verlenging)", "1,91", "1,91"),
    ("Handicap +5,5 / -5,5 (incl. verlenging)", "1,73", "1,95"),
])}
<p>Op het totaal biedt TOTO 227,5 punten (Over 1,73 / Under 1,95), 228,5 punten (Over 1,87 / Under 1,93) en 229,5 punten (Over 1,91 / Under 1,78), allemaal inclusief verlenging. Odds gelezen op woensdag rond 10:50 uur; vergelijk ze vlak voor de start nog even.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op Clippers – Lakers</strong></a></p>"""

content3 = f"""<h3><strong>Clippers – Lakers voorspelling: Lakers winnen in een duel met veel punten</strong></h3>
<p>De Lakers hebben met Dončić en Reaves het beste duo op het veld, en de Clippers missen nu ook Hachimura. Daar staat tegenover dat Los Angeles minder dan een dag rust heeft en verdedigend steeds zwakker oogt. De Clippers zijn uitgerust, maar hebben buiten Garland weinig spelers die zelf een kans creëren.</p>
<p>Wij verwachten opnieuw een open derby, met een kleiner verschil dan in de eerste ontmoeting. Onze voorspelling: <strong>LA Clippers – Los Angeles Lakers 113-119</strong>.</p>
<h3><strong>Onze wedtip: Over 228,5 punten (1,87)</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Onze kans"], [
    ("Over 228,5 punten (incl. verlenging)", "1,87", "TOTO", "Ongeveer 56 procent"),
])}
<p><strong>Waarom deze tip?</strong> De tip is goed als er in totaal 229 punten of meer vallen, een eventuele verlenging inbegrepen. Een odd van 1,87 staat voor een kans van 53,5 procent; zonder de marge van de bookmaker is dat ongeveer 51 procent. Wij schatten de kans op ongeveer 56 procent. De onderbouwing:</p>
<p><strong>1. Elke wedstrijd van de Lakers ging over deze lijn.</strong> De vier duels eindigden op 232, 242, 255 en 265 punten. Los Angeles scoort 128,2 punten per wedstrijd en kreeg er gemiddeld 120,2 tegen, met 136 tegen Portland als uitschieter.</p>
<p><strong>2. De eerste derby eindigde op 242 punten.</strong> En dat terwijl Dončić 11 keer de bal verloor en maar 23 punten maakte. De Clippers scoorden 117 punten zonder Beal, Ingram en Strus. Hun vele balverliezen leveren de tegenstander makkelijke punten op.</p>
<p><strong>3. Een back-to-back gaat vaak ten koste van de verdediging.</strong> De Lakers spelen binnen 24 uur opnieuw, na een duel waarin ze 136 punten weggaven. Vermoeide benen merk je vaak het eerst bij het terugverdedigen. Dončić en Reaves blijven wel scoren: samen 62,5 punten per duel.</p>
<p><strong>Waarom niet een andere markt?</strong> Een zege van de Lakers (1,54) vraagt om 65 procent kans; wij komen uit op ongeveer 66 procent, en dat verschil is te klein. Bij Lakers -4,5 (1,91) moet Los Angeles met minstens vijf punten winnen. Onze voorspelde marge is zes punten, maar met een back-to-back en de thuiszeges van de Clippers in de derby's van vorig seizoen is dat te krap. Over 227,5 is een punt veiliger, maar levert met 1,73 duidelijk minder op. Over 229,5 (1,91) geeft maar een fractie meer, terwijl onze voorspelling van 232 punten dan dichter bij de lijn komt.</p>
<p><strong>Het risico.</strong> De wedstrijden van de Clippers eindigden op 217, 242 en 209 punten, en zonder Hachimura missen ze nog een basisspeler. De twee derby's in de Intuit Dome van vorig seizoen bleven steken op 191 en 216 punten. Raken de Lakers door vermoeidheid hun schot kwijt, dan blijft het totaal eronder. Meer uitleg lees je in onze gidsen over <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap wedden</a> en de <a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">money line</a>.</p>
<h3><strong>Clippers – Lakers live kijken in Nederland</strong></h3>
<p>Bij <a href="/bookmakers/bet365">Bet365</a> kun je NBA-wedstrijden live volgen via de livestream. Je hebt daarvoor een account met een storting nodig. ESPN zendt in Nederland een deel van de NBA-wedstrijden uit; in de programmagids zie je of deze erbij zit. Met <strong>NBA League Pass</strong>, de betaalde dienst van de competitie, kun je alle wedstrijden volgen. Meer opties vind je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk Clippers – Lakers live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Vannacht voorspellen we ook <a href="/nieuws/pacers-76ers-voorspelling-wedtips-nba-2026">Pacers – 76ers</a>, <a href="/nieuws/bucks-rockets-voorspelling-wedtips-nba-2026">Bucks – Rockets</a> en <a href="/nieuws/mavericks-thunder-voorspelling-wedtips-nba-2026">Mavericks – Thunder</a>. Alle wedstrijden en onze beste tips staan in de <a href="/nieuws/nba-voorspellingen-vannacht-29-oktober-2026">NBA-voorspellingen van 29 oktober</a>. Eerder schreven we over beide ploegen in <a href="/nieuws/lakers-trail-blazers-voorspelling-wedtips-nba-2026">Lakers – Trail Blazers</a> en <a href="/nieuws/thunder-clippers-voorspelling-wedtips-nba-2026">Thunder – Clippers</a>. Benieuwd <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">welke Nederlanders in de NBA spelen</a>? Nieuw met basketbal? Lees <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels in de NBA</a>. Alle tips staan op <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Clippers – Lakers?</strong><br>Donderdag 29 oktober 2026 om 03:30 Nederlandse tijd, in de nacht van woensdag op donderdag. In Los Angeles is het dan woensdagavond 19:30.</p>
<p><strong>Speelt Luka Dončić mee?</strong><br>Naar verwachting wel. Hij speelde dinsdag 37 minuten tegen Portland en stond toen niet op de blessurelijst. De Lakers hadden hun lijst voor deze wedstrijd woensdagochtend nog niet ingeleverd. Dončić scoort dit seizoen 36 punten per duel.</p>
<p><strong>Wie is favoriet: Clippers of Lakers?</strong><br>De Lakers, met een quotering van 1,54 bij TOTO. De Clippers staan op 2,55.</p>
<p><strong>Wat is onze voorspelling voor Clippers – Lakers?</strong><br>De Lakers winnen met 113-119. Onze wedtip is Over 228,5 punten, inclusief verlenging (1,87 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

KAART = {"home": "Clippers", "away": "Lakers", "home_abbr": "lac", "away_abbr": "lal", "home_pos": "42-40 · nr. 9 West 2025/26", "away_pos": "53-29 · nr. 4 West 2025/26", "hs": 113, "as": 119, "datum": "Do 29 okt", "tijd": "03:30", "odd_home": "2,55", "odd_away": "1,54"}
WEDTIPS = {"wedtip-1-2": "Over 228,5 punten (incl. verlenging)", "quotering-wedtip-1": "1.87",
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
    assert not re.search(r"<(ul|ol|li)\b", html), "geen lijsten"
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"), "slotregel"
    # SEO: focuskeyword
    fk = "Clippers – Lakers voorspelling"
    assert fk in TITEL and fk in SAMENVATTING and len(SAMENVATTING) <= 160
    assert re.sub(r"<[^>]+>", "", content).startswith(fk), "focuskeyword in eerste zin intro"
    assert any(fk in h for h in re.findall(r"<h3>(.*?)</h3>", html)), "focuskeyword in een h3"
    # Links
    hrefs = re.findall(r'href="([^"]+)"', html)
    assert hrefs and all(h.startswith("/") or h == BET365 for h in hrefs), [h for h in hrefs if not h.startswith("/")]
    assert SLUG not in "".join(hrefs), "niet naar zichzelf linken"
    toegestaan = {"/nieuws/nba-voorspellingen-vannacht-29-oktober-2026", "/nieuws/nba-voorspellingen-vannacht-27-oktober-2026",
                  "/nieuws/nba-voorspellingen-vannacht-26-oktober-2026",
                  "/nieuws/pacers-76ers-voorspelling-wedtips-nba-2026", "/nieuws/bucks-rockets-voorspelling-wedtips-nba-2026",
                  "/nieuws/mavericks-thunder-voorspelling-wedtips-nba-2026",
                  "/nieuws/lakers-trail-blazers-voorspelling-wedtips-nba-2026", "/nieuws/lakers-warriors-voorspelling-wedtips-nba-2026",
                  "/nieuws/thunder-suns-voorspelling-wedtips-nba-2026", "/nieuws/thunder-clippers-voorspelling-wedtips-nba-2026",
                  "/nieuws/rockets-hawks-voorspelling-wedtips-nba-2026", "/nieuws/heat-mavericks-voorspelling-wedtips-nba-2026",
                  "/nieuws/76ers-pistons-voorspelling-wedtips-nba-2026", "/nieuws/knicks-pistons-voorspelling-wedtips-nba-2026",
                  "/nieuws/spurs-kings-voorspelling-wedtips-nba-2026", "/nieuws/celtics-nets-voorspelling-wedtips-nba-2026",
                  "/nieuws/welke-nederlanders-spelen-in-de-nba",
                  "/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders",
                  "/nieuws/wat-is-handicap-wedden-de-complete-gids",
                  "/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners",
                  "/wedden-op-nba-voorspellingen-en-wedtips---basketbal", "/bookmakers/toto", "/bookmakers/bet365",
                  "/live-kijken", BET365}
    assert set(hrefs) <= toegestaan, set(hrefs) - toegestaan
    for s in ("pacers-76ers", "bucks-rockets", "mavericks-thunder", "nba-voorspellingen-vannacht-29-oktober-2026"):
        assert any(s in h for h in hrefs), f"link naar {s} ontbreekt"
    assert sum(h == BET365 for h in hrefs) == 2, "één wed-CTA en één kijk-CTA, zoals het sjabloon"
    assert "<table" not in html.replace(f"<table {T}>", ""), "tabellen alleen via tabel()"
    verboden = ["BetCity", "ESPN-API", "ESPN.com", "Associated Press", "DraftKings", "Rotowire", "Betfans", "Unibet",
                "Holland Casino", "Jacks.nl"]
    assert not any(v.lower() in html.lower() for v in verboden), "geen bronnen/concurrenten"
    # Wedtip en consistentie
    assert set(WEDTIPS) == {"wedtip-1-2", "quotering-wedtip-1", "bookmaker-wedtips"}
    assert WEDTIPS["bookmaker-wedtips"] == "669ab9f5aceb8b717cea24c3"
    q = float(WEDTIPS["quotering-wedtip-1"])
    toto_odds = {2.55, 1.54, 2.60, 18.0, 1.53, 1.95, 1.73, 1.91, 1.87, 1.93, 1.78}
    assert q == 1.87 and q in toto_odds
    assert KAART["hs"] + KAART["as"] > 228.5, "voorspelde score moet Over 228,5 laten winnen"
    assert KAART["as"] > KAART["hs"], "voorspelling: Lakers winnen (favoriet bij TOTO)"
    assert f"{KAART['hs']}-{KAART['as']}" in content and f"{KAART['hs']}-{KAART['as']}" in content3
    assert KAART["odd_home"] == "2,55" and KAART["odd_away"] == "1,54" and KAART["tijd"] == "03:30"
    assert KAART["home_abbr"] == "lac" and KAART["away_abbr"] == "lal" and KAART["datum"] == "Do 29 okt"
    assert "228,5" in content and "1,87" in content and "1,87" in content3
    assert "Under" not in WEDTIPS["wedtip-1-2"], "nooit een under als tip"
    assert "woensdag rond 10:50 uur" in content2, "tijdstip odds"
    assert SLUG == "clippers-lakers-voorspelling-wedtips-nba-2026" and DATUM == "2026-10-29T02:30:00.000Z"
    assert datetime.fromisoformat(DATUM.replace("Z", "+00:00")).hour == 2, "03:30 CET = 02:30 UTC"
    # FAQ: 4 vragen
    assert len(re.findall(r"<p><strong>[^<]*\?</strong><br>", content3)) == 4, "4 FAQ-vragen"
    tekst = re.sub(r"<[^>]+>", " ", html)
    print(len(TITEL), "tekens titel |", len(SAMENVATTING), "tekens samenvatting |", len(tekst.split()), "woorden")
    print("Alle asserts geslaagd (dry run, niets gepubliceerd).")
