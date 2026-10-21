# -*- coding: utf-8 -*-
"""Herschrijving (bestaand item 65956fedef67b2cebc306708): Hoe weet ik of een bookmaker legaal is in Nederland?
Feiten: zie legaal_data.py + Bijlage 2 Regeling kansspelen op afstand (verboden weddenschappen), art. 4.9 Besluit,
Ksa 26-03-2026 (grenzen sportvergunning), Besluit ongerichte reclame (sportsponsoring verboden per 1-7-2025).
  python3 specials/bookmaker_legaal.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lk_webflow as WF
from legaal_data import tabel, merken_tabel, aanraders, KANSSPELWIJZER, PEILDATUM

ITEM_ID = "65956fedef67b2cebc306708"
TITEL = "Hoe weet ik of een bookmaker legaal is in Nederland? Zo check je het in 1 minuut"
SAMENVATTING = ("Hoe herken je een legale bookmaker in Nederland? Zo check je de vergunning, dit zijn alle legale "
                "wedsites en hierop mag je niet wedden.")
KSA_LOGO = "https://uploads-ssl.webflow.com/64f9f8e867f73b8e88841e09/65956eac6515a6ce0aac9e40_keurmerk-kansspelautoriteit.jpg"

content = f"""<p><strong>Een bookmaker is legaal in Nederland als hij een vergunning heeft van de Kansspelautoriteit (Ksa). Dat check je in een minuut in de Kansspelwijzer op de website van de Ksa: staat de wedsite of app daar niet in, dan is hij illegaal. Op dit moment hebben 25 aanbieders een vergunning voor online sportweddenschappen, waaronder TOTO, BetCity, Unibet, bet365, JACKS.NL, Bingoal, 711, Circus en BetMGM.</strong></p>
<p>Een Nederlandstalige website, iDEAL als betaalmethode of een .nl-adres zeggen niet genoeg: ook illegale sites en nepkopieën gebruiken die. In dit artikel lees je stap voor stap hoe je een legale bookmaker herkent, welke wedsites op dit moment een vergunning hebben (stand {PEILDATUM}), op welke gebeurtenissen je in Nederland niet mag wedden en wat de risico's zijn van een illegale bookmaker.</p>
<h3><strong>Zo check je in 4 stappen of een bookmaker legaal is</strong></h3>
<p><strong>1. Zoek de bookmaker op in de Kansspelwijzer</strong><br>Ga naar de <a href="{KANSSPELWIJZER}" target="_blank" rel="noopener">Kansspelwijzer van de Kansspelautoriteit</a> en zoek op de naam van de website of app. Je ziet dan welk bedrijf de vergunning heeft, tot wanneer die geldt en waarvoor: casino, sportweddenschappen, poker of paardenrennen. Dit is de enige officiële check.</p>
<p><strong>2. Klik op het Ksa-logo onderaan de site</strong><br>Een legale bookmaker moet informatie over zijn vergunning tonen en linken naar de website van de Ksa. De meeste doen dat met het Ksa-logo onderaan de pagina. Klik erop: een echt logo linkt door naar de Kansspelautoriteit. Een plaatje zonder link of een logo dat ergens anders heen gaat, is een rode vlag. Partijen zonder vergunning mogen het logo niet gebruiken.</p>
<figure class="w-richtext-align-center w-richtext-figure-type-image"><div><img src="{KSA_LOGO}" alt="Logo van de Kansspelautoriteit dat legale bookmakers onderaan hun website tonen" loading="lazy"></div><figcaption>Het logo van de Kansspelautoriteit: alleen legale aanbieders mogen het gebruiken.</figcaption></figure>
<p><strong>3. Let op bij het aanmaken van een account</strong><br>Een legale bookmaker vraagt altijd naar je identiteit, controleert of je 18 jaar of ouder bent en checkt of je in het Cruks-register staat. Ook moet je vóór je eerste weddenschap zelf limieten instellen voor je stortingen, je speeltijd en je saldo. Kun je zonder die stappen meteen wedden, dan heb je met een illegale site te maken.</p>
<p><strong>4. Check het exacte webadres</strong><br>Oplichters maken kopieën van legale wedsites, bijvoorbeeld op een .co.nl-adres. De Ksa liet in 2026 tientallen van die nepsites offline halen. Kijk dus goed of het adres precies overeenkomt met de website in de Kansspelwijzer, en ga bij twijfel via een betrouwbare link naar de site.</p>
<h3><strong>Welke bookmakers zijn legaal in Nederland?</strong></h3>
<p>Deze aanbieders hebben op {PEILDATUM} een vergunning voor online sportweddenschappen. Klik op een naam voor onze review.</p>
{merken_tabel(filter_prod="S")}
<p><em>Bron: Kansspelwijzer van de Kansspelautoriteit. De vergunning geldt voor de genoemde onderdelen; niet elk merk biedt ze in de praktijk allemaal aan. Een volledig overzicht inclusief casino's die alleen casinospellen aanbieden, vind je in ons artikel over <a href="/nieuws/dit-zijn-de-casinos-die-op-dit-moment-legaal-zijn-in-nederland">legale casino's in Nederland</a>.</em></p>
<p><strong>Onze aanraders:</strong></p>
{aanraders()}
<p>Bekijk alle bookmakers met onze beoordeling op de pagina <a href="/bookmakers">bookmakers</a>.</p>"""

content2 = f"""<h3><strong>Kenmerken van een legale bookmaker</strong></h3>
{tabel(["Legale bookmaker", "Illegale bookmaker"], [
    ("Staat in de Kansspelwijzer van de Ksa", "Staat niet in de Kansspelwijzer"),
    ("Ksa-logo dat doorlinkt naar de Kansspelautoriteit", "Geen logo, of een logo zonder werkende link"),
    ("Cruks-, leeftijds- en identiteitscheck bij inschrijving", "Inschrijven zonder controles"),
    ("Verplichte limieten en een netto stortingslimiet", "Vaak 'zonder limiet' of 'zonder Cruks'"),
    ("Betalen via een bank of betaaldienst met EU-vergunning", "Vaak alleen crypto of vage betaalmethoden"),
    ("Bonussen met duidelijke voorwaarden", "Ongeloofwaardige bonussen zonder voorwaarden"),
    ("Nederlands recht en gratis klantenservice", "Geen Nederlandse klantenservice of klachtenregeling"),
    ("Geen weddenschappen op kaarten of corners", "Wedden op alles, ook op verboden gebeurtenissen"),
])}
<p>Let op: iDEAL en een .nl-adres zijn geen bewijs. Ze zijn gangbaar bij legale aanbieders, maar niet wettelijk verplicht, en illegale sites gebruiken ze soms ook.</p>
<h3><strong>Waarop mag je niet wedden in Nederland?</strong></h3>
<p>Een legale bookmaker mag lang niet alles aanbieden. Om matchfixing en manipulatie tegen te gaan, zijn weddenschappen op een aantal gebeurtenissen verboden. Biedt een wedsite die wel aan, dan is dat een duidelijk signaal dat hij niet onder Nederlands toezicht staat.</p>
<ul><li><strong>Verboden gebeurtenissen in het voetbal:</strong> gele en rode kaarten, hoekschoppen, inworpen, overtredingen, strafschoppen veroorzaken of nemen, buitenspel, wissels, blessurebehandelingen, de extra tijd die de vierde official aangeeft, VAR-momenten en juichgedrag. Lees meer in ons artikel over <a href="/nieuws/dit-is-waarom-wedden-op-corners-niet-meer-legaal-is-in-nederland">waarom wedden op corners niet meer mag</a>.</li><li><strong>Verboden wedstrijden:</strong> jeugdwedstrijden en alle wedstrijden voor spelers onder 21 jaar, voetbal in de derde divisie en lager, en wedstrijden met alleen onbetaalde sporters.</li><li><strong>Tennis:</strong> geen weddenschappen op dubbele fouten, challenges of straffen van de scheidsrechter.</li><li><strong>Buiten de sport:</strong> geen weddenschappen op prijsverkiezingen zoals een MVP-titel, op transfers of op politieke verkiezingen.</li></ul>
<p>Wedden op de uitslag, doelpunten, doelpuntenmakers of <a href="/nieuws/dit-is-hoe-wedden-op-schoten-op-doel-werkt">schoten op doel</a> mag wel.</p>
<h3><strong>Sinds juli 2025 geen gokreclame meer bij sportclubs</strong></h3>
<p>Sinds 1 juli 2023 mogen online gokbedrijven geen reclame meer maken op tv, radio, in print of in de openbare ruimte. Online reclame mag alleen als vrijwel het hele publiek 24 jaar of ouder is. Sinds 1 juli 2025 is ook sportsponsoring verboden, dus geen bookmakerlogo's meer op shirts en reclameborden. Zie je toch nog opvallend veel gokreclame van een onbekende wedsite, bijvoorbeeld via influencers op sociale media, dan is dat vaak een illegale partij.</p>
<h3><strong>Wat zijn de risico's van een illegale bookmaker?</strong></h3>
<ul><li><strong>Geen bescherming:</strong> geen toezicht, geen limieten en geen Cruks-check.</li><li><strong>Geen garantie op uitbetaling:</strong> win je, dan is er niemand die ervoor zorgt dat je je geld krijgt.</li><li><strong>Je gegevens zijn niet veilig:</strong> identiteitsbewijzen en bankgegevens komen bij partijen zonder toezicht terecht.</li><li><strong>Strafbaar:</strong> wedden bij een aanbieder waarvan je weet dat hij geen vergunning heeft, is volgens de Wet op de kansspelen strafbaar, met een boete tot €11.000.</li><li><strong>Verlies niet terug te halen:</strong> de Hoge Raad oordeelde op 3 juli 2026 dat een overeenkomst met een illegale aanbieder niet nietig is. Je verlies terugvorderen op die grond lukt dus niet.</li><li><strong>Zelf belasting betalen:</strong> bij een illegale online aanbieder moet je zelf kansspelbelasting aangeven als je in een maand meer wint dan inzet. Bij een legale bookmaker regelt de aanbieder dat.</li></ul>
<p>De Kansspelautoriteit pakt illegale aanbieders steeds harder aan. De hoogste boete tot nu toe was €24,8 miljoen voor het bedrijf achter Qbet en 55Bet (maart 2026), en sinds juli 2026 begint een boete voor illegaal aanbod bij €800.000.</p>"""

content3 = f"""<h3><strong>Wat verandert er voor bookmakers?</strong></h3>
<p>In september 2026 kregen de eerste aanbieders een vervolgvergunning tot 2031, onder wie TOTO, BetCity, Bingoal en bet365. De komende tijd lopen meer vergunningen af en moeten aanbieders opnieuw aantonen dat ze aan de regels voldoen. Daarnaast wil het kabinet een reclameverbod, een bonusverbod, één stortingslimiet voor alle aanbieders samen en het blokkeren van illegale websites. Die plannen worden uitgewerkt in een wetsvoorstel; de ingangsdatum is nog niet bekend. Meer over de huidige limieten lees je in ons artikel over de <a href="/nieuws/netto-stortingslimiet">netto stortingslimiet</a>.</p>
<h3><strong>Verantwoord wedden</strong></h3>
<p>Ook bij een legale bookmaker is wedden geen manier om geld te verdienen. Bepaal vooraf je budget, stel je limieten bewust laag in en wed nooit om verlies terug te winnen. Merk je dat het gokken je te veel kost, schrijf je dan in bij <a href="/nieuws/cruks-de-gokstop-voor-verantwoord-gokken">Cruks</a> of bel gratis en anoniem met Open over Gokken via 0800 24 000 22. Meer tips lees je op onze pagina over <a href="/speel-bewust/verantwoord-wedden">verantwoord wedden</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe weet ik of een bookmaker legaal is?</strong><br>Zoek de website of app op in de Kansspelwijzer van de Kansspelautoriteit. Staat hij erin met een vergunning voor sportweddenschappen, dan is hij legaal. Zo niet, dan is het een illegale bookmaker.</p>
<p><strong>Hoeveel legale bookmakers zijn er in Nederland?</strong><br>Op {PEILDATUM} hebben 25 aanbieders een vergunning voor online sportweddenschappen.</p>
<p><strong>Is iDEAL een bewijs dat een bookmaker legaal is?</strong><br>Nee. iDEAL is gangbaar bij legale aanbieders, maar niet wettelijk verplicht en zegt op zichzelf niets over de vergunning.</p>
<p><strong>Is een bookmaker met een .nl-adres altijd legaal?</strong><br>Nee. Oplichters maken nepkopieën van legale sites, bijvoorbeeld op .co.nl-adressen. Check altijd het exacte adres in de Kansspelwijzer.</p>
<p><strong>Waarom kan ik niet wedden op gele kaarten of corners?</strong><br>Omdat die gebeurtenissen makkelijk te manipuleren zijn. Ze zijn bij Nederlandse legale aanbieders verboden, net als bijvoorbeeld inworpen, overtredingen en buitenspel.</p>
<p><strong>Is wedden bij een buitenlandse bookmaker strafbaar?</strong><br>Wedden bij een aanbieder zonder Nederlandse vergunning is volgens de wet strafbaar, met een boete tot €11.000. Bovendien heb je er geen bescherming en geen garantie op uitbetaling.</p>
<p><strong>Moet ik belasting betalen over mijn winst bij een bookmaker?</strong><br>Niet bij een legale bookmaker; die betaalt de kansspelbelasting. Bij een illegale online aanbieder moet je zelf aangifte doen.</p>
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
