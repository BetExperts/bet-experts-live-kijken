# -*- coding: utf-8 -*-
"""Herschrijving (bestaand item 67876b950bcd0ee61929a5e4): Wat zijn Opta-gegevens? Alles over schoten op doel en Unibet.
Feiten (schoten_facts 21-10-2026): The Analyst-glossary, Stats Perform (xGOT, FAQ), SVG 1-6-2026 (30 jaar Opta, 13.000
datapunten, Opta Vision 3,8 mln, 3.900+ competities), Wikipedia (1996/2013/2019), iGB 12-01-2026 (FIFA), FBref-stop 20-01-2026,
TOTO Nadere regels (23-09-2026), Kambi Rules v2.2 NL (Unibet). GSC: 'opta gegevens unibet', 'optagegevens', 'wat zijn opta gegevens'.
  python3 specials/opta_gegevens.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lk_webflow as WF
from legaal_data import tabel, aanraders

ITEM_ID = "67876b950bcd0ee61929a5e4"
TITEL = "Wat zijn Opta-gegevens? Alles over schoten op doel en Unibet-weddenschappen"
SAMENVATTING = ("Opta-gegevens zijn de officiële sportstatistieken waarmee Unibet en TOTO weddenschappen op schoten op doel "
                "afhandelen. Zo werkt het.")
S = "https://www.bet-experts.nl/be-static/"

content = f"""<p><strong>Opta-gegevens zijn sportstatistieken van Opta, een van de grootste sportdatabedrijven ter wereld en onderdeel van Stats Perform. Opta legt bij elke wedstrijd duizenden gebeurtenissen vast, zoals schoten, schoten op doel, reddingen en assists. Bookmakers als Unibet en TOTO gebruiken die data om weddenschappen op bijvoorbeeld schoten op doel af te handelen. Zie je bij Unibet "Volgens Opta-gegevens" achter een markt staan, dan betekent dat: de telling van Opta is leidend, ook als een tv-zender of website een ander aantal laat zien.</strong></p>
<p>Wie op spelersstatistieken wedt, komt Opta overal tegen. Maar wat zijn Opta-gegevens (of optagegevens) precies, hoe komen ze tot stand en wat telt volgens Opta als schot op doel? In dit artikel lees je alles over Opta, de definities die voor je weddenschap het verschil maken en hoe Unibet en TOTO de data gebruiken.</p>
<h3><strong>Wat is Opta?</strong></h3>
<p>Opta werd in 1996 in Engeland opgericht als Opta Index, om wedstrijden in de Premier League te analyseren. In het begin werden per wedstrijd zo'n 50 tot 60 gebeurtenissen met de hand vastgelegd, op basis van videobanden. Inmiddels is Opta uitgegroeid tot een wereldwijde standaard voor sportdata.</p>
{tabel(["Jaar", "Mijlpaal"], [
    ("1996", "Opta Index wordt opgericht en levert statistieken van de Premier League"),
    ("2013", "Overname door Perform Group"),
    ("2019", "Perform en het Amerikaanse STATS gaan samen verder als Stats Perform, met Opta als databrand"),
    ("2021", "Lancering van The Analyst, het publieksplatform met Opta-analyses"),
    ("januari 2026", "Opta wordt officiële leverancier van de spelersstatistieken van de FIFA aan bookmakers, onder meer voor het WK 2026"),
    ("2026", "Opta bestaat 30 jaar en levert data van meer dan 3.900 competities in ruim 20 sporten"),
])}
<h3><strong>Hoe verzamelt Opta zijn gegevens?</strong></h3>
<p>Bij een wedstrijd volgen analisten live elke actie op het veld en leggen die vast in het systeem van Opta: wie de bal speelt, waar, met welk lichaamsdeel en met welk resultaat. Na afloop worden de gegevens gecontroleerd en waar nodig gecorrigeerd. Volgens Stats Perform gaat het om zo'n 13.000 datapunten per wedstrijd die live worden vastgelegd. Met Opta Vision, waarbij ook beelden automatisch worden geanalyseerd, komen daar nog miljoenen trackinggegevens bij.</p>
<p>Omdat iedere analist met dezelfde vaste definities werkt, zijn de cijfers vergelijkbaar tussen wedstrijden, competities en seizoenen. Precies dat maakt Opta-data geschikt om weddenschappen eerlijk en eenduidig af te handelen.</p>"""

content2 = f"""<h3><strong>Wat is een schot op doel volgens Opta?</strong></h3>
<p>Voor wedders is dit de belangrijkste definitie. Opta deelt elke bewuste doelpoging in een van deze categorieën in:</p>
<figure class="w-richtext-align-fullwidth w-richtext-figure-type-image" style="max-width:100%"><div><img src="{S}schoten-opta-schema-3f979b39.webp" alt="Zo registreert Opta een schot: doelpunt en op doel gestopt tellen als schot op doel, naast en geblokt niet" loading="lazy"></div><figcaption>Zo deelt Opta een doelpoging in</figcaption></figure>
{tabel(["Opta-begrip", "Betekenis", "Telt als schot op doel?"], [
    ("<strong>Goal</strong>", "Een doelpunt, ook via paal, lat of een verdediger", "Ja"),
    ("<strong>Shot on target</strong>", "Een poging op doel die de keeper stopt, of die de laatste man van de lijn haalt", "Ja"),
    ("<strong>Shot off target</strong>", "Naast of over, of tegen paal of lat zonder doelpunt", "Nee"),
    ("<strong>Blocked shot</strong>", "Geblokt door een speler die nog verdedigers of de keeper achter zich heeft", "Nee"),
    ("<strong>Hit woodwork</strong>", "De bal raakt paal of lat en gaat er niet direct in", "Nee"),
])}
<p>Belangrijk om te weten:</p>
<ul><li><strong>Een kopbal is een gewoon schot.</strong> Opta registreert alleen met welk lichaamsdeel er geschoten is; een kopbal op doel telt dus net zo goed als een schot op doel.</li><li><strong>Een penalty is een doelpoging.</strong> Gaat hij erin of stopt de keeper hem, dan is het een schot op doel. Volgens Opta is een penalty bovendien altijd een "big chance".</li><li><strong>Eigen doelpunten tellen niet als schot.</strong> Opta schrijft een eigen doelpunt toe aan de verdediger die het maakt; het telt niet mee bij de schoten van de aanvaller.</li><li><strong>Het moet een bewuste doelpoging zijn.</strong> Een voorzet die toevallig op doel komt en door de keeper wordt gevangen, telt niet.</li></ul>
<h3><strong>Andere Opta-begrippen die je tegenkomt</strong></h3>
{tabel(["Begrip", "Uitleg"], [
    ("Big chance", "Een kans waarbij een speler redelijkerwijs zou moeten scoren, zoals een één-op-één of een penalty"),
    ("Expected goals (xG)", "De kans dat een schot een doelpunt wordt, op een schaal van 0 tot 1, gebaseerd op bijna een miljoen historische schoten"),
    ("Expected goals on target (xGOT)", "Kijkt na het schot naar de uitvoering en plaatsing; alleen voor schoten op doel. Handig om keepers te beoordelen"),
    ("Shooting accuracy", "Het percentage schoten dat op doel is (geblokte schoten tellen hier niet mee)"),
    ("Shot conversion", "Het percentage schoten dat een doelpunt wordt"),
])}
<h3><strong>Hoe gebruikt Unibet Opta-gegevens?</strong></h3>
<p>Unibet draait op het sportsbook van Kambi. Bij spelers- en teamstatistieken staat bij Unibet letterlijk "Volgens Opta-gegevens" in de naam van de markt. Voorbeelden:</p>
<ul><li>Schoten van speler op doel (Volgens Opta-gegevens)</li><li>Totaal aantal schoten op doel (Volgens Opta-gegevens)</li><li>Totaal aantal schoten op doel door een team (Volgens Opta-gegevens)</li><li>Reddingen keeper (Volgens Opta-gegevens)</li><li>Geeft een assist (Volgens Opta-gegevens)</li></ul>
<p>Die markten worden afgehandeld op de telling van Opta. Verder gelden de algemene voorwaarden van het sportsbook (versie 2.2, september 2026):</p>
<ul><li><strong>Alleen de reguliere speeltijd telt:</strong> 90 minuten inclusief blessuretijd. Verlenging en strafschoppenseries tellen niet mee.</li><li><strong>Speler vanaf de aftrap:</strong> volgens de voorwaarden zijn weddenschappen op de prestaties van een speler in één wedstrijd alleen geldig als hij vanaf de aftrap speelt. Speelt hij niet, dan krijg je je inzet terug.</li><li><strong>Eigen doelpunten tellen niet</strong> mee bij spelersweddenschappen.</li><li><strong>Bet builder:</strong> is één selectie ongeldig, dan vervalt de hele bet builder en krijg je je inzet terug.</li></ul>
<p>Hetzelfde Kambi-sportsbook, met dezelfde Opta-markten, vind je ook bij LeoVegas, JACKS.NL en Oranje Palace.</p>
<h3><strong>En bij TOTO?</strong></h3>
<p>Ook TOTO handelt schoten en schoten op doel af op basis van Opta. In de wedregels (geldig vanaf 23 september 2026) staat dat de definitief vastgestelde data van Opta na afloop van de wedstrijd leidend is, en dat andere bronnen worden uitgesloten. Een belangrijk verschil met Unibet: bij TOTO blijft een weddenschap op een speler staan als hij invalt. Alleen als hij helemaal niet speelt, is de weddenschap ongeldig. TOTO biedt naast schoten op doel ook de markt "schoten" aan, waarbij ook pogingen naast, tegen de paal en geblokt meetellen.</p>"""

content3 = f"""<h3><strong>Waar kun je Opta-gegevens zelf bekijken?</strong></h3>
<ul><li><strong>The Analyst (theanalyst.com):</strong> het eigen platform van Opta, met analyses, rankings en uitleg van alle definities.</li><li><strong>Statistieken-apps die Opta-data gebruiken,</strong> zoals FotMob, waar je per speler en per wedstrijd de schoten en schoten op doel ziet.</li></ul>
<p>Let op: de bekende statistiekensite FBref heeft sinds januari 2026 geen geavanceerde Opta-data meer. Kijk je daar, dan kunnen de cijfers afwijken van de telling waarmee je bookmaker afrekent. Ook tv-zenders en andere apps gebruiken soms een andere bron. Voor je weddenschap telt alleen de bron die je bookmaker noemt.</p>
<h3><strong>Wat als je het niet eens bent met de Opta-telling?</strong></h3>
<p>Het komt voor dat je een schot op doel anders beoordeelt dan Opta, bijvoorbeeld bij een afgebogen bal of een redding op de lijn. Bookmakers rekenen af op de definitieve Opta-data na afloop van de wedstrijd, en die is leidend. Opta controleert zijn eigen data na de wedstrijd; daardoor kan een live getoond aantal soms nog veranderen. Denk je dat een weddenschap verkeerd is afgehandeld, neem dan contact op met de klantenservice van je bookmaker. Legale bookmakers moeten een klachtenregeling hebben en klachten binnen acht weken behandelen.</p>
<h3><strong>Rekenvoorbeeld</strong></h3>
<p>Stel, je wedt bij Unibet op "Speler X meer dan 0,5 schoten op doel" (1+). In de wedstrijd schiet hij één keer tegen de lat en één keer tegen een verdediger die nog een ploeggenoot achter zich heeft. Volgens Opta zijn dat twee schoten, maar nul schoten op doel: je weddenschap is verloren. Had de verdediger de bal van de doellijn gehaald terwijl de keeper al was gepasseerd, dan was het wél een schot op doel geweest.</p>
<p>Meer voorbeelden, de markten 1+, 2+ en 3+, statistieken per competitie en tips lees je in ons artikel <a href="/nieuws/dit-is-hoe-wedden-op-schoten-op-doel-werkt">zo werkt wedden op schoten op doel</a>.</p>
<h3><strong>Wedden op schoten op doel</strong></h3>
<p>Schoten op doel zijn in Nederland legaal om op te wedden, in tegenstelling tot bijvoorbeeld corners en kaarten (lees <a href="/nieuws/dit-is-waarom-wedden-op-corners-niet-meer-legaal-is-in-nederland">waarom wedden op corners niet mag</a>). Je vindt de markten onder meer bij <a href="/bookmakers/unibet">Unibet</a>, <a href="/bookmakers/toto">TOTO</a>, <a href="/bookmakers/leovegas">LeoVegas</a> en <a href="/bookmakers/jacks-nl">JACKS.NL</a>. Onze aanraders:</p>
{aanraders()}
<h3><strong>Veelgestelde vragen over Opta-gegevens</strong></h3>
<p><strong>Wat zijn Opta-gegevens?</strong><br>Sportstatistieken van Opta, onderdeel van Stats Perform. Opta legt per wedstrijd duizenden gebeurtenissen vast, zoals schoten, schoten op doel, reddingen en assists, volgens vaste definities.</p>
<p><strong>Wat betekent "Volgens Opta-gegevens" bij Unibet?</strong><br>Dat de weddenschap wordt afgehandeld op basis van de telling van Opta. Wijkt een tv-zender of andere app af, dan telt toch het Opta-cijfer.</p>
<p><strong>Telt een schot op de paal als schot op doel volgens Opta?</strong><br>Nee, tenzij de bal daarna direct in het doel gaat. Een schot op de paal of lat telt bij Opta als schot naast doel.</p>
<p><strong>Telt een geblokt schot als schot op doel?</strong><br>Nee, behalve als de speler die blokt de laatste man is en de bal anders in het doel was gegaan, zoals bij een redding op de doellijn.</p>
<p><strong>Gebruikt TOTO ook Opta?</strong><br>Ja. TOTO handelt schoten en schoten op doel af op basis van de definitieve Opta-data na afloop van de wedstrijd.</p>
<p><strong>Wat gebeurt er bij Unibet als mijn speler niet start?</strong><br>Volgens de sportsbookvoorwaarden moeten spelers voor spelersweddenschappen in één wedstrijd vanaf de aftrap spelen. Speelt de speler niet, dan krijg je je inzet terug. Check daarom vóór je inzet de opstelling.</p>
<p><strong>Waar kan ik Opta-statistieken bekijken?</strong><br>Op The Analyst, het platform van Opta zelf, en in apps die Opta-data gebruiken, zoals FotMob.</p>
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
