# -*- coding: utf-8 -*-
"""Herschrijving (bestaand item 6656f1ea2bb63bb47fb7c938): Dit is hoe wedden op schoten (op doel) werkt.
Feiten (schoten_facts 21-10-2026): Opta/The Analyst-definities, TOTO 'Nadere regels per sport' (23-09-2026),
Kambi Rules v2.2 NL (Unibet, sept. 2026), Rkoa bijlage 2, FotMob/Opta-statistieken, Unibet-feed PSV-Feyenoord 21-10-2026.
Zoekvragen GSC: kopbal/penalty/speler start niet/verschil schoten-schoten op doel/1+ 2+ 3+.
  python3 specials/schoten_op_doel.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lk_webflow as WF
from legaal_data import tabel, aanraders

ITEM_ID = "6656f1ea2bb63bb47fb7c938"
TITEL = "Dit is hoe wedden op schoten (op doel) werkt: regels, markten en tips"
SAMENVATTING = ("Wat telt als schot op doel? Paal, kopbal, penalty en geblokte schoten uitgelegd, plus de regels van TOTO "
                "en Unibet, statistieken en tips.")
S = "https://www.bet-experts.nl/be-static/"


def fig(fn, alt, cap):
    return (f'<figure class="w-richtext-align-fullwidth w-richtext-figure-type-image" style="max-width:100%"><div>'
            f'<img src="{S}{fn}" alt="{alt}" loading="lazy"></div><figcaption>{cap}</figcaption></figure>')


content = f"""<p><strong>Een schot op doel is een bewuste doelpoging die in het doel gaat, door de keeper wordt gestopt of door de laatste verdediger van de lijn wordt gehaald. Een schot tegen de paal of lat telt níet, net als een schot dat naast gaat of door een verdediger wordt geblokt. Bij wedden op schoten op doel voorspel je hoeveel schoten op doel een speler, een team of een hele wedstrijd haalt, bijvoorbeeld "meer dan 0,5" (1+). Bookmakers als TOTO en Unibet handelen die weddenschappen af op basis van de officiële data van Opta.</strong></p>
<p>Iedere wedder kent het: je speler raakt in de laatste minuut de lat, en toch is je weddenschap verloren. In dit artikel lees je precies wat wel en niet telt als schot op doel, wat het verschil is met "schoten", hoe de markten werken, welke regels TOTO en Unibet hanteren (ook als je speler niet start) en waar je op let bij het kiezen van een weddenschap.</p>
<h3><strong>Wat is een schot op doel?</strong></h3>
<p>De meeste Nederlandse bookmakers volgen de definitie van Opta, het sportdatabedrijf achter de officiële statistieken van onder meer de Premier League. Volgens Opta is een schot op doel een bewuste poging om te scoren die op doel is. Dat zijn drie situaties:</p>
<ul><li><strong>Een doelpunt</strong>, ook als de bal via de paal, de lat of een verdediger erin gaat.</li><li><strong>Een redding van de keeper</strong> op een schot dat anders in het doel was gegaan.</li><li><strong>Een redding door de laatste man</strong>, bijvoorbeeld een verdediger die de bal van de lijn haalt terwijl de keeper al verslagen is.</li></ul>
{fig("schoten-schot-op-doel-1294c966.webp", "Wat telt als schot op doel: doelpunt, redding keeper en laatste man wel; paal of lat, naast en geblokt niet", "Wat telt wel en niet als schot op doel volgens Opta")}
<h3><strong>Wat is het verschil tussen schoten en schoten op doel?</strong></h3>
<p>Bij "schoten" (ook wel "schoten totaal" of "doelpogingen") telt elke bewuste doelpoging mee, ook als de bal naast gaat, tegen de paal komt of wordt geblokt. Bij "schoten op doel" tellen alleen de pogingen die echt op doel zijn. Elk schot op doel is dus ook een schot, maar niet andersom.</p>
{tabel(["Situatie", "Schot", "Schot op doel"], [
    ("Doelpunt", "✓", "✓"),
    ("Redding van de keeper", "✓", "✓"),
    ("Van de lijn gehaald door de laatste man", "✓", "✓"),
    ("Tegen paal of lat (geen doelpunt)", "✓", "✗"),
    ("Naast of over", "✓", "✗"),
    ("Geblokt door een verdediger (met nog iemand achter zich)", "✓", "✗"),
    ("Eigen doelpunt van de tegenstander", "✗", "✗"),
])}
<h3><strong>Telt het als schot op doel? De lastige gevallen</strong></h3>
{tabel(["Situatie", "Schot op doel?"], [
    ("<strong>Kopbal</strong> die de keeper tegenhoudt", "Ja, een kopbal is gewoon een schot"),
    ("<strong>Penalty</strong> die erin gaat of wordt gestopt", "Ja"),
    ("Penalty naast of tegen de paal", "Nee"),
    ("Schot tegen de paal of lat, daarna in het doel", "Ja, want het wordt een doelpunt"),
    ("Schot tegen de paal dat via de keeper terugkomt", "Nee"),
    ("Van richting veranderd schot dat de keeper stopt", "Ja"),
    ("Geblokt schot dat zonder kracht bij de keeper komt", "Nee"),
    ("Schot dat naast zou gaan, maar door de keeper wordt gepakt", "Nee"),
    ("Hoekschop direct op doel, keeper houdt tegen", "Nee"),
    ("Doelpunt rechtstreeks uit een hoekschop", "Ja"),
    ("Voorzet die op doel komt en door de keeper wordt gevangen", "Nee, geen bewuste doelpoging"),
    ("Schot in de verlenging of strafschoppenserie", "Telt niet mee voor je weddenschap"),
])}
<p><em>Gebaseerd op de definities van Opta en de voorbeelden in de wedregels van TOTO (geldig vanaf 23 september 2026).</em></p>"""

content2 = f"""<h3><strong>Hoe werkt wedden op schoten op doel?</strong></h3>
<p>Je voorspelt niet het exacte aantal, maar of het aantal schoten op doel boven of onder een lijn uitkomt die de bookmaker bepaalt. De meest gebruikte markten:</p>
<ul><li><strong>Speler schoten op doel:</strong> haalt een speler meer of minder dan bijvoorbeeld 0,5 of 1,5 schoten op doel? Dit is de populairste markt.</li><li><strong>Team schoten op doel:</strong> het aantal schoten op doel van één ploeg.</li><li><strong>Totaal schoten op doel in de wedstrijd:</strong> beide teams samen.</li><li><strong>Speler schoten (totaal):</strong> alle doelpogingen van een speler, dus ook naast en geblokt. Niet elke bookmaker biedt deze markt aan.</li><li><strong>Bet builder:</strong> combineer schoten op doel met andere markten uit dezelfde wedstrijd, zoals de winnaar of een doelpuntenmaker.</li></ul>
<p><strong>Wat betekent 1+ schoten op doel?</strong><br>1+ betekent minimaal één schot op doel, en is hetzelfde als "meer dan 0,5". 2+ is meer dan 1,5 (minimaal twee) en 3+ is meer dan 2,5 (minimaal drie). Bij "minder dan 1,5" win je als je speler nul of één schot op doel heeft.</p>
{fig("schoten-lijnen-61683248.webp", "Uitleg lijnen schoten op doel: 1+ is meer dan 0,5, 2+ is meer dan 1,5 en 3+ is meer dan 2,5", "1+, 2+ en 3+ schoten op doel uitgelegd")}
<p><strong>Voorbeeld: PSV – Feyenoord</strong><br>Zo zagen de markten er bij Unibet uit voor PSV – Feyenoord van zondag 25 oktober 2026 (stand op 21 oktober; quoteringen veranderen voortdurend):</p>
{tabel(["Markt", "Quotering"], [
    ("Ruben van Bommel meer dan 0,5 schoten op doel (1+)", "1,42"),
    ("Ruben van Bommel meer dan 1,5 schoten op doel (2+)", "2,80"),
    ("Anis Hadj Moussa meer dan 0,5 schoten op doel", "1,55"),
    ("Totaal schoten op doel meer dan 10,5", "1,67"),
    ("Totaal schoten op doel minder dan 10,5", "1,86"),
    ("PSV meer dan 5,5 schoten op doel", "1,68"),
    ("Feyenoord meer dan 4,5 schoten op doel", "1,74"),
])}
<p>Bekijk voor actuele quoteringen altijd meerdere bookmakers, bijvoorbeeld via onze <a href="/odds-vergelijken-bij-alle-bookmakers-beste-odds-vandaag">odds vergelijker</a>.</p>
<h3><strong>De regels per bookmaker: wat als je speler niet start?</strong></h3>
<p>De kleine lettertjes verschillen per bookmaker, en dat merk je vooral als je speler op de bank begint. De twee grootste systemen in Nederland zijn TOTO en Kambi. Kambi is het sportsbook achter Unibet, LeoVegas, JACKS.NL en Oranje Palace.</p>
{tabel(["Regel", "TOTO", "Unibet en andere Kambi-sites"], [
    ("Databron", "Opta (Stats Perform); andere bronnen tellen niet", "Opta (de markt heet 'Volgens Opta-gegevens')"),
    ("Speeltijd", "Reguliere speeltijd inclusief blessuretijd", "90 minuten inclusief blessuretijd"),
    ("Verlenging en strafschoppen", "Tellen niet mee", "Tellen niet mee"),
    ("Speler start op de bank", "Weddenschap blijft staan als hij invalt", "Spelersweddenschappen vereisen volgens de voorwaarden dat de speler vanaf de aftrap speelt"),
    ("Speler speelt helemaal niet", "Ongeldig, inzet terug", "Ongeldig, inzet terug"),
    ("Eigen doelpunten", "Tellen niet mee", "Tellen niet mee"),
    ("Bet builder met een ongeldige selectie", "Hele bet builder ongeldig", "Hele bet builder ongeldig"),
])}
<p><em>Bronnen: TOTO Nadere regels per sport (23 september 2026) en de algemene sportsbookvoorwaarden van Unibet/Kambi (versie 2.2, september 2026).</em></p>
<p>Bij andere bookmakers, zoals bet365, BetCity, Circus of Bingoal, kunnen de regels afwijken. Check bij twijfel de wedregels van je bookmaker, en kijk vóór je inzet of je speler in de basis staat. De vermoedelijke en definitieve opstellingen vind je op onze pagina <a href="/opstellingen">opstellingen</a>.</p>
<h3><strong>Is wedden op schoten op doel legaal?</strong></h3>
<p>Ja. Schoten en schoten op doel staan niet op de lijst met verboden weddenschappen van de Regeling kansspelen op afstand. Legale bookmakers bieden ze dan ook gewoon aan. Wedden op corners, kaarten, inworpen en buitenspel mag in Nederland wel niet; lees daarover ons artikel <a href="/nieuws/dit-is-waarom-wedden-op-corners-niet-meer-legaal-is-in-nederland">waarom wedden op corners niet meer legaal is</a>.</p>"""

content3 = f"""<h3><strong>Statistieken: hoeveel schoten op doel zijn normaal?</strong></h3>
{tabel(["Competitie", "Schoten op doel per wedstrijd 2025-26", "Lopend seizoen 2026-27"], [
    ("Eredivisie", "10,4", "10,5"),
    ("Premier League", "8,4", "8,7"),
    ("Champions League", "10,4", "11,2"),
])}
<p><em>Beide teams samen. Bron: Opta-data via FotMob, eigen berekening (peildatum 21 oktober 2026; het lopende seizoen is nog een kleine steekproef).</em></p>
<p>Gemiddeld wordt ongeveer één op de drie schoten op doel een doelpunt. In de Eredivisie vallen per wedstrijd duidelijk meer schoten op doel dan in de Premier League, waar verdedigingen sterker zijn.</p>
<p><strong>Spelers met de meeste schoten op doel per 90 minuten (2025-26)</strong></p>
{tabel(["Eredivisie", "Per 90 min", "Premier League", "Per 90 min"], [
    ("Ricardo Pepi (PSV)", "2,0", "Benjamin Šeško (Man United)", "1,9"),
    ("Troy Parrott (AZ)", "1,8", "Erling Haaland (Man City)", "1,8"),
    ("Milan Zonneveld (Sparta)", "1,7", "Jean-Philippe Mateta (Crystal Palace)", "1,3"),
    ("Ayase Ueda (Feyenoord)", "1,6", "Matheus Cunha (Man United)", "1,3"),
    ("Ismael Saibari (PSV)", "1,6", "Ollie Watkins (Aston Villa)", "1,2"),
])}
<p><em>Bron: Opta-data via FotMob, spelers met minimaal 900 speelminuten.</em></p>
<h3><strong>Tips voor wedden op schoten op doel</strong></h3>
<ul><li><strong>Check de opstelling.</strong> Zeker bij Kambi-bookmakers kan een basisplaats het verschil maken. Wacht bij twijfel tot de officiële opstelling bekend is.</li><li><strong>Kijk naar schoten op doel per 90 minuten</strong>, niet alleen naar het totaal. Een speler die vaak wordt gewisseld, haalt minder schoten dan zijn gemiddelde doet vermoeden.</li><li><strong>Let op de rol van de speler.</strong> Is hij de vaste penaltynemer of de nummer 9, dan heeft hij meer kansen dan een middenvelder met hetzelfde gemiddelde.</li><li><strong>Bekijk de tegenstander.</strong> Tegen een ploeg die veel kansen weggeeft, worden lijnen sneller gehaald. Ook thuis of uit spelen maakt verschil.</li><li><strong>Vergeet de lat niet.</strong> Een speler die vaak van afstand schiet, raakt vaker paal, lat of een verdediger. Dat telt wel als schot, maar niet als schot op doel.</li><li><strong>Vergelijk de quoteringen.</strong> Lijnen en odds verschillen per bookmaker, en een kleine verschuiving in de lijn (0,5 of 1,5) heeft grote invloed op je kans.</li></ul>
<p>Meer over hoe bookmakers de statistieken vastleggen, lees je in ons artikel <a href="/nieuws/wat-zijn-opta-gegevens-alles-over-schoten-op-doel-en-unibet-weddenschappen">wat zijn Opta-gegevens</a>. Op zoek naar tips per wedstrijd? Bekijk onze <a href="/voetbal-voorspellingen-vandaag">voetbal voorspellingen van vandaag</a> en al onze <a href="/wedtips">wedtips</a>.</p>
<h3><strong>Waar kun je wedden op schoten op doel?</strong></h3>
<p>Vrijwel alle legale Nederlandse bookmakers bieden schoten-op-doelmarkten aan, waaronder TOTO, Unibet, LeoVegas en JACKS.NL. Onze aanraders:</p>
{aanraders()}
<h3><strong>Veelgestelde vragen over schoten op doel</strong></h3>
<p><strong>Telt een kopbal als schot op doel?</strong><br>Ja. Een kopbal is gewoon een schot. Gaat hij erin of moet de keeper hem tegenhouden, dan telt hij als schot op doel, ook bij TOTO en Unibet.</p>
<p><strong>Telt een penalty als schot op doel?</strong><br>Ja, als de penalty erin gaat of door de keeper wordt gestopt. Een penalty naast of tegen de paal telt niet. Penalty's in een strafschoppenserie tellen nooit mee.</p>
<p><strong>Telt een schot op de paal als schot op doel?</strong><br>Nee, tenzij de bal daarna direct in het doel gaat. Een schot tegen de paal of lat telt wel als schot (totaal).</p>
<p><strong>Wat gebeurt er als mijn speler niet in de basis start?</strong><br>Dat verschilt per bookmaker. Bij TOTO blijft je weddenschap staan als de speler invalt. Volgens de voorwaarden van Unibet en andere Kambi-sites moeten spelers vanaf de aftrap spelen. Speelt je speler helemaal niet, dan krijg je bij beide je inzet terug.</p>
<p><strong>Wat betekent 1+ schoten op doel?</strong><br>Minimaal één schot op doel, hetzelfde als "meer dan 0,5". 2+ betekent minimaal twee, 3+ minimaal drie.</p>
<p><strong>Wat is het verschil tussen schoten en schoten op doel?</strong><br>Bij schoten telt elke doelpoging mee, ook naast, tegen de paal of geblokt. Bij schoten op doel alleen doelpunten, reddingen van de keeper en reddingen door de laatste man.</p>
<p><strong>Telt de verlenging mee?</strong><br>Nee. Alleen de reguliere speeltijd inclusief blessuretijd telt, tenzij de bookmaker bij de markt iets anders vermeldt.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "content": content, "content-2": content2, "content-3": content3, "samenvatting": SAMENVATTING,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        import re
        tekst = re.sub(r"<[^>]+>", " ", content + content2 + content3)
        print(len(SAMENVATTING), "tekens samenvatting |", len(tekst.split()), "woorden"); sys.exit()
    print(WF.update_live(ITEM_ID, fd).get("id"))
