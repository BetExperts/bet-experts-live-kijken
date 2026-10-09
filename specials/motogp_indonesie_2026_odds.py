# -*- coding: utf-8 -*-
"""Los artikel: MotoGP van Indonesië 2026 (Mandalika, 9-11 okt): beste odds (Bet365, stand 9 okt).
  python3 specials/motogp_indonesie_2026_odds.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF
from lk_config import PROVIDERS

TITEL = "MotoGP van Indonesië 2026: dit zijn de beste odds"
SLUG = "motogp-indonesie-2026-odds"
SAMENVATTING = ("Bezzecchi is favoriet in Mandalika, Márquez kan de WK-leiding pakken van Martín. De beste odds, het "
                "tijdschema en waar je kijkt.")
RUBRIEK_NIEUWS = "651be5190a7dba016817ccf0"
BOOKMAKER_BET365 = "651bd6728c40de720bd8072a"
B365 = PROVIDERS["bet365"]["link"]

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in koppen)
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}><thead><tr>{kop}</tr></thead><tbody>{body}</tbody></table>"


def odd(o):
    return f'<a href="{B365}" target="_blank" rel="sponsored noopener"><strong>{o}</strong></a>'


content = f"""<p><strong>Marco Bezzecchi is bij Bet365 de favoriet voor de MotoGP van Indonesië, met een odd van 2.37. Jorge Martín (3.60) en Marc Márquez (3.75) volgen, en zij hebben dit weekend meer op het spel staan: het verschil in de WK-stand is nog maar twee punten. De hoofdrace op het circuit van Mandalika begint zondag 11 oktober om 09:00 uur Nederlandse tijd en is live te zien op Ziggo Sport.</strong></p>
<p>Na de dubbele zege van Márquez in Japan is de titelstrijd in de MotoGP weer helemaal open. Martín begon in Motegi nog met twaalf punten voorsprong, maar houdt daar nu nog maar twee van over. Op Lombok wordt de zeventiende van de 22 races van het seizoen verreden, en die baan ligt Márquez historisch slecht. Hieronder zie je de beste odds, wat er voor de favorieten op het spel staat en wanneer je kunt kijken.</p>
<h3><strong>De odds voor de MotoGP van Indonesië</strong></h3>
{tabel(["Coureur", "Team", "Odd winnaar hoofdrace"], [
    ("Marco Bezzecchi", "Aprilia Racing", odd("2.37")),
    ("Jorge Martín", "Aprilia Racing", odd("3.60")),
    ("Marc Márquez", "Ducati Lenovo Team", odd("3.75")),
    ("Pedro Acosta", "Red Bull KTM Factory Racing", odd("7.50")),
])}
<p><em>Odds van Bet365 op vrijdag 9 oktober. Odds kunnen tot de start nog wijzigen.</em></p>"""

content2 = f"""<h3><strong>Marco Bezzecchi (2.37): revanche voor vorig jaar</strong></h3>
<p>Bezzecchi heeft iets recht te zetten op Mandalika. Vorig jaar was hij het hele weekend de snelste: hij pakte de pole position en won de sprint. In de hoofdrace kwam hij in de eerste ronde ten val na een botsing met Márquez, waardoor een bijna zekere zege verloren ging. Dit jaar begon hij opnieuw sterk, met de snelste tijd in de eerste vrije training. Op een circuit dat de Aprilia goed lijkt te liggen, is hij terecht de favoriet. In het WK is de Italiaan met 284 punten derde, al is de achterstand op de top twee groot.</p>
<h3><strong>Jorge Martín (3.60): de leiding verdedigen</strong></h3>
<p>Martín gaat met 333 punten aan kop in het kampioenschap. Na zijn tweede plaats in Oostenrijk leek hij de titelstrijd naar zich toe te trekken, maar in Japan liep Márquez tien punten in. Op Mandalika heeft de Spanjaard een kans om de marge weer te vergroten. De Aprilia was in de eerste training snel: tot de laatste ronde stonden er drie Aprilia's bovenaan, met Martín achter Bezzecchi en voor Raúl Fernández. Pas in de slotminuut duwde Márquez hem naar de derde plaats.</p>
<h3><strong>Marc Márquez (3.75): Mandalika blijft een lastige baan</strong></h3>
<p>Met 331 punten staat Márquez nog maar twee punten achter Martín. Een plek voor zijn landgenoot is dit weekend al genoeg om de leiding over te nemen, en dat is ook zijn eigen doel. De negenvoudig wereldkampioen gaf zelf toe dat het circuit beter bij de Aprilia's past dan bij zijn Ducati.</p>
<p>De geschiedenis spreekt ook tegen hem. In vier eerdere races in Indonesië haalde Márquez nooit de finish: drie keer kwam hij ten val en één keer viel hij uit met een technisch probleem. Daar staat tegenover dat de laatste drie winnaars op Mandalika allemaal op een Ducati reden. Met de tweede tijd in de eerste training liet hij bovendien zien dat hij er dit jaar beter voor staat.</p>
<h3><strong>Pedro Acosta (7.50): de outsider</strong></h3>
<p>Acosta boekte in Oostenrijk de eerste MotoGP-zege uit zijn carrière, maar kwam in Japan niet verder dan de zevende plaats. Op Mandalika voelt de jonge Spanjaard zich thuis in de hitte, en ook in de eerste training hoorde hij bij de snelsten. Met een odd van 7.50 is hij de interessantste outsider voor wie op een verrassing wil inzetten.</p>"""

content3 = f"""<h3><strong>Tijdschema en waar je kijkt</strong></h3>
<p>De MotoGP van Indonesië is het hele weekend live te zien bij <a href="/zenders/ziggo-sport">Ziggo Sport</a>. Let op: door het tijdsverschil met Lombok vallen de sessies vroeg op de dag.</p>
{tabel(["Sessie", "Dag", "Tijd (NL)"], [
    ("Kwalificatie", "Zaterdag 10 oktober", "04:50 uur"),
    ("Sprintrace", "Zaterdag 10 oktober", "09:00 uur"),
    ("Hoofdrace", "Zondag 11 oktober", "09:00 uur (Ziggo Sport 1)"),
])}
<h3><strong>WK-stand MotoGP voor Indonesië</strong></h3>
{tabel(["#", "Coureur", "Team", "Punten"], [
    ("1", "Jorge Martín", "Aprilia Racing", "333"),
    ("2", "Marc Márquez", "Ducati Lenovo Team", "331"),
    ("3", "Marco Bezzecchi", "Aprilia Racing", "284"),
    ("4", "Pedro Acosta", "Red Bull KTM Factory Racing", "243"),
    ("5", "Ai Ogura", "Trackhouse Racing", "237"),
    ("6", "Fabio Di Giannantonio", "Pertamina Enduro VR46 Racing", "230"),
    ("7", "Raúl Fernández", "Trackhouse Racing", "216"),
    ("8", "Francesco Bagnaia", "Ducati Lenovo Team", "164"),
    ("9", "Álex Márquez", "BK8 Gresini Racing", "158"),
    ("10", "Fermín Aldeguer", "BK8 Gresini Racing", "122"),
])}
<p>Martín en Márquez zijn duidelijk de twee titelkandidaten. Bezzecchi heeft al bijna vijftig punten achterstand en kan na Indonesië nog vijf grands prix rijden om die in te lopen.</p>
<h3><strong>Wedden op de MotoGP van Indonesië</strong></h3>
<p>Naast een weddenschap op de winnaar biedt <a href="{B365}" target="_blank" rel="sponsored noopener">Bet365</a> ook markten op een podiumplaats, de sprint en onderlinge duels tussen coureurs. Juist bij een spannende titelstrijd is een duel als Márquez tegen Martín een interessante keuze: dan gaat het niet om de winst, maar om wie van de twee als eerste over de finish komt. Hoe je bij Bet365 live meekijkt met sportevenementen, lees je op onze <a href="/zenders/bet365">Bet365-pagina</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wie is de favoriet voor de MotoGP van Indonesië?</strong><br>Marco Bezzecchi, met een odd van 2.37 bij Bet365. Hij was ook de snelste in de eerste vrije training.</p>
<p><strong>Hoe laat begint de MotoGP van Indonesië?</strong><br>De hoofdrace start zondag 11 oktober om 09:00 uur Nederlandse tijd. De sprint is zaterdag om 09:00 uur.</p>
<p><strong>Waar kan ik de MotoGP van Indonesië kijken?</strong><br>Live bij Ziggo Sport; de hoofdrace wordt uitgezonden op Ziggo Sport 1.</p>
<p><strong>Kan Márquez in Indonesië de WK-leiding pakken?</strong><br>Ja. Hij staat twee punten achter Martín, dus als hij voor zijn landgenoot eindigt, neemt hij de leiding over.</p>
<p><strong>Heeft Márquez ooit gewonnen op Mandalika?</strong><br>Nee. In vier eerdere races in Indonesië kwam hij nooit aan de finish.</p>
<p><em>24+ | Gokken is alleen toegestaan voor personen van 18 jaar en ouder. Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_NIEUWS, "bookmaker-wedtips": BOOKMAKER_BET365,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting"); sys.exit()
    print("item:", WF.create_live(fd))
