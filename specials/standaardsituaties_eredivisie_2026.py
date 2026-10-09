# -*- coding: utf-8 -*-
"""Los artikel: specialisten bij standaardsituaties van alle Eredivisie-clubs (2026/27, na 7 speelrondes).
Selecties, stand en alle strafschoppen gecontroleerd via API-Football (9 okt 2026); vertrek Ueda via feyenoord.com.
  python3 specials/standaardsituaties_eredivisie_2026.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Corners, vrije trappen en penalty's: de specialisten van alle Eredivisie-clubs"
SLUG = "standaardsituaties-eredivisie-corners-vrije-trappen-penaltys-2026-27"
SAMENVATTING = ("Wie neemt de corners, vrije trappen en penalty's bij Ajax, PSV, Feyenoord en de andere Eredivisie-clubs? "
                "Alle 18 specialisten op een rij.")
RUBRIEK_EREDIVISIE = "66a0b9c3af037fa49136bd98"
COMPETITIE_EREDIVISIE = "65de2f987de877fdf6583d10"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in koppen)
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}><thead><tr>{kop}</tr></thead><tbody>{body}</tbody></table>"


# club, slug, corners, vrije trappen, penalty's, aanname?
CLUBS = [
    ("AZ", "az", "Peer Koopmeiners, Weslley Patati", "Peer Koopmeiners, Calvin Stengs", "Mexx Meerdink", True),
    ("Feyenoord", "feyenoord", "Anis Hadj Moussa, Sem Steijn, Charles Vanhoutte", "Sem Steijn, Anis Hadj Moussa", "Nacho Ferri, Luciano Valente", False),
    ("PSV", "psv", "Ivan Perišić", "Mauro Júnior, Ivan Perišić", "Ricardo Pepi, Ivan Perišić, Sven Mijnans", False),
    ("FC Twente", "fc-twente", "Daouda Weidmann, Younes Taha, Marko Pjaca", "Ramiz Zerrouki, Younes Taha, Marko Pjaca", "Wout Weghorst", False),
    ("Ajax", "ajax", "Steven Berghuis, Viktor Tsygankov", "Steven Berghuis, Viktor Tsygankov, Julian Brandt", "Tolu Arokodare, Marcos Leonardo", True),
    ("Fortuna Sittard", "fortuna-sittard", "Mohamed Ihattaren, Shiloh 't Zand", "Mohamed Ihattaren, Shiloh 't Zand", "Mohamed Ihattaren", True),
    ("Excelsior", "excelsior", "Simon Janssen, Irakli Yegoian", "Irakli Yegoian, Simon Janssen, Lennard Hartjes", "Noah Naujoks, Aymen Sliti", True),
    ("FC Groningen", "fc-groningen", "David van der Werff, Tika de Jonge", "David van der Werff, Tika de Jonge", "Brynjólfur Willumsson, Thom van Bergen, Oskar Zawada", True),
    ("Go Ahead Eagles", "go-ahead-eagles", "Mathis Suray, Victor Edvardsen, Dean James", "Mathis Suray, Dean James", "Victor Edvardsen, Mathis Suray", True),
    ("sc Heerenveen", "heerenveen", "Jacob Trenskow, Levi Smans", "Dylan Vente, Jacob Trenskow, Levi Smans", "Dylan Vente, Maxence Rivera", True),
    ("NEC", "nec-nijmegen", "Tjaronn Chery, Dušan Tadić, Emre Mor", "Dušan Tadić, Tjaronn Chery", "Tjaronn Chery", False),
    ("Sparta Rotterdam", "sparta-rotterdam", "Julian Baas, Jens Toornstra, Bas Kuipers", "Jens Toornstra, Casper Terho, Bas Kuipers", "Andrej Kostić, Jens Toornstra, Milan Zonneveld", True),
    ("Telstar", "telstar", "Patrick Brouwer, Jeff Hardeveld", "Jeff Hardeveld, Patrick Brouwer", "Ronald Koeman jr.", False),
    ("SC Cambuur", "sc-cambuur", "Rafik El Arguioui, Nicky Souren", "Rafik El Arguioui, Nicky Souren", "Rafik El Arguioui, Nicky Souren", True),
    ("FC Utrecht", "fc-utrecht", "Yoann Cathline, Davy van den Berg", "Yoann Cathline, Davy van den Berg", "Artem Stepanov", False),
    ("PEC Zwolle", "pec-zwolle", "Tobias Sommer, Damian van der Haar", "Thijs Oosting, Tobias Sommer", "Koen Kostons", False),
    ("ADO Den Haag", "ado-den-haag", "Juho Kilo, Daryl van Mieghem", "Daryl van Mieghem, Juho Kilo", "Daryl van Mieghem, Yannick Eduardo", True),
    ("Willem II", "willem-2", "Calvin Twigt, Tonny Vilhena, Jaden Slory, Nathan Tjoe-A-On", "Eser Gürbüz, Calvin Twigt, Jaden Slory", "Thomas Verheydt, Devin Haen", True),
]
STAND = {"AZ": "1e", "Feyenoord": "2e", "PSV": "3e", "FC Twente": "4e", "Ajax": "5e", "Fortuna Sittard": "6e",
         "Excelsior": "7e", "FC Groningen": "8e", "Go Ahead Eagles": "9e", "sc Heerenveen": "10e", "NEC": "11e",
         "Sparta Rotterdam": "12e", "Telstar": "13e", "SC Cambuur": "14e", "FC Utrecht": "15e", "PEC Zwolle": "16e",
         "ADO Den Haag": "17e", "Willem II": "18e"}
SLUGS = {c[0]: c[1] for c in CLUBS}


def lijst(club):
    _, _, c, v, p, a = next(x for x in CLUBS if x[0] == club)
    return (f"<ul><li><strong>Corners:</strong> {c}</li><li><strong>Vrije trappen:</strong> {v}</li>"
            f"<li><strong>Penalty's:</strong> {p}{' (verwachting)' if a else ''}</li></ul>")


def kop(club):
    return f'<h3><strong>{club}</strong></h3>'


def cl(club, tekst=None):
    return f'<a href="/clubs/{SLUGS[club]}">{tekst or club}</a>'


overzicht = tabel(["Club", "Corners", "Vrije trappen", "Penalty's"],
                  [(cl(c), co.split(", ")[0], v.split(", ")[0], p.split(", ")[0] + (" *" if a else ""))
                   for c, _, co, v, p, a in CLUBS])

content = f"""<p><strong>Wie neemt de corners bij Feyenoord, wie legt de bal klaar voor een vrije trap bij Ajax en wie gaat er bij PSV achter een penalty staan? Na zeven speelrondes van de Eredivisie 2026/27 is bij de meeste clubs duidelijk wie de standaardsituaties neemt. Hieronder vind je per club de vaste corner-, vrijetrap- en penaltynemers, plus de spelers die hen kunnen vervangen.</strong></p>
<p>Standaardsituaties beslissen in de <a href="/competities/eredivisie">Eredivisie</a> geregeld wedstrijden. Een goede cornernemer levert kansen op, een specialist bij vrije trappen kan een gesloten duel openbreken en een betrouwbare penaltynemer is goud waard. Weet je wie die rollen heeft, dan begrijp je een wedstrijd beter. Het helpt ook als je kijkt naar markten op doelpunten of schoten van een speler.</p>
<p>Een belangrijke kanttekening bij de penalty's: elf van de achttien clubs hebben dit seizoen nog geen strafschop genomen. Bij die clubs is de penaltynemer een <strong>verwachting</strong>, gebaseerd op eerdere seizoenen, de rol van de speler in het elftal en de huidige selectie. In de overzichten staat dat steeds aangegeven.</p>
<h3><strong>Overzicht: de eerste keuze per club</strong></h3>
{overzicht}
<p><em>Clubs op volgorde van de stand na zeven speelrondes. * = nog geen penalty genomen dit seizoen, dus een verwachting. Selecties gecontroleerd op 9 oktober 2026.</em></p>
<h3><strong>Alle penalty's in de Eredivisie tot nu toe</strong></h3>
<p>In de eerste zeven speelrondes zijn in de Eredivisie dertien penalty's genomen, door zeven clubs. Daaruit valt af te lezen wie bij die clubs echt de eerste keuze is.</p>
{tabel(["Datum", "Wedstrijd", "Nemer", "Resultaat"], [
    ("23 aug", "PSV – FC Groningen", "Ricardo Pepi (PSV)", "Raak"),
    ("23 aug", "SC Cambuur – Feyenoord", "Ayase Ueda (Feyenoord)", "Raak"),
    ("29 aug", "PEC Zwolle – NEC", "Tjaronn Chery (NEC)", "Raak"),
    ("29 aug", "PEC Zwolle – NEC", "Tjaronn Chery (NEC)", "Raak"),
    ("29 aug", "PEC Zwolle – NEC", "Koen Kostons (PEC Zwolle)", "Raak"),
    ("29 aug", "PEC Zwolle – NEC", "Koen Kostons (PEC Zwolle)", "Gemist"),
    ("30 aug", "FC Utrecht – PSV", "Sven Mijnans (PSV)", "Gemist"),
    ("6 sep", "Telstar – SC Cambuur", "Ronald Koeman jr. (Telstar)", "Raak (2x)"),
    ("8 sep", "FC Utrecht – Go Ahead Eagles", "Artem Stepanov (FC Utrecht)", "Raak"),
    ("9 sep", "FC Twente – Telstar", "Wout Weghorst (FC Twente)", "Gemist"),
    ("12 sep", "FC Twente – ADO Den Haag", "Wout Weghorst (FC Twente)", "Raak"),
    ("20 sep", "Feyenoord – FC Utrecht", "Luciano Valente (Feyenoord)", "Raak"),
])}"""

content2 = f"""<h2><strong>De specialisten per club</strong></h2>
{kop("AZ")}
<p>Bij koploper {cl("AZ")} is de rolverdeling bij de corners het duidelijkst van de hele competitie. Peer Koopmeiners nam in de eerste zeven duels 31 hoekschoppen, meer dan wie ook in de Eredivisie. Weslley Patati volgt met zestien corners op afstand als tweede optie. Kees Smit stond ook een keer bij de cornervlag, maar is geen vaste nemer.</p>
<p>Bij vrije trappen rond de zestien zijn Koopmeiners en Calvin Stengs de aangewezen spelers. AZ kreeg dit seizoen nog geen strafschop, dus voor de penalty's is spits Mexx Meerdink een verwachting.</p>
{lijst("AZ")}
{kop("Feyenoord")}
<p>Anis Hadj Moussa neemt bij {cl("Feyenoord")} het merendeel van de corners zolang hij op het veld staat. Met zijn linkervoet is de Algerijn ook gevaarlijk bij vrije trappen. Sem Steijn is de andere kandidaat voor vrije trappen en neemt net als Charles Vanhoutte ook af en toe een corner.</p>
<p>De penalty's zijn een apart verhaal. Op 23 augustus schoot Ayase Ueda raak bij Cambuur, maar hij vertrok eind augustus naar Lille. Tegen FC Utrecht nam Luciano Valente de strafschop en ook hij scoorde. Volgens Valente zelf liet Nacho Ferri hem die penalty nemen. Daarmee is Ferri formeel de eerste nemer, maar is Valente meer dan een noodoplossing.</p>
{lijst("Feyenoord")}
{kop("PSV")}
<p>Sinds het vertrek van Joey Veerman is Ivan Perišić de vaste cornernemer van {cl("PSV")}. De Kroaat nam in zeven wedstrijden al 21 hoekschoppen. Bij directe vrije trappen is Mauro Júnior de man om op te letten: tegen FC Utrecht krulde hij er al een rechtstreeks in.</p>
<p>Ricardo Pepi is de eerste penaltynemer en benutte de strafschop tegen FC Groningen. Achter hem staan Perišić en Sven Mijnans. Mijnans miste in de slotfase tegen FC Utrecht een penalty.</p>
{lijst("PSV")}
{kop("FC Twente")}
<p>Daouda Weidmann is in Enschede uitgegroeid tot de belangrijkste cornernemer: 26 hoekschoppen in zes wedstrijden. Als hij niet speelt of niet achter de bal staat, nemen Younes Taha of Marko Pjaca het over. Vrije trappen zijn vaker voor Ramiz Zerrouki, met Taha en Pjaca als alternatieven.</p>
<p>Bij de penalty's laat {cl("FC Twente")} geen twijfel bestaan. Wout Weghorst miste tegen Telstar nog, maar ging drie dagen later tegen ADO Den Haag gewoon opnieuw achter de bal staan en scoorde wel.</p>
{lijst("FC Twente")}
{kop("Ajax")}
<p>Steven Berghuis is nog altijd de eerste cornernemer van {cl("Ajax")}; in zijn eerste zes competitieduels nam hij er twaalf. Viktor Tsygankov is intussen een serieus alternatief. Tegen Excelsior, toen Berghuis op de bank begon, stond de Oekraïner bij de cornervlag. Ajax lijkt de corners dus te verdelen over de twee linkspoten, afhankelijk van wie er speelt.</p>
<p>Voor vrije trappen komt daar Julian Brandt bij. Ajax kreeg nog geen penalty, waardoor Tolu Arokodare en Marcos Leonardo de logische kandidaten zijn.</p>
{lijst("Ajax")}
{kop("Fortuna Sittard")}
<p>Bij {cl("Fortuna Sittard")} draait veel om Mohamed Ihattaren. Staat hij op het veld, dan neemt hij de corners en de vrije trappen, en daar komt regelmatig gevaar uit. Valt hij uit of wordt hij gewisseld, dan neemt Shiloh 't Zand die taken over. Fortuna nam nog geen penalty, maar alles wijst naar Ihattaren als eerste nemer.</p>
{lijst("Fortuna Sittard")}
{kop("Excelsior")}
<p>Opvallend bij {cl("Excelsior")}: de belangrijkste cornernemer is een verdediger. Simon Janssen nam in de eerste weken al veel hoekschoppen en de Rotterdammers creëerden daaruit meteen kansen. Irakli Yegoian neemt een deel van de standaardsituaties over, en bij vrije trappen is ook Lennard Hartjes een optie. Excelsior nam nog geen penalty; Noah Naujoks heeft daarmee ervaring uit eerdere seizoenen.</p>
{lijst("Excelsior")}
{kop("FC Groningen")}
<p>David van der Werff neemt bij {cl("FC Groningen")} een groot deel van de corners en staat ook vaak achter de bal bij vrije trappen op de helft van de tegenstander. Tika de Jonge is de tweede optie. Bij de penalty's is het nog afwachten: de enige strafschop die Groningen kreeg, werd na tussenkomst van de VAR teruggedraaid. Brynjólfur Willumsson, Thom van Bergen en Oskar Zawada zijn de logische kandidaten.</p>
{lijst("FC Groningen")}
{kop("Go Ahead Eagles")}
<p>{cl("Go Ahead Eagles")} heeft geen vaste specialist, maar spreidt de standaardsituaties. Mathis Suray neemt veel corners, maar ook Victor Edvardsen stond dit seizoen al meerdere keren bij de vlag. Dean James is met zijn linkervoet gevaarlijk vanaf de linkerkant, ook bij vrije trappen. Deventer kreeg nog geen penalty. Edvardsen nam er eerder in zijn tijd bij Go Ahead geregeld een, en Suray benutte er vorig seizoen een in de Eredivisie.</p>
{lijst("Go Ahead Eagles")}
{kop("sc Heerenveen")}
<p>Jacob Trenskow is bij {cl("sc Heerenveen")} de vaste cornernemer. De Deen stond in de eerste speelrondes vaak bij de vlag, met Levi Smans als vervanger. Spits Dylan Vente is de interessante naam bij directe vrije trappen: dit seizoen schoot hij er al een tegen de lat. Hij is ook de waarschijnlijke penaltynemer, al moet Heerenveen de eerste strafschop nog krijgen.</p>
{lijst("sc Heerenveen")}
{kop("NEC")}
<p>Weinig clubs hebben zoveel goede trappers als {cl("NEC")}. Tjaronn Chery, Dušan Tadić en Emre Mor namen allemaal al corners, en bij vrije trappen zijn vooral Tadić en Chery gevaarlijk. Over de penalty's is geen twijfel: Chery kreeg er twee bij PEC Zwolle en schoot ze allebei binnen.</p>
{lijst("NEC")}"""

content3 = f"""{kop("Sparta Rotterdam")}
<p>Julian Baas is bij {cl("Sparta Rotterdam")} ver de belangrijkste cornernemer: 24 hoekschoppen in zes wedstrijden, tegen vijf voor Jens Toornstra. Toornstra blijft met zijn techniek wel een vaste kandidaat voor vrije trappen, net als Casper Terho en Bas Kuipers. Sparta nam nog geen penalty; Andrej Kostić is de verwachte nemer.</p>
{lijst("Sparta Rotterdam")}
{kop("Telstar")}
<p>Jeff Hardeveld werd lang gezien als dé specialist van {cl("Telstar")}, maar bij de corners heeft Patrick Brouwer hem ingehaald. Brouwer nam er in zeven wedstrijden elf, Hardeveld acht. Bij vrije trappen blijft Hardeveld wel de eerste keuze. De penaltynemer is duidelijk: Ronald Koeman jr. kreeg er tegen SC Cambuur twee en benutte ze allebei.</p>
{lijst("Telstar")}
{kop("SC Cambuur")}
<p>Rafik El Arguioui is een van de positieve verrassingen van de eerste speelrondes. Bij {cl("SC Cambuur")} neemt hij het merendeel van de corners en hij schiet ook directe vrije trappen op doel. Nicky Souren is de tweede optie. Cambuur kreeg nog geen penalty, dus ook daar is El Arguioui een verwachting.</p>
{lijst("SC Cambuur")}
{kop("FC Utrecht")}
<p>Yoann Cathline is bij {cl("FC Utrecht")} uitgegroeid tot de belangrijkste cornernemer, en uit zijn hoekschoppen ontstond al meerdere keren gevaar. Davy van den Berg is de andere speler die standaardsituaties neemt. Bij de penalty's is Artem Stepanov de man: tegen Go Ahead Eagles schoot hij in de slotfase een strafschop binnen.</p>
{lijst("FC Utrecht")}
{kop("PEC Zwolle")}
<p>{cl("PEC Zwolle")} verdeelt de corners vooral tussen Tobias Sommer en Damian van der Haar. Thijs Oosting zie je eerder bij vrije trappen dan bij de cornervlag. Penaltynemer is Koen Kostons. Tegen NEC kreeg hij er twee: de eerste ging erin, de tweede belandde op het aluminium.</p>
{lijst("PEC Zwolle")}
{kop("ADO Den Haag")}
<p>Juho Kilo kwam bij {cl("ADO Den Haag")} in de openingsweken naar voren als cornernemer. Daryl van Mieghem is met zijn goede trap de logische speler voor zowel corners als vrije trappen. ADO kreeg nog geen strafschop. Van Mieghem en Yannick Eduardo zijn de meest voor de hand liggende kandidaten.</p>
{lijst("ADO Den Haag")}
{kop("Willem II")}
<p>Bij {cl("Willem II")} heeft Calvin Twigt zijn plek als eerste cornernemer verstevigd: tien hoekschoppen in zeven duels. Tegen Fortuna Sittard kwam er een nieuwe naam bij. Tonny Vilhena nam een corner waaruit Finn Stam kopte. Eerder namen ook Jaden Slory en Nathan Tjoe-A-On hoekschoppen. Voor vrije trappen is Eser Gürbüz de eerste naam. Willem II wacht nog op zijn eerste penalty; Thomas Verheydt en Devin Haen zijn de kandidaten.</p>
{lijst("Willem II")}
<h3><strong>Wat zegt dit voor je weddenschap?</strong></h3>
<p>De specialist bij standaardsituaties is bij de bookmakers vaak een interessante speler. Een vaste penaltynemer heeft een extra kans op een doelpunt. Een cornernemer met een goede trap staat vaak hoog bij assists. Een vrijetrapspecialist schiet vaker op doel. Controleer voor een wedstrijd wel altijd de opstelling: begint de specialist op de bank, dan neemt een ander de standaardsituaties.</p>
<p>De opstellingen en onze voorspellingen per duel vind je bij onze <a href="/wedtips">wedtips</a>. Welke wedstrijden dit weekend live te zien zijn, lees je in <a href="/nieuws/eredivisie-speelronde-8-op-tv-9-oktober-2026">Eredivisie speelronde 8 op tv</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wie neemt de penalty's bij PSV?</strong><br>Ricardo Pepi is de eerste keuze; hij scoorde tegen FC Groningen. Daarachter staan Ivan Perišić en Sven Mijnans.</p>
<p><strong>Wie neemt de penalty's bij Feyenoord?</strong><br>Nacho Ferri is de eerste keuze. Tegen FC Utrecht liet hij de penalty aan Luciano Valente, die raak schoot.</p>
<p><strong>Wie neemt de corners bij Ajax?</strong><br>Steven Berghuis, met Viktor Tsygankov als alternatief. Speelt Berghuis niet, dan neemt Tsygankov de corners.</p>
<p><strong>Welke speler neemt de meeste corners in de Eredivisie?</strong><br>Peer Koopmeiners van AZ, met 31 corners in de eerste zeven speelrondes.</p>
<p><strong>Welke clubs hebben nog geen penalty genomen?</strong><br>AZ, Ajax, Fortuna Sittard, Excelsior, FC Groningen, Go Ahead Eagles, sc Heerenveen, Sparta Rotterdam, SC Cambuur, ADO Den Haag en Willem II.</p>
<p><em>Gokken is alleen toegestaan voor personen van 18 jaar en ouder. Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_EREDIVISIE, "competitie": COMPETITIE_EREDIVISIE,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting"); sys.exit()
    print("item:", WF.create_live(fd))
