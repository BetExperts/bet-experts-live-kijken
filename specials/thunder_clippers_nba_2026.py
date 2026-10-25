# -*- coding: utf-8 -*-
"""Los artikel: Thunder – Clippers voorspelling, NBA 26 oktober 2026 (00:00 NL, wintertijd), Paycom Center.
Feiten nagelopen op 25-10-2026 (ESPN-API: summary 401909865, boxscores 401909090, 401909094, 401909842 en 401909851,
teamschema's 2025/26 en 2026/27 (OKC speelt 26-10 US-tijd thuis tegen PHX = back-to-back; LAC speelde 21, 23 en 25 okt),
onderlinge duels 2025/26 (401810025, 401810224, 401811018: 3-0 OKC met 19, 21 en 18), standen 2025/26 en 2026/27,
play-offs 2026 (OKC 3-4 tegen SAS in de West-finale; NYK kampioen, 4-1 tegen SAS), awards 2025/26 (MVP SGA),
selecties en spelersgemiddelden; officiële NBA-blessurelijst 25-10 04:30 AM ET).
- Thunder 2026/27: 116-104 in San Antonio, 96-84 tegen Denver. Clippers: 121-96 tegen Sacramento, 117-125 bij de Lakers.
- OKC 2025/26 thuis (zonder neutraal duel) tegen ploegen met max. 45 zeges: 14 van de 25 met 15+ punten gewonnen.
- Odds: alleen TOTO, uit specials/nba_feiten_2026_10_26.md (zo ±09:45 NL). 'Winnaar' = incl. verlenging. Eén wedtip.
  python3 specials/thunder_clippers_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "Thunder – Clippers voorspelling: wedtip en odds voor het duel in Oklahoma City (26 oktober, 00:00)"
SLUG = "thunder-clippers-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("Oklahoma City (2-0) ontvangt een Clippers zonder Beal, Ingram en Strus. "
                "Voorspelling, onze wedtip, TOTO-odds en blessures.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet-experts.nl/go/bet365"
DATUM = "2026-10-25T23:00:00.000Z"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>In de nacht van zondag op maandag om 00:00 Nederlandse tijd ontvangt Oklahoma City Thunder de LA Clippers. De Thunder won zijn eerste twee wedstrijden en liet daarin gemiddeld maar 94 punten toe. De Clippers missen Bradley Beal, Brandon Ingram en Max Strus en spelen hun derde wedstrijd in vijf dagen. Onze voorspelling: Thunder – Clippers 120-102. Onze wedtip: Oklahoma City wint met minstens vijftien punten verschil (Thunder -14,5, odd 1,83 bij TOTO).</strong></p>
<p>Op de winnaar valt met een quotering van 1,09 weinig te verdienen, dus kijken we naar het verschil. Hieronder lees je waarom.</p>
<h3><strong>Thunder – Clippers: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "Oklahoma City Thunder – LA Clippers"),
    ("Datum", "Maandag 26 oktober 2026 (nacht van zondag op maandag)"),
    ("Aanvang", "00:00 Nederlandse tijd, wintertijd (zondag 18:00 in Oklahoma City)"),
    ("Arena", "Paycom Center, Oklahoma City"),
    ("Competitie", "NBA, reguliere competitie 2026/27"),
    ("Stand 2026/27", "Thunder 2-0, Clippers 1-1"),
    ("Onderlinge duels 2025/26", "3-0 voor de Thunder"),
    ("Bijzonder", "Derde wedstrijd in vijf dagen voor de Clippers; de Thunder speelt maandag (Amerikaanse tijd) alweer"),
])}
<h3><strong>Het seizoen tot nu toe: de Thunder verdedigt, de Clippers verliezen de bal</strong></h3>
<p>Oklahoma City begon met een 116-104 zege in San Antonio, bij de ploeg die de Thunder in mei uit de play-offs had gehaald. De grootste voorsprong was 26 punten; Shai Gilgeous-Alexander maakte 32 punten, invaller Jared McCain 20. Twee dagen later won de Thunder met 96-84 van Denver. Het schot zat niet mee (11 van de 43 driepunters raak), maar Denver schoot 38 procent uit het veld en verloor 22 keer de bal. Jalen Williams scoorde 21 punten, Chet Holmgren pakte 17 rebounds en blokte 4 schoten.</p>
<p>De Clippers wonnen hun opener met 121-96 van Sacramento, met 30 punten van Darius Garland. Vrijdag verloren ze met 117-125 bij de Lakers. Bij rust stond het nog 64-64, maar na rust liep het mis. De Clippers verloren 26 keer de bal, waar de Lakers 33 punten uit haalden. Garland scoorde 26 punten, maar had ook 9 van die balverliezen op zijn naam. Coach Tyronn Lue gebruikte maar negen spelers.</p>
<h3><strong>Rust en reizen: voordeel voor de Thunder</strong></h3>
<p>Oklahoma City speelde donderdag (Amerikaanse tijd) voor het laatst en had dus twee rustdagen. De Clippers speelden woensdag en vrijdag in Los Angeles, hadden zaterdag een rustdag en moesten zo'n 1.900 kilometer naar Oklahoma City reizen. Voor de Thunder is dit wel het eerste duel van een back-to-back: maandagavond (in Nederland dinsdag om 01:00) komt Phoenix op bezoek.</p>
<h3><strong>Vorig seizoen: de Thunder de beste, de Clippers in de play-in</strong></h3>
<p>Oklahoma City had in 2025/26 met 64-18 het beste record van de NBA en kreeg op Boston na de minste punten tegen. Gilgeous-Alexander werd voor de tweede keer op rij MVP. In de West-finale was San Antonio na zeven wedstrijden te sterk (3-4); de Spurs verloren daarna de finale van New York. De Clippers werden met 42-40 negende in het Westen en verloren in de play-in van Golden State (121-126).</p>
{tabel(["2025/26", "Oklahoma City Thunder", "LA Clippers"], [
    ("Eindstand", "64-18 (nr. 1 West)", "42-40 (nr. 9 West)"),
    ("Thuis / uit", "34-7 / 30-10 (plus 1 duel op neutraal terrein)", "23-18 / 19-22"),
    ("Punten voor / tegen", "119,0 / 107,9", "113,8 / 112,6"),
    ("Onderling", "3-0", "0-3"),
    ("Na het seizoen", "West-finale verloren van San Antonio (3-4)", "Uitgeschakeld in de play-in"),
])}
<p>De drie onderlinge duels waren eenzijdig: Oklahoma City won met 126-107 en 128-110 in Los Angeles en met 122-101 thuis. Dat zijn verschillen van 19, 18 en 21 punten. Toen hadden de Clippers nog Kawhi Leonard (twee keer) of James Harden (één keer) in de ploeg. Van die ploeg is weinig over: Harden werd geruild met Cleveland voor Garland, Ivica Zubac vertrok naar Indiana en Leonard ging deze zomer naar Toronto. Uit Toronto kwamen Ingram en Gradey Dick. Ook Rui Hachimura (van de Lakers) en Strus zijn nieuw. Bij de Thunder vertrokken Lu Dort, Isaiah Joe en Aaron Wiggins, maar de kern rond Gilgeous-Alexander, Jalen Williams en Holmgren bleef bij elkaar.</p>"""

content2 = f"""<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("Bradley Beal", "LA Clippers", "Speelt niet (rechterknie)"),
    ("Brandon Ingram", "LA Clippers", "Speelt niet (herstel na operatie aan de rechterhiel)"),
    ("Max Strus", "LA Clippers", "Speelt niet (scheur in de voetzoolpees, rechtervoet)"),
    ("Yanic Konan Niederhauser", "LA Clippers", "Speelt niet (voetoperatie)"),
    ("Jordan Miller", "LA Clippers", "Speelt niet (schouderoperatie)"),
    ("Nikola Topić", "Oklahoma City", "Speelt niet (rugoperatie)"),
    ("Thomas Sorber", "Oklahoma City", "Speelt niet (knieoperatie)"),
    ("Otega Oweh", "Oklahoma City", "Speelt niet (achillespees, rest van het seizoen)"),
])}
<p><em>Stand van de officiële NBA-blessurelijst op zondag 25 oktober, 09:30 Nederlandse tijd. Er staan geen twijfelgevallen op.</em></p>
<p><strong>Verwachte basisvijf Thunder:</strong> Shai Gilgeous-Alexander, Cason Wallace, Jalen Williams, Chet Holmgren, Isaiah Hartenstein. McCain, Mitchell, Caruso en Jaylin Williams zijn de eerste wissels.</p>
<p><strong>Verwachte basisvijf Clippers:</strong> Darius Garland, Kris Dunn, Derrick Jones Jr., Rui Hachimura, Isaiah Jackson, het vijftal van de eerste twee wedstrijden. Brook Lopez, rookie Keaton Wagler, Kobe Sanders en Dick komen van de bank.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Ptn", "Reb", "Ast", "2026/27 tot nu toe"], [
    ("Shai Gilgeous-Alexander (OKC)", "31,1", "4,3", "6,6", "24,5 ptn (32 en 17)"),
    ("Chet Holmgren (OKC)", "17,1", "8,9", "1,7", "13,0 ptn, 12,0 reb, 4,0 blocks"),
    ("Jalen Williams (OKC)", "17,1", "4,6", "5,5", "16,5 ptn, 6,0 reb"),
    ("Darius Garland (LAC)", "19,9*", "2,3*", "6,4*", "28,0 ptn, 5,0 ast"),
    ("Brook Lopez (LAC)", "8,5", "3,6", "1,3", "19,5 ptn, 7,5 reb als invaller"),
    ("Rui Hachimura (LAC)", "11,5*", "3,3*", "0,8*", "13,0 ptn, 7,0 reb"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26. * Garland: alleen zijn 19 duels bij de Clippers; Hachimura: cijfers bij de Lakers.</em></p>
<p><strong>Shai Gilgeous-Alexander</strong> is nog niet op zijn best: hij raakte 19 van zijn 46 schoten (41 procent), terwijl hij vorig seizoen 55 procent haalde. Tegen de Clippers was hij vorig seizoen goed voor 30, 32 en 20 punten, en hij speelde in die duels nooit meer dan 30 minuten.</p>
<p><strong>Darius Garland</strong> scoorde 30 en 26 punten, maar zonder Beal en Ingram is er naast hem weinig scorend vermogen.</p>
<h3><strong>Odds Thunder – Clippers bij TOTO: waarom de Thunder op 1,09 staat</strong></h3>
<p>Een quotering van 1,09 staat voor een kans van ruim 90 procent. De Clippers staan op 8,20, goed voor zo'n 12 procent. Bij <a href="/bookmakers/toto">TOTO</a> liggen de odds in de handicap het dichtst bij elkaar bij 15,5 punten in het voordeel van de Thunder, en het verwachte puntentotaal rond de 221,5 punten.</p>
{tabel(["Markt (TOTO)", "Thunder", "Clippers"], [
    ("Winnaar (incl. verlenging)", "1,09", "8,20"),
    ("1X2 (reguliere speeltijd, gelijk 29,00)", "1,05", "10,00"),
    ("Handicap -14,5 / +14,5 (incl. verlenging)", "1,83", "1,98"),
    ("Handicap -15,5 / +15,5 (incl. verlenging)", "1,95", "1,87"),
    ("Handicap -16,5 / +16,5 (incl. verlenging)", "2,10", "1,77"),
])}
<p>Totaal 220,5 punten (incl. verlenging): Over 1,77, Under 1,91. Bij 221,5 punten: Over 1,93, Under 1,87. Bij 222,5 punten: Over 1,95, Under 1,73. Gelezen op zondag 25 oktober rond 09:45 uur. Odds kunnen tot het begin nog veranderen.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op Thunder – Clippers</strong></a></p>"""

content3 = f"""<h3><strong>Onze voorspelling: de Thunder wint ruim</strong></h3>
<p>We verwachten een duidelijke zege van Oklahoma City. De Thunder is uitgerust, speelt thuis en won vorig seizoen ruim van een Clippers met Leonard of Harden. De bezoekers hebben naast Garland weinig spelers die zelf een kans creëren, en ze verliezen veel ballen. Juist daar is de Thunder sterk: Denver verloor donderdag 22 keer de bal.</p>
<p>Het schot van de Thunder valt niet elke wedstrijd zo slecht als tegen Denver. Wel verwachten we dat de basisspelers met het duel van maandag in het vooruitzicht in het slotkwart rusten als de wedstrijd beslist is. Onze voorspelling: <strong>Oklahoma City Thunder – LA Clippers 120-102</strong>.</p>
<h3><strong>Onze wedtip: Thunder -14,5 (1,83)</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Onze kans"], [
    ("Oklahoma City Thunder -14,5 punten (incl. verlenging)", "1,83", "TOTO", "Ongeveer 58 procent"),
])}
<p><strong>Waarom deze tip?</strong> Oklahoma City moet met minstens vijftien punten verschil winnen. Een odd van 1,83 staat voor een kans van 55 procent; wij schatten die kans op ongeveer 58 procent. Dat verschil is bij deze markt het grootst. De onderbouwing:</p>
<p><strong>1. Het onderlinge beeld.</strong> De Thunder won alle drie de duels van vorig seizoen met minstens achttien punten verschil (19, 21 en 18), terwijl de Clippers toen nog Leonard of Harden hadden.</p>
<p><strong>2. De vorm van de ploegen.</strong> Oklahoma City kreeg in twee wedstrijden gemiddeld 94 punten tegen, tegen twee ploegen die vorig seizoen bij de beste drie van het Westen eindigden. De Clippers missen drie aanvallers en verloren in twee wedstrijden 44 keer de bal.</p>
<p><strong>3. De cijfers van vorig seizoen.</strong> Thuis tegen ploegen met hooguit 45 zeges won de Thunder 14 van de 25 wedstrijden met vijftien punten of meer verschil. Zonder Leonard, Harden en Zubac, en met Beal en Ingram geblesseerd, zijn deze Clippers op papier zwakker dan de ploeg die vorig seizoen 42 keer won.</p>
<p><strong>Waarom niet een andere markt?</strong> Een zege van de Thunder (1,09) valt af: die odd ligt ver onder onze ondergrens van 1,40. Een stunt van de Clippers (8,20, zo'n 12 procent) schatten we lager in, op hooguit 10 procent. Bij -15,5 (1,95, kans volgens de odd 51 procent) en -16,5 (2,10, 48 procent) komen wij uit op 54 en 50 procent; het voordeel is daar kleiner. De Clippers met +14,5 (1,98) geven we 42 procent kans. Het puntentotaal laten we liggen: alle drie de duels van vorig seizoen gingen over de 221,5 punten (233, 223 en 238), maar beide wedstrijden van de Thunder bleven dit seizoen onder die lijn (220 en 180). Wij komen uit op 222 punten, precies rond de lijn van TOTO.</p>
<p><strong>Het risico.</strong> Een ruime voorsprong kan in het slotkwart nog slinken als de invallers erin komen. Beide zeges van de Thunder dit seizoen waren met twaalf punten verschil, en de Clippers bleven vrijdag bij de Lakers lang in de wedstrijd. Controleer de opstellingen dus vlak voor het begin. Let ook op: de handicap telt een eventuele verlenging mee. Meer uitleg vind je in onze gids over <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap wedden</a>.</p>
<h3><strong>Thunder – Clippers live kijken in Nederland</strong></h3>
<p>Bij <a href="/bookmakers/bet365">Bet365</a> kun je NBA-wedstrijden live volgen via de livestream; je hebt daarvoor een account nodig. ESPN zendt in Nederland een deel van de NBA-wedstrijden uit; of deze erbij zit, zie je in de programmagids. Met <strong>NBA League Pass</strong>, de betaalde dienst van de competitie, kun je alle wedstrijden volgen. Meer opties vind je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk Thunder – Clippers live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Lees ook onze voorbeschouwingen van <a href="/nieuws/thunder-nuggets-voorspelling-wedtips-nba-2026">Thunder – Nuggets</a> en <a href="/nieuws/lakers-clippers-voorspelling-wedtips-nba-2026">Lakers – Clippers</a>, de <a href="/nieuws/nba-voorspellingen-vannacht-25-oktober-2026">NBA-voorspellingen van 25 oktober</a> en <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">welke Nederlanders er in de NBA spelen</a>. Nieuw met basketbal? Lees <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels in de NBA</a> of <a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">hoe een money line werkt</a>. Alle tips staan op <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Thunder – Clippers?</strong><br>Maandag 26 oktober 2026 om 00:00 Nederlandse tijd, in de nacht van zondag op maandag. In Oklahoma City is het dan zondag 18:00.</p>
<p><strong>Welke Clippers ontbreken?</strong><br>Bradley Beal, Brandon Ingram, Max Strus, Yanic Konan Niederhauser en Jordan Miller staan allemaal als afwezig op de blessurelijst. Bij de Thunder ontbreken Nikola Topić, Thomas Sorber en Otega Oweh.</p>
<p><strong>Wie is favoriet: Thunder of Clippers?</strong><br>Oklahoma City, met een quotering van 1,09 bij TOTO. De Clippers staan op 8,20.</p>
<p><strong>Wat is onze voorspelling voor Thunder – Clippers?</strong><br>De Thunder wint met 120-102. Onze wedtip is Oklahoma City -14,5 punten (1,83 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

KAART = {"home": "Thunder", "away": "Clippers", "home_abbr": "okc", "away_abbr": "lac", "home_pos": "64-18 · nr. 1 West 2025/26", "away_pos": "42-40 · nr. 9 West 2025/26", "hs": 120, "as": 102, "datum": "Ma 26 okt", "tijd": "00:00", "odd_home": "1,09", "odd_away": "8,20"}
WEDTIPS = {"wedtip-1-2": "Oklahoma City Thunder -14,5 punten (incl. verlenging)", "quotering-wedtip-1": "1.83",
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
    # Vaste waarden
    assert SLUG == "thunder-clippers-voorspelling-wedtips-nba-2026"
    assert DATUM == "2026-10-25T23:00:00.000Z"
    assert set(WEDTIPS) == {"wedtip-1-2", "quotering-wedtip-1", "bookmaker-wedtips"}, "precies één wedtip"
    assert WEDTIPS["bookmaker-wedtips"] == "669ab9f5aceb8b717cea24c3"
    assert re.fullmatch(r"\d+\.\d{2}", WEDTIPS["quotering-wedtip-1"]) and float(WEDTIPS["quotering-wedtip-1"]) >= 1.40
    # Odd van de tip staat in het feitenblad (Thunder – Clippers-regel)
    feiten = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "nba_feiten_2026_10_26.md"), encoding="utf-8").read()
    regel = next(l for l in feiten.splitlines() if l.startswith("- **Thunder – Clippers**"))
    assert "-14,5 1,83" in regel and "1,09 / 8,20" in regel
    assert KAART["odd_home"] == "1,09" and KAART["odd_away"] == "8,20"
    assert (KAART["home"], KAART["away"], KAART["home_abbr"], KAART["away_abbr"]) == ("Thunder", "Clippers", "okc", "lac")
    assert (KAART["datum"], KAART["tijd"]) == ("Ma 26 okt", "00:00")
    # Voorspelling past bij de tip (Thunder wint met 15+) en staat zo in de tekst
    assert KAART["hs"] - KAART["as"] >= 15
    score = f"{KAART['hs']}-{KAART['as']}"
    assert alles.count(score) >= 3, "score in intro, voorspelling en FAQ"
    assert WEDTIPS["quotering-wedtip-1"].replace(".", ",") in content3
    # Opmaak
    assert content.startswith("<p><strong>"), "vetgedrukte intro"
    assert "<h2" not in alles and "<h4" not in alles and "<h1" not in alles
    assert alles.count("<h3>") == alles.count("<h3><strong>"), "elke h3 met strong"
    assert not re.search(r"<(/?)(ul|ol|li)>\s+<", alles) and not re.search(r">\s+<(/?)(ul|ol|li)>", alles), "geen witruimte in lijsten"
    hrefs = re.findall(r'href="([^"]+)"', alles)
    assert hrefs and all((h.startswith("/") and not h.startswith("//")) or h == BET365 for h in hrefs), "alle links relatief"
    toegestaan = set(re.findall(r"(/(?:nieuws|bookmakers)/[\w-]+|/wedden-op-nba-voorspellingen-en-wedtips---basketbal|/live-kijken)", feiten))
    assert all(h in toegestaan or h == BET365 for h in hrefs), [h for h in hrefs if h not in toegestaan and h != BET365]
    assert content3.splitlines()[-1] == "<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"
    assert "<table" in alles and alles.count("<table") == alles.count(f"<table {T}>"), "tabellen via tabel()"
    laag = alles.lower() + TITEL.lower() + SAMENVATTING.lower()
    for verboden in ("betcity", "espn-api", "draftkings", "sportradar", "associated press", "injury report", "<h2"):
        assert verboden not in laag, verboden
    assert "Bet365" in content3 and "ESPN" in content3, "live-kijken-sectie"
    tekst = re.sub(r"<[^>]+>", " ", alles)
    print(len(TITEL), "tekens titel |", len(SAMENVATTING), "tekens samenvatting |", len(tekst.split()), "woorden")
    print("Alle asserts geslaagd.")
