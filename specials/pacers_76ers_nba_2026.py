# -*- coding: utf-8 -*-
"""Los artikel: Pacers – 76ers voorspelling, NBA 29 oktober 2026 (00:00 NL, wintertijd; woensdag 19:00 ET), Gainbridge Fieldhouse.
Feiten nagelopen op 28-10-2026 rond 11:00 NL (ESPN-API: summary 401909884 incl. blessures; boxscores 401909839 (Pelicans –
Pacers 120-123), 401909844 (Pacers – Mavericks 105-121), 401909862 (Nets – Pacers 109-136), 401909872 (Bucks – Pacers 110-102),
401909089, 401909093, 401909855 en 401909866 (76ers – Pistons 93-106); teamschema's 2025/26 en 2026/27; spelersgemiddelden
2025/26; onderlinge duels 2025/26 401836752, 401810464, 401810686, 401811030; officiële NBA-blessurelijst 28-10 05:45 ET;
berichtgeving over de ruil Brown – George (1-7-2026) en het contract van James (24-7-2026)).
- Blessurelijst 28-10 05:45 ET: IND Zubac OUT (linkerenkel), McConnell out (rechterhamstring), Sheppard out (meniscus),
  Furphy out (kruisband); Haliburton (linkerhamstring) en Nembhard (nek) questionable; Nesmith (hamstring) en Toppin (hand)
  probable. PHI Barlow, Fall, Hukporti, Walker out. Embiid, James en Edgecombe staan er niet op.
- Rust: Philadelphia speelde zondag 25-10 (US) voor het laatst; Indiana maandag 26-10 in Milwaukee (3e duel in 4 dagen).
- Onderling 2025/26: 4-0 PHI (115-105 en 113-104 in Philadelphia, 135-114 en 105-94 in Indianapolis); Haliburton speelde niet.
- Stand 2025/26: IND 19-63 (nr. 14 Oost, 11-30/8-33, 112,4/120,4); PHI 45-37 (nr. 7 Oost, 23-18/22-19, 115,9/116,1).
- Odds: alleen TOTO, uit specials/nba_feiten_2026_10_29.md (wo ±10:50 NL). Winnaar en handicaps incl. verlenging.
- Eén wedtip (eis eigenaar): Philadelphia 76ers -4,5 @1,87, onze kans 57% (odd 53,5%; zonder marge ±51%).
  python3 specials/pacers_76ers_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "Pacers – 76ers voorspelling: wedtip en odds voor Philadelphia tegen een gehavend Indiana (29 oktober, 00:00)"
SLUG = "pacers-76ers-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("Pacers – 76ers voorspelling: Philadelphia (3-1) treft een Indiana zonder Zubac en met vraagtekens bij "
                "Haliburton. Wedtip, TOTO-odds en blessures.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet-experts.nl/go/bet365"
DATUM = "2026-10-28T23:00:00.000Z"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>Pacers – 76ers voorspelling: in de nacht van woensdag op donderdag om 00:00 Nederlandse tijd speelt Philadelphia in Indianapolis. De 76ers staan op drie zeges en één nederlaag en hebben met Tyrese Maxey, Joel Embiid, Jaylen Brown en LeBron James een nieuw sterrenteam. Indiana (2-2) mist center Ivica Zubac, en achter Tyrese Haliburton en Andrew Nembhard staat een vraagteken. Onze voorspelling: Pacers – 76ers 111-118. Onze wedtip: Philadelphia 76ers -4,5 punten (inclusief verlenging) tegen een quotering van 1,87 bij TOTO.</strong></p>
<p>Hieronder lees je alles over vorm, blessures, de odds van <a href="/bookmakers/toto">TOTO</a> en onze onderbouwing.</p>
<h3><strong>Pacers – 76ers: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "Indiana Pacers – Philadelphia 76ers"),
    ("Datum", "Donderdag 29 oktober 2026 (woensdagavond in de VS)"),
    ("Aanvang", "00:00 Nederlandse tijd (woensdag 19:00 in Indianapolis)"),
    ("Arena", "Gainbridge Fieldhouse, Indianapolis"),
    ("Competitie", "NBA, reguliere competitie 2026/27"),
    ("Stand 2026/27", "Pacers 2-2, 76ers 3-1"),
    ("Onderlinge duels 2025/26", "4-0 voor de 76ers"),
])}
<p>Philadelphia speelde zondag voor het laatst en had maandag en dinsdag vrij. Indiana speelde maandag nog in Milwaukee en begint aan zijn derde wedstrijd in vier dagen.</p>
<h3><strong>De eerste week: wisselend Indiana, Philadelphia met één misser</strong></h3>
<p><strong>Indiana Pacers: twee keer winst, twee keer verlies</strong></p>
<p>Indiana opende met een 123-120 zege in New Orleans, met 30 punten van Pascal Siakam en 23 punten en 12 assists van Haliburton in zijn eerste officiële wedstrijd sinds zijn achillespeesblessure in de Finale van 2025. Daarna ging het thuis mis tegen Dallas (105-121) en volgde een ruime 136-109 zege in Brooklyn. Maandag verloor Indiana met 110-102 in Milwaukee. Zubac en Nembhard ontbraken toen al.</p>
<p><strong>Philadelphia 76ers: drie zeges, dan een tegenvaller</strong></p>
<p>Philadelphia won in New York met 106-100 en kwam daarna thuis tegen Cleveland terug van een achterstand van 29 punten: 114-106, met 32 punten van Maxey. Tegen Milwaukee rustte James en won de ploeg van coach Nick Nurse met 127-116. Embiid had 28 punten, 11 rebounds en 10 assists, Brown scoorde 27 punten. Een dag later, zonder Embiid (rust) en VJ Edgecombe (buikspieren), verloor Philadelphia met 93-106 van Detroit. Brown raakte maar 5 van zijn 20 schoten.</p>
<h3><strong>Vorig seizoen en de onderlinge duels</strong></h3>
<p>Indiana won vorig seizoen maar 19 wedstrijden. Haliburton miste het hele seizoen. Philadelphia werd zevende, kwam in de eerste ronde van de play-offs tegen Boston terug van een 1-3 achterstand en ging daarna met 0-4 onderuit tegen New York.</p>
{tabel(["2025/26", "Indiana Pacers", "Philadelphia 76ers"], [
    ("Eindstand", "19-63 (nr. 14 Oost)", "45-37 (nr. 7 Oost)"),
    ("Thuis / uit", "11-30 / 8-33", "23-18 / 22-19"),
    ("Punten voor / tegen", "112,4 / 120,4", "115,9 / 116,1"),
    ("Onderling", "0-4", "4-0"),
    ("Na het seizoen", "Play-offs niet gehaald", "Tweede ronde (0-4 tegen New York)"),
])}
<p>Alle vier de onderlinge duels gingen naar Philadelphia, telkens met minstens negen punten verschil: 115-105 en 113-104 in Philadelphia, 135-114 en 105-94 in Indianapolis. Embiid scoorde 39, 30 en 27 punten in de drie duels die hij speelde, Maxey drie keer 29 punten of meer. Wel speelde Indiana in alle vier zonder Haliburton, en Brown en James zaten toen nog niet bij Philadelphia.</p>"""

content2 = f"""<h3><strong>Zo kwamen Brown en LeBron in Philadelphia terecht</strong></h3>
<p><strong>Philadelphia 76ers: twee grote namen erbij</strong></p>
<p>Begin juli haalde Philadelphia Jaylen Brown uit Boston, de MVP van de Finale van 2024. Daarvoor gingen Paul George, twee keuzes in de eerste ronde van de draft en twee in de tweede ronde naar Boston. Eind juli volgde LeBron James. De 41-jarige forward tekende na acht seizoenen bij de Lakers een contract voor twee jaar en ongeveer 8 miljoen dollar. Ook Anfernee Simons, Kentavious Caldwell-Pope en Dean Wade kwamen erbij. Quentin Grimes, Kelly Oubre jr. en Andre Drummond vertrokken, Kyle Lowry stopte.</p>
<p><strong>Indiana Pacers: Haliburton terug, Zubac geblesseerd</strong></p>
<p>De belangrijkste versterking is Haliburton zelf, na een jaar zonder basketbal. Oubre kwam over van Philadelphia, Larry Nance jr. van Cleveland, en in ruil voor Kam Jones haalde Indiana uit Chicago de rechten op Braden Smith, de nummer 38 van de draft. Zubac kwam in februari van de LA Clippers. Rick Carlisle is nog altijd de coach.</p>
<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("Ivica Zubac", "Indiana", "Speelt niet (verstuikte linkerenkel)"),
    ("T.J. McConnell", "Indiana", "Speelt niet (rechterhamstring)"),
    ("Ben Sheppard, Johnny Furphy", "Indiana", "Spelen niet (knie)"),
    ("Tyrese Haliburton", "Indiana", "Twijfelachtig (linkerhamstring)"),
    ("Andrew Nembhard", "Indiana", "Twijfelachtig (nek)"),
    ("Aaron Nesmith, Obi Toppin", "Indiana", "Waarschijnlijk inzetbaar (hamstring, hand)"),
    ("Dominick Barlow, Tacko Fall", "Philadelphia", "Spelen niet (rug, bovenbeen)"),
    ("Ariel Hukporti, Jabari Walker", "Philadelphia", "Spelen niet (achillespees, knie)"),
])}
<p><em>Stand van de officiële NBA-blessurelijst op woensdag 28 oktober, 05:45 uur Amerikaanse tijd (10:45 Nederlandse tijd).</em></p>
<p>Embiid, James en Edgecombe staan niet op de lijst. Zubac speelde in Brooklyn maar zeven minuten en miste daarna de wedstrijd in Milwaukee.</p>
<p><strong>Verwachte basisvijf Pacers:</strong> Tyrese Haliburton, Andrew Nembhard, Aaron Nesmith, Pascal Siakam, Jay Huff, als Haliburton en Nembhard fit zijn. In Milwaukee begonnen Haliburton, Nesmith, Kelly Oubre jr., Siakam en Huff. Obi Toppin, Jarace Walker en Quenton Jackson zijn de belangrijkste wissels.</p>
<p><strong>Verwachte basisvijf 76ers:</strong> Tyrese Maxey, VJ Edgecombe, Jaylen Brown, LeBron James, Joel Embiid. Met die vijf begon Philadelphia de eerste twee wedstrijden. Caldwell-Pope, Simons, Wade en Adem Bona zijn de invallers.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "2026/27 tot nu toe"], [
    ("Tyrese Maxey (PHI)", "28,3", "4,1", "6,6", "28,8 ptn, 4,8 ast"),
    ("Joel Embiid (PHI)", "26,9", "7,7", "3,9", "21,7 ptn, 9,7 reb"),
    ("Jaylen Brown (PHI)", "28,7*", "6,9*", "5,1*", "20,8 ptn, 5,8 reb"),
    ("LeBron James (PHI)", "20,9*", "6,1*", "7,2*", "16,3 ptn, 7 reb, 5,7 ast"),
    ("Pascal Siakam (IND)", "24,0", "6,6", "3,8", "23,5 ptn, 7,8 reb"),
    ("Tyrese Haliburton (IND)", "18,6**", "3,5**", "9,2**", "21,8 ptn, 9,5 ast"),
    ("Andrew Nembhard (IND)", "16,9", "2,8", "7,7", "16,0 ptn, 5,7 ast"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26. * Brown bij Boston, James bij de Lakers. ** Haliburton speelde in 2025/26 niet; dit zijn zijn cijfers van 2024/25. Embiid speelde vorig seizoen 38 wedstrijden.</em></p>
<p><strong>Joel Embiid</strong> is de sleutel: zonder Zubac heeft Indiana weinig lengte om hem af te stoppen, en vorig seizoen scoorde hij gemiddeld 32 punten tegen de Pacers. <strong>Tyrese Maxey</strong> scoorde in elke wedstrijd 26 punten of meer. Bij Indiana draait alles om <strong>Pascal Siakam</strong> en, als hij speelt, <strong>Tyrese Haliburton</strong>.</p>
<h3><strong>Odds Pacers – 76ers bij TOTO</strong></h3>
<p>TOTO ziet Philadelphia als favoriet: een quotering van 1,54 staat voor ongeveer 65 procent winkans. De handicap ligt rond de 4,5 punten in het voordeel van de 76ers, het verwachte puntentotaal rond de 236,5.</p>
{tabel(["Markt (TOTO)", "Pacers", "76ers"], [
    ("Winnaar (incl. verlenging)", "2,55", "1,54"),
    ("Handicap +3,5 / -3,5 (incl. verlenging)", "2,05", "1,77"),
    ("Handicap +4,5 / -4,5 (incl. verlenging)", "1,95", "1,87"),
    ("Handicap +5,5 / -5,5 (incl. verlenging)", "1,77", "1,91"),
])}
<p>Op het totaal biedt TOTO 235,5 punten (Over 1,73 / Under 1,95), 236,5 (1,87 / 1,93) en 237,5 (Over 1,91 / Under 1,77). Odds gelezen op woensdag rond 10:50 uur; vergelijk ze vlak voor de start nog even, zeker omdat de status van Haliburton de lijn kan verschuiven.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op Pacers – 76ers</strong></a></p>"""

content3 = f"""<h3><strong>Onze voorspelling: Philadelphia wint met een kleine voorsprong</strong></h3>
<p>Philadelphia heeft meer kwaliteit, is uitgerust en heeft met Embiid een voordeel onder de ring dat Indiana zonder Zubac moeilijk kan opvangen. De nederlaag tegen Detroit kwam op de tweede avond van een back-to-back, zonder Embiid en Edgecombe.</p>
<p>Indiana is wel een andere ploeg dan vorig seizoen. Met Haliburton erbij won de ploeg al in New Orleans en Brooklyn, en scoorde het daar 123 en 136 punten. Maar het blessurelijstje groeit: Zubac en McConnell spelen niet, en Haliburton en Nembhard zijn twijfelachtig. En thuis verloor Indiana de enige wedstrijd die het speelde, met zestien punten verschil van Dallas. Onze voorspelling: <strong>Indiana Pacers – Philadelphia 76ers 111-118</strong>.</p>
<h3><strong>Onze wedtip: 76ers -4,5 (1,87)</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Onze kans"], [
    ("Philadelphia 76ers -4,5 punten (incl. verlenging)", "1,87", "TOTO", "Ongeveer 57 procent"),
])}
<p><strong>Waarom deze tip?</strong> De tip is goed als Philadelphia met vijf punten of meer wint. Een odd van 1,87 staat voor een kans van 53,5 procent; zonder de marge van de bookmaker is dat ongeveer 51 procent. Wij schatten de kans op ongeveer 57 procent. De onderbouwing:</p>
<p><strong>1. Embiid tegen een Indiana zonder Zubac.</strong> Zubac is de enige echte center van Indiana. Zonder hem staan Jay Huff en Jarace Walker tegenover Embiid, die vorig seizoen in drie duels met de Pacers 39, 30 en 27 punten maakte.</p>
<p><strong>2. Uitgerust tegen vermoeid.</strong> Philadelphia had twee rustdagen, Indiana speelt zijn derde wedstrijd in vier dagen. Met McConnell en Sheppard aan de kant is de rotatie van Carlisle dun, zeker in de backcourt.</p>
<p><strong>3. De onderlinge duels waren nooit spannend.</strong> Philadelphia won vorig seizoen alle vier de duels met negen punten of meer, gemiddeld met bijna dertien punten. Toen speelde Philadelphia nog zonder Brown en James.</p>
<p><strong>Waarom niet een andere markt?</strong> Een zege van de 76ers (1,54) betaalt weinig uit voor wat wij verwachten. -3,5 (1,77) levert minder op, -5,5 (1,91) zit te dicht op onze voorspelde marge van zeven punten. Het puntentotaal laten we liggen: onze voorspelling komt uit op 229 punten, terwijl TOTO rond de 236,5 punten verwacht.</p>
<p><strong>Het risico.</strong> Speelt Haliburton toch, en zit hij zoals in Brooklyn in vorm, dan kan Indiana lang meekomen. Philadelphia won zijn zeges met zes, acht en elf punten verschil en schoot tot nu toe matig van afstand. Let op: de handicap telt een eventuele verlenging mee. Meer uitleg vind je in onze gidsen over <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap wedden</a> en de <a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">money line</a>.</p>
<h3><strong>Pacers – 76ers live kijken in Nederland</strong></h3>
<p>Bij <a href="/bookmakers/bet365">Bet365</a> kun je NBA-wedstrijden live volgen via de livestream. Je hebt daarvoor een account met een storting nodig. ESPN zendt in Nederland een deel van de NBA-wedstrijden uit; in de programmagids zie je of deze erbij zit. Met <strong>NBA League Pass</strong>, de betaalde dienst van de competitie, kun je alle wedstrijden volgen. Meer opties vind je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk Pacers – 76ers live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Vannacht schreven we ook voorbeschouwingen van <a href="/nieuws/bucks-rockets-voorspelling-wedtips-nba-2026">Bucks – Rockets</a>, <a href="/nieuws/mavericks-thunder-voorspelling-wedtips-nba-2026">Mavericks – Thunder</a> en <a href="/nieuws/clippers-lakers-voorspelling-wedtips-nba-2026">Clippers – Lakers</a>. Alle wedstrijden van de nacht vind je in de <a href="/nieuws/nba-voorspellingen-vannacht-29-oktober-2026">NBA-voorspellingen van 29 oktober</a>. Eerder schreven we over <a href="/nieuws/76ers-pistons-voorspelling-wedtips-nba-2026">76ers – Pistons</a>. Benieuwd <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">welke Nederlanders in de NBA spelen</a>? Nieuw met basketbal? Lees <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels in de NBA</a>. Alle tips staan op <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Pacers – 76ers?</strong><br>Donderdag 29 oktober 2026 om 00:00 Nederlandse tijd. In Indianapolis is het dan woensdag 19:00.</p>
<p><strong>Speelt Tyrese Haliburton mee?</strong><br>Dat is nog niet zeker. Hij staat op de officiële NBA-blessurelijst als twijfelachtig, met klachten aan zijn linkerhamstring. Joel Embiid en LeBron James staan niet op de lijst.</p>
<p><strong>Wie is favoriet: Pacers of 76ers?</strong><br>De 76ers, met een quotering van 1,54 bij TOTO. Indiana staat op 2,55.</p>
<p><strong>Wat is onze voorspelling voor Pacers – 76ers?</strong><br>Philadelphia wint met 111-118. Onze wedtip is Philadelphia 76ers -4,5 punten, inclusief verlenging (1,87 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

KAART = {"home": "Pacers", "away": "76ers", "home_abbr": "ind", "away_abbr": "phi", "home_pos": "19-63 · nr. 14 Oost 2025/26", "away_pos": "45-37 · nr. 7 Oost 2025/26", "hs": 111, "as": 118, "datum": "Do 29 okt", "tijd": "00:00", "odd_home": "2,55", "odd_away": "1,54"}
WEDTIPS = {"wedtip-1-2": "Philadelphia 76ers -4,5 punten (incl. verlenging)", "quotering-wedtip-1": "1.87",
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
                  "/nieuws/nba-voorspellingen-vannacht-29-oktober-2026",
                  "/nieuws/bucks-rockets-voorspelling-wedtips-nba-2026",
                  "/nieuws/mavericks-thunder-voorspelling-wedtips-nba-2026",
                  "/nieuws/clippers-lakers-voorspelling-wedtips-nba-2026",
                  "/nieuws/lakers-trail-blazers-voorspelling-wedtips-nba-2026",
                  "/nieuws/lakers-warriors-voorspelling-wedtips-nba-2026", "/nieuws/thunder-suns-voorspelling-wedtips-nba-2026",
                  "/nieuws/thunder-clippers-voorspelling-wedtips-nba-2026", "/nieuws/rockets-hawks-voorspelling-wedtips-nba-2026",
                  "/nieuws/heat-mavericks-voorspelling-wedtips-nba-2026", "/nieuws/76ers-pistons-voorspelling-wedtips-nba-2026",
                  "/nieuws/knicks-pistons-voorspelling-wedtips-nba-2026", "/nieuws/spurs-kings-voorspelling-wedtips-nba-2026",
                  "/nieuws/celtics-nets-voorspelling-wedtips-nba-2026",
                  "/nieuws/welke-nederlanders-spelen-in-de-nba",
                  "/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders",
                  "/nieuws/wat-is-handicap-wedden-de-complete-gids",
                  "/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners",
                  "/wedden-op-nba-voorspellingen-en-wedtips---basketbal", "/bookmakers/toto", "/bookmakers/bet365",
                  "/live-kijken", BET365}
    assert set(hrefs) <= toegestaan, set(hrefs) - toegestaan
    assert SLUG not in "".join(hrefs), "niet naar zichzelf linken"
    for s in ("bucks-rockets", "mavericks-thunder", "clippers-lakers"):
        assert f"/nieuws/{s}-voorspelling-wedtips-nba-2026" in hrefs, f"link naar {s} ontbreekt"
    assert "/nieuws/nba-voorspellingen-vannacht-29-oktober-2026" in hrefs, "link naar algemeen artikel vannacht"
    assert "/nieuws/76ers-pistons-voorspelling-wedtips-nba-2026" in hrefs, "eerder artikel zelfde ploeg"
    assert "<table" not in html.replace(f"<table {T}>", ""), "tabellen alleen via tabel()"
    verboden = ["BetCity", "ESPN-API", "ESPN.com", "Associated Press", "DraftKings", "Rotowire", "Betfans", "Shams",
                "Klutch", "Charania"]
    assert not any(v.lower() in html.lower() for v in verboden), "geen bronnen/concurrenten"
    # SEO: focuskeyword
    fk = "Pacers – 76ers voorspelling"
    assert fk in TITEL and fk in SAMENVATTING and len(SAMENVATTING) <= 160, len(SAMENVATTING)
    assert re.sub(r"<[^>]+>", "", content).startswith(fk), "focuskeyword in de eerste zin"
    assert any("Pacers – 76ers" in h for h in re.findall(r"<h3>(.*?)</h3>", html))
    # Wedtip en consistentie
    assert set(WEDTIPS) == {"wedtip-1-2", "quotering-wedtip-1", "bookmaker-wedtips"}
    assert WEDTIPS["bookmaker-wedtips"] == "669ab9f5aceb8b717cea24c3"
    q = float(WEDTIPS["quotering-wedtip-1"])
    toto_odds = {2.55, 1.54, 2.05, 1.77, 1.95, 1.87, 1.91, 1.73, 1.93}
    assert q in toto_odds and q == 1.87
    assert KAART["as"] - KAART["hs"] > 4.5, "voorspelde score moet 76ers -4,5 laten winnen"
    assert KAART["as"] > KAART["hs"], "voorspelling: 76ers winnen"
    assert f"{KAART['hs']}-{KAART['as']}" in content and f"{KAART['hs']}-{KAART['as']}" in content3
    assert KAART["odd_home"] == "2,55" and KAART["odd_away"] == "1,54" and KAART["tijd"] == "00:00"
    assert KAART["home_abbr"] == "ind" and KAART["away_abbr"] == "phi" and KAART["datum"] == "Do 29 okt"
    assert "1,87" in content and "1,87" in content3 and "-4,5" in content and "-4,5" in content3
    assert "woensdag rond 10:50 uur" in html, "tijdstip odds"
    assert html.count("👉 Klik hier: maak je Bet365-account aan en wed live mee op") == 1
    assert len(re.findall(r"<p><strong>[123]\. ", content3)) == 3, "onderbouwing in 3 punten"
    assert "Waarom niet een andere markt?" in content3
    assert SLUG == "pacers-76ers-voorspelling-wedtips-nba-2026" and DATUM == "2026-10-28T23:00:00.000Z"
    tekst = re.sub(r"<[^>]+>", " ", html)
    woorden = len(tekst.split())
    assert 1400 <= woorden <= 1850, woorden
    print(len(TITEL), "tekens titel |", len(SAMENVATTING), "tekens samenvatting |", woorden, "woorden")
    print("Alle asserts geslaagd (dry run, niets gepubliceerd).")
