# -*- coding: utf-8 -*-
"""NIEUW wedgids-artikel (Nieuws, nog geen item): verlies najagen bij gokken, waarom het niet werkt en hoe je stopt.
Wat het is, waarom het faalt (negatieve verwachting x hogere inzet = hoger verwacht verlies; gokkersdrogreden),
waarschuwingssignalen, hulpmiddelen in NL (speelgrenzen, pauze, uitsluiting, Cruks, netto-stortingsgrens), hulp.
Toon: serieus, behulpzaam, niet belerend. GEEN links naar bookmakers (ook geen /bookmakers/ of /go/).
Onderwerp: Engelstalige analysesite (alleen het onderwerp; niets overgenomen).
Slug verlies-najagen-gokken (gaf HTTP 404 op 10-11-2026, dus vrij; /nieuws/verlies-najagen gaf ook 404).
Rubriek Speluitleg (volgens de brief), wedgids-categorie 'Legaal en verantwoord'.
Zoekwoorden: 'verlies najagen', 'verlies najagen gokken', 'verlies terugwinnen gokken', 'chasing losses betekenis',
'gokkersdrogreden' / 'gambler's fallacy', 'stoppen met gokken', 'gokken stoppen tips', 'gokstop', 'hulp bij gokproblemen'.

Feiten nagelopen op 10-11-2026:
- OpenOverGokken: openovergokken.nl/hulplijnen (ingebouwde browser, alleen lezen): 'Bel gratis: 0800 24 000 22', 'Dag en
  nacht, 24/7 bereikbaar'; WhatsApp en chat tussen 08.00 en 00.00 uur; gratis en anoniem; meldpunt voor problemen met een
  kansspel. loketkansspel.nl stuurt op 10-11-2026 door naar openovergokken.nl (Loket Kansspel bestaat niet meer als
  aparte dienst; OpenOverGokken is de opvolger, zie ook wg_cruks.py/wg_gokverslaving.py, 21-10-2026).
- AGOG: agog.nl/contact (10-11-2026): gratis 0800 - 22 777 22, ervaringsdeskundige aan de lijn, 'in principe' van 9.00
  uur tot middernacht, anders inspreken en terugbellen; afdelingen/zelfhulpgroepen in het land.
- Besluit kansspelen op afstand (wetten.overheid.nl/BWBR0044773, geldend van 15-07-2022): art. 4.14 grenzen vóór
  inschrijving: maximale tijd per dag/week/maand, maximale stortingen per dag/week/maand, maximaal saldo; verlagen direct,
  verhogen pas na ten minste een week; aanbieder moet voorkomen dat de maxima worden overschreden. Art. 4.19 lid 1 a:
  aanbieder schorst de deelname 'op verzoek van de speler' (pauze/time-out, geen vaste duur in het besluit).
- Besluit werving, reclame en verslavingspreventie (geldend vanaf 01-01-2026) art. 8 uitsluiting bij één aanbieder,
  art. 2a lid 4 geen bonussen meer: nagelopen 21-10-2026 (zie wg_gokverslaving.py), niet opnieuw bekeken.
- Regeling speellimieten (sinds 01-10-2024): pop-up elke 30 minuten, melding bij 50% van een limiet; netto-stortingsgrens
  €700 per maand (€300 tot 24 jaar) per aanbieder uit de Beleidsregel verantwoord spelen 2024: nagelopen 21-10-2026 (zie
  netto_stortingslimiet.py en wg_gokverslaving.py).
- Cruks: minimaal 6 maanden, alle legale online aanbieders, speelautomatenhallen en Holland Casino, gratis via
  cruksregister.nl (Wet op de kansspelen art. 33h; zie wg_cruks.py, 21-10-2026).
Rekenwerk (fictief, eigen voorbeeld): weddenschap met odd 2,00 op een uitkomst met een echte kans van 47,5% -> verwachting
-5% per euro inzet; verdubbelen na verlies (6 rondes, budget €630) -> kans op 6x verlies, verwachte inzet en verwacht
resultaat per reeks; kans op minstens één verloren reeks bij 50 reeksen. Alles hieronder berekend en ge-assert.
Bewust weggelaten: diagnose-criteria/percentages gokverslaving (geen officiële NL-bron nagelopen); bankblokkades en
namen van blokkeersoftware (niet nagelopen); kabinetsplannen (staan in wg_cruks.py); elke link naar een bookmaker.
Interne links gecontroleerd op 10-11-2026 (HTTP 200).
  ../superodd-agent/.venv/bin/python specials/wg_publiceer.py verlies-najagen"""
import os, sys, re
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
import lk_webflow as WF
from legaal_data import tabel

ITEM_ID = None   # nieuw artikel
SLUG = "verlies-najagen-gokken"
RUBRIEK = "6672e1c5c1902e8ee8ce98cd"   # zelfde rubriek als andere Legaal-en-verantwoord-artikelen
WEDGIDS_CAT = "Legaal en verantwoord"
TITEL = "Verlies najagen bij gokken: waarom het niet werkt"
SAMENVATTING = ("Verlies najagen bij gokken: waarom terugwinnen bijna altijd duurder uitpakt, aan welke signalen je het "
                "herkent en hoe je stopt, met hulp in Nederland.")

OG_KOP = "Verlies <span>najagen</span>: waarom het niet werkt"
OG_EYEBROW = "Legaal en verantwoord"
OG_CHIPS = ["Met rekenvoorbeeld", "Hulp: 0800 24 000 22"]
OG_MOTIEF = "reeks"

CRUKS = "/nieuws/cruks-de-gokstop-voor-verantwoord-gokken"
NETTO = "/nieuws/netto-stortingslimiet"
ODDS = "/nieuws/odds-uitgelegd-quotering-lezen"
MARTINGALE = "/nieuws/wat-is-het-martingale-systeem-een-dubbel-of-niets-wedstrategie"
GOKVERSLAVING = "/nieuws/voorkomen-van-een-gokverslaving-belangrijke-stappen-en-hulpbronnen"
VERANTWOORD = "/speel-bewust/verantwoord-wedden"
KSA = "<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"


def k(x, n=2):
    return f"{x:.{n}f}".replace(".", ",")


def eur(x):
    s = f"€{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return s[:-3] if s.endswith(",00") else s


def pct(x, n=0):
    return f"{100 * x:.{n}f}".replace(".", ",") + "%"


# ---- basis: odd 2,00 op een uitkomst met een echte kans van 47,5% (de bookmaker houdt zijn marge) ----
ODD, KANS = 2.00, 0.475
EV = KANS * ODD - 1                      # verwacht resultaat per euro inzet
EERLIJK = 1 / KANS
assert round(EV, 3) == -0.05 and k(EERLIJK) == "2,11"

# hogere inzet = hoger verwacht verlies
INZETTEN_VAST = [10, 20, 50, 100]
VERWACHT = {i: i * EV for i in INZETTEN_VAST}
assert [round(v, 2) for v in VERWACHT.values()] == [-0.5, -1.0, -2.5, -5.0]

# ---- verlies najagen: na elk verlies verdubbelen, maximaal 6 rondes ----
START, RONDES = 10, 6
REEKS = [START * 2 ** i for i in range(RONDES)]
BUDGET = sum(REEKS)
assert REEKS == [10, 20, 40, 80, 160, 320] and BUDGET == 630
P_VERLIES = 1 - KANS
P_ALLES_KWIJT = P_VERLIES ** RONDES
P_WINST = 1 - P_ALLES_KWIJT
# verwachte totale inzet: ronde i wordt alleen gespeeld als de vorige i rondes verloren gingen
VERWACHTE_INZET = sum(z * P_VERLIES ** i for i, z in enumerate(REEKS))
RESULTAAT = P_WINST * START - P_ALLES_KWIJT * BUDGET
assert abs(RESULTAAT - VERWACHTE_INZET * EV) < 1e-9          # zelfde uitkomst langs twee wegen
assert pct(P_ALLES_KWIJT, 1) == "2,1%" and pct(P_WINST, 1) == "97,9%"
assert round(VERWACHTE_INZET, 2) == 68.02 and round(RESULTAAT, 2) == -3.40
assert round(RESULTAAT / (START * EV), 1) == 6.8                # bijna 7x zo veel verwacht verlies als één inzet van €10

# vaak herhalen: kans dat het minstens één keer helemaal misgaat
HERHAAL = 50
P_MINSTENS_EEN = 1 - P_WINST ** HERHAAL
assert pct(P_MINSTENS_EEN) == "65%"
assert (HERHAAL - 1) * START < BUDGET                          # 49 keer €10 winst dekt één verloren reeks niet

# gokkersdrogreden: na 5 verliezen is de kans op nog een verlies gewoon weer 52,5%
assert pct(P_VERLIES, 1) == "52,5%"

OG_DATA = [eur(z) for z in REEKS]

content = f"""<p><strong>Verlies najagen betekent dat je na een verlies doorgaat of hoger inzet om het verloren geld terug te winnen. Het werkt niet, omdat elke weddenschap gemiddeld geld kost: de bookmaker houdt een marge. Hoe meer je inzet, hoe groter je verwachte verlies, en een reeks verliezen maakt winst daarna niet waarschijnlijker. Stoppen begint met vooraf grenzen stellen en accepteren dat verloren geld weg is. Lukt dat niet meer, praat er dan over: OpenOverGokken is dag en nacht gratis en anoniem bereikbaar via 0800 24 000 22.</strong></p>
<p>Bijna iedereen die gokt, kent het gevoel. Je hebt net verloren en denkt: met één goede weddenschap sta ik weer op nul. Dat is menselijk. Maar het is ook een van de duidelijkste stappen van ontspannen spelen naar spelen dat je niet meer in de hand hebt. Hieronder lees je waarom terugwinnen bijna altijd duurder uitpakt, met een rekenvoorbeeld, hoe je het bij jezelf herkent en wat je eraan kunt doen.</p>
<h3><strong>Wat is verlies najagen?</strong></h3>
<p>Verlies najagen (in het Engels <em>chasing losses</em>) is gokken met als doel geld terug te winnen dat je al kwijt bent. Het kan er zo uitzien:</p>
<ul><li>Na een verloren weddenschap meteen een nieuwe plaatsen, vaak op een wedstrijd waar je eigenlijk niets van weet.</li><li>De inzet verhogen of verdubbelen, zodat één winst alles goedmaakt.</li><li>Kiezen voor hogere odds of grote combi's, omdat die "in één keer" genoeg opleveren.</li><li>Extra geld storten dat je voor iets anders nodig had.</li><li>Langer doorspelen dan je van plan was, tot je "weer op nul staat".</li></ul>
<p>Het verschil met gewoon gokken zit in het doel. Je speelt niet meer voor plezier of spanning, maar om een gat te dichten. En juist dat gat wordt vaak groter.</p>
<h3><strong>Waarom werkt verlies najagen niet?</strong></h3>
<p>Er zijn twee redenen: de rekensom en ons brein. Eerst de rekensom.</p>
<p>Een bookmaker zet zijn odds iets lager dan de echte kans rechtvaardigt. Dat verschil is zijn marge. Neem een weddenschap met een odd van {k(ODD)} op een uitkomst die in werkelijkheid {pct(KANS, 1)} kans heeft. Een eerlijke odd zou dan {k(EERLIJK)} zijn. Per euro die je inzet, verlies je gemiddeld {abs(round(100 * EV))} cent. Hoe odds en marges werken, lees je in <a href="{ODDS}">odds uitgelegd</a>.</p>
<p>Dat verwachte verlies groeit mee met je inzet. <em>Het voorbeeld is fictief.</em></p>
{tabel(["Inzet per weddenschap", "Verwacht resultaat bij odd 2,00 en 47,5% kans"], [
    (eur(i), "−" + eur(abs(v))) for i, v in VERWACHT.items()])}
<p>Wie na verlies zijn inzet verhoogt, maakt zijn verwachte verlies dus groter, precies op het moment dat hij het kleiner wil maken. Er bestaat geen manier van inzetten die een negatieve verwachting positief maakt.</p>"""

content2 = f"""<h3><strong>Rekenvoorbeeld: wat kost verdubbelen na verlies?</strong></h3>
<p>Een bekende manier van najagen is verdubbelen: je begint met {eur(START)} en verdubbelt na elk verlies, zodat de eerste winst alles terugbetaalt plus {eur(START)}. Stel dat je maximaal {RONDES} keer verdubbelt, want daarna is je budget op. Dit zijn de inzetten:</p>
{tabel(["Ronde", "Inzet", "Totaal ingezet"], [(str(i + 1), eur(z), eur(sum(REEKS[:i + 1]))) for i, z in enumerate(REEKS)])}
<p>Op hetzelfde soort weddenschap als hierboven ziet dat er zo uit:</p>
<ul><li>In <strong>{pct(P_WINST, 1)}</strong> van de reeksen win je één keer en sta je {eur(START)} in de plus.</li><li>In <strong>{pct(P_ALLES_KWIJT, 1)}</strong> verlies je zes keer op rij en ben je <strong>{eur(BUDGET)}</strong> kwijt.</li><li>Gemiddeld zet je per reeks {eur(round(VERWACHTE_INZET, 2))} in. Je verwachte resultaat is <strong>−{eur(abs(round(RESULTAAT, 2)))}</strong> per reeks: bijna {k(RESULTAAT / (START * EV), 0)} keer zoveel als één losse weddenschap van {eur(START)}.</li></ul>
<p>Daarom voelt najagen alsof het werkt: meestal gaat het goed. Maar je riskeert {eur(BUDGET)} om {eur(START)} te winnen. Herhaal je dit {HERHAAL} keer, dan is de kans {pct(P_MINSTENS_EEN)} dat je minstens één keer de hele {eur(BUDGET)} verliest. Met {HERHAAL - 1} keer {eur(START)} winst ({eur((HERHAAL - 1) * START)}) maak je dat niet goed. Meer over dit systeem lees je in ons artikel over de <a href="{MARTINGALE}">martingale-strategie</a>.</p>
<h3><strong>Waarom voelt het toch logisch om door te gaan?</strong></h3>
<p>Dan het brein. Een paar denkfouten maken verlies najagen verleidelijk:</p>
<ul><li><strong>De gokkersdrogreden.</strong> Na vijf verliezen voelt winst "aan de beurt". Maar een wedstrijd weet niet wat jij eerder verloor. Op ons voorbeeld is de kans op nog een verlies gewoon weer {pct(P_VERLIES, 1)}.</li><li><strong>Verlies doet meer pijn dan winst plezier geeft.</strong> Daardoor wil je een verlies ongedaan maken, ook als dat meer risico betekent.</li><li><strong>"Het geld is er al in gegaan".</strong> Wat je verloor, krijg je niet terug door door te gaan. Elke nieuwe weddenschap is een nieuwe beslissing met een nieuwe, negatieve verwachting.</li><li><strong>Bijna-winst.</strong> Een combi die op één wedstrijd na binnen was, voelt als bewijs dat je dichtbij bent. Dat is het niet.</li></ul>
<h3><strong>Aan welke signalen herken je verlies najagen?</strong></h3>
<p>Wees eerlijk tegen jezelf. Herken je een of meer van deze punten?</p>
<ul><li>Je zet hoger in na een verlies dan na een winst.</li><li>Je stort opnieuw binnen een paar uur na een verlies.</li><li>Je hebt een vast doel, zoals "weer op nul", en stopt pas als je dat haalt.</li><li>Je wedt op sporten of competities die je normaal overslaat, alleen om te kunnen spelen.</li><li>Je verhoogt je limiet of zoekt een andere aanbieder als je limiet op is.</li><li>Je gebruikt geld voor vaste lasten, leent geld of houdt je verliezen geheim.</li><li>Je denkt na het spelen nog lang aan wat je kwijt bent.</li></ul>
<p>Eén signaal betekent niet meteen dat je verslaafd bent, maar het is wel een reden om nu in te grijpen. Meer signalen en stappen vind je in ons artikel over <a href="{GOKVERSLAVING}">gokverslaving voorkomen</a>.</p>"""

content3 = f"""<h3><strong>Hoe stop je met verlies najagen?</strong></h3>
<ol><li><strong>Zie inzet als uitgave.</strong> Geld dat je inzet, ben je in principe kwijt, net als een kaartje voor de bioscoop. Wat je verloor, komt niet terug.</li><li><strong>Bepaal vooraf een budget en een verliesgrens.</strong> Bijvoorbeeld per week, met een bedrag dat je echt kunt missen. Is het op, dan stop je, ook als het "net misging".</li><li><strong>Gebruik een vaste inzet.</strong> Nooit hoger inzetten na een verlies.</li><li><strong>Neem afstand na een verlies.</strong> Sluit de app en wacht minstens een dag met de volgende weddenschap.</li><li><strong>Speel niet als je boos, moe, verdrietig of onder invloed bent.</strong> Dan is de neiging om terug te winnen het grootst.</li><li><strong>Praat erover.</strong> Vertel iemand die je vertrouwt hoeveel je speelt. Geheimhouden maakt stoppen moeilijker.</li></ol>
<h3><strong>Welke hulpmiddelen heb je in Nederland?</strong></h3>
<p>Bij aanbieders met een vergunning van de Kansspelautoriteit zijn deze hulpmiddelen verplicht. Stel ze in op een rustig moment, niet midden in een slechte avond.</p>
{tabel(["Hulpmiddel", "Wat het doet", "Goed om te weten"], [
    ("<strong>Speelgrenzen</strong>", "Een maximum voor je stortingen, je speeltijd en je saldo per dag, week of maand", "Verplicht bij inschrijving. Verlagen gaat direct, verhogen pas na minstens een week: tijd om af te koelen"),
    ("<strong>Pauze</strong>", "Je vraagt de aanbieder om je account te schorsen", "Elke legale aanbieder moet dat op jouw verzoek doen"),
    ("<strong>Uitsluiting bij één aanbieder</strong>", "Je sluit jezelf uit bij een bepaalde site", "Geldt niet voor andere aanbieders"),
    ("<strong>Cruks</strong>", "Gokstop bij alle legale online aanbieders, speelhallen en Holland Casino", "Minimaal 6 maanden, gratis via cruksregister.nl"),
    ("<strong>Netto-stortingsgrens</strong>", "De aanbieder moet ingrijpen als je netto meer stort dan de grens", "€700 per maand, of €300 als je jonger bent dan 24, per aanbieder"),
    ("<strong>Meldingen</strong>", "Een pop-up over je speeltijd en je limieten", "Elke 30 minuten, plus een melding bij 50% van een limiet"),
    ("<strong>Geen bonussen</strong>", "Je geeft aan dat je geen bonussen meer wilt", "Kan altijd, bij elke legale aanbieder"),
])}
<p>Hoe de grens van €700 en €300 werkt, lees je bij de <a href="{NETTO}">netto-stortingslimiet</a>. Alles over de landelijke gokstop staat in ons artikel over <a href="{CRUKS}">Cruks</a>. Let op: illegale goksites doen hier niet aan mee. Juist wie verlies najaagt, loopt daar het grootste risico.</p>
<h3><strong>Waar vind je hulp bij gokproblemen?</strong></h3>
<p>Hulp vragen is geen zwakte. Hoe eerder je het doet, hoe kleiner de schade meestal blijft.</p>
{tabel(["Waar", "Wat", "Bereikbaarheid"], [
    ("<strong>OpenOverGokken</strong>", "Praten met een deskundige, zelftest en informatie, ook voor naasten", "Gratis en anoniem: 0800 24 000 22, dag en nacht. WhatsApp en chat van 08.00 tot 00.00 uur, via openovergokken.nl"),
    ("<strong>AGOG</strong>", "Zelfhulpgroepen van ervaringsdeskundigen, ook voor naasten", "Gratis: 0800 22 777 22, in principe van 9.00 uur tot middernacht"),
    ("<strong>Huisarts</strong>", "Doorverwijzing naar de verslavingszorg", "Via je eigen huisarts"),
    ("<strong>Gemeente</strong>", "Schuldhulpverlening als gokken tot schulden heeft geleid", "Gratis, bij je eigen gemeente"),
])}
<p>Loket Kansspel bestaat niet meer als aparte dienst. Wie de oude website bezoekt, komt nu uit bij OpenOverGokken. Meer over bewust spelen lees je op onze pagina over <a href="{VERANTWOORD}">verantwoord wedden</a> en in de <a href="/wedgids">wedgids</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wat betekent verlies najagen?</strong><br>Doorgaan met gokken, vaak met hogere inzetten, om geld terug te winnen dat je al hebt verloren. In het Engels heet het chasing losses.</p>
<p><strong>Kun je verlies terugwinnen door je inzet te verdubbelen?</strong><br>Meestal lijkt het te lukken, maar af en toe verlies je in één reeks een groot bedrag. Omdat elke weddenschap een negatieve verwachting heeft, verlies je op den duur gemiddeld meer naarmate je meer inzet.</p>
<p><strong>Is de kans op winst groter na een paar keer verliezen?</strong><br>Nee. Elke wedstrijd staat los van de vorige. Denken dat winst "aan de beurt" is, heet de gokkersdrogreden.</p>
<p><strong>Hoe kan ik mezelf blokkeren bij goksites?</strong><br>Bij één aanbieder via de uitsluiting in je account. Bij alle legale aanbieders tegelijk met een gokstop in Cruks, voor minimaal zes maanden.</p>
<p><strong>Waar kan ik anoniem praten over gokken?</strong><br>Bij OpenOverGokken, gratis en dag en nacht via 0800 24 000 22. De AGOG is gratis bereikbaar via 0800 22 777 22.</p>
{KSA}"""

if __name__ == "__main__":
    html = content + content2 + content3
    assert re.search(r"<(ul|ol|/li)>\s+<", html) is None
    assert "/kennisbank/" not in html and "<h2" not in html and "<h4" not in html
    assert "/go/" not in html and "/bookmakers/" not in html          # geen bookmakerlinks in dit artikel
    assert html.rstrip().endswith(KSA)
    assert content.startswith("<p><strong>")
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert len(OG_CHIPS) == 2 and html.count("<table") >= 3
    koppen = re.findall(r"<h3>(.*?)</h3>", html)
    assert all(h.startswith("<strong>") and h.endswith("</strong>") for h in koppen)
    for link in (CRUKS, NETTO, ODDS, MARTINGALE, GOKVERSLAVING, VERANTWOORD, "/wedgids"):
        assert link in html, link
    for link in re.findall(r'href="([^"]+)"', html):
        assert link.startswith("/"), link
    assert html.count("0800 24 000 22") >= 2 and "0800 22 777 22" in html
    faq = content3.split("Veelgestelde vragen")[1]
    assert 4 <= faq.count("<p><strong>") <= 6
    for verboden in ("footymetrics", "betcity", "opstellingvandaag", "waaroptv", "toto", "unibet", "bet365"):
        assert verboden not in html.lower(), verboden
    tekst = re.sub(r"<[^>]+>", " ", html)
    woorden = len(tekst.split())
    assert 1200 <= woorden <= 2200, woorden
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", woorden, "woorden |",
          [len(re.sub(r"<[^>]+>", " ", c).split()) for c in (content, content2, content3)])
    # ---- NIET zelf publiceren; alleen na akkoord van Jasper via wg_publiceer.py verlies-najagen --live ----
