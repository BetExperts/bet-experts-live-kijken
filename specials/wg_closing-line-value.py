# -*- coding: utf-8 -*-
"""NIEUW wedgids-artikel (Nieuws, nog geen item): wat is closing line value (CLV)?
Slug wat-is-closing-line-value-clv (gaf HTTP 404 op 10-11-2026, dus vrij; ook wat-is-closing-line-value gaf 404).
Rubriek Speluitleg, wedgids-categorie 'Wedstrategieën'. Onderwerp: Engelstalige analysesite (alleen het onderwerp).
Zoekwoorden: 'closing line value' / 'wat is clv' (hoofd), 'closing line betekenis', 'clv berekenen', 'slotkoers wedden',
'line movement', 'steam betekenis wedden', 'odds dalen voor de wedstrijd'.

Afbakening t.o.v. /nieuws/wat-is-de-wedstrategie-value-betting (gelezen met curl op 10-11-2026): daar staat CLV in één
korte paragraaf (voorbeeld 2,30 tegen slotkoers 2,10 = 9,5%, zonder marge-correctie) en 'slotkoers bijhouden' in de
administratietabel. Hier dieper: wat de closing line is, waarom die als scherpste prijs geldt, CLV met en zonder marge
(twee-wegmarkt), negatieve CLV, de valkuil dat eenvoudige CLV positief kan zijn terwijl je onder de eerlijke odd zit,
waarom CLV meer zegt dan een korte winstreeks (exacte binomiale kans + ruis in ROI), line movement en steam, bijhouden van
gemiddelde CLV, grenzen. Andere voorbeelden en getallen dan in het value-artikel.

Feiten nagelopen op 10-11-2026 (bronnen NIET in de tekst genoemd):
- 'De slotkoers is de best geïnformeerde prijs' is de gangbare opvatting onder professionele wedders en in onderzoek, geen
  natuurwet. Onderbouwing: Forrest, Goddard & Simmons (2005), 'Odds-setters as forecasters: the case of English football',
  International Journal of Forecasting (salford-repository.worktribe.com/output/1472154): odds als voorspeller van ruim
  10.000 Engelse duels, steeds beter en niet verslagen door een statistisch model. Kaunitz, Zhong & Kreiner (2017), 'Beating
  the bookies with their own numbers' (arxiv.org/abs/1710.02824): strategie op basis van de impliciete kansen van
  bookmakers zelf (ook met slotkoersen) was winstgevend; de sector reageert met 'discriminatory practices against successful
  clients'. -> In de tekst daarom voorzichtig: 'geldt als', 'meestal', 'in grote, liquide markten'.
- Dat de efficiëntie lager is in kleine markten (spelersmarkten, lagere competities) is algemeen aanvaard, niet met één
  bron hard gemaakt -> kwalitatief geformuleerd.
- Vergunninghouders: Kansspelwijzer Ksa (kansspelautoriteit.nl/kansspelwijzer, stand 21-10-2026 in legaal_data.py, 31
  vergunninghouders): geen wedbeurs (exchange) en geen van de bekende internationale 'scherpe' bookmakers op de lijst ->
  in de tekst: 'die hebben geen Nederlandse vergunning'.
- Bookmakers mogen inzetten per klant beperken: volgens hun voorwaarden (zie value-artikel); hier alleen 'kunnen beperken'.
- Opstellingen in het voetbal: meestal ongeveer een uur voor de aftrap bekend (algemeen bekend) -> 'vaak rond een uur'.
Bewust weggelaten: namen van buitenlandse bookmakers/wedbeurzen (geen NL-vergunning, geen reclame voor illegaal aanbod),
geavanceerde methodes om de marge te verwijderen (power/Shin; noemen voegt voor beginners weinig toe), concrete
CLV-drempels 'die winst garanderen' (bestaan niet), percentages over hoe vaak steam klopt (niet betrouwbaar onderbouwd).
Interne link naar /nieuws/wat-is-expected-value-ev-bij-wedden pas toevoegen als dat artikel live staat (nu 404).
Alle quoteringen en kansen in de voorbeelden zijn fictief; alles hieronder berekend en ge-assert.
Interne links gecontroleerd met curl op 10-11-2026: alle HTTP 200 (zie de asserts).
  ../superodd-agent/.venv/bin/python specials/wg_publiceer.py closing-line-value   (dry run)"""
import os, sys, re
from math import comb, sqrt
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

ITEM_ID = None   # nieuw artikel
SLUG = "wat-is-closing-line-value-clv"
RUBRIEK = "6502b66cd9992658b4037cf5"   # Speluitleg
WEDGIDS_CAT = "Wedstrategieën"
TITEL = "Closing line value (CLV): wat is het en hoe bereken je het?"
SAMENVATTING = ("Wat is closing line value (CLV)? Waarom de slotkoers de scherpste prijs is, hoe je CLV berekent met en "
                "zonder marge, en wat steam betekent.")

OG_KOP = "Wat is <span>closing line value</span>?"
OG_EYEBROW = "CLV en de slotkoers"
OG_CHIPS = ["Met en zonder marge", "Met rekenvoorbeeld"]
OG_MOTIEF = "odds"
OG_DATA = ["Jouw odd · 2,05", "Slotkoers · 1,85", "Eerlijke slotkoers · 1,925", "CLV zonder marge · +6,5%"]

VALUE = "/nieuws/wat-is-de-wedstrategie-value-betting"
ODDS = "/nieuws/odds-uitgelegd-quotering-lezen"
XG = "/nieuws/wat-is-xg-expected-goals"
ARB = "/nieuws/wat-is-arbitrage-wedden-de-kunst-van-de-risicovrije-winst"
LEGAAL = "/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland"
LIMIET = "/nieuws/netto-stortingslimiet"
VERG = "/odds-vergelijken-bij-alle-bookmakers-beste-odds-vandaag"
LINKS = (VALUE, ODDS, XG, ARB, LEGAAL, LIMIET, VERG, "/speel-bewust/verantwoord-wedden", "/wedgids")


def k(x, n=2):
    return f"{x:.{n}f}".replace(".", ",")


def kf(x):
    """Odd met 3 decimalen als dat nodig is (1,925), anders 2 (3,10)."""
    t = f"{x:.3f}"
    return (t[:-1] if t.endswith("0") else t).replace(".", ",")


def pct(x, n=1):
    return f"{100 * x:.{n}f}".replace(".", ",") + "%"


def spct(x, n=1):
    return ("+" if x >= 0 else "−") + pct(abs(x), n)


def eerlijk(o, tegen):
    """Eerlijke kans en odd van o in een twee-wegmarkt (o, tegen), marge proportioneel verwijderd."""
    p = (1 / o) / (1 / o + 1 / tegen)
    return p, 1 / p


# ---- voorbeeld A: over 2,5 op 2,05; slot 1,85 (over) / 2,00 (under) ----
A_ODD, A_SO, A_SU = 2.05, 1.85, 2.00
A_MARGE = 1 / A_SO + 1 / A_SU - 1
A_P, A_FAIR = eerlijk(A_SO, A_SU)
A_CLV_EENV = A_ODD / A_SO - 1
A_CLV = A_ODD / A_FAIR - 1
assert (pct(A_MARGE), pct(A_P), kf(A_FAIR), spct(A_CLV_EENV), spct(A_CLV)) == ("4,1%", "51,9%", "1,925", "+10,8%", "+6,5%")
assert abs(A_CLV - (A_P * A_ODD - 1)) < 1e-12          # CLV zonder marge = EV als de slotkoers klopt
assert k(100 * (A_P - 1 / A_ODD), 1) == "3,2"           # verschil in procentpunten

# ---- voorbeeld B: thuiswinst op 1,95; slot 2,10 / 1,77 (thuis / niet-thuis, twee-weg) ----
B_ODD, B_ST, B_SN = 1.95, 2.10, 1.77
B_P, B_FAIR = eerlijk(B_ST, B_SN)
B_CLV_EENV, B_CLV = B_ODD / B_ST - 1, B_ODD / B_FAIR - 1
assert (kf(B_FAIR), spct(B_CLV_EENV), spct(B_CLV)) == ("2,186", "−7,1%", "−10,8%")

# ---- valkuil: 1,95 genomen, slot 1,90 / 1,90 ----
V_ODD, V_S = 1.95, 1.90
V_P, V_FAIR = eerlijk(V_S, V_S)
assert (k(V_FAIR), spct(V_ODD / V_S - 1), spct(V_ODD / V_FAIR - 1)) == ("2,00", "+2,6%", "−2,5%")

# ---- korte winstreeks: 13 van 20 op 2,00, zonder voordeel (p = 0,5) ----
N_R, W_R, O_R = 20, 13, 2.00
ROI_R = (W_R * (O_R - 1) - (N_R - W_R)) / N_R
KANS_R = sum(comb(N_R, w) for w in range(W_R, N_R + 1)) / 2 ** N_R
assert spct(ROI_R, 0) == "+30%" and pct(KANS_R) == "13,2%"
# ruis in ROI: bij odd 2,00 is de standaardafwijking per weddenschap ongeveer 1 inzet -> 2 sd = 2 / wortel(n)
RUIS = {n: 2 / sqrt(n) for n in (100, 1000)}
assert (pct(RUIS[100], 0), k(100 * RUIS[1000], 1)) == ("20%", "6,3")

# ---- line movement: thuisploeg ----
LIJN = [("Maandag: opening", 2.30), ("Donderdag: spits van de tegenstander geblesseerd", 2.15), ("Zaterdag: opstelling bekend, slotkoers", 2.05)]
SLOT = LIJN[-1][1]
assert [spct(o / SLOT - 1) for _, o in LIJN] == ["+12,2%", "+4,9%", "+0,0%"]
RIJEN_LIJN = [(f"<strong>{t}</strong>" if i == len(LIJN) - 1 else t, k(o), spct(o / SLOT - 1) if i < len(LIJN) - 1 else "–")
              for i, (t, o) in enumerate(LIJN)]

# ---- logboek: vijf weddenschappen, eerlijke slotkoers (marge al verwijderd) ----
LOG = [("Over 2,5 goals", A_ODD, A_FAIR, "Verloren"), ("Thuiswinst", B_ODD, B_FAIR, "Gewonnen"),
       ("Uitwinst", 3.40, 3.10, "Verloren"), ("Beide teams scoren", 1.80, 1.74, "Gewonnen"), ("Gelijkspel", 2.50, 2.62, "Verloren")]
CLVS = [o / s - 1 for _, o, s, _ in LOG]
GEM = sum(CLVS) / len(CLVS)
assert [spct(c) for c in CLVS] == ["+6,5%", "−10,8%", "+9,7%", "+3,4%", "−4,6%"] and spct(GEM) == "+0,8%"
RIJEN_LOG = [(m, k(o), kf(s), spct(c), u) for (m, o, s, u), c in zip(LOG, CLVS)]

content = f"""<p><strong>Closing line value (CLV) is het verschil tussen de odd waarop jij hebt ingezet en de slotkoers: de laatste odd vlak voor de aftrap. Je berekent het als jouw odd ÷ slotkoers − 1, het liefst met de marge uit de slotkoers gehaald. Haal je structureel een hogere odd dan de slotkoers, dan is dat een sterk teken dat je echt value vindt, ook als je resultaten tijdelijk tegenvallen. Een garantie op winst is het niet.</strong></p>
<p>In ons artikel over <a href="{VALUE}">value betting</a> kwam CLV al kort aan bod. Hier lees je het hele verhaal: wat de closing line is, waarom die als de scherpste prijs geldt, hoe je CLV met en zonder marge berekent, wat line movement en steam zijn en waar het begrip ophoudt. <em>Alle quoteringen in de voorbeelden zijn fictief.</em></p>
<h3><strong>Wat is de closing line?</strong></h3>
<p>Een odd staat niet stil. Een bookmaker opent een markt dagen voor de wedstrijd met een openingskoers en past die daarna steeds aan. De <strong>closing line</strong> of slotkoers is de odd op het moment dat de markt vóór de wedstrijd sluit, meestal bij de aftrap. Daarna begint live wedden, met odds die met de stand meebewegen; die tellen niet mee.</p>
<p>Tussen opening en slot verandert er veel. Er komt nieuws over blessures en schorsingen, de opstellingen worden bekend (in het voetbal vaak rond een uur voor de aftrap) en er wordt geld ingezet, ook door wedders die er veel verstand van hebben. Elke keer dat de bookmaker daarop reageert, schuift de odd een stukje.</p>
<h3><strong>Waarom geldt de slotkoers als de scherpste prijs?</strong></h3>
<p>Vlak voor de aftrap is alle informatie verwerkt die er vooraf te krijgen is. Bovendien laten bookmakers in grote markten de hoogste inzetten toe vlak voor de wedstrijd, dus dan weegt het geld van goed geïnformeerde wedders het zwaarst. De slotkoers is zo een soort samenvatting van alles wat de markt weet.</p>
<p>Daarom gebruiken onderzoekers en professionele wedders de slotkoers, met de marge eruit gehaald, als beste schatting van de echte kans. Dat is geen wet: de slotkoers zit er bij een losse wedstrijd ook vaak naast. Maar gemiddeld over veel wedstrijden is het in grote, drukbezochte markten moeilijk om hem structureel te verslaan. Hoe kleiner en stiller de markt, hoe minder scherp de slotkoers. Denk aan lagere competities, vrouwenvoetbal of spelersmarkten zoals schoten op doel.</p>
<h3><strong>Hoe bereken je CLV?</strong></h3>
<p>Er zijn twee manieren. De eenvoudige vergelijkt jouw odd met de slotkoers zoals de bookmaker hem toont. De nauwkeurige vergelijkt jouw odd met de <strong>eerlijke slotkoers</strong>, dus zonder marge.</p>
<ul><li><strong>Eenvoudige CLV</strong> = jouw odd ÷ slotkoers − 1</li><li><strong>CLV zonder marge</strong> = jouw odd ÷ eerlijke slotkoers − 1</li></ul>
<p>De eerlijke slotkoers vind je door de marge uit de markt te halen: deel de impliciete kans van jouw uitkomst door de som van alle impliciete kansen. Hoe dat werkt, staat stap voor stap in <a href="{ODDS}">odds uitgelegd</a>.</p>
<p><strong>Rekenvoorbeeld:</strong> op dinsdag zet je in op meer dan 2,5 doelpunten tegen {k(A_ODD)}. Bij de aftrap staat over 2,5 op {k(A_SO)} en under 2,5 op {k(A_SU)}.</p>
{tabel(["Stap", "Berekening", "Uitkomst"], [
    ("Marge van de slotmarkt", f"1 ÷ {k(A_SO)} + 1 ÷ {k(A_SU)} − 1", pct(A_MARGE)),
    ("Eerlijke kans op over 2,5", f"(1 ÷ {k(A_SO)}) ÷ {k(1 + A_MARGE, 4)}", pct(A_P)),
    ("Eerlijke slotkoers", f"1 ÷ {k(A_P, 4)}", kf(A_FAIR)),
    ("Eenvoudige CLV", f"{k(A_ODD)} ÷ {k(A_SO)} − 1", spct(A_CLV_EENV)),
    ("<strong>CLV zonder marge</strong>", f"{k(A_ODD)} ÷ {kf(A_FAIR)} − 1", f"<strong>{spct(A_CLV)}</strong>"),
])}
<p>De eenvoudige CLV van {spct(A_CLV_EENV)} overdrijft je voordeel, want een deel van het verschil is gewoon de marge van de bookmaker. De CLV zonder marge, {spct(A_CLV)}, is eerlijker. Als de slotkoers de echte kans goed weergeeft, is dit ook je verwachte rendement op deze weddenschap. In kansen uitgedrukt: jij kreeg een odd die bij {pct(1 / A_ODD)} kans hoort, terwijl de markt bij de aftrap {pct(A_P)} rekende.</p>
<p>Het kan ook andersom. Zet je in op een thuiszege tegen {k(B_ODD)} en sluit de markt op {k(B_ST)} voor thuis en {k(B_SN)} voor de andere kant, dan is de eerlijke slotkoers {kf(B_FAIR)}. Je CLV is {spct(B_CLV)}: de markt vond jouw keuze bij de aftrap minder kansrijk dan toen jij instapte.</p>"""

content2 = f"""<h3><strong>Waarom zegt CLV meer dan een winstreeks?</strong></h3>
<p>Uitslagen zijn grillig. Stel: je wint 13 van je 20 weddenschappen tegen {k(O_R)}. Dat is een rendement van {spct(ROI_R, 0)} en voelt als bewijs dat je het kunt. Maar iemand die zonder enig voordeel inzet, haalt zo'n reeks of beter in {pct(KANS_R)} van de gevallen, ongeveer één op de acht. Twintig weddenschappen zeggen dus bijna niets.</p>
<p>Ook over langere periodes blijft het rendement onrustig. Bij odds rond {k(O_R)} ligt je resultaat na 100 weddenschappen door puur toeval nog zo'n {k(100 * RUIS[100], 0)} procentpunt boven of onder je echte voordeel. Na 1.000 weddenschappen is dat nog ongeveer {k(100 * RUIS[1000], 1)} procentpunt. Een echt voordeel van een paar procent is daarin lastig te zien.</p>
<p>CLV heeft dat probleem veel minder. Je kunt het meten zodra de wedstrijd begint, los van de uitslag, en het verschil tussen jouw odd en de slotkoers is meestal een paar procent in plaats van de hele inzet. Daardoor zie je na tientallen tot honderden weddenschappen al of je structureel boven de slotkoers zit. Wie dat jarenlang doet, wint in de regel ook op de lange termijn. Wie structureel onder de slotkoers zit, verliest meestal, hoe mooi een reeks ook was.</p>
<h3><strong>Wat is line movement en wat is steam?</strong></h3>
<p><strong>Line movement</strong> is elke verandering van de odds tussen opening en aftrap. Zakt de odd van een uitkomst, dan vinden de bookmakers die uitkomst kansrijker of ze krijgen er veel geld op. Een voorbeeld van een thuisploeg in de loop van de week:</p>
{tabel(["Moment", "Odd thuiswinst", "Eenvoudige CLV bij instap"], RIJEN_LIJN)}
<p>Wie op maandag instapte, zit {spct(LIJN[0][1] / SLOT - 1)} boven de slotkoers; wie na het blessurenieuws instapte, nog {spct(LIJN[1][1] / SLOT - 1)}. Let op: dit is de eenvoudige CLV, met de marge er nog in.</p>
<p><strong>Steam</strong> is een plotselinge, snelle beweging die bij veel bookmakers tegelijk gebeurt, meestal omdat er in korte tijd veel geld van goed geïnformeerde wedders op één kant komt. Steam vertelt je dat de markt iets heeft opgepikt. Erachteraan jagen is lastig: als jij de beweging ziet, hebben de meeste bookmakers hun odds vaak al aangepast. En niet elke beweging is slim geld. Bij populaire clubs zakt een odd soms alleen omdat veel fans erop inzetten.</p>"""

content3 = f"""<h3><strong>Hoe houd je je CLV bij?</strong></h3>
<p>Noteer bij elke weddenschap je odd en, vlak voor de aftrap, de slotkoers van dezelfde markt. Haal de marge eruit en reken per weddenschap je CLV uit. Kijk daarna naar het gemiddelde, niet naar losse uitschieters:</p>
{tabel(["Weddenschap", "Jouw odd", "Eerlijke slotkoers", "CLV", "Uitslag"], RIJEN_LOG + [("<strong>Gemiddeld</strong>", "", "", f"<strong>{spct(GEM)}</strong>", "")])}
<p>Drie van de vijf weddenschappen gingen verloren, maar de gemiddelde CLV is licht positief. Andersom kan ook: een winnende week met negatieve CLV. Pas over minstens honderd weddenschappen wordt het gemiddelde betrouwbaar.</p>
<p>Welke slotkoers neem je? Hoe meer bookmakers je meeneemt, hoe beter. Een gemiddelde van meerdere legale Nederlandse bookmakers, met de marge eruit, is een redelijk ijkpunt; onze <a href="{VERG}">odds vergelijker</a> helpt daarbij. Internationaal worden vaak de odds van wedbeurzen en zogeheten scherpe bookmakers als maatstaf gebruikt, maar die hebben geen Nederlandse vergunning. Daar spelen is illegaal en je hebt er geen bescherming; lees <a href="{LEGAAL}">hoe je een legale bookmaker herkent</a>.</p>
<h3><strong>Wat zijn de grenzen van CLV?</strong></h3>
<ul><li><strong>Eenvoudige CLV kan misleiden.</strong> Zet je in op {k(V_ODD)} en sluit de markt op {k(V_S)} voor beide kanten, dan lijkt je CLV {spct(V_ODD / V_S - 1)}. De eerlijke slotkoers is echter {k(V_FAIR)}, dus zonder marge is je CLV {spct(V_ODD / V_FAIR - 1)}. Je kreeg een betere odd dan de slotkoers, maar nog steeds een lagere dan de eerlijke odd.</li><li><strong>De slotkoers is ook maar een schatting.</strong> In kleine markten kan één grote inzet de slotkoers verschuiven zonder dat er iets aan de kansen is veranderd.</li><li><strong>CLV vervangt geen rendement.</strong> Uiteindelijk telt wat je wint of verliest. CLV is een vroege meter, geen eindcijfer.</li><li><strong>Geen slotkoers bij live wedden.</strong> Voor weddenschappen tijdens de wedstrijd bestaat geen vergelijkbare slotkoers.</li><li><strong>Vroeg instappen heeft een prijs.</strong> De meeste CLV haal je vaak ver voor de wedstrijd, als er nog weinig bekend is. Dan loop je ook het risico dat een speler toch niet speelt.</li><li><strong>Bookmakers letten er ook op.</strong> Wie structureel de slotkoers verslaat, kan merken dat de bookmaker de maximale inzet verlaagt.</li></ul>
<p>Wil je zelf kansen inschatten om eerder dan de markt te zijn, dan helpen modellen op basis van <a href="{XG}">expected goals (xG)</a>. Wil je juist geen risico op de uitslag, lees dan over <a href="{ARB}">arbitrage wedden</a>. Welke strategie je ook kiest: zet alleen in wat je kunt missen, stel een <a href="{LIMIET}">netto-stortingslimiet</a> in en lees onze tips over <a href="/speel-bewust/verantwoord-wedden">verantwoord wedden</a>. Meer uitleg vind je in de <a href="/wedgids">wedgids</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wat betekent closing line value?</strong><br>Closing line value (CLV) is hoeveel beter of slechter jouw odd was dan de slotkoers vlak voor de aftrap. Positieve CLV betekent dat je een hogere odd kreeg dan de markt uiteindelijk gaf.</p>
<p><strong>Hoe bereken ik CLV?</strong><br>Jouw odd ÷ slotkoers − 1. Nauwkeuriger is het om eerst de marge uit de slotkoers te halen. Voorbeeld: {k(A_ODD)} tegen een eerlijke slotkoers van {kf(A_FAIR)} is {spct(A_CLV)}.</p>
<p><strong>Wat is een goede CLV?</strong><br>Elke gemiddelde CLV boven nul, zonder marge gemeten en over honderden weddenschappen, is een goed teken. Een paar procent gemiddeld is al veel. Een paar weddenschappen met hoge CLV zeggen weinig.</p>
<p><strong>Betekent positieve CLV dat ik winst maak?</strong><br>Nee, niet gegarandeerd. Op korte termijn kun je met positieve CLV verliezen, en de slotkoers is zelf ook een schatting. Het is wel een van de beste aanwijzingen dat je op lange termijn waarde vindt.</p>
<p><strong>Wat betekent steam bij wedden?</strong><br>Steam is een snelle, plotselinge daling van een odd bij veel bookmakers tegelijk, meestal door veel geld van goed geïnformeerde wedders op één uitkomst.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    html = content + content2 + content3
    assert re.search(r"<(ul|ol|/li)>\s+<", html) is None
    assert "/kennisbank/" not in html and "<h2" not in html and "<h4" not in html and "/go/" not in html
    assert html.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert content.startswith("<p><strong>")
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert len(OG_CHIPS) == 2 and len(OG_DATA) == 4
    for link in LINKS:
        assert f'href="{link}"' in html, link
    assert set(re.findall(r'href="([^"]+)"', html)) <= set(LINKS)
    faq = content3.split("Veelgestelde vragen")[1]
    assert 4 <= faq.count("<p><strong>") <= 6
    woorden = len(re.sub(r"<[^>]+>", " ", html).split())
    assert 1200 <= woorden <= 2200, woorden
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", woorden, "woorden")
