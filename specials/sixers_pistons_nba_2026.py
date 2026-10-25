# -*- coding: utf-8 -*-
"""Los artikel: 76ers – Pistons voorspelling, NBA 26 oktober 2026 (00:30 NL, wintertijd; zondag 19:30 ET), Xfinity Mobile Arena.
Feiten nagelopen op 25-10-2026 rond 09:30 NL (ESPN-API: summary 401909866 incl. blessures; boxscores 401909855 (76ers – Bucks
127-116), 401909089, 401909093, 401909088 (Pistons – Celtics 121-113) en 401909847 (Heat – Pistons 111-128); teamschema's
2026/27 en 2025/26; stand 2025/26; onderlinge duels 2025/26 401810050, 401809783, 401810808, 401810986; officiele
NBA-blessurelijst 25-10 04:30 ET; berichtgeving 23/24-10 over Embiid (speelt maar een van de twee weekendduels) en James).
- Back-to-back: ALLEEN Philadelphia (za 24-10 tegen Milwaukee, Embiid 36 min. 28/11/10, James rustte: onderrug).
  Detroit speelde vrijdag 23-10 in Miami (128-111) en had zaterdag vrij; dinsdag 27-10 in New York.
- Blessurelijst 25-10 04:30 ET: DET Duren out (rechterhamstring), Ausar Thompson questionable (rechterenkel); Philadelphia
  'not yet submitted'. ESPN: Embiid day-to-day 'rest', Walker day-to-day (rechterknie), James 'out' (stamt van zaterdag; hij
  wordt zondag terugverwacht), Barlow, Fall en Hukporti out. Embiid-rust is dus waarschijnlijk, niet officieel.
- Onderling 2025/26: 4-0 DET (111-108, 114-105, 131-109, 116-93); Embiid speelde in geen van de vier.
- Stand 2025/26: PHI 45-37 (nr. 7 Oost, 23-18/22-19, 115,9/116,1); DET 60-22 (nr. 1 Oost, 31-9 thuis, 28-13 uit,
  1 zege op neutraal terrein in Mexico-Stad; 117,8/109,6).
- Odds: alleen TOTO, uit specials/nba_feiten_2026_10_26.md (zo ±09:45 NL). 'Winnaar' en handicaps incl. verlenging.
- Eén wedtip (eis eigenaar): Detroit Pistons +2,5 @1,87, onze kans 56% (odd 53,5%; zonder marge 50,8%).
  python3 specials/sixers_pistons_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "76ers – Pistons voorspelling: wedtip en odds, back-to-back tegen Detroit (26 oktober, 00:30)"
SLUG = "76ers-pistons-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("Philadelphia (3-0) speelt de tweede avond van een back-to-back tegen Detroit (2-0). Voorspelling, onze wedtip, "
                "TOTO-odds en de status van Embiid en James.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet-experts.nl/go/bet365"
DATUM = "2026-10-25T23:30:00.000Z"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>In de nacht van zondag op maandag om 00:30 Nederlandse tijd ontvangen de Philadelphia 76ers de Detroit Pistons. Beide ploegen zijn nog ongeslagen: Philadelphia staat op 3-0, Detroit op 2-0. Philadelphia speelde zaterdagavond nog en moet het waarschijnlijk zonder Joel Embiid doen, Detroit mist center Jalen Duren. De bookmakers zien de 76ers als lichte favoriet. Onze voorspelling: Detroit wint met 113-110. Onze wedtip: Detroit Pistons +2,5 punten (1,87 bij TOTO).</strong></p>
<p>LeBron James keert waarschijnlijk terug na een avond rust. Hieronder lees je wie er speelt, wat <a href="/bookmakers/toto">TOTO</a> verwacht en waarom wij voor de Pistons kiezen.</p>
<h3><strong>76ers – Pistons: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "Philadelphia 76ers – Detroit Pistons"),
    ("Datum", "Maandag 26 oktober 2026 (nacht van zondag op maandag)"),
    ("Aanvang", "00:30 Nederlandse tijd (zondag 19:30 in Philadelphia)"),
    ("Arena", "Xfinity Mobile Arena, Philadelphia"),
    ("Competitie", "NBA, reguliere competitie 2026/27"),
    ("Stand 2026/27", "76ers 3-0, Pistons 2-0"),
    ("Onderlinge duels 2025/26", "4-0 voor de Pistons"),
])}
<p>Nederland staat sinds vannacht op wintertijd, de Verenigde Staten pas vanaf 1 november. Het tijdsverschil is deze week dus vijf uur. Alleen Philadelphia speelt een back-to-back: voor de 76ers is dit de vierde wedstrijd in zes dagen. Detroit speelde vrijdag in Miami en had zaterdag vrij.</p>
<h3><strong>Seizoen tot nu toe: 76ers 3-0, Pistons 2-0</strong></h3>
<p><strong>Philadelphia 76ers: drie zeges, steeds met Maxey voorop</strong></p>
<p>Philadelphia won bij kampioen New York met 106-100 en kwam donderdag tegen Cleveland terug van 29 punten achterstand (114-106). Zaterdag volgde een 127-116 zege op Milwaukee, zonder James (rust voor zijn onderrug). Embiid had 28 punten, 11 rebounds en 10 assists, Jaylen Brown scoorde 27 punten en Tyrese Maxey 26. Philadelphia raakte 19 van zijn 44 driepunters, na een zwakke start van 18 uit 68 in de eerste twee wedstrijden.</p>
<p><strong>Detroit Pistons: twee overtuigende zeges, maar twee nieuwe blessures</strong></p>
<p>Detroit opende met een 121-113 zege op Boston, na een achterstand van 22 punten in het derde kwart. Vrijdag won de ploeg van coach J.B. Bickerstaff met 128-111 in Miami. Detroit stond de hele wedstrijd voor en gaf 34 assists. John Collins scoorde 23 punten, invaller Paul Reed had 19 punten en 11 rebounds. Maar Duren viel in de eerste helft uit met een bovenbeenblessure en Ausar Thompson in het derde kwart met een enkelblessure.</p>
<h3><strong>Vorig seizoen: Detroit de beste van het Oosten, en vier keer te sterk voor Philadelphia</strong></h3>
<p>Detroit won in 2025/26 60 van de 82 wedstrijden en werd eerste in de Eastern Conference. Philadelphia eindigde op 45-37 als nummer zeven en overleefde de play-in en de eerste ronde. Beide ploegen strandden in de tweede ronde.</p>
{tabel(["2025/26", "Philadelphia 76ers", "Detroit Pistons"], [
    ("Eindstand", "45-37 (nr. 7 Oost)", "60-22 (nr. 1 Oost)"),
    ("Thuis / uit", "23-18 / 22-19", "31-9 / 28-13 (plus één zege in Mexico-Stad)"),
    ("Punten voor / tegen", "115,9 / 116,1", "117,8 / 109,6"),
    ("Onderling", "0-4", "4-0"),
    ("Play-offs", "Tweede ronde (0-4 tegen New York)", "Tweede ronde (3-4 tegen Cleveland)"),
])}
<p>Detroit won de vier onderlinge duels met 111-108 en 116-93 in Philadelphia, en met 114-105 en 131-109 in Detroit. Dat zegt minder dan het lijkt: Embiid speelde in geen van die duels mee, en Brown en James zaten nog niet bij Philadelphia.</p>"""

content2 = f"""<h3><strong>Selecties en blessures</strong></h3>
<p><strong>Philadelphia 76ers: James terug, Embiid waarschijnlijk niet</strong></p>
<p>Philadelphia bouwde deze zomer een nieuwe top: Brown kwam van Boston in een ruil voor Paul George, de 41-jarige James tekende als vrije speler. Embiid zei donderdag dat hij maar één van de twee wedstrijden van dit weekend speelt. Omdat hij zaterdag 36 minuten speelde, ligt rust tegen Detroit voor de hand, al is dat nog niet officieel. James wordt na een avond rust terugverwacht. Onder de ring is het dun: Jabari Walker raakte zaterdag geblesseerd aan zijn knie, en Dominick Barlow, Tacko Fall en Ariel Hukporti ontbreken al langer.</p>
<p><strong>Detroit Pistons: zonder Duren</strong></p>
<p>Duren, vorig seizoen goed voor 19,5 punten en 10,5 rebounds per wedstrijd, speelt niet door een blessure aan zijn rechterhamstring. Ausar Thompson is twijfelachtig met een verstuikte rechterenkel. Detroit bouwde verder op de ploeg van vorig seizoen; nieuw zijn onder meer Collins en schutter Isaiah Joe.</p>
{tabel(["Speler", "Team", "Status"], [
    ("Joel Embiid", "Philadelphia", "Waarschijnlijk rust (tweede avond back-to-back)"),
    ("LeBron James", "Philadelphia", "Waarschijnlijk inzetbaar (rustte zaterdag, onderrug)"),
    ("Jabari Walker", "Philadelphia", "Twijfelachtig (rechterknie)"),
    ("Dominick Barlow", "Philadelphia", "Speelt niet (rug)"),
    ("Tacko Fall", "Philadelphia", "Speelt niet (bovenbeen)"),
    ("Ariel Hukporti", "Philadelphia", "Speelt niet (achillespees)"),
    ("Jalen Duren", "Detroit", "Speelt niet (rechterhamstring)"),
    ("Ausar Thompson", "Detroit", "Twijfelachtig (rechterenkel)"),
])}
<p><em>Officiële NBA-blessurelijst van zondag 25 oktober, 09:30 Nederlandse tijd. Philadelphia had toen nog niets ingediend; de status van Embiid, James en Walker volgt later op de dag.</em></p>
<p><strong>Verwachte basisvijf 76ers:</strong> Tyrese Maxey, VJ Edgecombe, Jaylen Brown, LeBron James en waarschijnlijk Adem Bona als center. Kentavious Caldwell-Pope, Anfernee Simons en Dean Wade zijn de belangrijkste invallers.</p>
<p><strong>Verwachte basisvijf Pistons:</strong> Cade Cunningham, Duncan Robinson, Ausar Thompson, John Collins en Paul Reed in de plaats van Duren. Kan Thompson niet spelen, dan liggen Ronald Holland II, Javonte Green en Kevin Huerter klaar.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "Bijzonderheid"], [
    ("Tyrese Maxey (PHI)", "28,7", "3,7", "5,0", "Speelt gemiddeld ruim 39 minuten"),
    ("Jaylen Brown (PHI)", "22,3", "6,3", "5,0", "Nieuw, overgekomen van Boston"),
    ("LeBron James (PHI)", "15,5", "9,5", "6,0", "Twee duels, rustte zaterdag"),
    ("VJ Edgecombe (PHI)", "12,3", "8,0", "3,0", "13 rebounds tegen Milwaukee"),
    ("Cade Cunningham (DET)", "19,0", "3,0", "8,0", "Vorig seizoen 23,9 punten en 9,9 assists"),
    ("Duncan Robinson (DET)", "19,0", "1,5", "2,0", "10 driepunters in twee duels"),
    ("John Collins (DET)", "14,5", "6,0", "1,0", "23 punten in Miami"),
    ("Paul Reed (DET)", "12,5", "8,5", "2,5", "Vervangt waarschijnlijk Duren"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2026/27, tenzij anders vermeld.</em></p>
<p>Beide ploegen missen waarschijnlijk hun vaste center. Detroit schoot in de eerste twee wedstrijden 42,3 procent van achter de driepuntslijn, Philadelphia over drie wedstrijden 33,0 procent.</p>
<h3><strong>Odds 76ers – Pistons bij TOTO</strong></h3>
<p>Een quotering van 1,74 staat voor ongeveer 57 procent kans; zonder de marge van de bookmaker is dat zo'n 55 procent. De handicap ligt rond 2,5 punten, het verwachte puntentotaal rond 227,5.</p>
{tabel(["Markt", "76ers", "Pistons"], [
    ("Winnaar (incl. verlenging)", "1,74", "2,15"),
    ("1X2 (reguliere speeltijd, gelijk 17,00)", "1,77", "2,15"),
    ("Handicap -1,5 / +1,5", "1,73", "1,93"),
    ("Handicap -2,5 / +2,5", "1,93", "1,87"),
    ("Handicap -3,5 / +3,5", "2,00", "1,69"),
])}
<p>Op het totaal van 227,5 punten biedt TOTO Over 1,87 en Under 1,93; op 226,5 punten is dat Over 1,73 en Under 1,95. Handicaps en totalen zijn inclusief verlenging. Odds gelezen op zondag rond 09:45 uur. Wordt de status van Embiid of James officieel, dan kunnen de lijnen nog verschuiven.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op 76ers – Pistons</strong></a></p>"""

content3 = f"""<h3><strong>Onze voorspelling: Detroit wint nipt in Philadelphia</strong></h3>
<p>Waarom is Philadelphia favoriet? De 76ers spelen thuis, zijn ongeslagen en hebben met Maxey, Brown en een uitgeruste James genoeg kwaliteit om een wedstrijd naar zich toe te trekken.</p>
<p>Toch kiezen wij voor Detroit. De Pistons zijn uitgerust, terwijl Philadelphia zijn vierde wedstrijd in zes dagen speelt en Maxey al drie keer 36 minuten of meer maakte. Zonder Embiid en met Walker twijfelachtig heeft coach Nick Nurse weinig lengte. Detroit mist Duren, maar Reed liet vrijdag zien dat hij die rol aankan, en de Pistons wonnen hun twee wedstrijden met acht en zeventien punten verschil. Onze voorspelling: <strong>Philadelphia 76ers – Detroit Pistons 110-113</strong>.</p>
<h3><strong>Onze wedtip: Detroit Pistons +2,5 punten (1,87)</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Onze kans", "Kans volgens odds"], [
    ("Detroit Pistons +2,5 punten (incl. verlenging)", "1,87", "TOTO", "56%", "53%"),
])}
<p>Met deze weddenschap krijgt Detroit 2,5 punten voorsprong. Je wint als de Pistons winnen of met maximaal twee punten verschil verliezen. Een quotering van 1,87 staat voor ruim 53 procent kans; wij schatten die kans op 56 procent. Om drie redenen:</p>
<p><strong>1. De vermoeidheid ligt bij Philadelphia.</strong> Detroit had een vrije dag, Philadelphia speelde zaterdagavond nog. Waarschijnlijk rust Embiid. Zonder hem moet Philadelphia het onder de ring vooral van Bona hebben.</p>
<p><strong>2. Detroit is de completere ploeg.</strong> Detroit kreeg vorig seizoen 109,6 punten per wedstrijd tegen, Philadelphia 116,1. Bovendien beslisten invallers als Green (19 punten tegen Boston), Reed en Jenkins al wedstrijden. De bank van Philadelphia is smaller.</p>
<p><strong>3. De extra punten zijn het waard.</strong> In een gelijkopgaand duel beslist vaak één aanval. De +2,5 dekt ook een thuiszege van Philadelphia met één of twee punten.</p>
<p><strong>Het risico:</strong> Philadelphia heeft drie spelers die een wedstrijd in hun eentje kunnen beslissen, en zaterdag viel het schot van afstand eindelijk. Speelt Embiid toch, dan verschuift de wedstrijd in het voordeel van de 76ers. Kies daarom geen grote inzet.</p>
<p>Waarom geen andere tip? Een zege van Detroit levert met 2,15 meer op, maar dan verlies je ook bij een nipte nederlaag. De verschillen tussen deze ploegen zijn zo klein dat we die buffer liever hebben. Een zege van Philadelphia (1,74) past niet bij onze inschatting. Op het puntentotaal zien we geen duidelijke kant: de twee wedstrijden van Detroit gingen ruim over 227,5 punten (234 en 239), maar zonder Embiid en Duren en met een vermoeide thuisploeg kan het ook lager uitvallen. Meer uitleg over deze markt lees je in onze gids over <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap wedden</a>.</p>
<h3><strong>76ers – Pistons live kijken in Nederland</strong></h3>
<p>De makkelijkste manier: bij <a href="/bookmakers/bet365">Bet365</a> kijk je NBA-wedstrijden gratis live. Je hebt alleen een account met een kleine storting nodig, die je daarna weer kunt opnemen. ESPN heeft in Nederland de NBA-rechten, maar zendt maar een deel van de wedstrijden uit; check vooraf de gids. Met <strong>NBA League Pass</strong>, de betaalde streamingdienst van de competitie, volg je alle wedstrijden. Meer opties vind je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk 76ers – Pistons live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Lees ook onze voorspellingen voor <a href="/nieuws/76ers-bucks-voorspelling-wedtips-nba-2026">76ers – Bucks</a> en <a href="/nieuws/heat-pistons-voorspelling-wedtips-nba-2026">Heat – Pistons</a>, waarin onze hoofdtips allebei uitkwamen, en de <a href="/nieuws/nba-voorspellingen-vannacht-25-oktober-2026">NBA-voorspellingen van 25 oktober</a>. Nieuw met wedden op basketbal? Lees <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels in de NBA</a> en <a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">de uitleg over de money line</a>. Alle basketbaltips vind je op <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint 76ers – Pistons?</strong><br>Maandag 26 oktober 2026 om 00:30 Nederlandse tijd, in de nacht van zondag op maandag. In Philadelphia is het dan zondagavond 19:30.</p>
<p><strong>Speelt Joel Embiid mee?</strong><br>Waarschijnlijk niet. Embiid speelt maar één van de twee wedstrijden van dit weekend en speelde zaterdag tegen Milwaukee. De officiële beslissing volgt later op zondag.</p>
<p><strong>Speelt LeBron James mee?</strong><br>Waarschijnlijk wel. James rustte zaterdag om zijn onderrug te sparen en wordt tegen Detroit terugverwacht.</p>
<p><strong>Speelt Jalen Duren mee?</strong><br>Nee, de center van Detroit mist de wedstrijd met een hamstringblessure. Ausar Thompson is twijfelachtig (enkel).</p>
<p><strong>Wat is onze voorspelling en wedtip voor 76ers – Pistons?</strong><br>Detroit wint met 113-110. Onze wedtip is Detroit Pistons +2,5 punten (1,87 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

KAART = {"home": "76ers", "away": "Pistons", "home_abbr": "phi", "away_abbr": "det", "home_pos": "45-37 · nr. 7 Oost 2025/26", "away_pos": "60-22 · nr. 1 Oost 2025/26", "hs": 110, "as": 113, "datum": "Ma 26 okt", "tijd": "00:30", "odd_home": "1,74", "odd_away": "2,15"}
WEDTIPS = {"wedtip-1-2": "Detroit Pistons +2,5 punten (incl. verlenging)", "quotering-wedtip-1": "1.87",
           "bookmaker-wedtips": "669ab9f5aceb8b717cea24c3"}

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_BASKETBAL, "competitie": COMPETITIE_NBA,
          "datum-tijd-van-wedstrijd": DATUM,
          "publicatiedatum": datetime.now(timezone.utc).isoformat(), **WEDTIPS}
    # Alleen dry run: dit script publiceert niets.
    import re
    alles = content + content2 + content3
    tekst = re.sub(r"<[^>]+>", " ", alles)
    woorden = len(tekst.split())
    print(len(TITEL), "tekens titel |", len(SAMENVATTING), "tekens samenvatting |", woorden, "woorden")
    feiten = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "nba_feiten_2026_10_26.md"), encoding="utf-8").read()
    odds_regel = next(r for r in feiten.splitlines() if r.startswith("- **76ers – Pistons**"))
    # vaste waarden
    assert SLUG == "76ers-pistons-voorspelling-wedtips-nba-2026" and DATUM == "2026-10-25T23:30:00.000Z"
    assert TITEL.startswith("76ers – Pistons voorspelling: wedtip en odds") and TITEL.endswith("(26 oktober, 00:30)")
    assert len(TITEL) <= 110 and 120 <= len(SAMENVATTING) <= 155
    assert 1400 <= woorden <= 1800, woorden
    assert {k: KAART[k] for k in ("home", "away", "home_abbr", "away_abbr", "datum", "tijd", "odd_home", "odd_away")} == {
        "home": "76ers", "away": "Pistons", "home_abbr": "phi", "away_abbr": "det", "datum": "Ma 26 okt", "tijd": "00:30",
        "odd_home": "1,74", "odd_away": "2,15"}
    # precies één wedtip, odd uit het feitenblad en minimaal 1,40
    assert set(WEDTIPS) == {"wedtip-1-2", "quotering-wedtip-1", "bookmaker-wedtips"}
    assert WEDTIPS["bookmaker-wedtips"] == "669ab9f5aceb8b717cea24c3"
    q = float(WEDTIPS["quotering-wedtip-1"]); assert q >= 1.40 and "." in WEDTIPS["quotering-wedtip-1"]
    assert "+2,5 1,87" in odds_regel and "Winnaar 1,74 / 2,15" in odds_regel
    for o in ("1,74", "2,15", "1,77", "17,00", "1,73", "1,93", "1,87", "2,00", "1,69", "1,95"):
        assert o in odds_regel, o
    # score past bij de tip (Detroit +2,5 wint) en staat overal gelijk
    assert KAART["as"] + 2.5 > KAART["hs"]
    assert f"{KAART['hs']}-{KAART['as']}" in content3 and f"{KAART['as']}-{KAART['hs']}" in content and f"{KAART['as']}-{KAART['hs']}" in content3
    assert alles.count("Detroit Pistons +2,5 punten") >= 4 and "56%" in content3
    # opmaak
    assert content.startswith("<p><strong>")
    assert "<h2" not in alles and "<h4" not in alles and alles.count("<h3>") == alles.count("<h3><strong>")
    assert not re.search(r"<(ul|ol|/li)>\s+<", alles) and not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    assert content3.rstrip().splitlines()[-1] == "<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"
    assert alles.count("<table") == 6
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/") or href == BET365, href
    for link in ("/nieuws/76ers-bucks-voorspelling-wedtips-nba-2026", "/nieuws/heat-pistons-voorspelling-wedtips-nba-2026",
                 "/nieuws/nba-voorspellingen-vannacht-25-oktober-2026", "/bookmakers/bet365", "/live-kijken"):
        assert f'href="{link}"' in alles, link
    for href in set(re.findall(r'href="(/[^"]+)"', alles)) - {BET365}:
        assert href in feiten, href
    # geen bronnen, concurrenten of verboden namen
    for woord in ("betcity", "betfans", "rotowire", "cbs sports", "associated press", "draftkings", "espn-api", "affiliate"):
        assert woord not in alles.lower(), woord
    print("dry run ok – niets gepubliceerd")
