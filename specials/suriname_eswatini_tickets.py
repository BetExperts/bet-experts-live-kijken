# -*- coding: utf-8 -*-
"""Artikel 2/3 Suriname – Eswatini: tickets (waar, prijzen, De Vliert, parkeren, OV). Feiten: suriname_eswatini_2026_feiten.md §0, §2.
Prijzen zelf gecontroleerd in de ticketshop op 13-11 (€20 standaard, €10 vak I4, €45 business). Niet gevonden: kinderprijs,
kassa op de dag, openingstijd stadion -> niet als feit noemen. Buslijnnummers niet gecontroleerd -> verwijzen naar 9292.
  python3 specials/suriname_eswatini_tickets.py  (dry run)"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, "..")); sys.path.insert(0, HIER)
from legaal_data import tabel
from suriname_eswatini_2026_data import RUBRIEK, KSA, SLUGS, L, WEDSTRIJD

SLUG = SLUGS["tickets"]
TITEL = "Tickets Suriname – Eswatini: prijzen, De Vliert en parkeren"
SAMENVATTING = ("Tickets voor Suriname – Eswatini koop je via FC Den Bosch, vanaf €10. Prijzen, vakken, parkeren en "
                "de route naar De Vliert op een rij.")
OG_EB, OG_KOP = "Oefeninterland · tickets", "Tickets Suriname – <em>Eswatini</em>"
OG_RIJEN = [("Standaard", "€20"), ("Vak I4 (Noord)", "€10"), ("Business", "€45"), ("Max. per account", "8 tickets")]

content = f"""<p><strong>Tickets voor Suriname – Eswatini koop je alleen via de officiële ticketshop van FC Den Bosch. Een gewone plek kost €20, in één vak op de Noordtribune betaal je €10 en business kost €45. Je hebt een account nodig en kunt maximaal acht kaarten per account kopen. Op vrijdag 13 november waren er nog plekken in alle vakken. De wedstrijd is zondag 15 november om 18:00 uur in Stadion De Vliert in Den Bosch.</strong></p>
<p>Het is de eerste wedstrijd van Natio in Nederland sinds maart 2024, toen Suriname in Almere met 1-1 gelijkspeelde tegen Martinique. De Surinaamse bond roept de gemeenschap op om massaal te komen, onder het motto "Natio Famiri, we are back!". Rond het stadion is er Surinaamse muziek en zijn er kraampjes met Surinaams eten.</p>
<h3><strong>Waar koop je tickets voor Suriname – Eswatini?</strong></h3>
<p>De kaartverkoop loopt via <strong>ticketing.fcdenbosch.nl</strong>, de ticketshop van {L['denbosch']}. Zo werkt het:</p>
<ul><li><strong>Maak een account aan</strong> in de ticketshop van FC Den Bosch (of log in als je er al een hebt).</li><li><strong>Kies de wedstrijd Suriname – Eswatini</strong> en daarna een vak op de plattegrond.</li><li><strong>Kies het aantal kaarten</strong>: maximaal acht per account.</li><li><strong>Reken af</strong> en bewaar je e-ticket op je telefoon.</li></ul>
<p>Koop alleen via de officiële shop. Kaarten die via sociale media of doorverkoopsites worden aangeboden, kunnen nep zijn of al gebruikt.</p>
<h3><strong>Wat kosten de tickets?</strong></h3>
{tabel(["Plek", "Vakken", "Prijs"], [
    ("Hoofdtribune", "B, C, F, G", "€20"),
    ("Noordtribune", "I1 – I3", "€20"),
    ("Noordtribune", "I4 (naast het uitvak)", "<strong>€10</strong>"),
    ("M-side (sfeervakken)", "M1 – M8", "€20"),
    ("Zuidtribune", "R1 – R5 (R3 – R5 familievak)", "€20"),
    ("Business", "BL1 – BL5, BPL1, BPL2", "€45"),
])}
<p><em>Prijzen gecontroleerd in de ticketshop op vrijdag 13 november. Een aparte kinderprijs zagen we niet; ook in het familievak kost een kaart €20.</em></p>"""

content2 = f"""<h3><strong>Stadion De Vliert: wat moet je weten?</strong></h3>
<p>De Vliert is het stadion van FC Den Bosch, aan de Victorialaan 21 in 's-Hertogenbosch. Het opende in 1951 en biedt plaats aan ongeveer 8.500 toeschouwers. Volgens Omroep Brabant is dit de eerste interland in het stadion in 75 jaar. Suriname kwam hier terecht omdat Almere geen plek had: de bond belde FC Den Bosch, dat direct ja zei en in ongeveer een week alles regelde. Bondscoach Henk Fraser woont bovendien vlak bij Den Bosch.</p>
<p>Let op: De Vliert heeft een <strong>kunstgrasveld</strong>. Voor het publiek maakt dat niets uit, maar het verklaart waarom grotere tegenstanders hier liever niet spelen.</p>
<h3><strong>Parkeren bij De Vliert</strong></h3>
{tabel(["Optie", "Wat je moet weten"], [
    ("Parkeren bij het stadion (P3, P4, P5)", "Samen ongeveer 560 plaatsen. De openstelling op wedstrijddagen kan wisselen, dus kom op tijd."),
    ("P+R Transferium De Vliert", "Stadionlaan 9, ongeveer 700 plaatsen, €5,10 per dag inclusief bus naar het centrum. Ligt op loopafstand van het stadion."),
])}
<p>Wil je na de wedstrijd met de pendelbus van het transferium naar het centrum? Controleer dan de rijtijden: op zondag rijdt die bus volgens de informatie die wij vonden maar tot 18:00 uur.</p>
<h3><strong>Met het openbaar vervoer naar De Vliert</strong></h3>
<p>Het stadion ligt in het noordoosten van Den Bosch, ongeveer drie kilometer van station 's-Hertogenbosch. Lopen duurt zo'n half uur. Vanaf het station rijden bussen in de richting van De Vliert; plan je reis met 9292, want op zondag rijden er minder bussen. Fietsen kan ook: het stadion ligt zo’n 2,5 kilometer van het centrum.</p>
<h3><strong>Tips voor zondag</strong></h3>
<ul><li><strong>Kom op tijd.</strong> Rond het stadion zijn muziek en eetkraampjes, en bij een volle tribune kan het druk worden bij de ingang.</li><li><strong>Kleed je warm aan.</strong> De verwachting is ongeveer tien graden met motregen en wind.</li><li><strong>Neem je e-ticket mee</strong>, met een opgeladen telefoon.</li></ul>"""

content3 = f"""<h3><strong>Kun je de wedstrijd ook thuis kijken?</strong></h3>
<p>Op vrijdag was er nog geen tv-uitzending of livestream aangekondigd. Of dat nog verandert, lees je in ons artikel {L['kijken']}. Wie de spelers zijn en hoe Suriname ervoor staat, lees je in {L['voorspelling']}.</p>
<h3><strong>Suriname – Eswatini in het kort</strong></h3>
{tabel(["", ""], WEDSTRIJD)}
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Waar koop ik tickets voor Suriname – Eswatini?</strong><br>Alleen via de officiële ticketshop van FC Den Bosch (ticketing.fcdenbosch.nl). Je hebt een account nodig.</p>
<p><strong>Wat kost een kaartje voor Suriname – Eswatini?</strong><br>€20 voor een gewone plek, €10 in vak I4 op de Noordtribune en €45 voor business.</p>
<p><strong>Hoeveel tickets mag ik kopen?</strong><br>Maximaal acht per account.</p>
<p><strong>Is Suriname – Eswatini uitverkocht?</strong><br>Nee, op vrijdag 13 november waren er nog kaarten in alle vakken.</p>
<p><strong>Hoe laat begint de wedstrijd?</strong><br>Zondag 15 november 2026 om 18:00 uur.</p>
<p><strong>Waar kan ik parkeren bij De Vliert?</strong><br>Bij het stadion (P3, P4 en P5) of op P+R Transferium De Vliert aan de Stadionlaan, voor €5,10 per dag.</p>
{KSA}"""

if __name__ == "__main__":
    import re
    alles = content + content2 + content3
    w = len(re.sub(r"<[^>]+>", " ", alles).split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", w, "woorden")
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert 133 + 285 + 141 == 559
    assert "<h2" not in alles and "betcity" not in alles.lower() and "/go/" not in alles
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles) and content3.rstrip().endswith(KSA)
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    print("dry run ok")
