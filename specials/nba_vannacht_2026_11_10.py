# -*- coding: utf-8 -*-
"""Los artikel: de 3 beste NBA-wedtips van vannacht, maandag 9 op dinsdag 10 november 2026 (8 wedstrijden).
Zelfde opzet als nba_vannacht_2026_11_08.py, deelkaart via og_kaarten/nhl_top3.py met OG_LIGA = "nba".
Feiten nagelopen op 9-11-2026 (middag NL): ESPN-scoreboard 8/9-11, teamschema's 2026/27 (alleen competitie),
wedstrijdpagina's (event-id's 401909952-401909959: blessurelijst, gemiddelden, onderlinge duels).
- Back-to-backs: Lakers, Pistons, Mavericks en Pelicans speelden zondagnacht ook.
- Odds: TOTO, maandag 9-11 rond 16:00 NL (wedstrijdpagina's). 'Winnaar' (incl. verlenging) stond bij de meeste
  duels nog dicht; daarom in het programma de markt 'Uitslag (excl. verlenging)'. Tips: Handicap - Winnaar, incl. verlenging.
- Resultaten van eerdere NBA-tips niet noemen (eigenaar 30-10). Geen unders.
  python3 specials/nba_vannacht_2026_11_10.py   (alleen dry run, publiceert niets)"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel
import bet365_streams as B365

SLUG = "nba-voorspellingen-vannacht-10-november-2026"
RUBRIEK = "672293e14a76d88272bc0b61"   # Basketball
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
TITEL = "NBA voorspellingen vannacht: 3 beste wedtips (10 november)"
SAMENVATTING = ("De 3 beste NBA-wedtips van vannacht: Cavaliers -6,5 in Charlotte, Spurs -4,5 in Phoenix en "
                "Warriors -6,5 tegen New Orleans. Odds bij TOTO.")
DATUM = "2026-11-10T00:00:00.000Z"     # eerste wedstrijden: 01:00 NL
BET365 = "https://www.bet-experts.nl/go/bet365"

# kaart (og_kaarten/nhl_top3.py met OG_LIGA): (tijd, thuis, abbr, uit, abbr, tip, odd, onze kans)
OG_LIGA, OG_SPORT = "nba", "Basketbal"
TOP3 = [("01:00", "Hornets", "cha", "Cavaliers", "cle", "Cavaliers -6,5", "1,64", "68%"),
        ("03:00", "Suns", "phx", "Spurs", "sa", "Spurs -4,5", "1,42", "76%"),
        ("04:00", "Warriors", "gs", "Pelicans", "no", "Warriors -6,5", "1,58", "67%")]
OG_EYEBROW_DATUM = "10 november"
OG_GISTEREN = ("Wedstrijden", "8")
OG_RECHTS = "Incl. verlenging · TOTO"

L = {"regels": '<a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels van de NBA</a>',
     "handicap": '<a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">hoe handicap wedden werkt</a>',
     "moneyline": '<a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">de money line</a>',
     "toto": '<a href="/bookmakers/toto">TOTO</a>',
     "hub": '<a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>',
     "vorige": '<a href="/nieuws/nba-voorspellingen-vannacht-8-november-2026">de vorige NBA-tips</a>'}

# (tijd NL, thuis, uit, odd thuis, odd uit, back-to-back)  TOTO 'Uitslag (excl. verlenging)', gelijkspel apart
PROGRAMMA = [
    ("01:00", "Atlanta Hawks", "Los Angeles Lakers", 1.90, 1.98, "Lakers"),
    ("01:00", "Charlotte Hornets", "Cleveland Cavaliers", 3.75, 1.29, "-"),
    ("01:00", "Detroit Pistons", "Washington Wizards", 1.21, 4.75, "Pistons"),
    ("01:30", "Toronto Raptors", "Memphis Grizzlies", 1.68, 2.26, "-"),
    ("02:00", "Dallas Mavericks", "Indiana Pacers", 1.65, 2.32, "Mavericks"),
    ("02:30", "Houston Rockets", "Denver Nuggets", 1.30, 3.65, "-"),
    ("03:00", "Phoenix Suns", "San Antonio Spurs", 3.95, 1.27, "-"),
    ("04:00", "Golden State Warriors", "New Orleans Pelicans", 1.27, 4.00, "Pelicans"),
]
# TOTO 'Handicap - Winnaar (inc OT)' op de wedstrijdpagina's: (ploeg, lijn) -> odd
HCP = {("Cleveland Cavaliers", "-6,5"): 1.64, ("Cleveland Cavaliers", "-8,5"): 1.89,
       ("San Antonio Spurs", "-4,5"): 1.42, ("San Antonio Spurs", "-8,5"): 1.79,
       ("Golden State Warriors", "-6,5"): 1.58, ("Golden State Warriors", "-4,5"): 1.41}

KIJK = B365.kijk_zin("Basketball", DATUM[:10], [(p[1], p[2]) for p in PROGRAMMA], link="/bookmakers/bet365")
KIJK = (KIJK + " ") if KIJK else ""

MARKT_H = "Handicap - Winnaar, inclusief verlenging"


def q(x):
    return f"{x:.2f}".replace(".", ",")


def kort(n):
    return n.split()[-1] if n.split()[-1] not in ("Blazers",) else "Trail Blazers"


TIPS = [
    {"wedstrijd": "Charlotte Hornets vs. Cleveland Cavaliers", "competitie": "NBA", "speeltijd_utc": "2026-11-10T00:00:00Z",
     "tijd_nl": "01:00", "tip": "Cleveland Cavaliers -6,5 (incl. verlenging)", "odds": "1.64", "bookmaker": "toto", "markt": MARKT_H,
     "lijn": ("Cleveland Cavaliers", "-6,5"),
     "veld": "Hornets – Cavaliers (01:00): Cleveland Cavaliers -6,5 (incl. verlenging)",
     "analyse": "Charlotte verloor zes keer op rij, gemiddeld met 18,5 punten verschil, scoort met 96,3 punten het minst van iedereen vannacht en mist Brandon Miller, Kon Knueppel en Dennis Schröder."},
    {"wedstrijd": "Phoenix Suns vs. San Antonio Spurs", "competitie": "NBA", "speeltijd_utc": "2026-11-10T02:00:00Z",
     "tijd_nl": "03:00", "tip": "San Antonio Spurs -4,5 (incl. verlenging)", "odds": "1.42", "bookmaker": "toto", "markt": MARKT_H,
     "lijn": ("San Antonio Spurs", "-4,5"),
     "veld": "Suns – Spurs (03:00): San Antonio Spurs -4,5 (incl. verlenging)",
     "analyse": "San Antonio won acht keer op rij en alle vier de uitwedstrijden, gemiddeld met 14,8 punten verschil; Phoenix krijgt 118,6 punten per wedstrijd tegen en verloor alle drie de uitduels."},
    {"wedstrijd": "Golden State Warriors vs. New Orleans Pelicans", "competitie": "NBA", "speeltijd_utc": "2026-11-10T03:00:00Z",
     "tijd_nl": "04:00", "tip": "Golden State Warriors -6,5 (incl. verlenging)", "odds": "1.58", "bookmaker": "toto", "markt": MARKT_H,
     "lijn": ("Golden State Warriors", "-6,5"),
     "veld": "Warriors – Pelicans (04:00): Golden State Warriors -6,5 (incl. verlenging)",
     "analyse": "Golden State won zeven keer op rij en thuis vijf van de zes duels; New Orleans speelt een back-to-back na 123-139 bij de Clippers en krijgt 120,8 punten per wedstrijd tegen."},
]

content = f"""<p><strong>Onze 3 beste NBA-wedtips van vannacht: Cleveland Cavaliers wint met minstens zeven punten verschil in Charlotte (-6,5, odd 1,64), San Antonio Spurs wint met minstens vijf punten verschil in Phoenix (-4,5, odd 1,42) en Golden State Warriors wint met minstens zeven punten verschil van New Orleans Pelicans (-6,5, odd 1,58). Alle drie bij TOTO en alle drie inclusief verlenging. Er staan acht NBA-wedstrijden op het programma, van 01:00 tot 04:00 uur Nederlandse tijd.</strong></p>
<p>In de nacht van maandag 9 op dinsdag 10 november spelen vier ploegen een back-to-back: de Lakers, Pistons, Mavericks en Pelicans stonden zondagnacht ook op het veld. Bij de Lakers ontbreekt bovendien Luka Dončić (rug), die dit seizoen 40,1 punten per wedstrijd maakt. Wij liepen voor elk duel de vorm, de blessurelijst en de cijfers na, en kozen de drie tips waar onze eigen inschatting hoger ligt dan de kans die de odd aangeeft. Alle drie zijn het handicaps: bij deze grote favorieten levert gewoon winnen te weinig op, terwijl een kleinere handicap dan de hoofdlijn nog genoeg marge geeft. Een tip blijft natuurlijk een inschatting; zet alleen in wat je kunt missen.</p>
<p><strong>Kijken?</strong> {KIJK}Met NBA League Pass, de betaalde dienst van de competitie, zie je alle NBA-wedstrijden. Meer opties lees je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk de NBA vannacht live</strong></a></p>
<h3><strong>De 3 beste NBA-wedtips van vannacht</strong></h3>
{tabel(["Wedstrijd", "Tip", "Markt", "Odd", "Onze kans"], [
    ("Hornets – Cavaliers (01:00)", "<strong>Cleveland Cavaliers -6,5</strong>", "Handicap, incl. verlenging", "1,64", "68% (odd: 61%)"),
    ("Suns – Spurs (03:00)", "<strong>San Antonio Spurs -4,5</strong>", "Handicap, incl. verlenging", "1,42", "76% (odd: 70%)"),
    ("Warriors – Pelicans (04:00)", "<strong>Golden State Warriors -6,5</strong>", "Handicap, incl. verlenging", "1,58", "67% (odd: 63%)"),
])}
<p><em>Odds bij {L['toto']}, gelezen op maandag 9 november rond 16:00. Odds kunnen tot de start nog veranderen. Alle drie de tips gelden inclusief een eventuele verlenging. Het zijn losse tips: wie ze combineert, krijgt een totale odd van 3,68, maar dan moeten ze alle drie goed zijn.</em></p>
<h3><strong>Het NBA-programma van vannacht (Nederlandse tijd)</strong></h3>
{tabel(["Tijd", "Wedstrijd", "Uitslag na 48 min (thuis – uit)", "Back-to-back"], [
    (f"<strong>{t}</strong>", f"{h} – {u}", f"{q(oh)} – {q(ou)}", b2b) for t, h, u, oh, ou, b2b in PROGRAMMA
])}
<p><em>Alle wedstrijden beginnen in de nacht van maandag op dinsdag. De odds in deze tabel gelden voor de uitslag na 48 minuten, zonder verlenging; een gelijke stand is dan een aparte uitkomst (bij TOTO rond 14,50 tot 17,00). Bij de meeste duels was de markt Winnaar inclusief verlenging maandagmiddag nog niet geopend.</em></p>"""

content2 = f"""<h3><strong>Tip 1: Charlotte Hornets – Cleveland Cavaliers (01:00)</strong></h3>
<p><strong>De tip: Cleveland Cavaliers -6,5, odd 1,64. Markt: Handicap - Winnaar, inclusief verlenging.</strong> Cleveland moet met minstens zeven punten verschil winnen. Rekenvoorbeeld: bij 102-110 is de tip goed, bij 105-110 is de tip verloren.</p>
<p><strong>Waarom deze markt?</strong> Cleveland wint na 48 minuten staat op 1,29, te laag voor een losse tip. De hoofdlijn ligt op -8,5 (1,89); met -6,5 hebben we twee punten extra marge.</p>
<p><strong>Vorm en cijfers.</strong> Charlotte staat op 3-7 en verloor de laatste zes wedstrijden, gemiddeld met 18,5 punten verschil: 89-97 en 91-124 tegen Detroit, 79-95 in Washington, 104-109 tegen Philadelphia, 104-114 in Brooklyn en vrijdag 80-119 tegen Boston. Met 96,3 punten per wedstrijd scoort Charlotte het minst van alle ploegen die vannacht spelen, en het krijgt er 110,2 tegen. Cleveland staat op 5-5 en scoort 117,0 punten per wedstrijd. De ploeg verloor zaterdag thuis van New York (97-109) en won uit maar één keer, maar dat was wel met 136-111 in Milwaukee.</p>
<p><strong>Blessures.</strong> Charlotte mist zijn topscorer Brandon Miller (lies, 20,6 punten), Kon Knueppel en Grant Williams (allebei hamstring) en Dennis Schröder (hamstring, 4,9 assists). Rebounder Moussa Diabaté (dij) is twijfelachtig. Cleveland mist Sam Merrill (elleboog) en Jaylon Tyson (enkel); Jarrett Allen (knie) is twijfelachtig.</p>
<p><strong>Spelers om op te letten.</strong> Donovan Mitchell scoort 24,0 punten per wedstrijd, James Harden geeft 5,8 assists en Evan Mobley pakt 8,1 rebounds. Bij Charlotte moet het zonder Miller en Schröder van de bank komen; juist daarom haperde de aanval de laatste weken zo.</p>
<p><strong>Onze voorspelling: Charlotte Hornets – Cleveland Cavaliers 100-114.</strong> De odd van 1,64 gaat uit van 61%, wij schatten de kans op 68%. Het risico: Cleveland is uit wisselvallig (1-3) en speelt zonder twee rotatiespelers. Durf je meer? De hoofdlijn, -8,5, staat op 1,89.</p>
<h3><strong>Tip 2: Phoenix Suns – San Antonio Spurs (03:00)</strong></h3>
<p><strong>De tip: San Antonio Spurs -4,5, odd 1,42. Markt: Handicap - Winnaar, inclusief verlenging.</strong> San Antonio moet met minstens vijf punten verschil winnen. Rekenvoorbeeld: bij 108-114 is de tip goed, bij 110-113 is de tip verloren.</p>
<p><strong>Waarom deze markt?</strong> San Antonio wint na 48 minuten staat op 1,27. Met -4,5 krijgen we een speelbare odd en houden we ruime marge ten opzichte van de hoofdlijn (-9,5).</p>
<p><strong>Vorm en cijfers.</strong> San Antonio staat op 8-2: na thuisnederlagen tegen Oklahoma City en Houston in de eerste week won de ploeg acht keer op rij. Alle vier de uitwedstrijden werden gewonnen, gemiddeld met 14,8 punten verschil: 122-106 in Dallas, 117-111 in Utah, 124-109 in Sacramento en 125-103 in Portland. San Antonio scoort 118,4 punten en krijgt er 108,1 tegen. Phoenix staat op 3-5, verloor alle drie de uitduels en krijgt 118,6 punten per wedstrijd tegen. Thuis won Phoenix wel de laatste twee wedstrijden: 117-104 van Orlando en 102-99 van Houston.</p>
<p><strong>Blessures.</strong> Phoenix mist Mark Williams (schouder) en Jordan Goodwin (kuit). San Antonio mist Tobias Harris (kuit) en Jayden Quaintance (knie); Devin Vassell (lies) is twijfelachtig. Beide ploegen speelden voor het laatst in de nacht van zaterdag op zondag en hebben dus twee dagen rust gehad.</p>
<p><strong>Spelers om op te letten.</strong> Victor Wembanyama scoort 29,1 punten en pakt 12,0 rebounds per wedstrijd; De'Aaron Fox geeft 5,9 assists. Bij Phoenix scoort Devin Booker 25,2 punten met 4,9 assists en pakt Miles Bridges 8,1 rebounds.</p>
<p><strong>Onze voorspelling: Phoenix Suns – San Antonio Spurs 109-120.</strong> De odd van 1,42 gaat uit van 70%, wij schatten de kans op 76%. Het risico: Phoenix is thuis in vorm en Booker kan in zijn eentje een wedstrijd openhouden. Durf je meer? Spurs -8,5 staat op 1,79.</p>
<h3><strong>Tip 3: Golden State Warriors – New Orleans Pelicans (04:00)</strong></h3>
<p><strong>De tip: Golden State Warriors -6,5, odd 1,58. Markt: Handicap - Winnaar, inclusief verlenging.</strong> Golden State moet met minstens zeven punten verschil winnen. Rekenvoorbeeld: bij 118-110 is de tip goed, bij 115-111 is de tip verloren.</p>
<p><strong>Waarom deze markt?</strong> Golden State wint na 48 minuten staat op 1,27. Met -6,5 zitten we ruim onder de hoofdlijn, die rond de -10 ligt.</p>
<p><strong>Vorm en cijfers.</strong> Golden State staat op 7-3 en won de laatste zeven wedstrijden. Thuis won de ploeg vijf van de zes duels, met marges van 17, 12, 3, 20 en 7 punten; alleen Memphis won in San Francisco (108-111). Golden State scoort 118,6 punten per wedstrijd. New Orleans staat op 4-6, won uit maar één van de vier wedstrijden en krijgt met 120,8 punten per wedstrijd het meeste tegen van alle ploegen die vannacht spelen. Zondagnacht verloor New Orleans met 123-139 bij de Clippers: dit is de tweede wedstrijd in twee nachten.</p>
<p><strong>Blessures.</strong> Golden State mist Jimmy Butler (knie), Kristaps Porziņģis (ziek), Moses Moody (knie) en Will Richard (duim); Gui Santos (knie) is twijfelachtig. New Orleans mist Yves Missi (knie).</p>
<p><strong>Spelers om op te letten.</strong> Stephen Curry scoort 31,2 punten per wedstrijd en Draymond Green geeft 7,8 assists. Bij New Orleans scoort Zion Williamson 21,0 punten, geeft Dejounte Murray 5,0 assists en pakt Derik Queen 7,2 rebounds.</p>
<p><strong>Onze voorspelling: Golden State Warriors – New Orleans Pelicans 121-111.</strong> De odd van 1,58 gaat uit van 63%, wij schatten de kans op 67%. Het risico: Golden State mist vier rotatiespelers, en New Orleans scoort met 120,5 punten per wedstrijd genoeg om lang mee te komen. Liever veiliger? Warriors -4,5 staat op 1,41.</p>
<h3><strong>De andere NBA-wedstrijden van vannacht</strong></h3>
<p><strong>Hawks – Lakers (01:00)</strong>: Atlanta won vier keer op rij. De Lakers staan op 9-2, maar missen Luka Dončić en spelen na de 121-116-zege in Detroit een back-to-back. Met 1,90 tegen 1,98 is dit een muntworp; daar zetten wij niets op. <strong>Pistons – Wizards (01:00)</strong>: Detroit speelt een back-to-back na de nederlaag tegen de Lakers en mist Jalen Duren en Isaiah Joe. Washington verloor drie keer op rij, onder meer met 75-114 in Oklahoma City, en Anthony Davis (enkel) is twijfelachtig. <strong>Raptors – Grizzlies (01:30)</strong>: Toronto mist Kawhi Leonard, en Scottie Barnes (23,5 punten) en Immanuel Quickley zijn twijfelachtig. Memphis won alle vier de uitduels, maar verloor de laatste drie thuiswedstrijden. <strong>Mavericks – Pacers (02:00)</strong>: Dallas won zondag 130-93 van Brooklyn en speelt dus een back-to-back, zonder Dereck Lively II. Cooper Flagg scoort 24,0 punten met 7,0 assists. Indiana staat op 3-7 en mist Tyrese Haliburton, Ben Sheppard en Johnny Furphy; Dallas -3,5 staat op 1,92. <strong>Rockets – Nuggets (02:30)</strong>: bij Denver zijn Jamal Murray, Aaron Gordon, DeMar DeRozan, Christian Braun en Cameron Johnson allemaal twijfelachtig. Houston verloor de laatste twee wedstrijden en mist Clint Capela en Steven Adams. Zolang niet duidelijk is wie bij Denver speelt, blijven wij hier weg.</p>"""

content3 = f"""<h3><strong>Winnaar of handicap: let op de markt</strong></h3>
<p>Bij de NBA eindigt een wedstrijd nooit in een gelijkspel: bij een gelijke stand na 48 minuten volgt een verlenging van vijf minuten. Onze tips van vannacht zijn alle drie <strong>inclusief verlenging</strong>.</p>
{tabel(["Markt", "Wat telt mee", "Voorbeeld vannacht"], [
    ("<strong>Winnaar</strong>", "Eindstand inclusief verlenging. Er is altijd een winnaar.", "Hawks winnen van de Lakers: 1,86"),
    ("<strong>Handicap</strong>", "Eindstand inclusief verlenging, met een puntenvoorsprong of -achterstand voor één ploeg.", "Cavaliers -6,5: 1,64"),
    ("<strong>Totaal punten</strong>", "Alle punten van beide ploegen, inclusief verlenging.", "Suns – Spurs over 227,5: 1,91"),
    ("<strong>Uitslag (zonder verlenging)</strong>", "Alleen de stand na 48 minuten. Gelijkspel is een uitkomst.", "Spurs winnen na 48 minuten: 1,27"),
])}
<p>Bij een handicap van -6,5 telt Cleveland er in gedachten 6,5 punten af: wint de ploeg met 7 punten of meer, dan is de tip goed. Een half punt zorgt ervoor dat je inzet nooit wordt teruggestort. In de markt zonder verlenging is een gelijke stand na 48 minuten een aparte uitkomst (bij Suns – Spurs 16,00): wie dan op een van beide ploegen inzet, verliest. Lees ook {L['handicap']}, wat {L['moneyline']} is en {L['regels']}. Wil je terugkijken? Lees dan {L['vorige']}.</p>
<p>Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit. Twijfel je? Lees <a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>. Alle basketbaltips vind je op onze pagina {L['hub']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wat zijn de beste NBA-wedtips van vannacht?</strong><br>Cleveland Cavaliers -6,5 bij Charlotte Hornets (1,64), San Antonio Spurs -4,5 bij Phoenix Suns (1,42) en Golden State Warriors -6,5 tegen New Orleans Pelicans (1,58), alle odds bij TOTO. Zet alleen in wat je kunt missen.</p>
<p><strong>Gelden de tips inclusief verlenging?</strong><br>Ja, alle drie. Een verlenging telt mee voor de eindstand, dus ook voor het puntenverschil bij de handicaps.</p>
<p><strong>Hoe laat beginnen de NBA-wedstrijden vannacht?</strong><br>Hawks – Lakers, Hornets – Cavaliers en Pistons – Wizards beginnen om 01:00 uur Nederlandse tijd. Daarna volgen Raptors – Grizzlies om 01:30 uur, Mavericks – Pacers om 02:00 uur, Rockets – Nuggets om 02:30 uur, Suns – Spurs om 03:00 uur en Warriors – Pelicans om 04:00 uur.</p>
<p><strong>Speelt Luka Dončić vannacht?</strong><br>Nee. De Lakers melden hem af met een rugblessure voor de wedstrijd in Atlanta.</p>
<p><strong>Welke ploegen spelen vannacht een back-to-back?</strong><br>De Los Angeles Lakers, Detroit Pistons, Dallas Mavericks en New Orleans Pelicans. Zij speelden zondagnacht ook.</p>
<p><strong>Hoeveel NBA-wedstrijden zijn er vannacht?</strong><br>Acht, met zestien ploegen.</p>
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
        assert t["tijd_nl"] == p[0] and float(t["odds"]) == HCP[t["lijn"]], t
        assert t["lijn"][0] in (h, u) and t["lijn"][1] in t["tip"]
    assert len(PROGRAMMA) == 8 and 16 == len({x for p in PROGRAMMA for x in p[1:3]})
    # rekenvoorbeelden en voorspellingen kloppen met de lijnen
    assert 110 - 102 >= 7 and 110 - 105 < 7 and 114 - 100 >= 7
    assert 114 - 108 >= 5 and 113 - 110 < 5 and 120 - 109 >= 5
    assert 118 - 110 >= 7 and 115 - 111 < 7 and 121 - 111 >= 7
    assert abs(1.64 * 1.42 * 1.58 - 3.68) < 0.01
    assert (8 + 16 + 5 + 33 + 10 + 39) / 6 == 18.5 and round((16 + 6 + 15 + 22) / 4, 1) == 14.8
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
