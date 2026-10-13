# -*- coding: utf-8 -*-
"""Los artikel: Botic van de Zandschulp live kijken, achtste finale Shanghai tegen Rafael Jódar (wo 14 okt 2026, 06:00).
Tekst aangeleverd door de gebruiker, geredigeerd (o.a. 'matchpoint' bij eigen opslag -> breakpoint; coachclaim weggelaten).
  python3 specials/botic_jodar_shanghai_2026.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Botic van de Zandschulp Live Kijken: Achtste Finale Shanghai vs Jódar (14 oktober, 06:00)"
SLUG = "botic-van-de-zandschulp-live-kijken-shanghai-jodar-14-oktober-2026"
SAMENVATTING = ("Botic van de Zandschulp speelt woensdag 14 oktober om 06:00 uur in Shanghai tegen Rafael Jódar. Zo kijk je "
                "live via Ziggo Sport of Bet365.")
RUBRIEK_SHANGHAI = "68dd97a028b74cf1f3a2b0cb"
COMPETITIE_SHANGHAI = "68dd97842e3621da54985d13"
BET365 = "https://www.bet365.nl/hub/nl-nl/open-account?affiliate=365_02599619"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in koppen)
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}><thead><tr>{kop}</tr></thead><tbody>{body}</tbody></table>"


def lijst(items, tag="ul"):
    return f"<{tag}>" + "".join(f"<li>{i}</li>" for i in items) + f"</{tag}>"


content = f"""<p><strong>Botic van de Zandschulp zorgt voor een Nederlands feestje op de Rolex Shanghai Masters. De Veenendaler schakelde maandag de Franse topper Arthur Fils uit en staat in de achtste finale van het laatste Masters 1000-toernooi in Azië. Op woensdag 14 oktober om 06:00 uur Nederlandse tijd speelt hij voor een plek in de kwartfinale tegen het Spaanse toptalent Rafael Jódar. Hieronder lees je waar je de wedstrijd live kijkt, hoe Botic hier kwam en wat er op het spel staat.</strong></p>
<h3><strong>Botic van de Zandschulp vs Rafael Jódar in het kort</strong></h3>
{tabel(["", ""], [
    ("<strong>Wedstrijd</strong>", "Botic van de Zandschulp vs Rafael Jódar"),
    ("<strong>Ronde</strong>", "Achtste finale (vierde ronde)"),
    ("<strong>Toernooi</strong>", "Rolex Shanghai Masters 2026 (ATP Masters 1000)"),
    ("<strong>Datum</strong>", "Woensdag 14 oktober 2026"),
    ("<strong>Aanvang</strong>", "06:00 uur Nederlandse tijd (12:00 uur in Shanghai)"),
    ("<strong>Locatie</strong>", "Qi Zhong Tennis Center, Shanghai"),
    ("<strong>Ondergrond</strong>", "Outdoor hardcourt"),
    ("<strong>Live kijken</strong>", "Ziggo Sport en de livestream van Bet365"),
])}
<h3><strong>Waar kijk je Botic van de Zandschulp live?</strong></h3>
<h4>Ziggo Sport</h4>
<p><a href="/zenders/ziggo-sport">Ziggo Sport</a> zendt de ATP Masters 1000-toernooien uit in Nederland, en wedstrijden van Nederlanders krijgen voorrang in de programmering. De kans is dus groot dat Botic tegen Jódar live op Ziggo Sport te zien is. Kijk vlak voor 06:00 uur in de tv-gids op welk kanaal (Ziggo Sport, Ziggo Sport 4 of Ziggo Sport 5) de wedstrijd wordt uitgezonden.</p>
<h4>Gratis livestream bij Bet365</h4>
<p>Heb je geen Ziggo Sport, of kijk je liever op je telefoon in bed? Dan volg je de wedstrijd via de livestream van Bet365. Zo werkt het:</p>
{lijst(["Maak een gratis account aan via de link hieronder.",
        "Stort €10. Voor de livestream heb je een account met saldo nodig, of een weddenschap in de afgelopen 24 uur.",
        "Ga naar Tennis, kies Live en zoek Van de Zandschulp vs Jódar met het streamicoon.",
        "Klik op Live kijken en volg de wedstrijd met live statistieken.",
        "Haal na afloop je €10 er gewoon weer af."], "ol")}
<p>Regel dit bij voorkeur dinsdagavond al, zodat je om 06:00 uur meteen kunt kijken.</p>
<p>👉 <a href="{BET365}"><strong>Maak een gratis Bet365-account aan en kijk Botic live</strong></a></p>
<h4>Tennis TV</h4>
<p>De officiële streamingdienst van de ATP zendt ook alle wedstrijden uit, maar daarvoor heb je een betaald abonnement nodig.</p>
<h3><strong>Hoe laat speelt Botic van de Zandschulp?</strong></h3>
<p>De wedstrijd staat als eerste partij van de dag gepland om 06:00 uur Nederlandse tijd (12:00 uur in Shanghai). Omdat het de openingswedstrijd op de baan is, begint die in principe op tijd. Alleen regen kan dan nog voor uitstel zorgen.</p>
<p><em>Tip: zet je wekker op 05:45 uur, dan mis je het inspelen en de opkomst niet.</em></p>
<h3><strong>De weg van Botic naar de achtste finale</strong></h3>
<p>Botic van de Zandschulp beleeft een geweldige week in Shanghai. Hij versloeg drie tegenstanders:</p>
{tabel(["Ronde", "Tegenstander", "Uitslag"], [
    ("Eerste ronde", "Daniel Mérida (Spanje)", "1-6, 6-3, 6-4"),
    ("Tweede ronde", "Alex Michelsen (31e reekshoofd)", "6-4, 6-4"),
    ("Derde ronde", "Arthur Fils (8e reekshoofd)", "7-5, 6-4"),
])}
<h4>Eerste ronde: Daniel Mérida (1-6, 6-3, 6-4)</h4>
<p>Botic verloor de eerste set tegen de Spaanse Umag-winnaar in nog geen half uur met 1-6, maar herstelde zich goed. Met agressief netspel draaide hij de wedstrijd om.</p>
<h4>Tweede ronde: Alex Michelsen (6-4, 6-4)</h4>
<p>Tegen het 31e reekshoofd serveerde Botic sterk en bleef hij in de lastige momenten rustig. Eén break per set was genoeg, en voor het eerst in zijn carrière bereikte hij de derde ronde in Shanghai.</p>
<h4>Derde ronde: Arthur Fils (7-5, 6-4)</h4>
<p>De grootste stunt. Fils, de nummer tien van de wereld en winnaar van Cincinnati, kreeg in de eerste set zeven breakpoints, maar Botic wist ze allemaal te redden. Toen hij in de tweede set voor de wedstrijd serveerde, overleefde hij nog een laatste breakpoint met een prachtige forehand-winner. Fils was zo gefrustreerd dat hij twee rackets kapot sloeg. Onze voorbeschouwing op die partij lees je in de <a href="/nieuws/atp-shanghai-wedtips-voorspellingen-maandag-12-oktober-2026">ATP Shanghai wedtips van maandag 12 oktober</a>.</p>
<p>Eerder dit jaar haalde Botic ook al de vierde ronde op het Masters-toernooi van Montreal. Deze zomer bereikte hij bovendien de kwartfinale van de US Open, na een van de langste wedstrijden in de geschiedenis van het toernooi.</p>"""

content2 = f"""<h3><strong>Wie is Rafael Jódar?</strong></h3>
<p>Rafael Jódar (20) is een van de grootste Spaanse talenten na Carlos Alcaraz. Hij staat op de 13e plaats van de wereldranglijst en is in Shanghai als twaalfde geplaatst. Wat je over hem moet weten:</p>
{lijst(["Hij maakte dit seizoen een enorme sprong op de ranglijst.",
        "Deze zomer haalde hij de finale van het ATP-toernooi in Washington, die hij verloor van Taylor Fritz.",
        "Hij maakte zijn debuut op de Laver Cup, in Team Europe.",
        "In de derde ronde in Shanghai versloeg hij Jiří Lehečka, die een week eerder nog de finale van de Japan Open speelde."])}
<p>Jódar is een agressieve baselinespeler met een sterke forehand en veel energie. Wel mist hij nog wat ervaring in de late fases van grote toernooien.</p>
<h3><strong>Kansen en odds</strong></h3>
<p>De bookmakers zien Jódar als favoriet:</p>
{tabel(["Uitslag", "Odd"], [("Rafael Jódar wint", "<strong>1.50</strong>"), ("Botic van de Zandschulp wint", "<strong>2.62</strong>")])}
<p>Toch heeft Botic in Shanghai laten zien dat hij in vorm is. Na zijn zege op een top-tienspeler als Fils speelt hij vol vertrouwen, en met zijn sterke service en zijn rust in de belangrijke momenten is hij gevaarlijk voor de jonge Spanjaard. Meer tips voor deze ronde vind je in onze <a href="/nieuws/atp-shanghai-wedtips-voorspellingen-dinsdag-13-oktober-2026">ATP Shanghai wedtips</a>. <em>De odds zijn indicatief en kunnen wijzigen.</em></p>
<h3><strong>Wat staat er op het spel?</strong></h3>
{tabel(["", "Prijzengeld", "ATP-punten"], [
    ("<strong>Bij winst</strong> (kwartfinale)", "$193.645 (± €166.500)", "200"),
    ("<strong>Bij verlies</strong> (achtste finale)", "$105.720 (± €90.900)", "100"),
])}
<p>Met een overwinning haalt Botic zijn eerste kwartfinale ooit op een ATP Masters 1000-toernooi, en dat levert hem ook een flinke stijging op de wereldranglijst op. Alle bedragen per ronde vind je in ons overzicht van het <a href="/nieuws/prijzengeld-shanghai-masters-2026">prijzengeld van de Shanghai Masters 2026</a>.</p>"""

content3 = f"""<h3><strong>Wie wacht er in de kwartfinale?</strong></h3>
<p>Wint Botic van Jódar, dan speelt hij op donderdag 15 oktober in de kwartfinale tegen de winnaar van een andere achtste finale in zijn deel van het schema. Het toernooi zit vol verrassingen: Carlos Alcaraz werd uitgeschakeld door de Belg Zizou Bergs, Novak Djokovic verloor van Hubert Hurkacz, en Ben Shelton ging onderuit tegen de 21-jarige Fransman Arthur Géa. Door de nederlaag van Alcaraz is Alexander Zverev zeker van de nummer één-positie aan het eind van het jaar.</p>
<h3><strong>Speelschema Shanghai Masters 2026 (Nederlandse tijd)</strong></h3>
{tabel(["Dag", "Ronde"], [
    ("Dinsdag 13 en woensdag 14 oktober", "Achtste finales (vanaf 06:00 uur)"),
    ("Donderdag 15 oktober", "Kwartfinales"),
    ("Vrijdag 16 oktober", "Halve finales"),
    ("Zondag 18 oktober", "Finale (niet vóór 10:30 uur)"),
])}
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat speelt Botic van de Zandschulp op woensdag 14 oktober?</strong><br>Om 06:00 uur Nederlandse tijd, als eerste wedstrijd van de dag.</p>
<p><strong>Tegen wie speelt Botic van de Zandschulp?</strong><br>Tegen de 20-jarige Spanjaard Rafael Jódar, de nummer 13 van de wereld.</p>
<p><strong>Waar kijk ik Botic van de Zandschulp live?</strong><br>Op <a href="/zenders/ziggo-sport">Ziggo Sport</a> en via de livestream van Bet365.</p>
<p><strong>Kan ik Botic gratis kijken?</strong><br>Ja, via de livestream van Bet365. Stort €10, kijk de wedstrijd en haal je €10 daarna weer terug.</p>
<p><strong>Hoe versloeg Botic Arthur Fils?</strong><br>Met 7-5, 6-4. Hij redde zeven breakpoints in de eerste set en hield ook stand toen hij voor de wedstrijd serveerde.</p>
<p><strong>Wat verdient Botic als hij de kwartfinale haalt?</strong><br>$193.645 (ongeveer €166.500) en 200 ATP-punten.</p>
<p><strong>Speelt Tallon Griekspoor nog mee?</strong><br>Nee, Griekspoor werd in de eerste ronde uitgeschakeld door qualifier Pavel Kotov. Botic is de enige Nederlander die nog in het toernooi zit.</p>
<p><em>Gokken is alleen toegestaan voor personen van 18 jaar en ouder. Speel verantwoord. Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_SHANGHAI, "competitie": COMPETITIE_SHANGHAI,
          "tennis": True, "datum-tijd-van-wedstrijd": "2026-10-14T04:00:00.000Z",
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting"); sys.exit()
    print("item:", WF.create_live(fd))
