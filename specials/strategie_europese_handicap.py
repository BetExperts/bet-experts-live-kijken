# -*- coding: utf-8 -*-
"""Herschrijving Nieuws-item 65048b0a11426cdbe93aef1a (Kennisbank-versie offline + 301): Wat is een Europese handicap?
Uitleg 3-weg handicap met tabel per handicap (−1, −2, +1, +2), euro-voorbeelden, marge en vergelijking met Asian.
Feiten nagelopen op 21-10-2026:
- TOTO 'Nadere regels per sport' (online): 2-way en 3-way handicap als wedoptie; bij voetbal geldt de reguliere speeltijd.
  Menunaam 'handicap resultaat' niet in een actueel TOTO-document teruggevonden -> voorzichtig geformuleerd.
- Handicapmarkten vallen niet onder Bijlage 2, onderdeel 2.3 Regeling kansspelen op afstand (verboden gebeurtenissen).
- Marges en equivalenties worden hieronder berekend en ge-assert; Asian-afrekening via og_kaarten/asian_rekenen.py.
  python3 specials/strategie_europese_handicap.py [--live]"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, os.path.join(HIER, "..", "og_kaarten"))
sys.path.insert(0, HIER)
import lk_webflow as WF
from legaal_data import tabel, aanraders
from asian_rekenen import handicap

ITEM_ID = "65048b0a11426cdbe93aef1a"   # Nieuws
SLUG = "wat-een-europese-handicap-weddenschap"
RUBRIEK = "6502b66cd9992658b4037cf5"
TITEL = "Europese handicap: uitleg met tabellen en voorbeelden"
SAMENVATTING = ("Europese handicap (3-weg) uitgelegd: per handicap −1, −2, +1 en +2 zie je welke uitkomst wint. "
                "Met rekenvoorbeelden en het verschil met Asian.")

OG_KOP = "Europese <span>handicap</span>"
OG_EYEBROW = "3-weg handicap"
OG_CHIPS = ["Tabel per handicap", "Verschil met Asian"]
OG_MOTIEF = "tabel"
OG_DATA = ["−1 · wint met 2+ · 1", "−1 · wint met 1 · X", "−1 · gelijk of verlies · 2"]


def eur(x):
    return f"€{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def pct(x):
    return f"{x * 100:.1f}%".replace(".", ",")


def eh(lijn, saldo):
    """lijn = handicap van de ploeg waar de 1 bij hoort; saldo = doelsaldo van die ploeg. Geeft de winnende uitkomst."""
    v = saldo + lijn
    return "1" if v > 0 else ("X" if v == 0 else "2")


def score(thuis, uit, lijn):
    """Virtuele stand na handicap op de thuisploeg (lijn negatief = thuis achterstand)."""
    return (thuis, uit - lijn) if lijn < 0 else (thuis + lijn, uit)


def q(o):
    return f"{o:.2f}".replace(".", ",")


def marge(*odds):
    return sum(1 / o for o in odds) - 1


SALDI = [3, 2, 1, 0, -1, -2, -3]
KOLOMMEN = ["Wint met 3+", "Wint met 2", "Wint met 1", "Gelijk", "Verliest met 1", "Verliest met 2", "Verliest met 3+"]
LABEL = {"1": "<strong>1</strong>", "X": "<strong>X</strong>", "2": "<strong>2</strong>"}

# controles: tabellen en equivalenties
assert [eh(-1, s) for s in SALDI] == ["1", "1", "X", "2", "2", "2", "2"]
assert [eh(-2, s) for s in SALDI] == ["1", "X", "2", "2", "2", "2", "2"]
assert [eh(1, s) for s in SALDI] == ["1", "1", "1", "1", "X", "2", "2"]
assert [eh(2, s) for s in SALDI] == ["1", "1", "1", "1", "1", "X", "2"]
for s in range(-5, 6):
    assert (eh(-1, s) == "1") == (handicap(-1.5, s) == 1)          # EH −1 uitkomst 1 = Asian −1,5
    assert (eh(-1, s) == "2") == (handicap(0.5, -s) == 1)          # EH −1 uitkomst 2 = tegenstander Asian +0,5
    assert (eh(-1, s) in "X2") == (handicap(1.5, -s) == 1)         # EH −1 X2 = tegenstander Asian +1,5
    assert (eh(1, s) == "1") == (handicap(0.5, s) == 1)            # EH +1 uitkomst 1 = Asian +0,5
    assert (eh(1, s) == "2") == (handicap(-1.5, -s) == 1)          # EH +1 uitkomst 2 = tegenstander Asian −1,5
    assert (eh(-2, s) == "1") == (handicap(-2.5, s) == 1)          # EH −2 uitkomst 1 = Asian −2,5
assert score(3, 0, -1) == (3, 1) and score(2, 1, -1) == (2, 2) and score(1, 1, -1) == (1, 2) and score(0, 1, 1) == (1, 1)
# euro-voorbeeld PSV - NEC (0:1): 1 = 2,05, X = 3,80, 2 = 3,20
O1, OX, O2 = 2.05, 3.80, 3.20
assert eur(10 * O1) == "€20,50" and eur(10 * OX) == "€38,00" and eur(10 * O2) == "€32,00"
assert pct(marge(O1, OX, O2)) == "6,3%" and pct(marge(2.08, 1.82)) == "3,0%"
# dekken met twee uitkomsten: €10 op 1 en €10 op X
assert eur(10 * O1 - 20) == "€0,50" and eur(10 * OX - 20) == "€18,00"


def hc_tabel(lijn, voorbeelden):
    rijen = []
    for t, u in voorbeelden:
        vt, vu = score(t, u, lijn)
        rijen.append((f"PSV - NEC {t}-{u}", f"{vt}-{vu}", LABEL[eh(lijn, t - u)]))
    return tabel(["Echte uitslag", "Na handicap", "Winnende uitkomst"], rijen)


overzicht = tabel(["Handicap thuisploeg"] + KOLOMMEN,
                  [(f"<strong>{n}</strong>",) + tuple(LABEL[eh(l, s)] for s in SALDI)
                   for n, l in [("−2 (0:2)", -2), ("−1 (0:1)", -1), ("+1 (1:0)", 1), ("+2 (2:0)", 2)]])

content = f"""<p><strong>Een Europese handicap is een weddenschap waarbij een team vooraf een virtuele voorsprong of achterstand krijgt van een heel aantal doelpunten, zoals −1 of +2. Na de wedstrijd tel je die handicap op bij de uitslag. Je kiest net als bij 1X2 uit drie uitkomsten: thuiswinst (1), gelijkspel na handicap (X) of uitwinst (2). Speel je PSV −1 en wint PSV met precies één doelpunt verschil, dan wint de X en verlies je je inzet op PSV. Omdat er drie uitkomsten zijn, heet het ook 3-weg handicap.</strong></p>
<p>De Europese handicap is de oudste en simpelste vorm van handicap wedden. Je ziet hem vooral bij voetbal, maar ook bij handbal en ijshockey. Ga je voor het eerst met een Europese handicap gokken, dan is de X het onderdeel dat de meeste verwarring geeft. Hieronder vind je per handicap een tabel met welke uitkomst wint bij welke uitslag, rekenvoorbeelden in euro's en een eerlijke vergelijking met de <a href="/nieuws/wat-is-een-asian-handicap-weddenschap">Asian handicap</a>. Wil je eerst het grotere plaatje? Lees dan onze <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">complete gids over handicap wedden</a>.</p>
<h3><strong>Hoe werkt een Europese handicap?</strong></h3>
<p>De bookmaker geeft een van de twee ploegen een virtuele achterstand of voorsprong in hele doelpunten. Meestal krijgt de favoriet een achterstand. Bij veel bookmakers zie je dat als notatie tussen haakjes: <strong>(0:1)</strong> betekent dat de uitploeg met 1-0 voor begint, dus de thuisploeg speelt −1. <strong>(2:0)</strong> betekent dat de thuisploeg met 2-0 voor begint.</p>
<p>Daarna werkt het als een gewone 1X2-weddenschap, maar op de aangepaste stand:</p>
<ul><li><strong>1:</strong> de thuisploeg wint na de handicap.</li><li><strong>X:</strong> het staat gelijk na de handicap.</li><li><strong>2:</strong> de uitploeg wint na de handicap.</li></ul>
<p>Het belangrijkste om te onthouden: de X betekent hier <strong>niet</strong> dat de wedstrijd echt gelijk eindigt. Het is het gelijkspel ná de handicap. Bij PSV −1 valt de X juist als PSV met precies één doelpunt wint.</p>
<h3><strong>Europese handicap tabel: alle uitkomsten in één overzicht</strong></h3>
<p>Zoek links de handicap van de thuisploeg en kijk in de kolom naar het echte doelsaldo van de thuisploeg. In de cel staat welke uitkomst wint.</p>
{overzicht}
<p>Valt je oog op het patroon? Bij elke handicap is er precies één doelsaldo waarbij de X wint: het saldo dat de handicap precies ongedaan maakt.</p>"""

content2 = f"""<h3><strong>Europese handicap −1 (0:1)</strong></h3>
<p>De meest gespeelde Europese handicap. De favoriet moet met 2 of meer verschil winnen voor uitkomst 1.</p>
{hc_tabel(-1, [(3, 0), (2, 1), (1, 1), (0, 1)])}
<h3><strong>Europese handicap −2 (0:2)</strong></h3>
<p>Voor wedstrijden met een uitgesproken favoriet. Uitkomst 1 vraagt een zege met 3 of meer verschil, de X valt bij precies 2 verschil.</p>
{hc_tabel(-2, [(4, 0), (3, 1), (2, 1), (1, 1)])}
<h3><strong>Europese handicap +1 (1:0)</strong></h3>
<p>Nu krijgt de thuisploeg een voorsprong, handig als de thuisploeg de underdog is. Uitkomst 1 wint als de thuisploeg niet verliest.</p>
{hc_tabel(1, [(1, 0), (1, 1), (0, 1), (0, 2)])}
<h3><strong>Europese handicap +2 (2:0)</strong></h3>
<p>De thuisploeg begint met 2-0 voor. Uitkomst 1 wint zelfs bij een nederlaag met 1 verschil.</p>
{hc_tabel(2, [(1, 1), (0, 1), (0, 2), (0, 3)])}
<p>In deze tabellen is PSV steeds de thuisploeg. Krijgt de uitploeg de handicap, dan draai je het simpelweg om: bij (1:0) voor de thuisploeg speelt de uitploeg −1.</p>
<h3><strong>Rekenvoorbeeld in euro's: PSV - NEC met handicap (0:1)</strong></h3>
<p>PSV is thuis favoriet tegen NEC. De bookmaker biedt de Europese handicap (0:1) aan met deze quoteringen: <strong>1 = {q(O1)}</strong>, <strong>X = {q(OX)}</strong>, <strong>2 = {q(O2)}</strong>. Je zet €10 in.</p>
{tabel(["Jouw keuze", "Je wint als...", "Uitslag bijvoorbeeld", "Je krijgt terug"], [
    ("<strong>1</strong> (2,05)", "PSV met 2 of meer verschil wint", "3-0", eur(10 * O1)),
    ("<strong>X</strong> (3,80)", "PSV met precies 1 verschil wint", "2-1", eur(10 * OX)),
    ("<strong>2</strong> (3,20)", "het gelijk wordt of NEC wint", "1-1", eur(10 * O2)),
])}
<p><em>De quoteringen in dit voorbeeld zijn fictief en alleen bedoeld om de berekening te laten zien.</em></p>
<p>Je kunt ook twee uitkomsten afdekken. Zet je €10 op 1 en €10 op X, dan wint één van beide zodra PSV wint. Bij een ruime zege houd je {eur(10 * O1 - 20)} winst over, bij een zege met 1 verschil {eur(10 * OX - 20)}. Bij een gelijkspel of nederlaag ben je €20 kwijt. Dekken klinkt veilig, maar je betaalt op beide weddenschappen de marge van de bookmaker.</p>
<h3><strong>Wat is het verschil tussen Europese en Asian handicap?</strong></h3>
{tabel(["", "Europese handicap", "Asian handicap"], [
    ("<strong>Uitkomsten</strong>", "Drie: 1, X of 2 na handicap", "Twee: jouw team of de tegenstander"),
    ("<strong>Lijnen</strong>", "Alleen hele getallen (−1, +2)", "Hele, halve en kwartlijnen (−0,5, −1, −0,75)"),
    ("<strong>Gelijk na handicap</strong>", "De X wint, jouw inzet op 1 of 2 is verloren", "Inzet terug (hele lijn) of halve winst/verlies (kwartlijn)"),
    ("<strong>Marge in ons voorbeeld</strong>", pct(marge(O1, OX, O2)), pct(marge(2.08, 1.82))),
    ("<strong>Geschikt voor</strong>", "Wie een duidelijke verwachting heeft over het verschil", "Wie risico wil beperken bij een nipte uitslag"),
])}
<p>De marge bereken je door de omgekeerde quoteringen op te tellen. Voor de Europese handicap is dat 1/2,05 + 1/3,80 + 1/3,20 = {pct(1 + marge(O1, OX, O2))}, dus {pct(marge(O1, OX, O2))} marge. Een Asian lijn met 2,08 en 1,82 komt uit op {pct(marge(2.08, 1.82))}. Hoe lager de marge, hoe meer je op de lange termijn terugkrijgt.</p>"""

content3 = f"""<h3><strong>Welke Europese handicap is gelijk aan welke Asian handicap?</strong></h3>
<p>Veel uitkomsten van de Europese handicap hebben een exacte tegenhanger bij de Asian handicap. Vergelijk dan de quoteringen: in ons voorbeeld betaalt Asian −1,5 2,08 terwijl uitkomst 1 bij (0:1) 2,05 betaalt, voor precies dezelfde weddenschap.</p>
{tabel(["Europese handicap", "Wint als", "Zelfde als Asian"], [
    ("<strong>Thuis −1, uitkomst 1</strong>", "Thuis wint met 2+", "Thuis −1,5"),
    ("<strong>Thuis −1, uitkomst X</strong>", "Thuis wint met precies 1", "Geen tegenhanger"),
    ("<strong>Thuis −1, uitkomst 2</strong>", "Gelijk of uit wint", "Uit +0,5"),
    ("<strong>Thuis −2, uitkomst 1</strong>", "Thuis wint met 3+", "Thuis −2,5"),
    ("<strong>Thuis +1, uitkomst 1</strong>", "Thuis wint of gelijk", "Thuis +0,5"),
    ("<strong>Thuis +1, uitkomst 2</strong>", "Uit wint met 2+", "Uit −1,5"),
])}
<p>De X heeft geen Asian tegenhanger. Dat is meteen de reden dat sommige wedders juist voor de Europese handicap kiezen: verwacht je een krappe zege van de favoriet, zoals 1-0 of 2-1, dan krijg je op die X vaak een hoge quotering.</p>
<h3><strong>Wanneer kies je voor een Europese handicap?</strong></h3>
<ul><li><strong>Je verwacht een ruime zege van een favoriet</strong> en de 1X2-quotering is te laag. Vergelijk dan wel met Asian −1,5, die vaak iets beter betaalt.</li><li><strong>Je verwacht een zege met precies 1 verschil.</strong> De X bij (0:1) is dan de enige markt die precies dat scenario beloont.</li><li><strong>Je wilt de underdog extra ruimte geven</strong> met een (1:0) of (2:0) op de underdog, maar let op: bij de X verlies je, anders dan bij Asian +1.</li><li><strong>Je zoekt een eenvoudige markt.</strong> Geen halve winsten of splitsingen, gewoon 1, X of 2.</li></ul>
<h3><strong>Tips en valkuilen</strong></h3>
<ul><li><strong>Lees de notatie goed.</strong> (0:1) en (1:0) lijken op elkaar maar zijn elkaars tegenovergestelde.</li><li><strong>Alleen de reguliere speeltijd telt.</strong> Blessuretijd telt mee, verlenging en strafschoppen niet.</li><li><strong>Vergelijk met de Asian lijn.</strong> Voor dezelfde uitkomst kan de quotering verschillen. Gebruik onze <a href="/odds-vergelijken-bij-alle-bookmakers-beste-odds-vandaag">odds vergelijker</a>.</li><li><strong>Een hogere quotering is geen voordeel op zich.</strong> Je krijgt meer omdat je kans kleiner is. Alleen als jouw inschatting beter is dan die van de bookmaker heb je waarde; lees meer over <a href="/nieuws/wat-is-de-wedstrategie-value-betting">value betting</a>.</li><li><strong>Speel bewust.</strong> Bepaal vooraf je budget en zet nooit meer in dan je kunt missen.</li></ul>
<h3><strong>Europese handicap bij TOTO en andere legale bookmakers</strong></h3>
<p>Legale bookmakers in Nederland bieden de Europese handicap vrijwel allemaal aan, maar de naam verschilt. Je vindt hem onder namen als "Handicap", "3-weg handicap" of "handicap resultaat", vaak met de notatie (0:1). De 2-weg variant staat er meestal los van als "Asian handicap" of "Aziatische handicap". Handicapmarkten zijn in Nederland toegestaan, omdat ze over de uitslag gaan. Dat geldt niet voor markten op corners of kaarten; lees <a href="/nieuws/dit-is-waarom-wedden-op-corners-niet-meer-legaal-is-in-nederland">waarom wedden op corners niet legaal is</a>. Wed alleen bij een bookmaker met een vergunning van de Kansspelautoriteit. Bij een site zonder vergunning speel je illegaal en zonder bescherming.</p>
<p>Legale bookmakers die wij aanraden:</p>
{aanraders()}
<h3><strong>Veelgestelde vragen over de Europese handicap</strong></h3>
<p><strong>Wat is een Europese handicap?</strong><br>Een weddenschap met drie uitkomsten waarbij een team een virtuele voor- of achterstand in hele doelpunten krijgt. Je wedt op 1, X of 2 nadat de handicap bij de uitslag is opgeteld.</p>
<p><strong>Wat betekent handicap (0:1)?</strong><br>De uitploeg begint virtueel met 1-0 voor. De thuisploeg moet dus met 2 of meer verschil winnen voor uitkomst 1. Wint de thuisploeg met precies 1, dan wint de X.</p>
<p><strong>Wat is handicap resultaat?</strong><br>Daarmee wordt meestal de Europese of 3-weg handicap bedoeld: het resultaat 1, X of 2 na het toepassen van de handicap.</p>
<p><strong>Krijg je je inzet terug bij een gelijkspel na de handicap?</strong><br>Nee, bij de Europese handicap niet. Dan wint de X en verliest wie op 1 of 2 heeft ingezet. Inzet terug krijg je alleen bij een Asian handicap met een hele lijn.</p>
<p><strong>Is een Europese handicap −1 hetzelfde als Asian −1?</strong><br>Nee. Wint je team met precies 1 verschil, dan verlies je bij Europees −1 en krijg je bij Asian −1 je inzet terug. Europees −1 (uitkomst 1) is wel hetzelfde als Asian −1,5.</p>
<p><strong>Telt de verlenging mee?</strong><br>Bij voetbal niet. Alleen de reguliere speeltijd inclusief blessuretijd telt, tenzij de bookmaker bij de markt iets anders vermeldt.</p>
<p><strong>Is de Europese handicap beter dan de Asian handicap?</strong><br>Niet beter of slechter, wel anders. De Europese handicap is eenvoudiger en heeft de X als extra keuze. De Asian handicap heeft vaak een lagere marge en beschermt je bij een nipte uitslag.</p>
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
