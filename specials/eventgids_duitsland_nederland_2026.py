# -*- coding: utf-8 -*-
"""Eventgids: Duitsland – Nederland, Nations League groep A2, maandag 16 november 2026 (geschreven 9-11-2026).

Bronnen:
- Basisfeiten (stand, programma, tiebreaks): specials/nations_league_2028_feiten.md (UEFA, reglement art. 15, OnsOranje, DFB).
- Datum, aftrap 20.45, stadion en tv in Duitsland (ARD; Servië – Duitsland op RTL): DFB 05-11-2026
  https://www.dfb.de/news/klopp-im-video-ein-bunter-mix-aus-sehr-jung-und-durchaus-erfahren
- Poorten open 18.45: DFB fan-infos Berlin https://www.dfb.de/maenner/nationalmannschaften/nationalmannschaft/fan-infos-berlin
- Olympiastadion, 20.45 uur: https://olympiastadion.berlin/en/news/international-match-at-the-olympic-stadium-in-berlin/
- Capaciteit 74.475: officiële stadionplattegrond Olympiastadion (olympiastadion.berlin, oly-park-plan_de.pdf).
- Tv Nederland: NOS (NPO 3, stream NOS.nl/NOS-app) via de feitenbrief; eigen zenderconfig data/tv_zenders.json.
  Bet365-streamingschema: status "nee" -> geen stream beloofd.
- Onderlinge balans (49 duels: Duitsland 18, Nederland 12, 19 gelijk, incl. 24-09-2026) en recente uitslagen:
  ARD Sportschau-wedstrijdpagina https://www.sportschau.de/live-und-ergebnisse/fussball/uefa-nations-league-a/ma11904007/deutschland_niederlande/info
  Recente duels 2012-2026 ook in API-Football (headtohead 1118-25).
- 1-1 van 24-09-2026 (eerste duel van Klopp): DFB https://www.dfb.de/news/first-germany-game-under-klopp-ends-in-draw +
  API-Football fixture 1528862 (Nmecha 32' na assist Adeyemi, Gakpo 90+2' na assist Van Bommel, Havertz rond 30' eruit).
- Klopp: DFB 24-07-2026 https://www.dfb.de/news/juergen-klopp-als-bundestrainer-vorgestellt (start 15-08-2026,
  vierjarig contract t/m WK 2030, assistenten Krawietz, Lijnders, Bender; Nagelsmann stopte 03-07-2026 na WK-uitschakeling
  door Paraguay na strafschoppen). Eerste selectie 44 spelers in twee groepen: DFB 17-09-2026.
- Duitse uitslagen, doelpuntenmakers en balbezit (Nations League en WK 2026): API-Football (1528899, 1528917, 1528939, 1565176).
- Selectie november (24 spelers, 05-11-2026, Füllkrug terug, Mohya nieuw, Raum niet geselecteerd): 90min.de 05-11-2026
  https://www.90min.de/klopp-nominiert-zum-zweiten-mal-diese-24-spieler-stehen-im-dfb-kader + DFB 05-11-2026 (24 spelers).
- Scenario's: eigen doorrekening van alle 81 uitslagcombinaties met de tiebreakregels van art. 15 (onderling resultaat eerst).
- Odds: 711 (Kambi sevelevnl) maandag 9 november 2026 rond 16.45 uur: Duitsland – Nederland nog niet aangeboden;
  Servië – Duitsland 10,00 / 6,10 / 1,30.
- Historische duels (WK 1974, EK 1988, WK 1990, EK 1992, EK 2004, EK 2012) en EK 2024 in Berlijn (Nederland – Oostenrijk 2-3,
  finale Spanje – Engeland): algemeen bekende uitslagen, gecontroleerd met API-Football waar beschikbaar (EK 2012).

Bewust NIET gebruikt (onbevestigd):
- Belgische uitzender (niets bevestigd gevonden);
- of de wedstrijd uitverkocht is en of er een Nederlands supportersvak is;
- dat Servië – Duitsland zonder publiek wordt gespeeld (één bron);
- clubs van Duitse spelers (transfers zomer 2026 niet allemaal te controleren) en een verwachte Duitse opstelling;
- de reden waarom Musiala en Raum ontbreken.

  python3 specials/eventgids_duitsland_nederland_2026.py   (dry run)
  kaart: cd live-kijken-agent && PYTHONPATH=specials ../superodd-agent/.venv/bin/python og_kaarten/gsod.py eventgids_duitsland_nederland_2026
"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "duitsland-nederland-hoe-laat-tv-stadion-16-november-2026"
RUBRIEK = "66d6d655bc312d5c0e834ecd"   # Oranje/interlands
TITEL = "Duitsland – Nederland: hoe laat, tv en stadion (16 november)"
SAMENVATTING = ("Duitsland – Nederland is maandag 16 november om 20.45 uur in het Olympiastadion in Berlijn. "
                "Live op NPO 3, in Duitsland op ARD.")

# deelkaart: og_kaarten/gsod.py
OG_LOGO = "vlaggen-de-nl.png"
OG_EYEBROW = "Nations League · Groep A2"
OG_KOP = "Duitsland – Oranje<br><em>maandag 16 november</em>"
OG_TEGELS = [("Aftrap", "20:45"), ("Tv", "NPO 3")]
OG_KOPJE = "Het slotduel van Oranje in Berlijn"
OG_RECHTS = "Info"
OG_RIJEN = [("Aftrap", "Maandag 16 november 2026", "20:45"),
            ("Tv", "NPO 3 en NOS; in Duitsland op ARD", "Live"),
            ("Stadion", "Olympiastadion, Berlijn", "74.475"),
            ("Inzet", "Oranje 8 punten, Duitsland 5 punten", "Groep A2")]

# NA DE WEDSTRIJD: uitslag + gevolgen toevoegen

L = {"nlg": '<a href="/competities/uefa-nations-league">Nations League</a>',
     "rekenwerk": '<a href="/nieuws/nations-league-nieuwe-opzet-2028-wat-betekent-het-voor-oranje">alle rekensommen voor Oranje</a>',
     "selectie": '<a href="/nieuws/selectie-oranje-november-2026-griekenland-duitsland">de selectie van Oranje</a>',
     "uitleg": '<a href="/nieuws/hoe-werkt-de-nations-league-complete-uitleg-2026-2027">hoe de Nations League werkt</a>',
     "nlgr": '<a href="/nieuws/nederland-griekenland-hoe-laat-tv-stadion-opstelling-13-november-2026">Nederland – Griekenland</a>',
     "nl": '<a href="/clubs/nederland">Nederland</a>',
     "gr": '<a href="/clubs/griekenland">Griekenland</a>',
     "de": '<a href="/clubs/duitsland">Duitsland</a>',
     "rs": '<a href="/clubs/servie">Servië</a>',
     "711": '<a href="/bookmakers/711">711</a>',
     "legaal": '<a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>',
     "live": '<a href="/live-kijken">live kijken</a>',
     "opst": '<a href="/opstellingen">opstellingen</a>'}

AFTRAP = "20:45"
CAPACITEIT = "74.475"

SNEL = [("<strong>Wedstrijd</strong>", "Duitsland – Nederland"),
        ("<strong>Competitie</strong>", "Nations League, League A, groep A2, speelronde 6"),
        ("<strong>Datum</strong>", "Maandag 16 november 2026"),
        ("<strong>Aftrap</strong>", AFTRAP),
        ("<strong>Stadion</strong>", f"Olympiastadion, Berlijn ({CAPACITEIT} plaatsen)"),
        ("<strong>Tv in Nederland</strong>", "NPO 3, stream via NOS.nl en de NOS-app"),
        ("<strong>Tv in Duitsland</strong>", "ARD")]

KLASSIEKERS = [("7 jul 1974", "WK-finale, München", "West-Duitsland – Nederland", "2-1"),
               ("21 jun 1988", "EK, halve finale, Hamburg", "West-Duitsland – Nederland", "1-2"),
               ("24 jun 1990", "WK, achtste finale, Milaan", "West-Duitsland – Nederland", "2-1"),
               ("18 jun 1992", "EK, groepsfase, Göteborg", "Nederland – Duitsland", "3-1"),
               ("15 jun 2004", "EK, groepsfase, Porto", "Duitsland – Nederland", "1-1"),
               ("13 jun 2012", "EK, groepsfase, Charkiv", "Nederland – Duitsland", "1-2")]

RECENT = [("24 sep 2026", "Nederland – Duitsland", "1-1", "Nations League, Amsterdam"),
          ("14 okt 2024", "Duitsland – Nederland", "1-0", "Nations League, München"),
          ("10 sep 2024", "Nederland – Duitsland", "2-2", "Nations League, Amsterdam"),
          ("26 mrt 2024", "Duitsland – Nederland", "2-1", "Oefenduel, Frankfurt"),
          ("29 mrt 2022", "Nederland – Duitsland", "1-1", "Oefenduel, Amsterdam"),
          ("6 sep 2019", "Duitsland – Nederland", "2-4", "EK-kwalificatie, Hamburg")]

DUITS = [("24 sep", "Nederland – Duitsland", "1-1", "Nmecha"),
         ("27 sep", "Duitsland – Griekenland", "0-1", ""),
         ("1 okt", "Duitsland – Servië", "2-0", "Bischof, Wirtz"),
         ("4 okt", "Griekenland – Duitsland", "0-0", "")]

STAND = [("1", "Nederland", "4", "2-2-0", "7-5", "+2", "<strong>8</strong>"),
         ("2", "Griekenland", "4", "2-2-0", "5-3", "+2", "<strong>8</strong>"),
         ("3", "Duitsland", "4", "1-2-1", "3-2", "+1", "<strong>5</strong>"),
         ("4", "Servië", "4", "0-0-4", "3-8", "-5", "<strong>0</strong>")]

ORANJE = [
    ("Winst", "Winst of gelijk", "14 of 12", "<strong>Groepswinst</strong>"),
    ("Winst", "Verlies", "11", "Kwartfinale; alleen bij een driekamp op 11 punten beslist het onderlinge doelsaldo"),
    ("Gelijk", "Winst of gelijk", "12 of 10", "<strong>Kwartfinale zeker</strong>"),
    ("Gelijk", "Verlies", "9", "Kwartfinale als Duitsland in Servië verliest; wint Duitsland daar, dan moet Griekenland van Servië verliezen en beslist het doelsaldo"),
    ("Verlies", "Winst", "11", "<strong>Kwartfinale zeker</strong>, als nummer 2"),
    ("Verlies", "Gelijk", "9", "Nummer 2 als Duitsland niet wint in Servië; anders beslist het doelsaldo"),
    ("Verlies", "Verlies", "8", "Derde plaats, geen kwartfinale"),
]

content = f"""<p><strong>{L['de']} – {L['nl']} wordt gespeeld op maandag 16 november 2026 in het Olympiastadion in Berlijn. De aftrap is om 20.45 uur. In Nederland zie je de wedstrijd live op NPO 3 en via de stream van de NOS, in Duitsland zendt ARD het duel uit. Het is de laatste groepswedstrijd van Oranje in de {L['nlg']}, en voor Duitsland is het misschien wel alles of niets.</strong></p>
<p>Duitsland staat met 5 punten derde in groep A2, drie punten achter Oranje en Griekenland. In dit artikel lees je hoe laat de wedstrijd begint, op welke zender hij te zien is, wat je moet weten over het stadion en kaarten, en wat er voor beide landen op het spel staat. Ook duiken we in de rivaliteit, de 1-1 van september en het Duitsland van Jürgen Klopp.</p>
<h3><strong>Duitsland – Nederland in het kort</strong></h3>
{tabel(["", ""], SNEL)}
<h3><strong>Hoe laat en in welk stadion?</strong></h3>
<p>De wedstrijd begint om <strong>20.45 uur</strong>, in Nederland en Duitsland dezelfde tijd. Gespeeld wordt in het <strong>Olympiastadion in Berlijn</strong>, met {CAPACITEIT} plaatsen. In sommige overzichten staat München als speelstad, maar dat is niet juist: de DFB en het stadion bevestigen allebei Berlijn. De poorten gaan volgens de DFB om 18.45 uur open, twee uur voor de aftrap.</p>
<p>Het Olympiastadion is een beladen plek. Er werd de WK-finale van 2006 gespeeld en in 2024 de EK-finale tussen Spanje en Engeland. Oranje heeft er minder goede herinneringen aan: op het EK van 2024 verloor het er in de groepsfase met 2-3 van Oostenrijk.</p>
<h3><strong>Op welke zender is Duitsland – Nederland te zien?</strong></h3>
<p><strong>In Nederland</strong> heeft de NOS de rechten op de wedstrijden van het Nederlands elftal. Je kijkt gratis op <strong>NPO 3</strong>, of via de livestream op NOS.nl en in de NOS-app. Een abonnement is niet nodig.</p>
<p><strong>In Duitsland</strong> is de wedstrijd live te zien bij <strong>ARD</strong>, meldt de DFB. Het uitduel van Duitsland in Servië, drie dagen eerder, zendt RTL uit. Heb je Das Erste van de ARD in je tv-pakket, dan kun je de wedstrijd ook met Duits commentaar volgen. Een Belgische uitzender hebben wij bij het schrijven nog niet kunnen bevestigen. Alle wedstrijden die je deze week {L['live']} kunt, staan in ons overzicht.</p>
<h3><strong>Kaarten voor Duitsland – Nederland</strong></h3>
<p>De kaartverkoop voor het Olympiastadion loopt via de DFB. Of de wedstrijd uitverkocht is, was bij het schrijven van dit artikel niet bekend. Als Oranjesupporter kun je voor uitwedstrijden het beste kijken bij de officiële ticketshop van de KNVB op tickets.knvb.nl. Koop geen kaarten via doorverkoopsites: daar betaal je vaak meer dan de officiële prijs en loop je het risico dat je niet naar binnen mag.</p>"""

content2 = f"""<h3><strong>De rivaliteit: Duitsland tegen Nederland</strong></h3>
<p>Weinig interlands leven in Nederland zo als die tegen Duitsland. Volgens de statistieken van de Duitse ARD speelden de buurlanden 49 keer tegen elkaar. Duitsland won er 18, Nederland 12 en 19 keer werd het gelijk. De grootste overwinningen zijn een 7-0 voor Duitsland in 1959 en twee keer 3-0: voor Duitsland in 2011 in Hamburg en voor Oranje in 2018 in Amsterdam.</p>
<p>De beladenheid komt vooral uit de grote toernooien. De WK-finale van 1974 ging met 2-1 verloren in München. Veertien jaar later nam Oranje revanche, in de halve finale van het EK 1988 in Hamburg. Lothar Matthäus zette West-Duitsland uit een strafschop op voorsprong, Ronald Koeman maakte ook vanaf elf meter gelijk, en twee minuten voor tijd schoof Marco van Basten de 1-2 binnen. Oranje won daarna in München de finale tegen de Sovjet-Unie: nog altijd de enige grote prijs van het Nederlands elftal.</p>
{tabel(["Datum", "Toernooi", "Wedstrijd", "Uitslag"], KLASSIEKERS)}
<p>De laatste jaren is Duitsland de lastigste tegenstander voor Oranje. De laatste Nederlandse zege dateert van september 2019, toen het in Hamburg 2-4 werd in de EK-kwalificatie. Daarna volgden drie gelijke spelen en twee Duitse zeges.</p>
{tabel(["Datum", "Wedstrijd", "Uitslag", "Soort duel"], RECENT)}
<h3><strong>De 1-1 in Amsterdam: het eerste duel van Klopp</strong></h3>
<p>Op 24 september openden de twee landen de groep in de Johan Cruijff ArenA. Het was de eerste interland van Jürgen Klopp als bondscoach van Duitsland, en ook Xavi Hernández stond voor het eerst langs de lijn bij Oranje. Virgil van Dijk kopte in de twaalfde minuut raak, maar zijn doelpunt werd na tussenkomst van de VAR afgekeurd voor een overtreding in de aanloop. Rond het halfuur moest Kai Havertz na een harde overtreding naar de kant. Felix Nmecha maakte in de 32e minuut de 0-1, na een pass van Karim Adeyemi.</p>
<p>Oranje kreeg genoeg kansen. Crysencio Summerville kopte vrij naast en invaller Mexx Meerdink schoot in de tweede helft naast een leeg doel. Doelman Marc-André ter Stegen hield Duitsland lang overeind, tot Cody Gakpo in de tweede minuut van de blessuretijd de 1-1 binnenschoot, op aangeven van Ruben van Bommel. Door die gelijkmaker staat Oranje nu bovenaan.</p>"""

content3 = f"""<h3><strong>Duitsland onder Jürgen Klopp</strong></h3>
<p>Klopp volgde Julian Nagelsmann op, die op 3 juli 2026 stopte. Duitsland was op het WK in de eerste knock-outronde na strafschoppen uitgeschakeld door Paraguay. De DFB presenteerde Klopp op 24 juli, op 15 augustus begon hij officieel. Hij tekende een contract voor vier jaar, tot en met het WK 2030. Zijn assistenten zijn Peter Krawietz, Pepijn Lijnders en Sven Bender. Voor zijn eerste vier duels riep Klopp maar liefst 44 spelers op, verdeeld over twee groepen.</p>
{tabel(["Datum", "Wedstrijd", "Uitslag", "Duitse doelpunten"], DUITS)}
<p>De cijfers laten een duidelijk patroon zien. Duitsland heeft de bal, maar scoort weinig. Thuis tegen Griekenland had het 76 procent balbezit en verloor het toch met 0-1. Tegen Servië kwam het tot 32 schoten en twee doelpunten, in Thessaloniki bleef het bij 0-0 ondanks 21 schoten. In vier duels maakte Duitsland 3 doelpunten. Defensief staat het wel goed: Duitsland kreeg maar 2 doelpunten tegen, van Gakpo en van de Griek Dimitris Kourbelis.</p>
<p><strong>Sleutelspelers.</strong> Florian Wirtz is de creatieve spil en scoorde tegen Servië. Joshua Kimmich is de leider op het middenveld. Felix Nmecha maakte het doelpunt tegen Oranje, de jonge Tom Bischof scoorde tegen Servië. Kai Havertz is na zijn blessure in Amsterdam terug in de selectie. Achterin vormen Jonathan Tah en Nico Schlotterbeck het ervaren hart.</p>
<p>Voor de duels in Servië en tegen Oranje koos Klopp op 5 november voor 24 spelers. Spits Niclas Füllkrug is terug en U21-international Wael Mohya zit voor het eerst bij de A-selectie. Opvallend is dat RB Leipzig-aanvoerder David Raum ontbreekt.</p>
<h3><strong>Wat staat er op het spel?</strong></h3>
{tabel(["#", "Land", "G", "W-G-V", "Doelpunten", "Saldo", "Punten"], STAND)}
<p>Bij gelijke punten telt eerst het onderlinge resultaat. Griekenland heeft dat tegen Duitsland al binnen (0-1 en 0-0). Tussen Duitsland en Nederland staat het na de 1-1 nog gelijk, en dat geldt ook voor Nederland en Griekenland (2-2). De nummers 1 en 2 spelen in maart 2027 de kwartfinales.</p>
<p><strong>Wat heeft Duitsland nodig?</strong> Wij rekenden alle mogelijke uitslagen door. De conclusies:</p>
<ul><li><strong>Verlies tegen Oranje:</strong> Duitsland haalt de kwartfinales niet, ook niet met een zege in Servië.</li><li><strong>Gelijk tegen Oranje:</strong> alleen genoeg als Duitsland in Servië wint. Dan moet Griekenland in Amsterdam winnen (en beslist het doelsaldo tussen Duitsland en Oranje), of moet Oranje van Griekenland winnen en Griekenland daarna van Servië verliezen. Bij een gelijkspel in Amsterdam is Duitsland derde.</li><li><strong>Winst op Oranje:</strong> zeker genoeg als Griekenland in Amsterdam wint. Bij een gelijkspel in Amsterdam moet Duitsland in Servië minstens gelijkspelen. Wint Oranje van Griekenland, dan moet Duitsland ook in Servië winnen en mag Griekenland niet van Servië winnen; anders beslist het doelsaldo in een driekamp op 11 punten. Bij een gelijkspel in Servië moet Griekenland dan van Servië verliezen.</li><li><strong>Slechtste geval:</strong> verliest Duitsland in Belgrado en wint het niet van Oranje, dan kan het zelfs nog vierde worden, als Servië ook van Griekenland wint.</li></ul>
<p><strong>Wat heeft Oranje nodig?</strong> Dat hangt af van de uitslag van vrijdag tegen Griekenland. Dit is het overzicht:</p>
{tabel(["Tegen Griekenland", "In Berlijn", "Punten", "Uitkomst voor Oranje"], ORANJE)}
<p>De belangrijkste vuistregel: een overwinning in Berlijn betekent voor Oranje altijd de kwartfinales. Na de wedstrijd van vrijdag werken we dit overzicht bij. Meer achtergrond lees je in {L['rekenwerk']}, alles over het eerste duel van de week in onze gids voor {L['nlgr']}, en wie er in de selectie zit in {L['selectie']}. Nieuw met de Nations League? Lees eerst {L['uitleg']}.</p>
<h3><strong>Odds Duitsland – Nederland</strong></h3>
<p>Bij {L['711']} stonden op maandag 9 november nog geen odds voor Duitsland – Nederland online. Voor het duel van Duitsland in Servië is 711 duidelijk: een Duitse zege staat op 1,30, een gelijkspel op 6,10 en een Servische zege op 10,00. Zodra er odds zijn voor Berlijn, voegen we ze hier toe. Wed alleen bij een bookmaker met een vergunning van de Kansspelautoriteit; lees {L['legaal']}.</p>
<p>De officiële opstellingen komen ongeveer een uur voor de aftrap naar buiten. Je vindt ze dan op onze pagina met {L['opst']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>In welk stadion speelt Duitsland – Nederland op 16 november?</strong><br>In het Olympiastadion in Berlijn, met {CAPACITEIT} plaatsen. Niet in München, zoals sommige overzichten melden.</p>
<p><strong>Hoe laat begint Duitsland – Nederland?</strong><br>Op maandag 16 november 2026 om 20.45 uur. De poorten van het stadion gaan om 18.45 uur open.</p>
<p><strong>Op welke zender is Duitsland – Nederland te zien?</strong><br>In Nederland op NPO 3, met een gratis livestream op NOS.nl en in de NOS-app.</p>
<p><strong>Is Nederland – Duitsland op de Duitse tv?</strong><br>Ja. In Duitsland zendt ARD de wedstrijd live uit. Het duel van Duitsland in Servië, op vrijdag 13 november, is bij RTL te zien.</p>
<p><strong>Hoe kom ik aan kaarten voor Duitsland – Nederland?</strong><br>De kaartverkoop loopt via de DFB. Oranjesupporters kunnen het beste kijken bij de officiële KNVB-ticketshop op tickets.knvb.nl. Koop niet via doorverkoopsites.</p>
<p><strong>Wat heeft Oranje nodig in Berlijn?</strong><br>Met een overwinning is Oranje altijd zeker van de kwartfinales. Wat een gelijkspel of nederlaag betekent, hangt af van de uitslag tegen Griekenland op vrijdag.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    alles = content + content2 + content3
    w = len(re.sub(r"<[^>]+>", " ", alles).split())
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
    # tijden: aftrap 20.45/20:45, poorten 18.45 (tekst en FAQ gelijk)
    assert set(re.findall(r"\b\d{2}[.:]\d{2}\b", alles + str(OG_RIJEN) + str(OG_TEGELS))) <= {"20.45", "20:45", "18.45"}
    assert alles.count("18.45 uur") == 2 and "om 20.45 uur" in content3
    # capaciteit overal gelijk
    assert CAPACITEIT in content and CAPACITEIT in content3 and OG_RIJEN[2][2] == CAPACITEIT
    # onderlinge balans: 18 + 12 + 19 = 49; laatste zes: sinds 2019 geen Oranje-zege (3 gelijk, 2 verlies)
    assert 18 + 12 + 19 == 49
    uitslag = [tuple(map(int, r[2].split("-"))) for r in RECENT]
    nl_res = []
    for (wed, (a, b)) in zip([r[1] for r in RECENT], uitslag):
        nl_thuis = wed.startswith("Nederland")
        nl, de = (a, b) if nl_thuis else (b, a)
        nl_res.append("W" if nl > de else "G" if nl == de else "V")
    assert nl_res[:5].count("G") == 3 and nl_res[:5].count("V") == 2 and nl_res[5] == "W", nl_res
    # Duitse doelpunten 3 voor, 2 tegen in vier duels
    assert sum(int(r[2].split("-")[1 if r[1].startswith(("Nederland", "Griekenland")) else 0]) for r in DUITS) == 3
    assert sum(int(r[2].split("-")[0 if r[1].startswith(("Nederland", "Griekenland")) else 1]) for r in DUITS) == 2
    # Duitsland max 11 punten; bij verlies tegen Oranje max 8 < Oranje min 8 met onderling voordeel NL
    assert 5 + 3 + 3 == 11 and 5 + 3 == 8
    print("dry run ok")
