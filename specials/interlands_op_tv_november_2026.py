# -*- coding: utf-8 -*-
"""Los artikel: alle interlands van de Nations League (speeldag 5 en 6) op tv, per dag, 12 t/m 17 november 2026 (9-11-2026).
Bronnen:
- Speelschema, tijden (CET = Nederlandse tijd) en groepen: UEFA 'fixtures and results by team' (geraadpleegd 9-11-2026)
  https://www.uefa.com/uefanationsleague/news/02a2-1fea7079900a-801b2c5f6c9e-1000--2026-27-uefa-nations-league-league-phase-fixtures-and-results-by-team/
  Gecontroleerd tegen de eigen API-proxy (/api/fixtures/nations-league, 50 van de 52 duels; de twee ontbrekende duels van
  di 17-11, Israël – Oostenrijk en Bosnië-Herzegovina – Roemenië, staan wel bij UEFA) en de Kambi-feed van 711 (speeldag 5).
- Stand na speeldag 4: eigen API (/api/standings/nations-league, API-Football); groep A2 ook in specials/nations_league_2028_feiten.md.
- Zenders: Ziggo-programma Nations League (ziggo.nl/entertainment/sport/voetbal/nations-league/programma, 9-11-2026):
  per duel 'Ziggo Sport n', 'Switch op Ziggo Sport 1' of '-' (= geen Nederlandse uitzending; 17 duels).
  Ziggo 'kijken'-pagina: Switch op Ziggo Sport (kanaal 14, standaard), Ziggo Sport Totaal (401-406) = zelf kiezen, Ziggo GO.
  Eigen zenderconfig data/tv_zenders.json: Ziggo Sport = 'UEFA Nations League (zonder Nederlands elftal)', NOS = Oranje.
  Oranje op NPO 3 + NOS-stream: NOS (feitenbrief) en Ziggo-programma.
- Bet365: bet365_streams.status() voor alle 50 API-duels = 'nee' (schema 4-11, voetbal t/m 1-12): geen enkel
  Nations League-duel in het streamschema, dus geen Bet365-stream beloofd.
- Odds 711 (Kambi sevelevnl, uefa_nations_league listView), afgelezen ma 9-11-2026 ±17:00.
Bewust NIET gebruikt (onbevestigd): oefeninterlands van Europese landen (o.a. Litouwen – Suriname alleen in de API, geen
officiële bevestiging), stadions buiten de Oranje-duels, wat 'Switch' precies uitzendt per wedstrijd (Ziggo legt het niet uit),
kanaalnummers per Totaal-zender.
  python3 specials/interlands_op_tv_november_2026.py   (dry run)"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

SLUG = "interlands-op-tv-12-tot-en-met-17-november-2026"
RUBRIEK = "66d6d655bc312d5c0e834ecd"   # Oranje/interlands
TITEL = "Interlands op tv: alle duels van 12 t/m 17 november 2026"
SAMENVATTING = ("Welke interland is vandaag op tv? Alle 52 Nations League-duels van 12 t/m 17 november per dag, met tijden "
                "en zender: Oranje op NPO 3, de rest bij Ziggo.")
BIJWERKEN = "dagelijks tijdens de break"

# deelkaart: og_kaarten/gsod.py
OG_LOGO = "nations-league-logo.png"
OG_EYEBROW = "Interlands op tv · 12-17 november"
OG_KOP = "Welke interland<br><em>is vandaag op tv?</em>"
OG_TEGELS = [("Duels", "52"), ("Oranje", "NPO 3")]
OG_KOPJE = "De grootste duels van de week"
OG_RECHTS = "Zender"
OG_RIJEN = [("Do 12 nov", "Italië – Frankrijk · 20:45", "Ziggo 2"),
            ("Vr 13 nov", "Nederland – Griekenland · 20:45", "NPO 3"),
            ("Zo 15 nov", "Spanje – Engeland · 20:45", "Ziggo 2"),
            ("Ma 16 nov", "Duitsland – Nederland · 20:45", "NPO 3")]

NPO = "<strong>NPO 3</strong> (NOS)"
SW = "Switch op Ziggo Sport 1"
GEEN = "Geen Nederlandse zender"
ZS = lambda n: f"Ziggo Sport {n}"

# (tijd, thuis, uit, groep, zender) per dag - bron: UEFA + Ziggo-programma (9-11-2026)
DAGEN = [
    ("Donderdag 12 november", [
        ("18:00", "Turkije", "België", "A1", "Ziggo Sport 1 en 2"),
        ("18:00", "Armenië", "Cyprus", "C2", SW),
        ("20:45", "Italië", "Frankrijk", "A1", ZS(2)),
        ("20:45", "Engeland", "Kroatië", "A3", ZS(3)),
        ("20:45", "Tsjechië", "Spanje", "A3", ZS(5)),
        ("20:45", "Albanië", "Finland", "C1", SW),
        ("20:45", "San Marino", "Wit-Rusland", "C1", SW),
        ("20:45", "Montenegro", "Letland", "C2", SW)]),
    ("Vrijdag 13 november", [
        ("18:00", "Moldavië", "Kazachstan", "C3", GEEN),
        ("20:45", "Nederland", "Griekenland", "A2", NPO),
        ("20:45", "Servië", "Duitsland", "A2", ZS(1)),
        ("20:45", "Slovenië", "Zwitserland", "B1", GEEN),
        ("20:45", "Schotland", "Noord-Macedonië", "B1", GEEN),
        ("20:45", "Slowakije", "Faeröer", "C3", GEEN),
        ("20:45", "Bulgarije", "IJsland", "C4", GEEN),
        ("20:45", "Luxemburg", "Estland", "C4", GEEN),
        ("20:45", "Andorra", "Gibraltar", "D1", GEEN),
        ("20:45", "Liechtenstein", "Azerbeidzjan", "D2", GEEN)]),
    ("Zaterdag 14 november", [
        ("15:00", "Kosovo", "Israël", "B3", ZS(2)),
        ("18:00", "Noorwegen", "Wales", "A4", ZS(2)),
        ("18:00", "Georgië", "Hongarije", "B2", GEEN),
        ("20:45", "Portugal", "Denemarken", "A4", ZS(2)),
        ("20:45", "Noord-Ierland", "Oekraïne", "B2", ZS(3)),
        ("20:45", "Oostenrijk", "Ierland", "B3", SW),
        ("20:45", "Zweden", "Bosnië-Herzegovina", "B4", SW),
        ("20:45", "Roemenië", "Polen", "B4", SW)]),
    ("Zondag 15 november", [
        ("15:00", "Cyprus", "Montenegro", "C2", ZS(3)),
        ("15:00", "Letland", "Armenië", "C2", GEEN),
        ("18:00", "Finland", "San Marino", "C1", ZS(1)),
        ("18:00", "Wit-Rusland", "Albanië", "C1", GEEN),
        ("20:45", "Spanje", "Engeland", "A3", ZS(2)),
        ("20:45", "België", "Italië", "A1", ZS(3)),
        ("20:45", "Frankrijk", "Turkije", "A1", ZS(5)),
        ("20:45", "Kroatië", "Tsjechië", "A3", SW)]),
    ("Maandag 16 november", [
        ("16:00", "Kazachstan", "Slowakije", "C3", ZS(2)),
        ("16:00", "Faeröer", "Moldavië", "C3", GEEN),
        ("18:00", "Estland", "Bulgarije", "C4", "Ziggo Sport 1 en 3"),
        ("18:00", "IJsland", "Luxemburg", "C4", GEEN),
        ("18:00", "Litouwen", "Liechtenstein", "D2", GEEN),
        ("20:45", "Duitsland", "Nederland", "A2", NPO),
        ("20:45", "Griekenland", "Servië", "A2", ZS(1)),
        ("20:45", "Zwitserland", "Schotland", "B1", GEEN),
        ("20:45", "Noord-Macedonië", "Slovenië", "B1", GEEN),
        ("20:45", "Gibraltar", "Malta", "D1", GEEN)]),
    ("Dinsdag 17 november", [
        ("20:45", "Denemarken", "Noorwegen", "A4", ZS(2)),
        ("20:45", "Wales", "Portugal", "A4", ZS(3)),
        ("20:45", "Polen", "Zweden", "B4", SW),
        ("20:45", "Bosnië-Herzegovina", "Roemenië", "B4", SW),
        ("20:45", "Hongarije", "Noord-Ierland", "B2", SW),
        ("20:45", "Oekraïne", "Georgië", "B2", SW),
        ("20:45", "Israël", "Oostenrijk", "B3", SW),
        ("20:45", "Ierland", "Kosovo", "B3", SW)]),
]
ALLE = [(dag, *w) for dag, ws in DAGEN for w in ws]
N_DUELS = len(ALLE)
N_GEEN = sum(1 for w in ALLE if w[5] == GEEN)
N_SW = sum(1 for w in ALLE if w[5] == SW)
ORANJE = [w for w in ALLE if "Nederland" in (w[2], w[3])]
T_GRE, T_GER = ORANJE[0][1], ORANJE[1][1]

L = {"nlg": '<a href="/competities/uefa-nations-league">Nations League</a>',
     "reken": '<a href="/nieuws/nations-league-nieuwe-opzet-2028-wat-betekent-het-voor-oranje">wat Oranje precies nodig heeft</a>',
     "selectie": '<a href="/nieuws/selectie-oranje-november-2026-griekenland-duitsland">de selectie van Xavi</a>',
     "uitleg": '<a href="/nieuws/hoe-werkt-de-nations-league-complete-uitleg-2026-2027">hoe de Nations League werkt</a>',
     "vb": '<a href="/voorbeschouwingen">voorbeschouwingen</a>',
     "op": '<a href="/opstellingen">opstellingen</a>',
     "lk": '<a href="/live-kijken">live kijken</a>',
     "711": '<a href="/bookmakers/711">711</a>',
     "b365": '<a href="/bookmakers/bet365">Bet365</a>',
     "legaal": '<a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>'}
C = lambda slug, naam: f'<a href="/clubs/{slug}">{naam}</a>'


def dagtabel(dag):
    ws = dict(DAGEN)[dag]
    rijen = []
    for t, h, u, g, z in ws:
        wed = f"{h} – {u}"
        if "Nederland" in (h, u):
            wed = f"<strong>{wed}</strong>"
        rijen.append((t, wed, f"League {g[0]} · {g}", z))
    return tabel(["Tijd", "Wedstrijd", "League/groep", "Waar kijken"], rijen)


ORANJE_TABEL = tabel(["Datum", "Aftrap", "Wedstrijd", "Stadion", "Tv"], [
    ("<strong>Vr 13 november</strong>", T_GRE, "Nederland – Griekenland", "Johan Cruijff ArenA, Amsterdam", "NPO 3"),
    ("<strong>Ma 16 november</strong>", T_GER, "Duitsland – Nederland", "Olympiastadion, Berlijn", "NPO 3")])

STAND = tabel(["#", "Land", "Punten", "Saldo"], [
    ("1", C("nederland", "Nederland"), "<strong>8</strong>", "+2"), ("2", C("griekenland", "Griekenland"), "<strong>8</strong>", "+2"),
    ("3", C("duitsland", "Duitsland"), "<strong>5</strong>", "+1"), ("4", C("servie", "Servië"), "<strong>0</strong>", "-5")])

content = f"""<p><strong>Van donderdag 12 tot en met dinsdag 17 november 2026 staan er {N_DUELS} interlands in de {L['nlg']} op het programma: speeldag 5 en 6, de laatste twee van de groepsfase. Oranje speelt vrijdag om {T_GRE} uur tegen Griekenland en maandag om {T_GER} uur in Berlijn tegen Duitsland, allebei live op NPO 3. Bijna alle andere grote interlands, zoals Italië – Frankrijk en Spanje – Engeland, zie je bij Ziggo Sport. Hieronder staat per dag welke wedstrijd je waar kunt kijken.</strong></p>
<p>Alle tijden zijn Nederlandse tijd. De Eredivisie ligt tijdens deze interlandbreak stil en gaat verder op zaterdag 21 november. Wil je eerst weten {L['uitleg']}? Lees dan onze uitleg.</p>
<h3><strong>Oranje deze week</strong></h3>
{ORANJE_TABEL}
<p>Oranje staat in groep A2 bovenaan, met evenveel punten als Griekenland. Het verschil zit in het aantal gemaakte doelpunten (7 tegen 5).</p>
{STAND}
<p>Winst op Griekenland en een punt in Berlijn betekent groepswinst. Twee gelijke spelen zijn genoeg voor de kwartfinales in maart, en een zege in Berlijn ook. Alle scenario's lees je in {L['reken']}. Bondscoach Xavi Hernández nam 25 spelers mee, onder wie de teruggekeerde Frenkie de Jong; bekijk {L['selectie']}.</p>
<p><strong>Odds:</strong> bij {L['711']} staat een Nederlandse zege op Griekenland op <strong>1,47</strong>, een gelijkspel op 4,90 en een Griekse zege op 7,00 (afgelezen op maandag 9 november). Wed alleen bij een bookmaker met een vergunning van de Kansspelautoriteit; lees {L['legaal']}.</p>
<h3><strong>Donderdag 12 november: interlands op tv</strong></h3>
{dagtabel("Donderdag 12 november")}
<p><strong>Italië – Frankrijk</strong> is de kraker van de avond. {C('frankrijk', 'Frankrijk')} (10 punten) is met een zege in Italië zeker van de groepswinst in A1. {C('italie', 'Italië')} (7) en {C('belgie', 'België')} (6) strijden om de tweede plek; België speelt om 18.00 uur al in Turkije. Bij 711 is Frankrijk favoriet met 1,87, tegen 4,20 voor Italië (9 november).</p>
<p>{C('engeland', 'Engeland')} (9 punten) is met een zege op Kroatië zeker van de kwartfinales. Groepsleider {C('spanje', 'Spanje')} (12) heeft die plek al binnen en speelt in Tsjechië.</p>
<h3><strong>Vrijdag 13 november: interlands op tv</strong></h3>
{dagtabel("Vrijdag 13 november")}
<p>Alle ogen zijn gericht op <strong>Nederland – Griekenland</strong> in de Johan Cruijff ArenA, de topper van groep A2. Tegelijk speelt {C('duitsland', 'Duitsland')} (5 punten) in Belgrado tegen {C('servie', 'Servië')}. Die wedstrijd zie je op Ziggo Sport 1.</p>
<p>Op vrijdag zijn de meeste duels niet op de Nederlandse tv. Dat geldt ook voor Slovenië – {C('zwitserland', 'Zwitserland')}: de groepsleider van B1 (12 punten) is met een zege zeker van groepswinst en promotie naar League A.</p>"""

content2 = f"""<h3><strong>Zaterdag 14 november: interlands op tv</strong></h3>
{dagtabel("Zaterdag 14 november")}
<p><strong>Portugal – Denemarken</strong> is de grootste wedstrijd van de zaterdag. {C('portugal', 'Portugal')} (12 punten) is al zeker van de kwartfinales en wordt met een zege op {C('denemarken', 'Denemarken')} (6) ook groepswinnaar. Bij 711 staat een Portugese zege op 1,52 (9 november).</p>
<p>Om 18.00 uur spelen {C('noorwegen', 'Noorwegen')} en {C('wales', 'Wales')}, die allebei 3 punten hebben. Voor de nummer vier van groep A4 dreigt degradatie. In de avond strijden {C('zweden', 'Zweden')} (10) en {C('bosnie-herzegovina', 'Bosnië-Herzegovina')} (8) om de groepswinst in B4, en daarmee om promotie naar League A.</p>
<h3><strong>Zondag 15 november: interlands op tv</strong></h3>
{dagtabel("Zondag 15 november")}
<p><strong>Spanje – Engeland</strong> is misschien wel de wedstrijd van de week. Spanje (12) en Engeland (9) maken in dit duel waarschijnlijk uit wie groep A3 wint. De groepswinnaar speelt de return van de kwartfinale thuis.</p>
<p>Tegelijk speelt België thuis tegen Italië. Dat duel kan beslissen wie met Frankrijk naar de kwartfinales gaat. Frankrijk sluit thuis af tegen {C('turkije', 'Turkije')}, dat na vier duels nog geen punt heeft.</p>
<h3><strong>Maandag 16 november: interlands op tv</strong></h3>
{dagtabel("Maandag 16 november")}
<p><strong>Duitsland – Nederland</strong> in het Olympiastadion in Berlijn is de afsluiter voor Oranje. Het eerste duel eindigde in september in 1-1. Op hetzelfde moment speelt {C('griekenland', 'Griekenland')} thuis tegen Servië (Ziggo Sport 1). De uitslag daar telt mee voor de eindstand van groep A2.</p>
<p>{C('zwitserland', 'Zwitserland')} – {C('schotland', 'Schotland')} en de andere duels van League C en D om 18.00 uur zijn niet op de Nederlandse tv. Estland – Bulgarije en Kazachstan – Slowakije wel, bij Ziggo Sport.</p>"""

content3 = f"""<h3><strong>Dinsdag 17 november: interlands op tv</strong></h3>
{dagtabel("Dinsdag 17 november")}
<p>De groepsfase eindigt met <strong>Wales – Portugal</strong> (Ziggo Sport 3) en <strong>Denemarken – Noorwegen</strong> (Ziggo Sport 2). In League B valt de beslissing over promotie: {C('oostenrijk', 'Oostenrijk')} (8 punten) speelt uit tegen Israël, {C('noord-ierland', 'Noord-Ierland')} (8) uit tegen Hongarije. Die duels zie je in de Switch op Ziggo Sport 1.</p>
<h3><strong>Zo kijk je de interlands</strong></h3>
<p><strong>Oranje: NPO 3 en NOS.</strong> Beide wedstrijden van Oranje zijn gratis te zien op NPO 3. Online kijk je mee via de NOS-app, NOS.nl en NPO Start.</p>
<p><strong>Andere Nations League-duels: Ziggo Sport.</strong> Ziggo heeft de rechten op de Nations League zonder Oranje. Ziggo Sport (kanaal 14) zit standaard in het Ziggo-abonnement. Tijdens de Nations League zendt Ziggo daar de Switch uit. Deze week staan {N_SW} duels in het Ziggo-programma alleen in de Switch. Met het extra pakket Ziggo Sport Totaal (kanalen 401 tot en met 406) kies je zelf welke wedstrijd je kijkt. Onderweg kan dat in de app Ziggo GO.</p>
<p><strong>Geen Nederlandse zender.</strong> Voor {N_GEEN} van de {N_DUELS} duels is geen Nederlandse uitzending gepland. Het gaat vooral om wedstrijden uit League B, C en D. In de tabellen staat dan 'Geen Nederlandse zender'.</p>
<p><strong>Bet365.</strong> {L['b365']} zendt via zijn streamingschema veel wedstrijden live uit voor klanten met een geverifieerd account en saldo (18+). Deze week staat er geen enkel Nations League-duel in dat schema. Interlands kun je bij Bet365 deze week dus niet live kijken. Op onze pagina {L['lk']} zie je welke wedstrijden je wel via een bookmaker kunt volgen.</p>
<h3><strong>Voetbal op tv tijdens de interlandbreak</strong></h3>
<p>De Eredivisie speelt pas weer op zaterdag 21 en zondag 22 november (speelronde 13). De Keuken Kampioen Divisie gaat wel door: speelronde 15 wordt op zaterdag 14 en zondag 15 november gespeeld. Op de dagen van Oranje kun je terecht bij onze {L['vb']} met analyse en wedtips. De bevestigde {L['op']} van Oranje en de andere landen staan er ongeveer een uur voor de aftrap.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat speelt Nederland – Griekenland en waar kan ik het kijken?</strong><br>Op vrijdag 13 november om {T_GRE} uur in de Johan Cruijff ArenA. De wedstrijd is live op NPO 3 en via de NOS-app.</p>
<p><strong>Waar kan ik Duitsland – Nederland kijken?</strong><br>Op maandag 16 november om {T_GER} uur, live op NPO 3. Het duel wordt gespeeld in het Olympiastadion in Berlijn.</p>
<p><strong>Welke zender zendt de Nations League uit?</strong><br>De wedstrijden van Oranje zijn bij de NOS op NPO 3. Ziggo Sport heeft de rechten op de andere Nations League-duels. Een aantal kleinere duels is in Nederland niet op tv.</p>
<p><strong>Welke interland is vandaag op tv?</strong><br>Kijk in de tabel van de dag hierboven. De grootste duels zijn Italië – Frankrijk (do), Nederland – Griekenland (vr), Portugal – Denemarken (za), Spanje – Engeland (zo) en Duitsland – Nederland (ma), allemaal om 20.45 uur.</p>
<p><strong>Kan ik de interlands live kijken bij Bet365?</strong><br>Deze week niet. Er staat geen Nations League-duel in het streamingschema van Bet365.</p>
<p><strong>Waarom is er geen Eredivisie dit weekend?</strong><br>Het is interlandbreak (9 tot en met 17 november). Clubs moeten hun internationals dan afstaan aan hun land. De Eredivisie gaat verder op zaterdag 21 november.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    alles = content + content2 + content3
    w = len(re.sub(r"<[^>]+>", " ", alles).split())
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", w, "woorden |", N_DUELS, "duels |", N_GEEN, "zonder zender |", N_SW, "Switch")
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert 900 <= w <= 2000, w
    # schema: 52 duels, elk land precies 2x per speeldag-blok (A-C) en Oranje 2x op 20:45, NPO 3
    assert N_DUELS == 52 and N_GEEN == 17, (N_DUELS, N_GEEN)
    assert [len(ws) for _, ws in DAGEN] == [8, 10, 8, 8, 10, 8]
    from collections import Counter
    tel = Counter(x for w_ in ALLE for x in (w_[2], w_[3]))
    for land, n in tel.items():
        assert n in (1, 2), (land, n)          # League D (groepen van 3): sommige landen 1x
    assert sum(1 for n in tel.values() if n == 2) == 48 + 2   # A, B, C (48 landen) + Gibraltar en Liechtenstein
    assert len(ORANJE) == 2 and all(o[5] == NPO and o[1] == "20:45" for o in ORANJE)
    assert ORANJE[0][0].startswith("Vrijdag 13") and ORANJE[1][0].startswith("Maandag 16")
    # tijden en zenders in tekst/FAQ gelijk aan de tabel
    zender = {(w_[2], w_[3]): w_[5] for w_ in ALLE}
    assert zender[("Italië", "Frankrijk")] == ZS(2) and zender[("Spanje", "Engeland")] == ZS(2)
    assert zender[("Wales", "Portugal")] == ZS(3) and zender[("Denemarken", "Noorwegen")] == ZS(2)
    assert zender[("Servië", "Duitsland")] == ZS(1) and zender[("Griekenland", "Servië")] == ZS(1)
    assert zender[("Israël", "Oostenrijk")] == SW and zender[("Hongarije", "Noord-Ierland")] == SW
    assert zender[("Slovenië", "Zwitserland")] == GEEN and zender[("Zwitserland", "Schotland")] == GEEN
    assert zender[("Estland", "Bulgarije")].startswith("Ziggo") and zender[("Kazachstan", "Slowakije")].startswith("Ziggo")
    for h, u in [("Italië", "Frankrijk"), ("Portugal", "Denemarken"), ("Spanje", "Engeland")]:
        assert next(w_[1] for w_ in ALLE if (w_[2], w_[3]) == (h, u)) == "20:45"
    assert next(w_[1] for w_ in ALLE if (w_[2], w_[3]) == ("Turkije", "België")) == "18:00"
    assert next(w_[1] for w_ in ALLE if (w_[2], w_[3]) == ("Noorwegen", "Wales")) == "18:00"
    assert f"om {T_GRE} uur" in content3 and f"om {T_GER} uur" in content3
    # standen in de highlights (API na speeldag 4): groepswinst/kwartfinale-claims narekenen
    assert 10 + 3 > 7 + 3 and 10 + 3 > 6 + 6           # Frankrijk wint in Italië -> Italië max 10, België max 12 < 13
    assert 9 + 3 > 3 + 3 and 9 + 3 > 0 + 3 + 3          # Engeland wint van Kroatië -> Kroatië max 6, Tsjechië max 6
    assert 12 > 3 + 6 and 12 > 0 + 6                    # Spanje al zeker top 2 (alleen Engeland kan erover)
    assert 12 + 3 > 6 + 3                               # Portugal wint van Denemarken -> groepswinst
    assert 12 + 3 > 7 + 3                               # Zwitserland wint in Slovenië -> groepswinst B1
    assert "<h2" not in alles and "<h4" not in alles and "betcity" not in alles.lower() and "/go/" not in alles
    for verboden in ("espn", "footymetrics", "opstellingvandaag", "waaroptv", "wikipedia"):
        assert verboden not in alles.lower(), verboden
    assert content.startswith("<p><strong>") and content3.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/"), href
    assert "/voorbeschouwingen" in alles and "/opstellingen" in alles
    assert alles.count("Veelgestelde vragen") == 1 and 4 <= content3.split("Veelgestelde vragen")[1].count("<p><strong>") <= 6
    print("dry run ok")
