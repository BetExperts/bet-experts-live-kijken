# -*- coding: utf-8 -*-
"""Los artikel: Thunder – Suns voorspelling, NBA 27 oktober 2026 (01:00 NL, wintertijd), Paycom Center Oklahoma City.
Feiten nagelopen op 26-10-2026 rond 12:40 NL (ESPN-API: summary 401909873, boxscores 401909090, 401909094, 401909865,
401909841 en 401909860, teamschema's 2025/26 (regulier, play-in en play-offs) en 2026/27, rosters en coaches,
spelersgemiddelden 2025/26 en 2026/27; onderlinge duels 2025/26 (401809817, 401809835, 401810354, 401810640, 401811051)
en play-offs 2026 (401869192, 401869368, 401869370, 401869373); officiële NBA-blessurelijst 26-10 07:30 AM ET,
Thunder toen nog 'not yet submitted').
- Thunder 2026/27: 116-104 in San Antonio, 96-84 tegen Denver, 108-101 tegen de Clippers (zondag US = back-to-back).
  Punten tegen 104, 84, 101 (gem. 96,3); totalen 220, 180, 209; zelf 106,7 per duel, 33 van 98 driepunters.
- Suns 2026/27: 83-124 in Portland, 131-122 tegen Golden State (Booker 43; GSW zonder Curry, Green, Podziemski).
- Onderling 2025/26: 123-119 en 138-89 OKC thuis, 108-105 PHX thuis, 136-109 OKC in PHX, 135-103 PHX in OKC
  (13-4, beide ploegen met reserves). Play-offs ronde 1: 4-0 OKC (119-84, 120-107, 121-109, 131-122).
  Booker tegen OKC: 21, 24, 23, 22, 16, 24 (gem. 21,7); miste 12-2 en 13-4.
- OKC 2025/26 op de tweede avond van een back-to-back: 14 duels, 7-7, 113,0 punten voor (seizoen 119,0).
- Twijfel/weggelaten: 'titelhouder' (OKC won 2025, kampioen 2026 = New York), hoe Kennard naar Phoenix kwam,
  status Koa Peat, Sorber (niet meer op de lijst), reisafstand.
- Odds: alleen TOTO, uit specials/nba_feiten_2026_10_27.md (ma ±12:45 NL). Winnaar, handicap en totaal incl. verlenging.
- Eén wedtip (eis eigenaar): Under 219,5 @1,87, onze kans 55% (markt 53,5%, zonder marge ±51%).
  python3 specials/thunder_suns_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "Thunder – Suns voorspelling: wedtip en odds voor de back-to-back van OKC (27 oktober, 01:00)"
SLUG = "thunder-suns-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("De ongeslagen Thunder speelt voor de tweede avond op rij en ontvangt Devin Booker en Phoenix. "
                "Voorspelling, onze wedtip, TOTO-odds en blessures.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet-experts.nl/go/bet365"
DATUM = "2026-10-27T00:00:00.000Z"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>In de nacht van maandag op dinsdag om 01:00 Nederlandse tijd ontvangt Oklahoma City Thunder de Phoenix Suns. De Thunder won zijn eerste drie wedstrijden en kreeg daarin gemiddeld maar 96 punten tegen, maar speelt nu de tweede avond van een back-to-back. Bij Phoenix draait alles om Devin Booker, die gemiddeld 33 punten maakt. Onze voorspelling: Thunder – Suns 113-102. Onze wedtip: minder dan 219,5 punten (inclusief verlenging) tegen een quotering van 1,87 bij TOTO.</strong></p>
<p>Hieronder lees je over vorm, blessures, de odds van <a href="/bookmakers/toto">TOTO</a> en onze onderbouwing.</p>
<h3><strong>Thunder – Suns: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "Oklahoma City Thunder – Phoenix Suns"),
    ("Datum", "Dinsdag 27 oktober 2026 (nacht van maandag op dinsdag)"),
    ("Aanvang", "01:00 Nederlandse tijd (maandag 19:00 in Oklahoma City)"),
    ("Arena", "Paycom Center, Oklahoma City"),
    ("Competitie", "NBA, reguliere competitie 2026/27"),
    ("Stand 2026/27", "Thunder 3-0, Suns 1-1"),
    ("Onderlinge duels 2025/26", "3-2 voor de Thunder, plus 4-0 in de eerste ronde van de play-offs"),
    ("Bijzonder", "Tweede wedstrijd in twee avonden voor de Thunder; de Suns hadden zondag rust"),
])}
<h3><strong>Het seizoen tot nu toe: de Thunder verdedigt, Booker scoort</strong></h3>
<p><strong>Oklahoma City Thunder: drie zeges, weinig punten tegen</strong></p>
<p>De Thunder opende met een 116-104 zege in San Antonio (Shai Gilgeous-Alexander 32 punten) en won daarna met 96-84 van Denver. Zondag won Oklahoma City met 108-101 van de Clippers. Gilgeous-Alexander scoorde 34 punten (13 uit 26), Ajay Mitchell 18. De Clippers verloren 26 keer de bal, maar de Thunder raakte zelf maar 8 van de 24 driepunters.</p>
<p>Opvallend: de verdediging staat, de aanval nog niet. Oklahoma City kreeg 104, 84 en 101 punten tegen, maar scoorde zelf gemiddeld 106,7 punten. Vorig seizoen was dat nog 119,0. Van de 98 driepunters gingen er 33 in, nog geen 34 procent. De drie wedstrijden eindigden op 220, 180 en 209 punten.</p>
<p><strong>Phoenix Suns: van 83 naar 131 punten</strong></p>
<p>Phoenix begon met een 83-124 nederlaag in Portland, met 6 raak uit 32 driepunters. Zaterdag volgde een 131-122 zege op Golden State. Booker maakte 43 punten, met 17 van zijn 25 schoten raak. Wel speelden de Warriors de tweede avond van een back-to-back, zonder Stephen Curry, Draymond Green en Brandin Podziemski. In twee wedstrijden kreeg Phoenix 124 en 122 punten tegen.</p>
<h3><strong>Vorig seizoen en de onderlinge duels</strong></h3>
<p>Oklahoma City had in 2025/26 met 64-18 het beste record van de NBA. Gilgeous-Alexander werd voor de tweede keer op rij MVP. In de play-offs schakelde de Thunder Phoenix en de Lakers uit (allebei 4-0), maar in de West-finale was San Antonio na zeven wedstrijden te sterk. Phoenix werd zevende in het Westen, verloor in de play-in van Portland (110-114) en plaatste zich daarna met 111-96 tegen Golden State.</p>
{tabel(["2025/26", "Oklahoma City Thunder", "Phoenix Suns"], [
    ("Eindstand", "64-18 (nr. 1 West)", "45-37 (nr. 7 West)"),
    ("Thuis / uit", "34-7 / 30-10 (plus 1 duel op neutraal terrein)", "25-16 / 20-21"),
    ("Punten voor / tegen", "119,0 / 107,9", "112,6 / 111,1"),
    ("Na het seizoen", "West-finale verloren van San Antonio (3-4)", "Eerste ronde verloren van Oklahoma City (0-4)"),
])}
<p>In de reguliere competitie won de Thunder thuis met 123-119 en 138-89 en in Phoenix met 136-109. Phoenix won thuis met 108-105. Het vijfde duel, op de laatste speeldag, won Phoenix met 135-103 in Oklahoma City, maar toen stonden aan beide kanten vooral reserves op het veld. In de play-offs won de Thunder vier keer: 119-84, 120-107, 121-109 en 131-122.</p>"""

content2 = f"""<h3><strong>Zo zijn beide selecties veranderd</strong></h3>
<p><strong>Oklahoma City Thunder: de kern bleef bij elkaar</strong></p>
<p>Lu Dort, Isaiah Joe en Aaron Wiggins vertrokken, maar de basis rond Gilgeous-Alexander, Jalen Williams, Chet Holmgren en Isaiah Hartenstein bleef intact. Jared McCain kwam vorig seizoen halverwege over van Philadelphia en is nu een vaste invaller. Mark Daigneault is nog altijd de coach.</p>
<p><strong>Phoenix Suns: Bridges erbij</strong></p>
<p>Phoenix haalde deze zomer Miles Bridges uit Charlotte, in ruil voor Grayson Allen en Royce O'Neale. Ook schutter Luke Kennard is nieuw; hij speelde vorig seizoen voor Atlanta en de Lakers. Jordan Ott begint aan zijn tweede seizoen als coach.</p>
<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("Jalen Williams", "Oklahoma City", "Twijfelachtig (linkerenkel)"),
    ("Cason Wallace", "Oklahoma City", "Twijfelachtig (linkerschouder), speelde zondag maar zes minuten"),
    ("Jaylin Williams", "Oklahoma City", "Twijfelachtig (rechterpols)"),
    ("Nikola Topić", "Oklahoma City", "Speelt niet (rugoperatie)"),
    ("Otega Oweh", "Oklahoma City", "Speelt niet (achillespees)"),
    ("Mark Williams", "Phoenix", "Speelt niet (operatie aan de linkerschouder)"),
    ("Oso Ighodaro", "Phoenix", "Zeer twijfelachtig (schuine buikspier)"),
    ("Drew Timme", "Phoenix", "Niet bij de ploeg (G League)"),
])}
<p><em>Stand van de officiële NBA-blessurelijst op maandag 26 oktober, 12:30 Nederlandse tijd. De Thunder had zijn lijst toen nog niet ingediend; de status van de Thunder-spelers is de laatst bekende stand. Op de tweede avond van een back-to-back kan de Thunder ook spelers rust geven, dus controleer de opstellingen vlak voor het begin.</em></p>
<p><strong>Verwachte basisvijf Thunder:</strong> Shai Gilgeous-Alexander, Cason Wallace, Jalen Williams, Chet Holmgren, Isaiah Hartenstein. Dat was de vijf van zondag. Haakt Wallace af, dan kan Mitchell in de basis komen. Alex Caruso, McCain en Mitchell zijn de eerste wissels.</p>
<p><strong>Verwachte basisvijf Suns:</strong> Devin Booker, Jalen Green, Dillon Brooks, Miles Bridges, Khaman Maluach. Dezelfde vijf als in de eerste twee wedstrijden. Collin Gillespie, Kennard en Jordan Goodwin komen van de bank.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "2026/27 tot nu toe"], [
    ("Shai Gilgeous-Alexander (OKC)", "31,1", "4,3", "6,6", "27,7 ptn, 44 procent uit het veld"),
    ("Chet Holmgren (OKC)", "17,1", "8,9", "1,7", "12,0 ptn, 9,3 reb"),
    ("Jalen Williams (OKC)", "17,1", "4,6", "5,5", "13,7 ptn"),
    ("Devin Booker (PHX)", "26,1", "3,9", "6,0", "33,0 ptn (23 en 43)"),
    ("Dillon Brooks (PHX)", "20,2", "3,6", "1,8", "12,5 ptn"),
    ("Miles Bridges (PHX)", "17,1*", "5,8*", "3,2*", "12,0 ptn, 5,5 reb"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26. * Bridges: cijfers bij Charlotte.</em></p>
<p><strong>Devin Booker</strong> is in vorm, maar tegen Oklahoma City had hij het vorig seizoen lastig. In de zes duels die hij tegen de Thunder speelde (twee in de competitie, vier in de play-offs) maakte hij 21, 24, 23, 22, 16 en 24 punten. Dat is gemiddeld 21,7, ruim vier punten onder zijn seizoensgemiddelde. <strong>Shai Gilgeous-Alexander</strong> scoorde in de vier play-offduels 25, 37, 42 en 31 punten. <strong>Dillon Brooks</strong> was in de play-offserie juist de gevaarlijkste Sun, met 30 en 33 punten in duel twee en drie.</p>
<h3><strong>Odds Thunder – Suns bij TOTO</strong></h3>
<p>TOTO ziet de Thunder als grote favoriet: een quotering van 1,24 staat voor ongeveer 81 procent winkans. De handicap ligt rond de 9,5 punten in het voordeel van Oklahoma City, het verwachte puntentotaal op 219,5.</p>
{tabel(["Markt (TOTO)", "Thunder", "Suns"], [
    ("Winnaar (incl. verlenging)", "1,24", "4,15"),
    ("1X2 (reguliere speeltijd, gelijk 19,00)", "1,22", "4,50"),
    ("Handicap -8,5 / +8,5 (incl. verlenging)", "1,69", "2,00"),
    ("Handicap -9,5 / +9,5 (incl. verlenging)", "1,87", "1,93"),
    ("Handicap -10,5 / +10,5 (incl. verlenging)", "1,93", "1,73"),
])}
<p>Op het totaal (inclusief verlenging) biedt TOTO 218,5 punten (Over 1,78 / Under 1,91), 219,5 (Over 1,93 / Under 1,87) en 220,5 (Over 1,95 / Under 1,73). Odds gelezen op maandag rond 12:45 uur; vergelijk ze vlak voor de start nog even, zeker zodra de Thunder zijn blessurelijst bekendmaakt.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op Thunder – Suns</strong></a></p>"""

content3 = f"""<h3><strong>Onze voorspelling: de Thunder wint een wedstrijd met weinig punten</strong></h3>
<p>Oklahoma City is op papier de betere ploeg en won vorig seizoen zes van de zeven duels waarin beide basisploegen speelden. Toch verwachten we geen wedstrijd zoals de 138-89 van december. De Thunder speelt voor de tweede avond op rij en zijn aanval loopt nog niet. Phoenix heeft in Booker iemand die een wedstrijd in zijn eentje open kan breken, maar daarachter scoorden Brooks, Green en Bridges dit seizoen nog maar 11 tot 12,5 punten per duel.</p>
<p>Wij verwachten dat de Thunder het tempo laag houdt en het verschil in de tweede helft maakt met zijn verdediging. Onze voorspelling: <strong>Oklahoma City Thunder – Phoenix Suns 113-102</strong>. Dat is samen 215 punten.</p>
<h3><strong>Onze wedtip: Under 219,5 punten (1,87)</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Onze kans"], [
    ("Minder dan 219,5 punten (incl. verlenging)", "1,87", "TOTO", "Ongeveer 55 procent"),
])}
<p><strong>Waarom deze tip?</strong> De tip is goed als beide ploegen samen 219 punten of minder maken, een eventuele verlenging meegeteld. Een odd van 1,87 staat voor een kans van 53,5 procent; zonder de marge van de bookmaker is dat ongeveer 51 procent. Wij schatten de kans op ongeveer 55 procent. De onderbouwing:</p>
<p><strong>1. De verdediging van de Thunder.</strong> Oklahoma City kreeg in drie wedstrijden gemiddeld 96 punten tegen, tegen San Antonio, Denver en de Clippers. Twee van de drie wedstrijden bleven onder deze lijn (180 en 209 punten), de derde eindigde met 220 punten net boven de lijn.</p>
<p><strong>2. Vermoeide benen bij de thuisploeg.</strong> De Thunder speelde zondag nog en mist mogelijk Jalen Williams en Cason Wallace. Vorig seizoen scoorde Oklahoma City op de tweede avond van een back-to-back gemiddeld 113 punten, zes minder dan normaal, en won het daar maar 7 van de 14 duels. Ook dit seizoen scoort de Thunder met 106,7 punten per duel veel minder dan vorig jaar.</p>
<p><strong>3. Booker tegen deze verdediging.</strong> De 43 punten van zaterdag kwamen tegen een gehavend Golden State. Tegen Oklahoma City kwam Booker vorig seizoen gemiddeld niet verder dan 21,7 punten, en in de play-offs scoorde Phoenix gemiddeld 105,5 punten tegen de Thunder. Houdt de Thunder hem rond de 25 punten, dan wordt het voor Phoenix lastig om ver boven de 100 te komen.</p>
<p><strong>Waarom niet een andere markt?</strong> Een zege van de Thunder (1,24) ligt onder onze ondergrens van 1,40. Onze voorspelde marge van elf punten zit te dicht op de handicaplijnen van 9,5 en 10,5 punten om daar een duidelijk voordeel te zien. Under 218,5 (1,91) geeft een punt minder ruimte; Under 220,5 (1,73) vraagt om 58 procent kans, en zo hoog schatten wij die niet in.</p>
<p><strong>Het risico.</strong> De onderlinge duels van vorig seizoen pleiten niet voor deze tip: van de zeven wedstrijden waarin beide basisploegen speelden, gingen er vijf over de 219,5 punten. Toen scoorde de Thunder wel gemiddeld 119 punten per wedstrijd. Phoenix kreeg dit seizoen bovendien 124 en 122 punten tegen, en een verlenging telt mee. Meer uitleg vind je in onze gidsen over <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap wedden</a> en de <a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">money line</a>.</p>
<h3><strong>Thunder – Suns live kijken in Nederland</strong></h3>
<p>Bij <a href="/bookmakers/bet365">Bet365</a> kun je NBA-wedstrijden live volgen via de livestream. Je hebt daarvoor een account met een storting nodig. ESPN zendt in Nederland een deel van de NBA-wedstrijden uit; in de programmagids zie je of deze erbij zit. Met <strong>NBA League Pass</strong>, de betaalde dienst van de competitie, kun je alle wedstrijden volgen. Meer opties vind je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk Thunder – Suns live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Lees ook onze voorspellingen voor <a href="/nieuws/cavaliers-timberwolves-voorspelling-wedtips-nba-2026">Cavaliers – Timberwolves</a>, <a href="/nieuws/rockets-hawks-voorspelling-wedtips-nba-2026">Rockets – Hawks</a> en <a href="/nieuws/nuggets-warriors-voorspelling-wedtips-nba-2026">Nuggets – Warriors</a>, en alle tips van deze nacht in de <a href="/nieuws/nba-voorspellingen-vannacht-27-oktober-2026">NBA-voorspellingen van 27 oktober</a>. Eerder dit seizoen schreven we over <a href="/nieuws/thunder-clippers-voorspelling-wedtips-nba-2026">Thunder – Clippers</a>. Benieuwd <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">welke Nederlanders in de NBA spelen</a>? Nieuw met basketbal? Lees <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels in de NBA</a>. Alle tips staan op <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Thunder – Suns?</strong><br>Dinsdag 27 oktober 2026 om 01:00 Nederlandse tijd, in de nacht van maandag op dinsdag. In Oklahoma City is het dan maandag 19:00.</p>
<p><strong>Speelt Devin Booker mee?</strong><br>Ja, Booker staat niet op de blessurelijst. Hij maakte dit seizoen 23 en 43 punten. Bij Phoenix ontbreken Mark Williams en waarschijnlijk Oso Ighodaro.</p>
<p><strong>Wie is favoriet: Thunder of Suns?</strong><br>Oklahoma City, met een quotering van 1,24 bij TOTO. De Suns staan op 4,15.</p>
<p><strong>Wat is onze voorspelling voor Thunder – Suns?</strong><br>De Thunder wint met 113-102. Onze wedtip is minder dan 219,5 punten, inclusief verlenging (1,87 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

KAART = {"home": "Thunder", "away": "Suns", "home_abbr": "okc", "away_abbr": "phx", "home_pos": "64-18 · nr. 1 West 2025/26", "away_pos": "45-37 · nr. 7 West 2025/26", "hs": 113, "as": 102, "datum": "Di 27 okt", "tijd": "01:00", "odd_home": "1,24", "odd_away": "4,15"}
WEDTIPS = {"wedtip-1-2": "Minder dan 219,5 punten (incl. verlenging)", "quotering-wedtip-1": "1.87",
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
    assert html.count("<h3>") == html.count("<h3><strong>"), "h3 altijd met strong"
    assert content.startswith("<p><strong>"), "vetgedrukte intro"
    assert not re.search(r"<(ul|ol|li)\b", html), "geen lijsten"
    assert content3.splitlines()[-1] == "<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>", "slotregel"
    assert html.count("<table") == html.count(f"<table {T}>"), "tabellen alleen via tabel()"
    # Links: alleen relatief uit het feitenblad, plus de Bet365-CTA
    feiten = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "nba_feiten_2026_10_27.md"), encoding="utf-8").read()
    toegestaan = set(re.findall(r"(/(?:nieuws|bookmakers)/[\w-]+|/wedden-op-nba-voorspellingen-en-wedtips---basketbal|/live-kijken)", feiten))
    slugregel = next(l for l in feiten.splitlines() if l.startswith("- Slugs vannacht:"))
    toegestaan |= {"/nieuws/" + s for s in re.findall(r"[a-z0-9-]+-(?:nba-2026|27-oktober-2026)", slugregel)}
    hrefs = re.findall(r'href="([^"]+)"', html)
    assert hrefs and all((h.startswith("/") and not h.startswith("//")) or h == BET365 for h in hrefs), "alle links relatief"
    assert all(h in toegestaan or h == BET365 for h in hrefs), [h for h in hrefs if h not in toegestaan and h != BET365]
    assert "/nieuws/nba-voorspellingen-vannacht-27-oktober-2026" in hrefs, "link naar algemeen artikel"
    vannacht = [h for h in hrefs if h.endswith("-voorspelling-wedtips-nba-2026") and h[8:] in slugregel and SLUG not in h]
    assert 2 <= len(set(vannacht)) <= 4, vannacht
    assert SLUG not in "".join(hrefs), "niet naar zichzelf linken"
    assert html.count("👉 Klik hier: maak je Bet365-account aan en wed live mee op") == 1
    # Bronnen en concurrenten
    laag = (html + TITEL + SAMENVATTING).lower()
    for verboden in ("betcity", "espn-api", "espn.com", "draftkings", "rotowire", "associated press", "betfans", "injury report"):
        assert verboden not in laag, verboden
    # Wedtip en consistentie
    assert SLUG == "thunder-suns-voorspelling-wedtips-nba-2026" and DATUM == "2026-10-27T00:00:00.000Z"
    assert set(WEDTIPS) == {"wedtip-1-2", "quotering-wedtip-1", "bookmaker-wedtips"}, "precies één wedtip"
    assert WEDTIPS["bookmaker-wedtips"] == "669ab9f5aceb8b717cea24c3"
    assert re.fullmatch(r"\d+\.\d{2}", WEDTIPS["quotering-wedtip-1"]) and float(WEDTIPS["quotering-wedtip-1"]) >= 1.40
    regel = next(l for l in feiten.splitlines() if l.startswith("- **Thunder – Suns**"))
    assert "219,5 1,93/1,87" in regel and "1,24 / 4,15" in regel, "odds uit het feitenblad"
    assert "Under 219,5 punten (incl. verlenging) @1,87" in feiten, "vaste tip uit het feitenblad"
    assert KAART["hs"] + KAART["as"] < 219.5, "voorspelde score moet Under 219,5 laten winnen"
    assert KAART["hs"] > KAART["as"], "voorspelling: Thunder wint"
    score = f"{KAART['hs']}-{KAART['as']}"
    assert score in content and score in content3 and html.count(score) >= 3, "score in intro, voorspelling en FAQ"
    assert "1,87" in content and "1,87" in content3
    assert (KAART["home"], KAART["away"], KAART["home_abbr"], KAART["away_abbr"]) == ("Thunder", "Suns", "okc", "phx")
    assert (KAART["datum"], KAART["tijd"], KAART["odd_home"], KAART["odd_away"]) == ("Di 27 okt", "01:00", "1,24", "4,15")
    assert "maandag rond 12:45 uur" in content2, "tijdstip odds"
    assert content3.count("<p><strong>1.") == 1 and "<p><strong>2." in content3 and "<p><strong>3." in content3
    assert "Waarom niet een andere markt?" in content3
    assert content3.count("<br>") == 4, "4 FAQ-vragen"
    tekst = re.sub(r"<[^>]+>", " ", html)
    print(len(TITEL), "tekens titel |", len(SAMENVATTING), "tekens samenvatting |", len(tekst.split()), "woorden")
    print("Alle asserts geslaagd (dry run, niets gepubliceerd).")
