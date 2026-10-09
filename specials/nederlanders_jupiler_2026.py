# -*- coding: utf-8 -*-
"""Los artikel: Nederlanders in de Jupiler Pro League 2026/27 (nationaliteiten via API-Football, selecties via de
voetbal-API, twijfelgevallen nagezocht; 9 okt 2026).
  python3 specials/nederlanders_jupiler_2026.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Nederlanders in de Jupiler Pro League 2026/27: alle spelers in België"
SLUG = "nederlanders-in-de-jupiler-pro-league-2026-27"
SAMENVATTING = ("Dertien Nederlanders spelen in 2026/27 in de Jupiler Pro League. Lommel United heeft er zes, KV "
                "Mechelen vier. Het complete overzicht per club.")
RUBRIEK_NIEUWS = "651be5190a7dba016817ccf0"
COMPETITIE_JPL = "65de4c16dd6eb829e1867f4b"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in koppen)
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}><thead><tr>{kop}</tr></thead><tbody>{body}</tbody></table>"


C = {"Lommel United": "lommel-united", "KV Mechelen": "kv-mechelen", "Anderlecht": "anderlecht", "KAA Gent": "gent",
     "OH Leuven": "oh-leuven"}
_g = set()


def club(c):
    if c in _g:
        return c
    _g.add(c)
    return f'<a href="/clubs/{C[c]}">{c}</a>'


SPELERS = [
    ("Joey Pelupessy", "Lommel United", "Middenvelder", "32"),
    ("Ralf Seuntjens", "Lommel United", "Aanvaller", "36"),
    ("Tristan Gooijer", "Lommel United", "Verdediger", "21"),
    ("Sam de Grand", "Lommel United", "Verdediger", "21"),
    ("Jason van Duiven", "Lommel United", "Aanvaller", "20"),
    ("Don-Angelo Konadu", "Lommel United", "Aanvaller", "19"),
    ("Mike Eerdhuijzen", "KV Mechelen", "Verdediger", "25"),
    ("Luc Marijnissen", "KV Mechelen", "Verdediger", "22"),
    ("Myron van Brederode", "KV Mechelen", "Aanvaller", "22"),
    ("Bouke Boersma", "KV Mechelen", "Aanvaller", "20"),
    ("Enric Llansana", "Anderlecht", "Middenvelder", "24"),
    ("Aimé Omgba", "KAA Gent", "Middenvelder", "23"),
    ("Dani van den Heuvel", "OH Leuven", "Doelman", "23"),
]
L = "/nieuws/"

content = f"""<p><strong>In het seizoen 2026/27 spelen dertien Nederlanders in de Jupiler Pro League, verdeeld over vijf clubs. Promovendus Lommel United heeft er met zes de meeste, gevolgd door KV Mechelen met vier. Anderlecht (Enric Llansana), KAA Gent (Aimé Omgba) en OH Leuven (Dani van den Heuvel) hebben elk één Nederlander in de selectie.</strong></p>
<p>Voor Nederlandse voetballers is België vaak een logische tussenstap: dezelfde taal in Vlaanderen, een competitie met Europees voetbal en een korte reis naar huis. Opvallend is waar de Nederlanders dit seizoen zitten. Niet bij de topclubs, maar vooral bij Lommel en Mechelen. Hieronder vind je alle Nederlanders in de <a href="/competities/jupiler-pro-league">Jupiler Pro League</a>, hoe hun clubs ervoor staan en welke spelers deze zomer vertrokken.</p>
<h3><strong>Overzicht: Nederlanders in de Jupiler Pro League</strong></h3>
{tabel(["Speler", "Club", "Positie", "Leeftijd"], [(s, club(c), p, a) for s, c, p, a in SPELERS])}
<p><em>Alleen spelers met de Nederlandse voetbalnationaliteit. Selecties en nationaliteiten gecontroleerd op 9 oktober 2026.</em></p>
<h3><strong>Zo staan hun clubs ervoor</strong></h3>
{tabel(["Club", "Nederlanders", "Stand na 7 duels", "Volgende wedstrijd"], [
    ("KAA Gent", "1", "2e (19 pt)", f'<a href="{L}zulte-waregem-gent-live-gratis-kijken-10-10-2026">Zulte Waregem – Gent</a> (za 20:45)'),
    ("Anderlecht", "1", "5e (13 pt)", f'<a href="{L}cercle-brugge-anderlecht-live-gratis-kijken-10-10-2026">Cercle Brugge – Anderlecht</a> (za 16:00)'),
    ("Lommel United", "6", "12e (8 pt)", "SK Beveren – Lommel (vr 20:45)"),
    ("OH Leuven", "1", "15e (4 pt)", f'<a href="{L}union-sint-gilloise-oh-leuven-live-gratis-kijken-11-10-2026">Union – OH Leuven</a> (zo 16:00)'),
    ("KV Mechelen", "4", "18e (3 pt)", "KV Mechelen – Sint-Truiden (zo 19:15)"),
])}"""

content2 = """<h3><strong>Lommel United: een Nederlandse kolonie in Limburg</strong></h3>
<p>Geen club in België heeft zoveel Nederlanders als Lommel United. De promovendus combineert ervaring met jeugd. <strong>Joey Pelupessy</strong> (32) is de leider op het middenveld; de oud-speler van onder meer Heracles Almelo en Sheffield Wednesday brengt veel ervaring mee. Voorin staat de 36-jarige <strong>Ralf Seuntjens</strong>, die in Nederland voor een reeks clubs scoorde en ook op zijn leeftijd nog belangrijk is in de zestien.</p>
<p>Daarnaast heeft Lommel vier jonge Nederlanders: verdedigers <strong>Tristan Gooijer</strong> en <strong>Sam de Grand</strong> (beiden 21) en aanvallers <strong>Jason van Duiven</strong> (20) en <strong>Don-Angelo Konadu</strong> (19). Voor hen is de Jupiler Pro League een kans om op het hoogste Belgische niveau minuten te maken. Lommel staat na zeven speelrondes twaalfde, in de middenmoot.</p>
<h3><strong>KV Mechelen: vier Nederlanders in een lastige start</strong></h3>
<p>KV Mechelen heeft vier landgenoten. Verdediger <strong>Mike Eerdhuijzen</strong> is nieuw: hij kwam deze zomer over van FC Utrecht. Hij vormt samen met <strong>Luc Marijnissen</strong> een Nederlands duo in de verdediging. Voorin spelen <strong>Myron van Brederode</strong>, die via de jeugd van AZ in Mechelen terechtkwam, en de twintigjarige <strong>Bouke Boersma</strong>. De seizoensstart is zwaar: met drie punten uit zeven duels staat Mechelen laatste.</p>
<h3><strong>Llansana, Omgba en Van den Heuvel</strong></h3>
<p><strong>Enric Llansana</strong> werd in Spanje geboren als zoon van een Spaanse vader en een Nederlandse moeder, groeide op in Nederland en kwam uit voor Nederlandse jeugdelftallen. Na de opleiding van Ajax won hij in 2025 met Go Ahead Eagles de KNVB Beker, waarna Anderlecht hem tot 2029 vastlegde. Hij speelt zijn tweede seizoen in Brussel.</p>
<p><strong>Aimé Omgba</strong> verruilde in 2024 NAC Breda voor KAA Gent, waar hij tot medio 2029 vastligt. Gent draait goed mee: na zeven duels staat de club tweede. Doelman <strong>Dani van den Heuvel</strong> uit Delft doorliep de jeugdopleidingen van Ajax en Leeds United en kwam via Club Brugge bij OH Leuven terecht.</p>"""

content3 = f"""<h3><strong>Nederlandse roots, maar geen Nederlandse international</strong></h3>
<p>In de Jupiler Pro League lopen meer spelers met een Nederlandse achtergrond rond. Ze staan niet in het overzicht, omdat ze voor een ander land uitkomen of daar als eerste nationaliteit staan geregistreerd.</p>
<ul><li><strong>Ivan Pavlić</strong> (Union SG): geboren in Rotterdam, opgeleid bij Excelsior en Spartaan, en Belgisch-Nederlands. Hij kwam in 2025 van Paços de Ferreira naar Union.</li><li><strong>Nikki Havenaar</strong> (Union SG): zoon van de Nederlandse keeperstrainer Dido Havenaar, maar geboren in Japan en uitgekomen voor de Japanse jeugdteams.</li><li><strong>Mohammed El Hankouri</strong> (Standard Luik): geboren in Rotterdam, international van Marokko.</li><li><strong>Jearl Margaritha</strong> (SK Beveren): geboren in Groningen, international van Curaçao.</li></ul>
<h3><strong>Zij verlieten de Jupiler Pro League</strong></h3>
{tabel(["Speler", "Club in België", "Nu"], [
    ("Cedric Hatenboer", "Anderlecht", "Sparta Rotterdam"),
    ("Bjorn Meijer", "Club Brugge", "Sampdoria (volgens berichten)"),
])}
<p>Cedric Hatenboer keerde op 31 augustus definitief terug naar Sparta Rotterdam, waar hij tot 2030 tekende. Linksback Bjorn Meijer verliet volgens Italiaanse media Club Brugge voor Sampdoria; een officiële bevestiging van de club hebben we nog niet gezien.</p>
<h3><strong>Jupiler Pro League kijken in Nederland</strong></h3>
<p>Het brede DAZN-pakket met de Jupiler Pro League is in principe alleen in België te koop. In Nederland volg je een groot deel van de wedstrijden via de livestream van <a href="/zenders/711">711</a>, met een gratis account (18+). Welke wedstrijden dit weekend live te zien zijn, staat in ons overzicht van <a href="/nieuws/jupiler-pro-league-speelronde-8-op-tv-9-oktober-2026">Jupiler Pro League speelronde 8 op tv</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoeveel Nederlanders spelen er in de Jupiler Pro League?</strong><br>In 2026/27 zijn dat er dertien, bij vijf clubs.</p>
<p><strong>Welke Belgische club heeft de meeste Nederlanders?</strong><br>Lommel United, met zes Nederlanders, onder wie Joey Pelupessy en Ralf Seuntjens.</p>
<p><strong>Speelt er een Nederlander bij Anderlecht?</strong><br>Ja, middenvelder Enric Llansana. Cedric Hatenboer vertrok op 31 augustus naar Sparta Rotterdam.</p>
<p><strong>Is Nikki Havenaar een Nederlander?</strong><br>Hij heeft een Nederlandse vader, maar werd in Japan geboren en speelde voor de Japanse jeugdteams.</p>
<p><strong>Hoe kijk ik de Jupiler Pro League in Nederland?</strong><br>Vooral via de livestream van 711 met een gratis account; het DAZN-pakket met de Pro League is in principe alleen voor België.</p>
<p><em>Gokken is alleen toegestaan voor personen van 18 jaar en ouder. Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_NIEUWS, "competitie": COMPETITIE_JPL,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting"); sys.exit()
    print("item:", WF.create_live(fd))
