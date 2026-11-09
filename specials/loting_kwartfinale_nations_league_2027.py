# -*- coding: utf-8 -*-
"""Los artikel: loting kwartfinales Nations League 2026/27 (wanneer, hoe het werkt, mogelijke tegenstanders Oranje), 9-11-2026.

Bronnen (geraadpleegd ma 9-11-2026):
- Stand League A na speeldag 4 + resterend programma (data, aftrap, stadions): UEFA standings-/match-API
  (standings.uefa.com/v1/standings?competitionId=2014&seasonYear=2027, match.uefa.com/v5/matches?competitionId=2014&seasonYear=2027),
  dezelfde data als https://www.uefa.com/uefanationsleague/standings/ ; gecontroleerd met de Wikipedia-pagina 2026-27 League A.
- Regels kwartfinale: UEFA-reglement Nations League 2026/27, art. 17 (17.01 8 teams; 17.02 loting, groepswinnaars geplaatst tegen
  een nummer 2 uit een andere groep; 17.03 twee duels, nummer 2 heen thuis; 17.05 aparte loting halve finales):
  https://documents.uefa.com/r/Regulations-of-the-UEFA-Nations-League-2026/27/Article-17-Match-system-League-A-knockout-stage-Online
- Data kwartfinales 25-30 maart 2027 (heen 25-27, terug 28-30), Finals 9-13 juni 2027: UEFA all you need to know +
  specials/nations_league_2028_feiten.md.
- EK-reglement 2026-28 art. 13.02: winnaars van de kwartfinales ("one placeholder for each quarter-final pairing") elk in een andere
  groep van vier; groep van vijf max. één verliezende kwartfinalist:
  https://documents.uefa.com/r/Regulations-of-the-UEFA-European-Football-Championship-2026-28/Article-13-Group-formation-qualifying-group-stage-Online
- EK-loting 6 dec 2026, 18:00 (17:00 GMT), ICC Belfast: https://www.uefa.com/euro2028/news/029f-1f2ff991e87b-345fffcd69c3-1000/
- Precedent: kwartfinaleloting 2024/25 op vr 22 nov 2024 in Nyon (UEFA-voorbeschouwing + AP/Reuters/RFEF).
- Oranje – Spanje 2025: UEFA match-API (20-3-2025 De Kuip 2-2; 23-3-2025 Mestalla 3-3, strafschoppen 4-5 vanuit NL gezien).
- Odds 711 (Kambi sevelevnl), ma 9-11-2026 ±16:45: groepswinnaar A1/A2/A3 en eindwinnaar Nations League.

Bewust NIET gebruikt (onbevestigd): datum, tijd en plaats van de kwartfinaleloting (UEFA heeft die nog niet bekendgemaakt);
of de halve finales op dezelfde dag worden geloot; gastheer Finals 2027 (besluit Uitvoerend Comité in december, 6 of 7 dec);
waar je de loting/kwartfinales op tv ziet; doelpuntenmakers Nederland – Spanje 2025.
  python3 specials/loting_kwartfinale_nations_league_2027.py   (dry run)"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

# Na de loting bijwerken: datum/plaats loting (TIJDLIJN + intro + FAQ), de echte tegenstander, en de stand na speeldag 6.
NA_LOTING = "bijwerken met de uitkomst van de loting"

SLUG = "loting-kwartfinale-nations-league-2027-mogelijke-tegenstanders-oranje"
RUBRIEK = "66d6d655bc312d5c0e834ecd"   # Oranje/interlands
TITEL = "Loting kwartfinale Nations League: tegenstanders Oranje"
SAMENVATTING = ("Wanneer is de loting voor de kwartfinales van de Nations League, hoe werkt die en wie kan Oranje in maart "
                "2027 treffen? De stand van alle groepen.")

# deelkaart: og_kaarten/gsod.py
OG_LOGO = "nations-league-logo.png"
OG_EYEBROW = "Nations League · Oranje"
OG_KOP = "Loting kwartfinale<br><em>wie treft Oranje?</em>"
OG_TEGELS = [("Kwartfinale", "25–30 mrt"), ("Duels", "2")]
OG_KOPJE = "Mogelijke tegenstanders van Oranje"
OG_RECHTS = "Groep"
OG_RIJEN = [("Als nr. 1", "Italië, België, Engeland of Denemarken", "A1/A3/A4"),
            ("Als nr. 2", "Frankrijk, Spanje of Portugal", "A1/A3/A4"),
            ("Kan niet", "Griekenland, Duitsland of Servië", "A2"),
            ("Loting", "Datum nog niet bekend", "Vóór 6/12")]

L = {"nlg": '<a href="/competities/uefa-nations-league">Nations League</a>',
     "uitleg": '<a href="/nieuws/hoe-werkt-de-nations-league-complete-uitleg-2026-2027">hoe de Nations League werkt</a>',
     "opzet": '<a href="/nieuws/nations-league-nieuwe-opzet-2028-wat-betekent-het-voor-oranje">wat Oranje nodig heeft in de laatste twee duels</a>',
     "selectie": '<a href="/nieuws/selectie-oranje-november-2026-griekenland-duitsland">de selectie van Oranje</a>',
     "711": '<a href="/bookmakers/711">711</a>',
     "legaal": '<a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>'}
LANDSLUG = {"Nederland": "nederland", "Griekenland": "griekenland", "Duitsland": "duitsland", "Servië": "servie",
            "Frankrijk": "frankrijk", "Italië": "italie", "België": "belgie", "Turkije": "turkije",
            "Spanje": "spanje", "Engeland": "engeland", "Kroatië": "kroatie", "Tsjechië": "tsjechie",
            "Portugal": "portugal", "Denemarken": "denemarken", "Wales": "wales", "Noorwegen": "noorwegen"}


def land(n):
    return f'<a href="/clubs/{LANDSLUG[n]}">{n}</a>'


# Stand na speeldag 4 (UEFA, 9-11-2026): land, G, W, GL, V, voor, tegen, punten
STAND = {
    "A1": [("Frankrijk", 4, 3, 1, 0, 7, 2, 10), ("Italië", 4, 2, 1, 1, 8, 5, 7),
           ("België", 4, 2, 0, 2, 6, 5, 6), ("Turkije", 4, 0, 0, 4, 2, 11, 0)],
    "A2": [("Nederland", 4, 2, 2, 0, 7, 5, 8), ("Griekenland", 4, 2, 2, 0, 5, 3, 8),
           ("Duitsland", 4, 1, 2, 1, 3, 2, 5), ("Servië", 4, 0, 0, 4, 3, 8, 0)],
    "A3": [("Spanje", 4, 4, 0, 0, 12, 5, 12), ("Engeland", 4, 3, 0, 1, 14, 3, 9),
           ("Kroatië", 4, 1, 0, 3, 4, 14, 3), ("Tsjechië", 4, 0, 0, 4, 2, 10, 0)],
    "A4": [("Portugal", 4, 4, 0, 0, 9, 4, 12), ("Denemarken", 4, 2, 0, 2, 7, 7, 6),
           ("Wales", 4, 1, 0, 3, 2, 5, 3), ("Noorwegen", 4, 1, 0, 3, 6, 8, 3)],
}

# Resterend programma League A (UEFA; Nederlandse tijd)
PROGRAMMA = [("Do 12 november", "18:00", "Turkije – België", "A1"),
             ("Do 12 november", "20:45", "Italië – Frankrijk", "A1"),
             ("Do 12 november", "20:45", "Tsjechië – Spanje", "A3"),
             ("Do 12 november", "20:45", "Engeland – Kroatië", "A3"),
             ("Vr 13 november", "20:45", "<strong>Nederland – Griekenland</strong>", "A2"),
             ("Vr 13 november", "20:45", "Servië – Duitsland", "A2"),
             ("Za 14 november", "18:00", "Noorwegen – Wales", "A4"),
             ("Za 14 november", "20:45", "Portugal – Denemarken", "A4"),
             ("Zo 15 november", "20:45", "Frankrijk – Turkije", "A1"),
             ("Zo 15 november", "20:45", "België – Italië", "A1"),
             ("Zo 15 november", "20:45", "Kroatië – Tsjechië", "A3"),
             ("Zo 15 november", "20:45", "Spanje – Engeland", "A3"),
             ("Ma 16 november", "20:45", "<strong>Duitsland – Nederland</strong>", "A2"),
             ("Ma 16 november", "20:45", "Griekenland – Servië", "A2"),
             ("Di 17 november", "20:45", "Denemarken – Noorwegen", "A4"),
             ("Di 17 november", "20:45", "Wales – Portugal", "A4")]

KF_DATA = "25 tot en met 30 maart 2027"
HEEN, TERUG = "25 t/m 27 maart 2027", "28 t/m 30 maart 2027"
FINALS = "9 tot en met 13 juni 2027"

TIJDLIJN = [("13 en 16 november 2026", "Laatste groepsduels van Oranje", "Bevestigd"),
            ("17 november 2026", "Einde van de groepsfase", "Bevestigd"),
            ("Nog niet bekend", "Loting kwartfinales", "Verwacht eind november"),
            ("6 december 2026, 18:00", "Loting EK 2028-kwalificatie in Belfast", "Bevestigd"),
            (HEEN, "Heenduels kwartfinales (nummer 2 speelt thuis)", "Bevestigd"),
            (TERUG, "Returns kwartfinales (groepswinnaar speelt thuis)", "Bevestigd"),
            (FINALS, "Finals: halve finales, troostfinale en finale", "Bevestigd, gastland nog niet")]

# Oranje als groepswinnaar treft een nummer 2 uit A1/A3/A4; als nummer 2 een groepswinnaar uit A1/A3/A4
ALS_EEN = [("A1", "Italië of België", "Frankrijk"),
           ("A3", "Engeland", "Spanje (Kroatië alleen theoretisch)"),
           ("A4", "Denemarken", "Wales, Noorwegen of Portugal")]
ALS_TWEE = [("A1", "Frankrijk", "Italië of België"),
            ("A3", "Spanje", "Engeland"),
            ("A4", "Portugal", "Denemarken")]

# 711 (Kambi), ma 9-11-2026 ±16:45
ODDS_GROEP = {"A1": [("Frankrijk", "1,20"), ("Italië", "6,00"), ("België", "6,50")],
              "A2": [("Nederland", "1,72"), ("Griekenland", "2,75"), ("Duitsland", "6,00")],
              "A3": [("Spanje", "1,14"), ("Engeland", "5,50")]}
ODDS_WINNAAR = [("Spanje", "3,00"), ("Frankrijk", "3,75"), ("Engeland", "5,50"), ("Portugal", "6,00"),
                ("Duitsland", "11,00"), ("Nederland", "13,00")]


def stand_tabel(g):
    rijen = []
    for i, (n, gs, w, d, v, dv, dt, p) in enumerate(STAND[g], 1):
        rijen.append((str(i), land(n) if n != "Nederland" else f"<strong>{land(n)}</strong>", str(gs), f"{w}-{d}-{v}",
                      f"{dv}-{dt}", f"{dv - dt:+d}".replace("+0", "0"), f"<strong>{p}</strong>"))
    return tabel(["#", "Land", "G", "W-G-V", "Doelpunten", "Saldo", "Punten"], rijen)


def odds_zin(g):
    return ", ".join(f"{n} {o}" for n, o in ODDS_GROEP[g])


content = f"""<p><strong>De datum van de loting voor de kwartfinales van de {L['nlg']} is nog niet bekend. UEFA heeft nog geen dag, tijd of plaats gecommuniceerd. Wel staat vast dat de kwartfinales van {KF_DATA} worden gespeeld, in een thuis- en een uitduel. Oranje is nog niet zeker van een plek bij de laatste acht. Als groepswinnaar treft Oranje een nummer 2 uit groep A1, A3 of A4, zoals Italië, België, Engeland of Denemarken. Als nummer 2 wacht een groepswinnaar, waarschijnlijk Frankrijk, Spanje of Portugal.</strong></p>
<p>Oranje speelt op vrijdag 13 november tegen Griekenland en op maandag 16 november in Berlijn tegen Duitsland. Na die twee duels is duidelijk of het Nederlands elftal in maart 2027 een kwartfinale speelt, en zo ja, als groepswinnaar of als nummer 2. Dat maakt veel uit voor de mogelijke tegenstanders. Het rekenwerk lees je in ons artikel over {L['opzet']}.</p>
<h3><strong>Wanneer is de loting voor de kwartfinales?</strong></h3>
<p>UEFA heeft de datum van de loting nog niet bekendgemaakt. In het reglement staat alleen dat de kwartfinales door loting worden ingedeeld, niet wanneer. Bij de vorige editie vond de loting plaats op vrijdag 22 november 2024, vijf dagen na de laatste groepsduels, op het hoofdkantoor van UEFA in Nyon. Toen werd Oranje aan Spanje gekoppeld.</p>
<p>Er is een aanwijzing dat de loting ook nu snel na de groepsfase komt. Op zondag 6 december 2026 loot UEFA in Belfast de groepen voor de kwalificatie voor het EK 2028. Volgens het EK-reglement worden de kwartfinalekoppels daarin als vaste plaatshouders meegenomen. De kwartfinales moeten dus vóór 6 december geloot zijn. We verwachten de loting daarom eind november. Zodra UEFA de datum bevestigt, werken we dit artikel bij.</p>
{tabel(["Wanneer", "Wat", "Status"], [(f"<strong>{a}</strong>", b, c) for a, b, c in TIJDLIJN])}
<h3><strong>Zo werkt de loting</strong></h3>
<p>De acht kwartfinalisten zijn de vier groepswinnaars en de vier nummers 2 van League A. Voor de loting gelden deze regels:</p>
<ul><li><strong>Groepswinnaars zijn geplaatst.</strong> Elke groepswinnaar wordt gekoppeld aan een nummer 2.</li><li><strong>Geen landen uit dezelfde groep.</strong> Een groepswinnaar kan niet loten tegen de nummer 2 uit de eigen groep. Oranje kan dus niet tegen Griekenland, Duitsland of Servië.</li><li><strong>Thuisvoordeel in de return.</strong> De nummer 2 speelt de heenwedstrijd thuis, de groepswinnaar de return.</li><li><strong>Twee duels.</strong> Wie over twee wedstrijden de meeste doelpunten maakt, gaat door. Bij een gelijke stand volgen een verlenging en zo nodig strafschoppen. Uitdoelpunten tellen niet extra.</li></ul>
<p>UEFA mag nog extra voorwaarden toevoegen, maar die moeten worden goedgekeurd door het Uitvoerend Comité. De vier winnaars van de kwartfinales spelen van {FINALS} de Finals: halve finales op 9 en 10 juni, troostfinale en finale op 13 juni.</p>
<p><strong>Bepaalt de loting ook de weg naar de finale?</strong> Niet bij de kwartfinaleloting zelf. De halve finales worden volgens het reglement apart geloot. Bij de vorige editie gebeurde dat op dezelfde dag, direct na de kwartfinaleloting. Of dat nu ook zo gaat, is nog niet bekend. Het gastland van de Finals wordt niet geloot. Dat kiest het Uitvoerend Comité van UEFA in december, bij voorkeur uit de kwartfinalisten.</p>"""

content2 = f"""<h3><strong>De stand in League A na vier speelronden</strong></h3>
<p>Na vier van de zes speelronden zijn Spanje en Portugal zeker van de kwartfinales. Engeland is er zo goed als zeker van. In de andere groepen valt de beslissing in de laatste interlandperiode, van 12 tot en met 17 november.</p>
<p><strong>Groep A1</strong></p>
{stand_tabel("A1")}
<p><strong>Groep A2</strong></p>
{stand_tabel("A2")}
<p><strong>Groep A3</strong></p>
{stand_tabel("A3")}
<p><strong>Groep A4</strong></p>
{stand_tabel("A4")}
<p><em>Stand volgens UEFA op maandag 9 november 2026. G = gespeeld, W-G-V = winst, gelijk en verlies. Bij gelijke punten telt eerst het onderlinge resultaat.</em></p>
<h3><strong>Het resterende programma in League A</strong></h3>
{tabel(["Datum", "Aftrap", "Wedstrijd", "Groep"], [(f"<strong>{d}</strong>", t, w, g) for d, t, w, g in PROGRAMMA])}
<h3><strong>Wie worden groepswinnaar en nummer 2?</strong></h3>
<p><strong>Groep A1:</strong> {land('Frankrijk')} staat met 10 punten bovenaan, maar is nog niet zeker van de kwartfinales. Met een zege bij {land('Italië')} in Milaan is Frankrijk groepswinnaar. Om de tweede plek gaat het tussen Italië (7) en {land('België')} (6), die elkaar op zondag 15 november in Brussel treffen. België won in Rome met 0-2. Eindigen ze gelijk op punten, dan heeft België dus een voorsprong in het onderlinge resultaat. Bij 711 is Frankrijk de grote favoriet voor de groepswinst ({odds_zin('A1')}).</p>
<p><strong>Groep A2:</strong> {land('Nederland')} en {land('Griekenland')} hebben allebei 8 punten. Oranje staat bovenaan omdat het meer doelpunten maakte. {land('Duitsland')} heeft 5 punten en kan nog groepswinnaar worden. {land('Servië')} kan geen nummer 1 of 2 meer worden. Wint Oranje van Griekenland en haalt het een punt in Berlijn, dan is het groepswinnaar. Bij 711 is Oranje favoriet voor de groepswinst ({odds_zin('A2')}).</p>
<p><strong>Groep A3:</strong> {land('Spanje')} (12) en {land('Engeland')} (9) gaan vrijwel zeker allebei door. {land('Kroatië')} kan Engeland alleen nog inhalen met twee zeges, een Engelse nederlaag in Madrid en een enorme overwinning op de Engelsen, die in Rijeka met 0-7 wonnen. Over de groepswinst beslist het duel in Madrid op 15 november. Spanje heeft daar genoeg aan een gelijkspel, omdat het op Wembley al met 2-3 won. Ook hier is Spanje favoriet ({odds_zin('A3')}).</p>
<p><strong>Groep A4:</strong> {land('Portugal')} won alle vier de duels en is zeker van de kwartfinales. Met één punt uit de duels met {land('Denemarken')} en {land('Wales')} is het ook zeker groepswinnaar. Denemarken (6) is favoriet voor de tweede plek en is met een zege op {land('Noorwegen')} op 17 november zeker van de kwartfinales. Wales en Noorwegen staan op 3 punten en spelen op 14 november tegen elkaar in Oslo. Voor groep A4 bood 711 op maandag geen groepswinnaarsmarkt aan.</p>
<h3><strong>De mogelijke tegenstanders van Oranje</strong></h3>
<p><strong>Als Oranje groepswinnaar wordt</strong>, treft het een nummer 2 uit groep A1, A3 of A4. Oranje speelt dan eerst uit en de return thuis.</p>
{tabel(["Groep", "Waarschijnlijke nummer 2", "Ook nog mogelijk"], ALS_EEN)}
<p><strong>Als Oranje tweede wordt</strong>, treft het een groepswinnaar uit groep A1, A3 of A4. Oranje speelt dan de heenwedstrijd thuis en de return uit.</p>
{tabel(["Groep", "Waarschijnlijke groepswinnaar", "Ook nog mogelijk"], ALS_TWEE)}
<p>Het verschil is groot. Als groepswinnaar ontloopt Oranje Spanje, Frankrijk en Portugal, zolang die drie hun groep winnen. Engeland, bij de bookmakers de nummer drie voor de eindzege, blijft dan wel mogelijk. Als nummer 2 is Frankrijk, Spanje of Portugal vrijwel zeker de tegenstander. Wordt Oranje derde, dan speelt het geen kwartfinale.</p>"""

content3 = f"""<h3><strong>Wat zeggen de bookmakers?</strong></h3>
<p>Bij {L['711']} is Spanje de favoriet voor de eindzege in deze Nations League. Oranje staat zesde in de lijst (maandag 9 november).</p>
{tabel(["Land", "Quotering eindwinnaar"], [(land(n) if n != "Nederland" else f"<strong>{land(n)}</strong>", o) for n, o in ODDS_WINNAAR])}
<p>Voor Nederland – Griekenland staat een Nederlandse zege bij 711 op 1,47. Wed alleen bij een bookmaker met een vergunning van de Kansspelautoriteit; lees {L['legaal']}.</p>
<h3><strong>Waarom de kwartfinale extra belangrijk is</strong></h3>
<p>Een plek in de kwartfinale levert meer op dan twee extra wedstrijden. De acht kwartfinalisten eindigen in de top 8 van de eindranglijst en beginnen in 2028/29 zeker in League A. Dat is de eerste editie in de nieuwe opzet met drie leagues van 18 landen. Ook voor de EK-kwalificatie heeft het gevolgen. De winnaars van de kwartfinales komen bij de EK-loting elk in een andere groep van vier landen terecht. Een groep van vijf mag hooguit één verliezende kwartfinalist bevatten. Wil je eerst de basis weten, lees dan {L['uitleg']}.</p>
<h3><strong>De vorige kwartfinale: Oranje tegen Spanje</strong></h3>
<p>De kwartfinales bestaan sinds de editie 2024/25. Oranje speelde toen meteen een kraker. Op 20 maart 2025 werd het in De Kuip in Rotterdam 2-2 tegen Spanje. Drie dagen later eindigde de return in het Mestalla in Valencia na verlenging in 3-3. Het werd dus 5-5 over twee duels, en Spanje won de strafschoppenserie met 5-4. Spanje haalde daarna de finale, maar verloor die na strafschoppen van Portugal.</p>
<p>Bondscoach Xavi Hernández riep voor november 25 spelers op, onder wie de teruggekeerde Frenkie de Jong. Lees alles over {L['selectie']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wanneer is de loting voor de kwartfinales van de Nations League?</strong><br>Dat is nog niet bekend. UEFA heeft geen datum genoemd. Bij de vorige editie was de loting op 22 november, vijf dagen na de groepsfase. Omdat de EK-loting op 6 december de kwartfinalekoppels al meeneemt, verwachten we de loting eind november.</p>
<p><strong>Wanneer worden de kwartfinales gespeeld?</strong><br>Van {KF_DATA}. De heenduels zijn van {HEEN}, de returns van {TERUG}. De groepswinnaar speelt de return thuis.</p>
<p><strong>Tegen wie kan Oranje in de kwartfinale spelen?</strong><br>Als groepswinnaar tegen een nummer 2 uit groep A1, A3 of A4, zoals Italië, België, Engeland of Denemarken. Als nummer 2 tegen een groepswinnaar uit die groepen, waarschijnlijk Frankrijk, Spanje of Portugal. Landen uit de eigen groep (Griekenland, Duitsland en Servië) zijn uitgesloten.</p>
<p><strong>Wat gebeurt er bij een gelijke stand in de kwartfinale?</strong><br>Dan volgen een verlenging en zo nodig strafschoppen. Uitdoelpunten tellen niet extra.</p>
<p><strong>Wanneer en waar zijn de Finals?</strong><br>Van {FINALS}. Het gastland is nog niet bekend. Het Uitvoerend Comité van UEFA kiest dat in december, bij voorkeur uit de kwartfinalisten.</p>
<p><strong>Hoe ging de vorige kwartfinale van Oranje?</strong><br>In maart 2025 schakelde Spanje Oranje uit. Het werd 2-2 in Rotterdam en 3-3 na verlenging in Valencia. Spanje won de strafschoppenserie met 5-4.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    alles = content + content2 + content3
    tekst = re.sub(r"<[^>]+>", " ", alles)
    w = len(tekst.split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", w, "woorden")
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert 900 <= w <= 2000, w
    assert "<h2" not in alles and "<h4" not in alles and "betcity" not in alles.lower() and "/go/" not in alles
    for slecht in ("opstellingvandaag", "footymetrics", "espn", "wikipedia", "waaroptv"):
        assert slecht not in alles.lower(), slecht
    assert content.startswith("<p><strong>") and content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    assert "<h3><strong>Veelgestelde vragen</strong></h3>" in content3
    assert 4 <= content3.split("Veelgestelde vragen")[1].count("?</strong><br>") <= 6
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/") and not href.startswith("//"), href
    # stand intern consistent: punten = 3W + G, gespeeld = W+G+V, gesorteerd op punten
    for g, rijen in STAND.items():
        for n, gs, wi, d, v, dv, dt, p in rijen:
            assert p == 3 * wi + d and gs == wi + d + v == 4, (g, n)
        assert [r[7] for r in rijen] == sorted([r[7] for r in rijen], reverse=True), g
    assert sum(r[5] for g in STAND.values() for r in g) == sum(r[6] for g in STAND.values() for r in g)  # voor = tegen
    # feiten in de tekst gelijk aan de data
    pt = {r[0]: r[7] for g in STAND.values() for r in g}
    assert pt["Frankrijk"] == 10 and pt["Italië"] == 7 and pt["België"] == 6 and pt["Spanje"] == 12 and pt["Engeland"] == 9
    assert pt["Nederland"] == pt["Griekenland"] == 8 and pt["Duitsland"] == 5 and pt["Denemarken"] == 6 and pt["Wales"] == pt["Noorwegen"] == 3
    assert pt["Kroatië"] + 6 <= pt["Engeland"] and pt["Tsjechië"] + 6 < pt["Spanje"]    # Spanje zeker top 2; Kroatië max. gelijk
    assert pt["Denemarken"] + 6 <= pt["Portugal"] and pt["Wales"] + 6 < pt["Portugal"] + 1  # Portugal met 1 punt groepswinnaar
    assert len(PROGRAMMA) == 16 and sum("Nederland" in p[2] for p in PROGRAMMA) == 2
    # data in tabel, FAQ en intro gelijk
    assert alles.count(KF_DATA) >= 2 and HEEN in content and HEEN in content3 and TERUG in content3
    assert alles.count(FINALS) >= 3 and "22 november" in content and "22 november" in content3
    assert "6 december" in content and "6 december" in content3
    # mogelijke tegenstanders: geen land uit A2, en alles in de kaart staat ook in de tabellen
    for _, a, b in ALS_EEN + ALS_TWEE:
        assert not any(x in a + b for x in ("Griekenland", "Duitsland", "Servië"))
    for n in ("Italië", "België", "Engeland", "Denemarken"):
        assert n in OG_RIJEN[0][1] and any(n in r[1] for r in ALS_EEN)
    for n in ("Frankrijk", "Spanje", "Portugal"):
        assert n in OG_RIJEN[1][1] and any(n in r[1] for r in ALS_TWEE)
    assert "1,47" in content3 and ODDS_WINNAAR[0][0] == "Spanje"
    print("NA DE LOTING:", NA_LOTING)
    print("dry run ok")
