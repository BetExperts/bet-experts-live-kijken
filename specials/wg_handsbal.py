# -*- coding: utf-8 -*-
"""NIEUW wedgids-artikel (Nieuws, nog geen item): hands in het voetbal, wanneer is het handsbal? Spelregel 12 (2026/27):
armgrens, opzettelijk, onnatuurlijk groter, scoren met/vlak na hands, wat geen hands is, de keeper, strafschop, gele en
rode kaart, overzichtstabel met situaties. Rubriek Speluitleg, wedgids-categorie 'Sporten en regels'.
Onderwerp: Engelstalige analysesite (alleen het onderwerp, niets overgenomen).
Slug hands-voetbal-wanneer-is-het-handsbal (gaf HTTP 404 op 10-11-2026 met curl, dus vrij).
Zoekwoorden: 'hands voetbal' / 'handsbal regel' (hoofd), 'wanneer is het hands', 'hands regel 2026', 'onnatuurlijk groter',
'hands penalty', 'rood voor hands', 'hands schouder', 'hands keeper', 'hands aanvaller doelpunt'.

Feiten (bron + datum), alles nagelopen op 10-11-2026:
- IFAB Laws of the Game 2026/27, Law 12 (theifab.com/laws/latest/fouls-and-misconduct, seizoenkeuze toont 2026/27):
  * 'upper boundary of the arm is in line with the bottom of the armpit'; 'Not every touch ... is an offence'.
  * Overtreding: opzettelijk (bv. hand/arm naar de bal bewegen); arm maakt lichaam 'unnaturally bigger' = positie 'not a
    consequence of, or justifiable by, the player's body movement for that specific situation' (speler neemt risico);
    scoren direct uit hand/arm (ook per ongeluk, ook de keeper) of 'immediately after' de bal hand/arm raakte (ook per ongeluk).
  * Keeper: buiten strafschopgebied dezelfde beperkingen als iedereen; in eigen strafschopgebied onterecht met de hand =
    indirecte vrije schop, geen kaart (12.2: na loslaten opnieuw met de hand; na opzettelijke trap van medespeler; direct
    uit inworp van medespeler). 12.3: bal > 8 seconden in handen = hoekschop (sinds 2025/26, law-changes/2025-26).
  * Kaarten: geel voor hands die een veelbelovende aanval onderbreekt, 'except where the referee awards a penalty kick for
    a non-deliberate handball offence'; geel bij DOGSO met niet-opzettelijke hands + strafschop; geel voor hands 'in an
    attempt to score a goal'. Rood: DOGSO met opzettelijke hands (overal, behalve keeper in eigen strafschopgebied) en
    DOGSO met niet-opzettelijke hands buiten het eigen strafschopgebied (beide ook al in 2025/26-tekst).
  * Q&A Law 12: schouder is geen arm (goal met schouder telt, ook opzettelijk); arm tegen de borst, lichaam niet groter = geen
    hands; per ongeluk hands van medespeler die kans creëert of vóór goal van ander = geen overtreding; verdediger die bal
    via kop en arm in eigen doel werkt = doelpunt ('only applies to attacking team players'); aanvaller die bal in zestien
    opzettelijk met hand controleert = directe vrije schop, geel alleen bij poging tot scoren.
- IFAB Law changes 2026/27 (theifab.com/law-changes/latest): geen gele kaart voor DOGSO als voordeel wordt gegeven en er
  wordt gescoord; 'There is no caution when the referee plays advantage when a player has unsuccessfully tried to stop a
  goal with their hand(s)/arm(s)'. KNVB 'Spelregels 2026/'27, spelregelwijzigingen en toelichtingen' (1 juni 2026,
  knvb.nl/downloads/bestand/29991) bevestigt de Regel 12-wijzigingen. Wetten gelden vanaf 1 juli 2026 (IFAB-jaarcyclus).
- IFAB AGM 5 maart 2021 (inside.fifa.com, 'The IFAB clarifies handball law'): per ongeluk hands van een medespeler vóór een
  doelpunt of kans is geen overtreding meer; wetswijziging per 1 juli 2021.
- Uitzonderingen 'bal van eigen lichaam' en 'steunarm bij vallen' stonden letterlijk in Law 12 van 2019/20 en 2020/21
  (espn.com 'handball revamp confirmed ifab reveals new laws game 2019-20'; samenvatting cusa.ab.ca LOTG Revisions 2021-22:
  'hand/arm is between the body and the ground to support the body, but not extended laterally or vertically') en zijn
  sinds 2021/22 uit de wettekst; nu beoordeeld via het criterium lichaamsbeweging. Premier League-interpretatie 2024/25
  (premierleague.com/news/4079558, 9-9-2024): duidelijke afketsing weegt zwaar, maar contact met ander lichaamsdeel
  sluit hands niet automatisch uit. -> tekst: 'meestal geen hands', geen absolute regel.
- VAR: IFAB Law 5/6: alleen bij duidelijke fout of ernstig gemist voorval bij o.a. strafschop/geen strafschop en directe
  rode kaart. Eredivisie: VAR bij alle wedstrijden sinds 2018/19 (knvb.nl/themas/sportiviteit-en-respect/video-assistant-
  referee-var + KNVB 'seizoen 18/19 VAR in cijfers'). KNVB Beker 2026/27: VAR vanaf de achtste finales (Reglement
  Eurojackpot KNVB Beker 2026/'27, art. 2, knvb.nl/downloads/bestand/30192).
- Schorsing na rood: tuchtcommissie betaald voetbal van de KNVB beoordeelt; kaart kan worden geseponeerd als niet vast te
  stellen is dat er een duidelijke scoringskans was (KNVB-uitspraken 2025, o.a. knvb.nl/nieuws/.../tuchtcommissie-spreek-
  vaessen-fc-groningen-vrij). -> tekst algemeen, geen namen, geen vaste strafmaat genoemd.
- Wedden: Regeling kansspelen op afstand, Bijlage 2, onderdeel 2.3 Voetbal (wetten.overheid.nl/BWBR0044767/2026-04-01):
  geen weddenschappen op gele/rode kaarten, veroorzaken en nemen van strafschoppen, overtredingen e.d. Benutte strafschoppen
  in de wedstrijd tellen mee voor over/under en doelpuntenmaker (wg_over-under.py, wg_doelpuntenmaker.py).

Bewust weggelaten: geen echte hands-incidenten, geen namen van scheidsrechters of spelers, geen vaste schorsingsduur,
geen 'hands'-markten als wedmogelijkheid, geen rekenvoorbeeld (spelregelartikel; tabellen volstaan, brief ronde 2).
Interne links gecontroleerd op 10-11-2026 (curl HTTP 200), behalve STRAF: dat is het nieuwe strafschopartikel
(wg_strafschop-regels.py), nog 404 -> beide artikelen in één keer publiceren (wg_publiceer.py handsbal strafschop-regels).
Geen INFOGRAPHIC (de twee tabellen zijn het overzicht).
  ../superodd-agent/.venv/bin/python specials/wg_publiceer.py handsbal [--live]"""
import os, sys, re
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
import lk_webflow as WF
from legaal_data import tabel

ITEM_ID = None   # nieuw artikel
SLUG = "hands-voetbal-wanneer-is-het-handsbal"
RUBRIEK = "6502b66cd9992658b4037cf5"   # Speluitleg
WEDGIDS_CAT = "Sporten en regels"
TITEL = "Hands in het voetbal: wanneer is het handsbal?"
SAMENVATTING = ("Wanneer is het hands in het voetbal? De regels van 2026/27: waar de arm begint, onnatuurlijk groter, "
                "strafschop, geel of rood, met een overzichtstabel.")

OG_KOP = "Wanneer is het <span>hands</span>?"
OG_EYEBROW = "Spelregels voetbal 2026/27"
OG_CHIPS = ["Arm begint onder de oksel", "Met overzichtstabel"]
OG_MOTIEF = "tabel"
OG_DATA = ["Schouder · geen hands", "Arm naar de bal · hands", "Onnatuurlijk groter · hands", "Kans ontnomen · rood"]

STRAF = "/nieuws/strafschop-regels-penalty-overnemen"
CORNERS = "/nieuws/dit-is-waarom-wedden-op-corners-niet-meer-legaal-is-in-nederland"
OU = "/nieuws/over-under-uitleg-over-2-5-goals"
DOELP = "/nieuws/doelpuntenmaker-wedden-regels"
SPELREGELS = "/nieuws/nieuwe-spelregels-eredivisie-2026-27-alles-wat-je-moet-weten-op-een-rijtje"
GESTAAKT = "/nieuws/wedstrijd-gestaakt-wat-gebeurd-er-nu-met-je-weddenschap"
LEGAAL = "/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland"
BEWUST = "/speel-bewust/verantwoord-wedden"
LINKS = (STRAF, CORNERS, OU, DOELP, SPELREGELS, GESTAAKT, LEGAAL, BEWUST, "/competities/eredivisie", "/wedgids")

JA, NEE = "<strong>Ja</strong>", "<strong>Nee</strong>"

# ---- overzicht: sancties bij hands (IFAB Law 12, 2026/27) ----
SANCTIES = [
    ("Gewone hands, geen kans in gevaar", "Directe vrije schop (in eigen strafschopgebied: strafschop)", "Geen"),
    ("Hands onderbreekt een veelbelovende aanval", "Directe vrije schop", "Geel"),
    ("Idem, in eigen strafschopgebied, niet opzettelijk", "Strafschop", "Geen"),
    ("Idem, in eigen strafschopgebied, opzettelijk", "Strafschop", "Geel"),
    ("Opzettelijke hands ontneemt een doelpunt of duidelijke scoringskans", "Directe vrije schop of strafschop", "Rood (niet voor de keeper in eigen strafschopgebied)"),
    ("Niet-opzettelijke hands ontneemt een doelpunt of scoringskans, buiten eigen strafschopgebied", "Directe vrije schop", "Rood"),
    ("Niet-opzettelijke hands ontneemt een doelpunt of scoringskans, in eigen strafschopgebied", "Strafschop", "Geel"),
    ("Proberen te scoren met hand of arm", "Directe vrije schop, doelpunt telt niet", "Geel"),
    ("Doelpunt met de hand proberen te voorkomen, bal gaat toch in", "Doelpunt telt", "Geen (sinds 2026/27)"),
    ("Keeper pakt de bal onterecht in eigen strafschopgebied", "Indirecte vrije schop", "Geen"),
]
assert len(SANCTIES) == 10 and sum(r[2].startswith("Rood") for r in SANCTIES) == 2

# ---- overzicht: is het hands? ----
SITUATIES = [
    ("Bal tegen de schouder", NEE, "De arm begint pas onder de oksel"),
    ("Arm dicht tegen het lichaam", NEE, "Het lichaam wordt niet groter"),
    ("Arm beweegt naar de bal", JA, "Opzettelijk"),
    ("Armen wijd bij een blok, zonder logische reden", JA, "Lichaam onnatuurlijk groter"),
    ("Aanvaller scoort per ongeluk met de arm", JA, "Doelpunt telt niet"),
    ("Bal raakt de arm van de aanvaller, hij scoort meteen daarna", JA, "Doelpunt telt niet"),
    ("Bal raakt per ongeluk de arm van een medespeler, een ander scoort", NEE, "Doelpunt telt"),
    ("Verdediger werkt de bal via zijn arm in eigen doel", NEE, "Eigen doelpunt telt"),
    ("Bal kaatst van dichtbij van eigen been tegen de arm", "Meestal niet", "Tenzij de arm al ver van het lichaam stond"),
    ("Steunarm tussen lichaam en grond bij vallen", "Meestal niet", "Wel als de arm opzij of omhoog wordt gestoken"),
    ("Keeper pakt een terugspeelbal met de voet in eigen strafschopgebied", NEE, "Wel een indirecte vrije schop"),
    ("Keeper pakt de bal buiten zijn strafschopgebied", JA, "Hij is daar een gewone speler"),
]
assert len(SITUATIES) == 12

CHECK = {r[0]: r[1] for r in SITUATIES}
assert CHECK["Bal tegen de schouder"] == NEE and CHECK["Arm beweegt naar de bal"] == JA

content = f"""<p><strong>Hands is in het voetbal een overtreding als een speler de bal opzettelijk met zijn hand of arm raakt, of als zijn arm zijn lichaam onnatuurlijk groter maakt. Een aanvaller mag ook niet scoren met zijn arm of vlak nadat de bal zijn arm raakte, ook niet per ongeluk. De arm begint onder de oksel, dus een bal tegen de schouder is nooit hands.</strong></p>
<p>Niet elke aanraking met de arm is dus hands. In dit artikel lees je de regels zoals ze in het seizoen 2026/27 gelden, wat juist géén hands is, welke regels voor de keeper gelden en wanneer hands een strafschop, een gele kaart of een rode kaart oplevert. Onderaan staat een overzichtstabel met de bekendste situaties.</p>
<h3><strong>Welke regels gelden voor hands?</strong></h3>
<p>De spelregels van het voetbal worden gemaakt door de IFAB, de internationale spelregelcommissie waarin FIFA en de Britse voetbalbonden zitten. Hands staat in Regel 12, over overtredingen en onbehoorlijk gedrag. De KNVB vertaalt die regels naar de Nederlandse spelregels voor veldvoetbal, dus in de Eredivisie, de KNVB Beker en bij Oranje gelden dezelfde regels. Een nieuw spelregeljaar begint op 1 juli.</p>
<h3><strong>Waar begint de arm bij hands?</strong></h3>
<p>Voor hands telt alleen de arm onder de onderkant van de oksel. Alles daarboven, zoals de schouder, is geen arm. Een bal die van de schouder in het doel gaat, is dus gewoon een geldig doelpunt, ook als de speler de bal bewust met zijn schouder speelde.</p>
<p>In de praktijk is die grens op snelheid lastig te zien. Daarom bekijkt de VAR bij twijfel de beelden als er een doelpunt of strafschop van afhangt.</p>
<h3><strong>Wanneer is het hands volgens de spelregels?</strong></h3>
<p>Volgens Regel 12 maakt een speler hands als hij:</p>
<ul><li><strong>de bal opzettelijk met hand of arm raakt.</strong> Het duidelijkste voorbeeld is een arm die naar de bal toe beweegt.</li><li><strong>de bal raakt met een arm die zijn lichaam onnatuurlijk groter maakt.</strong> Dat is zo als de stand van de arm niet voortkomt uit, of niet te verklaren is door, de beweging die hij op dat moment maakt. Wie zijn arm zo houdt, neemt bewust het risico dat de bal ertegen komt.</li><li><strong>scoort direct met hand of arm</strong>, ook als het per ongeluk gebeurt. Dit geldt ook voor de keeper.</li><li><strong>scoort onmiddellijk nadat de bal zijn hand of arm raakte</strong>, ook als die aanraking per ongeluk was.</li></ul>
<p>Het tweede punt geeft de meeste discussie. Een verdediger die met gespreide armen een voorzet probeert te blokken, maakt zich groter dan nodig en wordt dan bestraft. Rent hij met zijn armen in een normale loophouding, of zwaait zijn arm mee bij een sprong, dan is die stand te verklaren door zijn beweging. De scheidsrechter beslist per situatie.</p>
<h3><strong>Telt hands van een medespeler vóór een doelpunt?</strong></h3>
<p>Nee, niet als het per ongeluk gebeurt. Raakt de bal per ongeluk de arm van een aanvaller en scoort een medespeler daarna, dan telt het doelpunt. Dat geldt ook als die aanraking een kans creëert. Sinds 1 juli 2021 geldt de strenge regel alleen nog voor de speler die zelf scoort. Was de aanraking van de medespeler wel opzettelijk, of stond zijn arm onnatuurlijk ver van zijn lichaam, dan is het alsnog hands.</p>"""

content2 = f"""<h3><strong>Wanneer is het geen hands?</strong></h3>
<p>Omdat niet elke aanraking telt, zijn er situaties die meestal ongestraft blijven:</p>
<ul><li><strong>Arm dicht bij het lichaam.</strong> Houdt een verdediger zijn arm tegen zijn borst of zij en komt de bal daartegen, dan maakt hij zich niet groter. Dat is geen hands.</li><li><strong>Bal van je eigen lichaam.</strong> Kaatst de bal van dichtbij eerst van je eigen been of hoofd tegen je arm, dan had je geen tijd om te reageren. Dit stond tot 2021 letterlijk als uitzondering in de regels. Nu valt het onder de vraag of de armstand te verklaren is: een duidelijke afketsing weegt zwaar, maar stond de arm al ver van het lichaam, dan kan het toch hands zijn.</li><li><strong>Steunarm bij vallen.</strong> Valt een speler en zet hij zijn arm tussen zijn lichaam en de grond om zich op te vangen, dan is dat een natuurlijke beweging. Steekt hij de arm opzij of omhoog, dan niet.</li><li><strong>Eigen doelpunt via de arm.</strong> Het verbod op scoren met de arm geldt alleen voor de aanvallende ploeg. Werkt een verdediger de bal via zijn arm in zijn eigen doel, dan telt het doelpunt gewoon.</li></ul>
<h3><strong>Welke hands-regels gelden voor de keeper?</strong></h3>
<p>Buiten zijn eigen strafschopgebied is de keeper een gewone speler en gelden dezelfde hands-regels als voor iedereen. In zijn eigen strafschopgebied mag hij de bal met zijn handen spelen, met een paar uitzonderingen. Hij mag de bal niet met de hand pakken:</p>
<ul><li>nadat hij de bal heeft losgelaten en niemand anders de bal heeft geraakt;</li><li>als een medespeler de bal bewust naar hem trapt (de terugspeelbal);</li><li>als hij de bal direct uit een inworp van een medespeler krijgt.</li></ul>
<p>Daarop staat een indirecte vrije schop, zonder kaart. Een strafschop of rode kaart voor hands kan de keeper in zijn eigen strafschopgebied dus niet krijgen. Sinds 2025/26 mag de keeper de bal bovendien niet langer dan acht seconden in zijn handen houden. Doet hij dat wel, dan krijgt de tegenstander een hoekschop.</p>
<h3><strong>Wanneer krijg je een strafschop voor hands?</strong></h3>
<p>Maakt een verdediger hands in zijn eigen strafschopgebied, dan volgt een strafschop. Buiten het strafschopgebied is het een directe vrije schop. Maakt een aanvaller hands, dan krijgt de verdedigende ploeg een directe vrije schop. Een aanvaller die in de zestien de bal met zijn hand aanneemt, krijgt geen kaart, tenzij hij daarmee probeerde te scoren. Hoe een penalty precies genomen wordt en wanneer hij over moet, lees je in ons artikel over de <a href="{STRAF}">regels voor de strafschop</a>.</p>
<p>In de <a href="/competities/eredivisie">Eredivisie</a> werkt de KNVB sinds het seizoen 2018/19 bij alle wedstrijden met een VAR. Die mag alleen ingrijpen bij een duidelijke fout of een gemist voorval rond een doelpunt, een strafschop, een directe rode kaart of een persoonsverwisseling. Een twijfelachtige handsbal waarbij de scheidsrechter een verdedigbare keuze maakte, blijft dus vaak staan. In de KNVB Beker wordt de VAR in 2026/27 pas vanaf de achtste finales ingezet. Wat er dit seizoen verder veranderde, lees je in ons overzicht van de <a href="{SPELREGELS}">nieuwe spelregels in de Eredivisie</a>.</p>
<h3><strong>Wanneer krijg je geel of rood voor hands?</strong></h3>
<p>Een kaart hangt af van wat de hands tegenhoudt en of hij opzettelijk was. De spelregels maken bij hands in het eigen strafschopgebied onderscheid, om een ploeg niet dubbel te straffen: de strafschop geeft de kans al grotendeels terug.</p>
{tabel(["Situatie", "Spelhervatting", "Kaart"], SANCTIES)}
<p>Een duidelijke scoringskans beoordeelt de scheidsrechter aan de hand van de afstand tot het doel, de richting van het spel, de kans dat de aanvaller de bal houdt of krijgt, en de plaats en het aantal verdedigers en aanvallers. Dat laatste, de aanvallers, staat er sinds 2026/27 bij. Nieuw is ook dat er geen kaart meer volgt als de scheidsrechter voordeel geeft en er toch wordt gescoord.</p>
<p>Na een rode kaart volgt in het betaald voetbal een schorsing. De tuchtcommissie van de KNVB bepaalt hoe lang en kan een kaart ook seponeren, bijvoorbeeld als op de beelden niet vast te stellen is dat er echt een scoringskans was.</p>"""

content3 = f"""<h3><strong>Overzicht: is het hands of niet?</strong></h3>
<p>Deze tabel zet de bekendste situaties op een rij, volgens de spelregels van 2026/27. Bij 'meestal niet' beslist de scheidsrechter, en bij een strafschop of doelpunt eventueel de VAR.</p>
{tabel(["Situatie", "Hands?", "Toelichting"], SITUATIES)}
<h3><strong>Wat betekent hands voor je weddenschap?</strong></h3>
<p>Een strafschop of een afgekeurd doelpunt kan een uitslag omgooien, en daarmee ook je weddenschap. Een benutte penalty in de wedstrijd telt gewoon mee bij <a href="{OU}">over/under</a> en bij de <a href="{DOELP}">doelpuntenmaker</a>. Een doelpunt dat na hands door de VAR wordt afgekeurd, telt niet: bookmakers rekenen af op de officiële uitslag. Wedden op de gebeurtenis zelf kan in Nederland niet. Weddenschappen op het veroorzaken of nemen van strafschoppen, op overtredingen en op gele of rode kaarten zijn verboden, net als <a href="{CORNERS}">wedden op corners</a>. Wat er gebeurt als een wedstrijd niet wordt uitgespeeld, lees je bij <a href="{GESTAAKT}">wedstrijd gestaakt</a>.</p>
<p>Wed je, doe dat dan alleen bij een <a href="{LEGAAL}">legale bookmaker</a> en lees onze tips over <a href="{BEWUST}">verantwoord wedden</a>. Meer uitleg over regels en wedden vind je in de <a href="/wedgids">wedgids</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Is een bal tegen de schouder hands?</strong><br>Nee. Voor hands telt alleen de arm onder de onderkant van de oksel. Een doelpunt met de schouder is geldig, ook als het bewust gebeurt.</p>
<p><strong>Is het altijd hands als de bal de arm raakt?</strong><br>Nee. Het is hands als de aanraking opzettelijk is, als de arm het lichaam onnatuurlijk groter maakt, of als een aanvaller met of vlak na een aanraking met zijn arm scoort. Een arm dicht bij het lichaam is geen hands.</p>
<p><strong>Wanneer krijg je rood voor hands?</strong><br>Als je met opzettelijke hands een doelpunt of een duidelijke scoringskans voorkomt, waar op het veld ook. Buiten je eigen strafschopgebied geldt dat ook voor niet-opzettelijke hands. Ontneem je in je eigen strafschopgebied met niet-opzettelijke hands een scoringskans, dan volgen een strafschop en geel.</p>
<p><strong>Telt een doelpunt als een medespeler eerst per ongeluk hands maakte?</strong><br>Ja. Sinds 2021 geldt de strenge regel alleen voor de speler die zelf scoort. Een medespeler die de bal per ongeluk met zijn arm raakte, maakt geen overtreding.</p>
<p><strong>Kan de keeper hands maken?</strong><br>Ja, buiten zijn eigen strafschopgebied. Daarbinnen kan hij de bal alleen op het verkeerde moment pakken, bijvoorbeeld na een terugspeelbal. Dan volgt een indirecte vrije schop, zonder kaart.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    html = content + content2 + content3
    assert re.search(r"<(ul|ol|/li)>\s+<", html) is None
    assert "/kennisbank/" not in html and "<h2" not in html and "<h4" not in html and "/go/" not in html
    assert html.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert content.startswith("<p><strong>")
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert len(OG_CHIPS) == 2 and len(OG_DATA) == 4 and html.count("<table") == 2
    for link in LINKS:
        assert f'href="{link}"' in html, link
    assert not re.search(r'href="(?!/)', html), "alleen relatieve links"
    assert all(h.startswith("<strong>") for h in re.findall(r"<h3>(.*?)</h3>", html))
    for verboden in ("FootyMetrics", "footymetrics", "BetCity", "opstellingvandaag", "waaroptv"):
        assert verboden not in html, verboden
    faq = content3.split("Veelgestelde vragen")[1]
    assert 4 <= faq.count("<p><strong>") <= 6
    tekst = re.sub(r"<[^>]+>", " ", html)
    woorden = len(tekst.split())
    assert 1200 <= woorden <= 2200, woorden
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", woorden, "woorden |",
          [len(re.sub(r"<[^>]+>", " ", c).split()) for c in (content, content2, content3)])
    # ---- --live: NIET zelf draaien; alleen na akkoord van Jasper (bij voorkeur via
    #      wg_publiceer.py handsbal strafschop-regels --live, dat ook de deelkaart en wedgids-categorie regelt) ----
    if "--live" in sys.argv:
        fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
              "samenvatting": SAMENVATTING, "rubriek": RUBRIEK, "wedgids": True,
              "publicatiedatum": datetime.now(timezone.utc).isoformat()}
        print("item:", WF.create_live(fd), "https://www.bet-experts.nl/nieuws/" + SLUG)
