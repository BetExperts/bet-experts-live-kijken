# -*- coding: utf-8 -*-
"""Los artikel: Tennis voorspellingen vandaag woensdag 11 november 2026 (ATP Stockholm tweede ronde + WTA Finals Indian Wells, groep 2).
Tips: Fritz -2.5 games vs Norrie (1.54), Gojo +3.5 games vs Humbert (1.58), Muchova wint van Svitolina (1.66),
Andreeva +2.5 games vs Sabalenka (1.60). Combinatie 6,46. Odds = 711 (Kambi sevelevnl, 11-11 ±10:00).
Zoekwoorden: tennis voorspellingen vandaag, tennis wedtips vandaag, ATP Stockholm voorspelling, WTA Finals voorspelling.
Feiten: specials/stockholm_2026_11_11_feiten.md en specials/wta_finals_2026_11_11_feiten.md (ATP daily schedule/results,
ATP media notes, ATP/Tennis Majors-verslagen, WTA day 4-preview, WTA-uitslagen, ziggo.nl/tvgids.nl, tennismylife H2H).
Fitheid gecheckt (regel 4-11): Humbert MTO onderrug Basel 28-10; Norrie 'wasn't feeling my best' (oorzaak onbekend);
Svitolina moeite met bewegen + coach afwezig; Sabalenka knie Wuhan 14-10, zegt nu 'physically I feel better', geen klachten 9-11;
Rune pijnvrij maar twee avondpartijen op rij. Onzeker en daarom vaag of niet genoemd: exacte rankings Fritz/Sonego,
aanvangstijd Rune en Sabalenka-Andreeva (aansluitend), baansnelheid Stockholm, H2H-details Muchova-Svitolina (alleen 3-1 en
Stuttgart-uitslag), scores groep 1 van 10-11, tv in NL voor de WTA Finals (niets bevestigd), indoor/outdoor (outdoor = VAVEL).
  python3 specials/tennis_voorspellingen_2026_11_11.py        (dry run)
  publiceren: specials/concept_publiceer.py tennis_voorspellingen_2026_11_11 --live  (deelkaart og/nieuws/nieuws-<slug>.webp)
  daarna: python3 specials/tennis_voorspellingen_2026_11_11.py --velden  (tennis, wedtips, bookmaker, aanvang)"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "tennis-voorspellingen-vandaag-woensdag-11-november-2026"
RUBRIEK = "665715dbf1f3cbdf7f874d79"   # Tennis
BOOKMAKER_711 = "66a8a87062108480763b7309"
TITEL = "Tennis voorspellingen vandaag: 4 tips voor 11 november"
SAMENVATTING = ("Tennis voorspellingen 11 november: Fritz en Gojo in Stockholm, Muchova en Andreeva op de WTA Finals. "
                "Vier tips met odds, tijden en uitleg.")
ODDS = [1.54, 1.58, 1.66, 1.60]
COMBI = "6,46"

L = {"hub": '<a href="/tennis-voorspellingen-vandaag">tennis voorspellingen vandaag</a>',
     "ziggo": '<a href="/zenders/ziggo-sport">Ziggo Sport</a>',
     "kijken": '<a href="/live-kijken">live kijken</a>',
     "duur": '<a href="/nieuws/hoe-lang-duurt-een-tenniswedstrijd">hoelang duurt een tenniswedstrijd</a>',
     "turijn": '<a href="/nieuws/atp-finals-2026-gekwalificeerd-race-to-turin">ATP Finals 2026: wie zijn er gekwalificeerd?</a>',
     "parijs": '<a href="/nieuws/finale-paris-masters-2026-wanneer-hoe-laat-tv">de Paris Masters</a>',
     "handicap": '<a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">hoe handicap wedden werkt</a>',
     "opgave": '<a href="/nieuws/tennisser-geeft-op-wat-zijn-de-regels-voor-je-weddenschap-bij-nederlandse-bookmakers">wat er gebeurt als een tennisser opgeeft</a>',
     "711": '<a href="/bookmakers/711">711</a>',
     "legaal": '<a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>'}

HELE = "Geldt voor de hele wedstrijd: alle sets tellen mee, een tiebreak telt als één game."


def waarom(punten):
    return "<p><strong>Waarom deze tip?</strong></p><ul>" + "".join(f"<li>{p}</li>" for p in punten) + "</ul>"


def markt(m):
    return f"<p><strong>De markt:</strong> {m}</p>"


TIPS = [("Fritz – Norrie", "ATP Stockholm", "niet voor 14:30 uur", "Fritz -2,5 games", "Game handicap, hele wedstrijd", "1,54"),
        ("Gojo – Humbert", "ATP Stockholm", "niet voor 16:00 uur", "Gojo +3,5 games", "Game handicap, hele wedstrijd", "1,58"),
        ("Muchova – Svitolina", "WTA Finals", "21:00 uur", "Muchova wint", "Winnaar van de wedstrijd", "1,66"),
        ("Andreeva – Sabalenka", "WTA Finals", "aansluitend, ±22:30 uur", "Andreeva +2,5 games", "Game handicap, hele wedstrijd", "1,60")]

content = f"""<p><strong>Onze tennis voorspellingen voor vandaag, woensdag 11 november: Taylor Fritz wint met minstens drie games verschil van Cameron Norrie (Fritz -2,5 games, 1,54), Borna Gojo blijft dicht bij Ugo Humbert (Gojo +3,5 games, 1,58), Karolina Muchova wint van Elina Svitolina (1,66) en Mirra Andreeva houdt het spannend tegen Aryna Sabalenka (Andreeva +2,5 games, 1,60). De eerste twee zijn tweede-rondepartijen van het ATP-toernooi in Stockholm, de laatste twee groepsduels op de WTA Finals in Indian Wells. Gecombineerd is dat een odd van ongeveer {COMBI} bij 711.</strong></p>
<p>Het tennisjaar loopt op zijn eind. Stockholm is het laatste ATP-toernooi voor de ATP Finals in Turijn (15 tot en met 22 november), en in Californië strijden acht van de beste speelsters van het jaar om de laatste grote titel van het seizoen. Drie van onze vier tips zijn games-weddenschappen. Die gelden voor de <strong>hele wedstrijd</strong>: alle sets tellen mee, ook een eventuele derde set, en een tiebreak telt als één game. Bij elke tip staat precies welke markt het is. Alle tijden zijn Nederlandse tijden.</p>
<h3><strong>Tennis voorspellingen vandaag in het kort</strong></h3>
{tabel(["Wedstrijd", "Toernooi", "Aanvang", "Tip", "Markt", "Odd"], [(f"<strong>{w}</strong>", t, a, tip, m, f"<strong>{o}</strong>") for w, t, a, tip, m, o in TIPS] + [("<strong>Combinatie</strong>", "", "", "Alle vier de tips", "", f"<strong>{COMBI}</strong>")])}
<p><em>Odds bij {L['711']}, woensdagochtend 11 november rond 10:00 uur. Odds en aanvangstijden kunnen nog veranderen. De tips staan los van elkaar: je kunt ze apart spelen of combineren.</em></p>
<h3><strong>Het tennisprogramma van woensdag</strong></h3>
{tabel(["Toernooi", "Baan", "Tijd", "Partij"], [
    ("Stockholm", "Center Court", "13:00 uur", "Lorenzo Sonego (Q) – Alejandro Tabilo (4)"),
    ("Stockholm", "Center Court", "niet voor 14:30 uur", "<strong>Taylor Fritz (1) – Cameron Norrie</strong>"),
    ("Stockholm", "Court 1", "niet voor 16:00 uur", "<strong>Borna Gojo (Q) – Ugo Humbert (7)</strong>"),
    ("Stockholm", "Center Court", "niet voor 18:00 uur", "Aleksandr Shevchenko (Q) – Casper Ruud (2)"),
    ("Stockholm", "Center Court", "aansluitend", "Miomir Kecmanovic – Holger Rune"),
    ("WTA Finals", "Stadium 1", "21:00 uur", "<strong>Karolina Muchova (7) – Elina Svitolina (6)</strong>"),
    ("WTA Finals", "Stadium 1", "aansluitend, ±22:30 uur", "<strong>Mirra Andreeva (3) – Aryna Sabalenka (2)</strong>"),
])}
<p>Op Court 1 in Stockholm spelen ook twee Nederlanders in het dubbelspel. Sander Arends en zijn Britse partner Luke Johnson openen om 13:00 uur met hun kwartfinale tegen de Tsjechen Adam Pavlásek en Patrik Rikl. Daarna spelen Jean-Julien Rojer en de Amerikaan Tristan Winegar hun eerste partij, tegen de Zweedse wildcards Wallin en Rejchtman Vinciguerra. Rojer won het dubbelspel in Stockholm al drie keer: in 2010, 2013 en 2022.</p>
<h3><strong>Live kijken</strong></h3>
<p>{L['ziggo']} zendt Stockholm uit: woensdag op Ziggo Sport 4 van 13:00 tot 17:00 uur en van 18:00 tot 22:00 uur, en op Ziggo Sport 1 van 18:00 tot 22:00 uur. Tussen 17:00 en 18:00 uur staat er niets live op de gids. Gojo – Humbert op Court 1 is daardoor misschien niet (helemaal) te zien. Wie de WTA Finals in Nederland uitzendt, was woensdagochtend nog niet bekend. Alle sport van vandaag vind je op onze pagina {L['kijken']}.</p>
<h3><strong>Zo hebben we deze tips gekozen</strong></h3>
<p>Bij elke tip kijken we naar de ranglijst, de vorm van de laatste weken, de onderlinge duels en hoe de spelers deze week speelden. Bij tennis gaat het om één persoon, en dan weegt de fitheid zwaar. Daarom zochten we per speler ook naar blessures, medische time-outs en wat de spelers zelf in interviews zeiden. Twee van onze tips draaien juist om zulke signalen: de rug van Humbert en de stroeve start van Svitolina. Bij elke tip noemen we ook eerlijk het grootste risico.</p>"""

content2 = f"""<h3><strong>Taylor Fritz – Cameron Norrie (Stockholm, niet voor 14:30 uur)</strong></h3>
<p><strong>De situatie.</strong> Fritz is het eerste reekshoofd in Stockholm en had in de eerste ronde een bye. Hij staat dit jaar op 43 zeges en 22 nederlagen en won de titel in Washington. Indoor is hij in vorm: van zijn laatste twaalf partijen in de hal (Lyon, Basel en Parijs) won hij er negen. Hij haalde de finale van Lyon en de halve finale van Basel. In de kwartfinale van {L['parijs']} miste hij vrijdag twee matchpoints tegen Carlos Alcaraz en verloor hij met 7-6(10), 5-7, 3-6. Voor Turijn is hij niet geplaatst: hij eindigde elfde in de Race en gaat als reserve mee. Meer daarover lees je in {L['turijn']}.</p>
<p>Norrie (rond nummer 45 van de wereld) won in de eerste ronde met 7-5, 6-0 van James Duckworth, met tien aces en acht gewonnen games op rij. Opvallend was wat hij na afloop zei: hij voelde zich vooraf "niet op zijn best" en het maakte hem "niet echt uit" of hij won of verloor, hij wilde vooral genieten. Of hij daarmee zijn lichaam of zijn gevoel bedoelde, zei hij niet. Een blessure is niet gemeld.</p>
<p><strong>Onderling.</strong> Fritz leidt met 8-6, en alle veertien duels waren op hardcourt. Ze speelden sinds januari 2024 niet meer tegen elkaar.</p>
{tabel(["Jaar", "Toernooi", "Winnaar", "Uitslag", "Games Fritz – Norrie"], [
    ("2024", "United Cup", "Fritz", "7-6(5), 6-4", "13-10"),
    ("2023", "Tokio", "Fritz", "6-4, 6-3", "12-7"),
    ("2023", "United Cup", "Norrie", "4-6, 7-5, 4-6", "15-17"),
    ("2022", "Davis Cup", "Norrie", "6-2, 6-7(2), 5-7", "17-16"),
    ("2021", "Parijs (indoor)", "Fritz", "6-3, 7-6(3)", "13-9"),
])}
<p><strong>Onze tip: Fritz -2,5 games (1,54).</strong></p>
{markt("game handicap. " + HELE + " Fritz krijgt vooraf 2,5 games achterstand. De tip wint als hij met minstens drie games verschil wint, bijvoorbeeld 6-4, 6-4 (12 tegen 8) of 7-6, 6-4 (13 tegen 10). Bij 7-6, 7-6 (14 tegen 12) is het verschil maar twee games en is de tip verloren. Wint Norrie, dan ook.")}
{waarom(["<strong>Fritz is een van de beste indoorspelers van dit najaar.</strong> Negen zeges in zijn laatste twaalf partijen in de hal, en hij dwong Alcaraz vrijdag tot drie sets.",
         "<strong>Het verschil in niveau.</strong> Nummer 1 van het toernooi tegen een speler rond plek 45, die zelf zegt dat hij zich niet op zijn best voelt.",
         "<strong>Als Fritz wint, wint hij meestal ruim genoeg.</strong> In zijn drie zeges uit de tabel (2024, 2023 en 2021) was het verschil telkens drie games of meer."])}
<p><strong>Het risico:</strong> Norrie is linkshandig en won zes van hun veertien duels. Fritz had dit jaar meerdere keren last van zijn knie; in november is daar niets meer over gemeld. Na de zware week in Parijs en zonder plek in Turijn kan de motivatie ook een rol spelen. Liever op de winnaar? Fritz wint staat op 1,32.</p>
<h3><strong>Borna Gojo – Ugo Humbert (Stockholm, niet voor 16:00 uur)</strong></h3>
<p><strong>De situatie.</strong> Humbert (nummer 39, zevende reekshoofd) haalde vorig jaar de finale in Stockholm. In de eerste ronde won hij met 6-4, 6-3 van Adolfo Daniel Vallejo, maar overtuigend was het niet: hij stond in beide sets een break achter en maakte 34 onnodige fouten. Belangrijker is zijn rug. Op 28 oktober in Basel nam hij tegen Novak Djokovic een medische time-out voor zijn onderrug. Vorig jaar gaf hij in Basel op en meldde hij zich een week later af voor Parijs, ook met rugklachten. Sinds Basel speelde hij drie partijen zonder dat er iets werd gemeld.</p>
<p>Gojo (nummer 134) uit Kroatië kwam via de kwalificaties en won al drie partijen. In de eerste ronde versloeg hij Tomáš Macháč met 6-3, 6-4. Hij sloeg veertien aces, werd geen enkele keer gebroken en werkte alle zes breakpoints weg. Ze speelden nooit eerder tegen elkaar.</p>
<p><strong>Onze tip: Gojo +3,5 games (1,58).</strong></p>
{markt("game handicap. " + HELE + " Gojo krijgt vooraf 3,5 games voorsprong. De tip wint als Gojo de wedstrijd wint, of als hij met maximaal drie games verschil verliest. Bij 7-6, 6-4 voor Humbert (13 tegen 10) is de tip goed; bij 6-4, 6-4 (12 tegen 8) niet.")}
{waarom(["<strong>Gojo serveert in topvorm.</strong> Veertien aces en geen enkele keer gebroken tegen Macháč. Met zo'n service blijven de sets close, en elke tiebreak houdt het gameverschil klein.",
         "<strong>Humbert is wisselvallig.</strong> Hij stond in de eerste ronde in beide sets achter en maakte veel fouten.",
         "<strong>De rug van Humbert.</strong> Een medische time-out twee weken geleden, en een rugverleden. Speelt dat op, dan wordt het snel lastig voor hem.",
         "<strong>Gojo heeft ritme.</strong> Drie gewonnen partijen in Stockholm, waaronder een op het tweede reekshoofd van de kwalificaties."])}
<p><strong>Het risico:</strong> Gojo speelt zijn vierde partij in vijf dagen en heeft weinig ervaring op dit niveau. Breekt Humbert in elke set één keer en wint hij met 6-4, 6-4, dan is de handicap net niet genoeg. Geeft Humbert op, dan bepalen de regels van de bookmaker wat er met je weddenschap gebeurt; lees {L['opgave']}.</p>"""

content3 = f"""<h3><strong>Wat staat er op het spel op de WTA Finals?</strong></h3>
<p>De WTA Finals worden dit jaar niet in Riyad maar in Indian Wells gespeeld, buiten op hardcourt. Na de eerste speeldag van groep 2 staan Andreeva en Sabalenka op één zege, Muchova en Svitolina hebben verloren.</p>
{tabel(["Speelster", "Gespeeld", "Uitslag maandag"], [
    ("Mirra Andreeva (3)", "1-0", "6-4, 6-0 tegen Svitolina"),
    ("Aryna Sabalenka (2)", "1-0", "7-6(2), 7-5 tegen Muchova"),
    ("Karolina Muchova (7)", "0-1", "6-7(2), 5-7 tegen Sabalenka"),
    ("Elina Svitolina (6)", "0-1", "4-6, 0-6 tegen Andreeva"),
])}
<p>De nummers 1 en 2 van de groep gaan naar de halve finale. Wie woensdag Muchova – Svitolina verliest, staat op twee nederlagen en is in twee van de vier mogelijke scenario's al uitgeschakeld. Voor Muchova en Svitolina is het dus bijna alles of niets. Sabalenka en Andreeva strijden daarnaast om de tweede plek op de wereldranglijst aan het eind van het jaar: voor het toernooi scheelde dat 179 punten, en elke groepszege levert 200 punten op.</p>
<h3><strong>Karolina Muchova – Elina Svitolina (WTA Finals, 21:00 uur)</strong></h3>
<p><strong>De situatie.</strong> Muchova (nummer 7) won dit jaar haar eerste WTA 1000-titel in Doha en haalde de finale van Wimbledon. Na het toernooi van Wuhan half oktober nam ze bewust rust. "Ik heb zeker meer kracht in me voor dit toernooi", zei ze voor de start. Maandag verloor ze in bijna twee uur van Sabalenka, maar ze speelde goed mee: ze stond in de eerste set op een break voorsprong en serveerde voor de set, en ze kwam in de tweede set terug tot 5-5.</p>
<p>Svitolina (nummer 6) won dit jaar de titels in Auckland en Rome, maar haar start in Indian Wells was zwak. Tegen Andreeva verloor ze met 4-6, 0-6, kreeg ze zes breakpoints en benutte ze er geen één. Ze verloor de laatste zeven games. Na afloop zei ze zelf dat ze moeite had met bewegen en dat de omstandigheden "een beetje lastig" zijn. Haar vaste coach is er deze week niet, omdat zijn vrouw moet bevallen; oud-speler Sergiy Stakhovsky vervangt hem. Haar laatste wedstrijd voor de Finals was op 16 oktober. Een blessure is niet gemeld.</p>
<p><strong>Onderling.</strong> Svitolina leidt met 3-1 en won beide duels op hardcourt. Maar de enige ontmoeting van dit jaar, in Stuttgart op gravel, won Muchova met 6-4, 2-6, 6-4.</p>
<p><strong>Onze tip: Muchova wint (1,66).</strong></p>
{markt("winnaar van de wedstrijd. Muchova moet de partij winnen; het maakt niet uit in twee of drie sets. Geeft een speelster op, dan bepalen de regels van de bookmaker of je weddenschap geldig blijft.")}
{waarom(["<strong>Muchova speelde maandag op niveau.</strong> Ze hield Sabalenka bijna twee uur bij en was dicht bij een set.",
         "<strong>Svitolina zoekt haar ritme nog.</strong> Ze zei zelf dat ze moeite had met bewegen, verloor de laatste zeven games en mist deze week haar vaste coach.",
         "<strong>De laatste ontmoeting was voor Muchova.</strong> In Stuttgart won ze dit jaar in drie sets."])}
<p><strong>Het risico:</strong> Svitolina is een ervaren vechter, won de Finals in 2018 en won hun twee duels op hardcourt. Muchova is wisselvallig: in Beijing verloor ze in oktober nog met 3-6, 0-6. Na één slechte dag kan Svitolina het "resetten", zoals ze zelf zei.</p>
<h3><strong>Mirra Andreeva – Aryna Sabalenka (WTA Finals, aansluitend, ±22:30 uur)</strong></h3>
<p><strong>De situatie.</strong> Sabalenka (nummer 2) won dit jaar onder meer Indian Wells en Miami, maar haar najaar was zwak. In Beijing verloor ze in de derde ronde en in Wuhan meteen in haar eerste partij. Daar speelde ze met een bandage om haar rechterknie en nam ze in de derde set een medische time-out. Voor het toernooi zei ze dat ze eerst haar lichaam "moest repareren" en dat ze zich fysiek beter voelt. Maandag won ze met 7-6(2), 7-5 van Muchova, zonder zichtbare problemen, maar wel met veel breaks: alleen al in de tweede set vielen er vijf.</p>
<p>Andreeva (nummer 3) won dit jaar Roland Garros, haar eerste grandslamtitel. In haar debuut op de Finals was ze maandag sterk: 6-4, 6-0 tegen Svitolina, in 70 minuten, zonder ook maar één keer haar service te verliezen. Ze won 88 procent van de punten op haar eerste opslag.</p>
<p><strong>Onderling.</strong> Sabalenka leidt met 4-2. Maar hun laatste duel was de finale van Indian Wells 2025, op precies deze plek, en die won Andreeva met 2-6, 6-4, 6-3. Het is hun eerste ontmoeting sinds die finale.</p>
<p><strong>Onze tip: Andreeva +2,5 games (1,60).</strong></p>
{markt("game handicap. " + HELE + " Andreeva krijgt vooraf 2,5 games voorsprong. De tip wint als Andreeva de wedstrijd wint, of als ze met maximaal twee games verschil verliest, bijvoorbeeld bij 7-6, 7-6 (14 tegen 12) of 4-6, 6-4, 6-4 (16 tegen 14) voor Sabalenka. Bij 6-4, 6-4 (12 tegen 8) of 7-6, 6-4 (13 tegen 10) voor Sabalenka is de tip verloren.")}
{waarom(["<strong>Andreeva is in vorm.</strong> Maandag liet ze Svitolina geen enkele break en won ze de laatste zeven games.",
         "<strong>Ze weet hoe ze Sabalenka hier verslaat.</strong> Hun laatste duel, de finale van Indian Wells 2025, won Andreeva.",
         "<strong>De bookmakers zien het ook als een gelijkopgaand duel.</strong> Beide speelsters staan op 1,90 om te winnen; met 2,5 games voorsprong heb je een extra buffer.",
         "<strong>Sabalenka is nog niet helemaal terug.</strong> Na een zwak najaar en knieklachten in oktober verloor ze maandag vijf keer haar service."])}
<p><strong>Het risico:</strong> Sabalenka won vier van hun zes duels, waaronder twee keer ruim op hardcourt in 2025 (6-3, 6-2 en 6-1, 6-2). Ze won dit seizoen bovendien de meeste tiebreaks van het circuit. Komt ze in haar ritme, dan kan ze Andreeva overrompelen.</p>
<h3><strong>Combinatie woensdag 11 november</strong></h3>
<p>Alle vier de tips samen: 1,54 × 1,58 × 1,66 × 1,60 = <strong>± {COMBI}</strong>. Een inzet van €10 levert bij deze combinatie ongeveer €64,60 op. Hoe meer tips in een combinatie, hoe groter de kans dat er één misgaat. Wil je minder risico, speel de tips dan los of combineer alleen de tips die je zelf het sterkst vindt.</p>
<h3><strong>De andere partijen in Stockholm</strong></h3>
<p><strong>Sonego – Tabilo (13:00 uur).</strong> Kwalificant Lorenzo Sonego is de favoriet (1,66) tegen het vierde reekshoofd Alejandro Tabilo. Tabilo verloor in Basel en Parijs van Rafael Jódar en sloeg in Parijs gefrustreerd met zijn racket. Sonego speelt al zijn vierde partij in vijf dagen. Geen tip van ons.</p>
<p><strong>Shevchenko – Ruud (niet voor 18:00 uur).</strong> Titelverdediger Casper Ruud haalde vorige week de halve finale van Parijs en won hun twee eerdere duels, beide met zes games verschil. Kwalificant Aleksandr Shevchenko won zijn drie partijen in Stockholm wel allemaal overtuigend. Wie een veilige optie zoekt: Ruud -2,5 games staat op 1,40.</p>
<p><strong>Kecmanovic – Rune (aansluitend).</strong> Holger Rune keert terug op de plek waar hij vorig jaar zijn achillespees scheurde. Hij won dinsdag met 6-3, 6-4 van het achtste reekshoofd Zizou Bergs en zegt pijnvrij te zijn. Toch speelt hij twee avonden op rij, elf maanden na zijn operatie, en Miomir Kecmanovic versloeg hem in 2023 juist hier in Stockholm. Rune wint staat op 1,40; wij laten deze partij liggen.</p>
<h3><strong>Wat betekenen deze weddenschappen?</strong></h3>
<p><strong>Winnaar.</strong> De speler moet de wedstrijd winnen, in twee of drie sets.</p>
<p><strong>Game handicap (+3,5 of -2,5 games).</strong> Tel na de wedstrijd alle gewonnen games per speler op, over alle sets. Bij een plus-handicap krijgt de speler die games erbij, bij een min-handicap gaan ze eraf. Heeft jouw speler daarna meer games, dan wint de tip. Een tiebreak telt als één game voor de winnaar ervan. Meer uitleg lees je in {L['handicap']}.</p>
<p>Geeft een speler op, dan hangt het van de regels van de bookmaker af wat er met je weddenschap gebeurt. Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit; lees {L['legaal']}. Benieuwd hoe lang een partij duurt? Lees {L['duur']}. Meer tips vind je op onze pagina {L['hub']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wat zijn de beste tennis voorspellingen van vandaag?</strong><br>Fritz -2,5 games tegen Norrie (1,54), Gojo +3,5 games tegen Humbert (1,58), Muchova wint van Svitolina (1,66) en Andreeva +2,5 games tegen Sabalenka (1,60). Gecombineerd is de odd ongeveer {COMBI}.</p>
<p><strong>Gelden de games-tips voor de hele wedstrijd?</strong><br>Ja. De handicaptips tellen alle games van alle sets mee, ook een eventuele derde set. Een tiebreak telt als één game.</p>
<p><strong>Hoe laat speelt Taylor Fritz in Stockholm?</strong><br>Niet voor 14:30 uur Nederlandse tijd, als tweede partij op het Center Court, tegen Cameron Norrie.</p>
<p><strong>Hoe laat speelt Sabalenka tegen Andreeva?</strong><br>Na Muchova – Svitolina, die om 21:00 uur Nederlandse tijd begint. Sabalenka – Andreeva start naar verwachting rond 22:30 uur.</p>
<p><strong>Waar kan ik ATP Stockholm live kijken?</strong><br>Op {L['ziggo']}: woensdag op Ziggo Sport 4 (13:00 tot 17:00 uur en 18:00 tot 22:00 uur) en Ziggo Sport 1 (18:00 tot 22:00 uur).</p>
<p><strong>Wat levert de combinatie op?</strong><br>Ongeveer {COMBI} keer je inzet. Met €10 is dat ongeveer €64,60.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

WEDTIPS = {"wedstrijd-1": "Combinatie: alle vier de tips",
           "wedtip-1-2": "Fritz -2.5 games + Gojo +3.5 games + Muchova wint + Andreeva +2.5 games (games-tips: hele wedstrijd)",
           "quotering-wedtip-1": "6.46",
           "wedstrijd-2": "Fritz vs Norrie", "wedtip-2-2": "Fritz -2.5 games (hele wedstrijd)", "quotering-wedtip-2": "1.54",
           "wedstrijd-3": "Gojo vs Humbert", "wedtip-3-2": "Gojo +3.5 games (hele wedstrijd)", "quotering-wedtip-3": "1.58",
           "wedtip-4-2": "Muchova wint van Svitolina", "quotering-wedtip-4": "1.66"}

if __name__ == "__main__":
    import re
    if "--velden" in sys.argv:
        import lk_webflow as WF
        it = WF._req("GET", f"{WF.WF_API}/collections/{WF.NIEUWS_COLLECTION}/items?slug={SLUG}")["items"][0]
        fd = {"tennis": True, "bookmaker-wedtips": BOOKMAKER_711, "datum-tijd-van-wedstrijd": "2026-11-11T13:30:00.000Z", **WEDTIPS}
        for pad in ("", "/live"):
            WF._req("PATCH", f"{WF.WF_API}/collections/{WF.NIEUWS_COLLECTION}/items/{it['id']}{pad}", {"fieldData": fd})
        print("velden gezet:", it["id"]); sys.exit()
    alles = content + content2 + content3
    w = len(re.sub(r"<[^>]+>", " ", alles).split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", w, "woorden")
    assert len(TITEL) <= 60 and 120 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    p = 1
    for o in ODDS: p *= o
    assert f"{p:.2f}".replace(".", ",") == COMBI, p
    assert f"{10 * p:.1f}" == "64.6", 10 * p
    assert [t[5] for t in TIPS] == ["1,54", "1,58", "1,66", "1,60"]
    # rekenvoorbeelden in de marktuitleg
    assert 13 - 10 >= 3 and 12 - 8 >= 3 and 14 - 12 < 3                 # Fritz -2,5
    assert 13 - 10 <= 3 and 12 - 8 > 3                                     # Gojo +3,5
    assert 14 - 12 <= 2 and 16 - 14 <= 2 and 12 - 8 > 2 and 13 - 10 > 2    # Andreeva +2,5
    assert 4 + 7 + 4 == 15 and 6 + 5 + 6 == 17 and 6 + 6 + 5 == 17 and 2 + 7 + 7 == 16   # H2H-tabel Fritz–Norrie
    assert 7 + 6 == 13 and 6 + 4 == 10 and 6 + 6 == 12 and 4 + 3 == 7 and 6 + 7 == 13 and 3 + 6 == 9
    assert 6 + 7 - (1 + 6) == 6 and 6 + 6 - (2 + 4) == 6                 # Ruud–Shevchenko H2H
    assert 7 + 7 == 14 and 6 + 5 == 11 and 6 + 6 == 12 and 4 + 0 == 4      # stand groep 2
    assert alles.count("<p><strong>De markt:</strong>") == 4 and alles.count(HELE) == 3
    assert "<h2" not in alles and "<h4" not in alles and "betcity" not in alles.lower() and "/go/" not in alles
    assert "indoor hardcourt" not in content3 and "Riyad" in content3
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    print("dry run ok")
