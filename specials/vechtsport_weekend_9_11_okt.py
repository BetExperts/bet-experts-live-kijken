# -*- coding: utf-8 -*-
"""Los artikel: alle vechtsport (boksen, MMA, Muay Thai) van vrijdag 9 t/m zondag 11 oktober 2026 in één overzicht.
Gecontroleerd: Schofield (19-0) - Bahdi (20-0) vacante WBA lichtgewicht, Wintrust Arena Chicago; Sandoval (WBA/WBC vlieg)
vs Sergio Mendoza na afmelding Collazo; UFC Allen (#4) - Duncan (#10) 5 ronden middengewicht, prelims 17:00 ET = 23:00 NL,
main 20:00 ET = 02:00 NL. Overige tijden/kanalen uit aangeleverde info.
  python3 specials/vechtsport_weekend_9_11_okt.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Boksen, UFC en MMA dit weekend: alle vechtsport van 9 tot en met 11 oktober op een rij"
SLUG = "boksen-ufc-mma-dit-weekend-9-11-oktober-2026"
SAMENVATTING = ("Van ONE in Bangkok tot Schofield vs Bahdi en UFC Allen vs Duncan: alle vechtsport dit weekend met "
                "Nederlandse tijden en waar je kijkt.")
RUBRIEK_UFC = "678c14300660499bb385a5cd"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in koppen)
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}><thead><tr>{kop}</tr></thead><tbody>{body}</tbody></table>"


DAZN = '<a href="/zenders/dazn">DAZN</a>'
HBO = '<a href="/zenders/hbo-max">HBO Max</a>'

content = f"""<p><strong>Dit weekend is er van vrijdagmiddag tot zondagochtend bijna onafgebroken vechtsport te zien. De grootste bokswedstrijd is Floyd Schofield tegen Lucas Bahdi om de vacante WBA-wereldtitel in het lichtgewicht (zondag vanaf 02:00 uur bij DAZN). Voor MMA-fans is er UFC Fight Night Allen vs Duncan (hoofdkaart zondag 02:00 uur bij HBO Max). Zaterdagavond staan ook Misfits Boxing met Joey Essex tegen Dapper Laughs, KSW 122 en een gratis PFL-event op het programma.</strong></p>
<p>Wie van boksen, MMA, kickboksen of Muay Thai houdt, kan zich dit weekend niet vervelen. Door de tijdsverschillen met Thailand, Polen, Marokko, Londen, Chicago en Las Vegas schuift het programma als een estafette door: eerst Bangkok in de middag, dan Europa in de avond en Amerika in de nacht. In dit overzicht zie je per event de Nederlandse starttijd, wie er vechten en hoe je legaal kijkt, betaald of gratis.</p>
<h3><strong>Het hele weekend in één schema</strong></h3>
{tabel(["Wanneer (NL-tijd)", "Event", "Sport", "Kijken"], [
    ("Vr 9 okt, 13:30", "ONE: The Inner Circle 34", "Muay Thai, kickboksen", "live.onefc.com (betaald)"),
    ("Vr 9 okt, 14:30", "ONE Friday Fights 174", "Muay Thai, kickboksen, MMA", "watch.onefc.com, soms gratis via ONE"),
    ("Za 10 okt, 19:00", "XTB KSW 122", "MMA", "KSWTV.com (betaald)"),
    ("Za 10 okt, 19:00", "PFL Africa: Morocco", "MMA", "Gratis via PFL op YouTube"),
    ("Za 10 okt, 19:30", "Misfits Boxing: Essex vs Dapper", "Crossoverboksen", DAZN),
    ("Za 10 okt, 22:00", "Schofield vs Bahdi: voorprogramma", "Boksen", "Gratis via Golden Boy op YouTube"),
    ("Za 10 okt, 23:00", "UFC Fight Night Allen vs Duncan: prelims", "MMA", HBO + " (Sport-add-on)"),
    ("Zo 11 okt, 02:00", "Schofield vs Bahdi: hoofdkaart", "Boksen", DAZN),
    ("Zo 11 okt, 02:00", "UFC Fight Night Allen vs Duncan: hoofdkaart", "MMA", HBO + " (Sport-add-on)"),
])}
<p><em>De tijden zijn de starttijden van de uitzending. Wanneer de hoofdpartij begint, hangt af van hoe lang de gevechten ervoor duren: een snelle knock-out haalt het schema naar voren, een reeks partijen over de volle afstand schuift het op.</em></p>
<h3><strong>Schofield vs Bahdi: wereldtitelboksen in Chicago</strong></h3>
<p>Sportief is dit de belangrijkste bokswedstrijd van het weekend. In de Wintrust Arena in Chicago vechten twee ongeslagen lichtgewichten om de WBA-titel die vrijkwam toen Gervonta Davis door de bond tot "champion in recess" werd benoemd. De Amerikaan <strong>Floyd "Kid Austin" Schofield</strong> (19-0) is de nummer één van de WBA-ranglijst en dwong die positie af met een knock-out in de eerste ronde tegen Tevin Farmer. De Canadees <strong>Lucas Bahdi</strong> (20-0) is de nummer twee. Hij won zijn laatste drie gevechten, onder meer tegen oud-wereldkampioen Roger Gutiérrez, telkens op punten.</p>
<p>Daarmee is het ook een duel tussen twee stijlen: Schofield staat bekend om zijn snelheid en explosieve punch, Bahdi heeft laten zien dat hij twaalf ronden lang zijn plan kan uitvoeren. Op dezelfde kaart verdedigt <strong>Ricardo Sandoval</strong> zijn WBA- en WBC-titels in het vlieggewicht. Zijn eerdere tegenstander moest afhaken; hij treft nu de Mexicaan Sergio Mendoza.</p>
{tabel(["", ""], [
    ("<strong>Datum</strong>", "Zaterdag 10 oktober (hoofdkaart in de nacht naar zondag)"),
    ("<strong>Locatie</strong>", "Wintrust Arena, Chicago"),
    ("<strong>Hoofdpartij</strong>", "Floyd Schofield – Lucas Bahdi, 12 ronden"),
    ("<strong>Inzet</strong>", "Vacante WBA-wereldtitel lichtgewicht"),
    ("<strong>Voorprogramma</strong>", "Za 22:00 uur, gratis via het YouTube-kanaal van Golden Boy"),
    ("<strong>Hoofdkaart</strong>", "Zo 02:00 uur bij " + DAZN),
])}
<p>Let op je abonnement: bij DAZN Ultimate is deze kaart inbegrepen. Heb je een ander pakket, kijk dan vooraf in de app of je het event los moet aanschaffen. De ringwalks van Schofield en Bahdi worden pas laat in de nacht verwacht.</p>"""

content2 = f"""<h3><strong>UFC Fight Night Allen vs Duncan in Las Vegas</strong></h3>
<p>In de APEX in Las Vegas staat een middengewichtgevecht over vijf ronden centraal. <strong>Brendan Allen</strong>, de nummer vier van de UFC-ranglijst, neemt het op tegen de nummer tien <strong>Christian Leroy Duncan</strong>. Voor de Brit is het zijn eerste hoofdpartij in de UFC, en met een zege op Allen zou hij flink stijgen in de divisie. Allen wil juist laten zien dat hij thuishoort in de strijd om een titelgevecht.</p>
<p>De hoofdkaart heeft meer interessante partijen. Matheus Camilo en Jai Herbert vechten in het lichtgewicht in de co-main event, Loopy Godinez neemt het op tegen Ketlen Souza en Andre Fili treft Kai Kamaka III in het vedergewicht. In de prelims staan onder anderen Gerald Meerschaert en Niko Price.</p>
{tabel(["", ""], [
    ("<strong>Datum</strong>", "Zaterdag 10 oktober (hoofdkaart in de nacht naar zondag)"),
    ("<strong>Locatie</strong>", "APEX, Las Vegas"),
    ("<strong>Hoofdpartij</strong>", "Brendan Allen – Christian Leroy Duncan, 5 ronden middengewicht"),
    ("<strong>Prelims</strong>", "Za 23:00 uur"),
    ("<strong>Hoofdkaart</strong>", "Zo 02:00 uur"),
    ("<strong>Kijken</strong>", HBO + " met de Sport-add-on"),
])}
<p>In Nederland zie je de volledige kaart bij HBO Max, met de Sport-add-on. Een gratis legale stream van het hele event is er niet. UFC Fight Pass heeft wel live vechtsport en een groot archief, maar is voor deze Fight Night niet de zekerste keuze. Wil je de hoofdpartij zien, schakel dan in bij de start van de hoofdkaart; het hoofdgevecht valt meestal in de vroege zondagochtend.</p>
<h3><strong>Misfits Boxing: Joey Essex tegen Dapper Laughs</strong></h3>
<p>Wie boksen vooral als avondvullend spektakel ziet, kan zaterdag terecht bij Misfits Boxing. In de Copper Box Arena in Londen, het voormalige olympische handbalstadion, neemt realityster <strong>Joey Essex</strong> het op tegen comedian <strong>Daniel O'Reilly</strong>, beter bekend als Dapper Laughs. Misfits draait om bekende gezichten uit entertainment en sociale media, met veel show rond de partijen. De uitzending bij {DAZN} begint om 19:30 uur Nederlandse tijd. De hoofdpartij wordt rond 22:15 uur verwacht, al is dat een richttijd. Misfits zit in een gewoon DAZN-abonnement; een gratis uitzending van de volledige kaart is er niet.</p>
<h3><strong>Vrijdagmiddag: ONE Championship vanuit Bangkok</strong></h3>
<p>Het weekend begint al op vrijdagmiddag in het beroemde Lumpinee Stadium in Bangkok, het mekka van het Muay Thai. Om 13:30 uur begint <strong>The Inner Circle 34</strong>, met in de hoofdpartij Suriyanlek Por Yenying tegen Rustam Yunusov in het vlieggewicht Muay Thai. Dit event is alleen te zien met een betaald lidmaatschap op live.onefc.com.</p>
<p>Een uur later volgt <strong>ONE Friday Fights 174</strong>, met Dedduanglek Torfunfarm tegen Mongkoldetlek Por Pim-on als hoofdpartij. Op deze kaart staan Muay Thai, kickboksen en MMA door elkaar. ONE zendt uit via watch.onefc.com en soms ook gratis via zijn YouTube- en Facebook-kanalen, maar dat verschilt per land. Kijk dus vooraf of de stream in Nederland beschikbaar is.</p>"""

content3 = """<h3><strong>Zaterdagavond: KSW 122 en PFL Africa</strong></h3>
<p>Om 19:00 uur beginnen twee Europese en Afrikaanse MMA-events tegelijk. In het Poolse Rzeszów verdedigt <strong>Vitalii Yakymenko</strong> bij <strong>XTB KSW 122</strong> zijn bantamgewichttitel tegen Marcello Morelli. KSW is de grootste MMA-organisatie van Europa en staat bekend om zijn spectaculaire producties. Buiten Polen kijk je via een betaalde livestream op KSWTV.com.</p>
<p>In Casablanca staat <strong>PFL Africa: Morocco</strong> op het programma, met een zwaargewichtgevecht tussen Abdoulaye Kane en Badr Medkouri als hoofdpartij. Dit is de beste gratis optie van het weekend: PFL zendt het event uit via zijn officiële YouTube-kanaal.</p>
<h3><strong>Welk event past bij jou?</strong></h3>
<ul><li><strong>Echt wereldtitelboksen:</strong> Schofield vs Bahdi bij DAZN, in de nacht van zaterdag op zondag.</li><li><strong>Topniveau MMA:</strong> UFC Fight Night Allen vs Duncan bij HBO Max.</li><li><strong>Gratis kijken:</strong> PFL Africa op YouTube en het voorprogramma van Schofield vs Bahdi bij Golden Boy.</li><li><strong>Show en entertainment:</strong> Misfits Boxing met Essex en Dapper Laughs bij DAZN.</li><li><strong>Muay Thai en kickboksen:</strong> ONE vanuit Bangkok op vrijdagmiddag.</li><li><strong>Europese MMA-titel:</strong> KSW 122 via KSWTV.com.</li></ul>
<h3><strong>Tips voor een lange vechtnacht</strong></h3>
<p>De Amerikaanse hoofdkaarten vallen voor Nederlandse kijkers diep in de nacht. Log vooraf in bij DAZN of HBO Max, zodat je niet op het laatste moment met een wachtwoord of betaling bezig bent. Beide apps werken op smart-tv's, laptops, tablets, telefoons, spelcomputers en streamingapparaten. Wil je niet wachten, kijk dan de prelims live en de hoofdpartij de volgende ochtend terug. Vermijd in dat geval sociale media als je de uitslag nog niet wilt weten. Kijk ook altijd via de officiële kanalen: illegale streams zijn niet alleen onbetrouwbaar, maar ook onveilig.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Hoe laat begint Schofield vs Bahdi?</strong><br>Het gratis voorprogramma begint zaterdag om 22:00 uur, de hoofdkaart bij DAZN zondag om 02:00 uur. De hoofdpartij volgt later in de nacht.</p>
<p><strong>Waar kijk ik UFC Allen vs Duncan in Nederland?</strong><br>Bij HBO Max met de Sport-add-on. De prelims beginnen zaterdag om 23:00 uur, de hoofdkaart zondag om 02:00 uur.</p>
<p><strong>Is Misfits Boxing gratis te zien?</strong><br>Nee, de kaart is alleen bij DAZN te zien, maar zit wel in een gewoon abonnement.</p>
<p><strong>Welk vechtsportevent is dit weekend gratis?</strong><br>PFL Africa: Morocco op het YouTube-kanaal van PFL en het voorprogramma van Schofield vs Bahdi op het YouTube-kanaal van Golden Boy.</p>
<p><strong>Om welke titel vechten Schofield en Bahdi?</strong><br>Om de vacante WBA-wereldtitel in het lichtgewicht, die vrijkwam nadat Gervonta Davis tot "champion in recess" werd benoemd.</p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_UFC,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting"); sys.exit()
    print("item:", WF.create_live(fd))
