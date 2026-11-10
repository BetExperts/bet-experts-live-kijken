# -*- coding: utf-8 -*-
"""Los artikel (cluster Grand Slam of Darts, evergreen): alle winnaars sinds 2007.
Zoekwoorden: grand slam of darts winnaars, finale grand slam of darts 2025, grand slam of darts van gerwen, recordwinnaar.
Feiten: gsod_data.WINNAARS (Wikipedia 'Grand Slam of Darts', gecontroleerd in gsod_feiten_2026.md), finale 2025 met
gemiddelden 100,61-99,56 en halve finales (Wikipedia 2025). Na 22-11-2026: winnaar 2026 toevoegen.
  python3 specials/gsod_winnaars.py   (dry run)"""
import os, sys
from collections import Counter
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel
import gsod_data as G

SLUG = G.SLUGS["winnaars"]
RUBRIEK = G.RUBRIEK
TITEL = "Winnaars Grand Slam of Darts: alle kampioenen sinds 2007"
SAMENVATTING = ("Alle winnaars van de Grand Slam of Darts sinds 2007, met finale-uitslagen. Phil Taylor won zes keer, "
                "Van Gerwen drie keer, Littler won in 2024 en 2025.")

TELLING = Counter(w for _, w, _, _ in G.WINNAARS)
assert TELLING["Phil Taylor"] == 6 and TELLING["Michael van Gerwen"] == 3 and TELLING["Gerwyn Price"] == 3 and TELLING["Luke Littler"] == 2

OG_EYEBROW = "Darts · erelijst sinds 2007"
OG_KOP = "Winnaars<br><em>Grand Slam of Darts</em>"
OG_TEGELS = [("Recordwinnaar", "Taylor 6×"), ("Titelhouder", "Littler")]
OG_KOPJE = "Meeste titels"
OG_RECHTS = "Finales 2007-2025"
OG_RIJEN = [("6 titels", "Phil Taylor", "2007-2014"),
            ("3 titels", "Michael van Gerwen", "2015-2017"),
            ("3 titels", "Gerwyn Price", "2018-2021"),
            ("2 titels", "Luke Littler", "2024 + 2025")]

content = f"""<p><strong>Phil Taylor is met zes titels de recordwinnaar van de Grand Slam of Darts. Michael van Gerwen en Gerwyn Price wonnen het toernooi elk drie keer, Luke Littler twee keer: in 2024 en 2025. Littler is titelverdediger en kan in november 2026 als derde speler ooit drie keer op rij winnen. Hieronder vind je alle winnaars en finales sinds de eerste editie in 2007.</strong></p>
<h3><strong>Alle winnaars van de Grand Slam of Darts</strong></h3>
{tabel(["Jaar", "Winnaar", "Uitslag", "Runner-up"], [
    (f"<strong>{j}</strong>", f"<strong>{w}</strong>", s, r) for j, w, s, r in reversed(G.WINNAARS)
])}
<p><em>De eerste twee finales (2007 en 2008) werden over best of 35 legs gespeeld, vanaf 2009 over best of 31 legs.</em></p>"""

content2 = f"""<h3><strong>Wie won de Grand Slam of Darts het vaakst?</strong></h3>
{tabel(["Speler", "Titels", "Jaren", "Verloren finales"], [
    ("<strong>Phil Taylor</strong>", "6", "2007, 2008, 2009, 2011, 2013, 2014", "1 (2015)"),
    ("<strong>Michael van Gerwen</strong>", "3", "2015, 2016, 2017", "1 (2012)"),
    ("<strong>Gerwyn Price</strong>", "3", "2018, 2019, 2021", "–"),
    ("<strong>Luke Littler</strong>", "2", "2024, 2025", "–"),
    ("Scott Waites", "1", "2010", "1 (2009)"),
    ("Raymond van Barneveld", "1", "2012", "–"),
    ("José de Sousa", "1", "2020", "–"),
    ("Michael Smith", "1", "2022", "–"),
    ("Luke Humphries", "1", "2023", "1 (2025)"),
])}
<p>Peter Wright en James Wade verloren allebei drie finales zonder het toernooi ooit te winnen. Gary Anderson stond twee keer in de finale (2011 en 2018) en verloor ook twee keer.</p>
<h3><strong>Nederlandse winnaars van de Grand Slam of Darts</strong></h3>
<p>Twee Nederlanders wonnen de Grand Slam. <strong>Raymond van Barneveld</strong> was in 2012 de eerste: hij won een volledig Nederlandse finale met 16-14 van Michael van Gerwen. <strong>Michael van Gerwen</strong> nam daarna revanche met drie titels op rij: in 2015 versloeg hij Phil Taylor (16-13), in 2016 James Wade (16-8) en in 2017 Peter Wright (16-12). Vorig jaar was Danny Noppert de beste Nederlander: hij haalde de halve finale, waarin hij met 9-16 verloor van Luke Littler.</p>
<h3><strong>De finale van 2025: Littler prolongeert</strong></h3>
<p>Op zondag 16 november 2025 won Luke Littler de Grand Slam voor de tweede keer op rij. In de finale versloeg hij Luke Humphries met 16-11, met een gemiddelde van 100,61 tegen 99,56 voor Humphries. In de halve finales had Littler met 16-9 gewonnen van Danny Noppert en Humphries met 16-13 van Gerwyn Price. Een jaar eerder won Littler zijn eerste Grand Slam met een van de meest eenzijdige finales uit de geschiedenis: 16-3 tegen Martin Lukeman.</p>"""

content3 = f"""<h3><strong>Opvallende feiten uit de geschiedenis</strong></h3>
<p><strong>Drie keer op rij.</strong> Alleen Phil Taylor (2007-2009) en Michael van Gerwen (2015-2017) wonnen de Grand Slam drie keer achter elkaar. Luke Littler kan zich in 2026 bij dat rijtje voegen.</p>
<p><strong>Van BDO naar PDC.</strong> De Grand Slam werd in 2007 opgezet om spelers van de PDC en de toenmalige BDO tegen elkaar te laten spelen. Scott Waites werd in 2010 de enige winnaar die via het BDO-circuit was geplaatst.</p>
<p><strong>Coventry.</strong> Bijna alle edities werden in Wolverhampton gespeeld: tot en met 2017 in de Civic Hall, sinds 2018 in Aldersley Leisure Village. Alleen in 2020 week het toernooi vanwege corona uit naar Coventry, zonder publiek. Winnaar werd de Portugees José de Sousa.</p>
<h3><strong>Grand Slam of Darts 2026</strong></h3>
<p>De 20e editie wordt van 14 tot en met 22 november 2026 gespeeld, met voor het eerst 48 spelers en £1 miljoen prijzengeld. Bekijk het {G.a('speelschema', 'speelschema van de Grand Slam of Darts 2026')}, de {G.a('deelnemers', 'deelnemers en poules')}, het {G.a('prijzengeld', 'prijzengeld')} en het {G.a('format', 'nieuwe format')}. Waar je kunt kijken, lees je in ons artikel over {G.a('tv', 'de Grand Slam of Darts live op tv')}. Meer darts-records vind je bij de {G.EXTRA['wkstats']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wie won de Grand Slam of Darts 2025?</strong><br>Luke Littler. Hij won de finale op 16 november 2025 met 16-11 van Luke Humphries.</p>
<p><strong>Wie heeft de Grand Slam of Darts het vaakst gewonnen?</strong><br>Phil Taylor, met zes titels (2007, 2008, 2009, 2011, 2013 en 2014).</p>
<p><strong>Hoe vaak won Michael van Gerwen de Grand Slam of Darts?</strong><br>Drie keer, in 2015, 2016 en 2017. In 2012 verloor hij de finale van Raymond van Barneveld.</p>
<p><strong>Welke Nederlanders wonnen de Grand Slam of Darts?</strong><br>Raymond van Barneveld (2012) en Michael van Gerwen (2015, 2016 en 2017).</p>
{G.SLOT}"""

if __name__ == "__main__":
    alles = G.check(sys.modules[__name__], 750)
    print("dry run ok – niets gepubliceerd")
