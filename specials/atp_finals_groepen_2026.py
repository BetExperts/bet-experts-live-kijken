# -*- coding: utf-8 -*-
"""Los artikel: groepen Nitto ATP Finals 2026 (loting 12-11-2026): John McEnroe Group en Ivan Lendl Group.
Zoekwoorden: ATP Finals 2026 groepen, ATP Finals loting, ATP Finals schema, John McEnroe Group, Ivan Lendl Group.
Feiten: specials/atp_finals_groepen_2026_feiten.md (ATP-lotingsartikel 12-11, ATP draw/schedule-preview, nittoatpfinals.com
rules/prize money, ziggo.nl ATP Finals-pagina 2026, ATP-kwalificatieberichten, Tennis Majors, Sky Sport Italia, tennismylife
+ Wikipedia-H2H-matrix). Bewust vaag of weggelaten: order of play zondag (nog niet gepubliceerd), oorzaak opgave Fils (been of
rug), Cobolli dij/schouder, seizoensbalansen (tennismylife, kunnen afwijken), heupopmerking Tiafoe, Race-punten Alcaraz.
Odds: op 12-11 nog geen winnaarsmarkt bij de Kambi-bookmakers -> geen odds genoemd.
Slug 404 gecontroleerd op 12-11.
  python3 specials/atp_finals_groepen_2026.py        (dry run)
  publiceren: specials/concept_publiceer.py atp_finals_groepen_2026 --live ; daarna --velden"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "atp-finals-2026-groepen-loting-schema"
RUBRIEK = "665715dbf1f3cbdf7f874d79"   # Tennis
TITEL = "ATP Finals 2026 groepen: loting, schema en favorieten"
SAMENVATTING = ("De groepen van de ATP Finals 2026 zijn bekend: Zverev, Shelton, Fils en Jodar in de McEnroe-groep, "
                "Alcaraz, Medvedev, Cobolli en Tiafoe bij Lendl.")

MCENROE = [("1", "Alexander Zverev", "Duitsland", "1", "9e (kampioen 2018 en 2021)"),
           ("3", "Ben Shelton", "Verenigde Staten", "4", "2e"),
           ("6", "Arthur Fils", "Frankrijk", "7", "debuut"),
           ("8", "Rafael Jódar", "Spanje", "11", "debuut")]
LENDL = [("2", "Carlos Alcaraz", "Spanje", "3", "4e (finalist 2025)"),
         ("4", "Daniil Medvedev", "–", "5", "7e (kampioen 2020)"),
         ("5", "Flavio Cobolli", "Italië", "6", "debuut"),
         ("7", "Frances Tiafoe", "Verenigde Staten", "8", "debuut")]

L = {"race": '<a href="/nieuws/atp-finals-2026-gekwalificeerd-race-to-turin">wie zich plaatsten voor de ATP Finals 2026</a>',
     "djokovic": '<a href="/nieuws/djokovic-mist-atp-finals-2026-turijn">Djokovic mist de ATP Finals 2026</a>',
     "parijs": '<a href="/nieuws/finale-paris-masters-2026-wanneer-hoe-laat-tv">de Paris Masters</a>',
     "ziggo": '<a href="/zenders/ziggo-sport">Ziggo Sport</a>',
     "tips": '<a href="/tennis-voorspellingen-vandaag">tennis voorspellingen vandaag</a>',
     "duur": '<a href="/nieuws/hoe-lang-duurt-een-tenniswedstrijd">hoelang een tenniswedstrijd duurt</a>',
     "legaal": '<a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>'}


def groep(rijen):
    return tabel(["Plaats", "Speler", "Land", "Ranking", "Deelname"],
                 [(r[0], f"<strong>{r[1]}</strong>", r[2], r[3], r[4]) for r in rijen])


content = f"""<p><strong>De groepen van de ATP Finals 2026 zijn bekend. In de John McEnroe Group spelen Alexander Zverev (1), Ben Shelton (3), Arthur Fils (6) en Rafael Jódar (8). De Ivan Lendl Group bestaat uit Carlos Alcaraz (2), Daniil Medvedev (4), Flavio Cobolli (5) en Frances Tiafoe (7). Het toernooi wordt van zondag 15 tot en met zondag 22 november gespeeld in de Inalpi Arena in Turijn; de nummers 1 en 2 van elke groep gaan door naar de halve finales.</strong></p>
<p>De loting was donderdag 12 november in Turijn. Jannik Sinner doet niet mee: de tweevoudig titelverdediger beëindigde begin oktober zijn seizoen met een knieontsteking. Ook Novak Djokovic is er niet bij; lees daarover {L['djokovic']}. Daardoor staan er vier debutanten in het veld: Fils, Jódar, Cobolli en Tiafoe. Hoe de acht spelers zich plaatsten, lees je in {L['race']}.</p>
<h3><strong>Wie zitten er in de John McEnroe Group?</strong></h3>
{groep(MCENROE)}
<h3><strong>Wie zitten er in de Ivan Lendl Group?</strong></h3>
{groep(LENDL)}
<p><em>Ranking: ATP-ranglijst van 9 november 2026. Medvedev speelt onder neutrale vlag. Reserves zijn Alex de Minaur (eerste) en Taylor Fritz (tweede).</em></p>
<h3><strong>Hoe werkt de groepsfase van de ATP Finals?</strong></h3>
<p>Elke speler speelt drie groepswedstrijden, tegen de drie anderen uit zijn groep. Alle partijen, ook de finale, gaan over twee gewonnen sets. De nummers 1 en 2 van elke groep plaatsen zich voor de halve finales. Daar speelt de winnaar van de ene groep tegen de nummer 2 van de andere groep.</p>
<p>Staan twee spelers gelijk, dan telt eerst het aantal zeges, dan het aantal gespeelde wedstrijden (2-1 gaat voor 2-0, bijvoorbeeld als iemand moest opgeven) en daarna het onderlinge duel. Bij drie spelers met evenveel zeges beslist het percentage gewonnen sets, daarna het percentage gewonnen games en tot slot de ranking.</p>
<h3><strong>Wat is het speelschema van de ATP Finals 2026?</strong></h3>
{tabel(["Dag", "Ronde", "Enkelspel (Nederlandse tijd)"], [
    ("Zondag 15 t/m vrijdag 20 november", "Groepsfase", "14:00 uur en niet voor 20:30 uur"),
    ("Zaterdag 21 november", "Halve finales", "14:30 uur en niet voor 20:30 uur"),
    ("Zondag 22 november", "Finale", "18:00 uur"),
])}
<p>Elke dag staan er twee enkelspelen en twee dubbelspelen op het programma; de groepen wisselen elkaar meestal per dag af. Welke partijen zondag de spits afbijten, maakt de organisatie later bekend. Meestal opent de groep van het eerste reekshoofd, in dit geval die van Zverev. Turijn ligt in dezelfde tijdzone als Nederland.</p>
<h3><strong>Waar kijk je de ATP Finals 2026 live?</strong></h3>
<p>{L['ziggo']} zendt de ATP Finals uit, op Ziggo Sport 4 en op dagen met veel tennis ook op Ziggo Sport (kanaal 14, in het basispakket). Zondag 15 november is het toernooi te zien op Ziggo Sport 4, van 14:00 tot 16:00 uur en van 20:30 tot 22:30 uur. De finale van zondag 22 november staat van 18:00 tot 20:30 uur op Ziggo Sport 4.</p>"""

content2 = f"""<h3><strong>John McEnroe Group: kan Zverev zijn vorm terugvinden?</strong></h3>
<p><strong>Alexander Zverev</strong> beleeft het beste seizoen van zijn carrière. Hij won Roland Garros en het US Open, zijn eerste twee grandslamtitels, en is al zeker van de eerste plek op de wereldranglijst aan het eind van het jaar. In Turijn is hij een bekende: hij won de ATP Finals in 2018 en 2021 en staat op 18 zeges en 12 nederlagen. Zijn vorm van de laatste weken is wel matig. In Shanghai en Wenen verloor hij in de halve finale, en in Parijs ging hij in zijn eerste partij als nummer 1 onderuit tegen Lorenzo Musetti. "Ik was slecht, zo simpel is het", zei hij daarna.</p>
<p><strong>Ben Shelton</strong> is juist op tijd in vorm. De linkshandige Amerikaan won dit jaar vier titels, waaronder de Masters van Montreal, en haalde vorige week de finale van {L['parijs']}, die hij in twee sets verloor van Alcaraz. Na het US Open voelde hij zich naar eigen zeggen "helemaal op", maar Parijs was de eerste week waarin hij zich weer volledig fit voelde. Vorig jaar verloor hij in Turijn al zijn drie groepswedstrijden. Tegen Zverev staat hij 0-6: hij verloor ook de US Open-finale van dit jaar en hun groepsduel in Turijn van 2025.</p>
<p><strong>Arthur Fils</strong> (22) is de eerste Fransman op de ATP Finals sinds Gaël Monfils in 2016. Hij won dit jaar de Masters van Cincinnati en het toernooi van Barcelona. Zijn lichaam is wel een aandachtspunt: eind oktober gaf hij in Basel op tegen Taylor Fritz met pijn in zijn been, en hij heeft een geschiedenis met rugklachten. In Parijs speelde hij daarna wel weer twee partijen.</p>
<p><strong>Rafael Jódar</strong> (20) is het verhaal van het jaar. Eind 2025 studeerde hij nog in de Verenigde Staten en stond hij buiten de top 150. Dit seizoen won hij in Marrakech, haalde hij de finale van de Masters van Shanghai en versloeg hij onder anderen Medvedev. Hij plaatste zich op de valreep, als nummer 11 van de wereld. Tegen Fils staat hij 2-1, met twee zeges op hardcourt dit jaar. Tegen Shelton speelde hij nog nooit.</p>
<p><strong>Onderlinge duels in de McEnroe-groep</strong></p>
{tabel(["Duel", "Stand", "Laatste ontmoeting"], [
    ("Zverev – Shelton", "6-0", "US Open 2026, finale: Zverev wint in vier sets"),
    ("Zverev – Fils", "5-2", "Indian Wells 2026: Zverev 6-2, 6-3"),
    ("Zverev – Jódar", "1-0", "Roland Garros 2026: Zverev in drie sets"),
    ("Shelton – Fils", "2-1", "Basel 2024 (indoor): Shelton 6-3, 7-6"),
    ("Shelton – Jódar", "0-0", "Nooit tegen elkaar gespeeld"),
    ("Fils – Jódar", "1-2", "Montreal 2026: Jódar 7-6, 6-3"),
])}
<p><strong>Onze verwachting:</strong> Zverev heeft het beste papier, maar Shelton heeft de betere vorm. Omdat Zverev al zes keer van Shelton won, zien we hen samen doorgaan, met Zverev als groepswinnaar. Jódar is de outsider die alles kan omgooien; Fils moet laten zien dat zijn lichaam drie zware wedstrijden aankan.</p>
<h3><strong>Ivan Lendl Group: Alcaraz als grote favoriet</strong></h3>
<p><strong>Carlos Alcaraz</strong> is de speler in vorm. Hij won dertien partijen op rij en de titels in Tokio, Wenen en Parijs. Dat is opvallend, want eerder dit jaar stond hij ruim vier maanden aan de kant met een polsblessure, waardoor hij Roland Garros en Wimbledon miste. In januari won hij wel de Australian Open. De ATP Finals won hij nog nooit: vorig jaar verloor hij de finale van Sinner. Zonder Sinner in het veld is hij nu de logische favoriet.</p>
<p><strong>Daniil Medvedev</strong> won de ATP Finals in 2020 en speelt zijn zevende editie. Hij won dit jaar vier titels, de laatste in Almaty, maar verloor in Parijs meteen in zijn eerste partij. Twee weken geleden verloor hij in de halve finale van Wenen van Alcaraz (6-4, 7-6). In maart versloeg hij Alcaraz nog in Indian Wells.</p>
<p><strong>Flavio Cobolli</strong> is de thuisspeler en het grootste vraagteken. De Italiaan haalde dit jaar de finale van Roland Garros, maar sinds het US Open won hij maar drie van zijn negen partijen. In Wenen gaf hij op met een lichte spierblessure aan zijn dijbeen, en voor Parijs meldde hij zich af. Een nieuwe medische update is er niet; wel trainde hij afgelopen zondag al in Turijn.</p>
<p><strong>Frances Tiafoe</strong> bereikte dit jaar de hoogste ranking uit zijn carrière (nummer 8) en de halve finale van het US Open. Daar versloeg hij onder anderen Medvedev. Zijn najaar was wel zwak: hij verloor zijn laatste drie partijen. Tegen Cobolli staat hij 4-1.</p>
<p><strong>Onderlinge duels in de Lendl-groep</strong></p>
{tabel(["Duel", "Stand", "Laatste ontmoeting"], [
    ("Alcaraz – Medvedev", "7-3", "Wenen 2026 (indoor): Alcaraz 6-4, 7-6"),
    ("Alcaraz – Cobolli", "1-0", "Roland Garros 2023: Alcaraz in drie sets"),
    ("Alcaraz – Tiafoe", "2-1", "Wimbledon 2024: Alcaraz in vijf sets"),
    ("Medvedev – Cobolli", "2-1", "Madrid 2026: Cobolli in drie sets"),
    ("Medvedev – Tiafoe", "6-2", "US Open 2026: Tiafoe in drie sets"),
    ("Cobolli – Tiafoe", "1-4", "Halle 2026: Tiafoe 6-2, 7-6"),
])}
<p><strong>Onze verwachting:</strong> Alcaraz wint de groep. Voor de tweede plek is Medvedev de favoriet, met zijn ervaring en een 6-2 tegen Tiafoe. Maar Tiafoe won hun laatste duel, en een fitte Cobolli met het publiek achter zich kan in Turijn verrassen.</p>"""

content3 = f"""<h3><strong>Wat verdienen de spelers op de ATP Finals 2026?</strong></h3>
<p>Er is in totaal 15,75 miljoen dollar aan prijzengeld te verdelen. Een ongeslagen kampioen, met drie groepszeges, een gewonnen halve finale en een gewonnen finale, verdient 5.171.000 dollar en 1.500 rankingpunten.</p>
{tabel(["Onderdeel", "Prijzengeld", "Rankingpunten"], [
    ("Deelname (drie groepswedstrijden)", "$338.000", "–"),
    ("Per gewonnen groepswedstrijd", "$405.000", "200"),
    ("Gewonnen halve finale", "$1.206.000", "400"),
    ("Gewonnen finale", "$2.412.000", "500"),
    ("<strong>Ongeslagen kampioen</strong>", "<strong>$5.171.000</strong>", "<strong>1.500</strong>"),
])}
<h3><strong>Wie wint de ATP Finals 2026?</strong></h3>
<p>Alcaraz is in onze ogen de favoriet: hij is in topvorm, zijn grote rivaal Sinner ontbreekt en hij kent Turijn na de finale van vorig jaar. Zverev is de logische tweede kandidaat, al moet hij zijn vorm van eerder dit seizoen terugvinden. Shelton is de gevaarlijkste outsider na zijn finale in Parijs. Bookmakers hadden op donderdag 12 november nog geen odds op de toernooiwinnaar online; zodra de markt opengaat, vind je onze dagelijkse tips op {L['tips']}.</p>
<p>Wedden op tennis? Een groepswedstrijd gaat over maximaal drie sets; lees ook {L['duur']}. Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit; lees {L['legaal']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wie zitten er in de groepen van de ATP Finals 2026?</strong><br>John McEnroe Group: Zverev, Shelton, Fils en Jódar. Ivan Lendl Group: Alcaraz, Medvedev, Cobolli en Tiafoe.</p>
<p><strong>Wanneer zijn de ATP Finals 2026?</strong><br>Van zondag 15 tot en met zondag 22 november 2026, in de Inalpi Arena in Turijn. De finale begint op zondag 22 november om 18:00 uur.</p>
<p><strong>Hoeveel spelers gaan door uit elke groep?</strong><br>Twee. De groepswinnaar speelt in de halve finale tegen de nummer 2 van de andere groep.</p>
<p><strong>Waarom doet Jannik Sinner niet mee?</strong><br>Sinner beëindigde begin oktober zijn seizoen met een knieontsteking. Alex de Minaur en Taylor Fritz zijn de reserves.</p>
<p><strong>Hoe laat beginnen de wedstrijden?</strong><br>In de groepsfase om 14:00 uur en niet voor 20:30 uur. De halve finales zijn op zaterdag 21 november om 14:30 uur en niet voor 20:30 uur.</p>
<p><strong>Waar zijn de ATP Finals op tv?</strong><br>Op Ziggo Sport 4 en Ziggo Sport. Zondag 15 november zendt Ziggo Sport 4 uit van 14:00 tot 16:00 uur en van 20:30 tot 22:30 uur.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    if "--velden" in sys.argv:
        import lk_webflow as WF
        it = WF._req("GET", f"{WF.WF_API}/collections/{WF.NIEUWS_COLLECTION}/items?slug={SLUG}")["items"][0]
        for pad in ("", "/live"):
            WF._req("PATCH", f"{WF.WF_API}/collections/{WF.NIEUWS_COLLECTION}/items/{it['id']}{pad}", {"fieldData": {"tennis": True}})
        print("velden gezet:", it["id"]); sys.exit()
    alles = content + content2 + content3
    w = len(re.sub(r"<[^>]+>", " ", alles).split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", w, "woorden")
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert 405000 * 3 + 1206000 + 2412000 + 338000 == 5171000
    assert 200 * 3 + 400 + 500 == 1500
    assert "<h2" not in alles and "<h4" not in alles and "betcity" not in alles.lower() and "/go/" not in alles
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    print("dry run ok")
