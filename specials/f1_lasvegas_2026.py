# -*- coding: utf-8 -*-
"""Los artikel: F1 Grand Prix van Las Vegas 2026 (ronde 21 van 23) - data, tijden, live kijken, circuit en odds.
Zoekwoorden: GP Las Vegas 2026, F1 Las Vegas tijden, hoe laat F1 Las Vegas, Las Vegas Grand Prix live kijken, Las Vegas circuit, odds.
Feiten: specials/f1_lasvegas_2026_feiten.md (formula1.com racepagina + circuitpagina + uitslagen 2023-2025 + standen 12-11,
ziggo.nl Las Vegas-pagina, gpblog 10-11 Verstappen, NOS 8-11, planetf1/crash.net 2026-terminologie, Pirelli, gpblog Viaplay/DPG).
Odds: Unibet NL (Kambi ubnl), event 1026519082 'GP Las Vegas 2026', twee markten 'GP-winnaar' (winnaar + top 3), 12-11-2026 14:48.
Bewust vaag of weggelaten: Straight Mode-zones en bandenkeuze Vegas 2026 (nog niet gepubliceerd), exacte topsnelheid,
pitstraatverlies, kanaalnummers KPN/Odido, weersverwachting, mogelijk kapot onderdeel Red Bull Brazilië.
Slug 404 gecontroleerd 12-11.
  python3 specials/f1_lasvegas_2026.py   (dry run)
  publiceren: specials/concept_publiceer.py f1_lasvegas_2026 --live"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "f1-las-vegas-2026-tijden-live-kijken-circuit-odds"
RUBRIEK = "673cb057713facd07c37844b"   # Formule 1
TITEL = "F1 GP Las Vegas 2026: tijden, live kijken, circuit en odds"
SAMENVATTING = ("Alles over de F1 Grand Prix van Las Vegas 2026: de race begint zondag 22 november om 05:00 uur. "
                "Tijden, tv, het circuit en de odds.")
PEIL = "donderdag 12 november, 14:48 uur"

SESSIES = [("Vrije training 1", "donderdag 19 november, 16:30", "vrijdag 20 november", "01:30 – 02:30"),
           ("Vrije training 2", "donderdag 19 november, 20:00", "vrijdag 20 november", "05:00 – 06:00"),
           ("Vrije training 3", "vrijdag 20 november, 16:30", "zaterdag 21 november", "01:30 – 02:30"),
           ("Kwalificatie", "vrijdag 20 november, 20:00", "zaterdag 21 november", "05:00 – 06:00"),
           ("Race (50 ronden)", "zaterdag 21 november, 20:00", "zondag 22 november", "05:00")]

# Unibet NL 12-11 14:48: (coureur, team, winnaar, top 3)
ODDS = [("Max Verstappen", "Red Bull", 2.50, 1.25), ("Kimi Antonelli", "Mercedes", 3.50, 1.50),
        ("Lando Norris", "McLaren", 6.00, 1.75), ("George Russell", "Mercedes", 7.50, 2.00),
        ("Charles Leclerc", "Ferrari", 13.00, 3.75), ("Lewis Hamilton", "Ferrari", 13.00, 3.75),
        ("Oscar Piastri", "McLaren", 13.00, 3.75), ("Isack Hadjar", "Red Bull", 17.00, 4.50)]

WINNAARS = [("2023", "Max Verstappen (Red Bull)", "Charles Leclerc", "Sergio Pérez", "Charles Leclerc"),
            ("2024", "George Russell (Mercedes)", "Lewis Hamilton", "Carlos Sainz", "George Russell"),
            ("2025", "Max Verstappen (Red Bull)", "George Russell", "Kimi Antonelli", "Lando Norris")]

STAND = [("1", "Kimi Antonelli", "Mercedes", "390 (kampioen)"), ("2", "Max Verstappen", "Red Bull", "279"),
         ("3", "George Russell", "Mercedes", "262"), ("4", "Lewis Hamilton", "Ferrari", "261"),
         ("5", "Charles Leclerc", "Ferrari", "249"), ("6", "Lando Norris", "McLaren", "246")]

L = {"viaplay": '<a href="/zenders/viaplay">Viaplay</a>',
     "f1tv": '<a href="/zenders/f1-tv">F1 TV</a>',
     "unibet": '<a href="/bookmakers/unibet">Unibet</a>',
     "brazilie": '<a href="/nieuws/wie-wint-f1-gp-brazilie-2026-favorieten-odds-voorspelling">de GP van Brazilië</a>',
     "kijkbr": '<a href="/nieuws/f1-brazilie-2026-live-kijken-gp-sao-paulo">hoe je de F1 kijkt bij Viaplay</a>',
     "legaal": '<a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>'}


def kans(o):
    return round(100 / o)


def o(x):
    return f"{x:.2f}".replace(".", ",")


content = f"""<p><strong>De Formule 1 Grand Prix van Las Vegas 2026 wordt gereden op zaterdagavond 21 november om 20:00 uur lokale tijd. In Nederland is dat zondag 22 november om 05:00 uur 's ochtends. De kwalificatie is een dag eerder, zaterdag 21 november om 05:00 uur. Je kijkt alle sessies live bij Viaplay. Max Verstappen, die in Las Vegas al twee keer won, is bij de bookmakers de favoriet.</strong></p>
<p>Las Vegas is de 21e race van 23 en geen sprintweekend. Na Las Vegas volgen alleen nog de Grand Prix van Qatar (29 november) en de slotrace in Abu Dhabi (6 december). De wereldtitel is al vergeven: Kimi Antonelli werd in Mexico kampioen en Mercedes pakte in Brazilië de constructeurstitel. Toch staat er nog genoeg op het spel, want Verstappen vecht met George Russell en Lewis Hamilton om de tweede plek in het kampioenschap.</p>
<h3><strong>Hoe laat is de F1 in Las Vegas?</strong></h3>
{tabel(["Sessie", "Lokale tijd (Las Vegas)", "Nederlandse datum", "Nederlandse tijd"], [(f"<strong>{s}</strong>" if s.startswith("Race") or s == "Kwalificatie" else s, lok, d, t) for s, lok, d, t in SESSIES])}
<p>Las Vegas ligt negen uur achter op Nederland. Omdat alles 's avonds onder de lampen wordt gereden, vallen alle sessies voor Nederlandse kijkers in de nacht of vroeg in de ochtend. Wil je de race live zien, zet dan de wekker voor zondagochtend vijf uur. De race duurt ongeveer anderhalf uur.</p>
<h3><strong>Waar kun je de GP van Las Vegas live kijken?</strong></h3>
<p>{L['viaplay']} zendt alle trainingen, de kwalificatie en de race live uit. Via de tv kijk je op Viaplay TV+ (bij Ziggo kanaal 432); de race staat daar van 05:00 tot 07:00 uur. Kijken kan ook in de Viaplay-app. Met een Viaplay-abonnement kun je in Nederland bovendien {L['f1tv']} Pro koppelen, voor onder meer de onboardbeelden en de boordradio; F1 TV is ook los af te sluiten.</p>
<p>Viaplay Nederland is sinds 30 oktober onderdeel van DPG Media, het bedrijf achter Videoland. Voor kijkers verandert er voorlopig niets: abonnement, prijs en app blijven hetzelfde. De sport komt later als apart pakket naast Videoland, maar dat gebeurt pas in 2027. Op vrijdagavond 20 november blikt het Ziggo Sport Race Café vooruit op het weekend (22:30 tot 23:45 uur). Meer over kijken lees je in {L['kijkbr']}.</p>"""

content2 = f"""<h3><strong>Het circuit: Las Vegas Strip Circuit</strong></h3>
<p>De Formule 1 rijdt in Las Vegas op een straatcircuit over de beroemde Las Vegas Boulevard, beter bekend als de Strip. Het circuit gaat langs de Sphere, Caesars Palace, de Bellagio en het Venetian, en wordt tegen de klok in gereden. Het pitgebouw staat op een voormalig parkeerterrein dat de Formule 1 zelf kocht. Las Vegas staat sinds 2023 op de kalender en blijft daar volgens een verlenging uit juni van dit jaar tot en met 2037.</p>
{tabel(["Kenmerk", "Las Vegas Strip Circuit"], [
    ("Lengte", "6,201 kilometer"),
    ("Aantal bochten", "17"),
    ("Aantal ronden", "50"),
    ("Racedistantie", "309,958 kilometer"),
    ("Langste rechte stuk", "± 1,9 kilometer over de Strip"),
    ("Ronderecord", "1:33.365, Max Verstappen (2025)"),
    ("Rijrichting", "Tegen de klok in"),
])}
<p><strong>Wat maakt Las Vegas zo lastig?</strong> Drie dingen. Ten eerste de snelheid: op het lange rechte stuk halen de auto's ruim 340 kilometer per uur, en de gemiddelde snelheid ligt op het niveau van Monza. Ten tweede de kou. In november is het 's nachts in de woestijn rond of onder de tien graden, waardoor de banden moeilijk op temperatuur komen. Dan ontstaat snel graining: kleine rubberrolletjes op het loopvlak, waardoor de grip wegvalt. Ten derde de baan zelf: het asfalt van de openbare weg is in het begin van het weekend stoffig en wordt elke sessie sneller.</p>
<p><strong>Nieuw in 2026: geen DRS meer.</strong> Met de nieuwe reglementen is de DRS-klep verdwenen. In plaats daarvan kunnen de auto's op aangewezen rechte stukken hun voor- en achtervleugel plat zetten (Straight Mode). Wie binnen een seconde van zijn voorganger rijdt, krijgt bovendien extra elektrisch vermogen om in te halen (Overtake Mode). Op de lange rechte stukken van Las Vegas speelt het energiebeheer daardoor een grote rol. Hoeveel Straight Mode-zones de FIA in Las Vegas aanwijst en welke banden Pirelli meeneemt, wordt in de raceweek bekend; de vorige drie jaar waren dat de drie zachtste soorten.</p>
<h3><strong>Wie wonnen er eerder in Las Vegas?</strong></h3>
{tabel(["Jaar", "Winnaar", "2e", "3e", "Pole position"], WINNAARS)}
<p>Verstappen is de enige die twee keer won in Las Vegas, en hij heeft het ronderecord. In 2023 won hij zelfs met een tijdstraf van vijf seconden. In 2024 werd het een Mercedes 1-2 met Russell voor Hamilton; Verstappen werd toen vijfde en pakte daarmee zijn vierde wereldtitel. Vorig jaar won Verstappen opnieuw, en kregen Lando Norris en Oscar Piastri na de race een diskwalificatie omdat de bodemplank van hun McLarens te veel was afgesleten. Ook in de jaren tachtig werd er al in Las Vegas geracet, op een parkeerterrein bij Caesars Palace (1981 en 1982).</p>
<h3><strong>Wat staat er op het spel?</strong></h3>
{tabel(["Plaats", "Coureur", "Team", "Punten"], STAND)}
<p>Na Brazilië staat Verstappen tweede met 17 punten voorsprong op Russell en 18 op Hamilton. Er zijn nog drie races en dus maximaal 75 punten te verdienen. Ook als Verstappen in Las Vegas wint en Russell niets scoort, staat hij er daarna 42 punten voor, en dat is minder dan de 50 punten die er dan nog te verdelen zijn. De strijd om plek twee wordt in Las Vegas dus nog niet beslist. Bij de teams vechten Red Bull (415) en McLaren (398) om de derde plaats.</p>
<p>Verstappen zelf houdt de verwachtingen laag. "Ik moet zeggen dat het normaal gesproken niet ons beste circuit is", zei hij na Brazilië, waar hij van de 21e startplek nog tweede werd. Volgens hem gedraagt door de kou iedere auto zich in Las Vegas anders, en werkt de slipstream er "een beetje zoals Monza". Haalt hij het podium, dan is het zijn negende podium op rij.</p>"""

rij = [(f"<strong>{n}</strong>", t, f"<strong>{o(w)}</strong>", f"{kans(w)}%", o(p)) for n, t, w, p in ODDS]
content3 = f"""<h3><strong>Odds: wie wint de GP van Las Vegas 2026?</strong></h3>
{tabel(["Coureur", "Team", "Winnaar", "Kans volgens odd", "Top 3"], rij)}
<p><em>Odds bij {L['unibet']}, {PEIL}. Odds kunnen tot de start nog veranderen. De kans is de odd omgerekend naar een percentage (1 gedeeld door de odd), zonder correctie voor de marge van de bookmaker.</em></p>
<p><strong>Zo lees je de odds.</strong> Bij een odd van 2,50 op Verstappen krijg je bij een inzet van €10 dus €25 terug als hij wint, inclusief je inzet. De bookmaker schat zijn kans daarmee op ongeveer 40 procent. Een top 3-weddenschap is goed als je coureur op het podium eindigt; daarom zijn die odds lager.</p>
<p><strong>Onze verwachting.</strong> Verstappen is terecht de favoriet: hij won hier twee keer, heeft het ronderecord en reed in Brazilië knap van de 21e plek naar de tweede. Toch is Las Vegas ook een Mercedes-circuit. Mercedes won hier in 2024 met een 1-2 en stond vorig jaar met Russell en Antonelli op het podium, juist omdat die auto in de kou zijn banden goed op temperatuur krijgt. Daarom vinden we Russell op 7,50 de interessantste prijs. Kampioen Antonelli (3,50) is de logische tweede favoriet. Norris won Brazilië, maar daar speelden regen en gridstraffen bij de concurrentie een grote rol.</p>
<p>Een voorspelling blijft een inschatting, en een straatcircuit in de kou kent veel onzekerheid: een safety car of een fout bij de koude banden kan alles omgooien. Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit; lees {L['legaal']}. Terugkijken hoe het in Brazilië ging, kan in ons stuk over {L['brazilie']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint de F1 race in Las Vegas?</strong><br>Op zondag 22 november om 05:00 uur Nederlandse tijd. In Las Vegas is het dan zaterdagavond 20:00 uur.</p>
<p><strong>Hoe laat is de kwalificatie in Las Vegas?</strong><br>Op zaterdag 21 november om 05:00 uur Nederlandse tijd.</p>
<p><strong>Is er een sprintrace in Las Vegas?</strong><br>Nee. Las Vegas heeft een gewoon raceweekend met drie vrije trainingen, een kwalificatie en de race.</p>
<p><strong>Waar kan ik de GP van Las Vegas live zien?</strong><br>Bij Viaplay, op Viaplay TV+ (Ziggo kanaal 432) en in de Viaplay-app. F1 TV Pro is in Nederland ook beschikbaar.</p>
<p><strong>Hoe lang is het circuit van Las Vegas?</strong><br>6,201 kilometer, met 17 bochten. De race gaat over 50 ronden, samen bijna 310 kilometer.</p>
<p><strong>Wie heeft de GP van Las Vegas het vaakst gewonnen?</strong><br>Max Verstappen, in 2023 en 2025. George Russell won in 2024.</p>
<p><strong>Wie is de favoriet volgens de odds?</strong><br>Max Verstappen, met een odd van 2,50 bij Unibet. Daarna volgen Kimi Antonelli (3,50) en Lando Norris (6,00).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    alles = content + content2 + content3
    w = len(re.sub(r"<[^>]+>", " ", alles).split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", w, "woorden")
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert kans(2.50) == 40 and 10 * 2.50 == 25
    assert 279 - 262 == 17 and 279 - 261 == 18 and 17 + 25 == 42 and 75 - 25 == 50 and 42 < 50 and 415 - 398 == 17
    assert abs(6.201 * 50 - 309.958) < 0.2
    assert "<h2" not in alles and "<h4" not in alles and "betcity" not in alles.lower() and "/go/" not in alles
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    print("dry run ok")
