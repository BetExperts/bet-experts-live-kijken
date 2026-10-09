# -*- coding: utf-8 -*-
"""Los artikel: Nederlanders in de Bundesliga 2026/27 (selecties gecontroleerd via de voetbal-API, 9 okt 2026).
  python3 specials/nederlanders_bundesliga_2026.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Nederlanders in de Bundesliga 2026/27: alle twaalf spelers en hun clubs"
SLUG = "nederlanders-in-de-bundesliga-2026-27"
SAMENVATTING = ("Twaalf Nederlanders spelen in 2026/27 in de Bundesliga, bij acht clubs. Van Veerman (Dortmund) tot "
                "nieuwkomer Van der Leij (Stuttgart): het complete overzicht.")
RUBRIEK_BUNDESLIGA = "66c5a16c2343e9e8d19323a9"
COMPETITIE_BUNDESLIGA = "65eb00d99d1e7b5cb35fe067"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in koppen)
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}><thead><tr>{kop}</tr></thead><tbody>{body}</tbody></table>"


C = {"Borussia Dortmund": "borussia-dortmund", "FC Augsburg": "augsburg", "Bayer Leverkusen": "bayer-leverkusen",
     "Werder Bremen": "werder-bremen", "RB Leipzig": "rb-leipzig", "1. FC Köln": "fc-koln",
     "TSG Hoffenheim": "hoffenheim", "VfB Stuttgart": "stuttgart"}
_g = set()


def club(c):
    if c in _g or c not in C:
        return c
    _g.add(c)
    return f'<a href="/clubs/{C[c]}">{c}</a>'


SPELERS = [
    ("Joey Veerman", "Borussia Dortmund", "Middenvelder", "nieuw (PSV)"),
    ("Jeffrey Gouweleeuw", "FC Augsburg", "Verdediger", "sinds januari 2016"),
    ("Mark Flekken", "Bayer Leverkusen", "Doelman", "sinds zomer 2025"),
    ("Ludovit Reis", "Werder Bremen", "Middenvelder", "nieuw (Club Brugge)"),
    ("Youri Regeer", "Werder Bremen", "Middenvelder", "nieuw (huur van Ajax)"),
    ("Ezechiel Banzuzi", "RB Leipzig", "Middenvelder", "al langer bij de club"),
    ("Thijs Dallinga", "1. FC Köln", "Aanvaller", "nieuw (huur van Bologna)"),
    ("Rav van den Berg", "1. FC Köln", "Verdediger", "sinds 2025/26"),
    ("Wouter Burger", "TSG Hoffenheim", "Middenvelder", "al langer bij de club"),
    ("Mats Rots", "TSG Hoffenheim", "Verdediger", "nieuw (FC Twente)"),
    ("Ramon Hendriks", "VfB Stuttgart", "Verdediger", "sinds zomer 2024"),
    ("Tim van der Leij", "VfB Stuttgart", "Aanvaller", "nieuw (RKC Waalwijk)"),
]

content = f"""<p><strong>Twaalf Nederlanders spelen in het seizoen 2026/27 in de Bundesliga, verdeeld over acht clubs. Joey Veerman (Borussia Dortmund) is de grootste nieuwe naam, Jeffrey Gouweleeuw (FC Augsburg) de veteraan. Köln, Hoffenheim, Werder Bremen en Stuttgart hebben elk twee Nederlanders in de selectie.</strong></p>
<p>Duitsland is van oudsher een logische volgende stap voor Nederlandse voetballers: de <a href="/competities/bundesliga">Bundesliga</a> ligt dichtbij, de stadions zitten vol en clubs durven jonge spelers kansen te geven. Deze zomer kwamen er zes nieuwe Nederlanders bij, terwijl een even grote groep Duitsland verliet. Hieronder staat wie er nu speelt, wie nieuw is en wie je dit weekend tegen elkaar ziet.</p>
<h3><strong>Overzicht: alle Nederlanders in de Bundesliga</strong></h3>
{tabel(["Speler", "Club", "Positie", "Status"], [(s, club(c), p, st) for s, c, p, st in SPELERS])}
<p><em>Alleen spelers die voor Nederland uitkomen. Selecties gecontroleerd op 9 oktober 2026.</em></p>
<h3><strong>Nederlanders dit weekend in actie</strong></h3>
<p>Speelronde 5 brengt meteen een Nederlands onderonsje: Veerman neemt het met Dortmund op tegen het Werder Bremen van Reis en Regeer.</p>
{tabel(["Wedstrijd", "Nederlanders", "Aftrap"], [
    ('<a href="/nieuws/borussia-dortmund-werder-bremen-live-gratis-kijken-09-10-2026">Dortmund – Werder Bremen</a>', "Veerman, Reis, Regeer", "vr 9 okt, 20:30"),
    ('<a href="/nieuws/mainz-05-bayer-leverkusen-live-gratis-kijken-10-10-2026">Mainz – Leverkusen</a>', "Flekken", "za 10 okt, 15:30"),
    ('<a href="/nieuws/augsburg-bayern-munchen-live-gratis-kijken-10-10-2026">Augsburg – Bayern München</a>', "Gouweleeuw", "za 10 okt, 15:30"),
    ('<a href="/nieuws/paderborn-stuttgart-live-gratis-kijken-10-10-2026">Paderborn – Stuttgart</a>', "Hendriks, Van der Leij", "za 10 okt, 15:30"),
    ("Hoffenheim – Hamburger SV", "Burger, Rots", "za 10 okt, 15:30"),
    ('<a href="/nieuws/rb-leipzig-eintracht-frankfurt-live-gratis-kijken-10-10-2026">Leipzig – Frankfurt</a>', "Banzuzi", "za 10 okt, 18:30"),
    ("Köln – Mönchengladbach", "Dallinga, Van den Berg", "zo 11 okt, 15:30"),
])}"""

content2 = """<h3><strong>De nieuwkomers van deze zomer</strong></h3>
<p><strong>Joey Veerman</strong> zette na een succesvolle periode bij PSV, met drie landstitels en twee KNVB Bekers, de stap naar Borussia Dortmund. Hij tekende tot medio 2031. Met zijn passing en spelinzicht moet hij het spel van Dortmund gaan dragen, en de seizoensstart is veelbelovend: Dortmund gaat na vier duels aan kop.</p>
<p><strong>Thijs Dallinga</strong> speelt voor het eerst in Duitsland. Bologna verhuurt de spits voor één seizoen aan 1. FC Köln, waar hij Rav van den Berg als landgenoot treft.</p>
<p>Werder Bremen haalde twee Nederlandse middenvelders. <strong>Ludovit Reis</strong> kwam definitief over van Club Brugge en kent Duitsland al van zijn tijd bij VfL Osnabrück en Hamburger SV. Op de laatste dag van de transferperiode volgde <strong>Youri Regeer</strong>, die Ajax voor één seizoen verhuurt, met een optie tot koop voor Werder.</p>
<p><strong>Mats Rots</strong> ruilde FC Twente in voor TSG Hoffenheim en is daar de nieuwe ploeggenoot van Wouter Burger. En dan is er <strong>Tim van der Leij</strong>: de spits uit Den Bosch, opgeleid bij PSV en Vitesse, maakte furore in de Keuken Kampioen Divisie bij RKC Waalwijk en tekende in juni 2026 bij VfB Stuttgart een contract tot medio 2030. Hij is daarmee een van de opvallendste stappen van de KKD naar de Bundesliga van de afgelopen jaren.</p>
<h3><strong>De vaste krachten</strong></h3>
<p><strong>Jeffrey Gouweleeuw</strong> is de Nederlander met de langste Bundesliga-loopbaan van dit moment. De verdediger kwam in januari 2016 van AZ naar FC Augsburg en is daar uitgegroeid tot clubicoon. Begin 2026 verlengde hij zijn contract tot 30 juni 2027; hij stond toen al op 263 Bundesliga-duels voor de club.</p>
<p><strong>Mark Flekken</strong> speelde eerder al voor Alemannia Aachen, MSV Duisburg en SC Freiburg. Na twee seizoenen bij Brentford in de Premier League haalde Bayer Leverkusen hem in 2025 terug naar Duitsland, voor drie seizoenen.</p>
<p><strong>Wouter Burger</strong> en <strong>Ramon Hendriks</strong> waren vorig seizoen vaste waarden. Burger speelde dertig competitieduels voor Hoffenheim, met vier goals en vijf assists. Hendriks, sinds 2024 bij Stuttgart, kwam tot 31 duels en drie assists. Verder horen <strong>Ezechiel Banzuzi</strong> (RB Leipzig) en <strong>Rav van den Berg</strong> (Köln) bij de Nederlandse groep.</p>
<h3><strong>Nederlandse roots, ander land</strong></h3>
<p>In de Bundesliga spelen ook twee spelers met Nederlandse wortels die internationaal voor een ander land kiezen, en daarom niet in het overzicht staan. Kevin Diks (Borussia Mönchengladbach) komt uit voor Indonesië. Ismael Saibari, die nu bij Bayern München speelt, is international van Marokko.</p>"""

content3 = """<h3><strong>Zij speelden vorig seizoen nog in de Bundesliga</strong></h3>
{vertrek}
<p>Danilho Doekhi liep na vier seizoenen en 137 officiële duels (zestien goals) uit zijn contract bij Union Berlin en tekende voor drie jaar bij Lazio. Ernest Poku, vorig seizoen goed voor vijf goals en vijf assists in 29 duels, wordt door Leverkusen verhuurd aan Beşiktaş. Ayodele Thomas kwam in februari 2026 naar RB Leipzig, maar vertrok zonder Bundesliga-debuut op 1 september naar NEC.</p>
<p>Twee Nederlanders verdwenen niet door een transfer maar door degradatie. VfL Wolfsburg verloor de play-offs van SC Paderborn en St. Pauli degradeerde rechtstreeks; Jenson Seelt (Wolfsburg) en Martijn Kaars (St. Pauli) spelen dit seizoen in de 2. Bundesliga.</p>
<h3><strong>Bundesliga kijken in Nederland</strong></h3>
<p>De Bundesliga is in Nederland te zien bij <a href="/zenders/viaplay">Viaplay</a>. Een groot deel van de wedstrijden kun je daarnaast volgen via de livestream van <a href="/zenders/711">711</a>, met een gratis account (18+). Per wedstrijd zie je zender en aftraptijd in ons overzicht van <a href="/nieuws/bundesliga-speelronde-5-op-tv-9-oktober-2026">Bundesliga speelronde 5 op tv</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoeveel Nederlanders spelen er in de Bundesliga?</strong><br>In 2026/27 zijn dat er twaalf, bij acht verschillende clubs.</p>
<p><strong>Welke Nederlander speelt bij Borussia Dortmund?</strong><br>Joey Veerman, die deze zomer van PSV kwam en tot medio 2031 vastligt.</p>
<p><strong>Welke Nederlanders zijn nieuw in de Bundesliga?</strong><br>Joey Veerman, Thijs Dallinga, Ludovit Reis, Youri Regeer, Mats Rots en Tim van der Leij.</p>
<p><strong>Waarom staan Kevin Diks en Ismael Saibari niet in het overzicht?</strong><br>Ze hebben Nederlandse roots, maar komen uit voor Indonesië (Diks) en Marokko (Saibari).</p>
<p><strong>Waar speelt Danilho Doekhi nu?</strong><br>Bij Lazio in Italië. Zijn contract bij Union Berlin liep af en hij tekende voor drie jaar in Rome.</p>
<p><em>Gokken is alleen toegestaan voor personen van 18 jaar en ouder. Wat kost gokken jou? Stop op tijd. 18+</em></p>""".replace("{vertrek}", tabel(["Speler", "Vorige club", "Nu"], [
    ("Danilho Doekhi", "Union Berlin", "Lazio"),
    ("Ernest Poku", "Bayer Leverkusen", "Beşiktaş (huur)"),
    ("Ayodele Thomas", "RB Leipzig", "NEC"),
    ("Jenson Seelt", "VfL Wolfsburg", "VfL Wolfsburg (2. Bundesliga)"),
    ("Martijn Kaars", "St. Pauli", "St. Pauli (2. Bundesliga)"),
]))

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_BUNDESLIGA, "competitie": COMPETITIE_BUNDESLIGA,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting"); sys.exit()
    print("item:", WF.create_live(fd))
