# -*- coding: utf-8 -*-
"""Los artikel: Paris Masters 2026 voorspellingen en wedtips voor vrijdag 6 november (dag 5: kwartfinales).
Donderdag 5/5 raak (Paul -2,5 games 13-10, Shelton-Rinderknech tiebreak in set 3, Van Assche-Musetti 31 games,
Etcheverry +1,5 (14-15), Fritz +2,5 (wint)).
Odds 711 (Kambi sevelevnl, vrijdag 6-11 ±10:10, ongewijzigd sinds ±08:30).
Feiten: specials/paris_dag5_feiten.md (officiële toernooi-API + ATP/TM/ABC/Yahoo AU/Maisfutebol; H2H tennismylife).
Onzeker en daarom vaag of niet genoemd: reden van Hijikata's twijfel woensdag (nek alleen indirect), live-rankings,
14 of 15 aces Fritz, exacte aanvang Van Assche – Hijikata (alleen 'daarna').
  python3 specials/paris_masters_tips_2026_11_06.py           (dry run)
  publiceren: specials/concept_publiceer.py paris_masters_tips_2026_11_06 --live; daarna --velden"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "paris-masters-2026-voorspellingen-wedtips-vrijdag-6-november"
RUBRIEK = "665715dbf1f3cbdf7f874d79"   # Tennis
BOOKMAKER_711 = "66a8a87062108480763b7309"
TITEL = "Paris Masters voorspellingen vandaag: 4 tips (6 november)"
SAMENVATTING = ("Paris Masters voorspellingen voor de kwartfinales van vrijdag 6 november: Paul houdt het spannend, "
                "Van Assche wint en Fritz – Alcaraz wordt lang.")
ODDS = [1.52, 1.61, 1.42]
COMBI = "3,48"

OG_LOGO = "paris-masters-logo.png"
OG_EYEBROW = "Tennis · vrijdag 6 november"
OG_KOP = "Paris Masters<br><em>kwartfinales</em>"
OG_TEGELS = [("Gisteren", "5/5"), ("Combi-odd", COMBI)]
OG_KOPJE = "Onze tips (Nederlandse tijd)"
OG_RECHTS = "Odds bij 711"
OG_RIJEN = [("14:00", "Paul +1,5 games tegen Shelton", "1,52"),
            ("± 15:30", "Van Assche wint van Hijikata", "1,61"),
            ("19:00", "Fritz – Alcaraz: 21+ games", "1,42"),
            ("20:30", "Extra: Borges wint min. 1 set", "1,68")]

L = {"hub": '<a href="/nieuws/paris-masters-2026-schema-tijden-tv-deelnemers-prijzengeld">Paris Masters 2026: schema, deelnemers en prijzengeld</a>',
     "kijk": '<a href="/nieuws/atp-1000-parijs-live-gratis-kijken-in-nederland-tv-gids-ziggo-sport-en-gratis-opties-griekspoor-alcaraz-sinner-en-meer-in-actie">Paris Masters 2026 live kijken</a>',
     "gisteren": '<a href="/nieuws/paris-masters-2026-voorspellingen-wedtips-donderdag-5-november">onze tips van donderdag</a>',
     "wiewint": '<a href="/nieuws/wie-wint-paris-masters-2026-favorieten-odds-voorspelling">wie wint de Paris Masters 2026?</a>',
     "finale": '<a href="/nieuws/finale-paris-masters-2026-wanneer-hoe-laat-tv">de finale van de Paris Masters 2026</a>',
     "tips": '<a href="/tennis-voorspellingen-vandaag">tennis voorspellingen vandaag</a>',
     "ziggo": '<a href="/zenders/ziggo-sport">Ziggo Sport</a>',
     "turijn": '<a href="/nieuws/atp-finals-2026-gekwalificeerd-race-to-turin">ATP Finals 2026: wie zijn er al gekwalificeerd?</a>',
     "handicap": '<a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">hoe handicap wedden werkt</a>',
     "711": '<a href="/bookmakers/711">711</a>',
     "legaal": '<a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>'}


def waarom(punten):
    return "<p><strong>Waarom deze tip?</strong></p><ul>" + "".join(f"<li>{p}</li>" for p in punten) + "</ul>"


def markt(m):
    return f"<p><strong>De markt:</strong> {m}</p>"


TIPS = [("Shelton – Paul", "Centercourt, 14:00 uur", "Paul +1,5 games", "Game handicap", "1,52"),
        ("Van Assche – Hijikata", "Centercourt, tweede partij (± 15:30 uur)", "Van Assche wint", "Winnaar", "1,61"),
        ("Fritz – Alcaraz", "Centercourt, niet voor 19:00 uur", "Meer dan 20,5 games", "Totaal aantal games", "1,42")]

EXTRA = [("Ruud – Borges", "Centercourt, niet voor 20:30 uur", "Extra: Borges wint minstens één set", "Set handicap", "1,68")]

GISTEREN = [("Paul – Halys", "Paul -2,5 games", "7-6, 6-4 (13-10 in games)", "✅"),
            ("Shelton – Rinderknech", "Minstens één tiebreak", "3-6, 6-4, 7-6", "✅"),
            ("Musetti – Van Assche", "Meer dan 21,5 games", "5-7, 6-3, 4-6 (31 games)", "✅"),
            ("Hijikata – Etcheverry", "Etcheverry +1,5 games", "6-2, 3-6, 5-7 (14-15)", "✅"),
            ("Fils – Fritz", "Fritz +2,5 games", "3-6, 4-6: Fritz wint", "✅")]

SCHEMA = [("<strong>Centercourt</strong>", "14:00", "Ben Shelton (3) – Tommy Paul (12)"),
          ("<strong>Centercourt</strong>", "daarna", "Luca Van Assche – Rinky Hijikata (Q)"),
          ("<strong>Centercourt</strong>", "niet voor 19:00", "Taylor Fritz (11) – Carlos Alcaraz (2)"),
          ("<strong>Centercourt</strong>", "niet voor 20:30", "Casper Ruud – Nuno Borges (LL)")]

content = f"""<p><strong>Onze Paris Masters voorspellingen voor de kwartfinales van vrijdag 6 november: Tommy Paul +1,5 games tegen Ben Shelton (1,52), Luca Van Assche wint van Rinky Hijikata (1,61) en Taylor Fritz – Carlos Alcaraz duurt meer dan 20,5 games (1,42). De odds zijn van 711; gecombineerd is dat een odd van ongeveer {COMBI}. Als losse extra tip kiezen we Nuno Borges wint minstens één set tegen Casper Ruud (1,68). Donderdag zaten alle vijf onze tips goed.</strong></p>
<p>De Paris Masters in de Paris La Défense Arena is toe aan de kwartfinales. Alle vier de partijen worden op de centercourt gespeeld, vanaf 14:00 uur. Het toernooi zit vol verrassingen: van de acht hoogste reekshoofden zijn alleen Alcaraz en Shelton nog over, en met Van Assche, Hijikata en Borges spelen drie mannen hun eerste kwartfinale op een Masters-toernooi. De baan is snel: 44 procent van de partijen in het hoofdtoernooi had minstens één tiebreak, met gemiddeld bijna 24 games per partij. Parijs ligt in dezelfde tijdzone als Nederland. Alles over het toernooi lees je in {L['hub']}.</p>
<h3><strong>Donderdag: alle 5 de tips raak</strong></h3>
{tabel(["Wedstrijd", "Onze tip", "Uitslag", ""], GISTEREN)}
<p>Paul won met precies drie games verschil, net genoeg voor de handicap. Shelton en Rinderknech hadden een beslissende tiebreak nodig, Van Assche versloeg Musetti in drie sets en Etcheverry verloor maar met één game verschil. Fritz won in de avond zelfs overtuigend van Arthur Fils. De combinatie (± 3,92) viel daarmee ook. Teruglezen kan in {L['gisteren']}. Een tip blijft een inschatting; vandaag kan het anders lopen.</p>
<h3><strong>Paris Masters voorspellingen vandaag in het kort</strong></h3>
{tabel(["Wedstrijd", "Baan en tijd", "Tip", "Markt", "Odd"], [(f"<strong>{w}</strong>", t, tip, m, f"<strong>{o}</strong>") for w, t, tip, m, o in TIPS] + [("<strong>Combinatie</strong>", "", "Alle drie de tips", "", f"<strong>{COMBI}</strong>")] + [(f"<strong>{w}</strong>", t, tip, m, f"<strong>{o}</strong>") for w, t, tip, m, o in EXTRA])}
<p><em>Odds bij {L['711']}, vrijdagochtend 6 november rond 10:00 uur. Odds en aanvangstijden kunnen nog veranderen; de tijd van de tweede partij is een schatting, omdat de partijen na elkaar op dezelfde baan worden gespeeld. De tips staan los van elkaar: je kunt ze apart spelen of combineren. De extra tip staat niet in de combinatie.</em></p>
<h3><strong>Het speelschema van vrijdag</strong></h3>
{tabel(["Baan", "Tijd", "Partij"], SCHEMA)}
<p>Alcaraz plaatste zich zonder te spelen: Matteo Berrettini trok zich donderdag terug met een elleboogblessure. {L['ziggo']} zendt de Paris Masters uit; hoe je gratis kunt kijken, lees je in {L['kijk']}.</p>"""

content2 = f"""<h3><strong>Ben Shelton – Tommy Paul (centercourt, 14:00 uur)</strong></h3>
<p>Shelton (nummer 4) beleeft met 43 zeges zijn beste seizoen ooit en is al zeker van Turijn. Donderdag had hij wel drie sets en een beslissende tiebreak nodig tegen Arthur Rinderknech; in die tiebreak stond hij nog 2-4 achter. Paul (nummer 14) gaf in Parijs nog geen set af en werd maar één keer gebroken. Donderdag verloor hij maar 2 van de 45 punten op zijn eerste service. Hij moet winnen om nog kans te houden op Turijn. Onderling staat het 2-2; Paul won hun laatste duel, indoor in Dallas.</p>
<p><strong>Onze tip: Paul +1,5 games (1,52).</strong></p>
{markt("game handicap. Paul krijgt 1,5 games voorsprong. De tip is goed als Paul wint, en ook als hij verliest met maar één game verschil, zoals bij 7-6, 6-7, 6-7. Verliest Paul met twee games of meer verschil, bijvoorbeeld 6-7, 6-7 of 4-6, 6-4, 4-6, dan is de tip verloren. Meer uitleg lees je in " + L['handicap'] + ".")}
{waarom(["<strong>De bookmaker ziet Paul als favoriet.</strong> Op de winnaar staat hij op 1,73, Shelton op 2,10. Met de handicap mag Paul zelfs nipt verliezen.",
         "<strong>Paul is fris en in vorm.</strong> Drie partijen in twee sets, en woensdag stond hij nog geen uur op de baan."])}
<p><strong>Het risico:</strong> Shelton sloeg donderdag 16 aces en kan met zijn opslag elke set in een tiebreak trekken. Twee verloren tiebreaks (6-7, 6-7) en de tip is weg. Wil je meer zekerheid? Paul +2,5 games staat op 1,38.</p>
<h3><strong>Luca Van Assche – Rinky Hijikata (centercourt, ± 15:30 uur)</strong></h3>
<p>Van Assche (nummer 47) is de laatste Fransman in het enkelspel en won deze week van Mariano Navone, Learner Tien en Lorenzo Musetti. Hij heeft het publiek volledig mee. Hij stond wel het langst op de baan van alle kwartfinalisten (6,5 uur), maar zegt zelf dat hij fysiek geen probleem heeft. Kwalificant Hijikata versloeg Novak Djokovic en Tomás Martín Etcheverry, beide keren na een set achterstand. Na donderdag zei hij dat hij 'een beetje weinig energie' had. Vrijdag speelt hij zijn zesde partij in zeven dagen, en woensdag wist hij 's ochtends nog niet of hij kon spelen. Ze speelden nog nooit tegen elkaar.</p>
<p><strong>Onze tip: Van Assche wint (1,61).</strong></p>
{markt("winnaar van de partij. De tip is goed als Van Assche wint, ongeacht de score.")}
{waarom(["<strong>Twijfels over Hijikata's fitheid.</strong> Hij gaf zelf aan dat zijn energie laag was, en het toernooi duurt voor hem al een week.",
         "<strong>Thuisvoordeel.</strong> Van Assche had het publiek de hele week achter zich; Hijikata werd donderdag uitgefloten."])}
<p><strong>Het risico:</strong> Hijikata vecht zich telkens terug en speelt goed op een snelle baan. Ook Van Assche is niet fris na drie lange partijen. Wil je meer zekerheid? Van Assche +1,5 games staat op 1,45.</p>
<h3><strong>Taylor Fritz – Carlos Alcaraz (centercourt, niet voor 19:00 uur)</strong></h3>
<p>Alcaraz (nummer 3) staat dit jaar op 39 zeges en 5 nederlagen en leidt onderling met 6-1. Hij speelde deze week maar één partij, tegen Alex Michelsen, en is dus uitgerust. Wel komt hij in Parijs nooit verder dan de kwartfinale. Fritz (nummer 12) heeft dit jaar 13 indoorzeges, het meeste van iedereen op de tour. Hij sloeg deze week 73 aces in drie partijen en kreeg tegen Arthur Fils geen enkel breekpunt tegen. Hij moet winnen om nog naar Turijn te kunnen. Volgens hemzelf voelt hij zich gezond en gemotiveerd, al speelt hij wel voor de vierde dag op rij.</p>
<p><strong>Onze tip: meer dan 20,5 games (1,42).</strong></p>
{markt("totaal aantal games, meer dan 20,5. Alle games van beide spelers tellen mee, een tiebreak telt als één game. De tip is goed vanaf 21 games, bijvoorbeeld bij 7-5, 6-4 of bij elke driesetter. Bij 6-4, 6-4 (20 games) is de tip verloren. Wie er wint, maakt niet uit.")}
{waarom(["<strong>Fritz serveert te goed voor een snelle partij.</strong> Op deze snelle baan houdt hij zijn opslag vaak, waardoor sets lang duren.",
         "<strong>Lange duels.</strong> Hun laatste indoorduel, op de ATP Finals van 2025, telde 34 games. Fritz moet winnen en zal tot de laatste bal vechten."])}
<p><strong>Het risico:</strong> Alcaraz retourneert als de beste. Breekt hij in elke set vroeg, dan kan het een 6-4, 6-4 of 6-3, 6-4 worden. Liever op de winnaar? Alcaraz wint staat op 1,35.</p>"""

content3 = f"""<h3><strong>Casper Ruud – Nuno Borges (centercourt, niet voor 20:30 uur)</strong></h3>
<p>Ruud gaf deze week nog geen set af en kreeg in drie partijen maar drie breekpunten tegen. Borges kwam als lucky loser in het hoofdtoernooi en is de eerste lucky loser ooit in de kwartfinale van Parijs. In het hoofdtoernooi werd hij nog niet gebroken. Het is een herhaling van Bazel, negen dagen geleden: daar won Borges met 1-6, 6-3, 6-4. Onderling staat het 2-2.</p>
<p><strong>Extra tip: Borges wint minstens één set (1,68).</strong></p>
{markt("set handicap. De tip is goed als Borges minstens één set wint, ook als hij de partij verliest. Wint Ruud in twee sets, dan is de tip verloren.")}
{waarom(["<strong>Borges weet hoe hij Ruud moet kloppen.</strong> Hij won twee van hun vier duels, waaronder dat van vorige week, indoor in Bazel.",
         "<strong>Hij serveert sterk.</strong> In drie partijen gaf hij maar twee breekpunten weg en redde hij ze allebei."])}
<p><strong>Het risico:</strong> Ruud is in vorm en hield donderdag al zijn servicegames tegen Jan-Lennard Struff. De tip staat los van de combinatie, omdat hij meer risico heeft.</p>
<h3><strong>Combinatie vrijdag 6 november</strong></h3>
<p>Alle drie de hoofdtips samen: 1,52 × 1,61 × 1,42 = <strong>± {COMBI}</strong>. Een inzet van €10 levert bij deze combinatie ongeveer €35 op. Hoe meer tips in een combinatie, hoe groter de kans dat er één misgaat. Wil je minder risico, speel de tips dan los, of combineer alleen Paul en Van Assche (samen ± 2,45).</p>
<h3><strong>Wie gaat er naar Turijn?</strong></h3>
<p>Voor de ATP Finals zijn nog twee plekken te verdelen. Fritz moet van Alcaraz winnen; haalt hij de finale, dan is hij zeker van Turijn. Paul moet minstens de finale halen. Wint Shelton vandaag, dan is Frances Tiafoe zeker van een plek. Meer lees je in {L['turijn']}. Wie volgens ons de titel pakt, lees je in {L['wiewint']} Alles over de eindstrijd van zondag staat in {L['finale']}.</p>
<h3><strong>Wat betekenen deze weddenschappen?</strong></h3>
<p><strong>Game handicap.</strong> Een speler krijgt een voorsprong in games, opgeteld over de hele partij. Bij +1,5 mag hij verliezen, zolang het verschil maar één game is.</p>
<p><strong>Totaal aantal games, meer dan 20,5.</strong> Alle games van beide spelers samen moeten op 21 of meer uitkomen. Een tiebreak telt als één game.</p>
<p><strong>Minstens één set winnen.</strong> De speler hoeft de partij niet te winnen; één gewonnen set is genoeg.</p>
<p>Geeft een speler op, dan hangt het van de regels van de bookmaker af wat er met je weddenschap gebeurt. Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit; lees {L['legaal']}. Meer tips vind je op onze pagina {L['tips']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wat zijn de beste Paris Masters-voorspellingen van vandaag?</strong><br>Paul +1,5 games tegen Shelton (1,52), Van Assche wint van Hijikata (1,61) en Fritz – Alcaraz duurt meer dan 20,5 games (1,42). Gecombineerd is de odd ongeveer {COMBI}. Losse extra tip: Borges wint minstens één set tegen Ruud (1,68).</p>
<p><strong>Hoe deden de tennistips van gisteren het?</strong><br>Alle vijf waren goed: Paul -2,5 games, de tiebreak bij Shelton – Rinderknech, meer dan 21,5 games bij Musetti – Van Assche, Etcheverry +1,5 games en Fritz +2,5 games.</p>
<p><strong>Hoe laat speelt Alcaraz vandaag?</strong><br>In de avondsessie op de centercourt, niet voor 19:00 uur, tegen Taylor Fritz.</p>
<p><strong>Waarom speelde Alcaraz donderdag niet?</strong><br>Matteo Berrettini trok zich terug met een elleboogblessure. Alcaraz ging daardoor zonder te spelen door naar de kwartfinale.</p>
<p><strong>Wie speelt er in de halve finale tegen wie?</strong><br>De winnaar van Shelton – Paul speelt zaterdag tegen de winnaar van Van Assche – Hijikata. De winnaar van Fritz – Alcaraz speelt tegen de winnaar van Ruud – Borges.</p>
<p><strong>Waar kan ik de Paris Masters live kijken?</strong><br>Op Ziggo Sport. Gratis kijken kan ook; hoe, lees je in {L['kijk']}.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

WEDTIPS = {"wedstrijd-1": "Combinatie: alle drie de tips",
           "wedtip-1-2": "Paul +1.5 games + Van Assche wint + Fritz vs Alcaraz meer dan 20.5 games",
           "quotering-wedtip-1": "3.48",
           "wedstrijd-2": "Shelton vs Paul", "wedtip-2-2": "Paul +1.5 games", "quotering-wedtip-2": "1.52",
           "wedstrijd-3": "Van Assche vs Hijikata", "wedtip-3-2": "Van Assche wint", "quotering-wedtip-3": "1.61",
           "wedtip-4-2": "Fritz vs Alcaraz meer dan 20.5 games", "quotering-wedtip-4": "1.42"}

if __name__ == "__main__":
    import re
    if "--velden" in sys.argv:
        import lk_webflow as WF
        it = WF._req("GET", f"{WF.WF_API}/collections/{WF.NIEUWS_COLLECTION}/items?slug={SLUG}")["items"][0]
        fd = {"tennis": True, "bookmaker-wedtips": BOOKMAKER_711, "datum-tijd-van-wedstrijd": "2026-11-06T13:00:00.000Z", **WEDTIPS}
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
    assert abs(1.52 * 1.61 - 2.45) < 0.01 and round(10 * p) == 35
    assert [t[4] for t in TIPS] == ["1,52", "1,61", "1,42"]
    assert alles.count("<p><strong>De markt:</strong>") == 4
    assert "<h2" not in alles and "<h4" not in alles and "betcity" not in alles.lower() and "/go/" not in alles
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    print("dry run ok")
