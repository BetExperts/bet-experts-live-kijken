# -*- coding: utf-8 -*-
"""NIEUW wedgids-artikel (Nieuws, nog geen item): bankroll management bij wedden, zo bepaal je je inzet.
Slug bankroll-management-wedden (gaf HTTP 404 op 10-11-2026, dus vrij). Rubriek Speluitleg, wedgids-categorie 'Wedstrategieën'.
Onderwerp: Engelstalige analysesite (alleen het onderwerp; tekst, opbouw en voorbeelden zelf gemaakt).
Zoekwoorden: 'bankroll management wedden', 'bankroll management', 'inzet bepalen wedden', 'units wedden',
'kelly criterium wedden', 'flat staking', 'hoeveel inzetten per weddenschap'.

Feiten nagelopen op 10-11-2026 (bronnen NIET in de tekst genoemd):
- Besluit kansspelen op afstand art. 4.14 (wetten.overheid.nl/BWBR0044773, gelezen 10-11-2026): inschrijving pas nadat de
  speler grenzen heeft aangegeven voor (a) maximale duur toegang spelersinterface per dag/week/maand, (b) maximale
  stortingen per dag/week/maand en (c) maximaal tegoed op de speelrekening; verlaging gaat direct in, verhoging 'eerst na
  ten minste een week'; de maxima kunnen niet worden overschreden.
- Netto-stortingsgrens (Ksa-infoblad nettostortingslimiet, kansspelautoriteit.nl/publish/library/30/infoblad_nettostortingslimiet.pdf;
  Beleidsregel verantwoord spelen 2024, in werking 1-10-2024; rijksoverheid.nl nieuws 01-10-2024): €300 per maand voor
  18 t/m 23 jaar, €700 vanaf 24 jaar, per aanbieder; netto = stortingen min opnames; boven de grens blokkeert de
  aanbieder verdere stortingen of doet hij een draagkrachttoets. Het is een beleidsregel/advies van de Ksa, geen wet:
  daarom in de tekst 'hanteert de Ksa' en niet 'de wet zegt'.
- Contactmoment bij een eigen stortingslimiet van €350+ per maand (<24: €150+), sinds 1-10-2024: Regeling speellimieten
  (Stcrt. 2024, 19648), eerder nagelopen in specials/netto_stortingslimiet.py (21-10-2026).
- Kelly-criterium voor een decimale quotering o en kans p: f = (p*o - 1) / (o - 1) (standaardformule, b = o - 1).
Rekenvoorbeelden: unittabel, Kelly (52% @ 2,10), Monte-Carlo-simulatie (5.000 runs x 500 weddenschappen @ 2,00, vaste seed)
en martingale-reeks (exacte kans via dynamisch programmeren); alles hieronder berekend en ge-assert.
Bewust weggelaten: vaste 'beste' unitgrootte (geen eenduidige bron, daarom bandbreedte 0,5-2%), andere progressies dan
martingale (eigen artikelen), merknamen van bookmakers, elke belofte van winst.
Interne links gecontroleerd op 10-11-2026 (HTTP 200): zie de lijst in de asserts.
  python3 specials/wg_bankroll-management.py"""
import os, sys, re, random, statistics
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
import lk_webflow as WF
from legaal_data import tabel

ITEM_ID = None   # nieuw artikel
SLUG = "bankroll-management-wedden"
RUBRIEK = "6502b66cd9992658b4037cf5"   # Speluitleg
WEDGIDS_CAT = "Wedstrategieën"
TITEL = "Bankroll management bij wedden: zo bepaal je je inzet"
SAMENVATTING = ("Bankroll management bij wedden uitgelegd: budget, units, vlak inzetten, percentage en Kelly, met een "
                "simulatie van 500 weddenschappen.")

OG_KOP = "Bankroll <span>management</span>"
OG_EYEBROW = "Wedstrategie uitgelegd"
OG_CHIPS = ["Units, vlak en Kelly", "Met simulatie"]
OG_MOTIEF = "tabel"

STORTING = "/nieuws/netto-stortingslimiet"
MARTINGALE = "/nieuws/wat-is-het-martingale-systeem-een-dubbel-of-niets-wedstrategie"
GOKVERSLAVING = "/nieuws/voorkomen-van-een-gokverslaving-belangrijke-stappen-en-hulpbronnen"
VALUE = "/nieuws/wat-is-de-wedstrategie-value-betting"
ODDS = "/nieuws/odds-uitgelegd-quotering-lezen"
CRUKS = "/nieuws/cruks-de-gokstop-voor-verantwoord-gokken"
LEGAAL = "/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland"


def k(x, n=2):
    return f"{x:,.{n}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def eur(x, n=2):
    return "€" + k(x, n)


def pct(x, n=0):
    return k(100 * x, n) + "%"


# ---- units: 1% en 2% van verschillende bankrolls ----
BANKROLLS = [100, 250, 500, 1000]
RIJEN_UNITS = [(eur(b, 0), eur(0.005 * b), eur(0.01 * b), eur(0.02 * b)) for b in BANKROLLS]
assert RIJEN_UNITS[2] == ("€500", "€2,50", "€5,00", "€10,00")

# ---- Kelly: eigen kans 52%, quotering 2,10, bankroll €500 ----
KP, KO, KB = 0.52, 2.10, 500.0
EDGE = KP * KO - 1
KELLY = EDGE / (KO - 1)
assert pct(EDGE, 1) == "9,2%" and pct(KELLY, 1) == "8,4%"
assert eur(KELLY * KB) == "€41,82" and eur(KELLY / 2 * KB) == "€20,91" and eur(KELLY / 4 * KB) == "€10,45"
assert pct(KELLY / 2, 1) == "4,2%" and pct(KELLY / 4, 1) == "2,1%"
ECHT = 0.47
assert pct(ECHT * KO - 1, 1) == "-1,3%"

# ---- simulatie: 500 weddenschappen @ 2,00, start €500, 5.000 runs per plan, vaste seed ----
START, N, ODD, RUNS, BASIS = 500.0, 500, 2.00, 5000, 5.0
P_MET, P_ZONDER = 0.52, 0.475                      # met 4% voorsprong / zonder voorsprong (-5%)
assert round(P_MET * ODD - 1, 3) == 0.04 and round(P_ZONDER * ODD - 1, 3) == -0.05
KELLY_SIM = (P_MET * ODD - 1) / (ODD - 1)          # 4% van de bankroll; Kelly rekent met de kans die je dénkt te hebben
PLANNEN = [  # (naam, omschrijving inzet, functie bankroll -> inzet of None = martingale)
    ("Vlak 1%", "Altijd €5 (1% van de start)", lambda b: BASIS),
    ("Vlak 5%", "Altijd €25 (5% van de start)", lambda b: 25.0),
    ("Percentage 2%", "2% van je actuele bankroll", lambda b: 0.02 * b),
    ("Volle Kelly", f"{pct(KELLY_SIM)} van je actuele bankroll", lambda b: KELLY_SIM * b),
    ("Kwart Kelly", f"{pct(KELLY_SIM / 4)} van je actuele bankroll", lambda b: KELLY_SIM / 4 * b),
    ("Martingale", "€5, na elk verlies verdubbelen", None),
]


def run(plan, p, rng):
    b, m = START, BASIS
    for _ in range(N):
        s = m if plan is None else plan(b)
        s = min(s, b)
        if b < 1 or s < 0.01:
            break
        if rng.random() < p:
            b += s * (ODD - 1); m = BASIS
        else:
            b -= s; m *= 2
    return b


def simuleer():
    uit = {}
    for naam, _, plan in PLANNEN:
        for p in (P_MET, P_ZONDER):
            rng = random.Random(2026)
            r = [run(plan, p, rng) for _ in range(RUNS)]
            uit[naam, p] = (statistics.median(r), sum(x < START / 2 for x in r) / RUNS, sum(x > START for x in r) / RUNS)
    return uit


SIM = simuleer()


def cel(naam, p):
    med, helft, _ = SIM[naam, p]
    return f"{eur(med, 0)}<br>helft kwijt: {pct(helft, 1)}"


RIJEN_SIM = [(f"<strong>{naam}</strong>", inzet, cel(naam, P_MET), cel(naam, P_ZONDER)) for naam, inzet, _ in PLANNEN]
M = {(n, p): (round(v[0]), round(1000 * v[1]) / 10, round(1000 * v[2]) / 10) for (n, p), v in SIM.items()}
# vaste seed -> vaste uitkomsten; controle op de getallen die in de tekst terugkomen
assert M["Vlak 1%", P_MET][0] > START and M["Kwart Kelly", P_MET][1] <= 1
assert all(M[n, P_ZONDER][0] < START for n, _, _ in PLANNEN), "zonder voorsprong verliest elk plan in de mediaan"
assert M["Vlak 5%", P_MET][0] > M["Vlak 1%", P_MET][0] and M["Vlak 5%", P_MET][1] > 10
assert M["Volle Kelly", P_ZONDER][1] > 60 and M["Martingale", P_MET][0] == 0 and M["Martingale", P_MET][1] > 40

# ---- martingale: €5 basis, bankroll €500 ----
VERLIES6 = sum(BASIS * 2 ** i for i in range(6))
assert eur(VERLIES6, 0) == "€315" and eur(BASIS * 2 ** 6, 0) == "€320" and eur(START - VERLIES6, 0) == "€185"


def kans_reeks(n, lengte, q):
    """Exacte kans op minstens één reeks van `lengte` verliezen op rij in n weddenschappen (verlieskans q)."""
    d = [1.0] + [0.0] * (lengte - 1)   # d[i] = kans dat de huidige verliesreeks i lang is (nog geen volle reeks gehad)
    for _ in range(n):
        nieuw = [0.0] * lengte
        nieuw[0] = sum(d) * (1 - q)
        for i in range(lengte - 1):
            nieuw[i + 1] += d[i] * q
        d = nieuw
    return 1 - sum(d)


P_REEKS = kans_reeks(100, 6, 1 - P_ZONDER)
P_REEKS_MET = kans_reeks(100, 6, 1 - P_MET)
assert pct(P_REEKS) == "64%" and pct(P_REEKS_MET) == "47%" and P_REEKS_MET < P_REEKS
assert abs(kans_reeks(6, 6, 0.5) - 0.5 ** 6) < 1e-12

OG_DATA = ["Bankroll · €500", "1 unit (1%) · €5", f"Kwart Kelly · {pct(KELLY / 4, 1)}", "Martingale · 6× mis = €315 weg"]

content = f"""<p><strong>Bankroll management betekent dat je een vast bedrag apart zet om mee te wedden, geld dat je kunt missen, en per weddenschap maar een klein deel daarvan inzet, meestal 1 tot 2 procent. Zo overleef je een verliesreeks en blijft één slechte avond één slechte avond. Het maakt van een verliezende aanpak geen winnende: het beperkt de schade en houdt je inzetten beheersbaar.</strong></p>
<p>Hieronder lees je hoe je een bankroll bepaalt, wat een unit is en hoe vlak inzetten, percentage-inzetten en het Kelly-criterium werken. Met een simulatie van 500 weddenschappen zie je wat elk inzetplan in de praktijk doet, en waarom verdubbelen na verlies zo gevaarlijk is.</p>
<h3><strong>Wat is een bankroll bij wedden?</strong></h3>
<p>Je bankroll is het totale bedrag dat je reserveert om mee te wedden. Het is geld dat je kunt verliezen zonder dat huur, boodschappen of spaargeld in gevaar komen. Zie het als een uitgave aan ontspanning, net als een concertkaartje: als het op is, is het op.</p>
<p>Leg vooraf vast voor welke periode je bankroll geldt, bijvoorbeeld een maand of een seizoen. Houd het geld gescheiden van je gewone rekening en stort niet bij als het weg is. Wed alleen bij een bookmaker met een Nederlandse vergunning; <a href="{LEGAAL}">zo controleer je dat</a>.</p>
<h3><strong>Hoe past je bankroll bij de Nederlandse speelgrenzen?</strong></h3>
<p>Bij een legale bookmaker stel je verplicht speelgrenzen in voordat je kunt spelen: hoeveel je maximaal stort per dag, week of maand, hoe lang je maximaal speelt en hoeveel saldo er maximaal op je account mag staan. Een verlaging gaat direct in, een verhoging pas na minstens een week. Wil je je stortingslimiet op €350 of meer per maand zetten (onder de 24 jaar: €150), dan neemt de aanbieder eerst contact met je op.</p>
<p>Daarnaast hanteert de Kansspelautoriteit een netto-stortingsgrens: €300 per maand tot je 24e en €700 per maand vanaf 24 jaar, per aanbieder. Netto betekent stortingen min opnames. Ga je erover, dan blokkeert de aanbieder verdere stortingen of controleert hij eerst of je het kunt betalen. Alles hierover lees je in ons artikel over de <a href="{STORTING}">netto-stortingslimiet</a>.</p>
<p>Die grenzen zijn een plafond, geen advies. Handiger is om je eigen stortingslimiet gelijk te zetten aan je bankroll. Is je maandbudget €100, zet de limiet dan op €100 per maand. Dan bewaakt de bookmaker je plan mee, en kun je in een opwelling niet meer storten dan je had afgesproken.</p>
<h3><strong>Wat is een unit en hoe groot moet die zijn?</strong></h3>
<p>Een unit is je standaardinzet, uitgedrukt als vast deel van je bankroll. Veel wedders houden 1 unit = 1% van hun bankroll aan. Voorzichtiger is 0,5%; boven de 2 tot 3% per weddenschap word je kwetsbaar voor verliesreeksen, die bij elke wedder voorkomen.</p>
{tabel(["Bankroll", "0,5%", "1 unit (1%)", "2%"], RIJEN_UNITS)}
<p>Werken in units heeft twee voordelen. Je inzet groeit en krimpt mee als je de unit af en toe herberekent, en je kunt resultaten vergelijken met die van anderen, ongeacht hoeveel geld ieder inzet. Sommige wedders zetten meer units in als ze meer value zien, bijvoorbeeld 0,5 tot 2 units. Dat kan, zolang de bovengrens vastligt en je die niet verhoogt om verlies terug te winnen.</p>"""

content2 = f"""<h3><strong>Vlak inzetten, percentage of Kelly: wat is het verschil?</strong></h3>
<ul><li><strong>Vlak inzetten (flat staking):</strong> elke weddenschap hetzelfde bedrag, bijvoorbeeld €5 bij een bankroll van €500. Simpel en goed bij te houden. Nadeel: als je bankroll krimpt, wordt diezelfde €5 een steeds groter deel ervan.</li><li><strong>Percentage inzetten:</strong> elke keer een vast percentage van je actuele bankroll. Na verlies zet je vanzelf minder in, na winst meer. Je bankroll raakt zo nooit helemaal op, maar kan wel flink slinken.</li><li><strong>Kelly-criterium:</strong> je inzet hangt af van hoeveel voordeel je denkt te hebben. Hoe groter het verschil tussen jouw kansinschatting en de quotering, hoe hoger de inzet. Zonder voordeel zegt Kelly: niet wedden.</li></ul>
<h3><strong>Hoe werkt het Kelly-criterium?</strong></h3>
<p>De formule voor een decimale quotering: <strong>inzet als deel van je bankroll = (kans × quotering − 1) / (quotering − 1)</strong>. De kans is je eigen inschatting, niet de kans die de bookmaker in zijn odds verwerkt.</p>
<p><strong>Rekenvoorbeeld.</strong> Je schat de kans dat een team wint op {pct(KP)} en de bookmaker biedt {k(KO)}. Je verwachte voordeel is dan {k(KP)} × {k(KO)} − 1 = {pct(EDGE, 1)}. Kelly zegt: {k(EDGE, 3)} / {k(KO - 1)} = {pct(KELLY, 1)} van je bankroll, bij {eur(KB, 0)} dus {eur(KELLY * KB)}. Dat is fors. Daarom kiezen de meeste wedders een fractie: halve Kelly ({pct(KELLY / 2, 1)}, {eur(KELLY / 2 * KB)}) of kwart Kelly ({pct(KELLY / 4, 1)}, {eur(KELLY / 4 * KB)}).</p>
<p>De zwakke plek is de kansinschatting. Kelly gaat ervan uit dat jouw {pct(KP)} klopt. Is de echte kans {pct(ECHT)}, dan heb je geen voordeel maar een nadeel van {pct(-(ECHT * KO - 1), 1)}, en zet volle Kelly juist veel geld in op een slechte weddenschap. Fractionele Kelly vangt een deel van die fouten op. Hoe je zelf een kans inschat en vergelijkt met de odds, lees je bij <a href="{VALUE}">value betting</a>; hoe je een quotering omrekent naar een kans, in <a href="{ODDS}">odds uitgelegd</a>.</p>
<h3><strong>Welk inzetplan houdt het langst vol? Een simulatie</strong></h3>
<p>We lieten elk plan {k(RUNS, 0)} keer lopen over {N} weddenschappen op een quotering van {k(ODD)}, met een startbankroll van {eur(START, 0)}. Twee scenario's. In het eerste heb je echt een voorsprong: {pct(P_MET)} winkans, gemiddeld {pct(P_MET * ODD - 1)} rendement. In het tweede denk je dat, maar win je in werkelijkheid {pct(P_ZONDER, 1)}: een nadeel van {pct(1 - P_ZONDER * ODD)}, ongeveer de marge van een bookmaker. Kelly rekent in beide gevallen met de {pct(P_MET)} die je dénkt te hebben. Per plan zie je de middelste eindstand (de mediaan) en de kans dat je na {N} weddenschappen minder dan de helft over hebt. <em>Fictieve simulatie, geen voorspelling.</em></p>
{tabel(["Inzetplan", "Inzet per weddenschap", f"Met voorsprong ({pct(P_MET)})", f"Zonder voorsprong ({pct(P_ZONDER, 1)})"], RIJEN_SIM)}
<p>Wat laat dit zien?</p>
<ul><li><strong>Zonder voorsprong verlies je met elk plan.</strong> De mediaan ligt bij alle zes de plannen onder de {eur(START, 0)}. Een inzetplan maakt van een nadeel geen voordeel; het bepaalt vooral hoe hard de schommelingen zijn.</li><li><strong>Grote vlakke inzetten zijn riskant.</strong> Vlak {eur(25, 0)} levert met voorsprong de hoogste mediaan op, maar toch eindigt {pct(SIM['Vlak 5%', P_MET][1])} van de reeksen onder de helft. Zonder voorsprong is dat {pct(SIM['Vlak 5%', P_ZONDER][1])}.</li><li><strong>Volle Kelly schommelt hard.</strong> Met voorsprong eindigt nog {pct(SIM['Volle Kelly', P_MET][1])} onder de helft. Zat je inschatting ernaast, dan is het {pct(SIM['Volle Kelly', P_ZONDER][1])}.</li><li><strong>Kleine inzetten zijn het rustigst.</strong> Vlak 1% en kwart Kelly groeien langzamer, maar je bankroll houdt het het langst vol, ook als je je voorsprong overschat.</li><li><strong>Martingale gaat vaak in één klap mis.</strong> Zelfs mét voorsprong is de mediaan {eur(0, 0)}: {pct(SIM['Martingale', P_MET][1])} van de reeksen eindigt onder de helft, vrijwel altijd met een lege bankroll.</li></ul>"""

content3 = f"""<h3><strong>Waarom is het martingale-systeem gevaarlijk?</strong></h3>
<p>Bij martingale verdubbel je je inzet na elk verlies. Het voelt veilig: de eerste winst maakt al je verlies goed, plus je basisinzet. Maar de inzetten lopen razendsnel op. Met een basisinzet van {eur(BASIS, 0)} en een bankroll van {eur(START, 0)} ben je na 6 verliezen op rij {eur(VERLIES6, 0)} kwijt. De zevende inzet zou {eur(BASIS * 2 ** 6, 0)} moeten zijn, maar je hebt nog maar {eur(START - VERLIES6, 0)}.</p>
<p>Hoe groot is die kans? Bij een winkans van {pct(P_ZONDER, 1)} op een quotering van {k(ODD)} krijg je in 100 weddenschappen met {pct(P_REEKS)} kans minstens één keer 6 verliezen op rij. Je wint dus steeds {eur(BASIS, 0)} en riskeert in één reeks bijna je hele bankroll. Daar komen de maximale inzet van de bookmaker en je stortingslimiet nog bij. Meer rekenvoorbeelden lees je in ons artikel over <a href="{MARTINGALE}">het martingale-systeem</a>.</p>
<h3><strong>Waarom moet je je weddenschappen bijhouden?</strong></h3>
<p>Zonder administratie weet je niet of je aanpak werkt. Je onthoudt de mooie winst op een hoge quotering beter dan tien kleine verliezen. Noteer daarom per weddenschap de datum, de wedstrijd en markt, de bookmaker, de quotering, je inzet in euro's en units, de uitkomst en je winst of verlies.</p>
<p>Reken daarna je rendement uit: totale winst gedeeld door totale inzet. Pas na honderden weddenschappen zegt dat getal echt iets, daarvoor speelt toeval een grote rol. Leg je administratie ook naast je budget: hoeveel heb je deze maand gestort, en past dat bij wat je met jezelf had afgesproken?</p>
<h3><strong>Hoe begin je met bankroll management?</strong></h3>
<ol><li><strong>Bepaal je budget.</strong> Een bedrag per maand of seizoen dat je kunt missen.</li><li><strong>Stel je limieten in.</strong> Zet je stortingslimiet bij de bookmaker gelijk aan dat budget.</li><li><strong>Kies je unit.</strong> 1% van je bankroll is een goed startpunt, 0,5% als je voorzichtig wilt zijn.</li><li><strong>Kies een inzetplan.</strong> Vlak inzetten is het eenvoudigst; percentage of kwart Kelly als je je inzet wilt laten meebewegen.</li><li><strong>Houd alles bij.</strong> Elke weddenschap, ook de verliezen.</li><li><strong>Evalueer per maand.</strong> Herbereken je unit, maar verhoog hem nooit om verlies goed te maken.</li></ol>
<h3><strong>Wat doe je als je bankroll op is?</strong></h3>
<p>Stoppen tot de volgende periode. Bijstorten om verlies terug te winnen heet 'chasing' en is precies het gedrag waar bankroll management je tegen moet beschermen. Lukt stoppen niet, of merk je dat wedden meer is dan ontspanning, lees dan <a href="{GOKVERSLAVING}">hoe je een gokverslaving voorkomt en waar je hulp vindt</a>, of overweeg een gokstop via <a href="{CRUKS}">Cruks</a>. Meer uitleg over wedden vind je in de <a href="/wedgids">wedgids</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoeveel moet ik per weddenschap inzetten?</strong><br>Een gangbare richtlijn is 1 tot 2% van je bankroll per weddenschap, bij een bankroll van {eur(500, 0)} dus {eur(5, 0)} tot {eur(10, 0)}. Kies je hoger, dan kan een normale verliesreeks al een groot deel van je budget kosten.</p>
<p><strong>Wat is een unit bij wedden?</strong><br>Een unit is je standaardinzet, meestal 1% van je bankroll. Door in units te rekenen kun je resultaten vergelijken, los van hoeveel geld iemand inzet.</p>
<p><strong>Is het Kelly-criterium geschikt voor beginners?</strong><br>Alleen als fractie, bijvoorbeeld kwart Kelly, en alleen als je je kansinschatting kunt onderbouwen. Volle Kelly levert grote schommelingen op en wordt gevaarlijk zodra je je voorsprong overschat.</p>
<p><strong>Kan ik met bankroll management winst garanderen?</strong><br>Nee. Een inzetplan bepaalt hoe groot je schommelingen zijn, niet of je op lange termijn wint. Zonder echte voorsprong op de odds verlies je met elk plan.</p>
<p><strong>Hoe groot moet mijn bankroll zijn?</strong><br>Zo groot als het bedrag dat je kunt missen, en niet groter. Daarnaast geldt bij legale bookmakers een netto-stortingsgrens van €300 per maand tot 24 jaar en €700 daarna, per aanbieder.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    html = content + content2 + content3
    assert re.search(r"<(ul|ol|/li)>\s+<", html) is None
    assert "/kennisbank/" not in html and "<h2" not in html and "<h4" not in html and "/go/" not in html
    assert html.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert len(OG_CHIPS) == 2 and len(OG_DATA) == 4 and html.count("<table") >= 2
    for link in (STORTING, MARTINGALE, GOKVERSLAVING, VALUE, ODDS, CRUKS, LEGAAL, "/wedgids"):
        assert f'href="{link}"' in html, link
    assert all(h.startswith("<h3><strong>") for h in re.findall(r"<h3>.{0,12}", html))
    faq = content3.split("Veelgestelde vragen")[1]
    assert 4 <= faq.count("<p><strong>") <= 6
    tekst = re.sub(r"<[^>]+>", " ", html)
    woorden = len(tekst.split())
    assert 1200 <= woorden <= 2200, woorden
    for (n, p), v in sorted(M.items()):
        print(f"{n:14} p={p}: mediaan €{v[0]}, helft kwijt {v[1]}%, in de plus {v[2]}%")
    print(f"kans reeks van 6 in 100 (47,5%): {pct(P_REEKS, 1)} | (52%): {pct(P_REEKS_MET, 1)}")
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", woorden, "woorden |",
          [len(re.sub(r"<[^>]+>", " ", c).split()) for c in (content, content2, content3)])
    # Publiceren alleen na akkoord van Jasper, via: wg_publiceer.py bankroll-management --live
