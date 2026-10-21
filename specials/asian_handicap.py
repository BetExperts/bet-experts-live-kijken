# -*- coding: utf-8 -*-
"""Herschrijving Nieuws-item 65047943217fd699abc2f47c (Kennisbank-versie 69b2a4aeadc3297af302cc5a is offline + 301): Wat is een Asian Handicap weddenschap? (+ Asian totaal).
Alle bedragen worden berekend met og_kaarten/asian_rekenen.py (zelfde rekenregels als de tabellen).
Visuals + pdf's: og_kaarten/asian.py -> be-static; deelkaart og/kennisbank/asian-handicap.webp (GitHub raw).
  python3 specials/asian_handicap.py [--live]"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, os.path.join(HIER, "..", "og_kaarten"))
sys.path.insert(0, HIER)
import lk_webflow as WF
from legaal_data import tabel, aanraders
from asian_rekenen import handicap, totaal, uitbetaling

KB_COLLECTION = "69b2a19a8be17864afce6d78"
ITEM_ID = "65047943217fd699abc2f47c"   # Nieuws
TITEL = "Wat is een Asian Handicap? Uitleg, tabel en voorbeelden"
INTRO = ("Bij een Asian Handicap krijgt een team een virtuele voor- of achterstand, zodat een gelijkspel als uitkomst "
         "verdwijnt. Bij hele en kwartlijnen kun je je inzet (deels) terugkrijgen.")
SAMENVATTING = ("Asian handicap uitleg met tabel: hele, halve en kwartlijnen, halve winst, inzet terug en Asian "
                "totaal. Met rekenvoorbeelden en gratis pdf.")
STATIC = "https://www.bet-experts.nl/be-static/"
OG = "https://raw.githubusercontent.com/BetExperts/bet-experts-live-kijken/main/og/kennisbank/asian-handicap.webp"
AH_IMG, AH_PDF = STATIC + "asian-handicap-tabel-38c9df73.webp", STATIC + "asian-handicap-tabel-ce02c40f.pdf"
AT_IMG, AT_PDF = STATIC + "asian-totaal-tabel-d39cc290.webp", STATIC + "asian-totaal-tabel-fd278613.pdf"
VB_AH, VB_AT = STATIC + "asian-vis-voorbeeld-218348ca.webp", STATIC + "asian-vis-totaal-a20cd546.webp"


def eur(x):
    return f"€{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def ah(lijn, saldo, odd, inzet=10):
    return eur(uitbetaling(handicap(lijn, saldo), inzet, odd))


def tot(lijn, goals, odd, over=True, inzet=10):
    return eur(uitbetaling(totaal(lijn, goals, over), inzet, odd))


def figuur(src, alt, onderschrift):
    return (f'<figure class="w-richtext-align-fullwidth w-richtext-figure-type-image" style="max-width:100%"><div>'
            f'<img src="{src}" alt="{alt}" loading="lazy"></div><figcaption>{onderschrift}</figcaption></figure>')


def pdf_link(href, tekst):
    return f'<p><strong><a href="{href}" target="_blank">📄 {tekst}</a></strong></p>'


# controle: de bedragen in de tekst moeten kloppen met de rekenregels (en dus met de tabellen)
assert ah(-0.75, 1, 1.90) == "€14,50" and ah(-0.75, 2, 1.90) == "€19,00" and ah(-0.75, 0, 1.90) == "€0,00"
assert ah(-1, 1, 1.90) == "€10,00" and ah(-0.25, 0, 1.95) == "€5,00" and ah(0.25, 0, 1.90) == "€14,50"
assert ah(-1.25, 1, 2.05) == "€5,00" and ah(-1.25, 2, 2.05) == "€20,50" and ah(0, 0, 1.60) == "€10,00"
assert tot(2.25, 2, 1.85) == "€5,00" and tot(2.25, 3, 1.85) == "€18,50" and tot(2, 2, 1.80) == "€10,00"
assert tot(2.75, 3, 1.95) == "€14,75" and tot(2.75, 4, 1.95) == "€19,50" and tot(2.25, 2, 1.95, False) == "€14,75"
assert tot(3, 3, 1.90, False) == "€10,00" and tot(2.25, 3, 1.95, False) == "€0,00"

content = f"""<p><strong>Een Asian Handicap is een weddenschap waarbij de bookmaker een team een virtuele voorsprong of achterstand geeft, bijvoorbeeld −1 of +0,5. Na het laatste fluitsignaal tel je die handicap op bij de echte uitslag. Omdat er maar twee kanten zijn, valt het gelijkspel als uitkomst weg. Bij een hele lijn (zoals −1) kun je je inzet terugkrijgen, en bij een kwartlijn (zoals −0,75) wordt je inzet in tweeën gesplitst, zodat je ook half kunt winnen of half kunt verliezen. Hetzelfde systeem bestaat voor doelpunten: dat heet Asian totaal of Asian over/under.</strong></p>
<p>Asian handicap klinkt ingewikkeld door alle getallen achter de komma, maar er zit een simpele logica achter. In deze uitleg lees je stap voor stap hoe het werkt, met een duidelijke tabel waarin je per handicap en per uitslag ziet wat er met je inzet gebeurt, en met rekenvoorbeelden in euro's. Beide tabellen kun je gratis als pdf downloaden.</p>
<h3><strong>Hoe werkt een Asian Handicap?</strong></h3>
<p>Bij een gewone 1X2-weddenschap heb je drie uitkomsten: thuiswinst, gelijkspel of uitwinst. Is een team duidelijk favoriet, dan is de quotering op dat team vaak zo laag dat inzetten weinig oplevert. De Asian handicap lost dat op: de favoriet begint met een achterstand (een min-getal) en de underdog met een voorsprong (een plus-getal). Zo worden beide kanten ongeveer even kansrijk en liggen de quoteringen meestal rond de 1,90.</p>
<p>Het werkt in drie stappen:</p>
<ol><li><strong>Kies een team en een lijn,</strong> bijvoorbeeld PSV −1.</li><li><strong>Tel na de wedstrijd de handicap op bij de uitslag van jouw team.</strong> Wint PSV met 3-1, dan wordt het met −1 virtueel 2-1.</li><li><strong>Kijk wie de virtuele wedstrijd wint.</strong> Staat jouw team virtueel voor, dan win je. Staat het virtueel gelijk, dan krijg je je inzet terug. Staat het virtueel achter, dan verlies je.</li></ol>
<p>Het makkelijkst is om alleen naar het <strong>doelsaldo</strong> te kijken: met hoeveel doelpunten verschil wint of verliest jouw team? Dat getal plus de handicap bepaalt de uitkomst. Wint PSV met 2 verschil en speel je −1, dan houd je +1 over: gewonnen.</p>
<h3><strong>Drie soorten lijnen: hele, halve en kwartlijnen</strong></h3>
<p>Elke Asian handicap valt in één van drie groepen. Zodra je weet in welke groep een lijn valt, weet je ook welke uitkomsten mogelijk zijn.</p>
{tabel(["Soort lijn", "Voorbeelden", "Wat kan er gebeuren?"], [
    ("<strong>Halve lijn</strong>", "−0,5 / +0,5 / −1,5 / +1,5", "Alleen winst of verlies. Een virtueel gelijkspel kan niet, want je kunt geen halve goal maken."),
    ("<strong>Hele lijn</strong>", "0 / −1 / +1 / −2 / +2", "Winst, verlies of <strong>inzet terug</strong> (push) als het virtueel gelijk staat."),
    ("<strong>Kwartlijn</strong>", "−0,25 / +0,25 / −0,75 / +0,75 / −1,25", "Je inzet wordt verdeeld over de twee lijnen ernaast. Daardoor kun je ook <strong>half winnen</strong> of <strong>half verliezen</strong>."),
])}
<p><strong>Kwartlijnen uitgelegd.</strong> Een kwartlijn ligt precies tussen een hele en een halve lijn. De bookmaker zet de helft van je inzet op de lijn eronder en de helft op de lijn erboven. €10 op −0,75 is dus €5 op −0,5 en €5 op −1. Je ziet kwartlijnen daarom ook vaak geschreven als <strong>−0,5/−1</strong> of <strong>0,5-1</strong>: dat betekent hetzelfde.</p>
<h3><strong>Asian handicap tabel: alle lijnen in één overzicht</strong></h3>
<p>In de tabel hieronder zie je voor elke handicap van −2 tot +2 wat er met je inzet gebeurt. Kies links je handicap en kijk in de kolom naar de uitslag van jouw team: groen is winst, lichtgroen halve winst, grijs inzet terug, roze half verlies en rood verlies.</p>
{figuur(AH_IMG, "Asian handicap tabel: per handicap van -2 tot +2 en per uitslag (wint met 3+, 2, 1, gelijk, verliest met 1, 2, 3+) of je wint, half wint, je inzet terugkrijgt, half verliest of verliest", "Asian handicap tabel: kies je handicap (rij) en kijk naar de uitslag van jouw team (kolom)")}
{pdf_link(AH_PDF, "Download de Asian handicap tabel als pdf (A4)")}
<h3><strong>De belangrijkste lijnen in gewone taal</strong></h3>
{tabel(["Handicap", "Jouw team moet...", "Bij een gelijkspel"], [
    ("<strong>0 (draw no bet)</strong>", "winnen", "Inzet terug"),
    ("<strong>−0,25</strong>", "winnen", "Half verlies (de helft terug)"),
    ("<strong>−0,5</strong>", "winnen (gelijk aan gewone winst in 1X2)", "Verlies"),
    ("<strong>−0,75</strong>", "met 2 verschil winnen voor volle winst; met 1 verschil is het halve winst", "Verlies"),
    ("<strong>−1</strong>", "met 2 verschil winnen; met 1 verschil krijg je je inzet terug", "Verlies"),
    ("<strong>−1,5</strong>", "met 2 of meer verschil winnen", "Verlies"),
    ("<strong>+0,25</strong>", "niet verliezen; winst is volle winst", "Halve winst"),
    ("<strong>+0,5</strong>", "winnen of gelijkspelen (gelijk aan dubbele kans)", "Winst"),
    ("<strong>+1</strong>", "niet verliezen; bij verlies met 1 verschil krijg je je inzet terug", "Winst"),
    ("<strong>+1,5</strong>", "winnen, gelijkspelen of met maximaal 1 verschil verliezen", "Winst"),
])}
<p>Een handicap aan de ene kant is altijd het spiegelbeeld van de andere kant. Speelt PSV −0,75, dan speelt de tegenstander +0,75. Wat voor de één halve winst is, is voor de ander half verlies.</p>"""

content2 = f"""<h3><strong>Rekenvoorbeelden: zo reken je een Asian handicap uit</strong></h3>
<p>Bij een Asian handicap reken je per helft van je inzet. Bij <strong>halve winst</strong> wint de ene helft tegen de quotering en krijg je de andere helft terug. Bij <strong>half verlies</strong> ben je de ene helft kwijt en krijg je de andere helft terug. De bedragen hieronder zijn wat je in totaal terugkrijgt, inclusief je inzet.</p>
{figuur(VB_AH, "Rekenvoorbeeld Asian handicap: 10 euro op PSV -0,75 tegen Feyenoord tegen odd 1,90. Wint PSV met 2 of meer: 19 euro. Wint PSV met 1: halve winst, 14,50 euro. Gelijk of verlies: 0 euro", "Rekenvoorbeeld: €10 op PSV −0,75, verdeeld over −0,5 en −1")}
<p><strong>Voorbeeld 1: PSV −0,75 tegen Feyenoord (odd 1,90, inzet €10)</strong></p>
<ul><li>PSV wint met 2-0: beide helften winnen. Je krijgt <strong>{ah(-0.75, 2, 1.90)}</strong> terug.</li><li>PSV wint met 2-1: de €5 op −0,5 wint (€9,50), de €5 op −1 is een push (€5 terug). Samen <strong>{ah(-0.75, 1, 1.90)}</strong>: halve winst.</li><li>Gelijkspel of verlies: beide helften verliezen. Je krijgt <strong>{ah(-0.75, 0, 1.90)}</strong>.</li></ul>
<p><strong>Voorbeeld 2: Ajax −1 tegen AZ (odd 1,90, inzet €10)</strong></p>
<ul><li>Ajax wint met 2 of meer verschil: <strong>{ah(-1, 2, 1.90)}</strong>.</li><li>Ajax wint met precies 1 verschil: virtueel gelijk, je krijgt je inzet terug: <strong>{ah(-1, 1, 1.90)}</strong>.</li><li>Gelijkspel of verlies: <strong>{ah(-1, 0, 1.90)}</strong>.</li></ul>
<p><strong>Voorbeeld 3: Feyenoord −0,25 tegen FC Twente (odd 1,95, inzet €10)</strong></p>
<ul><li>Feyenoord wint: <strong>{ah(-0.25, 1, 1.95)}</strong>.</li><li>Gelijkspel: de €5 op 0 wordt terugbetaald, de €5 op −0,5 verliest. Je krijgt <strong>{ah(-0.25, 0, 1.95)}</strong>: half verlies.</li><li>Feyenoord verliest: <strong>{ah(-0.25, -1, 1.95)}</strong>.</li></ul>
<p><strong>Voorbeeld 4: Go Ahead Eagles +0,25 tegen PSV (odd 1,90, inzet €10)</strong></p>
<ul><li>Go Ahead wint: <strong>{ah(0.25, 1, 1.90)}</strong>.</li><li>Gelijkspel: de €5 op +0,5 wint (€9,50), de €5 op 0 is een push (€5). Samen <strong>{ah(0.25, 0, 1.90)}</strong>: halve winst.</li><li>Go Ahead verliest: <strong>{ah(0.25, -1, 1.90)}</strong>.</li></ul>
<p><strong>Voorbeeld 5: Ajax −1,25 (odd 2,05, inzet €10)</strong></p>
<ul><li>Ajax wint met 2 of meer verschil: <strong>{ah(-1.25, 2, 2.05)}</strong>.</li><li>Ajax wint met 1 verschil: de €5 op −1 is een push, de €5 op −1,5 verliest. Je krijgt <strong>{ah(-1.25, 1, 2.05)}</strong>: half verlies.</li><li>Gelijkspel of verlies: <strong>{ah(-1.25, 0, 2.05)}</strong>.</li></ul>
<p><em>De teams en quoteringen in deze voorbeelden zijn fictief en alleen bedoeld om de berekening te laten zien.</em></p>
<h3><strong>Wat is Asian totaal (Asian over/under)?</strong></h3>
<p>Asian totaal werkt precies zoals de Asian handicap, maar dan op het <strong>totaal aantal doelpunten</strong> in de wedstrijd. Je kiest meer dan (over) of minder dan (under) een lijn. Bij een gewone over/under is de lijn altijd een halve, zoals 2,5. Bij Asian totaal heb je ook hele lijnen en kwartlijnen:</p>
<ul><li><strong>Halve lijn (2,5):</strong> winst of verlies, net als bij een gewone over/under.</li><li><strong>Hele lijn (2 of 3):</strong> valt het aantal doelpunten precies op de lijn, dan krijg je je inzet terug. €10 op meer dan 2 (odd 1,80) bij precies 2 doelpunten levert <strong>{tot(2, 2, 1.80)}</strong> terug.</li><li><strong>Kwartlijn (2,25 of 2,75):</strong> je inzet wordt verdeeld over de twee lijnen ernaast, dus 2,25 is de helft op 2 en de helft op 2,5.</li></ul>
{figuur(AT_IMG, "Asian totaal tabel: per lijn van 1,5 tot 3,5 voor meer dan en minder dan, en per aantal doelpunten (0 tot 5+) of je wint, half wint, je inzet terugkrijgt, half verliest of verliest", "Asian totaal tabel: kies je lijn (rij) en kijk hoeveel doelpunten er vallen (kolom)")}
{pdf_link(AT_PDF, "Download de Asian totaal tabel als pdf (A4)")}
{figuur(VB_AT, "Rekenvoorbeeld Asian totaal: 10 euro op meer dan 2,25 doelpunten tegen odd 1,85. 0 of 1 doelpunt: 0 euro. Precies 2 doelpunten: half verlies, 5 euro. 3 of meer doelpunten: 18,50 euro", "Rekenvoorbeeld: €10 op meer dan 2,25 doelpunten, verdeeld over meer dan 2 en meer dan 2,5")}
<p><strong>Voorbeeld: meer dan 2,75 doelpunten (odd 1,95, inzet €10)</strong></p>
<ul><li>2 doelpunten of minder: <strong>{tot(2.75, 2, 1.95)}</strong>.</li><li>Precies 3 doelpunten: de €5 op meer dan 2,5 wint (€9,75), de €5 op meer dan 3 is een push (€5). Samen <strong>{tot(2.75, 3, 1.95)}</strong>: halve winst.</li><li>4 doelpunten of meer: <strong>{tot(2.75, 4, 1.95)}</strong>.</li></ul>
<p><strong>Voorbeeld: minder dan 2,25 doelpunten (odd 1,95, inzet €10)</strong></p>
<ul><li>0 of 1 doelpunt: <strong>{tot(2.25, 1, 1.95, False)}</strong>.</li><li>Precies 2 doelpunten: de €5 op minder dan 2 is een push, de €5 op minder dan 2,5 wint. Samen <strong>{tot(2.25, 2, 1.95, False)}</strong>: halve winst.</li><li>3 doelpunten of meer: <strong>{tot(2.25, 3, 1.95, False)}</strong>.</li></ul>
<p>Wil je weten hoe vaak wedstrijden in een competitie boven de 2,5 doelpunten uitkomen? Bekijk dan onze <a href="/wedtips/over-2-5-goals-tips-voorspellingen">over 2,5 goals tips</a> en <a href="/wedtips/btts-tips-voorspellingen">BTTS-tips</a>.</p>
<h3><strong>Asian handicap of Europese handicap: wat is het verschil?</strong></h3>
{tabel(["", "Asian handicap", "Europese handicap"], [
    ("<strong>Uitkomsten</strong>", "Twee: jouw team of de tegenstander", "Drie: thuis, handicap-gelijkspel of uit"),
    ("<strong>Lijnen</strong>", "Hele, halve en kwartlijnen (−0,25, −0,5, −1, ...)", "Alleen hele getallen (−1, −2, +1, ...)"),
    ("<strong>Virtueel gelijkspel</strong>", "Inzet (deels) terug", "Aparte uitkomst waarop je kunt inzetten"),
    ("<strong>Halve winst of half verlies</strong>", "Ja, bij kwartlijnen", "Nee"),
    ("<strong>Quoteringen</strong>", "Meestal rond 1,90 aan beide kanten", "Drie quoteringen, vaak met een hogere marge"),
])}
<p>Bij een Europese handicap −1 verlies je als je team met precies 1 verschil wint, omdat dan de uitkomst "handicap-gelijkspel" valt. Bij een Asian handicap −1 krijg je in die situatie je inzet terug. Lees meer over <a href="/nieuws/wat-een-europese-handicap-weddenschap">de Europese handicap</a> en over <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">alle soorten handicap wedden</a>.</p>"""

content3 = f"""<h3><strong>Waarom kiezen wedders voor een Asian handicap?</strong></h3>
<ul><li><strong>Betere quoteringen op favorieten:</strong> in plaats van een odd van 1,25 op een thuiszege krijg je op −1,5 al snel een odd rond 1,90.</li><li><strong>Minder risico:</strong> met hele lijnen en kwartlijnen ben je bij een krappe uitslag niet meteen je hele inzet kwijt.</li><li><strong>Geen gelijkspel:</strong> je kiest een van de twee kanten, wat het overzichtelijk maakt.</li><li><strong>Lage marge:</strong> bookmakers rekenen op Asian lines vaak een kleinere marge dan op 1X2, waardoor je per weddenschap meer terugkrijgt.</li></ul>
<h3><strong>Tips en valkuilen bij Asian handicap</strong></h3>
<ul><li><strong>Begin met halve en hele lijnen.</strong> Die zijn het makkelijkst te begrijpen. Stap pas over op kwartlijnen als je de split snapt.</li><li><strong>Let op de schrijfwijze.</strong> −0,75 kan ook als −0,5/−1 op je scherm staan. Kijk altijd bij welk team het min-teken staat.</li><li><strong>Alleen de reguliere speeltijd telt.</strong> Verlenging en strafschoppen tellen bij een Asian handicap niet mee, blessuretijd wel.</li><li><strong>Check de regels bij live wedden.</strong> Bij veel bookmakers telt bij een live Asian handicap alleen wat er na het plaatsen van je weddenschap gebeurt, de stand op dat moment wordt dan als 0-0 gezien. Lees de voorwaarden van jouw bookmaker.</li><li><strong>Vergelijk quoteringen.</strong> Een verschil van 1,86 of 1,95 lijkt klein, maar tikt op lange termijn flink aan. Gebruik onze <a href="/odds-vergelijken-bij-alle-bookmakers-beste-odds-vandaag">odds vergelijker</a>.</li><li><strong>Zet nooit meer in dan je kunt missen.</strong> Ook met een handicap blijft wedden een kansspel.</li></ul>
<h3><strong>Mag je in Nederland wedden op een Asian handicap?</strong></h3>
<p>Ja. Wedden op een Asian handicap of een Asian totaal is in Nederland toegestaan bij bookmakers met een vergunning van de Kansspelautoriteit. Het gaat om de uitslag of het aantal doelpunten, en die markten staan niet op de lijst van verboden weddenschappen (zoals corners en kaarten). Niet elke legale bookmaker biedt alle kwartlijnen aan: soms vind je ze onder namen als "Aziatische handicap", "Asian lines" of "handicap (2-weg)". Lees ook <a href="/nieuws/dit-is-waarom-wedden-op-corners-niet-meer-legaal-is-in-nederland">waarom wedden op corners niet legaal is</a>.</p>
<p>Legale bookmakers die wij aanraden:</p>
{aanraders()}
<h3><strong>Veelgestelde vragen over Asian handicap</strong></h3>
<p><strong>Wat is een Asian handicap in het kort?</strong><br>Een weddenschap met twee uitkomsten waarbij een team een virtuele voor- of achterstand krijgt. Een gelijkspel bestaat niet: bij hele lijnen krijg je dan je inzet terug en bij kwartlijnen win of verlies je de helft.</p>
<p><strong>Wat betekent Asian handicap 0?</strong><br>Asian handicap 0 heet ook draw no bet. Wint je team, dan win je. Wordt het gelijk, dan krijg je je inzet terug. Verliest je team, dan verlies je.</p>
<p><strong>Wat betekent −0,5 en +0,5?</strong><br>−0,5 betekent dat je team moet winnen, net als een gewone 1 of 2 in 1X2. +0,5 betekent dat je team mag winnen of gelijkspelen, net als dubbele kans.</p>
<p><strong>Wat betekent halve winst?</strong><br>De helft van je inzet wint tegen de quotering en de andere helft krijg je terug. Met €10 tegen odd 1,90 krijg je dan €14,50 terug.</p>
<p><strong>Wat betekent half verlies?</strong><br>De helft van je inzet is verloren en de andere helft krijg je terug. Met €10 krijg je dan €5 terug, ongeacht de quotering.</p>
<p><strong>Wat is het verschil tussen Asian handicap en Asian totaal?</strong><br>Bij de Asian handicap draait het om het doelsaldo tussen twee teams. Bij Asian totaal draait het om het totaal aantal doelpunten in de wedstrijd. De rekenregels voor hele lijnen en kwartlijnen zijn hetzelfde.</p>
<p><strong>Telt de verlenging mee bij een Asian handicap?</strong><br>Nee. Een Asian handicap gaat over de reguliere speeltijd inclusief blessuretijd. Verlenging en strafschoppen tellen niet mee, tenzij de bookmaker dat bij de markt anders vermeldt.</p>
<p><strong>Is Asian handicap beter dan een Europese handicap?</strong><br>Niet per se beter, wel flexibeler. De Asian handicap geeft je meer lijnen en bescherming bij een virtueel gelijkspel. De Europese handicap geeft vaak hogere quoteringen, maar met meer risico.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    from datetime import datetime, timezone
    fd = {"name": TITEL, "content": content, "content-2": content2, "content-3": content3, "samenvatting": SAMENVATTING,
          "rubriek": "6502b66cd9992658b4037cf5", "publicatiedatum": datetime.now(timezone.utc).isoformat(),
          "afbeelding": {"url": OG, "alt": "Wat is een Asian Handicap? Uitleg met tabel"},
          "seo-afbeelding": {"url": OG, "alt": "Wat is een Asian Handicap? Uitleg met tabel"}}
    tekst = re.sub(r"<[^>]+>", " ", content + content2 + content3)
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", len(tekst.split()), "woorden")
    assert not re.search(r"<(ul|ol|/li)>\s+<", content + content2 + content3) and "/kennisbank/" not in content + content2 + content3
    if "--live" in sys.argv:
        print(WF.update_live(ITEM_ID, fd).get("lastPublished"))
