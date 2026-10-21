# -*- coding: utf-8 -*-
"""Herschrijving Nieuws-item 650489ed6bdea56292121b8e (Kennisbank-versie offline + 301): Wat is handicap wedden? De complete gids
(hub voor Europese handicap, Asian handicap, tennis- en basketbalhandicaps).
Feiten nagelopen op 21-10-2026:
- Bijlage 2, onderdeel 2.3 Regeling kansspelen op afstand (BWBR0044767): bij tennis verboden 'winst of verlies van een specifieke
  game' en 'van een specifieke set' (game-/sethandicap over de hele wedstrijd valt daar niet onder); basketbal staat niet in 2.3.
- TOTO 'Nadere regels per sport' (online): wedoptie Handicap op (doel)punten, sets, games; 2-way en 3-way handicap; bij hele
  handicap en gelijke stand na handicap quotering 1,00 (= inzet terug). Exacte menunaam 'handicap resultaat' niet in een
  actueel TOTO-document teruggevonden -> in de tekst voorzichtig geformuleerd ('onder namen als').
- Asian-afrekenregels via og_kaarten/asian_rekenen.py (zelfde rekenregels als asian_handicap.py).
  python3 specials/strategie_handicap_wedden.py [--live]"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, os.path.join(HIER, "..", "og_kaarten"))
sys.path.insert(0, HIER)
import lk_webflow as WF
from legaal_data import tabel, aanraders
from asian_rekenen import handicap, uitbetaling

ITEM_ID = "650489ed6bdea56292121b8e"   # Nieuws
SLUG = "wat-is-handicap-wedden-de-complete-gids"
RUBRIEK = "6502b64b78efefb4144fd2c1"
TITEL = "Handicap wedden: wat is het en welke soorten zijn er?"
SAMENVATTING = ("Handicap wedden uitgelegd: Europese en Asian handicap, +1,5 en 0,5, notatie 2:0, tennis en basketbal. "
                "Met tabellen en rekenvoorbeelden.")

OG_KOP = "Handicap <span>wedden</span>"
OG_EYEBROW = "Complete gids"
OG_CHIPS = ["Europees, Asian, tennis", "Met rekenvoorbeelden"]
OG_MOTIEF = "tabel"
OG_DATA = ["Ajax −1,5 · 3-1 · winst", "Ajax −1,5 · 2-1 · verlies", "Heracles +1,5 · 2-1 · winst"]


def eur(x):
    return f"€{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def ah(lijn, saldo, odd, inzet=10):
    """Asian handicap (2-weg): totale terugbetaling."""
    return eur(uitbetaling(handicap(lijn, saldo), inzet, odd))


def eh(lijn, saldo):
    """Europese (3-weg) handicap: welke uitkomst wint? lijn = handicap thuisploeg, saldo = doelsaldo thuisploeg."""
    v = saldo + lijn
    return "1" if v > 0 else ("X" if v == 0 else "2")


def eh_bet(lijn, saldo, keuze, odd, inzet=10):
    return eur(inzet * odd if eh(lijn, saldo) == keuze else 0)


# controles: OG_DATA en tabellen moeten kloppen met de rekenregels
assert handicap(-1.5, 2) == 1 and handicap(-1.5, 1) == -1 and handicap(1.5, -1) == 1
assert eur(10 * 1.35) == "€13,50" and ah(-1, 3, 1.80) == "€18,00" and ah(-1, 1, 1.80) == "€10,00" and ah(-1, 0, 1.80) == "€0,00"
assert ah(-1.5, 3, 2.05) == "€20,50" and ah(-1.5, 1, 2.05) == "€0,00"
assert eh_bet(-1, 3, "1", 2.10) == "€21,00" and eh(-1, 1) == "X" and eh(-1, 0) == "2" and eh_bet(-1, 1, "1", 2.10) == "€0,00"
assert ah(1.5, -1, 1.80) == "€18,00" and ah(1.5, -3, 1.80) == "€0,00" and ah(1.5, 0, 1.80) == "€18,00"
# notatie 0:2 -> thuisploeg -2; 3-0 wordt virtueel 3-2
assert eh(-2, 3) == "1" and eh(-2, 2) == "X" and eh(2, -1) == "1"
# tennis: Speler A -4,5 games (odd 1,85): 6-4 6-3 = 12-7 (+5) wint, 7-6 6-4 = 13-10 (+3) verliest
assert (6 + 6) - (4 + 3) == 5 and handicap(-4.5, 5) == 1 and ah(-4.5, 5, 1.85) == "€18,50"
assert (7 + 6) - (6 + 4) == 3 and handicap(-4.5, 3) == -1
# basketbal: -6,5 punten (odd 1,90): 104-99 (+5) verlies, 110-101 (+9) winst
assert handicap(-6.5, 104 - 99) == -1 and handicap(-6.5, 110 - 101) == 1 and ah(-6.5, 9, 1.90) == "€19,00"

content = f"""<p><strong>Handicap wedden is een weddenschap waarbij de bookmaker een team of speler een virtuele voorsprong of achterstand geeft, bijvoorbeeld −1 of +1,5. Na afloop tel je die handicap op bij de echte uitslag en kijk je wie de virtuele wedstrijd wint. Zo krijg je een hogere quotering op een favoriet, of extra speelruimte op een underdog. De twee bekendste soorten zijn de Europese handicap (drie uitkomsten, alleen hele getallen) en de Asian handicap (twee uitkomsten, ook halve en kwartlijnen). Bij tennis en basketbal werkt hetzelfde principe met games, sets of punten.</strong></p>
<p>Bij een gewone 1X2-weddenschap krijg je op een grote favoriet vaak een quotering van 1,30 of lager. Handicap wedden maakt zo'n wedstrijd interessanter, omdat je niet meer op de uitslag wedt maar op het verschil. In deze gids lees je hoe het werkt, welke soorten er zijn, wat notaties als +1,5, 0,5 en 2:0 betekenen en welke handicap bij welke situatie past. Voor de details per soort verwijzen we naar onze uitgebreide uitleg over de <a href="/nieuws/wat-een-europese-handicap-weddenschap">Europese handicap</a> en de <a href="/nieuws/wat-is-een-asian-handicap-weddenschap">Asian handicap</a>.</p>
<h3><strong>Hoe werkt handicap wedden?</strong></h3>
<p>Het principe is in elke sport hetzelfde. De favoriet krijgt een min-getal (een achterstand), de underdog een plus-getal (een voorsprong). Na de wedstrijd doe je drie dingen:</p>
<ol><li><strong>Neem de echte uitslag,</strong> bijvoorbeeld Ajax - Heracles 3-1.</li><li><strong>Tel de handicap op bij de score van jouw team.</strong> Met Ajax −1,5 wordt het virtueel 1,5-1.</li><li><strong>Kijk wie er virtueel wint.</strong> Ajax staat virtueel voor, dus je weddenschap is gewonnen.</li></ol>
<p>Nog makkelijker is het om alleen naar het <strong>doelsaldo</strong> te kijken. Wint jouw team met 2 verschil en speel je −1,5, dan houd je +0,5 over: gewonnen. Wint het met 1 verschil, dan houd je −0,5 over: verloren.</p>
<h3><strong>Welke soorten handicap wedden zijn er?</strong></h3>
{tabel(["Soort", "Waar je het ziet", "Kenmerk"], [
    ("<strong>Europese handicap (3-weg)</strong>", "Voetbal, handbal, ijshockey", "Hele getallen (−1, +2). Drie uitkomsten: 1, X of 2 na de handicap."),
    ("<strong>Asian handicap (2-weg)</strong>", "Voetbal, ijshockey", "Hele, halve en kwartlijnen (−0,5, −1, −0,75). Geen gelijkspel, wel inzet terug of halve winst."),
    ("<strong>Game-handicap</strong>", "Tennis", "Voorsprong of achterstand in het totaal aantal games, zoals −4,5 games."),
    ("<strong>Set-handicap</strong>", "Tennis, volleybal, darts (legs/sets)", "Voorsprong of achterstand in sets, zoals −1,5 sets."),
    ("<strong>Puntenhandicap (spread)</strong>", "Basketbal, American football", "Voorsprong of achterstand in punten, zoals −6,5 punten."),
    ("<strong>Puck line / run line</strong>", "IJshockey, honkbal", "Vaste handicap van meestal 1,5 doelpunt of run."),
])}
<p><strong>Europese handicap: drie uitkomsten</strong></p>
<p>De Europese handicap gebruikt alleen hele getallen. Daardoor kan het na de handicap gelijk staan, en dat is een aparte uitkomst waarop je kunt inzetten. Speel je Ajax −1 en wint Ajax met precies 1 verschil, dan wint de uitkomst "handicap gelijk" en verlies je je inzet op Ajax. Alle tabellen per handicap vind je in onze uitleg over de <a href="/nieuws/wat-een-europese-handicap-weddenschap">Europese handicap</a>.</p>
<p><strong>Asian handicap: twee uitkomsten</strong></p>
<p>De Asian handicap heeft maar twee kanten. Halve lijnen (−0,5, −1,5) leveren winst of verlies op. Bij hele lijnen (−1) krijg je bij een virtueel gelijkspel je inzet terug. Bij kwartlijnen (−0,75) wordt je inzet verdeeld over twee lijnen, waardoor je ook half kunt winnen of verliezen. Lees alles daarover in onze uitleg over de <a href="/nieuws/wat-is-een-asian-handicap-weddenschap">Asian handicap</a>.</p>"""

content2 = f"""<h3><strong>Wat betekent +1,5, −1,5 en 0,5 handicap?</strong></h3>
<p>Halve lijnen zijn het makkelijkst, want een halve goal kan niet vallen. Er is dus altijd een winnaar en nooit inzet terug. Zo lees je de meest gezochte lijnen:</p>
{tabel(["Handicap", "Je wint als jouw team...", "Vergelijkbaar met"], [
    ("<strong>−0,5</strong>", "wint", "Gewone winst (1 of 2) in 1X2"),
    ("<strong>+0,5</strong>", "wint of gelijkspeelt", "Dubbele kans (1X of X2)"),
    ("<strong>−1,5</strong>", "met 2 of meer doelpunten verschil wint", "Europese handicap −1, uitkomst 1"),
    ("<strong>+1,5</strong>", "wint, gelijkspeelt of met maximaal 1 doelpunt verschil verliest", "Europese handicap +1, uitkomst 1X"),
    ("<strong>−2,5</strong>", "met 3 of meer verschil wint", "Europese handicap −2, uitkomst 1"),
    ("<strong>+2,5</strong>", "niet met 3 of meer verschil verliest", "Europese handicap +2, uitkomst 1X"),
])}
<p>Een handicap van 0,5 zonder teken bestaat in de praktijk niet: er staat altijd een min bij de ene ploeg en een plus bij de andere. Kijk dus goed bij welk team het min-teken staat voordat je inzet.</p>
<h3><strong>Wat betekent handicap 2:0 of 0:1?</strong></h3>
<p>Bij de Europese handicap zie je vaak een notatie als <strong>(0:1)</strong> of <strong>(2:0)</strong>. Dat is de virtuele beginstand: het eerste getal hoort bij de thuisploeg, het tweede bij de uitploeg. Die stand tel je op bij de echte uitslag.</p>
{tabel(["Notatie", "Betekenis", "Voorbeeld: echte uitslag", "Uitslag na handicap"], [
    ("<strong>(0:1)</strong>", "Uitploeg begint met 1-0 voor (thuis −1)", "Ajax - Heracles 2-1", f"2-2: uitkomst {eh(-1, 1)}"),
    ("<strong>(0:2)</strong>", "Uitploeg begint met 2-0 voor (thuis −2)", "Ajax - Heracles 3-0", f"3-2: uitkomst {eh(-2, 3)}"),
    ("<strong>(1:0)</strong>", "Thuisploeg begint met 1-0 voor (thuis +1)", "Heracles - Ajax 0-1", f"1-1: uitkomst {eh(1, -1)}"),
    ("<strong>(2:0)</strong>", "Thuisploeg begint met 2-0 voor (thuis +2)", "Heracles - Ajax 0-1", f"2-1: uitkomst {eh(2, -1)}"),
])}
<p>Bij een handicap 2:0 heeft de thuisploeg dus een flinke virtuele voorsprong. Je kiest daarna nog steeds uit drie uitkomsten: 1, X of 2 na de handicap.</p>
<h3><strong>Rekenvoorbeeld: zo verschillen de handicaps in euro's</strong></h3>
<p>Stel: Ajax speelt thuis tegen Heracles en is grote favoriet. Je zet steeds €10 in. In de tabel zie je wat je in totaal terugkrijgt (inclusief inzet) bij drie mogelijke uitslagen.</p>
{tabel(["Weddenschap (odd)", "Ajax wint 3-0", "Ajax wint 2-1", "1-1"], [
    ("<strong>Ajax wint, 1X2</strong> (1,35)", eur(13.5), eur(13.5), eur(0)),
    ("<strong>Ajax −1 Asian</strong> (1,80)", ah(-1, 3, 1.80), ah(-1, 1, 1.80) + " (inzet terug)", ah(-1, 0, 1.80)),
    ("<strong>Ajax −1,5 Asian</strong> (2,05)", ah(-1.5, 3, 2.05), ah(-1.5, 1, 2.05), ah(-1.5, 0, 2.05)),
    ("<strong>Ajax (0:1) Europees, uitkomst 1</strong> (2,10)", eh_bet(-1, 3, "1", 2.10), eh_bet(-1, 1, "1", 2.10), eh_bet(-1, 0, "1", 2.10)),
    ("<strong>Heracles +1,5 Asian</strong> (1,80)", ah(1.5, -3, 1.80), ah(1.5, -1, 1.80), ah(1.5, 0, 1.80)),
])}
<p><em>De quoteringen in dit voorbeeld zijn fictief en alleen bedoeld om de berekening te laten zien.</em></p>
<p>Je ziet het patroon: hoe groter de handicap op de favoriet, hoe hoger de quotering, maar hoe minder uitslagen goed voor je zijn. De Asian −1 beschermt je bij een zege met 1 verschil, de Europese handicap en de −1,5 niet. Op de underdog werkt het andersom: Heracles +1,5 wint zelfs bij een nipte nederlaag.</p>
<h3><strong>Hoe werkt handicap wedden bij tennis?</strong></h3>
<p>Bij tennis zijn er twee varianten. Bij de <strong>game-handicap</strong> tel je alle games van de wedstrijd bij elkaar. Speel je Speler A −4,5 games (odd 1,85) en wint hij met 6-4, 6-3, dan is het 12-7 in games: 5 verschil, dus je wint en krijgt {ah(-4.5, 5, 1.85)} terug. Wint hij met 7-6, 6-4, dan is het 13-10: maar 3 verschil, en verlies je je inzet, ook al won je speler de partij.</p>
<p>Bij de <strong>set-handicap</strong> gaat het om sets. Speler A −1,5 sets betekent in een best-of-three dat hij met 2-0 moet winnen. Speler B +1,5 sets wint als B minstens één set pakt.</p>
<p>Let op: in Nederland mag je niet wedden op de winnaar van <strong>één specifieke game of set</strong>, zoals "wie wint de tweede set". Een game- of set-handicap over de hele wedstrijd mag wel.</p>
<h3><strong>Hoe werkt handicap wedden bij basketbal?</strong></h3>
<p>Bij basketbal heet de handicap vaak <strong>spread</strong> of <strong>puntenhandicap</strong>. Omdat er veel punten vallen, zijn de lijnen groter, zoals −6,5 of +11,5. Speel je een team op −6,5 (odd 1,90), dan moet het met 7 punten of meer winnen. Bij 104-99 verlies je, bij 110-101 krijg je {ah(-6.5, 9, 1.90)} terug. Bij basketbal telt de verlenging meestal mee voor de handicap, anders dan bij voetbal. Controleer dit altijd in de marktregels van je bookmaker.</p>"""

content3 = f"""<h3><strong>Welke handicap kies je?</strong></h3>
{tabel(["Jouw verwachting", "Passende keuze"], [
    ("Favoriet wint ruim, met 2 of meer verschil", "Asian −1,5 of Europese handicap −1 (uitkomst 1)"),
    ("Favoriet wint, maar misschien nipt", "Asian −1 of −0,75: bij 1 verschil krijg je (een deel van) je inzet terug"),
    ("Favoriet wint precies met 1 verschil", "Europese handicap −1, uitkomst X (hoge quotering, smal scenario)"),
    ("Underdog houdt het close", "Asian +1,5 of +1 op de underdog"),
    ("Je twijfelt tussen winst en gelijkspel", "Asian 0 (draw no bet) of +0,5"),
    ("Tennis: favoriet wint overtuigend", "Game-handicap −3,5 of −4,5, of set-handicap −1,5"),
])}
<p>Begin bij twijfel met halve lijnen of de Asian handicap 0. Die zijn het makkelijkst te volgen. De Europese handicap is overzichtelijk, maar door de derde uitkomst ligt de marge vaak hoger. Vergelijk de quoteringen altijd even met onze <a href="/odds-vergelijken-bij-alle-bookmakers-beste-odds-vandaag">odds vergelijker</a>, want per bookmaker kan een handicap flink verschillen.</p>
<h3><strong>Tips en valkuilen bij handicap wedden</strong></h3>
<ul><li><strong>Een hogere quotering is geen betere kans.</strong> Een handicap verschuift alleen het risico. De bookmaker rekent op elke lijn een marge.</li><li><strong>Alleen de reguliere speeltijd telt bij voetbal.</strong> Blessuretijd telt mee, verlenging en strafschoppen niet.</li><li><strong>Let op live handicaps.</strong> Bij veel bookmakers telt bij een live Asian handicap alleen wat er gebeurt na het plaatsen van je weddenschap. Lees meer over <a href="/nieuws/uitleg-in-play-live-wedden-dynamiek-strategie-en-kansen-in-realtime">live wedden</a>.</li><li><strong>Kijk naar speelstijl, niet alleen naar de stand.</strong> Een favoriet die na een 1-0 voorsprong gas terugneemt, haalt een −1,5 minder vaak dan de ranglijst doet vermoeden.</li><li><strong>Handicaps in een combinatie maken het risico groter.</strong> Elke extra selectie moet ook uitkomen. Lees hoe een <a href="/nieuws/uitleg-wedstrategie-accumulator-weddenschappen">accumulator</a> werkt.</li><li><strong>Zet nooit meer in dan je kunt missen.</strong> Handicap wedden blijft een kansspel.</li></ul>
<h3><strong>Handicap wedden bij TOTO en andere Nederlandse bookmakers</strong></h3>
<p>De namen verschillen per bookmaker. Bij TOTO en andere legale bookmakers vind je de Europese handicap onder namen als "Handicap", "3-weg handicap" of "handicap resultaat", vaak met een notatie als (0:1). De Asian handicap heet ook wel "Aziatische handicap", "Asian lines" of "handicap (2-weg)". Bij basketbal staat er vaak "handicap" of "spread", bij tennis "games handicap" of "sets handicap". Heb je twijfel wat een markt precies inhoudt? De bookmaker moet de regels per wedoptie in zijn voorwaarden vermelden.</p>
<h3><strong>Mag je in Nederland handicap wedden?</strong></h3>
<p>Ja. Handicap wedden is in Nederland toegestaan bij bookmakers met een vergunning van de Kansspelautoriteit. De handicap draait om de uitslag, het aantal doelpunten, games of punten, en dat zijn toegestane markten. Wat niet mag: wedden op corners, kaarten en andere makkelijk te manipuleren gebeurtenissen, en bij tennis op de winnaar van een specifieke game of set. Lees ook <a href="/nieuws/dit-is-waarom-wedden-op-corners-niet-meer-legaal-is-in-nederland">waarom wedden op corners niet legaal is</a>. Speel je bij een site zonder Nederlandse vergunning, dan is dat illegaal en heb je geen enkele bescherming. Check het met ons artikel <a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe weet ik of een bookmaker legaal is</a>.</p>
<p>Legale bookmakers die wij aanraden:</p>
{aanraders()}
<h3><strong>Veelgestelde vragen over handicap wedden</strong></h3>
<p><strong>Wat betekent handicap bij TOTO?</strong><br>Hetzelfde als bij elke andere bookmaker: een team krijgt een virtuele voor- of achterstand die je na afloop optelt bij de uitslag. Bij een 3-weg handicap kies je uit 1, X of 2 na de handicap, bij een 2-weg (Asian) handicap uit twee kanten.</p>
<p><strong>Wat is handicap resultaat?</strong><br>Met "handicap resultaat" wordt meestal de Europese of 3-weg handicap bedoeld: de uitslag (1X2) nadat de handicap is toegepast.</p>
<p><strong>Wat betekent +1,5 handicap?</strong><br>Jouw team mag met maximaal 1 doelpunt verschil verliezen. Bij winst, gelijkspel of een nederlaag met 1 verschil win je. Verliest het met 2 of meer verschil, dan verlies je.</p>
<p><strong>Wat betekent 0,5 handicap?</strong><br>−0,5 betekent dat je team moet winnen. +0,5 betekent dat je team mag winnen of gelijkspelen. Een virtueel gelijkspel is bij een halve lijn onmogelijk.</p>
<p><strong>Wat betekent handicap 2:0?</strong><br>De thuisploeg begint virtueel met een 2-0 voorsprong. Eindigt de wedstrijd in 0-1, dan wordt het na de handicap 2-1 en wint de uitkomst 1.</p>
<p><strong>Wat is het verschil tussen een Europese en een Asian handicap?</strong><br>De Europese handicap heeft drie uitkomsten en alleen hele getallen. De Asian handicap heeft twee uitkomsten en ook halve en kwartlijnen, waardoor je bij een virtueel gelijkspel je inzet (deels) terugkrijgt.</p>
<p><strong>Telt de verlenging mee bij handicap wedden?</strong><br>Bij voetbal niet: alleen de reguliere speeltijd inclusief blessuretijd telt. Bij basketbal telt de verlenging meestal wel mee. Check altijd de regels van de markt.</p>
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
