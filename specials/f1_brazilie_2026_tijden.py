# -*- coding: utf-8 -*-
"""Artikel 1/3 F1 São Paulo 2026: tijden en programma per dag (NL-tijd). Feiten en bronnen: f1_brazilie_2026_data.py.
Bijgewerkt 10-11-2026 na de race: uitslag, kwalificatie, WK-stand, Mercedes constructeurskampioen, vooruitblik
Las Vegas. Bronnen van de update: f1_brazilie_2026_feiten.md.
  python3 specials/f1_brazilie_2026_tijden.py   (dry run)"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from legaal_data import tabel
from f1_brazilie_2026_data import (SESSIES, sessie_rij, UITSLAG, KWALI_TOP, SNELSTE, STAND_NA, TEAMS_NA, WINNAARS_NA,
                                   VOLGENDE, L, KSA, RUBRIEK)

TITEL = "F1 Brazilië 2026 uitslag: Norris wint, tijden en WK-stand"
SLUG = "f1-brazilie-2026-tijden-programma-gp-sao-paulo"
SAMENVATTING = ("Lando Norris won de GP van São Paulo 2026, voor Verstappen en Hadjar. De uitslag, kwalificatie, "
                "tijden en WK-stand, en wanneer Las Vegas is.")

content = f"""<p><strong>Lando Norris heeft de Formule 1 Grand Prix van Brazilië 2026 gewonnen. De McLaren-coureur won op zondag 8 november op Interlagos vanaf pole position, 14,6 seconden voor Max Verstappen. Verstappen startte door een motorstraf als 21e en reed in een regenrace naar de tweede plaats. Isack Hadjar maakte het podium compleet. Mercedes is na de race constructeurskampioen. De volgende race is de GP van Las Vegas, op zondag 22 november om 05:00 uur Nederlandse tijd.</strong></p>
<p><strong>Update dinsdag 10 november:</strong> dit artikel is bijgewerkt met de uitslag, de kwalificatie en de stand in het WK. De tijden hieronder laten zien hoe het weekend verliep.</p>
<h3><strong>Uitslag GP van Brazilië 2026</strong></h3>
{tabel(["Pos.", "Coureur", "Team", "Start", "Tijd / verschil", "Punten"],
       [(str(p), f"<strong>{n}</strong>" if p <= 3 else n, t, str(s), v, str(pt)) for p, n, t, s, v, pt in UITSLAG])}
<p>De race begon op een natte baan, droogde daarna op en eindigde in de regen. Norris verloor bij de start de leiding aan Kimi Antonelli, maar kwam weer op kop toen de Italiaan in ronde 20 spinde. Daarna hield de Brit de race onder controle. De snelste ronde was voor {SNELSTE[0]} ({SNELSTE[1]}, ronde {SNELSTE[2]}). Lance Stroll viel na 30 ronden uit met een technisch probleem. Valtteri Bottas ging niet van start: zijn Cadillac werd voor de start van de grid gehaald. Antonelli kreeg vijf seconden straf voor een onveilige vrijlating uit de pitbox, Charles Leclerc vijf seconden voor een aanrijding met Liam Lawson. Daardoor eindigde Lawson als zevende, voor Leclerc. De Braziliaanse thuisrijders hadden een lastige middag: Gabriel Bortoleto werd zestiende, debutant Rafael Câmara twintigste.</p>
<h3><strong>Kwalificatie: Norris op pole, Verstappen sparend</strong></h3>
{tabel(["Pos.", "Coureur", "Team", "Tijd"], [(str(p), f"<strong>{n}</strong>" if p == 1 else n, t, tm) for p, n, t, tm in KWALI_TOP])}
<p>De kwalificatie op zaterdag werd in de regen verreden en kort na de start stilgelegd met een rode vlag. Norris pakte pole met 1:27,470. Verstappen reed alleen Q1 (zestiende) en sloeg Q2 bewust over: Red Bull had zijn auto een nieuwe motor gegeven, goed voor dertig plaatsen gridstraf. Ook Lewis Hamilton (75 plaatsen), George Russell (5), Leclerc (10) en enkele anderen kregen straffen voor nieuwe motoronderdelen. Daardoor startte Antonelli als tweede, Hamilton als twintigste en Verstappen als 21e.</p>
<h3><strong>F1 Brazilië 2026 in het kort</strong></h3>
{tabel(["", "GP van São Paulo 2026"], [
    ("<strong>Winnaar</strong>", "Lando Norris (McLaren)"),
    ("<strong>Podium</strong>", "Norris, Verstappen, Hadjar"),
    ("<strong>Pole position</strong>", "Lando Norris, 1:27,470"),
    ("<strong>Snelste ronde</strong>", f"{SNELSTE[0]}, {SNELSTE[1]}"),
    ("<strong>Datum</strong>", "Vrijdag 6 tot en met zondag 8 november"),
    ("<strong>Circuit</strong>", "Interlagos (Autódromo José Carlos Pace), São Paulo"),
    ("<strong>Ronde</strong>", "20 van 23"),
    ("<strong>Volgende race</strong>", "GP van Las Vegas, zondag 22 november 05:00 uur (NL)"),
])}"""

content2 = f"""<h3><strong>Zo zag het programma eruit</strong></h3>
{tabel(["Sessie", "Dag", "Tijd NL", "Lokaal"], [sessie_rij(*s) for s in SESSIES])}
<p>Het was een gewoon raceweekend zonder sprint, voor het eerst sinds 2021. In São Paulo is het vier uur vroeger dan in Nederland. De race begon om 18:00 uur Nederlandse tijd en duurde 1 uur en 35 minuten.</p>
<h3><strong>WK-stand na Brazilië</strong></h3>
<p>Kimi Antonelli was al wereldkampioen sinds Mexico. Achter hem staat Verstappen nu 17 punten voor Russell en 18 voor Hamilton. Met nog drie races en maximaal 75 punten per coureur is de strijd om de tweede plaats nog niet beslist.</p>
{tabel(["Pos.", "Coureur", "Team", "Punten"], [(str(p), f"<strong>{n}</strong>" if p <= 3 else n, t, str(pt)) for p, n, t, pt in STAND_NA])}
<p>Bij de constructeurs is Mercedes kampioen. Het team scoorde in Brazilië 22 punten, Ferrari 6. Daarmee groeide de voorsprong naar {TEAMS_NA[0][2] - TEAMS_NA[1][2]} punten, meer dan er in de laatste drie races nog te verdienen is. Het is de negende constructeurstitel voor Mercedes en de eerste sinds 2021.</p>
{tabel(["Pos.", "Team", "Punten"], [(str(p), f"<strong>{t}</strong>" if p == 1 else t, str(pt)) for p, t, pt in TEAMS_NA])}"""

content3 = f"""<h3><strong>Het circuit: Interlagos</strong></h3>
<p>Het Autódromo José Carlos Pace in São Paulo, beter bekend als Interlagos, staat sinds 1973 op de kalender. Het is een van de weinige circuits die tegen de klok in worden gereden. De baan is kort, heuvelachtig en snel, en het weer slaat er vaak plotseling om.</p>
{tabel(["", "Interlagos"], [
    ("<strong>Lengte</strong>", "4,309 km"),
    ("<strong>Aantal ronden</strong>", "71"),
    ("<strong>Raceafstand</strong>", "305,879 km"),
    ("<strong>Bochten</strong>", "15"),
    ("<strong>Ronderecord</strong>", "1:10.540, Valtteri Bottas (2018)"),
    ("<strong>Eerste GP</strong>", "1973"),
])}
<h3><strong>Winnaars van de GP van Brazilië</strong></h3>
{tabel(["Jaar", "Winnaar", "Team"], WINNAARS_NA)}
<p>Norris won de GP van Brazilië voor de tweede keer op rij, en net als vorig jaar vanaf pole. Verstappen won hier in 2019, 2023 en 2024.</p>
<h3><strong>Volgende race: Las Vegas</strong></h3>
<p>De GP van Las Vegas wordt op zaterdagavond lokale tijd verreden. In Nederland is dat zondag 22 november om 05:00 uur 's ochtends. De kwalificatie is op zaterdag 21 november om 05:00 uur, de eerste training op vrijdag 20 november om 01:30 uur. In Nederland zie je de Formule 1 voor zover bekend nog bij Viaplay. Meer daarover lees je in <a href="{L['kijken']}">F1 live kijken</a>.</p>
{tabel(["Race", "Datum", "Start (NL)"], VOLGENDE)}
<h3><strong>Veelgestelde vragen over de F1 in Brazilië</strong></h3>
<p><strong>Wie heeft de F1-race in Brazilië 2026 gewonnen?</strong><br>Lando Norris (McLaren), vanaf pole position. Max Verstappen werd tweede, Isack Hadjar derde.</p>
<p><strong>Hoe laat was de race in Brazilië?</strong><br>Op zondag 8 november om 18:00 uur Nederlandse tijd, 14:00 uur in São Paulo.</p>
<p><strong>Waarom startte Verstappen achteraan?</strong><br>Red Bull gaf hem een nieuwe motor. Omdat hij daarmee over het maximum aan motoronderdelen ging, kreeg hij dertig plaatsen gridstraf. Hij startte als 21e.</p>
<p><strong>Is Mercedes constructeurskampioen?</strong><br>Ja. Na Brazilië heeft Mercedes {TEAMS_NA[0][2] - TEAMS_NA[1][2]} punten voorsprong op Ferrari, met nog drie races te gaan. Dat is niet meer in te halen.</p>
<p><strong>Wanneer is de volgende F1-race?</strong><br>De GP van Las Vegas, op zondag 22 november om 05:00 uur Nederlandse tijd.</p>
<p><strong>Wie won de GP van Brazilië in 2025?</strong><br>Ook Lando Norris, voor Kimi Antonelli en Max Verstappen.</p>
<p>Hoe de race verliep tegenover de odds vooraf, lees je in <a href="{L['wiewint']}">wie won de GP van Brazilië</a>.</p>
{KSA}"""


if __name__ == "__main__":
    alles = content + content2 + content3
    w = len(re.sub(r"<[^>]+>", " ", alles).split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", w, "woorden |", len(content), len(content2), len(content3))
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160
    assert "<h2" not in alles and "<h1" not in alles and "<h4" not in alles and "—" not in alles and content.startswith("<p><strong>")
    assert not re.search(r"<(?:ul|ol)>\s|\s</(?:ul|ol)>|</li>\s+<li>", alles)
    assert alles.rstrip().endswith(KSA) and alles.count("Wat kost gokken jou?") == 1
    assert "/go/" not in alles and "2016" not in alles
    print("dry run ok")
