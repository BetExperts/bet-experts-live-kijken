# -*- coding: utf-8 -*-
"""Los artikel: de 3 beste NBA-wedtips van vannacht, vrijdag 13 op zaterdag 14 november 2026 (9 wedstrijden).
Zelfde opzet als nba_vannacht_2026_11_13.py, deelkaart via og_kaarten/nhl_top3.py met OG_LIGA = "nba".
Feiten nagelopen op 13-11-2026 (±16:00 NL): ESPN-scoreboard 13-11, teamschema's 2026/27, wedstrijdpagina's
(event-id's 401909296-401909304: blessurelijst, leiders, thuis/uit-balans) en box scores van de laatste drie duels
(Curry speelde woensdagnacht in Houston maar 6 minuten en is nu out; Porzingis en Moody misten alle drie; Powell (Bulls)
miste de laatste twee; Wembanyama, Fox en Castle speelden alle drie; Avdija, Lillard, Holiday, Clingan alle drie; Morant out).
- Geen back-to-backs vannacht (niemand speelde donderdagnacht).
- Odds: TOTO, vrijdag 13-11 rond 16:00 NL (wedstrijdpagina's). Tips: Handicap - Winnaar (inc OT). Geen unders.
- Resultaten van eerdere NBA-tips niet noemen (eigenaar 30-10).
  python3 specials/nba_vannacht_2026_11_14.py   (alleen dry run, publiceert niets)"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel
import bet365_streams as B365

SLUG = "nba-voorspellingen-vannacht-14-november-2026"
RUBRIEK = "672293e14a76d88272bc0b61"   # Basketball
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
TITEL = "NBA voorspellingen vannacht: 3 beste wedtips (14 november)"
SAMENVATTING = ("De 3 beste NBA-wedtips van vannacht: Spurs -8,5 tegen Golden State zonder Curry, Blazers -7,5 in "
                "Sacramento en Hawks -4,5 in Chicago.")
DATUM = "2026-11-14T00:00:00.000Z"     # eerste wedstrijd: 01:00 NL
BET365 = "https://www.bet-experts.nl/go/bet365"

OG_LIGA, OG_SPORT = "nba", "Basketbal"
TOP3 = [("02:00", "Bulls", "chi", "Hawks", "atl", "Hawks -4,5", "1,59", "68%"),
        ("03:30", "Spurs", "sa", "Warriors", "gs", "Spurs -8,5", "1,48", "71%"),
        ("04:00", "Kings", "sac", "Trail Blazers", "por", "Blazers -7,5", "1,54", "69%")]
OG_EYEBROW_DATUM = "14 november"
OG_GISTEREN = ("Wedstrijden", "9")
OG_RECHTS = "Incl. verlenging · TOTO"

L = {"regels": '<a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels van de NBA</a>',
     "handicap": '<a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">hoe handicap wedden werkt</a>',
     "kans": '<a href="/nieuws/kans-berekenen-uit-odds-impliciete-kans">hoe je een odd omrekent naar een kans</a>',
     "toto": '<a href="/bookmakers/toto">TOTO</a>',
     "hub": '<a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>'}

# (tijd NL, thuis, uit, odd thuis, odd uit)  TOTO 'Winnaar' (inclusief verlenging)
PROGRAMMA = [
    ("01:00", "Indiana Pacers", "New York Knicks", 3.10, 1.38),
    ("01:00", "Orlando Magic", "Milwaukee Bucks", 1.26, 3.90),
    ("02:00", "Miami Heat", "Cleveland Cavaliers", 1.73, 2.12),
    ("02:00", "Chicago Bulls", "Atlanta Hawks", 3.25, 1.35),
    ("02:00", "New Orleans Pelicans", "Memphis Grizzlies", 2.33, 1.61),
    ("02:30", "Houston Rockets", "Utah Jazz", 1.06, 9.00),
    ("03:30", "San Antonio Spurs", "Golden State Warriors", 1.14, 5.75),
    ("04:00", "Sacramento Kings", "Portland Trail Blazers", 4.75, 1.19),
    ("04:30", "LA Clippers", "Oklahoma City Thunder", 3.30, 1.33),
]
LIJNEN = {("San Antonio Spurs", "-8,5"): 1.48, ("San Antonio Spurs", "-12,5"): 1.89, ("San Antonio Spurs", "-6,5"): 1.35,
          ("Portland Trail Blazers", "-7,5"): 1.54, ("Portland Trail Blazers", "-10,5"): 1.89, ("Portland Trail Blazers", "-5,5"): 1.39,
          ("Atlanta Hawks", "-4,5"): 1.59, ("Atlanta Hawks", "-7,5"): 1.91, ("Atlanta Hawks", "-2,5"): 1.43}

KIJK = B365.kijk_zin("Basketball", DATUM[:10], [(p[1], p[2]) for p in PROGRAMMA], link="/bookmakers/bet365")
KIJK = (KIJK + " ") if KIJK else ""
MARKT_H = "Handicap - Winnaar, inclusief verlenging"

SPURS_REEKS = [(119, 97), (112, 111), (124, 109), (125, 103), (122, 96), (124, 119)]   # zes zeges op rij (ploeg eerst)
KINGS_THUIS = [(115, 100)]   # enige zege was uit in Dallas; thuis 0-6
BULLS_REEKS = [(127, 133), (111, 125), (107, 126), (105, 135), (121, 127), (119, 124)]   # zes nederlagen op rij


def q(x):
    return f"{x:.2f}".replace(".", ",")


def gem(xs):
    return f"{sum(xs) / len(xs):.1f}".replace(".", ",")


SPURS_GEM = gem([a - b for a, b in SPURS_REEKS])
BULLS_GEM = gem([b - a for a, b in BULLS_REEKS])
COMBI = q(1.48 * 1.54 * 1.59)

TIPS = [
    {"wedstrijd": "Chicago Bulls vs. Atlanta Hawks", "competitie": "NBA", "speeltijd_utc": "2026-11-14T01:00:00Z",
     "tijd_nl": "02:00", "tip": "Atlanta Hawks -4,5 (incl. verlenging)", "odds": "1.59", "bookmaker": "toto", "markt": MARKT_H,
     "lijn": ("Atlanta Hawks", "-4,5"),
     "veld": "Bulls – Hawks (02:00): Atlanta Hawks -4,5 (incl. verlenging)",
     "analyse": f"Chicago staat op 1-9, verloor alle vier de thuiswedstrijden en krijgt 128,8 punten per wedstrijd tegen; topscorer Norman Powell miste de laatste twee duels. Atlanta won uit vier van de zes wedstrijden."},
    {"wedstrijd": "San Antonio Spurs vs. Golden State Warriors", "competitie": "NBA", "speeltijd_utc": "2026-11-14T02:30:00Z",
     "tijd_nl": "03:30", "tip": "San Antonio Spurs -8,5 (incl. verlenging)", "odds": "1.48", "bookmaker": "toto", "markt": MARKT_H,
     "lijn": ("San Antonio Spurs", "-8,5"),
     "veld": "Spurs – Warriors (03:30): San Antonio Spurs -8,5 (incl. verlenging)",
     "analyse": f"San Antonio won zes keer op rij (gemiddeld met {SPURS_GEM} punten verschil) en heeft met +11,2 het beste puntensaldo van de nacht; Golden State mist Stephen Curry, Kristaps Porziņģis en Moses Moody."},
    {"wedstrijd": "Sacramento Kings vs. Portland Trail Blazers", "competitie": "NBA", "speeltijd_utc": "2026-11-14T03:00:00Z",
     "tijd_nl": "04:00", "tip": "Portland Trail Blazers -7,5 (incl. verlenging)", "odds": "1.54", "bookmaker": "toto", "markt": MARKT_H,
     "lijn": ("Portland Trail Blazers", "-7,5"),
     "veld": "Kings – Trail Blazers (04:00): Portland Trail Blazers -7,5 (incl. verlenging)",
     "analyse": "Sacramento staat op 1-10 en verloor alle zes de thuiswedstrijden; Portland won uit vijf van de zes wedstrijden en versloeg deze week twee keer Oklahoma City."},
]

content = f"""<p><strong>Onze 3 beste NBA-wedtips van vannacht: San Antonio Spurs wint met minstens negen punten verschil van een Golden State Warriors zonder Stephen Curry (-8,5, odd 1,48), Portland Trail Blazers wint met minstens acht punten verschil in Sacramento (-7,5, odd 1,54) en Atlanta Hawks wint met minstens vijf punten verschil in Chicago (-4,5, odd 1,59). Alle drie bij TOTO en alle drie inclusief verlenging. Er staan negen NBA-wedstrijden op het programma, van 01:00 tot 04:30 uur Nederlandse tijd.</strong></p>
<p>De topper van de nacht van vrijdag 13 op zaterdag 14 november is San Antonio Spurs (10-2) tegen Golden State Warriors (8-4), om 03:30 uur. Maar die wedstrijd verandert sterk door het nieuws van het afgelopen etmaal: Stephen Curry viel woensdagnacht in Houston na zes minuten uit en staat nu als out gemeld. Wij liepen per wedstrijd de vorm, de blessurelijst, de box scores van de laatste wedstrijden en de cijfers na, en kozen de drie tips waar onze inschatting hoger ligt dan de kans die de odd aangeeft. Alle drie zijn het handicaps op de uitploeg of thuisfavoriet, met een lagere lijn dan de hoofdlijn: zo houden we marge. Een tip blijft natuurlijk een inschatting; zet alleen in wat je kunt missen.</p>
<p><strong>Kijken?</strong> {KIJK}Met NBA League Pass, de betaalde dienst van de competitie, zie je alle NBA-wedstrijden. Meer opties lees je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk de NBA vannacht live</strong></a></p>
<h3><strong>De 3 beste NBA-wedtips van vannacht</strong></h3>
{tabel(["Wedstrijd", "Tip", "Markt", "Odd", "Onze kans"], [
    ("Bulls – Hawks (02:00)", "<strong>Atlanta Hawks -4,5</strong>", "Handicap, incl. verlenging", "1,59", "68% (odd: 63%)"),
    ("Spurs – Warriors (03:30)", "<strong>San Antonio Spurs -8,5</strong>", "Handicap, incl. verlenging", "1,48", "71% (odd: 68%)"),
    ("Kings – Trail Blazers (04:00)", "<strong>Portland Trail Blazers -7,5</strong>", "Handicap, incl. verlenging", "1,54", "69% (odd: 65%)"),
])}
<p><em>Odds bij {L['toto']}, gelezen op vrijdag 13 november rond 16:00. Odds kunnen tot de start nog veranderen. Alle drie de tips gelden inclusief een eventuele verlenging. Het zijn losse tips: wie ze combineert, krijgt een totale odd van {COMBI}, maar dan moeten ze alle drie goed zijn. Achter "odd" staat de kans die de odd zelf aangeeft; lees {L['kans']}.</em></p>
<h3><strong>Het NBA-programma van vannacht (Nederlandse tijd)</strong></h3>
{tabel(["Tijd", "Wedstrijd", "Winnaar (thuis – uit)"], [
    (f"<strong>{t}</strong>", f"{h} – {u}", f"{q(oh)} – {q(ou)}") for t, h, u, oh, ou in PROGRAMMA
])}
<p><em>Alle wedstrijden beginnen in de nacht van vrijdag op zaterdag. De odds in deze tabel gelden voor de markt Winnaar, inclusief verlenging. Geen enkele ploeg speelt vannacht een back-to-back.</em></p>"""

content2 = f"""<h3><strong>Tip 1: San Antonio Spurs – Golden State Warriors (03:30)</strong></h3>
<p><strong>De tip: San Antonio Spurs -8,5, odd 1,48. Markt: Handicap - Winnaar, inclusief verlenging.</strong> San Antonio moet met minstens negen punten verschil winnen. Rekenvoorbeeld: bij 120-111 is de tip goed, bij 118-110 is de tip verloren.</p>
<p><strong>Waarom deze markt?</strong> Een zege van San Antonio staat op 1,14: te laag voor een losse tip. De hoofdlijn ligt op -12,5 (1,89). Met -8,5 hebben we vier punten extra marge en blijft de odd speelbaar.</p>
<p><strong>Vorm en cijfers.</strong> San Antonio staat op 10-2, is koploper in het westen en won de laatste zes wedstrijden, gemiddeld met {SPURS_GEM} punten verschil. Met +11,2 punten per wedstrijd heeft de ploeg het beste puntensaldo van alle ploegen die vannacht spelen. Golden State staat op 8-4 en won vijf keer op rij voordat het woensdagnacht in Houston met 108-115 verloor. Uit won Golden State maar twee van de vijf wedstrijden.</p>
<p><strong>Blessures.</strong> Dit is het belangrijkste nieuws: <strong>Stephen Curry</strong> (27,8 punten per wedstrijd) speelde in Houston maar zes minuten en staat nu als out gemeld. Ook Kristaps Porziņģis en Moses Moody ontbreken; zij speelden de laatste drie wedstrijden al niet. Bij San Antonio zijn De'Aaron Fox en Devin Vassell twijfelachtig. Fox speelde de laatste drie wedstrijden wel, Vassell miste de laatste twee. Tobias Harris is out.</p>
<p><strong>Spelers om op te letten.</strong> Victor Wembanyama scoort 30,2 punten en pakt 11,7 rebounds per wedstrijd. Bij Golden State moet het zonder Curry komen van Draymond Green, die 7,5 assists geeft.</p>
<p><strong>Onze voorspelling: San Antonio Spurs – Golden State Warriors 121-106.</strong> De odd van 1,48 gaat uit van 68%, wij schatten de kans op 71%. Het risico: zonder Curry kan Golden State een andere, meer verdedigende wedstrijd spelen, en San Antonio verloor thuis al twee van de zes wedstrijden. Liever veiliger? Spurs -6,5 staat op 1,35.</p>
<h3><strong>Tip 2: Sacramento Kings – Portland Trail Blazers (04:00)</strong></h3>
<p><strong>De tip: Portland Trail Blazers -7,5, odd 1,54. Markt: Handicap - Winnaar, inclusief verlenging.</strong> Portland moet met minstens acht punten verschil winnen. Rekenvoorbeeld: bij 108-118 is de tip goed, bij 110-117 is de tip verloren.</p>
<p><strong>Waarom deze markt?</strong> Een zege van Portland staat op 1,19 en de hoofdlijn ligt op -10,5 (1,89). Met -7,5 hebben we drie punten extra marge.</p>
<p><strong>Vorm en cijfers.</strong> Sacramento staat op 1-10 en verloor alle zes de thuiswedstrijden. De ploeg krijgt 121,0 punten per wedstrijd tegen en heeft een puntensaldo van -12,7. Portland staat op 8-3, won uit vijf van de zes wedstrijden en versloeg deze week twee keer Oklahoma City (123-103 en 118-108). Portland scoort gemiddeld 119,5 punten.</p>
<p><strong>Blessures.</strong> Portland mist Ja Morant, Shaedon Sharpe en Vít Krejčí, maar won de laatste wedstrijden ook zonder hen; Deni Avdija, Damian Lillard en Jrue Holiday speelden de laatste drie duels allemaal. Sacramento mist Maxime Raynaud en Ben Simmons.</p>
<p><strong>Spelers om op te letten.</strong> Deni Avdija scoort 23,0 punten met 6,5 assists en Donovan Clingan pakt 10,5 rebounds. Bij Sacramento is rookie Darius Acuff Jr. (26,2 punten) de grote man, en Domantas Sabonis pakt 13,3 rebounds.</p>
<p><strong>Onze voorspelling: Sacramento Kings – Portland Trail Blazers 109-121.</strong> De odd van 1,54 gaat uit van 65%, wij schatten de kans op 69%. Het risico: Acuff kan een wedstrijd alleen openbreken, en een paar late punten kunnen het verschil onder de acht brengen. Liever veiliger? Blazers -5,5 staat op 1,39.</p>
<h3><strong>Tip 3: Chicago Bulls – Atlanta Hawks (02:00)</strong></h3>
<p><strong>De tip: Atlanta Hawks -4,5, odd 1,59. Markt: Handicap - Winnaar, inclusief verlenging.</strong> Atlanta moet met minstens vijf punten verschil winnen. Rekenvoorbeeld: bij 120-126 is de tip goed, bij 120-124 is de tip verloren.</p>
<p><strong>Waarom deze markt?</strong> Een zege van Atlanta staat op 1,35 en de hoofdlijn ligt op -7,5 (1,91). Met -4,5 hebben we drie punten extra marge.</p>
<p><strong>Vorm en cijfers.</strong> Chicago staat op 1-9, verloor de laatste zes wedstrijden (gemiddeld met {BULLS_GEM} punten verschil) en won nog geen enkele thuiswedstrijd. De Bulls krijgen 128,8 punten per wedstrijd tegen: het meeste van alle ploegen die vannacht spelen. Atlanta staat op 7-5 en won uit vier van de zes wedstrijden.</p>
<p><strong>Blessures.</strong> Bij Chicago is topscorer Norman Powell (19,2 punten) twijfelachtig; hij miste de laatste twee wedstrijden. Ook Caleb Wilson en Tobe Awaka zijn out. Bij Atlanta ontbreken onder meer Mouhamed Gueye en Asa Newell, maar Nickeil Alexander-Walker en Jalen Johnson speelden de laatste duels wel.</p>
<p><strong>Spelers om op te letten.</strong> Nickeil Alexander-Walker scoort 21,9 punten en Jalen Johnson pakt 8,6 rebounds met 7,2 assists. Bij Chicago geeft Josh Giddey 8,3 assists.</p>
<p><strong>Onze voorspelling: Chicago Bulls – Atlanta Hawks 117-127.</strong> De odd van 1,59 gaat uit van 63%, wij schatten de kans op 68%. Het risico: in wedstrijden met veel punten kan een achterstand snel kleiner worden. Liever veiliger? Hawks -2,5 staat op 1,43.</p>
<h3><strong>De andere NBA-wedstrijden van vannacht</strong></h3>
<p><strong>Pacers – Knicks (01:00)</strong>: Indiana mist Tyrese Haliburton en won thuis maar één van de vijf wedstrijden; New York is favoriet (1,38). <strong>Magic – Bucks (01:00)</strong>: Milwaukee staat op 1-11 en verloor alle vijf de uitwedstrijden, maar Orlando won thuis nog niets en mist Paolo Banchero; Orlando wint staat op 1,26. <strong>Heat – Cavaliers (02:00)</strong>: Cleveland mist Evan Mobley, bij Miami is Giannis Antetokounmpo twijfelachtig. <strong>Pelicans – Grizzlies (02:00)</strong>: Memphis won alle vijf de uitwedstrijden, maar mist Zach Edey. <strong>Rockets – Jazz (02:30)</strong>: Houston is met 1,06 grote favoriet tegen een Utah dat op 1-11 staat. <strong>Clippers – Thunder (04:30)</strong>: Oklahoma City verloor twee keer in Portland en mist nog altijd Chet Holmgren; de Clippers missen Brandon Ingram en Bradley Beal. Bij deze duels zien wij geen duidelijke voorsprong in de odds.</p>"""

content3 = f"""<h3><strong>Handicap bij de NBA: hoe werkt het?</strong></h3>
<p>Bij de NBA eindigt een wedstrijd nooit in een gelijkspel: bij een gelijke stand na 48 minuten volgt een verlenging van vijf minuten. Onze tips van vannacht zijn alle drie <strong>inclusief verlenging</strong>.</p>
{tabel(["Markt", "Wat telt mee", "Voorbeeld vannacht"], [
    ("<strong>Winnaar</strong>", "Eindstand inclusief verlenging. Er is altijd een winnaar.", "Spurs winnen van Golden State: 1,14"),
    ("<strong>Handicap</strong>", "Eindstand inclusief verlenging, met een puntenachterstand voor de favoriet.", "Spurs -8,5: 1,48"),
    ("<strong>Hoofdlijn</strong>", "De handicap waarbij beide kanten ongeveer even waarschijnlijk zijn.", "Spurs -12,5: 1,89"),
])}
<p>Een min-handicap trekt punten af van de favoriet. Bij Spurs -8,5 haal je in gedachten 8,5 punten weg bij San Antonio: wint de ploeg met negen punten of meer, dan is de tip goed. Een half punt zorgt ervoor dat je inzet nooit wordt teruggestort. Hoe lager de handicap, hoe groter de kans en hoe lager de odd. Lees ook {L['handicap']} en {L['regels']}.</p>
<p>Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit. Twijfel je? Lees <a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>. Alle basketbaltips vind je op onze pagina {L['hub']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wat zijn de beste NBA-wedtips van vannacht?</strong><br>San Antonio Spurs -8,5 tegen Golden State Warriors (1,48), Portland Trail Blazers -7,5 bij Sacramento Kings (1,54) en Atlanta Hawks -4,5 bij Chicago Bulls (1,59), alle odds bij TOTO. Zet alleen in wat je kunt missen.</p>
<p><strong>Speelt Stephen Curry vannacht?</strong><br>Nee. Golden State meldt hem als out; hij speelde woensdagnacht in Houston maar zes minuten.</p>
<p><strong>Hoe laat is Spurs – Warriors?</strong><br>Om 03:30 uur Nederlandse tijd, in de nacht van vrijdag op zaterdag.</p>
<p><strong>Hoe laat beginnen de NBA-wedstrijden vannacht?</strong><br>De eerste twee om 01:00 uur, de laatste (Clippers – Thunder) om 04:30 uur Nederlandse tijd.</p>
<p><strong>Gelden de tips inclusief verlenging?</strong><br>Ja, alle drie. Een verlenging telt mee voor de eindstand, dus ook voor het puntenverschil bij de handicaps.</p>
<p><strong>Hoeveel NBA-wedstrijden zijn er vannacht?</strong><br>Negen, met achttien ploegen.</p>
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
    assert len(TIPS) == len(TOP3) == 3 and sorted(q(float(t["odds"])) for t in TIPS) == sorted(k[6] for k in TOP3)
    assert all(1.40 <= float(t["odds"]) <= 1.80 and t["bookmaker"] == "toto" for t in TIPS)
    for t in TIPS:
        h, u = t["wedstrijd"].split(" vs. ")
        p = next(x for x in PROGRAMMA if x[1] == h and x[2] == u)
        assert t["tijd_nl"] == p[0] and float(t["odds"]) == LIJNEN[t["lijn"]], t
    assert all(a > b for a, b in SPURS_REEKS) and all(a < b for a, b in BULLS_REEKS)
    assert 120 - 111 >= 9 and 118 - 110 < 9 and 121 - 106 >= 9
    assert 118 - 108 >= 8 and 117 - 110 < 8 and 121 - 109 >= 8
    assert 126 - 120 >= 5 and 124 - 120 < 5 and 127 - 117 >= 5
    assert COMBI == "3,62"
    assert round(100 / 1.48) == 68 and round(100 / 1.54) == 65 and round(100 / 1.59) == 63
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert "<h2" not in alles and "<h4" not in alles and "betcity" not in alles.lower() and "espn" not in alles.lower()
    assert not re.search(r"\bunder\b", alles, re.I) and alles.count(BET365) == 1
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/") or href == BET365, href
    print("dry run ok – niets gepubliceerd")
