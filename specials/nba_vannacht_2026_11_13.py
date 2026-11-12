# -*- coding: utf-8 -*-
"""Los artikel: de 3 beste NBA-wedtips van vannacht, donderdag 12 op vrijdag 13 november 2026 (4 wedstrijden).
Zelfde opzet als nba_vannacht_2026_11_11.py, deelkaart via og_kaarten/nhl_top3.py met OG_LIGA = "nba".
Feiten nagelopen op 12-11-2026 (±15:30 NL): ESPN-scoreboard 12-11, teamschema's 2026/27, wedstrijdpagina's
(event-id's 401909976-401909979: blessurelijst, leiders, thuis/uit-balans), standen, box scores van de laatste drie duels
(wie speelde er echt: Edwards en DiVincenzo misten alle drie; Kawhi Leonard en Scottie Barnes ook; Miller, Knueppel en
Schröder misten de laatste wedstrijd; Duren de laatste drie; Embiid en LeBron speelden alle drie).
- Back-to-back: Toronto (woensdagnacht 93-98 tegen Boston) en Washington (woensdagnacht 101-114 in Indiana).
- Odds: TOTO, donderdag 12-11 rond 15:30 NL (wedstrijdpagina's). Tips: Handicap - Winnaar (inc OT). Geen unders.
- Resultaten van eerdere NBA-tips niet noemen (eigenaar 30-10).
  python3 specials/nba_vannacht_2026_11_13.py   (alleen dry run, publiceert niets)"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel
import bet365_streams as B365

SLUG = "nba-voorspellingen-vannacht-13-november-2026"
RUBRIEK = "672293e14a76d88272bc0b61"   # Basketball
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
TITEL = "NBA voorspellingen vannacht: 3 beste wedtips (13 november)"
SAMENVATTING = ("De 3 beste NBA-wedtips van vannacht: 76ers -5,5 tegen Toronto, Pistons -6,5 in Washington en "
                "Suns -3,5 tegen een uitgedund Charlotte.")
DATUM = "2026-11-13T00:00:00.000Z"     # eerste wedstrijd: 01:00 NL
BET365 = "https://www.bet-experts.nl/go/bet365"

OG_LIGA, OG_SPORT = "nba", "Basketbal"
TOP3 = [("01:00", "76ers", "phi", "Raptors", "tor", "76ers -5,5", "1,51", "71%"),
        ("01:00", "Wizards", "wsh", "Pistons", "det", "Pistons -6,5", "1,50", "71%"),
        ("03:00", "Suns", "phx", "Hornets", "cha", "Suns -3,5", "1,58", "68%")]
OG_EYEBROW_DATUM = "13 november"
OG_GISTEREN = ("Wedstrijden", "4")
OG_RECHTS = "Incl. verlenging · TOTO"

L = {"regels": '<a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels van de NBA</a>',
     "handicap": '<a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">hoe handicap wedden werkt</a>',
     "kans": '<a href="/nieuws/kans-berekenen-uit-odds-impliciete-kans">hoe je een odd omrekent naar een kans</a>',
     "toto": '<a href="/bookmakers/toto">TOTO</a>',
     "hub": '<a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>'}

# (tijd NL, thuis, uit, odd thuis, odd uit, back-to-back)  TOTO 'Winnaar' (inclusief verlenging)
PROGRAMMA = [
    ("01:00", "Philadelphia 76ers", "Toronto Raptors", 1.27, 3.85, "Raptors"),
    ("01:00", "Washington Wizards", "Detroit Pistons", 4.25, 1.22, "Wizards"),
    ("02:00", "Minnesota Timberwolves", "Dallas Mavericks", 1.45, 2.80, "-"),
    ("03:00", "Phoenix Suns", "Charlotte Hornets", 1.40, 2.95, "-"),
]
LIJNEN = {("Philadelphia 76ers", "-5,5"): 1.51, ("Philadelphia 76ers", "-9,5"): 1.94, ("Philadelphia 76ers", "-3,5"): 1.38,
          ("Detroit Pistons", "-6,5"): 1.50, ("Detroit Pistons", "-10,5"): 1.91, ("Detroit Pistons", "-4,5"): 1.36,
          ("Phoenix Suns", "-3,5"): 1.58, ("Phoenix Suns", "-6,5"): 1.91, ("Phoenix Suns", "-1,5"): 1.43}

KIJK = B365.kijk_zin("Basketball", DATUM[:10], [(p[1], p[2]) for p in PROGRAMMA], link="/bookmakers/bet365")
KIJK = (KIJK + " ") if KIJK else ""
MARKT_H = "Handicap - Winnaar, inclusief verlenging"

WIZ_REEKS = [(105, 120), (132, 139), (75, 114), (111, 122), (101, 114)]     # vijf nederlagen op rij (ploeg eerst)
CHA_PUNTEN = [79, 104, 91, 104, 80, 124]                                     # laatste zes duels Charlotte


def q(x):
    return f"{x:.2f}".replace(".", ",")


def gem(xs):
    return f"{sum(xs) / len(xs):.1f}".replace(".", ",")


WIZ_GEM = gem([b - a for a, b in WIZ_REEKS])
CHA_GEM = gem(CHA_PUNTEN)
COMBI = q(1.51 * 1.50 * 1.58)

TIPS = [
    {"wedstrijd": "Philadelphia 76ers vs. Toronto Raptors", "competitie": "NBA", "speeltijd_utc": "2026-11-13T00:00:00Z",
     "tijd_nl": "01:00", "tip": "Philadelphia 76ers -5,5 (incl. verlenging)", "odds": "1.51", "bookmaker": "toto", "markt": MARKT_H,
     "lijn": ("Philadelphia 76ers", "-5,5"),
     "veld": "76ers – Raptors (01:00): Philadelphia 76ers -5,5 (incl. verlenging)",
     "analyse": "Toronto speelt een back-to-back en mist Kawhi Leonard en topscorer Scottie Barnes; Philadelphia staat op 9-3 en speelt met Maxey, Embiid en LeBron James."},
    {"wedstrijd": "Washington Wizards vs. Detroit Pistons", "competitie": "NBA", "speeltijd_utc": "2026-11-13T00:00:00Z",
     "tijd_nl": "01:00", "tip": "Detroit Pistons -6,5 (incl. verlenging)", "odds": "1.50", "bookmaker": "toto", "markt": MARKT_H,
     "lijn": ("Detroit Pistons", "-6,5"),
     "veld": "Wizards – Pistons (01:00): Detroit Pistons -6,5 (incl. verlenging)",
     "analyse": f"Washington verloor vijf keer op rij (gemiddeld met {WIZ_GEM} punten verschil) en speelt een back-to-back; Detroit won eerder deze week nog met 122-111 van dezelfde tegenstander en staat uit op 4-1."},
    {"wedstrijd": "Phoenix Suns vs. Charlotte Hornets", "competitie": "NBA", "speeltijd_utc": "2026-11-13T02:00:00Z",
     "tijd_nl": "03:00", "tip": "Phoenix Suns -3,5 (incl. verlenging)", "odds": "1.58", "bookmaker": "toto", "markt": MARKT_H,
     "lijn": ("Phoenix Suns", "-3,5"),
     "veld": "Suns – Hornets (03:00): Phoenix Suns -3,5 (incl. verlenging)",
     "analyse": f"Charlotte mist Brandon Miller, Kon Knueppel, Dennis Schröder en Grant Williams, scoort 98,8 punten per wedstrijd en won uit maar één van de vier duels."},
]

content = f"""<p><strong>Onze 3 beste NBA-wedtips van vannacht: Philadelphia 76ers wint met minstens zes punten verschil van Toronto Raptors (-5,5, odd 1,51), Detroit Pistons wint met minstens zeven punten verschil in Washington (-6,5, odd 1,50) en Phoenix Suns wint met minstens vier punten verschil van Charlotte Hornets (-3,5, odd 1,58). Alle drie bij TOTO en alle drie inclusief verlenging. Er staan vier NBA-wedstrijden op het programma, van 01:00 tot 03:00 uur Nederlandse tijd.</strong></p>
<p>Het is een korte NBA-nacht van donderdag 12 op vrijdag 13 november, maar wel een met duidelijke verschillen in fitheid. Toronto en Washington spelen allebei een back-to-back, en Toronto en Charlotte missen meerdere basisspelers. Wij liepen per wedstrijd de vorm, de blessurelijst, de box scores van de laatste wedstrijden en de cijfers na, en kozen de drie tips waar onze inschatting hoger ligt dan de kans die de odd aangeeft. Het zijn alle drie handicaps op de favoriet, maar telkens met een lagere lijn dan de hoofdlijn van de bookmaker: zo houden we marge. Een tip blijft natuurlijk een inschatting; zet alleen in wat je kunt missen.</p>
<p><strong>Kijken?</strong> {KIJK}Met NBA League Pass, de betaalde dienst van de competitie, zie je alle NBA-wedstrijden. Meer opties lees je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk de NBA vannacht live</strong></a></p>
<h3><strong>De 3 beste NBA-wedtips van vannacht</strong></h3>
{tabel(["Wedstrijd", "Tip", "Markt", "Odd", "Onze kans"], [
    ("76ers – Raptors (01:00)", "<strong>Philadelphia 76ers -5,5</strong>", "Handicap, incl. verlenging", "1,51", "71% (odd: 66%)"),
    ("Wizards – Pistons (01:00)", "<strong>Detroit Pistons -6,5</strong>", "Handicap, incl. verlenging", "1,50", "71% (odd: 67%)"),
    ("Suns – Hornets (03:00)", "<strong>Phoenix Suns -3,5</strong>", "Handicap, incl. verlenging", "1,58", "68% (odd: 63%)"),
])}
<p><em>Odds bij {L['toto']}, gelezen op donderdag 12 november rond 15:30. Odds kunnen tot de start nog veranderen. Alle drie de tips gelden inclusief een eventuele verlenging. Het zijn losse tips: wie ze combineert, krijgt een totale odd van {COMBI}, maar dan moeten ze alle drie goed zijn. Achter "odd" staat de kans die de odd zelf aangeeft; lees {L['kans']}.</em></p>
<h3><strong>Het NBA-programma van vannacht (Nederlandse tijd)</strong></h3>
{tabel(["Tijd", "Wedstrijd", "Winnaar (thuis – uit)", "Back-to-back"], [
    (f"<strong>{t}</strong>", f"{h} – {u}", f"{q(oh)} – {q(ou)}", b2b) for t, h, u, oh, ou, b2b in PROGRAMMA
])}
<p><em>Alle wedstrijden beginnen in de nacht van donderdag op vrijdag. De odds in deze tabel gelden voor de markt Winnaar, inclusief verlenging.</em></p>"""

content2 = f"""<h3><strong>Tip 1: Philadelphia 76ers – Toronto Raptors (01:00)</strong></h3>
<p><strong>De tip: Philadelphia 76ers -5,5, odd 1,51. Markt: Handicap - Winnaar, inclusief verlenging.</strong> Philadelphia moet met minstens zes punten verschil winnen. Rekenvoorbeeld: bij 112-106 is de tip goed, bij 110-105 is de tip verloren.</p>
<p><strong>Waarom deze markt?</strong> Een zege van Philadelphia staat op 1,27: te laag voor een losse tip. De hoofdlijn ligt op -9,5 (1,94). Met -5,5 hebben we vier punten extra marge en blijft de odd speelbaar.</p>
<p><strong>Vorm en cijfers.</strong> Philadelphia staat op 9-3 en is tweede in de Eastern Conference. In de nacht naar woensdag verloor de ploeg met 101-123 van Boston, maar daarvoor won ze vijf van de zes wedstrijden. Toronto staat op 5-6, verloor de laatste twee wedstrijden en speelde woensdagnacht nog thuis tegen Boston (93-98). Vannacht speelt Toronto dus een back-to-back, en dat op bezoek.</p>
<p><strong>Blessures.</strong> Bij Toronto ontbreken Kawhi Leonard (knie) en Scottie Barnes (lies), de topscorer met 23,5 punten en 7,6 rebounds per wedstrijd. Ze speelden de laatste drie wedstrijden allebei niet. Ook Nate Bittle is er niet bij. Bij Philadelphia zijn Joel Embiid (voet) en LeBron James (rug) twijfelachtig, maar ze speelden de laatste drie wedstrijden allebei ruim dertig minuten.</p>
<p><strong>Spelers om op te letten.</strong> Tyrese Maxey scoort 26,7 punten per wedstrijd, Embiid pakt 9,3 rebounds en LeBron James geeft 6,5 assists. Bij Toronto draait RJ Barrett zonder Leonard en Barnes de aanval; Jamal Shead geeft 6,9 assists.</p>
<p><strong>Onze voorspelling: Philadelphia 76ers – Toronto Raptors 116-106.</strong> De odd van 1,51 gaat uit van 66%, wij schatten de kans op 71%. Het risico: Embiid of LeBron haakt alsnog af, en Philadelphia ging tegen Boston zwaar onderuit. Liever veiliger? 76ers -3,5 staat op 1,38.</p>
<h3><strong>Tip 2: Washington Wizards – Detroit Pistons (01:00)</strong></h3>
<p><strong>De tip: Detroit Pistons -6,5, odd 1,50. Markt: Handicap - Winnaar, inclusief verlenging.</strong> Detroit moet met minstens zeven punten verschil winnen. Rekenvoorbeeld: bij 108-115 is de tip goed, bij 106-112 is de tip verloren.</p>
<p><strong>Waarom deze markt?</strong> Een zege van Detroit staat op 1,22 en de hoofdlijn ligt op -10,5 (1,91). Met -6,5 hebben we vier punten extra marge.</p>
<p><strong>Vorm en cijfers.</strong> Washington staat op 4-8 en verloor de laatste vijf wedstrijden, gemiddeld met {WIZ_GEM} punten verschil. Woensdagnacht verloor de ploeg nog met 101-114 in Indiana, dus vannacht volgt een back-to-back. Detroit staat op 7-3, is derde in het oosten en won uit vier van de vijf wedstrijden. Eerder deze week speelden beide ploegen ook al tegen elkaar: Detroit won toen met 122-111 in Detroit. Detroit heeft met +8,1 punten per wedstrijd een veel beter puntensaldo dan Washington (-5,9).</p>
<p><strong>Blessures.</strong> Detroit mist center Jalen Duren (hamstring), die de laatste drie wedstrijden al niet speelde, en schutter Isaiah Joe (heup). Washington mist Tristan Vukčević, Reece Beekman, Justin Champagnie en Jamir Watkins.</p>
<p><strong>Spelers om op te letten.</strong> Cade Cunningham scoort 22,3 punten met 7,6 assists voor Detroit. Bij Washington is Anthony Davis (25,2 punten en 10,0 rebounds) de grote man, en Trae Young geeft 8,3 assists.</p>
<p><strong>Onze voorspelling: Washington Wizards – Detroit Pistons 106-118.</strong> De odd van 1,50 gaat uit van 67%, wij schatten de kans op 71%. Het risico: met Davis en Young heeft Washington aanvallend genoeg kwaliteit om lang mee te gaan, en zonder Duren mist Detroit rebounds onder de basket. Liever veiliger? Pistons -4,5 staat op 1,36.</p>
<h3><strong>Tip 3: Phoenix Suns – Charlotte Hornets (03:00)</strong></h3>
<p><strong>De tip: Phoenix Suns -3,5, odd 1,58. Markt: Handicap - Winnaar, inclusief verlenging.</strong> Phoenix moet met minstens vier punten verschil winnen. Rekenvoorbeeld: bij 110-106 is de tip goed, bij 108-105 is de tip verloren.</p>
<p><strong>Waarom deze markt?</strong> Een zege van Phoenix staat op 1,40 en de hoofdlijn ligt op -6,5 (1,91). Met -3,5 hebben we drie punten extra marge.</p>
<p><strong>Vorm en cijfers.</strong> Charlotte staat op 4-7, scoort maar 98,8 punten per wedstrijd (het minste van alle ploegen die vannacht spelen) en krijgt er 110,4 tegen. In de laatste zes wedstrijden scoorde de ploeg gemiddeld {CHA_GEM} punten, met uitschieters naar beneden van 79 en 80 punten. Uit won Charlotte maar één van de vier wedstrijden. Phoenix staat op 4-6, maar won thuis vier van de zeven duels en won in de nacht naar woensdag nog met 133-110 van de Clippers.</p>
<p><strong>Blessures.</strong> Charlotte mist Brandon Miller (lies, 20,6 punten), Kon Knueppel (hamstring), Dennis Schröder (hamstring) en Grant Williams (hamstring); Moussa Diabaté (dij, 9,1 rebounds) is twijfelachtig. Phoenix mist alleen Mark Williams (schouder).</p>
<p><strong>Spelers om op te letten.</strong> Devin Booker scoort 25,1 punten per wedstrijd met 4,8 assists, en Miles Bridges pakt 7,4 rebounds.</p>
<p><strong>Onze voorspelling: Phoenix Suns – Charlotte Hornets 112-102.</strong> De odd van 1,58 gaat uit van 63%, wij schatten de kans op 68%. Het risico: Phoenix verloor dit seizoen ook al van zwakkere ploegen, en Charlotte won eerder deze week verrassend met 124-112 van Cleveland. Liever veiliger? Suns -1,5 staat op 1,43.</p>
<h3><strong>De andere NBA-wedstrijd van vannacht</strong></h3>
<p><strong>Timberwolves – Mavericks (02:00)</strong>: Minnesota staat op 8-3 en won de laatste vier wedstrijden, ondanks het ontbreken van Anthony Edwards (knie) en Donte DiVincenzo (achillespees). Rudy Gobert pakt 12,1 rebounds. Dallas won de laatste drie wedstrijden en rookie Cooper Flagg scoort 25,9 punten met 6,9 assists, maar mist Dereck Lively II. Minnesota wint staat op 1,45. Met twee ploegen in vorm en zonder Edwards zien wij hier geen duidelijke voorsprong in de odds; wij laten dit duel liggen.</p>"""

content3 = f"""<h3><strong>Handicap bij de NBA: hoe werkt het?</strong></h3>
<p>Bij de NBA eindigt een wedstrijd nooit in een gelijkspel: bij een gelijke stand na 48 minuten volgt een verlenging van vijf minuten. Onze tips van vannacht zijn alle drie <strong>inclusief verlenging</strong>.</p>
{tabel(["Markt", "Wat telt mee", "Voorbeeld vannacht"], [
    ("<strong>Winnaar</strong>", "Eindstand inclusief verlenging. Er is altijd een winnaar.", "Pistons winnen in Washington: 1,22"),
    ("<strong>Handicap</strong>", "Eindstand inclusief verlenging, met een puntenachterstand voor de favoriet.", "Pistons -6,5: 1,50"),
    ("<strong>Hoofdlijn</strong>", "De handicap waarbij beide kanten ongeveer even waarschijnlijk zijn.", "Pistons -10,5: 1,91"),
])}
<p>Een min-handicap trekt punten af van de favoriet. Bij Pistons -6,5 haal je in gedachten 6,5 punten weg bij Detroit: wint de ploeg met zeven punten of meer, dan is de tip goed. Een half punt zorgt ervoor dat je inzet nooit wordt teruggestort. Hoe lager de handicap, hoe groter de kans en hoe lager de odd. Lees ook {L['handicap']} en {L['regels']}.</p>
<p>Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit. Twijfel je? Lees <a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>. Alle basketbaltips vind je op onze pagina {L['hub']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wat zijn de beste NBA-wedtips van vannacht?</strong><br>Philadelphia 76ers -5,5 tegen Toronto Raptors (1,51), Detroit Pistons -6,5 bij Washington Wizards (1,50) en Phoenix Suns -3,5 tegen Charlotte Hornets (1,58), alle odds bij TOTO. Zet alleen in wat je kunt missen.</p>
<p><strong>Gelden de tips inclusief verlenging?</strong><br>Ja, alle drie. Een verlenging telt mee voor de eindstand, dus ook voor het puntenverschil bij de handicaps.</p>
<p><strong>Hoe laat beginnen de NBA-wedstrijden vannacht?</strong><br>76ers – Raptors en Wizards – Pistons beginnen om 01:00 uur Nederlandse tijd, Timberwolves – Mavericks om 02:00 uur en Suns – Hornets om 03:00 uur.</p>
<p><strong>Welke ploegen spelen vannacht een back-to-back?</strong><br>Toronto Raptors en Washington Wizards. Toronto verloor woensdagnacht met 93-98 van Boston, Washington met 101-114 in Indiana.</p>
<p><strong>Speelt Anthony Edwards vannacht?</strong><br>Nee. Minnesota meldt hem af met een knieblessure; hij miste ook de laatste drie wedstrijden.</p>
<p><strong>Hoeveel NBA-wedstrijden zijn er vannacht?</strong><br>Vier, met acht ploegen.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    alles = content + content2 + content3
    tekst = re.sub(r"<[^>]+>", " ", alles)
    woorden = len(tekst.split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", woorden, "woorden |", len(TIPS), "tips")
    assert len(TITEL) <= 60 and 120 <= len(SAMENVATTING) <= 155, (len(TITEL), len(SAMENVATTING))
    assert 1100 <= woorden <= 2300, woorden
    assert KIJK, "geen Bet365-stream in het schema: KIJK-zin aanpassen"
    assert len(TIPS) == len(TOP3) == 3 and [q(float(t["odds"])) for t in TIPS] == [k[6] for k in TOP3]
    assert all(1.40 <= float(t["odds"]) <= 1.80 and t["bookmaker"] == "toto" for t in TIPS)
    for t in TIPS:
        h, u = t["wedstrijd"].split(" vs. ")
        p = next(x for x in PROGRAMMA if x[1] == h and x[2] == u)
        assert t["tijd_nl"] == p[0] and float(t["odds"]) == LIJNEN[t["lijn"]], t
        assert t["lijn"][0] in (h, u) and t["lijn"][1] in t["tip"]
    assert all(a < b for a, b in WIZ_REEKS) and WIZ_GEM == "17,0"
    assert CHA_GEM == "97,0"
    assert 112 - 106 >= 6 and 110 - 105 < 6 and 116 - 106 >= 6
    assert 115 - 108 >= 7 and 112 - 106 < 7 and 118 - 106 >= 7
    assert 110 - 106 >= 4 and 108 - 105 < 4 and 112 - 102 >= 4
    assert COMBI == "3,58"
    assert round(100 / 1.51) == 66 and round(100 / 1.50) == 67 and round(100 / 1.58) == 63
    assert content2.count("<strong>De tip:") == 3
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert "<h2" not in alles and "<h4" not in alles and "betcity" not in alles.lower() and "espn" not in alles.lower()
    assert not re.search(r"\bunder\b", alles, re.I) and alles.count(BET365) == 1
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/") or href == BET365, href
    print("dry run ok – niets gepubliceerd")
