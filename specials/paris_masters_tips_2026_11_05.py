# -*- coding: utf-8 -*-
"""Los artikel: Paris Masters 2026 voorspellingen en wedtips voor donderdag 5 november (dag 4: laatste zestien).
Eigenaar 4-11: 'woensdag wederom 3/4 raak, Tien verloor als enige' (Musetti 7-6(5) 6-2 v Zverev, Etcheverry 7-6(2) 6-3 v De Minaur,
Fils 6-3 7-6(4) v Macháč; Van Assche 7-6(4) 6-4 v Tien).
Odds 711 (Kambi sevelevnl, woensdag 4-11 ±23:05). Om 23:05 stonden alleen de drie middagpartijen op de Central in het aanbod;
de andere vijf (Court 1 + avondsessie) krijgen een voorspelling zonder odd. Komen die odds erbij: ODDS_LATER invullen.
Feiten: specials/paris_dag4_feiten.md (officiële toernooi-API + Tennis Majors/TennisActu/OA Sport/Ubitennis; H2H tennismylife).
Onzeker en daarom vaag of niet genoemd: oorzaak Hijikata's twijfel (nek alleen indirect), medisch nieuws Berrettini (elleboog),
Fils' blessure in Basel (rug volgens TM, linkerbeen volgens Fils zelf).
  python3 specials/paris_masters_tips_2026_11_05.py           (dry run)
  publiceren: specials/concept_publiceer.py paris_masters_tips_2026_11_05 --live; daarna --velden"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "paris-masters-2026-voorspellingen-wedtips-donderdag-5-november"
RUBRIEK = "665715dbf1f3cbdf7f874d79"   # Tennis
BOOKMAKER_711 = "66a8a87062108480763b7309"
TITEL = "Paris Masters voorspellingen vandaag: 5 tips (5 november)"
SAMENVATTING = ("Paris Masters voorspellingen voor donderdag 5 november: Paul wint ruim, Shelton – Rinderknech krijgt een tiebreak "
                "en Musetti – Van Assche wordt lang.")
ODDS = [1.52, 1.50, 1.72]
COMBI = "3,92"

OG_LOGO = "paris-masters-logo.png"
OG_EYEBROW = "Tennis · donderdag 5 november"
OG_KOP = "Paris Masters<br><em>laatste zestien</em>"
OG_TEGELS = [("Gisteren", "3/4"), ("Combi-odd", COMBI)]
OG_KOPJE = "Onze tips (Nederlandse tijd)"
OG_RECHTS = "Odds bij 711"
OG_RIJEN = [("11:00", "Paul -2,5 games tegen Halys", "1,52"),
            ("± 12:30", "Shelton – Rinderknech: tiebreak", "1,50"),
            ("± 14:00", "Musetti – Van Assche: 22+ games", "1,72")]

L = {"hub": '<a href="/nieuws/paris-masters-2026-schema-tijden-tv-deelnemers-prijzengeld">Paris Masters 2026: schema, deelnemers en prijzengeld</a>',
     "kijk": '<a href="/nieuws/atp-1000-parijs-live-gratis-kijken-in-nederland-tv-gids-ziggo-sport-en-gratis-opties-griekspoor-alcaraz-sinner-en-meer-in-actie">Paris Masters 2026 live kijken</a>',
     "gisteren": '<a href="/nieuws/paris-masters-2026-voorspellingen-wedtips-woensdag-4-november">onze tips van woensdag</a>',
     "wiewint": '<a href="/nieuws/wie-wint-paris-masters-2026-favorieten-odds-voorspelling">wie wint de Paris Masters 2026?</a>',
     "djok": '<a href="/nieuws/djokovic-mist-atp-finals-2026-turijn">Djokovic mist de ATP Finals 2026</a>',
     "tips": '<a href="/tennis-voorspellingen-vandaag">tennis voorspellingen vandaag</a>',
     "ziggo": '<a href="/zenders/ziggo-sport">Ziggo Sport</a>',
     "duur": '<a href="/nieuws/hoe-lang-duurt-een-tenniswedstrijd">hoelang duurt een tenniswedstrijd</a>',
     "turijn": '<a href="/nieuws/atp-finals-2026-gekwalificeerd-race-to-turin">ATP Finals 2026: wie zijn er al gekwalificeerd?</a>',
     "handicap": '<a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">hoe handicap wedden werkt</a>',
     "711": '<a href="/bookmakers/711">711</a>',
     "legaal": '<a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>'}


def waarom(punten):
    return "<p><strong>Waarom deze tip?</strong></p><ul>" + "".join(f"<li>{p}</li>" for p in punten) + "</ul>"


def markt(m):
    return f"<p><strong>De markt:</strong> {m}</p>"


TIPS = [("Paul – Halys", "Centercourt, 11:00 uur", "Paul -2,5 games", "Game handicap", "1,52"),
        ("Shelton – Rinderknech", "Centercourt, tweede partij (± 12:30 uur)", "Minstens één tiebreak", "Totaal aantal tiebreaks: meer dan 0,5", "1,50"),
        ("Musetti – Van Assche", "Centercourt, derde partij (± 14:00 uur)", "Meer dan 21,5 games", "Totaal aantal games", "1,72")]

EXTRA = [("Hijikata – Etcheverry", "Court 1, niet voor 14:00 uur", "Extra: Etcheverry +1,5 games", "Game handicap", "1,57"),
         ("Fils – Fritz", "Centercourt, niet voor 20:30 uur", "Extra: Fritz +2,5 games", "Game handicap", "1,60")]

GISTEREN = [("Van Assche – Tien", "Tien wint", "7-6, 6-4 voor Van Assche", "❌"),
            ("Zverev – Musetti", "Musetti wint min. 1 set", "7-6, 6-2 voor Musetti", "✅"),
            ("Etcheverry – De Minaur", "Max. 2 sets", "7-6, 6-3 voor Etcheverry", "✅"),
            ("Fils – Macháč", "Fils wint", "6-3, 7-6 voor Fils", "✅")]

SCHEMA = [("<strong>Centercourt</strong>", "11:00", "Tommy Paul – Quentin Halys"),
          ("<strong>Centercourt</strong>", "daarna", "Ben Shelton – Arthur Rinderknech"),
          ("<strong>Centercourt</strong>", "daarna", "Lorenzo Musetti – Luca Van Assche"),
          ("<strong>Court 1</strong>", "niet voor 14:00", "Rinky Hijikata – Tomás Martín Etcheverry"),
          ("<strong>Court 1</strong>", "daarna", "Nuno Borges – Ignacio Buse"),
          ("<strong>Court 1</strong>", "daarna", "Jan-Lennard Struff – Casper Ruud"),
          ("<strong>Centercourt</strong>", "niet voor 19:00", "Matteo Berrettini – Carlos Alcaraz"),
          ("<strong>Centercourt</strong>", "niet voor 20:30", "Arthur Fils – Taylor Fritz")]

content = f"""<p><strong>Onze Paris Masters voorspellingen voor donderdag 5 november: Tommy Paul wint met minstens drie games verschil van Quentin Halys (1,52), Ben Shelton – Arthur Rinderknech krijgt minstens één tiebreak (1,50) en Lorenzo Musetti – Luca Van Assche duurt meer dan 21,5 games (1,72). De odds zijn van 711; gecombineerd is dat een odd van ongeveer {COMBI}. Nu alle odds bekend zijn, geven we er nog twee losse tips bij: Etcheverry +1,5 games (1,57) en Fritz +2,5 games (1,60). Woensdag zaten opnieuw drie van onze vier tips goed.</strong></p>
<p>Na een woensdag vol verrassingen in de Paris La Défense Arena, met de uitschakeling van Alexander Zverev, Daniil Medvedev, Alex de Minaur en Novak Djokovic, wordt vandaag de hele laatste zestien gespeeld. Er komt in ieder geval een nieuwe winnaar: geen enkele oud-winnaar zit nog in het toernooi. De baan is volgens de spelers de snelste van het seizoen. Musetti zegt dat de bal er laag blijft, Alcaraz noemde hem veel sneller dan in Wenen. Woensdag hadden negen van de veertien enkelpartijen minstens één tiebreak. Parijs ligt in dezelfde tijdzone als Nederland. Alles over het toernooi lees je in {L['hub']}.</p>
<h3><strong>Woensdag: opnieuw 3 van de 4 tips raak</strong></h3>
{tabel(["Wedstrijd", "Onze tip", "Uitslag", ""], GISTEREN)}
<p>Musetti won de eerste set van nummer één Zverev, na 2-5 in de tiebreak, en won daarna zelfs de partij. De Minaur – Etcheverry eindigde in twee sets en Arthur Fils won in de avondsessie overtuigend van Tomáš Macháč, zonder één breekpunt tegen. Alleen Learner Tien stelde teleur: Luca Van Assche redde negen van de tien breekpunten en won in twee sets. Daardoor viel de combinatie niet. Teruglezen kan in {L['gisteren']}. Een tip blijft een inschatting; ook vandaag kan het anders lopen.</p>
<h3><strong>Paris Masters voorspellingen vandaag in het kort</strong></h3>
{tabel(["Wedstrijd", "Baan en tijd", "Tip", "Markt", "Odd"], [(f"<strong>{w}</strong>", t, tip, m, f"<strong>{o}</strong>") for w, t, tip, m, o in TIPS] + [("<strong>Combinatie</strong>", "", "Alle drie de tips", "", f"<strong>{COMBI}</strong>")] + [(f"<strong>{w}</strong>", t, tip, m, f"<strong>{o}</strong>") for w, t, tip, m, o in EXTRA])}
<p><em>Odds bij {L['711']}, woensdagavond 4 november rond 23:00 uur. Odds en aanvangstijden kunnen nog veranderen; tijden met ± zijn een schatting, omdat de partijen na elkaar op dezelfde baan worden gespeeld. De tips staan los van elkaar: je kunt ze apart spelen of combineren. De partijen op Court 1 en in de avondsessie stonden toen nog niet in het aanbod. De twee extra tips (odds donderdagochtend rond 07:00 uur) staan los van de combinatie en worden verderop uitgelegd.</em></p>
<h3><strong>Het speelschema van donderdag</strong></h3>
{tabel(["Baan", "Tijd", "Partij"], SCHEMA)}
<p>De twee avondpartijen kunnen volgens de organisatie nog van plek wisselen. {L['ziggo']} zendt de Paris Masters uit; hoe je gratis kunt kijken, lees je in {L['kijk']}.</p>"""

content2 = f"""<h3><strong>Tommy Paul – Quentin Halys (centercourt, 11:00 uur)</strong></h3>
<p><strong>De situatie.</strong> Paul (nummer 14, twaalfde reekshoofd) is fris. Na een zege in twee sets op Holger Rune had hij woensdag maar 48 minuten nodig tegen Daniel Mérida: 6-1, 6-1, met 34 winners tegen 8 onnodige fouten. De Amerikaan staat dit seizoen op 48 zeges en 21 nederlagen en haalde onlangs de halve finale in Lyon en de kwartfinale in Wenen. Hij moet hier ver komen om nog naar Turijn te gaan.</p>
<p>Halys (nummer 46) beleefde woensdag de grootste avond van zijn carrière. Tegen Frances Tiafoe sloeg hij 17 aces en redde hij in de tiebreak van de derde set vier matchpunten. Het was pas zijn tweede zege op een top-10-speler, na 1 zege en 21 nederlagen. Die partij duurde bijna twee uur en was emotioneel zwaar, en vandaag moet hij later ook nog dubbelspelen. Dit seizoen staat hij op 26-22.</p>
<p><strong>Onderling.</strong> Ze speelden nog nooit tegen elkaar.</p>
<p><strong>Onze tip: Paul -2,5 games (1,52).</strong></p>
{markt("game handicap. Paul begint met 2,5 games achterstand. Wint hij met 6-4, 6-4 (12 tegen 8 games), dan wint hij met 4 games verschil en is de tip goed. Bij 7-6, 6-4 is het verschil 3 games: ook goed. Bij 7-6, 7-6 (2 games verschil) is de tip verloren; ook een nipte driesetter kan te krap zijn. Meer uitleg lees je in " + L['handicap'] + ".")}
{waarom(["<strong>Paul is in vorm en uitgerust.</strong> Twee overtuigende zeges, en woensdag stond hij nog geen uur op de baan.",
         "<strong>Halys moet herstellen.</strong> Na een emotionele partij van twee uur moet hij weer om 11:00 uur beginnen, met later ook een dubbelpartij.",
         "<strong>Het niveauverschil op hardcourt.</strong> Paul staat op 30-15, Halys op 15-16."])}
<p><strong>Het risico:</strong> Halys serveert hard en won deze week al zijn tiebreaks. Met het thuispubliek achter zich kan hij sets lang spannend houden. Wil je meer zekerheid? Paul wint staat op 1,29.</p>
<h3><strong>Ben Shelton – Arthur Rinderknech (centercourt, ± 12:30 uur)</strong></h3>
<p><strong>De situatie.</strong> Shelton (nummer 4, derde reekshoofd) won dit jaar vier titels en haalde de finale van de US Open. Sindsdien gaat het minder: in Bazel verloor hij nog van een wildcard buiten de top 200. In Parijs begon hij wel sterk: tegen Cameron Norrie won hij 28 van de 32 punten op zijn eerste service. Hij is al zeker van Turijn en had woensdag rust.</p>
<p>Rinderknech (nummer 68) is een van de Franse uitblinkers deze week. Woensdag won hij in 65 minuten van Mattia Bellucci, zonder één breekpunt tegen. Ook hij speelt vandaag nog een dubbelpartij.</p>
<p><strong>Onderling.</strong> Rinderknech leidt met 1-0: op Queen's 2025 won hij met 7-6, 7-6.</p>
<p><strong>Onze tip: minstens één tiebreak (1,50).</strong></p>
{markt("totaal aantal tiebreaks, meer dan 0,5. De tip is goed zodra er in de partij één tiebreak wordt gespeeld, ongeacht wie er wint.")}
{waarom(["<strong>Twee grote serveerders op een snelle baan.</strong> Shelton heeft een van de beste opslagen van het circuit, Rinderknech gaf woensdag geen enkel breekpunt weg.",
         "<strong>Het enige onderlinge duel had twee tiebreaks.</strong> Op Queen's eindigden beide sets in 7-6.",
         "<strong>De cijfers van deze week.</strong> Woensdag kwam het in negen van de veertien enkelpartijen tot minstens één tiebreak."])}
<p><strong>Het risico:</strong> één vroege break per set kan genoeg zijn. Shelton is de duidelijke favoriet, en als Rinderknech op zijn tweede service wankelt, kan het een 6-4, 6-4 worden. Durf je meer? Rinderknech wint minstens één set staat op 1,88.</p>
<h3><strong>Lorenzo Musetti – Luca Van Assche (centercourt, ± 14:00 uur)</strong></h3>
<p><strong>De situatie.</strong> Musetti (nummer 24) is de man van de week. Hij won twee weken geleden het toernooi van Lyon en versloeg woensdag Zverev in diens eerste partij als nummer één van de wereld. Hij hield al zijn opslagbeurten en won acht van zijn laatste negen partijen. Indoor staat hij dit seizoen op 8-1.</p>
<p>Van Assche (nummer 47) haalt voor het eerst de laatste zestien van een Masters-toernooi. Tegen Tien sloeg hij 11 aces, redde hij negen van de tien breekpunten en won hij het matchpunt na een rally van 41 slagen. Het publiek staat vandaag achter hem: hij is de derde Fransman op rij op de centercourt.</p>
<p><strong>Onderling.</strong> Het staat 1-1, en beide duels waren lang. Op de Australian Open van 2024 won Van Assche in vijf sets. In de kwartfinale van Lyon, twee weken geleden, won Musetti met 7-6, 6-7, 6-4, na 3,5 uur.</p>
<p><strong>Onze tip: meer dan 21,5 games (1,72).</strong></p>
{markt("totaal aantal games, meer dan 21,5. Alle games van beide spelers tellen mee, tiebreaks tellen als één game. De tip is goed vanaf 22 games, bijvoorbeeld bij 7-5, 6-4 of bij elke driesetter. Bij 6-4, 6-4 (20 games) is de tip verloren. Wie er wint, maakt niet uit.")}
{waarom(["<strong>Hun laatste duel was een marathon.</strong> In Lyon werden er twee weken geleden 36 games gespeeld, op dezelfde ondergrond.",
         "<strong>Allebei sterk op de opslag deze week.</strong> Musetti hield al zijn servicegames tegen Zverev, Van Assche gaf maar één break weg tegen Tien.",
         "<strong>Van Assche heeft het publiek mee.</strong> Dat maakt een snelle 2-0 van Musetti minder waarschijnlijk."])}
<p><strong>Het risico:</strong> Musetti is in topvorm. Als hij vroeg breekt en Van Assche moe is na twee lange partijen, kan het een korte wedstrijd worden. Liever op de winnaar? Musetti wint staat op 1,38.</p>"""

content3 = f"""<h3><strong>Combinatie donderdag 5 november</strong></h3>
<p>Alle drie de tips samen: 1,52 × 1,50 × 1,72 = <strong>± {COMBI}</strong>. Een inzet van €10 levert bij deze combinatie ongeveer €39 op. Hoe meer tips in een combinatie, hoe groter de kans dat er één misgaat. Wil je minder risico, speel de tips dan los, of combineer alleen Paul en de tiebreak bij Shelton – Rinderknech (samen ± 2,28).</p>
<h3><strong>Twee extra tips nu alle odds bekend zijn</strong></h3>
<p>Donderdagochtend kwamen ook de odds voor Court 1 en de avondsessie online. Daar halen we nog twee losse tips uit. Ze staan niet in de combinatie hierboven; speel ze apart of maak er je eigen combinatie mee.</p>
<p><strong>Extra tip 1: Etcheverry +1,5 games tegen Hijikata (1,57).</strong></p>
{markt("game handicap. Etcheverry krijgt 1,5 games voorsprong. De tip is goed als hij wint, en ook als hij verliest met maar één game verschil, zoals bij 6-7, 7-6, 6-7. Verliest hij met twee games of meer verschil, bijvoorbeeld 4-6, 6-4, 4-6 of 6-7, 6-7, dan is de tip verloren.")}
{waarom(["<strong>Twijfel over Hijikata.</strong> De kwalificant zei na zijn zege op Djokovic dat hij 's ochtends niet wist of hij kon spelen. Vandaag speelt hij zijn vijfde partij in zes dagen.",
         "<strong>Etcheverry won hun enige duel ruim.</strong> Dat werd 6-1, 6-4.",
         "<strong>Ook een nipte nederlaag is genoeg.</strong> Met 1,5 games voorsprong mag Etcheverry zelfs verliezen, als het maar krap is."])}
<p><strong>Het risico:</strong> ook Etcheverry speelt voor de derde dag op rij en stond in twee partijen bijna vijf uur op de baan. Is Hijikata wel fit, dan is hij met zijn snelle spel lastig op deze baan.</p>
<p><strong>Extra tip 2: Fritz +2,5 games tegen Fils (1,60).</strong></p>
{markt("game handicap. Fritz krijgt 2,5 games voorsprong. De tip is goed als Fritz wint, en ook als Fils wint met hooguit twee games verschil, zoals bij 7-6, 7-6 of in een spannende driesetter. Wint Fils met 6-4, 7-6 (drie games verschil) of ruimer, dan is de tip verloren.")}
{waarom(["<strong>Fritz is in vorm.</strong> Hij sloeg woensdag 37 aces zonder één dubbele fout en staat indoor dit jaar op 12-3.",
         "<strong>Hij moet winnen.</strong> Alleen met een plek in de halve finale houdt Fritz nog kans op Turijn; Fils is al zeker.",
         "<strong>Weinig breaks verwacht.</strong> Met twee sterke serveerders op een snelle baan wordt het verschil in games waarschijnlijk klein, ook als Fils wint."])}
<p><strong>Het risico:</strong> Fils heeft het Franse publiek mee en speelde woensdag zonder klachten. De bookmaker ziet hem als favoriet. Fritz speelt voor de derde avond op rij.</p>
<h3><strong>Onze voorspelling voor de andere partijen</strong></h3>
<p>Deze partijen stonden woensdagavond nog niet in het aanbod. Hieronder onze verwachting, met de odds van donderdagochtend rond 07:00 uur (711).</p>
<p><strong>Hijikata – Etcheverry (Court 1, niet voor 14:00 uur): lichte voorkeur voor Etcheverry (1,76; Hijikata 2,06). Onze extra tip: Etcheverry +1,5 games.</strong> Kwalificant Rinky Hijikata won woensdag van Djokovic, maar zei daarna dat hij 's ochtends niet zeker wist of hij kon spelen. Hij gaf geen reden. Het is zijn vijfde partij in zes dagen. Etcheverry won hun enige duel (6-1, 6-4) en redde tegen De Minaur 12 van de 13 breekpunten. Wel speelt hij al drie dagen op rij, met bijna vijf uur speeltijd in twee partijen.</p>
<p><strong>Borges – Buse (Court 1): lichte voorkeur voor Borges (1,63; Buse 2,28).</strong> Nuno Borges kwam als lucky loser in het hoofdtoernooi en hield daar al zijn servicegames: tegen Karen Khachanov kreeg hij geen enkel breekpunt tegen. Indoor staat hij dit seizoen op 4-1. Ignacio Buse versloeg Medvedev, maar is vooral een gravelspeler. Hij won wel het enige onderlinge duel, op gravel in de Davis Cup.</p>
<p><strong>Struff – Ruud (Court 1): voor ons een fiftyfiftypartij (Ruud 1,53; Struff 2,50).</strong> Jan-Lennard Struff is indoor in de vorm van zijn leven: finale in Brussel, halve finale in Bazel en 10 zeges in zijn laatste 12 indoorpartijen. Hij leidt ook met 3-1 tegen Casper Ruud. Maar de Duitser is 36, speelt drie dagen op rij en stond woensdag 2 uur en 23 minuten op de baan. Ruud had een rustdag. Als Struff fris begint, is hij de gevaarlijkste.</p>
<p><strong>Berrettini – Alcaraz (centercourt, niet voor 19:00 uur): Alcaraz wint (1,15; Berrettini 5,50).</strong> Carlos Alcaraz is fit, won zijn laatste zes partijen en leidt met 3-1 tegen Matteo Berrettini. De Italiaan had woensdag tegen Ugo Humbert last van zijn rechterelleboog en greep in de tweede set meerdere keren naar zijn onderarm. Of hij er vandaag last van heeft, is niet bekend. Wel blijft hij met zijn opslag (13 aces woensdag) gevaarlijk in tiebreaks.</p>
<p><strong>Fils – Fritz (centercourt, niet voor 20:30 uur): de topper van de dag, met een kleine voorkeur voor Fritz (2,12; Fils 1,72). Onze extra tip: Fritz +2,5 games.</strong> De bookmaker ziet Fils als favoriet, wij denken dat Fritz hier iets te hoog staat. Het is een herhaling van de kwartfinale in Bazel, zes dagen geleden. Arthur Fils gaf daar op bij 2-6, 0-2. Fils is sinds woensdag zeker van Turijn en speelde tegen Macháč zonder zichtbare klachten. Zijn blessure in Bazel wordt verschillend omschreven: Fils sprak zelf van een spierprobleem in zijn linkerbeen, andere bronnen noemen zijn rug. Taylor Fritz moet winnen om nog kans te maken op Turijn. Hij sloeg woensdag 37 aces en maakte geen enkele dubbele fout, al speelt hij wel voor de derde dag op rij laat op de avond. Indoor staat hij dit jaar op 12-3. Gezien hun opslag verwachten we weinig breaks. Wie wat nodig heeft voor Turijn lees je in {L['djok']} en {L['turijn']}.</p>
<p>Wie volgens ons de titel pakt, lees je in ons artikel {L['wiewint']}</p>
<h3><strong>Wat betekenen deze weddenschappen?</strong></h3>
<p><strong>Game handicap.</strong> De favoriet begint met een achterstand in games. Bij -2,5 moet hij met minstens drie games verschil winnen, opgeteld over de hele partij. Bij +1,5 of +2,5 krijgt een speler juist een voorsprong: hij mag verliezen, zolang het verschil kleiner blijft dan die voorsprong.</p>
<p><strong>Totaal aantal tiebreaks, meer dan 0,5.</strong> De tip is goed zodra er één tiebreak wordt gespeeld.</p>
<p><strong>Totaal aantal games, meer dan 21,5.</strong> Alle games van beide spelers samen moeten op 22 of meer uitkomen. Een tiebreak telt als één game.</p>
<p>Geeft een speler op, dan hangt het van de regels van de bookmaker af wat er met je weddenschap gebeurt. Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit; lees {L['legaal']}. Benieuwd hoe lang een partij duurt? Lees {L['duur']}. Meer tips vind je op onze pagina {L['tips']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wat zijn de beste Paris Masters-voorspellingen van vandaag?</strong><br>Paul wint met minstens drie games verschil van Halys (1,52), Shelton – Rinderknech krijgt minstens één tiebreak (1,50) en Musetti – Van Assche duurt meer dan 21,5 games (1,72). Gecombineerd is de odd ongeveer {COMBI}. Losse extra tips: Etcheverry +1,5 games (1,57) en Fritz +2,5 games (1,60).</p>
<p><strong>Hoe deden de tennistips van gisteren het?</strong><br>Drie van de vier waren goed: Musetti won een set van Zverev (en de partij), De Minaur – Etcheverry eindigde in twee sets en Fils won van Macháč. Tien verloor van Van Assche.</p>
<p><strong>Hoe laat speelt Alcaraz vandaag?</strong><br>In de avondsessie op de centercourt, niet voor 19:00 uur, tegen Matteo Berrettini. Daarna volgt Fils – Fritz; de twee avondpartijen kunnen nog van plek wisselen.</p>
<p><strong>Wie wint Fils – Fritz?</strong><br>Een open partij. Wij hebben een kleine voorkeur voor Fritz: hij is indoor sterk, serveert uitstekend en moet winnen voor Turijn. Onze tip is Fritz +2,5 games (1,60). Fils heeft het publiek mee, maar gaf vorige week tegen Fritz nog op.</p>
<p><strong>Speelt Berrettini tegen Alcaraz?</strong><br>Hij staat op het schema. Berrettini had woensdag last van zijn elleboog; over een afmelding is niets bekend.</p>
<p><strong>Waar kan ik de Paris Masters live kijken?</strong><br>Op Ziggo Sport. Gratis kijken kan ook; hoe, lees je in {L['kijk']}.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

WEDTIPS = {"wedstrijd-1": "Combinatie: alle drie de tips",
           "wedtip-1-2": "Paul -2.5 games + Shelton vs Rinderknech minstens één tiebreak + Musetti vs Van Assche meer dan 21.5 games",
           "quotering-wedtip-1": "3.92",
           "wedstrijd-2": "Paul vs Halys", "wedtip-2-2": "Paul -2.5 games", "quotering-wedtip-2": "1.52",
           "wedstrijd-3": "Shelton vs Rinderknech", "wedtip-3-2": "Minstens één tiebreak", "quotering-wedtip-3": "1.50",
           "wedtip-4-2": "Musetti vs Van Assche meer dan 21.5 games", "quotering-wedtip-4": "1.72"}

if __name__ == "__main__":
    import re
    if "--velden" in sys.argv:
        import lk_webflow as WF
        it = WF._req("GET", f"{WF.WF_API}/collections/{WF.NIEUWS_COLLECTION}/items?slug={SLUG}")["items"][0]
        fd = {"tennis": True, "bookmaker-wedtips": BOOKMAKER_711, "datum-tijd-van-wedstrijd": "2026-11-05T10:00:00.000Z", **WEDTIPS}
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
    assert abs(1.52 * 1.50 - 2.28) < 0.01 and round(10 * p) == 39
    assert [t[4] for t in TIPS] == ["1,52", "1,50", "1,72"]
    assert alles.count("<p><strong>De markt:</strong>") == 5
    assert "<h2" not in alles and "<h4" not in alles and "betcity" not in alles.lower() and "/go/" not in alles
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    print("dry run ok")
