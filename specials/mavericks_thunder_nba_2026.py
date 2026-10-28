# -*- coding: utf-8 -*-
"""Los artikel: Mavericks – Thunder voorspelling, NBA 29 oktober 2026 (02:30 NL, wintertijd), American Airlines Center Dallas.
Feiten nagelopen op 28-10-2026 rond 11:00 NL (ESPN-API: summary 401909891, boxscores 401909090, 401909094, 401909865,
401909873, 401909840, 401909844, 401909858 en 401909871, teamschema's 2025/26 (regulier en play-offs) en 2026/27,
standen 2025/26 en 2026/27, rosters en coaches, spelersgemiddelden 2025/26 en 2026/27; onderlinge duels 2025/26
(401809974, 401810204, 401810731); officiële NBA-blessurelijst 28-10 05:45 AM ET; berichtgeving over de operaties van
Jalen Williams en Cason Wallace (26-10), Caruso (enkel, 26-10) en de aanstelling van Dusty May / draft Morez Johnson Jr.).
- Thunder 2026/27: 116-104 in San Antonio, 96-84 Denver, 108-101 Clippers, 125-114 Phoenix: marges 12, 12, 7, 11.
  Punten tegen 100,8 per duel = minste van alle 30 ploegen. Tegen PHX zonder Holmgren, J. Williams en Wallace; Caruso
  viel in het tweede kwart uit. Mitchell 30 punten (10 uit 16). Tegenstanders verloren 14, 22, 26 en 13 keer de bal.
- Mavericks 2026/27: 110-128 in Houston, 121-105 in Indiana (Flagg na rust uit), 106-122 thuis tegen SA (zonder Flagg
  en Irving), 113-109 in Miami (Flagg 29 ptn en 11 ast). Balverliezen 21, 15, 21, 17 (18,5 per duel).
- Onderling 2025/26: 94-101 en 87-100 in Dallas, 111-132 in OKC (3-0 OKC). Flagg 2 (1 uit 9) en 16, miste maart.
  SGA 23, 33, 30. Irving speelde in 2025/26 niet.
- Beide ploegen speelden maandag (US) en hadden dinsdag rust.
- Twijfel/weggelaten: titels (OKC won 2025, niet 2026), 'Rookie of the Year' Flagg, details van de ruil Risacher/Dort/
  Aldama, terugkeerdatum Holmgren, of Mitchell speelt, of Topić/Sorber/Oweh iets veranderen.
- Odds: alleen TOTO, uit specials/nba_feiten_2026_10_29.md (wo ±10:50 NL). Winnaar, handicap en totaal incl. verlenging.
- Eén wedtip (vast, eigenaar): Thunder -4,5 @1,69, onze kans 61% (markt 59,2%, zonder marge ±54%).
  python3 specials/mavericks_thunder_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "Mavericks – Thunder voorspelling: wedtip en odds voor de gehavende, ongeslagen Thunder (29 oktober, 02:30)"
SLUG = "mavericks-thunder-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("Mavericks – Thunder voorspelling: de ongeslagen Thunder mist Holmgren en Jalen Williams tegen Cooper Flagg. "
                "Onze wedtip, TOTO-odds en blessures.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet-experts.nl/go/bet365"
DATUM = "2026-10-29T01:30:00.000Z"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>Onze Mavericks – Thunder voorspelling voor de nacht van woensdag op donderdag (02:30 Nederlandse tijd) draait om één vraag: hoe lang houdt Oklahoma City het vol met een halve selectie? De Thunder won alle vier de wedstrijden met minstens zeven punten verschil en kreeg de minste punten tegen van de NBA, maar mist Chet Holmgren, Jalen Williams, Cason Wallace en Alex Caruso; Ajay Mitchell is twijfelachtig. Tegenover hen staan Cooper Flagg (25 punten per duel) en Kyrie Irving. Onze voorspelling: Mavericks – Thunder 107-116. Onze wedtip: Oklahoma City Thunder -4,5 punten (inclusief verlenging) tegen een quotering van 1,69 bij TOTO.</strong></p>
<p>Hieronder lees je over vorm, blessures, de odds van <a href="/bookmakers/toto">TOTO</a> en onze onderbouwing.</p>
<h3><strong>Mavericks – Thunder: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "Dallas Mavericks – Oklahoma City Thunder"),
    ("Datum", "Donderdag 29 oktober 2026 (nacht van woensdag op donderdag)"),
    ("Aanvang", "02:30 Nederlandse tijd (woensdag 20:30 in Dallas)"),
    ("Arena", "American Airlines Center, Dallas"),
    ("Competitie", "NBA, reguliere competitie 2026/27"),
    ("Stand 2026/27", "Mavericks 2-2, Thunder 4-0"),
    ("Onderlinge duels 2025/26", "3-0 voor de Thunder"),
    ("Rust", "Beide ploegen speelden maandag (Amerikaanse tijd) en hadden dinsdag een rustdag"),
])}
<p>Nederland staat al op wintertijd, de Verenigde Staten pas vanaf 1 november: het tijdsverschil met Dallas is deze week zes uur.</p>
<h3><strong>Het seizoen tot nu toe: de Thunder wint, maar verliest spelers</strong></h3>
<p><strong>Oklahoma City Thunder: vier zeges, een week vol tegenslag</strong></p>
<p>De Thunder won met 116-104 in San Antonio en thuis van Denver (96-84), de Clippers (108-101) en Phoenix (125-114): marges van 12, 12, 7 en 11 punten. Met 100,8 punten tegen per wedstrijd heeft Oklahoma City de zuinigste verdediging van de competitie. De tegenstanders verloren bijna 19 keer per wedstrijd de bal.</p>
<p>De zege op de Clippers kostte wel veel. Jalen Williams brak in de slotminuut zijn linkerkuitbeen en ontwrichtte zijn enkel. Cason Wallace scheurde in het eerste kwart het labrum in zijn linkerschouder. Beiden worden geopereerd en zijn maanden uit de roulatie. Een dag later ontbrak ook Holmgren (peesontsteking in de rechterknie) en verstuikte Caruso vlak voor rust zijn rechterenkel. Toch won de Thunder ruim van Phoenix. Mitchell, de vervanger van Williams in de basis, scoorde 30 punten (10 uit 16), Shai Gilgeous-Alexander 26.</p>
<p><strong>Dallas Mavericks: twee zeges, twee keer kansloos</strong></p>
<p>Dallas verloor met 110-128 in Houston en won met 121-105 in Indiana, waar Flagg voor rust uitviel met een pijnlijke schouder. Zonder Flagg en Irving ging de thuisopener tegen San Antonio met 106-122 verloren. Maandag won Dallas met 113-109 in Miami: Flagg had 29 punten en 11 assists en blokte in de slotfase een schot waarmee Miami op voorsprong had kunnen komen. Het zwakke punt van de ploeg van coach Dusty May is de bal: Dallas verloor in vier wedstrijden 74 keer balbezit, 18,5 keer per duel.</p>
<h3><strong>Vorig seizoen en de onderlinge duels</strong></h3>
<p>Oklahoma City had in 2025/26 met 64-18 het beste record van de NBA; Gilgeous-Alexander werd voor de tweede keer op rij MVP. In de West-finale was San Antonio te sterk. Dallas speelde het hele seizoen zonder Irving (gescheurde kruisband), deed in februari Anthony Davis van de hand en werd twaalfde in het Westen.</p>
{tabel(["2025/26", "Dallas Mavericks", "Oklahoma City Thunder"], [
    ("Eindstand", "26-56 (nr. 12 West)", "64-18 (nr. 1 West)"),
    ("Thuis / uit", "16-25 / 10-30 (plus 1 duel in Mexico-Stad)", "34-7 / 30-10 (plus 1 duel op neutraal terrein)"),
    ("Punten voor / tegen", "114,1 / 119,6", "119,0 / 107,9"),
    ("Na het seizoen", "Play-offs niet gehaald", "West-finale verloren van San Antonio (3-4)"),
])}
<p>De Thunder won alle drie de onderlinge duels: 101-94 en 100-87 in Dallas, 132-111 in Oklahoma City. Dallas kwam nooit boven de 111 punten. Gilgeous-Alexander scoorde 23, 33 en 30 punten. Flagg bleef in oktober steken op 2 punten (1 uit 9), maakte er in december 16 en ontbrak in maart. Irving speelde geen van de drie duels.</p>"""

content2 = f"""<h3><strong>Zo zijn beide selecties veranderd</strong></h3>
<p><strong>Dallas Mavericks: nieuwe coach, Irving terug</strong></p>
<p>Dusty May volgde deze zomer Jason Kidd op en koos in de draft meteen zijn speler van Michigan, Morez Johnson Jr. (nummer negen). Via ruilen kwamen onder meer Zaccharie Risacher en Santi Aldama. De belangrijkste ‘aanwinst’ is Irving, die zijn eerste officiële wedstrijden sinds maart 2025 speelt.</p>
<p><strong>Oklahoma City Thunder: de diepte wordt op de proef gesteld</strong></p>
<p>Lu Dort vertrok naar Atlanta, Isaiah Joe en Aaron Wiggins verdwenen ook. Coach Mark Daigneault leunt nu op Mitchell, Jared McCain, Kenrich Williams en jonge invallers als Aday Mara en Bennett Stirtz.</p>
<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("Kyrie Irving", "Dallas", "Twijfelachtig (linkerknie, belastingsmanagement)"),
    ("Naji Marshall, Caleb Martin", "Dallas", "Twijfelachtig (ziek; rechterduim)"),
    ("Santi Aldama, Tarik Biberović", "Dallas", "Zeer twijfelachtig (knie; hiel)"),
    ("Dereck Lively II, Sergio de Larrea", "Dallas", "Spelen niet (voetoperatie; rechterknie)"),
    ("Ajay Mitchell", "Oklahoma City", "Twijfelachtig (verstuikte rechterenkel)"),
    ("Chet Holmgren", "Oklahoma City", "Speelt niet (peesontsteking rechterknie)"),
    ("Alex Caruso", "Oklahoma City", "Speelt niet (verstuikte rechterenkel)"),
    ("Jalen Williams", "Oklahoma City", "Speelt niet (gebroken linkerenkel, operatie)"),
    ("Cason Wallace", "Oklahoma City", "Speelt niet (gescheurd labrum linkerschouder, operatie)"),
    ("Nikola Topić, Thomas Sorber", "Oklahoma City", "Spelen niet (herstel na operaties)"),
])}
<p><em>Stand van de officiële NBA-blessurelijst op woensdag 28 oktober, 10:45 Nederlandse tijd. Controleer vlak voor het begin of Irving en Mitchell spelen.</em></p>
<p><strong>Verwachte basisvijf Mavericks:</strong> Kyrie Irving, Max Christie, Cooper Flagg, P.J. Washington, Daniel Gafford. De vijf van elke wedstrijd waarin Flagg en Irving fit waren. Risacher, Johnson Jr. en Marcus Sasser zijn de belangrijkste wissels.</p>
<p><strong>Verwachte basisvijf Thunder:</strong> Shai Gilgeous-Alexander, Jared McCain, Ajay Mitchell, Kenrich Williams, Isaiah Hartenstein, de vijf van maandag. Valt Mitchell af, dan wordt de rotatie nog smaller; Jaylin Williams, Mara, Stirtz en Josh Dix speelden maandag al minstens twintig minuten.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "2026/27 tot nu toe"], [
    ("Shai Gilgeous-Alexander (OKC)", "31,1", "4,3", "6,6", "27,3 ptn, 47,8 procent uit het veld"),
    ("Ajay Mitchell (OKC)", "13,6", "3,3", "3,6", "16,0 ptn, 30 tegen Phoenix"),
    ("Isaiah Hartenstein (OKC)", "9,2", "9,4", "3,5", "9,3 ptn, 8,5 reb"),
    ("Cooper Flagg (DAL)", "21,0", "6,7", "4,5", "25,0 ptn, 6,3 ast"),
    ("Kyrie Irving (DAL)", "24,7*", "4,8*", "4,6*", "19,0 ptn in drie duels"),
    ("P.J. Washington (DAL)", "14,2", "7,0", "1,8", "15,5 ptn, 7,5 reb"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26. * Irving speelde in 2025/26 niet; bij hem staan de cijfers van 2024/25.</em></p>
<p><strong>Cooper Flagg</strong> (19) scoort meer dan vorig seizoen, geeft meer assists en schiet 56,5 procent uit het veld, maar de Thunder hield hem vorig seizoen goed in toom. <strong>Shai Gilgeous-Alexander</strong> moet nu nog meer zelf doen en kwam tegen Dallas vorig seizoen gemiddeld tot bijna 29 punten. <strong>Ajay Mitchell</strong> is in vorm, maar staat met een enkelblessure op de lijst.</p>
<h3><strong>Odds Mavericks – Thunder bij TOTO</strong></h3>
<p>TOTO ziet Oklahoma City als duidelijke favoriet, ondanks alle afwezigen: een quotering van 1,48 staat voor ongeveer 68 procent winkans. De handicap ligt rond de 5,5 punten in het voordeel van de Thunder, het verwachte puntentotaal rond de 229 punten.</p>
{tabel(["Markt (TOTO)", "Mavericks", "Thunder"], [
    ("Winnaar (incl. verlenging)", "2,75", "1,48"),
    ("1X2 (reguliere speeltijd, gelijk 19,00)", "2,90", "1,44"),
    ("Handicap +4,5 / -4,5 (incl. verlenging)", "2,00", "1,69"),
    ("Handicap +5,5 / -5,5 (incl. verlenging)", "1,95", "1,87"),
    ("Handicap +6,5 / -6,5 (incl. verlenging)", "1,73", "1,93"),
])}
<p>Op het totaal (inclusief verlenging) biedt TOTO 228,5 punten (Over 1,78 / Under 1,87), 229,5 (Over 1,95 / Under 1,87) en 230,5 (Over 1,95 / Under 1,73). Odds gelezen op woensdag rond 10:50 uur; vergelijk ze vlak voor de start nog even, zeker zodra bekend is of Irving en Mitchell spelen.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op Mavericks – Thunder</strong></a></p>"""

content3 = f"""<h3><strong>Mavericks – Thunder voorspelling: de Thunder wint ook met een smalle selectie</strong></h3>
<p>Zonder Holmgren, Williams, Wallace en Caruso mist Oklahoma City vier van zijn beste verdedigers. Toch verwachten we dat het systeem van Daigneault overeind blijft: maandag stond de Thunder met drie basisspelers minder bij rust met 67-53 voor en liep het verschil op tot 17 punten. Gilgeous-Alexander blijft de beste speler op het veld, en Dallas verliest zelf al vaak de bal.</p>
<p>Dallas speelt thuis en heeft met Flagg en Irving twee spelers die een wedstrijd kunnen kantelen. We verwachten daarom geen ruime zege zoals in december, maar wel een duidelijke. Onze voorspelling: <strong>Dallas Mavericks – Oklahoma City Thunder 107-116</strong>.</p>
<h3><strong>Onze wedtip: Thunder -4,5 (1,69)</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Onze kans"], [
    ("Oklahoma City Thunder -4,5 punten (incl. verlenging)", "1,69", "TOTO", "Ongeveer 61 procent"),
])}
<p><strong>Waarom deze tip?</strong> De tip is goed als Oklahoma City met minstens vijf punten verschil wint, een eventuele verlenging meegeteld. Een odd van 1,69 staat voor een kans van 59 procent; zonder de marge van de bookmaker is dat ongeveer 54 procent. Wij schatten de kans op ongeveer 61 procent. De onderbouwing:</p>
<p><strong>1. Elke zege was ruim genoeg.</strong> De Thunder won alle vier de wedstrijden met minstens zeven punten verschil, ook maandag zonder drie basisspelers (125-114). Met 100,8 punten tegen per duel staat er nog altijd de beste verdediging van de NBA.</p>
<p><strong>2. Dallas verliest de bal te vaak.</strong> De Mavericks verloren dit seizoen 18,5 keer per wedstrijd de bal, de tegenstanders van de Thunder bijna 19 keer. Tegen Houston kostte dat Dallas al een ruime nederlaag (21 balverliezen) en thuis tegen San Antonio ook (21).</p>
<p><strong>3. Het onderlinge beeld.</strong> Vorig seizoen won Oklahoma City alle drie de duels, met 7, 13 en 21 punten verschil, en scoorde Dallas gemiddeld maar 97 punten. Flagg maakte in die duels samen 18 punten. Irving was er toen niet bij, maar staat nu als twijfelachtig op de lijst.</p>
<p><strong>Waarom niet een andere markt?</strong> Een zege van de Thunder (1,48) vraagt om 68 procent kans; wij komen uit op ongeveer 70 procent, een te klein verschil voor een lage odd. Thunder -5,5 (1,87) en -6,5 (1,93) leveren meer op, maar met zo'n smalle rotatie willen we de extra ruimte van de -4,5. Onze voorspelde marge van negen punten geeft daar een buffer van vier punten. Het puntentotaal laten we liggen: met zoveel afwezigen bij de Thunder is lastig te voorspellen hoe de verdediging standhoudt.</p>
<p><strong>Het risico.</strong> Haakt Mitchell ook af, dan rust er nog meer op Gilgeous-Alexander. Flagg is in vorm, Irving kan een wedstrijd openbreken, en tegen de Clippers was het verschil maar zeven punten. Een verlenging telt mee. Meer uitleg vind je in onze gidsen over <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap wedden</a> en de <a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">money line</a>.</p>
<h3><strong>Mavericks – Thunder live kijken in Nederland</strong></h3>
<p>Bij <a href="/bookmakers/bet365">Bet365</a> kun je NBA-wedstrijden live volgen via de livestream. Je hebt daarvoor een account met een storting nodig. ESPN zendt in Nederland een deel van de NBA-wedstrijden uit; in de programmagids zie je of deze erbij zit. Met <strong>NBA League Pass</strong>, de betaalde dienst van de competitie, kun je alle wedstrijden volgen. Meer opties vind je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk Mavericks – Thunder live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Lees ook onze voorspellingen voor <a href="/nieuws/pacers-76ers-voorspelling-wedtips-nba-2026">Pacers – 76ers</a>, <a href="/nieuws/bucks-rockets-voorspelling-wedtips-nba-2026">Bucks – Rockets</a> en <a href="/nieuws/clippers-lakers-voorspelling-wedtips-nba-2026">Clippers – Lakers</a>, en alle tips van deze nacht in de <a href="/nieuws/nba-voorspellingen-vannacht-29-oktober-2026">NBA-voorspellingen van 29 oktober</a>. Eerder dit seizoen schreven we over <a href="/nieuws/thunder-suns-voorspelling-wedtips-nba-2026">Thunder – Suns</a> en <a href="/nieuws/heat-mavericks-voorspelling-wedtips-nba-2026">Heat – Mavericks</a>. Benieuwd <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">welke Nederlanders in de NBA spelen</a>? Nieuw met basketbal? Lees <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels in de NBA</a>. Alle tips staan op <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Mavericks – Thunder?</strong><br>Donderdag 29 oktober 2026 om 02:30 Nederlandse tijd, in de nacht van woensdag op donderdag. In Dallas is het dan woensdag 20:30.</p>
<p><strong>Speelt Cooper Flagg mee?</strong><br>Ja, Flagg staat niet op de blessurelijst. Hij miste eerder de thuisopener met een verstuikte schouder, maar maakte maandag in Miami 29 punten. Achter Irving staat wel een vraagteken (linkerknie).</p>
<p><strong>Wie is favoriet: Mavericks of Thunder?</strong><br>Oklahoma City, met een quotering van 1,48 bij TOTO. De Mavericks staan op 2,75.</p>
<p><strong>Wat is onze voorspelling voor Mavericks – Thunder?</strong><br>De Thunder wint met 107-116. Onze wedtip is Oklahoma City Thunder -4,5 punten, inclusief verlenging (1,69 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

KAART = {"home": "Mavericks", "away": "Thunder", "home_abbr": "dal", "away_abbr": "okc", "home_pos": "26-56 · nr. 12 West 2025/26", "away_pos": "64-18 · nr. 1 West 2025/26", "hs": 107, "as": 116, "datum": "Do 29 okt", "tijd": "02:30", "odd_home": "2,75", "odd_away": "1,48"}
WEDTIPS = {"wedtip-1-2": "Oklahoma City Thunder -4,5 punten (incl. verlenging)", "quotering-wedtip-1": "1.69",
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
    # SEO: focuskeyword
    fk = "Mavericks – Thunder voorspelling"
    assert fk in TITEL and fk in SAMENVATTING and len(SAMENVATTING) <= 160, len(SAMENVATTING)
    eerste_zin = re.sub(r"<[^>]+>", "", content).split(":")[0]
    assert fk in eerste_zin, "focuskeyword in de eerste zin"
    assert any(fk in h for h in re.findall(r"<h3><strong>(.*?)</strong></h3>", html)), "focuskeyword in een h3"
    assert "02:30" in TITEL and "29 oktober" in TITEL
    # Links: alleen relatief uit het feitenblad, plus de Bet365-CTA
    feiten = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "nba_feiten_2026_10_29.md"), encoding="utf-8").read()
    toegestaan = set(re.findall(r"(/(?:nieuws|bookmakers)/[\w-]+|/wedden-op-nba-voorspellingen-en-wedtips---basketbal|/live-kijken)", feiten))
    slugregel = next(l for l in feiten.splitlines() if "Slugs vannacht:" in l)
    toegestaan |= {"/nieuws/" + s for s in re.findall(r"[a-z0-9-]+-(?:nba-2026|29-oktober-2026)", slugregel)}
    hrefs = re.findall(r'href="([^"]+)"', html)
    assert hrefs and all((h.startswith("/") and not h.startswith("//")) or h == BET365 for h in hrefs), "alle links relatief"
    assert all(h in toegestaan or h == BET365 for h in hrefs), [h for h in hrefs if h not in toegestaan and h != BET365]
    assert "/nieuws/nba-voorspellingen-vannacht-29-oktober-2026" in hrefs, "link naar algemeen artikel"
    vannacht = {h for h in hrefs if h.endswith("-voorspelling-wedtips-nba-2026") and h[8:] in slugregel and SLUG not in h}
    assert len(vannacht) == 3, vannacht
    assert SLUG not in "".join(hrefs), "niet naar zichzelf linken"
    assert html.count("👉 Klik hier: maak je Bet365-account aan en wed live mee op") == 1
    # Bronnen en concurrenten
    laag = (html + TITEL + SAMENVATTING).lower()
    for verboden in ("betcity", "espn-api", "espn.com", "draftkings", "rotowire", "associated press", "betfans", "injury report"):
        assert verboden not in laag, verboden
    # Wedtip en consistentie
    assert SLUG == "mavericks-thunder-voorspelling-wedtips-nba-2026" and DATUM == "2026-10-29T01:30:00.000Z"
    assert set(WEDTIPS) == {"wedtip-1-2", "quotering-wedtip-1", "bookmaker-wedtips"}, "precies één wedtip"
    assert WEDTIPS["bookmaker-wedtips"] == "669ab9f5aceb8b717cea24c3"
    assert re.fullmatch(r"\d+\.\d{2}", WEDTIPS["quotering-wedtip-1"]) and float(WEDTIPS["quotering-wedtip-1"]) >= 1.40
    regel = next(l for l in feiten.splitlines() if l.startswith("- **Mavericks – Thunder**"))
    assert "+4,5 2,00 / -4,5 1,69" in regel and "2,75 / 1,48" in regel and "2,90 / X 19,00 / 1,44" in regel, "odds uit het feitenblad"
    assert "Oklahoma City Thunder -4,5 (incl. verlenging) @1,69" in feiten, "vaste tip uit het feitenblad"
    assert KAART["hs"] + 4.5 < KAART["as"], "voorspelde score moet Thunder -4,5 laten winnen"
    assert KAART["as"] > KAART["hs"], "voorspelling: Thunder wint"
    score = f"{KAART['hs']}-{KAART['as']}"
    assert score in content and score in content3 and html.count(score) >= 3, "score in intro, voorspelling en FAQ"
    assert "1,69" in content and "1,69" in content3
    assert (KAART["home"], KAART["away"], KAART["home_abbr"], KAART["away_abbr"]) == ("Mavericks", "Thunder", "dal", "okc")
    assert (KAART["datum"], KAART["tijd"], KAART["odd_home"], KAART["odd_away"]) == ("Do 29 okt", "02:30", "2,75", "1,48")
    assert "woensdag rond 10:50 uur" in content2, "tijdstip odds"
    assert content3.count("<p><strong>1.") == 1 and "<p><strong>2." in content3 and "<p><strong>3." in content3
    assert "Waarom niet een andere markt?" in content3
    assert content3.count("<br>") == 4, "4 FAQ-vragen"
    tekst = re.sub(r"<[^>]+>", " ", html)
    print(len(TITEL), "tekens titel |", len(SAMENVATTING), "tekens samenvatting |", len(tekst.split()), "woorden")
    print("Alle asserts geslaagd (dry run, niets gepubliceerd).")
