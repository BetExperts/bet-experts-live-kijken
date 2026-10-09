# -*- coding: utf-8 -*-
"""Wedtips Swiss Darts Trophy, vrijdag 9 okt 2026 (eerste ronde). Tip 1 (Van Barneveld @ 2.00) van de gebruiker;
overige odds Starcasino (Altenar-feed, 9 okt ~12:30).
  python3 specials/wedtips_swiss_darts_9_okt.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Wedtips Swiss Darts Trophy vrijdag 9 oktober: voorspellingen voor de eerste ronde"
SLUG = "wedtips-swiss-darts-trophy-9-oktober-2026"
SAMENVATTING = ("Onze wedtips voor de eerste dag van de Swiss Darts Trophy: Van Barneveld @ 2.00, een leg handicap op Doets "
                "en twee tips op 180's en legs.")
RUBRIEK_DARTS = "66b726271e317999159d5d44"
SC = "https://media1.affiliates.starcasino.nl/redirect.aspx?pid=2170&bid=1478"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in koppen)
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}><thead><tr>{kop}</tr></thead><tbody>{body}</tbody></table>"


def sc(o):
    return f'<a href="{SC}" target="_blank" rel="sponsored noopener"><strong>{o}</strong></a>'


content = f"""<p><strong>Vandaag begint in Basel de Swiss Darts Trophy met zestien wedstrijden in de eerste ronde. Onze beste wedtips voor vrijdag 9 oktober: Raymond van Barneveld wint het Nederlandse onderonsje met Maik Kuivenhoven (odd 2.00), Kevin Doets wint met minstens drie legs verschil, Michael Smith gooit de meeste 180's tegen Rob Owen en Chisnall – Soutar gaat over 9,5 legs.</strong></p>
<p>De openingsdag van de voorlaatste European Tour-stop telt een middagsessie vanaf 13:00 uur en een avondsessie vanaf 19:00 uur. De zestien reekshoofden komen pas zaterdag in actie, dus vandaag strijden de qualifiers om een plek in de tweede ronde en om belangrijk prijzengeld in de race naar het WK. Alles over het toernooi, de loting en het format lees je in onze <a href="/nieuws/swiss-darts-trophy-2026">voorbeschouwing van de Swiss Darts Trophy 2026</a>.</p>
<h3><strong>Onze wedtips in het kort</strong></h3>
{tabel(["Tip", "Wedstrijd", "Odd"], [
    ("Raymond van Barneveld wint", "Van Barneveld – Kuivenhoven (±20:30)", "<strong>2.00</strong>"),
    ("Kevin Doets wint met -2,5 legs", "Doets – Kenny (±22:30)", sc("1.83")),
    ("Meeste 180's: Michael Smith", "M. Smith – Owen (±21:30)", sc("2.43")),
    ("Meer dan 9,5 legs", "Chisnall – Soutar (±20:00)", sc("1.90")),
])}
<p><em>Odds van vrijdag 9 oktober rond 12:30 uur. Tip 1 komt van onze eigen tipgever; de overige odds zijn van Starcasino. Odds kunnen tot de start van de wedstrijd nog wijzigen. Aanvangstijden zijn indicatief, omdat de wedstrijden binnen een sessie na elkaar worden gespeeld.</em></p>"""

content2 = f"""<h3><strong>Tip 1: Raymond van Barneveld wint van Maik Kuivenhoven @ 2.00</strong></h3>
<p>Het Nederlandse duel van de avond is meer dan een prestigestrijd. Van Barneveld doet na een goed Pro Tour-tweeluik vorige maand weer mee in de race om een WK-ticket, en een zege levert hem belangrijk prijzengeld op en een wedstrijd tegen Jonny Clayton. Voor Kuivenhoven staat er ook veel op het spel, want hij vecht voor zijn tourkaart.</p>
<p>De bookmakers zien Kuivenhoven als lichte favoriet, maar in een best of 11 is het verschil klein. Van Barneveld heeft in dit soort beladen avondpartijen het publiek en zijn ervaring mee. Met een odd van 2.00 krijg je een mooie prijs voor de vijfvoudig wereldkampioen in een wedstrijd die bijna gelijk opgaat.</p>
<h3><strong>Tip 2: Kevin Doets wint met minstens drie legs verschil @ 1.83</strong></h3>
<p>Kevin Doets sluit de vrijdag af tegen Nick Kenny en is daarin de duidelijke favoriet (odd 1.24 voor de winst). Die odd is te laag om los te spelen. Daarom kiezen we voor de leg handicap: Doets moet met 6-3 of ruimer winnen. Kenny kan sterk spelen, maar is minder constant. Bij een goede avond van Doets ligt een ruime zege voor de hand, met een duel tegen Luke Humphries als beloning.</p>
<h3><strong>Tip 3: Michael Smith gooit de meeste 180's tegen Rob Owen @ 2.43</strong></h3>
<p>Michael Smith is de laatste tijd niet in topvorm en is tegen Rob Owen zelfs underdog (2.15). Toch blijft de oud-wereldkampioen een van de zwaarste scorers van het circuit. Ook op een mindere dag gooit hij veel maximums. Daarom spelen we niet de winnaar, maar de 180's: Smith gooit er volgens ons meer dan Owen. Een gelijk aantal betekent verlies, maar met 2.43 is de prijs aantrekkelijk.</p>
<h3><strong>Tip 4: Chisnall – Soutar gaat over 9,5 legs @ 1.90</strong></h3>
<p>Bij Dave Chisnall tegen Alan Soutar geven de bookmakers beide spelers precies dezelfde odd (1.83). Dat zegt genoeg: dit duel kan alle kanten op. In zo'n gelijkopgaande wedstrijd is een lange partij waarschijnlijk. Meer dan 9,5 legs betekent dat het minstens 6-4 moet worden. Daarvoor heb je niet nodig dat je de winnaar goed voorspelt.</p>"""

content3 = f"""<h3><strong>Alle wedstrijden van vrijdag met odds</strong></h3>
{tabel(["Wedstrijd", "Odds (Starcasino)"], [
    ("Niels Zonneveld – Bradley Brooks", "1.56 – 2.30"),
    ("William O'Connor – Jani Haavisto", "1.19 – 4.30"),
    ("Mensur Suljović – György Jehirszki", "1.20 – 4.20"),
    ("Sebastian Białecki – Karel Sedláček", "1.95 – 1.74"),
    ("Niko Springer – Roman Wellinger", "1.07 – 7.50"),
    ("Joe Cullen – Tom Bissell", "1.83 – 1.83"),
    ("Cameron Menzies – Cristo Reyes", "1.95 – 1.74"),
    ("Rob Cross – Mario Vandenbogaerde", "1.30 – 3.25"),
    ("Andrew Gilding – Stefan Bellmont", "1.33 – 3.10"),
    ("Jeffrey de Graaf – Sietse Lap", "1.30 – 3.25"),
    ("Dave Chisnall – Alan Soutar", "1.83 – 1.83"),
    ("Raymond van Barneveld – Maik Kuivenhoven", "1.95 – 1.74"),
    ("Dirk van Duijvenbode – Bruno Stoeckli", "1.15 – 4.75"),
    ("Michael Smith – Rob Owen", "2.15 – 1.65"),
    ("Damon Heta – Alex Fehlmann", "1.04 – 9.00"),
    ("Kevin Doets – Nick Kenny", "1.24 – 3.75"),
])}
<h3><strong>Wat verwachten de tipsters voor het hele toernooi?</strong></h3>
<p>Zonder Luke Littler is Luke Humphries de favoriet voor de eindzege. Bij Britse tipsters vallen ook Ross Smith en Luke Woodhouse op, die vorig jaar nog de finale in Basel haalde. Onze eigen voorspelling voor het toernooi, met Humphries als winnaar en Gian van Veen als finalist, staat in onze <a href="/nieuws/swiss-darts-trophy-2026">voorbeschouwing</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint de Swiss Darts Trophy vandaag?</strong><br>De middagsessie begint om 13:00 uur met Zonneveld – Brooks. De avondsessie start om 19:00 uur en eindigt met Doets – Kenny.</p>
<p><strong>Wat is de beste wedtip voor vandaag?</strong><br>Onze favoriete tip is Raymond van Barneveld die wint van Maik Kuivenhoven, tegen een odd van 2.00.</p>
<p><strong>Kun je wedden op 180's bij darts?</strong><br>Ja. De meeste bookmakers bieden markten op het totaal aantal 180's, wie de meeste 180's gooit en wie de eerste 180 gooit.</p>
<p><strong>Wat betekent een leg handicap van -2,5?</strong><br>De speler moet met minstens drie legs verschil winnen; in een best of 11 dus met 6-3 of ruimer.</p>
<p><em>24+ | Gokken is alleen toegestaan voor personen van 18 jaar en ouder. Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_DARTS,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting"); sys.exit()
    print("item:", WF.create_live(fd))
