# -*- coding: utf-8 -*-
"""Los artikel: Prijzengeld Shanghai Masters 2026 (officiële ATP-bedragen in USD, omgerekend tegen ±0,89).
  python3 specials/prijzengeld_shanghai_2026.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Prijzengeld Shanghai Masters 2026: bedragen per ronde"
SLUG = "prijzengeld-shanghai-masters-2026"
SAMENVATTING = ("Prijzengeld Shanghai Masters 2026: in totaal $9,4 miljoen (± €8,4 miljoen). De winnaar krijgt ± €1,02 "
                "miljoen. Alle bedragen per ronde.")
RUBRIEK_SHANGHAI = "68dd97a028b74cf1f3a2b0cb"
COMPETITIE_SHANGHAI = "68dd97842e3621da54985d13"
KOERS = 0.89
WEDTIPS = "/nieuws/atp-shanghai-wedtips-voorspellingen-vrijdag-9-oktober-2026"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
THR = 'style="text-align:right;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'
TDR = 'style="text-align:right;padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def usd(x):
    return "$ " + f"{x:,}".replace(",", ".")


def eur(x):
    return "€ " + f"{round(x * KOERS):,}".replace(",", ".")


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH if i == 0 else THR}>{k}</th>" for i, k in enumerate(koppen))
    body = "".join("<tr>" + "".join(f"<td {TD if i == 0 else TDR}>{c}</td>" for i, c in enumerate(r)) + "</tr>"
                   for r in rijen)
    return f"<table {T}><thead><tr>{kop}</tr></thead><tbody>{body}</tbody></table>"


ENKEL = [("Winnaar", 1151380, "1.000"), ("Finalist", 612340, "650"), ("Halve finale", 340190, "400"),
         ("Kwartfinale", 193645, "200"), ("Vierde ronde (laatste 16)", 105720, "100"),
         ("Derde ronde (laatste 32)", 61865, "50"), ("Tweede ronde (laatste 64)", 36110, "30"),
         ("Eerste ronde (laatste 96)", 23760, "10")]
DUBBEL = [("Winnaars", 468200, "1.000"), ("Finalisten", 247870, "600"), ("Halve finale", 133110, "360"),
          ("Kwartfinale", 66570, "180"), ("Tweede ronde", 35700, "90"), ("Eerste ronde", 19510, "0")]
KWALI = [("Tweede kwalificatieronde", 14130), ("Eerste kwalificatieronde", 7330)]
JAREN = [("2023", 8800000, 1262220), ("2024", 8995555, 1100000), ("2025", 9193540, 1124380),
         ("2026", 9415725, 1151380)]

content = f"""<p><strong>Op de Shanghai Masters 2026 wordt in totaal $ 9.415.725 aan prijzengeld verdeeld, omgerekend ongeveer € 8,4 miljoen. De winnaar van het enkelspel krijgt $ 1.151.380 (± € 1,02 miljoen) en 1.000 ATP-punten. Wie in de eerste ronde verliest, gaat nog altijd met $ 23.760 (± € 21.000) naar huis.</strong></p>
<p>De Rolex Shanghai Masters is het laatste ATP Masters 1000-toernooi in Azië en wordt van 7 tot en met 18 oktober 2026 gespeeld op de hardcourtbanen van het Qi Zhong Tennis Center. Hieronder zie je per ronde hoeveel prijzengeld en hoeveel rankingpunten er te verdienen zijn, voor het enkelspel, het dubbelspel en de kwalificatie, plus hoe de prijzenpot zich de afgelopen jaren ontwikkelde.</p>
<h3><strong>Prijzengeld Shanghai Masters 2026 in het kort</strong></h3>
<ul><li><strong>Totale prijzenpot:</strong> {usd(9415725)} (± € 8,38 miljoen)</li><li><strong>Winnaar enkelspel:</strong> {usd(1151380)} (± € 1,02 miljoen) en 1.000 punten</li><li><strong>Verliezend finalist:</strong> {usd(612340)} (± € 545.000) en 650 punten</li><li><strong>Eerste ronde:</strong> {usd(23760)} (± € 21.000) en 10 punten</li><li><strong>Winnaars dubbelspel:</strong> {usd(468200)} per team</li><li><strong>Stijging ten opzichte van 2025:</strong> ongeveer 2,4 procent</li></ul>
<h3><strong>Prijzengeld enkelspel per ronde</strong></h3>
<p>Het hoofdtoernooi telt 96 spelers. De 32 hoogst geplaatste spelers krijgen een bye en stromen in de tweede ronde in. Het bedrag per ronde is wat een speler ontvangt als hij in die ronde uitgeschakeld wordt; de winnaar krijgt het bedrag van de bovenste rij.</p>
{tabel(["Ronde", "Prijzengeld (USD)", "Omgerekend (EUR)", "ATP-punten"], [(r, usd(b), eur(b), p) for r, b, p in ENKEL])}
<p><em>De ATP maakt het prijzengeld bekend in Amerikaanse dollars. De bedragen in euro zijn omgerekend tegen een koers van ongeveer € 0,89 per dollar en dus een indicatie.</em></p>"""

content2 = f"""<h3><strong>Wat verdient de winnaar van de Shanghai Masters 2026?</strong></h3>
<p>De kampioen van het enkelspel ontvangt {usd(1151380)}, omgerekend ruim € 1,02 miljoen. Dat is $ 27.000 meer dan vorig jaar, toen de Monegask Valentin Vacherot als qualifier het toernooi won door in de finale zijn neef Arthur Rinderknech te verslaan (4-6, 6-3, 6-3). Vacherot kreeg in 2025 nog $ 1.124.380.</p>
<p>Opvallend is hoe groot het verschil tussen winnen en verliezen in de laatste rondes is. De verliezend finalist krijgt met {usd(612340)} iets meer dan de helft van het bedrag van de winnaar. Een plek in de halve finale levert {usd(340190)} op, en wie de kwartfinale haalt, verdient {usd(193645)}. Bij de punten is het verschil nog groter: de winnaar pakt 1.000 punten, de finalist 650.</p>
<h3><strong>Prijzengeld dubbelspel</strong></h3>
<p>In het dubbelspel spelen 32 teams. De bedragen hieronder gelden per team en worden dus verdeeld over de twee spelers. In 2025 wonnen de Duitsers Kevin Krawietz en Tim Pütz het dubbelspel.</p>
{tabel(["Ronde", "Per team (USD)", "Omgerekend (EUR)", "ATP-punten"], [(r, usd(b), eur(b), p) for r, b, p in DUBBEL])}
<h3><strong>Prijzengeld kwalificatie</strong></h3>
<p>Ook spelers die zich via de kwalificatie proberen te plaatsen voor het hoofdtoernooi, verdienen geld. Wie in de laatste kwalificatieronde strandt, krijgt {usd(14130)}; verlies in de eerste ronde levert {usd(7330)} op. Plaatst een speler zich wel, dan krijgt hij minimaal het prijzengeld van de eerste ronde van het hoofdtoernooi.</p>
{tabel(["Ronde", "Prijzengeld (USD)", "Omgerekend (EUR)"], [(r, usd(b), eur(b)) for r, b in KWALI])}
<h3><strong>Zo groeide het prijzengeld van de Shanghai Masters</strong></h3>
<p>De totale prijzenpot stijgt al jaren in kleine stappen. Het bedrag voor de winnaar beweegt minder gelijkmatig mee: in 2023 kreeg de kampioen met $ 1.262.220 zelfs meer dan in 2026, terwijl de totale prijzenpot toen lager was.</p>
{tabel(["Jaar", "Totale prijzenpot (USD)", "Winnaar enkelspel (USD)"], [(j, usd(t), usd(w)) for j, t, w in JAREN])}
<h3><strong>Hoe werkt het prijzengeld bij een Masters 1000-toernooi?</strong></h3>
<p>Een speler krijgt het bedrag van de ronde waarin hij wordt uitgeschakeld; de bedragen tellen niet bij elkaar op. Het zijn brutobedragen. Van het prijzengeld betalen spelers onder meer hun reis, hun hotel en hun begeleiding, zoals coach en fysiotherapeut. Daarnaast kan er in het land van het toernooi belasting worden ingehouden.</p>
<p>Naast het geld gaat het om rankingpunten. Een Masters 1000 is na de Grand Slams de belangrijkste categorie in het tennis. In oktober telt elk punt extra, omdat de top acht van de race zich plaatst voor de ATP Finals in Turijn.</p>"""

content3 = f"""<h3><strong>Shanghai Masters live kijken</strong></h3>
<p>In Nederland zendt <a href="/zenders/ziggo-sport">Ziggo Sport</a> geselecteerde wedstrijden uit, op Ziggo Sport, Ziggo Sport 4 en Ziggo Sport 5. Wil je meer banen volgen, dan streamt Bet365 veel wedstrijden van het toernooi voor spelers met een gestort account (18+). Onze voorspellingen voor de wedstrijden van vandaag lees je in de <a href="{WEDTIPS}">ATP Shanghai wedtips van vrijdag 9 oktober</a>.</p>
<h3><strong>Veelgestelde vragen over het prijzengeld</strong></h3>
<p><strong>Hoeveel prijzengeld is er op de Shanghai Masters 2026?</strong><br>In totaal $ 9.415.725, omgerekend ongeveer € 8,4 miljoen. Dat is ruim 2 procent meer dan in 2025.</p>
<p><strong>Wat verdient de winnaar van de Shanghai Masters?</strong><br>De winnaar van het enkelspel krijgt $ 1.151.380, omgerekend ongeveer € 1,02 miljoen, en 1.000 ATP-punten.</p>
<p><strong>Wat krijgt een speler die in de eerste ronde verliest?</strong><br>$ 23.760, omgerekend ongeveer € 21.000, en 10 ATP-punten.</p>
<p><strong>Hoeveel krijgen de winnaars van het dubbelspel?</strong><br>$ 468.200 per team, dus ongeveer $ 234.100 per speler, plus 1.000 punten elk.</p>
<p><strong>Wie won de Shanghai Masters in 2025?</strong><br>Valentin Vacherot uit Monaco. Hij begon als qualifier en versloeg in de finale Arthur Rinderknech.</p>
<p><strong>Wanneer wordt de Shanghai Masters 2026 gespeeld?</strong><br>Van 7 tot en met 18 oktober 2026 in het Qi Zhong Tennis Center in Shanghai.</p>
<p><em>Gokken is alleen toegestaan voor personen van 18 jaar en ouder. Wat kost gokken jou? Stop op tijd. 18+</em></p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_SHANGHAI, "competitie": COMPETITIE_SHANGHAI,
          "tennis": True, "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting"); sys.exit()
    print("item:", WF.create_live(fd))
