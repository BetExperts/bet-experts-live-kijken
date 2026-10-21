# -*- coding: utf-8 -*-
"""Nieuw Nieuws-artikel: Asian totaal / Asian over-under (meer dan / minder dan doelpunten).
Uitkomsten en bedragen via og_kaarten/asian_rekenen.py (zelfde rekenregels als de tabel en asian_handicap.py).
Tabel + pdf + rekenvisual: be-static (og_kaarten/asian.py); deelkaart og/nieuws/asian-totaal.webp (og_kaarten/asian_totaal_og.py).
  python3 specials/asian_totaal.py [--live]"""
import os, sys, re
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, os.path.join(HIER, "..", "og_kaarten"))
sys.path.insert(0, HIER)
import lk_webflow as WF
from legaal_data import tabel, aanraders
from asian_rekenen import totaal, uitbetaling

SLUG = "wat-is-asian-totaal-asian-over-under"
TITEL = "Asian over/under (Asian totaal): uitleg met tabel en voorbeelden"
SAMENVATTING = ("Asian over/under uitgelegd: meer dan en minder dan 2, 2,25, 2,5 en 2,75 doelpunten, inzet terug en halve "
                "winst. Met tabel, voorbeelden en gratis pdf.")
RUBRIEK = "6502b66cd9992658b4037cf5"   # Speluitleg
STATIC = "https://www.bet-experts.nl/be-static/"
OG = "https://raw.githubusercontent.com/BetExperts/bet-experts-live-kijken/main/og/nieuws/asian-totaal.webp"
AT_IMG, AT_PDF = STATIC + "asian-totaal-tabel-d39cc290.webp", STATIC + "asian-totaal-tabel-fd278613.pdf"
VB_AT = STATIC + "asian-vis-totaal-a20cd546.webp"
AH = "/nieuws/wat-is-een-asian-handicap-weddenschap"
LABEL = {1: "winst", 0.5: "halve winst", 0: "inzet terug", -0.5: "half verlies", -1: "verlies"}


def eur(x):
    return f"€{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def nl(x):
    return f"{x:.2f}".rstrip("0").rstrip(".").replace(".", ",")


def tot(lijn, goals, odd, over=True, inzet=10):
    return eur(uitbetaling(totaal(lijn, goals, over), inzet, odd))


def figuur(src, alt, onderschrift):
    return (f'<figure class="w-richtext-align-fullwidth w-richtext-figure-type-image" style="max-width:100%"><div>'
            f'<img src="{src}" alt="{alt}" loading="lazy"></div><figcaption>{onderschrift}</figcaption></figure>')


def uitkomsten(lijn, over):
    """'3+ doelpunten: winst · 2: half verlies · 0-1: verlies' uit de rekenregels (0..6 doelpunten)."""
    groepen = []
    for g in range(0, 7):
        u = LABEL[totaal(lijn, g, over)]
        if groepen and groepen[-1][1] == u: groepen[-1][0].append(g)
        else: groepen.append([[g], u])
    def bereik(gs):
        if gs[-1] == 6: return f"{gs[0]} of meer"
        return str(gs[0]) if len(gs) == 1 else f"{gs[0]} t/m {gs[-1]}"
    return " · ".join(f"{bereik(gs)}: {u}" for gs, u in (groepen if over else groepen))


# controle tegen de rekenregels (en dus de tabel en de visual)
assert tot(2.25, 2, 1.85) == "€5,00" and tot(2.25, 3, 1.85) == "€18,50" and tot(2.25, 1, 1.85) == "€0,00"
assert tot(2, 2, 1.80) == "€10,00" and tot(2, 3, 1.80) == "€18,00"
assert tot(2.75, 3, 1.95) == "€14,75" and tot(2.75, 4, 1.95) == "€19,50" and tot(2.75, 2, 1.95) == "€0,00"
assert tot(2.25, 2, 1.95, False) == "€14,75" and tot(2.25, 1, 1.95, False) == "€19,50" and tot(2.25, 3, 1.95, False) == "€0,00"
assert tot(2.75, 3, 1.90, False) == "€5,00" and tot(2.75, 2, 1.90, False) == "€19,00"
assert tot(3, 3, 2.05) == "€10,00" and tot(3, 4, 2.05) == "€20,50"
assert uitkomsten(2.25, True) == "0 t/m 1: verlies · 2: half verlies · 3 of meer: winst"

LIJNEN = [1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5]

content = f"""<p><strong>Asian over/under, ook Asian totaal genoemd, is een weddenschap op het totaal aantal doelpunten in een wedstrijd: je kiest meer dan of minder dan een lijn. Anders dan bij een gewone over/under is de lijn niet altijd een halve, zoals 2,5. Bij een hele lijn (zoals meer dan 2) krijg je je inzet terug als het aantal doelpunten precies op de lijn valt. Bij een kwartlijn (zoals meer dan 2,25) wordt je inzet in tweeën gesplitst, zodat je ook half kunt winnen of half kunt verliezen. Zo verklein je het risico of krijg je een hogere quotering.</strong></p>
<p>De Asian over/under komt uit dezelfde familie als de <a href="{AH}">Asian handicap</a> en werkt met precies dezelfde rekenregels, alleen draait het hier niet om het doelsaldo maar om het totaal aantal goals. Hieronder lees je stap voor stap hoe het werkt, zie je per lijn wat er met je inzet gebeurt en reken je met voorbeelden in euro's mee. De volledige tabel kun je gratis als pdf downloaden.</p>
<h3><strong>Hoe werkt Asian over/under?</strong></h3>
<ol><li><strong>Kies een lijn,</strong> bijvoorbeeld 2,25 doelpunten.</li><li><strong>Kies meer dan (over) of minder dan (under).</strong> Meer dan 2,25 betekent dat je rekent op een wedstrijd met veel doelpunten.</li><li><strong>Tel na de wedstrijd alle doelpunten bij elkaar op.</strong> Bij 2-1 zijn dat er 3, bij 1-1 zijn het er 2. Alleen de reguliere speeltijd inclusief blessuretijd telt, verlenging en strafschoppen niet.</li><li><strong>Vergelijk het totaal met je lijn.</strong> Ligt het totaal aan jouw kant van de lijn, dan win je. Valt het precies op een hele lijn, dan krijg je je inzet terug. Bij een kwartlijn kijk je per helft van je inzet.</li></ol>
<h3><strong>Halve, hele en kwartlijnen</strong></h3>
{tabel(["Soort lijn", "Voorbeelden", "Wat kan er gebeuren?"], [
    ("<strong>Halve lijn</strong>", "1,5 / 2,5 / 3,5", "Alleen winst of verlies. Een halve goal bestaat niet, dus het totaal valt nooit precies op de lijn. Dit is de gewone over/under."),
    ("<strong>Hele lijn</strong>", "2 / 3 / 4", "Winst, verlies of <strong>inzet terug</strong> als het aantal doelpunten precies gelijk is aan de lijn."),
    ("<strong>Kwartlijn</strong>", "1,75 / 2,25 / 2,75 / 3,25", "Je inzet gaat half op de lijn eronder en half op de lijn erboven. Daardoor kun je ook <strong>half winnen</strong> of <strong>half verliezen</strong>."),
])}
<p><strong>Kwartlijnen uitgelegd.</strong> Meer dan 2,25 is de helft van je inzet op meer dan 2 en de helft op meer dan 2,5. Meer dan 2,75 is de helft op meer dan 2,5 en de helft op meer dan 3. Bookmakers schrijven kwartlijnen daarom ook als <strong>2/2,5</strong> of <strong>2,5/3</strong>. Dat betekent hetzelfde.</p>
<h3><strong>Asian totaal tabel: alle lijnen in één overzicht</strong></h3>
<p>In de tabel zie je voor elke lijn van 1,5 tot 3,5 doelpunten, voor meer dan en minder dan, wat er met je inzet gebeurt bij 0 tot 5 of meer doelpunten. Groen is winst, lichtgroen halve winst, grijs inzet terug, roze half verlies en rood verlies.</p>
{figuur(AT_IMG, "Asian totaal tabel: per lijn van 1,5 tot 3,5 voor meer dan en minder dan, en per aantal doelpunten van 0 tot 5 of meer, of je wint, half wint, je inzet terugkrijgt, half verliest of verliest", "Asian over/under tabel: kies je lijn (rij) en kijk hoeveel doelpunten er vallen (kolom)")}
<p><strong><a href="{AT_PDF}" target="_blank">📄 Download de Asian totaal tabel als pdf (A4)</a></strong></p>"""

content2 = f"""<h3><strong>Meer dan: alle lijnen in gewone taal</strong></h3>
{tabel(["Lijn", "Wat gebeurt er bij hoeveel doelpunten?"], [(f"<strong>Meer dan {nl(l)}</strong>", uitkomsten(l, True)) for l in LIJNEN])}
<h3><strong>Minder dan: alle lijnen in gewone taal</strong></h3>
{tabel(["Lijn", "Wat gebeurt er bij hoeveel doelpunten?"], [(f"<strong>Minder dan {nl(l)}</strong>", uitkomsten(l, False)) for l in LIJNEN])}
<p>Meer dan en minder dan op dezelfde lijn zijn elkaars spiegelbeeld. Wat bij meer dan 2,25 half verlies is, is bij minder dan 2,25 halve winst.</p>
<h3><strong>Rekenvoorbeelden: zo reken je Asian over/under uit</strong></h3>
<p>Bij een kwartlijn reken je per helft van je inzet. Bij <strong>halve winst</strong> wint de ene helft tegen de quotering en krijg je de andere helft terug. Bij <strong>half verlies</strong> ben je de ene helft kwijt en krijg je de andere helft terug. De bedragen zijn wat je in totaal terugkrijgt, inclusief je inzet.</p>
{figuur(VB_AT, "Rekenvoorbeeld Asian over/under: 10 euro op meer dan 2,25 doelpunten tegen odd 1,85. 0 of 1 doelpunt: 0 euro. Precies 2 doelpunten: half verlies, 5 euro. 3 of meer doelpunten: 18,50 euro", "Rekenvoorbeeld: €10 op meer dan 2,25 doelpunten, verdeeld over meer dan 2 en meer dan 2,5")}
<p><strong>Voorbeeld 1: meer dan 2,25 doelpunten (odd 1,85, inzet €10)</strong></p>
<ul><li>0 of 1 doelpunt: beide helften verliezen. Je krijgt <strong>{tot(2.25, 1, 1.85)}</strong>.</li><li>Precies 2 doelpunten: de €5 op meer dan 2 is een push (€5 terug), de €5 op meer dan 2,5 verliest. Je krijgt <strong>{tot(2.25, 2, 1.85)}</strong>: half verlies.</li><li>3 of meer doelpunten: beide helften winnen. Je krijgt <strong>{tot(2.25, 3, 1.85)}</strong>.</li></ul>
<p><strong>Voorbeeld 2: meer dan 2 doelpunten (odd 1,80, inzet €10)</strong></p>
<ul><li>Precies 2 doelpunten: je krijgt je volledige inzet terug, <strong>{tot(2, 2, 1.80)}</strong>.</li><li>3 of meer doelpunten: <strong>{tot(2, 3, 1.80)}</strong>.</li><li>0 of 1 doelpunt: <strong>{tot(2, 1, 1.80)}</strong>.</li></ul>
<p><strong>Voorbeeld 3: meer dan 2,75 doelpunten (odd 1,95, inzet €10)</strong></p>
<ul><li>2 doelpunten of minder: <strong>{tot(2.75, 2, 1.95)}</strong>.</li><li>Precies 3 doelpunten: de €5 op meer dan 2,5 wint (€9,75), de €5 op meer dan 3 is een push (€5). Samen <strong>{tot(2.75, 3, 1.95)}</strong>: halve winst.</li><li>4 doelpunten of meer: <strong>{tot(2.75, 4, 1.95)}</strong>.</li></ul>
<p><strong>Voorbeeld 4: minder dan 2,25 doelpunten (odd 1,95, inzet €10)</strong></p>
<ul><li>0 of 1 doelpunt: <strong>{tot(2.25, 1, 1.95, False)}</strong>.</li><li>Precies 2 doelpunten: de €5 op minder dan 2 is een push, de €5 op minder dan 2,5 wint. Samen <strong>{tot(2.25, 2, 1.95, False)}</strong>: halve winst.</li><li>3 doelpunten of meer: <strong>{tot(2.25, 3, 1.95, False)}</strong>.</li></ul>
<p><strong>Voorbeeld 5: minder dan 2,75 doelpunten (odd 1,90, inzet €10)</strong></p>
<ul><li>2 doelpunten of minder: <strong>{tot(2.75, 2, 1.90, False)}</strong>.</li><li>Precies 3 doelpunten: de €5 op minder dan 2,5 verliest, de €5 op minder dan 3 is een push. Je krijgt <strong>{tot(2.75, 3, 1.90, False)}</strong>: half verlies.</li><li>4 doelpunten of meer: <strong>{tot(2.75, 4, 1.90, False)}</strong>.</li></ul>
<p><em>De quoteringen in deze voorbeelden zijn fictief en alleen bedoeld om de berekening te laten zien.</em></p>"""

content3 = f"""<h3><strong>Asian over/under of gewone over/under 2,5?</strong></h3>
{tabel(["", "Gewone over/under", "Asian over/under"], [
    ("<strong>Lijnen</strong>", "Alleen halve lijnen: 1,5 / 2,5 / 3,5", "Ook hele en kwartlijnen: 2 / 2,25 / 2,75 / 3"),
    ("<strong>Uitkomsten</strong>", "Winst of verlies", "Winst, halve winst, inzet terug, half verlies of verlies"),
    ("<strong>Risico</strong>", "Eén doelpunt te weinig en je inzet is weg", "Bij hele en kwartlijnen ben je niet altijd meteen alles kwijt"),
    ("<strong>Quoteringen</strong>", "Vaste stappen per halve goal", "Fijnere stappen, vaak beide kanten rond 1,90"),
])}
<p>Twijfel je tussen meer dan 2,5 en meer dan 3,5? Dan zit er bij de Asian over/under altijd een lijn tussen. Meer dan 2,75 betaalt meer uit dan meer dan 2,5, maar bij precies 3 doelpunten win je maar de helft. Meer dan 2,25 betaalt minder dan meer dan 2,5, maar bij precies 2 doelpunten krijg je de helft van je inzet terug. Zo kies je zelf hoeveel risico je neemt.</p>
<h3><strong>Wanneer kies je welke lijn?</strong></h3>
<ul><li><strong>Verwacht je een open wedstrijd, maar twijfel je over het derde doelpunt?</strong> Dan beschermt meer dan 2,25 of meer dan 2 je bij precies 2 doelpunten.</li><li><strong>Ben je zeker van veel doelpunten?</strong> Dan geeft meer dan 2,75 of meer dan 3 een hogere quotering, met een vangnet bij precies 3 doelpunten.</li><li><strong>Verwacht je een gesloten wedstrijd?</strong> Minder dan 2,75 wint ook bij 2 doelpunten volledig en kost je bij precies 3 doelpunten maar de helft van je inzet.</li><li><strong>Kijk naar de statistieken.</strong> Hoe vaak eindigen wedstrijden van beide ploegen boven of onder de 2,5? Onze <a href="/wedtips/over-2-5-goals-tips-voorspellingen">over 2,5 goals tips</a> en <a href="/wedtips/btts-tips-voorspellingen">BTTS-tips</a> helpen je op weg.</li></ul>
<h3><strong>Tips en valkuilen</strong></h3>
<ul><li><strong>Let op de schrijfwijze.</strong> 2,25 en 2/2,5 zijn dezelfde lijn. Kijk ook goed of je meer dan of minder dan aanklikt.</li><li><strong>Alleen de reguliere speeltijd telt.</strong> Doelpunten in de verlenging of strafschoppen tellen niet mee, blessuretijd wel.</li><li><strong>Check de regels bij live wedden.</strong> Bij een live over/under schuift de lijn mee met de stand. Lees bij je bookmaker of het totaal over de hele wedstrijd telt of alleen vanaf het moment van je inzet.</li><li><strong>Ook voor de eerste helft.</strong> Veel bookmakers bieden Asian lijnen ook aan voor alleen de eerste helft, vaak rond de 0,75 of 1 doelpunt.</li><li><strong>Vergelijk quoteringen.</strong> Een verschil van 1,85 of 1,95 tikt op lange termijn flink aan. Gebruik onze <a href="/odds-vergelijken-bij-alle-bookmakers-beste-odds-vandaag">odds vergelijker</a>.</li></ul>
<h3><strong>Mag je in Nederland wedden op Asian over/under?</strong></h3>
<p>Ja. Wedden op het totaal aantal doelpunten, ook met Asian lijnen, is toegestaan bij bookmakers met een vergunning van de Kansspelautoriteit. Let op: over/under op corners of kaarten mag in Nederland niet, die gebeurtenissen staan op de lijst met verboden weddenschappen. Lees <a href="/nieuws/dit-is-waarom-wedden-op-corners-niet-meer-legaal-is-in-nederland">waarom wedden op corners niet legaal is</a>. Niet elke legale bookmaker biedt alle kwartlijnen aan; je vindt ze vaak onder namen als "Aziatisch totaal", "Asian lines" of "totaal aantal doelpunten (Aziatisch)".</p>
<p>Legale bookmakers die wij aanraden:</p>
{aanraders()}
<h3><strong>Veelgestelde vragen over Asian over/under</strong></h3>
<p><strong>Wat is Asian over/under?</strong><br>Een weddenschap op meer of minder dan een aantal doelpunten, waarbij naast halve lijnen ook hele lijnen en kwartlijnen bestaan. Daardoor kun je je inzet terugkrijgen, half winnen of half verliezen.</p>
<p><strong>Wat betekent meer dan 2,25 doelpunten?</strong><br>De helft van je inzet staat op meer dan 2 en de helft op meer dan 2,5. Bij 3 of meer doelpunten win je alles, bij precies 2 krijg je de helft terug en bij 0 of 1 verlies je.</p>
<p><strong>Wat betekent meer dan 2,75 doelpunten?</strong><br>De helft van je inzet staat op meer dan 2,5 en de helft op meer dan 3. Bij 4 of meer doelpunten win je alles, bij precies 3 is het halve winst en bij 2 of minder verlies je.</p>
<p><strong>Wat gebeurt er bij meer dan 2 en precies 2 doelpunten?</strong><br>Dan krijg je je volledige inzet terug. Dat heet een push.</p>
<p><strong>Is Asian totaal hetzelfde als Asian over/under?</strong><br>Ja. Asian totaal, Asian over/under, Aziatisch totaal en Asian goal line zijn verschillende namen voor dezelfde markt.</p>
<p><strong>Wat is het verschil met de Asian handicap?</strong><br>Bij de <a href="{AH}">Asian handicap</a> gaat het om het doelsaldo tussen twee teams, bij Asian over/under om het totaal aantal doelpunten. De rekenregels voor hele lijnen en kwartlijnen zijn hetzelfde.</p>
<p><strong>Tellen eigen doelpunten mee?</strong><br>Ja. Elk doelpunt dat op het scorebord komt in de reguliere speeltijd telt mee, ook een eigen doelpunt of een benutte strafschop.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    html = content + content2 + content3
    assert not re.search(r"<(ul|ol|/li)>\s+<", html) and "/kennisbank/" not in html and "<h2" not in html
    tekst = re.sub(r"<[^>]+>", " ", html)
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", len(tekst.split()), "woorden")
    if "--live" in sys.argv:
        og = {"url": OG, "alt": "Wat is Asian over/under? Uitleg met tabel"}
        fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
              "samenvatting": SAMENVATTING, "rubriek": RUBRIEK, "wedgids": True, "afbeelding": og, "seo-afbeelding": og,
              "publicatiedatum": datetime.now(timezone.utc).isoformat()}
        print("item:", WF.create_live(fd))
