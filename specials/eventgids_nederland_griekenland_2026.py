# -*- coding: utf-8 -*-
"""Eventgids: Nederland – Griekenland, Nations League groep A2, vrijdag 13 november 2026 (geschreven 9-11-2026).

Bronnen:
- Basisfeiten (stand, programma, tiebreaks, selectie): specials/nations_league_2028_feiten.md
  (UEFA speelschema 09-11-2026, UEFA-reglement art. 15, OnsOranje, NOS, DFB).
- Datum, aftrap 20.45 en stadion: UEFA, OnsOranje (selectie 06-11-2026:
  https://www.onsoranje.nl/nieuws/nederlands-elftal-mannen/82811/oranje-met-25-spelers-naar-slotduels-groepsfase-nations-league).
- Tv: NOS (NPO 3, stream en liveblog op NOS.nl/NOS-app), via de feitenbrief; eigen zenderconfig data/tv_zenders.json
  (NOS = Nederlands elftal). Bet365-streamingschema: status "nee" voor dit duel -> geen stream beloofd.
- Selectie (25 spelers, incl. Summerville en Kluivert): OnsOranje 06-11-2026 + NOS.
- Opstellingen, wissels en doelpunten van de vier vorige duels (24-09, 27-09, 01-10, 04-10-2026) en van Griekenland
  (Servië – Griekenland 1-2, Duitsland – Griekenland 0-1, Griekenland – Duitsland 0-0): API-Football
  (fixtures 1528862, 1528896, 1528918, 1528940, 1528863, 1528899, 1528939); gecontroleerd met het DFB-verslag van
  24-09 (https://www.dfb.de/news/first-germany-game-under-klopp-ends-in-draw) en Flashscore/NOS-berichten over 01-10
  (Tzolis met hamstringklacht naar de kant, Reijnders 89', Gravenberch en Reijnders eerst op de bank).
- Onderlinge historie (12 duels: 9 zeges, 2 gelijk, 1 nederlaag): 11v11-overzicht (9-1-1 tot en met 2023) + 2-2 van
  01-10-2026; EK 1980 1-0 en de 1-2 van 01-09-2016 in Eindhoven (NOS: https://nos.nl/artikel/2129484); EK-kwalificatie
  2023 3-0 en 0-1 (API-Football).
- Kaarten: OnsOranje verwijst naar de officiële ticketshop tickets.knvb.nl; NOS meldde eerder dat de KNVB doorverkochte
  tickets blokkeerde (https://nos.nl/l/2523103).
- Odds: 711 (Kambi sevelevnl), afgelezen maandag 9 november 2026 rond 16.45 uur: 1,47 / 4,90 / 7,00; meer dan 2,5
  doelpunten 1,53; beide teams scoren ja 1,68.

Bewust NIET gebruikt (onbevestigd):
- of de wedstrijd uitverkocht is (alleen doorverkoopsites melden dat; geen KNVB- of ArenA-bericht gevonden);
- een Belgische of Griekse uitzender (niets bevestigd gevonden);
- de Griekse selectie voor november (niet gevonden; UEFA-teampagina is niet gedateerd) en de fitheid van Tzolis;
- de capaciteit van de ArenA, de scheidsrechter en de begintijd van de NOS-uitzending;
- spelersmarkten van 711 (noemen spelers die mogelijk niet meedoen).

  python3 specials/eventgids_nederland_griekenland_2026.py   (dry run)
  kaart: cd live-kijken-agent && PYTHONPATH=specials ../superodd-agent/.venv/bin/python og_kaarten/gsod.py eventgids_nederland_griekenland_2026
"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "nederland-griekenland-hoe-laat-tv-stadion-opstelling-13-november-2026"
RUBRIEK = "66d6d655bc312d5c0e834ecd"   # Oranje/interlands
TITEL = "Nederland – Griekenland: hoe laat, tv, stadion en opstelling"
SAMENVATTING = ("Nederland – Griekenland is vrijdag 13 november om 20.45 uur in de Johan Cruijff ArenA, live op NPO 3. "
                "Tv, kaarten, inzet en opstelling.")

# deelkaart: og_kaarten/gsod.py
OG_LOGO = "vlaggen-nl-gr.png"
OG_EYEBROW = "Nations League · Groep A2"
OG_KOP = "Oranje – Griekenland<br><em>vrijdag 13 november</em>"
OG_TEGELS = [("Aftrap", "20:45"), ("Tv", "NPO 3")]
OG_KOPJE = "Alles over het koploperduel"
OG_RECHTS = "Info"
OG_RIJEN = [("Aftrap", "Vrijdag 13 november 2026", "20:45"),
            ("Tv", "NPO 3, stream via NOS.nl en NOS-app", "Live"),
            ("Stadion", "Johan Cruijff ArenA, Amsterdam", "Thuis"),
            ("Inzet", "Koploperduel: beide landen op 8 punten", "Groep A2")]

# NA DE WEDSTRIJD: uitslag + gevolgen toevoegen

L = {"nlg": '<a href="/competities/uefa-nations-league">Nations League</a>',
     "rekenwerk": '<a href="/nieuws/nations-league-nieuwe-opzet-2028-wat-betekent-het-voor-oranje">wat Oranje nodig heeft in de Nations League</a>',
     "selectie": '<a href="/nieuws/selectie-oranje-november-2026-griekenland-duitsland">de volledige selectie van Oranje</a>',
     "uitleg": '<a href="/nieuws/hoe-werkt-de-nations-league-complete-uitleg-2026-2027">hoe de Nations League werkt</a>',
     "xavi": '<a href="/nieuws/salaris-xavi-hernandez-bondscoach-oranje">bondscoach Xavi Hernández</a>',
     "nl": '<a href="/clubs/nederland">Nederland</a>',
     "gr": '<a href="/clubs/griekenland">Griekenland</a>',
     "de": '<a href="/clubs/duitsland">Duitsland</a>',
     "rs": '<a href="/clubs/servie">Servië</a>',
     "711": '<a href="/bookmakers/711">711</a>',
     "legaal": '<a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>',
     "live": '<a href="/live-kijken">live kijken</a>',
     "opst": '<a href="/opstellingen">opstellingen</a>',
     "vb": '<a href="/voorbeschouwingen">voorbeschouwingen</a>'}

AFTRAP = "20:45"
DATUM = "vrijdag 13 november 2026"

SNEL = [("<strong>Wedstrijd</strong>", "Nederland – Griekenland"),
        ("<strong>Competitie</strong>", "Nations League, League A, groep A2, speelronde 5"),
        ("<strong>Datum</strong>", "Vrijdag 13 november 2026"),
        ("<strong>Aftrap</strong>", AFTRAP),
        ("<strong>Stadion</strong>", "Johan Cruijff ArenA, Amsterdam"),
        ("<strong>Tv</strong>", "NPO 3"),
        ("<strong>Stream</strong>", "NOS.nl en de NOS-app")]

STAND = [("1", "Nederland", "4", "2-2-0", "7-5", "+2", "<strong>8</strong>"),
         ("2", "Griekenland", "4", "2-2-0", "5-3", "+2", "<strong>8</strong>"),
         ("3", "Duitsland", "4", "1-2-1", "3-2", "+1", "<strong>5</strong>"),
         ("4", "Servië", "4", "0-0-4", "3-8", "-5", "<strong>0</strong>")]

SCENARIO = [
    ("Winst", "Winst of gelijk", "14 of 12", "<strong>Groepswinst</strong>"),
    ("Winst", "Verlies", "11", "Kwartfinale; alleen bij een driekamp op 11 punten beslist het onderlinge doelsaldo"),
    ("Gelijk", "Winst of gelijk", "12 of 10", "<strong>Kwartfinale zeker</strong>"),
    ("Gelijk", "Verlies", "9", "Kwartfinale als Duitsland in Servië verliest; wint Duitsland daar, dan moet Griekenland van Servië verliezen en beslist het doelsaldo"),
    ("Verlies", "Winst", "11", "<strong>Kwartfinale zeker</strong>, als nummer 2"),
    ("Verlies", "Gelijk", "9", "Nummer 2 als Duitsland niet wint in Servië; anders beslist het doelsaldo"),
    ("Verlies", "Verlies", "8", "Derde plaats, geen kwartfinale"),
]

BASIS = [("Bart Verbruggen", "Doel", "4"), ("Denzel Dumfries", "Rechtsback", "4"),
         ("Virgil van Dijk", "Centrale verdediger", "4"), ("Micky van de Ven", "Linksback", "4"),
         ("Crysencio Summerville", "Rechtsbuiten", "4"), ("Tijjani Reijnders", "Middenveld", "3"),
         ("Joey Veerman", "Middenveld", "3"), ("Mexx Meerdink", "Spits", "3"),
         ("Jan Paul van Hecke", "Centrale verdediger", "2"), ("Cody Gakpo", "Linksbuiten", "2")]

DUEL1 = [("Doelpunten Griekenland", "Fotis Ioannidis (23'), Giorgos Masouras (45+')"),
         ("Doelpunten Oranje", "Virgil van Dijk (59'), Tijjani Reijnders (89')"),
         ("Wissels bij rust", "Reijnders, Gravenberch en Lang voor Til, Q. Timber en Van Bommel"),
         ("Opvallend", "Christos Tzolis na 18 minuten geblesseerd naar de kant")]

H2H = [("1 okt 2026", "Griekenland – Nederland", "2-2", "Nations League"),
       ("16 okt 2023", "Griekenland – Nederland", "0-1", "EK-kwalificatie"),
       ("7 sep 2023", "Nederland – Griekenland", "3-0", "EK-kwalificatie"),
       ("1 sep 2016", "Nederland – Griekenland", "1-2", "Oefenduel")]

GRIEKS = [("24 sep", "Servië – Griekenland", "1-2", "Tzolis, Douvikas"),
          ("27 sep", "Duitsland – Griekenland", "0-1", "Kourbelis"),
          ("1 okt", "Griekenland – Nederland", "2-2", "Ioannidis, Masouras"),
          ("4 okt", "Griekenland – Duitsland", "0-0", "")]

ODDS = [("Nederland wint", "1,47"), ("Gelijkspel", "4,90"), ("Griekenland wint", "7,00"),
        ("Meer dan 2,5 doelpunten", "1,53"), ("Beide teams scoren: ja", "1,68")]

content = f"""<p><strong>{L['nl']} – {L['gr']} begint op {DATUM} om 20.45 uur in de Johan Cruijff ArenA in Amsterdam. De NOS zendt de wedstrijd live uit op NPO 3, met een livestream op NOS.nl en in de NOS-app. Het is het vijfde groepsduel van Oranje in de {L['nlg']} en meteen een kraker: beide landen staan na vier wedstrijden op 8 punten bovenaan groep A2.</strong></p>
<p>Wie wint, zet een grote stap richting groepswinst. Hieronder lees je hoe laat de wedstrijd begint, waar je kijkt, wat je moet weten over kaarten en het stadion, wat er op het spel staat en hoe Oranje vermoedelijk begint. Ook blikken we terug op de 2-2 in Thessaloniki en kijken we naar de vorm van Griekenland en de odds.</p>
<h3><strong>Nederland – Griekenland in het kort</strong></h3>
{tabel(["", ""], SNEL)}
<h3><strong>Hoe laat begint Nederland – Griekenland?</strong></h3>
<p>De aftrap is om <strong>20.45 uur</strong> Nederlandse tijd, op vrijdag 13 november. Dat is ook de tijd die UEFA en de KNVB noemen. In sommige programmaoverzichten staat het duel op donderdag 12 november, maar dat klopt niet: Oranje speelt op vrijdag. Op dezelfde avond, ook om 20.45 uur, speelt {L['de']} in Belgrado tegen {L['rs']}. Die uitslag telt voor Oranje net zo goed mee.</p>
<h3><strong>Op welke zender is Nederland – Griekenland te zien?</strong></h3>
<p>De NOS heeft de rechten op de wedstrijden van het Nederlands elftal. Je kijkt Nederland – Griekenland dus gratis op <strong>NPO 3</strong>. Online volg je de wedstrijd via de livestream op NOS.nl en in de NOS-app, waar ook een liveblog meeloopt. Je hebt geen abonnement nodig. Een overzicht van alle wedstrijden die je deze week {L['live']} kunt, vind je op onze site.</p>
<h3><strong>Stadion en kaarten</strong></h3>
<p>Oranje speelt in de Johan Cruijff ArenA, dezelfde plek waar het in september met 1-1 gelijkspeelde tegen Duitsland. Kaarten verkoopt de KNVB via de officiële ticketshop op tickets.knvb.nl. Of de wedstrijd helemaal uitverkocht is, had de KNVB bij het schrijven van dit artikel niet gemeld. Sommige doorverkoopsites zeggen van wel, maar die bieden vaak kaarten aan boven de officiële prijs. De KNVB heeft eerder doorverkochte tickets geblokkeerd. Koop daarom alleen via de officiële kanalen, dan weet je zeker dat je naar binnen kunt.</p>"""

content2 = f"""<h3><strong>Wat staat er op het spel?</strong></h3>
<p>Na vier speelronden is groep A2 een tweestrijd aan de top. Oranje staat eerste op meer gemaakte doelpunten, Griekenland heeft precies evenveel punten en hetzelfde doelsaldo.</p>
{tabel(["#", "Land", "G", "W-G-V", "Doelpunten", "Saldo", "Punten"], STAND)}
<p>Bij gelijke punten telt eerst het onderlinge resultaat. De eerste ontmoeting eindigde in 2-2, dus deze wedstrijd beslist wie dat onderlinge duel wint. Oranje kan niet meer laatste worden, want Servië komt hooguit op 6 punten. De nummers 1 en 2 gaan in maart 2027 naar de kwartfinales.</p>
{tabel(["Tegen Griekenland", "In Berlijn", "Punten", "Uitkomst voor Oranje"], SCENARIO)}
<p>Voor Griekenland is het simpel: wint het in Amsterdam, dan is het zeker groepswinnaar. Ook voor Oranje is een zege goud waard, want daarna is één punt in Berlijn genoeg voor de eerste plaats. Alle rekensommen, ook voor een derde plek en de nieuwe opzet vanaf 2028, lees je in ons artikel over {L['rekenwerk']}. Nieuw met de Nations League? Lees eerst {L['uitleg']}.</p>
<h3><strong>De selectie van Oranje</strong></h3>
<p>{L['xavi']} riep op vrijdag 6 november 25 spelers op. Frenkie de Jong is terug na zijn knieblessure. Ook Ian Maatsen, Donyell Malen en Justin Kluivert zijn erbij. Ryan Gravenberch (hiel), Jorrel Hato, Nathan Aké en Jeremie Frimpong zijn niet fit. Kenneth Taylor en Joshua Zirkzee, die in oktober nog scoorde tegen Servië, zijn niet geselecteerd. Alle namen en clubs staan in {L['selectie']}.</p>
<h3><strong>Verwachte opstelling van Oranje</strong></h3>
<p>De officiële opstelling komt ongeveer een uur voor de aftrap naar buiten. Tot die tijd is alles een inschatting. Wij baseren die op de vier vorige duels onder Xavi en op de selectie. Deze spelers stonden het vaakst in de basis:</p>
{tabel(["Speler", "Positie", "Basisplaatsen (van 4)"], BASIS)}
<p><strong>Onze verwachting:</strong> Verbruggen; Dumfries, Van Hecke, Van Dijk, Van de Ven; Veerman, Reijnders, Frenkie de Jong; Summerville, Meerdink, Gakpo. Dat is een verwachting, geen zekerheid. Xavi wisselde in vier wedstrijden flink: in Thessaloniki zaten Reijnders en Gravenberch eerst op de bank, tegen Servië stond Teun Koopmeiners centraal achterin. Twijfelgevallen zijn er genoeg. Het is de vraag of De Jong na zijn blessure meteen negentig minuten kan spelen; anders ligt Quinten Timber of Koopmeiners voor de hand. Voorin zijn Brian Brobbey, Malen en Noa Lang de alternatieven, en Jurriën Timber kan rechts of centraal in de verdediging spelen. Gakpo ging in september in Belgrado al na een kwartier geblesseerd van het veld en miste daarna de duels met Griekenland en Servië, maar zit weer bij de selectie.</p>
<p>Zodra de opstellingen officieel zijn, werken we dit artikel bij. Je vindt ze dan ook op onze pagina met {L['opst']}.</p>
<h3><strong>De eerste ontmoeting: 2-2 in Thessaloniki</strong></h3>
<p>Op 1 oktober speelde Oranje in Thessaloniki een slechte eerste helft. Griekenland leidde bij rust met 2-0 en had zelfs vroeg al een treffer van Tzolis afgekeurd zien worden wegens buitenspel. Xavi greep in de rust in met drie wissels en dat werkte. Van Dijk kopte na een uur een hoekschop van Veerman binnen, Reijnders maakte in de 89e minuut de gelijkmaker. Ook Dumfries zag twee doelpunten afgekeurd worden. Xavi nam na afloop de schuld van de eerste helft op zich.</p>
{tabel(["", "Griekenland – Nederland 2-2"], DUEL1)}"""

content3 = f"""<h3><strong>Onderlinge historie</strong></h3>
<p>Oranje speelde twaalf keer tegen Griekenland: negen zeges, twee gelijke spelen en één nederlaag. Op het EK van 1980 won Nederland met 1-0. De enige Griekse zege dateert van 1 september 2016: in een oefenduel in Eindhoven won Griekenland met 1-2, na een vroege goal van Georginio Wijnaldum. In de kwalificatie voor het EK 2024 won Oranje twee keer: 3-0 in Eindhoven en 0-1 in Athene, met een late strafschop van Van Dijk.</p>
<p>De laatste vier ontmoetingen:</p>
{tabel(["Datum", "Wedstrijd", "Uitslag", "Soort duel"], H2H)}
<h3><strong>Vorm en sleutelspelers van Griekenland</strong></h3>
<p>Griekenland, onder leiding van de Servische bondscoach Ivan Jovanović, is nog ongeslagen in deze Nations League. Het won in Belgrado en in Augsburg, en speelde in Thessaloniki gelijk tegen Oranje en Duitsland. Griekenland kreeg in vier duels maar 3 tegendoelpunten; alleen Duitsland (2) kreeg er minder.</p>
{tabel(["Datum", "Wedstrijd", "Uitslag", "Griekse doelpunten"], GRIEKS)}
<p>De Grieken laten de bal graag aan de tegenstander. Tegen Duitsland hadden ze in beide duels maar een kwart tot een derde van het balbezit, en toch pakten ze vier punten. In Augsburg was één doelpunt van middenvelder Dimitris Kourbelis genoeg. Jovanović speelde in alle vier de duels met twee spitsen.</p>
<p><strong>Op deze spelers moet Oranje letten:</strong></p>
<ul><li><strong>Vangelis Pavlidis</strong>: de spits stond in alle vier de duels in de basis en gaf de assist bij de Griekse gelijkmaker in Belgrado.</li><li><strong>Fotis Ioannidis</strong>: maakte de 1-0 tegen Oranje en gaf de assist bij de 2-0.</li><li><strong>Christos Tzolis</strong>: de vleugelaanvaller scoorde in Belgrado, maar ging tegen Oranje na 18 minuten geblesseerd naar de kant en miste daarna het duel met Duitsland. Of hij fit is, is onzeker.</li><li><strong>Kostas Tsimikas</strong>: de linksback is de ervaren kracht achterin en gaf de assist bij de winnende goal in Belgrado.</li><li><strong>Konstantinos Karetsas</strong>: het 18-jarige talent begon drie van de vier duels op het middenveld.</li></ul>
<p>De Griekse selectie voor deze interlandperiode was bij het schrijven nog niet door ons te bevestigen. Wie er precies bij is, lees je in onze {L['vb']} op de wedstrijddag.</p>
<h3><strong>Odds en voorspelling Nederland – Griekenland</strong></h3>
<p>Bij {L['711']} is Oranje duidelijk favoriet. Dit zijn de odds zoals wij ze op maandag 9 november hebben afgelezen:</p>
{tabel(["Markt", "Odd bij 711"], ODDS)}
<p>Omgerekend geeft de bookmaker Oranje ongeveer 66 procent kans op winst, een gelijkspel zo'n 20 procent en Griekenland 14 procent. <strong>Onze verwachting:</strong> Oranje heeft thuis meer kwaliteit en meer aanvallende opties, maar Griekenland is lastig te bespelen en laat weinig toe. Wij rekenen op een Nederlandse zege, maar niet op een makkelijke avond. Odds veranderen tot aan de aftrap, dus check ze vlak voor de wedstrijd opnieuw. Wed alleen bij een bookmaker met een vergunning van de Kansspelautoriteit; lees {L['legaal']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Nederland – Griekenland?</strong><br>De aftrap is op vrijdag 13 november 2026 om 20.45 uur in de Johan Cruijff ArenA in Amsterdam.</p>
<p><strong>Op welke zender is Nederland – Griekenland?</strong><br>Op NPO 3. De NOS zendt de wedstrijd live uit en heeft ook een gratis livestream op NOS.nl en in de NOS-app.</p>
<p><strong>Is Nederland – Griekenland uitverkocht?</strong><br>Dat had de KNVB bij het schrijven niet gemeld. Kaarten koop je alleen via de officiële KNVB-ticketshop op tickets.knvb.nl; doorverkochte kaarten kunnen worden geblokkeerd.</p>
<p><strong>Wat is de opstelling van Oranje tegen Griekenland?</strong><br>De officiële opstelling komt ongeveer een uur voor de aftrap. Onze verwachting is Verbruggen; Dumfries, Van Hecke, Van Dijk, Van de Ven; Veerman, Reijnders, Frenkie de Jong; Summerville, Meerdink, Gakpo.</p>
<p><strong>Wat is de uitslag van de eerste wedstrijd tegen Griekenland?</strong><br>Op 1 oktober 2026 eindigde Griekenland – Nederland in Thessaloniki in 2-2. Oranje kwam terug van 2-0 achter via Van Dijk en Reijnders.</p>
<p><strong>Wanneer speelt Oranje hierna?</strong><br>Op maandag 16 november om 20.45 uur tegen Duitsland in het Olympiastadion in Berlijn, ook live op NPO 3.</p>
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
    for verboden in ("opstellingvandaag", "footymetrics", "espn", "wikipedia", "waaroptv"):
        assert verboden not in alles.lower(), verboden
    assert content.startswith("<p><strong>") and content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    # tijden: alleen 20.45 / 20:45 (aftrap) in tekst, tabel, FAQ en kaart
    assert set(re.findall(r"\b\d{2}[.:]\d{2}\b", alles + str(OG_RIJEN) + str(OG_TEGELS))) <= {"20.45", "20:45"}
    assert "20.45 uur" in content and AFTRAP in content and "om 20.45 uur in de Johan Cruijff ArenA" in content3
    # stand en scenario's
    pt = {"NED": 8, "GRE": 8, "GER": 5, "SRB": 0}
    assert pt["SRB"] + 6 < pt["NED"]                      # Oranje kan niet meer laatste worden
    assert 8 + 1 + 1 > pt["GER"] + 3 + 1   # twee keer gelijk (10) > max Duitsland zonder winst op NL (9)
    assert sum(int(r[2]) for r in BASIS[:5]) == 20 and len(BASIS) == 10
    # onderlinge historie: 12 duels, 9-2-1
    assert 9 + 2 + 1 == 12
    # odds-consistentie (kans afgeleid uit 1,47 / 4,90 / 7,00)
    inv = [1 / 1.47, 1 / 4.90, 1 / 7.00]
    kans = [round(100 * x / sum(inv)) for x in inv]
    assert kans == [66, 20, 14], kans
    assert "1,47" in content3 and "8 punten" in content and "2-2" in content2
    print("dry run ok")
