# -*- coding: utf-8 -*-
"""Los artikel: Nederlanders in de Premier League 2026/27 (selecties gecontroleerd via de voetbal-API, 9 okt 2026).
  python3 specials/nederlanders_premier_league_2026.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Nederlanders in de Premier League 2026/27: alle 32 spelers op een rij"
SLUG = "nederlanders-in-de-premier-league-2026-27"
SAMENVATTING = ("32 Nederlanders spelen in 2026/27 in de Premier League, verdeeld over 15 clubs. Liverpool heeft er "
                "met Van Dijk, Gakpo, Gravenberch en Frimpong de meeste.")
RUBRIEK_PL = "66a266c00edad587814b64b9"
COMPETITIE_PL = "65de4d0c4b5e9d86b7abf7e4"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in koppen)
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}><thead><tr>{kop}</tr></thead><tbody>{body}</tbody></table>"


CLUB = {"Arsenal": "arsenal", "Aston Villa": "aston-villa", "Bournemouth": "bournemouth", "Brentford": "brentford",
        "Brighton & Hove Albion": "brighton", "Chelsea": "chelsea", "Coventry City": "coventry",
        "Crystal Palace": "crystal-palace", "Fulham": "fulham", "Ipswich Town": "ipswich-town",
        "Liverpool": "liverpool", "Manchester United": "manchester-united", "Newcastle United": "newcastle-united",
        "Sunderland": "sunderland", "Tottenham Hotspur": "tottenham"}
SPELERS = [
    ("Jurriën Timber", "Arsenal", "Verdediger"),
    ("Marco Bizot", "Aston Villa", "Doelman"), ("Lamare Bogarde", "Aston Villa", "Middenvelder"),
    ("Ian Maatsen", "Aston Villa", "Verdediger"),
    ("Justin Kluivert", "Bournemouth", "Aanvaller"),
    ("Sepp van den Berg", "Brentford", "Verdediger"), ("Antoni Milambo", "Brentford", "Middenvelder"),
    ("Bart Verbruggen", "Brighton & Hove Albion", "Doelman"), ("Pascal Struijk", "Brighton & Hove Albion", "Verdediger"),
    ("Mats Wieffer", "Brighton & Hove Albion", "Middenvelder"),
    ("Emmanuel Emegha", "Chelsea", "Aanvaller"), ("Jorrel Hato", "Chelsea", "Verdediger"),
    ("Milan van Ewijk", "Coventry City", "Verdediger"), ("Gustavo Hamer", "Coventry City", "Middenvelder"),
    ("Quinten Timber", "Crystal Palace", "Middenvelder"),
    ("Kenny Tete", "Fulham", "Verdediger"),
    ("Azor Matusiwa", "Ipswich Town", "Middenvelder"), ("Zian Flemming", "Ipswich Town", "Aanvaller"),
    ("Kjell Scherpen", "Ipswich Town", "Doelman"),
    ("Virgil van Dijk", "Liverpool", "Verdediger"), ("Ryan Gravenberch", "Liverpool", "Middenvelder"),
    ("Jeremie Frimpong", "Liverpool", "Verdediger"), ("Cody Gakpo", "Liverpool", "Aanvaller"),
    ("Matthijs de Ligt", "Manchester United", "Verdediger"), ("Joshua Zirkzee", "Manchester United", "Aanvaller"),
    ("Sven Botman", "Newcastle United", "Verdediger"), ("Sean Steur", "Newcastle United", "Middenvelder"),
    ("Robin Roefs", "Sunderland", "Doelman"), ("Brian Brobbey", "Sunderland", "Aanvaller"),
    ("Jan Paul van Hecke", "Tottenham Hotspur", "Verdediger"), ("Micky van de Ven", "Tottenham Hotspur", "Verdediger"),
    ("Xavi Simons", "Tottenham Hotspur", "Middenvelder"),
]
STAND = {"Arsenal": 2, "Brighton & Hove Albion": 3, "Brentford": 4, "Liverpool": 6, "Newcastle United": 9, "Chelsea": 10,
         "Ipswich Town": 11, "Manchester United": 12, "Sunderland": 14, "Crystal Palace": 15, "Aston Villa": 16,
         "Bournemouth": 17, "Coventry City": 18, "Fulham": 19, "Tottenham Hotspur": 20}

gelinkt = set()


def club(c):
    if c in gelinkt:
        return c
    gelinkt.add(c)
    return f'<a href="/clubs/{CLUB[c]}">{c}</a>'


rijen = [(s, club(c), p) for s, c, p in SPELERS]
per_club = {}
for s, c, p in SPELERS:
    per_club.setdefault(c, []).append(s)
club_rijen = [(c, str(len(v)), f"{STAND[c]}e") for c, v in sorted(per_club.items(), key=lambda x: (-len(x[1]), STAND[x[0]]))]

content = f"""<p><strong>In het seizoen 2026/27 spelen 32 Nederlanders in de Premier League, verdeeld over vijftien clubs. Liverpool heeft er met Virgil van Dijk, Cody Gakpo, Ryan Gravenberch en Jeremie Frimpong de meeste. Aston Villa, Brighton, Ipswich Town en Tottenham Hotspur volgen met elk drie Nederlanders.</strong></p>
<p>Geen buitenlandse competitie is zo populair bij Nederlandse voetballers als de <a href="/competities/premier-league">Premier League</a>. Van de aanvoerder van Liverpool tot een keeper bij een promovendus: bijna elke speelronde staan er meerdere landgenoten tegenover elkaar. In dit overzicht vind je alle Nederlanders per club, hoe hun ploegen ervoor staan en wie Engeland deze zomer verliet.</p>
<h3><strong>Alle Nederlanders in de Premier League 2026/27</strong></h3>
{tabel(["Speler", "Club", "Positie"], rijen)}
<p><em>In dit overzicht staan spelers die voor Nederland uitkomen en tot de selectie van een Premier League-club behoren, inclusief spelers onder 21 jaar. Selecties gecontroleerd op 9 oktober 2026.</em></p>
<h3><strong>Aantal Nederlanders per club</strong></h3>
{tabel(["Club", "Nederlanders", "Stand na 5 duels"], club_rijen)}"""

content2 = """<h3><strong>Liverpool: vier Nederlanders op Anfield</strong></h3>
<p>Nergens in Engeland is de Nederlandse inbreng zo groot als bij Liverpool. Virgil van Dijk is al jaren de aanvoerder en geldt als een van de beste verdedigers in de geschiedenis van de club. Cody Gakpo is inmiddels een vaste waarde in de aanval, Ryan Gravenberch groeide uit tot een van de belangrijkste middenvelders van de ploeg en sinds 2025 zorgt Jeremie Frimpong voor snelheid langs de rechterkant. Liverpool staat na vijf speelrondes zesde.</p>
<h3><strong>Tottenham: drie Oranje-internationals in Noord-Londen</strong></h3>
<p>Tottenham Hotspur heeft een stevige Nederlandse ruggengraat. Micky van de Ven en Xavi Simons speelden al voor de club, en in juni 2026 kwam Jan Paul van Hecke over van Brighton. Daarmee staan er twee Nederlandse centrale verdedigers in de selectie. De seizoensstart is wel zwaar: na vijf duels staat Tottenham onderaan.</p>
<h3><strong>Brighton, Aston Villa en Ipswich: elk drie Nederlanders</strong></h3>
<p>Brighton &amp; Hove Albion blijft een geliefde club voor Nederlandse spelers. Keeper Bart Verbruggen en middenvelder Mats Wieffer kregen deze zomer gezelschap van Pascal Struijk, die van Leeds United kwam en een contract voor vijf seizoenen tekende. Brighton staat derde en is daarmee de best presterende club met meerdere Nederlanders.</p>
<p>Bij Aston Villa spelen doelman Marco Bizot, Lamare Bogarde en Ian Maatsen. Ipswich Town heeft met keeper Kjell Scherpen, middenvelder Azor Matusiwa en aanvaller Zian Flemming ook drie Nederlanders in de selectie.</p>
<h3><strong>Chelsea, Manchester United, Newcastle en Sunderland</strong></h3>
<p>Bij Chelsea speelt Emmanuel Emegha, die deze zomer na zijn periode als aanvoerder van Strasbourg naar Londen kwam, samen met verdediger Jorrel Hato. Manchester United heeft Joshua Zirkzee en Matthijs de Ligt in de selectie; De Ligt werkt na een rugoperatie aan zijn rentree.</p>
<p>Newcastle United combineert ervaring en talent: Sven Botman speelt er al jaren, terwijl de 17-jarige Sean Steur uit de jeugdopleiding van Ajax overkwam. Bij Sunderland staan keeper Robin Roefs en spits Brian Brobbey samen onder contract.</p>
<h3><strong>De andere Nederlanders</strong></h3>
<p>Coventry City heeft met Milan van Ewijk en Gustavo Hamer twee Nederlanders. Bij Brentford spelen Sepp van den Berg en Antoni Milambo, die terugkomt van een zware knieblessure. Jurriën Timber (Arsenal), Justin Kluivert (Bournemouth), Quinten Timber (Crystal Palace) en Kenny Tete (Fulham) zijn de enige Nederlander bij hun club. Opvallend: de tweelingbroers Timber spelen allebei in Londen, Jurriën bij koploperskandidaat Arsenal en Quinten sinds september bij Crystal Palace.</p>
<h3><strong>Waarom staan er ook spelers onder 21 in het overzicht?</strong></h3>
<p>Elke Premier League-club mag 25 spelers boven de 21 jaar registreren. Jongere spelers vallen daarbuiten en mogen zonder die registratie gewoon in de competitie spelen. Daardoor kunnen clubs talenten als Sean Steur bij Newcastle meteen laten debuteren, zonder dat dit ten koste gaat van een plek in de selectie van 25.</p>"""

content3 = """<h3><strong>Deze Nederlanders vertrokken uit de Premier League</strong></h3>
<p>Tegenover de nieuwkomers staan ook een paar bekende vertrekkers. Nathan Aké verliet Manchester City na zes seizoenen en speelt nu voor Fenerbahçe in Turkije. Het contract van Tyrell Malacia bij Manchester United liep in de zomer van 2026 af, waarna hij uit de Premier League vertrok.</p>
<h3><strong>Premier League kijken in Nederland</strong></h3>
<p>De Premier League is in Nederland te zien bij <a href="/zenders/viaplay">Viaplay</a>. Eén wedstrijd per speelronde, meestal op zaterdag om 13:30 uur, zendt <a href="/zenders/prime-video">Prime Video</a> uit. Welke wedstrijden met Nederlanders je dit weekend waar kunt zien, staat in ons overzicht van <a href="/nieuws/premier-league-speelronde-6-op-tv-10-oktober-2026">Premier League speelronde 6 op tv</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoeveel Nederlanders spelen er in de Premier League?</strong><br>In het seizoen 2026/27 zijn dat er 32, verdeeld over vijftien clubs.</p>
<p><strong>Welke club heeft de meeste Nederlanders?</strong><br>Liverpool, met Virgil van Dijk, Cody Gakpo, Ryan Gravenberch en Jeremie Frimpong.</p>
<p><strong>Bij welke club speelt Xavi Simons?</strong><br>Bij Tottenham Hotspur, samen met Micky van de Ven en Jan Paul van Hecke.</p>
<p><strong>Speelt Nathan Aké nog in Engeland?</strong><br>Nee. Hij verliet Manchester City in de zomer van 2026 en speelt nu voor Fenerbahçe.</p>
<p><strong>Waarom staat Sean Steur in het overzicht?</strong><br>Hij hoort bij de selectie van Newcastle United. Als speler onder 21 jaar telt hij niet mee voor de limiet van 25 spelers, maar hij mag wel in de Premier League spelen.</p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_PL, "competitie": COMPETITIE_PL,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting", len(SPELERS), "spelers", len(per_club), "clubs"); sys.exit()
    print("item:", WF.create_live(fd))
