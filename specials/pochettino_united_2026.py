# -*- coding: utf-8 -*-
"""Los artikel: Mauricio Pochettino wordt de nieuwe trainer van Manchester United (13-11-2026).
Zoekwoorden: Pochettino Manchester United, nieuwe trainer Manchester United, Pochettino United contract, Carrick ontslagen,
eerste wedstrijd Pochettino, Liverpool - Manchester United.
Feiten: specials/pochettino_united_2026_feiten.md (Sky Sports 12/13-11, ESPN 13-11, The Athletic via Soccernews/Voetbalzone,
NOS, Wikipedia carrière + seizoenspagina, Kambi-odds Unibet/711 13-11 12:20). STATUS bij schrijven: nog niet officieel op
manutd.com -> formulering 'akkoord volgens Sky/ESPN/The Athletic, officiële bekendmaking verwacht'. Na de clubverklaring
bijwerken (titel kan blijven).
Weggelaten (onzeker): exacte afkoopsom (alleen 'zo'n 9 à 10 miljoen euro'), staf behalve Jesús Pérez, score CL-finale 2019,
Xavi Simons, aftraptijden na Liverpool (alleen datums + 'onder voorbehoud'), citaat Pochettino (nog niet gepresenteerd).
  python3 specials/pochettino_united_2026.py  (dry run)"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, "..")); sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "pochettino-nieuwe-trainer-manchester-united"
RUBRIEK = "64ff0fbd5a8f205b05d5468f"   # Voetbal
TITEL = "Pochettino nieuwe trainer Manchester United: alle feiten"
SAMENVATTING = ("Mauricio Pochettino wordt de nieuwe trainer van Manchester United als opvolger van Carrick. Contract, "
                "eerste wedstrijd en zijn loopbaan.")
OG_EB = "Premier League · trainersnieuws"
OG_KOP = "Pochettino naar <em>Manchester United</em>"
OG_RIJEN = [("Contract", "tot zomer 2029"), ("Opvolger van", "Michael Carrick"), ("Eerste duel", "Liverpool – United, 22-11"),
            ("Stand United", "18e, 8 punten")]

L = {"united": '<a href="/clubs/manchester-united">Manchester United</a>',
     "liverpool": '<a href="/clubs/liverpool">Liverpool</a>',
     "pl": '<a href="/competities/premier-league">Premier League</a>',
     "unibet": '<a href="/bookmakers/unibet">Unibet</a>',
     "legaal": '<a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>'}

content = f"""<p><strong>Mauricio Pochettino wordt de nieuwe trainer van {L['united']}. Volgens Sky Sports, ESPN en The Athletic is de Argentijn akkoord over een contract van tweeënhalf jaar, tot de zomer van 2029. Hij volgt Michael Carrick op, die donderdag werd ontslagen met United op de achttiende plaats in de Premier League. Zijn eerste wedstrijd is meteen een kraker: Liverpool – Manchester United op zondag 22 november om 17:30 uur.</strong></p>
<p>De officiële bekendmaking door de club werd vrijdag 13 november verwacht. Pochettino is nu nog bondscoach van de Verenigde Staten; United koopt hem daar los via een clausule in zijn contract, voor zo'n 9 à 10 miljoen euro. Hij wordt de achtste vaste trainer van United sinds het vertrek van Sir Alex Ferguson in 2013. De club sprak al eerder met hem, onder meer in 2022, toen uiteindelijk Erik ten Hag werd gekozen.</p>
<h3><strong>Pochettino en Manchester United in het kort</strong></h3>
{tabel(["", "Pochettino bij Manchester United"], [
    ("Functie", "Head coach (trainer)"),
    ("Contract", "Tweeënhalf jaar, tot de zomer van 2029"),
    ("Opvolger van", "Michael Carrick (ontslagen op 12 november)"),
    ("Vorige club", "Bondscoach van de Verenigde Staten (2024 – 2026)"),
    ("Eerste training", "Donderdag 19 november"),
    ("Eerste wedstrijd", "Liverpool – Manchester United, zondag 22 november, 17:30 uur"),
    ("Assistent", "Jesús Pérez, zijn vaste rechterhand"),
])}
<h3><strong>Waarom moest Carrick weg?</strong></h3>
<p>Manchester United beleeft de slechtste competitiestart in veertig jaar. Na tien wedstrijden staat de ploeg met acht punten op de achttiende plaats, in de degradatiezone: één zege, vijf gelijke spelen en vier nederlagen. Na het 4-4-gelijkspel tegen Aston Villa besloot de clubleiding, op advies van CEO Omar Berrada en technisch directeur Jason Wilcox, tot ontslag. Volgens de club was het "the extremely difficult conclusion that a change is necessary". Ook Carricks assistenten, onder wie Jonny Evans en Jonathan Woodgate, moesten vertrekken.</p>
<p>Het is een opvallende val voor Carrick. Hij nam het in januari 2026 over van de ontslagen Ruben Amorim, eindigde vorig seizoen nog als derde en kreeg in mei een contract tot 2028. Dit seizoen won United maar drie van de vijftien wedstrijden in alle competities. In de League Cup lag de ploeg er al in september uit, tegen Brighton.</p>"""

content2 = f"""<h3><strong>Wat is het programma van Pochettino bij United?</strong></h3>
<p>Pochettino maakt eerst de interlandperiode af bij de Verenigde Staten: hij coacht de VS nog in twee wedstrijden tegen Haïti in de CONCACAF Nations League, op zaterdag 14 november en dinsdag 17 november. Daarna vliegt hij naar Manchester. Op donderdag 19 november leidt hij zijn eerste training, en drie dagen later staat hij al op Anfield.</p>
{tabel(["Datum", "Wedstrijd", "Competitie"], [
    ("Zondag 22 november, 17:30", "<strong>Liverpool – Manchester United</strong>", "Premier League"),
    ("Woensdag 25 november", "Sporting – Manchester United", "Champions League"),
    ("Zaterdag 28 november", "Manchester United – Brentford", "Premier League"),
    ("Woensdag 2 december", "Newcastle – Manchester United", "Premier League"),
    ("Zaterdag 5 december", "Manchester United – Coventry", "Premier League"),
    ("Dinsdag 8 december", "Manchester United – RB Leipzig", "Champions League"),
])}
<p><em>Aftraptijden na Liverpool – United onder voorbehoud: die kunnen door tv-keuzes nog verschuiven.</em></p>
<p>In de Champions League staat United na vier wedstrijden zeventiende in de competitiefase, met zes punten. Plek 9 tot en met 24 geeft recht op de play-offs, dus Europa ligt nog open.</p>
<h3><strong>Wie is Mauricio Pochettino?</strong></h3>
<p>Pochettino (54) werd geboren in Murphy, in de Argentijnse provincie Santa Fe. Als centrale verdediger speelde hij voor Newell's Old Boys, Espanyol, Paris Saint-Germain en Bordeaux, en hij speelde twintig interlands voor Argentinië, onder meer op het WK van 2002. Als trainer bouwde hij een reputatie op met hoge druk, een grote fysieke intensiteit en het vertrouwen in jonge spelers: bij Tottenham groeiden onder hem Harry Kane en Dele Alli uit tot vaste krachten.</p>
{tabel(["Periode", "Club", "Hoogtepunt"], [
    ("2009 – 2012", "Espanyol", "Eerste trainersbaan, bij zijn oude club"),
    ("2013 – 2014", "Southampton", "Achtste plaats in de Premier League"),
    ("2014 – 2019", "Tottenham Hotspur", "Tweede in 2016/17, finale Champions League 2019"),
    ("2021 – 2022", "Paris Saint-Germain", "Landstitel 2022, Coupe de France 2021"),
    ("2023 – 2024", "Chelsea", "Finale League Cup 2024, zesde in de Premier League"),
    ("2024 – 2026", "Verenigde Staten", "Achtste finale op het WK 2026"),
])}
<p>Zijn enige prijzen als trainer won hij met PSG: de Franse titel, de Coupe de France en de Trophée des Champions. Met Tottenham haalde hij in 2019 de finale van de Champions League, die verloren ging tegen Liverpool. Met de Verenigde Staten won hij op het eigen WK van 2026 zijn groep, met onder meer 4-1 tegen Paraguay, en daarna van Bosnië-Herzegovina (2-0): de eerste WK-zege in de knock-outfase van de VS sinds 2002. In de achtste finale was België te sterk (1-4).</p>"""

content3 = f"""<h3><strong>Wat betekent Pochettino voor de Nederlanders bij United?</strong></h3>
<p>Bij United spelen met Matthijs de Ligt en Joshua Zirkzee twee Nederlanders, en ook de in Leiderdorp geboren Marokkaanse international Noussair Mazraoui zit in de selectie. Hoe Pochettino met hen verder wil, is nog onbekend. Ervaring met Nederlanders heeft hij wel: bij PSG werkte hij met Georginio Wijnaldum, bij Tottenham met Vincent Janssen en bij Chelsea met Ian Maatsen. Talent Chido Obi wordt dit seizoen verhuurd aan Willem II.</p>
<h3><strong>Odds: kan Pochettino United nog omhoog trekken?</strong></h3>
{tabel(["Markt", "Odd"], [
    ("Liverpool wint (22 november)", "1,79"),
    ("Gelijkspel", "4,30"),
    ("Manchester United wint", "4,35"),
    ("Manchester United eindigt in de top 4", "8,00"),
    ("Manchester United eindigt in de top 6", "4,00"),
    ("Manchester United landskampioen", "201,00"),
])}
<p><em>Odds bij {L['unibet']}, vrijdag 13 november rond 12:20 uur. Odds kunnen nog veranderen.</em></p>
<p>De bookmakers verwachten weinig van een snelle ommekeer: een plek bij de eerste vier staat op 8,00, en in het eerste duel op Anfield is United duidelijk de underdog. Arsenal is met 1,25 de grote favoriet voor de titel. Wedden doe je alleen bij een bookmaker met een vergunning van de Kansspelautoriteit; lees {L['legaal']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wie is de nieuwe trainer van Manchester United?</strong><br>Mauricio Pochettino. Volgens Sky Sports, ESPN en The Athletic is hij akkoord over een contract tot de zomer van 2029.</p>
<p><strong>Wie volgt Pochettino op bij Manchester United?</strong><br>Michael Carrick, die op donderdag 12 november werd ontslagen.</p>
<p><strong>Wanneer is de eerste wedstrijd van Pochettino bij United?</strong><br>Op zondag 22 november om 17:30 uur, uit bij Liverpool in de Premier League.</p>
<p><strong>Hoe lang is het contract van Pochettino?</strong><br>Tweeënhalf jaar, tot de zomer van 2029.</p>
<p><strong>Welke prijzen won Pochettino als trainer?</strong><br>Met PSG won hij de Franse titel (2022), de Coupe de France (2021) en de Trophée des Champions. Met Tottenham haalde hij de finale van de Champions League (2019).</p>
<p><strong>Op welke plek staat Manchester United?</strong><br>Achttiende in de Premier League, met acht punten uit tien wedstrijden.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    alles = content + content2 + content3
    w = len(re.sub(r"<[^>]+>", " ", alles).split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", w, "woorden")
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert 1 + 5 + 4 == 10 and 1 * 3 + 5 == 8
    assert "<h2" not in alles and "betcity" not in alles.lower() and "/go/" not in alles
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    print("dry run ok")
