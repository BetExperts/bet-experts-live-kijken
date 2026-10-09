# -*- coding: utf-8 -*-
"""Los artikel: Nederlanders in de Serie A 2026/27 (selecties gecontroleerd via de voetbal-API, 9 okt 2026).
  python3 specials/nederlanders_serie_a_2026.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Nederlanders in de Serie A 2026/27: alle zestien spelers in Italië"
SLUG = "nederlanders-in-de-serie-a-2026-27"
SAMENVATTING = ("Zestien Nederlanders spelen in 2026/27 in de Serie A, bij elf clubs. Roma en Lazio hebben er elk drie, "
                "met onder meer Malen, De Roon en Taylor.")
RUBRIEK_SERIE_A = "66bdfe01e623adcef04827b2"
COMPETITIE_SERIE_A = "65de2f987de877fdf6583d0c"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in koppen)
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}><thead><tr>{kop}</tr></thead><tbody>{body}</tbody></table>"


C = {"AS Roma": "as-roma", "Lazio": "lazio", "Napoli": "napoli", "Juventus": "juventus", "Bologna": "bologna",
     "Como": "como", "Genoa": "genoa", "Lecce": "lecce", "Sassuolo": "sassuolo", "Torino": "torino", "Udinese": "udinese"}
_g = set()


def club(c):
    if c in _g:
        return c
    _g.add(c)
    return f'<a href="/clubs/{C[c]}">{c}</a>'


SPELERS = [
    ("Donyell Malen", "AS Roma", "Aanvaller", "1e"), ("Marten de Roon", "AS Roma", "Middenvelder", "1e"),
    ("Devyne Rensch", "AS Roma", "Verdediger", "1e"),
    ("Kenneth Taylor", "Lazio", "Middenvelder", "3e"), ("Tijjani Noslin", "Lazio", "Aanvaller", "3e"),
    ("Danilho Doekhi", "Lazio", "Verdediger", "3e"),
    ("Teun Koopmeiners", "Juventus", "Middenvelder", "7e"),
    ("Jayden Addai", "Como", "Aanvaller", "8e"),
    ("Sam Beukema", "Napoli", "Verdediger", "9e"), ("Noa Lang", "Napoli", "Aanvaller", "9e"),
    ("Cas Odenthal", "Sassuolo", "Verdediger", "10e"),
    ("Olaf Gorter", "Lecce", "Middenvelder", "12e"),
    ("Jurgen Ekkelenkamp", "Udinese", "Middenvelder", "13e"),
    ("Kian Fitz-Jim", "Torino", "Middenvelder", "14e"),
    ("Jay Enem", "Bologna", "Aanvaller", "18e"),
    ("Justin Bijlow", "Genoa", "Doelman", "19e"),
]

L = "/nieuws/"
content = f"""<p><strong>In het seizoen 2026/27 spelen zestien Nederlanders in de Serie A, verdeeld over elf clubs. De Romeinse clubs AS Roma en Lazio hebben er elk drie: Malen, De Roon en Rensch bij Roma, Taylor, Noslin en Doekhi bij Lazio. Napoli volgt met Sam Beukema en Noa Lang.</strong></p>
<p>Italië is de afgelopen jaren een steeds vaker gekozen bestemming voor Nederlandse voetballers. Het tactische spel en de ruimte voor technische middenvelders passen veel spelers uit de Eredivisie, en dat zie je terug in de <a href="/competities/serie-a">Serie A</a>: van internationals bij de topclubs tot jonge spelers die via een middenmoter hun kans pakken. Hieronder staan ze allemaal, met de positie van hun club op de ranglijst.</p>
<h3><strong>Welke Nederlanders spelen in de Serie A?</strong></h3>
{tabel(["Speler", "Club", "Positie", "Club op de ranglijst"], [(s, club(c), p, st) for s, c, p, st in SPELERS])}
<p><em>Alleen spelers die voor Nederland uitkomen. Selecties en stand gecontroleerd op 9 oktober 2026, na vijf speelrondes.</em></p>
<h3><strong>Drie Nederlandse onderonsjes dit weekend</strong></h3>
<p>Speelronde 6 zit vol duels tussen landgenoten. Wie de Nederlanders in Italië wil volgen, heeft dit weekend genoeg te kijken.</p>
{tabel(["Wedstrijd", "Nederlanders", "Aftrap"], [
    (f'<a href="{L}como-as-roma-live-gratis-kijken-11-10-2026">Como – AS Roma</a>', "Addai tegen Malen, De Roon en Rensch", "zo 11 okt, 12:30"),
    ("Lecce – Bologna", "Gorter tegen Enem", "zo 11 okt, 15:00"),
    ("Torino – Udinese", "Fitz-Jim tegen Ekkelenkamp", "ma 12 okt, 20:45"),
    (f'<a href="{L}genoa-fiorentina-live-gratis-kijken-10-10-2026">Genoa – Fiorentina</a>', "Bijlow", "za 10 okt, 15:00"),
    (f'<a href="{L}napoli-frosinone-live-gratis-kijken-10-10-2026">Napoli – Frosinone</a>', "Beukema, Lang", "za 10 okt, 20:45"),
    (f'<a href="{L}lazio-monza-live-gratis-kijken-11-10-2026">Lazio – Monza</a>', "Taylor, Noslin, Doekhi", "zo 11 okt, 15:00"),
    (f'<a href="{L}sassuolo-ac-milan-live-gratis-kijken-11-10-2026">Sassuolo – AC Milan</a>', "Odenthal", "zo 11 okt, 18:00"),
    (f'<a href="{L}cagliari-juventus-live-gratis-kijken-11-10-2026">Cagliari – Juventus</a>', "Koopmeiners", "zo 11 okt, 20:45"),
])}"""

content2 = """<h3><strong>Rome: zes Nederlanders in één stad</strong></h3>
<p>Nergens in Italië is het Nederlandse accent zo sterk als in Rome. Bij <strong>AS Roma</strong>, dat na vijf speelrondes aan kop gaat, is <strong>Donyell Malen</strong> de blikvanger. De aanvaller kwam in de loop van het seizoen 2025/26 over van Aston Villa en sloeg meteen aan: in de tweede seizoenshelft scoorde hij veertien keer in achttien competitieduels, waarmee hij een grote rol speelde in de derde plaats en het ticket voor de Champions League. <strong>Devyne Rensch</strong> speelt al sinds begin 2025 in Rome, en deze zomer kwam <strong>Marten de Roon</strong> erbij. De middenvelder kent trainer Gian Piero Gasperini van zijn lange periode bij Atalanta.</p>
<p>Stadgenoot <strong>Lazio</strong>, dat met hetzelfde aantal punten derde staat, heeft ook drie Nederlanders. <strong>Kenneth Taylor</strong> zette na zijn jaren bij Ajax de stap naar Italië, <strong>Tijjani Noslin</strong> kwam via Fortuna Sittard en Hellas Verona in Rome terecht, en <strong>Danilho Doekhi</strong> is nieuw: hij kwam deze zomer transfervrij over van Union Berlin. Roma en Lazio delen het Stadio Olimpico, dus in de derby van Rome kunnen straks zes Nederlanders tegenover elkaar staan.</p>
<h3><strong>Koopmeiners, Beukema en Lang bij de traditieclubs</strong></h3>
<p><strong>Teun Koopmeiners</strong> is na zijn succesvolle periode bij Atalanta sinds 2024 speler van Juventus. Bij <strong>Napoli</strong> spelen twee Nederlanders die in 2025 kwamen: verdediger <strong>Sam Beukema</strong> van Bologna en aanvaller <strong>Noa Lang</strong> van PSV.</p>
<h3><strong>De Nederlanders bij de middenmoters</strong></h3>
<p>Een groot deel van de Nederlandse groep speelt bij clubs buiten de top. <strong>Justin Bijlow</strong> staat in het doel bij Genoa, <strong>Jurgen Ekkelenkamp</strong> speelt op het middenveld van Udinese en <strong>Cas Odenthal</strong> verdedigt bij Sassuolo. Bij Lecce staat de jonge middenvelder <strong>Olaf Gorter</strong> onder contract.</p>
<p>Ook <strong>Kian Fitz-Jim</strong> ruilde Ajax in voor Italië en speelt bij Torino. Bij Como staat oud-AZ-aanvaller <strong>Jayden Addai</strong> onder contract. De laatste aanwinst is <strong>Jay Enem</strong>: Bologna haalde de Amsterdamse spits vlak voor het sluiten van de transfermarkt weg bij Rode Ster Belgrado. Enem doorliep eerder de jeugdopleidingen van AZ en Ajax.</p>
<h3><strong>Nederlandse roots, ander land: Kingsley Ehizibue</strong></h3>
<p>Kingsley Ehizibue is geboren en getogen in Nederland en speelde jaren in de Eredivisie, maar komt internationaal uit voor Nigeria. Hij staat daarom niet in het overzicht. Ehizibue speelt overigens wel nog in de Serie A: na vier seizoenen bij Udinese tekende hij op 3 september 2026 als transfervrije speler bij Genoa.</p>"""

content3 = f"""<h3><strong>Vertrokken uit Italië</strong></h3>
{tabel(["Speler", "Club in de Serie A", "Nu"], [
    ("Denzel Dumfries", "Internazionale", "Real Madrid"),
    ("Stefan de Vrij", "Internazionale", "Panathinaikos"),
    ("Thijs Dallinga", "Bologna", "1. FC Köln (huur)"),
    ("Calvin Stengs", "Pisa (huur)", "AZ"),
    ("Mitchel Bakker", "Atalanta", "contract ontbonden"),
    ("Othniël Raterink", "Cagliari", "ADO Den Haag (huur)"),
])}
<p>De grootste vertrekker is Denzel Dumfries, die Inter verruilde voor Real Madrid en daar tot medio 2030 tekende. Ook zijn ploeggenoot Stefan de Vrij vertrok: na twaalf jaar in Italië, bij Lazio en Inter, speelt de verdediger nu voor Panathinaikos in Griekenland. Thijs Dallinga wordt door Bologna verhuurd aan 1. FC Köln. Calvin Stengs keerde na een huurperiode bij Pisa terug naar Feyenoord en tekende later bij AZ. Atalanta en Mitchel Bakker ontbonden op 1 september in goed overleg zijn contract, en Othniël Raterink wordt door Cagliari verhuurd aan ADO Den Haag.</p>
<h3><strong>Serie A kijken in Nederland</strong></h3>
<p>De Serie A is in Nederland te zien bij <a href="/zenders/ziggo-sport">Ziggo Sport</a>. Veel wedstrijden kun je ook volgen via de livestream van <a href="/zenders/bet365">Bet365</a>, met een gestort account (18+). Per wedstrijd zie je de zender en de aftraptijd in ons overzicht van <a href="/nieuws/serie-a-speelronde-6-op-tv-10-oktober-2026">Serie A speelronde 6 op tv</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoeveel Nederlanders spelen er in de Serie A?</strong><br>In 2026/27 zijn dat er zestien, verdeeld over elf clubs.</p>
<p><strong>Welke clubs hebben de meeste Nederlanders?</strong><br>AS Roma en Lazio, met elk drie. Napoli heeft er twee.</p>
<p><strong>Bij welke club speelt Donyell Malen?</strong><br>Bij AS Roma, waar hij in de loop van 2025/26 kwam en in zijn eerste halve seizoen veertien keer scoorde in de competitie.</p>
<p><strong>Speelt Denzel Dumfries nog bij Inter?</strong><br>Nee. Hij vertrok in de zomer van 2026 naar Real Madrid.</p>
<p><strong>Waarom staat Kingsley Ehizibue niet in het overzicht?</strong><br>Hij is in Nederland geboren, maar komt internationaal uit voor Nigeria. Hij speelt bij Genoa.</p>
<p><em>Gokken is alleen toegestaan voor personen van 18 jaar en ouder. Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_SERIE_A, "competitie": COMPETITIE_SERIE_A,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting"); sys.exit()
    print("item:", WF.create_live(fd))
