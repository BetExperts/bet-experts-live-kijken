# -*- coding: utf-8 -*-
"""Los artikel: Grand Slam of Darts 2026 voorspellingen en wedtips dag 1 (zaterdag 14 november, groepsfase speelronde 1).
Tips: Woodhouse wint (1.55), Clayton -2.5 legs (1.67), Price -1.5 legs (1.48), Humphries -2.5 legs (1.52). Combi 5,82.
Odds: Unibet NL (Kambi ubnl), vrijdag 13-11 ±14:00. Groepsfase = best of 9 legs.
Feiten: specials/gsod_dag1_feiten.md (mastercaller WGP/EK-gemiddelden, Sporting Life/Sky/Dartsplanet/DartsKing PC31-34,
Dartsnews form guide en jaarranglijst (aug), interviews) + gsod_data.py (groepen, sessies, winnaars).
Fitheid gecheckt: Humphries voedselvergiftiging (EK afgemeld) -> hersteld, won PC33 + finale PC34; Aspinall miste PC34 zonder
bekende reden -> geen tip; Littler sinds 25-10 geen officiële partij -> geen tip; Van Veen nierstenen voorjaar -> geen klachten.
Weggelaten: exacte aanvangstijden per partij (schattingen), seizoensgemiddelden (alleen augustus-cijfers, niet genoemd).
  python3 specials/gsod_dag1_tips_2026.py   (dry run)
  publiceren: specials/concept_publiceer.py gsod_dag1_tips_2026 --live ; daarna --velden"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, "..")); sys.path.insert(0, HIER)
from legaal_data import tabel
import gsod_data as G

SLUG = "grand-slam-of-darts-2026-voorspellingen-wedtips-dag-1"
RUBRIEK = G.RUBRIEK
UNIBET = "64ff0fbd5a8f205b05d54687"
TITEL = "Grand Slam of Darts voorspellingen dag 1: 4 beste wedtips"
SAMENVATTING = ("Grand Slam of Darts voorspellingen voor zaterdag 14 november: Woodhouse, Clayton, Price en Humphries. "
                "Vier wedtips met odds en uitleg.")
ODDS = [1.55, 1.67, 1.48, 1.52]
COMBI = "5,82"

OG_EYEBROW = "Darts · zaterdag 14 november"
OG_KOP = "Grand Slam dag 1:<br><em>beste wedtips</em>"
OG_TEGELS = [("Partijen", "16"), ("Combi-odd", COMBI)]
OG_KOPJE = "Onze tips (best of 9 legs)"
OG_RECHTS = "Odds bij Unibet"
OG_RIJEN = [("Middag", "Woodhouse wint van Sykes", "1,55"),
            ("Middag", "Clayton -2,5 legs v. Östlund", "1,67"),
            ("Avond", "Price -1,5 legs v. Hunt", "1,48"),
            ("Avond", "Humphries -2,5 legs v. Nebrida", "1,52")]

L = {"unibet": '<a href="/bookmakers/unibet">Unibet</a>',
     "handicap": '<a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">hoe handicap wedden werkt</a>',
     "legaal": '<a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>'}


def waarom(punten):
    return "<p><strong>Waarom deze tip?</strong></p><ul>" + "".join(f"<li>{p}</li>" for p in punten) + "</ul>"


TIPS = [("Woodhouse – Sykes", "Middag (1e partij)", "Luke Woodhouse wint", "Winnaar", "1,55"),
        ("Clayton – Östlund", "Middag (8e partij)", "Jonny Clayton -2,5 legs", "Leg handicap", "1,67"),
        ("Price – Hunt", "Avond (1e partij)", "Gerwyn Price -1,5 legs", "Leg handicap", "1,48"),
        ("Humphries – Nebrida", "Avond (5e partij)", "Luke Humphries -2,5 legs", "Leg handicap", "1,52")]

PROGRAMMA = [("Middag", "J", "Luke Woodhouse – Tom Sykes", "1,55 – 2,45"),
             ("Middag", "B", "Jermaine Wattimena – Lisa Ashton", "1,04 – 11,00"),
             ("Middag", "D", "Stephen Bunting – Raymond Smith", "1,43 – 2,85"),
             ("Middag", "F", "Ryan Searle – Charlie Manby", "1,63 – 2,28"),
             ("Middag", "C", "Josh Rock – Tommy Morris", "1,73 – 2,12"),
             ("Middag", "H", "Wessel Nijman – Adam Sevada", "1,20 – 4,60"),
             ("Middag", "P", "Nathan Aspinall – Maik Kuivenhoven", "1,32 – 3,40"),
             ("Middag", "G", "Jonny Clayton – Anton Östlund", "1,14 – 6,00"),
             ("Avond", "E", "Gerwyn Price – Joe Hunt", "1,25 – 4,00"),
             ("Avond", "K", "James Wade – Cam Crabtree", "1,35 – 3,25"),
             ("Avond", "O", "Ross Smith – Rusty-Jake Rodriguez", "1,08 – 7,50"),
             ("Avond", "L", "Michael van Gerwen – Henry Coates", "1,50 – 2,55"),
             ("Avond", "I", "Luke Humphries – Paolo Nebrida", "1,10 – 7,00"),
             ("Avond", "A", "Luke Littler – Beau Greaves", "1,25 – 4,00"),
             ("Avond", "M", "Gian van Veen – Carl Sneyd", "1,27 – 3,75"),
             ("Avond", "N", "Chris Dobey – Jan Schmidt", "1,18 – 5,00")]

content = f"""<p><strong>Onze Grand Slam of Darts voorspellingen voor dag 1, zaterdag 14 november: Luke Woodhouse wint van Tom Sykes (1,55), Jonny Clayton wint met minstens drie legs verschil van Anton Östlund (-2,5 legs, 1,67), Gerwyn Price wint met minstens twee legs verschil van Joe Hunt (-1,5 legs, 1,48) en Luke Humphries wint met minstens drie legs verschil van Paolo Nebrida (-2,5 legs, 1,52). Gecombineerd is dat een odd van ongeveer {COMBI} bij Unibet. Alle groepswedstrijden gaan over best of 9 legs: wie als eerste vijf legs wint, wint de partij.</strong></p>
<p>De Grand Slam of Darts 2026 begint zaterdag in Wolverhampton met zestien partijen: acht in de middagsessie vanaf 14:00 uur en acht in de avondsessie vanaf 20:00 uur. Voor het eerst doen er 48 spelers mee in 16 groepen van drie, en alleen de groepswinnaar gaat door. Op dag 1 speelt in elke groep het geplaatste reekshoofd tegen de outsider uit pot 3. Een nederlaag is dus meteen een flinke klap. Alle groepen en de kansen van de zeven Nederlanders lees je in ons artikel over de {G.a('deelnemers', 'loting van de Grand Slam of Darts 2026')}.</p>
<h3><strong>Grand Slam of Darts voorspellingen dag 1 in het kort</strong></h3>
{tabel(["Partij", "Sessie", "Tip", "Markt", "Odd"], [(f"<strong>{w}</strong>", s, t, m, f"<strong>{o}</strong>") for w, s, t, m, o in TIPS] + [("<strong>Combinatie</strong>", "", "Alle vier de tips", "", f"<strong>{COMBI}</strong>")])}
<p><em>Odds bij {L['unibet']}, vrijdag 13 november rond 14:00 uur. Odds kunnen nog veranderen. De tips staan los van elkaar.</em></p>
<h3><strong>Het programma van zaterdag 14 november</strong></h3>
{tabel(["Sessie", "Groep", "Partij", "Odds (Unibet)"], [(s, g, p, o) for s, g, p, o in PROGRAMMA])}
<p><em>Middagsessie vanaf 14:00 uur, avondsessie vanaf 20:00 uur (Nederlandse tijd), in deze volgorde. Een partij duurt ongeveer 25 minuten. De sessies zijn live te zien bij Viaplay; lees ook {G.a('tv', 'waar je de Grand Slam of Darts live kijkt')}.</em></p>"""

content2 = f"""<h3><strong>Tip 1: Luke Woodhouse – Tom Sykes (middag, eerste partij)</strong></h3>
<p>Woodhouse opent het toernooi in vorm. Op de World Grand Prix in oktober versloeg hij Luke Littler, en op het Europees kampioenschap haalde hij de kwartfinale, waarin hij met een gemiddelde van 103,40 nipt verloor van Ross Smith. Vorig jaar won hij op de Grand Slam al zijn groep met drie zeges. Tom Sykes debuteert op het toernooi: hij plaatste zich via de qualifier met een 5-3-zege op de laatste dag. Hij is een gevaarlijke speler (hij gooide dit najaar een negendarter op de Players Championship-vloer), maar op het tv-podium van een groot toernooi staat hij voor het eerst.</p>
<p><strong>Onze tip: Woodhouse wint (1,55).</strong> De markt is gewoon de winnaar van de partij.</p>
{waarom(["<strong>Woodhouse speelt het beste darts van zijn carrière.</strong> Een zege op Littler en 103,40 gemiddeld op het EK.",
         "<strong>Ervaring tegen debuut.</strong> Woodhouse kent het Grand Slam-podium, Sykes niet.",
         "<strong>De odd is ruim.</strong> 1,55 gaat uit van ongeveer 65 procent; op basis van de vorm schatten wij de kans hoger in."])}
<p><strong>Het risico:</strong> in een best of 9 kan één slechte start beslissend zijn, en Sykes kan op een goede dag hoog scoren.</p>
<h3><strong>Tip 2: Jonny Clayton – Anton Östlund (middag, achtste partij)</strong></h3>
<p>Clayton won dit jaar de Swiss Darts Trophy en versloeg Littler met 10-4 op de World Series Finals. Op het EK ging hij wel onderuit tegen Martin Schindler (1-10), maar op een korte afstand is de Welshman een van de meest constante spelers van het circuit. Anton Östlund uit Zweden plaatste zich via de Nordic & Baltic-qualifier, die hij in de finale won met een gemiddelde van 83,11. Dat is ruim onder het niveau van de top van de PDC.</p>
<p><strong>Onze tip: Clayton -2,5 legs (1,67).</strong> De markt: leg handicap. Clayton moet met minstens drie legs verschil winnen, dus 5-2, 5-1 of 5-0. Bij 5-3 of een nederlaag is de tip verloren. Meer uitleg lees je in {L['handicap']}.</p>
{waarom(["<strong>Groot niveauverschil.</strong> Een gemiddelde rond de 83 is bij de PDC-top meestal niet genoeg om veel legs te pakken.",
         "<strong>Clayton wint staat op 1,14.</strong> Dat is te laag; met -2,5 legs krijg je een speelbare odd voor een ruime zege."])}
<p><strong>Het risico:</strong> Claytons EK-nederlaag laat zien dat hij ook slechte avonden heeft, en Östlund heeft weinig te verliezen.</p>
<h3><strong>Tip 3: Gerwyn Price – Joe Hunt (avond, eerste partij)</strong></h3>
<p>Price is in topvorm. Hij haalde de finale van de World Grand Prix en de halve finale van het EK, waar hij in de kwartfinale 103,00 gemiddeld gooide. In de vormranglijst van de laatste weken staat hij bovenaan, met een gemiddelde van ruim 100. Bovendien won hij de Grand Slam al drie keer. Joe Hunt won dit jaar vijf toernooien op de Challenge Tour, maar speelt zaterdag zijn eerste groot tv-toernooi.</p>
<p><strong>Onze tip: Price -1,5 legs (1,48).</strong> Price moet met minstens twee legs verschil winnen: 5-3 of beter. Bij 5-4 is de tip verloren.</p>
{waarom(["<strong>Vorm.</strong> Price is op dit moment de speler met het hoogste gemiddelde van de laatste weken.",
         "<strong>Ervaring.</strong> Drievoudig Grand Slam-winnaar tegen een debutant op het grote podium."])}
<p><strong>Het risico:</strong> Hunt is een winnaar op de Challenge Tour en kan vrij spelen. Wordt het 5-4, dan mis je de handicap.</p>
<h3><strong>Tip 4: Luke Humphries – Paolo Nebrida (avond, vijfde partij)</strong></h3>
<p>Humphries meldde zich in oktober af voor het EK door voedselvergiftiging: hij viel ongeveer zes kilo af en trainde twee weken niet. Inmiddels is hij helemaal terug. Hij won Players Championship 33 met een gemiddelde van 103,77 in de finale en haalde een dag later opnieuw de finale. Paolo Nebrida uit de Filipijnen debuteert op de Grand Slam. Op het WK van vorig jaar versloeg hij verrassend Ross Smith, dus onderschatten mag niet.</p>
<p><strong>Onze tip: Humphries -2,5 legs (1,52).</strong> Humphries moet met minstens drie legs verschil winnen: 5-2 of beter.</p>
{waarom(["<strong>Humphries is hersteld en in vorm.</strong> Een titel en een finale op de laatste twee Players Championships.",
         "<strong>Klasseverschil.</strong> De Grand Slam-winnaar van 2023 tegen een debutant uit het Aziatische circuit."])}
<p><strong>Het risico:</strong> Nebrida liet op het WK zien dat hij op een groot podium kan verrassen. Twee gewonnen legs zijn genoeg om deze handicap te laten mislukken bij 5-3.</p>"""

content3 = f"""<h3><strong>De Nederlanders op dag 1</strong></h3>
<p>Vijf van de zeven Nederlanders spelen zaterdag. Wij geven op hun partijen geen aparte tip, maar dit is hoe wij het zien.</p>
<ul><li><strong>Jermaine Wattimena – Lisa Ashton (middag)</strong>: Wattimena is grote favoriet (1,04). Ashton kwam in vijf deelnames nooit door de groep.</li><li><strong>Wessel Nijman – Adam Sevada (middag)</strong>: Nijman is favoriet (1,20), maar haalde op het EK geen tweede ronde. Sevada won het North American Championship.</li><li><strong>Nathan Aspinall – Maik Kuivenhoven (middag)</strong>: debutant Kuivenhoven is de underdog (3,40), maar haalde dit jaar twee finales op de vloer. Aspinall speelde Players Championship 34 niet; de reden is niet bekend.</li><li><strong>Michael van Gerwen – Henry Coates (avond)</strong>: Van Gerwen (1,50) ging op de World Grand Prix en het EK in de eerste ronde onderuit, maar gooide daarna 114,15 gemiddeld in een partij op de vloer. Coates won dit jaar een Players Championship. Een lastige partij.</li><li><strong>Gian van Veen – Carl Sneyd (avond)</strong>: Van Veen is duidelijk favoriet (1,27) tegen debutant Sneyd. Van Veen haalde de kwartfinale van de World Grand Prix.</li></ul>
<p>Niels Zonneveld en Kevin Doets spelen pas zondag. Jeffrey de Graaf, die in de groep van Van Gerwen zit, speelt voor Zweden.</p>
<h3><strong>En Littler tegen Greaves?</strong></h3>
<p>De afsluiter van de avond is de partij waar iedereen naar uitkijkt: titelverdediger Luke Littler tegen Beau Greaves. Onderling staat het 1-1, maar nooit op tv: Greaves won met 6-5 op het jeugd-WK van 2025, Littler met 6-5 op de vloer. Littler is favoriet (1,25), maar hij speelde sinds 25 oktober geen officiële partij en ging op de laatste drie grote toernooien niet verder dan de kwartfinale. Te veel vraagtekens voor een tip; wij laten deze partij liggen.</p>
<h3><strong>Wat betekenen deze weddenschappen?</strong></h3>
<p><strong>Winnaar.</strong> De speler moet de partij winnen. In de groepsfase is dat als eerste vijf legs.</p>
<p><strong>Leg handicap.</strong> Bij -1,5 legs moet je speler met minstens twee legs verschil winnen (5-3 of beter), bij -2,5 legs met minstens drie (5-2 of beter).</p>
<p>Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit; lees {L['legaal']}. Het hele toernooi vind je in ons {G.a('speelschema', 'speelschema van de Grand Slam of Darts 2026')}, het prijzengeld in {G.a('prijzengeld', 'prijzengeld Grand Slam of Darts 2026')}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wat zijn de beste wedtips voor dag 1 van de Grand Slam of Darts?</strong><br>Woodhouse wint van Sykes (1,55), Clayton -2,5 legs tegen Östlund (1,67), Price -1,5 legs tegen Hunt (1,48) en Humphries -2,5 legs tegen Nebrida (1,52). Samen ongeveer {COMBI}.</p>
<p><strong>Hoe laat begint de Grand Slam of Darts op zaterdag?</strong><br>De middagsessie begint om 14:00 uur, de avondsessie om 20:00 uur Nederlandse tijd.</p>
<p><strong>Hoeveel legs is een partij in de groepsfase?</strong><br>Best of 9: wie als eerste vijf legs wint, wint de partij.</p>
<p><strong>Welke Nederlanders spelen zaterdag?</strong><br>Wattimena, Nijman en Kuivenhoven in de middag, Van Gerwen en Van Veen in de avond.</p>
<p><strong>Hoe laat speelt Luke Littler?</strong><br>In de avondsessie, als zesde partij, tegen Beau Greaves. Reken op een aanvang ergens na 22:00 uur.</p>
{G.SLOT}"""

WEDTIPS = {"wedstrijd-1": "Combinatie: alle vier de tips",
           "wedtip-1-2": "Woodhouse wint + Clayton -2.5 legs + Price -1.5 legs + Humphries -2.5 legs",
           "quotering-wedtip-1": "5.82",
           "wedstrijd-2": "Woodhouse vs Sykes", "wedtip-2-2": "Luke Woodhouse wint", "quotering-wedtip-2": "1.55",
           "wedstrijd-3": "Price vs Hunt", "wedtip-3-2": "Gerwyn Price -1.5 legs", "quotering-wedtip-3": "1.48",
           "wedtip-4-2": "Luke Humphries -2.5 legs tegen Nebrida", "quotering-wedtip-4": "1.52"}

if __name__ == "__main__":
    if "--velden" in sys.argv:
        import lk_webflow as WF
        it = WF._req("GET", f"{WF.WF_API}/collections/{WF.NIEUWS_COLLECTION}/items?slug={SLUG}")["items"][0]
        fd = {"bookmaker-wedtips": UNIBET, "datum-tijd-van-wedstrijd": "2026-11-14T13:00:00.000Z", **WEDTIPS}
        for pad in ("", "/live"):
            WF._req("PATCH", f"{WF.WF_API}/collections/{WF.NIEUWS_COLLECTION}/items/{it['id']}{pad}", {"fieldData": fd})
        print("velden gezet:", it["id"]); sys.exit()
    alles = G.check(sys.modules[__name__], 1000, 2300)
    p = 1
    for o in ODDS: p *= o
    assert f"{p:.2f}".replace(".", ",") == COMBI, p
    assert len(PROGRAMMA) == 16 and sorted(x[1] for x in PROGRAMMA) == sorted(G.ZA_MIDDAG + G.ZA_AVOND)
    assert [x[1] for x in PROGRAMMA] == G.ZA_MIDDAG + G.ZA_AVOND
    assert round(100 / 1.55) == 65
    print("dry run ok")
