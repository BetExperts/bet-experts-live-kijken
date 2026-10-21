# -*- coding: utf-8 -*-
"""Herschrijving Nieuws-item 6504835a02b11fec9dee4120: HUB 'Alle wedstrategieën op een rijtje'.
De oude /kennisbank-overzichtspagina redirect (301) hierheen; deze pagina linkt naar elk strategie-artikel.
Alle rekenvoorbeelden worden hieronder in Python berekend en met assert gecontroleerd.
Feiten (nagelopen 21-10-2026):
- Netto stortingslimiet Ksa: €300 p/m tot 24 jaar, €700 vanaf 24 (Beleidsregel verantwoord spelen 2024, sinds 1-10-2024);
  bij overschrijding minimaal 30 dagen geen bonussen (zie netto_stortingslimiet.py / casino_zonder_stortingslimiet.py).
- Kabinet (Rijksoverheid 12-06-2026) wil o.a. een bonusverbod, reclameverbod en één stortingslimiet voor alle aanbieders.
- Verboden markten (corners, kaarten enz.): Bijlage 2 Regeling kansspelen op afstand (zie corners_niet_legaal.py).
- Gelijkspel Eredivisie 2025/26: 80 van 306 = 26,1% (zie strategie_fibonacci.py).
Let op: /nieuws/wat-houdt-de-wedstrategie-matched-betting-in gaf op 21-10-2026 nog 404 (artikel in de maak?).
  python3 specials/strategie_wedstrategieen_hub.py [--live]"""
import os, sys, re
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel, aanraders

ITEM_ID = "6504835a02b11fec9dee4120"   # Nieuws
SLUG = "alle-verschillende-wedstrategieen-op-een-rijtje"
RUBRIEK = "6502b64b78efefb4144fd2c1"
TITEL = "Alle wedstrategieën op een rijtje: overzicht en uitleg"
SAMENVATTING = ("Alle wedstrategieën op een rijtje: value betting, arbitrage, matched betting, martingale, Fibonacci, "
                "handicap en meer, met risico en voor wie.")

OG_KOP = "Alle <span>wedstrategieën</span>"
OG_EYEBROW = "Overzicht strategieën"
OG_CHIPS = ["10 strategieën", "Risico per strategie"]
OG_MOTIEF = "tabel"
OG_DATA = ["Value betting · gemiddeld", "Arbitrage · laag", "Martingale · zeer hoog", "Accumulator · hoog"]

N = "/nieuws/"
L = {
    "value": N + "wat-is-de-wedstrategie-value-betting",
    "matched": N + "wat-houdt-de-wedstrategie-matched-betting-in",
    "arb": N + "wat-is-arbitrage-wedden-de-kunst-van-de-risicovrije-winst",
    "mart": N + "wat-is-het-martingale-systeem-een-dubbel-of-niets-wedstrategie",
    "fib": N + "wedden-op-gelijkspel-de-fibonacci-wedstrategie-onder-de-loep",
    "acca": N + "uitleg-wedstrategie-accumulator-weddenschappen",
    "live": N + "uitleg-in-play-live-wedden-dynamiek-strategie-en-kansen-in-realtime",
    "hc": N + "wat-is-handicap-wedden-de-complete-gids",
    "eh": N + "wat-een-europese-handicap-weddenschap",
    "ah": N + "wat-is-een-asian-handicap-weddenschap",
}


def eur(x):
    x = round(x + 0.0, 2)
    if abs(x - round(x)) < 0.005:
        return f"€{int(round(x)):,}".replace(",", ".").replace("€-", "−€")
    return f"€{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".").replace("€-", "−€")


def pct(x, d=1):
    return f"{x * 100:.{d}f}%".replace(".", ",")


def odd(x):
    return f"{x:.2f}".replace(".", ",")


def a(k, tekst):
    return f'<a href="{L[k]}">{tekst}</a>'


# ---------- rekenvoorbeelden ----------
# value betting: jouw kans 50%, quotering 2,20
VB_KANS, VB_ODD = 0.50, 2.20
VB_EV = VB_KANS * VB_ODD - 1
assert pct(VB_EV) == "10,0%" and pct(1 / VB_ODD) == "45,5%"

# arbitrage: twee-wegmarkt, 2,10 bij bookmaker A en 2,05 bij bookmaker B, €100 totaal
ARB_A, ARB_B, ARB_TOT = 2.10, 2.05, 100
ARB_SOM = 1 / ARB_A + 1 / ARB_B
ARB_IN_A = round(ARB_TOT * (1 / ARB_A) / ARB_SOM, 2)
ARB_IN_B = round(ARB_TOT - ARB_IN_A, 2)
ARB_UIT_A, ARB_UIT_B = round(ARB_IN_A * ARB_A, 2), round(ARB_IN_B * ARB_B, 2)
assert (ARB_IN_A, ARB_IN_B) == (49.4, 50.6) and (ARB_UIT_A, ARB_UIT_B) == (103.74, 103.73) and ARB_SOM < 1

# martingale: €10 start, 6 verliezen op rij
assert sum(10 * 2 ** i for i in range(6)) == 630

# accumulator: 4 selecties van 1,80, elk 52% kans
ACCA = 1.80 ** 4
ACCA_KANS = 0.52 ** 4
assert odd(ACCA) == "10,50" and pct(ACCA_KANS) == "7,3%" and pct(ACCA_KANS * ACCA - 1) == "-23,2%" and pct(0.52 * 1.80 - 1) == "-6,4%"

# bankroll: vaste inzet als percentage van je bankroll
BANKROLLS, PERCS = (100, 250, 500), (0.01, 0.02, 0.03)
BR_RIJEN = [(f"<strong>{eur(b)}</strong>", *[eur(b * p) for p in PERCS]) for b in BANKROLLS]
assert BR_RIJEN[1][2] == "€5" and BR_RIJEN[2][3] == "€15" and BR_RIJEN[0][1] == "€1"

OVERZICHT = [
    ("<strong>" + a("value", "Value betting") + "</strong>", "Inzetten als jouw kans hoger is dan de quotering aangeeft", "Gemiddeld", "Wedders die zelf kansen willen inschatten"),
    ("<strong>" + a("matched", "Matched betting") + "</strong>", "Free bets en bonussen afdekken met een tegengestelde weddenschap", "Laag tot gemiddeld", "Precieze rekenaars die voorwaarden goed lezen"),
    ("<strong>" + a("arb", "Arbitrage") + "</strong>", "Alle uitkomsten afdekken bij verschillende bookmakers door verschillen in odds", "Laag per bet, hoog praktisch risico", "Snelle wedders met accounts bij meerdere legale aanbieders"),
    ("<strong>" + a("mart", "Martingale") + "</strong>", "Inzet verdubbelen na elk verlies", "Zeer hoog", "Niemand die zijn bankroll wil beschermen"),
    ("<strong>" + a("fib", "Fibonacci") + "</strong>", "Inzet volgt 1-1-2-3-5-8, vaak op gelijkspel", "Hoog", "Wedders die een vaste structuur willen, met strak eindpunt"),
    ("<strong>" + a("acca", "Accumulator") + "</strong>", "Meerdere selecties op één wedbriefje, quoteringen worden vermenigvuldigd", "Hoog", "Wie kleine inzet wil voor een grote uitbetaling"),
    ("<strong>" + a("live", "Live wedden") + "</strong>", "Inzetten tijdens de wedstrijd op basis van wat je ziet", "Gemiddeld tot hoog", "Wedders die de wedstrijd echt volgen"),
    ("<strong>" + a("hc", "Handicap wedden") + "</strong>", "Een team krijgt een virtuele voor- of achterstand", "Gemiddeld", "Wie op favorieten wil wedden tegen betere quoteringen"),
    ("<strong>" + a("eh", "Europese handicap") + "</strong>", "Hele handicap, gelijkspel blijft een aparte uitkomst", "Gemiddeld", "Wie een hogere quotering zoekt en een duidelijke uitslag verwacht"),
    ("<strong>" + a("ah", "Asian handicap") + "</strong>", "Halve en kwartlijnen, geen gelijkspel, soms inzet terug", "Laag tot gemiddeld", "Wedders die hun risico willen spreiden"),
]
assert len(OVERZICHT) == 10

content = f"""<p><strong>Een wedstrategie is een vaste aanpak voor waarop je wedt en hoeveel je inzet. De bekendste zijn value betting, matched betting, arbitrage, inzetsystemen zoals martingale en Fibonacci, accumulators, live wedden en handicap wedden. Ze verschillen sterk in risico. Geen enkele strategie garandeert winst: de bookmaker bouwt altijd een marge in, en systemen die je inzet na verlies verhogen, maken je verlies alleen groter.</strong></p>
<p>Op deze pagina zie je alle wedstrategieën op een rijtje, met per strategie hoe het werkt, hoe groot het risico is en voor wie het geschikt is. Bij elke strategie vind je een link naar de volledige uitleg met rekenvoorbeelden. Onderaan lees je hoe je je bankroll beheert, want dat is bij elke strategie de basis.</p>
<h3><strong>Welke wedstrategieën zijn er?</strong></h3>
{tabel(["Strategie", "Hoe het werkt", "Risico", "Voor wie"], OVERZICHT)}
<p>Je kunt de strategieën grofweg in drie groepen verdelen. <strong>Kansstrategieën</strong> zoals value betting draaien om het vinden van te hoge quoteringen. <strong>Afdekstrategieën</strong> zoals matched betting en arbitrage proberen het risico weg te nemen door meerdere weddenschappen te combineren. <strong>Inzetsystemen</strong> zoals martingale en Fibonacci bepalen alleen hoeveel je inzet. Daarnaast zijn er <strong>typen weddenschappen</strong>, zoals accumulators en handicaps, die je met elke strategie kunt combineren.</p>
<h3><strong>Value betting: de kans tegenover de quotering</strong></h3>
<p>Bij value betting zoek je weddenschappen waarbij de quotering hoger is dan de echte kans rechtvaardigt. Een quotering van {odd(VB_ODD)} staat voor een kans van {pct(1 / VB_ODD)}. Schat jij de kans op {pct(VB_KANS, 0)}, dan is je verwachte rendement {pct(VB_EV, 0)} van je inzet. De quoteringen in de voorbeelden op deze pagina zijn fictief. Het lastige is dat je kansinschatting beter moet zijn dan die van de bookmaker, en dat lukt alleen met kennis, discipline en veel weddenschappen. Lees meer over {a("value", "value betting")}.</p>
<h3><strong>Matched betting: bonussen afdekken</strong></h3>
<p>Bij matched betting gebruik je een free bet of bonus en dek je de uitkomst af met een tegengestelde weddenschap, zodat je het bonusbedrag (deels) omzet in echt geld. Op papier is het risico klein. In Nederland is de praktijk lastiger: bonussen hebben vaak inzetvereisten en minimale quoteringen, je krijgt een welkomstbonus meestal maar één keer, en wie de netto stortingslimiet overschrijdt, krijgt minimaal dertig dagen geen bonussen. Het kabinet wil bonussen bovendien verder aan banden leggen. Bookmakers kunnen accounts beperken als ze bonusmisbruik vermoeden. Lees de volledige uitleg over {a("matched", "matched betting")} en bekijk de actuele <a href="/bonussen/free-bets">free bets</a>.</p>"""

content2 = f"""<h3><strong>Arbitrage wedden: verschillen tussen bookmakers</strong></h3>
<p>Bij arbitrage dek je alle uitkomsten af bij verschillende bookmakers, omdat hun quoteringen zo ver uit elkaar liggen dat je altijd iets overhoudt. Een voorbeeld op een markt met twee uitkomsten:</p>
{tabel(["", "Bookmaker A", "Bookmaker B"], [
    ("<strong>Uitkomst</strong>", "Over 2,5 goals", "Under 2,5 goals"),
    ("<strong>Quotering</strong>", odd(ARB_A), odd(ARB_B)),
    ("<strong>Inzet</strong>", eur(ARB_IN_A), eur(ARB_IN_B)),
    ("<strong>Uitbetaling als deze kant wint</strong>", eur(ARB_UIT_A), eur(ARB_UIT_B)),
])}
<p>Met {eur(ARB_TOT)} totale inzet krijg je hoe dan ook ongeveer {eur(ARB_UIT_B)} terug. Zulke kansen zijn zeldzaam, verdwijnen snel en leveren meestal maar een paar procent op. Bookmakers zien arbitrage niet graag en kunnen de limieten van een account aanpassen. Een quotering die verandert voordat je tweede weddenschap staat, maakt van een "zekere" winst een gewone gok. Meer in de uitleg over {a("arb", "arbitrage wedden")}.</p>
<h3><strong>Martingale: verdubbelen na verlies</strong></h3>
<p>Bij martingale verdubbel je je inzet na elk verlies, zodat de eerste winst alles goedmaakt. Het werkt tot het misgaat: zes verliezen op rij kosten je met €10 als startinzet al €630, voor een winst van €10. Inzetlimieten en de netto stortingslimiet houden je bovendien vaak tegen voordat je je verlies hebt teruggewonnen. Lees waarom {a("mart", "het martingale systeem")} op lange termijn faalt.</p>
<h3><strong>Fibonacci: wedden op gelijkspel</strong></h3>
<p>De Fibonacci-methode volgt de reeks 1, 1, 2, 3, 5, 8, 13 als inzetladder. Na een verlies ga je een stap verder, na een winst twee stappen terug. Veel wedders gebruiken het op gelijkspel, omdat die quotering meestal 3,00 of hoger is. Maar in de Eredivisie van 2025/26 eindigde maar 26,1% van de wedstrijden gelijk, en reeksen van tien duels zonder remise komen geregeld voor. Bekijk de rekentabel bij {a("fib", "de Fibonacci wedstrategie")}.</p>
<h3><strong>Accumulators: meerdere wedstrijden op één briefje</strong></h3>
<p>Bij een accumulator (combinatieweddenschap) vermenigvuldig je de quoteringen. Vier selecties van 1,80 geven samen een quotering van {odd(ACCA)}. Alle vier moeten wel goed zijn. Is de kans per selectie 52%, dan win je het briefje maar in {pct(ACCA_KANS)} van de gevallen, en omdat de marge van de bookmaker zich ook vermenigvuldigt, verlies je op termijn meer dan bij losse weddenschappen. Leuk met een kleine inzet, geen manier om stabiel te winnen. Lees de uitleg over {a("acca", "accumulator weddenschappen")}.</p>
<h3><strong>Live wedden: inspelen op de wedstrijd</strong></h3>
<p>Bij live wedden zet je in terwijl de wedstrijd bezig is. Je kunt reageren op wat je ziet: een rode kaart, een team dat duidelijk de overhand heeft of een blessure. De quoteringen bewegen snel en de marge is live vaak hoger. Het grootste risico zit in impulsief gedrag: na een tegendoelpunt snel nog even inzetten. Spreek vooraf af hoeveel je live wilt inzetten. Meer in {a("live", "de uitleg over in-play wedden")}, en via <a href="/live-kijken">live kijken</a> zie je waar je de wedstrijd volgt.</p>"""

content3 = f"""<h3><strong>Handicap wedden: Europees en Aziatisch</strong></h3>
<p>Bij handicap wedden krijgt een team een virtuele voor- of achterstand. Zo krijg je een betere quotering op een duidelijke favoriet, of meer zekerheid op een underdog. Er zijn twee hoofdvormen:</p>
<ul><li><strong>Europese handicap:</strong> een hele handicap, zoals −1. Het gelijkspel na handicap is een aparte uitkomst, waardoor je drie keuzes hebt en vaak hogere quoteringen krijgt. Lees {a("eh", "wat een Europese handicap is")}.</li><li><strong>Asian handicap:</strong> halve en kwartlijnen, zoals −0,5 of −0,75. Er is geen gelijkspel en bij sommige lijnen krijg je je inzet (deels) terug. Lees {a("ah", "hoe een Asian handicap werkt")}.</li></ul>
<p>Alle soorten naast elkaar, met de verschillen en rekenvoorbeelden, vind je in {a("hc", "de complete gids over handicap wedden")}.</p>
<h3><strong>Bankroll management: de basis van elke strategie</strong></h3>
<p>Welke strategie je ook kiest, het belangrijkste is hoeveel je inzet. Bankroll management betekent dat je vooraf een vast bedrag reserveert dat je kunt missen, en per weddenschap maar een klein deel daarvan inzet. Een veelgebruikte regel is 1 tot 3% per weddenschap:</p>
{tabel(["Bankroll", "1% per bet", "2% per bet", "3% per bet"], BR_RIJEN)}
<ul><li><strong>Vaste inzet:</strong> zet steeds hetzelfde percentage in, ook na een verlies. Zo kan geen enkele reeks je bankroll in één keer leegmaken.</li><li><strong>Geen verliezen najagen:</strong> verhoog je inzet niet om terug te winnen wat je kwijt bent.</li><li><strong>Houd alles bij:</strong> noteer je weddenschappen, quoteringen en resultaten. Zo zie je eerlijk of een aanpak werkt.</li><li><strong>Vergelijk quoteringen:</strong> een iets hogere quotering is bij elke strategie winst. Gebruik de <a href="/odds-vergelijken-bij-alle-bookmakers-beste-odds-vandaag">odds vergelijker</a>.</li><li><strong>Gebruik limieten:</strong> stel bij je bookmaker zelf een stortings- en speellimiet in die past bij je budget.</li></ul>
<h3><strong>Verantwoord wedden</strong></h3>
<p>Een strategie kan wedden overzichtelijker maken, maar het blijft een kansspel. Zie je inzet als geld voor je plezier, niet als manier om geld te verdienen. Merk je dat je meer inzet dan je wilt, vaker speelt of verliezen probeert terug te winnen, neem dan pauze. Je kunt jezelf via Cruks laten uitsluiten van alle legale aanbieders. Meer tips en hulp vind je op onze pagina over <a href="/speel-bewust/verantwoord-wedden">verantwoord wedden</a>.</p>
<h3><strong>Mag je deze wedstrategieën gebruiken in Nederland?</strong></h3>
<p>Ja, alle strategieën op deze pagina zijn toegestaan, zolang je speelt bij een bookmaker met een vergunning van de Kansspelautoriteit. Spelen bij een aanbieder zonder Nederlandse vergunning is illegaal. Let wel op twee dingen. Bookmakers mogen in hun voorwaarden regels stellen over bonussen, maximuminzetten en het beperken van accounts. En sommige markten mogen in Nederland helemaal niet worden aangeboden, zoals weddenschappen op corners en kaarten. Lees <a href="/nieuws/dit-is-waarom-wedden-op-corners-niet-meer-legaal-is-in-nederland">waarom wedden op corners niet legaal is</a> en <a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je controleert of een bookmaker legaal is</a>. Alle legale aanbieders vind je bij onze <a href="/bookmakers">bookmakers</a>.</p>
<p>Legale bookmakers die wij aanraden:</p>
{aanraders()}
<h3><strong>Veelgestelde vragen over wedstrategieën</strong></h3>
<p><strong>Wat is de beste wedstrategie?</strong><br>Er is geen strategie die altijd wint. Value betting is de enige aanpak die op termijn een voordeel kan opleveren, maar alleen als je kansen beter inschat dan de bookmaker. Goed bankroll management is bij elke strategie het belangrijkst.</p>
<p><strong>Bestaat er een wedstrategie die winst garandeert?</strong><br>Nee. Arbitrage en matched betting komen het dichtst in de buurt, maar ook daar lopen het risico op fouten, veranderende quoteringen, voorwaarden en beperkte accounts mee.</p>
<p><strong>Zijn inzetsystemen zoals martingale en Fibonacci zinvol?</strong><br>Ze bepalen alleen hoeveel je inzet, niet of je wint. Na een verliesreeks loopt je inzet snel op. Het voordeel van de bookmaker blijft bestaan.</p>
<p><strong>Is arbitrage wedden legaal in Nederland?</strong><br>Ja, het is niet verboden. Wel kunnen bookmakers volgens hun voorwaarden de limieten van een account aanpassen als ze arbitrage zien.</p>
<p><strong>Wat is het verschil tussen een strategie en een type weddenschap?</strong><br>Een type weddenschap, zoals een accumulator of handicap, is wat je speelt. Een strategie is hoe je kiest en hoeveel je inzet. Je kunt bijvoorbeeld value betting toepassen op een Asian handicap.</p>
<p><strong>Hoeveel moet ik per weddenschap inzetten?</strong><br>Een veelgebruikte richtlijn is 1 tot 3% van je bankroll per weddenschap. Met een bankroll van €250 is dat €2,50 tot €7,50.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    alles = content + content2 + content3
    tekst = re.sub(r"<[^>]+>", " ", alles)
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", len(tekst.split()), "woorden")
    assert not re.search(r"<(ul|ol|/li)>\s+<", alles) and "/kennisbank/" not in alles
    assert alles.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>") and "<h2" not in alles
    assert all(f'href="{u}"' in alles for u in L.values())   # hub linkt naar elk strategie-artikel
    if "--live" in sys.argv:   # ---- LIVE: alleen draaien na akkoord van Jasper ----
        import lk_webflow as WF
        fd = {"name": TITEL, "content": content, "content-2": content2, "content-3": content3,
              "samenvatting": SAMENVATTING, "rubriek": RUBRIEK,
              "publicatiedatum": datetime.now(timezone.utc).isoformat()}
        print(WF.update_live(ITEM_ID, fd).get("lastPublished"))
