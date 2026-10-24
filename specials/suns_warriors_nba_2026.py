# -*- coding: utf-8 -*-
"""Los artikel: Suns – Warriors voorspelling, NBA 25 oktober 2026 (03:00 NL, wintertijd). Feiten nagelopen op 24-10-2026
rond 13:00 NL (ESPN-API: summary 401909860, boxscores 401909841 en 401909850, scoreboards 21/23/24-10, rosters,
schema's en spelersgemiddelden 2025/26 incl. play-in; officiele NBA-blessurelijst 24-10 06:45 ET, Warriors nog
'not yet submitted'; berichtgeving na Warriors-Grizzlies over Curry ("Probably not, but I'll talk to the staff") en
Podziemski (zegt zelf niet te spelen); ruil Bridges-Allen/O'Neale (28-6, officieel 13-7-2026)).
- Suns-Blazers 83-124 (Booker 23, 6/32 driepunters); Warriors-Grizzlies 108-111 (Curry 24, Podziemski en Lendeborg 18).
- 2025/26: Suns 45-37 (7e West op record, play-in: 110-114 tegen POR, 111-96 tegen GSW, daarna 0-4 tegen OKC);
  Warriors 37-45 (10e). Onderling 3-1 Warriors; totalen 225, 197, 235, 198 en play-in 207.
- Leons: two-way bij GSW (dec. 2025, ESPN-roster 2026/27), 9 min in de opener, DNP tegen Memphis.
- Odds: alleen TOTO, uit specials/nba_feiten_2026_10_25.md (±12:50 NL op 24-10).
  ../superodd-agent/.venv/bin/python specials/suns_warriors_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "Suns – Warriors voorspelling: wedtip en odds zonder Curry? (25 oktober, 03:00)"
SLUG = "suns-warriors-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("Phoenix ontvangt Golden State, dat op een back-to-back waarschijnlijk zonder Stephen Curry speelt. "
                "Voorspelling, wedtip, odds en blessures.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet-experts.nl/go/bet365"
DATUM = "2026-10-25T02:00:00.000Z"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>In de nacht van zaterdag op zondag om 03:00 uur Nederlandse tijd (wintertijd: om 03:00 gaat de klok een uur terug) ontvangen de Phoenix Suns de Golden State Warriors. Beide ploegen wachten nog op hun eerste zege. De Warriors spelen de tweede avond van een back-to-back en doen dat waarschijnlijk zonder Stephen Curry en volgens eigen zeggen ook zonder Brandin Podziemski. Onze voorspelling: de Suns winnen met 112-101. Onze wedtip: minder dan 218,5 punten (1,93 bij TOTO).</strong></p>
<p>Phoenix ging in Portland met 41 punten verschil onderuit, Golden State gaf vrijdag tegen Memphis in de slotminuten een flinke voorsprong weg. Daarna liet Curry doorschemeren dat hij in Phoenix waarschijnlijk rust neemt. Mede daarom staan de Suns op 1,26. Hieronder lees je wie er ontbreekt, wat de odds zijn en waarom wij op weinig punten rekenen.</p>
<h3><strong>Suns – Warriors: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "Phoenix Suns – Golden State Warriors"),
    ("Datum", "Zondag 25 oktober 2026 (nacht van zaterdag op zondag)"),
    ("Aanvang", "03:00 uur Nederlandse tijd, wintertijd (zaterdag 19:00 in Phoenix)"),
    ("Arena", "Mortgage Matchup Center, Phoenix"),
    ("Competitie", "NBA, reguliere competitie 2026/27"),
    ("Stand 2026/27", "Suns 0-1, Warriors 0-2"),
    ("Onderlinge duels 2025/26", "3-1 voor de Warriors (plus een play-inzege voor Phoenix)"),
])}
<p>Let op de klok: in deze nacht gaat Nederland over op de wintertijd, en de wedstrijd begint om 03:00 wintertijd. De Suns hadden donderdag en vrijdag rust; de Warriors speelden vrijdagnacht nog thuis in San Francisco.</p>
<h3><strong>Het seizoen tot nu toe: 0-3 samen</strong></h3>
<p><strong>Phoenix Suns: zware start in Portland</strong></p>
<p>De Suns verloren hun opener met 83-124 van de Trail Blazers. Phoenix raakte maar 6 van zijn 32 driepunters (19 procent). Devin Booker scoorde 23 punten in 29 minuten, maar verder kwam niemand boven de tien. Collin Gillespie, vorig seizoen goed voor 40 procent van achter de lijn, miste al zijn acht pogingen.</p>
<p><strong>Golden State Warriors: twee nederlagen en een back-to-back</strong></p>
<p>Golden State verloor de opener met 105-127 bij de Lakers. Curry scoorde 23 punten in 21 minuten, maar de ploeg raakte maar 8 van de 36 driepunters. Vrijdag stonden de Warriors in de laatste vier minuten nog twaalf punten voor tegen Memphis, maar na een reeks van 17-0 won Memphis met 108-111. Curry had 24 punten (5 uit 15), Podziemski en rookie Yaxel Lendeborg scoorden er allebei 18.</p>
<h3><strong>Vorig seizoen: de Warriors gingen er in Phoenix uit</strong></h3>
<p>De Suns eindigden in 2025/26 met 45-37 als zevende in het Westen. In de play-in verloren ze thuis van Portland (110-114), maar drie dagen later wonnen ze, weer thuis, met 111-96 van Golden State. Jalen Green scoorde toen 36 punten. In de eerste ronde was Oklahoma City met 4-0 te sterk.</p>
{tabel(["2025/26", "Phoenix Suns", "Golden State Warriors"], [
    ("Eindstand", "45-37 (nr. 7 West)", "37-45 (nr. 10 West)"),
    ("Thuis / uit", "25-16 / 20-21", "22-19 / 15-26"),
    ("Punten voor / tegen", "112,6 / 111,1", "114,6 / 115,2"),
    ("Na het seizoen", "Via de play-in naar de eerste ronde (0-4 tegen OKC)", "Uitgeschakeld in de play-in, in Phoenix"),
])}
<p>In de reguliere competitie won Golden State drie van de vier duels: 118-107 en 119-116 thuis, 101-97 in Phoenix. De Suns wonnen thuis met 99-98. De vijf duels eindigden op 225, 197, 235, 198 en 207 punten.</p>"""

content2 = f"""<h3><strong>Blessures: waarom de Suns op 1,26 staan</strong></h3>
<p>Na de nederlaag tegen Memphis zei Curry dat hij zaterdag waarschijnlijk niet speelt, al overlegt hij nog met de medische staf. Coach Steve Kerr wil de speeltijd van de 38-jarige het hele seizoen bewaken. Podziemski (rug) zei zelf al dat hij niet speelt. De Warriors hadden zaterdagmiddag hun officiële blessurelijst nog niet ingediend.</p>
{tabel(["Speler", "Team", "Status"], [
    ("Stephen Curry", "Golden State", "Waarschijnlijk niet (rust op de tweede avond van een back-to-back)"),
    ("Brandin Podziemski", "Golden State", "Speelt naar eigen zeggen niet (rug)"),
    ("Jimmy Butler", "Golden State", "Speelt niet (herstel van kruisbandblessure)"),
    ("Moses Moody", "Golden State", "Speelt niet (herstel van knieblessure)"),
    ("Kristaps Porziņģis", "Golden State", "Speelt niet (niet bij de ploeg, gezondheid)"),
    ("Charles Bassey", "Golden State", "Miste vrijdag (knie)"),
    ("Mark Williams", "Phoenix", "Speelt niet (operatie aan de linkerschouder)"),
    ("Oso Ighodaro", "Phoenix", "Zeer twijfelachtig (schuine buikspier)"),
    ("Luke Kennard", "Phoenix", "Twijfelachtig (linkerknie)"),
])}
<p><em>Stand van de officiële NBA-blessurelijst op zaterdag 24 oktober, 12:45 Nederlandse tijd. De status van Curry en Podziemski is gebaseerd op hun eigen uitspraken; de officiële melding van de Warriors volgt later.</em></p>
<p><strong>Verwachte basisvijf Suns:</strong> Devin Booker, Jalen Green, Dillon Brooks, Miles Bridges, Khaman Maluach. Dezelfde vijf als in Portland. Zonder Williams en Ighodaro doen Maluach en Duop Reath het werk onder de ring.</p>
<p><strong>Verwachte spelers Warriors:</strong> Draymond Green, Lendeborg en Al Horford krijgen veel minuten; De'Anthony Melton, Brandon Williams en Gary Payton II moeten de twee guards vervangen. Kerr maakt zijn basisvijf pas kort voor de wedstrijd bekend.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "Bijzonderheid"], [
    ("Devin Booker (PHX)", "26,1", "3,9", "6,0", "Twee keer 38 punten tegen Golden State vorig seizoen"),
    ("Jalen Green (PHX)", "17,8", "3,6", "2,8", "36 punten in de play-in tegen de Warriors"),
    ("Dillon Brooks (PHX)", "20,2", "3,6", "1,8", "Twee keer 24 punten tegen Golden State"),
    ("Miles Bridges (PHX)", "17,1", "5,8", "3,2", "Cijfers bij Charlotte, deze zomer geruild"),
    ("Yaxel Lendeborg (GSW)", "15,0", "8,0", "4,0", "Rookie, cijfers uit zijn eerste twee duels"),
    ("Draymond Green (GSW)", "8,4", "5,5", "5,5", "Gemiddeld 7 assists dit seizoen"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26 (Lendeborg: 2026/27).</em></p>
<p>Phoenix haalde Bridges deze zomer uit Charlotte, in ruil voor Grayson Allen en Royce O'Neale. Bij Golden State valt zonder Curry veel op de schouders van Lendeborg, de nummer elf van de draft.</p>
<h3><strong>Odds Suns – Warriors bij TOTO</strong></h3>
<p>TOTO ziet de Suns als grote favoriet: een quotering van 1,26 staat voor ongeveer 79 procent kans. De handicap ligt rond 9,5 punten en het puntentotaal op 218,5, laag voor de NBA.</p>
{tabel(["Markt", "Suns", "Warriors"], [
    ("Winnaar (incl. verlenging)", "1,26", "4,05"),
    ("1X2 (reguliere speeltijd, gelijk 20,00)", "1,23", "4,25"),
    ("Handicap -8,5 / +8,5", "1,69", "2,00"),
    ("Handicap -9,5 / +9,5", "1,87", "1,95"),
    ("Handicap -10,5 / +10,5", "1,91", "1,77"),
])}
<p>Op het totaal biedt TOTO 218,5 punten (Over 1,87 / Under 1,93) en 219,5 punten (Over 1,91 / Under 1,77). Odds gelezen op zaterdag rond 12:50 uur; vergelijk ze vlak voor de start nog even, zeker zodra de Warriors hun blessurelijst bekendmaken.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op Suns – Warriors</strong></a></p>"""

content3 = f"""<h3><strong>Onze voorspelling: Suns winnen een wedstrijd met weinig punten</strong></h3>
<p>Phoenix heeft alles mee: twee rustdagen, een thuiswedstrijd en een tegenstander die vrijdagnacht nog speelde en zijn twee belangrijkste guards mist. Toch verwachten we geen walk-over. Green en Horford zijn ervaren, vorig seizoen won Golden State drie van de vier duels en Phoenix heeft zelf problemen onder de ring. Onze voorspelling: <strong>Phoenix Suns – Golden State Warriors 112-101</strong>.</p>
<h3><strong>Onze wedtip voor Suns – Warriors</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Onze kans"], [
    ("Minder dan 218,5 punten (incl. verlenging)", "1,93", "TOTO", "57 procent"),
])}
<p><strong>Minder dan 218,5 punten (1,93).</strong> De quotering staat voor zo'n 52 procent kans, wij schatten die op 57 procent. Onze voorspelling komt uit op 213 punten. Vier redenen:</p>
<ul><li><strong>Wie scoort er bij Golden State?</strong> Curry en Podziemski waren vorig seizoen samen goed voor 40,4 punten per wedstrijd. Al in de opener, toen van die twee alleen Podziemski ontbrak, raakte Golden State maar 22 procent van zijn driepunters.</li><li><strong>Vermoeide benen.</strong> Golden State speelt de tweede wedstrijd in twee avonden, met een vlucht ertussen. Dat zie je meestal het eerst aan de schoten van afstand.</li><li><strong>De onderlinge duels.</strong> Drie van de vijf wedstrijden tussen deze ploegen bleven vorig seizoen onder deze lijn: 197, 198 en 207 punten. De twee duels die erover gingen (225 en 235) waren wedstrijden waarin Curry 28 en Booker 38 punten maakte. In het duel van februari, zonder allebei, vielen er maar 198 punten.</li><li><strong>Phoenix scoort ook niet makkelijk.</strong> De Suns maakten in Portland maar 83 punten en gaven vorig seizoen gemiddeld 111,1 punten per wedstrijd weg, minder dan de Warriors (115,2). Een thuisploeg die ruim voorstaat, haalt bovendien vaak het tempo eruit.</li></ul>
<p><strong>Het risico.</strong> Speelt Curry tóch, dan kan hij het totaal in zijn eentje opdrijven. En een beslist slotkwart wordt soms een schietfestijn van wisselspelers. Daarom zetten we de kans op 57 procent en niet hoger.</p>
<p>Waarom niet op de winnaar of de handicap? De Suns staan op 1,26, onder onze grens van 1,40, en voor de handicap van 9,5 punten zien we te weinig verschil tussen de quotering en onze eigen inschatting.</p>
<h3><strong>Suns – Warriors live kijken in Nederland</strong></h3>
<p>De makkelijkste manier: bij <a href="/bookmakers/bet365">Bet365</a> kijk je NBA-wedstrijden gratis live. Je hebt alleen een account met een kleine storting nodig, en die storting kun je daarna gewoon weer opnemen. ESPN heeft in Nederland de NBA-rechten, maar zendt maar een deel van de wedstrijden uit; check vooraf de gids. Met <strong>NBA League Pass</strong>, de betaalde streamingdienst van de competitie, volg je alle wedstrijden. Meer opties vind je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk Suns – Warriors live</strong></a></p>
<h3><strong>Een Nederlander bij Golden State</strong></h3>
<p>Malevy Leons heeft een two-waycontract bij de Warriors. In de opener tegen de Lakers speelde hij 9 minuten; vrijdag tegen Memphis kwam hij niet in actie. Op de blessurelijst van vrijdag stond hij niet. Met zoveel afwezigen is de kans op minuten groter dan normaal. Lees meer in ons overzicht <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">welke Nederlanders in de NBA spelen</a>.</p>
<h3><strong>Meer NBA</strong></h3>
<p>Lees ook onze voorspellingen voor <a href="/nieuws/lakers-warriors-voorspelling-wedtips-nba-2026">Lakers – Warriors</a>, <a href="/nieuws/spurs-rockets-voorspelling-wedtips-nba-2026">Spurs – Rockets</a>, <a href="/nieuws/pacers-mavericks-voorspelling-wedtips-nba-2026">Pacers – Mavericks</a> en <a href="/nieuws/76ers-cavaliers-voorspelling-wedtips-nba-2026">76ers – Cavaliers</a>, plus de <a href="/nieuws/nba-voorspellingen-vannacht-24-oktober-2026">NBA-voorspellingen van 24 oktober</a>. Nieuw met wedden op basketbal? Lees <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels in de NBA</a> en <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">wat handicap wedden is</a>. Alle basketbaltips vind je op <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Suns – Warriors?</strong><br>Zondag 25 oktober 2026 om 03:00 uur Nederlandse tijd (wintertijd), in de nacht van zaterdag op zondag. In Phoenix is het dan zaterdagavond 19:00.</p>
<p><strong>Speelt Stephen Curry tegen de Suns?</strong><br>Waarschijnlijk niet. Hij zei na de nederlaag tegen Memphis dat hij waarschijnlijk rust neemt; de medische staf beslist. Ook Brandin Podziemski (rug) speelt niet.</p>
<p><strong>Wie is favoriet: Suns of Warriors?</strong><br>De Suns, met een quotering van 1,26 bij TOTO. De Warriors staan op 4,05.</p>
<p><strong>Wat is onze voorspelling voor Suns – Warriors?</strong><br>De Suns winnen met 112-101. Onze wedtip is minder dan 218,5 punten (1,93 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

KAART = {"home": "Suns", "away": "Warriors", "home_abbr": "phx", "away_abbr": "gs", "home_pos": "45-37 · nr. 7 West 2025/26", "away_pos": "37-45 · nr. 10 West 2025/26", "hs": 112, "as": 101, "datum": "Zo 25 okt", "tijd": "03:00", "odd_home": "1,26", "odd_away": "4,05"}
WEDTIPS = {"wedtip-1-2": "Minder dan 218,5 punten (incl. verlenging)", "quotering-wedtip-1": "1.93",
           "bookmaker-wedtips": "669ab9f5aceb8b717cea24c3"}

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_BASKETBAL, "competitie": COMPETITIE_NBA,
          "datum-tijd-van-wedstrijd": DATUM,
          "publicatiedatum": datetime.now(timezone.utc).isoformat(), **WEDTIPS}
    # Alleen dry run: dit script publiceert niets.
    import re
    tekst = re.sub(r"<[^>]+>", " ", content + content2 + content3)
    print(len(TITEL), "tekens titel |", len(SAMENVATTING), "tekens samenvatting |", len(tekst.split()), "woorden")
