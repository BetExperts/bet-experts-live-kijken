# -*- coding: utf-8 -*-
"""Los artikel: Nederlanders in de Süper Lig 2026/27 (nationaliteiten en selecties via API-Football,
twijfelgevallen nagezocht; 9 okt 2026).
  python3 specials/nederlanders_super_lig_2026.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Nederlanders in de Süper Lig 2026/27: alle spelers in Turkije"
SLUG = "nederlanders-in-de-super-lig-2026-27"
SAMENVATTING = ("Tien Nederlanders spelen in 2026/27 in de Süper Lig, verdeeld over zeven clubs. Van Nathan Aké bij "
                "Fenerbahçe tot Ernest Poku bij Beşiktaş.")
RUBRIEK_NIEUWS = "651be5190a7dba016817ccf0"
COMPETITIE_SUPER_LIG = "66ed7d481dc85d2ca649595c"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in koppen)
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}><thead><tr>{kop}</tr></thead><tbody>{body}</tbody></table>"


C = {"Fenerbahçe": "fenerbahce", "Beşiktaş": "besiktas", "Trabzonspor": "trabzonspor", "Kasımpaşa": "kasimpasa",
     "Gaziantep FK": "gaziantep", "Erzurumspor": "erzurumspor", "Samsunspor": "samsunspor"}
_g = set()


def club(c):
    if c in _g:
        return c
    _g.add(c)
    return f'<a href="/clubs/{C[c]}">{c}</a>'


SPELERS = [
    ("Nathan Aké", "Fenerbahçe", "Verdediger", "31"),
    ("Jayden Oosterwolde", "Fenerbahçe", "Verdediger", "25"),
    ("Ernest Poku", "Beşiktaş", "Aanvaller", "22"),
    ("Sidny Lopes Cabral", "Trabzonspor", "Verdediger", "24"),
    ("Godfried Frimpong", "Kasımpaşa", "Verdediger", "27"),
    ("Sontje Hansen", "Gaziantep FK", "Aanvaller", "24"),
    ("Gyrano Kerk", "Erzurumspor", "Aanvaller", "30"),
    ("İlkan Sever", "Erzurumspor", "Aanvaller", "21"),
    ("Bilal Bayazıt", "Samsunspor", "Doelman", "27"),
    ("Elayis Tavsan", "Samsunspor", "Aanvaller", "25"),
]
L = "/nieuws/"

content = f"""<p><strong>In het seizoen 2026/27 spelen tien Nederlanders in de Süper Lig, verdeeld over zeven clubs. Nathan Aké is bij Fenerbahçe de bekendste naam en ook de enige Nederlander die elke week in de basis staat. Fenerbahçe, Erzurumspor en Samsunspor hebben elk twee Nederlanders in de selectie.</strong></p>
<p>Turkije is al jaren een populaire bestemming voor Nederlandse voetballers. De grote Istanbulse clubs betalen goed, de stadions zitten vol en de competitie levert regelmatig Europees voetbal op. Daarnaast lopen er in de <a href="/competities/super-lig">Süper Lig</a> veel spelers rond die in Nederland zijn geboren en opgeleid, maar voor Turkije of een ander land uitkomen. In dit overzicht lees je wie er voor Nederland speelt, hoe hun club ervoor staat en wie er Nederlandse roots heeft.</p>
<h3><strong>Alle Nederlanders in de Süper Lig op een rij</strong></h3>
{tabel(["Speler", "Club", "Positie", "Leeftijd"], [(s, club(c), p, a) for s, c, p, a in SPELERS])}
<p><em>Alleen spelers met de Nederlandse voetbalnationaliteit. Selecties gecontroleerd op 9 oktober 2026.</em></p>
<h3><strong>Nederlanders in speelronde 7</strong></h3>
{tabel(["Wedstrijd", "Nederlander(s)", "Aftrap"], [
    (f'<a href="{L}galatasaray-kasimpasa-live-gratis-kijken-09-10-2026">Galatasaray – Kasımpaşa</a>', "Frimpong", "vr 9 okt, 19:00"),
    (f'<a href="{L}alanyaspor-erzurumspor-live-gratis-kijken-10-10-2026">Alanyaspor – Erzurumspor</a>', "Kerk, Sever", "za 10 okt, 15:00"),
    (f'<a href="{L}samsunspor-trabzonspor-live-gratis-kijken-10-10-2026">Samsunspor – Trabzonspor</a>', "Bayazıt, Lopes Cabral", "za 10 okt, 15:00"),
    (f'<a href="{L}rizespor-fenerbahce-live-gratis-kijken-10-10-2026">Rizespor – Fenerbahçe</a>', "Aké", "za 10 okt, 18:00"),
    (f'<a href="{L}gaziantep-corum-fk-live-gratis-kijken-11-10-2026">Gaziantep FK – Çorum FK</a>', "Hansen", "zo 11 okt, 15:00"),
    (f'<a href="{L}besiktas-kocaelispor-live-gratis-kijken-11-10-2026">Beşiktaş – Kocaelispor</a>', "Poku", "zo 11 okt, 18:00"),
])}
<p>Oosterwolde (Fenerbahçe) en Tavsan (Samsunspor) zijn geblesseerd en spelen dit weekend niet mee.</p>"""

content2 = f"""<h3><strong>Fenerbahçe: Aké als vaste waarde</strong></h3>
<p><strong>Nathan Aké</strong> is de grootste Nederlandse naam in Turkije. De Hagenaar maakte naam in Engeland, waar hij onder meer voor Chelsea, Bournemouth en Manchester City speelde. Bij Fenerbahçe is hij direct een vaste kracht: hij speelde alle competitieduels van dit seizoen volledig. Met zijn ervaring en zijn linkervoet is hij belangrijk in de opbouw van achteruit.</p>
<p>Zijn landgenoot <strong>Jayden Oosterwolde</strong>, oud-speler van FC Twente, staat momenteel aan de kant met een achillespeesblessure. Fenerbahçe staat na zes speelrondes zesde, drie punten achter koploper Amed.</p>
<h3><strong>Ernest Poku: talent bij Beşiktaş</strong></h3>
<p>De 22-jarige <strong>Ernest Poku</strong> brak door bij AZ en speelt nu bij Beşiktaş, de nummer drie van de competitie. De snelle buitenspeler moet in Istanbul nog vechten voor een vaste basisplaats. Met Beşiktaş speelt hij in een team dat dit seizoen meedoet om de bovenste plaatsen.</p>
<h3><strong>Lopes Cabral en Frimpong: twee linksbacks</strong></h3>
<p><strong>Sidny Lopes Cabral</strong> uit Rotterdam kwam via Excelsior en Benfica bij Trabzonspor terecht. De linksback speelde dit seizoen in alle competitieduels mee, al was hij niet altijd basisspeler. Trabzonspor staat zevende, met evenveel punten als Fenerbahçe.</p>
<p><strong>Godfried Frimpong</strong> speelt sinds de zomer van 2025 bij Kasımpaşa. Hij kwam transfervrij over van het Portugese Moreirense. Dit seizoen moet de verdediger nog zijn eerste competitieminuten maken. Kasımpaşa staat achtste.</p>
<h3><strong>Erzurumspor, Gaziantep en Samsunspor</strong></h3>
<p>Bij promovendus Erzurumspor spelen twee Nederlandse aanvallers. <strong>Gyrano Kerk</strong> (30), oud-speler van FC Utrecht en Royal Antwerp, is de routinier en kwam vier keer in actie. De 21-jarige <strong>İlkan Sever</strong> uit Enschede maakte zijn debuut als invaller. Erzurumspor staat veertiende.</p>
<p><strong>Sontje Hansen</strong>, opgeleid bij Ajax en later actief bij NEC, speelt bij Gaziantep FK. De buitenspeler kwam vier keer in actie, waarvan één keer als basisspeler. Gaziantep staat tiende.</p>
<p>Samsunspor heeft twee Nederlanders, maar beiden spelen voorlopig niet. Doelman <strong>Bilal Bayazıt</strong>, eerder onder meer keeper van Vitesse, is tweede keus en kwam nog niet in actie. <strong>Elayis Tavsan</strong>, die in januari 2026 naar Samsunspor kwam, heeft een spierblessure. De club staat op een teleurstellende zestiende plaats.</p>"""

content3 = f"""<h3><strong>Geboren in Nederland, international van een ander land</strong></h3>
<p>Naast de tien Nederlanders spelen er in de Süper Lig nog veel meer spelers die in Nederland zijn geboren. Ze staan niet in het overzicht hierboven, omdat ze voor een ander land uitkomen.</p>
<ul><li><strong>Orkun Kökçü</strong> (Beşiktaş): geboren in Haarlem, opgeleid bij Feyenoord, Turks international.</li><li><strong>Oğuz Aydın</strong> (Fenerbahçe): geboren in Den Haag, Turks international.</li><li><strong>Halil Dervişoğlu</strong> (Gaziantep FK): geboren in Rotterdam, eerder actief bij Sparta, Turks international.</li><li><strong>Deniz Türüç</strong> (Konyaspor): geboren in Enschede, Turks international.</li><li><strong>Yusuf Barası</strong> (Eyüpspor): geboren in Alkmaar, opgeleid bij AZ, komt uit voor Turkije.</li><li><strong>Anfernee Dijksteel</strong> (Kocaelispor): geboren in Amsterdam, international van Suriname.</li><li><strong>Juninho Bacuna</strong> (Gaziantep FK): geboren in Groningen, international van Curaçao.</li></ul>
<h3><strong>Vertrokken: Anthony Musaba</strong></h3>
<p>Anthony Musaba speelde vorig seizoen nog in Turkije, eerst bij Samsunspor en vanaf januari 2026 bij Fenerbahçe. Door een blessure kwam hij daar weinig aan spelen. Op 19 augustus verhuurde Fenerbahçe hem voor een seizoen aan Norwich City in de Championship.</p>
<h3><strong>Süper Lig kijken in Nederland</strong></h3>
<p>De Süper Lig is niet op de Nederlandse televisie te zien. Wel kun je veel wedstrijden volgen via de livestreams van <a href="/zenders/toto">TOTO</a> en <a href="/zenders/bet365">Bet365</a>, met een gratis account (18+). Welke wedstrijden dit weekend live te zien zijn, lees je in ons overzicht van <a href="/nieuws/super-lig-speelronde-7-op-tv-9-oktober-2026">Süper Lig speelronde 7 op tv</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoeveel Nederlanders spelen er in de Süper Lig?</strong><br>In 2026/27 zijn dat er tien, verdeeld over zeven clubs.</p>
<p><strong>Welke Nederlanders spelen bij Fenerbahçe?</strong><br>Nathan Aké en Jayden Oosterwolde. Oosterwolde is op dit moment geblesseerd.</p>
<p><strong>Speelt er een Nederlander bij Beşiktaş?</strong><br>Ja, aanvaller Ernest Poku. Ook Orkun Kökçü speelt bij Beşiktaş; hij is geboren in Haarlem, maar komt uit voor Turkije.</p>
<p><strong>Speelt er een Nederlander bij Galatasaray?</strong><br>Nee, Galatasaray heeft dit seizoen geen Nederlander in de selectie.</p>
<p><strong>Hoe kijk ik de Süper Lig in Nederland?</strong><br>Via de livestreams van TOTO en Bet365, met een gratis account (18+). Op de Nederlandse tv is de competitie niet te zien.</p>
<p><em>Gokken is alleen toegestaan voor personen van 18 jaar en ouder. Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_NIEUWS, "competitie": COMPETITIE_SUPER_LIG,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting"); sys.exit()
    print("item:", WF.create_live(fd))
