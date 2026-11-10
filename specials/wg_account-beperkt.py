# -*- coding: utf-8 -*-
"""NIEUW wedgids-artikel (Nieuws, nog geen item): waarom beperken bookmakers je account? Limiet, stake factoring,
wat een bookmaker als 'winnaar' of 'bonusjager' ziet, wat je kunt doen en hoe het in Nederland zit.
Slug account-beperkt-bookmaker (gaf HTTP 404 op 10-11-2026, dus vrij). Rubriek Speluitleg, wedgids-categorie
'Wedden uitgelegd'. Onderwerp: Engelstalige analysesite (niets overgenomen; eigen opzet, eigen voorbeelden).
Zoekwoorden: 'account beperkt bookmaker', 'bookmaker limiet verlaagd', 'maximale inzet verlaagd', 'gelimiteerd account',
'stake factoring', 'waarom beperken bookmakers winnaars', 'mag een bookmaker je beperken', 'klacht bookmaker'.

Feiten nagelopen op 10-11-2026 (bronnen NIET in de tekst genoemd, behalve de wet/Ksa in algemene zin):
- Besluit kansspelen op afstand (Bkoa, wetten.overheid.nl/BWBR0044773, 'Geldend van 15-07-2022 t/m heden'):
  art. 4.10 alleen natuurlijke personen; art. 4.15 lid 1 c speler verklaart 'uitsluitend voor eigen rekening te zullen
  spelen', d inschrijving niet gebruiken voor fraude met of misbruik van de kansspelen; art. 4.26 lid 1 'slechts een
  enkele speelrekening' per speler; art. 4.14 verplichte grenzen (duur, stortingen, tegoed), verlagen direct, verhogen
  na ten minste een week; art. 4.19 schorsing (op verzoek, bij redelijk vermoeden dat niet meer aan de voorwaarden wordt
  voldaan, bij onmatige deelname/verslaving); art. 4.34 lid 1 c en g: info over algemene voorwaarden en
  klachtenregeling; art. 4.35 geen ander recht dan Nederlands recht en geen andere dan de Nederlandse rechter;
  art. 4.36 klantendienst kosteloos; art. 4.37 transparante, eenvoudige en kosteloze klachtenprocedure, klager
  'schriftelijk en gemotiveerd' op de hoogte van bevindingen, afhandeling 'uiterlijk binnen acht weken';
  art. 4.8 lid 4 / 4.9: passende maatregelen bij ongebruikelijke feiten die duiden op manipulatie.
- Regeling kansspelen op afstand (BWBR0044767, 'Geldend van 01-04-2026'): art. 3.21 klacht registreren binnen 72 uur;
  art. 3.22 lid 1 ontvangstbevestiging uiterlijk binnen 72 uur; lid 3 niet in behandeling -> binnen een week bericht.
- Besluit werving, reclame en verslavingspreventie kansspelen (BWBR0033412, 'Geldend van 01-01-2026'): art. 2a lid 3
  speler informeren over bonusvoorwaarden en geen bonus zonder uitdrukkelijke aanvaarding; lid 4 speler kan te allen
  tijde aangeven geen bonus meer te willen; lid 2 bonus niet afstemmen op individueel speelgedrag.
- BW art. 6:233 (wetten.overheid.nl/BWBR0005289): beding in algemene voorwaarden vernietigbaar als het onredelijk
  bezwarend is.
- Ksa 'Stel een vraag of doe een melding over een kansspel' (kansspelautoriteit.nl/stel-een-vraag-doe-een-melding-over-
  een-kansspel, 10-11-2026): 'De Kansspelautoriteit kan uw probleem niet oplossen en wij kunnen niet persoonlijk
  bemiddelen'; geen persoonlijke terugkoppeling; advies: in gesprek met de aanbieder, klachtenfunctionaris of juridisch
  adviseur, bijv. Het Juridisch Loket; Ksa kan optreden bij risico of herhaalde meldingen.
- Ksa-nieuws 2-4-2026 ('De Ksa geeft duidelijkheid over kosten bij accountsluiting en uitbetaling via de klantenservice'):
  account sluiten op verzoek verplicht, geen kosten voor sluiten, resterend tegoed zonder onnodige vertraging uitbetalen,
  geen minimumbedrag. Ksa-nieuws 17-07-2025 (ZEbet/Starcasino): eigen saldo direct opneembaar; rondspeelvoorwaarden
  alleen bij een bonus.
- Ksa 'Inzet op integriteit, leidraad integriteit van sportweddenschappen' (pdf 2025-12): maatregelen bij verhoogd
  risico o.a. 'inzetbeperkingen' en verscherpte transactiemonitoring, achteraf 'het blokkeren van de betreffende
  spelers'; risicovariabelen o.a. 'Herhalende weddenschappen die grenzen aan inzetlimieten' en 'Inactieve of recent
  geopende accounts waaruit afwijkende inzetten worden geplaatst'.
- Ksa Leidraad Wwft (december 2023, kansspelautoriteit.nl/leidraad-wwft): voorbeelden om de bron van middelen te
  onderzoeken o.a. 'Inzetten van de speler op alle mogelijke uitkomsten van een wedoptie zodat men zeker is van winst'
  en inzetten 'voornamelijk ... op (zeer) lage quoteringen'.
- Netto-stortingsgrens €300 (18 t/m 23) / €700 (24+) per kalendermaand: Beleidsregel verantwoord spelen 2024, zie
  netto_stortingslimiet.py (nagelopen 21-10-2026); hier alleen in de vergelijkingstabel + link.
- GEEN regel gevonden (Wok, Bkoa, Rkoa, Besluit werving, Ksa-site, Kamerstukken via zoeken op 10-11-2026) die een
  vergunde bookmaker verplicht elke inzet te accepteren of verbiedt winnende spelers te beperken -> in de tekst als
  'de Nederlandse kansspelregels verplichten ... nergens' en 'voor zover wij kunnen nagaan'. ONZEKER-ish: negatief bewijs.
- Praktijk (geen juridisch feit, algemeen bekend in de branche, voorzichtig geformuleerd): stake factoring / factor per
  account, beperking tot enkele euro's, uitsluiten van promoties, slotkoers als maatstaf.
Bewust weggelaten: namen van bookmakers (geen beschuldigingen zonder bron), percentages 'zoveel % van de accounts wordt
beperkt' (niet officieel), tips om een beperking te ontlopen (meerdere accounts, iemand anders laten wedden: verboden),
illegale aanbieders als alternatief.
Rekenvoorbeeld: slotkoers over/under 1,90/1,98 -> marge, eerlijke kans, EV van een inzet op 2,10; stake factoring
€500 x 0,05; alles hieronder berekend en ge-assert.
Interne links gecontroleerd op 10-11-2026 (HTTP 200): zie de lijst in de asserts.
  python3 specials/wg_account-beperkt.py [--live]"""
import os, sys, re
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
import lk_webflow as WF
from legaal_data import tabel

ITEM_ID = None   # nieuw artikel
SLUG = "account-beperkt-bookmaker"
RUBRIEK = "6502b66cd9992658b4037cf5"   # Speluitleg
WEDGIDS_CAT = "Wedden uitgelegd"
TITEL = "Account beperkt bij je bookmaker? Zo zit het"
SAMENVATTING = ("Waarom verlaagt een bookmaker je maximale inzet? Uitleg over beperkte accounts, stake factoring en "
                "slotkoersen, plus wat je in Nederland kunt doen.")

OG_KOP = "Account <span>beperkt</span> door je bookmaker?"
OG_EYEBROW = "Stake factoring uitgelegd"
OG_CHIPS = ["Met rekenvoorbeeld", "Zo zit het in Nederland"]
OG_MOTIEF = "lijst"
OG_DATA = ["Beter dan de slotkoers", "Arbitrage", "Alleen voor bonussen", "Opvallend inzetpatroon"]

ODDS = "/nieuws/odds-uitgelegd-quotering-lezen"
VALUE = "/nieuws/wat-is-de-wedstrategie-value-betting"
ARB = "/nieuws/wat-is-arbitrage-wedden-de-kunst-van-de-risicovrije-winst"
MATCHED = "/nieuws/wat-houdt-de-wedstrategie-matched-betting-in"
NETTO = "/nieuws/netto-stortingslimiet"
LEGAAL = "/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland"
FREEBET = "/nieuws/beste-free-bet-nederland-rondspeelvoorwaarden"
VERANTWOORD = "/speel-bewust/verantwoord-wedden"
KSA = "<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"


def k(x, n=2):
    return f"{x:.{n}f}".replace(".", ",")


def pct(x, n=0):
    return f"{100 * x:.{n}f}".replace(".", ",") + "%"


def eur(x, n=2):
    s = f"{x:,.{n}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return "€" + s


# ---- rekenvoorbeeld 1 (fictief): jouw inzet op over 2,5 tegen 2,10; slotkoers over 1,90 / under 1,98 ----
JOUW_ODD, SLOT_OVER, SLOT_UNDER = 2.10, 1.90, 1.98
RUW_OVER, RUW_UNDER = 1 / SLOT_OVER, 1 / SLOT_UNDER
BOEK = RUW_OVER + RUW_UNDER
MARGE = BOEK - 1
P_FAIR = RUW_OVER / BOEK
EERLIJK = 1 / P_FAIR
CLV = JOUW_ODD / SLOT_OVER - 1
EV_JOUW = P_FAIR * JOUW_ODD - 1
EV_SLOT = P_FAIR * SLOT_OVER - 1
assert (pct(MARGE, 1), pct(P_FAIR), k(EERLIJK)) == ("3,1%", "51%", "1,96")
assert (pct(CLV, 1), pct(EV_JOUW, 1), pct(EV_SLOT, 1)) == ("10,5%", "7,2%", "-3,0%")
INZET, AANTAL = 20, 100
VERWACHT = AANTAL * INZET * EV_JOUW
assert round(VERWACHT) == 143

# ---- rekenvoorbeeld 2 (fictief): stake factoring ----
MAX_STANDAARD, FACTOR = 500, 0.05
MAX_JIJ = MAX_STANDAARD * FACTOR
assert MAX_JIJ == 25 and round(MAX_JIJ * EV_JOUW, 2) == 1.79

content = f"""<p><strong>Een bookmaker beperkt je account als hij je ziet als een klant die hem op termijn geld kost: iemand die structureel betere odds pakt dan de koers bij de aftrap, die arbitrage speelt of die vooral voor bonussen komt. Je maximale inzet gaat dan omlaag, soms tot een paar euro, of je wordt uitgesloten van acties. In Nederland is dat voor zover wij kunnen nagaan toegestaan: geen enkele regel verplicht een vergunde bookmaker om elke inzet te accepteren. Wel moet je je saldo altijd kunnen opnemen en heb je recht op een serieuze klachtafhandeling.</strong></p>
<p>Een beperkt account voelt als straf voor goed wedden, en zo werkt het eigenlijk ook. In dit artikel lees je wat een beperking precies inhoudt, hoe stake factoring werkt, welke patronen een bookmaker in de gaten houdt en wat je wel en niet kunt doen. Met een rekenvoorbeeld dat laat zien waarom een kleine voorsprong voor een bookmaker al reden genoeg is.</p>
<h3><strong>Wat betekent een beperkt account?</strong></h3>
<p>Bij een beperkt (of 'gelimiteerd') account kun je nog wel inloggen, storten en opnemen, maar mag je minder inzetten dan andere klanten. Een beperking kan verschillende vormen hebben:</p>
<ul><li><strong>Lagere maximale inzet:</strong> waar een ander honderden euro's kan inzetten, krijg jij bij dezelfde wedoptie maar een fractie geaccepteerd.</li><li><strong>Bepaalde markten dicht:</strong> bijvoorbeeld live wedden, spelersmarkten of kleinere competities.</li><li><strong>Geen acties meer:</strong> je krijgt geen odds boosts, free bets of andere promoties.</li><li><strong>Handmatige goedkeuring:</strong> een medewerker beoordeelt je weddenschap eerst, en accepteert hem soms maar half of tegen een lagere quotering.</li><li><strong>Account gesloten:</strong> de zwaarste stap. Je saldo moet je dan wel terugkrijgen.</li></ul>
<p>Een beperking geldt voor nieuwe weddenschappen. Je merkt het meestal pas als een inzet wordt afgewezen of als er een melding verschijnt dat het maximum is bereikt.</p>
<h3><strong>Wat is stake factoring?</strong></h3>
<p>Veel bookmakers geven elk account een eigen factor. Die factor bepaalt welk deel van de standaard maximale inzet jij mag plaatsen. Een nieuwe klant begint vaak rond 1, een klant die als scherp wordt gezien kan naar 0,1 of lager zakken. Sommige recreatieve spelers krijgen juist een hogere factor.</p>
{tabel(["Situatie", "Maximale inzet"], [
    ("Standaard maximum op een wedoptie", eur(MAX_STANDAARD, 0)),
    (f"Jouw factor", k(FACTOR)),
    ("<strong>Wat jij mag inzetten</strong>", f"<strong>{eur(MAX_STANDAARD, 0)} × {k(FACTOR)} = {eur(MAX_JIJ, 0)}</strong>"),
])}
<p><em>Bedragen en factor zijn fictief; elke bookmaker hanteert eigen maxima.</em> De factor is niet zichtbaar in je account. Je ziet alleen het resultaat: een lager maximum dan je gewend was. Omdat de standaardmaxima per sport, competitie en markt verschillen, kan je limiet bij een Champions League-wedstrijd nog redelijk zijn en bij een lagere divisie bijna nul.</p>"""

content2 = f"""<h3><strong>Waarom beperken bookmakers winnende spelers?</strong></h3>
<p>Een bookmaker verdient aan de marge in zijn odds. Tel je de kansen achter alle uitkomsten van een wedoptie op, dan kom je boven 100% uit. Dat surplus is zijn verdienmodel: wie zonder voorsprong wedt, verliest op lange termijn gemiddeld ongeveer dat percentage. Hoe je die marge uit <a href="{ODDS}">odds</a> haalt, lees je in onze uitleg over quoteringen.</p>
<p>Een speler die de prijs structureel verslaat, keert dat model om. Een bookmaker kan zo iemand niet tegenhouden door zijn odds te verlagen voor alleen die klant, dus verlaagt hij het bedrag dat die klant mag inzetten. Dat is een commerciële keuze, geen oordeel over of je iets verkeerd hebt gedaan.</p>
<h3><strong>Rekenvoorbeeld: waarom de slotkoers zo belangrijk is</strong></h3>
<p>De beste graadmeter voor scherp wedden is de <strong>slotkoers</strong> (closing line): de odd vlak voor de aftrap, als alle informatie over opstellingen en blessures in de markt zit. Pak je structureel een betere odd dan de slotkoers, dan heb je bijna zeker een voorsprong. Bookmakers meten dat, ook als je toevallig een slechte reeks hebt. <em>Voorbeeld is fictief.</em></p>
<p>Je zet in op meer dan 2,5 doelpunten tegen een odd van {k(JOUW_ODD)}. Bij de aftrap staat de markt zo:</p>
{tabel(["Stap", "Berekening", "Uitkomst"], [
    ("Slotkoers over / under", "", f"{k(SLOT_OVER)} / {k(SLOT_UNDER)}"),
    ("Marge van de bookmaker", f"1/{k(SLOT_OVER)} + 1/{k(SLOT_UNDER)} − 1", pct(MARGE, 1)),
    ("Eerlijke kans op over 2,5", f"(1/{k(SLOT_OVER)}) ÷ {k(BOEK, 4)}", pct(P_FAIR, 1)),
    ("Eerlijke odd", f"1 ÷ {k(P_FAIR, 3)}", k(EERLIJK)),
    ("Jouw voorsprong op de slotkoers", f"{k(JOUW_ODD)} ÷ {k(SLOT_OVER)} − 1", pct(CLV, 1)),
    ("<strong>Verwacht rendement van jouw inzet</strong>", f"{k(P_FAIR, 3)} × {k(JOUW_ODD)} − 1", f"<strong>+{pct(EV_JOUW, 1)}</strong>"),
    ("Ter vergelijking: inzet tegen de slotkoers", f"{k(P_FAIR, 3)} × {k(SLOT_OVER)} − 1", pct(EV_SLOT, 1)),
])}
<p>Wie tegen de slotkoers wedt, verliest gemiddeld ongeveer {pct(-EV_SLOT, 0)} van zijn inzet. Jij wint met deze inzet gemiddeld {pct(EV_JOUW, 1)}. Doe je dat {AANTAL} keer met {eur(INZET, 0)}, dan is je verwachte winst ongeveer {eur(VERWACHT, 0)}, ook al kun je in die periode door pech verliezen. Precies dat verwachte verlies wil de bookmaker kwijt. Met de factor uit het vorige voorbeeld mag je nog maar {eur(MAX_JIJ, 0)} inzetten: je voorsprong is dan per weddenschap ongeveer {eur(MAX_JIJ * EV_JOUW)} waard. Meer over wedden op een voorsprong lees je in ons artikel over <a href="{VALUE}">value betting</a>.</p>
<h3><strong>Welk gedrag valt een bookmaker op?</strong></h3>
<p>Bookmakers volgen niet alleen je winst, maar vooral hoe je wedt. Deze signalen leiden vaak tot een beperking:</p>
<ul><li><strong>Je verslaat de slotkoers.</strong> Vroeg instappen op odds die daarna dalen, zoals hierboven.</li><li><strong>Je speelt <a href="{ARB}">arbitrage</a>.</strong> Je dekt alle uitkomsten af bij verschillende aanbieders, vaak met krom ogende bedragen zoals €47,30. In de Wwft-leidraad van de Kansspelautoriteit staat inzetten op alle uitkomsten zodat winst zeker is zelfs als voorbeeld van gedrag waarbij een aanbieder kan gaan onderzoeken waar je geld vandaan komt.</li><li><strong>Je komt alleen voor acties.</strong> Je zet alleen in als er een boost, free bet of andere bonus is, vaak met <a href="{MATCHED}">matched betting</a>. Hoe die voorwaarden werken, lees je in ons artikel over <a href="{FREEBET}">free bets en rondspeelvoorwaarden</a>.</li><li><strong>Je wedt op trage markten.</strong> Kleine competities of spelersmarkten waar de odds achterlopen op nieuws, bijvoorbeeld net voordat een opstelling bekend wordt.</li><li><strong>Je combineert uitkomsten die samenhangen.</strong> Bijvoorbeeld een team dat wint én zijn spits die scoort in één combinatie. Die gebeurtenissen hangen samen, dus de gewone combi-odd is te hoog. Daarom blokkeren veel bookmakers zulke combinaties of rekenen ze via een bet builder met een aangepaste prijs.</li><li><strong>Je zet steeds precies het maximum in.</strong> Ook dat valt op, zeker bij een nieuw account.</li></ul>
<p>Dat laatste is niet alleen een commercieel signaal. Volgens de leidraad integriteit van sportweddenschappen van de Kansspelautoriteit zijn 'herhalende weddenschappen die grenzen aan inzetlimieten' en afwijkende inzetten vanuit nieuwe of inactieve accounts mogelijke tekenen van matchfixing. Bij een verhoogd risico moet een Nederlandse aanbieder maatregelen nemen, en een inzetbeperking is daar een van.</p>"""

content3 = f"""<h3><strong>Mag een Nederlandse bookmaker winnaars beperken?</strong></h3>
<p>Ja, voor zover wij kunnen nagaan. De Nederlandse kansspelregels verplichten een bookmaker met een vergunning van de Kansspelautoriteit (Ksa) nergens om elke weddenschap of elk bedrag te accepteren, en er staat ook geen regel in die het beperken van winnende spelers verbiedt. Er staat ook geen plicht in om uit te leggen waarom je limiet omlaag gaat. Wel gelden er harde regels over hoe de bookmaker met je omgaat:</p>
<ul><li><strong>Je saldo blijft van jou.</strong> Een beperking mag je niet hinderen bij het opnemen van je eigen tegoed. Volgens de Ksa moet een aanbieder het tegoed zonder onnodige vertraging uitbetalen, zonder minimumbedrag. Rondspeelvoorwaarden mogen alleen gelden voor geld uit een bonus.</li><li><strong>Je kunt je account laten sluiten.</strong> De aanbieder moet dat op verzoek doen en mag er geen kosten voor rekenen.</li><li><strong>Voorwaarden moeten vooraf te vinden zijn.</strong> Algemene voorwaarden, bonusvoorwaarden en de klachtenregeling moeten op de site staan. Een bonus mag je alleen krijgen als je de voorwaarden uitdrukkelijk hebt aanvaard, en je kunt altijd aangeven dat je geen bonussen meer wilt.</li><li><strong>Nederlands recht.</strong> Een vergunde aanbieder mag niet bepalen dat een geschil onder buitenlands recht valt of bij een buitenlandse rechter moet worden uitgevochten.</li></ul>
<p>Twijfel je of je bookmaker een Nederlandse vergunning heeft, lees dan <a href="{LEGAAL}">hoe je controleert of een bookmaker legaal is</a>. Bij een illegale aanbieder gelden deze beschermingen niet.</p>
<h3><strong>Wat kun je doen als je account beperkt is?</strong></h3>
<p>Een beperking terugdraaien lukt zelden, maar je staat niet machteloos. Dit zijn de stappen:</p>
<ul><li><strong>Vraag om uitleg</strong> via de klantenservice. Die moet volgens de regels kosteloos bereikbaar zijn.</li><li><strong>Lees de voorwaarden</strong> waar de bookmaker zich op beroept, zeker als er bonuswinst is ingehouden.</li><li><strong>Dien een formele klacht in</strong> via de klachtenprocedure op de site. De aanbieder moet de ontvangst binnen 72 uur bevestigen, je schriftelijk en gemotiveerd laten weten wat hij heeft gevonden en de klacht uiterlijk binnen acht weken afhandelen.</li><li><strong>Haal juridisch advies</strong> als je vindt dat er geld wordt ingehouden zonder goede grond, bijvoorbeeld bij Het Juridisch Loket. Een beding in algemene voorwaarden dat onredelijk bezwarend is, kan de rechter vernietigen.</li><li><strong>Doe een melding bij de Ksa</strong> als je denkt dat een aanbieder de regels overtreedt. Let op: de Ksa bemiddelt niet in individuele geschillen en geeft geen persoonlijke terugkoppeling, maar gebruikt meldingen wel voor haar toezicht.</li></ul>
<p>Wat je beter niet doet: een tweede account openen of iemand anders voor je laten wedden. Een aanbieder mag per speler maar één speelrekening hebben en je verklaart bij inschrijving dat je alleen voor eigen rekening speelt. Wie dat omzeilt, riskeert dat het account wordt gesloten en dat de aanbieder de zaak als misbruik behandelt.</p>
<h3><strong>Wat is het verschil met speelgrenzen en de stortingslimiet?</strong></h3>
<p>Een accountbeperking door de bookmaker heeft niets te maken met de limieten die bedoeld zijn om jou te beschermen. Die worden vaak door elkaar gehaald:</p>
{tabel(["Soort limiet", "Wie bepaalt het?", "Waarom?"], [
    ("<strong>Accountbeperking</strong> (lagere maximale inzet)", "De bookmaker", "Commercieel: je kost hem naar verwachting geld"),
    ("<strong>Speelgrenzen</strong> (speeltijd, stortingen, saldo)", "Jij, verplicht bij inschrijving", "Bescherming: verlagen werkt direct, verhogen pas na ten minste een week"),
    ("<strong>Netto-stortingsgrens</strong> (€300 tot 24 jaar, €700 vanaf 24 per kalendermaand)", "De Ksa", "Bescherming: daarboven moet de aanbieder nagaan of je het kunt dragen"),
    ("<strong>Schorsing</strong>", "De bookmaker, op jouw verzoek of uit zorgplicht", "Bescherming of onderzoek, bijvoorbeeld bij signalen van gokproblemen"),
])}
<p>Meer over de grens van €300 en €700 lees je in ons artikel over de <a href="{NETTO}">netto stortingslimiet</a>. Merk je dat je je verliezen probeert terug te winnen bij een andere bookmaker, neem dan even afstand. Tips daarvoor vind je bij <a href="{VERANTWOORD}">verantwoord wedden</a>. Meer uitleg over wedden staat in de <a href="/wedgids">wedgids</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Is het legaal dat een bookmaker mijn account beperkt?</strong><br>Ja, voor zover wij kunnen nagaan. Geen Nederlandse regel verplicht een vergunde bookmaker om elke inzet te accepteren. Hij moet je wel je saldo laten opnemen en je klacht serieus behandelen.</p>
<p><strong>Krijg ik mijn saldo terug als mijn account beperkt of gesloten wordt?</strong><br>Ja. Je eigen tegoed moet zonder onnodige vertraging naar je eigen rekening worden betaald. Alleen bij een lopend onderzoek, bijvoorbeeld naar fraude of witwassen, kan dat tijdelijk worden opgeschort.</p>
<p><strong>Kan de Kansspelautoriteit mijn beperking ongedaan maken?</strong><br>Nee. De Ksa bemiddelt niet in individuele geschillen. Je kunt wel een melding doen; die gebruikt de Ksa voor haar toezicht.</p>
<p><strong>Wat is stake factoring?</strong><br>Een factor per account die bepaalt welk deel van de standaard maximale inzet je mag plaatsen. Bij een factor van {k(FACTOR)} en een standaardmaximum van {eur(MAX_STANDAARD, 0)} mag je {eur(MAX_JIJ, 0)} inzetten.</p>
<p><strong>Mag ik een nieuw account openen als mijn account beperkt is?</strong><br>Niet bij dezelfde aanbieder: per speler is maar één speelrekening toegestaan. Bij een andere legale bookmaker mag je je wel inschrijven.</p>
{KSA}"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    html = content + content2 + content3
    assert re.search(r"<(ul|ol|/li)>\s+<", html) is None
    assert "/kennisbank/" not in html and "<h2" not in html and "<h4" not in html and "/go/" not in html
    assert html.rstrip().endswith(KSA)
    assert content.startswith("<p><strong>")
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert TITEL.lower().startswith("account beperkt")
    assert len(OG_CHIPS) == 2 and len(OG_DATA) == 4 and html.count("<table") >= 3
    for link in (ODDS, VALUE, ARB, MATCHED, NETTO, LEGAAL, FREEBET, VERANTWOORD, "/wedgids"):
        assert f'href="{link}"' in html, link
    assert all(h.startswith("<h3><strong>") for h in re.findall(r"<h3>.*?</h3>", html))
    verboden = ("footymetrics", "betcity", "opstellingvandaag", "waaroptv")
    assert not any(v in html.lower() for v in verboden)
    faq = content3.split("Veelgestelde vragen")[1]
    assert 4 <= faq.count("<p><strong>") <= 6
    tekst = re.sub(r"<[^>]+>", " ", html)
    woorden = len(tekst.split())
    assert 1200 <= woorden <= 2200, woorden
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", woorden, "woorden |",
          [len(re.sub(r"<[^>]+>", " ", c).split()) for c in (content, content2, content3)])
    # ---- --live: NIET zelf draaien; alleen na akkoord van Jasper (bij voorkeur via wg_publiceer.py account-beperkt --live,
    #      dat ook de deelkaart en wedgids-categorie regelt) ----
    if "--live" in sys.argv:
        fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
              "samenvatting": SAMENVATTING, "rubriek": RUBRIEK, "wedgids": True,
              "publicatiedatum": datetime.now(timezone.utc).isoformat()}
        print("item:", WF.create_live(fd), "https://www.bet-experts.nl/nieuws/" + SLUG)
