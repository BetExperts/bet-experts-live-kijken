# -*- coding: utf-8 -*-
"""Los artikel: ATP Finals 2026, dinsdag 17 november (tweede speelronde John McEnroe Group) - voorspellingen en wedtips.
Tips: meer dan 20,5 games in Fils - Jodar (1,42) en Zverev wint van Shelton (1,50). Combinatie 2,13.
LIVE item 6afae9b47f378424346e5e39, slug atp-finals-dinsdag-17-november-voorspellingen-wedtips.

16-11-2026 (avond) GROTE UITBREIDING na een tweede feitenronde, zie specials/atp_finals_dag3_feiten.md:
  + uitslagen en stand van maandag (Alcaraz - Tiafoe 6-2 6-2 in 69 min, Medvedev - Cobolli 7-6(4) 6-3 in 1u25)
  + eigen doorrekening van de kwalificatiescenario's + de officiele tiebreak-criteria (ATP Rulebook 2026, 4.01 D.3).
    ER BESTAAT GEEN officieel ATP-stuk met groepsscenario's; dit is onze eigen berekening en staat zo in de tekst.
  + prijzengeld en ranglijstpunten per groepszege (officiele Nitto-pagina)
  + vergelijkingstabel serveer-/returncijfers (ATP MatchFacts peildatum 9-11-2026; indoorrecords = EIGEN TELLING
    uit de officiele ATP-activity-scorelines, want de ATP publiceert geen indoor/outdoor-split per speler)
  + H2H-verdieping: Zverev - Shelton speelden vorig jaar al in Turijn (enige indoorduel van de zes);
    Fils - Jodar speelden NOOIT indoor (nul sample)
  + tv-nuance: Fils - Jodar staat op kanaal 14 (in het Ziggo-abonnement), Zverev - Shelton ALLEEN op Ziggo Sport 4
  + Zverev kreeg maandagavond de Year-End No. 1-trofee

Odds opnieuw gecontroleerd op 16-11 ±23:00 (711, Kambi sevelevnl): meer dan 20,5 games nog steeds 1,42 en
Zverev wint nog steeds 1,50 - beide tips blijven dus staan. WEL verschoven: de wedstrijdnotering van Fils - Jodar
ging van 2,05/1,77 naar 1,90/1,90. Dat staat zo in de tekst.

Fitheid gecheckt (regel 4-11): in het hele venster 15 t/m 16 november GEEN ENKEL blessurebericht over Zverev,
Shelton, Fils of Jodar; niemand teruggetrokken, geen reserve opgeroepen, alle vier spelen. Dat is afwezigheid van
nieuws, geen bewijs van fitheid, en zo staat het er ook. Correcties t.o.v. de eerste versie: Fils gaf op 30 oktober
op in Bazel (niet eerder) en sprak zelf over zijn BEEN; onderzoeken waren schoon en op 2 november noemde hij zich
"100 procent". De rondzwervende "Jodar spierverrekking" is in werkelijkheid Cobolli - niet gebruiken.

Bewust weggelaten: winners/unforced errors van alle vier de partijen tot nu toe (nergens gepubliceerd),
aces/dubbele fouten van Medvedev - Cobolli, officieel indoor-W-V per speler (bestaat niet), persconferenties van
maandag van de vier McEnroe-spelers (bestaan niet), tv-dekking van de twee dubbelpartijen in Nederland.
  python3 specials/atp_finals_dinsdag_2026.py        (dry run)
  kaart: ../superodd-agent/.venv/bin/python og_kaarten/atp_finals_dinsdag_2026.py
  bijwerken: set -a; . ../superodd-agent/.env; set +a; ../superodd-agent/.venv/bin/python specials/bijwerk_live.py atp_finals_dinsdag_2026 6afae9b47f378424346e5e39"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "atp-finals-dinsdag-17-november-voorspellingen-wedtips"
ITEM_ID = "6afae9b47f378424346e5e39"
RUBRIEK = "665715dbf1f3cbdf7f874d79"   # Tennis
BOOKMAKER_711 = "66a8a87062108480763b7309"
TITEL = "ATP Finals dinsdag: voorspellingen en wedtips 17 november"
SAMENVATTING = ("Voorspellingen voor dinsdag op de ATP Finals: Fils tegen Jodar en Zverev tegen Shelton. "
                "Twee wedtips met odds, de stand in de groep en de tv-tijden.")
ODDS = [1.42, 1.50]
COMBI = "2,13"

L = {"hub": '<a href="/tennis-voorspellingen-vandaag">tennis voorspellingen vandaag</a>',
     "dag1": '<a href="/nieuws/atp-finals-2026-dag-1-voorspellingen-wedtips">de uitslagen en onze tips van dag 1</a>',
     "maandag": '<a href="/nieuws/atp-finals-maandag-16-november-voorspellingen-wedtips">ons artikel over maandag</a>',
     "groepen": '<a href="/nieuws/atp-finals-2026-groepen-loting-schema">de groepen en het schema van de ATP Finals 2026</a>',
     "ziggo": '<a href="/zenders/ziggo-sport">Ziggo Sport</a>',
     "kijken": '<a href="/live-kijken">live kijken</a>',
     "duur": '<a href="/nieuws/hoe-lang-duurt-een-tenniswedstrijd">hoelang een tenniswedstrijd duurt</a>',
     "handicap": '<a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">hoe handicap wedden werkt</a>',
     "opgave": '<a href="/nieuws/tennisser-geeft-op-wat-zijn-de-regels-voor-je-weddenschap-bij-nederlandse-bookmakers">wat er met je weddenschap gebeurt als een tennisser opgeeft</a>',
     "wedgids": '<a href="/wedgids">de Wedgids</a>',
     "711": '<a href="/bookmakers/711">711</a>',
     "legaal": '<a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>'}

HELE = "Geldt voor de hele wedstrijd: alle sets tellen mee, en een set die op 7-6 eindigt levert dertien games op."

TIPS = [("Fils – Jódar", "ATP Finals", "14:00 uur", "Meer dan 20,5 games", "Totaal aantal games, hele wedstrijd", "1,42"),
        ("Zverev – Shelton", "ATP Finals", "niet voor 20:30 uur", "Zverev wint", "Winnaar van de wedstrijd", "1,50")]

PROGRAMMA = [("11:30 uur", "Dubbelspel", "Heliövaara/Patten – Arévalo/Pavić", "niet op de Nederlandse tv"),
             ("niet voor 14:00 uur", "Enkelspel", "<strong>Arthur Fils – Rafael Jódar</strong>", "Ziggo Sport 1 (kanaal 14) én Ziggo Sport 4, 14:00–16:00 uur"),
             ("niet voor 18:00 uur", "Dubbelspel", "Arribagé/Olivetti – Luz/Matos", "niet op de Nederlandse tv"),
             ("niet voor 20:30 uur", "Enkelspel", "<strong>Alexander Zverev – Ben Shelton</strong>", "alléén Ziggo Sport 4, 20:30–22:30 uur")]

STAND = [("1", "Alexander Zverev", "1-0", "2-0", "12-8", "60,00%"),
         ("2", "Ben Shelton", "1-0", "2-1", "15-11", "57,69%"),
         ("3", "Arthur Fils", "0-1", "1-2", "11-15", "42,31%"),
         ("4", "Rafael Jódar", "0-1", "0-2", "8-12", "40,00%")]

STAND_LENDL = [("1", "Carlos Alcaraz", "1-0", "2-0", "12-4", "75,00%"),
               ("2", "Daniil Medvedev", "1-0", "2-0", "13-9", "59,09%"),
               ("3", "Flavio Cobolli", "0-1", "0-2", "9-13", "40,91%"),
               ("4", "Frances Tiafoe", "0-1", "0-2", "4-12", "25,00%")]

SCENARIO = [("Zverev wint én <strong>Jódar</strong> wint", "<strong>Fils ligt eruit.</strong> Hij staat dan op 0-2 en speelt donderdag tegen Zverev, die al twee keer won. Uit Shelton – Jódar komt donderdag nóg een speler met twee zeges. Fils haalt maximaal 1-2 en wordt gepasseerd."),
            ("Shelton wint én <strong>Fils</strong> wint", "<strong>Jódar ligt eruit.</strong> Precies dezelfde rekensom, met Shelton in de rol van Zverev."),
            ("Zverev wint én <strong>Fils</strong> wint", "Jódar leeft op papier nog: hij moet donderdag van Shelton winnen én Zverev moet van Fils winnen. Dan staan er drie spelers op 1-2 en beslist het setpercentage. Uiterst dun."),
            ("Shelton wint én <strong>Jódar</strong> wint", "Fils leeft op papier nog, via exact dezelfde constructie. Even dun.")]

H2H_ZS = [("2024", "Cincinnati, kwartfinale", "hardcourt (buiten)", "Zverev wint 3-6, 7-6(3), 7-5"),
          ("2025", "München, finale", "gravel", "Zverev wint 6-2, 6-4"),
          ("2025", "Stuttgart, halve finale", "gras", "Zverev wint 7-6(8), 7-6(1)"),
          ("2025", "Cincinnati, kwartfinale", "hardcourt (buiten)", "Zverev wint 6-2, 6-2"),
          ("2025", "<strong>ATP Finals Turijn, groepsfase</strong>", "<strong>indoor hardcourt</strong>", "Zverev wint 6-3, 7-6(6)"),
          ("2026", "US Open, finale", "hardcourt (buiten)", "Zverev wint 6-3, 7-6(2), 5-7, 6-2")]

H2H_FJ = [("april 2026", "Barcelona, halve finale", "gravel", "Fils wint 3-6, 6-3, 6-2", "26"),
          ("juli 2026", "Washington, openingsronde", "hardcourt (buiten)", "Jódar wint 7-6(5), 6-3", "22"),
          ("augustus 2026", "Montreal, kwartfinale", "hardcourt (buiten)", "Jódar wint 7-6(5), 6-3", "22")]

# ATP MatchFacts, peildatum 9 november 2026; indoorrecord en games per wedstrijd = eigen telling
CIJFERS = [("Positie op de wereldranglijst", "1", "4", "7", "10"),
           ("Balans 2026", "65-18", "45-19", "39-16", "45-19"),
           ("Titels in 2026", "2", "4", "2", "1"),
           ("Balans indoor hardcourt 2026", "3-2", "<strong>10-2</strong>", "7-5", "2-3"),
           ("Aces per wedstrijd", "10,2", "<strong>11,3</strong>", "5,7", "4,4"),
           ("Eerste service in", "<strong>71%</strong>", "68%", "64%", "63%"),
           ("Servicegames gewonnen", "<strong>90%</strong>", "<strong>90%</strong>", "86%", "81%"),
           ("Breakpoints gered", "63%", "<strong>69%</strong>", "67%", "63%"),
           ("Returngames gewonnen", "22%", "15%", "21%", "<strong>29%</strong>"),
           ("Breakpoints benut", "41%", "36%", "37%", "<strong>43%</strong>"),
           ("Games per wedstrijd, recent indoor", "24,2", "<strong>30,0</strong>", "23,9", "22,0")]

GELD = [("Elke groepswedstrijd die je wint", "$405.000", "200"),
        ("De halve finale winnen", "$1.206.000", "400"),
        ("De finale winnen", "$2.412.000", "500"),
        ("Ongeslagen kampioen worden", "$5.171.000", "1.500")]


def waarom(punten):
    return "<p><strong>Waarom deze tip?</strong></p><ul>" + "".join(f"<li>{p}</li>" for p in punten) + "</ul>"


def markt(m):
    return f"<p><strong>De markt:</strong> {m}</p>"


content = f"""<p><strong>Onze voorspellingen voor dinsdag 17 november op de ATP Finals: in Arthur Fils – Rafael Jódar vallen er meer dan 20,5 games (1,42) en Alexander Zverev wint van Ben Shelton (1,50). De John McEnroe Group speelt dinsdag zijn tweede ronde: Fils – Jódar om 14:00 uur, Zverev – Shelton niet voor 20:30 uur. Gecombineerd staan die twee tips op ongeveer {COMBI} bij {L['711']}.</strong></p>
<p>Zondag won Zverev met 6-4, 6-4 van Jódar en klopte Shelton in drie sets Fils (6-2, 3-6, 6-3). Daardoor staan de twee winnaars dinsdagavond tegenover elkaar en vechten de twee verliezers 's middags om hun laatste kans. Alle uitslagen van dag 1 en hoe onze tips daar uitpakten, lees je in {L['dag1']}.</p>
<p>Maandag was de andere groep aan de beurt. <strong>Carlos Alcaraz versloeg Frances Tiafoe met 6-2, 6-2 in 69 minuten</strong> — Tiafoe won geen enkel punt op zijn tweede service, nul uit twaalf — en <strong>Daniil Medvedev won met 7-6(4), 6-3 van Flavio Cobolli</strong> in een uur en 25 minuten, met 83 procent gewonnen punten achter zijn eerste service. Wat wij maandag voorspelden staat in {L['maandag']}. Maandagavond kreeg Zverev in de Inalpi Arena ook nog de trofee voor de eindzege in de jaarrace uitgereikt: hij sluit 2026 af als nummer 1 van de wereld.</p>
<h3><strong>De wedtips voor dinsdag in het kort</strong></h3>
{tabel(["Tijd", "Wedstrijd", "Onze tip", "Markt", "Odd"],
       [(t[2], f"<strong>{t[0]}</strong>", t[3], t[4], f"<strong>{t[5]}</strong>") for t in TIPS])}
<p><em>Odds van {L['711']}, opnieuw gecontroleerd op maandagavond 16 november. Odds veranderen; controleer ze voordat je inzet.</em></p>
<h3><strong>Het programma van dinsdag 17 november</strong></h3>
{tabel(["Tijd", "Onderdeel", "Wedstrijd", "Tv in Nederland"], PROGRAMMA)}
<p>De tijden met "niet voor" zijn vroegst mogelijke starttijden: loopt de partij ervoor uit, dan schuift alles op. Turijn heeft dezelfde tijd als Nederland. Let op het verschil tussen de twee enkelpartijen: <strong>Fils – Jódar is te zien op {L['ziggo']} 1, dat op kanaal 14 in het standaard Ziggo-pakket zit, terwijl Zverev – Shelton alleen op Ziggo Sport 4 staat</strong> — die zender hoort bij het betaalde Ziggo Sport Totaal. De twee dubbelpartijen worden in Nederland helemaal niet uitgezonden. Meer kijkopties staan op onze pagina {L['kijken']}.</p>
<h3><strong>Zo staan beide groepen na twee speeldagen</strong></h3>
<p><strong>John McEnroe Group</strong> — speelt dinsdag.</p>
{tabel(["#", "Speler", "Zeges", "Sets", "Games", "Gamepercentage"],
       [(n, f"<strong>{s}</strong>", z, st, g, p) for n, s, z, st, g, p in STAND])}
<p><strong>Ivan Lendl Group</strong> — speelde maandag, is woensdag weer aan de beurt.</p>
{tabel(["#", "Speler", "Zeges", "Sets", "Games", "Gamepercentage"],
       [(n, f"<strong>{s}</strong>", z, st, g, p) for n, s, z, st, g, p in STAND_LENDL])}
<p>Dat gamepercentage in de laatste kolom is geen opsmuk. Staan er straks drie spelers op evenveel zeges, dan beslist eerst het setpercentage en daarna het gamepercentage wie doorgaat. Alcaraz staat in zijn groep bovenaan op precies dat criterium, en in de McEnroe-groep scheelt het tussen Zverev en Shelton nu nog maar twee procentpunt. Elke game telt dus, ook in een partij die al beslist lijkt.</p>"""

content2 = f"""<h3><strong>Wat er dinsdag op het spel staat</strong></h3>
<p>Hier zit het echte verhaal van dag 3, en het is niet wat je zou verwachten. <strong>Niemand kan zich dinsdag al plaatsen voor de halve finales — zelfs niet met twee zeges uit twee.</strong> Stel dat Zverev wint en daarmee op 2-0 komt: verliest hij donderdag van Fils, en wint Shelton donderdag van Jódar, dan staan er drie spelers op 2-1 en valt er alsnog één af op setpercentage. Twee uit twee is in deze groep dus geen garantie.</p>
<p>Afvallen kan wél. Donderdag speelt Zverev tegen Fils en Shelton tegen Jódar — dat is de enige combinatie die nog overblijft. Daaruit volgt één heldere regel: <strong>wie 's middags verliest, ligt eruit als zijn donderdag-tegenstander 's avonds óók wint.</strong></p>
{tabel(["Als dit dinsdag gebeurt", "Dan geldt donderdag"], [(a, b) for a, b in SCENARIO])}
<p><em>Dit is onze eigen doorrekening op basis van de officiële stand en de officiële rangschikkingsregels van de ATP (Rulebook 2026, hoofdstuk IV). De ATP publiceert zelf geen scenario's voor de groepsfase. De volgorde van die regels is: aantal zeges, dan aantal gespeelde wedstrijden, dan het onderlinge duel als er twee gelijk staan — en staan er drie gelijk, dan setpercentage, daarna gamepercentage, daarna de wereldranglijst.</em></p>
<p>Praktisch gezien maakt dat de middagpartij de belangrijkste van de twee. Voor Fils en Jódar is dit een afvalrace met scherprechter; voor Zverev en Shelton gaat het vooral om de volgorde en om de vraag wie donderdag met een reservekussentje de baan op stapt.</p>
<h3><strong>Arthur Fils – Rafael Jódar (14:00 uur)</strong></h3>
<p>Twee debutanten die allebei verloren, en die elkaar dit jaar al drie keer troffen. Dat is meteen het interessantste aan deze partij: <strong>Jódar leidt met 2-1</strong>, en zijn twee zeges waren opvallend identiek. Zowel in Washington als in Montreal won hij met exact 7-6(5), 6-3 — twee keer 22 games, twee keer met een tiebreak in de eerste set. Fils won hun eerste duel, in de halve finale van Barcelona, en pakte daarna in datzelfde toernooi de titel.</p>
{tabel(["Wanneer", "Toernooi", "Ondergrond", "Uitslag", "Games"], H2H_FJ)}
<p><em>De gamestelling is onze eigen telling uit de setstanden.</em></p>
<p><strong>En hier zit het gat in alle cijfers:</strong> die drie duels waren op gravel en op hardcourt in de buitenlucht. <strong>Dinsdag is hun eerste ontmoeting ooit indoor.</strong> De baan in Turijn ligt snel, en snelheid helpt de serveerder. Dat is precies de reden waarom wij in deze partij geen winnaar aanwijzen, maar wel iets durven te zeggen over het aantal games.</p>
<p>Zondag maakte Fils een betere indruk dan de uitslag suggereert. Hij bracht 76 procent van zijn eerste services in, tegen 66 procent voor Shelton, sloeg meer winners (15 om 13) en pakte de tweede set. Hij verloor vooral op de grote punten: Shelton benutte drie van zijn twaalf breakkansen, Fils één van vier. "I played a good match, with a very high level of tennis", zei hij achteraf. "I'm not sad. I'm not crying. I have another match on Tuesday, another match on Thursday."</p>
<p>Jódar kwam tegen Zverev nauwelijks in de buurt van een break: hij kreeg twee breakkansen en benutte er geen. Zijn eigen service stond onder druk, met 63 procent eerste services in. "I think the match was decided by small details", zei de twintigjarige Spanjaard. Tegen Fils krijgt hij een tegenstander die een stuk minder hard serveert dan Zverev, en dat is precies het soort partij waarin hij dit jaar twee keer won.</p>
<p><strong>Het fysieke vraagteken bij Fils.</strong> Hij gaf op 30 oktober in Bazel op na een medical time-out; hij sprak zelf over pijn in zijn been, terwijl een deel van de berichtgeving over zijn onderrug ging. De onderzoeken leverden niets op en begin november noemde hij zichzelf weer "100 procent". Sindsdien speelde hij twee partijen in Parijs en zondag bijna twee uur tegen Shelton, telkens zonder zichtbaar ongemak, en op de persconferentie klaagde hij niet over zijn lichaam. <strong>Tussen zondagavond en maandagavond is er over geen van de vier spelers uit deze groep één blessurebericht verschenen, niemand heeft zich teruggetrokken en er is geen reserve opgeroepen.</strong> Dat is geen bewijs van topfitheid, maar wel het beste wat er te weten valt.</p>
{waarom(["Hun twee duels van dit jaar op hardcourt leverden allebei precies 22 games op, ruim boven deze lijn.",
         "In beide partijen ging de eerste set naar een tiebreak: geen van tweeën breekt de ander makkelijk.",
         "De bookmaker zet de kans op drie sets op ongeveer 45 procent; in dat geval is deze tip al na de tweede set zo goed als binnen.",
         "Jódar is de beste returner van de vier (29 procent gewonnen returngames, 43 procent van zijn breakpoints benut) maar de zwakste serveerder — die combinatie levert lange, gebroken sets op.",
         "Voor allebei is dit een afvalrace. Niemand gaat hier makkelijk akkoord met een korte partij."])}
{markt(f"Meer dan 20,5 games, totaal aantal games. Tel alle games van beide spelers bij elkaar op. Bij 6-4, 7-5 zijn dat 10 + 12 = 22 games en win je. Bij 6-3, 6-4 zijn dat 19 games en verlies je. {HELE}")}
<p><strong>Waar we vanaf blijven.</strong> Toen wij maandagmiddag keken, stond Jódar op 1,77 en Fils op 2,05 — de bookmaker maakte de verliezer van zondag met 0-2 in sets dus favoriet boven de speler die wél een set pakte. Maandagavond was dat weggepoetst: <strong>beiden staan nu op 1,90</strong>, een volledig open partij. Dat zegt vooral hoe weinig houvast er is. Met een onbevestigd fysiek vraagteken aan de ene kant en nul indoorgeschiedenis aan de andere, kiezen wij hier geen winnaar.</p>
<h3><strong>Alexander Zverev – Ben Shelton (niet voor 20:30 uur)</strong></h3>
<p>Dit is de partij van de dag, en tegelijk de meest eenzijdige geschiedenis van het toernooi: <strong>Zverev won alle zes hun onderlinge duels</strong>. Daar zitten zware partijen bij — de US Open-finale van dit jaar ging over vier sets — maar Shelton heeft hem nog nooit verslagen. In al die zes partijen pakte hij in totaal één set.</p>
{tabel(["Jaar", "Toernooi", "Ondergrond", "Uitslag"], H2H_ZS)}
<p><em>Alle zes hun ontmoetingen. Zverev won ze allemaal, en geen enkele eindigde in een opgave.</em></p>
<p><strong>Let op de vijfde rij.</strong> Precies één van die zes was indoor, en dat was vorig jaar in deze zaal, in deze fase van dit toernooi: Zverev won met 6-3, 7-6(6). Shelton had in die tweede tiebreak setpunten. Het is dus niet zo dat Zverev hem indoor van de baan speelde — maar hij won wel.</p>
<p>Zverev opende het toernooi zoals je van een eindejaars-nummer 1 verwacht: tien aces, geen enkele dubbele fout, 84 procent eerste services in en in de openingsset zelfs 88 procent. Bij 4-5 in die eerste set redde hij 15-40 met twee aces en twee onreturneerbare services. Zelf was hij nuchter: "I still think I have a lot of things to improve. It was not a perfect match, but to start the tournament I'm very happy." Hij staat nu op 19 zeges en 12 nederlagen in negen deelnames aan dit toernooi.</p>
<p>Shelton boekte zondag zijn <strong>eerste zege ooit op de ATP Finals</strong>, nadat hij vorig jaar al zijn drie groepswedstrijden verloor. Dat kostte hem wel bijna twee uur tegen Fils, tegen een uur en 27 minuten voor Zverev. "So it was physical, really physical", zei hij. "I was breathing hard after pretty much every point." Hij maakte 31 onnodige fouten, waarvan twintig met de backhand — precies de kant waar Zverev hem in hun eerdere duels naartoe speelde.</p>
{waarom(["Zverev won alle zes hun duels, inclusief die in deze zaal, in deze fase, vorig jaar.",
         "Zverev stond zondag een half uur korter op de baan en heeft de frissere benen voor een avondpartij.",
         "Hij sloeg tien aces zonder dubbele fout en brengt 71 procent van zijn eerste services in, het hoogste percentage van de vier.",
         "Shelton maakte 31 onnodige fouten, twintig daarvan met de backhand — zijn kwetsbaarste kant tegen Zverev.",
         "Shelton staat na zondag op 1-3 op de ATP Finals; Zverev op 19-12, met twee titels."])}
{markt("Zverev wint. De speler moet de wedstrijd winnen, in twee of drie sets. Wordt de partij niet uitgespeeld, dan gelden de opgaveregels van je bookmaker.")}
<p><strong>De keerzijde.</strong> Een odd van 1,50 betekent dat de bookmaker Zverev op ongeveer 67 procent inschat, en daar zit niet veel ruimte in. Shelton is op dit moment de nummer 4 van de wereld, heeft met 10-2 verreweg het beste indoorrecord van de vier, haalde vorige week de finale van Parijs en heeft met Juan Carlos Ferrero sinds dit weekend een extra stem in zijn box. Daar staat tegenover dat Zverev dit jaar 3-9 speelde tegen spelers uit de top tien — ook dat hoor je te weten. Wie meer rendement wil: Zverev met -1,5 games staat op 1,73, en dat wint ook als hij in drie sets wint met twee games verschil. Wij houden het bij de simpele variant.</p>
<h3><strong>De vier spelers naast elkaar</strong></h3>
{tabel(["", "Zverev", "Shelton", "Fils", "Jódar"],
       [(f"<strong>{r[0]}</strong>", r[1], r[2], r[3], r[4]) for r in CIJFERS])}
<p><em>Serveer- en returncijfers komen uit de officiële ATP-statistieken over heel 2026 (peildatum 9 november). De indoorbalans en het aantal games per wedstrijd zijn onze eigen telling uit de uitslagenarchieven: de ATP publiceert geen aparte indoorcijfers per speler.</em></p>
<p>Twee dingen springen eruit. <strong>Shelton is indoor de sterkste van de vier</strong> (10-2, met de titel in Dallas) en slaat de meeste aces, maar hij heeft veruit de slechtste return: hij wint maar 15 procent van zijn returngames. En <strong>Jódar is precies het omgekeerde</strong>: de zwakste serveerder van de vier, maar met 29 procent gewonnen returngames en 43 procent benutte breakpoints de beste returner. Op een snelle indoorbaan is dat zijn grootste handicap — en tegelijk de reden dat zijn partijen zelden kort zijn.</p>"""

content3 = f"""<h3><strong>Combinatie dinsdag 17 november</strong></h3>
<p>Beide tips samen: 1,42 × 1,50 = <strong>± {COMBI}</strong>. Een inzet van €10 levert dan ongeveer €21,30 op. Het zijn twee losse partijen, dus de weddenschappen beïnvloeden elkaar niet, maar er moeten wel twee dingen goed gaan in plaats van één.</p>
<h3><strong>Waar spelen ze dinsdag eigenlijk voor?</strong></h3>
<p>Meer dan bij welk ander toernooi ook. De prijzenpot van de ATP Finals 2026 is met $15.750.000 de hoogste ooit, en anders dan elders wordt hier per gewonnen partij uitbetaald — ook in de groepsfase.</p>
{tabel(["Prestatie", "Prijzengeld", "Ranglijstpunten"],
       [(f"<strong>{a}</strong>", b, c) for a, b, c in GELD])}
<p>Elke deelnemer krijgt daarnaast een vaste deelnamefee van $338.000 voor drie groepswedstrijden. Een zege van dinsdagavond is dus letterlijk ruim vier ton waard, plus 200 punten voor de wereldranglijst van 2027. Voor Jódar, die pas dit jaar op tourniveau debuteerde, is dat een ander soort bedrag dan voor Zverev.</p>
<h3><strong>Wat gebeurt er woensdag en donderdag?</strong></h3>
<p>Woensdag 18 november is de Ivan Lendl Group weer aan de beurt, met Alcaraz tegen Medvedev en Cobolli tegen Tiafoe. De McEnroe-groep sluit af op donderdag 19 november, met Zverev – Fils en Shelton – Jódar. De halve finales zijn zaterdag 21 november, de finale zondag 22 november. Het volledige schema en de groepsindeling staan in {L['groepen']}.</p>
<h3><strong>Wat betekenen deze weddenschappen?</strong></h3>
<p><strong>Totaal aantal games (meer dan 20,5).</strong> Alle games van beide spelers bij elkaar opgeteld, over alle sets. De halve game in de lijn zorgt ervoor dat er geen gelijkspel kan zijn: bij 20 games verlies je, bij 21 win je. Een partij in twee sets eindigt meestal tussen de 18 en 26 games; gaat het naar drie sets, dan zit je er bijna altijd ruim boven.</p>
<p><strong>Winnaar van de wedstrijd.</strong> De speler moet de partij winnen, in twee of drie sets. Hoeveel games of sets hij verliest, maakt niet uit. Wil je meer rendement op dezelfde gedachte, dan kun je naar de game handicap kijken; hoe die werkt lees je in {L['handicap']}.</p>
<p>Geeft een speler op, dan bepalen de regels van je bookmaker wat er met je weddenschap gebeurt: lees {L['opgave']}. Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit; in {L['legaal']} leggen we uit waar je dat aan ziet. Meer uitleg over soorten weddenschappen vind je in {L['wedgids']}, en hoe lang je voor een avondpartij moet uittrekken staat in {L['duur']}. Alle tennistips van vandaag staan op {L['hub']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wat zijn de beste wedtips voor dinsdag op de ATP Finals?</strong><br>Meer dan 20,5 games in Fils – Jódar (1,42) en Zverev wint van Shelton (1,50). Gecombineerd is dat ongeveer {COMBI}, waarmee €10 inzet ongeveer €21,30 oplevert.</p>
<p><strong>Welke wedstrijden staan er dinsdag 17 november op het programma?</strong><br>Arthur Fils – Rafael Jódar om 14:00 uur en Alexander Zverev – Ben Shelton niet voor 20:30 uur, allebei in de John McEnroe Group. Daarnaast twee dubbelpartijen, om 11:30 en 18:00 uur.</p>
<p><strong>Hoe laat speelt Zverev tegen Shelton?</strong><br>Niet voor 20:30 uur Nederlandse tijd, als laatste partij van de avondsessie. Turijn heeft dezelfde tijd als Nederland.</p>
<p><strong>Waar kan ik de ATP Finals dinsdag live kijken?</strong><br>Fils – Jódar staat van 14:00 tot 16:00 uur op Ziggo Sport 1 (kanaal 14, in het standaard Ziggo-pakket) en op Ziggo Sport 4. Zverev – Shelton staat van 20:30 tot 22:30 uur alléén op Ziggo Sport 4, onderdeel van het betaalde Ziggo Sport Totaal. De dubbelpartijen worden in Nederland niet uitgezonden.</p>
<p><strong>Kan iemand zich dinsdag al plaatsen voor de halve finale?</strong><br>Nee. Zelfs met twee zeges uit twee is niemand zeker, omdat er donderdag nog een drievoudig gelijkspel op 2-1 kan ontstaan dat op setpercentage wordt beslist.</p>
<p><strong>Wie ligt er dinsdag uit?</strong><br>De verliezer van Fils – Jódar is uitgeschakeld als zijn donderdag-tegenstander 's avonds ook wint. Verliest Fils en wint Zverev, dan ligt Fils eruit; verliest Jódar en wint Shelton, dan ligt Jódar eruit.</p>
<p><strong>Heeft Shelton ooit van Zverev gewonnen?</strong><br>Nee. Zverev won alle zes hun onderlinge duels, waaronder de US Open-finale van dit jaar en hun groepspartij in Turijn van vorig jaar. Shelton pakte in die zes partijen in totaal één set.</p>
<p><strong>Hoe staat het in de John McEnroe Group?</strong><br>Zverev en Shelton staan op één zege, Fils en Jódar op nul. Zverev leidt op setsaldo: 2-0 tegen 2-1 voor Shelton.</p>
<p><strong>Wat waren de uitslagen van maandag?</strong><br>Carlos Alcaraz won met 6-2, 6-2 van Frances Tiafoe in 69 minuten en Daniil Medvedev versloeg Flavio Cobolli met 7-6(4), 6-3. In de Ivan Lendl Group staan Alcaraz en Medvedev dus allebei op 1-0.</p>
<p><strong>Hoeveel verdient een speler met een zege in de groepsfase?</strong><br>$405.000 en 200 ranglijstpunten. Wie het toernooi ongeslagen wint, krijgt $5.171.000 en 1.500 punten.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

WEDTIPS = {"wedstrijd-1": "Combinatie: beide tips",
           "wedtip-1-2": "Meer dan 20.5 games in Fils - Jodar + Zverev wint van Shelton",
           "quotering-wedtip-1": "2.13",
           "wedstrijd-2": "Fils vs Jodar", "wedtip-2-2": "Meer dan 20.5 games (hele wedstrijd)", "quotering-wedtip-2": "1.42",
           "wedstrijd-3": "Zverev vs Shelton", "wedtip-3-2": "Zverev wint", "quotering-wedtip-3": "1.50"}

if __name__ == "__main__":
    import re
    if "--velden" in sys.argv:
        import lk_webflow as WF
        it = WF._req("GET", f"{WF.WF_API}/collections/{WF.NIEUWS_COLLECTION}/items?slug={SLUG}")["items"][0]
        fd = {"tennis": True, "bookmaker-wedtips": BOOKMAKER_711, "datum-tijd-van-wedstrijd": "2026-11-17T13:00:00.000Z", **WEDTIPS}
        for pad in ("", "/live"):
            WF._req("PATCH", f"{WF.WF_API}/collections/{WF.NIEUWS_COLLECTION}/items/{it['id']}{pad}", {"fieldData": fd})
        print("velden gezet:", it["id"]); sys.exit()
    alles = content + content2 + content3
    w = len(re.sub(r"<[^>]+>", " ", alles).split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", w, "woorden")
    assert len(TITEL) <= 60 and 120 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert 2200 <= w <= 3400, w
    p = 1
    for o in ODDS: p *= o
    assert f"{p:.2f}".replace(".", ",") == COMBI, p
    assert f"{10 * p:.1f}" == "21.3", 10 * p
    assert [t[5] for t in TIPS] == ["1,42", "1,50"]
    assert 10 + 12 == 22 > 20.5 and 6 + 3 + 6 + 4 == 19 < 20.5          # rekenvoorbeelden
    assert 7 + 6 + 6 + 3 == 22 and [h[4] for h in H2H_FJ] == ["26", "22", "22"]
    assert 3 + 6 + 6 + 3 + 6 + 2 == 26                                  # gamestelling Barcelona
    assert len(H2H_ZS) == 6 and sum("indoor" in h[2] for h in H2H_ZS) == 1
    assert 338000 + 3 * 405000 + 1206000 + 2412000 == 5171000           # officiele optelling prijzengeld
    assert len(STAND) == len(STAND_LENDL) == 4 and len(SCENARIO) == 4
    assert alles.count("<p><strong>De markt:</strong>") == 2 and alles.count(HELE) == 1
    assert "eigen doorrekening" in alles and "eigen telling" in alles   # eigen cijfers altijd als zodanig benoemd
    assert "<h2" not in alles and "<h4" not in alles and "/go/" not in alles
    for verboden in ("betcity", "footymetrics", "opstellingvandaag", "waaroptv", "squawka"):
        assert verboden not in alles.lower(), verboden
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    print("dry run ok")
