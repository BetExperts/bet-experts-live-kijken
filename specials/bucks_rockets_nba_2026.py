# -*- coding: utf-8 -*-
"""Los artikel: Bucks – Rockets voorspelling, NBA 29 oktober 2026 (01:00 NL, wintertijd; woensdag 19:00 CT), Fiserv Forum Milwaukee.
Feiten nagelopen op 28-10-2026 (ESPN-API: summary 401909887, box scores 2026/27 401909835, 401909848, 401909855, 401909872
(MIL) en 401909840, 401909096, 401909856, 401909874 (HOU), teamschema's 2025/26 en 2026/27, rosters en coaches, standen
2025/26, play-offs 2025/26, alle 82 box scores Houston 2025/26 (Şengün-afwezigheden) en Milwaukee/Miami 2025/26
(spelersgemiddelden), onderlinge duels 2025/26 (401810046, 401810965); officiële NBA-blessurelijst 28-10 05:45 ET;
berichtgeving over de ruil Antetokounmpo/Portis naar Miami (23-6-2026) en de aanstelling van Taylor Jenkins (30-4-2026)).
- Bucks 2026/27: 116-128 in Washington, 125-132 tegen Chicago, 116-127 in Philadelphia, 110-102 tegen Indiana (61 rebounds).
- Rockets 2026/27: 128-110 tegen Dallas, 114-110 in San Antonio, 121-114 in Atlanta, 120-110 tegen Atlanta (Şengün 29/9/9).
- Onderling 2025/26: 115-122 in Milwaukee (Giannis 37, Durant 31), 119-113 in Houston (Bucks zonder Giannis, Turner, Kuzma, Portis).
- Houston 2025/26 zonder Şengün: 10 duels, 6-4, 110,7 punten voor (seizoen 115,2); marges +19, -13, +17, +7, +3, -1, -6, +2, -8, +31
  (in 7 van de 10 zou +8,5 voor de tegenstander gewonnen hebben). In maart miste hij twee duels met rugklachten.
- Blessurelijst 28-10 05:45 ET: HOU Şengün out (low back soreness), Adams out (rechterkuit/soleus), Smart questionable (linkeronderarm),
  Copeland en Phillips out (G League). Milwaukee staat niet op de lijst.
- Beide ploegen speelden maandag (US) en hadden dinsdag rust.
- Odds: alleen TOTO, uit specials/nba_feiten_2026_10_29.md (±10:50 NL op 28-10). Handicap en totaal incl. verlenging.
- Eén wedtip (vast, eigenaar): Bucks +8,5 @1,87, onze kans ±58% (markt 53,5%, zonder marge ±51%).
  python3 specials/bucks_rockets_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "Bucks – Rockets voorspelling: wedtip en odds, ongeslagen Houston zonder Şengün (29 oktober, 01:00)"
SLUG = "bucks-rockets-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("Bucks – Rockets voorspelling: het ongeslagen Houston speelt in Milwaukee zonder Alperen Şengün. "
                "Onze wedtip, TOTO-odds en blessures.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet-experts.nl/go/bet365"
DATUM = "2026-10-29T00:00:00.000Z"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>Onze Bucks – Rockets voorspelling draait om één afwezige: Alperen Şengün. De Houston Rockets zijn met 4-0 nog ongeslagen, maar spelen in de nacht van woensdag op donderdag om 01:00 Nederlandse tijd in Milwaukee zonder hun center, die met rugklachten aan de kant staat. Şengün was dit seizoen met 24,5 punten, 9 rebounds en 7 assists per wedstrijd de spil van de ploeg. Milwaukee staat na de vertrekken van de zomer op 1-3, maar won maandag van Indiana. Onze voorspelling: Bucks – Rockets 111-117. Onze wedtip: Milwaukee Bucks +8,5 punten (inclusief verlenging) tegen een quotering van 1,87 bij TOTO.</strong></p>
<p>Hieronder lees je alles over vorm, blessures, de odds van <a href="/bookmakers/toto">TOTO</a> en onze onderbouwing.</p>
<h3><strong>Bucks – Rockets: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "Milwaukee Bucks – Houston Rockets"),
    ("Datum", "Donderdag 29 oktober 2026 (nacht van woensdag op donderdag)"),
    ("Aanvang", "01:00 Nederlandse tijd (woensdag 19:00 in Milwaukee)"),
    ("Arena", "Fiserv Forum, Milwaukee"),
    ("Competitie", "NBA, reguliere competitie 2026/27"),
    ("Stand 2026/27", "Bucks 1-3, Rockets 4-0"),
    ("Onderlinge duels 2025/26", "2-0 voor Houston"),
])}
<p>Beide ploegen speelden maandag (Amerikaanse tijd) en hadden dinsdag een rustdag. Van een back-to-back is dus geen sprake.</p>
<h3><strong>Seizoen tot nu toe: Houston 4-0, Milwaukee 1-3</strong></h3>
<p><strong>Houston Rockets: vier zeges, twee keer krap</strong></p>
<p>Houston opende met een 128-110 thuiszege op Dallas, waarin Kevin Durant en Jabari Smith Jr. allebei 30 punten maakten. Daarna volgden 114-110 in San Antonio en twee duels met Atlanta: 121-114 in Atlanta en maandag 120-110 in Houston. In die laatste wedstrijd was Şengün de grote man, met 29 punten, 9 rebounds, 9 assists en 6 steals. Houston won zijn vier duels met 18, 4, 7 en 10 punten verschil. In Atlanta stond Houston zeven minuten voor tijd nog twintig punten voor, maar won het met zeven.</p>
<p><strong>Milwaukee Bucks: veel gescoord, nog meer tegen</strong></p>
<p>De Bucks verloren hun eerste drie wedstrijden: 116-128 in Washington, 125-132 thuis tegen Chicago en 116-127 in Philadelphia. Milwaukee scoorde gemiddeld 116,8 punten, maar kreeg er 122,2 tegen. Maandag volgde de eerste zege: 110-102 tegen Indiana, dat zonder Ivica Zubac en Andrew Nembhard speelde. Tyler Herro had 23 punten, 10 rebounds en 7 assists, Kel'el Ware 16 punten en 14 rebounds. Milwaukee pakte 61 rebounds, tegen 48 voor Indiana. Ook in Philadelphia won de ploeg van coach Taylor Jenkins de reboundstrijd ruim (62 tegen 40).</p>
<h3><strong>Vorig seizoen en de onderlinge duels</strong></h3>
<p>Houston won in 2025/26 52 wedstrijden en verloor in de eerste ronde van de play-offs met 2-4 van de Lakers. Milwaukee won er maar 32 en miste voor het eerst sinds 2016 de play-offs. Giannis Antetokounmpo speelde door blessures maar 36 wedstrijden.</p>
{tabel(["2025/26", "Milwaukee Bucks", "Houston Rockets"], [
    ("Eindstand", "32-50 (nr. 11 Oost)", "52-30 (nr. 5 West)"),
    ("Thuis / uit", "19-22 / 13-28", "30-11 / 22-19"),
    ("Punten voor / tegen", "110,6 / 116,8", "115,2 / 110,0"),
    ("Na het seizoen", "Play-offs niet gehaald", "Eerste ronde (2-4 tegen de Lakers)"),
])}
<p>Beide onderlinge duels gingen naar Houston, maar het verschil bleef klein. In november won Houston met 122-115 in Milwaukee: Antetokounmpo scoorde 37 punten, Durant 31 en Şengün had 23 punten en 11 rebounds. In april volgde 119-113 in Houston. Milwaukee speelde toen zonder Antetokounmpo, Myles Turner, Kyle Kuzma en Bobby Portis, maar verloor toch maar met zes punten verschil.</p>"""

content2 = f"""<h3><strong>Zo zijn beide selecties veranderd</strong></h3>
<p><strong>Milwaukee Bucks: een nieuwe ploeg zonder Giannis</strong></p>
<p>In juni ruilde Milwaukee Antetokounmpo en Portis naar Miami. Daarvoor kwamen Herro, Jaime Jaquez Jr., Ware en Kasparas Jakučionis naar Milwaukee, plus een pakket draftkeuzes. Doc Rivers stopte na het seizoen; Taylor Jenkins, eerder coach van Memphis, is zijn opvolger. Turner, Kuzma en Rollins bleven.</p>
<p><strong>Houston Rockets: VanVleet terug, Şengün nu weg</strong></p>
<p>Fred VanVleet miste het hele vorige seizoen met een gescheurde kruisband en is terug als spelverdeler. Nieuw zijn Marcus Smart (van de Lakers) en Bogdan Bogdanović (van de Clippers). Ime Udoka is nog altijd de coach.</p>
<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("Alperen Şengün", "Houston", "Speelt niet (rugklachten, onderrug)"),
    ("Steven Adams", "Houston", "Speelt niet (kuitblessure rechts)"),
    ("Marcus Smart", "Houston", "Twijfelachtig (verrekte linkeronderarm)"),
    ("Quadir Copeland, Julian Phillips", "Houston", "Niet bij de ploeg (G League)"),
    ("Milwaukee Bucks", "Milwaukee", "Geen blessures gemeld"),
])}
<p><em>Stand van de officiële NBA-blessurelijst op woensdag 28 oktober, 10:45 Nederlandse tijd.</em></p>
<p>Houston mist zo zijn twee grootste centers. Clint Capela speelde dit seizoen gemiddeld nog geen acht minuten. In maart miste Şengün al eens twee duels met rugklachten.</p>
<p><strong>Verwachte basisvijf Bucks:</strong> Tyler Herro, Ryan Rollins, Jaime Jaquez Jr., Kyle Kuzma, Myles Turner. Jenkins begon alle vier de wedstrijden met deze vijf. Ware, Jakučionis, AJ Green en Burries zijn de belangrijkste wissels.</p>
<p><strong>Verwachte basisvijf Houston:</strong> Fred VanVleet, Amen Thompson, Kevin Durant, Jabari Smith Jr. en Clint Capela of Tari Eason. Vorig seizoen begon zonder Şengün meestal Adams, en anders Eason of Capela. Reed Sheppard, Bogdanović en (als hij fit is) Smart komen van de bank.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "2026/27 tot nu toe"], [
    ("Kevin Durant (HOU)", "26,0", "5,5", "4,8", "23,5 ptn, 54% uit het veld"),
    ("Amen Thompson (HOU)", "18,3", "7,8", "5,3", "17,0 ptn, 9,0 reb"),
    ("Jabari Smith Jr. (HOU)", "15,8", "6,9", "1,9", "16,8 ptn, 6,8 reb"),
    ("Tyler Herro (MIL)", "20,5*", "4,8*", "4,1*", "23,5 ptn, 5,8 reb, 5,8 ast"),
    ("Jaime Jaquez Jr. (MIL)", "15,4*", "5,0*", "4,7*", "17,5 ptn, 8,0 reb"),
    ("Kel'el Ware (MIL)", "11,1*", "9,0*", "0,7*", "13,2 ptn, 8,5 reb (bank)"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26. * Cijfers bij Miami; Herro speelde vorig seizoen 33 wedstrijden.</em></p>
<p><strong>Kevin Durant</strong> wordt zonder Şengün nog meer het aanspreekpunt. <strong>Amen Thompson</strong> moet met zijn snelheid en lengte de rebounds en de spelopbouw opvangen die Şengün normaal levert. <strong>Tyler Herro</strong> is de eerste scorer van Milwaukee (34 punten tegen Chicago). <strong>Kel'el Ware</strong> pakte in de laatste twee duels 13 en 14 rebounds en kan onder de ring het verschil maken tegen een Houston zonder centers.</p>
<h3><strong>Odds Bucks – Rockets bij TOTO</strong></h3>
<p>TOTO ziet Houston als ruime favoriet: een quotering van 1,30 staat voor ongeveer 77 procent winkans. De handicap ligt rond de 8,5 punten in het voordeel van de Rockets, het verwachte puntentotaal op 227,5.</p>
{tabel(["Markt (TOTO)", "Bucks", "Rockets"], [
    ("Winnaar (incl. verlenging)", "3,65", "1,30"),
    ("1X2 (reguliere speeltijd, gelijk 18,00)", "4,00", "1,29"),
    ("Handicap +7,5 / -7,5 (incl. verlenging)", "1,93", "1,73"),
    ("Handicap +8,5 / -8,5 (incl. verlenging)", "1,87", "1,95"),
    ("Handicap +9,5 / -9,5 (incl. verlenging)", "1,69", "2,00"),
])}
<p>Op het totaal biedt TOTO 226,5 punten (Over 1,73 / Under 1,95), 227,5 (1,87 / 1,93) en 228,5 (Over 1,87 / Under 1,78). Odds gelezen op woensdag rond 10:50 uur; vergelijk ze vlak voor de start nog even.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op Bucks – Rockets</strong></a></p>"""

content3 = f"""<h3><strong>Bucks – Rockets voorspelling: Houston wint, maar niet ruim</strong></h3>
<p>Houston is de betere ploeg, ook zonder Şengün. Durant, Thompson en Smith Jr. zijn alle drie in vorm en VanVleet geeft rust aan de bal. Toch verliest Udoka zijn belangrijkste aanvaller en passer, en met Adams erbij ontbreken ook allebei zijn centers. Vorig seizoen speelde Houston tien wedstrijden zonder Şengün: het won er zes en scoorde gemiddeld 110,7 punten, ruim vier minder dan zijn seizoensgemiddelde.</p>
<p>Milwaukee heeft juist lengte, met Turner, Ware, Kuzma en Jaquez, en pakte in de laatste twee duels meer dan zestig rebounds per wedstrijd. De verdediging lekt, maar tegen een Houston zonder middenas verwachten we een spannende wedstrijd. Onze voorspelling: <strong>Milwaukee Bucks – Houston Rockets 111-117</strong>.</p>
<h3><strong>Onze wedtip: Bucks +8,5 (1,87)</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Onze kans"], [
    ("Milwaukee Bucks +8,5 punten (incl. verlenging)", "1,87", "TOTO", "Ongeveer 58 procent"),
])}
<p><strong>Waarom deze tip?</strong> De tip is goed als Milwaukee wint, of verliest met maximaal acht punten verschil. Een odd van 1,87 staat voor een kans van ruim 53 procent; zonder de marge van de bookmaker is dat ongeveer 51 procent. Wij schatten de kans op ongeveer 58 procent. De onderbouwing:</p>
<p><strong>1. Zonder Şengün wint Houston minder ruim.</strong> In de tien wedstrijden die hij vorig seizoen miste, won Houston maar drie keer met meer dan acht punten verschil. In de andere zeven had deze handicap gewonnen. Dit seizoen liep bijna alles via hem: 24,5 punten en 7 assists per wedstrijd.</p>
<p><strong>2. Milwaukee wint de strijd onder de ring.</strong> De Bucks pakten tegen Philadelphia en Indiana 62 en 61 rebounds. Houston mist met Şengün en Adams zijn twee belangrijkste centers. Extra balbezit helpt een underdog om in de buurt te blijven.</p>
<p><strong>3. De onderlinge duels waren krap.</strong> Vorig seizoen won Houston met 7 en 6 punten verschil, de tweede keer tegen een Milwaukee vol reserves. Ook dit seizoen won Houston twee van zijn vier duels met acht punten of minder verschil, en in Atlanta liep een voorsprong van twintig punten terug tot zeven.</p>
<p><strong>Waarom niet een andere markt?</strong> Een zege van de Bucks (3,65) vraagt om ruim 27 procent kans. Wij komen uit op ongeveer 30 procent: een klein verschil voor een gok met veel risico. Bucks +7,5 (1,93) levert iets meer op, maar een nederlaag met precies acht punten is in basketbal geen zeldzaamheid, dus dat extra punt houden we graag. Bucks +9,5 (1,69) betaalt te weinig voor één punt extra. Het puntentotaal laten we liggen: onze voorspelling komt uit op 228 punten, vlak bij de lijn van 227,5.</p>
<p><strong>Het risico.</strong> Milwaukee kreeg in drie van de vier wedstrijden 127 punten of meer tegen en verloor twee keer met elf of twaalf punten verschil. En Durant kan een wedstrijd in zijn eentje beslissen. Let ook op: de handicap telt een eventuele verlenging mee. Meer uitleg vind je in onze gidsen over <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap wedden</a> en de <a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">money line</a>.</p>
<h3><strong>Bucks – Rockets live kijken in Nederland</strong></h3>
<p>Bij <a href="/bookmakers/bet365">Bet365</a> kun je NBA-wedstrijden live volgen via de livestream. Je hebt daarvoor een account met een storting nodig. ESPN zendt in Nederland een deel van de NBA-wedstrijden uit; in de programmagids zie je of deze erbij zit. Met <strong>NBA League Pass</strong>, de betaalde dienst van de competitie, kun je alle wedstrijden volgen. Meer opties vind je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk Bucks – Rockets live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Vannacht staan er meer duels op het programma. Lees ook onze voorspellingen voor <a href="/nieuws/pacers-76ers-voorspelling-wedtips-nba-2026">Pacers – 76ers</a>, <a href="/nieuws/mavericks-thunder-voorspelling-wedtips-nba-2026">Mavericks – Thunder</a> en <a href="/nieuws/clippers-lakers-voorspelling-wedtips-nba-2026">Clippers – Lakers</a>, en alle <a href="/nieuws/nba-voorspellingen-vannacht-29-oktober-2026">NBA-voorspellingen van 29 oktober</a>. Terugblikken? Lees onze voorspelling voor <a href="/nieuws/rockets-hawks-voorspelling-wedtips-nba-2026">Rockets – Hawks</a>. Benieuwd <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">welke Nederlanders in de NBA spelen</a>? Nieuw met basketbal? Lees <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels in de NBA</a>. Alle tips staan op <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Bucks – Rockets?</strong><br>Donderdag 29 oktober 2026 om 01:00 Nederlandse tijd, in de nacht van woensdag op donderdag. In Milwaukee is het dan woensdagavond 19:00.</p>
<p><strong>Speelt Alperen Şengün mee?</strong><br>Nee. Hij staat met rugklachten als 'speelt niet' op de officiële blessurelijst. Ook Steven Adams ontbreekt, achter Marcus Smart staat een vraagteken.</p>
<p><strong>Wie is favoriet: Bucks of Rockets?</strong><br>De Rockets, met een quotering van 1,30 bij TOTO. Milwaukee staat op 3,65.</p>
<p><strong>Wat is onze voorspelling voor Bucks – Rockets?</strong><br>De Rockets winnen met 111-117. Onze wedtip is Milwaukee Bucks +8,5 punten, inclusief verlenging (1,87 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

KAART = {"home": "Bucks", "away": "Rockets", "home_abbr": "mil", "away_abbr": "hou", "home_pos": "32-50 · nr. 11 Oost 2025/26", "away_pos": "52-30 · nr. 5 West 2025/26", "hs": 111, "as": 117, "datum": "Do 29 okt", "tijd": "01:00", "odd_home": "3,65", "odd_away": "1,30"}
WEDTIPS = {"wedtip-1-2": "Milwaukee Bucks +8,5 punten (incl. verlenging)", "quotering-wedtip-1": "1.87",
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
    assert not re.search(r"<(ul|ol|li)\b", html), "geen lijsten"
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"), "slotregel"
    hrefs = re.findall(r'href="([^"]+)"', html)
    assert hrefs and all(h.startswith("/") or h == BET365 for h in hrefs), [h for h in hrefs if not h.startswith("/")]
    toegestaan = {"/nieuws/nba-voorspellingen-vannacht-29-oktober-2026",
                  "/nieuws/nba-voorspellingen-vannacht-27-oktober-2026", "/nieuws/nba-voorspellingen-vannacht-26-oktober-2026",
                  "/nieuws/pacers-76ers-voorspelling-wedtips-nba-2026",
                  "/nieuws/mavericks-thunder-voorspelling-wedtips-nba-2026",
                  "/nieuws/clippers-lakers-voorspelling-wedtips-nba-2026",
                  "/nieuws/lakers-trail-blazers-voorspelling-wedtips-nba-2026",
                  "/nieuws/lakers-warriors-voorspelling-wedtips-nba-2026", "/nieuws/thunder-suns-voorspelling-wedtips-nba-2026",
                  "/nieuws/thunder-clippers-voorspelling-wedtips-nba-2026", "/nieuws/rockets-hawks-voorspelling-wedtips-nba-2026",
                  "/nieuws/heat-mavericks-voorspelling-wedtips-nba-2026", "/nieuws/76ers-pistons-voorspelling-wedtips-nba-2026",
                  "/nieuws/knicks-pistons-voorspelling-wedtips-nba-2026", "/nieuws/spurs-kings-voorspelling-wedtips-nba-2026",
                  "/nieuws/celtics-nets-voorspelling-wedtips-nba-2026",
                  "/nieuws/welke-nederlanders-spelen-in-de-nba",
                  "/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders",
                  "/nieuws/wat-is-handicap-wedden-de-complete-gids",
                  "/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners",
                  "/wedden-op-nba-voorspellingen-en-wedtips---basketbal", "/bookmakers/toto", "/bookmakers/bet365",
                  "/live-kijken", BET365}
    assert set(hrefs) <= toegestaan, set(hrefs) - toegestaan
    assert "/nieuws/nba-voorspellingen-vannacht-29-oktober-2026" in hrefs, "link naar het algemene artikel"
    vannacht = {"pacers-76ers", "mavericks-thunder", "clippers-lakers"}
    assert all(f"/nieuws/{s}-voorspelling-wedtips-nba-2026" in hrefs for s in vannacht), "3 andere previews"
    assert "/nieuws/rockets-hawks-voorspelling-wedtips-nba-2026" in hrefs, "eerder artikel van dezelfde ploeg"
    assert f"/nieuws/{SLUG}" not in hrefs, "geen link naar zichzelf"
    assert hrefs.count(BET365) == 2, "Bet365-CTA's zoals in het sjabloon"
    assert "<table" not in html.replace(f"<table {T}>", ""), "tabellen alleen via tabel()"
    verboden = ["BetCity", "ESPN-API", "ESPN.com", "Associated Press", "DraftKings", "Rotowire", "Betfans"]
    assert not any(v.lower() in html.lower() for v in verboden), "geen bronnen/concurrenten"
    # SEO
    fk = "Bucks – Rockets voorspelling"
    assert fk in TITEL and fk in SAMENVATTING and len(SAMENVATTING) <= 160
    assert fk in re.sub(r"<[^>]+>", "", content).split(".")[0], "focuskeyword in eerste zin"
    assert any(fk in h for h in re.findall(r"<h3><strong>(.*?)</strong></h3>", html)), "focuskeyword in h3"
    # Wedtip en consistentie
    assert set(WEDTIPS) == {"wedtip-1-2", "quotering-wedtip-1", "bookmaker-wedtips"}
    assert WEDTIPS["bookmaker-wedtips"] == "669ab9f5aceb8b717cea24c3"
    q = float(WEDTIPS["quotering-wedtip-1"])
    toto_odds = {3.65, 1.30, 4.00, 18.0, 1.29, 1.93, 1.73, 1.87, 1.95, 1.69, 2.00, 1.78}
    assert q in toto_odds and q == 1.87
    assert KAART["hs"] + 8.5 > KAART["as"], "voorspelde score moet Bucks +8,5 laten winnen"
    assert KAART["as"] > KAART["hs"], "voorspelling: Rockets winnen"
    assert f"{KAART['hs']}-{KAART['as']}" in content and f"{KAART['hs']}-{KAART['as']}" in content3
    assert KAART["odd_home"] == "3,65" and KAART["odd_away"] == "1,30" and KAART["tijd"] == "01:00"
    assert KAART["home_abbr"] == "mil" and KAART["away_abbr"] == "hou" and KAART["datum"] == "Do 29 okt"
    assert "1,87" in content and "1,87" in content3 and "woensdag rond 10:50 uur" in content2
    assert "Waarom niet een andere markt?" in content3
    assert all(f"<p><strong>{i}. " in content3 for i in (1, 2, 3)), "3 genummerde punten"
    assert content3.count("<p><strong>Hoe laat") + content3.count("<p><strong>Speelt") + \
        content3.count("<p><strong>Wie is favoriet") + content3.count("<p><strong>Wat is onze voorspelling") == 4, "4 FAQ"
    assert SLUG == "bucks-rockets-voorspelling-wedtips-nba-2026" and DATUM == "2026-10-29T00:00:00.000Z"
    tekst = re.sub(r"<[^>]+>", " ", html)
    woorden = len(tekst.split())
    assert 1300 <= woorden <= 1900, woorden
    print(len(TITEL), "tekens titel |", len(SAMENVATTING), "tekens samenvatting |", woorden, "woorden")
    print("Alle asserts geslaagd (dry run, niets gepubliceerd).")
