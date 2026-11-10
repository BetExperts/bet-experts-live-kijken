# -*- coding: utf-8 -*-
"""Los artikel (cluster Grand Slam of Darts 2026, centrale pagina): speelschema, programma en tijden.
Zoekwoorden (Google-suggesties NL + GSC 2025): grand slam of darts speelschema / programma (vandaag, vanavond) / tijden /
finale tijd / wanneer begint. Feiten: gsod_data.py (sessietijden en programma za 14 nov: pdc.tv 09-11-2026 + ticketverkoop).
Bijgewerkt 10-11-2026 na de loting. Nog bijwerken: volgorde zo 15 t/m di 17 nov zodra de PDC die publiceert (na de uitslagen).
  python3 specials/gsod_speelschema_2026.py   (dry run)
  kaart: og_kaarten/gsod.py gsod_speelschema_2026, publiceren: specials/concept_publiceer.py gsod_speelschema_2026 --live"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel
import gsod_data as G

SLUG = G.SLUGS["speelschema"]
RUBRIEK = G.RUBRIEK
TITEL = "Speelschema Grand Slam of Darts 2026: programma en tijden"
SAMENVATTING = ("Speelschema Grand Slam of Darts 2026: alle 12 sessies in Nederlandse tijd en het programma van de "
                "openingsdag, van Littler-Greaves tot de finale.")

OG_EYEBROW = "Darts · 14-22 november 2026"
OG_KOP = "Speelschema<br><em>Grand Slam 2026</em>"
OG_TEGELS = [("Start", "Za 14 nov"), ("Finale", "Zo 22 nov")]
OG_KOPJE = "Programma (Nederlandse tijd)"
OG_RECHTS = "Loting 9 nov · 12 sessies"
OG_RIJEN = [("Za 14 · 14:00", "Nijman · Wattimena · Kuivenhoven", "8 duels"),
            ("Za 14 · 20:00", "Littler-Greaves · Van Gerwen · Van Veen", "8 duels"),
            ("Wo 18 – za 21", "Laatste 16 en kwartfinales", "20:00"),
            ("Zondag 22 nov", "Halve finales 14:00 · finale", "20:30")]

def naam(s):
    return f"<strong>{s}</strong> 🇳🇱" if s in G.NL else s


def duel(g):
    seed, a, b, c = G.GROEP[g]
    return f"{naam(a)} ({seed}) – {naam(c)}"


content = f"""<p><strong>De Grand Slam of Darts 2026 wordt van zaterdag 14 tot en met zondag 22 november gespeeld in WV Active Aldersley in Wolverhampton. Voor het eerst doen er 48 spelers mee, verdeeld over 16 groepen van drie. Het toernooi telt 12 sessies: de eerste pijlen vliegen op zaterdag 14 november om 14:00 uur Nederlandse tijd, de finale is op zondag 22 november in de avondsessie vanaf 20:30 uur. De loting is bekend: de openingssessie begint met Luke Woodhouse tegen Tom Sykes, titelverdediger Luke Littler speelt zaterdagavond tegen Beau Greaves. Hieronder vind je het volledige speelschema met alle dagen, tijden en rondes. Bijgewerkt op dinsdag 10 november.</strong></p>
<h3><strong>Grand Slam of Darts 2026 in het kort</strong></h3>
{tabel(["", ""], [
    ("<strong>Toernooi</strong>", "Mr Vegas Grand Slam of Darts 2026 (20e editie)"),
    ("<strong>Datum</strong>", "Zaterdag 14 t/m zondag 22 november 2026"),
    ("<strong>Locatie</strong>", "WV Active Aldersley, Wolverhampton (Engeland)"),
    ("<strong>Deelnemers</strong>", "48 spelers in 16 groepen van drie"),
    ("<strong>Sessies</strong>", "12, verdeeld over negen speeldagen"),
    ("<strong>Prijzengeld</strong>", f"£1.000.000, waarvan £200.000 voor de winnaar"),
    ("<strong>Titelverdediger</strong>", "Luke Littler (won in 2024 en 2025)"),
    ("<strong>Tv in Nederland</strong>", "Viaplay, een deel van de sessies gratis op Viaplay TV"),
])}
<h3><strong>Speelschema Grand Slam of Darts 2026 (Nederlandse tijd)</strong></h3>
{tabel(["Dag", "Aanvang (NL)", "Ronde", "Wedstrijden"], [
    (f"<strong>{d} {dt}</strong>", nl, r, n) for d, dt, nl, uk, r, n in G.SESSIES
])}
<p><em>De tijden zijn de aanvangstijden van de sessies volgens de officiële ticketverkoop van de PDC. In Engeland is het een uur vroeger: de middagsessies beginnen daar om 13:00 uur, de avondsessies om 19:00 of 19:30 uur. Indeling en tijden volgens het programma dat de PDC na de loting publiceerde.</em></p>"""

content2 = f"""<h3><strong>Programma zaterdag 14 november: de openingsdag</strong></h3>
<p>Op de openingsdag speelt in elke groep de geplaatste speler tegen de speler uit pot 3. De PDC heeft de volgorde al bekendgemaakt. Wessel Nijman, Jermaine Wattimena en Maik Kuivenhoven spelen 's middags, Michael van Gerwen en Gian van Veen 's avonds.</p>
<p><strong>Middagsessie, 14:00 uur</strong></p>
{tabel(["#", "Groep", "Wedstrijd"], [(str(i), g, duel(g)) for i, g in enumerate(G.ZA_MIDDAG, 1)])}
<p><strong>Avondsessie, 20:00 uur</strong></p>
{tabel(["#", "Groep", "Wedstrijd"], [(str(i), g, duel(g)) for i, g in enumerate(G.ZA_AVOND, 1)])}
<h3><strong>Programma zondag 15 tot en met dinsdag 17 november</strong></h3>
<p>Vanaf zondag hangt het programma af van de uitslagen van zaterdag. Wel staat al vast wie in welke sessie speelt:</p>
{tabel(["Sessie (NL-tijd)", "Wie speelt er?", "Groepen"], [
    ("<strong>Zondag 14:00</strong>", "De speler uit pot 2 tegen de verliezer van zaterdagmiddag", ", ".join(G.ZA_MIDDAG)),
    ("<strong>Zondag 20:30</strong>", "De speler uit pot 2 tegen de verliezer van zaterdagavond", ", ".join(G.ZA_AVOND)),
    ("<strong>Maandag 20:00</strong>", "De speler uit pot 2 tegen de winnaar van zaterdag", "A t/m H"),
    ("<strong>Dinsdag 20:00</strong>", "De speler uit pot 2 tegen de winnaar van zaterdag", "I t/m P"),
])}
<p>Zo speelt Niels Zonneveld zondagavond tegen de verliezer van Littler-Greaves en maandag tegen de winnaar. Kevin Doets speelt zondagmiddag tegen de verliezer van Josh Rock-Tommy Morris. De exacte volgorde binnen deze sessies maakt de PDC na de uitslagen van zaterdag bekend. Alle poules en de kansen van de Nederlanders lees je in ons artikel over de {G.a('deelnemers', 'loting van de Grand Slam of Darts 2026')}.</p>
<h3><strong>Laatste 16: wie kan tegen wie?</strong></h3>
{tabel(["Dag", "Wedstrijden (winnaars van de groepen)"], [(f"<strong>{d}</strong>", " · ".join(f"{p[0]} tegen {p[1]}" for p in paren)) for d, paren in G.L16])}
<p>In de kwartfinales spelen op vrijdag de winnaars van A/B tegen C/D en van E/F tegen G/H, op zaterdag die van I/J tegen K/L en van M/N tegen O/P. Littler en Humphries zitten in verschillende helften. Van Gerwen en Van Veen zitten in dezelfde helft en kunnen elkaar in de halve finale treffen.</p>
<h3><strong>Zo verloopt het toernooi, dag voor dag</strong></h3>
<p><strong>Zaterdag 14 en zondag 15 november: groepsfase.</strong> Het openingsweekend telt vier sessies met elk acht groepswedstrijden over best of 9 legs. In een groep van drie speelt iedere speler twee wedstrijden. Na zaterdag heeft elke groep één wedstrijd gespeeld, na zondag twee.</p>
<p><strong>Maandag 16 en dinsdag 17 november: de beslissing in de groepen.</strong> Op maandagavond worden de laatste duels van de groepen A tot en met H gespeeld, op dinsdagavond die van de groepen I tot en met P. Alleen de groepswinnaar gaat door naar de laatste 16. Eén nederlaag kan dus al fataal zijn. Bij een gelijke stand telt eerst het legsaldo.</p>
<p><strong>Woensdag 18 en donderdag 19 november: laatste 16.</strong> Elke avond staan er vier wedstrijden op het programma. Er wordt, net als vorig jaar, over best of 19 legs gespeeld.</p>
<p><strong>Vrijdag 20 en zaterdag 21 november: kwartfinales.</strong> Twee kwartfinales per avond, over best of 31 legs. Dat zijn de langste wedstrijden van de week, op de halve finales en de finale na.</p>
<p><strong>Zondag 22 november: finaledag.</strong> In de middagsessie (14:00 uur) worden de twee halve finales gespeeld, in de avondsessie (20:30 uur) de finale om de Eric Bristow Trophy en £200.000.</p>
<h3><strong>Hoe laat begint de finale van de Grand Slam of Darts 2026?</strong></h3>
<p>De avondsessie met de finale begint op zondag 22 november om 20:30 uur Nederlandse tijd (19:30 uur in Engeland). De finale is de enige wedstrijd van die sessie. Een finale over best of 31 legs duurt meestal anderhalf tot twee uur, inclusief de opkomst: de finale van vorig jaar, die Luke Littler met 16-11 won van Luke Humphries, duurde zonder opkomst bijna anderhalf uur. Reken dus op een winnaar tussen ongeveer 22:00 en 22:30 uur.</p>
<h3><strong>Het nieuwe format in het kort</strong></h3>
{tabel(["Ronde", "Spelers", "Best of", "Dagen"], [
    ("<strong>Groepsfase</strong>", "48 (16 groepen van 3)", "9 legs", "14-17 november"),
    ("<strong>Laatste 16</strong>", "16 groepswinnaars", "19 legs", "18-19 november"),
    ("<strong>Kwartfinales</strong>", "8", "31 legs", "20-21 november"),
    ("<strong>Halve finales</strong>", "4", "31 legs", "22 november (middag)"),
    ("<strong>Finale</strong>", "2", "31 legs", "22 november (avond)"),
])}
<p>Waarom zijn het dit jaar groepen van drie en wat betekent dat voor de favorieten? Dat lees je in ons artikel over het {G.a('format', 'nieuwe format van de Grand Slam of Darts 2026')}.</p>"""

content3 = f"""<h3><strong>Waar kijk je de Grand Slam of Darts 2026 live?</strong></h3>
<p>In Nederland heeft {G.EXTRA['viaplay']} de rechten op de PDC-toernooien, dus ook op de Grand Slam of Darts. Een deel van de sessies is gratis te zien op Viaplay TV; welke dat zijn, maakt Viaplay vlak voor het toernooi bekend. De beslissende wedstrijden zitten meestal achter de betaalmuur. De eerste speeldagen (14, 15 en 16 november) staan ook in de livestream van Bet365. In België zendt VTM traditioneel de grote PDC-toernooien gratis uit. Alle opties lees je in ons artikel over {G.a('tv', 'de Grand Slam of Darts live kijken op tv en via een stream')}.</p>
<h3><strong>Meer over de Grand Slam of Darts 2026</strong></h3>
<p>Wie zitten er in welke poule? Lees het in {G.a('deelnemers', 'de loting en alle poules')}. Wat verdienen de spelers per ronde? Dat staat in ons artikel over het {G.a('prijzengeld', 'prijzengeld van de Grand Slam of Darts 2026')}: de winnaar krijgt £200.000, £50.000 meer dan vorig jaar. En wie wonnen het toernooi eerder? Bekijk de {G.a('winnaars', 'lijst met alle winnaars van de Grand Slam of Darts')}: Phil Taylor is met zes titels de recordhouder, Michael van Gerwen won drie keer. Nieuw in het darten? Lees eerst {G.EXTRA['regels']}.</p>
<p>Wedden op de Grand Slam? Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit. Twijfel je, lees dan {G.EXTRA['legaal']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wanneer begint de Grand Slam of Darts 2026?</strong><br>Op zaterdag 14 november 2026. De eerste sessie begint om 14:00 uur Nederlandse tijd, de tweede om 20:00 uur.</p>
<p><strong>Hoe laat begint de finale van de Grand Slam of Darts 2026?</strong><br>Op zondag 22 november. De avondsessie met de finale begint om 20:30 uur Nederlandse tijd. De halve finales zijn dezelfde dag vanaf 14:00 uur.</p>
<p><strong>Waar wordt de Grand Slam of Darts 2026 gespeeld?</strong><br>In WV Active Aldersley in Wolverhampton, waar het toernooi sinds 2018 wordt gehouden (met uitzondering van 2020).</p>
<p><strong>Hoeveel spelers doen er mee aan de Grand Slam of Darts 2026?</strong><br>48, voor het eerst. Ze spelen in 16 groepen van drie; alleen de groepswinnaars gaan door naar de laatste 16.</p>
<p><strong>Wie speelt de eerste wedstrijd van de Grand Slam of Darts 2026?</strong><br>Luke Woodhouse en Tom Sykes (groep J) openen het toernooi op zaterdag 14 november in de middagsessie, die om 14:00 uur Nederlandse tijd begint.</p>
<p><strong>Wanneer spelen Van Gerwen en Van Veen?</strong><br>Allebei op zaterdagavond 14 november, in de sessie vanaf 20:00 uur: Van Gerwen tegen Henry Coates, Van Veen tegen Carl Sneyd. Hun tweede groepsduel volgt op zondagavond of dinsdagavond, afhankelijk van de uitslag van zaterdag.</p>
{G.SLOT}"""

if __name__ == "__main__":
    alles = G.check(sys.modules[__name__], 900)
    assert "20:30" in content and "14:00" in content and alles.count("<table") == 7, alles.count("<table")
    assert "{" not in alles and "10 november" in content and "Woodhouse" in content2 and "Littler tegen Beau Greaves" not in content2
    print("dry run ok – niets gepubliceerd")
