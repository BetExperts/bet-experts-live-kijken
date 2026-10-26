# -*- coding: utf-8 -*-
"""Los artikel: Nuggets – Warriors voorspelling, NBA 27 oktober 2026 (03:00 NL, wintertijd; maandag 20:00 MT), Ball Arena Denver.
Feiten nagelopen op 26-10-2026 (ESPN-API: summary 401909876, boxscores 401909094, 401909859, 401909092, 401909850
en 401909860, teamschema's 2025/26 (incl. play-offs en play-in) en 2026/27, rosters en coaches, standen 2025/26,
spelersgemiddelden, onderlinge duels 2025/26 (401809237, 401809779, 401810675, 401810945); officiële NBA-blessurelijst
26-10 07:30 ET; berichtgeving na Suns-Warriors (Curry, Green, Podziemski en Horford kregen rust; Curry officieel
'rechterknie'); selectiewijzigingen zoals eerder nagelopen in specials/thunder_nuggets_nba_2026.py en lakers_warriors).
- Nuggets: 84-96 in Oklahoma City (31/82 uit het veld, 22 balverliezen), 141-135 n.v. tegen New Orleans
  (108-89 achter na drie kwarten, 37-18 in het vierde; Murray 42, Jokić 35/15/10).
- Warriors: 105-127 bij de Lakers, 108-111 tegen Memphis, 122-131 in Phoenix zonder Curry/Green/Podziemski/Horford.
- Onderling 2025/26: 2-2. In San Francisco 137-131 n.v. en 128-117 voor GSW, in Denver 129-104 en 116-93 voor DEN.
  Stephen Curry speelde alleen het eerste duel (42 punten).
- Beide ploegen speelden zaterdag (US) en hadden zondag rust; geen back-to-back.
- Odds: alleen TOTO, uit specials/nba_feiten_2026_10_27.md (±12:45 NL op 26-10). Handicap en totaal incl. verlenging.
- Eén wedtip (eis eigenaar): Nuggets -6,5 @1,69, onze kans 62% (markt 59,2%, zonder marge ±54%).
  python3 specials/nuggets_warriors_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "Nuggets – Warriors voorspelling: wedtip en odds voor Jokić tegen een winloos Golden State (27 oktober, 03:00)"
SLUG = "nuggets-warriors-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("Denver ontvangt een Golden State dat nog niet won en zonder Porziņģis en Moody speelt. Voorspelling, "
                "onze wedtip, TOTO-odds, blessures en opstellingen.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet-experts.nl/go/bet365"
DATUM = "2026-10-27T02:00:00.000Z"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>In de nacht van maandag op dinsdag om 03:00 Nederlandse tijd ontvangen de Denver Nuggets de Golden State Warriors in Ball Arena. Denver staat op één zege en één nederlaag, Golden State verloor alle drie de wedstrijden. Stephen Curry is na een rustbeurt in Phoenix weer terug, maar Kristaps Porziņģis en Moses Moody ontbreken nog altijd. Onze voorspelling: Nuggets – Warriors 121-110. Onze wedtip: Denver Nuggets -6,5 punten (inclusief verlenging) tegen een quotering van 1,69 bij TOTO.</strong></p>
<p>Hieronder lees je alles over vorm, blessures, de odds van <a href="/bookmakers/toto">TOTO</a> en onze onderbouwing.</p>
<h3><strong>Nuggets – Warriors: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "Denver Nuggets – Golden State Warriors"),
    ("Datum", "Dinsdag 27 oktober 2026 (nacht van maandag op dinsdag)"),
    ("Aanvang", "03:00 Nederlandse tijd (maandag 20:00 in Denver)"),
    ("Arena", "Ball Arena, Denver"),
    ("Competitie", "NBA, reguliere competitie 2026/27"),
    ("Stand 2026/27", "Nuggets 1-1, Warriors 0-3"),
    ("Onderlinge duels 2025/26", "2-2 (Denver won beide thuisduels)"),
])}
<p>Beide ploegen speelden zaterdag (Amerikaanse tijd) en hadden zondag een rustdag. Van een back-to-back is dus geen sprake. Golden State speelt woensdag pas weer, in Minneapolis.</p>
<h3><strong>De eerste week: Denver herstelt, Golden State zoekt een zege</strong></h3>
<p><strong>Denver Nuggets: een slechte avond en een grote ommekeer</strong></p>
<p>Denver begon in Oklahoma City met een 84-96 nederlaag. De Nuggets raakten maar 31 van hun 82 schoten en verloren de bal 22 keer. Nikola Jokić scoorde 13 punten (5 van 19), Jamal Murray maar 6 (2 van 11). Zaterdag volgde de thuisopener tegen New Orleans, en ook die leek mis te gaan. Na drie kwarten stond Denver met 89-108 achter. Een vierde kwart van 37-18 dwong een verlenging af, die de Nuggets met 15-9 wonnen: 141-135. Murray maakte 42 punten, met 8 van de 16 driepunters raak. Jokić had een triple-double van 35 punten, 15 rebounds en 10 assists. Verdedigend ging het mis: New Orleans scoorde 70 punten in de bucket.</p>
<p><strong>Golden State Warriors: drie nederlagen, één met een B-ploeg</strong></p>
<p>Golden State verloor de opener met 105-127 bij de Lakers. Curry scoorde 23 punten in 21 minuten, maar de ploeg raakte maar 8 van de 36 driepunters. Vrijdag gaven de Warriors tegen Memphis in de slotminuten een voorsprong van twaalf punten weg: 108-111. Een dag later in Phoenix kregen Curry, Draymond Green, Brandin Podziemski en Al Horford rust. Rookie Yaxel Lendeborg (26 punten) en De'Anthony Melton (25) hielden de reserves lang in de wedstrijd, maar Devin Booker maakte er 43: 131-122. Golden State kreeg in drie duels gemiddeld 123 punten tegen.</p>
<h3><strong>Vorig seizoen en de onderlinge duels</strong></h3>
<p>Denver werd derde in het Westen en had de beste aanval van de NBA, maar ging in de eerste ronde van de play-offs met 2-4 onderuit tegen Minnesota. Golden State werd tiende, won in de play-in bij de Clippers (126-121) en verloor daarna in Phoenix (96-111).</p>
{tabel(["2025/26", "Denver Nuggets", "Golden State Warriors"], [
    ("Eindstand", "54-28 (nr. 3 West)", "37-45 (nr. 10 West)"),
    ("Thuis / uit", "28-13 / 26-15", "22-19 / 15-26"),
    ("Punten voor / tegen", "122,1 / 116,9", "114,6 / 115,2"),
    ("Na het seizoen", "Eerste ronde (2-4 tegen Minnesota)", "Uitgeschakeld in de play-in"),
])}
<p>De vier onderlinge duels eindigden in 2-2, en elke ploeg won zijn thuisduels. In San Francisco won Golden State in oktober met 137-131 na verlenging (Curry 42 punten, Aaron Gordon 50) en in februari met 128-117. In Denver was het twee keer eenzijdig: 129-104 in november en 116-93 in maart. Een kanttekening: Curry speelde alleen het eerste duel mee. Jokić kwam in de vier wedstrijden gemiddeld tot bijna 27 punten, 14 rebounds en 10 assists.</p>"""

content2 = f"""<h3><strong>Zo zijn beide selecties veranderd</strong></h3>
<p><strong>Denver Nuggets: dezelfde kern, een nieuwe bank</strong></p>
<p>Coach David Adelman houdt de kern rond Jokić, Murray, Gordon en Christian Braun bij elkaar. Peyton Watson vertrok in een sign-and-trade naar Cleveland, Tim Hardaway Jr. tekende bij Miami en ook Jonas Valančiūnas en Bruce Brown zijn weg. De 37-jarige DeMar DeRozan kwam over van Sacramento, en ook Marvin Bagley III, Alpha Diallo en Trevon Brazile kwamen erbij.</p>
<p><strong>Golden State Warriors: oud, en voorlopig kort</strong></p>
<p>Steve Kerr begint aan zijn dertiende seizoen als coach. Green, Horford en Porziņģis tekenden opnieuw, Jonathan Kuminga speelt inmiddels voor Minnesota en Quinten Post voor Memphis. De grootste nieuwkomer is Lendeborg, de nummer elf van de draft, die met 18,7 punten en 8,3 rebounds direct de tweede scorer is. Curry (38), Green (36) en Horford (40) krijgen geregeld rust.</p>
<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("Jimmy Butler", "Golden State", "Speelt niet (herstel van kruisbandoperatie)"),
    ("Moses Moody", "Golden State", "Speelt niet (herstel van knieoperatie)"),
    ("Kristaps Porziņģis", "Golden State", "Speelt niet (niet bij de ploeg)"),
    ("Gui Santos", "Golden State", "Twijfelachtig (peesontsteking linkerknie)"),
    ("Brandon Williams, Charles Bassey", "Golden State", "Waarschijnlijk inzetbaar (rug, knie)"),
    ("Cameron Johnson", "Denver", "Zeer twijfelachtig (verstuikte rechterenkel)"),
    ("Alpha Diallo", "Denver", "Zeer twijfelachtig (pols, persoonlijke redenen)"),
    ("Spencer Jones, Julian Strawther", "Denver", "Spelen niet (hamstrings, knie)"),
])}
<p><em>Stand van de officiële NBA-blessurelijst op maandag 26 oktober, 12:30 Nederlandse tijd.</em></p>
<p>Curry, Green, Podziemski en Horford staan niet op de lijst en zijn dus inzetbaar. Curry miste het duel in Phoenix omdat hij rust kreeg op de tweede avond van een back-to-back.</p>
<p><strong>Verwachte basisvijf Denver:</strong> Jamal Murray, Christian Braun, Bryce Hopkins, Aaron Gordon, Nikola Jokić. Dat was de vijf van zaterdag; Cameron Johnson miste die wedstrijd al met zijn enkel. DeRozan, Brazile en Bagley zijn de belangrijkste wissels.</p>
<p><strong>Verwachte basisvijf Golden State:</strong> Stephen Curry, Brandin Podziemski, Yaxel Lendeborg, Graham Ike, Draymond Green. Zo begon Golden State tegen Memphis. Melton, Horford, Gary Payton II en Georges Niang zijn de belangrijkste wissels. Kerr maakt zijn basisvijf pas kort voor de wedstrijd bekend.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "2026/27 tot nu toe"], [
    ("Nikola Jokić (DEN)", "27,7", "12,9", "10,7", "24 ptn, 11 reb, 7,5 ast"),
    ("Jamal Murray (DEN)", "25,4", "4,4", "7,1", "24 ptn, 8 van 17 driepunters"),
    ("Aaron Gordon (DEN)", "16,2", "5,8", "2,7", "13,5 ptn"),
    ("Stephen Curry (GSW)", "26,6", "3,6", "4,7", "23,5 ptn in 2 duels"),
    ("Brandin Podziemski (GSW)", "13,8", "5,1", "3,7", "18 ptn in 1 duel"),
    ("Yaxel Lendeborg (GSW)", "18,7*", "8,3*", "4,3*", "Rookie, 44% driepunters"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26. * Lendeborg: 2026/27. Curry speelde vorig seizoen 43 wedstrijden, Gordon 36.</em></p>
<p><strong>Nikola Jokić</strong> had in Oklahoma City een zeldzaam slechte avond, maar liet zaterdag zien wat hij doet als hij de ruimte krijgt. <strong>Jamal Murray</strong> scoorde vorig seizoen in alle vier de duels met de Warriors 20 punten of meer. <strong>Stephen Curry</strong> is uitgerust, maar raakte dit seizoen nog maar 29 procent van zijn driepunters.</p>
<h3><strong>Odds Nuggets – Warriors bij TOTO</strong></h3>
<p>TOTO ziet Denver als duidelijke favoriet: een quotering van 1,34 staat voor ongeveer 75 procent winkans. De handicap ligt rond de 7,5 punten in het voordeel van de Nuggets, het verwachte puntentotaal rond de 233 punten.</p>
{tabel(["Markt (TOTO)", "Nuggets", "Warriors"], [
    ("Winnaar (incl. verlenging)", "1,34", "3,35"),
    ("1X2 (reguliere speeltijd, gelijk 18,00)", "1,33", "3,65"),
    ("Handicap -6,5 / +6,5 (incl. verlenging)", "1,69", "2,00"),
    ("Handicap -7,5 / +7,5 (incl. verlenging)", "1,87", "1,93"),
    ("Handicap -8,5 / +8,5 (incl. verlenging)", "2,00", "1,80"),
])}
<p>Op het totaal biedt TOTO 232,5 punten (Over 1,73 / Under 1,95), 233,5 (1,87 / 1,93) en 234,5 (Over 1,87 / Under 1,78). Odds gelezen op maandag rond 12:45 uur; vergelijk ze vlak voor de start nog even.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op Nuggets – Warriors</strong></a></p>"""

content3 = f"""<h3><strong>Onze voorspelling: Denver wint met ruim verschil</strong></h3>
<p>Denver heeft de twee beste spelers op het veld en speelt thuis. De Warriors zijn met Curry, Green en Podziemski sterker dan in Phoenix, maar zonder Porziņģis, Moody en Butler is de rotatie kort en ontbreekt lengte onder de ring. Golden State kreeg in alle drie de duels meer dan 110 punten tegen.</p>
<p>Denver moet verdedigend wel beter dan tegen New Orleans. Toch verwachten we, net als in de twee duels in Denver van vorig seizoen, een duidelijke thuiszege. Onze voorspelling: <strong>Denver Nuggets – Golden State Warriors 121-110</strong>.</p>
<h3><strong>Onze wedtip: Nuggets -6,5 (1,69)</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Onze kans"], [
    ("Denver Nuggets -6,5 punten (incl. verlenging)", "1,69", "TOTO", "Ongeveer 62 procent"),
])}
<p><strong>Waarom deze tip?</strong> De tip is goed als Denver met zeven punten of meer verschil wint. Een odd van 1,69 staat voor een kans van 59 procent; zonder de marge van de bookmaker is dat ongeveer 54 procent. Wij schatten de kans op ongeveer 62 procent. De onderbouwing:</p>
<p><strong>1. Jokić en Murray thuis, op hoogte.</strong> Denver won vorig seizoen 28 van zijn 41 thuisduels, en Ball Arena ligt op ruim 1.600 meter. In de twee thuisduels met Golden State wonnen de Nuggets met 25 en 23 punten verschil. Zaterdag kantelden Jokić en Murray samen nog een wedstrijd.</p>
<p><strong>2. Golden State mist lengte en diepte.</strong> Porziņģis is niet bij de ploeg, Moody en Butler herstellen van een operatie en Santos is twijfelachtig. Daardoor staan Green (36) en Horford (40) tegenover Jokić onder de ring. Phoenix en de Lakers scoorden tegen de Warriors 60 en 66 punten in de bucket.</p>
<p><strong>3. Curry is terug, maar speelt beperkt.</strong> Kerr bewaakt de minuten van zijn 38-jarige ster: Curry speelde 21 en 30 minuten in zijn twee duels en raakte maar 5 van de 17 driepunters. Zodra hij rust, heeft Golden State weinig scorend vermogen: buiten Curry en Lendeborg kwam nog niemand aan 15 punten per wedstrijd, op Podziemski na, die pas één duel speelde.</p>
<p><strong>Waarom niet een andere markt?</strong> Een zege van Denver (1,34) vraagt om 75 procent kans. Wij komen uit op ongeveer 77 procent; dat verschil is te klein voor zo'n lage odd. Bij Nuggets -7,5 (1,87) en -8,5 (2,00) heb je minder ruimte: onze voorspelde marge van elf punten ligt daar dicht tegenaan, en zaterdag stond Denver tegen New Orleans nog met 23 punten achter. Het puntentotaal laten we liggen. Onze voorspelling komt uit op 231 punten, vlak onder de lijn, en de twee wedstrijden van Denver eindigden op 180 en 276 punten.</p>
<p><strong>Het risico.</strong> Denver liet tegen New Orleans 135 punten en 70 punten in de bucket toe, en Cameron Johnson ontbreekt waarschijnlijk. In Phoenix toonde een Golden State zonder vier vaste spelers bovendien veel veerkracht. Krijgt Curry het warm, zoals bij zijn 42 punten in oktober vorig jaar, dan kan het spannend blijven. Let ook op: de handicap telt een eventuele verlenging mee. Meer uitleg vind je in onze gidsen over <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap wedden</a> en de <a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">money line</a>.</p>
<h3><strong>Nuggets – Warriors live kijken in Nederland</strong></h3>
<p>Bij <a href="/bookmakers/bet365">Bet365</a> kun je NBA-wedstrijden live volgen via de livestream. Je hebt daarvoor een account met een storting nodig. ESPN zendt in Nederland een deel van de NBA-wedstrijden uit; in de programmagids zie je of deze erbij zit. Met <strong>NBA League Pass</strong>, de betaalde dienst van de competitie, kun je alle wedstrijden volgen. Meer opties vind je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk Nuggets – Warriors live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Lees ook onze voorspellingen voor <a href="/nieuws/thunder-suns-voorspelling-wedtips-nba-2026">Thunder – Suns</a>, <a href="/nieuws/cavaliers-timberwolves-voorspelling-wedtips-nba-2026">Cavaliers – Timberwolves</a> en <a href="/nieuws/rockets-hawks-voorspelling-wedtips-nba-2026">Rockets – Hawks</a>, en alle <a href="/nieuws/nba-voorspellingen-vannacht-27-oktober-2026">NBA-voorspellingen van 27 oktober</a>. Benieuwd <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">welke Nederlanders in de NBA spelen</a>? Malevy Leons zit met een two-waycontract bij Golden State. Nieuw met basketbal? Lees <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels in de NBA</a>. Alle tips staan op <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Nuggets – Warriors?</strong><br>Dinsdag 27 oktober 2026 om 03:00 Nederlandse tijd, in de nacht van maandag op dinsdag. In Denver is het dan maandagavond 20:00.</p>
<p><strong>Speelt Stephen Curry mee?</strong><br>Naar verwachting wel. Curry staat niet op de officiële blessurelijst. Hij miste zaterdag het duel in Phoenix omdat hij rust kreeg op de tweede avond van een back-to-back.</p>
<p><strong>Wie is favoriet: Nuggets of Warriors?</strong><br>Denver, met een quotering van 1,34 bij TOTO. Golden State staat op 3,35.</p>
<p><strong>Wat is onze voorspelling voor Nuggets – Warriors?</strong><br>Denver wint met 121-110. Onze wedtip is Denver Nuggets -6,5 punten, inclusief verlenging (1,69 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

KAART = {"home": "Nuggets", "away": "Warriors", "home_abbr": "den", "away_abbr": "gs", "home_pos": "54-28 · nr. 3 West 2025/26", "away_pos": "37-45 · nr. 10 West 2025/26", "hs": 121, "as": 110, "datum": "Di 27 okt", "tijd": "03:00", "odd_home": "1,34", "odd_away": "3,35"}
WEDTIPS = {"wedtip-1-2": "Denver Nuggets -6,5 punten (incl. verlenging)", "quotering-wedtip-1": "1.69",
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
    toegestaan = {"/nieuws/nba-voorspellingen-vannacht-26-oktober-2026", "/nieuws/nba-voorspellingen-vannacht-25-oktober-2026",
                  "/nieuws/nba-voorspellingen-vannacht-24-oktober-2026",
                  "/nieuws/thunder-clippers-voorspelling-wedtips-nba-2026", "/nieuws/jazz-lakers-voorspelling-wedtips-nba-2026",
                  "/nieuws/76ers-pistons-voorspelling-wedtips-nba-2026", "/nieuws/hawks-rockets-voorspelling-wedtips-nba-2026",
                  "/nieuws/thunder-nuggets-voorspelling-wedtips-nba-2026", "/nieuws/lakers-warriors-voorspelling-wedtips-nba-2026",
                  "/nieuws/76ers-cavaliers-voorspelling-wedtips-nba-2026",
                  "/nieuws/welke-nederlanders-spelen-in-de-nba",
                  "/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders",
                  "/nieuws/wat-is-handicap-wedden-de-complete-gids",
                  "/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners",
                  "/wedden-op-nba-voorspellingen-en-wedtips---basketbal", "/bookmakers/toto", "/bookmakers/bet365",
                  "/live-kijken", BET365,
                  "/nieuws/cavaliers-timberwolves-voorspelling-wedtips-nba-2026",
                  "/nieuws/heat-mavericks-voorspelling-wedtips-nba-2026",
                  "/nieuws/thunder-suns-voorspelling-wedtips-nba-2026",
                  "/nieuws/rockets-hawks-voorspelling-wedtips-nba-2026",
                  "/nieuws/nba-voorspellingen-vannacht-27-oktober-2026"}
    assert set(hrefs) <= toegestaan, set(hrefs) - toegestaan
    assert "/nieuws/nba-voorspellingen-vannacht-27-oktober-2026" in hrefs, "link naar algemeen artikel van vannacht"
    vannacht = {"/nieuws/cavaliers-timberwolves-voorspelling-wedtips-nba-2026", "/nieuws/heat-mavericks-voorspelling-wedtips-nba-2026",
                "/nieuws/thunder-suns-voorspelling-wedtips-nba-2026", "/nieuws/rockets-hawks-voorspelling-wedtips-nba-2026"}
    assert 2 <= len(vannacht & set(hrefs)) <= 4, "2-4 andere voorbeschouwingen van vannacht"
    assert SLUG not in "".join(hrefs), "geen link naar zichzelf"
    assert "<table" not in html.replace(f"<table {T}>", ""), "tabellen alleen via tabel()"
    verboden = ["BetCity", "ESPN-API", "ESPN.com", "Associated Press", "DraftKings", "Rotowire", "Betfans"]
    assert not any(v.lower() in html.lower() for v in verboden), "geen bronnen/concurrenten"
    # Wedtip en consistentie
    assert set(WEDTIPS) == {"wedtip-1-2", "quotering-wedtip-1", "bookmaker-wedtips"}
    assert WEDTIPS["bookmaker-wedtips"] == "669ab9f5aceb8b717cea24c3"
    q = float(WEDTIPS["quotering-wedtip-1"])
    toto_odds = {1.34, 3.35, 1.33, 18.0, 3.65, 2.00, 1.80, 1.87, 1.93, 1.69, 1.73, 1.95, 1.78}
    assert q in toto_odds and q == 1.69 and q >= 1.40
    assert KAART["hs"] - 6.5 > KAART["as"], "voorspelde score moet Nuggets -6,5 laten winnen"
    assert KAART["hs"] > KAART["as"], "voorspelling: Nuggets winnen"
    assert f"{KAART['hs']}-{KAART['as']}" in content and f"{KAART['hs']}-{KAART['as']}" in content3
    assert KAART["odd_home"] == "1,34" and KAART["odd_away"] == "3,35" and KAART["tijd"] == "03:00"
    assert KAART["home_abbr"] == "den" and KAART["away_abbr"] == "gs" and KAART["datum"] == "Di 27 okt"
    assert "1,69" in content and "1,69" in content3
    assert "12:45" in content2, "tijdstip odds"
    assert SLUG == "nuggets-warriors-voorspelling-wedtips-nba-2026" and DATUM == "2026-10-27T02:00:00.000Z"
    assert html.count(BET365) == 2
    tekst = re.sub(r"<[^>]+>", " ", html)
    print(len(TITEL), "tekens titel |", len(SAMENVATTING), "tekens samenvatting |", len(tekst.split()), "woorden")
    print("Alle asserts geslaagd (dry run, niets gepubliceerd).")
