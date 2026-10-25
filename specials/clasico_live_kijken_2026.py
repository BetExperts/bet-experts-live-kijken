# -*- coding: utf-8 -*-
"""Herschrijving van het live-kijken-artikel El Clásico (item 6adce776f7e20cc73ec8ee99, slug blijft
fc-barcelona-real-madrid-live-gratis-kijken-25-10-2026), 25-10-2026, op verzoek van Jasper: "Live Stream FC Barcelona –
Real Madrid kijken & waar op tv, helemaal gratis te kijken bij TOTO". Backup oude versie:
scratchpad/clasico/live_backup.json. Na publicatie zet het script state 'handmatig' zodat generate.py het niet overschrijft.
Feiten: specials/clasico_feiten_2026_10_25.md (Ziggo Sport 1, kanaal 14; zonder Ziggo: Ziggo Sport Totaal via KPN 233 /
Odido 160 / app; scheidsrechter Martínez Munuera), uitzendschema uit het agent-artikel (20:00 voorbeschouwing).
TOTO: livestream met een gratis account, geen storting nodig (lk_config, gebruiker 8 okt 2026).
  python3 specials/clasico_live_kijken_2026.py          (dry run)
  python3 specials/clasico_live_kijken_2026.py --live   (staged + live bijwerken, state handmatig)"""
import os, sys, re, json
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

ITEM_ID = "6adce776f7e20cc73ec8ee99"
FID = "1570426"
TITEL = "Live stream FC Barcelona – Real Madrid kijken: waar op tv is El Clásico?"
SAMENVATTING = ("El Clásico live kijken op zondag 25 oktober om 21:00 uur: op Ziggo Sport 1 of gratis via de livestream van "
                "TOTO. Zender, tijden en zo werkt het.")
TOTO = "https://www.bet-experts.nl/go/toto-live-kijken"
VB = "/nieuws/wedtips-barcelona---real-madrid-voorspelling-odds-opstellingen-kan-mourinhos-madrid-de-koploper-van-zijn-troon-stoten"
OPST = "/nieuws/opstelling-fc-barcelona-real-madrid-25-10-2026"
WIEWINT = "/nieuws/wie-wint-barcelona-real-madrid-el-clasico-oktober-2026"
CTA = f'<p><a href="{TOTO}"><strong>👉 Klik hier: maak een gratis TOTO-account aan en kijk El Clásico live</strong></a></p>'

content = f"""<p><a href="/live-kijken">‹ Alle wedstrijden die je gratis live kunt kijken</a></p>
<p><strong>El Clásico tussen <a href="/clubs/fc-barcelona">FC Barcelona</a> en <a href="/clubs/real-madrid">Real Madrid</a> begint op zondag 25 oktober 2026 om 21:00 uur en is in Nederland live te zien op Ziggo Sport 1 (kanaal 14 bij Ziggo). Heb je geen Ziggo Sport? Dan kijk je de wedstrijd helemaal gratis via de livestream van TOTO: je hebt alleen een gratis account nodig, storten is niet nodig.</strong></p>
<p>Hieronder lees je op welke zender El Clásico te zien is, hoe laat de uitzending begint, hoe je de gratis livestream van TOTO in een paar minuten regelt en welke andere manieren er zijn om FC Barcelona – Real Madrid live te kijken.</p>
{CTA}
<h3><strong>Waar is FC Barcelona – Real Madrid op tv?</strong></h3>
{tabel(None, [
    ("Wedstrijd", "FC Barcelona – Real Madrid (El Clásico)"),
    ("Competitie", '<a href="/competities/la-liga">La Liga</a>, speelronde 10'),
    ("Datum", "Zondag 25 oktober 2026"),
    ("Aftrap", "21:00 uur (Nederlandse tijd, wintertijd)"),
    ("Tv-zender", '<a href="/zenders/ziggo-sport">Ziggo Sport 1</a>'),
    ("Kanaal bij Ziggo", "14"),
    ("Zonder Ziggo", "Ziggo Sport Totaal, onder meer via KPN (kanaal 233) en Odido (kanaal 160)"),
    ("Gratis livestream", f'<a href="{TOTO}">TOTO</a>, met een gratis account (18+)'),
    ("Stadion", "Spotify Camp Nou, Barcelona"),
])}
<h3><strong>Uitzendschema Ziggo Sport 1</strong></h3>
<p>Ziggo Sport begint de uitzending al een uur voor de aftrap, zodat je de opstellingen en de voorbeschouwing meekrijgt.</p>
{tabel(["Tijd", "Programma"], [
    ("20:00 uur", "Voorbeschouwing LaLiga Matchday"),
    ("20:55 uur", "Schakeling naar het Spotify Camp Nou"),
    ("21:00 uur", "<strong>Aftrap FC Barcelona – Real Madrid</strong>"),
    ("± 22:55 uur", "Einde wedstrijd (afhankelijk van blessuretijd)"),
    ("23:00 uur", "Nabeschouwing LaLiga Matchday"),
])}
<p>Welke sportzender bij jouw tv-pakket hoort, zie je in ons <a href="/nieuws/sportzenders-kanaalnummers">overzicht van alle sportzenders en kanaalnummers</a>.</p>
<h3><strong>Live stream FC Barcelona – Real Madrid: gratis kijken via TOTO</strong></h3>
<p>De makkelijkste manier om El Clásico gratis te kijken is de livestream van <a href="/bookmakers/toto">TOTO</a>. TOTO zendt de wedstrijd live uit voor iedereen met een account. Dat account is gratis, en voor de stream hoef je geen geld te storten. Zo werkt het:</p>
<ol><li><strong>Maak een gratis account aan</strong> bij TOTO via de knop op deze pagina. Omdat TOTO een vergunning van de Kansspelautoriteit heeft, controleert TOTO je leeftijd en identiteit; houd je identiteitsbewijs bij de hand.</li><li><strong>Log in</strong> op de site of in de app van TOTO, op je telefoon, tablet of laptop.</li><li><strong>Zoek FC Barcelona – Real Madrid</strong> in het voetbaloverzicht of bij de livewedstrijden.</li><li><strong>Klik op de livestream</strong> zodra de wedstrijd om 21:00 uur begint en kijk El Clásico live mee.</li></ol>
<p>Tip: maak je account al ruim voor de aftrap aan. De controle van je account kan even duren, en zo mis je niets van de eerste minuten.</p>
{CTA}
<h3><strong>Alle manieren om El Clásico live te kijken</strong></h3>
{tabel(["Manier", "Wat heb je nodig?", "Kosten"], [
    ("<strong>Livestream TOTO</strong>", "Gratis TOTO-account (18+)", "<strong>Gratis</strong>, geen storting nodig"),
    ("Ziggo Sport 1 via Ziggo", "Ziggo-abonnement met tv, kanaal 14", "Inbegrepen bij Ziggo"),
    ("Ziggo Sport via KPN of Odido", "Ziggo Sport Totaal als extra pakket", "Betaald abonnement"),
    ("Ziggo Sport-app", "Ziggo Sport Totaal-account", "Betaald abonnement"),
])}
<p>Kijk je liever op een groot scherm? Sluit je laptop met een hdmi-kabel aan op je televisie, dan kijk je de stream op je tv. Meer gratis kijkopties voor andere wedstrijden vind je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<h3><strong>Waarom je deze Clásico niet wilt missen</strong></h3>
<p>Barcelona staat met 27 punten uit negen wedstrijden bovenaan in La Liga en won elke competitiewedstrijd van dit seizoen. Real Madrid volgt op de derde plek met 21 punten, en moet het doen zonder de geschorste Vinícius Júnior. Het is bovendien de eerste Clásico tussen Hansi Flick en José Mourinho, die deze zomer terugkeerde als trainer van Real Madrid. In de officiële onderlinge balans staat het precies gelijk: beide clubs wonnen 106 keer. Alle statistieken en records lees je in ons artikel <a href="{WIEWINT}">Wie wint Barcelona – Real Madrid?</a></p>"""

content2 = f"""<h3><strong>Wedstrijdinformatie El Clásico</strong></h3>
<p><strong>Wedstrijd:</strong> FC Barcelona – Real Madrid<br><strong>Competitie:</strong> La Liga, speelronde 10<br><strong>Datum:</strong> zondag 25 oktober 2026<br><strong>Aftrap:</strong> 21:00 uur (Nederlandse tijd)<br><strong>Stadion:</strong> Spotify Camp Nou, Barcelona<br><strong>Scheidsrechter:</strong> Juan Martínez Munuera (VAR: Javier Iglesias Villanueva)<br><strong>Live op tv:</strong> Ziggo Sport 1<br><strong>Gratis livestream:</strong> TOTO</p>
<h3><strong>Barcelona en Real Madrid in vorm</strong></h3>
<p>De ploeg van Flick won alle negen competitieduels met een doelsaldo van 39-9. De enige nederlaag van het seizoen kwam dinsdag in de Champions League, met 4-2 bij Paris Saint-Germain. Real Madrid won de laatste vier wedstrijden, waaronder 4-3 bij AS Roma en 4-1 tegen RB Leipzig, maar verloor in de competitie uit bij Real Betis en Atlético Madrid. Barcelona mist Dani Olmo, Eric García, Andreas Christensen en Roony Bardghji, achter Jules Koundé staat een vraagteken. Bij Real Madrid ontbreken naast Vinícius ook Rodrygo en Raúl Asencio.</p>
<p>De officiële opstellingen zijn ongeveer een uur voor de aftrap bekend en vind je dan in ons artikel over de <a href="{OPST}">opstellingen van Barcelona – Real Madrid</a>, dat we automatisch bijwerken.</p>
<h3><strong>Odds en voorspelling</strong></h3>
<p>Barcelona is bij de bookmakers duidelijk favoriet. Bij TOTO stond een zege van Barça zaterdag op 1,58, een gelijkspel op 5,25 en een zege van Real Madrid op 3,70. Onze volledige analyse, met voorspelling en wedtip, lees je in de <a href="{VB}">voorbeschouwing van Barcelona – Real Madrid</a>.</p>"""

content3 = f"""<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Waar kan ik FC Barcelona – Real Madrid live kijken?</strong><br>Op Ziggo Sport 1, bij Ziggo op kanaal 14. Zonder Ziggo Sport kijk je gratis mee via de livestream van TOTO, met een gratis account.</p>
<p><strong>Is El Clásico gratis te kijken?</strong><br>Ja. Met een gratis account bij TOTO kijk je de wedstrijd live. Je hoeft daarvoor geen geld te storten. Ziggo-klanten kijken ook zonder extra kosten mee op Ziggo Sport 1.</p>
<p><strong>Hoe laat begint Barcelona – Real Madrid?</strong><br>De aftrap is om 21:00 uur Nederlandse tijd op zondag 25 oktober 2026. Ziggo Sport 1 begint de uitzending om 20:00 uur.</p>
<p><strong>Op welk kanaal is Ziggo Sport 1?</strong><br>Bij Ziggo op kanaal 14. Bij KPN en Odido heb je het pakket Ziggo Sport Totaal nodig: kanaal 233 bij KPN en kanaal 160 bij Odido.</p>
<p><strong>Kan ik El Clásico op mijn telefoon kijken?</strong><br>Ja, de livestream van TOTO werkt op je telefoon, tablet en laptop. Log in op je account en open de wedstrijd zodra die begint.</p>
<p><strong>Wie is de scheidsrechter van El Clásico?</strong><br>Juan Martínez Munuera fluit de wedstrijd, met Javier Iglesias Villanueva als VAR.</p>
{CTA}
<p><a href="/live-kijken"><strong>Bekijk alle wedstrijden die je gratis live kunt kijken</strong></a></p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    alles = content + content2 + content3
    tekst = re.sub(r"<[^>]+>", " ", alles)
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", len(tekst.split()), "woorden")
    assert len(TITEL) <= 75 and 120 <= len(SAMENVATTING) <= 160
    assert "<h2" not in alles and "<h4" not in alles and "betcity" not in alles.lower()
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles) and not re.search(r"<(ul|ol)>\s+<", alles)
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    if "--live" not in sys.argv:
        print("dry run ok"); sys.exit()
    import lk_webflow as WF
    fd = {"name": TITEL, "samenvatting": SAMENVATTING, "content": content, "content-2": content2, "content-3": content3}
    print("staged:", WF._req("PATCH", f"{WF.WF_API}/collections/64ff0fbd5a8f205b05d54656/items/{ITEM_ID}", {"fieldData": fd}).get("id"))
    print("live:", str(WF._req("PATCH", f"{WF.WF_API}/collections/64ff0fbd5a8f205b05d54656/items/live",
                                {"items": [{"id": ITEM_ID, "fieldData": fd}]}))[:120])
    p = os.path.join(HIER, "..", "state", "live-kijken.json")
    st = json.load(open(p, encoding="utf-8")); st[FID]["handmatig"] = True
    json.dump(st, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("state: handmatig = True (generate.py slaat dit artikel over)")
