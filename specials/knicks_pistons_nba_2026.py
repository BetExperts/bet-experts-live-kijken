# -*- coding: utf-8 -*-
"""Los artikel: Knicks – Pistons voorspelling, NBA 28 oktober 2026 (01:00 NL, wintertijd; dinsdag 20:00 ET), Madison Square Garden.
Feiten nagelopen op 27-10-2026 rond 11:00 NL (ESPN-API: summary 401909878 incl. blessures; boxscores 401909089 (Knicks – 76ers
100-106), 401909095 (Celtics – Knicks 107-103), 401909863 (Knicks – Magic 102-111), 401909088 (Pistons – Celtics 121-113),
401909847 (Heat – Pistons 111-128) en 401909866 (76ers – Pistons 93-106); teamschema's 2025/26 (regulier + play-offs) en 2026/27;
standen 2025/26 en 2026/27; rosters en coaches; spelersgemiddelden; onderlinge duels 2025/26 401810357, 401810597, 401810651;
officiële NBA-blessurelijst 27-10 05:45 ET).
- Mikal Bridges: speelde WEL alle drie de duels als basisspeler (33, 22 en 35 min.): 4, 0 en 6 punten, 5 uit 23, 0 uit 10 voor drie.
  Het feitenblad (geen minuut gespeeld) klopt dus niet. Geen blessure, geen transfer; hij staat niet op de blessurelijst.
- Coach Knicks: Mike Brown. Coach Pistons: J.B. Bickerstaff.
- Knicks 2025/26: 53-29 (nr. 3 Oost), thuis 30-10, uit 22-19 (+1 zege neutraal), 116,5/110,1; kampioen (4-2 ATL, 4-0 PHI,
  4-0 CLE, 4-1 SA in de finale); NBA Cup 124-113 tegen SA (telt niet mee in de stand).
- Pistons 2025/26: 60-22 (nr. 1 Oost), thuis 31-9, uit 28-13 (+1 zege neutraal), 117,8/109,6; 4-3 tegen ORL (na 1-3),
  3-4 tegen CLE in de tweede ronde (na 2-0).
- Onderling 2025/26: 3-0 DET (121-90 en 118-80 in Detroit, 126-111 in New York). Duren miste de laatste twee (knie, schorsing).
- 2026/27: Knicks scoren 101,7 per duel, het laagste van de competitie; Pistons de enige ongeslagen ploeg in het Oosten.
- Beide ploegen spelen woensdag (US) alweer: NY in Chicago, DET thuis tegen Charlotte.
- Odds: alleen TOTO, uit specials/nba_feiten_2026_10_28.md (dinsdag ±10:45 NL). Winnaar, handicap en totaal incl. verlenging.
- Eén wedtip (eis eigenaar): Detroit Pistons +3,5 @1,95, onze kans 57% (odd 51,3%; zonder marge ±49%).
  python3 specials/knicks_pistons_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "Knicks – Pistons voorspelling: wedtip en odds, kampioen New York nog zonder zege (28 oktober, 01:00)"
SLUG = "knicks-pistons-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("Knicks – Pistons voorspelling: kampioen New York (0-3) ontvangt het ongeslagen Detroit, zonder Duren. "
                "Onze wedtip, TOTO-odds en opstellingen.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet-experts.nl/go/bet365"
DATUM = "2026-10-28T00:00:00.000Z"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>Deze Knicks – Pistons voorspelling draait om een opvallende start van het seizoen: kampioen New York verloor zijn eerste drie wedstrijden, Detroit won ze alle drie. In de nacht van dinsdag op woensdag om 01:00 Nederlandse tijd staan ze tegenover elkaar in Madison Square Garden. De Knicks scoren tot nu toe het minst van alle dertig ploegen, de Pistons missen hun center Jalen Duren. Onze voorspelling: Knicks – Pistons 107-110. Onze wedtip: Detroit Pistons +3,5 punten (inclusief verlenging) tegen een quotering van 1,95 bij TOTO.</strong></p>
<p>Hieronder lees je alles over vorm, blessures, de odds van <a href="/bookmakers/toto">TOTO</a> en onze onderbouwing.</p>
<h3><strong>Knicks – Pistons: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "New York Knicks – Detroit Pistons"),
    ("Datum", "Woensdag 28 oktober 2026 (dinsdagavond in New York)"),
    ("Aanvang", "01:00 Nederlandse tijd (20:00 in New York)"),
    ("Arena", "Madison Square Garden, New York"),
    ("Competitie", "NBA, reguliere competitie 2026/27"),
    ("Stand 2026/27", "Knicks 0-3, Pistons 3-0"),
    ("Onderlinge duels 2025/26", "3-0 voor de Pistons"),
])}
<p>Beide ploegen speelden zondag (Amerikaanse tijd) en hadden maandag een rustdag. Woensdag spelen ze allebei alweer: New York in Chicago, Detroit thuis tegen Charlotte.</p>
<h3><strong>De eerste week: Detroit loopt, New York hapert</strong></h3>
<p><strong>New York Knicks: drie keer net tekort</strong></p>
<p>De ploeg van coach Mike Brown verloor de opener thuis met 100-106 van Philadelphia. Jalen Brunson maakte 21 punten, maar raakte maar 6 van zijn 19 schoten. In Boston volgde een 107-103 nederlaag, ondanks 22 punten en 10 rebounds van Karl-Anthony Towns en 20 punten, 10 rebounds en 8 assists van OG Anunoby. Zondag ging het thuis tegen Orlando mis in het laatste kwart: New York stond na drie kwarten 75-71 voor, maar kreeg er in de laatste twaalf minuten 40 tegen en verloor met 102-111. Brunson scoorde 28 punten, met 12 uit 28.</p>
<p>De Knicks verloren dus drie keer met hooguit negen punten verschil. Het probleem zit vooral voorin: 101,7 punten per wedstrijd is het laagste van de competitie. Opvallend is Mikal Bridges. Hij stond alle drie de keren in de basis, maar maakte in totaal 10 punten: 5 uit 23 uit het veld en 0 uit 10 achter de driepuntslijn. Hij staat niet op de blessurelijst; het is een kwestie van vorm.</p>
<p><strong>Detroit Pistons: de enige ongeslagen ploeg in het Oosten</strong></p>
<p>Detroit opende thuis met 121-113 tegen Boston, na een achterstand van 13 punten bij rust. Cade Cunningham maakte 22 punten en 8 assists, Duren 22 punten en 9 rebounds, Duncan Robinson 21 punten. In Miami won de ploeg van coach J.B. Bickerstaff met 128-111. Zondag volgde een 93-106 zege in Philadelphia, zonder Duren en zonder Ausar Thompson. Cunningham had 26 punten, 8 rebounds en 8 assists, Robinson 21 en Daniss Jenkins 18. Detroit scoort 118,3 punten per duel en krijgt er 105,7 tegen.</p>
<h3><strong>Vorig seizoen en de onderlinge duels</strong></h3>
<p>De Knicks werden in 2025/26 kampioen. Na de derde plaats in het Oosten versloegen ze Atlanta (4-2), Philadelphia (4-0), Cleveland (4-0) en in de finale San Antonio (4-1). Detroit won de reguliere competitie in het Oosten met 60 zeges, maar had het in de play-offs moeilijk: tegen Orlando kwam het terug van 1-3, daarna ging het in de tweede ronde met 3-4 onderuit tegen Cleveland, na een 2-0-voorsprong.</p>
{tabel(["2025/26", "New York Knicks", "Detroit Pistons"], [
    ("Eindstand", "53-29 (nr. 3 Oost)", "60-22 (nr. 1 Oost)"),
    ("Thuis / uit*", "30-10 / 22-19", "31-9 / 28-13"),
    ("Punten voor / tegen", "116,5 / 110,1", "117,8 / 109,6"),
    ("Na het seizoen", "Kampioen (4-1 tegen San Antonio)", "Tweede ronde (3-4 tegen Cleveland)"),
])}
<p><em>* Beide ploegen wonnen daarnaast één wedstrijd op neutraal terrein.</em></p>
<p>In de onderlinge duels was Detroit vorig seizoen veel sterker. In Detroit werd het 121-90 en 118-80, in New York 126-111. In dat laatste duel misten de Pistons Duren en Isaiah Stewart door een schorsing en maakte Cunningham 42 punten en 13 assists. Ook in het tweede duel ontbrak Duren, net als Anunoby bij New York.</p>"""

content2 = f"""<h3><strong>Zo zijn beide selecties veranderd</strong></h3>
<p><strong>New York Knicks: de kern blijft</strong></p>
<p>De basisvijf van de titel is intact: Brunson, Bridges, Josh Hart, Anunoby en Towns. Center Mitchell Robinson speelt nu bij Boston. Andre Drummond kwam over van Philadelphia en is de eerste invaller onder de ring. Verder zijn Dalton Knecht en James Wiseman nieuw.</p>
<p><strong>Detroit Pistons: meer schutters rond Cunningham</strong></p>
<p>Tobias Harris (nu San Antonio) en Stewart (nu Memphis) zijn weg; Jaden Ivey vertrok vorig seizoen al naar Chicago. Daarvoor kwamen John Collins, die vorig seizoen bij de Clippers 13,6 punten maakte, Isaiah Joe uit Oklahoma City en Taurean Prince. Kevin Huerter kwam tijdens vorig seizoen over. Met Robinson, Collins, Joe en Javonte Green heeft Bickerstaff meer schotkracht van afstand dan een jaar geleden.</p>
<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("Jose Alvarado", "New York", "Speelt niet (verstuikte linkerenkel)"),
    ("Jalen Duren", "Detroit", "Speelt niet (verrekte rechterhamstring)"),
    ("Ausar Thompson", "Detroit", "Twijfelachtig (verstuikte rechterenkel)"),
    ("Isaiah Joe", "Detroit", "Twijfelachtig (kneuzing rechterheup)"),
])}
<p><em>Stand van de officiële NBA-blessurelijst op dinsdag 27 oktober, 10:45 Nederlandse tijd. Spelers die bij de G League-ploegen zitten, staan niet in de tabel.</em></p>
<p><strong>Verwachte basisvijf Knicks:</strong> Jalen Brunson, Mikal Bridges, Josh Hart, OG Anunoby, Karl-Anthony Towns. Dezelfde vijf als in alle drie de wedstrijden. Drummond, McBride en Shamet zijn de belangrijkste wissels.</p>
<p><strong>Verwachte basisvijf Pistons:</strong> Cade Cunningham, Daniss Jenkins, Duncan Robinson, John Collins, Paul Reed. Dat was de vijf in Philadelphia. Kan Thompson spelen, dan begint hij waarschijnlijk in plaats van Jenkins. Huerter, Green en Ronald Holland II zijn de belangrijkste wissels.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "2026/27 tot nu toe"], [
    ("Jalen Brunson (NY)", "26,0", "3,3", "6,8", "22,7 ptn, 39,1% uit het veld"),
    ("Karl-Anthony Towns (NY)", "20,1", "11,9", "3,0", "21,0 ptn, 12,0 reb"),
    ("Mikal Bridges (NY)", "14,4", "3,8", "3,7", "3,3 ptn, 5 uit 23"),
    ("Cade Cunningham (DET)", "23,9", "5,5", "9,9", "21,3 ptn, 8,0 ast"),
    ("Duncan Robinson (DET)", "12,2", "2,7", "2,1", "19,7 ptn, 15 uit 28 voor drie"),
    ("John Collins (DET)", "13,6*", "5,3*", "1,0*", "15,0 ptn, 7,7 reb"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26. * Collins: cijfers bij de LA Clippers.</em></p>
<p><strong>Cade Cunningham</strong> was vorig seizoen de grote man in de onderlinge duels, met 29 punten en 13 assists in Detroit en 42 punten in New York. <strong>Jalen Brunson</strong> scoort wel, maar heeft er veel schoten voor nodig. <strong>Karl-Anthony Towns</strong> is de Knick in vorm en krijgt zonder Duren vooral Reed en Collins tegenover zich, die minder lang en zwaar zijn. <strong>Mikal Bridges</strong> maakte vorig seizoen 14,4 punten per duel en moet zijn dip doorbreken.</p>
<h3><strong>Odds Knicks – Pistons bij TOTO</strong></h3>
<p>TOTO ziet de Knicks als favoriet: een quotering van 1,59 staat voor ongeveer 63 procent winkans. De handicap ligt rond de 3,5 punten in het voordeel van New York, het verwachte puntentotaal rond de 218 punten.</p>
{tabel(["Markt (TOTO)", "Knicks", "Pistons"], [
    ("Winnaar (incl. verlenging)", "1,59", "2,45"),
    ("1X2 (reguliere speeltijd, gelijk 18,00)", "1,59", "2,50"),
    ("Handicap -2,5 / +2,5 (incl. verlenging)", "1,67", "2,00"),
    ("Handicap -3,5 / +3,5 (incl. verlenging)", "1,87", "1,95"),
    ("Handicap -4,5 / +4,5 (incl. verlenging)", "1,91", "1,78"),
])}
<p>Op het totaal biedt TOTO 217,5 punten (Over 1,73 / Under 1,98), 218,5 (1,87 / 1,95) en 219,5 (Over 1,87 / Under 1,78). Odds gelezen op dinsdag rond 10:45 uur; vergelijk ze vlak voor de start nog even.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op Knicks – Pistons</strong></a></p>"""

content3 = f"""<h3><strong>Onze Knicks – Pistons voorspelling: Detroit houdt de reeks vast</strong></h3>
<p>New York is beter dan 0-3. De Knicks verloren drie keer nipt, Towns en Anunoby spelen goed, en een schutter als Bridges blijft niet eeuwig op 0 uit 10 voor drie staan. Daar staat tegenover dat het aanvallende probleem breder is dan één speler. Brunson schiet onder de 40 procent en de ploeg scoort minder dan wie ook.</p>
<p>Detroit speelt juist met veel zelfvertrouwen. Het won twee keer uit, waarvan één keer zonder Duren en Thompson, en Cunningham stuurt het spel met 8 assists per wedstrijd. Vorig seizoen won Detroit alle drie de onderlinge duels met minstens 15 punten verschil. Zonder Duren verliest Detroit wel lengte onder de ring, en daar kan Towns van profiteren. Onze voorspelling: <strong>New York Knicks – Detroit Pistons 107-110</strong>.</p>
<h3><strong>Onze wedtip: Pistons +3,5 (1,95)</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Onze kans"], [
    ("Detroit Pistons +3,5 punten (incl. verlenging)", "1,95", "TOTO", "Ongeveer 57 procent"),
])}
<p><strong>Waarom deze tip?</strong> De tip is goed als Detroit wint, of verliest met maximaal drie punten verschil. Een odd van 1,95 staat voor een kans van 51 procent; zonder de marge van de bookmaker is dat ongeveer 49 procent. Wij schatten de kans op ongeveer 57 procent. De onderbouwing:</p>
<p><strong>1. Het verschil in vorm is groot.</strong> Detroit scoort 118,3 punten per wedstrijd en krijgt er 105,7 tegen. New York maakt 101,7 punten, het laagste van de competitie, en schiet 32 procent voor drie.</p>
<p><strong>2. Detroit kan zonder Duren.</strong> Zondag won de ploeg in Philadelphia met 13 punten verschil zonder Duren en Thompson. Vorig seizoen versloeg Detroit New York twee keer zonder Duren, waarvan één keer in Madison Square Garden (126-111).</p>
<p><strong>3. De markt rekent op de naam van de kampioen.</strong> Een handicap van 3,5 punten voor een ploeg die nog niet won en vorig seizoen alle drie de onderlinge duels ruim verloor, vinden wij te ruim voor New York. Met +3,5 ben je ook beschermd bij een krappe thuiszege, en dat is reëel: de Knicks speelden drie keer een wedstrijd die tot het eind spannend bleef.</p>
<p><strong>Waarom niet een andere markt?</strong> Een zege van de Knicks (1,59) vraagt om 63 procent kans; wij komen uit op ongeveer 56 procent, dus die odd is te laag. Detroit als winnaar (2,45) betaalt meer en wij geven de Pistons ongeveer 44 procent kans, maar dan heb je geen marge voor een nipte thuiszege. Pistons +4,5 (1,78) vraagt om 56 procent kans voor één punt extra; dat is het niet waard. Het puntentotaal laten we liggen: onze voorspelling komt uit op 217 punten, precies rond de lijn van 217,5 en 218,5.</p>
<p><strong>Het risico.</strong> Vindt New York thuis zijn schot terug, dan is dit een ploeg die vorig seizoen kampioen werd en in de play-offs Philadelphia en Cleveland met 4-0 versloeg. Een avond met tien driepunters van Bridges en McBride samen, en de Knicks winnen ruim. Let ook op: de handicap telt een eventuele verlenging mee. Meer uitleg vind je in onze gidsen over <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap wedden</a> en de <a href="/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners">money line</a>.</p>
<h3><strong>Knicks – Pistons live kijken in Nederland</strong></h3>
<p>Bij <a href="/bookmakers/bet365">Bet365</a> kun je NBA-wedstrijden live volgen via de livestream. Je hebt daarvoor een account met een storting nodig. ESPN zendt in Nederland een deel van de NBA-wedstrijden uit; in de programmagids zie je of deze erbij zit. Met <strong>NBA League Pass</strong>, de betaalde dienst van de competitie, kun je alle wedstrijden volgen. Meer opties vind je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk Knicks – Pistons live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Vannacht spelen ook <a href="/nieuws/celtics-nets-voorspelling-wedtips-nba-2026">Celtics – Nets</a>, <a href="/nieuws/spurs-kings-voorspelling-wedtips-nba-2026">Spurs – Kings</a> en <a href="/nieuws/lakers-trail-blazers-voorspelling-wedtips-nba-2026">Lakers – Trail Blazers</a>; ook daarvoor staat onze voorspelling klaar. Eerder schreven we over Detroit in <a href="/nieuws/76ers-pistons-voorspelling-wedtips-nba-2026">76ers – Pistons</a> en <a href="/nieuws/pistons-celtics-voorspelling-wedtips-nba-opening-2026">Pistons – Celtics</a>. Benieuwd <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">welke Nederlanders in de NBA spelen</a>? Nieuw met basketbal? Lees <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels in de NBA</a>. Alle tips staan op <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Knicks – Pistons?</strong><br>In de nacht van dinsdag op woensdag 28 oktober 2026 om 01:00 Nederlandse tijd. In New York is het dan dinsdagavond 20:00.</p>
<p><strong>Speelt Jalen Duren mee?</strong><br>Nee. Duren staat met een verrekte rechterhamstring als 'out' op de officiële NBA-blessurelijst. Ausar Thompson (enkel) en Isaiah Joe (heup) zijn twijfelachtig. Bij de Knicks ontbreekt alleen Jose Alvarado.</p>
<p><strong>Wie is favoriet: Knicks of Pistons?</strong><br>De Knicks, met een quotering van 1,59 bij TOTO. Detroit staat op 2,45.</p>
<p><strong>Wat is onze voorspelling voor Knicks – Pistons?</strong><br>Detroit wint met 107-110. Onze wedtip is Detroit Pistons +3,5 punten, inclusief verlenging (1,95 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

KAART = {"home": "Knicks", "away": "Pistons", "home_abbr": "ny", "away_abbr": "det", "home_pos": "53-29 · nr. 3 Oost 2025/26", "away_pos": "60-22 · nr. 1 Oost 2025/26", "hs": 107, "as": 110, "datum": "Wo 28 okt", "tijd": "01:00", "odd_home": "1,59", "odd_away": "2,45"}
WEDTIPS = {"wedtip-1-2": "Detroit Pistons +3,5 punten (incl. verlenging)", "quotering-wedtip-1": "1.95",
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
                  "/nieuws/pistons-celtics-voorspelling-wedtips-nba-opening-2026",
                  "/nieuws/spurs-thunder-voorspelling-wedtips-nba-opening-2026",
                  "/nieuws/76ers-pistons-voorspelling-wedtips-nba-2026", "/nieuws/jazz-lakers-voorspelling-wedtips-nba-2026",
                  "/nieuws/lakers-warriors-voorspelling-wedtips-nba-2026",
                  "/nieuws/cavaliers-timberwolves-voorspelling-wedtips-nba-2026",
                  "/nieuws/nuggets-warriors-voorspelling-wedtips-nba-2026",
                  "/nieuws/celtics-nets-voorspelling-wedtips-nba-2026", "/nieuws/spurs-kings-voorspelling-wedtips-nba-2026",
                  "/nieuws/lakers-trail-blazers-voorspelling-wedtips-nba-2026",
                  "/nieuws/welke-nederlanders-spelen-in-de-nba",
                  "/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders",
                  "/nieuws/wat-is-handicap-wedden-de-complete-gids",
                  "/nieuws/wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners",
                  "/wedden-op-nba-voorspellingen-en-wedtips---basketbal", "/bookmakers/toto", "/bookmakers/bet365",
                  "/live-kijken", BET365}
    assert set(hrefs) <= toegestaan, set(hrefs) - toegestaan
    assert "nba-voorspellingen-vannacht-28-oktober-2026" not in html, "vannacht geen algemeen artikel"
    for s in ("celtics-nets", "spurs-kings", "lakers-trail-blazers"):
        assert f"/nieuws/{s}-voorspelling-wedtips-nba-2026" in html, s
    assert "<table" not in html.replace(f"<table {T}>", ""), "tabellen alleen via tabel()"
    verboden = ["BetCity", "ESPN-API", "ESPN.com", "Associated Press", "DraftKings", "Rotowire", "Betfans", "Sportradar"]
    assert not any(v.lower() in html.lower() for v in verboden), "geen bronnen/concurrenten"
    # SEO
    fk = "Knicks – Pistons voorspelling"
    assert fk in TITEL and fk in SAMENVATTING and len(SAMENVATTING) <= 160
    assert fk in re.sub(r"<[^>]+>", "", content).split(":")[0], "focuskeyword in eerste zin intro"
    assert any(fk in h for h in re.findall(r"<h3><strong>(.*?)</strong></h3>", html)), "focuskeyword in een h3"
    assert "28 oktober" in TITEL and "01:00" in TITEL
    # Wedtip en consistentie
    assert set(WEDTIPS) == {"wedtip-1-2", "quotering-wedtip-1", "bookmaker-wedtips"}
    assert WEDTIPS["bookmaker-wedtips"] == "669ab9f5aceb8b717cea24c3"
    q = float(WEDTIPS["quotering-wedtip-1"])
    toto_odds = {1.59, 2.45, 2.50, 18.0, 1.91, 1.78, 1.87, 1.95, 1.67, 2.00, 1.73, 1.98}
    assert q in toto_odds and q == 1.95
    assert KAART["as"] + 3.5 > KAART["hs"], "voorspelde score moet Pistons +3,5 laten winnen"
    assert KAART["as"] > KAART["hs"], "voorspelling: Pistons winnen"
    assert f"{KAART['hs']}-{KAART['as']}" in content and f"{KAART['hs']}-{KAART['as']}" in content3
    assert KAART["odd_home"] == "1,59" and KAART["odd_away"] == "2,45" and KAART["tijd"] == "01:00"
    assert KAART["home_abbr"] == "ny" and KAART["away_abbr"] == "det"
    assert "1,95" in content and "1,95" in content3 and "Pistons +3,5" in content3
    assert "rond 10:45 uur" in content2
    assert len(re.findall(r"<p><strong>[123]\. ", content3)) == 3 and "Waarom niet een andere markt?" in content3
    assert len(re.findall(r"<p><strong>[^<]*\?</strong><br>", content3)) == 4, "4 FAQ-vragen"
    assert SLUG == "knicks-pistons-voorspelling-wedtips-nba-2026" and DATUM == "2026-10-28T00:00:00.000Z"
    tekst = re.sub(r"<[^>]+>", " ", html)
    print(len(TITEL), "tekens titel |", len(SAMENVATTING), "tekens samenvatting |", len(tekst.split()), "woorden")
    print("Alle asserts geslaagd (dry run, niets gepubliceerd).")
