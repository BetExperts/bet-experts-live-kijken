# -*- coding: utf-8 -*-
"""Los nieuwsartikel: Oranje Palace laat op 15 oktober 2026 om 05:00 alle bonussaldi en ongebruikte free spins vervallen.
Bron: melding op de promotiepagina van oranjepalace.nl (screenshot gebruiker, 13-10). Reden en gevolgen nog onbekend:
bewust feitelijk gehouden, met praktische tips en een verantwoord-spelen-noot. Bijwerken zodra er meer bekend is.
  python3 specials/oranje_palace_bonussen_vervallen.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Oranje Palace: bonussaldi en free spins vervallen op 15 oktober, wat betekent dit?"
SLUG = "oranje-palace-bonussen-vervallen-15-oktober"
SAMENVATTING = ("Oranje Palace laat op 15 oktober om 05:00 uur alle bonussaldi en ongebruikte free spins vervallen. Dit weten "
                "we, en dit kun je nu doen.")
RUBRIEK_ALGEMEEN = "6502b65d49bc032ba533e7a2"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in koppen)
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}><thead><tr>{kop}</tr></thead><tbody>{body}</tbody></table>"


content = f"""<p><strong>Wie op dit moment de promotiepagina van <a href="/bookmakers/oranje-palace">Oranje Palace</a> opent, krijgt een opvallende melding te zien: op donderdag 15 oktober om 05:00 uur vervallen alle bestaande bonussaldi en ongebruikte free spins. Wat de aanleiding is en wat er daarna verandert, heeft Oranje Palace nog niet bekendgemaakt. In dit artikel zetten we op een rij wat er wél vaststaat, voor wie het geldt en wat je nu kunt doen.</strong></p>
<h3><strong>Wat meldt Oranje Palace precies?</strong></h3>
<p>Bovenaan de pagina met promoties en bonussen staat een waarschuwing met de titel "Bonussen vervallen binnenkort". Daarin staan twee concrete punten:</p>
<ul><li>Op <strong>15 oktober om 05:00 uur</strong> vervallen alle bestaande bonussaldi en ongebruikte free spins.</li><li>Bonussaldi waarvoor je nog <strong>niet aan de inzetvereisten</strong> hebt voldaan, en free spins die je nog niet hebt gebruikt, worden <strong>automatisch verwijderd</strong>.</li></ul>
<h3><strong>Het belangrijkste op een rij</strong></h3>
{tabel(["", ""], [
    ("<strong>Wanneer</strong>", "Donderdag 15 oktober 2026, 05:00 uur"),
    ("<strong>Wat vervalt</strong>", "Bestaande bonussaldi en ongebruikte free spins"),
    ("<strong>Voorwaarde</strong>", "Bonussaldo waarvoor de inzetvereisten nog niet zijn gehaald"),
    ("<strong>Wat gebeurt er</strong>", "Het saldo en de spins worden automatisch verwijderd"),
    ("<strong>Reden</strong>", "Nog niet bekendgemaakt"),
    ("<strong>Wat er daarna verandert</strong>", "Nog niet bekendgemaakt"),
])}
<h3><strong>Wat betekent dit voor jou?</strong></h3>
<p>Het verschil zit in het onderscheid tussen bonusgeld en echt geld. Een bonussaldo is geld dat je van het casino of de sportsbook krijgt, maar dat pas opneembaar wordt nadat je aan de inzetvereisten (ook wel rondspeelvoorwaarden) hebt voldaan. Zolang dat niet is gebeurd, blijft het een bonus. Volgens de melding verdwijnt juist dát deel op 15 oktober.</p>
<ul><li><strong>Heb je geen actieve bonus of free spins?</strong> Dan merk je volgens de melding niets van deze stap.</li><li><strong>Heb je een bonussaldo waarvan de inzetvereisten al zijn gehaald?</strong> De melding gaat over saldi waarvoor dat nog niet is gebeurd. Controleer in je account of je bonus al is omgezet naar echt saldo.</li><li><strong>Heb je nog openstaande free spins?</strong> Die worden op 15 oktober om 05:00 uur verwijderd als je ze niet hebt gebruikt.</li></ul>
<p>Over je gewone stortingssaldo zegt de melding niets. Het gaat uitdrukkelijk om bonussaldi en free spins.</p>"""

content2 = f"""<h3><strong>Wat kun je nu doen?</strong></h3>
<ol><li><strong>Controleer je account.</strong> Kijk in het bonusoverzicht van Oranje Palace of je een actieve bonus of openstaande free spins hebt, en hoe ver je bent met de inzetvereisten.</li><li><strong>Gebruik openstaande free spins</strong> als je dat toch al van plan was. Free spins kosten je geen eigen geld, maar vervallen anders.</li><li><strong>Vraag het na bij de klantenservice</strong> als je twijfelt wat er met jouw saldo gebeurt. Bewaar zo nodig een screenshot van je bonusoverzicht.</li><li><strong>Laat je niet opjagen.</strong> Ga niet meer of vaker inzetten dan je van plan was om een bonus nog op tijd vrij te spelen. Een bonus is nooit een reden om je eigen grenzen op te rekken.</li></ol>
<h3><strong>Welke acties staan er nu bij Oranje Palace?</strong></h3>
<p>Op het moment van schrijven toont Oranje Palace onder meer de volgende promoties:</p>
{tabel(["Actie", "Kort"], [
    ('<a href="/promoties/oranje-palace-casino-welkomstbonus-100-tot-250">100% Welkomstbonus casino</a>', "Tot €250 extra bij je eerste storting (min. €10, 30x inzetvereiste)"),
    ('<a href="/promoties/oranje-palace-sport-welkomstbonus-3x-14-free-bets">Sport Welkomstbonus</a>', "Zet €1 in en ontvang 3× €14 aan free bets (min. €10 storting)"),
    ('<a href="/promoties/oranje-palace-lucky-wheel-dagelijks-free-spins">Lucky Wheel</a>', "Eén keer per dag draaien voor free spins"),
    ('<a href="/promoties/oranje-palace-weekbonus-25-free-spins-gator-hunters-2-12-13-oktober">Wekelijkse Bonus</a>', "Deze week 25 free spins op Gator Hunters 2 (min. €50 storting)"),
])}
<p>Of deze acties na 15 oktober in dezelfde vorm blijven bestaan, is nog niet bekend. Op onze <a href="/promoties">promotiepagina</a> houden we het aanbod van alle legale bookmakers bij.</p>
<h3><strong>Waarom zou een aanbieder bonussaldi laten vervallen?</strong></h3>
<p>Oranje Palace heeft zelf nog geen reden gegeven, dus we gaan niet speculeren over de aanleiding in dit specifieke geval. In het algemeen zie je zo'n stap bij aanbieders bijvoorbeeld wanneer het bonussysteem wordt vernieuwd, de bonusvoorwaarden veranderen of een platform wordt aangepast. Welke van deze situaties hier speelt, of dat het om iets anders gaat, moet nog blijken.</p>
<h3><strong>We houden je op de hoogte</strong></h3>
<p>Het is nog niet helemaal duidelijk wat deze aankondiging inhoudt en wat er na 15 oktober verandert. Zodra Oranje Palace meer informatie deelt, werken we dit artikel bij.</p>"""

content3 = """<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wanneer vervallen de bonussen bij Oranje Palace?</strong><br>Op donderdag 15 oktober 2026 om 05:00 uur.</p>
<p><strong>Welke bonussen vervallen?</strong><br>Alle bestaande bonussaldi waarvoor je nog niet aan de inzetvereisten hebt voldaan, en alle ongebruikte free spins.</p>
<p><strong>Verlies ik ook mijn eigen gestorte geld?</strong><br>De melding gaat alleen over bonussaldi en free spins, niet over je gewone saldo. Twijfel je, neem dan contact op met de klantenservice van Oranje Palace.</p>
<p><strong>Waarom laat Oranje Palace de bonussen vervallen?</strong><br>Dat is nog niet bekendgemaakt. We werken dit artikel bij zodra er meer informatie is.</p>
<p><strong>Kan ik nog een welkomstbonus claimen?</strong><br>Op dit moment staan de welkomstbonussen nog op de promotiepagina van Oranje Palace. Of en hoe die na 15 oktober beschikbaar blijven, is nog niet duidelijk.</p>
<p><em>Speel bewust en zet nooit meer in dan je wilt missen, ook niet om een bonus op tijd vrij te spelen. Meer tips lees je op onze pagina over <a href="/speel-bewust/verantwoord-wedden">verantwoord wedden</a>. Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_ALGEMEEN,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting"); sys.exit()
    print("item:", WF.create_live(fd))
