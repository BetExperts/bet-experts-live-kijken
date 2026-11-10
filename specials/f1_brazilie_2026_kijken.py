# -*- coding: utf-8 -*-
"""Artikel 2/3 F1 São Paulo 2026: live kijken in Nederland. Feiten en bronnen: f1_brazilie_2026_data.py.
Bijgewerkt 10-11-2026 na de race: verleden tijd, uitslag kort, terugkijken, vooruitblik Las Vegas (NL-tijden) en de
tv-status na de overname van Viaplay door DPG Media (sport later als los pakket bij Videoland, plannen 'in 2027', geen
datum). Bronnen van de update: f1_brazilie_2026_feiten.md.
Niet gebruikt (niet hard genoeg): commentatoren Viaplay 2026, F1 TV Pro-prijs 2026, Viaplay-prijzen, gratis samenvattingen.
  python3 specials/f1_brazilie_2026_kijken.py   (dry run)"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from legaal_data import tabel
from f1_brazilie_2026_data import SESSIES, sessie_rij, tijden, LV_SESSIES, VOLGENDE, L, KSA, RUBRIEK

TITEL = "F1 Brazilië 2026 terugkijken en Las Vegas live kijken"
SLUG = "f1-brazilie-2026-live-kijken-gp-sao-paulo"
SAMENVATTING = ("De GP van São Paulo was live bij Viaplay en F1 TV Pro. Zo kijk je de race terug en zo zie je Las Vegas "
                "op zondag 22 november om 05:00 uur.")

DAGNL = {4: "Vrijdag", 5: "Zaterdag", 6: "Zondag"}
lv_rijen = [(f"<strong>{naam}</strong>" if c != "VT1" else naam, f"{DAGNL[n.weekday()]} {n.day} nov", f"<strong>{n:%H:%M}</strong>")
            for c, naam, u in LV_SESSIES for n in [tijden(u)[0]]]

content = f"""<p><strong>De Formule 1 Grand Prix van Brazilië 2026 was in Nederland live te zien bij Viaplay en via F1 TV Pro. Lando Norris won de race op zondag 8 november, voor Max Verstappen en Isack Hadjar. Wie de race heeft gemist, kan hem bij Viaplay en F1 TV Pro terugkijken. De volgende race, de GP van Las Vegas, is op zondag 22 november om 05:00 uur Nederlandse tijd en is voor zover bekend ook bij Viaplay te zien.</strong></p>
<p><strong>Update dinsdag 10 november:</strong> de race is verreden. Viaplay is sinds 30 oktober onderdeel van DPG Media, het bedrijf achter Videoland. Voor kijkers verandert voorlopig niets: abonnement, prijs en app blijven gelijk. Videoland wil sport later als apart pakket aanbieden en maakt de plannen in 2027 bekend. Een datum waarop de Formule 1 overstapt, is er nog niet.</p>
<h3><strong>Alle kijkopties op een rij</strong></h3>
{tabel(["Optie", "Wat zie je", "Gratis?"], [
    (f'<strong><a href="{L["viaplay"]}">Viaplay</a></strong>', "Alle sessies live en terug te kijken, met Nederlands commentaar", "Nee, abonnement"),
    (f'<strong><a href="{L["f1tv"]}">F1 TV Pro</a></strong>', "Alle sessies live en terug te kijken, met onboardcamera's en teamradio", "Nee, abonnement"),
    ("<strong>Videoland</strong>", "Nog niet: sport komt hier later als apart pakket", "-"),
    ("<strong>NOS / Ziggo Sport</strong>", "Geen Formule 1", "-"),
    ("<strong>Grand Prix Radio</strong>", "Radioverslag met Olav Mol en Jack Plooij", "Ja"),
])}
<h3><strong>De race in Brazilië terugkijken</strong></h3>
<p>Het was een race om terug te kijken. Het begon nat, droogde op en eindigde weer in de regen. Verstappen startte door een motorstraf als 21e en werd tweede. Kampioen Kimi Antonelli spinde twee keer en werd vijfde, en Mercedes werd constructeurskampioen, ook al stond er geen Mercedes op het podium. Bij Viaplay en F1 TV Pro kun je de race en de kwalificatie terugkijken met je abonnement. De volledige uitslag en de WK-stand staan in ons artikel over <a href="{L['tijden']}">de uitslag en tijden van de F1 in Brazilië</a>.</p>
<p>Zo zag het weekend eruit, in Nederlandse tijd:</p>
{tabel(["Sessie", "Dag", "Tijd NL", "Lokaal"], [sessie_rij(*s) for s in SESSIES])}"""

content2 = f"""<h3><strong>Volgende race: de GP van Las Vegas live kijken</strong></h3>
<p>De GP van Las Vegas is de 21e van de 23 races van 2026. De race wordt op zaterdagavond lokale tijd verreden, en Las Vegas loopt negen uur achter op Nederland. Wie live wil kijken, moet dus vroeg op: de race begint op zondag 22 november om 05:00 uur.</p>
{tabel(["Sessie", "Dag", "Tijd NL"], lv_rijen)}
<p>Voor zover nu bekend zendt Viaplay ook Las Vegas, Qatar en de slotrace in Abu Dhabi uit. Er is geen bericht dat de Formule 1 nog dit seizoen naar Videoland gaat. Mocht dat veranderen, dan werken we dit artikel bij.</p>
{tabel(["Race", "Datum", "Start (NL)"], VOLGENDE)}
<h3><strong>F1 TV Pro: de dienst van de Formule 1 zelf</strong></h3>
<p>F1 TV Pro is ook in Nederland los af te sluiten. Je ziet daarmee alle sessies live, met extra's zoals de onboardcamera van elke coureur, live timing en de teamradio. Na afloop kun je races volledig terugkijken. Het commentaar is standaard Engelstalig.</p>
<h3><strong>Kun je de Formule 1 gratis kijken?</strong></h3>
<p>Een gratis live-uitzending is er niet. NOS en Ziggo Sport zenden geen Formule 1 uit. Wel gratis is het radioverslag van Grand Prix Radio met Olav Mol en Jack Plooij. Pas op met illegale streams: die zijn vaak traag, zitten vol reclame en kunnen malware bevatten. Bovendien is kijken via zo'n stream in Nederland niet legaal.</p>"""

content3 = f"""<h3><strong>Veelgestelde vragen over F1 kijken</strong></h3>
<p><strong>Waar was de F1 in Brazilië te zien?</strong><br>Live bij Viaplay en via F1 TV Pro. Bij beide diensten kun je de race ook terugkijken.</p>
<p><strong>Wie won de GP van Brazilië 2026?</strong><br>Lando Norris, voor Max Verstappen en Isack Hadjar. Lees hoe dat zich verhield tot de odds in <a href="{L['wiewint']}">wie won de GP van Brazilië</a>.</p>
<p><strong>Hoe laat is de F1 in Las Vegas?</strong><br>De race begint op zondag 22 november om 05:00 uur Nederlandse tijd. De kwalificatie is op zaterdag 21 november om 05:00 uur.</p>
<p><strong>Op welke zender is de F1 in Las Vegas?</strong><br>Voor zover bekend bij Viaplay, en daarnaast via F1 TV Pro.</p>
<p><strong>Is de F1 al bij Videoland te zien?</strong><br>Nee. Viaplay is wel overgenomen door DPG Media, het bedrijf van Videoland, maar de Formule 1 blijft voorlopig bij Viaplay. Videoland wil sport later als apart pakket aanbieden. Een datum is nog niet bekend.</p>
<p><strong>Zendt de NOS de Formule 1 uit?</strong><br>Nee. De NOS en Ziggo Sport hebben geen F1-rechten.</p>
{KSA}"""


if __name__ == "__main__":
    alles = content + content2 + content3
    w = len(re.sub(r"<[^>]+>", " ", alles).split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", w, "woorden |", len(content), len(content2), len(content3))
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160
    assert "<h2" not in alles and "<h4" not in alles and "—" not in alles and content.startswith("<p><strong>")
    assert not re.search(r"<(?:ul|ol)>\s|\s</(?:ul|ol)>|</li>\s+<li>", alles)
    assert alles.rstrip().endswith(KSA) and alles.count("Wat kost gokken jou?") == 1
    assert "/go/" not in alles and [r[2] for r in lv_rijen] == ["<strong>01:30</strong>", "<strong>05:00</strong>", "<strong>05:00</strong>"]
    print([re.sub(r"<[^>]+>", "", " | ".join(r)) for r in lv_rijen])
    print("dry run ok")
