# -*- coding: utf-8 -*-
"""Los artikel: Jong Oranje treft Jong Denemarken in de play-offs voor het EK onder 21 van 2027 (loting 9 okt 2026).
Gecontroleerd: EK 2027 in Albanië/Servië (16 juni-3 juli, 16 landen), play-offs 9-17 nov (4 duels over twee wedstrijden),
EK 2025: NL-DEN 1-2 (groep), kwartfinale 1-0 Portugal (Poku), halve finale 1-2 Engeland (2x Elliott).
  python3 specials/jong_oranje_playoff_denemarken.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Jong Oranje treft Jong Denemarken in play-offs om EK-ticket: tegenstander, data en kansen"
SLUG = "jong-oranje-jong-denemarken-play-offs-ek-onder-21-2027"
SAMENVATTING = ("Jong Oranje speelt in november tegen Jong Denemarken om een plek op het EK onder 21 van 2027. Data, "
                "format, de weg naar de play-offs en de historie.")
RUBRIEK_NL = "66d6d655bc312d5c0e834ecd"
COMPETITIE_EK21_KWAL = "6abaf551b3633bce07b3312c"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in koppen)
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}><thead><tr>{kop}</tr></thead><tbody>{body}</tbody></table>"


content = f"""<p><strong>Jong Oranje speelt in de play-offs voor het EK onder 21 van 2027 tegen Jong Denemarken. Dat bepaalde de loting op vrijdag 9 oktober in het Zwitserse Nyon. De heenwedstrijd wordt gespeeld tussen 9 en 12 november, de return tussen 15 en 17 november. De winnaar over twee wedstrijden plaatst zich voor het EK in Albanië en Servië.</strong></p>
<p>Voor de ploeg van bondscoach Michael Reiziger is het de laatste kans op het eindtoernooi van volgend jaar, en een weerzien met een bekende tegenstander. Op het vorige EK, in 2025 in Slowakije, troffen beide landen elkaar al in de groepsfase. Toen wonnen de Denen met 2-1.</p>
<h3><strong>De play-off in het kort</strong></h3>
{tabel(["", ""], [
    ("<strong>Tegenstander</strong>", "Jong Denemarken"),
    ("<strong>Heenwedstrijd</strong>", "Tussen 9 en 12 november 2026"),
    ("<strong>Return</strong>", "Tussen 15 en 17 november 2026"),
    ("<strong>Format</strong>", "Twee wedstrijden, één thuis en één uit; de beste totaalscore plaatst zich"),
    ("<strong>Inzet</strong>", "Een plek op het EK onder 21 van 2027"),
    ("<strong>EK 2027</strong>", "16 juni – 3 juli 2027 in Albanië en Servië"),
])}
<p><em>De precieze speeldata, aftraptijden en speelsteden worden later door de UEFA en de KNVB bekendgemaakt.</em></p>
<h3><strong>Via een omweg naar de play-offs</strong></h3>
<p>Lang zag het er niet goed uit voor Jong Oranje. In de kwalificatiepoule liet de ploeg punten liggen tegen Israël en verloor ze in blessuretijd van Noorwegen, waardoor het EK steeds verder uit beeld raakte. Op de slotavond, afgelopen dinsdag, moest Jong Oranje zelf winnen en hopen op hulp van elders.</p>
<p>Beide gebeurden. Jong Oranje won overtuigend met 4-0 van Bosnië en Herzegovina, en in Noorwegen kwamen Jong Noorwegen en Jong Israël niet verder dan een gelijkspel. Daardoor eindigde Nederland toch als tweede in de poule. Die tweede plek gaf recht op de play-offs: de laatste route naar het EK.</p>
<h3><strong>Zo werken de play-offs</strong></h3>
<p>Aan het EK onder 21 van 2027 doen zestien landen mee. Gastlanden Albanië en Servië zijn automatisch geplaatst. Verder gaan de negen groepswinnaars en de beste nummer twee rechtstreeks naar het eindtoernooi. De acht andere nummers twee, onder wie Nederland, spelen in vier duels om de laatste vier tickets. Elk duel bestaat uit een thuis- en een uitwedstrijd. Bij een gelijke totaalscore volgen een verlenging en zo nodig strafschoppen.</p>"""

content2 = """<h3><strong>Weerzien met Denemarken: wat gebeurde er op het EK van 2025?</strong></h3>
<p>Op het EK van 2025 in Slowakije zaten Nederland en Denemarken samen in de groep, met Finland en Oekraïne. Jong Oranje begon teleurstellend met een 2-2 tegen Finland en verloor daarna in Prešov met 1-2 van de Denen. Pas in de laatste groepswedstrijd volgde met 2-0 tegen Oekraïne de bevrijding.</p>
<p>Daarna liet Jong Oranje een heel ander gezicht zien. In de kwartfinale werd favoriet Portugal met tien man verslagen: invaller Ernest Poku maakte het enige doelpunt. In de halve finale was titelhouder Engeland met 2-1 te sterk, door twee doelpunten van Harvey Elliott. De Denen bleken in die groep dus een lastige tegenstander, en dat maakt deze play-off extra beladen.</p>
<h3><strong>Wat maakt Jong Denemarken gevaarlijk?</strong></h3>
<p>Denemarken heeft al jaren een sterke jeugdopleiding, met clubs als FC Kopenhagen, FC Midtjylland en Brøndby die talenten vroeg laten spelen. Veel Deense jeugdinternationals spelen bovendien al in de grote Europese competities, ook in de Eredivisie. Dat zie je terug in het spel: fysiek sterk, goed georganiseerd en efficiënt in de omschakeling.</p>
<p>Daar staat tegenover dat Jong Oranje in de laatste kwalificatiewedstrijd met de 4-0 tegen Bosnië liet zien wat het kan als het team op dreef is. Met spelers die wekelijks spelen in de Eredivisie en daarbuiten, is de selectie van Reiziger aan elkaar gewaagd met die van de Denen.</p>"""

content3 = """<h3><strong>Wat staat er op het spel?</strong></h3>
<p>Het EK onder 21 is voor jonge spelers een belangrijk podium. Scouts van topclubs uit heel Europa kijken mee, en een goed toernooi kan een carrière versnellen. Voor Jong Oranje zou het bovendien een vervolg zijn op het sterke EK van 2025, toen de ploeg tot de halve finale kwam. Het is voor het eerst dat het EK onder 21 in Albanië en Servië wordt gespeeld. Er wordt gespeeld in vier groepen van vier, waarna de nummers één en twee doorgaan naar de kwartfinales.</p>
<h3><strong>Onze verwachting</strong></h3>
<p>Het wordt een gelijkopgaand tweeluik. Denemarken heeft het psychologische voordeel van de zege op het vorige EK, maar Jong Oranje gaat met vertrouwen de play-offs in na de ontsnapping op de slotavond. Wij zien Nederland als lichte favoriet, mits de ploeg in de heenwedstrijd niet te veel weggeeft. Zodra de odds bekend zijn en de wedstrijden dichterbij komen, vind je onze voorspellingen bij onze <a href="/wedtips">wedtips</a>.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Tegen wie speelt Jong Oranje in de play-offs?</strong><br>Tegen Jong Denemarken. De loting vond plaats op vrijdag 9 oktober 2026 in Nyon.</p>
<p><strong>Wanneer spelen Jong Oranje en Jong Denemarken?</strong><br>De heenwedstrijd is tussen 9 en 12 november, de return tussen 15 en 17 november 2026. De exacte data volgen nog.</p>
<p><strong>Hoe plaatste Jong Oranje zich voor de play-offs?</strong><br>Door op de slotavond met 4-0 van Bosnië en Herzegovina te winnen, terwijl Noorwegen en Israël gelijkspeelden. Daardoor werd Nederland tweede in de poule.</p>
<p><strong>Waar wordt het EK onder 21 van 2027 gespeeld?</strong><br>In Albanië en Servië, van 16 juni tot en met 3 juli 2027.</p>
<p><strong>Wat was de uitslag tussen Jong Oranje en Jong Denemarken op het EK van 2025?</strong><br>Denemarken won in de groepsfase met 2-1.</p>
<p><em>Gokken is alleen toegestaan voor personen van 18 jaar en ouder. Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_NL, "competitie": COMPETITIE_EK21_KWAL,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting"); sys.exit()
    print("item:", WF.create_live(fd))
