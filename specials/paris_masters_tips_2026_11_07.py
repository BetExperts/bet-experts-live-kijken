# -*- coding: utf-8 -*-
"""Los artikel: Paris Masters 2026 voorspellingen en wedtips voor de halve finales van zaterdag 7 november (dag 6).
Vrijdag 2/4 raak (Van Assche wint, Fritz – Alcaraz 34 games; Paul +1,5 en Borges min. 1 set fout).
Odds 711 (Kambi sevelevnl, zaterdag 7-11 ±10:20).
Feiten: specials/paris_dag6_feiten.md (officiële toernooi-API + officiële artikelen, ATP/TM/AP/Perfect Tennis/We Love Tennis;
H2H tennismylife). Onzeker en daarom vaag of niet genoemd: welk lichaamsdeel Ruud liet behandelen (alleen 'fysio'),
aces Shelton (19/20), winners/UE-cijfers, live-rankings, eindtijden vrijdag, definitieve tijd finale.
  python3 specials/paris_masters_tips_2026_11_07.py           (dry run)
  publiceren: specials/concept_publiceer.py paris_masters_tips_2026_11_07 --live; daarna --velden"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "paris-masters-2026-voorspellingen-wedtips-halve-finales-7-november"
RUBRIEK = "665715dbf1f3cbdf7f874d79"   # Tennis
BOOKMAKER_711 = "66a8a87062108480763b7309"
TITEL = "Paris Masters voorspellingen halve finales (7 november)"
SAMENVATTING = ("Paris Masters voorspellingen voor de halve finales van zaterdag 7 november: Shelton te sterk voor "
                "Van Assche en Alcaraz wint ruim van Ruud.")
ODDS = [1.49, 1.52]
COMBI = "2,26"

OG_LOGO = "paris-masters-logo.png"
OG_EYEBROW = "Tennis · zaterdag 7 november"
OG_KOP = "Paris Masters<br><em>halve finales</em>"
OG_TEGELS = [("Gisteren", "2/4"), ("Combi-odd", COMBI)]
OG_KOPJE = "Onze tips (Nederlandse tijd)"
OG_RECHTS = "Odds bij 711"
OG_RIJEN = [("14:30", "Shelton -2,5 games tegen Van Assche", "1,49"),
            ("17:00", "Alcaraz -3,5 games tegen Ruud", "1,52"),
            ("14:30", "Extra: tiebreak bij Van Assche – Shelton", "1,79")]

L = {"hub": '<a href="/nieuws/paris-masters-2026-schema-tijden-tv-deelnemers-prijzengeld">Paris Masters 2026: schema, deelnemers en prijzengeld</a>',
     "kijk": '<a href="/nieuws/atp-1000-parijs-live-gratis-kijken-in-nederland-tv-gids-ziggo-sport-en-gratis-opties-griekspoor-alcaraz-sinner-en-meer-in-actie">Paris Masters 2026 live kijken</a>',
     "gisteren": '<a href="/nieuws/paris-masters-2026-voorspellingen-wedtips-vrijdag-6-november">onze tips van vrijdag</a>',
     "wiewint": '<a href="/nieuws/wie-wint-paris-masters-2026-favorieten-odds-voorspelling">wie wint de Paris Masters 2026?</a>',
     "finale": '<a href="/nieuws/finale-paris-masters-2026-wanneer-hoe-laat-tv">de finale van de Paris Masters 2026</a>',
     "tips": '<a href="/tennis-voorspellingen-vandaag">tennis voorspellingen vandaag</a>',
     "ziggo": '<a href="/zenders/ziggo-sport">Ziggo Sport</a>',
     "turijn": '<a href="/nieuws/atp-finals-2026-gekwalificeerd-race-to-turin">ATP Finals 2026: wie zijn er gekwalificeerd?</a>',
     "handicap": '<a href="/nieuws/wat-is-handicap-wedden-de-complete-gids">hoe handicap wedden werkt</a>',
     "711": '<a href="/bookmakers/711">711</a>',
     "legaal": '<a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>'}


def waarom(punten):
    return "<p><strong>Waarom deze tip?</strong></p><ul>" + "".join(f"<li>{p}</li>" for p in punten) + "</ul>"


def markt(m):
    return f"<p><strong>De markt:</strong> {m}</p>"


TIPS = [("Van Assche – Shelton", "Court Central, niet voor 14:30 uur", "Shelton -2,5 games", "Game handicap", "1,49"),
        ("Ruud – Alcaraz", "Court Central, niet voor 17:00 uur", "Alcaraz -3,5 games", "Game handicap", "1,52")]

EXTRA = [("Van Assche – Shelton", "Court Central, niet voor 14:30 uur", "Extra: minstens één tiebreak", "Totaal aantal tiebreaks", "1,79")]

GISTEREN = [("Shelton – Paul", "Paul +1,5 games", "6-4, 4-6, 6-3 (16-13 in games)", "❌"),
            ("Van Assche – Hijikata", "Van Assche wint", "6-4, 6-7, 7-5", "✅"),
            ("Alcaraz – Fritz", "Meer dan 20,5 games", "6-7, 7-5, 6-3 (34 games)", "✅"),
            ("Ruud – Borges", "Borges wint minstens één set", "7-6, 6-4", "❌")]

SCHEMA = [("12:00", "Dubbelspel: Miedler/Oberleitner – Harrison/Skupski (2)"),
          ("niet voor 14:30", "<strong>Luca Van Assche – Ben Shelton (3)</strong>"),
          ("niet voor 17:00", "<strong>Casper Ruud – Carlos Alcaraz (2)</strong>"),
          ("daarna", "Dubbelspel: Heliövaara/Patten (1) – Halys/Herbert")]

content = f"""<p><strong>Onze Paris Masters voorspellingen voor de halve finales van zaterdag 7 november: Ben Shelton wint met minstens drie games verschil van Luca Van Assche (Shelton -2,5 games, 1,49) en Carlos Alcaraz wint met minstens vier games verschil van Casper Ruud (Alcaraz -3,5 games, 1,52). Gecombineerd is dat een odd van ongeveer {COMBI} bij 711. Als losse extra tip kiezen we minstens één tiebreak bij Van Assche – Shelton (1,79).</strong></p>
<p>Zaterdag worden beide halve finales op de Court Central in de Paris La Défense Arena gespeeld, de eerste niet voor 14:30 uur. Parijs ligt in dezelfde tijdzone als Nederland. Er komt hoe dan ook een nieuwe kampioen: geen van de vier halvefinalisten won het toernooi eerder, en alle vier spelen ze hun eerste halve finale in Parijs. Van de acht hoogste reekshoofden zijn alleen Alcaraz (2) en Shelton (3) over. De baan blijft snel: 23 van de 49 partijen in het hoofdtoernooi hadden minstens één tiebreak. Alles over het toernooi lees je in {L['hub']}.</p>
<h3><strong>Vrijdag: 2 van de 4 tips raak</strong></h3>
{tabel(["Wedstrijd", "Onze tip", "Uitslag", ""], GISTEREN)}
<p>Van Assche won in bijna drie uur van Rinky Hijikata en Alcaraz – Fritz werd met 34 games een lange partij. Paul verloor van Shelton met drie games verschil, één te veel voor de handicap. De Borges-tip ging nipt mis: in de eerste set won hij meer punten dan Ruud (40 tegen 38), maar Ruud pakte de tiebreak. Teruglezen kan in {L['gisteren']}. Een tip blijft een inschatting.</p>
<h3><strong>Paris Masters voorspellingen halve finales in het kort</strong></h3>
{tabel(["Wedstrijd", "Baan en tijd", "Tip", "Markt", "Odd"], [(f"<strong>{w}</strong>", t, tip, m, f"<strong>{o}</strong>") for w, t, tip, m, o in TIPS] + [("<strong>Combinatie</strong>", "", "Beide tips", "", f"<strong>{COMBI}</strong>")] + [(f"<strong>{w}</strong>", t, tip, m, f"<strong>{o}</strong>") for w, t, tip, m, o in EXTRA])}
<p><em>Odds bij {L['711']}, zaterdagochtend 7 november rond 10:20 uur. Odds kunnen tot de start nog veranderen. De tips staan los van elkaar; de extra tip staat niet in de combinatie.</em></p>
<h3><strong>Het speelschema van zaterdag (Court Central)</strong></h3>
{tabel(["Tijd", "Partij"], SCHEMA)}
<p>De finale is op zondag 8 november, volgens het voorlopige schema om 15:00 uur. {L['ziggo']} zendt de Paris Masters uit; hoe je gratis kunt kijken, lees je in {L['kijk']}.</p>"""

content2 = f"""<h3><strong>Luca Van Assche – Ben Shelton (Court Central, niet voor 14:30 uur)</strong></h3>
<p>Shelton (nummer 4 van de wereld) staat dit jaar op 44 zeges en 18 nederlagen en won vier titels. Het is zijn derde halve finale op een Masters 1000-toernooi; de vorige twee keer, in Toronto 2025 en Montreal 2026, won hij ook de titel. Hij is de eerste Amerikaan in de halve finale van Parijs sinds Jack Sock in 2017. Vrijdag versloeg hij Tommy Paul in drie sets met 19 aces, en hij kreeg tegen Paul en ook tegen Arthur Rinderknech telkens maar één breekpunt tegen. Hij stond deze week vijf uur op de baan en was vrijdag al halverwege de middag klaar.</p>
<p>Van Assche (nummer 47) is de grote man van het toernooi. Na Richard Gasquet in 2007 is hij de jongste Fransman in een halve finale in Parijs, en het is zijn eerste halve finale op een Masters 1000-toernooi. Maar de week eist zijn tol. Hij stond al ruim negen uur op de baan, bijna twee keer zo lang als Shelton, en speelt vandaag zijn vijfde partij in zes dagen. Na zijn zege op Hijikata zei hij zelf dat hij 'een beetje moe' was en dat hij vooral bezig is met herstellen. Een blessure is niet gemeld. Tegen spelers uit de top 10 verloor hij alle vijf zijn partijen, en tegen linkshandigen zoals Shelton staat hij op 8 zeges en 9 nederlagen. Ze speelden nog nooit tegen elkaar.</p>
<p><strong>Onze tip: Shelton -2,5 games (1,49).</strong></p>
{markt("game handicap. Shelton krijgt 2,5 games achterstand. De tip is goed als Shelton wint met minstens drie games verschil, zoals bij 6-4, 7-6 (13-10) of 6-3, 6-4. Wint Shelton met 7-6, 7-6 (14-12), dan is het verschil maar twee games en is de tip verloren. Wint Van Assche, dan ook. Meer uitleg lees je in " + L['handicap'] + ".")}
{waarom(["<strong>Fris tegen moe.</strong> Shelton stond deze week vier uur korter op de baan, en Van Assche gaf zelf aan dat hij vermoeid is.",
         "<strong>Shelton serveert op deze baan bijna onbreekbaar.</strong> Op een snelle baan, waar Van Assche zelf zegt dat de omstandigheden Shelton goed liggen, krijgt de Fransman weinig kansen op een break."])}
<p><strong>Het risico:</strong> Van Assche heeft 17.500 Franse fans achter zich en vecht zich telkens terug. Gaan beide sets naar een tiebreak, dan kan Shelton winnen en toch de handicap missen. Liever op de winnaar? Shelton wint staat op 1,28; met -1,5 games krijg je 1,35.</p>
<p><strong>Extra tip: minstens één tiebreak (1,79).</strong> {"Op deze baan had bijna de helft van de partijen een tiebreak, vrijdag zelfs drie van de vier. Shelton houdt zijn opslag bijna altijd en Van Assche sloeg vrijdag 13 aces. De tip is goed zodra één set in een tiebreak eindigt, wie de partij ook wint. Deze tip staat los van de combinatie."}</p>
<h3><strong>Casper Ruud – Carlos Alcaraz (Court Central, niet voor 17:00 uur)</strong></h3>
<p>Alcaraz (nummer 3) staat dit jaar op 40 zeges en 5 nederlagen en won vier titels, als laatste vorige week in Wenen. In Parijs kwam hij nooit verder dan de kwartfinale, maar vrijdag redde hij tegen Taylor Fritz twee matchpunten en won hij de laatste set overtuigend met 6-3. Hij sprak na afloop over zenuwen, niet over zijn lichaam. Onderling leidt hij met 6-1, en op hardcourt met 5-1. Hun laatste duel, in maart op Indian Wells, won hij met 6-1, 7-6. Ruuds enige zege dateert van de ATP Finals 2024.</p>
<p>Ruud (nummer 23) gaf deze week nog geen set af en werd in vier partijen maar één keer gebroken. Hij speelt zijn elfde halve finale op een Masters 1000-toernooi en zijn eerste in Parijs. Wel zijn er twee punten om op te letten. Volgens het officiële verslag kreeg Ruud aan het eind van zijn partij tegen Nuno Borges behandeling van de fysio; om welk lichaamsdeel het ging, is niet bekend. Ruud zegt zelf dat hij zich goed voelt. Daarnaast stond hij tot na middernacht op de baan en moet hij niet voor 17:00 uur alweer spelen: een korte nacht.</p>
<p><strong>Onze tip: Alcaraz -3,5 games (1,52).</strong></p>
{markt("game handicap. Alcaraz krijgt 3,5 games achterstand. De tip is goed als Alcaraz wint met minstens vier games verschil, zoals bij 6-4, 6-4 (12-8) of 6-3, 4-6, 6-3. Wint Alcaraz met 7-6, 6-4 (13-10), dan is het verschil drie games en is de tip verloren. Wint Ruud, dan ook.")}
{waarom(["<strong>Alcaraz is beter en frisser.</strong> Hij had een paar uur meer rust, terwijl Ruud na middernacht nog speelde en aan het eind van zijn partij de fysio nodig had.",
         "<strong>Onderling overtuigend.</strong> In vier van zijn zes zeges op Ruud won Alcaraz met vier games of meer verschil, de laatste keer met 13-7 in games."])}
<p><strong>Het risico:</strong> Ruud serveert deze week uitstekend. Houdt hij zijn opslag lang vast en wordt het een tiebreak, dan kan het verschil te klein worden: in Tokio (2025) won Alcaraz maar met twee games verschil. Liever op de winnaar? Alcaraz wint staat op 1,17; Alcaraz in twee sets op 1,56.</p>"""

content3 = f"""<h3><strong>Combinatie zaterdag 7 november</strong></h3>
<p>Beide hoofdtips samen: 1,49 × 1,52 = <strong>± {COMBI}</strong>. Een inzet van €10 levert bij deze combinatie ongeveer €23 op. Beide tips moeten dan goed zijn. Wil je minder risico, speel de tips dan los.</p>
<h3><strong>Wie wint de Paris Masters?</strong></h3>
<p>Wint Alcaraz zaterdag, dan is hij zondag de grote favoriet voor zijn vijfde titel van het jaar. Shelton won zijn vorige twee Masters-finales en is dus ook een geduchte finalist. Voor Turijn speelt het geen rol meer: Alcaraz en Shelton zijn al zeker van de ATP Finals, en Ruud en Van Assche kunnen er niet meer bij. Sinds vrijdag staat het veld vast, met Frances Tiafoe en Rafael Jódar als laatste twee. Meer lees je in {L['turijn']}. Onze voorspelling voor de titel lees je in {L['wiewint']} Alles over de eindstrijd van zondag staat in {L['finale']}.</p>
<h3><strong>Wat betekenen deze weddenschappen?</strong></h3>
<p><strong>Game handicap.</strong> Alle games van de hele partij tellen mee. Bij -2,5 moet een speler minstens drie games meer winnen dan zijn tegenstander, bij -3,5 minstens vier. Een tiebreak telt als één game.</p>
<p><strong>Totaal aantal tiebreaks, meer dan 0,5.</strong> Er moet minstens één set in een tiebreak eindigen (7-6 of 6-7). Wie de tiebreak wint, maakt niet uit.</p>
<p>Geeft een speler op, dan hangt het van de regels van de bookmaker af wat er met je weddenschap gebeurt. Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit; lees {L['legaal']}. Meer tips vind je op onze pagina {L['tips']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wat zijn de beste voorspellingen voor de halve finales van de Paris Masters?</strong><br>Shelton -2,5 games tegen Van Assche (1,49) en Alcaraz -3,5 games tegen Ruud (1,52), samen ongeveer {COMBI}. Losse extra tip: minstens één tiebreak bij Van Assche – Shelton (1,79).</p>
<p><strong>Hoe laat zijn de halve finales van de Paris Masters?</strong><br>Van Assche – Shelton begint niet voor 14:30 uur, Ruud – Alcaraz niet voor 17:00 uur. Beide partijen zijn op de Court Central.</p>
<p><strong>Hoe deden de tennistips van vrijdag het?</strong><br>Twee van de vier waren goed: Van Assche wint en meer dan 20,5 games bij Alcaraz – Fritz. Paul +1,5 games en Borges wint een set gingen mis.</p>
<p><strong>Is Casper Ruud fit?</strong><br>Ruud kreeg vrijdag aan het eind van zijn partij behandeling van de fysio, maar zei zelf dat hij zich goed voelt. Een blessure is niet gemeld.</p>
<p><strong>Wanneer is de finale van de Paris Masters 2026?</strong><br>Op zondag 8 november, volgens het voorlopige schema om 15:00 uur op de Court Central.</p>
<p><strong>Waar kan ik de Paris Masters live kijken?</strong><br>Op Ziggo Sport. Gratis kijken kan ook; hoe, lees je in {L['kijk']}.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

WEDTIPS = {"wedstrijd-1": "Combinatie: beide tips",
           "wedtip-1-2": "Shelton -2.5 games + Alcaraz -3.5 games",
           "quotering-wedtip-1": "2.26",
           "wedstrijd-2": "Van Assche vs Shelton", "wedtip-2-2": "Shelton -2.5 games", "quotering-wedtip-2": "1.49",
           "wedstrijd-3": "Ruud vs Alcaraz", "wedtip-3-2": "Alcaraz -3.5 games", "quotering-wedtip-3": "1.52",
           "wedtip-4-2": "Van Assche vs Shelton minstens één tiebreak", "quotering-wedtip-4": "1.79"}

if __name__ == "__main__":
    import re
    if "--velden" in sys.argv:
        import lk_webflow as WF
        it = WF._req("GET", f"{WF.WF_API}/collections/{WF.NIEUWS_COLLECTION}/items?slug={SLUG}")["items"][0]
        fd = {"tennis": True, "bookmaker-wedtips": BOOKMAKER_711, "datum-tijd-van-wedstrijd": "2026-11-07T13:30:00.000Z", **WEDTIPS}
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
    assert round(10 * p) == 23
    assert [t[4] for t in TIPS] == ["1,49", "1,52"]
    assert 13 - 10 >= 3 and 14 - 12 < 3 and 12 - 8 >= 4 and 13 - 10 < 4 and 6 + 4 + 6 == 16 and 13 + 12 + 9 == 34
    assert alles.count("<p><strong>De markt:</strong>") == 2
    assert "<h2" not in alles and "<h4" not in alles and "betcity" not in alles.lower() and "/go/" not in alles
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    print("dry run ok")
