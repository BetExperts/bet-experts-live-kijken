# -*- coding: utf-8 -*-
"""Los artikel: Rockets – Hawks voorspelling, NBA 27 oktober 2026 (01:30 NL, wintertijd), Toyota Center Houston.
Feiten nagelopen op 26-10-2026 (ESPN-API: summary 401909874, box score en play-by-play eerste duel 401909856,
box scores 401909840, 401909096, 401909834 en 401909843, teamschema's 2025/26 en 2026/27, rosters en coaches,
spelersgemiddelden 2025/26 en 2026/27, onderlinge duels 2025/26 (401810537, 401810873); officiële NBA-blessurelijst
24-10 20:00 ET (VanVleet out 'right knee injury management', Smart out) en 26-10 07:30 ET (12:30 NL)).
- Eerste duel za 24-10 (US) in Atlanta: Hawks – Rockets 114-121. Kwarten 26-30, 22-29, 33-33, 33-29; rust 48-59.
  Houston 20 punten voor (108-88, 7:15 in het vierde kwart), daarna 9-24; 117-112 met 36,5 sec te gaan, Durant 2 vrije
  worpen (18,9 sec), slot 121-114. Houston: 14/35 drie, 21/23 vrije worpen, 16 balverliezen. Atlanta: 13/49 drie,
  15/21 vrije worpen, 58 punten in de bucket, 35 assists. Durant 22 (8/15, +19), Sheppard 19 (5/11 drie, in de basis),
  Eason 19 (bank), Thompson 17/11 (9/9 vrije worpen), Şengün 17/10/7, Smith Jr. 14, Bogdanović 11 = zeven in dubbele
  cijfers. Johnson 26 ptn, 16 ast, 9 reb; Alexander-Walker 18, Daniels 18, McCollum 17, Wiggins 16, Okongwu 8 (2/8).
- VanVleet, Smart en Adams ontbraken in Atlanta. Vandaag: VanVleet niet op de lijst, Smart questionable, Adams out.
- Onderling 2025/26: 104-86 in Atlanta, 117-95 in Houston (beide Houston).
- Odds: alleen TOTO, uit specials/nba_feiten_2026_10_27.md (±12:45 NL op 26-10). Handicap en totaal incl. verlenging.
- Vorige tip (Hawks wint @1,83) ging verloren; dat staat eerlijk in de tekst.
- Eén wedtip (eis eigenaar): Rockets -4,5 @1,77, onze kans ±59% (markt 56,5%, zonder marge ±52%).
  python3 specials/rockets_hawks_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "Rockets – Hawks voorspelling: wedtip en odds voor de revanche in Houston (27 oktober, 01:30)"
SLUG = "rockets-hawks-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("Drie dagen na 121-114 in Atlanta treffen Rockets en Hawks elkaar opnieuw, nu in Houston en met Fred "
                "VanVleet terug. Voorspelling, onze wedtip, TOTO-odds, blessures en opstellingen.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet-experts.nl/go/bet365"
DATUM = "2026-10-27T00:30:00.000Z"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>In de nacht van maandag op dinsdag om 01:30 Nederlandse tijd staan de Houston Rockets en de Atlanta Hawks voor de tweede keer in drie dagen tegenover elkaar. Zaterdag won Houston met 121-114 in Atlanta, nu volgt de return in het Toyota Center. De Rockets zijn met 3-0 nog ongeslagen en krijgen hun vaste spelverdeler Fred VanVleet terug, die zaterdag rust kreeg. Atlanta wil de eerste nederlaag van het seizoen rechtzetten. Onze voorspelling: Rockets – Hawks 118-110. Onze wedtip: Houston Rockets -4,5 punten (inclusief verlenging) tegen een quotering van 1,77 bij TOTO.</strong></p>
<p>Hieronder lees je wat het eerste duel ons leerde, plus blessures, de odds van <a href="/bookmakers/toto">TOTO</a> en onze onderbouwing.</p>
<h3><strong>Rockets – Hawks: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "Houston Rockets – Atlanta Hawks"),
    ("Datum", "Dinsdag 27 oktober 2026 (nacht van maandag op dinsdag)"),
    ("Aanvang", "01:30 Nederlandse tijd (maandag 19:30 in Houston)"),
    ("Arena", "Toyota Center, Houston"),
    ("Competitie", "NBA, reguliere competitie 2026/27"),
    ("Stand 2026/27", "Rockets 3-0, Hawks 2-1"),
    ("Onderlinge duels", "2025/26: 2-0 voor Houston · 2026/27: 1-0 voor Houston"),
])}
<p>Beide ploegen speelden zaterdag tegen elkaar en hadden zondag een rustdag. Van vermoeidheid door een back-to-back is dus geen sprake.</p>
<h3><strong>Terugblik: zo verliep Hawks – Rockets (114-121)</strong></h3>
<p>In ons <a href="/nieuws/hawks-rockets-voorspelling-wedtips-nba-2026">artikel over het eerste duel</a> kozen we voor Atlanta. De Hawks hadden de frissere benen en speelden hun eerste thuisduel, maar dat bleek niet genoeg: onze tip ging verloren. Houston was het grootste deel van de wedstrijd de betere ploeg.</p>
<p><strong>Houston bepaalde het tempo</strong></p>
<p>De Rockets stonden na het eerste kwart 30-26 voor en gingen rusten bij 59-48. Zeven minuten voor tijd stond het 108-88. Houston stond 88 procent van de wedstrijd aan de leiding. Opvallend: dat lukte zonder VanVleet (rust voor zijn rechterknie), Marcus Smart (onderarm) en Steven Adams. Coach Ime Udoka zette Reed Sheppard in de basis. Hij scoorde 19 punten, met vijf driepunters. Tari Eason maakte er ook 19 vanaf de bank en Kevin Durant er 22, met 8 van zijn 15 schoten raak. Alperen Şengün en Amen Thompson kwamen allebei aan een double-double; in totaal scoorden zeven Rockets tien punten of meer.</p>
<p><strong>Atlanta kwam te laat terug</strong></p>
<p>Vanaf 108-88 kwam Atlanta met een reeks van 24-9 terug tot 117-112, met nog 36 seconden op de klok. Durant benutte daarna twee vrije worpen en Eason maakte het af met een dunk. Jalen Johnson deed bij de Hawks alles: 26 punten, 9 rebounds en 16 assists. Het probleem zat in het schieten van afstand: Atlanta nam 49 driepunters en miste er 36 (27 procent). Houston schoot 14 van de 35 (40 procent) en benutte 21 van de 23 vrije worpen. Ook belangrijk: de Hawks dwongen in hun eerste twee wedstrijden samen 47 balverliezen af, maar Houston verloor de bal zaterdag maar 16 keer.</p>
<h3><strong>Vorig seizoen en de onderlinge duels</strong></h3>
<p>Houston was in 2025/26 de sterkere ploeg en vooral thuis lastig te kloppen. In de play-offs strandden beide ploegen in de eerste ronde.</p>
{tabel(["2025/26", "Houston Rockets", "Atlanta Hawks"], [
    ("Eindstand", "52-30 (nr. 5 West)", "46-36 (nr. 6 Oost)"),
    ("Thuis / uit", "30-11 / 22-19", "24-17 / 22-19"),
    ("Punten voor / tegen", "115,2 / 110,0", "118,5 / 116,0"),
    ("Play-offs", "Eerste ronde (2-4 tegen de Lakers)", "Eerste ronde (2-4 tegen New York)"),
])}
<p>Houston won de laatste drie onderlinge duels allemaal: 104-86 in Atlanta in januari, 117-95 in Houston in maart en zaterdag 121-114. Dat is gemiddeld bijna zestien punten verschil.</p>"""

content2 = f"""<h3><strong>Zo zijn beide selecties veranderd</strong></h3>
<p><strong>Houston Rockets: VanVleet terug, meer ervaring op de bank</strong></p>
<p>VanVleet miste het hele vorige seizoen met een gescheurde kruisband. Op de tweede avond van een back-to-back kreeg hij zaterdag rust; maandag is hij gewoon beschikbaar. Nieuw zijn Smart (van de Lakers) en Bogdan Bogdanović (van de Clippers), die net als Clint Capela eerder voor Atlanta speelde. Ime Udoka is nog altijd de coach.</p>
<p><strong>Atlanta Hawks: een nieuw team rond Johnson</strong></p>
<p>Trae Young vertrok vorig seizoen naar Washington, uit Washington kwamen CJ McCollum en Corey Kispert. Deze zomer kwamen Luguentz Dort en Aaron Wiggins over van Oklahoma City, plus Dorian Finney-Smith uit Houston. Atlanta koos in de draft Kingston Flemings als nummer acht. Quin Snyder is nog altijd de coach.</p>
<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("Steven Adams", "Houston", "Speelt niet (kuitblessure rechts)"),
    ("Marcus Smart", "Houston", "Twijfelachtig (verrekte linkeronderarm), miste zaterdag"),
    ("Fred VanVleet", "Houston", "Staat niet op de lijst, kreeg zaterdag rust (rechterknie)"),
    ("Quadir Copeland, Julian Phillips", "Houston", "Niet bij de ploeg (G League)"),
    ("Mouhamed Gueye", "Atlanta", "Speelt niet (gebroken linkervoet)"),
    ("Henri Veesaar", "Atlanta", "Speelt niet (gescheurde kruisband, seizoen voorbij)"),
    ("Jock Landale", "Atlanta", "Inzetbaar (gebroken neus)"),
    ("RayJ Dennis, Keshon Gilbert, Jalen Wilson", "Atlanta", "Waarschijnlijk niet (G League)"),
])}
<p><em>Stand van de officiële NBA-blessurelijst op maandag 26 oktober, 12:30 Nederlandse tijd.</em></p>
<p><strong>Verwachte basisvijf Houston:</strong> Fred VanVleet, Amen Thompson, Kevin Durant, Jabari Smith Jr., Alperen Şengün. Zo begon Houston de eerste twee wedstrijden. Sheppard schuift dan terug naar de bank, naast Eason, Bogdanović en Capela.</p>
<p><strong>Verwachte basisvijf Atlanta:</strong> Dyson Daniels, Nickeil Alexander-Walker, CJ McCollum, Jalen Johnson, Onyeka Okongwu. Snyder begon alle drie de wedstrijden met deze vijf. Wiggins, Dort, Landale en Flemings zijn de vaste wissels.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "2026/27 tot nu toe"], [
    ("Kevin Durant (HOU)", "26,0", "5,5", "4,8", "24,0 ptn, 56% uit het veld"),
    ("Alperen Şengün (HOU)", "20,4", "8,9", "6,2", "23,0 ptn, 9,0 reb, 6,3 ast"),
    ("Amen Thompson (HOU)", "18,3", "7,8", "5,3", "17,7 ptn, 10,3 reb"),
    ("Fred VanVleet (HOU)", "–*", "–*", "–*", "10,0 ptn, 8,0 ast (2 duels)"),
    ("Jalen Johnson (ATL)", "22,5", "10,3", "7,9", "21,7 ptn, 10,0 reb, 10,0 ast"),
    ("Nickeil Alexander-Walker (ATL)", "20,8", "3,4", "3,7", "21,0 ptn, 41% driepunters"),
    ("Dyson Daniels (ATL)", "11,9", "6,8", "5,9", "16,3 ptn, 62% uit het veld"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26. * VanVleet speelde vorig seizoen niet door een kruisbandblessure.</em></p>
<p><strong>Jalen Johnson</strong> staat na drie wedstrijden op gemiddeld een triple-double en is de motor van de Hawks. <strong>Amen Thompson</strong> heeft na drie duels drie double-doubles en kan Johnson met zijn snelheid en lengte het leven zuur maken. <strong>Kevin Durant</strong> staat op 56 procent uit het veld en zette zaterdag de wedstrijd met twee vrije worpen in de laatste twintig seconden op slot. Bij Atlanta moet <strong>Nickeil Alexander-Walker</strong> beter mikken: zaterdag zaten er 4 van zijn 12 driepunters in.</p>
<h3><strong>Odds Rockets – Hawks bij TOTO</strong></h3>
<p>Zaterdag zag TOTO Atlanta nog als lichte favoriet. Nu is dat omgedraaid: een quotering van 1,51 op Houston staat voor ongeveer 66 procent winkans. De handicap ligt rond de 5,5 punten in het voordeel van de Rockets, het verwachte puntentotaal op 229,5.</p>
{tabel(["Markt (TOTO)", "Rockets", "Hawks"], [
    ("Winnaar (incl. verlenging)", "1,51", "2,65"),
    ("1X2 (reguliere speeltijd, gelijk 18,00)", "1,49", "2,75"),
    ("Handicap -4,5 / +4,5 (incl. verlenging)", "1,77", "1,91"),
    ("Handicap -5,5 / +5,5 (incl. verlenging)", "1,95", "1,87"),
    ("Handicap -6,5 / +6,5 (incl. verlenging)", "2,05", "1,67"),
])}
<p>Op het totaal biedt TOTO 228,5 punten (Over 1,73 / Under 1,93), 229,5 (1,91 / 1,91) en 230,5 (Over 1,91 / Under 1,77). Odds gelezen op maandag rond 12:45 uur; vergelijk ze vlak voor de start nog even.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op Rockets – Hawks</strong></a></p>"""

content3 = f"""<h3><strong>Onze voorspelling: Houston opnieuw te sterk</strong></h3>
<p>Het eerste duel liet zien dat Houston een ploeg is met veel scorers en weinig zwakke plekken. Zelfs zonder VanVleet en Smart, en met Adams aan de kant, stonden de Rockets in Atlanta lang ruim voor. Nu spelen ze thuis, waar ze vorig seizoen bijna drie van de vier wedstrijden wonnen, en met hun vaste basisvijf.</p>
<p>Atlanta heeft wel argumenten: Johnson is in vorm, de bank is breed en een betere avond van afstand dan 13 van de 49 ligt voor de hand. Toch zien we Houston weer winnen, en ruimer dan met vier punten. Onze voorspelling: <strong>Houston Rockets – Atlanta Hawks 118-110</strong>.</p>
<h3><strong>Onze wedtip: Rockets -4,5 (1,77)</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Onze kans"], [
    ("Houston Rockets -4,5 punten (incl. verlenging)", "1,77", "TOTO", "Ongeveer 59 procent"),
])}
<p><strong>Waarom deze tip?</strong> De tip is goed als Houston met vijf punten of meer verschil wint. Een odd van 1,77 staat voor een kans van ruim 56 procent; zonder de marge van de bookmaker is dat ongeveer 52 procent. Wij schatten de kans op ongeveer 59 procent. De onderbouwing:</p>
<p><strong>1. VanVleet maakt Houston completer.</strong> Zaterdag won Houston met zeven punten verschil zonder zijn eerste spelverdeler en zonder Smart. VanVleet gaf in zijn twee wedstrijden dit seizoen gemiddeld 8 assists. Met hem erbij heeft Udoka een extra balhandler, en Sheppard kan weer als schutter van de bank komen.</p>
<p><strong>2. Houston wint deze duels ruim.</strong> De laatste drie onderlinge wedstrijden gingen met 18, 22 en 7 punten verschil naar de Rockets. Thuis wonnen ze vorig seizoen 30 van de 41 duels.</p>
<p><strong>3. Het wapen van Atlanta werkte niet.</strong> De Hawks leven van balveroveringen: Orlando en Charlotte verloren samen 47 keer de bal. Houston bleef zaterdag op 16 balverliezen steken. Met VanVleet aan de bal wordt dat voor de Hawks niet makkelijker.</p>
<p><strong>Waarom niet een andere markt?</strong> Een zege van de Rockets (1,51) vraagt om 66 procent kans. Wij komen uit op ongeveer 69 procent: dat verschil is klein en de odd levert weinig op. Rockets -5,5 (1,95) en -6,5 (2,05) betalen meer, maar dan moet Houston met zes of zeven punten winnen. Zaterdag werd het precies zeven, terwijl de Rockets twintig punten voor hadden gestaan. In de slotfase kan een voorsprong snel kleiner worden, dus die extra punten speling willen we houden. Het puntentotaal laten we liggen: onze voorspelling komt uit op 228 punten, net onder de lijn van 229,5, en zaterdag vielen er 235.</p>
<p><strong>Het risico.</strong> Atlanta schoot zaterdag 27 procent van afstand. Gaat dat richting een normaal percentage, dan scoren de Hawks er al snel tien punten meer bij. Johnson kan in zijn eentje een wedstrijd kantelen, en de slotfase van zaterdag liet zien dat Houston een ruime voorsprong niet altijd vasthoudt. Let ook op: de handicap telt een eventuele verlenging mee. Meer uitleg vind je in onze gidsen over <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap wedden</a> en de <a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">money line</a>.</p>
<h3><strong>Rockets – Hawks live kijken in Nederland</strong></h3>
<p>Bij <a href="/bookmakers/bet365">Bet365</a> kun je NBA-wedstrijden live volgen via de livestream. Je hebt daarvoor een account met een storting nodig. ESPN zendt in Nederland een deel van de NBA-wedstrijden uit; in de programmagids zie je of deze erbij zit. Met <strong>NBA League Pass</strong>, de betaalde dienst van de competitie, kun je alle wedstrijden volgen. Meer opties vind je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk Rockets – Hawks live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Vannacht staan er meer duels op het programma. Lees ook onze voorspellingen voor <a href="/nieuws/cavaliers-timberwolves-voorspelling-wedtips-nba-2026">Cavaliers – Timberwolves</a>, <a href="/nieuws/thunder-suns-voorspelling-wedtips-nba-2026">Thunder – Suns</a> en <a href="/nieuws/nuggets-warriors-voorspelling-wedtips-nba-2026">Nuggets – Warriors</a>, en alle <a href="/nieuws/nba-voorspellingen-vannacht-27-oktober-2026">NBA-voorspellingen van 27 oktober</a>. Benieuwd <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">welke Nederlanders in de NBA spelen</a>? Nieuw met basketbal? Lees <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels in de NBA</a>. Alle tips staan op <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Rockets – Hawks?</strong><br>Dinsdag 27 oktober 2026 om 01:30 Nederlandse tijd, in de nacht van maandag op dinsdag. In Houston is het dan maandagavond 19:30.</p>
<p><strong>Speelt Fred VanVleet mee?</strong><br>Naar verwachting wel. Hij miste zaterdag het eerste duel in Atlanta omdat Houston zijn rechterknie rust gaf, maar staat nu niet op de blessurelijst. Steven Adams speelt niet, achter Marcus Smart staat een vraagteken.</p>
<p><strong>Wie is favoriet: Rockets of Hawks?</strong><br>De Rockets, met een quotering van 1,51 bij TOTO. Atlanta staat op 2,65.</p>
<p><strong>Wat is onze voorspelling voor Rockets – Hawks?</strong><br>De Rockets winnen met 118-110. Onze wedtip is Houston Rockets -4,5 punten, inclusief verlenging (1,77 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

KAART = {"home": "Rockets", "away": "Hawks", "home_abbr": "hou", "away_abbr": "atl", "home_pos": "52-30 · nr. 5 West 2025/26", "away_pos": "46-36 · nr. 6 Oost 2025/26", "hs": 118, "as": 110, "datum": "Di 27 okt", "tijd": "01:30", "odd_home": "1,51", "odd_away": "2,65"}
WEDTIPS = {"wedtip-1-2": "Houston Rockets -4,5 punten (incl. verlenging)", "quotering-wedtip-1": "1.77",
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
                  "/nieuws/hawks-rockets-voorspelling-wedtips-nba-2026",
                  "/nieuws/cavaliers-timberwolves-voorspelling-wedtips-nba-2026",
                  "/nieuws/heat-mavericks-voorspelling-wedtips-nba-2026",
                  "/nieuws/thunder-suns-voorspelling-wedtips-nba-2026",
                  "/nieuws/nuggets-warriors-voorspelling-wedtips-nba-2026",
                  "/nieuws/thunder-clippers-voorspelling-wedtips-nba-2026", "/nieuws/jazz-lakers-voorspelling-wedtips-nba-2026",
                  "/nieuws/76ers-pistons-voorspelling-wedtips-nba-2026", "/nieuws/thunder-nuggets-voorspelling-wedtips-nba-2026",
                  "/nieuws/lakers-warriors-voorspelling-wedtips-nba-2026", "/nieuws/76ers-cavaliers-voorspelling-wedtips-nba-2026",
                  "/nieuws/welke-nederlanders-spelen-in-de-nba",
                  "/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders",
                  "/nieuws/wat-is-handicap-wedden-de-complete-gids",
                  "/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners",
                  "/wedden-op-nba-voorspellingen-en-wedtips---basketbal", "/bookmakers/toto", "/bookmakers/bet365",
                  "/live-kijken", BET365}
    assert set(hrefs) <= toegestaan, set(hrefs) - toegestaan
    assert "/nieuws/hawks-rockets-voorspelling-wedtips-nba-2026" in hrefs, "link naar het eerste duel"
    assert "/nieuws/nba-voorspellingen-vannacht-27-oktober-2026" in hrefs, "link naar het algemene artikel"
    vannacht = {"cavaliers-timberwolves", "heat-mavericks", "thunder-suns", "nuggets-warriors"}
    assert 2 <= sum(f"/nieuws/{s}-voorspelling-wedtips-nba-2026" in hrefs for s in vannacht) <= 4, "2-4 andere previews"
    assert hrefs.count(BET365) == 2, "Bet365-CTA's zoals in het sjabloon"
    assert "<table" not in html.replace(f"<table {T}>", ""), "tabellen alleen via tabel()"
    verboden = ["BetCity", "ESPN-API", "ESPN.com", "Associated Press", "DraftKings", "Rotowire", "Betfans"]
    assert not any(v.lower() in html.lower() for v in verboden), "geen bronnen/concurrenten"
    # Wedtip en consistentie
    assert set(WEDTIPS) == {"wedtip-1-2", "quotering-wedtip-1", "bookmaker-wedtips"}
    assert WEDTIPS["bookmaker-wedtips"] == "669ab9f5aceb8b717cea24c3"
    q = float(WEDTIPS["quotering-wedtip-1"])
    toto_odds = {1.51, 2.65, 1.49, 18.0, 2.75, 2.05, 1.67, 1.95, 1.87, 1.77, 1.91, 1.73, 1.93}
    assert q in toto_odds and q == 1.77
    assert KAART["hs"] - 4.5 > KAART["as"], "voorspelde score moet Rockets -4,5 laten winnen"
    assert KAART["hs"] > KAART["as"], "voorspelling: Rockets winnen"
    assert f"{KAART['hs']}-{KAART['as']}" in content and f"{KAART['hs']}-{KAART['as']}" in content3
    assert KAART["odd_home"] == "1,51" and KAART["odd_away"] == "2,65" and KAART["tijd"] == "01:30"
    assert KAART["home_abbr"] == "hou" and KAART["away_abbr"] == "atl" and KAART["datum"] == "Di 27 okt"
    assert "1,77" in content and "1,77" in content3 and "maandag rond 12:45 uur" in content2
    assert "121-114" in content, "uitslag eerste duel"
    assert SLUG == "rockets-hawks-voorspelling-wedtips-nba-2026" and DATUM == "2026-10-27T00:30:00.000Z"
    tekst = re.sub(r"<[^>]+>", " ", html)
    print(len(TITEL), "tekens titel |", len(SAMENVATTING), "tekens samenvatting |", len(tekst.split()), "woorden")
    print("Alle asserts geslaagd (dry run, niets gepubliceerd).")
