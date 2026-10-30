# -*- coding: utf-8 -*-
"""Los artikel: Mavericks – Rockets voorspelling, NBA 31 oktober 2026 (01:00 NL, wintertijd; vrijdag 19:00 CT), American Airlines Center Dallas.
Feiten nagelopen op 30-10-2026 rond 14:00 NL (ESPN-API: summary 401909283 incl. blessures en onderlinge stand; box scores
2026/27 401909840 (Rockets – Mavericks 128-110), 401909844, 401909858, 401909871, 401909891 (DAL) en 401909096, 401909856,
401909874, 401909887 (HOU); teamschema's 2025/26 (regulier en play-offs) en 2026/27; stand 2025/26; rosters en coaches;
spelersgemiddelden 2024/25, 2025/26 en 2026/27; onderlinge duels 2025/26 401810015, 401810211, 401810346, 401810556;
officiële NBA-blessurelijst 30-10 06:00 AM ET; berichtgeving over de contracten van Smart en Bogdanović (juli 2026) en de
ruil van Anthony Davis naar Washington (4-2-2026)).
- Rockets 2026/27: 128-110 DAL, 114-110 in SA, 121-114 in ATL, 120-110 ATL, 132-100 in MIL (zonder Şengün en Smart):
  marges 18, 4, 7, 10, 32 (gemiddeld +14,2); 123,0 voor / 108,8 tegen.
- Mavericks 2026/27: 110-128 in HOU (rust 38-70, 21 balverliezen), 121-105 in IND, 106-122 SA (zonder Flagg en Irving),
  113-109 in MIA, 120-96 OKC (OKC 5 uit 32 voor drie, Dallas 11 balverliezen). Balverliezen 85 in 5 duels (17,0).
- Onderling 2025/26: 2-2, telkens won de thuisploeg: 110-102 en 111-107 in Houston, 122-109 en 110-104 in Dallas.
  Dallas-zeges: in december zonder Şengün, in januari viel Şengün na 1 minuut uit. Irving en VanVleet speelden geen duel.
  Flagg 12, 19, 10, 34; Durant 21, 27, 34, 13.
- Blessurelijst 30-10 06:00 ET: HOU Adams out (rechterkuit/soleus), Sheppard out (onderrug), Şengün questionable (onderrug),
  Smart questionable (linkeronderarm), Copeland en Phillips out (G League). DAL de Larrea out (knie), Lively II out
  (voetoperatie), Aldama doubtful (knieoperatie), Biberović doubtful (hiel), Marshall questionable (ziek), Caleb Martin
  available (duimspalk). Smart speelde de laatste drie duels niet, Aldama nog geen enkel.
- Stand 2025/26: DAL 26-56 (nr. 12 West, 16-25/10-30, 114,1/119,6); HOU 52-30 (nr. 5 West, 30-11/22-19, 115,2/110,0),
  eerste ronde 2-4 tegen de Lakers.
- Rust: beide ploegen speelden woensdag (US) en hadden donderdag vrij.
- Twijfel/weggelaten: 'enige ongeslagen ploeg', details van de ruilen voor Risacher/Aldama, terugkeerdatum Lively II,
  of Şengün speelt, Rookie of the Year-titel Flagg, data van onderlinge duels (alleen maanden genoemd).
- Odds: alleen TOTO, uit specials/nba_feiten_2026_10_31.md (vrijdag ±13:45 NL). Winnaar, handicap en totaal incl. verlenging.
- Eén wedtip (vast, eigenaar): Houston Rockets -4,5 @1,63, onze kans ±64% (odd 61,3%, zonder marge ±56%).
  python3 specials/mavericks_rockets_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "Mavericks – Rockets voorspelling: wedtip en odds voor het ongeslagen Houston in Dallas (31 oktober, 01:00)"
SLUG = "mavericks-rockets-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("Mavericks – Rockets voorspelling: het ongeslagen Houston (5-0) speelt in Dallas, met een vraagteken achter "
                "Şengün. Wedtip, TOTO-odds en blessures.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet-experts.nl/go/bet365"
DATUM = "2026-10-31T00:00:00.000Z"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>Mavericks – Rockets voorspelling: in de nacht van vrijdag op zaterdag om 01:00 Nederlandse tijd krijgt Dallas de kans op revanche. In de eerste wedstrijd van het seizoen stond Houston bij rust met 70-38 voor en won het met 128-110. Sindsdien verloren de Rockets geen wedstrijd meer: ze staan op 5-0 en wonnen gemiddeld met veertien punten verschil. Dallas (3-2) won wel drie van de laatste vier wedstrijden, met Cooper Flagg in topvorm. Achter Alperen Şengün staat een vraagteken (rug). Onze voorspelling: Mavericks – Rockets 108-117. Onze wedtip: Houston Rockets -4,5 punten (inclusief verlenging) tegen een quotering van 1,63 bij TOTO.</strong></p>
<p>Hieronder lees je alles over vorm, blessures, de odds van <a href="/bookmakers/toto">TOTO</a> en onze onderbouwing.</p>
<h3><strong>Mavericks – Rockets: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "Dallas Mavericks – Houston Rockets"),
    ("Datum", "Zaterdag 31 oktober 2026 (vrijdagavond in de VS)"),
    ("Aanvang", "01:00 Nederlandse tijd (vrijdag 19:00 in Dallas)"),
    ("Arena", "American Airlines Center, Dallas"),
    ("Competitie", "NBA, reguliere competitie 2026/27"),
    ("Stand 2026/27", "Mavericks 3-2, Rockets 5-0"),
    ("Onderlinge duels 2025/26", "2-2, telkens won de thuisploeg"),
    ("Rust", "Beide ploegen speelden woensdag (Amerikaanse tijd) en hadden donderdag vrij"),
])}
<h3><strong>De eerste anderhalve week: Houston foutloos, Dallas herstelt</strong></h3>
<p><strong>Houston Rockets: vijf zeges, vier keer met vijf punten of meer</strong></p>
<p>Houston opende met de ruime zege op Dallas, waarin Kevin Durant en Jabari Smith Jr. allebei 30 punten maakten. Daarna volgden 114-110 in San Antonio en twee zeges op Atlanta (121-114 en 120-110). Woensdag won Houston met 132-100 in Milwaukee, zonder Şengün en Marcus Smart. Fred VanVleet scoorde 24 punten, Amen Thompson 23. Houston scoort 123 punten per wedstrijd en krijgt er 108,8 tegen.</p>
<p><strong>Dallas Mavericks: van 0-1 naar 3-2</strong></p>
<p>Na de nederlaag in Houston won Dallas met 121-105 in Indiana. Zonder Flagg en Kyrie Irving ging de thuisopener tegen San Antonio verloren (106-122). Daarna volgden 113-109 in Miami en woensdag 120-96 tegen Oklahoma City, met 26 punten en 8 assists van Flagg. Oklahoma City miste wel onder anderen Chet Holmgren en Jalen Williams en raakte maar 5 van zijn 32 driepunters.</p>
<h3><strong>Vorig seizoen en de onderlinge duels</strong></h3>
<p>Houston won in 2025/26 52 wedstrijden en verloor in de eerste ronde van de play-offs met 2-4 van de Lakers. Dallas speelde het hele seizoen zonder Irving (gescheurde kruisband), deed in februari Anthony Davis van de hand en eindigde als twaalfde in het Westen.</p>
{tabel(["2025/26", "Dallas Mavericks", "Houston Rockets"], [
    ("Eindstand", "26-56 (nr. 12 West)", "52-30 (nr. 5 West)"),
    ("Thuis / uit", "16-25 / 10-30", "30-11 / 22-19"),
    ("Punten voor / tegen", "114,1 / 119,6", "115,2 / 110,0"),
    ("Onderling", "2-2", "2-2"),
    ("Na het seizoen", "Play-offs niet gehaald", "Eerste ronde (2-4 tegen de Lakers)"),
])}
<p>De vier duels van vorig seizoen gingen allemaal naar de thuisploeg. Houston won in november met 110-102 en eind januari met 111-107, ondanks 34 punten van Flagg. Dallas won in december met 122-109 en in januari met 110-104, maar toen speelde Şengün niet of viel hij na één minuut uit, en had Dallas nog Davis. Irving en VanVleet speelden geen van de vier duels.</p>"""

content2 = f"""<h3><strong>Zo zijn beide selecties veranderd</strong></h3>
<p><strong>Dallas Mavericks: nieuwe coach, Irving terug</strong></p>
<p>Dusty May volgde deze zomer Jason Kidd op als coach. In de draft koos Dallas Morez Johnson Jr. als nummer negen, en via ruilen kwamen onder meer Zaccharie Risacher en Santi Aldama. De belangrijkste ‘aanwinst’ is Irving, die na zijn kruisbandblessure weer meespeelt.</p>
<p><strong>Houston Rockets: VanVleet terug, Smart en Bogdanović erbij</strong></p>
<p>VanVleet miste het hele vorige seizoen met een gescheurde kruisband en is terug als spelverdeler. Nieuw zijn Smart (van de Lakers) en Bogdan Bogdanović. Tari Eason bleef. Ime Udoka is nog altijd de coach.</p>
<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("Alperen Şengün", "Houston", "Twijfelachtig (onderrug); miste woensdag in Milwaukee"),
    ("Marcus Smart", "Houston", "Twijfelachtig (verrekte linkeronderarm); miste de laatste drie duels"),
    ("Reed Sheppard", "Houston", "Speelt niet (onderrug)"),
    ("Steven Adams", "Houston", "Speelt niet (verrekte rechterkuit)"),
    ("Naji Marshall", "Dallas", "Twijfelachtig (ziek); miste de laatste twee duels"),
    ("Santi Aldama, Tarik Biberović", "Dallas", "Zeer twijfelachtig (herstel na knieoperatie; hiel)"),
    ("Dereck Lively II, Sergio de Larrea", "Dallas", "Spelen niet (voetoperatie; rechterknie)"),
])}
<p><em>Stand van de officiële NBA-blessurelijst op vrijdag 30 oktober, 06:00 uur Amerikaanse tijd (11:00 Nederlandse tijd). Of Şengün speelt, wordt waarschijnlijk pas kort voor het begin bekend.</em></p>
<p><strong>Verwachte basisvijf Mavericks:</strong> Kyrie Irving, Max Christie, Cooper Flagg, P.J. Washington, Daniel Gafford. De vijf van elke wedstrijd waarin Flagg en Irving fit waren. Risacher, Johnson Jr., Marcus Sasser en Walter Clayton Jr. zijn de belangrijkste wissels.</p>
<p><strong>Verwachte basisvijf Rockets:</strong> Fred VanVleet, Amen Thompson, Kevin Durant, Jabari Smith Jr. en Alperen Şengün. Kan Şengün niet spelen, dan begint Eason, zoals woensdag in Milwaukee. Bogdanović, Clint Capela en Oscar Tshiebwe komen van de bank.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "2026/27 tot nu toe"], [
    ("Kevin Durant (HOU)", "26,0", "5,5", "4,8", "22,4 ptn, 54% uit het veld"),
    ("Alperen Şengün (HOU)", "20,4", "8,9", "6,2", "24,5 ptn, 9,0 reb, 7,0 ast"),
    ("Amen Thompson (HOU)", "18,3", "7,8", "5,3", "18,2 ptn, 8,0 reb"),
    ("Fred VanVleet (HOU)", "14,1*", "3,7*", "5,6*", "12,3 ptn, 6,5 ast"),
    ("Cooper Flagg (DAL)", "21,0", "6,7", "4,5", "25,3 ptn, 6,8 ast"),
    ("Kyrie Irving (DAL)", "24,7*", "4,8*", "4,6*", "18,0 ptn, 3,8 ast"),
    ("P.J. Washington (DAL)", "14,2", "7,0", "1,8", "16,0 ptn, 7,8 reb"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26. * VanVleet en Irving speelden in 2025/26 niet; bij hen staan de cijfers van 2024/25.</em></p>
<p><strong>Cooper Flagg</strong> is de motor van Dallas: in elke wedstrijd die hij uitspeelde scoorde hij minstens 26 punten, in Houston 32. <strong>Kevin Durant</strong> scoorde vorig seizoen gemiddeld bijna 24 punten tegen Dallas. Speelt <strong>Alperen Şengün</strong>, dan heeft Houston zijn beste passer terug.</p>
<h3><strong>Odds Mavericks – Rockets bij TOTO</strong></h3>
<p>TOTO ziet Houston als duidelijke favoriet: een quotering van 1,43 staat voor ongeveer 70 procent winkans. De handicap ligt rond de 6,5 punten in het voordeel van de Rockets, het verwachte puntentotaal rond de 225 punten.</p>
{tabel(["Markt (TOTO)", "Mavericks", "Rockets"], [
    ("Winnaar (incl. verlenging)", "2,90", "1,43"),
    ("1X2 (reguliere speeltijd, gelijk 20,00)", "3,00", "1,40"),
    ("Handicap +4,5 / -4,5 (incl. verlenging)", "2,10", "1,63"),
    ("Handicap +5,5 / -5,5 (incl. verlenging)", "1,95", "1,73"),
    ("Handicap +6,5 / -6,5 (incl. verlenging)", "1,91", "1,91"),
    ("Handicap +7,5 / -7,5 (incl. verlenging)", "1,73", "1,95"),
])}
<p>Op het totaal (inclusief verlenging) biedt TOTO onder meer 224,5 punten (Over 1,77 / Under 1,91) en 225,5 punten (Over 1,93 / Under 1,87). Odds gelezen op vrijdag rond 13:45 uur; vergelijk ze vlak voor de start nog even, zeker zodra bekend is of Şengün speelt.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op Mavericks – Rockets</strong></a></p>"""

content3 = f"""<h3><strong>Mavericks – Rockets voorspelling: Houston wint ook in Dallas</strong></h3>
<p>Houston is de completere ploeg: Durant, Thompson en Smith Jr. zijn in vorm, VanVleet geeft rust aan de bal en woensdag bleek dat het ook zonder Şengün kan. Wel ontbreken Sheppard, Adams en mogelijk Smart.</p>
<p>Dallas speelt thuis en is beter dan in de eerste week, maar de zege op Oklahoma City kwam tegen een zwaar gehavende tegenstander. In Houston won Dallas de tweede helft (72-58), toen de wedstrijd al beslist was. Onze voorspelling: <strong>Dallas Mavericks – Houston Rockets 108-117</strong>.</p>
<h3><strong>Onze wedtip: Rockets -4,5 (1,63)</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Onze kans"], [
    ("Houston Rockets -4,5 punten (incl. verlenging)", "1,63", "TOTO", "Ongeveer 64 procent"),
])}
<p><strong>Waarom deze tip?</strong> Bij een handicap van -4,5 worden er 4,5 punten van de score van Houston afgetrokken, een eventuele verlenging meegeteld. Een rekenvoorbeeld: wint Houston met 117-108 (negen punten), dan houd je na aftrek 4,5 punten over en wint de tip. Wint Houston met 112-108 (vier punten) of wint Dallas, dan verlies je. Een odd van 1,63 staat voor een kans van ruim 61 procent; zonder de marge van de bookmaker is dat ongeveer 56 procent. Wij schatten de kans op ongeveer 64 procent. De onderbouwing:</p>
<p><strong>1. Elke zege was ruim genoeg, op één na.</strong> Houston won zijn vijf wedstrijden met 18, 4, 7, 10 en 32 punten verschil, gemiddeld met ruim veertien punten. Vier van de vijf keer zou deze handicap gewonnen hebben, ook woensdag zonder Şengün.</p>
<p><strong>2. Het eerste duel was eenzijdig.</strong> Bij rust stond het 70-38 en de voorsprong liep op tot 37 punten. Dallas verloor 21 keer de bal en Houston scoorde 29 punten uit de break. Balverlies blijft het zwakke punt van Dallas (17 per wedstrijd).</p>
<p><strong>3. Meer wapens dan Dallas.</strong> Houston heeft met Durant, Thompson, Smith Jr. en VanVleet vier spelers die een wedstrijd kunnen dragen. Bij Dallas rust veel op Flagg, en vorig seizoen verloor Dallas thuis 25 van zijn 41 wedstrijden.</p>
<p><strong>Waarom niet een andere markt?</strong> Een zege van Houston (1,43) vraagt om 70 procent kans. Wij komen uit op ongeveer 73 procent: een te klein verschil voor zo'n lage odd. Rockets -6,5 (1,91) en -7,5 (1,95) betalen meer uit, maar liggen dicht bij onze voorspelde marge van negen punten. Met de onzekerheid rond Şengün nemen we liever de extra ruimte van -4,5. Het puntentotaal laten we liggen: onze voorspelling komt uit op 225 punten, precies rond de lijn van TOTO.</p>
<p><strong>Het risico.</strong> Vorig seizoen won Dallas beide thuisduels tegen Houston, al ontbrak Şengün toen (bijna) helemaal. Flagg kan een wedstrijd in zijn eentje openbreken, en in San Antonio won Houston maar met vier punten. Let op: de handicap telt een eventuele verlenging mee. Meer uitleg vind je in onze gidsen over <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap wedden</a> en de <a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">money line</a>.</p>
<h3><strong>Mavericks – Rockets live kijken in Nederland</strong></h3>
<p>Bij <a href="/bookmakers/bet365">Bet365</a> kun je NBA-wedstrijden live volgen via de livestream. Je hebt daarvoor een account met een storting nodig. ESPN zendt in Nederland een deel van de NBA-wedstrijden uit; in de programmagids zie je of deze erbij zit. Met <strong>NBA League Pass</strong>, de betaalde dienst van de competitie, kun je alle wedstrijden volgen. Meer opties vind je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk Mavericks – Rockets live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Vannacht schreven we ook voorbeschouwingen van <a href="/nieuws/76ers-knicks-voorspelling-wedtips-nba-2026">76ers – Knicks</a>, <a href="/nieuws/warriors-lakers-voorspelling-wedtips-nba-2026">Warriors – Lakers</a> en <a href="/nieuws/suns-nuggets-voorspelling-wedtips-nba-2026">Suns – Nuggets</a>. Eerder deze week schreven we over <a href="/nieuws/mavericks-thunder-voorspelling-wedtips-nba-2026">Mavericks – Thunder</a> en <a href="/nieuws/bucks-rockets-voorspelling-wedtips-nba-2026">Bucks – Rockets</a>. Benieuwd <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">welke Nederlanders in de NBA spelen</a>? Nieuw met basketbal? Lees <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels in de NBA</a>. Alle tips staan op <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Mavericks – Rockets?</strong><br>Zaterdag 31 oktober 2026 om 01:00 Nederlandse tijd, in de nacht van vrijdag op zaterdag. In Dallas is het dan vrijdag 19:00.</p>
<p><strong>Speelt Alperen Şengün mee?</strong><br>Dat is nog niet zeker. Hij staat met klachten aan zijn onderrug als twijfelachtig op de officiële NBA-blessurelijst en miste woensdag de wedstrijd in Milwaukee. Reed Sheppard en Steven Adams spelen niet.</p>
<p><strong>Wie is favoriet: Mavericks of Rockets?</strong><br>De Rockets, met een quotering van 1,43 bij TOTO. Dallas staat op 2,90.</p>
<p><strong>Wat is onze voorspelling voor Mavericks – Rockets?</strong><br>Houston wint met 108-117. Onze wedtip is Houston Rockets -4,5 punten, inclusief verlenging (1,63 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

KAART = {"home": "Mavericks", "away": "Rockets", "home_abbr": "dal", "away_abbr": "hou", "home_pos": "26-56 · nr. 12 West 2025/26", "away_pos": "52-30 · nr. 5 West 2025/26", "hs": 108, "as": 117, "datum": "Za 31 okt", "tijd": "01:00", "odd_home": "2,90", "odd_away": "1,43"}
WEDTIPS = {"wedtip-1-2": "Houston Rockets -4,5 punten (incl. verlenging)", "quotering-wedtip-1": "1.63",
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
                  "/nieuws/warriors-lakers-voorspelling-wedtips-nba-2026",
                  "/nieuws/suns-nuggets-voorspelling-wedtips-nba-2026",
                  "/nieuws/welke-nederlanders-spelen-in-de-nba",
                  "/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders",
                  "/nieuws/wat-is-handicap-wedden-de-complete-gids",
                  "/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners",
                  "/wedden-op-nba-voorspellingen-en-wedtips---basketbal", "/bookmakers/toto", "/bookmakers/bet365",
                  "/live-kijken", BET365}
    assert set(hrefs) <= toegestaan, set(hrefs) - toegestaan
    assert SLUG not in "".join(hrefs), "niet naar zichzelf linken"
    for s in ("76ers-knicks", "warriors-lakers", "suns-nuggets"):
        assert f"/nieuws/{s}-voorspelling-wedtips-nba-2026" in hrefs, f"link naar {s} ontbreekt"
    assert "/nieuws/mavericks-thunder-voorspelling-wedtips-nba-2026" in hrefs, "eerder artikel Dallas"
    assert "/nieuws/bucks-rockets-voorspelling-wedtips-nba-2026" in hrefs, "eerder artikel Houston"
    assert "nba-voorspellingen-vannacht" not in "".join(hrefs), "vannacht geen algemeen artikel"
    assert "<table" not in html.replace(f"<table {T}>", ""), "tabellen alleen via tabel()"
    verboden = ["BetCity", "ESPN-API", "ESPN.com", "Associated Press", "DraftKings", "Rotowire", "Betfans", "Shams",
                "Klutch", "Charania", "Spotrac"]
    assert not any(v.lower() in html.lower() for v in verboden), "geen bronnen/concurrenten"
    # SEO: focuskeyword
    fk = "Mavericks – Rockets voorspelling"
    assert fk in TITEL and fk in SAMENVATTING and len(SAMENVATTING) <= 160, len(SAMENVATTING)
    assert "31 oktober, 01:00" in TITEL
    assert re.sub(r"<[^>]+>", "", content).startswith(fk), "focuskeyword in de eerste zin"
    assert any(fk in h for h in re.findall(r"<h3>(.*?)</h3>", html)), "focuskeyword in een h3"
    # Wedtip en consistentie
    assert set(WEDTIPS) == {"wedtip-1-2", "quotering-wedtip-1", "bookmaker-wedtips"}
    assert WEDTIPS["bookmaker-wedtips"] == "669ab9f5aceb8b717cea24c3"
    q = float(WEDTIPS["quotering-wedtip-1"])
    toto_odds = {2.90, 1.43, 3.00, 1.40, 2.10, 1.63, 1.95, 1.73, 1.91, 2.10}
    assert q in toto_odds and q == 1.63
    assert KAART["as"] - KAART["hs"] >= 5 and KAART["as"] - KAART["hs"] > 4.5, "voorspelde score moet Rockets -4,5 laten winnen"
    assert KAART["as"] > KAART["hs"], "voorspelling: Rockets winnen"
    assert f"{KAART['hs']}-{KAART['as']}" in content and f"{KAART['hs']}-{KAART['as']}" in content3
    assert KAART["odd_home"] == "2,90" and KAART["odd_away"] == "1,43" and KAART["tijd"] == "01:00"
    assert KAART["home_abbr"] == "dal" and KAART["away_abbr"] == "hou" and KAART["datum"] == "Za 31 okt"
    assert KAART["home"] == "Mavericks" and KAART["away"] == "Rockets"
    assert "1,63" in content and "1,63" in content3 and "-4,5" in content and "-4,5" in content3
    assert "incl. verlenging" in WEDTIPS["wedtip-1-2"] and "inclusief verlenging" in content
    assert "vrijdag rond 13:45 uur" in html, "tijdstip odds"
    assert html.count("👉 Klik hier: maak je Bet365-account aan en wed live mee op") == 1
    assert len(re.findall(r"<p><strong>[123]\. ", content3)) == 3, "onderbouwing in 3 punten"
    assert "Waarom niet een andere markt?" in content3
    assert "rekenvoorbeeld" in content3.lower(), "rekenvoorbeeld handicap"
    assert len(re.findall(r"<p><strong>[^<]*\?</strong><br>", content3)) == 4, "4 FAQ-vragen"
    assert SLUG == "mavericks-rockets-voorspelling-wedtips-nba-2026" and DATUM == "2026-10-31T00:00:00.000Z"
    tekst = re.sub(r"<[^>]+>", " ", html)
    woorden = len(tekst.split())
    assert 1400 <= woorden <= 1850, woorden
    print(len(TITEL), "tekens titel |", len(SAMENVATTING), "tekens samenvatting |", woorden, "woorden")
    print("Alle asserts geslaagd (dry run, niets gepubliceerd).")
