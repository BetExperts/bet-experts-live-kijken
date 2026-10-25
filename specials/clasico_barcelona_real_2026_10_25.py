# -*- coding: utf-8 -*-
"""Los SEO-artikel: Wie wint FC Barcelona – Real Madrid? El Clásico 25 oktober 2026 in cijfers (24-10-2026).
Zoekwoorden (Google-suggesties NL + GSC): el clasico 2026 oktober, barcelona real madrid onderlinge resultaten,
el clasico uitslagen (all time), hoe vaak heeft barcelona van real madrid gewonnen, el clasico statistieken,
barcelona real madrid 5-0 / 11-1, barcelona real madrid kijken, barcelona real madrid odds, opstellingen.
Feiten: specials/clasico_feiten_2026_10_25.md (ESPN-API, Wikipedia, laliga.com, fcbarcelona.com, Ziggo; 24-10).
Odds: eigen odds-feed (/api/odds-feed, 15 NL-bookmakers) en Kambi, za 24-10 ±14:30. Wedtip (Jasper): minder dan 14,5
schoten op doel @1,86 bij Bet365, tweede tip Barcelona minder dan 9,5 schoten op doel @1,60 (Unibet: 1,75 en 1,52).
Niet gebruikt (onzeker): 'voor het eerst ooit voor in de balans', transferbedragen, beroep Vinícius, scorers 1995.
  python3 specials/clasico_barcelona_real_2026_10_25.py   (dry run)
  kaart: og_kaarten/clasico.py, publiceren: specials/concept_publiceer.py clasico_barcelona_real_2026_10_25 --live"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

TITEL = "Wie wint Barcelona – Real Madrid? El Clásico in cijfers"
SLUG = "wie-wint-barcelona-real-madrid-el-clasico-oktober-2026"
SAMENVATTING = ("El Clásico op 25 oktober 2026: wie wint Barcelona – Real Madrid? Odds van 15 bookmakers, onderlinge "
                "resultaten, statistieken en onze wedtip.")
RUBRIEK = "64ff0fbd5a8f205b05d5468f"   # zelfde rubriek als de voorbeschouwing van deze wedstrijd

VB = "/nieuws/wedtips-barcelona---real-madrid-voorspelling-odds-opstellingen-kan-mourinhos-madrid-de-koploper-van-zijn-troon-stoten"
ODDS = "/odds-vergelijken-bij-alle-bookmakers-beste-odds-vandaag"

# (bookmaker, review-slug, Barcelona, gelijk, Real Madrid)  1X2, za 24-10 ±14:30
ODDS_1X2 = [
    ("711", "711", 1.65, 6.00, 4.00), ("Starcasino", "starcasino", 1.64, 5.66, 3.75),
    ("Unibet", "unibet", 1.63, 6.00, 4.00), ("BetMGM", "betmgm", 1.63, 5.80, 3.90),
    ("Bet365", "bet365", 1.62, 5.75, 4.00), ("Circus", "circus", 1.62, 5.60, 3.95),
    ("Vbet", "vbet", 1.62, 5.80, 3.72), ("JACKS.NL", "jacks-nl", 1.61, 5.75, 3.85),
    ("Oranje Palace", "oranje-palace", 1.61, 5.75, 3.85), ("Tonybet", "tonybet", 1.61, 5.80, 3.75),
    ("LeoVegas", "leovegas", 1.60, 5.50, 3.75), ("888sport", None, 1.59, 5.75, 3.91),
    ("ComeOn!", "comeon", 1.59, 5.75, 3.91), ("TOTO", "toto", 1.58, 5.25, 3.70),
    ("Bingoal", "bingoal", 1.58, 6.00, 3.70),
]
BEST = [max(r[i] for r in ODDS_1X2) for i in (2, 3, 4)]


def q(x):
    return f"{x:.2f}".replace(".", ",")


def cel(x, best):
    return f"<strong>{q(x)}</strong>" if x == best else q(x)


def kansen():
    """Gemiddelde kans zonder bookmakermarge (in hele procenten)."""
    gem = [sum(1 / r[i] for r in ODDS_1X2) / len(ODDS_1X2) for i in (2, 3, 4)]
    return [round(100 * g / sum(gem)) for g in gem]


KANS_B, KANS_G, KANS_R = kansen()

content = f"""<p><strong>Barcelona is de favoriet voor El Clásico van zondag 25 oktober 2026 (21:00 uur, Ziggo Sport 1). Volgens de odds van 15 Nederlandse bookmakers heeft Barça ongeveer {KANS_B} procent kans om te winnen, Real Madrid {KANS_R} procent en een gelijkspel {KANS_G} procent. Barça staat met 27 punten uit negen wedstrijden bovenaan in La Liga, Real Madrid mist de geschorste Vinícius Júnior. In de officiële onderlinge balans staat het precies gelijk: beide clubs wonnen 106 keer, 52 keer werd het gelijk. Onze wedtip: minder dan 14,5 schoten op doel (1,86 bij Bet365).</strong></p>
<h3><strong>El Clásico op 25 oktober 2026: aanvang, stadion en zender</strong></h3>
{tabel(None, [
    ("Wedstrijd", "FC Barcelona – Real Madrid"),
    ("Competitie", '<a href="/competities/la-liga">La Liga</a>, speelronde 10'),
    ("Datum en aanvang", "Zondag 25 oktober 2026, 21:00 uur (wintertijd)"),
    ("Stadion", "Spotify Camp Nou, Barcelona"),
    ("Scheidsrechter", "Juan Martínez Munuera (VAR: Javier Iglesias Villanueva)"),
    ("Live op tv", "Ziggo Sport 1 (bij Ziggo kanaal 14)"),
    ("Trainers", "Hansi Flick (Barcelona) en José Mourinho (Real Madrid)"),
])}
<p>In de nacht van zaterdag op zondag gaat de klok een uur terug, maar dat verandert niets aan de aanvangstijd: de wedstrijd begint om 21:00 uur Nederlandse tijd. Ziggo Sport heeft dit seizoen de uitzendrechten van La Liga. Kijk je niet via Ziggo, dan heb je een Ziggo Sport Totaal-abonnement nodig, dat ook bij KPN en Odido te krijgen is. Alle opties lees je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<h3><strong>Wie wint Barcelona – Real Madrid volgens de bookmakers?</strong></h3>
<p>Barcelona is bij elke bookmaker de favoriet. De odds op een zege van Barça liggen tussen 1,58 en 1,65, op Real Madrid tussen 3,70 en 4,00 en op een gelijkspel tussen 5,25 en 6,00. Dit zijn de odds op de einduitslag (1X2) bij alle vergunde bookmakers in ons overzicht, de hoogste odd per uitkomst is vetgedrukt:</p>
{tabel(["Bookmaker", "Barcelona", "Gelijk", "Real Madrid"], [
    (f'<a href="/bookmakers/{s}">{n}</a>' if s else n, cel(b, BEST[0]), cel(g, BEST[1]), cel(r, BEST[2]))
    for n, s, b, g, r in ODDS_1X2
])}
<p><em>Odds van zaterdag 24 oktober rond 14:30 uur. Ze kunnen tot de aftrap nog veranderen; de actuele odds zie je in onze <a href="{ODDS}">odds-vergelijker</a>.</em></p>
<p>Opvallend is hoe zeker de bookmakers zijn van doelpunten. Meer dan 2,5 goals staat overal op 1,16 tot 1,18 en beide teams scoren op 1,23 tot 1,26. Dat past bij de geschiedenis: in negen van de laatste tien Clásicos vielen er drie of meer doelpunten. Die markten leveren dus weinig op.</p>"""

content2 = f"""<h3><strong>Stand en vorm: Barça foutloos, Real wankelt buiten Madrid</strong></h3>
{tabel(["#", "Club", "Gespeeld", "Doelsaldo", "Punten"], [
    ("1", "<strong>FC Barcelona</strong>", "9", "39-9", "<strong>27</strong>"),
    ("2", "Atlético Madrid", "9", "19-8", "22"),
    ("3", "<strong>Real Madrid</strong>", "9", "23-9", "<strong>21</strong>"),
    ("4", "Real Betis", "9", "16-14", "19"),
])}
<p><em>Stand van La Liga voor speelronde 10, zaterdagochtend 24 oktober. Atlético speelt zaterdagavond nog tegen Deportivo.</em></p>
<p>Barcelona won alle negen competitiewedstrijden en scoorde gemiddeld 4,3 keer per duel. Uit wonnen de Catalanen onder meer met 0-5 bij Elche en Valencia en vorige week met 2-5 bij Betis. De enige nederlaag van het seizoen kwam dinsdag in de Champions League: 4-2 bij Paris Saint-Germain. Topscorer is Raphinha met 12 competitiedoelpunten, gevolgd door Lamine Yamal met 8.</p>
<p>Real Madrid won zeven van de negen competitieduels en is thuis nog foutloos (5 uit 5). Buiten Madrid gaat het minder: de ploeg van Mourinho verloor met 1-0 bij Betis en met 2-1 bij Atlético Madrid, waar Dean Huijsen rood kreeg. In de Champions League won Real wel alle drie de wedstrijden, onder meer met 3-4 bij AS Roma en woensdag met 4-1 van RB Leipzig. Kylian Mbappé maakte negen competitiedoelpunten. Wint Barcelona zondag, dan staat Real negen punten achter de koploper.</p>
<p>De trainers kennen elkaar: Flick en Mourinho stonden pas één keer eerder tegenover elkaar, in de Champions League van 2019 (Bayern München – Tottenham, 3-1). Flick won zes van zijn zeven Clásicos als trainer van Barça. Mourinho speelde in zijn eerste periode bij Real (2010-2013) zeventien keer tegen Barcelona: vijf zeges, zes gelijke spelen en zes nederlagen.</p>
<h3><strong>Wie ontbreken er? Afwezigen en verwachte opstellingen</strong></h3>
<p><strong>Real Madrid</strong> mist <strong>Vinícius Júnior</strong>. Hij kreeg op 10 oktober tegen Villarreal direct rood, nadat hij een tegenstander aan de haren trok, en is vier wedstrijden geschorst. Ook Rodrygo (knie) en Raúl Asencio (been) ontbreken, en Ferland Mendy doet niet mee. Bij <strong>Barcelona</strong> zijn Dani Olmo (adductor), Eric García (dij), Andreas Christensen en Roony Bardghji geblesseerd. Achter Jules Koundé (enkel) staat een groot vraagteken.</p>
<p>Beide clubs hebben deze zomer flink ingekocht, dus de opstellingen zien er anders uit dan vorig seizoen. Zo verwachten de Spaanse media de ploegen:</p>
<p><strong>Vermoedelijke opstelling FC Barcelona:</strong> Joan García; Xavi Espart, Pau Cubarsí, Gerard Martín, João Cancelo; Rodri, Pedri, Fermín López; Lamine Yamal, Raphinha, Anthony Gordon.</p>
<p><strong>Vermoedelijke opstelling Real Madrid:</strong> Courtois; Valverde, Konaté, Huijsen, Cucurella; Tchouaméni, Bernardo Silva; Güler, Bellingham, Diomande; Mbappé.</p>
<p>De officiële opstellingen zijn ongeveer een uur voor de aftrap bekend. Je vindt ze dan in onze <a href="{VB}">voorbeschouwing van Barcelona – Real Madrid</a>, die we tot de aftrap bijwerken. Meer over beide clubs lees je op de clubpagina's van <a href="/clubs/fc-barcelona">FC Barcelona</a> en <a href="/clubs/real-madrid">Real Madrid</a>.</p>
<h3><strong>Onderlinge resultaten: hoe vaak won Barcelona van Real Madrid?</strong></h3>
<p>In officiële wedstrijden speelden Barcelona en Real Madrid 264 keer tegen elkaar. Beide clubs wonnen er 106, en 52 keer werd het gelijk. Barça scoorde 441 keer, Real 444 keer. Sinds de 2-0 van Barcelona in mei 2026 staat de balans dus precies gelijk. Wint Barça zondag, dan komt de club in de officiële onderlinge balans voor te staan.</p>
{tabel(["Competitie", "Duels", "Barcelona", "Gelijk", "Real Madrid"], [
    ("<strong>Alle officiële duels</strong>", "264", "<strong>106</strong>", "52", "<strong>106</strong>"),
    ("La Liga", "192", "77", "35", "80"),
    ("Copa del Rey", "38", "17", "8", "13"),
    ("Supercopa de España", "19", "7", "2", "10"),
    ("Champions League", "8", "2", "3", "3"),
])}
<p><em>Officiële wedstrijden tot en met 10 mei 2026, zonder vriendschappelijke duels. Telt je de oefenduels mee, dan staat Barcelona voor: 131 zeges tegen 112 voor Real.</em></p>
<p>In La Liga heeft Real Madrid een kleine voorsprong (80 tegen 77). In de recente jaren is Barcelona juist de sterkste: van de laatste zeven Clásicos won Barça er zes.</p>
<h3><strong>De laatste 10 Clásicos: alle uitslagen</strong></h3>
{tabel(["Datum", "Competitie", "Uitslag"], [
    ("10 mei 2026", "La Liga", "<strong>Barcelona – Real Madrid 2-0</strong>"),
    ("11 januari 2026", "Supercopa (finale)", "<strong>Barcelona</strong> – Real Madrid 3-2"),
    ("26 oktober 2025", "La Liga", "<strong>Real Madrid</strong> – Barcelona 2-1"),
    ("11 mei 2025", "La Liga", "<strong>Barcelona</strong> – Real Madrid 4-3"),
    ("26 april 2025", "Copa del Rey (finale)", "<strong>Barcelona</strong> – Real Madrid 3-2 (na verlenging)"),
    ("12 januari 2025", "Supercopa (finale)", "Real Madrid – <strong>Barcelona</strong> 2-5"),
    ("26 oktober 2024", "La Liga", "Real Madrid – <strong>Barcelona</strong> 0-4"),
    ("21 april 2024", "La Liga", "<strong>Real Madrid</strong> – Barcelona 3-2"),
    ("14 januari 2024", "Supercopa (finale)", "<strong>Real Madrid</strong> – Barcelona 4-1"),
    ("28 oktober 2023", "La Liga", "Barcelona – <strong>Real Madrid</strong> 1-2"),
])}
<p>Barcelona won zes van de laatste tien Clásicos, Real Madrid vier. Een gelijkspel was er niet. Met de 2-0 van 10 mei 2026, door doelpunten van Marcus Rashford en Ferran Torres, werd Barça voor de 29e keer kampioen. Real Madrid won voor het laatst in Barcelona op 28 oktober 2023, toen Jude Bellingham twee keer scoorde (1-2).</p>"""

content3 = f"""<h3><strong>El Clásico statistieken: doelpunten, kaarten en schoten op doel</strong></h3>
<p>De laatste tien officiële Clásicos in cijfers:</p>
<ul><li><strong>4,6 doelpunten</strong> per wedstrijd gemiddeld (46 in tien duels).</li><li><strong>Meer dan 2,5 goals:</strong> 9 van de 10 wedstrijden, alleen de 2-0 van mei 2026 niet.</li><li><strong>Beide teams scoorden:</strong> 8 van de 10 wedstrijden.</li><li><strong>6 gele kaarten</strong> per wedstrijd gemiddeld.</li><li><strong>13 schoten op doel</strong> per wedstrijd gemiddeld (samen), in de negen duels waarvan de cijfers bekend zijn.</li><li><strong>Barcelona</strong> kwam in die negen duels nooit verder dan 9 schoten op doel, gemiddeld 6,7.</li></ul>
<p>Er vallen dus veel doelpunten, maar het aantal schoten op doel is lager dan je zou denken. Beide ploegen geven elkaar weinig ruimte en een groot deel van de goals valt uit de weinige kansen die er zijn. In La Liga komt Barça dit seizoen gemiddeld wel op 8,4 schoten op doel per wedstrijd, maar dat is tegen zwakkere tegenstanders.</p>
<h3><strong>De grootste overwinningen in El Clásico</strong></h3>
<p>De grootste uitslag ooit is <strong>Real Madrid – Barcelona 11-1</strong>, op 13 juni 1943 in de halve finale van de beker. Barça had de heenwedstrijd met 3-0 gewonnen, maar ging in Madrid onderuit in een vijandige sfeer, met omstreden beslissingen van de scheidsrechter. Bij rust stond het al 8-0. Het is nog altijd het grootste verschil in de geschiedenis van El Clásico.</p>
<ul><li><strong>Real Madrid – Barcelona 8-2</strong> (3 februari 1935, competitie)</li><li><strong>Barcelona – Real Madrid 7-2</strong> (24 september 1950, competitie)</li><li><strong>Real Madrid – Barcelona 0-5</strong> (17 februari 1974): Barça won in het Bernabéu, in het eerste seizoen van Johan Cruijff, die zelf ook scoorde.</li><li><strong>Barcelona – Real Madrid 5-0</strong> (8 januari 1994): hattrick van Romário, met Cruijff als trainer.</li><li><strong>Real Madrid – Barcelona 5-0</strong> (7 januari 1995): de revanche een jaar later.</li><li><strong>Barcelona – Real Madrid 5-0</strong> (29 november 2010): het Barça van Guardiola tegen het Real Madrid van José Mourinho, die zondag weer op de bank zit.</li></ul>
<h3><strong>Topscorers aller tijden in El Clásico</strong></h3>
<p><strong>Lionel Messi</strong> is met 26 doelpunten in 45 wedstrijden de topscorer aller tijden van El Clásico. Daarna volgen Alfredo Di Stéfano en Cristiano Ronaldo (allebei 18), Karim Benzema (16) en Raúl (15). Sergio Busquets speelde de meeste Clásicos: 48. Van de spelers die zondag op het veld kunnen staan, zijn Raphinha en Mbappé de gevaarlijkste: Raphinha scoorde dit seizoen al 14 keer in alle competities, Mbappé 12 keer.</p>
<h3><strong>Barcelona en Real Madrid: de prijzenkast</strong></h3>
{tabel(["Prijs", "FC Barcelona", "Real Madrid"], [
    ("Landstitels", "29", "<strong>36</strong>"),
    ("Europacup I / Champions League", "5", "<strong>15</strong>"),
    ("Copa del Rey", "<strong>32</strong>", "20"),
    ("Supercopa de España", "<strong>16</strong>", "13"),
])}
<p>Barcelona werd in 2025/26 voor de tweede keer op rij kampioen onder Flick. Real Madrid won de afgelopen twee seizoenen geen grote prijs. In juni haalde de club José Mourinho terug als trainer.</p>
<h3><strong>Wedden op El Clásico: onze wedtip</strong></h3>
<p><strong>Onze wedtip: minder dan 14,5 schoten op doel (1,86 bij <a href="/bookmakers/bet365">Bet365</a>).</strong> Bij deze weddenschap tel je de schoten op doel van beide ploegen samen, volgens de officiële wedstrijdstatistieken. Bij 14 of minder win je. De odd van 1,86 staat voor een kans van ongeveer 54 procent; wij schatten die kans op 60 procent. Waarom:</p>
<ul><li><strong>Clásicos zijn zuiniger dan ze lijken.</strong> In zes van de negen recente Clásicos met bekende cijfers bleef het totaal op 14 of lager, gemiddeld waren het er 13.</li><li><strong>Real mist zijn gevaarlijkste dribbelaar.</strong> Zonder Vinícius en Rodrygo komt minder van het gevaar van de flanken. Real haalde buiten Madrid dit seizoen gemiddeld maar 5,75 schoten op doel.</li><li><strong>Ook Barça blijft in Clásicos onder zijn gemiddelde.</strong> In La Liga komt Barça dit seizoen op 8,4 schoten op doel per wedstrijd, in de recente Clásicos gemiddeld op 6,7. Daarbij mist Flick ook nog Dani Olmo.</li><li><strong>Bet365 heeft de beste odd.</strong> Bij Unibet staat dezelfde lijn op 1,75.</li></ul>
<p>Het risico: drie van die zes duels eindigden op precies 14 schoten op doel, en de bookmakers verwachten veel doelpunten. Wordt het een open wedstrijd met vroege goals, dan kan het totaal snel oplopen. Zet daarom geen grote inzet.</p>
<p><strong>Liever een tweede optie?</strong> Barcelona minder dan 9,5 schoten op doel staat op 1,60 bij Bet365. Barça bleef in alle negen recente Clásicos met bekende cijfers onder de 10. Meer uitleg over deze markten lees je in onze <a href="{VB}">voorbeschouwing met voorspelling en odds</a>.</p>
<h3><strong>Veelgestelde vragen over El Clásico</strong></h3>
<p><strong>Hoe laat begint Barcelona – Real Madrid?</strong><br>Zondag 25 oktober 2026 om 21:00 uur Nederlandse tijd, in het Spotify Camp Nou in Barcelona.</p>
<p><strong>Waar kan ik El Clásico live kijken?</strong><br>Op Ziggo Sport 1. Bij Ziggo is dat kanaal 14; bij andere providers heb je Ziggo Sport Totaal nodig.</p>
<p><strong>Wie wint Barcelona – Real Madrid volgens de bookmakers?</strong><br>Barcelona. Met odds tussen 1,58 en 1,65 geven de bookmakers Barça ongeveer {KANS_B} procent winkans, tegen {KANS_R} procent voor Real Madrid.</p>
<p><strong>Hoe vaak heeft Barcelona van Real Madrid gewonnen?</strong><br>In officiële wedstrijden 106 keer, net zo vaak als Real Madrid van Barcelona won. In La Liga won Barça 77 keer en Real 80 keer.</p>
<p><strong>Wat is de grootste overwinning ooit in El Clásico?</strong><br>Real Madrid – Barcelona 11-1 op 13 juni 1943, in de halve finale van de beker. De grootste zeges van Barça zijn 7-2 (1950) en de 5-0's van 1994 en 2010, en de 0-5 in Madrid in 1974.</p>
<p><strong>Wie is de topscorer aller tijden van El Clásico?</strong><br>Lionel Messi, met 26 doelpunten in 45 wedstrijden.</p>
<p><strong>Speelt Vinícius Júnior mee?</strong><br>Nee. Hij is vier wedstrijden geschorst na zijn rode kaart tegen Villarreal op 10 oktober.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    alles = content + content2 + content3
    tekst = re.sub(r"<[^>]+>", " ", alles)
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", len(tekst.split()), "woorden | kansen", KANS_B, KANS_G, KANS_R)
    assert len(TITEL) <= 60 and 120 <= len(SAMENVATTING) <= 155 and KANS_B + KANS_G + KANS_R in (99, 100, 101)
    assert "<h2" not in alles and "<h4" not in alles and "affiliate" not in alles.lower() and "betcity" not in alles.lower()
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles) and not re.search(r"<(ul|ol)>\s+<", alles)
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    print("dry run ok – niets gepubliceerd")
