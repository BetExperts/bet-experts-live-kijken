# -*- coding: utf-8 -*-
"""NIEUW wedgids-artikel (Nieuws, nog geen item): wat is xA (expected assists), en npxG?
Slug wat-is-xa-expected-assists (gaf HTTP 404 op 10-11-2026, dus vrij; ook xa-expected-assists gaf 404).
Rubriek Speluitleg, wedgids-categorie 'Wedden uitgelegd'. Onderwerp: Engelstalige analysesite (alleen het onderwerp).
Zoekwoorden: 'wat is xa' / 'expected assists' (hoofd), 'xa betekenis voetbal', 'xag', 'npxg betekenis', 'non-penalty xg',
'key pass betekenis', 'wat telt als assist', 'wedden op assists', 'geeft een assist'.

Afbakening t.o.v. /nieuws/wat-is-xg-expected-goals (gelezen met curl op 10-11-2026): daar xG, xGOT en xGA (= expected goals
against), penalty 0,76-0,79 xG en een over-2,5-voorbeeld. Hier NIET opnieuw uitgelegd hoe xG werkt; wel gelinkt. Nieuw:
xA vs xAG, key pass vs assist, Opta- vs fantasy-assist, npxG, xGChain/xGBuildup, assistmarkten in NL.

Feiten nagelopen op 10-11-2026 (bronnen NIET in de tekst genoemd, behalve Opta):
- xA (theanalyst.com/articles/what-are-expected-assists-xa, gepubliceerd 24-03-2021, gewijzigd 28-05-2025): 'measures the
  likelihood that a given pass will become a goal assist'; 0-1; logistische regressie op honderdduizenden passes; factoren:
  type pass (voorzet, kopbal, steekbal), spelsituatie (open spel, corner, vrije trap, inworp), waar de pass vandaan komt en
  aankomt, lengte; 'regardless of whether the receiver takes a shot or not'.
  theanalyst.com/articles/opta-football-stats-definitions (23-07-2024, gewijzigd 29-05-2025): xA = 'likelihood that a
  completed pass will become a goal assist' -> in de tekst 'aangekomen pass'.
- xAG: een grote statistieksite gebruikte tot oktober 2022 'xA' voor 'expected assisted goals' (xG van schoten na een pass)
  en noemde dat xAG toen ze Opta's pass-xA overnam (eigen uitlegpagina 'xG Explained', gezien via zoekresultaat; site gaf
  403 aan de fetcher). -> in de tekst zonder sitenaam: 'sommige sites ... tot 2022'. xGA = expected goals against op ons eigen
  xG-artikel en de meeste sites -> alleen gewaarschuwd, geen claim dat iemand xGA voor assists gebruikt.
- Opta-definities (zelfde theanalyst-pagina): assist = 'The final touch from a teammate that leads to the recipient of the
  ball scoring a goal'; afgeweken door tegenstander -> alleen als de bal 'deemed as travelling to the goalscorer'; geen
  assist bij eigen doelpunt, direct benutte vrije trap of corner, en penalty's (tenzij de nemer de bal aan een ploeggenoot
  geeft); key pass = 'final pass ... who then attempts a shot on goal without scoring'; chance created = assists + key passes;
  'fantasy assist' is bij Opta een aparte categorie (o.a. rebound na redding, penalty versierd, vrije trap versierd).
- Fantasy (premierleague.com/en/news/2174909, 'FPL basics explained: Scoring points', 20-07-2026): wie de overtreding
  versiert krijgt een assist als de penalty/vrije trap direct wordt benut (niet als hij zelf neemt); rebound na geblokt,
  gestopt of paal/lat -> assist; schot of pass die een eigen doelpunt afdwingt -> assist; 3 punten per assist.
- npxG: xG zonder penalty's (algemeen gebruik). Penaltywaarde Opta 0,79 (theanalyst, zie wg_xg.py); andere modellen 0,76-0,78.
- xGChain/xGBuildup: StatsBomb, 'Introducing xGChain and xGBuildup', Thom Lawrence, 30-08-2018 (statsbomb.com/?p=9491):
  xGChain = totale xG van alle aanvallen (balbezitten) waarin een speler betrokken was, elke betrokken speler krijgt de
  volle xG; xGBuildup = idem maar zonder schoten en key passes. Merknaam StatsBomb NIET genoemd in de tekst.
- Wet: Bijlage 2 Regeling kansspelen op afstand (wetten.overheid.nl/BWBR0044767, geldend vanaf 01-04-2026, curl 10-11):
  verboden voetbalgebeurtenissen o.a. kaarten, inworpen, overtredingen, 'veroorzaken van strafschoppen' en 'nemen van
  strafschoppen', buitenspel, hoekschoppen, wissels, VAR. Assists staan er NIET op -> assistmarkten zijn toegestaan.
- Aanbod: Kambi-wedaanbod (eu-offering-api.kambicdn.com, Manchester City - Fulham 21-11-2026, opgevraagd 10-11-2026) bij
  ubnl (Unibet), leonl (LeoVegas), jvh (JACKS), betmgmnl (BetMGM), sevelevnl (711) en hgtnl: markten 'Geeft een assist
  (Volgens Opta-gegevens)' en 'Scoort of geeft een assist (Volgens Opta-gegevens)'; quoteringen 'Ja' voor creatieve spelers
  ±2,60-4,60, verdedigers 9-18. bet365/TOTO/Holland Casino: help-pagina's niet bereikbaar (403) -> NIET geclaimd.
- Kambi Rules v2.2 NL (pdf via unibet.nl/general-info/terms, 'Versie 2.2 September 2026'): voetbal regel 7: individuele
  spelersprestaties vereisen dat de speler 'vanaf de aftrap' speelt, tenzij anders aangegeven; algemene regel 10: afrekening
  van statistieken zoals assists volgens de definitie van de officiële bron, tenzij bij de markt anders vermeld (hier: Opta).
Bewust weggelaten: echte spelers en hun xA (geen bron die we mogen gebruiken voor Eredivisie), sitenamen van statistieksites,
second assist, expected threat (xT), een 'vaste' xA-waarde per soort pass (verschilt per model).
Rekenvoorbeelden fictief; alles hieronder berekend en ge-assert. Poisson is een vereenvoudiging, zo ook in de tekst.
Interne links gecontroleerd met curl op 10-11-2026: alle HTTP 200, behalve /nieuws/wat-is-ppda-pressing (nieuw zusterartikel,
gaat samen live).
  ../superodd-agent/.venv/bin/python specials/wg_publiceer.py xa-expected-assists   (dry run)"""
import os, sys, re
from math import exp
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

ITEM_ID = None   # nieuw artikel
SLUG = "wat-is-xa-expected-assists"
RUBRIEK = "6502b66cd9992658b4037cf5"   # Speluitleg
WEDGIDS_CAT = "Wedden uitgelegd"
TITEL = "Wat is xA? Expected assists en npxG uitgelegd"
SAMENVATTING = ("Wat is xA (expected assists)? Het verschil met xAG, key passes en assists, wat npxG is en hoe je "
                "deze cijfers gebruikt bij wedden op assists.")

OG_KOP = "Wat is <span>xA</span>?"
OG_EYEBROW = "Expected assists en npxG"
OG_CHIPS = ["Met rekenvoorbeeld", "xA, xAG en npxG"]
OG_MOTIEF = "tabel"

XG = "/nieuws/wat-is-xg-expected-goals"
PPDA = "/nieuws/wat-is-ppda-pressing"
EV = "/nieuws/wat-is-expected-value-ev-bij-wedden"
KANS = "/nieuws/kans-berekenen-uit-odds-impliciete-kans"
DOEL = "/nieuws/doelpuntenmaker-wedden-regels"
OPTA = "/nieuws/wat-zijn-opta-gegevens-alles-over-schoten-op-doel-en-unibet-weddenschappen"
SCHOTEN = "/nieuws/dit-is-hoe-wedden-op-schoten-op-doel-werkt"
CORNERS = "/nieuws/dit-is-waarom-wedden-op-corners-niet-meer-legaal-is-in-nederland"
VERANTW = "/speel-bewust/verantwoord-wedden"
LINKS = (XG, PPDA, EV, KANS, DOEL, OPTA, SCHOTEN, CORNERS, VERANTW, "/wedgids")


def k(x, n=2):
    return f"{x:.{n}f}".replace(".", ",")


def pct(x, n=1):
    return f"{100 * x:.{n}f}".replace(".", ",") + "%"


def spct(x, n=1):
    return ("+" if x >= 0 else "−") + pct(abs(x), n)


# ---- rekenvoorbeeld 1 (fictief): vijf aangekomen passes van middenvelder X in één wedstrijd ----
# (omschrijving, xA, schot? (None = geen schot), xG van dat schot, uitkomst)
PASSES = [("Steekbal tussen de centrale verdedigers door", 0.28, "Ja, gemist", 0.35, "Key pass"),
          ("Voorzet vanaf de zijkant, ploeggenoot kopt raak", 0.06, "Ja, doelpunt", 0.09, "Assist"),
          ("Pass naar de rand van de zestien, ploeggenoot loopt vast", 0.12, None, 0.0, "Telt niet"),
          ("Bal teruggelegd vanaf de achterlijn", 0.22, "Ja, over", 0.40, "Key pass"),
          ("Korte pass, ploeggenoot schiet van ver", 0.02, "Ja, gemist", 0.03, "Key pass")]
XA = sum(p[1] for p in PASSES)
XAG = sum(p[3] for p in PASSES if p[2])
ASSISTS = sum(p[4] == "Assist" for p in PASSES)
KEYP = sum(p[4] == "Key pass" for p in PASSES)
assert (k(XA), k(XAG), ASSISTS, KEYP, ASSISTS + KEYP) == ("0,70", "0,87", 1, 3, 4)
RIJEN_PASSES = [(o, k(xa), s or "Nee", k(xg) if s else "–", u) for o, xa, s, xg, u in PASSES] + [
    ("<strong>Totaal</strong>", f"<strong>{k(XA)}</strong>", "", f"<strong>{k(XAG)}</strong>", f"<strong>{ASSISTS} assist, {KEYP} key passes</strong>")]

# ---- rekenvoorbeeld 2 (fictief): npxG van twee spitsen over een seizoenshelft ----
PEN_XG = 0.79
SPITS = [("Spits A (vaste penaltynemer)", 9.4, 4, 1530), ("Spits B (neemt geen penalty's)", 7.1, 0, 1440)]
NPXG = {n: xg - p * PEN_XG for n, xg, p, _ in SPITS}
NP90 = {n: NPXG[n] / m * 90 for n, _, _, m in SPITS}
assert (k(NPXG["Spits A (vaste penaltynemer)"]), k(NPXG["Spits B (neemt geen penalty's)"])) == ("6,24", "7,10")
assert (k(NP90["Spits A (vaste penaltynemer)"]), k(NP90["Spits B (neemt geen penalty's)"])) == ("0,37", "0,44")
RIJEN_NPXG = [(f"<strong>{n}</strong>", k(xg, 1), str(p), f"{k(xg, 1)} − {p} × {k(PEN_XG)} = {k(NPXG[n])}", k(NP90[n]))
              for n, xg, p, m in SPITS]

# ---- rekenvoorbeeld 3 (fictief): kans op een assist ----
XA90, NPXG90, MIN, ODD_A = 0.30, 0.25, 80, 4.30
L_A = XA90 * MIN / 90
P_A = 1 - exp(-L_A)
EV_A = P_A * ODD_A - 1
L_SA = (XA90 + NPXG90) * MIN / 90
P_SA = 1 - exp(-L_SA)
assert (k(L_A, 3), pct(P_A), k(1 / P_A), spct(EV_A)) == ("0,267", "23,4%", "4,27", "+0,7%")
assert (k(L_SA, 3), pct(P_SA), k(1 / P_SA)) == ("0,489", "38,7%", "2,59")
L_60 = XA90 * 60 / 90
P_60 = 1 - exp(-L_60)
assert (pct(P_60), k(1 / P_60), spct(P_60 * ODD_A - 1)) == ("18,1%", "5,52", "−22,1%")

OG_DATA = [f"Steekbal · {k(PASSES[0][1])} xA", f"Voorzet · {k(PASSES[1][1])} xA",
           f"xA {k(XA)} · {ASSISTS} assist", "npxG · xG zonder penalty's"]

content = f"""<p><strong>xA staat voor expected assists: de kans dat een aangekomen pass een assist wordt, als getal tussen 0 en 1. xA hangt niet af van wat de ploeggenoot met de bal doet: ook een goede pass waarna niemand schiet, levert xA op. Daarmee meet je hoe goed een speler kansen creëert, los van de afwerking van anderen. npxG is xG zonder penalty's: een eerlijkere maat voor hoeveel kansen een speler zelf uit het spel krijgt.</strong></p>
<p>Hoe xG werkt, lees je in ons artikel <a href="{XG}">wat is xG</a>. Dit artikel gaat over de speler die de bal geeft. Je leest hoe xA wordt berekend, waarom xA, xAG en xGA vaak door elkaar lopen, wat het verschil is tussen een key pass en een assist en wat er wel en niet als assist telt. Daarna komen npxG, xGChain en het gebruik bij wedden aan bod. <em>Spelers en cijfers in de voorbeelden zijn fictief.</em></p>
<h3><strong>Hoe wordt xA berekend?</strong></h3>
<p>Een xA-model kijkt naar honderdduizenden eerdere passes en telt hoe vaak een vergelijkbare pass tot een doelpunt leidde. Dat percentage is de xA van die pass. De belangrijkste factoren zijn:</p>
<ul><li><strong>Soort pass:</strong> een steekbal, een voorzet, een pass met het hoofd of een bal die wordt teruggelegd.</li><li><strong>Spelsituatie:</strong> open spel of een standaardsituatie zoals een hoekschop, vrije trap of inworp.</li><li><strong>Waar de bal vandaan komt:</strong> een pass vanaf de achterlijn is gevaarlijker dan een pass vanaf de middenlijn.</li><li><strong>Waar de bal aankomt:</strong> hoe dichter bij het doel en hoe centraler, hoe hoger de xA.</li><li><strong>Lengte van de pass:</strong> lange ballen komen minder vaak precies goed aan.</li></ul>
<p>Het belangrijke verschil met andere maten: xA wordt berekend op het moment dat de pass aankomt. Of de ontvanger schiet, mist of de bal verspeelt, verandert de xA niet. Een breedtepass op het middenveld heeft een xA van bijna nul, een steekbal die een spits alleen voor de keeper zet, een stuk meer.</p>
<h3><strong>Rekenvoorbeeld: xA, xAG, key passes en assists</strong></h3>
<p>Middenvelder X geeft in een wedstrijd vijf passes die gevaarlijk worden. Zo ziet dat er per pass uit:</p>
{tabel(["Pass", "xA", "Schot?", "xG van het schot", "Telt als"], RIJEN_PASSES)}
<p>Middenvelder X komt op {k(XA)} xA, {ASSISTS} assist en {KEYP} key passes. Zijn {ASSISTS} assist kwam van de pass met de laagste kans: een voorzet waarvan een ploeggenoot met een moeilijke kopbal iets moois maakte. De twee beste passes leverden niets op, omdat de ontvangers misten of over schoten.</p>
<p>Zet je alleen de assists op een rij, dan lijkt middenvelder X een gewone wedstrijd te hebben gespeeld. De xA laat zien dat hij in één duel kansen gaf die samen bijna een assist waard waren. Over een heel seizoen gaat het juist om dat soort verschillen: wie structureel veel xA haalt, geeft op den duur ook assists, al bepaalt de afwerking van ploeggenoten hoeveel.</p>"""

content2 = f"""<h3><strong>Wat is het verschil tussen xA, xAG en xGA?</strong></h3>
<p>De afkortingen lijken op elkaar en worden niet overal hetzelfde gebruikt. Kijk daarom altijd naar de uitleg van de bron die je leest.</p>
{tabel(["Afkorting", "Betekenis", "Hangt af van het schot?"], [
    ("<strong>xA</strong> (expected assists)", "Kans dat een aangekomen pass een assist wordt. In het voorbeeld: " + k(XA), "Nee"),
    ("<strong>xAG</strong> (expected assisted goals)", "De xG van de schoten die direct na jouw pass komen. In het voorbeeld: " + k(XAG) + ". Sommige sites noemden dit tot 2022 ook xA", "Ja: geen schot is 0"),
    ("<strong>xGA</strong> (expected goals against)", "De xG die een team tegen krijgt. Heeft niets met assists te maken", "Niet van toepassing"),
])}
<p>xAG is afhankelijk van de ontvanger. Schiet die direct van grote afstand, dan krijgt de passgever weinig. Kiest hij voor een betere plek, dan krijgt de passgever veel. In het voorbeeld levert de pass naar de rand van de zestien 0 xAG op, maar wel {k(PASSES[2][1])} xA. Wil je weten hoe goed iemand passes geeft, dan is xA de zuiverste maat. Wil je weten hoeveel kansen er uit zijn passes kwamen, dan zegt xAG meer.</p>
<h3><strong>Wat is het verschil tussen een key pass en een assist?</strong></h3>
<p>Opta, de grootste leverancier van voetbaldata, hanteert deze definities:</p>
<ul><li><strong>Assist:</strong> de laatste aanraking van een ploeggenoot waarna de ontvanger scoort.</li><li><strong>Key pass:</strong> de laatste pass naar een ploeggenoot die daarna schiet, maar niet scoort.</li><li><strong>Gecreëerde kans:</strong> assists en key passes samen.</li></ul>
<p>Een key pass is dus een assist die het net niet werd, omdat de ploeggenoot miste of de keeper redde. Het aantal key passes zegt vaak meer over een creatieve speler dan het aantal assists, omdat het minder afhangt van de afwerking. Maar een key pass naar een afstandsschot telt even zwaar als een key pass die de spits alleen voor de keeper zet. Daarom kijken analisten liever naar xA.</p>
<h3><strong>Wat telt als assist, en waarom verschilt dat?</strong></h3>
<p>Officiële statistieken en fantasyspellen tellen assists niet op dezelfde manier. In de officiële Opta-telling krijg je geen assist bij een eigen doelpunt, bij een vrije trap of hoekschop die direct in het doel gaat en bij een penalty, tenzij de nemer de bal breed legt voor een ploeggenoot. Raakt een tegenstander de pass, dan is het alleen een assist als de bal ook zonder die aanraking bij de scorer was gekomen. Fantasyspellen zijn ruimer, omdat ze meer spelers punten willen geven. Een voorbeeld uit het officiële fantasyspel van de Premier League:</p>
{tabel(["Situatie", "Assist volgens Opta?", "Assist in het fantasyspel?"], [
    ("Pass, ploeggenoot scoort", "Ja", "Ja"),
    ("Penalty versierd, ploeggenoot benut hem", "Nee", "Ja"),
    ("Vrije trap versierd, ploeggenoot schiet hem direct raak", "Nee", "Ja"),
    ("Jouw schot wordt gestopt, ploeggenoot scoort uit de rebound", "Nee", "Ja"),
    ("Jouw voorzet dwingt een eigen doelpunt af", "Nee", "Ja"),
])}
<p>Opta houdt die ruimere variant apart bij als 'fantasy assist'. Voor wedders is het verschil belangrijk: een assistweddenschap wordt afgerekend op de officiële telling, niet op de fantasyregels. Daarover hieronder meer.</p>"""

content3 = f"""<h3><strong>Wat is npxG en waarom is het eerlijker?</strong></h3>
<p>npxG staat voor non-penalty expected goals: alle xG van een speler of team, min de xG van penalty's. Een penalty krijgt in elk model een vaste, hoge waarde. Opta rekent met {k(PEN_XG)}, andere modellen met 0,76 tot 0,78. Twee penalty's tellen dus al op tot bijna 1,6 xG, terwijl een spits uit het spel per wedstrijd meestal ruim onder de 1 xG blijft.</p>
<p>Dat geeft een vertekend beeld. Een penalty zegt weinig over hoe goed een spits zich vrijloopt, en wie hem neemt is een keuze van de trainer. Bovendien krijgt een team er maar een paar per seizoen. Haal je ze eruit, dan kun je spelers eerlijker vergelijken:</p>
{tabel(["Speler", "xG", "Penalty's", "npxG", "npxG per 90 min."], RIJEN_NPXG)}
<p>Op basis van xG lijkt spits A het gevaarlijkst. Zonder penalty's haalt spits B per 90 minuten meer kansen uit het spel. Voor wedders zit er een addertje onder het gras: bij een weddenschap op een doelpuntenmaker telt een benutte penalty gewoon mee. Een vaste penaltynemer heeft dus een hogere kans om te scoren dan zijn npxG doet vermoeden. Wedden op wie een penalty neemt of veroorzaakt, mag in Nederland overigens niet; dat staat op de wettelijke lijst van verboden weddenschappen, net als <a href="{CORNERS}">corners en kaarten</a>.</p>
<h3><strong>Wat zijn xGChain en xGBuildup?</strong></h3>
<p>xA beloont alleen de laatste pass. Maar een aanval begint vaak veel eerder, bij een verdediger die de bal goed inspeelt of een middenvelder die tussen de linies opduikt. Daarvoor zijn twee maten bedacht:</p>
<ul><li><strong>xGChain:</strong> de totale xG van alle aanvallen waarin een speler de bal heeft geraakt. Iedere speler in die aanval krijgt de volle xG van het schot.</li><li><strong>xGBuildup:</strong> hetzelfde, maar zonder het schot en de laatste pass. Zo zie je wie in de opbouw belangrijk is, zonder dat de spits en de aangever alles opeisen.</li></ul>
<p>Deze maten zijn handig om spelers te herkennen die vaak 'de pass vóór de assist' geven. Voor wedden zijn ze minder direct bruikbaar, omdat er geen markten op bestaan.</p>
<h3><strong>Hoe gebruik je xA en npxG bij wedden?</strong></h3>
<p>Wedden op assists mag in Nederland: assists staan niet op de wettelijke lijst van verboden gebeurtenissen. Bij bookmakers op het Kambi-platform, zoals Unibet, LeoVegas, JACKS, BetMGM en 711, vind je bij grote wedstrijden de markten 'Geeft een assist' en 'Scoort of geeft een assist'. Achter die markten staat 'Volgens Opta-gegevens': ze worden dus afgerekend op de Opta-telling uit de tabel hierboven, niet op de fantasyregels. Volgens de voorwaarden van die bookmakers moet de speler bij een weddenschap vóór de wedstrijd in de basis staan, tenzij bij de markt iets anders staat. Hoe Opta-gegevens werken, lees je in ons artikel over <a href="{OPTA}">Opta en schoten op doel</a>.</p>
<p><strong>Rekenvoorbeeld:</strong> een middenvelder haalt over de laatste vijftien wedstrijden {k(XA90)} xA per 90 minuten. Je verwacht dat hij {MIN} minuten speelt.</p>
{tabel(["Stap", "Berekening", "Uitkomst"], [
    ("Verwachte assists in deze wedstrijd", f"{k(XA90)} × {MIN} ÷ 90", k(L_A, 3)),
    ("Kans op minstens één assist", f"1 − e<sup>−{k(L_A, 3)}</sup>", pct(P_A)),
    ("Eerlijke quotering", f"1 ÷ {k(P_A, 3)}", k(1 / P_A)),
    ("Verwacht rendement bij een quotering van " + k(ODD_A), f"{k(P_A, 3)} × {k(ODD_A)} − 1", f"<strong>{spct(EV_A)}</strong>"),
])}
<p>Bij {k(ODD_A)} zit er volgens dit model dus nauwelijks waarde in: {spct(EV_A)} valt ruim binnen de foutmarge. Speelt hij maar 60 minuten, dan zakt de kans naar {pct(P_60)} en is de eerlijke quotering {k(1 / P_60)}. Dezelfde weddenschap levert dan gemiddeld {spct(P_60 * ODD_A - 1)} op. Bij 'Scoort of geeft een assist' tel je zijn npxG ({k(NPXG90)} per 90 minuten) erbij op: dat geeft een kans van ongeveer {pct(P_SA)}, een eerlijke quotering van {k(1 / P_SA)}. Neemt hij ook de penalty's, dan ligt de kans iets hoger. Wat zo'n uitkomst betekent, staat in onze uitleg over <a href="{EV}">expected value</a> en <a href="{KANS}">kansen uit odds</a>.</p>
<p>Houd rekening met de grenzen van zo'n berekening:</p>
<ul><li><strong>Het blijft een benadering.</strong> De formule gaat ervan uit dat assists los van elkaar vallen. In werkelijkheid hangt het af van de wedstrijd, de tegenstander en de stand.</li><li><strong>Ploeggenoten tellen mee.</strong> Een speler met hoge xA bij een ploeg met zwakke afwerkers krijgt minder assists dan zijn xA belooft.</li><li><strong>Minuten zijn de grootste onzekerheid.</strong> Rotatie, een vroege wissel of een blessure maken veel uit.</li><li><strong>Kleine aantallen.</strong> Vijf wedstrijden zeggen weinig, kijk liever naar vijftien of meer. Vergelijk ook alleen cijfers uit hetzelfde model.</li><li><strong>Bookmakers kennen deze cijfers ook.</strong> xA en npxG zijn een hulpmiddel, geen garantie op winst.</li></ul>
<p>Wil je liever op het scoren zelf wedden, lees dan de regels bij een <a href="{DOEL}">doelpuntenmaker-weddenschap</a> of over <a href="{SCHOTEN}">wedden op schoten op doel</a>. Hoe teams kansen afdwingen door druk te zetten, lees je in ons artikel <a href="{PPDA}">wat is PPDA</a>. Wed alleen met geld dat je kunt missen en lees onze tips over <a href="{VERANTW}">verantwoord wedden</a>. Meer uitleg vind je in de <a href="/wedgids">wedgids</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wat betekent xA in het voetbal?</strong><br>xA staat voor expected assists: de kans dat een aangekomen pass een assist wordt, tussen 0 en 1. Opgeteld over een seizoen zie je hoeveel assists een speler op basis van zijn passes 'verdiende'.</p>
<p><strong>Wat is het verschil tussen xA en xAG?</strong><br>xA kijkt naar de pass, ook als er niet geschoten wordt. xAG telt de xG van de schoten die direct na de pass komen en hangt dus af van wat de ontvanger doet.</p>
<p><strong>Wat is een key pass?</strong><br>Een pass waarna een ploeggenoot schiet zonder te scoren. Key passes en assists samen heten gecreëerde kansen.</p>
<p><strong>Wat betekent npxG?</strong><br>Non-penalty expected goals: xG zonder penalty's. Zo vergelijk je spelers op de kansen die ze uit het spel krijgen, los van wie de penalty's neemt.</p>
<p><strong>Mag je in Nederland wedden op assists?</strong><br>Ja. Assists staan niet op de lijst van verboden weddenschappen. Bij onder meer Unibet en andere Kambi-bookmakers wordt afgerekend volgens de Opta-telling. Een penalty versierd of een rebound na jouw schot telt daar niet als assist.</p>
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
    assert not re.search(r"(?i)footymetrics|betcity|statsbomb|fbref|understat|opstellingvandaag|waaroptv", html)
    faq = content3.split("Veelgestelde vragen")[1]
    assert 4 <= faq.count("<p><strong>") <= 6
    woorden = len(re.sub(r"<[^>]+>", " ", html).split())
    assert 1200 <= woorden <= 2200, woorden
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", woorden, "woorden")
