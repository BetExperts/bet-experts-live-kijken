# -*- coding: utf-8 -*-
"""NIEUW wedgids-artikel (Nieuws, nog geen item): ROI, yield en hit rate bij wedden, zo bereken je ze.
Slug roi-yield-hit-rate-wedden (gaf HTTP 404 op 10-11-2026, dus vrij). Rubriek Speluitleg, wedgids-categorie 'Wedstrategieën'.
Onderwerp: Engelstalige analysesite (alleen het onderwerp; tekst, opbouw en voorbeelden zelf gemaakt).
Zoekwoorden: 'roi wedden', 'yield wedden', 'roi berekenen weddenschappen', 'hit rate wedden', 'strike rate',
'verschil roi en yield', 'weddenschappen bijhouden excel', 'hoeveel weddenschappen voor betrouwbaar resultaat'.

Feiten / definities (10-11-2026):
- Yield = netto winst / totale inzet; ROI wordt in de wedwereld door elkaar gebruikt: de ene keer als synoniem van yield,
  de andere keer als winst t.o.v. de startbankroll (het 'geïnvesteerde' kapitaal). In de tekst bewust beide genoemd en
  één vaste definitie gekozen. Bet-Experts rekent zelf ROI = winst / inzet (VIP-ROI, zie geheugen 'Units op value' 7-11).
- Break-even hit rate = 1 / decimale quotering (wiskundig, geen bron nodig).
- Spreiding van de yield bij vlakke inzet en quotering o, zonder voorsprong (p = 1/o): sd per weddenschap = sqrt(o - 1);
  95%-band na n weddenschappen = ±1,96 * sqrt(o - 1) / sqrt(n); benodigd aantal om 5% voorsprong te onderscheiden
  n = (1,96 * sqrt(o - 1) / 0,05)^2 (normale benadering, illustratief). Kans 'in de plus' zonder voorsprong exact binomiaal.
- Kansspelbelasting: bij een legale aanbieder draagt de aanbieder die af, de speler hoeft niets te doen
  (zie /nieuws/kansspelbelasting-gokwinst-belasting, nagelopen 21-10-2026).
- Spreadsheetformules in Nederlandstalige Excel/Google Sheets: SOM, AANTAL.ALS, puntkomma als scheidingsteken.
Rekenvoorbeelden: administratie van 10 fictieve weddenschappen, twee fictieve tipsters, spreidingstabel en
binomiale kansen; alles hieronder berekend en ge-assert.
Bewust weggelaten: halve winsten/verliezen bij Aziatische handicaps (te specifiek), statistische toetsen buiten de
95%-vuistregel, merknamen van bookmakers en tipsters, elke belofte van winst.
Interne links gecontroleerd op 10-11-2026 (HTTP 200): zie de lijst in de asserts.
  python3 specials/wg_roi-yield-wedden.py"""
import os, sys, re
from math import comb, sqrt
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
import lk_webflow as WF
from legaal_data import tabel

ITEM_ID = None   # nieuw artikel
SLUG = "roi-yield-hit-rate-wedden"
RUBRIEK = "6502b66cd9992658b4037cf5"   # Speluitleg
WEDGIDS_CAT = "Wedstrategieën"
TITEL = "ROI, yield en hit rate bij wedden: zo bereken je ze"
SAMENVATTING = ("ROI, yield en hit rate bij wedden uitgelegd: zo bereken je ze, waarom hit rate alleen niets zegt en na "
                "hoeveel weddenschappen je resultaat iets betekent.")

OG_KOP = "ROI, <span>yield</span> en hit rate"
OG_EYEBROW = "Je resultaten meten"
OG_CHIPS = ["Break-even per quotering", "Met rekenvoorbeelden"]
OG_MOTIEF = "tabel"

ODDS = "/nieuws/odds-uitgelegd-quotering-lezen"
VALUE = "/nieuws/wat-is-de-wedstrategie-value-betting"
STORTING = "/nieuws/netto-stortingslimiet"
GOKVERSLAVING = "/nieuws/voorkomen-van-een-gokverslaving-belangrijke-stappen-en-hulpbronnen"
BELASTING = "/nieuws/kansspelbelasting-gokwinst-belasting"
XG = "/nieuws/wat-is-xg-expected-goals"


def k(x, n=2):
    return f"{x:,.{n}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def eur(x, n=2):
    s = "€" + k(abs(x), n)
    return ("−" if x < 0 else "+" if x > 0 else "") + s


def pct(x, n=1):
    return k(100 * x, n) + "%"


# ---- rekenvoorbeeld: administratie van 10 weddenschappen, vlak €10 ----
INZET, BANKROLL = 10.0, 500.0
LOG = [("Thuisoverwinning", 1.85, "W"), ("Over 2,5 goals", 2.10, "V"), ("Beide teams scoren", 1.60, "W"),
       ("Gelijkspel", 3.20, "V"), ("Uitoverwinning", 1.95, "W"), ("Handicap −1", 2.40, "W"),
       ("Over 2,5 goals", 1.75, "V"), ("Draw no bet", 2.05, "O"), ("Dubbele kans", 1.50, "W"), ("Uitoverwinning", 2.60, "V")]
UITSLAG = {"W": "Gewonnen", "V": "Verloren", "O": "Ongeldig"}


def resultaat(o, u):
    return INZET * (o - 1) if u == "W" else -INZET if u == "V" else 0.0


AFGEHANDELD = [(m, o, u) for m, o, u in LOG if u != "O"]
WINST = sum(resultaat(o, u) for _, o, u in LOG)
INGEZET = INZET * len(AFGEHANDELD)                 # ongeldige weddenschap: inzet terug, telt niet mee
GEWONNEN = sum(u == "W" for _, _, u in AFGEHANDELD)
YIELD = WINST / INGEZET
HIT = GEWONNEN / len(AFGEHANDELD)
GEM_ODD = sum(o for _, o, _ in AFGEHANDELD) / len(AFGEHANDELD)
ROI_BR = WINST / BANKROLL
assert eur(WINST) == "+€3,00" and eur(INGEZET, 0).lstrip("+") == "€90" and GEWONNEN == 5
assert pct(YIELD) == "3,3%" and pct(HIT) == "55,6%" and pct(ROI_BR) == "0,6%" and k(GEM_ODD) == "2,11"
assert pct(1 / GEM_ODD) == "47,5%"
RIJEN_LOG = [(str(i + 1), m, k(o), eur(INZET).lstrip("+"), UITSLAG[u], eur(resultaat(o, u)))
             for i, (m, o, u) in enumerate(LOG)]

# ---- break-even hit rate per quotering ----
QUOTERINGEN = [1.30, 1.50, 1.80, 2.00, 2.50, 3.00, 4.00]
RIJEN_BE = [(k(o), pct(1 / o)) for o in QUOTERINGEN]
assert RIJEN_BE[1] == ("1,50", "66,7%") and RIJEN_BE[3] == ("2,00", "50,0%") and RIJEN_BE[-1] == ("4,00", "25,0%")

# ---- twee fictieve tipsters ----
TA_HIT, TA_ODD, TB_HIT, TB_ODD = 0.72, 1.35, 0.38, 2.95
TA_Y, TB_Y = TA_HIT * TA_ODD - 1, TB_HIT * TB_ODD - 1
assert pct(TA_Y) == "-2,8%" and pct(TB_Y) == "12,1%" and pct(1 / TA_ODD) == "74,1%" and pct(1 / TB_ODD) == "33,9%"

# ---- variantie: 95%-band van de yield en benodigd aantal weddenschappen (zonder voorsprong, p = 1/o) ----
Z, VOORSPRONG = 1.96, 0.05
VAR_ODDS, AANTALLEN = [1.50, 2.00, 3.00, 5.00], [100, 500, 1000]


def band(o, n):
    return Z * sqrt(o - 1) / sqrt(n)


def nodig(o):
    return (Z * sqrt(o - 1) / VOORSPRONG) ** 2


assert abs(sqrt(2.0 - 1) - 2.0 * sqrt(0.5 * 0.5)) < 1e-12        # sd per weddenschap = o * sqrt(p(1-p)) = sqrt(o-1)
assert k(100 * band(2.0, 100), 1) == "19,6" and k(100 * band(2.0, 1000), 1) == "6,2"
assert round(nodig(1.5), -1) == 770 and round(nodig(2.0), -1) == 1540 and round(nodig(3.0), -1) == 3070 and round(nodig(5.0), -1) == 6150


def rondaf(x):
    return k(round(x, -1), 0)


RIJEN_VAR = [(k(o),) + tuple("±" + k(100 * band(o, n), 1) + "%" for n in AANTALLEN) + (rondaf(nodig(o)),) for o in VAR_ODDS]

# ---- kans om zonder voorsprong (5% nadeel, 47,5% @ 2,00) toch in de plus te staan ----
P_NADEEL = 0.475
assert round(P_NADEEL * 2.0 - 1, 3) == -0.05


def kans_plus(n, p=P_NADEEL):
    return sum(comb(n, w) * p ** w * (1 - p) ** (n - w) for w in range(n // 2 + 1, n + 1))


PLUS = {n: kans_plus(n) for n in (100, 500, 1000)}
assert pct(PLUS[100], 0) == "27%" and pct(PLUS[500], 0) == "12%" and pct(PLUS[1000], 0) == "5%"

# ---- betrouwbaarheid hit rate: 55% na 100 weddenschappen ----
HR, HN = 0.55, 100
HR_BAND = Z * sqrt(HR * (1 - HR) / HN)
assert k(100 * HR_BAND, 0) == "10"

OG_DATA = [f"Quotering {k(o)} · {pct(1 / o)}" for o in (1.50, 2.00, 3.00, 5.00)]
assert OG_DATA[3] == "Quotering 5,00 · 20,0%"

content = f"""<p><strong>Yield is je winst gedeeld door je totale inzet: zet je €1.000 in en hou je daar €50 winst aan over, dan is je yield 5%. ROI betekent bij wedders meestal hetzelfde, al rekenen sommigen het uit ten opzichte van hun startbudget. Hit rate is het percentage gewonnen weddenschappen; dat zegt pas iets in combinatie met de quotering, want bij een quotering van 2,00 heb je al 50% nodig om quitte te spelen.</strong></p>
<p>Hieronder lees je hoe je alle drie berekent, met een rekenvoorbeeld. Je ziet ook waarom een hoge hit rate misleidend kan zijn, hoeveel weddenschappen je nodig hebt voordat je resultaat iets betekent en hoe je je weddenschappen eenvoudig bijhoudt.</p>
<h3><strong>Wat is het verschil tussen ROI en yield?</strong></h3>
<p>Beide termen beschrijven hoe winstgevend je wedt, maar ze worden in de wedwereld niet altijd hetzelfde gebruikt. Daarom eerst de definities zoals wij ze hanteren:</p>
{tabel(["Begrip", "Formule", "Wat zegt het?"], [
    ("<strong>Netto winst</strong>", "Totaal uitbetaald − totaal ingezet", "Hoeveel je erop vooruit of achteruit bent gegaan"),
    ("<strong>Yield</strong>", "Netto winst ÷ totale inzet × 100%", "Wat je gemiddeld per ingezette euro overhoudt"),
    ("<strong>ROI op inzet</strong>", "Netto winst ÷ totale inzet × 100%", "Hetzelfde als yield; zo gebruiken de meeste tipsters het"),
    ("<strong>ROI op bankroll</strong>", "Netto winst ÷ startbudget × 100%", "Hoeveel je budget is gegroeid of gekrompen"),
])}
<p>Het verschil tussen yield en ROI op bankroll is groot. Wie met €100 begint en daarmee in een seizoen €2.000 inzet, kan een yield van 2% hebben (€40 winst) en tegelijk een ROI op bankroll van 40%. Zie je een tipster een indrukwekkend ROI-percentage noemen, vraag dan altijd: ten opzichte van wat? Op Bet-Experts bedoelen we met ROI de winst gedeeld door de totale inzet, dus hetzelfde als yield.</p>
<h3><strong>Rekenvoorbeeld: zo bereken je yield, ROI en hit rate</strong></h3>
<p>Je zet tien keer {eur(INZET, 0).lstrip('+')} in. Eén weddenschap wordt ongeldig (bijvoorbeeld een draw no bet die gelijk eindigt): je krijgt je inzet terug. <em>Weddenschappen en quoteringen zijn fictief.</em></p>
{tabel(["#", "Markt", "Quotering", "Inzet", "Uitslag", "Winst/verlies"], RIJEN_LOG)}
<ul><li><strong>Netto winst:</strong> {eur(WINST)}.</li><li><strong>Totale inzet:</strong> {eur(INGEZET, 0).lstrip('+')}. De ongeldige weddenschap tel je niet mee, want die inzet kreeg je terug.</li><li><strong>Yield (en ROI op inzet):</strong> {k(WINST)} ÷ {k(INGEZET, 0)} = {pct(YIELD)}.</li><li><strong>Hit rate:</strong> {GEWONNEN} van de {len(AFGEHANDELD)} afgehandelde weddenschappen gewonnen = {pct(HIT)}.</li><li><strong>ROI op bankroll:</strong> met een startbudget van {eur(BANKROLL, 0).lstrip('+')} is dat {k(WINST)} ÷ {k(BANKROLL, 0)} = {pct(ROI_BR)}.</li></ul>
<p>Mooi resultaat? Tien weddenschappen zeggen nog bijna niets: één andere uitslag en de yield staat ruim in de min. Verderop lees je hoeveel weddenschappen je wel nodig hebt.</p>"""

content2 = f"""<h3><strong>Wat is hit rate en waarom zegt het alleen niets?</strong></h3>
<p>Hit rate, ook wel strike rate of winstpercentage, is het aandeel gewonnen weddenschappen: gewonnen gedeeld door afgehandeld. Ongeldige weddenschappen laat je erbuiten. Het klinkt als het belangrijkste getal, maar zonder de quotering erbij zegt het niets. Wie alleen op favorieten van 1,30 wedt, wint vaak en kan toch verlies draaien. Wie op quoteringen van 3,00 wedt, verliest vaker dan hij wint en kan toch winst maken.</p>
<p>Het omslagpunt is de <strong>break-even hit rate: 1 gedeeld door de quotering</strong>. Zit je daar gemiddeld boven, dan maak je winst; zit je eronder, dan verlies je. Hoe je een quotering omrekent naar een kans, lees je in <a href="{ODDS}">odds uitgelegd</a>.</p>
{tabel(["Quotering", "Nodig om quitte te spelen"], RIJEN_BE)}
<p><strong>Voorbeeld met twee tipsters.</strong> Tipster A wint {pct(TA_HIT, 0)} van zijn tips, op een gemiddelde quotering van {k(TA_ODD)}. Tipster B wint maar {pct(TB_HIT, 0)}, op gemiddeld {k(TB_ODD)}. A lijkt de betere, maar zijn yield is {k(TA_HIT)} × {k(TA_ODD)} − 1 = {pct(TA_Y)}: hij zit onder zijn break-even van {pct(1 / TA_ODD)}. B haalt {k(TB_HIT)} × {k(TB_ODD)} − 1 = {pct(TB_Y)}, want zijn break-even ligt op {pct(1 / TB_ODD)}. <em>Beide tipsters zijn fictief.</em></p>
<p>In het rekenvoorbeeld hierboven was de gemiddelde quotering {k(GEM_ODD)}, met een break-even van ongeveer {pct(1 / GEM_ODD)}. De hit rate van {pct(HIT)} lag daar ruim boven, en toch is de winst klein: juist de gewonnen weddenschappen hadden lage quoteringen. Een gemiddelde quotering is dus maar een ruwe maatstaf. Kijk daarom altijd naar hit rate én gemiddelde quotering samen, of direct naar de yield. Of je structureel boven de break-even zit, hangt ervan af of je kansen beter inschat dan de bookmaker: dat is het idee achter <a href="{VALUE}">value betting</a>.</p>
<h3><strong>Na hoeveel weddenschappen zegt je resultaat iets?</strong></h3>
<p>Wedden heeft veel spreiding (variantie): zelfs als je precies quitte zou moeten spelen, wijkt je yield over een korte reeks flink af van nul. Die spreiding is groter naarmate de quoteringen hoger zijn, en neemt pas langzaam af als je meer weddenschappen plaatst. De tabel laat zien binnen welke band je yield in 95% van de gevallen uitkomt bij vlakke inzetten, puur door toeval, en hoeveel weddenschappen je ongeveer nodig hebt om een echte voorsprong van 5% van geluk te onderscheiden.</p>
{tabel(["Quotering", "Na 100", "Na 500", "Na 1.000", "Nodig voor 5% voorsprong"], RIJEN_VAR)}
<p>Bij quoteringen rond 2,00 kan je yield na 100 weddenschappen dus zomaar +15% of −15% zijn zonder dat je iets bijzonders doet. Pas na ruim {rondaf(nodig(2.0))} weddenschappen is een yield van 5% met redelijke zekerheid meer dan geluk. Bij hoge quoteringen, zoals outrights of spelersweddenschappen, duurt het nog veel langer. <em>Illustratieve berekening met een normale benadering.</em></p>
<p>Andersom geldt hetzelfde. Iemand met een nadeel van 5%, ongeveer de marge van een bookmaker, staat na 100 weddenschappen op 2,00 toch met {pct(PLUS[100], 0)} kans in de plus. Na 500 weddenschappen is dat nog {pct(PLUS[500], 0)}, na 1.000 nog {pct(PLUS[1000], 0)}. Een goede start bewijst dus weinig, en dat geldt ook voor de resultaten van tipsters die je online ziet. Hetzelfde voor hit rate: 55% na 100 weddenschappen betekent dat de echte hit rate ergens tussen ongeveer {pct(HR - HR_BAND, 0)} en {pct(HR + HR_BAND, 0)} ligt.</p>
<p>Een snellere graadmeter is je quotering vergelijken met de slotquotering, vlak voor de aftrap. Krijg je structureel een hogere quotering dan de markt uiteindelijk geeft, dan zat je vaak aan de goede kant. Ook dat is geen garantie, maar het zegt sneller iets dan een winstpercentage over vijftig weddenschappen.</p>"""

content3 = f"""<h3><strong>Hoe houd je je weddenschappen bij?</strong></h3>
<p>Een spreadsheet in Excel of Google Sheets is genoeg. Gebruik één regel per weddenschap en deze kolommen:</p>
{tabel(["Kolom", "Voorbeeld", "Waarom?"], [
    ("Datum", "8-11-2026", "Resultaten per maand of seizoen bekijken"),
    ("Sport en competitie", "Voetbal, Eredivisie", "Zien waar je goed en minder goed in bent"),
    ("Wedstrijd en markt", "Over 2,5 goals", "Markten met elkaar vergelijken"),
    ("Bookmaker", "Naam van de aanbieder", "Controleren of je je inzetten goed spreidt"),
    ("Quotering", "2,10", "Nodig voor yield en break-even"),
    ("Inzet", "€10 of 1 unit", "Totale inzet optellen"),
    ("Uitslag", "Gewonnen, Verloren of Ongeldig", "Hit rate berekenen"),
    ("Winst/verlies", "+€11,00", "Netto winst optellen"),
    ("Slotquotering (optioneel)", "1,95", "Zien of je de markt voor was"),
])}
<p>Per regel bereken je de winst of het verlies: bij winst inzet × (quotering − 1), bij verlies min de inzet, bij een ongeldige weddenschap 0. Heb je uitgecasht, noteer dan het uitbetaalde bedrag min je inzet. Houd free bets en andere promoties apart, anders vertekenen ze je yield.</p>
<p>Daarna heb je twee formules nodig (Nederlandstalige versie, met de inzet in kolom F, de uitslag in G en de winst in H):</p>
<ul><li><strong>Yield:</strong> =SOM(H:H)/SOMMEN.ALS(F:F;G:G;"&lt;&gt;Ongeldig")</li><li><strong>Hit rate:</strong> =AANTAL.ALS(G:G;"Gewonnen")/(AANTAL.ALS(G:G;"Gewonnen")+AANTAL.ALS(G:G;"Verloren"))</li></ul>
<p>Werk je met units, noteer dan ook de unitgrootte. Zo blijven je resultaten vergelijkbaar als je budget verandert. Bekijk je cijfers één keer per maand, niet na elke weddenschap: dat voorkomt dat je na een paar verliezen je aanpak overhoop gooit.</p>
<h3><strong>Waarom bijhouden ook bij verantwoord spelen helpt</strong></h3>
<p>Een administratie laat niet alleen zien of je aanpak werkt, maar ook hoeveel je echt uitgeeft. Veel wedders schatten hun verlies lager in dan het is. Leg je totale inzet en je netto resultaat per maand naast je budget en naast je <a href="{STORTING}">netto-stortingslimiet</a>. Gaat er meer geld en tijd in dan je wilt, lees dan <a href="{GOKVERSLAVING}">hoe je een gokverslaving voorkomt en waar je hulp vindt</a>.</p>
<p>Meer uitleg over wedden, van <a href="{XG}">xG</a> tot odds, vind je in de <a href="/wedgids">wedgids</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe bereken je ROI bij wedden?</strong><br>Deel je netto winst door je totale inzet en vermenigvuldig met 100%. Met €30 winst op €600 inzet is je ROI (of yield) 5%. Sommigen delen door hun startbudget; vermeld daarom altijd welke berekening je gebruikt.</p>
<p><strong>Wat is een goede yield bij wedden?</strong><br>Over een lange reeks is elke positieve yield bijzonder, omdat bookmakers een marge in hun odds verwerken. Een yield van een paar procent over duizenden weddenschappen is al sterk. Hoge percentages over een korte reeks zeggen vooral iets over geluk.</p>
<p><strong>Wat is een goede hit rate?</strong><br>Dat hangt af van je quoteringen. Bij een gemiddelde quotering van 2,00 heb je meer dan 50% nodig, bij 1,50 meer dan 66,7% en bij 3,00 meer dan 33,3%.</p>
<p><strong>Tel je ongeldige weddenschappen mee?</strong><br>Nee. Je krijgt je inzet terug, dus ze tellen niet mee in je totale inzet en niet in je hit rate.</p>
<p><strong>Moet ik belasting van mijn winst aftrekken?</strong><br>Nee, bij een legale bookmaker draagt de aanbieder de kansspelbelasting af. Lees meer over <a href="{BELASTING}">kansspelbelasting op gokwinst</a>.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    html = content + content2 + content3
    assert re.search(r"<(ul|ol|/li)>\s+<", html) is None
    assert "/kennisbank/" not in html and "<h2" not in html and "<h4" not in html and "/go/" not in html
    assert html.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert len(OG_CHIPS) == 2 and len(OG_DATA) == 4 and html.count("<table") >= 4
    for link in (ODDS, VALUE, STORTING, GOKVERSLAVING, BELASTING, XG, "/wedgids"):
        assert f'href="{link}"' in html, link
    assert all(h.startswith("<h3><strong>") for h in re.findall(r"<h3>.{0,12}", html))
    faq = content3.split("Veelgestelde vragen")[1]
    assert 4 <= faq.count("<p><strong>") <= 6
    tekst = re.sub(r"<[^>]+>", " ", html)
    woorden = len(tekst.split())
    assert 1200 <= woorden <= 2200, woorden
    print("variantie:", RIJEN_VAR)
    print("in de plus zonder voorsprong:", {n: pct(v) for n, v in PLUS.items()}, "| hit-rate-band ±", pct(HR_BAND))
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", woorden, "woorden |",
          [len(re.sub(r"<[^>]+>", " ", c).split()) for c in (content, content2, content3)])
    # Publiceren alleen na akkoord van Jasper, via: wg_publiceer.py roi-yield-wedden --live
