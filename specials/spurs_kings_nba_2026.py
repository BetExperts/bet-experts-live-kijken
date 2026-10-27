# -*- coding: utf-8 -*-
"""Los artikel: Spurs – Kings voorspelling, NBA nacht van 27 op 28 oktober 2026 (01:00 NL, wintertijd; 19:00 CT),
Frost Bank Center San Antonio. Feiten nagelopen op 27-10-2026 (ESPN-API: summary 401909879, box scores 401909090,
401909096, 401909858, 401909842, 401909852 en 401909867, teamschema's 2025/26 (season 2026, type 2/3) en 2026/27,
rosters en coaches, standen 2025/26, spelersgemiddelden 2025/26 en 2026/27, onderlinge duels 2025/26 (401810089,
401810670, 401810853); officiële NBA-blessurelijst 27-10 05:45 ET (= 10:45 NL)).
- Spurs: 104-116 en 110-114 thuis tegen OKC en Houston (Wembanyama 1 uit 13 in de opener), 122-106 in Dallas.
  Speelden zaterdag (US), twee rustdagen; woensdag (US) alweer in Utah (eerste avond van een back-to-back).
- Kings: 96-121 bij de Clippers, 120-128 tegen Portland, 112-123 tegen Memphis (LaVine 37). 124,0 punten tegen per duel.
- Onderling 2025/26: 123-110 en 139-122 in San Antonio, 132-104 in Sacramento (3-0 SAS; totalen 233, 261, 236).
- 2025/26: Spurs 62-20 (nr. 2 West, thuis 32-8, uit 29-12, 119,8/111,5), West-finale 4-3 tegen OKC, Finals 1-4 tegen NY.
  Kings 22-60 (nr. 14 West, thuis 15-26, uit 7-34, 111,0/121,0).
- Odds: alleen TOTO, uit specials/nba_feiten_2026_10_28.md (dinsdag ±10:45 NL). Handicap en totaal incl. verlenging.
- Eén wedtip (eis eigenaar): Over 230,5 @1,87, onze kans 57% (markt 53,5%, zonder marge ±51%).
  python3 specials/spurs_kings_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "Spurs – Kings voorspelling: wedtip en odds voor Wembanyama tegen een lek Sacramento (28 oktober, 01:00)"
SLUG = "spurs-kings-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("Spurs – Kings voorspelling: Wembanyama treft een Sacramento dat 124 punten per duel weggeeft. "
                "Onze wedtip, TOTO-odds, blessures en opstellingen.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet-experts.nl/go/bet365"
DATUM = "2026-10-28T00:00:00.000Z"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>Onze Spurs – Kings voorspelling voor de nacht van dinsdag op woensdag: veel punten in San Antonio. Victor Wembanyama en de Spurs ontvangen om 01:00 Nederlandse tijd een Sacramento dat na drie wedstrijden nog zonder zege staat en gemiddeld 124 punten per duel tegen krijgt. De Kings missen bovendien Keegan Murray en de centers Maxime Raynaud en Dylan Cardwell. Onze voorspelling: Spurs – Kings 125-110. Onze wedtip: meer dan 230,5 punten (inclusief verlenging) tegen een quotering van 1,87 bij TOTO.</strong></p>
<p>Hieronder lees je alles over vorm, blessures, de odds van <a href="/bookmakers/toto">TOTO</a> en onze onderbouwing.</p>
<h3><strong>Spurs – Kings: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "San Antonio Spurs – Sacramento Kings"),
    ("Datum", "Woensdag 28 oktober 2026 (nacht van dinsdag op woensdag)"),
    ("Aanvang", "01:00 Nederlandse tijd (dinsdag 19:00 in San Antonio)"),
    ("Arena", "Frost Bank Center, San Antonio"),
    ("Competitie", "NBA, reguliere competitie 2026/27"),
    ("Stand 2026/27", "Spurs 1-2, Kings 0-3"),
    ("Onderlinge duels 2025/26", "3-0 voor de Spurs"),
])}
<p>San Antonio speelde zaterdag in Dallas en had daarna twee rustdagen. Sacramento speelde zondag thuis tegen Memphis en had maandag vrij. Voor de Spurs is dit wel de eerste avond van een back-to-back: woensdagavond (Amerikaanse tijd) wacht een uitduel in Salt Lake City.</p>
<h3><strong>De eerste week: Spurs vinden hun ritme, Kings lekken punten</strong></h3>
<p><strong>San Antonio Spurs: twee thuisnederlagen, daarna een ruime zege</strong></p>
<p>De finalist van vorig seizoen begon stroef. In de opener verloor San Antonio met 104-116 van Oklahoma City, met een zeldzaam slechte avond van Wembanyama: 12 punten en 13 rebounds, maar 1 uit 13 uit het veld. Daarna ging het thuis met 110-114 mis tegen Houston, ondanks 25 punten en 13 rebounds van de Fransman. Zaterdag volgde de eerste zege: 122-106 in Dallas, met 23 punten van Wembanyama in 29 minuten en 22 van Dylan Harper. Opvallend is het schutterswerk: in drie duels ging maar 32 procent van de driepunters erin (37 uit 116).</p>
<p><strong>Sacramento Kings: drie nederlagen, 124 punten tegen</strong></p>
<p>Sacramento verloor met 96-121 bij de Clippers, waar rookie Darius Acuff Jr. maar 5 van zijn 24 schoten raak gooide. Thuis volgde een 120-128 nederlaag tegen Portland: Acuff Jr. maakte 33 punten, Domantas Sabonis had 27 punten, 19 rebounds en 10 assists. Zondag verloren de Kings met 112-123 van Memphis. Zach LaVine scoorde 37 punten (13 uit 25), maar de Grizzlies pakten 54 rebounds tegen 44. De Kings scoren dus wel, maar krijgen er gemiddeld 124 tegen.</p>
<h3><strong>Vorig seizoen en de onderlinge duels</strong></h3>
<p>San Antonio won 62 wedstrijden en werd tweede in het Westen. In de play-offs gingen Portland, Minnesota en, na zeven wedstrijden in de West-finale, Oklahoma City eraan. In de NBA Finals was New York met 4-1 te sterk. Sacramento werd met 22-60 voorlaatste in het Westen en kreeg 121,0 punten per wedstrijd tegen, het op drie na hoogste aantal van de competitie.</p>
{tabel(["2025/26", "San Antonio Spurs", "Sacramento Kings"], [
    ("Eindstand", "62-20 (nr. 2 West)", "22-60 (nr. 14 West)"),
    ("Thuis / uit", "32-8 / 29-12", "15-26 / 7-34"),
    ("Punten voor / tegen", "119,8 / 111,5", "111,0 / 121,0"),
    ("Na het seizoen", "NBA Finals (1-4 tegen New York)", "Play-offs niet gehaald"),
])}
<p>De Spurs wonnen alle drie de onderlinge duels: 123-110 en 139-122 in San Antonio en 132-104 in Sacramento. Dat leverde samen 233, 261 en 236 punten op. Wembanyama miste het eerste duel; in de andere twee maakte hij 28 punten en 15 rebounds en 18 punten in 22 minuten.</p>"""

content2 = f"""<h3><strong>Zo zijn beide selecties veranderd</strong></h3>
<p><strong>San Antonio Spurs: de finaleploeg bleef bij elkaar</strong></p>
<p>Coach Mitch Johnson heeft vrijwel dezelfde ploeg als vorig seizoen. De belangrijkste nieuwkomer is Tobias Harris, die uit Detroit kwam maar met een kuitblessure nog geen minuut speelde. In de draft koos San Antonio Jayden Quaintance, die herstelt van een knieoperatie, en center Tarris Reed Jr. Johnson kiest voor drie guards in de basis: De'Aaron Fox, Stephon Castle en Harper.</p>
<p><strong>Sacramento Kings: jong en dun bezet</strong></p>
<p>Bij coach Doug Christie is DeMar DeRozan vertrokken (naar Denver), en ook Russell Westbrook staat niet meer op de selectie. Nieuw zijn Acuff Jr., de nummer zeven van de draft, de rookies Emanuel Sharp en Alex Karaban, Jonathan Mogbo en Leaky Black. Ben Simmons tekende ook, maar is na een operatie aan zijn achillespees het hele seizoen uitgeschakeld.</p>
<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("Tobias Harris", "San Antonio", "Speelt niet (kuit)"),
    ("Jayden Quaintance", "San Antonio", "Speelt niet (herstel na knieoperatie)"),
    ("Keegan Murray", "Sacramento", "Speelt niet (enkel)"),
    ("Maxime Raynaud", "Sacramento", "Speelt niet (knieschijf)"),
    ("Dylan Cardwell", "Sacramento", "Speelt niet (kuit)"),
    ("Ben Simmons", "Sacramento", "Speelt niet (achillespees, seizoen voorbij)"),
])}
<p><em>Stand van de officiële NBA-blessurelijst op dinsdag 27 oktober, 10:45 Nederlandse tijd.</em></p>
<p><strong>Verwachte basisvijf Spurs:</strong> De'Aaron Fox, Stephon Castle, Dylan Harper, Devin Vassell, Victor Wembanyama. Dezelfde vijf als in alle drie de wedstrijden. Keldon Johnson, Julian Champagnie en Luke Kornet zijn de belangrijkste wissels.</p>
<p><strong>Verwachte basisvijf Kings:</strong> Darius Acuff Jr., Zach LaVine, De'Andre Hunter, Precious Achiuwa, Domantas Sabonis. Zo begon Sacramento zondag, toen Achiuwa de plek van Murray innam. Achter Sabonis is er geen echte center: Mogbo, Malik Monk, Daeqwon Plowden en Sharp vullen de wissels.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "2026/27 tot nu toe"], [
    ("Victor Wembanyama (SA)", "25,0", "11,5", "3,1", "20 ptn, 11 reb, 4 blocks"),
    ("De'Aaron Fox (SA)", "18,6", "3,8", "6,2", "17,3 ptn, 8,3 ast"),
    ("Dylan Harper (SA)", "11,8", "3,4", "3,9", "20 ptn in 32 minuten"),
    ("Zach LaVine (SAC)", "19,2*", "2,8*", "2,3*", "29 ptn, 38 minuten"),
    ("Domantas Sabonis (SAC)", "15,8*", "11,4*", "4,1*", "18,7 ptn, 17,3 reb, 7 ast"),
    ("Darius Acuff Jr. (SAC)", "rookie", "-", "-", "22,3 ptn, 24 uit 73 raak"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26. * LaVine speelde vorig seizoen 39 duels, Sabonis maar 19.</em></p>
<p><strong>Victor Wembanyama</strong> staat na de valse start in de opener weer op 25 en 23 punten. Zonder Raynaud en Cardwell moet Sacramento hem verdedigen met Sabonis en Achiuwa, die allebei een stuk kleiner zijn. <strong>Zach LaVine</strong> is de topscorer van de Kings: 29 punten per duel, met 37 tegen Memphis. <strong>Domantas Sabonis</strong> pakt 17,3 rebounds per wedstrijd en zet veel kansen voor anderen op.</p>
<h3><strong>Odds Spurs – Kings bij TOTO</strong></h3>
<p>TOTO ziet San Antonio als enorme favoriet: een quotering van 1,05 staat voor ongeveer 95 procent winkans. De handicap ligt rond de 17,5 punten in het voordeel van de Spurs, het verwachte puntentotaal op 230,5.</p>
{tabel(["Markt (TOTO)", "Spurs", "Kings"], [
    ("Winnaar (incl. verlenging)", "1,05", "11,75"),
    ("Handicap -16,5 / +16,5 (incl. verlenging)", "1,71", "1,98"),
    ("Handicap -17,5 / +17,5 (incl. verlenging)", "1,87", "1,93"),
    ("Handicap -18,5 / +18,5 (incl. verlenging)", "1,93", "1,77"),
])}
<p>Op het totaal biedt TOTO 229,5 punten (Over 1,73 / Under 1,95), 230,5 (1,87 / 1,93) en 231,5 (Over 1,91 / Under 1,77). Odds gelezen op dinsdag rond 10:45 uur; vergelijk ze vlak voor de start nog even.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op Spurs – Kings</strong></a></p>"""

content3 = f"""<h3><strong>Spurs – Kings voorspelling: San Antonio wint, en er vallen veel punten</strong></h3>
<p>Over de winnaar bestaat weinig twijfel. San Antonio is een finalist met de beste speler op het veld, Sacramento een ploeg in de wederopbouw die drie keer verloor en nu ook nog drie lange spelers mist. De vraag is vooral hoeveel punten er vallen.</p>
<p>De verdediging van de Kings is het zwakke punt. Vorig seizoen kreeg Sacramento al 121 punten per wedstrijd tegen, dit seizoen zelfs 124. De Spurs scoorden in de drie onderlinge duels van vorig jaar 123, 139 en 132 punten. Tegelijk kunnen de Kings zelf punten maken: LaVine en Acuff Jr. nemen samen ruim 40 schoten per duel, en in hun twee thuiswedstrijden scoorde Sacramento 120 en 112. Onze voorspelling: <strong>San Antonio Spurs – Sacramento Kings 125-110</strong>.</p>
<h3><strong>Onze wedtip: meer dan 230,5 punten (1,87)</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Onze kans"], [
    ("Over 230,5 punten (incl. verlenging)", "1,87", "TOTO", "Ongeveer 57 procent"),
])}
<p><strong>Waarom deze tip?</strong> De tip is goed als er samen minstens 231 punten vallen, een eventuele verlenging inbegrepen. Een odd van 1,87 staat voor een kans van 53,5 procent; zonder de marge van de bookmaker is dat ongeveer 51 procent. Wij schatten de kans op ongeveer 57 procent. De onderbouwing:</p>
<p><strong>1. Sacramento verdedigt slecht en mist lengte.</strong> De Kings kregen 121, 128 en 123 punten tegen. Zonder Murray, Raynaud en Cardwell staat er achter Sabonis geen center meer, terwijl Wembanyama met zijn lengte boven iedereen uitsteekt. Memphis pakte zondag al tien rebounds meer.</p>
<p><strong>2. De onderlinge duels gingen allemaal over de lijn.</strong> Vorig seizoen vielen er 233, 261 en 236 punten, dus drie keer meer dan 230,5. Ook in het duel zonder Wembanyama scoorde San Antonio 123 punten.</p>
<p><strong>3. Beide aanvallen hebben meer in de tank.</strong> De Spurs scoorden vorig seizoen 119,8 punten per wedstrijd, maar schieten nu maar 32 procent voor drie. Na twee rustdagen en tegen deze verdediging ligt een betere avond voor de hand. Bij de Kings scoort LaVine 29 per duel; hun wedstrijden kwamen dit seizoen uit op 217, 248 en 235 punten.</p>
<p><strong>Waarom niet een andere markt?</strong> Een zege van de Spurs (1,05) levert vrijwel niets op. De handicap van -17,5 (1,87) laten we bewust liggen. Daarvoor moet San Antonio met minstens 18 punten winnen, en dat lukte vorig seizoen maar één keer in drie duels (13, 17 en 28 punten verschil). Dit seizoen was de grootste zege 16 punten, in Dallas. Bovendien speelt San Antonio de avond erna in Utah. Loopt de voorsprong op, dan zit Wembanyama in het vierde kwart waarschijnlijk op de bank en krijgen de reserves de rest van de wedstrijd. Juist dan loopt een grote voorsprong vaak nog wat terug. Onze voorspelde marge van 15 punten valt onder de lijn. Kings +17,5 (1,93) is ook geen keuze: vorig seizoen ging het in Sacramento met 28 punten mis. Over 231,5 (1,91) betaalt iets meer, maar dan heb je een punt minder speelruimte.</p>
<p><strong>Het risico.</strong> De drie wedstrijden van de Spurs dit seizoen bleven allemaal onder de lijn (220, 224 en 228 punten), en vorig seizoen kreeg San Antonio maar 111,5 punten per duel tegen. Ook de Kings bleven bij de Clippers steken op 96 punten. En als het al vroeg beslist is, kan het tempo in de tweede helft zakken. Let op: het puntentotaal telt een eventuele verlenging mee. Meer uitleg vind je in onze gidsen over <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap wedden</a> en de <a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">money line</a>.</p>
<h3><strong>Spurs – Kings live kijken in Nederland</strong></h3>
<p>Bij <a href="/bookmakers/bet365">Bet365</a> kun je NBA-wedstrijden live volgen via de livestream. Je hebt daarvoor een account met een storting nodig. ESPN zendt in Nederland een deel van de NBA-wedstrijden uit; in de programmagids zie je of deze erbij zit. Met <strong>NBA League Pass</strong>, de betaalde dienst van de competitie, kun je alle wedstrijden volgen. Meer opties vind je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk Spurs – Kings live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Vannacht schreven we ook voorbeschouwingen van <a href="/nieuws/celtics-nets-voorspelling-wedtips-nba-2026">Celtics – Nets</a>, <a href="/nieuws/knicks-pistons-voorspelling-wedtips-nba-2026">Knicks – Pistons</a> en <a href="/nieuws/lakers-trail-blazers-voorspelling-wedtips-nba-2026">Lakers – Trail Blazers</a>. Lees ook onze voorspelling voor de opener <a href="/nieuws/spurs-thunder-voorspelling-wedtips-nba-opening-2026">Spurs – Thunder</a> en de <a href="/nieuws/nba-voorspellingen-vannacht-26-oktober-2026">NBA-voorspellingen van 26 oktober</a>, met onze tip voor Kings – Grizzlies. Benieuwd <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">welke Nederlanders in de NBA spelen</a>? Nieuw met basketbal? Lees <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels in de NBA</a>. Alle tips staan op <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Spurs – Kings?</strong><br>In de nacht van dinsdag op woensdag 28 oktober 2026 om 01:00 Nederlandse tijd. In San Antonio is het dan dinsdag 19:00.</p>
<p><strong>Speelt Victor Wembanyama mee?</strong><br>Ja, hij staat niet op de blessurelijst en speelde alle drie de wedstrijden. Bij San Antonio ontbreken alleen Tobias Harris en Jayden Quaintance.</p>
<p><strong>Wie is favoriet: Spurs of Kings?</strong><br>De Spurs, met een quotering van 1,05 bij TOTO. Sacramento staat op 11,75.</p>
<p><strong>Wat is onze voorspelling voor Spurs – Kings?</strong><br>De Spurs winnen met 125-110. Onze wedtip is meer dan 230,5 punten, inclusief verlenging (1,87 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

KAART = {"home": "Spurs", "away": "Kings", "home_abbr": "sa", "away_abbr": "sac", "home_pos": "62-20 · nr. 2 West 2025/26", "away_pos": "22-60 · nr. 14 West 2025/26", "hs": 125, "as": 110, "datum": "Wo 28 okt", "tijd": "01:00", "odd_home": "1,05", "odd_away": "11,75"}
WEDTIPS = {"wedtip-1-2": "Over 230,5 punten (incl. verlenging)", "quotering-wedtip-1": "1.87",
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
                  "/nieuws/lakers-trail-blazers-voorspelling-wedtips-nba-2026",
                  "/nieuws/welke-nederlanders-spelen-in-de-nba",
                  "/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders",
                  "/nieuws/wat-is-handicap-wedden-de-complete-gids",
                  "/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners",
                  "/wedden-op-nba-voorspellingen-en-wedtips---basketbal", "/bookmakers/toto", "/bookmakers/bet365",
                  "/live-kijken", BET365}
    assert set(hrefs) <= toegestaan, set(hrefs) - toegestaan
    assert "nba-voorspellingen-vannacht-28-oktober-2026" not in html, "geen algemeen artikel vannacht"
    assert f"/nieuws/{SLUG}" not in html, "niet naar jezelf linken"
    vannacht = ["celtics-nets", "knicks-pistons", "lakers-trail-blazers"]
    assert all(f"/nieuws/{s}-voorspelling-wedtips-nba-2026" in html for s in vannacht), "link naar de 3 andere voorbeschouwingen"
    assert html.count(BET365) == 2 and "Klik hier: maak je Bet365-account aan en wed live mee op Spurs – Kings" in html
    assert "<table" not in html.replace(f"<table {T}>", ""), "tabellen alleen via tabel()"
    verboden = ["BetCity", "ESPN-API", "ESPN.com", "Associated Press", "DraftKings", "Rotowire", "Betfans", "BPI"]
    assert not any(v.lower() in html.lower() for v in verboden), "geen bronnen/concurrenten"
    # SEO
    fk = "Spurs – Kings voorspelling"
    assert fk in TITEL and fk in SAMENVATTING and len(SAMENVATTING) <= 160
    assert fk in re.split(r"(?<=[.:!?])\s", re.sub(r"<[^>]+>", "", content))[0], "focuskeyword in eerste zin intro"
    assert any(fk in h for h in re.findall(r"<h3>(.*?)</h3>", html)), "focuskeyword in een h3"
    # Wedtip en consistentie
    assert set(WEDTIPS) == {"wedtip-1-2", "quotering-wedtip-1", "bookmaker-wedtips"}
    assert WEDTIPS["bookmaker-wedtips"] == "669ab9f5aceb8b717cea24c3"
    q = float(WEDTIPS["quotering-wedtip-1"])
    toto_odds = {1.05, 11.75, 1.93, 1.77, 1.87, 1.71, 1.98, 1.73, 1.95, 1.91}
    assert q in toto_odds and q == 1.87
    assert KAART["hs"] + KAART["as"] > 230.5, "voorspelde score moet Over 230,5 laten winnen"
    assert KAART["hs"] > KAART["as"], "voorspelling: Spurs winnen"
    assert KAART["hs"] - KAART["as"] < 17.5, "voorspelde marge onder de handicap: daarom geen -17,5"
    assert f"{KAART['hs']}-{KAART['as']}" in content and f"{KAART['hs']}-{KAART['as']}" in content3
    assert KAART["odd_home"] == "1,05" and KAART["odd_away"] == "11,75" and KAART["tijd"] == "01:00"
    assert KAART["home_abbr"] == "sa" and KAART["away_abbr"] == "sac"
    assert "1,87" in content and "1,87" in content3 and "230,5" in content
    assert "dinsdag rond 10:45 uur" in html
    assert SLUG == "spurs-kings-voorspelling-wedtips-nba-2026" and DATUM == "2026-10-28T00:00:00.000Z"
    tekst = re.sub(r"<[^>]+>", " ", html)
    print(len(TITEL), "tekens titel |", len(SAMENVATTING), "tekens samenvatting |", len(tekst.split()), "woorden")
    print("Alle asserts geslaagd (dry run, niets gepubliceerd).")
