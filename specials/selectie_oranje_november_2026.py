# -*- coding: utf-8 -*-
"""Los artikel: selectie Oranje voor Nederland – Griekenland en Duitsland – Nederland (Nations League), bekend sinds vr 6-11-2026.
Bronnen (6-11, ±14:30):
- selectie (25), terugkeer, afwezigen, melden maandag in Zeist, stand groep (NL en GRE 8, GER 5, SRB 0), top 2 door:
  meemetoranje.nl/nederlands-elftal/nieuws/xavi-selectie-oranje-griekenland-duitsland-nations-league/ (6-11, 12:02),
  bevestigd door voetbalnieuws.nl/headliner (Gravenberch, Frimpong, Hato, Aké blessure; Taylor gepasseerd)
- programma: vr 13-11 20:45 Johan Cruijff ArenA, ma 16-11 20:45 Olympiastadion Berlijn (Flashscore, Squawka, Weekend Goals)
- odds Nederland – Griekenland 711 (Kambi sevelevnl) 6-11 ±14:30: 1,47 / 4,80 / 6,75
- tv: NOS zendt het Nederlands elftal uit (eigen zenderconfig data/tv_zenders.json)
Update di 10-11-2026 (±14:25), zie specials/nations_league_2028_feiten.md §6b:
- Van Dijk en Brobbey vallen af, niet fit (OnsOranje/KNVB 9-11 17:45; NOS 2638755).
- Sepp van den Berg (Brentford) opgeroepen als vervanger van Van Dijk, selectie 24; geen vervanger voor Brobbey
  (OnsOranje 82822, NOS 2638854 13:06, VI 12:53).
- Training ma-avond alleen Dumfries, Summerville, Reijnders buiten (NOS); di 23 fitte spelers op het veld (ANP).
- Aanvoerder nog niet bekend; Xavi noemde De Jong "een van onze aanvoerders" (NOS 2638812).
- odds 711 (Kambi) di 10-11 14:25: 1,49 / 4,60 / 6,75.
Niet gebruikt (onzeker): wie de aanvoerdersband krijgt, aard blessures Van Dijk/Brobbey, rugnummers, interlands per speler, reden afwezigheid Zirkzee.
  python3 specials/selectie_oranje_november_2026.py   (dry run)"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "selectie-oranje-november-2026-griekenland-duitsland"
RUBRIEK = "66d6d655bc312d5c0e834ecd"   # zelfde rubriek als het Xavi-salarisartikel
TITEL = "Selectie Oranje november 2026: Van den Berg voor Van Dijk"
SAMENVATTING = ("Oranje telt 24 spelers voor Griekenland en Duitsland: Van Dijk en Brobbey zijn niet fit, debutant "
                "Sepp van den Berg is erbij en De Jong is terug.")

OG_LOGO = "nederland-logo.png"
OG_EYEBROW = "Oranje · Nations League"
OG_KOP = "Selectie Oranje<br><em>november 2026</em>"
OG_TEGELS = [("Spelers", "24"), ("Punten", "8")]
OG_KOPJE = "Programma en selectie"
OG_RECHTS = "Aftrap"
OG_RIJEN = [("vr 13/11", "Nederland – Griekenland (Amsterdam)", "20:45"),
            ("ma 16/11", "Duitsland – Nederland (Berlijn)", "20:45"),
            ("Nieuw", "Sepp van den Berg (Brentford)", "✓"),
            ("Af", "Van Dijk en Brobbey (niet fit)", "✗")]

L = {"xavi": '<a href="/nieuws/salaris-xavi-hernandez-bondscoach-oranje">wat Xavi verdient als bondscoach</a>',
     "nl": '<a href="/clubs/nederland">Nederlands elftal</a>',
     "afgemeld": '<a href="/nieuws/van-dijk-brobbey-afgemeld-oranje-griekenland-duitsland">wat de afmeldingen van Van Dijk en Brobbey betekenen</a>',
     "nlg": '<a href="/competities/uefa-nations-league">Nations League</a>',
     "711": '<a href="/bookmakers/711">711</a>',
     "legaal": '<a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>'}

SELECTIE = [
    ("<strong>Keepers (3)</strong>", "Mark Flekken (Bayer Leverkusen), Robin Roefs (Sunderland), Bart Verbruggen (Brighton & Hove Albion)"),
    ("<strong>Verdedigers (7)</strong>", "Denzel Dumfries (Real Madrid), Lutsharel Geertruida (PSV), Jan Paul van Hecke (Tottenham Hotspur), Ian Maatsen (Aston Villa), Jurriën Timber (Arsenal), Micky van de Ven (Tottenham Hotspur), Sepp van den Berg (Brentford)"),
    ("<strong>Middenvelders (8)</strong>", "Frenkie de Jong (Barcelona), Justin Kluivert (Bournemouth), Teun Koopmeiners (Juventus), Tijjani Reijnders (Al Qadsiah), Quinten Timber (Crystal Palace), Joey Veerman (Borussia Dortmund), Gjivai Zechiël (Feyenoord), Guus Til (PSV)"),
    ("<strong>Aanvallers (6)</strong>", "Donyell Malen (AS Roma), Ruben van Bommel (PSV), Cody Gakpo (Liverpool), Noa Lang (Napoli), Crysencio Summerville (Al Hilal), Mexx Meerdink (AZ)"),
]

AFGEVALLEN = [("<strong>Virgil van Dijk</strong> (Liverpool)", "Niet fit, afgemeld op 9 november", "Sepp van den Berg (Brentford)"),
              ("<strong>Brian Brobbey</strong> (Sunderland)", "Niet fit, afgemeld op 9 november", "Geen vervanger")]

PROGRAMMA = [("Vrijdag 13 november", "20:45", "Nederland – Griekenland", "Johan Cruijff ArenA, Amsterdam"),
             ("Maandag 16 november", "20:45", "Duitsland – Nederland", "Olympiastadion, Berlijn")]

STAND = [("1", "Nederland", "8"), ("2", "Griekenland", "8"), ("3", "Duitsland", "5"), ("4", "Servië", "0")]

content = f"""<p><strong>Oranje gaat met 24 spelers de laatste twee groepsduels in de Nations League in: Nederland – Griekenland (vrijdag 13 november, 20:45 uur) en Duitsland – Nederland (maandag 16 november, 20:45 uur). Bondscoach Xavi Hernández koos op vrijdag 6 november 25 spelers, maar aanvoerder Virgil van Dijk en spits Brian Brobbey vielen maandag af omdat ze niet fit zijn. Op dinsdag 10 november riep Xavi Brentford-verdediger Sepp van den Berg op als vervanger van Van Dijk; voor Brobbey komt er niemand bij. Frenkie de Jong is terug na vier maanden blessureleed.</strong></p>
<p>Voor Oranje staat er veel op het spel. Nederland en Griekenland staan in groep A2 allebei op acht punten, Duitsland heeft er vijf. Een plek bij de eerste twee is genoeg voor de kwartfinales van de {L['nlg']}. De spelers meldden zich maandag 9 november in Zeist.</p>
<p><strong>Update dinsdag 10 november, 14:30 uur:</strong> de KNVB maakte maandagavond bekend dat Van Dijk (Liverpool) en Brobbey (Sunderland) niet fit uit het speelweekend zijn gekomen. Dinsdagmiddag volgde de oproep van <strong>Sepp van den Berg</strong> (24). De centrale verdediger van Brentford zat nooit eerder bij de A-selectie en meldt zich dinsdagavond in Zeist. Daarmee telt de selectie 24 spelers. Wie de aanvoerdersband van Van Dijk overneemt, heeft Xavi nog niet bekendgemaakt; hij noemde Frenkie de Jong wel "een van onze aanvoerders". Op de training van dinsdag stonden 23 fitte spelers op het veld. Lees ook {L['afgemeld']}.</p>
<h3><strong>De selectie van Oranje voor Griekenland en Duitsland</strong></h3>
{tabel(["Linie", "Spelers"], SELECTIE)}
<p><em>Selectie per dinsdag 10 november 2026 (24 spelers). Bij nieuwe blessures kan Xavi nog spelers bijroepen.</em></p>
<p><strong>Afgevallen na de bekendmaking</strong></p>
{tabel(["Speler", "Reden", "Vervanger"], AFGEVALLEN)}"""

content2 = f"""<h3><strong>Wie keren terug en wie ontbreken?</strong></h3>
<p><strong>Frenkie de Jong</strong> is de belangrijkste terugkeerder. De middenvelder maakte onlangs bij Barcelona zijn rentree na een absentie van vier maanden en is voor Xavi een vaste spil. Ook <strong>Donyell Malen</strong> is er weer bij: de spits van AS Roma miste de vorige interlandperiode door een blessure. Linksback <strong>Ian Maatsen</strong> van Aston Villa zit voor het eerst in een selectie van Xavi. Zijn enige interland speelde hij in maart 2025 tegen Spanje (3-3).</p>
<p>Nieuw is <strong>Sepp van den Berg</strong>. De 24-jarige centrale verdediger debuteerde op zijn zestiende bij PEC Zwolle, vertrok in 2019 naar Liverpool en werd daarna verhuurd aan onder meer Schalke 04 en Mainz. Sinds 2024 speelt hij bij Brentford, waar hij na een blessure de laatste vier competitieduels in de basis begon. Hij speelde acht duels voor Jong Oranje en is de enige speler in de selectie zonder interland.</p>
<p>Daartegenover staan zes spelers die in september en oktober wel bij de groep zaten. <strong>Ryan Gravenberch</strong> en <strong>Jeremie Frimpong</strong> van Liverpool zijn geblesseerd, net als <strong>Nathan Aké</strong> (dijbeen) en <strong>Jorrel Hato</strong>. <strong>Kenneth Taylor</strong> en <strong>Joshua Zirkzee</strong> zijn niet opgeroepen; nu De Jong en Justin Kluivert fit zijn, is er minder ruimte op het middenveld. Feyenoord-aanvoerder Luciano Valente ontbreekt opnieuw. Daar kwamen na de bekendmaking <strong>Virgil van Dijk</strong> en <strong>Brian Brobbey</strong> bij, die allebei niet fit uit het speelweekend kwamen.</p>
<p>Opvallend is de vaste plek voor jonge spelers uit de Eredivisie. <strong>Ruben van Bommel</strong> (PSV) en <strong>Gjivai Zechiël</strong> (Feyenoord), die in de eerste selectie van Xavi debuteerden, zijn er weer bij. <strong>Guus Til</strong> (PSV) en <strong>Mexx Meerdink</strong> (AZ), vorige keer opgeroepen als vervangers, mogen zich opnieuw melden.</p>
<h3><strong>Wanneer speelt Oranje?</strong></h3>
{tabel(["Datum", "Aftrap", "Wedstrijd", "Stadion"], [(f"<strong>{d}</strong>", t, w, s) for d, t, w, s in PROGRAMMA])}
<p>Beide wedstrijden zijn live te zien bij de NOS. Alles over het team, de vorm en de uitslagen vind je op onze pagina over het {L['nl']}.</p>
<h3><strong>De stand in Nations League-groep A2</strong></h3>
{tabel(["Plaats", "Land", "Punten"], STAND)}
<p>De nummers één en twee van de groep gaan door naar de kwartfinales. Wint Oranje van Griekenland, dan is een plek bij de laatste acht vrijwel zeker. In Berlijn gaat het daarna mogelijk om de groepswinst.</p>"""

content3 = f"""<h3><strong>Wat zeggen de bookmakers?</strong></h3>
<p>Oranje is ook zonder Van Dijk duidelijk favoriet tegen Griekenland. Bij {L['711']} staat een zege van Nederland op <strong>1,49</strong>, een gelijkspel op 4,60 en een Griekse zege op 6,75 (dinsdag 10 november, 14:25 uur). Voor Duitsland – Nederland waren nog geen odds beschikbaar. Wed alleen bij een bookmaker met een vergunning van de Kansspelautoriteit; lees {L['legaal']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoeveel spelers zitten er in de selectie van Oranje?</strong><br>24. Xavi Hernández koos op vrijdag 6 november 25 spelers. Van Dijk en Brobbey vielen af, Sepp van den Berg kwam erbij.</p>
<p><strong>Staat Frenkie de Jong in de selectie?</strong><br>Ja. De middenvelder van Barcelona is terug na vier maanden blessureleed.</p>
<p><strong>Wie ontbreken er bij Oranje?</strong><br>Virgil van Dijk en Brian Brobbey zijn niet fit. Ryan Gravenberch, Jeremie Frimpong, Nathan Aké en Jorrel Hato waren al niet opgeroepen vanwege blessures.</p>
<p><strong>Wie vervangt Virgil van Dijk?</strong><br>Sepp van den Berg van Brentford. Het is zijn eerste oproep voor Oranje. Voor Brobbey komt geen vervanger.</p>
<p><strong>Hoe laat speelt Nederland tegen Griekenland?</strong><br>Op vrijdag 13 november om 20:45 uur in de Johan Cruijff ArenA, live bij de NOS.</p>
<p>Meer over de bondscoach lees je in {L['xavi']}.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    alles = content + content2 + content3
    w = len(re.sub(r"<[^>]+>", " ", alles).split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", w, "woorden")
    assert len(TITEL) <= 60 and 120 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    n = sum(len(r[1].split("),")) for r in SELECTIE)
    assert n == 24, n
    namen = " ".join(r[1] for r in SELECTIE)
    assert "Van Dijk" not in namen and "Brobbey" not in namen and "Sepp van den Berg" in namen
    assert "1,49" in content3 and "24" in OG_TEGELS[0][1] and "24 spelers" in content
    assert "<h2" not in alles and "betcity" not in alles.lower() and "/go/" not in alles
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    print("dry run ok")
