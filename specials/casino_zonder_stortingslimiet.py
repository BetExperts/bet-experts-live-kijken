# -*- coding: utf-8 -*-
"""Herschrijving (bestaand item 670536ee5af008850c317e40): Casino zonder stortingslimiet.
Feiten: stortingslimiet_facts (Beleidsregel verantwoord spelen 2024, Regeling speellimieten, art. 4.14 Bkoa) en
legaal_facts (Wok art. 1/36a, HR 3-7-2026, Ksa-boetes, OpenOverGokken rode vlaggen, kabinet 12-06-2026).
De twee externe links onderaan stonden in de oude versie (navragen bij Jasper of ze moeten blijven).
  python3 specials/casino_zonder_stortingslimiet.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lk_webflow as WF
from legaal_data import tabel, aanraders, KANSSPELWIJZER

ITEM_ID = "670536ee5af008850c317e40"
TITEL = "Casino zonder stortingslimiet: de risico's en legale alternatieven (2026)"
SAMENVATTING = ("Een casino zonder stortingslimiet is altijd illegaal in Nederland. Dit zijn de risico's, zo werken de "
                "limieten en dit zijn de legale alternatieven.")

content = f"""<p><strong>Een online casino zonder stortingslimiet is in Nederland altijd een illegaal casino. Alle legale aanbieders zijn verplicht om met limieten te werken: je stelt bij inschrijving zelf een stortingslimiet in, en daarnaast geldt een netto grens van €300 per maand tot 24 jaar en €700 per maand vanaf 24 jaar. Wie die limieten omzeilt bij een casino zonder vergunning, verliest alle bescherming: geen toezicht, geen Cruks-check en geen garantie dat je je winst uitbetaald krijgt.</strong></p>
<p>Sinds de regels in oktober 2024 strenger werden, zoeken sommige spelers naar een casino "zonder limiet". Begrijpelijk misschien, maar het is een slecht idee. In dit artikel lees je hoe de stortingslimieten in Nederland precies werken, waarom een casino zonder stortingslimiet illegaal en riskant is, hoe je zulke sites herkent en wat je legale alternatieven zijn.</p>
<h3><strong>Welke stortingslimieten gelden er in Nederland?</strong></h3>
<p>Bij legale online casino's en bookmakers heb je met twee soorten limieten te maken:</p>
{tabel(["", "Je eigen stortingslimiet", "De netto stortingslimiet"], [
    ("Wat is het?", "Een limiet die je zelf instelt bij inschrijving (verplicht)", "Een grens van de Kansspelautoriteit voor je netto stortingen"),
    ("Hoe hoog?", "Kies je zelf; vanaf €350 per maand (tot 24 jaar €150) eerst een gesprek", "€300 per maand (18 t/m 23 jaar) of €700 per maand (24+)"),
    ("Wat telt mee?", "Al je stortingen", "Stortingen min opnames, per kalendermaand"),
    ("Verhogen?", "Pas na minimaal 7 dagen", "Alleen na een draagkrachttoets met loonstroken of je belastingaangifte"),
])}
<p>Ga je over de netto grens, dan blokkeert het casino nieuwe stortingen tot het einde van de maand, en krijg je minimaal 30 dagen geen bonussen meer. Alles over de berekening, met voorbeelden en een downloadbare infographic, lees je in ons artikel over de <a href="/nieuws/netto-stortingslimiet">netto stortingslimiet</a>.</p>
<p>Die regels zijn er niet voor niets. Volgens metingen van de Ksa daalde het aandeel spelers dat per maand netto meer dan de grens stortte van 9,4 procent naar 2,2 procent, en het aandeel spelers dat meer dan €1.000 per maand verloor van 3,9 naar 0,9 procent.</p>
<h3><strong>Bestaat er een legaal casino zonder stortingslimiet?</strong></h3>
<p>Nee. Elk casino met een Nederlandse vergunning moet zich aan de limietregels houden. Een site die adverteert met "geen stortingslimiet", "onbeperkt storten" of "zonder Cruks" heeft per definitie geen Nederlandse vergunning. Ook een casino met alleen een buitenlandse licentie, bijvoorbeeld uit Curaçao, is illegaal in Nederland: alleen een vergunning van de Kansspelautoriteit telt. Controleer het zelf in de <a href="{KANSSPELWIJZER}" target="_blank" rel="noopener">Kansspelwijzer van de Ksa</a>.</p>"""

content2 = f"""<h3><strong>De risico's van een casino zonder stortingslimiet</strong></h3>
<ul><li><strong>Geen bescherming tegen gokschade:</strong> geen limieten, geen meldingen, geen pauzes en geen ingreep als je meer verliest dan je kunt missen. Juist die bescherming voorkomt dat gokken uit de hand loopt.</li><li><strong>Geen Cruks:</strong> illegale casino's zijn niet aangesloten op het Centraal Register Uitsluiting Kansspelen. Ook wie zichzelf een gokstop heeft opgelegd, kan er gewoon spelen.</li><li><strong>Geen garantie op uitbetaling:</strong> er is geen toezichthouder die ervoor zorgt dat je je winst krijgt. Uitbetalingen worden vaak vertraagd of geweigerd.</li><li><strong>Je gegevens zijn niet veilig:</strong> je deelt je identiteitsbewijs en bankgegevens met een partij zonder toezicht.</li><li><strong>Je verlies is niet terug te halen:</strong> de Hoge Raad oordeelde op 3 juli 2026 dat een overeenkomst met een illegale aanbieder niet nietig is. Terugvorderen op die grond lukt dus niet meer.</li><li><strong>Het is strafbaar:</strong> spelen bij een aanbieder waarvan je weet dat hij geen vergunning heeft, is volgens de Wet op de kansspelen strafbaar, met een boete tot €11.000.</li><li><strong>Zelf belasting betalen:</strong> bij een illegale online aanbieder moet je zelf kansspelbelasting aangeven als je in een maand meer wint dan inzet. Bij een legaal casino doet de aanbieder dat.</li></ul>
<h3><strong>Zo herken je een illegaal casino</strong></h3>
<ul><li>Het casino staat niet in de Kansspelwijzer van de Kansspelautoriteit.</li><li>Er staat geen Ksa-logo met een werkende link naar de Kansspelautoriteit.</li><li>Je kunt je inschrijven zonder controle van je identiteit, leeftijd of Cruks-registratie.</li><li>Je hoeft geen limieten in te stellen, of de site adverteert juist met "geen limiet".</li><li>Je kunt alleen met crypto of vage betaalmethoden storten.</li><li>Er worden ongeloofwaardige bonussen beloofd, zoals duizenden euro's zonder voorwaarden.</li><li>Er is geen Nederlandse klantenservice of klachtenregeling.</li><li>Je wordt via influencers of sociale media naar de site gelokt.</li></ul>
<p>De Kansspelautoriteit treedt hard op tegen dit soort sites. De hoogste boete tot nu toe was €24,8 miljoen voor het bedrijf achter Qbet en 55Bet (maart 2026). Sinds juli 2026 begint een boete voor illegaal aanbod bij €800.000. Toch gaat volgens de Ksa nog bijna de helft van het in Nederland vergokte geld naar illegale aanbieders.</p>
<h3><strong>Legale alternatieven</strong></h3>
<p>Wil je online spelen, kies dan altijd een casino met een Nederlandse vergunning. Daar speel je met bescherming, krijg je je winst gegarandeerd uitbetaald en betaal je geen kansspelbelasting over je winst. Een volledige lijst vind je in ons artikel <a href="/nieuws/dit-zijn-de-casinos-die-op-dit-moment-legaal-zijn-in-nederland">dit zijn de casino's die legaal zijn in Nederland</a>. Onze aanraders:</p>
{aanraders()}
<p>Lees ook <a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je herkent of een bookmaker legaal is</a> en ons artikel over <a href="/nieuws/casino-zonder-cruks-wat-je-moet-weten">casino's zonder Cruks</a>.</p>"""

content3 = """<h3><strong>Wat verandert er?</strong></h3>
<p>Het kabinet wil de regels verder aanscherpen. Op 12 juni 2026 werd aangekondigd dat er één stortingslimiet komt die geldt voor alle online aanbieders samen. Nu geldt de netto grens nog per casino. Wie hoger wil, moet dan eerst aantonen dat hij het kan betalen. Ook een reclameverbod, een bonusverbod, een Cruks-gokstop voor onbepaalde tijd en het blokkeren van illegale websites staan op de planning. De hoogte van de nieuwe limiet en de ingangsdatum zijn nog niet bekend.</p>
<h3><strong>Hulp bij gokproblemen</strong></h3>
<p>Merk je dat je limieten wilt omzeilen of dat je meer speelt dan je wilt? Dat is een signaal om hulp te zoeken. Dat kan gratis en anoniem:</p>
<ul><li><strong>Open over Gokken</strong> (voorheen Loket Kansspel): dag en nacht bereikbaar via 0800 24 000 22, en via chat en WhatsApp.</li><li><strong>Cruks (gokstop):</strong> sluit jezelf voor minimaal 6 maanden uit bij alle legale aanbieders. Inschrijven doe je met DigiD via cruksregister.nl. Lees meer over <a href="/nieuws/cruks-de-gokstop-voor-verantwoord-gokken">Cruks, de gokstop</a>.</li><li><strong>AGOG</strong> (Anonieme Gokkers Over Gokken): zelfhulpgroepen voor gokkers en hun naasten, gratis bereikbaar via 0800-22 777 22.</li></ul>
<p>Meer tips vind je op onze pagina over <a href="/speel-bewust/verantwoord-wedden">verantwoord spelen</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Bestaat er een legaal casino zonder stortingslimiet in Nederland?</strong><br>Nee. Elk legaal online casino moet met limieten werken. Een casino zonder stortingslimiet heeft geen Nederlandse vergunning en is dus illegaal.</p>
<p><strong>Hoeveel mag ik per maand storten in een online casino?</strong><br>Netto €300 per kalendermaand als je 18 tot en met 23 jaar bent en €700 vanaf 24 jaar, per aanbieder. Daarbovenop geldt de limiet die je zelf hebt ingesteld.</p>
<p><strong>Kan ik mijn stortingslimiet verhogen?</strong><br>Je eigen limiet kun je verhogen, maar de verhoging gaat pas na 7 dagen in, en vanaf €350 per maand (tot 24 jaar €150) volgt eerst een gesprek. Boven de netto grens storten kan alleen na een draagkrachttoets met loonstroken of je belastingaangifte.</p>
<p><strong>Is spelen bij een casino zonder limiet strafbaar?</strong><br>Spelen bij een aanbieder zonder Nederlandse vergunning is volgens de wet strafbaar, met een boete tot €11.000. Daarnaast heb je er geen enkele bescherming.</p>
<p><strong>Krijg ik mijn geld terug van een illegaal casino?</strong><br>Meestal niet. Sinds een uitspraak van de Hoge Raad in juli 2026 kun je je verlies niet meer terugvorderen op grond van een ongeldige overeenkomst.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>
<p><strong>Extra interessante websites</strong><br><a href="https://casinozondercruks.nl/">Casino zonder cruks</a> · <a href="https://casinozondervergunning.nl/">Casino zonder vergunning</a></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "content": content, "content-2": content2, "content-3": content3, "samenvatting": SAMENVATTING,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        import re
        tekst = re.sub(r"<[^>]+>", " ", content + content2 + content3)
        print(len(SAMENVATTING), "tekens samenvatting |", len(tekst.split()), "woorden"); sys.exit()
    print(WF.update_live(ITEM_ID, fd).get("id"))
