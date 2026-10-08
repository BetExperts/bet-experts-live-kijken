# -*- coding: utf-8 -*-
"""Los artikel: Ronde van Lombardije 2026 op tv (Eurosport 1). Evergreen slug, volgend jaar bijwerken.
  python3 specials/ronde_van_lombardije_2026.py [--live]"""
import os, sys, hashlib
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF
from lk_build import kanaal_tabel, esc
from lk_config import PROVIDERS, BASE

SLUG = "ronde-van-lombardije-op-tv"
TITEL = "Ronde van Lombardije op tv: zender, starttijd en livestream"
RUBRIEK_LIVE_KIJKEN = "67d41f195cace9697f8f9ad3"
TOTO = PROVIDERS["toto"]
_T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
_TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
_TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'

content = f"""<p><a href="/live-kijken">‹ Alle sport live kijken: zenders en tijden</a></p>
<p><strong>De Ronde van Lombardije zie je zaterdag 10 oktober gratis live op Eurosport 1. De uitzending begint om 10:35 uur, het peloton vertrekt om 11:00 uur in Bergamo en de winnaar komt tussen ongeveer 16:40 en 17:20 uur over de streep in Como.</strong></p>
<p>Il Lombardia is het laatste monument van het wielerseizoen en voor veel renners de laatste kans op een grote zege voor de winterstop. Hieronder lees je op welke zender en welk kanaalnummer je de koers volgt, hoe laat de uitzending begint, hoe je online meekijkt en wat het parcours van 2026 zo zwaar maakt.</p>
<h3>Waar is de Ronde van Lombardije op tv?</h3>
<ul><li><strong>Eurosport 1</strong> (gratis, in het basispakket): live van 10:35 tot 17:15 uur</li><li><strong>Online</strong>: in de tv-app van je aanbieder (zoals Ziggo GO, KPN TV en Odido TV) en via HBO Max met de sportuitbreiding</li></ul>
{kanaal_tabel("Eurosport 1")}
<h3>Hoe laat begint de Ronde van Lombardije?</h3>
<p>De officiële start is om 11:00 uur op de Piazza Matteotti in Bergamo. Eurosport 1 schakelt al om 10:35 uur in, zodat je het vertrek en de neutralisatie live meekrijgt. Afhankelijk van het tempo wordt de finish aan de Lungo Lario in Como tussen 16:40 en 17:20 uur verwacht.</p>
<table {_T}><thead><tr><th {_TH}>Zender</th><th {_TH}>Uitzending (NL)</th><th {_TH}>Toegang</th></tr></thead><tbody><tr><td {_TD}>Eurosport 1</td><td {_TD}>10:35 tot 17:15 uur</td><td {_TD}>gratis</td></tr></tbody></table>
<h3>Ronde van Lombardije gratis kijken</h3>
<p>Je hoeft geen extra abonnement af te sluiten: Eurosport 1 zit bij Ziggo, KPN, Odido, DELTA, Youfone en de meeste andere aanbieders gewoon in het basispakket. Zet zaterdag dus op tijd het juiste kanaalnummer aan en je kijkt de hele koers zonder extra kosten. Onderweg kijk je met dezelfde inloggegevens mee in de tv-app van je aanbieder.</p>"""

content2 = """<h3>Het parcours van 2026: van Bergamo naar Como</h3>
<p>De Ronde van Lombardije wisselt elk jaar van richting tussen Bergamo en Como. Dit jaar, in de 120e editie, is Bergamo de startplaats en ligt de finish in Como. De renners rijden 239 kilometer met ruim 4.600 hoogtemeters, verdeeld over negen beklimmingen. Daarmee is het een koers voor echte klimmers: wie hier wint, moet na zes uur koers nog kunnen versnellen.</p>
<p><strong>De belangrijkste klimmen op een rij:</strong></p>
<ul><li><strong>Selvino</strong> (ongeveer 11 km, top op 947 meter): de lange haarspeldbochtenklim in de Bergamasker Prealpen, vroeg in de koers</li><li><strong>Valpiana</strong> (6,4 km): met 989 meter het hoogste punt van de dag</li><li><strong>Colle Brianza</strong> (top op 670 meter): de overgang van de Prealpen naar het Comomeer</li><li><strong>Madonna del Ghisallo</strong> (8,6 km, uitschieters tot 14%): de mythische klim vanuit Bellagio naar de kapel van de wielrenners, ruim 60 km voor de finish</li><li><strong>San Fermo della Battaglia</strong> (2,7 km, gemiddeld zo'n 7%): twee keer op het slotcircuit, de laatste top ligt ongeveer 5 km voor de streep</li><li><strong>Civiglio</strong> (4,2 km aan gemiddeld 9,7%): de steilste klim van de finale</li></ul>
<h3>Waar valt de beslissing?</h3>
<p>Nieuw dit jaar is het slotcircuit van zo'n 22 kilometer rond Como. Binnen een half uur koers liggen daar drie klimmen: San Fermo della Battaglia, de Civiglio en opnieuw San Fermo. De Ghisallo zorgt voor de schifting, maar de echte aanval verwachten we op de Civiglio. Wie daar weg is, moet op de laatste klim van San Fermo nog één keer standhouden en kan dan in de afdaling naar het meer de zege veiligstellen.</p>
<h3>Favorieten: geen Pogačar dit jaar</h3>
<p>Tadej Pogačar won de laatste vijf edities (2021 tot en met 2025) en kwam daarmee op gelijke hoogte met recordhouder Fausto Coppi. Dit jaar ontbreekt de Sloveen: na zijn val in de Vuelta eind augustus, met onder meer een gebroken sleutelbeen, zit zijn seizoen erop. Daardoor ligt de koers wijd open.</p>
<ul><li><strong>Remco Evenepoel</strong>: vorig jaar tweede achter Pogačar en net Europees kampioen, op papier de grootste kanshebber</li><li><strong>Isaac Del Toro</strong> en <strong>Juan Ayuso</strong>: explosieve klimmers die een finale met steile hellingen aankunnen</li><li><strong>Brandon McNulty</strong> (wereldkampioen) en <strong>Matteo Jorgenson</strong>: sterk op lange, zware klimmen</li><li><strong>Tom Pidcock</strong> en <strong>Quinn Simmons</strong>: kunnen profiteren van de snelle afdalingen richting Como</li><li><strong>Italiaanse hoop</strong>: Giulio Ciccone, Christian Scaroni en Antonio Tiberi rijden hun thuiskoers</li></ul>
<h3>Over de Ronde van Lombardije</h3>
<p>Il Lombardia werd voor het eerst verreden in 1905 en is een van de vijf wielermonumenten, naast Milaan-Sanremo, de Ronde van Vlaanderen, Parijs-Roubaix en Luik-Bastenaken-Luik. Omdat de koers in de herfst valt, heet hij in Italië ook wel de klassieker van de vallende bladeren. Bovenop de Ghisallo staat de kapel van de Madonna del Ghisallo, de beschermheilige van de wielrenners, met een museum vol fietsen van wielerlegendes.</p>"""

toto_link = TOTO["link"]
content3 = f"""<h3>Wedden op de Ronde van Lombardije</h3>
<p>Bij bookmakers kun je wedden op de winnaar van Il Lombardia, op een podiumplaats of op onderlinge duels tussen twee renners. Zonder de vijfvoudig winnaar aan de start liggen de odds dit jaar dichter bij elkaar dan normaal, wat de koers ook voor wedders interessant maakt. Bekijk vooraf het parcours: een klimmer met een goede afdaling heeft in deze finale een streepje voor.</p>
<p>👉 <a href="{toto_link}"><strong>Bekijk de odds op de Ronde van Lombardije bij TOTO</strong></a></p>
<h3>Veelgestelde vragen</h3>
<p><strong>Op welke zender is de Ronde van Lombardije?</strong><br>Op Eurosport 1, zaterdag 10 oktober van 10:35 tot 17:15 uur. Bij Ziggo is dat kanaal 25, bij KPN kanaal 35 en bij Odido kanaal 131.</p>
<p><strong>Hoe laat begint de Ronde van Lombardije?</strong><br>De renners vertrekken om 11:00 uur in Bergamo. De tv-uitzending begint om 10:35 uur en de finish in Como wordt tussen 16:40 en 17:20 uur verwacht.</p>
<p><strong>Kan ik de Ronde van Lombardije gratis kijken?</strong><br>Ja. Eurosport 1 zit bij vrijwel elke Nederlandse tv-aanbieder in het basispakket, dus met je gewone tv-abonnement kijk je zonder extra kosten mee.</p>
<p><strong>Kan ik de Ronde van Lombardije online kijken?</strong><br>Ja, via de tv-app van je aanbieder (zoals Ziggo GO, KPN TV of Odido TV) of via HBO Max met de sportuitbreiding.</p>
<p><strong>Hoe lang is de Ronde van Lombardije 2026?</strong><br>239 kilometer van Bergamo naar Como, met negen beklimmingen en ruim 4.600 hoogtemeters.</p>
<p><strong>Wie won de Ronde van Lombardije in 2025?</strong><br>Tadej Pogačar, voor de vijfde keer op rij. Remco Evenepoel werd tweede op 1 minuut en 48 seconden, Michael Storer derde.</p>
<p><a href="/live-kijken"><strong>Bekijk alle sport die je live kunt kijken</strong></a></p>
<p><em>Gokken is alleen toegestaan voor personen van 18 jaar en ouder. Wat kost gokken jou? Stop op tijd. 18+ | Speel bewust.</em></p>"""

SAMENVATTING = ("De Ronde van Lombardije zie je zaterdag 10 oktober gratis live op Eurosport 1 (10:35-17:15 uur). "
                "Start 11:00 uur in Bergamo, plus de kanaalnummers.")

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING[:155], "rubriek": RUBRIEK_LIVE_KIJKEN,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        os.makedirs(os.path.join(BASE, "preview"), exist_ok=True)
        open(os.path.join(BASE, "preview", SLUG + ".html"), "w", encoding="utf-8").write(
            f"<h1>{esc(TITEL)}</h1><p><em>{esc(fd['samenvatting'])}</em></p>{content}{content2}{content3}")
        print("preview geschreven", len(fd["samenvatting"])); sys.exit()
    print("item:", WF.create_live(fd))
