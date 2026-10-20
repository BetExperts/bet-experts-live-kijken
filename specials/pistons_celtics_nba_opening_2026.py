# -*- coding: utf-8 -*-
"""Los artikel: Pistons – Celtics voorspelling, NBA-opener 20 oktober 2026 (21:00 NL). Feiten nagelopen op 20-10-2026
(NBA.com, ESPN, Covers, Wikipedia, team- en oddspagina's); Nederlandse odds uit onze feed (TOTO, Circus).
  python3 specials/pistons_celtics_nba_opening_2026.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Pistons – Celtics voorspelling: wedtips en odds voor de NBA-opener (20 oktober)"
SLUG = "pistons-celtics-voorspelling-wedtips-nba-opening-2026"
SAMENVATTING = ("Pistons – Celtics opent om 21:00 het NBA-seizoen. Voorspelling, wedtips, odds, blessures en "
                "opstellingen van de topper in Detroit.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


def lijst(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


content = f"""<p><strong>Het NBA-seizoen 2026/27 begint vanavond om 21:00 Nederlandse tijd in Detroit, met de topper Detroit Pistons – Boston Celtics. De nummers één en twee van het Oosten van vorig seizoen staan direct tegenover elkaar. Onze voorspelling: Detroit wint met 109-104. De hoofdtip is een thuiszege van de Pistons rond odds 2,00, met de Under als waardetip.</strong></p>
<p>Opening night valt dit jaar op een ongewone tijd. Omdat de NBA de avond opent met een tripleheader op de Amerikaanse zender NBC, begint deze wedstrijd in Detroit al om 15:00 lokale tijd. Voor Nederlandse basketbalfans en wedders is dat ideaal: geen nachtwerk, maar gewoon een wedstrijd na het avondeten. Hieronder lees je wat er veranderd is bij beide ploegen, wie er speelt, wat de bookmakers verwachten en welke weddenschappen wij interessant vinden.</p>
<h3><strong>Detroit Pistons – Boston Celtics: aftrap en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "Detroit Pistons – Boston Celtics"),
    ("Datum", "Dinsdag 20 oktober 2026"),
    ("Aanvang", "21:00 Nederlandse tijd (15:00 in Detroit)"),
    ("Arena", "Little Caesars Arena, Detroit"),
    ("Competitie", "NBA, reguliere competitie 2026/27 (openingswedstrijd)"),
    ("Onderlinge duels 2025/26", "3-1 voor Detroit"),
])}
<p>Let op de volgorde: Detroit is de thuisploeg. Boston speelt zijn eerste thuiswedstrijd pas op vrijdag 23 oktober, tegen de New York Knicks.</p>
<h3><strong>Vorig seizoen: Detroit de beste van het Oosten, Boston onderuit in de playoffs</strong></h3>
<p>Detroit maakte in 2025/26 de grootste sprong van de competitie af. De Pistons wonnen 60 van de 82 wedstrijden en werden eerste in de Eastern Conference, met een indrukwekkend thuisrecord van 32-9. In de playoffs kwam de ploeg van coach J.B. Bickerstaff tegen Orlando terug van een 1-3 achterstand, de eerste gewonnen serie sinds 2008. In de tweede ronde was Cleveland na zeven wedstrijden te sterk.</p>
<p>Boston eindigde als nummer twee (56-26), maar het seizoen eindigde in een kater. Tegen Philadelphia gaven de Celtics in de eerste ronde een 3-1 voorsprong weg, voor het eerst in de clubgeschiedenis, en in Game 7 ontbrak Jayson Tatum met een knieblessure.</p>
{tabel(["2025/26", "Detroit Pistons", "Boston Celtics"], [
    ("Eindstand", "60-22 (nr. 1 Oost)", "56-26 (nr. 2 Oost)"),
    ("Punten voor / tegen", "117,8 / 109,6", "114,9 / 107,2"),
    ("Aanvallende rating", "117,3", "120,0"),
    ("Verdedigende rating", "108,9 (2e van de NBA)", "111,7 (4e)"),
    ("Tempo", "99,9 balbezittingen", "95,6 (traagste van de NBA)"),
    ("Tegen de handicap (ATS)", "44-38", "49-33"),
])}
<p><em>Ratings en tempo zijn per 100 balbezittingen; bron: geavanceerde teamstatistieken van seizoen 2025/26.</em></p>"""

content2 = f"""<h3><strong>Zo zijn beide selecties veranderd</strong></h3>
<p><strong>Boston Celtics</strong></p>
<p>De grootste transfer van de zomer was een Celtics-zaak. Boston ruilde Jaylen Brown, de MVP van de Finals in 2024 en vorig seizoen goed voor 28,7 punten per wedstrijd, naar Philadelphia. In ruil kwamen Paul George en een flink pakket draftpicks, waaronder een onbeschermde eerste ronde van de Sixers in 2031. Daarnaast haalde president Brad Stevens rebounder Mitchell Robinson van de Knicks en routinier Mike Conley. Nikola Vučević vertrok naar Orlando.</p>
<p>Het belangrijkste nieuws is Jayson Tatum. Zeventien maanden na zijn gescheurde achillespees begint hij voor het eerst sinds 2025 een seizoen fit. Vorig seizoen speelde hij pas laat mee (16 wedstrijden, 21,8 punten en 10,0 rebounds) en in geen van de vier duels met Detroit. Zonder Brown is hij nu meer dan ooit de eerste optie.</p>
<p><strong>Detroit Pistons</strong></p>
<p>Detroit bouwde verder op de basis die vorig seizoen werkte. John Collins (sign-and-trade met de Clippers) moet de vertrokken Tobias Harris vervangen, en schutter Isaiah Joe komt over van Oklahoma City. Isaiah Stewart, Caris LeVert en Marcus Sasser vertrokken. Belangrijk detail: center Jalen Duren tekende pas begin oktober een nieuw contract (vijf jaar, 200 miljoen dollar) en miste daardoor het begin van het trainingskamp.</p>
<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("Devin Carter", "Boston", "Speelt niet (ziek)"),
    ("Taurean Prince", "Detroit", "Twijfelachtig (persoonlijke redenen)"),
    ("Jayson Tatum", "Boston", "Speelt naar verwachting"),
    ("Paul George, Derrick White, Payton Pritchard, Mitchell Robinson", "Boston", "Rustten in de laatste oefenwedstrijd, inzetbaar"),
])}
<p><strong>Verwachte basisvijf Detroit:</strong> Cade Cunningham, Duncan Robinson, Ausar Thompson, John Collins, Jalen Duren.</p>
<p><strong>Verwachte basisvijf Boston:</strong> Derrick White, Jordan Walsh, Paul George, Jayson Tatum, Mitchell Robinson. Coach Joe Mazzulla wisselt vaak (vorig seizoen 23 verschillende basisvijven), dus Payton Pritchard of Neemias Queta in de basis is ook goed mogelijk.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "Bijzonderheid"], [
    ("Cade Cunningham (DET)", "23,9", "5,5", "9,9", "Spelverdeler en leider van de Pistons"),
    ("Jalen Duren (DET)", "19,5", "10,5", "2,0", "65% van zijn schoten raak"),
    ("Ausar Thompson (DET)", "9,9", "5,7", "3,1", "2,0 steals, topverdediger"),
    ("Jayson Tatum (BOS)", "21,8", "10,0", "5,3", "16 wedstrijden na zijn blessure"),
    ("Payton Pritchard (BOS)", "17,0", "3,9", "5,2", "Sterkste schutter van de bank"),
    ("Paul George (BOS, vorig seizoen PHI)", "17,3", "5,3", "3,6", "Nieuwe tweede ster naast Tatum"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26.</em></p>
<h3><strong>Odds Pistons – Celtics bij Nederlandse bookmakers</strong></h3>
<p>De bookmakers zien een bijna gelijkopgaande wedstrijd. Opvallend is de beweging in de markt: deze zomer was Detroit nog favoriet met 2,5 punten verschil, inmiddels geldt Boston als lichte favoriet. Ook het verwachte puntentotaal is gezakt, van ruim 224 naar rond de 220 punten.</p>
{tabel(["Markt", "Bookmaker", "Pistons", "Celtics"], [
    ("Winnaar (incl. verlenging)", "<a href=\"/bookmakers/circus\">Circus</a>", "1,99", "1,86"),
    ("1X2 (reguliere speeltijd, gelijk 16,0)", "<a href=\"/bookmakers/toto\">TOTO</a>", "2,00", "1,87"),
    ("Handicap +6,5 / -6,5 (incl. verlenging)", "Circus", "1,43", "2,60"),
])}
<p>Bij Circus is ook gespeeld op het totaal van 216,5 punten: Over 1,53, Under 2,35. Odds kunnen tot de aftrap nog veranderen; vergelijk ze vlak voor de start nog even.</p>"""

content3 = f"""<h3><strong>Onze voorspelling: Detroit wint een taaie opener</strong></h3>
<p>De markt is de afgelopen weken flink naar Boston gedraaid, vooral omdat Tatum weer fit is. Wij vinden die beweging te groot. Detroit was vorig seizoen thuis een van de sterkste ploegen van de competitie (32-9), won drie van de vier onderlinge duels en heeft zijn kern bij elkaar gehouden. Boston daarentegen begint met een flink veranderde ploeg: zonder Brown, met George en Robinson als nieuwkomers en met een sterspeler die net terug is van een zware blessure. In de eerste wedstrijd van een seizoen wint de ingespeelde ploeg vaker dan de ploeg die nog moet wennen.</p>
<p>Daarbij verwachten we geen schutterswedstrijd. Boston speelde vorig seizoen het laagste tempo van de NBA en kreeg de minste punten tegen, Detroit had de op één na beste verdediging. Op opening night zijn de rotaties nog niet geslepen en is het ritme vaak zoek. Onze voorspelling: <strong>Detroit Pistons – Boston Celtics 109-104</strong>.</p>
<h3><strong>Wedtips voor Pistons – Celtics</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Inzet"], [
    ("Detroit Pistons wint (incl. verlenging)", "1,99", "Circus", "Hoofdtip"),
    ("Minder dan 216,5 punten (incl. verlenging)", "2,35", "Circus", "Waardetip, hoger risico"),
    ("Detroit Pistons +6,5 punten", "1,43", "Circus", "Veilige basis voor een combinatie"),
])}
<p><strong>1. Detroit Pistons wint (1,99).</strong> Thuisvoordeel, een ingespeelde selectie en een sterke onderlinge reeks. Volgens het voorspellingsmodel van ESPN heeft Detroit iets meer dan 52% kans; bij odds rond 2,00 rekent de bookmaker met 50%. Wie bij TOTO speelt: daar gaat de 1X2-markt alleen over de reguliere speeltijd (gelijkspel 16,0), dus bij een verlenging verlies je je inzet.</p>
<p><strong>2. Minder dan 216,5 punten (2,35).</strong> Dit is de tip met het meeste risico, maar ook de meeste waarde. Het hoofdtotaal in de markt ligt rond 220,5 punten; deze lijn ligt vier punten lager en levert daardoor ruim twee keer de inzet op. Het tempo van Boston, de verdediging van Detroit en de onwennigheid van opening night pleiten voor een lage score. Van de vier onderlinge duels vorig seizoen bleven er twee onder de 220 punten.</p>
<p><strong>3. Detroit +6,5 (1,43).</strong> Detroit hoeft niet te winnen; verliezen met maximaal zes punten is ook goed. Een lage quotering, maar handig om een combinatieweddenschap mee op te bouwen.</p>
<p><a href="https://www.bet365.nl/hub/nl-nl/open-account?affiliate=365_02599619"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op Pistons – Celtics</strong></a></p>
<p>Speel je liever op een speler: Tatum pakte vorig seizoen 10 rebounds per wedstrijd en krijgt zonder Brown meer bal. Covers ziet in zijn reboundlijn van 8,5 een kans op de Over.</p>
<h3><strong>Pistons – Celtics live kijken in Nederland</strong></h3>
<p>De makkelijkste manier om de NBA-opener te zien: bij <a href="/bookmakers/bet365">Bet365</a> kijk je NBA-wedstrijden gratis live met een account. In de Verenigde Staten zendt NBC de wedstrijd uit; in Nederland heeft ESPN de NBA-rechten, maar niet elke wedstrijd staat op een van de ESPN-kanalen. Met <strong>NBA League Pass</strong>, de betaalde streamingdienst van de competitie, kun je ook alle wedstrijden volgen.</p>
<p><a href="https://www.bet365.nl/hub/nl-nl/open-account?affiliate=365_02599619"><strong>👉 Klik hier: maak je Bet365-account aan en kijk Pistons – Celtics live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Wil je weten welke landgenoten dit seizoen in de NBA spelen? Lees ons overzicht <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">Welke Nederlanders spelen in de NBA</a>. Alle basketbaltips vind je op onze pagina <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Pistons – Celtics?</strong><br>Dinsdag 20 oktober 2026 om 21:00 Nederlandse tijd (15:00 in Detroit). Het is de allereerste wedstrijd van het NBA-seizoen 2026/27.</p>
<p><strong>Waar wordt Pistons – Celtics gespeeld?</strong><br>In de Little Caesars Arena in Detroit. De Pistons zijn de thuisploeg.</p>
<p><strong>Wie is favoriet: Pistons of Celtics?</strong><br>Boston is bij de bookmakers een lichte favoriet (rond 1,86), Detroit staat rond 2,00. In de zomer was dat nog andersom.</p>
<p><strong>Speelt Jayson Tatum mee?</strong><br>Naar verwachting wel. Hij is zeventien maanden na zijn achillespeesblessure weer fit en begint het seizoen zonder bekende beperking in speeltijd.</p>
<p><strong>Waarom speelt Jaylen Brown niet meer voor Boston?</strong><br>Boston ruilde Brown deze zomer met Philadelphia voor Paul George en meerdere draftpicks.</p>
<p><strong>Wat is onze voorspelling voor Pistons – Celtics?</strong><br>Detroit wint met 109-104. Onze hoofdtip is een zege van de Pistons inclusief verlenging (1,99 bij Circus).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_BASKETBAL, "competitie": COMPETITIE_NBA,
          "datum-tijd-van-wedstrijd": "2026-10-20T19:00:00.000Z",
          "wedtip-1-2": "Detroit Pistons wint (incl. verlenging)", "quotering-wedtip-1": "1.99",
          "wedtip-2-2": "Minder dan 216.5 punten (incl. verlenging)", "quotering-wedtip-2": "2.35",
          "wedtip-3-2": "Detroit Pistons +6.5 punten", "quotering-wedtip-3": "1.43",
          "bookmaker-wedtips": "64ff0fbd5a8f205b05d54670",
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        import re
        tekst = re.sub(r"<[^>]+>", " ", content + content2 + content3)
        print(len(SAMENVATTING), "tekens samenvatting |", len(tekst.split()), "woorden"); sys.exit()
    print("item:", WF.create_live(fd))
