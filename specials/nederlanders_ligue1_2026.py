# -*- coding: utf-8 -*-
"""Los artikel: Nederlanders in de Ligue 1 2026/27 (selecties gecontroleerd via de voetbal-API, 9 okt 2026).
  python3 specials/nederlanders_ligue1_2026.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Nederlanders in de Ligue 1 2026/27: alle spelers op een rij"
SLUG = "nederlanders-in-de-ligue-1-2026-27"
SAMENVATTING = ("Vier Nederlanders spelen in 2026/27 in de Ligue 1: Teze (Monaco), Kluivert (Lyon), Van den Boomen "
                "(Angers) en De Lange (Marseille). Alle spelers op een rij.")
RUBRIEK_NIEUWS = "651be5190a7dba016817ccf0"
COMPETITIE_LIGUE1 = "65de4c075bc6f2f430bb4ab7"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in koppen)
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}><thead><tr>{kop}</tr></thead><tbody>{body}</tbody></table>"


C = {"monaco": '<a href="/clubs/as-monaco">AS Monaco</a>', "lyon": '<a href="/clubs/lyon">Olympique Lyon</a>',
     "angers": '<a href="/clubs/angers">Angers</a>', "marseille": '<a href="/clubs/marseille">Olympique Marseille</a>'}

content = f"""<p><strong>In het seizoen 2026/27 spelen vier Nederlanders in de Ligue 1: Jordan Teze (AS Monaco), Ruben Kluivert (Olympique Lyon), Branco van den Boomen (Angers) en Jeffrey de Lange (Olympique Marseille). Elk van hen speelt bij een andere club, en drie van de vier zijn verdedigers of keepers.</strong></p>
<p>Frankrijk is geen land waar veel Nederlanders voetballen, zeker niet vergeleken met Engeland, Duitsland of Italië. Wie de <a href="/competities/ligue-1">Ligue 1</a> volgt, komt toch wekelijks een landgenoot tegen, van de nummer één van de ranglijst tot een traditieclub die onderaan staat. Hieronder lees je wie het zijn, hoe ze in Frankrijk terechtkwamen, hoe hun club er nu voor staat en welke Nederlanders de competitie deze zomer verlieten.</p>
<h3><strong>Alle Nederlanders in de Ligue 1 op een rij</strong></h3>
{tabel(["Speler", "Club", "Positie", "Bij de club sinds"], [
    ("Jordan Teze", C["monaco"], "Verdediger", "zomer 2024"),
    ("Ruben Kluivert", C["lyon"], "Verdediger", "zomer 2025"),
    ("Branco van den Boomen", C["angers"], "Middenvelder", "januari 2026 (eerst op huurbasis)"),
    ("Jeffrey de Lange", C["marseille"], "Doelman", "zomer 2024"),
])}
<h3><strong>Zo staan hun clubs ervoor</strong></h3>
<p>Na vijf speelrondes lopen de situaties van de vier clubs flink uiteen. Monaco en Lyon draaien bovenin mee, Marseille beleeft een moeizame seizoensstart.</p>
{tabel(["Club", "Stand", "Punten", "Volgende wedstrijd"], [
    (C["monaco"], "1e", "13", '<a href="/nieuws/as-monaco-toulouse-live-gratis-kijken-10-10-2026">Monaco – Toulouse</a> (za 10 okt, 20:45)'),
    (C["lyon"], "2e", "11", '<a href="/nieuws/lens-lyon-live-gratis-kijken-09-10-2026">Lens – Lyon</a> (vr 9 okt, 20:45)'),
    (C["angers"], "7e", "7", "Brest – Angers (za 10 okt, 20:45)"),
    (C["marseille"], "17e", "3", '<a href="/nieuws/troyes-marseille-live-gratis-kijken-11-10-2026">Troyes – Marseille</a> (zo 11 okt, 20:45)'),
])}
<p><em>Stand na speelronde 5, bijgewerkt op 9 oktober 2026.</em></p>"""

content2 = f"""<h3><strong>Jordan Teze: vaste kracht bij koploper Monaco</strong></h3>
<p>Jordan Teze is de Nederlander met de grootste rol in Frankrijk. De verdediger vertrok in de zomer van 2024 bij PSV naar {C["monaco"]}, waar hij een contract tekende tot medio 2029. Hij speelde vier interlands voor het Nederlands elftal.</p>
<p>In zijn tweede seizoen in het Prinsdom werd Teze een van de spelers op wie de trainer altijd kon rekenen: hij kwam in 2025/26 tot 44 officiële wedstrijden en scoorde vier keer. Zijn kracht is zijn veelzijdigheid. Teze speelt even makkelijk als rechtsback als in het centrum van de defensie, en dat maakt hem voor zijn trainer breed inzetbaar. Dit seizoen begon Monaco als koploper, met vier zeges en een gelijkspel uit de eerste vijf duels.</p>
<h3><strong>Ruben Kluivert: tweede seizoen bij Lyon</strong></h3>
<p>Ruben Kluivert, de jongere broer van Justin en zoon van Patrick, koos in 2025 voor een avontuur in Frankrijk. Hij kwam over van het Portugese Casa Pia en tekende bij {C["lyon"]} een contract tot medio 2030. In zijn eerste seizoen speelde hij 24 officiële wedstrijden, waarvan zestien in de Ligue 1, en scoorde hij twee keer.</p>
<p>Voor Kluivert is 2026/27 het seizoen om zich definitief een basisplaats toe te eigenen. Lyon begon sterk en staat na vijf speelrondes tweede, met nog geen nederlaag.</p>
<h3><strong>Branco van den Boomen: terug in Frankrijk bij Angers</strong></h3>
<p>Geen Nederlander kent het Franse voetbal zo goed als Branco van den Boomen. De middenvelder speelde van 2020 tot 2023 voor Toulouse, promoveerde met die club naar de Ligue 1 en won in 2023 de Coupe de France. Daarna keerde hij terug naar Ajax.</p>
<p>In januari 2026 ging hij opnieuw naar Frankrijk: {C["angers"]} huurde hem voor de tweede seizoenshelft, waarin hij vijftien competitieduels speelde. Beide partijen waren tevreden, dus de transfer werd in de zomer definitief. Van den Boomen ligt nu tot medio 2029 vast. Met zijn passing en spelhervattingen is hij bij Angers een van de spelers die het spel moeten maken.</p>
<h3><strong>Jeffrey de Lange: van stand-in naar de keepersdiscussie in Marseille</strong></h3>
<p>Jeffrey de Lange maakte in 2024 de stap van Go Ahead Eagles naar {C["marseille"]}. Daar stond hij lange tijd in de schaduw van Gerónimo Rulli; in 2025/26 kwam hij vijf keer in actie in de competitie.</p>
<p>Na het vertrek van Rulli in de zomer van 2026 is de keepersvraag in Marseille weer open, en De Lange schoof op in de rangorde. Dat valt samen met een moeilijke periode voor de club: Marseille verloor vier van de eerste vijf duels en staat zeventiende.</p>"""

content3 = f"""<h3><strong>Nederlandse roots, maar geen Oranje-speler</strong></h3>
<p>In de Ligue 1 lopen nog drie spelers rond die in Nederland zijn geboren, maar internationaal voor een ander land uitkomen. Daarom staan ze niet in het overzicht hierboven.</p>
<ul><li><strong>Calvin Verdonk</strong> (<a href="/clubs/lille">Lille</a>): geboren in Dordrecht en lang actief in de Eredivisie, maar international van Indonesië.</li><li><strong>Başar Önal</strong> (Lille): de aanvaller uit Doetinchem kwam via NEC in Frankrijk terecht en speelt voor Turkije Onder 21.</li><li><strong>Safouane Benzahra</strong> (AS Monaco): de Bredanaar zat in de jeugdopleiding van NAC, komt uit voor de Marokkaanse jeugdteams en tekende in september 2026 zijn eerste profcontract bij Monaco.</li></ul>
<h3><strong>Deze Nederlanders verlieten de Ligue 1</strong></h3>
<p>Een seizoen eerder was de Nederlandse groep in Frankrijk nog groter. Drie spelers vertrokken deze zomer.</p>
{tabel(["Speler", "Club in de Ligue 1", "Nu bij"], [
    ("Emanuel Emegha", "Strasbourg", "Chelsea"),
    ("Quinten Timber", "Olympique Marseille", "Crystal Palace"),
    ("Hans Hateboer", "Stade Rennes (verhuurd aan Lyon)", "FC Groningen"),
])}
<p>Emegha groeide in Straatsburg uit tot aanvoerder en spits van de club. Chelsea legde zijn komst al ruim van tevoren vast, waarna hij in de zomer van 2026 naar Londen verhuisde. Quinten Timber speelde slechts een half seizoen in Marseille (vijftien competitiewedstrijden vanaf januari 2026) en tekende op 1 september bij Crystal Palace. Hans Hateboer, die het seizoen 2025/26 op huurbasis bij Lyon speelde, keerde na het aflopen van zijn contract bij Rennes terug naar FC Groningen.</p>
<h3><strong>Ligue 1 kijken in Nederland</strong></h3>
<p>De Ligue 1 is in Nederland te zien bij <a href="/zenders/viaplay">Viaplay</a>. Wil je zien op welke zender en hoe laat de wedstrijden van Teze, Kluivert, Van den Boomen en De Lange worden uitgezonden, kijk dan in ons overzicht van <a href="/nieuws/ligue-1-speelronde-6-op-tv-9-oktober-2026">Ligue 1 speelronde 6 op tv</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoeveel Nederlanders spelen er in de Ligue 1?</strong><br>In het seizoen 2026/27 zijn dat er vier: Jordan Teze, Ruben Kluivert, Branco van den Boomen en Jeffrey de Lange.</p>
<p><strong>Bij welke club speelt Jordan Teze?</strong><br>Bij AS Monaco, waar hij sinds de zomer van 2024 speelt en een contract heeft tot medio 2029.</p>
<p><strong>Speelt Ruben Kluivert in Frankrijk?</strong><br>Ja, de verdediger speelt sinds 2025 voor Olympique Lyon en ligt daar vast tot medio 2030.</p>
<p><strong>Welke Nederlander speelt bij Marseille?</strong><br>Doelman Jeffrey de Lange. Quinten Timber speelde vorig seizoen ook voor Marseille, maar vertrok in september 2026 naar Crystal Palace.</p>
<p><strong>Is Calvin Verdonk een Nederlander?</strong><br>Hij werd in Dordrecht geboren, maar komt internationaal uit voor Indonesië. Hij speelt in de Ligue 1 voor Lille.</p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_NIEUWS, "competitie": COMPETITIE_LIGUE1,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting"); sys.exit()
    print("item:", WF.create_live(fd))
