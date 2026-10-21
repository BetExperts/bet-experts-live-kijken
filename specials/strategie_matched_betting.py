# -*- coding: utf-8 -*-
"""Nieuw Nieuws-item (ITEM_ID None, slug wat-houdt-de-wedstrategie-matched-betting-in; de oude Kennisbank-versie is
offline en 301't naar deze Nieuws-URL, die nu nog 404 geeft): Wat is matched betting en werkt het in Nederland?
GSC-query: "matched betting nederland".
Feiten nagelopen op 21-10-2026:
- Geen betting exchange onder de vergunninghouders in de Kansspelwijzer van de Ksa (legaal_data.py, stand 21-10-2026).
  Aanbieden zonder Nederlandse vergunning is verboden (art. 1 Wok); Ksa handhaaft o.a. met lasten onder dwangsom.
- Bonus = reclame volgens het Besluit werving, reclame en verslavingspreventie kansspelen (art. 1 sub f);
  werving/reclame mag niet gericht zijn op 18-24 jaar (art. 2 lid 4 onder a), Ksa beboette meerdere aanbieders hiervoor.
- Ksa: cashback (bonus op basis van verlies) niet toegestaan (brief nov. 2022, verduidelijkt feb. 2024).
- Rijksoverheid 12-06-2026: kabinet wil het aanbieden van bonussen verbieden (o.a. gratis inzet bij account aanmaken);
  wordt uitgewerkt in een wetsvoorstel, nog geen datum van inwerkingtreding.
- Netto stortingslimiet: €300 (18-23 jaar) / €700 (24+) per kalendermaand, per aanbieder (zie netto_stortingslimiet.py).
- Kansspelbelasting 37,8% per 1-1-2026 (Belastingdienst); bij een aanbieder met Ksa-vergunning betaalt de aanbieder,
  de speler doet geen aangifte.
Alle bedragen worden hieronder berekend en ge-assert.
  python3 specials/strategie_matched_betting.py [--live]"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
import lk_webflow as WF
from legaal_data import tabel, aanraders

ITEM_ID = None   # nieuw item
SLUG = "wat-houdt-de-wedstrategie-matched-betting-in"
RUBRIEK = "6502b64b78efefb4144fd2c1"
TITEL = "Matched betting: wat is het en werkt het in Nederland?"
SAMENVATTING = ("Matched betting uitgelegd: back en lay, de inzetformule, free bets omzetten en rekenvoorbeelden. "
                "Plus de Nederlandse realiteit en de risico's.")

OG_KOP = "Matched <span>betting</span>"
OG_EYEBROW = "Wedstrategie uitgelegd"
OG_CHIPS = ["Free bet omzetten", "Geen winstgarantie"]
OG_MOTIEF = "tabel"


def eur(x):
    s = f"€{abs(x):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return ("−" + s) if x < -0.004 else s


def odd(x):
    return f"{x:.2f}".replace(".", ",")


def r2(x):
    return round(x + 1e-9, 2)


# ---------- 1. Exchange-voorbeeld (internationaal principe) ----------
B, OB, OL, COM = 10, 2.00, 2.10, 0.02
LAY_Q = r2(B * OB / (OL - COM))                       # 9,62
AANSPR_Q = r2(LAY_Q * (OL - 1))                       # verplichting 10,58
Q_WINT = r2(B * (OB - 1) - AANSPR_Q)                  # back wint
Q_VERLIEST = r2(-B + LAY_Q * (1 - COM))               # lay wint
assert LAY_Q == 9.62 and AANSPR_Q == 10.58 and Q_WINT == -0.58 and Q_VERLIEST == -0.57

FB, FOB, FOL = 10, 5.00, 5.20
LAY_SNR = r2(FB * (FOB - 1) / (FOL - COM))            # 7,72
SNR_WINT = r2(FB * (FOB - 1) - LAY_SNR * (FOL - 1))
SNR_VERLIEST = r2(LAY_SNR * (1 - COM))
assert LAY_SNR == 7.72 and SNR_WINT == 7.58 and SNR_VERLIEST == 7.57

# ---------- 2. Nederlandse variant: dekken bij een tweede legale bookmaker ----------
Q_OB, Q_OC = 1.95, 1.90                               # over 2,5 bij A, under 2,5 bij B
DEK_Q = r2(B * Q_OB / Q_OC)                           # 10,26
NL_Q_OVER = r2(B * (Q_OB - 1) - DEK_Q)
NL_Q_UNDER = r2(-B + DEK_Q * (Q_OC - 1))
assert DEK_Q == 10.26 and NL_Q_OVER == -0.76 and NL_Q_UNDER == -0.77

F_OB, F_OC = 3.10, 1.40                               # free bet over 3,5 bij A, under 3,5 bij B
DEK_SNR = r2(FB * (F_OB - 1) / F_OC)                  # 15,00
NL_SNR_OVER = r2(FB * (F_OB - 1) - DEK_SNR)
NL_SNR_UNDER = r2(DEK_SNR * (F_OC - 1))
assert DEK_SNR == 15.00 and NL_SNR_OVER == 6.00 and NL_SNR_UNDER == 6.00

DEK_SR = r2(FB * F_OB / F_OC)                         # 22,14
NL_SR_OVER = r2(FB * F_OB - DEK_SR)
NL_SR_UNDER = r2(DEK_SR * F_OC - DEK_SR)
assert DEK_SR == 22.14 and NL_SR_OVER == 8.86 and NL_SR_UNDER == 8.86

TOTAAL = r2(min(NL_Q_OVER, NL_Q_UNDER) + NL_SNR_OVER)
assert TOTAAL == 5.23

# Rendement van een free bet van €10 (SNR) bij verschillende quoteringen (dekking bij een tweede bookmaker)
RIJEN_FB = []
for ob, oc in [(2.00, 1.90), (3.10, 1.40), (5.00, 1.22)]:
    dek = r2(FB * (ob - 1) / oc)
    winst = r2(FB * (ob - 1) - dek)
    assert abs(winst - r2(dek * (oc - 1))) <= 0.01
    RIJEN_FB.append((odd(ob), odd(oc), eur(dek), eur(winst), f"{winst / FB * 100:.0f}%"))
assert [r[3] for r in RIJEN_FB] == ["€4,74", "€6,00", "€7,21"]

OG_DATA = ["Free bet · €10 op 3,10", f"Dekking · {eur(DEK_SNR)} op 1,40", f"Resultaat · +{eur(NL_SNR_OVER)}"]

content = f"""<p><strong>Matched betting is een strategie waarbij je een bonus of free bet van een bookmaker omzet in (bijna) zeker geld. Je zet in op een uitkomst bij de bookmaker die de bonus geeft en dekt tegelijk de tegenovergestelde uitkomst af, zodat de uitslag er nauwelijks toe doet. Je winst komt niet uit voorspellen, maar uit de waarde van de bonus. In Nederland is het lastiger dan in het buitenland: er is geen legale betting exchange, bonussen zijn aan strenge regels gebonden en bookmakers kunnen je uitsluiten van promoties.</strong></p>
<p>Op internationale forums lees je dat matched betting "gratis geld" oplevert. Zo simpel is het niet. Het rekenwerk klopt, maar de praktijk bepaalt hoeveel er overblijft. Hieronder lees je hoe matched betting werkt, met de formules en rekenvoorbeelden in euro's, en wat er in Nederland in 2026 nog van over is. De quoteringen in de voorbeelden zijn fictief.</p>
<h3><strong>Hoe werkt matched betting?</strong></h3>
<p>Elke matched bet bestaat uit twee weddenschappen op dezelfde gebeurtenis:</p>
<ul><li><strong>De back bet:</strong> je zet in dat iets <em>wel</em> gebeurt, bijvoorbeeld "Ajax wint". Dat is een gewone weddenschap bij een bookmaker.</li><li><strong>De lay bet of dekking:</strong> je zet in dat het <em>niet</em> gebeurt. Bij een betting exchange speel je dan zelf voor bookmaker ("layen"). Zonder exchange dek je de andere uitkomsten af bij een tweede bookmaker.</li></ul>
<p>Omdat je beide kanten speelt, win je de ene weddenschap en verlies je de andere. Met de juiste inzetverhouding zijn die twee bijna even groot, waardoor je per saldo een klein bedrag verliest. Dat kleine verlies is de prijs om de bonus vrij te spelen. Daarna gebruik je de free bet op dezelfde manier, en daar zit de winst.</p>
<p><strong>De vaste volgorde</strong></p>
<ol><li><strong>Kwalificerende weddenschap:</strong> je plaatst de inzet die nodig is om de bonus te krijgen, bijvoorbeeld "zet €10 in en ontvang een free bet van €10", en dekt die af.</li><li><strong>Free bet ontvangen:</strong> de bookmaker zet de free bet op je account zodra de kwalificerende weddenschap is afgehandeld.</li><li><strong>Free bet omzetten:</strong> je speelt de free bet en dekt opnieuw af. De winst van de free bet is het rendement van de hele actie.</li></ol>
<h3><strong>Wat is een betting exchange en wat betekent layen?</strong></h3>
<p>Een betting exchange is een wedbeurs waar spelers tegen elkaar wedden in plaats van tegen een bookmaker. De ene speler biedt een quotering aan, de ander neemt die aan. Wie <strong>layt</strong>, wint de inzet van de tegenpartij als de uitkomst niet gebeurt, en betaalt uit als die wel gebeurt. Het bedrag dat je dan moet betalen heet de <strong>verplichting</strong> (liability): lay-inzet × (lay-quotering − 1). De exchange verdient aan een commissie op je winst, vaak een paar procent.</p>
<p>Met een exchange is matched betting het makkelijkst uit te leggen: één lay bet dekt alle andere uitkomsten af. Waarom dat in Nederland niet kan, lees je verderop.</p>
<h3><strong>Hoe bereken je de lay-inzet?</strong></h3>
<p>Er zijn drie formules, afhankelijk van wat voor weddenschap je afdekt. Commissie schrijf je als decimaal, dus 2% is 0,02.</p>
{tabel(["Situatie", "Formule lay-inzet", "Waarom"], [
    ("<strong>Kwalificerende weddenschap</strong> (eigen geld)", "inzet × back-odd ÷ (lay-odd − commissie)", "Je eigen inzet zit in de uitbetaling, dus je dekt de volledige uitbetaling af."),
    ("<strong>Free bet, inzet niet terug</strong> (SNR)", "free bet × (back-odd − 1) ÷ (lay-odd − commissie)", "Je krijgt alleen de winst, niet de inzet van de free bet."),
    ("<strong>Free bet, inzet wel terug</strong> (SR)", "free bet × back-odd ÷ (lay-odd − commissie)", "Zeldzaam: je krijgt winst én inzet, dus de free bet is meer waard."),
])}
<p><strong>Voorbeeld kwalificerende weddenschap</strong></p>
<p>Je zet €{B} in op Ajax wint tegen een quotering van {odd(OB)}. Op de exchange kun je "Ajax wint" layen tegen {odd(OL)} met 2% commissie. De lay-inzet is {B} × {odd(OB)} ÷ ({odd(OL)} − 0,02) = <strong>{eur(LAY_Q)}</strong>. Je verplichting is {eur(LAY_Q)} × {odd(OL - 1)} = {eur(AANSPR_Q)}.</p>
{tabel(["Uitslag", "Bookmaker (back)", "Exchange (lay)", "Saldo"], [
    ("Ajax wint", f"+{eur(B * (OB - 1))}", f"−{eur(AANSPR_Q)}", f"<strong>{eur(Q_WINT)}</strong>"),
    ("Gelijk of verlies Ajax", f"−{eur(B)}", f"+{eur(r2(LAY_Q * (1 - COM)))} (na commissie)", f"<strong>{eur(Q_VERLIEST)}</strong>"),
])}
<p>Wat er ook gebeurt, je bent ongeveer 57 à 58 cent kwijt. Dat heet het kwalificatieverlies: het is de kostprijs van de free bet.</p>"""

content2 = f"""<h3><strong>Hoe zet je een free bet om in geld?</strong></h3>
<p>Bij een free bet van het type <strong>stake not returned</strong> (SNR) krijg je bij winst alleen de winst uitbetaald. Daarom kies je hier juist een hogere quotering: hoe hoger de odd, hoe groter het deel van de free bet dat je overhoudt. Stel dat je de free bet van €{FB} speelt tegen {odd(FOB)} en layt tegen {odd(FOL)}. De lay-inzet is {FB} × {odd(FOB - 1)} ÷ ({odd(FOL)} − 0,02) = {eur(LAY_SNR)}. Wint je back bet, dan houd je {eur(SNR_WINT)} over. Wint de lay, dan houd je {eur(SNR_VERLIEST)} over. Van de €{FB} free bet blijft zo ruim 75% over als echt geld.</p>
<h3><strong>Matched betting in Nederland: zonder exchange</strong></h3>
<p>Hier zit het grote verschil met landen als het Verenigd Koninkrijk. Geen enkele aanbieder met een Nederlandse vergunning van de Kansspelautoriteit biedt op dit moment een betting exchange aan (stand oktober 2026). Een buitenlandse exchange zonder Nederlandse vergunning mag zich niet op Nederlandse spelers richten, en daar speel je zonder toezicht en zonder bescherming. Dat is dus geen optie.</p>
<p>Wat overblijft, is dekken bij een <strong>tweede legale bookmaker</strong>. Dat werkt het best bij markten met twee uitkomsten, zoals over/under doelpunten, beide teams scoren, draw no bet of de winnaar van een tenniswedstrijd. De formule wordt dan iets anders, omdat je bij de tweede bookmaker een gewone back bet plaatst:</p>
<ul><li><strong>Kwalificerend:</strong> dekking = inzet × odd bookmaker A ÷ odd bookmaker B</li><li><strong>Free bet (SNR):</strong> dekking = free bet × (odd bookmaker A − 1) ÷ odd bookmaker B</li><li><strong>Free bet (SR):</strong> dekking = free bet × odd bookmaker A ÷ odd bookmaker B</li></ul>
<p><strong>Rekenvoorbeeld zonder exchange</strong></p>
<p>Stap 1: je zet €{B} in op over 2,5 doelpunten bij bookmaker A tegen {odd(Q_OB)} en dekt under 2,5 bij bookmaker B tegen {odd(Q_OC)}. Dekking: {B} × {odd(Q_OB)} ÷ {odd(Q_OC)} = {eur(DEK_Q)}. Stap 2: je free bet van €{FB} gaat op over 3,5 doelpunten tegen {odd(F_OB)} bij bookmaker A, en je dekt under 3,5 bij bookmaker B tegen {odd(F_OC)}. Dekking: {FB} × {odd(F_OB - 1)} ÷ {odd(F_OC)} = {eur(DEK_SNR)}.</p>
{tabel(["Stap", "Uitslag", "Bookmaker A", "Bookmaker B", "Saldo"], [
    ("Kwalificerend", "Over 2,5", f"+{eur(B * (Q_OB - 1))}", f"−{eur(DEK_Q)}", f"<strong>{eur(NL_Q_OVER)}</strong>"),
    ("Kwalificerend", "Under 2,5", f"−{eur(B)}", f"+{eur(r2(DEK_Q * (Q_OC - 1)))}", f"<strong>{eur(NL_Q_UNDER)}</strong>"),
    ("Free bet (SNR)", "Over 3,5", f"+{eur(FB * (F_OB - 1))}", f"−{eur(DEK_SNR)}", f"<strong>+{eur(NL_SNR_OVER)}</strong>"),
    ("Free bet (SNR)", "Under 3,5", "€0,00 (free bet kost niets)", f"+{eur(r2(DEK_SNR * (F_OC - 1)))}", f"<strong>+{eur(NL_SNR_UNDER)}</strong>"),
])}
<p>Samen levert de actie in het slechtste geval {eur(TOTAAL)} op. Was de free bet van het type <strong>stake returned</strong>, dan was de dekking {eur(DEK_SR)} en de winst {eur(NL_SR_OVER)}. Let op hoeveel geld je vastzet: voor een winst van €6 staat er tijdelijk €{FB} free bet plus {eur(DEK_SNR)} eigen geld bij bookmaker B in het spel.</p>
<p><strong>Hogere odd, meer rendement, meer kapitaal</strong></p>
<p>De tabel laat zien wat een free bet van €{FB} (SNR) oplevert bij verschillende quoteringen, telkens gedekt bij een tweede bookmaker.</p>
{tabel(["Odd free bet", "Odd dekking", "Dekking", "Winst", "Deel van de free bet"], RIJEN_FB)}
<p>Hoe hoger de odd, hoe meer je van de free bet overhoudt, maar ook hoe meer eigen geld je bij de tweede bookmaker moet neerzetten. Met de netto stortingslimiet (€300 per maand tot je 24e, €700 daarna, per aanbieder) loop je daar sneller tegenaan dan je denkt.</p>
<p><strong>Drie uitkomsten? Dan heb je drie bookmakers nodig</strong></p>
<p>Bij 1X2 (thuis, gelijk, uit) moet je zonder exchange de twee andere uitkomsten bij twee andere bookmakers dekken. Dat kost meer marge en saldo, en de kans op een fout wordt groter. Vergelijk de quoteringen per uitkomst met onze <a href="/odds-vergelijken-bij-alle-bookmakers-beste-odds-vandaag">odds vergelijker</a>, zodat je per uitkomst de hoogste odd vindt.</p>
<h3><strong>Welke regels gelden voor bonussen in Nederland?</strong></h3>
<p>Matched betting staat of valt met bonussen, en daar zijn de Nederlandse regels streng:</p>
<ul><li><strong>Een bonus is reclame.</strong> In de regels voor werving en reclame valt een bonus, zoals gratis speltegoed, onder reclame. Reclame mag niet gericht zijn op jongvolwassenen van 18 tot 24 jaar. De Kansspelautoriteit heeft al meerdere aanbieders beboet voor bonusmails aan jonge spelers. Ben je jonger dan 24, dan krijg je dus weinig tot geen bonusaanbiedingen.</li><li><strong>Geen cashback.</strong> Bonussen die je verlies vergoeden, zijn volgens de Kansspelautoriteit niet toegestaan, omdat ze onmatig spelen kunnen aanmoedigen.</li><li><strong>Zorgplicht.</strong> Een aanbieder moet je speelgedrag volgen en ingrijpen bij risicovol gedrag. Wie veel en snel inzet om bonussen vrij te spelen, kan zo'n gesprek of beperking krijgen.</li><li><strong>Een bonusverbod is in de maak.</strong> Het kabinet maakte op 12 juni 2026 bekend dat het aanbieden van bonussen verboden moet worden, zoals gratis inzet bij het openen van een account. Dat wordt nog uitgewerkt in een wetsvoorstel; een ingangsdatum is er nog niet.</li></ul>
<p>Welke free bets er nu zijn, en onder welke voorwaarden, zie je op onze pagina met <a href="/bonussen/free-bets">free bets</a>.</p>"""

content3 = f"""<h3><strong>Waarom bookmakers matched bettors beperken</strong></h3>
<p>Een bookmaker geeft een bonus om je als klant te houden, niet om je €6 cadeau te doen. Wie alleen bonussen pakt en altijd afdekt, valt op. In de algemene voorwaarden staat bijna altijd dat de bookmaker bonussen kan weigeren of intrekken bij "bonusmisbruik", en dat hij de maximale inzet per klant mag verlagen. In het Engels heet dat <em>gubbing</em> of <em>account limiting</em>: je account blijft open, maar je krijgt geen promoties meer of je mag nog maar kleine bedragen inzetten. Je hebt geen recht op bonussen.</p>
<p>Lees daarom altijd de bonusvoorwaarden. Let vooral op:</p>
<ul><li><strong>Minimale odd:</strong> de kwalificerende inzet telt vaak pas vanaf een bepaalde quotering.</li><li><strong>Uitgesloten markten:</strong> soms tellen draw no bet, handicap of live weddenschappen niet mee.</li><li><strong>Geldigheid:</strong> een free bet vervalt vaak na een paar dagen.</li><li><strong>Inzetvoorwaarden:</strong> bij een bonus in plaats van een free bet moet je soms eerst een veelvoud inzetten voordat je kunt opnemen. Dat verandert het rekenwerk flink.</li><li><strong>Eén account per persoon:</strong> meerdere accounts bij dezelfde aanbieder is niet toegestaan.</li></ul>
<h3><strong>De risico's van matched betting</strong></h3>
<ul><li><strong>Fouten bij het invullen:</strong> een verkeerde inzet, verkeerde odd of verkeerde markt maakt van een gedekte weddenschap een gewone gok.</li><li><strong>Bewegende odds:</strong> als de dekkingsodd zakt tussen je eerste en tweede weddenschap, klopt je berekening niet meer.</li><li><strong>Verschillende regels per bookmaker:</strong> bij een gestaakte wedstrijd of een speler die niet start in tennis kan de ene bookmaker je weddenschap ongeldig verklaren en de andere niet. Dan ben je in één klap niet meer gedekt.</li><li><strong>Kapitaal en limieten:</strong> je geld staat verspreid over meerdere accounts, terwijl de stortingslimiet per aanbieder geldt.</li><li><strong>Gokgedrag:</strong> de verleiding om een free bet "gewoon even te spelen" zonder dekking is groot. Dan is het geen matched betting meer.</li></ul>
<p>Lijkt matched betting op arbitrage? Een beetje. Bij <a href="/nieuws/wat-is-arbitrage-wedden-de-kunst-van-de-risicovrije-winst">arbitrage wedden</a> haal je winst uit oddsverschillen tussen bookmakers, zonder bonus. Bij <a href="/nieuws/wat-is-de-wedstrategie-value-betting">value betting</a> accepteer je juist risico, omdat je denkt dat een quotering te hoog is. Alle strategieën naast elkaar vind je in ons overzicht van <a href="/nieuws/alle-verschillende-wedstrategieen-op-een-rijtje">wedstrategieën</a>.</p>
<h3><strong>Mag je matched betting doen in Nederland?</strong></h3>
<p>Ja, matched betting zelf is niet verboden: je plaatst gewone weddenschappen bij legale bookmakers. Wel is het belangrijk dat je alleen speelt bij aanbieders met een vergunning van de Kansspelautoriteit. Die controleren bij registratie je identiteit en checken in Cruks of je jezelf hebt uitgesloten. Twijfel je over een site, lees dan <a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je weet of een bookmaker legaal is</a>.</p>
<p>Belasting is bij een legale bookmaker geen probleem: de aanbieder betaalt de kansspelbelasting (37,8% in 2026) en jij ontvangt je winst zonder aftrek.</p>
<p>Legale bookmakers die wij aanraden:</p>
{aanraders()}
<h3><strong>Veelgestelde vragen over matched betting</strong></h3>
<p><strong>Is matched betting risicovrij?</strong><br>Nee. De berekening dekt de uitslag af, maar fouten, bewegende odds, ongeldig verklaarde weddenschappen en ingetrokken bonussen kunnen je geld kosten.</p>
<p><strong>Kun je in Nederland layen op een betting exchange?</strong><br>Niet legaal. Geen enkele Nederlandse vergunninghouder biedt een exchange aan. Je kunt alleen dekken door de andere uitkomst bij een tweede legale bookmaker te spelen.</p>
<p><strong>Wat is het verschil tussen SNR en SR?</strong><br>Bij stake not returned (SNR) krijg je bij winst alleen de winst van je free bet. Bij stake returned (SR) krijg je ook de inzet. Een SR free bet is daardoor meer waard.</p>
<p><strong>Hoeveel kun je verdienen met matched betting?</strong><br>Bij een SNR free bet houd je meestal 50 tot 80% van de waarde over, min het kwalificatieverlies. Met de kleine bonussen in Nederland, de limieten en het bonusverbod dat eraan komt, is het geen inkomstenbron.</p>
<p><strong>Mag een bookmaker mijn bonus intrekken?</strong><br>Als je de bonusvoorwaarden niet naleeft, ja. Lees ze voordat je begint, en bewaar screenshots van je weddenschappen en de actievoorwaarden.</p>
<p><strong>Moet ik belasting betalen over winst uit matched betting?</strong><br>Niet bij een bookmaker met een Nederlandse vergunning; die draagt de kansspelbelasting af.</p>
<p><strong>Wat als ik jonger ben dan 24?</strong><br>Dan mag een aanbieder zijn reclame, en dus ook bonussen, niet op jou richten. Matched betting is voor jou in de praktijk nauwelijks mogelijk.</p>
<p>Wedden blijft een kansspel. Merk je dat je meer inzet dan je wilt, kijk dan op onze pagina over <a href="/speel-bewust/verantwoord-wedden">verantwoord wedden</a>.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    import re
    from datetime import datetime, timezone
    alles = content + content2 + content3
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK, "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    tekst = re.sub(r"<[^>]+>", " ", alles)
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", len(tekst.split()), "woorden")
    assert not re.search(r"<(ul|ol|/li)>\s+<", alles) and "/kennisbank/" not in alles
    if "--live" in sys.argv:   # ---- LIVE: alleen na akkoord van de gebruiker ----
        print(WF.create_live(fd))
