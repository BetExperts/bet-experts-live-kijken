# -*- coding: utf-8 -*-
"""Herschrijving (bestaand item 667295019c5a3c5080449881): Waarom wedden op corners niet meer legaal is in Nederland.
Feiten: art. 4.9 Besluit kansspelen op afstand, art. 3.15 en Bijlage 2 Regeling kansspelen op afstand (BWBR0044767),
Ksa 26-03-2026 (grenzen sportvergunning), Ksa-waarschuwing aan een aanbieder 16-07-2026 (corners/inworpen live tijdens WK),
Wok art. 1/36a, legaal_data.py (25 sportvergunningen, stand 21-10-2026).
  python3 specials/corners_niet_legaal.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lk_webflow as WF
from legaal_data import tabel, aanraders, KANSSPELWIJZER

ITEM_ID = "667295019c5a3c5080449881"
TITEL = "Waarom wedden op corners niet meer legaal is in Nederland (en wat wel mag)"
SAMENVATTING = ("Wedden op corners is in Nederland verboden, net als op kaarten en inworpen. Waarom, wat de regels precies "
                "zijn en waar je wél op mag wedden.")

content = f"""<p><strong>Wedden op corners (hoekschoppen) mag in Nederland niet. Corners staan op de wettelijke lijst van verboden weddenschappen, omdat ze makkelijk te manipuleren zijn. Die regel geldt sinds de Wet kansspelen op afstand op 1 april 2021 in werking trad, en sinds de legale online markt op 1 oktober 2021 openging, bieden legale bookmakers geen cornermarkten aan. Dat geldt voor alle legale bookmakers: geen weddenschappen op het aantal corners in een wedstrijd, per helft of per team, en ook niet op wie de eerste corner krijgt. Hetzelfde verbod geldt onder meer voor gele en rode kaarten, inworpen, overtredingen en buitenspel.</strong></p>
<p>Wie in het buitenland of op een buitenlandse site ooit op corners wedde, kijkt bij Nederlandse bookmakers vaak tevergeefs naar die markt. In dit artikel lees je waarom wedden op corners verboden is, welke regel het precies verbiedt, op welke andere gebeurtenissen je ook niet mag wedden en welke legale alternatieven er wel zijn.</p>
<h3><strong>Waarom is wedden op corners verboden?</strong></h3>
<p>De reden is matchfixing. Een corner is een kleine gebeurtenis die een speler in zijn eentje kan veroorzaken: een bal bewust over de achterlijn werken kost een verdediger weinig moeite en valt nauwelijks op. Een wedstrijd verliezen is lastig te regelen, maar een extra corner weggeven niet. Juist daarom zijn dit soort markten aantrekkelijk voor criminelen die wedstrijden willen manipuleren, en kwetsbaar voor spelers die daarvoor worden benaderd.</p>
<p>De Nederlandse regels verbieden daarom weddenschappen op gebeurtenissen die negatief zijn of eenvoudig te manipuleren. Zo wil de overheid de integriteit van de sport beschermen en voorkomen dat (jonge) spelers onder druk worden gezet om een wedstrijd te beïnvloeden.</p>
<h3><strong>Welke regel verbiedt wedden op corners?</strong></h3>
<p>Het verbod staat in de regels die horen bij de Wet kansspelen op afstand:</p>
<ul><li><strong>Besluit kansspelen op afstand, artikel 4.9:</strong> een aanbieder mag geen weddenschappen aanbieden op een negatieve of eenvoudig te manipuleren gebeurtenis, op jeugdwedstrijden, op wedstrijden met alleen onbetaalde sporters en op wedstrijden waarvan het verloop niet objectief wordt vastgelegd.</li><li><strong>Regeling kansspelen op afstand, artikel 3.15 en Bijlage 2:</strong> hierin staat per sport precies welke wedstrijden en gebeurtenissen zijn uitgesloten. Bij voetbal staan de hoekschoppen er letterlijk in: het veroorzaken, toekennen en nemen van een corner, inclusief het aantal per wedstrijd, per helft of per team.</li></ul>
<p>Het verbod geldt dus niet alleen voor "aantal corners over 9,5", maar voor elke markt waarin corners een rol spelen, ook als onderdeel van een bet builder of een live weddenschap.</p>"""

content2 = f"""<h3><strong>Op welke gebeurtenissen mag je nog meer niet wedden?</strong></h3>
{tabel(["Sport", "Verboden weddenschappen"], [
    ("<strong>Voetbal</strong>", "Hoekschoppen, gele en rode kaarten (ook voor trainers), inworpen, overtredingen, strafschoppen veroorzaken of nemen, buitenspel, wissels, blessurebehandelingen, de extra tijd die de vierde official aangeeft, VAR-momenten en juichgedrag"),
    ("<strong>Tennis</strong>", "Dubbele fouten, challenges, straffen van de scheidsrechter, en winst of verlies van een specifieke game of set"),
    ("<strong>Handbal</strong>", "Tijdelijke en definitieve uitsluitingen"),
    ("<strong>Wedstrijden</strong>", "Alle wedstrijden voor spelers onder 21 jaar, jeugdwedstrijden, voetbal in de derde divisie en lager, en wedstrijden met alleen amateurs"),
    ("<strong>Buiten de wedstrijd</strong>", "Prijsverkiezingen zoals een MVP- of spelersprijs, transfers en politieke verkiezingen"),
])}
<p><em>Bron: Bijlage 2 bij de Regeling kansspelen op afstand en de Kansspelautoriteit (maart 2026).</em></p>
<p>Opvallend: in tennis mag je dus ook niet wedden op wie een bepaalde game of set wint, terwijl wedden op de uitslag van de wedstrijd of het aantal games wel mag.</p>
<h3><strong>Controleert de Kansspelautoriteit dit ook?</strong></h3>
<p>Ja. De Kansspelautoriteit (Ksa) houdt toezicht op het wedaanbod van legale bookmakers. In 2026 sprak de Ksa nog een legale aanbieder aan die tijdens het WK live weddenschappen aanbood op inworpen, overtredingen, hoekschoppen en buitenspel. Eerder kregen meerdere aanbieders een waarschuwing en één zelfs een last onder dwangsom vanwege verboden weddenschappen. Ook in maart 2026 wees de Ksa alle aanbieders er nog eens op wat wel en niet onder hun vergunning valt.</p>
<h3><strong>Kan ik nog ergens op corners wedden?</strong></h3>
<p>Niet legaal in Nederland. Buitenlandse wedsites die wel cornermarkten aanbieden aan Nederlandse spelers, hebben geen Nederlandse vergunning en zijn dus illegaal. Wedden bij zo'n site is volgens de Wet op de kansspelen strafbaar, met een boete tot €11.000. Bovendien heb je er geen bescherming: geen toezicht, geen garantie dat je je winst krijgt en geen Cruks-check. Het aanbieden van verboden weddenschappen zoals corners is juist een van de duidelijkste kenmerken van een illegale bookmaker.</p>
<p>Twijfel je of een wedsite legaal is? Zoek hem op in de <a href="{KANSSPELWIJZER}" target="_blank" rel="noopener">Kansspelwijzer van de Kansspelautoriteit</a> of lees ons artikel <a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe weet ik of een bookmaker legaal is</a>.</p>"""

content3 = f"""<h3><strong>Waar mag je wél op wedden? De legale alternatieven</strong></h3>
<p>Ook zonder corners en kaarten is er bij legale bookmakers genoeg keus. Populaire alternatieven:</p>
<ul><li><strong>Schoten op doel:</strong> het aantal schoten op doel van een speler, een team of de hele wedstrijd. Lees <a href="/nieuws/dit-is-hoe-wedden-op-schoten-op-doel-werkt">hoe wedden op schoten op doel werkt</a>.</li><li><strong>Over/under doelpunten:</strong> meer of minder dan bijvoorbeeld 2,5 doelpunten. Bekijk onze <a href="/wedtips/over-2-5-goals-tips-voorspellingen">over 2,5 goals tips</a>.</li><li><strong>Beide teams scoren:</strong> scoren beide ploegen wel of niet? Zie onze <a href="/wedtips/btts-tips-voorspellingen">BTTS-tips</a>.</li><li><strong>Doelpuntenmakers:</strong> wie scoort de eerste goal, of scoort een speler op enig moment in de wedstrijd?</li><li><strong>Handicap wedden:</strong> een team begint met een virtuele voor- of achterstand. Lees <a href="/kennisbank/wat-is-handicap-wedden-welke-soorten-handicap-wedden-opties-zijn-er-in-nederland">wat handicap wedden is</a>.</li><li><strong>Bet builder:</strong> combineer meerdere markten uit één wedstrijd, zoals een winnaar, doelpunten en schoten op doel. Zie onze <a href="/wedtips/betbuilder-tips-voorspellingen">betbuilder tips</a>.</li></ul>
<p>Vergelijk vóór je inzet altijd de quoteringen, want die verschillen per bookmaker. Dat doe je eenvoudig met onze <a href="/odds-vergelijken-bij-alle-bookmakers-beste-odds-vandaag">odds vergelijker</a>.</p>
<h3><strong>Legale bookmakers in Nederland</strong></h3>
<p>Op dit moment hebben 25 aanbieders een vergunning voor online sportweddenschappen. Onze aanraders:</p>
{aanraders()}
<p>Bekijk alle legale bookmakers met onze beoordeling op de pagina <a href="/bookmakers">bookmakers</a>.</p>
<h3><strong>Veelgestelde vragen over wedden op corners</strong></h3>
<p><strong>Mag je in Nederland wedden op corners?</strong><br>Nee. Weddenschappen op hoekschoppen zijn bij Nederlandse legale bookmakers verboden, net als weddenschappen op kaarten, inworpen, overtredingen en buitenspel.</p>
<p><strong>Sinds wanneer is wedden op corners verboden?</strong><br>De regel staat in de Regeling kansspelen op afstand en geldt sinds de Wet kansspelen op afstand op 1 april 2021 in werking trad. Sinds de legale online markt op 1 oktober 2021 openging, bieden legale bookmakers geen weddenschappen op corners aan.</p>
<p><strong>Waarom mag je niet wedden op gele kaarten?</strong><br>Om dezelfde reden als bij corners: een gele kaart kan een speler zelf makkelijk veroorzaken, waardoor de markt gevoelig is voor matchfixing. Kaarten zijn daarnaast een negatieve gebeurtenis, en die zijn ook uitgesloten.</p>
<p><strong>Kan ik in een bet builder corners toevoegen?</strong><br>Nee, ook niet als onderdeel van een combinatie. Het verbod geldt voor elke weddenschap waarin corners voorkomen.</p>
<p><strong>Mag je wedden op schoten op doel?</strong><br>Ja. Schoten en schoten op doel staan niet op de lijst met verboden gebeurtenissen en worden door legale bookmakers aangeboden.</p>
<p><strong>Is wedden op corners bij een buitenlandse site strafbaar?</strong><br>Wedden bij een aanbieder zonder Nederlandse vergunning is volgens de wet strafbaar, met een boete tot €11.000. Bovendien heb je er geen enkele bescherming.</p>
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
