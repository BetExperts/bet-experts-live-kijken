# -*- coding: utf-8 -*-
"""Los artikel (cluster Grand Slam of Darts 2026): de loting – alle poules, deelnemers en de Nederlanders.
Zoekwoorden: loting grand slam of darts 2026 / poules / groepen / deelnemers / line up, grand slam of darts van gerwen,
nederlanders, poule des doods. Feiten: gsod_data.py + gsod_feiten_2026.md, sectie 'Loting 10-11' (loting ma 9 nov,
pdc.tv 09-11; NL-aantal Dartsnieuws/DartsKing; De Graaf komt uit voor Zweden).
Bijwerken na de groepsfase (16-17 nov): wie er door is, en de laatste 16.
  python3 specials/gsod_deelnemers_2026.py   (dry run)
  kaart: og_kaarten/gsod.py gsod_deelnemers_2026"""
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HIER, ".."))
sys.path.insert(0, HIER)
from legaal_data import tabel
import gsod_data as G

SLUG = G.SLUGS["deelnemers"]
RUBRIEK = G.RUBRIEK
TITEL = "Loting Grand Slam of Darts 2026: alle poules en deelnemers"
SAMENVATTING = ("Loting Grand Slam of Darts 2026: Littler treft Zonneveld en Greaves, Van Gerwen loot De Graaf. "
                "Alle 16 poules, de Nederlanders en hun kansen.")

OG_EYEBROW = "Darts · loting 9 november"
OG_KOP = "Loting<br><em>Grand Slam 2026</em>"
OG_TEGELS = [("Poules", "16 × 3"), ("Nederlanders", "7")]
OG_KOPJE = "Poules met Nederlanders · eerste duel (NL-tijd)"
OG_RECHTS = "Alleen de winnaar gaat door"
OG_RIJEN = [("Groep A", "Littler · Zonneveld · Greaves", "Zo 20:30"),
            ("Groep L", "Van Gerwen · De Graaf · Coates", "Za 20:00"),
            ("Groep M", "Van Veen · Brooks · Sneyd", "Za 20:00"),
            ("Groep H", "Nijman · Springer · Sevada", "Za 14:00")]


def naam(s):
    if s in G.NL:
        return f"{s} 🇳🇱"
    if s == G.ZWE_NL:
        return f"{s} 🇸🇪"
    return s


def spelers(g):
    seed, a, b, c = G.GROEP[g]
    vlag = naam(a)[len(a):]
    return f"<strong>{a} ({seed})</strong>{vlag}, {naam(b)}, {naam(c)}"


content = f"""<p><strong>De loting van de Grand Slam of Darts 2026 is op maandag 9 november verricht. Titelverdediger Luke Littler zit in groep A met Niels Zonneveld en Beau Greaves, Michael van Gerwen treft in groep L Jeffrey de Graaf en Henry Coates, en Gian van Veen kreeg in groep M Bradley Brooks en Carl Sneyd. Ook Wessel Nijman (groep H), Jermaine Wattimena (B), Kevin Doets (C) en Maik Kuivenhoven (P) spelen in Wolverhampton: zeven Nederlanders in totaal. Er zijn 16 poules van drie, en alleen de groepswinnaar gaat door naar de laatste 16. Bijgewerkt op dinsdag 10 november.</strong></p>
<h3><strong>Alle poules van de Grand Slam of Darts 2026</strong></h3>
{tabel(["Groep", "Spelers"], [(f"<strong>{g}</strong>", spelers(g)) for g, *_ in G.GROEPEN])}
<p><em>Vetgedrukt: de geplaatste speler, met zijn plaatsingsnummer. Daarna de speler uit pot 2 en de speler uit pot 3. 🇳🇱 = Nederlander, 🇸🇪 = Jeffrey de Graaf, die voor Zweden uitkomt.</em></p>
<h3><strong>Zo werkt de groepsfase</strong></h3>
<p>De 48 spelers zijn over 16 groepen van drie verdeeld. Elke groep bestaat uit één van de 16 hoogst geplaatste spelers op de PDC-ranking, één speler uit pot 2 (plek 17 tot en met 32 van de deelnemers) en één uit pot 3 (de rest). Iedereen speelt twee wedstrijden over best of 9 legs, een zege levert twee punten op. De PDC heeft bevestigd dat dit jaar <strong>alleen de groepswinnaar</strong> doorgaat. Tot en met 2025 gingen er nog twee spelers per groep door. Eén nederlaag kan nu al het einde betekenen.</p>
<p>Eindigen spelers gelijk op punten, dan telt eerst het legsaldo. Is dat ook gelijk, dan beslissen achtereenvolgens het aantal gewonnen legs, de legs gewonnen tegen de pijl in, het hoogste toernooigemiddelde en het hoogste gemiddelde in een gewonnen partij. Helpt dat allemaal niet, dan volgt een shoot-out om de negen pijlen.</p>
{tabel(["Speeldag", "Wie speelt er?"], [
    ("<strong>Zaterdag 14 november</strong>", "In elke groep de geplaatste speler tegen de speler uit pot 3"),
    ("<strong>Zondag 15 november</strong>", "De speler uit pot 2 tegen de verliezer van zaterdag"),
    ("<strong>Maandag 16 november</strong>", "Groepen A t/m H: de speler uit pot 2 tegen de winnaar van zaterdag"),
    ("<strong>Dinsdag 17 november</strong>", "Groepen I t/m P: de speler uit pot 2 tegen de winnaar van zaterdag"),
])}
<p>In de laatste 16 spelen de winnaars van twee naast elkaar liggende groepen tegen elkaar: A tegen B, C tegen D, enzovoort. Littler (groep A) en Luke Humphries (groep I) zitten daardoor in verschillende helften en kunnen elkaar pas in de finale treffen. Van Gerwen en Van Veen zitten wel in dezelfde helft: zij kunnen elkaar in de halve finale tegenkomen.</p>"""

content2 = f"""<h3><strong>De Nederlanders in de loting</strong></h3>
{tabel(["Speler", "Groep", "Tegenstanders", "Eerste duel (NL-tijd)"], [
    ("<strong>Gian van Veen</strong> (3)", "M", "Bradley Brooks, Carl Sneyd", "Za 14 nov, 20:00 – Sneyd"),
    ("<strong>Michael van Gerwen</strong> (10)", "L", "Jeffrey de Graaf, Henry Coates", "Za 14 nov, 20:00 – Coates"),
    ("<strong>Wessel Nijman</strong> (12)", "H", "Niko Springer, Adam Sevada", "Za 14 nov, 14:00 – Sevada"),
    ("<strong>Jermaine Wattimena</strong> (16)", "B", "Alan Soutar, Lisa Ashton", "Za 14 nov, 14:00 – Ashton"),
    ("<strong>Niels Zonneveld</strong>", "A", "Luke Littler, Beau Greaves", "Zo 15 nov, 20:30"),
    ("<strong>Kevin Doets</strong>", "C", "Josh Rock, Tommy Morris", "Zo 15 nov, 14:00"),
    ("<strong>Maik Kuivenhoven</strong>", "P", "Nathan Aspinall, Karel Sedláček", "Za 14 nov, 14:00 – Aspinall"),
])}
<p><em>Zonneveld en Doets spelen zondag tegen de verliezer van het zaterdagduel in hun groep en op maandag tegen de winnaar. Plaatsingsnummer tussen haakjes.</em></p>
<h3><strong>Gian van Veen (groep M): op papier de mooiste loting</strong></h3>
<p>De nummer 3 van de plaatsingslijst opent zaterdagavond tegen debutant Carl Sneyd, die zich via de qualifier plaatste. De lastigste horde is Bradley Brooks: hij versloeg in de laatste qualifierronde Dave Chisnall met 5-2 en een gemiddelde van ruim 106. Van Veen, dit jaar finalist op het WK en op de World Cup, is de duidelijke favoriet om de groep te winnen. In de laatste 16 wacht dan de winnaar van groep N, waarin Chris Dobey en Martin Schindler zitten.</p>
<h3><strong>Michael van Gerwen (groep L): Nederlands onderonsje met De Graaf</strong></h3>
<p>De drievoudig Grand Slam-winnaar begint zaterdagavond tegen Henry Coates. Daarna wacht Jeffrey de Graaf, die net als Coates dit jaar een Players Championship won. De Graaf is Nederlander, maar komt uit voor Zweden. Van Gerwen won vorig jaar zijn groep, onder meer met een 5-2 zege op Gary Anderson en een gemiddelde van bijna 109, en is ook nu favoriet. Een uitglijder is echter duur, want er gaat maar één speler door. De winnaar van groep L speelt in de laatste 16 tegen de winnaar van groep K (James Wade, Ricky Evans en Cam Crabtree).</p>
<h3><strong>Wessel Nijman (groep H): favoriet, maar een zware laatste 16</strong></h3>
<p>Nijman won dit jaar zes Players Championships en twee European Tour-toernooien en is als nummer 12 geplaatst. Hij opent zaterdagmiddag tegen Adam Sevada, de kampioen van Noord-Amerika, en treft daarna de Duitser Niko Springer, die via de qualifier kwam. Wint hij de groep, dan volgt woensdag de winnaar van groep G, waarin Jonny Clayton en Rob Cross zitten. Dat is een van de zwaarste paden naar de kwartfinale.</p>
<h3><strong>Jermaine Wattimena (groep B): groepswinst kan, dan wacht waarschijnlijk Littler</strong></h3>
<p>Wattimena is als nummer 16 de laagst geplaatste speler in pot 1, maar zijn loting valt mee. Hij opent zaterdagmiddag tegen Lisa Ashton en speelt daarna tegen de Schot Alan Soutar, die in de qualifier de Belg Mike De Decker uitschakelde. Wattimena is favoriet in deze groep. De keerzijde: de winnaar van groep B speelt in de laatste 16 tegen de winnaar van groep A, en dat is naar verwachting Luke Littler.</p>
<h3><strong>Niels Zonneveld (groep A): debuut in de zwaarste poule</strong></h3>
<p>Zonneveld plaatste zich met zijn zege op het {G.EXTRA['ddc']} en debuteert meteen in de groep van de titelverdediger. Zaterdagavond spelen Littler en Greaves eerst tegen elkaar. Zonneveld speelt zondagavond tegen de verliezer van dat duel en maandag tegen de winnaar. Hij is de duidelijke underdog, maar heeft één voordeel: hij weet bij zijn tweede wedstrijd precies wat hij nodig heeft.</p>
<h3><strong>Kevin Doets (groep C): open groep met een speler in vorm</strong></h3>
<p>Ook Doets maakt zijn Grand Slam-debuut. Zijn groep wordt geleid door Josh Rock (nummer 8), die dit jaar de Austrian Darts Open won. De derde speler is Tommy Morris, die op 5 november zonder Tour Card Players Championship 34 won, met in de finale een 8-5 zege op Luke Humphries. Doets speelt zondagmiddag tegen de verliezer van Rock-Morris en maandag tegen de winnaar. Het is een groep waarin alle drie de spelers kansen hebben.</p>
<h3><strong>Maik Kuivenhoven (groep P): debutant tegen Aspinall</strong></h3>
<p>Kuivenhoven was op 6 november een van de tien spelers die zich via de Tour Card Holder Qualifier in Leicester plaatsten; in de beslissende ronde won hij met 5-2 van Chris Landman. Hij opent zaterdagmiddag tegen Nathan Aspinall (nummer 11), de verliezend finalist van de Players Championship Finals van vorig jaar. Daarna volgt Karel Sedláček. Kuivenhoven is de underdog, maar in een groep van drie kan één goede wedstrijd al veel veranderen.</p>"""

content3 = f"""<h3><strong>Wat is de poule des doods?</strong></h3>
<p><strong>Groep A</strong> is de zwaarste poule voor de Nederlanders. Luke Littler is wereldkampioen, nummer 1 van de wereld en jaagt op zijn derde Grand Slam-titel op rij. Beau Greaves werd dit jaar de eerste vrouw die een PDC-rankingtoernooi won en pakte ook de Women's World Matchplay. En Niels Zonneveld won dit jaar een European Tour-toernooi. Maar één van de drie overleeft de groep.</p>
<p><strong>Groep N</strong> is de poule met de sterkste speler uit pot 2. Martin Schindler haalde dit jaar de finale van het EK, maar viel door zijn ranking buiten de top 16 van de plaatsingslijst. Hij treft Chris Dobey, die dit jaar drie Players Championships won, en jeugdfinalist Jan Schmidt. Wie hier wint, speelt in de laatste 16 waarschijnlijk tegen Gian van Veen.</p>
<p><strong>Groep G</strong> is de derde kandidaat. Jonny Clayton (nummer 5) won dit jaar de Swiss Darts Trophy, Rob Cross is oud-wereldkampioen en stond in 2023 nog in de Grand Slam-finale, en Anton Östlund kwam als kampioen van het Nordic & Baltic Championship het veld in. Twee spelers van topniveau, maar slechts één plek.</p>
<h3><strong>Alle 48 deelnemers van de Grand Slam of Darts 2026</strong></h3>
{tabel(["#", "Speler", "Groep", "Geplaatst als"], [(str(i), naam(s), G.groep_van(s), r) for i, (s, r) in enumerate(G.VELD, 1)])}
<h3><strong>Hoe zijn de laatste plekken vergeven?</strong></h3>
{tabel(["Datum", "Toernooi", "Uitkomst"], [(f"<strong>{d}</strong>", t, u) for d, t, u in G.OPEN])}
<p>Danny Noppert, vorig jaar nog halvefinalist, ging al in de eerste ronde van de qualifier onderuit. Ook Dirk van Duijvenbode en Raymond van Barneveld plaatsten zich niet. Er doet geen Belg mee: Mike De Decker en Stefaan Henderyck strandden allebei in de laatste ronde van de qualifier.</p>
<h3><strong>Meer over de Grand Slam of Darts 2026</strong></h3>
<p>Wie wanneer speelt, zie je in het {G.a('speelschema', 'speelschema van de Grand Slam of Darts 2026')}. Wat de spelers per ronde verdienen, lees je bij het {G.a('prijzengeld', 'prijzengeld')}, en hoe het toernooi in elkaar zit in ons artikel over het {G.a('format', 'nieuwe format')}. Waar je kunt kijken, staat in {G.a('tv', 'de Grand Slam of Darts live op tv')}.</p>
<p>Wedden op de Grand Slam? Speel alleen bij een bookmaker met een vergunning van de Kansspelautoriteit en lees bij twijfel {G.EXTRA['legaal']}.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wanneer was de loting van de Grand Slam of Darts 2026?</strong><br>Op maandag 9 november 2026, een dag nadat Anton Östlund het laatste ticket pakte op het Nordic & Baltic Championship.</p>
<p><strong>In welke poule zit Michael van Gerwen?</strong><br>In groep L, met Jeffrey de Graaf en Henry Coates. Hij opent zaterdag 14 november in de avondsessie tegen Coates.</p>
<p><strong>Welke Nederlanders doen mee aan de Grand Slam of Darts 2026?</strong><br>Zeven: Gian van Veen, Michael van Gerwen, Wessel Nijman, Jermaine Wattimena, Niels Zonneveld, Kevin Doets en Maik Kuivenhoven. Zonneveld, Doets en Kuivenhoven debuteren. Jeffrey de Graaf is Nederlander, maar komt uit voor Zweden.</p>
<p><strong>Hoeveel spelers gaan er per poule door?</strong><br>Eén: alleen de groepswinnaar gaat naar de laatste 16. De nummers 2 en 3 krijgen £12.500 en £5.000.</p>
<p><strong>Doet Danny Noppert mee?</strong><br>Nee. Noppert verloor in de eerste ronde van de qualifier op 6 november.</p>
<p><strong>Wie is de titelverdediger?</strong><br>Luke Littler. Hij won in 2024 en 2025 en kan als derde speler ooit drie keer op rij winnen, na Phil Taylor en Michael van Gerwen. Alle eerdere winnaars zie je in de {G.a('winnaars', 'lijst met winnaars van de Grand Slam of Darts')}.</p>
{G.SLOT}"""

if __name__ == "__main__":
    alles = G.check(sys.modules[__name__], 1500, 2600)
    # 16 poules + 48 deelnemers; elke Nederlander 2x met vlag (poule-tabel + deelnemerslijst), De Graaf 2x 🇸🇪
    assert alles.count("🇳🇱") == 2 * len(G.NL) + 1 and alles.count("🇸🇪") == 2 + 1, (alles.count("🇳🇱"), alles.count("🇸🇪"))
    assert all(f"<strong>{g}</strong>" in content for g, *_ in G.GROEPEN) and "9 november" in content
    assert "10 november" in content and "{" not in alles and all(s.split()[-1] in alles for s in G.NL)
    print("dry run ok – niets gepubliceerd")
