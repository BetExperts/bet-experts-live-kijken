# -*- coding: utf-8 -*-
"""Los artikel: Suns – Nuggets voorspelling, NBA 31 oktober 2026 (03:00 NL, wintertijd; vrijdag 19:00 in Arizona),
Mortgage Matchup Center Phoenix. Feiten nagelopen op 30-10-2026 rond 13:50 NL (ESPN-API: summary 401909286 incl.
blessures; boxscores 2026/27 401909841 (Blazers – Suns 124-83), 401909860 (Suns – Warriors 131-122), 401909873
(Thunder – Suns 125-114), 401909094 (Thunder – Nuggets 96-84), 401909859 (Nuggets – Pelicans 141-135 n.v.), 401909876
(Nuggets – Warriors 114-134), 401909889 (Pelicans – Nuggets 91-104); teamschema's 2025/26 (regulier, play-in,
play-offs) en 2026/27; stand West 2025/26; rosters en coaches; spelersgemiddelden 2025/26; onderlinge duels 2025/26
401809959 (DEN – PHX 133-111), 401810154 (PHX – DEN 112-130), 401810905 (PHX – DEN 123-125); officiële NBA-blessurelijst
30-10 06:00 ET; selectiewijzigingen zoals eerder nagelopen in thunder_nuggets, suns_warriors en thunder_suns).
- Blessurelijst 30-10 06:00 ET: PHX Mark Williams out (operatie linkerschouder), Ighodaro questionable (rechter
  schuine buikspier), Timme out (G League). DEN Spencer Jones out (hamstrings), Strawther out (linkerknie),
  Cameron Johnson questionable (rechterenkel; miste de laatste drie duels), Diallo questionable (persoonlijk).
  NB: ESPN (±13:30 NL) en de opdracht noemen Johnson en Diallo 'out'; wij volgen de officiële lijst (twijfelachtig).
- Rust: Phoenix speelde maandag 26-10 (US) voor het laatst (drie rustdagen); Denver woensdag 28-10 in New Orleans.
  Het feitenblad zegt dat alle ploegen woensdag speelden; dat klopt niet voor Phoenix.
- Stand 2025/26: DEN 54-28 (nr. 3 West, 28-13/26-15, 122,1/116,9, ronde 1 2-4 tegen MIN); PHX 45-37 (nr. 7 West op
  record, 25-16/20-21, 112,6/111,1; play-in 110-114 POR, 111-96 GS; ronde 1 0-4 tegen OKC).
- Onderling 2025/26: 3-0 DEN (133-111 in Denver, 130-112 en 125-123 in Phoenix). Booker 31/24/22; Jokić 14-14-15,
  26-9-10 (7/7), 23-17-17.
- Odds: alleen TOTO, uit specials/nba_feiten_2026_10_31.md (vr ±13:45 NL). Winnaar, handicap, totaal incl. verlenging.
- Eén wedtip (vast, eigenaar): Denver Nuggets wint (incl. verlenging) @1,59, onze kans ±66% (odd 62,9%; zonder
  marge ±61%).
  python3 specials/suns_nuggets_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "Suns – Nuggets voorspelling: wedtip en odds voor Jokić tegen een lekke Suns-verdediging (31 oktober, 03:00)"
SLUG = "suns-nuggets-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("Suns – Nuggets voorspelling: Phoenix krijgt 123,7 punten per duel tegen, Denver won vorig seizoen "
                "alle drie de duels. Wedtip, TOTO-odds en blessures.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet-experts.nl/go/bet365"
DATUM = "2026-10-31T02:00:00.000Z"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>Suns – Nuggets voorspelling: in de nacht van vrijdag op zaterdag om 03:00 Nederlandse tijd ontvangt Phoenix de Denver Nuggets. De Suns staan op één zege en twee nederlagen en kregen in die drie wedstrijden gemiddeld 123,7 punten tegen. Denver (2-2) won vorig seizoen alle drie de onderlinge duels, twee daarvan in Phoenix. Bij de Suns ontbreekt center Mark Williams en is Oso Ighodaro twijfelachtig. Onze voorspelling: Suns – Nuggets 113-119. Onze wedtip: Denver Nuggets wint (inclusief verlenging) tegen een quotering van 1,59 bij TOTO.</strong></p>
<p>Hieronder lees je alles over vorm, blessures, de odds van <a href="/bookmakers/toto">TOTO</a> en onze onderbouwing.</p>
<h3><strong>Suns – Nuggets: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "Phoenix Suns – Denver Nuggets"),
    ("Datum", "Zaterdag 31 oktober 2026 (nacht van vrijdag op zaterdag)"),
    ("Aanvang", "03:00 Nederlandse tijd (vrijdag 19:00 in Phoenix)"),
    ("Arena", "Mortgage Matchup Center, Phoenix"),
    ("Competitie", "NBA, reguliere competitie 2026/27"),
    ("Stand 2026/27", "Suns 1-2, Nuggets 2-2"),
    ("Onderlinge duels 2025/26", "3-0 voor de Nuggets"),
])}
<p>Phoenix speelde maandag (Amerikaanse tijd) voor het laatst, in Oklahoma City, en had daarna drie dagen rust. Denver won woensdag in New Orleans en had donderdag een rustdag. Geen van beide ploegen speelt dus op de tweede avond van een back-to-back.</p>
<h3><strong>Het seizoen tot nu toe: veel punten tegen aan beide kanten</strong></h3>
<p><strong>Phoenix Suns: één zege, en veel gaten achterin</strong></p>
<p>Phoenix begon met een 83-124 nederlaag in Portland (6 raak uit 32 driepunters). Daarna volgde een 131-122 zege op een Golden State zonder Stephen Curry, Draymond Green en Brandin Podziemski, met 43 punten van Devin Booker. Maandag verloor Phoenix met 114-125 in Oklahoma City, tegen een Thunder die ook meerdere spelers miste. Booker had een zeldzaam slechte avond: 3 punten, 1 van de 7 uit het veld.</p>
<p><strong>Denver Nuggets: wisselvallig, maar een nette zege in New Orleans</strong></p>
<p>Denver opende met een 84-96 nederlaag in Oklahoma City. Thuis tegen New Orleans stond de ploeg na drie kwarten nog negentien punten achter, maar won na verlenging met 141-135, met 42 punten van Jamal Murray en een triple-double van Nikola Jokić. Daarna ging het thuis mis tegen Golden State (114-134). Woensdag herstelde Denver zich in New Orleans: 104-91, met 23 punten van Murray en opnieuw een triple-double van Jokić (21 punten, 13 rebounds, 10 assists).</p>
<h3><strong>Vorig seizoen en de onderlinge duels</strong></h3>
<p>Denver werd vorig seizoen derde in het Westen, maar ging in de eerste ronde van de play-offs met 2-4 onderuit tegen Minnesota. Phoenix eindigde als zevende, verloor in de play-in thuis van Portland (110-114) en plaatste zich daarna met 111-96 tegen Golden State. In de eerste ronde was Oklahoma City met 4-0 te sterk.</p>
{tabel(["2025/26", "Phoenix Suns", "Denver Nuggets"], [
    ("Eindstand", "45-37 (nr. 7 West)", "54-28 (nr. 3 West)"),
    ("Thuis / uit", "25-16 / 20-21", "28-13 / 26-15"),
    ("Punten voor / tegen", "112,6 / 111,1", "122,1 / 116,9"),
    ("Onderling", "0-3", "3-0"),
    ("Na het seizoen", "Via de play-in naar de eerste ronde (0-4 tegen Oklahoma City)", "Eerste ronde (2-4 tegen Minnesota)"),
])}
<p>Denver won alle drie de duels: 133-111 in oktober in Denver, 130-112 eind november in Phoenix (Jokić 26 punten, zeven uit zeven) en 123-125 eind maart, opnieuw in Phoenix, met 23 punten, 17 rebounds en 17 assists van Jokić. Booker scoorde 31, 24 en 22 punten. Miles Bridges zat toen nog niet bij Phoenix.</p>"""

content2 = f"""<h3><strong>Zo zijn beide selecties veranderd</strong></h3>
<p><strong>Phoenix Suns: Bridges en Kennard erbij</strong></p>
<p>Phoenix haalde deze zomer Miles Bridges uit Charlotte, in ruil voor Grayson Allen en Royce O'Neale. Ook schutter Luke Kennard is nieuw; hij speelde vorig seizoen voor Atlanta en de Lakers. Jordan Ott begint aan zijn tweede seizoen als coach. Center Mark Williams herstelt van een operatie aan zijn linkerschouder, waardoor de tweedejaars Khaman Maluach in de basis staat.</p>
<p><strong>Denver Nuggets: dezelfde kern, een nieuwe bank</strong></p>
<p>Coach David Adelman houdt de kern rond Jokić, Murray, Gordon en Christian Braun bij elkaar. Peyton Watson vertrok in een sign-and-trade naar Cleveland, Tim Hardaway Jr. tekende bij Miami en ook Jonas Valančiūnas en Bruce Brown zijn weg. De 37-jarige DeMar DeRozan kwam over van Sacramento. Ook Marvin Bagley III, Alpha Diallo en Trevon Brazile kwamen erbij.</p>
<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("Mark Williams", "Phoenix", "Speelt niet (operatie aan de linkerschouder)"),
    ("Oso Ighodaro", "Phoenix", "Twijfelachtig (rechter schuine buikspier)"),
    ("Drew Timme", "Phoenix", "Niet bij de ploeg (G League)"),
    ("Spencer Jones", "Denver", "Speelt niet (hamstrings)"),
    ("Julian Strawther", "Denver", "Speelt niet (verstuikte linkerknie)"),
    ("Cameron Johnson", "Denver", "Twijfelachtig (verstuikte rechterenkel)"),
    ("Alpha Diallo", "Denver", "Twijfelachtig (persoonlijke redenen)"),
])}
<p><em>Stand van de officiële NBA-blessurelijst op vrijdag 30 oktober, 06:00 uur Amerikaanse tijd (11:00 Nederlandse tijd).</em></p>
<p>Cameron Johnson verstuikte zijn enkel in de opener en miste daarna drie wedstrijden, net als Diallo. Booker, Jokić en Murray staan niet op de lijst.</p>
<p><strong>Verwachte basisvijf Suns:</strong> Devin Booker, Jalen Green, Dillon Brooks, Miles Bridges, Khaman Maluach. Zo begon Phoenix alle drie de wedstrijden. Collin Gillespie, Kennard en Jordan Goodwin komen van de bank.</p>
<p><strong>Verwachte basisvijf Nuggets:</strong> Jamal Murray, Christian Braun, Trevon Brazile, Aaron Gordon, Nikola Jokić. Zo begon Denver woensdag in New Orleans; in de twee duels daarvoor stond Bryce Hopkins op de plek van Brazile. DeRozan, Bagley en Tyus Jones komen van de bank.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "2026/27 tot nu toe"], [
    ("Nikola Jokić (DEN)", "27,7", "12,9", "10,7", "22,0 ptn, 10,5 reb, 9,0 ast"),
    ("Jamal Murray (DEN)", "25,4", "4,4", "7,1", "22,5 ptn, 47 procent driepunters"),
    ("Aaron Gordon (DEN)", "16,2", "5,8", "2,7", "12,3 ptn, 6,5 reb"),
    ("Devin Booker (PHX)", "26,1", "3,9", "6,0", "23,0 ptn (23, 43 en 3)"),
    ("Dillon Brooks (PHX)", "20,2", "3,6", "1,8", "14,7 ptn"),
    ("Jalen Green (PHX)", "17,8", "3,6", "2,8", "14,0 ptn"),
    ("Miles Bridges (PHX)", "17,1*", "5,8*", "3,2*", "13,7 ptn, 6,3 reb"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26. * Bridges: cijfers bij Charlotte. Green speelde vorig seizoen 32 wedstrijden, Gordon 36.</em></p>
<p><strong>Nikola Jokić</strong> is de sleutel: Phoenix heeft zonder Williams weinig lengte, en Maluach speelde vorig seizoen gemiddeld nog geen negen minuten. <strong>Devin Booker</strong> scoorde vorig seizoen gemiddeld bijna 26 punten tegen Denver. <strong>Jamal Murray</strong> maakte in de drie duels 23, 24 en 21 punten.</p>
<h3><strong>Odds Suns – Nuggets bij TOTO</strong></h3>
<p>TOTO ziet Denver als favoriet: een quotering van 1,59 staat voor ongeveer 63 procent winkans. De handicap ligt rond de 4 punten in het voordeel van de Nuggets, het verwachte puntentotaal rond de 231,5.</p>
{tabel(["Markt (TOTO)", "Suns", "Nuggets"], [
    ("Winnaar (incl. verlenging)", "2,45", "1,59"),
    ("1X2 (reguliere speeltijd, gelijk 18,00)", "2,50", "1,57"),
    ("Handicap +3,5 / -3,5 (incl. verlenging)", "1,87", "1,78"),
    ("Handicap +4,5 / -4,5 (incl. verlenging)", "1,87", "1,95"),
    ("Handicap +5,5 / -5,5 (incl. verlenging)", "1,69", "2,00"),
])}
<p>Op het totaal biedt TOTO 230,5 punten (Over 1,78 / Under 1,91), 231,5 (1,93 / 1,87) en 232,5 (Over 1,95 / Under 1,73). Odds gelezen op vrijdag rond 13:45 uur; vergelijk ze vlak voor de start nog even, zeker omdat de status van Cameron Johnson en Ighodaro de lijn kan verschuiven.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op Suns – Nuggets</strong></a></p>"""

content3 = f"""<h3><strong>Onze voorspelling: Denver wint in Phoenix</strong></h3>
<p>Denver heeft met Jokić en Murray de twee beste spelers op het veld en treft een ploeg die onder de ring kwetsbaar is.</p>
<p>Helemaal gerust zijn we niet. Denver verloor thuis met twintig punten van Golden State en liet ook tegen New Orleans 135 punten toe. Phoenix is uitgerust en speelt pas zijn tweede thuisduel. Maar de Nuggets lieten woensdag zien dat ze een wedstrijd ook met verdedigen kunnen winnen, en vorig seizoen was Denver drie keer de betere. Onze voorspelling: <strong>Phoenix Suns – Denver Nuggets 113-119</strong>.</p>
<h3><strong>Onze wedtip: Nuggets winnen (1,59)</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Onze kans"], [
    ("Denver Nuggets wint (incl. verlenging)", "1,59", "TOTO", "Ongeveer 66 procent"),
])}
<p><strong>Waarom deze tip?</strong> De tip is goed als Denver de wedstrijd wint, ook als dat pas na verlenging gebeurt. De marge maakt niet uit. Een odd van 1,59 staat voor een kans van 63 procent; zonder de marge van de bookmaker is dat ongeveer 61 procent. Wij schatten de kans op ongeveer 66 procent. De onderbouwing:</p>
<p><strong>1. Jokić tegen een Phoenix zonder lengte.</strong> Williams speelt niet, Ighodaro is twijfelachtig en Maluach heeft weinig ervaring. Vorig seizoen had Jokić tegen Phoenix twee triple-doubles en raakte hij in Phoenix al zijn zeven schoten. In twee van de drie duels scoorde Denver 58 punten of meer in de bucket.</p>
<p><strong>2. De verdediging van Phoenix lekt.</strong> De Suns kregen 124, 122 en 125 punten tegen, gemiddeld 123,7. Vorig seizoen was dat nog 111,1. Zelfs een Golden State zonder Curry, Green en Podziemski scoorde 122 punten in Phoenix.</p>
<p><strong>3. Denver wint ook uit.</strong> De Nuggets wonnen vorig seizoen 26 van hun 41 uitwedstrijden, en beide duels in Phoenix. Woensdag hield Denver New Orleans op 91 punten.</p>
<p><strong>Waarom niet een andere markt?</strong> Nuggets -4,5 (1,95) betaalt meer uit, maar in maart won Denver in Phoenix met maar twee punten verschil, en onze voorspelde marge van zes punten ligt dicht bij die lijn. De 1X2-markt (1,57) betaalt minder en telt een verlenging niet mee. Het puntentotaal laten we liggen: onze voorspelling komt uit op 232 punten, vrijwel gelijk aan de lijn van TOTO.</p>
<p><strong>Het risico.</strong> Denver kreeg zelf ook veel punten tegen (gemiddeld 114) en mist met Cameron Johnson waarschijnlijk een vaste schutter. Phoenix had drie rustdagen, Denver één. En Booker liet met 43 punten tegen Golden State zien dat hij een wedstrijd in zijn eentje kan kantelen. Let op: de winnaarsmarkt telt een eventuele verlenging mee. Meer uitleg vind je in onze gidsen over <a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">de money line</a> en <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap wedden</a>.</p>
<h3><strong>Suns – Nuggets live kijken in Nederland</strong></h3>
<p>Bij <a href="/bookmakers/bet365">Bet365</a> kun je NBA-wedstrijden live volgen via de livestream. Je hebt daarvoor een account met een storting nodig. ESPN zendt in Nederland een deel van de NBA-wedstrijden uit; in de programmagids zie je of deze erbij zit. Met <strong>NBA League Pass</strong>, de betaalde dienst van de competitie, kun je alle wedstrijden volgen. Meer opties vind je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk Suns – Nuggets live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Vannacht schreven we ook voorbeschouwingen van <a href="/nieuws/76ers-knicks-voorspelling-wedtips-nba-2026">76ers – Knicks</a>, <a href="/nieuws/mavericks-rockets-voorspelling-wedtips-nba-2026">Mavericks – Rockets</a> en <a href="/nieuws/warriors-lakers-voorspelling-wedtips-nba-2026">Warriors – Lakers</a>, dat net als deze wedstrijd om 03:00 begint. Eerder dit seizoen schreven we over <a href="/nieuws/suns-warriors-voorspelling-wedtips-nba-2026">Suns – Warriors</a> en <a href="/nieuws/nuggets-warriors-voorspelling-wedtips-nba-2026">Nuggets – Warriors</a>. Benieuwd <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">welke Nederlanders in de NBA spelen</a>? Nieuw met basketbal? Lees <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels in de NBA</a>. Alle tips staan op <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Suns – Nuggets?</strong><br>Zaterdag 31 oktober 2026 om 03:00 Nederlandse tijd, in de nacht van vrijdag op zaterdag. In Phoenix is het dan vrijdagavond 19:00.</p>
<p><strong>Speelt Nikola Jokić mee?</strong><br>Ja, Jokić staat niet op de officiële NBA-blessurelijst. Bij Denver zijn Cameron Johnson en Alpha Diallo twijfelachtig; bij Phoenix ontbreekt Mark Williams.</p>
<p><strong>Wie is favoriet: Suns of Nuggets?</strong><br>De Nuggets, met een quotering van 1,59 bij TOTO. Phoenix staat op 2,45.</p>
<p><strong>Wat is onze voorspelling voor Suns – Nuggets?</strong><br>Denver wint met 113-119. Onze wedtip is Denver Nuggets wint, inclusief verlenging (1,59 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

KAART = {"home": "Suns", "away": "Nuggets", "home_abbr": "phx", "away_abbr": "den", "home_pos": "45-37 · nr. 7 West 2025/26", "away_pos": "54-28 · nr. 3 West 2025/26", "hs": 113, "as": 119, "datum": "Za 31 okt", "tijd": "03:00", "odd_home": "2,45", "odd_away": "1,59"}
WEDTIPS = {"wedtip-1-2": "Denver Nuggets wint (incl. verlenging)", "quotering-wedtip-1": "1.59",
           "bookmaker-wedtips": "669ab9f5aceb8b717cea24c3"}

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_BASKETBAL, "competitie": COMPETITIE_NBA,
          "datum-tijd-van-wedstrijd": DATUM,
          "publicatiedatum": datetime.now(timezone.utc).isoformat(), **WEDTIPS}
    # Alleen dry run: dit script publiceert niets.
    import re
    html = content + content2 + content3
    # Opmaak
    assert not re.search(r"<h[1245]", html), "alleen h3 gebruiken"
    assert all(m.startswith("<h3><strong>") for m in re.findall(r"<h3>.{0,8}", html)), "h3 altijd met strong"
    assert content.startswith("<p><strong>"), "vetgedrukte intro"
    assert not re.search(r"<(ul|ol|li)\b", html) or not re.search(r"(</?(ul|ol|li)>)\s+(?=<)", html), "witruimte in lijsten"
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"), "slotregel"
    hrefs = re.findall(r'href="([^"]+)"', html)
    assert hrefs and all(h.startswith("/") or h == BET365 for h in hrefs), [h for h in hrefs if not h.startswith("/")]
    # Toegestane links: alleen uit het feitenblad (lijst 'Bestaande artikelen' + slugs vannacht)
    toegestaan = {"/nieuws/nba-voorspellingen-vannacht-29-oktober-2026",
                  "/nieuws/pacers-76ers-voorspelling-wedtips-nba-2026",
                  "/nieuws/bucks-rockets-voorspelling-wedtips-nba-2026",
                  "/nieuws/mavericks-thunder-voorspelling-wedtips-nba-2026",
                  "/nieuws/clippers-lakers-voorspelling-wedtips-nba-2026",
                  "/nieuws/lakers-warriors-voorspelling-wedtips-nba-2026",
                  "/nieuws/thunder-nuggets-voorspelling-wedtips-nba-2026",
                  "/nieuws/knicks-pistons-voorspelling-wedtips-nba-2026",
                  "/nieuws/76ers-pistons-voorspelling-wedtips-nba-2026",
                  "/nieuws/heat-mavericks-voorspelling-wedtips-nba-2026",
                  "/nieuws/rockets-hawks-voorspelling-wedtips-nba-2026",
                  "/nieuws/suns-warriors-voorspelling-wedtips-nba-2026",
                  "/nieuws/nuggets-warriors-voorspelling-wedtips-nba-2026",
                  "/nieuws/76ers-knicks-voorspelling-wedtips-nba-2026",
                  "/nieuws/mavericks-rockets-voorspelling-wedtips-nba-2026",
                  "/nieuws/warriors-lakers-voorspelling-wedtips-nba-2026",
                  "/nieuws/welke-nederlanders-spelen-in-de-nba",
                  "/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders",
                  "/nieuws/wat-is-handicap-wedden-de-complete-gids",
                  "/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners",
                  "/wedden-op-nba-voorspellingen-en-wedtips---basketbal", "/bookmakers/toto", "/bookmakers/bet365",
                  "/live-kijken", BET365}
    assert set(hrefs) <= toegestaan, set(hrefs) - toegestaan
    assert SLUG not in "".join(hrefs), "niet naar zichzelf linken"
    for s in ("76ers-knicks", "mavericks-rockets", "warriors-lakers"):
        assert f"/nieuws/{s}-voorspelling-wedtips-nba-2026" in hrefs, f"link naar {s} ontbreekt"
    assert "/nieuws/suns-warriors-voorspelling-wedtips-nba-2026" in hrefs, "eerder artikel Suns"
    assert "/nieuws/nuggets-warriors-voorspelling-wedtips-nba-2026" in hrefs, "eerder artikel Nuggets"
    assert "nba-voorspellingen-vannacht" not in "".join(hrefs), "geen algemeen artikel vannacht"
    assert "<table" not in html.replace(f"<table {T}>", ""), "tabellen alleen via tabel()"
    verboden = ["BetCity", "ESPN-API", "ESPN.com", "Associated Press", "DraftKings", "Rotowire", "Betfans", "Shams",
                "Klutch", "Charania", "CBS", "Field Level"]
    assert not any(v.lower() in html.lower() for v in verboden), "geen bronnen/concurrenten"
    assert "kampioen" not in html.lower() and "titelhouder" not in html.lower(), "geen ongecontroleerde kwalificaties"
    # SEO: focuskeyword
    fk = "Suns – Nuggets voorspelling"
    assert fk in TITEL and fk in SAMENVATTING and len(SAMENVATTING) <= 160, len(SAMENVATTING)
    assert re.sub(r"<[^>]+>", "", content).startswith(fk), "focuskeyword in de eerste zin"
    assert any("Suns – Nuggets" in h for h in re.findall(r"<h3>(.*?)</h3>", html))
    assert "31 oktober, 03:00" in TITEL
    # Wedtip en consistentie
    assert set(WEDTIPS) == {"wedtip-1-2", "quotering-wedtip-1", "bookmaker-wedtips"}
    assert WEDTIPS["bookmaker-wedtips"] == "669ab9f5aceb8b717cea24c3"
    q = float(WEDTIPS["quotering-wedtip-1"])
    toto_odds = {2.45, 1.59, 2.50, 1.57, 1.87, 1.78, 1.95, 1.69, 2.00, 1.91, 1.93, 1.73}
    assert q in toto_odds and q == 1.59
    assert "incl. verlenging" in WEDTIPS["wedtip-1-2"]
    assert KAART["as"] > KAART["hs"], "voorspelde score moet 'Denver Nuggets wint' laten winnen"
    assert f"{KAART['hs']}-{KAART['as']}" in content and f"{KAART['hs']}-{KAART['as']}" in content3
    assert KAART["odd_home"] == "2,45" and KAART["odd_away"] == "1,59" and KAART["tijd"] == "03:00"
    assert KAART["home_abbr"] == "phx" and KAART["away_abbr"] == "den" and KAART["datum"] == "Za 31 okt"
    assert KAART["home"] == "Suns" and KAART["away"] == "Nuggets"
    assert "1,59" in content and "1,59" in content3 and "inclusief verlenging" in content
    assert "vrijdag rond 13:45 uur" in html, "tijdstip odds"
    assert html.count("👉 Klik hier: maak je Bet365-account aan en wed live mee op") == 1
    assert len(re.findall(r"<p><strong>[123]\. ", content3)) == 3, "onderbouwing in 3 punten"
    assert "Waarom niet een andere markt?" in content3
    assert len(re.findall(r"<p><strong>[^<]*\?</strong><br>", content3)) == 4, "FAQ: 4 vragen"
    assert SLUG == "suns-nuggets-voorspelling-wedtips-nba-2026" and DATUM == "2026-10-31T02:00:00.000Z"
    tekst = re.sub(r"<[^>]+>", " ", html)
    woorden = len(tekst.split())
    assert 1400 <= woorden <= 1850, woorden
    print(len(TITEL), "tekens titel |", len(SAMENVATTING), "tekens samenvatting |", woorden, "woorden")
    print("Alle asserts geslaagd (dry run, niets gepubliceerd).")
