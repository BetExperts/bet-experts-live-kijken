# -*- coding: utf-8 -*-
"""Los artikel: Cavaliers – Timberwolves voorspelling, NBA 27 oktober 2026 (00:00 NL, wintertijd; ma 19:00 ET),
Rocket Mortgage FieldHouse Cleveland. Feiten nagelopen op 26-10-2026 (ESPN-API: summary 401909869, box scores
401909093, 401909854, 401909864, 401909091, 401909845, play-offduels 2026 van Minnesota, teamschema's 2025/26 en
2026/27, rosters en coaches, standen 2025/26, spelersgemiddelden, onderlinge duels 2025/26 (401810385, 401810397);
officiële NBA-blessurelijst 26-10 07:30 ET (Minnesota nog niet ingediend); selectiewijzigingen uit de eerder
nagelopen artikelen 76ers – Cavaliers (22-10) en het feitenblad van 26-10).
- Cavs: 106-114 in Philadelphia (rust 69-45, grootste voorsprong 29, tweede helft 37-69, 21 balverliezen),
  125-121 tegen Brooklyn (voorsprong tot 22, vierde kwart 29-41, 23 balverliezen). Harden 6 uit 20.
- Wolves: 131-106 in Miami, 115-93 in Orlando, 117-94 tegen Toronto (zonder Kawhi Leonard; Edwards 26 min, Ball 17 min).
- Onderling 2025/26: 131-122 in Minneapolis (8-1-2026 US), 146-134 in Cleveland (10-1-2026), 1-1.
- Back-to-back: Wolves speelden zondag (US) thuis, Cavs zaterdag. 2025/26 tweede avond b2b Wolves 8-6, uit 2-4 (eigen telling).
- Odds: alleen TOTO, uit specials/nba_feiten_2026_10_27.md (ma ±12:45 NL). Winnaar, handicap en totaal incl. verlenging.
- Eén wedtip (eis eigenaar): Timberwolves +3,5 @1,91, onze kans 56% (markt 52,4%, zonder marge ±50%).
  python3 specials/cavaliers_timberwolves_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "Cavaliers – Timberwolves voorspelling: wedtip en odds voor ongeslagen Wolves op back-to-back (27 oktober, 00:00)"
SLUG = "cavaliers-timberwolves-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("De ongeslagen Wolves spelen een dag na hun thuiszege in Cleveland, tegen uitgeruste Cavs. Voorspelling, "
                "onze wedtip, TOTO-odds, blessures en opstellingen.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet-experts.nl/go/bet365"
DATUM = "2026-10-26T23:00:00.000Z"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>In de nacht van maandag op dinsdag om 00:00 Nederlandse tijd spelen de Cleveland Cavaliers thuis tegen de Minnesota Timberwolves. De Wolves zijn na drie wedstrijden nog ongeslagen en wonnen met gemiddeld 23 punten verschil, maar ze speelden zondag ook al en moeten het nog altijd zonder Donte DiVincenzo doen. Cleveland staat op één zege en één nederlaag en had zondag rust. Onze voorspelling: Cavaliers – Timberwolves 116-114. Onze wedtip: Minnesota Timberwolves +3,5 punten (inclusief verlenging) tegen een quotering van 1,91 bij TOTO.</strong></p>
<p>Hieronder lees je alles over de vorm, de blessures, de odds van <a href="/bookmakers/toto">TOTO</a> en onze onderbouwing.</p>
<h3><strong>Cavaliers – Timberwolves: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "Cleveland Cavaliers – Minnesota Timberwolves"),
    ("Datum", "Dinsdag 27 oktober 2026 (nacht van maandag op dinsdag)"),
    ("Aanvang", "00:00 Nederlandse tijd (maandag 19:00 in Cleveland)"),
    ("Arena", "Rocket Mortgage FieldHouse, Cleveland"),
    ("Competitie", "NBA, reguliere competitie 2026/27"),
    ("Stand 2026/27", "Cavaliers 1-1, Timberwolves 3-0"),
    ("Onderlinge duels 2025/26", "1-1"),
])}
<p>Nederland staat sinds zondag op wintertijd, in de Verenigde Staten gaat de klok pas op 1 november terug. Daarom is het verschil met Cleveland deze week vijf uur. Minnesota speelde zondagavond thuis tegen Toronto en staat dus voor de tweede avond van een back-to-back. Cleveland speelde zaterdag en had zondag een rustdag.</p>
<h3><strong>De eerste week: Wolves walsen, Cavs morsen voorsprongen</strong></h3>
<p><strong>Minnesota Timberwolves: drie ruime zeges</strong></p>
<p>De Wolves openden met 131-106 in Miami, waar Anthony Edwards 45 punten maakte met negen driepunters. Daarna volgden 115-93 in Orlando en zondag 117-94 tegen Toronto, in de eerste thuiswedstrijd van het seizoen. Tegen de Raptors liep Minnesota uit tot 32 punten voorsprong; Edwards (26 punten) speelde maar 26 minuten, LaMelo Ball 17. Een kanttekening: Miami staat op 0-3 en Toronto miste Kawhi Leonard met een gezwollen knie. Toch kreeg Minnesota gemiddeld maar 97,7 punten tegen.</p>
<p><strong>Cleveland Cavaliers: twee keer een grote voorsprong weggegeven</strong></p>
<p>In Philadelphia stond Cleveland bij rust met 69-45 voor, maar de tweede helft ging met 37-69 verloren: 106-114. Zaterdag tegen Brooklyn liep de voorsprong op tot 22 punten, waarna de Nets het vierde kwart met 41-29 wonnen. Cleveland hield net stand: 125-121. Donovan Mitchell (32 en 22 punten) en Jarrett Allen, die 13 van zijn 18 schoten raak gooide, zijn goed begonnen. James Harden niet: hij raakte 6 van zijn 20 schoten en verloor de bal 10 keer. Als ploeg kwam Cleveland in twee duels aan 44 balverliezen.</p>
<h3><strong>Vorig seizoen en de onderlinge duels</strong></h3>
<p>Cleveland werd vierde in het Oosten en won in de play-offs twee keer een zevende wedstrijd, tegen Toronto en Detroit. In de finale van het Oosten was New York met 4-0 te sterk. Minnesota werd zesde in het Westen, schakelde Denver uit (4-2) en verloor in de tweede ronde met 2-4 van San Antonio.</p>
{tabel(["2025/26", "Cleveland Cavaliers", "Minnesota Timberwolves"], [
    ("Eindstand", "52-30 (nr. 4 Oost)", "49-33 (nr. 6 West)"),
    ("Thuis / uit", "27-14 / 25-16", "26-15 / 23-18"),
    ("Punten voor / tegen", "119,5 / 115,4", "118,0 / 114,6"),
    ("Na het seizoen", "Finale Oost (0-4 tegen New York)", "Tweede ronde (2-4 tegen San Antonio)"),
])}
<p>In januari troffen beide ploegen elkaar twee keer binnen drie dagen. Minnesota won thuis met 131-122, met 28 punten van Julius Randle en 26 van Jaden McDaniels; Mitchell maakte 30 punten voor Cleveland. Twee dagen later won Cleveland thuis met 146-134. Mitchell scoorde 28 punten, Evan Mobley 24 en invaller Jaylon Tyson 23; bij de Wolves maakten Edwards en Naz Reid er elk 25. Let wel: Randle, Reid, DiVincenzo en Darius Garland speelden toen nog mee, Harden en Ball niet.</p>"""

content2 = f"""<h3><strong>Zo zijn beide selecties veranderd</strong></h3>
<p><strong>Cleveland Cavaliers: de kern blijft</strong></p>
<p>In februari ruilde Cleveland Garland voor Harden. Deze zomer kreeg Mitchell een contractverlenging van vier jaar en tekende Harden opnieuw voor drie jaar. De belangrijkste nieuwkomer is Peyton Watson, die uit Denver kwam en vorig seizoen 14,6 punten per wedstrijd maakte. Ook Mario Hezonja (Real Madrid) en rookie Meleek Thomas kwamen erbij. Max Strus, Dennis Schröder, Dean Wade, Keon Ellis en Larry Nance jr. vertrokken. Kenny Atkinson begint aan zijn derde seizoen als coach.</p>
<p><strong>Minnesota Timberwolves: Ball en Kuminga erbij</strong></p>
<p>Minnesota haalde LaMelo Ball uit Charlotte en Jonathan Kuminga, die vorig seizoen voor Golden State en Atlanta speelde. Ook Trey Lyles, Cody Williams en rookie Isaiah Evans zijn nieuw. Randle vertrok naar Brooklyn, Reid naar Charlotte. Chris Finch is nog altijd de coach. De grootste afwezige is DiVincenzo: hij liep in april in de eerste ronde van de play-offs tegen Denver een zware blessure aan zijn rechterachillespees op en werd geopereerd.</p>
<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("Donte DiVincenzo", "Minnesota", "Speelt niet (herstel na een operatie aan de rechterachillespees)"),
    ("Khalifa Diop", "Cleveland", "Speelt niet (linkerknie)"),
    ("Nae'Qwan Tomlin", "Cleveland", "Speelt niet (stressreactie in de onderrug)"),
    ("Ernest Udeh jr.", "Cleveland", "Niet bij de ploeg (G League)"),
])}
<p><em>Stand van de officiële NBA-blessurelijst op maandag 26 oktober, 12:30 Nederlandse tijd. Minnesota had zijn lijst toen nog niet ingediend; de Wolves meldden de afgelopen dagen alleen DiVincenzo als geblesseerd.</em></p>
<p><strong>Verwachte basisvijf Cavaliers:</strong> James Harden, Donovan Mitchell, Peyton Watson, Evan Mobley, Jarrett Allen. Dezelfde vijf als in beide wedstrijden. Tyson, Sam Merrill en Hezonja zijn de belangrijkste wissels.</p>
<p><strong>Verwachte basisvijf Timberwolves:</strong> LaMelo Ball, Anthony Edwards, Jaden McDaniels, Jonathan Kuminga, Rudy Gobert. Dezelfde vijf als in de eerste drie duels. Ayo Dosunmu, Terrence Shannon jr. en Lyles komen van de bank.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "2026/27 tot nu toe"], [
    ("Anthony Edwards (MIN)", "28,8", "5,0", "3,7", "28,7 ptn, 43% driepunters"),
    ("LaMelo Ball (MIN)", "20,1*", "4,8*", "7,1*", "16,0 ptn, 6,3 ast"),
    ("Rudy Gobert (MIN)", "10,9", "11,5", "1,7", "9,0 ptn, 12,3 reb"),
    ("Donovan Mitchell (CLE)", "27,9", "4,5", "5,7", "27,0 ptn, 7,5 reb"),
    ("James Harden (CLE)", "23,6**", "4,8**", "8,0**", "14,0 ptn, 6 uit 20"),
    ("Evan Mobley (CLE)", "18,2", "9,0", "3,6", "19,0 ptn, 9,0 reb"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26. * Ball: bij Charlotte. ** Harden: alle 70 duels van vorig seizoen, waarvan 44 voor de Clippers.</em></p>
<p><strong>Anthony Edwards</strong> scoorde vorig seizoen twee keer 25 punten tegen Cleveland. Onder de ring is het <strong>Rudy Gobert</strong> tegen <strong>Jarrett Allen</strong>. <strong>Donovan Mitchell</strong> moet Cleveland dragen zolang Harden zijn ritme niet heeft. En let op <strong>Jonathan Kuminga</strong>: 7 van zijn 11 driepunters waren raak.</p>
<h3><strong>Odds Cavaliers – Timberwolves bij TOTO</strong></h3>
<p>TOTO maakt Cleveland favoriet: een quotering van 1,63 staat voor ongeveer 61 procent winkans. De handicap ligt rond de 3,5 punten in het voordeel van de Cavs, het verwachte puntentotaal op 232,5.</p>
{tabel(["Markt (TOTO)", "Cavaliers", "Timberwolves"], [
    ("Winnaar (incl. verlenging)", "1,63", "2,35"),
    ("1X2 (reguliere speeltijd, gelijk 18,00)", "1,61", "2,40"),
    ("Handicap -2,5 / +2,5 (incl. verlenging)", "1,71", "1,98"),
    ("Handicap -3,5 / +3,5 (incl. verlenging)", "1,91", "1,91"),
    ("Handicap -4,5 / +4,5 (incl. verlenging)", "1,93", "1,73"),
    ("Handicap -5,5 / +5,5 (incl. verlenging)", "2,05", "1,65"),
])}
<p>Op het totaal biedt TOTO onder meer 230,5 punten (Over 1,69 / Under 2,00), 232,5 (1,91 / 1,91) en 234,5 (Over 2,00 / Under 1,69). Odds gelezen op maandag rond 12:45 uur; vergelijk ze vlak voor de start nog even.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op Cavaliers – Timberwolves</strong></a></p>"""

content3 = f"""<h3><strong>Onze voorspelling: Cleveland nipt, maar Minnesota blijft dichtbij</strong></h3>
<p>Cleveland speelt thuis, is uitgerust en won vorig seizoen 27 van zijn 41 thuisduels. Mitchell en Mobley zijn in vorm, en Harden kan elk moment loskomen. Maar de Cavs stortten in beide wedstrijden na rust in en verloren de bal veel te vaak.</p>
<p>Minnesota is een van de vormploegen van het Westen, met een vaste basisvijf en een verdediging die nog geen tegenstander boven de 106 punten liet komen. De back-to-back is de grote vraag, maar zondag kregen de basisspelers ruim rust in de tweede helft. Wij verwachten dat Cleveland het in de slotfase net beslist. Onze voorspelling: <strong>Cleveland Cavaliers – Minnesota Timberwolves 116-114</strong>.</p>
<h3><strong>Onze wedtip: Timberwolves +3,5 (1,91)</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Onze kans"], [
    ("Minnesota Timberwolves +3,5 punten (incl. verlenging)", "1,91", "TOTO", "Ongeveer 56 procent"),
])}
<p><strong>Waarom deze tip?</strong> De tip is goed als Minnesota wint, of verliest met maximaal drie punten verschil. Een odd van 1,91 staat voor een kans van 52 procent; zonder de marge van de bookmaker is dat ongeveer 50 procent. Wij schatten de kans op ongeveer 56 procent. De onderbouwing:</p>
<p><strong>1. Minnesota is in topvorm en bijna compleet.</strong> Drie zeges met 25, 22 en 23 punten verschil, steeds met dezelfde vijf in de basis. Alleen DiVincenzo ontbreekt, en die speelde dit seizoen nog geen minuut, dus de ploeg is al aan zijn afwezigheid gewend.</p>
<p><strong>2. De back-to-back weegt minder zwaar dan het lijkt.</strong> Zondag was de wedstrijd al vroeg beslist. Edwards speelde 26 minuten, Ball 17, en geen enkele basisspeler stond langer dan 31 minuten op het veld.</p>
<p><strong>3. Cleveland is nog niet stabiel.</strong> De Cavs gaven twee keer een voorsprong van meer dan twintig punten (bijna) weg, verloren 44 keer de bal en kregen in de tweede helften 69 en 67 punten tegen. Harden zoekt zijn vorm nog. Tegen een ploeg als Minnesota kost dat punten.</p>
<p><strong>Waarom niet een andere markt?</strong> Een zege van Cleveland (1,63) vraagt om 61 procent kans; wij komen uit op ongeveer 54 procent, dus die odd is te laag. Bij Cavs -3,5 (1,91) moet Cleveland met vier punten of meer winnen, en dat verwachten wij niet. Een zege van Minnesota (2,35) levert meer op, maar op de tweede avond van een back-to-back willen we de buffer van 3,5 punten. Bij Wolves +4,5 (1,73) of +5,5 (1,65) zakt de odd sneller dan de kans stijgt. Het puntentotaal laten we liggen: onze voorspelling komt uit op 230 punten, vlak bij de lijnen van TOTO.</p>
<p><strong>Het risico.</strong> Cleveland is uitgerust en speelt thuis, en Minnesota won vorig seizoen maar 2 van zijn 6 uitduels op de tweede avond van een back-to-back. Bovendien waren de tegenstanders van de Wolves tot nu toe niet sterk. Komt Harden los, dan kan Cleveland ook ruimer winnen. Let ook op: de handicap telt een eventuele verlenging mee. Meer uitleg vind je in onze gidsen over <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap wedden</a> en de <a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">money line</a>.</p>
<h3><strong>Cavaliers – Timberwolves live kijken in Nederland</strong></h3>
<p>Bij <a href="/bookmakers/bet365">Bet365</a> kun je NBA-wedstrijden live volgen via de livestream. Je hebt daarvoor een account met een storting nodig. ESPN zendt in Nederland een deel van de NBA-wedstrijden uit; in de programmagids zie je of deze erbij zit. Met <strong>NBA League Pass</strong>, de betaalde dienst van de competitie, kun je alle wedstrijden volgen. Meer opties vind je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk Cavaliers – Timberwolves live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Lees ook onze voorspellingen voor <a href="/nieuws/heat-mavericks-voorspelling-wedtips-nba-2026">Heat – Mavericks</a>, <a href="/nieuws/thunder-suns-voorspelling-wedtips-nba-2026">Thunder – Suns</a> en <a href="/nieuws/rockets-hawks-voorspelling-wedtips-nba-2026">Rockets – Hawks</a>, en alle <a href="/nieuws/nba-voorspellingen-vannacht-27-oktober-2026">NBA-voorspellingen van 27 oktober</a>. De eerste wedstrijd van Cleveland lees je terug in onze voorbeschouwing van <a href="/nieuws/76ers-cavaliers-voorspelling-wedtips-nba-2026">76ers – Cavaliers</a>. Benieuwd <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">welke Nederlanders in de NBA spelen</a>? Nieuw met basketbal? Lees <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels in de NBA</a>. Alle tips staan op <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Cavaliers – Timberwolves?</strong><br>Dinsdag 27 oktober 2026 om 00:00 Nederlandse tijd, in de nacht van maandag op dinsdag. In Cleveland is het dan maandagavond 19:00.</p>
<p><strong>Speelt Anthony Edwards mee?</strong><br>Ja, daar gaan we van uit. Edwards staat niet op de blessurelijst en speelde zondag maar 26 minuten. Bij Minnesota ontbreekt alleen Donte DiVincenzo, die herstelt van een operatie aan zijn achillespees.</p>
<p><strong>Wie is favoriet: Cavaliers of Timberwolves?</strong><br>Cleveland, met een quotering van 1,63 bij TOTO. Minnesota staat op 2,35.</p>
<p><strong>Wat is onze voorspelling voor Cavaliers – Timberwolves?</strong><br>Cleveland wint met 116-114. Onze wedtip is Minnesota Timberwolves +3,5 punten, inclusief verlenging (1,91 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

KAART = {"home": "Cavaliers", "away": "Timberwolves", "home_abbr": "cle", "away_abbr": "min", "home_pos": "52-30 · nr. 4 Oost 2025/26", "away_pos": "49-33 · nr. 6 West 2025/26", "hs": 116, "as": 114, "datum": "Di 27 okt", "tijd": "00:00", "odd_home": "1,63", "odd_away": "2,35"}
WEDTIPS = {"wedtip-1-2": "Minnesota Timberwolves +3,5 punten (incl. verlenging)", "quotering-wedtip-1": "1.91",
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
    toegestaan = {"/nieuws/nba-voorspellingen-vannacht-27-oktober-2026", "/nieuws/nba-voorspellingen-vannacht-26-oktober-2026",
                  "/nieuws/nba-voorspellingen-vannacht-25-oktober-2026", "/nieuws/nba-voorspellingen-vannacht-24-oktober-2026",
                  "/nieuws/heat-mavericks-voorspelling-wedtips-nba-2026", "/nieuws/thunder-suns-voorspelling-wedtips-nba-2026",
                  "/nieuws/rockets-hawks-voorspelling-wedtips-nba-2026", "/nieuws/nuggets-warriors-voorspelling-wedtips-nba-2026",
                  "/nieuws/thunder-clippers-voorspelling-wedtips-nba-2026", "/nieuws/jazz-lakers-voorspelling-wedtips-nba-2026",
                  "/nieuws/76ers-pistons-voorspelling-wedtips-nba-2026", "/nieuws/hawks-rockets-voorspelling-wedtips-nba-2026",
                  "/nieuws/thunder-nuggets-voorspelling-wedtips-nba-2026", "/nieuws/lakers-warriors-voorspelling-wedtips-nba-2026",
                  "/nieuws/76ers-cavaliers-voorspelling-wedtips-nba-2026",
                  "/nieuws/welke-nederlanders-spelen-in-de-nba",
                  "/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders",
                  "/nieuws/wat-is-handicap-wedden-de-complete-gids",
                  "/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners",
                  "/wedden-op-nba-voorspellingen-en-wedtips---basketbal", "/bookmakers/toto", "/bookmakers/bet365",
                  "/live-kijken", BET365}
    assert set(hrefs) <= toegestaan, set(hrefs) - toegestaan
    vannacht = {"/nieuws/heat-mavericks-voorspelling-wedtips-nba-2026", "/nieuws/thunder-suns-voorspelling-wedtips-nba-2026",
                "/nieuws/rockets-hawks-voorspelling-wedtips-nba-2026", "/nieuws/nuggets-warriors-voorspelling-wedtips-nba-2026"}
    assert 2 <= len(set(hrefs) & vannacht) <= 4, "link naar 2-4 andere voorbeschouwingen van vannacht"
    assert "/nieuws/nba-voorspellingen-vannacht-27-oktober-2026" in hrefs, "link naar het algemene artikel van vannacht"
    assert hrefs.count(BET365) == 2
    assert "<table" not in html.replace(f"<table {T}>", ""), "tabellen alleen via tabel()"
    verboden = ["BetCity", "ESPN-API", "ESPN.com", "ESPN-BPI", "BPI", "Associated Press", "DraftKings", "Rotowire", "Betfans"]
    assert not any(v.lower() in html.lower() for v in verboden), "geen bronnen/concurrenten"
    # Wedtip en consistentie
    assert set(WEDTIPS) == {"wedtip-1-2", "quotering-wedtip-1", "bookmaker-wedtips"}
    assert WEDTIPS["bookmaker-wedtips"] == "669ab9f5aceb8b717cea24c3"
    q = float(WEDTIPS["quotering-wedtip-1"])
    toto_odds = {1.63, 2.35, 1.61, 18.0, 2.40, 2.05, 1.65, 1.93, 1.73, 1.91, 1.71, 1.98, 2.10, 1.69, 2.00, 1.77}
    assert q in toto_odds and q == 1.91
    assert KAART["as"] + 3.5 > KAART["hs"], "voorspelde score moet Timberwolves +3,5 laten winnen"
    assert KAART["hs"] > KAART["as"], "voorspelling: Cavaliers winnen nipt"
    assert f"{KAART['hs']}-{KAART['as']}" in content and f"{KAART['hs']}-{KAART['as']}" in content3
    assert KAART["odd_home"] == "1,63" and KAART["odd_away"] == "2,35" and KAART["tijd"] == "00:00"
    assert KAART["home_abbr"] == "cle" and KAART["away_abbr"] == "min" and KAART["datum"] == "Di 27 okt"
    assert "1,91" in content and "1,91" in content3 and "+3,5" in content and "+3,5" in content3
    assert "maandag rond 12:45 uur" in html
    assert SLUG == "cavaliers-timberwolves-voorspelling-wedtips-nba-2026" and DATUM == "2026-10-26T23:00:00.000Z"
    assert html.count("<p><strong>Hoe laat begint") == 1 and html.count("<br>") == 4, "4 FAQ-vragen"
    tekst = re.sub(r"<[^>]+>", " ", html)
    print(len(TITEL), "tekens titel |", len(SAMENVATTING), "tekens samenvatting |", len(tekst.split()), "woorden")
    print("Alle asserts geslaagd (dry run, niets gepubliceerd).")
