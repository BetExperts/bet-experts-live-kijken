# -*- coding: utf-8 -*-
"""Los artikel: Mavericks – Spurs voorspelling, NBA 25 oktober 2026 (02:00 NL, nog zomertijd), American Airlines Center.
Feiten nagelopen op 24-10-2026 (ESPN-API: summary 401909858, scoreboards 20-24 okt, boxscores 401909844 en 401909096,
onderlinge duels 2025/26 (401809235, 401810593, 401810604, 401811035), standen 2025/26, selecties, spelersgemiddelden,
back-to-backs Spurs 2025/26; officiële NBA-blessurelijst 23-10 23:45 ET en 24-10 06:45 ET (SAS@DAL nog niet ingediend);
nieuws over Flaggs schouder en Irvings minutenlimiet).
- Pacers – Mavericks 105-121 en Spurs – Rockets 110-114 (Austin) op 23-10 (US-tijd): voor beide een back-to-back.
- Onderling 2025/26: 92-125 en 123-135 in Dallas, 138-125 en 139-120 in San Antonio (4-0 SAS, steeds 12+ punten verschil).
- Odds: TOTO uit specials/nba_feiten_2026_10_25.md (±12:50 NL op 24-10). 'Winnaar' = incl. verlenging. Eén wedtip.
  ../superodd-agent/.venv/bin/python specials/mavericks_spurs_nba_2026.py   (alleen dry run, publiceert niets)"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

TITEL = "Mavericks – Spurs voorspelling: wedtip en odds voor de thuisopener van Dallas (25 oktober, 02:00)"
SLUG = "mavericks-spurs-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("Dallas speelt zijn thuisopener tegen Wembanyama en de Spurs, waarschijnlijk zonder Cooper Flagg. "
                "Voorspelling, onze wedtip, TOTO-odds en blessures.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet-experts.nl/go/bet365"
DATUM = "2026-10-25T00:00:00.000Z"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>In de nacht van zaterdag op zondag om 02:00 Nederlandse tijd speelt Dallas zijn eerste thuiswedstrijd van het seizoen, tegen San Antonio. Voor beide ploegen is het de tweede wedstrijd in twee dagen. Dallas moet het waarschijnlijk zonder Cooper Flagg doen, die vrijdag in Indianapolis hard op zijn linkerschouder viel. Onze voorspelling: Mavericks – Spurs 104-120. Onze wedtip: San Antonio wint met minstens twaalf punten verschil (Spurs -11,5, odd 1,78 bij TOTO).</strong></p>
<p>De Spurs staan nog op nul zeges, toch zijn ze met een quotering van 1,18 een van de grootste favorieten van de nacht. Hieronder lees je waarom.</p>
<h3><strong>Mavericks – Spurs: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "Dallas Mavericks – San Antonio Spurs"),
    ("Datum", "Zondag 25 oktober 2026 (nacht van zaterdag op zondag)"),
    ("Aanvang", "02:00 Nederlandse tijd, nog zomertijd (zaterdag 19:00 in Dallas)"),
    ("Arena", "American Airlines Center, Dallas"),
    ("Competitie", "NBA, reguliere competitie 2026/27"),
    ("Stand 2026/27", "Mavericks 1-1, Spurs 0-2"),
    ("Onderlinge duels 2025/26", "4-0 voor de Spurs"),
    ("Bijzonder", "Thuisopener van Dallas; voor beide ploegen het tweede duel van een back-to-back"),
])}
<h3><strong>Het seizoen tot nu toe: Dallas herstelt zich, de Spurs wachten nog op een zege</strong></h3>
<p>Dallas verloor woensdag met 128-110 in Houston, maar won vrijdag met 121-105 in Indianapolis, de eerste zege onder de nieuwe coach Dusty May. Bij rust stond het al 77-43. Kyrie Irving maakte 24 punten in nog geen 25 minuten, P.J. Washington had 20 punten en 13 rebounds. Flagg stond op 14 punten en 6 assists toen Aaron Nesmith hem vlak voor rust bij een breakaway van achteren neerhaalde (flagrant foul). Na rust kwam Flagg niet meer terug.</p>
<p>San Antonio verloor de opener van Oklahoma City (104-116) en vrijdag in Austin met 110-114 van Houston, nadat Amen Thompson in de slotseconde de gelijkmakende layup van Victor Wembanyama blokte. Wembanyama had 25 punten en 13 rebounds, Dylan Harper 20 punten en De'Aaron Fox 19 punten en 9 assists. Het probleem zit in het schot van afstand: in twee wedstrijden ging maar 22 van de 74 driepunters erin (29,7 procent).</p>
<h3><strong>Twee ploegen op een back-to-back</strong></h3>
<p>Dallas moest ruim 1.200 kilometer terugvliegen uit Indianapolis, maar door de grote voorsprong speelden de basisspelers weinig. San Antonio reisde maar zo'n 300 kilometer vanuit Austin, maar had een zware avond: Harper en Devin Vassell speelden 36 minuten, Fox 34, Stephon Castle 33 en Wembanyama 32. Vorig seizoen had San Antonio daar weinig last van: de Spurs wonnen 12 van hun 15 tweede duels van een back-to-back, waaronder een 123-135 zege in Dallas op 5 februari.</p>
<h3><strong>Vorig seizoen: 4-0 voor San Antonio</strong></h3>
<p>San Antonio werd in 2025/26 tweede in het Westen en verloor pas in de NBA Finals van New York. Dallas speelde het hele seizoen zonder Irving, deed in februari Anthony Davis van de hand en werd twaalfde.</p>
{tabel(["2025/26", "Dallas Mavericks", "San Antonio Spurs"], [
    ("Eindstand", "26-56 (nr. 12 West)", "62-20 (nr. 2 West)"),
    ("Punten voor / tegen", "114,1 / 119,6", "119,8 / 111,5"),
    ("Thuis", "16-25", "32-8"),
    ("Onderling", "0-4", "4-0"),
    ("Play-offs", "Niet gehaald", "Finale verloren van New York (1-4)"),
])}
<p>De onderlinge duels eindigden in Dallas op 92-125 (oktober) en 123-135 (februari), en in San Antonio op 138-125 (februari) en 139-120 (april). San Antonio won ze allemaal met minstens twaalf punten verschil, terwijl Flagg alle vier de keren meespeelde. Wembanyama kwam tegen Dallas gemiddeld tot 31,3 punten en 12,5 rebounds.</p>"""

content2 = f"""<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("Cooper Flagg", "Dallas", "Waarschijnlijk afwezig (pijnlijke linkerschouder)"),
    ("Dereck Lively II", "Dallas", "Speelt niet (voetoperatie)"),
    ("Santi Aldama", "Dallas", "Speelt niet (knieoperatie)"),
    ("Caleb Martin", "Dallas", "Speelde vrijdag niet (verstuikte duim)"),
    ("Jett Howard", "Dallas", "Speelde vrijdag niet (kuit)"),
    ("Tarik Biberović", "Dallas", "Speelde vrijdag niet (hiel)"),
    ("Tobias Harris", "San Antonio", "Speelt niet (kuit)"),
    ("Jayden Quaintance", "San Antonio", "Speelt niet (herstel na knieoperatie)"),
])}
<p><em>Stand op zaterdag 24 oktober, 12:50 Nederlandse tijd. De officiële blessurelijst voor deze wedstrijd was toen nog niet ingediend. Coach May zei vrijdag dat Flagg 'de komende dagen' wordt onderzocht.</em></p>
<p>Irving staat niet op de lijst, maar speelt na zijn kruisbandblessure met een minutenlimiet (rond de 25 minuten). Dit is zijn eerste back-to-back sinds zijn rentree.</p>
<p><strong>Verwachte basisvijf Mavericks:</strong> Kyrie Irving, Max Christie, Naji Marshall, P.J. Washington, Daniel Gafford. Marshall begon vrijdag na rust in plaats van Flagg; Zaccharie Risacher is de andere kandidaat. Zonder Lively en Aldama zijn Morez Johnson jr. en Moussa Cissé de enige lange invallers.</p>
<p><strong>Verwachte basisvijf Spurs:</strong> De'Aaron Fox, Stephon Castle, Dylan Harper, Devin Vassell, Victor Wembanyama, dezelfde vijf als vrijdag.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Ptn", "Reb", "Ast", "2026/27 tot nu toe"], [
    ("Victor Wembanyama (SAS)", "25,0", "11,5", "3,1", "18,5 ptn, 13,0 reb, 4,0 blocks"),
    ("De'Aaron Fox (SAS)", "18,6", "3,8", "6,2", "16,5 ptn, 8,0 ast"),
    ("Stephon Castle (SAS)", "16,7", "5,3", "7,4", "19,5 ptn, 7,0 reb"),
    ("Dylan Harper (SAS)", "11,8", "3,4", "3,9", "19,0 ptn als basisspeler"),
    ("Kyrie Irving (DAL)", "24,7*", "4,8*", "4,6*", "19,5 ptn in 24,5 minuten"),
    ("P.J. Washington (DAL)", "14,2", "7,0", "1,8", "15,0 ptn, 8,5 reb"),
    ("Cooper Flagg (DAL)", "21,0", "6,7", "4,5", "23,0 ptn; waarschijnlijk afwezig"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26. * Irving speelde in 2025/26 niet; bij hem staan de cijfers van 2024/25.</em></p>
<p><strong>Victor Wembanyama</strong> schiet nog niet goed (1 van de 13 in de opener, 9 van de 21 vrijdag), maar pakt wel 13 rebounds per wedstrijd. Tegen Dallas had hij vorig seizoen twee keer 40 punten, en zonder Lively en Aldama heeft de thuisploeg weinig lengte om hem af te stoppen.</p>
<p><strong>Cooper Flagg</strong>, de Rookie of the Year van vorig seizoen, begon sterk met 32 punten in Houston. Valt hij af, dan moet de aanval vooral van Irving komen, en die is aan een minutenlimiet gebonden.</p>
<h3><strong>Odds Mavericks – Spurs bij TOTO: waarom San Antonio op 1,18 staat</strong></h3>
<p>Een quotering van 1,18 staat voor een kans van zo'n 85 procent. Voor een uitploeg zonder zege lijkt dat veel. De verklaring: Dallas mist waarschijnlijk zijn beste speler en twee lange spelers, Irving is beperkt inzetbaar, en het niveauverschil was vorig seizoen enorm (62 tegen 26 zeges, en 4-0 onderling). Bij <a href="/bookmakers/toto">TOTO</a> ligt de handicap op 12,5 punten in het voordeel van de Spurs en het verwachte puntentotaal rond de 231 punten.</p>
{tabel(["Markt (TOTO)", "Mavericks", "Spurs"], [
    ("Winnaar (incl. verlenging)", "5,15", "1,18"),
    ("1X2 (reguliere speeltijd, gelijk 23,00)", "5,75", "1,14"),
    ("Handicap +11,5 / -11,5 (incl. verlenging)", "2,05", "1,78"),
    ("Handicap +12,5 / -12,5 (incl. verlenging)", "1,93", "1,87"),
    ("Handicap +13,5 / -13,5 (incl. verlenging)", "1,80", "2,00"),
])}
<p>Totaal 230,5 punten (incl. verlenging): Over 1,80, Under 1,87. Bij 231,5 punten: Over 1,95, Under 1,87. Gelezen op zaterdag 24 oktober rond 12:50 uur. Odds kunnen nog veranderen zodra duidelijk is of Flagg en Irving spelen.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op Mavericks – Spurs</strong></a></p>"""

content3 = f"""<h3><strong>Onze voorspelling: de Spurs winnen ruim</strong></h3>
<p>We verwachten dat San Antonio zijn eerste zege pakt, en niet met een klein verschil. De Spurs verloren van twee topploegen uit het Westen, de laatste pas in de slotseconde. Dallas is zonder Flagg, Lively en Aldama een veel zwakkere tegenstander, met weinig antwoord op Wembanyama en naast Irving weinig creativiteit.</p>
<p>De thuisopener geeft Dallas energie en vrijdag vielen de driepunters goed (14 van de 34). Maar een team met Wembanyama, Fox, Castle en Harper blijft niet op 30 procent uit de driepunters hangen. Onze voorspelling: <strong>Dallas Mavericks – San Antonio Spurs 104-120</strong>.</p>
<h3><strong>Onze wedtip: Spurs -11,5 (1,78)</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Onze kans"], [
    ("San Antonio Spurs -11,5 punten (incl. verlenging)", "1,78", "TOTO", "Ongeveer 61 procent"),
])}
<p><strong>Waarom deze tip?</strong> San Antonio moet met minstens twaalf punten verschil winnen. Een odd van 1,78 staat voor een kans van 56 procent; wij schatten die kans op ongeveer 61 procent. Dat verschil maakt deze markt de beste keuze van de wedstrijd. De onderbouwing:</p>
<p><strong>1. Het onderlinge beeld.</strong> San Antonio won alle vier de duels van vorig seizoen met minstens twaalf punten verschil (33, 12, 13 en 19). Dallas had toen Flagg wel tot zijn beschikking.</p>
<p><strong>2. De afwezigen.</strong> Zonder Flagg mist Dallas zijn beste speler, zonder Lively en Aldama ook lengte tegen de langste speler van de competitie. Irving speelt maar ongeveer de helft van de wedstrijd.</p>
<p><strong>3. Back-to-backs zijn geen probleem voor de Spurs.</strong> Vorig seizoen won San Antonio 12 van de 15 tweede wedstrijden van een back-to-back, inclusief een zege in Dallas.</p>
<p><strong>Waarom niet een andere markt?</strong> Een zege van de Spurs (1,18) schatten we net zo hoog in als de bookmaker en de odd is te laag; een stunt van Dallas (5,15) schatten we lager in. Bij -12,5 en -13,5 groeit het risico sneller dan de odds. Het puntentotaal laten we liggen: zonder Flagg scoort Dallas minder, maar de vier duels van vorig seizoen leverden gemiddeld 249 punten op.</p>
<p><strong>Het risico.</strong> Een ruime voorsprong kan in het slotkwart nog slinken als de invallers erin komen. Speelt Flagg toch, of laat San Antonio Wembanyama op de tweede avond rusten, dan ziet deze wedstrijd er heel anders uit. Controleer de opstellingen dus vlak voor het begin. Let ook op: de handicap telt een eventuele verlenging mee. Meer uitleg vind je in onze gids over <a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">handicap wedden</a>.</p>
<h3><strong>Mavericks – Spurs live kijken in Nederland</strong></h3>
<p>Bij <a href="/bookmakers/bet365">Bet365</a> kun je NBA-wedstrijden live volgen via de livestream; je hebt daarvoor een account met een storting nodig. ESPN zendt in Nederland een deel van de NBA-wedstrijden uit; of deze erbij zit, zie je in de programmagids. Met <strong>NBA League Pass</strong>, de betaalde dienst van de competitie, kun je alle wedstrijden volgen. Meer opties vind je op onze pagina <a href="/live-kijken">live kijken</a>.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk Mavericks – Spurs live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Lees ook onze voorbeschouwingen van <a href="/nieuws/spurs-rockets-voorspelling-wedtips-nba-2026">Spurs – Rockets</a> en <a href="/nieuws/pacers-mavericks-voorspelling-wedtips-nba-2026">Pacers – Mavericks</a>, de <a href="/nieuws/nba-voorspellingen-vannacht-24-oktober-2026">NBA-voorspellingen van 24 oktober</a> en <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">welke Nederlanders er in de NBA spelen</a>. Nieuw met basketbal? Lees <a href="/nieuws/belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders">de belangrijkste regels in de NBA</a>. Alle tips staan op <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Mavericks – Spurs?</strong><br>Zondag 25 oktober 2026 om 02:00 Nederlandse tijd, in de nacht van zaterdag op zondag. In Dallas is het dan zaterdagavond 19:00. Let op: tijdens de wedstrijd gaat in Nederland de klok een uur terug naar wintertijd.</p>
<p><strong>Speelt Cooper Flagg mee?</strong><br>Waarschijnlijk niet. Flagg viel vrijdag in Indianapolis op zijn linkerschouder en speelde na rust niet meer. Een officiële beslissing volgt pas op de blessurelijst van zaterdag.</p>
<p><strong>Waarom zijn de Spurs zo'n grote favoriet?</strong><br>Dallas mist waarschijnlijk Flagg, Lively en Aldama, en San Antonio won vorig seizoen alle vier de onderlinge duels ruim. TOTO geeft 1,18 op de Spurs en 5,15 op Dallas.</p>
<p><strong>Wat is onze voorspelling voor Mavericks – Spurs?</strong><br>De Spurs winnen met 104-120. Onze wedtip is San Antonio -11,5 punten (1,78 bij TOTO).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

KAART = {"home": "Mavericks", "away": "Spurs", "home_abbr": "dal", "away_abbr": "sa", "home_pos": "26-56 · nr. 12 West 2025/26", "away_pos": "62-20 · nr. 2 West 2025/26", "hs": 104, "as": 120, "datum": "Zo 25 okt", "tijd": "02:00", "odd_home": "5,15", "odd_away": "1,18"}
WEDTIPS = {"wedtip-1-2": "San Antonio Spurs -11,5 punten (incl. verlenging)", "quotering-wedtip-1": "1.78",
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
