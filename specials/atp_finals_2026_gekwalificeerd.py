# -*- coding: utf-8 -*-
"""Los artikel: wie zijn er gekwalificeerd voor de Nitto ATP Finals 2026 (Race to Turin). Alleen kwalificatie;
schema/groepen/odds/tv schrijft Jasper begin november zelf.
Feiten nagelopen op 22-10-2026: PIF ATP Live Race To Turin (live-stand 22-10, tijdens Almaty/Lyon/Brussel),
ATP-kwalificatieberichten per speler (Sinner 10-7, Zverev 6-8, Alcaraz 16-9, Shelton 18-10), ATP Live Race-update
18-10, ATP-kalender 2026, ATP Rulebook 2026 hfdst. IV (art. 4.01 B: top 7 na Rolex Paris Masters, grandslamwinnaars
8-20, terugtrekking/alternates), afmelding Sinner 6-10, Doubles Teams Race (live 22-10).
Alleen dry run; publiceren gaat via artikelen/werk_bij.py of een aparte stap.
  python3 specials/atp_finals_2026_gekwalificeerd.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from legaal_data import tabel

TITEL = "ATP Finals 2026: wie zijn er al gekwalificeerd? (Race to Turin)"
SLUG = "atp-finals-2026-gekwalificeerd-race-to-turin"
SAMENVATTING = ("Wie zijn er gekwalificeerd voor de ATP Finals 2026? Zverev, Alcaraz en Shelton zijn zeker. "
                "De stand in de Race to Turin en wie nog kans maakt.")
RUBRIEK_TENNIS = "665715dbf1f3cbdf7f874d79"
PEILDATUM = "22 oktober 2026"

# Deelkaart: Race to Turin zonder de afgemelde Sinner (2e, 7.950 punten). (naam, land, status, punten)
SINNER_POS = 2  # positie van Sinner in de Race; spelers erna schuiven in de kaart één plek op
SPELERS = [
    ("Alexander Zverev", "GER", "Zeker", 9150),
    ("Carlos Alcaraz", "ESP", "Zeker", 4600),
    ("Ben Shelton", "USA", "Zeker", 4480),
    ("Flavio Cobolli", "ITA", "Race", 3540),
    ("Daniil Medvedev", "RUS", "Race", 3420),
    ("Frances Tiafoe", "USA", "Race", 3380),
    ("Arthur Fils", "FRA", "Race", 3375),
    ("Rafael Jódar", "ESP", "Race", 3159),
    ("Alex de Minaur", "AUS", "Race", 2880),
    ("Novak Djokovic", "SRB", "Race", 2840),
]


def race_pos(i):
    """Officiële Race-positie van SPELERS[i] (Sinner staat op SINNER_POS)."""
    return i + 1 if i + 1 < SINNER_POS else i + 2


def pt(n):
    return f"{n:,}".replace(",", ".")


content = f"""<p><strong>Voor de ATP Finals 2026 zijn op 22 oktober drie tennissers zeker van hun plek: Alexander Zverev, Carlos Alcaraz en Ben Shelton. Jannik Sinner was ook al zeker, maar stopt dit seizoen met een knieblessure. Er zijn dus nog vijf plekken vrij. Flavio Cobolli, Daniil Medvedev, Frances Tiafoe, Arthur Fils en Rafael Jódar staan nu op een plaats voor Turijn.</strong></p>
<p>De ATP Finals worden van 15 tot en met 22 november 2026 gespeeld in de Inalpi Arena in Turijn. Alleen de acht beste spelers van het seizoen mogen meedoen. Wie dat zijn, bepaalt de Race to Turin: de ranglijst met alle punten die een speler in 2026 heeft verdiend.</p>
<h3><strong>ATP Finals 2026: deze spelers zijn al gekwalificeerd</strong></h3>
<p>De ATP maakt per speler bekend wanneer hij zeker is van Turijn:</p>
{tabel(["Speler", "Land", "Zeker sinds", "Hoe"], [
    ("Jannik Sinner", "Italië", "10 juli", "Haalde de finale van Wimbledon (en won die). <em>Afgemeld met blessure.</em>"),
    ("Alexander Zverev", "Duitsland", "6 augustus", "Door zijn resultaten op het Masters-toernooi in Canada"),
    ("Carlos Alcaraz", "Spanje", "16 september", "Kon niet meer uit de top 20 van de Race vallen"),
    ("Ben Shelton", "Verenigde Staten", "18 oktober", "Bevestigd na het Masters-toernooi in Shanghai"),
])}
<p><strong>Alexander Zverev</strong> is de grote man van 2026. Hij won Roland Garros en de US Open en staat met ruime voorsprong bovenaan de Race. Het is de negende keer dat hij zich plaatst voor het eindejaarstoernooi. <strong>Carlos Alcaraz</strong> won in januari de Australian Open en is voor de vijfde keer op rij van de partij, ondanks een lange periode met een polsblessure. <strong>Ben Shelton</strong> stond dit jaar in de finale van de US Open en speelt voor de tweede keer op rij in Turijn.</p>
<h3><strong>Waarom speelt Jannik Sinner niet mee?</strong></h3>
<p>Sinner was op 10 juli de eerste speler die zich plaatste, door de finale van Wimbledon te halen. Daarna won hij de titel, maar sindsdien speelde hij niet meer. Op 6 oktober maakte hij bekend dat zijn seizoen voorbij is, omdat hij zijn knie moet laten behandelen. De Italiaan won de ATP Finals in 2024 en 2025, maar kan zijn titel dit jaar dus niet verdedigen.</p>
<p>Sinner staat met 7.950 punten nog wel op de tweede plaats van de Race. Volgens de regels gaat zijn plek naar de eerstvolgende speler op de lijst. Daarom tellen de plekken 1 tot en met 9 van de Race nu mee, zonder Sinner.</p>"""

content2 = f"""<h3><strong>Race to Turin 2026: de stand</strong></h3>
<p>Dit is de stand in de Race to Turin op {PEILDATUM}. De punten van de toernooien in Almaty, Lyon en Brussel, die deze week worden gespeeld, tellen al voor een deel mee.</p>
{tabel(["Positie", "Speler", "Punten", "Status"], [
    ("1", "Alexander Zverev (Duitsland)", "9.150", "Zeker"),
    ("2", "Jannik Sinner (Italië)", "7.950", "Afgemeld"),
    ("3", "Carlos Alcaraz (Spanje)", "4.600", "Zeker"),
    ("4", "Ben Shelton (Verenigde Staten)", "4.480", "Zeker"),
    ("5", "Flavio Cobolli (Italië)", "3.540", "Op koers"),
    ("6", "Daniil Medvedev", "3.420", "Op koers"),
    ("7", "Frances Tiafoe (Verenigde Staten)", "3.380", "Op koers"),
    ("8", "Arthur Fils (Frankrijk)", "3.375", "Op koers"),
    ("9", "Rafael Jódar (Spanje)", "3.159", "Op koers"),
    ("10", "Alex de Minaur (Australië)", "2.880", "Jager"),
    ("11", "Novak Djokovic (Servië)", "2.840", "Jager"),
    ("12", "Tommy Paul (Verenigde Staten)", "2.635", "Jager"),
    ("13", "Taylor Fritz (Verenigde Staten)", "2.530", "Jager"),
])}
<p><em>Live-stand van de Race to Turin op {PEILDATUM}. De stand verandert na elke gewonnen partij.</em></p>
<h3><strong>Wie maakt nog kans op de ATP Finals?</strong></h3>
<p>Achter de drie zekere spelers is het spannend. Tussen de nummer vijf, Cobolli, en de nummer negen, Jódar, zit nog geen 400 punten. Tiafoe en Fils staan zelfs maar 5 punten van elkaar.</p>
<p><strong>Flavio Cobolli</strong> haalde dit jaar de finale van Roland Garros en speelt deze week als eerste geplaatste in Lyon. <strong>Daniil Medvedev</strong> won de ATP Finals al eens in 2020 en is deze week de titelverdediger in Almaty. <strong>Frances Tiafoe</strong>, <strong>Arthur Fils</strong> en <strong>Rafael Jódar</strong> hopen op hun eerste deelname. Vooral Jódar maakte een sprong: de jonge Spanjaard haalde de finale van het Masters-toernooi in Shanghai en klom zo naar de laatste plek die toegang geeft.</p>
<p>De belangrijkste jagers zijn <strong>Alex de Minaur</strong> en <strong>Novak Djokovic</strong>. Zij staan nu op de plekken van de twee reservespelers. Djokovic, die het toernooi zeven keer won, kreeg een wildcard voor Basel.</p>
<h3><strong>Hoeveel punten zijn er nog te verdienen?</strong></h3>
<p>Na het Masters-toernooi in Parijs is de Race voor Turijn afgelopen. Tot die tijd zijn er nog deze toernooien:</p>
{tabel(["Week", "Toernooien", "Niveau", "Punten winnaar"], [
    ("19 t/m 25 oktober", "Almaty, Lyon en Brussel", "ATP 250", "250"),
    ("26 oktober t/m 1 november", "Basel en Wenen", "ATP 500", "500"),
    ("2 t/m 8 november", "Masters Parijs", "ATP 1000", "1.000"),
])}
<p>Een speler kan per week maar één toernooi spelen. Wie alles wint, pakt dus maximaal 1.750 punten. Dat is in de praktijk vaak minder, omdat niet elk resultaat meetelt: in de Race tellen de 18 beste resultaten van een speler. Het toernooi in Stockholm (8 tot en met 14 november) telt niet meer mee voor dit jaar, maar al voor de ATP Finals van 2027.</p>"""

content3 = f"""<h3><strong>Hoe werkt de kwalificatie voor de ATP Finals?</strong></h3>
<p>De lijst wordt opgemaakt op maandag 9 november, de dag na de finale in Parijs. De plekken gaan in deze volgorde weg:</p>
<ul><li><strong>Top 7:</strong> de zeven beste spelers van de Race to Turin zijn direct geplaatst.</li><li><strong>Grandslamwinnaars:</strong> heeft een speler dit jaar een grandslam gewonnen en staat hij op plek 8 tot en met 20, dan krijgt hij voorrang op de nummer acht. Dat geldt voor maximaal twee spelers.</li><li><strong>Plek 8:</strong> is er geen grandslamwinnaar buiten de top 7, dan gaat de laatste plek naar de nummer acht van de Race.</li></ul>
<p>Dit jaar speelt de grandslamregel geen rol. De vier grandslams zijn gewonnen door Alcaraz (Australian Open), Zverev (Roland Garros en US Open) en Sinner (Wimbledon). Zij staan allemaal in de top drie.</p>
<p><strong>Reservespelers.</strong> De eerste twee spelers die net buiten de boot vallen, zijn de reserves. Zij moeten in Turijn aanwezig zijn en vallen in als een speler zich afmeldt of tijdens het toernooi opgeeft. Lees ook <a href="/nieuws/tennisser-geeft-op-wat-zijn-de-regels-voor-je-weddenschap-bij-nederlandse-bookmakers">wat de regels zijn als een tennisser opgeeft</a> en <a href="/nieuws/wat-gebeurd-er-bij-een-walkover-met-een-tennisweddenschap">wat er gebeurt bij een walkover</a>.</p>
<p>In Turijn spelen de acht spelers eerst in twee groepen van vier. Alle partijen gaan over twee gewonnen sets. Hoe lang zo'n partij gemiddeld duurt, lees je in <a href="/nieuws/hoe-lang-duurt-een-tenniswedstrijd">hoe lang duurt een tenniswedstrijd</a>. Bij het dubbelspel zijn Heliövaara/Patten, Granollers/Zeballos en Harrison/Skupski al zeker van een plek.</p>
<h3><strong>Is Griekspoor gekwalificeerd voor de ATP Finals?</strong></h3>
<p>Nee. Er doet dit jaar geen Nederlander mee in Turijn. Botic van de Zandschulp is de beste Nederlander in de Race to Turin: hij staat 37e met 1.270 punten. Tallon Griekspoor staat 60e met 825 punten. Het verschil met de top negen is voor allebei te groot om nog goed te maken. Ook in het dubbelspel lukt het niet: Robin Haase staat met zijn Duitse partner Constantin Frantzen 15e in de Race en Sander Arends en David Pel staan 18e.</p>
<p>Alles over het toernooi vind je op de pagina van de <a href="/competities/atp-finals">ATP Finals</a>. Onze dagelijkse tips staan bij de <a href="/tennis-voorspellingen-vandaag">tennis voorspellingen van vandaag</a>.</p>
<h3><strong>Veelgestelde vragen over de ATP Finals 2026</strong></h3>
<p><strong>Wie zijn er gekwalificeerd voor de ATP Finals 2026?</strong><br>Op 22 oktober zijn Alexander Zverev, Carlos Alcaraz en Ben Shelton zeker. Jannik Sinner was ook gekwalificeerd, maar speelt niet mee door een knieblessure.</p>
<p><strong>Hoeveel plekken zijn er nog vrij?</strong><br>Vijf. Cobolli, Medvedev, Tiafoe, Fils en Jódar staan nu op die plekken. De Minaur en Djokovic zijn hun naaste jagers.</p>
<p><strong>Wanneer is bekend wie er meedoen?</strong><br>Na het Masters-toernooi in Parijs, dat op 8 november eindigt. De stand van maandag 9 november is beslissend.</p>
<p><strong>Is Griekspoor gekwalificeerd voor de ATP Finals?</strong><br>Nee. Griekspoor staat 60e in de Race to Turin en Van de Zandschulp 37e. Geen van beiden kan Turijn nog halen.</p>
<p><strong>Wat is de Race to Turin?</strong><br>Een ranglijst met alleen de punten die spelers in 2026 hebben verdiend. De beste acht mogen naar de ATP Finals.</p>
<p><strong>Wanneer en waar zijn de ATP Finals 2026?</strong><br>Van 15 tot en met 22 november 2026 in de Inalpi Arena in Turijn.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    alles = content + content2 + content3
    tekst = re.sub(r"<[^>]+>", " ", alles)
    woorden = len(tekst.split())
    intro = re.sub(r"<[^>]+>", " ", content.split("</p>")[0]).split()
    print("titel:", len(TITEL), "tekens |", TITEL)
    print("slug:", SLUG)
    print("samenvatting:", len(SAMENVATTING), "tekens")
    print("woorden:", woorden, "| intro (vet):", len(intro), "woorden")
    for n, c in (("content", content), ("content-2", content2), ("content-3", content3)):
        print(f"{n}: {len(c)} tekens")
    print("spelers deelkaart:", [(race_pos(i), s[0], s[2], pt(s[3])) for i, s in enumerate(SPELERS)])
    assert len(TITEL) <= 65
    assert 120 <= len(SAMENVATTING) <= 155
    assert "<h2" not in alles
    assert content.startswith("<p><strong>")
    assert not re.search(r"<(?:ul|ol)>\s|\s</(?:ul|ol)>|</li>\s+<li>|<li>\s", alles), "witruimte tussen lijst-tags"
    assert alles.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert alles.count("Wat kost gokken jou?") == 1
    assert 900 <= woorden <= 1400, woorden
    assert all(s[2] in ("Zeker", "Race") for s in SPELERS) and 8 <= len(SPELERS) <= 10
    print("dry run ok (niets gepubliceerd)")
