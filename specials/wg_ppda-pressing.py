# -*- coding: utf-8 -*-
"""NIEUW wedgids-artikel (Nieuws, nog geen item): wat is PPDA? Pressing in cijfers, plus field tilt, balbezit en big chances.
Slug wat-is-ppda-pressing (gaf HTTP 404 op 10-11-2026, dus vrij; ook wat-is-ppda gaf 404).
Rubriek Speluitleg, wedgids-categorie 'Wedden uitgelegd'. Onderwerp: Engelstalige analysesite (alleen het onderwerp).
Zoekwoorden: 'wat is ppda' / 'ppda voetbal' (hoofd), 'ppda betekenis', 'pressing statistiek', 'field tilt', 'balbezit
berekenen', 'big chance betekenis', 'grote kans opta'.

Afbakening: /nieuws/wat-is-xg-expected-goals (xG/xGOT/xGA) en het zusterartikel /nieuws/wat-is-xa-expected-assists worden
gelinkt, niet herhaald. Het Opta-artikel (/nieuws/wat-zijn-opta-gegevens-...) noemt 'penalty = altijd big chance' al in
één zin; hier de volledige definitie.

Feiten nagelopen op 10-11-2026 (bronnen NIET in de tekst genoemd, behalve Opta):
- Oorspronkelijke PPDA (Colin Trainor, 'Defensive Metrics: Measuring the Intensity of a High Press', 30-07-2014, nu op
  hudl.com/blog/defensive-metrics-measuring-the-intensity-of-a-high-press): 'Number of Passes made by Attacking Team /
  Number of Defensive Actions', alleen acties met Opta x-coördinaat > 40 vanuit de verdedigende ploeg = de 60% van het veld
  het verst van het eigen doel (hele helft tegenstander + een vijfde van de eigen helft); verdedigende acties = tackles,
  onderscheppingen, duels/mislukte tackles ('challenges') en overtredingen; lager = feller; voorbeelden: Engelse club na
  trainerswissel binnen zes duels van ±10-14 naar onder de 8, Barcelona onder Guardiola ±6-9. Auteur koos x=40 boven 33 en 50.
- Opta nu (theanalyst.com/articles/opta-football-stats-definitions, 23-07-2024, gewijzigd 29-05-2025): passes van de
  tegenstander 'outside of the pressing team's own defensive third' / verdedigende acties daar = fouls, tackles,
  interceptions, challenges en blocked passes. -> in de tekst: leveranciers verschillen in zone en acties.
- Waarden: premierleague.com/en/news/4250153 (19-02-2025, data van een dataleverancier, niet genoemd): 2021/22 laagste PPDA in
  de top-5 competities 7,26, hoogste 16,93. -> in de tekst 'rond 7' en 'rond 17', zonder clubnamen.
- Field tilt: geen officiële Opta-definitie gevonden; gangbaar = aandeel van een ploeg in alle passes (soms: aanrakingen) in
  het laatste derde deel van het veld (o.a. driblab.com, support.spiideo.com 'definitions autodata'). -> in de tekst 'meestal'.
- Balbezit: Opta rekende balbezit van oudsher als aandeel passes, niet als tijd (statsbomb-blog 'Does possession % matter?',
  slate.com 27-06-2014, nbcsports.com); één bron meldt dat Opta sinds 2017 met 'possessions' werkt -> NIET hard te maken
  welke methode nu precies wordt gebruikt. In de tekst daarom: 'veel leveranciers ... op basis van passes', 'andere meten
  tijd', 'percentages kunnen per bron verschillen'.
- Big chance (theanalyst, zelfde definitiepagina): 'A situation where a player should reasonably be expected to score,
  usually in a one-on-one scenario' (+ van heel dichtbij, elders in Opta-teksten); 'Penalties are always considered big
  chances'. Het is een oordeel van de data-analist, geen model.
- Wet: Bijlage 2 Regeling kansspelen op afstand (wetten.overheid.nl/BWBR0044767, geldend vanaf 01-04-2026): o.a.
  overtredingen, kaarten en hoekschoppen verboden -> in de tekst alleen als 'mag niet', met link naar het corners-artikel.
Bewust weggelaten: echte clubnamen en Eredivisie-cijfers (geen openbare bron die we mogen gebruiken), namen van
dataleveranciers buiten Opta, 'harde' drempels voor PPDA (zijn relatief), claims dat lage PPDA tot meer doelpunten leidt
(niet onderbouwd), pressingmaten op basis van tracking (te technisch), expected threat.
Rekenvoorbeelden fictief; alles hieronder berekend en ge-assert.
Interne links gecontroleerd met curl op 10-11-2026: alle HTTP 200, behalve /nieuws/wat-is-xa-expected-assists (nieuw
zusterartikel, gaat samen live).
  ../superodd-agent/.venv/bin/python specials/wg_publiceer.py ppda-pressing   (dry run)"""
import os, sys, re
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

ITEM_ID = None   # nieuw artikel
SLUG = "wat-is-ppda-pressing"
RUBRIEK = "6502b66cd9992658b4037cf5"   # Speluitleg
WEDGIDS_CAT = "Wedden uitgelegd"
TITEL = "Wat is PPDA? Pressing in cijfers uitgelegd"
SAMENVATTING = ("Wat betekent PPDA in het voetbal? Zo meet je pressing, met rekenvoorbeeld, plus field tilt, balbezit en "
                "big chances, en wat je eraan hebt bij wedden.")

OG_KOP = "Wat is <span>PPDA</span>?"
OG_EYEBROW = "Pressing in cijfers"
OG_CHIPS = ["Met rekenvoorbeeld", "Field tilt en balbezit"]
OG_MOTIEF = "tabel"

XG = "/nieuws/wat-is-xg-expected-goals"
XA = "/nieuws/wat-is-xa-expected-assists"
OU = "/nieuws/over-under-uitleg-over-2-5-goals"
BTTS = "/nieuws/beide-teams-scoren-btts-betekenis"
SCHOTEN = "/nieuws/dit-is-hoe-wedden-op-schoten-op-doel-werkt"
OPTA = "/nieuws/wat-zijn-opta-gegevens-alles-over-schoten-op-doel-en-unibet-weddenschappen"
CORNERS = "/nieuws/dit-is-waarom-wedden-op-corners-niet-meer-legaal-is-in-nederland"
CLV = "/nieuws/wat-is-closing-line-value-clv"
VERANTW = "/speel-bewust/verantwoord-wedden"
LINKS = (XG, XA, OU, BTTS, SCHOTEN, OPTA, CORNERS, CLV, VERANTW, "/wedgids")


def k(x, n=1):
    return f"{x:.{n}f}".replace(".", ",")


def pct(x, n=1):
    return f"{100 * x:.{n}f}".replace(".", ",") + "%"


# ---- rekenvoorbeeld 1 (fictief): team A (fel) tegen team B (afwachtend) ----
# passes van de tegenstander in de drukzone, en de verdedigende acties van de ploeg die druk zet in die zone
ACTIES = ("Tackles", "Onderscheppingen", "Duels (ook mislukte tackles)", "Overtredingen")
A = {"passes_tegen": 238, "acties": (11, 9, 4, 5)}
B = {"passes_tegen": 401, "acties": (8, 8, 3, 5)}
PPDA_A = A["passes_tegen"] / sum(A["acties"])
PPDA_B = B["passes_tegen"] / sum(B["acties"])
assert (sum(A["acties"]), sum(B["acties"]), k(PPDA_A), k(PPDA_B)) == (29, 24, "8,2", "16,7")
RIJEN_PPDA = ([("Passes van de tegenstander in de drukzone", str(A["passes_tegen"]), str(B["passes_tegen"]))]
              + [(a, str(x), str(y)) for a, x, y in zip(ACTIES, A["acties"], B["acties"])]
              + [("Verdedigende acties samen", str(sum(A["acties"])), str(sum(B["acties"]))),
                 ("<strong>PPDA</strong>", f"<strong>{A['passes_tegen']} ÷ {sum(A['acties'])} = {k(PPDA_A)}</strong>",
                  f"<strong>{B['passes_tegen']} ÷ {sum(B['acties'])} = {k(PPDA_B)}</strong>")])
# zelfde wedstrijd, andere zone: alleen de helft van de tegenstander
A_HELFT_P, A_HELFT_ACT = 181, 20
PPDA_A_HELFT = A_HELFT_P / A_HELFT_ACT
assert k(PPDA_A_HELFT) == "9,1" and A_HELFT_P < A["passes_tegen"] and A_HELFT_ACT < sum(A["acties"])

# ---- rekenvoorbeeld 2 (fictief): team C (veel balbezit) tegen team D (direct) ----
C = {"passes": 540, "derde": 70, "zone_tegen": 210, "acties": 14, "big": 0, "xg": 0.62}
D = {"passes": 300, "derde": 100, "zone_tegen": 410, "acties": 34, "big": 3, "xg": 1.85}
BEZIT_C = C["passes"] / (C["passes"] + D["passes"])
TILT_C = C["derde"] / (C["derde"] + D["derde"])
PPDA_C, PPDA_D = C["zone_tegen"] / C["acties"], D["zone_tegen"] / D["acties"]
assert (pct(BEZIT_C), pct(1 - BEZIT_C), pct(TILT_C), pct(1 - TILT_C)) == ("64,3%", "35,7%", "41,2%", "58,8%")
assert (k(PPDA_C), k(PPDA_D)) == ("15,0", "12,1")
RIJEN_CD = [
    ("Passes", str(C["passes"]), str(D["passes"])),
    ("<strong>Balbezit</strong> (aandeel passes)", pct(BEZIT_C), pct(1 - BEZIT_C)),
    ("Passes in het laatste derde deel", str(C["derde"]), str(D["derde"])),
    ("<strong>Field tilt</strong>", pct(TILT_C), pct(1 - TILT_C)),
    ("<strong>PPDA</strong>", k(PPDA_C), k(PPDA_D)),
    ("Big chances", str(C["big"]), str(D["big"])),
    ("xG", k(C["xg"], 2), k(D["xg"], 2)),
]

OG_DATA = [f"Team A · PPDA {k(PPDA_A)}", f"Team B · PPDA {k(PPDA_B)}", "Lager = feller druk zetten",
           f"Balbezit {pct(BEZIT_C, 0)} · field tilt {pct(TILT_C, 0)}"]

content = f"""<p><strong>PPDA staat voor passes per defensive action: het aantal passes dat een ploeg de tegenstander laat geven per eigen verdedigende actie, zoals een tackle, onderschepping, duel of overtreding. Je telt alleen op het deel van het veld waar je druk kunt zetten, meestal de 60 procent die het verst van je eigen doel ligt. Hoe lager de PPDA, hoe feller een ploeg jaagt: rond 8 is fel, rond 15 of hoger betekent dat een ploeg vooral afwacht.</strong></p>
<p>PPDA is de bekendste manier om pressing in één getal te vangen. In dit artikel lees je hoe je het berekent, waarom de uitkomst per bron verschilt en wat het wel en niet zegt. Daarna komen drie verwante cijfers aan bod: field tilt, balbezit en big chances. Tot slot lees je hoe analisten en wedders deze cijfers eerlijk gebruiken. <em>Teams en cijfers in de voorbeelden zijn fictief.</em></p>
<h3><strong>Hoe bereken je PPDA?</strong></h3>
<p>De formule is eenvoudig:</p>
<ul><li><strong>PPDA</strong> = passes van de tegenstander in de drukzone ÷ eigen verdedigende acties in diezelfde zone</li></ul>
<p>De <strong>drukzone</strong> is het deel van het veld waar een ploeg redelijkerwijs kan jagen. In de oorspronkelijke versie uit 2014 is dat de 60 procent van het veld het verst van het eigen doel: de hele helft van de tegenstander plus een strook van de eigen helft. Wat er dieper gebeurt, vlak voor het eigen doel, telt niet mee. Daar verdedigt elke ploeg, ook een ploeg die nooit druk zet.</p>
<p>Als <strong>verdedigende acties</strong> tellen tackles, onderscheppingen, duels om de bal (ook mislukte tackles) en overtredingen. Een overtreding telt mee, omdat ook die een aanval van de tegenstander afbreekt.</p>
<h3><strong>Rekenvoorbeeld: PPDA van twee teams</strong></h3>
<p>Team A speelt thuis tegen team B. Per ploeg tel je de passes van de tegenstander in de drukzone en de eigen verdedigende acties daar:</p>
{tabel(["", "Team A zet druk", "Team B zet druk"], RIJEN_PPDA)}
<p>Team A grijpt gemiddeld na elke {k(PPDA_A)} passes van de tegenstander in, team B pas na {k(PPDA_B)}. Team A jaagt dus veel feller. Ter vergelijking: in seizoen 2021/22 lag de felste ploeg in de vijf grote Europese competities rond de 7 en de meest afwachtende rond de 17.</p>
<h3><strong>Waarom verschilt PPDA per bron?</strong></h3>
<p>Niet elke dataleverancier gebruikt dezelfde zone en dezelfde acties. Opta telt bijvoorbeeld alles buiten het eigen verdedigende derde deel van het veld en rekent ook geblokte passes mee als verdedigende actie. Andere bronnen kijken alleen naar de helft van de tegenstander. Tel je in het voorbeeld alleen die helft, dan komt team A uit op {A_HELFT_P} passes en {A_HELFT_ACT} acties, een PPDA van {k(PPDA_A_HELFT)} in plaats van {k(PPDA_A)}.</p>
<p>Vergelijk daarom alleen PPDA-cijfers uit dezelfde bron. Een 9 op de ene site kan op een andere site een 8 of een 10 zijn.</p>"""

content2 = f"""<h3><strong>Wat zegt een lage of hoge PPDA, en wat niet?</strong></h3>
<p>PPDA beschrijft een speelstijl, geen kwaliteit. Een lage PPDA betekent dat een ploeg hoog op het veld de bal probeert te veroveren. Een hoge PPDA betekent dat een ploeg zich laat terugzakken en pas dichter bij het eigen doel ingrijpt. Allebei kan goed werken: veel sterke ploegen verdedigen bewust laag en loeren op de counter.</p>
<p>Verder wordt het getal beïnvloed door zaken die niets met de eigen pressing te maken hebben:</p>
<ul><li><strong>De stand:</strong> een ploeg die voorstaat, zakt vaak terug. Haar PPDA stijgt dan, ook al is de stijl niet veranderd.</li><li><strong>De tegenstander:</strong> een ploeg die snel lange ballen speelt, geeft weinig passes in de drukzone. Haar tegenstander krijgt dan een lage PPDA zonder echt hard te jagen.</li><li><strong>Kleine aantallen:</strong> één wedstrijd zegt weinig. Analisten kijken naar gemiddelden over vijf tot tien duels.</li></ul>
<p>Waar PPDA sterk in is: veranderingen zichtbaar maken. In het oorspronkelijke onderzoek uit 2014 zakte de PPDA van een Engelse club na een trainerswissel binnen zes wedstrijden van tussen de 10 en 14 naar onder de 8. Zo'n sprong zie je in de cijfers vaak eerder dan in de uitslagen.</p>
<h3><strong>Wat is field tilt?</strong></h3>
<p><strong>Field tilt</strong> laat zien welke ploeg het meest op de helft van de ander speelt. Meestal is het het aandeel van een ploeg in alle passes in het laatste derde deel van het veld, van beide ploegen samen. Sommige bronnen tellen balcontacten in plaats van passes. Heeft team C 70 passes in het laatste derde deel en team D 100, dan heeft team C een field tilt van {pct(TILT_C)} en team D van {pct(1 - TILT_C)}.</p>
<p>Field tilt meet terrein, geen kansen. Een ploeg kan het veld 'kantelen' en toch weinig gevaar stichten, bijvoorbeeld door veel voorzetten die niets opleveren.</p>
<h3><strong>Waarom zegt balbezit zo weinig?</strong></h3>
<p>Balbezit is het bekendste cijfer op tv, maar wel het minst veelzeggende. Veel dataleveranciers meten balbezit niet met een stopwatch, maar als het aandeel passes van beide ploegen. Andere bronnen meten tijd aan de bal. Daardoor kan het percentage per bron verschillen. Belangrijker is dat balbezit niets zegt over waar de bal is en wat ermee gebeurt. Neem deze wedstrijd:</p>
{tabel(["", "Team C", "Team D"], RIJEN_CD)}
<p>Team C had {pct(BEZIT_C, 0)} balbezit, maar speelde de bal vooral rond op eigen helft. Team D speelde direct, had meer passes in het laatste derde deel en kreeg {D['big']} grote kansen. Op balbezit lijkt team C de baas, op field tilt, big chances en <a href="{XG}">xG</a> was team D sterker. Let ook op de PPDA: team D zette feller druk ({k(PPDA_D)}) dan team C ({k(PPDA_C)}), ondanks veel minder balbezit.</p>"""

content3 = f"""<h3><strong>Wat is een big chance?</strong></h3>
<p>Een <strong>big chance</strong> of grote kans is volgens Opta een situatie waarin je redelijkerwijs mag verwachten dat een speler scoort, meestal een een-op-een met de keeper of een schot van heel dichtbij. Een penalty telt altijd als big chance. Het aantal gemiste grote kansen zie je vaak terug in samenvattingen als bewijs dat een ploeg 'had moeten winnen'.</p>
<p>Het verschil met xG: een big chance is een oordeel van een data-analist die de wedstrijd bekijkt, ja of nee. xG is een model dat elk schot een kans tussen 0 en 1 geeft. Een kans van 0,30 xG kan een big chance zijn of niet, afhankelijk van de situatie. Big chances zijn daardoor makkelijk te begrijpen, maar grover en iets subjectiever dan xG. Wie de aangever van zulke kansen wil meten, kijkt naar <a href="{XA}">xA (expected assists)</a>.</p>
<h3><strong>Hoe gebruiken analisten en wedders pressingdata?</strong></h3>
<p>Clubs gebruiken PPDA en field tilt vooral om stijlen te herkennen: hoe zet de volgende tegenstander druk, waar kun je hem bespelen, past een nieuwe speler bij de manier van verdedigen? Voor wedders zijn het nuttige achtergrondcijfers, mits je eerlijk bent over wat ze wel en niet zeggen.</p>
<ul><li><strong>Stijl botst op stijl.</strong> Een ploeg die fel jaagt tegen een ploeg die van achteruit opbouwt, kan balverlies dicht bij het doel opleveren. Dat kan een reden zijn om goed naar de markten voor <a href="{OU}">over/under</a>, <a href="{BTTS}">beide teams scoren</a> of <a href="{SCHOTEN}">schoten op doel</a> te kijken. Een vaste regel dat een lage PPDA meer doelpunten oplevert, bestaat niet.</li><li><strong>Veranderingen vóór de uitslagen.</strong> Een nieuwe trainer die hoger laat drukken, zie je vaak eerst in PPDA en xG terug. Combineer de twee altijd: pressing zonder betere kansen levert niets op.</li><li><strong>Context bij drukke weken.</strong> Fel jagen kost energie. Bij veel wedstrijden kort na elkaar kan een trainer kiezen voor rust. Dat is een aanwijzing, geen zekerheid.</li><li><strong>Kaarten en overtredingen vallen af.</strong> Pressing leidt vaak tot meer overtredingen, maar wedden op overtredingen, kaarten of <a href="{CORNERS}">corners</a> mag in Nederland niet.</li></ul>
<p>Bedenk ook dat bookmakers dezelfde cijfers kennen. Speelstijl zit al grotendeels in de odds verwerkt, zeker bij grote competities. Wil je meten of jouw inschattingen beter zijn dan de markt, kijk dan naar je <a href="{CLV}">closing line value</a> in plaats van naar een paar gewonnen weddenschappen. Hoe bookmakers spelersmarkten afrekenen, lees je in ons artikel over <a href="{OPTA}">Opta-gegevens</a>.</p>
<p>Wed alleen met geld dat je kunt missen en lees onze tips over <a href="{VERANTW}">verantwoord wedden</a>. Meer uitleg over wedden en statistieken vind je in de <a href="/wedgids">wedgids</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wat betekent PPDA in het voetbal?</strong><br>PPDA staat voor passes per defensive action: het aantal passes dat een ploeg de tegenstander laat geven per eigen verdedigende actie, op het deel van het veld waar je druk kunt zetten. Hoe lager, hoe feller de pressing.</p>
<p><strong>Wat is een goede PPDA?</strong><br>Er is geen goede of slechte PPDA, het is een stijl. Onder de 9 geldt als fel, boven de 14 als afwachtend. Vergelijk alleen cijfers uit dezelfde bron, want de zone en de acties verschillen per dataleverancier.</p>
<p><strong>Wat is field tilt?</strong><br>Het aandeel van een ploeg in alle passes in het laatste derde deel van het veld, van beide ploegen samen. Het laat zien wie het meest op de helft van de ander speelt.</p>
<p><strong>Hoe wordt balbezit berekend?</strong><br>Vaak als het aandeel passes van beide ploegen, soms als tijd aan de bal. Daardoor kan het percentage per bron verschillen. Balbezit zegt weinig over kansen: kijk ook naar field tilt en xG.</p>
<p><strong>Wat is een big chance?</strong><br>Volgens Opta een kans waarbij je redelijkerwijs mag verwachten dat de speler scoort, zoals een een-op-een of een schot van heel dichtbij. Een penalty is altijd een big chance.</p>
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
    assert not re.search(r"(?i)footymetrics|betcity|statsbomb|wyscout|fbref|understat|opstellingvandaag|waaroptv", html)
    faq = content3.split("Veelgestelde vragen")[1]
    assert 4 <= faq.count("<p><strong>") <= 6
    woorden = len(re.sub(r"<[^>]+>", " ", html).split())
    assert 1200 <= woorden <= 2200, woorden
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", woorden, "woorden")
