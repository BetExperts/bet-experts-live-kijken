# -*- coding: utf-8 -*-
"""Los artikel: Spurs – Thunder voorspelling, NBA-opener 21 oktober 2026 (03:30 NL). Feiten nagelopen op 20-10-2026
(NBA.com, ESPN, Covers, FanDuel Research, StatMuse, Wikipedia); Nederlandse odds uit onze feed (TOTO, Circus).
  python3 specials/spurs_thunder_nba_opening_2026.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Spurs – Thunder voorspelling: wedtips en odds voor de NBA-topper (21 oktober, 03:30)"
SLUG = "spurs-thunder-voorspelling-wedtips-nba-opening-2026"
SAMENVATTING = ("Spurs – Thunder is de reprise van de West-finale. Voorspelling, wedtips, odds, blessures en "
                "opstellingen voor de NBA-topper om 03:30.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet365.nl/hub/nl-nl/open-account?affiliate=365_02599619"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>In de nacht van dinsdag op woensdag om 03:30 Nederlandse tijd staat de grootste affiche van de NBA-openingsavond op het programma: San Antonio Spurs – Oklahoma City Thunder, de herhaling van de West-finale van vorig seizoen. Onze voorspelling: de Spurs winnen met 114-108. Hoofdtip: een thuiszege van San Antonio, met de Under als sterke tweede tip.</strong></p>
<p>Vijf maanden geleden won San Antonio in een zenuwslopende zevende wedstrijd in Oklahoma City de finale van het Westen. Nu beginnen beide ploegen het nieuwe seizoen tegen elkaar, als de twee grote favorieten voor de titel. Hieronder lees je hoe de selecties veranderd zijn, wie er speelt, wat de bookmakers verwachten en welke weddenschappen wij interessant vinden.</p>
<h3><strong>Spurs – Thunder: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "San Antonio Spurs – Oklahoma City Thunder"),
    ("Datum", "Woensdag 21 oktober 2026 (nacht van dinsdag op woensdag)"),
    ("Aanvang", "03:30 Nederlandse tijd (20:30 in San Antonio)"),
    ("Arena", "Frost Bank Center, San Antonio"),
    ("Competitie", "NBA, reguliere competitie 2026/27 (openingsavond)"),
    ("Onderlinge duels 2025/26", "8-4 voor San Antonio (inclusief play-offs)"),
])}
<p>De Spurs zijn de thuisploeg. Het is de afsluiter van de openingsavond, na <a href="/nieuws/pistons-celtics-voorspelling-wedtips-nba-opening-2026">Pistons – Celtics</a> (21:00) en 76ers – Knicks (01:00).</p>
<h3><strong>Vorig seizoen: de twee beste teams van het Westen</strong></h3>
<p>Oklahoma City had in 2025/26 het beste record van de hele NBA (64-18) en de beste verdediging van de competitie. Shai Gilgeous-Alexander werd voor de tweede keer op rij verkozen tot MVP. In de play-offs veegde de Thunder eerst Phoenix en daarna de Lakers met 4-0 van de baan, maar in de finale van het Westen was San Antonio na zeven wedstrijden te sterk.</p>
<p>De Spurs eindigden met 62-20 als tweede en maakten de grootste sprong van de competitie. Victor Wembanyama werd unaniem verkozen tot beste verdediger van de NBA, en De'Aaron Fox en Wembanyama speelden de All-Star Game. In de NBA Finals was New York met 4-1 te sterk, maar de eerste finale in twaalf jaar betekende wel de terugkeer van San Antonio aan de top.</p>
{tabel(["2025/26", "San Antonio Spurs", "Oklahoma City Thunder"], [
    ("Eindstand", "62-20 (nr. 2 West)", "64-18 (nr. 1 West)"),
    ("Thuis / uit", "32-8 / 30-12", "34-8 / 30-10"),
    ("Punten voor / tegen", "119,8 / 111,5", "119,0 / 107,9"),
    ("Aanvallende rating", "118,7 (3e)", "117,6 (7e)"),
    ("Verdedigende rating", "110,4 (3e)", "106,5 (1e)"),
    ("Over in de reguliere competitie", "36 van 82", "45 van 82"),
    ("Play-offs", "Finale verloren van New York (1-4)", "West-finale verloren van San Antonio (3-4)"),
])}
<p><em>Ratings per 100 balbezittingen (NBA.com).</em></p>"""

content2 = f"""<h3><strong>Zo zijn beide selecties veranderd</strong></h3>
<p><strong>San Antonio Spurs</strong></p>
<p>San Antonio koos voor continuïteit: 94 procent van de speelminuten van vorig seizoen staat nog onder contract, het hoogste percentage van de competitie. De enige grote nieuwkomer is Tobias Harris, die over kwam van Detroit maar met een kuitblessure de opener mist. Harrison Barnes en Jordan McLaughlin tekenden bij, en in de draft koos de club Jayden Quaintance (nummer 20), die met een knieblessure nog maanden uitvalt.</p>
<p><strong>Oklahoma City Thunder</strong></p>
<p>Bij de Thunder is meer veranderd. Lu Dort, Isaiah Joe en Aaron Wiggins vertrokken; volgens NBA.com waren dat over de afgelopen twee seizoenen de nummers twee, vijf en zes in speelminuten. Daar staat een fitte Jalen Williams tegenover, die in de West-finale maar één van de zeven wedstrijden kon spelen. Verder kwamen draftkeuzes Aday Mara (nummer 12) en Bennett Stirtz (nummer 16) erbij, en speelt Jared McCain zijn eerste volledige seizoen voor de club.</p>
<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("Tobias Harris", "San Antonio", "Speelt niet (kuit)"),
    ("Jayden Quaintance", "San Antonio", "Speelt niet (knie)"),
    ("Thomas Sorber", "Oklahoma City", "Speelt niet (knie)"),
    ("Nikola Topić", "Oklahoma City", "Speelt niet (rug)"),
    ("Otega Oweh", "Oklahoma City", "Rest van het seizoen uitgeschakeld (achillespees)"),
])}
<p>De sterren staan niet op het blessurerapport: Gilgeous-Alexander, Jalen Williams, Holmgren, Wembanyama, Fox, Castle en Harper zijn allemaal inzetbaar.</p>
<p><strong>Verwachte basisvijf San Antonio:</strong> De'Aaron Fox, Stephon Castle, Dylan Harper, Devin Vassell, Victor Wembanyama. Coach Mitch Johnson koos in de laatste serieuze oefenwedstrijd voor deze vijf met drie guards; Julian Champagnie is het alternatief.</p>
<p><strong>Verwachte basisvijf Oklahoma City:</strong> Shai Gilgeous-Alexander, Cason Wallace, Jalen Williams, Chet Holmgren, Isaiah Hartenstein.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "Bijzonderheid"], [
    ("Victor Wembanyama (SAS)", "25,0", "11,5", "3,1", "3,1 blocks, beste verdediger van de NBA"),
    ("De'Aaron Fox (SAS)", "18,6", "3,8", "6,2", "Spelverdeler, All-Star"),
    ("Stephon Castle (SAS)", "16,7", "5,3", "7,4", "18,0 punten in de West-finale"),
    ("Shai Gilgeous-Alexander (OKC)", "31,1", "4,3", "6,6", "Tweevoudig MVP"),
    ("Chet Holmgren (OKC)", "17,1", "8,9", "1,7", "1,9 blocks"),
    ("Jalen Williams (OKC)", "17,1", "4,6", "5,5", "Terug na een blessureseizoen"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26.</em></p>
<p>Let op de onderlinge cijfers: in de West-finale hield San Antonio Gilgeous-Alexander op 25,9 punten per wedstrijd met maar 40,9 procent van zijn schoten raak, terwijl Wembanyama 27,3 punten, 10,9 rebounds en 2,7 blocks per duel noteerde.</p>
<h3><strong>Odds Spurs – Thunder bij Nederlandse bookmakers</strong></h3>
<p>De bookmakers zien een bijna gelijkopgaande wedstrijd met San Antonio als lichte favoriet. In de dagen voor de wedstrijd kwam er geld op Oklahoma City: in de Amerikaanse markt zakte de Spurs-favorietenrol van 3 naar 1,5 punt. Het verwachte puntentotaal ligt rond de 231 tot 233 punten.</p>
{tabel(["Markt", "Bookmaker", "Spurs", "Thunder"], [
    ("Winnaar (incl. verlenging)", "<a href=\"/bookmakers/circus\">Circus</a>", "1,86", "1,99"),
    ("1X2 (reguliere speeltijd, gelijk 16,0)", "<a href=\"/bookmakers/toto\">TOTO</a>", "1,87", "2,00"),
    ("Handicap +4,5 / -4,5 (incl. verlenging)", "Circus", "1,48", "2,45"),
])}
<p>Bij Circus kun je ook spelen op het totaal van 237,5 punten: Over 2,35, Under 1,53. Odds kunnen tot de aftrap nog veranderen; vergelijk ze vlak voor de start nog even.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op Spurs – Thunder</strong></a></p>"""

content3 = f"""<h3><strong>Onze voorspelling: San Antonio wint opnieuw</strong></h3>
<p>Wij zien San Antonio als terechte favoriet. De Spurs wonnen acht van de twaalf duels met de Thunder vorig seizoen, dekten in die wedstrijden ook acht keer de handicap en hebben hun kern volledig bij elkaar gehouden. Oklahoma City moet drie belangrijke rotatiespelers vervangen, en juist in een eerste wedstrijd van het seizoen telt een ingespeelde ploeg zwaar. De terugkeer van Jalen Williams maakt de Thunder wel gevaarlijker dan in mei, dus we verwachten geen walk-over.</p>
<p>We verwachten ook geen schutterswedstrijd. Beide ploegen hadden vorig seizoen een top-3-verdediging, San Antonio ging in de reguliere competitie maar 36 van de 82 keer over de lijn en de twaalf onderlinge duels kwamen gemiddeld uit op 222,5 punten. Onze voorspelling: <strong>San Antonio Spurs – Oklahoma City Thunder 114-108</strong>.</p>
<h3><strong>Wedtips voor Spurs – Thunder</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Inzet"], [
    ("San Antonio Spurs wint (incl. verlenging)", "1,86", "Circus", "Hoofdtip"),
    ("Minder dan 237,5 punten (incl. verlenging)", "1,53", "Circus", "Sterke tweede tip"),
    ("San Antonio Spurs +4,5 punten", "1,48", "Circus", "Veilige basis voor een combinatie"),
])}
<p><strong>1. San Antonio wint (1,86).</strong> Thuisvoordeel, de onderlinge reeks van 8-4 en de continuïteit in de selectie. Volgens het voorspellingsmodel van ESPN heeft San Antonio 52,6 procent kans; de onafhankelijke rekenmodellen van Dimers komen zelfs op 56 procent. Speel je bij TOTO, let dan op: daar gaat de 1X2-markt alleen over de reguliere speeltijd (gelijkspel 16,0).</p>
<p><strong>2. Minder dan 237,5 punten (1,53).</strong> Van de twaalf onderlinge duels vorig seizoen bleven er tien onder de 237,5 punten. Met twee topverdedigingen en een ploeg die nog moet wennen aan nieuwe rotaties is dit voor ons de meest betrouwbare tip. Durf je meer risico, dan biedt de hoofdlijn rond 231,5 punten een hogere quotering.</p>
<p><strong>3. San Antonio +4,5 (1,48).</strong> De Spurs mogen met maximaal vier punten verliezen. Een lage quotering, maar een stevige basis om een combinatieweddenschap mee op te bouwen.</p>
<p>Speel je liever op een speler: Gilgeous-Alexander scoorde vorig seizoen 31,1 punten per wedstrijd, maar kwam in de West-finale tegen deze verdediging gemiddeld niet verder dan 25,9. Een lijn rond 30,5 punten vinden wij voor de Under interessanter dan voor de Over.</p>
<h3><strong>Spurs – Thunder live kijken in Nederland</strong></h3>
<p>De makkelijkste manier om de wedstrijd te zien: bij <a href="/bookmakers/bet365">Bet365</a> kijk je NBA-wedstrijden gratis live. Je hebt alleen een account met een kleine storting nodig, en die storting kun je daarna gewoon weer opnemen. In de Verenigde Staten zendt NBC de wedstrijd uit; in Nederland heeft ESPN de NBA-rechten, maar niet elke wedstrijd staat op een van de ESPN-kanalen. Met <strong>NBA League Pass</strong>, de betaalde streamingdienst van de competitie, kun je ook alle wedstrijden volgen.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk Spurs – Thunder live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Lees ook onze voorspelling voor de opener <a href="/nieuws/pistons-celtics-voorspelling-wedtips-nba-opening-2026">Pistons – Celtics</a> en ons overzicht <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">Welke Nederlanders spelen in de NBA</a>. Alle basketbaltips vind je op onze pagina <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Spurs – Thunder?</strong><br>Woensdag 21 oktober 2026 om 03:30 Nederlandse tijd, in de nacht van dinsdag op woensdag. In San Antonio is het dan dinsdagavond 20:30.</p>
<p><strong>Waar wordt Spurs – Thunder gespeeld?</strong><br>In het Frost Bank Center in San Antonio. De Spurs zijn de thuisploeg.</p>
<p><strong>Wie is favoriet: Spurs of Thunder?</strong><br>San Antonio is bij de bookmakers een lichte favoriet (rond 1,86), Oklahoma City staat rond 2,00.</p>
<p><strong>Wie won de West-finale van vorig seizoen?</strong><br>San Antonio, met 4-3. De beslissende zevende wedstrijd won de ploeg in Oklahoma City met 111-103.</p>
<p><strong>Waar kan ik Spurs – Thunder live kijken?</strong><br>Gratis live bij Bet365, met een account met een kleine storting. Ook via NBA League Pass kun je alle wedstrijden volgen.</p>
<p><strong>Wat is onze voorspelling voor Spurs – Thunder?</strong><br>San Antonio wint met 114-108. Onze hoofdtip is een zege van de Spurs inclusief verlenging (1,86 bij Circus).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

WEDTIPS = {"wedtip-1-2": "San Antonio Spurs wint (incl. verlenging)", "quotering-wedtip-1": "1.86",
           "wedtip-2-2": "Minder dan 237.5 punten (incl. verlenging)", "quotering-wedtip-2": "1.53",
           "wedtip-3-2": "San Antonio Spurs +4.5 punten", "quotering-wedtip-3": "1.48",
           "bookmaker-wedtips": "64ff0fbd5a8f205b05d54670"}

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_BASKETBAL, "competitie": COMPETITIE_NBA,
          "datum-tijd-van-wedstrijd": "2026-10-21T01:30:00.000Z",
          "publicatiedatum": datetime.now(timezone.utc).isoformat(), **WEDTIPS}
    if "--live" not in sys.argv:
        import re
        tekst = re.sub(r"<[^>]+>", " ", content + content2 + content3)
        print(len(SAMENVATTING), "tekens samenvatting |", len(tekst.split()), "woorden"); sys.exit()
    print("item:", WF.create_live(fd))
