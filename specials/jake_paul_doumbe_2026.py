# -*- coding: utf-8 -*-
"""Los artikel: Jake Paul vs Cédric Doumbé, donderdag 24 december 2026, Coca-Cola Arena Dubai (aangekondigd 2-11-2026).
Feiten (onderzoek 2-11): persbericht MVP 2-11-2026: 8 ronden cruisergewicht, 200 lbs, 10-ounce handschoenen; records Paul
12-2 (7 KO), Doumbé kickboksen 75-7-1 (45 KO), mma 6-1 (6 KO), boksen 1-0; persco's 10-11 18:00 CET Pavillon Cambon Parijs,
12-11 18:00 GST Dubai Opera; voorverkoop PFL Dubai-kopers 6-11, presale 14-11, verkoop 15-11 09:00 CET; uitzending en
undercard volgen. Wikipedia: Doumbé geboren 30-8-1992 Douala, op zijn 9e naar Frankrijk; Glory-weltergewichtkampioen 2x
(Holzken 12-2016 verdeeld, eerste Franse Glory-kampioen; Holzken 2017; Groenhart 2015 W, 2017 L, 2021 KO), 2015-2016
maandelijks bij Mejiro Gym Amsterdam; mma: UFC-debuut 2022 ging niet door; PFL-debuut 30-9-2023 KO Zébo in 9 s; 7-3-2024
TKO-verlies Chamsoudinov (glas in teen); 17-5-2024 TKO Willis (Bellator Parijs). Coca-Cola Arena: City Walk, 17.000 plaatsen.
Usyk stopte Verhoeven op 23-5-2026 in Gizeh in ronde 11. Bewust weggelaten: aanvangstijd, uitzender, odds, gage, undercard.
Update 10-11 (zie jake_paul_doumbe_feiten_2026.md): nog steeds geen uitzender/aanvangstijd/undercard/gage; Paul belooft te
stoppen als Doumbé wint (video 3-11, Reuters); persco Parijs live op YouTube MVP/PFL (niet beschrijven als gebeurd);
NY Post 29-10: niet op Netflix, DAZN-ppv waarschijnlijk (onbevestigd, als melding gebracht); 711/Kambi 10-11 14:23 geen odds.
  python3 specials/jake_paul_doumbe_2026.py        (dry run)
  publiceren: TAPE_URL=<be-static-url> specials/concept_publiceer.py jake_paul_doumbe_2026 --live"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "jake-paul-vs-cedric-doumbe-24-december-dubai-tijd-live-kijken"
RUBRIEK = "6502b65d49bc032ba533e7a2"   # boksen
TITEL = "Jake Paul vs Cédric Doumbé: datum, tijd, live kijken en odds"
SAMENVATTING = ("Jake Paul bokst op kerstavond 24 december in Dubai tegen Cédric Doumbé. Tijd, live kijken, records, "
                "kaartverkoop en wie de favoriet is.")
TAPE_URL = os.environ.get("TAPE_URL", "")   # be-static-URL van og/nieuws/jake-paul-doumbe-tale-of-the-tape.webp

L = {"kijken": '<a href="/live-kijken">live kijken</a>',
     "boksen": '<a href="/beste-boksen-wedden-sites-nederland-legaal-veilig-gokken-in-nederland">wedden op boksen</a>',
     "bs": '<a href="/nieuws/boxing-stars-2026-schema-deelnemers-waar-live-kijken-videoland">Boxing Stars 2026</a>',
     "legaal": '<a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>'}


def tape_figuur(url):
    return (f'<figure class="w-richtext-align-fullwidth w-richtext-figure-type-image"><div><img src="{url}" '
            f'alt="Tale of the tape Jake Paul vs Cédric Doumbé: leeftijd, records in boksen, kickboksen en mma, laatste gevecht, '
            f'gevechtsregels en belangrijke data tot 24 december 2026 in Dubai" loading="lazy"></div>'
            f'<figcaption>Jake Paul en Cédric Doumbé naast elkaar: records, regels en alle data tot het gevecht.</figcaption></figure>')


DOUMBE = [   # (jaar, moment)
    ("2013", "Wereldtitel WKA full contact, knock-out in 13 seconden"),
    ("2016", "Wint de Glory-titel in het weltergewicht van Nieky Holzken, eerste Franse Glory-kampioen"),
    ("2017", "Verdedigt de titel opnieuw tegen Holzken, verliest hem daarna aan Murthel Groenhart"),
    ("2019", "Pakt de Glory-titel voor de tweede keer"),
    ("2021", "Stopt Groenhart in de derde partij, stapt over naar mma"),
    ("2023", "PFL-debuut in Parijs: knock-out na 9 seconden tegen Jordan Zébo"),
    ("2024", "Eerste mma-nederlaag tegen Baissangour Chamsoudinov, daarna knock-out tegen Jaleel Willis"),
]

TAPE = [   # (onderdeel, Paul, Doumbé)
    ("Leeftijd op 24 december", "29 jaar", "34 jaar"),
    ("Geboren", "Cleveland, Verenigde Staten", "Douala, Kameroen"),
    ("Profrecord boksen", "12-2 (7 knock-outs)", "1-0"),
    ("Record kickboksen", "-", "75-7-1 (45 knock-outs)"),
    ("Record mma", "-", "6-1 (6 knock-outs)"),
    ("Grootste prestatie", "Zeges op Tyson, Chávez Jr., Diaz en Silva", "2x Glory-wereldkampioen weltergewicht"),
    ("Laatste gevecht", "KO-verlies vs Joshua (dec. 2025)", "TKO-winst vs Willis (mei 2024, mma)"),
]

content = f"""<p><strong>Jake Paul bokst op donderdag 24 december 2026, kerstavond, tegen de Franse vechtsportster Cédric Doumbé. Het gevecht vindt plaats in de Coca-Cola Arena in Dubai en gaat over acht ronden in het cruisergewicht. Promotor Most Valuable Promotions (MVP) maakte dat op maandag 2 november bekend. Doumbé is tweevoudig wereldkampioen kickboksen bij Glory, maar heeft als profbokser pas één partij achter zijn naam. Voor Paul is het de eerste wedstrijd sinds zijn knock-outnederlaag tegen Anthony Joshua.</strong></p>
<p><strong>Update dinsdag 10 november:</strong> vanavond om 18:00 uur staan Paul en Doumbé voor het eerst tegenover elkaar, op de persconferentie in Parijs. MVP en de PFL zenden die live uit op hun YouTube-kanalen. Donderdag 12 november volgt een tweede persconferentie in Dubai. De kaartverkoop begint zondag 15 november om 09:00 uur. Paul zei in een video dat hij stopt met boksen als Doumbé wint. De uitzender, de aanvangstijd en het voorprogramma zijn nog altijd niet bekendgemaakt, en bij 711 zijn er nog geen odds op het gevecht.</p>
<h3><strong>Jake Paul vs Cédric Doumbé in het kort</strong></h3>
{tabel(["", ""], [
    ("<strong>Datum</strong>", "Donderdag 24 december 2026 (kerstavond)"),
    ("<strong>Plaats</strong>", "Coca-Cola Arena, City Walk, Dubai (ongeveer 17.000 plaatsen)"),
    ("<strong>Soort gevecht</strong>", "Profboksen, officieel erkend, 8 ronden"),
    ("<strong>Gewicht</strong>", "Cruisergewicht, maximaal 200 pond (90,7 kilo)"),
    ("<strong>Handschoenen</strong>", "10 ounce"),
    ("<strong>Organisatie</strong>", "Most Valuable Promotions (MVP)"),
    ("<strong>Aanvangstijd</strong>", "Nog niet bekend (Dubai loopt 3 uur voor op Nederland)"),
    ("<strong>Uitzending</strong>", "Nog niet bekend, volgt in de komende weken"),
    ("<strong>Kaartverkoop</strong>", "Zondag 15 november, 09:00 uur Nederlandse tijd"),
])}
{tape_figuur(TAPE_URL) if TAPE_URL else ""}
<h3><strong>Wat is er bekendgemaakt?</strong></h3>
<p>Eind oktober liet MVP al weten dat Paul op kerstavond in Dubai terugkeert, maar toen was zijn tegenstander nog geheim. Op 2 november volgde de naam: Cédric Doumbé. Lang werd gedacht dat de Engelse oud-UFC-vechter Darren Till de tegenstander zou worden, maar het werd dus de Fransman.</p>
<p>Het gevecht is een officieel erkende profpartij en telt dus mee voor de records van beide mannen. Er wordt gebokst met handschoenen van 10 ounce, de gewichtslimiet is 200 pond. Paul vocht ook tegen Julio César Chávez Jr. in die klasse. Het evenement komt naar Dubai via een samenwerking tussen MVP, de Dubai Sports Council en het Dubaise ministerie van Economie en Toerisme. MVP fuseerde eerder met de mma-organisatie PFL, waar Doumbé onder contract staat.</p>
<p>Voor het gevecht zijn er twee persconferenties waar Paul en Doumbé elkaar voor het eerst in de ogen kijken. Beide zijn gratis toegankelijk voor publiek. De persconferentie in Parijs is ook live te volgen via de YouTube-kanalen van MVP en de PFL.</p>
<p>In de aanloop legde Paul de lat zelf hoog. In een video die hij een dag na de aankondiging plaatste, beloofde hij te stoppen met boksen als hij van Doumbé verliest.</p>
{tabel(["Datum", "Wat", "Tijd in Nederland"], [
    ("Vrijdag 6 november", "Voorverkoop voor kopers van een PFL Dubai-ticket", "09:00 uur"),
    ("Dinsdag 10 november", "Persconferentie in Pavillon Cambon, Parijs", "18:00 uur"),
    ("Donderdag 12 november", "Persconferentie in de Dubai Opera", "15:00 uur"),
    ("Zaterdag 14 november", "Voorverkoop na aanmelding", "09:00 uur"),
    ("Zondag 15 november", "Vrije kaartverkoop via de Coca-Cola Arena", "09:00 uur"),
    ("Donderdag 24 december", "<strong>Jake Paul vs Cédric Doumbé</strong>", "Nog niet bekend"),
])}
<h3><strong>Wie is Cédric Doumbé?</strong></h3>
<p>Cédric Doumbé werd op 30 augustus 1992 geboren in Douala, Kameroen. Op zijn negende verhuisde hij met zijn moeder en zus naar Frankrijk. Zijn vader was rond zijn geboorte omgekomen bij een auto-ongeluk. Doumbé ontdekte het full-contact kickboksen als tiener en stopte met zijn studie psychologie om profvechter te worden.</p>
<p>In het kickboksen werd hij een van de besten ter wereld in het weltergewicht. Hij won 75 van zijn 83 partijen, 45 daarvan op knock-out. Bij Glory, de grootste kickboksorganisatie, was hij twee keer wereldkampioen. Voor Nederlanders is hij geen onbekende. In 2015 en 2016 trainde hij elke maand in Amsterdam bij de bekende Mejiro Gym. Hij won zijn eerste Glory-titel in 2016 van Nieky Holzken en vocht drie keer tegen Murthel Groenhart.</p>
{tabel(["Jaar", "Hoogtepunt Doumbé"], DOUMBE)}
<p>In 2021 stapte Doumbé over naar het mma. Een UFC-debuut in Parijs in 2022 ging niet door, waarna hij tekende bij de PFL. Daar werd hij in één klap een ster in Frankrijk: bij zijn debuut in september 2023 sloeg hij Jordan Zébo na negen seconden knock-out, met Kylian Mbappé en meerdere spelers van Paris Saint-Germain in de zaal. Zijn enige nederlaag kwam in maart 2024 tegen Baissangour Chamsoudinov. Die partij werd gestopt omdat er een stukje glas in de teen van Doumbé zat. Twee maanden later won hij in Parijs weer met een knock-out in de eerste ronde. In het mma staat hij op zes zeges en één nederlaag, alle zeges op knock-out. Als profbokser won hij zijn enige partij.</p>"""

content2 = f"""<h3><strong>Jake Paul en Cédric Doumbé naast elkaar</strong></h3>
{tabel(["", "Jake Paul", "Cédric Doumbé"], [(f"<strong>{a}</strong>", b, c) for a, b, c in TAPE])}
<p>Het grootste verschil zit in de ervaring in de boksring. Paul vocht 14 profpartijen, waaronder tegen Joshua, Tyson en Chávez Jr. Doumbé heeft er één. Daar staat tegenover dat Doumbé al sinds 2013 op het hoogste niveau vecht en in het kickboksen meer dan 80 partijen afwerkte. Wat opvalt is het gewicht. Doumbé vocht zijn hele loopbaan in het weltergewicht, rond de 77 kilo. Voor dit gevecht mag hij tot 90,7 kilo wegen. Paul vocht de laatste jaren al in het cruiser- en zwaargewicht.</p>
<h3><strong>Waarom vechten Paul en Doumbé tegen elkaar?</strong></h3>
<p>De twee zitten elkaar al jaren in de haren. Eind 2024 daagde Doumbé de Amerikaan uit voor een gevecht met gemengde regels, en begin 2025 sprak hij zich in Dubai nog eens in harde woorden over Paul uit. MVP-topman Nakisa Bidarian zegt dat Doumbé al jaren om dit gevecht vraagt. Volgens hem kwam het nu op het juiste moment.</p>
<p>Bij de aankondiging gingen beide mannen meteen los. Paul noemde Doumbé spottend 'Douchebag' en gaf toe dat hij roestig is en dat zijn kaak 'niet meer helemaal goed' is. Maar, zei hij, dit is geen kickboksen maar boksen. Hij verwees naar Rico Verhoeven, die in mei door Oleksandr Usyk in de elfde ronde werd gestopt: 'Net zoals Usyk Verhoeven opat, eet ik jou op in Dubai.' Doumbé sloeg terug dat Paul nog nooit zo'n probleem als hem heeft gehad. Hij wil 'het werk afmaken dat Joshua begon' en op kerstavond de Franse vlag zwaaien.</p>
<h3><strong>Jake Paul: de comeback na Joshua</strong></h3>
<p>Paul vocht voor het laatst op 19 december 2025 in Miami tegen Anthony Joshua. De Brit sloeg hem vier keer naar het canvas en won in de zesde ronde op knock-out. Paul brak zijn kaak op twee plekken en kreeg titanium platen. Het was de eerste knock-outnederlaag in zijn loopbaan. In oktober kreeg hij groen licht om weer volledig te sparren. Daarvoor won hij in juni 2025 nog op punten van Julio César Chávez Jr. Zijn enige andere nederlaag leed hij in 2023 tegen Tommy Fury.</p>
<p>Paul is in Nederland extra bekend omdat hij verloofd is met schaatsster Jutta Leerdam. Zijn gevecht tegen Mike Tyson in november 2024 werd volgens MVP wereldwijd door 125 miljoen mensen bekeken, het gevecht tegen Joshua door 33 miljoen.</p>"""

content3 = f"""<h3><strong>Hoe laat is Jake Paul vs Doumbé in Nederland?</strong></h3>
<p>De aanvangstijd is nog niet bekend. Dubai loopt in december drie uur voor op Nederland. Begint de hoofdpartij in Dubai om 23:00 uur, dan is het in Nederland 20:00 uur. Begint het gevecht pas na middernacht in Dubai, dan kijk je in Nederland rond 21:00 uur. De ringwandeling van de hoofdpartij is bij grote boksavonden meestal pas aan het einde van de avond, na het voorprogramma. Zodra de tijden bekend zijn, werken we dit artikel bij.</p>
<h3><strong>Waar kun je Jake Paul vs Doumbé live kijken?</strong></h3>
<p>Ook de uitzender is nog niet bekendgemaakt. MVP meldt alleen dat de wereldwijde uitzending in de komende weken volgt. Pauls gevechten tegen Mike Tyson en Anthony Joshua waren in Nederland live te zien op Netflix, zijn partij tegen Chávez Jr. werd uitgezonden door DAZN. De Amerikaanse krant New York Post meldde eind oktober dat dit gevecht niet op Netflix komt en dat DAZN de waarschijnlijkste uitzender is. MVP heeft dat niet bevestigd. Waar je het gevecht in Nederland kunt zien, is dus nog niet zeker. Een overzicht van alle sport die je kunt {L['kijken']}, vind je op onze site.</p>
<h3><strong>Wie is de favoriet: Paul of Doumbé?</strong></h3>
<p>Op papier is Paul de favoriet. Het is een bokspartij, en daarin heeft hij veel meer ervaring. Doumbé mag in de boksring niet trappen en geen knieën gebruiken, juist de wapens waarmee hij in het kickboksen veel won. Ook het gewicht speelt mee: Paul is van nature een stuk zwaarder en is gewend aan partijen van acht of tien ronden met boksregels.</p>
<p>Toch is Doumbé geen kansloze tegenstander. Hij heeft snelle handen, een uitstekend timinggevoel en veel slagkracht, getuige zijn knock-outs in drie verschillende sporten. Bovendien zijn er vraagtekens bij Paul. Hij stond een jaar aan de kant, en niemand weet hoe zijn herstelde kaak reageert op een harde treffer. Verwacht daarom dat bookmakers Paul als favoriet neerzetten, en dat Doumbé een interessante outsider wordt voor wie op een verrassing gokt.</p>
<h3><strong>Wedden op Jake Paul vs Doumbé</strong></h3>
<p>Er zijn nog geen odds op het gevecht. Bij 711 stond het op dinsdag 10 november om 14:23 uur nog niet in het aanbod. Zodra de bookmakers markten openen, kun je onder meer wedden op de winnaar, de manier van winnen (knock-out of op punten) en de ronde waarin het gevecht eindigt. Bij acht ronden is ook de vraag of het de volle afstand gaat een populaire markt. Lees in ons overzicht over {L['boksen']} bij welke aanbieders je terechtkunt. Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit; lees {L['legaal']}. Meer boksen dichter bij huis? Bekijk dan ons artikel over {L['bs']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Tegen wie vecht Jake Paul op 24 december?</strong><br>Tegen Cédric Doumbé, een Franse vechtsporter en tweevoudig Glory-wereldkampioen kickboksen.</p>
<p><strong>Wanneer en waar is Jake Paul vs Doumbé?</strong><br>Op donderdag 24 december 2026 (kerstavond) in de Coca-Cola Arena in Dubai.</p>
<p><strong>Hoe laat is het gevecht in Nederland?</strong><br>Dat is nog niet bekend. Dubai loopt in december drie uur voor op Nederland, dus een hoofdpartij om 23:00 uur in Dubai is 20:00 uur in Nederland.</p>
<p><strong>Waar kan ik Jake Paul vs Doumbé kijken?</strong><br>Dat is nog niet bekend. MVP maakt de uitzender in de komende weken bekend. Volgens de New York Post komt het gevecht niet op Netflix, maar bevestigd is dat niet.</p>
<p><strong>Hoeveel ronden duurt het gevecht?</strong><br>Maximaal acht ronden, in het cruisergewicht met een limiet van 200 pond (90,7 kilo).</p>
<p><strong>Wat is het record van Cédric Doumbé?</strong><br>In het kickboksen 75 zeges, 7 nederlagen en 1 gelijkspel (45 knock-outs). In het mma 6-1, als profbokser 1-0.</p>
<p><strong>Wat is het record van Jake Paul?</strong><br>12 zeges en 2 nederlagen, 7 keer won hij op knock-out. Hij verloor van Tommy Fury en Anthony Joshua.</p>
<p><strong>Stopt Jake Paul als hij verliest?</strong><br>Dat zegt hij wel. In een video beloofde Paul te stoppen met boksen als Doumbé hem verslaat.</p>
<p><strong>Hoeveel verdient Jake Paul met dit gevecht?</strong><br>De gages zijn niet bekendgemaakt.</p>
<p><strong>Wanneer start de kaartverkoop?</strong><br>Op zondag 15 november om 09:00 uur Nederlandse tijd, met een voorverkoop vanaf 14 november.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    alles = content + content2 + content3
    w = len(re.sub(r"<[^>]+>", " ", alles).split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", w, "woorden | tabellen", alles.count("<table"))
    assert len(TITEL) <= 70 and 120 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert "<h2" not in alles and "<h4" not in alles and "betcity" not in alles.lower() and "/go/" not in alles and "—" not in alles
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    print("dry run ok")
