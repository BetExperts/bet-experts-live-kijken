# -*- coding: utf-8 -*-
"""Herschrijving + samenvoeging wedgids-artikel (Nieuws, bestaand item 664e213e1f4179b085ea903b): wat is een walkover bij
tennis en wat gebeurt er met je weddenschap. Slug ongewijzigd (rankt op 'wat is een walkover bij tennis', 402 impressies,
positie 10,7). Voegt het concurrerende artikel /nieuws/walkover-tennis-dit-gebeurt-er-met-je-weddenschap-bij-een-walkover-
nederlandse-bookmakers (item 68fb844233a04ccd7123895b) hierin samen; dat item krijgt NA publicatie een 301 naar deze slug
(niet door dit script). Titel herstelt de typfout 'gebeurd'.
Beide oude versies op 22-10-2026 met curl gelezen: veel fouten (o.a. Circus 'First Set Rule', Unibet winnaar ongeldig,
LiveScoreBet als bookmaker, bet365 'Retirement Guarantee' als terugbetaling) -> alleen het onderwerp overgenomen.

Walkover-regels per bookmaker (eigen pagina's van de bookmaker; ingebouwde browser alleen lezen, geen cookie-, leeftijds-
of inlogklikken; curl waar de pagina zonder JavaScript leesbaar was):
- TOTO (22-10): toto.nl/klantenservice/tennisweddenschappen: 'Start een wedstrijd niet, bijvoorbeeld door een walkover? Dan
  worden alle wedopties op die wedstrijd ongeldig verklaard'; 'Begint een speler niet aan de wedstrijd? Dan worden
  spelergerelateerde wedopties, zoals aces, ongeldig verklaard'; Bet Builder: een selectie ongeldig (o.a. 'een speler zich
  terugtrekt voordat de wedstrijd begint') -> hele Bet Builder ongeldig. 'Nadere regels per sport' (pdf via
  toto.nl/deelnemersreglement, 'Geldig vanaf 23 september 2026'), h. 29 Tennis: walkover -> alle wedopties ongeldig;
  'Als een wedstrijd niet begint vanwege een walk-over, worden alle Bet Builder-selecties op die wedstrijd ongeldig
  verklaard'; dubbelspel: speler(s) vervangen voor aanvang -> alles ongeldig (h. padel/beachvolleybal-tekst; voor tennis
  enkelspel niet apart genoemd). Combi 1,00: toto.nl/klantenservice/wedstrijd-afgelast-of-gestaakt (02-12-2025, gelezen
  21-10 voor wg_tennis-opgave-hoofd.py). TOTO noemt GEEN regel voor de toernooiwinnaar als een speler niet start -> niet
  geclaimd.
- Unibet (22-10): 'Algemene Voorwaarden Sportsbook Versie 2.2, Laatst bijgewerkt: September 2026' (Kambi-pdf, gelinkt in
  unibet.nl/general-info/terms 9.3): B 5.4 'Alle wedaanbiedingen met betrekking tot de wedstrijden/evenementen die niet
  plaatsvinden of die worden toegekend via een walk-over-beslissing, worden ongeldig verklaard'; B 5.11 weddenschappen op
  deelnemers die niet aan een evenement deelnemen -> ongeldig; A 5: ongeldig = notering 1.00, meervoudige weddenschap blijft
  geldig; A 5.3 (iii): weddenschappen geplaatst na een terugtrekking die de deelnemer uitsluit -> nietig; B 3.22 Bet Builder
  met een ongeldige selectie -> geheel ongeldig; C 27.2 'Wedstrijd' = wie doorgaat, geldig bij minimaal een voltooide set;
  C 27.6 dubbelspel: een speler vervangen -> alles ongeldig.
- Zelfde Kambi-clausules (walk-over-beslissing + notering 1.00 + combi blijft geldig) op 22-10 met curl gevonden in de eigen
  voorwaarden van JACKS.NL (jacks.nl/sports-rules, versie 2.1 aug 2025), LeoVegas (leovegas.nl/voorwaarden, v1.6 sept
  2026), BetMGM (betmgm.nl/voorwaarden, v1.5 sept 2026), 711 (711.nl/voorwaarden-sportweddenschappen), Oranje Palace
  (oranjepalace.nl/nl/voorwaarden-sportweddenschappen), Betnation (betnation.nl/sportregels, v2.2 sept 2026). B 5.11 (niet
  deelnemen -> ongeldig) gevonden bij JACKS.NL, 711, Oranje Palace en Betnation. BetCity en Hommerson: walkover ongeldig
  volgens het onderzoek van 21-10 (wg_tennis-opgave-hoofd.py; BetCity ook club.betcity.nl/walkover-tennis); combi-1,00 bij
  Hommerson niet gevonden -> 'zie voorwaarden'.
- bet365 (22-10, ingebouwde browser): help.bet365.nl/s/nl-nl/sports/non-runners: 'Golf en tennis - Als een speler zich
  terugtrekt voor de start van de wedstrijd of het toernooi, is de selectie ongeldig'; terugtrekking tijdens wedstrijd of
  toernooi -> sportregels; combi: non-runner ongeldig, rest loopt door ('bij een drievoud wordt de weddenschap een dubbel').
  help.bet365.nl/s/nl-nl/sportsrules/tennis: geen aparte walkover-regel; 'Qualifier bereikt de finale': een lucky loser
  telt niet als qualifier; finalistenmarkten 'Non-runner, geen weddenschap'.
- Circus (22-10, support.circus.nl artikel 27376437604498 Tennis): geen aparte walkover-regel; 'Bij enkelspel, als een
  speler wordt vervangen, worden alle weddenschappen geannuleerd'; outright: speler die op geen enkel moment deelneemt ->
  geannuleerd. Combi 1,00 (Algemene Sportregels, 12-06-2026, gelezen 21-10).
- Vbet (22-10, vbet.nl/nl/help/177304/sportsbook-regels, ingebouwde browser): tennis: geen aparte walkover-regel; 'Een
  opgehouden, niet gespeelde of uitgestelde wedstrijd wordt ... slechts als niet gestart en geannuleerd/geretourneerd
  beschouwd als de wedstrijd of het evenement/de competitie wordt afgelast'; outright 'Niet gestart, geen weddenschap'.
  Combi: afgerekend op de overige selecties (21-10). -> in de tabel 'geen aparte regel'.
- One Casino (22-10, sb.onecasino.com/nl/pages/betting-rules, algemeen 2.1): evenement begint niet op de geplande datum ->
  alle weddenschappen vervallen, behalve al vastgestelde markten. Combi 1,00 (21-10).
- Holland Casino Online (wedregels 41 Tennis), ComeOn en 888 (betting-rules-tnc), Starcasino (Sportsbook regels v1.31),
  TonyBet (wedregels 27 Tennis): walk-over ongeldig volgens het onderzoek van 21-10 (wg_tennis-opgave-hoofd.py); combi 1,00
  bij ComeOn en 888 bevestigd, bij Holland Casino, Starcasino en TonyBet niet gevonden -> 'zie voorwaarden'. Op 22-10 niet
  opnieuw leesbaar met curl (JavaScript-pagina's).
- Bingoal (voorwaarden achter captcha/consent) en ZEbet (HTTP 530 op 21-10): niet in te zien -> 'zie voorwaarden'. Hard Rock
  Casino en Lucky7casino: geen sportsbook.
Begrippen (lucky loser, no-show) algemeen tennis; geen bron genoemd. Alle bedragen berekend en ge-assert; quoteringen fictief.
  ../superodd-agent/.venv/bin/python specials/wg_publiceer.py walkover        (dry run)
  python3 specials/wg_walkover.py [--live]"""
import os, sys, re
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
import lk_webflow as WF
from legaal_data import tabel, MERKEN

ITEM_ID = "664e213e1f4179b085ea903b"
SLUG = "wat-gebeurd-er-bij-een-walkover-met-een-tennisweddenschap"
TITEL = "Wat is een walkover bij tennis? Dit gebeurt er met je weddenschap"
SAMENVATTING = ("Wat is een walkover bij tennis? Een speler start niet en je weddenschap wordt ongeldig. Zo werkt het bij "
                "TOTO, bet365, Unibet en meer.")

OG_KOP = "Wat is een <span>walkover</span> bij tennis?"
OG_EYEBROW = "Regels per bookmaker"
OG_CHIPS = ["20 bookmakers vergeleken", "Combi telt 1,00"]
OG_MOTIEF = "logos"
OG_DATA = ["toto · Alle wedopties ongeldig", "bet365 · Selectie ongeldig", "unibet · Ongeldig, combi 1,00",
           "circus · Speler vervangen: ongeldig"]

SLUGS = {m: s for m, _, _, _, s in MERKEN}
assert SLUGS["BetCity"] is None and SLUGS["Holland Casino Online"] is None and SLUGS["TOTO en Winnitt"] == "toto"


def bm(naam, merk=None):
    s = SLUGS[merk or naam]
    return f'<a href="/bookmakers/{s}">{naam}</a>' if s else naam


def eur(x):
    return f"€{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def q(x):
    return f"{x:.2f}".replace(".", ",")


TOTO = bm("TOTO", "TOTO en Winnitt")
HOOFD = "/nieuws/tennisser-geeft-op-wat-zijn-de-regels-voor-je-weddenschap-bij-nederlandse-bookmakers"
ACCA = "/nieuws/uitleg-wedstrategie-accumulator-weddenschappen"
LIVE = "/nieuws/uitleg-in-play-live-wedden-dynamiek-strategie-en-kansen-in-realtime"
BB = "/nieuws/wat-is-een-bet-builder"

# ---- walkover-regels per bookmaker: (naam, merk in MERKEN, walkover, combi) ----
ONG, ONG1, V = "Ongeldig, inzet terug", "Telt als 1,00", "Zie voorwaarden"
REGELS = [
    ("TOTO", "TOTO en Winnitt", "Alle wedopties ongeldig", ONG1),
    ("bet365", "bet365", "Selectie ongeldig, inzet terug", "Rest loopt door"),
    ("Unibet", "Unibet", ONG, ONG1),
    ("BetCity", "BetCity", ONG, ONG1),
    ("JACKS.NL", "JACKS.NL", ONG, ONG1),
    ("LeoVegas", "LeoVegas", ONG, ONG1),
    ("BetMGM", "BetMGM", ONG, ONG1),
    ("711", "711", ONG, ONG1),
    ("Oranje Palace", "Oranje Palace", ONG, ONG1),
    ("Betnation", "Betnation", ONG, ONG1),
    ("Hommerson", "Hommerson", ONG, V),
    ("Circus", "Circus", "Geen aparte regel*", ONG1),
    ("Holland Casino Online", "Holland Casino Online", ONG, V),
    ("ComeOn", "ComeOn! en GetLucky", ONG, ONG1),
    ("888", "888", ONG, ONG1),
    ("Starcasino", "Starcasino", ONG, V),
    ("TonyBet", "TonyBet", ONG, V),
    ("One Casino", "One Casino en OneSports", ONG, ONG1),
    ("Vbet", "Vbet", "Geen aparte regel**", "Rest loopt door"),
    ("Bingoal", "Bingoal", V, V),
    ("ZEbet", "ZEbet en ZEturf", V, V),
]
assert all(m in SLUGS for _, m, *_ in REGELS) and len(REGELS) == 21 and REGELS[0][0] == "TOTO"
ONGELDIG = [n for n, _, w, _ in REGELS if w.startswith(("Ongeldig", "Alle", "Selectie"))]
assert len(ONGELDIG) == 17
RIJEN_REGELS = [(f"<strong>{bm(n, m)}</strong>", w, c) for n, m, w, c in REGELS]


def lijst(namen):
    namen = [bm(n, dict((a, b) for a, b, *_ in REGELS)[n]) for n in namen]
    return ", ".join(namen[:-1]) + " en " + namen[-1]


# ---- voorbeeld 1: enkele weddenschap (fictief) ----
INZET, ODD_A = 10, 1.60
assert eur(INZET * ODD_A) == "€16,00"

# ---- voorbeeld 2: combi van drie met een walkover (fictief) ----
C_VOET, C_TEN, C_DARTS = 1.80, 1.60, 2.10
C_VOL = C_VOET * C_TEN * C_DARTS
C_WO = C_VOET * 1.00 * C_DARTS
assert q(C_VOL) == "6,05" and eur(INZET * C_VOL) == "€60,48"
assert q(C_WO) == "3,78" and eur(INZET * C_WO) == "€37,80"

# ---- voorbeeld 3: Bet Builder op de wedstrijd met walkover (fictief) ----
BB_ODD = 3.40
BB_UIT = INZET  # een selectie ongeldig -> hele Bet Builder ongeldig -> inzet terug
assert eur(BB_UIT) == "€10,00" and eur(INZET * BB_ODD) == "€34,00"

content = f"""<p><strong>Een walkover bij tennis betekent dat een speler zich terugtrekt voordat de wedstrijd begint. Zijn tegenstander gaat dan zonder te spelen door naar de volgende ronde. Voor je weddenschap is het simpel: de wedstrijd is niet gespeeld, dus je weddenschap wordt ongeldig en je krijgt je inzet terug. Dat geldt voor de winnaar, sets, games en handicaps. Zit de wedstrijd in een combi, dan telt die selectie als quotering 1,00.</strong></p>
<p>Walkovers komen in het tennis vaak voor. Een speler raakt geblesseerd in de ronde ervoor, wordt ziek of stopt om een andere reden. Hieronder lees je wat een walkover precies is, hoe het verschilt van een opgave, een no-show en een lucky loser, en hoe {TOTO}, {bm("bet365")}, {bm("Unibet")} en andere legale bookmakers je weddenschap afhandelen.</p>
<h3><strong>Wat is een walkover bij tennis?</strong></h3>
<p>Bij een walkover wordt een wedstrijd niet gespeeld, omdat één speler niet aan de start komt. In het schema staat dan vaak 'w.o.' achter de naam van de winnaar. Hij gaat door naar de volgende ronde zonder één bal te slaan. Het woord komt uit het Engels: de winnaar 'loopt' als het ware de ronde door.</p>
<p>Belangrijk voor wedders: de wedstrijd moet echt niet begonnen zijn. Wordt er al één punt gespeeld en stopt een speler daarna, dan is het geen walkover meer maar een opgave. Daarvoor gelden andere regels.</p>
<h3><strong>Walkover, opgave, no-show of lucky loser: wat is het verschil?</strong></h3>
{tabel(["Begrip", "Wat gebeurt er?", "Je weddenschap op de winnaar"], [
    ("<strong>Walkover</strong>", "Een speler trekt zich terug vóór de eerste service.", "Ongeldig, je krijgt je inzet terug."),
    ("<strong>No-show</strong>", "Een speler komt niet opdagen. De partij gaat naar de tegenstander.", "Net als bij een walkover: de wedstrijd is niet begonnen, dus ongeldig."),
    ("<strong>Lucky loser</strong>", "Een verliezer uit de kwalificatie neemt de plek in van een speler die zich vóór de start terugtrok.", "De wedstrijd waarop je wedde gaat niet door: ongeldig. De lucky loser speelt een nieuwe wedstrijd."),
    ("<strong>Opgave</strong>", "Een speler stopt tijdens de wedstrijd, meestal door een blessure.", "Verschilt per bookmaker. Bij TOTO ongeldig, bij Unibet en BetCity wint na één set de speler die doorgaat."),
    ("<strong>Diskwalificatie</strong>", "De scheidsrechter zet een speler tijdens de wedstrijd uit.", "Meestal als een opgave. Bij bet365 en Vbet wint de speler die doorgaat."),
])}
<p>Over opgaves lees je alles in ons artikel over <a href="{HOOFD}">wat er gebeurt als een tennisser opgeeft</a>. Dat verschil is belangrijk: bij een opgave kun je je weddenschap verliezen, bij een walkover niet.</p>
<h3><strong>Wat gebeurt er met je weddenschap bij een walkover?</strong></h3>
<p>Omdat er niets gespeeld is, kan niets al beslist zijn. Daarom worden bij een walkover alle markten op die wedstrijd ongeldig:</p>
{tabel(["Markt", "Bij een walkover"], [
    ("<strong>Winnaar van de wedstrijd</strong>", "Ongeldig. Ook als je op de speler wedde die doorgaat."),
    ("<strong>Setwedden en eerste set</strong>", "Ongeldig, er is geen set gespeeld."),
    ("<strong>Totaal games (over/under)</strong>", "Ongeldig, er zijn nul games gespeeld en de lijn telt niet."),
    ("<strong>Handicap in games of sets</strong>", "Ongeldig, er is geen uitslag om de handicap op toe te passen."),
    ("<strong>Spelermarkten (aces, breaks)</strong>", "Ongeldig. TOTO noemt dit apart: begint een speler niet aan de wedstrijd, dan vervallen de spelergerelateerde wedopties."),
    ("<strong>Bet Builder</strong>", "De hele Bet Builder wordt ongeldig."),
])}
<p><em>De quoteringen in dit artikel zijn fictief en alleen bedoeld om de berekening te laten zien.</em></p>
<p><strong>Voorbeeld.</strong> Je zet {eur(INZET)} in op speler A tegen een quotering van {q(ODD_A)}. Had A gewonnen, dan kreeg je {eur(INZET * ODD_A)}. Maar speler B trekt zich voor de wedstrijd terug met een blessure. A gaat door, maar jouw weddenschap wordt ongeldig. Je krijgt je {eur(INZET)} terug, zonder winst en zonder verlies.</p>"""

content2 = f"""<h3><strong>Walkover in een combi: de selectie telt als 1,00</strong></h3>
<p>Zit een tenniswedstrijd met een walkover in je combinatieweddenschap, dan vervalt je combi niet. De ongeldige selectie telt als quotering 1,00 en de rest loopt gewoon door.</p>
<p><strong>Rekenvoorbeeld.</strong> Je zet {eur(INZET)} op een combi van drie: een voetbalwedstrijd op {q(C_VOET)}, speler A op {q(C_TEN)} en een darter op {q(C_DARTS)}. Samen is dat {q(C_VOL)}, goed voor {eur(INZET * C_VOL)}. Dan volgt een walkover in de tenniswedstrijd. De quotering wordt {q(C_VOET)} × 1,00 × {q(C_DARTS)} = {q(C_WO)}. Winnen de andere twee, dan krijg je {eur(INZET * C_WO)}. Bij bet365 heet dit anders, maar het komt op hetzelfde neer: je drievoud wordt een dubbel. Meer uitleg vind je bij <a href="{ACCA}">combinatieweddenschappen</a>.</p>
<p><strong>Bet Builder.</strong> Een <a href="{BB}">bet builder</a> binnen één tenniswedstrijd werkt anders. Wordt één selectie ongeldig, dan vervalt bij TOTO en Unibet de hele Bet Builder. Bij een walkover zijn alle selecties ongeldig. Zet je {eur(INZET)} in op een Bet Builder van {q(BB_ODD)}, dan krijg je dus {eur(BB_UIT)} terug.</p>
<h3><strong>Walkover per bookmaker: alle regels op een rij</strong></h3>
<p>Bijna alle legale bookmakers maken een weddenschap bij een walkover ongeldig. Het verschil zit vooral in hoe duidelijk ze het opschrijven.</p>
{tabel(["Bookmaker", "Walkover", "In een combi"], RIJEN_REGELS)}
<p>Stand 22 oktober 2026, op basis van de eigen voorwaarden van elke bookmaker. Bij 'zie voorwaarden' staat de regel niet duidelijk in de tekst die we konden lezen. Bingoal en ZEbet konden we niet inzien. * Circus noemt geen aparte walkover-regel, maar annuleert alle weddenschappen als een speler in het enkelspel wordt vervangen. ** Vbet noemt geen aparte walkover-regel. Een niet gespeelde wedstrijd geldt daar als geannuleerd als hij wordt afgelast. Vraag bij twijfel de klantenservice.</p>
<h3><strong>TOTO en walkover: wat zijn de regels?</strong></h3>
<p>{TOTO} is het duidelijkst. Start een wedstrijd niet, bijvoorbeeld door een walkover, dan worden alle wedopties op die wedstrijd ongeldig verklaard. Dat geldt ook voor spelermarkten zoals aces en voor alle Bet Builder-selecties op die wedstrijd. In een combi telt de wedstrijd als 1,00.</p>
<h3><strong>Bet365, Unibet en BetCity bij een walkover</strong></h3>
<p>Bij {bm("bet365")} geldt een speler die zich voor de start terugtrekt als 'non-runner': je selectie is ongeldig en je krijgt je inzet terug. In een combi loopt de rest door.</p>
<p>{bm("Unibet")} schrijft dat alle weddenschappen op wedstrijden 'die worden toegekend via een walk-over-beslissing' ongeldig zijn. Dezelfde tekst staat in de voorwaarden van {lijst(["BetCity", "JACKS.NL", "LeoVegas", "BetMGM", "711", "Oranje Palace", "Betnation"])}. Bij deze bookmakers telt een ongeldige selectie in een combi als 1,00.</p>"""

content3 = f"""<h3><strong>Walkover en live wedden</strong></h3>
<p>Live wedden kan pas als een wedstrijd begonnen is. Bij een walkover bestaat er dus geen live weddenschap op die wedstrijd. Stopt een speler na het eerste punt, dan is het een opgave en gelden de regels voor een opgave. Lees meer over <a href="{LIVE}">live wedden</a> en over <a href="/nieuws/hoe-lang-duurt-een-tenniswedstrijd">hoe lang een tenniswedstrijd duurt</a>.</p>
<p>Let wel op als je wedt terwijl het nieuws over een terugtrekking al rondgaat. Bij Unibet worden weddenschappen die zijn geplaatst nadat een speler zich al had teruggetrokken, ongeldig verklaard. Je wint dan niets, ook al zag je de quotering nog staan.</p>
<h3><strong>Walkover en de toernooiwinnaar</strong></h3>
<p>Wed je op de winnaar van een heel toernooi, dan telt het moment van terugtrekken:</p>
<ul><li><strong>Vóór het toernooi:</strong> start je speler niet, dan is je weddenschap bij bet365, Unibet, Circus en Vbet ongeldig en krijg je je inzet terug.</li><li><strong>Tijdens het toernooi:</strong> geeft je speler bijvoorbeeld een walkover in de kwartfinale, dan heeft hij wel meegedaan. Je weddenschap op de toernooiwinnaar is dan meestal verloren.</li></ul>
<p>TOTO noemt hiervoor geen aparte regel. Twijfel je, kijk dan bij de wedoptie zelf of vraag het de klantenservice.</p>
<h3><strong>Tips om een walkover voor te zijn</strong></h3>
<ul><li><strong>Volg het nieuws.</strong> Had een speler de dag ervoor een lange partij of een blessure? Dan is de kans op een walkover groter.</li><li><strong>Wed dichter bij de start.</strong> Een terugtrekking wordt meestal kort voor de wedstrijd bekend. Wed je op de dag zelf, dan weet je meer.</li><li><strong>Houd je combi klein.</strong> Een walkover kost je geen geld, maar je combi wordt wel lager.</li><li><strong>Ken het verschil met een opgave.</strong> Bij een opgave kun je wel verliezen. Kies bij twijfel over de fitheid van een speler een bookmaker die bij een opgave je inzet teruggeeft, zoals TOTO.</li></ul>
<h3><strong>Wedden op tennis bij een legale bookmaker</strong></h3>
<p>Wed alleen bij bookmakers met een vergunning van de Kansspelautoriteit. Speel je bij een site zonder vergunning, dan speel je illegaal en sta je nergens als een walkover verkeerd wordt afgehandeld. Lees <a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je herkent of een bookmaker legaal is</a>. Zet alleen in wat je kunt missen, stel limieten in en lees onze tips over <a href="/speel-bewust/verantwoord-wedden">verantwoord wedden</a>. Meer uitleg over weddenschappen vind je in de <a href="/wedgids">wedgids</a>.</p>
<h3><strong>Veelgestelde vragen over een walkover bij tennis</strong></h3>
<p><strong>Wat is een walkover bij tennis?</strong><br>Een speler trekt zich terug voordat de wedstrijd begint. Zijn tegenstander gaat zonder te spelen door naar de volgende ronde.</p>
<p><strong>Krijg ik mijn geld terug bij een walkover?</strong><br>Ja. Bij bijna alle legale bookmakers wordt je weddenschap ongeldig en krijg je je inzet terug, ook als je wedde op de speler die doorgaat.</p>
<p><strong>Wat doet TOTO bij een walkover?</strong><br>TOTO verklaart alle wedopties op die wedstrijd ongeldig, ook spelermarkten zoals aces. Een Bet Builder op die wedstrijd is helemaal ongeldig. In een combi telt de wedstrijd als 1,00.</p>
<p><strong>Wat gebeurt er met mijn combi bij een walkover?</strong><br>De combi blijft staan. De tenniswedstrijd telt als quotering 1,00 en je wint als de andere selecties goed zijn. Je totale quotering wordt wel lager.</p>
<p><strong>Wat is het verschil tussen een walkover en een opgave?</strong><br>Bij een walkover begint de wedstrijd niet. Bij een opgave stopt een speler tijdens de wedstrijd. Een walkover is altijd ongeldig; bij een opgave verschilt het per bookmaker of je weddenschap blijft staan.</p>
<p><strong>Wat is een lucky loser?</strong><br>Een speler die in de laatste kwalificatieronde verloor, maar toch in het hoofdtoernooi komt omdat een andere speler zich terugtrok. Je weddenschap op de oorspronkelijke wedstrijd wordt ongeldig.</p>
<p><strong>Kan ik live wedden op een wedstrijd met een walkover?</strong><br>Nee. Live wedden kan pas als de wedstrijd begonnen is. Stopt een speler na de eerste bal, dan is het een opgave.</p>
<p>Meer over de regels bij een opgave lees je in ons <a href="{HOOFD}">hoofdartikel over tennis opgave</a>.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    html = content + content2 + content3
    assert re.search(r"<(ul|ol|/li)>\s+<", html) is None
    assert "/kennisbank/" not in html and "<h2" not in html
    assert html.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert "gebeurd" not in TITEL and len(TITEL) <= 70 and TITEL.lower().startswith("wat is een walkover bij tennis")
    assert 120 <= len(SAMENVATTING) <= 155
    assert len(OG_CHIPS) == 2 and len(OG_DATA) == 4 and html.count("<table") >= 3
    for link in (HOOFD, "/wedgids", ACCA, LIVE, BB, "/speel-bewust/verantwoord-wedden"):
        assert link in html, link
    faq = content3.split("Veelgestelde vragen")[1]
    assert 6 <= faq.count("<p><strong>") <= 8
    tekst = re.sub(r"<[^>]+>", " ", html)
    woorden = len(tekst.split())
    assert 1200 <= woorden <= 1800, woorden
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", woorden, "woorden |",
          [len(re.sub(r"<[^>]+>", " ", c).split()) for c in (content, content2, content3)])
    # ---- --live: NIET zelf draaien; alleen na akkoord van Jasper (bij voorkeur via wg_publiceer.py walkover --live).
    #      Daarna handmatig 301: /nieuws/walkover-tennis-dit-gebeurt-er-met-je-weddenschap-bij-een-walkover-nederlandse-
    #      bookmakers -> /nieuws/wat-gebeurd-er-bij-een-walkover-met-een-tennisweddenschap ----
    if "--live" in sys.argv:
        fd = {"name": TITEL, "content": content, "content-2": content2, "content-3": content3,
              "samenvatting": SAMENVATTING, "publicatiedatum": datetime.now(timezone.utc).isoformat()}
        print(WF.update_live(ITEM_ID, fd).get("lastPublished"))
