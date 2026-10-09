# -*- coding: utf-8 -*-
"""Los artikel: Welke Nederlanders spelen in de NBA? (2026/27, kernfeiten nagelopen 9 okt 2026).
  python3 specials/nederlanders_nba_2026.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Welke Nederlanders spelen in de NBA? Alle spelers in 2026/27"
SLUG = "welke-nederlanders-spelen-in-de-nba"
SAMENVATTING = ("Drie Nederlanders staan in 2026/27 onder contract in de NBA: Quinten Post (Memphis), Malevy Leons "
                "(Warriors) en Tristan Enaruna (Cavaliers). Het overzicht.")
RUBRIEK_BASKETBAL = "672293e14a76d88272bc0b61"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in koppen)
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}><thead><tr>{kop}</tr></thead><tbody>{body}</tbody></table>"


content = f"""<p><strong>In het seizoen 2026/27 staan drie Nederlanders onder contract bij een NBA-team: Quinten Post (Memphis Grizzlies), Malevy Leons (Golden State Warriors) en Tristan Enaruna (Cleveland Cavaliers). Post heeft een gewoon NBA-contract, Leons en Enaruna spelen op basis van een two-way-contract. Rienk Mast probeert via een trainingskampcontract bij de Indiana Pacers de vierde te worden.</strong></p>
<p>Lange tijd was een Nederlander in de NBA een uitzondering. Na Rik Smits, Francisco Elson en Dan Gadzuric bleef het jarenlang stil, maar sinds 2024 maakten in korte tijd vier landgenoten hun debuut. Hieronder lees je wie er nu in de NBA spelen, wat hun contract precies inhoudt en welke Nederlanders je eerder in de beste basketbalcompetitie ter wereld zag.</p>
<h3><strong>Nederlanders in de NBA 2026/27</strong></h3>
{tabel(["Speler", "Team", "Positie", "Contract"], [
    ("Quinten Post", "Memphis Grizzlies", "Center", "NBA-contract (3 jaar)"),
    ("Malevy Leons", "Golden State Warriors", "Forward", "Two-way"),
    ("Tristan Enaruna", "Cleveland Cavaliers", "Forward", "Two-way"),
    ("Rienk Mast", "Indiana Pacers", "Center/forward", "Exhibit 10 (trainingskamp)"),
])}
<p><em>Mast staat in de tabel als kanshebber: met een Exhibit 10-contract heeft hij nog geen gegarandeerde plek in de NBA-selectie.</em></p>"""

content2 = f"""<h3><strong>Quinten Post: na de Warriors verder in Memphis</strong></h3>
<p>Quinten Post heeft van de huidige Nederlanders de sterkste positie. De center uit Amsterdam werd in de NBA Draft van 2024 als 52e gekozen en groeide bij de Golden State Warriors uit van tweederonde-pick tot rotatiespeler. Zijn waarde zit vooral in een combinatie die je zelden ziet bij een speler van 2,13 meter: hij kan van ver schieten en trekt daarmee de verdediging van de tegenstander uit elkaar.</p>
<p>In de zomer van 2026 was Post een zogenoemde restricted free agent. Memphis bood hem een contract (offer sheet) aan van drie jaar en in totaal 30 miljoen dollar, waarvan het eerste jaar gegarandeerd is. Golden State had het recht om dat bod te evenaren, maar deed dat niet. Daarmee ging Post na twee seizoenen naar de Grizzlies. Het was voor het eerst sinds 2020 dat een NBA-club een speler op deze manier kwijtraakte.</p>
<h3><strong>Malevy Leons: two-way-speler bij Golden State</strong></h3>
<p>Malevy Leons schreef in november 2024 geschiedenis. De forward uit IJmuiden maakte toen namens de Oklahoma City Thunder zijn NBA-debuut en was de eerste Nederlander in bijna dertien jaar die minuten maakte in de NBA. Leons speelde collegebasketbal bij Bradley University en is een energieke verdediger die op meerdere posities uit de voeten kan.</p>
<p>In december 2025 tekende hij een two-way-contract bij de Golden State Warriors. Daarmee kan hij zowel voor de Warriors als voor hun opleidingsteam Santa Cruz Warriors in de G League spelen. Zijn beste NBA-avond kende hij in februari 2026 in Memphis: negen punten in achttien minuten bij een ruime zege. Ook in 2026/27 is Leons via een two-way-contract aan de Warriors verbonden.</p>
<h3><strong>Tristan Enaruna: de tiende Nederlander in de NBA</strong></h3>
<p>Tristan Enaruna uit Almere nam de lange weg. Hij speelde collegebasketbal in de Verenigde Staten en bouwde daarna in de G League aan zijn kans. Eind januari 2026 tekende hij een two-way-contract bij de Cleveland Cavaliers, en op 1 februari 2026 volgde zijn debuut. Daarmee werd hij de tiende Nederlander ooit met speelminuten in de NBA.</p>
<p>In zijn eerste seizoen kwam Enaruna tot negen wedstrijden voor Cleveland, met gemiddeld 4,1 punten. Net als Leons kan hij met zijn two-way-contract heen en weer tussen het NBA-team en het G League-team Cleveland Charge.</p>
<h3><strong>Rienk Mast: vechten voor een plek bij Indiana</strong></h3>
<p>De volgende Nederlander die op de deur klopt, is Rienk Mast. De big man uit Groningen leidde Nebraska naar het beste seizoen in de geschiedenis van het programma, maar werd in de NBA Draft van 2026 niet gekozen. Direct daarna tekende hij een Exhibit 10-contract bij de Indiana Pacers. Hij speelde de Summer League voor Indiana en zit in het trainingskamp.</p>
<p>Een Exhibit 10-contract geeft geen garantie op een plek in de selectie. De club kan het omzetten in een two-way-contract; blijft dat uit, dan kan Mast via het G League-team van Indiana, de Noblesville Boom, verder werken aan zijn kans.</p>"""

content3 = f"""<h3><strong>NBA-contract, two-way of Exhibit 10: wat is het verschil?</strong></h3>
{tabel(["Contract", "Wat houdt het in?", "Nederlander"], [
    ("Standaard NBA-contract", "Vaste plek in de selectie van 15, volledig NBA-salaris", "Quinten Post"),
    ("Two-way", "Speler pendelt tussen het NBA-team en het G League-team, met een beperkt aantal NBA-wedstrijden", "Malevy Leons, Tristan Enaruna"),
    ("Exhibit 10", "Trainingskampcontract zonder garantie, kan worden omgezet in een two-way-contract", "Rienk Mast"),
])}
<h3><strong>Alle Nederlanders die in de NBA speelden</strong></h3>
<p>Tien Nederlanders kwamen ooit in actie in de NBA of de voorloper daarvan. De bekendste is Rik Smits, die zijn hele carrière bij de Indiana Pacers speelde en in 1998 het All-Star Game haalde. Francisco Elson werd in 2007 kampioen met de San Antonio Spurs.</p>
{tabel(["#", "Speler", "Bekendste team"], [
    ("1", "Hank Beenders", "Providence Steamrollers"),
    ("2", "Swen Nater", "San Diego Clippers"),
    ("3", "Rik Smits", "Indiana Pacers"),
    ("4", "Geert Hammink", "Orlando Magic"),
    ("5", "Francisco Elson", "San Antonio Spurs"),
    ("6", "Dan Gadzuric", "Milwaukee Bucks"),
    ("7", "Malevy Leons", "Golden State Warriors"),
    ("8", "Quinten Post", "Memphis Grizzlies"),
    ("9", "Jesse Edwards", "Minnesota Timberwolves"),
    ("10", "Tristan Enaruna", "Cleveland Cavaliers"),
])}
<h3><strong>NBA kijken in Nederland</strong></h3>
<p>Wedstrijden uit de NBA zie je in Nederland bij <a href="/zenders/espn">ESPN</a>, vooral in de avond en nacht op ESPN 2 tot en met 4. Wil je elke wedstrijd kunnen volgen, dan is NBA League Pass de streamingdienst van de competitie zelf.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoeveel Nederlanders spelen er in de NBA?</strong><br>In 2026/27 zijn er drie Nederlanders met een NBA-contract: Quinten Post, Malevy Leons en Tristan Enaruna. Rienk Mast vecht bij Indiana nog om een plek.</p>
<p><strong>Bij welk team speelt Quinten Post?</strong><br>Bij de Memphis Grizzlies. Hij tekende in de zomer van 2026 een contract voor drie jaar; Golden State zag af van matchen.</p>
<p><strong>Wat is een two-way-contract?</strong><br>Een contract waarmee een speler zowel voor het NBA-team als voor het bijbehorende G League-team speelt, met een beperkt aantal NBA-wedstrijden per seizoen.</p>
<p><strong>Wie was de eerste Nederlander in de NBA?</strong><br>Hank Beenders, die in de jaren veertig speelde in de BAA, de voorloper van de NBA.</p>
<p><strong>Wie is de bekendste Nederlandse NBA-speler?</strong><br>Rik Smits. De center uit Eindhoven speelde twaalf seizoenen voor de Indiana Pacers en stond in 2000 met de club in de NBA Finals.</p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_BASKETBAL, "competitie": COMPETITIE_NBA,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting"); sys.exit()
    print("item:", WF.create_live(fd))
