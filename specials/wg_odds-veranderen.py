# -*- coding: utf-8 -*-
"""NIEUW wedgids-artikel (Nieuws, nog geen item): waarom veranderen odds? Line movement, openings- en slotkoers, geld en
risico, nieuws, market makers en volgers, scherpe en recreatieve bookmakers, steam, verschillen tussen NL-bookmakers en
geschorste live odds. Slug waarom-veranderen-odds (gaf HTTP 404 op 10-11-2026 met curl, dus vrij).
Rubriek Speluitleg, wedgids-categorie 'Wedden uitgelegd'. Onderwerp: Engelstalige analysesite (alleen het onderwerp).
Zoekwoorden: 'waarom veranderen odds' (hoofd), 'odds veranderen', 'odds dalen', 'odds stijgen', 'line movement',
'openingskoers', 'odds verschillen per bookmaker', 'live odds geschorst', 'markt gesloten bookmaker', 'steam wedden'.

Afbakening t.o.v. /nieuws/wat-is-closing-line-value-clv (gelezen op 10-11-2026): daar staan CLV berekenen, de slotkoers als
scherpste prijs, een fictieve line-movement-tabel en steam in één alinea. Hier breder: WAAROM odds bewegen (nieuws, geld en
risico met rekenvoorbeeld, market makers/volgers, scherp/recreatief, efficiëntie), een ECHT voorbeeld, waarom NL-bookmakers
verschillen (echte odds van 7 merken) en het schorsen van live markten. CLV niet opnieuw uitgelegd: alleen gelinkt.

Feiten (bron + datum):
- ECHTE ODDS Nederland - Griekenland (Nations League, vr 13-11-2026 20:45 uur), 711 (publieke Kambi-feed, brand sevelevnl):
  * ma 9-11-2026 ±16:45: 1,47 / 4,90 / 7,00; meer dan 2,5 doelpunten 1,53; beide teams scoren ja 1,68
    (bron: docstring specials/eventgids_nederland_griekenland_2026.py en nations_league_2028_feiten.md).
  * di 10-11-2026 15:23 CET, zelf gelezen: eu-offering-api.kambicdn.com/offering/v2018/sevelevnl/listView/football/
    uefa_nations_league.json?lang=nl_NL&market=NL&useCombined=true -> event 1026632377: 1,49 / 4,60 / 6,75; over/onder 2,5
    1,57 / 2,33. betoffer/event/1026632377.json (15:23): beide teams scoren ja 1,71 / nee 2,04; changedDate van 1X2,
    over/onder en BTTS = 2026-11-10T11:09:49Z (12:09 uur NL); enkele kleine markten hebben een eerder tijdstip -> in de tekst
    'vrijwel alle markten'. (Om 14:25 stond 1X2 al op 1,49 / 4,60 / 6,75, zie nations_league_2028_feiten.md §6b.)
  * Nieuws: KNVB/OnsOranje ma 9-11 17:45: Van Dijk en Brobbey vallen af (onsoranje.nl/nieuws/nederlands-elftal-mannen/82817;
    NOS 2638755). Dus NA de eerste aflezing (16:45). Di 10-11 ±13:00 Sepp van den Berg opgeroepen (OnsOranje 82822, NOS 2638854).
    Oorzaak van de beweging is NIET te bewijzen -> in de tekst expliciet 'we weten niet zeker'.
- ECHTE ODDS 7 Nederlandse merken op hetzelfde Kambi-platform, di 10-11-2026 ±15:25 CET, betoffer/event/1026632377.json per
  brand (sevelevnl=711, ubnl=Unibet, leonl=LeoVegas, betmgmnl=BetMGM, jvh=JACKS.NL, bingoalnl=Bingoal, hgtnl=Oranje Palace):
  1X2 zie MERKEN hieronder; over/onder 2,5 (1,57/2,33) en BTTS (1,71/2,04) bij alle 7 gelijk; changedDate 1X2 bij alle 7
  2026-11-10T11:09:49Z. Alle 7 staan als vergunninghouder in legaal_data.py (Kansspelwijzer Ksa, stand 21-10-2026).
- Verboden live markten: Regeling kansspelen op afstand (BWBR0044767, 'Geldend van 01-04-2026 t/m heden', gelezen
  10-11-2026), Bijlage 2, onderdeel 2.3 Voetbal: o.a. i/j strafschoppen veroorzaken/nemen, t 'aan de Video Assistance Referee
  (VAR) gerelateerde momenten', a gele/rode kaarten, m-o hoekschoppen. Wedden op de uitslag en doelpunten tijdens de
  wedstrijd (live) mag wel.
- Geen wedbeurs en geen van de bekende internationale 'scherpe' bookmakers op de Kansspelwijzer (legaal_data.py, 21-10-2026).
Rekenvoorbeeld geld en risico: fictief (gemarkeerd), berekend en ge-assert.

Bewust weggelaten:
- Namen van buitenlandse scherpe bookmakers en wedbeurzen (geen NL-vergunning; geen reclame voor illegaal aanbod).
- Odds van bookmakers op een ander platform (ComeOn/TOTO via onze eigen feed): tijdstip niet exact te controleren en TOTO's
  markt was een 'vroege uitbetaling'-variant -> alleen kwalitatief genoemd.
- Percentages over hoe vaak steam 'klopt' of hoeveel odds door weer bewegen (niet betrouwbaar te onderbouwen).
- De reden van de verschillen in marge per merk (eigen keuze van elk merk; niet door de merken bevestigd) -> 'eigen marge'.
- Geen bron van het onderwerp genoemd.
Interne links gecontroleerd met curl op 10-11-2026: allemaal HTTP 200 (zie LINKS / asserts). Geen INFOGRAPHIC.
  ../superodd-agent/.venv/bin/python specials/wg_publiceer.py odds-veranderen   (dry run)"""
import os, sys, re
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel

ITEM_ID = None   # nieuw artikel
SLUG = "waarom-veranderen-odds"
RUBRIEK = "6502b66cd9992658b4037cf5"   # Speluitleg
WEDGIDS_CAT = "Wedden uitgelegd"
TITEL = "Waarom veranderen odds? Zo bewegen quoteringen"
SAMENVATTING = ("Waarom veranderen odds? Zo bewegen quoteringen door nieuws en geld, waarom bookmakers verschillen en "
                "waarom live odds even dichtgaan. Met echt voorbeeld.")

OG_KOP = "Waarom veranderen <span>odds</span>?"
OG_EYEBROW = "Zo bewegen quoteringen"
OG_CHIPS = ["Echt voorbeeld: Oranje", "7 bookmakers vergeleken"]
OG_MOTIEF = "odds"
OG_DATA = ["Oranje wint · 1,47 → 1,49", "Gelijkspel · 4,90 → 4,60", "Griekenland · 7,00 → 6,75", "Marge · 2,7% → 3,7%"]

CLV = "/nieuws/wat-is-closing-line-value-clv"
ODDS = "/nieuws/odds-uitgelegd-quotering-lezen"
KANS = "/nieuws/kans-berekenen-uit-odds-impliciete-kans"
MARGE = "/nieuws/marge-bookmaker-overround-uitbetalingspercentage"
VALUE = "/nieuws/wat-is-de-wedstrategie-value-betting"
BEPERKT = "/nieuws/account-beperkt-bookmaker"
LEGAAL = "/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland"
CORNERS = "/nieuws/dit-is-waarom-wedden-op-corners-niet-meer-legaal-is-in-nederland"
CASHOUT = "/nieuws/wat-is-cash-out"
VERG = "/odds-vergelijken-bij-alle-bookmakers-beste-odds-vandaag"
LIMIET = "/nieuws/netto-stortingslimiet"
LINKS = (CLV, ODDS, KANS, MARGE, VALUE, BEPERKT, LEGAAL, CORNERS, CASHOUT, VERG, LIMIET, "/speel-bewust/verantwoord-wedden",
         "/wedgids", "/bookmakers/711", "/bookmakers/unibet", "/bookmakers/leovegas", "/bookmakers/betmgm",
         "/bookmakers/jacks-nl", "/bookmakers/bingoal", "/bookmakers/oranje-palace")


def k(x, n=2):
    return f"{x:.{n}f}".replace(".", ",")


def pct(x, n=1):
    return f"{100 * x:.{n}f}".replace(".", ",") + "%"


def eur(x):
    return "€" + f"{abs(x):,.0f}".replace(",", ".")


def marge(odds):
    return sum(1 / o for o in odds) - 1


def eerlijk(odds):
    s = sum(1 / o for o in odds)
    return [(1 / o) / s for o in odds]


# ---- echt voorbeeld: Nederland - Griekenland bij 711 ----
MA = (1.47, 4.90, 7.00)   # ma 9-11-2026 ±16:45
DI = (1.49, 4.60, 6.75)   # di 10-11-2026 15:23
MA_P, DI_P = eerlijk(MA), eerlijk(DI)
assert (pct(marge(MA)), pct(marge(DI))) == ("2,7%", "3,7%")
assert [pct(p) for p in MA_P] == ["66,2%", "19,9%", "13,9%"]
assert [pct(p) for p in DI_P] == ["64,7%", "21,0%", "14,3%"]
UITK = ["Nederland wint", "Gelijkspel", "Griekenland wint"]
RIJEN_NG = [(u, k(a), k(b), pct(pa), pct(pb)) for u, a, b, pa, pb in zip(UITK, MA, DI, MA_P, DI_P)]
RIJEN_NG += [("Meer dan 2,5 doelpunten", "1,53", "1,57", "–", "–"), ("Beide teams scoren: ja", "1,68", "1,71", "–", "–"),
             ("<strong>Marge 1X2</strong>", "", "", f"<strong>{pct(marge(MA))}</strong>", f"<strong>{pct(marge(DI))}</strong>")]

# ---- echte odds 7 merken, zelfde platform, zelfde moment (di 10-11-2026 ±15:25) ----
MERKEN = [("711", "711", (1.49, 4.60, 6.75)), ("Unibet", "unibet", (1.46, 4.60, 6.75)),
          ("JACKS.NL", "jacks-nl", (1.45, 4.50, 6.50)), ("Bingoal", "bingoal", (1.45, 4.50, 6.50)),
          ("Oranje Palace", "oranje-palace", (1.45, 4.50, 6.50)), ("LeoVegas", "leovegas", (1.44, 4.40, 6.40)),
          ("BetMGM", "betmgm", (1.43, 4.35, 6.25))]
MARGES = {m: marge(o) for m, _, o in MERKEN}
assert [pct(MARGES[m]) for m, _, _ in MERKEN] == ["3,7%", "5,0%", "6,6%", "6,6%", "6,6%", "7,8%", "8,9%"]
RIJEN_MERK = [(f'<a href="/bookmakers/{s}">{m}</a>', k(o[0]), k(o[1]), k(o[2])) for m, s, o in MERKEN]   # bewust geen marge per merk (partners)
INZET = 10
HOOG, LAAG = MERKEN[0][2][0], MERKEN[-1][2][0]
assert (k(INZET * HOOG), k(INZET * LAAG), k(INZET * (HOOG - LAAG))) == ("14,90", "14,30", "0,60")
# over 100 gelijke weddenschappen op favorieten scheelt 0,06 x 100 x inzet
assert k(100 * INZET * (HOOG - LAAG), 0) == "60"

# ---- rekenvoorbeeld geld en risico (fictief): over/onder 2,5 ----
O1 = (1.90, 1.90)
IN1 = (40000, 10000)                 # inzet op over, onder tegen de openingsodds
O2 = (1.80, 2.02)
IN2 = (10000, 25000)                 # inzet na de aanpassing


def resultaat(blokken):
    """Winst van de bookmaker als over (0) of onder (1) uitkomt; blokken = [(odds, inzetten), ...]."""
    totaal = sum(sum(i) for _, i in blokken)
    return [totaal - sum(i[w] * o[w] for o, i in blokken) for w in (0, 1)]


R1 = resultaat([(O1, IN1)])
R2 = resultaat([(O1, IN1), (O2, IN2)])
assert R1 == [-26000, 31000]
assert [round(x) for x in R2] == [-9000, 15500]
assert (pct(marge(O1)), pct(marge(O2))) == ("5,3%", "5,1%")
# als de bookmaker zelf 50/50 inschat, blijft zijn verwachte winst positief; het risico (verschil) wordt kleiner
assert round(sum(R1) / 2) == 2500 and round(sum(R2) / 2) == 3250
assert round(R1[1] - R1[0]) == 57000 and round(R2[1] - R2[0]) == 24500

content = f"""<p><strong>Odds veranderen omdat een bookmaker zijn prijs steeds aanpast aan nieuwe informatie en aan het geld dat binnenkomt. Blessures, opstellingen, schorsingen en het weer veranderen de kansen. Veel geld op één uitkomst verhoogt het risico van de bookmaker. Zakt een odd, dan vindt de markt die uitkomst kansrijker of wordt er veel op ingezet; stijgt hij, dan is het andersom.</strong></p>
<p>In dit artikel lees je wat er tussen de openingskoers en de aftrap gebeurt, wie de prijzen eigenlijk bepaalt, waarom Nederlandse bookmakers verschillende odds geven voor dezelfde wedstrijd en waarom live markten soms ineens dichtgaan. Met een echt voorbeeld: Nederland – Griekenland.</p>
<h3><strong>Wat is een openingskoers en wat is de slotkoers?</strong></h3>
<p>Een bookmaker opent een markt vaak dagen of zelfs weken voor de wedstrijd. De eerste prijs heet de <strong>openingskoers</strong>. Daarna verandert de odd nog vaak. De laatste odd voor de aftrap is de <strong>slotkoers</strong> (closing line). Alle bewegingen daartussen samen heten <strong>line movement</strong>.</p>
<p>De openingskoers is gebaseerd op het rekenmodel van de bookmaker en op wat er op dat moment bekend is. Er is dan nog weinig geld ingezet en de maximale inzet is vaak laag. Naarmate de aftrap dichterbij komt, komt er meer informatie en meer geld, en wordt de prijs scherper. Of jij beter instapt dan de slotkoers, meet je met <a href="{CLV}">closing line value (CLV)</a>. Dat leggen we daar uitgebreid uit; hier gaat het om de vraag waaróm de lijn beweegt.</p>
<h3><strong>Waarom veranderen odds voor een wedstrijd?</strong></h3>
<p>Een odd is een prijs voor een kans, met de marge van de bookmaker erin. Hoe je die kans uit een odd haalt, lees je in <a href="{KANS}">kans berekenen uit odds</a>. Verandert de kans of het risico, dan verandert de prijs. De belangrijkste oorzaken:</p>
<ul><li><strong>Blessures en schorsingen.</strong> Valt een sterkhouder af, dan daalt de winkans van zijn ploeg. Bij een topspits of een vaste keeper kan dat flink schelen.</li><li><strong>Opstellingen.</strong> In het voetbal zijn die meestal ongeveer een uur voor de aftrap bekend. Speelt een trainer met reserves, bijvoorbeeld voor een Europese wedstrijd, dan beweegt de markt vaak direct.</li><li><strong>Weer en veld.</strong> Zware regen, harde wind of een slecht veld kunnen het spel en het aantal doelpunten beïnvloeden. Dat zie je vooral terug in de markten op het aantal doelpunten.</li><li><strong>Motivatie en programma.</strong> Een ploeg die al zeker is van de titel of drie dagen later een belangrijkere wedstrijd speelt, krijgt soms een andere prijs.</li><li><strong>Geld.</strong> Komt er veel geld op één kant, dan past de bookmaker de odds aan om zijn risico te beperken. Hieronder zie je hoe dat werkt.</li></ul>
<h3><strong>Hoe beïnvloedt ingezet geld de odds?</strong></h3>
<p>Een bookmaker wil niet dat hij bij één uitslag een groot bedrag verliest. Dat mogelijke verlies heet <strong>aansprakelijkheid</strong> (liability). Een rekenvoorbeeld met een markt over/onder 2,5 doelpunten. <em>De bedragen zijn fictief.</em></p>
<p>De bookmaker opent beide kanten op {k(O1[0])} (marge {pct(marge(O1))}). Er komt {eur(IN1[0])} binnen op meer dan 2,5 en {eur(IN1[1])} op minder dan 2,5. Valt de over, dan moet hij {eur(IN1[0] * O1[0])} uitbetalen en verliest hij {eur(R1[0])}. Valt de under, dan wint hij {eur(R1[1])}. Om dat risico te verkleinen, verlaagt hij de over naar {k(O2[0])} en verhoogt hij de under naar {k(O2[1])}. Daarna komt er nog {eur(IN2[0])} op de over en {eur(IN2[1])} op de under.</p>
{tabel(["Situatie", "Resultaat bookmaker bij over", "Resultaat bookmaker bij under"], [
    (f"Na de eerste inzetten (beide {k(O1[0])})", f"−{eur(R1[0])}", f"+{eur(R1[1])}"),
    (f"Na de aanpassing ({k(O2[0])} / {k(O2[1])})", f"−{eur(R2[0])}", f"+{eur(R2[1])}"),
])}
<p>Het verschil tussen de beste en slechtste uitkomst voor de bookmaker daalt van {eur(R1[1] - R1[0])} naar {eur(R2[1] - R2[0])}. Schat de bookmaker de kans zelf op 50/50, dan verwacht hij in beide gevallen winst te maken; de aanpassing maakt die winst vooral zekerder.</p>
<p>In de praktijk is het genuanceerder. Grote bookmakers hoeven niet elke markt precies in balans te brengen. Ze kijken vooral naar <strong>wie</strong> inzet. Geld van wedders die vaak gelijk krijgen, weegt zwaar: daar past een bookmaker zijn prijs snel op aan. Veel kleine inzetten van fans op hun eigen club zijn vaak minder reden om de kans anders te schatten.</p>"""

content2 = f"""<h3><strong>Echt voorbeeld: hoe bewogen de odds van Nederland – Griekenland?</strong></h3>
<p>Nederland speelt op vrijdag 13 november 2026 in de Nations League thuis tegen Griekenland. We lazen de odds van <a href="/bookmakers/711">711</a> op maandagmiddag 9 november en op dinsdagmiddag 10 november af. De kans zonder marge hebben we zelf berekend.</p>
{tabel(["Markt", "Odd ma 9-11 (16.45 uur)", "Odd di 10-11 (15.23 uur)", "Kans zonder marge ma", "Kans zonder marge di"], RIJEN_NG)}
<p>Wat valt op?</p>
<ul><li><strong>De odd van Oranje steeg licht</strong>, van {k(MA[0])} naar {k(DI[0])}. De kans zonder marge daalde van {pct(MA_P[0])} naar {pct(DI_P[0])}.</li><li><strong>Het gelijkspel bewoog het meest.</strong> Die odd zakte van {k(MA[1])} naar {k(DI[1])}: de kans steeg van {pct(MA_P[1])} naar {pct(DI_P[1])}.</li><li><strong>De marge werd groter</strong>, van {pct(marge(MA))} naar {pct(marge(DI))}. Een deel van de lagere odds voor gelijkspel en Griekenland komt dus niet door een andere kans, maar doordat de bookmaker meer marge rekent. Daarom vergelijk je bewegingen het best zonder marge.</li><li><strong>Vrijwel alle markten van dit duel veranderden tegelijk</strong>, op dinsdag om 12.09 uur volgens de feed van de bookmaker. Een bookmaker past dus niet één odd aan, maar rekent de hele wedstrijd in één keer opnieuw door.</li></ul>
<p>Op maandag om 17.45 uur, ná onze eerste aflezing, meldde de KNVB dat Virgil van Dijk en Brian Brobbey afvallen. Het ligt voor de hand dat de markt daarop reageerde, maar zeker weten doen we het niet: geld, het eigen model van de bookmaker en ander nieuws spelen ook mee. Dat is typerend voor line movement. Je ziet wél dat een prijs beweegt, maar zelden precies waarom.</p>
<h3><strong>Waarom verschillen odds tussen Nederlandse bookmakers?</strong></h3>
<p>Elke bookmaker kiest zijn eigen marge en volgt zijn eigen risico. Sommige zetten hun eigen prijzen, andere nemen ze grotendeels over van een leverancier. Minstens zeven legale Nederlandse bookmakers halen hun voetbalodds bij dezelfde leverancier, Kambi. Hun odds voor Nederland – Griekenland op dinsdag 10 november rond 15.25 uur:</p>
{tabel(["Bookmaker", "Nederland", "Gelijk", "Griekenland"], RIJEN_MERK)}
<p>Alle zeven werden op hetzelfde moment bijgewerkt en hadden precies dezelfde odds voor meer of minder dan 2,5 doelpunten en voor beide teams scoren. Alleen in de 1X2-markt verschillen ze, doordat elk merk zijn eigen marge kiest; op dit duel liep die uiteen van ongeveer 4 tot 9 procent. Een inzet van €{INZET} op Oranje levert bij de hoogste odd €{k(INZET * HOOG)} op en bij de laagste €{k(INZET * LAAG)}. Dat lijkt weinig, maar over honderd van zulke weddenschappen is het €{k(100 * INZET * (HOOG - LAAG), 0)}. Bookmakers die hun prijzen zelf maken, kunnen nog meer afwijken. Hoe je de marge zelf berekent, lees je in ons artikel over de <a href="{MARGE}">marge van een bookmaker</a>.</p>
<p>Wil je weten waar de odd op dit moment het hoogst is, gebruik dan de <a href="{VERG}">odds vergelijker</a>. Let wel: odds veranderen snel, dus deze tabel is een momentopname.</p>
<h3><strong>Wie bepaalt de prijs: market makers en volgers</strong></h3>
<p>Niet elke bookmaker rekent zelf alles uit. Grofweg zijn er twee soorten:</p>
<ul><li><strong>Market makers</strong> zetten zelf een prijs neer, met eigen rekenmodellen en handelaren. Ze laten vaak hogere inzetten toe, ook van wedders die structureel winnen, en gebruiken die inzetten als informatie. Zulke bookmakers worden ook wel <strong>scherpe bookmakers</strong> genoemd. Ze werken met lage marges en verdienen aan grote aantallen.</li><li><strong>Volgers</strong> nemen prijzen over van een leverancier of kijken naar de markt en passen hun odds aan als de rest beweegt. Ze richten zich vooral op recreatieve wedders: <strong>recreatieve bookmakers</strong>, of in het Engels soft bookmakers. Hun marges zijn vaak hoger en ze kunnen de inzet van winnende klanten beperken. Meer daarover lees je in <a href="{BEPERKT}">account beperkt door je bookmaker</a>.</li></ul>
<p>De bekende scherpe bookmakers en wedbeurzen werken internationaal en hebben geen Nederlandse vergunning. Spelen bij een aanbieder zonder vergunning is in Nederland niet toegestaan en je hebt er geen bescherming. Controleer daarom altijd <a href="{LEGAAL}">of een bookmaker legaal is</a>.</p>"""

content3 = f"""<h3><strong>Hoe efficiënt is de wedmarkt?</strong></h3>
<p>Een markt heet efficiënt als de prijs alle bekende informatie al bevat. Dan valt er met openbare informatie weinig te halen. Hoe meer geld en aandacht een markt krijgt, hoe sneller nieuws in de prijs zit. De 1X2-markt van een topwedstrijd in de Eredivisie of de Champions League is daardoor veel scherper dan een markt op een lagere competitie of op een spelersmarkt.</p>
<p>De meeste informatie zit in de prijs vlak voor de aftrap. Vroeg in de week zijn de odds minder scherp, maar dan weet je ook minder: een speler kan alsnog afvallen. Wie eerder dan de markt goed nieuws of een betere inschatting heeft, kan een hogere odd pakken. Dat is precies het idee achter <a href="{VALUE}">value betting</a>.</p>
<h3><strong>Wat is steam?</strong></h3>
<p>Steam is een plotselinge, snelle daling van een odd bij veel bookmakers tegelijk. Meestal komt er in korte tijd veel geld van goed geïnformeerde wedders op één kant, en volgen andere bookmakers. Erachteraan jagen werkt zelden: als jij het ziet, zijn de meeste odds al aangepast. Ook niet elke daling is slim geld. Bij grote clubs zakt een odd soms alleen doordat veel fans inzetten. In het artikel over <a href="{CLV}">closing line value</a> lees je hoe je meet of jij voor of na zo'n beweging instapt.</p>
<h3><strong>Waarom worden live odds geschorst?</strong></h3>
<p>Tijdens een wedstrijd gaan markten regelmatig even dicht. Je ziet dan een slotje, 'geschorst' of 'markt gesloten'. Dat gebeurt bij gevaarlijke momenten: een aanval in het strafschopgebied, een vrije trap vlak bij de goal, een doelpunt, een strafschop, een rode kaart of een check door de VAR.</p>
<p>De reden is snelheid. Een tv-beeld of stream loopt vaak een paar seconden achter op wat er in het stadion gebeurt. Bookmakers krijgen hun gegevens sneller binnen, maar als een markt open bleef tijdens een kans, kon iemand met sneller beeld inzetten op iets wat al gebeurd is. Dus sluit de bookmaker de markt, wacht hij de afloop af en opent hij met een nieuwe prijs. Bij een VAR-check kan dat een paar minuten duren. Zet je in op het moment dat een markt dichtgaat, dan wordt je weddenschap geweigerd of krijg je de vraag of je een nieuwe odd accepteert. Ook <a href="{CASHOUT}">cash-out</a> is in die momenten meestal niet beschikbaar.</p>
<p>Let op: in Nederland mag je wél live wedden op de uitslag of het aantal doelpunten, maar niet op de VAR-momenten zelf, op strafschoppen, kaarten of corners. Die staan op de lijst van verboden weddenschappen (Regeling kansspelen op afstand, bijlage 2). Lees ook <a href="{CORNERS}">waarom wedden op corners niet mag</a>.</p>
<h3><strong>Wat betekent dit voor jou als wedder?</strong></h3>
<ul><li><strong>Vergelijk odds.</strong> Zelfs bij bookmakers op hetzelfde platform kan het een paar cent per euro schelen.</li><li><strong>Kijk naar de kans, niet alleen naar de odd.</strong> Een lagere odd kan ook door een hogere marge komen, zoals bij Nederland – Griekenland.</li><li><strong>Kies je moment bewust.</strong> Vroeg instappen geeft soms een betere prijs, maar meer onzekerheid. Laat instappen geeft meer informatie, maar een scherpere prijs.</li><li><strong>Ren niet achter elke beweging aan.</strong> Een dalende odd betekent niet dat de uitkomst zeker is.</li></ul>
<p>Odds lezen en omrekenen leer je in <a href="{ODDS}">odds uitgelegd</a>. Zet alleen in wat je kunt missen, stel een <a href="{LIMIET}">netto-stortingslimiet</a> in en lees onze tips over <a href="/speel-bewust/verantwoord-wedden">verantwoord wedden</a>. Meer uitleg vind je in de <a href="/wedgids">wedgids</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Waarom dalen odds vlak voor de wedstrijd?</strong><br>Meestal door nieuws, zoals de opstelling of een blessure, of door veel geld op één uitkomst. Een dalende odd betekent dat de bookmaker die uitkomst kansrijker vindt of zijn risico wil beperken. Soms komt het ook door een hogere marge.</p>
<p><strong>Waarom heeft elke bookmaker andere odds?</strong><br>Elke bookmaker kiest zijn eigen marge en volgt zijn eigen risico. Op 10 november 2026 hadden zeven Nederlandse bookmakers op hetzelfde platform voor Oranje odds van {k(LAAG)} tot {k(HOOG)}. Het verschil zit in de marge die elk merk zelf kiest.</p>
<p><strong>Wat is een openingskoers?</strong><br>De eerste odd die een bookmaker voor een markt neerzet. Daarna past hij de prijs aan op nieuws en inzetten, tot de slotkoers bij de aftrap.</p>
<p><strong>Waarom staat een live markt op slot?</strong><br>Bij gevaarlijke momenten, een doelpunt of een VAR-check sluit de bookmaker de markt even, omdat de uitkomst op dat moment snel kan veranderen. Daarna gaat hij open met een nieuwe odd.</p>
<p><strong>Wat zijn scherpe bookmakers?</strong><br>Bookmakers die zelf prijzen maken, lage marges hebben en hoge inzetten van winnende wedders toelaten. De bekende namen hebben geen Nederlandse vergunning; daar spelen mag in Nederland niet.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    html = content + content2 + content3
    assert re.search(r"<(ul|ol|/li)>\s+<", html) is None
    assert "/kennisbank/" not in html and "<h2" not in html and "<h4" not in html and "/go/" not in html
    assert html.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>")
    assert content.startswith("<p><strong>")
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert len(OG_CHIPS) == 2 and len(OG_DATA) == 4
    for link in LINKS:
        assert f'href="{link}"' in html, link
    assert set(re.findall(r'href="([^"]+)"', html)) <= set(LINKS), set(re.findall(r'href="([^"]+)"', html)) - set(LINKS)
    for verboden in ("FootyMetrics", "BetCity", "opstellingvandaag", "waaroptv", "Betfair", "Pinnacle"):
        assert verboden.lower() not in html.lower(), verboden
    faq = content3.split("Veelgestelde vragen")[1]
    assert 4 <= faq.count("<p><strong>") <= 6
    woorden = len(re.sub(r"<[^>]+>", " ", html).split())
    assert 1200 <= woorden <= 2200, woorden
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", woorden, "woorden")
