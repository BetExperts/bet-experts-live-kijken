# -*- coding: utf-8 -*-
"""Los artikel (cluster Grand Slam of Darts 2026): prijzengeld per ronde, 2026 tegenover 2025.
Zoekwoorden: prijzengeld grand slam of darts 2026, grand slam of darts prijzengeld, prijzengeld winnaar, prize money.
Feiten: gsod_data.PRIJZEN (PDC Europe 31-03-2025 + Wikipedia 2026/2025 + DartsKing; telt op tot £1.000.000).
Bijgewerkt 10-11-2026 na de loting (gsod_data.GROEPEN): rekenvoorbeelden per Nederlander; format nu bevestigd door de PDC.
Euro-bedragen: alleen indicatief (koers ±€1,15 per pond, niet als vast feit genoemd).
  python3 specials/gsod_prijzengeld_2026.py   (dry run)"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel
import gsod_data as G

SLUG = G.SLUGS["prijzengeld"]
RUBRIEK = G.RUBRIEK
TITEL = "Prijzengeld Grand Slam of Darts 2026: £200.000 voor winnaar"
SAMENVATTING = ("Prijzengeld Grand Slam of Darts 2026: £1 miljoen, £200.000 voor de winnaar. "
                "Alle bedragen per ronde, 2025 ter vergelijking en wat de Nederlanders verdienen.")

OG_EYEBROW = "Darts · prijzengeld 2026"
OG_KOP = "Prijzengeld<br><em>Grand Slam 2026</em>"
OG_TEGELS = [("Winnaar", "£200.000"), ("Totaal", "£1 mln")]
OG_KOPJE = "Per speler, met 2025 ter vergelijking"
OG_RECHTS = "+54% ten opzichte van 2025"
OG_RIJEN = [("Finale", "Runner-up · 2025: £70.000", "£100.000"),
            ("Halve finale", "Twee verliezers · 2025: £50.000", "£60.000"),
            ("Kwartfinale", "Vier verliezers · 2025: £25.000", "£35.000"),
            ("Laatste 16", "Acht verliezers · 2025: £12.250", "£20.000")]


# (speler, groep, mogelijke tegenstander in de laatste 16) — loting 9 november (gsod_data.GROEPEN)
NL_PAD = [
    ("Gian van Veen", "M", "Winnaar groep N (Dobey, Schindler, Schmidt)"),
    ("Michael van Gerwen", "L", "Winnaar groep K (Wade, Evans, Crabtree)"),
    ("Wessel Nijman", "H", "Winnaar groep G (Clayton, Cross, Östlund)"),
    ("Jermaine Wattimena", "B", "Winnaar groep A (Littler, Zonneveld, Greaves)"),
    ("Niels Zonneveld", "A", "Winnaar groep B (Wattimena, Soutar, Ashton)"),
    ("Kevin Doets", "C", "Winnaar groep D (Bunting, Menzies, R. Smith)"),
    ("Maik Kuivenhoven", "P", "Winnaar groep O (Ross Smith, Clemens, Rodriguez)"),
]


def r25(x):
    return G.pond(x) if x else "–"


content = f"""<p><strong>Het prijzengeld van de Grand Slam of Darts 2026 stijgt naar £1.000.000, £350.000 meer dan vorig jaar. De winnaar krijgt £200.000 (2025: £150.000), de verliezend finalist £100.000. Doordat het veld groeit naar 48 spelers, verdient iedere deelnemer minimaal £5.000. Nu de loting bekend is, rekenen we ook uit wat de zeven Nederlanders kunnen verdienen. Bijgewerkt op dinsdag 10 november.</strong></p>
<h3><strong>Prijzengeld Grand Slam of Darts 2026 per ronde</strong></h3>
{tabel(["Ronde", "Spelers", "Per speler 2026", "Per speler 2025"], [
    (f"<strong>{p}</strong>", str(n), G.pond(b), r25(o)) for p, n, b, o in G.PRIJZEN
] + [("<strong>Totaal</strong>", "48", f"<strong>{G.pond(G.TOTAAL_2026)}</strong>", G.pond(G.TOTAAL_2025))])}
<p><em>In 2025 was er geen 'nummer 2 in de groep' als aparte plek: met groepen van vier gingen toen de nummers 1 en 2 door, en kreeg een nummer 4 £5.000. Groepswinnaars kregen in 2025 bovendien een bonus van £3.500. Euro-bedragen hangen af van de wisselkoers; met een pond rond de €1,15 is de hoofdprijs zo'n €230.000 waard.</em></p>"""

content2 = f"""<h3><strong>Wat verdient de winnaar van de Grand Slam of Darts?</strong></h3>
<p>De winnaar van de Grand Slam of Darts 2026 krijgt £200.000 en de Eric Bristow Trophy. Dat is £50.000 meer dan Luke Littler vorig jaar verdiende met zijn 16-11 zege op Luke Humphries. Omdat het prijzengeld meetelt voor de PDC Order of Merit, kan een goede week in Wolverhampton een speler ook flink op de ranking laten stijgen.</p>
<h3><strong>Waar gaat de extra £350.000 heen?</strong></h3>
<p>Het grootste deel van de verhoging zit onderin het toernooi, en dat komt door het nieuwe format. Er doen 16 spelers meer mee, en ook wie in de groep strandt, verdient meer dan vroeger:</p>
{tabel(["", "2025", "2026"], [
    ("<strong>Uitgeschakeld in de groep</strong>", "£5.000 of £8.000 (nummer 4 of 3 van 8 groepen)", "£5.000 of £12.500 (nummer 3 of 2 van 16 groepen)"),
    ("<strong>Samen voor wie in de groep strandt</strong>", "£104.000 (16 spelers)", "£280.000 (32 spelers)"),
    ("<strong>Samen vanaf de laatste 16</strong>", "£518.000, plus £28.000 aan bonussen voor groepswinnaars", "£720.000"),
])}
<p>De sprong is het grootst in de laatste 16: wie in die ronde verliest, krijgt £20.000 in plaats van £12.250. Een kwartfinale levert £35.000 op (was £25.000), een halve finale £60.000 (was £50.000).</p>
<h3><strong>Wat betekent het nieuwe format voor het prijzengeld?</strong></h3>
<p>De PDC heeft bevestigd dat alleen de groepswinnaar doorgaat naar de knock-outfase. Het verschil tussen de eerste en de tweede plek in een groep is daardoor groot: de nummer 2 gaat met £12.500 naar huis, terwijl de groepswinnaar minimaal £20.000 zeker heeft en nog kans maakt op £200.000. Hoe de groepen en de rondes precies werken, lees je in ons artikel over het {G.a('format', 'format van de Grand Slam of Darts 2026')}.</p>"""

content3 = f"""<h3><strong>Wat kunnen de Nederlanders verdienen?</strong></h3>
<p>Het prijzengeld wordt niet opgeteld per ronde: een speler krijgt het bedrag dat hoort bij de ronde waarin hij uitgeschakeld wordt. Wie zijn groep wint en in de kwartfinale verliest, gaat dus naar huis met £35.000, niet met £20.000 plus £35.000. Zo ziet de rekensom eruit voor elke Nederlander:</p>
{tabel(["Uitgeschakeld in", "Prijzengeld", "Wat moet een Nederlander daarvoor doen?"], [
    ("<strong>Groep, als nummer 3</strong>", G.pond(5000), "Beide groepsduels verliezen"),
    ("<strong>Groep, als nummer 2</strong>", G.pond(12500), "Eén groepsduel winnen, maar niet de groep"),
    ("<strong>Laatste 16</strong>", G.pond(20000), "Groepswinst, daarna verlies op 18 of 19 november"),
    ("<strong>Kwartfinale</strong>", G.pond(35000), "Eén knock-outzege, verlies op 20 of 21 november"),
    ("<strong>Halve finale</strong>", G.pond(60000), "Twee knock-outzeges, verlies op zondagmiddag 22 november"),
    ("<strong>Finale verloren</strong>", G.pond(100000), "Drie knock-outzeges"),
    ("<strong>Winnaar</strong>", G.pond(200000), "Alle vijf de wedstrijden winnen"),
])}
{tabel(["Speler", "Groep", "Zeker", "Bij groepswinst", "Tegenstander laatste 16"], [
    ("<strong>" + s + "</strong>", g, G.pond(5000), "minimaal " + G.pond(20000), t) for s, g, t in NL_PAD
])}
<p>Samen hebben de zeven Nederlanders minimaal {G.pond(7 * 5000)} zeker. Ze zitten alle zeven in een andere groep, dus in theorie kunnen ze allemaal doorgaan; dan is er minstens {G.pond(7 * 20000)} binnen. Alleen Zonneveld en Wattimena kunnen elkaar in de laatste 16 treffen, want de winnaars van groep A en B spelen tegen elkaar. Ter vergelijking: Danny Noppert was vorig jaar met zijn halve finale de best verdienende Nederlander, goed voor £50.000. Wie er in welke groep zit, lees je in ons artikel over de {G.a('deelnemers', 'loting en poules van de Grand Slam of Darts 2026')}.</p>
<h3><strong>Prijzengeld door de jaren heen</strong></h3>
<p>Het prijzengeld van de Grand Slam is de laatste jaren hard gestegen. In 2025 ging het nog om £650.000 in totaal, met £150.000 voor de winnaar. In 2026 gaat er voor het eerst £1 miljoen om in Wolverhampton. Ter vergelijking: op de {G.EXTRA['wgp']} lees je wat er in Leicester te verdienen viel.</p>
<h3><strong>Meer over de Grand Slam of Darts 2026</strong></h3>
<p>Het toernooi wordt van 14 tot en met 22 november gespeeld in Wolverhampton. Alle dagen en tijden vind je in het {G.a('speelschema', 'speelschema van de Grand Slam of Darts 2026')}, de groepen in {G.a('deelnemers', 'de loting en poules')} en waar je kunt kijken in ons artikel over {G.a('tv', 'de Grand Slam of Darts live op tv')}.</p>
<p>Wedden op de Grand Slam? Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit en lees bij twijfel {G.EXTRA['legaal']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoeveel prijzengeld is er op de Grand Slam of Darts 2026?</strong><br>£1.000.000 in totaal, £350.000 meer dan in 2025.</p>
<p><strong>Wat verdient de winnaar van de Grand Slam of Darts 2026?</strong><br>£200.000, tegen £150.000 vorig jaar. De verliezend finalist krijgt £100.000.</p>
<p><strong>Wat krijgt een speler die in de groep uitgeschakeld wordt?</strong><br>De nummer 3 van een groep krijgt £5.000, de nummer 2 £12.500. Alleen de groepswinnaar gaat door.</p>
<p><strong>Hoeveel prijzengeld hebben de Nederlanders zeker?</strong><br>Elke deelnemer krijgt minimaal £5.000, dus de zeven Nederlanders samen minimaal £35.000. Wie zijn groep wint, heeft £20.000 zeker.</p>
<p><strong>Wie won vorig jaar het meeste prijzengeld op de Grand Slam?</strong><br>Luke Littler, die de finale met 16-11 won van Luke Humphries en £150.000 verdiende.</p>
{G.SLOT}"""

if __name__ == "__main__":
    # narekening van de tabel 'Waar gaat de extra £350.000 heen?'
    assert 8 * 8000 + 8 * 5000 == 104000 and 104000 + 518000 + 8 * 3500 == 650000
    assert 16 * 12500 + 16 * 5000 == 280000 and 200000 + 100000 + 120000 + 140000 + 160000 == 720000
    assert 150000 + 70000 + 100000 + 100000 + 8 * 12250 == 518000
    assert len(NL_PAD) == len(G.NL) == 7 and {s for s, _, _ in NL_PAD} == G.NL
    assert all(G.groep_van(s) == g for s, g, _ in NL_PAD)
    # tegenstander laatste 16: A-B, C-D, ..., O-P
    paar = {a: b for x in ("AB", "CD", "EF", "GH", "IJ", "KL", "MN", "OP") for a, b in (x, x[::-1])}
    assert all(t.startswith(f"Winnaar groep {paar[g]} ") for _, g, t in NL_PAD)
    alles = G.check(sys.modules[__name__], 900)
    assert "{" not in alles and "}" not in alles
    assert "10 november" in content and "£35.000" in content3 and "£140.000" in content3
    print("dry run ok – niets gepubliceerd")
