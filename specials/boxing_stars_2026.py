# -*- coding: utf-8 -*-
"""Los SEO-artikel: Boxing Stars 2026 bij Videoland (schema, deelnemers, tijden, tickets, live kijken). 25-10-2026.
Opzet naar het best scorende artikel ooit (Boxing Influencers 2025: 9.532 kliks): 'schema, programma en waar live kijken
(datum)' + later live bijwerken met uitslagen per Fight Night. Zoekwoorden (Google NL): boxing stars, boxing stars 31 oktober,
boxing stars wanneer, boxing stars videoland, boxing stars 2026, boxing stars deelnemers, boxing stars kijken.
Feiten: specials/boxing_stars_feiten_2026.md (boxing-stars.nl, rtl.nl/boulevard 13-10 en 23-10, Broadcast Magazine 14-10,
videoland.com, nl.wikipedia). Indeling per avond: alleen Roelvink–Platier Luna in de media (De Stentor), de rest volgens
Wikipedia zonder bron -> overal als 'verwacht' gemarkeerd. Geen bookmaker-CTA (rolmodellenverbod; wedden op Boxing Stars kan
niet bij vergunde aanbieders). Edino van Dorsten zonder Ruinerwold (verband niet bevestigd in Boxing Stars-berichten).
  python3 specials/boxing_stars_2026.py   (dry run)
  beelden: og_kaarten/boxing_stars.py; publiceren: specials/concept_publiceer.py boxing_stars_2026 --live"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

TITEL = "Boxing Stars 2026: schema, deelnemers en live kijken (31 oktober)"
SLUG = "boxing-stars-2026-schema-deelnemers-waar-live-kijken-videoland"
SAMENVATTING = ("Boxing Stars 2026 bij Videoland: 12 BN'ers, drie live Fight Nights vanaf 31 oktober om 20:00 uur. Schema, "
                "deelnemers, tickets en live kijken.")
RUBRIEK = "6502b65d49bc032ba533e7a2"   # zelfde rubriek als Boxing Influencers 2025
SCHEMA_URL = os.environ.get("BOXING_SCHEMA_URL", "")   # be-static-URL van og/nieuws/boxing-stars-schema.webp (publiceerstap)

AVONDEN = [
    {"naam": "Fight Night 1", "datum": "za 31 okt", "finale": False, "kort": "Eerste partij in elke poule",
     "duels": [("Mannen zwaargewicht", "Donny Roelvink", "Carlos Platier Luna"),
               ("Vrouwen lichtgewicht", "Priscilla Nasi", "Gaby Blaaser"),
               ("Mannen lichtgewicht", "Eliyha Altena", "Vincent Visser")]},
    {"naam": "Fight Night 2", "datum": "za 7 nov", "finale": False, "kort": "Tweede partij in elke poule",
     "duels": [("Mannen zwaargewicht", "Nesim el Ahmadi", "Edino van Dorsten"),
               ("Vrouwen lichtgewicht", "Beate van der Weide", "Jaimie Vaes"),
               ("Mannen lichtgewicht", "Koen Pieter van Dijk", "Jasha Rudge")]},
    {"naam": "Finale-avond", "datum": "za 14 nov", "finale": True, "kort": "Drie finales: de poulewinnaars", "duels": []},
]
POULES = [
    {"naam": "Mannen zwaargewicht", "sub": "Poule 1",
     "namen": ["Donny Roelvink", "Carlos Platier Luna", "Nesim el Ahmadi", "Edino van Dorsten"]},
    {"naam": "Mannen lichtgewicht", "sub": "Poule 2",
     "namen": ["Eliyha Altena", "Vincent Visser", "Koen Pieter van Dijk", "Jasha Rudge"]},
    {"naam": "Vrouwen lichtgewicht", "sub": "Poule 3",
     "namen": ["Priscilla Nasi", "Gaby Blaaser", "Beate van der Weide", "Jaimie Vaes"]},
]

BI25 = "/nieuws/boxing-influencers-2025-schema-programma-en-waar-live-gratis-kijken-op-tv-in-nederland-zondag-5-oktober-2025"
BI25U = "/nieuws/uitslagen-boxing-influencers-2025---dave-roelvink-kroont-zich-tot-kampioen"


def schema_figuur(url):
    return (f'<figure class="w-richtext-align-fullwidth w-richtext-figure-type-image"><div><img src="{url}" '
            f'alt="Schema Boxing Stars 2026: drie Fight Nights op 31 oktober, 7 november en 14 november bij Videoland, met de drie poules" '
            f'loading="lazy"></div><figcaption>Het schema van Boxing Stars 2026 met alle Fight Nights en poules.</figcaption></figure>')


content = f"""<p><strong>Boxing Stars is terug. Na acht jaar stappen twaalf bekende Nederlanders weer de boksring in, dit keer live bij Videoland. De eerste Fight Night is op zaterdag 31 oktober 2026 om 20:00 uur, daarna volgen 7 november en de finale-avond op 14 november. De avonden vinden plaats in de Mediahaven in Amsterdam en worden gepresenteerd door Monica Geuze en Valerio Zeno. Op de eerste avond maakt Donny Roelvink zijn boksdebuut.</strong></p>
<p>Hieronder vind je het volledige schema, alle deelnemers per poule, wie tegen wie bokst, hoe laat alles begint, hoeveel een ticket kost en hoe je Boxing Stars live kijkt. Tijdens de Fight Nights werken we dit artikel bij met de uitslagen.</p>
<!--SCHEMA-->
<h3><strong>Wat is Boxing Stars?</strong></h3>
<p>Boxing Stars is een bokscompetitie voor bekende Nederlanders. De deelnemers trainen wekenlang onder begeleiding van ervaren trainers en onder toezicht van de Nederlandse Boksbond (NBB), en nemen het daarna live tegen elkaar op in de ring. Het format komt van het Belgische productiehuis De Mensen. In Nederland was het in 2018 al te zien bij RTL 5; nu komt het terug met drie live-uitzendingen bij Videoland, geproduceerd door Signal.Stream.</p>
<h3><strong>Wanneer is Boxing Stars? Datums en tijden</strong></h3>
{tabel(["Avond", "Datum", "Live bij Videoland"], [
    ("<strong>Fight Night 1</strong>", "Zaterdag 31 oktober 2026", "20:00 uur"),
    ("<strong>Fight Night 2</strong>", "Zaterdag 7 november 2026", "20:00 uur"),
    ("<strong>Finale-avond</strong>", "Zaterdag 14 november 2026", "20:00 uur"),
])}
<p>Een uitzending duurt naar verwachting ongeveer anderhalf uur. Rond 22:00 uur is de avond afgelopen, al kan het iets uitlopen.</p>
<h3><strong>Waar is Boxing Stars? Locatie en tickets</strong></h3>
{tabel(None, [
    ("Locatie", "Mediahaven, Moermanskkade 107, Amsterdam (Houthavens)"),
    ("Deuren open", "17:30 uur, met voorprogramma"),
    ("Laatste entree", "18:45 uur (daarna kom je niet meer binnen)"),
    ("Start live-uitzending", "20:00 uur"),
    ("Einde", "Rond 22:00 uur"),
    ("Ticketprijs", "€35 per persoon"),
    ("Inbegrepen", "Toegang, 2 alcoholische drankjes (18+), onbeperkt frisdrank en kleine snacks"),
    ("Kaartverkoop", "Via de officiële site van Boxing Stars en de RTL-pagina van het programma"),
])}
<p>Je ticket is digitaal, met een QR-code: printen is niet nodig. Kom je met de auto, dan is parkeergarage P1 Minervahaven het dichtst in de buurt. Let op: welke partijen er op een avond te zien zijn, kan volgens de organisatie per avond verschillen.</p>"""

if SCHEMA_URL:
    content = content.replace("<!--SCHEMA-->", schema_figuur(SCHEMA_URL))

content2 = f"""<h3><strong>Deelnemers Boxing Stars 2026: alle twaalf BN'ers</strong></h3>
<p>De twaalf deelnemers zijn verdeeld over drie poules van vier: twee mannenpoules en een vrouwenpoule.</p>
<p><strong>Mannen zwaargewicht</strong></p>
{tabel(["Deelnemer", "Bekend van"], [
    ("Donny Roelvink", "Mediapersoonlijkheid, zoon van Dries en broer van Dave Roelvink; Temptation Island VIPS en Expeditie Robinson"),
    ("Carlos Platier Luna", "Winnaar Expeditie Robinson 2017, judoka; bokste ook al mee in Boxing Stars 2018"),
    ("Nesim el Ahmadi", "Comedian, presentator en rapper, de helft van het duo Supergaande"),
    ("Edino van Dorsten", "Spreker en auteur van het boek Mijn naam is Edino"),
])}
<p><strong>Mannen lichtgewicht</strong></p>
{tabel(["Deelnemer", "Bekend van"], [
    ("Eliyha Altena", "Acteur, bekend als Daan in de serie Knokke Off"),
    ("Vincent Visser", "Acteur, bekend van Brugklas en als Valentijn Sanders in GTST"),
    ("Koen Pieter van Dijk", "Presentator, voorheen bekend als Koen Kardashian; Expeditie Robinson 2025"),
    ("Jasha Rudge", "Acteur, onder meer in De leerling en Flikken Rotterdam"),
])}
<p><strong>Vrouwen lichtgewicht</strong></p>
{tabel(["Deelnemer", "Bekend van"], [
    ("Priscilla Nasi", "Dochter van Patty Brard; vervangt de geblesseerde Sylvia Geersen"),
    ("Gaby Blaaser", "Actrice en presentatrice, Sacha in GTST en de Bachelorette van 2020"),
    ("Beate van der Weide", "Contentcreator, bekend van De Bachelor en De Bachelorette 2026"),
    ("Jaimie Vaes", "Styliste en presentatrice, Just Tattoo of Us en Expeditie Robinson 2023"),
])}
<p><strong>Sylvia Geersen doet niet mee.</strong> Het model trok zich op 23 oktober terug met een blessure, nadat ze zichzelf naar eigen zeggen had overtraind. Priscilla Nasi, de dochter van Patty Brard, neemt haar plek in.</p>
<h3><strong>Boxing Stars schema: wie bokst tegen wie?</strong></h3>
<p>Per Fight Night wordt in elke poule één partij gebokst. Op de eerste twee avonden is dus iedere deelnemer één keer aan de beurt. De winnaars van die partijen strijden op 14 november in de finale van hun poule. Zo ziet de indeling er volgens de laatste berichten uit:</p>
{tabel(["Avond", "Poule", "Partij"], [
    (f"<strong>{a['datum'].replace('za ', 'Za ')}</strong>", p, f"{x} – {y}") for a in AVONDEN for p, x, y in a["duels"]
] + [("<strong>Za 14 nov</strong>", "Alle poules", "Finales: de winnaars per poule")])}
<p><em>Videoland heeft nog geen officiële fightcard gepubliceerd. Alleen het duel tussen Donny Roelvink en Carlos Platier Luna is in de media bevestigd; de andere partijen kunnen nog veranderen. We werken het schema bij zodra de indeling definitief is.</em></p>
<h3><strong>Donny Roelvink – Carlos Platier Luna: de blikvanger</strong></h3>
<p>De eerste avond draait om Donny Roelvink. Vorig jaar zat hij nog als analist naast de ring bij Boxing Influencers, toen zijn broer Dave het toernooi won. Nu maakt hij zelf zijn boksdebuut. Zijn tegenstander Carlos Platier Luna heeft één groot voordeel: hij stond in 2018 ook al in de Boxing Stars-ring. Hij won toen van zanger Brace en verloor de halve finale op een jurybeslissing van Juvat Westendorp. Platier Luna is de enige deelnemer van toen die terugkeert.</p>"""

content3 = f"""<h3><strong>Boxing Stars live kijken bij Videoland</strong></h3>
<p>Boxing Stars is alleen live te zien bij Videoland, op zaterdag 31 oktober, 7 november en 14 november vanaf 20:00 uur. Voor live kijken heb je een betaald abonnement nodig: het gratis TV Gemist-account geeft geen toegang tot live-uitzendingen.</p>
{tabel(["Abonnement", "Prijs per maand", "Live kijken"], [
    ("Videoland Basis (met reclame)", "€6,99", "Ja"),
    ("Videoland Plus", "€11,99", "Ja"),
    ("Videoland Premium", "€14,99", "Ja"),
    ("TV Gemist (gratis)", "€0", "Nee"),
])}
<p>Een abonnement is maandelijks opzegbaar. Je kijkt via de app op je telefoon, tablet of smart-tv, in de browser of via je tv-aanbieder: bij Ziggo vind je Videoland op kanaal 151, bij KPN op kanaal 204. Meer kijkopties voor sport lees je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<h3><strong>Presentatie en commentaar</strong></h3>
<p>Monica Geuze en Valerio Zeno presenteren de Fight Nights. Monica Geuze presenteerde vorig jaar ook Boxing Influencers. Jay-Jay Boske en Mark Schaaf geven commentaar vanaf de eerste rij, en Duncan Tromp doet verslag vanaf de rode loper.</p>
<h3><strong>Kun je wedden op Boxing Stars?</strong></h3>
<p>Nee. Bij Nederlandse bookmakers met een vergunning van de Kansspelautoriteit kun je niet op Boxing Stars wedden. Vergunde aanbieders mogen alleen weddenschappen aanbieden op erkende, georganiseerde sport, en een bokscompetitie voor bekende Nederlanders valt daar niet onder.</p>
<h3><strong>Boxing Stars 2018: de vorige editie</strong></h3>
<p>De eerste Nederlandse editie was in het najaar van 2018 te zien bij RTL 5, met Ruben Nicolai en Olcay Gulsen als presentatoren. Toen deden zestien mannen en acht vrouwen mee, in een knock-outsysteem met partijen van drie ronden van anderhalve minuut. De titels gingen naar Juvat Westendorp (zwaargewicht), Rein van Duivenboden (lichtgewicht) en Jessie Jazz Vuijk (vrouwen).</p>
<h3><strong>Boxing Stars en Boxing Influencers</strong></h3>
<p>Boxing Stars is een ander programma dan Boxing Influencers, het toernooi dat vorig jaar werd gewonnen door Dave Roelvink. Ze zijn allebei bij Videoland te zien en delen een paar gezichten, zoals presentatrice Monica Geuze, commentator Mark Schaaf en de familie Roelvink. Teruglezen? Bekijk ons artikel over <a href="{BI25}">Boxing Influencers 2025</a> en de <a href="{BI25U}">uitslagen van Boxing Influencers 2025</a>.</p>
<h3><strong>Veelgestelde vragen over Boxing Stars</strong></h3>
<p><strong>Wanneer is Boxing Stars 2026?</strong><br>Op zaterdag 31 oktober, zaterdag 7 november en zaterdag 14 november 2026, telkens live om 20:00 uur bij Videoland.</p>
<p><strong>Hoe laat begint Boxing Stars?</strong><br>De live-uitzending begint om 20:00 uur. Bezoekers kunnen vanaf 17:30 uur naar binnen en moeten uiterlijk om 18:45 uur binnen zijn.</p>
<p><strong>Waar kan ik Boxing Stars kijken?</strong><br>Alleen bij Videoland, met een abonnement vanaf €6,99 per maand. Met het gratis TV Gemist-account kun je niet live kijken.</p>
<p><strong>Waar wordt Boxing Stars opgenomen?</strong><br>In de Mediahaven in Amsterdam, in de Houthavens. Tickets kosten €35, inclusief twee drankjes, frisdrank en snacks.</p>
<p><strong>Wie doen er mee aan Boxing Stars 2026?</strong><br>Donny Roelvink, Carlos Platier Luna, Nesim el Ahmadi, Edino van Dorsten, Eliyha Altena, Vincent Visser, Koen Pieter van Dijk, Jasha Rudge, Priscilla Nasi, Gaby Blaaser, Beate van der Weide en Jaimie Vaes.</p>
<p><strong>Tegen wie bokst Donny Roelvink?</strong><br>Tegen Carlos Platier Luna, op de eerste Fight Night van zaterdag 31 oktober.</p>
<p><strong>Waarom doet Sylvia Geersen niet mee?</strong><br>Ze trok zich op 23 oktober terug met een blessure. Priscilla Nasi, de dochter van Patty Brard, neemt haar plek over.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    alles = content + content2 + content3
    tekst = re.sub(r"<[^>]+>", " ", alles)
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", len(tekst.split()), "woorden")
    assert len(TITEL) <= 70 and 120 <= len(SAMENVATTING) <= 160 and (content.count("<!--SCHEMA-->") == 1 or "boxing-stars-schema" in content)
    assert "<h2" not in alles and "<h4" not in alles and "betcity" not in alles.lower() and "/go/" not in alles
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles) and not re.search(r"<(ul|ol)>\s+<", alles)
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    print("dry run ok – niets gepubliceerd")
