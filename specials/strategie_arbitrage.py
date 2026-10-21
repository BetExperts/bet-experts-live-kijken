# -*- coding: utf-8 -*-
"""Herschrijving Nieuws-item 650487e434e7a24deccee8f6 (Kennisbank-versie is offline + 301):
Wat is arbitrage wedden? Surebets uitgelegd met rekenvoorbeeld.
GSC-queries: "arbitrage gokken uitleg", "arbitrage betting nederland", "arbitrage gokken sport".
Feiten nagelopen op 21-10-2026:
- Geen betting exchange onder de vergunninghouders in de Kansspelwijzer van de Ksa (legaal_data.py, stand 21-10-2026).
- Netto stortingslimiet: €300 (18-23 jaar) / €700 (24+) per kalendermaand, per aanbieder (zie netto_stortingslimiet.py).
- Kansspelbelasting 37,8% per 1-1-2026 (Belastingdienst); bij een aanbieder met Ksa-vergunning betaalt de aanbieder.
- Kennelijke-fout-regels, inzetlimieten en ongeldig verklaren: algemene voorwaarden van bookmakers (geen wettelijke regel).
Alle bedragen worden hieronder berekend en ge-assert.
  python3 specials/strategie_arbitrage.py [--live]"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
import lk_webflow as WF
from legaal_data import tabel, aanraders

ITEM_ID = "650487e434e7a24deccee8f6"
SLUG = "wat-is-arbitrage-wedden-de-kunst-van-de-risicovrije-winst"
RUBRIEK = "6502b64b78efefb4144fd2c1"
TITEL = "Wat is arbitrage wedden? Surebets uitgelegd met voorbeeld"
SAMENVATTING = ("Arbitrage wedden uitgelegd: zo herken je een surebet, verdeel je je inzet over 2 of 3 uitkomsten "
                "en lees je waarom het in Nederland zelden werkt.")

OG_KOP = "Arbitrage <span>wedden</span>"
OG_EYEBROW = "Surebets uitgelegd"
OG_CHIPS = ["Som 1/odds onder 1", "Met rekenvoorbeeld"]
OG_MOTIEF = "odds"
OG_DATA = ["Bookmaker A · Speler A 2,10", "Bookmaker B · Speler B 2,05", "Winst · €3,73 op €100"]


def eur(x):
    s = f"€{abs(x):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return ("−" + s) if x < -0.004 else s


def odd(x):
    return f"{x:.2f}".replace(".", ",")


def pct(x, d=1):
    return f"{x * 100:.{d}f}%".replace(".", ",")


def r2(x):
    return round(x + 1e-9, 2)


def verdeel(odds, totaal):
    """Inzet per uitkomst zodat elke uitkomst evenveel oplevert; laatste inzet sluit af op het totaal."""
    s = sum(1 / o for o in odds)
    inz = [r2(totaal * (1 / o) / s) for o in odds[:-1]]
    inz.append(r2(totaal - sum(inz)))
    return s, inz, [r2(i * o) for i, o in zip(inz, odds)]


# Impliciete kans
KANS_RIJEN = [(odd(o), pct(1 / o)) for o in (1.50, 2.00, 2.05, 2.10, 3.00, 4.00)]
assert KANS_RIJEN[3] == ("2,10", "47,6%") and KANS_RIJEN[2] == ("2,05", "48,8%")

# 2-weg: tennis, Speler A bij bookmaker A, Speler B bij bookmaker B
OA, OB2, T2 = 2.10, 2.05, 100
S2, (IA, IB), (UA, UB) = verdeel([OA, OB2], T2)
assert round(S2, 4) == 0.9640 and (IA, IB) == (49.40, 50.60) and (UA, UB) == (103.74, 103.73)
WINST2 = r2(min(UA, UB) - T2)
assert WINST2 == 3.73
# zelfde wedstrijd zonder arbitrage (2,10 en 1,80 bij dezelfde bookmaker)
S_GEEN = 1 / 2.10 + 1 / 1.80
assert S_GEEN > 1 and pct(S_GEEN) == "103,2%"

# 3-weg: 1X2 bij drie bookmakers
O3, T3 = [2.60, 3.70, 3.20], 200
S3, I3, U3 = verdeel(O3, T3)
assert round(S3, 4) == 0.9674 and I3 == [79.52, 55.88, 64.60] and U3 == [206.75, 206.76, 206.72]
WINST3 = r2(min(U3) - T3)
assert WINST3 == 6.72

# Wat kan misgaan
# a) quotering B zakt naar 1,90 voordat je de tweede weddenschap plaatst
OB_NIEUW = 1.90
IB_NIEUW = r2(IA * OA / OB_NIEUW)
VERLIES_ZAKT = r2(UA - (IA + IB_NIEUW))
assert IB_NIEUW == 54.60 and VERLIES_ZAKT == -0.26
# b) weddenschap bij bookmaker B wordt ongeldig verklaard (inzet terug), A staat open
OPEN_WINT, OPEN_VERLIEST = r2(IA * (OA - 1)), -IA
assert OPEN_WINT == 54.34 and OPEN_VERLIEST == -49.40
# c) omzet nodig voor €100 winst bij 3% arbitrage
OMZET = round(100 / 0.03)
assert OMZET == 3333

content = f"""<p><strong>Arbitrage wedden, ook wel surebetting of arbing genoemd, betekent dat je op alle uitkomsten van een wedstrijd inzet bij verschillende bookmakers, zodat je bij elke uitslag winst maakt. Dat kan alleen als de bookmakers het zo oneens zijn dat de hoogste quoteringen samen een kans van minder dan 100% aangeven. De winst is meestal 1 tot 3% van je inzet. In theorie is het risicovrij, maar in de praktijk zorgen bewegende odds, ongeldige weddenschappen en inzetlimieten ervoor dat het zelden zo uitpakt.</strong></p>
<p>Het idee komt uit de financiële wereld, waar handelaren prijsverschillen tussen markten benutten. Bij sportweddenschappen is het principe hetzelfde: elke bookmaker maakt zijn eigen prijs, en soms lopen die zo ver uiteen dat je beide kanten met winst kunt spelen. Hieronder lees je hoe je een surebet herkent, hoe je je inzet verdeelt bij twee en drie uitkomsten, en waarom arbitrage in Nederland vooral een rekenoefening is. De quoteringen in de voorbeelden zijn fictief.</p>
<h3><strong>Wat zegt een quotering over de kans?</strong></h3>
<p>Elke quotering is een vertaling van een kans. De <strong>impliciete kans</strong> reken je uit met 1 gedeeld door de odd. Een quotering van 2,00 staat voor 50%, een quotering van 4,00 voor 25%.</p>
{tabel(["Quotering", "Impliciete kans (1 ÷ odd)"], KANS_RIJEN)}
<p>Bij één bookmaker tellen de impliciete kansen van alle uitkomsten samen altijd op tot méér dan 100%. Dat overschot is de marge van de bookmaker. Bied een bookmaker bij een tenniswedstrijd 2,10 op speler A en 1,80 op speler B, dan is de som {pct(S_GEEN)}: de bookmaker houdt gemiddeld zo'n 3% van alle inzetten over.</p>
<h3><strong>Hoe herken je een arbitragekans?</strong></h3>
<p>Een surebet ontstaat als je per uitkomst de <strong>hoogste quotering bij verschillende bookmakers</strong> pakt en de impliciete kansen samen onder de 100% blijven. De test is simpel:</p>
<ul><li><strong>Tel 1 ÷ odd op voor elke uitkomst</strong>, telkens met de beste odd die je kunt vinden.</li><li><strong>Is de som lager dan 1</strong> (minder dan 100%), dan is er een arbitragekans.</li><li><strong>Je winstpercentage</strong> is ongeveer 1 ÷ som − 1. Bij een som van 0,97 is dat ruim 3%.</li></ul>
<p>De eenvoudigste manier om die hoogste quoteringen naast elkaar te zien, is een oddsvergelijker. Met onze <a href="/odds-vergelijken-bij-alle-bookmakers-beste-odds-vandaag">odds vergelijker</a> zie je per wedstrijd welke legale bookmaker de beste odd heeft.</p>
<h3><strong>Hoe verdeel je je inzet?</strong></h3>
<p>Je wilt bij elke uitslag hetzelfde bedrag terugkrijgen. Dat bereik je door je totale inzet te verdelen naar verhouding van de impliciete kansen:</p>
<p><strong>Inzet per uitkomst = totale inzet × (1 ÷ odd van die uitkomst) ÷ som van alle 1 ÷ odd</strong></p>
<p>De uitbetaling is dan bij elke uitslag gelijk aan totale inzet ÷ som. Alles boven je totale inzet is winst.</p>"""

content2 = f"""<p><strong>Rekenvoorbeeld met twee uitkomsten</strong></p>
<p>In een tenniswedstrijd biedt bookmaker A {odd(OA)} op speler A en bookmaker B {odd(OB2)} op speler B. De som is 1 ÷ {odd(OA)} + 1 ÷ {odd(OB2)} = {f'{S2:.4f}'.replace('.', ',')}, dus {pct(S2)}. Dat is minder dan 100%: een surebet van ruim 3,6%. Je zet in totaal €{T2} in.</p>
{tabel(["", "Bookmaker A: speler A", "Bookmaker B: speler B"], [
    ("Quotering", odd(OA), odd(OB2)),
    ("Inzet", eur(IA), eur(IB)),
    ("Uitbetaling als deze kant wint", eur(UA), eur(UB)),
    ("Winst op je totale inzet van €100", f"<strong>{eur(r2(UA - T2))}</strong>", f"<strong>{eur(r2(UB - T2))}</strong>"),
])}
<p>Wint speler A, dan krijg je {eur(UA)} terug bij bookmaker A en ben je de {eur(IB)} bij bookmaker B kwijt. Wint speler B, dan is het andersom. Beide keren houd je ongeveer {eur(WINST2)} over. Het verschil van een cent komt door het afronden van de inzet.</p>
<p><strong>Rekenvoorbeeld met drie uitkomsten</strong></p>
<p>Bij voetbal (1X2) heb je drie uitkomsten nodig. Stel dat drie bookmakers deze quoteringen geven: thuiswinst {odd(O3[0])} bij bookmaker A, gelijkspel {odd(O3[1])} bij bookmaker B en uitwinst {odd(O3[2])} bij bookmaker C. De som is 1 ÷ 2,60 + 1 ÷ 3,70 + 1 ÷ 3,20 = {pct(S3)}. Je zet in totaal €{T3} in.</p>
{tabel(["Uitkomst", "Bookmaker", "Quotering", "Inzet", "Uitbetaling"], [
    ("Thuiswinst", "A", odd(O3[0]), eur(I3[0]), eur(U3[0])),
    ("Gelijkspel", "B", odd(O3[1]), eur(I3[1]), eur(U3[1])),
    ("Uitwinst", "C", odd(O3[2]), eur(I3[2]), eur(U3[2])),
    ("<strong>Totaal</strong>", "", "", f"<strong>{eur(T3)}</strong>", f"<strong>minimaal {eur(min(U3))}</strong>"),
])}
<p>Bij elke uitslag houd je minimaal {eur(WINST3)} over, ruim 3% van je inzet. Daarvoor heb je wel saldo nodig bij drie verschillende bookmakers, en moet je drie weddenschappen plaatsen voordat een van de quoteringen verandert.</p>
<h3><strong>Waarom arbitrage in de praktijk zelden werkt</strong></h3>
<p>Op papier is arbitrage de enige strategie met gegarandeerde winst. In de praktijk gaat het vaak mis, en meestal op een manier die de kleine winst in één keer wegvaagt.</p>
<p><strong>1. De odds bewegen</strong></p>
<p>Een surebet bestaat vaak maar een paar minuten. Stel dat je {eur(IA)} hebt ingezet op speler A tegen {odd(OA)}, en dat de odd op speler B zakt naar {odd(OB_NIEUW)} voordat je de tweede weddenschap plaatst. Om toch gedekt te zijn, moet je nu {eur(IB_NIEUW)} op speler B zetten. Je totale inzet wordt {eur(r2(IA + IB_NIEUW))} voor een uitbetaling van {eur(UA)}: een verlies van {eur(-VERLIES_ZAKT)}, ongeacht de uitslag.</p>
<p><strong>2. Een weddenschap wordt ongeldig verklaard</strong></p>
<p>Een uitzonderlijk hoge quotering is vaak gewoon een fout van de bookmaker. In de algemene voorwaarden staat bijna altijd dat de bookmaker een weddenschap tegen een kennelijk foute odd ongeldig mag verklaren of tegen de juiste odd mag afrekenen. Gebeurt dat bij bookmaker B, dan krijg je daar je inzet terug, maar staat je weddenschap bij bookmaker A gewoon open. Je hebt dan geen surebet meer, maar een gewone gok van {eur(IA)}: je wint {eur(OPEN_WINT)} of je verliest {eur(IA)}.</p>
<p><strong>3. Verschillende regels per bookmaker</strong></p>
<p>Geeft een tennisspeler op na één set, dan rekent de ene bookmaker de weddenschap af en verklaart de andere hem ongeldig. Bij voetbal verschillen de regels voor gestaakte of verplaatste wedstrijden. Speel je beide kanten bij bookmakers met verschillende regels, dan kan één uitslag aan de ene kant verlies en aan de andere kant inzet terug opleveren.</p>
<p><strong>4. Inzetlimieten en beperkte accounts</strong></p>
<p>Bookmakers zien arbitrage niet graag, omdat je alleen hun hoogste (vaak verkeerde) prijzen pakt. Wie steeds op afwijkende odds inzet, valt op. Bookmakers mogen volgens hun voorwaarden de maximale inzet per klant verlagen of je uitsluiten van promoties. Dan kun je nog maar een paar euro inzetten, en is arbitrage voorbij.</p>
<p><strong>5. Kleine winst, grote omzet</strong></p>
<p>Bij 3% winst per surebet moet je zo'n €{f'{OMZET:,}'.replace(',', '.')} inzetten om €100 te verdienen. Eén mislukte arb door een ongeldige weddenschap of een rekenfout kost al snel meer dan tien geslaagde opleveren.</p>
{tabel(["Wat gaat er mis?", "Gevolg", "Hoe beperk je het?"], [
    ("Odd zakt tijdens het plaatsen", f"Je dekking wordt duurder, bijvoorbeeld {eur(-VERLIES_ZAKT)} verlies op €104", "Plaats eerst de weddenschap met de odd die het snelst verandert"),
    ("Weddenschap ongeldig door een kennelijke fout", f"Eén kant staat open: {eur(OPEN_WINT)} winst of {eur(IA)} verlies", "Wantrouw odds die ver boven de rest liggen"),
    ("Verschillende afhandelingsregels", "Verlies aan de ene en inzet terug aan de andere kant", "Lees de sportregels van beide bookmakers"),
    ("Inzetlimiet", "Je kunt de berekende inzet niet plaatsen", "Check de maximale inzet vóór je eerste weddenschap"),
    ("Rekenfout of verkeerde markt", "Geen dekking", "Controleer markt, lijn en odd twee keer"),
])}"""

content3 = f"""<h3><strong>Arbitrage wedden in Nederland</strong></h3>
<p>In Nederland mag je alleen wedden bij bookmakers met een vergunning van de Kansspelautoriteit. Dat maakt arbitrage lastiger dan in landen met honderden aanbieders:</p>
<ul><li><strong>Weinig aanbieders:</strong> er zijn maar ruim twintig legale merken met een sportvergunning. Hoe minder bookmakers, hoe kleiner de kans op een groot prijsverschil.</li><li><strong>Gedeelde odds:</strong> meerdere Nederlandse bookmakers gebruiken hetzelfde platform voor hun quoteringen. Hun odds liggen dan dicht bij elkaar, en arbitrage tussen die merken bestaat bijna nooit.</li><li><strong>Geen exchange:</strong> geen enkele vergunninghouder biedt een betting exchange aan (stand oktober 2026). In het buitenland gebruiken arbers die vaak als vaste tweede kant.</li><li><strong>Stortingslimiet per aanbieder:</strong> netto €300 per maand tot je 24e en €700 daarna. Je saldo staat verspreid over meerdere accounts, en een limiet bereik je snel.</li><li><strong>Kleinere markten:</strong> sommige markten mogen in Nederland niet worden aangeboden, zoals corners en kaarten. Lees <a href="/nieuws/dit-is-waarom-wedden-op-corners-niet-meer-legaal-is-in-nederland">waarom wedden op corners niet legaal is</a>.</li></ul>
<p>Buitenlandse sites met "betere" odds zijn geen alternatief. Een aanbieder zonder Nederlandse vergunning is illegaal, en daar heb je geen enkele garantie dat je winst wordt uitbetaald. Precies bij arbitrage, waar je winst van beide kanten afhangt, is dat een groot risico. Twijfel je, lees dan <a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je weet of een bookmaker legaal is</a>.</p>
<h3><strong>Arbitrage, matched betting en value betting: het verschil</strong></h3>
{tabel(["Strategie", "Waar komt de winst vandaan?", "Risico"], [
    ("<strong>Arbitrage</strong>", "Prijsverschil tussen bookmakers, alle uitkomsten gedekt", "Laag in theorie, in de praktijk ongeldige weddenschappen en limieten"),
    ("<strong>Matched betting</strong>", "De waarde van een bonus of free bet", "Laag per actie, afhankelijk van bonusregels"),
    ("<strong>Value betting</strong>", "Een quotering die hoger is dan de echte kans", "Hoog op korte termijn, je dekt niets af"),
])}
<p>Meer over de andere twee lees je in onze uitleg over <a href="/nieuws/wat-houdt-de-wedstrategie-matched-betting-in">matched betting</a> en <a href="/nieuws/wat-is-de-wedstrategie-value-betting">value betting</a>. Ook als arbitrage niet lukt, is de onderliggende les nuttig: wie altijd de hoogste odd pakt, betaalt minder marge. Alle strategieën op een rij vind je in ons overzicht van <a href="/nieuws/alle-verschillende-wedstrategieen-op-een-rijtje">wedstrategieën</a>.</p>
<h3><strong>Mag je arbitrage wedden in Nederland?</strong></h3>
<p>Ja. Arbitrage is niet verboden: je plaatst gewone weddenschappen bij legale bookmakers. Een bookmaker mag wel zelf bepalen hoeveel hij van jou accepteert, en kan je account beperken. Bij een legale bookmaker betaal je geen belasting over je winst; de aanbieder draagt de kansspelbelasting af (37,8% in 2026).</p>
<p>Legale bookmakers die wij aanraden:</p>
{aanraders()}
<h3><strong>Veelgestelde vragen over arbitrage wedden</strong></h3>
<p><strong>Is arbitrage wedden echt risicovrij?</strong><br>Alleen als alle weddenschappen geplaatst worden zoals berekend en ook zo worden afgerekend. Bewegende odds, ongeldig verklaarde weddenschappen en verschillende regels per bookmaker maken het in de praktijk riskant.</p>
<p><strong>Hoe weet ik of iets een surebet is?</strong><br>Tel voor elke uitkomst 1 ÷ de hoogste odd op. Komt de som onder 1 uit, dan is het een surebet. Bij 2,10 en 2,05 is de som 0,964.</p>
<p><strong>Hoeveel winst levert een surebet op?</strong><br>Meestal 1 tot 3% van je totale inzet. Op €100 is dat €1 tot €3.</p>
<p><strong>Is arbitrage wedden illegaal?</strong><br>Nee, zolang je bij bookmakers met een Nederlandse vergunning speelt. Het is wel tegen het belang van de bookmaker, en die kan je inzetten beperken.</p>
<p><strong>Waarom zijn er in Nederland zo weinig surebets?</strong><br>Er zijn relatief weinig legale bookmakers, een deel gebruikt hetzelfde oddsplatform en er is geen legale exchange. Daardoor liggen de prijzen dicht bij elkaar.</p>
<p><strong>Wat is het verschil met hedgen?</strong><br>Bij hedgen dek je een bestaande weddenschap later (deels) af om winst vast te zetten of verlies te beperken. Bij arbitrage plaats je alle weddenschappen tegelijk en ligt de winst vanaf het begin vast.</p>
<p><strong>Kan ik arbitrage live doen?</strong><br>Dat kan, maar live bewegen odds nog sneller en schorten bookmakers markten vaak op. Lees meer over <a href="/nieuws/uitleg-in-play-live-wedden-dynamiek-strategie-en-kansen-in-realtime">live wedden</a>.</p>
<p>Wedden blijft een kansspel. Zet nooit geld in dat je niet kunt missen, en lees onze tips over <a href="/speel-bewust/verantwoord-wedden">verantwoord wedden</a>.</p>
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
