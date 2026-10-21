# -*- coding: utf-8 -*-
"""Herschrijving Nieuws-item 65048d353042ab3595ee1f76 (Kennisbank-versie offline + 301): Accumulator / combinatieweddenschap
(combi, accu, parlay): odds vermenigvuldigen, rekenvoorbeelden, stapelende marge, systeemweddenschappen, bet builder.
Feiten nagelopen op 21-10-2026:
- Bijlage 2, onderdeel 2.3 Regeling kansspelen op afstand (BWBR0044767): corners, kaarten e.d. ook verboden binnen een
  bet builder/combinatie (zelfde verbod, zie corners_niet_legaal.py).
- Alle bedragen, marges en systeemaantallen worden hieronder berekend en ge-assert. Geen merk-specifieke bonusvoorwaarden
  genoemd (verschillen per bookmaker en wijzigen vaak).
  python3 specials/strategie_accumulator.py [--live]"""
import os, sys
from math import comb, prod
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
import lk_webflow as WF
from legaal_data import tabel, aanraders

ITEM_ID = "65048d353042ab3595ee1f76"   # Nieuws
SLUG = "uitleg-wedstrategie-accumulator-weddenschappen"
RUBRIEK = "6502b64b78efefb4144fd2c1"
TITEL = "Accumulator wedden: zo werkt een combinatieweddenschap"
SAMENVATTING = ("Wat is een accumulator (combi)? Zo vermenigvuldig je odds, waarom de marge meegroeit, hoe systeemweddenschappen "
                "werken en accu vs bet builder.")

OG_KOP = "Accumulator <span>uitleg</span>"
OG_EYEBROW = "Combi wedden"
OG_CHIPS = ["Odds vermenigvuldigen", "Marge stapelt mee"]
OG_MOTIEF = "reeks"
OG_DATA = ["1,80", "× 2,00", "× 1,65", "= 5,94"]


def eur(x):
    return f"€{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def q(x, d=2):
    return f"{x:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def pct(x, d=1):
    return f"{x * 100:.{d}f}%".replace(".", ",")


# voorbeeld 1: viervoudige combi (fictief)
BENEN = [("PSV wint", 1.80), ("Beide teams scoren in Feyenoord - AZ", 2.00), ("Ajax wint", 1.65), ("Meer dan 2,5 goals in Twente - Utrecht", 2.20)]
TOT4 = prod(o for _, o in BENEN)
assert q(prod([1.80, 2.00, 1.65])) == "5,94" and q(TOT4, 3) == "13,068" and eur(10 * TOT4) == "€130,68"
# één wedstrijd uitgesteld -> quotering 1,00
assert q(1.80 * 2.00 * 2.20) == "7,92" and eur(10 * 1.80 * 2.00 * 2.20) == "€79,20"

# voorbeeld 2: stapelende marge. Elke selectie: echte kans 50% (eerlijke odd 2,00), bookmaker biedt 1,90
EERLIJK, AANGEBODEN = 2.00, 1.90
assert pct(1 / AANGEBODEN * 2 - 1) == "5,3%"   # marge per markt van 1,90 / 1,90


def rij(n):
    fair, offer = EERLIJK ** n, AANGEBODEN ** n
    rtp = offer / fair
    return (f"<strong>{n}</strong>", pct(0.5 ** n, 2 if n >= 4 else 1), q(fair), q(offer), pct(rtp), pct(1 - rtp))


MARGE_RIJEN = [rij(n) for n in (1, 2, 3, 4, 6, 8)]
assert MARGE_RIJEN[3] == ("<strong>4</strong>", "6,25%", "16,00", "13,03", "81,5%", "18,5%")
assert MARGE_RIJEN[5][4] == "66,3%" and MARGE_RIJEN[0][5] == "5,0%"
VERWACHT4 = 0.5 ** 4 * 10 * AANGEBODEN ** 4
assert eur(VERWACHT4) == "€8,15" and eur(10 - VERWACHT4) == "€1,85"
# boost van 10% op de nettowinst maakt de viervoudige combi nog niet eerlijk
WINST4 = 10 * AANGEBODEN ** 4 - 10
BOOST = 10 + WINST4 * 1.10
assert eur(WINST4) == "€120,32" and eur(BOOST) == "€142,35" and eur(0.5 ** 4 * BOOST) == "€8,90"

# voorbeeld 3: systeem 2/3 (drie dubbels) met €5 per combinatie, odds A 2,00 / B 1,80 / C 2,50
A, B, C = 2.00, 1.80, 2.50
assert comb(3, 2) == 3 and eur(3 * 5) == "€15,00"
assert eur(5 * A * B) == "€18,00" and eur(5 * (A * B + A * C + B * C)) == "€65,50" and eur(15 * A * B * C) == "€135,00"
# systeemnamen en aantallen weddenschappen
SYS = {"Trixie": (3, comb(3, 2) + comb(3, 3)), "Patent": (3, 3 + comb(3, 2) + 1), "Yankee": (4, sum(comb(4, k) for k in (2, 3, 4))),
       "Lucky 15": (4, sum(comb(4, k) for k in (1, 2, 3, 4))), "Canadian (Super Yankee)": (5, sum(comb(5, k) for k in range(2, 6)))}
assert SYS == {"Trixie": (3, 4), "Patent": (3, 7), "Yankee": (4, 11), "Lucky 15": (4, 15), "Canadian (Super Yankee)": (5, 26)}

content = f"""<p><strong>Een accumulator, ook combi, combinatieweddenschap of parlay genoemd, is één weddenschap met twee of meer selecties uit verschillende wedstrijden. De quoteringen worden met elkaar vermenigvuldigd, dus met een kleine inzet kun je flink winnen. Daar staat tegenover dat álle selecties moeten uitkomen: gaat er één mis, dan ben je je hele inzet kwijt. Bovendien stapelt de marge van de bookmaker zich per selectie op, waardoor een combi op lange termijn duurder is dan losse weddenschappen.</strong></p>
<p>De combi is bij veel wedders de favoriete weddenschap van het weekend: vier of vijf wedstrijden in één briefje, voor een paar euro inzet. Hieronder lees je hoe je de uitbetaling berekent, waarom de kans op winst sneller daalt dan je denkt, wat de marge met je verwachte rendement doet en hoe systeemweddenschappen en de bet builder zich tot een gewone combi verhouden.</p>
<h3><strong>Hoe werkt een accumulator?</strong></h3>
<p>Je kiest meerdere uitkomsten, bijvoorbeeld de winnaar van drie wedstrijden, en zet ze op één wedbriefje. De bookmaker vermenigvuldigt de quoteringen tot één totaalquotering. Die totaalquotering keer je inzet is wat je terugkrijgt als alles goed gaat.</p>
<ul><li><strong>Dubbel:</strong> 2 selecties.</li><li><strong>Treble:</strong> 3 selecties.</li><li><strong>Viervoudig en hoger:</strong> 4 of meer selecties. In het Engels heet dat een fourfold, fivefold enzovoort.</li></ul>
<p>Selecties uit dezelfde wedstrijd mag je in een gewone combi meestal niet combineren, omdat ze met elkaar samenhangen. Daarvoor bestaat de bet builder, waarover verderop meer.</p>
<h3><strong>Rekenvoorbeeld: zo bereken je de uitbetaling</strong></h3>
<p>Je zet €10 op een viervoudige combi:</p>
{tabel(["Selectie", "Quotering", "Totaalquotering tot nu toe"], [
    (f"<strong>{n}</strong>", q(o), q(prod(x for _, x in BENEN[:i + 1]), 3 if i == 3 else 2)) for i, (n, o) in enumerate(BENEN)
])}
<p>De totaalquotering is 1,80 × 2,00 × 1,65 × 2,20 = <strong>{q(TOT4, 3)}</strong>. Komen alle vier de selecties uit, dan krijg je {eur(10 * TOT4)} terug: {eur(10 * TOT4 - 10)} winst. Gaat er ook maar één mis, dan krijg je niets.</p>
<p><strong>Wat als een wedstrijd niet doorgaat?</strong> Wordt een wedstrijd afgelast of uitgesteld, dan rekenen de meeste bookmakers die selectie af tegen een quotering van 1,00. Je combi gaat dan verder met de overige selecties. Valt in dit voorbeeld Ajax weg, dan wordt de totaalquotering 1,80 × 2,00 × 2,20 = {q(1.80 * 2.00 * 2.20)} en krijg je bij winst {eur(10 * 1.80 * 2.00 * 2.20)} terug. De precieze regels staan in de voorwaarden van je bookmaker.</p>
<p><em>De quoteringen in de voorbeelden in dit artikel zijn fictief en alleen bedoeld om de berekening te laten zien.</em></p>"""

content2 = f"""<h3><strong>Waarom is de kans op winst zo klein?</strong></h3>
<p>Kansen worden net als quoteringen met elkaar vermenigvuldigd. Heeft elke selectie 50% kans, dan is de kans dat twee selecties allebei uitkomen 50% × 50% = 25%. Bij vier selecties is dat nog maar 6,25%: gemiddeld één op de zestien keer. Elke extra selectie halveert in dit voorbeeld je kans. Dat voelt vaak anders, omdat elke selectie op zich "best kansrijk" lijkt.</p>
<h3><strong>Waarom stapelt de marge van de bookmaker zich op?</strong></h3>
<p>Een bookmaker biedt nooit de eerlijke quotering. Bij een markt met twee gelijkwaardige uitkomsten zou de eerlijke quotering 2,00 zijn, maar je krijgt bijvoorbeeld 1,90. Op één weddenschap krijg je dan gemiddeld 95% van je inzet terug. In een combi worden niet alleen de quoteringen vermenigvuldigd, maar ook die 95%. Zo groeit de marge met elke selectie.</p>
{tabel(["Selecties", "Kans dat alles uitkomt", "Eerlijke quotering", "Aangeboden quotering", "Gemiddeld terug", "Huisvoordeel"], MARGE_RIJEN)}
<p>Bij één selectie verlies je gemiddeld 5% van je inzet, bij een viervoudige combi al {MARGE_RIJEN[3][5]} en bij acht selecties meer dan een derde. Omgerekend: zet je €10 op een viervoudige combi van vier keer 1,90, dan krijg je op lange termijn gemiddeld {eur(VERWACHT4)} terug. Dat is {eur(10 - VERWACHT4)} verlies per briefje, tegen €0,50 als je vier losse weddenschappen van €2,50 had gespeeld.</p>
<p>Dat is ook waarom bookmakers combi's graag promoten. Een <strong>combiboost</strong> of winstboost klinkt genereus, maar compenseert de stapelende marge vaak niet. Krijg je in dit voorbeeld 10% extra op je nettowinst, dan wordt de uitbetaling {eur(BOOST)}. Gemiddeld krijg je dan {eur(0.5 ** 4 * BOOST)} terug per €10: nog steeds minder dan je inzet. Lees altijd de voorwaarden, want boosts gelden vaak alleen vanaf een minimum aantal selecties of een minimale quotering per selectie. Meer over acties lees je bij onze <a href="/bonussen/free-bets">free bets</a>.</p>
<h3><strong>Wat zijn systeemweddenschappen?</strong></h3>
<p>Met een systeemweddenschap verdeel je je selecties over meerdere kleinere combi's. Je hoeft dan niet alles goed te hebben om iets terug te krijgen, maar je betaalt voor elke combinatie een aparte inzet.</p>
<p><strong>Voorbeeld: systeem 2 uit 3</strong></p>
<p>Je kiest drie selecties met quoteringen 2,00, 1,80 en 2,50 en speelt alle dubbels: dat zijn er {comb(3, 2)}. Met €5 per dubbel is je totale inzet {eur(15)}.</p>
{tabel(["Uitkomst", "Systeem 2/3 (3 × €5)", "Treble (€15)"], [
    ("<strong>Alle drie goed</strong>", eur(5 * (A * B + A * C + B * C)), eur(15 * A * B * C)),
    ("<strong>Twee goed (2,00 en 1,80)</strong>", eur(5 * A * B), eur(0)),
    ("<strong>Eén of geen goed</strong>", eur(0), eur(0)),
])}
<p>Het systeem kost je bij een volledig goed briefje veel winst, maar levert bij één misser nog iets op. In dit voorbeeld krijg je met twee goede selecties {eur(5 * A * B)} terug: net iets meer dan je inzet. Systeemweddenschappen verkleinen de schommelingen, maar niet de marge: je speelt immers meer combi's.</p>
{tabel(["Systeem", "Selecties", "Aantal weddenschappen", "Wat zit erin"], [
    ("<strong>Trixie</strong>", "3", str(SYS["Trixie"][1]), "3 dubbels en 1 treble"),
    ("<strong>Patent</strong>", "3", str(SYS["Patent"][1]), "3 enkels, 3 dubbels en 1 treble"),
    ("<strong>Yankee</strong>", "4", str(SYS["Yankee"][1]), "6 dubbels, 4 trebles en 1 viervoudige"),
    ("<strong>Lucky 15</strong>", "4", str(SYS["Lucky 15"][1]), "4 enkels, 6 dubbels, 4 trebles en 1 viervoudige"),
    ("<strong>Canadian (Super Yankee)</strong>", "5", str(SYS["Canadian (Super Yankee)"][1]), "10 dubbels, 10 trebles, 5 viervoudige en 1 vijfvoudige"),
])}
<p>Let op: het aantal weddenschappen telt op. Een Lucky 15 van €1 per weddenschap kost je dus €15.</p>"""

content3 = f"""<h3><strong>Wat is het verschil tussen een bet builder en een accumulator?</strong></h3>
{tabel(["", "Accumulator (combi)", "Bet builder"], [
    ("<strong>Selecties uit</strong>", "Verschillende wedstrijden", "Eén wedstrijd"),
    ("<strong>Quotering</strong>", "Losse quoteringen vermenigvuldigd", "Door de bookmaker berekend, rekening houdend met samenhang"),
    ("<strong>Samenhang</strong>", "Selecties staan los van elkaar", "Selecties hangen vaak samen (bijv. winst en meer dan 2,5 goals)"),
    ("<strong>Marge</strong>", "Stapelt per selectie", "Vaak nog hoger, en lastig zelf te controleren"),
    ("<strong>Toegestaan in Nederland</strong>", "Ja", "Ja, maar zonder corners, kaarten en andere verboden markten"),
])}
<p>Bij een bet builder kun je de quotering niet zomaar narekenen door te vermenigvuldigen, omdat de selecties samenhangen. Speelt een favoriet thuis en verwacht je dat hij wint én dat er veel doelpunten vallen, dan zijn die twee uitkomsten deels afhankelijk van elkaar. De bookmaker verlaagt de quotering daarom. In Nederland mag een bet builder geen verboden onderdelen bevatten, zoals corners of kaarten. Lees <a href="/nieuws/dit-is-waarom-wedden-op-corners-niet-meer-legaal-is-in-nederland">waarom wedden op corners niet legaal is</a>.</p>
<h3><strong>Tips voor slimmer combi wedden</strong></h3>
<ul><li><strong>Houd het klein.</strong> Een dubbel of treble geeft al een mooie quotering, met een veel grotere kans en minder opgestapelde marge dan een combi van acht.</li><li><strong>Vergelijk de quotering van elke selectie.</strong> Een iets hogere quotering per selectie telt in een combi extra door. Vier keer 1,95 in plaats van 1,90 geeft {q(1.95 ** 4)} in plaats van {q(1.90 ** 4)}. Gebruik onze <a href="/odds-vergelijken-bij-alle-bookmakers-beste-odds-vandaag">odds vergelijker</a>.</li><li><strong>Voeg geen "zekerheidjes" toe.</strong> Een selectie van 1,15 verhoogt je quotering nauwelijks, maar brengt wel een extra risico en extra marge mee.</li><li><strong>Kies alleen selecties waar je echt iets van vindt.</strong> Een combi wordt niet beter door meer wedstrijden. Wil je op lange termijn winnen, dan moet elke selectie waarde hebben; lees wat <a href="/nieuws/wat-is-de-wedstrategie-value-betting">value betting</a> is.</li><li><strong>Gebruik handicaps met beleid.</strong> Een <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap</a> verhoogt de quotering per selectie, maar ook het risico per selectie.</li><li><strong>Zie een combi als vermaak.</strong> Zet er een klein, vast bedrag op dat je kunt missen.</li></ul>
<p>Op zoek naar inspiratie? Bekijk onze <a href="/wedtips">wedtips</a>, zoals de <a href="/wedtips/btts-tips-voorspellingen">BTTS-tips</a>.</p>
<h3><strong>Mag je in Nederland een accumulator spelen?</strong></h3>
<p>Ja. Combinatieweddenschappen zijn bij alle legale bookmakers in Nederland toegestaan. Voorwaarde is wel dat alle selecties binnen de Nederlandse regels vallen: weddenschappen op bijvoorbeeld corners, kaarten, jeugdwedstrijden of lagere amateurklassen worden ook in een combi niet aangeboden. Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit; bij een site zonder vergunning speel je illegaal en heb je geen bescherming. Twijfel je? Lees <a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe weet ik of een bookmaker legaal is</a>.</p>
<p>Legale bookmakers die wij aanraden:</p>
{aanraders()}
<h3><strong>Veelgestelde vragen over accumulators</strong></h3>
<p><strong>Wat is een accumulator?</strong><br>Eén weddenschap met twee of meer selecties uit verschillende wedstrijden. De quoteringen worden vermenigvuldigd en alle selecties moeten uitkomen om te winnen.</p>
<p><strong>Wat is het verschil tussen een combi, accu en parlay?</strong><br>Er is geen verschil. Combi en combinatieweddenschap zijn de Nederlandse termen, accu of acca komt uit het Engels en parlay uit de Verenigde Staten.</p>
<p><strong>Hoe bereken je de quotering van een combi?</strong><br>Vermenigvuldig de quoteringen van alle selecties. Drie selecties van 1,80, 2,00 en 1,65 geven samen {q(1.80 * 2.00 * 1.65)}. Met €10 inzet krijg je bij winst {eur(10 * 1.80 * 2.00 * 1.65)} terug.</p>
<p><strong>Wat gebeurt er als één wedstrijd wordt uitgesteld?</strong><br>Meestal wordt die selectie afgerekend tegen 1,00 en loopt de combi door met de overige selecties. Check de voorwaarden van je bookmaker.</p>
<p><strong>Is een combi slimmer dan losse weddenschappen?</strong><br>Niet als het om je verwachte rendement gaat. De marge stapelt per selectie op, waardoor je met een combi gemiddeld meer verliest dan met dezelfde selecties los. Een combi geeft wel een kans op een grote uitbetaling met een kleine inzet.</p>
<p><strong>Wat is een systeemweddenschap?</strong><br>Een verzameling kleinere combi's uit dezelfde selecties, zoals alle dubbels uit drie wedstrijden. Je krijgt ook iets terug als niet alles goed is, maar je betaalt per combinatie een inzet.</p>
<p><strong>Mag ik selecties uit één wedstrijd combineren?</strong><br>In een gewone combi meestal niet. Daarvoor gebruik je een bet builder, waarvan de bookmaker de quotering zelf berekent.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    from datetime import datetime, timezone
    alles = content + content2 + content3
    tekst = re.sub(r"<[^>]+>", " ", alles)
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", len(tekst.split()), "woorden")
    assert not re.search(r"<(ul|ol|/li)>\s+<", alles) and "/kennisbank/" not in alles
    # ---- --live: alleen handmatig draaien na akkoord ----
    if "--live" in sys.argv:
        fd = {"name": TITEL, "content": content, "content-2": content2, "content-3": content3,
              "samenvatting": SAMENVATTING, "rubriek": RUBRIEK, "publicatiedatum": datetime.now(timezone.utc).isoformat()}
        print(WF.update_live(ITEM_ID, fd).get("lastPublished"))
