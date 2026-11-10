# -*- coding: utf-8 -*-
"""Los artikel (cluster Grand Slam of Darts 2026): het nieuwe format (48 spelers, 16 groepen van 3).
Zoekwoorden: grand slam of darts format 2026 / new format / groepen / poules / hoe werkt.
Feiten: pdc.tv 11-02-2026 (48 spelers, 16 groepen van 3, top 16 geplaatst, potten), gsod_feiten_2026.md (groepsfase bo9,
alleen groepswinnaars door volgens Wikipedia/DartsKing/Darts Planet -> 'volgens de huidige opzet'; knock-out bo19/bo31 zoals 2025),
Wikipedia 2025 (format 2025: 8 groepen van 4, top 2 door, bo9/bo19/bo31).
  python3 specials/gsod_format_2026.py   (dry run)"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel
import gsod_data as G

SLUG = G.SLUGS["format"]
RUBRIEK = G.RUBRIEK
TITEL = "Grand Slam of Darts 2026 format: zo werken de 16 poules"
SAMENVATTING = ("Het nieuwe format van de Grand Slam of Darts 2026: 48 spelers, 16 groepen van drie en alleen de groepswinnaar "
                "door. Alles uitgelegd.")

OG_EYEBROW = "Darts · nieuw format 2026"
OG_KOP = "Nieuw format<br><em>Grand Slam 2026</em>"
OG_TEGELS = [("Spelers", "48"), ("Groepen", "16 × 3")]
OG_KOPJE = "Van groep naar finale"
OG_RECHTS = "Best of (legs)"
OG_RIJEN = [("Groepsfase", "2 duels per speler · winnaar door", "Best of 9"),
            ("Laatste 16", "16 groepswinnaars", "Best of 19"),
            ("Kwart + halve", "8 en 4 spelers", "Best of 31"),
            ("Finale", "Eric Bristow Trophy", "Best of 31")]

content = f"""<p><strong>De Grand Slam of Darts krijgt in 2026 een nieuw format. Het veld groeit van 32 naar 48 spelers, die in 16 groepen van drie worden verdeeld in plaats van in 8 groepen van vier. Iedere speler speelt twee groepswedstrijden over best of 9 legs. Volgens de huidige opzet gaat alleen de groepswinnaar door naar de laatste 16; vanaf daar is het een knock-outtoernooi tot en met de finale op zondag 22 november.</strong></p>
<h3><strong>Wat verandert er aan de Grand Slam of Darts in 2026?</strong></h3>
{tabel(["", "2025", "2026"], [
    ("<strong>Spelers</strong>", "32", "48"),
    ("<strong>Groepen</strong>", "8 groepen van 4", "16 groepen van 3"),
    ("<strong>Groepswedstrijden per speler</strong>", "3", "2"),
    ("<strong>Door naar de knock-out</strong>", "Nummers 1 en 2 van elke groep", "Alleen de groepswinnaar (huidige opzet)"),
    ("<strong>Eerste knock-outronde</strong>", "Laatste 16", "Laatste 16"),
    ("<strong>Plekken via de qualifier</strong>", "8", "Minimaal 8"),
    ("<strong>Prijzengeld</strong>", "£650.000", "£1.000.000"),
    ("<strong>Speeldagen</strong>", "9", "9 (12 sessies)"),
])}
<p>De PDC maakte de uitbreiding in februari bekend. Met 48 spelers is er plek voor meer winnaars van de vloertoernooien en voor meer spelers van de secundaire circuits, zoals de jeugd, de vrouwen en de regionale tours in Azië, Noord-Amerika, Scandinavië en Australië.</p>"""

content2 = f"""<h3><strong>Zo werkt de groepsfase</strong></h3>
<p>Elke groep bestaat uit drie spelers: één van de 16 hoogst geplaatste deelnemers, één uit de groep 17 tot en met 32 van de PDC-ranking en één uit de groep 33 tot en met 48. De 16 geplaatste spelers worden volgens een vast schema over de groepen verdeeld, de andere twee worden geloot.</p>
<p>In een groep van drie worden drie wedstrijden gespeeld, en iedereen speelt er twee. Een zege levert twee punten op. De volgorde is vast: op zaterdag 14 november speelt in elke groep het eerste duel, op zondag 15 november het tweede, en op maandag 16 (groepen A tot en met H) of dinsdag 17 november (groepen I tot en met P) het laatste. Bij een gelijke stand beslist volgens de huidige opzet het legsaldo. Alle groepswedstrijden gaan over best of 9 legs: wie als eerste vijf legs wint, wint de wedstrijd.</p>
<p><strong>Wat betekent dat in de praktijk?</strong> Met maar twee wedstrijden is er weinig ruimte voor een slechte dag. Verlies je je eerste wedstrijd, dan moet je de tweede winnen en hopen op een gunstige uitslag in het andere duel. En omdat in een korte partij over best of 9 legs alles kan gebeuren, is de kans op verrassingen groter dan in de knock-outfase. Voor de grote namen is de groepsfase dus de gevaarlijkste fase van het toernooi.</p>
<h3><strong>Zo werkt de knock-outfase</strong></h3>
{tabel(["Ronde", "Spelers", "Best of", "Wanneer (NL-tijd)"], [
    ("<strong>Laatste 16</strong>", "16", "19 legs (10 om te winnen)", "Wo 18 en do 19 november, 20:00"),
    ("<strong>Kwartfinales</strong>", "8", "31 legs (16 om te winnen)", "Vr 20 en za 21 november, 20:00"),
    ("<strong>Halve finales</strong>", "4", "31 legs", "Zo 22 november, 14:00"),
    ("<strong>Finale</strong>", "2", "31 legs", "Zo 22 november, 20:30"),
])}
<p>Vanaf de kwartfinales zijn de wedstrijden bij de Grand Slam lang: je moet 16 legs winnen. Ter vergelijking: een finale op een European Tour-toernooi win je al met acht legs. Dat beloont spelers met een hoog en constant niveau. De best-of-lengtes in de knock-outfase zijn de huidige planning en gelijk aan vorig jaar.</p>"""

content3 = f"""<h3><strong>Wat betekent het nieuwe format voor de favorieten?</strong></h3>
<p>Voor titelverdediger Luke Littler en de andere toppers is de groepsfase spannender geworden. Vorig jaar kon je met één zege uit drie wedstrijden soms nog doorgaan; nu moet je in de regel allebei je wedstrijden winnen om groepswinnaar te worden. Ook het prijzengeld weerspiegelt dat: de nummer 2 van een groep gaat met £12.500 naar huis, de groepswinnaar heeft minimaal £20.000 zeker. Alle bedragen staan in ons artikel over het {G.a('prijzengeld', 'prijzengeld van de Grand Slam of Darts 2026')}.</p>
<p>Wie er in de groepen terechtkomen, hangt af van de loting. Die volgt pas als het veld compleet is, na het Nordic & Baltic Championship van 8 november. Lees in {G.a('deelnemers', 'deelnemers, poules en loting')} wie er al zeker zijn, en bekijk het {G.a('speelschema', 'speelschema van de Grand Slam of Darts 2026')} voor alle dagen en tijden. Ken je de basis van het darten nog niet? Lees dan eerst {G.EXTRA['regels']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe werkt de Grand Slam of Darts 2026?</strong><br>48 spelers worden verdeeld over 16 groepen van drie. Iedere speler speelt twee groepswedstrijden over best of 9 legs. Volgens de huidige opzet gaan de 16 groepswinnaars door naar de laatste 16, waarna het toernooi tot en met de finale een knock-outtoernooi is.</p>
<p><strong>Hoeveel groepen zijn er op de Grand Slam of Darts 2026?</strong><br>16 groepen (A tot en met P) van drie spelers.</p>
<p><strong>Gaan er twee spelers per groep door?</strong><br>Volgens de huidige opzet niet: alleen de groepswinnaar gaat door. In 2025, met groepen van vier, gingen de nummers 1 en 2 door.</p>
<p><strong>Over hoeveel legs wordt de finale gespeeld?</strong><br>Over best of 31 legs: wie als eerste 16 legs wint, is kampioen.</p>
{G.SLOT}"""

if __name__ == "__main__":
    alles = G.check(sys.modules[__name__], 750)
    print("dry run ok – niets gepubliceerd")
