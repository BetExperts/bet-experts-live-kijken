# -*- coding: utf-8 -*-
"""Los informatief SEO-artikel: Rolex Paris Masters 2026 (ATP Masters 1000, 2-8 november 2026, Plenitude Arena / Paris
La Défense Arena, Nanterre). Geschreven op maandag 2-11-2026, dag 1 van het hoofdtoernooi.
UPDATE dinsdag 10-11-2026: toernooi voorbij. Carlos Alcaraz won de finale van Ben Shelton (7-6(5) 7-5); artikel omgezet
naar 'winnaar en uitslagen' (verleden tijd, uitslagen per ronde, Nederlanders/Belgen, dubbel, gevolgen Turijn). SLUG gelijk.
Zoekwoorden (Google NL-suggesties + GSC okt-nov 2025): paris masters 2026, masters parijs, rolex paris masters, paris masters
winnaar / uitslag / uitslagen, atp parijs (schema, op tv, prijzengeld), tennis parijs finale, paris masters finale,
paris masters prijzengeld, paris masters winnaar 2025/2026, bercy tennis 2026, la defense arena tennis.
Feiten: specials/paris_masters_feiten_2026.md (ATP-toernooigids, prijzengeld, Ziggo, winnaarslijst) en
specials/paris_masters_uitslag_feiten_2026.md (officiële toernooi-API 2..8-11, officiële artikelen, ATP, Tennis Majors,
Al Jazeera, AP; gecontroleerd 10-11 14:00-14:25). Onzeker en daarom weggelaten: winners-aantallen finale (API en TM
verschillen), reden afwezigheid Blockx, loting ATP Finals. Okker-titels (voorganger, vóór 1986) vaag gehouden.
Webflow-item-id: niet bekend in deze module (hoofdsessie zoekt op SLUG).
  python3 specials/paris_masters_2026.py   (dry run)
  kaart: ../superodd-agent/.venv/bin/python og_kaarten/gsod.py paris_masters_2026 (OG_LOGO)"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "paris-masters-2026-schema-tijden-tv-deelnemers-prijzengeld"
RUBRIEK = "665715dbf1f3cbdf7f874d79"   # Tennis
TITEL = "Paris Masters 2026: winnaar Alcaraz en alle uitslagen"
SAMENVATTING = ("Carlos Alcaraz wint de Paris Masters 2026 met 7-6 7-5 van Ben Shelton. Alle uitslagen, de Nederlanders, "
                "prijzengeld, tv en de lijst met winnaars.")

OG_LOGO = "paris-masters-logo.png"
OG_EYEBROW = "Tennis · ATP Masters 1000"
OG_KOP = "Paris Masters<br><em>2026</em>"
OG_TEGELS = [("Winnaar", "Alcaraz"), ("Finale", "7-6 7-5")]
OG_KOPJE = "Uitslagen slotdagen"
OG_RECHTS = "8 november 2026"
OG_RIJEN = [("Finale", "Alcaraz – Shelton", "7-6 7-5"),
            ("Halve finale", "Alcaraz – Ruud", "6-4 6-4"),
            ("Halve finale", "Shelton – Van Assche", "2-1 sets"),
            ("Prijzengeld", "Winnaar Alcaraz", "€974.370")]

L = {"oud": '<a href="/nieuws/atp-1000-parijs-live-gratis-kijken-in-nederland-tv-gids-ziggo-sport-en-gratis-opties-griekspoor-alcaraz-sinner-en-meer-in-actie">ons artikel over live kijken naar de ATP in Parijs</a>',
     "finale": '<a href="/nieuws/finale-paris-masters-2026-wanneer-hoe-laat-tv">het verslag van de finale</a>',
     "wiewint": '<a href="/nieuws/wie-wint-paris-masters-2026-favorieten-odds-voorspelling">hoe de favorieten het deden</a>',
     "turijn": '<a href="/nieuws/atp-finals-2026-gekwalificeerd-race-to-turin">de spelers die zich plaatsten voor de ATP Finals in Turijn</a>',
     "tips": '<a href="/tennis-voorspellingen-vandaag">tennisvoorspellingen van vandaag</a>',
     "duur": '<a href="/nieuws/hoe-lang-duurt-een-tenniswedstrijd">hoe lang een tenniswedstrijd duurt</a>',
     "ziggo": '<a href="/zenders/ziggo-sport">Ziggo Sport</a>',
     "kijken": '<a href="/live-kijken">live kijken</a>'}

UITSLAGEN = [  # (ronde, dag, winnaar – verliezer, score)
    ("Finale", "Zo 8 nov", "Carlos Alcaraz (2) – Ben Shelton (3)", "7-6(5) 7-5"),
    ("Halve finale", "Za 7 nov", "Carlos Alcaraz (2) – Casper Ruud", "6-4 6-4"),
    ("Halve finale", "Za 7 nov", "Ben Shelton (3) – Luca Van Assche", "5-7 6-3 6-4"),
    ("Kwartfinale", "Vr 6 nov", "Carlos Alcaraz (2) – Taylor Fritz (11)", "6-7(10) 7-5 6-3"),
    ("Kwartfinale", "Vr 6 nov", "Casper Ruud – Nuno Borges", "7-6(5) 6-4"),
    ("Kwartfinale", "Vr 6 nov", "Ben Shelton (3) – Tommy Paul (12)", "6-4 4-6 6-3"),
    ("Kwartfinale", "Vr 6 nov", "Luca Van Assche – Rinky Hijikata", "6-4 6-7(4) 7-5"),
]

LAATSTE16 = [  # do 5 nov
    ("Luca Van Assche – Lorenzo Musetti", "7-5 3-6 6-4"), ("Rinky Hijikata – Tomás Martín Etcheverry", "2-6 6-3 7-5"),
    ("Ben Shelton (3) – Arthur Rinderknech", "3-6 6-4 7-6(5)"), ("Tommy Paul (12) – Quentin Halys", "7-6(3) 6-4"),
    ("Casper Ruud – Jan-Lennard Struff", "6-3 6-3"), ("Nuno Borges – Ignacio Buse", "6-0 6-2"),
    ("Taylor Fritz (11) – Arthur Fils (6)", "6-3 6-4"), ("Carlos Alcaraz (2) – Matteo Berrettini", "walkover"),
]

GEPLAATST = [  # (plaatsing, speler, land, resultaat)
    (1, "Alexander Zverev", "Duitsland", "2e ronde, verloor van Musetti"),
    (2, "Carlos Alcaraz", "Spanje", "<strong>Winnaar</strong>"),
    (3, "Ben Shelton", "Verenigde Staten", "Finale, verloor van Alcaraz"),
    (4, "Daniil Medvedev", "–", "2e ronde, verloor van Buse"),
    (5, "Flavio Cobolli", "Italië", "Afgemeld (linkerbeen)"),
    (6, "Arthur Fils", "Frankrijk", "Laatste 16, verloor van Fritz"),
    (7, "Frances Tiafoe", "Verenigde Staten", "2e ronde, verloor van Halys"),
    (8, "Alex de Minaur", "Australië", "2e ronde, verloor van Etcheverry"),
    (9, "Rafael Jódar", "Spanje", "2e ronde, verloor van Ruud"),
    (10, "Novak Djokovic", "Servië", "2e ronde, verloor van Hijikata"),
    (11, "Taylor Fritz", "Verenigde Staten", "Kwartfinale, verloor van Alcaraz"),
    (12, "Tommy Paul", "Verenigde Staten", "Kwartfinale, verloor van Shelton"),
    (13, "Alejandro Davidovich Fokina", "Spanje", "Afgemeld (rug)"),
    (14, "Brandon Nakashima", "Verenigde Staten", "1e ronde, verloor van Berrettini"),
    (15, "Learner Tien", "Verenigde Staten", "2e ronde, verloor van Van Assche"),
    (16, "Francisco Cerúndolo", "Argentinië", "1e ronde, opgave tegen Rinderknech"),
]

PRIJZEN = [("Winnaar", "€974.370", "1000"), ("Finalist", "€532.120", "650"), ("Halve finale", "€290.960", "400"),
           ("Kwartfinale", "€158.700", "200"), ("Laatste 16", "€84.890", "100"), ("2e ronde", "€45.520", "50"),
           ("1e ronde", "€25.220", "10"), ("Kwalificatie, 2e ronde", "€12.920", "–"), ("Kwalificatie, 1e ronde", "€6.765", "–")]

WINNAARS = [  # (jaar, winnaar, finalist, uitslag)
    ("2026", "Carlos Alcaraz", "Ben Shelton", "7-6 7-5"),
    ("2025", "Jannik Sinner", "Félix Auger-Aliassime", "6-4 7-6"), ("2024", "Alexander Zverev", "Ugo Humbert", "6-2 6-2"),
    ("2023", "Novak Djokovic", "Grigor Dimitrov", "6-4 6-3"), ("2022", "Holger Rune", "Novak Djokovic", "3-6 6-3 7-5"),
    ("2021", "Novak Djokovic", "Daniil Medvedev", "4-6 6-3 6-3"), ("2020", "Daniil Medvedev", "Alexander Zverev", "5-7 6-4 6-1"),
    ("2019", "Novak Djokovic", "Denis Shapovalov", "6-3 6-4"), ("2018", "Karen Khachanov", "Novak Djokovic", "7-5 6-4"),
    ("2017", "Jack Sock", "Filip Krajinović", "5-7 6-4 6-1"), ("2016", "Andy Murray", "John Isner", "6-3 6-7 6-4"),
    ("2015", "Novak Djokovic", "Andy Murray", "6-2 6-4"), ("2014", "Novak Djokovic", "Milos Raonic", "6-2 6-3"),
    ("2013", "Novak Djokovic", "David Ferrer", "7-5 7-5"), ("2012", "David Ferrer", "Jerzy Janowicz", "6-4 6-3"),
    ("2011", "Roger Federer", "Jo-Wilfried Tsonga", "6-1 7-6"), ("2010", "Robin Söderling", "Gaël Monfils", "6-1 7-6"),
    ("2009", "Novak Djokovic", "Gaël Monfils", "6-2 5-7 7-6"), ("2008", "Jo-Wilfried Tsonga", "David Nalbandian", "6-3 4-6 6-4"),
    ("2007", "David Nalbandian", "Rafael Nadal", "6-4 6-0"), ("2006", "Nikolay Davydenko", "Dominik Hrbatý", "6-1 6-2 6-2"),
]

content = f"""<p><strong>Carlos Alcaraz heeft de Rolex Paris Masters 2026 gewonnen. De Spanjaard versloeg op zondag 8 november in de finale Ben Shelton met 7-6(5) 7-5, na 1 uur en 57 minuten. Het is zijn eerste titel in Parijs en zijn negende Masters 1000-titel. Alcaraz verdiende €974.370 en 1000 rankingpunten. In het dubbelspel wonnen de Fransen Quentin Halys en Pierre-Hugues Herbert. Nederlanders en Belgen speelden geen rol: Botic van de Zandschulp en Zizou Bergs verloren in de eerste ronde.</strong></p>
<p><strong>Update dinsdag 10 november:</strong> de Paris Masters is voorbij. Hieronder staan de uitslagen van de kwartfinales tot en met de finale, de resultaten van de geplaatste spelers, het prijzengeld en de gevolgen voor de ATP Finals in Turijn, die zondag 15 november beginnen. Het complete verslag van de eindstrijd lees je in {L['finale']}.</p>
<h3><strong>Paris Masters 2026 in het kort</strong></h3>
{tabel(None, [
    ("<strong>Winnaar</strong>", "Carlos Alcaraz (Spanje, 2e geplaatst)"),
    ("<strong>Finale</strong>", "Alcaraz – Ben Shelton 7-6(5) 7-5, zondag 8 november"),
    ("<strong>Halve finalisten</strong>", "Casper Ruud en Luca Van Assche"),
    ("<strong>Dubbelspel</strong>", "Quentin Halys/Pierre-Hugues Herbert (Frankrijk)"),
    ("<strong>Toernooi</strong>", "Rolex Paris Masters, ATP Masters 1000; jubileumjaar, 40 jaar na de eerste editie in 1986"),
    ("<strong>Data</strong>", "Hoofdtoernooi maandag 2 t/m zondag 8 november 2026; kwalificatie 31 oktober en 1 november"),
    ("<strong>Locatie</strong>", "Plenitude Arena (Paris La Défense Arena), Nanterre, net buiten Parijs"),
    ("<strong>Ondergrond</strong>", "Hardcourt, indoor"),
    ("<strong>Prijzengeld</strong>", "€6.309.095 in totaal, €974.370 voor de winnaar"),
    ("<strong>Titelverdediger</strong>", "Jannik Sinner (speelde niet, geblesseerd)"),
])}
<h3><strong>Uitslagen Paris Masters 2026: kwartfinales tot en met de finale</strong></h3>
{tabel(["Ronde", "Dag", "Winnaar – verliezer", "Uitslag"], [
    (f"<strong>{r}</strong>", d, w, u) for r, d, w, u in UITSLAGEN
])}
<p>De finale begon zondag om 15:00 uur. Alcaraz gaf in het hele toernooi slechts één set weg, in de kwartfinale tegen Taylor Fritz. Daarin redde hij twee matchpunten. Shelton had in de halve finale drie sets nodig tegen de Fransman Luca Van Assche, die als ongeplaatste speler zijn eerste halve finale op Masters 1000-niveau haalde.</p>
<h3><strong>Uitslagen laatste 16 (donderdag 5 november)</strong></h3>
{tabel(["Winnaar – verliezer", "Uitslag"], [(w, u) for w, u in LAATSTE16])}
<p><em>Uitslagen volgens de officiële toernooisite. Matteo Berrettini trok zich voor zijn partij tegen Alcaraz terug met een elleboogblessure.</em></p>"""

content2 = f"""<h3><strong>Zo won Alcaraz de finale</strong></h3>
<p>Shelton begon het sterkst. Hij serveerde goed en kreeg in de eerste set zes breakpunten, maar Alcaraz redde ze allemaal. De tiebreak ging na 65 minuten met 7-5 naar de Spanjaard. In de tweede set brak Shelton bij 2-2, onder meer door een dubbele fout van Alcaraz. Die brak terug naar 4-4 en won tussen 2-4 en 5-4 twaalf van de vijftien punten. Bij 5-6 op de service van Shelton maakte Alcaraz het af op zijn tweede matchpunt.</p>
<p>Shelton sloeg meer aces (13 tegen 6), maar Alcaraz won de belangrijke punten: hij redde zes van de zeven breakpunten en benutte er twee van de vijf. Voor Alcaraz was het ook een revanche: Shelton had hem in september in de kwartfinale van de US Open verslagen. Alcaraz is nu de tweede Spaanse winnaar van het toernooi, na David Ferrer in 2012. Meer cijfers en citaten lees je in {L['finale']}.</p>
<h3><strong>Geplaatste spelers: hoe ver kwamen ze?</strong></h3>
<p>Aan het enkelspel deden 56 spelers mee; de top-8 had een bye in de eerste ronde. Van de favorieten haakten er veel vroeg af. Nummer één Alexander Zverev verloor in de tweede ronde van Lorenzo Musetti, Daniil Medvedev van Ignacio Buse en Novak Djokovic, zevenvoudig winnaar, van kwalificant Rinky Hijikata. Lees ook {L['wiewint']}.</p>
{tabel(["Plaatsing", "Speler", "Land", "Resultaat"], [(f"<strong>{n}</strong>", s, l, r) for n, s, l, r in GEPLAATST])}
<p>Titelverdediger Jannik Sinner speelde niet door een knieblessure. Ook Félix Auger-Aliassime, finalist van vorig jaar, en João Fonseca hadden zich vooraf afgemeld.</p>
<h3><strong>Nederlanders en Belgen op de Paris Masters 2026</strong></h3>
{tabel(["Speler", "Resultaat"], [
    ("<strong>Botic van de Zandschulp</strong> 🇳🇱", "1e ronde: verloor van Ugo Humbert, 7-6(5) 6-7(9) 6-3"),
    ("<strong>Tallon Griekspoor</strong> 🇳🇱", "Kwalificatie: verloor van Benjamin Bonzi, 6-3 6-7 6-3"),
    ("<strong>David Pel</strong> 🇳🇱", "Dubbelspel met Sadio Doumbia: won van Martos Gornes/Walkow (6-4 6-4), verloor daarna van Heliövaara/Patten (2-6 6-4 10-6)"),
    ("<strong>Zizou Bergs</strong> 🇧🇪", "1e ronde: verloor van Ignacio Buse, 6-2 6-4"),
    ("<strong>Alexander Blockx</strong> 🇧🇪", "Niet gestart; lucky loser Báez nam zijn plaats in"),
])}
<p>Van de Zandschulp hield Humbert ruim tweeënhalf uur bezig, maar verloor ook zijn zesde ATP-partij tegen de Fransman. Jesper de Jong stond niet op de deelnemerslijst. David Goffin, jarenlang de beste Belg, is gestopt met tennis.</p>
<h3><strong>Gevolgen voor de ATP Finals in Turijn</strong></h3>
<p>Parijs was de laatste kans om punten te halen voor de ATP Finals in Turijn (15 tot en met 22 november). Het veld van acht is compleet: Alexander Zverev, Carlos Alcaraz, Ben Shelton, Daniil Medvedev, Flavio Cobolli, Arthur Fils, Frances Tiafoe en Rafael Jódar. Fils was al tijdens de toernooiweek zeker. Tiafoe plaatste zich door de zege van Shelton op Tommy Paul, Jódar doordat Fritz in de kwartfinale van Alcaraz verloor. Fritz en Alex de Minaur gaan als reserve mee naar Turijn; Paul en Djokovic vielen af. Lees meer over {L['turijn']}.</p>
<h3><strong>Format</strong></h3>
<p>Het enkelspel telde 56 spelers in een schema voor 64; de top-8 begon in de tweede ronde. Alle partijen gingen over twee gewonnen sets, ook de finale. In het dubbelspel werd een derde set beslist met een match-tiebreak tot tien punten. Het hele evenement duurde negen dagen: twee dagen kwalificatie en zeven dagen hoofdtoernooi. Wil je weten hoeveel tijd een partij kost? Lees {L['duur']}.</p>"""

content3 = f"""<h3><strong>Dubbelspel: Franse titel voor Halys en Herbert</strong></h3>
<p>Quentin Halys en Pierre-Hugues Herbert, die met een wildcard meededen, wonnen de dubbelfinale van Christian Harrison en Neal Skupski: 7-6(3) 6-7(4) 10-8. Een dag eerder hadden ze in de halve finale het als eerste geplaatste duo Heliövaara/Patten uitgeschakeld. Voor Herbert is het zijn tweede dubbeltitel in Parijs, na 2019 met Nicolas Mahut.</p>
<h3><strong>Prijzengeld Paris Masters 2026</strong></h3>
<p>Het totale prijzengeld was dit jaar €6.309.095, 2,9% meer dan vorig jaar (€6.128.940). Winnaar Alcaraz kreeg €974.370, finalist Shelton €532.120. Ruud en Van Assche verdienden als halvefinalisten elk €290.960.</p>
{tabel(["Ronde", "Prijzengeld", "Rankingpunten"], [(f"<strong>{r}</strong>", p, pt) for r, p, pt in PRIJZEN])}
<p><em>Bedragen in euro, per speler in het enkelspel, volgens de ATP. Het winnende dubbelteam deelt €298.950 en krijgt elk 1000 punten.</em></p>
<h3><strong>Waar was de Paris Masters te zien?</strong></h3>
<p>In Nederland zond {L['ziggo']} het toernooi uit op Ziggo Sport 1 en Ziggo Sport 4; de finale was live op Ziggo Sport 4. In België was het toernooi te zien op Play Sports van Telenet. Hoe je het tennis van komende toernooien kunt volgen, lees je in {L['oud']} en op onze pagina {L['kijken']}.</p>
<h3><strong>Winnaars van de Paris Masters</strong></h3>
<p>Novak Djokovic is met zeven titels de recordwinnaar (2009, 2013, 2014, 2015, 2019, 2021 en 2023). Hij is ook de enige die de titel wist te verdedigen, en dat zelfs drie jaar op rij. Carlos Alcaraz voegde zijn naam in 2026 voor het eerst toe aan de lijst; vorig jaar won Jannik Sinner, in de eerste editie in de nieuwe hal.</p>
{tabel(["Jaar", "Winnaar", "Finalist", "Uitslag"], [(f"<strong>{j}</strong>", w, f, u) for j, w, f, u in WINNAARS])}
<p>Boris Becker is met 18 jaar de jongste winnaar ooit (1986, de eerste editie in Bercy). Hij reikte dit jaar de trofee uit aan Alcaraz. De laatste Franse winnaar is Jo-Wilfried Tsonga, in 2008. Tomáš Berdych won in 2005 als nummer 50 van de wereld: de laagst geplaatste kampioen.</p>
<h3><strong>Nederlanders in Parijs</strong></h3>
<p>In het enkelspel kwam de laatste jaren geen Nederlander voorbij de laatste 16. In 2023 haalden Tallon Griekspoor en Botic van de Zandschulp allebei die ronde; Van de Zandschulp zelfs als kwalificant. In het dubbelspel won Wesley Koolhof de Paris Masters twee keer: in 2022 met Neal Skupski en in 2024 met Nikola Mektić. Tom Okker won al in 1969 en 1975 het toernooi in Parijs dat de voorloper was van de huidige Masters.</p>
<h3><strong>Van Bercy naar La Défense Arena</strong></h3>
<p>Van 1986 tot en met 2024 werd de Paris Masters gespeeld in Bercy, in de Accor Arena. Daarom spreken veel tennisfans nog steeds van "Bercy". Sinds 2025 wordt het toernooi gespeeld in de Paris La Défense Arena in Nanterre, die nu Plenitude Arena heet. Ook dit jaar kwamen er volgens de organisatie meer dan 200.000 toeschouwers. Bekijk ook onze {L['tips']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wie heeft de Paris Masters 2026 gewonnen?</strong><br>Carlos Alcaraz. Hij versloeg in de finale van zondag 8 november Ben Shelton met 7-6(5) 7-5. Het is zijn eerste titel in Parijs.</p>
<p><strong>Wat was de uitslag van de finale van de Paris Masters 2026?</strong><br>Alcaraz – Shelton 7-6(5) 7-5, na 1 uur en 57 minuten.</p>
<p><strong>Wie speelden de halve finales?</strong><br>Alcaraz won met 6-4 6-4 van Casper Ruud, Shelton met 5-7 6-3 6-4 van Luca Van Assche.</p>
<p><strong>Hoeveel prijzengeld kreeg de winnaar van de Paris Masters 2026?</strong><br>€974.370 en 1000 rankingpunten. Het totale prijzengeld was €6.309.095.</p>
<p><strong>Wie won de Paris Masters 2025?</strong><br>Jannik Sinner. Hij versloeg in de finale Félix Auger-Aliassime met 6-4 7-6. Dit jaar speelde hij niet vanwege een knieblessure.</p>
<p><strong>Wie heeft de Paris Masters het vaakst gewonnen?</strong><br>Novak Djokovic, met zeven titels.</p>
<p><strong>Hoe deden de Nederlanders het op de Paris Masters 2026?</strong><br>Botic van de Zandschulp verloor in de eerste ronde van Ugo Humbert. Tallon Griekspoor strandde in de kwalificatie. David Pel haalde in het dubbelspel de tweede ronde.</p>
<p><strong>Wordt de Paris Masters nog in Bercy gespeeld?</strong><br>Nee. Sinds 2025 wordt het toernooi gespeeld in de Paris La Défense Arena in Nanterre, die nu Plenitude Arena heet.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    alles = content + content2 + content3
    tekst = re.sub(r"<[^>]+>", " ", alles)
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", len(tekst.split()), "woorden")
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert content.startswith("<p><strong>") and "Alcaraz" in content[:200] and "7-6(5) 7-5" in content[:400]
    assert "<h2" not in alles and "<h4" not in alles and "betcity" not in alles.lower() and "/go/" not in alles
    assert all(h.startswith("<h3><strong>") for h in re.findall(r"<h3>.{0,12}", alles))
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert "waaroptv" not in alles.lower() and "opstellingvandaag" not in alles.lower() and "footymetrics" not in alles.lower()
    assert "wordt gespeeld van" not in alles and "speelt vanavond" not in alles   # niets meer in de toekomende tijd
    assert WINNAARS[0] == ("2026", "Carlos Alcaraz", "Ben Shelton", "7-6 7-5")
    assert len(WINNAARS) == 21 and [j for j, w, _, _ in WINNAARS if w == "Novak Djokovic"] == ["2023", "2021", "2019", "2015", "2014", "2013", "2009"]
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    print("dry run ok – niets gepubliceerd")
