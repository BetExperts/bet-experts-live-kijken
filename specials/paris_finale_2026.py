# -*- coding: utf-8 -*-
"""Los informatief SEO-artikel: finale Rolex Paris Masters 2026 (zondag 8 november, Paris La Défense Arena / Plenitude
Arena, Nanterre). Geschreven op woensdag 4-11-2026 (dag 3, 2e ronde bezig): finalisten nog onbekend.
UPDATE dinsdag 10-11-2026: finale gespeeld. Carlos Alcaraz – Ben Shelton 7-6(5) 7-5 (1u57). Artikel omgezet naar
'Finale Paris Masters 2026: uitslag' (verloop, statistieken, records, prijzengeld, gevolgen Turijn). SLUG gelijk.
Eigenaar: 'Schrijf een seo informatief artikel voor Finale ATP Masters Parijs, wanneer, hoe laat, waar live kijken, finale
vorig jaar, favorieten etc.'
Zoekintenties nu: finale paris masters 2026 (uitslag), alcaraz shelton finale, wie won paris masters 2026, paris masters
finale score, prijzengeld winnaar paris masters, tennis parijs finale.
Feiten: specials/paris_finale_feiten_2026.md (oud, vooraf) en specials/paris_masters_uitslag_feiten_2026.md (officiële
toernooi-API 7/8-11 + officiële artikelen, ATP, Tennis Majors, Al Jazeera, AP; gecontroleerd 10-11 14:00-14:25).
Onzeker en daarom weggelaten: winners/onafgedwongen fouten (API 47-22 vs TM 33-25), aantal loopbaantitels (29, alleen
officieel artikel) alleen als 'zijn 29e titel volgens de organisatie'. Geen finale-odds afgelezen: niet genoemd.
CMS-velden: alleen de standaardvelden van concept_publiceer.py (eventueel "tennis": True).
Links: TOTO als volledige /go/-URL (stond er al); Bet365-link verwijderd (ging over de livestream van de finale).
Webflow-item-id: niet bekend in deze module (hoofdsessie zoekt op SLUG).
  python3 specials/paris_finale_2026.py   (dry run)
  kaart: ../superodd-agent/.venv/bin/python og_kaarten/gsod.py paris_finale_2026 (OG_LOGO)"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "finale-paris-masters-2026-wanneer-hoe-laat-tv"
RUBRIEK = "665715dbf1f3cbdf7f874d79"   # Tennis
TITEL = "Finale Paris Masters 2026: uitslag Alcaraz – Shelton"
SAMENVATTING = ("Alcaraz wint de finale van de Paris Masters 2026 met 7-6 7-5 van Shelton. Het verloop, de cijfers, het "
                "prijzengeld en wat de titel betekent.")
TOTO = "https://www.bet-experts.nl/go/toto-live-kijken"

OG_LOGO = "paris-masters-logo.png"
OG_EYEBROW = "Tennis · ATP Masters 1000"
OG_KOP = "Finale Paris<br><em>Masters 2026</em>"
OG_TEGELS = [("Winnaar", "Alcaraz"), ("Uitslag", "7-6 7-5")]
OG_KOPJE = "De finale in cijfers"
OG_RECHTS = "Zondag 8 november"
OG_RIJEN = [("Tegenstander", "Ben Shelton (VS)", "4-1 H2H"),
            ("Duur", "Twee sets", "1u57"),
            ("Breakpunten", "Alcaraz redde er", "6 van 7"),
            ("Prijzengeld", "Plus 1000 punten", "€974.370")]

L = {"hub": '<a href="/nieuws/paris-masters-2026-schema-tijden-tv-deelnemers-prijzengeld">Paris Masters 2026: winnaar en alle uitslagen</a>',
     "wiewint": '<a href="/nieuws/wie-wint-paris-masters-2026-favorieten-odds-voorspelling">hoe de favorieten het deden</a>',
     "tips": '<a href="/tennis-voorspellingen-vandaag">tennisvoorspellingen van vandaag</a>',
     "toto": '<a href="/bookmakers/toto">TOTO</a>',
     "duur": '<a href="/nieuws/hoe-lang-duurt-een-tenniswedstrijd">hoe lang een tenniswedstrijd duurt</a>',
     "turijn": '<a href="/nieuws/atp-finals-2026-gekwalificeerd-race-to-turin">wie er meedoen aan de ATP Finals</a>'}

WINNAARS = [  # (jaar, winnaar, finalist, uitslag) – zelfde bron als paris_masters_2026.py
    ("2026", "Carlos Alcaraz", "Ben Shelton", "7-6 7-5"),
    ("2025", "Jannik Sinner", "Félix Auger-Aliassime", "6-4 7-6"), ("2024", "Alexander Zverev", "Ugo Humbert", "6-2 6-2"),
    ("2023", "Novak Djokovic", "Grigor Dimitrov", "6-4 6-3"), ("2022", "Holger Rune", "Novak Djokovic", "3-6 6-3 7-5"),
    ("2021", "Novak Djokovic", "Daniil Medvedev", "4-6 6-3 6-3"), ("2020", "Daniil Medvedev", "Alexander Zverev", "5-7 6-4 6-1"),
    ("2019", "Novak Djokovic", "Denis Shapovalov", "6-3 6-4"), ("2018", "Karen Khachanov", "Novak Djokovic", "7-5 6-4"),
    ("2017", "Jack Sock", "Filip Krajinović", "5-7 6-4 6-1"),
]

STATS = [  # (onderdeel, Alcaraz, Shelton) – officiële toernooi-API
    ("Aces", "6", "13"),
    ("Dubbele fouten", "2", "1"),
    ("Punten gewonnen op eerste service", "40 van 56 (71%)", "33 van 52 (63%)"),
    ("Punten gewonnen op tweede service", "13 van 22 (59%)", "15 van 28 (54%)"),
    ("Breakpunten benut", "2 van 5", "1 van 7"),
    ("Breakpunten gered", "6 van 7", "3 van 5"),
    ("Totaal gewonnen punten", "85", "73"),
]

ROUTE = [  # (ronde, Alcaraz, Shelton)
    ("1e ronde", "Bye", "Bye"),
    ("2e ronde", "Alex Michelsen 7-6(4) 6-3", "Cameron Norrie 6-3 6-4"),
    ("Laatste 16", "Matteo Berrettini (walkover)", "Arthur Rinderknech 3-6 6-4 7-6(5)"),
    ("Kwartfinale", "Taylor Fritz 6-7(10) 7-5 6-3", "Tommy Paul 6-4 4-6 6-3"),
    ("Halve finale", "Casper Ruud 6-4 6-4", "Luca Van Assche 5-7 6-3 6-4"),
]

content = f"""<p><strong>Carlos Alcaraz heeft de finale van de Rolex Paris Masters 2026 gewonnen. De Spanjaard versloeg op zondag 8 november de Amerikaan Ben Shelton met 7-6(5) 7-5. De finale in de Paris La Défense Arena (Plenitude Arena) in Nanterre begon om 15:00 uur en duurde 1 uur en 57 minuten. Het is de eerste titel van Alcaraz in Parijs en zijn negende Masters 1000-titel. Hij verdiende €974.370 en 1000 rankingpunten; Shelton kreeg €532.120 en 650 punten.</strong></p>
<p>Voor Alcaraz was het ook een revanche. Shelton had hem in september in vijf sets uitgeschakeld in de kwartfinale van de US Open. Hieronder lees je hoe de finale verliep, de belangrijkste cijfers en wat de titel betekent. Alle uitslagen van het toernooi staan in {L['hub']}.</p>
<h3><strong>Finale Paris Masters 2026 in het kort</strong></h3>
{tabel(None, [
    ("<strong>Uitslag</strong>", "Carlos Alcaraz (2) – Ben Shelton (3): 7-6(5) 7-5"),
    ("<strong>Datum en aanvang</strong>", "Zondag 8 november 2026, 15:00 uur"),
    ("<strong>Duur</strong>", "1 uur en 57 minuten (eerste set 65 minuten)"),
    ("<strong>Locatie</strong>", "Paris La Défense Arena (Plenitude Arena), Nanterre"),
    ("<strong>Ondergrond</strong>", "Hardcourt, indoor"),
    ("<strong>Winnaar</strong>", "€974.370 en 1000 rankingpunten"),
    ("<strong>Finalist</strong>", "€532.120 en 650 rankingpunten"),
    ("<strong>Onderlinge stand</strong>", "4-1 voor Alcaraz"),
    ("<strong>Dubbelfinale</strong>", "Halys/Herbert – Harrison/Skupski 7-6(3) 6-7(4) 10-8"),
])}
<h3><strong>Zo verliep de finale</strong></h3>
<p><strong>Eerste set: Alcaraz overleeft.</strong> Shelton begon het sterkst en zette Alcaraz met zijn opslag direct onder druk. Bij 1-2 stond Alcaraz 0-40 achter op zijn eigen service; hij redde vier breakpunten in die game. Bij 3-4 kreeg Shelton er nog twee, maar ook die gingen verloren. In de tiebreak wisselden de mini-breaks elkaar af. Vanaf 5-4 hield Alcaraz zijn voorsprong vast; op zijn tweede setpunt won hij de tiebreak met 7-5, na 65 minuten. Shelton maakte in die set volgens de organisatie 17 onafgedwongen fouten.</p>
<p><strong>Tweede set: de terugslag en de comeback.</strong> Juist toen alles goed ging, zakte Alcaraz even weg. Bij 2-2 verloor hij zijn opslag, onder meer door een dubbele fout. Shelton liep uit naar 4-2, maar Alcaraz bleef geduldig. Met een passing op zijn forehand dwong hij twee breakkansen af en brak terug naar 4-4. Tussen 2-4 en 5-4 won hij twaalf van de vijftien punten. Bij 5-6 moest Shelton serveren om een tweede tiebreak af te dwingen. Alcaraz kreeg twee matchpunten en maakte het op het tweede af met een winner.</p>
<h3><strong>Statistieken van de finale</strong></h3>
{tabel(["Onderdeel", "Alcaraz", "Shelton"], [(f"<strong>{o}</strong>", a, b) for o, a, b in STATS])}
<p><em>Cijfers volgens de officiële toernooisite. Shelton sloeg meer aces, maar Alcaraz won de beslissende punten: hij redde zes van de zeven breakpunten en won 54% van alle punten.</em></p>
<p>Shelton wist na afloop precies waar het misging. Hij had in de eerste set 0-40 en 15-40 op de opslag van Alcaraz en had die kansen willen benutten om zelf voor de set te kunnen serveren. Alcaraz noemde de week na afloop zo goed als hij zich had kunnen dromen. Hij had in de kwartfinale tegen Taylor Fritz twee matchpunten weggewerkt en zei dat hij daarna vooral zichzelf was gebleven op de baan.</p>"""

content2 = f"""<h3><strong>Wat de titel betekent voor Alcaraz</strong></h3>
<ul><li>Het is zijn eerste titel op de Paris Masters. Eerder kwam hij in Parijs nooit verder dan de kwartfinale.</li><li>Het is zijn negende Masters 1000-titel. Hij won nu zeven van de negen Masters 1000-toernooien; alleen Canada en Shanghai ontbreken nog.</li><li>Hij is pas de derde speler met Masters 1000-titels in vijf opeenvolgende jaren, na Novak Djokovic en Rafael Nadal.</li><li>Het is zijn vijfde titel van 2026, na de Australian Open, Doha, Tokio en Wenen. Alleen Jannik Sinner won er dit jaar meer (zes).</li><li>Alcaraz is de tweede Spaanse winnaar van het toernooi, na David Ferrer in 2012.</li><li>Na Wenen en Parijs heeft hij negen partijen op rij gewonnen. Volgens de organisatie is het de 29e titel van zijn loopbaan.</li></ul>
<p>Alcaraz miste dit jaar ruim vier maanden door een polsblessure, onder meer Roland Garros en Wimbledon. Bij de prijsuitreiking, waar Boris Becker de trofee overhandigde, bedankte hij het Parijse publiek en zei hij te hopen nooit meer een toernooi in Parijs te hoeven missen. Op de wereldranglijst blijft hij derde, achter Alexander Zverev en Sinner.</p>
<h3><strong>Shelton: eerste verloren Masters-finale</strong></h3>
<p>Voor Ben Shelton was het zijn zesde finale van het seizoen en zijn eerste in Parijs. Zijn twee eerdere Masters 1000-finales, in Canada in 2025 en 2026, won hij allebei. Hij blijft vierde op de wereldranglijst en gaat, net als Alcaraz, naar de ATP Finals in Turijn. In de halve finale had hij drie sets nodig tegen de Fransman Luca Van Assche, die het publiek achter zich had.</p>
<h3><strong>De weg naar de finale</strong></h3>
{tabel(["Ronde", "Alcaraz won van", "Shelton won van"], [(f"<strong>{r}</strong>", a, s) for r, a, s in ROUTE])}
<p>Alcaraz verloor in het hele toernooi maar één set, tegen Fritz. Berrettini trok zich voor hun partij in de laatste 16 terug met een elleboogblessure. In de halve finale gaf Alcaraz Ruud geen enkel breakpunt. Shelton moest vaker diep gaan: tegen Rinderknech, Paul en Van Assche had hij drie sets nodig. Hoe dit spoort met de verwachtingen vooraf, lees je in {L['wiewint']}.</p>
<h3><strong>Dubbelfinale: Franse winnaars</strong></h3>
<p>Voor de enkelfinale won het Franse duo Quentin Halys en Pierre-Hugues Herbert, met een wildcard in het toernooi, de dubbelfinale van Christian Harrison en Neal Skupski: 7-6(3) 6-7(4) 10-8. Herbert won de titel in Parijs eerder in 2019 met Nicolas Mahut.</p>"""

content3 = f"""<h3><strong>Prijzengeld en punten voor de finalisten</strong></h3>
<p>Het totale prijzengeld van de Paris Masters 2026 was €6.309.095. Winnaar Alcaraz kreeg €974.370, bijna €28.000 meer dan Sinner vorig jaar (€946.610).</p>
{tabel(["Ronde", "Speler(s)", "Prijzengeld", "Rankingpunten"], [
    ("<strong>Winnaar</strong>", "Carlos Alcaraz", "€974.370", "1000"),
    ("<strong>Finalist</strong>", "Ben Shelton", "€532.120", "650"),
    ("<strong>Halve finale</strong>", "Casper Ruud, Luca Van Assche", "€290.960", "400"),
    ("<strong>Kwartfinale</strong>", "Taylor Fritz, Tommy Paul, Nuno Borges, Rinky Hijikata", "€158.700", "200"),
])}
<p><em>Bedragen per speler in het enkelspel, volgens de ATP. Het winnende dubbelteam deelt €298.950 en krijgt elk 1000 punten.</em></p>
<h3><strong>Wat nu: de ATP Finals in Turijn</strong></h3>
<p>Beide finalisten spelen van 15 tot en met 22 november de ATP Finals in Turijn. Het veld van acht is compleet: Alexander Zverev, Carlos Alcaraz, Ben Shelton, Daniil Medvedev, Flavio Cobolli, Arthur Fils, Frances Tiafoe en Rafael Jódar. Alcaraz heeft het eindtoernooi nog nooit gewonnen. Fritz en Alex de Minaur zijn reserve. Lees meer over {L['turijn']}.</p>
<h3><strong>Winnaars van de Paris Masters: de laatste tien finales</strong></h3>
{tabel(["Jaar", "Winnaar", "Finalist", "Uitslag"], [(f"<strong>{j}</strong>", w, f, u) for j, w, f, u in WINNAARS])}
<p>Novak Djokovic is met zeven titels de recordwinnaar van het toernooi (2009, 2013, 2014, 2015, 2019, 2021 en 2023). De complete lijst met winnaars staat in {L['hub']}.</p>
<h3><strong>Speelden er Nederlanders of Belgen in de finale?</strong></h3>
<p>Nee. Botic van de Zandschulp verloor in de eerste ronde van Ugo Humbert en Tallon Griekspoor strandde in de kwalificatie. Van de Belgen verloor Zizou Bergs in de eerste ronde; Alexander Blockx kwam niet in actie. Wesley Koolhof won de dubbeltitel in Parijs wel twee keer: in 2022 met Neal Skupski en in 2024 met Nikola Mektić.</p>
<p><strong>Tennis live volgen?</strong> Bij {L['toto']} kun je met een gratis account, zonder storting, naar de tennislivestreams kijken. Welke partijen in de stream zitten, zie je per partij in het live-gedeelte (18+). Wil je weten hoe lang een partij gemiddeld duurt? Lees {L['duur']}. Voorspellingen per dag vind je bij onze {L['tips']}.</p>
<p><a href="{TOTO}"><strong>👉 Klik hier: maak je gratis TOTO-account aan en kijk tennis live</strong></a></p>
<h3><strong>Veelgestelde vragen over de finale</strong></h3>
<p><strong>Wie heeft de finale van de Paris Masters 2026 gewonnen?</strong><br>Carlos Alcaraz. Hij versloeg Ben Shelton op zondag 8 november met 7-6(5) 7-5.</p>
<p><strong>Wat was de uitslag van de finale van de Paris Masters 2026?</strong><br>7-6(5) 7-5 voor Alcaraz. De eerste set werd beslist in een tiebreak, in de tweede set brak Alcaraz bij 5-6 de opslag van Shelton.</p>
<p><strong>Hoe lang duurde de finale?</strong><br>1 uur en 57 minuten. De eerste set alleen al duurde 65 minuten.</p>
<p><strong>Hoeveel prijzengeld kreeg de winnaar van de Paris Masters 2026?</strong><br>€974.370 en 1000 rankingpunten. Finalist Shelton kreeg €532.120 en 650 punten.</p>
<p><strong>Wie won de Paris Masters in 2025?</strong><br>Jannik Sinner. Hij versloeg Félix Auger-Aliassime in de finale met 6-4 7-6. Dit jaar speelde hij niet vanwege een knieblessure.</p>
<p><strong>Hoeveel Masters 1000-titels heeft Carlos Alcaraz?</strong><br>Negen. Parijs was zijn eerste Masters 1000-titel van 2026.</p>
<p><strong>Spelen Alcaraz en Shelton de ATP Finals?</strong><br>Ja. Beide finalisten zijn geplaatst voor de ATP Finals in Turijn, van 15 tot en met 22 november.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    alles = content + content2 + content3
    tekst = re.sub(r"<[^>]+>", " ", alles)
    w = len(tekst.split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", w, "woorden")
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert 1100 <= w <= 1900, w
    assert content.startswith("<p><strong>") and "zondag 8 november" in content[:300] and "7-6(5) 7-5" in content[:300]
    assert "<h2" not in alles and "<h4" not in alles and "betcity" not in alles.lower() and "espn" not in alles.lower()
    assert "telegram" not in alles.lower() and "tennis tv" not in alles.lower() and "Accor" not in alles
    assert "footymetrics" not in alles.lower() and "niet vóór 15:00" not in alles   # finale is gespeeld
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles) and not re.search(r"<(ul|ol)>\s+<", alles)
    assert all(h.startswith("<h3><strong>") for h in re.findall(r"<h3>.{0,12}", alles))
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert "waaroptv" not in alles.lower() and "opstellingvandaag" not in alles.lower()
    assert alles.count(TOTO) == 1 and "/go/bet365" not in alles
    assert len(re.findall(r"<p><strong>[^<]+\?</strong><br>", content3)) == 7   # FAQ: 7 vragen
    assert WINNAARS[0] == ("2026", "Carlos Alcaraz", "Ben Shelton", "7-6 7-5") and len(WINNAARS) == 10
    for k in ("/nieuws/paris-masters-2026-schema-tijden-tv-deelnemers-prijzengeld", "/bookmakers/toto",
              "/nieuws/wie-wint-paris-masters-2026-favorieten-odds-voorspelling"):
        assert k in alles, k
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/") or href == TOTO, href
    print("dry run ok – niets gepubliceerd")
