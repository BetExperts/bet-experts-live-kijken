# -*- coding: utf-8 -*-
"""Artikel 3/3 F1 São Paulo 2026: wie wint? Oorspronkelijk favorieten, odds (Unibet 5-11 13:36) en voorspelling.
Bijgewerkt 10-11-2026 na de race tot terugblik: wie won tegenover wat de odds vooraf zeiden. De odds van 5-11 blijven als
historie staan en zijn zo gelabeld. Feiten en bronnen: f1_brazilie_2026_data.py en f1_brazilie_2026_feiten.md.
  python3 specials/f1_brazilie_2026_wiewint.py   (dry run)"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from legaal_data import tabel
from f1_brazilie_2026_data import (ODDS, TEAM_ODDS, WINNAARS_NA, UITSLAG, STAND_NA, TEAMS_NA, SNELSTE, L, KSA, RUBRIEK,
                                   PEIL, UNIBET_GO, o)

TITEL = "Wie won de F1 GP van Brazilië 2026? Uitslag tegen de odds"
SLUG = "wie-wint-f1-gp-brazilie-2026-favorieten-odds-voorspelling"
SAMENVATTING = ("Lando Norris won de GP van Brazilië 2026 bij een odd vooraf van 10,00. Favoriet Verstappen (2,25) werd "
                "tweede. De uitslag tegenover de odds.")
V, A = ODDS[0], ODDS[1]
N = next(r for r in ODDS if r[0] == "Lando Norris")
kans = lambda x: round(100 / x)
POS = {n: p for p, n, *_ in UITSLAG}
plek = lambda n: f"{POS[n]}e" if n in POS else "buiten top 10"
assert N[2] == 10.00 and POS["Lando Norris"] == 1 and POS["Max Verstappen"] == 2

content = f"""<p><strong>Lando Norris heeft de Formule 1 Grand Prix van Brazilië 2026 gewonnen, en dat hadden de bookmakers vooraf niet zien aankomen. Bij Unibet stond de McLaren-coureur op 5 november op een odd van {o(N[2])}, als vijfde favoriet. Favoriet Max Verstappen ({o(V[2])}) werd tweede na een inhaalrace vanaf de 21e startplek. De tweede favoriet, kampioen Kimi Antonelli ({o(A[2])}), spinde twee keer en eindigde als vijfde. Isack Hadjar, vooraf {o(ODDS[6][2])}, werd derde.</strong></p>
<p><strong>Update dinsdag 10 november:</strong> dit artikel was een voorbeschouwing met odds en een voorspelling. Na de race is het een terugblik. De odds hieronder zijn de odds van vóór het weekend en zijn niet meer te spelen.</p>
<h3><strong>Uitslag tegenover de odds vooraf</strong></h3>
<p><em>Odds van Unibet op de winnaar, afgelezen op {PEIL} (vóór de trainingen, de kwalificatie en de gridstraffen).</em></p>
{tabel(["Coureur", "Team", "Odd winnaar (vooraf)", "Kans volgens odd", "Uitslag"],
       [(f"<strong>{n}</strong>" if n in ("Lando Norris", "Max Verstappen") else n, t, o(w), f"{kans(w)}%", f"<strong>{plek(n)}</strong>" if POS.get(n) == 1 else plek(n))
        for n, t, w, p, q in ODDS])}
<p>Op basis van de odds had Norris vooraf een kans van ongeveer {kans(N[2])} procent. Dat hij toch won, kwam door een sterke kwalificatie in de regen en een race waarin de grootste favorieten tegenvielen of van achteraan moesten komen.</p>
<h3><strong>Waarom won Norris?</strong></h3>
<p>Norris pakte op zaterdag in de natte kwalificatie pole position. Bij de start verloor hij de leiding aan Antonelli, maar in ronde 20 spinde de Italiaan in de eerste bocht en nam Norris de leiding weer over. Daarna hield hij de race onder controle, ook toen het in de slotfase opnieuw ging regenen. Hij won met 14,6 seconden voorsprong. Het was zijn derde zege van 2026, na Hongarije en Zandvoort, en zijn tweede op rij in Brazilië. Ook de pole kwam als verrassing: Unibet bood die vooraf aan voor {o(N[4])}.</p>"""

content2 = f"""<h3><strong>Wat ging er mis bij de favorieten?</strong></h3>
<p><strong>Max Verstappen ({o(V[2])}): tweede.</strong> Red Bull gaf hem op zaterdag een nieuwe motor, goed voor dertig plaatsen gridstraf. Verstappen reed daarom alleen Q1 en startte als 21e. In de race was hij na vijf ronden al achtste en vanaf ronde 38 tweede, toen teamgenoot Hadjar hem voorliet. Voor de zege kwam hij tekort, maar de veiligere optie uit onze voorbeschouwing, Verstappen op het podium ({o(V[3])}), viel wel goed.</p>
<p><strong>Kimi Antonelli ({o(A[2])}): vijfde.</strong> De kampioen spinde al in de verkenningsronde van de baan, leidde na de start, maar spinde in ronde 20 en later nog eens. Hij kreeg ook vijf seconden straf voor een onveilige vrijlating uit de pitbox. Wel reed hij de snelste ronde ({SNELSTE[1]}).</p>
<p><strong>Ferrari ({o(ODDS[2][2])}): achtste en negende.</strong> Door motorstraffen startte Charles Leclerc als veertiende en Lewis Hamilton als twintigste. Leclerc kreeg bovendien vijf seconden straf voor een aanrijding met Liam Lawson. Hamilton, die zijn 400e Grand Prix reed, spinde laat in de race en werd negende.</p>
<p><strong>Isack Hadjar ({o(ODDS[6][2])}): derde.</strong> De grootste verrassing bij de uitdagers. Hadjar startte als vijfde en pakte zijn podiumplek, waar Unibet vooraf {o(ODDS[6][3])} voor gaf.</p>
<h3><strong>Onze voorspelling: wat viel goed en wat niet?</strong></h3>
<p>Wij voorspelden vooraf een zege van Verstappen. Dat kwam niet uit. De gridstraf en de regen maakten het voor hem een race van inhalen in plaats van winnen.</p>
{tabel(["Tip vooraf", "Odd (Unibet, 5 nov)", "Uitkomst"], [
    ("Max Verstappen wint de race", o(V[2]), "Niet raak (2e)"),
    ("<strong>Max Verstappen op het podium</strong>", f"<strong>{o(V[3])}</strong>", "<strong>Raak (2e)</strong>"),
    ("Red Bull levert de winnaar", o(TEAM_ODDS[0][1]), "Niet raak (McLaren)"),
])}"""

content3 = f"""<h3><strong>Wat betekent de uitslag voor het WK?</strong></h3>
<p>Antonelli was al wereldkampioen sinds Mexico. Verstappen staat met {STAND_NA[1][3]} punten tweede, {STAND_NA[1][3] - STAND_NA[2][3]} punten voor George Russell en {STAND_NA[1][3] - STAND_NA[3][3]} voor Hamilton. Met nog drie races is die strijd niet beslist. Mercedes is na Brazilië constructeurskampioen: de voorsprong op Ferrari is {TEAMS_NA[0][2] - TEAMS_NA[1][2]} punten en niet meer in te halen.</p>
{tabel(["Pos.", "Coureur", "Team", "Punten"], [(str(p), f"<strong>{n}</strong>" if p <= 2 else n, t, str(pt)) for p, n, t, pt in STAND_NA[:6]])}
<h3><strong>Winnaars van de GP van Brazilië</strong></h3>
{tabel(["Jaar", "Winnaar", "Team"], WINNAARS_NA)}
<p>Verstappen won de GP van Brazilië in 2019, 2023 en 2024. Norris won in 2025 en 2026, beide keren vanaf pole.</p>
<h3><strong>Volgende race: Las Vegas</strong></h3>
<p>De volgende Grand Prix is in Las Vegas, op zondag 22 november om 05:00 uur Nederlandse tijd. Zet alleen in wat je kunt missen: zoals Brazilië liet zien, kunnen regen, straffen en fouten de odds snel op hun kop zetten.</p>
<p><a href="{UNIBET_GO}"><strong>👉 Klik hier: bekijk de F1-odds bij Unibet</strong></a></p>
<p>De volledige uitslag en de tijden staan in <a href="{L['tijden']}">F1 Brazilië 2026 uitslag en tijden</a>. Waar je de Formule 1 kunt zien, lees je in <a href="{L['kijken']}">F1 live kijken</a>. Meer tips vind je bij onze <a href="/wedtips">wedtips</a>, alle legale aanbieders bij de <a href="/bookmakers">bookmakers</a>.</p>
<h3><strong>Veelgestelde vragen over de winnaar van de GP van Brazilië</strong></h3>
<p><strong>Wie won de GP van Brazilië 2026?</strong><br>Lando Norris (McLaren), vanaf pole position. Max Verstappen werd tweede, Isack Hadjar derde.</p>
<p><strong>Wie was vooraf de favoriet?</strong><br>Max Verstappen, met een odd van {o(V[2])} bij Unibet (5 november). Kimi Antonelli was tweede favoriet ({o(A[2])}), Norris stond op {o(N[2])}.</p>
<p><strong>Hoe vaak won Verstappen in Brazilië?</strong><br>Drie keer: in 2019, 2023 en 2024.</p>
<p><strong>Is Mercedes constructeurskampioen?</strong><br>Ja. Na Brazilië heeft Mercedes {TEAMS_NA[0][2] - TEAMS_NA[1][2]} punten voorsprong op Ferrari, met nog drie races te gaan. Het is de negende titel voor het team.</p>
<p><strong>Wanneer is de volgende F1-race?</strong><br>De GP van Las Vegas, op zondag 22 november om 05:00 uur Nederlandse tijd.</p>
{KSA}"""


if __name__ == "__main__":
    alles = content + content2 + content3
    w = len(re.sub(r"<[^>]+>", " ", alles).split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", w, "woorden |", len(content), len(content2), len(content3))
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160
    assert "<h2" not in alles and "<h4" not in alles and "—" not in alles and content.startswith("<p><strong>")
    assert not re.search(r"<(?:ul|ol)>\s|\s</(?:ul|ol)>|</li>\s+<li>", alles)
    assert alles.rstrip().endswith(KSA) and alles.count("Wat kost gokken jou?") == 1
    assert "2016" not in alles and alles.count("/go/") == 1
    print("dry run ok")
