# -*- coding: utf-8 -*-
"""NIEUW wedgids-artikel (Nieuws, nog geen item): wisselregels in het voetbal, hoeveel wissels een ploeg mag doen.
Slug wisselregels-voetbal-hoeveel-wissels (gaf HTTP 404 op 10-11-2026, dus vrij). Rubriek Speluitleg,
wedgids-categorie 'Sporten en regels'. Onderwerp: Engelstalige analysesite (alleen het onderwerp, niets overgenomen).
Zoekwoorden: 'hoeveel wissels voetbal' (hoofd), 'wisselregels voetbal', 'wisselmomenten', 'wissels verlenging',
'hoeveel wissels eredivisie', 'wisselspelers op de bank', 'terugwisselen', 'minimaal aantal spelers voetbal'.

Feiten (bron + datum, alles nagelopen op 10-11-2026):
- IFAB Laws of the Game 2026/27, Law 3 (theifab.com/laws/latest/the-players): officiële competities max. 5 wissels;
  topdivisies en A-landenteams met 5 wissels: max. 3 wisselmomenten + extra moment in de rust; wissels van beide teams
  tegelijk = moment voor beide; ongebruikte wissels/momenten mee naar de verlenging; optie 1 extra wissel + 1 extra moment
  in de verlenging; wissels tussen einde reguliere tijd en verlenging en in de rust van de verlenging tellen niet als
  moment. Competitie bepaalt aantal op te geven wissels: 3 tot max. 15. Andere wedstrijden zonder afspraak: max. 6.
  Terugwisselen alleen in jeugd-, veteranen-, aangepast en recreatievoetbal (met toestemming bond). Wisselprocedure: speler
  verlaat het veld bij het dichtstbijzijnde punt, binnen 10 seconden na het wisselbord; invaller alleen bij onderbreking,
  bij de middenlijn, nadat de speler eruit is en na teken scheidsrechter; wissel voltooid als de invaller het veld betreedt.
  Te laat: invaller pas bij eerste onderbreking na 1 minuut na hervatting, wissel niet te annuleren. 3.1: max. 11 spelers,
  wedstrijd mag niet beginnen of doorgaan met minder dan 7; team dat daardoor het staken veroorzaakt verliest in principe
  (reglement competitie). 3.4: elke speler mag met de keeper wisselen als de scheidsrechter het weet, tijdens een
  onderbreking. 3.6: rood vóór inlevering formulier -> niet op te geven; na opgave en vóór aftrap -> vervangen door
  opgegeven wisselspeler (aantal wissels niet minder, die wisselspeler zelf niet te vervangen); na de aftrap niet te
  vervangen; wisselspeler die rood krijgt, niet te vervangen.
- IFAB-nieuws 28-02-2026 (140e AGM, ingang 1 juli 2026) + KNVB 'Spelregels 2026/'27' (knvb.nl/downloads/bestand/29991,
  1 juni 2026): vriendschappelijke A-interlands max. 8 wissels, of 11 als beide teams dat afspreken en de scheidsrechter
  vooraf informeren; 'De beperking van drie wisselmomenten per team blijft van kracht'; tijdslimiet 10 seconden.
- IFAB 13-06-2022 (theifab.com/news/the-ifab-permanently-approves-five-substitute-option-in-top-level-competitions):
  5 wissels permanent (sinds 2020 tijdelijk), ingang 1 juli 2022; max. op te geven wissels van 12 naar 15.
- IFAB 02-03-2024 (theifab.com/news/the-ifab-approves-permanent-concussion-substitutes-...): extra permanente
  hersenschuddingswissels als optie voor competities vanaf 1 juli 2024; max. 1 per team; tegenstander krijgt een extra
  wissel. KNVB-nieuws 25-06-2024 (knvb.nl/node/69348): witte wissel definitief vanaf 2024/'25 in het betaald voetbal (niet
  O21/O18 destijds). KNVB 'Reglementen betaald voetbal' versie juli 2026 (knvb.nl/downloads/bestand/29888, gedownload
  10-11-2026), Reglement Wedstrijden Betaald Voetbal art. 8: lid 1 max. 7 team-officials + max. 12 wisselspelers op de
  bank; lid 3 max. 5 spelers vervangen, 3 momenten, rust telt niet, verlenging: ongebruikte momenten mee + 4e moment + 6e
  speler; tegelijk wisselen = moment voor beide; lid 4 vervangen speler mag niet meer meedoen; lid 6 beginnen met minder
  dan 11 maar meer dan 7 en aanvullen; lid 7 witte wissel (1 extra, tegenstander 1 extra + moment), niet in O21/O19.
  Art. 11: max. 12 invallers op het wedstrijdformulier (O21/O19: 7).
- KNVB 'Handboek competitie veldvoetbal seizoen 2026/'27' (knvb.nl/downloads/sites/bestand/knvb/30142, gedownload
  10-11-2026), 3.6: categorie A mannen/vrouwen (incl. O21, O23): 5 spelers, 3 wisselmomenten (exclusief de rust),
  doorwisselen nee; O15-O17 cat. A: 7, 3, ja; O13/O14 cat. A: 7, onbeperkt, ja; categorie B alle: 7, onbeperkt, ja.
  3.6.1: geen witte wissel in het hele amateurvoetbal. Wedstrijdformulier: max. 7 wisselspelers. knvb.nl/node/67541:
  cat. A senioren in de verlenging 1 extra wissel + 1 extra moment.
- UEFA Nations League 2026/27 (documents.uefa.com, art. 52 + 53, gelezen 10-11-2026): 23 spelers op het
  wedstrijdformulier (finaleronde 26); max. 5 wissels, 6e alleen in de verlenging; max. 3 onderbrekingen + 1 in de
  verlenging; rust e.d. telt niet; gewisselde speler mag niet terug. Hersenschuddingswissel niet in art. 53 -> niet geclaimd.
- EK 2024: UEFA-reglementswijziging 2022-24 (editorial.uefa.com ... amendments_20240503114432.pdf, gelezen 10-11-2026):
  art. 44.01 23 tot 26 spelers op het wedstrijdformulier. ONZEKER: 6e wissel in de verlenging en 3 + 1 momenten bij het EK
  2024 alleen via secundaire bronnen (Bolavip/FourFourTwo) bevestigd, niet in de UEFA-tekst zelf gelezen.
- Bookmakers (spelersmarkten): zie docstring wg_doelpuntenmaker.py (nagelezen 22-10-2026): TOTO speler gerelateerde
  wedopties geldig als de speler het veld betrad in de reguliere speeltijd, ongeacht basisplaats; bet365 'scoort op een
  willekeurig moment' ongeldig als de speler niet begint. Regeling kansspelen op afstand, Bijlage 2, Voetbal, onder r
  (wetten.overheid.nl/BWBR0044767/2026-04-01, 10-11-2026): 'inbrengen van wisselspelers' (aantal, per helft, per team,
  tijdstippen) verboden.
Rekenvoorbeeld wisselmomenten is FICTIEF (gemarkeerd); alles hieronder berekend en ge-assert.

Bewust weggelaten:
- Geen bankgrootte voor het WK 2026 (alleen secundaire bronnen, onderling tegenstrijdig).
- Geen echte incidenten (bijv. teams met 12 man op het veld): niet nodig en niet dubbel bevestigd.
- Witte wissel kort; verwijzing naar het bestaande artikel /nieuws/wat-is-een-witte-wissel.
- Geen bron van het onderwerp genoemd; geen concurrent- of affiliatesites; geen kaarten- of wisselmarkten als wedoptie.
Interne links gecontroleerd op 10-11-2026 (curl, allemaal HTTP 200): zie de asserts onderaan.
Geen INFOGRAPHIC (de tabellen volstaan).
  ../superodd-agent/.venv/bin/python specials/wg_publiceer.py wisselregels [--live]"""
import os, sys, re
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
import lk_webflow as WF
from legaal_data import tabel

ITEM_ID = None   # nieuw artikel
SLUG = "wisselregels-voetbal-hoeveel-wissels"
RUBRIEK = "6502b66cd9992658b4037cf5"   # Speluitleg
WEDGIDS_CAT = "Sporten en regels"
TITEL = "Wisselregels in het voetbal: hoeveel wissels mag je doen?"
SAMENVATTING = ("Hoeveel wissels mag een ploeg doen? Vijf wissels in drie momenten, de extra wissel in de verlenging, "
                "de witte wissel en wisselregels per competitie.")

OG_KOP = "Hoeveel <span>wissels</span> mag je doen?"
OG_EYEBROW = "Spelregels voetbal"
OG_CHIPS = ["5 wissels, 3 momenten", "Regels per competitie"]
OG_MOTIEF = "tabel"
OG_DATA = ["Eredivisie · 5 + witte wissel", "Verlenging · 6e wissel", "Oefeninterland · max. 8", "Minimaal · 7 spelers"]

WITTE = "/nieuws/wat-is-een-witte-wissel"
NIEUWE_REGELS = "/nieuws/nieuwe-spelregels-eredivisie-2026-27-alles-wat-je-moet-weten-op-een-rijtje"
GESTAAKT = "/nieuws/wedstrijd-gestaakt-wat-gebeurd-er-nu-met-je-weddenschap"
DOELPUNTENMAKER = "/nieuws/doelpuntenmaker-wedden-regels"
SCHOTEN = "/nieuws/dit-is-hoe-wedden-op-schoten-op-doel-werkt"
OPTA = "/nieuws/wat-zijn-opta-gegevens-alles-over-schoten-op-doel-en-unibet-weddenschappen"
CORNERS = "/nieuws/dit-is-waarom-wedden-op-corners-niet-meer-legaal-is-in-nederland"
VERLENGING = "/nieuws/weddenschap-bij-bet365-als-een-wedstrijd-naar-verlenging-gaat-zo-werkt-het"
LEGAAL = "/nieuws/legale-goksites-in-nederland"
VERANTWOORD = "/speel-bewust/verantwoord-wedden"
BLESSURETIJD = "/nieuws/blessuretijd-voetbal-extra-tijd-uitgelegd"   # zusterartikel, nog niet live -> NIET linken
LINKS = (WITTE, NIEUWE_REGELS, GESTAAKT, DOELPUNTENMAKER, SCHOTEN, OPTA, CORNERS, VERLENGING, LEGAAL, VERANTWOORD, "/wedgids")

# ---- regels Eredivisie (RWBV art. 8) ----
WISSELS, MOMENTEN = 5, 3
WISSELS_VERL, MOMENTEN_VERL = 6, 4


def tel(wissels, verlenging=False):
    """wissels: lijst (moment, aantal). 'rust'/'voor verlenging' tellen niet als moment. Geeft (gebruikt, momenten, ok)."""
    gratis = {"Rust", "Voor de verlenging", "Rust verlenging"}
    gebruikt = sum(n for _, n in wissels)
    momenten = sum(1 for m, _ in wissels if m not in gratis)
    ok = gebruikt <= (WISSELS_VERL if verlenging else WISSELS) and momenten <= (MOMENTEN_VERL if verlenging else MOMENTEN)
    return gebruikt, momenten, ok


# fictief voorbeeld A: slim verdeeld
A = [("Rust", 2), ("62e minuut", 1), ("78e minuut", 2)]
assert tel(A) == (5, 2, True)
# fictief voorbeeld B: drie losse wissels, daarna zitten de momenten op
B = [("55e minuut", 1), ("67e minuut", 1), ("80e minuut", 1)]
assert tel(B) == (3, 3, True)
assert tel(B + [("88e minuut", 1)]) == (4, 4, False)                       # vierde moment in de 90 minuten: niet toegestaan
B_VERL = B + [("Voor de verlenging", 2), ("105e minuut", 1)]
assert tel(B_VERL, verlenging=True) == (6, 4, True)                          # 2 gratis voor de verlenging + 6e wissel op moment 4
assert tel(B_VERL + [("115e minuut", 1)], verlenging=True)[2] is False     # 7e wissel kan niet

RIJ = lambda lijst: [(m, str(n), "Nee" if m in {"Rust", "Voor de verlenging"} else "Ja") for m, n in lijst]

content = f"""<p><strong>In het profvoetbal mag een ploeg vijf spelers wisselen, verdeeld over maximaal drie momenten tijdens de wedstrijd. Wisselen in de rust telt niet als moment. Komt er een verlenging, dan krijgt elke ploeg er een zesde wissel en een vierde moment bij. In de Eredivisie en Keuken Kampioen Divisie mag daarnaast één extra 'witte wissel' bij een (vermoedelijke) hersenschudding. Een gewisselde speler mag niet terug in het veld.</strong></p>
<p>Dat klinkt simpel, maar in de praktijk zijn er veel uitzonderingen. Hoeveel spelers mogen er op de bank? Wat geldt er bij een oefeninterland van Oranje? En wat gebeurt er als een team door blessures en rode kaarten te weinig spelers overhoudt? Hieronder staan de regels op een rij, volgens de spelregels van de IFAB (2026/27) en de reglementen van de KNVB.</p>
<h3><strong>Hoeveel wissels mag je doen in het voetbal?</strong></h3>
<p>De spelregels zeggen dat een officiële competitie maximaal vijf wissels per ploeg mag toestaan. Die vijf wissels werden in 2020 tijdelijk ingevoerd vanwege de coronapandemie. De IFAB maakte ze in 2022 definitief, vanaf het seizoen 2022/23.</p>
<p>Om te voorkomen dat vijf wissels tot vijf onderbrekingen leiden, gelden er wisselmomenten:</p>
<ul><li><strong>Drie momenten tijdens het spel.</strong> Wissel je bij één onderbreking twee of drie spelers tegelijk, dan telt dat als één moment.</li><li><strong>De rust is gratis.</strong> Wissels in de rust tellen niet als moment.</li><li><strong>Samen wisselen telt voor allebei.</strong> Wisselen beide ploegen bij dezelfde onderbreking, dan heeft elke ploeg een moment gebruikt.</li><li><strong>Ongebruikt gaat mee.</strong> Wissels en momenten die je in de 90 minuten niet gebruikt, mag je in de verlenging nog inzetten.</li></ul>
<p>Deze regels gelden onder meer in de Eredivisie, de Keuken Kampioen Divisie en bij officiële interlands, zoals de Nations League. Het aantal kan per competitie lager zijn, maar nooit hoger dan vijf (plus de extra wissels in de verlenging en bij een hersenschudding).</p>
<h3><strong>Voorbeeld: hoe tel je wisselmomenten?</strong></h3>
<p>Twee trainers gebruiken hun wissels op een andere manier. <em>De voorbeelden zijn fictief.</em></p>
<p><strong>Trainer A</strong> wisselt slim:</p>
{tabel(["Moment", "Aantal wissels", "Telt als wisselmoment?"], RIJ(A) + [("<strong>Totaal</strong>", f"<strong>{tel(A)[0]} wissels</strong>", f"<strong>{tel(A)[1]} momenten</strong>")])}
<p>Trainer A heeft alle {tel(A)[0]} wissels gebruikt, maar pas {tel(A)[1]} van de 3 momenten. Hij houdt dus geen wissel meer over, maar heeft het spel ook maar twee keer stilgelegd.</p>
<p><strong>Trainer B</strong> wisselt steeds één speler:</p>
{tabel(["Moment", "Aantal wissels", "Telt als wisselmoment?"], RIJ(B) + [("<strong>Totaal</strong>", f"<strong>{tel(B)[0]} wissels</strong>", f"<strong>{tel(B)[1]} momenten</strong>")])}
<p>Trainer B heeft nog twee wissels over, maar alle drie momenten zijn op. In de reguliere speeltijd mag hij dus niet meer wisselen, ook niet als er in de 88e minuut een speler geblesseerd raakt. In de Eredivisie kan dan alleen nog een witte wissel bij een (vermoedelijke) hersenschudding. Gaat de wedstrijd naar de verlenging, dan mag trainer B vóór de verlenging zijn twee resterende wissels inzetten zonder dat het een moment kost, en krijgt hij er een zesde wissel en een vierde moment bij.</p>"""

content2 = f"""<h3><strong>Mag je extra wisselen in de verlenging?</strong></h3>
<p>Ja, als de competitie dat toestaat, en dat doen bijna alle grote competities. In de Nederlandse reglementen voor het betaald voetbal krijgt elke ploeg in de verlenging:</p>
<ul><li><strong>een zesde wissel</strong>, ook als de vijf gewone wissels al zijn gebruikt;</li><li><strong>een vierde wisselmoment</strong>, bovenop de momenten die nog over waren;</li><li><strong>gratis wissels</strong> tussen het einde van de 90 minuten en het begin van de verlenging, en in de korte rust van de verlenging.</li></ul>
<p>Hetzelfde geldt in de Nations League en bij de amateurs in categorie A. Een verlenging zie je vooral in bekerwedstrijden, play-offs en de knock-outfase van toernooien.</p>
<h3><strong>Wat is de witte wissel bij een hersenschudding?</strong></h3>
<p>Sinds 1 juli 2024 mogen competities extra wissels bij een hersenschudding gebruiken. De IFAB maakte die regel toen definitief na een proef van een paar jaar. In het Nederlandse betaald voetbal heet dat de <strong>witte wissel</strong>. Die geldt sinds het seizoen 2024/25 in onder meer de Eredivisie en de Keuken Kampioen Divisie.</p>
<ul><li>Elke ploeg mag maximaal één witte wissel per wedstrijd gebruiken, bij een (vermoedelijke) hersenschudding.</li><li>De witte wissel telt niet mee voor de vijf gewone wissels en de drie momenten.</li><li>De tegenstander krijgt dan direct ook een extra wissel en een extra wisselmoment.</li><li>De witte wissel geldt niet in de competities onder 21 en onder 19, en in het hele amateurvoetbal niet.</li></ul>
<p>Hoe dat in de praktijk gaat en wie de beslissing neemt, lees je in ons artikel <a href="{WITTE}">wat is een witte wissel</a>.</p>
<h3><strong>Hoeveel wisselspelers mogen er op de bank?</strong></h3>
<p>Het aantal wissels en het aantal wisselspelers zijn twee verschillende dingen. Een ploeg mag vijf keer wisselen, maar mag vaak veel meer spelers op het wedstrijdformulier zetten. De spelregels laten competities kiezen tussen 3 en maximaal 15 op te geven wisselspelers. In de Eredivisie zijn dat er maximaal twaalf.</p>
{tabel(["Competitie", "Wissels", "Wisselmomenten", "Wisselspelers op het formulier", "Gewisselde speler terug?"], [
    ("<strong>Eredivisie en Keuken Kampioen Divisie</strong>", "5, bij verlenging 6, plus de witte wissel", "3 + rust, bij verlenging 4", "Max. 12", "Nee"),
    ("<strong>Nations League 2026/27</strong>", "5, bij verlenging 6", "3 + rust, bij verlenging 4", "Max. 12 (finaleronde 15)", "Nee"),
    ("<strong>EK 2024</strong>", "5, bij verlenging 6", "3 + rust, bij verlenging 4", "Hele selectie van max. 26, dus tot 15", "Nee"),
    ("<strong>Oefeninterland (A-elftal)</strong>", "Max. 8, of 11 als beide teams dat afspreken", "3 + rust", "Max. 15", "Nee"),
    ("<strong>Amateurs categorie A (senioren)</strong>", "5", "3 (de rust telt niet)", "Max. 7", "Nee"),
    ("<strong>Amateurs categorie B</strong>", "7", "Onbeperkt", "Max. 7", "Ja (doorwisselen)"),
])}
<p><em>Bronnen: IFAB-spelregels 2026/27, KNVB-reglementen betaald voetbal (juli 2026), KNVB-handboek competitie veldvoetbal 2026/27 en de UEFA-reglementen.</em></p>
<p>De regel voor oefeninterlands is nieuw dit seizoen. Tot vorig seizoen mochten A-landenteams in een oefenduel maximaal zes keer wisselen. Sinds 2026/27 zijn dat er acht, of elf als beide bonden dat vooraf afspreken en de scheidsrechter informeren. Ook dan blijft het bij drie wisselmomenten plus de rust.</p>
<h3><strong>Mag een gewisselde speler terug in het veld?</strong></h3>
<p>In het profvoetbal niet. Wie eruit is gehaald, doet niet meer mee, ook niet in de verlenging of de strafschoppenserie. De spelregels staan terugwisselen alleen toe in het jeugd-, veteranen-, aangepast en recreatievoetbal, als de bond dat goedkeurt.</p>
<p>De KNVB heeft daar voor het amateurvoetbal eigen regels voor. In de lagere amateurklassen (categorie B) mag een ploeg zeven wisselspelers opgeven en onbeperkt doorwisselen. Ook in een deel van de jeugdcompetities mag dat. In de hoogste amateurklassen (categorie A senioren) gelden dezelfde regels als bij de profs: vijf wissels, drie momenten en niet terug.</p>
<h3><strong>Hoe verloopt een wissel volgens de regels?</strong></h3>
<p>Een wissel gaat in vaste stappen. Sinds dit seizoen zit er een tijdslimiet in.</p>
<ul><li><strong>1. Melden.</strong> De ploeg meldt de wissel bij de vierde official of de scheidsrechter. Wisselen mag alleen als het spel stilligt.</li><li><strong>2. Bord omhoog.</strong> De vierde official laat de rugnummers zien op het wisselbord.</li><li><strong>3. Binnen tien seconden eruit.</strong> De speler die eruit gaat, moet het veld binnen tien seconden verlaten, via het dichtstbijzijnde punt van de lijn. Bij meerdere wissels tegelijk geldt: tien seconden na de laatste aangekondigde wissel.</li><li><strong>4. Invaller erin.</strong> De invaller komt bij de middenlijn het veld in, pas als de andere speler eruit is en de scheidsrechter een teken geeft. Vanaf dat moment is de wissel voltooid.</li></ul>
<p>Doet een speler langer dan tien seconden over het verlaten van het veld, dan moet hij er toch af, maar mag de invaller pas bij de eerste onderbreking nadat er een minuut is gespeeld. De ploeg speelt dan dus even met tien man. De wissel kan niet meer worden teruggedraaid. Een geblesseerde speler of een onveilige situatie is een uitzondering. Lees meer over alle wijzigingen van dit seizoen in ons overzicht van de <a href="{NIEUWE_REGELS}">nieuwe spelregels in de Eredivisie</a>.</p>"""

content3 = f"""<h3><strong>Wat gebeurt er met een speler die rood krijgt?</strong></h3>
<p>Krijgt een speler na de aftrap een rode kaart, dan mag hij niet worden vervangen. De ploeg speelt verder met een man minder. Voor de aftrap ligt dat anders:</p>
{tabel(["Situatie", "Wat zeggen de regels?"], [
    ("<strong>Rood vóór het inleveren van het wedstrijdformulier</strong>", "De speler mag niet op het formulier, als basisspeler noch als wisselspeler"),
    ("<strong>Rood na het inleveren, maar vóór de aftrap</strong>", "Een opgegeven wisselspeler neemt zijn plaats in. De ploeg houdt al zijn wissels. Die wisselspeler kan zelf niet meer worden vervangen op de bank"),
    ("<strong>Rood na de aftrap</strong>", "Niet te vervangen: de ploeg speelt met een man minder"),
    ("<strong>Wisselspeler krijgt rood</strong>", "Hij mag niet meer meedoen en kan niet worden vervangen. Het aantal wissels van de ploeg blijft gelijk"),
])}
<p>Krijgt de keeper rood terwijl er nog wissels zijn, dan haalt de trainer meestal een veldspeler eraf en brengt hij de reservekeeper in. Zijn de wissels op, dan gaat een veldspeler op doel. Dat mag altijd, als de scheidsrechter het vooraf weet en het tijdens een onderbreking gebeurt.</p>
<h3><strong>Met hoeveel spelers moet een team minimaal spelen?</strong></h3>
<p>Een wedstrijd mag niet beginnen of doorgaan als een ploeg minder dan <strong>zeven spelers</strong> heeft. Dat kan gebeuren door rode kaarten en blessures als alle wissels al op zijn. Zakt een ploeg onder de zeven, dan wordt de wedstrijd gestaakt. Heeft die ploeg dat zelf veroorzaakt, dan verliest ze in principe, maar het precieze gevolg staat in het reglement van de competitie. Bij de profs beslist in Nederland de KNVB.</p>
<p>Een ploeg mag ook met minder dan elf spelers beginnen, zolang het er minstens zeven zijn. Spelers die te laat komen, mogen later nog in het veld komen om het team aan te vullen tot elf. Wat een gestaakte wedstrijd voor een weddenschap betekent, lees je in <a href="{GESTAAKT}">wedstrijd gestaakt, wat gebeurt er met je weddenschap</a>.</p>
<h3><strong>Wat betekenen wissels voor je weddenschap?</strong></h3>
<p>Wissels hebben vooral invloed op weddenschappen op spelers, zoals een <a href="{DOELPUNTENMAKER}">doelpuntenmaker</a> of <a href="{SCHOTEN}">schoten op doel</a>. Wordt jouw speler na een uur gewisseld, dan blijft je weddenschap gewoon staan: hij heeft meegedaan. Doet hij helemaal niet mee, dan is de weddenschap meestal ongeldig en krijg je je inzet terug. Let op: de regels verschillen per bookmaker. Bij TOTO is een spelersweddenschap geldig zodra de speler in de reguliere speeltijd het veld betreedt. Bij bet365 is 'scoort op een willekeurig moment' ongeldig als de speler niet in de basis begint. Kijk dus naar de opstelling voor je inzet, en lees hoe <a href="{OPTA}">officiële wedstrijddata</a> bepaalt wat er telt.</p>
<p>Op de wissels zelf kun je in Nederland niet wedden. Het aantal wissels en het moment waarop een wissel valt, staan op de lijst van verboden weddenschappen, net als <a href="{CORNERS}">corners en kaarten</a>. Wed alleen bij <a href="{LEGAAL}">legale bookmakers</a> en houd het bij een vast bedrag: <a href="{VERANTWOORD}">verantwoord wedden</a>.</p>
<p>Gaat een bekerwedstrijd naar de verlenging? Bij de meeste markten telt alleen de reguliere speeltijd, zie <a href="{VERLENGING}">wat er met je weddenschap gebeurt bij een verlenging</a>. Meer spelregels en uitleg vind je in de <a href="/wedgids">wedgids</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoeveel wissels mag je doen in de Eredivisie?</strong><br>Vijf, verdeeld over drie momenten plus de rust. Bij een verlenging komt er een zesde wissel en een vierde moment bij, en bij een (vermoedelijke) hersenschudding mag elke ploeg één extra witte wissel inzetten.</p>
<p><strong>Telt wisselen in de rust als wisselmoment?</strong><br>Nee. Wissels in de rust, voor de verlenging en in de rust van de verlenging tellen niet mee voor het aantal momenten. Ze tellen wel mee voor het aantal wissels.</p>
<p><strong>Hoeveel wisselspelers mogen er op de bank in de Eredivisie?</strong><br>Maximaal twaalf, naast maximaal zeven stafleden. In de competities onder 21 en onder 19 zijn het er maximaal zeven.</p>
<p><strong>Mag een gewisselde speler weer terugkomen?</strong><br>In het profvoetbal en de hoogste amateurklassen niet. In de lagere amateurklassen (categorie B) en een deel van het jeugdvoetbal mag wel worden doorgewisseld.</p>
<p><strong>Hoeveel spelers moet een team minimaal hebben?</strong><br>Zeven. Met minder spelers mag een wedstrijd niet beginnen of doorgaan.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    html = content + content2 + content3
    assert not re.search(r"<(ul|ol|/li)>\s+<", html) and "/kennisbank/" not in html and "<h2" not in html and "<h4" not in html
    assert html.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert content.startswith("<p><strong>") and "/go/" not in html and BLESSURETIJD not in html
    assert len(TITEL) <= 60 and TITEL.startswith("Wisselregels") and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert len(OG_CHIPS) == 2 and len(OG_DATA) == 4 and html.count("<table") >= 4
    for link in LINKS:
        assert link in html, link
    for h in re.findall(r"<h3>(.*?)</h3>", html):
        assert h.startswith("<strong>") and h.endswith("</strong>"), h
    faq = content3.split("Veelgestelde vragen")[1]
    assert 4 <= faq.count("<p><strong>") <= 6
    tekst = re.sub(r"<[^>]+>", " ", html)
    woorden = len(tekst.split())
    assert 1200 <= woorden <= 2200, woorden
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", woorden, "woorden")
    if "--live" in sys.argv:   # NIET zelf draaien; alleen na akkoord (bij voorkeur via wg_publiceer.py wisselregels --live)
        fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
              "samenvatting": SAMENVATTING, "rubriek": RUBRIEK, "wedgids": True,
              "publicatiedatum": datetime.now(timezone.utc).isoformat()}
        print("item:", WF.create_live(fd), "https://www.bet-experts.nl/nieuws/" + SLUG)
