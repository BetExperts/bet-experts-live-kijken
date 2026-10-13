# -*- coding: utf-8 -*-
"""Los artikel: Eneco Tour 2026 (13-18 okt, Den Haag - Arnhem): etappes, favorieten, odds Bet365, weer, tv.
Aanleveringstekst herschreven. Gecontroleerd: data/etappes (Ziggo-overzicht), naam (vorig jaar Tour of Holland, Laporte won),
eerste editie met vrouwen (2.1), uitzending HBO Max met sport-add-on. Weggelaten: afstand proloog en etappe 4 (bronnen
verschillen), 'eerste winnaar sinds Erik Dekker 2004'. Odds aangeleverd door de gebruiker (Bet365, 13-10).
  python3 specials/eneco_tour_2026.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Eneco Tour 2026: data, etappes, favorieten, odds en waar je kijkt"
SLUG = "eneco-tour-2026"
SAMENVATTING = ("Eneco Tour 2026 (13-18 oktober, Den Haag - Arnhem): alle etappes, de favorieten met odds, het weer en "
                "waar je de koers live kijkt.")
RUBRIEK_LIVE_KIJKEN = "67d41f195cace9697f8f9ad3"
BET365 = "https://www.bet365.nl/hub/nl-nl/open-account?affiliate=365_02599619"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in koppen)
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}><thead><tr>{kop}</tr></thead><tbody>{body}</tbody></table>"


def odd(x):
    return f'<a href="{BET365}" rel="sponsored"><strong>{x}</strong></a>'


ODDS = [("Christophe Laporte", "Visma | Lease a Bike", "1.66"), ("Finn Fisher-Black", "Red Bull-BORA-hansgrohe", "5.00"),
        ("Jakob Söderqvist", "Lidl-Trek", "6.00"), ("Lukas Kubis", "Unibet Rose Rockets", "15.00"),
        ("Ethan Hayter", "Soudal Quick-Step", "15.00"), ("Mick van Dijke", "Red Bull-BORA-hansgrohe", "21.00"),
        ("Victor Campenaerts", "Visma | Lease a Bike", "21.00"), ("Pepijn Reinderink", "Soudal Quick-Step", "26.00"),
        ("Tomas Kopecky", "Unibet Rose Rockets", "41.00"), ("Wessel Mouris", "Unibet Rose Rockets", "41.00"),
        ("Filippo Fiorelli", "Visma | Lease a Bike", "51.00"), ("Edoardo Affini", "Visma | Lease a Bike", "51.00")]

content = f"""<p><strong>De Eneco Tour 2026 begint dinsdagavond 13 oktober met een proloog in Den Haag en eindigt zondag 18 oktober in Arnhem. Zes dagen lang trekt het peloton door Nederland, langs de Veluwe, Brabant, Zuid-Limburg en Drenthe. Christophe Laporte verdedigt zijn titel en is volgens de bookmakers de grote favoriet. Hieronder lees je alles over de etappes, de kanshebbers, de odds, het weer en waar je de koers live kijkt.</strong></p>
<h3><strong>Eneco Tour 2026 in het kort</strong></h3>
{tabel(["", ""], [
    ("<strong>Data</strong>", "Dinsdag 13 t/m zondag 18 oktober 2026"),
    ("<strong>Start en finish</strong>", "Den Haag (proloog) - Arnhem (slotetappe)"),
    ("<strong>Aantal dagen</strong>", "Zes: een proloog en vijf etappes"),
    ("<strong>Titelverdediger</strong>", "Christophe Laporte (Visma | Lease a Bike)"),
    ("<strong>Topfavoriet</strong>", f"Christophe Laporte ({odd('1.66')} bij Bet365)"),
    ("<strong>Live kijken</strong>", "HBO Max (met sport-add-on) en Eurosport"),
    ("<strong>Nieuw dit jaar</strong>", "Voor het eerst ook een vrouwenwedstrijd, op dezelfde dagen"),
])}
<p>De koers heette vorig jaar nog de Tour of Holland en gaat dit jaar verder als de Eneco Tour, met voor het eerst ook een wedstrijd voor de vrouwen. In dit artikel focussen we op de mannenwedstrijd.</p>
<h3><strong>Etappes Eneco Tour 2026</strong></h3>
{tabel(["Dag", "Etappe", "Type"], [
    ("Di 13 okt", "Proloog: Den Haag (Sportcampus Zuiderpark)", "Korte tijdrit in de avond"),
    ("Wo 14 okt", "Etappe 1: Ede - Ede (120 km)", "Vlak, sprintersrit"),
    ("Do 15 okt", "Etappe 2: Tilburg - Tilburg (13,6 km)", "Individuele tijdrit"),
    ("Vr 16 okt", "Etappe 3: Sittard - Watersley (110,5 km)", "Heuvelrit in Zuid-Limburg"),
    ("Za 17 okt", "Etappe 4: Hoogeveen - VAM-berg", "Heuvelrit met finish bergop"),
    ("Zo 18 okt", "Etappe 5: Arnhem - Arnhem (149,2 km)", "Vlak, sprint verwacht"),
])}
<h4>Proloog, dinsdag 13 oktober: Den Haag</h4>
<p>De openingsdag is een korte, vlakke tijdrit in de avonduren bij Sportcampus Zuiderpark, waarin de mannen en vrouwen om en om van start gaan. Wie hier wint, heeft vooral snelheid en explosiviteit nodig. Vorig jaar was Ethan Hayter de snelste in de proloog, voor Cameron Rogers en Jakob Söderqvist.</p>
<h4>Etappe 1, woensdag 14 oktober: Ede - Ede</h4>
<p>Een vlakke rit van 120 kilometer over de Veluwe, met start en finish aan de Arnhemseweg. Alles wijst op een sprint. Ede heeft een rijke wielergeschiedenis: op grotendeels dezelfde wegen werd Danny van Poppel in 2025 Nederlands kampioen. Tim Merlier en Dylan Groenewegen gelden als de snelste mannen in het veld.</p>
<h4>Etappe 2, donderdag 15 oktober: tijdrit in Tilburg</h4>
<p>Een individuele tijdrit van 13,6 kilometer, met start en finish vlak bij elkaar aan de Stappegoorweg. Hier ontstaan de eerste echte verschillen in het klassement. Vorig jaar won Hayter de tijdrit, toen nog in Etten-Leur. Hayter, Söderqvist en Edoardo Affini zijn de kanshebbers voor de dagzege.</p>
<h4>Etappe 3, vrijdag 16 oktober: Sittard - Watersley</h4>
<p>De eerste heuvelrit gaat van het Tom Dumoulin Bikepark in Sittard naar het Watersley Sports &amp; Talentpark, over 110,5 kilometer. Het peloton rijdt meerdere rondes met per ronde vier korte, steile stukken:</p>
{tabel(["Helling", "Lengte", "Gemiddeld"], [
    ("Sittardseweg", "600 meter", "4,6%"), ("Schatsberg", "700 meter", "4,4%"),
    ("Windraak", "690 meter", "4,6%"), ("Finishstraat Watersley", "750 meter", "4,2%"),
])}
<p>Vorig jaar werd deze etappe stilgelegd vanwege onveilige situaties en uiteindelijk geschrapt. Dit jaar kan Limburg dus voor het eerst echt een rol spelen in het klassement.</p>
<h4>Etappe 4, zaterdag 17 oktober: Hoogeveen - VAM-berg</h4>
<p>De koninginnenrit eindigt boven op de VAM-berg in Wijster, het hoogste punt van Drenthe. Vorig jaar won Timo de Jong hier, voor Lukas Kubis en Christophe Laporte, en die dag pakte Laporte de leiderstrui over van de uitgestapte Hayter. Op dezelfde berg werd Laporte in 2023 Europees kampioen.</p>
<h4>Etappe 5, zondag 18 oktober: Arnhem - Arnhem</h4>
<p>De slotrit over 149,2 kilometer begint en eindigt aan de Zijpendaalseweg. Het parcours wisselt technische stukken af met snelle wegen. Op papier is het een dag voor de sprinters, maar als het klassement kort is, kan de finale nog spannend worden. Vorig jaar won Van Poppel de slotetappe, en op dezelfde Zijpendaalseweg werd Groenewegen in 2024 Nederlands kampioen.</p>"""

content2 = f"""<h3><strong>Favorieten en voorspelling voor de eindzege</strong></h3>
<p>Om de Eneco Tour te winnen, moet je goed kunnen tijdrijden én mee kunnen in de heuvels van Limburg en Drenthe. Vorig jaar won Laporte het eindklassement met 37 seconden voorsprong op Kubis, Söderqvist werd derde.</p>
<h4>Topfavoriet: Christophe Laporte ({odd('1.66')})</h4>
<p>De Fransman van Visma | Lease a Bike is de titelverdediger en heeft een parcours dat hem op het lijf geschreven is. De finish op de VAM-berg, waar hij in 2023 Europees kampioen werd en vorig jaar de leiderstrui veroverde, past perfect bij zijn kwaliteiten. Ook in de tijdritten kan hij mee, en met Affini en Victor Campenaerts heeft hij twee sterke tijdrijders naast zich. Eerder dit jaar won hij de openingsetappe van de Ruta del Sol. Eén kanttekening: begin september stapte hij uit in de Vuelta, zonder dat daar een reden voor werd gegeven. Hoe zijn vorm precies is, blijft daardoor een vraagteken.</p>
<h4>Tweede kanshebber: Finn Fisher-Black ({odd('5.00')})</h4>
<p>De 24-jarige Nieuw-Zeelander van Red Bull-BORA-hansgrohe is nationaal kampioen tijdrijden en werd in augustus tweede in de Tour de Pologne, tien seconden achter Marco Brenner. In de slottijdrit daar eindigde hij als tweede achter Stefan Küng. Met een proloog en een tijdrit van 13,6 kilometer kan hij vroeg in de week tijd pakken. De vraag is of hij die voorsprong vasthoudt op de hellingen in Limburg en op de VAM-berg.</p>
<h4>Outsiders</h4>
<ul><li><strong>Jakob Söderqvist</strong> (Lidl-Trek, {odd('6.00')}): vorig jaar derde in het klassement en in de proloog, kanshebber in beide tijdritten.</li><li><strong>Lukas Kubis</strong> (Unibet Rose Rockets, {odd('15.00')}): eindigde vorig jaar als tweede en werd derde op de VAM-berg.</li><li><strong>Ethan Hayter</strong> (Soudal Quick-Step, {odd('15.00')}): won vorig jaar de proloog en de tijdrit en droeg de leiderstrui tot hij in etappe 4 uitstapte.</li><li><strong>Mick van Dijke</strong> (Red Bull-BORA-hansgrohe, {odd('21.00')}): Nederlandse outsider die ver kan komen in het klassement.</li><li><strong>Victor Campenaerts</strong> (Visma | Lease a Bike, {odd('21.00')}): sterke tijdrijder in de ploeg van Laporte.</li><li><strong>Pepijn Reinderink</strong> (Soudal Quick-Step, {odd('26.00')}): Nederlandse outsider, kanshebber voor de rit naar Watersley.</li></ul>
<p><strong>Onze voorspelling:</strong> Laporte prolongeert zijn titel. Het parcours met de VAM-berg past perfect bij hem en hij heeft een sterke ploeg. Wil je meer rendement, dan is Fisher-Black een interessante tweede keuze, vooral als hij de tijdritten domineert.</p>
<h3><strong>Odds eindzege Eneco Tour 2026</strong></h3>
<p>De odds hieronder zijn van Bet365 (stand 13 oktober). Klik op een quotering om direct naar Bet365 te gaan.</p>
{tabel(["Renner", "Ploeg", "Odd winnaar"], [(r, p, odd(o)) for r, p, o in ODDS])}
<p>👉 <a href="{BET365}" rel="sponsored"><strong>Maak een account aan bij Bet365 en bekijk alle odds voor de Eneco Tour</strong></a></p>
<p><em>De odds zijn indicatief en kunnen wijzigen.</em></p>"""

content3 = """<h3><strong>Het weer tijdens de Eneco Tour</strong></h3>
<p>Het weer wordt wisselvallig, maar zonder uitschieters. De middagtemperaturen liggen de hele week tussen ongeveer 13 en 19 graden, met de koelste dagen aan het eind van de week. Regen valt vooral tijdens de proloog op dinsdagavond en op vrijdag en zaterdag, steeds in beperkte hoeveelheden. Woensdag en donderdag blijven naar verwachting droog. De wind is zwak tot matig. Omdat de koers door het hele land trekt, kan het weer per etappeplaats verschillen: controleer op de dag zelf de verwachting voor de etappe.</p>
<h3><strong>Waar kun je de Eneco Tour 2026 live kijken?</strong></h3>
<p>De Eneco Tour is van dinsdag 13 tot en met zondag 18 oktober live te zien op <a href="/zenders/hbo-max">HBO Max</a>, met de sport-add-on, en via <a href="/zenders/eurosport">Eurosport</a>. Op de dag zelf vind je de exacte uitzendtijden in de tv-gids van je aanbieder.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wanneer is de Eneco Tour 2026?</strong><br>Van dinsdag 13 tot en met zondag 18 oktober 2026.</p>
<p><strong>Waar begint en eindigt de Eneco Tour?</strong><br>De proloog is in Den Haag, de slotetappe in Arnhem.</p>
<p><strong>Wie won de koers vorig jaar?</strong><br>Christophe Laporte, met 37 seconden voorsprong op Lukas Kubis. De koers heette toen nog de Tour of Holland.</p>
<p><strong>Wie is de favoriet voor de eindzege?</strong><br>Christophe Laporte, met een quotering van 1.66 bij Bet365. Finn Fisher-Black volgt op 5.00.</p>
<p><strong>Waar kan ik de Eneco Tour live kijken?</strong><br>Op HBO Max met de sport-add-on en via Eurosport.</p>
<p><strong>Wat is de zwaarste etappe?</strong><br>Etappe 4 naar de VAM-berg in Drenthe, met de finish boven op de berg. Ook de heuvelrit naar Watersley kan het klassement flink opschudden.</p>
<p><em>Gokken is alleen toegestaan voor personen van 18 jaar en ouder. Speel verantwoord. Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_LIVE_KIJKEN,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting"); sys.exit()
    print("item:", WF.create_live(fd))
