# -*- coding: utf-8 -*-
"""Los artikel (evergreen): netto stortingslimiet. Feiten nagelopen op 21-10-2026: Beleidsregel verantwoord spelen 2024
(Stcrt. 2024, 18177), Regeling speellimieten (Stcrt. 2024, 19648), art. 4.14 Besluit kansspelen op afstand, Ksa good/bad
practices draagkrachttoetsen (juni 2026), Ksa-monitor voorjaar 2026, Kamerstuk 24557 nr. 273, Rijksoverheid 12-06-2026.
Infographic + pdf: og_kaarten/stortingslimiet.py -> be-static.
  python3 specials/netto_stortingslimiet.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Netto stortingslimiet: alles wat je moet weten over de grens van €300 en €700"
SLUG = "netto-stortingslimiet"
SAMENVATTING = ("De netto stortingslimiet is €300 per maand tot 24 jaar en €700 daarna. Zo bereken je het, dit gebeurt "
                "bij overschrijding en dit verandert er.")
RUBRIEK_CRUKS = "6672e1c5c1902e8ee8ce98cd"
STATIC = "https://www.bet-experts.nl/be-static/"
IMG = STATIC + "netto-stortingslimiet-infographic-aff0b88e.webp"
PDF = STATIC + "netto-stortingslimiet-infographic-3a212386.pdf"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


INFOGRAPHIC = (f'<figure class="w-richtext-align-fullwidth w-richtext-figure-type-image" style="max-width:100%">'
               f'<div><img src="{IMG}" alt="Infographic netto stortingslimiet: €300 per maand voor 18 t/m 23 jaar, €700 '
               f'vanaf 24 jaar, rekenvoorbeeld en wat er gebeurt bij overschrijding" loading="lazy"></div>'
               f'<figcaption>De netto stortingslimiet in één overzicht (stand oktober 2026)</figcaption></figure>'
               f'<p><strong><a href="{PDF}" target="_blank">📄 Download deze infographic als pdf (A4)</a></strong></p>')

content = f"""<p><strong>De netto stortingslimiet is de grens van de Kansspelautoriteit voor hoeveel geld je per maand netto mag storten bij een legaal online casino of een legale bookmaker. Ben je 18 tot en met 23 jaar, dan ligt die grens op €300 per kalendermaand. Vanaf je 24e is het €700. Netto betekent: alles wat je stort, min wat je in dezelfde maand opneemt. Ga je erover, dan blokkeert de aanbieder nieuwe stortingen tot het einde van de maand, tenzij je met loonstroken of je belastingaangifte aantoont dat je meer kunt dragen.</strong></p>
<p>De regel geldt sinds 1 oktober 2024 en zorgt nog steeds voor veel vragen. Is het een wet? Telt een opname mee? Geldt het per casino of voor alle aanbieders samen? En wat is het verschil met de stortingslimiet die je zelf instelt? In dit artikel lees je alles over de netto stortingslimiet, met rekenvoorbeelden, de regels voor een hogere limiet en de plannen voor één limiet voor alle aanbieders samen. Verderop vind je alles ook in één overzichtelijke infographic, die je als pdf kunt downloaden.</p>
<h3><strong>Wat is de netto stortingslimiet?</strong></h3>
<p>Officieel heet het de <strong>netto-stortingsgrens</strong>. Het is geen wet, maar een norm uit de Beleidsregel verantwoord spelen 2024 van de Kansspelautoriteit (Ksa). Daarin legt de toezichthouder vast hoe online aanbieders hun zorgplicht moeten invullen: ze moeten spelers beschermen tegen gokschade en ingrijpen als iemand meer verliest dan hij kan missen.</p>
<p>De netto stortingslimiet is daarbij een vast signaal. Stort een speler in een kalendermaand netto meer dan de grens, dan gaat de Ksa ervan uit dat hij de financiële gevolgen van zijn speelgedrag mogelijk niet meer kan dragen. De aanbieder moet dan ingrijpen. In de praktijk werkt de grens daardoor als een maandlimiet, al noemt de Ksa het nadrukkelijk een beschermingsmaatregel en geen "budget" dat je op verzoek kunt laten ophogen.</p>
<h3><strong>Hoe hoog is de netto stortingslimiet?</strong></h3>
{tabel(["Leeftijd", "Netto stortingslimiet", "Periode"], [
    ("18 tot en met 23 jaar (jongvolwassenen)", "<strong>€300</strong>", "Per kalendermaand"),
    ("24 jaar en ouder", "<strong>€700</strong>", "Per kalendermaand"),
])}
<p>Deze bedragen zijn de standaardgrens voor als de aanbieder je inkomen niet kent. Weet de aanbieder wel wat je verdient, dan gaat de Ksa uit van het deel van je netto-inkomen dat je recreatief kunt besteden, of anders van 30 procent van je netto maandinkomen. Je grens kan dan hoger, maar ook lager uitvallen dan €700.</p>
<p>De bedragen komen niet uit de lucht vallen. De Ksa schatte met CBS-cijfers hoeveel een gemiddelde Nederlander per maand vrij kan besteden aan recreatie, en rondde dat af op €300 voor jongvolwassenen en €700 voor andere spelers. In het eerste plan van december 2023 stond voor jongeren nog €350; in de definitieve regel werd dat €300. Zie je ergens nog €350 als netto grens voor jongeren, dan is die informatie verouderd.</p>
<h3><strong>Hoe bereken je je netto stortingen?</strong></h3>
<p>De formule is eenvoudig: <strong>stortingen min opnames = netto stortingen</strong>. Je kijkt per kalendermaand (van de 1e tot en met de laatste dag) en per speelaccount. Bonussen en winsten tellen niet als storting; een opname verlaagt je netto bedrag wel.</p>
<p><strong>Voorbeeld van de Kansspelautoriteit (speler van 24 jaar of ouder)</strong><br>Je stort in een maand drie keer €300, in totaal €900. Dat is meer dan €700, dus de aanbieder blokkeert verdere stortingen. Neem je daarna €400 op, dan sta je op netto €500 (€900 min €400). Dat is weer onder de grens, en de Ksa heeft er dan geen bezwaar tegen als de aanbieder storten weer toestaat.</p>
<p><strong>Voorbeeld voor een jongvolwassene</strong><br>Sanne is 21 en stort €200 en later nog €150: €350 in totaal. Daarmee gaat ze over de €300 en wordt storten geblokkeerd. Ze neemt €100 op en staat dan op netto €250. De aanbieder mag storten weer toestaan, maar hoeft dat niet: een opname geeft je geen recht op nieuwe stortingsruimte.</p>
<p>Let op: wie steeds geld opneemt om daarna nog verder over de grens te storten, valt volgens de Ksa juist op als risicospeler.</p>
{INFOGRAPHIC}"""

content2 = f"""<h3><strong>Wat gebeurt er als je over de netto stortingslimiet gaat?</strong></h3>
<ul><li><strong>Storten geblokkeerd:</strong> de aanbieder blokkeert direct nieuwe stortingen voor de rest van de kalendermaand, of tot aannemelijk is dat je het verlies kunt dragen.</li><li><strong>Draagkrachttoets:</strong> wil je toch meer storten, dan moet je aantonen dat je dat kunt betalen. Dat gaat met officiële documenten, niet met een simpele vragenlijst.</li><li><strong>Bonusstop:</strong> na een blokkade wegens overschrijding mag de aanbieder je minimaal 30 dagen geen bonussen meer aanbieden.</li><li><strong>Nieuwe maand:</strong> op de 1e van de volgende maand begint de telling weer bij nul. Je eigen stortingslimiet blijft dan natuurlijk wel gelden.</li></ul>
<p>Een aanbieder mag alleen van deze aanpak afwijken als hij dat goed kan onderbouwen, en volgens de Ksa "niet lichtvaardig". Het voorbeeld uit de beleidsregel is een professionele pokerspeler die voor een toernooi een hoger bedrag moet storten.</p>
<h3><strong>Kun je de netto stortingslimiet verhogen?</strong></h3>
<p>Alleen als je met een draagkrachttoets laat zien dat je meer kunt missen. De Ksa stelt strenge eisen aan de bewijsstukken: ze moeten "voldoende, correct en controleerbaar" zijn en echt van jou.</p>
<p><strong>Dit telt wel als bewijs:</strong></p>
<ul><li>Salarisstroken</li><li>Je aangifte inkomstenbelasting</li><li>Vakantiegeld, voor maximaal 1/12 deel per maand</li></ul>
<p><strong>Dit telt niet als bewijs of als inkomen:</strong></p>
<ul><li>Een eigen verklaring of vragenlijst over je inkomen</li><li>Spaargeld of het saldo op je bankrekening</li><li>Overwaarde van je huis of bedrijfsvermogen</li><li>Inkomen van je partner, toeslagen of kinderbijslag</li><li>Opnames van een gokaccount, erfenissen of Tikkies</li></ul>
<p>Een draagkrachttoets kan je grens ook verlagen. Blijkt uit je loonstrook dat je een laag inkomen hebt, dan mag de aanbieder je een lagere grens geven dan €700. Sommige aanbieders gaan nog verder: zij laten jongvolwassenen nooit boven de €300 komen, of staan maar één overschrijding toe. De Ksa noemt dat goede voorbeelden.</p>
<h3><strong>Verschil tussen de netto stortingslimiet en je eigen stortingslimiet</strong></h3>
<p>Dit is het punt waar de meeste verwarring over bestaat. Naast de netto-grens van de Ksa moet je bij elk legaal casino of elke legale bookmaker ook <strong>zelf</strong> limieten instellen voordat je kunt spelen: een maximum voor je stortingen, je speeltijd en het saldo op je account. Dat staat in de wet (artikel 4.14 van het Besluit kansspelen op afstand).</p>
{tabel(["", "Netto stortingslimiet", "Eigen stortingslimiet"], [
    ("Wie bepaalt het?", "De Kansspelautoriteit (norm)", "Jij, verplicht bij inschrijving"),
    ("Wat telt mee?", "Stortingen min opnames", "Alle stortingen (bruto)"),
    ("Periode", "Per kalendermaand", "Per dag, week of maand (jouw keuze)"),
    ("Verhogen", "Alleen na een draagkrachttoets", "Pas na minimaal 7 dagen"),
    ("Verlagen", "Niet van toepassing", "Gaat direct in"),
    ("Extra drempel", "-", "Vanaf €350 per maand (tot 24 jaar €150) eerst een gesprek"),
])}
<p>Wil je je eigen stortingslimiet op €350 of meer per maand zetten (of €150 of meer als je jonger bent dan 24), dan kan dat sinds 1 oktober 2024 alleen na een contactmoment met een medewerker die is opgeleid in verslavingspreventie. Die vraagt of je beseft dat het om een hoog bedrag gaat en of je bereid bent dat te verliezen, en wijst je op Cruks en hulplijnen. Weigeren mag de aanbieder daarna niet, maar de wachttijd van 7 dagen blijft gelden. Verder krijg je elke 30 minuten een pop-up met je speeltijd en limieten, en een melding als je 50 procent van een limiet hebt bereikt.</p>
<p>Kort gezegd: de €350 en €150 gaan over de limiet die je <strong>zelf</strong> instelt, de €700 en €300 over de <strong>netto</strong> grens van de Ksa. Veel websites halen die twee door elkaar.</p>
<h3><strong>Geldt de limiet per casino of voor alle aanbieders samen?</strong></h3>
<p>Op dit moment <strong>per aanbieder</strong>. De netto stortingslimiet geldt per speelaccount, dus bij elk casino en elke bookmaker apart. Er is nog geen centraal systeem dat je stortingen bij verschillende aanbieders bij elkaar optelt.</p>
<p>Dat heeft een keerzijde. Volgens de Ksa-monitor van voorjaar 2026 gebruikten spelers in de tweede helft van 2025 gemiddeld 3,2 legale aanbieders, tegen 2,8 een jaar eerder, en waren er gemiddeld 1,38 miljoen actieve accounts per maand terwijl het aantal spelers niet steeg. De Ksa ziet daarin een aanwijzing dat een deel van de spelers de limieten per account probeert te omzeilen. Aanbieders moeten dat ook als risicosignaal behandelen: wie in de chat zegt dat hij bij een ander casino een hogere limiet heeft, of bij veel aanbieders tegelijk speelt, hoort extra aandacht te krijgen.</p>"""

content3 = f"""<h3><strong>Komt er één stortingslimiet voor alle aanbieders?</strong></h3>
<p>Ja, dat is de bedoeling. Op 12 juni 2026 kondigde staatssecretaris Claudia van Bruggen (Justitie en Veiligheid) aan dat er een stortingslimiet komt die geldt voor alle online kansspelen samen. Wie hoger wil, moet eerst voldoende financiële draagkracht aantonen. Bij die toets wordt onder meer gekeken naar curatele of bewind, betalingsachterstanden en je financiële situatie.</p>
<p>De hoogte van die overkoepelende limiet en de datum waarop hij ingaat, zijn nog niet bekend. De plannen worden uitgewerkt in een wetsvoorstel. In hetzelfde pakket zitten ook een reclameverbod voor online kansspelen, een bonusverbod en een strengere gokstop via Cruks. Ook dat zijn voorlopig voornemens, geen geldende regels. Zodra er meer bekend is, werken we dit artikel bij.</p>
<h3><strong>Werkt de netto stortingslimiet?</strong></h3>
<p>De eerste cijfers wijzen daarop. Uit de effectmeting van de Ksa, die staatssecretaris Struycken in juli 2025 naar de Tweede Kamer stuurde:</p>
{tabel(["Meting", "Voor 1 oktober 2024", "Na invoering"], [
    ("Spelers die netto meer stortten dan de grens", "9,4%", "2,2% (mei 2025)"),
    ("Gemiddeld verlies per account per maand", "€116", "€80 (oktober 2024)"),
    ("Spelers met meer dan €1.000 verlies per maand", "3,9%", "0,9%"),
])}
<p>Daar staat tegenover dat spelers vaker bij meerdere aanbieders spelen, wat het effect deels tenietdoet. Precies daarom komt de overkoepelende limiet.</p>
<h3><strong>Hoe streng is het toezicht?</strong></h3>
<p>De Kansspelautoriteit controleert of aanbieders de zorgplicht goed uitvoeren, en daar hoort ook het juist berekenen van netto stortingen en het correct uitvoeren van draagkrachttoetsen bij. In februari 2025 sprak de Ksa aanbieders al aan op slordige draagkrachttoetsen. Sindsdien volgden bindende aanwijzingen en boetes wegens schending van de zorgplicht, oplopend tot bijna €900.000 per aanbieder. De Ksa publiceert die besluiten in haar sanctieregister.</p>
<h3><strong>Hoe zit het in andere landen?</strong></h3>
{tabel(["Land", "Regel"], [
    ("Nederland", "€300 (18-23 jaar) of €700 netto per maand, per aanbieder"),
    ("Duitsland", "In principe €1.000 per maand, voor alle aanbieders samen via een centraal systeem (LUGAS)"),
    ("België", "€200 per week; hoger kan via de Kansspelcommissie. Online gokken mag pas vanaf 21 jaar"),
    ("Verenigd Koninkrijk", "Geen vaste limiet, wel financiële checks vanaf £150 netto storting per 30 dagen"),
])}
<h3><strong>Waarom je geen casino zonder stortingslimiet moet kiezen</strong></h3>
<p>Online zie je regelmatig reclame voor casino's "zonder stortingslimiet" of "zonder Cruks". Dat zijn altijd aanbieders zonder Nederlandse vergunning. Spelen daar is niet alleen illegaal aanbod, je hebt er ook geen enkele bescherming: geen verplichte limieten, geen toezicht van de Ksa en geen garantie dat je je winst uitbetaald krijgt. Lees meer in ons artikel over <a href="/nieuws/casino-zonder-stortingslimiet-risicos-en-legale-alternatieven-voor-nederlandse-spelers">casino's zonder stortingslimiet</a>, bekijk <a href="/nieuws/dit-zijn-de-casinos-die-op-dit-moment-legaal-zijn-in-nederland">welke casino's legaal zijn in Nederland</a> of lees <a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je herkent of een bookmaker legaal is</a>.</p>
<h3><strong>Tips om bewust met je stortingen om te gaan</strong></h3>
<ul><li><strong>Stel je eigen limiet lager in dan de netto-grens.</strong> De €700 is een bovengrens, geen advies. Kies een bedrag dat past bij wat je echt kunt missen.</li><li><strong>Zie stortingen als uitgaven.</strong> Reken nooit op winst om je limiet "terug te verdienen".</li><li><strong>Speel niet bij meerdere aanbieders tegelijk om de grens te omzeilen.</strong> Het is een signaal dat je speelgedrag uit de hand loopt.</li><li><strong>Gebruik de pop-ups en meldingen.</strong> Een melding bij 50 procent van je limiet is een goed moment om te stoppen.</li><li><strong>Neem een pauze via Cruks</strong> als je merkt dat je meer speelt dan je wilt.</li></ul>
<p>Meer over verantwoord spelen lees je op onze pagina's over <a href="/speel-bewust/verantwoord-wedden">verantwoord wedden</a> en <a href="/speel-bewust/kwetsbare-groepen">kwetsbare groepen</a>.</p>
<h3><strong>Hulp nodig?</strong></h3>
<ul><li><strong>Cruks (gokstop):</strong> sluit jezelf uit bij alle legale aanbieders in Nederland, voor minimaal 6 maanden. Inschrijven doe je met DigiD via cruksregister.nl. Lees meer in ons artikel over <a href="/nieuws/cruks-de-gokstop-voor-verantwoord-gokken">Cruks, de gokstop</a>.</li><li><strong>Open over Gokken</strong> (voorheen Loket Kansspel): gratis en anoniem, dag en nacht bereikbaar via 0800 24 000 22, en via chat en WhatsApp.</li><li><strong>AGOG (Anonieme Gokkers Over Gokken):</strong> zelfhulpgroepen voor gokkers en hun naasten, gratis bereikbaar via 0800-22 777 22.</li></ul>
<h3><strong>Veelgestelde vragen over de netto stortingslimiet</strong></h3>
<p><strong>Hoeveel mag ik per maand storten in een online casino?</strong><br>Netto €300 per kalendermaand als je 18 tot en met 23 jaar bent, en €700 vanaf 24 jaar, per aanbieder. Daarbovenop geldt de stortingslimiet die je zelf hebt ingesteld.</p>
<p><strong>Is de netto stortingslimiet een wet?</strong><br>Nee. Het is een norm uit de Beleidsregel verantwoord spelen 2024 van de Kansspelautoriteit. Aanbieders moeten zich er wel aan houden, omdat de Ksa er de zorgplicht op controleert.</p>
<p><strong>Telt een opname mee voor de netto stortingslimiet?</strong><br>Ja. Je netto stortingen zijn je stortingen min je opnames in dezelfde kalendermaand. Een opname verlaagt dus je netto bedrag.</p>
<p><strong>Wanneer kan ik weer storten na een blokkade?</strong><br>Op de 1e van de volgende kalendermaand begint de telling opnieuw. Eerder kan alleen als je netto weer onder de grens komt en de aanbieder storten toestaat, of na een goedgekeurde draagkrachttoets.</p>
<p><strong>Hoe verhoog ik mijn netto stortingslimiet?</strong><br>Door met loonstroken of je belastingaangifte aan te tonen dat je het kunt dragen. Een eigen verklaring of spaargeld is niet genoeg.</p>
<p><strong>Geldt de limiet bij elk casino apart?</strong><br>Ja, op dit moment wel. Het kabinet heeft in juni 2026 aangekondigd dat er één limiet voor alle online aanbieders samen komt, maar de hoogte en ingangsdatum zijn nog niet bekend.</p>
<p><strong>Geldt de netto stortingslimiet ook voor sportweddenschappen?</strong><br>Ja. De grens geldt voor alle online kansspelen bij legale aanbieders, dus voor online casino's, bookmakers en online poker.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_CRUKS,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        import re
        tekst = re.sub(r"<[^>]+>", " ", content + content2 + content3)
        print(len(SAMENVATTING), "tekens samenvatting |", len(tekst.split()), "woorden"); sys.exit()
    print("item:", WF.create_live(fd))
