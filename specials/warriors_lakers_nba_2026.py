# -*- coding: utf-8 -*-
"""Los artikel: Warriors – Lakers voorspelling, NBA 31 oktober 2026 (03:00 NL, wintertijd; vrijdag 19:00 PT), Chase Center
San Francisco. Eerste groepsduel van de NBA Cup (West Groep C), telt ook mee voor de reguliere competitie.
Feiten nagelopen op 30-10-2026 rond 14:00 NL (ESPN-API: summary 401909285 incl. blessures en NBA Cup-notitie; boxscores
2026/27 401909092 (Lakers – Warriors 127-105), 401909850, 401909860, 401909876, 401909888 (Timberwolves – Warriors 114-119),
401909851, 401909861, 401909880 en 401909892 (Clippers – Lakers 87-103, zonder Dončić); teamschema's 2025/26 incl. play-offs
en play-in; standen 2025/26; spelersgemiddelden 2025/26 en 2026/27; onderlinge duels 2025/26 401809244, 401810608,
401810721, 401811025; officiële NBA-blessurelijst 30-10 06:00 ET; NBA.com-preview NBA Cup West Groep C; berichtgeving over
Dončić (rugklachten, rust op de back-to-back, niet op de lijst voor vrijdag), Porziņģis (niet bij de ploeg) en de
zomertransfers van de Lakers (Kessler sign-and-trade, Reaves vier jaar)).
- Blessurelijst 30-10 06:00 ET: LAL Carr out (rechter schuine buikspier), Thiero out (linkerknie), Ziaire Williams
  questionable (linkervoet/hiel), Kessler available (spalk linkervinger). GSW Butler out (kruisband), Moody out
  (patellapees linkerknie), Porziņģis out (niet bij de ploeg), Santos doubtful (tendinitis linkerknie).
  Dončić, Reaves en Curry staan er niet op.
- Rust: beide ploegen speelden woensdag (US) en hadden donderdag vrij; geen back-to-back.
- Onderling 2025/26: 3-1 LAL (109-119 GSW in LA, 105-99 LAL in LA, 129-101 en 119-103 LAL in SF). Curry en Dončić stonden
  alleen in het eerste duel allebei op het veld.
- Stand 2025/26: GSW 37-45 (nr. 10 West, 22-19/15-26, 114,6/115,2, play-in: 126-121 bij LAC, 96-111 bij PHX);
  LAL 53-29 (nr. 4 West, 28-13/25-16, 116,3/114,6; 4-2 tegen HOU, 0-4 tegen OKC).
- Odds: alleen TOTO, uit specials/nba_feiten_2026_10_31.md (vr ±13:45 NL). Winnaar/handicap/totaal incl. verlenging.
- Eén wedtip (vast, eigenaar): Los Angeles Lakers wint (incl. verlenging) @1,74, onze kans 61% (odd 57,5%, zonder marge ±55%).
  python3 specials/warriors_lakers_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "Warriors – Lakers voorspelling: wedtip en odds voor de NBA Cup-opener in San Francisco (31 oktober, 03:00)"
SLUG = "warriors-lakers-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("Warriors – Lakers voorspelling: NBA Cup-opener, Dončić terug en Golden State zonder Butler, Porziņģis "
                "en Moody. Wedtip, TOTO-odds en blessures.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet-experts.nl/go/bet365"
DATUM = "2026-10-31T02:00:00.000Z"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>Warriors – Lakers voorspelling: in de nacht van vrijdag op zaterdag om 03:00 Nederlandse tijd ontvangt Golden State de Los Angeles Lakers in het Chase Center. Het is de tweede ontmoeting in tien dagen en voor beide ploegen het eerste groepsduel in de NBA Cup. De Lakers (4-1) wonnen de opener met 127-105 en krijgen Luka Dončić terug na een rustbeurt. Golden State (2-3) won zijn laatste twee wedstrijden, maar mist Jimmy Butler, Kristaps Porziņģis en Moses Moody. Onze voorspelling: Warriors – Lakers 112-118. Onze wedtip: Los Angeles Lakers wint (inclusief verlenging) tegen een quotering van 1,74 bij TOTO.</strong></p>
<p>Hieronder lees je alles over vorm, blessures, de odds van <a href="/bookmakers/toto">TOTO</a> en onze onderbouwing.</p>
<h3><strong>Warriors – Lakers: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "Golden State Warriors – Los Angeles Lakers"),
    ("Datum", "Zaterdag 31 oktober 2026 (vrijdagavond in de VS)"),
    ("Aanvang", "03:00 Nederlandse tijd (vrijdag 19:00 in San Francisco)"),
    ("Arena", "Chase Center, San Francisco"),
    ("Competitie", "NBA, reguliere competitie 2026/27 en NBA Cup (West Groep C)"),
    ("Stand 2026/27", "Warriors 2-3, Lakers 4-1"),
    ("Onderlinge duels", "3-1 voor de Lakers in 2025/26, 1-0 voor de Lakers dit seizoen"),
])}
<p>Het is ook voor beide ploegen het eerste groepsduel in de NBA Cup (West Groep C, met verder Portland, Sacramento en San Antonio). Beide ploegen hadden donderdag vrij; niemand speelt op een back-to-back.</p>
<h3><strong>De eerste anderhalve week: Lakers sterk, Warriors in de lift</strong></h3>
<p><strong>Golden State Warriors: drie keer verlies, dan twee uitzeges</strong></p>
<p>Golden State verloor de opener in Los Angeles met 105-127 en raakte daar maar 8 van de 36 driepunters. Na nederlagen tegen Memphis (108-111) en in Phoenix (122-131) volgden twee uitzeges: 134-114 in Denver, met 31 punten van rookie Yaxel Lendeborg, en 119-114 in Minnesota, waar Stephen Curry 44 punten maakte. De enige thuiswedstrijd tot nu toe ging verloren.</p>
<p><strong>Los Angeles Lakers: vier zeges en een misstap</strong></p>
<p>De ploeg van coach JJ Redick won van Golden State, de Clippers (125-117) en in Utah (132-123, met 52 punten van Dončić). Thuis tegen Portland ging het mis (129-136), ondanks 41 punten van Dončić. Een dag later rustte hij met rugklachten, maar Los Angeles won toch met 103-87 bij de Clippers. De Lakers scoren 123,2 punten per wedstrijd en krijgen er 113,6 tegen.</p>
<h3><strong>Vorig seizoen en de onderlinge duels</strong></h3>
<p>De Lakers werden vorig seizoen vierde in het Westen, versloegen Houston in de play-offs (4-2) en verloren daarna met 0-4 van Oklahoma City. Golden State werd tiende en strandde in de play-in in Phoenix (96-111).</p>
{tabel(["2025/26", "Golden State Warriors", "Los Angeles Lakers"], [
    ("Eindstand", "37-45 (nr. 10 West)", "53-29 (nr. 4 West)"),
    ("Thuis / uit", "22-19 / 15-26", "28-13 / 25-16"),
    ("Punten voor / tegen", "114,6 / 115,2", "116,3 / 114,6"),
    ("Onderling", "1-3", "3-1"),
    ("Na het seizoen", "Uitgeschakeld in de play-in", "Tweede ronde (0-4 tegen Oklahoma City)"),
])}
<p>Golden State won het eerste duel van vorig seizoen met 119-109 in Los Angeles (31 punten van Butler, 43 van Dončić). Daarna won Los Angeles drie keer; Curry deed in die duels niet mee. In de opener van dit seizoen raakte Walker Kessler al zijn twaalf schoten uit het veld (26 punten) en scoorden de Lakers 66 punten in de bucket.</p>"""

content2 = f"""<h3><strong>Zo zijn beide selecties veranderd</strong></h3>
<p><strong>Los Angeles Lakers: alles draait om Dončić en Reaves</strong></p>
<p>LeBron James vertrok naar Philadelphia. De Lakers haalden center Walker Kessler uit Utah via een sign-and-trade (vier jaar, 130 miljoen dollar), Austin Reaves tekende bij voor vier jaar en ook Grimes, Sexton, Sandro Mamukelashvili en Matisse Thybulle kwamen erbij. Deandre Ayton, Rui Hachimura, Marcus Smart en Luke Kennard vertrokken. Redick is bezig aan zijn derde seizoen.</p>
<p><strong>Golden State Warriors: Lendeborg is de grote verrassing</strong></p>
<p>Coach Steve Kerr houdt de kern bij elkaar: Draymond Green, Al Horford en Porziņģis tekenden opnieuw, Jonathan Kuminga speelt nu voor Minnesota. Nieuwkomer Lendeborg, de nummer elf van de draft en beste speler van de Summer League, is al de tweede scorer. De Nederlander Malevy Leons (two-way-contract) kreeg in drie wedstrijden een paar minuten.</p>
<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("Jimmy Butler", "Golden State", "Speelt niet (herstel van kruisbandoperatie)"),
    ("Moses Moody", "Golden State", "Speelt niet (operatie aan de linkerknie)"),
    ("Kristaps Porziņģis", "Golden State", "Speelt niet (niet bij de ploeg, gezondheid)"),
    ("Gui Santos", "Golden State", "Onwaarschijnlijk (peesontsteking linkerknie)"),
    ("Ziaire Williams", "LA Lakers", "Twijfelachtig (linkervoet en hiel)"),
    ("Cameron Carr", "LA Lakers", "Speelt niet (buikspier)"),
    ("Adou Thiero", "LA Lakers", "Speelt niet (linkerknie)"),
    ("Walker Kessler", "LA Lakers", "Inzetbaar (spalk om linkervinger)"),
])}
<p><em>Stand van de officiële NBA-blessurelijst op vrijdag 30 oktober, 06:00 uur Amerikaanse tijd (11:00 Nederlandse tijd).</em></p>
<p>Dončić, Reaves en Curry staan niet op de lijst. Santos miste woensdag al de wedstrijd in Minnesota.</p>
<p><strong>Verwachte basisvijf Warriors:</strong> Stephen Curry, Brandin Podziemski, Yaxel Lendeborg, Georges Niang, Draymond Green. Zo begon Golden State in Minnesota. De'Anthony Melton, Horford, Brandon Williams en Gary Payton II zijn de belangrijkste wissels.</p>
<p><strong>Verwachte basisvijf Lakers:</strong> Luka Dončić, Austin Reaves, Matisse Thybulle, Ziaire Williams, Walker Kessler, de basisvijf van de eerste vier wedstrijden. Is Williams niet fit, dan begint Jake LaRavia of Grimes.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "2026/27 tot nu toe"], [
    ("Luka Dončić (LAL)", "33,5", "7,7", "8,3", "36,0 ptn, 8,3 ast"),
    ("Austin Reaves (LAL)", "23,3", "4,7", "5,5", "24,4 ptn, 5,4 ast"),
    ("Walker Kessler (LAL)", "14,4*", "10,8*", "3,0*", "14,8 ptn, 8,2 reb"),
    ("Stephen Curry (GSW)", "26,6", "3,6", "4,7", "28,8 ptn, 3,5 ast"),
    ("Yaxel Lendeborg (GSW)", "-", "-", "-", "22,6 ptn, 9,2 reb, 4,0 ast"),
    ("Brandin Podziemski (GSW)", "13,8", "5,1", "3,7", "14,7 ptn, 4,7 ast"),
    ("Draymond Green (GSW)", "8,4", "5,5", "5,5", "3,3 ptn, 6,8 ast"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26. * Kessler speelde vorig seizoen vijf wedstrijden voor Utah. Lendeborg is rookie. Curry speelde vorig seizoen 43 wedstrijden, Dončić 64.</em></p>
<p><strong>Luka Dončić</strong> was vorig seizoen topscorer van de NBA en zit nu op 36 punten per wedstrijd. <strong>Stephen Curry</strong> speelt gemiddeld 27 minuten, maar kan een wedstrijd alleen beslissen. Onder de ring gaat het om <strong>Walker Kessler</strong> tegen een ploeg zonder echte center. <strong>Yaxel Lendeborg</strong> scoorde in zijn laatste vier wedstrijden telkens 18 punten of meer.</p>
<h3><strong>Odds Warriors – Lakers bij TOTO</strong></h3>
<p>TOTO ziet de Lakers als favoriet: een quotering van 1,74 staat voor ongeveer 57 procent winkans. De handicap ligt rond 2,5 punten, het verwachte totaal rond 234,5.</p>
{tabel(["Markt (TOTO)", "Warriors", "Lakers"], [
    ("Winnaar (incl. verlenging)", "2,15", "1,74"),
    ("1X2 (reguliere speeltijd, gelijk 17,00)", "2,20", "1,73"),
    ("Handicap +1,5 / -1,5 (incl. verlenging)", "1,95", "1,73"),
    ("Handicap +2,5 / -2,5 (incl. verlenging)", "1,91", "1,91"),
    ("Handicap +3,5 / -3,5 (incl. verlenging)", "1,71", "1,98"),
])}
<p>Op het totaal biedt TOTO 233,5 punten (Over 1,83 / Under 1,98), 234,5 (1,93 / 1,87) en 235,5 (1,95 / 1,73). Odds gelezen op vrijdag rond 13:45 uur; check ze vlak voor de start, zeker bij nieuws over Santos of Ziaire Williams.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op Warriors – Lakers</strong></a></p>"""

content3 = f"""<h3><strong>Onze voorspelling: de Lakers winnen opnieuw, maar het wordt spannender</strong></h3>
<p>De Lakers hebben de twee beste aanvallers op het veld en een center waar Golden State zonder Porziņģis geen antwoord op heeft.</p>
<p>Toch verwachten we geen herhaling van 127-105. De Warriors spelen thuis, wonnen twee keer op rij en raakten in de opener maar 22 procent van hun driepunters. Ook de Lakers zijn achterin kwetsbaar, zoals Portland liet zien. Onze voorspelling: <strong>Golden State Warriors – Los Angeles Lakers 112-118</strong>.</p>
<h3><strong>Onze wedtip: Lakers winnen (1,74)</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Onze kans"], [
    ("Los Angeles Lakers wint (incl. verlenging)", "1,74", "TOTO", "Ongeveer 61 procent"),
])}
<p><strong>Waarom deze tip?</strong> De tip is goed als de Lakers winnen, ook als dat pas na verlenging gebeurt. Een odd van 1,74 staat voor een kans van 57,5 procent; zonder de marge van de bookmaker is dat ongeveer 55 procent. Wij schatten de kans op ongeveer 61 procent. De onderbouwing:</p>
<p><strong>1. Golden State mist lengte.</strong> Zonder Porziņģis staan Green (36) en Horford (40) tegenover Kessler. In de opener won Los Angeles de strijd in de bucket met 66 tegen 56 punten.</p>
<p><strong>2. Dončić is terug en uitgerust.</strong> Zijn rustbeurt op de back-to-back was een voorzorgsmaatregel. In zijn vier wedstrijden scoorde hij 28, 23, 52 en 41 punten, en met Reaves (24,4 punten) heeft Los Angeles twee spelers die een wedstrijd kunnen beslissen.</p>
<p><strong>3. De Lakers hebben de bredere selectie.</strong> Zonder Dončić wonnen ze met zestien punten bij de Clippers. Golden State mist met Butler, Porziņģis, Moody en waarschijnlijk Santos vier rotatiespelers en leunt zwaar op Curry en Lendeborg.</p>
<p><strong>Waarom niet een andere markt?</strong> Lakers -1,5 betaalt met 1,73 zelfs minder dan de winnaarsmarkt, terwijl je bij een zege met één punt verliest. Lakers -2,5 (1,91) betaalt meer, maar vraagt een zege met minstens drie punten. Een voorbeeld: bij 113-115 is onze tip goed, maar verliest -2,5. Tegen een Curry in vorm is een krappe uitslag goed mogelijk. De 1X2-markt (1,73) telt alleen de reguliere speeltijd. Het puntentotaal laten we liggen: onze voorspelling komt uit op 230 punten, iets onder de lijn.</p>
<p><strong>Het risico.</strong> Curry scoorde in Minnesota 44 punten; valt zijn schot zo, dan kan Golden State iedereen verslaan. De Lakers kregen tegen Portland 136 punten tegen, en basisspeler Ziaire Williams is twijfelachtig. Meer uitleg vind je in onze gidsen over de <a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">money line</a> en <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap wedden</a>.</p>
<h3><strong>Warriors – Lakers live kijken in Nederland</strong></h3>
<p>Bij <a href="/bookmakers/bet365">Bet365</a> kun je NBA-wedstrijden live volgen via de livestream. Je hebt daarvoor een account met een storting nodig. In de Verenigde Staten is de wedstrijd te zien bij Prime Video. ESPN zendt in Nederland een deel van de NBA-wedstrijden uit; in de programmagids zie je of deze erbij zit. Met <strong>NBA League Pass</strong>, de betaalde dienst van de competitie, kun je alle wedstrijden volgen. Meer opties vind je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk Warriors – Lakers live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Vannacht schreven we ook voorbeschouwingen van <a href="/nieuws/76ers-knicks-voorspelling-wedtips-nba-2026">76ers – Knicks</a>, <a href="/nieuws/mavericks-rockets-voorspelling-wedtips-nba-2026">Mavericks – Rockets</a> en <a href="/nieuws/suns-nuggets-voorspelling-wedtips-nba-2026">Suns – Nuggets</a>. Onze voorbeschouwing van de eerste ontmoeting lees je in <a href="/nieuws/lakers-warriors-voorspelling-wedtips-nba-2026">Lakers – Warriors</a>, en eerder deze week schreven we over <a href="/nieuws/clippers-lakers-voorspelling-wedtips-nba-2026">Clippers – Lakers</a>. Benieuwd <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">welke Nederlanders in de NBA spelen</a>? Nieuw met basketbal? Lees <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels in de NBA</a>. Alle tips staan op <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Warriors – Lakers?</strong><br>Zaterdag 31 oktober 2026 om 03:00 Nederlandse tijd. In San Francisco is het dan vrijdag 19:00.</p>
<p><strong>Speelt Luka Dončić mee?</strong><br>Ja, naar verwachting wel. Hij rustte woensdag met rugklachten, maar staat niet op de officiële NBA-blessurelijst voor deze wedstrijd. Bij Golden State spelen Jimmy Butler, Kristaps Porziņģis en Moses Moody niet.</p>
<p><strong>Wie is favoriet: Warriors of Lakers?</strong><br>De Lakers, met een quotering van 1,74 bij TOTO. Golden State staat op 2,15.</p>
<p><strong>Wat is onze voorspelling voor Warriors – Lakers?</strong><br>De Lakers winnen met 112-118. Onze wedtip is Los Angeles Lakers wint, inclusief verlenging (1,74 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

KAART = {"home": "Warriors", "away": "Lakers", "home_abbr": "gs", "away_abbr": "lal", "home_pos": "37-45 · nr. 10 West 2025/26", "away_pos": "53-29 · nr. 4 West 2025/26", "hs": 112, "as": 118, "datum": "Za 31 okt", "tijd": "03:00", "odd_home": "2,15", "odd_away": "1,74"}
WEDTIPS = {"wedtip-1-2": "Los Angeles Lakers wint (incl. verlenging)", "quotering-wedtip-1": "1.74",
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
    toegestaan = {"/nieuws/76ers-knicks-voorspelling-wedtips-nba-2026",
                  "/nieuws/mavericks-rockets-voorspelling-wedtips-nba-2026",
                  "/nieuws/suns-nuggets-voorspelling-wedtips-nba-2026",
                  "/nieuws/nba-voorspellingen-vannacht-29-oktober-2026",
                  "/nieuws/pacers-76ers-voorspelling-wedtips-nba-2026", "/nieuws/bucks-rockets-voorspelling-wedtips-nba-2026",
                  "/nieuws/mavericks-thunder-voorspelling-wedtips-nba-2026",
                  "/nieuws/clippers-lakers-voorspelling-wedtips-nba-2026",
                  "/nieuws/lakers-warriors-voorspelling-wedtips-nba-2026", "/nieuws/thunder-nuggets-voorspelling-wedtips-nba-2026",
                  "/nieuws/knicks-pistons-voorspelling-wedtips-nba-2026", "/nieuws/76ers-pistons-voorspelling-wedtips-nba-2026",
                  "/nieuws/heat-mavericks-voorspelling-wedtips-nba-2026", "/nieuws/rockets-hawks-voorspelling-wedtips-nba-2026",
                  "/nieuws/suns-warriors-voorspelling-wedtips-nba-2026",
                  "/nieuws/nuggets-warriors-voorspelling-wedtips-nba-2026",
                  "/nieuws/welke-nederlanders-spelen-in-de-nba",
                  "/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders",
                  "/nieuws/wat-is-handicap-wedden-de-complete-gids",
                  "/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners",
                  "/wedden-op-nba-voorspellingen-en-wedtips---basketbal", "/bookmakers/toto", "/bookmakers/bet365",
                  "/live-kijken", BET365}
    assert set(hrefs) <= toegestaan, set(hrefs) - toegestaan
    assert SLUG not in "".join(hrefs), "niet naar zichzelf linken"
    for s in ("76ers-knicks", "mavericks-rockets", "suns-nuggets"):
        assert f"/nieuws/{s}-voorspelling-wedtips-nba-2026" in hrefs, f"link naar {s} ontbreekt"
    assert "/nieuws/lakers-warriors-voorspelling-wedtips-nba-2026" in hrefs, "vorige ontmoeting"
    assert not any("nba-voorspellingen-vannacht" in h for h in hrefs), "vannacht geen algemeen artikel"
    assert "<table" not in html.replace(f"<table {T}>", ""), "tabellen alleen via tabel()"
    verboden = ["BetCity", "ESPN-API", "ESPN.com", "Associated Press", "DraftKings", "Rotowire", "Betfans", "Shams",
                "Klutch", "Charania", "NBA.com", "Field Level", "Yahoo", "NBC Sports"]
    assert not any(v.lower() in html.lower() for v in verboden), "geen bronnen/concurrenten"
    assert "kampioen" not in html.lower() and "titelhouder" not in html.lower(), "geen ongecontroleerde kwalificaties"
    # SEO: focuskeyword
    fk = "Warriors – Lakers voorspelling"
    assert fk in TITEL and fk in SAMENVATTING and len(SAMENVATTING) <= 160, len(SAMENVATTING)
    assert re.sub(r"<[^>]+>", "", content).startswith(fk), "focuskeyword in de eerste zin"
    assert any("Warriors – Lakers" in h for h in re.findall(r"<h3>(.*?)</h3>", html))
    assert "31 oktober, 03:00" in TITEL
    # Wedtip en consistentie
    assert set(WEDTIPS) == {"wedtip-1-2", "quotering-wedtip-1", "bookmaker-wedtips"}
    assert WEDTIPS["bookmaker-wedtips"] == "669ab9f5aceb8b717cea24c3"
    assert WEDTIPS["wedtip-1-2"] == "Los Angeles Lakers wint (incl. verlenging)"
    q = float(WEDTIPS["quotering-wedtip-1"])
    toto_odds = {2.15, 1.74, 2.20, 1.73, 1.95, 1.91, 1.71, 1.98, 1.83, 1.93, 1.87}
    assert q in toto_odds and q == 1.74
    assert KAART["as"] > KAART["hs"], "voorspelde score moet de tip Lakers wint laten winnen"
    assert f"{KAART['hs']}-{KAART['as']}" in content and f"{KAART['hs']}-{KAART['as']}" in content3
    assert KAART["odd_home"] == "2,15" and KAART["odd_away"] == "1,74" and KAART["tijd"] == "03:00"
    assert KAART["home_abbr"] == "gs" and KAART["away_abbr"] == "lal" and KAART["datum"] == "Za 31 okt"
    assert KAART["home"] == "Warriors" and KAART["away"] == "Lakers"
    assert "1,74" in content and "1,74" in content3 and "incl" in WEDTIPS["wedtip-1-2"]
    assert "inclusief verlenging" in content and "inclusief verlenging" in content3
    assert "vrijdag rond 13:45 uur" in html, "tijdstip odds"
    assert html.count("👉 Klik hier: maak je Bet365-account aan en wed live mee op") == 1
    assert len(re.findall(r"<p><strong>[123]\. ", content3)) == 3, "onderbouwing in 3 punten"
    assert "Waarom niet een andere markt?" in content3
    assert len(re.findall(r"<p><strong>[^<]*\?</strong><br>", content3)) == 4, "4 FAQ-vragen"
    assert SLUG == "warriors-lakers-voorspelling-wedtips-nba-2026" and DATUM == "2026-10-31T02:00:00.000Z"
    tekst = re.sub(r"<[^>]+>", " ", html)
    woorden = len(tekst.split())
    assert 1400 <= woorden <= 1850, woorden
    print(len(TITEL), "tekens titel |", len(SAMENVATTING), "tekens samenvatting |", woorden, "woorden")
    print("Alle asserts geslaagd (dry run, niets gepubliceerd).")
