# -*- coding: utf-8 -*-
"""Los artikel: de nieuwe opzet van de Nations League vanaf 2028/29 en wat die betekent voor Oranje (9-11-2026).
Feitenbrief met bronnen: specials/nations_league_2028_feiten.md (UEFA 20-05-2026 Istanbul, UEFA 15-09-2026 Thessaloniki,
reglement 2026/27 art. 15 en 19, OnsOranje, NOS, DFB). Odds Nederland – Griekenland: 711 (Kambi sevelevnl), 9-11 ±17:00.
Bewust NIET gebruikt (onbevestigd): aantal potten in de nieuwe groepen, maand van de Finals vanaf 2029, koppeling EK 2032,
gastheer Finals 2027, stadions Servië – Duitsland en Griekenland – Servië.
  python3 specials/nations_league_nieuwe_opzet_2028.py   (dry run)"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "nations-league-nieuwe-opzet-2028-wat-betekent-het-voor-oranje"
RUBRIEK = "66d6d655bc312d5c0e834ecd"   # zelfde rubriek als de andere Oranje-artikelen
TITEL = "Nieuwe opzet Nations League 2028: dit verandert voor Oranje"
SAMENVATTING = ("Vanaf 2028/29 drie leagues van 18 landen en groepen van zes. Wat verandert er, hoe telt deze editie mee "
                "en wat heeft Oranje nodig?")

# deelkaart: og_kaarten/gsod.py
OG_LOGO = "nations-league-logo.png"
OG_EYEBROW = "Nations League · Oranje"
OG_KOP = "Nieuwe opzet<br><em>vanaf 2028/29</em>"
OG_TEGELS = [("Leagues", "4 → 3"), ("Per groep", "6 landen")]
OG_KOPJE = "Wat verandert er en wat telt nu?"
OG_RECHTS = "Status"
OG_RIJEN = [("2028/29", "Drie leagues van 18 landen, League D verdwijnt", "Nieuw"),
            ("Groep", "6 duels tegen 5 verschillende tegenstanders", "Nieuw"),
            ("Top 18", "Eindstand 2026/27 = plek in League A", "Telt nu"),
            ("Oranje", "8 punten, kan niet meer laatste worden", "Groep A2")]

L = {"nlg": '<a href="/competities/uefa-nations-league">Nations League</a>',
     "uitleg": '<a href="/nieuws/hoe-werkt-de-nations-league-complete-uitleg-2026-2027">hoe de Nations League werkt</a>',
     "selectie": '<a href="/nieuws/selectie-oranje-november-2026-griekenland-duitsland">de selectie van Oranje voor november</a>',
     "nl": '<a href="/clubs/nederland">Nederland</a>',
     "de": '<a href="/clubs/duitsland">Duitsland</a>',
     "gr": '<a href="/clubs/griekenland">Griekenland</a>',
     "rs": '<a href="/clubs/servie">Servië</a>',
     "711": '<a href="/bookmakers/711">711</a>',
     "legaal": '<a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>'}

VERSCHIL = [
    ("<strong>Aantal leagues</strong>", "Vier: A, B, C en D", "Drie: A, B en C"),
    ("<strong>Landen per league</strong>", "16 in A, B en C; de rest in D", "18 per league"),
    ("<strong>Groepen</strong>", "Groepen van vier", "Drie groepen van zes per league"),
    ("<strong>Tegenstanders</strong>", "Drie, allemaal thuis en uit", "Vijf: één thuis en uit, vier één keer"),
    ("<strong>Groepsduels per land</strong>", "Zes", "Zes"),
    ("<strong>Kwartfinales, Finals, play-offs</strong>", "Ja", "Blijven bestaan"),
]

RANG = [
    ("1 t/m 4", "De vier landen in de Finals", "League A"),
    ("5 t/m 8", "De verliezende kwartfinalisten", "League A"),
    ("9 en 10", "De twee beste nummers drie van League A", "League A"),
    ("11 t/m 18", "Groepswinnaars van League B en winnaars van de A/B-play-offs", "League A"),
    ("19 t/m 36", "Degradanten en play-offverliezers uit A, de nummers 3 uit B, groepswinnaars uit C en winnaars van de B/C-play-offs", "League B"),
    ("37 en lager", "Verliezers van de B/C-play-offs, de nummers 3 en 4 uit C en alle landen uit League D", "League C"),
]

PROMDEG = [
    ("<strong>League A</strong>", "Nummers 1 en 2 naar de kwartfinales. De twee beste nummers 3 blijven in A. De twee slechtste nummers 3 en de twee beste nummers 4 spelen een A/B-play-off. De twee slechtste nummers 4 degraderen direct."),
    ("<strong>League B</strong>", "Groepswinnaars promoveren direct. Nummers 2 spelen een A/B-play-off, nummers 3 blijven in B, nummers 4 spelen een B/C-play-off. Niemand degradeert direct."),
    ("<strong>League C</strong>", "Groepswinnaars promoveren direct. Nummers 2 spelen een B/C-play-off, nummers 3 en 4 blijven in C."),
    ("<strong>League D</strong>", "Alle landen gaan naar League C, omdat League D verdwijnt."),
]

STAND = [("1", "Nederland", "4", "2-2-0", "7-5", "+2", "<strong>8</strong>"),
         ("2", "Griekenland", "4", "2-2-0", "5-3", "+2", "<strong>8</strong>"),
         ("3", "Duitsland", "4", "1-2-1", "3-2", "+1", "<strong>5</strong>"),
         ("4", "Servië", "4", "0-0-4", "3-8", "-5", "<strong>0</strong>")]

SCENARIO = [
    ("Winst", "Winst of gelijk", "14 of 12", "<strong>Groepswinst</strong>"),
    ("Winst", "Verlies", "11", "Kwartfinale vrijwel zeker; alleen bij een driekamp op 11 punten beslist het onderlinge doelsaldo"),
    ("Gelijk", "Winst", "12", "<strong>Kwartfinale zeker</strong>, groepswinst mogelijk"),
    ("Gelijk", "Gelijk", "10", "<strong>Kwartfinale zeker</strong>, Duitsland kan niet meer langszij"),
    ("Gelijk", "Verlies", "9", "Afhankelijk van Duitsland en Griekenland"),
    ("Verlies", "Winst", "11", "<strong>Kwartfinale zeker</strong>, als nummer 2"),
    ("Verlies", "Gelijk", "9", "Nummer 2 als Duitsland niet wint in Servië; anders beslist het totale doelsaldo"),
    ("Verlies", "Verlies", "8", "Derde plaats: geen kwartfinale"),
]

PROGRAMMA = [("Vr 13 november", "20:45", "Nederland – Griekenland", "Johan Cruijff ArenA, Amsterdam"),
             ("Vr 13 november", "20:45", "Servië – Duitsland", "Belgrado"),
             ("Ma 16 november", "20:45", "Duitsland – Nederland", "Olympiastadion, Berlijn"),
             ("Ma 16 november", "20:45", "Griekenland – Servië", "Griekenland")]

TIJDLIJN = [("13 en 16 november 2026", "Laatste groepsduels van Oranje"),
            ("17 november 2026", "Einde van de groepsfase"),
            ("25 t/m 30 maart 2027", "Kwartfinales (thuis en uit) en de A/B- en B/C-play-offs"),
            ("9 t/m 13 juni 2027", "Finals: halve finales op 9 en 10 juni, finale en troostfinale op 13 juni"),
            ("2028/29", "Eerste editie in de nieuwe opzet")]

content = f"""<p><strong>De {L['nlg']} krijgt vanaf het seizoen 2028/29 een nieuwe opzet. De vier leagues worden er drie, elke league telt 18 landen en de groepen worden groter: zes landen in plaats van vier. Elk land speelt nog steeds zes groepsduels, maar tegen vijf verschillende tegenstanders. De huidige editie 2026/27 is de laatste in het oude format, en de eindstand bepaalt in welke league een land aan het nieuwe tijdperk begint. Voor Oranje staat er daarom op 13 en 16 november meer op het spel dan alleen de kwartfinales.</strong></p>
<p>Het Uitvoerend Comité van de UEFA keurde het nieuwe concept goed op 20 mei 2026 in Istanbul. Op 15 september volgden in Thessaloniki aangepaste regels voor promotie en degradatie in de huidige editie, zodat de overstap naar drie leagues klopt. In dit artikel lees je wat er precies verandert, hoe de eindstand van 2026/27 de nieuwe indeling bepaalt en wat Oranje in de laatste twee groepsduels nodig heeft. Wil je eerst de basis weten? Lees dan {L['uitleg']}.</p>
<h3><strong>Wat verandert er vanaf 2028/29?</strong></h3>
{tabel(["", "Tot en met 2026/27", "Vanaf 2028/29"], VERSCHIL)}
<p>De grootste verandering zit in de groepen. Met zes landen per groep speel je niet meer steeds twee keer tegen dezelfde drie tegenstanders. Eén tegenstander speel je thuis en uit, de andere vier speel je één keer, thuis of uit. Het aantal wedstrijden blijft gelijk, dus er komen geen extra speeldagen bij. Je krijgt wel meer afwisseling: een land uit League A treft in de groepsfase vijf andere toplanden in plaats van drie.</p>
<p>League D verdwijnt helemaal. UEFA gaat in de nieuwe opzet uit van 55 landen, waardoor één groep in League C zeven landen telt. Nu doen er 54 landen mee, omdat Rusland is geschorst. De kwartfinales, de Finals met vier landen en de play-offs voor promotie en degradatie blijven bestaan.</p>"""

content2 = f"""<h3><strong>Ook de EK- en WK-kwalificatie gaat op de schop</strong></h3>
<p>Tegelijk met de Nations League verandert de kwalificatie voor eindtoernooien. Die blijft een aparte competitie, maar wordt ingedeeld op basis van de Nations League. De 36 landen uit League A en B vormen samen het hoogste niveau: drie groepen van twaalf, waarin elk land zes duels speelt tegen zes verschillende tegenstanders. De overige landen spelen een eigen kwalificatie, op dezelfde manier ingedeeld als League C. Ook zij houden via de play-offs een kans op een eindtoernooi.</p>
<p>UEFA zegt dat de nieuwe kwalificatie ingaat na het EK 2028. Volgens de Ierse omroep RTÉ geldt ze voor het eerst voor het WK 2030. Dat maakt een plek in League A of B extra waardevol: wie daar speelt, treft in de kwalificatie de sterkere landen en heeft meer directe tickets binnen bereik.</p>
<h3><strong>Waarom de eindstand van 2026/27 zo belangrijk is</strong></h3>
<p>Volgens het reglement van deze editie krijgt elk land aan het eind een plek op een ranglijst van 1 tot en met 54. De nummers 1 tot en met 18 beginnen in 2028/29 in League A, de nummers 19 tot en met 36 in League B, de rest in League C.</p>
{tabel(["Plek", "Wie", "Vanaf 2028/29"], RANG)}
<p>In League A van 2028/29 zitten dus de acht kwartfinalisten, de twee beste nummers drie, de vier groepswinnaars uit League B en de vier winnaars van de A/B-play-offs. Samen precies 18 landen.</p>
<h3><strong>Promotie en degradatie in deze editie</strong></h3>
<p>Om van vier naar drie leagues te gaan, zijn de regels voor promotie en degradatie dit seizoen aangepast. In League A degradeert geen enkele nummer drie direct.</p>
{tabel(["League", "Regels 2026/27"], PROMDEG)}
<p>De play-offs worden van 25 tot en met 30 maart 2027 over twee wedstrijden gespeeld. Het land uit de hogere league speelt de return thuis. Is het na twee duels gelijk, dan volgen een verlenging en zo nodig strafschoppen. Uitdoelpunten tellen niet extra.</p>
<h3><strong>Wat betekent de nieuwe Nations League voor Oranje?</strong></h3>
<p>{L['nl']} speelt in League A, groep A2, met {L['de']}, {L['gr']} en {L['rs']}. Na vier duels is Oranje nog ongeslagen. Het staat bovenaan door meer gemaakte doelpunten dan Griekenland.</p>
{tabel(["#", "Land", "G", "W-G-V", "Doelpunten", "Saldo", "Punten"], STAND)}
<p><em>Uitslagen van Oranje: Nederland – Duitsland 1-1, Servië – Nederland 1-2, Griekenland – Nederland 2-2 en Nederland – Servië 2-1.</em></p>
<p>Eén ding staat al vast: Oranje kan niet meer laatste worden, want Servië kan hooguit nog op zes punten komen. Rechtstreekse degradatie is dus uitgesloten. Eindigt Oranje bij de eerste twee, dan speelt het in maart de kwartfinales en begint het in 2028/29 zeker in League A. Bij een derde plek hangt het af van de vergelijking met de andere nummers drie: de beste twee blijven in League A, de andere twee moeten in maart een play-off spelen.</p>
<p><strong>Wat heeft Oranje nodig?</strong> Bij gelijke punten telt eerst het onderlinge resultaat, daarna pas het doelsaldo over alle groepsduels. Griekenland heeft het onderlinge duel met Duitsland al gewonnen (1-0 en 0-0). Tussen Nederland en Griekenland (2-2) en Nederland en Duitsland (1-1) is nog niets beslist.</p>
{tabel(["Tegen Griekenland", "In Berlijn", "Punten", "Uitkomst voor Oranje"], SCENARIO)}
<p>Kort gezegd: winst op Griekenland en een punt in Berlijn betekent groepswinst. Twee gelijke spelen zijn genoeg voor de kwartfinales, en een zege in Berlijn ook. Alleen bij twee nederlagen is Oranje zeker derde. De groepswinnaar speelt in maart de return van de kwartfinale thuis en kan niet loten tegen een land uit de eigen groep.</p>"""

content3 = f"""<h3><strong>Het programma van de laatste speelronden</strong></h3>
{tabel(["Datum", "Aftrap", "Wedstrijd", "Stadion"], [(f"<strong>{d}</strong>", t, w, s) for d, t, w, s in PROGRAMMA])}
<p>Beide wedstrijden van Oranje zijn live te zien op NPO 3. Bondscoach Xavi Hernández heeft 25 spelers opgeroepen. Frenkie de Jong is terug, Ryan Gravenberch en Jeremie Frimpong zijn geblesseerd. Alle namen lees je in {L['selectie']}. Duitsland, sinds deze editie onder leiding van Jürgen Klopp, staat drie punten achter Oranje en Griekenland.</p>
<p><strong>Wat zeggen de bookmakers?</strong> Oranje is duidelijk favoriet tegen Griekenland. Bij {L['711']} staat een Nederlandse zege op <strong>1,47</strong>, een gelijkspel op 4,90 en een Griekse zege op 7,00 (maandag 9 november). Voor Duitsland – Nederland zijn nog geen odds beschikbaar. Wed alleen bij een bookmaker met een vergunning van de Kansspelautoriteit; lees {L['legaal']}.</p>
<h3><strong>De belangrijkste data</strong></h3>
{tabel(["Wanneer", "Wat"], TIJDLIJN)}
<p>De gastheer van de Finals in juni 2027 is nog niet bekend; UEFA kiest die in december 2026.</p>
<h3><strong>Oranje in de Nations League tot nu toe</strong></h3>
<p>Er zijn vier edities gespeeld, met drie verschillende winnaars: Portugal (2019 en 2025), Frankrijk (2021) en Spanje (2023). Oranje haalde in 2019 de finale, het beste resultaat tot nu toe: na een 3-1-zege op Engeland in de halve finale verloor het in Porto met 1-0 van Portugal. In 2023 werd Nederland als gastland vierde. In 2025 ging Oranje in de kwartfinale tegen Spanje na 5-5 over twee duels pas na strafschoppen onderuit.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wat verandert er aan de Nations League vanaf 2028?</strong><br>Vanaf 2028/29 zijn er drie leagues van 18 landen in plaats van vier. League D verdwijnt. Elke league heeft drie groepen van zes, en elk land speelt zes duels tegen vijf verschillende tegenstanders.</p>
<p><strong>Is de Nations League 2026/27 de laatste in de oude opzet?</strong><br>Ja. De eindstand van deze editie bepaalt de indeling: plek 1 tot en met 18 gaat naar League A, plek 19 tot en met 36 naar League B en de rest naar League C.</p>
<p><strong>Kan Oranje nog degraderen uit League A?</strong><br>Niet rechtstreeks. Oranje kan niet meer laatste worden in groep A2. Bij een derde plek speelt Oranje alleen een play-off als het bij de twee slechtste nummers drie van League A hoort.</p>
<p><strong>Wat heeft Oranje nodig voor de kwartfinales?</strong><br>Een plek bij de eerste twee in groep A2. Twee gelijke spelen zijn genoeg, net als een zege in Berlijn. Winst op Griekenland en een punt in Berlijn levert groepswinst op.</p>
<p><strong>Wanneer zijn de kwartfinales van de Nations League?</strong><br>Van 25 tot en met 30 maart 2027, in een thuis- en een uitwedstrijd. De Finals volgen van 9 tot en met 13 juni 2027.</p>
<p><strong>Verandert de EK-kwalificatie ook?</strong><br>Ja. Na het EK 2028 wordt de kwalificatie ingedeeld op basis van de Nations League: de 36 landen uit League A en B spelen samen in drie groepen van twaalf, de overige landen in een eigen kwalificatie.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    alles = content + content2 + content3
    w = len(re.sub(r"<[^>]+>", " ", alles).split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", w, "woorden")
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert 1200 <= w <= 2400, w
    # stand en scenario's controleren
    pt = {"NED": 8, "GRE": 8, "GER": 5, "SRB": 0}
    assert pt["SRB"] + 6 < pt["NED"] + 0 or pt["SRB"] + 6 < 8  # Servië max 6 < 8: Oranje nooit vierde
    assert 8 + 1 + 1 > 5 + 3 + 1   # twee keer gelijk (10) > Duitsland max zonder winst op NL (9)
    assert 4 + 4 + 8 + 2 == 18      # opbouw League A 2028/29
    assert "<h2" not in alles and "betcity" not in alles.lower() and "/go/" not in alles
    assert content.startswith("<p><strong>") and content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    print("dry run ok")
