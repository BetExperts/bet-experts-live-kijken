# -*- coding: utf-8 -*-
"""Los artikel: de 3 beste NBA-wedtips van vannacht, dinsdag 10 op woensdag 11 november 2026 (6 wedstrijden).
Zelfde opzet als nba_vannacht_2026_11_10.py, deelkaart via og_kaarten/nhl_top3.py met OG_LIGA = "nba".
Feiten nagelopen op 10-11-2026 (±18:00 NL): ESPN-scoreboard 9/10-11, teamschema's 2026/27 (alleen competitie),
wedstrijdpagina's (event-id's 401909960-401909965: blessurelijst, gemiddelden) en box scores van de laatste zes duels
(wie speelde er echt: Holmgren/Jalen Williams/Wallace misten alle zes, Morant de laatste vijf, Hart de laatste twee).
- Back-to-back: alleen Phoenix (maandagnacht 96-122 tegen San Antonio).
- Odds: TOTO, dinsdag 10-11 rond 18:00 NL (wedstrijdpagina's). Tips: Handicap - Winnaar (inc OT) en
  Aantal punten (inc OT, alleen over). Geen unders.
- Resultaten van eerdere NBA-tips niet noemen (eigenaar 30-10).
  python3 specials/nba_vannacht_2026_11_11.py   (alleen dry run, publiceert niets)"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel
import bet365_streams as B365

SLUG = "nba-voorspellingen-vannacht-11-november-2026"
RUBRIEK = "672293e14a76d88272bc0b61"   # Basketball
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
TITEL = "NBA voorspellingen vannacht: 3 beste wedtips (11 november)"
SAMENVATTING = ("De 3 beste NBA-wedtips van vannacht: Knicks -10,5 tegen Milwaukee, Thunder +2,5 in Portland en "
                "over 220,5 punten bij Kings – Magic.")
DATUM = "2026-11-11T00:30:00.000Z"     # eerste wedstrijd: 01:30 NL
BET365 = "https://www.bet-experts.nl/go/bet365"

# kaart (og_kaarten/nhl_top3.py met OG_LIGA): (tijd, thuis, abbr, uit, abbr, tip, odd, onze kans)
OG_LIGA, OG_SPORT = "nba", "Basketbal"
TOP3 = [("01:30", "Knicks", "ny", "Bucks", "mil", "Knicks -10,5", "1,46", "71%"),
        ("04:00", "Kings", "sac", "Magic", "orl", "Over 220,5", "1,69", "65%"),
        ("05:00", "Trail Blazers", "por", "Thunder", "okc", "Thunder +2,5", "1,58", "67%")]
OG_EYEBROW_DATUM = "11 november"
OG_GISTEREN = ("Wedstrijden", "6")
OG_RECHTS = "Incl. verlenging · TOTO"

L = {"regels": '<a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels van de NBA</a>',
     "handicap": '<a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">hoe handicap wedden werkt</a>',
     "moneyline": '<a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">de money line</a>',
     "kans": '<a href="/nieuws/kans-berekenen-uit-odds-impliciete-kans">hoe je een odd omrekent naar een kans</a>',
     "toto": '<a href="/bookmakers/toto">TOTO</a>',
     "hub": '<a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>',
     "vorige": '<a href="/nieuws/nba-voorspellingen-vannacht-10-november-2026">de NBA-tips van gisteren</a>'}

# (tijd NL, thuis, uit, odd thuis, odd uit, back-to-back)  TOTO 'Winnaar' (inclusief verlenging)
PROGRAMMA = [
    ("01:30", "New York Knicks", "Milwaukee Bucks", 1.09, 7.50, "-"),
    ("02:00", "Philadelphia 76ers", "Boston Celtics", 2.00, 1.82, "-"),
    ("03:00", "Phoenix Suns", "Los Angeles Clippers", 1.60, 2.34, "Suns"),
    ("03:00", "Utah Jazz", "Miami Heat", 3.90, 1.26, "-"),
    ("04:00", "Sacramento Kings", "Orlando Magic", 2.85, 1.43, "-"),
    ("05:00", "Portland Trail Blazers", "Oklahoma City Thunder", 2.07, 1.76, "-"),
]
# TOTO-wedstrijdpagina's: (ploeg of 'Over', lijn) -> odd
LIJNEN = {("New York Knicks", "-10,5"): 1.46, ("New York Knicks", "-12,5"): 1.61, ("New York Knicks", "-15,5"): 1.93,
          ("Oklahoma City Thunder", "+2,5"): 1.58, ("Oklahoma City Thunder", "+4,5"): 1.44, ("Oklahoma City Thunder", "-1,5"): 1.85,
          ("Over", "220,5"): 1.69, ("Over", "223,5"): 1.91, ("Over", "218,5"): 1.57}

KIJK = B365.kijk_zin("Basketball", DATUM[:10], [(p[1], p[2] if p[2] != "Los Angeles Clippers" else "LA Clippers") for p in PROGRAMMA],
                     link="/bookmakers/bet365")
KIJK = (KIJK + " ") if KIJK else ""

MARKT_H = "Handicap - Winnaar, inclusief verlenging"
MARKT_T = "Aantal punten, inclusief verlenging"

# Vorm (reguliere competitie, uitslagen ploeg eerst)
BUCKS_REEKS = [(100, 132), (111, 136), (100, 112), (102, 109), (107, 121), (97, 117)]   # zes nederlagen op rij
KNICKS_REEKS = [(103, 90), (135, 105), (109, 97)]                                        # drie zeges op rij
THUNDER_REEKS = [(117, 112), (124, 116), (128, 97), (114, 75)]                           # vier zeges op rij
KINGS_TOT = [217, 248, 235, 233, 252, 241, 215, 219, 233, 222]
MAGIC_TOT = [257, 208, 213, 228, 235, 205, 197, 221, 245]


def q(x):
    return f"{x:.2f}".replace(".", ",")


def gem(xs):
    return f"{sum(xs) / len(xs):.1f}".replace(".", ",")


BUCKS_GEM = gem([b - a for a, b in BUCKS_REEKS])
KINGS_GEM, MAGIC_GEM = gem(KINGS_TOT), gem(MAGIC_TOT)
OVER_N = sum(t > 220.5 for t in KINGS_TOT + MAGIC_TOT)
COMBI = q(1.46 * 1.69 * 1.58)

TIPS = [
    {"wedstrijd": "New York Knicks vs. Milwaukee Bucks", "competitie": "NBA", "speeltijd_utc": "2026-11-11T00:30:00Z",
     "tijd_nl": "01:30", "tip": "New York Knicks -10,5 (incl. verlenging)", "odds": "1.46", "bookmaker": "toto", "markt": MARKT_H,
     "lijn": ("New York Knicks", "-10,5"),
     "veld": "Knicks – Bucks (01:30): New York Knicks -10,5 (incl. verlenging)",
     "analyse": f"Milwaukee verloor zes keer op rij, gemiddeld met {BUCKS_GEM} punten verschil, won geen enkele uitwedstrijd en krijgt 121,6 punten per wedstrijd tegen; New York won de laatste drie duels met 13, 30 en 12 punten verschil."},
    {"wedstrijd": "Sacramento Kings vs. Orlando Magic", "competitie": "NBA", "speeltijd_utc": "2026-11-11T03:00:00Z",
     "tijd_nl": "04:00", "tip": "Over 220,5 punten (incl. verlenging)", "odds": "1.69", "bookmaker": "toto", "markt": MARKT_T,
     "lijn": ("Over", "220,5"),
     "veld": "Kings – Magic (04:00): over 220,5 punten (incl. verlenging)",
     "analyse": f"Sacramento krijgt 122,4 punten per wedstrijd tegen, het meeste van alle ploegen die vannacht spelen; {OVER_N} van de 19 wedstrijden van beide ploegen samen eindigden boven 220,5 punten."},
    {"wedstrijd": "Portland Trail Blazers vs. Oklahoma City Thunder", "competitie": "NBA", "speeltijd_utc": "2026-11-11T04:00:00Z",
     "tijd_nl": "05:00", "tip": "Oklahoma City Thunder +2,5 (incl. verlenging)", "odds": "1.58", "bookmaker": "toto", "markt": MARKT_H,
     "lijn": ("Oklahoma City Thunder", "+2,5"),
     "veld": "Trail Blazers – Thunder (05:00): Oklahoma City Thunder +2,5 (incl. verlenging)",
     "analyse": "Oklahoma City won vier keer op rij en heeft op Boston na het beste puntensaldo van de avond (+8,0), ook zonder Holmgren en Jalen Williams; Portland verloor thuis twee van de drie duels en mist Ja Morant."},
]

content = f"""<p><strong>Onze 3 beste NBA-wedtips van vannacht: New York Knicks wint met minstens elf punten verschil van Milwaukee Bucks (-10,5, odd 1,46), Sacramento Kings – Orlando Magic eindigt boven de 220,5 punten (odd 1,69) en Oklahoma City Thunder verliest in Portland niet met drie punten of meer (+2,5, odd 1,58). Alle drie bij TOTO en alle drie inclusief verlenging. Er staan zes NBA-wedstrijden op het programma, van 01:30 tot 05:00 uur Nederlandse tijd.</strong></p>
<p>Het is een kleine NBA-nacht van dinsdag 10 op woensdag 11 november, maar met een echte topper: Philadelphia 76ers (9-2) tegen Boston Celtics (8-2), de nummers één en twee van de Eastern Conference. Alleen Phoenix speelt een back-to-back. Wij liepen voor elk duel de vorm, de blessurelijst, de box scores van de laatste wedstrijden en de cijfers na, en kozen de drie tips waar onze eigen inschatting hoger ligt dan de kans die de odd aangeeft. Daarbij zitten twee handicaps en één puntentotaal. Een tip blijft natuurlijk een inschatting; zet alleen in wat je kunt missen.</p>
<p><strong>Kijken?</strong> {KIJK}Met NBA League Pass, de betaalde dienst van de competitie, zie je alle NBA-wedstrijden. Meer opties lees je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk de NBA vannacht live</strong></a></p>
<h3><strong>De 3 beste NBA-wedtips van vannacht</strong></h3>
{tabel(["Wedstrijd", "Tip", "Markt", "Odd", "Onze kans"], [
    ("Knicks – Bucks (01:30)", "<strong>New York Knicks -10,5</strong>", "Handicap, incl. verlenging", "1,46", "71% (odd: 68%)"),
    ("Kings – Magic (04:00)", "<strong>Over 220,5 punten</strong>", "Aantal punten, incl. verlenging", "1,69", "65% (odd: 59%)"),
    ("Trail Blazers – Thunder (05:00)", "<strong>Oklahoma City Thunder +2,5</strong>", "Handicap, incl. verlenging", "1,58", "67% (odd: 63%)"),
])}
<p><em>Odds bij {L['toto']}, gelezen op dinsdag 10 november rond 18:00. Odds kunnen tot de start nog veranderen. Alle drie de tips gelden inclusief een eventuele verlenging. Het zijn losse tips: wie ze combineert, krijgt een totale odd van {COMBI}, maar dan moeten ze alle drie goed zijn. Achter "odd" staat de kans die de odd zelf aangeeft; lees {L['kans']}.</em></p>
<h3><strong>Het NBA-programma van vannacht (Nederlandse tijd)</strong></h3>
{tabel(["Tijd", "Wedstrijd", "Winnaar (thuis – uit)", "Back-to-back"], [
    (f"<strong>{t}</strong>", f"{h} – {u}", f"{q(oh)} – {q(ou)}", b2b) for t, h, u, oh, ou, b2b in PROGRAMMA
])}
<p><em>Alle wedstrijden beginnen in de nacht van dinsdag op woensdag. De odds in deze tabel gelden voor de markt Winnaar, inclusief verlenging. Oklahoma City en Portland spelen de nacht erna opnieuw tegen elkaar, ook in Portland.</em></p>"""

content2 = f"""<h3><strong>Tip 1: New York Knicks – Milwaukee Bucks (01:30)</strong></h3>
<p><strong>De tip: New York Knicks -10,5, odd 1,46. Markt: Handicap - Winnaar, inclusief verlenging.</strong> New York moet met minstens elf punten verschil winnen. Rekenvoorbeeld: bij 112-101 is de tip goed, bij 110-100 is de tip verloren.</p>
<p><strong>Waarom deze markt?</strong> Een zege van New York staat op 1,09: veel te laag voor een losse tip. De hoofdlijn ligt op -15,5 (1,93). Met -10,5 hebben we vijf punten extra marge en blijft de odd speelbaar.</p>
<p><strong>Vorm en cijfers.</strong> Milwaukee staat op 1-9 en verloor de laatste zes wedstrijden, gemiddeld met {BUCKS_GEM} punten verschil: 100-132 tegen Houston, 111-136 tegen Cleveland, 100-112 in Minnesota, twee keer tegen Boston (102-109 en 97-117) en 107-121 tegen Toronto. Alle vier de uitwedstrijden gingen verloren, drie daarvan met elf punten of meer. Milwaukee scoort 108,4 punten en krijgt er 121,6 tegen. New York staat op 5-4 en won de laatste drie wedstrijden: 103-90 van Brooklyn, 135-105 van Chicago en zaterdag 109-97 in Cleveland, dus met 13, 30 en 12 punten verschil. De Knicks scoren 109,9 punten en krijgen er 104,2 tegen.</p>
<p><strong>Blessures.</strong> Bij New York is Josh Hart (enkel) twijfelachtig; hij miste ook de laatste twee wedstrijden, die allebei ruim werden gewonnen. Bij Milwaukee is topscorer Tyler Herro (knie, 21,4 punten) twijfelachtig. Hij speelde zondag nog 27 minuten.</p>
<p><strong>Spelers om op te letten.</strong> Jalen Brunson scoort 26,2 punten per wedstrijd en Karl-Anthony Towns pakt 13,6 rebounds; in Cleveland maakten ze samen 60 punten. Bij Milwaukee scoorde Kyle Kuzma zondag 27 punten tegen Boston.</p>
<p><strong>Onze voorspelling: New York Knicks – Milwaukee Bucks 118-103.</strong> De odd van 1,46 gaat uit van 68%, wij schatten de kans op 71%. Het risico: New York won thuis maar drie van de vijf wedstrijden, en verloor daar van Philadelphia en Orlando. Durf je meer? Knicks -12,5 staat op 1,61.</p>
<h3><strong>Tip 2: Sacramento Kings – Orlando Magic (04:00)</strong></h3>
<p><strong>De tip: over 220,5 punten, odd 1,69. Markt: Aantal punten, inclusief verlenging.</strong> Beide ploegen moeten samen minstens 221 punten maken. Rekenvoorbeeld: bij 112-109 (221 punten) is de tip goed, bij 108-112 (220 punten) is de tip verloren. Een eventuele verlenging telt mee.</p>
<p><strong>Waarom deze markt?</strong> Orlando wint staat op 1,43, maar in een duel tussen twee ploegen met samen drie zeges uit negentien wedstrijden kiezen we liever niet voor een winnaar. De verdedigingen zijn het zwakke punt, en dat maakt het puntentotaal interessanter. De hoofdlijn ligt op 223,5 (1,91); met 220,5 hebben we drie punten extra marge.</p>
<p><strong>Vorm en cijfers.</strong> Sacramento staat op 1-9, verloor alle vijf de thuiswedstrijden en krijgt 122,4 punten per wedstrijd tegen: het meeste van alle ploegen die vannacht spelen. De wedstrijden van Sacramento eindigden gemiddeld op {KINGS_GEM} punten, die van Orlando op {MAGIC_GEM}. Van de negentien wedstrijden van beide ploegen samen eindigden er {OVER_N} boven 220,5 punten: zeven van de tien bij Sacramento en vijf van de negen bij Orlando. Orlando staat op 2-7, verloor de laatste vier wedstrijden en gaf zaterdag nog 126 punten weg in Golden State (119-126).</p>
<p><strong>Blessures.</strong> Sacramento mist Maxime Raynaud (knie) en Ben Simmons (achillespees); Domantas Sabonis (knie, 14,6 rebounds) en Keegan Murray (pols) zijn twijfelachtig. Orlando mist Paolo Banchero (enkel), Jalen Suggs en Jonathan Isaac (allebei knie), Noah Penda (hamstring) en Izaiyah Nelson (enkel). Banchero en Suggs speelden de laatste zes wedstrijden al niet; hun afwezigheid zit dus al in de cijfers hierboven.</p>
<p><strong>Spelers om op te letten.</strong> Rookie Darius Acuff Jr. scoort 25,9 punten met 7,4 assists voor Sacramento en maakte zondag 32 punten tegen Miami. Bij Orlando scoort Franz Wagner 20,8 punten met 8,8 assists; in Golden State maakte hij er 30.</p>
<p><strong>Onze voorspelling: Sacramento Kings – Orlando Magic 110-117 (227 punten).</strong> De odd van 1,69 gaat uit van 59%, wij schatten de kans op 65%. Het risico: zonder Sabonis en met een uitgedund Orlando kan het aanvallend stroef gaan; vier van de negen wedstrijden van Orlando bleven onder de 214 punten. Liever veiliger? Over 218,5 staat op 1,57.</p>
<h3><strong>Tip 3: Portland Trail Blazers – Oklahoma City Thunder (05:00)</strong></h3>
<p><strong>De tip: Oklahoma City Thunder +2,5, odd 1,58. Markt: Handicap - Winnaar, inclusief verlenging.</strong> Oklahoma City mag niet met drie punten of meer verliezen. Rekenvoorbeeld: wint Oklahoma City, of verliest het met 110-112, dan is de tip goed; bij 108-111 is de tip verloren.</p>
<p><strong>Waarom deze markt?</strong> Een zege van Oklahoma City staat op 1,76 en de hoofdlijn ligt op Thunder -1,5 (1,85). Met +2,5 heb je ook een kleine nederlaag nog gedekt.</p>
<p><strong>Vorm en cijfers.</strong> Oklahoma City staat op 8-2, won de laatste vier wedstrijden (117-112 en 124-116 tegen Cleveland, 128-97 in Memphis en 114-75 tegen Washington) en heeft met +8,0 punten per wedstrijd op Boston (+10,7) na het beste puntensaldo van alle ploegen die vannacht spelen. Dat lukte zonder Chet Holmgren, Jalen Williams en Cason Wallace: zij speelden de laatste zes wedstrijden geen minuut. Portland staat op 6-3 en won vijf van de zes uitwedstrijden, maar thuis maar één van de drie. De laatste twee wedstrijden gingen verloren: 118-124 bij de Lakers en 103-125 tegen San Antonio.</p>
<p><strong>Blessures.</strong> Portland mist Ja Morant (hamstring), die de laatste vijf wedstrijden niet speelde, plus Shaedon Sharpe (knie) en Vít Krejčí (enkel). Oklahoma City mist Holmgren (knie), Jalen Williams (been), Wallace (schouder), Jaylin Williams (rug) en Thomas Sorber (knie).</p>
<p><strong>Spelers om op te letten.</strong> Shai Gilgeous-Alexander scoort 29,9 punten per wedstrijd en Isaiah Hartenstein pakt 10,1 rebounds. Bij Portland scoort Deni Avdija 22,3 punten met 6,3 assists en pakt Donovan Clingan 10,0 rebounds.</p>
<p><strong>Onze voorspelling: Portland Trail Blazers – Oklahoma City Thunder 109-114.</strong> De odd van 1,58 gaat uit van 63%, wij schatten de kans op 67%. Het risico: Portland is een sterke ploeg met Avdija, Damian Lillard en Jrue Holiday, en Oklahoma City heeft een korte rotatie. Liever veiliger? Thunder +4,5 staat op 1,44.</p>
<h3><strong>De andere NBA-wedstrijden van vannacht</strong></h3>
<p><strong>76ers – Celtics (02:00)</strong>: de topper van de nacht. Philadelphia won thuis vier van de vijf wedstrijden en heeft met Tyrese Maxey (26,9 punten), Joel Embiid en LeBron James (6,7 assists) veel ervaring in de basis. Boston won de laatste drie wedstrijden, onder meer met 119-80 in Charlotte, heeft geen blessures en Jayson Tatum scoort 27,1 punten met 7,8 assists. Met 2,00 tegen 1,82 is dit een muntworp; daar zetten wij niets op. <strong>Suns – Clippers (03:00)</strong>: Phoenix verloor maandagnacht met 96-122 van San Antonio en speelt dus een back-to-back. De Clippers staan op 2-7, verloren alle vier de uitduels en missen Brandon Ingram (achillespees) en Bradley Beal (knie). Devin Booker scoort 26,0 punten. Phoenix wint staat op 1,60; de vermoeidheid na de back-to-back houdt ons hier weg. <strong>Jazz – Heat (03:00)</strong>: Utah verloor acht keer op rij en mist Keyonte George (enkel, 21,1 punten), Jaren Jackson Jr. en Jusuf Nurkić; Lauri Markkanen (pols) is twijfelachtig. Miami is favoriet (1,26), maar Giannis Antetokounmpo (pols, 27,5 punten en 12,8 rebounds) is twijfelachtig. Zolang niet duidelijk is of hij speelt, blijven wij hier weg.</p>"""

content3 = f"""<h3><strong>Winnaar, handicap of puntentotaal: let op de markt</strong></h3>
<p>Bij de NBA eindigt een wedstrijd nooit in een gelijkspel: bij een gelijke stand na 48 minuten volgt een verlenging van vijf minuten. Onze tips van vannacht zijn alle drie <strong>inclusief verlenging</strong>.</p>
{tabel(["Markt", "Wat telt mee", "Voorbeeld vannacht"], [
    ("<strong>Winnaar</strong>", "Eindstand inclusief verlenging. Er is altijd een winnaar.", "Thunder winnen in Portland: 1,76"),
    ("<strong>Handicap</strong>", "Eindstand inclusief verlenging, met een puntenvoorsprong of -achterstand voor één ploeg.", "Knicks -10,5: 1,46"),
    ("<strong>Aantal punten</strong>", "Alle punten van beide ploegen, inclusief verlenging.", "Kings – Magic over 220,5: 1,69"),
    ("<strong>Uitslag (zonder verlenging)</strong>", "Alleen de stand na 48 minuten. Gelijkspel is een uitkomst.", "Knicks winnen na 48 minuten: 1,10"),
])}
<p>Een min-handicap trekt punten af van de favoriet, een plus-handicap telt punten op bij de ploeg die je kiest. Bij Thunder +2,5 tel je in gedachten 2,5 punten op bij Oklahoma City: verliest de ploeg met één of twee punten, dan is de tip toch goed. Een half punt zorgt ervoor dat je inzet nooit wordt teruggestort. Bij een puntentotaal tellen ook de punten in een verlenging mee, en een verlenging levert al snel twintig punten extra op. Lees ook {L['handicap']}, wat {L['moneyline']} is en {L['regels']}. Wil je terugkijken? Lees dan {L['vorige']}.</p>
<p>Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit. Twijfel je? Lees <a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>. Alle basketbaltips vind je op onze pagina {L['hub']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wat zijn de beste NBA-wedtips van vannacht?</strong><br>New York Knicks -10,5 tegen Milwaukee Bucks (1,46), over 220,5 punten bij Sacramento Kings – Orlando Magic (1,69) en Oklahoma City Thunder +2,5 bij Portland Trail Blazers (1,58), alle odds bij TOTO. Zet alleen in wat je kunt missen.</p>
<p><strong>Gelden de tips inclusief verlenging?</strong><br>Ja, alle drie. Een verlenging telt mee voor de eindstand, dus ook voor het puntenverschil bij de handicaps en voor het puntentotaal.</p>
<p><strong>Hoe laat beginnen de NBA-wedstrijden vannacht?</strong><br>Knicks – Bucks begint om 01:30 uur Nederlandse tijd en 76ers – Celtics om 02:00 uur. Suns – Clippers en Jazz – Heat volgen om 03:00 uur, Kings – Magic om 04:00 uur en Trail Blazers – Thunder om 05:00 uur.</p>
<p><strong>Speelt Giannis Antetokounmpo vannacht?</strong><br>Dat is nog onzeker. Miami meldt hem als twijfelachtig met een polsblessure voor de wedstrijd in Utah. Zondag speelde hij nog 34 minuten in Sacramento en maakte hij 29 punten.</p>
<p><strong>Welke ploeg speelt vannacht een back-to-back?</strong><br>Alleen de Phoenix Suns: zij verloren maandagnacht met 96-122 van San Antonio en spelen nu thuis tegen de Clippers.</p>
<p><strong>Hoeveel NBA-wedstrijden zijn er vannacht?</strong><br>Zes, met twaalf ploegen.</p>
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
    assert all("incl. verlenging" in t["tip"] and "incl. verlenging" in t["veld"] and "inclusief verlenging" in t["markt"] for t in TIPS)
    for t in TIPS:
        h, u = t["wedstrijd"].split(" vs. ")
        p = next(x for x in PROGRAMMA if x[1] == h and x[2] == u)
        assert t["tijd_nl"] == p[0] and float(t["odds"]) == LIJNEN[t["lijn"]], t
        assert (t["lijn"][0] in (h, u) or t["lijn"][0] == "Over") and t["lijn"][1] in t["tip"]
    assert len(PROGRAMMA) == 6 and 12 == len({x for p in PROGRAMMA for x in p[1:3]})
    # reeksen en gemiddelden
    assert all(a < b for a, b in BUCKS_REEKS) and BUCKS_GEM == "18,3"
    assert [a - b for a, b in KNICKS_REEKS] == [13, 30, 12] and all(a > b for a, b in THUNDER_REEKS)
    assert KINGS_GEM == "231,5" and MAGIC_GEM == "223,2" and OVER_N == 12
    assert sum(t > 220.5 for t in KINGS_TOT) == 7 and sum(t > 220.5 for t in MAGIC_TOT) == 5
    assert sum(t < 214 for t in MAGIC_TOT) == 4
    assert sum(b - a >= 11 for a, b in [(116, 128), (116, 127), (100, 112), (102, 109)]) == 3
    # rekenvoorbeelden en voorspellingen kloppen met de lijnen
    assert 112 - 101 >= 11 and 110 - 100 < 11 and 118 - 103 >= 11
    assert 112 + 109 > 220.5 and 108 + 112 < 220.5 and 110 + 117 > 220.5 and 110 + 117 == 227
    assert 112 - 110 < 2.5 and 111 - 108 > 2.5 and 114 > 109
    assert COMBI == "3,90"
    assert content2.count("<strong>De tip:") == 3 and content2.count("inclusief verlenging.</strong>") == 3
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert "<h2" not in alles and "<h4" not in alles and "betcity" not in alles.lower() and "espn" not in alles.lower()
    assert content.startswith("<p><strong>Onze 3 beste NBA-wedtips") and "<p><strong>Kijken?</strong>" in content
    assert not any(re.search(r"minder dan|\bunder\b", t["tip"], re.I) for t in TIPS) and not re.search(r"\bunder\b", alles, re.I)
    assert alles.count(BET365) == 1
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/") or href == BET365, href
    print("dry run ok – niets gepubliceerd")
