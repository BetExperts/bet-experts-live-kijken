# -*- coding: utf-8 -*-
"""Nieuws-artikel (bestaand item, slug blijft): Ballon d'Or 2026 - datum, tijd, genomineerden, favorieten en odds.
Voegt de oude Ballon d'Or-artikelen (2025-datum, favorieten 2025/2026, top-4/top-5-lijstjes) samen tot één actueel stuk.
ITEM_ID 6abbacc9a6402ef4a95a8f7f. Rubriek blijft zoals hij is, geen wedgids-velden.

Gecontroleerd op 21-10-2026 (ceremonie nog NIET geweest):
- 70e editie, ma 26 okt 2026, London Palladium Theatre, Londen (UEFA 28-05 en 08-09-2026). Eerste keer buiten Parijs,
  eerbetoon aan Stanley Matthews (winnaar 1956).
- Aanvang 20.00 uur Londen = 21.00 uur NL (Britse zomertijd eindigt 25-10; Ziggo-pagina en Belgische gids: 21.00 uur).
  Rode loper vanaf 19.00 uur NL. Gratis live via DAZN (wereldwijd partner, ~200 markten, gratis account) en ballondor.com.
  Geen Ziggo Sport-zender aangekondigd voor 2026 (2025: Ziggo Sport 2).
- Beoordelingsperiode mannen 3-8-2025 t/m 19-7-2026 (WK-finale). Stemming sloot 28-09. Jury: 100 journalisten (top-100
  FIFA), vrouwen 50. Punten 15-12-10-8-7-5-4-3-2-1. Criteria: individueel, team/prijzen, klasse/fair play.
- 30 genomineerden mannen + vrouwen + bijprijzen: UEFA-nominatiebericht 08-09-2026 (bijgewerkt 22-09).
  Geen Nederlandse man; vrouwen: Brugts, Casparij, Miedema; Kopa vrouwen: Veerle Buurman.
- Kane: 61 goals in 51 Bayern-duels (36 BL, 14 CL, 10 Pokal, 1 Supercup), 73 in 65 incl. Engeland, 6 WK-goals,
  Engeland 3e (6-4 tegen Frankrijk), Gouden Schoen; Bayern kampioen + beker; CL-halve finale verloren van PSG.
- Yamal: LaLiga kampioen + speler van het seizoen, 16 goals + 11 assists in 28 LaLiga-duels, vanaf april geblesseerd
  (club), wereldkampioen (finale 1-0 n.v. tegen Argentinië, Ferran Torres 106'), 1 WK-goal; 2e in 2025.
- WK-prijzen: Gouden Bal Rodri, Gouden Schoen Mbappé (10), Messi Zilveren Bal (8 goals). CL-finale 30-05 Boedapest:
  PSG-Arsenal 1-1 n.v., PSG wint 4-3 na strafschoppen.
- Markt (19-10-2026): Kane favoriet (~65% impliciet), Yamal 2e (begin okt kort favoriet), Mbappé/Messi/Rodri ver daarachter.
- Wedden: Besluit kansspelen op afstand art. 2.1 lid 1 onder c (alleen weddenschappen op een sportwedstrijd of
  gebeurtenissen daarin) + Ksa-bericht 26-03-2026 ("prijsverkiezingen, zoals een MVP-prijs" niet toegestaan).
  NB: Bijlage 2 Regeling kansspelen op afstand noemt prijsverkiezingen NIET (die gaat over kaarten, corners e.d.).
  python3 specials/ballon_dor_2026.py [--live]"""
import os, sys, re
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

ITEM_ID = "6abbacc9a6402ef4a95a8f7f"
SLUG = "ballon-dor-2026-odds-favorieten-kanshebbers-onze-voorspelling"
TITEL = "Ballon d'Or 2026: datum, tijd, favorieten en genomineerden"
SAMENVATTING = ("De Ballon d'Or 2026 wordt maandag 26 oktober om 21.00 uur uitgereikt in Londen. Datum, tv, "
                "genomineerden, favorieten en de odds op een rij.")

# Deelkaart (maatwerk, geen spelersfoto's)
OG_KOP = "Ballon d'Or <span>2026</span>"
OG_EYEBROW = "Ma 26 okt · 21.00 uur"
OG_CHIPS = ["London Palladium", "Gratis op DAZN"]
OG_MOTIEF = "lijst"
OG_DATA = ["Harry Kane · Bayern", "Lamine Yamal · Barcelona", "Kylian Mbappé · Real Madrid", "Rodri · Man City"]
OG_HEADER = "Voetbal"
OG_HEADER_SUB = "favorieten volgens de markt"

KSA = "<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"
CL, WK = "/competities/champions-league", "/competities/world-cup"
BAR, BAY, PSG = "/clubs/fc-barcelona", "/clubs/bayern-munchen", "/clubs/paris-saint-germain-psg"
RMA, ARS, MCI, MIA = "/clubs/real-madrid", "/clubs/arsenal", "/clubs/manchester-city", "/clubs/inter-miami"
CORNERS = "/nieuws/dit-is-waarom-wedden-op-corners-niet-meer-legaal-is-in-nederland"


def a(href, tekst):
    return f'<a href="{href}">{tekst}</a>'


# Kane: 36 + 10 + 14 + 1 = 61 voor Bayern, + 12 voor Engeland = 73
KANE_BAYERN = 36 + 10 + 14 + 1
KANE_TOTAAL = KANE_BAYERN + 12
assert KANE_BAYERN == 61 and KANE_TOTAAL == 73

PUNTEN = [15, 12, 10, 8, 7, 5, 4, 3, 2, 1]
JURY = 100
PER_STEMBRIEF = sum(PUNTEN)
MAX_PUNTEN = PUNTEN[0] * JURY
assert PER_STEMBRIEF == 67 and MAX_PUNTEN == 1500

GENOMINEERDEN = [
    ("Jude Bellingham", "Engeland", "Real Madrid"), ("Pau Cubarsí", "Spanje", "FC Barcelona"),
    ("Marc Cucurella", "Spanje", "Chelsea"), ("Ousmane Dembélé", "Frankrijk", "Paris Saint-Germain"),
    ("Luis Díaz", "Colombia", "Bayern München"), ("Bruno Fernandes", "Portugal", "Manchester United"),
    ("Gabriel", "Brazilië", "Arsenal"), ("Erling Haaland", "Noorwegen", "Manchester City"),
    ("Achraf Hakimi", "Marokko", "Paris Saint-Germain"), ("Harry Kane", "Engeland", "Bayern München"),
    ("Khvicha Kvaratskhelia", "Georgië", "Paris Saint-Germain"), ("Lamine Yamal", "Spanje", "FC Barcelona"),
    ("Sadio Mané", "Senegal", "Al-Nassr"), ("Marquinhos", "Brazilië", "Paris Saint-Germain"),
    ("Lautaro Martínez", "Argentinië", "Inter"), ("Kylian Mbappé", "Frankrijk", "Real Madrid"),
    ("Nuno Mendes", "Portugal", "Paris Saint-Germain"), ("Lionel Messi", "Argentinië", "Inter Miami"),
    ("João Neves", "Portugal", "Paris Saint-Germain"), ("Michael Olise", "Frankrijk", "Bayern München"),
    ("Willian Pacho", "Ecuador", "Paris Saint-Germain"), ("Julián Quiñones", "Mexico", "Al-Qadsiah"),
    ("Declan Rice", "Engeland", "Arsenal"), ("Rodri", "Spanje", "Manchester City"),
    ("Fabián Ruiz", "Spanje", "Paris Saint-Germain"), ("William Saliba", "Frankrijk", "Arsenal"),
    ("Ferran Torres", "Spanje", "FC Barcelona"), ("Dayot Upamecano", "Frankrijk", "Bayern München"),
    ("Vinícius Júnior", "Brazilië", "Real Madrid"), ("Vitinha", "Portugal", "Paris Saint-Germain"),
]
assert len(GENOMINEERDEN) == 30
N_PSG = sum(1 for g in GENOMINEERDEN if g[2] == "Paris Saint-Germain")
assert N_PSG == 9

VROUWEN = ["Selma Bacha", "Barbra Banda", "<strong>Esmee Brugts</strong>", "Klara Bühl", "Mariona Caldentey",
           "Scarlett Camberos", "<strong>Kerstin Casparij</strong>", "Temwa Chawinga", "Cata Coll", "Melchie Dumornay",
           "Caroline Graham Hansen", "Alex Greenwood", "Patri Guijarro", "Pernille Harder", "Yui Hasegawa",
           "Rose Lavelle", "Mapi León", "Lorena", "Melvine Malard", "Manaka Matsukubo", "<strong>Vivianne Miedema</strong>",
           "Ewa Pajor", "Clàudia Pina", "Alexia Putellas", "Wendie Renard", "Alessia Russo", "Khadija Shaw",
           "Momoko Tanikawa", "Caroline Weir", "Tessa Wullaert"]
assert len(VROUWEN) == 30

content = f"""<p><strong>De Ballon d'Or 2026 wordt uitgereikt op maandag 26 oktober 2026 in het London Palladium in Londen. De ceremonie begint om 21.00 uur Nederlandse tijd, de rode loper start om 19.00 uur. Je kijkt gratis live via DAZN en de officiële Ballon d'Or-website. Harry Kane geldt als grote favoriet, met Lamine Yamal als belangrijkste uitdager. De winnaar is dus nog niet bekend: die hoor je op 26 oktober.</strong></p>
<p>Het is de zeventigste editie van de bekendste individuele prijs in het voetbal, en voor het eerst verlaat de uitreiking Parijs. Organisator France Football kiest voor Londen als eerbetoon aan Stanley Matthews, de Engelsman die in 1956 de allereerste Gouden Bal won. In dit artikel lees je hoe laat alles begint, waar je kijkt, wie de 30 genomineerden zijn, wie volgens ons en volgens de markt de favorieten zijn, hoe de stemming werkt en waarom je in Nederland niet op de Ballon d'Or kunt wedden.</p>
<h3><strong>Wanneer is de Ballon d'Or 2026 uitreiking?</strong></h3>
<p>De uitreiking is op <strong>maandag 26 oktober 2026</strong>. Dat is iets later dan vorig jaar, toen de prijs al op 22 september in Parijs werd uitgereikt. Door het WK in de zomer liep de beoordelingsperiode dit jaar door tot de WK-finale van 19 juli.</p>
{tabel(["", "Ballon d'Or 2026"], [
    ("<strong>Datum</strong>", "Maandag 26 oktober 2026"),
    ("<strong>Tijd (NL)</strong>", "Rode loper vanaf 19.00 uur, ceremonie vanaf 21.00 uur"),
    ("<strong>Locatie</strong>", "London Palladium Theatre, Londen"),
    ("<strong>Live kijken</strong>", "Gratis via DAZN en ballondor.com"),
    ("<strong>Editie</strong>", "70e"),
    ("<strong>Beoordeeld seizoen</strong>", "3 augustus 2025 tot en met 19 juli 2026, inclusief het WK"),
    ("<strong>Titelhouder</strong>", "Ousmane Dembélé (Paris Saint-Germain)"),
    ("<strong>Favorieten</strong>", "Harry Kane en Lamine Yamal"),
])}
<h3><strong>Hoe laat is de Ballon d'Or 2026?</strong></h3>
<p>De show begint om <strong>21.00 uur Nederlandse tijd</strong>. In Londen is het dan 20.00 uur. Let op: een dag eerder, in de nacht van zaterdag 25 op zondag 26 oktober, gaat de klok een uur terug, maar het tijdsverschil met Londen blijft één uur. De rode loper, met interviews en aankomende spelers, kun je vanaf 19.00 uur volgen. Reken op een avond van zo'n twee tot drie uur: de bijprijzen komen eerst, de Gouden Bal voor mannen is traditioneel het slotstuk, dus pas laat op de avond weet je wie er wint.</p>
<h3><strong>Waar kun je de Ballon d'Or 2026 kijken?</strong></h3>
<p>DAZN is wereldwijd partner van de Ballon d'Or en zendt de volledige uitreiking <strong>gratis</strong> uit in zo'n tweehonderd landen, inclusief de rode loper. Je hebt daarvoor alleen een gratis account nodig, een betaald abonnement is niet nodig. Ook op de officiële website ballondor.com staat een gratis livestream. Vorig jaar zond Ziggo Sport de uitreiking uit, maar voor 2026 is er geen Nederlandse tv-zender aangekondigd. Wil je zeker zijn, check dan op de dag zelf even de programmering. Meer voetbal live zien? Op onze pagina <a href="/live-kijken">live kijken</a> zie je per wedstrijd waar je terechtkunt.</p>
<h3><strong>Tijdlijn van de Ballon d'Or 2026</strong></h3>
{tabel(["Datum", "Wat"], [
    ("3 augustus 2025", "Start van de beoordelingsperiode"),
    ("30 mei 2026", f"{a(CL, 'Champions League')}-finale in Boedapest: Paris Saint-Germain wint na strafschoppen van Arsenal (1-1)"),
    ("19 juli 2026", f"{a(WK, 'WK')}-finale: Spanje wint met 1-0 na verlenging van Argentinië, einde beoordelingsperiode"),
    ("8 september 2026", "France Football maakt de genomineerden bekend"),
    ("28 september 2026", "Stemming van de jury sluit"),
    ("26 oktober 2026, 19.00 uur", "Rode loper in Londen, live via DAZN en ballondor.com"),
    ("26 oktober 2026, 21.00 uur", "Start van de ceremonie in het London Palladium"),
])}
<h3><strong>Wie zijn de favorieten voor de Ballon d'Or 2026?</strong></h3>
<p>De stemming is al gesloten, dus het is nu wachten op de envelop. Op basis van prestaties, prijzen en de consensus onder kenners komen wij op deze rangorde:</p>
<ol><li><strong>Harry Kane ({a(BAY, 'Bayern München')}, Engeland).</strong> Het seizoen van zijn leven: {KANE_BAYERN} goals in 51 wedstrijden voor Bayern en {KANE_TOTAAL} in totaal met Engeland erbij. Landskampioen, bekerwinnaar, topscorer van de Bundesliga en winnaar van de Gouden Schoen. Op het WK scoorde hij zes keer en werd Engeland derde, het beste resultaat sinds 1966.</li><li><strong>Lamine Yamal ({a(BAR, 'FC Barcelona')}, Spanje).</strong> Wereldkampioen, landskampioen en speler van het seizoen in LaLiga, met 16 goals en 11 assists in 28 competitieduels. Een blessure hield hem vanaf april een tijd aan de kant en op het WK scoorde hij één keer. Vorig jaar werd hij tweede.</li><li><strong>Kylian Mbappé ({a(RMA, 'Real Madrid')}, Frankrijk).</strong> Topscorer van het WK met tien goals en topscorer van de Champions League, één goal meer dan Kane. Maar Real Madrid won geen grote prijs en Frankrijk werd vierde.</li><li><strong>Rodri ({a(MCI, 'Manchester City')}, Spanje).</strong> Winnaar van de Gouden Bal als beste speler van het WK en de motor van het Spaanse elftal. Zijn clubseizoen was wisselvallig.</li><li><strong>Lionel Messi ({a(MIA, 'Inter Miami')}, Argentinië).</strong> Acht goals en de Zilveren Bal op het WK, verloren finale. Op zijn 39e een outsider, maar de achtvoudig winnaar valt nooit helemaal af te schrijven.</li><li><strong>Michael Olise (Bayern München, Frankrijk).</strong> Uitgeroepen tot beste speler van de Bundesliga en een van de beste aangevers van Europa. Op het WK werd hij met Frankrijk vierde.</li><li><strong>Vitinha, Dembélé en Kvaratskhelia ({a(PSG, 'Paris Saint-Germain')}).</strong> PSG won voor de tweede keer op rij de Champions League en heeft negen spelers op de lijst. Die stemmen vallen waarschijnlijk uiteen over meerdere spelers, waardoor er geen PSG'er boven Kane en Yamal uitkomt.</li></ol>"""

content2 = f"""<h3><strong>Wat zegt de markt over de Ballon d'Or 2026?</strong></h3>
<p>Volgens de internationale markt is <strong>Harry Kane favoriet</strong>. Omgerekend krijgt hij een winkans van rond de 65 procent. Lamine Yamal staat duidelijk tweede: begin oktober nam hij de favorietenrol even over, maar halverwege de maand schoof Kane weer naar voren. Daarachter is het gat groot. Mbappé, Messi en Rodri worden internationaal gezien als outsiders met hooguit een paar procent kans. Let wel: dit zijn buitenlandse noteringen, die je in Nederland niet legaal kunt spelen. Verderop lees je waarom.</p>
<h3><strong>Harry Kane of Lamine Yamal: de cijfers naast elkaar</strong></h3>
{tabel(["", "Harry Kane", "Lamine Yamal"], [
    ("<strong>Club</strong>", "Bayern München", "FC Barcelona"),
    ("<strong>Leeftijd</strong>", "33", "19"),
    ("<strong>Competitie</strong>", "36 goals en 5 assists in 31 duels", "16 goals en 11 assists in 28 duels"),
    ("<strong>Totaal club</strong>", f"{KANE_BAYERN} goals in 51 duels", "Rond de 24 goals in alle competities"),
    ("<strong>Prijzen club</strong>", "Bundesliga, DFB-Pokal en Supercup", "LaLiga"),
    ("<strong>Champions League</strong>", "14 goals, halve finale (uitgeschakeld door PSG)", "Barcelona haalde de finale niet"),
    ("<strong>WK 2026</strong>", "6 goals, Engeland derde", "1 goal, wereldkampioen"),
    ("<strong>Individueel</strong>", "Gouden Schoen, topscorer Bundesliga", "Speler van het seizoen LaLiga"),
])}
<h3><strong>Onze voorspelling: wie wint de Ballon d'Or 2026?</strong></h3>
<p>Wij gaan voor <strong>Harry Kane</strong>. Het eerste criterium van de jury is de individuele prestatie, en niemand haalde in 2025/26 zijn niveau: {KANE_TOTAAL} goals voor club en land, drie prijzen met Bayern en een WK waarin hij Engeland naar de halve finale schoot. Kane zou de eerste Engelse winnaar worden sinds Michael Owen in 2001.</p>
<p>Toch is Yamal een serieus risico voor die voorspelling. Een wereldtitel weegt bij journalisten traditioneel zwaar, hij werd al tweede in 2025 en hij was de beste speler van de Spaanse kampioen. Daar staat tegenover dat hij een deel van het seizoen miste en op het WK weinig beslissende cijfers liet zien. Een verrassing van Mbappé, de topscorer van zowel het WK als de Champions League, sluiten we niet uit, maar zonder grote prijs is dat lastig.</p>
<h3><strong>De 30 genomineerden voor de Ballon d'Or 2026</strong></h3>
<p>France Football maakte de lijst op 8 september bekend. Paris Saint-Germain levert met {N_PSG} spelers de grootste groep, gevolgd door Bayern München met vier. Opvallend is de Mexicaan Julián Quiñones, spits van het Saoedische Al-Qadsiah. Bij spelers die deze zomer verhuisden, zoals Rodri, Ferran Torres en Marc Cucurella, staat hieronder de club waar ze het beoordeelde seizoen speelden.</p>
{tabel(["Speler", "Land", "Club 2025/26"], GENOMINEERDEN)}
<h3><strong>Staan er Nederlanders op de lijst?</strong></h3>
<p>Bij de mannen niet: er staat geen Nederlander tussen de 30 genomineerden. Bij de vrouwen wel. Op de lijst voor de Ballon d'Or Féminin staan <strong>Esmee Brugts</strong> (Barcelona), <strong>Kerstin Casparij</strong> (Manchester City) en <strong>Vivianne Miedema</strong> (Manchester City). Daarnaast maakt verdediger <strong>Veerle Buurman</strong> (Chelsea) kans op de Kopa-trofee voor het beste jonge talent. Ook historisch heeft Nederland een sterke band met de prijs: Johan Cruijff en Marco van Basten wonnen hem allebei drie keer, Ruud Gullit één keer.</p>
<h3><strong>De genomineerden voor de Ballon d'Or Féminin</strong></h3>
<p>Ook bij de vrouwen zijn er dertig kandidaten. Opvallend: Aitana Bonmatí, die de prijs de afgelopen drie jaar won, staat er dit keer niet tussen. De Nederlandse kandidaten zijn vetgedrukt: {", ".join(VROUWEN)}.</p>"""

content3 = f"""<h3><strong>Welke prijzen worden er nog meer uitgereikt?</strong></h3>
<p>Naast de twee Gouden Ballen worden op 26 oktober ook een reeks bijprijzen uitgereikt, steeds voor mannen en vrouwen.</p>
{tabel(["Prijs", "Waarvoor", "Kanshebbers 2026", "Winnaar 2025"], [
    ("<strong>Kopa-trofee</strong>", "Beste speler onder 21 jaar", "10 mannen (onder wie Yamal, Cubarsí en Zaïre-Emery), 5 vrouwen (onder wie Veerle Buurman)", "Lamine Yamal / Vicky López"),
    ("<strong>Yashin-trofee</strong>", "Beste keeper", "Onder anderen Courtois, Raya, Joan García en Unai Simón; bij de vrouwen onder anderen Hampton en Berger", "Gianluigi Donnarumma / Hannah Hampton"),
    ("<strong>Gerd Müller-trofee</strong>", "Topscorer van het seizoen", "Geen shortlist; Kane is met 73 goals de logische kandidaat", "Viktor Gyökeres / Ewa Pajor"),
    ("<strong>Johan Cruijff-trofee</strong>", "Trainer van het jaar", "Arteta, De la Fuente, Emery, Kompany en Luis Enrique; bij de vrouwen onder anderen Giráldez en Romeu", "Luis Enrique / Sarina Wiegman"),
    ("<strong>Club van het jaar</strong>", "Beste club", f"{a(ARS, 'Arsenal')}, Bayern München, Bodø/Glimt, Flamengo en PSG; bij de vrouwen onder anderen Barcelona en OL Lyonnes", "Paris Saint-Germain / Arsenal"),
    ("<strong>Sócrates-prijs</strong>", "Maatschappelijke inzet", "Geen shortlist", "Xana Foundation"),
])}
<h3><strong>Hoe werkt de stemming voor de Ballon d'Or?</strong></h3>
<p>De winnaar wordt gekozen door een internationale jury van journalisten: één per land. Bij de mannen komen de juryleden uit de honderd hoogst geplaatste landen op de FIFA-ranking, bij de vrouwen uit de top vijftig. Elk jurylid kiest uit de dertig genomineerden een top tien en deelt daar punten aan uit. Per stembrief zijn dat {PER_STEMBRIEF} punten, dus met {JURY} juryleden kan een speler maximaal {MAX_PUNTEN:,} punten halen. Ter vergelijking: Dembélé won vorig jaar met 1.380 punten.</p>
{tabel(["Plek op de stembrief", "Punten"], [(f"{i}", f"{p}") for i, p in enumerate(PUNTEN, 1)])}
<p>De jury beoordeelt in deze volgorde:</p>
<ul><li><strong>Individuele prestaties</strong>, met nadruk op beslissende en indrukwekkende optredens.</li><li><strong>Prestaties van het team</strong> en gewonnen prijzen, bij club en land.</li><li><strong>Klasse en fair play.</strong></li></ul>
<p>Eindigen twee spelers met evenveel punten, dan wint wie de meeste eerste plaatsen kreeg, daarna telt het aantal tweede plaatsen, enzovoort. De stemming voor 2026 sloot op 28 september en de uitslag blijft geheim tot de avond zelf.</p>
<h3><strong>Winnaars van de Ballon d'Or 2021 tot en met 2025</strong></h3>
{tabel(["Jaar", "Mannen", "Vrouwen"], [
    ("2025", "Ousmane Dembélé (Paris Saint-Germain)", "Aitana Bonmatí (FC Barcelona)"),
    ("2024", "Rodri (Manchester City)", "Aitana Bonmatí (FC Barcelona)"),
    ("2023", "Lionel Messi (Paris Saint-Germain / Inter Miami)", "Aitana Bonmatí (FC Barcelona)"),
    ("2022", "Karim Benzema (Real Madrid)", "Alexia Putellas (FC Barcelona)"),
    ("2021", "Lionel Messi (FC Barcelona / Paris Saint-Germain)", "Alexia Putellas (FC Barcelona)"),
])}
<p>Lionel Messi is met acht Gouden Ballen recordhouder, gevolgd door Cristiano Ronaldo met vijf. In 2020 werd de prijs niet uitgereikt vanwege de coronapandemie.</p>
<h3><strong>Kun je in Nederland op de Ballon d'Or wedden?</strong></h3>
<p><strong>Nee.</strong> Volgens het Besluit kansspelen op afstand mogen bookmakers met een Nederlandse vergunning alleen weddenschappen aanbieden op de uitslag van een sportwedstrijd of op gebeurtenissen tijdens een sportwedstrijd. De Ballon d'Or is geen wedstrijd, maar een stemming door journalisten. De Kansspelautoriteit heeft in maart 2026 nog eens uitdrukkelijk laten weten dat weddenschappen op prijsverkiezingen, zoals een MVP-prijs, buiten de vergunning vallen, net als weddenschappen op transfers en politieke verkiezingen. Legale aanbieders die zulke markten toch aanboden, moesten ze direct offline halen.</p>
<p>Zie je ergens toch een Ballon d'Or-markt, dan gaat het om een aanbieder zonder Nederlandse vergunning. Dat is illegaal, en bij een conflict over je uitbetaling sta je met lege handen. Lees <a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je herkent of een bookmaker legaal is</a>. Het is overigens niet de enige markt die in Nederland verboden is: ook op kaarten en corners mag je niet wedden, zoals we uitleggen in <a href="{CORNERS}">waarom wedden op corners niet legaal is</a>.</p>
<p>Wil je toch iets met de kandidaten doen? Wedden op hun wedstrijden mag wel. Denk aan Kane met Bayern of Yamal met Barcelona in de {a(CL, 'Champions League')}. In onze <a href="/voorbeschouwingen">voorbeschouwingen</a> lees je per duel wat je kunt verwachten en op onze pagina met <a href="/wedtips">wedtips</a> vind je dagelijks onze voorspellingen. Speel wel met een vast budget; tips daarvoor vind je bij <a href="/speel-bewust/verantwoord-wedden">verantwoord wedden</a>.</p>
<h3><strong>Veelgestelde vragen over de Ballon d'Or 2026</strong></h3>
<p><strong>Wanneer is de Ballon d'Or 2026 uitreiking?</strong><br>Op maandag 26 oktober 2026 in het London Palladium in Londen. Het is de eerste keer dat de uitreiking buiten Parijs plaatsvindt.</p>
<p><strong>Hoe laat is de Ballon d'Or 2026?</strong><br>De ceremonie begint om 21.00 uur Nederlandse tijd (20.00 uur in Londen). De rode loper is vanaf 19.00 uur live te zien. De winnaar bij de mannen wordt meestal als laatste bekendgemaakt, laat op de avond.</p>
<p><strong>Waar kan ik de Ballon d'Or kijken?</strong><br>Gratis live via DAZN, met een gratis account, en via de livestream op ballondor.com. Een Nederlandse tv-zender is voor 2026 niet aangekondigd.</p>
<p><strong>Wie heeft de Ballon d'Or 2026 gewonnen?</strong><br>Dat is nog niet bekend. De winnaar wordt op maandagavond 26 oktober bekendgemaakt. Harry Kane en Lamine Yamal zijn de grootste kanshebbers.</p>
<p><strong>Wie is favoriet voor de Ballon d'Or 2026?</strong><br>Harry Kane. Volgens de internationale markt heeft hij ongeveer twee derde kans, met Lamine Yamal als duidelijke nummer twee. Ook wij verwachten dat Kane wint.</p>
<p><strong>Maakt Lamine Yamal kans op de Ballon d'Or 2026?</strong><br>Zeker. Hij werd wereldkampioen met Spanje, landskampioen met Barcelona en vorig jaar al tweede. Hij is de enige echte bedreiging voor Kane.</p>
<p><strong>Kun je in Nederland op de Ballon d'Or wedden?</strong><br>Nee. Legale bookmakers mogen alleen weddenschappen op sportwedstrijden aanbieden, en de Kansspelautoriteit noemt prijsverkiezingen uitdrukkelijk als niet toegestaan. Wedden op de wedstrijden van de kandidaten mag wel.</p>
<p><strong>Hoe werkt de stemming?</strong><br>Honderd journalisten, één per land uit de top 100 van de FIFA-ranking, kiezen elk een top tien uit dertig genomineerden. De nummer één krijgt 15 punten, de nummer tien 1 punt. Wie de meeste punten heeft, wint.</p>
<p><strong>Welke Nederlanders zijn genomineerd?</strong><br>Bij de mannen geen. Bij de vrouwen Esmee Brugts, Kerstin Casparij en Vivianne Miedema, en voor de Kopa-trofee Veerle Buurman.</p>
{KSA}"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    html = content + content2 + content3
    assert not re.search(r"<(ul|ol|/li)>\s+<", html), "witruimte tussen lijsttags"
    assert "/kennisbank/" not in html and "<h2" not in html
    assert html.rstrip().endswith(KSA)
    assert len(TITEL) <= 60 and "Ballon d'Or 2026" in TITEL
    assert 120 <= len(SAMENVATTING) <= 155
    assert len(OG_CHIPS) == 2 and len(OG_DATA) == 4 and OG_MOTIEF in ("lijst", "tabel")
    tekst = re.sub(r"<[^>]+>", " ", html)
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", len(tekst.split()), "woorden")
    if "--live" in sys.argv:   # NIET uitvoeren zonder akkoord van Jasper
        import lk_webflow as WF
        fd = {"name": TITEL, "content": content, "content-2": content2, "content-3": content3,
              "samenvatting": SAMENVATTING, "publicatiedatum": datetime.now(timezone.utc).isoformat()}
        print("item:", WF.update_live(ITEM_ID, fd))
