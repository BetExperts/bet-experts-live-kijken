# -*- coding: utf-8 -*-
"""Los artikel: RB Leipzig – PSV kijken zonder Ziggo Sport (Ziggo Sport Free), CL 13 okt 2026 21:00.
Aanleveringstekst van de gebruiker volledig herschreven. Gecontroleerd op ziggo.nl/uefa: gratis voor Europese
duels van Nederlandse clubs + finales; binnen NL geen account nodig, in de EU wel een gratis account.
Niet bevestigd en daarom weggelaten: maximaal aantal apparaten.
  python3 specials/rb_leipzig_psv_zonder_ziggo.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "RB Leipzig – PSV kijken zonder Ziggo Sport: zo zie je het gratis (13 oktober)"
SLUG = "rb-leipzig-psv-kijken-zonder-ziggo-sport"
SAMENVATTING = ("Geen Ziggo Sport? RB Leipzig – PSV kijk je dinsdag om 21:00 uur gratis via Ziggo Sport Free in de Ziggo GO-app "
                "of op ziggogo.tv. Zo werkt het.")
RUBRIEK_ALGEMEEN = "6502b65d49bc032ba533e7a2"
CL = "65de4adac046f4488dfdebc2"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in koppen)
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}><thead><tr>{kop}</tr></thead><tbody>{body}</tbody></table>"


def lijst(items, tag="ul"):
    return f"<{tag}>" + "".join(f"<li>{i}</li>" for i in items) + f"</{tag}>"


content = f"""<p><strong>Geen Ziggo Sport in je tv-pakket? Geen probleem. RB Leipzig – PSV is vanavond gratis te zien via Ziggo Sport Free, omdat Europese wedstrijden van Nederlandse clubs voor iedereen openstaan. Je hebt geen Ziggo-abonnement en geen Ziggo Sport Totaal nodig: in Nederland start je de stream gewoon in de Ziggo GO-app of op ziggogo.tv. Hieronder lees je precies hoe dat werkt, op welk apparaat je het beste kijkt en wat je moet doen als je in het buitenland bent.</strong></p>
<h3><strong>RB Leipzig – PSV in het kort</strong></h3>
{tabel(["", ""], [
    ("<strong>Wedstrijd</strong>", "RB Leipzig – PSV"),
    ("<strong>Competitie</strong>", "UEFA Champions League, speelronde 2"),
    ("<strong>Datum en aftrap</strong>", "Dinsdag 13 oktober 2026, 21:00 uur"),
    ("<strong>Op tv</strong>", "Ziggo Sport 1 (voor Ziggo-klanten)"),
    ("<strong>Gratis zonder Ziggo</strong>", "Ziggo Sport Free via de Ziggo GO-app of ziggogo.tv"),
    ("<strong>Account nodig?</strong>", "Niet in Nederland; wel een gratis account als je in een ander EU-land bent"),
])}
<h3><strong>Waarom is RB Leipzig – PSV gratis te zien?</strong></h3>
<p>Ziggo heeft de rechten op het Europese clubvoetbal in Nederland en biedt een deel daarvan gratis aan onder de naam <strong>Ziggo Sport Free</strong>. Daaronder vallen de Europese wedstrijden van Nederlandse clubs en de finales van de Champions League, de Europa League en de Conference League. Omdat PSV een Nederlandse club is, hoort de uitwedstrijd in Leipzig daar gewoon bij.</p>
<p>Voor Ziggo-klanten staat de wedstrijd ook op <a href="/zenders/ziggo-sport">Ziggo Sport 1</a>, het open kanaal in hun tv-pakket. Heb je een ander tv-abonnement, bijvoorbeeld bij KPN of Odido, of kijk je helemaal geen lineaire tv? Dan gebruik je de gratis online stream.</p>
<h3><strong>Zo kijk je RB Leipzig – PSV gratis in Nederland</strong></h3>
<p>In Nederland hoef je geen account aan te maken. Je opent de stream en je kijkt. Zo werkt het:</p>
{lijst(["<strong>Kies je apparaat.</strong> Op een telefoon, tablet of geschikte smart-tv installeer je de Ziggo GO-app. Op een laptop of computer ga je in je browser naar ziggogo.tv.",
        "<strong>Open Ziggo GO</strong> ruim voor de aftrap, zodat je niet op het laatste moment nog iets hoeft te installeren of bij te werken.",
        "<strong>Zoek de wedstrijd</strong> op naam (RB Leipzig – PSV) of tussen de live uitzendingen van de Champions League-avond.",
        "<strong>Start de live stream</strong> zodra die beschikbaar is. De uitzending begint ruim voor de aftrap.",
        "<strong>Kijk mee vanaf 21:00 uur</strong>, zonder Ziggo Sport Totaal en zonder tv-abonnement bij Ziggo."], "ol")}
<p><em>Tip: een stabiele wifiverbinding voorkomt dat het beeld blijft hangen op het moment dat PSV in de aanval gaat.</em></p>
<h3><strong>Op welk apparaat kijk je het makkelijkst?</strong></h3>
{tabel(["Apparaat", "Zo kijk je"], [
    ("Smartphone of tablet", "Download de Ziggo GO-app en open de live stream"),
    ("Laptop of computer", "Ga in je browser naar ziggogo.tv"),
    ("Smart-tv", "Installeer de Ziggo GO-app, als jouw tv die ondersteunt"),
    ("Tv met Chromecast of AirPlay", "Start Ziggo GO op je telefoon of tablet en stuur het beeld naar de tv"),
    ("Tv met HDMI-aansluiting", "Sluit je laptop met een HDMI-kabel aan en open ziggogo.tv"),
])}
<h3><strong>Op de grote tv kijken zonder Ziggo Sport-zender</strong></h3>
<p>Je hoeft dus niet naar een tv-kanaal te zappen om de wedstrijd op groot scherm te zien. Drie manieren:</p>
{lijst(["<strong>Smart-tv-app:</strong> heeft je televisie de Ziggo GO-app, dan start je de gratis stream direct op de tv.",
        "<strong>Casten:</strong> open Ziggo GO op je telefoon of tablet en stuur het beeld via Chromecast of AirPlay naar de televisie.",
        "<strong>HDMI-kabel:</strong> sluit een laptop aan op de tv en open ziggogo.tv in de browser."])}
<p>Test het beeld en geluid even voor 21:00 uur. Dan zit je bij de aftrap niet nog met instellingen te puzzelen.</p>"""

content2 = f"""<h3><strong>Onderweg kijken</strong></h3>
<p>Ben je op het moment van de wedstrijd niet thuis, maar wel in Nederland? Open dan Ziggo GO op je telefoon of tablet, via wifi of mobiele data. Kijk je met een beperkte databundel, zet dan de beeldkwaliteit wat lager. Zo voorkom je haperend beeld en een onverwacht hoog dataverbruik. Een volledige wedstrijd in hoge kwaliteit kan snel meerdere gigabytes kosten.</p>
<h3><strong>In het buitenland? Zo kijk je binnen de EU</strong></h3>
<p>Ben je tijdelijk in een ander land van de Europese Unie, bijvoorbeeld op vakantie of voor werk? Dan kun je ook kijken, maar met één extra stap: je hebt dan wel een <strong>gratis Ziggo Sport Free-account</strong> nodig.</p>
{lijst(["Maak het account aan op de website van Ziggo, het liefst al vóór je vertrek of in elk geval ruim voor de aftrap.",
        "Ziggo kan je vragen om te bevestigen dat je in Nederland woont.",
        "Log daarna in op Ziggo GO en start de stream van RB Leipzig – PSV.",
        "Sta locatietoegang toe als je apparaat daarom vraagt."], "ol")}
<p>Gebruik geen VPN om een regiobeperking te omzeilen; dat is in strijd met de voorwaarden van de dienst. Buiten de Europese Unie kan de beschikbaarheid anders zijn.</p>
<h3><strong>Wat krijg je wel en niet met Ziggo Sport Free?</strong></h3>
{tabel(["Wel gratis", "Niet gratis (Ziggo Sport Totaal nodig)"], [
    ("Europese wedstrijden van Nederlandse clubs, zoals RB Leipzig – PSV", "Champions League-wedstrijden zonder Nederlandse club"),
    ("De finales van de Champions League, Europa League en Conference League", "Achtste finales, kwartfinales en halve finales zonder Nederlandse club"),
    ("Live kijken via Ziggo GO en ziggogo.tv", "Het volledige aanbod met voor- en nabeschouwingen en extra kanalen"),
])}
<p>Wil je élke Champions League-wedstrijd kunnen zien, dan heb je Ziggo Sport Totaal nodig, te boeken bij Ziggo, KPN en Odido. Wil je alleen PSV volgen, dan is Ziggo Sport Free alles wat je nodig hebt.</p>
<h3><strong>Meer over RB Leipzig – PSV</strong></h3>
<p>Benieuwd naar de vorm, de verwachte opstellingen en onze wedtips? Lees dan onze <a href="/nieuws/wedtips-rb-leipzig-psv-eindhoven-voorspelling-odds-opstellingen">voorspelling voor RB Leipzig – PSV</a>. Alle kijkopties voor deze wedstrijd, inclusief de tv-zender, staan in <a href="/nieuws/rb-leipzig-psv-live-gratis-kijken-13-10-2026">RB Leipzig – PSV live kijken</a>. Het complete overzicht van deze speelronde vind je in <a href="/nieuws/champions-league-speelronde-2-op-tv-13-oktober-2026">Champions League speelronde 2 op tv</a>.</p>"""

content3 = """<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Waar kan ik RB Leipzig – PSV gratis kijken?</strong><br>In Nederland via Ziggo Sport Free, in de Ziggo GO-app of op ziggogo.tv. Omdat PSV een Nederlandse club is, valt de wedstrijd binnen het gratis aanbod.</p>
<p><strong>Heb ik Ziggo Sport Totaal nodig?</strong><br>Nee. Voor de Europese wedstrijden van Nederlandse clubs is Ziggo Sport Free gratis. Ziggo Sport Totaal heb je alleen nodig voor het volledige aanbod.</p>
<p><strong>Moet ik een account aanmaken?</strong><br>In Nederland niet: je opent de stream zonder account. Ben je in een ander EU-land, dan maak je eerst een gratis Ziggo Sport Free-account aan.</p>
<p><strong>Hoe laat begint RB Leipzig – PSV?</strong><br>Dinsdag 13 oktober om 21:00 uur. De uitzending begint ruim voor de aftrap.</p>
<p><strong>Kan ik op mijn tv kijken zonder Ziggo Sport-zender?</strong><br>Ja. Gebruik de Ziggo GO-app op een geschikte smart-tv, cast de stream met Chromecast of AirPlay, of sluit een laptop met een HDMI-kabel aan.</p>
<p><strong>Kan ik kijken als ik op vakantie ben?</strong><br>Binnen de Europese Unie wel, met een gratis Ziggo Sport Free-account. Buiten de EU kan de beschikbaarheid anders zijn.</p>
<p><em>De beschikbaarheid van de stream, de ondersteunde apparaten en de voorwaarden kunnen wijzigen. Controleer kort voor de wedstrijd de actuele informatie in Ziggo GO of op ziggo.nl. Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_ALGEMEEN, "competitie": CL,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting"); sys.exit()
    print("item:", WF.create_live(fd))
