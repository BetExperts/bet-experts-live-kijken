# -*- coding: utf-8 -*-
"""Los artikel: ATP Shanghai wedtips dinsdag 13 oktober 2026 (tekst aangeleverd door de gebruiker, geredigeerd).
Wedtip-velden gevuld (4 velden, 4 tips + combinatie), bookmaker wedtips = 711 (zoals 11 en 12 okt).
  python3 specials/atp_shanghai_2026_10_13.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "ATP Shanghai Wedtips Dinsdag 13 Oktober: Zverev vs Bublik, Menšík vs Géa en Meer"
SLUG = "atp-shanghai-wedtips-voorspellingen-dinsdag-13-oktober-2026"
SAMENVATTING = ("Wedtips Shanghai Masters dinsdag 13 oktober: 21.5+ games De Minaur-Khachanov (1.50), Menšík wint (1.56), "
                "Bublik 9.5+ games (1.50) en een tiebreak bij Hurkacz (1.54).")
RUBRIEK_SHANGHAI = "68dd97a028b74cf1f3a2b0cb"
COMPETITIE_SHANGHAI = "68dd97842e3621da54985d13"
BOOKMAKER_711 = "66a8a87062108480763b7309"
BET365 = "https://www.bet365.nl/hub/nl-nl/open-account?affiliate=365_02599619"


def waarom(punten):
    return "<p><strong>Waarom deze tip?</strong></p><ul>" + "".join(f"<li>{p}</li>" for p in punten) + "</ul>"


content = f"""<p><strong>Op dinsdag 13 oktober begint de vierde ronde van de Rolex Shanghai Masters. De laatste zestien spelers strijden om een plek in de kwartfinale. Eerste reekshoofd Alexander Zverev speelt tegen showman Alexander Bublik, de 21-jarige Fransman Arthur Géa neemt het na zijn stunt tegen Ben Shelton op tegen Jakub Menšík, en Alex de Minaur treft Karen Khachanov. Daarnaast speelt Hubert Hurkacz, die Novak Djokovic uitschakelde, tegen Alejandro Davidovich Fokina. Hieronder lees je onze vier wedtips met analyse, en waar je de wedstrijden live kijkt.</strong></p>
<h3><strong>Wedtips dinsdag 13 oktober in het kort</strong></h3>
<ul><li>Meer dan 21.5 games in De Minaur vs Khachanov: <strong>1.50</strong></li><li>Menšík wint van Géa: <strong>1.56</strong></li><li>Bublik meer dan 9.5 games vs Zverev: <strong>1.50</strong></li><li>Meer dan 0.5 tiebreak in Hurkacz vs Davidovich Fokina: <strong>1.54</strong></li><li>Combinatie van alle vier tips: <strong>± 5.41</strong></li></ul>
<h3><strong>Live kijken en speeltijden</strong></h3>
<p>Shanghai loopt zes uur voor op Nederland. De wedstrijden van de vierde ronde worden in twee sessies gespeeld, vanaf 06:00 uur en vanaf 12:00 uur Nederlandse tijd. De exacte volgorde per baan vind je in de dagelijkse order of play van de ATP.</p>
<ul><li><strong><a href="/zenders/ziggo-sport">Ziggo Sport</a></strong>: geselecteerde wedstrijden op Ziggo Sport, Ziggo Sport 4 en Ziggo Sport 5</li><li><strong>Bet365-livestream</strong>: stort €10, kijk de wedstrijden met een streamicoon en haal je €10 daarna weer terug</li></ul>
<p>👉 <a href="{BET365}"><strong>Maak een gratis Bet365-account aan en kijk Shanghai live</strong></a></p>
<h3><strong>Alex de Minaur vs Karen Khachanov</strong></h3>
<h4>Weg naar de vierde ronde</h4>
<p>Alex de Minaur (negende reekshoofd) lijkt hersteld van de liesblessure waarmee hij een week geleden in de finale van Beijing opgaf. Na een walk-over in de tweede ronde versloeg hij in de derde ronde de Japanse sensatie Rei Sakamoto met 7-6(6), 6-4. Dat waren al 23 games. Voor de Australiër staat er veel op het spel: hij strijdt in de Race to Turin om een van de laatste plekken voor de ATP Finals.</p>
<p>Karen Khachanov (26e reekshoofd) is na zijn zware openingswedstrijd tegen Arthur Fery (drie tiebreaks, bijna 3,5 uur) steeds beter gaan spelen. In de derde ronde won hij makkelijk met 6-2, 6-4 van Adrian Mannarino, de speler die eerder Flavio Cobolli uitschakelde. Khachanov haalde dit seizoen de halve finale van de US Open.</p>
<h4>Tip: Meer dan 21.5 games @ 1.50</h4>
<p>Bij deze weddenschap moeten er in totaal minimaal 22 games worden gespeeld.</p>
{waarom(["<strong>Twee spelers van vergelijkbaar niveau.</strong> De Minaur is met zijn snelheid en verdediging de beste counterpuncher van de tour, en Khachanov heeft een harde service en zware slagen.",
         "<strong>Lange rally's en strakke sets.</strong> De Minaur geeft weinig punten weg, waardoor Khachanov zijn servicegames moet verdienen.",
         "<strong>Een driesetter haalt de lijn bijna altijd.</strong>",
         "<strong>Ook twee strakke sets zijn genoeg.</strong> 7-5, 6-4 is precies 22 games, en een tiebreak helpt nog meer."])}
<h3><strong>Jakub Menšík vs Arthur Géa</strong></h3>
<h4>Weg naar de vierde ronde</h4>
<p>Jakub Menšík (13e reekshoofd) won in de derde ronde met 6-3, 3-6, 6-2 van het 21e reekshoofd Francisco Cerúndolo. De 21-jarige Tsjech, die in 2025 de Miami Open won, heeft een van de beste services van het circuit en een explosieve forehand.</p>
<p>Arthur Géa (21) zorgde voor de stunt van het weekend. In zijn eerste Masters 1000-toernooi ooit versloeg hij eerst landgenoot Ugo Humbert (6-4, 3-6, 6-1) en daarna het derde reekshoofd Ben Shelton met 7-6(5), 7-6(3). Het was de eerste overwinning van zijn carrière op een top-10-speler.</p>
<h4>Tip: Menšík wint @ 1.56</h4>
<p>Géa speelt vol vertrouwen, maar staat voor het eerst in een vierde ronde van een Masters-toernooi. Na zo'n grote overwinning valt een jonge speler vaak een beetje terug, terwijl Menšík al ervaring heeft met grote wedstrijden en een Masters-titel op zijn naam heeft.</p>
<p>Menšík heeft een betere service, slaat harder en is op hardcourt in zijn element. We verwachten dat hij een einde maakt aan het sprookje van Géa.</p>"""

content2 = f"""<h3><strong>Alexander Zverev vs Alexander Bublik</strong></h3>
<h4>Weg naar de vierde ronde</h4>
<p>Alexander Zverev (eerste reekshoofd) heeft een uitzonderlijk seizoen, met de titels op Roland Garros en de US Open. Tegen Quentin Halys boekte hij zijn 60e overwinning van 2026, maar het ging niet makkelijk: hij won met 6-4, 6-7(8), 6-3 en liet in de tiebreak van de tweede set twee matchpoints liggen. Zverev jaagt op zijn eerste titel in Shanghai, waar hij in 2019 de finale haalde. Ook de nummer één aan het eind van het jaar is in zicht.</p>
<p>Alexander Bublik (19e reekshoofd) kwam in de derde ronde terug tegen het 16e reekshoofd Brandon Nakashima en won met 6-7(7), 6-3, 7-6(5). Eerder in het toernooi won hij al van Tomáš Macháč.</p>
<h4>Tip: Bublik meer dan 9.5 games @ 1.50</h4>
<p>Bij deze weddenschap moet Bublik zelf minimaal 10 games winnen.</p>
{waarom(["<strong>Bublik heeft een van de beste services van de tour.</strong> Zverev zal moeite hebben om hem vaak te breken.",
         "<strong>Zverev wint zelden makkelijk.</strong> Halys nam hem een set af, en ook Wu Yibing hield hem tot een tiebreak.",
         "<strong>Ook bij een nederlaag in twee sets</strong> haalt Bublik de lijn, bijvoorbeeld met 6-4, 7-6 of 7-5, 6-4.",
         "<strong>Een driesetter</strong> levert Bublik vrijwel altijd minimaal 10 games op."])}
<p>Zverev blijft de favoriet om te winnen, maar Bublik zal hem met zijn service, onderhandse opslagen en dropshots tot het uiterste dwingen.</p>
<h3><strong>Hubert Hurkacz vs Alejandro Davidovich Fokina</strong></h3>
<h4>Weg naar de vierde ronde</h4>
<p>Hubert Hurkacz zorgde voor de grootste stunt van het toernooi toen hij Novak Djokovic met 6-4, 6-3 uitschakelde. Het was zijn eerste zege op de Serviër na acht nederlagen. Hij hield al zijn tien servicegames, sloeg 13 aces en won 82% van de punten op zijn eerste service. Na de vroege opgave in Beijing met een spierblessure lijkt hij weer fit. Hurkacz won Shanghai in 2023 en heeft hier sindsdien geen wedstrijd verloren.</p>
<p>Alejandro Davidovich Fokina (25e reekshoofd) versloeg in de derde ronde het zevende reekshoofd Frances Tiafoe met 7-6(4), 4-6, 7-6(6). Hij redde een matchpoint in de beslissende tiebreak. Het was zijn eerste overwinning op een top-10-speler dit jaar. De Spanjaard is in vorm: eind september won hij in Chengdu zijn eerste titel op hardcourt, zonder één keer zijn service te verliezen.</p>
<h4>Tip: Meer dan 0.5 tiebreak @ 1.54</h4>
<p>Bij deze weddenschap moet er in de wedstrijd minimaal één tiebreak worden gespeeld.</p>
{waarom(["<strong>Hurkacz serveert enorm sterk.</strong> Hij is een van de beste serveerders ter wereld en won al zijn servicegames tegen Djokovic.",
         "<strong>Davidovich Fokina houdt zijn service ook vast.</strong> In Chengdu verloor hij de hele week geen servicegame.",
         "<strong>Beide spelers speelden in Shanghai al tiebreaks.</strong> Davidovich Fokina zelfs twee tegen Tiafoe.",
         "<strong>Het snelle hardcourt van Shanghai</strong> maakt breaks schaars."])}"""

content3 = """<h3><strong>Combinatiebet dinsdag 13 oktober</strong></h3>
<p>Alle vier tips: 1.50 × 1.56 × 1.50 × 1.54 = <strong>± 5.41</strong></p>
<p>Een inzet van €10 levert bij deze combinatie ongeveer €54 op. Wil je minder risico, kies dan voor een kleinere combinatie:</p>
<ul><li>Meer dan 21.5 games De Minaur/Khachanov + Bublik meer dan 9.5 games: <strong>± 2.25</strong></li><li>Tiebreak Hurkacz/Davidovich Fokina + Menšík wint: <strong>± 2.40</strong></li></ul>
<h3><strong>Wat staat er op het spel in de vierde ronde?</strong></h3>
<ul><li>Winnaar vierde ronde (naar de kwartfinale): $193.645 (± €166.500) en 200 ATP-punten</li><li>Verliezer vierde ronde: $105.720 (± €90.900) en 100 ATP-punten</li></ul>
<p>Voor spelers als De Minaur en Hurkacz gaat het ook om de laatste plekken voor de ATP Finals in Turijn. Elke overwinning kan het verschil maken. Alle bedragen per ronde vind je in ons overzicht van het <a href="/nieuws/prijzengeld-shanghai-masters-2026">prijzengeld van de Shanghai Masters 2026</a>.</p>
<h3><strong>Verrassingen tot nu toe in Shanghai</strong></h3>
<ul><li>Novak Djokovic werd in de tweede ronde uitgeschakeld door Hubert Hurkacz.</li><li>Ben Shelton, het derde reekshoofd, verloor van debutant Arthur Géa.</li><li>Frances Tiafoe liet tegen Davidovich Fokina een matchpoint liggen.</li><li>Andrey Rublev verloor van qualifier Rei Sakamoto.</li><li>Flavio Cobolli werd uitgeschakeld door de 38-jarige Adrian Mannarino.</li></ul>
<p>Onze wedtips van gisteren lees je in <a href="/nieuws/atp-shanghai-wedtips-voorspellingen-maandag-12-oktober-2026">ATP Shanghai wedtips maandag 12 oktober</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wanneer wordt de vierde ronde van de Shanghai Masters gespeeld?</strong><br>Op dinsdag 13 en woensdag 14 oktober 2026.</p>
<p><strong>Hoe laat beginnen de wedstrijden?</strong><br>De sessies beginnen om 06:00 uur en 12:00 uur Nederlandse tijd.</p>
<p><strong>Waar kijk ik de Shanghai Masters live?</strong><br>Via <a href="/zenders/ziggo-sport">Ziggo Sport</a> en de livestream van Bet365.</p>
<p><strong>Wat betekent Bublik meer dan 9.5 games?</strong><br>Dat Bublik zelf minimaal 10 games moet winnen, ongeacht de uitslag.</p>
<p><strong>Wat betekent meer dan 21.5 games?</strong><br>Dat er in de hele wedstrijd minimaal 22 games moeten worden gespeeld.</p>
<p><strong>Wie is Arthur Géa?</strong><br>Een 21-jarige Fransman die in zijn eerste Masters 1000-toernooi Ugo Humbert en Ben Shelton versloeg.</p>
<p><strong>Wat levert de combinatie op?</strong><br>Ongeveer 5.41 keer je inzet.</p>
<p><em>Gokken is alleen toegestaan voor personen van 18 jaar en ouder. Speel verantwoord. De genoemde odds zijn indicatief en kunnen wijzigen. Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

WEDTIPS = {
    "wedstrijd-1": "Combinatie: alle 4 wedtips",
    "wedtip-1-2": "De Minaur/Khachanov 21.5+ games + Menšík wint + Bublik 9.5+ games + tiebreak Hurkacz/Davidovich Fokina",
    "quotering-wedtip-1": "5.41",
    "wedstrijd-2": "Menšík vs Géa", "wedtip-2-2": "Menšík wint", "quotering-wedtip-2": "1.56",
    "wedstrijd-3": "De Minaur vs Khachanov", "wedtip-3-2": "Meer dan 21.5 games", "quotering-wedtip-3": "1.50",
    "wedtip-4-2": "Bublik meer dan 9.5 games (vs Zverev)", "quotering-wedtip-4": "1.50",
}

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_SHANGHAI, "competitie": COMPETITIE_SHANGHAI,
          "tennis": True, "bookmaker-wedtips": BOOKMAKER_711,
          "datum-tijd-van-wedstrijd": "2026-10-13T04:00:00.000Z",
          "publicatiedatum": datetime.now(timezone.utc).isoformat(), **WEDTIPS}
    if "--live" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting"); sys.exit()
    print("item:", WF.create_live(fd))
