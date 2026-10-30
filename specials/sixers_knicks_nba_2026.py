# -*- coding: utf-8 -*-
"""Los artikel: 76ers – Knicks voorspelling, NBA 31 oktober 2026 (00:30 NL, wintertijd; vrijdag 19:30 ET), Xfinity Mobile Arena.
NBA Cup, groepsfase (groep B Oost: NY, CLE, PHI, MIA, IND); telt ook mee voor de reguliere competitie.
Feiten nagelopen op 30-10-2026 rond 14:00 NL (ESPN-API: summary 401909280 incl. blessures, gameNote 'NBA Cup - Group Play';
boxscores 401909089 (Knicks – 76ers 100-106), 401909093, 401909855, 401909866, 401909884, 401909095, 401909863,
401909878, 401909886; teamschema's 2025/26 (regulier + play-offs) en 2026/27; standen 2025/26 en 2026/27; rosters en coaches;
spelersgemiddelden 2025/26 en 2026/27; onderlinge duels 2025/26 401810237, 401810342, 401810498, 401810635 en play-offs
401871159-401871162; officiële NBA-blessurelijst 30-10 06:00 ET; berichtgeving over de ruil Brown – George (1-7-2026),
Robinson naar Boston (1-7-2026) en de NBA Cup-groepen).
- Blessurelijst 30-10 06:00 ET: PHI Brown QUESTIONABLE (pijn linkerknie), Barlow out (stressreactie onderrug), Fall out
  (linkerquadriceps), Hukporti out (achillespees), Walker out (linkerknie, patellapees). NY Alvarado out (linkerenkel).
- Rust: beide speelden woensdag (US), donderdag vrij. PHI speelt zaterdag 31-10 18:00 ET in Charlotte (back-to-back);
  NY pas maandag 2-11 thuis tegen Brooklyn. Vorige back-to-back PHI: James rust eerste avond (rug), Embiid tweede avond.
- Onderling 2025/26 regulier 2-2 (PHI 116-107 en 130-119 in NY; NY 112-109 en 138-89 in PHI); play-offs tweede ronde 4-0 NY
  (137-98, 108-102, 108-94, 144-114). 2026/27: 106-100 PHI in New York (20-10).
- Stand 2025/26: PHI 45-37 (nr. 7 Oost, 23-18/22-19, 115,9/116,1); NY 53-29 (nr. 3 Oost, 30-10/22-19 + 1 neutraal,
  116,5/110,1), kampioen (4-2 ATL, 4-0 PHI, 4-0 CLE, 4-1 SA) en winnaar NBA Cup 2025.
- Feitenblad zei 'thuis 3-1' voor PHI: klopt niet (thuis 2-1, uit 2-0); niet gebruikt.
- Odds: alleen TOTO, uit specials/nba_feiten_2026_10_31.md (vrijdag ±13:45 NL). Winnaar, handicap en totaal incl. verlenging.
- Eén wedtip (eis eigenaar): Philadelphia 76ers +3,5 @1,63, onze kans 64% (odd 61,3%; zonder marge ±56%).
  python3 specials/sixers_knicks_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "76ers – Knicks voorspelling: wedtip en odds voor de NBA Cup-opener in Philadelphia (31 oktober, 00:30)"
SLUG = "76ers-knicks-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("76ers – Knicks voorspelling: Philadelphia (4-1) ontvangt cupwinnaar New York, met Jaylen Brown "
                "twijfelachtig. Wedtip, TOTO-odds en blessures.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet-experts.nl/go/bet365"
DATUM = "2026-10-30T23:30:00.000Z"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>76ers – Knicks voorspelling: in de nacht van vrijdag op zaterdag om 00:30 Nederlandse tijd ontvangt Philadelphia de New York Knicks in de eerste groepswedstrijd van de NBA Cup. Het duel telt ook mee voor de competitie. De 76ers (4-1) wonnen het eerste onderlinge duel van dit seizoen in New York, maar de Knicks schakelden Philadelphia in mei nog met 4-0 uit in de play-offs. Jaylen Brown staat met kniepijn als twijfelachtig op de blessurelijst. Onze voorspelling: 76ers – Knicks 112-109. Onze wedtip: Philadelphia 76ers +3,5 punten (inclusief verlenging) tegen een quotering van 1,63 bij TOTO.</strong></p>
<p>Hieronder lees je alles over vorm, blessures, de odds van <a href="/bookmakers/toto">TOTO</a> en onze onderbouwing.</p>
<h3><strong>76ers – Knicks: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "Philadelphia 76ers – New York Knicks"),
    ("Datum", "Zaterdag 31 oktober 2026 (vrijdagavond in de VS)"),
    ("Aanvang", "00:30 Nederlandse tijd (vrijdag 19:30 in Philadelphia)"),
    ("Arena", "Xfinity Mobile Arena, Philadelphia"),
    ("Competitie", "NBA, reguliere competitie 2026/27 en NBA Cup (groep B Oost)"),
    ("Stand 2026/27", "76ers 4-1, Knicks 2-3"),
    ("Eerste duel 2026/27", "Knicks – 76ers 100-106"),
])}
<p>Beide ploegen hadden donderdag vrij. Philadelphia speelt zaterdag alweer in Charlotte, de Knicks pas maandag. In groep B van de NBA Cup zitten verder Cleveland, Miami en Indiana; New York verdedigt de beker die het vorig seizoen won.</p>
<h3><strong>De eerste week: Philadelphia stabiel, New York herstelt zich</strong></h3>
<p><strong>Philadelphia 76ers: vier zeges in vijf duels</strong></p>
<p>De ploeg van coach Nick Nurse opende met een 100-106 zege in Madison Square Garden: 28 punten van Tyrese Maxey, terwijl Joel Embiid maar 4 van zijn 15 schoten raakte. Daarna kwam Philadelphia tegen Cleveland terug van 29 punten achterstand (114-106) en won het zonder LeBron James (rust voor zijn rug) met 127-116 van Milwaukee. Een avond later, zonder Embiid (rust) en VJ Edgecombe (buikspieren), ging het mis tegen Detroit: 93-106. Woensdag volgde een 109-114 zege in Indianapolis, met 27 punten van Maxey, 20 punten en 10 rebounds van Brown en 20 punten van invaller Anfernee Simons.</p>
<p><strong>New York Knicks: na drie nederlagen twee keer winst</strong></p>
<p>De Knicks begonnen met 0-3: na Philadelphia volgden nederlagen in Boston (107-103) en thuis tegen Orlando (102-111). Dinsdag kwam de ommekeer: 111-97 tegen Detroit, met 27 punten en 20 rebounds van Karl-Anthony Towns. Een dag later won New York met 127-133 in Chicago, na in de tweede helft nog 19 punten achter te hebben gestaan. Jalen Brunson maakte 38 punten.</p>
<h3><strong>Vorig seizoen en de onderlinge duels</strong></h3>
<p>New York werd vorig seizoen kampioen, met in de finale 4-1 tegen San Antonio. Philadelphia kwam in de eerste ronde tegen Boston terug van 1-3, maar ging daarna met 0-4 onderuit tegen de Knicks.</p>
{tabel(["2025/26", "Philadelphia 76ers", "New York Knicks"], [
    ("Eindstand", "45-37 (nr. 7 Oost)", "53-29 (nr. 3 Oost)"),
    ("Thuis / uit", "23-18 / 22-19", "30-10 / 22-19*"),
    ("Punten voor / tegen", "115,9 / 116,1", "116,5 / 110,1"),
    ("Onderling (regulier)", "2-2", "2-2"),
    ("Na het seizoen", "Tweede ronde (0-4 tegen New York)", "Kampioen (4-1 tegen San Antonio)"),
])}
<p><em>* De Knicks wonnen daarnaast één wedstrijd op neutraal terrein.</em></p>
<p>In de competitie won steeds de uitploeg: Philadelphia twee keer in New York (116-107 en 130-119), de Knicks twee keer in Philadelphia (112-109 en 138-89). In de play-offs was het eenrichtingsverkeer: 137-98, 108-102, 108-94 en 144-114. Maar Philadelphia speelde toen nog met Paul George en Kelly Oubre jr., niet met Brown en James.</p>"""

content2 = f"""<h3><strong>Zo zijn beide selecties veranderd</strong></h3>
<p><strong>Philadelphia 76ers: Brown en James erbij</strong></p>
<p>Begin juli haalde Philadelphia Jaylen Brown uit Boston, in ruil voor Paul George en draftkeuzes. Daarna kwam de 41-jarige LeBron James over van de Lakers. Ook Simons, Kentavious Caldwell-Pope en Dean Wade zijn nieuw. Center Andre Drummond vertrok naar New York.</p>
<p><strong>New York Knicks: de titelploeg blijft bij elkaar</strong></p>
<p>De basisvijf van de titel is intact: Brunson, Mikal Bridges, Josh Hart, OG Anunoby en Towns. Mitchell Robinson vertrok naar Boston; Drummond is nu de eerste invaller onder de ring. Mike Brown is de coach.</p>
<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("Jaylen Brown", "Philadelphia", "Twijfelachtig (pijn linkerknie)"),
    ("Dominick Barlow", "Philadelphia", "Speelt niet (onderrug)"),
    ("Tacko Fall", "Philadelphia", "Speelt niet (linkerbovenbeen)"),
    ("Ariel Hukporti, Jabari Walker", "Philadelphia", "Spelen niet (achillespees, linkerknie)"),
    ("Jose Alvarado", "New York", "Speelt niet (verstuikte linkerenkel)"),
])}
<p><em>Stand van de officiële NBA-blessurelijst op vrijdag 30 oktober, 06:00 uur Amerikaanse tijd (11:00 Nederlandse tijd).</em></p>
<p>Brown speelde woensdag nog 34 minuten; of hij kan spelen, wordt pas kort voor de wedstrijd duidelijk. Embiid, James en Edgecombe staan niet op de lijst. Let wel op de back-to-back: de vorige keer rustte James op de eerste avond en Embiid op de tweede.</p>
<p><strong>Verwachte basisvijf 76ers:</strong> Tyrese Maxey, VJ Edgecombe, Jaylen Brown, LeBron James, Joel Embiid. Speelt Brown niet, dan ligt Caldwell-Pope of Wade het meest voor de hand. Simons is de belangrijkste invaller.</p>
<p><strong>Verwachte basisvijf Knicks:</strong> Jalen Brunson, Mikal Bridges, Josh Hart, OG Anunoby, Karl-Anthony Towns. Dezelfde vijf als in alle vijf de wedstrijden. Landry Shamet, Jordan Clarkson, Drummond en Miles McBride komen van de bank.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "2026/27 tot nu toe"], [
    ("Tyrese Maxey (PHI)", "28,3", "4,1", "6,6", "28,4 ptn, 4,6 ast"),
    ("Joel Embiid (PHI)", "26,9", "7,7", "3,9", "21,5 ptn, 10,0 reb"),
    ("Jaylen Brown (PHI)", "28,7*", "6,9*", "5,1*", "20,6 ptn, 6,6 reb"),
    ("LeBron James (PHI)", "20,9*", "6,1*", "7,2*", "15,5 ptn, 6,8 ast"),
    ("Jalen Brunson (NY)", "26,0", "3,3", "6,8", "25,8 ptn, 40,2% uit het veld"),
    ("Karl-Anthony Towns (NY)", "20,1", "11,9", "3,0", "21,8 ptn, 13,8 reb"),
    ("OG Anunoby (NY)", "16,7", "5,2", "2,2", "17,6 ptn, 6,2 reb"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26. * Brown bij Boston, James bij de Lakers. Embiid speelde vorig seizoen 38 wedstrijden.</em></p>
<p><strong>Tyrese Maxey</strong> scoorde dit seizoen in elke wedstrijd minstens 26 punten. <strong>Karl-Anthony Towns</strong> is de Knick in vorm; zijn duel met Embiid onder de ring wordt belangrijk. <strong>Mikal Bridges</strong> zit in een dip: 5,0 punten per wedstrijd en 27 procent uit het veld.</p>
<h3><strong>Odds 76ers – Knicks bij TOTO</strong></h3>
<p>TOTO ziet de Knicks als lichte favoriet: een quotering van 1,83 staat voor ongeveer 55 procent winkans. De handicap ligt rond 1,5 punt in het voordeel van New York, het verwachte puntentotaal rond de 227,5.</p>
{tabel(["Markt (TOTO)", "76ers", "Knicks"], [
    ("Winnaar (incl. verlenging)", "2,00", "1,83"),
    ("1X2 (reguliere speeltijd, gelijk 16,00)", "2,05", "1,87"),
    ("Handicap +1,5 / -1,5 (incl. verlenging)", "1,91", "1,91"),
    ("Handicap +2,5 / -2,5 (incl. verlenging)", "1,73", "1,98"),
    ("Handicap +3,5 / -3,5 (incl. verlenging)", "1,63", "2,10"),
])}
<p>Op het totaal biedt TOTO 225,5 punten (Over 1,69 / Under 2,00), 227,5 (1,91 / 1,91) en 228,5 (Over 1,93 / Under 1,77). Odds gelezen op vrijdag rond 13:45 uur; vergelijk ze vlak voor de start nog even, want nieuws over Brown kan de lijn verschuiven.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op 76ers – Knicks</strong></a></p>"""

content3 = f"""<h3><strong>Onze 76ers – Knicks voorspelling: een spannend duel</strong></h3>
<p>Philadelphia heeft de betere start, Maxey is in vorm en met Simons heeft Nurse een invaller die een wedstrijd kan kantelen.</p>
<p>New York komt wel op stoom, met twee zeges op rij. Toch is de aanval nog niet overtuigend: Brunson schiet 40 procent, Anunoby raakt 27 procent van zijn driepunters en Bridges is uit vorm. Onze voorspelling: <strong>Philadelphia 76ers – New York Knicks 112-109</strong>.</p>
<h3><strong>Onze wedtip: 76ers +3,5 (1,63)</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Onze kans"], [
    ("Philadelphia 76ers +3,5 punten (incl. verlenging)", "1,63", "TOTO", "Ongeveer 64 procent"),
])}
<p><strong>Waarom deze tip?</strong> Bij een handicap van +3,5 tellen we 3,5 punten op bij de score van Philadelphia, inclusief een eventuele verlenging. De tip is dus goed als Philadelphia wint, of verliest met maximaal drie punten. Een rekenvoorbeeld: verliest Philadelphia met 108-110, dan wordt het 111,5 tegen 110 en is de tip goed. Bij 106-110 wordt het 109,5 tegen 110 en is de tip verloren. Een odd van 1,63 staat voor 61,3 procent kans; zonder de marge van de bookmaker ongeveer 56 procent. Wij schatten de kans op ongeveer 64 procent. De onderbouwing:</p>
<p><strong>1. Philadelphia won het eerste duel al.</strong> Op 20 oktober won Philadelphia met 106-100 in Madison Square Garden, terwijl Embiid 4 uit 15 schoot. Nu speelt Philadelphia thuis.</p>
<p><strong>2. Maxey tegen een Knicks-aanval die nog zoekt.</strong> Maxey scoorde in elke wedstrijd minstens 26 punten en maakte vorig seizoen in de vier competitieduels met New York gemiddeld 30 punten. De Knicks bleven in hun eerste drie duels steeds op 103 punten of minder steken. Pas in Chicago, tegen een ploeg die 130 punten per duel tegen krijgt, liep het.</p>
<p><strong>3. Een buffer tegen de twijfel.</strong> Met Brown twijfelachtig en een uitwedstrijd in Charlotte een dag later, kiezen we bewust niet voor een kale zege. De +3,5 beschermt je bij een nipte nederlaag, en die is reëel tussen twee bijna even sterk ingeschatte ploegen.</p>
<p><strong>Waarom niet een andere markt?</strong> Philadelphia als winnaar (2,00) vraagt om 50 procent kans; wij komen uit op ongeveer 53 procent, zonder buffer bij een nipt verlies. +2,5 (1,73) betaalt iets meer, maar een verschil van precies drie punten komt in de NBA vaak voor. Het puntentotaal laten we liggen: onze voorspelling komt uit op 221 punten, onder alle lijnen van TOTO, en een over past daar niet bij.</p>
<p><strong>Het risico.</strong> Speelt Brown niet en spaart Nurse ook nog een ster voor Charlotte, dan wordt het lastig. Brunson kan een wedstrijd in zijn eentje beslissen. Let ook op: de handicap telt een eventuele verlenging mee. Meer uitleg vind je in onze gidsen over <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap wedden</a> en de <a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">money line</a>.</p>
<h3><strong>76ers – Knicks live kijken in Nederland</strong></h3>
<p>In de Verenigde Staten zendt Prime Video de wedstrijd uit. Bij <a href="/bookmakers/bet365">Bet365</a> kun je NBA-wedstrijden live volgen via de livestream. Je hebt daarvoor een account met een storting nodig. ESPN zendt in Nederland een deel van de NBA-wedstrijden uit; in de programmagids zie je of deze erbij zit. Met <strong>NBA League Pass</strong>, de betaalde dienst van de competitie, kun je alle wedstrijden volgen. Meer opties vind je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk 76ers – Knicks live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Vannacht schreven we ook voorbeschouwingen van <a href="/nieuws/mavericks-rockets-voorspelling-wedtips-nba-2026">Mavericks – Rockets</a>, <a href="/nieuws/warriors-lakers-voorspelling-wedtips-nba-2026">Warriors – Lakers</a> en <a href="/nieuws/suns-nuggets-voorspelling-wedtips-nba-2026">Suns – Nuggets</a>. Eerder deze week schreven we over <a href="/nieuws/pacers-76ers-voorspelling-wedtips-nba-2026">Pacers – 76ers</a> en <a href="/nieuws/knicks-pistons-voorspelling-wedtips-nba-2026">Knicks – Pistons</a>. Benieuwd <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">welke Nederlanders in de NBA spelen</a>? Nieuw met basketbal? Lees <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels in de NBA</a>. Alle tips staan op <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint 76ers – Knicks?</strong><br>In de nacht van vrijdag op zaterdag 31 oktober 2026 om 00:30 Nederlandse tijd. In Philadelphia is het dan vrijdagavond 19:30.</p>
<p><strong>Speelt Jaylen Brown mee?</strong><br>Dat is nog niet zeker. Hij staat op de officiële NBA-blessurelijst als twijfelachtig, met pijn aan zijn linkerknie. Joel Embiid en LeBron James staan niet op de lijst. Bij de Knicks ontbreekt alleen Jose Alvarado.</p>
<p><strong>Wie is favoriet: 76ers of Knicks?</strong><br>De Knicks, nipt, met een quotering van 1,83 bij TOTO. Philadelphia staat op 2,00.</p>
<p><strong>Wat is onze voorspelling voor 76ers – Knicks?</strong><br>Philadelphia wint met 112-109. Onze wedtip is Philadelphia 76ers +3,5 punten, inclusief verlenging (1,63 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

KAART = {"home": "76ers", "away": "Knicks", "home_abbr": "phi", "away_abbr": "ny", "home_pos": "45-37 · nr. 7 Oost 2025/26", "away_pos": "53-29 · nr. 3 Oost 2025/26", "hs": 112, "as": 109, "datum": "Za 31 okt", "tijd": "00:30", "odd_home": "2,00", "odd_away": "1,83"}
WEDTIPS = {"wedtip-1-2": "Philadelphia 76ers +3,5 punten (incl. verlenging)", "quotering-wedtip-1": "1.63",
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
    toegestaan = {"/nieuws/nba-voorspellingen-vannacht-29-oktober-2026",
                  "/nieuws/pacers-76ers-voorspelling-wedtips-nba-2026", "/nieuws/bucks-rockets-voorspelling-wedtips-nba-2026",
                  "/nieuws/mavericks-thunder-voorspelling-wedtips-nba-2026",
                  "/nieuws/clippers-lakers-voorspelling-wedtips-nba-2026",
                  "/nieuws/lakers-warriors-voorspelling-wedtips-nba-2026", "/nieuws/thunder-nuggets-voorspelling-wedtips-nba-2026",
                  "/nieuws/knicks-pistons-voorspelling-wedtips-nba-2026", "/nieuws/76ers-pistons-voorspelling-wedtips-nba-2026",
                  "/nieuws/heat-mavericks-voorspelling-wedtips-nba-2026", "/nieuws/rockets-hawks-voorspelling-wedtips-nba-2026",
                  "/nieuws/suns-warriors-voorspelling-wedtips-nba-2026", "/nieuws/nuggets-warriors-voorspelling-wedtips-nba-2026",
                  "/nieuws/mavericks-rockets-voorspelling-wedtips-nba-2026",
                  "/nieuws/warriors-lakers-voorspelling-wedtips-nba-2026",
                  "/nieuws/suns-nuggets-voorspelling-wedtips-nba-2026",
                  "/nieuws/welke-nederlanders-spelen-in-de-nba",
                  "/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders",
                  "/nieuws/wat-is-handicap-wedden-de-complete-gids",
                  "/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners",
                  "/wedden-op-nba-voorspellingen-en-wedtips---basketbal", "/bookmakers/toto", "/bookmakers/bet365",
                  "/live-kijken", BET365}
    assert set(hrefs) <= toegestaan, set(hrefs) - toegestaan
    assert SLUG not in "".join(hrefs), "niet naar zichzelf linken"
    for s in ("mavericks-rockets", "warriors-lakers", "suns-nuggets"):
        assert f"/nieuws/{s}-voorspelling-wedtips-nba-2026" in hrefs, f"link naar {s} ontbreekt"
    assert not any("nba-voorspellingen-vannacht" in h for h in hrefs), "vannacht geen algemeen artikel"
    assert "/nieuws/pacers-76ers-voorspelling-wedtips-nba-2026" in hrefs, "eerder artikel 76ers"
    assert "/nieuws/knicks-pistons-voorspelling-wedtips-nba-2026" in hrefs, "eerder artikel Knicks"
    assert "<table" not in html.replace(f"<table {T}>", ""), "tabellen alleen via tabel()"
    verboden = ["BetCity", "ESPN-API", "ESPN.com", "Associated Press", "DraftKings", "Rotowire", "Betfans", "Shams",
                "Klutch", "Charania", "Fox Sports", "NBC Sports"]
    assert not any(v.lower() in html.lower() for v in verboden), "geen bronnen/concurrenten"
    # SEO: focuskeyword
    fk = "76ers – Knicks voorspelling"
    assert fk in TITEL and fk in SAMENVATTING and len(SAMENVATTING) <= 160, len(SAMENVATTING)
    assert re.sub(r"<[^>]+>", "", content).startswith(fk), "focuskeyword in de eerste zin"
    assert any(fk in h for h in re.findall(r"<h3>(.*?)</h3>", html)), "focuskeyword in een h3"
    assert "(31 oktober, 00:30)" in TITEL
    # Wedtip en consistentie
    assert set(WEDTIPS) == {"wedtip-1-2", "quotering-wedtip-1", "bookmaker-wedtips"}
    assert WEDTIPS["bookmaker-wedtips"] == "669ab9f5aceb8b717cea24c3"
    q = float(WEDTIPS["quotering-wedtip-1"])
    toto_odds = {2.00, 1.83, 2.05, 1.87, 16.00, 2.20, 1.57, 1.67, 1.91, 1.73, 1.98, 1.63, 2.10, 1.69, 1.77, 1.93}
    assert q in toto_odds and q == 1.63
    assert KAART["hs"] + 3.5 > KAART["as"], "voorspelde score moet 76ers +3,5 laten winnen"
    assert f"{KAART['hs']}-{KAART['as']}" in content and f"{KAART['hs']}-{KAART['as']}" in content3
    assert KAART["odd_home"] == "2,00" and KAART["odd_away"] == "1,83" and KAART["tijd"] == "00:30"
    assert KAART["home"] == "76ers" and KAART["away"] == "Knicks"
    assert KAART["home_abbr"] == "phi" and KAART["away_abbr"] == "ny" and KAART["datum"] == "Za 31 okt"
    assert "1,63" in content and "1,63" in content3 and "+3,5" in content and "+3,5" in content3
    assert "inclusief verlenging" in content and "incl. verlenging" in WEDTIPS["wedtip-1-2"]
    assert "vrijdag rond 13:45 uur" in html, "tijdstip odds"
    assert html.count("👉 Klik hier: maak je Bet365-account aan en wed live mee op") == 1
    assert len(re.findall(r"<p><strong>[123]\. ", content3)) == 3, "onderbouwing in 3 punten"
    assert "Waarom niet een andere markt?" in content3
    assert "rekenvoorbeeld" in content3.lower(), "rekenvoorbeeld handicap"
    assert "thuis 3-1" not in html, "PHI is thuis 2-1"
    assert SLUG == "76ers-knicks-voorspelling-wedtips-nba-2026" and DATUM == "2026-10-30T23:30:00.000Z"
    tekst = re.sub(r"<[^>]+>", " ", html)
    woorden = len(tekst.split())
    assert 1400 <= woorden <= 1850, woorden
    print(len(TITEL), "tekens titel |", len(SAMENVATTING), "tekens samenvatting |", woorden, "woorden")
    print("Alle asserts geslaagd (dry run, niets gepubliceerd).")
