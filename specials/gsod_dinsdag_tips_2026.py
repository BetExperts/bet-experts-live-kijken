# -*- coding: utf-8 -*-
"""Los artikel: Grand Slam of Darts 2026, voorspellingen en wedtips voor dinsdagavond 17 november
(derde en laatste groepsronde van de groepen I t/m P, 8 duels, 20:00 NL / 19:00 UK).
Tips: Humphries -2,5 legs (1,76), Aspinall -1,5 legs (1,78), Van Veen -1,5 legs (1,83) en Wade -1,5 legs (1,54). Combi 8,83.
Odds: 711 (Kambi sevelevnl), dinsdag 17-11 ochtend. Unibet gaf exact dezelfde odds (zelfde Kambi-feed).

EIGEN DOORREKENING (de kern van dit artikel, staat nergens anders): per groep uitgerekend welke uitslag welke
speler doorstuurt, uit de officiele uitslagen van za 14 en zo 15 nov + de regel punten -> legsaldo -> onderling.
Script: scratchpad/gsod_groepen.py. Uitkomst:
  J, K, M, N = zuivere knock-out (winnaar pakt de groep, verliezer ligt eruit)
  I = Humphries moet winnen of met 4-5 verliezen; verliest hij met 2+ legs verschil dan gaat NEBRIDA door
      (bij 0-5 gaat Cullen door). LET OP: de eerste doorrekening gebruikte 'onderling resultaat' als derde criterium;
      de officiele PDC-volgorde is punten -> legsaldo -> totaal gewonnen legs -> legs tegen de pijl in.
  L = De Graaf moet met 2+ legs verschil winnen; bij 5-4 staan Van Gerwen, Coates en De Graaf alle drie op
      2 punten, saldo 0 EN 9 gewonnen legs - dan beslist pas criterium 3 (legs gewonnen tegen de pijl in)
  O = Clemens moet met 2+ legs verschil winnen; bij 5-4 gaat Rodriguez door
  P = Sedlacek moet met 3+ legs verschil winnen (5-2 of ruimer); Aspinall overleeft 5-3 en 5-4
Gemiddelden zijn de officiele driepijlsgemiddelden uit de uitslagen van het openingsweekend (gsod_speelschema_2026).
Aspinall gooide 111,68 en Van Veen 110,51: de twee hoogste van alle zestien spelers die dinsdag spelen.

Bewust GEEN tip op: Clemens -1,5 (moet weliswaar met 2+
winnen, maar gooide zondag 84,43), Van Gerwen -1,5 (won zaterdag maar met 5-4), Dobey - Schindler en Ratajski - Sykes
(te dicht bij elkaar). Dat staat zo in de tekst.
Feiten maandaguitslagen + fitheid + H2H: specials/gsod_dinsdag_feiten.md (17-11, tweede ronde).
Daaruit toegevoegd na publicatie: officiele aanvangstijd per wedstrijd (pdc.tv-toernooihub), Zonneveld 5-4 Littler
(einde reeks van 15), Humphries' voedselvergiftiging + zijn eigen 'probably second favourite', Cullens galblaasoperatie,
Sedlacek won in september nog van Aspinall (6-3, PC30), Van Veen 3-1 H2H + oefenzege 6-2 op Humphries, en vooral:
EVANS WON TWEE VAN DE LAATSTE DRIE VAN WADE (3-2 WK, 6-4 Baltic Sea). Die laatste stond er eerst niet in; de eerste
versie had in plaats daarvan een niet-onderbouwde claim over Evans' speeltempo. Verwijderd.
Alle acht groepsscenario's zijn na publicatie geverifieerd tegen de officiele permutatiepagina van Sky Sports: alle acht
komen exact overeen met onze eigen doorrekening. NIET schrijven: rugklachten Dobey (bestaan niet), polsblessure Aspinall
(hij spreekt over 'my throw'), en wie tweede werd in groep A (bronnen spreken elkaar tegen).
  python3 specials/gsod_dinsdag_tips_2026.py   (dry run)
  kaart: ../superodd-agent/.venv/bin/python og_kaarten/gsod.py gsod_dinsdag_tips_2026
  publiceren: set -a; . ../superodd-agent/.env; set +a; ../superodd-agent/.venv/bin/python specials/concept_publiceer.py gsod_dinsdag_tips_2026 --live
  daarna: ... specials/gsod_dinsdag_tips_2026.py --velden"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, "..")); sys.path.insert(0, HIER)
from legaal_data import tabel
import gsod_data as G

SLUG = "grand-slam-of-darts-2026-voorspellingen-wedtips-dinsdag"
RUBRIEK = G.RUBRIEK
BOOKMAKER_711 = "66a8a87062108480763b7309"
TITEL = "Grand Slam of Darts voorspellingen dinsdag: 4 wedtips"
SAMENVATTING = ("Grand Slam of Darts voorspellingen voor dinsdag 17 november: acht beslissingsduels in de groepen I "
                "tot en met P. Vier wedtips met odds en uitleg.")
DATUM = "2026-11-17T19:00:00.000Z"
ODDS = [1.76, 1.78, 1.83, 1.54]
COMBI = "8,83"

OG_EYEBROW = "Darts · dinsdag 17 november"
OG_KOP = "Grand Slam dinsdag:<br><em>4 beste wedtips</em>"
OG_TEGELS = [("Beslissingsduels", "8"), ("Combi-odd", COMBI)]
OG_KOPJE = "Onze tips (best of 9 legs)"
OG_RECHTS = "Leg handicap · 711"
OG_RIJEN = [("Groep I", "Humphries -2,5 v. Cullen", "1,76"),
            ("Groep P", "Aspinall -1,5 v. Sedláček", "1,78"),
            ("Groep M", "Van Veen -1,5 v. Brooks", "1,83"),
            ("Groep K", "Wade -1,5 v. Evans", "1,54")]

L = {"711": '<a href="/bookmakers/711">711</a>',
     "handicap": '<a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">hoe handicap wedden werkt</a>',
     "legaal": '<a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>',
     "dag1": '<a href="/nieuws/grand-slam-of-darts-2026-voorspellingen-wedtips-dag-1">onze tips van dag 1</a>',
     "regels": G.EXTRA["regels"], "viaplay": G.EXTRA["viaplay"], "livekijken": G.EXTRA["livekijken"]}

# (volgorde, groep, wedstrijd, odds thuis - uit)  711, dinsdagochtend 17-11
PROGRAMMA = [("20:15", "J", "Krzysztof Ratajski – Tom Sykes", "1,73 – 2,10"),
             ("20:45", "O", "Gabriel Clemens – Rusty-Jake Rodriguez", "1,28 – 3,70"),
             ("21:15", "N", "Chris Dobey – Martin Schindler", "1,68 – 2,20"),
             ("21:45", "K", "<strong>James Wade – Ricky Evans</strong>", "1,30 – 3,50"),
             ("22:15", "M", "<strong>Gian van Veen – Bradley Brooks</strong>", "1,45 – 2,75"),
             ("22:45", "I", "<strong>Luke Humphries – Joe Cullen</strong>", "1,17 – 5,00"),
             ("23:15", "L", "Michael van Gerwen – Jeffrey de Graaf", "1,54 – 2,50"),
             ("23:45", "P", "<strong>Nathan Aspinall – Karel Sedláček</strong>", "1,43 – 2,85")]

TIPS = [("Humphries – Cullen", "Groep I", "Luke Humphries -2,5 legs", "Leg handicap", "1,76"),
        ("Aspinall – Sedláček", "Groep P", "Nathan Aspinall -1,5 legs", "Leg handicap", "1,78"),
        ("Van Veen – Brooks", "Groep M", "Gian van Veen -1,5 legs", "Leg handicap", "1,83"),
        ("Wade – Evans", "Groep K", "James Wade -1,5 legs", "Leg handicap", "1,54")]

# Eigen doorrekening: (groep, duel, stand voor het duel, wat er nodig is)
NODIG = [("J", "Ratajski – Sykes", "Allebei 2 punten", "<strong>Zuivere knock-out.</strong> De winnaar pakt de groep, de verliezer ligt eruit. Het legsaldo doet niet meer mee."),
         ("K", "Wade – Evans", "Allebei 2 punten", "<strong>Zuivere knock-out.</strong> Wade +4, Evans +1, maar dat maakt niet uit: winnen is door."),
         ("M", "Van Veen – Brooks", "Allebei 2 punten", "<strong>Zuivere knock-out.</strong> Van Veen +3, Brooks +2. Wie wint, speelt woensdag of donderdag verder."),
         ("N", "Dobey – Schindler", "Allebei 2 punten", "<strong>Zuivere knock-out.</strong> Schindler heeft het beste saldo van de hele groepsfase (+5 na 5-0)."),
         ("I", "Humphries – Cullen", "Humphries 2 pt (+2), Cullen 0 pt (–3)", "<strong>Humphries moet winnen, of met 4-5 verliezen.</strong> Verliest hij met twee legs of meer verschil, dan glipt Nebrida erdoorheen — behalve bij 0-5, want dan gaat Cullen zelf door."),
         ("L", "Van Gerwen – De Graaf", "Van Gerwen 2 pt (+1), De Graaf 0 pt (–1)", "Van Gerwen is bij winst door. <strong>De Graaf moet met minstens twee legs verschil winnen</strong>; bij 5-4 staan hij, Van Gerwen én Coates alle drie op 2 punten, saldo nul én negen gewonnen legs."),
         ("O", "Clemens – Rodriguez", "Rodriguez 2 pt (+2), Clemens 0 pt (–1)", "Rodriguez is bij winst door. <strong>Clemens moet met minstens twee legs verschil winnen</strong>: wint hij met 5-4, dan gaat Rodriguez alsnog door."),
         ("P", "Aspinall – Sedláček", "Aspinall 2 pt (+4), Sedláček 0 pt (–1)", "Aspinall is bij winst door en <strong>overleeft zelfs een nederlaag met 3-5 of 4-5</strong>. Sedláček moet met 5-2 of ruimer winnen.")]

# Hoogste driepijlsgemiddelde in het openingsweekend (officiële wedstrijdcijfers)
GEMIDDELDEN = [("Nathan Aspinall", "P", "111,68", "5-1 tegen Kuivenhoven"),
               ("Gian van Veen", "M", "110,51", "5-2 tegen Sneyd"),
               ("Luke Humphries", "I", "105,70", "5-3 tegen Nebrida"),
               ("James Wade", "K", "104,09", "5-1 tegen Crabtree"),
               ("Michael van Gerwen", "L", "100,42", "5-4 tegen Coates"),
               ("Chris Dobey", "N", "98,66", "5-2 tegen Schmidt"),
               ("Bradley Brooks", "M", "97,38", "5-3 tegen Sneyd"),
               ("Karel Sedláček", "P", "94,98", "4-5 tegen Kuivenhoven"),
               ("Ricky Evans", "K", "87,71", "5-4 tegen Crabtree"),
               ("Krzysztof Ratajski", "J", "87,67", "5-1 tegen Woodhouse"),
               ("Martin Schindler", "N", "87,38", "5-0 tegen Schmidt"),
               ("Jeffrey de Graaf", "L", "86,29", "4-5 tegen Coates"),
               ("Tom Sykes", "J", "85,97", "5-3 tegen Woodhouse"),
               ("Gabriel Clemens", "O", "84,43", "4-5 tegen Smith"),
               ("Rusty-Jake Rodriguez", "O", "83,43", "5-3 tegen Smith"),
               ("Joe Cullen", "I", "76,93", "2-5 tegen Nebrida")]

# Laatste 16 van woensdag 18 november: de winnaars van de groepen A t/m H (speelschema 711/PDC)
LAATSTE16 = [("<strong>Luke Littler – Jermaine Wattimena</strong>", "winnaar groep A – winnaar groep B"),
             ("<strong>Kevin Doets – Cameron Menzies</strong>", "winnaar groep C – winnaar groep D"),
             ("<strong>Gerwyn Price – Ryan Searle</strong>", "winnaar groep E – winnaar groep F"),
             ("<strong>Rob Cross – Niko Springer</strong>", "winnaar groep G – winnaar groep H")]

GELD = [("Groepswinnaar (laatste 16)", "£20.000"),
        ("Kwartfinale", "£35.000"),
        ("Halve finale", "£60.000"),
        ("Finalist", "£100.000"),
        ("Winnaar", "£200.000")]


def waarom(punten):
    return "<p><strong>Waarom deze tip?</strong></p><ul>" + "".join(f"<li>{p}</li>" for p in punten) + "</ul>"


def markt(m):
    return f"<p><strong>De markt:</strong> {m}</p>"


UITLEG_HC = ("Leg handicap -1,5: de speler begint in gedachten met 1,5 leg achterstand, dus hij moet met minstens "
             "twee legs verschil winnen. Bij 5-3 win je, bij 5-4 verlies je. Een halve leg zorgt ervoor dat je inzet "
             "nooit wordt teruggestort.")

content = f"""<p><strong>Onze 4 beste wedtips voor dinsdagavond 17 november op de Grand Slam of Darts: Luke Humphries wint met minstens drie legs verschil van Joe Cullen (-2,5 legs, 1,76), en Nathan Aspinall, Gian van Veen en James Wade winnen alle drie met minstens twee legs verschil (-1,5 legs, respectievelijk 1,78, 1,83 en 1,54). Alle vier bij {L['711']}. De sessie begint om 20:00 uur Nederlandse tijd met acht wedstrijden: de derde en laatste groepsronde van de groepen I tot en met P.</strong></p>
<p>Dit is de avond waarop de tweede helft van het toernooi wordt uitgedund van 24 naar 8 spelers. In elk van deze acht groepen gaat <strong>alleen de winnaar</strong> door naar de laatste 16 — er is geen tweede plek. In vier groepen is het vanavond een zuivere knock-out tussen twee spelers met evenveel punten. In de andere vier ligt het subtieler: daar beslist het legsaldo, en dan maakt het ineens uit of iemand met 5-4 of met 5-2 wint. Wij hebben dat per groep uitgerekend; de tabel staat hieronder.</p>
<p>Zaterdag en zondag werden de eerste twee speelrondes afgewerkt, maandagavond vielen de beslissingen in de groepen A tot en met H. Daardoor liggen de eerste vier affiches van de laatste 16 al vast, en die worden woensdag gespeeld.</p>
{tabel(["Woensdag 18 november", "Groepswinnaars"], LAATSTE16)}
<p>Maandagavond leverde meteen de klapper van het toernooi op, en die was Nederlands: <strong>Niels Zonneveld versloeg Luke Littler met 5-4</strong> en maakte daarmee een einde aan Littlers reeks van vijftien opeenvolgende zeges op de Grand Slam. Littler gooide in die partij nog 150 uit met drie keer bull om in leven te blijven, maar had zijn groep toen al gewonnen — Zonneveld niet, en die ligt er ondanks de stunt uit. Ook <strong>Jermaine Wattimena</strong> had het zwaar: hij miste acht matchdarts tegen Alan Soutar voordat hij op dubbel 8 afmaakte. Wessel Nijman verloor met 3-5 van Niko Springer, die in de tweede leg een 11-darter gooide.</p>
<p>Voor Nederland betekent dat twee namen door: <strong>Wattimena</strong> en <strong>Kevin Doets</strong> staan woensdag op het podium. Dinsdagavond kunnen daar Gian van Veen en Michael van Gerwen bij komen. Onze tips van de openingsdag en hoe die uitpakten, lees je in {L['dag1']}. Een tip blijft een inschatting; zet alleen in wat je kunt missen.</p>
<h3><strong>De 4 beste wedtips voor dinsdagavond</strong></h3>
{tabel(["Wedstrijd", "Groep", "Onze tip", "Markt", "Odd"],
       [(f"<strong>{w}</strong>", g, t, m, f"<strong>{o}</strong>") for w, g, t, m, o in TIPS])}
<p><em>Odds bij {L['711']}, opgehaald op dinsdagochtend 17 november. Odds kunnen tot de start nog veranderen. Het zijn vier losse tips: wie ze combineert komt uit op ongeveer {COMBI}, maar dan moeten ze alle vier goed gaan. {UITLEG_HC}</em></p>
<h3><strong>Het programma van dinsdagavond (20:00 uur)</strong></h3>
{tabel(["Tijd", "Groep", "Wedstrijd", "Odds (winnaar)"], PROGRAMMA)}
<p><em>De zaal gaat om 20:00 uur open; dit zijn de officiële richttijden per wedstrijd in Nederlandse tijd. Loopt een partij uit, dan schuift de rest op. Alle groepswedstrijden gaan over best of 9 legs: de eerste speler op vijf legs wint. Onze drie laatste tips staan dus laat op de avond: 21:45, 22:15, 22:45 en 23:45.</em></p>
<h3><strong>Wat heeft iedereen vanavond nodig?</strong></h3>
<p>Dit is de tabel waar het vanavond om draait, en hij staat nergens anders zo uitgeschreven. Wij hebben alle uitslagen van zaterdag en zondag ingevoerd en per groep doorgerekend welke uitslag wie doorstuurt. De volgorde bij gelijke punten is: <strong>eerst het aantal punten, dan het legsaldo, dan het onderlinge resultaat</strong>.</p>
{tabel(["Groep", "Beslissingsduel", "Stand voor het duel", "Wat er moet gebeuren"],
       [(f"<strong>{g}</strong>", f"<strong>{d}</strong>", s, w) for g, d, s, w in NODIG])}
<p><em>Eigen berekening op basis van de officiële uitslagen van het openingsweekend. In de vier knock-outgroepen hebben beide spelers één wedstrijd gewonnen en is de derde speler al uitgeschakeld; in de andere vier heeft de derde speler zijn programma al afgerond en ligt er dus een saldo waar overheen gegooid moet worden.</em></p>"""

content2 = f"""<h3><strong>Tip 1: Luke Humphries – Joe Cullen (groep I)</strong></h3>
<p><strong>De tip: Luke Humphries -2,5 legs, odd 1,76.</strong> Humphries moet met minstens drie legs verschil winnen. Rekenvoorbeeld: bij 5-2 is de tip goed, bij 5-3 is de tip verloren.</p>
<p><strong>Waarom deze markt?</strong> Humphries winnen staat op 1,17 — daar begin je niets mee. De bookmaker vraagt voor drie legs marge 1,76, en dat is de ruimste prijs die wij vanavond op een duidelijk klasseverschil zien.</p>
<p><strong>Het klasseverschil.</strong> Humphries gooide zaterdag 105,70 tegen Paolo Nebrida. Cullen speelde zondag tegen diezelfde Nebrida en kwam tot <strong>76,93</strong> — het laagste gemiddelde van alle zestien spelers die dinsdagavond aantreden, bijna negenentwintig punten onder dat van zijn tegenstander. Hij verloor die partij met 2-5. Dat is dus een directe vergelijking: dezelfde tegenstander, hetzelfde podium, dezelfde week.</p>
<p><strong>En anders dan het lijkt, moet Humphries echt aan de bak.</strong> Op het eerste gezicht is hij al zo goed als door. Uit onze doorrekening blijkt iets anders: hij gaat alleen verder als hij <strong>wint of met 4-5 verliest</strong>. Verliest hij met twee legs verschil of meer, dan heeft Nebrida een beter legsaldo en ligt de nummer één van de plaatsingslijst eruit. Humphries kan het zich dus niet veroorloven om de partij te laten lopen — en dat is precies wat je wilt bij een handicap.</p>
{waarom(["Humphries gooide 105,70 tegen Nebrida; Cullen kwam tegen dezelfde speler tot 76,93 en verloor met 2-5.",
         "76,93 is het laagste gemiddelde van alle zestien spelers die dinsdagavond spelen.",
         "Humphries moet winnen of hoogstens met 4-5 verliezen, anders gaat Nebrida door: hij kan niet gas terugnemen.",
         "Cullen heeft alleen aan een 5-0 genoeg om zelf door te gaan — bij elke andere zege profiteert Nebrida. Dat is een slopend scenario om voor te spelen.",
         "Humphries won zijn eigen partij met 5-3 en is de hoogst geplaatste speler van de avond."])}
{markt("Leg handicap -2,5: de speler begint in gedachten met 2,5 leg achterstand en moet dus met minstens drie legs verschil winnen. Bij 5-2 win je, bij 5-3 verlies je.")}
<p><strong>Het fysieke verhaal, en het is er een.</strong> Humphries miste in oktober het EK in Dortmund door een voedselvergiftiging en lag daarna lang stil. Zijn eigen woorden na zijn eerste partij hier: <em>"The food poisoning meant I had to take a step back, and it's like, well, I haven't thrown for probably two or three weeks."</em> En: <em>"Who knows? Am I going to come back and still be the same again, or are we going to have to work for two or three months to try to get back to that level?"</em> Hij noemt zichzelf nu uitdrukkelijk niet de favoriet, maar <em>"probably second favourite"</em>. Dat hoort erbij als je op hem inzet. Daar staat tegenover dat hij in zijn eerste partij gewoon 105,70 gooide, en dat zijn tegenstander een eigen verhaal heeft: Cullen onderging in september een galblaasoperatie en zei daarover <em>"I am not sure how I will play from game to game, which is frustrating as a darts player."</em></p>
<p><strong>De keerzijde.</strong> Dit is de tip met de grootste marge die we vragen: drie legs in een best of 9 betekent dat Cullen hoogstens twee legs mag pakken. Cullen is een voormalig halvefinalist van het WK, en één goede avond verandert veel. Liever veiliger? Humphries -1,5 legs staat op 1,35.</p>
<h3><strong>Tip 2: Nathan Aspinall – Karel Sedláček (groep P)</strong></h3>
<p><strong>De tip: Nathan Aspinall -1,5 legs, odd 1,78.</strong> Aspinall moet met minstens twee legs verschil winnen. Rekenvoorbeeld: bij 5-3 is de tip goed, bij 5-4 is de tip verloren.</p>
<p><strong>Waarom deze markt?</strong> Aspinall winnen staat op 1,43: te laag voor een losse tip. Met de leg handicap vragen we één ding extra en krijgen we een odd die wél de moeite waard is.</p>
<p><strong>Het cijfer dat deze tip draagt.</strong> Aspinall gooide zaterdag tegen Maik Kuivenhoven een gemiddelde van <strong>111,68</strong>. Dat is niet alleen zijn eigen beste partij van het toernooi — het is het <strong>hoogste gemiddelde van alle zestien spelers die dinsdagavond in actie komen</strong>. Hij won die partij met 5-1. Sedláček kwam in zijn enige partij tot 94,98 en verloor die nog ook, met 4-5 van Kuivenhoven.</p>
<p><strong>De situatie werkt mee.</strong> Aspinall staat op twee punten en een saldo van +4. Hij is bij winst door, en door dat ruime saldo overleeft hij zelfs een nederlaag met 3-5 of 4-5. Sedláček heeft nul punten en moet met 5-2 of ruimer winnen om de groep te pakken. Dat is precies de situatie waarin de favoriet rustig kan spelen en de underdog risico moet nemen — en risico nemen in een best of 9 levert zelden een 5-4 op.</p>
{waarom(["Aspinall gooide het hoogste gemiddelde van alle zestien spelers van dinsdagavond: 111,68.",
         "Sedláček verloor zijn enige partij van dit toernooi, met 4-5 van Maik Kuivenhoven.",
         "Aspinall won zijn eigen partij met 5-1, dus ruim binnen deze lijn.",
         "Sedláček moet voor een eigen kans met minstens drie legs verschil winnen; hij kan niet voorzichtig spelen.",
         "Aspinall heeft met +4 het ruimste legsaldo van alle acht spelers die dinsdag nog een kans hebben."])}
{markt(UITLEG_HC)}
<p><strong>Wat die 111,68 precies was.</strong> Het is zijn hoogste televisiegemiddelde ooit én zijn hoogste op een major. Hij gooide in die partij 149 en 120 uit en kwam in de slotleg tot <strong>zeven perfecte darts</strong> voordat de negendarter sneuvelde. Over zijn eigen hoofd is hij open: hij worstelt al langer met zijn worp, maar zegt nu <em>"I'm in a very, very good headspace at the moment."</em> Over vanavond: <em>"He knows I'm going to be on it when I play him, and I'll come out of that game on top."</em></p>
<p><strong>De keerzijde, en die is reëel.</strong> Onderling staat het 6-2 voor Aspinall, maar <strong>Sedláček won de laatste ontmoeting</strong>: 6-3 in Den Bosch in september, op weg naar zijn eerste rankingtitel ooit — de eerste Tsjech met een PDC-titel. Aspinall kan zich bovendien een nederlaag met 4-5 permitteren, en een speler die weet dat hij genoeg heeft aan weinig, speelt soms ook naar weinig. Liever veiliger? Aspinall winnen zonder handicap staat op 1,43.</p>
<h3><strong>Tip 3: Gian van Veen – Bradley Brooks (groep M)</strong></h3>
<p><strong>De tip: Gian van Veen -1,5 legs, odd 1,83.</strong> Van Veen moet met minstens twee legs verschil winnen. Bij 5-3 win je, bij 5-4 verlies je.</p>
<p><strong>Waarom deze markt?</strong> Van Veen winnen staat op 1,45. De handicap verhoogt dat naar 1,83 en vraagt er maar één leg marge voor terug.</p>
<p><strong>Vorm en cijfers.</strong> Van Veen won zaterdag met 5-2 van Carl Sneyd en gooide daarbij <strong>110,51</strong>, het op één na hoogste gemiddelde van de dinsdagavondspelers. Brooks won zondag ook, maar had tegen diezelfde Sneyd meer moeite: 5-3, met een gemiddelde van 97,38. Dertien punten verschil in gemiddelde tegen dezelfde tegenstander is een eerlijke vergelijking — precies dezelfde maatstaf, precies hetzelfde podium.</p>
<p><strong>De situatie.</strong> Dit is een zuivere knock-out: beide spelers staan op twee punten, Sneyd is uitgeschakeld. De winnaar gaat door, de verliezer gaat naar huis. Geen rekenwerk, geen saldo, geen scenario's — en dus ook geen reden voor Van Veen om de handrem erop te houden.</p>
{waarom(["Van Veen gooide 110,51 tegen Carl Sneyd; Brooks kwam tegen dezelfde speler tot 97,38.",
         "Van Veen won met 5-2, Brooks met 5-3: ook in legs was Van Veen overtuigender.",
         "Zuivere knock-out: allebei volledig gemotiveerd, geen enkele reden om te sparen.",
         "Van Veen is dit seizoen gestegen tot de wereldtop en speelt in de zaal waar hij vorig jaar al indruk maakte.",
         "Brooks is de laagst geplaatste van de twee en moet het hebben van een uitschieter."])}
{markt(UITLEG_HC)}
<p><strong>Onderling en vooraf.</strong> Ze speelden vier keer op de Pro Tour, met 3-1 voor Van Veen, en nooit eerder op televisie. Veelzeggender: op 8 november, tien dagen voor dit toernooi, won Van Veen een oefenpartij met 6-2 van Luke Humphries.</p>
<p><strong>De keerzijde, en die is er.</strong> Brooks is geen vulling: hij plaatste zich via het kwalificatietoernooi door Dave Chisnall met 106,31 gemiddeld te verslaan, en gooide hier vijf keer 180. Hij zei zelf over Van Veen: <em>"After looking at Gian and Carl's game yesterday, with those averages, I'm glad I weren't playing in that because I'd probably have lost."</em> Dat klinkt nederig, maar het is ook een man die weet waar hij aan begint. En Van Veens laatste televisiewedstrijd vóór dit toernooi was een 3-0 nederlaag tegen James Wade met 81,6 gemiddeld. Een best of 9 is kort: één break en het staat 5-4. Dit is van onze vier tips degene met de hoogste odd, en dat is niet voor niets. Liever veiliger? Van Veen winnen staat op 1,45.</p>
<h3><strong>Tip 4: James Wade – Ricky Evans (groep K)</strong></h3>
<p><strong>De tip: James Wade -1,5 legs, odd 1,54.</strong> Wade moet met minstens twee legs verschil winnen.</p>
<p><strong>Waarom deze markt?</strong> Wade winnen staat op 1,30 — te kort. Met -1,5 komt de odd op 1,54.</p>
<p><strong>Vorm en cijfers.</strong> Wade rekende zaterdag met <strong>5-1</strong> af met Cam Crabtree en gooide daarbij 104,09. Evans had tegen diezelfde Crabtree alles nodig: hij won met 5-4 en kwam tot 87,71. Zestien punten verschil in gemiddelde, en vier legs verschil in marge, tegen dezelfde tegenstander.</p>
<p><strong>De situatie.</strong> Ook hier een zuivere knock-out: beide spelers op twee punten, Crabtree uitgeschakeld. Wade is met 43 jaar en acht majortitels verreweg de meest ervaren van de twee op dit podium.</p>
{waarom(["Wade won met 5-1 en 104,09 gemiddeld van Crabtree; Evans won van dezelfde speler pas met 5-4 en 87,71.",
         "Zestien punten verschil in driepijlsgemiddelde is in een best of 9 een groot gat.",
         "Zuivere knock-out: de verliezer is uitgeschakeld, dus Wade heeft geen reden om te sparen.",
         "Evans is traditioneel een snelle speler die bij tegenslag nog sneller gaat gooien — zelden goed voor een nipte uitslag.",
         "Wade is de enige van de twee met ervaring in de latere rondes van dit toernooi."])}
{markt(UITLEG_HC)}
<p><strong>De keerzijde, en dit is de belangrijkste van de vier.</strong> Onderling leidt Wade met 8-5, maar <strong>Evans won twee van hun laatste drie duels</strong>: 3-2 op het WK van vorig jaar — waar hij de zevende geplaatste eruit gooide met zijn achtste matchdart — en 6-4 op de Baltic Sea Darts Open in mei. Evans trekt partijen graag naar het einde, en dat deed hij zondag ook met een 5-4 tegen Crabtree. Wade zelf is er bovendien nuchter over: <em>"I haven't felt great for six to eight weeks"</em> en over zijn eigen 104,09: <em>"I'm still shell-shocked by the average."</em> 1,54 is de laagste odd van onze vier, dus de marge is hier het dunst. Liever veiliger? Wade winnen staat op 1,30.</p>
<h3><strong>De vier duels waar we vanaf blijven</strong></h3>
<p><strong>Clemens – Rodriguez (groep O).</strong> Hier klopt het verhaal juist wél: Clemens <em>moet</em> met minstens twee legs verschil winnen, dus zijn belang valt precies samen met de lijn van -1,5 (1,53). Maar zijn cijfer niet: hij gooide zondag 84,43 en verloor met 4-5 van Ross Smith. Een speler die zelf onder de 85 zit, is geen betrouwbare basis voor een handicap, ook niet als hij moet.</p>
<p><strong>Van Gerwen – De Graaf (groep L).</strong> Van Gerwen hoeft alleen maar te winnen en staat op 1,54. Zijn eigen partij ging echter met 5-4 tegen Henry Coates, met 100,42 gemiddeld — geen cijfer waarop je een handicap bouwt. Mooi detail: als De Graaf met 5-4 wint, staan Van Gerwen, Coates en De Graaf alle drie op twee punten en een saldo van nul. De Graaf moet dus met minstens twee legs verschil winnen om het zelf in de hand te houden.</p>
<p><strong>Dobey – Schindler (groep N).</strong> Schindler won met 5-0 en heeft met +5 het beste saldo van de groepsfase, maar deed dat met 87,38 gemiddeld tegen de zwakste speler van de groep. Dobey gooide 98,66. De markt heeft ze op 1,68 om 2,20 en wij zien geen reden om daarvan af te wijken.</p>
<p><strong>Ratajski – Sykes (groep J).</strong> 87,67 om 85,97, en een markt van 1,73 om 2,10. Twee spelers die allebei één keer wonnen en allebei rond hetzelfde niveau gooien. Dit is een kop-of-munt met een knock-out eraan vast: niets voor een tip.</p>
<h3><strong>Het hoogste gemiddelde per speler tot nu toe</strong></h3>
{tabel(["Speler", "Groep", "Beste gemiddelde", "In die partij"],
       [(f"<strong>{s}</strong>", g, f"<strong>{gem}</strong>", w) for s, g, gem, w in GEMIDDELDEN])}
<p><em>Officiële driepijlsgemiddelden uit de wedstrijden van zaterdag 14 en zondag 15 november. Elke speler in de groepen I tot en met P speelde er tot nu toe één; de derde speler van elke groep heeft zijn programma al afgerond. Let op de bovenste twee namen: dat zijn precies de twee spelers waar onze eerste twee tips op staan.</em></p>"""

content3 = f"""<h3><strong>Combinatie dinsdag 17 november</strong></h3>
<p>Alle vier de tips samen: 1,76 × 1,78 × 1,83 × 1,54 = <strong>± {COMBI}</strong>. Een inzet van €10 levert dan ongeveer €88,30 op. Het zijn vier losse partijen die elkaar niet beïnvloeden, maar er moeten wel vier dingen goed gaan in plaats van één — en bij vier tips is de kans dat er eentje misgaat flink. Wie liever minder risico neemt, speelt ze los.</p>
<h3><strong>Hoe werkt de leg handicap bij darts?</strong></h3>
<p>Bij een leg handicap begint een speler in gedachten met een achterstand of voorsprong in legs. Onze drie tips zijn alle drie <strong>-1,5 legs</strong>: de favoriet start op −1,5 en moet dus met minstens twee legs verschil winnen.</p>
{tabel(["Uitslag", "Telt als", "Tip -1,5 legs"], [
    ("5-0, 5-1, 5-2 of 5-3", "winst met 2 tot 5 legs verschil", "<strong>✅ gewonnen</strong>"),
    ("5-4", "winst met 1 leg verschil", "<strong>❌ verloren</strong>"),
    ("4-5 of lager", "nederlaag", "<strong>❌ verloren</strong>"),
])}
<p>De halve leg zorgt ervoor dat de weddenschap nooit gelijk kan eindigen: je wint of je verliest. Hoe hoger de handicap, hoe hoger de odd en hoe kleiner de kans. Meer uitleg staat in {L['handicap']}, en de spelregels zelf vind je in {L['regels']}.</p>
<h3><strong>Waar spelen ze vanavond voor?</strong></h3>
<p>Groepswinst levert niet alleen een plek in de laatste 16 op, maar ook een flinke sprong in het prijzengeld. Dit zijn de bedragen van 2026.</p>
{tabel(["Resultaat", "Prijzengeld"], [(f"<strong>{a}</strong>", b) for a, b in GELD])}
<p>Het verschil tussen groepswinst en uitschakeling is dus minimaal £7.500 — en wie vanavond verliest, is meteen klaar. Nummers twee in de groep krijgen £12.500, maar gaan wel naar huis: in dit toernooi telt alleen de eerste plaats. Meer over het toernooi lees je in {G.a("format", "het format van de Grand Slam of Darts")}, {G.a("speelschema", "het volledige speelschema")} en {G.a("prijzengeld", "het prijzengeld")}.</p>
<h3><strong>Hoe kijk je de Grand Slam of Darts dinsdag?</strong></h3>
<p>De avondsessie loopt van 20:00 tot ongeveer 00:00 uur Nederlandse tijd en is in Nederland te zien bij {L['viaplay']}. Meer kijkopties staan op onze pagina {L['livekijken']}. Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit; in {L['legaal']} leggen we uit waar je dat aan ziet.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wat zijn de beste wedtips voor dinsdag op de Grand Slam of Darts?</strong><br>Luke Humphries -2,5 legs tegen Joe Cullen (1,76), Nathan Aspinall -1,5 legs tegen Karel Sedláček (1,78), Gian van Veen -1,5 legs tegen Bradley Brooks (1,83) en James Wade -1,5 legs tegen Ricky Evans (1,54), alle odds bij 711. Gecombineerd ongeveer {COMBI}.</p>
<p><strong>Hoe laat begint de Grand Slam of Darts dinsdag?</strong><br>Om 20:00 uur Nederlandse tijd (19:00 uur Britse tijd). Er staan acht wedstrijden op het programma; alleen de eerste heeft een vaste aanvangstijd.</p>
<p><strong>Welke wedstrijden staan er dinsdag 17 november op het programma?</strong><br>Ratajski – Sykes, Clemens – Rodriguez, Dobey – Schindler, Wade – Evans, Van Veen – Brooks, Humphries – Cullen, Van Gerwen – De Graaf en Aspinall – Sedláček: de laatste groepsronde van de groepen I tot en met P.</p>
<p><strong>Gaat de nummer twee van de groep ook door?</strong><br>Nee. Op de Grand Slam of Darts gaat alleen de groepswinnaar door naar de laatste 16. Daarom is bijna elke partij van dinsdagavond een beslissingsduel.</p>
<p><strong>Wat moet Michael van Gerwen doen om door te gaan?</strong><br>Winnen is genoeg. Verliest hij, dan moet Jeffrey de Graaf dat met minstens twee legs verschil doen; bij 5-4 komen Van Gerwen, De Graaf en Henry Coates alle drie op twee punten, saldo nul én negen gewonnen legs uit, en beslist pas het aantal legs dat ze tegen de pijl in wonnen.</p>
<p><strong>Is Luke Humphries al zeker van de laatste 16?</strong><br>Nee. Volgens onze berekening moet hij winnen of hoogstens met 4-5 verliezen. Verliest hij met twee legs verschil of meer, dan gaat Paolo Nebrida door op legsaldo — en bij 0-5 gaat Joe Cullen zelf door.</p>
<p><strong>Welke Nederlanders spelen er dinsdag?</strong><br>Gian van Veen (tegen Bradley Brooks) en Michael van Gerwen (tegen Jeffrey de Graaf, die voor Zweden uitkomt).</p>
<p><strong>Hoeveel legs gaat een groepswedstrijd?</strong><br>Best of 9: de eerste speler die vijf legs wint, wint de partij. Vanaf de laatste 16 wordt het best of 19, en vanaf de kwartfinales best of 31.</p>
<p><strong>Wie gooide tot nu toe het hoogste gemiddelde van de dinsdagavondspelers?</strong><br>Nathan Aspinall, met 111,68 in zijn 5-1 tegen Maik Kuivenhoven — zijn hoogste televisiegemiddelde ooit. Gian van Veen volgt met 110,51. Van het hele toernooi staat Rob Cross bovenaan met 114,32.</p>
<p><strong>Is er al een negendarter gegooid?</strong><br>Nee. Aspinall kwam er het dichtst bij: hij gooide in zijn slotleg zeven perfecte darts. De hoogste uitgooi tot nu toe is 170, van Joe Hunt.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

WEDTIPS = {"wedstrijd-1": "Aspinall vs Sedlacek", "wedtip-1-2": "Nathan Aspinall -1.5 legs", "quotering-wedtip-1": "1.78",
           "wedstrijd-2": "Van Veen vs Brooks", "wedtip-2-2": "Gian van Veen -1.5 legs", "quotering-wedtip-2": "1.83",
           "wedstrijd-3": "Wade vs Evans", "wedtip-3-2": "James Wade -1.5 legs", "quotering-wedtip-3": "1.54"}

if __name__ == "__main__":
    import re
    if "--velden" in sys.argv:
        import lk_webflow as WF
        it = WF._req("GET", f"{WF.WF_API}/collections/{WF.NIEUWS_COLLECTION}/items?slug={SLUG}")["items"][0]
        fd = {"bookmaker-wedtips": BOOKMAKER_711, "datum-tijd-van-wedstrijd": DATUM, **WEDTIPS}
        for pad in ("", "/live"):
            WF._req("PATCH", f"{WF.WF_API}/collections/{WF.NIEUWS_COLLECTION}/items/{it['id']}{pad}", {"fieldData": fd})
        print("velden gezet:", it["id"]); sys.exit()
    alles = content + content2 + content3
    w = len(re.sub(r"<[^>]+>", " ", alles).split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", w, "woorden |", len(TIPS), "tips")
    assert len(TITEL) <= 60 and 120 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert 1800 <= w <= 4400, w
    p = 1
    for o in ODDS: p *= o
    assert f"{p:.2f}".replace(".", ",") == COMBI, p
    assert f"{10 * p:.2f}" == "88.29", 10 * p      # afgerond ~88,30 in de tekst
    assert [t[4] for t in TIPS] == ["1,76", "1,78", "1,83", "1,54"] == [r[2] for r in OG_RIJEN]
    assert len(PROGRAMMA) == len(NODIG) == 8 and len(GEMIDDELDEN) == 16 and len(LAATSTE16) == 4
    assert sorted(g for g, *_ in NODIG) == list("IJKLMNOP")
    assert sum(1 for *_, t in NODIG if "Zuivere knock-out" in t) == 4
    assert 5 - 3 >= 2 and 5 - 4 < 2 and 5 - 2 >= 3 and 5 - 3 < 3   # rekenvoorbeelden leg handicap
    assert [float(g.replace(",", ".")) for _, _, g, _ in GEMIDDELDEN] == sorted(
        (float(g.replace(",", ".")) for _, _, g, _ in GEMIDDELDEN), reverse=True)
    assert GEMIDDELDEN[0][0] == "Nathan Aspinall" and GEMIDDELDEN[1][0] == "Gian van Veen"
    assert "eigen berekening" in alles.lower() and "doorgerekend" in alles.lower()
    assert "<h2" not in alles and "<h4" not in alles and "/go/" not in alles
    for verboden in ("betcity", "footymetrics", "opstellingvandaag", "waaroptv", "squawka"):
        assert verboden not in alles.lower(), verboden
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    print("dry run ok")
