# -*- coding: utf-8 -*-
"""Los artikel: Paris Masters 2026 voorspellingen en wedtips voor woensdag 4 november (dag 3: 2e ronde). Eigenaar 3-11: 'gisteren 3/4,
Ruud won knap van Jódar' (Paul 7-5 6-4, Vacherot pakte set 1 maar Djokovic won 6-7(5) 7-5 6-1, Michelsen 6-7(5) 6-2 6-4, Ruud 6-3 6-4).
Odds 711 (Kambi sevelevnl, dinsdag 3-11 ±22:30). Partijen van 11:00 bewust overgeslagen.
Feiten: specials/paris_dag3_feiten.md (officiële toernooisite + Tennis Majors/TennisActu + Tennis Abstract; atptour.com niet gebruikt).
Onzeker en daarom vaag: exacte aanvangstijden (alleen 'niet voor'-tijden bevestigd), tv-indeling per baan op Ziggo Sport.
  python3 specials/paris_masters_tips_2026_11_04.py           (dry run)
  publiceren: specials/concept_publiceer.py paris_masters_tips_2026_11_04 --live; daarna --velden"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "paris-masters-2026-voorspellingen-wedtips-woensdag-4-november"
RUBRIEK = "665715dbf1f3cbdf7f874d79"   # Tennis
BOOKMAKER_711 = "66a8a87062108480763b7309"
TITEL = "Paris Masters voorspellingen vandaag: 4 tips (4 november)"
SAMENVATTING = ("Paris Masters voorspellingen voor woensdag 4 november: Tien en Fils winnen, Musetti pakt een set van Zverev "
                "en De Minaur – Etcheverry duurt maximaal twee sets.")
ODDS = [1.44, 1.78, 1.43, 1.49]
COMBI = "5,46"

OG_LOGO = "paris-masters-logo.png"
OG_EYEBROW = "Tennis · woensdag 4 november"
OG_KOP = "Paris Masters<br><em>4 wedtips</em>"
OG_TEGELS = [("Gisteren", "3/4"), ("Combi-odd", COMBI)]
OG_KOPJE = "Onze tips (Nederlandse tijd)"
OG_RECHTS = "Odds bij 711"
OG_RIJEN = [("± 12:30", "Tien wint van Van Assche", "1,44"),
            ("na 13:30", "Musetti wint min. 1 set", "1,78"),
            ("± 14:00", "De Minaur – Etcheverry: max. 2 sets", "1,43"),
            ("na 20:30", "Fils wint van Macháč", "1,49")]

L = {"hub": '<a href="/nieuws/paris-masters-2026-schema-tijden-tv-deelnemers-prijzengeld">Paris Masters 2026: schema, deelnemers en prijzengeld</a>',
     "kijk": '<a href="/nieuws/atp-1000-parijs-live-gratis-kijken-in-nederland-tv-gids-ziggo-sport-en-gratis-opties-griekspoor-alcaraz-sinner-en-meer-in-actie">Paris Masters 2026 live kijken</a>',
     "gisteren": '<a href="/nieuws/paris-masters-2026-voorspellingen-wedtips-dinsdag-3-november">onze tips van dinsdag</a>',
     "tips": '<a href="/tennis-voorspellingen-vandaag">tennis voorspellingen vandaag</a>',
     "ziggo": '<a href="/zenders/ziggo-sport">Ziggo Sport</a>',
     "duur": '<a href="/nieuws/hoe-lang-duurt-een-tenniswedstrijd">hoelang duurt een tenniswedstrijd</a>',
     "turijn": '<a href="/nieuws/atp-finals-2026-gekwalificeerd-race-to-turin">ATP Finals 2026: wie zijn er al gekwalificeerd?</a>',
     "711": '<a href="/bookmakers/711">711</a>',
     "legaal": '<a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>'}


def waarom(punten):
    return "<p><strong>Waarom deze tip?</strong></p><ul>" + "".join(f"<li>{p}</li>" for p in punten) + "</ul>"


def markt(m):
    return f"<p><strong>De markt:</strong> {m}</p>"


TIPS = [("Van Assche – Tien", "Court 1, tweede partij (± 12:30 uur)", "Tien wint", "Winnaar van de wedstrijd", "1,44"),
        ("Zverev – Musetti", "Centercourt, niet voor 13:30 uur", "Musetti wint minstens één set", "Wint speler minstens één set: ja", "1,78"),
        ("Etcheverry – De Minaur", "Court 2, tweede partij (± 14:00 uur)", "Minder dan 2,5 sets", "Totaal aantal sets", "1,43"),
        ("Fils – Macháč", "Centercourt, niet voor 20:30 uur", "Fils wint", "Winnaar van de wedstrijd", "1,49")]

GISTEREN = [("Paul – Rune", "Paul wint", "7-5, 6-4 voor Paul", "✅"),
            ("Djokovic – Vacherot", "Vacherot wint min. 1 set", "6-7, 7-5, 6-1 voor Djokovic (set 1 voor Vacherot)", "✅"),
            ("Michelsen – Lehečka", "Michelsen +2,5 games", "6-7, 6-2, 6-4 voor Michelsen", "✅"),
            ("Ruud – Jódar", "Jódar wint", "6-3, 6-4 voor Ruud", "❌")]

content = f"""<p><strong>Onze Paris Masters voorspellingen voor woensdag 4 november: Learner Tien wint van Luca Van Assche (1,44), Lorenzo Musetti pakt minstens één set van Alexander Zverev (1,78), Alex de Minaur – Tomás Martín Etcheverry duurt maximaal twee sets (1,43) en Arthur Fils wint in de avondsessie van Tomáš Macháč (1,49). De odds zijn van 711; gecombineerd is dat een odd van ongeveer {COMBI}. Gisteren zaten drie van onze vier tips goed.</strong></p>
<p>Op dag drie van de Rolex Paris Masters in de Plenitude Arena wordt de hele tweede ronde afgemaakt. Wereldnummer één Alexander Zverev, Carlos Alcaraz, Daniil Medvedev, Alex de Minaur en Arthur Fils beginnen vandaag pas aan het toernooi, na een bye in de eerste ronde. Spelers noemen de baan dit jaar opvallend snel; Novak Djokovic vergeleek hem gisteren met ijs. Dat helpt de serveerders. De partijen van 11:00 uur laten we buiten onze tips, zodat je alles nog op tijd kunt spelen. Parijs ligt in dezelfde tijdzone als Nederland. Alles over het toernooi lees je in {L['hub']}.</p>
<h3><strong>Gisteren: 3 van de 4 tips raak</strong></h3>
{tabel(["Wedstrijd", "Onze tip", "Uitslag", ""], GISTEREN)}
<p>Tommy Paul won zonder problemen van Holger Rune, Valentin Vacherot pakte zoals verwacht de eerste set van Djokovic en Alex Michelsen won zelfs van Jiří Lehečka. Alleen onze avondtip ging mis: Casper Ruud speelde knap en won in twee sets van Rafael Jódar: hij sloeg 7 aces en benutte 3 van zijn 4 breekkansen. De combinatie viel daardoor niet. Teruglezen kan in {L['gisteren']}. Een tip blijft een inschatting; ook vandaag kan het anders lopen.</p>
<h3><strong>Paris Masters voorspellingen vandaag in het kort</strong></h3>
{tabel(["Wedstrijd", "Baan en tijd", "Tip", "Markt", "Odd"], [(f"<strong>{w}</strong>", t, tip, m, f"<strong>{o}</strong>") for w, t, tip, m, o in TIPS] + [("<strong>Combinatie</strong>", "", "Alle vier de tips", "", f"<strong>{COMBI}</strong>")])}
<p><em>Odds bij {L['711']}, dinsdagavond 3 november rond 22:30 uur. Odds en aanvangstijden kunnen nog veranderen; tijden met ± zijn een schatting, omdat de partijen na elkaar op dezelfde baan worden gespeeld. De tips staan los van elkaar: je kunt ze apart spelen of combineren.</em></p>
<h3><strong>Live kijken</strong></h3>
<p>{L['ziggo']} zendt de Paris Masters uit. Welke baan er op welk moment op tv is, beslist de zender. Hoe je gratis kunt kijken, ook naar de avondpartijen van Alcaraz en Fils, lees je in {L['kijk']}.</p>"""

content2 = f"""<h3><strong>Luca Van Assche – Learner Tien (Court 1, ± 12:30 uur)</strong></h3>
<p><strong>De situatie.</strong> Tien (nummer 19, vijftiende reekshoofd) won gisteren in drie sets van lucky loser Adolfo Daniel Vallejo, met 6-3, 5-7, 7-5. Mooi was dat niet: hij maakte 41 onnodige fouten. Maar de Amerikaan van 20 draait een sterk seizoen (33 zeges, 20 nederlagen) en moet hier minstens de derde ronde halen om in de top 20 te blijven. Dat geeft extra motivatie.</p>
<p>Van Assche (nummer 47) won maandag zijn eerste partij ooit in Parijs, met 6-3, 7-5 van Mariano Navone. De Fransman heeft het publiek mee, maar op tourniveau is hardcourt niet zijn ondergrond: dit seizoen staat hij daar op 4 zeges en 8 nederlagen. Zijn sterke cijfers haalt hij vooral op challengers (26-6).</p>
<p><strong>Onderling.</strong> Tien leidt met 1-0, en dat duel is pas een week oud: in Wenen won hij indoor met 6-3, 6-1.</p>
<p><strong>Onze tip: Tien wint (1,44).</strong></p>
{markt("winnaar van de wedstrijd. Tien moet de partij winnen; het maakt niet uit in hoeveel sets. Geeft een speler op, dan bepalen de regels van de bookmaker of je weddenschap geldig blijft.")}
{waarom(["<strong>Vorige week was het een eenzijdige partij.</strong> Tien won in Wenen met 6-3, 6-1, op dezelfde ondergrond.",
         "<strong>Groot verschil op hardcourt.</strong> Tien staat op 22-14, Van Assche op 4-8 op tourniveau.",
         "<strong>Tien heeft iets te verdedigen.</strong> Met de derde ronde blijft hij in de top 20."])}
<p><strong>Het risico:</strong> Tien was gisteren wisselvallig en liet Vallejo terugkomen in de tweede set. Van Assche speelt voor eigen publiek en won zijn eerste partij hier zonder één keer gebroken te worden. Wil je meer zekerheid? Tien wint minstens één set staat op 1,17.</p>
<h3><strong>Alexander Zverev – Lorenzo Musetti (centercourt, niet voor 13:30 uur)</strong></h3>
<p><strong>De situatie.</strong> Zverev is sinds maandag voor het eerst nummer één van de wereld. Hij won dit jaar Roland-Garros en de US Open en staat op 64 zeges en 16 nederlagen. Indoor speelde hij dit najaar wel een paar krappe partijen: in Wenen verloor hij in de halve finale in drie sets van De Minaur, en eerder in dat toernooi had hij een tiebreak in de derde set nodig tegen een wildcard. Vandaag speelt hij zijn eerste partij in Parijs.</p>
<p>Musetti (nummer 24) heeft er al een partij op zitten. Maandag won hij in twee tiebreaks van Hubert Hurkacz, en daarbij kreeg hij maar één breekpunt tegen. Indoor is de Italiaan dit seizoen sterk: 7 zeges en 1 nederlaag. Vorige maand won hij het toernooi van Lyon, met in de finale een zege op Taylor Fritz.</p>
<p><strong>Onderling.</strong> Musetti leidt met 3-2. Indoor staat het 1-1: in Wenen 2024 won Musetti in drie sets, in Wenen 2025 won Zverev met 6-4, 7-5.</p>
<p><strong>Onze tip: Musetti wint minstens één set (1,78).</strong></p>
{markt("wint Musetti minstens één set: ja. De tip is goed als Musetti een set wint, ook als Zverev de wedstrijd daarna in drie sets wint. Wint Musetti de partij, dan is de tip natuurlijk ook goed. Alleen bij een 2-0 voor Zverev is de tip verloren.")}
{waarom(["<strong>Musetti is in vorm.</strong> Toernooizege in Lyon en 7-1 indoor dit seizoen.",
         "<strong>De onderlinge duels zijn spannend.</strong> Musetti won drie van de vijf partijen, en ook het eerste indoorduel.",
         "<strong>Zverev begint koud.</strong> Het is zijn eerste partij in Parijs, tegen iemand die de baan al kent. Op een snelle baan kan één break of tiebreak een set beslissen."])}
<p><strong>Het risico:</strong> Zverev is de nummer één van de wereld en won in Wenen vorig jaar nog in twee sets van Musetti. Serveert hij zoals hij kan, dan is een 2-0 goed mogelijk. Durf je meer? Musetti wint staat op 3,05.</p>"""

content3 = f"""<h3><strong>Tomás Martín Etcheverry – Alex de Minaur (Court 2, ± 14:00 uur)</strong></h3>
<p><strong>De situatie.</strong> Voor De Minaur (achtste reekshoofd) is dit de belangrijkste partij van de dag. Met een zege passeert hij Jódar in de race naar Turijn en neemt hij de negende plek over, nu de laatste plaats voor de ATP Finals. Indoor is hij dit jaar bijna onklopbaar: 9 zeges en 1 nederlaag. Hij won Rotterdam en haalde zondag de finale in Wenen, waar hij onder anderen Zverev versloeg.</p>
<p>Etcheverry (nummer 31) won gisteren na 2 uur en 50 minuten van Andrey Rublev, de langste partij van de dag. Daarmee stopte hij een reeks van zes nederlagen op rij. Hij sloeg 20 aces, maar op hardcourt is zijn balans dit jaar matig: 9 zeges en 14 nederlagen.</p>
<p><strong>Onderling.</strong> De Minaur leidt met 2-1. Op hardcourt won hij het enige duel: 6-1, 6-4 in de United Cup van 2025.</p>
<p><strong>Onze tip: minder dan 2,5 sets (1,43).</strong></p>
{markt("totaal aantal sets, minder dan 2,5. De tip is goed als de wedstrijd in twee sets eindigt, ongeacht wie er wint. Komt er een derde set, dan is de tip verloren.")}
{waarom(["<strong>De Minaur is indoor in topvorm.</strong> 9-1 dit seizoen, met de finale in Wenen van zondag.",
         "<strong>Etcheverry heeft een lange partij in de benen.</strong> Bijna drie uur tegen Rublev, en daarvoor zes nederlagen op rij.",
         "<strong>Het verschil op hardcourt is groot.</strong> De Minaur staat op 30-12, Etcheverry op 9-14. Een driesetter ligt minder voor de hand dan een duidelijke zege."])}
<p><strong>Het risico:</strong> Etcheverry serveerde gisteren sterk (20 aces, geen enkele break tegen). Op deze snelle baan kan hij een set naar zich toe trekken via een tiebreak. Liever alleen op de winnaar? De Minaur wint staat op 1,24.</p>
<h3><strong>Arthur Fils – Tomáš Macháč (centercourt, niet voor 20:30 uur)</strong></h3>
<p><strong>De situatie.</strong> Fils (nummer 7, zesde reekshoofd) speelt zijn eerste partij in Parijs, voor eigen publiek. Hij staat zevende in de race naar Turijn en is zeker van de ATP Finals als hij de kwartfinale haalt. Zijn seizoen is sterk: 38 zeges en 15 nederlagen. In Basel gaf hij in de kwartfinale tegen Fritz op met pijn aan zijn linkerbeen, maar volgens Fils was dat een spierprobleem en uit voorzorg. Zijn deelname in Parijs noemde hij '100 procent' zeker.</p>
<p>Macháč (nummer 69) kwam via de kwalificatie in de hoofdtabel en won maandag in twee sets van wildcard Jacquet. De Tsjech speelt een wisselend jaar: 17 zeges en 17 nederlagen, op hardcourt 11-12.</p>
<p><strong>Onderling.</strong> Fils won het enige duel, in 2024 op gras in Halle: 6-4, 6-4.</p>
<p><strong>Onze tip: Fils wint (1,49).</strong></p>
{markt("winnaar van de wedstrijd. Fils moet de partij winnen, in twee of drie sets.")}
{waarom(["<strong>Fils speelt om Turijn.</strong> Met twee zeges is hij zeker van de ATP Finals.",
         "<strong>Het publiek staat achter hem.</strong> Hij speelt in de avondsessie op de centercourt, in een volle arena.",
         "<strong>Het niveauverschil is groot.</strong> Fils staat op 38-15 dit seizoen, Macháč op 17-17."])}
<p><strong>Het risico:</strong> de opgave in Basel is pas negen dagen oud. Als het been toch opspeelt, wordt dit lastig. Macháč heeft al drie partijen in de benen en serveert goed op deze snelle baan. Liever meer zekerheid? Fils wint minstens één set staat op 1,19.</p>
<h3><strong>Combinatie woensdag 4 november</strong></h3>
<p>Alle vier de tips samen: 1,44 × 1,78 × 1,43 × 1,49 = <strong>± {COMBI}</strong>. Een inzet van €10 levert bij deze combinatie ongeveer €55 op. Hoe meer tips in een combinatie, hoe groter de kans dat er één misgaat. Wil je minder risico, speel de tips dan los, of combineer alleen Tien en De Minaur – Etcheverry (samen ± 2,06).</p>
<h3><strong>De andere partijen van vandaag</strong></h3>
<p>Zonder extra tip van ons: om 11:00 uur opent Frances Tiafoe op de centercourt tegen Quentin Halys, die gisteren geen enkele keer werd gebroken. Op hetzelfde moment speelt Arthur Rinderknech op Court 1 tegen Mattia Bellucci. Daniil Medvedev begint tegen Ignacio Buse en won 7 van zijn laatste 8 indoorpartijen. Djokovic speelt na Zverev – Musetti tegen kwalificant Rinky Hijikata, maar stond gisteren 2 uur en 35 minuten op de baan. Carlos Alcaraz opent de avondsessie (niet voor 19:00 uur) tegen Alex Michelsen, die in Tokyo een set van hem won. Verder spelen Paul – Mérida, Fritz – Molcan, Khachanov – Borges, Humbert – Berrettini en Struff – Tirante. De strijd om Turijn volg je in {L['turijn']}.</p>
<h3><strong>Wat betekenen deze weddenschappen?</strong></h3>
<p><strong>Winnaar.</strong> De speler moet de wedstrijd winnen, in twee of drie sets.</p>
<p><strong>Wint speler minstens één set.</strong> De tip is goed zodra de speler één set wint, ongeacht wie de wedstrijd wint.</p>
<p><strong>Totaal aantal sets, minder dan 2,5.</strong> De wedstrijd moet in twee sets eindigen. Wie er wint, maakt niet uit.</p>
<p>Geeft een speler op, dan hangt het van de regels van de bookmaker af wat er met je weddenschap gebeurt. Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit; lees {L['legaal']}. Benieuwd hoe lang een partij duurt? Lees {L['duur']}. Meer tips vind je op onze pagina {L['tips']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wat zijn de beste Paris Masters-voorspellingen van vandaag?</strong><br>Tien wint van Van Assche (1,44), Musetti wint minstens één set van Zverev (1,78), De Minaur – Etcheverry eindigt in twee sets (1,43) en Fils wint van Macháč (1,49). Gecombineerd is de odd ongeveer {COMBI}.</p>
<p><strong>Hoe deden de tennistips van gisteren het?</strong><br>Drie van de vier waren goed: Paul won, Vacherot pakte een set van Djokovic en Michelsen won van Lehečka. Jódar verloor in twee sets van Ruud.</p>
<p><strong>Hoe laat speelt Zverev vandaag?</strong><br>Niet voor 13:30 uur op de centercourt, tegen Lorenzo Musetti. Daarna volgt Djokovic – Hijikata.</p>
<p><strong>Hoe laat speelt Alcaraz vandaag?</strong><br>In de avondsessie op de centercourt, niet voor 19:00 uur, tegen Alex Michelsen. Daarna, niet voor 20:30 uur, speelt Fils tegen Macháč.</p>
<p><strong>Wie wint Zverev – Musetti?</strong><br>De bookmakers zien Zverev als favoriet, maar Musetti is indoor in vorm en won drie van hun vijf duels. Wij verwachten dat Musetti minstens één set wint.</p>
<p><strong>Waar kan ik de Paris Masters live kijken?</strong><br>Op Ziggo Sport. Gratis kijken kan ook; hoe, lees je in {L['kijk']}.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

WEDTIPS = {"wedstrijd-1": "Combinatie: alle vier de tips",
           "wedtip-1-2": "Tien wint + Musetti wint minstens één set + De Minaur vs Etcheverry minder dan 2.5 sets + Fils wint",
           "quotering-wedtip-1": "5.46",
           "wedstrijd-2": "Van Assche vs Tien", "wedtip-2-2": "Tien wint", "quotering-wedtip-2": "1.44",
           "wedstrijd-3": "Zverev vs Musetti", "wedtip-3-2": "Musetti wint minstens één set", "quotering-wedtip-3": "1.78",
           "wedtip-4-2": "Fils wint van Macháč", "quotering-wedtip-4": "1.49"}

if __name__ == "__main__":
    import re
    if "--velden" in sys.argv:
        import lk_webflow as WF
        it = WF._req("GET", f"{WF.WF_API}/collections/{WF.NIEUWS_COLLECTION}/items?slug={SLUG}")["items"][0]
        fd = {"tennis": True, "bookmaker-wedtips": BOOKMAKER_711, "datum-tijd-van-wedstrijd": "2026-11-04T11:30:00.000Z", **WEDTIPS}
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
    assert abs(1.44 * 1.43 - 2.06) < 0.01 and round(10 * p) == 55
    assert [t[4] for t in TIPS] == ["1,44", "1,78", "1,43", "1,49"]
    assert alles.count("<p><strong>De markt:</strong>") == 4
    assert "<h2" not in alles and "<h4" not in alles and "betcity" not in alles.lower() and "/go/" not in alles
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    assert content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    print("dry run ok")
