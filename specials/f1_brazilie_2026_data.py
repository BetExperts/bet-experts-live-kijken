# -*- coding: utf-8 -*-
"""Gedeelde feiten voor de drie artikelen over de F1 GP van São Paulo 2026 (Interlagos), nagelopen op 5-11-2026,
bijgewerkt na de race op 10-11-2026 (uitslag, kwalificatie, stand, Las Vegas, tv-status): zie f1_brazilie_2026_feiten.md
voor bron-URL's en controletijden van de update. Hieronder de bronnen van de voorbeschouwing (5-11).
Bronnen (alleen hier, nooit in de tekst):
- Ronde 20 van 23, 6-8 nov, geen sprint (eerste keer sinds 2021 zonder sprint), sessietijden in UTC:
  formula1.com/en/racing/2026/brazil; RacingNews365 tijdschema (BRT + CET). Kambi/Unibet-markten bevestigen VT1 15:30Z,
  kwali 18:00Z, race 17:00Z. São Paulo = UTC-3 (geen zomertijd), NL = CET (UTC+1): verschil 4 uur (assert hieronder).
- Circuit: formula1.com (4,309 km, 71 ronden, 305,879 km, ronderecord 1:10.540 Bottas 2018, eerste GP 1973);
  15 bochten volgens meerdere gidsen; tegen de klok in (algemeen bekend).
- Winnaars 2021-2025: formula1.com results (2021 Hamilton, 2022 Russell, 2023/2024 Verstappen, 2025 Norris vanaf pole,
  podium Norris-Antonelli-Verstappen, Verstappen startte uit de pitstraat).
- Stand na Mexico (ronde 19): formula1.com/en/results/2026/drivers en /team. Antonelli wereldkampioen in Mexico (3e):
  Sky Sports 1-11-2026 (jongste kampioen ooit, eerste Italiaanse kampioen sinds Ascari 1953). Kambi heeft geen markt
  'Coureurskampioenschap 2026' meer (alleen 2027) = bevestiging.
- Constructeurs: Mercedes 630, Ferrari 504 (126 verschil); na Brazilië nog 3 races = max. 129 punten per team (25+18 per
  race, geen sprints, geen punt voor snelste ronde). Mercedes kampioen bij +3 t.o.v. Ferrari (gelijk = Mercedes door meer zeges:
  Antonelli 10 + Russell 3 tegen Hamilton 1 + Leclerc 1). Eigen rekensom + grandepremio/littlebigreddot.
- Laatste races: Singapore (11-10) Verstappen/Leclerc/Antonelli; Austin (25-10) Antonelli/Leclerc/Verstappen;
  Mexico (1-11) Verstappen/Hamilton/Antonelli (Hamilton van pole). Silverstone.co.uk, The Race.
- Câmara debuteert bij Haas in plaats van Ocon (grandepremio, littlebigreddot). Bortoleto thuisrace (Audi).
- Weer: Open-Meteo-model (5-11): zaterdagmiddag 63-78% neerslagkans, zondag 90-98%; littlebigreddot: za 50%. -> 'grote kans op regen'.
- Tv: Viaplay NL exclusief t/m 2029, sinds 30-10-2026 onderdeel van DPG Media (Videoland); F1 gaat later naar Videoland,
  datum onbekend, Viaplay-app werkt gewoon: GPblog, GPFans. F1 TV Pro los af te sluiten in NL (GPFans/GPblog). Geen gratis
  live-uitzending (NOS/Ziggo geen F1). Radio: Grand Prix Radio met Olav Mol en Jack Plooij (GPFans).
- Odds: Unibet NL (Kambi ubnl), event 1026519081 (race), 1026519093 (kwalificatie), opgehaald 5-11-2026 13:36 NL."""
from datetime import datetime
from zoneinfo import ZoneInfo

NL, SP, UTC = ZoneInfo("Europe/Amsterdam"), ZoneInfo("America/Sao_Paulo"), ZoneInfo("UTC")
DAG = {0: "maandag", 1: "dinsdag", 2: "woensdag", 3: "donderdag", 4: "vrijdag", 5: "zaterdag", 6: "zondag"}
PEIL = "5 november, 13:36 uur"
UNIBET_GO = "https://www.bet-experts.nl/go/unibet"

SESSIES = [   # (code, naam, start UTC, duur)
    ("VT1", "Vrije training 1", "2026-11-06T15:30", "1 uur"),
    ("VT2", "Vrije training 2", "2026-11-06T19:00", "1 uur"),
    ("VT3", "Vrije training 3", "2026-11-07T14:30", "1 uur"),
    ("KWALI", "Kwalificatie", "2026-11-07T18:00", "±1 uur"),
    ("RACE", "Race (71 ronden)", "2026-11-08T17:00", "±1,5 uur"),
]


def tijden(utc):
    d = datetime.fromisoformat(utc).replace(tzinfo=UTC)
    return d.astimezone(NL), d.astimezone(SP)


assert [f"{tijden(u)[0]:%H:%M}" for _, _, u, _ in SESSIES] == ["16:30", "20:00", "15:30", "19:00", "18:00"]
assert [f"{tijden(u)[1]:%H:%M}" for _, _, u, _ in SESSIES] == ["12:30", "16:00", "11:30", "15:00", "14:00"]
assert all(tijden(u)[0].utcoffset().total_seconds() == 3600 for _, _, u, _ in SESSIES)


def sessie_rij(code, naam, utc, duur, met_lokaal=True):
    n, s = tijden(utc)
    dag = f"{DAG[n.weekday()].capitalize()} {n.day} nov"
    nm = f"<strong>{naam}</strong>" if code in ("RACE", "KWALI") else naam
    r = (nm, dag, f"<strong>{n:%H:%M}</strong>")
    return r + (f"{s:%H:%M}",) if met_lokaal else r


STAND = [  # pos, coureur, team, punten
    (1, "Kimi Antonelli", "Mercedes", 380), (2, "Max Verstappen", "Red Bull", 261), (3, "Lewis Hamilton", "Ferrari", 259),
    (4, "George Russell", "Mercedes", 250), (5, "Charles Leclerc", "Ferrari", 245), (6, "Lando Norris", "McLaren", 221),
    (7, "Oscar Piastri", "McLaren", 144), (8, "Isack Hadjar", "Red Bull", 107),
]
TEAMS = [(1, "Mercedes", 630), (2, "Ferrari", 504), (3, "Red Bull", 382), (4, "McLaren", 365), (5, "Racing Bulls", 108)]
WINNAARS = [("2025", "Lando Norris", "McLaren"), ("2024", "Max Verstappen", "Red Bull"), ("2023", "Max Verstappen", "Red Bull"),
            ("2022", "George Russell", "Mercedes"), ("2021", "Lewis Hamilton", "Mercedes")]
VORM = [("Singapore (11 okt)", "Max Verstappen", "Charles Leclerc", "Kimi Antonelli"),
        ("Verenigde Staten (25 okt)", "Kimi Antonelli", "Charles Leclerc", "Max Verstappen"),
        ("Mexico (1 nov)", "Max Verstappen", "Lewis Hamilton", "Kimi Antonelli")]
# Unibet NL, 5-11-2026 13:36: (coureur, team, winnaar, podium, pole)
ODDS = [("Max Verstappen", "Red Bull", 2.25, 1.33, 2.65), ("Kimi Antonelli", "Mercedes", 3.35, 1.45, 3.25),
        ("Charles Leclerc", "Ferrari", 9.00, 1.90, 5.50), ("Lewis Hamilton", "Ferrari", 9.00, 1.90, 6.50),
        ("Lando Norris", "McLaren", 10.00, 2.25, 9.00), ("George Russell", "Mercedes", 17.00, 3.25, 10.00),
        ("Isack Hadjar", "Red Bull", 29.00, 6.00, None), ("Oscar Piastri", "McLaren", 34.00, 7.00, None)]
TEAM_ODDS = [("Red Bull", 2.00), ("Mercedes", 3.00), ("Ferrari", 4.50), ("McLaren", 9.00)]
o = lambda x: f"{x:.2f}".replace(".", ",") if x else "-"
assert STAND[1][3] - STAND[2][3] == 2 and TEAMS[0][2] - TEAMS[1][2] == 126

# ---- Na de race (10-11-2026, formula1.com results/standings; zie f1_brazilie_2026_feiten.md) ----
# (pos, coureur, team, start, verschil, punten)
UITSLAG = [
    (1, "Lando Norris", "McLaren", 1, "1:35:23,504", 25), (2, "Max Verstappen", "Red Bull", 21, "+14,602 s", 18),
    (3, "Isack Hadjar", "Red Bull", 5, "+24,485 s", 15), (4, "George Russell", "Mercedes", 7, "+33,991 s", 12),
    (5, "Kimi Antonelli", "Mercedes", 2, "+41,017 s", 10), (6, "Oscar Piastri", "McLaren", 10, "+56,475 s", 8),
    (7, "Liam Lawson", "Racing Bulls", 3, "+1:15,402", 6), (8, "Charles Leclerc", "Ferrari", 14, "+1:18,586", 4),
    (9, "Lewis Hamilton", "Ferrari", 20, "+1 ronde", 2), (10, "Nico Hülkenberg", "Audi", 4, "+1 ronde", 1),
]
KWALI_TOP = [(1, "Lando Norris", "McLaren", "1:27,470"), (2, "George Russell", "Mercedes", "1:27,674"),
             (3, "Kimi Antonelli", "Mercedes", "1:28,095"), (4, "Charles Leclerc", "Ferrari", "1:28,289"),
             (5, "Liam Lawson", "Racing Bulls", "1:28,321")]
SNELSTE = ("Kimi Antonelli", "1:12,689", 55)
STAND_NA = [  # na Brazilië (ronde 20 van 23)
    (1, "Kimi Antonelli", "Mercedes", 390), (2, "Max Verstappen", "Red Bull", 279), (3, "George Russell", "Mercedes", 262),
    (4, "Lewis Hamilton", "Ferrari", 261), (5, "Charles Leclerc", "Ferrari", 249), (6, "Lando Norris", "McLaren", 246),
    (7, "Oscar Piastri", "McLaren", 152), (8, "Isack Hadjar", "Red Bull", 122),
]
TEAMS_NA = [(1, "Mercedes", 652), (2, "Ferrari", 510), (3, "Red Bull", 415), (4, "McLaren", 398), (5, "Racing Bulls", 114)]
_voor = {n: p for _, n, _, p in STAND}
_pts = {n: p for _, n, _, _, _, p in UITSLAG}
assert all(_voor[n] + _pts.get(n, 0) == p for _, n, _, p in STAND_NA if n in _voor)
assert dict((t, p) for _, t, p in TEAMS)["Mercedes"] + 22 == TEAMS_NA[0][2] and TEAMS[1][2] + 6 == TEAMS_NA[1][2]
assert TEAMS_NA[0][2] - TEAMS_NA[1][2] > 3 * 43   # Mercedes kampioen: 142 > 129 nog te verdienen
assert STAND_NA[1][3] - STAND_NA[2][3] == 17 and STAND_NA[1][3] - STAND_NA[3][3] == 18
WINNAARS_NA = [("2026", "Lando Norris", "McLaren")] + WINNAARS

# Volgende race: Las Vegas (formula1.com, lokale tijd UTC-8 -> NL)
LV_SESSIES = [("VT1", "Vrije training 1", "2026-11-20T00:30"), ("KWALI", "Kwalificatie", "2026-11-21T04:00"),
              ("RACE", "Race", "2026-11-22T04:00")]
assert [f"{tijden(u)[0]:%d %H:%M}" for _, _, u in LV_SESSIES] == ["20 01:30", "21 05:00", "22 05:00"]
VOLGENDE = [("GP van Las Vegas", "Zondag 22 november", "05:00 uur"), ("GP van Qatar", "Zondag 29 november", "17:00 uur"),
            ("GP van Abu Dhabi (slotrace)", "Zondag 6 december", "14:00 uur")]

# interne links
L = {
    "tijden": "/nieuws/f1-brazilie-2026-tijden-programma-gp-sao-paulo",
    "kijken": "/nieuws/f1-brazilie-2026-live-kijken-gp-sao-paulo",
    "wiewint": "/nieuws/wie-wint-f1-gp-brazilie-2026-favorieten-odds-voorspelling",
    "austin": "/nieuws/f1-austin-2026-tijden-programma-gp-verenigde-staten",
    "hadjar": "/nieuws/wie-is-isack-hadjar-de-nieuwe-f1-teamgenoot-van-max-verstappen-in-2026",
    "viaplay": "/zenders/viaplay", "f1tv": "/zenders/f1-tv", "unibet": "/bookmakers/unibet",
}
KSA = "<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"
RUBRIEK = "673cb057713facd07c37844b"   # Formule 1
