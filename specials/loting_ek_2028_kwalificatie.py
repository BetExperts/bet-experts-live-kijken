# -*- coding: utf-8 -*-
"""Los artikel: loting EK 2028-kwalificatie (6-12-2026, Belfast), opzet, potindeling en mogelijke tegenstanders van Oranje, 9-11-2026.

Bronnen (geraadpleegd ma 9-11-2026):
- Loting zo 6 dec 2026, 17:00 GMT = 18:00 NL-tijd, ICC Belfast; 12 groepen van 4 of 5, thuis en uit, maart-november 2027,
  play-offs maart 2028: https://www.uefa.com/euro2028/news/029f-1f2ff991e87b-345fffcd69c3-1000/ (bijgewerkt 17-09-2026)
- EK 2028 basis (gastheren, 9 juni-9 juli 2028, 24 landen, 6 groepen, opening Cardiff, finale Wembley 9 juli 18:00 CEST,
  halve finales 4 en 5 juli Wembley, 51 duels, 9 stadions in 8 steden, aftraptijden 15/18/21 uur):
  https://www.uefa.com/euro2028/news/028f-1b599fe02d18-0c758142f5e4-1000/ en
  https://www.uefa.com/euro2028/news/029f-1f2f36424d97-2486810a0d57-1000/
- Kwalificatiesysteem (12 winnaars + 8 beste nummers 2 direct, 2 plekken voor gastlanden, play-offs 2-4 tickets, paden):
  https://www.uefa.com/news-media/news/0299-1dcf36ade17c-099c9d4b7d85-1000/ (21-05-2025, ExCo Bilbao)
- EK-reglement 2026-28: art. 13 (loting ná de league phase NL; plaatsing op de "interim overall 2026/27 UEFA Nations League
  rankings"; gastlanden + Noord-Ierland in aparte groepen; winnaars kwartfinales NL elk in een andere groep van vier; groep van vijf
  max. één verliezende kwartfinalist of één deelnemer aan de A/B- of B/C-play-offs), art. 14.04 (gastlandplekken), art. 16 (play-offs):
  https://documents.uefa.com/r/Regulations-of-the-UEFA-European-Football-Championship-2026-28-Online
- Tussenranglijst NL: reglement NL 2026/27 art. 19.01-19.02 (League A 1-16, B 17-32, C 33-48, D daarna; eerst groepspositie).
- Stand alle leagues na speeldag 4: UEFA standings-API (standings.uefa.com, competitionId 2014, seasonYear 2027), 9-11-2026.
- Odds EK 2028-winnaar 711 (Kambi sevelevnl, euro_2028), ma 9-11-2026 ±16:50.
- Precedent: loting EK 2024-kwalificatie geplaatst op de Nations League-ranglijst 2022/23 (UEFA).

Bewust NIET gebruikt of als verwachting geformuleerd: de exacte potindeling (UEFA publiceert de lotingsprocedure nog; wij gaan uit
van potten van 12 op volgorde van de tussenranglijst), de exacte speeldagen per groep in 2027 en de play-offdata in maart 2028 (alleen
'maart 2028' bevestigd), de definitieve lijst met verboden duels, capaciteiten van stadions, datum loting eindtoernooi.
  python3 specials/loting_ek_2028_kwalificatie.py   (dry run)"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

# Na de loting (6-12) bijwerken: groep en tegenstanders van Oranje, definitieve potten, speeldata; na 17-11 de potverwachting.
NA_LOTING = "bijwerken met de uitkomst van de loting: groep en tegenstanders van Oranje, definitieve potten en speeldata"

SLUG = "loting-ek-2028-kwalificatie-potindeling-oranje"
RUBRIEK = "66d6d655bc312d5c0e834ecd"   # Oranje/interlands
TITEL = "Loting EK 2028-kwalificatie: potindeling en Oranje"
SAMENVATTING = ("Op 6 december loot UEFA in Belfast de groepen voor het EK 2028. Zo werkt de kwalificatie, zo worden de potten "
                "bepaald en dit kan Oranje treffen.")

# deelkaart: og_kaarten/gsod.py
OG_LOGO = "nederland-logo.png"
OG_EYEBROW = "EK 2028 · Oranje"
OG_KOP = "Loting EK 2028<br><em>kwalificatie</em>"
OG_TEGELS = [("Loting", "6 dec"), ("Groepen", "12")]
OG_KOPJE = "Wat je moet weten"
OG_RECHTS = "Status"
OG_RIJEN = [("Belfast", "Zondag 6 december, 18:00 uur", "Loting"),
            ("Oranje", "Verwacht in pot 1", "Verwacht"),
            ("Direct", "12 groepswinnaars + 8 beste nummers 2", "20 tickets"),
            ("EK 2028", "9 juni – 9 juli 2028, 24 landen", "VK / IE")]

L = {"nlg": '<a href="/competities/uefa-nations-league">Nations League</a>',
     "opzet": '<a href="/nieuws/nations-league-nieuwe-opzet-2028-wat-betekent-het-voor-oranje">wat Oranje nodig heeft in de Nations League</a>',
     "uitleg": '<a href="/nieuws/hoe-werkt-de-nations-league-complete-uitleg-2026-2027">hoe de Nations League werkt</a>',
     "selectie": '<a href="/nieuws/selectie-oranje-november-2026-griekenland-duitsland">de selectie van Oranje</a>',
     "711": '<a href="/bookmakers/711">711</a>',
     "legaal": '<a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>'}
LANDSLUG = {"Nederland": "nederland", "Griekenland": "griekenland", "Duitsland": "duitsland", "Servië": "servie",
            "Engeland": "engeland", "Ierland": "ierland", "Schotland": "schotland", "Wales": "wales", "Noord-Ierland": "noord-ierland",
            "Zwitserland": "zwitserland", "Oostenrijk": "oostenrijk", "Zweden": "zweden", "Noorwegen": "noorwegen", "Turkije": "turkije",
            "Malta": "malta", "Gibraltar": "gibraltar", "Andorra": "andorra"}


def land(n):
    return f'<a href="/clubs/{LANDSLUG[n]}">{n}</a>'


LOTING_DATUM, LOTING_TIJD, LOTING_PLAATS = "zondag 6 december 2026", "18:00 uur", "het ICC in Belfast"
EK_DATA = "9 juni tot en met 9 juli 2028"
DEELNEMERS = 54          # alle UEFA-leden behalve het geschorste Rusland
GROEPEN = 12
GROEPEN_5 = DEELNEMERS - 4 * GROEPEN    # 6 groepen van vijf
GROEPEN_4 = GROEPEN - GROEPEN_5          # 6 groepen van vier
DIRECT = 12 + 8

EK = [("Gastlanden", "Engeland, Ierland, Schotland en Wales"),
      ("Wanneer", EK_DATA),
      ("Openingsduel", "Vrijdag 9 juni 2028 in Cardiff"),
      ("Halve finales", "4 en 5 juli 2028, Wembley"),
      ("Finale", "Zondag 9 juli 2028, 18:00 uur, Wembley (Londen)"),
      ("Deelnemers", "24 landen in zes groepen van vier"),
      ("Wedstrijden", "51 in negen stadions en acht steden")]

STADIONS = [("Londen", "Wembley Stadium"), ("Londen", "Tottenham Hotspur Stadium"),
            ("Cardiff", "National Stadium of Wales (Principality Stadium)"), ("Dublin", "Dublin Arena (Aviva Stadium)"),
            ("Glasgow", "Hampden Park"), ("Manchester", "Manchester City Stadium (Etihad Stadium)"),
            ("Liverpool", "Everton Stadium"), ("Newcastle", "St James' Park"), ("Birmingham", "Villa Park")]

ROUTES = [("Groepswinnaars", "12", "Direct naar het EK"),
          ("Beste nummers 2", "8", "Direct naar het EK"),
          ("Gastlanden die zich niet direct plaatsen", "2", "Gereserveerde plekken"),
          ("Play-offs (maart 2028)", "2 tot 4", "Overige nummers 2 en groepswinnaars van de Nations League")]

# verwachte potten: 12 per pot op volgorde van de tussenranglijst NL 2026/27 (stand 9-11-2026, UEFA)
POTTEN = [("Pot 1", "1 t/m 12", "Nummers 1, 2 en 3 van League A",
           "Nederland, Griekenland, Frankrijk, Italië, Spanje, Engeland, Portugal en vijf van België, Turkije, Duitsland, Servië, Kroatië, Tsjechië, Denemarken, Wales en Noorwegen"),
          ("Pot 2", "13 t/m 24", "Nummers 4 van League A, nummers 1 en 2 van League B",
           "De vier nummers 4 van League A, plus nu: Zwitserland, Slovenië, Noord-Ierland, Hongarije, Oostenrijk, Kosovo, Zweden, Bosnië-Herzegovina"),
          ("Pot 3", "25 t/m 36", "Nummers 3 en 4 van League B, groepswinnaars League C",
           "Nu onder meer Schotland, Ierland, Oekraïne, Polen, Noord-Macedonië, Albanië, Montenegro, Slowakije en IJsland"),
          ("Pot 4", "37 t/m 48", "Nummers 2, 3 en 4 van League C", "Nu onder meer Finland, Cyprus, Estland, Bulgarije en Armenië"),
          ("Pot 5", "49 t/m 54", "League D", "Malta, Gibraltar, Andorra, Azerbeidzjan, Litouwen en Liechtenstein")]

# 711 (Kambi), EK 2028-winnaar, ma 9-11-2026 ±16:50
ODDS_EK = [("Spanje", "4,75"), ("Frankrijk", "5,00"), ("Engeland", "5,50"), ("Portugal", "8,00"),
           ("Duitsland", "10,00"), ("Nederland", "13,00")]

content = f"""<p><strong>De loting voor de kwalificatie van het EK 2028 is op {LOTING_DATUM} om {LOTING_TIJD} Nederlandse tijd in {LOTING_PLAATS}. UEFA verdeelt dan {DEELNEMERS} landen over {GROEPEN} groepen van vier of vijf. De kwalificatie loopt van maart tot en met november 2027. Nederland is nog niet geplaatst voor het EK 2028 en moet zich, net als de gastlanden, via de kwalificatie plaatsen. De potten worden bepaald door de tussenstand van de {L['nlg']} 2026/27. Oranje zit naar verwachting in pot 1.</strong></p>
<p>Het EK 2028 wordt van {EK_DATA} gespeeld in Engeland, Ierland, Schotland en Wales. Er doen 24 landen mee. In dit artikel lees je hoe de kwalificatie werkt, hoe de potten worden bepaald, in welke pot Oranje waarschijnlijk zit en welke landen Oranje kan treffen.</p>
<h3><strong>Het EK 2028 in het kort</strong></h3>
{tabel(["", "EK 2028"], [(f"<strong>{a}</strong>", b) for a, b in EK])}
<p>Er doen 24 landen mee, verdeeld over zes groepen van vier. De nummers 1 en 2 van elke groep en de vier beste nummers 3 gaan door naar de achtste finales. Daarna volgt een knock-outfase. De wedstrijden beginnen om 15:00, 18:00 of 21:00 uur Nederlandse tijd.</p>
<p><strong>De stadions.</strong> Er wordt gespeeld in negen stadions, verdeeld over acht steden. Londen heeft er twee.</p>
{tabel(["Stad", "Stadion"], STADIONS)}
<p>Noord-Ierland zat in het oorspronkelijke bod, maar er worden geen EK-duels gespeeld. Het geplande stadion in Belfast, Casement Park, zou niet op tijd klaar zijn. Wel is Belfast de stad van de kwalificatieloting.</p>
<h3><strong>Plaatsen de gastlanden zich automatisch?</strong></h3>
<p>Nee. {land('Engeland')}, {land('Ierland')}, {land('Schotland')} en {land('Wales')} spelen gewoon mee in de kwalificatie. Ze worden elk in een andere groep geloot. Wel heeft UEFA twee plekken op het EK gereserveerd voor gastlanden die zich niet direct plaatsen, ook als ze via de play-offs zouden moeten. Vallen er meer dan twee gastlanden buiten de directe plaatsing, dan gaan die twee plekken naar de twee best gerangschikte gastlanden. Worden de gereserveerde plekken niet allemaal gebruikt, dan gaan ze naar de play-offs.</p>"""

content2 = f"""<h3><strong>Wanneer en waar is de loting?</strong></h3>
<p>De loting is op <strong>{LOTING_DATUM}</strong> om <strong>{LOTING_TIJD}</strong> (17:00 uur lokale tijd) in het International Convention Centre (ICC) in Belfast. Dat is drie weken na de laatste groepsduels in de Nations League, die op 17 november eindigen. Pas dan staat de ranglijst vast waarmee UEFA de potten maakt.</p>
<h3><strong>Zo werkt de kwalificatie voor het EK 2028</strong></h3>
<p>Alle {DEELNEMERS} landen (alle UEFA-leden behalve het geschorste Rusland) worden verdeeld over {GROEPEN} groepen van vier of vijf landen. Met {DEELNEMERS} deelnemers worden dat {GROEPEN_5} groepen van vijf en {GROEPEN_4} van vier. Elk land speelt thuis en uit tegen alle groepsgenoten. De groepsfase loopt van maart tot en met november 2027.</p>
{tabel(["Route naar het EK", "Plekken", "Toelichting"], [(f"<strong>{a}</strong>", b, c) for a, b, c in ROUTES])}
<p>Er gaan dus {DIRECT} landen direct naar het EK. De nummers 2 worden onderling vergeleken via een ranglijst. De overige nummers 2 gaan naar de play-offs in maart 2028, samen met groepswinnaars uit League A, B en C van de Nations League 2026/27 die zich nog niet geplaatst hebben. Hoeveel tickets de play-offs opleveren, hangt af van de gastlanden. Gebruiken twee gastlanden een gereserveerde plek, dan zijn er nog twee play-offtickets. Bij één gastland zijn het er drie, en als geen gastland een gereserveerde plek nodig heeft, vier.</p>
<h3><strong>Hoe worden de potten bepaald?</strong></h3>
<p>Volgens het EK-reglement worden de landen geplaatst op basis van de tussenranglijst van de Nations League 2026/27. Die ranglijst komt er direct na de groepsfase, op 17 november. De volgorde is eenvoudig: eerst de landen uit League A (plek 1 tot en met 16), dan League B (17 tot en met 32), dan League C (33 tot en met 48) en daarna League D. Binnen een league telt eerst de positie in de groep, daarna onder meer punten en doelsaldo. Bij de kwalificatie voor het EK 2024 gebruikte UEFA ook al de Nations League-ranglijst.</p>
<p>UEFA heeft de exacte lotingsprocedure nog niet gepubliceerd. Bij {GROEPEN} groepen ligt een pot van twaalf landen voor de hand: één land per groep. Dan ziet de indeling er volgens de stand van maandag 9 november zo uit:</p>
{tabel(["Pot", "Plek op ranglijst", "Wie", "Verwachting (stand 9 november)"], [(f"<strong>{a}</strong>", b, c, d) for a, b, c, d in POTTEN])}
<p>Daarnaast gelden extra regels bij de loting:</p>
<ul><li>De vier gastlanden en Noord-Ierland komen elk in een andere groep.</li><li>De winnaars van de vier kwartfinales van de Nations League komen elk in een andere groep van vier. Bij de loting staat er per kwartfinale een plaatshouder, omdat die duels pas in maart 2027 worden gespeeld.</li><li>In een groep van vijf zit hooguit één verliezende kwartfinalist of één land dat in maart een A/B- of B/C-play-off speelt.</li><li>Zoals bij eerdere lotingen houdt UEFA rekening met politiek gevoelige duels, zoals Kosovo – Servië en Gibraltar – Spanje.</li></ul>"""

content3 = f"""<h3><strong>In welke pot zit Oranje?</strong></h3>
<p>Naar verwachting in pot 1. {land('Nederland')} staat na vier duels bovenaan in groep A2 met 8 punten, evenveel als {land('Griekenland')}. {land('Duitsland')} heeft 5 punten, {land('Servië')} 0. Omdat Servië hooguit nog op 6 punten kan komen, wordt Oranje in het slechtste geval derde. Een groepswinnaar uit League A staat op plek 1 tot en met 4 van de ranglijst, een nummer 2 op plek 5 tot en met 8 en een nummer 3 op plek 9 tot en met 12. Bij potten van twaalf landen zit Oranje dus in alle gevallen in pot 1. Het rekenwerk voor 13 en 16 november lees je in ons artikel over {L['opzet']}.</p>
<p>De uitslagen in november bepalen wel de groepsgrootte. Haalt Oranje de kwartfinale van de Nations League en wint het die in maart, dan speelt het in een groep van vier. Verliest Oranje de kwartfinale, dan kan het in een groep van vijf terechtkomen. Hoe UEFA dat precies uitvoert, staat in de lotingsprocedure die nog moet verschijnen.</p>
<h3><strong>Mogelijke tegenstanders van Oranje</strong></h3>
<p>Als Oranje in pot 1 zit, kan het niet loten tegen andere landen uit pot 1, zoals Spanje, Frankrijk, Engeland en Portugal. Ook Griekenland en Duitsland (als die niet laatste wordt) zitten dan in pot 1. Uit elke andere pot komt één tegenstander. In een groep van vier zijn dat landen uit pot 2, 3 en 4. In een groep van vijf komt daar naar verwachting een land uit pot 5 bij.</p>
<p><strong>Pot 2:</strong> uit deze pot komt de sterkste tegenstander. Hier zitten de vier nummers 4 van League A, op dit moment {land('Turkije')}, Servië, Tsjechië en {land('Noorwegen')}. Daarnaast nu onder meer {land('Zwitserland')}, {land('Oostenrijk')}, {land('Zweden')} en {land('Noord-Ierland')} uit League B. Noorwegen en Turkije kunnen in de laatste speelronden nog uit de laatste plaats wegkomen, en dan schuift een ander land naar pot 2.</p>
<p><strong>Pot 3 en 4:</strong> de gastlanden Schotland en Ierland staan nu derde in hun groep in League B. Blijft dat zo, dan zitten ze in pot 3. Ierland kan met een tweede plek nog naar pot 2. Wales staat in League A derde en zit dan in pot 1; wordt Wales vierde, dan schuift het naar pot 2. In pot 4 zitten landen uit League C, zoals Finland, Cyprus en Estland.</p>
<p><strong>Pot 5:</strong> de zes landen uit League D: {land('Malta')}, {land('Gibraltar')}, {land('Andorra')}, Azerbeidzjan, Litouwen en Liechtenstein. Komt Oranje in een groep van vijf, dan is een van hen naar verwachting de vijfde tegenstander.</p>
<h3><strong>Waarom de Nations League telt voor het EK</strong></h3>
<p>De Nations League bepaalt niet alleen de potten. De competitie biedt ook een vangnet. Groepswinnaars uit League A, B en C die zich niet via de kwalificatie plaatsen, kunnen via de ranglijst alsnog een plek in de play-offs van maart 2028 krijgen. Een groepswinnaar van League A staat daarbij vooraan. Groepswinst in A2 is voor Oranje dus ook een soort verzekering voor het EK. Wil je eerst de basis weten, lees dan {L['uitleg']}.</p>
<h3><strong>Oranje op het EK en de bookmakers</strong></h3>
<p>Oranje werd in 1988 Europees kampioen. Op het laatste EK, in 2024, verloor het in Dortmund met 2-1 van Engeland in de halve finale. Bondscoach Xavi Hernández leidt Oranje nu in de Nations League. Lees ook over {L['selectie']}.</p>
<p>Bij {L['711']} is Spanje favoriet voor de Europese titel in 2028. Oranje staat zesde (maandag 9 november).</p>
{tabel(["Land", "Quotering EK-winnaar"], [(f"<strong>{n}</strong>" if n == "Nederland" else n, o) for n, o in ODDS_EK])}
<p>Wed alleen bij een bookmaker met een vergunning van de Kansspelautoriteit; lees {L['legaal']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wanneer is de loting voor de EK 2028-kwalificatie?</strong><br>Op {LOTING_DATUM} om {LOTING_TIJD} Nederlandse tijd in Belfast. Dan worden de {GROEPEN} kwalificatiegroepen geloot.</p>
<p><strong>Doet Nederland mee aan het EK 2028?</strong><br>Dat is nog niet zeker. Oranje moet zich plaatsen via de kwalificatie, die van maart tot en met november 2027 loopt. De groepswinnaars en de acht beste nummers 2 gaan direct naar het EK. De overige nummers 2 en een aantal groepswinnaars uit de Nations League krijgen nog een kans in de play-offs van maart 2028.</p>
<p><strong>Hoeveel landen doen mee aan het EK 2028?</strong><br>Er doen 24 landen mee. Aan de kwalificatie nemen {DEELNEMERS} landen deel.</p>
<p><strong>Wie is het gastland van het EK 2028?</strong><br>Het EK wordt georganiseerd door Engeland, Ierland, Schotland en Wales. Zij plaatsen zich niet automatisch, maar er zijn twee plekken gereserveerd voor gastlanden die zich niet direct plaatsen.</p>
<p><strong>Wanneer wordt het EK 2028 gespeeld?</strong><br>Van {EK_DATA}. De openingswedstrijd is in Cardiff, de finale op 9 juli op Wembley in Londen.</p>
<p><strong>In welke pot zit Oranje bij de loting?</strong><br>Naar verwachting in pot 1. De potten zijn gebaseerd op de tussenranglijst van de Nations League, en Oranje eindigt in groep A2 minimaal als derde. UEFA moet de lotingsprocedure nog publiceren.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    alles = content + content2 + content3
    w = len(re.sub(r"<[^>]+>", " ", alles).split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", w, "woorden")
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert 900 <= w <= 2000, w
    assert "<h2" not in alles and "<h4" not in alles and "betcity" not in alles.lower() and "/go/" not in alles
    for slecht in ("opstellingvandaag", "footymetrics", "espn", "wikipedia", "waaroptv"):
        assert slecht not in alles.lower(), slecht
    assert content.startswith("<p><strong>") and content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    assert 4 <= content3.split("Veelgestelde vragen")[1].count("?</strong><br>") <= 6
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/") and not href.startswith("//"), href
    # getallen intern consistent
    assert GROEPEN_5 * 5 + GROEPEN_4 * 4 == DEELNEMERS and GROEPEN_5 + GROEPEN_4 == GROEPEN == 12
    assert DIRECT + 2 + 2 == 24 == DIRECT + 4          # 20 direct + 2 gastland + 2 play-off = 20 + 4 play-off zonder gastlanden
    assert 12 * 4 + 6 == DEELNEMERS                     # potten van 12 + pot 5 (League D) met 6 landen
    assert len(STADIONS) == 9 and len({s for s, _ in STADIONS}) == 8
    assert alles.count(LOTING_DATUM) >= 3 and alles.count(LOTING_TIJD) >= 3 and alles.count(EK_DATA) >= 3
    assert "6 dec" in OG_TEGELS[0][1] and LOTING_DATUM.endswith("6 december 2026") and "18:00" in OG_RIJEN[0][1]
    assert "pot 1" in content and "pot 1" in content3.split("Veelgestelde vragen")[1]
    oranje = (8, 0, 6)                                  # Oranje, Servië, max extra Servië: Oranje kan niet meer vierde worden
    assert oranje[1] + oranje[2] < oranje[0]
    assert ODDS_EK[5][0] == "Nederland" and "zesde" in content3
    print("NA DE LOTING:", NA_LOTING)
    print("dry run ok")
