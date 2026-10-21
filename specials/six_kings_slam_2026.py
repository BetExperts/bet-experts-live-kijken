# -*- coding: utf-8 -*-
"""Los artikel: Six Kings Slam 2026 (verplaatst naar 27-30 december). Feiten nagelopen op 21-10-2026 (Al Jazeera/AFP,
Gulf News, Sky Sports, NOS, Tennis Majors, ATP, Ziggo, Wikipedia, arenahub). Nog geen odds beschikbaar: aanvullen zodra
bookmakers markten openen.
  python3 specials/six_kings_slam_2026.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Six Kings Slam 2026: uitgesteld naar december, spelers, schema, prijzengeld en waar je kijkt"
SLUG = "six-kings-slam-2026"
SAMENVATTING = ("De Six Kings Slam 2026 is verplaatst naar 27-30 december. Spelers, loting, tijden, prijzengeld, "
                "favorieten en waar je kijkt.")
RUBRIEK_TENNIS = "665715dbf1f3cbdf7f874d79"
COMPETITIE_SKS = "68f1f95e07965f31dc1401b2"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>De Six Kings Slam 2026 gaat niet in oktober door. De organisatie in Saudi-Arabië heeft het tennistoernooi met de grootste prijzenpot ter wereld verplaatst naar 27 tot en met 30 december 2026. Titelhouder Jannik Sinner doet niet mee: hij is geblesseerd en wordt vervangen door Learner Tien. Carlos Alcaraz, Novak Djokovic, Alexander Zverev, Taylor Fritz, Alex de Minaur en Tien strijden om 6 miljoen dollar voor de winnaar. In Nederland kijk je live via Netflix.</strong></p>
<p>Oorspronkelijk zou de derde editie van de Six Kings Slam op 21 oktober beginnen in Riyad. Op 14 oktober maakte de organisatie bekend dat het toernooi naar eind december schuift. Hieronder lees je alles over de nieuwe data, het speelschema in Nederlandse tijd, de loting, het prijzengeld, waar je het live ziet en wie volgens ons de favorieten zijn.</p>
<h3><strong>Wat is de Six Kings Slam?</strong></h3>
<p>De Six Kings Slam is een exhibitietoernooi voor zes van de beste tennissers ter wereld. Het wordt georganiseerd door de Saudische General Entertainment Authority als onderdeel van Riyadh Season en wordt gespeeld in de ANB Arena in Riyad, een speciaal voor het evenement gebouwde arena met zo'n 8.000 plaatsen. De eerste editie was in 2024.</p>
<p>Omdat het een exhibitie is, staat het toernooi niet op de officiële ATP-kalender. Er zijn geen rankingpunten te verdienen en de uitslagen tellen niet mee voor de officiële onderlinge statistieken. Wat het toernooi zo bijzonder maakt, is het geld: de winnaar verdient meer dan de winnaar van een grandslamtoernooi.</p>
<h3><strong>Waarom is de Six Kings Slam uitgesteld?</strong></h3>
<p>Volgens de organisatie is het toernooi verplaatst vanwege "organisatorische en logistieke uitdagingen" en de mogelijke gevolgen voor de ervaring van bezoekers. Turki Alalshikh, voorzitter van de General Entertainment Authority, maakte het nieuws op 14 oktober bekend. Internationale media brengen het uitstel in verband met de aanvallen op het vliegveld van Riyad begin oktober, maar de organisatie zelf noemt die reden niet. Gekochte tickets blijven geldig voor de nieuwe data.</p>
<h3><strong>Six Kings Slam 2026: data en speelschema</strong></h3>
{tabel(["Datum", "Ronde", "Wedstrijden"], [
    ("Zondag 27 december", "Kwartfinales", "Alexander Zverev – Taylor Fritz<br>Learner Tien – Alex de Minaur"),
    ("Maandag 28 december", "Halve finales", "Carlos Alcaraz – winnaar Zverev/Fritz<br>Novak Djokovic – winnaar Tien/De Minaur"),
    ("Dinsdag 29 december", "Rustdag", "-"),
    ("Woensdag 30 december", "Troostfinale en finale", "Strijd om de derde plaats, daarna de finale"),
])}
<p>Alle wedstrijden worden gespeeld over twee gewonnen sets. Tussen de halve finales en de finale zit een rustdag, omdat de ATP-regels niet toestaan dat een exhibitie drie dagen achter elkaar wordt gespeeld.</p>
<h3><strong>Hoe laat speelt de Six Kings Slam (Nederlandse tijd)?</strong></h3>
<p>In december geldt in Nederland de wintertijd, waardoor het in Riyad twee uur later is dan bij ons. Volgens de arena opent de zaal om 15:30 uur Nederlandse tijd en begint de eerste wedstrijd van de avond om 17:30 uur. De tweede wedstrijd volgt na afloop van de eerste, meestal rond 19:30 tot 20:00 uur. De organisatie heeft de exacte volgorde van de wedstrijden nog niet bekendgemaakt; we werken dit bij zodra het definitieve schema bekend is.</p>
<p><em>Ter vergelijking: vorig jaar begonnen de avonden om 18:30 uur Nederlandse tijd, maar toen gold nog de zomertijd.</em></p>"""

content2 = f"""<h3><strong>De spelers van de Six Kings Slam 2026</strong></h3>
<p>Het deelnemersveld werd in juli bekendgemaakt. Alex de Minaur verving toen Stefanos Tsitsipas, en op 6 oktober meldde Jannik Sinner zich af met een knieblessure. Zijn plek is ingenomen door de 20-jarige Amerikaan Learner Tien. Of alle zes de spelers ook op de nieuwe data in december aantreden, heeft de organisatie nog niet bevestigd.</p>
{tabel(["Speler", "Land", "ATP-ranking", "Grandslamtitels", "Bijzonderheid"], [
    ("Alexander Zverev", "Duitsland", "2", "2", "Won in 2026 Roland Garros en de US Open"),
    ("Carlos Alcaraz", "Spanje", "3", "7", "Twee keer finalist, bye naar de halve finale"),
    ("Alex de Minaur", "Australië", "8", "0", "Debuut op de Six Kings Slam"),
    ("Novak Djokovic", "Servië", "12", "24", "Bye naar de halve finale"),
    ("Taylor Fritz", "Verenigde Staten", "14", "0", "Werd vorig jaar derde"),
    ("Learner Tien", "Verenigde Staten", "18", "0", "Vervanger van Sinner, linkshandig"),
])}
<p><em>ATP-ranking van 19 oktober 2026.</em></p>
<p><strong>Waarom krijgen Alcaraz en Djokovic een bye?</strong> De twee spelers met de meeste grandslamtitels slaan de kwartfinales over en stromen direct in in de halve finale. Daardoor spelen zij minimaal twee wedstrijden: de halve finale en de finale of de troostfinale.</p>
<h3><strong>Waarom speelt Jannik Sinner niet mee?</strong></h3>
<p>Sinner, winnaar van de edities in 2024 en 2025, kampt met een blessure aan zijn rechterknie. Hij miste daardoor ook de US Open, de toernooien in Beijing en Shanghai en de ATP Finals. Zonder de titelhouder krijgt de Six Kings Slam dit jaar sowieso een nieuwe winnaar.</p>
<h3><strong>Prijzengeld Six Kings Slam 2026</strong></h3>
{tabel(["Onderdeel", "Bedrag"], [
    ("Startgeld per speler", "1,5 miljoen dollar (gegarandeerd)"),
    ("Extra voor de winnaar", "4,5 miljoen dollar"),
    ("Totaal voor de winnaar", "6 miljoen dollar"),
    ("Totale prijzenpot", "13,5 miljoen dollar"),
])}
<p>Met 6 miljoen dollar verdient de winnaar van een toernooi van drie wedstrijddagen meer dan de winnaar van een grandslam. Vorig jaar kreeg Sinner daarbij ook een massief gouden racket van ongeveer vier kilo. Of er dit jaar weer zo'n racket wordt uitgereikt, is nog niet bekend.</p>
<h3><strong>Six Kings Slam kijken in Nederland</strong></h3>
<p>De Six Kings Slam is in Nederland live te zien op <strong>Netflix</strong>, zonder extra kosten bovenop je abonnement. Volgens Ziggo zijn alle wedstrijden van 27 tot en met 30 december live te zien en kun je ze daarna terugkijken. Heb je Netflix via Ziggo, dan kijk je gewoon via je tv-ontvanger. Andere zenders zoals Ziggo Sport, Eurosport of de NOS hebben geen uitzendrechten.</p>
<h3><strong>Winnaars van de Six Kings Slam</strong></h3>
{tabel(["Jaar", "Winnaar", "Finale", "Derde plaats"], [
    ("2024", "Jannik Sinner", "Sinner – Alcaraz 6-7(5) 6-3 6-3", "Djokovic won van Nadal"),
    ("2025", "Jannik Sinner", "Sinner – Alcaraz 6-2 6-4", "Fritz won van Djokovic (opgave)"),
    ("2026", "Nog te spelen", "30 december", "30 december"),
])}
<p>In 2024 nam Rafael Nadal in Riyad afscheid van het grote publiek; hij kreeg toen een gouden racket als eerbetoon. Alcaraz stond beide keren in de finale, maar verloor telkens van Sinner.</p>"""

content3 = f"""<h3><strong>Favorieten voor de Six Kings Slam 2026</strong></h3>
<p>Bookmakers hebben na het uitstel nog geen markten geopend; zodra er odds zijn, zetten we ze hier. Op basis van vorm, ervaring en de loting zien wij dit als de rangorde:</p>
<p><strong>1. Carlos Alcaraz.</strong> De logische favoriet. Hij won dit jaar de Australian Open, stond twee keer in de finale van de Six Kings Slam en heeft door de bye maar twee wedstrijden nodig voor de titel. Wel miste hij een groot deel van het seizoen met een polsblessure en ging hij in Shanghai al vroeg onderuit.</p>
<p><strong>2. Alexander Zverev.</strong> De nummer twee van de wereld beleeft het beste jaar van zijn loopbaan, met titels op Roland Garros en de US Open. Hij moet wel via de kwartfinale tegen Fritz, tegen wie hij een negatieve onderlinge balans heeft (6-10), al won hij dit jaar op Wimbledon overtuigend.</p>
<p><strong>3. Novak Djokovic.</strong> De 24-voudig grandslamwinnaar won begin oktober nog het toernooi in Beijing en krijgt eveneens een bye. In Riyad verloor hij de vorige twee keer wel van Sinner in de halve finale. Tegen De Minaur staat hij 4-1 voor; tegen Tien speelde hij nog niet officieel.</p>
<p><strong>Outsiders:</strong> Taylor Fritz (vorig jaar derde, won toen van Zverev), Alex de Minaur (finalist in Beijing, maar kampte daar met een liesblessure) en Learner Tien, het jonge talent dat als vervanger instroomt.</p>
<p><strong>Mogelijke finale:</strong> Alcaraz tegen Djokovic zou de affiche zijn waar de organisatie op hoopt. Hun onderlinge balans staat op 5-5, na de finale van de Australian Open 2026 die Alcaraz in vier sets won.</p>
<h3><strong>Vorm van de spelers in oktober</strong></h3>
{tabel(["Speler", "Recente resultaten"], [
    ("Alexander Zverev", "Halve finale Shanghai Masters"),
    ("Carlos Alcaraz", "Uitgeschakeld in de tweede ronde van Shanghai (tegen Bergs)"),
    ("Novak Djokovic", "Won de China Open in Beijing, verloor daarna direct in Shanghai"),
    ("Alex de Minaur", "Finale Beijing (opgave), kwartfinale Shanghai"),
    ("Taylor Fritz", "Verloor in Shanghai van Tsitsipas"),
    ("Learner Tien", "Verloor in Shanghai van Ruud"),
])}
<h3><strong>Kritiek op de Six Kings Slam</strong></h3>
<p>Het toernooi is niet onomstreden. Mensenrechtenorganisaties zoals Amnesty International zien Saudische sportevenementen als sportswashing: het gebruik van sport om het imago van het land op te poetsen. Tegelijk groeit de band tussen het tennis en Saudi-Arabië: het staatsinvesteringsfonds PIF is naamgever van de ATP-ranglijst en vanaf 2028 komt er een Masters 1000-toernooi in het land. Door de verplaatsing naar eind december eindigt de Six Kings Slam bovendien net voor de start van het nieuwe tennisseizoen, met de United Cup op 1 januari.</p>
<h3><strong>Geen Nederlanders in Riyad</strong></h3>
<p>Er doet geen Nederlander mee aan de Six Kings Slam. De beste Nederlander op de ranglijst, Botic van de Zandschulp, haalde onlangs de achtste finales van het Masters-toernooi in Shanghai. Onze dagelijkse tennistips vind je bij de <a href="/tennis-voorspellingen-vandaag">tennis voorspellingen van vandaag</a>, en alles over het toernooi op de pagina van de <a href="/competities/six-kings-slam">Six Kings Slam</a>.</p>
<h3><strong>Veelgestelde vragen over de Six Kings Slam</strong></h3>
<p><strong>Wanneer is de Six Kings Slam 2026?</strong><br>Van zondag 27 tot en met woensdag 30 december 2026, met dinsdag 29 december als rustdag. Het toernooi stond eerst gepland voor 21 tot en met 24 oktober.</p>
<p><strong>Waarom is de Six Kings Slam verplaatst?</strong><br>Volgens de organisatie om organisatorische en logistieke redenen. Media brengen het in verband met de veiligheidssituatie in Riyad.</p>
<p><strong>Waarom speelt Sinner niet mee aan de Six Kings Slam?</strong><br>Jannik Sinner heeft een knieblessure en heeft zich op 6 oktober afgemeld. Learner Tien neemt zijn plek in.</p>
<p><strong>Hoeveel verdient de winnaar van de Six Kings Slam?</strong><br>6 miljoen dollar: 1,5 miljoen startgeld plus 4,5 miljoen dollar extra. Iedere deelnemer krijgt minimaal 1,5 miljoen dollar.</p>
<p><strong>Waar kan ik de Six Kings Slam kijken?</strong><br>In Nederland live op Netflix, zonder extra kosten. Ook via Netflix op Ziggo.</p>
<p><strong>Hoe laat beginnen de wedstrijden?</strong><br>De eerste wedstrijd van elke avond begint naar verwachting om 17:30 uur Nederlandse tijd, de tweede rond 19:30 tot 20:00 uur. Het definitieve schema volgt.</p>
<p><strong>Telt de Six Kings Slam mee voor de ATP-ranking?</strong><br>Nee. Het is een exhibitietoernooi zonder rankingpunten.</p>
<p><strong>Wie won de Six Kings Slam in 2024 en 2025?</strong><br>Beide keren Jannik Sinner, telkens in de finale tegen Carlos Alcaraz.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_TENNIS, "competitie": COMPETITIE_SKS, "tennis": True,
          "datum-tijd-van-wedstrijd": "2026-12-27T16:30:00.000Z",
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        import re
        tekst = re.sub(r"<[^>]+>", " ", content + content2 + content3)
        print(len(SAMENVATTING), "tekens samenvatting |", len(tekst.split()), "woorden"); sys.exit()
    print("item:", WF.create_live(fd))
