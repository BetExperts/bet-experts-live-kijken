# -*- coding: utf-8 -*-
"""Los artikel: de 2 beste NBA-wedtips van vannacht, dinsdag 17 op woensdag 18 november 2026 (5 wedstrijden).
Jasper vroeg om 1 of 2 tips, alleen de allerbeste - dus bewust kort gehouden op het aantal picks,
niet op de onderbouwing.

Tips: Los Angeles Lakers -4,5 (1,55) en LA Clippers -4,5 (1,72). Combi 2,67.
Odds: 711 (Kambi sevelevnl), dinsdag 17-11 avond. Markt: Handicap - Winnaar, inclusief verlenging.

EIGEN BEREKENING uit alle uitslagen van dit seizoen (zelfde methode als 17-11):
per wedstrijd het thuissaldo van de thuisploeg tegen het uitsaldo van de uitploeg. Twee duels
springen eruit met +16,0 en +17,5; de andere drie zitten onder de +6,5 en krijgen geen tip.
De marges per wedstrijd zijn apart nagelopen, want een gemiddelde kan op twee uitschieters drijven:
  Charlotte uit: +7, -8, -16, -10, -5, -8  -> Lakers -4,5 zou in 5 van de 6 raak zijn geweest
  Utah uit:      -20, -22, -7, -12, -15, -7 -> nog NOOIT een uitnederlaag met minder dan 7 verschil
Rust: alleen Minnesota en Portland spelen een back-to-back (zij speelden 17-11 tegen elkaar);
de acht andere ploegen speelden voor het laatst op 15 november en hebben twee dagen rust.
Geen unders (Jasper 13-11). Resultaten van eerdere NBA-tips niet noemen (Jasper 30-10).
  python3 specials/nba_vannacht_2026_11_18.py   (alleen dry run, publiceert niets)
  kaart: ../superodd-agent/.venv/bin/python og_kaarten/nhl_top3.py nba_vannacht_2026_11_18
  publiceren: set -a; . ../superodd-agent/.env; set +a; ../superodd-agent/.venv/bin/python specials/concept_publiceer.py nba_vannacht_2026_11_18 --live
  daarna: ... specials/nba_vannacht_2026_11_18.py --velden"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel
import bet365_streams as B365

SLUG = "nba-voorspellingen-vannacht-18-november-2026"
RUBRIEK = "672293e14a76d88272bc0b61"   # Basketball
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BOOKMAKER_711 = "66a8a87062108480763b7309"
TITEL = "NBA voorspellingen vannacht: 2 beste wedtips (18 november)"
SAMENVATTING = ("De 2 beste NBA-wedtips van vannacht: de Lakers -4,5 tegen Charlotte en de Clippers -4,5 tegen "
                "Utah. Met odds, tijden en uitleg.")
DATUM = "2026-11-18T00:30:00.000Z"     # eerste wedstrijd: 01:30 NL
BET365 = "https://www.bet-experts.nl/go/bet365"

OG_LIGA, OG_SPORT = "nba", "Basketbal"
OG_EYEBROW_DATUM = "18 november"
OG_GISTEREN = ("Wedstrijden", "5")
OG_RECHTS = "Handicap incl. verlenging · 711"
TOP3 = [("05:00", "Lakers", "lal", "Hornets", "cha", "Lakers -4,5", "1,55", "73%"),
        ("04:30", "Clippers", "lac", "Jazz", "utah", "Clippers -4,5", "1,72", "67%")]

L = {"regels": '<a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels van de NBA</a>',
     "handicap": '<a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">hoe handicap wedden werkt</a>',
     "kans": '<a href="/nieuws/kans-berekenen-uit-odds-impliciete-kans">hoe je een odd omrekent naar een kans</a>',
     "711": '<a href="/bookmakers/711">711</a>',
     "hub": '<a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>',
     "legaal": '<a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>',
     "kijken": '<a href="/live-kijken">live kijken</a>',
     "tv": '<a href="/nieuws/voetbal-op-tv-deze-week">het weekoverzicht op tv</a>'}

MARKT_H = "Handicap - Winnaar, inclusief verlenging"

# (tijd NL, thuis, uit, odd thuis, odd uit) - markt 'Winnaar inclusief verlenging' bij 711
PROGRAMMA = [
    ("01:30", "Toronto Raptors", "New York Knicks", 2.25, 1.66),
    ("02:00", "San Antonio Spurs", "Detroit Pistons", 1.25, 4.10),
    ("02:00", "Minnesota Timberwolves", "Portland Trail Blazers", 1.70, 2.18),
    ("04:30", "LA Clippers", "Utah Jazz", 1.41, 2.95),
    ("05:00", "Los Angeles Lakers", "Charlotte Hornets", 1.30, 3.65),
]
HOOFDLIJN = {"New York Knicks": "-2,5", "San Antonio Spurs": "-9,5", "Minnesota Timberwolves": "-2,5",
             "LA Clippers": "-6,5", "Los Angeles Lakers": "-7,5"}
LIJNEN = {("Los Angeles Lakers", "-4,5"): 1.55, ("Los Angeles Lakers", "-3,5"): 1.48, ("Los Angeles Lakers", "-7,5"): 1.85,
          ("LA Clippers", "-4,5"): 1.72, ("LA Clippers", "-3,5"): 1.63, ("LA Clippers", "-6,5"): 1.93}

# Eigen berekening: (wedstrijd, thuissaldo thuisploeg, uitsaldo uitploeg, verschil)
SALDO = [("Clippers – Jazz", "+3,7 (7 duels)", "–13,8 (6 duels)", "<strong>+17,5</strong>"),
         ("Lakers – Hornets", "+9,3 (6 duels)", "–6,7 (6 duels)", "<strong>+16,0</strong>"),
         ("Timberwolves – Blazers", "+13,4 (8 duels)", "+7,1 (8 duels)", "+6,3"),
         ("Raptors – Knicks", "+6,8 (6 duels)", "+1,8 (6 duels)", "+5,0"),
         ("Spurs – Pistons", "+11,7 (7 duels)", "+7,0 (7 duels)", "+4,7")]

CHA_UIT = [7, -8, -16, -10, -5, -8]        # marges van Charlotte in zijn zes uitwedstrijden
UTAH_UIT = [-20, -22, -7, -12, -15, -7]    # marges van Utah in zijn zes uitwedstrijden
LAL_THUIS = [22, 8, -7, 6, 21, 6]          # marges van de Lakers in zijn zes thuiswedstrijden
LAC_THUIS = [25, -16, -7, -1, 16, 1, 8]    # marges van de Clippers in zijn zeven thuiswedstrijden


def q(x):
    return f"{x:.2f}".replace(".", ",")


def gem(xs):
    return f"{sum(xs) / len(xs):.1f}".replace(".", ",")


COMBI = q(1.55 * 1.72)
UITBET = f"{10 * 1.55 * 1.72:.2f}".replace(".", ",")
CHA_GEM, UTAH_GEM = gem(CHA_UIT), gem(UTAH_UIT)
KIJK = B365.kijk_zin("Basketball", DATUM[:10], [(p[1], p[2]) for p in PROGRAMMA], link="/bookmakers/bet365")
KIJK = (KIJK + " ") if KIJK else ""

TIPS = [
    {"wedstrijd": "Los Angeles Lakers vs. Charlotte Hornets", "competitie": "NBA", "speeltijd_utc": "2026-11-18T04:00:00Z",
     "tijd_nl": "05:00", "tip": "Los Angeles Lakers -4,5 (incl. verlenging)", "odds": "1.55", "markt": MARKT_H,
     "lijn": ("Los Angeles Lakers", "-4,5"),
     "analyse": "De Lakers staan op 12-2, wonnen acht keer op rij en scoren thuis 129,0 punten per wedstrijd. Charlotte maakt uit maar 97,2 punten en verloor vijf van zijn zes uitwedstrijden."},
    {"wedstrijd": "LA Clippers vs. Utah Jazz", "competitie": "NBA", "speeltijd_utc": "2026-11-18T03:30:00Z",
     "tijd_nl": "04:30", "tip": "LA Clippers -4,5 (incl. verlenging)", "odds": "1.72", "markt": MARKT_H,
     "lijn": ("LA Clippers", "-4,5"),
     "analyse": f"Utah staat op 1-13, is 0-6 in uitwedstrijden en verloor die zes keer met gemiddeld {UTAH_GEM} punten verschil - nooit met minder dan zeven. De ploeg mist bovendien haar hele frontcourt."},
]

WEDTIPS = {"wedstrijd-1": "Los Angeles Lakers vs Charlotte Hornets", "wedtip-1-2": "Los Angeles Lakers -4.5 (incl. verlenging)", "quotering-wedtip-1": "1.55",
           "wedstrijd-2": "LA Clippers vs Utah Jazz", "wedtip-2-2": "LA Clippers -4.5 (incl. verlenging)", "quotering-wedtip-2": "1.72"}

content = f"""<p><strong>Onze 2 beste NBA-wedtips van vannacht: Los Angeles Lakers wint met minstens vijf punten verschil van Charlotte Hornets (-4,5, odd 1,55) en LA Clippers doet hetzelfde tegen Utah Jazz (-4,5, odd 1,72). Allebei bij {L['711']} en allebei inclusief verlenging. Er staan vannacht vijf NBA-wedstrijden op het programma, van 01:30 tot 05:00 uur Nederlandse tijd.</strong></p>
<p>Een korte speelronde, en dat komt goed uit: wij geven liever twee tips waar we achter staan dan vijf om de lijst vol te maken. Wij liepen alle vijf de duels na, rekenden per wedstrijd het thuissaldo van de thuisploeg af tegen het uitsaldo van de uitploeg, controleerden daarna de marges per wedstrijd en pas als laatste de odds. Twee duels sprongen eruit, en dat zijn precies de twee die hieronder staan. Een tip blijft een inschatting; zet alleen in wat je kunt missen.</p>
<p><strong>Kijken?</strong> {KIJK}Met NBA League Pass, de betaalde dienst van de competitie, zie je alle NBA-wedstrijden. Meer opties lees je op onze pagina {L['kijken']}.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk de NBA vannacht live</strong></a></p>
<h3><strong>De 2 beste NBA-wedtips van vannacht</strong></h3>
{tabel(["Wedstrijd", "Tip", "Markt", "Odd", "Onze kans"], [
    ("Lakers – Hornets (05:00)", "<strong>Los Angeles Lakers -4,5</strong>", "Handicap, incl. verlenging", "1,55", "73% (odd: 65%)"),
    ("Clippers – Jazz (04:30)", "<strong>LA Clippers -4,5</strong>", "Handicap, incl. verlenging", "1,72", "67% (odd: 58%)"),
])}
<p><em>Odds bij {L['711']}, gelezen op dinsdagavond 17 november. Odds kunnen tot de start nog veranderen. Beide tips gelden inclusief een eventuele verlenging. Het zijn losse tips: wie ze combineert, krijgt een totale odd van {COMBI} — dan moeten ze allebei goed zijn en levert €10 inzet €{UITBET} op. Achter "odd" staat de kans die de odd zelf aangeeft; lees {L['kans']}.</em></p>
<h3><strong>Het NBA-programma van vannacht (Nederlandse tijd)</strong></h3>
{tabel(["Tijd", "Wedstrijd", "Winnaar (thuis – uit)", "Hoofdlijn handicap"], [
    (f"<strong>{t}</strong>", f"{h} – {u}", f"{q(oh)} – {q(ou)}",
     f"{[k for k in (h, u) if k in HOOFDLIJN][0].split()[-1]} {HOOFDLIJN[[k for k in (h, u) if k in HOOFDLIJN][0]]}")
    for t, h, u, oh, ou in PROGRAMMA
])}
<p><em>In de laatste kolom staat de hoofdlijn: de handicap waarbij beide kanten ongeveer even waarschijnlijk zijn. Onze twee tips zitten daar bewust onder, zodat er marge overblijft. Alleen Minnesota en Portland spelen vannacht hun tweede duel in twee dagen — zij troffen elkaar dinsdagnacht ook al. De andere acht ploegen speelden voor het laatst op 15 november en hebben dus twee dagen rust.</em></p>
<h3><strong>Thuissaldo tegen uitsaldo: waarom juist deze twee</strong></h3>
<p>Dit is onze eigen berekening uit alle uitslagen van dit seizoen. Per wedstrijd zetten we het <strong>thuissaldo van de thuisploeg</strong> (punten voor min punten tegen, per thuiswedstrijd) tegenover het <strong>uitsaldo van de uitploeg</strong>. Het verschil in de laatste kolom is een ruwe schatting van het verwachte puntenverschil.</p>
{tabel(["Wedstrijd", "Thuissaldo thuisploeg", "Uitsaldo uitploeg", "Verschil"],
       [(f"<strong>{w}</strong>", t, u, v) for w, t, u, v in SALDO])}
<p><em>Eigen berekening, bijgewerkt na de wedstrijden van dinsdagnacht. Het aantal duels staat erbij, want bij zes wedstrijden zegt een saldo minder dan bij acht.</em></p>
<p>De bovenste twee staan met +17,5 en +16,0 ver boven de rest; de andere drie blijven onder de +6,5. Dat is geen klein verschil maar een gat, en het komt in beide gevallen van dezelfde kant: een uitploeg die dit seizoen simpelweg niet functioneert buiten de eigen zaal.</p>"""

content2 = f"""<h3><strong>Tip 1: Los Angeles Lakers – Charlotte Hornets (05:00)</strong></h3>
<p><strong>De tip: Los Angeles Lakers -4,5, odd 1,55. Markt: Handicap - Winnaar, inclusief verlenging.</strong> De Lakers moeten met minstens vijf punten verschil winnen. Rekenvoorbeeld: bij 120-115 is de tip goed, bij 119-115 is de tip verloren.</p>
<p><strong>Waarom deze markt?</strong> Een zege van de Lakers staat op 1,30: te laag voor een losse tip. De hoofdlijn ligt op -7,5 (1,85). Met -4,5 hebben we drie punten extra marge en blijft de odd speelbaar.</p>
<p><strong>Vorm en cijfers.</strong> De Lakers staan op 12-2 en wonnen hun laatste <strong>acht wedstrijden op rij</strong>. Thuis zijn ze 5-1 met een saldo van +9,3 per wedstrijd, en daar scoren ze <strong>129,0 punten</strong> — het hoogste thuisgemiddelde van alle tien de ploegen die vannacht spelen. Over het hele seizoen staat de teller op 122,8 voor en 114,9 tegen.</p>
<p><strong>Aan de andere kant.</strong> Charlotte staat op 4-9 en is uit 1-5. En dan het cijfer dat deze tip draagt: de ploeg maakt in uitwedstrijden <strong>97,2 punten per wedstrijd</strong>. Dat is het enige gemiddelde onder de honderd van de hele speelronde. Over het hele seizoen scoort Charlotte 99,1 punten — ook daarmee staan ze als enige onder de honderd. De zes uitwedstrijden leverden deze marges op: {", ".join(str(m) for m in CHA_UIT[:-1])} en {CHA_UIT[-1]}. Eén zege, vijf nederlagen — en <strong>alle vijf met minstens vijf punten verschil</strong>. Onze lijn van -4,5 zou in vijf van die zes uitwedstrijden geraakt zijn.</p>
<p><strong>De man die het verschil maakt.</strong> Luka Dončić gooit er dit seizoen <strong>39,0 punten per wedstrijd</strong> in, met 7,8 assists en 7,2 rebounds. Dat is geen normaal cijfer — dat is het soort seizoen dat een ploeg in zijn eentje boven de lijn tilt. Bij Charlotte komt Brandon Miller tot 19,2 punten.</p>
<p><strong>Blessures.</strong> De Lakers missen <strong>Austin Reaves</strong> en Walker Kessler; dat is de belangrijkste kanttekening bij deze tip. Charlotte mist Kon Knueppel en Dennis Schröder.</p>
<p><strong>Onze voorspelling: Los Angeles Lakers – Charlotte Hornets 124-110.</strong> De odd van 1,55 gaat uit van 65%, wij schatten de kans op 73%. <strong>Het risico:</strong> zonder Reaves valt er scorend gewicht weg, en de Lakers wonnen thuis twee van hun zes duels met precies zes punten verschil — dicht bij onze lijn. Liever veiliger? Lakers -3,5 staat op 1,48.</p>
<h3><strong>Tip 2: LA Clippers – Utah Jazz (04:30)</strong></h3>
<p><strong>De tip: LA Clippers -4,5, odd 1,72. Markt: Handicap - Winnaar, inclusief verlenging.</strong> De Clippers moeten met minstens vijf punten verschil winnen. Rekenvoorbeeld: bij 112-107 is de tip goed, bij 111-107 is de tip verloren.</p>
<p><strong>Waarom deze markt?</strong> Een zege van de Clippers staat op 1,41 en de hoofdlijn ligt op -6,5 (1,93). Met -4,5 vragen we twee punten minder dan de markt zelf verwacht.</p>
<p><strong>Het cijfer dat deze tip draagt.</strong> Utah staat op 1-13 en is <strong>0-6 in uitwedstrijden</strong>. Belangrijker dan die nul is hóé die zes verliespartijen eindigden: {", ".join(str(abs(m)) for m in UTAH_UIT[:-1])} en {abs(UTAH_UIT[-1])} punten verschil. Met andere woorden: <strong>Utah verloor dit seizoen nog geen enkele uitwedstrijd met minder dan zeven punten verschil</strong>, en gemiddeld met {UTAH_GEM}. Uit scoort de ploeg 105,2 punten en geeft er 119,0 weg.</p>
<p><strong>De reden staat op de blessurelijst.</strong> Utah mist <strong>Lauri Markkanen, Jusuf Nurkić, Jaren Jackson Jr. en Jaxson Hayes</strong> — in de praktijk het volledige frontcourt. Keyonte George (20,3 punten) moet het dragen. Dat verklaart zowel het puntentekort als het aantal punten dat de ploeg tegen krijgt.</p>
<p><strong>Aan de andere kant.</strong> Eerlijk is eerlijk: de Clippers zijn zelf geen goede ploeg. Ze staan op 4-8 met een saldo van –4,2 en missen Brandon Ingram en Bradley Beal. Maar thuis zijn ze 4-3 met een positief saldo, en Darius Garland komt tot 21,2 punten en 6,9 assists. Tegen de slechtste uitploeg van de competitie is dat genoeg.</p>
<p><strong>Onze voorspelling: LA Clippers – Utah Jazz 115-103.</strong> De odd van 1,72 gaat uit van 58%, wij schatten de kans op 67%. <strong>Het risico:</strong> de Clippers zijn thuis wisselvallig — drie van hun zeven thuisduels gingen verloren, waaronder één met zestien punten verschil. Dit is de tip met de grootste odd van de twee, en dat is niet toevallig. Liever veiliger? Clippers -3,5 staat op 1,63.</p>
<h3><strong>De drie wedstrijden waar we vanaf blijven</strong></h3>
<p><strong>Spurs – Pistons (02:00)</strong>: op papier de mooiste wedstrijd van de nacht. San Antonio staat op 12-2 met het beste saldo van de speelronde (+12,9) en Victor Wembanyama maakt 28,6 punten met 11,6 rebounds en 4,3 blocks. Maar Detroit is uit 5-2 met een saldo van +7,0, en de hoofdlijn ligt meteen op -9,5. Detroit mist vijf spelers, onder wie Jalen Duren, maar Cade Cunningham (25,7 punten, 7,9 assists) is er wel. Het gat in de cijfers is met +4,7 te klein voor de marge die de markt vraagt.</p>
<p><strong>Timberwolves – Blazers (02:00)</strong>: dezelfde twee ploegen stonden dinsdagnacht ook al tegenover elkaar, in dezelfde zaal — Minnesota won toen. Nu spelen ze allebei hun tweede wedstrijd in twee dagen. Minnesota mist Anthony Edwards en Donte DiVincenzo, Portland mist Ja Morant en Shaedon Sharpe. Twee halve ploegen met moeë benen en een hoofdlijn van -2,5: daar valt voor ons niets te halen.</p>
<p><strong>Raptors – Knicks (01:30)</strong>: Toronto mist Kawhi Leonard, en New York is met 1,66 favoriet. Maar het Toronto-thuissaldo (+6,8) drijft volledig op twee uitschieters van 43 en 30 punten; in de vier andere thuiswedstrijden verloren ze. Zo'n gemiddelde zegt te weinig om er geld op te zetten.</p>"""

content3 = f"""<h3><strong>Handicap bij de NBA: hoe werkt het?</strong></h3>
<p>Bij de NBA eindigt een wedstrijd nooit in een gelijkspel: bij een gelijke stand na 48 minuten volgt een verlenging van vijf minuten. Onze tips van vannacht gelden allebei <strong>inclusief verlenging</strong>, dus die vijf minuten tellen mee voor het puntenverschil.</p>
{tabel(["Markt", "Wat telt mee", "Voorbeeld vannacht"], [
    ("<strong>Winnaar</strong>", "Eindstand inclusief verlenging. Er is altijd een winnaar.", "Lakers winnen van Charlotte: 1,30"),
    ("<strong>Handicap</strong>", "Eindstand inclusief verlenging, met een puntenachterstand voor de favoriet.", "Lakers -4,5: 1,55"),
    ("<strong>Hoofdlijn</strong>", "De handicap waarbij beide kanten ongeveer even waarschijnlijk zijn.", "Lakers -7,5: 1,85"),
])}
<p>Een min-handicap trekt punten af van de favoriet. Bij Lakers -4,5 haal je in gedachten 4,5 punt weg bij Los Angeles: wint de ploeg met vijf punten of meer, dan is de tip goed. De halve punt zorgt ervoor dat je inzet nooit wordt teruggestort. Hoe lager de handicap, hoe groter de kans en hoe lager de odd. Lees ook {L['handicap']} en {L['regels']}.</p>
<p>Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit. Twijfel je? Lees {L['legaal']}. Alle basketbaltips vind je op onze pagina {L['hub']}, en welke sport er verder op tv is, staat in {L['tv']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wat zijn de beste NBA-wedtips van vannacht?</strong><br>Los Angeles Lakers -4,5 tegen Charlotte Hornets (1,55) en LA Clippers -4,5 tegen Utah Jazz (1,72), beide odds bij 711 en beide inclusief verlenging. Zet alleen in wat je kunt missen.</p>
<p><strong>Hoeveel NBA-wedstrijden zijn er vannacht?</strong><br>Vijf, met tien ploegen. De eerste begint om 01:30 uur Nederlandse tijd, de laatste (Lakers – Hornets) om 05:00 uur.</p>
<p><strong>Hoeveel punten maakt Luka Dončić dit seizoen?</strong><br>39,0 per wedstrijd, met 7,8 assists en 7,2 rebounds. Het is veruit het hoogste gemiddelde van alle spelers die vannacht in actie komen.</p>
<p><strong>Speelt Austin Reaves vannacht?</strong><br>Nee. De Lakers melden hem als out, net als Walker Kessler.</p>
<p><strong>Waarom is Utah Jazz zo slecht uit?</strong><br>De ploeg staat 0-6 in uitwedstrijden en verloor die duels met gemiddeld {UTAH_GEM} punten verschil. Utah mist Lauri Markkanen, Jusuf Nurkić, Jaren Jackson Jr. en Jaxson Hayes — in de praktijk het hele frontcourt.</p>
<p><strong>Welke ploegen spelen vannacht een back-to-back?</strong><br>Alleen Minnesota en Portland; zij speelden dinsdagnacht ook al tegen elkaar. De andere acht ploegen hebben twee dagen rust gehad.</p>
<p><strong>Gelden de tips inclusief verlenging?</strong><br>Ja, allebei. Een verlenging telt mee voor de eindstand, dus ook voor het puntenverschil bij de handicaps.</p>
<p><strong>Waar kan ik de NBA vannacht live kijken?</strong><br>Alle vijf de wedstrijden staan in het streamingschema van Bet365, en met NBA League Pass zie je elke wedstrijd. Meer opties staan op onze pagina live kijken.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    if "--velden" in sys.argv:
        import lk_webflow as WF
        it = WF._req("GET", f"{WF.WF_API}/collections/{WF.NIEUWS_COLLECTION}/items?slug={SLUG}")["items"][0]
        fd = {"competitie": COMPETITIE_NBA, "bookmaker-wedtips": BOOKMAKER_711,
              "datum-tijd-van-wedstrijd": DATUM, **WEDTIPS}
        for pad in ("", "/live"):
            WF._req("PATCH", f"{WF.WF_API}/collections/{WF.NIEUWS_COLLECTION}/items/{it['id']}{pad}", {"fieldData": fd})
        print("velden gezet:", it["id"]); sys.exit()
    alles = content + content2 + content3
    woorden = len(re.sub(r"<[^>]+>", " ", alles).split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", woorden, "woorden |", len(TIPS), "tips")
    assert len(TITEL) <= 60 and 120 <= len(SAMENVATTING) <= 155, (len(TITEL), len(SAMENVATTING))
    assert 1400 <= woorden <= 2600, woorden
    assert KIJK, "geen Bet365-stream in het schema: KIJK-zin aanpassen"
    assert len(TIPS) == len(TOP3) == 2 and [q(float(t["odds"])) for t in TIPS] == [k[6] for k in TOP3]
    assert all(1.40 <= float(t["odds"]) <= 1.80 for t in TIPS)
    for t in TIPS:
        h, u = t["wedstrijd"].split(" vs. ")
        p = next(x for x in PROGRAMMA if x[1] == h and x[2] == u)
        assert t["tijd_nl"] == p[0] and float(t["odds"]) == LIJNEN[t["lijn"]], t
        ploeg, lijn = t["lijn"]
        assert float(lijn.replace(",", ".")) > float(HOOFDLIJN[ploeg].replace(",", ".")), t["lijn"]
    assert COMBI == "2,67" and UITBET == "26,66", (COMBI, UITBET)
    assert round(100 / 1.55) == 65 and round(100 / 1.72) == 58
    assert len(CHA_UIT) == len(UTAH_UIT) == 6 and len(LAL_THUIS) == 6 and len(LAC_THUIS) == 7
    assert max(UTAH_UIT) <= -7 and UTAH_GEM == "-13,8"        # nooit met minder dan 7 verloren
    assert sum(1 for m in CHA_UIT if m <= -5) == 5 and sum(1 for m in CHA_UIT if m > 0) == 1
    assert sum(1 for m in LAL_THUIS if m > 0) == 5 and LAL_THUIS.count(6) == 2
    assert sum(1 for m in LAC_THUIS if m < 0) == 3 and min(LAC_THUIS) == -16
    assert 120 - 115 >= 5 and 119 - 115 < 5 and 124 - 110 >= 5      # rekenvoorbeelden tip 1
    assert 112 - 107 >= 5 and 111 - 107 < 5 and 115 - 103 >= 5      # tip 2
    assert len(PROGRAMMA) == 5 and len(SALDO) == 5
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert "<h2" not in alles and "<h4" not in alles
    for verboden in ("betcity", "espn", "footymetrics", "opstellingvandaag", "waaroptv", "toto"):
        assert verboden not in alles.lower(), verboden
    assert not re.search(r"\bunder\b", alles, re.I) and alles.count(BET365) == 1
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/") or href == BET365, href
    print("dry run ok - niets gepubliceerd")
