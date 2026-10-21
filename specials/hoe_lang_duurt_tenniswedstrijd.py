# -*- coding: utf-8 -*-
"""Los artikel (evergreen): Hoelang duurt een tenniswedstrijd? Feiten nagelopen op 21-10-2026: ITF Rules of Tennis
2026, ATP (By The Numbers 2025, hitteregel 15-12-2025), PTPA 2024, The Athletic, Opta/Tennis Majors, ITF Coaching
Review 2019, Tennis Abstract, Wikipedia (records), AP/Reuters/AFP. Grandslamfinale-gemiddelden = eigen berekening 2022-2026.
  python3 specials/hoe_lang_duurt_tenniswedstrijd.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Hoelang duurt een tenniswedstrijd? Van snelle partij tot vijfsetter"
SLUG = "hoe-lang-duurt-een-tenniswedstrijd"
SAMENVATTING = ("Een tenniswedstrijd duurt gemiddeld 1,5 tot 2 uur, een vijfsetter op een grandslam 3 tot 6 uur. "
                "Alle gemiddelden, regels en records op een rij.")
RUBRIEK_TENNIS = "665715dbf1f3cbdf7f874d79"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


content = f"""<p><strong>Een tenniswedstrijd heeft geen vaste speeltijd. Een gewone partij over twee gewonnen sets (best of three) duurt gemiddeld anderhalf tot twee uur, een grandslamwedstrijd bij de mannen over drie gewonnen sets (best of five) gemiddeld bijna drie uur. Een echte vijfsetter loopt al snel uit tot vier à zes uur. De kortste wedstrijden zijn binnen een halfuur klaar, de langste ooit duurde 11 uur en 5 minuten, verdeeld over drie dagen.</strong></p>
<p>Waarom lopen tenniswedstrijden zo uiteen? Dat komt door de telling: er is geen klok die afloopt, je moet een vast aantal punten, games en sets winnen. Zolang twee spelers aan elkaar gewaagd zijn, kan het in theorie eindeloos doorgaan. In dit artikel lees je hoe lang een wedstrijd gemiddeld duurt per formaat, welke regels de duur bepalen, waarom wedstrijden steeds langer worden, welke records er staan en hoeveel tijd je moet reserveren als je live wilt kijken.</p>
<h3><strong>Hoelang duurt een tenniswedstrijd gemiddeld?</strong></h3>
{tabel(["Soort wedstrijd", "Gemiddelde duur", "Uitersten"], [
    ("Profwedstrijd algemeen (ATP/WTA)", "± 2 uur (120 minuten in 2024)", "-"),
    ("ATP-toernooi, best of three", "1,5 tot 2 uur", "45 min tot 3u48 (ATP 2025)"),
    ("WTA-toernooi, best of three", "± 1,5 uur (97 minuten)", "40 min tot 3u45"),
    ("Grandslam mannen, best of five", "± 3 uur (2u54 in 2023)", "Tot 11u05"),
    ("Grandslam vrouwen, best of three", "± 1u45", "Tot 4u44"),
    ("Grandslamfinale mannen", "± 3u30", "Tot 5u53"),
    ("Grandslamfinale vrouwen", "± 1u50", "32 min tot 2u46"),
])}
<p><em>Bronnen: PTPA Player Health Report 2024, ATP By The Numbers 2025, Tennis Abstract, The Athletic, Opta. Gemiddelden grandslamfinales: onze berekening over 2022-2026.</em></p>
<h3><strong>Waarom heeft tennis geen vaste speeltijd?</strong></h3>
<p>In voetbal of hockey speel je een vast aantal minuten. In tennis win je pas als je de laatste set binnenhaalt. Die telling werkt in vier lagen:</p>
<ul><li><strong>Punt:</strong> één rally. De telling in een game gaat 15, 30, 40, game.</li><li><strong>Game:</strong> wie als eerste vier punten wint met twee punten verschil. Bij 40-40 (deuce) moet je twee punten op rij winnen, en dat kan lang duren.</li><li><strong>Set:</strong> wie als eerste zes games wint met twee games verschil. Bij 6-6 volgt een tiebreak tot 7 punten.</li><li><strong>Wedstrijd:</strong> wie als eerste twee sets wint (best of three) of drie sets (best of five).</li></ul>
<p>Een wedstrijd van 6-0, 6-0 bestaat uit minimaal 48 punten. Een wedstrijd waarin elke game naar deuce gaat en elke set een tiebreak heeft, kan er honderden tellen. Daarom loopt de duur zo sterk uiteen.</p>
<h3><strong>Best of three of best of five: het grootste verschil</strong></h3>
<p>Het formaat bepaalt het meest hoe lang je bezig bent. Op vrijwel alle ATP- en WTA-toernooien geldt best of three: wie twee sets wint, is klaar. Alleen het mannenenkelspel op de vier grandslams (<a href="/competities/australian-open">Australian Open</a>, <a href="/competities/roland-garros">Roland Garros</a>, <a href="/competities/wimbledon">Wimbledon</a> en de <a href="/competities/us-open">US Open</a>) wordt over best of five gespeeld. Ook het vrouwenenkelspel op de grandslams is best of three.</p>
<p>Dat verschil zie je direct terug in de cijfers. Een grandslamwedstrijd bij de mannen duurde in 2023 gemiddeld 2 uur en 54 minuten. Op de Australian Open 2024 was het gemiddelde in de eerste week zelfs 2 uur en 57 minuten, met 55 wedstrijden van meer dan drie uur. Bij de vrouwen lag het gemiddelde op hetzelfde toernooi op 1 uur en 45 minuten.</p>
<h3><strong>Hoelang duurt een game, een set en een punt?</strong></h3>
<p>Uit een studie van de ITF naar grandslamwedstrijden bij de mannen kun je goed afleiden hoe lang de onderdelen gemiddeld duren:</p>
{tabel(["Onderdeel", "Op gravel", "Op hardcourt en gras"], [
    ("Hele wedstrijd (best of five)", "± 149 minuten", "± 125 minuten"),
    ("Aantal sets", "3,4", "3,1"),
    ("Aantal games", "32,8", "29,9"),
    ("Eén set", "± 44 minuten", "± 40 minuten"),
    ("Eén game", "± 4,5 minuut", "± 4,2 minuten"),
    ("Eén punt, inclusief pauzes", "± 43 seconden", "± 39 seconden"),
    ("Eén punt, bal echt in het spel", "6,3 seconden", "5,1 seconden"),
])}
<p><em>Bron: ITF Coaching & Sport Science Review (2019), grandslamwedstrijden. Duur per set, game en punt is onze berekening.</em></p>
<p>Als vuistregel kun je dus uitgaan van zo'n 40 tot 45 minuten per set en 4 tot 5 minuten per game. Een best-of-threewedstrijd in twee sets duurt dan rond de anderhalf uur, een driesetter eerder twee uur of meer.</p>
<h3><strong>De bal is maar 13 tot 15 procent van de tijd in het spel</strong></h3>
<p>Een verrassend feit: in een tenniswedstrijd wordt veel minder getennist dan je denkt. Volgens dezelfde ITF-studie is de bal maar 12,9 procent (snelle banen) tot 14,5 procent (gravel) van de totale wedstrijdtijd echt in het spel. In een wedstrijd van twee uur gaat het dus om maar 15 tot 17 minuten pure speeltijd. Een gemiddelde rally telt ruim vier slagen. De rest van de tijd gaat op aan de pauze tussen punten, het wisselen van kant, setpauzes, het oprapen van ballen en het voorbereiden van de service.</p>"""

content2 = f"""<h3><strong>Welke regels bepalen hoe lang een wedstrijd duurt?</strong></h3>
<p>De tijd tussen de punten is aan strikte regels gebonden. Dit zijn de officiële regels van de ITF (Rules of Tennis 2026), die ook op de ATP, de WTA en de grandslams gelden:</p>
{tabel(["Regel", "Maximale tijd"], [
    ("Tussen twee punten (shotclock)", "25 seconden"),
    ("Wisselen van kant na een oneven game", "90 seconden"),
    ("Na de eerste game van een set en tijdens een tiebreak", "Wisselen zonder pauze"),
    ("Pauze tussen twee sets", "120 seconden"),
    ("Inspelen voor de wedstrijd", "5 minuten"),
    ("Medische time-out", "1 keer 3 minuten (voor een behandelbare blessure)"),
    ("Toiletpauze (ATP)", "1 keer 3 minuten, alleen in een setpauze, plus 2 minuten om om te kleden"),
    ("Extra rustpauze (alleen als vooraf aangekondigd)", "Maximaal 10 minuten na de 2e set (best of three) of 3e set (best of five)"),
])}
<p>Sinds een paar jaar hangt er op elke grote baan een zichtbare shotclock. De klok begint te lopen zodra de scheidsrechter de stand heeft omgeroepen, en wie te laat serveert, krijgt een waarschuwing en daarna een strafpunt. Toch blijft er veel tijd tussen de punten zitten: op de Australian Open van 2016 werd gemiddeld 21,5 seconden tussen twee punten gemeten.</p>
<p><strong>Hitte en regen</strong><br>Ook het weer bepaalt de duur. Sinds 2026 heeft de ATP een hitteregel: bij een hoge hittestress-index (vanaf 30,1 graden WBGT) mag elke speler in een best-of-threepartij na de tweede set een koelpauze van tien minuten aanvragen, en boven 32,2 graden wordt het spel stilgelegd. De Australian Open heeft een eigen hitteschaal. Regen kan een wedstrijd uren onderbreken, al hebben de grandslams inmiddels daken op hun belangrijkste banen. Op Wimbledon geldt een avondklok: om 23:00 uur lokale tijd moet het spel stoppen.</p>
<h3><strong>De tiebreak in de beslissende set: einde aan de eindeloze vijfde set</strong></h3>
<p>Lange tijd werd de laatste set op sommige grandslams zonder tiebreak gespeeld: je moest met twee games verschil winnen, hoe lang dat ook duurde. Zo kon het gebeuren dat John Isner en Nicolas Mahut op Wimbledon 2010 in de vijfde set tot 70-68 doorgingen. Sinds Roland Garros 2022 spelen alle vier de grandslams bij 6-6 in de beslissende set een tiebreak tot 10 punten (met twee punten verschil). Daarmee is een wedstrijd van elf uur vrijwel onmogelijk geworden.</p>
<p>Lang blijft het wel. De langste wedstrijd onder de nieuwe regel was op Roland Garros 2026: Juan Manuel Cerúndolo en Martín Landaluce speelden vijf sets met vier tiebreaks, in bijna zes uur (5u58).</p>
<h3><strong>Gravel, gras of hardcourt: maakt de ondergrond uit?</strong></h3>
<p>Ja. Op gravel stuitert de bal hoger en langzamer, waardoor rally's langer duren en de server minder makkelijke punten pakt. In de ITF-studie duurde een grandslamwedstrijd op gravel gemiddeld 149 minuten, tegen 125 minuten op hardcourt en gras. Op gravel werden ook meer sets en games gespeeld. Roland Garros heeft dan ook de langste gemiddelde mannenwedstrijden van de vier grandslams (bijna drie uur), Wimbledon op gras de kortste (rond de 2,5 uur). De Australian Open zat daar met gemiddeld 163 minuten tussenin.</p>
<h3><strong>Worden tenniswedstrijden steeds langer?</strong></h3>
<p>Ja, en flink. Volgens de spelersvakbond PTPA duurde een gemiddelde profwedstrijd in 1999 nog 98 minuten, en in 2024 120 minuten: ruim 20 procent langer. Op de grandslams ging een mannenwedstrijd van gemiddeld 2 uur en 21 minuten in 1999 naar 2 uur en 54 minuten in 2023. De PTPA vatte het samen als: drie sets in 2024 zijn als vier sets in 1999.</p>
<p>Vaak genoemde oorzaken: spelers zijn fitter en verdedigen beter, waardoor punten langer duren, en er wordt tussen de punten meer tijd genomen dan vroeger. De discussie over kortere formats laait dan ook geregeld op. In 2026 werd geopperd om op de grandslams in de eerste rondes best of three te spelen en pas vanaf de kwartfinales best of five, maar een besluit is er niet.</p>
<h3><strong>Dubbelspel, Laver Cup, Davis Cup en andere formats</strong></h3>
<p>Niet elke wedstrijd wordt in het klassieke format gespeeld. Een paar varianten die een wedstrijd een stuk korter maken:</p>
<ul><li><strong>Dubbelspel (ATP en WTA):</strong> no-ad-telling (op deuce beslist één punt) en bij 1-1 in sets een match-tiebreak tot 10 in plaats van een derde set. Bij de invoering in 2005 was het doel een duur van rond de 80 minuten. Op de grandslams is ook het herendubbel sinds 2023 overal best of three.</li><li><strong>Laver Cup:</strong> best of three, maar bij 1-1 een match-tiebreak tot 10 in plaats van een derde set.</li><li><strong>Davis Cup Finals:</strong> twee enkels en één dubbel per ontmoeting, allemaal best of three met tiebreaks.</li><li><strong>United Cup:</strong> een herenenkel, een damesenkel en een gemengd dubbel. In het dubbel volgt bij 1-1 een match-tiebreak.</li><li><strong>Next Gen ATP Finals:</strong> het proeflab van de ATP. Sets tot 4 games (tiebreak bij 3-3), best of five, no-ad en een kortere shotclock na korte punten.</li><li><strong>Exhibities</strong> zoals de <a href="/nieuws/six-kings-slam-2026">Six Kings Slam</a>: best of three, zonder rankingpunten.</li></ul>"""

content3 = f"""<h3><strong>De langste tenniswedstrijden ooit</strong></h3>
{tabel(["Wedstrijd", "Toernooi", "Duur"], [
    ("John Isner – Nicolas Mahut (70-68 in de 5e set)", "Wimbledon 2010, 1e ronde", "<strong>11 uur en 5 minuten</strong> (over drie dagen)"),
    ("Vicki Nelson – Jean Hepner (langste vrouwenwedstrijd)", "Richmond (VS) 1984", "6 uur en 31 minuten"),
    ("Fabrice Santoro – Arnaud Clément", "Roland Garros 2004", "6 uur en 33 minuten"),
    ("J.M. Cerúndolo – Martín Landaluce (langste met tiebreak tot 10)", "Roland Garros 2026", "5 uur en 58 minuten"),
    ("Novak Djokovic – Rafael Nadal (langste grandslamfinale)", "Australian Open 2012", "5 uur en 53 minuten"),
    ("Dan Evans – Karen Khachanov (langste US Open-wedstrijd)", "US Open 2024", "5 uur en 35 minuten"),
    ("Francesca Schiavone – Svetlana Kuznetsova (langste vrouwenwedstrijd op een grandslam)", "Australian Open 2011", "4 uur en 44 minuten"),
])}
<p>Isner en Mahut speelden alleen al in de vijfde set 8 uur en 11 minuten, goed voor 183 games in totaal. In de wedstrijd van Nelson en Hepner zat de langste rally ooit: 643 slagen in 29 minuten, in één punt van de tiebreak.</p>
<p><strong>Langste finales per grandslam (mannen)</strong></p>
{tabel(["Grandslam", "Finale", "Duur"], [
    ("Australian Open", "Djokovic – Nadal (2012)", "5u53"),
    ("Roland Garros", "Alcaraz – Sinner (2025)", "5u29"),
    ("Wimbledon", "Djokovic – Federer (2019)", "4u57"),
    ("US Open", "Wilander – Lendl (1988) en Murray – Djokovic (2012)", "4u54"),
])}
<p>Ook 2026 leverde lange wedstrijden op: Carlos Alcaraz en Alexander Zverev speelden op de Australian Open de langste halve finale in de geschiedenis van het toernooi (5u27), en Novak Djokovic won op Wimbledon de langste kwartfinale ooit van Félix Auger-Aliassime (5u15), vlak voor de avondklok.</p>
<h3><strong>De kortste tenniswedstrijden</strong></h3>
{tabel(["Wedstrijd", "Toernooi", "Duur"], [
    ("Steffi Graf – Natasha Zvereva, 6-0 6-0 (kortste grandslamfinale)", "Roland Garros 1988", "32 minuten speeltijd"),
    ("Jarkko Nieminen – Bernard Tomic, 6-0 6-1 (kortste ATP-wedstrijd)", "Miami 2014", "28 minuten"),
    ("Alex de Minaur – Grigor Dimitrov, 6-0 6-0 (kortste ATP-wedstrijd van 2025)", "Monte-Carlo 2025", "45 minuten"),
    ("Iga Świątek – Amanda Anisimova, 6-0 6-0", "Wimbledonfinale 2025", "57 minuten"),
])}
<p><strong>Andere opvallende records</strong></p>
<ul><li><strong>Langste tiebreak (ATP):</strong> 24-22, Reilly Opelka – John Isner in Dallas (2022).</li><li><strong>Langste tiebreak op een grandslam:</strong> 22-20, Anna Blinkova – Elena Rybakina op de Australian Open 2024, goed voor 31 minuten.</li><li><strong>Latste eindtijd op een grandslam:</strong> 04:34 uur 's nachts, Lleyton Hewitt – Marcos Baghdatis op de Australian Open 2008.</li><li><strong>Latste eindtijd op de US Open:</strong> 03:33 uur, Ben Shelton – Carlos Alcaraz in de kwartfinale van 2026.</li></ul>
<h3><strong>Hoelang duurt een grandslamfinale?</strong></h3>
<p>Wij rekenden de finales van 2022 tot en met 2026 door. Een grandslamfinale bij de mannen duurde in die periode gemiddeld 3 uur en 28 minuten (de kortste 2u17, de langste 5u29). Bij de vrouwen was dat gemiddeld 1 uur en 49 minuten (de kortste 57 minuten, de langste 2u46). De grandslamfinales van dit jaar:</p>
{tabel(["Grandslam 2026", "Mannen", "Vrouwen"], [
    ("Australian Open", "Alcaraz – Djokovic, 2-6 6-2 6-3 7-5 (± 3 uur)", "Rybakina – Sabalenka, 6-4 4-6 6-4 (2u18)"),
    ("Roland Garros", "Zverev – Cobolli, 6-1 4-6 6-4 6-7 6-1 (4u16)", "Andreeva – Chwalińska, 6-3 6-2 (± 1u20)"),
    ("Wimbledon", "Sinner – Zverev, 6-7 7-6 6-3 6-4 (3u46)", "Nosková – Muchová, 6-2 5-7 6-3 (± 2 uur)"),
    ("US Open", "Zverev – Shelton, 6-3 7-6 5-7 6-2", "Rybakina – Sabalenka, 6-4 5-7 6-2 (2u21)"),
])}
<h3><strong>Hoeveel tijd moet je reserveren als je live kijkt?</strong></h3>
<ul><li><strong>Gewone ATP- of WTA-wedstrijd:</strong> reken op 1,5 tot 2 uur, met uitloop tot 3 uur bij een driesetter met tiebreaks.</li><li><strong>Grandslamwedstrijd bij de mannen:</strong> reken op 3 uur. Wordt het een vijfsetter, dan ben je 4 tot 6 uur verder.</li><li><strong>Grandslamwedstrijd bij de vrouwen:</strong> rond de 1u45.</li><li><strong>Grandslamfinale:</strong> bij de mannen gemiddeld 3,5 uur, bij de vrouwen bijna 2 uur.</li></ul>
<p>Let op met aanvangstijden: alleen de eerste wedstrijd op een baan heeft een vaste starttijd. Wedstrijden daarna staan als "niet voor" of "na de vorige" op het schema. Op de US Open begint de daysession om 11:00 uur lokale tijd en de nightsession niet voor 19:00 uur, op de Australian Open om 11:00 en 19:00 uur. Op Wimbledon begint Centre Court om 13:30 uur, op Roland Garros is er één nightsession-wedstrijd om 20:15 uur. Loopt een eerdere wedstrijd uit, dan schuift alles op. Zo eindigde de kwartfinale tussen Shelton en Alcaraz op de US Open 2026 pas om 03:33 uur 's nachts.</p>
<h3><strong>Wedstrijdduur en wedden op tennis</strong></h3>
<p>Hoe lang een wedstrijd duurt, hangt nauw samen met een aantal populaire wedmarkten: het totaal aantal games (over/under), het aantal sets, de exacte setstand en of er een tiebreak in de wedstrijd komt. Op gravel worden gemiddeld meer games en sets gespeeld dan op gras, en twee sterke serveerders spelen vaker tiebreaks. Ook een game-handicap, een vorm van <a href="/kennisbank/wat-is-handicap-wedden-welke-soorten-handicap-wedden-opties-zijn-er-in-nederland">handicap wedden</a>, hangt hiermee samen.</p>
<p>Wat gebeurt er met je weddenschap als een speler opgeeft of de wedstrijd wordt onderbroken? Dat verschilt per bookmaker. Bij de ene blijft de weddenschap staan zodra de eerste set is uitgespeeld, bij de andere moet de wedstrijd helemaal worden afgemaakt, en een enkele hanteert de regel dat de speler die doorgaat wint zodra er geserveerd is. Bij een walkover (opgave vóór de eerste bal) vervallen weddenschappen meestal en krijg je je inzet terug. Check daarom altijd de voorwaarden van je bookmaker. Waar je legaal op tennis kunt wedden, lees je in ons overzicht van <a href="/de-beste-websites-om-te-wedden-op-tennis-in-nederland-legaal-veilig-gokken-in-nederland">de beste websites om te wedden op tennis</a>, en onze dagelijkse tips vind je bij de <a href="/tennis-voorspellingen-vandaag">tennis voorspellingen van vandaag</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoelang duurt een tenniswedstrijd gemiddeld?</strong><br>Een gewone profwedstrijd over twee gewonnen sets duurt gemiddeld 1,5 tot 2 uur. Het gemiddelde van alle profwedstrijden lag in 2024 op 120 minuten.</p>
<p><strong>Hoelang duurt een vijfsetter?</strong><br>Een grandslamwedstrijd over best of five duurt bij de mannen gemiddeld bijna 3 uur. Gaat het echt de volle vijf sets, dan duurt een wedstrijd meestal 4 tot 6 uur.</p>
<p><strong>Hoelang duurt een set tennis?</strong><br>Gemiddeld 40 tot 45 minuten. Een set van 6-0 kan in 20 minuten klaar zijn, een set met een lange tiebreak duurt soms meer dan een uur.</p>
<p><strong>Wat is de langste tenniswedstrijd ooit?</strong><br>John Isner tegen Nicolas Mahut op Wimbledon 2010: 11 uur en 5 minuten, verspreid over drie dagen. De vijfde set eindigde in 70-68.</p>
<p><strong>Kan een tenniswedstrijd nog zo lang duren als Isner–Mahut?</strong><br>Vrijwel niet. Sinds 2022 spelen alle grandslams bij 6-6 in de beslissende set een tiebreak tot 10 punten.</p>
<p><strong>Waarom duren vrouwenwedstrijden op grandslams korter?</strong><br>Omdat vrouwen ook op de grandslams best of three spelen, terwijl de mannen best of five spelen. Een grandslamwedstrijd bij de vrouwen duurt gemiddeld rond de 1u45.</p>
<p><strong>Hoelang is de pauze tussen sets in tennis?</strong><br>Maximaal 120 seconden. Bij het wisselen van kant na een oneven game mogen spelers 90 seconden pauzeren, tussen twee punten maximaal 25 seconden.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_TENNIS, "tennis": True,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        import re
        tekst = re.sub(r"<[^>]+>", " ", content + content2 + content3)
        print(len(SAMENVATTING), "tekens samenvatting |", len(tekst.split()), "woorden"); sys.exit()
    print("item:", WF.create_live(fd))
