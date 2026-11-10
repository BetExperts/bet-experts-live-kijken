# -*- coding: utf-8 -*-
"""NIEUW wedgids-artikel (Nieuws, nog geen item): verificatie bij bookmakers (KYC/cliëntenonderzoek). Waarom een
legale bookmaker je ID, BSN, bankafschriften of loonstrook vraagt, wat er gebeurt als je niet verifieert, privacy en
tips om het snel te regelen.
Slug verificatie-bij-bookmakers-id-en-bankafschriften (gaf HTTP 404 op 10-11-2026, dus vrij). Rubriek Speluitleg,
wedgids-categorie 'Legaal en verantwoord'. Onderwerp: Engelstalige analysesite (niets overgenomen; eigen opzet).
Zoekwoorden: 'verificatie bookmaker', 'bookmaker vraagt bankafschrift', 'account verifiëren bookmaker', 'kyc gokken',
'bookmaker vraagt loonstrook', 'waarom bsn bij goksite', 'uitbetaling geblokkeerd verificatie', 'bron van middelen'.

Feiten nagelopen op 10-11-2026 (bronnen NIET in de tekst genoemd, behalve de wet/Ksa in algemene zin):
- Wet op de kansspelen (wetten.overheid.nl/BWBR0002469, 'Geldend van 12-02-2025 t/m heden') art. 31k lid 1 geen
  kansspelen aan niet-ingeschreven personen; lid 2 inschrijving pas na vaststelling identiteit, 18+, niet in Cruks,
  grenzen speelgedrag; lid 4 vergunninghouder mag het BSN gebruiken.
- Besluit kansspelen op afstand (BWBR0044773, 'Geldend van 15-07-2022 t/m heden'): art. 4.11 lid 1 naam, voornamen,
  geboortedatum, geboorteplaats, BSN 'voor zover die persoon daarover beschikt', fysiek adres, e-mail en telefoon,
  rekeningnummer + tenaamstelling tegenrekening; lid 2 kwaliteitscontrole; lid 3 gegevens onderling geen afwijkingen,
  e-mail of telefoon gevalideerd. Art. 4.12 Cruks vóór inschrijving (Ksa geeft unieke code). Art. 4.13 geen bezwaren
  op grond van Wwft en Sanctiewet 1977. Art. 4.14 grenzen speelgedrag. Art. 4.16 identiteit geverifieerd met
  'voldoende betrouwbaar' methode. Art. 4.18 bij iedere aanmelding identificeren + Cruks. Art. 4.19 lid 1 b schorsing
  bij redelijk vermoeden dat niet (meer) aan de voorwaarden voor inschrijving wordt voldaan; 4.20 onderzoek, schorsing
  voor de duur van het onderzoek; 4.21 schorsing laat inzage in speelrekening onverlet. Art. 4.25 lid 2 b betaalmiddelen
  'ondubbelzinnig' te herleiden tot de speler; 4.26 één speelrekening, één tegenrekening; 4.27 storten alleen van de
  tegenrekening of rekening op naam van de speler; 4.29 lid 1-2 uitbetalen naar de tegenrekening; lid 4 de plicht om op
  verzoek uit te betalen geldt niet zolang de speler is geschorst op grond van 4.19 lid 1 b.
- Besluit werving, reclame en verslavingspreventie kansspelen (BWBR0033412, 'Geldend van 01-01-2026') art. 20 lid 3 en 4:
  BSN alleen voor Cruks en identiteit bij inschrijving, 'onverwijld na het gebruik' vernietigen.
- Wwft (BWBR0024282, 'Geldend van 01-07-2026 t/m heden'): art. 1a lid 4 sub l kansspelaanbieders zijn instelling;
  toezicht Ksa (art. 1d, 'de kansspelautoriteit ... onderdeel l'); art. 3 lid 2 a identificeren en verifiëren, c doel
  en aard relatie, d voortdurende controle 'met zo nodig een onderzoek naar de bron van de middelen'; art. 5 lid 1
  verbod relatie/transactie zonder cliëntenonderzoek, lid 3 relatie beëindigen als cliëntenonderzoek niet lukt;
  art. 8 lid 6 PEP: 'bron van het vermogen en van de middelen'; art. 16 melding ongebruikelijke transactie bij FIU;
  art. 23 lid 1 geheimhouding over een melding, lid 3 AVG-inzage (art. 15) mag zo nodig buiten toepassing blijven;
  art. 33 lid 3 gegevens 5 jaar na einde zakelijke relatie bewaren.
- Ksa Leidraad Wwft (december 2023; kansspelautoriteit.nl/leidraad-wwft, 'op 18 december 2023 ... aangepast'):
  kansspelaanbieders gaan 'altijd een zakelijke relatie' aan, cliëntenonderzoek 'altijd verplicht'; speler mag niet
  deelnemen 'voordat het cliëntenonderzoek is afgerond' (uitzondering o.a. 1-centbetaling voor verificatie);
  verificatie van identiteit moet klaar zijn vóór de zakelijke relatie (geen uitstel, kansspelen geen laag risico);
  geldige documenten: paspoort, NL identiteitskaart, NL rijbewijs, EU-rijbewijs/ID met pasfoto en naam, reisdocumenten
  vluchtelingen/vreemdelingen, vreemdelingendocumenten, 'voldoende betrouwbaar identificatiemiddel'. Bron van middelen
  'zo nodig' (vierde stap); voorbeelden van aanleidingen: inzetten op alle uitkomsten, (zeer) lage quoteringen, opsplitsen
  van transacties, storten en nauwelijks spelen, storting niet van de tegenrekening; alarm bij netto-storting 'méér dan
  €2.500 in 30 dagen' als VOORBEELD ('aan te raden'), netto = stortingen min uitbetalingen; alarm 'hoeft niet automatisch
  een onderzoek te betekenen'; eerst verklaring van de speler, dan zo nodig verificatie via openbare bronnen of documenten
  (bijv. bankafschrift, notarisafrekening). §3.8: relatie niet aangaan of beëindigen als speler 'geen of onvoldoende
  informatie wil geven over de bron van de middelen'; bij herinschrijving nieuwe risico-inschatting.
- Ksa 'Online kansspelaanbieders leven Wwft-verplichtingen nog onvoldoende na' (2-5-2022): Ksa verwacht 'dat er eerder
  onderzoek wordt gedaan' dan bij stortingen 'veel hoger dan 2.500 euro'.
- Netto-stortingsgrens €300 (18 t/m 23) / €700 (24+) per kalendermaand + draagkrachttoets met loonstrook/belastingaangifte:
  Beleidsregel verantwoord spelen 2024, zie netto_stortingslimiet.py (nagelopen 21-10-2026).
- Ksa 'Stel een vraag of doe een melding' (10-11-2026): Ksa bemiddelt niet persoonlijk. Ksa-nieuws 2-4-2026: tegoed
  zonder onnodige vertraging uitbetalen, geen minimumbedrag.
- Rijksoverheid 'Welke organisaties mogen een kopie van mijn identiteitsbewijs maken?' (rijksoverheid.nl/documenten/
  vraag-en-antwoord/identiteitsfraude/ben-ik-verplicht-om-een-kopie-van-mijn-identiteitsbewijs-te-geven-aan-een-bedrijf,
  10-11-2026): 'Slechts enkele organisaties' mogen een kopie vragen, o.a. banken, notarissen en casino's.
  Rijksoverheid 'Hoe maak ik met de KopieID-app een veilige kopie' (10-11-2026): watermerk met doel en ontvanger + datum,
  gegevens wegstrepen afhankelijk van het doel.
- AVG art. 12 lid 3 / art. 15: reactie op inzageverzoek binnen 1 maand, verlengbaar met 2 maanden (rijksoverheid.nl
  'Hoe versterkt de AVG mijn privacyrechten?' en autoriteitpersoonsgegevens.nl 'Recht op inzage', 10-11-2026).
- Praktijk, GEEN wettelijke eis (voorzichtig geformuleerd: 'veel aanbieders'): verificatie via iDIN (inloggen bij je
  bank; o.a. Nederlandse Loterij gebruikt dit volgens een klantverhaal van de leverancier), foto van ID + selfie.
ONZEKER: hoe lang verificatie duurt (verschilt per aanbieder, geen getal genoemd); wat er uiteindelijk met het saldo
gebeurt na beëindiging op grond van de Wwft (niet expliciet geregeld; in de tekst alleen: uitbetaling kan tijdens het
onderzoek worden opgeschort, en terugbetaling gaat alleen naar je eigen tegenrekening).
Bewust weggelaten: namen van bookmakers, exacte verificatietermijnen, EU-witwasverordening (AMLR, pas vanaf juli 2027),
details over FIU-procedures, BSN wegstrepen (een legale aanbieder mag het BSN juist gebruiken voor Cruks).
Rekenvoorbeeld: fictieve stortingen in oktober 2026 -> netto-stortingsgrens €700 en het Wwft-voorbeeldalarm €2.500 in
30 dagen; berekend en ge-assert.
Interne links gecontroleerd op 10-11-2026 (HTTP 200): zie de lijst in de asserts.
  python3 specials/wg_verificatie-bookmaker.py [--live]"""
import os, sys, re
from datetime import date
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
import lk_webflow as WF
from legaal_data import tabel

ITEM_ID = None   # nieuw artikel
SLUG = "verificatie-bij-bookmakers-id-en-bankafschriften"
RUBRIEK = "6672e1c5c1902e8ee8ce98cd"   # zelfde rubriek als andere Legaal-en-verantwoord-artikelen
WEDGIDS_CAT = "Legaal en verantwoord"
TITEL = "Verificatie bij bookmakers: waarom ID en bankafschrift?"
SAMENVATTING = ("Waarom vraagt een bookmaker om je ID, BSN of bankafschriften? Zo werkt verificatie in Nederland, wat er "
                "gebeurt als je niet verifieert en hoe het snel gaat.")

OG_KOP = "Waarom wil je bookmaker je <span>ID</span> zien?"
OG_EYEBROW = "Verificatie (KYC) uitgelegd"
OG_CHIPS = ["Wet Koa en Wwft", "Tips om het snel te regelen"]
OG_MOTIEF = "tabel"
OG_DATA = ["Inschrijving · ID + Cruks", "Elke login · Cruks", "Netto > €700 · draagkracht", "Wwft · bron van je geld"]

CRUKS = "/nieuws/cruks-de-gokstop-voor-verantwoord-gokken"
NETTO = "/nieuws/netto-stortingslimiet"
GEGEVENS = "/nieuws/dit-is-wat-casinos-doen-met-jouw-gegevens"
LEGAAL = "/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland"
LEEFTIJD = "/nieuws/minimum-leeftijd-gokken-nederland"
VERANTWOORD = "/speel-bewust/verantwoord-wedden"
KSA = "<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"
MAANDEN = ["januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus", "september", "oktober",
           "november", "december"]


def eur(x):
    return "€" + f"{x:,.0f}".replace(",", ".")


def datum(d):
    return f"{d.day} {MAANDEN[d.month - 1]}"


# ---- rekenvoorbeeld (fictief): speler van 30, stortingen en opnames in oktober 2026 ----
NETTO_GRENS, WWFT_ALARM = 700, 2500     # Ksa-beleidsregel (24+) en voorbeeldalarm uit de Ksa-leidraad Wwft (30 dagen)
MUTATIES = [(date(2026, 10, 3), 500), (date(2026, 10, 8), 400), (date(2026, 10, 14), 800),
            (date(2026, 10, 18), -300), (date(2026, 10, 24), 1300)]
assert (MUTATIES[-1][0] - MUTATIES[0][0]).days < 30 and len({d.month for d, _ in MUTATIES}) == 1
RIJEN, saldo, OVER_700, OVER_2500 = [], 0, None, None
for d, b in MUTATIES:
    saldo += b
    if OVER_700 is None and saldo > NETTO_GRENS: OVER_700 = d
    if OVER_2500 is None and saldo > WWFT_ALARM: OVER_2500 = d
    noot = ("Boven €700 netto: verder storten pas na draagkrachttoets" if d == OVER_700 else
            "Boven €2.500 in 30 dagen: aanleiding om naar de herkomst te kijken" if d == OVER_2500 else "")
    RIJEN.append((datum(d), ("Storting " if b > 0 else "Opname ") + eur(abs(b)), eur(saldo), noot))
NETTO_EIND = saldo
assert NETTO_EIND == 2700 and OVER_700 == date(2026, 10, 8) and OVER_2500 == date(2026, 10, 24)
STORT = sum(b for _, b in MUTATIES if b > 0)
OPNAME = -sum(b for _, b in MUTATIES if b < 0)
assert (STORT, OPNAME) == (3000, 300)

content = f"""<p><strong>Een bookmaker met een Nederlandse vergunning moet wettelijk vaststellen wie je bent voordat je mag wedden: je naam, geboortedatum, adres, bankrekening en, als je dat hebt, je burgerservicenummer. Zo controleert hij of je 18+ bent, of je een gokstop in Cruks hebt en of er risico op witwassen is. Om bankafschriften of een loonstrook vraagt hij later, als hij moet nagaan of je je stortingen kunt dragen of waar je geld vandaan komt. Werk je niet mee, dan kan hij je account schorsen en een uitbetaling tijdelijk tegenhouden.</strong></p>
<p>Verificatie heet in de branche ook KYC: know your customer, ken je klant. Voor veel spelers is het de vervelendste stap van een nieuw account, zeker als er later nog een verzoek om een bankafschrift komt. In dit artikel lees je welke controles verplicht zijn, wanneer een bookmaker om extra documenten vraagt, wat er met je gegevens gebeurt en hoe je het zo snel mogelijk regelt.</p>
<h3><strong>Waarom moet een bookmaker weten wie je bent?</strong></h3>
<p>Daar zijn twee wetten voor. De <strong>Wet op de kansspelen</strong> bepaalt dat een online aanbieder je pas mag inschrijven als je identiteit is vastgesteld, als vaststaat dat je 18 jaar of ouder bent, als je niet in Cruks staat en als je je eigen speelgrenzen hebt ingesteld. Lees meer over de <a href="{LEEFTIJD}">minimumleeftijd en speelgrenzen</a>.</p>
<p>Daarnaast vallen kansspelaanbieders onder de <strong>Wwft</strong>, de Wet ter voorkoming van witwassen en financieren van terrorisme. Net als een bank moet een bookmaker daardoor cliëntenonderzoek doen: wie ben je, wat is het doel van je account en past wat je doet bij wat hij van je weet. Volgens de Kansspelautoriteit (Ksa), die hierop toezicht houdt, is dat onderzoek voor kansspelaanbieders altijd verplicht. Het moet klaar zijn voordat je je eerste weddenschap plaatst.</p>
<h3><strong>Welke gegevens moet je opgeven bij je inschrijving?</strong></h3>
<p>De regels schrijven precies voor wat een aanbieder minimaal van je moet hebben:</p>
{tabel(["Gegeven", "Waarvoor"], [
    ("Naam, voornamen, geboortedatum en geboorteplaats, zoals op je identiteitsbewijs", "Identiteit en leeftijd vaststellen, Cruks raadplegen"),
    ("Burgerservicenummer, als je dat hebt", "Alleen voor de Cruks-check en je identificatie bij inschrijving"),
    ("Woonadres, e-mailadres en telefoonnummer", "Identificatie en contact; je e-mail of telefoon wordt gecontroleerd"),
    ("Rekeningnummer en tenaamstelling", "Je vaste tegenrekening voor stortingen en uitbetalingen"),
    ("Je speelgrenzen", "Verplicht: maximale speeltijd, stortingen en saldo"),
])}
<p>Alle gegevens moeten met elkaar kloppen. Staat de bankrekening op een andere naam dan je identiteitsbewijs, dan mag de aanbieder je niet inschrijven. Je BSN mag hij na gebruik niet bewaren: de regels schrijven voor dat hij het direct vernietigt.</p>
<h3><strong>Hoe verloopt de verificatie?</strong></h3>
<p>Na het invullen van het formulier doorloopt de aanbieder een vaste reeks controles:</p>
<ul><li><strong>Contact bevestigen:</strong> je klikt op een link in een e-mail of vult een sms-code in.</li><li><strong>Identiteit verifiëren:</strong> met een methode die 'voldoende betrouwbaar' is. Veel aanbieders laten je inloggen bij je eigen bank via iDIN, of vragen een foto van je identiteitsbewijs met een selfie. Ook een kleine controlebetaling van je eigen rekening komt voor.</li><li><strong>Cruks raadplegen:</strong> de aanbieder krijgt alleen te zien óf je in het register staat.</li><li><strong>Witwas- en sanctiecheck:</strong> de aanbieder controleert onder meer sanctielijsten en of je een politiek prominent persoon (PEP) bent.</li><li><strong>Speelgrenzen instellen:</strong> pas daarna kun je storten en spelen.</li></ul>
<p>Geldige documenten zijn onder meer een paspoort, een Nederlandse identiteitskaart of een Nederlands rijbewijs. Een EU-rijbewijs of EU-identiteitskaart met pasfoto en naam en een verblijfsdocument tellen ook. Hoe snel het gaat, verschilt per aanbieder: een digitale controle via je bank is vaak direct klaar, een handmatige beoordeling van een foto kan langer duren.</p>"""

content2 = f"""<h3><strong>Waarom controleert een bookmaker Cruks bij elke login?</strong></h3>
<p>De controle bij inschrijving is niet genoeg. Een legale aanbieder moet je bij <em>iedere</em> aanmelding opnieuw identificeren en Cruks raadplegen. Heb je in de tussentijd een gokstop aangevraagd, dan kom je er niet meer in. Is Cruks door een storing even niet bereikbaar, dan mag de aanbieder je binnenlaten, maar moet hij achteraf alsnog controleren. Meer hierover lees je in ons artikel over <a href="{CRUKS}">Cruks, de gokstop</a>.</p>
<h3><strong>Wanneer vraagt een bookmaker om bankafschriften of een loonstrook?</strong></h3>
<p>Een verzoek om extra documenten komt meestal pas als je al een tijd speelt. Daar zijn drie verschillende redenen voor, en ze worden vaak door elkaar gehaald:</p>
{tabel(["Reden", "Wanneer?", "Wat kun je verwachten?"], [
    ("<strong>Zorgplicht: kun je het dragen?</strong>", "Je netto stortingen gaan boven €300 (18 t/m 23 jaar) of €700 (vanaf 24) per kalendermaand", "Loonstrook of belastingaangifte"),
    ("<strong>Wwft: waar komt het geld vandaan?</strong>", "Je stortingen of je speelgedrag passen niet bij wat de aanbieder van je weet", "Eerst een verklaring, zo nodig een bankafschrift of ander bewijs"),
    ("<strong>Gegevens kloppen niet</strong>", "Een storting komt van een andere rekening, of je naam of adres wijkt af", "Bijvoorbeeld een bankafschrift met je naam en rekeningnummer"),
])}
<p>Bij de eerste reden gaat het om jouw bescherming. Hoe dat precies werkt, lees je in ons artikel over de <a href="{NETTO}">netto stortingslimiet</a>.</p>
<p>Bij de tweede reden gaat het om de <strong>bron van middelen</strong>: het geld dat je nu inzet. Komt het van je salaris, een spaarrekening, een erfenis of de verkoop van je auto? De Ksa noemt in haar leidraad voorbeelden van situaties waarin een aanbieder dat kan onderzoeken: veel storten en nauwelijks spelen, inzetten op alle uitkomsten van een wedstrijd, vooral op heel lage odds wedden, of storten via iets anders dan je vaste tegenrekening, zoals een e-wallet. De <strong>bron van vermogen</strong> gaat verder: hoe je totale vermogen is ontstaan. Daar moet een aanbieder volgens de Wwft onder meer naar kijken bij politiek prominente personen.</p>
<p>Ook winst bij andere goksites is niet automatisch een verklaring. Wie €1.000 stort en €800 laat uitbetalen, heeft €200 verloren, ook al staat er €800 'winst' op het bankafschrift. Daarom kan een aanbieder vragen om ook je stortingen bij die andere site te laten zien.</p>
<h3><strong>Rekenvoorbeeld: wanneer gaan de signalen af?</strong></h3>
<p>Een speler van 30 stort en neemt in oktober het volgende op. <em>Bedragen zijn fictief.</em> Netto storten betekent: alles wat je stort, min wat je opneemt.</p>
{tabel(["Datum", "Transactie", "Netto gestort", "Wat gebeurt er?"], RIJEN)}
<p>Op {datum(OVER_700)} komt de speler boven de netto-stortingsgrens van €700. Daarna mag de aanbieder pas nieuwe stortingen toestaan als uit een draagkrachttoets blijkt dat de speler dat kan missen. Stel dat hij met een loonstrook aantoont dat dat zo is. Op {datum(OVER_2500)} staat hij in nog geen maand {eur(NETTO_EIND)} netto in de min ({eur(STORT)} gestort, {eur(OPNAME)} opgenomen). Een netto-storting van meer dan €2.500 in 30 dagen noemt de Ksa in haar Wwft-leidraad als voorbeeld van een grens waarbij een aanbieder een signaal kan instellen. Dat signaal betekent niet automatisch een onderzoek, maar de aanbieder kan de speler nu vragen om uit te leggen waar het geld vandaan komt, en zo nodig om een bankafschrift.</p>"""

content3 = f"""<h3><strong>Wat gebeurt er als je niet verifieert?</strong></h3>
<p>Dat hangt af van het moment:</p>
<ul><li><strong>Bij inschrijving:</strong> zonder geverifieerde identiteit, Cruks-check en witwascheck mag de aanbieder je niet inschrijven. Je kunt dus niet eerst spelen en later verifiëren.</li><li><strong>Tijdens het spelen:</strong> heeft de aanbieder een redelijk vermoeden dat je niet meer aan de voorwaarden voldoet, dan moet hij je account schorsen en dat onderzoeken. Zolang die schorsing loopt, hoeft hij je saldo niet uit te betalen. Je houdt wel inzage in je speelrekening.</li><li><strong>Als je geen informatie geeft:</strong> lukt het cliëntenonderzoek niet, bijvoorbeeld omdat je niets wilt zeggen over de herkomst van je geld, dan moet de aanbieder de relatie volgens de Wwft beëindigen.</li></ul>
<p>Uitbetalingen gaan bovendien alleen naar je eigen tegenrekening, de rekening waarmee je hebt gestort. Wie probeert uit te betalen naar een andere rekening, stuit dus altijd op een controle. Vind je dat een aanbieder je ten onrechte tegenhoudt, dien dan een klacht in via de klachtenprocedure op de site. De Ksa bemiddelt niet in individuele zaken.</p>
<h3><strong>Is het veilig om je ID en bankafschriften te sturen?</strong></h3>
<p>Bij een aanbieder met een Nederlandse vergunning wel. Volgens de Rijksoverheid mogen maar enkele organisaties een kopie van je identiteitsbewijs vragen, en casino's en kansspelaanbieders horen daar bij. Er gelden strenge regels voor wat er met je gegevens gebeurt:</p>
<ul><li>Je BSN mag alleen worden gebruikt voor Cruks en je identificatie en moet daarna direct worden vernietigd.</li><li>Gegevens uit het cliëntenonderzoek worden vijf jaar na het sluiten van je account bewaard, omdat de Wwft dat verplicht.</li><li>Je kunt onder de AVG opvragen welke gegevens de aanbieder van je heeft. Hij moet binnen een maand reageren, of uitleggen waarom het langer duurt.</li><li>Heeft de aanbieder een melding van een ongebruikelijke transactie gedaan, dan mag hij je dat niet vertellen. Die geheimhouding gaat in dat geval voor je inzagerecht.</li></ul>
<p>Bij een illegale goksite heb je die bescherming niet. Controleer daarom altijd eerst <a href="{LEGAAL}">of een bookmaker legaal is in Nederland</a>. Wat legale aanbieders verder met je gegevens doen, lees je in ons artikel over <a href="{GEGEVENS}">gegevens bij online casino's en bookmakers</a>.</p>
<h3><strong>Hoe regel je de verificatie zo snel mogelijk?</strong></h3>
<ul><li><strong>Gebruik je eigen bankrekening</strong> op je eigen naam. Een rekening van je partner of ouders levert altijd vertraging op.</li><li><strong>Vul je gegevens exact in</strong> zoals ze op je identiteitsbewijs staan, inclusief alle voornamen.</li><li><strong>Zorg voor een geldig identiteitsbewijs.</strong> Een verlopen paspoort wordt niet geaccepteerd.</li><li><strong>Kies de digitale route</strong> als die er is, zoals verificatie via je bank.</li><li><strong>Maak een veilige kopie</strong> met de KopieID-app van de Rijksoverheid en zet in het watermerk voor wie de kopie is en waarvoor.</li><li><strong>Upload documenten alleen in je account</strong> op de site of in de app, nooit via een link in een onverwachte mail of een chatbericht.</li><li><strong>Stuur een recent en volledig bankafschrift</strong> waarop je naam en rekeningnummer staan als daarom wordt gevraagd.</li></ul>
<p>Merk je dat je vaker stort dan je van plan was, stel dan een lagere stortingslimiet in. Dat werkt direct. Meer tips vind je bij <a href="{VERANTWOORD}">verantwoord wedden</a> en in de <a href="/wedgids">wedgids</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Waarom vraagt een bookmaker om mijn BSN?</strong><br>Om in Cruks te controleren of je een gokstop hebt en om je identiteit vast te stellen. De aanbieder mag je BSN alleen daarvoor gebruiken en moet het daarna direct vernietigen. Heb je geen BSN, dan kun je je ook zonder inschrijven.</p>
<p><strong>Kan ik wedden zonder verificatie?</strong><br>Niet bij een legale bookmaker. De identiteitscontrole, de Cruks-check en de witwascheck moeten klaar zijn voordat je kunt spelen.</p>
<p><strong>Waarom vraagt mijn bookmaker om een bankafschrift?</strong><br>Meestal omdat hij moet nagaan of je stortingen passen bij je inkomen of vermogen (Wwft), of omdat een storting niet van je eigen rekening lijkt te komen. Voor de netto-stortingsgrens gaat het vaker om een loonstrook of belastingaangifte.</p>
<p><strong>Mag een bookmaker mijn uitbetaling tegenhouden als ik niet verifieer?</strong><br>Tijdelijk wel: zolang je account is geschorst voor onderzoek, geldt de plicht om op verzoek uit te betalen niet. Uitbetalen gebeurt bovendien altijd naar je eigen tegenrekening.</p>
<p><strong>Moet ik mij bij elke bookmaker opnieuw laten verifiëren?</strong><br>Ja. Elke aanbieder schrijft je zelf in en moet zelf je identiteit verifiëren en Cruks raadplegen.</p>
<p><strong>Kan de Kansspelautoriteit helpen als mijn verificatie vastloopt?</strong><br>Nee, de Ksa bemiddelt niet in individuele zaken. Dien eerst een klacht in bij de aanbieder; die moet binnen acht weken schriftelijk en gemotiveerd reageren.</p>
{KSA}"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    html = content + content2 + content3
    assert re.search(r"<(ul|ol|/li)>\s+<", html) is None
    assert "/kennisbank/" not in html and "<h2" not in html and "<h4" not in html and "/go/" not in html
    assert html.rstrip().endswith(KSA)
    assert content.startswith("<p><strong>")
    assert len(TITEL) <= 60 and 110 <= len(SAMENVATTING) <= 160, (len(TITEL), len(SAMENVATTING))
    assert TITEL.lower().startswith("verificatie bij bookmakers")
    assert len(OG_CHIPS) == 2 and len(OG_DATA) == 4 and html.count("<table") >= 3
    for link in (CRUKS, NETTO, GEGEVENS, LEGAAL, LEEFTIJD, VERANTWOORD, "/wedgids"):
        assert f'href="{link}"' in html, link
    assert all(h.startswith("<h3><strong>") for h in re.findall(r"<h3>.*?</h3>", html))
    verboden = ("footymetrics", "betcity", "opstellingvandaag", "waaroptv")
    assert not any(v in html.lower() for v in verboden)
    faq = content3.split("Veelgestelde vragen")[1]
    assert 4 <= faq.count("<p><strong>") <= 6
    tekst = re.sub(r"<[^>]+>", " ", html)
    woorden = len(tekst.split())
    assert 1200 <= woorden <= 2200, woorden
    print(len(TITEL), "titel |", len(SAMENVATTING), "samenvatting |", woorden, "woorden |",
          [len(re.sub(r"<[^>]+>", " ", c).split()) for c in (content, content2, content3)])
    # ---- --live: NIET zelf draaien; alleen na akkoord van Jasper (bij voorkeur via wg_publiceer.py verificatie-bookmaker
    #      --live, dat ook de deelkaart en wedgids-categorie regelt). Na livegang van account-beperkt kan een link naar
    #      /nieuws/account-beperkt-bookmaker erbij (nu nog 404) ----
    if "--live" in sys.argv:
        fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
              "samenvatting": SAMENVATTING, "rubriek": RUBRIEK, "wedgids": True,
              "publicatiedatum": datetime.now(timezone.utc).isoformat()}
        print("item:", WF.create_live(fd), "https://www.bet-experts.nl/nieuws/" + SLUG)
