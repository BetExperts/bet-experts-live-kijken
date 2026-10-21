# -*- coding: utf-8 -*-
"""Los artikel (evergreen): Pokerhanden uitgelegd, alle combinaties op volgorde. Kansen: standaard combinatoriek
(52 kaarten; 2.598.960 vijfkaartshanden, 133.784.560 zevenkaartscombinaties voor Texas Hold'em).
Infographic + pdf: og_kaarten/pokerhanden.py -> be-static.
  python3 specials/pokerhanden.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Pokerhanden uitgelegd: alle poker combinaties op volgorde"
SLUG = "pokerhanden"
SAMENVATTING = ("Alle pokerhanden op volgorde, van royal flush tot high card. Met uitleg, voorbeelden, kansen, de "
                "kickerregel en een gratis pdf.")
RUBRIEK_CASINO = "6656fda64a14a528f93c6af8"
STATIC = "https://www.bet-experts.nl/be-static/"
IMG = STATIC + "pokerhanden-infographic-67dc6f2a.webp"
PDF = STATIC + "pokerhanden-infographic-8792ce0a.pdf"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


INFOGRAPHIC = (f'<figure class="w-richtext-align-fullwidth w-richtext-figure-type-image" style="max-width:100%">'
               f'<div><img src="{IMG}" alt="Infographic pokerhanden op volgorde: royal flush, straight flush, four of a '
               f'kind, full house, flush, straight, three of a kind, two pair, one pair en high card, met kansen" '
               f'loading="lazy"></div><figcaption>Alle pokerhanden op volgorde, van sterk naar zwak</figcaption></figure>'
               f'<p><strong><a href="{PDF}" target="_blank">📄 Download het overzicht van alle pokerhanden als pdf (A4)</a></strong></p>')

content = f"""<p><strong>In poker zijn er tien handen, van sterk naar zwak: royal flush, straight flush, four of a kind, full house, flush, straight, three of a kind, two pair, one pair en high card. Je hand bestaat altijd uit de beste vijf kaarten die je kunt maken. Hebben twee spelers dezelfde soort hand, dan wint de hoogste combinatie, en is die ook gelijk, dan beslist de hoogste losse kaart (de kicker). De kleur van de kaarten telt nooit mee voor de rangorde.</strong></p>
<p>Of je nu net begint met Texas Hold'em of je kennis wilt opfrissen: in dit artikel lees je welke pokerhand wint, met voorbeelden, de regels bij een gelijke hand, de kans op elke combinatie en de fouten die beginners het vaakst maken. Je kunt het hele overzicht ook als pdf downloaden om naast je te leggen tijdens het spelen.</p>
<h3><strong>Pokerhanden op volgorde: het overzicht</strong></h3>
{tabel(["#", "Pokerhand", "Voorbeeld", "Wat is het?"], [
    ("1", "<strong>Royal flush</strong>", "A♥ K♥ Q♥ J♥ 10♥", "10 tot en met aas van dezelfde kleur"),
    ("2", "<strong>Straight flush</strong>", "9♠ 8♠ 7♠ 6♠ 5♠", "Vijf opeenvolgende kaarten van dezelfde kleur"),
    ("3", "<strong>Four of a kind</strong> (carré)", "Q♣ Q♦ Q♥ Q♠ 7♦", "Vier kaarten van dezelfde waarde"),
    ("4", "<strong>Full house</strong>", "8♦ 8♠ 8♣ K♥ K♣", "Drie van dezelfde waarde plus een paar"),
    ("5", "<strong>Flush</strong>", "A♦ J♦ 9♦ 6♦ 2♦", "Vijf kaarten van dezelfde kleur"),
    ("6", "<strong>Straight</strong> (straat)", "10♣ 9♦ 8♠ 7♥ 6♣", "Vijf opeenvolgende kaarten"),
    ("7", "<strong>Three of a kind</strong>", "5♥ 5♣ 5♠ K♦ 2♣", "Drie kaarten van dezelfde waarde"),
    ("8", "<strong>Two pair</strong>", "J♠ J♥ 4♣ 4♦ A♠", "Twee verschillende paren"),
    ("9", "<strong>One pair</strong>", "10♥ 10♠ K♣ 7♦ 3♠", "Twee kaarten van dezelfde waarde"),
    ("10", "<strong>High card</strong>", "A♣ Q♦ 9♥ 6♠ 3♦", "Geen combinatie: de hoogste kaart telt"),
])}
<p>De kaartwaarden lopen van laag naar hoog: 2, 3, 4, 5, 6, 7, 8, 9, 10, boer (J), vrouw (Q), heer (K) en aas (A). De aas is de hoogste kaart, maar mag in een straat ook als laagste kaart dienen (A-2-3-4-5).</p>
{INFOGRAPHIC}"""

content2 = f"""<h3><strong>Alle pokerhanden uitgelegd</strong></h3>
<p><strong>1. Royal flush</strong><br>De beste hand in poker: 10, boer, vrouw, heer en aas, allemaal van dezelfde kleur. Er zijn maar vier royal flushes mogelijk, één per kleur. Een royal flush is eigenlijk de hoogst mogelijke straight flush, maar krijgt vanwege de zeldzaamheid een eigen naam.</p>
<p><strong>2. Straight flush</strong><br>Vijf opeenvolgende kaarten van dezelfde kleur, zoals 5-6-7-8-9 in schoppen. Hebben twee spelers een straight flush, dan wint degene met de hoogste kaart bovenaan de reeks. De laagste straight flush is A-2-3-4-5 van één kleur.</p>
<p><strong>3. Four of a kind (carré)</strong><br>Vier kaarten van dezelfde waarde, aangevuld met één losse kaart. Vier vrouwen verslaan vier boeren. In Texas Hold'em kunnen alle vier de kaarten op tafel liggen; dan beslist de vijfde kaart (de kicker) wie wint.</p>
<p><strong>4. Full house</strong><br>Drie kaarten van dezelfde waarde plus een paar, bijvoorbeeld drie achten en twee heren ("achten vol met heren"). Bij twee full houses telt eerst de drieling: 8-8-8-2-2 wint van 7-7-7-A-A. Pas als de drieling gelijk is, kijk je naar het paar.</p>
<p><strong>5. Flush</strong><br>Vijf kaarten van dezelfde kleur, maar niet op volgorde. Bij twee flushes vergelijk je de hoogste kaart, dan de tweede, enzovoort. Een flush met de aas als hoogste kaart heet een nut flush wanneer niemand een hogere flush kan hebben.</p>
<p><strong>6. Straight (straat)</strong><br>Vijf opeenvolgende kaarten van verschillende kleuren. De hoogste straat is 10-J-Q-K-A (broadway), de laagste A-2-3-4-5 (de wheel). Een straat "om de hoek", zoals Q-K-A-2-3, telt niet. Bij twee straten wint de straat met de hoogste kaart.</p>
<p><strong>7. Three of a kind</strong><br>Drie kaarten van dezelfde waarde met twee losse kaarten. In Texas Hold'em heet het een <em>set</em> als je een paar in je hand hebt en de derde kaart op tafel ligt, en <em>trips</em> als er een paar op tafel ligt en jij de derde kaart hebt.</p>
<p><strong>8. Two pair</strong><br>Twee verschillende paren plus een losse kaart. Bij een gelijke stand telt eerst het hoogste paar, dan het tweede paar en dan de kicker. Heb je met zeven kaarten drie paren, dan tellen alleen de twee hoogste.</p>
<p><strong>9. One pair</strong><br>Twee kaarten van dezelfde waarde. Het hoogste paar wint; bij hetzelfde paar beslissen de drie losse kaarten, van hoog naar laag. Een paar azen in je starthand (pocket aces) is de sterkste starthand in Texas Hold'em, maar je krijgt hem gemiddeld maar één keer per 221 handen.</p>
<p><strong>10. High card</strong><br>Geen paar, straat of flush? Dan telt je hoogste kaart. Heeft je tegenstander ook een aas als hoogste kaart, dan vergelijk je de tweede kaart, enzovoort.</p>
<h3><strong>Wie wint bij een gelijke pokerhand?</strong></h3>
<p>Hebben twee spelers dezelfde soort hand, dan bepalen drie regels de winnaar:</p>
<ul><li><strong>De hoogste combinatie wint.</strong> Een paar heren verslaat een paar boeren, een flush met een aas verslaat een flush met een heer.</li><li><strong>Daarna beslist de kicker.</strong> Hebben beide spelers een paar heren, dan wint de speler met de hoogste losse kaart. Je hand bestaat altijd uit precies vijf kaarten, dus de zesde en zevende kaart tellen nooit mee.</li><li><strong>Helemaal gelijk? Dan wordt de pot gedeeld.</strong> Dit heet een split pot. Dat gebeurt bijvoorbeeld als de beste vijf kaarten allemaal op tafel liggen (de board speelt).</li></ul>
<p>De kleur van de kaarten (harten, ruiten, klaveren of schoppen) maakt bij standaardpoker nooit uit. Een flush in harten is niet sterker dan een flush in klaveren met dezelfde kaartwaarden.</p>"""

content3 = f"""<h3><strong>Hoe groot is de kans op elke pokerhand?</strong></h3>
<p>Hoe zeldzamer een hand, hoe hoger hij staat. In de tabel zie je de kans op elke hand met vijf willekeurige kaarten (zoals in five card draw) en de kans dat het je beste hand is met zeven kaarten, zoals in Texas Hold'em (twee eigen kaarten plus vijf op tafel).</p>
{tabel(["Pokerhand", "Kans met 5 kaarten", "Ongeveer 1 op", "Kans met 7 kaarten (Hold'em)"], [
    ("Royal flush", "0,00015%", "649.740", "0,003%"),
    ("Straight flush", "0,0014%", "72.193", "0,03%"),
    ("Four of a kind", "0,024%", "4.165", "0,17%"),
    ("Full house", "0,14%", "694", "2,6%"),
    ("Flush", "0,20%", "509", "3,0%"),
    ("Straight", "0,39%", "255", "4,6%"),
    ("Three of a kind", "2,1%", "47", "4,8%"),
    ("Two pair", "4,8%", "21", "23,5%"),
    ("One pair", "42,3%", "2,4", "43,8%"),
    ("High card", "50,1%", "2", "17,4%"),
])}
<p><em>Berekend over alle 2.598.960 mogelijke handen van vijf kaarten en alle 133.784.560 combinaties van zeven kaarten uit een spel van 52.</em></p>
<p>Opvallend: met zeven kaarten is high card (17,4%) zeldzamer dan one pair (43,8%) en two pair (23,5%). Met zoveel kaarten heb je bijna altijd wel een paar. Daarom is een paar in Texas Hold'em vaak niet genoeg om te winnen.</p>
<h3><strong>Veelgemaakte fouten met pokerhanden</strong></h3>
<ul><li><strong>Een straat om de hoek bestaat niet.</strong> Q-K-A-2-3 is geen straat. De aas is óf hoog (10-J-Q-K-A) óf laag (A-2-3-4-5).</li><li><strong>Een flush verslaat een straat.</strong> Veel beginners denken andersom, maar een flush is zeldzamer en dus sterker.</li><li><strong>Je hand is altijd vijf kaarten.</strong> In Texas Hold'em maak je de beste vijf uit zeven kaarten. Je mag daarvoor twee, één of zelfs geen van je eigen kaarten gebruiken.</li><li><strong>Twee drielingen is een full house.</strong> Heb je met zeven kaarten 9-9-9 en 4-4-4, dan speel je 9-9-9-4-4.</li><li><strong>Kleur telt niet bij een gelijke stand.</strong> Er bestaat geen "hogere" kleur in standaardpoker.</li><li><strong>In Omaha gelden andere regels.</strong> Daar moet je precies twee van je vier eigen kaarten en precies drie kaarten van tafel gebruiken.</li></ul>
<h3><strong>Geldt deze volgorde bij elke pokervariant?</strong></h3>
<p>De rangorde in dit artikel geldt voor vrijwel alle populaire varianten: Texas Hold'em, Omaha, Seven Card Stud en Five Card Draw. Er zijn een paar uitzonderingen:</p>
<ul><li><strong>Short Deck (Six Plus Hold'em):</strong> er wordt gespeeld zonder de 2 tot en met 5. Omdat een flush dan zeldzamer wordt, wint een flush van een full house. Bij veel tafels wint ook three of a kind van een straat; check de huisregels.</li><li><strong>Lowball-varianten (zoals Razz en 2-7 Triple Draw):</strong> hier wint juist de laagste hand.</li><li><strong>Hi-lo-varianten (zoals Omaha Hi-Lo):</strong> de pot wordt verdeeld tussen de hoogste en de laagste hand.</li></ul>
<h3><strong>Handige pokertermen</strong></h3>
{tabel(["Term", "Betekenis"], [
    ("Kicker", "De hoogste losse kaart die beslist bij een gelijke hand"),
    ("Nuts", "De best mogelijke hand op dat moment met de kaarten op tafel"),
    ("Quads", "Four of a kind"),
    ("Boat", "Full house"),
    ("Broadway", "De hoogste straat: 10-J-Q-K-A"),
    ("Wheel", "De laagste straat: A-2-3-4-5"),
    ("Set", "Drie gelijke kaarten met een paar in je eigen hand"),
    ("Trips", "Drie gelijke kaarten met een paar op tafel"),
    ("Suited", "Je twee eigen kaarten hebben dezelfde kleur"),
    ("Split pot", "De pot wordt gedeeld bij een volledig gelijke hand"),
])}
<h3><strong>Online poker spelen in Nederland</strong></h3>
<p>Online poker is in Nederland alleen legaal bij aanbieders met een vergunning van de Kansspelautoriteit. Daar gelden dezelfde beschermingsregels als bij online casino's en bookmakers: je stelt zelf limieten in en er geldt een <a href="/nieuws/netto-stortingslimiet">netto stortingslimiet</a> van €300 per maand tot 24 jaar en €700 daarna. Twijfel je of een site legaal is? Bekijk dan <a href="/nieuws/dit-zijn-de-casinos-die-op-dit-moment-legaal-zijn-in-nederland">welke casino's legaal zijn in Nederland</a>. Speel altijd met een vast budget, zie je inleg als uitgave en lees onze tips voor <a href="/speel-bewust/verantwoord-wedden">verantwoord spelen</a>.</p>
<h3><strong>Veelgestelde vragen over pokerhanden</strong></h3>
<p><strong>Wat is de hoogste pokerhand?</strong><br>De royal flush: 10, boer, vrouw, heer en aas van dezelfde kleur. Met vijf willekeurige kaarten is de kans ongeveer 1 op 649.740.</p>
<p><strong>Wat is hoger: een flush of een straat?</strong><br>Een flush. Vijf kaarten van dezelfde kleur zijn zeldzamer dan vijf opeenvolgende kaarten.</p>
<p><strong>Wat is hoger: een full house of een flush?</strong><br>Een full house. Alleen in Short Deck poker is het andersom.</p>
<p><strong>Telt de aas als hoge of lage kaart?</strong><br>Allebei. De aas is de hoogste kaart, maar je mag hem ook als laagste kaart gebruiken in de straat A-2-3-4-5.</p>
<p><strong>Wat is een kicker in poker?</strong><br>De hoogste losse kaart naast je combinatie. Die beslist als twee spelers dezelfde hand hebben, bijvoorbeeld allebei een paar heren.</p>
<p><strong>Wint harten van schoppen in poker?</strong><br>Nee. In standaardpoker hebben de kleuren geen rangorde. Bij een volledig gelijke hand wordt de pot gedeeld.</p>
<p><strong>Hoeveel kaarten telt een pokerhand?</strong><br>Altijd vijf. In Texas Hold'em kies je de beste vijf uit je twee eigen kaarten en de vijf kaarten op tafel.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_CASINO,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        import re
        tekst = re.sub(r"<[^>]+>", " ", content + content2 + content3)
        print(len(SAMENVATTING), "tekens samenvatting |", len(tekst.split()), "woorden"); sys.exit()
    print("item:", WF.create_live(fd))
