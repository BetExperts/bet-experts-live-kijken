# -*- coding: utf-8 -*-
"""Herschrijving Nieuws-item 6504860be48715c9bfc940c6 (oude Kennisbank-versie is offline + 301 naar deze Nieuws-versie):
Wedden op gelijkspel met de Fibonacci wedstrategie.
Alle bedragen en kansen worden hieronder in Python berekend en met assert gecontroleerd.
Feiten (nagelopen 21-10-2026, uitgerekend uit de complete wedstrijduitslagen per seizoen):
- Eredivisie 2025/26 (8-8-2025 t/m 17-5-2026): 306 wedstrijden, 80 gelijk = 26,1%. Eredivisie 2024/25: 77/306 = 25,2%.
- Top-5 competities samen (PL, LaLiga, Bundesliga, Serie A, Ligue 1) 2025/26: 446/1.752 = 25,5%.
- Eredivisie 2025/26 per club: PSV 3 gelijke spelen in 34 duels, Go Ahead Eagles 14; langste reeks zonder gelijkspel
  13 duels (PSV en Heracles). Tussenstanden uit het seizoen (PSV 2 gelijk na 29, GAE 10 gelijk na 20) bevestigen dit beeld.
- Gemiddelde vooraf-quotering op gelijkspel Eredivisie 2025/26 ca. 4,3 (mediaan ca. 3,9).
- Netto stortingslimiet Ksa: €300 p/m tot 24 jaar, €700 vanaf 24 (Beleidsregel verantwoord spelen 2024).
  python3 specials/strategie_fibonacci.py [--live]"""
import os, sys, re
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel, aanraders

ITEM_ID = "6504860be48715c9bfc940c6"   # Nieuws
SLUG = "wedden-op-gelijkspel-de-fibonacci-wedstrategie-onder-de-loep"
RUBRIEK = "6502b64b78efefb4144fd2c1"
TITEL = "Fibonacci gok strategie: wedden op gelijkspel uitgelegd"
SAMENVATTING = ("De Fibonacci wedstrategie op gelijkspel uitgelegd: de reeks, twee stappen terug, rekentabel bij odds 3,20, "
                "risico's en hoe vaak het echt gelijk wordt.")

OG_KOP = "Fibonacci op <span>gelijkspel</span>"
OG_EYEBROW = "Wedstrategie uitgelegd"
OG_CHIPS = ["1-1-2-3-5-8-13", "Rekentabel odds 3,20"]
OG_MOTIEF = "reeks"
OG_DATA = ["€10", "€10", "€20", "€30", "€50", "€80"]


# ---------- rekenhulpjes ----------
def eur(x):
    x = round(x + 0.0, 2)
    if abs(x - round(x)) < 0.005:
        return f"€{int(round(x)):,}".replace(",", ".").replace("€-", "−€")
    return f"€{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".").replace("€-", "−€")


def plus(x):
    return ("+" if x > 0 else "") + eur(x)


def pct(x, d=1):
    return f"{x * 100:.{d}f}%".replace(".", ",")


def p_reeks(q, k, n):
    """Kans op minstens één reeks van k verliezen op rij in n weddenschappen (verlieskans q)."""
    st, hit = [1.0] + [0.0] * (k - 1), 0.0
    for _ in range(n):
        nieuw = [0.0] * k
        for r, pr in enumerate(st):
            nieuw[0] += pr * (1 - q)
            if r + 1 == k:
                hit += pr * q
            else:
                nieuw[r + 1] += pr * q
        st = nieuw
    return hit


EENHEID, ODD = 10, 3.20
FIB = [1, 1]
while len(FIB) < 13:
    FIB.append(FIB[-1] + FIB[-2])
assert FIB[:10] == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# 1) progressietabel bij odds 3,20 (en ter vergelijking het resultaat bij odds 2,00)
RIJEN = []
cum = 0
for n, f in enumerate(FIB[:10], 1):
    inzet = f * EENHEID
    cum += inzet
    RIJEN.append((n, inzet, cum, round(inzet * ODD, 2), round(inzet * ODD - cum, 2), inzet * 2 - cum))
assert [r[4] for r in RIJEN] == [22, 12, 24, 26, 40, 56, 86, 132, 208, 330]
assert [r[5] for r in RIJEN][:6] == [10, 0, 0, -10, -20, -40]
assert RIJEN[9][2] == 1430

# 2) voorbeeld met de regel 'twee stappen terug' bij odds 3,20 (V = verlies, W = gelijkspel = winst)
VOORBEELD = "VVVVVWVWW"
idx, saldo, VB_RIJEN = 0, 0.0, []
for i, u in enumerate(VOORBEELD, 1):
    stap, inzet = idx + 1, FIB[idx] * EENHEID
    res = inzet * (ODD - 1) if u == "W" else -inzet
    saldo = round(saldo + res, 2)
    VB_RIJEN.append((i, f"stap {stap}", eur(inzet), "gelijkspel" if u == "W" else "geen gelijkspel", plus(res), plus(saldo)))
    idx = max(0, idx - 2) if u == "W" else idx + 1
assert saldo == 180 and VB_RIJEN[5][5] == "+€56"

# 3) martingale vs Fibonacci: inzet en totaal na x verliezen (eenheid €10)
VERGELIJK = []
for k in (3, 5, 8, 10):
    VERGELIJK.append((k, EENHEID * 2 ** k, EENHEID * (2 ** k - 1), FIB[k] * EENHEID, sum(FIB[:k]) * EENHEID))
assert VERGELIJK[3] == (10, 10240, 10230, 890, 1430)

# 4) gelijkspelpercentages (seizoensdata, zie docstring)
ERE_2526, ERE_2425, TOP5_2526 = (80, 306), (77, 306), (446, 1752)
assert pct(80 / 306) == "26,1%" and pct(77 / 306) == "25,2%" and pct(446 / 1752) == "25,5%"
BREAKEVEN = 1 / ODD
assert pct(BREAKEVEN, 2) == "31,25%"

# 5) kans op reeksen zonder gelijkspel bij 26,1% gelijkspelkans
Q = 1 - 80 / 306
REEKS = [(k, Q ** k, p_reeks(Q, k, 50), p_reeks(Q, k, 100)) for k in (5, 8, 10, 13)]
assert pct(REEKS[0][1]) == "22,0%" and pct(REEKS[2][1]) == "4,8%" and pct(REEKS[2][3]) == "74,6%"
assert pct(REEKS[1][2]) == "73,6%"
BANK_13 = sum(FIB[:13]) * EENHEID
assert BANK_13 == 6090

# 6) verwachte waarde: stel echte kans 30% bij odds 3,20
assert round(0.30 * ODD - 1, 3) == -0.04


content = f"""<p><strong>De Fibonacci wedstrategie is een inzetsysteem waarbij je inzet de getallenreeks 1, 1, 2, 3, 5, 8, 13 volgt. Verlies je, dan schuif je een stap op in de reeks. Win je, dan ga je twee stappen terug. Het wordt vaak gebruikt bij wedden op gelijkspel, omdat de quotering daar meestal 3,00 of hoger is. De inzet stijgt trager dan bij martingale, maar het systeem verandert niets aan je kans en garandeert geen winst.</strong></p>
<p>Wedden op gelijkspel heeft iets aantrekkelijks: hogere quoteringen en het gevoel dat een remise "er wel een keer aan komt". De Fibonacci-reeks geeft dat gevoel een vaste structuur. Hieronder lees je hoe het systeem werkt, zie je een rekentabel bij odds 3,20, vergelijken we het met martingale en kijken we naar de cijfers: hoe vaak eindigt een wedstrijd eigenlijk in een gelijkspel?</p>
<h3><strong>Wat is de Fibonacci-reeks?</strong></h3>
<p>De Fibonacci-reeks is een getallenreeks waarin elk getal de som is van de twee getallen ervoor: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 enzovoort. In de wiskunde en de natuur duikt de reeks overal op. Bij wedden gebruik je hem als ladder voor je inzet: elk getal is een aantal eenheden. Met een eenheid van €10 zet je dus €10, €10, €20, €30, €50, €80 in.</p>
<h3><strong>Hoe werkt de Fibonacci wedstrategie?</strong></h3>
<ol><li><strong>Kies je eenheid,</strong> bijvoorbeeld €10, en begin bij het eerste getal van de reeks.</li><li><strong>Verlies je, dan ga je één stap verder</strong> in de reeks en zet je dat aantal eenheden in.</li><li><strong>Win je, dan ga je twee stappen terug.</strong> Sta je op stap 1 of 2, dan begin je opnieuw bij het begin.</li><li><strong>De reeks is klaar</strong> als je weer bij stap 1 bent en je verliezen zijn goedgemaakt.</li></ol>
<p>De regel "twee stappen terug" komt uit de oorspronkelijke versie voor weddenschappen met odds rond de 2,00. Bij die odds maakt één winst niet al je verliezen goed, zie de laatste kolom in de tabel hieronder. Daarom heb je meestal twee winsten nodig om een verliesreeks weg te werken.</p>
<h3><strong>Rekenvoorbeeld: Fibonacci op gelijkspel bij odds 3,20</strong></h3>
<p>Je zet elke keer in op een gelijkspel tegen een quotering van 3,20. In de tabel zie je je inzet per stap, wat je in totaal hebt ingezet en wat je overhoudt als het in die stap gelijk wordt. De quoteringen in dit voorbeeld zijn fictief.</p>
{tabel(["Stap", "Inzet", "Totaal ingezet", "Uitbetaling bij gelijkspel", "Netto bij odds 3,20", "Netto bij odds 2,00"],
       [(f"<strong>{r[0]}</strong>", eur(r[1]), eur(r[2]), eur(r[3]), plus(r[4]), plus(r[5])) for r in RIJEN])}
<p>Bij odds 3,20 maakt elk gelijkspel de hele reeks goed en houd je er iets aan over. Daarom beginnen veel gelijkspelwedders na een winst gewoon opnieuw bij stap 1. Bij odds 2,00 sta je vanaf stap 4 ondanks je winst nog in de min, en dan is de regel "twee stappen terug" nodig.</p>"""

content2 = f"""<h3><strong>Voorbeeld met de regel "twee stappen terug"</strong></h3>
<p>Zo verloopt een reeks van negen weddenschappen op gelijkspel bij odds 3,20, als je na elke winst twee stappen teruggaat:</p>
{tabel(["Bet", "Stap", "Inzet", "Uitkomst", "Resultaat", "Saldo"], VB_RIJEN)}
<p>Dit voorbeeld loopt goed af: drie gelijke spelen in negen wedstrijden is 33%. Dat is meer dan je gemiddeld mag verwachten. Haal je in dezelfde negen wedstrijden maar één gelijkspel, of komt de remise pas na tien wedstrijden, dan ziet het saldo er heel anders uit.</p>
<h3><strong>Hoe vaak eindigt een wedstrijd in een gelijkspel?</strong></h3>
<p>Een gelijkspel voelt vaak als een uitkomst die "eraan zit te komen", maar de cijfers zijn nuchter:</p>
{tabel(["Competitie", "Seizoen", "Wedstrijden", "Gelijk", "Percentage"], [
    ("<strong>Eredivisie</strong>", "2025/26", ERE_2526[1], ERE_2526[0], pct(ERE_2526[0] / ERE_2526[1])),
    ("<strong>Eredivisie</strong>", "2024/25", ERE_2425[1], ERE_2425[0], pct(ERE_2425[0] / ERE_2425[1])),
    ("<strong>Top-5 competities samen</strong>", "2025/26", f"{TOP5_2526[1]:,}".replace(",", "."), TOP5_2526[0], pct(TOP5_2526[0] / TOP5_2526[1])),
])}
<p><em>Top-5 competities: Premier League, LaLiga, Bundesliga, Serie A en Ligue 1.</em></p>
<p>Ongeveer één op de vier wedstrijden eindigt dus gelijk. Bij een quotering van 3,20 moet een gelijkspel in meer dan {pct(BREAKEVEN, 2)} van de gevallen vallen om quitte te spelen. Die 3,20 zie je vooral bij wedstrijden tussen twee gelijkwaardige teams, waar de kans op een gelijkspel ook hoger ligt dan gemiddeld. Bij duels met een duidelijke favoriet staat het gelijkspel eerder op 4,00 of hoger, juist omdat de kans kleiner is.</p>
<p>Per club zijn de verschillen groot. In de Eredivisie van 2025/26 speelde PSV maar drie keer gelijk in 34 wedstrijden, terwijl Go Ahead Eagles er veertien noteerde. PSV en Heracles gingen allebei dertien duels op rij zonder gelijkspel. Wie met een Fibonacci-reeks op de gelijkspellen van één van die clubs had gewed, verloor dertien keer op rij en had met een eenheid van €10 in totaal {eur(BANK_13)} ingezet.</p>
<h3><strong>Hoe groot is de kans op een lange reeks zonder gelijkspel?</strong></h3>
<p>Uitgaande van een gelijkspelkans van {pct(1 - Q)}, zoals in de Eredivisie van 2025/26, is dit de kans dat je een reeks zonder gelijkspel meemaakt:</p>
{tabel(["Geen gelijkspel op rij", "Kans per reeks", "Minstens één keer in 50 bets", "In 100 bets", "Totaal ingezet (eenheid €10)"],
       [(f"<strong>{k}</strong>", pct(p1), pct(p50), pct(p100), eur(sum(FIB[:k]) * EENHEID)) for k, p1, p50, p100 in REEKS])}
<p>Een reeks van tien wedstrijden zonder gelijkspel is dus geen pech, maar iets wat je bij honderd weddenschappen in {pct(REEKS[2][3])} van de gevallen minstens één keer tegenkomt. Op dat moment heb je {eur(RIJEN[9][2])} ingezet en is je volgende inzet {eur(FIB[10] * EENHEID)}.</p>
<h3><strong>Fibonacci vergeleken met martingale</strong></h3>
<p>Bij <a href="/nieuws/wat-is-het-martingale-systeem-een-dubbel-of-niets-wedstrategie">het martingale systeem</a> verdubbel je na elk verlies. Fibonacci stijgt trager, en dat is het grootste verschil:</p>
{tabel(["Na zoveel verliezen", "Martingale: volgende inzet", "Martingale: totaal ingezet", "Fibonacci: volgende inzet", "Fibonacci: totaal ingezet"],
       [(f"<strong>{k}</strong>", eur(a), eur(b), eur(c), eur(d)) for k, a, b, c, d in VERGELIJK])}
<p>Fibonacci is dus minder explosief. Daar staat tegenover dat je bij odds rond de 2,00 vaak meerdere winsten nodig hebt om een reeks af te sluiten, en dat de reeks bij gelijkspellen langer kan duren dan bij een 50/50-markt. Beide systemen veranderen de kans op de uitkomst niet.</p>"""

content3 = f"""<h3><strong>De risico's van de Fibonacci strategie</strong></h3>
<ul><li><strong>Geen invloed op je kans.</strong> Een inzetsysteem bepaalt alleen hoeveel je inzet, niet of het gelijk wordt. Is de echte kans op een gelijkspel bijvoorbeeld 30% bij een quotering van 3,20, dan verlies je gemiddeld 4% van elke inzet, met of zonder Fibonacci.</li><li><strong>Lange reeksen kosten veel.</strong> Tien keer geen gelijkspel betekent {eur(RIJEN[9][2])} aan inzet bij een eenheid van €10.</li><li><strong>Marge van de bookmaker.</strong> Op gelijkspel rekenen bookmakers hun marge net zo goed mee. Kleine verschillen in quotering tellen op over een hele reeks.</li><li><strong>Limieten.</strong> Bookmakers hebben een maximuminzet per weddenschap en kunnen de limieten van een account aanpassen.</li><li><strong>Verliezen najagen.</strong> Een systeem dat je inzet na verlies verhoogt, voelt als terugwinnen. Precies dat gedrag maakt gokken riskant.</li></ul>
<h3><strong>Hoe pas je de Fibonacci strategie verstandig toe?</strong></h3>
<ul><li><strong>Leg vooraf een eindpunt vast,</strong> bijvoorbeeld stap 6 ({eur(sum(FIB[:6]) * EENHEID)} in totaal bij €10). Haal je dat zonder gelijkspel, dan stop je de reeks en accepteer je het verlies.</li><li><strong>Kies een kleine eenheid.</strong> Met €2 in plaats van €10 kost een reeks van tien verliezen {eur(sum(FIB[:10]) * 2)} in plaats van {eur(RIJEN[9][2])}.</li><li><strong>Kies wedstrijden, geen blind systeem.</strong> Gelijkwaardige teams en wedstrijden met weinig doelpunten geven een grotere kans op een remise dan een duel met een topfavoriet. Onze <a href="/wedtips">wedtips</a> helpen je bij het inschatten.</li><li><strong>Vergelijk quoteringen.</strong> Of je 3,20 of 3,40 krijgt, maakt bij elke winst verschil. Gebruik de <a href="/odds-vergelijken-bij-alle-bookmakers-beste-odds-vandaag">odds vergelijker</a>.</li><li><strong>Zoek value in plaats van een systeem.</strong> Alleen als jouw kans hoger is dan de quotering aangeeft, heb je op termijn een voordeel. Lees hoe dat werkt bij <a href="/nieuws/wat-is-de-wedstrategie-value-betting">value betting</a>.</li></ul>
<p>Op zoek naar andere nieuwe wedden strategieën? In het overzicht van <a href="/nieuws/alle-verschillende-wedstrategieen-op-een-rijtje">alle wedstrategieën</a> zie je ze naast elkaar, met het risico en voor wie ze geschikt zijn.</p>
<h3><strong>Mag je de Fibonacci strategie gebruiken in Nederland?</strong></h3>
<p>Ja. Wedden op een gelijkspel is een gewone 1X2-weddenschap en een inzetsysteem is niet verboden. Doe het wel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit. Spelen bij een aanbieder zonder Nederlandse vergunning is illegaal. Bij legale aanbieders geldt bovendien een netto stortingslimiet van €300 per maand tot je 24e en €700 daarna, wat bij een lange Fibonacci-reeks snel in beeld komt. Weet je niet zeker of je bookmaker legaal is? Lees <a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je dat controleert</a>.</p>
<p>Legale bookmakers die wij aanraden:</p>
{aanraders()}
<h3><strong>Veelgestelde vragen over de Fibonacci wedstrategie</strong></h3>
<p><strong>Wat is de Fibonacci gok strategie?</strong><br>Een inzetsysteem waarbij je inzet de reeks 1, 1, 2, 3, 5, 8, 13 volgt. Na een verlies ga je één stap verder, na een winst twee stappen terug.</p>
<p><strong>Waarom wordt Fibonacci vaak gebruikt bij gelijkspel?</strong><br>Een gelijkspel heeft meestal een quotering van 3,00 of hoger. Eén winst maakt dan een hele reeks goed, terwijl de inzet trager stijgt dan bij verdubbelen.</p>
<p><strong>Hoe vaak eindigt een voetbalwedstrijd in een gelijkspel?</strong><br>Ongeveer een kwart van de wedstrijden. In de Eredivisie van 2025/26 was het {pct(ERE_2526[0] / ERE_2526[1])}, in de top-5 competities samen {pct(TOP5_2526[0] / TOP5_2526[1])}.</p>
<p><strong>Is Fibonacci veiliger dan martingale?</strong><br>Minder explosief, niet veilig. Na tien verliezen heb je met €10 als eenheid {eur(RIJEN[9][2])} ingezet, tegen {eur(VERGELIJK[3][2])} bij martingale. Beide systemen verliezen op termijn als de quotering te laag is voor de echte kans.</p>
<p><strong>Wat betekent twee stappen terug?</strong><br>Win je op bijvoorbeeld stap 6 (€80), dan is je volgende inzet die van stap 4 (€30). Sta je op stap 1 of 2, dan begin je opnieuw.</p>
<p><strong>Kun je met de Fibonacci strategie winst garanderen?</strong><br>Nee. Geen inzetsysteem garandeert winst. Een lange reeks zonder gelijkspel kan meer kosten dan je in maanden met kleine winsten hebt opgebouwd.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    alles = content + content2 + content3
    tekst = re.sub(r"<[^>]+>", " ", alles)
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", len(tekst.split()), "woorden")
    assert not re.search(r"<(ul|ol|/li)>\s+<", alles) and "/kennisbank/" not in alles
    assert alles.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>") and "<h2" not in alles
    if "--live" in sys.argv:   # ---- LIVE: alleen draaien na akkoord van Jasper ----
        import lk_webflow as WF
        fd = {"name": TITEL, "content": content, "content-2": content2, "content-3": content3,
              "samenvatting": SAMENVATTING, "rubriek": RUBRIEK,
              "publicatiedatum": datetime.now(timezone.utc).isoformat()}
        print(WF.update_live(ITEM_ID, fd).get("lastPublished"))
