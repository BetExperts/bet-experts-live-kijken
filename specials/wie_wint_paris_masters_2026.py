# -*- coding: utf-8 -*-
"""Los SEO-artikel 'Wie wint de Paris Masters 2026?' (favorieten, odds, voorspelling). Geschreven woensdagavond 4-11-2026
na de tweede ronde, bijgewerkt donderdag 5-11 (R16-odds 711). Eigenaar (4-11): 'wie wint atp masters in parijs is wellicht
ook een goede' (format 'wie wint' bij grote toernooien, zie memory bet-experts-ai-impressies-kliks).
UPDATE dinsdag 10-11-2026: toernooi voorbij. Omgezet naar terugblik 'winnaar': Alcaraz won (7-6(5) 7-5 van Shelton);
onze voorspelling van 5-11 (Alcaraz winnaar, Shelton finalist) kwam uit; per favoriet hoe ver hij kwam; eerlijk over de
odds: er was GEEN winnaarsmarkt bij onze bookmakers, alleen wedstrijdodds (711 R16 5-11 ±09:45, HF 7-11 ±10:20).
SLUG gelijk. Geen finale-odds afgelezen: niet genoemd.
Feiten: specials/paris_masters_winnaar_feiten_2026.md (vooraf) en specials/paris_masters_uitslag_feiten_2026.md
(officiële toernooi-API 2..8-11, officiële artikelen, ATP, Tennis Majors, Al Jazeera, AP; gecontroleerd 10-11).
Webflow-item-id: niet bekend in deze module (hoofdsessie zoekt op SLUG).
  python3 specials/wie_wint_paris_masters_2026.py   (dry run)
  kaart: ../superodd-agent/.venv/bin/python og_kaarten/gsod.py wie_wint_paris_masters_2026"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

# R16-odds donderdag 5-11 (711, Kambi sevelevnl, ±09:45) met de uitslag: (partij, odds vooraf, winnaar + score)
R16 = [
    ("Lorenzo Musetti – Luca Van Assche", "Musetti 1,38 / Van Assche 3,00", "Van Assche 7-5 3-6 6-4"),
    ("Rinky Hijikata – Tomás Martín Etcheverry", "Hijikata 2,06 / Etcheverry 1,76", "Hijikata 2-6 6-3 7-5"),
    ("Ben Shelton – Arthur Rinderknech", "Shelton 1,30 / Rinderknech 3,50", "Shelton 3-6 6-4 7-6(5)"),
    ("Tommy Paul – Quentin Halys", "Paul 1,32 / Halys 3,40", "Paul 7-6(3) 6-4"),
    ("Casper Ruud – Jan-Lennard Struff", "Ruud 1,53 / Struff 2,50", "Ruud 6-3 6-3"),
    ("Ignacio Buse – Nuno Borges", "Buse 2,28 / Borges 1,63", "Borges 6-0 6-2"),
    ("Arthur Fils – Taylor Fritz", "Fils 1,72 / Fritz 2,12", "Fritz 6-3 6-4"),
    ("Matteo Berrettini – Carlos Alcaraz", "Berrettini 5,50 / Alcaraz 1,15", "Alcaraz (walkover)"),
]

SLUG = "wie-wint-paris-masters-2026-favorieten-odds-voorspelling"
RUBRIEK = "665715dbf1f3cbdf7f874d79"   # Tennis
TITEL = "Winnaar Paris Masters 2026: Alcaraz, zo deden de favorieten"
SAMENVATTING = ("Carlos Alcaraz won de Paris Masters 2026, zoals wij voorspelden. Hoe de favorieten het deden, wat de odds "
                "zeiden en de finale tegen Shelton.")

OG_LOGO = "paris-masters-logo.png"
OG_EYEBROW = "Tennis · ATP 1000 Parijs"
OG_KOP = "Winnaar Paris<br><em>Masters 2026</em>"
OG_TEGELS = [("Winnaar", "Alcaraz"), ("Finale", "7-6 7-5")]
OG_KOPJE = "Onze favorieten (5 nov)"
OG_RECHTS = "zo ver kwamen ze"
OG_RIJEN = [("Alcaraz", "Onze favoriet", "Winnaar"),
            ("Shelton", "Onze finalist", "Finale"),
            ("Fritz", "Had twee matchpunten", "Kwartfin."),
            ("Musetti", "Versloeg Zverev", "Laatste 16")]

L = {"hub": '<a href="/nieuws/paris-masters-2026-schema-tijden-tv-deelnemers-prijzengeld">Paris Masters 2026: winnaar en alle uitslagen</a>',
     "finale": '<a href="/nieuws/finale-paris-masters-2026-wanneer-hoe-laat-tv">het verslag van de finale van de Paris Masters 2026</a>',
     "hf": '<a href="/nieuws/paris-masters-2026-voorspellingen-wedtips-halve-finales-7-november">onze voorspellingen voor de halve finales</a>',
     "djok": '<a href="/nieuws/djokovic-mist-atp-finals-2026-turijn">Djokovic mist de ATP Finals 2026</a>',
     "turijn": '<a href="/nieuws/atp-finals-2026-gekwalificeerd-race-to-turin">wie er meedoen aan de ATP Finals 2026</a>',
     "tips": '<a href="/tennis-voorspellingen-vandaag">tennisvoorspellingen van vandaag</a>'}

content = f"""<p><strong>Carlos Alcaraz heeft de Paris Masters 2026 gewonnen. Hij versloeg op zondag 8 november in de finale Ben Shelton met 7-6(5) 7-5. Daarmee kwam onze voorspelling uit: na de tweede ronde zagen wij Alcaraz als de grote favoriet en Shelton als finalist uit de bovenste helft. Het is de eerste titel van Alcaraz in Parijs en zijn negende Masters 1000-titel.</strong></p>
<p>Op donderdag 5 november, voor de laatste zestien, schreven we in dit artikel wie volgens ons de titel zou pakken. Hieronder lees je hoe dat uitpakte: wat er klopte, wat niet, en wat de odds vooraf zeiden. Alle uitslagen van het toernooi staan in {L['hub']}.</p>
<h3><strong>De Paris Masters 2026 in het kort</strong></h3>
{tabel(None, [
    ("<strong>Winnaar</strong>", "Carlos Alcaraz (Spanje, 2e geplaatst)"),
    ("<strong>Finale</strong>", "Alcaraz – Ben Shelton 7-6(5) 7-5, zondag 8 november"),
    ("<strong>Halve finales</strong>", "Alcaraz – Casper Ruud 6-4 6-4; Shelton – Luca Van Assche 5-7 6-3 6-4"),
    ("<strong>Onze voorspelling (5 nov)</strong>", "Alcaraz winnaar, Shelton finalist: beide uitgekomen"),
    ("<strong>Titelverdediger</strong>", "Jannik Sinner, speelde niet (knieblessure)"),
    ("<strong>Prijzengeld winnaar</strong>", "€974.370 en 1000 ATP-punten"),
    ("<strong>Nederlanders</strong>", "Geen Nederlander voorbij de eerste ronde in het enkelspel"),
])}
<h3><strong>Wie won de Paris Masters 2026?</strong></h3>
<p>Alcaraz won de finale na 1 uur en 57 minuten. Shelton kreeg in de eerste set zes breakpunten, maar Alcaraz redde ze allemaal en won de tiebreak met 7-5. In de tweede set kwam hij een break achter, brak terug naar 4-4 en maakte het bij 5-6 af op de opslag van Shelton. Het was ook een revanche: Shelton had hem in september uitgeschakeld in de kwartfinale van de US Open. Alle cijfers lees je in {L['finale']}.</p>
<p>Alcaraz verloor in het hele toernooi maar één set. Het spannendste moment kwam in de kwartfinale: tegen Taylor Fritz stond hij een set achter en moest hij twee matchpunten wegwerken (6-7(10) 7-5 6-3). In de laatste zestien kreeg hij een walkover van Matteo Berrettini, die een elleboogblessure had.</p>"""

content2 = f"""<h3><strong>Zo deden onze favorieten het</strong></h3>
{tabel(["Favoriet (5 nov)", "Onze verwachting", "Resultaat"], [
    ("<strong>1. Carlos Alcaraz</strong>", "Winnaar", "Winnaar: 7-6(5) 7-5 in de finale tegen Shelton"),
    ("<strong>2. Ben Shelton</strong>", "Finalist uit de bovenste helft", "Finale; won van Rinderknech, Paul en Van Assche"),
    ("<strong>3. Lorenzo Musetti</strong>", "Grootste verrassing in de bovenste helft", "Laatste 16: verloor van Van Assche, 7-5 3-6 6-4"),
    ("<strong>4. Taylor Fritz</strong>", "Gevaarlijke serveerder", "Kwartfinale: verloor met twee matchpunten van Alcaraz"),
    ("<strong>Arthur Fils</strong>", "Geen topfavoriet, twijfel over zijn been", "Laatste 16: verloor van Fritz, 6-3 6-4"),
])}
<p><strong>Wat klopte.</strong> Alcaraz was de beste speler die nog in het toernooi zat, en dat bleek. Hij speelde vier partijen en gaf daarin maar één set weg, tegen Fritz. Shelton kwam, zoals verwacht, uit de bovenste helft. Zijn opslag was op de snelle baan het wapen dat we vooraf noemden: in de halve finale tegen Van Assche sloeg hij 19 aces.</p>
<p><strong>Wat niet klopte.</strong> Musetti, onze verrassing in de bovenste helft, verloor al in de laatste zestien van de Fransman Luca Van Assche. Die haalde daarna als ongeplaatste speler de halve finale. Ook Casper Ruud, door ons alleen als outsider genoemd, kwam verder dan verwacht: hij haalde de halve finale en steeg naar de achttiende plaats op de wereldranglijst. En Fritz kwam dichter bij een stunt dan wij hadden ingeschat.</p>
<h3><strong>De favorieten van voor het toernooi</strong></h3>
<p>Voor de start stonden Alcaraz, Alexander Zverev en Daniil Medvedev bovenaan in de verwachtingen van analisten. Alleen Alcaraz maakte dat waar. Zverev, de nummer één van de plaatsing, verloor in de tweede ronde van Musetti (7-6(5) 6-2). Medvedev ging in dezelfde ronde onderuit tegen Ignacio Buse (6-4 6-4). Recordwinnaar Novak Djokovic verloor van kwalificant Rinky Hijikata (2-6 6-3 6-3), waardoor hij ook de ATP Finals misliep; lees daarover {L['djok']}. Titelverdediger Jannik Sinner speelde niet.</p>
<h3><strong>Wat zeiden de odds vooraf?</strong></h3>
<p>Eerlijk is eerlijk: een winnaarsmarkt voor de Paris Masters was er tijdens het toernooi niet bij de Nederlandse bookmakers die we bekeken. Onze voorspelling was dus een eigen inschatting. Wel waren er odds per partij. Dit zijn de odds van 711 van donderdagochtend 5 november voor de laatste zestien, met de uitslag erbij.</p>
{tabel(["Partij", "Odds vooraf (711)", "Winnaar"], [(f"<strong>{p}</strong>", o, w) for p, o, w in R16])}
<p><em>Odds van donderdag 5 november rond 09:45 uur. De partij Berrettini – Alcaraz werd niet gespeeld.</em></p>
<p>Van de zeven gespeelde partijen won de favoriet er vier: Shelton, Paul, Ruud en Borges. Drie keer won de underdog. Van Assche (3,00) tegen Musetti was de grootste verrassing, Fritz (2,12) won ruim van Fils, en Hijikata (2,06) won van Etcheverry. Alcaraz was met 1,15 de grootste favoriet van de dag, maar hoefde niet te spelen. In de halve finales voorspelden we dat Shelton met minstens drie games verschil zou winnen (1,49) en Alcaraz met minstens vier (1,52). Beide kwamen uit: Shelton won met drie games verschil, Alcaraz met vier. Zie {L['hf']}.</p>"""

content3 = f"""<h3><strong>Wat leverde de titel op?</strong></h3>
{tabel(["Ronde", "Speler(s)", "Prijzengeld", "ATP-punten"], [
    ("<strong>Winnaar</strong>", "Carlos Alcaraz", "€974.370", "1000"),
    ("<strong>Finalist</strong>", "Ben Shelton", "€532.120", "650"),
    ("<strong>Halve finale</strong>", "Casper Ruud, Luca Van Assche", "€290.960", "400"),
    ("<strong>Kwartfinale</strong>", "Taylor Fritz, Tommy Paul, Nuno Borges, Rinky Hijikata", "€158.700", "200"),
])}
<p>Parijs was het laatste toernooi dat meetelde voor de ATP Finals in Turijn (15 tot en met 22 november). Het veld is compleet: Zverev, Alcaraz, Shelton, Medvedev, Cobolli, Fils, Frances Tiafoe en Rafael Jódar. Fritz en Paul vielen in Parijs net af; Fritz en Alex de Minaur gaan als reserve mee. Lees ook {L['turijn']}.</p>
<h3><strong>Winnaars van de Paris Masters</strong></h3>
{tabel(["Jaar", "Winnaar", "Finale"], [
    ("<strong>2026</strong>", "Carlos Alcaraz", "7-6 7-5 tegen Ben Shelton"),
    ("<strong>2025</strong>", "Jannik Sinner", "6-4 7-6 tegen Félix Auger-Aliassime"),
    ("<strong>2024</strong>", "Alexander Zverev", "6-2 6-2 tegen Ugo Humbert"),
    ("<strong>2023</strong>", "Novak Djokovic", "6-4 6-3 tegen Grigor Dimitrov"),
    ("<strong>2022</strong>", "Holger Rune", "3-6 6-3 7-5 tegen Novak Djokovic"),
    ("<strong>2021</strong>", "Novak Djokovic", "4-6 6-3 6-3 tegen Daniil Medvedev"),
])}
<p>Djokovic is met zeven titels recordwinnaar. Alcaraz is de tweede Spaanse winnaar, na David Ferrer in 2012. De laatste Franse winnaar blijft Jo-Wilfried Tsonga (2008). Voor de kansen per partij bij volgende toernooien kun je terecht bij onze {L['tips']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wie heeft de Paris Masters 2026 gewonnen?</strong><br>Carlos Alcaraz. Hij versloeg Ben Shelton in de finale van zondag 8 november met 7-6(5) 7-5.</p>
<p><strong>Was Alcaraz de favoriet voor de Paris Masters 2026?</strong><br>Ja. Na de uitschakeling van Zverev en Medvedev was hij de hoogst geplaatste speler die nog meedeed. Een winnaarsmarkt was er bij de Nederlandse bookmakers niet, maar in zijn partijen was hij steeds favoriet.</p>
<p><strong>Wie won de Paris Masters in 2025?</strong><br>Jannik Sinner. Hij versloeg in de finale Félix Auger-Aliassime met 6-4 7-6. Dit jaar speelde hij niet.</p>
<p><strong>Hoeveel verdiende de winnaar van de Paris Masters 2026?</strong><br>€974.370 en 1000 punten voor de wereldranglijst.</p>
<p><strong>Deed er een Nederlander mee?</strong><br>Botic van de Zandschulp verloor in de eerste ronde van Ugo Humbert. Tallon Griekspoor strandde in de kwalificatie.</p>
<p><strong>Waarom won Djokovic niet?</strong><br>Hij verloor in de tweede ronde van qualifier Rinky Hijikata: 2-6 6-3 6-3.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    alles = content + content2 + content3
    w = len(re.sub(r"<[^>]+>", " ", alles).split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", w, "woorden")
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert content.startswith("<p><strong>") and "Alcaraz" in content[:120] and "<h2" not in alles and "<h4" not in alles
    assert "betcity" not in alles.lower() and "telegram" not in alles.lower() and "/go/" not in alles
    assert "waaroptv" not in alles.lower() and "opstellingvandaag" not in alles.lower() and "footymetrics" not in alles.lower()
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    assert all(h.startswith("<h3><strong>") for h in re.findall(r"<h3>.{0,12}", alles))
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert len(R16) == 8 and sum(1 for _, _, w in R16 if "walkover" in w) == 1
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    print("dry run ok – niets gepubliceerd")
