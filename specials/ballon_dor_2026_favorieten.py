# -*- coding: utf-8 -*-
"""Los artikel: Favorieten Ballon d'Or 2026 (uitreiking ma 26 okt 2026, Londen, 70e editie).
Aanleveringstekst herschreven. Gecontroleerd: 30 genomineerden (lijst 8 sep), Kane 61 goals in 51 clubduels
(36 Bundesliga - topscorer 3e jaar op rij -, 14 CL in 13 duels tot de halve finale, 10 DFB-Pokal incl. hattrick in
de finale) en minstens 6 WK-goals; Yamal 24 goals + 11 assists voor Barcelona (ESPN), kampioen, wereldkampioen
(finale 1-0 n.v. tegen Argentinië, Ferran Torres), vorig jaar 2e achter Dembélé. Weggelaten (niet te bevestigen):
73 goals Kane, 25+20 Yamal, Yamal-WK-bijdrage, Reijnders bij Al-Qadsiah.
  python3 specials/ballon_dor_2026_favorieten.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Favorieten Ballon d'Or 2026: Harry Kane of Lamine Yamal?"
SLUG = "favorieten-ballon-dor-2026"
SAMENVATTING = ("Op 26 oktober wordt de Ballon d'Or 2026 uitgereikt. Alle 30 genomineerden, Kane tegen Yamal in cijfers, "
                "onze favoriet en alle eerdere winnaars.")
RUBRIEK_ALGEMEEN = "6502b65d49bc032ba533e7a2"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in koppen)
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}><thead><tr>{kop}</tr></thead><tbody>{body}</tbody></table>"


GENOMINEERDEN = [
    ("Jude Bellingham", "Real Madrid"), ("Pau Cubarsí", "FC Barcelona"), ("Marc Cucurella", "Chelsea / Real Madrid"),
    ("Ousmane Dembélé", "Paris Saint-Germain"), ("Luis Díaz", "Bayern München"), ("Bruno Fernandes", "Manchester United"),
    ("Gabriel", "Arsenal"), ("Achraf Hakimi", "Paris Saint-Germain"), ("Erling Haaland", "Manchester City"),
    ("Harry Kane", "Bayern München"), ("Khvicha Kvaratskhelia", "Paris Saint-Germain"), ("Lamine Yamal", "FC Barcelona"),
    ("Sadio Mané", "Al-Nassr"), ("Marquinhos", "Paris Saint-Germain"), ("Lautaro Martínez", "Inter"),
    ("Kylian Mbappé", "Real Madrid"), ("Nuno Mendes", "Paris Saint-Germain"), ("Lionel Messi", "Inter Miami"),
    ("João Neves", "Paris Saint-Germain"), ("Michael Olise", "Bayern München"), ("Willian Pacho", "Paris Saint-Germain"),
    ("Julián Quiñones", "Al-Qadsiah"), ("Declan Rice", "Arsenal"), ("Rodri", "Manchester City / FC Barcelona"),
    ("Fabián Ruiz", "Paris Saint-Germain"), ("William Saliba", "Arsenal"), ("Ferran Torres", "FC Barcelona / Paris Saint-Germain"),
    ("Dayot Upamecano", "Bayern München"), ("Vinícius Júnior", "Real Madrid"), ("Vitinha", "Paris Saint-Germain"),
]

WINNAARS = [
    ("2025", "Ousmane Dembélé", "Paris Saint-Germain"), ("2024", "Rodri", "Manchester City"),
    ("2023", "Lionel Messi", "Paris Saint-Germain / Inter Miami"), ("2022", "Karim Benzema", "Real Madrid"),
    ("2021", "Lionel Messi", "FC Barcelona / Paris Saint-Germain"), ("2020", "Niet uitgereikt (coronapandemie)", "-"),
    ("2019", "Lionel Messi", "FC Barcelona"), ("2018", "Luka Modrić", "Real Madrid"), ("2017", "Cristiano Ronaldo", "Real Madrid"),
    ("2016", "Cristiano Ronaldo", "Real Madrid"), ("2015", "Lionel Messi", "FC Barcelona"), ("2014", "Cristiano Ronaldo", "Real Madrid"),
    ("2013", "Cristiano Ronaldo", "Real Madrid"), ("2012", "Lionel Messi", "FC Barcelona"), ("2011", "Lionel Messi", "FC Barcelona"),
    ("2010", "Lionel Messi", "FC Barcelona"), ("2009", "Lionel Messi", "FC Barcelona"), ("2008", "Cristiano Ronaldo", "Manchester United"),
    ("2007", "Kaká", "AC Milan"), ("2006", "Fabio Cannavaro", "Juventus / Real Madrid"), ("2005", "Ronaldinho", "FC Barcelona"),
    ("2004", "Andrij Sjevtsjenko", "AC Milan"), ("2003", "Pavel Nedvěd", "Juventus"), ("2002", "Ronaldo", "Real Madrid"),
    ("2001", "Michael Owen", "Liverpool"), ("2000", "Luís Figo", "Real Madrid"), ("1999", "Rivaldo", "FC Barcelona"),
    ("1998", "Zinédine Zidane", "Juventus"), ("1997", "Ronaldo", "Internazionale"), ("1996", "Matthias Sammer", "Borussia Dortmund"),
    ("1995", "George Weah", "AC Milan"), ("1994", "Hristo Stoitsjkov", "FC Barcelona"), ("1993", "Roberto Baggio", "Juventus"),
    ("1992", "<strong>Marco van Basten</strong>", "AC Milan"), ("1991", "Jean-Pierre Papin", "Olympique Marseille"),
    ("1990", "Lothar Matthäus", "Internazionale"), ("1989", "<strong>Marco van Basten</strong>", "AC Milan"),
    ("1988", "<strong>Marco van Basten</strong>", "AC Milan"), ("1987", "<strong>Ruud Gullit</strong>", "AC Milan"),
    ("1986", "Ihor Belanov", "Dynamo Kiev"), ("1985", "Michel Platini", "Juventus"), ("1984", "Michel Platini", "Juventus"),
    ("1983", "Michel Platini", "Juventus"), ("1982", "Paolo Rossi", "Juventus"), ("1981", "Karl-Heinz Rummenigge", "Bayern München"),
    ("1980", "Karl-Heinz Rummenigge", "Bayern München"), ("1979", "Kevin Keegan", "Hamburger SV"), ("1978", "Kevin Keegan", "Hamburger SV"),
    ("1977", "Allan Simonsen", "Borussia Mönchengladbach"), ("1976", "Franz Beckenbauer", "Bayern München"),
    ("1975", "Oleg Blochin", "Dynamo Kiev"), ("1974", "<strong>Johan Cruijff</strong>", "FC Barcelona"),
    ("1973", "<strong>Johan Cruijff</strong>", "FC Barcelona"), ("1972", "Franz Beckenbauer", "Bayern München"),
    ("1971", "<strong>Johan Cruijff</strong>", "Ajax"), ("1970", "Gerd Müller", "Bayern München"), ("1969", "Gianni Rivera", "AC Milan"),
    ("1968", "George Best", "Manchester United"), ("1967", "Flórián Albert", "Ferencváros"), ("1966", "Bobby Charlton", "Manchester United"),
    ("1965", "Eusébio", "Benfica"), ("1964", "Denis Law", "Manchester United"), ("1963", "Lev Jasjin", "Dinamo Moskou"),
    ("1962", "Josef Masopust", "Dukla Praag"), ("1961", "Omar Sívori", "Juventus"), ("1960", "Luis Suárez", "FC Barcelona"),
    ("1959", "Alfredo Di Stéfano", "Real Madrid"), ("1958", "Raymond Kopa", "Real Madrid"), ("1957", "Alfredo Di Stéfano", "Real Madrid"),
    ("1956", "Stanley Matthews", "Blackpool"),
]

content = f"""<p><strong>Op maandag 26 oktober 2026 wordt in Londen de Ballon d'Or uitgereikt, de prestigieuze prijs voor de beste voetballer van het seizoen. Het is de zeventigste editie en de beoordeling gaat over het seizoen 2025/26, inclusief het WK. Wie neemt de Gouden Bal mee naar huis? Wat ons betreft gaat het tussen twee spelers, en één van hen heeft onze voorkeur.</strong></p>
<p>In dit artikel vind je alle dertig genomineerden, de cijfers van de twee grote favorieten, onze voorspelling en een overzicht van alle eerdere winnaars, met de drie Nederlanders die de prijs ooit wonnen.</p>
<h3><strong>Ballon d'Or 2026 in het kort</strong></h3>
{tabel(["", ""], [
    ("<strong>Uitreiking</strong>", "Maandag 26 oktober 2026, Londen"),
    ("<strong>Editie</strong>", "70e"),
    ("<strong>Beoordeeld seizoen</strong>", "2025/26, inclusief het WK 2026"),
    ("<strong>Genomineerden</strong>", "30 spelers"),
    ("<strong>Titelhouder</strong>", "Ousmane Dembélé (Paris Saint-Germain)"),
    ("<strong>Grootste favorieten</strong>", "Harry Kane en Lamine Yamal"),
])}
<h3><strong>De 30 genomineerden voor de Ballon d'Or 2026</strong></h3>
<p>Organisator France Football maakte op 8 september de lijst met dertig kanshebbers bekend. Daarop staan de verwachte grote namen, maar ook een paar keuzes die voor discussie zorgden. De meest opvallende is <strong>Julián Quiñones</strong>, de Mexicaanse spits van het Saoedische Al-Qadsiah. Hij is de enige Mexicaan op de lijst. Tegelijk ontbreken Raphinha van FC Barcelona en Cristiano Ronaldo, terwijl Sadio Mané wel genomineerd is. Paris Saint-Germain, de club van titelhouder Dembélé, levert met negen spelers de grootste afvaardiging.</p>
{tabel(["Speler", "Club"], GENOMINEERDEN)}"""

content2 = f"""<h3><strong>Harry Kane of Lamine Yamal: wie verdient de Gouden Bal?</strong></h3>
<p>Kijken we naar de grootste kanshebbers, dan komen we uit bij twee spelers met een heel ander profiel: de ervaren Engelse spits <strong>Harry Kane</strong> en het Spaanse supertalent <strong>Lamine Yamal</strong>. Ook Lionel Messi en Kylian Mbappé worden genoemd, maar zij hebben wat ons betreft een flinke achterstand op dit duo.</p>
{tabel(["", "Harry Kane", "Lamine Yamal"], [
    ("<strong>Club</strong>", "Bayern München", "FC Barcelona"),
    ("<strong>Clubgoals 2025/26</strong>", "61 (in 51 wedstrijden)", "24"),
    ("<strong>Clubassists 2025/26</strong>", "-", "11"),
    ("<strong>Competitie</strong>", "Kampioen + topscorer Bundesliga (36 goals)", "Kampioen LaLiga"),
    ("<strong>Beker</strong>", "DFB-Pokal, met een hattrick in de finale", "-"),
    ("<strong>Champions League</strong>", "14 goals, halve finale", "-"),
    ("<strong>WK 2026</strong>", "Minstens 6 goals voor Engeland", "Wereldkampioen met Spanje"),
    ("<strong>Ballon d'Or 2025</strong>", "-", "2e achter Dembélé"),
])}
<h4>Waarom Harry Kane?</h4>
<p>De cijfers van Kane zijn indrukwekkend. Met 61 goals in 51 wedstrijden voor Bayern München was hij het hele seizoen de beslissende factor. Hij werd voor het derde jaar op rij topscorer van de Bundesliga met 36 treffers en scoorde 14 keer in de Champions League, waarin Bayern de halve finale haalde. In de DFB-Pokal maakte hij tien doelpunten, met een hattrick in de finale. Op het WK bleef hij scoren: met minstens zes goals schoot hij Engeland naar de kwartfinale, en werd hij de Engelse topscorer aller tijden op WK's.</p>
<h4>Waarom Lamine Yamal?</h4>
<p>Yamal heeft het argument dat bij stemmers vaak zwaar weegt: hij werd wereldkampioen. Spanje won de finale van het WK 2026 met 1-0 na verlenging van Argentinië, met een winnende treffer van Ferran Torres. Bij Barcelona was Yamal met 24 goals en 11 assists opnieuw de smaakmaker van het elftal dat landskampioen werd, en hij werd door velen uitgeroepen tot speler van het seizoen in LaLiga. Vorig jaar eindigde hij al als tweede in de verkiezing. Dat hij bovendien pas negentien is, maakt zijn seizoen nog opmerkelijker.</p>
<h4>Onze favoriet: Harry Kane</h4>
<p>Wij kiezen voor <strong>Harry Kane</strong>. Zijn doelpuntenproductie, zijn constantheid over het hele seizoen en zijn rol in de Champions League én op het WK maken hem voor ons de logische winnaar. Toch is het een nek-aan-nekrace: een wereldtitel weegt bij de jury traditioneel zwaar, en dat maakt Yamal een zeer serieuze kandidaat.</p>"""

content3 = f"""<h3><strong>Alle winnaars van de Ballon d'Or</strong></h3>
<p>Sinds 1956 is de Ballon d'Or uitgereikt aan de grootste spelers uit de geschiedenis. In 2020 ging de verkiezing niet door vanwege de coronapandemie, waardoor 2026 de zeventigste editie is. Lionel Messi is met acht overwinningen recordhouder, gevolgd door Cristiano Ronaldo met vijf.</p>
<p>Ook Nederland heeft een mooie band met de prijs. Drie Nederlanders wonnen de Gouden Bal: <strong>Johan Cruijff</strong> (1971, 1973 en 1974), <strong>Marco van Basten</strong> (1988, 1989 en 1992) en <strong>Ruud Gullit</strong> (1987). Zij staan hieronder vetgedrukt.</p>
{tabel(["Jaar", "Winnaar", "Club"], WINNAARS)}
<h3><strong>Veelgestelde vragen over de Ballon d'Or 2026</strong></h3>
<p><strong>Wanneer wordt de Ballon d'Or 2026 uitgereikt?</strong><br>Op maandag 26 oktober 2026 in Londen.</p>
<p><strong>Wie zijn de favorieten?</strong><br>Harry Kane (Bayern München) en Lamine Yamal (FC Barcelona). Wij zien Kane als favoriet, maar de wereldtitel van Yamal maakt het spannend.</p>
<p><strong>Over welk seizoen gaat de Ballon d'Or 2026?</strong><br>Over het seizoen 2025/26, inclusief het WK 2026.</p>
<p><strong>Wie won de Ballon d'Or 2025?</strong><br>Ousmane Dembélé van Paris Saint-Germain, met Lamine Yamal als tweede.</p>
<p><strong>Welke Nederlanders wonnen de Ballon d'Or?</strong><br>Johan Cruijff en Marco van Basten (allebei drie keer) en Ruud Gullit (één keer).</p>
<p><strong>Wie won de Ballon d'Or het vaakst?</strong><br>Lionel Messi, met acht overwinningen.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_ALGEMEEN,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting"); sys.exit()
    print("item:", WF.create_live(fd))
