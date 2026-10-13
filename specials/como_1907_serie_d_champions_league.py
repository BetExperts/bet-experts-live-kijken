# -*- coding: utf-8 -*-
"""Los artikel: Van Serie D naar Champions League: dit is Como 1907 (voor Feyenoord – Como, wo 14 okt 2026 18:45).
Aanleveringstekst van de gebruiker herschreven en aangevuld. Gecontroleerd: 4e in Serie A 2025/26 met 71 punten
(op de slotdag langs AC Milan), Sánchez (huur Chelsea) en Kean (huur met koopplicht) op deadline day, 4-1 tegen
RB Leipzig op speeldag 1 (Douvikas scoorde), Fàbregas trainer, Stadio Giuseppe Sinigaglia.
  python3 specials/como_1907_serie_d_champions_league.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Van Serie D naar Champions League: dit is Como 1907, de tegenstander van Feyenoord"
SLUG = "como-1907-van-serie-d-naar-champions-league"
SAMENVATTING = ("Negen jaar geleden speelde Como nog op het vierde niveau, nu wacht Feyenoord in de Champions League. "
                "Het verhaal achter de opmars van Como 1907.")
RUBRIEK_ALGEMEEN = "6502b65d49bc032ba533e7a2"
CL = "65de4adac046f4488dfdebc2"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in koppen)
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}><thead><tr>{kop}</tr></thead><tbody>{body}</tbody></table>"


content = f"""<p><strong>In 2017 stond Como 1907 met lege handen. De club uit Noord-Italië was failliet en mocht niet meer meedoen in het profvoetbal. De herstart volgde in de Serie D, het vierde niveau van Italië. Negen jaar later speelt <a href="/clubs/como">Como</a> in de Champions League en woensdag 14 oktober om 18:45 uur is <a href="/clubs/feyenoord">Feyenoord</a> de tegenstander in De Kuip. Dit is het verhaal van een van de snelste opmarsen in het Europese voetbal.</strong></p>
<h3><strong>Como 1907 in het kort</strong></h3>
{tabel(["", ""], [
    ("<strong>Opgericht</strong>", "1907"),
    ("<strong>Stad</strong>", "Como, aan het Comomeer (Lombardije)"),
    ("<strong>Stadion</strong>", "Stadio Giuseppe Sinigaglia"),
    ("<strong>Eigenaar</strong>", "SENT Entertainment (sinds april 2019)"),
    ("<strong>Trainer</strong>", "Cesc Fàbregas"),
    ("<strong>Serie A 2025/26</strong>", "4e plaats, 71 punten uit 38 wedstrijden"),
    ("<strong>Champions League</strong>", "Debuut in 2026/27, 4-1 winst op RB Leipzig in de eerste speelronde"),
    ("<strong>Volgende wedstrijd</strong>", "Feyenoord – Como, woensdag 14 oktober, 18:45 uur, De Kuip"),
])}
<h3><strong>Van faillissement naar de Serie D</strong></h3>
<p>Como is een oude club met een rijke geschiedenis. De Lombarden speelden in het verleden meerdere seizoenen in de Serie A, de laatste keer in 2002/03. Daarna ging het bergafwaarts. Degradaties volgden elkaar op en de financiële problemen werden steeds groter, tot de club failliet ging. Een nieuwe eigenaar nam het over, maar Como werd niet toegelaten tot het profvoetbal. In de zomer van 2017 begon de club daarom opnieuw, in de Serie D.</p>
<p>Voor een club die ooit tegen Juventus, Milan en Inter speelde, was dat een harde val. Het was tegelijk het startpunt van een opmerkelijke wederopstanding.</p>
<h3><strong>De nieuwe eigenaar en een razendsnelle opmars</strong></h3>
<p>Het keerpunt kwam in april 2019. SENT Entertainment, in handen van de Indonesische familie Hartono, nam de club over. De nieuwe eigenaren investeerden niet alleen in de selectie, maar ook in de organisatie, de jeugdopleiding en de faciliteiten. Het effect was direct zichtbaar:</p>
{tabel(["Seizoen", "Competitie", "Resultaat"], [
    ("2018/19", "Serie D", "Kampioen, promotie naar de Serie C"),
    ("2020/21", "Serie C", "Kampioen, promotie naar de Serie B"),
    ("2023/24", "Serie B", "2e plaats, rechtstreekse promotie naar de Serie A"),
    ("2024/25", "Serie A", "Handhaving in het eerste seizoen terug"),
    ("2025/26", "Serie A", "4e met 71 punten, plaatsing voor de Champions League"),
])}
<p>Met de promotie in 2024 keerde Como voor het eerst sinds 2003 terug in de <a href="/competities/serie-a">Serie A</a>. Het bleek geen kort bezoek. In 2025/26 eindigde de ploeg als vierde, na een slotdag waarop Como nog langs AC Milan ging. Dat leverde een ticket voor de Champions League op, voor het eerst in de clubgeschiedenis.</p>"""

content2 = """<h3><strong>Cesc Fàbregas aan het roer</strong></h3>
<p>Het gezicht van het nieuwe Como is Cesc Fàbregas. De Spaanse oud-middenvelder, die furore maakte bij Arsenal, FC Barcelona en Chelsea en wereldkampioen werd met Spanje, sloot zijn spelerscarrière af bij Como. Daarna stapte hij over naar de technische staf en inmiddels is hij hoofdtrainer. Onder Fàbregas speelt Como verzorgd, aanvallend voetbal met veel balbezit, een stijl die eerder doet denken aan een Spaanse topclub dan aan een gepromoveerde Italiaanse ploeg.</p>
<p>De selectie is internationaal samengesteld. Bekende namen zijn:</p>
<ul><li><strong>Nico Paz</strong>: het Argentijnse talent is de creatieve motor van het elftal.</li><li><strong>Tasos Douvikas</strong>: de Griekse spits scoorde al in de Champions League, tegen RB Leipzig.</li><li><strong>Moise Kean</strong>: de Italiaanse international kwam deze zomer op huurbasis, met een verplichting tot koop.</li><li><strong>Robert Sánchez</strong>: de Spaanse doelman werd op de laatste transferdag een seizoen gehuurd van Chelsea.</li></ul>
<p>Fàbregas waarschuwde zelf al dat zijn ploeg in Europa een smalle selectie heeft. Door de regels van de UEFA voor de spelerslijst kan hij in de Champions League maar met een beperkte groep spelers werken. In de eerste speelronde was daar weinig van te merken: Como versloeg RB Leipzig met 4-1.</p>
<h3><strong>Meer dan een club met een mooi uitzicht</strong></h3>
<p>Como speelt in het Stadio Giuseppe Sinigaglia, een stadion dat direct aan het wereldberoemde Comomeer ligt. Die ligging geeft de club een internationale uitstraling, en de eigenaren spelen daar bewust op in. Toch is de grootste verandering sportief. Como is niet langer alleen een club met een prachtig decor en een turbulent verleden. Het is een serieuze Champions League-ploeg geworden.</p>
<h3><strong>Wat betekent dit voor Feyenoord?</strong></h3>
<p>Voor Feyenoord is Como een lastige tegenstander om in te schatten. De Italianen hebben geen lange Europese traditie, maar wel een sterk elftal met een duidelijke speelstijl en een trainer die weet wat er op het hoogste niveau nodig is. De 4-1 tegen RB Leipzig liet zien dat Como zich niet laat intimideren door grotere namen.</p>
<p>Woensdag in De Kuip moet blijken hoe ver de opmars van Como al is gekomen. Feyenoord heeft het thuispubliek mee en kan de onervarenheid van de Italianen in Europa misschien uitbuiten. Dat het geen makkelijke avond wordt, staat wel vast.</p>"""

content3 = """<h3><strong>Feyenoord – Como live kijken</strong></h3>
<p>Feyenoord – Como begint woensdag 14 oktober om 18:45 uur en is in Nederland te zien bij <a href="/zenders/ziggo-sport">Ziggo Sport</a>. Omdat het om een Europese wedstrijd van een Nederlandse club gaat, kun je ook zonder Ziggo-abonnement gratis kijken via Ziggo Sport Free, in de Ziggo GO-app of op ziggogo.tv. Alle wedstrijden, zenders en aftraptijden van deze week vind je in ons overzicht <a href="/nieuws/champions-league-speelronde-2-op-tv-13-oktober-2026">Champions League speelronde 2 op tv</a>.</p>
<h3><strong>Veelgestelde vragen over Como 1907</strong></h3>
<p><strong>Wanneer speelt Feyenoord tegen Como?</strong><br>Woensdag 14 oktober 2026 om 18:45 uur, in De Kuip in Rotterdam.</p>
<p><strong>Waarom speelde Como in de Serie D?</strong><br>De club ging failliet en werd niet toegelaten tot het profvoetbal. In 2017 begon Como daarom opnieuw op het vierde niveau van Italië.</p>
<p><strong>Wie is de eigenaar van Como?</strong><br>SENT Entertainment, van de Indonesische familie Hartono. Zij namen de club in april 2019 over.</p>
<p><strong>Wie is de trainer van Como?</strong><br>Cesc Fàbregas, de oud-middenvelder van Arsenal, FC Barcelona en Chelsea, die zijn spelerscarrière bij Como afsloot.</p>
<p><strong>Hoe plaatste Como zich voor de Champions League?</strong><br>Door in 2025/26 als vierde te eindigen in de Serie A, met 71 punten. Op de laatste speeldag ging Como nog langs AC Milan.</p>
<p><strong>Waar speelt Como zijn thuiswedstrijden?</strong><br>In het Stadio Giuseppe Sinigaglia, aan het Comomeer.</p>
<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_ALGEMEEN, "competitie": CL,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting"); sys.exit()
    print("item:", WF.create_live(fd))
