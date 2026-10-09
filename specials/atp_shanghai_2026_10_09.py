# -*- coding: utf-8 -*-
"""Los artikel: ATP Shanghai wedtips vrijdag 9 oktober 2026 (tekst aangeleverd door de gebruiker).
  python3 specials/atp_shanghai_2026_10_09.py [--live]"""
import hashlib, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF
from lk_config import BASE

TITEL = "ATP Shanghai Wedtips Vrijdag 9 Oktober: Djokovic, Tiafoe, Menšík en Bublik"
SLUG = "atp-shanghai-wedtips-voorspellingen-vrijdag-9-oktober-2026"
SAMENVATTING = ("Wedtips Shanghai Masters vrijdag 9 oktober: Djokovic wint (1.48), Khachanov (1.47), "
                "Menšík -2.5 (1.50), Bublik (1.53) en Tiafoe 12.5+ games (1.58).")
RUBRIEK_SHANGHAI = "68dd97a028b74cf1f3a2b0cb"
COMPETITIE_SHANGHAI = "68dd97842e3621da54985d13"
BET365_BOOKMAKER = "651bd6728c40de720bd8072a"
BET365 = "https://www.bet365.nl/hub/nl-nl/open-account?affiliate=365_02599619"

content = f"""<p><strong>De tweede ronde van de Rolex Shanghai Masters brengt op vrijdag 9 oktober een sterk programma, met als hoogtepunt Novak Djokovic, die na zijn titel in Beijing meteen tegen Hubert Hurkacz speelt. Ook Frances Tiafoe, Karen Khachanov, Jakub Menšík en Alexander Bublik spelen vandaag. Hieronder lees je onze voorspellingen, de vorm van de spelers en waar je de wedstrijden live kijkt.</strong></p>
<h3><strong>Wedtips vrijdag 9 oktober in het kort</strong></h3>
<ul><li>Tiafoe meer dan 12.5 games vs Hanfmann: <strong>1.58</strong></li><li>Khachanov wint van Fery: <strong>1.47</strong></li><li>Menšík -2.5 game handicap vs Kecmanović: <strong>1.50</strong></li><li>Bublik wint van Macháč: <strong>1.53</strong></li><li>Djokovic wint van Hurkacz: <strong>1.48</strong></li><li>Combinatie van alle vijf tips: <strong>± 7.89</strong></li></ul>
<h3><strong>Live kijken en speeltijden</strong></h3>
<p>De wedstrijden in Shanghai zijn in twee sessies verdeeld: de eerste begint om 06:00 uur en de tweede om 12:00 uur Nederlandse tijd. De exacte volgorde per baan wordt dagelijks door de ATP bekendgemaakt.</p>
<ul><li><strong><a href="/zenders/ziggo-sport">Ziggo Sport</a></strong>: geselecteerde wedstrijden op Ziggo Sport, Ziggo Sport 4 en Ziggo Sport 5</li><li><strong>Bet365-livestream</strong>: stort €10, kijk de wedstrijden met een streamicoon en haal je €10 daarna weer terug</li></ul>
<p>👉 <a href="{BET365}"><strong>Maak een gratis Bet365-account aan en kijk Shanghai live</strong></a></p>"""

content2 = """<h3><strong>Frances Tiafoe vs Yannick Hanfmann</strong></h3>
<h4>Vorm en achtergrond</h4>
<p>Frances Tiafoe had een sterke zomer. Hij haalde de halve finale van de US Open, waar hij in een volledig Amerikaans duel van Ben Shelton verloor. In Tokio werd hij in de tweede ronde uitgeschakeld door Arthur Fils, de latere halvefinalist.</p>
<p>Yannick Hanfmann (34) is een ervaren Duitser rond de 54e plaats op de wereldranglijst. Dit jaar haalde hij de finale van het toernooi in Chili, waarin hij onderweg het eerste reekshoofd Francisco Cerúndolo versloeg. Shanghai ligt hem goed: vorig jaar kwam hij als qualifier tot de derde ronde, waarin hij verloor van Djokovic.</p>
<h4>Tip: Tiafoe meer dan 12.5 games @ 1.58</h4>
<p>Bij deze weddenschap moet Tiafoe zelf minimaal 13 games winnen. We verwachten een lange wedstrijd. Hanfmann is een taaie speler van de baseline die niet snel wegvalt, en Tiafoe kent altijd wisselende momenten.</p>
<p><strong>Zo dek je de 12.5 games:</strong></p>
<ul><li>Bij een driesetter haalt Tiafoe dit bijna altijd, ook als hij verliest.</li><li>Bij een winst in twee sets volstaat bijvoorbeeld 7-5, 6-4 of 7-6, 6-4.</li><li>Alleen bij een eenvoudige zege (6-3, 6-4) of een snelle nederlaag gaat het mis.</li></ul>
<h3><strong>Karen Khachanov vs Arthur Fery</strong></h3>
<h4>Vorm en achtergrond</h4>
<p>Karen Khachanov is een van de best presterende spelers van de afgelopen maanden. De Rus haalde de halve finale van de US Open, waar hij verloor van de latere winnaar Alexander Zverev. In Beijing bereikte hij de kwartfinale, waar hij verloor van Hurkacz.</p>
<p>Arthur Fery is een jonge Brit die dit seizoen een sprong heeft gemaakt. Hij heeft talent, maar mist nog ervaring op Masters-niveau tegen spelers uit de top 20.</p>
<h4>Tip: Khachanov wint @ 1.47</h4>
<p>Khachanov is fysiek sterk, serveert hard en is solide vanaf de baseline. Op hardcourt is hij in zijn element. Het niveauverschil met Fery is te groot, en we verwachten dat de Rus deze wedstrijd degelijk uitspeelt.</p>
<h3><strong>Jakub Menšík vs Miomir Kecmanović</strong></h3>
<h4>Vorm en achtergrond</h4>
<p>Jakub Menšík is een van de grootste talenten op de ATP Tour. De lange Tsjech brak definitief door in 2025 met de titel op de Miami Open, waarin hij in de finale Novak Djokovic versloeg. Hij heeft een van de beste services van het circuit en een explosieve forehand.</p>
<p>Miomir Kecmanović is een solide Serviër die op hardcourt altijd moeilijk te verslaan is. Hij heeft echter geen wapen dat Menšík echt pijn kan doen, en tegen grote serveerders heeft hij vaak moeite.</p>
<h4>Tip: Menšík -2.5 game handicap @ 1.50</h4>
<p>Menšík moet met minimaal drie games verschil winnen. Met zijn service krijgt Kecmanović weinig kansen op een break. Breekt Menšík één keer per set, dan wint hij met 6-4, 6-4 en dekt hij de handicap. Ook een driesetter met een duidelijke derde set is genoeg.</p>
<h3><strong>Alexander Bublik vs Tomáš Macháč</strong></h3>
<h4>Vorm en achtergrond</h4>
<p>Alexander Bublik is de entertainer van de tour. De Kazach heeft een enorme service, slaat onverwacht onderhandse opslagen en drop shots, en speelt met veel risico. Op snelle hardcourts is hij op zijn gevaarlijkst. Dit seizoen speelde hij voor Team World op de Laver Cup.</p>
<p>Tomáš Macháč heeft goede herinneringen aan Shanghai. In 2024 versloeg hij hier Carlos Alcaraz en bereikte hij de halve finale tegen Jannik Sinner. De Tsjech is snel en speelt agressief, maar zijn vorm schommelt.</p>
<h4>Tip: Bublik wint @ 1.53</h4>
<p>De service van Bublik is in Shanghai een groot wapen. Macháč zal moeite hebben om breakkansen te creëren, en in de belangrijke momenten verwachten we dat Bublik de doorslag geeft. Er zit risico in, want Bublik is onvoorspelbaar, maar bij 1.53 vinden we dit een goede keuze.</p>
<h3><strong>Novak Djokovic vs Hubert Hurkacz</strong></h3>
<h4>Vorm en achtergrond</h4>
<p>Novak Djokovic komt naar Shanghai als kersverse winnaar van Beijing. De Minaur gaf in de finale op met een liesblessure, nadat Djokovic de eerste set in de tiebreak had gewonnen. Het was zijn eerste titel in bijna een jaar en zijn zevende in Beijing, waarmee hij er nog altijd ongeslagen is. Het was de 102e titel van zijn carrière, waarmee hij nog maar één achter Roger Federer staat. In Shanghai is hij met vier titels recordhouder.</p>
<p>Hubert Hurkacz won de Shanghai Masters in 2023. Hij had een sterke Aziatische swing, met de halve finale in Beijing en winst in zeven van zijn laatste negen wedstrijden. Er is wel een groot vraagteken: in de halve finale van Beijing gaf hij op met een blessure aan zijn adductor bij een achterstand van 6-4, 3-2.</p>
<h4>Tip: Djokovic wint @ 1.48</h4>
<p>Hurkacz serveert enorm, maar Djokovic is de beste returner ter wereld en heeft nog nooit van de Pool verloren. Na de blessure in Beijing is het bovendien de vraag of Hurkacz voluit kan gaan. Djokovic speelt vol vertrouwen na zijn titel en wil in Shanghai nog meer punten pakken in de race naar Turijn.</p>
<p><strong>Let op:</strong> de 39-jarige Djokovic gaf zelf aan dat het een zwaar jaar is geweest met fysieke problemen. Toch zien we hem deze wedstrijd winnen.</p>"""

content3 = f"""<h3><strong>Combinatiebet vrijdag 9 oktober</strong></h3>
<p>Alle vijf tips: 1.58 × 1.47 × 1.50 × 1.53 × 1.48 = <strong>± 7.89</strong></p>
<p>Een inzet van €10 levert bij deze combinatie ongeveer €78,90 op. Wil je minder risico, kies dan voor een kleinere combinatie, bijvoorbeeld:</p>
<ul><li>Khachanov + Djokovic: <strong>± 2.18</strong></li><li>Khachanov + Djokovic + Menšík: <strong>± 3.26</strong></li></ul>
<p>👉 <a href="{BET365}"><strong>Bekijk de odds op de Shanghai Masters bij Bet365</strong></a></p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat beginnen de wedstrijden in Shanghai?</strong><br>De eerste sessie begint om 06:00 uur en de tweede om 12:00 uur Nederlandse tijd.</p>
<p><strong>Waar kijk ik de Shanghai Masters live?</strong><br>Via Ziggo Sport en de livestream van <a href="/zenders/bet365">Bet365</a>.</p>
<p><strong>Wat betekent Tiafoe meer dan 12.5 games?</strong><br>Dat Tiafoe zelf minimaal 13 games in de wedstrijd moet winnen, ongeacht de uitslag.</p>
<p><strong>Wat betekent Menšík -2.5 game handicap?</strong><br>Dat Menšík met minimaal drie games verschil moet winnen, bijvoorbeeld met 6-4, 6-4.</p>
<p><strong>Hoe vaak won Djokovic de Shanghai Masters?</strong><br>Vier keer. Hij is recordhouder van het toernooi.</p>
<p><strong>Wat levert de combinatie op?</strong><br>Ongeveer 7.89 keer je inzet.</p>
<p><em>Gokken is alleen toegestaan voor personen van 18 jaar en ouder. Speel verantwoord. Stop op tijd. De genoemde odds zijn indicatief en kunnen wijzigen. Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_SHANGHAI, "competitie": COMPETITIE_SHANGHAI,
          "tennis": True, "bookmaker-wedtips": BET365_BOOKMAKER,
          "datum-tijd-van-wedstrijd": "2026-10-09T04:00:00.000Z",
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting"); sys.exit()
    print("item:", WF.create_live(fd))
