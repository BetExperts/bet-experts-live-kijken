# -*- coding: utf-8 -*-
"""NIEUW wedgids-artikel (Nieuws, nog geen item): wat is DOGSO? De noodrem en wanneer het rood is.
Slug wat-is-dogso-noodrem-rode-kaart (gaf HTTP 404 op 10-11-2026, dus vrij; wat-is-dogso gaf ook 404).
Rubriek Speluitleg, wedgids-categorie 'Sporten en regels'. Onderwerp: Engelstalige analysesite (alleen het onderwerp;
twee pagina's: DOGSO en 'professional foul').
Zoekwoorden: 'wat is dogso' (hoofd), 'dogso betekenis', 'noodrem voetbal rode kaart', 'duidelijke scoringskans ontnemen',
'professional foul', 'veelbelovende aanval geel', 'penalty en rood triple punishment', 'hands doellijn rood'.

Feiten nagelopen op 10-11-2026 (bronnen NIET in de tekst genoemd, behalve 'de spelregels' en 'de KNVB'):
- IFAB Laws of the Game 2026/27 (downloads.theifab.com/downloads/laws-of-the-game-202627-single-pages, 'Effective from
  1st July 2026'), Law 12 par. 3/4:
  - DOGSO in eigen strafschopgebied + strafschop: geel als de overtreding 'an attempt to play the ball or a challenge for
    the ball' was; in alle andere gevallen (vasthouden, trekken, duwen, geen mogelijkheid de bal te spelen) rood.
  - DOGSO door opzettelijke hands: rood waar dan ook (behalve keeper in eigen strafschopgebied). Niet-opzettelijke hands
    + strafschop: geel; niet-opzettelijke hands buiten eigen strafschopgebied: rood.
  - Rood voor DOGSO met een vrije-schop-overtreding bij een tegenstander 'whose overall movement is towards the
    offender's goal'. Wissel/gewisselde speler die zonder toestemming het veld in komt en een kans ontneemt: rood.
  - Vier overwegingen: afstand tot het doel, algemene richting van het spel, waarschijnlijkheid de bal te houden of te
    krijgen, plaats en aantal verdedigers 'and attackers'.
  - Geel voor SPA (veelbelovende aanval onderbreken), behalve bij een strafschop voor een overtreding die een poging was
    de bal te spelen; hands om een veelbelovende aanval te stoppen = geel, behalve bij een strafschop voor
    niet-opzettelijke hands.
  - Voordeel na DOGSO: geel, behalve als er door het voordeel een doelpunt valt (dan geen kaart); voordeel na SPA: geen
    kaart. Hands bij een poging te scoren: geel.
  - Ernstig gemeen spel (excessive force / gevaar voor de tegenstander): altijd rood.
- Wijzigingen 2026/27 (IFAB circulaire 32 van 31-03-2026, AGM 28-02-2026; 'Laws of the Game 2026/27 - Law changes';
  bevestigd in KNVB 'Spelregels 2026/'27' van 1-6-2026, knvb.nl/downloads/bestand/29991): (1) geen gele kaart voor DOGSO
  als voordeel wordt gegeven en er een doelpunt valt; (2) 'aanvallers' toegevoegd aan de vierde overweging. Nederlandse
  termen uit het KNVB-document: 'ontnemen van een duidelijke scoringskans', 'veelbelovende aanval', 'voordeelregel'.
- 2016/17-wijziging ('triple punishment'): IFAB circulaire 5 (2016) en Sky Sports/Premier League-berichtgeving: DOGSO in
  het strafschopgebied met een poging de bal te spelen wordt geel i.p.v. rood; rood blijft bij hands, vasthouden, trekken,
  duwen of geen poging de bal te spelen.
- VAR: KNVB-protocol 2026/27: directe rode kaarten zijn herzienbaar, bij DOGSO 'met name plaats van de overtreding en
  positie van de andere spelers'.
- Schorsing: KNVB RTBV (Reglementen Betaald Voetbal juli 2026, knvb.nl/downloads/bestand/29888) art. 34 (automatisch 1
  wedstrijd), art. 22 lid 1a (max. 2 wedstrijden bij scoringskans ontnemen door hands of vrije-schop-overtreding),
  art. 28 lid 2 (alleen het eigen elftal). UEFA Disciplinary Regulations editie 2026, art. 15 lid 1a-ix: 1 wedstrijd voor
  het ontnemen van een duidelijke scoringskans.
- Wedden: Regeling kansspelen op afstand, Bijlage 2 (wetten.overheid.nl/BWBR0044767, geldend vanaf 01-04-2026): gele/rode
  kaarten, het veroorzaken en het nemen van strafschoppen zijn verboden weddenschappen.
- 'Professional foul' is geen term uit de spelregels; Engelse spreektaal voor een bewuste overtreding om een aanval of
  kans te stoppen. In het Nederlands: 'noodrem' of 'tactische overtreding'. Algemeen taalgebruik, geen bron nodig.
Onzeker: geen. De voorbeelden zijn fictief; er worden geen echte incidenten of scheidsrechters genoemd.
Bewust weggelaten: de 2026/27-tekstwijziging over hands 'in an unsuccessful attempt to prevent a goal' (voor lezers
verwarrend en niet nodig), futsal/amateurvoetbal (tijdstraf), statistieken over aantallen rode kaarten.
Geen rekenvoorbeeld (spelregelartikel, aanvulling ronde 2); wel een sanctietabel die hieronder uit één functie wordt
opgebouwd en met asserts wordt gecontroleerd.
Interne links gecontroleerd met curl op 10-11-2026: alle HTTP 200, behalve de kruislink naar het nieuwe
schorsingsartikel (gaat tegelijk live).
  ../superodd-agent/.venv/bin/python specials/wg_publiceer.py dogso-noodrem   (dry run)"""
import os, sys, re
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

ITEM_ID = None   # nieuw artikel
SLUG = "wat-is-dogso-noodrem-rode-kaart"
RUBRIEK = "6502b66cd9992658b4037cf5"   # Speluitleg
WEDGIDS_CAT = "Sporten en regels"
TITEL = "Wat is DOGSO? De noodrem en wanneer het rood is"
SAMENVATTING = ("Wat betekent DOGSO in het voetbal? Wanneer de noodrem rood of geel oplevert, wat een veelbelovende aanval "
                "is en wat er in 2026/27 veranderde.")

OG_KOP = "Wat is <span>DOGSO</span>?"
OG_EYEBROW = "De noodrem in het voetbal"
OG_CHIPS = ["Wanneer geel, wanneer rood", "Spelregels 2026/27"]
OG_MOTIEF = "tabel"
OG_DATA = ["Buiten de zestien · rood", "In de zestien, bal gespeeld · geel", "Opzettelijke hands · rood", "Veelbelovende aanval · geel"]

KSA = "<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"
SCHORSING = "/nieuws/schorsing-rode-kaart-hoeveel-wedstrijden"   # het tweede nieuwe artikel (gaat tegelijk live)
SPELREGELS = "/nieuws/nieuwe-spelregels-eredivisie-2026-27-alles-wat-je-moet-weten-op-een-rijtje"
CORNERS = "/nieuws/dit-is-waarom-wedden-op-corners-niet-meer-legaal-is-in-nederland"
PENALTY = "/nieuws/dit-zijn-de-penaltynemers-van-elke-club-in-de-eredivisie-2026-27"
XG = "/nieuws/wat-is-xg-expected-goals"
DOELPUNT = "/nieuws/doelpuntenmaker-wedden-regels"
BEWUST = "/speel-bewust/verantwoord-wedden"
LINKS = (SCHORSING, SPELREGELS, CORNERS, PENALTY, XG, DOELPUNT, BEWUST, "/wedgids")


# ---- sanctie volgens Law 12 (2026/27) ----
def sanctie(soort, in_zestien, poging_bal=False, hands=None, voordeel_goal=None):
    """soort: 'dogso' of 'spa'. hands: None, 'opzet' of 'geen opzet'. voordeel_goal: None (gefloten), True/False.
    Geeft (hervatting, kaart)."""
    if voordeel_goal is not None:   # scheidsrechter liet voordeel lopen
        if soort == "spa":
            return ("Voordeel", "Geen kaart")
        return ("Doelpunt telt", "Geen kaart") if voordeel_goal else ("Voordeel", "Geel")
    hervat = "Strafschop" if in_zestien else "Vrije schop"
    if soort == "dogso":
        if hands == "opzet":
            return hervat, "Rood"
        if hands == "geen opzet":
            return hervat, "Geel" if in_zestien else "Rood"
        return hervat, "Geel" if (in_zestien and poging_bal) else "Rood"
    # spa
    if hands == "geen opzet" and in_zestien:
        return hervat, "Geen kaart"
    if hands is None and in_zestien and poging_bal:
        return hervat, "Geen kaart"
    return hervat, "Geel"


assert sanctie("dogso", False) == ("Vrije schop", "Rood")
assert sanctie("dogso", True, poging_bal=True) == ("Strafschop", "Geel")
assert sanctie("dogso", True, poging_bal=False) == ("Strafschop", "Rood")
assert sanctie("dogso", True, hands="opzet") == ("Strafschop", "Rood") and sanctie("dogso", False, hands="opzet")[1] == "Rood"
assert sanctie("dogso", True, hands="geen opzet") == ("Strafschop", "Geel")
assert sanctie("dogso", False, hands="geen opzet") == ("Vrije schop", "Rood")
assert sanctie("spa", False) == ("Vrije schop", "Geel")
assert sanctie("spa", True, poging_bal=True) == ("Strafschop", "Geen kaart")
assert sanctie("spa", True, poging_bal=False) == ("Strafschop", "Geel")
assert sanctie("spa", False, hands="opzet") == ("Vrije schop", "Geel")
assert sanctie("spa", True, hands="geen opzet") == ("Strafschop", "Geen kaart")
assert sanctie("dogso", True, voordeel_goal=True) == ("Doelpunt telt", "Geen kaart")
assert sanctie("dogso", True, voordeel_goal=False)[1] == "Geel" and sanctie("spa", False, voordeel_goal=False)[1] == "Geen kaart"

SCENARIO = [
    ("Tackle, trekken of duwen buiten de zestien die een duidelijke kans ontneemt", dict(soort="dogso", in_zestien=False)),
    ("Overtreding in de zestien bij een echte poging om de bal te spelen", dict(soort="dogso", in_zestien=True, poging_bal=True)),
    ("Vasthouden, trekken of duwen in de zestien, zonder poging de bal te spelen", dict(soort="dogso", in_zestien=True)),
    ("Opzettelijke hands die een doelpunt of duidelijke kans voorkomt (veldspeler)", dict(soort="dogso", in_zestien=True, hands="opzet")),
    ("Niet-opzettelijke hands in de eigen zestien die een duidelijke kans ontneemt", dict(soort="dogso", in_zestien=True, hands="geen opzet")),
    ("Niet-opzettelijke hands buiten de eigen zestien die een duidelijke kans ontneemt", dict(soort="dogso", in_zestien=False, hands="geen opzet")),
    ("Veelbelovende aanval onderbroken buiten de zestien (SPA)", dict(soort="spa", in_zestien=False)),
    ("Veelbelovende aanval onderbroken in de zestien, met een poging de bal te spelen", dict(soort="spa", in_zestien=True, poging_bal=True)),
    ("Veelbelovende aanval onderbroken in de zestien door vasthouden of duwen", dict(soort="spa", in_zestien=True)),
    ("Hands om een veelbelovende aanval te stoppen, buiten de zestien", dict(soort="spa", in_zestien=False, hands="opzet")),
    ("DOGSO-overtreding, scheidsrechter geeft voordeel en er valt een doelpunt", dict(soort="dogso", in_zestien=False, voordeel_goal=True)),
    ("DOGSO-overtreding, scheidsrechter geeft voordeel maar er valt geen doelpunt", dict(soort="dogso", in_zestien=False, voordeel_goal=False)),
]
KLEUR = {"Rood": "<strong>Rood</strong>", "Geel": "<strong>Geel</strong>", "Geen kaart": "Geen kaart"}
RIJEN = [(s, *(lambda h, k: (h, KLEUR[k]))(*sanctie(**kw))) for s, kw in SCENARIO]
assert sum("Rood" in r[2] for r in RIJEN) == 4 and sum("Geel" in r[2] for r in RIJEN) == 6 and len(RIJEN) == 12

content = f"""<p><strong>DOGSO staat voor 'denying an obvious goal-scoring opportunity': een tegenstander met een overtreding of hands een doelpunt of een duidelijke scoringskans ontnemen. In Nederland heet dat ook wel 'de noodrem trekken'. Buiten het strafschopgebied levert dat altijd rood op. Gebeurt het binnen de zestien en probeerde de verdediger echt de bal te spelen, dan geeft de scheidsrechter een strafschop en alleen geel. Bij vasthouden, duwen of opzettelijke hands blijft het rood.</strong></p>
<p>Wanneer is een kans 'duidelijk', wat is het verschil met het onderbreken van een veelbelovende aanval, en wat veranderde er in het seizoen 2026/27? Hieronder lees je het, met een overzicht van alle situaties en de bijbehorende kaart.</p>
<h3><strong>Wat betekent DOGSO precies?</strong></h3>
<p>DOGSO is de Engelse afkorting uit de spelregels van de IFAB, de organisatie die de voetbalregels wereldwijd vaststelt. In de Nederlandse spelregels van de KNVB heet het 'het ontnemen van een doelpunt of een duidelijke scoringskans'. Commentatoren en scheidsrechters gebruiken de afkorting ook in Nederland steeds vaker.</p>
<p>Het gaat altijd om een situatie waarin een aanvaller vrijwel zeker een grote kans had gekregen, en een tegenstander dat met een overtreding of met de hand voorkomt. Denk aan een spits die alleen op de keeper afloopt en van achteren wordt neergehaald, of een verdediger die een bal op de doellijn met zijn hand wegslaat.</p>
<p>In het Engels hoor je ook de term <strong>professional foul</strong>. Die staat niet in de spelregels: het is spreektaal voor een bewuste, berekende overtreding om een aanval te stoppen. Zo'n overtreding kan een DOGSO zijn (rood), maar ook 'alleen' het onderbreken van een veelbelovende aanval (geel). In het Nederlands spreek je dan van een tactische overtreding.</p>
<h3><strong>Wanneer is een kans 'duidelijk'? De vier overwegingen</strong></h3>
<p>De spelregels geven de scheidsrechter vier punten om af te wegen. Het is geen afvinklijst: hij kijkt naar het totaalbeeld. Maar als één punt duidelijk de andere kant op wijst, bijvoorbeeld omdat er nog een verdediger kan ingrijpen, is het meestal geen DOGSO.</p>
{tabel(["Overweging", "Waar kijkt de scheidsrechter naar?", "Wijst op DOGSO als..."], [
    ("<strong>Afstand tot het doel</strong>", "Hoe ver de overtreding van het doel plaatsvond", "De aanvaller dicht bij het doel is, vaak in of vlak voor de zestien"),
    ("<strong>Richting van het spel</strong>", "Beweegt de aanvaller richting het doel of juist naar de zijlijn?", "De aanvaller recht op het doel afgaat"),
    ("<strong>Controle over de bal</strong>", "Had de aanvaller de bal, of zou hij hem zeker hebben gekregen?", "De bal aan zijn voet is of binnen bereik ligt"),
    ("<strong>Verdedigers en aanvallers</strong>", "Waar staan de andere spelers?", "Er geen verdediger meer tussen aanvaller en doel kan komen, behalve eventueel de keeper"),
])}
<p>Sinds 2026/27 noemen de spelregels bij dat laatste punt ook uitdrukkelijk de <strong>aanvallers</strong>. Staat er een vrije medespeler klaar die de bal zo kan binnentikken, dan kan dat helpen om te bepalen dat er een duidelijke kans was.</p>
<p><strong>Voorbeeld.</strong> In een Eredivisie-duel loopt een spits na een steekpass vanaf de middenlijn alleen op de keeper af. Op 25 meter van het doel trekt de laatste verdediger hem aan zijn shirt naar de grond. De afstand is klein, de spits gaat recht op het doel af, hij heeft de bal en er staat geen verdediger meer tussen hem en de keeper: rood. Loopt de spits op dezelfde plek schuin richting de cornervlag en zit er nog een tweede verdediger in de buurt, dan is het een veelbelovende aanval en blijft het bij geel. <em>Dit voorbeeld is fictief.</em></p>"""

content2 = f"""<h3><strong>Waarom is het binnen de zestien soms maar geel?</strong></h3>
<p>Vroeger kreeg een verdediger die in de zestien een scoringskans ontnam altijd drie straffen tegelijk: een strafschop tegen, een rode kaart en een schorsing. Die 'drievoudige straf' (in het Engels <em>triple punishment</em>) werd te zwaar gevonden, omdat de strafschop de kans al grotendeels teruggeeft.</p>
<p>Sinds het seizoen 2016/17 maken de spelregels daarom onderscheid. Probeerde de verdediger echt de bal te spelen, of ging hij eerlijk een duel aan, dan volgt een strafschop en geel. Was er geen sprake van een poging om de bal te spelen, zoals bij vasthouden, trekken of duwen, dan blijft het rood. Hetzelfde geldt voor een overtreding die op zichzelf al rood is, zoals ernstig gemeen spel: die is overal op het veld rood.</p>
<p>Ook voor de keeper geldt dit. Haalt hij in zijn eigen zestien een doorgebroken spits neer terwijl hij naar de bal duikt, dan volgt een strafschop en geel. Doet hij hetzelfde buiten de zestien, dan is het een vrije schop en rood.</p>
<h3><strong>Wat is het verschil tussen DOGSO en een veelbelovende aanval?</strong></h3>
<p>Niet elke overtreding op een aanvaller is een DOGSO. Is de kans niet 'duidelijk', bijvoorbeeld omdat er nog verdedigers terug kunnen of de aanvaller ver van het doel is, dan spreken de spelregels van het onderbreken van een <strong>veelbelovende aanval</strong>. In het Engels heet dat SPA: <em>stopping a promising attack</em>. De straf is lichter: een gele kaart.</p>
<p>Ook hier telt de plek. Onderbreekt een verdediger in zijn eigen zestien een veelbelovende aanval terwijl hij de bal probeerde te spelen, dan volgt een strafschop zonder kaart. Houdt hij de aanvaller vast of duwt hij hem weg, dan krijgt hij wel geel.</p>
<h3><strong>Hoe zit het met hands?</strong></h3>
<p>Bij hands maken de spelregels onderscheid tussen opzet en geen opzet:</p>
<ul><li><strong>Opzettelijke hands</strong> die een doelpunt of een duidelijke kans voorkomt, is altijd rood, waar het ook gebeurt. De enige uitzondering is de keeper in zijn eigen strafschopgebied.</li><li><strong>Niet-opzettelijke hands</strong> die een duidelijke kans ontneemt, levert in de eigen zestien een strafschop en geel op. Buiten de eigen zestien is het rood.</li><li><strong>Hands om een veelbelovende aanval te stoppen</strong> is geel, behalve als er een strafschop volgt voor niet-opzettelijke hands; dan blijft een kaart achterwege.</li><li><strong>Hands bij een poging te scoren</strong>, zoals een aanvaller die de bal in het doel slaat, is altijd geel.</li></ul>
<h3><strong>Overzicht: welke sanctie bij welke situatie?</strong></h3>
{tabel(["Situatie", "Spelhervatting", "Kaart"], RIJEN)}
<p>Een wisselspeler of gewisselde speler die zonder toestemming het veld op loopt en zo een doelpunt of duidelijke kans voorkomt, krijgt ook rood.</p>"""

content3 = f"""<h3><strong>Wat is er in 2026/27 veranderd?</strong></h3>
<p>Voor het seizoen 2026/27 heeft de IFAB twee wijzigingen doorgevoerd die over DOGSO gaan. Ze gelden sinds 1 juli 2026, ook in de Eredivisie:</p>
<ul><li><strong>Geen kaart als voordeel tot een doelpunt leidt.</strong> Laat de scheidsrechter na een DOGSO-overtreding voordeel lopen en valt er daardoor een doelpunt, dan krijgt de overtreder geen kaart meer. Tot vorig seizoen was dat geel. Valt er geen doelpunt, dan blijft het geel.</li><li><strong>Aanvallers tellen mee.</strong> Bij de vierde overweging kijkt de scheidsrechter nu naar de plaats en het aantal verdedigers én aanvallers.</li></ul>
<p>Daarnaast mag de VAR sinds dit seizoen een rode kaart na een duidelijk onterechte tweede gele kaart herzien. Een overzicht van alle wijzigingen lees je in ons artikel over de <a href="{SPELREGELS}">nieuwe spelregels in de Eredivisie</a>.</p>
<h3><strong>Kijkt de VAR mee bij DOGSO?</strong></h3>
<p>Ja. Een directe rode kaart is een van de beslissingen die de videoscheidsrechter mag herzien als er een duidelijke fout is gemaakt. Bij DOGSO kijkt de VAR vooral naar de plek van de overtreding en de positie van de andere spelers. Het verschil tussen net buiten en net binnen de zestien maakt immers het verschil tussen een vrije schop en een strafschop, en soms tussen rood en geel.</p>
<h3><strong>Hoeveel wedstrijden schorsing krijg je na DOGSO-rood?</strong></h3>
<p>In het Nederlandse betaald voetbal ben je na een directe rode kaart automatisch de volgende wedstrijd geschorst. Voor het ontnemen van een scoringskans geldt een maximum van twee wedstrijden, en die schorsing geldt alleen voor het elftal waarin je speelde. In de Europese toernooien gaat de UEFA bij DOGSO uit van één wedstrijd. Hoe het tuchtrecht werkt en wat er bij gele kaarten gebeurt, lees je in ons artikel over de <a href="{SCHORSING}">schorsing na een rode kaart</a>.</p>
<h3><strong>Wat betekent DOGSO voor je weddenschap?</strong></h3>
<p>Een DOGSO-moment verandert een wedstrijd in één klap: vaak een strafschop of een gevaarlijke vrije schop, en soms een team met tien man. Live quoteringen schuiven direct mee. Wedden op kaarten en op strafschoppen zelf kan in Nederland niet: die markten staan op de lijst van verboden weddenschappen, net als <a href="{CORNERS}">corners</a>. Een benutte strafschop telt wel gewoon als doelpunt, bijvoorbeeld bij een weddenschap op een <a href="{DOELPUNT}">doelpuntenmaker</a>; kijk daarvoor ook naar de vaste <a href="{PENALTY}">penaltynemers in de Eredivisie</a>. Wil je inschatten hoeveel grote kansen een team creëert, dan helpt <a href="{XG}">xG</a> meer dan het aantal rode kaarten. Wed altijd met een vaste limiet; lees ook onze tips voor <a href="{BEWUST}">verantwoord wedden</a>. Meer spelregels en wedtermen vind je in de <a href="/wedgids">wedgids</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wat betekent DOGSO?</strong><br>Denying an obvious goal-scoring opportunity: een tegenstander met een overtreding of hands een doelpunt of een duidelijke scoringskans ontnemen. In Nederland ook wel 'de noodrem trekken'.</p>
<p><strong>Is DOGSO altijd rood?</strong><br>Nee. Binnen het eigen strafschopgebied is het geel als de verdediger echt de bal probeerde te spelen, en ook bij niet-opzettelijke hands. Buiten de zestien, en bij vasthouden, duwen of opzettelijke hands, is het rood.</p>
<p><strong>Wat is het verschil tussen DOGSO en SPA?</strong><br>Bij DOGSO was er een duidelijke scoringskans; dat is meestal rood. Bij SPA ging het om een veelbelovende aanval zonder zo'n duidelijke kans; dat is geel.</p>
<p><strong>Wat is een professional foul?</strong><br>Engelse spreektaal voor een bewuste overtreding om een aanval te stoppen. Afhankelijk van de situatie is het een DOGSO (rood) of het onderbreken van een veelbelovende aanval (geel).</p>
<p><strong>Krijg je geel als de scheidsrechter voordeel geeft na een DOGSO?</strong><br>Sinds 2026/27 niet meer als er door het voordeel een doelpunt valt. Valt er geen doelpunt, dan volgt alsnog geel.</p>
{KSA}"""

if __name__ == "__main__":
    html = content + content2 + content3
    assert not re.search(r"<(ul|ol|/li)>\s+<", html) and "/kennisbank/" not in html and "<h2" not in html and "<h4" not in html
    assert html.rstrip().endswith(KSA) and "/go/" not in html
    assert content.startswith("<p><strong>") and len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert len(OG_CHIPS) == 2 and len(OG_DATA) == 4 and html.count("<table") >= 2
    for link in LINKS:
        assert f'href="{link}"' in html, link
    assert all(h.startswith("<strong>") for h in re.findall(r"<h3>(.*?)</h3>", html))
    faq = content3.split("Veelgestelde vragen")[1]
    assert 4 <= faq.count("<p><strong>") <= 6
    woorden = len(re.sub(r"<[^>]+>", " ", html).split())
    assert 1200 <= woorden <= 2200, woorden
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", woorden, "woorden |",
          [len(re.sub(r"<[^>]+>", " ", c).split()) for c in (content, content2, content3)])
    # Publiceren: NIET zelf; alleen na akkoord van Jasper via wg_publiceer.py dogso-noodrem --live
