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
SAMENVATTING = ("Oranje Palace liet op 15 oktober alle bonussaldi vervallen en werkt nu zonder bonussaldo: winst uit bonussen "
                "is direct echt geld. Dit is er veranderd.")
RUBRIEK_ALGEMEEN = "6502b65d49bc032ba533e7a2"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in koppen)
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}><thead><tr>{kop}</tr></thead><tbody>{body}</tbody></table>"


content = f"""<p><strong>Wie op dit moment de promotiepagina van <a href="/bookmakers/oranje-palace">Oranje Palace</a> opent, krijgt een opvallende melding te zien: op donderdag 15 oktober om 05:00 uur vervallen alle bestaande bonussaldi en ongebruikte free spins. Inmiddels weten we waarom: Oranje Palace werkt sinds 15 oktober met een nieuw bonusmodel zonder bonussaldo. In dit artikel lees je wat er veranderd is en wat het betekent voor jou.</strong></p>
<h3><strong>Update 15 oktober: dit is er veranderd</strong></h3>
<p>Inmiddels is duidelijk waarom de bonussaldi vervielen. Oranje Palace heeft op 15 oktober een nieuw bonusmodel ingevoerd, <strong>zonder apart bonussaldo</strong>. Wat je wint met Free Spins of Free Bets, komt nu direct als echt geld op je saldo. Bij de meeste acties moet je de promotie wel eerst activeren voordat je inzetten meetellen.</p>
<ul><li><strong>Casino Welkomstbonus:</strong> nu <a href="/promoties/oranje-palace-casino-welkomstbonus-100-free-spins">100 Free Spins op I Love Oranje</a> na €20 inzet, in plaats van 100% bonusgeld tot €250.</li><li><strong>Lucky's Quest:</strong> <a href="/promoties/oranje-palace-luckys-quest-75-free-spins-15-25-oktober">nieuwe wekelijkse actie</a> met tot 75 Free Spins in drie mijlpalen. Die vervangt de Week- en Weekendbonus.</li><li><strong>Lucky Wheel:</strong> blijft, maar je speelt je dagelijkse draai nu vrij met €5 inzet op dezelfde dag.</li><li><strong>Loyaliteitspunten:</strong> inwisselbaar voor echt geld, €0,05 per punt, en 60 dagen geldig.</li><li><strong>Sport Welkomstbonus:</strong> ongewijzigd, nog steeds 3× €14 aan Free Bets.</li></ul>
<p>Hieronder lees je wat er vóór 15 oktober gemeld werd en wat dat betekende voor bestaande bonussen.</p>
<h3><strong>Wat meldt Oranje Palace precies?</strong></h3>
<p>Bovenaan de pagina met promoties en bonussen staat een waarschuwing met de titel "Bonussen vervallen binnenkort". Daarin staan twee concrete punten:</p>
<ul><li>Op <strong>15 oktober om 05:00 uur</strong> vervallen alle bestaande bonussaldi en ongebruikte free spins.</li><li>Bonussaldi waarvoor je nog <strong>niet aan de inzetvereisten</strong> hebt voldaan, en free spins die je nog niet hebt gebruikt, worden <strong>automatisch verwijderd</strong>.</li></ul>
<h3><strong>Het belangrijkste op een rij</strong></h3>
{tabel(["", ""], [
    ("<strong>Wanneer</strong>", "Donderdag 15 oktober 2026, 05:00 uur"),
    ("<strong>Wat vervalt</strong>", "Bestaande bonussaldi en ongebruikte free spins"),
    ("<strong>Voorwaarde</strong>", "Bonussaldo waarvoor de inzetvereisten nog niet zijn gehaald"),
    ("<strong>Wat gebeurt er</strong>", "Het saldo en de spins worden automatisch verwijderd"),
    ("<strong>Reden</strong>", "Overstap naar een nieuw bonusmodel zonder bonussaldo"),
    ("<strong>Wat er daarna verandert</strong>", "Winst uit bonussen is direct echt geld; acties eerst activeren"),
])}
<h3><strong>Wat betekent dit voor jou?</strong></h3>
<p>Het verschil zit in het onderscheid tussen bonusgeld en echt geld. Een bonussaldo is geld dat je van het casino of de sportsbook krijgt, maar dat pas opneembaar wordt nadat je aan de inzetvereisten (ook wel rondspeelvoorwaarden) hebt voldaan. Zolang dat niet is gebeurd, blijft het een bonus. Volgens de melding verdwijnt juist dát deel op 15 oktober.</p>
<ul><li><strong>Heb je geen actieve bonus of free spins?</strong> Dan merk je volgens de melding niets van deze stap.</li><li><strong>Heb je een bonussaldo waarvan de inzetvereisten al zijn gehaald?</strong> De melding gaat over saldi waarvoor dat nog niet is gebeurd. Controleer in je account of je bonus al is omgezet naar echt saldo.</li><li><strong>Heb je nog openstaande free spins?</strong> Die worden op 15 oktober om 05:00 uur verwijderd als je ze niet hebt gebruikt.</li></ul>
<p>Over je gewone stortingssaldo zegt de melding niets. Het gaat uitdrukkelijk om bonussaldi en free spins.</p>"""

content2 = f"""<h3><strong>Wat kun je nu doen?</strong></h3>
<ol><li><strong>Controleer je account.</strong> Kijk in het bonusoverzicht van Oranje Palace of je een actieve bonus of openstaande free spins hebt, en hoe ver je bent met de inzetvereisten.</li><li><strong>Gebruik openstaande free spins</strong> als je dat toch al van plan was. Free spins kosten je geen eigen geld, maar vervallen anders.</li><li><strong>Vraag het na bij de klantenservice</strong> als je twijfelt wat er met jouw saldo gebeurt. Bewaar zo nodig een screenshot van je bonusoverzicht.</li><li><strong>Laat je niet opjagen.</strong> Ga niet meer of vaker inzetten dan je van plan was om een bonus nog op tijd vrij te spelen. Een bonus is nooit een reden om je eigen grenzen op te rekken.</li></ol>
<h3><strong>Welke acties staan er nu bij Oranje Palace?</strong></h3>
<p>Sinds 15 oktober toont Oranje Palace deze promoties:</p>
{tabel(["Actie", "Kort"], [
    ('<a href="/promoties/oranje-palace-casino-welkomstbonus-100-free-spins">Casino Welkomstbonus</a>', "100 Free Spins op I Love Oranje na €20 inzet (activeren)"),
    ('<a href="/promoties/oranje-palace-sport-welkomstbonus-3x-14-free-bets">Sport Welkomstbonus</a>', "Zet €1 in en ontvang 3× €14 aan free bets (min. €10 storting)"),
    ('<a href="/promoties/oranje-palace-luckys-quest-75-free-spins-15-25-oktober">Lucky’s Quest</a>', "Tot 75 Free Spins in drie mijlpalen (15 t/m 25 oktober)"),
    ('<a href="/promoties/oranje-palace-lucky-wheel-dagelijks-free-spins">Lucky Wheel</a>', "Eén keer per dag draaien na €5 inzet op dezelfde dag"),
])}
<p>Op onze <a href="/promoties">promotiepagina</a> houden we het aanbod van alle legale bookmakers bij.</p>
<h3><strong>Waarom zou een aanbieder bonussaldi laten vervallen?</strong></h3>
<p>Bij Oranje Palace was de aanleiding een nieuw bonusmodel. In het algemeen zie je zo'n stap bij aanbieders bijvoorbeeld wanneer het bonussysteem wordt vernieuwd, de bonusvoorwaarden veranderen of een platform wordt aangepast.</p>
<h3><strong>Wat betekent het nieuwe model voor jou?</strong></h3>
<p>Het voordeel is duidelijk: wat je met Free Spins of Free Bets wint, kun je direct opnemen. Het verschil zit in de voorwaarden vooraf: je activeert een actie en zet een bepaald bedrag in om de beloning vrij te spelen. Dat bedrag is de totale inzet, geen verlies. Lees per actie de voorwaarden en laat een bonus nooit de reden zijn om meer in te zetten dan je van plan was.</p>"""

content3 = """<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wanneer vervallen de bonussen bij Oranje Palace?</strong><br>Op donderdag 15 oktober 2026 om 05:00 uur.</p>
<p><strong>Welke bonussen vervallen?</strong><br>Alle bestaande bonussaldi waarvoor je nog niet aan de inzetvereisten hebt voldaan, en alle ongebruikte free spins.</p>
<p><strong>Verlies ik ook mijn eigen gestorte geld?</strong><br>De melding gaat alleen over bonussaldi en free spins, niet over je gewone saldo. Twijfel je, neem dan contact op met de klantenservice van Oranje Palace.</p>
<p><strong>Waarom liet Oranje Palace de bonussen vervallen?</strong><br>Omdat Oranje Palace op 15 oktober is overgestapt op een nieuw bonusmodel zonder bonussaldo. Winst uit Free Spins en Free Bets is nu direct echt geld.</p>
<p><strong>Kan ik nog een welkomstbonus claimen?</strong><br>Ja. Nieuwe spelers krijgen in het casino 100 Free Spins op I Love Oranje na €20 inzet, en op sport nog steeds 3× €14 aan Free Bets.</p>
<p><em>Speel bewust en zet nooit meer in dan je wilt missen, ook niet om een bonus op tijd vrij te spelen. Meer tips lees je op onze pagina over <a href="/speel-bewust/verantwoord-wedden">verantwoord wedden</a>. Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_ALGEMEEN,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv and "--update" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting"); sys.exit()
    if "--update" in sys.argv:
        fd.pop("publicatiedatum"); fd.pop("slug")
        print("bijgewerkt:", WF.update_live("6ace2650348bcab95688914b", fd))
    else:
        print("item:", WF.create_live(fd))
