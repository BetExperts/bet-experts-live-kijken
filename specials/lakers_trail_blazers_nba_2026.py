# -*- coding: utf-8 -*-
"""Los artikel: Lakers – Trail Blazers voorspelling, NBA 28 oktober 2026 (04:00 NL, wintertijd; dinsdag 20:00 PT),
Crypto.com Arena Los Angeles. Feiten nagelopen op 27-10-2026 (ESPN-API: summary 401909880, boxscores 401909092,
401909851, 401909861, 401909841 en 401909852, teamschema's 2025/26 en 2026/27, play-in 401866754, play-offs,
rosters en coaches, standen 2025/26, spelersgemiddelden 2025/26, onderlinge duels 2025/26 (401809977, 401810018,
401810456); officiële NBA-blessurelijst 27-10 05:45 ET; berichtgeving over de ruil Morant (29-6-2026, voor Grant en
Kris Murray), de aanstelling van coach Micah Nori (23-6-2026), de ruil Holiday-Simons (juni 2025) en de terugkeer
van Lillard na zijn achillespees (gescheurd april 2025, heel 2025/26 gemist)).
- Lakers 2026/27: 127-105 Warriors, 125-117 Clippers, 132-123 in Utah (Dončić 52/8/10). Totalen 232, 242, 255.
- Portland 2026/27: 124-83 Suns (Lillard 25, Morant debuut 14/8), 128-120 in Sacramento (Avdija 26, Camara 19).
- Onderling 2025/26: 108-122 en 116-132 (Portland), 123-115 in Portland (Lakers). Dončić speelde in geen van de drie.
- Portland rust sinds vrijdag (US); de Lakers spelen woensdag (US) alweer, bij de Clippers (back-to-back).
- Odds: alleen TOTO, uit specials/nba_feiten_2026_10_28.md (±10:45 NL op 27-10). Handicap en totaal incl. verlenging.
- Eén wedtip (eis eigenaar): Over 236,5 punten @1,91, onze kans 56% (markt 52,4%, zonder marge 50%).
  python3 specials/lakers_trail_blazers_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "Lakers – Trail Blazers voorspelling: wedtip en odds voor twee ongeslagen ploegen (28 oktober, 04:00)"
SLUG = "lakers-trail-blazers-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("Lakers – Trail Blazers voorspelling: Dončić en Reaves tegen Lillard en Morant. Onze wedtip, TOTO-odds, "
                "blessures en opstellingen.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet-experts.nl/go/bet365"
DATUM = "2026-10-28T03:00:00.000Z"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>Lakers – Trail Blazers voorspelling: in de nacht van dinsdag op woensdag ontvangen de Los Angeles Lakers om 04:00 Nederlandse tijd de Portland Trail Blazers in de Crypto.com Arena. Het is het enige duel van de nacht tussen twee ongeslagen ploegen: de Lakers wonnen hun eerste drie wedstrijden, Portland de eerste twee. Luka Dončić en Austin Reaves treffen een Portland dat met Damian Lillard en Ja Morant een compleet nieuw achterveld heeft. Onze voorspelling: Lakers – Trail Blazers 122-117. Onze wedtip: Over 236,5 punten (inclusief verlenging) tegen een quotering van 1,91 bij TOTO.</strong></p>
<p>Hieronder lees je alles over vorm, blessures, de odds van <a href="/bookmakers/toto">TOTO</a> en onze onderbouwing.</p>
<h3><strong>Lakers – Trail Blazers: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "Los Angeles Lakers – Portland Trail Blazers"),
    ("Datum", "Woensdag 28 oktober 2026 (nacht van dinsdag op woensdag)"),
    ("Aanvang", "04:00 Nederlandse tijd (dinsdag 20:00 in Los Angeles)"),
    ("Arena", "Crypto.com Arena, Los Angeles"),
    ("Competitie", "NBA, reguliere competitie 2026/27"),
    ("Stand 2026/27", "Lakers 3-0, Trail Blazers 2-0"),
    ("Onderlinge duels 2025/26", "2-1 voor Portland"),
])}
<p>Omdat de klok in de Verenigde Staten pas op 1 november teruggaat, is het verschil met Los Angeles deze week acht uur. Portland speelde vrijdag (Amerikaanse tijd) voor het laatst en heeft drie rustdagen achter de rug. De Lakers hadden maandag vrij en spelen woensdag alweer, bij de Clippers.</p>
<h3><strong>De eerste week: twee ploegen die makkelijk scoren</strong></h3>
<p><strong>Los Angeles Lakers: drie zeges, 128 punten per duel</strong></p>
<p>De ploeg van coach JJ Redick versloeg Golden State met 127-105 en de Clippers met 125-117. Zondag volgde de eerste uitwedstrijd, in Utah: 132-123. Dončić had daar 52 punten, 10 assists en 8 rebounds, met 17 van zijn 30 schoten raak en 8 driepunters. Reaves voegde er 29 punten aan toe. Gemiddeld scoren de Lakers 128 punten, en hun drie wedstrijden eindigden op 232, 242 en 255 punten in totaal. Achterin liep het aantal tegenpunten op van 105 naar 117 en 123.</p>
<p><strong>Portland Trail Blazers: overtuigende start met nieuwe gezichten</strong></p>
<p>Portland opende thuis met 124-83 tegen Phoenix. Lillard maakte 25 punten, met 6 driepunters, in zijn eerste competitieduel voor Portland sinds maart 2023. Morant debuteerde met 14 punten en 8 assists. Vrijdag won Portland met 128-120 in Sacramento, met 26 punten van Deni Avdija en 19 van Toumani Camara. Een kanttekening: Phoenix scoorde maar 83 punten, en Sacramento verloor ook zijn andere twee wedstrijden. De 101,5 tegenpunten per duel van Portland zeggen dus nog weinig.</p>
<h3><strong>Vorig seizoen en de onderlinge duels</strong></h3>
<p>De Lakers wonnen 53 wedstrijden, versloegen Houston in de eerste ronde van de play-offs (4-2) en gingen daarna met 0-4 onderuit tegen Oklahoma City. Portland eindigde als achtste in het Westen, won de play-inwedstrijd in Phoenix (114-110) en verloor in de eerste ronde met 1-4 van San Antonio.</p>
{tabel(["2025/26", "Los Angeles Lakers", "Portland Trail Blazers"], [
    ("Eindstand", "53-29 (nr. 4 West)", "42-40 (nr. 8 West)"),
    ("Thuis / uit", "28-13 / 25-16", "24-17 / 18-23"),
    ("Punten voor / tegen", "116,3 / 114,6", "115,5 / 115,8"),
    ("Na het seizoen", "Tweede ronde (0-4 tegen OKC)", "Eerste ronde (1-4 tegen San Antonio)"),
])}
<p>Portland won twee van de drie onderlinge duels: 122-108 in Los Angeles in oktober (ondanks 41 punten van Reaves) en 132-116 thuis in januari. Daartussen won Los Angeles in november met 123-115 in Portland. Opvallend: Dončić speelde in geen van de drie wedstrijden. Toch kwamen de duels uit op 230, 238 en 248 punten.</p>"""

content2 = f"""<h3><strong>Zo zijn beide selecties veranderd</strong></h3>
<p><strong>Portland Trail Blazers: Lillard, Morant en een nieuwe coach</strong></p>
<p>Jrue Holiday kwam in juni 2025 al over van Boston, in een ruil voor Anfernee Simons; hij speelde vorig seizoen 53 wedstrijden voor Portland. Lillard keerde in de zomer van 2025 terug, maar miste het hele seizoen met de achillespees die hij in april 2025 in de play-offs met Milwaukee scheurde. De grote zomeraanwinst is Morant: Portland haalde hem op 29 juni uit Memphis, in ruil voor Jerami Grant en Kris Murray. Op de bank zit Micah Nori, sinds juni de nieuwe hoofdcoach. Hij was eerste assistent in Minnesota en volgde interim-coach Tiago Splitter op. Matisse Thybulle vertrok naar Los Angeles en speelt vannacht dus tegen zijn oude club.</p>
<p><strong>Los Angeles Lakers: alles om Dončić</strong></p>
<p>LeBron James tekende bij Philadelphia, en ook Rui Hachimura, Deandre Ayton, Marcus Smart en Jaxson Hayes vertrokken. Daarvoor kwamen Walker Kessler, Quentin Grimes, Collin Sexton, Kevon Looney en Thybulle.</p>
<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("Shaedon Sharpe", "Portland", "Speelt niet (operatie aan de meniscus, rechterknie)"),
    ("Scoot Henderson", "Portland", "Twijfelachtig (pijnlijke linkerenkel)"),
    ("Branden Carlson", "Portland", "Twijfelachtig (hersenschuddingsprotocol)"),
    ("Jayson Kent, John Tonje, Chris Youngblood", "Portland", "Niet bij de ploeg (G League)"),
    ("Cameron Carr", "LA Lakers", "Speelt niet (schuine buikspier rechts)"),
    ("Adou Thiero", "LA Lakers", "Speelt niet (vocht in de linkerknie)"),
    ("Walker Kessler", "LA Lakers", "Inzetbaar (spalk om een vinger van de linkerhand)"),
])}
<p><em>Stand van de officiële NBA-blessurelijst op dinsdag 27 oktober, 10:45 Nederlandse tijd.</em></p>
<p><strong>Verwachte basisvijf Lakers:</strong> Luka Dončić, Austin Reaves, Matisse Thybulle, Ziaire Williams, Walker Kessler. Dezelfde vijf als in alle drie de wedstrijden. Quentin Grimes, Sandro Mamukelashvili en Collin Sexton zijn de belangrijkste wissels.</p>
<p><strong>Verwachte basisvijf Portland:</strong> Ja Morant, Damian Lillard, Deni Avdija, Toumani Camara, Donovan Clingan. Zo begon Portland beide duels. Holiday komt als eerste guard van de bank, Robert Williams III en Sidy Cissoko zijn de andere vaste wissels.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "2026/27 tot nu toe"], [
    ("Luka Dončić (LAL)", "33,5", "7,7", "8,3", "34,3 ptn, 8 ast, 52 in Utah"),
    ("Austin Reaves (LAL)", "23,3", "4,7", "5,5", "26,7 ptn, 8 van 13 driepunters"),
    ("Walker Kessler (LAL)", "14,4*", "10,8*", "3,0*", "16,7 ptn, 8 reb"),
    ("Deni Avdija (POR)", "24,2", "6,9", "6,7", "22 ptn, 8,5 reb"),
    ("Damian Lillard (POR)", "-", "-", "-", "22 ptn, 8 van 20 driepunters"),
    ("Ja Morant (POR)", "19,5*", "3,3*", "8,1*", "13 ptn, 7,5 ast"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26. * Kessler speelde vorig seizoen vijf wedstrijden voor Utah, Morant twintig voor Memphis. Lillard speelde in 2025/26 niet.</em></p>
<p><strong>Luka Dončić</strong> begint het seizoen op hetzelfde niveau als vorig jaar, al blijven de balverliezen een aandachtspunt. <strong>Deni Avdija</strong> was vorig seizoen de topscorer van Portland en krijgt nu meer ruimte doordat Lillard en Morant de bal ook kunnen dragen.</p>
<h3><strong>Odds Lakers – Trail Blazers bij TOTO</strong></h3>
<p>TOTO ziet de Lakers als lichte favoriet: een quotering van 1,71 staat voor ongeveer 58 procent winkans. De handicap ligt rond de 2,5 à 3,5 punten in het voordeel van Los Angeles, het verwachte puntentotaal op 236,5.</p>
{tabel(["Markt (TOTO)", "Lakers", "Trail Blazers"], [
    ("Winnaar (incl. verlenging)", "1,71", "2,20"),
    ("1X2 (reguliere speeltijd, gelijk 17,00)", "1,71", "2,25"),
    ("Handicap -1,5 / +1,5 (incl. verlenging)", "1,69", "2,00"),
    ("Handicap -2,5 / +2,5 (incl. verlenging)", "1,87", "1,93"),
    ("Handicap -3,5 / +3,5 (incl. verlenging)", "1,93", "1,73"),
])}
<p>Op het totaal biedt TOTO 235,5 punten (Over 1,77 / Under 1,93) en 236,5 punten (Over 1,91 / Under 1,91), allebei inclusief verlenging. Odds gelezen op dinsdag rond 10:45 uur; vergelijk ze vlak voor de start nog even.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op Lakers – Trail Blazers</strong></a></p>"""

content3 = f"""<h3><strong>Onze voorspelling: Lakers winnen een wedstrijd met veel punten</strong></h3>
<p>Los Angeles speelt thuis en heeft met Dončić de beste speler op het veld. Portland heeft meer creatieve guards dan vorig seizoen en komt uitgerust naar Los Angeles. Wij verwachten een open duel.</p>
<p>Defensief zijn beide ploegen nog niet echt getest. De Lakers kregen in hun laatste twee duels 117 en 123 punten tegen, Portland speelde tegen Phoenix en Sacramento, die samen één van hun zes wedstrijden wonnen. Onze voorspelling: <strong>Los Angeles Lakers – Portland Trail Blazers 122-117</strong>.</p>
<h3><strong>Onze wedtip: Over 236,5 punten (1,91)</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Onze kans"], [
    ("Over 236,5 punten (incl. verlenging)", "1,91", "TOTO", "Ongeveer 56 procent"),
])}
<p><strong>Waarom deze tip?</strong> De tip is goed als er in totaal 237 punten of meer vallen, een eventuele verlenging inbegrepen. Een odd van 1,91 staat voor een kans van 52 procent; omdat beide kanten op 1,91 staan, is dat zonder de marge van de bookmaker precies 50 procent. Wij schatten de kans op ongeveer 56 procent. De onderbouwing:</p>
<p><strong>1. De Lakers spelen alleen maar wedstrijden met veel punten.</strong> Ze scoren 128 punten per duel en kregen er gemiddeld 115 tegen. Hun drie wedstrijden eindigden op 232, 242 en 255 punten; twee daarvan gingen over de lijn van vannacht.</p>
<p><strong>2. Portland heeft meer aanvallend vermogen dan vorig seizoen.</strong> Met Lillard en Morant erbij scoorde Portland 124 en 128 punten. En de drie onderlinge duels van vorig seizoen kwamen al uit op 230, 238 en 248 punten, zonder Dončić, Lillard of Morant.</p>
<p><strong>3. Een spannend duel helpt het totaal.</strong> De handicap van TOTO ligt rond de drie punten, dus ook de bookmaker verwacht een gelijkopgaande wedstrijd. Dan volgen er in de slotfase vaker fouten en vrije worpen, en een verlenging telt gewoon mee.</p>
<p><strong>Waarom niet een andere markt?</strong> Een zege van de Lakers (1,71) vraagt om 58 procent kans; wij komen uit op ongeveer 60 procent, en dat verschil is te klein. Bij Lakers -3,5 (1,93) moet Los Angeles met minstens vier punten winnen, en onze voorspelde marge van vijf punten zit daar te dicht tegenaan. Over 235,5 is een punt veiliger, maar levert met 1,77 duidelijk minder op dan 1,91 bij 236,5.</p>
<p><strong>Het risico.</strong> Portland heeft lengte en goede verdedigers: Clingan en Williams onder de ring, Camara en Holiday aan de buitenkant. Tegen Phoenix bleef het totaal op 207 steken. Valt het schot van Lillard en Morant tegen, of besluit Redick met het oog op de derby van woensdag het tempo laag te houden, dan kan het totaal eronder blijven. Meer uitleg over deze markt lees je in onze gidsen over <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap wedden</a> en de <a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">money line</a>.</p>
<h3><strong>Lakers – Trail Blazers live kijken in Nederland</strong></h3>
<p>Bij <a href="/bookmakers/bet365">Bet365</a> kun je NBA-wedstrijden live volgen via de livestream. Je hebt daarvoor een account met een storting nodig. ESPN zendt in Nederland een deel van de NBA-wedstrijden uit; in de programmagids zie je of deze erbij zit. Met <strong>NBA League Pass</strong>, de betaalde dienst van de competitie, kun je alle wedstrijden volgen. Meer opties vind je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk Lakers – Trail Blazers live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Lees ook onze voorspellingen voor <a href="/nieuws/celtics-nets-voorspelling-wedtips-nba-2026">Celtics – Nets</a>, <a href="/nieuws/knicks-pistons-voorspelling-wedtips-nba-2026">Knicks – Pistons</a> en <a href="/nieuws/spurs-kings-voorspelling-wedtips-nba-2026">Spurs – Kings</a>. Eerder schreven we over de Lakers in <a href="/nieuws/lakers-warriors-voorspelling-wedtips-nba-2026">Lakers – Warriors</a> en <a href="/nieuws/jazz-lakers-voorspelling-wedtips-nba-2026">Jazz – Lakers</a>. Benieuwd <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">welke Nederlanders in de NBA spelen</a>? Nieuw met basketbal? Lees <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels in de NBA</a>. Alle tips staan op <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Lakers – Trail Blazers?</strong><br>Woensdag 28 oktober 2026 om 04:00 Nederlandse tijd, in de nacht van dinsdag op woensdag. In Los Angeles is het dan dinsdagavond 20:00.</p>
<p><strong>Speelt Luka Dončić mee?</strong><br>Ja, naar verwachting wel. Dončić staat niet op de officiële NBA-blessurelijst. Hij scoorde in de eerste drie wedstrijden gemiddeld 34,3 punten.</p>
<p><strong>Wie is favoriet: Lakers of Trail Blazers?</strong><br>De Lakers, met een quotering van 1,71 bij TOTO. Portland staat op 2,20.</p>
<p><strong>Wat is onze voorspelling voor Lakers – Trail Blazers?</strong><br>De Lakers winnen met 122-117. Onze wedtip is Over 236,5 punten, inclusief verlenging (1,91 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

KAART = {"home": "Lakers", "away": "Trail Blazers", "home_abbr": "lal", "away_abbr": "por", "home_pos": "53-29 · nr. 4 West 2025/26", "away_pos": "42-40 · nr. 8 West 2025/26", "hs": 122, "as": 117, "datum": "Wo 28 okt", "tijd": "04:00", "odd_home": "1,71", "odd_away": "2,20"}
WEDTIPS = {"wedtip-1-2": "Over 236,5 punten (incl. verlenging)", "quotering-wedtip-1": "1.91",
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
                  "/nieuws/celtics-nets-voorspelling-wedtips-nba-2026", "/nieuws/knicks-pistons-voorspelling-wedtips-nba-2026",
                  "/nieuws/spurs-kings-voorspelling-wedtips-nba-2026",
                  "/nieuws/welke-nederlanders-spelen-in-de-nba",
                  "/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders",
                  "/nieuws/wat-is-handicap-wedden-de-complete-gids",
                  "/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners",
                  "/wedden-op-nba-voorspellingen-en-wedtips---basketbal", "/bookmakers/toto", "/bookmakers/bet365",
                  "/live-kijken", BET365}
    assert set(hrefs) <= toegestaan, set(hrefs) - toegestaan
    assert "nba-voorspellingen-vannacht-28-oktober-2026" not in html, "geen algemeen artikel vannacht"
    assert SLUG not in "".join(hrefs), "niet naar zichzelf linken"
    for s in ("celtics-nets", "knicks-pistons", "spurs-kings"):
        assert f"/nieuws/{s}-voorspelling-wedtips-nba-2026" in hrefs, f"link naar {s} ontbreekt"
    assert "<table" not in html.replace(f"<table {T}>", ""), "tabellen alleen via tabel()"
    verboden = ["BetCity", "ESPN-API", "ESPN.com", "Associated Press", "DraftKings", "Rotowire", "Betfans", "Shams"]
    assert not any(v.lower() in html.lower() for v in verboden), "geen bronnen/concurrenten"
    # SEO: focuskeyword
    fk = "Lakers – Trail Blazers voorspelling"
    assert fk in TITEL and fk in SAMENVATTING and len(SAMENVATTING) <= 160
    assert re.sub(r"<[^>]+>", "", content).startswith(fk), "focuskeyword in de eerste zin"
    assert any(fk in h for h in re.findall(r"<h3>(.*?)</h3>", html)) or "<h3><strong>Lakers – Trail Blazers" in html
    assert any("Lakers – Trail Blazers" in h for h in re.findall(r"<h3>(.*?)</h3>", html))
    # Wedtip en consistentie
    assert set(WEDTIPS) == {"wedtip-1-2", "quotering-wedtip-1", "bookmaker-wedtips"}
    assert WEDTIPS["bookmaker-wedtips"] == "669ab9f5aceb8b717cea24c3"
    q = float(WEDTIPS["quotering-wedtip-1"])
    toto_odds = {1.71, 2.20, 17.0, 2.25, 1.93, 1.73, 1.87, 1.69, 2.00, 1.77, 1.91}
    assert q in toto_odds and q == 1.91
    assert KAART["hs"] + KAART["as"] > 236.5, "voorspelde score moet Over 236,5 laten winnen"
    assert KAART["hs"] > KAART["as"], "voorspelling: Lakers winnen"
    assert f"{KAART['hs']}-{KAART['as']}" in content and f"{KAART['hs']}-{KAART['as']}" in content3
    assert KAART["odd_home"] == "1,71" and KAART["odd_away"] == "2,20" and KAART["tijd"] == "04:00"
    assert KAART["home_abbr"] == "lal" and KAART["away_abbr"] == "por" and KAART["datum"] == "Wo 28 okt"
    assert "1,91" in content and "1,91" in content3 and "236,5" in content and "236,5" in content3
    assert "dinsdag rond 10:45 uur" in html, "tijdstip odds"
    assert html.count("👉 Klik hier: maak je Bet365-account aan en wed live mee op") == 1
    assert SLUG == "lakers-trail-blazers-voorspelling-wedtips-nba-2026" and DATUM == "2026-10-28T03:00:00.000Z"
    tekst = re.sub(r"<[^>]+>", " ", html)
    woorden = len(tekst.split())
    assert 1400 <= woorden <= 1850, woorden
    print(len(TITEL), "tekens titel |", len(SAMENVATTING), "tekens samenvatting |", woorden, "woorden")
    print("Alle asserts geslaagd (dry run, niets gepubliceerd).")
