# -*- coding: utf-8 -*-
"""Los artikel: Nederlanders in La Liga 2026/27 (selecties gecontroleerd via de voetbal-API, 9 okt 2026).
  python3 specials/nederlanders_la_liga_2026.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Nederlanders in La Liga 2026/27: alle acht spelers in Spanje"
SLUG = "nederlanders-in-la-liga-2026-27"
SAMENVATTING = ("Acht Nederlanders spelen in 2026/27 in La Liga, bij zes clubs. Van Frenkie de Jong (Barcelona) en "
                "Denzel Dumfries (Real Madrid) tot het Valencia-trio.")
RUBRIEK_LA_LIGA = "66bdf1e952f7cbe082b4c165"
COMPETITIE_LA_LIGA = "65eafa89159aadee0c5d81d2"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in koppen)
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}><thead><tr>{kop}</tr></thead><tbody>{body}</tbody></table>"


C = {"FC Barcelona": "fc-barcelona", "Real Madrid": "real-madrid", "Valencia": "valencia", "Espanyol": "espanyol",
     "Rayo Vallecano": "rayo-vallecano", "Deportivo La Coruña": "deportivo-la-coruna"}
_g = set()


def club(c):
    if c in _g:
        return c
    _g.add(c)
    return f'<a href="/clubs/{C[c]}">{c}</a>'


SPELERS = [
    ("Frenkie de Jong", "FC Barcelona", "Middenvelder", "1e"),
    ("Denzel Dumfries", "Real Madrid", "Verdediger", "4e"),
    ("Zakaria Eddahchouri", "Deportivo La Coruña", "Aanvaller", "7e"),
    ("Jozhua Vertrouwd", "Rayo Vallecano", "Verdediger", "12e"),
    ("Quilindschy Hartman", "Espanyol", "Verdediger", "15e"),
    ("Arnaut Danjuma", "Valencia", "Aanvaller", "19e"),
    ("Justin de Haas", "Valencia", "Verdediger", "19e"),
    ("Kayne van Oevelen", "Valencia", "Doelman", "19e"),
]
L = "/nieuws/"

content = f"""<p><strong>In het seizoen 2026/27 spelen acht Nederlanders in La Liga, verdeeld over zes clubs. Frenkie de Jong (FC Barcelona) en nieuwkomer Denzel Dumfries (Real Madrid) zijn de grootste namen. Valencia heeft met Arnaut Danjuma, Justin de Haas en Kayne van Oevelen de meeste Nederlanders in de selectie.</strong></p>
<p>Spanje trekt minder Nederlanders dan Engeland, Duitsland of Italië, maar wie er speelt, doet dat vaak bij een club met naam. Deze zomer kwamen er vier nieuwe landgenoten bij, onder wie Dumfries bij Real Madrid. In dit overzicht lees je wie er in <a href="/competities/la-liga">La Liga</a> speelt, hoe hun club ervoor staat en wie Spanje verliet.</p>
<h3><strong>Alle Nederlanders in La Liga 2026/27</strong></h3>
{tabel(["Speler", "Club", "Positie", "Club op de ranglijst"], [(s, club(c), p, st) for s, c, p, st in SPELERS])}
<p><em>Alleen spelers die voor Nederland uitkomen. Selecties en stand gecontroleerd op 9 oktober 2026, na zeven speelrondes.</em></p>
<h3><strong>Nederlanders in speelronde 8</strong></h3>
{tabel(["Wedstrijd", "Nederlander", "Aftrap"], [
    ("Málaga – Espanyol", "Hartman", "vr 9 okt, 21:00"),
    (f'<a href="{L}rayo-vallecano-athletic-bilbao-live-gratis-kijken-10-10-2026">Rayo Vallecano – Athletic Club</a>', "Vertrouwd", "za 10 okt, 14:00"),
    (f'<a href="{L}fc-barcelona-getafe-live-gratis-kijken-10-10-2026">Barcelona – Getafe</a>', "De Jong", "za 10 okt, 18:30"),
    (f'<a href="{L}real-madrid-villarreal-live-gratis-kijken-10-10-2026">Real Madrid – Villarreal</a>', "Dumfries", "za 10 okt, 21:00"),
    (f'<a href="{L}real-sociedad-deportivo-la-coruna-live-gratis-kijken-11-10-2026">Real Sociedad – Deportivo</a>', "Eddahchouri", "zo 11 okt, 16:15"),
    (f'<a href="{L}racing-santander-valencia-live-gratis-kijken-11-10-2026">Racing Santander – Valencia</a>', "Danjuma, De Haas, Van Oevelen", "zo 11 okt, 21:00"),
])}"""

content2 = """<h3><strong>Frenkie de Jong: aan zijn achtste seizoen bij Barcelona</strong></h3>
<p>Frenkie de Jong kwam in 2019 van Ajax naar Barcelona en is daar al jaren een van de dragende spelers op het middenveld. Hij werd drie keer Spaans kampioen met de club: in 2022/23, 2024/25 en 2025/26. Als regerend kampioen begon Barcelona ook dit seizoen sterk: na zeven duels staat de ploeg met 21 punten aan kop, oftewel zeven zeges uit zeven wedstrijden.</p>
<h3><strong>Denzel Dumfries: van Inter naar Real Madrid</strong></h3>
<p>De opvallendste Nederlandse transfer naar Spanje deze zomer was die van Denzel Dumfries. Real Madrid haalde de rechtsback weg bij Internazionale en legde hem vast tot medio 2030. Na Sparta, Heerenveen, PSV en vijf jaar Italië is het zijn eerste avontuur in Spanje. Daarmee spelen er nu bij beide Spaanse grootmachten Nederlanders, en treffen De Jong en Dumfries elkaar dit seizoen in El Clásico.</p>
<h3><strong>Valencia: drie Nederlanders in Mestalla</strong></h3>
<p>De grootste Nederlandse groep vind je niet in Madrid of Barcelona, maar in Valencia. Aanvaller <strong>Arnaut Danjuma</strong> kent Spanje het best: hij speelde eerder voor Villarreal en Girona en tekende in 2025 bij Valencia tot medio 2028. Deze zomer kwamen er twee landgenoten bij. Centrale verdediger <strong>Justin de Haas</strong> kwam transfervrij over van Famalicão in Portugal, waar hij in 2025/26 alle 33 competitieduels volledig speelde en zes keer scoorde. Hij tekende tot 2030. Doelman <strong>Kayne van Oevelen</strong>, oud-keeper van FC Volendam, wordt dit seizoen gehuurd van Ipswich Town.</p>
<p>De seizoensstart van Valencia is wel zorgelijk: na zeven duels staat de club negentiende met vier punten.</p>
<h3><strong>Hartman, Vertrouwd en Eddahchouri</strong></h3>
<p><strong>Quilindschy Hartman</strong> speelde jarenlang voor Feyenoord en wordt dit seizoen door Burnley verhuurd aan Espanyol. <strong>Jozhua Vertrouwd</strong> nam een minder gebruikelijke route: na de jeugdopleidingen in Nederland en Jong FC Utrecht vertrok hij naar Castellón in Spanje, waarna Rayo Vallecano hem voor vijf seizoenen vastlegde.</p>
<p><strong>Zakaria Eddahchouri</strong> kende eerder periodes bij onder meer Go Ahead Eagles en Telstar. Met Deportivo La Coruña promoveerde hij in 2025/26 als nummer twee van de Segunda División, waarmee de club na acht jaar terugkeerde in La Liga. De promovendus doet het goed: na zeven duels staat Deportivo zevende.</p>"""

content3 = f"""<h3><strong>Zij verlieten La Liga</strong></h3>
{tabel(["Speler", "Club in La Liga", "Nu"], [
    ("Daley Blind", "Girona", "Ajax"),
    ("Donny van de Beek", "Girona", "Girona (La Liga 2)"),
    ("Teun Gijselhart", "Deportivo La Coruña", "Al Ain (huur)"),
])}
<p>Daley Blind keerde in juli 2026 transfervrij terug bij Ajax, voor zijn derde periode in Amsterdam, en tekende tot medio 2027. Donny van de Beek bleef bij Girona, maar de club degradeerde na het seizoen 2025/26, waardoor hij nu in La Liga 2 speelt. Teun Gijselhart kwam deze zomer nog naar Deportivo La Coruña, maar werd op 16 september voor de rest van het seizoen verhuurd aan Al Ain in de Verenigde Arabische Emiraten.</p>
<h3><strong>La Liga kijken in Nederland</strong></h3>
<p>La Liga is in Nederland te zien bij <a href="/zenders/ziggo-sport">Ziggo Sport</a>; de grote wedstrijden staan meestal op Ziggo Sport 1, dat voor Ziggo-klanten in het tv-pakket zit. Veel wedstrijden zijn daarnaast te volgen via de livestream van <a href="/zenders/toto">TOTO</a>, met een gratis account (18+). Per wedstrijd zie je zender en aftraptijd in ons overzicht van <a href="/nieuws/la-liga-speelronde-8-op-tv-9-oktober-2026">La Liga speelronde 8 op tv</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoeveel Nederlanders spelen er in La Liga?</strong><br>In 2026/27 zijn dat er acht, verdeeld over zes clubs.</p>
<p><strong>Welke club heeft de meeste Nederlanders?</strong><br>Valencia, met Arnaut Danjuma, Justin de Haas en Kayne van Oevelen.</p>
<p><strong>Speelt Denzel Dumfries bij Real Madrid?</strong><br>Ja. Hij kwam in de zomer van 2026 over van Inter en tekende tot medio 2030.</p>
<p><strong>Hoe lang speelt Frenkie de Jong al bij Barcelona?</strong><br>Sinds de zomer van 2019; 2026/27 is zijn achtste seizoen bij de club.</p>
<p><strong>Waar speelt Daley Blind nu?</strong><br>Bij Ajax. Hij keerde in juli 2026 transfervrij terug uit Girona.</p>
<p><em>Gokken is alleen toegestaan voor personen van 18 jaar en ouder. Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_LA_LIGA, "competitie": COMPETITIE_LA_LIGA,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting"); sys.exit()
    print("item:", WF.create_live(fd))
