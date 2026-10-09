# -*- coding: utf-8 -*-
"""Los artikel (evergreen): Wat is een witte wissel? (feiten: IFAB-protocol maart 2024, KNVB vanaf 2024/25).
  python3 specials/witte_wissel.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Wat is een witte wissel en wanneer mag die worden gebruikt?"
SLUG = "wat-is-een-witte-wissel"
SAMENVATTING = ("Een witte wissel is een extra, definitieve wissel bij (een vermoeden van) een hersenschudding. Zo werkt "
                "de regel en dit krijgt de tegenstander.")
RUBRIEK_SPELUITLEG = "6502b66cd9992658b4037cf5"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in koppen)
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}><thead><tr>{kop}</tr></thead><tbody>{body}</tbody></table>"


content = f"""<p><strong>Een witte wissel is een extra wissel die een ploeg mag inzetten als een speler (mogelijk) een hersenschudding heeft. De wissel telt niet mee voor de vijf gewone wissels, de vervangen speler mag niet meer terugkomen en de tegenstander krijgt er direct ook een extra wissel bij. In Nederland geldt de witte wissel sinds het seizoen 2024/25 in het betaald voetbal.</strong></p>
<p>Wie naar de Eredivisie kijkt, ziet het af en toe gebeuren: na een botsing met het hoofd gaat een speler naar de kant, terwijl zijn ploeg al alle wissels heeft gebruikt. Toch komt er een vervanger in. Dat is de witte wissel. Hieronder lees je wat de regel precies inhoudt, wie bepaalt of hij wordt ingezet en in welke competities hij geldt.</p>
<h3><strong>Wat is een witte wissel?</strong></h3>
<p>De witte wissel is de Nederlandse naam voor wat internationaal een <em>additional permanent concussion substitute</em> heet: een aanvullende, definitieve wissel bij een hersenschudding. Het idee is eenvoudig. Een speler bij wie hoofdletsel wordt vermoed, moet zonder aarzeling van het veld kunnen. Een ploeg mag daar sportief niet voor worden gestraft, bijvoorbeeld door met tien man verder te moeten omdat de wissels op zijn.</p>
<p>Daarom staat de witte wissel helemaal los van de gewone wissels. Ook als een ploeg al vijf keer heeft gewisseld, kan een speler met (vermoedelijk) hoofdletsel nog worden vervangen.</p>
<h3><strong>De regels op een rij</strong></h3>
<ul><li>De wissel mag worden gebruikt bij een hersenschudding <strong>of een vermoeden daarvan</strong>; het hoeft niet medisch vast te staan.</li><li>Per ploeg mag maximaal <strong>één</strong> witte wissel per wedstrijd worden ingezet.</li><li>De wissel is <strong>definitief</strong>: de vervangen speler mag niet meer terug in het veld.</li><li>De wissel telt <strong>niet mee</strong> voor het gewone aantal wissels en wisselmomenten.</li><li>Zet een ploeg een witte wissel in, dan krijgt de <strong>tegenstander direct ook een extra wissel</strong> en een extra wisselmoment, ook als er bij die ploeg niemand geblesseerd is.</li></ul>
<h3><strong>Gewone wissel en witte wissel vergeleken</strong></h3>
{tabel(["", "Gewone wissel", "Witte wissel"], [
    ("Aantal per wedstrijd", "Vijf (in de reguliere speeltijd)", "Maximaal één per ploeg"),
    ("Reden", "Vrij: tactisch, vermoeidheid of blessure", "Alleen bij (vermoeden van) hersenschudding"),
    ("Wisselmoment", "Telt mee voor de drie wisselmomenten", "Telt niet mee"),
    ("Speler terug in het veld?", "Nee", "Nee"),
    ("Gevolg voor de tegenstander", "Geen", "Krijgt ook een extra wissel en wisselmoment"),
    ("Wie beslist?", "De trainer", "De medische staf van de ploeg"),
])}"""

content2 = """<h3><strong>Wie beslist over een witte wissel?</strong></h3>
<p>De beslissing ligt bij de ploeg zelf, en dan vooral bij de medische staf. Zij beoordelen of er sprake kan zijn van een hersenschudding. De scheidsrechter beslist daar niet over: die en de vierde official zorgen alleen dat de wissel volgens de regels verloopt. Bestaat er achteraf twijfel over het gebruik van een witte wissel, dan kan de wedstrijdleiding dat melden bij de bond.</p>
<p>Juist omdat de keuze bij de medische staf ligt, zit er geen drempel in de regel. Een speler die duizelig is, wazig ziet of zich na een klap tegen het hoofd niet goed voelt, kan direct worden gewisseld. Het motto in de sport is niet voor niets: bij twijfel, eruit.</p>
<h3><strong>Zo verloopt een witte wissel</strong></h3>
<ul><li>Een speler krijgt een klap tegen het hoofd of vertoont signalen van hoofdletsel.</li><li>De medische staf beoordeelt de speler en adviseert hem van het veld te halen.</li><li>De ploeg meldt bij de vierde official dat het om een witte wissel gaat.</li><li>De vervanger komt in het veld; de vervangen speler mag niet meer meedoen.</li><li>De tegenstander wordt geïnformeerd dat hij nu ook een extra wissel tot zijn beschikking heeft.</li></ul>
<h3><strong>Een voorbeeld uit de praktijk</strong></h3>
<p>Stel: in de 80e minuut heeft de thuisploeg al vijf keer gewisseld. Bij een kopduel botsen de centrale verdediger en een aanvaller van de tegenstander met de hoofden tegen elkaar. De verdediger is groggy en de dokter wil geen risico nemen. Zonder de witte wissel zou de thuisploeg de laatste tien minuten met tien man moeten spelen. Met de witte wissel komt er een nieuwe verdediger in, en mag de tegenstander, ook als die al vijf keer heeft gewisseld, eveneens nog één speler vervangen.</p>
<h3><strong>Waarom bestaat de witte wissel?</strong></h3>
<p>Een hersenschudding is niet altijd direct zichtbaar, en doorspelen met hoofdletsel kan gevaarlijk zijn. Vroeger kwam het voor dat spelers na een klap toch bleven staan, omdat hun ploeg anders met tien man verder moest. De regel haalt die afweging weg: de gezondheid van de speler gaat voor.</p>
<p>De internationale spelregelcommissie IFAB testte de extra wissel bij hersenschuddingen een aantal jaren in verschillende competities. In maart 2024 werd het protocol definitief goedgekeurd als mogelijkheid voor competities. De KNVB voerde de witte wissel na een eigen proefperiode vanaf het seizoen 2024/25 permanent in.</p>"""

content3 = f"""<h3><strong>Waar geldt de witte wissel?</strong></h3>
<p>De IFAB heeft de witte wissel niet verplicht gesteld: elke competitie bepaalt zelf of ze hem gebruikt. Daardoor verschilt de regel per land en per niveau.</p>
{tabel(["Competitie of niveau", "Witte wissel?"], [
    ('<a href="/competities/eredivisie">Eredivisie</a> en Keuken Kampioen Divisie', "Ja"),
    ("Vrouwen Eredivisie", "Ja"),
    ("Onder 21- en Onder 18-competities", "Nee"),
    ("Amateurvoetbal", "Nee, niet als standaardregel"),
    ("Premier League", "Ja, al sinds 2021"),
    ("Andere competities en toernooien", "Verschilt per organisator"),
])}
<p>In het amateurvoetbal bestaat de witte wissel officieel niet. Daar wordt vaak al met doorlopende wissels gespeeld, waardoor een speler met hoofdletsel sowieso gewisseld kan worden. Ook dan geldt: haal een speler met een vermoedelijke hersenschudding uit de wedstrijd en laat hem daarna niet meer meedoen.</p>
<h3><strong>Witte wissel en verlenging</strong></h3>
<p>In een wedstrijd met verlenging krijgen ploegen bij de meeste competities een extra gewone wissel. De witte wissel staat daar los van: ook in de verlenging kan een ploeg die zijn witte wissel nog niet heeft gebruikt, een speler met hoofdletsel vervangen.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wat is een witte wissel?</strong><br>Een extra, definitieve wissel die een ploeg mag inzetten bij een (vermoedelijke) hersenschudding. Hij telt niet mee voor de gewone vijf wissels.</p>
<p><strong>Hoeveel witte wissels mag een ploeg gebruiken?</strong><br>Maximaal één per wedstrijd.</p>
<p><strong>Krijgt de tegenstander ook een extra wissel?</strong><br>Ja. Zodra een ploeg een witte wissel inzet, krijgt de tegenstander ook een extra wissel en een extra wisselmoment.</p>
<p><strong>Mag een speler na een witte wissel terugkomen?</strong><br>Nee, de wissel is definitief.</p>
<p><strong>Moet een hersenschudding vaststaan?</strong><br>Nee, een vermoeden is genoeg. De medische staf van de ploeg beoordeelt dat.</p>
<p><strong>Geldt de witte wissel in het amateurvoetbal?</strong><br>Nee, de regel geldt in Nederland alleen in het betaald voetbal, met uitzondering van de Onder 21- en Onder 18-competities.</p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_SPELUITLEG,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting"); sys.exit()
    print("item:", WF.create_live(fd))
