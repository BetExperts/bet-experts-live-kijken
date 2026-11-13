# -*- coding: utf-8 -*-
"""Artikel 3/3 Suriname – Eswatini: voorspelling, selectie, debutanten, wie is Eswatini, historie.
Feiten: suriname_eswatini_2026_feiten.md §1, §4, §5, §6, §7 (+ litouwen_suriname_2026_feiten.md).
Odds 13-11 nog niet online (Circus, Kambi) -> geen odds, wel 'volgen'. Weggelaten: doelpuntenmakers Almere 2024 (bronnen
tegenstrijdig), reden afwezigheid Garden/Berger/Becker/Kerk/Paal/Sh. Pinas in Kaunas, schorsing Gamedze (onzeker).
  python3 specials/suriname_eswatini_voorspelling.py  (dry run)"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, "..")); sys.path.insert(0, HIER)
from legaal_data import tabel
from suriname_eswatini_2026_data import RUBRIEK, KSA, SLUGS, L

SLUG = SLUGS["voorspelling"]
TITEL = "Suriname – Eswatini voorspelling: selectie en historie"
SAMENVATTING = ("Suriname – Eswatini voorspelling: wie is Eswatini, welke debutanten zitten bij Natio en hoe vaak speelde "
                "Suriname in Nederland? Alles op een rij.")
OG_EB, OG_KOP = "Oefeninterland · voorbeschouwing", "Suriname – Eswatini <em>voorspelling</em>"
OG_RIJEN = [("FIFA-ranking", "128 – 164"), ("Onderling", "Eerste duel ooit"), ("Laatste duel", "Litouwen – Suriname 0-0"),
            ("Onze voorspelling", "Suriname wint 2-0")]

DEBUTANTEN = [("Cheveyo Balentien", "AC Milan", "19 jaar, aanvaller"),
              ("Neville Ogidi Nwankwo", "FC Utrecht", "verdediger"),
              ("Sanjeev van Haren", "NEC", "18 jaar, doelman"),
              ("Jaden Pinas", "FC Dordrecht", "aanvoerder van Dordrecht"),
              ("David Garden", "Excelsior", "aanvaller"),
              ("Yannick Boerleider", "Torino", "16 jaar, doelman")]

content = f"""<p><strong>Suriname is zondag de favoriet tegen Eswatini. Natio staat 128e op de wereldranglijst, Eswatini 164e. Eswatini, tot 2018 Swaziland, won geen enkele van zijn tien WK-kwalificatieduels en speelde donderdag met tien man 1-1 op Malta. Wij voorspellen een 2-0-zege voor Suriname. De oefeninterland begint zondag 15 november om 18:00 uur in De Vliert in Den Bosch; het is de eerste ontmoeting ooit tussen beide landen.</strong></p>
<p>Voor bondscoach Henk Fraser is het een wedstrijd om nieuwe spelers te bekijken. Donderdag speelde {L['suriname']} in Kaunas met 0-0 gelijk tegen Litouwen. Daar debuteerde doelman Jahnilo Wiegel-Triebel (KVC Westerlo), die de nul hield. De beste Surinaamse kans was voor Joël Piroe, wiens schot in de 71e minuut werd gekeerd. Vijf nieuwkomers zaten op de bank zonder te spelen; zij maken zondag waarschijnlijk hun debuut.</p>
<h3><strong>Wie zijn de debutanten bij Suriname?</strong></h3>
{tabel(["Speler", "Club", "Bijzonderheid"], DEBUTANTEN)}
<p>De meest besproken naam is Cheveyo Balentien, de 19-jarige aanvaller van AC Milan. Feyenoord-doelman Mannou Berger werd eerder ook genoemd als nieuwkomer, maar stond in Kaunas niet in de wedstrijdselectie. Vaste doelman Etienne Vaessen ontbreekt door een schorsing van vier duels na het duel in Guatemala, en Warner Hahn is geblesseerd.</p>
<h3><strong>De rest van de selectie</strong></h3>
<p>Naast de nieuwkomers zitten er veel bekende namen bij Natio, onder wie spelers van Nederlandse clubs: Navajo Bakboord en Liam van Gelderen (RKC), Djevencio van der Kust (Heracles), Shiloh 't Zand (Fortuna Sittard) en Richonell Margaret (Go Ahead Eagles). Verder Joël Piroe (West Ham, gehuurd van Leeds), Immanuel Pherai (Hamburger SV), Justin Lonwijk (Dynamo Kyiv), Ridgeciano Haps, Myenty Abena, Jaden Montnor, Denilho Cleonise en Jayden Turfkruier. In Kaunas begon Suriname met: Wiegel-Triebel; Bakboord, Abena, Van Gelderen, Haps; Klas, Pherai, Jubitana; Cleonise, Montnor en Piroe.</p>"""

content2 = f"""<h3><strong>Wie is Eswatini?</strong></h3>
<p>Eswatini is een klein koninkrijk in zuidelijk Afrika, tussen Zuid-Afrika en Mozambique. Tot april 2018 heette het land Swaziland. Het nationale elftal heet Sihlangu Semnikati, "het schild van de koning", en staat 164e op de FIFA-ranglijst. Eswatini plaatste zich nog nooit voor de Afrika Cup of het WK; het beste resultaat is een derde plek op de COSAFA Cup, het toernooi voor zuidelijk Afrika (2016 en 2021).</p>
{tabel(["", "Eswatini"], [
    ("Bijnaam", "Sihlangu Semnikati (het schild van de koning)"),
    ("FIFA-ranking", "164e"),
    ("Bondscoach", "Dominic Kunene (interim)"),
    ("WK-kwalificatie 2026", "Laatste in de groep: 0 zeges, 3 gelijk, 7 verloren"),
    ("Afrika Cup-kwalificatie 2027", "In de voorronde uitgeschakeld door Eritrea"),
    ("Laatste wedstrijd", "Malta – Eswatini 1-1 (12 november)"),
])}
<p>Eswatini maakt deze maand zijn eerste Europese tournee ooit. Op Malta speelde de ploeg ruim een uur met tien man, nadat Gift Gamedze in de 29e minuut rood kreeg, en toch werd het 1-1: aanvoerder Philani Mkhontfo scoorde vlak voor rust. De selectie bestaat vooral uit spelers uit de eigen competitie en uit Zimbabwe. De bekendste naam is Justice Figareido van Chippa United uit Zuid-Afrika. Interim-bondscoach Kunene was eerder al bondscoach van 2020 tot 2024 en voerde voor deze tournee elf wijzigingen door.</p>
<h3><strong>Onze voorspelling: Suriname – Eswatini 2-0</strong></h3>
<p>Suriname is op papier duidelijk sterker. Het verschil op de wereldranglijst is 36 plaatsen, en de Surinaamse selectie speelt grotendeels in Europa, terwijl Eswatini vooral spelers uit Afrikaanse competities heeft. Eswatini verdedigt wel taai: met tien man hield het Malta op 1-1. En Suriname scoorde in Litouwen niet, ondanks een paar goede kansen. Met het publiek achter zich en een aanval met Piroe, Montnor en mogelijk debutant Balentien verwachten wij dat Natio zondag wel scoort. Onze voorspelling: <strong>Suriname wint met 2-0</strong>.</p>
<p>Odds voor deze wedstrijd stonden op vrijdag 13 november nog niet online bij de bookmakers die we controleerden. Speel je erop, doe dat dan alleen bij een bookmaker met een vergunning van de Kansspelautoriteit; lees {L['legaal']}.</p>"""

content3 = f"""<h3><strong>Suriname in Nederland: een korte historie</strong></h3>
<p>Natio speelt maar zelden in Nederland. De vorige keer was op 24 maart 2024: in het Yanmar Stadion in Almere speelde Suriname, toen nog onder Stanley Menzo, met 1-1 gelijk tegen Martinique. Het duel was volgens berichten uitverkocht, en de NOS kopte dat het Surinaams elftal Almere "op tropisch oord" liet lijken.</p>
<p>Sindsdien maakte Suriname flinke stappen. In 2025 speelde het voor de tweede keer op rij op de Gold Cup, met onder meer een 4-3-nederlaag tegen Costa Rica en een 0-0 tegen de Dominicaanse Republiek. In de WK-kwalificatie ging Natio lang aan kop van zijn groep en bereikte het de intercontinentale play-offs. Daar ging het op 26 maart 2026 in Monterrey mis: na een 0-1-voorsprong door Liam van Gelderen won Bolivia met 2-1. Op de FIFA-ranglijst klom Suriname intussen naar plek 128.</p>
<p>Het najaar was zwaar. In de Nations League van de CONCACAF won Suriname van Honduras (2-3) en Martinique (2-1), maar na een 0-0 thuis en een 1-0-nederlaag in Guatemala bleef de ploeg steken op de derde plaats. Dat laatste duel werd overschaduwd door racisme: Surinaamse spelers hoorden apengeluiden en Richonell Margaret kreeg rood. FIFA-voorzitter Infantino noemde het "volkomen onacceptabel". De straffen die de CONCACAF daarna uitdeelde, vond de Surinaamse bond veel te licht.</p>
{tabel(["Datum", "Wedstrijd", "Uitslag"], [
    ("12 november 2026", "Litouwen – Suriname (oefenduel, Kaunas)", "0-0"),
    ("5 oktober 2026", "Guatemala – Suriname (Nations League)", "1-0"),
    ("2 oktober 2026", "Suriname – Guatemala (Nations League)", "0-0"),
    ("28 september 2026", "Suriname – Martinique (Nations League)", "2-1"),
    ("25 september 2026", "Honduras – Suriname (Nations League)", "2-3"),
    ("26 maart 2026", "Bolivia – Suriname (WK-play-off, Monterrey)", "2-1"),
])}
<h3><strong>Kaarten en kijken</strong></h3>
<p>Wil je erbij zijn? Er waren vrijdag nog kaarten vanaf €10; lees alles over {L['tickets']}. Kijken vanaf de bank? Op vrijdag was er nog geen uitzending aangekondigd. Of dat verandert, lees je in {L['kijken']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wat is de voorspelling voor Suriname – Eswatini?</strong><br>Wij voorspellen een 2-0-zege voor Suriname. Natio staat 128e op de FIFA-ranglijst, Eswatini 164e.</p>
<p><strong>Hebben Suriname en Eswatini al eens tegen elkaar gespeeld?</strong><br>Nee, zondag is de eerste ontmoeting ooit.</p>
<p><strong>Wie is de bondscoach van Suriname?</strong><br>Henk Fraser. Hij volgde eind juli 2026 Henk ten Cate op.</p>
<p><strong>Wie zijn de debutanten bij Suriname?</strong><br>Onder anderen Cheveyo Balentien (AC Milan), Neville Ogidi Nwankwo (FC Utrecht), Sanjeev van Haren (NEC), Jaden Pinas (FC Dordrecht) en David Garden (Excelsior). Doelman Jahnilo Wiegel-Triebel debuteerde al in Litouwen.</p>
<p><strong>Is Eswatini hetzelfde als Swaziland?</strong><br>Ja. Het land heet sinds april 2018 officieel Eswatini.</p>
<p><strong>Wanneer speelde Suriname voor het laatst in Nederland?</strong><br>Op 24 maart 2024, tegen Martinique in Almere (1-1).</p>
{KSA}"""

if __name__ == "__main__":
    import re
    alles = content + content2 + content3
    w = len(re.sub(r"<[^>]+>", " ", alles).split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", w, "woorden")
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert 164 - 128 == 36
    assert "<h2" not in alles and "betcity" not in alles.lower() and "/go/" not in alles
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles) and content3.rstrip().endswith(KSA)
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    print("dry run ok")
