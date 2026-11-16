# -*- coding: utf-8 -*-
"""Los artikel: ATP Finals 2026, maandag 16 november (eerste speelronde Ivan Lendl Group).
16-11-2026 (avond) OMGEBOUWD van vooruitblik naar uitslagenartikel, na afloop van beide partijen.
LIVE item 6afb0430caba30afca744c32, slug atp-finals-maandag-16-november-voorspellingen-wedtips.

Uitslagen: Alcaraz - Tiafoe 6-2 6-2 (69 min) en Medvedev - Cobolli 7-6(4) 6-3 (1u25).
ONZE TIP WON: minder dan 2,5 sets in Medvedev - Cobolli (1,50) - de partij ging in twee sets.
Eerlijk vermeld: op Alcaraz - Tiafoe gaven we bewust geen tip, en beide games-markten die we toen te strak
vonden (minder dan 19,5 games 1,62 en Alcaraz -5,5 games 1,53) waren achteraf wél raak geweest. Dat staat erin.

Feiten: specials/atp_finals_dag3_feiten.md secties 1, 2 en 4 (officiele ATP-matchrapporten van maandag,
officiele groepsstanden nittoatpfinals.com, letterlijke citaten Alcaraz en Medvedev).
LET OP de valkuilen uit dat rapport:
 - speelduur Alcaraz - Tiafoe is 69 minuten; het rondzwervende "41 minuten" is het uitserveren, niet de partij.
 - "You're way too good" zei ALCARAZ tegen Tiafoe, niet omgekeerd. Niet omdraaien.
 - de ATP-uitslagenpagina gaf maandagavond een verouderde "In progress"-cache voor Medvedev - Cobolli;
   de groepsstandenpagina (13-9 games = 7-6 + 6-3) is leidend.
 - ATP zegt zes geredde breakpoints voor Cobolli in set 1; Italiaanse media zeggen vijf. ATP aangehouden.
Bewust weggelaten: winners/unforced errors van beide partijen (nergens gepubliceerd), aces/dubbele fouten van
Medvedev - Cobolli, citaten van Cobolli van na de wedstrijd (bestaan niet), speelduur van de dubbelpartijen.
  python3 specials/atp_finals_maandag_2026.py        (dry run)
  kaart: ../superodd-agent/.venv/bin/python og_kaarten/atp_finals_maandag_2026.py
  bijwerken: set -a; . ../superodd-agent/.env; set +a; ../superodd-agent/.venv/bin/python specials/bijwerk_live.py atp_finals_maandag_2026 6afb0430caba30afca744c32 --kaart"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "atp-finals-maandag-16-november-voorspellingen-wedtips"
ITEM_ID = "6afb0430caba30afca744c32"
RUBRIEK = "665715dbf1f3cbdf7f874d79"   # Tennis
BOOKMAKER_711 = "66a8a87062108480763b7309"
TITEL = "ATP Finals maandag: uitslagen Alcaraz en Medvedev en wedtip"
SAMENVATTING = ("Alcaraz won met 6-2, 6-2 van Tiafoe en Medvedev klopte Cobolli in twee sets. De uitslagen, de "
                "stand in de groep en hoe onze wedtip uitpakte.")
ODD = "1,50"

L = {"hub": '<a href="/tennis-voorspellingen-vandaag">tennis voorspellingen vandaag</a>',
     "dag1": '<a href="/nieuws/atp-finals-2026-dag-1-voorspellingen-wedtips">de uitslagen van dag 1</a>',
     "dinsdag": '<a href="/nieuws/atp-finals-dinsdag-17-november-voorspellingen-wedtips">onze tips voor dinsdag</a>',
     "groepen": '<a href="/nieuws/atp-finals-2026-groepen-loting-schema">de groepen en het schema van de ATP Finals 2026</a>',
     "ziggo": '<a href="/zenders/ziggo-sport">Ziggo Sport</a>',
     "kijken": '<a href="/live-kijken">live kijken</a>',
     "duur": '<a href="/nieuws/hoe-lang-duurt-een-tenniswedstrijd">hoelang een tenniswedstrijd duurt</a>',
     "opgave": '<a href="/nieuws/tennisser-geeft-op-wat-zijn-de-regels-voor-je-weddenschap-bij-nederlandse-bookmakers">wat er met je weddenschap gebeurt als een tennisser opgeeft</a>',
     "wedgids": '<a href="/wedgids">de Wedgids</a>',
     "711": '<a href="/bookmakers/711">711</a>',
     "legaal": '<a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>'}

UITSLAGEN = [("14:00 uur", "Carlos Alcaraz – Frances Tiafoe", "<strong>6-2, 6-2</strong>", "1 uur 9"),
             ("20:30 uur", "Daniil Medvedev – Flavio Cobolli", "<strong>7-6(4), 6-3</strong>", "1 uur 25"),
             ("11:30 uur", "Granollers/Zeballos – Bolelli/Vavassori (dubbel)", "<strong>6-4, 6-4</strong>", "–"),
             ("18:00 uur", "Krawietz/Pütz – Harrison/Skupski (dubbel)", "<strong>6-1, 6-3</strong>", "–")]

RESULTAAT = [("Minder dan 2,5 sets in Medvedev – Cobolli", "1,50",
              "Medvedev won in twee sets: 7-6(4), 6-3", "✅ gewonnen"),
             ("Alcaraz – Tiafoe", "–", "Bewust geen tip: de odds waren te strak geprijsd", "⚪ geen inzet")]

STAND = [("1", "Carlos Alcaraz", "1-0", "2-0", "12-4", "75,00%"),
         ("2", "Daniil Medvedev", "1-0", "2-0", "13-9", "59,09%"),
         ("3", "Flavio Cobolli", "0-1", "0-2", "9-13", "40,91%"),
         ("4", "Frances Tiafoe", "0-1", "0-2", "4-12", "25,00%")]

STATS_AT = [("Punten gewonnen", "<strong>57</strong>", "36"),
            ("Aces", "4", "<strong>7</strong>"),
            ("Punten gewonnen op de tweede service", "<strong>8 van 10</strong>", "<strong>0 van 12</strong>"),
            ("Breakpoints benut", "<strong>4 van 5</strong>", "0"),
            ("Breakpoints gered", "<strong>3 van 3</strong>", "1 van 5")]

WOENSDAG = [("14:00 uur", "<strong>Flavio Cobolli – Frances Tiafoe</strong>", "De verliezer is vrijwel uitgeschakeld"),
            ("niet voor 20:30 uur", "<strong>Carlos Alcaraz – Daniil Medvedev</strong>", "Twee winnaars tegenover elkaar, net als dinsdagavond")]


content = f"""<p><strong>De uitslagen van maandag 16 november op de ATP Finals: Carlos Alcaraz won met 6-2, 6-2 van Frances Tiafoe en Daniil Medvedev versloeg Flavio Cobolli met 7-6(4), 6-3. Onze wedtip — de partij tussen Medvedev en Cobolli in twee sets, odd 1,50 bij {L['711']} — kwam daarmee uit. Op de middagpartij gaven we bewust geen tip; verderop leggen we eerlijk uit wat dat ons kostte.</strong></p>
<p>Zo kwam de Ivan Lendl Group op gang zoals de papieren verhouding het voorschreef: de twee geplaatste favorieten wonnen allebei in twee sets, en de twee debutanten in deze groep staan na één speeldag al met de rug tegen de muur. Zondag opende de andere groep, met zeges voor Alexander Zverev en Ben Shelton; dat leest u in {L['dag1']}. Dinsdag is die groep weer aan de beurt, met Fils – Jódar en Zverev – Shelton: onze voorspellingen daarvoor staan in {L['dinsdag']}.</p>
<h3><strong>De uitslagen van maandag 16 november</strong></h3>
{tabel(["Tijd", "Wedstrijd", "Uitslag", "Speelduur"], UITSLAGEN)}
<p><em>De speelduur van de twee dubbelpartijen is niet gepubliceerd. Turijn heeft dezelfde tijd als Nederland; beide enkelpartijen waren te zien op {L['ziggo']}.</em></p>
<h3><strong>Hoe onze wedtip uitpakte</strong></h3>
{tabel(["Onze tip", "Odd", "Wat er gebeurde", "Resultaat"],
       [(f"<strong>{t}</strong>", o, w, r) for t, o, w, r in RESULTAAT])}
<p>De redenering achter de tip was dat Cobolli achttien dagen geen wedstrijd had gespeeld — hij gaf eind oktober op in Wenen met een spierblessure en trok zich daarna terug voor Parijs — en dat hij in zo'n partij vooral een korte, felle wedstrijd nodig had. Dat klopte: hij hield de eerste set tot in de tiebreak gelijk, maar zodra die weg was, ging het snel.</p>
<h3><strong>De stand in de Ivan Lendl Group</strong></h3>
{tabel(["#", "Speler", "Zeges", "Sets", "Games", "Gamepercentage"],
       [(n, f"<strong>{s}</strong>", z, st, g, p) for n, s, z, st, g, p in STAND])}
<p>Alcaraz en Medvedev staan allebei op één zege zonder setverlies, maar Alcaraz gaat bovenaan op gamepercentage: 75 procent tegen 59. Dat is geen schoonheidsprijs maar een officieel criterium — staan er straks drie spelers op evenveel zeges, dan beslist eerst het setpercentage en daarna het gamepercentage wie doorgaat. Cobolli en Tiafoe staan allebei op 0-2 in sets en spelen woensdag tegen elkaar om hun laatste realistische kans.</p>"""

content2 = f"""<h3><strong>Daniil Medvedev – Flavio Cobolli 7-6(4), 6-3</strong></h3>
<p>Een uur en 25 minuten, en veel spannender dan de setstanden doen vermoeden. <strong>Cobolli redde in de eerste set zes breakpoints</strong>, waaronder één op 3-4 en 30-40 met een diepe backhandpassing, en hield zo een Medvedev van zich af die de set eigenlijk de hele tijd in handen had. Pas in de tiebreak viel het om: 7-4.</p>
<p>Daarna was het klaar. In de tweede set brak Medvedev in de zevende game, en dat was genoeg. De cijfers verklaren waarom het zo moeilijk was om hem te breken: <strong>hij won 83 procent van de punten achter zijn eerste service, 34 van de 41</strong>. "I managed to serve well", zei hij na afloop. "It's a very fast indoor court, so the serve is important. I'm happy I managed to stay tough and get the win."</p>
<p>Voor Cobolli was dit zijn debuut op de ATP Finals, in eigen land, als enige Italiaan in het enkelspelschema. Hij speelde een goede eerste set en liet in de tweede zien dat achttien dagen zonder wedstrijd hun tol eisen. Onderling staat het nu 3-1 voor Medvedev. Woensdag speelt Cobolli tegen Tiafoe, de andere verliezer van maandag.</p>
<h3><strong>Carlos Alcaraz – Frances Tiafoe 6-2, 6-2</strong></h3>
<p>69 minuten, en geen moment echt spannend. Alcaraz liep in de openingsset meteen uit naar 4-0 en verloor in die set vrijwel niets op zijn eigen service. Bij 3-2 in de tweede set kwam Tiafoe nog één keer dichtbij met drie breakpoints — Alcaraz redde ze alle drie — en daarna sloeg de Spanjaard de partij uit op eigen service, afgesloten met een backhandwinner langs de lijn.</p>
{tabel(["", "Alcaraz", "Tiafoe"], STATS_AT)}
<p><em>De partij werd beslist op de tweede service. Tiafoe won daar geen enkel punt: nul uit twaalf.</em></p>
<p>Dat ene cijfer is het hele verhaal. Tiafoe sloeg méér aces dan Alcaraz (zeven om vier), maar zodra zijn eerste service niet viel, was het punt weg. Alcaraz won in totaal 57 punten tegen 36.</p>
<p>Alcaraz komt uit opeenvolgende titels in Wenen en Parijs en staat nu op tien zeges op rij. Hij miste dit jaar vier maanden met een polsblessure en won sinds zijn rentree op het US Open twintig van zijn 22 partijen. "I would say this is the best I have felt so far in my career at this part of the season", zei hij na afloop. "Coming here I have a lot of energy and ambition and I am hungry for more." Hij staat voor het vierde jaar in Turijn en was vorig jaar finalist.</p>
<p>Tiafoe maakte op zijn 28e zijn debuut op de ATP Finals, na het beste seizoen van zijn loopbaan met 44 zeges en de titel in Halle. Hij is daarmee de oudste debutant op dit toernooi sinds 2018. Over zijn tegenstander zei hij achteraf dat Alcaraz op momenten gewoon "Superman" is. Onderling staat het nu 3-1 voor Alcaraz.</p>
<h3><strong>En de partij waar we vanaf bleven</strong></h3>
<p>Eerlijk is eerlijk: dit kostte ons wat. Wij gaven op Alcaraz – Tiafoe geen tip, om twee redenen. De eerste was dat de odd op Alcaraz maandagochtend van 1,12 naar <strong>1,03</strong> schoof zonder dat daar een gepubliceerde reden voor was — zo'n beweging is een waarschuwing dat de markt iets weet wat niet in het nieuws staat. De tweede was dat de games-markten er strak omheen lagen: minder dan 19,5 games stond op 1,62 en zou al verliezen bij 6-4, 6-4, en Alcaraz met -5,5 games stond op 1,53 en zou al verliezen bij 6-4, 6-3.</p>
<p>Het werd 6-2, 6-2: zestien games, een verschil van acht. <strong>Allebei die weddenschappen waren dus raak geweest.</strong> Dat is geen reden om de redenering achteraf anders te maken — bij een odd van 1,03 en een plotselinge beweging zonder uitleg blijven wij eraf — maar het hoort er wel bij dat we het opschrijven. Op dinsdag en woensdag liggen de marges ruimer.</p>"""

content3 = f"""<h3><strong>Wat gebeurt er woensdag?</strong></h3>
<p>De twee groepen wisselen elkaar per dag af. Dinsdag 17 november speelt de John McEnroe Group zijn tweede ronde; deze groep is woensdag 18 november weer aan de beurt.</p>
{tabel(["Tijd", "Wedstrijd", "Wat er op het spel staat"], WOENSDAG)}
<p>De McEnroe-groep sluit af op donderdag 19 november, deze groep op vrijdag 20 november. De halve finales zijn zaterdag 21 november, de finale zondag 22 november. Het volledige schema en beide groepen staan in {L['groepen']}. Onze voorspellingen voor dinsdag, met Fils – Jódar en Zverev – Shelton, lees je in {L['dinsdag']}, en alle tennistips van vandaag verzamelen we op {L['hub']}.</p>
<h3><strong>Wat betekende deze weddenschap?</strong></h3>
<p><strong>Minder dan 2,5 sets.</strong> Op de ATP Finals gaat elke partij over twee gewonnen sets, dus er worden twee of drie sets gespeeld. Bij deze weddenschap moet de wedstrijd in twee sets klaar zijn, ongeacht wie wint. De halve set in de lijn zorgt ervoor dat er geen gelijkspel kan zijn. Medvedev won met 7-6(4), 6-3 en dus is deze weddenschap gewonnen; was Cobolli met 2-0 doorgegaan, dan had je ook gewonnen.</p>
<p>Geeft een speler op, dan bepalen de regels van je bookmaker wat er met je inzet gebeurt: lees {L['opgave']}. Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit; in {L['legaal']} leggen we uit waar je dat aan ziet. Meer uitleg over soorten weddenschappen vind je in {L['wedgids']}, en hoe lang je voor een avondpartij moet uittrekken staat in {L['duur']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wat waren de uitslagen van maandag 16 november op de ATP Finals?</strong><br>Carlos Alcaraz won met 6-2, 6-2 van Frances Tiafoe en Daniil Medvedev versloeg Flavio Cobolli met 7-6(4), 6-3. In het dubbelspel wonnen Granollers/Zeballos met 6-4, 6-4 en Krawietz/Pütz met 6-1, 6-3.</p>
<p><strong>Kwam de wedtip van maandag uit?</strong><br>Ja. De tip was minder dan 2,5 sets in Medvedev – Cobolli op {ODD}; die partij werd in twee sets beslist. Op Alcaraz – Tiafoe gaven we geen tip.</p>
<p><strong>Hoe lang duurde Alcaraz – Tiafoe?</strong><br>69 minuten. Medvedev – Cobolli duurde een uur en 25 minuten.</p>
<p><strong>Hoe staat het in de Ivan Lendl Group?</strong><br>Alcaraz en Medvedev staan allebei op één zege zonder setverlies; Alcaraz gaat bovenaan op gamepercentage (75 om 59 procent). Cobolli en Tiafoe staan op nul zeges en spelen woensdag tegen elkaar.</p>
<p><strong>Wie speelt er woensdag 18 november?</strong><br>Flavio Cobolli – Frances Tiafoe om 14:00 uur en Carlos Alcaraz – Daniil Medvedev niet voor 20:30 uur.</p>
<p><strong>Hoeveel zeges op rij heeft Alcaraz nu?</strong><br>Tien. Hij won daarvoor de titels in Wenen en Parijs, en sinds zijn rentree op het US Open na een polsblessure won hij twintig van zijn 22 partijen.</p>
<p><strong>Waar kon je de ATP Finals maandag kijken?</strong><br>Op Ziggo Sport: de middagsessie van 14:00 tot 16:00 uur op Ziggo Sport 1 en Ziggo Sport 4, de avondsessie van 20:30 tot 22:30 uur op Ziggo Sport 4.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

WEDTIPS = {"wedstrijd-1": "Medvedev vs Cobolli", "wedtip-1-2": "Minder dan 2.5 sets (de wedstrijd in twee sets)",
           "quotering-wedtip-1": "1.50"}

if __name__ == "__main__":
    import re
    if "--velden" in sys.argv:
        import lk_webflow as WF
        it = WF._req("GET", f"{WF.WF_API}/collections/{WF.NIEUWS_COLLECTION}/items?slug={SLUG}")["items"][0]
        fd = {"tennis": True, "bookmaker-wedtips": BOOKMAKER_711, "datum-tijd-van-wedstrijd": "2026-11-16T19:30:00.000Z", **WEDTIPS}
        for pad in ("", "/live"):
            WF._req("PATCH", f"{WF.WF_API}/collections/{WF.NIEUWS_COLLECTION}/items/{it['id']}{pad}", {"fieldData": fd})
        print("velden gezet:", it["id"]); sys.exit()
    alles = content + content2 + content3
    w = len(re.sub(r"<[^>]+>", " ", alles).split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", w, "woorden")
    assert len(TITEL) <= 60 and 120 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert 1200 <= w <= 2400, w
    assert ODD == "1,50"
    assert 7 + 6 + 6 + 3 == 22 and 6 + 2 + 6 + 2 == 16            # gamestellingen
    assert 12 - 4 == 8 and 13 - 9 == 4                            # gamesaldo uit de officiele stand
    assert 6 + 4 + 6 + 4 == 20 > 19.5 and 6 - 4 == 2 < 5.5        # waarom die twee markten te strak waren
    assert 16 < 19.5 and 12 - 4 > 5.5                             # ... en achteraf toch raak
    assert sum(1 for r in RESULTAAT if "✅" in r[3]) == 1
    assert len(STAND) == 4 and len(UITSLAGEN) == 4 and len(STATS_AT) == 5
    assert "<h2" not in alles and "<h4" not in alles and "/go/" not in alles
    for verboden in ("betcity", "footymetrics", "opstellingvandaag", "waaroptv", "squawka"):
        assert verboden not in alles.lower(), verboden
    assert "41 minuten" not in alles                              # bekende foute speelduur
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    print("dry run ok")
