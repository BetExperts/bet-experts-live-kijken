# -*- coding: utf-8 -*-
"""Los artikel: Thunder – Nuggets voorspelling, NBA 23 oktober 2026 (03:30 NL). Feiten nagelopen op 22-10-2026:
- Uitslagen/boxscores/schema's/selecties: NBA-scoreboard (Thunder won 20-10 116-104 in San Antonio; Denver speelt
  hier zijn eerste duel, Thunder heeft één rustdag, geen back-to-backs), officieel NBA-blessurerapport 22-10 03:15 ET.
- Records/ratings/ATS 2025/26 en onderlinge duels (3-1 OKC; play-offs 2025 4-3 OKC) nagelopen.
- Selectiewijzigingen Denver/OKC: teamberichten en grote media (sign-and-trade Watson 20-08, DeRozan 08-09, enz.).
- Odds: TOTO gelezen op sport.toto.nl/wedden/wedstrijd/12223956 om 09:18 NL (22-10); Circus uit onze odds-feed
  (gegenereerd 07:18 UTC = 09:18 NL). 'Winnaar' en handicap/totaal bij TOTO = incl. verlenging.
  python3 specials/thunder_nuggets_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "Thunder – Nuggets voorspelling: wedtips en odds voor de NBA-kraker (23 oktober, 03:30)"
SLUG = "thunder-nuggets-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("Thunder – Nuggets is de seizoensopener van Denver. Voorspelling, wedtips, odds, blessures en "
                "opstellingen voor het NBA-duel van 03:30.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet365.nl/hub/nl-nl/open-account?affiliate=365_02599619"

# Deelkaart (OG-afbeelding)
OG_KOP = "Thunder – Nuggets <span>voorspelling</span>"
OG_EYEBROW = "NBA · vrijdag 23 oktober, 03:30"
OG_CHIPS = ["Opener Denver", "3 wedtips"]
OG_MOTIEF = "tabel"
OG_DATA = ["Aftrap · 03:30", "Arena · Paycom Center", "Onderling 25/26 · 3-1 OKC", "Favoriet · Thunder"]

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>In de nacht van donderdag op vrijdag om 03:30 Nederlandse tijd begint Denver zijn NBA-seizoen met een uitwedstrijd bij Oklahoma City Thunder. De Thunder won de opener in San Antonio overtuigend en is duidelijk favoriet. Onze voorspelling: Oklahoma City wint met 122-116. Hoofdtip: Denver Nuggets +8,5, met meer dan 235,5 punten als tweede tip.</strong></p>
<p>Het is een affiche met veel geschiedenis. In mei 2025 won Oklahoma City na zeven wedstrijden de tweede ronde van de play-offs tegen Denver, op weg naar de titel. Vorig seizoen was de Thunder in de onderlinge duels opnieuw de baas. Toch heeft Denver met Nikola Jokić en Jamal Murray een duo dat elke verdediging pijn kan doen. Hieronder lees je wat er veranderd is, wie er speelt, wat de bookmakers verwachten en welke weddenschappen wij interessant vinden.</p>
<h3><strong>Thunder – Nuggets: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "Oklahoma City Thunder – Denver Nuggets"),
    ("Datum", "Vrijdag 23 oktober 2026 (nacht van donderdag op vrijdag)"),
    ("Aanvang", "03:30 Nederlandse tijd (20:30 in Oklahoma City)"),
    ("Arena", "Paycom Center, Oklahoma City"),
    ("Competitie", "NBA, reguliere competitie 2026/27 (thuisopener Thunder, eerste wedstrijd Denver)"),
    ("Onderlinge duels 2025/26", "3-1 voor Oklahoma City"),
])}
<p>Oklahoma City is de thuisploeg. Dit seizoen ontmoeten beide teams elkaar nog drie keer: op 30 januari in Oklahoma City en op 2 februari en 11 april (Amerikaanse datum) in Denver.</p>
<h3><strong>Zo begon de Thunder het seizoen</strong></h3>
<p>Oklahoma City heeft er al één wedstrijd op zitten. Op dinsdag 20 oktober won de ploeg met 116-104 in San Antonio, bij de club die de Thunder vorig seizoen in de West-finale uitschakelde. De Thunder stond bijna de hele wedstrijd voor, leidde bij rust met 65-44 en had op het hoogtepunt een voorsprong van 26 punten. Shai Gilgeous-Alexander scoorde 32 punten, invaller Jared McCain maakte er 20 (zes van de acht driepunters raak) en Chet Holmgren had 14 punten, 7 rebounds en 4 blocks. San Antonio schoot maar 39 procent uit het veld en 10 van de 37 driepunters; Victor Wembanyama raakte slechts 1 van zijn 13 schoten.</p>
<p>Denver speelt deze nacht zijn eerste officiële wedstrijd. De Nuggets zijn dus volledig uitgerust. Oklahoma City had na de wedstrijd in San Antonio één rustdag; er is voor geen van beide ploegen sprake van een back-to-back.</p>
<h3><strong>Vorig seizoen: Thunder de beste, Denver vroeg klaar</strong></h3>
<p>Oklahoma City had in 2025/26 met 64-18 het beste record van de NBA en de beste verdediging van de competitie. Gilgeous-Alexander werd voor de tweede keer op rij MVP. In de play-offs won de Thunder van Phoenix en de Lakers (allebei 4-0), maar in de West-finale was San Antonio na zeven wedstrijden te sterk.</p>
<p>Denver werd met 54-28 derde in het Westen en won de laatste twaalf wedstrijden van de reguliere competitie. De Nuggets hadden de beste aanval van de NBA (122,6 punten per 100 balbezittingen), maar de verdediging was slechts de 21e van de competitie. In de eerste ronde van de play-offs ging het mis: Minnesota, als nummer zes geplaatst, won met 4-2. Denver kampte in die serie met blessures, onder meer bij Aaron Gordon en Peyton Watson.</p>
{tabel(["2025/26", "Oklahoma City Thunder", "Denver Nuggets"], [
    ("Eindstand", "64-18 (nr. 1 West)", "54-28 (nr. 3 West)"),
    ("Thuis / uit", "34-7 / 30-10 (plus 1 duel op neutraal terrein)", "28-13 / 26-15"),
    ("Punten voor / tegen", "119,0 / 107,9", "122,1 / 116,9"),
    ("Aanvallende rating (rang)", "7e van de NBA", "1e van de NBA"),
    ("Verdedigende rating (rang)", "1e van de NBA", "21e van de NBA"),
    ("Tegen de handicap (ATS)", "39-43", "44-38"),
    ("Play-offs", "West-finale verloren van San Antonio (3-4)", "Eerste ronde verloren van Minnesota (2-4)"),
])}
<p><em>Ratings in punten per 100 balbezittingen. Het duel op neutraal terrein was de halve finale van de NBA Cup in Las Vegas. De ATS-cijfers gaan over de reguliere competitie en kunnen per bron één tot twee wedstrijden verschillen.</em></p>"""

content2 = f"""<h3><strong>Zo zijn beide selecties veranderd</strong></h3>
<p><strong>Oklahoma City Thunder</strong></p>
<p>De Thunder nam deze zomer afscheid van drie vaste rotatiespelers: Lu Dort vertrok via een ruil naar Atlanta, Aaron Wiggins ging ook naar Atlanta en Isaiah Joe naar Detroit. Isaiah Hartenstein en Kenrich Williams tekenden opnieuw. In de draft kwamen center Aday Mara (nummer 12) en guard Bennett Stirtz (nummer 16) erbij. Belangrijker is dat Jalen Williams weer fit is, en dat Jared McCain zijn eerste volledige seizoen voor de club speelt. Coach Mark Daigneault heeft de kern rond Gilgeous-Alexander, Williams en Holmgren dus volledig bij elkaar.</p>
<p><strong>Denver Nuggets</strong></p>
<p>Bij Denver bleef de basisvijf intact, maar de bank is flink veranderd. Peyton Watson vertrok in augustus via een sign-and-trade naar Cleveland, Tim Hardaway Jr. tekende bij Miami, Jonas Valančiūnas werd ontslagen en ook Bruce Brown, Jalen Pickett en David Roddy zijn weg. Daar staan de 37-jarige DeMar DeRozan (zesvoudig All-Star, overgekomen van Sacramento) en Marvin Bagley III tegenover, allebei op een minimumcontract. Verder kwamen Alpha Diallo (vorig seizoen beste verdediger van de EuroLeague bij Monaco) en Trevon Brazile erbij. Opvallend: Oklahoma City deed deze zomer een contractbod op Spencer Jones, maar Denver evenaarde dat. Coach David Adelman begint aan zijn tweede volledige seizoen en noemt een plek bij de beste zes van het Westen het doel.</p>
<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("Nikola Topić", "Oklahoma City", "Speelt niet (rugoperatie)"),
    ("Thomas Sorber", "Oklahoma City", "Speelt niet (knieoperatie)"),
    ("Otega Oweh", "Oklahoma City", "Rest van het seizoen uitgeschakeld (achillespees)"),
    ("Julian Strawther", "Denver", "Speelt niet (verstuikte knie)"),
    ("Spencer Jones", "Denver", "Twijfelachtig (hamstrings)"),
])}
<p>Stand van het officiële blessurerapport op donderdagochtend 22 oktober. De sterren staan er niet op: Gilgeous-Alexander, Jalen Williams, Holmgren, Jokić, Murray en Gordon zijn allemaal inzetbaar.</p>
<p><strong>Verwachte basisvijf Oklahoma City:</strong> Shai Gilgeous-Alexander, Cason Wallace, Jalen Williams, Chet Holmgren, Isaiah Hartenstein. Dit vijftal begon ook in San Antonio.</p>
<p><strong>Verwachte basisvijf Denver:</strong> Jamal Murray, Christian Braun, Cameron Johnson, Aaron Gordon, Nikola Jokić. Dit vijftal stond vorig seizoen 23 keer samen aan de start en won daarvan er 18. DeRozan is naar verwachting de eerste man van de bank.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "Bijzonderheid"], [
    ("Shai Gilgeous-Alexander (OKC)", "31,1", "4,3", "6,6", "Scoorde 34, 36 en 35 punten tegen Denver vorig seizoen"),
    ("Chet Holmgren (OKC)", "17,1", "8,9", "1,7", "1,9 blocks, 4 blocks in de opener"),
    ("Jalen Williams (OKC)", "17,1", "4,6", "5,5", "Speelde door blessures maar 33 duels"),
    ("Nikola Jokić (DEN)", "27,7", "12,9", "10,7", "Gemiddeld een triple-double"),
    ("Jamal Murray (DEN)", "25,4", "4,4", "7,1", "43,5% van achter de driepuntlijn"),
    ("DeMar DeRozan (DEN)", "18,4", "2,9", "4,1", "Nieuwkomer, cijfers bij Sacramento"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26.</em></p>
<p>Let op Murray. Hij scoorde vorig seizoen 39 punten tegen Oklahoma City, en zijn vaste bewaker van de afgelopen jaren, Lu Dort, speelt niet meer voor de Thunder. Adelman wees daar zelf ook al op. Jokić maakte in de laatste twee onderlinge duels waarin hij speelde 23 punten, 17 rebounds en 14 assists en daarna 32 punten, 14 rebounds en 13 assists.</p>
<h3><strong>Odds Thunder – Nuggets bij Nederlandse bookmakers</strong></h3>
<p>De bookmakers zien Oklahoma City als duidelijke favoriet. De thuisploeg is fit, al op dreef en speelt voor eigen publiek. In de Amerikaanse markt is de Thunder 8,5 punten favoriet en ligt het verwachte puntentotaal op 235,5 punten. Die lijnen vind je ook terug bij TOTO.</p>
{tabel(["Markt", "Bookmaker", "Thunder", "Nuggets"], [
    ("Winnaar (incl. verlenging)", "<a href=\"/bookmakers/toto\">TOTO</a> en <a href=\"/bookmakers/circus\">Circus</a>", "1,31", "3,60"),
    ("1X2 (reguliere speeltijd, gelijk 18,0)", "TOTO", "1,29", "3,85"),
    ("Handicap -8,5 / +8,5 (incl. verlenging)", "TOTO", "1,95", "1,87"),
    ("Handicap -4,5 / +4,5 (incl. verlenging)", "Circus", "1,48", "2,45"),
])}
<p>Op het totaal kun je bij TOTO spelen op 235,5 punten: Over 1,91, Under 1,91 (inclusief verlenging). Circus biedt de lijn van 240,5 punten: Over 2,35, Under 1,53. Wij lazen de odds op donderdag 22 oktober om 09:18 uur. Odds kunnen tot de aftrap nog veranderen; vergelijk ze vlak voor de start nog even.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op Thunder – Nuggets</strong></a></p>"""

content3 = f"""<h3><strong>Onze voorspelling: Thunder wint, maar Denver blijft dichtbij</strong></h3>
<p>Oklahoma City is terecht favoriet. De Thunder heeft de beste verdediging van de NBA, speelt thuis en liet in San Antonio zien dat de ploeg ook zonder Dort, Joe en Wiggins direct klaar is. Vorig seizoen won Oklahoma City alle drie de duels waarin Gilgeous-Alexander en Jokić allebei speelden. Alleen het laatste duel in april ging naar Denver, maar toen lieten beide ploegen hun sterren rusten.</p>
<p>Toch verwachten we geen ruime zege. Die drie overwinningen van de Thunder waren met 10, 6 (na verlenging) en 3 punten verschil. Denver begint met dezelfde sterke basisvijf als vorig jaar, is volledig uitgerust en heeft in Jokić en Murray twee spelers die een wedstrijd in hun eentje kunnen beslissen. We rekenen ook op veel punten: de drie onderlinge duels met beide sterren eindigden op 232, 248 en 255 punten. Onze voorspelling: <strong>Oklahoma City Thunder – Denver Nuggets 122-116</strong>.</p>
<h3><strong>Wedtips voor Thunder – Nuggets</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Inzet"], [
    ("Denver Nuggets +8,5 punten (incl. verlenging)", "1,87", "TOTO", "Hoofdtip"),
    ("Meer dan 235,5 punten (incl. verlenging)", "1,91", "TOTO", "Tweede tip"),
    ("Shai Gilgeous-Alexander 30+ punten", "1,56", "TOTO", "Spelerstip"),
])}
<p><strong>1. Denver +8,5 (1,87).</strong> Denver mag met maximaal acht punten verliezen. In de laatste tien onderlinge duels waarin Jokić en Gilgeous-Alexander allebei speelden (inclusief de play-offserie van 2025), bleef Denver zeven keer binnen die marge. Oklahoma City is als grote favoriet bovendien niet altijd betrouwbaar tegen de handicap: vorig seizoen 39 keer wel en 43 keer niet. Het risico: als de Thunder net als in San Antonio een vroege voorsprong neemt, kan het verschil snel oplopen.</p>
<p><strong>2. Meer dan 235,5 punten (1,91).</strong> Denver had vorig seizoen de beste aanval van de NBA en ging in 52 van de 82 wedstrijden over de lijn van de bookmakers. Twee van de drie onderlinge duels met beide sterren kwamen boven de 235,5 uit. Eerlijk is eerlijk: de kans hierop is ongeveer 50 procent. De Thunder-verdediging is de beste van de competitie en in de play-offserie van 2025 bleven vijf van de zeven duels onder deze lijn. Zet hier dus een kleinere inzet op.</p>
<p><strong>3. Gilgeous-Alexander 30+ punten (1,56).</strong> De MVP scoorde vorig seizoen gemiddeld 31,1 punten en kwam in alle drie de duels met Denver boven de 30 (34, 36 en 35). In de opener maakte hij er 32. Het grootste risico is een ruime voorsprong, waardoor hij in het laatste kwart op de bank blijft. Controleer in de wedregels van TOTO of punten in een eventuele verlenging meetellen.</p>
<p>Speel je liever op de favoriet: een zege van Oklahoma City inclusief verlenging staat op 1,31 bij TOTO en Circus. Dat is weinig, maar wel een logische basis voor een combinatieweddenschap. Let op: in de 1X2-markt van TOTO telt alleen de reguliere speeltijd (gelijkspel 18,0).</p>
<h3><strong>Thunder – Nuggets live kijken in Nederland</strong></h3>
<p>De makkelijkste manier om de wedstrijd te zien: bij <a href="/bookmakers/bet365">Bet365</a> kijk je NBA-wedstrijden gratis live. Je hebt alleen een account met een kleine storting nodig, en die storting kun je daarna gewoon weer opnemen. In de Verenigde Staten zendt ESPN de wedstrijd uit; in Nederland heeft ESPN de NBA-rechten, maar niet elke wedstrijd staat op een van de Nederlandse ESPN-kanalen. Met <strong>NBA League Pass</strong>, de betaalde streamingdienst van de competitie, kun je ook alle wedstrijden volgen.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk Thunder – Nuggets live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Lees ook onze voorspelling voor <a href="/nieuws/spurs-thunder-voorspelling-wedtips-nba-opening-2026">Spurs – Thunder</a>, ons overzicht <a href="/nieuws/nba-voorspellingen-vannacht-22-oktober-2026">NBA voorspellingen vannacht</a> en het artikel <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">Welke Nederlanders spelen in de NBA</a>. Nieuw met basketbal? In <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels van de NBA</a> lees je hoe het spel werkt. Alle basketbaltips vind je op onze pagina <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Thunder – Nuggets?</strong><br>Vrijdag 23 oktober 2026 om 03:30 Nederlandse tijd, in de nacht van donderdag op vrijdag. In Oklahoma City is het dan donderdagavond 20:30.</p>
<p><strong>Waar wordt Thunder – Nuggets gespeeld?</strong><br>In het Paycom Center in Oklahoma City. De Thunder is de thuisploeg.</p>
<p><strong>Wie is favoriet: Thunder of Nuggets?</strong><br>Oklahoma City, met een quotering van 1,31. Denver staat op 3,60.</p>
<p><strong>Speelt Nikola Jokić mee?</strong><br>Ja. Jokić staat niet op het blessurerapport. Bij Denver ontbreekt alleen Julian Strawther zeker; Spencer Jones is twijfelachtig.</p>
<p><strong>Heeft Denver al gespeeld dit seizoen?</strong><br>Nee, dit is de eerste wedstrijd van Denver. Oklahoma City won zijn opener op 20 oktober met 116-104 in San Antonio.</p>
<p><strong>Wie won de onderlinge duels vorig seizoen?</strong><br>Oklahoma City, met 3-1. In de play-offs van 2025 won de Thunder in de tweede ronde ook van Denver, met 4-3.</p>
<p><strong>Waar kan ik Thunder – Nuggets live kijken?</strong><br>Gratis live bij Bet365, met een account met een kleine storting. Ook via NBA League Pass kun je alle wedstrijden volgen.</p>
<p><strong>Wat is onze voorspelling voor Thunder – Nuggets?</strong><br>Oklahoma City wint met 122-116. Onze hoofdtip is Denver +8,5 punten inclusief verlenging (1,87 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

WEDTIPS = {"wedtip-1-2": "Denver Nuggets +8.5 punten (incl. verlenging)", "quotering-wedtip-1": "1.87",
           "wedtip-2-2": "Meer dan 235.5 punten (incl. verlenging)", "quotering-wedtip-2": "1.91",
           "wedtip-3-2": "Shai Gilgeous-Alexander 30+ punten", "quotering-wedtip-3": "1.56",
           "bookmaker-wedtips": "669ab9f5aceb8b717cea24c3"}

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_BASKETBAL, "competitie": COMPETITIE_NBA,
          "datum-tijd-van-wedstrijd": "2026-10-23T01:30:00.000Z",
          "publicatiedatum": datetime.now(timezone.utc).isoformat(), **WEDTIPS}
    # Alleen dry run: dit script publiceert niets.
    import re
    tekst = re.sub(r"<[^>]+>", " ", content + content2 + content3)
    print(len(TITEL), "tekens titel |", len(SAMENVATTING), "tekens samenvatting |", len(tekst.split()), "woorden")
