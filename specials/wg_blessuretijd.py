# -*- coding: utf-8 -*-
"""NIEUW wedgids-artikel (Nieuws, nog geen item): blessuretijd in het voetbal, hoe de extra tijd wordt bepaald.
Slug blessuretijd-voetbal-extra-tijd-uitgelegd (gaf HTTP 404 op 10-11-2026, dus vrij). Rubriek Speluitleg,
wedgids-categorie 'Sporten en regels'. Onderwerp: Engelstalige analysesite (alleen het onderwerp, niets overgenomen).
Zoekwoorden: 'blessuretijd voetbal' (hoofd), 'extra tijd voetbal', 'hoe wordt blessuretijd bepaald', 'wie bepaalt
blessuretijd', 'blessuretijd weddenschap' / 'telt blessuretijd mee', 'minimale extra speeltijd', 'vierde official bord'.

Feiten (bron + datum, alles nagelopen op 10-11-2026):
- IFAB Laws of the Game, Law 7 (theifab.com/laws/latest/the-duration-of-the-match, 2026/27): 2 × 45 minuten; extra tijd
  voor tijdverlies door wissels, beoordelen/afvoeren van geblesseerde spelers, tijdrekken, disciplinaire straffen, medische
  onderbrekingen die de competitie toestaat (drinkpauze max. 1 minuut, cooling break 90 sec. tot 3 min.), VAR-checks en
  -reviews, doelpuntvieringen en elke andere oorzaak (o.a. vertraagde hervatting, ingrijpen van buitenaf). De vierde official
  toont de MINIMALE extra tijd, door de scheidsrechter bepaald aan het eind van de laatste minuut van elke helft; die mag
  door de scheidsrechter worden verhoogd, niet verlaagd. Een fout in de tijdwaarneming in de eerste helft wordt niet in de
  tweede helft gecompenseerd. Wordt een strafschop genomen of overgenomen, dan duurt de helft tot die is afgerond.
  Law 7 zegt NIETS over het laten afmaken van een aanval -> in de tekst: 'de regels schrijven dat niet voor'.
- IFAB Law 14 (theifab.com/laws/latest/the-penalty-kick, 10-11-2026): bij een strafschop na afloop van de tijd is de
  strafschop afgerond als de bal stil ligt, uit het spel gaat, door een andere speler dan de verdedigende keeper (ook de
  nemer) wordt gespeeld, of de scheidsrechter fluit voor een overtreding van het nemende team.
- KNVB 'Spelregels 2026/'27, spelregelwijzigingen en toelichtingen' (knvb.nl/downloads/bestand/29991/spelregels, datum
  1 juni 2026) + IFAB-nieuws 28-02-2026 (theifab.com/news/the-ifab-introduces-further-measures-to-improve-match-flow-and-
  player-behaviour; 140e AGM, ingang 1 juli 2026): wisselspeler moet binnen 10 seconden van het veld (anders invaller pas
  bij eerste onderbreking na 1 minuut); speler die op het veld is beoordeeld/behandeld moet het veld verlaten en 1 minuut
  (doorlopende klok) na hervatting wachten, met uitzonderingen (o.a. keeper, ernstige hoofdblessure, overtreding met
  gele/rode kaart); visueel aftellen van 5 seconden bij vertraagde inworp (-> inworp tegenpartij) en doelschop
  (-> hoekschop tegenpartij).
- 8-secondenregel keeper (theifab.com/news/the-ifab-tackles-goalkeeper-time-wasting; ingang 1 juli 2025): keeper die de bal
  langer dan 8 seconden vasthoudt (5 sec. visueel afgeteld) -> hoekschop voor de tegenstander.
- KNVB-nieuws 25-06-2024 (knvb.nl/node/69348): doorlopende stadionklok in het betaald voetbal vanaf 2024/'25; klok bleef
  eerder op 45 en 90 staan; speaker/scorebord melden 'minimale extra speeltijd'.
- FIFA, 30-11-2022 (inside.fifa.com/en/refereeing/news/collina-weve-asked-referees-to-calculate-stoppage-time-more-
  accurately): Collina: gemiddeld ongeveer 10 minuten extra tijd op het WK 2022 tegen ongeveer 6,5 minuten in 2018;
  gemiddeld bijna 59 minuten effectieve speeltijd; Engeland - Iran 23 minuten extra (andere media: 27) -> in de tekst
  'ruim twintig minuten' (twee bronnen bevestigen >20).
- Premier League, 25-04-2024 (premierleague.com/news/3978045): gemiddelde extra tijd per wedstrijd 7:29 (2021/22),
  8:27 (2022/23), 11:39 (2023/24). Opta Analyst 12-10-2023 (theanalyst.com/articles/football-time-keeping-and-time-
  wasting-measures): in de vier hoogste Engelse divisies tikt de klok gemiddeld voorbij de 100 minuten; aanpak 'in lijn met
  de recentste IFAB-richtlijnen'.
- Bookmakers: TOTO klantenservice 'Spelregels bij verlenging' (toto.nl/klantenservice/spelregels-bij-verlenging, curl
  10-11-2026): 'Bij bijna alle wedopties telt alleen wat er binnen 90 minuten + blessuretijd gebeurt', behalve wedopties
  waarbij TOTO dat vooraf aangeeft (o.a. 'To qualify'). Unibet Algemene Voorwaarden Sportsbook 'Versie 2.2', 'September
  2026' (Kambi Rules v2.2 NL.pdf via unibet.nl/general-info/terms, gedownload 10-11-2026): A 1.1 'Fulltime' bij voetbal =
  '90 minuten inclusief blessuretijd'; regel over tijdvakken (voorbeeld 60:00-89:59): blessuretijd telt NIET mee tenzij
  vermeld; 'Blessuretijd' = het door de official aangegeven aantal minuten. bet365: help.bet365.nl sportregels voetbal
  (nagelezen 22-10-2026, zie docstring wg_doelpuntenmaker.py): wedstrijdmarkten na 90 minuten, exclusief verlenging en
  strafschoppenreeks, tenzij anders aangegeven.
- Regeling kansspelen op afstand, Bijlage 2, Voetbal (wetten.overheid.nl/BWBR0044767/2026-04-01, gelezen 10-11-2026):
  verboden o.a. s. 'toevoegen van extra tijd door de vierde official per wedstrijd en per helft', p. blessurebehandelingen,
  r. inbrengen van wisselspelers, t. VAR-momenten -> in de tekst: daarop kun je in Nederland niet wedden.
Voorbeeld van de opbouw van de extra tijd is FICTIEF (gemarkeerd); de spelregels kennen geen vaste tijd per gebeurtenis.
Alle getallen hieronder berekend en ge-assert.

Bewust weggelaten:
- Geen Eredivisie-gemiddelden voor extra tijd: geen openbare, bruikbare bron gevonden.
- Geen gemiddelden voor de Premier League na 2023/24 (niet nagelezen) en geen claims over 'records' in de blessuretijd.
- Geen namen van scheidsrechters, geen echte omstreden incidenten; WK 2022 alleen met cijfers van FIFA zelf.
- Geen bron van het onderwerp genoemd; geen concurrent- of affiliatesites.
Interne links gecontroleerd op 10-11-2026 (curl, allemaal HTTP 200): zie de asserts onderaan.
Geen INFOGRAPHIC (de tabellen volstaan).
  ../superodd-agent/.venv/bin/python specials/wg_publiceer.py blessuretijd [--live]"""
import os, sys, re
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
import lk_webflow as WF
from legaal_data import tabel

ITEM_ID = None   # nieuw artikel
SLUG = "blessuretijd-voetbal-extra-tijd-uitgelegd"
RUBRIEK = "6502b66cd9992658b4037cf5"   # Speluitleg
WEDGIDS_CAT = "Sporten en regels"
TITEL = "Blessuretijd in het voetbal: hoe wordt extra tijd bepaald?"
SAMENVATTING = ("Hoe bepaalt de scheidsrechter de blessuretijd? Waarvoor tijd wordt bijgeteld, wat het bord van de vierde "
                "official betekent en wat telt voor je weddenschap.")

OG_KOP = "Hoe werkt <span>blessuretijd</span>?"
OG_EYEBROW = "Spelregels voetbal"
OG_CHIPS = ["Regel 7 uitgelegd", "Telt mee bij 1X2"]
OG_MOTIEF = "tabel"
OG_DATA = ["Bord · minimale extra tijd", "Wissels en VAR · tellen mee", "Verlenging · telt niet bij 1X2",
           "WK 2022 · gemiddeld ±10 min"]

GESTAAKT = "/nieuws/wedstrijd-gestaakt-wat-gebeurd-er-nu-met-je-weddenschap"
VERLENGING = "/nieuws/weddenschap-bij-bet365-als-een-wedstrijd-naar-verlenging-gaat-zo-werkt-het"
NIEUWE_REGELS = "/nieuws/nieuwe-spelregels-eredivisie-2026-27-alles-wat-je-moet-weten-op-een-rijtje"
DRINKPAUZES = "/nieuws/drinkpauzes-wk-2026-regels-timing-impact-op-wedstrijden"
CORNERS = "/nieuws/dit-is-waarom-wedden-op-corners-niet-meer-legaal-is-in-nederland"
OVER_UNDER = "/nieuws/over-under-uitleg-over-2-5-goals"
BTTS = "/nieuws/beide-teams-scoren-btts-betekenis"
LIVE = "/nieuws/uitleg-in-play-live-wedden-dynamiek-strategie-en-kansen-in-realtime"
KANS = "/nieuws/kans-berekenen-uit-odds-impliciete-kans"
XG = "/nieuws/wat-is-xg-expected-goals"
WISSELS = "/nieuws/wisselregels-voetbal-hoeveel-wissels"   # zusterartikel, nog niet live -> NIET linken tot het live staat
VERANTWOORD = "/speel-bewust/verantwoord-wedden"
LINKS = (GESTAAKT, VERLENGING, NIEUWE_REGELS, DRINKPAUZES, CORNERS, OVER_UNDER, BTTS, LIVE, KANS, XG, VERANTWOORD, "/wedgids")


def mmss(sec):
    return f"{sec // 60}:{sec % 60:02d}"


def pct(x):
    return f"{100 * x:.0f}%"


# ---- fictief voorbeeld: zo loopt de tijd op in de tweede helft ----
VOORBEELD = [
    ("Vier wisselmomenten (samen), elk ongeveer een halve minuut", 4 * 30),
    ("Een speler wordt op het veld behandeld en van het veld gebracht", 90),
    ("VAR-check bij een doelpunt", 75),
    ("Doelpuntviering", 45),
    ("Tijdrekken bij een vrije trap en een doelschop", 30),
]
TOTAAL = sum(s for _, s in VOORBEELD)
assert TOTAAL == 360 and mmss(TOTAAL) == "6:00"
NA_BORD = [("Wissel in de extra tijd", 30), ("Nieuwe blessurebehandeling in de extra tijd", 60)]
TOTAAL2 = TOTAAL + sum(s for _, s in NA_BORD)
assert mmss(TOTAAL2) == "7:30" and sum(s for _, s in NA_BORD) == 90

# ---- Premier League, gemiddelde extra tijd per wedstrijd (premierleague.com, 25-04-2024) ----
PL = [("2021/22", 7 * 60 + 29), ("2022/23", 8 * 60 + 27), ("2023/24", 11 * 60 + 39)]
STIJGING = PL[2][1] - PL[1][1]
assert mmss(STIJGING) == "3:12" and pct(PL[2][1] / PL[1][1] - 1) == "38%" and pct(PL[2][1] / PL[0][1] - 1) == "56%"

content = f"""<p><strong>Blessuretijd is de speeltijd die de scheidsrechter aan het eind van elke helft bijtelt voor tijd die verloren ging aan wissels, blessures, VAR-checks, doelpuntvieringen, tijdrekken en andere onderbrekingen. De scheidsrechter bepaalt hoeveel, de vierde official laat het zien op het bord. Dat getal is een minimum: de scheidsrechter mag langer laten spelen, maar niet korter.</strong></p>
<p>De officiële term is 'extra tijd' of 'toegevoegde tijd'. In Nederland zeggen we bijna altijd blessuretijd, ook al gaat het om veel meer dan blessures. Hieronder lees je wat de spelregels precies zeggen, waarom de extra tijd sinds het WK 2022 langer is geworden en wat blessuretijd betekent voor je weddenschap.</p>
<h3><strong>Wat zeggen de spelregels over blessuretijd?</strong></h3>
<p>De spelregels van het voetbal worden wereldwijd vastgesteld door de IFAB, de internationale spelregelcommissie. De KNVB neemt die regels over. Over de duur van een wedstrijd gaat Regel 7. Een wedstrijd duurt twee helften van 45 minuten. Aan het eind van elke helft telt de scheidsrechter de tijd bij die tijdens die helft verloren is gegaan.</p>
<p>De scheidsrechter is de officiële tijdwaarnemer. Het stadionklokje en de klok op tv zijn alleen een hulpmiddel. Daarom kan een wedstrijd ook na '90+5' op de klok nog doorgaan, als de scheidsrechter vindt dat er nog tijd te goed is.</p>
<h3><strong>Waarvoor telt de scheidsrechter tijd bij?</strong></h3>
<p>Regel 7 noemt deze oorzaken van tijdverlies:</p>
<ul><li><strong>Wissels:</strong> elke wissel kost tijd, zeker als een speler langzaam van het veld loopt.</li><li><strong>Blessures:</strong> het beoordelen van een geblesseerde speler en hem van het veld halen.</li><li><strong>Tijdrekken:</strong> bijvoorbeeld een keeper die een doelschop rekt of een speler die de bal wegtrapt na een fluitsignaal.</li><li><strong>Kaarten:</strong> de tijd die het geven van een gele of rode kaart kost.</li><li><strong>Medische pauzes:</strong> drinkpauzes (maximaal één minuut) en cooling breaks bij hitte (anderhalve tot drie minuten), als de competitie die toestaat. Meer daarover lees je in ons artikel over <a href="{DRINKPAUZES}">drinkpauzes</a>.</li><li><strong>VAR:</strong> checks en reviews van de videoscheidsrechter.</li><li><strong>Doelpuntvieringen:</strong> de tijd tussen een doelpunt en de aftrap.</li><li><strong>Overige oorzaken:</strong> elke andere flinke vertraging, zoals een supporter of voorwerp op het veld.</li></ul>
<p>De spelregels geven geen vaste tijd per gebeurtenis. Er staat nergens dat een wissel dertig seconden waard is. De scheidsrechter houdt zelf bij hoeveel tijd er echt verloren ging, vaak met hulp van de vierde official.</p>
<h3><strong>Rekenvoorbeeld: zo komt het bord op zes minuten</strong></h3>
<p>Stel: in de tweede helft van een Eredivisie-wedstrijd gebeurt het volgende. <em>Dit voorbeeld en de tijden zijn fictief.</em></p>
{tabel(["Gebeurtenis", "Verloren tijd"], [(s, mmss(t)) for s, t in VOORBEELD] + [("<strong>Totaal</strong>", f"<strong>{mmss(TOTAAL)}</strong>")])}
<p>In de laatste minuut van de helft geeft de scheidsrechter het getal door aan de vierde official, en die steekt het bord op: <strong>+{TOTAAL // 60}</strong>. Valt er in die extra tijd opnieuw tijd weg, bijvoorbeeld door een wissel en een nieuwe blessure, dan telt de scheidsrechter die er gewoon bij. In dit voorbeeld komen er {sum(s for _, s in NA_BORD)} seconden bij, dus wordt er ongeveer zevenenhalve minuut extra gespeeld in plaats van {TOTAAL // 60}. Daarom zie je soms dat er langer wordt doorgespeeld dan het bord aangaf.</p>"""

content2 = f"""<h3><strong>Wie bepaalt de blessuretijd en wat betekent het bord?</strong></h3>
<p>De scheidsrechter bepaalt de extra tijd. De vierde official, de official tussen de twee dug-outs, laat het getal zien op het elektronische bord. Volgens Regel 7 gebeurt dat aan het eind van de laatste minuut van elke helft.</p>
<p>Het getal op het bord is de <strong>minimale</strong> extra tijd. Daar gelden drie regels voor:</p>
<ul><li><strong>Langer mag:</strong> de scheidsrechter mag de extra tijd verlengen, bijvoorbeeld als er tijdens de blessuretijd opnieuw tijd verloren gaat.</li><li><strong>Korter mag niet:</strong> staat er +4 op het bord, dan wordt er minstens vier minuten gespeeld.</li><li><strong>Geen compensatie:</strong> heeft de scheidsrechter zich in de eerste helft vergist in de tijd, dan mag hij dat niet goedmaken door de tweede helft langer of korter te maken.</li></ul>
<p>In het Nederlandse betaald voetbal loopt de stadionklok sinds het seizoen 2024/25 door na 45 en 90 minuten. Eerder bleef de klok op 45:00 of 90:00 staan. De speaker en het scorebord melden er altijd bij dat het om de <em>minimale</em> extra speeltijd gaat.</p>
<h3><strong>Fluit de scheidsrechter precies op tijd af?</strong></h3>
<p>Niet altijd tot op de seconde. De scheidsrechter beslist zelf wanneer de tijd om is. De spelregels schrijven niet voor dat hij een aanval moet laten afmaken, en ook niet dat hij moet wachten tot de bal uit is. Veel scheidsrechters fluiten op een neutraal moment, maar dat is gewoonte, geen regel.</p>
<p>Er is één harde uitzondering. Wordt er een strafschop gegeven of overgenomen, dan duurt de helft tot die strafschop is genomen. Ook als de tijd intussen voorbij is. Daarna mag alleen de keeper de bal nog raken. Speelt een andere speler de bal, ook de nemer zelf, dan is de helft voorbij: een rebound binnenschieten telt dan niet. Gaat de bal via de keeper, de paal of de lat vanzelf het doel in, dan telt het doelpunt wel.</p>
<p>Verder geldt: een doelpunt telt alleen als de bal helemaal over de lijn is voordat de scheidsrechter affluit. Zodra het eindsignaal klinkt, is de bal uit het spel.</p>
<h3><strong>Waarom duurt de blessuretijd tegenwoordig zo lang?</strong></h3>
<p>Op het WK 2022 in Qatar vroeg de FIFA aan scheidsrechters om de verloren tijd nauwkeuriger te berekenen, vooral bij wissels, blessures, VAR en doelpuntvieringen. Volgens Pierluigi Collina, de baas van de FIFA-scheidsrechters, kwam de extra tijd daardoor uit op gemiddeld ongeveer tien minuten per wedstrijd, tegen zo'n zesenhalve minuut op het WK 2018. Bij Engeland - Iran werd in totaal zelfs ruim twintig minuten bijgeteld, vooral door twee lange blessurebehandelingen.</p>
<p>Vanaf het seizoen 2023/24 namen onder meer de Engelse competities dezelfde aanpak over. In de Premier League groeide de gemiddelde extra tijd per wedstrijd zo:</p>
{tabel(["Seizoen", "Gemiddelde extra tijd per wedstrijd"], [(f"<strong>{s}</strong>", f"{mmss(t)} minuten") for s, t in PL])}
<p><em>Bron: Premier League, april 2024.</em> Dat is in één seizoen {mmss(STIJGING)} minuut (ongeveer {pct(PL[2][1] / PL[1][1] - 1)}) meer. Volgens Opta tikte de klok in de vier hoogste Engelse divisies in het begin van dat seizoen gemiddeld voorbij de 100 minuten.</p>
<p>Het doel is meer echte speeltijd, niet langere wedstrijden. Collina wees erop dat de bal op het WK 2022 gemiddeld bijna 59 minuten in het spel was. Wie tijd rekt, wint er weinig mee als die tijd er later gewoon bij komt.</p>
<h3><strong>Welke nieuwe regels moeten tijdrekken tegengaan?</strong></h3>
<p>De IFAB pakt tijdrekken ook direct aan. Deze regels gelden in Nederland, ook in de Eredivisie:</p>
{tabel(["Regel", "Sinds", "Wat er gebeurt"], [
    ("<strong>Keeper houdt de bal te lang vast</strong>", "2025/26", "Na 8 seconden (de laatste 5 telt de scheidsrechter zichtbaar af) krijgt de tegenstander een hoekschop"),
    ("<strong>Inworp vertragen</strong>", "2026/27", "Na een zichtbaar aftellen van 5 seconden gaat de inworp naar de tegenstander"),
    ("<strong>Doelschop vertragen</strong>", "2026/27", "Na een zichtbaar aftellen van 5 seconden krijgt de tegenstander een hoekschop"),
    ("<strong>Wissel rekken</strong>", "2026/27", "De speler moet binnen 10 seconden van het veld. Lukt dat niet, dan mag de invaller pas na een minuut erin"),
    ("<strong>Behandeling op het veld</strong>", "2026/27", "De speler moet van het veld en mag pas een minuut na de hervatting terug (met uitzonderingen, zoals voor de keeper)"),
])}
<p>Alle wijzigingen voor dit seizoen lees je in ons overzicht van de <a href="{NIEUWE_REGELS}">nieuwe spelregels in de Eredivisie</a>.</p>"""

content3 = f"""<h3><strong>Telt de blessuretijd mee voor je weddenschap?</strong></h3>
<p>Ja. Bij voetbal gaan de meeste weddenschappen over de reguliere speeltijd, en daar hoort de blessuretijd bij. Een doelpunt in de 90+7e minuut telt dus gewoon mee voor de 1X2, <a href="{OVER_UNDER}">over/under</a> en <a href="{BTTS}">beide teams scoren</a>. Wat niet meetelt, is de verlenging van 2 × 15 minuten en een strafschoppenserie.</p>
<p>Zo staat het bij legale bookmakers in de regels:</p>
<ul><li><strong>TOTO:</strong> bij bijna alle wedopties telt alleen wat er binnen 90 minuten plus blessuretijd gebeurt. Alleen bij wedopties waarbij TOTO vooraf aangeeft dat de verlenging meetelt, zoals 'to qualify' (wie gaat door), is dat anders.</li><li><strong>Unibet:</strong> 'fulltime' is bij voetbal 90 minuten inclusief blessuretijd. Let op: bij een weddenschap op een tijdvak, zoals de uitslag tussen 60:00 en 89:59, telt de blessuretijd juist niet mee, tenzij dat erbij staat.</li><li><strong>bet365:</strong> wedstrijdmarkten gaan over de 90 minuten, zonder verlenging en strafschoppen, tenzij er iets anders bij staat.</li></ul>
<p>Gaat een bekerwedstrijd naar de verlenging? Lees dan <a href="{VERLENGING}">wat er met je weddenschap gebeurt bij een verlenging</a>. Wordt een wedstrijd stilgelegd en niet uitgespeeld, dan gelden weer andere regels: zie <a href="{GESTAAKT}">wedstrijd gestaakt, wat gebeurt er met je weddenschap</a>.</p>
<p>Kun je wedden op hoeveel minuten er wordt bijgeteld? In Nederland niet. De extra tijd die de vierde official aangeeft, staat net als wissels, blessurebehandelingen en VAR-momenten op de lijst van verboden weddenschappen, omdat zulke gebeurtenissen makkelijk te beïnvloeden zijn. Dezelfde lijst verbiedt ook wedden op <a href="{CORNERS}">corners en kaarten</a>.</p>
<p>Wed je live, dan veranderen de odds in de blessuretijd snel: elke minuut die wegtikt, maakt een extra doelpunt minder waarschijnlijk. Staat er +7 op het bord, dan is er nog meer tijd over dan de '90' op de klok doet vermoeden. Hoe je zo'n kans vergelijkt met de odds, lees je in <a href="{KANS}">kans berekenen uit odds</a> en in onze uitleg over <a href="{LIVE}">live wedden</a>. Spreek vooraf een bedrag af en houd je eraan: <a href="{VERANTWOORD}">verantwoord wedden</a>.</p>
<p>Meer uitleg over spelregels en wedden vind je in de <a href="/wedgids">wedgids</a>, bijvoorbeeld wat <a href="{XG}">xG</a> zegt over de kansen die een team creëert.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wie bepaalt de blessuretijd?</strong><br>De scheidsrechter. De vierde official laat het getal alleen zien op het bord, aan het eind van de laatste minuut van elke helft.</p>
<p><strong>Is de blessuretijd op het bord precies?</strong><br>Nee, het is een minimum. De scheidsrechter mag langer laten spelen, bijvoorbeeld als er tijdens de extra tijd een wissel of blessure is, maar hij mag niet eerder affluiten.</p>
<p><strong>Waarom heet het blessuretijd als het niet alleen om blessures gaat?</strong><br>Dat is gewoon spreektaal. Officieel heet het extra tijd of toegevoegde tijd. Wissels, VAR-checks, doelpuntvieringen en tijdrekken tellen ook mee.</p>
<p><strong>Telt een doelpunt in de blessuretijd mee voor mijn weddenschap?</strong><br>Ja, bij weddenschappen op de reguliere speeltijd, zoals 1X2 en over/under, telt de blessuretijd mee. De verlenging en strafschoppen tellen niet mee, tenzij dat bij de markt staat.</p>
<p><strong>Mag de scheidsrechter eerder affluiten dan het bord aangeeft?</strong><br>Nee. De extra tijd mag worden verlengd, maar niet ingekort. Alleen bij een gestaakte wedstrijd, bijvoorbeeld door noodweer, eindigt een wedstrijd eerder.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    html = content + content2 + content3
    assert not re.search(r"<(ul|ol|/li)>\s+<", html) and "/kennisbank/" not in html and "<h2" not in html and "<h4" not in html
    assert html.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert content.startswith("<p><strong>") and "/go/" not in html and WISSELS not in html
    assert len(TITEL) <= 60 and TITEL.startswith("Blessuretijd") and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert len(OG_CHIPS) == 2 and len(OG_DATA) == 4 and html.count("<table") >= 3
    for link in LINKS:
        assert link in html, link
    for h in re.findall(r"<h3>(.*?)</h3>", html):
        assert h.startswith("<strong>") and h.endswith("</strong>"), h
    faq = content3.split("Veelgestelde vragen")[1]
    assert 4 <= faq.count("<p><strong>") <= 6
    tekst = re.sub(r"<[^>]+>", " ", html)
    woorden = len(tekst.split())
    assert 1200 <= woorden <= 2200, woorden
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", woorden, "woorden")
    if "--live" in sys.argv:   # NIET zelf draaien; alleen na akkoord (bij voorkeur via wg_publiceer.py blessuretijd --live)
        fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
              "samenvatting": SAMENVATTING, "rubriek": RUBRIEK, "wedgids": True,
              "publicatiedatum": datetime.now(timezone.utc).isoformat()}
        print("item:", WF.create_live(fd), "https://www.bet-experts.nl/nieuws/" + SLUG)
