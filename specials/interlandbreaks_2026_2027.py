# -*- coding: utf-8 -*-
"""Evergreen artikel: alle interlandbreaks van 2026/27, wat Oranje speelt en waarom er geen Eredivisie is (9-11-2026).
Bronnen:
- FIFA Men's International Match Calendar 2023-2030 (versie april 2026, digitalhub.fifa.com/m/3123d37097318f7f/...):
  2026: 21 sep - 6 okt (max. 4 duels), 9 - 17 nov (2). 2027: 22 - 30 mrt (2), 7 - 15 jun (2), 20 sep - 5 okt (4),
  8 - 16 nov (2). 2028: 20 - 28 mrt (2), 29 mei - 6 jun (2).
- KNVB speeldagenkalender betaald voetbal 2026/'27 (pdf knvb.nl/downloads/bestand/29830 + nieuwsbericht 19-12-2025):
  Eredivisie rd 7 = 19/20 sep, rd 8 = 9-11 okt (PSV - Heerenveen vr 9 okt, eredivisie.nl), rd 12 = 6-8 nov, rd 13 = 21/22 nov,
  rd 27 = 20/21 mrt, rd 28 = 3/4 apr 2027; laatste rd 34 zo 23 mei 2027; winterstop na zo 20 dec, hervat vr 8 jan 2027;
  geen Eredivisie op 17/18 apr 2027 (bekerfinale zo 18 apr, De Kuip). KKD: rd 8 vr 25 sep en rd 9 vr 2 okt (tijdens de break),
  rd 15 in week 46 (tijdens de break), geen KKD in week 12 (maartbreak), laatste rd vr 14 mei 2027.
- Speelronde 13 Eredivisie (aftrap): eigen API /api/fixtures/eredivisie (9-11-2026); NEC - PSV za 16:30 en Feyenoord - Excelsior
  za 18:45 ook bij Sporza, Ajax - ADO zo 14:30 ook bij Ajax.nl. KKD rd 15 za 14 / zo 15 nov: API + fcupdate (NAC - Emmen za 16:30).
- Oranje sep/okt + nov 2026: specials/nations_league_2028_feiten.md (UEFA, OnsOranje, NOS). Kwartfinales/play-offs 25-30 mrt 2027,
  Finals 9-13 jun 2027: UEFA 'all you need to know' 2026/27.
- EK 2028: UEFA 'EURO 2028 all you need to know' (toernooi 9 jun - 9 jul 2028, VK + Ierland; kwalificatie mrt - nov 2027,
  play-offs mrt 2028); loting kwalificatie zo 6 dec 2026 Belfast (UEFA).
- Vrijgave spelers: FIFA-reglement status en transfers van spelers (RSTP), bijlage 1; ECA Q&A over verplichte vrijgave.
Bewust NIET gebruikt (onbevestigd): exacte data vrouwen-interlandperiodes (geen primaire FIFA-bron geopend), of Oranje in maart
2027 naast de kwartfinales ook EK-kwalificatieduels speelt, exacte EK-kwalificatiespeeldagen per periode, gastheer Finals 2027,
precieze vrijgavedagen per window (maandag-start wel, terugkeerregels niet).
  python3 specials/interlandbreaks_2026_2027.py   (dry run)"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "interlandbreaks-2026-2027-alle-data-geen-eredivisie"
RUBRIEK = "66d6d655bc312d5c0e834ecd"   # Oranje/interlands
TITEL = "Interlandbreaks 2026/27: alle data en geen Eredivisie"
SAMENVATTING = ("Wanneer is de volgende interlandbreak? Alle FIFA-periodes van 2026/27, wat Oranje speelt en welke "
                "Eredivisie-ronde ervoor en erna valt.")
BIJWERKEN = "na elke interlandbreak (eerstvolgende: woensdag 18 november 2026, antwoordblok en tabel 'nu bezig')"

# deelkaart: og_kaarten/gsod.py
OG_LOGO = "nederland-logo.png"
OG_EYEBROW = "Alle data · wanneer geen Eredivisie"
OG_KOP = "Interlandbreaks<br><em>2026/27</em>"
OG_TEGELS = [("Nu", "9-17 nov"), ("Volgende", "22-30 mrt")]
OG_KOPJE = "FIFA-interlandperiodes 2026/27"
OG_RECHTS = "Max. duels"
OG_RIJEN = [("Sep/okt", "21 september t/m 6 oktober 2026", "4"),
            ("November", "9 t/m 17 november 2026", "2"),
            ("Maart", "22 t/m 30 maart 2027", "2"),
            ("Juni", "7 t/m 15 juni 2027", "2")]

# FIFA-kalender (versie april 2026): (naam, van, tot, max duels)
BREAKS = [("September/oktober 2026", "ma 21 september", "di 6 oktober 2026", 4),
          ("November 2026", "ma 9 november", "di 17 november 2026", 2),
          ("Maart 2027", "ma 22 maart", "di 30 maart 2027", 2),
          ("Juni 2027", "ma 7 juni", "di 15 juni 2027", 2)]
VOLGEND_SEIZOEN = [("September/oktober 2027", "ma 20 september", "di 5 oktober 2027", 4),
                   ("November 2027", "ma 8 november", "di 16 november 2027", 2),
                   ("Maart 2028", "ma 20 maart", "di 28 maart 2028", 2),
                   ("Mei/juni 2028", "ma 29 mei", "di 6 juni 2028", 2)]

ORANJE = {
    "September/oktober 2026": "Nations League: Nederland – Duitsland 1-1, Servië – Nederland 1-2, Griekenland – Nederland 2-2, Nederland – Servië 2-1",
    "November 2026": "Nations League: Nederland – Griekenland (vr 13 nov) en Duitsland – Nederland (ma 16 nov), beide 20.45 uur",
    "Maart 2027": "Bij een plek bij de eerste twee: kwartfinale Nations League (25 t/m 30 maart, thuis en uit). De EK-kwalificatie begint ook in maart",
    "Juni 2027": "Bij plaatsing: Nations League Finals (9 t/m 13 juni). Anders naar verwachting EK-kwalificatie",
}

# Eredivisie/KKD rond elke break (KNVB-speeldagenkalender 2026/'27)
EREDIVISIE = [("September/oktober 2026", "Speelronde 7 (19 en 20 september)", "Speelronde 8 (9 tot en met 11 oktober)",
               "Ja: speelronde 8 (vr 25 sep) en 9 (vr 2 okt)"),
              ("November 2026", "Speelronde 12 (6 tot en met 8 november)", "Speelronde 13 (21 en 22 november)",
               "Ja: speelronde 15 (za 14 en zo 15 nov)"),
              ("Maart 2027", "Speelronde 27 (20 en 21 maart)", "Speelronde 28 (3 en 4 april)", "Nee"),
              ("Juni 2027", "Speelronde 34 (zo 23 mei, slotronde)", "Seizoen 2027/28", "Nee, seizoen is voorbij")]

# speelronde 13 (eigen API 9-11-2026, onder voorbehoud van wijzigingen)
RONDE13 = [("Za 21 nov", "16:30", "NEC – PSV"), ("Za 21 nov", "18:45", "FC Utrecht – SC Cambuur"),
           ("Za 21 nov", "18:45", "Feyenoord – Excelsior"), ("Za 21 nov", "21:00", "FC Groningen – sc Heerenveen"),
           ("Za 21 nov", "21:00", "Telstar – PEC Zwolle"), ("Zo 22 nov", "12:15", "FC Twente – Willem II"),
           ("Zo 22 nov", "14:30", "Ajax – ADO Den Haag"), ("Zo 22 nov", "14:30", "Sparta Rotterdam – AZ"),
           ("Zo 22 nov", "16:45", "Go Ahead Eagles – Fortuna Sittard")]

L = {"nlg": '<a href="/competities/uefa-nations-league">Nations League</a>',
     "ere": '<a href="/competities/eredivisie">Eredivisie</a>',
     "kkd": '<a href="/competities/keuken-kampioen-divisie">Keuken Kampioen Divisie</a>',
     "reken": '<a href="/nieuws/nations-league-nieuwe-opzet-2028-wat-betekent-het-voor-oranje">wat Oranje nodig heeft voor de kwartfinales</a>',
     "uitleg": '<a href="/nieuws/hoe-werkt-de-nations-league-complete-uitleg-2026-2027">hoe de Nations League werkt</a>',
     "selectie": '<a href="/nieuws/selectie-oranje-november-2026-griekenland-duitsland">selectie van Oranje voor november</a>',
     "nl": '<a href="/clubs/nederland">Oranje</a>',
     "vb": '<a href="/voorbeschouwingen">voorbeschouwingen</a>',
     "op": '<a href="/opstellingen">opstellingen</a>',
     "lk": '<a href="/live-kijken">live kijken</a>'}

VOLGENDE = BREAKS[2]
NU = BREAKS[1]
ANTWOORD = tabel(None, [
    ("<strong>Volgende interlandbreak</strong>", f"<strong>{VOLGENDE[1]} t/m {VOLGENDE[2]}</strong> (maximaal {VOLGENDE[3]} duels per land)"),
    ("<strong>Nu bezig</strong>", f"{NU[1]} t/m {NU[2]}"),
    ("<strong>Eredivisie weer terug</strong>", "Zaterdag 21 november 2026, speelronde 13"),
    ("<strong>Oranje deze break</strong>", "Nederland – Griekenland (vr 13 nov) en Duitsland – Nederland (ma 16 nov), 20.45 uur, NPO 3")])

BREAK_TABEL = tabel(["Interlandbreak", "Data", "Max. duels", "Oranje speelt"],
                    [(f"<strong>{n}</strong>", f"{v} t/m {t}", str(m), ORANJE[n]) for n, v, t, m in BREAKS])
ERE_TABEL = tabel(["Interlandbreak", "Laatste Eredivisie-ronde ervoor", "Eerste ronde erna", "KKD speelt door?"],
                  [(f"<strong>{a}</strong>", b, c, d) for a, b, c, d in EREDIVISIE])
R13_TABEL = tabel(["Dag", "Aftrap", "Wedstrijd"], RONDE13)
VOLGEND_TABEL = tabel(["Interlandbreak", "Data", "Max. duels"], [(f"<strong>{n}</strong>", f"{v} t/m {t}", str(m)) for n, v, t, m in VOLGEND_SEIZOEN])

content = f"""<p><strong>In het seizoen 2026/27 zijn er vier interlandbreaks van de FIFA: van 21 september tot en met 6 oktober 2026, van 9 tot en met 17 november 2026, van 22 tot en met 30 maart 2027 en van 7 tot en met 15 juni 2027. Nu loopt de novemberbreak. Daarom is er op 14 en 15 november geen Eredivisie. De competitie gaat verder op zaterdag 21 november met speelronde 13. De volgende interlandbreak begint op maandag 22 maart 2027.</strong></p>
{ANTWOORD}
<p>Hieronder vind je alle data, wat {L['nl']} in elke periode speelt, welke Eredivisie-ronde ervoor en erna valt, en waarom de competitie stilligt. Dit overzicht werken we na elke interlandbreak bij.</p>
<h3><strong>Alle interlandbreaks van 2026/27</strong></h3>
{BREAK_TABEL}
<p>De interlandperiodes staan vast in de internationale wedstrijdkalender van de FIFA, die geldt tot en met 2030. Een gewone periode duurt negen dagen, van maandag tot en met dinsdag van de week erna, met maximaal twee interlands per land. Nieuw dit seizoen is de dubbele periode in september en oktober: zestien dagen met ruimte voor vier wedstrijden. De oude losse breaks in september en oktober zijn daarin samengevoegd.</p>
<p>Na het WK van 2026 (11 juni tot en met 19 juli) was die lange periode de eerste interlandbreak van het nieuwe seizoen. Oranje speelde daarin vier groepsduels in de {L['nlg']} en bleef ongeslagen.</p>
<h3><strong>Interlandbreak november 2026</strong></h3>
<p>De novemberbreak loopt van maandag 9 tot en met dinsdag 17 november. Oranje verzamelde op 9 november in Zeist en speelt de laatste twee groepsduels: vrijdag 13 november thuis tegen Griekenland in de Johan Cruijff ArenA en maandag 16 november tegen Duitsland in het Olympiastadion in Berlijn. Beide wedstrijden beginnen om 20.45 uur en zijn live op NPO 3. Oranje staat met 8 punten bovenaan in groep A2, gelijk met Griekenland. Lees {L['reken']} en bekijk de {L['selectie']}.</p>"""

content2 = f"""<h3><strong>Eredivisie voor en na elke interlandbreak</strong></h3>
{ERE_TABEL}
<p>De {L['ere']} slaat in elke interlandperiode een weekend over. In september en oktober waren dat er twee achter elkaar: het laatste weekend van september en het eerste weekend van oktober. De laatste speelronde van het seizoen is op zondag 23 mei 2027. De interlandbreak van juni valt dus na de competitie.</p>
<p><strong>Waarom geen Eredivisie dit weekend?</strong> Op 14 en 15 november ligt de Eredivisie stil vanwege de interlandbreak. Pas op zaterdag 21 november wordt er weer gespeeld:</p>
{R13_TABEL}
<p><em>Aftraptijden volgens het programma van 9 november; wijzigingen zijn mogelijk.</em> Voor elke wedstrijd vind je op onze site {L['vb']}, en kort voor de aftrap de {L['op']}.</p>
<h3><strong>Waarom ligt de Eredivisie stil tijdens een interlandbreak?</strong></h3>
<p>Volgens het FIFA-reglement voor de status en transfers van spelers moeten clubs hun internationals afstaan voor wedstrijden in een officiële interlandperiode. Dat staat in bijlage 1 van dat reglement. De spelers melden zich op de maandag waarop de periode begint bij hun land. Buiten die periodes zijn clubs dat niet verplicht.</p>
<p>Bijna elke Eredivisie-club heeft spelers in een nationale ploeg, van Oranje en Jong Oranje tot buitenlandse landenteams. Zou de competitie doorgaan, dan zouden clubs zonder hun basisspelers moeten spelen. Daarom plant de KNVB in elke interlandperiode geen Eredivisie-wedstrijden.</p>
<h3><strong>Speelt de Keuken Kampioen Divisie wel door?</strong></h3>
<p>Meestal wel. De {L['kkd']} speelde tijdens de lange break in het najaar op vrijdag 25 september en vrijdag 2 oktober. Ook nu gaat de competitie door: speelronde 15 wordt op zaterdag 14 en zondag 15 november gespeeld, een week later volgt op vrijdag 20 november speelronde 16. Twee duels tussen beloftenteams staan op maandag 23 november.</p>
<p>In maart 2027 ligt ook de Keuken Kampioen Divisie stil. De laatste ronde voor die break is op vrijdag 19 maart, daarna wordt er weer gespeeld op vrijdag 2 april.</p>"""

content3 = f"""<h3><strong>Wat speelt Oranje in maart en juni 2027?</strong></h3>
<p><strong>Maart 2027 (22 tot en met 30 maart).</strong> Eindigt Oranje bij de eerste twee van groep A2, dan speelt het de kwartfinale van de Nations League, in een thuis- en een uitwedstrijd tussen 25 en 30 maart. In dezelfde dagen worden de play-offs voor promotie en degradatie gespeeld. Ook de kwalificatie voor het EK 2028 begint in maart 2027. Of Oranje dan al EK-kwalificatieduels speelt, wordt duidelijk na de loting op zondag 6 december 2026 in Belfast.</p>
<p><strong>Juni 2027 (7 tot en met 15 juni).</strong> In deze periode zijn de Nations League Finals: de halve finales op 9 en 10 juni en de finale en de troostfinale op 13 juni. De gastheer wordt in december gekozen. Landen die niet bij de laatste vier zitten, spelen naar verwachting EK-kwalificatieduels.</p>
<p>De groepsfase van de EK-kwalificatie loopt tot en met november 2027. De groepswinnaars plaatsen zich direct, en in maart 2028 volgen play-offs. Het EK 2028 zelf wordt van 9 juni tot en met 9 juli 2028 gespeeld in Engeland, Schotland, Wales, Noord-Ierland en Ierland. Meer over de opzet lees je in onze uitleg over {L['uitleg']}.</p>
<h3><strong>Vooruitblik: de interlandbreaks van 2027/28</strong></h3>
{VOLGEND_TABEL}
<p>Ook in 2027/28 is er dus weer een dubbele periode in september en oktober. Die interlandbreaks staan volledig in het teken van de EK-kwalificatie, die in november 2027 eindigt.</p>
<p><strong>Andere weekenden zonder Eredivisie.</strong> Niet alleen interlands zorgen voor een leeg weekend. De winterstop begint na zondag 20 december 2026, de Eredivisie gaat weer verder op vrijdag 8 januari 2027. In het weekend van de bekerfinale (zondag 18 april 2027, De Kuip) staat ook geen Eredivisie-ronde op het programma.</p>
<p><strong>Vrouwen.</strong> De Oranjevrouwen spelen in eigen interlandperiodes van de FIFA, met andere data dan de mannen. Die periodes staan los van de breaks in dit overzicht.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wanneer is de volgende interlandbreak?</strong><br>De huidige interlandbreak loopt van {NU[1]} tot en met {NU[2]}. De volgende is van {VOLGENDE[1]} tot en met {VOLGENDE[2]}.</p>
<p><strong>Waarom is er geen Eredivisie dit weekend?</strong><br>Op 14 en 15 november is het interlandbreak. Clubs moeten hun internationals dan afstaan. De Eredivisie gaat verder op zaterdag 21 november met speelronde 13.</p>
<p><strong>Speelt de Keuken Kampioen Divisie tijdens de interlandbreak?</strong><br>In november wel: speelronde 15 staat op zaterdag 14 en zondag 15 november. In de interlandbreak van maart 2027 ligt de Keuken Kampioen Divisie wel stil.</p>
<p><strong>Wanneer is de interlandbreak in maart 2027?</strong><br>Van {VOLGENDE[1]} tot en met {VOLGENDE[2]}. De kwartfinales van de Nations League worden van 25 tot en met 30 maart gespeeld.</p>
<p><strong>Hoeveel interlandbreaks zijn er in 2026/27?</strong><br>Vier: september/oktober (21 september tot en met 6 oktober), november (9 tot en met 17 november), maart (22 tot en met 30 maart) en juni (7 tot en met 15 juni).</p>
<p><strong>Wanneer speelt Oranje weer?</strong><br>Op vrijdag 13 november tegen Griekenland en maandag 16 november tegen Duitsland, beide om 20.45 uur op NPO 3. Daarna speelt Oranje pas weer in de interlandbreak van maart 2027.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re, datetime as dt
    alles = content + content2 + content3
    w = len(re.sub(r"<[^>]+>", " ", alles).split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", w, "woorden")
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert 900 <= w <= 2000, w
    # FIFA-windows: maandag t/m dinsdag, 9 dagen (2 duels) of 16 dagen (4 duels)
    MND = {"januari": 1, "februari": 2, "maart": 3, "april": 4, "mei": 5, "juni": 6, "juli": 7, "augustus": 8,
           "september": 9, "oktober": 10, "november": 11, "december": 12}
    def d(s, jaar):
        p = s.split()
        return dt.date(int(p[3]) if len(p) > 3 else jaar, MND[p[2]], int(p[1]))
    for n, v, t, m in BREAKS + VOLGEND_SEIZOEN:
        eind = d(t, 0)
        begin = d(v, eind.year)
        assert begin.weekday() == 0 and eind.weekday() == 1, (n, begin, eind)
        assert (eind - begin).days + 1 == (16 if m == 4 else 9), (n, begin, eind)
    # weekdagen in de tekst kloppen
    for datum, dag in [((2026, 11, 13), 4), ((2026, 11, 16), 0), ((2026, 11, 21), 5), ((2026, 11, 22), 6), ((2026, 11, 14), 5),
                       ((2026, 11, 20), 4), ((2026, 11, 23), 0), ((2026, 9, 25), 4), ((2026, 10, 2), 4), ((2027, 3, 19), 4),
                       ((2027, 4, 2), 4), ((2026, 12, 20), 6), ((2027, 1, 8), 4), ((2027, 4, 18), 6), ((2027, 5, 23), 6),
                       ((2026, 12, 6), 6), ((2026, 11, 9), 0)]:
        assert dt.date(*datum).weekday() == dag, datum
    # break en Eredivisie-rondes vallen niet samen
    assert dt.date(2026, 11, 8) < dt.date(2026, 11, 9) and dt.date(2026, 11, 17) < dt.date(2026, 11, 21)
    assert dt.date(2027, 3, 21) < dt.date(2027, 3, 22) and dt.date(2027, 3, 30) < dt.date(2027, 4, 3)
    assert dt.date(2026, 9, 20) < dt.date(2026, 9, 21) and dt.date(2026, 10, 6) < dt.date(2026, 10, 9)
    assert dt.date(2027, 5, 23) < dt.date(2027, 6, 7)
    assert dt.date(2027, 3, 22) <= dt.date(2027, 3, 25) and dt.date(2027, 3, 30) >= dt.date(2027, 3, 30)   # NL-kwartfinales in window
    assert dt.date(2027, 6, 7) <= dt.date(2027, 6, 9) and dt.date(2027, 6, 13) <= dt.date(2027, 6, 15)      # Finals in window
    assert len(RONDE13) == 9 and all(r[0][:2] in ("Za", "Zo") for r in RONDE13)
    # antwoordblok, intro en FAQ noemen dezelfde data
    for s in ("22 maart", "30 maart 2027"):
        assert s in ANTWOORD and s in content3.split("Veelgestelde vragen")[1]
    assert "22 maart 2027" in content.split("</strong></p>")[0]
    assert "9 tot en met 17 november" in content and "21 november" in content and "21 november" in content3
    assert "<h2" not in alles and "<h4" not in alles and "betcity" not in alles.lower() and "/go/" not in alles
    for verboden in ("espn", "footymetrics", "opstellingvandaag", "waaroptv", "wikipedia"):
        assert verboden not in alles.lower(), verboden
    assert content.startswith("<p><strong>") and content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    assert alles.count("Veelgestelde vragen") == 1 and 4 <= content3.split("Veelgestelde vragen")[1].count("<p><strong>") <= 6
    print("dry run ok")
