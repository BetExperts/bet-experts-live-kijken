# -*- coding: utf-8 -*-
"""Herschrijving (bestaand item 66a0f22144a3cda0737e58d7): Dit zijn de casino's die op dit moment legaal zijn in Nederland.
Feiten: Kansspelwijzer Ksa (21-10-2026), Ksa-nieuws vervolgvergunningen 17-09-2026, intrekking LiveScore/Tombola 23-12-2024,
Wok/Besluit kansspelen op afstand, HR 3-7-2026 (ECLI:NL:HR:2026:1159), Ksa-boetes, monitor voorjaar 2026, Belastingdienst.
  python3 specials/legale_casinos_nl.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lk_webflow as WF
from legaal_data import tabel, merken_tabel, aanraders, KANSSPELWIJZER, PEILDATUM

ITEM_ID = "66a0f22144a3cda0737e58d7"
TITEL = "Dit zijn de casino's die op dit moment legaal zijn in Nederland (oktober 2026)"
SAMENVATTING = ("Welke online casino's zijn legaal in Nederland? De actuele lijst van alle 31 vergunninghouders van de "
                "Kansspelautoriteit, en zo check je het zelf.")

content = f"""<p><strong>In Nederland zijn op dit moment 31 aanbieders met een vergunning voor online kansspelen van de Kansspelautoriteit (Ksa), samen goed voor zo'n 29 merken. Bekende legale online casino's zijn onder meer Holland Casino Online, TOTO, BetCity, JACKS.NL, Unibet, bet365, BetMGM, LeoVegas, Circus, Starcasino en 888. Of een casino legaal is, check je in een paar seconden in de Kansspelwijzer van de Ksa. Alles wat daar niet in staat, is illegaal in Nederland.</strong></p>
<p>Sinds 1 oktober 2021 is online gokken in Nederland legaal bij aanbieders met een Nederlandse vergunning. Vijf jaar later is de markt flink veranderd: er kwamen nieuwe casino's bij, een paar bekende namen vertrokken, en in september 2026 kregen de eerste aanbieders een vervolgvergunning tot 2031. In dit artikel vind je de volledige, actuele lijst (stand {PEILDATUM}), hoe je zelf controleert of een casino legaal is en waarom je illegale sites beter kunt vermijden.</p>
<h3><strong>Hoeveel legale online casino's zijn er in Nederland?</strong></h3>
<p>Volgens de Kansspelwijzer van de Kansspelautoriteit hebben 31 partijen een vergunning voor online kansspelen. Bijna allemaal (30) mogen ze casinospellen aanbieden, 25 hebben ook een vergunning voor sportweddenschappen, 8 voor online poker en 9 voor paardenweddenschappen. Een paar vergunninghouders noemen bij de Ksa (nog) geen merk of website; het aantal herkenbare merken ligt daardoor rond de 29.</p>
<ul><li><strong>Verlengd tot 2031:</strong> op 17 september 2026 kregen de eerste acht aanbieders een vervolgvergunning, geldig van oktober 2026 tot en met september 2031: TOTO (met Winnitt), Holland Casino Online, Kansino, Fair Play Casino, Bingoal, bet365, GGPoker en BetCity.</li><li><strong>Nieuw sinds 2024:</strong> Hard Rock Casino, Lucky7casino, Starcasino, 888 (juli 2025) en winz.nl (november 2025). In 2026 kwamen er tot nu toe geen nieuwe aanbieders bij.</li><li><strong>Gestopt:</strong> LiveScore Bet en Tombola leverden hun vergunning eind 2024 op eigen verzoek in. Ook Scori PRO staat niet meer in de lijst.</li></ul>
<h3><strong>Lijst van alle legale online casino's in Nederland</strong></h3>
<p>In de tabel zie je per merk de website, het bedrijf achter de vergunning en waarvoor de vergunning geldt. Klik op een merknaam voor onze uitgebreide review.</p>
{merken_tabel()}
<p><em>Bron: Kansspelwijzer van de Kansspelautoriteit, stand {PEILDATUM}. De producten zijn de onderdelen waarvoor de vergunning geldt; niet elk merk biedt ze ook allemaal aan. Daarnaast hebben JOI I Ltd, JOI II Ltd en New Future Games B.V. een vergunning, zonder dat de Ksa er een merk of website bij noemt.</em></p>
<p>Zoek je alleen een online casino? Casino777, Fair Play Casino, Kansino en winz.nl bieden uitsluitend casinospellen aan, GGPoker is vooral een pokersite. ZEbet en ZEturf hebben juist geen casinovergunning: daar kun je alleen op sport en paarden wedden.</p>
<h3><strong>Onze aanraders onder de legale aanbieders</strong></h3>
<p>Alle aanbieders in de lijst zijn legaal en staan onder toezicht. Op basis van onze reviews springen deze er voor ons uit:</p>
{aanraders()}
<p>Een overzicht van alle bookmakers en casino's met onze beoordeling vind je op onze pagina met <a href="/bookmakers">bookmakers</a>, en de beste casino's op een rij in onze <a href="/top-10-beste-online-casino-in-nederland">top 10 online casino's</a>.</p>"""

content2 = f"""<h3><strong>Hoe controleer je of een online casino legaal is?</strong></h3>
<p>De enige officiële check is de <a href="{KANSSPELWIJZER}" target="_blank" rel="noopener">Kansspelwijzer van de Kansspelautoriteit</a>. Daar zoek je op de naam van de website of de app. Staat het casino er niet in, dan heeft het geen Nederlandse vergunning en is het illegaal, ook als de site er Nederlands en betrouwbaar uitziet. Het oude vergunningenregister van de Ksa bestaat niet meer; de Kansspelwijzer is ervoor in de plaats gekomen.</p>
<p>Daarnaast herken je een legaal casino aan een paar vaste kenmerken:</p>
<ul><li><strong>Vergunningsinformatie met link naar de Ksa.</strong> Een legaal casino toont informatie over zijn vergunning en linkt naar de website van de Ksa, meestal via het Ksa-logo onderaan de pagina. Klik erop: het logo moet doorlinken naar de Ksa. Partijen zonder vergunning mogen het logo niet gebruiken.</li><li><strong>Cruks- en leeftijdscheck bij inschrijving.</strong> Een legaal casino stelt je identiteit vast, controleert of je 18 jaar of ouder bent en checkt of je niet in het Cruks-register staat.</li><li><strong>Verplichte limieten.</strong> Voordat je kunt spelen, stel je zelf een maximum in voor je stortingen, je speeltijd en je saldo. Daarnaast geldt een <a href="/nieuws/netto-stortingslimiet">netto stortingslimiet</a> van €300 per maand tot 24 jaar en €700 daarna.</li><li><strong>Betalen via een EU-bank of betaaldienst.</strong> Je stort met een betaalmiddel op je eigen naam, van een bank of betaaldienst met een Europese vergunning.</li><li><strong>Nederlandse voorwaarden.</strong> Nederlands recht is van toepassing, de klantenservice is gratis bereikbaar en klachten worden binnen acht weken behandeld.</li></ul>
<p><strong>Let op met nepkopieën.</strong> Oplichters maken soms kopieën van legale sites op een .co.nl-adres. De Ksa liet in 2026 tientallen van die gekloonde websites offline halen. Een .nl-adres is dus geen garantie: check altijd de exacte website in de Kansspelwijzer. Andersom is .nl ook niet verplicht: One Casino staat bijvoorbeeld bij de Ksa geregistreerd met nl.onecasino.com.</p>
<p>Meer tips lees je in ons artikel <a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe weet ik of een bookmaker legaal is</a> en op onze pagina over <a href="/legale-goksites-nederland">legale goksites in Nederland</a>.</p>
<h3><strong>Waarom zou je alleen bij een legaal casino spelen?</strong></h3>
<p>Een casino zonder Nederlandse vergunning is niet alleen illegaal, het is ook riskant. Je hebt er geen bescherming: er is geen toezicht, geen verplichte limiet, geen Cruks-check en geen garantie dat je je winst uitbetaald krijgt. Ook je persoonsgegevens zijn er niet veilig. Typische kenmerken van illegale sites zijn ongeloofwaardige bonussen zonder voorwaarden, betalen met alleen crypto, geen leeftijdscheck en reclame dat je er "zonder stortingslimiet" of <a href="/nieuws/casino-zonder-cruks-wat-je-moet-weten">zonder Cruks</a> kunt spelen. Lees ook ons artikel over <a href="/nieuws/casino-zonder-stortingslimiet-risicos-en-legale-alternatieven-voor-nederlandse-spelers">casino's zonder stortingslimiet</a>.</p>
<p><strong>Is spelen bij een illegaal casino strafbaar?</strong><br>Ja, in theorie wel. De Wet op de kansspelen verbiedt het om mee te doen aan een kansspel waarvan je weet dat er geen vergunning voor is. Daar staat een geldboete van maximaal €11.000 op. In de praktijk richt de handhaving zich op de aanbieders.</p>
<p><strong>Kun je je verlies terugvorderen?</strong><br>Lange tijd probeerden spelers via de rechter hun verliezen bij illegale casino's terug te halen, met het argument dat de overeenkomst ongeldig was. Op 3 juli 2026 oordeelde de Hoge Raad dat een overeenkomst met een online aanbieder zonder vergunning niet nietig is. Terugvorderen op die grond lukt dus niet meer. Alleen in bijzondere gevallen, bijvoorbeeld bij misleiding, kan er nog een claim mogelijk zijn.</p>
<h3><strong>Boetes voor illegale casino's</strong></h3>
<p>De Kansspelautoriteit treedt hard op tegen illegaal aanbod. Een paar recente boetes:</p>
{tabel(["Datum", "Aanbieder", "Websites (o.a.)", "Boete"], [
    ("10 maart 2026", "Novatech", "Qbet, 55Bet", "<strong>€24,8 miljoen</strong> (hoogste ooit)"),
    ("17 juni 2026", "Chestoption S.R.L.", "Vave", "€3,1 miljoen"),
    ("13 januari 2026", "Starscream Limited", "Rant Casino, AllStarz Casino, Sugar Casino", "€4,2 miljoen"),
    ("10 maart 2026", "Fortaprime SRL", "Amonbet, Supraplay, Kaasino e.a.", "€1,8 miljoen"),
    ("17 februari 2026", "Polymarket", "polymarket.com", "Last onder dwangsom tot €840.000"),
])}
<p>Sinds 24 juli 2026 geldt een nieuw boetebeleid: de basisboete voor illegaal aanbod is €800.000, of 100 procent van wat de aanbieder in Nederland verdiende als dat meer is. Bij herhaling wordt de boete verdubbeld.</p>
<p>Toch is illegaal gokken nog altijd groot. Volgens de Ksa speelt ongeveer 91 procent van de Nederlandse gokkers alleen bij legale aanbieders, maar gaat gemeten in geld maar 53 procent naar het legale aanbod. Bijna de helft van het vergokte geld verdwijnt dus nog naar illegale sites.</p>"""

content3 = f"""<h3><strong>Moet je belasting betalen over je winst?</strong></h3>
<p>Bij een legaal online casino niet. De aanbieder draagt de kansspelbelasting af (37,8 procent in 2026) en jij ontvangt je winst zonder aftrek. Speel je bij een online aanbieder zonder Nederlandse vergunning, dan moet je zelf aangifte doen bij de Belastingdienst als je in een kalendermaand meer hebt gewonnen dan ingezet.</p>
<h3><strong>Wat verandert er de komende tijd?</strong></h3>
<p>Het kabinet maakte op 12 juni 2026 plannen bekend om online gokken strenger te regelen. Het gaat om een reclameverbod, een verbod op bonussen zoals gratis inzet bij inschrijving, één stortingslimiet voor alle aanbieders samen, een gokstop via Cruks voor onbepaalde tijd, het blokkeren van illegale websites en onderzoek naar minder vergunninghouders. Die plannen worden uitgewerkt in een wetsvoorstel; wanneer ze ingaan, is nog niet bekend. Ook de lijst van legale casino's kan nog veranderen, omdat de komende tijd meer vergunningen aflopen en verlengd moeten worden. Wij houden dit artikel up-to-date.</p>
<h3><strong>Verantwoord spelen</strong></h3>
<p>Ook bij een legaal casino blijft gokken een risico. Speel met een vast budget, zie je inleg als uitgave en stel je limieten bewust laag in. Merk je dat het gokken je te veel tijd of geld kost, schrijf je dan in bij <a href="/nieuws/cruks-de-gokstop-voor-verantwoord-gokken">Cruks</a> (de gokstop, minimaal 6 maanden) of bel gratis en anoniem met Open over Gokken via 0800 24 000 22, dag en nacht bereikbaar. Meer tips vind je op onze pagina over <a href="/speel-bewust/verantwoord-wedden">verantwoord spelen</a>.</p>
<h3><strong>Veelgestelde vragen over legale casino's</strong></h3>
<p><strong>Hoeveel legale online casino's zijn er in Nederland?</strong><br>Op {PEILDATUM} hebben 31 aanbieders een vergunning voor online kansspelen van de Kansspelautoriteit, goed voor zo'n 29 merken. 30 daarvan mogen casinospellen aanbieden.</p>
<p><strong>Hoe weet ik of een online casino legaal is?</strong><br>Zoek de website of app op in de Kansspelwijzer van de Kansspelautoriteit. Staat hij er niet in, dan is het casino illegaal in Nederland.</p>
<p><strong>Is Holland Casino Online legaal?</strong><br>Ja. Holland Casino Online heeft een vergunning van de Ksa en kreeg in september 2026 een vervolgvergunning tot en met september 2031.</p>
<p><strong>Welke casino's zijn gestopt in Nederland?</strong><br>LiveScore Bet en Tombola leverden hun vergunning eind 2024 in. Ook Scori PRO staat niet meer in de lijst van de Ksa.</p>
<p><strong>Is spelen bij een buitenlands casino strafbaar?</strong><br>Spelen bij een aanbieder zonder Nederlandse vergunning is volgens de wet strafbaar, met een boete van maximaal €11.000. Bovendien heb je er geen enkele bescherming en kun je je verlies sinds een uitspraak van de Hoge Raad (juli 2026) niet meer terugvorderen op grond van een ongeldige overeenkomst.</p>
<p><strong>Is een casino met een Curaçao- of Malta-licentie legaal in Nederland?</strong><br>Alleen een vergunning van de Nederlandse Kansspelautoriteit telt. Veel legale aanbieders zijn wel in Malta gevestigd, maar dan hebben ze daarnaast een Nederlandse vergunning. Een casino met alleen een buitenlandse licentie is illegaal in Nederland.</p>
<p><strong>Moet ik belasting betalen over mijn casinowinst?</strong><br>Niet bij een legaal casino: de aanbieder betaalt de kansspelbelasting. Bij een illegale online aanbieder moet je zelf aangifte doen.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "content": content, "content-2": content2, "content-3": content3, "samenvatting": SAMENVATTING,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        import re
        tekst = re.sub(r"<[^>]+>", " ", content + content2 + content3)
        print(len(SAMENVATTING), "tekens samenvatting |", len(tekst.split()), "woorden"); sys.exit()
    print(WF.update_live(ITEM_ID, fd).get("id"))
