# -*- coding: utf-8 -*-
"""Artikel 1/3 Suriname – Eswatini: live kijken (tv, stream, hoe laat). Feiten: suriname_eswatini_2026_feiten.md §0, §3, §8.
Stand 13-11: nergens een uitzending aangekondigd (NL, Suriname, Eswatini, SVB); niet in Bet365-schema, niet bij Kambi.
Daarom: "nog geen uitzending aangekondigd", geen stream beloven. Zaterdag/zondag opnieuw checken en bijwerken.
  python3 specials/suriname_eswatini_kijken.py  (dry run)"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, "..")); sys.path.insert(0, HIER)
from legaal_data import tabel
from suriname_eswatini_2026_data import RUBRIEK, KSA, SLUGS, L, WEDSTRIJD

SLUG = SLUGS["kijken"]
TITEL = "Suriname – Eswatini live kijken: tv, stream en hoe laat"
SAMENVATTING = ("Suriname – Eswatini live kijken? Natio speelt zondag 15 november om 18:00 uur in De Vliert in Den Bosch. "
                "Dit weten we over tv en stream.")
OG_EB, OG_KOP = "Oefeninterland · live kijken", "Suriname – Eswatini <em>live kijken</em>"
OG_RIJEN = [("Aftrap", "zo 15 nov · 18:00"), ("Stadion", "De Vliert, Den Bosch"), ("Tv / stream", "Nog niet aangekondigd"),
            ("Tickets", "Vanaf €10")]

content = f"""<p><strong>Suriname – Eswatini begint op zondag 15 november 2026 om 18:00 uur Nederlandse tijd in Stadion De Vliert in Den Bosch. Op vrijdag 13 november had nog geen enkele Nederlandse of Surinaamse zender een uitzending aangekondigd, en ook de Surinaamse voetbalbond meldt (nog) geen livestream. Wie de wedstrijd zeker wil zien, kan het beste een kaartje kopen: die zijn er vanaf €10. Zodra er een uitzending bekend wordt, werken we dit artikel bij.</strong></p>
<p>Voor de Surinaamse gemeenschap in Nederland is dit een bijzondere wedstrijd. Het is de eerste keer sinds maart 2024 dat Natio in Nederland speelt, en volgens Omroep Brabant de eerste interland in De Vliert in 75 jaar. Donderdag speelde Suriname in Kaunas met 0-0 gelijk tegen Litouwen; lees daarover in ons artikel over {L['litouwen']}.</p>
<h3><strong>Suriname – Eswatini: alle informatie</strong></h3>
{tabel(["", "Suriname – Eswatini"], WEDSTRIJD + [("Tv en stream", "Nog niet aangekondigd (stand vrijdag 13 november)")])}
<h3><strong>Op welke zender is Suriname – Eswatini?</strong></h3>
<p>Voor zover nu bekend op geen enkele. We zochten bij de Nederlandse zenders (NOS, ESPN, Ziggo Sport, Viaplay, Videoland en DAZN), bij Omroep Brabant en bij de Surinaamse zenders ATV, STVS, Sun TV en ABC. Nergens staat Suriname – Eswatini op het programma. Ook de Surinaamse voetbalbond (SVB) en de bond van Eswatini noemen geen uitzending.</p>
<p>Dat is niet vreemd bij een oefeninterland die pas deze week definitief werd: FC Den Bosch had ongeveer een week om alles te regelen. Houd daarom de kanalen van de SVB en van Natio in de gaten: een livestream via Facebook of YouTube wordt soms op het laatste moment aangekondigd.</p>
<h3><strong>Kun je Suriname – Eswatini live streamen bij een bookmaker?</strong></h3>
<p>Ook dat lijkt er niet in te zitten. De wedstrijd staat niet in het livestreamschema van Bet365, en bij de bookmakers die we controleerden stond het duel op vrijdag nog niet eens in het aanbod. Daarom beloven wij hier geen stream. Verandert dat, dan lees je het hier. Kijk voor de streams van dit weekend ook op onze pagina {L['livekijken']}.</p>"""

content2 = f"""<h3><strong>Hoe laat is Suriname – Eswatini?</strong></h3>
<p>De aftrap is om <strong>18:00 uur</strong> Nederlandse tijd. In Suriname is het dan 14:00 uur en in Eswatini 19:00 uur. Een oefeninterland duurt, inclusief rust, ongeveer twee uur; rond 20:00 uur is de wedstrijd afgelopen. Op zondagavond is er geen concurrentie van Oranje: het Nederlands elftal speelt vrijdag tegen Griekenland en maandag in Duitsland.</p>
<h3><strong>Toch live erbij zijn? Zo kom je aan kaarten</strong></h3>
<p>Kaarten koop je alleen via de officiële ticketshop van {L['denbosch']}. Een plek kost €20 in de meeste vakken, €10 in één vak op de Noordtribune en €45 voor business. Op vrijdag waren er nog volop kaarten. Alles over prijzen, parkeren en de route lees je in ons artikel over {L['tickets']}.</p>
<h3><strong>Het weer in Den Bosch</strong></h3>
<p>Neem een jas mee. De verwachting voor zondag rond 18:00 uur is ongeveer tien graden, motregen en een stevige wind. De Vliert heeft een kunstgrasveld, dus de wedstrijd gaat bij regen gewoon door.</p>
<h3><strong>Waarom speelt Suriname tegen Eswatini?</strong></h3>
<p>Suriname heeft deze interlandperiode geen officiële wedstrijden. In oktober lag Natio in de Nations League van de CONCACAF eruit na een 1-0-nederlaag in Guatemala, een duel dat werd overschaduwd door racisme richting de Surinaamse spelers. Bondscoach Henk Fraser gebruikt deze week om nieuwe spelers te testen. Eswatini, het vroegere Swaziland, maakt een Europese tournee: donderdag speelde het met 1-1 gelijk op Malta. Meer over beide ploegen, de selectie en de debutanten lees je in {L['voorspelling']}.</p>"""

content3 = f"""<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Waar kan ik Suriname – Eswatini live kijken?</strong><br>Op vrijdag 13 november was er nog geen tv-uitzending of livestream aangekondigd, in Nederland noch in Suriname. Houd de kanalen van de SVB in de gaten; we werken dit artikel bij zodra er een uitzending bekend is.</p>
<p><strong>Hoe laat begint Suriname – Eswatini?</strong><br>Zondag 15 november 2026 om 18:00 uur Nederlandse tijd (14:00 uur in Suriname).</p>
<p><strong>Waar wordt Suriname – Eswatini gespeeld?</strong><br>In Stadion De Vliert in 's-Hertogenbosch, het stadion van FC Den Bosch (Victorialaan 21).</p>
<p><strong>Is Suriname – Eswatini op tv in Suriname?</strong><br>Ook ATV, STVS, Sun TV en ABC hadden de wedstrijd vrijdag nog niet op het programma staan.</p>
<p><strong>Zijn er nog kaarten?</strong><br>Ja, op vrijdag waren er nog volop kaarten, vanaf €10, via de ticketshop van FC Den Bosch.</p>
<p><strong>Wat was de uitslag van Litouwen – Suriname?</strong><br>0-0. Doelman Jahnilo Wiegel-Triebel debuteerde en hield de nul.</p>
{KSA}"""

if __name__ == "__main__":
    import re
    alles = content + content2 + content3
    w = len(re.sub(r"<[^>]+>", " ", alles).split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", w, "woorden")
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert "<h2" not in alles and "betcity" not in alles.lower() and "waaroptv" not in alles.lower() and "/go/" not in alles
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles) and content3.rstrip().endswith(KSA)
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    print("dry run ok")
