# -*- coding: utf-8 -*-
"""Los artikel: Lakers – Warriors voorspelling, NBA 22 oktober 2026 (04:00 NL). Feiten nagelopen op 21-10-2026
(NBA.com, ESPN, Basketnews, Newsweek, StatMuse, Wikipedia, iHeart/VegasInsider); Nederlandse odds uit onze feed.
  python3 specials/lakers_warriors_nba_2026.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Lakers – Warriors voorspelling: wedtips en odds voor de NBA-klassieker (22 oktober, 04:00)"
SLUG = "lakers-warriors-voorspelling-wedtips-nba-2026"
SAMENVATTING = ("Lakers – Warriors opent voor beide ploegen het NBA-seizoen. Voorspelling, wedtips, odds, blessures en "
                "opstellingen, zonder LeBron James.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BET365 = "https://www.bet365.nl/hub/nl-nl/open-account?affiliate=365_02599619"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>In de nacht van woensdag op donderdag om 04:00 Nederlandse tijd beginnen de Los Angeles Lakers en de Golden State Warriors hun NBA-seizoen tegen elkaar. Voor het eerst sinds 2018 staan de Lakers aan de start zonder LeBron James. Onze voorspelling: de Lakers winnen met 117-110. Hoofdtip: minder dan 239 punten, met de Warriors +12 als tweede tip.</strong></p>
<p>Het is een van de beroemdste rivaliteiten van de moderne NBA, maar dit seizoen ziet de affiche er anders uit. LeBron James vertrok deze zomer naar Philadelphia, waardoor de Lakers nu volledig om Luka Dončić en Austin Reaves draaien. Bij Golden State begint de 38-jarige Stephen Curry aan zijn zoveelste seizoen, maar met een lange lijst afwezigen. Hieronder lees je wat er veranderd is, wie er speelt, wat de bookmakers verwachten en welke weddenschappen wij interessant vinden.</p>
<h3><strong>Lakers – Warriors: aanvang en wedstrijdinfo</strong></h3>
{tabel(None, [
    ("Wedstrijd", "Los Angeles Lakers – Golden State Warriors"),
    ("Datum", "Donderdag 22 oktober 2026 (nacht van woensdag op donderdag)"),
    ("Aanvang", "04:00 Nederlandse tijd (19:00 in Los Angeles)"),
    ("Arena", "Crypto.com Arena, Los Angeles"),
    ("Competitie", "NBA, reguliere competitie 2026/27 (eerste wedstrijd voor beide ploegen)"),
    ("Onderlinge duels 2025/26", "3-1 voor de Lakers"),
])}
<p>De Lakers zijn de thuisploeg. Dit seizoen ontmoeten beide teams elkaar nog drie keer: op 30 oktober in San Francisco (NBA Cup), op 21 januari in San Francisco en op 14 maart in Los Angeles.</p>
<h3><strong>Vorig seizoen: Lakers sterk, Warriors in de play-in</strong></h3>
<p>De Lakers wonnen in 2025/26 53 van de 82 wedstrijden en werden vierde in het Westen. Dončić scoorde gemiddeld 33,5 punten, maar miste vanaf begin april met een hamstringblessure de hele play-offs. Zonder hem won Los Angeles toch van Houston (4-2), waarna Oklahoma City in de tweede ronde met 4-0 te sterk was.</p>
<p>Golden State kwam niet verder dan 37-45 en een tiende plaats. In de play-in won de ploeg nog bij de Clippers, maar verloor daarna in Phoenix, waardoor het seizoen voor de play-offs eindigde. Jimmy Butler scheurde in januari zijn kruisband en Curry miste door een knieblessure een groot deel van het seizoen.</p>
{tabel(["2025/26", "Los Angeles Lakers", "Golden State Warriors"], [
    ("Eindstand", "53-29 (nr. 4 West)", "37-45 (nr. 10 West)"),
    ("Thuis / uit", "28-13 / 25-16", "22-19 / 15-26"),
    ("Punten voor / tegen", "116,3 / 114,6", "114,6 / 115,2"),
    ("Aanvallende / verdedigende rating", "118,2 / 116,4", "115,0 / 115,6"),
    ("Tegen de handicap (ATS)", "45-37", "35-47"),
    ("Play-offs", "Tweede ronde (0-4 tegen OKC)", "Uitgeschakeld in de play-in"),
])}
<p><em>Ratings per 100 balbezittingen (StatMuse). De ATS-cijfers verschillen per bron één tot twee wedstrijden.</em></p>"""

content2 = f"""<h3><strong>Zo zijn beide selecties veranderd</strong></h3>
<p><strong>Los Angeles Lakers: alles om Dončić</strong></p>
<p>De Lakers maakten de grootste verbouwing van de twee. LeBron James tekende in juli voor twee jaar bij de Philadelphia 76ers, en ook Deandre Ayton, Rui Hachimura, Marcus Smart en Luke Kennard vertrokken. Daar kwamen center Walker Kessler (sign-and-trade met Utah, vier jaar en 130 miljoen dollar), Quentin Grimes, Collin Sexton, Sandro Mamukelashvili, Kevon Looney en verdediger Matisse Thybulle voor in de plaats. Austin Reaves verlengde voor vier jaar. Coach JJ Redick begint aan zijn derde seizoen.</p>
<p><strong>Golden State Warriors: rustige zomer, veel blessures</strong></p>
<p>Golden State hield de kern bij elkaar: Kristaps Porziņģis, Al Horford en Draymond Green (voor één jaar) tekenden opnieuw. De grootste nieuwkomer is rookie Yaxel Lendeborg, de nummer elf van de draft en beste speler van de Summer League. Opvallend voor Nederlanders: Quinten Post vertrok naar Memphis nadat de Warriors zijn contractaanbod niet evenaarden, terwijl Malevy Leons op een two-way-contract bij Golden State blijft.</p>
<h3><strong>Blessures en verwachte opstellingen</strong></h3>
{tabel(["Speler", "Team", "Status"], [
    ("Jimmy Butler", "Golden State", "Speelt niet (kruisband, terug begin 2027)"),
    ("Kristaps Porziņģis", "Golden State", "Speelt niet (persoonlijke gezondheidskwestie)"),
    ("Brandin Podziemski", "Golden State", "Speelt niet (onderrug)"),
    ("Moses Moody", "Golden State", "Speelt niet (knie)"),
    ("Stephen Curry", "Golden State", "Speelt naar verwachting (lichte enkelblessure)"),
    ("Collin Sexton", "LA Lakers", "Twijfelachtig (kuit)"),
    ("Luka Dončić, Austin Reaves, Walker Kessler", "LA Lakers", "Fit"),
])}
<p><strong>Verwachte basisvijf Lakers:</strong> Luka Dončić, Austin Reaves, Quentin Grimes, Ziaire Williams, Walker Kessler.</p>
<p><strong>Verwachte basisvijf Warriors:</strong> Stephen Curry, De'Anthony Melton, Gui Santos, Yaxel Lendeborg, Draymond Green. Coach Steve Kerr speelt met Green als center; wie Podziemski vervangt (Melton of Gary Payton II) maakt hij pas kort voor de wedstrijd bekend.</p>
<h3><strong>De spelers om op te letten</strong></h3>
{tabel(["Speler", "Punten", "Rebounds", "Assists", "Bijzonderheid"], [
    ("Luka Dončić (LAL)", "33,5", "7,7", "8,3", "Scoorde 43 punten in de opener van vorig jaar tegen Golden State"),
    ("Austin Reaves (LAL)", "23,3", "4,7", "5,5", "Tweede ster na het vertrek van LeBron"),
    ("Walker Kessler (LAL)", "14,4", "10,8", "3,0", "Nieuwe center, vorig seizoen maar 5 duels door schouderoperatie"),
    ("Stephen Curry (GSW)", "26,6", "3,6", "4,7", "39,3% van achter de driepuntlijn"),
    ("Draymond Green (GSW)", "8,4", "5,5", "5,5", "Spelverdeler en verdedigingsleider"),
    ("Yaxel Lendeborg (GSW)", "15,3", "8,3", "3,8", "Rookie, cijfers uit de voorbereiding"),
])}
<p><em>Gemiddelden per wedstrijd in de reguliere competitie 2025/26 (Lendeborg: voorbereiding 2026).</em></p>
<h3><strong>Odds Lakers – Warriors bij Nederlandse bookmakers</strong></h3>
<p>De bookmakers zien de Lakers als duidelijke favoriet, en die rol werd de afgelopen dagen groter. In de Amerikaanse markt ging de handicap van 5,5 naar 6,5 punten in het voordeel van Los Angeles, vooral door het blessurenieuws bij Golden State. Het verwachte puntentotaal ligt daar rond de 234,5 punten.</p>
{tabel(["Markt", "Bookmaker", "Lakers", "Warriors"], [
    ("Winnaar (incl. verlenging)", "<a href=\"/bookmakers/circus\">Circus</a>", "1,37", "3,20"),
    ("1X2 (reguliere speeltijd, gelijk 19,0)", "<a href=\"/bookmakers/toto\">TOTO</a>", "1,40", "3,00"),
    ("Handicap -12 / +12 (incl. verlenging)", "Circus", "2,60", "1,43"),
])}
<p>Bij Circus kun je ook spelen op het totaal van 239 punten: Over 2,35, Under 1,53. Odds kunnen tot de aftrap nog veranderen; vergelijk ze vlak voor de start nog even.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en wed live mee op Lakers – Warriors</strong></a></p>"""

content3 = f"""<h3><strong>Onze voorspelling: Lakers winnen, maar geen ruime zege</strong></h3>
<p>Op papier is dit een duidelijke zaak. De Lakers hebben Dončić en Reaves fit, een nieuwe center onder de ring en spelen thuis, terwijl Golden State zonder Butler, Porziņģis, Podziemski en Moody aan de start verschijnt. Toch verwachten we geen walk-over. De Warriors hebben een ervaren kern die elkaar blind kent, Curry kan in zijn eentje een wedstrijd openbreken en in de voorbereiding won Golden State beide duels met Los Angeles. De Lakers moeten na een zomer met veel nieuwe spelers nog op elkaar ingespeeld raken.</p>
<p>We rekenen ook op minder punten dan de bookmakers. De vier onderlinge duels van vorig seizoen eindigden op 204, 222, 228 en 230 punten, en Kerr liet doorschemeren dat Curry in het begin van het seizoen minder speelminuten krijgt. Onze voorspelling: <strong>Los Angeles Lakers – Golden State Warriors 117-110</strong>.</p>
<h3><strong>Wedtips voor Lakers – Warriors</strong></h3>
{tabel(["Tip", "Odds", "Bookmaker", "Inzet"], [
    ("Minder dan 239 punten (incl. verlenging)", "1,53", "Circus", "Hoofdtip"),
    ("Golden State Warriors +12 punten", "1,43", "Circus", "Tweede tip"),
    ("Los Angeles Lakers wint (incl. verlenging)", "1,37", "Circus", "Basis voor een combinatie"),
])}
<p><strong>1. Minder dan 239 punten (1,53).</strong> Alle vier de onderlinge duels van vorig seizoen bleven ruim onder deze lijn, en de rekenmodellen in de Amerikaanse markt komen uit op 229 tot 232 punten. Met een Warriors-selectie vol afwezigen, een Curry met een minutenlimiet en een Lakers-ploeg die nog moet wennen, is een totaal boven de 239 voor ons onwaarschijnlijk.</p>
<p><strong>2. Golden State +12 (1,43).</strong> De Warriors mogen met maximaal elf punten verliezen. De Amerikaanse handicap staat op 6,5 punten; deze lijn geeft je bijna een dubbele marge. In de opener van vorig seizoen won Golden State zelfs in Los Angeles (119-109), en in de voorbereiding van dit seizoen won de ploeg beide duels met de Lakers.</p>
<p><strong>3. Lakers wint (1,37).</strong> Een lage quotering, maar wel de logische uitkomst. Handig als stevige basis in een combinatieweddenschap met andere wedstrijden van de avond.</p>
<p>Speel je liever op een speler: Dončić is zonder LeBron de onbetwiste eerste optie bij de Lakers. In de Amerikaanse markt staat zijn puntenlijn op 31,5; vorig seizoen scoorde hij gemiddeld 33,5 en in de opener tegen Golden State zelfs 43.</p>
<h3><strong>Lakers – Warriors live kijken in Nederland</strong></h3>
<p>De makkelijkste manier om de wedstrijd te zien: bij <a href="/bookmakers/bet365">Bet365</a> kijk je NBA-wedstrijden gratis live. Je hebt alleen een account met een kleine storting nodig, en die storting kun je daarna gewoon weer opnemen. In de Verenigde Staten zendt ESPN de wedstrijd uit; in Nederland heeft ESPN de NBA-rechten, maar niet elke wedstrijd staat op een van de Nederlandse ESPN-kanalen. Met <strong>NBA League Pass</strong>, de betaalde streamingdienst van de competitie, kun je ook alle wedstrijden volgen.</p>
<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk Lakers – Warriors live</strong></a></p>
<h3><strong>Meer NBA</strong></h3>
<p>Lees ook onze voorspellingen voor <a href="/nieuws/pistons-celtics-voorspelling-wedtips-nba-opening-2026">Pistons – Celtics</a> en <a href="/nieuws/spurs-thunder-voorspelling-wedtips-nba-opening-2026">Spurs – Thunder</a>, en ons overzicht <a href="/nieuws/welke-nederlanders-spelen-in-de-nba">Welke Nederlanders spelen in de NBA</a>. Alle basketbaltips vind je op onze pagina <a href="/wedden-op-nba-voorspellingen-en-wedtips---basketbal">wedden op de NBA</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Lakers – Warriors?</strong><br>Donderdag 22 oktober 2026 om 04:00 Nederlandse tijd, in de nacht van woensdag op donderdag. In Los Angeles is het dan woensdagavond 19:00.</p>
<p><strong>Waar wordt Lakers – Warriors gespeeld?</strong><br>In de Crypto.com Arena in Los Angeles. De Lakers zijn de thuisploeg.</p>
<p><strong>Speelt LeBron James mee?</strong><br>Nee. LeBron James tekende deze zomer bij de Philadelphia 76ers en speelt dus niet meer voor de Lakers.</p>
<p><strong>Speelt Stephen Curry tegen de Lakers?</strong><br>Naar verwachting wel. Hij verzwikte zijn enkel in de voorbereiding, maar coach Steve Kerr noemde hem speelklaar. Wel is de kans groot dat zijn speeltijd beperkt blijft.</p>
<p><strong>Wie is favoriet: Lakers of Warriors?</strong><br>De Lakers, met een quotering rond 1,37. De Warriors staan rond 3,20.</p>
<p><strong>Speelt er een Nederlander mee?</strong><br>Malevy Leons staat met een two-way-contract onder contract bij Golden State; of hij speelt is nog niet bekend. Quinten Post speelt sinds deze zomer voor de Memphis Grizzlies.</p>
<p><strong>Wat is onze voorspelling voor Lakers – Warriors?</strong><br>De Lakers winnen met 117-110. Onze hoofdtip is minder dan 239 punten (1,53 bij Circus).</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

WEDTIPS = {"wedtip-1-2": "Minder dan 239 punten (incl. verlenging)", "quotering-wedtip-1": "1.53",
           "wedtip-2-2": "Golden State Warriors +12 punten", "quotering-wedtip-2": "1.43",
           "wedtip-3-2": "Los Angeles Lakers wint (incl. verlenging)", "quotering-wedtip-3": "1.37",
           "bookmaker-wedtips": "64ff0fbd5a8f205b05d54670"}

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_BASKETBAL, "competitie": COMPETITIE_NBA,
          "datum-tijd-van-wedstrijd": "2026-10-22T02:00:00.000Z",
          "publicatiedatum": datetime.now(timezone.utc).isoformat(), **WEDTIPS}
    if "--live" not in sys.argv:
        import re
        tekst = re.sub(r"<[^>]+>", " ", content + content2 + content3)
        print(len(SAMENVATTING), "tekens samenvatting |", len(tekst.split()), "woorden"); sys.exit()
    print("item:", WF.create_live(fd))
