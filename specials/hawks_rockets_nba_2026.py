# -*- coding: utf-8 -*-
"""Los artikel: Hawks – Rockets voorspelling, NBA 25 oktober 2026 (02:30 NL, nog zomertijd), State Farm Arena Atlanta.
Feiten nagelopen op 24-10-2026 (ESPN-API: summary 401909856, boxscores 401909834, 401909843, 401909840 en 401909096,
scoreboards 21/23/24-10, schema's en standen 2025/26, onderlinge duels 401810537 en 401810873, spelersgemiddelden 2025/26;
NBA-injury reports 23-10 20:15 ET en 24-10 06:30 ET: Hawks en Rockets voor dit duel nog 'not yet submitted').
- Hawks: 132-125 in Orlando, 128-81 in Charlotte (grootste zege uit de clubgeschiedenis, 47 punten; vorig record 46).
- Rockets: 128-110 tegen Dallas, 114-110 tegen de Spurs in Austin (Thompson blokte Wembanyama in de laatste seconde).
- Onderling 2025/26: 86-104 (in Atlanta, 29-1, Johnson ontbrak) en 117-95 (in Houston, 20-3), allebei Houston.
- Return al op 26-10 in Houston (27-10 01:30 NL, wintertijd).
- Odds: alleen TOTO, uit specials/nba_feiten_2026_10_25.md (±12:50 NL op 24-10). 'Winnaar' = incl. verlenging.
- Eén wedtip (eis eigenaar): Hawks wint @1,83, onze kans 58% (markt 54,6%).
  ../superodd-agent/.venv/bin/python specials/hawks_rockets_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "Hawks – Rockets voorspelling: wedtip en odds voor twee ongeslagen ploegen (25 oktober, 02:30)"
SLUG = "hawks-rockets-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("Atlanta en Houston staan allebei op 2-0 en spelen allebei hun tweede duel in twee dagen. Voorspelling, "
                "onze wedtip, TOTO-odds, blessures en opstellingen.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet-experts.nl/go/bet365"
DATUM = "2026-10-25T00:30:00.000Z"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>In de nacht van zaterdag op zondag om 02:30 Nederlandse tijd ontvangen de Atlanta Hawks de Houston Rockets. Beide ploegen begonnen het seizoen met twee zeges en spelen allebei hun tweede wedstrijd in twee dagen. Het verschil zit in hoe die vrijdagavond verliep: Atlanta won met 47 punten verschil in Charlotte en liet de basisspelers rusten, Houston moest in Austin tot de laatste seconde knokken tegen de Spurs. Onze voorspelling: de Hawks winnen met 116-111. Onze wedtip: Atlanta Hawks wint (inclusief verlenging) tegen een quotering van 1,83 bij TOTO.</strong></p>
<p>Hieronder lees je alles over vorm, blessures, de odds van <a href="/bookmakers/toto">TOTO</a> en onze onderbouwing.</p>
<h3><strong>Hawks – Rockets: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "Atlanta Hawks – Houston Rockets"),
    ("Datum", "Zondag 25 oktober 2026 (nacht van zaterdag op zondag)"),
    ("Aanvang", "02:30 Nederlandse tijd (zaterdag 20:30 in Atlanta)"),
    ("Arena", "State Farm Arena, Atlanta"),
    ("Competitie", "NBA, reguliere competitie 2026/27"),
    ("Stand 2026/27", "Hawks 2-0, Rockets 2-0"),
    ("Onderlinge duels 2025/26", "2-0 voor Houston"),
])}
<p>Let op: in deze nacht gaat de klok in Nederland om 03:00 een uur terug. De wedstrijd begint dus nog in zomertijd. De return volgt al maandagavond in Houston (in Nederland dinsdag 27 oktober om 01:30).</p>
<h3><strong>Twee keer 2-0, maar een heel andere vrijdag</strong></h3>
<p><strong>Atlanta Hawks: recordzege in Charlotte</strong></p>
<p>De Hawks openden woensdag met een 132-125 zege in Orlando (Nickeil Alexander-Walker 31 punten, Jalen Johnson 20 punten en 14 rebounds). Vrijdag won Atlanta met 128-81 in Charlotte, een verschil van 47 punten. Johnson had 19 punten en 8 assists, invaller Aaron Wiggins maakte 19 punten en Dyson Daniels pakte 7 steals. De Hornets verloren de bal 27 keer. Belangrijk voor vannacht: geen enkele basisspeler van Atlanta stond langer dan 29 minuten op het veld.</p>
<p><strong>Houston Rockets: zwaar bevochten zege in Austin</strong></p>
<p>Houston begon met een 128-110 thuiszege op Dallas, waarin Kevin Durant en Jabari Smith Jr. allebei 30 punten scoorden. Vrijdagavond won de ploeg van coach Ime Udoka met 114-110 van San Antonio in Austin. Alperen Şengün maakte 29 punten en Amen Thompson voorkwam in de laatste seconde met een block op Victor Wembanyama de gelijkmaker. Dat kostte veel energie: Durant speelde 37 minuten, Şengün en Thompson 36, Smith Jr. 34 en Fred VanVleet 32. Daarna volgde nog een vlucht van ruim 1.300 kilometer naar Atlanta, terwijl de Hawks uit Charlotte nog geen 400 kilometer hoefden te reizen.</p>
<h3><strong>Vorig seizoen en de onderlinge duels</strong></h3>
<p>Houston was in 2025/26 de sterkere ploeg, terwijl VanVleet het hele seizoen ontbrak met een gescheurde kruisband. Atlanta won de Southeast Division. Beide ploegen strandden in de eerste ronde van de play-offs.</p>
{tabel(["2025/26", "Atlanta Hawks", "Houston Rockets"], [
    ("Eindstand", "46-36 (nr. 6 Oost)", "52-30 (nr. 5 West)"),
    ("Thuis / uit", "24-17 / 22-19", "30-11 / 22-19"),
    ("Punten voor / tegen", "118,5 / 116,0", "115,2 / 110,0"),
    ("Tweede duel van een back-to-back", "6-7", "7-7"),
    ("Play-offs", "Eerste ronde (2-4 tegen New York)", "Eerste ronde (2-4 tegen de Lakers)"),
])}
<p>Beide onderlinge duels gingen vorig seizoen naar Houston: 104-86 in Atlanta op 29 januari en 117-95 in Houston op 20 maart. Durant scoorde 31 en 25 punten. Wel ontbrak Johnson in januari met een kuitblessure, en nieuwkomers als Luguentz Dort, Wiggins, Jock Landale en rookie Kingston Flemings (nummer acht van de draft) waren er nog niet bij.</p>"""

content2 = f"""<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("Mouhamed Gueye", "Atlanta", "Speelt niet (gebroken linkervoet)"),
    ("Henri Veesaar", "Atlanta", "Speelt niet (gescheurde kruisband, seizoen voorbij)"),
    ("Jock Landale", "Atlanta", "Speelt met een gebroken neus, was vrijdag gewoon inzetbaar"),
    ("RayJ Dennis, Keshon Gilbert, Jalen Wilson", "Atlanta", "Vrijdag niet bij de ploeg (G League)"),
    ("Reed Sheppard", "Houston", "Miste vrijdag de wedstrijd (botkneuzing linkerknie), status vannacht onbekend"),
    ("Steven Adams", "Houston", "Was vrijdag twijfelachtig (kuit), speelde toen 9 minuten"),
    ("Fred VanVleet", "Houston", "Niet geblesseerd gemeld, speelde vrijdag 32 minuten"),
])}
<p><em>Stand van de officiële NBA-blessurelijst van vrijdagavond. Op zaterdag om 12:30 Nederlandse tijd hadden beide clubs hun lijst voor dit duel nog niet ingediend.</em></p>
<p>Het grootste vraagteken is VanVleet. Hij stond vrijdag niet op de blessurelijst, maar dit is zijn eerste back-to-back na een jaar zonder wedstrijden door zijn kruisbandblessure. Krijgt hij rust, dan nemen Marcus Smart en Thompson de opbouw over.</p>
<p><strong>Verwachte basisvijf Atlanta:</strong> Dyson Daniels, Nickeil Alexander-Walker, CJ McCollum, Jalen Johnson, Onyeka Okongwu. Dezelfde vijf als in de eerste twee wedstrijden. Dort, Wiggins, Flemings, Landale en Corey Kispert vormen een brede bank.</p>
<p><strong>Verwachte basisvijf Houston:</strong> Fred VanVleet, Amen Thompson, Kevin Durant, Jabari Smith Jr., Alperen Şengün. Tari Eason, Smart, Bogdan Bogdanović, Adams en Clint Capela zijn de belangrijkste wissels.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "Bijzonderheid"], [
    ("Jalen Johnson (ATL)", "22,5", "10,3", "7,9", "Dit seizoen 19,5 punten, 10,5 rebounds en 7 assists"),
    ("Kevin Durant (HOU)", "26,0", "5,5", "4,8", "52% uit het veld, 41% driepunters"),
    ("Alperen Şengün (HOU)", "20,4", "8,9", "6,2", "29 punten tegen de Spurs"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26.</em></p>
<p><strong>Jalen Johnson</strong> is sinds het vertrek van Trae Young het middelpunt van Atlanta en kwam vorig seizoen bijna aan een triple-double per wedstrijd; zijn duel met Thompson is een wedstrijd in de wedstrijd. <strong>Kevin Durant</strong> blijft op zijn 38e de afmaker van Houston, al staan er met Daniels en Dort twee lastige verdedigers tegenover hem. <strong>Alperen Şengün</strong> is de spil van de Rockets-aanval en scoorde vrijdag acht punten op rij in het slotkwart. Okongwu en Landale krijgen het fysiek zwaar.</p>
<h3><strong>Odds Hawks – Rockets bij TOTO</strong></h3>
<p>TOTO ziet Atlanta als lichte favoriet: 1,83 staat voor ongeveer 55 procent winkans. Het verwachte puntentotaal ligt op 229,5.</p>
{tabel(["Markt (TOTO)", "Hawks", "Rockets"], [
    ("Winnaar (incl. verlenging)", "1,83", "2,00"),
    ("1X2 (reguliere speeltijd, gelijk 16,00)", "1,87", "2,05"),
    ("Handicap -1,5 / +1,5 (incl. verlenging)", "1,91", "1,91"),
    ("Handicap -2,5 / +2,5 (incl. verlenging)", "1,95", "1,73"),
    ("Handicap -3,5 / +3,5 (incl. verlenging)", "2,10", "1,63"),
])}
<p>Op het totaal biedt TOTO 228,5 punten (Over 1,77 / Under 1,91), 229,5 (1,91 / 1,91) en 230,5 (Over 1,93 / Under 1,77). Odds gelezen op zaterdag rond 12:50 uur; vergelijk ze vlak voor de start nog even.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op Hawks – Rockets</strong></a></p>"""

content3 = f"""<h3><strong>Onze voorspelling: Atlanta profiteert van de frissere benen</strong></h3>
<p>Uitgerust zou dit een toss-up zijn, met Houston als iets betere ploeg. Maar het verschil in vermoeidheid is groot. De vijf basisspelers van Houston speelden vrijdag samen 175 minuten in een wedstrijd die tot de laatste seconde spannend bleef, en reisden daarna van Austin naar Atlanta. De basisspelers van de Hawks hadden aan 123 minuten genoeg en hoefden maar een kort stuk naar huis.</p>
<p>Daarnaast heeft Atlanta een bredere selectie: Wiggins, Flemings, Dort en Landale speelden vrijdag allemaal minstens 18 minuten. Bij Houston is de bank smaller zonder Sheppard, en Adams speelde vrijdag met een kuitprobleem maar 9 minuten. De verdediging van de Hawks, met Daniels en Dort, dwong in twee wedstrijden samen 47 balverliezen af. Tegen een vermoeide tegenstander levert dat makkelijke punten op.</p>
<p>Houston houdt het voordeel onder de ring en heeft met Durant een speler die een wedstrijd alleen kan beslissen. Daarom verwachten we geen ruime zege. Onze voorspelling: <strong>Atlanta Hawks – Houston Rockets 116-111</strong>.</p>
<h3><strong>Onze wedtip voor Hawks – Rockets</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Onze kans"], [
    ("Atlanta Hawks wint (incl. verlenging)", "1,83", "TOTO", "58%"),
])}
<p><strong>Atlanta Hawks wint (1,83).</strong> De quotering van 1,83 staat voor ongeveer 55 procent kans; zonder de marge van de bookmaker is dat zo'n 52 procent. Wij schatten de kans op een zege van Atlanta op 58 procent. Die inschatting rust op drie punten. Ten eerste het verschil in vermoeidheid: de Rockets speelden een zware, lange wedstrijd en reisden ver, de Hawks konden hun belangrijkste spelers sparen. Ten tweede het thuisvoordeel: Atlanta won vorig seizoen 24 van de 41 thuiswedstrijden. Ten derde de breedte van de selectie, die op de tweede avond van een back-to-back extra zwaar weegt. Het risico: Durant en Şengün maken het verschil in de slotfase, en vorig seizoen won Houston beide duels ruim.</p>
<p>Waarom deze markt? De 1X2-markt (1,87) telt alleen de reguliere speeltijd: bij een gelijke stand verlies je ook als Atlanta in de verlenging wint. Bij een handicap moet Atlanta met twee of drie punten verschil winnen, terwijl gelijkwaardige duels vaak met een of twee punten worden beslist. Op het puntentotaal zien we te weinig houvast: de onderlinge duels van vorig seizoen bleven ver onder de lijn (190 en 212 punten), maar Atlanta scoorde dit seizoen al 132 en 128. De winnaarsmarkt biedt de beste verhouding tussen onze inschatting en de quotering.</p>
<p>Krijgt VanVleet rust, dan zakt de quotering op Atlanta waarschijnlijk. Meer uitleg over deze markten vind je in onze gidsen over <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap wedden</a> en de <a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">money line</a>.</p>
<h3><strong>Hawks – Rockets live kijken in Nederland</strong></h3>
<p>Bij <a href="/bookmakers/bet365">Bet365</a> kun je NBA-wedstrijden live volgen via de livestream. Je hebt daarvoor een account met een storting nodig. ESPN zendt in Nederland een deel van de NBA-wedstrijden uit; in de programmagids zie je of deze erbij zit. Met <strong>NBA League Pass</strong>, de betaalde dienst van de competitie, kun je alle wedstrijden volgen. Meer opties vind je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk Hawks – Rockets live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Lees ook onze voorspelling voor <a href="/nieuws/spurs-rockets-voorspelling-wedtips-nba-2026">Spurs – Rockets</a>, de <a href="/nieuws/nba-voorspellingen-vannacht-24-oktober-2026">NBA-voorspellingen van 24 oktober</a> (met Hornets – Hawks) en <a href="/nieuws/pacers-mavericks-voorspelling-wedtips-nba-2026">Pacers – Mavericks</a>. Benieuwd <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">welke Nederlanders in de NBA spelen</a>? Nieuw met basketbal? Lees <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels in de NBA</a>. Alle tips staan op <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Hawks – Rockets?</strong><br>Zondag 25 oktober 2026 om 02:30 Nederlandse tijd, in de nacht van zaterdag op zondag. Dat is nog zomertijd: de klok gaat pas om 03:00 terug. In Atlanta is het dan zaterdagavond 20:30.</p>
<p><strong>Spelen beide ploegen een back-to-back?</strong><br>Ja. Atlanta won vrijdag met 128-81 in Charlotte, Houston met 114-110 van de Spurs in Austin.</p>
<p><strong>Speelt Fred VanVleet mee?</strong><br>Hij staat niet op de blessurelijst en speelde vrijdag 32 minuten. Omdat het zijn eerste back-to-back van het seizoen is, na een jaar zonder wedstrijden door een kruisbandblessure, is rust niet uitgesloten. Reed Sheppard miste vrijdag de wedstrijd met een knieblessure.</p>
<p><strong>Wie is favoriet: Hawks of Rockets?</strong><br>De Hawks, maar nipt: 1,83 bij TOTO, tegenover 2,00 voor de Rockets.</p>
<p><strong>Wat is onze voorspelling voor Hawks – Rockets?</strong><br>De Hawks winnen met 116-111. Onze wedtip is een zege van Atlanta, inclusief verlenging (1,83 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

KAART = {"home": "Hawks", "away": "Rockets", "home_abbr": "atl", "away_abbr": "hou", "home_pos": "46-36 · nr. 6 Oost 2025/26", "away_pos": "52-30 · nr. 5 West 2025/26", "hs": 116, "as": 111, "datum": "Zo 25 okt", "tijd": "02:30", "odd_home": "1,83", "odd_away": "2,00"}
WEDTIPS = {"wedtip-1-2": "Atlanta Hawks wint (incl. verlenging)", "quotering-wedtip-1": "1.83",
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
