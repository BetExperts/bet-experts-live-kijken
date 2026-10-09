# -*- coding: utf-8 -*-
"""Los artikel: Schaatskalender 2026/2027 (langebaan + shorttrack). Internationale data gecontroleerd met de
ISU-kalenders 2026/27; nationale data (KNSB) en tv-afspraken uit de aangeleverde info (9 okt 2026).
  python3 specials/schaatskalender_2026_2027.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Schaatskalender 2026/2027: alle belangrijke wedstrijden op de langebaan en in het shorttrack"
SLUG = "schaatskalender-2026-2027"
SAMENVATTING = ("Van het kwalificatietoernooi in Thialf tot het WK shorttrack in Seoel: alle wereldbekers, EK's, WK's en "
                "NK's van 2026/2027 en waar je kijkt.")
RUBRIEK_NIEUWS = "651be5190a7dba016817ccf0"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in koppen)
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}><thead><tr>{kop}</tr></thead><tbody>{body}</tbody></table>"


NL = "🇳🇱 "

content = f"""<p><strong>Het schaatsseizoen 2026/2027 begint op vrijdag 30 oktober met het kwalificatietoernooi in Thialf en eindigt op zondag 14 maart 2027 met het WK shorttrack in Seoel. Op de langebaan staan zes wereldbekers, het EK in Heerenveen en het WK afstanden in Peking op het programma. De shorttrackers rijden zeven World Tour-wedstrijden, het EK in Dresden en het WK in Seoel. Alles is in Nederland te zien bij de NOS.</strong></p>
<p>Het is de eerste winter na de Olympische Spelen van Milaan en Cortina, en dat is te merken. Sommige toppers nemen afstand, andere schaatsers krijgen juist de kans om zich te laten zien. In deze kalender vind je alle belangrijke wedstrijden op een rij, met de toernooien in Nederland, de grootste veranderingen van dit seizoen en waar je alles live kunt volgen.</p>
<h3><strong>De hoogtepunten van het seizoen</strong></h3>
<ul><li><strong>30 oktober – 1 november:</strong> kwalificatietoernooi in Thialf, de start van het seizoen</li><li><strong>4 – 6 december:</strong> wereldbeker in Heerenveen</li><li><strong>8 – 10 januari:</strong> EK allround en sprint in Heerenveen</li><li><strong>12 – 14 februari:</strong> World Tour shorttrack in Tilburg</li><li><strong>25 – 28 februari:</strong> WK afstanden in Peking</li><li><strong>12 – 14 maart:</strong> WK shorttrack in Seoel, de afsluiter van de winter</li></ul>
<h3><strong>Kalender langebaanschaatsen 2026/2027</strong></h3>
{tabel(["Datum", "Wedstrijd", "Plaats"], [
    ("30 okt – 1 nov 2026", "Kwalificatietoernooi wereldbeker", NL + "Heerenveen"),
    ("13 – 15 nov 2026", "Wereldbeker 1", "Peking, China"),
    ("20 – 22 nov 2026", "Wereldbeker 2", "Obihiro, Japan"),
    ("4 – 6 dec 2026", "Wereldbeker 3", NL + "Heerenveen"),
    ("11 – 13 dec 2026", "Wereldbeker 4", "Stavanger, Noorwegen"),
    ("27 – 28 dec 2026", "NK allround en sprint", NL + "Heerenveen"),
    ("8 – 10 jan 2027", "EK allround en sprint", NL + "Heerenveen"),
    ("22 – 24 jan 2027", "NK afstanden", NL + "Heerenveen"),
    ("29 – 31 jan 2027", "Wereldbeker 5", "Salt Lake City, Verenigde Staten"),
    ("5 – 7 feb 2027", "Wereldbeker 6", "Calgary, Canada"),
    ("25 – 28 feb 2027", "WK afstanden", "Peking, China"),
])}
<h3><strong>Kalender shorttrack 2026/2027</strong></h3>
{tabel(["Datum", "Wedstrijd", "Plaats"], [
    ("23 – 25 okt 2026", "World Tour 1", "Vancouver, Canada"),
    ("30 okt – 1 nov 2026", "World Tour 2", "Montreal, Canada"),
    ("20 – 22 nov 2026", "World Tour 3", "Seoel, Zuid-Korea"),
    ("27 – 29 nov 2026", "World Tour 4", "Shanghai, China"),
    ("4 – 6 dec 2026", "World Tour 5", "Peking, China"),
    ("2 – 3 jan 2027", "NK shorttrack", NL + "Leeuwarden"),
    ("15 – 17 jan 2027", "EK shorttrack", "Dresden, Duitsland"),
    ("5 – 7 feb 2027", "World Tour 6", "Gdansk, Polen"),
    ("12 – 14 feb 2027", "World Tour 7", NL + "Tilburg"),
    ("12 – 14 mrt 2027", "WK shorttrack", "Seoel, Zuid-Korea"),
])}"""

content2 = """<h3><strong>Schaatsen in Nederland: Thialf, Leeuwarden en Tilburg</strong></h3>
<p>Wie een wedstrijd live wil zien, kan deze winter vaak in eigen land terecht. Thialf in Heerenveen is weer het middelpunt van de langebaan. Het seizoen opent er met het kwalificatietoernooi, waar de Nederlandse schaatsers strijden om de startbewijzen voor de eerste wereldbekers. In december volgt de enige Nederlandse wereldbeker. Rond de jaarwisseling zijn het NK allround en sprint, en begin januari strijden de beste Europeanen om de EK-titels. Eind januari staat het NK afstanden op het programma, waar ook de plekken voor het WK te verdienen zijn.</p>
<p>De shorttrackers hebben twee Nederlandse afspraken. Begin januari is het NK in Leeuwarden, en half februari komt de World Tour naar Tilburg. Tilburg is de afgelopen jaren uitgegroeid tot de vaste Nederlandse plek voor internationale shorttrackwedstrijden.</p>
<h3><strong>Wat is er nieuw dit seizoen?</strong></h3>
<p><strong>Geen Jutta Leerdam.</strong> De olympisch kampioene op de 1000 meter, die in Milaan ook zilver won op de 500 meter, rijdt deze winter geen wedstrijden. Ze maakte dat zelf bekend, maar wil nog niet spreken van een definitief afscheid. Bij de vrouwensprint is daardoor meer ruimte voor andere namen.</p>
<p><strong>Twijfel bij Femke Kok.</strong> Ook Femke Kok, wereldrecordhouder op de 500 meter, staat niet te springen. Half september gaf ze aan dat de zin om weer wedstrijden te rijden nog niet echt terug was. Het is dus afwachten hoe snel zij in vorm komt.</p>
<p><strong>Discussie over de WK-selectie.</strong> Omdat de kalender krap is, wil de KNSB de beste rijders voor het WK afstanden beschermen en terug naar een vorm van voorselectie. Zo hoeven toppers zich niet in elk toernooi opnieuw te bewijzen. Niet iedereen is daar blij mee: topcoach Jac Orie liet weten dat hij het een stap terug vindt en verwacht dat de discussie over eerlijke selectie dan weer opnieuw begint.</p>
<p><strong>Een volle agenda in Azië en Noord-Amerika.</strong> Langebaanschaatsers reizen in november van Peking naar Obihiro. Na de jaarwisseling volgen twee wereldbekers in Salt Lake City en Calgary, waar op de snelle hooglandbanen vaak records sneuvelen. Het WK afstanden gaat daarna terug naar Peking. Shorttrackers beginnen het seizoen al eind oktober in Canada.</p>"""

content3 = """<h3><strong>Langebaanschaatsen kijken in Nederland</strong></h3>
<p>De NOS zendt het langebaanschaatsen uit. Met de KNSB sloot de omroep in september een akkoord voor vier jaar over de Nederlandse wedstrijden, zoals het kwalificatietoernooi en de NK's. Ook de wereldbekers, het EK en het WK zijn dit seizoen bij de NOS te zien.</p>
<p>Alle wedstrijden zijn live te volgen via nos.nl en de NOS-app. Op televisie staat het schaatsen meestal op NPO 1, soms op NPO 2 of NPO 3. Bij het kwalificatietoernooi is de vrijdag op NPO 3 te zien en de zaterdag en zondag op NPO 1. Meer over de zender lees je op onze <a href="/zenders/nos">NOS-pagina</a>.</p>
<h3><strong>Shorttrack kijken in Nederland</strong></h3>
<p>Ook het shorttrack is bij de NOS te zien: de World Tour, het EK en het WK. Online kun je alle wedstrijden volgen via nos.nl en de NOS-app. Een deel van de races wordt daarnaast op NPO 1 of NPO 3 uitgezonden. Het NK in Leeuwarden valt onder de afspraken tussen de NOS en de KNSB. Let op de tijden: de wedstrijden in Azië en Canada vallen voor Nederlandse kijkers vaak 's nachts of vroeg in de ochtend.</p>
<p>Wil je weten welke sportzender op welk kanaalnummer zit? Dat zie je in ons <a href="/nieuws/sportzenders-kanaalnummers">overzicht van sportzenders en kanaalnummers</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wanneer begint het schaatsseizoen 2026/2027?</strong><br>Op vrijdag 30 oktober 2026 met het kwalificatietoernooi in Thialf in Heerenveen. De shorttrackers beginnen al op 23 oktober met de World Tour in Vancouver.</p>
<p><strong>Waar is het WK afstanden 2027?</strong><br>In Peking, van 25 tot en met 28 februari 2027.</p>
<p><strong>Wanneer is de wereldbeker in Heerenveen?</strong><br>Van 4 tot en met 6 december 2026 in Thialf.</p>
<p><strong>Waar is het EK schaatsen 2027?</strong><br>Het EK allround en sprint is van 8 tot en met 10 januari 2027 in Heerenveen. Het EK shorttrack is van 15 tot en met 17 januari in Dresden.</p>
<p><strong>Rijdt Jutta Leerdam dit seizoen?</strong><br>Nee, de olympisch kampioene op de 1000 meter rijdt in 2026/2027 geen wedstrijden.</p>
<p><strong>Waar kan ik schaatsen kijken?</strong><br>Bij de NOS: live via nos.nl en de NOS-app, en op televisie meestal op NPO 1, soms op NPO 2 of NPO 3.</p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_NIEUWS,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting"); sys.exit()
    print("item:", WF.create_live(fd))
