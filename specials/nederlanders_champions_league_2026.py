# -*- coding: utf-8 -*-
"""Los artikel: Nederlanders in de Champions League 2026/27 (selecties, nationaliteiten, speeldag 1 en speeldag 2
via API-Football; 9 okt 2026).
  python3 specials/nederlanders_champions_league_2026.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Nederlanders in de Champions League 2026/27: alle spelers en clubs"
SLUG = "nederlanders-in-de-champions-league-2026-27"
SAMENVATTING = ("28 Nederlanders spelen in 2026/27 bij buitenlandse clubs in de Champions League, plus de selecties van "
                "PSV en Feyenoord. Het complete overzicht.")
RUBRIEK_CL = "669fc3ef5bd43f5dfd4b9146"
COMPETITIE_CL = "65de4adac046f4488dfdebc2"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in koppen)
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}><thead><tr>{kop}</tr></thead><tbody>{body}</tbody></table>"


C = {"Liverpool": "liverpool", "Aston Villa": "aston-villa", "AS Roma": "as-roma", "Manchester United": "manchester-united",
     "Napoli": "napoli", "Fenerbahçe": "fenerbahce", "LASK": "lask-linz", "Lille": "lille", "Real Madrid": "real-madrid",
     "FC Barcelona": "fc-barcelona", "Arsenal": "arsenal", "Borussia Dortmund": "borussia-dortmund",
     "VfB Stuttgart": "stuttgart", "RB Leipzig": "rb-leipzig", "Como": "como", "FC Porto": "fc-porto",
     "Viking": "viking", "PSV": "psv", "Feyenoord": "feyenoord"}
_g = set()


def club(c):
    if c in _g:
        return c
    _g.add(c)
    return f'<a href="/clubs/{C[c]}">{c}</a>'


SPELERS = [
    ("Virgil van Dijk", "Liverpool", "Verdediger", "35"),
    ("Jeremie Frimpong", "Liverpool", "Verdediger", "25"),
    ("Ryan Gravenberch", "Liverpool", "Middenvelder", "24"),
    ("Cody Gakpo", "Liverpool", "Aanvaller", "27"),
    ("Marco Bizot", "Aston Villa", "Doelman", "35"),
    ("Ian Maatsen", "Aston Villa", "Verdediger", "24"),
    ("Lamare Bogarde", "Aston Villa", "Middenvelder", "22"),
    ("Devyne Rensch", "AS Roma", "Verdediger", "23"),
    ("Marten de Roon", "AS Roma", "Middenvelder", "35"),
    ("Donyell Malen", "AS Roma", "Aanvaller", "27"),
    ("Matthijs de Ligt", "Manchester United", "Verdediger", "27"),
    ("Joshua Zirkzee", "Manchester United", "Aanvaller", "25"),
    ("Sam Beukema", "Napoli", "Verdediger", "27"),
    ("Noa Lang", "Napoli", "Aanvaller", "27"),
    ("Nathan Aké", "Fenerbahçe", "Verdediger", "31"),
    ("Jayden Oosterwolde", "Fenerbahçe", "Verdediger", "25"),
    ("Xavier Mbuyamba", "LASK", "Verdediger", "24"),
    ("Melayro Bogarde", "LASK", "Verdediger", "24"),
    ("Denzel Dumfries", "Real Madrid", "Verdediger", "30"),
    ("Frenkie de Jong", "FC Barcelona", "Middenvelder", "29"),
    ("Jurriën Timber", "Arsenal", "Verdediger", "25"),
    ("Calvin Verdonk", "Lille", "Verdediger", "29"),
    ("Joey Veerman", "Borussia Dortmund", "Middenvelder", "27"),
    ("Ramon Hendriks", "VfB Stuttgart", "Verdediger", "25"),
    ("Ezechiel Banzuzi", "RB Leipzig", "Middenvelder", "21"),
    ("Jayden Addai", "Como", "Aanvaller", "21"),
    ("Pablo Rosario", "FC Porto", "Middenvelder", "29"),
    ("Romano Postema", "Viking", "Aanvaller", "24"),
]

content = f"""<p><strong>In de Champions League 2026/27 spelen 28 Nederlanders bij buitenlandse clubs, verdeeld over zeventien clubs. Liverpool heeft er met Virgil van Dijk, Jeremie Frimpong, Ryan Gravenberch en Cody Gakpo de meeste. Aston Villa en AS Roma volgen met drie. Daarnaast doen PSV en Feyenoord mee, met samen ruim tien Nederlanders in de selectie.</strong></p>
<p>De <a href="/competities/champions-league">Champions League</a> is ook dit seizoen een toernooi met veel Nederlandse inbreng. Van aanvoerder Van Dijk bij Liverpool tot twee verdedigers bij het Oostenrijkse LASK: bij meer dan de helft van de 36 deelnemers staat minstens één Nederlander in de selectie. In dit overzicht vind je alle spelers, wat ze op de eerste speeldag lieten zien, wie er geblesseerd is en welke Nederlanders elkaar op speeldag 2 tegenkomen.</p>
<h3><strong>Alle Nederlanders bij buitenlandse clubs</strong></h3>
{tabel(["Speler", "Club", "Positie", "Leeftijd"], [(s, club(c), p, a) for s, c, p, a in SPELERS])}
<p><em>Alleen spelers met de Nederlandse voetbalnationaliteit. Selecties gecontroleerd op 9 oktober 2026, na speeldag 1.</em></p>
<h3><strong>Speeldag 2: hier spelen de Nederlanders</strong></h3>
<p>Speeldag 2 van de competitiefase staat op dinsdag 13 en woensdag 14 oktober op het programma. Er zitten een paar echte Nederlandse onderonsjes tussen.</p>
{tabel(["Wedstrijd", "Nederlanders", "Aftrap"], [
    ("Arsenal – Lille", "Timber / Verdonk", "di 13 okt, 21:00"),
    ("RB Leipzig – PSV", "Banzuzi / PSV-selectie", "di 13 okt, 21:00"),
    ("Atlético Madrid – Manchester United", "Zirkzee, De Ligt", "di 13 okt, 21:00"),
    ("Villarreal – Napoli", "Lang, Beukema", "di 13 okt, 21:00"),
    ("Galatasaray – FC Barcelona", "De Jong", "di 13 okt, 21:00"),
    ("Viking – Bayern München", "Postema", "di 13 okt, 21:00"),
    ("Feyenoord – Como", "Feyenoord-selectie / Addai", "wo 14 okt, 18:45"),
    ("LASK – Liverpool", "Mbuyamba, M. Bogarde / Van Dijk, Frimpong, Gravenberch, Gakpo", "wo 14 okt, 18:45"),
    ("Aston Villa – Fenerbahçe", "Maatsen, Bizot, L. Bogarde / Aké, Oosterwolde", "wo 14 okt, 21:00"),
    ("Bodø/Glimt – Borussia Dortmund", "Veerman", "wo 14 okt, 21:00"),
    ("AS Roma – Real Madrid", "Malen, Rensch, De Roon / Dumfries", "wo 14 okt, 21:00"),
    ("Real Betis – FC Porto", "Rosario", "wo 14 okt, 21:00"),
    ("Slovan Bratislava – VfB Stuttgart", "Hendriks", "wo 14 okt, 21:00"),
])}"""

content2 = f"""<h3><strong>PSV en Feyenoord: de Nederlandse clubs</strong></h3>
<p>{club("PSV")} begon de competitiefase met een 1-1 gelijkspel tegen Shakhtar Donetsk. Guus Til, Armando Obispo, Lutsharel Geertruida en Ruben van Bommel speelden de hele wedstrijd; Obispo gaf de assist bij de treffer van Sergiño Dest. Ook Sven Mijnans en Ryan Flamingo kwamen in actie. Joey Veerman zit er niet meer bij: hij vertrok deze zomer naar Borussia Dortmund.</p>
<p>{club("Feyenoord")} kreeg een zware start: in Barcelona werd het 5-1. Sem Steijn maakte de Rotterdamse eer. Jeremiah St. Juste, Givairo Read en Gjivai Zechiël speelden de volledige wedstrijd. Op speeldag 2 ontvangt Feyenoord Como, waar met Jayden Addai ook een Nederlander onder contract staat.</p>
<h3><strong>Liverpool: vier Nederlanders onder één dak</strong></h3>
<p>Geen buitenlandse club heeft zoveel Nederlanders als {club("Liverpool")}. Aanvoerder <strong>Virgil van Dijk</strong> speelde de 2-1 zege op Atlético Madrid volledig. <strong>Jeremie Frimpong</strong> en <strong>Ryan Gravenberch</strong> kwamen in de tweede helft in het veld. <strong>Cody Gakpo</strong> ontbrak met een enkelblessure; of hij tegen LASK speelt, is nog onzeker. Dat duel in Linz is extra interessant, want bij LASK spelen ook twee Nederlanders.</p>
<h3><strong>Aston Villa en AS Roma: drie Nederlanders</strong></h3>
<p>Bij {club("Aston Villa")} speelde <strong>Ian Maatsen</strong> de 2-3 zege bij Club Brugge volledig. Inmiddels heeft hij wel last van zijn enkel. <strong>Lamare Bogarde</strong> viel in, en doelman <strong>Marco Bizot</strong> is de reservekeeper. Op speeldag 2 komt Fenerbahçe naar Birmingham, met Nathan Aké.</p>
<p>{club("AS Roma")} speelde op speeldag 1 met 1-1 gelijk bij Fenerbahçe. <strong>Donyell Malen</strong> gaf daarin een assist en <strong>Devyne Rensch</strong> stond in de basis. <strong>Marten de Roon</strong> kwam in de slotfase in het veld. Op speeldag 2 wacht een kraker tegen Real Madrid, de club van Denzel Dumfries.</p>
<h3><strong>Real Madrid, Barcelona en Arsenal</strong></h3>
<p><strong>Denzel Dumfries</strong> speelde bij {club("Real Madrid")} zijn eerste Champions League-wedstrijd voor de club meteen tegen zijn oude werkgever: de 2-1 zege op Internazionale speelde hij volledig. Bij {club("FC Barcelona")} is <strong>Frenkie de Jong</strong> geblesseerd aan zijn knie; hij miste de 5-1 tegen Feyenoord. <strong>Jurriën Timber</strong> kwam bij de 0-1 zege van {club("Arsenal")} bij Napoli niet in actie, maar wordt tegen Lille terugverwacht.</p>
<h3><strong>Manchester United en Napoli</strong></h3>
<p>Bij {club("Manchester United")} kwam <strong>Joshua Zirkzee</strong> in de 4-0 zege op Sabah tot 26 minuten speeltijd. <strong>Matthijs de Ligt</strong> is na een rugoperatie nog niet fit. Bij {club("Napoli")} kwamen <strong>Noa Lang</strong> en <strong>Sam Beukema</strong> op speeldag 1 niet in actie bij de 0-1 nederlaag tegen Arsenal.</p>"""

content3 = f"""<h3><strong>Bundesliga: Veerman, Banzuzi en Hendriks</strong></h3>
<p><strong>Joey Veerman</strong> maakte bij {club("Borussia Dortmund")} een sterke start in de Champions League: hij speelde de 3-2 zege op Villarreal volledig. <strong>Ezechiel Banzuzi</strong> kwam bij {club("RB Leipzig")} een halfuur in actie bij de 4-1 nederlaag bij Como. Op speeldag 2 neemt hij het met Leipzig op tegen PSV. <strong>Ramon Hendriks</strong> speelde negentien minuten mee bij de 3-1 zege van {club("VfB Stuttgart")} op Viking.</p>
<h3><strong>Fenerbahçe, LASK en de andere clubs</strong></h3>
<p>{club("Fenerbahçe")} plaatste zich via de voorrondes en daar was <strong>Nathan Aké</strong> elke wedstrijd een vaste kracht. Ook tegen Roma speelde hij de volle negentig minuten. <strong>Jayden Oosterwolde</strong> is uitgeschakeld met een achillespeesblessure.</p>
<p>Bij {club("LASK")} spelen twee Nederlandse verdedigers. <strong>Xavier Mbuyamba</strong> en <strong>Melayro Bogarde</strong> stonden allebei de hele wedstrijd op het veld bij de 1-0 nederlaag bij AEK Athene. <strong>Pablo Rosario</strong> speelde bij {club("FC Porto")} de 0-2 nederlaag tegen Manchester City volledig.</p>
<p>Bij {club("Lille")} is <strong>Calvin Verdonk</strong> de Nederlander in de selectie; hij kwam tegen Real Betis niet in actie. <strong>Jayden Addai</strong> ({club("Como")}) en <strong>Romano Postema</strong> ({club("Viking")}) wachten ook nog op hun eerste minuten in de competitiefase.</p>
<h3><strong>Geblesseerde Nederlanders</strong></h3>
<ul><li><strong>Frenkie de Jong</strong> (FC Barcelona): knieblessure</li><li><strong>Matthijs de Ligt</strong> (Manchester United): herstellend van een rugoperatie</li><li><strong>Jayden Oosterwolde</strong> (Fenerbahçe): achillespeesblessure</li><li><strong>Ian Maatsen</strong> (Aston Villa): enkelblessure</li><li><strong>Cody Gakpo</strong> (Liverpool): enkelblessure, twijfelachtig voor speeldag 2</li></ul>
<h3><strong>Geboren in Nederland, international van een ander land</strong></h3>
<p>Een aantal spelers in de Champions League is in Nederland geboren of opgeleid, maar komt uit voor een ander land. Zij staan niet in het overzicht hierboven.</p>
<ul><li><strong>Dean Huijsen</strong> (Real Madrid): geboren in Amsterdam, Spaans international. Hij speelde naast Dumfries de volle 90 minuten tegen Inter.</li><li><strong>Noussair Mazraoui</strong> (Manchester United): geboren in Leiderdorp, opgeleid bij Ajax, international van Marokko.</li><li><strong>Sergiño Dest</strong> (PSV): geboren in Almere, international van de Verenigde Staten. Hij scoorde tegen Shakhtar.</li><li><strong>Başar Önal</strong> (Lille): geboren in Doetinchem, met de Turkse nationaliteit.</li><li><strong>Oğuz Aydın</strong> (Fenerbahçe): geboren in Den Haag, Turks international.</li></ul>
<h3><strong>Champions League kijken in Nederland</strong></h3>
<p>Alle wedstrijden van de Champions League zijn in Nederland te zien bij <a href="/zenders/ziggo-sport">Ziggo Sport</a>. Per wedstrijd zie je in de tv-gids van Ziggo Sport op welk kanaal het duel wordt uitgezonden.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoeveel Nederlanders spelen er in de Champions League?</strong><br>Bij buitenlandse clubs zijn dat er 28, verdeeld over zeventien clubs. Daarnaast hebben PSV en Feyenoord samen ruim tien Nederlanders in de selectie.</p>
<p><strong>Welke buitenlandse club heeft de meeste Nederlanders?</strong><br>Liverpool, met Virgil van Dijk, Jeremie Frimpong, Ryan Gravenberch en Cody Gakpo.</p>
<p><strong>Welke Nederlandse clubs spelen in de Champions League?</strong><br>PSV en Feyenoord. PSV speelde op speeldag 1 met 1-1 gelijk tegen Shakhtar Donetsk. Feyenoord verloor met 5-1 bij Barcelona.</p>
<p><strong>Welke Nederlanders treffen elkaar op speeldag 2?</strong><br>Onder meer bij LASK – Liverpool, Aston Villa – Fenerbahçe, AS Roma – Real Madrid, Arsenal – Lille en RB Leipzig – PSV.</p>
<p><strong>Is Dean Huijsen een Nederlander?</strong><br>Hij is geboren in Amsterdam, maar speelt voor het Spaanse nationale elftal.</p>
<p><em>Gokken is alleen toegestaan voor personen van 18 jaar en ouder. Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_CL, "competitie": COMPETITIE_CL,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting"); sys.exit()
    print("item:", WF.create_live(fd))
