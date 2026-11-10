# -*- coding: utf-8 -*-
"""Bestaand artikel bijwerken naar 2026 (cluster Grand Slam of Darts): live kijken op tv en via een stream.
Item 690f2669c289e94b55ba7a38, slug blijft (heeft historie in GSC: 'grand slam of darts 2025 op tv', 'livestream').
Back-up: backups/nieuws-690f2669-gsod-tv-2026-10-31.json. De oude tekst (2025) noemde een gratis TOTO-stream; dat is voor
2026 niet bevestigd en staat er daarom niet meer in.
Feiten: gsod_feiten_2026.md sectie 9 (Viaplay + deel gratis op Viaplay TV; DPG-overname, darts blijft voorlopig bij Viaplay
(DartsKing 30-10); België VTM (waarschijnlijk); PDCTV niet in NL; VK Sky Sports) + officiële sessietijden.
  python3 specials/gsod_tv_2026.py   (dry run)   bijwerken: zie publicatiestap in de sessie (update_staged + /items/live)"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel
import gsod_data as G

ITEM_ID = "690f2669c289e94b55ba7a38"
SLUG = G.SLUGS["tv"]
RUBRIEK = G.RUBRIEK
TITEL = "Grand Slam of Darts 2026 live kijken: op tv en via stream"
SAMENVATTING = ("Grand Slam of Darts 2026 live kijken: alle sessies op Viaplay, een deel gratis op Viaplay TV en de eerste "
                "speeldagen via de livestream van Bet365.")
B365 = "https://www.bet-experts.nl/go/bet365"   # Bet365-streamschema 4-11-2026: sessies 14, 15 en 16 nov in NL te zien

OG_EYEBROW = "Darts · 14-22 november 2026"
OG_KOP = "Grand Slam 2026<br><em>live kijken</em>"
OG_TEGELS = [("Op tv", "Viaplay"), ("Livestream", "Bet365")]
OG_KOPJE = "Uitzendingen (Nederlandse tijd)"
OG_RECHTS = "12 sessies live"
OG_RIJEN = [("Za 14 + zo 15", "Groepsfase · middag en avond", "14:00"),
            ("Ma 16 – za 21", "Avondsessies", "20:00"),
            ("Zo 22 nov", "Halve finales · finale 20:30", "14:00")]

content = f"""<p><strong>De Grand Slam of Darts 2026 is in Nederland live te zien op Viaplay. Alle 12 sessies, van zaterdag 14 tot en met zondag 22 november, worden uitgezonden. Een deel van de sessies is gratis te zien op Viaplay TV; de beslissende rondes zitten meestal achter de betaalmuur. Daarnaast staan de eerste speeldagen in de livestream van Bet365. In België zendt VTM de grote PDC-toernooien traditioneel gratis uit. Hieronder lees je per dag hoe laat je moet afstemmen en welke opties je hebt.</strong></p>
<h3><strong>Grand Slam of Darts 2026 op tv: de opties</strong></h3>
{tabel(["Optie", "Wat zie je", "Kosten"], [
    (f"<strong>{G.EXTRA['viaplay']} (streamingdienst)</strong>", "Alle sessies live, plus herhalingen", "Betaald abonnement"),
    ("<strong>Viaplay TV (tv-zender)</strong>", "Een deel van de sessies; welke, maakt Viaplay vlak voor het toernooi bekend", "Gratis in de meeste tv-pakketten"),
    ("<strong>VTM (België)</strong>", "Grote PDC-toernooien, via VTM 2 en VTM GO", "Gratis"),
    ("<strong>Bet365 (livestream)</strong>", "De sessies van 14, 15 en 16 november; latere sessies mogelijk later", "Saldo op je account of een weddenschap in de afgelopen 24 uur"),
    ("<strong>PDCTV</strong>", "Niet beschikbaar in Nederland en België, omdat er een tv-partner is", "–"),
])}
<p>Viaplay Nederland is overgenomen door DPG Media. Volgens de huidige berichtgeving verandert er voor de Grand Slam 2026 niets: de darts blijft voorlopig bij Viaplay, net als de Players Championship Finals en het WK. De sportrechten gaan pas op termijn naar Videoland.</p>"""

content2 = f"""<h3><strong>Hoe laat is de Grand Slam of Darts 2026 op tv?</strong></h3>
{tabel(["Dag", "Aanvang (NL)", "Ronde"], [
    (f"<strong>{d} {dt}</strong>", nl, r) for d, dt, nl, uk, r, n in G.SESSIES
])}
<p><em>Aanvangstijden van de sessies volgens de officiële ticketverkoop van de PDC, omgerekend naar Nederlandse tijd. De uitzending begint meestal kort voor de eerste wedstrijd. Het complete {G.a('speelschema', 'speelschema van de Grand Slam of Darts 2026')} met uitleg per dag vind je in ons aparte artikel.</em></p>
<h3><strong>Gratis kijken naar de Grand Slam of Darts</strong></h3>
<p>Gratis en legaal kijken kan in Nederland alleen naar de sessies die Viaplay op zijn tv-zender Viaplay TV uitzendt. Die zender zit in de basispakketten van de meeste tv-aanbieders. Welke sessies dat dit jaar zijn, publiceert Viaplay kort voor het toernooi; bij eerdere grote toernooien waren het vooral de sessies in de eerste dagen. Op welk kanaal je Viaplay TV vindt, lees je op onze pagina over {G.EXTRA['viaplay']}. Kijk uit voor illegale streams: die zijn niet alleen verboden, ze zitten ook vaak vol met malware en misleidende reclame.</p>
<p>Woon je in België, dan kun je bij VTM terecht. In 2025 zond VTM de Grand Slam gratis uit via VTM 2 en de app VTM GO; op drukke dagen kan een sessie naar een andere VTM-zender gaan. Check vlak voor het toernooi de programmering.</p>
<h3><strong>Grand Slam of Darts live kijken via Bet365</strong></h3>
<p>Ook Bet365 zendt de Grand Slam of Darts uit in zijn livestream. Volgens het streamingschema van Bet365 (stand 4 november) zijn de middag- en avondsessie van zaterdag 14 en zondag 15 november en de avondsessie van maandag 16 november ook in Nederland live te zien. Bet365 vult het schema aan zodra de volgende speeldagen vastliggen. Het is dus goed mogelijk dat de latere rondes volgen, maar zeker is dat nu nog niet.</p>
<p><strong>Zo kijk je de Grand Slam via Bet365:</strong></p>
<ol><li><strong>Open een account</strong> bij Bet365 via de link hieronder (18+, met ID-controle)</li><li><strong>Zorg voor saldo</strong> op je account: met saldo, of een weddenschap in de afgelopen 24 uur, krijg je toegang tot de livestream</li><li><strong>Ga naar Live</strong>, kies darts en start de stream van de sessie op je telefoon, tablet of laptop</li></ol>
<p>Het kijken zelf kost niets: saldo dat je niet gebruikt, kun je gewoon weer opnemen. <a href="{B365}"><strong>👉 Klik hier: open een account bij Bet365 en kijk de Grand Slam live</strong></a></p>
<h3><strong>Kijken vanuit het buitenland</strong></h3>
<p>In het Verenigd Koninkrijk is Sky Sports de rechtenhouder, met uitzendingen op Sky Sports en via de Sky Sports-app en NOW. Ben je op vakantie in het buitenland, dan kun je met een Nederlands Viaplay-abonnement binnen de EU gewoon blijven kijken.</p>"""

content3 = f"""<h3><strong>Wat kun je verwachten van de Grand Slam of Darts 2026?</strong></h3>
<p>Het toernooi wordt groter dan ooit: 48 spelers in 16 groepen van drie en £1 miljoen prijzengeld, waarvan £200.000 voor de winnaar. Luke Littler verdedigt zijn titel en kan als derde speler ooit drie keer op rij winnen. Met onder anderen Michael van Gerwen, Gian van Veen en Wessel Nijman zijn er zeven Nederlanders zeker van een plek. Lees meer in {G.a('deelnemers', 'deelnemers en poules')}, het {G.a('format', 'nieuwe format')}, het {G.a('prijzengeld', 'prijzengeld')} en de {G.a('winnaars', 'lijst met winnaars van de Grand Slam of Darts')}. Andere manieren om sport te volgen vind je op onze pagina {G.EXTRA['livekijken']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Op welke zender is de Grand Slam of Darts 2026?</strong><br>In Nederland op Viaplay; een deel van de sessies is gratis op Viaplay TV. In België op VTM, in het Verenigd Koninkrijk op Sky Sports.</p>
<p><strong>Kan ik de Grand Slam of Darts gratis kijken?</strong><br>Ja, de sessies die op Viaplay TV worden uitgezonden. Voor alle sessies heb je een Viaplay-abonnement nodig.</p>
<p><strong>Kan ik de Grand Slam of Darts kijken via Bet365?</strong><br>Ja, in elk geval de sessies van 14, 15 en 16 november: die staan in het streamingschema van Bet365 en zijn in Nederland te zien. Je hebt een account met saldo nodig, of een weddenschap in de afgelopen 24 uur.</p>
<p><strong>Hoe laat begint de Grand Slam of Darts op tv?</strong><br>Op zaterdag 14 november om 14:00 uur Nederlandse tijd. De finale is op zondag 22 november in de avondsessie vanaf 20:30 uur.</p>
<p><strong>Blijft de darts bij Viaplay nu DPG Viaplay heeft overgenomen?</strong><br>Voor de Grand Slam 2026, de Players Championship Finals en het WK wel. Wanneer de rechten naar Videoland gaan, is nog niet bekend.</p>
{G.SLOT}"""

if __name__ == "__main__":
    alles = G.check(sys.modules[__name__], 700)
    assert "toto" not in alles.lower() and alles.count(B365) == 1
    print("dry run ok – niets gepubliceerd")
