# -*- coding: utf-8 -*-
"""Los SEO-artikel: Boxing Stars 2026 bij Videoland (schema, deelnemers, tijden, tickets, live kijken). 25-10-2026.
Opzet naar het best scorende artikel ooit (Boxing Influencers 2025: 9.532 kliks): 'schema, programma en waar live kijken
(datum)' + later live bijwerken met uitslagen per Fight Night. Zoekwoorden (Google NL): boxing stars, boxing stars 31 oktober,
boxing stars wanneer, boxing stars videoland, boxing stars 2026, boxing stars deelnemers, boxing stars kijken.
Feiten: specials/boxing_stars_feiten_2026.md (boxing-stars.nl, rtl.nl/boulevard 13-10 en 23-10, Broadcast Magazine 14-10,
videoland.com, nl.wikipedia). Indeling per avond: bekendgemaakt op 28-10-2026 (Weekblad Party en VK Magazine, zelfde
persbericht): 31 okt Roelvink–Van Dorsten, Van Dijk–Visser, Vaes–Blaaser; 7 nov El Ahmadi–Platier Luna, Altena–Rudge,
Nasi–Van der Weide. Tweede mannenpoule = middengewicht. Geen bookmaker-CTA (rolmodellenverbod; wedden op Boxing Stars kan
niet bij vergunde aanbieders). Edino van Dorsten zonder Ruinerwold (verband niet bevestigd in Boxing Stars-berichten).
Uitslagen Fight Night 1 (1-11-2026): VK Magazine 31-10 ('Koen Pieter van Dijk keihard knock-out', alle drie de partijen)
+ Vandaag Inside 31-10 (Roelvink KO ronde 2, finale tegen winnaar El Ahmadi–Platier Luna). Ruinerwold bewust weggelaten.
Uitslagen Fight Night 2 (10-11-2026): El Ahmadi, Rudge en Van der Weide wonnen, alle drie na drie ronden (geen KO;
scorekaarten niet gepubliceerd). Bronnen: fight.nl 7-11, VK Magazine 7-11, Puna 7-11/8-11, Vandaag Inside 8-11, LoveThat 9-11,
Ziggo programmapagina 8-11 (finales). Titel/intro gericht op de finale van 14 november. Volgorde finales nog niet bekend.
Na 14 nov: UITSLAG aanvullen met de drie finales, titel naar 'winnaars/kampioenen Boxing Stars 2026'.
  python3 specials/boxing_stars_2026.py   (dry run)
  beelden: og_kaarten/boxing_stars.py; publiceren: specials/concept_publiceer.py boxing_stars_2026 --live"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

TITEL = "Boxing Stars finale 14 november: wie tegen wie en uitslagen"
SLUG = "boxing-stars-2026-schema-deelnemers-waar-live-kijken-videoland"
SAMENVATTING = ("Boxing Stars finale op zaterdag 14 november: Roelvink – El Ahmadi, Visser – Rudge en Vaes – Van der Weide. "
                "Met alle uitslagen van 7 november.")
RUBRIEK = "6502b65d49bc032ba533e7a2"   # zelfde rubriek als Boxing Influencers 2025
SCHEMA_URL = os.environ.get("BOXING_SCHEMA_URL", "")   # be-static-URL van og/nieuws/boxing-stars-schema.webp (publiceerstap)

AVONDEN = [
    {"naam": "Fight Night 1", "datum": "za 31 okt", "finale": False, "kort": "Gewonnen: Roelvink, Visser en Vaes",
     "duels": [("Mannen zwaargewicht", "Donny Roelvink", "Edino van Dorsten"),
               ("Mannen middengewicht", "Koen Pieter van Dijk", "Vincent Visser"),
               ("Vrouwen lichtgewicht", "Jaimie Vaes", "Gaby Blaaser")]},
    {"naam": "Fight Night 2", "datum": "za 7 nov", "finale": False, "kort": "Gewonnen: El Ahmadi, Rudge en Van der Weide",
     "duels": [("Mannen zwaargewicht", "Nesim el Ahmadi", "Carlos Platier Luna"),
               ("Mannen middengewicht", "Eliyha Altena", "Jasha Rudge"),
               ("Vrouwen lichtgewicht", "Priscilla Nasi", "Beate van der Weide")]},
    {"naam": "Finale-avond", "datum": "za 14 nov", "finale": True, "kort": "Drie finales, live om 20:00 uur", "duels": []},
]
POULES = [
    {"naam": "Mannen zwaargewicht", "sub": "Poule 1",
     "namen": ["Donny Roelvink", "Edino van Dorsten", "Nesim el Ahmadi", "Carlos Platier Luna"]},
    {"naam": "Mannen middengewicht", "sub": "Poule 2",
     "namen": ["Koen Pieter van Dijk", "Vincent Visser", "Eliyha Altena", "Jasha Rudge"]},
    {"naam": "Vrouwen lichtgewicht", "sub": "Poule 3",
     "namen": ["Jaimie Vaes", "Gaby Blaaser", "Priscilla Nasi", "Beate van der Weide"]},
]

# uitslagen per partij ("A – B"): (winnaar, korte uitslag, uitleg)
UITSLAG = {
    "Donny Roelvink – Edino van Dorsten": ("Donny Roelvink", "Knock-out, ronde 2",
        "Roelvink werkte Van Dorsten in de tweede ronde met een rechtse stoot naar het canvas; de scheidsrechter stopte de partij"),
    "Koen Pieter van Dijk – Vincent Visser": ("Vincent Visser", "Knock-out, ronde 1",
        "Visser raakte Van Dijk na drie seconden met een rechtse hoek op de kaak; de partij was binnen drie minuten voorbij"),
    "Jaimie Vaes – Gaby Blaaser": ("Jaimie Vaes", "Na drie ronden",
        "Vaes was alle drie de ronden de aanvallende partij en werd na de volledige afstand tot winnaar uitgeroepen"),
    "Nesim el Ahmadi – Carlos Platier Luna": ("Nesim el Ahmadi", "Na drie ronden",
        "Nipte zege: El Ahmadi was in de eerste twee ronden net iets beter, de derde ronde ging naar Platier Luna"),
    "Eliyha Altena – Jasha Rudge": ("Jasha Rudge", "Na drie ronden",
        "Gelijk opgaande partij met veel clinches; Rudge raakte als eerste goed en werd na drie ronden tot winnaar uitgeroepen"),
    "Priscilla Nasi – Beate van der Weide": ("Beate van der Weide", "Na drie ronden",
        "Van der Weide hield Nasi met haar reikwijdte en rechte stoten op afstand en werd na drie ronden als winnares aangewezen"),
}
# finales 14 november: (poule, winnaar 31 okt, winnaar 7 nov). Volgorde/ringtijden nog niet bekendgemaakt.
FINALES = [("Mannen zwaargewicht", "Donny Roelvink", "Nesim el Ahmadi"),
           ("Mannen middengewicht", "Vincent Visser", "Jasha Rudge"),
           ("Vrouwen lichtgewicht", "Jaimie Vaes", "Beate van der Weide")]
AVONDEN[2]["duels"] = list(FINALES)


def achternaam(n):
    a = {"Koen Pieter van Dijk": "Van Dijk"}.get(n) or n.split(" ", 1)[1]
    return a[0].upper() + a[1:]


def weg(naam):
    """Hoe een finalist de finale bereikte, bv. 'knock-out in ronde 2 tegen Van Dorsten'."""
    for duel, (w, kort, _u) in UITSLAG.items():
        if w == naam:
            x, y = duel.split(" – ")
            k = kort.lower().replace("knock-out, ronde", "knock-out in ronde")
            return f"{k} tegen {achternaam(y if x == naam else x)}"
    return ""


def uitslag(x, y):
    u = UITSLAG.get(f"{x} – {y}")
    return f"<strong>{u[0]}</strong> ({u[1].lower()})" if u else "Finale, nog te boksen"


BI25 = "/nieuws/boxing-influencers-2025-schema-programma-en-waar-live-gratis-kijken-op-tv-in-nederland-zondag-5-oktober-2025"
BI25U = "/nieuws/uitslagen-boxing-influencers-2025---dave-roelvink-kroont-zich-tot-kampioen"


def schema_figuur(url):
    return (f'<figure class="w-richtext-align-fullwidth w-richtext-figure-type-image"><div><img src="{url}" '
            f'alt="Schema Boxing Stars 2026: drie Fight Nights op 31 oktober, 7 november en 14 november bij Videoland, met de uitslagen van Fight Night 1 en 2 en de drie finales" '
            f'loading="lazy"></div><figcaption>Het schema van Boxing Stars 2026 met alle Fight Nights, poules en uitslagen.</figcaption></figure>')


content = f"""<p><strong>De finales van Boxing Stars 2026 zijn op zaterdag 14 november, live om 20:00 uur bij Videoland. Donny Roelvink bokst tegen Nesim el Ahmadi (zwaargewicht), Vincent Visser tegen Jasha Rudge (middengewicht) en Jaimie Vaes tegen Beate van der Weide (vrouwen lichtgewicht). El Ahmadi, Rudge en Van der Weide plaatsten zich op 7 november: alle drie wonnen ze hun partij na drie ronden, van Carlos Platier Luna, Eliyha Altena en Priscilla Nasi.</strong></p>
<p><strong>Update 10 november:</strong> hieronder staan de uitslagen van Fight Night 2 en hoe de partijen verliepen. Daarmee zijn alle drie de finales bekend. De volgorde van de finales en de precieze ringtijden zijn nog niet bekendgemaakt. Direct na afloop van zaterdag 14 november zetten we hier de kampioenen.</p>
<h3><strong>Boxing Stars finale 14 november: wie tegen wie?</strong></h3>
{tabel(["Poule", "Finale", "Zo kwamen ze in de finale"], [
    (p, f"<strong>{a} – {b}</strong>", f"{achternaam(a)}: {weg(a)} (31 okt). {achternaam(b)}: {weg(b)} (7 nov).")
    for p, a, b in FINALES
])}
<p><em>Finale-avond, zaterdag 14 november 2026, Mediahaven Amsterdam. Live bij Videoland vanaf 20:00 uur.</em></p>
<h3><strong>Uitslagen Boxing Stars 2026</strong></h3>
{tabel(["Avond", "Poule", "Partij", "Winnaar", "Uitslag"], [
    (a["datum"].replace("za ", "Za "), p, f"{x} – {y}", f"<strong>{UITSLAG[f'{x} – {y}'][0]}</strong>", UITSLAG[f"{x} – {y}"][1])
    for a in (AVONDEN[1], AVONDEN[0]) for p, x, y in a["duels"]
])}
<p><em>Fight Night 2 op 7 november en Fight Night 1 op 31 oktober 2026, Mediahaven Amsterdam. Scorekaarten van de partijen die de volle drie ronden duurden, zijn niet gepubliceerd.</em></p>
<h3><strong>Fight Night 2 (7 november): zo verliepen de partijen</strong></h3>
<p><strong>Nesim el Ahmadi – Carlos Platier Luna (zwaargewicht).</strong> Een rommelige partij met wilde stoten en veel clinches, waarover Platier Luna zich na afloop beklaagde. El Ahmadi was in de eerste twee ronden net iets beter. De derde ronde ging naar Platier Luna, maar dat was te laat: El Ahmadi kreeg de nipte zege. Daarmee ligt Platier Luna, de enige deelnemer die in 2018 ook al meedeed, eruit. Direct na de partij richtte El Ahmadi zich tot zijn finaletegenstander Donny Roelvink.</p>
<p><strong>Eliyha Altena – Jasha Rudge (middengewicht).</strong> De twee acteurs hielden elkaar lang in evenwicht. Rudge raakte in de eerste ronde als eerste goed, daarna wisselden de stoten elkaar af en gingen ze vaak de clinch in. In de derde ronde speelde de vermoeidheid Altena parten. Na drie ronden werd Rudge tot winnaar uitgeroepen. Altena zei na afloop nog nooit zoveel spanning te hebben gevoeld.</p>
<p><strong>Priscilla Nasi – Beate van der Weide (vrouwen lichtgewicht).</strong> Van der Weide hield Nasi met haar reikwijdte en rechte stoten op afstand. Nasi, die pas laat instapte als vervanger van Sylvia Geersen, bleef naar voren gaan, maar moest veel klappen incasseren. Na drie ronden werd Van der Weide als winnares aangewezen.</p>
<p>Hieronder vind je verder het volledige schema, alle deelnemers per poule, hoe de eerste avond verliep, hoe laat de finale begint, hoeveel een ticket kost en hoe je Boxing Stars live kijkt.</p>
<!--SCHEMA-->
<h3><strong>Wat is Boxing Stars?</strong></h3>
<p>Boxing Stars is een bokscompetitie voor bekende Nederlanders. De deelnemers trainen wekenlang onder begeleiding van ervaren trainers en onder toezicht van de Nederlandse Boksbond (NBB), en nemen het daarna live tegen elkaar op in de ring. Het format komt van het Belgische productiehuis De Mensen. In Nederland was het in 2018 al te zien bij RTL 5; nu komt het terug met drie live-uitzendingen bij Videoland, geproduceerd door Signal.Stream.</p>
<h3><strong>Wanneer is Boxing Stars? Datums en tijden</strong></h3>
{tabel(["Avond", "Datum", "Live bij Videoland", "Status"], [
    ("<strong>Fight Night 1</strong>", "Zaterdag 31 oktober 2026", "20:00 uur", "Geweest"),
    ("<strong>Fight Night 2</strong>", "Zaterdag 7 november 2026", "20:00 uur", "Geweest"),
    ("<strong>Finale-avond</strong>", "Zaterdag 14 november 2026", "20:00 uur", "<strong>Drie finales</strong>"),
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
    ("Kaartverkoop", "Via de officiële site van Boxing Stars (Weeztix), kies daar de datum"),
])}
<p>Je ticket is digitaal, met een QR-code: printen is niet nodig. Kom je met de auto, dan is parkeergarage P1 Minervahaven het dichtst in de buurt.</p>"""

if SCHEMA_URL:
    content = content.replace("<!--SCHEMA-->", schema_figuur(SCHEMA_URL))

content2 = f"""<h3><strong>Deelnemers Boxing Stars 2026: alle twaalf BN'ers</strong></h3>
<p>De twaalf deelnemers zijn verdeeld over drie poules van vier: twee mannenpoules (zwaargewicht en middengewicht) en een vrouwenpoule.</p>
<p><strong>Mannen zwaargewicht</strong></p>
{tabel(["Deelnemer", "Bekend van"], [
    ("Donny Roelvink", "Mediapersoonlijkheid, zoon van Dries en broer van Dave Roelvink; Temptation Island VIPS en Expeditie Robinson"),
    ("Edino van Dorsten", "Spreker en auteur van het boek Mijn naam is Edino"),
    ("Nesim el Ahmadi", "Comedian, presentator en rapper, de helft van het duo Supergaande"),
    ("Carlos Platier Luna", "Winnaar Expeditie Robinson 2017, judoka; bokste ook al mee in Boxing Stars 2018"),
])}
<p><strong>Mannen middengewicht</strong></p>
{tabel(["Deelnemer", "Bekend van"], [
    ("Koen Pieter van Dijk", "Presentator, voorheen bekend als Koen Kardashian; Expeditie Robinson 2025"),
    ("Vincent Visser", "Acteur, bekend van Brugklas en als Valentijn Sanders in GTST"),
    ("Eliyha Altena", "Acteur, bekend als Daan in de serie Knokke Off"),
    ("Jasha Rudge", "Acteur, onder meer in De leerling en Flikken Rotterdam"),
])}
<p><strong>Vrouwen lichtgewicht</strong></p>
{tabel(["Deelnemer", "Bekend van"], [
    ("Jaimie Vaes", "Styliste en presentatrice, Just Tattoo of Us en Expeditie Robinson 2023"),
    ("Gaby Blaaser", "Actrice en presentatrice, Sacha in GTST en de Bachelorette van 2020"),
    ("Priscilla Nasi", "Dochter van Patty Brard; vervangt de geblesseerde Sylvia Geersen"),
    ("Beate van der Weide", "Contentcreator, bekend van De Bachelor en De Bachelorette 2026"),
])}
<p><strong>Sylvia Geersen doet niet mee.</strong> Het model trok zich op 23 oktober terug met een blessure, nadat ze zichzelf naar eigen zeggen had overtraind. Priscilla Nasi, de dochter van Patty Brard, neemt haar plek in.</p>
<h3><strong>Boxing Stars schema: wie bokst tegen wie?</strong></h3>
<p>Per Fight Night werd in elke poule één partij gebokst, zodat op de eerste twee avonden iedere deelnemer één keer aan de beurt was. De winnaars van die partijen strijden op 14 november in de finale van hun poule. Dit is het volledige schema met de uitslagen tot nu toe:</p>
{tabel(["Avond", "Poule", "Partij", "Winnaar"], [
    (f"<strong>{a['datum'].replace('za ', 'Za ')}</strong>", p, f"{x} – {y}", uitslag(x, y)) for a in AVONDEN for p, x, y in a["duels"]
])}
<p><em>Bij een blessure kan een finale nog veranderen. We werken het schema na de finales bij.</em></p>
<h3><strong>Fight Night 1 (31 oktober): zo verliepen de partijen</strong></h3>
<p><strong>Donny Roelvink – Edino van Dorsten (zwaargewicht).</strong> Van Dorsten begon fel en dreef Roelvink in de eerste ronde meteen de hoek in. Roelvink moest vooral verdedigen, maar vond in de tweede ronde zijn ritme. Met een rechtse stoot werkte hij Van Dorsten naar het canvas. Die stond snel weer op, maar de scheidsrechter stopte de partij. Na afloop gaf Roelvink toe dat zijn tegenstander het hem lastig had gemaakt. Een jaar nadat zijn broer Dave Boxing Influencers won, staat Donny bij zijn boksdebuut meteen in de finale.</p>
<p><strong>Koen Pieter van Dijk – Vincent Visser (middengewicht).</strong> Dit was de kortste partij van de avond. Na amper drie seconden raakte Visser zijn tegenstander met een harde rechtse hoek op de kaak, terwijl Van Dijk zijn handen te laag hield. Van Dijk ging neer en de partij was binnen drie minuten voorbij. De 25-jarige acteur, bekend van Brugklas en GTST, is daarmee de tweede finalist.</p>
<p><strong>Jaimie Vaes – Gaby Blaaser (vrouwen lichtgewicht).</strong> De enige partij die de volle drie ronden duurde. Vaes ging vanaf de eerste bel in de aanval en raakte Blaaser in de eerste ronde zo hard met een rechtse hoek dat de scheidsrechter even ingreep. Blaaser bleef terugvechten, maar Vaes deelde de hardste klappen uit en werd tot winnaar uitgeroepen. Ze is de eerste vrouw in de finale.</p>
<p>Gemist? De complete partijen van Fight Night 1 zijn inmiddels terug te zien.</p>
<h3><strong>Finales 14 november: wat kun je verwachten?</strong></h3>
<p><strong>Donny Roelvink – Nesim el Ahmadi (zwaargewicht).</strong> Roelvink maakte bij zijn boksdebuut op 31 oktober indruk met een knock-out in de tweede ronde tegen Edino van Dorsten, nadat hij in de eerste ronde zelf onder druk had gestaan. El Ahmadi had op 7 november de volle drie ronden nodig en won nipt van Carlos Platier Luna, de enige deelnemer met Boxing Stars-ervaring. Roelvink legde zo de overtuigendste weg naar de finale af, El Ahmadi heeft al drie volle ronden in de benen.</p>
<p><strong>Vincent Visser – Jasha Rudge (middengewicht).</strong> Visser had in zijn eerste partij maar een paar seconden nodig: met een rechtse hoek sloeg hij Koen Pieter van Dijk knock-out. Rudge won een zware, gelijk opgaande partij van Eliyha Altena na drie ronden. Visser stond dus nauwelijks in de ring, Rudge weet al hoe het voelt om drie ronden vol te maken.</p>
<p><strong>Jaimie Vaes – Beate van der Weide (vrouwen lichtgewicht).</strong> Beide vrouwen wonnen hun eerste partij na drie ronden. Vaes zocht tegen Gaby Blaaser vanaf de eerste bel de aanval, Van der Weide won van Priscilla Nasi juist door afstand te houden met haar reikwijdte en rechte stoten. In de finale staat dus een aanvaller tegenover een bokser die op afstand werkt.</p>
<p>Op zaterdag 14 november worden de drie finales live uitgezonden bij Videoland, vanaf 20:00 uur. De winnaar van elke finale is de kampioen van zijn of haar poule in Boxing Stars 2026. In welke volgorde de finales worden gebokst, is nog niet bekendgemaakt.</p>"""

content3 = f"""<h3><strong>Boxing Stars live kijken bij Videoland</strong></h3>
<p>De finales van Boxing Stars zijn alleen live te zien bij Videoland, op zaterdag 14 november vanaf 20:00 uur. Voor live kijken heb je een betaald abonnement nodig: het gratis TV Gemist-account geeft geen toegang tot live-uitzendingen.</p>
{tabel(["Abonnement", "Prijs per maand", "Live kijken"], [
    ("Videoland Basis (met reclame)", "€6,99", "Ja"),
    ("Videoland Plus", "€11,99", "Ja"),
    ("Videoland Premium", "€14,99", "Ja"),
    ("TV Gemist (gratis)", "€0", "Nee"),
])}
<p>Een abonnement is maandelijks opzegbaar. Je kijkt via de app op je telefoon, tablet of smart-tv, in de browser of via je tv-aanbieder: bij Ziggo vind je Videoland op kanaal 151, bij KPN op kanaal 204. Meer kijkopties voor sport lees je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<h3><strong>Presentatie en commentaar</strong></h3>
<p>Monica Geuze en Valerio Zeno presenteren de Fight Nights, ook de finale-avond. Monica Geuze presenteerde vorig jaar ook Boxing Influencers. Jay-Jay Boske en Mark Schaaf geven commentaar vanaf de eerste rij, en Duncan Tromp doet verslag vanaf de rode loper.</p>
<h3><strong>Kun je wedden op Boxing Stars?</strong></h3>
<p>Nee. Bij Nederlandse bookmakers met een vergunning van de Kansspelautoriteit kun je niet op Boxing Stars wedden. Vergunde aanbieders mogen alleen weddenschappen aanbieden op erkende, georganiseerde sport, en een bokscompetitie voor bekende Nederlanders valt daar niet onder.</p>
<h3><strong>Boxing Stars 2018: de vorige editie</strong></h3>
<p>De eerste Nederlandse editie was in het najaar van 2018 te zien bij RTL 5, met Ruben Nicolai en Olcay Gulsen als presentatoren. Toen deden zestien mannen en acht vrouwen mee, in een knock-outsysteem met partijen van drie ronden van anderhalve minuut. De titels gingen naar Juvat Westendorp (zwaargewicht), Rein van Duivenboden (lichtgewicht) en Jessie Jazz Vuijk (vrouwen).</p>
<h3><strong>Boxing Stars en Boxing Influencers</strong></h3>
<p>Boxing Stars is een ander programma dan Boxing Influencers, het toernooi dat vorig jaar werd gewonnen door Dave Roelvink. Ze zijn allebei bij Videoland te zien en delen een paar gezichten, zoals presentatrice Monica Geuze, commentator Mark Schaaf en de familie Roelvink. Teruglezen? Bekijk ons artikel over <a href="{BI25}">Boxing Influencers 2025</a> en de <a href="{BI25U}">uitslagen van Boxing Influencers 2025</a>.</p>
<h3><strong>Veelgestelde vragen over Boxing Stars</strong></h3>
<p><strong>Wanneer is de finale van Boxing Stars 2026?</strong><br>Op zaterdag 14 november 2026, live om 20:00 uur bij Videoland. De eerste twee Fight Nights waren op 31 oktober en 7 november.</p>
<p><strong>Wie staan er in de finale van Boxing Stars?</strong><br>Donny Roelvink tegen Nesim el Ahmadi (zwaargewicht), Vincent Visser tegen Jasha Rudge (middengewicht) en Jaimie Vaes tegen Beate van der Weide (vrouwen lichtgewicht).</p>
<p><strong>Hoe laat begint de finale van Boxing Stars?</strong><br>De live-uitzending begint om 20:00 uur en duurt ongeveer anderhalf uur. Bezoekers kunnen vanaf 17:30 uur naar binnen en moeten uiterlijk om 18:45 uur binnen zijn. De volgorde van de drie finales is nog niet bekendgemaakt.</p>
<p><strong>Wie heeft er gewonnen bij Boxing Stars op 7 november?</strong><br>Nesim el Ahmadi (tegen Carlos Platier Luna), Jasha Rudge (tegen Eliyha Altena) en Beate van der Weide (tegen Priscilla Nasi). Alle drie de partijen duurden de volle drie ronden.</p>
<p><strong>Wie heeft er gewonnen bij Boxing Stars op 31 oktober?</strong><br>Donny Roelvink (knock-out in de tweede ronde tegen Edino van Dorsten), Vincent Visser (knock-out in de eerste ronde tegen Koen Pieter van Dijk) en Jaimie Vaes (na drie ronden tegen Gaby Blaaser).</p>
<p><strong>Tegen wie bokst Donny Roelvink in de finale?</strong><br>Tegen Nesim el Ahmadi, die op 7 november nipt won van Carlos Platier Luna. De finale is op zaterdag 14 november.</p>
<p><strong>Heeft Donny Roelvink gewonnen bij Boxing Stars?</strong><br>Hij won zijn boksdebuut op 31 oktober in de tweede ronde van Edino van Dorsten. Op 14 november bokst hij in de finale van het zwaargewicht tegen Nesim el Ahmadi.</p>
<p><strong>Waar kan ik Boxing Stars kijken?</strong><br>Alleen bij Videoland, met een abonnement vanaf €6,99 per maand. Met het gratis TV Gemist-account kun je niet live kijken.</p>
<p><strong>Waar wordt Boxing Stars opgenomen?</strong><br>In de Mediahaven in Amsterdam, in de Houthavens. Tickets kosten €35, inclusief twee drankjes, frisdrank en snacks.</p>
<p><strong>Wie doen er mee aan Boxing Stars 2026?</strong><br>Donny Roelvink, Carlos Platier Luna, Nesim el Ahmadi, Edino van Dorsten, Eliyha Altena, Vincent Visser, Koen Pieter van Dijk, Jasha Rudge, Priscilla Nasi, Gaby Blaaser, Beate van der Weide en Jaimie Vaes.</p>
<p><strong>Waarom doet Sylvia Geersen niet mee?</strong><br>Ze trok zich op 23 oktober terug met een blessure. Priscilla Nasi, de dochter van Patty Brard, nam haar plek over.</p>
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
