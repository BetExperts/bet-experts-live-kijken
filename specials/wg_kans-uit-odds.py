# -*- coding: utf-8 -*-
"""NIEUW wedgids-artikel (Nieuws, nog geen item): kans berekenen uit odds, impliciete kans en eerlijke odds.
Slug kans-berekenen-uit-odds-impliciete-kans (gaf HTTP 404 op 10-11-2026, dus vrij). Rubriek Speluitleg,
wedgids-categorie 'Wedden uitgelegd'. Onderwerp: Engelstalige analysesite (alleen het onderwerp, niets overgenomen).
Zoekwoorden: 'kans berekenen odds' / 'odds naar kans' (hoofd), 'impliciete kans', 'eerlijke odds', 'marge uit odds halen',
'devig' / 'odds zonder marge', 'odds omrekenen naar percentage', 'kans berekenen weddenschap', 'value berekenen'.

Afbakening t.o.v. /nieuws/odds-uitgelegd-quotering-lezen (gecontroleerd met curl op 10-11-2026, HTTP 200): dat artikel
geeft 1 ÷ odd en één proportioneel rekenvoorbeeld (fictief). Dit artikel gaat dieper: omrekentabel mét kans zonder marge,
de marge eruit halen met echte odds (1X2 én tweeweg), proportioneel vs. power-methode (+ additief en Shin genoemd),
eerlijke odds, eigen kans vergelijken (verwachte waarde, minimale odd, kans op verlies na 100 weddenschappen) en combi's.

Feiten (bron + datum):
- ECHTE ODDS 711: publieke Kambi-feed van 711 (brand sevelevnl), gelezen op 10-11-2026 om 14:34 uur (CET):
  eu-offering-api.kambicdn.com/offering/v2018/sevelevnl/listView/football/netherlands/eredivisie.json?lang=nl_NL&market=NL&useCombined=true
  Sparta Rotterdam - AZ (zo 22-11-2026 13:30 UTC = 14:30 uur NL): 1X2 4,60 / 4,40 / 1,71.
  FC Groningen - SC Heerenveen (za 21-11-2026 21:00 uur NL): over/onder 3,5 doelpunten 1,96 / 1,81.
  Feyenoord - Excelsior 1,19/8,00/14,00; Ajax - ADO Den Haag 1,19/8,50/15,00; FC Twente - Willem II 1,09/12,50/31,00.
- Power-methode: kansen p_i = (1/odd_i)^k met k zo dat de som 1 is (bisectie hieronder). Additieve methode: marge gelijk
  over de uitkomsten aftrekken. Shin-methode (H.S. Shin, model met wedders met voorkennis): alleen genoemd.
- Favoriet-outsider-bias (favourite-longshot bias): algemeen beschreven verschijnsel in de literatuur over wedmarkten;
  in de tekst bewust voorzichtig geformuleerd ('veel onderzoek vindt ... gemiddeld').
- Eigen inschatting 62% voor AZ is fictief (gemarkeerd). Kans op verlies na 100 weddenschappen: binomiaal, berekend.
Alle getallen hieronder berekend en ge-assert.

Bewust weggelaten:
- Geen formules van de Shin-methode (te technisch voor de doelgroep), geen breuken/Amerikaanse odds (staat in odds-uitgelegd).
- Geen claims over welke bookmaker de beste/laagste odds heeft; geen bron van het onderwerp genoemd.
- Geen link naar het nieuwe marge-artikel (bookmaker-marge), want dat staat nog niet live: na publicatie onderling linken.
Interne links gecontroleerd op 10-11-2026 (curl, allemaal HTTP 200): zie de asserts onderaan.
Geen INFOGRAPHIC (odds-uitgelegd heeft al een spiekbriefje; de tabellen volstaan).
  ../superodd-agent/.venv/bin/python specials/wg_publiceer.py kans-uit-odds [--live]"""
import os, sys, re
from math import comb
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
import lk_webflow as WF
from legaal_data import tabel

ITEM_ID = None   # nieuw artikel
SLUG = "kans-berekenen-uit-odds-impliciete-kans"
RUBRIEK = "6502b66cd9992658b4037cf5"   # Speluitleg
WEDGIDS_CAT = "Wedden uitgelegd"
TITEL = "Kans berekenen uit odds: impliciete kans en eerlijke odds"
SAMENVATTING = ("Zo bereken je de kans uit odds: impliciete kans, de marge eruit halen en eerlijke odds. Met echte "
                "voorbeelden, een omrekentabel en value berekenen.")

ODDS = "/nieuws/odds-uitgelegd-quotering-lezen"
VALUE = "/nieuws/wat-is-de-wedstrategie-value-betting"
XG = "/nieuws/wat-is-xg-expected-goals"
ARB = "/nieuws/wat-is-arbitrage-wedden-de-kunst-van-de-risicovrije-winst"
ACCA = "/nieuws/uitleg-wedstrategie-accumulator-weddenschappen"
VERGELIJK = "/odds-vergelijken-bij-alle-bookmakers-beste-odds-vandaag"
DNB = "/nieuws/wat-betekent-ongeldig-bij-gelijkspel"
OU = "/nieuws/over-under-uitleg-over-2-5-goals"
LEGAAL = "/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland"
LIMIET = "/nieuws/netto-stortingslimiet"
BEWUST = "/speel-bewust/verantwoord-wedden"
BM711 = '<a href="/bookmakers/711">711</a>'
GELEZEN = "10 november 2026 om 14:34 uur"


def q(x):
    return f"{x:.2f}".replace(".", ",")


def pct(x, d=1):
    return f"{100 * x:.{d}f}%".replace(".", ",")


def eur(x):
    return f"€{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def proportioneel(odds):
    imp = [1 / o for o in odds]
    s = sum(imp)
    return [p / s for p in imp]


def power(odds):
    """Kansen (1/odd)^k, k zo gekozen dat ze samen 1 zijn."""
    imp = [1 / o for o in odds]
    lo, hi = 1.0, 3.0
    for _ in range(200):
        k = (lo + hi) / 2
        if sum(p ** k for p in imp) > 1:
            lo = k
        else:
            hi = k
    return [p ** k for p in imp], k


# ---- omrekentabel: odd -> impliciete kans, en zonder 3% / 6% marge (proportioneel) ----
LIJST = [1.10, 1.25, 1.33, 1.40, 1.50, 1.60, 1.71, 1.80, 1.91, 2.00, 2.20, 2.50, 3.00, 3.50, 4.00, 5.00, 6.00, 8.00, 10.00, 15.00]
RIJEN_OMREKEN = [(f"<strong>{q(o)}</strong>", pct(1 / o), pct(1 / o / 1.03), pct(1 / o / 1.06)) for o in LIJST]
I = {q(o): r for o, r in zip(LIJST, RIJEN_OMREKEN)}
assert I["2,00"][1:] == ("50,0%", "48,5%", "47,2%")
assert I["1,71"][1:] == ("58,5%", "56,8%", "55,2%")
assert I["1,10"][1] == "90,9%" and I["15,00"][1:] == ("6,7%", "6,5%", "6,3%")

# ---- echte odds 711: Sparta - AZ ----
SA = [4.60, 4.40, 1.71]
SA_IMP = [1 / o for o in SA]
SA_SOM = sum(SA_IMP)
SA_P = proportioneel(SA)
SA_POW, K = power(SA)
assert [pct(p) for p in SA_IMP] == ["21,7%", "22,7%", "58,5%"] and pct(SA_SOM, 2) == "102,95%"
assert [pct(p) for p in SA_P] == ["21,1%", "22,1%", "56,8%"] and [q(1 / p) for p in SA_P] == ["4,74", "4,53", "1,76"]
assert abs(sum(SA_POW) - 1) < 1e-9 and [pct(p) for p in SA_POW] == ["20,7%", "21,7%", "57,5%"]
assert [q(1 / p) for p in SA_POW] == ["4,82", "4,60", "1,74"] and f"{K:.3f}" == "1.031"
SA_ADD = [p - (SA_SOM - 1) / 3 for p in SA_IMP]
assert [pct(p) for p in SA_ADD] == ["20,8%", "21,7%", "57,5%"]
UITK = ("Sparta wint", "Gelijk", "AZ wint")
RIJEN_SA = [(f"<strong>{u}</strong>", q(o), pct(i), pct(p), q(1 / p)) for u, o, i, p in zip(UITK, SA, SA_IMP, SA_P)]
RIJEN_SA.append(("<strong>Totaal</strong>", "", f"<strong>{pct(SA_SOM)}</strong>", "<strong>100,0%</strong>", ""))
RIJEN_METHODE = [(f"<strong>{u}</strong>", q(o), pct(p), q(1 / p), pct(w), q(1 / w)) for u, o, p, w in zip(UITK, SA, SA_P, SA_POW)]

# ---- tweeweg: over/onder 3,5 bij FC Groningen - sc Heerenveen ----
OV, ON = 1.96, 1.81
OU_SOM = 1 / OV + 1 / ON
P_OV, P_ON = proportioneel([OV, ON])
assert (pct(1 / OV), pct(1 / ON), pct(OU_SOM)) == ("51,0%", "55,2%", "106,3%")
assert (pct(P_OV), pct(P_ON), q(1 / P_OV), q(1 / P_ON)) == ("48,0%", "52,0%", "2,08", "1,92")

# ---- jouw kans vs de odd: AZ (fictieve eigen inschatting 62%) ----
JIJ, ODD_AZ, INZET, N = 0.62, 1.71, 10, 100
EV = JIJ * ODD_AZ - 1
assert pct(EV) == "6,0%" and q(1 / JIJ) == "1,61" and pct(1 / ODD_AZ) == "58,5%"
assert eur(N * INZET * EV) == "€60,20"
NODIG = next(w for w in range(N + 1) if w * ODD_AZ - N >= 0)      # winsten nodig om niet in de min te staan
P_VERLIES = sum(comb(N, w) * JIJ ** w * (1 - JIJ) ** (N - w) for w in range(NODIG))
assert NODIG == 59 and pct(P_VERLIES, 0) == "23%"
assert pct(JIJ - SA_P[2]) == "5,2%"

# ---- kans -> eerlijke odd -> minimale odd voor 5% value ----
KANSEN = [0.10, 0.20, 0.25, 0.30, 0.40, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.90]
RIJEN_KANS = [(f"<strong>{pct(p, 0)}</strong>", q(1 / p), q(1.05 / p)) for p in KANSEN]
KI = {r[0]: r for r in RIJEN_KANS}
assert KI["<strong>50%</strong>"][1:] == ("2,00", "2,10") and KI["<strong>60%</strong>"][1:] == ("1,67", "1,75")
assert KI["<strong>25%</strong>"][1:] == ("4,00", "4,20")

# ---- combi: drie favorieten, kans zonder marge vermenigvuldigen ----
FAV = [("Feyenoord", [1.19, 8.00, 14.00]), ("Ajax", [1.19, 8.50, 15.00]), ("FC Twente", [1.09, 12.50, 31.00])]
C_ODD = FAV[0][1][0] * FAV[1][1][0] * FAV[2][1][0]
C_FAIR = [proportioneel(o)[0] for _, o in FAV]
C_P = C_FAIR[0] * C_FAIR[1] * C_FAIR[2]
assert q(C_ODD) == "1,54" and pct(1 / C_ODD) == "64,8%"
assert [pct(p) for p in C_FAIR] == ["81,1%", "82,0%", "89,1%"] and pct(C_P) == "59,2%" and q(1 / C_P) == "1,69"

OG_KOP = "Kans berekenen uit <span>odds</span>"
OG_EYEBROW = "Impliciete kans en eerlijke odds"
OG_CHIPS = ["Met omrekentabel", "Marge eruit rekenen"]
OG_MOTIEF = "tabel"
OG_DATA = [f"Odd {q(ODD_AZ)} · {pct(1 / ODD_AZ)}", f"Zonder marge · {pct(SA_P[2])}", f"Eerlijke odd · {q(1 / SA_P[2])}",
           f"Jouw kans {pct(JIJ, 0)} · +{pct(EV)}"]
assert OG_DATA == ["Odd 1,71 · 58,5%", "Zonder marge · 56,8%", "Eerlijke odd · 1,76", "Jouw kans 62% · +6,0%"]

content = f"""<p><strong>Je berekent de kans uit een odd met 1 gedeeld door de decimale odd: een odd van {q(ODD_AZ)} staat voor {pct(1 / ODD_AZ)}. Dat is de impliciete kans, inclusief de marge van de bookmaker. Wil je de kans zonder marge, deel dan de impliciete kans van elke uitkomst door het totaal van alle uitkomsten. 1 gedeeld door die kans is de eerlijke odd.</strong></p>
<p>In dit artikel reken je stap voor stap met echte odds van {BM711}, zie je twee manieren om de marge eruit te halen en lees je hoe je jouw eigen inschatting naast de odds legt. Weet je nog niet hoe je een quotering leest of hoe breuken en Amerikaanse odds werken? Lees dan eerst <a href="{ODDS}">odds uitgelegd</a>.</p>
<h3><strong>Wat is de impliciete kans?</strong></h3>
<p>De impliciete kans is de kans die in een odd 'verstopt' zit. Je rekent hem uit met <strong>kans = 1 ÷ odd</strong>, keer 100 voor een percentage. Bij een odd van 4,00 is dat 1 ÷ 4,00 = {pct(1 / 4)}. Bij {q(ODD_AZ)} is het {pct(1 / ODD_AZ)}.</p>
<p>Je kunt de impliciete kans ook lezen als je break-even punt. Speel je steeds op {q(ODD_AZ)}, dan moet je meer dan {pct(1 / ODD_AZ)} van die weddenschappen winnen om op lange termijn niet te verliezen. Deze tabel zet de gangbare odds om. De laatste twee kolommen laten zien wat er overblijft als je een marge van 3% of 6% eruit haalt, ongeveer wat wij maten op de uitslag en op over/onder.</p>
{tabel(["Odd", "Impliciete kans", "Zonder 3% marge", "Zonder 6% marge"], RIJEN_OMREKEN)}
<h3><strong>Waarom is de impliciete kans niet de echte kans?</strong></h3>
<p>Omdat de bookmaker een marge in de odds verwerkt. Daardoor tellen de impliciete kansen van alle uitkomsten samen altijd op tot meer dan 100%. Neem Sparta - AZ, zondag 22 november om 14:30 uur. Bij 711 stond op {GELEZEN}: Sparta {q(SA[0])}, gelijk {q(SA[1])} en AZ {q(SA[2])}. Dat is {pct(SA_IMP[0])} + {pct(SA_IMP[1])} + {pct(SA_IMP[2])} = {pct(SA_SOM)}. De {pct(SA_SOM - 1)} boven de 100% is de marge.</p>
<p>Zelfs zonder marge is een odd geen echte kans, maar een prijs. Die prijs zegt wat de bookmaker en de wedders samen verwachten. Niemand kent de echte kans precies.</p>"""

content2 = f"""<h3><strong>Hoe haal je de marge uit de odds?</strong></h3>
<p>Dit heet in het Engels 'devig' (van vigorish, een ander woord voor marge). De meest gebruikte manier is de proportionele methode, ook wel de multiplicatieve methode genoemd:</p>
<ol><li>Reken elke odd om naar een impliciete kans: 1 ÷ odd.</li><li>Tel de kansen op. Bij Sparta - AZ is dat {pct(SA_SOM)}.</li><li>Deel elke kans door dat totaal. Voor AZ: {pct(SA_IMP[2])} ÷ {pct(SA_SOM)} = {pct(SA_P[2])}.</li><li>De eerlijke odd is 1 ÷ die kans: 1 ÷ {pct(SA_P[2])} = {q(1 / SA_P[2])}.</li></ol>
{tabel(["Uitkomst", "Odd 711", "Impliciete kans", "Kans zonder marge", "Eerlijke odd"], RIJEN_SA)}
<p>Zonder marge zou AZ dus {q(1 / SA_P[2])} betalen in plaats van {q(SA[2])}. De kansen tellen nu precies op tot 100%.</p>
<p><strong>Bij twee uitkomsten werkt het hetzelfde.</strong> Bij FC Groningen - sc Heerenveen stond <a href="{OU}">over 3,5 doelpunten</a> op {q(OV)} en onder op {q(ON)}. Impliciet is dat {pct(1 / OV)} en {pct(1 / ON)}, samen {pct(OU_SOM)}. Zonder marge wordt het {pct(P_OV)} voor over en {pct(P_ON)} voor onder, met eerlijke odds van {q(1 / P_OV)} en {q(1 / P_ON)}.</p>
<h3><strong>Zijn er ook andere methodes?</strong></h3>
<p>Ja. De proportionele methode gaat ervan uit dat de bookmaker de marge eerlijk over alle uitkomsten verdeelt. Dat is niet altijd zo. Veel onderzoek naar wedmarkten vindt dat de odds van grote outsiders gemiddeld te laag zijn in verhouding tot hun echte kans. Dat heet de favoriet-outsider-bias. Andere methodes houden daar rekening mee:</p>
<ul><li><strong>Power-methode:</strong> verheft elke impliciete kans tot dezelfde macht, zo gekozen dat het totaal op 100% uitkomt. Outsiders verliezen daardoor naar verhouding meer kans dan de favoriet.</li><li><strong>Additieve methode:</strong> trekt van elke uitkomst hetzelfde aantal procentpunten af.</li><li><strong>Methode van Shin:</strong> gaat ervan uit dat een deel van de wedders voorkennis heeft en dat de bookmaker zich daartegen indekt. Die is wiskundig zwaarder en vooral nuttig bij markten met grote outsiders.</li></ul>
<p>Voor Sparta - AZ geven de proportionele en de power-methode dit:</p>
{tabel(["Uitkomst", "Odd", "Proportioneel", "Eerlijke odd", "Power", "Eerlijke odd"], RIJEN_METHODE)}
<p>Het verschil is klein: de power-methode geeft AZ {pct(SA_POW[2])} in plaats van {pct(SA_P[2])}. Bij een lage marge en een duel zonder grote outsider maakt de keuze weinig uit. Bij een hoge marge of een odd van 10,00 of hoger loopt het verschil op. Gebruik dan liefst steeds dezelfde methode, zodat je eigen berekeningen onderling te vergelijken zijn.</p>
<h3><strong>Wat zijn eerlijke odds?</strong></h3>
<p>Eerlijke odds, of fair odds, zijn de odds zonder marge: 1 gedeeld door de kans zonder marge. Een bookmaker die eerlijke odds zou aanbieden, verdient op lange termijn niets. Je gebruikt ze als meetlat. Ligt de odd bij een andere bookmaker boven de eerlijke odd die je uit een scherpe markt hebt berekend, dan is dat een aanwijzing dat die odd ruim is. Met onze <a href="{VERGELIJK}">odds vergelijker</a> zie je per wedstrijd de hoogste odds bij legale bookmakers. Tellen de impliciete kansen van de hoogste odds samen op tot minder dan 100%, dan is er een kans op <a href="{ARB}">arbitrage</a>.</p>"""

content3 = f"""<h3><strong>Hoe vergelijk je jouw eigen kans met de odds?</strong></h3>
<p>Stel dat je met je eigen analyse, bijvoorbeeld op basis van <a href="{XG}">xG</a>, vorm en opstellingen, de kans op een zege van AZ op {pct(JIJ, 0)} schat. <em>Die inschatting is fictief.</em> Dan reken je zo:</p>
<ul><li><strong>Jouw eerlijke odd:</strong> 1 ÷ {pct(JIJ, 0)} = {q(1 / JIJ)}. Alles daarboven is volgens jou te ruim geprijsd.</li><li><strong>Verwachte waarde:</strong> jouw kans × odd − 1 = {q(JIJ)} × {q(ODD_AZ)} − 1 = +{pct(EV)}. Per {eur(INZET)} verwacht je gemiddeld {eur(INZET * EV)} winst.</li><li><strong>Vergelijk met de markt:</strong> zonder marge geeft de markt AZ {pct(SA_P[2])}. Jij zit {pct(JIJ - SA_P[2])} hoger. Vraag jezelf af wat jij weet dat de markt niet weet.</li></ul>
<p>Is de verwachte waarde positief, dan heet zo'n weddenschap een value bet. Hoe je daar een aanpak van maakt, lees je in onze uitleg over <a href="{VALUE}">value betting</a>. Deze tabel laat zien welke odd je minimaal nodig hebt bij een bepaalde kans, en welke odd je zou moeten krijgen voor 5% verwachte winst:</p>
{tabel(["Jouw kans", "Eerlijke odd", "Odd voor 5% value"], RIJEN_KANS)}
<p><strong>Ook met value kun je verliezen.</strong> Klopt jouw {pct(JIJ, 0)} precies en speel je {N} keer {eur(INZET)} op {q(ODD_AZ)}, dan verwacht je {eur(N * INZET * EV)} winst. Toch heb je {NODIG} winnende weddenschappen nodig om niet in de min te staan, en de kans dat dat niet lukt is ongeveer {pct(P_VERLIES, 0)}. En zit je eigen inschatting ernaast, dan bestaat de value alleen op papier.</p>
<h3><strong>Hoe bereken je de kans van een combinatie?</strong></h3>
<p>Bij een <a href="{ACCA}">combi</a> moeten alle selecties uitkomen. Staan de wedstrijden los van elkaar, dan vermenigvuldig je de kansen. Drie favorieten van dezelfde speelronde bij 711: {FAV[0][0]} {q(FAV[0][1][0])}, {FAV[1][0]} {q(FAV[1][1][0])} en {FAV[2][0]} {q(FAV[2][1][0])}. De combi-odd is {q(C_ODD)}, een impliciete kans van {pct(1 / C_ODD)}.</p>
<p>Zonder marge zijn de losse kansen {pct(C_FAIR[0])}, {pct(C_FAIR[1])} en {pct(C_FAIR[2])}. Samen is dat {pct(C_P)}, een eerlijke odd van {q(1 / C_P)}. Het verschil tussen {q(C_ODD)} en {q(1 / C_P)} is de marge die zich in de combi opstapelt.</p>
<h3><strong>Waar moet je op letten?</strong></h3>
<ul><li><strong>Markten met één kant.</strong> Biedt een bookmaker alleen 'ja' aan, zoals bij veel spelersmarkten, dan kun je de marge er niet uit halen. De impliciete kans is dan te hoog en je weet niet hoeveel.</li><li><strong>Markten met veel uitkomsten.</strong> Bij correcte score of eerste doelpuntenmaker is de marge zo groot dat een kans zonder marge minder betrouwbaar is.</li><li><strong>Geld terug-regels.</strong> Bij <a href="{DNB}">draw no bet</a> krijg je je inzet terug bij gelijkspel. Dan is 1 ÷ odd niet de kans op winst, maar de kans op winst als het geen gelijkspel wordt.</li><li><strong>Odds bewegen.</strong> Een kans geldt alleen voor het moment waarop je de odds las. Blessures en opstellingen kunnen hem tot de aftrap veranderen.</li></ul>
<p>Rekenen maakt je niet onkwetsbaar: een goede kans is geen zekerheid. Speel alleen bij een <a href="{LEGAAL}">legale bookmaker</a>, houd je aan je eigen speelgrenzen en de <a href="{LIMIET}">netto-stortingslimiet</a>, en lees onze tips over <a href="{BEWUST}">verantwoord wedden</a>. Meer uitleg vind je in de <a href="/wedgids">wedgids</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe reken je odds om naar kans?</strong><br>Deel 1 door de decimale odd en vermenigvuldig met 100. Een odd van 2,50 geeft 1 ÷ 2,50 = {pct(1 / 2.5)}. Dat is de impliciete kans, inclusief de marge van de bookmaker.</p>
<p><strong>Wat is de impliciete kans?</strong><br>De kans die in een odd zit: 1 ÷ odd. Het is ook het percentage weddenschappen dat je op die odd moet winnen om quitte te spelen.</p>
<p><strong>Hoe haal je de marge uit de odds?</strong><br>Tel de impliciete kansen van alle uitkomsten op en deel elke kans door dat totaal. Bij Sparta - AZ wordt {pct(SA_IMP[2])} voor AZ zo {pct(SA_P[2])}.</p>
<p><strong>Wat zijn eerlijke odds?</strong><br>Odds zonder marge: 1 gedeeld door de kans zonder marge. Voor AZ was dat {q(1 / SA_P[2])}, terwijl 711 {q(SA[2])} bood.</p>
<p><strong>Wanneer is een odd value?</strong><br>Als jouw kans keer de odd meer dan 1 is. Bij een kans van {pct(JIJ, 0)} en een odd van {q(ODD_AZ)} is dat {q(JIJ * ODD_AZ)}: +{pct(EV)} verwachte waarde. Dat is een gemiddelde over veel weddenschappen, geen garantie.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    html = content + content2 + content3
    assert re.search(r"<(ul|ol|/li)>\s+<", html) is None
    assert "/kennisbank/" not in html and "<h2" not in html and "<h4" not in html and "/go/" not in html
    assert html.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert content.startswith("<p><strong>")
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert len(OG_CHIPS) == 2 and len(OG_DATA) == 4 and html.count("<table") >= 4
    for link in (ODDS, VALUE, XG, ARB, ACCA, VERGELIJK, DNB, OU, LEGAAL, LIMIET, BEWUST, "/bookmakers/711", "/wedgids"):
        assert f'href="{link}"' in html, link
    assert not re.search(r'href="(?!/)', html), "alleen relatieve links"
    assert all(h.startswith("<strong>") for h in re.findall(r"<h3>(.*?)</h3>", html))
    faq = content3.split("Veelgestelde vragen")[1]
    assert 4 <= faq.count("<p><strong>") <= 6
    tekst = re.sub(r"<[^>]+>", " ", html)
    woorden = len(tekst.split())
    assert 1200 <= woorden <= 2200, woorden
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", woorden, "woorden |",
          [len(re.sub(r"<[^>]+>", " ", c).split()) for c in (content, content2, content3)])
    # ---- --live: NIET zelf draaien; alleen na akkoord van Jasper (bij voorkeur via wg_publiceer.py kans-uit-odds --live,
    #      dat ook de deelkaart en wedgids-categorie regelt) ----
    if "--live" in sys.argv:
        fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
              "samenvatting": SAMENVATTING, "rubriek": RUBRIEK, "wedgids": True,
              "publicatiedatum": datetime.now(timezone.utc).isoformat()}
        print("item:", WF.create_live(fd), "https://www.bet-experts.nl/nieuws/" + SLUG)
