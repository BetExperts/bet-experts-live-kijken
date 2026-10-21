# -*- coding: utf-8 -*-
"""Herschrijving Nieuws-item 650488f9e48715c9bfccbacd (oude Kennisbank-versie is offline + 301 naar deze Nieuws-versie):
Wat is het martingale systeem? Dubbel-of-niets bij sportweddenschappen en roulette.
Alle bedragen en kansen worden hieronder in Python berekend en met assert gecontroleerd.
Feiten (nagelopen 21-10-2026):
- Europese roulette: 37 vakken (0-36), 18 rood -> winkans 18/37 = 48,65%, huisvoordeel 1/37 = 2,70%.
  Amerikaanse roulette 38 vakken (0 en 00) -> 47,37%. La Partage (Franse roulette) halveert het verlies bij nul -> 1,35%.
- Netto stortingslimiet Ksa (Beleidsregel verantwoord spelen 2024, sinds 1-10-2024): €300 p/m tot 24 jaar, €700 vanaf 24
  (zie specials/netto_stortingslimiet.py).
- Verliesreeks-kansen: exacte kans op minimaal één reeks van k verliezen in N weddenschappen (dynamisch programmeren).
  python3 specials/strategie_martingale.py [--live]"""
import os, sys, re
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel, aanraders

ITEM_ID = "650488f9e48715c9bfccbacd"   # Nieuws
SLUG = "wat-is-het-martingale-systeem-een-dubbel-of-niets-wedstrategie"
RUBRIEK = "6502b64b78efefb4144fd2c1"
TITEL = "Martingale systeem: zo werkt het en daarom faalt het"
SAMENVATTING = ("Het martingale systeem uitgelegd: verdubbelen na verlies, rekentabel bij odds 2,00 en 1,90, roulette, "
                "verliesreeksen, limieten en Paroli.")

OG_KOP = "Martingale <span>systeem</span>"
OG_EYEBROW = "Wedstrategie uitgelegd"
OG_CHIPS = ["Verdubbelen na verlies", "Rekentabel odds 2,00"]
OG_MOTIEF = "reeks"
OG_DATA = ["€10", "€20", "€40", "€80", "€160"]


# ---------- rekenhulpjes ----------
def eur(x):
    x = round(x + 0.0, 2)
    if abs(x - round(x)) < 0.005:
        return f"€{int(round(x)):,}".replace(",", ".").replace("€-", "−€")
    return f"€{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".").replace("€-", "−€")


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


BASIS = 10

# 1) klassieke martingale bij odds 2,00
RIJEN_200 = []
totaal = 0
for n in range(1, 11):
    inzet = BASIS * 2 ** (n - 1)
    totaal += inzet
    uit = inzet * 2.0
    RIJEN_200.append((n, inzet, totaal, uit, uit - totaal))
assert all(r[4] == BASIS for r in RIJEN_200)
assert RIJEN_200[5][1:3] == (320, 630) and RIJEN_200[7][1:3] == (1280, 2550) and RIJEN_200[9][1:3] == (5120, 10230)

# 2) gewoon verdubbelen bij odds 1,90
RIJEN_190 = []
totaal = 0
for n in range(1, 9):
    inzet = BASIS * 2 ** (n - 1)
    totaal += inzet
    uit = round(inzet * 1.90, 2)
    RIJEN_190.append((n, inzet, totaal, uit, round(uit - totaal, 2)))
assert [r[4] for r in RIJEN_190] == [9, 8, 6, 2, -6, -22, -54, -118]

# 3) aangepaste inzet bij odds 1,90: verlies + €9 terugwinnen, afgerond naar boven op hele euro's
import math
RIJEN_190B = []
verlies = 0
for n in range(1, 9):
    inzet = BASIS if n == 1 else math.ceil((verlies + 9) / 0.90)
    uit = round(inzet * 1.90, 2)
    RIJEN_190B.append((n, inzet, verlies + inzet, uit, round(uit - verlies - inzet, 2)))
    verlies += inzet
assert [r[1] for r in RIJEN_190B[:6]] == [10, 22, 46, 97, 205, 433]
assert RIJEN_190B[7][2] > RIJEN_200[7][2]   # na 8 rondes meer ingezet dan bij odds 2,00
assert all(r[4] >= 9 for r in RIJEN_190B)

# 4) kansen op verliesreeksen bij 49% winkans (q = 0,51) en roulette rood (q = 19/37)
Q_SPORT, Q_ROOD = 0.51, 19 / 37
REEKS = {k: (Q_SPORT ** k, [p_reeks(Q_SPORT, k, n) for n in (100, 250, 500, 1000)]) for k in (6, 8, 10)}
assert pct(REEKS[6][0]) == "1,8%" and pct(REEKS[8][0], 2) == "0,46%" and pct(REEKS[10][0], 2) == "0,12%"
assert pct(REEKS[8][1][2]) == "67,7%" and pct(REEKS[6][1][1]) == "89,5%" and pct(REEKS[10][1][3]) == "44,1%"

# 5) verwachte waarde per cyclus met maximaal k rondes (winst €10, of verlies van de hele reeks)
def ev(q, k):
    return (1 - q ** k) * BASIS - q ** k * BASIS * (2 ** k - 1)
assert eur(ev(Q_SPORT, 8)) == "−€1,72" and eur(ev(Q_ROOD, 8)) == "−€2,38" and eur(ev(Q_SPORT, 6)) == "−€1,26"
assert pct(18 / 37, 2) == "48,65%" and pct(1 / 37, 2) == "2,70%"

# 6) tafellimiet (fictief voorbeeld): minimum €1, maximum €500 -> laatste mogelijke inzet €256 (ronde 9)
RONDES_TAFEL = max(n for n in range(1, 20) if 2 ** (n - 1) <= 500)
assert RONDES_TAFEL == 9 and 2 ** RONDES_TAFEL - 1 == 511

# 7) bankroll per startinzet en aantal rondes
BANKROLL = [(b, [b * (2 ** k - 1) for k in (5, 6, 8, 10)]) for b in (1, 5, 10, 25)]
assert BANKROLL[2][1] == [310, 630, 2550, 10230]

# 8) Paroli (3 winsten) en D'Alembert
assert 10 + 20 + 40 == 70 and pct(0.49 ** 3) == "11,8%"
DALEM_REEKS = "VVWVWW"   # V = verlies, W = winst
dal, inzet, DAL_RIJEN = 0, BASIS, []
for i, u in enumerate(DALEM_REEKS, 1):
    res = inzet if u == "W" else -inzet
    dal += res
    DAL_RIJEN.append((i, eur(inzet), "winst" if u == "W" else "verlies", eur(res), eur(dal)))
    inzet = max(BASIS, inzet - BASIS) if u == "W" else inzet + BASIS
assert dal == 30


def r200(r):
    return (f"<strong>{r[0]}</strong>", eur(r[1]), eur(r[2]), eur(r[3]), f"+{eur(r[4])}")


def r190(r):
    return (f"<strong>{r[0]}</strong>", eur(r[1]), eur(r[2]), eur(r[3]),
            ("+" if r[4] > 0 else "") + eur(r[4]))


content = f"""<p><strong>Het martingale systeem is een wedstrategie waarbij je je inzet verdubbelt na elk verlies en na een winst terugkeert naar je startinzet. Het idee: de eerste winst maakt alle eerdere verliezen goed en levert precies je startinzet op. In de praktijk faalt het, omdat lange verliesreeksen vaker voorkomen dan je denkt, je inzet razendsnel oploopt en bookmakers en casino's een maximuminzet hanteren. Het verandert niets aan het voordeel van de bookmaker of het casino.</strong></p>
<p>Martingale is een van de oudste goksystemen en wordt zowel bij roulette als bij sportweddenschappen gebruikt. Het voelt logisch: je verliest toch niet eindeloos? Hieronder zie je met echte rekentabellen wat er gebeurt bij odds 2,00 en 1,90, hoe groot de kans op een verliesreeks is, hoeveel geld je nodig hebt en welke varianten er zijn, zoals de reverse martingale (Paroli) en D'Alembert.</p>
<h3><strong>Hoe werkt het martingale systeem?</strong></h3>
<p>Je kiest een weddenschap met ongeveer 50% kans en een quotering rond de 2,00. Denk aan rood of zwart bij roulette, of bij sport aan een markt als over/under of een handicap waar beide kanten ongeveer even kansrijk zijn. Daarna volg je vier vaste stappen:</p>
<ol><li><strong>Bepaal je startinzet,</strong> bijvoorbeeld €10.</li><li><strong>Verlies je, dan verdubbel je</strong> je volgende inzet: €20, daarna €40, €80 enzovoort.</li><li><strong>Win je, dan ben je je verliezen kwijt</strong> en sta je €10 in de plus.</li><li><strong>Na een winst begin je opnieuw</strong> met €10.</li></ol>
<p>Zo lang je uiteindelijk wint, eindig je elke reeks met één startinzet winst. Dat is het hele idee. Het probleem zit in dat woordje "uiteindelijk".</p>
<h3><strong>Rekenvoorbeeld: martingale bij odds 2,00</strong></h3>
<p>In deze tabel zie je per ronde je inzet, wat je in totaal hebt ingezet, wat je terugkrijgt als je in die ronde wint en wat je netto overhoudt. De quoteringen in dit voorbeeld en de rest van dit artikel zijn fictief.</p>
{tabel(["Ronde", "Inzet", "Totaal ingezet", "Uitbetaling bij winst", "Nettowinst"], [r200(r) for r in RIJEN_200])}
<p>Wat opvalt: je winst blijft altijd €10, maar je risico groeit exponentieel. Na zes verliezen op rij moet je {eur(RIJEN_200[6][1])} inzetten om {eur(BASIS)} te winnen. Na tien verliezen heb je al {eur(RIJEN_200[9][2])} ingezet en is je volgende inzet {eur(RIJEN_200[9][1] * 2)}. Je riskeert dus steeds meer voor dezelfde kleine beloning.</p>"""

content2 = f"""<h3><strong>Wat gebeurt er bij odds 1,90?</strong></h3>
<p>Bij sportweddenschappen kom je zelden een zuivere 2,00 tegen. Bij twee even kansrijke uitkomsten ligt de quotering vaak rond de 1,90, omdat de bookmaker zijn marge inbouwt. Verdubbel je dan gewoon, dan werkt de rekensom niet meer:</p>
{tabel(["Ronde", "Inzet", "Totaal ingezet", "Uitbetaling bij winst", "Netto resultaat"], [r190(r) for r in RIJEN_190])}
<p>Win je pas in ronde 5, dan sta je ondanks je winst {eur(-RIJEN_190[4][4])} in de min. Om toch elke reeks met winst af te sluiten, moet je bij odds 1,90 meer dan verdubbelen: je inzet is dan je totale verlies plus de gewenste winst, gedeeld door 0,90.</p>
{tabel(["Ronde", "Inzet", "Totaal ingezet", "Uitbetaling bij winst", "Netto resultaat"], [r190(r) for r in RIJEN_190B])}
<p>Na acht rondes heb je zo al {eur(RIJEN_190B[7][2])} ingezet, tegen {eur(RIJEN_200[7][2])} bij odds 2,00. Elke cent marge maakt het systeem duurder.</p>
<h3><strong>De roulette martingale strategie</strong></h3>
<p>Bij roulette is martingale het bekendst, meestal op rood of zwart. Dat lijkt een 50/50-gok, maar dat is het niet. Europese roulette heeft 37 vakken: 18 rood, 18 zwart en de groene nul. Je kans op rood is dus {pct(18 / 37, 2)} en het huisvoordeel is {pct(1 / 37, 2)}. Bij Amerikaanse roulette met een extra dubbele nul zakt je winkans naar 47,37%. Speel je toch roulette, kies dan liever een Europese tafel of Franse roulette met de La Partage-regel, die bij een nul de helft van je inzet teruggeeft.</p>
<p>Daarnaast heeft elke tafel een minimum- en maximuminzet. Stel dat een tafel loopt van €1 tot €500. Begin je met €1, dan is €256 je laatste toegestane inzet: dat is ronde {RONDES_TAFEL}. Verlies je die ook, dan ben je {eur(2 ** RONDES_TAFEL - 1)} kwijt en kun je niet verder verdubbelen. Het tafelmaximum is precies bedoeld om systemen als dit te stoppen.</p>
<h3><strong>Waarom werkt het martingale systeem niet?</strong></h3>
<p><strong>1. Verliesreeksen komen vaker voor dan je denkt</strong></p>
<p>De kans om zes keer achter elkaar te verliezen lijkt klein. Maar je speelt niet één reeks, je speelt er honderden. Bij een winkans van 49% per weddenschap is dit de kans dat je minstens één keer zo'n reeks meemaakt:</p>
{tabel(["Verliezen op rij", "Kans per reeks", "In 100 bets", "In 250 bets", "In 500 bets", "In 1.000 bets"],
       [(f"<strong>{k}</strong>", pct(v[0], 2), *[pct(x) for x in v[1]]) for k, v in REEKS.items()])}
<p>Wie 250 keer inzet, heeft dus {pct(REEKS[6][1][1])} kans dat er minstens één reeks van zes verliezen tussen zit. Met €10 als startinzet kost die ene reeks je {eur(RIJEN_200[5][2])}, terwijl elke gewonnen reeks maar €10 oplevert.</p>
<p><strong>2. Het voordeel van de bookmaker blijft bestaan</strong></p>
<p>Een inzetsysteem verandert de kans op de uitkomst niet. Stop je na maximaal acht rondes, dan is je verwachte resultaat per reeks bij 49% winkans {eur(ev(Q_SPORT, 8))} en bij rood op roulette {eur(ev(Q_ROOD, 8))}. Je wint vaak een beetje en verliest af en toe heel veel. Op lange termijn is het saldo negatief.</p>
<p><strong>3. Maximuminzetten en limieten</strong></p>
<p>Bookmakers en casino's hebben een maximuminzet per weddenschap of per tafel. Daarnaast passen bookmakers soms de limieten van een account aan. Je loopt dus op een muur voordat je verlies is terugverdiend.</p>
<p><strong>4. Je wint klein en verliest groot</strong></p>
<p>Psychologisch is martingale verraderlijk. Wekenlang kleine winsten geven het gevoel dat het systeem werkt, tot één slechte avond alles wegvaagt. Dat patroon is precies wat verliezen najagen zo gevaarlijk maakt.</p>"""

content3 = f"""<h3><strong>Hoeveel bankroll heb je nodig voor martingale?</strong></h3>
<p>Je bankroll moet de hele reeks kunnen dragen. De formule is simpel: startinzet × (2<sup>aantal rondes</sup> − 1).</p>
{tabel(["Startinzet", "5 rondes", "6 rondes", "8 rondes", "10 rondes"],
       [(f"<strong>{eur(b)}</strong>", *[eur(x) for x in v]) for b, v in BANKROLL])}
<p>Ter vergelijking: bij legale online aanbieders in Nederland geldt een netto stortingslimiet van €300 per maand tot je 24e en €700 per maand daarna. Met een startinzet van €10 kun je met €700 dus nog geen zeven verliezen op rij opvangen ({eur(BASIS * (2 ** 7 - 1))} nodig). Dat is geen fout van de regels: het laat zien hoe snel martingale uit de hand loopt. Lees meer over <a href="/speel-bewust/verantwoord-wedden">verantwoord wedden</a>.</p>
<h3><strong>Reverse martingale (Paroli) en D'Alembert</strong></h3>
<p><strong>Reverse martingale of Paroli</strong></p>
<p>Bij de reverse martingale draai je het om: je verdubbelt na een <em>winst</em> en gaat na een verlies terug naar je startinzet. Meestal stop je na drie winsten op rij. Met €10 bij odds 2,00 zet je €10, €20 en €40 in. Win je drie keer, dan sta je €70 in de plus. Verlies je ergens onderweg, dan ben je alleen je startinzet van €10 kwijt. Bij 49% winkans haal je drie winsten op rij in {pct(0.49 ** 3)} van de gevallen. Je risico per reeks is klein, maar ook hier blijft het huisvoordeel staan.</p>
<p><strong>D'Alembert</strong></p>
<p>Bij D'Alembert verhoog je je inzet met één eenheid na een verlies en verlaag je hem met één eenheid na een winst. De stappen zijn veel kleiner dan bij martingale. Een voorbeeld met eenheden van €10 bij odds 2,00:</p>
{tabel(["Bet", "Inzet", "Uitkomst", "Resultaat", "Saldo"], DAL_RIJEN)}
<p>Met drie winsten en drie verliezen sta je hier {eur(dal)} in de plus. Tegelijk kan een lange verliesreeks ook hier je inzet flink laten oplopen, en de verwachte waarde blijft negatief.</p>
{tabel(["Systeem", "Na verlies", "Na winst", "Risico"], [
    ("<strong>Martingale</strong>", "Inzet verdubbelen", "Terug naar start", "Zeer hoog: inzet groeit exponentieel"),
    ("<strong>Reverse martingale</strong>", "Terug naar start", "Inzet verdubbelen", "Laag per reeks, winst zeldzaam"),
    ("<strong>D'Alembert</strong>", "+1 eenheid", "−1 eenheid", "Gemiddeld: inzet groeit lineair"),
    ("<strong>Fibonacci</strong>", "Volgend getal in de reeks", "Twee stappen terug", "Hoog bij lange reeksen"),
])}
<p>Meer over de Fibonacci-methode lees je in onze uitleg over <a href="/nieuws/wedden-op-gelijkspel-de-fibonacci-wedstrategie-onder-de-loep">de Fibonacci wedstrategie</a>. Alle systemen naast elkaar vind je in het overzicht van <a href="/nieuws/alle-verschillende-wedstrategieen-op-een-rijtje">alle wedstrategieën</a>.</p>
<h3><strong>Wil je het toch proberen? Houd je hieraan</strong></h3>
<ul><li><strong>Leg vooraf een maximum aantal rondes vast,</strong> bijvoorbeeld vijf, en accepteer het verlies als die reeks misgaat.</li><li><strong>Gebruik alleen geld dat je kunt missen.</strong> Zie het als de prijs van je speelplezier, niet als investering.</li><li><strong>Zoek de hoogste quotering.</strong> Het verschil tussen 1,90 en 1,95 scheelt in elke ronde. Gebruik onze <a href="/odds-vergelijken-bij-alle-bookmakers-beste-odds-vandaag">odds vergelijker</a>.</li><li><strong>Stop na een verliesreeks.</strong> Begin niet direct een nieuwe reeks om het verlies terug te halen.</li><li><strong>Houd je resultaten bij.</strong> Zo zie je eerlijk wat het systeem je kost.</li></ul>
<p>Wil je kansen beter inschatten in plaats van inzetten te verhogen? Bekijk dan <a href="/nieuws/wat-is-de-wedstrategie-value-betting">value betting</a>, de enige aanpak die op de kans zelf mikt.</p>
<h3><strong>Mag je het martingale systeem gebruiken in Nederland?</strong></h3>
<p>Ja. Een inzetsysteem is geen verboden weddenschap, dus je mag martingale toepassen bij elke legale aanbieder. Speel alleen bij bookmakers en casino's met een vergunning van de Kansspelautoriteit. Spelen bij een site zonder Nederlandse vergunning is illegaal, en je hebt daar geen bescherming zoals de netto stortingslimiet of Cruks. Twijfel je? Lees <a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>.</p>
<p>Legale bookmakers die wij aanraden:</p>
{aanraders()}
<h3><strong>Veelgestelde vragen over het martingale systeem</strong></h3>
<p><strong>Wat is het martingale systeem in het kort?</strong><br>Een inzetsysteem waarbij je na elk verlies je inzet verdubbelt en na een winst opnieuw begint. Elke gewonnen reeks levert je startinzet op, een verloren reeks kost je alles wat je in die reeks hebt ingezet.</p>
<p><strong>Werkt de martingale strategie echt?</strong><br>Op korte termijn lijkt het vaak te werken, omdat je meestal kleine winsten boekt. Op lange termijn niet: één lange verliesreeks kost meer dan alle kleine winsten samen, en het voordeel van de aanbieder blijft bestaan.</p>
<p><strong>Werkt martingale bij roulette?</strong><br>Nee. Door de nul is je kans op rood of zwart {pct(18 / 37, 2)} en houdt het casino {pct(1 / 37, 2)} voordeel. Daarnaast stopt het tafelmaximum je na een aantal verdubbelingen.</p>
<p><strong>Welke odds heb je nodig voor martingale?</strong><br>Het systeem gaat uit van odds 2,00. Bij lagere odds, zoals 1,90, moet je meer dan verdubbelen om je verlies terug te winnen. Dat maakt het nog riskanter.</p>
<p><strong>Hoeveel geld heb je nodig voor martingale?</strong><br>Startinzet × (2<sup>rondes</sup> − 1). Wil je met €10 tien verliezen kunnen opvangen, dan heb je {eur(RIJEN_200[9][2])} nodig voor die ene reeks.</p>
<p><strong>Wat is het verschil met de reverse martingale?</strong><br>Bij de reverse martingale (Paroli) verdubbel je na een winst in plaats van na een verlies. Je verliest per reeks maximaal je startinzet, maar grote winsten zijn zeldzaam.</p>
<p><strong>Kan een bookmaker je blokkeren voor martingale?</strong><br>Martingale zelf is niet verboden. Wel hebben bookmakers maximuminzetten en kunnen ze de limieten van een account aanpassen volgens hun voorwaarden.</p>
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
