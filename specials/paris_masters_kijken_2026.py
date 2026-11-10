# -*- coding: utf-8 -*-
"""Bestaand artikel bijwerken naar 2026: Paris Masters live (gratis) kijken.
UPDATE 10-11-2026 (minimaal): toernooi voorbij; intro-slotzin, update-alinea (winnaar Alcaraz + link hub) en 2 FAQ's
omgezet naar verleden tijd. Feiten: paris_masters_uitslag_feiten_2026.md. Rest (uitzendschema) bewust ongewijzigd. Item 69008300b87d5da2e4ab33a8, slug blijft
(GSC 2025: 'tennis parijs live' pos 7,6, 'tennis parijs op tv' pos 6,8, 'atp parijs', 'atp 1000 parijs').
Back-up: backups/nieuws-atp-parijs-kijken-2026-11-02.json. Op verzoek van Jasper (2-11-2026): 'gratis kijken kan gewoon bij
TOTO nog steeds'. TOTO = gratis account, geen storting (lk_config PROVIDERS['toto'], deposit False, Jasper 8-10);
link /go/toto-live-kijken met de '👉 Klik hier'-regel (lk-cta.js zet de CTA-afbeelding erboven, be-static).
Feiten: paris_masters_feiten_2026.md (Ziggo-uitzendschema per dag, kanaalnummers, ATP-starttijden, Play Sports BE).
  python3 specials/paris_masters_kijken_2026.py   (dry run)"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

ITEM_ID = "69008300b87d5da2e4ab33a8"
SLUG = "atp-1000-parijs-live-gratis-kijken-in-nederland-tv-gids-ziggo-sport-en-gratis-opties-griekspoor-alcaraz-sinner-en-meer-in-actie"
RUBRIEK = "665715dbf1f3cbdf7f874d79"   # Tennis
TITEL = "Paris Masters 2026 live kijken: gratis via TOTO en op Ziggo Sport"
SAMENVATTING = ("Paris Masters 2026 live kijken: gratis via de livestream van TOTO of op tv bij Ziggo Sport. Met zenders, "
                "tijden per dag en de finale.")
TOTO = "https://www.bet-experts.nl/go/toto-live-kijken"

OG_LOGO = "paris-masters-logo.png"
OG_EYEBROW = "Tennis · 2 t/m 8 november"
OG_KOP = "Paris Masters<br><em>live kijken</em>"
OG_TEGELS = [("Gratis stream", "TOTO"), ("Op tv", "Ziggo Sport")]
OG_KOPJE = "Live op tv (Nederlandse tijd)"
OG_RECHTS = "Finale zondag 8 november"
OG_RIJEN = [("Ma 2 – do 5", "Ziggo Sport 1 en 4", "vanaf 11:00"),
            ("Vr 6 nov", "Kwartfinales · Ziggo Sport 4", "vanaf 14:00"),
            ("Za 7 nov", "Halve finales · Ziggo Sport 4", "vanaf 14:30"),
            ("Zo 8 nov", "Finale · Ziggo Sport 4", "15:00")]

L = {"hub": '<a href="/nieuws/paris-masters-2026-schema-tijden-tv-deelnemers-prijzengeld">Paris Masters 2026: schema, deelnemers en prijzengeld</a>',
     "toto": '<a href="/zenders/toto">de livestreams van TOTO</a>',
     "ziggo": '<a href="/zenders/ziggo-sport">Ziggo Sport</a>',
     "tips": '<a href="/tennis-voorspellingen-vandaag">tennisvoorspellingen van vandaag</a>',
     "kijken": '<a href="/live-kijken">live kijken</a>',
     "bonus": '<a href="/bookmakers/toto">TOTO</a>'}

ZIGGO = [  # (dag, ronde, Ziggo Sport-uitzending)
    ("Ma 2 nov", "1e ronde", "Ziggo Sport 1: 11:00-19:00 · Ziggo Sport 4: 11:00-23:00"),
    ("Di 3 nov", "1e en 2e ronde", "Ziggo Sport 1: 11:00-15:00 · Ziggo Sport 4: 11:00-20:55"),
    ("Wo 4 nov", "2e ronde", "Ziggo Sport 1: 11:00-15:00 · Ziggo Sport 4: 11:00-20:55"),
    ("Do 5 nov", "Laatste 16", "Ziggo Sport 1: 11:00-15:00 · Ziggo Sport 4: 11:00-18:40"),
    ("Vr 6 nov", "Kwartfinales", "Ziggo Sport 4: 14:00-18:00 en 19:00-23:00"),
    ("Za 7 nov", "Halve finales", "Ziggo Sport 4: 14:30-16:30 en 17:00-19:00"),
    ("Zo 8 nov", "Finale", "Ziggo Sport 4: 15:00-17:30"),
]

content = f"""<p><strong>De Paris Masters 2026 kun je in Nederland gratis live kijken via de livestream van TOTO: je hebt alleen een gratis account nodig, een storting is niet nodig. Op tv is het toernooi te zien op Ziggo Sport, met Ziggo Sport 1 (in het basispakket van Ziggo) en Ziggo Sport 4 (met Ziggo Sport Totaal). Het toernooi liep van maandag 2 tot en met zondag 8 november; Carlos Alcaraz won de finale.</strong></p>
<p><strong>Update dinsdag 10 november:</strong> de Paris Masters 2026 is voorbij. Carlos Alcaraz won zondag de finale van Ben Shelton met 7-6(5) 7-5. Botic van de Zandschulp en Zizou Bergs verloren in de eerste ronde. Alle uitslagen en het prijzengeld lees je in {L['hub']}. Het uitzendschema hieronder laat zien hoe het toernooi te zien was.</p>
<h3><strong>Paris Masters 2026 gratis kijken via TOTO</strong></h3>
<p>Bij TOTO kun je de partijen van de Paris Masters live volgen in de livestream, in HD op je telefoon, tablet of laptop. Je hoeft geen tv-abonnement te hebben en ook geen geld te storten: een gratis account is genoeg. Dat maakt TOTO de makkelijkste manier om in Nederland gratis naar het tennis in Parijs te kijken, ook als je geen Ziggo hebt.</p>
<p><strong>Zo werkt gratis kijken via TOTO:</strong></p>
<ol><li>Maak een gratis account aan bij TOTO via de link hieronder</li><li>Log in op je account</li><li>Ga naar Live en kies tennis</li><li>Kies de partij die je wilt zien en zet de livestream aan</li></ol>
<p>Je moet 18 jaar of ouder zijn om een account te openen. In het live-gedeelte zie je per partij of er een stream beschikbaar is. Wil je ook meewedden, dan kun je dat in dezelfde app doen, maar voor het kijken is dat niet nodig. Lees meer over {L['toto']}.</p>
<p><a href="{TOTO}"><strong>👉 Klik hier: maak je gratis TOTO-account aan en kijk de Paris Masters live</strong></a></p>
<h3><strong>Alle manieren om de Paris Masters 2026 te kijken</strong></h3>
{tabel(["Optie", "Wat zie je", "Kosten"], [
    ("<strong>TOTO livestream</strong>", "Partijen live in de app of op de site", "Gratis account, geen storting"),
    ("<strong>Ziggo Sport 1</strong>", "Een deel van de partijen, vooral overdag van maandag tot en met donderdag", "In het basispakket van Ziggo"),
    ("<strong>Ziggo Sport 4</strong>", "De meeste partijen, ook de kwartfinales, halve finales en finale", "Met Ziggo Sport Totaal"),
    ("<strong>Ziggo Sport-app</strong>", "Online meekijken op telefoon, tablet of laptop", "Met Ziggo Sport Totaal"),
    ("<strong>Play Sports (België)</strong>", "ATP Masters 1000 live via Telenet", "Betaald"),
])}"""

content2 = f"""<h3><strong>Paris Masters 2026 op tv: Ziggo Sport-schema per dag</strong></h3>
<p>In Nederland heeft {L['ziggo']} de tv-rechten op de ATP Masters 1000-toernooien. Ziggo zendt vooral de beste partijen en de partijen met Nederlanders uit. Dit is het uitzendschema in Nederlandse tijd:</p>
{tabel(["Dag", "Ronde", "Live op tv"], [(f"<strong>{d}</strong>", r, z) for d, r, z in ZIGGO])}
<p><em>Uitzendtijden volgens Ziggo Sport; wijzigingen zijn mogelijk, bijvoorbeeld als een partij uitloopt. De partijen in Parijs beginnen van maandag tot en met donderdag om 11:00 uur, de kwartfinales op vrijdag om 12:00 uur en de halve finales op zaterdag om 11:30 uur.</em></p>
<p><strong>Op welk kanaal vind je Ziggo Sport?</strong> Ziggo Sport 1 staat bij Ziggo op kanaal 14, bij KPN op 233 en bij Odido op 160. Ziggo Sport 4 vind je bij Ziggo op 404, bij KPN op 236 en bij Odido op 163. Ziggo Sport Totaal kun je ook afnemen als je tv bij een andere aanbieder hebt, zoals KPN of Odido.</p>
<h3><strong>Hoe laat spelen de Nederlanders en Belgen?</strong></h3>
{tabel(["Speler", "Partij", "Wanneer"], [
    ("<strong>Botic van de Zandschulp</strong> 🇳🇱", "1e ronde tegen Ugo Humbert", "Ma 2 nov, centercourt, niet vóór 20:30"),
    ("<strong>David Pel</strong> 🇳🇱", "Dubbelspel met Sadio Doumbia, tegen Nys/Roger-Vasselin", "Zie het dagschema"),
    ("<strong>Zizou Bergs</strong> 🇧🇪", "1e ronde tegen Ignacio Buse", "Ma 2 nov, Court 2, 11:00"),
    ("<strong>Alexander Blockx</strong> 🇧🇪", "1e ronde tegen Daniel Mérida", "Ma 2 nov, Court 2, derde partij"),
])}
<p>Tallon Griekspoor speelt niet: hij verloor in de kwalificatie van Benjamin Bonzi. Wint Van de Zandschulp van Humbert, dan wacht in de tweede ronde Brandon Nakashima of Matteo Berrettini. Partijen met Nederlanders zendt Ziggo Sport meestal uit; via TOTO kun je ze ook volgen als ze niet op tv zijn.</p>
<h3><strong>Kijken in België</strong></h3>
<p>In België zijn de ATP Masters 1000-toernooien live te zien op Play Sports van Telenet, en in België en Luxemburg ook op BeTV. Een gratis uitzending op de Belgische open zenders is er niet.</p>"""

content3 = f"""<h3><strong>Wat moet je weten over de Paris Masters 2026?</strong></h3>
<p>De Rolex Paris Masters is het laatste ATP Masters 1000-toernooi van het seizoen en wordt sinds 2025 niet meer in Bercy gespeeld, maar in de Paris La Défense Arena in Nanterre (nu Plenitude Arena). Titelverdediger Jannik Sinner ontbreekt met een knieblessure; Alexander Zverev en Carlos Alcaraz zijn als eerste en tweede geplaatst, en recordwinnaar Novak Djokovic (zeven titels) doet ook mee. Voor veel spelers gaat het ook om een plek in de ATP Finals in Turijn. De winnaar krijgt €974.370 en 1000 rankingpunten. Het complete speelschema, alle deelnemers, het prijzengeld en de winnaars lees je in {L['hub']}. Wil je meewedden? Bekijk onze {L['tips']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Kun je de Paris Masters 2026 gratis kijken?</strong><br>Ja. Via de livestream van TOTO kijk je met een gratis account, zonder storting. Ben je Ziggo-klant, dan kijk je ook zonder extra kosten mee via Ziggo Sport 1.</p>
<p><strong>Op welke zender is de Paris Masters 2026?</strong><br>Op Ziggo Sport: Ziggo Sport 1 en Ziggo Sport 4. De kwartfinales, halve finales en finale zijn op Ziggo Sport 4.</p>
<p><strong>Wie won de finale van de Paris Masters 2026?</strong><br>Carlos Alcaraz. Hij versloeg Ben Shelton op zondag 8 november met 7-6(5) 7-5. De finale begon om 15:00 uur en was live op Ziggo Sport 4.</p>
<p><strong>Kan ik de Paris Masters kijken zonder Ziggo?</strong><br>Ja. Met een gratis account bij TOTO kijk je via de livestream. Je kunt ook Ziggo Sport Totaal afnemen bij een andere tv-aanbieder, zoals KPN of Odido.</p>
<p><strong>Hoe deed Botic van de Zandschulp het?</strong><br>Hij verloor op maandag 2 november in de eerste ronde van Ugo Humbert: 7-6(5) 6-7(9) 6-3.</p>
<p><strong>Waar kijk je de Paris Masters in België?</strong><br>Op Play Sports van Telenet en op BeTV.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    alles = content + content2 + content3
    tekst = re.sub(r"<[^>]+>", " ", alles)
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", len(tekst.split()), "woorden")
    assert len(TITEL) <= 70 and 120 <= len(SAMENVATTING) <= 160
    assert "<h2" not in alles and "<h4" not in alles and "betcity" not in alles.lower() and "partner.toto.nl" not in alles
    assert alles.count(TOTO) == 1 and "2 november 2025" not in alles and "Accor" not in alles
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles) and not re.search(r"<(ul|ol)>\s+<", alles)
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/") or href == TOTO, href
    print("dry run ok – niets gepubliceerd")
