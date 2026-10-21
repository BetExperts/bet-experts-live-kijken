# -*- coding: utf-8 -*-
"""Herschrijving Nieuws-item 65048c60f63856759c0c239b (Kennisbank-versie offline + 301): In-play / live wedden: hoe live odds
bewegen, cash out, bet delay, geschorste markten, wat live NIET mag in Nederland, strategie en risico's.
Feiten nagelopen op 21-10-2026:
- Bijlage 2, onderdeel 2.3 Regeling kansspelen op afstand (BWBR0044767): voetbal o.a. kaarten, inworpen, overtredingen,
  strafschoppen veroorzaken/nemen, buitenspel, hoekschoppen, wissels, blessurebehandelingen, extra tijd vierde official, VAR
  (incl. 'daaraan gerelateerde tijdstippen'); tennis: dubbele fout(en), challenges, straf scheidsrechter, winst/verlies van
  een specifieke game of set; handbal: uitsluitingen. Geldt ook live.
- Ksa sprak in 2026 een legale aanbieder aan die tijdens het WK live wedden op inworpen, overtredingen, hoekschoppen en
  buitenspel aanbood (zie corners_niet_legaal.py, Ksa 16-07-2026).
- Netto-stortingsgrens €300 (18 t/m 23 jaar) / €700 (24+) per kalendermaand sinds 1-10-2024 (zie netto_stortingslimiet.py).
- Cash-out- en oddsvoorbeelden zijn fictief; de 'eerlijke' cash-outwaarde wordt hieronder berekend en ge-assert.
  python3 specials/strategie_in_play.py [--live]"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
import lk_webflow as WF
from legaal_data import tabel, aanraders

ITEM_ID = "65048c60f63856759c0c239b"   # Nieuws
SLUG = "uitleg-in-play-live-wedden-dynamiek-strategie-en-kansen-in-realtime"
RUBRIEK = "6502b64b78efefb4144fd2c1"
TITEL = "Live wedden (in-play): zo werkt het en waar let je op?"
SAMENVATTING = ("Live wedden uitgelegd: hoe live odds bewegen, cash out met rekenvoorbeeld, bet delay, geschorste markten "
                "en welke live markten in NL niet mogen.")

OG_KOP = "Live <span>wedden</span>"
OG_EYEBROW = "In-play uitleg"
OG_CHIPS = ["Cash out uitgelegd", "Wat mag in NL?"]
OG_MOTIEF = "odds"
OG_DATA = ["Aftrap 0-0 · Ajax 1,80", "25' 0-1 · Ajax 3,40", "60' 1-1 · Ajax 2,30"]


def eur(x):
    return f"€{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def q(x):
    return f"{x:.2f}".replace(".", ",")


def pct(x):
    return f"{x * 100:.1f}%".replace(".", ",")


# odds-verloop (fictief) Ajax - AZ, quotering op Ajax-winst
VERLOOP = [("Aftrap", "0-0", 1.80, "Ajax is favoriet"), ("25e minuut", "0-1", 3.40, "AZ scoort, Ajax moet twee keer scoren"),
           ("60e minuut", "1-1", 2.30, "Ajax maakt gelijk en drukt door"), ("85e minuut", "1-1", 4.50, "Weinig tijd over, gelijkspel wordt waarschijnlijker")]
assert [pct(1 / o) for _, _, o, _ in VERLOOP] == ["55,6%", "29,4%", "43,5%", "22,2%"]
assert OG_DATA == [f"{'Aftrap' if t == 'Aftrap' else t.split('e ')[0] + chr(39)} {s} · Ajax {q(o)}" for t, s, o, _ in VERLOOP[:3]]

# cash out: €10 op Ajax-winst voor de aftrap tegen 2,00. Eerlijke waarde = inzet x oorspronkelijke odd / huidige live odd.
INZET, ODD = 10, 2.00
KORTING = 0.05   # voorbeeld: bookmaker biedt 5% minder dan de eerlijke waarde


def cash(live):
    eerlijk = INZET * ODD / live
    return eerlijk, eerlijk * (1 - KORTING)


CO = [("70e minuut, 1-0 voor Ajax", 1.25), ("85e minuut, 2-0 voor Ajax", 1.05), ("30e minuut, 0-1 achter", 3.00), ("75e minuut, 0-1 achter", 6.00)]
assert [eur(cash(o)[0]) for _, o in CO] == ["€16,00", "€19,05", "€6,67", "€3,33"]
assert [eur(cash(o)[1]) for _, o in CO] == ["€15,20", "€18,10", "€6,33", "€3,17"]
# gedeeltelijke cash out: helft (€5 inzet) uitcashen bij 1,25, rest loopt door tegen 2,00
assert eur(cash(1.25)[1] / 2) == "€7,60" and eur(5 * ODD) == "€10,00" and eur(cash(1.25)[1] / 2 + 5 * ODD) == "€17,60"

content = f"""<p><strong>Live wedden, ook in-play wedden genoemd, is wedden op een wedstrijd terwijl die al bezig is. De bookmaker past de quoteringen voortdurend aan op basis van de stand, de resterende tijd en wat er op het veld gebeurt. Na een doelpunt of een andere grote gebeurtenis gaat de markt even dicht. Met cash out kun je een lopende weddenschap vroegtijdig afrekenen. In Nederland mag je live alleen wedden op toegestane markten: corners, kaarten, inworpen en bij tennis de winnaar van een specifieke game of set zijn ook live verboden.</strong></p>
<p>Live wedden maakt een wedstrijd spannender, maar het tempo is ook het grootste risico: je beslist in seconden, vaak op gevoel. Hieronder lees je hoe live odds tot stand komen, hoe cash out werkt (met rekenvoorbeeld), waarom je inzet soms wordt geweigerd, welke live markten in Nederland niet zijn toegestaan en hoe je verstandig live wedt.</p>
<h3><strong>Hoe werken live odds?</strong></h3>
<p>Voor de aftrap is de quotering een inschatting van de kansen over 90 minuten. Tijdens de wedstrijd rekent de bookmaker die kans steeds opnieuw uit. Drie dingen tellen het zwaarst: de <strong>stand</strong>, de <strong>resterende tijd</strong> en de <strong>wedstrijdsituatie</strong>, zoals een rode kaart of een blessure. De quoteringen veranderen daardoor soms elke paar seconden.</p>
<p>Zo kan de quotering op Ajax-winst in een thuiswedstrijd tegen AZ verlopen:</p>
{tabel(["Moment", "Stand", "Quotering Ajax wint", "Kans volgens de quotering", "Waarom"], [
    (f"<strong>{t}</strong>", s, q(o), pct(1 / o), w) for t, s, o, w in VERLOOP
])}
<p><em>De quoteringen in dit voorbeeld zijn fictief en alleen bedoeld om het principe te laten zien.</em></p>
<p>De kans volgens de quotering is 1 gedeeld door de quotering. Die ligt altijd iets hoger dan de echte kans, omdat de bookmaker er een marge op zet. Bij live wedden is die marge vaak groter dan voor de wedstrijd, omdat de bookmaker meer risico loopt. Opvallend in de tabel: bij dezelfde stand (1-1) loopt de quotering op Ajax op naarmate de tijd verstrijkt. Tijd is live een van de belangrijkste factoren.</p>
<h3><strong>Welke live markten zijn er?</strong></h3>
<ul><li><strong>Winnaar (1X2) en dubbele kans:</strong> de bekendste live markt.</li><li><strong>Volgende doelpunt:</strong> welk team scoort als volgende, of komt er geen doelpunt meer.</li><li><strong>Over/under doelpunten:</strong> de lijn schuift mee met de stand, zoals meer dan 2,5 bij 1-1. Zie onze <a href="/wedtips/over-2-5-goals-tips-voorspellingen">over 2,5 goals tips</a>.</li><li><strong>Beide teams scoren</strong> en <strong>doelpuntenmakers</strong>.</li><li><strong>Live handicap:</strong> bij veel bookmakers telt bij een live Asian handicap alleen wat er gebeurt ná het plaatsen van je weddenschap. Lees meer over <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap wedden</a>.</li><li><strong>Tennis en basketbal:</strong> winnaar van de wedstrijd, totaal aantal games of punten, en handicaps over de hele wedstrijd.</li></ul>"""

content2 = f"""<h3><strong>Wat is cash out?</strong></h3>
<p>Met cash out reken je een lopende weddenschap af voordat de wedstrijd voorbij is. De bookmaker doet je een bod op basis van de huidige live quotering. Neem je het aan, dan is de weddenschap klaar: je krijgt dat bedrag, wat er daarna ook gebeurt.</p>
<p>Je kunt het bod zelf ongeveer narekenen. De eerlijke waarde is je inzet keer je oorspronkelijke quotering, gedeeld door de huidige live quotering op dezelfde uitkomst. In de praktijk biedt de bookmaker iets minder, omdat hij er ook aan wil verdienen.</p>
<p><strong>Voorbeeld: €10 op Ajax-winst tegen 2,00</strong></p>
{tabel(["Moment", "Live quotering Ajax", "Eerlijke waarde", "Bod bookmaker (voorbeeld)"], [
    (f"<strong>{m}</strong>", q(o), eur(cash(o)[0]), eur(cash(o)[1])) for m, o in CO
])}
<p><em>In dit fictieve voorbeeld biedt de bookmaker 5% minder dan de eerlijke waarde. Dat verschil is per bookmaker en per moment anders.</em></p>
<p>Je ziet twee dingen. Staat Ajax voor, dan stijgt het bod richting de volledige uitbetaling van €20. Staat Ajax achter, dan kun je nog een deel van je inzet redden. In beide gevallen lever je een stukje in ten opzichte van de eerlijke waarde. Cash out is dus geen gratis verzekering: het is een tweede weddenschap tegen een quotering met marge.</p>
<p><strong>Gedeeltelijke cash out.</strong> Bij veel bookmakers kun je ook een deel uitcashen. Cash je in het eerste voorbeeld de helft uit, dan krijg je nu {eur(cash(1.25)[1] / 2)} en loopt €5 door tegen 2,00. Wint Ajax, dan krijg je in totaal {eur(cash(1.25)[1] / 2 + 5 * ODD)} terug.</p>
<p>Cash out is niet altijd beschikbaar. Tijdens een geschorste markt, bij sommige wedopties of vlak voor het einde kan de knop verdwijnen. Reken er dus nooit op dat je altijd kunt uitstappen.</p>
<h3><strong>Wat is een bet delay?</strong></h3>
<p>Plaats je live een weddenschap, dan wordt die vaak niet direct geaccepteerd. De bookmaker wacht een paar seconden: de <strong>bet delay</strong>. Gebeurt er in die seconden iets belangrijks, zoals een doelpunt of een gevaarlijke aanval, dan kan je weddenschap worden geweigerd of krijg je een nieuwe quotering voorgelegd.</p>
<p>Dat heeft een reden. Een tv-uitzending of livestream loopt vaak een aantal seconden achter op de werkelijkheid, terwijl de bookmaker zijn gegevens direct van het stadion krijgt. Zonder bet delay zouden spelers met snellere informatie kunnen wedden op iets wat al gebeurd is. In je account kun je vaak instellen of je hogere of alle gewijzigde quoteringen automatisch accepteert. Kijk je de wedstrijd mee, kijk dan bij <a href="/live-kijken">live kijken</a> waar hij te zien is.</p>
<h3><strong>Waarom is een markt geschorst?</strong></h3>
<p>Bij grote momenten zet de bookmaker een markt even op slot. Je ziet dan "geschorst", "gesloten" of een slotje. Dat gebeurt bijvoorbeeld bij:</p>
<ul><li>een doelpunt of een doelpunt dat wordt gecontroleerd;</li><li>een strafschop of een gevaarlijke vrije trap;</li><li>een VAR-check of een rode kaart;</li><li>een blessure of een onderbreking, en bij tennis vaak tussen punten op cruciale momenten.</li></ul>
<p>Zodra de situatie duidelijk is, gaat de markt weer open met nieuwe quoteringen. Weddenschappen die je eerder had geplaatst blijven gewoon staan.</p>"""

content3 = f"""<h3><strong>Welke live markten mogen niet in Nederland?</strong></h3>
<p>Voor live wedden gelden dezelfde regels als voor wedden vooraf. In de Regeling kansspelen op afstand staat een lijst met gebeurtenissen waarop legale bookmakers geen weddenschappen mogen aanbieden, omdat ze makkelijk te manipuleren of negatief zijn. Live zijn juist dit soort markten in het buitenland populair, maar in Nederland zie je ze niet.</p>
{tabel(["Sport", "Live niet toegestaan", "Live wel toegestaan (voorbeelden)"], [
    ("<strong>Voetbal</strong>", "Corners, gele en rode kaarten, inworpen, overtredingen, wie een strafschop veroorzaakt of neemt, buitenspel, wissels, blessurebehandelingen, de extra tijd van de vierde official, VAR-momenten, en het tijdstip waarop die gebeurtenissen plaatsvinden", "Winnaar, volgende doelpunt, over/under doelpunten, beide teams scoren, doelpuntenmakers, handicap, schoten op doel"),
    ("<strong>Tennis</strong>", "Winnaar van een specifieke game of set, dubbele fouten, challenges, straffen van de scheidsrechter", "Winnaar van de wedstrijd, totaal aantal games, game- of set-handicap over de hele wedstrijd"),
    ("<strong>Handbal</strong>", "Tijdelijke en definitieve uitsluitingen", "Winnaar, handicap, totaal aantal doelpunten"),
])}
<p>Vooral de tennisregel verrast veel wedders: "wie wint de volgende game" is in het buitenland een van de drukste live markten, maar in Nederland niet toegestaan. De Kansspelautoriteit controleert dit ook actief: in 2026 sprak de toezichthouder nog een legale aanbieder aan die tijdens het WK live weddenschappen aanbood op inworpen, overtredingen, corners en buitenspel. Lees meer in ons artikel <a href="/nieuws/dit-is-waarom-wedden-op-corners-niet-meer-legaal-is-in-nederland">waarom wedden op corners niet legaal is</a>.</p>
<p>Zie je een wedsite die deze markten wel live aanbiedt aan Nederlandse spelers? Dan is dat bijna altijd een site zonder Nederlandse vergunning. Daar spelen is illegaal en je hebt er geen enkele bescherming. Lees <a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je herkent of een bookmaker legaal is</a>.</p>
<h3><strong>Strategietips voor live wedden</strong></h3>
<ul><li><strong>Maak vooraf een plan.</strong> Bepaal voor de aftrap op welke situatie je wacht, bijvoorbeeld een vroege achterstand van een favoriet, en hoeveel je maximaal inzet.</li><li><strong>Wed niet op wat je net zag.</strong> Zag je een grote kans, dan heeft de bookmaker die informatie ook al verwerkt. De quotering is dan al aangepast.</li><li><strong>Let op de tijd.</strong> Bij een gelijke stand dalen de quoteringen op een gelijkspel en over-markten veranderen snel richting het einde.</li><li><strong>Kijk naar de wedstrijd, niet alleen naar de cijfers.</strong> Statistieken zoals balbezit zeggen weinig als een ploeg geen echte kansen creëert.</li><li><strong>Vergelijk quoteringen.</strong> Ook live verschillen bookmakers. Gebruik voor de aftrap onze <a href="/odds-vergelijken-bij-alle-bookmakers-beste-odds-vandaag">odds vergelijker</a> om een beeld te krijgen.</li><li><strong>Gebruik cash out bewust.</strong> Uitcashen omdat je zenuwachtig bent, kost je op lange termijn geld. Doe het alleen als je inschatting echt veranderd is.</li></ul>
<h3><strong>Wat zijn de risico's van live wedden?</strong></h3>
<p>Live wedden is de snelste vorm van sportwedden, en dat maakt het riskanter dan wedden vooraf. Je kunt in één wedstrijd tientallen weddenschappen plaatsen, vaak in een emotionele bui. Verlies je een weddenschap, dan is de verleiding groot om het direct terug te willen winnen. Dat najagen van verlies is een van de belangrijkste signalen van probleemgedrag.</p>
<ul><li><strong>Stel limieten in.</strong> Legale bookmakers laten je een stortings-, verlies- en speeltijdlimiet instellen. Daarnaast geldt een netto-stortingsgrens van €300 per maand tot en met 23 jaar en €700 per maand vanaf 24 jaar.</li><li><strong>Speel met een vast bedrag per wedstrijd</strong> en stop als dat op is.</li><li><strong>Neem een pauze</strong> als je merkt dat je wedt om een verlies goed te maken.</li><li><strong>Hulp nodig?</strong> Via Cruks kun je jezelf uitsluiten bij alle legale aanbieders. Lees meer over <a href="/speel-bewust/verantwoord-wedden">verantwoord wedden</a>.</li></ul>
<h3><strong>Mag je in Nederland live wedden?</strong></h3>
<p>Ja. Live wedden is in Nederland toegestaan bij bookmakers met een vergunning van de Kansspelautoriteit, zolang het om toegestane markten gaat. Bijna alle legale bookmakers bieden live wedden aan, vaak met cash out. Bekijk alle beoordelingen op onze pagina <a href="/bookmakers">bookmakers</a>.</p>
<p>Legale bookmakers die wij aanraden:</p>
{aanraders()}
<h3><strong>Veelgestelde vragen over live wedden</strong></h3>
<p><strong>Wat is in-play wedden?</strong><br>Hetzelfde als live wedden: je plaatst een weddenschap terwijl de wedstrijd al bezig is, tegen quoteringen die continu veranderen.</p>
<p><strong>Hoe wordt een cash-outbedrag berekend?</strong><br>Ongeveer als inzet keer oorspronkelijke quotering, gedeeld door de huidige live quotering, min een marge voor de bookmaker. €10 tegen 2,00 met een live quotering van 1,25 is eerlijk {eur(cash(1.25)[0])}; het bod ligt meestal iets lager.</p>
<p><strong>Waarom wordt mijn live weddenschap geweigerd?</strong><br>Door de bet delay. Gebeurt er in de seconden na het plaatsen iets belangrijks, of is de quotering veranderd, dan weigert de bookmaker de weddenschap of vraagt hij je een nieuwe quotering te accepteren.</p>
<p><strong>Mag je live wedden op corners of kaarten?</strong><br>Nee. Corners, kaarten, inworpen, overtredingen en buitenspel zijn in Nederland verboden markten, ook live.</p>
<p><strong>Mag je in Nederland wedden op wie de volgende game wint bij tennis?</strong><br>Nee. Wedden op de winst of het verlies van een specifieke game of set is in Nederland niet toegestaan. Wedden op de winnaar van de wedstrijd of het totaal aantal games mag wel.</p>
<p><strong>Is live wedden winstgevender dan wedden vooraf?</strong><br>Nee, niet vanzelf. Live marges zijn vaak hoger en de bookmaker heeft snellere data dan jij. Live wedden geeft wel meer mogelijkheden, maar vraagt ook meer discipline.</p>
<p><strong>Telt bij een live handicap de stand mee?</strong><br>Bij veel bookmakers niet: bij een live Asian handicap telt vaak alleen wat er na het plaatsen gebeurt, alsof het 0-0 staat. Lees altijd de regels bij de markt.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    from datetime import datetime, timezone
    alles = content + content2 + content3
    tekst = re.sub(r"<[^>]+>", " ", alles)
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", len(tekst.split()), "woorden")
    assert not re.search(r"<(ul|ol|/li)>\s+<", alles) and "/kennisbank/" not in alles
    # ---- --live: alleen handmatig draaien na akkoord ----
    if "--live" in sys.argv:
        fd = {"name": TITEL, "content": content, "content-2": content2, "content-3": content3,
              "samenvatting": SAMENVATTING, "rubriek": RUBRIEK, "publicatiedatum": datetime.now(timezone.utc).isoformat()}
        print(WF.update_live(ITEM_ID, fd).get("lastPublished"))
