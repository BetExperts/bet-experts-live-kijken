# -*- coding: utf-8 -*-
"""Los artikel: Swiss Darts Trophy 2026 (Basel, 9-11 okt). Historie gecontroleerd (2024 Schindler-Searle 8-7,
2025 Bunting-Woodhouse 8-3); schema/loting uit de aangeleverde info.
  python3 specials/swiss_darts_trophy_2026.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Swiss Darts Trophy 2026: speelschema, loting, deelnemersveld, voorbeschouwing, historie, format en voorspellingen"
SLUG = "swiss-darts-trophy-2026"
SAMENVATTING = ("Van 9 t/m 11 oktober draait de Swiss Darts Trophy in Basel. Speelschema, loting, de Nederlanders, het "
                "format, de historie en onze voorspelling.")
RUBRIEK_DARTS = "66b726271e317999159d5d44"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in koppen)
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}><thead><tr>{kop}</tr></thead><tbody>{body}</tbody></table>"


def sessie(rijen):
    return tabel(["Wedstrijd", "Ronde"], [(f"{a} – {b}", r) for a, b, r in rijen])


content = f"""<p><strong>De Swiss Darts Trophy 2026 wordt van vrijdag 9 tot en met zondag 11 oktober gespeeld in de St. Jakobshalle in Basel. 48 spelers strijden om een prijzenpot van £230.000. Luke Humphries is het eerste reekshoofd, Gian van Veen het tweede. Stephen Bunting verdedigt de titel. Luke Littler slaat het toernooi over.</strong></p>
<p>Basel is de voorlaatste stop van de European Tour. Een week later sluit het Dutch Darts Championship in Maastricht het reguliere Euro Tour-seizoen af. Dat maakt dit weekend extra belangrijk: in deze fase van het jaar telt elk pond mee in de kwalificatierankings voor de grote televisietoernooien, met het WK als belangrijkste doel. Hieronder vind je het speelschema, de loting, alle deelnemers, het format, de eerdere winnaars en onze voorspelling.</p>
<h3><strong>Het toernooi in het kort</strong></h3>
{tabel(["", ""], [
    ("<strong>Data</strong>", "Vrijdag 9 t/m zondag 11 oktober 2026"),
    ("<strong>Locatie</strong>", "St. Jakobshalle, Basel (Zwitserland)"),
    ("<strong>Prijzenpot</strong>", "£230.000"),
    ("<strong>Deelnemers</strong>", "48 spelers"),
    ("<strong>Titelverdediger</strong>", "Stephen Bunting"),
    ("<strong>Nummer 1 van de plaatsingslijst</strong>", "Luke Humphries"),
    ("<strong>Sessies</strong>", "Dagelijks vanaf 13:00 en 19:00 uur"),
])}
<h3><strong>Luke Littler ontbreekt</strong></h3>
<p>De grootste afwezige is Luke Littler. De Engelse wereldkampioen heeft besloten de laatste twee toernooien van de European Tour over te slaan. Hij komt dus niet in Basel en ook niet in Maastricht in actie. Daardoor staat Luke Humphries bovenaan de plaatsingslijst, met Gian van Veen als tweede reekshoofd.</p>
<h3><strong>Speelschema Swiss Darts Trophy 2026</strong></h3>
<p><strong>Vrijdag 9 oktober – middagsessie (13:00 uur), eerste ronde</strong></p>
{sessie([
    ("Niels Zonneveld", "Bradley Brooks", "R1"), ("William O'Connor", "Jani Haavisto", "R1"),
    ("Mensur Suljović", "György Jehirszki", "R1"), ("Sebastian Białecki", "Karel Sedláček", "R1"),
    ("Niko Springer", "Roman Wellinger", "R1"), ("Joe Cullen", "Tom Bissell", "R1"),
    ("Cameron Menzies", "Cristo Reyes", "R1"), ("Rob Cross", "Mario Vandenbogaerde", "R1"),
])}
<p><strong>Vrijdag 9 oktober – avondsessie (19:00 uur), eerste ronde</strong></p>
{sessie([
    ("Andrew Gilding", "Stefan Bellmont", "R1"), ("Jeffrey de Graaf", "Sietse Lap", "R1"),
    ("Dave Chisnall", "Alan Soutar", "R1"), ("Raymond van Barneveld", "Maik Kuivenhoven", "R1"),
    ("Dirk van Duijvenbode", "Bruno Stoeckli", "R1"), ("Michael Smith", "Rob Owen", "R1"),
    ("Damon Heta", "Alex Fehlmann", "R1"), ("Kevin Doets", "Nick Kenny", "R1"),
])}
<p><strong>Zaterdag 10 oktober – middagsessie (13:00 uur), tweede ronde</strong></p>
{sessie([
    ("Krzysztof Ratajski", "Gilding/Bellmont", "R2"), ("Wessel Nijman", "Białecki/Sedláček", "R2"),
    ("Luke Woodhouse", "Cross/Vandenbogaerde", "R2"), ("Martin Schindler", "Cullen/Bissell", "R2"),
    ("Ryan Searle", "Menzies/Reyes", "R2"), ("Ross Smith", "O'Connor/Haavisto", "R2"),
    ("Chris Dobey", "Zonneveld/Brooks", "R2"), ("Jermaine Wattimena", "M. Smith/Owen", "R2"),
])}
<p><strong>Zaterdag 10 oktober – avondsessie (19:00 uur), tweede ronde</strong></p>
{sessie([
    ("Josh Rock", "Chisnall/Soutar", "R2"), ("Stephen Bunting", "De Graaf/Lap", "R2"),
    ("James Wade", "Van Duijvenbode/Stoeckli", "R2"), ("Jonny Clayton", "Van Barneveld/Kuivenhoven", "R2"),
    ("Michael van Gerwen", "Suljović/Jehirszki", "R2"), ("Luke Humphries", "Doets/Kenny", "R2"),
    ("Gian van Veen", "Springer/Wellinger", "R2"), ("Danny Noppert", "Heta/Fehlmann", "R2"),
])}
<p><strong>Zondag 11 oktober</strong>: in de middagsessie (13:00 uur) worden de acht wedstrijden van de laatste zestien gespeeld. In de avondsessie (19:00 uur) volgen de kwartfinales, de halve finales en de finale.</p>"""

content2 = f"""<h3><strong>Loting: de reekshoofden en hun mogelijke tegenstanders</strong></h3>
<p>De zestien geplaatste spelers stromen pas in de tweede ronde in. Ze treffen daar de winnaar van een eerste-ronde-duel. Zo ziet de loting eruit, in de volgorde van het schema:</p>
{tabel(["Reekshoofd", "Tegen winnaar van"], [
    ("(6) Josh Rock", "Dave Chisnall / Alan Soutar"),
    ("(11) Wessel Nijman", "Sebastian Białecki / Karel Sedláček"),
    ("(3) Jonny Clayton", "Raymond van Barneveld / Maik Kuivenhoven"),
    ("(14) Luke Woodhouse", "Rob Cross / Mario Vandenbogaerde"),
    ("(7) Stephen Bunting", "Jeffrey de Graaf / Sietse Lap"),
    ("(10) Chris Dobey", "Niels Zonneveld / Bradley Brooks"),
    ("(2) Gian van Veen", "Niko Springer / Roman Wellinger"),
    ("(15) Martin Schindler", "Joe Cullen / Tom Bissell"),
    ("(5) Michael van Gerwen", "Mensur Suljović / György Jehirszki"),
    ("(12) Ross Smith", "William O'Connor / Jani Haavisto"),
    ("(4) James Wade", "Dirk van Duijvenbode / Bruno Stoeckli"),
    ("(13) Jermaine Wattimena", "Michael Smith / Rob Owen"),
    ("(8) Danny Noppert", "Damon Heta / Alex Fehlmann"),
    ("(9) Ryan Searle", "Cameron Menzies / Cristo Reyes"),
    ("(1) Luke Humphries", "Kevin Doets / Nick Kenny"),
    ("(16) Krzysztof Ratajski", "Andrew Gilding / Stefan Bellmont"),
])}
<h3><strong>Voorbeschouwing: veel Nederlands op de openingsdag</strong></h3>
<p>Voor <strong>Raymond van Barneveld</strong> staat er vrijdagavond veel op het spel. Na een sterk Pro Tour-tweeluik vorige maand doet de vijfvoudig wereldkampioen weer mee in de race om een WK-ticket. Een zege op landgenoot <strong>Maik Kuivenhoven</strong> levert belangrijk prijzengeld op en een tweede ronde tegen Jonny Clayton.</p>
<p>De Nederlandse inbreng begint al in de eerste partij van het toernooi, waarin <strong>Niels Zonneveld</strong> het opneemt tegen Bradley Brooks. 's Avonds staan Jeffrey de Graaf en <strong>Sietse Lap</strong> tegenover elkaar, en <strong>Dirk van Duijvenbode</strong> speelt tegen de Zwitserse qualifier Bruno Stoeckli. <strong>Kevin Doets</strong> sluit de vrijdag af tegen Nick Kenny, met een mogelijke tweede ronde tegen Luke Humphries als beloning.</p>
<p>Zaterdag komen de geplaatste Nederlanders in actie: <strong>Gian van Veen</strong>, <strong>Michael van Gerwen</strong>, <strong>Danny Noppert</strong>, <strong>Wessel Nijman</strong> en <strong>Jermaine Wattimena</strong>. Mario Vandenbogaerde is de enige Belg in Basel. Hij begint vrijdagmiddag meteen tegen oud-wereldkampioen Rob Cross. Andere bekende namen op de eerste dag zijn William O'Connor, Mensur Suljović, Joe Cullen, Cameron Menzies, Michael Smith en Damon Heta.</p>
<h3><strong>Deelnemersveld</strong></h3>
{tabel(["Groep", "Spelers"], [
    ("<strong>Reekshoofden (1-16)</strong>", "Luke Humphries, Gian van Veen, Jonny Clayton, James Wade, Michael van Gerwen, Josh Rock, Stephen Bunting, Danny Noppert, Ryan Searle, Chris Dobey, Wessel Nijman, Ross Smith, Jermaine Wattimena, Luke Woodhouse, Martin Schindler, Krzysztof Ratajski"),
    ("<strong>Via de Pro Tour Order of Merit</strong>", "Kevin Doets, Andrew Gilding, Rob Cross, William O'Connor, Niko Springer, Niels Zonneveld, Dirk van Duijvenbode, Joe Cullen, Cameron Menzies, Damon Heta, Sebastian Białecki, Dave Chisnall"),
    ("<strong>Tour Card-kwalificatie</strong>", "Bradley Brooks, Mensur Suljović, Tom Bissell, Jeffrey de Graaf, Michael Smith, Mario Vandenbogaerde, Raymond van Barneveld, Sietse Lap, Maik Kuivenhoven, Cristo Reyes"),
    ("<strong>Reservelijst</strong>", "Karel Sedláček, Alan Soutar, Rob Owen, Nick Kenny"),
    ("<strong>Zwitserse qualifiers</strong>", "Stefan Bellmont, Roman Wellinger, Bruno Stoeckli, Alex Fehlmann"),
    ("<strong>Nordic & Baltic qualifier</strong>", "Jani Haavisto"),
    ("<strong>Oost-Europese qualifier</strong>", "György Jehirszki"),
])}"""

content3 = f"""<h3><strong>Format: zo wordt er gespeeld</strong></h3>
<p>Net als bij de andere toernooien van de European Tour wordt er in legs gespeeld. Tot en met de kwartfinales wint wie als eerste zes legs pakt; in de laatste twee rondes worden de wedstrijden langer.</p>
{tabel(["Ronde", "Format", "Nodig om te winnen"], [
    ("Eerste ronde", "Best of 11 legs", "6 legs"),
    ("Tweede ronde", "Best of 11 legs", "6 legs"),
    ("Laatste 16", "Best of 11 legs", "6 legs"),
    ("Kwartfinales", "Best of 11 legs", "6 legs"),
    ("Halve finales", "Best of 13 legs", "7 legs"),
    ("Finale", "Best of 15 legs", "8 legs"),
])}
<h3><strong>Historie: eerdere winnaars</strong></h3>
<p>De Swiss Darts Trophy is een jong toernooi: het werd in 2024 voor het eerst in Basel gespeeld.</p>
{tabel(["Jaar", "Winnaar", "Uitslag", "Finalist"], [
    ("2025", "Stephen Bunting", "8-3", "Luke Woodhouse"),
    ("2024", "Martin Schindler", "8-7", "Ryan Searle"),
])}
<p>De eerste editie leverde direct een klassieker op. Martin Schindler stond in de finale met 7-4 achter, maar Ryan Searle miste zeven matchdarts en de Duitser won alsnog met 8-7. Een jaar later was Stephen Bunting veel te sterk voor Luke Woodhouse. Met een gemiddelde van bijna 104 won hij de finale met 8-3. Alle vier de finalisten van de vorige twee edities zijn dit jaar weer van de partij.</p>
<h3><strong>Voorspelling Swiss Darts Trophy 2026</strong></h3>
<p>Zonder Littler is <strong>Luke Humphries</strong> de logische favoriet. Als nummer één van de plaatsingslijst heeft hij een loting die hem tot de laatste zestien weinig problemen zou moeten geven. <strong>Gian van Veen</strong> is als tweede reekshoofd de grootste Nederlandse kanshebber. Hij zit in de andere helft van het schema, waardoor een finale tegen Humphries mogelijk is.</p>
<p>Houd ook <strong>Stephen Bunting</strong> in de gaten. De titelverdediger voelt zich duidelijk thuis in de St. Jakobshalle en won hier vorig jaar overtuigend. Een andere naam om op te letten is <strong>Martin Schindler</strong>, de winnaar van 2024, die als vijftiende reekshoofd een flinke outsider is.</p>
<p><strong>Onze voorspelling:</strong> Luke Humphries wint de Swiss Darts Trophy, na een finale tegen Gian van Veen. Als outsider kiezen we Stephen Bunting. In de eerste ronde verwachten we dat Van Barneveld zijn duel met Kuivenhoven wint, zodat het Nederlandse publiek zaterdag een clash tussen Barney en Jonny Clayton krijgt. De odds per wedstrijd en meer wedtips vind je bij onze <a href="/wedtips">wedtips</a>.</p>
<h3><strong>Waar kun je de Swiss Darts Trophy kijken?</strong></h3>
<p>In Nederland worden de PDC-toernooien uitgezonden door <a href="/zenders/viaplay">Viaplay</a>. Via de app volg je alle sessies live, en de grootste toernooien zijn ook te zien op de tv-zender Viaplay TV+. De sessies beginnen elke dag om 13:00 en 19:00 uur.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wanneer is de Swiss Darts Trophy 2026?</strong><br>Van vrijdag 9 tot en met zondag 11 oktober 2026, met elke dag een middag- en een avondsessie.</p>
<p><strong>Waar wordt de Swiss Darts Trophy gespeeld?</strong><br>In de St. Jakobshalle in Basel, Zwitserland.</p>
<p><strong>Wie is de titelverdediger?</strong><br>Stephen Bunting. Hij won in 2025 de finale met 8-3 van Luke Woodhouse.</p>
<p><strong>Hoeveel prijzengeld is er te verdienen?</strong><br>De totale prijzenpot is £230.000.</p>
<p><strong>Speelt Luke Littler mee?</strong><br>Nee. Littler slaat de laatste twee Euro Tour-toernooien over, ook het Dutch Darts Championship in Maastricht.</p>
<p><strong>Welke Nederlanders doen mee?</strong><br>Onder anderen Gian van Veen, Michael van Gerwen, Danny Noppert, Wessel Nijman, Jermaine Wattimena, Raymond van Barneveld, Dirk van Duijvenbode, Kevin Doets, Niels Zonneveld, Sietse Lap en Maik Kuivenhoven.</p>
<p><em>Gokken is alleen toegestaan voor personen van 18 jaar en ouder. Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_DARTS,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting"); sys.exit()
    print("item:", WF.create_live(fd))
