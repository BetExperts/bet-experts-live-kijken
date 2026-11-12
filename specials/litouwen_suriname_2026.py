# -*- coding: utf-8 -*-
"""Los artikel: Litouwen – Suriname live kijken (oefeninterland, donderdag 12 november 2026, 18:00 NL, Kaunas).
Zoekwoorden: Litouwen Suriname live kijken, Suriname live stream, Natio live kijken, Litouwen – Suriname zender, hoe laat.
Feiten: specials/litouwen_suriname_2026_feiten.md (lff.lt, LRT-programmaschema + stream-API 12-11 15:00 vanaf NL-IP,
SR Herald / Culturu / Sun.sr selectie, NOS + SVB bondscoach Fraser, Circus-odds 12-11 15:05, eigen Bet365-schema van 4-11:
wedstrijd staat er niet in -> geen Bet365-stream beloven; eigenaar: misschien later bij Bet365, wel live te volgen via de
live-tracker). Bewust weggelaten: club Piroe (bronnen tegenstrijdig), scheidsrechter, exacte LRT-blokkade (niet vooraf te
controleren -> voorzichtig geformuleerd). Geen illegale streams. Slug 404 gecontroleerd 12-11.
  python3 specials/litouwen_suriname_2026.py   (dry run)
  publiceren: specials/concept_publiceer.py litouwen_suriname_2026 --live"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "litouwen-suriname-live-kijken"
RUBRIEK = "64ff0fbd5a8f205b05d5468f"   # Voetbal (rubriek van de voorbeschouwingen)
TITEL = "Litouwen – Suriname live kijken: zender, stream en tijd"
SAMENVATTING = ("Litouwen – Suriname live kijken? De oefeninterland begint donderdag om 18:00 uur in Kaunas. "
                "Waar je het duel kunt volgen en hoe laat.")
BET365 = "https://www.bet-experts.nl/go/bet365"
ODDS = (2.85, 3.10, 2.50)   # Circus, 12-11 15:05: Litouwen, gelijk, Suriname

L = {"bet365": '<a href="/bookmakers/bet365">Bet365</a>',
     "circus": '<a href="/bookmakers/circus">Circus</a>',
     "suriname": '<a href="/clubs/suriname">Suriname</a>',
     "litouwen": '<a href="/clubs/litouwen">Litouwen</a>',
     "kijken": '<a href="/live-kijken">live kijken</a>',
     "curacao": '<a href="/nieuws/curacao-panama-live-gratis-kijken-13-11-2026">Curaçao – Panama live kijken</a>',
     "legaal": '<a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>'}


def o(x):
    return f"{x:.2f}".replace(".", ",")


content = f"""<p><strong>Litouwen – Suriname is een oefeninterland op donderdag 12 november 2026 om 18:00 uur Nederlandse tijd, in het S. Darius en S. Girėnas-stadion in Kaunas. Een Nederlandse tv-zender zendt de wedstrijd niet uit. De Litouwse publieke omroep LRT zet het duel wel live op LRT.lt, maar die stream kan buiten Litouwen geblokkeerd zijn. Bij {L['bet365']} kun je de wedstrijd in elk geval live volgen met de live-tracker en live meewedden.</strong></p>
<p>Voor veel Nederlanders is dit een interessante wedstrijd: in de selectie van Suriname staan spelers van onder meer Feyenoord, NEC, Heracles, FC Utrecht, Fortuna Sittard en Go Ahead Eagles. Het is bovendien de eerste ontmoeting ooit tussen beide landen. Eerst was het plan om in een neutraal stadion in Nederland te spelen, maar de bonden werden het niet eens over een stadion. Daarom speelt Natio in Kaunas.</p>
<h3><strong>Litouwen – Suriname: de wedstrijd in het kort</strong></h3>
{tabel(["", "Litouwen – Suriname"], [
    ("Soort wedstrijd", "Oefeninterland"),
    ("Datum", "Donderdag 12 november 2026"),
    ("Aftrap", "18:00 uur Nederlandse tijd (19:00 uur in Litouwen, 14:00 uur in Suriname)"),
    ("Stadion", "S. Darius en S. Girėnas-stadion, Kaunas"),
    ("Nederlandse tv", "Niet te zien"),
    ("Stream", "LRT.lt (mogelijk alleen in Litouwen)"),
    ("Live volgen", "Live-tracker bij Bet365"),
])}
<h3><strong>Op welke zender is Litouwen – Suriname te zien?</strong></h3>
<p>Op geen enkele Nederlandse zender. Ziggo Sport, ESPN, NOS, Viaplay en DAZN hebben de wedstrijd niet op het programma; Ziggo Sport zendt op hetzelfde tijdstip Turkije – België uit. Ook de Surinaamse zenders en de Surinaamse voetbalbond hebben geen uitzending aangekondigd.</p>
<p>De enige uitzending die we vonden, is die van LRT, de publieke omroep van Litouwen. Volgens het programmaschema zet LRT de wedstrijd vanaf 17:45 uur Nederlandse tijd live op de website LRT.lt. Bij deze uitzending staat geen melding dat hij alleen in Litouwen te zien is, maar buitenlandse sportstreams worden vaak geblokkeerd. Of de stream in Nederland werkt, blijkt dus pas vlak voor de aftrap.</p>
<h3><strong>Litouwen – Suriname live volgen bij Bet365</strong></h3>
<p>Ook als er geen beelden zijn, kun je de wedstrijd minuut voor minuut volgen. {L['bet365']} heeft het duel live in zijn aanbod en toont het verloop in een live-tracker: een animatie van het veld met balbezit, aanvallen, schoten, corners en doelpunten, zodat je ziet waar de bal is en welke ploeg drukt. Op het moment van schrijven stond de wedstrijd nog niet in het livestreamschema van Bet365. Komt er alsnog een stream, dan zie je dat in de app of op de site: met saldo op je account (of een weddenschap in de afgelopen 24 uur) kun je dan meekijken.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: volg Litouwen – Suriname live bij Bet365</strong></a></p>"""

content2 = f"""<h3><strong>Suriname: Fraser en een selectie vol Nederlandse namen</strong></h3>
<p>Bondscoach van {L['suriname']} is Henk Fraser, die eind juli Henk ten Cate opvolgde. Het is zijn eerste reeks oefenwedstrijden met Natio. Suriname staat 128e op de wereldranglijst van de FIFA en liep in maart op een haar na het WK 2026 mis: in de halve finale van de intercontinentale play-offs verloor het in Monterrey met 2-1 van Bolivia, nadat Liam van Gelderen Suriname op voorsprong had gezet.</p>
<p>In de selectie zitten vier debutanten: Cheveyo Balentien (19, AC Milan), Neville Ogidi Nwankwo (FC Utrecht), Mannou Berger (Feyenoord) en Sanjeev van Haren (NEC). Sheraldo Becker (Mainz 05), Joël Piroe en Ridgeciano Haps keren terug. Verder staan onder meer Immanuel Pherai (Hamburger SV), Justin Lonwijk (Dynamo Kyiv), Kenneth Paal, Myenty Abena, Shaquille Pinas, Gyrano Kerk, Navajo Bakboord en Liam van Gelderen (RKC), Djevencio van der Kust (Heracles), Shiloh 't Zand (Fortuna Sittard) en Richonell Margaret (Go Ahead Eagles) in de selectie. Doelman Etienne Vaessen ontbreekt door een schorsing en Warner Hahn is geblesseerd.</p>
<h3><strong>Litouwen: nieuwe bondscoach, Nations League in de benen</strong></h3>
<p>{L['litouwen']} staat 149e op de FIFA-ranking en heeft met Mindaugas Čepas een interim-bondscoach, die vandaag debuteert. Hij volgde Edgaras Jankauskas op, die werd ontslagen na een 1-0-nederlaag in Azerbeidzjan. In de Nations League (groep D2) won Litouwen met 2-0 in Liechtenstein en speelde het thuis 1-1 tegen Azerbeidzjan. De bekendste namen zijn middenvelder Gvidas Gineitis (Torino) en Arnas Voitinovičius (Benfica). Maandag speelt Litouwen in de Nations League thuis tegen Liechtenstein.</p>
<h3><strong>Odds Litouwen – Suriname</strong></h3>
{tabel(["Uitslag", "Odd"], [("Litouwen wint", o(ODDS[0])), ("Gelijkspel", o(ODDS[1])), ("Suriname wint", f"<strong>{o(ODDS[2])}</strong>")])}
<p><em>Odds bij {L['circus']}, donderdag 12 november om 15:05 uur. Odds kunnen tot de aftrap nog veranderen.</em></p>
<p>De bookmakers zien Suriname als lichte favoriet, ondanks de uitwedstrijd. Dat is logisch: Suriname staat ruim twintig plaatsen hoger op de wereldranglijst en heeft meer spelers die in Europese topcompetities spelen. Tegelijk is het een oefenduel met een nieuwe bondscoach, vier debutanten en een lange reis, dus de uitslag is lastig te voorspellen. Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit; lees {L['legaal']}.</p>"""

content3 = f"""<h3><strong>Wanneer speelt Suriname weer?</strong></h3>
<p>Na Kaunas reist de selectie naar Nederland. Op zondag 15 november om 18:00 uur speelt Suriname een oefeninterland tegen Eswatini in Stadion De Vliert in Den Bosch, de eerste wedstrijd van Natio in Nederland sinds maart 2024. Ook interessant voor wie van Caribisch voetbal houdt: Curaçao speelt vannacht in de CONCACAF Nations League tegen Panama; lees {L['curacao']}. Alle wedstrijden die je deze week kunt kijken, vind je op onze pagina {L['kijken']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Litouwen – Suriname?</strong><br>Om 18:00 uur Nederlandse tijd, op donderdag 12 november 2026. In Litouwen is het dan 19:00 uur, in Suriname 14:00 uur.</p>
<p><strong>Op welke zender is Litouwen – Suriname?</strong><br>Niet op de Nederlandse tv. De Litouwse omroep LRT zet de wedstrijd live op LRT.lt, maar die stream kan buiten Litouwen geblokkeerd zijn.</p>
<p><strong>Kan ik Litouwen – Suriname live volgen?</strong><br>Ja, bij Bet365 volg je het duel live via de live-tracker, met balbezit, aanvallen, schoten en doelpunten.</p>
<p><strong>Waar wordt Litouwen – Suriname gespeeld?</strong><br>In het S. Darius en S. Girėnas-stadion in Kaunas, de tweede stad van Litouwen.</p>
<p><strong>Wie is de bondscoach van Suriname?</strong><br>Henk Fraser. Hij volgde eind juli 2026 Henk ten Cate op.</p>
<p><strong>Tegen wie speelt Suriname zondag?</strong><br>Tegen Eswatini, op zondag 15 november om 18:00 uur in Stadion De Vliert in Den Bosch.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    alles = content + content2 + content3
    w = len(re.sub(r"<[^>]+>", " ", alles).split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", w, "woorden")
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert 149 - 128 > 20
    assert "<h2" not in alles and "<h4" not in alles and "betcity" not in alles.lower() and "waaroptv" not in alles.lower()
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles) and alles.count(BET365) == 1
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/") or href == BET365, href
    print("dry run ok")
