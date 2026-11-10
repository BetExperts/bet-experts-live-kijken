# -*- coding: utf-8 -*-
"""Los artikel: Virgil van Dijk en Brian Brobbey melden zich af bij Oranje (maandag 9-11-2026, ±17:45).
Bronnen:
- NOS 9-11-2026 17:47 (nos.nl/artikel/2638755): beide niet voldoende fit na clubduels in het weekend (Liverpool, Sunderland),
  geen vervangers, selectie nu 23; Van Dijk speelde zijn 100e interland tegen Servië (2-1, begin oktober); Brobbey viel tegen
  Duitsland (1-1) na ruim een halfuur geblesseerd uit in zijn 17e interland; Xavi zei eerder die dag dat Brobbey zich goed voelde.
- Bevestigd door Soccernews, Voetbalprimeur, Dagblad010 (9-11).
- Selectie (25 -> 23): specials/selectie_oranje_november_2026.py (OnsOranje 6-11). Stand/scenario's: nations_league_2028_feiten.md.
- Odds 711 (Kambi) 9-11 ±19:00: Nederland – Griekenland 1,47 / 4,90 / 7,00 (ongewijzigd na het nieuws).
Update di 10-11-2026 (±14:25), feiten + URL's in specials/nations_league_2028_feiten.md §6b:
- Bevestiging KNVB: OnsOranje 9-11 17:45 (onsoranje.nl/.../82817): niet fit uit het speelweekend, selectie vooralsnog 23.
- Vervanger: Sepp van den Berg (Brentford, 24) voor het eerst opgeroepen, meldt zich di-avond in Zeist, selectie 24
  (OnsOranje 82822; NOS 2638854 13:06 "als vervanger Van Dijk"; VI 12:53). Geen vervanger voor Brobbey.
- Training: ma-avond alleen Dumfries, Summerville, Reijnders buiten (NOS 2638755/2638812); di 23 fitte spelers (ANP via nieuws.nl 12:28).
- Aanvoerder: niet bekendgemaakt; Xavi noemde De Jong "een van onze aanvoerders" (NOS 2638812, 10-11 07:00).
- Odds 711 (Kambi) di 10-11 14:25: 1,49 / 4,60 / 6,75; Duitsland – Nederland nog niet beschikbaar.
Bewust NIET: aard van de blessures (niet bekend), wie de aanvoerdersband krijgt (niet bekend; bekendmaking donderdag
alleen gespeculeerd), uitspraak De Jong over de band (alleen via een tv-interview van een niet te noemen zender).
  python3 specials/van_dijk_brobbey_afgemeld_oranje_2026.py   (dry run)"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "van-dijk-brobbey-afgemeld-oranje-griekenland-duitsland"
RUBRIEK = "66d6d655bc312d5c0e834ecd"
TITEL = "Van Dijk en Brobbey af bij Oranje, Van den Berg erbij"
SAMENVATTING = ("Van Dijk en Brobbey zijn niet fit voor Griekenland en Duitsland. Xavi roept Sepp van den Berg op als "
                "vervanger van Van Dijk, voor Brobbey komt niemand.")

OG_LOGO = "nederland-logo.png"
OG_EYEBROW = "Oranje · Nations League"
OG_KOP = "Van Dijk en Brobbey af<br><em>Van den Berg erbij</em>"
OG_TEGELS = [("Selectie", "24"), ("Vervangers", "1")]
OG_KOPJE = "Afmeldingen en programma"
OG_RECHTS = "Status"
OG_RIJEN = [("Van Dijk", "Aanvoerder, centrale verdediger (Liverpool)", "Niet fit"),
            ("Brobbey", "Spits (Sunderland)", "Niet fit"),
            ("Van den Berg", "Centrale verdediger (Brentford)", "Nieuw"),
            ("Vr 13/11", "Nederland – Griekenland, 20:45, NPO 3", "Thuis")]

L = {"selectie": '<a href="/nieuws/selectie-oranje-november-2026-griekenland-duitsland">de selectie van Oranje voor november</a>',
     "ned_gre": '<a href="/nieuws/nederland-griekenland-hoe-laat-tv-stadion-opstelling-13-november-2026">Nederland – Griekenland: hoe laat, tv en opstelling</a>',
     "dui_ned": '<a href="/nieuws/duitsland-nederland-hoe-laat-tv-stadion-16-november-2026">Duitsland – Nederland: hoe laat, tv en stadion</a>',
     "opstelling": '<a href="/nieuws/opstelling-oranje-vandaag">opstelling Oranje vandaag</a>',
     "rekenwerk": '<a href="/nieuws/nations-league-nieuwe-opzet-2028-wat-betekent-het-voor-oranje">wat Oranje nodig heeft in de Nations League</a>',
     "nl": '<a href="/clubs/nederland">Nederlands elftal</a>',
     "711": '<a href="/bookmakers/711">711</a>',
     "legaal": '<a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>'}

SELECTIE = [
    ("<strong>Keepers (3)</strong>", "Mark Flekken, Robin Roefs, Bart Verbruggen"),
    ("<strong>Verdedigers (7)</strong>", "Denzel Dumfries, Lutsharel Geertruida, Jan Paul van Hecke, Ian Maatsen, Jurriën Timber, Micky van de Ven, Sepp van den Berg"),
    ("<strong>Middenvelders (8)</strong>", "Frenkie de Jong, Justin Kluivert, Teun Koopmeiners, Tijjani Reijnders, Quinten Timber, Joey Veerman, Gjivai Zechiël, Guus Til"),
    ("<strong>Aanvallers (6)</strong>", "Donyell Malen, Ruben van Bommel, Cody Gakpo, Noa Lang, Crysencio Summerville, Mexx Meerdink"),
]

PROGRAMMA = [("Vrijdag 13 november", "20:45", "Nederland – Griekenland", "Johan Cruijff ArenA", "NPO 3"),
             ("Maandag 16 november", "20:45", "Duitsland – Nederland", "Olympiastadion, Berlijn", "NPO 3")]

content = f"""<p><strong>Oranje speelt de laatste twee groepsduels in de Nations League zonder aanvoerder Virgil van Dijk en spits Brian Brobbey. De KNVB bevestigde maandagavond 9 november dat beide spelers niet fit genoeg zijn voor Nederland – Griekenland (vrijdag 13 november) en Duitsland – Nederland (maandag 16 november). Een dag later riep bondscoach Xavi Hernández Sepp van den Berg van Brentford op als vervanger van Van Dijk. Voor Brobbey komt er niemand bij. De selectie telt nu 24 spelers.</strong></p>
<p><strong>Update dinsdag 10 november, 14:30 uur:</strong> Maandag hield Xavi de selectie nog op 23 spelers, dinsdag riep hij toch een vervanger op. Centrale verdediger <strong>Sepp van den Berg</strong> (24) krijgt zijn eerste oproep voor Oranje en meldt zich dinsdagavond in Zeist. Hij kan vrijdag tegen Griekenland of maandag in Berlijn debuteren. Wie de aanvoerdersband overneemt, is nog niet bekendgemaakt. Op de training van dinsdag stonden 23 fitte spelers op het veld; nieuwe afmeldingen of twijfelgevallen zijn niet gemeld.</p>
<p>Het nieuws kwam een paar uur nadat Xavi op zijn persconferentie nog positief was over Brobbey. Hij had de spits gesproken en die voelde zich goed, zei de bondscoach, al wilde hij eerst de medische check afwachten. Die viel dus verkeerd uit. Beide spelers stonden afgelopen weekend nog op het veld in de Premier League: Van Dijk voor Liverpool, Brobbey voor Sunderland, dat zondag met 1-0 van Chelsea won. Wat ze precies mankeren, is niet bekendgemaakt.</p>
<h3><strong>Wat er gebeurd is in het kort</strong></h3>
{tabel(["", "Virgil van Dijk", "Brian Brobbey"], [
    ("<strong>Positie</strong>", "Centrale verdediger, aanvoerder", "Spits"),
    ("<strong>Club</strong>", "Liverpool", "Sunderland"),
    ("<strong>Laatste interland</strong>", "Nederland – Servië 2-1 (oktober), zijn 100e", "Nederland – Duitsland 1-1 (september), na ruim een halfuur geblesseerd eraf"),
    ("<strong>Interlands</strong>", "100", "17"),
    ("<strong>Status</strong>", "Niet fit, afgemeld", "Niet fit, afgemeld"),
])}
<p><em>Bron: KNVB (maandag 9 november, 17:45 uur) en de NOS. Op dinsdag 10 november werd Sepp van den Berg opgeroepen als vervanger van Van Dijk.</em></p>"""

content2 = f"""<h3><strong>Wie vervangt Van Dijk centraal achterin?</strong></h3>
<p>Het wegvallen van Van Dijk is de grootste klap. De aanvoerder is al jaren de vaste waarde in het centrum van de defensie en speelde in oktober tegen Servië zijn honderdste interland. Met Nathan Aké, die al geblesseerd ontbrak, is Xavi nu twee ervaren centrale verdedigers kwijt.</p>
<p>Xavi haalde er met <strong>Sepp van den Berg</strong> een extra centrale verdediger bij. De 24-jarige debuteerde op zijn zestiende bij PEC Zwolle, vertrok in 2019 naar Liverpool en werd daarna verhuurd aan onder meer Schalke 04 en Mainz. Sinds 2024 speelt hij bij Brentford, waar hij na een blessure de laatste vier competitieduels in de basis begon. Hij speelde acht duels voor Jong Oranje, maar nog geen interland. Dat hij direct basisspeler wordt, ligt niet voor de hand.</p>
<p>De meest voor de hand liggende vervangers zitten namelijk al in de groep. <strong>Jan Paul van Hecke</strong> en <strong>Micky van de Ven</strong>, ploeggenoten bij Tottenham Hotspur, vormen een duo dat elkaar kent. <strong>Jurriën Timber</strong> kan zowel rechtsback als centraal spelen, en <strong>Lutsharel Geertruida</strong> is ook in het centrum inzetbaar. Xavi liet in oktober al zien dat hij durft te schuiven: tegen Servië stond <strong>Teun Koopmeiners</strong> centraal achterin. Wie de aanvoerdersband overneemt, heeft Xavi nog niet gezegd. Hij noemde Frenkie de Jong deze week wel "een van onze aanvoerders" en zei dat de middenvelder een leider moet zijn. Ook Denzel Dumfries wordt in de media als kandidaat genoemd.</p>
<h3><strong>Wie speelt er in de spits?</strong></h3>
<p>In de spits is de keuze ruimer. <strong>Mexx Meerdink</strong> van AZ scoorde in september twee keer bij de 1-2-zege in Belgrado en is de enige pure spits die overblijft. <strong>Donyell Malen</strong> is terug na een blessure en Xavi zei op zijn persconferentie van maandag dat hij de aanvaller van AS Roma vertrouwen wil geven om ook in Oranje te scoren. Daarnaast kan <strong>Cody Gakpo</strong> centraal spelen, net als <strong>Noa Lang</strong> en <strong>Justin Kluivert</strong> in een beweeglijkere voorhoede. Voor Brobbey roept Xavi geen vervanger op. Joshua Zirkzee, die in oktober nog scoorde tegen Servië, wordt dus ook niet bijgeroepen.</p>
<h3><strong>De selectie van Oranje (24 spelers)</strong></h3>
{tabel(["Linie", "Spelers"], SELECTIE)}
<p><em>Selectie na de afmeldingen van Van Dijk en Brobbey en de oproep van Van den Berg (dinsdag 10 november). Clubs en de volledige oorspronkelijke lijst staan in {L['selectie']}.</em></p>
<h3><strong>Wat betekent het voor de wedstrijden?</strong></h3>
<p>Er staat veel op het spel. Oranje en Griekenland staan in groep A2 allebei op acht punten, Duitsland heeft er vijf. De eerste twee gaan naar de kwartfinales, en de eindstand bepaalt ook in welke league Oranje in de nieuwe opzet vanaf 2028/29 begint. Wint Oranje vrijdag van Griekenland en haalt het maandag een punt in Berlijn, dan is de groepswinst binnen. Alle scenario's lees je in {L['rekenwerk']}.</p>
{tabel(["Datum", "Aftrap", "Wedstrijd", "Stadion", "Tv"], [(f"<strong>{d}</strong>", t, w, s, tv) for d, t, w, s, tv in PROGRAMMA])}
<p>De officiële opstelling verschijnt ongeveer een uur voor de aftrap op onze pagina {L['opstelling']}. Meer over de wedstrijden lees je in {L['ned_gre']} en {L['dui_ned']}.</p>"""

content3 = f"""<h3><strong>Wat zeggen de bookmakers?</strong></h3>
<p>De bookmakers reageerden nauwelijks op het nieuws. Bij {L['711']} stond een Nederlandse zege tegen Griekenland op maandagavond op 1,47. Op dinsdag 10 november om 14:25 uur was dat <strong>1,49</strong>, met 4,60 voor een gelijkspel en 6,75 voor een Griekse zege. Voor Duitsland – Nederland zijn nog geen odds beschikbaar. Odds kunnen tot de aftrap nog veranderen, zeker als de opstellingen bekend zijn. Wed alleen bij een bookmaker met een vergunning van de Kansspelautoriteit; lees {L['legaal']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Waarom hebben Van Dijk en Brobbey zich afgemeld?</strong><br>Beide spelers zijn volgens de KNVB niet voldoende fit. Wat ze precies mankeren, is niet bekendgemaakt. Ze speelden afgelopen weekend nog in de Premier League.</p>
<p><strong>Wie vervangt Van Dijk in de selectie?</strong><br>Sepp van den Berg van Brentford. Xavi riep de centrale verdediger op dinsdag 10 november voor het eerst op. Voor Brobbey komt geen vervanger, de selectie telt nu 24 spelers.</p>
<p><strong>Wie wordt aanvoerder van Oranje zonder Van Dijk?</strong><br>Dat heeft Xavi nog niet bekendgemaakt. Frenkie de Jong, door Xavi "een van onze aanvoerders" genoemd, ligt het meest voor de hand.</p>
<p><strong>Wie speelt in de spits zonder Brobbey?</strong><br>Mexx Meerdink, Donyell Malen en Cody Gakpo zijn de belangrijkste kandidaten. Meerdink scoorde in september twee keer tegen Servië.</p>
<p><strong>Wanneer speelt Oranje?</strong><br>Vrijdag 13 november om 20:45 uur tegen Griekenland in de Johan Cruijff ArenA en maandag 16 november om 20:45 uur tegen Duitsland in Berlijn. Beide wedstrijden zijn live op NPO 3.</p>
<p>Meer over het team lees je op onze pagina over het {L['nl']}.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    alles = content + content2 + content3
    w = len(re.sub(r"<[^>]+>", " ", alles).split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", w, "woorden")
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert 700 <= w <= 2000, w
    n = sum(len(r[1].split(", ")) for r in SELECTIE)
    assert n == 24, n
    assert "Sepp van den Berg" in " ".join(r[1] for r in SELECTIE)
    assert "1,49" in content3 and "24 spelers" in content and OG_TEGELS[0][1] == "24"
    assert "Van Dijk" not in " ".join(r[1] for r in SELECTIE) and "Brobbey" not in " ".join(r[1] for r in SELECTIE)
    assert "<h2" not in alles and "betcity" not in alles.lower() and "/go/" not in alles
    assert content.startswith("<p><strong>") and content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    print("dry run ok")
