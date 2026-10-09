# -*- coding: utf-8 -*-
"""Wedtips Swiss Darts Trophy, zaterdag 10 okt 2026 (tweede ronde). Vooraf gepubliceerd op 9 okt (voor indexatie);
tegenstanders + odds worden bijgewerkt zodra de eerste ronde gespeeld is (RESULTATEN/ODDS hieronder invullen).
  python3 specials/wedtips_swiss_darts_10_okt.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Wedtips Swiss Darts Trophy zaterdag 10 oktober: voorspellingen voor de tweede ronde"
SLUG = "wedtips-swiss-darts-trophy-10-oktober-2026"
SAMENVATTING = ("Op zaterdag stromen de zestien reekshoofden in. Onze voorspellingen en wedtips voor de tweede ronde van de "
                "Swiss Darts Trophy in Basel.")
RUBRIEK_DARTS = "66b726271e317999159d5d44"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in koppen)
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}><thead><tr>{kop}</tr></thead><tbody>{body}</tbody></table>"


# (reekshoofd, tegenstander = winnaar van ..., onze voorspelling)
MIDDAG = [
    ("(16) Krzysztof Ratajski", "Gilding / Bellmont", "Ratajski"),
    ("(11) Wessel Nijman", "Białecki / Sedláček", "Nijman"),
    ("(14) Luke Woodhouse", "Cross / Vandenbogaerde", "Woodhouse"),
    ("(15) Martin Schindler", "Cullen / Bissell", "Schindler"),
    ("(9) Ryan Searle", "Menzies / Reyes", "Searle"),
    ("(12) Ross Smith", "O'Connor / Haavisto", "Ross Smith"),
    ("(10) Chris Dobey", "Zonneveld / Brooks", "Dobey"),
    ("(13) Jermaine Wattimena", "M. Smith / Owen", "Wattimena"),
]
AVOND = [
    ("(6) Josh Rock", "Chisnall / Soutar", "Rock"),
    ("(7) Stephen Bunting", "De Graaf / Lap", "Bunting"),
    ("(4) James Wade", "Van Duijvenbode / Stoeckli", "Van Duijvenbode"),
    ("(3) Jonny Clayton", "Van Barneveld / Kuivenhoven", "Clayton"),
    ("(5) Michael van Gerwen", "Suljović / Jehirszki", "Van Gerwen"),
    ("(1) Luke Humphries", "Doets / Kenny", "Humphries"),
    ("(2) Gian van Veen", "Springer / Wellinger", "Van Veen"),
    ("(8) Danny Noppert", "Heta / Fehlmann", "Noppert"),
]

content = f"""<p><strong>Op zaterdag 10 oktober stromen de zestien reekshoofden in bij de Swiss Darts Trophy in Basel. Grote namen als Luke Humphries, Gian van Veen, Michael van Gerwen en titelverdediger Stephen Bunting spelen hun eerste wedstrijd. Onze beste wedtips: Humphries en Van Veen winnen hun openingsduel, Bunting begint zijn titelverdediging met een zege en Dirk van Duijvenbode verrast James Wade.</strong></p>
<p>Na de eerste ronde op vrijdag gaat het toernooi op zaterdag pas echt los. Alle zestien wedstrijden van de tweede ronde worden in twee sessies gespeeld, vanaf 13:00 en 19:00 uur. De reekshoofden spelen tegen de winnaars van vrijdag. Voor de Nederlanders is het een drukke dag: Van Veen, Van Gerwen, Noppert, Nijman en Wattimena komen in actie, en ook de Nederlandse winnaars van vrijdag zijn weer van de partij.</p>
<p><em>Dit artikel werken we bij zodra de eerste ronde is gespeeld. Dan staan hier de definitieve tegenstanders en de actuele odds. De tips en odds voor vrijdag vind je in onze <a href="/nieuws/wedtips-swiss-darts-trophy-9-oktober-2026">wedtips voor de eerste dag</a>.</em></p>
<h3><strong>Onze beste wedtips voor zaterdag</strong></h3>
<ul><li><strong>Luke Humphries wint zijn openingspartij</strong> tegen Kevin Doets of Nick Kenny</li><li><strong>Gian van Veen wint zijn openingspartij</strong> tegen Niko Springer of Roman Wellinger</li><li><strong>Stephen Bunting wint</strong> van Jeffrey de Graaf of Sietse Lap</li><li><strong>Verrassing: Dirk van Duijvenbode wint van James Wade</strong>, als hij vrijdag zijn eerste partij wint</li></ul>
<h3><strong>Speelschema en voorspellingen zaterdag 10 oktober</strong></h3>
<p><strong>Middagsessie (vanaf 13:00 uur)</strong></p>
{tabel(["Reekshoofd", "Tegen winnaar van", "Onze voorspelling"], MIDDAG)}
<p><strong>Avondsessie (vanaf 19:00 uur)</strong></p>
{tabel(["Reekshoofd", "Tegen winnaar van", "Onze voorspelling"], AVOND)}"""

content2 = """<h3><strong>Tip 1: Luke Humphries wint zijn openingspartij</strong></h3>
<p>Zonder Luke Littler is Humphries de topfavoriet voor de eindzege in Basel. De nummer één van de plaatsingslijst speelt in de laatste wedstrijd van de avond tegen de winnaar van Kevin Doets – Nick Kenny. Doets is een lastige tegenstander, die vrijdag als favoriet aan de start staat, maar een Humphries in vorm wint dit soort partijen bijna altijd. Wil je meer rendement, kijk dan naar een leg handicap op Humphries in plaats van de kale winst.</p>
<h3><strong>Tip 2: Gian van Veen wint zijn openingspartij</strong></h3>
<p>Van Veen is het tweede reekshoofd en de grootste Nederlandse kanshebber voor de titel. Waarschijnlijk treft hij de Duitser Niko Springer, die vrijdag de grote favoriet is tegen de Zwitserse qualifier Roman Wellinger. Springer kan goed darten, maar Van Veen is een klasse beter. Wij rekenen op een zege voor de Nederlander, die in de kwartfinale titelverdediger Bunting kan tegenkomen.</p>
<h3><strong>Tip 3: Stephen Bunting begint met een zege</strong></h3>
<p>De titelverdediger voelt zich thuis in de St. Jakobshalle: vorig jaar won hij hier de finale met 8-3 en een gemiddelde van bijna 104. Zijn tegenstander is de winnaar van Jeffrey de Graaf – Sietse Lap. Allebei hebben ze kwaliteit, maar Bunting is op dit podium de favoriet. Een overwinning van The Bullet is onze derde tip.</p>
<h3><strong>Tip 4: Dirk van Duijvenbode verrast James Wade</strong></h3>
<p>Dit is onze gok met de hoogste odd. Wint Van Duijvenbode vrijdag van de Zwitser Bruno Stoeckli, dan treft hij zaterdagavond het vierde reekshoofd James Wade. Van Duijvenbode kan op zijn beste dagen iedereen kloppen en is met zijn scoringsvermogen gevaarlijk in een korte best of 11. Wade is ervaren en constant, maar tegen een Aubergenius in vorm zien we de Nederlander als underdog met een goede kans.</p>
<h3><strong>De andere Nederlanders op zaterdag</strong></h3>
<p><strong>Michael van Gerwen</strong> treft de winnaar van Mensur Suljović – György Jehirszki en is favoriet om door te gaan. <strong>Danny Noppert</strong> heeft een lastige loting: zijn waarschijnlijke tegenstander is Damon Heta, een van de sterkste spelers die vrijdag al in actie komt. <strong>Wessel Nijman</strong> speelt tegen Białecki of Sedláček, en <strong>Jermaine Wattimena</strong> mogelijk tegen oud-wereldkampioen Michael Smith. Wint Raymond van Barneveld vrijdag van Maik Kuivenhoven, dan wacht een aansprekend duel met Jonny Clayton.</p>"""

content3 = """<h3><strong>Kijken en wedden op de Swiss Darts Trophy</strong></h3>
<p>De Swiss Darts Trophy is in Nederland te volgen via <a href="/zenders/viaplay">Viaplay</a>, dat de rechten op de PDC-toernooien heeft. De speeldag begint om 13:00 uur, de avondsessie om 19:00 uur. Wedden op darts kan bij de meeste Nederlandse bookmakers, met markten op de winnaar, leg handicaps, het aantal legs en 180's. Meer over het toernooi, de loting en het format lees je in onze <a href="/nieuws/swiss-darts-trophy-2026">voorbeschouwing van de Swiss Darts Trophy 2026</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wie spelen er zaterdag bij de Swiss Darts Trophy?</strong><br>De zestien reekshoofden, onder wie Luke Humphries, Gian van Veen, Michael van Gerwen, Danny Noppert en Stephen Bunting, tegen de winnaars van de eerste ronde.</p>
<p><strong>Hoe laat begint de darts op zaterdag?</strong><br>De middagsessie begint om 13:00 uur en de avondsessie om 19:00 uur.</p>
<p><strong>Wat is de beste wedtip voor zaterdag?</strong><br>Onze veiligste tip is een zege van Luke Humphries in zijn openingspartij. Wil je een hogere odd, dan kies je voor Dirk van Duijvenbode tegen James Wade.</p>
<p><strong>Wanneer is de finale van de Swiss Darts Trophy?</strong><br>Op zondag 11 oktober, in de avondsessie die om 19:00 uur begint.</p>
<p><em>24+ | Gokken is alleen toegestaan voor personen van 18 jaar en ouder. Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_DARTS,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting"); sys.exit()
    print("item:", WF.create_live(fd))
