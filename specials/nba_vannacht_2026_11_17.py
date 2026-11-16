# -*- coding: utf-8 -*-
"""Los artikel: de 3 beste NBA-wedtips van vannacht, maandag 16 op dinsdag 17 november 2026 (8 wedstrijden).
Opzet als nba_vannacht_2026_11_14.py, deelkaart via og_kaarten/nhl_top3.py met OG_LIGA = "nba".

Eigen analyse (nieuw in dit artikel, staat in geen enkel ander stuk): twee tabellen die we zelf hebben berekend
uit alle uitslagen van dit seizoen - (1) het rustschema: wie speelde zondagnacht en zit dus in een back-to-back,
(2) het thuissaldo van de thuisploeg tegen het uitsaldo van de uitploeg, per wedstrijd, met het verschil.
Daar komen de drie tips uit: de drie duels met het grootste gat.

Feiten nagelopen op 16-11-2026 (±21:00 NL): officiele NBA-dagprogramma's van 13, 14, 15 en 16 november (US-datum),
teamschema's met alle uitslagen 2026/27, blessurelijsten en topscorers per wedstrijd. Rust bepaald op US-speeldatum,
niet op de UTC-datum van de kalender (die schuift een dag op bij avondwedstrijden).
- Back-to-back vannacht: Boston, Philadelphia, Houston, Washington en Phoenix (speelden zondag 15-11).
  Twee dagen rust: Orlando, Golden State en Portland. De rest speelde zaterdag.
- Odds: 711 (Kambi sevelevnl, publieke offering-API), maandag 16-11 rond 21:00 NL. Markt: Handicap - inclusief
  verlenging. Geen unders (Jasper 13-11). Resultaten van eerdere NBA-tips niet noemen (Jasper 30-10).
- Afgewezen tips na controle van de marges per wedstrijd: Cleveland -5,5 (slechts 3 van 7 thuiszeges waren ruimer),
  Denver -5,5 (1 van 4 thuisduels), Golden State -1,5 (2 van 6 uitduels). Die staan er dus NIET in.
  python3 specials/nba_vannacht_2026_11_17.py   (alleen dry run, publiceert niets)
  kaart: ../superodd-agent/.venv/bin/python og_kaarten/nhl_top3.py nba_vannacht_2026_11_17
  publiceren: set -a; . ../superodd-agent/.env; set +a; ../superodd-agent/.venv/bin/python specials/concept_publiceer.py nba_vannacht_2026_11_17 --live
  daarna: ... specials/nba_vannacht_2026_11_17.py --velden"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel
import bet365_streams as B365

SLUG = "nba-voorspellingen-vannacht-17-november-2026"
RUBRIEK = "672293e14a76d88272bc0b61"   # Basketball
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BOOKMAKER_711 = "66a8a87062108480763b7309"
TITEL = "NBA voorspellingen vannacht: 3 beste wedtips (17 november)"
SAMENVATTING = ("De 3 beste NBA-wedtips van vannacht: Memphis -1,5 in Washington, Boston -4,5 tegen Orlando en "
                "Philadelphia -2,5 in Brooklyn. Met odds en tijden.")
DATUM = "2026-11-17T00:00:00.000Z"     # eerste wedstrijd: 01:00 NL
BET365 = "https://www.bet-experts.nl/go/bet365"

OG_LIGA, OG_SPORT = "nba", "Basketbal"
OG_EYEBROW_DATUM = "17 november"
OG_GISTEREN = ("Wedstrijden", "8")
OG_RECHTS = "Handicap incl. verlenging · 711"
TOP3 = [("01:00", "Wizards", "wsh", "Grizzlies", "mem", "Grizzlies -1,5", "1,71", "68%"),
        ("01:00", "Celtics", "bos", "Magic", "orl", "Celtics -4,5", "1,55", "71%"),
        ("01:30", "Nets", "bkn", "76ers", "phi", "76ers -2,5", "1,65", "68%")]

L = {"regels": '<a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels van de NBA</a>',
     "handicap": '<a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">hoe handicap wedden werkt</a>',
     "kans": '<a href="/nieuws/kans-berekenen-uit-odds-impliciete-kans">hoe je een odd omrekent naar een kans</a>',
     "711": '<a href="/bookmakers/711">711</a>',
     "hub": '<a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>',
     "legaal": '<a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>',
     "kijken": '<a href="/live-kijken">live kijken</a>'}

MARKT_H = "Handicap - Winnaar, inclusief verlenging"

# (tijd NL, thuis, uit, odd thuis, odd uit) - markt 'Winnaar inclusief verlenging' bij 711
PROGRAMMA = [
    ("01:00", "Boston Celtics", "Orlando Magic", 1.29, 3.65),
    ("01:00", "Cleveland Cavaliers", "Chicago Bulls", 1.27, 3.85),
    ("01:00", "Washington Wizards", "Memphis Grizzlies", 2.32, 1.63),
    ("01:30", "Brooklyn Nets", "Philadelphia 76ers", 2.70, 1.48),
    ("01:30", "Miami Heat", "Houston Rockets", 2.15, 1.72),
    ("02:00", "Minnesota Timberwolves", "Portland Trail Blazers", 1.72, 2.14),
    ("02:00", "New Orleans Pelicans", "Golden State Warriors", 2.43, 1.58),
    ("03:00", "Denver Nuggets", "Phoenix Suns", 1.22, 4.35),
]
# hoofdlijn per wedstrijd (de handicap waar beide kanten rond 1,90 staan)
HOOFDLIJN = {"Boston Celtics": "-8,5", "Cleveland Cavaliers": "-8,5", "Memphis Grizzlies": "-3,5",
             "Philadelphia 76ers": "-4,5", "Houston Rockets": "-2,5", "Minnesota Timberwolves": "-2,5",
             "Golden State Warriors": "-3,5", "Denver Nuggets": "-9,5"}
LIJNEN = {("Memphis Grizzlies", "-1,5"): 1.71, ("Memphis Grizzlies", "-0,5"): 1.62, ("Memphis Grizzlies", "-3,5"): 1.92,
          ("Boston Celtics", "-4,5"): 1.55, ("Boston Celtics", "-2,5"): 1.41, ("Boston Celtics", "-8,5"): 1.94,
          ("Philadelphia 76ers", "-2,5"): 1.65, ("Philadelphia 76ers", "-1,5"): 1.56, ("Philadelphia 76ers", "-4,5"): 1.87}

# Rustschema: (ploeg, laatste duel, uitslag, rust) - US-speeldatum, eigen telling uit de dagprogramma's
RUST = [("Boston Celtics", "zondag, thuis", "131-94 tegen Dallas", "<strong>back-to-back</strong>"),
        ("Philadelphia 76ers", "zondag, thuis", "131-124 tegen Indiana", "<strong>back-to-back</strong>"),
        ("Houston Rockets", "zondag, uit", "147-119 bij Washington", "<strong>back-to-back</strong>"),
        ("Washington Wizards", "zondag, thuis", "119-147 tegen Houston", "<strong>back-to-back</strong>"),
        ("Phoenix Suns", "zondag, thuis", "123-131 tegen de Lakers", "<strong>back-to-back</strong>"),
        ("Orlando Magic", "vrijdag, thuis", "107-99 tegen Milwaukee", "twee dagen rust"),
        ("Golden State Warriors", "vrijdag, uit", "85-123 bij San Antonio", "twee dagen rust"),
        ("Portland Trail Blazers", "vrijdag, uit", "120-107 bij Sacramento", "twee dagen rust")]

# Saldo per wedstrijd: (wedstrijd, thuissaldo thuisploeg, uitsaldo uitploeg, verschil) - eigen berekening
SALDO = [("Celtics – Magic", "+16,3 (6 duels)", "–1,7 (7 duels)", "+18,0"),
         ("Cavaliers – Bulls", "+4,7 (7 duels)", "–17,6 (7 duels)", "+22,3"),
         ("Wizards – Grizzlies", "–4,8 (6 duels)", "+14,5 (6 duels)", "–19,3"),
         ("Nets – 76ers", "–10,0 (4 duels)", "+0,7 (6 duels)", "–10,7"),
         ("Heat – Rockets", "+1,0 (6 duels)", "+10,5 (6 duels)", "–9,5"),
         ("Timberwolves – Blazers", "+14,1 (7 duels)", "+9,3 (7 duels)", "+4,9"),
         ("Pelicans – Warriors", "–6,0 (9 duels)", "–8,5 (6 duels)", "+2,5"),
         ("Nuggets – Suns", "–0,8 (4 duels)", "–18,3 (3 duels)", "+17,6")]

MEM_UIT = [3, 5, 11, 16, 21, 31]                  # marges van de zes uitzeges van Memphis
BOS_THUIS = [4, 35, 1, 14, 7, 37]                 # marges van de zes thuiszeges van Boston
BOS_REEKS = [7, 39, 20, 22, 5, 37]                # marges van de laatste zes zeges van Boston
PHI_UIT = [6, 5, 5, 6, -24, 6]                    # marges van de zeven... zes uitduels van Philadelphia
WSH_REEKS = [15, 7, 39, 11, 13, 4, 28]            # verliesmarges van de zeven nederlagen op rij van Washington
POR_UIT = [8, 7, 22, 8, 13, -6, 13]               # marges van de zeven uitduels van Portland


def q(x):
    return f"{x:.2f}".replace(".", ",")


def gem(xs):
    return f"{sum(xs) / len(xs):.1f}".replace(".", ",")


COMBI = q(1.71 * 1.55 * 1.65)
UITBET = f"{10 * 1.71 * 1.55 * 1.65:.2f}".replace(".", ",")
MEM_GEM, WSH_GEM = gem(MEM_UIT), gem(WSH_REEKS)
KIJK = B365.kijk_zin("Basketball", DATUM[:10], [(p[1], p[2]) for p in PROGRAMMA], link="/bookmakers/bet365")
KIJK = (KIJK + " ") if KIJK else ""

TIPS = [
    {"wedstrijd": "Washington Wizards vs. Memphis Grizzlies", "competitie": "NBA", "speeltijd_utc": "2026-11-17T00:00:00Z",
     "tijd_nl": "01:00", "tip": "Memphis Grizzlies -1,5 (incl. verlenging)", "odds": "1.71", "markt": MARKT_H,
     "lijn": ("Memphis Grizzlies", "-1,5"),
     "analyse": f"Memphis won al zijn zes uitwedstrijden, telkens met minstens drie punten verschil (gemiddeld {MEM_GEM}). Washington verloor zeven keer op rij, gemiddeld met {WSH_GEM} punten, en speelt vannacht zijn tweede duel in twee dagen."},
    {"wedstrijd": "Boston Celtics vs. Orlando Magic", "competitie": "NBA", "speeltijd_utc": "2026-11-17T00:00:00Z",
     "tijd_nl": "01:00", "tip": "Boston Celtics -4,5 (incl. verlenging)", "odds": "1.55", "markt": MARKT_H,
     "lijn": ("Boston Celtics", "-4,5"),
     "analyse": "Boston staat op 11-2, won al zijn zes thuiswedstrijden en pakte zijn laatste zes zeges allemaal met minstens vijf punten verschil. Orlando mist topscorer Paolo Banchero en heeft een negatief uitsaldo."},
    {"wedstrijd": "Brooklyn Nets vs. Philadelphia 76ers", "competitie": "NBA", "speeltijd_utc": "2026-11-17T00:30:00Z",
     "tijd_nl": "01:30", "tip": "Philadelphia 76ers -2,5 (incl. verlenging)", "odds": "1.65", "markt": MARKT_H,
     "lijn": ("Philadelphia 76ers", "-2,5"),
     "analyse": "Philadelphia won vijf van zijn zes uitwedstrijden, elke keer met vijf of zes punten verschil. Brooklyn is thuis de zwakste ploeg van de nacht: 1-3 en gemiddeld tien punten minder dan de tegenstander."},
]

WEDTIPS = {"wedstrijd-1": "Washington Wizards vs Memphis Grizzlies", "wedtip-1-2": "Memphis Grizzlies -1.5 (incl. verlenging)", "quotering-wedtip-1": "1.71",
           "wedstrijd-2": "Boston Celtics vs Orlando Magic", "wedtip-2-2": "Boston Celtics -4.5 (incl. verlenging)", "quotering-wedtip-2": "1.55",
           "wedstrijd-3": "Brooklyn Nets vs Philadelphia 76ers", "wedtip-3-2": "Philadelphia 76ers -2.5 (incl. verlenging)", "quotering-wedtip-3": "1.65"}

content = f"""<p><strong>Onze 3 beste NBA-wedtips van vannacht: Memphis Grizzlies wint met minstens twee punten verschil in Washington (-1,5, odd 1,71), Boston Celtics wint met minstens vijf punten verschil van Orlando Magic (-4,5, odd 1,55) en Philadelphia 76ers wint met minstens drie punten verschil in Brooklyn (-2,5, odd 1,65). Alle drie bij {L['711']} en alle drie inclusief verlenging. Er staan acht NBA-wedstrijden op het programma, van 01:00 tot 03:00 uur Nederlandse tijd.</strong></p>
<p>De nacht van maandag 16 op dinsdag 17 november is een <strong>tweede speeldag in twee dagen</strong> voor vijf van de zestien ploegen. Dat is dit keer belangrijker dan welke affiche er bovenaan staat, want juist in twee van onze drie tips zit het verschil in rust of in de thuis- en uitcijfers. Wij liepen alle uitslagen van dit seizoen na, rekenden per wedstrijd het thuissaldo van de thuisploeg af tegen het uitsaldo van de uitploeg, controleerden de blessurelijsten en keken daarna pas naar de odds. Beide tabellen hieronder zijn onze eigen berekening. Een tip blijft een inschatting; zet alleen in wat je kunt missen.</p>
<p><strong>Kijken?</strong> {KIJK}Met NBA League Pass, de betaalde dienst van de competitie, zie je alle NBA-wedstrijden. Meer opties lees je op onze pagina {L['kijken']}.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk de NBA vannacht live</strong></a></p>
<h3><strong>De 3 beste NBA-wedtips van vannacht</strong></h3>
{tabel(["Wedstrijd", "Tip", "Markt", "Odd", "Onze kans"], [
    ("Wizards – Grizzlies (01:00)", "<strong>Memphis Grizzlies -1,5</strong>", "Handicap, incl. verlenging", "1,71", "68% (odd: 58%)"),
    ("Celtics – Magic (01:00)", "<strong>Boston Celtics -4,5</strong>", "Handicap, incl. verlenging", "1,55", "71% (odd: 65%)"),
    ("Nets – 76ers (01:30)", "<strong>Philadelphia 76ers -2,5</strong>", "Handicap, incl. verlenging", "1,65", "68% (odd: 61%)"),
])}
<p><em>Odds bij {L['711']}, gelezen op maandag 16 november rond 21:00 uur. Odds kunnen tot de start nog veranderen. Alle drie de tips gelden inclusief een eventuele verlenging. Het zijn losse tips: wie ze combineert, krijgt een totale odd van {COMBI} — dan moeten ze alle drie goed zijn en levert €10 inzet €{UITBET} op. Achter "odd" staat de kans die de odd zelf aangeeft; lees {L['kans']}.</em></p>
<h3><strong>Het NBA-programma van vannacht (Nederlandse tijd)</strong></h3>
{tabel(["Tijd", "Wedstrijd", "Winnaar (thuis – uit)", "Hoofdlijn handicap"], [
    (f"<strong>{t}</strong>", f"{h} – {u}", f"{q(oh)} – {q(ou)}",
     f"{[k for k in (h, u) if k in HOOFDLIJN][0].split()[-1]} {HOOFDLIJN[[k for k in (h, u) if k in HOOFDLIJN][0]]}")
    for t, h, u, oh, ou in PROGRAMMA
])}
<p><em>De odds in deze tabel gelden voor de markt Winnaar, inclusief verlenging. In de laatste kolom staat de hoofdlijn: de handicap waarbij beide kanten ongeveer even waarschijnlijk zijn. Onze drie tips zitten bewust onder die hoofdlijn, zodat er marge overblijft.</em></p>
<h3><strong>Wie speelde er zondagnacht? Het rustschema van vannacht</strong></h3>
<p>Dit is het eerste dat wij bekijken en wat je zelden ergens ziet staan. Een ploeg die gisteren nog speelde, heeft minder benen in de vierde periode — en helemaal als er ook nog gevlogen moest worden. Vannacht geldt dat voor vijf ploegen. Drie andere ploegen hadden juist twee dagen vrij.</p>
{tabel(["Ploeg", "Vorige wedstrijd", "Uitslag", "Rust voor vannacht"],
       [(f"<strong>{p}</strong>", w, u, r) for p, w, u, r in RUST])}
<p>De overige acht ploegen — Orlando uitgezonderd die er al in staat — speelden zaterdag en hebben dus één dag rust gehad. De scherpste combinatie van de nacht: <strong>Houston</strong> won zondag met 147-119 in Washington, vloog door naar Miami en speelt daar vannacht alweer, terwijl Miami zaterdag al klaar was. En <strong>Phoenix</strong> verloor zondag thuis van de Lakers en moet nu naar Denver, waar de bal op hoogte verder vliegt en de longen harder werken.</p>"""

content2 = f"""<h3><strong>Thuissaldo tegen uitsaldo: waar het gat het grootst is</strong></h3>
<p>De tweede tabel is onze eigen berekening en wijst de tips vrijwel aan. Per wedstrijd zetten we het <strong>thuissaldo van de thuisploeg</strong> (punten voor min punten tegen, per thuiswedstrijd dit seizoen) tegenover het <strong>uitsaldo van de uitploeg</strong>. Het verschil in de laatste kolom is een ruwe schatting van het verwachte puntenverschil: een plus betekent voordeel voor de thuisploeg, een min voordeel voor de bezoeker.</p>
{tabel(["Wedstrijd", "Thuissaldo thuisploeg", "Uitsaldo uitploeg", "Verschil"],
       [(f"<strong>{w}</strong>", t, u, f"<strong>{v}</strong>") for w, t, u, v in SALDO])}
<p><em>Eigen berekening uit alle uitslagen van dit seizoen, bijgewerkt na de wedstrijden van zondag. Het aantal duels staat erbij, want bij vier wedstrijden zegt een saldo minder dan bij negen.</em></p>
<p>Drie dingen vallen op. Het grootste gat staat bij <strong>Cavaliers – Bulls</strong> (+22,3), maar daar hebben we gekeken naar de marges per wedstrijd en toen afgehaakt: Cleveland won slechts drie van zijn zeven thuiswedstrijden met meer dan vijf punten verschil. Een groot gemiddelde komt daar vooral van twee uitschieters. Bij <strong>Wizards – Grizzlies</strong> staat het gat met –19,3 helemaal aan de kant van de bezoeker, terwijl de bookmaker Memphis maar als lichte favoriet ziet: dat is het grootste verschil van de nacht tussen de cijfers en de markt. En bij <strong>Nuggets – Suns</strong> (+17,6) zit Denver zelf op een thuissaldo van –0,8, dus ook daar hebben we de tip laten liggen.</p>
<h3><strong>Tip 1: Washington Wizards – Memphis Grizzlies (01:00)</strong></h3>
<p><strong>De tip: Memphis Grizzlies -1,5, odd 1,71. Markt: Handicap - Winnaar, inclusief verlenging.</strong> Memphis moet met minstens twee punten verschil winnen. Rekenvoorbeeld: bij 110-112 is de tip goed, bij 110-111 is de tip verloren.</p>
<p><strong>Waarom deze markt?</strong> Een zege van Memphis staat op 1,63 en de hoofdlijn ligt op -3,5 (1,92). Met -1,5 vragen we twee punten minder dan de hoofdlijn en houden we een odd over die ruim boven de zege zelf ligt.</p>
<p><strong>Het cijfer dat deze tip draagt.</strong> Memphis is dit seizoen <strong>6-0 in uitwedstrijden</strong>, en dat is geen reeks van nipte zeges: de marges waren {", ".join(str(m) for m in MEM_UIT[:-1])} en {MEM_UIT[-1]} punten, gemiddeld {MEM_GEM}. Elke uitzege was dus ruimer dan de 1,5 punt die wij vragen. Uit scoort Memphis 121,3 punten en geeft het er 106,8 weg; thuis is het juist een middelmatige ploeg (3-4). Dit is een echte wegploeg.</p>
<p><strong>Aan de andere kant.</strong> Washington staat op 4-10 en verloor <strong>zeven wedstrijden op rij</strong>, gemiddeld met {WSH_GEM} punten verschil. Zondagavond ging het thuis met 119-147 onderuit tegen Houston — 147 tegen is het hoogste aantal dat een ploeg dit seizoen in één wedstrijd incasseerde van de ploegen die vannacht spelen. Vannacht is het tweede duel in twee dagen. In zijn zes thuiswedstrijden heeft Washington een saldo van –4,8.</p>
<p><strong>Blessures.</strong> Memphis mist vijf spelers (Isaiah Stewart, Scotty Pippen Jr., GG Jackson, Ty Jerome en Quinten Post), maar die reeks van zes uitzeges is grotendeels mét die absenties tot stand gekomen. Bij Washington ontbreken Tristan Vukcevic, Reece Beekman, Justin Champagnie en Jamir Watkins, en is Tre Johnson twijfelachtig.</p>
<p><strong>Spelers om op te letten.</strong> Memphis heeft geen enkele speler die boven de zestien punten per wedstrijd komt — Cameron Boozer leidt met 15,5 punten en 9,7 rebounds — en scoort er toch 120,6 per wedstrijd. Dat is spreiding in plaats van één man. Washington heeft wel twee grote namen: Anthony Davis (24,7 punten, 10,2 rebounds) en Trae Young (8,7 assists).</p>
<p><strong>Onze voorspelling: Washington Wizards – Memphis Grizzlies 112-122.</strong> De odd van 1,71 gaat uit van 58%, wij schatten de kans op 68%. <strong>Het risico:</strong> met Davis en Young heeft Washington meer talent dan de stand doet vermoeden, en een thuisploeg die zeven keer op rij verloor kan juist vannacht uit de startblokken schieten. Liever veiliger? Memphis wint (zonder handicap) staat op 1,63.</p>
<h3><strong>Tip 2: Boston Celtics – Orlando Magic (01:00)</strong></h3>
<p><strong>De tip: Boston Celtics -4,5, odd 1,55. Markt: Handicap - Winnaar, inclusief verlenging.</strong> Boston moet met minstens vijf punten verschil winnen. Rekenvoorbeeld: bij 115-110 is de tip goed, bij 114-110 is de tip verloren.</p>
<p><strong>Waarom deze markt?</strong> Een zege van Boston staat op 1,29: te laag voor een losse tip. De hoofdlijn ligt op -8,5 (1,94). Met -4,5 houden we vier punten extra marge en blijft de odd speelbaar.</p>
<p><strong>Vorm en cijfers.</strong> Boston staat op 11-2 en is met een saldo van +13,2 de beste ploeg van de nacht. Thuis is het <strong>6-0</strong>, met een saldo van +16,3 per wedstrijd: 121,8 punten voor, 105,5 tegen. Belangrijker voor deze lijn: de laatste zes zeges kwamen allemaal met minstens vijf punten verschil tot stand ({", ".join(str(m) for m in BOS_REEKS[:-1])} en {BOS_REEKS[-1]}). Zondag werd Dallas thuis met 131-94 opzij gezet.</p>
<p><strong>Aan de andere kant.</strong> Orlando staat op 5-7, maar is wél in vorm: drie zeges op rij, en uit is de ploeg beter dan thuis (4-3 tegen 1-4). Het uitsaldo is met –1,7 bijna neutraal. Op 1 november won Boston in Orlando met 108-97, elf punten verschil.</p>
<p><strong>Blessures.</strong> Dit is het verschil: Orlando mist <strong>Paolo Banchero</strong> (verstuikte enkel), en daarnaast Jonathan Isaac, Noah Penda en Izaiyah Nelson. Franz Wagner (24,4 punten, 8,2 assists) moet het dragen. Bij Boston is alleen Neemias Queta twijfelachtig, met rust als reden; Jayson Tatum (26,8 punten, 7,3 assists) is er.</p>
<p><strong>Onze voorspelling: Boston Celtics – Orlando Magic 118-106.</strong> De odd van 1,55 gaat uit van 65%, wij schatten de kans op 71%. <strong>Het risico:</strong> Boston speelt zijn tweede wedstrijd in twee dagen en won twee van die zes thuiswedstrijden met slechts één en vier punten verschil — precies onder onze lijn. Orlando is bovendien de fitste van de twee. Liever veiliger? Boston -2,5 staat op 1,41.</p>
<h3><strong>Tip 3: Brooklyn Nets – Philadelphia 76ers (01:30)</strong></h3>
<p><strong>De tip: Philadelphia 76ers -2,5, odd 1,65. Markt: Handicap - Winnaar, inclusief verlenging.</strong> Philadelphia moet met minstens drie punten verschil winnen. Rekenvoorbeeld: bij 108-111 is de tip goed, bij 108-110 is de tip verloren.</p>
<p><strong>Waarom deze markt?</strong> Een zege van Philadelphia staat op 1,48 en de hoofdlijn ligt op -4,5 (1,87). Met -2,5 vragen we twee punten minder.</p>
<p><strong>Vorm en cijfers.</strong> Philadelphia staat op 11-3 en is uit 5-1. Daar zit een merkwaardig patroon in: <strong>alle vijf de uitzeges kwamen met vijf of zes punten verschil</strong> (6, 5, 5, 6 en 6), de enige uitnederlaag was een afstraffing in Cleveland (-24). Philadelphia wint op bezoek dus zelden ruim, maar bijna altijd. Dat is precies waarom we niet verder gaan dan -2,5: op de hoofdlijn van -4,5 zouden die zeges van vijf punten maar een halve punt marge hebben.</p>
<p><strong>Aan de andere kant.</strong> Brooklyn is met een thuissaldo van <strong>–10,0</strong> de zwakste thuisploeg van de nacht en staat op 1-3 in eigen zaal. De ploeg maakt daar gemiddeld maar 105,0 punten — het laagste aantal van alle zestien ploegen vannacht — en geeft er 115,0 weg. Zaterdag werd het 110-129 in Memphis.</p>
<p><strong>Blessures.</strong> Philadelphia mist LeBron James, Dominick Barlow, Adem Bona en Ariel Hukporti, en <strong>Joel Embiid staat als twijfelachtig</strong>. Tyrese Maxey (26,7 punten) is er wel. Brooklyn meldt geen afwezigen; Michael Porter Jr. (21,5 punten, 7,5 rebounds) is de topscorer.</p>
<p><strong>Onze voorspelling: Brooklyn Nets – Philadelphia 76ers 107-116.</strong> De odd van 1,65 gaat uit van 61%, wij schatten de kans op 68%. <strong>Het risico:</strong> dit is de tip met de meeste vraagtekens. Philadelphia speelt zijn tweede duel in twee dagen, Brooklyn is uitgerust, en zonder Embiid zijn die uitzeges van vijf punten snel uitzeges van één punt. Liever veiliger? Philadelphia -1,5 staat op 1,56.</p>
<h3><strong>De andere NBA-wedstrijden van vannacht</strong></h3>
<p><strong>Cavaliers – Bulls (01:00)</strong>: op papier het grootste gat van de nacht (+22,3), want Chicago geeft uit 126,6 punten per wedstrijd weg. Maar Cleveland mist Evan Mobley en won slechts drie van zeven thuisduels met meer dan vijf punten verschil, en Chicago won zijn laatste twee. Geen tip. <strong>Heat – Rockets (01:30)</strong>: Houston is uit de sterkste ploeg van de nacht (+10,5) maar zit in een back-to-back met vlucht, mist Clint Capela en Steven Adams en kan niet beschikken over de geschorste Marcus Smart; Miami was zaterdag al klaar. <strong>Timberwolves – Blazers (02:00)</strong>: de aantrekkelijkste wedstrijd van de nacht. Minnesota is thuis uitstekend (+14,1) maar mist <strong>Anthony Edwards</strong> en Donte DiVincenzo, en verloor zaterdag thuis van Chicago. Portland won zes van zijn zeven uitduels, alle zes met minstens zeven punten verschil, maar mist Ja Morant en Shaedon Sharpe. Twee halve ploegen: wij blijven erbuiten. <strong>Pelicans – Warriors (02:00)</strong>: New Orleans verloor zes keer op rij, maar Golden State is zonder Stephen Curry, Kristaps Porziņģis en Moses Moody uit 2-4 en verloor zijn laatste twee uitduels met 7 en 38 punten verschil. <strong>Nuggets – Suns (03:00)</strong>: Phoenix won nog geen enkele uitwedstrijd (0-3, gemiddeld 18,3 punten verschil) en zit in een back-to-back, maar Denver heeft thuis een negatief saldo en won maar één van vier thuisduels ruim. Nikola Jokić staat op 23,7 punten, 10,5 rebounds en 9,1 assists.</p>"""

content3 = f"""<h3><strong>Handicap bij de NBA: hoe werkt het?</strong></h3>
<p>Bij de NBA eindigt een wedstrijd nooit in een gelijkspel: bij een gelijke stand na 48 minuten volgt een verlenging van vijf minuten. Onze tips van vannacht zijn alle drie <strong>inclusief verlenging</strong>, dus die vijf minuten tellen mee voor het puntenverschil.</p>
{tabel(["Markt", "Wat telt mee", "Voorbeeld vannacht"], [
    ("<strong>Winnaar</strong>", "Eindstand inclusief verlenging. Er is altijd een winnaar.", "Memphis wint in Washington: 1,63"),
    ("<strong>Handicap</strong>", "Eindstand inclusief verlenging, met een puntenachterstand voor de favoriet.", "Memphis -1,5: 1,71"),
    ("<strong>Hoofdlijn</strong>", "De handicap waarbij beide kanten ongeveer even waarschijnlijk zijn.", "Memphis -3,5: 1,92"),
])}
<p>Een min-handicap trekt punten af van de favoriet. Bij Memphis -1,5 haal je in gedachten 1,5 punt weg bij Memphis: wint de ploeg met twee punten of meer, dan is de tip goed. De halve punt zorgt ervoor dat je inzet nooit wordt teruggestort. Hoe lager de handicap, hoe groter de kans en hoe lager de odd. Lees ook {L['handicap']} en {L['regels']}.</p>
<p>Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit. Twijfel je? Lees {L['legaal']}. Alle basketbaltips vind je op onze pagina {L['hub']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wat zijn de beste NBA-wedtips van vannacht?</strong><br>Memphis Grizzlies -1,5 in Washington (1,71), Boston Celtics -4,5 tegen Orlando Magic (1,55) en Philadelphia 76ers -2,5 in Brooklyn (1,65), alle odds bij 711 en alle drie inclusief verlenging. Zet alleen in wat je kunt missen.</p>
<p><strong>Hoeveel NBA-wedstrijden zijn er vannacht?</strong><br>Acht, met zestien ploegen. De eerste drie beginnen om 01:00 uur Nederlandse tijd, de laatste (Nuggets – Suns) om 03:00 uur.</p>
<p><strong>Welke ploegen spelen vannacht een back-to-back?</strong><br>Boston, Philadelphia, Houston, Washington en Phoenix speelden zondagnacht ook al. Orlando, Golden State en Portland hadden twee dagen rust; de rest speelde zaterdag.</p>
<p><strong>Speelt Paolo Banchero vannacht?</strong><br>Nee. Orlando meldt hem als out met een verstuikte enkel. Ook Jonathan Isaac, Noah Penda en Izaiyah Nelson ontbreken.</p>
<p><strong>Speelt Joel Embiid vannacht in Brooklyn?</strong><br>Dat is onzeker: Philadelphia zet hem op de blessurelijst als twijfelachtig. LeBron James is wel zeker afwezig.</p>
<p><strong>Hoe staat Memphis er uit voor?</strong><br>Memphis won al zijn zes uitwedstrijden van dit seizoen, met marges van 3 tot 31 punten, en scoort uit 121,3 punten per wedstrijd. Thuis is de ploeg juist 3-4.</p>
<p><strong>Gelden de tips inclusief verlenging?</strong><br>Ja, alle drie. Een verlenging telt mee voor de eindstand, dus ook voor het puntenverschil bij de handicaps.</p>
<p><strong>Waar kan ik de NBA vannacht live kijken?</strong><br>Alle acht de wedstrijden staan in het streamingschema van Bet365, en met NBA League Pass zie je elke wedstrijd. Meer opties staan op onze pagina live kijken.</p>
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
    assert 1400 <= woorden <= 2900, woorden
    assert KIJK, "geen Bet365-stream in het schema: KIJK-zin aanpassen"
    assert len(TIPS) == len(TOP3) == 3 and [q(float(t["odds"])) for t in TIPS] == [k[6] for k in TOP3]
    assert all(1.40 <= float(t["odds"]) <= 1.80 for t in TIPS)
    for t in TIPS:
        h, u = t["wedstrijd"].split(" vs. ")
        p = next(x for x in PROGRAMMA if x[1] == h and x[2] == u)
        assert t["tijd_nl"] == p[0] and float(t["odds"]) == LIJNEN[t["lijn"]], t
    # de tip moet onder de hoofdlijn liggen (marge houden)
    for t in TIPS:
        ploeg, lijn = t["lijn"]
        assert float(lijn.replace(",", ".")) > float(HOOFDLIJN[ploeg].replace(",", ".")), t["lijn"]
    assert COMBI == "4,37" and UITBET == "43,73", (COMBI, UITBET)
    assert round(100 / 1.71) == 58 and round(100 / 1.55) == 65 and round(100 / 1.65) == 61
    assert len(MEM_UIT) == 6 and all(m >= 3 for m in MEM_UIT) and MEM_GEM == "14,5"
    assert len(BOS_REEKS) == 6 and all(m >= 5 for m in BOS_REEKS)
    assert len(BOS_THUIS) == 6 and sorted(BOS_THUIS)[:2] == [1, 4]        # twee thuiszeges onder de lijn
    assert PHI_UIT.count(5) == 2 and PHI_UIT.count(6) == 3 and min(PHI_UIT) == -24
    assert len(WSH_REEKS) == 7 and WSH_GEM == "16,7"
    assert len(POR_UIT) == 7 and sum(1 for m in POR_UIT if m > 0) == 6 and all(m >= 7 for m in POR_UIT if m > 0)
    assert 112 - 110 >= 2 and 111 - 110 < 2 and 122 - 112 >= 2           # rekenvoorbeelden tip 1
    assert 115 - 110 >= 5 and 114 - 110 < 5 and 118 - 106 >= 5           # tip 2
    assert 111 - 108 >= 3 and 110 - 108 < 3 and 116 - 107 >= 3           # tip 3
    assert len(PROGRAMMA) == 8 and len(SALDO) == 8 and len(RUST) == 8
    assert sum(1 for r in RUST if "back-to-back" in r[3]) == 5
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert "<h2" not in alles and "<h4" not in alles
    for verboden in ("betcity", "espn", "footymetrics", "opstellingvandaag", "waaroptv", "toto"):
        assert verboden not in alles.lower(), verboden
    assert not re.search(r"\bunder\b", alles, re.I) and alles.count(BET365) == 1
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/") or href == BET365, href
    print("dry run ok - niets gepubliceerd")
