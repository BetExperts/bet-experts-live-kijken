# -*- coding: utf-8 -*-
"""Los artikel (evergreen): FIFA-ranking Nederland, waar staat Oranje? Stand: ranking van 7-10-2026, geschreven 9-11-2026.

BIJWERKEN NA ELKE NIEUWE RANKING (eerstvolgende: NA_PUBLICATIE = 18-11-2026):
  1. PUBLICATIE / VORIGE_PUBLICATIE aanpassen;
  2. RANKING (top 10) en EXTRA (België, Duitsland, ...) vervangen: (plek, land, slug, punten, vorige plek, vorige punten);
  3. ORANJE_DUELS vervangen door de duels uit het nieuwe venster; NOVEMBER/VOLGENDE_DUELS en de november-alinea's herschrijven;
  4. NA_PUBLICATIE op de datum van de volgende ranking zetten (fifa.com, 'Next official update');
  5. dry run draaien en de kaart opnieuw renderen.

Bronnen (allemaal gecontroleerd op 9-11-2026):
- FIFA, actuele ranking: https://inside.fifa.com/fifa-rankings/world-ranking/men ('Last official update: 07 October 2026',
  'Next official update: 18 November 2026'); top 10 en punten afgelezen in de volledige tabel (nog geen duels gespeeld in het
  novembervenster, dat volgens /api/live-world-ranking/get-international-ranking-window loopt van 8 t/m 18 november 2026).
- FIFA, vorige editie 20-07-2026: /api/ranking-overview?locale=en&dateId=id15175 (plekken en punten per land).
- FIFA-nieuws 7-10-2026: https://inside.fifa.com/news/coca-cola-mens-world-ranking-october-2026-portugal-spain
  (Portugal +2 naar 5e, enige stijger in top 10; Brazilië 6e, Marokko 7e; Duitsland 13e na inhaalslag Zwitserland; Griekenland 41e).
- FIFA, punten per duel van Oranje: /api/live-world-ranking/get-match-window-matches (TeamAPointsBefore/After); de vier
  Nations League-duels en de WK-duels tegen Tunesië (1-3) en Marokko (1-1, 2-3 na strafschoppen, 1/16e finale).
- FIFA, historie Oranje: /api/rankings/by-country?gender=1&countryCode=NED (hoogste plek 1 op 24-08-2011, laagste 36 op
  10-08-2017; 7e op 19-11-2025, 8e op 11-06-2026, 9e op 20-07-2026); landenpagina: hoogste 1e, laagste 36e, gemiddeld 9e.
- FIFA-methodiek (pdf 'Revision of the FIFA/Coca-Cola World Ranking'):
  https://digitalhub.fifa.com/m/f99da4f73212220/original/edbm045h0udbwkqew35a-pdf.pdf (formule, I-waarden, strafschoppen,
  knock-outregel). Nagerekend: Servië – Nederland 1-2 met I=15 geeft exact +3,81 (zie dry run).
- UEFA EK-reglement 2026-28, art. 13.02: potten EK-kwalificatie op 'interim overall 2026/27 UEFA Nations League rankings':
  https://documents.uefa.com/r/Regulations-of-the-UEFA-European-Football-Championship-2026-28/Article-13-Group-formation-qualifying-group-stage-Online
- Loting EK-kwalificatie 6-12-2026 Belfast: specials/nations_league_2028_feiten.md (UEFA 15-09-2026).
- WK-loting 2026: pot 1 = drie gastlanden + beste negen van de FIFA-ranking van november 2025 (o.a. VI, FCUpdate; Oranje in pot 1).
- WK-kwalificatie 2026 (loting dec. 2024): potten op FIFA-ranking november 2024, Nations League-kwartfinalisten in pot 1
  (theScore, Flashscore).
- Odds: 711 (Kambi sevelevnl, listView uefa_nations_league), 9-11-2026 ±16:45: Nederland – Griekenland 1,47 / 4,90 / 7,00;
  Turkije – België 12-11 18:00 staat in dezelfde Nations League-lijst.
Bewust NIET gebruikt (onbevestigd of niet relevant): Ruslands plek in de live-ranking, de tweede novembertegenstander van
België, het exacte aantal ranking-edities na 18 november, de rol van de FIFA-ranking in de WK 2030-kwalificatie.
  python3 specials/fifa_ranking_nederland_2026.py   (dry run)"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

# ---------------------------------------------------------------- DATA (na elke nieuwe ranking hier bijwerken)
PUBLICATIE = "7 oktober 2026"
VORIGE_PUBLICATIE = "20 juli 2026"
NA_PUBLICATIE = "2026-11-18"            # volgende officiële FIFA-ranking (fifa.com: 'Next official update')
NA_PUBLICATIE_TEKST = "woensdag 18 november 2026"

# (plek, land, club-slug of None, punten, vorige plek, vorige punten)
RANKING = [
    (1, "Spanje", "spanje", 2011.57, 1, 1995.88),
    (2, "Argentinië", None, 1972.80, 2, 1970.37),
    (3, "Frankrijk", None, 1958.86, 3, 1948.97),
    (4, "Engeland", None, 1925.59, 4, 1922.83),
    (5, "Portugal", None, 1807.69, 7, 1787.85),
    (6, "Brazilië", None, 1806.51, 5, 1804.92),
    (7, "Marokko", "marokko", 1805.34, 6, 1803.99),
    (8, "België", "belgie", 1779.17, 8, 1778.36),
    (9, "Nederland", "nederland", 1778.61, 9, 1775.54),
    (10, "Mexico", None, 1738.48, 10, 1754.30),
]
EXTRA = [
    (11, "Colombia", None, 1735.80, 11, 1739.89),
    (12, "Zwitserland", None, 1725.39, 14, 1710.88),
    (13, "Duitsland", "duitsland", 1717.52, 12, 1726.22),
    (41, "Griekenland", "griekenland", 1498.71, 46, 1473.19),
    (44, "Servië", "servie", 1482.24, 40, 1502.13),
]

# punten van Oranje vóór en na elk duel (FIFA), tussen VORIGE_PUBLICATIE en PUBLICATIE
ORANJE_DUELS = [
    ("24 sep", "Nederland – Duitsland", "1-1", 1775.54224, 1774.834531),
    ("27 sep", "Servië – Nederland", "1-2", 1774.834531, 1778.645901),
    ("1 okt", "Griekenland – Nederland", "2-2", 1778.645901, 1774.890798),
    ("4 okt", "Nederland – Servië", "2-1", 1774.890798, 1778.612237),
]

# Oranje in de ranking door de jaren heen: (moment, plek, toelichting)
HISTORIE = [
    ("Augustus 2011", "<strong>1</strong>", "Hoogste plek ooit, de enige editie met Oranje op nummer 1"),
    ("Augustus 2017", "<strong>36</strong>", "Laagste plek ooit, midden in de mislukte kwalificatie voor het WK 2018"),
    ("November 2025", "7", "Ranking voor de WK-loting: Oranje in pot 1"),
    ("11 juni 2026", "8", "Ranking bij de start van het WK 2026"),
    ("20 juli 2026", "9", "Na het WK: uitgeschakeld in de 1/16e finale door Marokko"),
    ("7 oktober 2026", "9", "Na vier Nations League-duels, 3,07 punten erbij"),
]

IMPORTANTIE = [
    ("Vriendschappelijk, buiten een interlandperiode", 5),
    ("Vriendschappelijk, binnen een interlandperiode", 10),
    ("Nations League, groepsfase", 15),
    ("Nations League, play-offs en Finals", 25),
    ("Kwalificatie voor WK of continentaal toernooi (zoals het EK)", 25),
    ("EK, Copa América e.d. tot de kwartfinale", 35),
    ("EK, Copa América e.d. vanaf de kwartfinale", 40),
    ("WK-eindronde tot de kwartfinale", 50),
    ("WK-eindronde vanaf de kwartfinale", 60),
]

# novembervenster (8 t/m 18 november 2026)
NOVEMBER = [("Vr 13 november", "20:45", "Nederland – Griekenland", "Johan Cruijff ArenA", "NPO 3"),
            ("Ma 16 november", "20:45", "Duitsland – Nederland", "Olympiastadion, Berlijn", "NPO 3")]
ODDS_NED_GRE = (1.47, 4.90, 7.00)       # 711, 9-11-2026


# ---------------------------------------------------------------- REKENWERK (FIFA SUM-formule)
def verwacht(p_a, p_b):
    """We = 1 / (10^(-dr/600) + 1), dr = punten A - punten B."""
    return 1 / (10 ** (-(p_a - p_b) / 600) + 1)


def verschil(p_a, p_b, w, imp=15):
    return imp * (w - verwacht(p_a, p_b))


def nl(x, d=2, teken=False):
    s = f"{x:+.{d}f}" if teken else f"{x:.{d}f}"
    return s.replace(".", ",")


PT = {r[1]: r[3] for r in RANKING + EXTRA}
PLEK = {r[1]: r[0] for r in RANKING + EXTRA}
VPLEK = {r[1]: r[4] for r in RANKING + EXTRA}
NED, BEL, GER, GRE = PT["Nederland"], PT["België"], PT["Duitsland"], PT["Griekenland"]
ACHTER_BEL = BEL - NED
TOTAAL_WINST = NED - [r[5] for r in RANKING if r[1] == "Nederland"][0]

GR = {u: verschil(NED, GRE, w) for u, w in (("w", 1), ("g", .5), ("v", 0))}
# Duitsland – Nederland: Oranje met de punten na het duel met Griekenland, Duitsland met de huidige punten (benadering)
DE = {u: verschil(NED + GR["w"], GER, w) for u, w in (("w", 1), ("g", .5), ("v", 0))}
DE_NA_VERLIES = {u: verschil(NED + GR["v"], GER, w) for u, w in (("w", 1), ("g", .5), ("v", 0))}
BESTE = NED + GR["w"] + DE["w"]
SLECHTSTE = NED + GR["v"] + DE_NA_VERLIES["v"]
BEL_TUR = {u: verschil(BEL, PT_TUR, w) for PT_TUR in (1563.54,) for u, w in (("w", 1), ("g", .5), ("v", 0))}
WE_GRE = verwacht(NED, GRE)

# voorbeelden voor de uitleg van de formule
SRB_VOOR, NED_VOOR = 1494.217049, 1774.834531                 # Servië – Nederland 1-2, 27-9-2026
WE_SRB = verwacht(NED_VOOR, SRB_VOOR)
SRB_WINST = verschil(NED_VOOR, SRB_VOOR, 1)
MAR_NED, MAR_MAR, MAR_NA = 1775.49909, 1776.398605, 1775.54224  # Nederland – Marokko 1-1 (2-3 strafschoppen), WK 2026
WE_MAR = verwacht(MAR_NED, MAR_MAR)
GRE_DUEL = ORANJE_DUELS[2]

OG_DATUM = PUBLICATIE

L = {"nl": '<a href="/clubs/nederland">Nederland</a>',
     "oranje": '<a href="/clubs/nederland">Oranje</a>',
     "be": '<a href="/clubs/belgie">België</a>',
     "de": '<a href="/clubs/duitsland">Duitsland</a>',
     "gr": '<a href="/clubs/griekenland">Griekenland</a>',
     "es": '<a href="/clubs/spanje">Spanje</a>',
     "ma": '<a href="/clubs/marokko">Marokko</a>',
     "nlg": '<a href="/competities/uefa-nations-league">Nations League</a>',
     "opzet": '<a href="/nieuws/nations-league-nieuwe-opzet-2028-wat-betekent-het-voor-oranje">wat Oranje nodig heeft in de Nations League</a>',
     "uitleg": '<a href="/nieuws/hoe-werkt-de-nations-league-complete-uitleg-2026-2027">hoe de Nations League werkt</a>',
     "selectie": '<a href="/nieuws/selectie-oranje-november-2026-griekenland-duitsland">de selectie van Oranje voor november</a>',
     "711": '<a href="/bookmakers/711">711</a>',
     "legaal": '<a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>',
     "live": '<a href="/live-kijken">live kijken</a>'}


def land(naam, slug):
    return f'<a href="/clubs/{slug}">{naam}</a>' if slug else naam


def beweging(nu, vorig):
    return "=" if nu == vorig else (f"▲ {vorig - nu}" if nu < vorig else f"▼ {nu - vorig}")


TOP10 = [(f"<strong>{p}</strong>", f"<strong>{land(n, s)}</strong>" if n == "Nederland" else land(n, s),
          f"<strong>{nl(pt)}</strong>" if n == "Nederland" else nl(pt), beweging(p, vp), nl(pt - vpt, teken=True))
         for p, n, s, pt, vp, vpt in RANKING]
BUREN = [(land(n, s), f"<strong>{p}</strong>", nl(pt), str(vp), beweging(p, vp))
         for p, n, s, pt, vp, vpt in sorted([r for r in RANKING + EXTRA
                                             if r[1] in ("België", "Nederland", "Duitsland", "Griekenland")])]
DUELS = [(d, w, u, nl(na - voor, teken=True), nl(na)) for d, w, u, voor, na in ORANJE_DUELS]
SCENARIO = [("Nederland – Griekenland (13-11)", nl(GR["w"], teken=True), nl(GR["g"], teken=True), nl(GR["v"], teken=True)),
            ("Duitsland – Nederland (16-11)", nl(DE["w"], teken=True), nl(DE["g"], teken=True), nl(DE["v"], teken=True))]

# deelkaart: og_kaarten/gsod.py
OG_LOGO = "nederland-logo.png"
OG_EYEBROW = "FIFA-ranking · Oranje"
OG_KOP = f"Oranje staat<br><em>{PLEK['Nederland']}e van de wereld</em>"
OG_TEGELS = [("Punten Oranje", nl(NED)), ("Achter België", nl(ACHTER_BEL))]
OG_KOPJE = f"FIFA-ranking van {OG_DATUM}"
OG_RECHTS = "Punten"
OG_RIJEN = [(f"{PLEK['Spanje']}. Spanje", "Wereldkampioen, ruim aan kop", nl(PT["Spanje"])),
            (f"{PLEK['België']}. België", "Eén plek boven Oranje", nl(BEL)),
            (f"{PLEK['Nederland']}. Nederland", f"Gelijk gebleven, {nl(TOTAAL_WINST, teken=True)} punten", nl(NED)),
            (f"{PLEK['Duitsland']}. Duitsland", "Eén plek gezakt", nl(GER))]

SLUG = "fifa-ranking-nederland-waar-staat-oranje"
RUBRIEK = "66d6d655bc312d5c0e834ecd"   # zelfde rubriek als de andere Oranje-artikelen
TITEL = "FIFA-ranking Nederland: waar staat Oranje? Stand 2026"
SAMENVATTING = (f"Oranje staat {PLEK['Nederland']}e op de FIFA-ranking van {PUBLICATIE}, net achter België. "
                "Top 10, punten, de formule en wat november nog verandert.")

# ---------------------------------------------------------------- TEKST
content = f"""<p><strong>{L['nl']} staat {PLEK['Nederland']}e op de FIFA-wereldranglijst. In de officiële ranking van {PUBLICATIE} heeft Oranje {nl(NED)} punten. Dat is dezelfde plek als in de vorige editie van {VORIGE_PUBLICATIE}, met {nl(TOTAAL_WINST)} punten meer. {L['es']} is nummer 1 met {nl(PT['Spanje'])} punten. {L['be']} staat één plek hoger dan Oranje, met een voorsprong van maar {nl(ACHTER_BEL)} punt. {L['de']} is {PLEK['Duitsland']}e. De volgende FIFA-ranking verschijnt op {NA_PUBLICATIE_TEKST}, na de interlands tegen Griekenland en Duitsland.</strong></p>
<p>FIFA publiceert de wereldranglijst na elke interlandperiode. Hieronder vind je de actuele top 10, de plek van Oranje en de buurlanden, en wat de twee duels in november nog kunnen veranderen. We leggen ook uit hoe de punten worden berekend en waarom de ranking ertoe doet. De cijfers komen rechtstreeks van FIFA en zijn gecontroleerd op 9 november 2026.</p>
<h3><strong>De actuele FIFA-ranking: de top 10</strong></h3>
{tabel(["#", "Land", "Punten", "Plek t.o.v. " + VORIGE_PUBLICATIE[:-5], "Punten erbij/eraf"], TOP10)}
<p>Spanje, de regerend wereldkampioen, liep in de interlandperiode van september en oktober verder uit en heeft nu bijna 40 punten voorsprong op Argentinië. Portugal is de enige stijger binnen de top 10: na vier zeges in de Nations League ging het twee plekken omhoog naar de vijfde plaats. Brazilië en Marokko zakten daardoor elk één plek. Mexico verloor als enige in de top 10 flink wat punten, maar bleef tiende.</p>
<h3><strong>Waar staan Oranje, België en Duitsland?</strong></h3>
{tabel(["Land", "Plek", "Punten", "Vorige plek", "Verschil"], BUREN)}
<p>Tussen België en Oranje zit minder dan één punt. Duitsland zakte één plek, omdat Zwitserland erlangs ging. Griekenland, de tegenstander van vrijdag, steeg vijf plekken naar de {PLEK['Griekenland']}e plaats en was daarmee een van de stijgers van deze editie.</p>
<p><strong>Waar kwamen de punten van Oranje vandaan?</strong> Tussen de rankings van juli en oktober speelde Oranje vier duels in de {L['nlg']}. Elk duel leverde punten op of kostte punten:</p>
{tabel(["Datum", "Wedstrijd", "Uitslag", "Punten", "Totaal na duel"], DUELS)}
<p>Opvallend: het gelijkspel in Griekenland kostte Oranje {nl(GRE_DUEL[3] - GRE_DUEL[4])} punten. Volgens de formule hoorde Oranje die wedstrijd te winnen, dus een punt is minder dan verwacht. Het gelijkspel tegen Duitsland kostte bijna niets, omdat de landen dicht bij elkaar staan. De twee zeges op Servië leverden samen ruim 7,5 punten op.</p>"""

content2 = f"""<h3><strong>Wanneer komt de volgende FIFA-ranking uit?</strong></h3>
<p>De volgende officiële FIFA-ranking verschijnt op <strong>{NA_PUBLICATIE_TEKST}</strong>. Het rankingvenster van november loopt volgens FIFA van 8 tot en met 18 november. Alle interlands in die periode tellen mee. Voor Oranje zijn dat de laatste twee groepsduels in de Nations League:</p>
{tabel(["Datum", "Aftrap", "Wedstrijd", "Stadion", "Tv"], [(f"<strong>{d}</strong>", t, w, s, tv) for d, t, w, s, tv in NOVEMBER])}
<p>Beide duels vallen in de groepsfase van de Nations League en tellen dus met gewicht 15 (zie de uitleg hieronder). Wat er in de groep op het spel staat, lees je in ons artikel over {L['opzet']}. Bondscoach Xavi Hernández heeft 25 spelers opgeroepen; zie {L['selectie']}.</p>
<h3><strong>Wat kan Oranje in november winnen of verliezen?</strong></h3>
<p>Met de FIFA-formule kun je vooraf uitrekenen wat elke uitslag oplevert. De bedragen hieronder zijn afgerond. Voor het duel in Berlijn gaan we uit van de huidige punten van Duitsland en van een Oranje-zege op Griekenland. De echte bedragen hangen af van de punten vlak voor de aftrap, want ook Duitsland speelt eerst nog (in Servië).</p>
{tabel(["Wedstrijd", "Winst", "Gelijk", "Verlies"], SCENARIO)}
<p><strong>Tegen Griekenland is Oranje de grote favoriet.</strong> Het verschil is bijna 280 punten, dus de formule verwacht een resultaat van {nl(WE_GRE)} (op een schaal van 0 tot 1). Winst levert daardoor weinig op ({nl(GR['w'], teken=True)}). Een gelijkspel kost bijna net zoveel ({nl(GR['g'], teken=True)}) en een nederlaag kost veel ({nl(GR['v'], teken=True)}). <strong>In Berlijn is het andersom</strong>: Duitsland staat dichter bij Oranje, dus daar valt met een zege meer te winnen.</p>
<p><strong>Wat betekent dat voor de plek?</strong></p>
<ul><li><strong>Twee zeges:</strong> Oranje komt op ongeveer {nl(BESTE, 0)} punten. Dat is genoeg om België te passeren, tenzij België in zijn eigen duels ook flink punten pakt.</li><li><strong>Plek 8 is het hoogst haalbare</strong> in normale omstandigheden. Marokko (7e) staat {nl(PT['Marokko'] - NED)} punten voor; dat haalt Oranje alleen in bij zeer onverwachte uitslagen elders.</li><li><strong>Twee nederlagen:</strong> Oranje zakt naar ongeveer {nl(SLECHTSTE, 0)} punten. Uit de top 10 vallen is dan nog steeds vrijwel uitgesloten: Mexico (10e, {nl(PT['Mexico'])}) en Colombia (11e, {nl(PT['Colombia'])}) zouden er in november ruim 20 punten bij moeten halen.</li></ul>
<p><strong>Let ook op België.</strong> De Belgen spelen op donderdag 12 november om 18:00 uur in Turkije, ook in de Nations League. Winst levert België ongeveer {nl(BEL_TUR['w'], teken=True)} op, een gelijkspel {nl(BEL_TUR['g'], teken=True)} en een nederlaag {nl(BEL_TUR['v'], teken=True)}. Omdat het verschil met Oranje maar {nl(ACHTER_BEL)} punt is, beslissen de resultaten van beide landen samen wie op 18 november achtste staat.</p>
<h3><strong>Hoe werkt de FIFA-ranking? De SUM-formule</strong></h3>
<p>Sinds augustus 2018 gebruikt FIFA de zogeheten SUM-methode, gebaseerd op het Elo-systeem uit het schaken. Er wordt geen gemiddelde meer berekend: na elke interland gaan er punten bij of af. Wat de winnaar wint, verliest de verliezer. De formule is:</p>
<p><strong>P = P<sub>voor</sub> + I × (W – W<sub>e</sub>)</strong></p>
<ul><li><strong>P<sub>voor</sub></strong>: de punten van een land vóór de wedstrijd.</li><li><strong>I</strong>: het belang van de wedstrijd (zie de tabel).</li><li><strong>W</strong>: de uitslag. Winst = 1, gelijk = 0,5, verlies = 0. Na strafschoppen krijgt de winnaar 0,75 en de verliezer 0,5.</li><li><strong>W<sub>e</sub></strong>: het verwachte resultaat: 1 / (10<sup>(–dr/600)</sup> + 1), waarbij dr het puntenverschil tussen de twee landen is.</li></ul>
{tabel(["Soort wedstrijd", "Belang (I)"], [(s, f"<strong>{i}</strong>") for s, i in IMPORTANTIE])}
<p><strong>Rekenvoorbeeld.</strong> Voor de uitwedstrijd in Servië had Oranje {nl(NED_VOOR)} punten en Servië {nl(SRB_VOOR)}. Het verschil van {nl(NED_VOOR - SRB_VOOR, 1)} punten geeft een verwacht resultaat van {nl(WE_SRB, 3)}. Oranje won met 1-2, dus: 15 × (1 – {nl(WE_SRB, 3)}) = <strong>{nl(SRB_WINST, teken=True)}</strong> punten. Precies dat bedrag staat ook in de FIFA-cijfers.</p>
<p><strong>Twee extra regels.</strong> Wie in de knock-outfase van een eindtoernooi verliest, verliest geen punten. En er is geen voordeel voor het thuisspelende land: alleen het puntenverschil telt. Een voorbeeld is de uitschakeling van Oranje op het WK 2026. In de 1/16e finale werd het 1-1 tegen Marokko en verloor Oranje met 2-3 na strafschoppen. Dat telt als gelijkspel (W = 0,5). Omdat beide landen bijna evenveel punten hadden (verwachting {nl(WE_MAR, 3)}), hield Oranje er zelfs {nl(MAR_NA - MAR_NED, teken=True)} punt aan over.</p>"""

content3 = f"""<h3><strong>Oranje in de FIFA-ranking: hoogste en laagste plek</strong></h3>
{tabel(["Moment", "Plek", "Toelichting"], [(f"<strong>{m}</strong>", p, t) for m, p, t in HISTORIE])}
<p>De beste plek ooit van Oranje is de eerste. In augustus 2011, een jaar na de verloren WK-finale van 2010, stond Nederland voor het eerst en tot nu toe de enige keer bovenaan. Het dieptepunt was augustus 2017: plek 36, midden in de kwalificatie voor het WK 2018, waarvoor Oranje zich niet plaatste. Volgens FIFA staat Oranje gemiddeld negende. Punten van voor augustus 2018 kun je niet vergelijken met de huidige punten, omdat FIFA toen een andere berekening gebruikte.</p>
<p>Op het WK 2026 begon Oranje als nummer 8 van de wereld. Bij de loting in december 2025 telde de ranking van november 2025, waarin Oranje zevende stond. Dat was genoeg voor pot 1. Na de uitschakeling tegen {L['ma']} zakte Oranje in juli naar de negende plaats.</p>
<h3><strong>Waarom is de FIFA-ranking belangrijk?</strong></h3>
<p>De ranking bepaalt vooral de <strong>potindeling bij lotingen</strong>. Bij de WK-loting van 2026 zaten de drie gastlanden en de beste negen landen van de FIFA-ranking van november 2025 in pot 1. Ook bij de Europese WK-kwalificatie voor 2026 werden de potten op de FIFA-ranking gebaseerd (van november 2024). Alleen de kwartfinalisten van de Nations League kregen toen voorrang voor pot 1.</p>
<p><strong>Voor de EK-kwalificatie telt de FIFA-ranking níet.</strong> UEFA verdeelt de potten voor de kwalificatie van het EK 2028 volgens het reglement op basis van de tussenstand van de Nations League 2026/27 over alle leagues. De loting is op zondag 6 december 2026 in Belfast. De duels tegen Griekenland en Duitsland tellen dus twee keer: voor de FIFA-ranking en, via de Nations League-stand, voor de EK-loting. Na het EK 2028 deelt UEFA de kwalificatie in volgens de Nations League-leagues; lees ook {L['uitleg']}.</p>
<p><strong>Wat zeggen de bookmakers?</strong> Ook de bookmakers zien Oranje als duidelijke favoriet tegen Griekenland. Bij {L['711']} staat een Nederlandse zege op <strong>{nl(ODDS_NED_GRE[0])}</strong>, een gelijkspel op {nl(ODDS_NED_GRE[1])} en een Griekse zege op {nl(ODDS_NED_GRE[2])} (maandag 9 november). Wed alleen bij een bookmaker met een vergunning van de Kansspelautoriteit; lees {L['legaal']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Op welke plek staat Nederland op de FIFA-ranking?</strong><br>Nederland staat {PLEK['Nederland']}e met {nl(NED)} punten, in de officiële FIFA-ranking van {PUBLICATIE}. Dat is dezelfde plek als in juli.</p>
<p><strong>Wanneer komt de nieuwe FIFA-ranking uit?</strong><br>De volgende officiële ranking verschijnt op {NA_PUBLICATIE_TEKST}. Daarin tellen de interlands van 8 tot en met 18 november mee, voor Oranje dus de duels met Griekenland en Duitsland.</p>
<p><strong>Wie staat er nummer 1 op de FIFA-ranking?</strong><br>Spanje, met {nl(PT['Spanje'])} punten. Argentinië ({nl(PT['Argentinië'])}) en Frankrijk ({nl(PT['Frankrijk'])}) maken de top 3 compleet.</p>
<p><strong>Waar staat België op de FIFA-ranking?</strong><br>België staat {PLEK['België']}e met {nl(BEL)} punten, slechts {nl(ACHTER_BEL)} punt meer dan Oranje. Duitsland staat {PLEK['Duitsland']}e.</p>
<p><strong>Wat is de hoogste plek van Oranje ooit?</strong><br>De eerste plek, in augustus 2011. De laagste plek was 36 in augustus 2017.</p>
<p><strong>Telt de FIFA-ranking mee voor de EK-loting?</strong><br>Nee. De potten voor de EK 2028-kwalificatie worden ingedeeld op de tussenstand van de Nations League 2026/27. De FIFA-ranking telt wel bij de WK-loting.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re, datetime
    alles = content + content2 + content3
    w = len(re.sub(r"<[^>]+>", " ", alles).split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", w, "woorden")
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert 900 <= w <= 2000, w
    # data-consistentie
    assert [r[0] for r in RANKING] == list(range(1, 11))
    assert all(RANKING[i][3] > RANKING[i + 1][3] for i in range(9)), "top 10 niet aflopend"
    assert RANKING[-1][3] > EXTRA[0][3]
    assert datetime.date.fromisoformat(NA_PUBLICATIE) > datetime.date(2026, 10, 7)
    assert "18 november 2026" in NA_PUBLICATIE_TEKST and NA_PUBLICATIE.endswith("11-18")
    # duels sluiten aan op de ranking: vorige punten -> huidige punten
    assert abs(ORANJE_DUELS[0][3] - 1775.54) < .01 and abs(ORANJE_DUELS[-1][4] - NED) < .01
    assert all(abs(ORANJE_DUELS[i][4] - ORANJE_DUELS[i + 1][3]) < 1e-6 for i in range(3))
    assert abs(sum(na - voor for *_, voor, na in ORANJE_DUELS) - TOTAAL_WINST) < .01
    # formule nagerekend tegen de FIFA-cijfers (I=15 Nations League, strafschoppen = 0,5)
    assert abs(SRB_WINST - (ORANJE_DUELS[1][4] - ORANJE_DUELS[1][3])) < .01
    assert abs(verschil(1775.54224, 1726.218839, .5) - (ORANJE_DUELS[0][4] - ORANJE_DUELS[0][3])) < .01
    assert abs(50 * (.5 - WE_MAR) - (MAR_NA - MAR_NED)) < .01
    # beweringen in de tekst
    assert 0 < ACHTER_BEL < 1 and BESTE < PT["Marokko"] and BESTE > BEL
    assert SLECHTSTE - PT["Mexico"] > 20 and SLECHTSTE - PT["Colombia"] > 20
    assert PT["Spanje"] - PT["Argentinië"] < 40 and PT["Spanje"] - PT["Argentinië"] > 38
    assert VPLEK["Portugal"] - PLEK["Portugal"] == 2
    assert NED - SRB_VOOR > 0 and 279 < NED - GRE < 280
    assert "20:45" in content2 and alles.count("18 november 2026") >= 3
    # huisstijl
    assert "<h2" not in alles and "<h4" not in alles and "betcity" not in alles.lower() and "/go/" not in alles
    for verboden in ("opstellingvandaag", "footymetrics", "espn", "wikipedia"):
        assert verboden not in alles.lower(), verboden
    assert content.startswith("<p><strong>") and content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    assert "Kansspelautoriteit" in alles
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    assert 4 <= alles.count("<br>") <= 6
    print("links:", sorted(set(re.findall(r'href="([^"]+)"', alles))))
    print("Griekenland:", {k: round(v, 2) for k, v in GR.items()}, "Duitsland:", {k: round(v, 2) for k, v in DE.items()},
          "beste", round(BESTE, 2), "slechtste", round(SLECHTSTE, 2), "België-Turkije", {k: round(v, 2) for k, v in BEL_TUR.items()})
    print("dry run ok")
