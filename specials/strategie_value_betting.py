# -*- coding: utf-8 -*-
"""Herschrijving Nieuws-item 650484d1ed62b7de32fe2088 (Kennisbank-versie is offline + 301):
Wat is value betting? Uitleg met rekenvoorbeelden (impliciete kans, EV, marge eruit, variantie, CLV, bijhouden).
Feiten nagelopen op 21-10-2026:
- Wedtips-model v2 (sinds 15-10-2026, tips-agent/tp_model.py + tp_odds.market_fair + tp_select.py): eigen kans uit
  verwachte doelpunten (Poisson/Dixon-Coles) gecombineerd met de marge-vrije gemiddelde kans over 15 NL-bookmakers;
  tips vooral waar de beste odd boven de eerlijke odd ligt; BTTS-aanvullingen rond de eerlijke prijs; openbaar
  trackrecord (raak% en aantal), bewust geen winst/rendement. Tekst claimt dus geen winst en geen garantie.
- Kansspelbelasting 37,8% per 1-1-2026 (Belastingdienst); bij een aanbieder met Ksa-vergunning betaalt de aanbieder.
- Inzetlimieten: algemene voorwaarden van bookmakers (geen wettelijke regel).
Alle getallen (EV, eerlijke odds, binomiale kansen, CLV, Kelly) worden hieronder berekend en ge-assert.
  python3 specials/strategie_value_betting.py [--live]"""
import os, sys
from math import comb
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
import lk_webflow as WF
from legaal_data import tabel, aanraders

ITEM_ID = "650484d1ed62b7de32fe2088"
SLUG = "wat-is-de-wedstrategie-value-betting"
RUBRIEK = "6502b64b78efefb4144fd2c1"
TITEL = "Wat is value betting? Uitleg met rekenvoorbeelden"
SAMENVATTING = ("Value betting uitgelegd: impliciete kans, verwachte waarde, de marge eruit rekenen, variantie en "
                "closing line value. Met rekenvoorbeelden in euro's.")

OG_KOP = "Value <span>betting</span>"
OG_EYEBROW = "Wedstrategie uitgelegd"
OG_CHIPS = ["Kans × odd groter dan 1", "Eerlijke odds"]
OG_MOTIEF = "odds"
OG_DATA = ["Jouw kans · 50%", "Odd · 2,40", "Verwachte waarde · +20%"]


def eur(x):
    s = f"€{abs(x):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return ("−" + s) if x < -0.004 else ("+" + s if x > 0.004 else s)


def bedrag(x):
    return eur(x).lstrip("+")


def odd(x):
    return f"{x:.2f}".replace(".", ",")


def pct(x, d=1, teken=False):
    s = f"{x * 100:{'+' if teken else ''}.{d}f}%".replace(".", ",")
    return s.replace("-", "−")


def ev(p, o):
    return p * o - 1


def kans_in_de_min(n, p):
    """Kans dat je na n weddenschappen tegen odd 2,00 (vaste inzet) verlies hebt: minder dan n/2 keer raak."""
    return sum(comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(0, (n + 1) // 2))


# 1. Verwachte waarde
P1, O1, INZ = 0.50, 2.40, 10
EV1 = ev(P1, O1)
assert round(EV1, 4) == 0.20 and round(EV1 * INZ, 2) == 2.00 and pct(1 / O1) == "41,7%"
P2, O2 = 0.52, 1.80
EV2 = ev(P2, O2)
assert round(EV2, 4) == -0.064 and round(EV2 * INZ, 2) == -0.64 and pct(1 / O2) == "55,6%"
assert odd(1 / P1) == "2,00" and odd(1 / P2) == "1,92"

EV_RIJEN = []
for p, o in [(0.50, 2.40), (0.50, 2.00), (0.52, 1.80), (0.35, 3.20), (0.60, 1.75)]:
    EV_RIJEN.append((pct(p, 0), odd(o), pct(1 / o), odd(1 / p), pct(ev(p, o), 1, True), eur(round(ev(p, o) * INZ, 2))))
assert EV_RIJEN[3][4] == "+12,0%" and EV_RIJEN[4][4] == "+5,0%" and EV_RIJEN[1][4] == "+0,0%"

# 2. Marge eruit rekenen (1X2)
O3 = [2.10, 3.40, 3.60]
SOM = sum(1 / o for o in O3)
EERLIJK = [(1 / o) / SOM for o in O3]
EERLIJKE_ODDS = [1 / p for p in EERLIJK]
assert pct(SOM) == "104,8%" and [pct(p) for p in EERLIJK] == ["45,4%", "28,1%", "26,5%"]
assert [odd(o) for o in EERLIJKE_ODDS] == ["2,20", "3,56", "3,77"]
O_ELDERS = 2.30
EV_ELDERS = ev(EERLIJK[0], O_ELDERS)
assert pct(EV_ELDERS, 1, True) == "+4,5%"

# 3. Variantie: vaste inzet €10 tegen odd 2,00
VAR_RIJEN = []
for n in (100, 500, 1000):
    a, b = kans_in_de_min(n, 0.53), kans_in_de_min(n, 0.51)
    VAR_RIJEN.append((str(n), eur(n * INZ * ev(0.53, 2.0)), pct(a, 0), eur(n * INZ * ev(0.51, 2.0)), pct(b, 0)))
assert [r[2] for r in VAR_RIJEN] == ["24%", "8%", "3%"] and [r[4] for r in VAR_RIJEN] == ["38%", "31%", "25%"]
assert VAR_RIJEN[0][1] == "+€60,00" and VAR_RIJEN[2][3] == "+€200,00"

# 4. Closing line value
O_GENOMEN, O_SLOT = 2.30, 2.10
CLV = O_GENOMEN / O_SLOT - 1
assert pct(CLV) == "9,5%"

# 5. Kelly
KELLY = (P1 * O1 - 1) / (O1 - 1)
assert pct(KELLY) == "14,3%" and pct(KELLY / 4) == "3,6%"

content = f"""<p><strong>Value betting betekent dat je alleen inzet als de quotering hoger is dan de echte kans rechtvaardigt. Een odd van {odd(O1)} staat voor een kans van {pct(1 / O1)}. Schat jij die kans op {pct(P1, 0)}, dan heeft de weddenschap waarde: op lange termijn levert elke €{INZ} inzet gemiddeld {bedrag(EV1 * INZ)} op. Je wint daarmee niet elke weddenschap, en op korte termijn kun je flink verliezen. Het lastige deel is je kans beter inschatten dan de markt.</strong></p>
<p>Bijna iedere serieuze wedder noemt value betting de basis van elke strategie, en dat klopt: zonder waarde verlies je op lange termijn door de marge van de bookmaker. Maar value vinden is moeilijker dan het klinkt. Hieronder lees je hoe je de impliciete kans en de verwachte waarde uitrekent, hoe je de marge uit de odds haalt, waarom je veel geduld nodig hebt en hoe je controleert of je echt waarde vindt. De quoteringen in de voorbeelden zijn fictief.</p>
<h3><strong>Wat is de impliciete kans van een quotering?</strong></h3>
<p>Een quotering is een kans in een andere vorm. De impliciete kans is <strong>1 ÷ odd</strong>. Een odd van 2,00 staat voor 50%, een odd van {odd(O2)} voor {pct(1 / O2)}. Andersom kun je van elke kans een <strong>eerlijke odd</strong> maken: 1 ÷ kans. Denk je dat een team 52% kans heeft, dan is de eerlijke odd {odd(1 / P2)}. Alles daarboven is value, alles daaronder niet.</p>
<h3><strong>Hoe bereken je de verwachte waarde?</strong></h3>
<p>De verwachte waarde (expected value, EV) zegt wat een weddenschap gemiddeld oplevert als je hem heel vaak zou spelen. De formule per euro inzet:</p>
<p><strong>EV = jouw kans × odd − 1</strong></p>
<p>Is de uitkomst positief, dan heeft de weddenschap waarde. Twee voorbeelden met €{INZ} inzet:</p>
<ul><li><strong>Kans {pct(P1, 0)}, odd {odd(O1)}:</strong> {odd(P1)} × {odd(O1)} − 1 = {odd(EV1)}. Gemiddeld {bedrag(EV1 * INZ)} winst per €{INZ}, een rendement van {pct(EV1, 0)}.</li><li><strong>Kans {pct(P2, 0)}, odd {odd(O2)}:</strong> {odd(P2)} × {odd(O2)} − 1 = {f'{EV2:.3f}'.replace('.', ',').replace('-', '−')}. Gemiddeld {eur(EV2 * INZ)} per €{INZ}. Je speelt de favoriet, je wint vaker dan je verliest, en toch is het een slechte weddenschap.</li></ul>
<p>Dat tweede voorbeeld is de kern van value betting: het gaat niet om de vraag of iets gebeurt, maar of de prijs klopt.</p>
{tabel(["Jouw kans", "Odd", "Impliciete kans", "Eerlijke odd", "EV", "Per €10 inzet"], EV_RIJEN)}
<p>Een weddenschap op 3,20 met 35% kans heeft meer waarde dan een favoriet op 1,75 met 60% kans, al win je die tweede veel vaker. Value zit dus net zo goed in underdogs als in favorieten.</p>
<h3><strong>Hoe haal je de marge uit de odds?</strong></h3>
<p>Een bookmaker bouwt winst in zijn quoteringen. Tel je de impliciete kansen van alle uitkomsten op, dan kom je boven de 100% uit. Stel: thuiswinst {odd(O3[0])}, gelijk {odd(O3[1])}, uitwinst {odd(O3[2])}. Samen is dat {pct(SOM)}, een marge van {pct(SOM - 1)}.</p>
<p>Om de <strong>eerlijke kans</strong> te vinden, deel je elke impliciete kans door de som. Dat heet de proportionele methode; er bestaan nauwkeurigere methodes, maar deze is voor de meeste markten goed genoeg.</p>"""

content2 = f"""{tabel(["Uitkomst", "Odd", "Impliciete kans", "Eerlijke kans", "Eerlijke odd"], [
    ("Thuiswinst", odd(O3[0]), pct(1 / O3[0]), pct(EERLIJK[0]), odd(EERLIJKE_ODDS[0])),
    ("Gelijkspel", odd(O3[1]), pct(1 / O3[1]), pct(EERLIJK[1]), odd(EERLIJKE_ODDS[1])),
    ("Uitwinst", odd(O3[2]), pct(1 / O3[2]), pct(EERLIJK[2]), odd(EERLIJKE_ODDS[2])),
    ("<strong>Totaal</strong>", "", f"<strong>{pct(SOM)}</strong>", "<strong>100,0%</strong>", ""),
])}
<p>Biedt een andere bookmaker {odd(O_ELDERS)} op thuiswinst, dan is dat hoger dan de eerlijke odd van {odd(EERLIJKE_ODDS[0])}. Met de eerlijke kans van {pct(EERLIJK[0])} is de EV {f'{EERLIJK[0]:.4f}'.replace('.', ',')} × {odd(O_ELDERS)} − 1 = {pct(EV_ELDERS, 1, True)}. Je hebt dan waarde zonder zelf een kans te schatten.</p>
<p>Dit is de eenvoudigste vorm van value betting: je gebruikt de markt zelf als schatting en zoekt de bookmaker die afwijkt. Werkt het altijd? Nee. Soms weet die afwijkende bookmaker iets wat de rest nog niet heeft verwerkt, en soms is de markt waaruit je de eerlijke kans haalt zelf niet scherp. Het helpt om de eerlijke kans te baseren op het gemiddelde van meerdere bookmakers. Met onze <a href="/odds-vergelijken-bij-alle-bookmakers-beste-odds-vandaag">odds vergelijker</a> zie je per wedstrijd snel welke legale bookmaker de hoogste odd heeft.</p>
<h3><strong>Hoe schat je zelf een kans in?</strong></h3>
<p>Wie verder wil dan odds vergelijken, maakt een eigen kansschatting. Daarvoor zijn ruwweg drie routes:</p>
<ul><li><strong>Een statistisch model:</strong> bijvoorbeeld op basis van verwachte doelpunten (xG) of aanvals- en verdedigingssterkte. Met een Poisson-verdeling reken je zo'n verwachting om naar kansen op uitslagen, over/under en beide teams scoren.</li><li><strong>Kennis van een niche:</strong> in kleinere competities of minder bekende sporten zijn bookmakers minder scherp. Wie een competitie echt volgt, ziet blessures, opstellingen en motivatie soms eerder dan de markt.</li><li><strong>Nieuws en timing:</strong> een geschorste spits of een gewijzigde opstelling verandert de kansen. Wie dat sneller verwerkt dan de bookmaker, heeft even waarde.</li></ul>
<p>Wees eerlijk tegen jezelf: de odds van de grote markten zijn het resultaat van veel geld en veel informatie. Zit je schatting ver van de markt af, dan is de kans groter dat jij iets mist dan dat de bookmaker zich vergist.</p>
<p><strong>Zo werken onze wedtips</strong></p>
<p>Onze <a href="/wedtips">wedtips</a> gebruiken hetzelfde idee. Een kansmodel op basis van verwachte doelpunten berekent per wedstrijd de kansen, en dat wordt vergeleken met de eerlijke kans volgens de gezamenlijke Nederlandse bookmakers (de marge eruit gehaald). We zoeken vooral tips waarbij de beste odd boven de eerlijke odd ligt. Het trackrecord houden we openbaar bij op de tip-pagina's, zoals bij <a href="/wedtips/over-2-5-goals-tips-voorspellingen">over 2,5 goals</a> en <a href="/wedtips/btts-tips-voorspellingen">beide teams scoren</a>. Ook een model kan het mis hebben: een tip is een inschatting, geen garantie.</p>
<h3><strong>Waarom heb je zoveel geduld nodig?</strong></h3>
<p>Value betting werkt pas over honderden weddenschappen. Op korte termijn bepaalt toeval bijna alles. De tabel laat zien hoe groot de kans is dat je na een aantal weddenschappen nog verlies hebt, met een vaste inzet van €{INZ} tegen odd 2,00. Bij 6% voordeel is je echte kans 53%, bij 2% voordeel 51%.</p>
{tabel(["Aantal weddenschappen", "Verwachte winst bij 6%", "Kans op verlies bij 6%", "Verwachte winst bij 2%", "Kans op verlies bij 2%"], VAR_RIJEN)}
<p>Zelfs met een voordeel van 6%, wat al heel veel is, sta je na 100 weddenschappen in een op de vier gevallen in de min. Met een realistischer voordeel van 2% is dat na 1.000 weddenschappen nog steeds een op de vier. Dat is geen pech, dat is wiskunde. Wie na twintig verloren weddenschappen stopt of de inzet verdubbelt, zoals bij het <a href="/nieuws/wat-is-het-martingale-systeem-een-dubbel-of-niets-wedstrategie">martingale systeem</a>, haalt de strategie onderuit.</p>
<h3><strong>Hoeveel zet je in per weddenschap?</strong></h3>
<p>Omdat de schommelingen groot zijn, bepaalt je inzet of je een slechte reeks overleeft. Twee veelgebruikte methodes:</p>
<ul><li><strong>Vaste inzet:</strong> elke weddenschap hetzelfde bedrag, bijvoorbeeld 1 tot 2% van een vast budget dat je kunt missen. Simpel en overzichtelijk.</li><li><strong>Kelly-criterium:</strong> inzet als deel van je budget = (kans × odd − 1) ÷ (odd − 1). Bij {pct(P1, 0)} kans en odd {odd(O1)} is dat {pct(KELLY)}. Dat is veel te agressief, zeker omdat je eigen kans nooit precies klopt. Wie Kelly gebruikt, neemt vaak een kwart: {pct(KELLY / 4)}.</li></ul>
<p>Combinaties zijn zelden een value-strategie: bij een <a href="/nieuws/uitleg-wedstrategie-accumulator-weddenschappen">accumulator</a> vermenigvuldig je de marge van elke selectie mee.</p>"""

content3 = f"""<h3><strong>Wat is closing line value?</strong></h3>
<p>Omdat uitslagen zo grillig zijn, kijken ervaren wedders naar iets anders: de <strong>closing line</strong>, de laatste quotering vlak voor de aftrap. Daarin zit de meeste informatie verwerkt. Pak je structureel een hogere odd dan de slotkoers, dan is dat een sterk teken dat je echt waarde vindt, ook als je resultaten tijdelijk tegenzitten.</p>
<p>Voorbeeld: je zet in tegen {odd(O_GENOMEN)} en de quotering sluit op {odd(O_SLOT)}. Je closing line value is {odd(O_GENOMEN)} ÷ {odd(O_SLOT)} − 1 = {pct(CLV)}. Sluit de odd juist hoger dan waar jij instapte, dan had je achteraf beter kunnen wachten. Gebeurt dat steeds, dan vind je waarschijnlijk geen waarde.</p>
<h3><strong>Hoe houd je je resultaten bij?</strong></h3>
<p>Zonder administratie weet je niet of je value vindt of geluk hebt. Houd per weddenschap minimaal dit bij:</p>
{tabel(["Wat", "Waarom"], [
    ("Datum, wedstrijd en markt", "Zodat je later per sport of markt kunt vergelijken"),
    ("Bookmaker, odd en inzet", "De basis voor je rendement"),
    ("Jouw geschatte kans", "Om te zien of je schattingen kloppen (kalibratie)"),
    ("Slotkoers vlak voor de aftrap", "Voor je closing line value"),
    ("Uitslag en winst of verlies", "Je rendement over honderden weddenschappen"),
])}
<p>Kijk na een paar honderd weddenschappen of de uitkomsten met jouw kansen overeenkomen: van alle keren dat je 60% schatte, moet ongeveer 60% raak zijn. Zo niet, dan zit je model ernaast, ook als je toevallig in de plus staat.</p>
<h3><strong>Waarom bookmakers winnende wedders beperken</strong></h3>
<p>Een bookmaker verdient aan de marge en ziet het snel als je structureel tegen te hoge odds inzet, zeker als je steeds de slotkoers verslaat. Volgens hun voorwaarden mogen bookmakers de maximale inzet per klant verlagen of je uitsluiten van promoties. Value betting is niet verboden, maar je hebt geen recht op onbeperkte inzetten. Speel daarom bij meerdere legale bookmakers en vergelijk altijd de odds.</p>
<p>Wil je weten hoe value betting zich verhoudt tot strategieën zonder risico op de uitslag? Lees dan over <a href="/nieuws/wat-is-arbitrage-wedden-de-kunst-van-de-risicovrije-winst">arbitrage wedden</a> en <a href="/nieuws/wat-houdt-de-wedstrategie-matched-betting-in">matched betting</a>, of bekijk alle <a href="/nieuws/alle-verschillende-wedstrategieen-op-een-rijtje">wedstrategieën op een rij</a>.</p>
<h3><strong>Mag je value betting doen in Nederland?</strong></h3>
<p>Ja. Value betting is gewoon wedden met een eigen inschatting, en dat mag bij elke bookmaker met een vergunning van de Kansspelautoriteit. Speel alleen bij legale aanbieders: daar heb je toezicht en uitbetalingszekerheid, en de aanbieder draagt de kansspelbelasting af (37,8% in 2026), zodat jij over je winst niets hoeft te betalen. Weet je niet zeker of een site legaal is, lees dan <a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je dat controleert</a>.</p>
<p>Legale bookmakers die wij aanraden:</p>
{aanraders()}
<h3><strong>Veelgestelde vragen over value betting</strong></h3>
<p><strong>Wat is een value bet in één zin?</strong><br>Een weddenschap waarbij de quotering hoger is dan de eerlijke odd die bij de echte kans hoort, zodat jouw kans × odd groter is dan 1.</p>
<p><strong>Is value betting een garantie op winst?</strong><br>Nee. Je verwachte waarde is positief als je kansschatting klopt, maar op korte termijn kun je flink verliezen, en je schatting kan ernaast zitten.</p>
<p><strong>Hoe reken ik de impliciete kans uit?</strong><br>Deel 1 door de odd. Een odd van 2,50 staat voor 40%.</p>
<p><strong>Hoe weet ik of ik echt value vind?</strong><br>Houd je weddenschappen bij en vergelijk je odd met de slotkoers. Versla je die structureel, dan is de kans groot dat je waarde vindt.</p>
<p><strong>Hoeveel weddenschappen heb je nodig om iets te zeggen?</strong><br>Honderden, liefst meer dan duizend. Na 100 weddenschappen zegt je resultaat bijna niets over je voordeel.</p>
<p><strong>Kan value ook in een favoriet zitten?</strong><br>Ja. Het gaat niet om hoe hoog de odd is, maar of die hoger is dan de eerlijke odd. Een favoriet op 1,75 met 60% kans is value.</p>
<p><strong>Waarom beperken bookmakers soms mijn inzet?</strong><br>Omdat ze winnende wedders herkennen. Bookmakers mogen volgens hun voorwaarden zelf bepalen hoeveel ze van een klant accepteren.</p>
<p>Wedden blijft een kansspel. Bepaal vooraf je budget en lees onze tips over <a href="/speel-bewust/verantwoord-wedden">verantwoord wedden</a>.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    from datetime import datetime, timezone
    alles = content + content2 + content3
    fd = {"name": TITEL, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK, "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    tekst = re.sub(r"<[^>]+>", " ", alles)
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", len(tekst.split()), "woorden")
    assert not re.search(r"<(ul|ol|/li)>\s+<", alles) and "/kennisbank/" not in alles
    if "--live" in sys.argv:   # ---- LIVE: alleen na akkoord van de gebruiker ----
        print(WF.update_live(ITEM_ID, fd).get("lastPublished"))
