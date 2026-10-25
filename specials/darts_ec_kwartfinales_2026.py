# -*- coding: utf-8 -*-
"""Los artikel: darts vandaag, voorspellingen en wedtips kwartfinales PDC European Championship 2026 (zo 25 oktober,
Westfalenhallen Dortmund). Tips en odds: Jaspers Bet365-betslip (25-10, 03:38): Smith – Woodhouse 2+ 100+ finishes
in de wedstrijd @1,53; Bet Builder Price wint + 1+ 100+ finish Price @1,86; Clayton -1,5 legs @1,57; Littler -4,5 legs
@1,57; combinatie €15 -> €106,18 (Bet Builder+). Feiten (25-10): dartsnews.com (uitslagen + averages R1/R2, formaat,
prijzengeld, titelverdediger Van Veen), cswdarts.co.uk (uitslagen), pdc-europe.tv (sessies 13:00 en 19:00, Viaplay NL),
Wikipedia 2025 European Championship (Van Veen 11-10 Humphries; Ross Smith winnaar 2022).
  python3 specials/darts_ec_kwartfinales_2026.py   (dry run)
  kaart: og_kaarten/darts_ec.py, publiceren: specials/concept_publiceer.py darts_ec_kwartfinales_2026 --live"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

TITEL = "Darts vandaag: voorspellingen en wedtips (25 oktober)"
SLUG = "darts-vandaag-voorspellingen-wedtips-european-championship-25-oktober-2026"
SAMENVATTING = ("Darts vandaag: de kwartfinales van het European Championship in Dortmund. Speeltijden, vorm, onze vier "
                "wedtips als single en de combinatie.")
RUBRIEK = "66b726271e317999159d5d44"   # rubriek van de darts-artikelen
BET365 = "https://www.bet-experts.nl/go/bet365"

# (tijd NL, speler 1, speler 2, tip, odd)  odds Bet365, zo 25-10
TIPS = [
    ("13:15", "Ross Smith", "Luke Woodhouse", "2 of meer 100+ finishes in de wedstrijd", 1.53),
    ("14:15", "Gerwyn Price", "Stephen Bunting", "Bet Builder: Price wint én gooit 1+ 100+ finish", 1.86),
    ("15:15", "Martin Schindler", "Jonny Clayton", "Jonny Clayton -1,5 legs", 1.57),
    ("16:15", "Krzysztof Ratajski", "Luke Littler", "Luke Littler -4,5 legs", 1.57),
]
INZET, UITBETALING = 15, 106.18


def q(x):
    return f"{x:.2f}".replace(".", ",")


content = f"""<p><strong>Darts vandaag: op zondag 25 oktober staan de kwartfinales van het PDC European Championship op het programma in de Westfalenhallen in Dortmund. Vanaf 13:00 uur spelen Ross Smith – Luke Woodhouse, Gerwyn Price – Stephen Bunting, Martin Schindler – Jonny Clayton en Krzysztof Ratajski – Luke Littler. 's Avonds volgen vanaf 19:00 uur de halve finales en de finale. Onze vier wedtips: twee of meer 100+ finishes bij Smith – Woodhouse, Price wint met minstens één 100+ finish, Clayton -1,5 legs en Littler -4,5 legs.</strong></p>
<p>Titelverdediger Gian van Veen is er niet meer bij: hij verloor zaterdag met 6-10 van Luke Woodhouse. Ook alle andere Nederlanders zijn uitgeschakeld. Hieronder vind je het programma van vandaag, de vorm van alle acht spelers en onze tips, los en als combinatie bij <a href="/bookmakers/bet365">Bet365</a>.</p>
<h3><strong>Darts vandaag: het programma van zondag 25 oktober</strong></h3>
{tabel(["Tijd (NL)", "Wedstrijd", "Ronde"], [
    ("13:15", "Ross Smith – Luke Woodhouse", "Kwartfinale"),
    ("14:15", "Gerwyn Price – Stephen Bunting", "Kwartfinale"),
    ("15:15", "Martin Schindler – Jonny Clayton", "Kwartfinale"),
    ("16:15", "Krzysztof Ratajski – Luke Littler", "Kwartfinale"),
    ("19:00", "Halve finales", "Best of 21 legs"),
    ("Na de halve finales", "Finale", "Best of 21 legs"),
])}
<p><em>De middagsessie begint om 13:00 uur, de avondsessie om 19:00 uur. De tijden per wedstrijd zijn een schatting: loopt een partij uit, dan schuift de rest op. De kwartfinales gaan over best of 19 legs: wie het eerst tien legs wint, gaat door.</em></p>
<h3><strong>Onze 4 darts wedtips van vandaag</strong></h3>
{tabel(["Wedstrijd", "Tip", "Odd"], [(f"{s1} – {s2} ({t})", f"<strong>{tip}</strong>", q(o)) for t, s1, s2, tip, o in TIPS])}
<p><strong>Combinatie:</strong> zet je de vier tips samen in één weddenschap, dan keert Bet365 bij een inzet van €{INZET} in totaal <strong>€{q(UITBETALING)}</strong> uit. Een combinatie levert meer op, maar alle vier de tips moeten dan uitkomen. Speel je liever op zeker, kies dan voor losse tips (singles).</p>
<p><em>Odds van Bet365, gelezen op zondag 25 oktober. Odds kunnen tot de start van een wedstrijd veranderen.</em></p>
<h3><strong>1. Ross Smith – Luke Woodhouse: 2 of meer 100+ finishes (1,53)</strong></h3>
<p>Twee spelers in vorm. Ross Smith, kampioen van dit toernooi in 2022, won met 6-4 van Karel Sedlacek en met 10-7 van Damon Heta (gemiddeld 96,19). Luke Woodhouse is de verrassing van het weekend: na een 6-3 zege op Dirk van Duijvenbode (99,11 gemiddeld) schakelde hij zaterdag titelverdediger Gian van Veen uit met 10-6. Bij een best of 19 worden al snel vijftien legs of meer gespeeld, en met twee spelers die goed scoren is de kans groot dat er minstens twee legs met een finish van honderd of meer worden uitgegooid. Het risico: een snelle, eenzijdige partij met weinig legs.</p>
<h3><strong>2. Gerwyn Price – Stephen Bunting: Price wint én gooit een 100+ finish (1,86)</strong></h3>
<p>Gerwyn Price speelt sterk in Dortmund. De Welshman won met 6-2 van Rob Cross (gemiddeld 99,26) en met 10-4 van Cameron Menzies. Stephen Bunting overleefde in de eerste ronde maar net tegen Danny Noppert (6-5), maar won zaterdag overtuigend met 10-3 van Kim Huybrechts (96,83). Wij verwachten dat Price wint, en in een wedstrijd van minstens tien legs voor hem is één finish van honderd of meer zeer waarschijnlijk. Met deze Bet Builder krijg je een hogere odd dan voor alleen een zege van Price. Het risico: Bunting kan bij zijn beste niveau iedereen kloppen.</p>
<h3><strong>3. Martin Schindler – Jonny Clayton: Clayton -1,5 legs (1,57)</strong></h3>
<p>Met -1,5 legs moet Jonny Clayton met minstens twee legs verschil winnen: elke zege behalve 10-9 is goed. Clayton won met 6-3 van Niko Springer (96,81) en met 10-8 van Josh Rock (98,28). Martin Schindler speelt voor eigen publiek, maar kwam in de eerste ronde maar net langs Wessel Nijman (6-5) en haalde tegen Jermaine Wattimena een gemiddelde van 90,25. Het thuispubliek kan Schindler vleugels geven: dat is het grootste risico.</p>
<h3><strong>4. Krzysztof Ratajski – Luke Littler: Littler -4,5 legs (1,57)</strong></h3>
<p>Luke Littler speelt in Dortmund op een ander niveau dan de rest. Na 6-3 tegen William O'Connor (gemiddeld 105,05) won hij zaterdag met 10-5 van Nathan Aspinall, met een gemiddelde van 114,47. Krzysztof Ratajski won met 6-2 van Dave Chisnall en met 10-8 van Kevin Doets. Met -4,5 legs moet Littler met vijf legs verschil winnen: 10-5 of ruimer. Speelt hij zoals tegen Aspinall, dan is dat haalbaar. Het risico: Ratajski is een ervaren speler die met een sterke dag vijf of zes legs kan pakken.</p>"""

content2 = f"""<h3><strong>De weg naar de kwartfinales: alle uitslagen</strong></h3>
{tabel(["Speler", "Ronde 1 (best of 11)", "Ronde 2 (best of 19)"], [
    ("Ross Smith", "6-4 tegen Karel Sedlacek", "10-7 tegen Damon Heta"),
    ("Luke Woodhouse", "6-3 tegen Dirk van Duijvenbode", "10-6 tegen Gian van Veen"),
    ("Gerwyn Price", "6-2 tegen Rob Cross", "10-4 tegen Cameron Menzies"),
    ("Stephen Bunting", "6-5 tegen Danny Noppert", "10-3 tegen Kim Huybrechts"),
    ("Martin Schindler", "6-5 tegen Wessel Nijman", "10-4 tegen Jermaine Wattimena"),
    ("Jonny Clayton", "6-3 tegen Niko Springer", "10-8 tegen Josh Rock"),
    ("Krzysztof Ratajski", "6-2 tegen Dave Chisnall", "10-8 tegen Kevin Doets"),
    ("Luke Littler", "6-3 tegen William O'Connor", "10-5 tegen Nathan Aspinall"),
])}
<p>Opvallend: alle Nederlanders zijn uitgeschakeld. Michael van Gerwen verloor al in de eerste ronde met 3-6 van Kevin Doets, die zaterdag zelf met 8-10 onderuitging tegen Ratajski. Danny Noppert, Wessel Nijman, Niels Zonneveld, Dirk van Duijvenbode en Jermaine Wattimena strandden ook vroeg, en titelverdediger Gian van Veen haalde de kwartfinales niet.</p>
<h3><strong>European Championship 2026: formaat en prijzengeld</strong></h3>
{tabel(None, [
    ("Locatie", "Westfalenhallen, Dortmund"),
    ("Data", "Donderdag 22 tot en met zondag 25 oktober 2026"),
    ("Deelnemers", "32 spelers"),
    ("Formaat", "Ronde 1 best of 11, ronde 2 en kwartfinales best of 19, halve finales en finale best of 21 legs"),
    ("Prijzengeld", "£750.000 in totaal, £150.000 voor de winnaar"),
    ("Titelverdediger", "Gian van Veen (won in 2025 met 11-10 van Luke Humphries)"),
])}
<h3><strong>Darts vandaag live kijken</strong></h3>
<p>In Nederland is het European Championship live te zien bij Viaplay, met een betaald abonnement. Daarnaast kun je met een account bij <a href="{BET365}">Bet365</a> veel dartstoernooien live streamen. Meer kijkopties voor sport lees je op onze pagina <a href="/live-kijken">live kijken</a>.</p>"""

content3 = """<h3><strong>Wedden op darts: zo werken deze markten</strong></h3>
<p>Bij een <strong>handicap in legs</strong> krijgt een speler een aantal legs achterstand of voorsprong. Bij Littler -4,5 trekt de bookmaker 4,5 leg af van zijn totaal: hij moet dus met vijf legs verschil winnen. Bij <strong>100+ finishes</strong> tel je de keren dat een speler een leg uitgooit met honderd punten of meer. Met een <strong>Bet Builder</strong> combineer je meerdere markten uit één wedstrijd in één weddenschap, zoals de winnaar en een 100+ finish. Meer uitleg over de spelregels lees je in <a href="/nieuws/darts-regels-uitgelegd">de dartsregels uitgelegd</a>.</p>
<p>Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit. Twijfel je? Lees <a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint het darts vandaag?</strong><br>De kwartfinales van het European Championship beginnen om 13:00 uur, de halve finales en de finale om 19:00 uur Nederlandse tijd.</p>
<p><strong>Waar kan ik het European Championship darts kijken?</strong><br>In Nederland bij Viaplay. Met een account bij Bet365 kun je ook veel dartswedstrijden live streamen.</p>
<p><strong>Doet er nog een Nederlander mee?</strong><br>Nee. Alle Nederlanders zijn uitgeschakeld, ook titelverdediger Gian van Veen, die zaterdag met 6-10 verloor van Luke Woodhouse.</p>
<p><strong>Wie is de favoriet voor de titel?</strong><br>Luke Littler. Hij gooide zaterdag een gemiddelde van 114,47 tegen Nathan Aspinall en is bij de bookmakers de favoriet voor de titel.</p>
<p><strong>Hoeveel prijzengeld krijgt de winnaar?</strong><br>De winnaar van het European Championship krijgt £150.000, van een totaal van £750.000.</p>
<p><strong>Wat is de beste darts wedtip van vandaag?</strong><br>Onze favoriet is Luke Littler -4,5 legs tegen Krzysztof Ratajski, met een odd van 1,57 bij Bet365. Een tip blijft een inschatting: zet alleen in wat je kunt missen.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    alles = content + content2 + content3
    tekst = re.sub(r"<[^>]+>", " ", alles)
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", len(tekst.split()), "woorden")
    assert len(TITEL) <= 60 and 120 <= len(SAMENVATTING) <= 155
    assert "<h2" not in alles and "<h4" not in alles and "betcity" not in alles.lower()
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles) and not re.search(r"<(ul|ol)>\s+<", alles)
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/") or href == BET365, href
    print("dry run ok – niets gepubliceerd")
