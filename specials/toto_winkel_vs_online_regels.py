# -*- coding: utf-8 -*-
"""Los artikel: TOTO Winkel vs TOTO online — regels bij spelerweddenschappen, voetbal en tennis.
Bronnen: 'Nadere regels per sport' TOTO Winkel (geldig vanaf 8 mrt 2024) en TOTO Sportweddenschappen online
(geldig vanaf 24 dec 2024), plus de wijziging online per 28 apr 2026 (spelerweddenschappen ook geldig bij invallen).
  python3 specials/toto_winkel_vs_online_regels.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF
from lk_config import PROVIDERS

TITEL = "TOTO Winkel of TOTO online: zo verschillen de regels bij spelers, voetbal en tennis"
SLUG = "toto-winkel-vs-toto-online-regels"
SAMENVATTING = ("Wanneer wordt je TOTO-weddenschap ongeldig als een speler niet start, invalt of een tennisser opgeeft? "
                "De regels van TOTO Winkel en online naast elkaar.")
RUBRIEK_SPELUITLEG = "6502b66cd9992658b4037cf5"
TOTO = PROVIDERS["toto"]["link"]
N = "/nieuws/"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in koppen)
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}><thead><tr>{kop}</tr></thead><tbody>{body}</tbody></table>"


content = f"""<p><strong>TOTO Winkel en TOTO online hanteren grotendeels dezelfde regels, maar bij spelerweddenschappen op voetbal zit een belangrijk verschil. Online telt een weddenschap op schoten, schoten op doel of assists sinds 28 april 2026 ook als de speler invalt. In de TOTO Winkel moet de speler volgens het reglement nog altijd in de basis starten, anders wordt de weddenschap ongeldig en krijg je je inzet terug. Bij tennis zijn de regels gelijk: geeft een speler op, dan krijg je bij een weddenschap op de winnaar je inzet terug.</strong></p>
<p>TOTO is in Nederland op twee manieren te spelen. Online, via de website of app van TOTO, met een eigen account. En in de TOTO Winkel: je stelt je weddenschap samen in de app of op de website, krijgt een QR-code en rekent af bij een verkooppunt, zoals een supermarkt, tankstation of tabakszaak. Voor beide kanalen geldt een eigen reglement met "nadere regels per sport". Die lijken sterk op elkaar, maar zijn niet identiek. Hieronder lees je wanneer een weddenschap ongeldig (void) wordt en waar de verschillen zitten.</p>
<h3><strong>Het belangrijkste verschil in één tabel</strong></h3>
{tabel(["Situatie", "TOTO Winkel", "TOTO online"], [
    ("Schoten, schoten op doel of assists: speler start in de basis", "Geldig", "Geldig"),
    ("Schoten, schoten op doel of assists: speler valt in", "<strong>Ongeldig</strong> (inzet terug)", "<strong>Geldig</strong> (sinds 28 april 2026)"),
    ("Doelpuntenmaker: speler valt in", "Geldig", "Geldig"),
    ("Speler komt helemaal niet in actie", "Ongeldig", "Ongeldig"),
    ("Speler valt in, maar het resultaat is niet meer haalbaar", "Ongeldig", "Ongeldig"),
    ("Tennis: speler geeft op tijdens de partij", "Winnaar ongeldig, afgeronde sets tellen", "Winnaar ongeldig, afgeronde sets tellen"),
    ("Tennis: walk-over", "Alles ongeldig", "Alles ongeldig"),
    ("Live wedden", "Niet mogelijk", "Wel mogelijk"),
])}
<p><em>Gebaseerd op de reglementen van TOTO Winkel (geldig vanaf 8 maart 2024) en TOTO online (geldig vanaf 24 december 2024), aangevuld met de aanpassing die TOTO online per 28 april 2026 doorvoerde. Reglementen kunnen wijzigen; controleer bij twijfel altijd de actuele versie bij TOTO.</em></p>"""

content2 = f"""<h3><strong>Voetbal: spelerweddenschappen in de winkel</strong></h3>
<p>Bij spelerweddenschappen voorspel je wat een individuele speler doet: scoort hij, geeft hij een assist, hoeveel keer schiet hij op doel. Het reglement van TOTO Winkel maakt daarbij onderscheid tussen twee groepen.</p>
<ul><li><strong>Schoten, schoten op doel en assists:</strong> de speler moet in de basis starten. Begint hij op de bank, dan wordt de weddenschap ongeldig verklaard, ook als hij later invalt en de gevraagde actie alsnog maakt.</li><li><strong>Alle andere spelerweddenschappen</strong>, zoals doelpuntenmaker, kopgoal of scoren van buiten de zestien: de weddenschap is geldig als de speler de kans heeft gehad om het resultaat te halen, hoe kort hij ook speelde.</li></ul>
<p>Een voorbeeld: je zet in de winkel in op "Ruben van Bommel geeft een assist" en hij valt na rust in. Geeft hij daarna een assist, dan krijg je toch alleen je inzet terug. Zet je in op "Van Bommel scoort" en hij scoort als invaller, dan wint je weddenschap wel.</p>
<h3><strong>Voetbal: spelerweddenschappen online</strong></h3>
<p>Online gold lange tijd dezelfde basisregel voor schoten en assists. Op 28 april 2026 paste TOTO dat aan, met het oog op het WK. Sindsdien maakt het online niet meer uit of een speler start of invalt: staat hij ook maar even op het veld, dan blijft de weddenschap staan. Dat betekent ook dat Bet Builders minder vaak ongeldig worden, omdat één invaller niet meer de hele combinatie laat vervallen. Voor TOTO Winkel is zo'n wijziging niet aangekondigd; daar geldt volgens het reglement nog de basisregel.</p>
<p>Let op: invallen betekent niet automatisch dat je weddenschap telt. Voor beide kanalen geldt dat een weddenschap ongeldig wordt als de speler het gevraagde resultaat bij zijn invalbeurt niet meer kon halen. Wie inzet op "Ronaldo scoort in de eerste tien minuten" en hem na rust ziet invallen, krijgt zijn inzet terug.</p>
<h3><strong>Regels die in de winkel en online hetzelfde zijn</strong></h3>
<ul><li><strong>Reguliere speeltijd:</strong> TOTO kijkt bij voetbal naar de reguliere speeltijd inclusief blessuretijd. Verlengingen en strafschoppen tellen niet mee, behalve bij weddenschappen op wie zich plaatst of de beker wint.</li><li><strong>Eigen doelpunten:</strong> die tellen niet mee voor weddenschappen op doelpuntenmakers. Is een eigen doelpunt het enige doelpunt van de wedstrijd, dan wint "geen doelpuntenmaker". Bij "beide teams scoren" en de clean sheet tellen eigen doelpunten wel mee.</li><li><strong>Speler doet niet mee:</strong> komt de speler helemaal niet in actie, dan is de weddenschap altijd ongeldig en krijg je je inzet terug.</li><li><strong>Afgelast of gestaakt:</strong> wordt een wedstrijd afgelast, of gestaakt voordat er 80 minuten gespeeld zijn, en niet binnen twee dagen alsnog gespeeld? Dan tellen alleen de weddenschappen waarvan de uitkomst al vaststond. De rest wordt ongeldig. Wordt er gestaakt na minstens 80 minuten, dan geldt de stand op dat moment.</li><li><strong>Bet Builder:</strong> wordt één onderdeel van je Bet Builder ongeldig, dan vervalt de hele Bet Builder en krijg je je inzet terug.</li></ul>"""

content3 = f"""<h3><strong>Tennis: opgave, walk-over en gestaakte partijen</strong></h3>
<p>Bij tennis zijn de regels in de winkel en online gelijk. Het uitgangspunt is: wat al beslist is, wordt uitbetaald; wat nog open stond, wordt ongeldig.</p>
{tabel(["Situatie", "Gevolg voor je weddenschap"], [
    ("Walk-over: de partij begint niet", "Alle weddenschappen op de partij zijn ongeldig, je krijgt je inzet terug"),
    ("Speler geeft op tijdens de partij", "Weddenschap op de winnaar ongeldig; markten die al beslist waren (bv. winnaar eerste set) worden uitbetaald"),
    ("Partij wordt gestaakt en niet binnen het toernooi uitgespeeld", "Beslist = uitbetaald, de rest ongeldig"),
    ("Partij wordt verplaatst, of ander baanoppervlak / binnen-buiten", "Alle weddenschappen blijven geldig"),
    ("Strafpunt door de scheidsrechter", "Weddenschappen op die game blijven geldig"),
    ("Tiebreak of match-tiebreak", "Telt als één game; een match-tiebreak in een best of 3 geldt als derde set"),
])}
<p>Een voorbeeld: je wedt op Djokovic als winnaar van de partij én op Djokovic als winnaar van de eerste set. Hij wint de eerste set en geeft daarna op. Je setweddenschap wint, de weddenschap op de partij wordt ongeldig. Dat is strenger voor de speler dan bij sommige andere bookmakers, waar de winnaar al geldig is zodra er één set is gespeeld. Meer daarover lees je in ons overzicht van <a href="{N}dit-zijn-de-regels-wanneer-een-speler-opgeeft-bij-tennis---zo-werken-de-regels-per-bookmaker">de regels bij opgave per bookmaker</a> en in ons artikel over <a href="{N}wat-gebeurd-er-bij-een-walkover-met-een-tennisweddenschap">een walk-over bij tennis</a>.</p>
<p>Online kent TOTO bij tennis nog een paar extra regels, omdat daar meer markten zijn, zoals aantal aces of breaks en Bet Builders op tennis. Geeft een speler op, dan worden spelerweddenschappen die al beslist waren gewoon afgehandeld. Had je meer dan vijf aces en zat hij op zes voordat hij opgaf, dan win je. Stond hij nog op drie, dan wordt de weddenschap ongeldig.</p>
<h3><strong>Andere verschillen tussen de winkel en online</strong></h3>
<ul><li><strong>Live wedden:</strong> kan alleen online. In de winkel zet je in voordat de wedstrijd begint.</li><li><strong>Bonussen:</strong> acties zoals boosts, free bets en welkomstbonussen zijn gericht op online spelen; in de winkel speel je zonder bonus.</li><li><strong>Betalen en uitbetalen:</strong> in de winkel betaal je aan de kassa en is je weddenschap pas geplaatst als je een deelnamebewijs hebt. Bewaar dat goed: je hebt het nodig om je winst te laten uitbetalen. Online komt je winst direct op je saldo.</li><li><strong>Aanbod:</strong> online is het aanbod aan wedstrijden en markten groter dan in de winkel.</li></ul>
<h3><strong>Welke kies je?</strong></h3>
<p>Wed je graag op spelers, zoals schoten op doel of assists, dan is online op dit moment het voordeligst: je weddenschap blijft ook staan als de speler invalt. Wie in de winkel speelt, doet er goed aan om pas in te zetten als de opstellingen bekend zijn, ongeveer een uur voor de aftrap. Zo voorkom je dat je inzet terugkomt omdat je speler op de bank begint. Online wedden bij TOTO doe je via een <a href="{TOTO}" target="_blank" rel="sponsored noopener">gratis TOTO-account</a> (18+). Daarmee kun je bij TOTO ook live meekijken; meer daarover op onze <a href="/zenders/toto">TOTO-pagina</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wat gebeurt er bij TOTO als mijn speler invalt?</strong><br>Online blijft je weddenschap sinds 28 april 2026 staan, ook bij schoten, schoten op doel en assists. In de TOTO Winkel wordt een weddenschap op schoten, schoten op doel of assists ongeldig als de speler niet in de basis begon.</p>
<p><strong>Wat als mijn doelpuntenmaker niet speelt?</strong><br>Dan wordt de weddenschap ongeldig en krijg je je inzet terug, zowel in de winkel als online.</p>
<p><strong>Krijg ik bij TOTO mijn geld terug als een tennisser opgeeft?</strong><br>Bij een weddenschap op de winnaar van de partij krijg je je inzet terug. Weddenschappen die al beslist waren, zoals de winnaar van de eerste set, worden gewoon uitbetaald.</p>
<p><strong>Tellen verlengingen mee bij TOTO?</strong><br>Nee, alleen de reguliere speeltijd met blessuretijd telt, behalve bij weddenschappen op wie zich plaatst of de beker wint.</p>
<p><strong>Tellen eigen doelpunten mee voor de doelpuntenmaker?</strong><br>Nee. Is een eigen doelpunt het enige doelpunt, dan wint de optie "geen doelpuntenmaker".</p>
<p><em>24+ | Gokken is alleen toegestaan voor personen van 18 jaar en ouder. Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_SPELUITLEG,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting"); sys.exit()
    print("item:", WF.create_live(fd))
