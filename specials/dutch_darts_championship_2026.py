# -*- coding: utf-8 -*-
"""Los artikel: Dutch Darts Championship 2026 live kijken (Maastricht, 16-18 okt). Tekst aangeleverd door de gebruiker,
geredigeerd. Gecontroleerd: historie (2018 White, 2022 Smith 8-7 Noppert, 2023 Chisnall 8-5 Humphries in Leeuwarden,
2024 Rock 8-4 Clayton, 2025 Clayton 8-6 Springer in Rosmalen), Swiss Darts Trophy 2026 (Clayton 8-4 Humphries, halve
finale 7-4 tegen Van Veen), terugkeer naar het MECC.
  python3 specials/dutch_darts_championship_2026.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Dutch Darts Championship 2026 Live Kijken: Gratis op Viaplay TV, Schema & Nederlanders"
SLUG = "dutch-darts-championship-2026-live-kijken"
SAMENVATTING = ("Dutch Darts Championship 2026 (16-18 oktober, MECC Maastricht) gratis kijken op Viaplay TV: speelschema, "
                "kanaalnummers, de Nederlanders en £230.000 prijzengeld.")
RUBRIEK_DARTS = "66b726271e317999159d5d44"
UNIBET = "https://b1.trickyrock.com/redirect.aspx?pid=86118747&bid=39312"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in koppen)
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}><thead><tr>{kop}</tr></thead><tbody>{body}</tbody></table>"


def lijst(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


content = f"""<p><strong>Het darts-seizoen gaat de eindsprint in, en het laatste European Tour-toernooi van 2026 wordt in Nederland gespeeld. Van vrijdag 16 tot en met zondag 18 oktober gooien de beste darters van de PDC in het MECC in Maastricht om de titel op het Dutch Darts Championship. Met Gian van Veen als tweede reekshoofd en ook Michael van Gerwen, Danny Noppert en Wessel Nijman in het deelnemersveld is er veel Nederlandse inbreng. Hieronder lees je waar je het toernooi gratis kijkt, hoe het speelschema eruitziet, wie er meedoen en wat er te verdienen is.</strong></p>
<h3><strong>Dutch Darts Championship 2026 in het kort</strong></h3>
{tabel(["", ""], [
    ("<strong>Toernooi</strong>", "Elten Safety Shoes Dutch Darts Championship 2026"),
    ("<strong>Datum</strong>", "Vrijdag 16 t/m zondag 18 oktober 2026"),
    ("<strong>Locatie</strong>", "MECC Maastricht"),
    ("<strong>Categorie</strong>", "PDC European Tour, het 15e en laatste toernooi van 2026"),
    ("<strong>Deelnemers</strong>", "48 darters"),
    ("<strong>Prijzengeld</strong>", "£230.000 (± €265.000)"),
    ("<strong>Winnaar</strong>", "£35.000 (± €40.250)"),
    ("<strong>Titelverdediger</strong>", "Jonny Clayton"),
    ("<strong>Live kijken</strong>", "Gratis op Viaplay TV, en via Viaplay en de livestream van Unibet"),
])}
<h3><strong>Waar kijk je het Dutch Darts Championship 2026?</strong></h3>
<h4>Gratis op Viaplay TV</h4>
<p>Alle sessies van het toernooi zijn gratis te zien op Viaplay TV. Dat is een open kanaal dat zonder extra kosten in het standaard tv-pakket zit van de meeste Nederlandse providers. Je hebt er geen Viaplay-abonnement voor nodig.</p>
{tabel(["Provider", "Kanaal Viaplay TV"], [
    ("Ziggo", "13"), ("KPN", "51"), ("Odido", "13"), ("DELTA", "22"), ("Youfone", "51"), ("hollandsnieuwe", "13"),
])}
<h4>Uitzendtijden op Viaplay TV</h4>
{tabel(["Dag", "Middag", "Avond"], [
    ("Vrijdag 16 oktober", "13:00 - 17:00 uur", "18:45 - 23:00 uur"),
    ("Zaterdag 17 oktober", "13:00 - 17:00 uur", "18:45 - 23:00 uur"),
    ("Zondag 18 oktober", "13:00 - 17:00 uur", "18:45 - 23:00 uur"),
])}
<h4>Viaplay-abonnement</h4>
<p>Wil je online kijken via de Viaplay-app of op viaplay.com, of op Viaplay TV+, dan heb je een abonnement op <a href="/zenders/viaplay">Viaplay</a> nodig. Dat kost €19,99 (Basis) of €21,99 (Standaard) per maand.</p>
<h4>Gratis livestream bij Unibet</h4>
<p>Zit je niet voor de tv? Bij Unibet kun je de wedstrijden ook online volgen. Zo werkt het:</p>
<ol><li>Maak een gratis account aan via de link hieronder.</li><li>Stort €10 om de livestream te activeren.</li><li>Kijk het Dutch Darts Championship live op je telefoon, tablet of laptop.</li><li>Haal na afloop je €10 er gewoon weer af.</li></ol>
<p>👉 <a href="{UNIBET}"><strong>Maak een gratis Unibet-account aan en kijk het Dutch Darts Championship live</strong></a></p>
<h3><strong>Speelschema Dutch Darts Championship 2026</strong></h3>
<p>De exacte volgorde van de wedstrijden maakt de PDC na de loting bekend. Het toernooi volgt het vaste schema van de European Tour:</p>
{tabel(["Dag", "Middagsessie (13:00 uur)", "Avondsessie (18:45 uur)"], [
    ("Vrijdag 16 oktober", "Eerste ronde", "Eerste ronde"),
    ("Zaterdag 17 oktober", "Tweede ronde, de 16 reekshoofden komen in actie", "Tweede ronde"),
    ("Zondag 18 oktober", "Derde ronde (laatste 16)", "Kwartfinales, halve finales en finale"),
])}
<h3><strong>Format: hoe werkt het toernooi?</strong></h3>
<p>Het Dutch Darts Championship heeft een deelnemersveld van 48 spelers:</p>
{lijst(["<strong>16 reekshoofden</strong> op basis van de PDC Order of Merit. Zij hebben een vrijstelling voor de eerste ronde en beginnen op zaterdag.",
        "<strong>32 andere spelers</strong>, die zich plaatsten via de Pro Tour Order of Merit, de Tour Card-kwalificaties, de Host Nation-kwalificatie en regionale kwalificaties. Zij spelen op vrijdag de eerste ronde."])}
<p>Aantal legs per ronde:</p>
{lijst(["Eerste ronde t/m kwartfinales: best of 11 legs (eerst naar 6)",
        "Halve finales: best of 13 legs (eerst naar 7)",
        "Finale: best of 15 legs (eerst naar 8)"])}
<p>Er wordt gespeeld volgens het principe van double out: elke leg moet worden uitgegooid op een dubbel of de bullseye.</p>"""

content2 = f"""<h3><strong>Nederlanders op het Dutch Darts Championship 2026</strong></h3>
<p>Nederland is in Maastricht met minimaal elf darters vertegenwoordigd. De grootste namen:</p>
{lijst(["<strong>Gian van Veen</strong>: tweede reekshoofd en de hoogst geplaatste Nederlander. Hij is een van de spelers van het jaar en haalde vorige week in Bazel nog de halve finale. Nu speelt hij voor eigen publiek.",
        "<strong>Michael van Gerwen</strong>: drievoudig wereldkampioen en de meest succesvolle speler in de geschiedenis van de European Tour. Het Dutch Darts Championship won hij nog nooit, en in Maastricht heeft hij de kans om dat recht te zetten.",
        "<strong>Danny Noppert</strong>: verloor in 2022 de finale van dit toernooi met 8-7 van Michael Smith en hoopt nu wel de titel te pakken.",
        "<strong>Wessel Nijman</strong>: een van de grootste Nederlandse talenten, die dit seizoen opnieuw stappen heeft gemaakt.",
        "<strong>Jermaine Wattimena</strong>: ervaren en altijd gevaarlijk.",
        "<strong>Kevin Doets</strong>: speelt ook mee in Maastricht."])}
<p>Het Nederlandse publiek in het MECC zorgt traditioneel voor een geweldige sfeer, en dat geeft de Nederlanders een extra steun in de rug.</p>
<h3><strong>Favorieten en deelnemersveld</strong></h3>
<p>De vier hoogste reekshoofden:</p>
<ol><li><strong>Luke Humphries</strong> (Engeland): voormalig wereldkampioen en de nummer één van de plaatsingslijst.</li><li><strong>Gian van Veen</strong> (Nederland).</li><li><strong>Gerwyn Price</strong> (Wales).</li><li><strong>Jonny Clayton</strong> (Wales): titelverdediger, die afgelopen zondag de <a href="/nieuws/swiss-darts-trophy-2026">Swiss Darts Trophy</a> in Bazel won. In de finale versloeg hij Humphries met 8-4, na een 7-4 in de halve finale tegen Van Veen.</li></ol>
<p>Andere bekende deelnemers: Michael van Gerwen, Danny Noppert, Stephen Bunting, Wessel Nijman, Ross Smith, Nathan Aspinall, Rob Cross en de Duitser Niko Springer, die vorig jaar de finale haalde.</p>
<p><strong>Onze favorieten:</strong> Jonny Clayton speelt met veel vertrouwen na zijn titel in Bazel, Luke Humphries is op papier de topfavoriet, en Gian van Veen kan met het thuispubliek achter zich ver komen. De odds per wedstrijd en meer tips vind je bij onze <a href="/wedtips">wedtips</a>.</p>
<h3><strong>Prijzengeld Dutch Darts Championship 2026</strong></h3>
<p>In 2026 is het prijzengeld van elk European Tour-toernooi verhoogd van £175.000 naar £230.000, omgerekend ongeveer €265.000. De verdeling (omgerekend tegen ongeveer £1 = €1,15):</p>
{tabel(["Ronde", "Prijzengeld"], [
    ("Winnaar", "£35.000 (± €40.250)"), ("Runner-up", "£15.000 (± €17.250)"), ("Halve finale", "£10.000 (± €11.500)"),
    ("Kwartfinale", "£8.000 (± €9.200)"), ("Laatste 16", "£5.000 (± €5.750)"),
    ("Laatste 32 (tweede ronde)", "£3.500 (± €4.025)"), ("Eerste ronde", "£2.000 (± €2.300)"),
])}
<p><em>Let op: een reekshoofd dat zijn eerste wedstrijd (in de tweede ronde) verliest, krijgt wel het prijzengeld, maar dat telt niet mee voor de Order of Merit.</em></p>
<h3><strong>Wat staat er nog meer op het spel?</strong></h3>
<p>Omdat dit het laatste European Tour-toernooi van het jaar is, is het van groot belang voor de European Tour Order of Merit. Die ranglijst bepaalt wie zich plaatst voor het Europees Kampioenschap in Dortmund en welke plaatsing de spelers daar krijgen. Acht Nederlanders zijn al zeker van deelname, maar voor andere spelers is Maastricht de laatste kans om zich te plaatsen of hun plaatsing te verbeteren.</p>"""

content3 = f"""<h3><strong>Geschiedenis van het Dutch Darts Championship</strong></h3>
<p>Het toernooi werd voor het eerst gespeeld in 2018, in het MECC in Maastricht, en Ian White won de eerste editie. Daarna verhuisde het toernooi onder meer naar Leeuwarden en Rosmalen. In 2026 keert het terug naar de hal waar het begon.</p>
{tabel(["Jaar", "Winnaar", "Finale"], [
    ("2025", "Jonny Clayton", "8-6 tegen Niko Springer (Rosmalen)"),
    ("2024", "Josh Rock", "8-4 tegen Jonny Clayton"),
    ("2023", "Dave Chisnall", "8-5 tegen Luke Humphries (Leeuwarden)"),
    ("2022", "Michael Smith", "8-7 tegen Danny Noppert"),
    ("2018", "Ian White", "tegen Ricky Evans (Maastricht)"),
])}
<p>Opvallend: nog nooit heeft een Nederlander het Dutch Darts Championship gewonnen. Danny Noppert kwam in 2022 het dichtst bij, met een nipte nederlaag in de finale.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wanneer is het Dutch Darts Championship 2026?</strong><br>Van vrijdag 16 tot en met zondag 18 oktober 2026.</p>
<p><strong>Waar wordt het toernooi gespeeld?</strong><br>In het MECC in Maastricht.</p>
<p><strong>Kan ik het Dutch Darts Championship gratis kijken?</strong><br>Ja, alle sessies zijn gratis te zien op Viaplay TV. Dit kanaal zit in het standaardpakket van onder meer Ziggo, KPN, Odido en DELTA.</p>
<p><strong>Op welk kanaal zit Viaplay TV?</strong><br>Kanaal 13 bij Ziggo, Odido en hollandsnieuwe, kanaal 51 bij KPN en Youfone, en kanaal 22 bij DELTA.</p>
<p><strong>Hoe laat beginnen de sessies?</strong><br>Elke dag om 13:00 uur (middagsessie) en 18:45 uur (avondsessie).</p>
<p><strong>Wie is de titelverdediger?</strong><br>Jonny Clayton. Hij won vorig jaar de finale met 8-6 van Niko Springer.</p>
<p><strong>Hoeveel verdient de winnaar?</strong><br>£35.000, ongeveer €40.250.</p>
<p><strong>Welke Nederlanders doen mee?</strong><br>Onder anderen Gian van Veen, Michael van Gerwen, Danny Noppert, Wessel Nijman, Jermaine Wattimena en Kevin Doets.</p>
<p><strong>Heeft er ooit een Nederlander gewonnen?</strong><br>Nee. Danny Noppert haalde in 2022 de finale, maar verloor met 8-7 van Michael Smith.</p>
<p><em>Gokken is alleen toegestaan voor personen van 18 jaar en ouder. Speel verantwoord. Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_DARTS,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting"); sys.exit()
    print("item:", WF.create_live(fd))
