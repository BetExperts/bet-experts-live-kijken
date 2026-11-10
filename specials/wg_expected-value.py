# -*- coding: utf-8 -*-
"""NIEUW wedgids-artikel (Nieuws, nog geen item): wat is expected value (EV) bij wedden?
Slug wat-is-expected-value-ev-bij-wedden (gaf HTTP 404 op 10-11-2026, dus vrij; ook wat-is-expected-value gaf 404).
Rubriek Speluitleg, wedgids-categorie 'Wedstrategieën'. Onderwerp: Engelstalige analysesite (alleen het onderwerp).
Zoekwoorden: 'expected value' / 'expected value betekenis' (hoofd), 'expected value berekenen', 'wat is ev wedden',
'+EV weddenschap', 'verwachte waarde weddenschap', 'positieve verwachtingswaarde'.

Afbakening t.o.v. /nieuws/wat-is-de-wedstrategie-value-betting (gelezen met curl op 10-11-2026): dat artikel behandelt al
impliciete kans, EV = kans x odd - 1 (voorbeelden 50%/2,40 en 52%/1,80), marge eruit halen (2,10/3,40/3,60), kans op verlies
bij 6% en 2% voordeel tegen odd 2,00, Kelly en kort closing line value. Hier dus GEEN herhaling daarvan, maar dieper:
EV in euro's en de twee vormen van de formule, break-even-kans, waarom de marge elke uitkomst even -EV maakt (1/som - 1),
combi's (marge stapelt), zelfde EV maar andere schommelingen bij lage vs hoge odds (exacte binomiale kansen, verliesreeksen),
EV van free bets en boosts (ook een boost die -EV blijft), gevoeligheid van EV voor je kansschatting, verwachte kosten van
recreatief wedden. Andere voorbeelden en getallen dan in het value-artikel.

Feiten nagelopen op 10-11-2026 (bronnen NIET in de tekst genoemd):
- Het rekenwerk is wiskunde (verwachtingswaarde, binomiale verdeling); alles hieronder berekend en ge-assert.
- Free bet: inzet komt niet terug, je krijgt alleen de winst (TOTO-voorwaarden, nagelopen in wg_free-bet.py op 22-10-2026).
  Rekenmodel waarde free bet gelijk aan wg_free-bet.py: kans = 0,95 / quotering (5% marge).
- Bonussen alleen vanaf 24 jaar bij o.a. TOTO, Unibet en bet365 (nagelopen in wg_free-bet.py op 22-10-2026; Besluit werving,
  reclame en verslavingspreventie kansspelen art. 2 lid 4 onder a: werving niet gericht op 18-24 jaar).
- Kabinet wil bonussen verbieden: rijksoverheid.nl/actueel/nieuws/2026/06/12/kabinet-scherpt-beleid-online-kansspelen-flink-aan
  (gelezen 10-11-2026): 'het aanbieden van bonussen wordt verboden'; uitwerking in een wetsvoorstel, geen datum genoemd.
- Kansspelbelasting 37,8% in 2026 en draagt de vergunde aanbieder af (zoals in het value-artikel / kansspelbelasting-artikel).
Bewust weggelaten: Kelly-criterium en marge-verwijderen in detail (staat al in het value-artikel), welke bookmaker welke marge
heeft (wisselt per markt en dag, niet betrouwbaar te onderbouwen), 'favourite-longshot bias' (niet nagelopen voor NL-markten),
closing line value in detail (eigen artikel wg_closing-line-value.py; link pas toevoegen als dat live staat).
Alle quoteringen en kansen in de voorbeelden zijn fictief.
Interne links gecontroleerd met curl op 10-11-2026: alle HTTP 200 (zie de asserts).
  ../superodd-agent/.venv/bin/python specials/wg_publiceer.py expected-value   (dry run)"""
import os, sys, re
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

ITEM_ID = None   # nieuw artikel
SLUG = "wat-is-expected-value-ev-bij-wedden"
RUBRIEK = "6502b66cd9992658b4037cf5"   # Speluitleg
WEDGIDS_CAT = "Wedstrategieën"
TITEL = "Expected value (EV) bij wedden: uitleg en formule"
SAMENVATTING = ("Wat is expected value (EV) bij wedden? De formule met decimale odds, rekenvoorbeelden, waarom de marge "
                "je EV negatief maakt en wat free bets doen.")

OG_KOP = "Wat is <span>expected value</span>?"
OG_EYEBROW = "EV bij wedden uitgelegd"
OG_CHIPS = ["Formule met decimale odds", "Met rekenvoorbeelden"]
OG_MOTIEF = "tabel"
OG_DATA = ["EV = kans × odd − 1", "54% op 1,95 · +5,3%", "Marge 5,3% · EV −5,0%", "Free bet €10 op 3,00 · €6,33"]

VALUE = "/nieuws/wat-is-de-wedstrategie-value-betting"
ODDS = "/nieuws/odds-uitgelegd-quotering-lezen"
FREEBET = "/nieuws/wat-is-een-free-bet"
BOOST = "/nieuws/wat-is-een-superboost-of-superodd"
XG = "/nieuws/wat-is-xg-expected-goals"
ARB = "/nieuws/wat-is-arbitrage-wedden-de-kunst-van-de-risicovrije-winst"
LIMIET = "/nieuws/netto-stortingslimiet"
CRUKS = "/nieuws/cruks-de-gokstop-voor-verantwoord-gokken"
VERG = "/odds-vergelijken-bij-alle-bookmakers-beste-odds-vandaag"
LINKS = (VALUE, ODDS, FREEBET, BOOST, XG, ARB, LIMIET, CRUKS, VERG, "/speel-bewust/verantwoord-wedden", "/wedgids")


def k(x, n=2):
    return f"{x:.{n}f}".replace(".", ",")


def pct(x, n=1):
    return f"{100 * x:.{n}f}".replace(".", ",") + "%"


def spct(x, n=1):
    return ("+" if x >= 0 else "−") + pct(abs(x), n)


def eur(x):
    return f"€{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def seur(x):
    return ("+" if x >= 0 else "−") + eur(abs(x))


def ev(p, o):
    """EV per euro inzet."""
    return p * o - 1


# ---- 1. muntworp: bekende kans van 50% ----
INZ = 10
EV_MUNT_HOOG, EV_MUNT_LAAG = INZ * ev(0.5, 2.10), INZ * ev(0.5, 1.90)
assert seur(EV_MUNT_HOOG) == "+€0,50" and seur(EV_MUNT_LAAG) == "−€0,50"
# twee vormen van de formule zijn gelijk
assert abs(0.5 * (2.10 - 1) * INZ - 0.5 * INZ - EV_MUNT_HOOG) < 1e-9

# ---- 2. over 2,5 op 1,95, eigen kans 54% ----
P_O, O_O = 0.54, 1.95
WINST_O, VERLIES_O = P_O * (O_O - 1) * INZ, (1 - P_O) * INZ
EV_O = WINST_O - VERLIES_O
assert (eur(WINST_O), eur(VERLIES_O), seur(EV_O), spct(ev(P_O, O_O))) == ("€5,13", "€4,60", "+€0,53", "+5,3%")
BREAK_O = 1 / O_O
assert pct(BREAK_O) == "51,3%"

# ---- 3. marge: 1X2 met 1,85 / 3,60 / 4,20 ----
ODDS_1X2 = [("Thuiswinst", 1.85), ("Gelijkspel", 3.60), ("Uitwinst", 4.20)]
SOM = sum(1 / o for _, o in ODDS_1X2)
assert pct(SOM) == "105,6%"
RIJEN_MARGE = []
for naam, o in ODDS_1X2:
    eerlijk = (1 / o) / SOM
    RIJEN_MARGE.append((naam, k(o), pct(1 / o), pct(eerlijk), spct(ev(eerlijk, o))))
    assert spct(ev(eerlijk, o)) == "−5,3%"   # elke uitkomst even negatief: 1/som - 1
assert spct(1 / SOM - 1) == "−5,3%"
# twee-weg 1,90 / 1,90 en een combi van drie
EV_2W = 1 / (2 / 1.90) - 1
EV_COMBI3 = (1 + EV_2W) ** 3 - 1
assert spct(EV_2W) == "−5,0%" and spct(EV_COMBI3) == "−14,3%"
assert eur(-INZ * EV_COMBI3 * 10) == "€14,26"   # verwacht verlies op 10 combi's van €10


# ---- 4. zelfde EV, andere schommelingen: 1,50 (70%) vs 3,50 (30%) ----
def kans_verlies(p, o, n):
    """Exacte kans dat je na n weddenschappen van 1 eenheid in de min staat (binomiaal)."""
    d = [1.0]
    for _ in range(n):
        nd = [0.0] * (len(d) + 1)
        for i, v in enumerate(d):
            nd[i] += v * (1 - p); nd[i + 1] += v * p
        d = nd
    return sum(v for w, v in enumerate(d) if w * (o - 1) - (n - w) < -1e-9)


def kans_reeks(p_verlies, n, lengte):
    """Kans op minstens één reeks van `lengte` verliezen op rij in n weddenschappen."""
    st = [0.0] * lengte; st[0] = 1.0; raak = 0.0
    for _ in range(n):
        nw = [0.0] * lengte
        for i, v in enumerate(st):
            nw[0] += v * (1 - p_verlies)
            if i + 1 >= lengte: raak += v * p_verlies
            else: nw[i + 1] += v * p_verlies
        st = nw
    return raak


LAAG, HOOG = (0.70, 1.50), (0.30, 3.50)
assert spct(ev(*LAAG)) == spct(ev(*HOOG)) == "+5,0%"
NS = (100, 500, 2000)
VL = {n: kans_verlies(*LAAG, n) for n in NS}
VH = {n: kans_verlies(*HOOG, n) for n in NS}
assert [pct(VL[n], 0) for n in NS] == ["22%", "5%", "0%"] and VL[2000] < 0.005
assert [pct(VH[n], 0) for n in NS] == ["38%", "23%", "8%"]
RIJEN_VAR = [(f"{n:,}".replace(",", "."), eur(n * INZ * 0.05), pct(VL[n], 0) if VL[n] >= 0.005 else "minder dan 1%", pct(VH[n], 0))
             for n in NS]
REEKS10 = kans_reeks(0.70, 500, 10)
assert pct(0.70 ** 10) == "2,8%" and pct(REEKS10, 0) == "99%"

# ---- 5. free bet en boosts ----
FB = 10


def fb_waarde(o, marge=0.95):
    return FB * (o - 1) * marge / o


RIJEN_FB = [(k(o), pct(0.95 / o), eur(FB * (o - 1)), eur(fb_waarde(o))) for o in (1.50, 3.00, 6.00)]
assert [eur(fb_waarde(o)) for o in (1.50, 3.00, 6.00)] == ["€3,17", "€6,33", "€7,92"]
B_P, B_N, B_B = 0.50, 1.85, 2.05
assert (spct(ev(B_P, B_N)), spct(ev(B_P, B_B))) == ("−7,5%", "+2,5%")
BB_P, BB_N, BB_B = 0.20, 4.00, 4.50
assert (pct(1 / BB_N, 0), spct(ev(BB_P, BB_N), 0), spct(ev(BB_P, BB_B), 0)) == ("25%", "−20%", "−10%")

# ---- 6. gevoeligheid: odd 2,10 ----
G_O = 2.10
RIJEN_GEV = [(pct(p, 0), spct(ev(p, G_O)), seur(INZ * ev(p, G_O))) for p in (0.52, 0.50, 0.48, 0.46)]
assert [spct(ev(p, G_O)) for p in (0.52, 0.50, 0.48, 0.46)] == ["+9,2%", "+5,0%", "+0,8%", "−3,4%"]
assert pct(1 / G_O) == "47,6%"

# ---- 7. verwachte kosten recreatief wedden ----
KOSTEN = 52 * INZ * abs(EV_2W)
assert eur(KOSTEN) == "€26,00"

content = f"""<p><strong>Expected value (EV), in het Nederlands verwachte waarde, is wat een weddenschap je gemiddeld oplevert als je hem heel vaak zou plaatsen. Met decimale odds reken je het zo uit: EV = inzet × (kans × odd − 1). Is de uitkomst positief (+EV), dan win je op lange termijn gemiddeld geld; is hij negatief (−EV), dan verlies je gemiddeld. Door de marge van de bookmaker zijn de meeste weddenschappen −EV, en het lastige is dat niemand de echte kans precies kent.</strong></p>
<p>EV is het belangrijkste begrip achter elke serieuze wedstrategie. In ons artikel over <a href="{VALUE}">value betting</a> lees je hoe je value zoekt. Hier gaan we dieper in op de rekenkunde zelf: de formule in twee vormen, waarom de marge je EV omlaag drukt, waarom twee weddenschappen met dezelfde EV heel anders kunnen verlopen en wat free bets en boosts met je EV doen. <em>Alle quoteringen en kansen in de voorbeelden zijn fictief.</em></p>
<h3><strong>Wat betekent expected value precies?</strong></h3>
<p>EV is een gewogen gemiddelde. Je neemt elke mogelijke uitkomst, vermenigvuldigt wat je dan wint of verliest met de kans dat die uitkomst valt, en telt alles op. Het resultaat is geen bedrag dat je bij één weddenschap krijgt, maar het gemiddelde per weddenschap over heel veel herhalingen.</p>
<p>Het simpelste voorbeeld is een eerlijke munt. De kans op kop is precies 50%. Biedt iemand je {k(2.10)} op kop en zet je {eur(INZ)} in, dan win je de helft van de keren {eur(INZ * 1.10)} en verlies je de helft van de keren {eur(INZ)}. Je EV is 0,5 × {eur(INZ * 1.10)} − 0,5 × {eur(INZ)} = {seur(EV_MUNT_HOOG)} per worp. Krijg je maar {k(1.90)}, dan is je EV {seur(EV_MUNT_LAAG)}. Na één worp merk je daar niets van, na duizend worpen wel.</p>
<h3><strong>Hoe bereken je EV met decimale odds?</strong></h3>
<p>Er zijn twee vormen van dezelfde formule. Gebruik de vorm die voor jou het meest logisch voelt:</p>
<ul><li><strong>Uitgeschreven:</strong> EV = kans × winst bij winst − (1 − kans) × inzet. De winst bij winst is inzet × (odd − 1).</li><li><strong>Kort:</strong> EV = inzet × (kans × odd − 1). Laat je de inzet weg, dan krijg je de EV per euro, als percentage.</li></ul>
<p><strong>Rekenvoorbeeld:</strong> je zet {eur(INZ)} op meer dan 2,5 doelpunten tegen een odd van {k(O_O)}. Jij schat de kans op {pct(P_O, 0)}.</p>
{tabel(["Stap", "Berekening", "Uitkomst"], [
    ("Gemiddelde winst", f"{pct(P_O, 0)} × {eur(INZ)} × ({k(O_O)} − 1)", eur(WINST_O)),
    ("Gemiddeld verlies", f"{pct(1 - P_O, 0)} × {eur(INZ)}", eur(VERLIES_O)),
    ("<strong>EV per weddenschap</strong>", f"{eur(WINST_O)} − {eur(VERLIES_O)}", f"<strong>{seur(EV_O)}</strong>"),
    ("<strong>EV in procenten</strong>", f"{k(P_O)} × {k(O_O)} − 1", f"<strong>{spct(ev(P_O, O_O))}</strong>"),
])}
<p>Handig is ook de <strong>break-evenkans</strong>: 1 ÷ odd. Bij {k(O_O)} is dat {pct(BREAK_O)}. Schat je de kans hoger, dan is de weddenschap +EV; schat je hem lager, dan −EV. Hoe je odds omrekent naar kansen, lees je in <a href="{ODDS}">odds uitgelegd</a>.</p>
<h3><strong>Wat is het verschil tussen positieve en negatieve EV?</strong></h3>
<p>Bij <strong>positieve EV (+EV)</strong> is de odd hoger dan de echte kans rechtvaardigt. Bij <strong>negatieve EV (−EV)</strong> is hij lager. Dat staat los van de vraag of je de weddenschap wint: een favoriet op {k(1.30)} kan −EV zijn en een underdog op {k(5.00)} +EV. Een +EV-weddenschap kun je prima verliezen, en een −EV-weddenschap kun je winnen. EV gaat over de prijs, niet over de uitslag.</p>"""

content2 = f"""<h3><strong>Waarom zijn de meeste weddenschappen −EV?</strong></h3>
<p>Een bookmaker zet zijn odds iets lager dan de echte kansen. Tel je de impliciete kansen van alle uitkomsten op, dan kom je boven de 100% uit. Het deel daarboven is de marge. Neem een wedstrijd met deze odds:</p>
{tabel(["Uitkomst", "Odd", "Impliciete kans", "Kans zonder marge", "EV"], RIJEN_MARGE + [("<strong>Totaal</strong>", "", f"<strong>{pct(SOM)}</strong>", "<strong>100,0%</strong>", "")])}
<p>Stel dat de bookmaker de kansen precies goed inschat en alleen de marge erbij doet. Dan is elke uitkomst even slecht: {spct(1 / SOM - 1)} EV, wat je ook kiest. Dat is geen toeval. Met deze manier van rekenen is de EV van elke uitkomst 1 ÷ {k(SOM, 3)} − 1. Kies je 'blind' een uitkomst bij één bookmaker, dan betaal je dus gemiddeld de marge.</p>
<p>Bij <strong>combinaties</strong> stapelt de marge. Een markt met {k(1.90)} op beide kanten heeft {spct(EV_2W)} EV per selectie. Zet je drie van zulke selecties in één combi, dan is de EV {spct(EV_COMBI3)}. Tien van die combi's van {eur(INZ)} kosten je gemiddeld {eur(-INZ * EV_COMBI3 * 10)}, tegen {eur(-INZ * EV_2W * 10)} voor tien losse weddenschappen.</p>
<p>+EV vind je dus alleen als een odd hoger is dan de echte kans. Dat kan als je de kans beter inschat dan de bookmaker, als één bookmaker afwijkt van de rest (vergelijk met onze <a href="{VERG}">odds vergelijker</a>) of via een actie zoals een free bet of boost. Bij <a href="{ARB}">arbitrage</a> combineer je odds van verschillende bookmakers zo dat de uitslag er niet meer toe doet.</p>
<h3><strong>Waarom kun je met +EV toch lang verliezen?</strong></h3>
<p>EV is een gemiddelde over de lange termijn. Op korte termijn bepaalt toeval bijna alles, en hoe hoger de odds, hoe groter de schommelingen. Vergelijk twee weddenschappen met precies dezelfde EV van {spct(ev(*LAAG))}: een odd van {k(LAAG[1])} met {pct(LAAG[0], 0)} kans en een odd van {k(HOOG[1])} met {pct(HOOG[0], 0)} kans. Je zet steeds {eur(INZ)} in.</p>
{tabel(["Aantal weddenschappen", "Verwachte winst", f"Kans op verlies bij {k(LAAG[1])}", f"Kans op verlies bij {k(HOOG[1])}"], RIJEN_VAR)}
<p>De verwachte winst is in beide gevallen gelijk, maar bij {k(HOOG[1])} sta je na 500 weddenschappen in bijna een kwart van de gevallen nog in de min. Ook lange verliesreeksen horen erbij. De kans dat tien weddenschappen op {k(HOOG[1])} achter elkaar verliezen, is {pct(0.70 ** 10)}. Toch krijg je over 500 weddenschappen zo'n reeks in {pct(REEKS10, 0)} van de gevallen minstens één keer. Wie dan stopt of zijn inzet verhoogt om het terug te winnen, haalt zijn eigen strategie onderuit.</p>
<p>Daarom zegt een maand winst of verlies weinig over je EV. Ervaren wedders kijken daarom ook naar de slotkoers: krijg je structureel een hogere odd dan vlak voor de aftrap, dan is dat een eerder teken van +EV dan je resultaat.</p>
<h3><strong>Hoe veranderen free bets en boosts je EV?</strong></h3>
<p>Bij een <a href="{FREEBET}">free bet</a> krijg je je inzet niet terug, alleen de winst. De EV is dan kans × inzet × (odd − 1); er staat geen verlies tegenover, want het was niet jouw geld. Daardoor is een free bet op een hogere odd gemiddeld meer waard. Hieronder een free bet van {eur(FB)}, uitgaande van een marge van 5%:</p>
{tabel(["Odd", "Kans (na marge)", "Winst als hij valt", "Verwachte waarde"], RIJEN_FB)}
<p>Een <a href="{BOOST}">odds boost</a> verhoogt de odd terwijl de kans gelijk blijft. Schat je een uitkomst op {pct(B_P, 0)} en gaat de odd van {k(B_N)} naar {k(B_B)}, dan gaat je EV van {spct(ev(B_P, B_N))} naar {spct(ev(B_P, B_B))}. Niet elke boost is +EV. Rekent een bookmaker op een bet builder met {pct(1 / BB_N, 0)} kans (odd {k(BB_N)}) terwijl de echte kans {pct(BB_P, 0)} is, dan maakt een boost naar {k(BB_B)} de EV alleen minder slecht: van {spct(ev(BB_P, BB_N), 0)} naar {spct(ev(BB_P, BB_B), 0)}.</p>
<p>Free bets en andere bonussen zijn in Nederland alleen voor spelers van 24 jaar en ouder, en ze hebben vaak voorwaarden die de waarde verlagen, zoals een minimale odd of een korte geldigheid. Het kabinet heeft bovendien aangekondigd dat het bonussen wil verbieden; dat moet nog in een wet worden uitgewerkt.</p>"""

content3 = f"""<h3><strong>Waarom is de echte kans het moeilijkste deel?</strong></h3>
<p>De formule is simpel, maar alles hangt af van één getal: de kans die jij invult. En die kent niemand precies. Kleine fouten maken een groot verschil. Zo ziet de EV van {eur(INZ)} op een odd van {k(G_O)} eruit bij verschillende inschattingen:</p>
{tabel(["Jouw kans", "EV", f"Per {eur(INZ)}"], RIJEN_GEV)}
<p>Een verschil van maar 4 procentpunt in je inschatting draait een weddenschap van {spct(ev(0.50, G_O))} naar {spct(ev(0.46, G_O))}. De break-evenkans ligt hier op {pct(1 / G_O)}. Zit je schatting daar net boven, dan is je 'value' vooral een kwestie van hoe zeker je van je eigen kans bent.</p>
<p>Hoe kom je dan aan een goede schatting?</p>
<ul><li><strong>Gebruik de markt als ijkpunt.</strong> De odds van meerdere bookmakers samen, met de marge eruit gehaald, zijn vaak al een sterke schatting. Wijkt jouw kans daar ver van af, vraag je dan eerst af wat jij weet dat de markt niet weet.</li><li><strong>Werk met een model.</strong> Bijvoorbeeld op basis van <a href="{XG}">expected goals (xG)</a>, vorm en opstellingen. Een model maakt je schattingen consequent en controleerbaar.</li><li><strong>Controleer je kalibratie.</strong> Houd je schattingen bij. Van alle keren dat je 60% zei, moet ongeveer 60% uitkomen. Pas na honderden weddenschappen zie je of dat klopt.</li><li><strong>Wees conservatief.</strong> Ga ervan uit dat je schatting eerder te optimistisch is dan te voorzichtig, zeker bij grote afwijkingen van de markt.</li></ul>
<h3><strong>Wat zegt EV niet?</strong></h3>
<p>EV zegt niets over risico. Twee weddenschappen met dezelfde EV kunnen, zoals je hierboven zag, heel verschillend verlopen. Hoeveel je per keer inzet, bepaalt of je een slechte reeks overleeft. Daarover lees je meer bij <a href="{VALUE}">value betting</a>.</p>
<p>EV helpt ook om eerlijk te kijken naar recreatief wedden. Zet je elke week {eur(INZ)} in op weddenschappen met gemiddeld {spct(EV_2W, 0)} EV, dan kost je dat per jaar gemiddeld zo'n {eur(KOSTEN)}. Dat is prima als je het als entertainment ziet, zolang je het als kosten behandelt en niet als manier om geld te verdienen. Stel daarom een <a href="{LIMIET}">netto-stortingslimiet</a> in en lees onze tips over <a href="/speel-bewust/verantwoord-wedden">verantwoord wedden</a>; merk je dat het niet meer lukt om te stoppen, dan kun je je inschrijven in <a href="{CRUKS}">Cruks</a>.</p>
<p>Wedden bij een bookmaker met een vergunning van de Kansspelautoriteit heeft nog een voordeel: de aanbieder draagt de kansspelbelasting af, dus over je winst betaal je zelf niets. Meer uitleg over wedden vind je in de <a href="/wedgids">wedgids</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wat betekent expected value bij wedden?</strong><br>Expected value (EV) of verwachte waarde is wat een weddenschap gemiddeld oplevert als je hem heel vaak zou plaatsen. Positief betekent gemiddeld winst, negatief gemiddeld verlies.</p>
<p><strong>Hoe bereken ik EV met decimale odds?</strong><br>EV = inzet × (kans × odd − 1). Bij {pct(P_O, 0)} kans, odd {k(O_O)} en {eur(INZ)} inzet is dat {eur(INZ)} × ({k(P_O)} × {k(O_O)} − 1) = {seur(EV_O)}.</p>
<p><strong>Wat betekent +EV?</strong><br>Een +EV-weddenschap heeft een odd die hoger is dan de echte kans rechtvaardigt. Je kunt hem nog steeds verliezen; het voordeel zie je pas over honderden weddenschappen.</p>
<p><strong>Is een free bet altijd +EV?</strong><br>Ja, omdat je je eigen geld niet inzet, is de verwachte waarde altijd positief. Hoe hoog hangt af van de odd: een free bet van {eur(FB)} op {k(3.00)} is gemiddeld ongeveer {eur(fb_waarde(3.00))} waard, op {k(1.50)} maar {eur(fb_waarde(1.50))}.</p>
<p><strong>Garandeert positieve EV winst?</strong><br>Nee. EV is een gemiddelde. Op korte termijn kun je met +EV verliezen, en of je weddenschap echt +EV is, hangt af van een kansschatting die nooit zeker is.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    html = content + content2 + content3
    assert re.search(r"<(ul|ol|/li)>\s+<", html) is None
    assert "/kennisbank/" not in html and "<h2" not in html and "<h4" not in html and "/go/" not in html
    assert html.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert content.startswith("<p><strong>")
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert len(OG_CHIPS) == 2 and len(OG_DATA) == 4
    for link in LINKS:
        assert f'href="{link}"' in html, link
    assert set(re.findall(r'href="([^"]+)"', html)) <= set(LINKS)
    faq = content3.split("Veelgestelde vragen")[1]
    assert 4 <= faq.count("<p><strong>") <= 6
    woorden = len(re.sub(r"<[^>]+>", " ", html).split())
    assert 1200 <= woorden <= 2200, woorden
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", woorden, "woorden")
assert OG_DATA[1].endswith(spct(ev(P_O, O_O))) and OG_DATA[2] == f"Marge {pct(2 / 1.90 - 1)} · EV {spct(EV_2W)}" and OG_DATA[3].endswith(eur(fb_waarde(3.00)))
