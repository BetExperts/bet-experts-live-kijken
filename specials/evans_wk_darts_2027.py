# -*- coding: utf-8 -*-
"""Los artikel: gaat Ricky Evans naar het WK Darts 2027? (17-11-2026)

Kernantwoord: nee, nog niet - en anders dan Plaisier en De Zwaan heeft Evans het
vanavond nog zelf in handen. Hij mist de ProTour-route definitief met £1.250 (85e
ongefilterd, ±46e gefilterd), staat 52e op de wereldranglijst met £167.500 terwijl
de 40e plek op £194.250 staat, en speelt dinsdagavond 17 november om 21:45 tegen
James Wade om groep K van de Grand Slam of Darts. Hij heeft MINIMAAL de kwartfinale
nodig om alsnog in de wereldtop 40 te komen. Daarnaast blijft de PDC Tour Card Holder
Qualifier van 30 november (4 tickets).

Feiten en bronnen: specials/evans_wk_feiten.md + wk_darts_kwalificatie_data.py.
LET OP de bronnendiscrepantie die in de tekst wordt benoemd: pdc.tv geeft 52e/£167.500
(Grand Slam-geld nog niet verwerkt), dartsrankings.com en dartrankings.co.uk geven
allebei £177.000 doorgerekend naar de peildatum (45e resp. 43e). Dat bedrag klopt exact
met zijn seizoensopbouw 2024 £25.000 + 2025 £103.750 + 2026 £48.250. Beide genoemd.

Bewust weggelaten (niet hard te krijgen, zie het feitenrapport):
- worpen/darts per minuut (geen enkele bron)
- het jaar waarin de Shakin' Stevens-kerstopkomst begon (nergens vermeld; bewijs vanaf dec 2023)
- de locatie van de Tour Card Holder Qualifier
- seizoensgemiddelde, aantal 180's en checkoutpercentage over 2026
- zijn eigen zin "2014 was the last time I didn't qualify" (feitelijk onjuist: hij miste
  ook 2015 en 2018) - we geven de echte reeks in plaats daarvan
- de 180 in 2,16 seconden wordt genoemd MET het voorbehoud dat de PDC geen officieel
  register bijhoudt en bronnen botsen over het jaar (WK 2016 vs WK 2017)
- dat Shakin' Stevens "bijna 80" zou zijn (Evans' eigen woorden; hij is 77)

Slug 404 gecontroleerd op 17-11.
Bijwerken: na de Grand Slam (22 nov), na de Players Championship Finals (29 nov) en na de
Tour Card Holder Qualifier (30 nov) is het antwoord definitief.
  python3 specials/evans_wk_darts_2027.py        (dry run)
  kaart: ../superodd-agent/.venv/bin/python og_kaarten/wk_darts_kwalificatie.py evans_wk_darts_2027
  publiceren: specials/concept_publiceer.py evans_wk_darts_2027 --live"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel
import wk_darts_kwalificatie_data as D

SLUG = "gaat-ricky-evans-naar-het-wk-darts-2027"
RUBRIEK = D.RUBRIEK
TITEL = "Gaat Ricky Evans naar het WK Darts 2027? Zo staat het"
SAMENVATTING = ("Ricky Evans mist het WK Darts 2027 met 1.250 pond en staat 52e op de wereldranglijst. "
                "Dit heeft hij nog nodig, en wanneer het beslist wordt.")

GSOD = '<a href="/nieuws/grand-slam-of-darts-2026-voorspellingen-wedtips-dinsdag">onze voorspellingen voor dinsdagavond</a>'
SCHEMA = '<a href="/nieuws/speelschema-grand-slam-of-darts-2026">het speelschema van de Grand Slam of Darts</a>'

RANGLIJSTEN = [
    ("Wereldranglijst (twee jaar), officiële stand nu", "<strong>52e</strong>", "&pound;167.500",
     "40e: Callan Rydz, &pound;194.250", "<strong>&minus; &pound;26.750</strong>"),
    ("<em>Dezelfde lijst, doorgerekend naar de peildatum</em>", "<em>45e</em>", "<em>&pound;177.000</em>",
     "<em>40e: Callan Rydz, &pound;195.250</em>", "<em>&minus; &pound;18.250</em>"),
    ("ProTour-ranglijst (een jaar)", "85e", "&pound;32.000", "&ndash;", "&ndash;"),
    ("<em>Dezelfde lijst, zonder wie al via de wereldranglijst binnen is</em>",
     "<strong>46e</strong>", "<strong>&pound;32.000</strong>", "40e: Henry Coates, &pound;33.250",
     "<strong>&minus; &pound;1.250</strong>"),
    ("Players Championship-ranglijst", "123e", "&pound;13.000", "64e: Henry Coates, &pound;33.250", "&minus; &pound;20.250"),
]

SCENARIO = [
    ("Tweede in de groep &mdash; hij verliest vanavond", "&pound;12.500", "&pound;177.000", "Nee"),
    ("Laatste 16 &mdash; hij wint vanavond en verliest daarna", "&pound;20.000", "&pound;184.500", "Nee"),
    ("<strong>Kwartfinale</strong>", "<strong>&pound;35.000</strong>", "<strong>&pound;199.500</strong>", "<strong>Ja, net</strong>"),
    ("Halve finale", "&pound;60.000", "&pound;224.500", "Ja"),
    ("Finale", "&pound;100.000", "&pound;264.500", "Ja"),
    ("Toernooiwinst", "&pound;200.000", "&pound;364.500", "Ja"),
]

WK_HISTORIE = [
    ("2014", "Tweede ronde", "Mervyn King 2-4 v", "Zijn debuut"),
    ("2015", "Niet gekwalificeerd", "&ndash;", "&ndash;"),
    ("2016", "Tweede ronde", "Jamie Caven 0-4 v", "130-finish om Simon Whitlock te verslaan"),
    ("2017", "Eerste ronde", "Michael Smith 2-3 v", "De beroemde 180 in 2,16 seconden"),
    ("2018", "Niet gekwalificeerd", "&ndash;", "&ndash;"),
    ("2019", "Eerste ronde", "Rowby-John Rodriguez 1-3 v", "Start van acht deelnames op rij"),
    ("2020", "<strong>Derde ronde</strong>", "Michael van Gerwen 0-4 v", "&ndash;"),
    ("2021", "<strong>Derde ronde</strong>", "Michael van Gerwen 0-4 v", "&ndash;"),
    ("2022", "Tweede ronde", "Daryl Gurney 1-3 v", "&ndash;"),
    ("2023", "Tweede ronde", "Joe Cullen 1-3 v", "Snelste 180 van de partij: 2,28 seconden"),
    ("2024", "<strong>Derde ronde</strong>", "Daryl Gurney 2-4 v", "Won in ronde 2 van Nathan Aspinall"),
    ("2025", "<strong>Derde ronde</strong>", "Rob Owen 2-4 v", "&ndash;"),
    ("2026", "<strong>Derde ronde</strong>", "Charlie Manby 2-4 v", "Stond 2-1 voor; hierna begonnen zijn moeilijke maanden"),
]

SEIZOEN = [
    ("WK Darts (januari)", "Derde ronde", "2-4 tegen Charlie Manby, na een 2-1 voorsprong"),
    ("UK Open", "Vierde ronde", "Hier gooide hij 102,49 tegen Brendan Dolan: zijn hoogste gemiddelde van 2026"),
    ("Baltic Sea Darts Open", "<strong>Halve finale</strong>", "Zijn beste resultaat van het jaar, met een 6-4 zege op James Wade"),
    ("Players Championships", "Zwak", "Negen van de 33 openingswedstrijden gewonnen; eind oktober acht toernooien op rij direct eruit"),
    ("Players Championship Finals", "Niet gekwalificeerd", "123e op de Players Championship-ranglijst; de top 64 mocht naar Minehead"),
    ("Grand Slam of Darts", "Groepsfase", "Via de Tour Card Holder Qualifier; won met 5-4 van Cam Crabtree"),
]

PRIJZENGELD = [("2024", "&pound;25.000"), ("2025", "&pound;103.750"), ("2026", "&pound;48.250")]


content = f"""<p><strong>Nee, Ricky Evans is nog niet zeker van het WK Darts 2027 &mdash; maar anders dan de meeste spelers op de wip heeft hij het vanavond nog zelf in handen. Hij miste het startbewijs via de ProTour-ranglijst met &pound;1.250, staat op de wereldranglijst 52e terwijl alleen de top 40 doorgaat, en speelt dinsdagavond om 21:45 uur tegen James Wade om groep K van de Grand Slam of Darts. Om via de ranglijst binnen te komen heeft hij minimaal de kwartfinale nodig. Lukt dat niet, dan rest de Tour Card Holder Qualifier van 30 november.</strong></p>
<p>Dat is het korte antwoord. Hieronder staat precies hoe hij ervoor staat op alle ranglijsten die meetellen, wat elk resultaat in Wolverhampton hem oplevert, en waarom het voor deze speler meer is dan een startbewijs: Evans staat op het punt zijn reeks van acht WK-deelnames op rij te verliezen &mdash; en daarmee de opkomst waar Alexandra Palace elk jaar op wacht.</p>
<h3><strong>Zo staat Ricky Evans ervoor</strong></h3>
<p>Voor het WK tellen twee ranglijsten. De wereldranglijst is een geldlijst over twee jaar, waarvan de top 40 rechtstreeks binnen is. De ProTour-ranglijst gaat alleen over dit seizoen en verdeelt daarna nog eens 40 plekken onder de spelers die via de wereldranglijst net niet binnen zijn.</p>
{tabel(["Ranglijst", "Positie", "Prijzengeld", "Laatste plek die zich plaatst", "Verschil"], RANGLIJSTEN)}
<p><em>Over de twee bedragen op de wereldranglijst: &pound;167.500 is de officiële stand op de PDC-site, waarin het prijzengeld van de Grand Slam nog niet is verwerkt &mdash; de PDC schrijft geld pas bij als een toernooi is afgelopen. De &pound;177.000 is de stand doorgerekend naar de peildatum van eind november, inclusief wat hij deze week al verdiende. Twee onafhankelijke ranglijstsites komen op dat bedrag, en het klopt precies met zijn seizoensopbouw.</em></p>
<p>De vierde regel is de pijnlijkste. Op de geschoonde ProTour-lijst, waar de laatste veertig WK-tickets liggen, eindigde Evans zes plekken en <strong>&pound;1.250</strong> onder de streep. Tussen hem en de veertigste plek staan precies vijf spelers: {D.L['plaisier']}, {D.L['zwaan']}, Shane McGuirk, Cam Crabtree en David Sharp. Die lijst ligt sinds 5 november definitief vast: er staan geen ProTour-toernooien meer op het programma. Die route is dus dicht.</p>
<p>Nog een cijfer dat laat zien hoe het ging: op de Players Championship-ranglijst staat hij 123e met &pound;13.000. De top 64 mocht naar de Players Championship Finals in Minehead, en de 64e plek ging &mdash; opnieuw &mdash; naar Henry Coates met &pound;33.250. Evans speelt dat toernooi dus niet, en dat is meer dan een gemist weekend: het betekent dat de <strong>Grand Slam het enige toernooi is waarmee hij zijn ranglijstpositie nog kan verbeteren</strong>, terwijl zijn concurrenten eind november nog een heel weekend lang geld kunnen bijschrijven.</p>
<h3><strong>Wat levert vanavond hem op?</strong></h3>
<p>Evans staat op twee punten, net als Wade. Crabtree is uitgeschakeld, dus dit is een zuivere knock-out: de winnaar pakt groep K, de verliezer gaat naar huis. In deze tabel staat wat elk resultaat betekent voor zijn stand op de peildatum, afgezet tegen de veertigste plek die rond &pound;195.250 ligt.</p>
{tabel(["Hoe ver komt hij?", "Prijzengeld", "Totaal op de peildatum", "Boven de streep?"], SCENARIO)}
<p><em>Projectie op basis van de doorgerekende ranglijst. Het prijzengeld van de Grand Slam telt mee voor de wereldranglijst.</em></p>
<p>Daar staat het zwart op wit: <strong>winnen vanavond is niet genoeg.</strong> Ook een plek bij de laatste zestien laat hem nog ruim &pound;10.000 tekortkomen. Hij heeft minstens de kwartfinale nodig, en zelfs dan is het niet veilig &mdash; want wie net boven hem staat, speelt in Minehead nog door terwijl zijn eigen totaal dan vastligt. Pas bij een halve finale kan hij echt achteroverleunen.</p>
<p>Het goede nieuws: hij heeft hier eerder gewonnen van deze tegenstander. In mei versloeg hij Wade met 6-4 op de Baltic Sea Darts Open, en op het WK van vorig jaar schakelde hij hem uit met 3-2, met zijn achtste matchdart. Onderling leidt Wade met 8-5, maar Evans won twee van hun laatste drie duels. Wat wij van die partij verwachten, en van de zeven andere duels van dinsdagavond, staat in {GSOD} &mdash; eerlijk gezegd staat onze eigen tip daar op Wade. Het volledige programma vind je in {SCHEMA}.</p>
<p>Hijzelf is er helder over. &bdquo;I've now got that one game to kind of change my Christmas&rdquo;, zei hij dinsdagochtend. &bdquo;And if I can beat Wadey, who knows what I can do?&rdquo;</p>"""

content2 = f"""<h3><strong>De Tour Card Holder Qualifier: zijn tweede kans</strong></h3>
<p>Lukt het vanavond niet, dan blijft er één route over. Op maandag 30 november, de dag nadat beide ranglijsten op slot gaan, speelt de PDC een apart kwalificatietoernooi voor Tour Card-houders die zich nog niet hebben geplaatst. Er liggen vier WK-tickets. Evans mag meedoen: hij heeft sinds 2019 onafgebroken een Tour Card en staat ver binnen de top 64 die de kaart behoudt, dus zijn plek op de tour loopt geen gevaar.</p>
{tabel(["Wanneer", "Wat", "Waar", "Welke ranglijst"], D.AGENDA)}
<p>Diezelfde avond verricht de PDC ook de loting, dus op maandag 30 november is het hele veld van 128 bekend. Hoe hij er zelf over denkt, zei hij deze week in Wolverhampton: &bdquo;If I'm not in the Worlds, who cares? You've got a qualifier to get yourself in through the back door. There's more to life, but I'm going to give it a go.&rdquo;</p>
<h3><strong>Zo zijn de 128 plekken op het WK verdeeld</strong></h3>
<p>Het WK Darts duurt van {D.WK['start']} tot en met {D.WK['eind']} en wordt gespeeld in {D.WK['zaal']}. Er doen {D.WK['veld']} spelers mee, die allemaal in de eerste ronde beginnen; de top 32 van de wereldranglijst is geplaatst. De prijzenpot is {D.WK['pot']}, met {D.WK['winnaar']} voor de wereldkampioen en {D.WK['r1']} voor iedereen die in de eerste ronde verliest.</p>
{tabel(["Route", "Plekken", "Hoe het werkt"], D.ROUTES)}
<p>Meer over het toernooi zelf, het speelschema en het prijzengeld per ronde staat op {D.L['hub']}. {D.L['stats']} vind je in ons overzicht van alle records.</p>
<h3><strong>De opkomst waar Ally Pally elk jaar op wacht</strong></h3>
<p>Dit is waarom het meer dan een ranglijstverhaal is. Op het WK loopt Evans op naar <strong>&bdquo;Merry Christmas Everyone&rdquo; van Shakin' Stevens</strong>, in een kerstshirt, met een opblaasbare elf, en met de hele Great Hall die meezingt. Hij houdt de microfoon erbij en laat de zaal het werk doen; in 2026 droeg hij een shirt met zichzelf als Kerstman erop. De dartsmedia noemen het inmiddels een van de vaste tradities van het toernooi.</p>
<p>Zijn plannen gaan verder dan het shirt. &bdquo;I want to walk on with genuine elves&rdquo;, zei hij vorig jaar. &bdquo;I want elves to walk me on, I want reindeer, I'd like to throw snowballs into the crowd with presents or flights in it.&rdquo; Waarna de nuchtere toevoeging: &bdquo;But I think there's too much health and safety involved with some of those walk-ons.&rdquo; Hij vroeg ook publiekelijk om de zanger zelf: &bdquo;Can we get Shakin' Stevens here?&rdquo; Dat is nooit gelukt.</p>
<p>Het mooiste detail zit in de bekentenis erachter. &bdquo;I'm someone that hates Christmas, by the way&rdquo;, zei hij. Hij doet het omdat het werkt: &bdquo;Everyone seems to be in the party mood, and it gets them on my side as well.&rdquo; En over wat die steun met hem doet: &bdquo;They seem to love me.&rdquo; Hij zei dat hij met die zaal achter zich met 3-0 had kunnen verliezen en nog steeds glimlachend was vertrokken &mdash; de steun &bdquo;gives you drive&rdquo;. Zichzelf noemt hij in december &bdquo;the Michael Bublé of darts&rdquo;. En over het shirt: &bdquo;Well, I've never lost a game in a Christmas shirt.&rdquo;</p>
<p>Op andere toernooien gebruikt hij andere muziek, en juist deze maand wisselde hij. Vlak voor de Grand Slam ruilde hij Madonna's &bdquo;Like a Prayer&rdquo; in voor &bdquo;Daydream Believer&rdquo; van The Monkees, een tip van zijn vriend en collega James Wilson. &bdquo;I love that song&rdquo;, zei hij. &bdquo;Every time I go to a bar, a disco, a wedding or whatever, I love a bit of the Monkees. I thought: that's a bit me.&rdquo; De reden voor de wissel is typisch Evans: &bdquo;It went brilliantly at the Worlds, but I'm a superstitious person, and I never seem to win with it.&rdquo; Na zijn eerste zege op het nieuwe nummer: &bdquo;I really enjoyed that tonight, so hopefully that could be the one.&rdquo;</p>
<h3><strong>Waarom hij &bdquo;Rapid&rdquo; heet</strong></h3>
<p>De bijnaam is letterlijk bedoeld. Evans gooit zijn drie pijlen doorgaans binnen drie tot vijf seconden nadat hij bij de oche staat, en dat tempo maakte hem beroemd voordat zijn resultaten dat deden. Zijn bekendste moment is een <strong>180 in 2,16 seconden</strong>, gegooid tegen Michael Smith op het WK. Een officieel record is het niet: de PDC houdt daar geen register van bij, en bronnen zijn het niet eens over het jaar. Commentator Wayne Mardle, die hem de snelste speler noemt die hij ooit zag, vatte het destijds zo samen: &bdquo;It's just wrong. It's just madness.&rdquo;</p>
<p>Opvallend genoeg kwamen zijn beste resultaten toen hij juist gas terugnam. Na zijn zege op Nathan Aspinall op het WK van 2024 zei Mardle: &bdquo;He's a better darts player than he's ever been. He has slowed down, I believe that's the reason why he's getting results.&rdquo; Evans gooide twee negendarters in de PDC, waarvan die bij Players Championship 30 in 2023 tegen Callan Rydz door de dartsmedia werd omschreven als mogelijk de snelste ooit &mdash; al is ook die nooit geklokt.</p>"""

content3 = f"""<h3><strong>Elf WK's, vijf keer de derde ronde</strong></h3>
<p>Evans stond elf keer op het WK en haalde de laatste acht edities op rij. Verder dan de derde ronde kwam hij nooit, maar hij sloopte er wel vier spelers die op dat moment in de top tien stonden: James Wade, Nathan Aspinall, Simon Whitlock en Dave Chisnall.</p>
{tabel(["WK", "Tot hoever", "Uitgeschakeld door", "Bijzonderheden"], WK_HISTORIE)}
<p>Die laatste regel is het begin van dit verhaal. Op het WK van 2026 stond hij met 2-1 voor op Charlie Manby en verloor alsnog met 2-4. &bdquo;It was 11 months of pure hatred since losing to Charlie at the World Championship&rdquo;, zei hij deze week.</p>
<h3><strong>Het seizoen 2026 van Ricky Evans</strong></h3>
<p>Hij begon het jaar als nummer 40 van de wereld, precies op de WK-streep, en zakte twaalf plekken. De verklaring staat in één cijfer: van de 33 Players Championships waaraan hij meedeed, won hij er maar negen keer zijn openingswedstrijd. Eind oktober stond de teller op acht toernooien op rij waarin hij meteen verloor.</p>
{tabel(["Onderdeel", "Resultaat 2026", "Toelichting"], SEIZOEN)}
<p>Ook aan zijn prijzengeld is de terugval af te lezen.</p>
{tabel(["Jaar", "Verdiend prijzengeld"], PRIJZENGELD)}
<p>Zijn eigen diagnose, begin november: &bdquo;It's 6-5s. Too many 6-5s is the problem.&rdquo; En eerlijker nog: &bdquo;I'm not getting better. That's the thing.&rdquo; In datzelfde gesprek zei hij dat hij er niet van kon slapen en bij een paar vragen vol schoot. Zijn oplossing, in vier woorden: &bdquo;I need to go back to being fast.&rdquo;</p>
<h3><strong>&bdquo;Elf maanden pure haat&rdquo;</strong></h3>
<p>Wat dit verhaal anders maakt dan een ranglijstverhaal, is wat hij er deze week zelf over vertelde. &bdquo;I'm loving darts again at the minute, and I've had 11 months of pure hatred&rdquo;, zei hij na zijn zege op Crabtree. &bdquo;I'm going to hotels, I'm arguing with my girlfriend, and my manager.&rdquo; Over het spel zelf: &bdquo;To me, it was more like a chore than a hobby and a game. I love darts, full stop. If darts is on YouTube or whatever, I'm watching it. I wasn't enjoying any of it.&rdquo;</p>
<p>Het keerpunt kwam in het kwalificatietoernooi voor dit toernooi, tegen Cristo Reyes. &bdquo;Cristo was absolutely smashing me to bits. I was three down. I took out 161, and from then I don't think I threw a bad dart.&rdquo; Hij won dat duel met 5-3 en stond zo alsnog in Wolverhampton. Zijn reactie destijds bestond uit twee woorden: &bdquo;Stupid game.&rdquo;</p>
<p>En er is iets veranderd buiten de baan. &bdquo;I'm falling out of love with the whole aspect of travelling and living out of a suitcase. I've got something to fall back on now. I've got a girlfriend. I've got something to fight for. I want to get my own house.&rdquo; Over zijn ouders: &bdquo;I love my parents dearly. They're the best people in the world. But I don't want to be going home every time, saying: I've lost again.&rdquo;</p>
<p>Hij houdt het bijgeloof erin. Tegen Crabtree droeg hij, naar eigen zeggen, dezelfde onderbroek en sokken als in het kwalificatietoernooi. En over zijn eigen hoofd: &bdquo;I'm one of those who overthink everything. I could tell you what I did last week in the hotel, what food I ate, and what time I ordered it.&rdquo; Zijn eigen samenvatting van waar hij nu staat: &bdquo;I'm in a great place right now. I could lose a game and be an idiot again. But right now I'm loving it.&rdquo;</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Gaat Ricky Evans naar het WK Darts 2027?</strong><br>Nog niet. Hij mist de ProTour-route definitief met &pound;1.250 en staat 52e op de wereldranglijst, waarvan de top 40 doorgaat. Hij kan zich nog plaatsen via een diepe run op de Grand Slam of Darts of via de Tour Card Holder Qualifier van 30 november.</p>
<p><strong>Wat heeft Evans op de Grand Slam nodig om zich te plaatsen?</strong><br>Minimaal de kwartfinale. Groepswinst en een plek bij de laatste zestien leveren &pound;20.000 op, en daarmee komt hij nog ruim &pound;10.000 tekort voor de top 40.</p>
<p><strong>Waarom mist Ricky Evans de ProTour-route?</strong><br>Met &pound;32.000 eindigde hij ongeveer 46e op de geschoonde ProTour-ranglijst. De veertigste en laatste plek ging naar Henry Coates met &pound;33.250, een verschil van &pound;1.250.</p>
<p><strong>Wanneer weet Ricky Evans of hij naar het WK mag?</strong><br>De ranglijsten gaan op 30 november op slot, na de Players Championship Finals van 27 tot en met 29 november. De Tour Card Holder Qualifier is op diezelfde maandag 30 november, met vier WK-tickets.</p>
<p><strong>Hoe vaak stond Ricky Evans op het WK Darts?</strong><br>Elf keer, waarvan de laatste acht edities op rij. Zijn beste resultaat is de derde ronde, die hij vijf keer haalde: in 2020, 2021, 2024, 2025 en 2026.</p>
<p><strong>Op welk nummer loopt Ricky Evans op?</strong><br>Op het WK al jaren op &bdquo;Merry Christmas Everyone&rdquo; van Shakin' Stevens, in kerstshirt en met de hele zaal meezingend. Sinds de Grand Slam of Darts van 2026 gebruikt hij daarbuiten &bdquo;Daydream Believer&rdquo; van The Monkees.</p>
<p><strong>Waarom heet Ricky Evans &bdquo;Rapid&rdquo;?</strong><br>Omdat hij de snelste gooier van het circuit is: hij werkt zijn drie pijlen meestal binnen drie tot vijf seconden af. Zijn bekendste moment is een 180 in 2,16 seconden tegen Michael Smith op het WK.</p>
<p><strong>Raakt Evans zijn Tour Card kwijt?</strong><br>Nee. Hij staat 52e op de wereldranglijst en daarmee ruim binnen de top 64 die de kaart behoudt. Hij zei zelf al: &bdquo;I'm not going to lose my card this year.&rdquo;</p>
<p>Alle Nederlanders die zich al plaatsten, plus de laatste kansen van {D.L['plaisier']} en {D.L['zwaan']}, staan in hun eigen overzichten. De loting en het speelschema volgen op {D.L['hub']}; onze favorieten lees je bij {D.L['voorsp']} en het dagprogramma tijdens het toernooi bij {D.L['vandaag']}.</p>
{D.KSA}"""

KAART = {
    "eyebrow": "WK Darts 2027 &middot; kwalificatie",
    "kop": "Gaat <em>Ricky Evans</em><br>naar het WK?",
    "gap_label": "Tekort op de ProTour-lijst",
    "gap": "&pound;1.250",
    "gap_sub": "46e van 40. Die route is definitief dicht.",
    "kolom": "Zo staat Ricky Evans ervoor",
    "stand": "Stand 17 november",
    "regels": [
        ("Wereldranglijst (top 40 gaat door)", "52e", "40e: Callan Rydz, &pound;194.250"),
        ("ProTour-ranglijst (top 40 gaat door)", "46e", "40e: Henry Coates, &pound;33.250"),
        ("Nodig op de Grand Slam", "kwartfinale", "vanavond 21:45 tegen Wade"),
        ("Laatste kans", "30 november", "Tour Card Holder Qualifier, 4 tickets"),
    ],
}

if __name__ == "__main__":
    import re
    import wk_darts_kwalificatie_data as DD
    alles = content + content2 + content3
    # eigen extra controles
    assert 12500 + 164500 == 177000                        # 2e in de groep = huidige projectie
    assert 25000 + 103750 + 48250 == 177000                # seizoensopbouw klopt met de projectie
    assert 194250 - 167500 == 26750 and 33250 - 32000 == 1250
    assert 195250 - 177000 == 18250 and 33250 - 13000 == 20250
    assert len([r for r in WK_HISTORIE if "Derde ronde" in r[1]]) == 5
    assert len([r for r in WK_HISTORIE if r[1] != "Niet gekwalificeerd"]) == 11
    assert len(SCENARIO) == 6 and len(RANGLIJSTEN) == 5
    assert "2,16" in alles and "Een officieel record is het niet" in alles   # nooit als PDC-record brengen
    assert "Shakin' Stevens" in alles and "Daydream Believer" in alles
    assert "bijna 80" not in alles and "80 jaar" not in alles   # Evans noemde Stevens 80; hij is 77 - leeftijd weggelaten
    DD.check([sys.modules[__name__]])
