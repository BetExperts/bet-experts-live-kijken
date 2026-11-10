# -*- coding: utf-8 -*-
"""Los artikel: Paris Masters 2026 voorspellingen en wedtips voor dinsdag 3 november (dag 2: 1e en 2e ronde). Eigenaar 3-11: 'gisteren 4/4' (Jódar 6-2 6-3, Norrie 6-4 1-6 6-3, Macháč 7-6 6-1, Humbert 6-7 7-6 6-3 = 19-16
games). Odds 711 (Kambi sevelevnl, dinsdag 3-11 ±10:00, nagekeken ±10:05). Partijen van 11:00 bewust overgeslagen.
Feiten: specials/paris_dag2_feiten.md (Tennis Abstract + Univers Tennis/TennisActu/Tennis Majors; atptour.com niet gebruikt).
Onzeker en daarom vaag: banen/volgorde op Court 1 en 2 (alleen media), exacte Race-grens na de afwezigheid van Sinner.
  python3 specials/paris_masters_tips_2026_11_03.py           (dry run)
  publiceren: specials/concept_publiceer.py paris_masters_tips_2026_11_03 --live; daarna --velden"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "paris-masters-2026-voorspellingen-wedtips-dinsdag-3-november"
RUBRIEK = "665715dbf1f3cbdf7f874d79"   # Tennis
BOOKMAKER_711 = "66a8a87062108480763b7309"
TITEL = "Paris Masters voorspellingen vandaag: 4 tips (3 november)"
SAMENVATTING = ("Paris Masters voorspellingen voor dinsdag 3 november: Paul en Jódar winnen, Vacherot pakt een set van "
                "Djokovic en Michelsen +2,5 games.")
ODDS = [1.42, 1.53, 1.63, 1.75]
COMBI = "6,20"

OG_LOGO = "paris-masters-logo.png"
OG_EYEBROW = "Tennis · dinsdag 3 november"
OG_KOP = "Paris Masters<br><em>4 wedtips</em>"
OG_TEGELS = [("Gisteren", "4/4"), ("Combi-odd", COMBI)]
OG_KOPJE = "Onze tips (Nederlandse tijd)"
OG_RECHTS = "Odds bij 711"
OG_RIJEN = [("± 14:00", "Paul wint van Rune", "1,42"),
            ("± 14:00", "Vacherot wint min. 1 set", "1,63"),
            ("na 15:00", "Michelsen +2,5 games", "1,75"),
            ("na 20:30", "Jódar wint van Ruud", "1,53")]

L = {"hub": '<a href="/nieuws/paris-masters-2026-schema-tijden-tv-deelnemers-prijzengeld">Paris Masters 2026: schema, deelnemers en prijzengeld</a>',
     "kijk": '<a href="/nieuws/atp-1000-parijs-live-gratis-kijken-in-nederland-tv-gids-ziggo-sport-en-gratis-opties-griekspoor-alcaraz-sinner-en-meer-in-actie">Paris Masters 2026 live kijken</a>',
     "gisteren": '<a href="/nieuws/paris-masters-2026-voorspellingen-wedtips-maandag-2-november">onze tips van maandag</a>',
     "tips": '<a href="/tennis-voorspellingen-vandaag">tennis voorspellingen vandaag</a>',
     "ziggo": '<a href="/zenders/ziggo-sport">Ziggo Sport</a>',
     "duur": '<a href="/nieuws/hoe-lang-duurt-een-tenniswedstrijd">hoelang duurt een tenniswedstrijd</a>',
     "turijn": '<a href="/nieuws/atp-finals-2026-gekwalificeerd-race-to-turin">ATP Finals 2026: wie zijn er al gekwalificeerd?</a>',
     "711": '<a href="/bookmakers/711">711</a>',
     "legaal": '<a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>'}

HELE = "Geldt voor de hele wedstrijd: alle sets tellen mee, een tiebreak telt als één game."


def waarom(punten):
    return "<p><strong>Waarom deze tip?</strong></p><ul>" + "".join(f"<li>{p}</li>" for p in punten) + "</ul>"


def markt(m):
    return f"<p><strong>De markt:</strong> {m}</p>"


TIPS = [("Paul – Rune", "Court 1, derde partij (± 14:00 uur)", "Paul wint", "Winnaar van de wedstrijd", "1,42"),
        ("Djokovic – Vacherot", "Centercourt, derde partij (± 14:00 uur)", "Vacherot wint minstens één set", "Wint speler minstens één set: ja", "1,63"),
        ("Michelsen – Lehečka", "Court 2, niet voor 15:00 uur", "Michelsen +2,5 games", "Game handicap, hele wedstrijd", "1,75"),
        ("Ruud – Jódar", "Centercourt, niet voor 20:30 uur", "Jódar wint", "Winnaar van de wedstrijd", "1,53")]

GISTEREN = [("Tabilo – Jódar", "Jódar wint in twee sets", "6-2, 6-3 voor Jódar", "✅"),
            ("Norrie – Arnaldi", "Norrie wint", "6-4, 1-6, 6-3 voor Norrie", "✅"),
            ("Jacquet – Macháč", "Macháč wint", "7-6, 6-1 voor Macháč", "✅"),
            ("Humbert – Van de Zandschulp", "Humbert -1,5 games", "6-7, 7-6, 6-3 voor Humbert (19-16 in games)", "✅")]

content = f"""<p><strong>Onze Paris Masters voorspellingen voor dinsdag 3 november: Tommy Paul wint van Holger Rune (1,42), Valentin Vacherot pakt minstens één set van Novak Djokovic (1,63), Alex Michelsen blijft binnen twee games van Jiří Lehečka (+2,5 games, 1,75) en Rafael Jódar wint van Casper Ruud (1,53). De odds zijn van 711; gecombineerd is dat een odd van ongeveer {COMBI}. Gisteren zaten alle vier onze tips goed.</strong></p>
<p>Op dag twee van de Rolex Paris Masters in de Plenitude Arena (de vroegere Paris La Défense Arena) beginnen onder meer Novak Djokovic, Taylor Fritz en Tommy Paul aan het toernooi, en worden de eerste partijen van de tweede ronde gespeeld. Voor een aantal spelers gaat het ook om een plek in de ATP Finals in Turijn. De partijen van 11:00 uur laten we buiten onze tips, zodat je alles nog op tijd kunt spelen. Parijs ligt in dezelfde tijdzone als Nederland. Alles over het toernooi lees je in {L['hub']}.</p>
<h3><strong>Gisteren: 4 van de 4 tips raak</strong></h3>
{tabel(["Wedstrijd", "Onze tip", "Uitslag", ""], GISTEREN)}
<p>De combinatie van gisteren, met een odd van 5,99, viel dus ook goed. De spannendste was de avondpartij: Van de Zandschulp won een sterke tweede set, maar Humbert pakte de derde met 6-3 en won in totaal drie games meer. Teruglezen kan in {L['gisteren']}. Een tip blijft natuurlijk een inschatting; ook vandaag kan het anders lopen.</p>
<h3><strong>Paris Masters voorspellingen vandaag in het kort</strong></h3>
{tabel(["Wedstrijd", "Baan en tijd", "Tip", "Markt", "Odd"], [(f"<strong>{w}</strong>", t, tip, m, f"<strong>{o}</strong>") for w, t, tip, m, o in TIPS] + [("<strong>Combinatie</strong>", "", "Alle vier de tips", "", f"<strong>{COMBI}</strong>")])}
<p><em>Odds bij {L['711']}, dinsdagochtend 3 november rond 10:00 uur. Odds en aanvangstijden kunnen nog veranderen; tijden met ± zijn een schatting, omdat de partijen na elkaar op dezelfde baan worden gespeeld. De tips staan los van elkaar: je kunt ze apart spelen of combineren.</em></p>
<h3><strong>Live kijken</strong></h3>
<p>{L['ziggo']} zendt de Paris Masters uit: vandaag op Ziggo Sport 1 van 11:00 tot 15:00 uur en op Ziggo Sport 4 van 11:00 tot 20:55 uur. Welke baan er op welk moment op tv is, beslist de zender. Hoe je gratis kunt kijken, ook naar de avondpartij van Jódar, lees je in {L['kijk']}.</p>"""

content2 = f"""<h3><strong>Tommy Paul – Holger Rune (Court 1, ± 14:00 uur)</strong></h3>
<p><strong>De situatie.</strong> Paul (nummer 14, twaalfde reekshoofd) draait een sterk seizoen: 46 zeges en 21 nederlagen. Vorige week haalde hij in Wenen de kwartfinale, waarin hij pas na een tiebreak in de tweede set verloor van Carlos Alcaraz. Daarvoor won hij met 6-1, 6-1 van Luciano Darderi en met 7-5, 6-2 van Andrey Rublev. In de race naar Turijn staat Paul dertiende, dus hij heeft punten nodig.</p>
<p>Rune is terug na een zware blessure. Hij scheurde in oktober 2025 in Stockholm zijn achillespees en miste daardoor bijna het hele seizoen 2026. Door die afwezigheid is hij gezakt naar plek 433; hij speelt in Parijs met een beschermde ranking. In Basel won hij vorige week voor het eerst weer wedstrijden op ATP-niveau, maar dat kostte veel: twee partijen werden pas in een tiebreak in de derde set beslist, en in de kwartfinale verloor hij in drie sets van Vacherot.</p>
<p><strong>Onderling.</strong> De twee speelden nog nooit tegen elkaar.</p>
<p><strong>Onze tip: Paul wint (1,42).</strong></p>
{markt("winnaar van de wedstrijd. Paul moet de partij winnen; het maakt niet uit in hoeveel sets. Geeft een speler op, dan bepalen de regels van de bookmaker of je weddenschap geldig blijft.")}
{waarom(["<strong>Paul is in vorm.</strong> Kwartfinale in Wenen, halve finale in Lyon en een seizoensbalans van 46-21.",
         "<strong>Rune heeft nog weinig wedstrijden in de benen.</strong> Hij speelde dit jaar zeven partijen op ATP-niveau, en de drie in Basel duurden allemaal lang.",
         "<strong>Paul speelt om Turijn.</strong> Als nummer dertien in de race heeft hij elke overwinning nodig."])}
<p><strong>Het risico:</strong> Rune won Parijs in 2022 en liet in Basel zien dat zijn niveau terugkomt: hij versloeg er Hubert Hurkacz. Als hij fris is, is hij op indoor hardcourt een gevaarlijke tegenstander. Wil je een hogere odd? Paul -1,5 games staat op 1,50.</p>
<h3><strong>Novak Djokovic – Valentin Vacherot (centercourt, ± 14:00 uur)</strong></h3>
<p><strong>De situatie.</strong> Vacherot (nummer 27) is in topvorm. Zondag won hij het toernooi van Basel, met vijf zeges op rij in de hal. Onderweg versloeg hij Rafael Jódar, Holger Rune, Taylor Fritz en in de finale Jiří Lehečka. Parijs ligt hem ook: vorig jaar haalde hij hier als wildcard de kwartfinale. En hij weet hoe hij Djokovic moet verslaan. In de halve finale van Shanghai 2025 won hij als kwalificant met 6-3, 6-4 van de Serviër, en daarna won hij dat hele toernooi.</p>
<p>Djokovic (nummer 11) won Parijs zeven keer, maar zijn seizoen verloopt wisselend: 20 zeges en 9 nederlagen. Hij won in oktober het toernooi van Beijing, maar verloor in Shanghai van Hurkacz en vorige week in Basel van Jan-Lennard Struff. Djokovic vertelde in Parijs zelf dat hij vier maanden met een lichamelijk probleem worstelde, dat meer met zijn gezondheid dan met zijn conditie te maken had. Het gaat nu beter, zei hij.</p>
<p><strong>Onderling.</strong> Vacherot leidt met 1-0: Shanghai 2025, 6-3, 6-4.</p>
<p><strong>Onze tip: Vacherot wint minstens één set (1,63).</strong></p>
{markt("wint Vacherot minstens één set: ja. De tip is goed als Vacherot een set wint, ook als Djokovic de wedstrijd daarna in drie sets wint. Wint Vacherot de wedstrijd, dan is de tip natuurlijk ook goed. Alleen bij een 2-0 voor Djokovic is de tip verloren.")}
{waarom(["<strong>Vacherot won vijf indoorwedstrijden op rij.</strong> Onder meer tegen drie spelers uit de top vijftien.",
         "<strong>Hij versloeg Djokovic al eens.</strong> In Shanghai was het 6-3, 6-4, zonder setverlies.",
         "<strong>Djokovic is niet op zijn best.</strong> Twee nederlagen in zijn laatste drie toernooien en een lichamelijk probleem waar hij mee worstelde."])}
<p><strong>Het risico:</strong> Vacherot speelde zondag nog de finale in Basel en staat twee dagen later alweer op de baan. Djokovic moet in Parijs ver komen om nog kans te maken op Turijn, en zo'n situatie haalt vaak het beste in hem naar boven. Durf je meer? Vacherot wint staat op 2,70.</p>"""

content3 = f"""<h3><strong>Alex Michelsen – Jiří Lehečka (Court 2, niet voor 15:00 uur)</strong></h3>
<p><strong>De situatie.</strong> Lehečka (nummer 15) speelde vorige week vijf wedstrijden in Basel en verloor zondag pas in de finale, in drie sets van Vacherot. Twee dagen later begint hij in Parijs. Hij draait wel een sterk seizoen: 40 zeges en 21 nederlagen, en 28-14 op hardcourt. Vorig jaar verloor hij in Parijs meteen, met 6-1, 6-3 van Vacherot.</p>
<p>Michelsen (nummer 35) verloor de afgelopen twee weken twee keer nipt van Arthur Fils: in Brussel met 6-4, 7-6 na een tiebreak van 14-12, en in Basel pas in een tiebreak in de derde set, nadat hij de eerste set had gewonnen. Daarvoor won hij in Basel van Botic van de Zandschulp. Zijn hoogtepunt dit jaar was de kwartfinale op de US Open.</p>
<p><strong>Onderling.</strong> Het staat 1-1. Op de Australian Open 2024 (hardcourt) won Michelsen in vier sets, in Madrid 2026 (gravel) won Lehečka met 6-4, 6-2.</p>
<p><strong>Onze tip: Michelsen +2,5 games (1,75).</strong></p>
{markt("game handicap. " + HELE + " Michelsen krijgt vooraf 2,5 games voorsprong. De tip is goed als Michelsen wint, of verliest met maximaal twee games verschil. Een voorbeeld: Lehečka wint met 7-6, 6-4 (13 tegen 10): drie games verschil, de tip is verloren. Wint Lehečka met 6-4, 3-6, 6-4 (15 tegen 14), dan is de tip goed.")}
{waarom(["<strong>Lehečka zit op een zware week.</strong> Vijf wedstrijden in Basel, met de finale op zondag.",
         "<strong>Michelsen speelt goed indoor.</strong> Zijn twee nederlagen tegen Fils waren allebei krap en eindigden in tiebreaks.",
         "<strong>Het onderlinge duel op hardcourt</strong> won Michelsen, en op deze ondergrond liggen de twee dicht bij elkaar."])}
<p><strong>Het risico:</strong> Lehečka is de betere speler op papier en staat indoor dit seizoen op 5-2. Wint hij in twee duidelijke sets, dan is het gameverschil al snel drie of meer. Liever meer zekerheid? Michelsen wint minstens één set staat op 1,49.</p>
<h3><strong>Casper Ruud – Rafael Jódar (centercourt, niet voor 20:30 uur)</strong></h3>
<p><strong>De situatie.</strong> Beide spelers wonnen gisteren in twee sets. Ruud (nummer 23) was ijzersterk tegen qualifier Juan Manuel Cerúndolo: 6-3, 6-2 in een uur, zonder dat hij één breekkans tegen kreeg. Jódar (nummer 10, negende reekshoofd) won met 6-2, 6-3 van Alejandro Tabilo. Jódar speelt het seizoen van zijn leven, met 44 zeges en 18 nederlagen, en staat tiende in de race naar Turijn, één punt achter Alex de Minaur. Elke zege in Parijs telt dus voor hem. Ruud staat ver van de Turijn-plaatsen en speelt op hardcourt een gemiddeld jaar (13-12).</p>
<p><strong>Onderling.</strong> Jódar leidt met 1-0. In de kwartfinale van Shanghai, vorige maand, verloor hij de eerste set, maar won hij daarna met 4-6, 6-4, 6-3. Jódar haalde daar uiteindelijk de finale.</p>
<p><strong>Onze tip: Jódar wint (1,53).</strong></p>
{markt("winnaar van de wedstrijd. Jódar moet de partij winnen, in twee of drie sets.")}
{waarom(["<strong>Jódar won het enige duel</strong>, vorige maand op hardcourt in Shanghai.",
         "<strong>Groot verschil op deze ondergrond.</strong> Jódar staat op hardcourt op 22-13, Ruud op 13-12.",
         "<strong>Jódar speelt om Turijn.</strong> Hij staat tiende in de race, één punt achter de nummer negen."])}
<p><strong>Het risico:</strong> Ruud serveerde gisteren uitstekend, en in Shanghai won hij de eerste set van Jódar. Is zijn opslag weer zo sterk, dan wordt dit een lange avond. Na deze partij volgt het afscheid van Gaël Monfils op de centercourt. Wil je een hogere odd? Jódar -1,5 games staat op 1,65.</p>
<h3><strong>Combinatie dinsdag 3 november</strong></h3>
<p>Alle vier de tips samen: 1,42 × 1,63 × 1,75 × 1,53 = <strong>± {COMBI}</strong>. Een inzet van €10 levert bij deze combinatie ongeveer €62 op. Hoe meer tips in een combinatie, hoe groter de kans dat er één misgaat. Wil je minder risico, speel de tips dan los, of combineer alleen Paul en Jódar (samen ± 2,17).</p>
<h3><strong>De andere partijen van vandaag</strong></h3>
<p>Zonder extra tip van ons: om 11:00 uur opent Arthur Rinderknech op de centercourt tegen Francisco Cerúndolo. Rinderknech liep begin oktober in Beijing een scheur in een buikspier op en verloor zijn laatste vier wedstrijden. Andrey Rublev speelt om 11:00 uur tegen Tomás Martín Etcheverry, die zes wedstrijden op rij verloor. Ben Shelton begint in de avondsessie (niet voor 19:00 uur) tegen Cameron Norrie, maar Shelton zit sinds de US Open in een dip: twee zeges en vier nederlagen, met acht tiebreaks in zijn laatste vier partijen. Taylor Fritz speelt niet voor 15:30 uur tegen qualifier Benjamin Bonzi, die Tallon Griekspoor uit de kwalificatie sloeg; Fritz staat op 1,23, maar speelde de afgelopen twee weken al negen wedstrijden. De strijd om Turijn volg je in {L['turijn']}.</p>
<h3><strong>Wat betekenen deze weddenschappen?</strong></h3>
<p><strong>Winnaar.</strong> De speler moet de wedstrijd winnen, in twee of drie sets.</p>
<p><strong>Wint speler minstens één set.</strong> De tip is goed zodra de speler één set wint, ongeacht wie de wedstrijd wint.</p>
<p><strong>Game handicap (+2,5 games).</strong> Tel na de wedstrijd alle gewonnen games per speler op, over alle sets. Bij een plus-handicap krijgt jouw speler die games er vooraf bij. Heeft hij daarna meer games dan de tegenstander, dan wint de tip. Een tiebreak telt als één game voor de winnaar ervan.</p>
<p>Geeft een speler op, dan hangt het van de regels van de bookmaker af wat er met je weddenschap gebeurt. Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit; lees {L['legaal']}. Benieuwd hoe lang een partij duurt? Lees {L['duur']}. Meer tips vind je op onze pagina {L['tips']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wat zijn de beste Paris Masters-voorspellingen van vandaag?</strong><br>Paul wint van Rune (1,42), Vacherot wint minstens één set van Djokovic (1,63), Michelsen +2,5 games tegen Lehečka (1,75) en Jódar wint van Ruud (1,53). Gecombineerd is de odd ongeveer {COMBI}.</p>
<p><strong>Hoe deden de tennistips van gisteren het?</strong><br>Alle vier goed: Jódar won in twee sets, Norrie en Macháč wonnen hun partij en Humbert won met drie games meer dan Van de Zandschulp.</p>
<p><strong>Hoe laat speelt Djokovic vandaag?</strong><br>Als derde partij op de centercourt, na Rinderknech – Cerúndolo en Davidovich Fokina – Kouamé, naar verwachting rond 14:00 uur.</p>
<p><strong>Wie wint Djokovic – Vacherot?</strong><br>De bookmakers zien Djokovic als favoriet, maar Vacherot won zondag Basel en versloeg Djokovic eerder al. Wij verwachten dat Vacherot minstens één set wint.</p>
<p><strong>Hoe laat speelt Jódar tegen Ruud?</strong><br>Niet voor 20:30 uur, als laatste partij op de centercourt.</p>
<p><strong>Waar kan ik de Paris Masters live kijken?</strong><br>Op Ziggo Sport 1 en Ziggo Sport 4. Gratis kijken kan ook; hoe, lees je in {L['kijk']}.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

WEDTIPS = {"wedstrijd-1": "Combinatie: alle vier de tips",
           "wedtip-1-2": "Paul wint + Vacherot wint minstens één set + Michelsen +2.5 games + Jódar wint",
           "quotering-wedtip-1": "6.20",
           "wedstrijd-2": "Paul vs Rune", "wedtip-2-2": "Paul wint", "quotering-wedtip-2": "1.42",
           "wedstrijd-3": "Djokovic vs Vacherot", "wedtip-3-2": "Vacherot wint minstens één set", "quotering-wedtip-3": "1.63",
           "wedtip-4-2": "Jódar wint van Ruud", "quotering-wedtip-4": "1.53"}

if __name__ == "__main__":
    import re
    if "--velden" in sys.argv:
        import lk_webflow as WF
        it = WF._req("GET", f"{WF.WF_API}/collections/{WF.NIEUWS_COLLECTION}/items?slug={SLUG}")["items"][0]
        fd = {"tennis": True, "bookmaker-wedtips": BOOKMAKER_711, "datum-tijd-van-wedstrijd": "2026-11-03T13:00:00.000Z", **WEDTIPS}
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
    assert abs(1.42 * 1.53 - 2.17) < 0.01
    assert [t[4] for t in TIPS] == ["1,42", "1,63", "1,75", "1,53"]
    assert alles.count("<p><strong>De markt:</strong>") == 4
    assert 7 + 6 - (6 + 4) == 3 and (6 + 3 + 6) - (4 + 6 + 4) == 1   # rekenvoorbeelden Michelsen +2,5
    assert "<h2" not in alles and "<h4" not in alles and "betcity" not in alles.lower() and "/go/" not in alles
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    print("dry run ok")
