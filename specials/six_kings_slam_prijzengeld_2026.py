# -*- coding: utf-8 -*-
"""Los artikel: Six Kings Slam prijzengeld 2026. Feiten nagelopen op 21-10-2026 (Wikipedia 2024/2025 Six Kings Slam,
Front Office Sports, Tennis365, Tennis Majors, Sky Sports, ATP Tour, nittoatpfinals.com, ECB-koers 20-10-2026).
Bedragen 2026 zijn door de organisatie niet apart bekendgemaakt: "naar verwachting" gelijk aan 2024/2025.
  python3 specials/six_kings_slam_prijzengeld_2026.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Six Kings Slam prijzengeld 2026: zoveel verdienen Alcaraz, Djokovic en co in Riyad"
SLUG = "six-kings-slam-prijzengeld-2026"
SAMENVATTING = ("Six Kings Slam prijzengeld 2026: 1,5 miljoen dollar startgeld per speler en 6 miljoen voor de winnaar. "
                "Alle bedragen in euro's, per plaats en vergeleken.")
RUBRIEK_TENNIS = "665715dbf1f3cbdf7f874d79"
COMPETITIE_SKS = "68f1f95e07965f31dc1401b2"
HOOFD = "/nieuws/six-kings-slam-2026"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>Het prijzengeld van de Six Kings Slam 2026 is naar verwachting weer het hoogste van het hele tennisjaar. Elke speler krijgt 1,5 miljoen dollar (± €1,34 miljoen) alleen al voor zijn deelname, en de winnaar gaat naar huis met 6 miljoen dollar (± €5,35 miljoen). In totaal ligt er 13,5 miljoen dollar (± €12 miljoen) klaar voor zes spelers, die maximaal drie wedstrijden spelen. Dat is meer dan de winnaar van de US Open, Wimbledon of de ATP Finals verdient.</strong></p>
<p>De derde editie van de Six Kings Slam is verplaatst naar 27 tot en met 30 december 2026 in de ANB Arena in Riyad. Carlos Alcaraz, Novak Djokovic, Alexander Zverev, Taylor Fritz, Alex de Minaur en Learner Tien (de vervanger van de geblesseerde Jannik Sinner) spelen om het geld. Hieronder zie je precies wat er te verdienen valt, wat elke speler minimaal en maximaal meeneemt, hoe het zich verhoudt tot de grandslams en wat de spelers in 2024 en 2025 verdienden. Alles over het schema, de loting en waar je kijkt, lees je in ons <a href="{HOOFD}">overzichtsartikel over de Six Kings Slam 2026</a>.</p>
<h3><strong>Hoeveel prijzengeld is er te verdienen op de Six Kings Slam 2026?</strong></h3>
{tabel(["Onderdeel", "Bedrag in dollar", "Omgerekend in euro"], [
    ("Startgeld per speler (gegarandeerd)", "$ 1.500.000", "± € 1.340.000"),
    ("Bonus voor de winnaar", "$ 4.500.000", "± € 4.010.000"),
    ("<strong>Totaal voor de winnaar</strong>", "<strong>$ 6.000.000</strong>", "<strong>± € 5.350.000</strong>"),
    ("Totale prijzenpot (6 spelers)", "$ 13.500.000", "± € 12.040.000"),
])}
<p>De euro-bedragen zijn omgerekend tegen de ECB-koers van 20 oktober 2026 (1 dollar = € 0,89) en dus indicatief. De organisatie, de Saudische General Entertainment Authority, heeft de bedragen voor 2026 niet apart bekendgemaakt. Ook na het uitstel naar december heeft geen enkele bron een wijziging gemeld, dus de verwachting is dat dezelfde structuur geldt als in 2024 en 2025.</p>
<h3><strong>Prijzengeld per plaats: wat krijgt de finalist?</strong></h3>
<p>Het prijzengeld werkt op de Six Kings Slam anders dan op een gewoon ATP-toernooi. Daar stijgt het bedrag met elke ronde die je wint. Hier krijgt iedereen hetzelfde startgeld en verdient alleen de winnaar extra. De verliezend finalist krijgt voor zover bekend niets bovenop zijn 1,5 miljoen, en de troostfinale levert ook geen extra geld op.</p>
{tabel(["Plaats", "Prijzengeld", "In euro"], [
    ("Winnaar", "$ 6.000.000", "± € 5.350.000"),
    ("Finalist", "$ 1.500.000", "± € 1.340.000"),
    ("Derde plaats", "$ 1.500.000", "± € 1.340.000"),
    ("Vierde plaats", "$ 1.500.000", "± € 1.340.000"),
    ("Verliezers kwartfinale (2 spelers)", "$ 1.500.000 per speler", "± € 1.340.000 per speler"),
])}
<p>Het verschil tussen winnen en verliezen in de finale is dus 4,5 miljoen dollar, voor één wedstrijd. Dat is meer dan de winnaars van Roland Garros en de Australian Open 2026 in totaal kregen.</p>
<h3><strong>Wat verdient elke speler minimaal en maximaal?</strong></h3>
<p>Alcaraz en Djokovic, de twee spelers met de meeste grandslamtitels, krijgen een bye naar de halve finale. Zij hebben maar twee overwinningen nodig voor de hoofdprijs. De andere vier beginnen in de kwartfinale en moeten drie keer winnen. Wie in de kwartfinale verliest, speelt maar één wedstrijd, maar heeft zijn 1,5 miljoen dollar wel binnen.</p>
{tabel(["Speler", "ATP-ranking*", "Start", "Minimaal", "Maximaal"], [
    ("Carlos Alcaraz", "3", "Halve finale (bye)", "$ 1,5 mln na 2 duels", "$ 6 mln na 2 duels"),
    ("Novak Djokovic", "12", "Halve finale (bye)", "$ 1,5 mln na 2 duels", "$ 6 mln na 2 duels"),
    ("Alexander Zverev", "2", "Kwartfinale", "$ 1,5 mln na 1 duel", "$ 6 mln na 3 duels"),
    ("Taylor Fritz", "14", "Kwartfinale", "$ 1,5 mln na 1 duel", "$ 6 mln na 3 duels"),
    ("Alex de Minaur", "8", "Kwartfinale", "$ 1,5 mln na 1 duel", "$ 6 mln na 3 duels"),
    ("Learner Tien", "18", "Kwartfinale", "$ 1,5 mln na 1 duel", "$ 6 mln na 3 duels"),
])}
<p><em>*ATP-ranking van 19 oktober 2026.</em></p>
<p>Voor Alcaraz en Djokovic komt de hoofdprijs dus neer op 3 miljoen dollar per gewonnen wedstrijd. Ter vergelijking: de winnaar van de US Open 2026 moest zeven wedstrijden over vijf sets winnen voor 5,5 miljoen dollar, gemiddeld zo'n 786.000 dollar per wedstrijd.</p>"""

content2 = f"""<h3><strong>Six Kings Slam vs. grandslams en ATP Finals</strong></h3>
<p>Wat de Six Kings Slam zo opvallend maakt, is de verhouding tussen geld en inspanning. Hieronder het winnaarsbedrag in het enkelspel bij de grootste toernooien van 2026, omgerekend tegen dezelfde koers.</p>
{tabel(["Toernooi", "Winnaar (officieel)", "± in euro", "Wedstrijden voor de titel"], [
    ("<strong>Six Kings Slam</strong> (exhibitie)", "<strong>$ 6.000.000</strong>", "<strong>€ 5,35 mln</strong>", "2 of 3"),
    ("US Open 2026", "$ 5.500.000", "€ 4,90 mln", "7"),
    ("ATP Finals 2025 (ongeslagen kampioen)*", "$ 5.071.000", "€ 4,52 mln", "5"),
    ("Wimbledon 2026", "£ 3.600.000", "€ 4,28 mln", "7"),
    ("Roland Garros 2026", "€ 2.800.000", "€ 2,80 mln", "7"),
    ("Australian Open 2026", "A$ 4.150.000", "€ 2,58 mln", "7"),
    ("Laver Cup 2026 (per speler winnend team)", "$ 250.000", "€ 0,22 mln", "-"),
])}
<p><em>*De bedragen voor de ATP Finals 2026 in Turijn (15-22 november) zijn nog niet gepubliceerd; daarom staat hier het bedrag van 2025.</em></p>
<p>De totale prijzenpot van een grandslam is wel vele malen groter. De US Open 2026 verdeelde 108 miljoen dollar over honderden spelers, Wimbledon 64,2 miljoen pond. Op de Six Kings Slam gaat 13,5 miljoen dollar naar slechts zes man. Per deelnemer is het daarmee het best betaalde tennisevenement ter wereld.</p>
<h3><strong>Hoeveel verdienden de spelers in 2024 en 2025?</strong></h3>
<p>De structuur is sinds de eerste editie gelijk gebleven. Jannik Sinner won beide keren en verdiende zo in twee jaar 12 miljoen dollar met zes wedstrijden in Riyad.</p>
<p><strong>Six Kings Slam 2024</strong></p>
{tabel(["Speler", "Resultaat", "Verdiend"], [
    ("Jannik Sinner", "Winnaar (finale tegen Alcaraz: 6-7, 6-3, 6-3)", "$ 6.000.000"),
    ("Carlos Alcaraz", "Finalist", "$ 1.500.000"),
    ("Novak Djokovic", "Derde (won de troostfinale van Nadal)", "$ 1.500.000"),
    ("Rafael Nadal", "Vierde", "$ 1.500.000 + gouden racket"),
    ("Daniil Medvedev", "Kwartfinale", "$ 1.500.000"),
    ("Holger Rune", "Kwartfinale", "$ 1.500.000"),
])}
<p>Sommige media meldden in 2024 dat Sinner 7,5 miljoen dollar kreeg (1,5 miljoen startgeld plus 6 miljoen). Dat klopt niet met de totale pot van 13,5 miljoen: 6 miljoen is het totaalbedrag voor de winnaar, inclusief startgeld. Sinners 6 miljoen was destijds het hoogste bedrag dat ooit met één tennistoernooi werd verdiend.</p>
<p><strong>Six Kings Slam 2025</strong></p>
{tabel(["Speler", "Resultaat", "Verdiend"], [
    ("Jannik Sinner", "Winnaar (finale tegen Alcaraz)", "$ 6.000.000 + gouden racket"),
    ("Carlos Alcaraz", "Finalist", "$ 1.500.000"),
    ("Taylor Fritz", "Derde (Djokovic gaf op in de troostfinale)", "$ 1.500.000"),
    ("Novak Djokovic", "Vierde", "$ 1.500.000"),
    ("Alexander Zverev", "Kwartfinale", "$ 1.500.000"),
    ("Stefanos Tsitsipas", "Kwartfinale", "$ 1.500.000"),
])}
<p>Een opvallend rekensommetje uit 2025: Zverev verloor zijn kwartfinale van Fritz in 59 minuten (6-4, 6-4). Voor dat uurtje tennis kreeg hij 1,5 miljoen dollar, omgerekend zo'n 25.000 dollar per minuut.</p>
<p><strong>Totaal verdiend op de Six Kings Slam (2024 + 2025)</strong></p>
{tabel(["Speler", "Edities", "Totaal"], [
    ("Jannik Sinner", "2 (2 keer winnaar)", "$ 12.000.000"),
    ("Carlos Alcaraz", "2", "$ 3.000.000"),
    ("Novak Djokovic", "2", "$ 3.000.000"),
    ("Taylor Fritz, Alexander Zverev", "1", "$ 1.500.000 elk"),
    ("Alex de Minaur, Learner Tien", "Debuut in 2026", "-"),
])}
<p>Alcaraz en Djokovic staan dit jaar voor het derde jaar op rij in Riyad en tikken dus sowieso de 4,5 miljoen dollar aan. Wint een van hen, dan komt hij op 9 miljoen dollar uit drie edities.</p>
<h3><strong>Het gouden racket: de bonus bovenop het geld</strong></h3>
<p>Naast het prijzengeld deelt de Six Kings Slam een opvallende trofee uit: een levensgroot tennisracket van massief goud. Sinner kreeg in 2025 een handgemaakt racket van 24-karaats goud, van ongeveer vier kilo, zo'n twintig keer zo zwaar als een normaal racket. De waarde wordt geschat op ongeveer 250.000 dollar, al heeft de organisatie dat nooit bevestigd. Rafael Nadal kreeg in 2024 een gouden racket van zo'n drie kilo als eerbetoon aan zijn loopbaan, kort voor zijn afscheid. Of er in december 2026 weer een gouden racket klaarligt, is nog niet aangekondigd.</p>"""

content3 = f"""<h3><strong>Telt het prijzengeld mee voor de ATP-ranglijst?</strong></h3>
<p>Nee. De Six Kings Slam is een exhibitie en staat los van de ATP Tour. Spelers verdienen geen rankingpunten en de uitslagen tellen niet mee voor de officiële onderlinge resultaten. Ook het geld komt niet in de officiële prijzengeldstatistieken van de ATP: Sinners miljoenen uit Riyad staan niet in zijn carrièretotaal op atptour.com. Voor de spelers is het puur extra inkomen, zonder sportieve druk op de ranglijst.</p>
<h3><strong>Waarom is het prijzengeld zo hoog?</strong></h3>
<p>Het toernooi is onderdeel van Riyadh Season, het grote entertainmentprogramma van Saudi-Arabië. Het land investeert al jaren fors in topsport, van voetbal en golf tot boksen en tennis. Met een prijzenpot die de grandslams overtreft, trekt de organisatie de grootste namen naar Riyad, en dankzij de wereldwijde uitzending op Netflix bereikt het evenement een enorm publiek.</p>
<p>Daar is ook kritiek op. Mensenrechtenorganisaties noemen de Saudische sportinvesteringen sportswashing: het gebruik van sport om het imago van het land op te poetsen. Rafael Nadal erkende in 2024 dat dat element meespeelt, en Carlos Alcaraz gaf eerlijk toe dat het geld meespeelde in zijn keuze om mee te doen. Sommige spelers, zoals Casper Ruud, sloegen een uitnodiging juist bewust af.</p>
<h3><strong>Moeten de spelers belasting betalen over het prijzengeld?</strong></h3>
<p>Over de belasting op het prijzengeld maakt de organisatie niets bekend. Spelers betalen in de regel belasting in het land waar ze fiscaal wonen. Nadal vertelde in 2024 dat hij als inwoner van Spanje een groot deel van zijn verdiensten afdraagt. Wat er netto overblijft, verschilt daardoor sterk per speler.</p>
<h3><strong>Komt er ook een vrouwentoernooi met prijzengeld?</strong></h3>
<p>Nee. De Six Kings Slam is een enkelspeltoernooi voor zes mannen, zonder dubbelspel en zonder vrouwenonderdeel. De WTA Finals, die in 2024 en 2025 in Riyad werden gespeeld, zijn voor 2026 om veiligheidsredenen verplaatst naar Indian Wells in de Verenigde Staten (8-15 november).</p>
<h3><strong>Wie gaat er met de 6 miljoen vandoor?</strong></h3>
<p>Zonder Sinner, de winnaar van beide eerdere edities, komt er hoe dan ook een nieuwe kampioen. Op papier is Carlos Alcaraz de grootste kanshebber: hij heeft een bye, stond twee keer in de finale en heeft na Djokovic de meeste grandslamtitels van het deelnemersveld. Alexander Zverev, de nummer 2 van de wereld, is de logische uitdager, maar moet drie wedstrijden winnen. Bookmakers hebben nog geen markten geopend voor het toernooi. Zodra er odds zijn, vind je ze in ons <a href="{HOOFD}">artikel over de Six Kings Slam 2026</a> en bij onze <a href="/tennis-voorspellingen-vandaag">tennis voorspellingen van vandaag</a>. Meer over het toernooi vind je op de <a href="/competities/six-kings-slam">Six Kings Slam-pagina</a>. Wil je zien hoe het prijzengeld op een regulier ATP-toernooi werkt? Bekijk dan het <a href="/nieuws/prijzengeld-shanghai-masters-2026">prijzengeld van de Shanghai Masters 2026</a>.</p>
<h3><strong>Veelgestelde vragen over het prijzengeld van de Six Kings Slam</strong></h3>
<p><strong>Hoeveel verdient de winnaar van de Six Kings Slam 2026?</strong><br>Naar verwachting 6 miljoen dollar, omgerekend zo'n € 5,35 miljoen. Dat bestaat uit 1,5 miljoen dollar startgeld en een bonus van 4,5 miljoen dollar.</p>
<p><strong>Hoe groot is de totale prijzenpot?</strong><br>13,5 miljoen dollar (± € 12 miljoen): zes keer 1,5 miljoen startgeld plus de bonus van 4,5 miljoen voor de winnaar.</p>
<p><strong>Wat krijgt de verliezend finalist?</strong><br>Voor zover bekend alleen het startgeld van 1,5 miljoen dollar, net als de andere vier spelers. Alleen de winnaar krijgt extra.</p>
<p><strong>Verdient de winnaar meer dan op een grandslam?</strong><br>Ja. De US Open-winnaar kreeg in 2026 5,5 miljoen dollar, de Wimbledon-winnaar 3,6 miljoen pond. De Six Kings Slam-winnaar krijgt 6 miljoen dollar voor maximaal drie wedstrijden.</p>
<p><strong>Telt het prijzengeld mee voor de officiële ATP-statistieken?</strong><br>Nee. Het is een exhibitie: er zijn geen rankingpunten te verdienen en het geld telt niet mee in het officiële prijzengeld van de spelers.</p>
<p><strong>Wanneer wordt de Six Kings Slam 2026 gespeeld?</strong><br>Van 27 tot en met 30 december 2026 in de ANB Arena in Riyad. Het toernooi was eerst gepland voor 21-24 oktober, maar is op 14 oktober verplaatst.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_TENNIS, "competitie": COMPETITIE_SKS, "tennis": True,
          "datum-tijd-van-wedstrijd": "2026-12-27T16:30:00.000Z",
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        import re
        tekst = re.sub(r"<[^>]+>", " ", content + content2 + content3)
        print(len(SAMENVATTING), "tekens samenvatting |", len(tekst.split()), "woorden"); sys.exit()
    print("item:", WF.create_live(fd))
