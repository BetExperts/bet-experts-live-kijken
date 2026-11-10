# -*- coding: utf-8 -*-
"""Los artikel: Paris Masters 2026 voorspellingen en wedtips voor maandag 2 november (dag 1 hoofdtoernooi, 1e ronde).
Eigenaar 2-11: 'de beste wedtips, odds rond de 1.4 en 1.6/7'. Partijen van 11:00 bewust overgeslagen (artikel live ±11:30).
Odds = 711 (Kambi sevelevnl, maandag 2-11 ±10:50). Combinatie 5,99.
Feiten: specials/paris_dag1_feiten.md (Tennis Abstract: rankings, seizoen 2026, recente uitslagen, H2H; atptour.com gaf
Cloudflare-403 en is niet omzeild) + paris_masters_feiten_2026.md (ATP-dagschema, Ziggo-uitzendschema).
Onzeker en daarom weggelaten/vaag: exacte ranking Norrie (41 of 45 -> 'rond plek 40'), blessure Blockx/Shapovalov,
indoor-balansen.
  python3 specials/paris_masters_tips_2026_11_02.py           (dry run)
  publiceren: specials/concept_publiceer.py paris_masters_tips_2026_11_02 --live; daarna --velden"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "paris-masters-2026-voorspellingen-wedtips-maandag-2-november"
RUBRIEK = "665715dbf1f3cbdf7f874d79"   # Tennis
BOOKMAKER_711 = "66a8a87062108480763b7309"
TITEL = "Paris Masters voorspellingen vandaag: 4 tips (2 november)"
SAMENVATTING = ("Paris Masters voorspellingen voor maandag 2 november: Norrie en Macháč winnen, Jódar in twee sets en "
                "Humbert -1,5 games. Met odds en tijden.")
ODDS = [1.45, 1.49, 1.62, 1.71]
COMBI = "5,99"

OG_LOGO = "paris-masters-logo.png"
OG_EYEBROW = "Tennis · maandag 2 november"
OG_KOP = "Paris Masters<br><em>4 wedtips</em>"
OG_TEGELS = [("Combi-odd", COMBI), ("Odds bij", "711")]
OG_KOPJE = "Onze tips (Nederlandse tijd)"
OG_RECHTS = "1e ronde · dag 1"
OG_RIJEN = [("± 12:30", "Jódar wint in 2 sets", "1,62"),
            ("± 14:00", "Norrie wint", "1,45"),
            ("na 15:30", "Macháč wint", "1,49"),
            ("na 20:30", "Humbert -1,5 games", "1,71")]

L = {"hub": '<a href="/nieuws/paris-masters-2026-schema-tijden-tv-deelnemers-prijzengeld">Paris Masters 2026: schema, deelnemers en prijzengeld</a>',
     "kijk": '<a href="/nieuws/atp-1000-parijs-live-gratis-kijken-in-nederland-tv-gids-ziggo-sport-en-gratis-opties-griekspoor-alcaraz-sinner-en-meer-in-actie">Paris Masters 2026 live kijken</a>',
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


TIPS = [("Tabilo – Jódar", "Centercourt, tweede partij (± 12:30 uur)", "Jódar wint in twee sets", "Setuitslag: 2-0 voor Jódar", "1,62"),
        ("Norrie – Arnaldi", "Court 1, derde partij (± 14:00 uur)", "Norrie wint", "Winnaar van de wedstrijd", "1,45"),
        ("Jacquet – Macháč", "Court 1, niet voor 15:30 uur", "Macháč wint", "Winnaar van de wedstrijd", "1,49"),
        ("Humbert – Van de Zandschulp", "Centercourt, niet voor 20:30 uur", "Humbert -1,5 games", "Game handicap, hele wedstrijd", "1,71")]

content = f"""<p><strong>Onze Paris Masters voorspellingen voor maandag 2 november: Rafael Jódar wint in twee sets van Alejandro Tabilo (1,62), Cameron Norrie wint van Matteo Arnaldi (1,45), Tomáš Macháč wint van Kyrian Jacquet (1,49) en Ugo Humbert wint met minstens twee games verschil van Botic van de Zandschulp (-1,5 games, 1,71). Het zijn allemaal partijen uit de eerste ronde van het ATP Masters 1000-toernooi in Parijs, op indoor hardcourt. De odds zijn van 711; gecombineerd is dat een odd van ongeveer {COMBI}.</strong></p>
<p>Vandaag begint het hoofdtoernooi van de Rolex Paris Masters in de Paris La Défense Arena, die nu Plenitude Arena heet. De eerste partijen beginnen om 11:00 uur; die laten we buiten onze tips, zodat je alle tips nog op tijd kunt spelen. Parijs ligt in dezelfde tijdzone als Nederland, dus alle tijden zijn Nederlandse tijden. Bij elke tip staat precies welke markt het is. Alles over het toernooi, zoals het schema, de deelnemers en het prijzengeld, lees je in {L['hub']}.</p>
<h3><strong>Paris Masters voorspellingen vandaag in het kort</strong></h3>
{tabel(["Wedstrijd", "Baan en tijd", "Tip", "Markt", "Odd"], [(f"<strong>{w}</strong>", t, tip, m, f"<strong>{o}</strong>") for w, t, tip, m, o in TIPS] + [("<strong>Combinatie</strong>", "", "Alle vier de tips", "", f"<strong>{COMBI}</strong>")])}
<p><em>Odds bij {L['711']}, maandagochtend 2 november rond 10:50 uur. Odds en aanvangstijden kunnen nog veranderen; tijden met ± zijn een schatting, omdat de partijen na elkaar op dezelfde baan worden gespeeld. De tips staan los van elkaar: je kunt ze apart spelen of combineren.</em></p>
<h3><strong>Live kijken</strong></h3>
<p>{L['ziggo']} zendt de Paris Masters uit: vandaag op Ziggo Sport 1 van 11:00 tot 19:00 uur en op Ziggo Sport 4 van 11:00 tot 23:00 uur. De avondpartij van Van de Zandschulp zie je dus op Ziggo Sport 4. Welke baan er op welk moment op tv is, beslist de zender. Hoe je gratis kunt kijken, lees je in {L['kijk']}.</p>
<h3><strong>Zo hebben we deze tips gekozen</strong></h3>
<p>Bij elke tip kijken we naar de ranglijst, de vorm van de laatste weken, de onderlinge duels en hoe de spelers op hardcourt presteren. Indoor hardcourt is een snelle ondergrond zonder wind en zon, waarop de opslag zwaar weegt. Bij elke tip noemen we ook eerlijk het grootste risico.</p>"""

content2 = f"""<h3><strong>Alejandro Tabilo – Rafael Jódar (centercourt, ± 12:30 uur)</strong></h3>
<p><strong>De situatie.</strong> Jódar is de doorbraak van het jaar: vorig jaar speelde hij nog Challengers, nu is hij nummer 10 van de wereld en negende reekshoofd in Parijs. Hij staat dit seizoen op 44 zeges en 18 nederlagen en haalde drie weken geleden de finale van het Masters-toernooi van Shanghai. Daar versloeg hij onder anderen Casper Ruud en Daniil Medvedev, en verloor hij pas in drie sets van Alejandro Davidovich Fokina. Vorige week in Basel ging hij in de tweede ronde onderuit tegen Valentin Vacherot, pas in een tiebreak in de derde set. In Parijs speelt Jódar om een ticket voor de ATP Finals in Turijn: hij moet vandaag winnen om in de race te blijven.</p>
<p>Tabilo (nummer 30) zit in een dip. Sinds zijn zege op Tommy Paul in Tokio, eind september, won hij geen wedstrijd meer op ATP-niveau. Daarna verloor hij in Tokio van Denis Shapovalov, in Shanghai van Pablo Carreño Busta en vorige week in Basel van... Jódar.</p>
<p><strong>Onderling.</strong> Jódar leidt met 3-1 en won de laatste drie duels.</p>
{tabel(["Jaar", "Toernooi", "Winnaar", "Uitslag (vanuit de winnaar)"], [
    ("2026", "Basel, vorige week (indoor hard)", "Jódar", "6-4, 6-2"),
    ("2026", "Cincinnati (hard)", "Jódar", "6-2, 6-1"),
    ("2026", "Washington (hard)", "Jódar", "6-7(6), 6-4, 6-4"),
    ("2026", "Indian Wells (hard)", "Tabilo", "6-1, 6-2"),
])}
<p><strong>Onze tip: Jódar wint in twee sets (1,62).</strong></p>
{markt("setuitslag. Jódar moet met 2-0 in sets winnen. Wint hij in drie sets, of wint Tabilo, dan is de tip verloren. Gewoon Jódar wint staat op 1,21; door de tweesetsoverwinning te kiezen krijg je een veel hogere odd.")}
{waarom(["<strong>Vorige week was het al eenzijdig.</strong> In Basel won Jódar met 6-4, 6-2, en in Cincinnati gaf hij Tabilo maar drie games.",
         "<strong>Tabilo is uit vorm.</strong> Drie nederlagen op ATP-niveau op rij, en zijn laatste zege dateert van eind september.",
         "<strong>Groot klasseverschil.</strong> Nummer 10 tegen nummer 30, met een seizoensbalans van 44-18 tegen 26-27.",
         "<strong>Jódar moet winnen.</strong> Een nederlaag kost hem waarschijnlijk zijn plek in Turijn, dus hij komt gefocust de baan op."])}
<p><strong>Het risico:</strong> bij deze markt is één verloren set al genoeg om de tip te verliezen. Tabilo is linkshandig en won in maart nog met 6-1, 6-2 van Jódar. En de druk van de race naar Turijn kan ook verlammend werken.</p>
<h3><strong>Cameron Norrie – Matteo Arnaldi (Court 1, ± 14:00 uur)</strong></h3>
<p><strong>De situatie.</strong> Norrie (rond plek 40) speelde vorige week in Wenen sterk. Hij versloeg Francisco Cerúndolo met 6-4, 6-1 en had Medvedev bijna: de Rus won pas met een tiebreak in de derde set. Parijs ligt hem bovendien: vorig jaar haalde hij hier de achtste finale, met een zege op Carlos Alcaraz.</p>
<p>Arnaldi (nummer 36) speelt een moeizaam seizoen op hardcourt: 3 zeges en 11 nederlagen. Hij verloor zijn laatste drie wedstrijden op ATP-niveau, alle drie in twee sets: van Taylor Fritz in Shanghai, van Lorenzo Musetti in Lyon (6-1, 6-4) en vorige week van Luciano Darderi in Wenen (7-5, 6-2). Vorig jaar strandde hij in Parijs in de kwalificatie.</p>
<p><strong>Onderling.</strong> Arnaldi leidt met 1-0: op de US Open van 2023 won hij met 6-3, 6-4, 6-3. Dat is drie jaar geleden.</p>
<p><strong>Onze tip: Norrie wint (1,45).</strong></p>
{markt("winnaar van de wedstrijd. Norrie moet de partij winnen; het maakt niet uit in hoeveel sets. Geeft een speler op, dan bepalen de regels van de bookmaker of je weddenschap geldig blijft.")}
{waarom(["<strong>Arnaldi staat dit jaar op 3-11 op hardcourt.</strong> Op deze ondergrond verliest hij bijna elke week.",
         "<strong>Norrie is in vorm.</strong> Vorige week stond hij tegen Medvedev in de derde set nog op gelijke hoogte.",
         "<strong>Goede herinneringen aan Parijs.</strong> Vorig jaar versloeg Norrie hier Alcaraz en haalde hij de achtste finale.",
         "<strong>Er staat een prijs klaar.</strong> De winnaar speelt in de tweede ronde tegen Ben Shelton."])}
<p><strong>Het risico:</strong> Arnaldi won het enige onderlinge duel overtuigend, en Norrie heeft dit seizoen zelf ook een negatieve balans (22-23). Half oktober verloor hij in Lyon nog van Benjamin Bonzi.</p>"""

content3 = f"""<h3><strong>Kyrian Jacquet – Tomáš Macháč (Court 1, niet voor 15:30 uur)</strong></h3>
<p><strong>De situatie.</strong> Macháč (nummer 69) kwam via de kwalificatie in het hoofdtoernooi, en dat ging overtuigend. Hij won zonder setverlies van Daniel Landaluce (6-4, 6-3) en van het eerste reekshoofd van de kwalificatie, Sebastián Báez (6-2, 6-4). Hij heeft dus al twee wedstrijden in deze hal in de benen. Vorige week pakte hij in Wenen ook al een set van Alex de Minaur (6-1).</p>
<p>Jacquet (nummer 80) speelt met een wildcard voor eigen publiek. Hij won dit jaar veel op het Challenger-circuit, maar op ATP-niveau staat hij op 8 zeges en 10 nederlagen. Zijn laatste toernooi was Lyon, twee weken geleden, waar hij Matteo Berrettini versloeg en daarna van Brandon Nakashima verloor (6-4, 6-3).</p>
<p><strong>Onderling.</strong> De twee speelden nog nooit tegen elkaar.</p>
<p><strong>Onze tip: Macháč wint (1,49).</strong></p>
{markt("winnaar van de wedstrijd. Macháč moet de partij winnen, in twee of drie sets.")}
{waarom(["<strong>Macháč is al op temperatuur.</strong> Twee zeges in twee sets in de kwalificatie, op dezelfde banen.",
         "<strong>Hij speelt de laatste weken goed.</strong> In Wenen won hij een set van De Minaur, in Almaty stond hij tegen Karen Khachanov tot de tiebreak van de derde set.",
         "<strong>Jacquet mist ritme op dit niveau.</strong> Hij speelde sinds Lyon geen wedstrijd meer en staat op ATP-niveau onder de 50 procent."])}
<p><strong>Het risico:</strong> Jacquet heeft het Franse publiek achter zich, en dat kan in Parijs een groot verschil maken. Bovendien won Macháč dit jaar indoor op ATP-niveau maar één van zijn vier wedstrijden.</p>
<h3><strong>Ugo Humbert – Botic van de Zandschulp (centercourt, niet voor 20:30 uur)</strong></h3>
<p><strong>De situatie.</strong> De laatste partij van de dag is die van de enige Nederlander in het hoofdtoernooi. Op de ranglijst zijn ze bijna gelijk: Van de Zandschulp is nummer 37, Humbert nummer 38. Beide spelers zitten in een mindere periode. Humbert verloor zijn laatste vier wedstrijden, al waren de laatste drie daarvan pas in drie sets: tegen Novak Djokovic in Basel won hij zelfs de eerste set. Van de Zandschulp verloor zijn laatste drie wedstrijden, waaronder in Brussel van qualifier Moez Chidekh (6-1, 6-4). Daarvoor haalde hij in Shanghai wel de achtste finale, met zeges op Arthur Fils en Alex Michelsen.</p>
<p><strong>Onderling.</strong> Humbert won alle vijf de duels op ATP-niveau, en verloor sinds 2024 geen set meer tegen Van de Zandschulp.</p>
{tabel(["Jaar", "Toernooi", "Uitslag (Humbert won)", "Games Humbert – Van de Zandschulp"], [
    ("2026", "Montpellier (indoor hard)", "6-3, 6-4", "12-7"),
    ("2024", "Wimbledon (gras)", "7-6(9), 6-1, 6-3", "19-10"),
    ("2024", "Madrid (gravel)", "6-3, 6-3", "12-6"),
    ("2024", "Miami (hard)", "6-4, 6-3", "12-7"),
    ("2023", "Shanghai (hard)", "6-4, 1-6, 6-2", "13-12"),
])}
<p><strong>Onze tip: Humbert -1,5 games (1,71).</strong></p>
{markt("game handicap. " + HELE + " Humbert krijgt vooraf 1,5 game achterstand. De tip wint als hij de wedstrijd wint met minstens twee games meer dan Van de Zandschulp, bijvoorbeeld 6-4, 6-4 (12 tegen 8). Bij 7-6, 6-4 (13 tegen 10) is de tip ook goed; wint Humbert met 6-4, 1-6, 6-4 (13 tegen 14), dan niet.")}
{waarom(["<strong>Een duidelijke onderlinge balans.</strong> In vier van de vijf duels won Humbert met vijf games of meer verschil; alleen in 2023 was het krapper.",
         "<strong>Het laatste duel was indoor.</strong> In Montpellier, dit jaar, won Humbert met 6-3, 6-4, in een hal zoals deze.",
         "<strong>Thuispubliek.</strong> Humbert speelt de avondsessie op de centercourt in Parijs, met het Franse publiek achter zich.",
         "<strong>De linkshandige opslag van Humbert</strong> is indoor een groot wapen."])}
<p><strong>Het risico:</strong> Humbert verloor vier keer op rij en Van de Zandschulp heeft niets te verliezen. Wint de Nederlander een set, dan wordt het gameverschil snel kleiner. Hoop je op een Nederlandse zege? Van de Zandschulp wint staat op 2,38, en Van de Zandschulp +1,5 games op 2,07.</p>
<h3><strong>Combinatie maandag 2 november</strong></h3>
<p>Alle vier de tips samen: 1,62 × 1,45 × 1,49 × 1,71 = <strong>± {COMBI}</strong>. Een inzet van €10 levert bij deze combinatie ongeveer €59,90 op. Hoe meer tips in een combinatie, hoe groter de kans dat er één misgaat. Wil je minder risico, speel de tips dan los, of combineer alleen Norrie en Macháč (samen ± 2,16).</p>
<h3><strong>De andere partijen van vandaag</strong></h3>
<p>Zonder extra tip van ons: op de centercourt opent Lorenzo Musetti tegen Hubert Hurkacz (11:00 uur, 1,90 tegen 1,90), later volgen Casper Ruud tegen qualifier Juan Manuel Cerúndolo (Ruud 1,36, maar Cerúndolo won twee van hun drie duels) en Denis Shapovalov tegen Karen Khachanov (niet voor 19:00 uur, Khachanov 1,61). Op Court 2 begint Zizou Bergs om 11:00 uur tegen Ignacio Buse (Bergs 1,36), en Alexander Blockx speelt daarna tegen Daniel Mérida (Blockx 1,61). Blockx speelde sinds Shanghai geen wedstrijd meer, en dat maakt hem voor ons te onzeker. De strijd om de laatste plekken in Turijn volg je in {L['turijn']}.</p>
<h3><strong>Wat betekenen deze weddenschappen?</strong></h3>
<p><strong>Winnaar.</strong> De speler moet de wedstrijd winnen, in twee of drie sets.</p>
<p><strong>Setuitslag (2-0).</strong> Je voorspelt de exacte uitslag in sets. Bij 2-0 moet de speler beide sets winnen.</p>
<p><strong>Game handicap (-1,5 games).</strong> Tel na de wedstrijd alle gewonnen games per speler op, over alle sets. Bij een min-handicap gaan die games er vooraf af. Heeft jouw speler daarna nog meer games, dan wint de tip. Een tiebreak telt als één game voor de winnaar ervan.</p>
<p>Geeft een speler op, dan hangt het van de regels van de bookmaker af wat er met je weddenschap gebeurt. Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit; lees {L['legaal']}. Benieuwd hoe lang een partij duurt? Lees {L['duur']}. Meer tips vind je op onze pagina {L['tips']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wat zijn de beste Paris Masters-voorspellingen van vandaag?</strong><br>Jódar wint in twee sets van Tabilo (1,62), Norrie wint van Arnaldi (1,45), Macháč wint van Jacquet (1,49) en Humbert -1,5 games tegen Van de Zandschulp (1,71). Gecombineerd is de odd ongeveer {COMBI}.</p>
<p><strong>Hoe laat speelt Botic van de Zandschulp vandaag?</strong><br>Niet voor 20:30 uur, als laatste partij op de centercourt, tegen Ugo Humbert. De partij is live op Ziggo Sport 4.</p>
<p><strong>Wie wint Humbert – Van de Zandschulp?</strong><br>Wij verwachten Humbert: hij won alle vijf de onderlinge duels en speelt voor eigen publiek. Daarom tippen we Humbert -1,5 games.</p>
<p><strong>Hoe laat speelt Jódar in Parijs?</strong><br>Als tweede partij op de centercourt, na Musetti – Hurkacz, naar verwachting rond 12:30 uur.</p>
<p><strong>Waar kan ik de Paris Masters live kijken?</strong><br>Op Ziggo Sport 1 en Ziggo Sport 4. Gratis kijken kan ook; hoe, lees je in {L['kijk']}.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

WEDTIPS = {"wedstrijd-1": "Combinatie: alle vier de tips",
           "wedtip-1-2": "Jódar wint 2-0 in sets + Norrie wint + Macháč wint + Humbert -1.5 games (hele wedstrijd)",
           "quotering-wedtip-1": "5.99",
           "wedstrijd-2": "Tabilo vs Jódar", "wedtip-2-2": "Jódar wint in twee sets (2-0)", "quotering-wedtip-2": "1.62",
           "wedstrijd-3": "Norrie vs Arnaldi", "wedtip-3-2": "Norrie wint", "quotering-wedtip-3": "1.45",
           "wedtip-4-2": "Humbert -1.5 games tegen Van de Zandschulp (hele wedstrijd)", "quotering-wedtip-4": "1.71"}

if __name__ == "__main__":
    import re
    if "--velden" in sys.argv:
        import lk_webflow as WF
        it = WF._req("GET", f"{WF.WF_API}/collections/{WF.NIEUWS_COLLECTION}/items?slug={SLUG}")["items"][0]
        fd = {"tennis": True, "bookmaker-wedtips": BOOKMAKER_711, "datum-tijd-van-wedstrijd": "2026-11-02T11:30:00.000Z", **WEDTIPS}
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
    assert abs(1.45 * 1.49 - 2.16) < 0.01
    assert [t[4] for t in TIPS] == ["1,62", "1,45", "1,49", "1,71"]
    assert alles.count("<p><strong>De markt:</strong>") == 4
    assert "<h2" not in alles and "<h4" not in alles and "betcity" not in alles.lower() and "/go/" not in alles
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    print("dry run ok")
