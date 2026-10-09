# -*- coding: utf-8 -*-
"""Los artikel: Johan Cruijff Legacy Match Ajax Legends – Barça Legends (15 nov 2026).
Feiten: aankondiging ajax.nl (9 okt 2026) en ticketpagina ajax.nl/legends.
  python3 specials/cruijff_legacy_match_2026.py [--live]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import lk_webflow as WF

TITEL = "Johan Cruijff Legacy Match tussen Ajax en Barcelona: datum, spelers, tickets en waar je kunt kijken"
SLUG = "johan-cruijff-legacy-match-ajax-barcelona"
SAMENVATTING = ("Op 15 november 2026 spelen legends van Ajax en Barcelona de Johan Cruijff Legacy Match in de ArenA. "
                "Alles over spelers, tickets en tv.")
RUBRIEK_NIEUWS = "651be5190a7dba016817ccf0"

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in koppen)
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}><thead><tr>{kop}</tr></thead><tbody>{body}</tbody></table>"


content = f"""<p><strong>Ajax en FC Barcelona eren Johan Cruijff op zondag 15 november 2026 met de Johan Cruijff Legacy Match. In de Johan Cruijff ArenA nemen oud-spelers van beide clubs het tegen elkaar op, met onder meer Patrick Kluivert, Jari Litmanen en de broers De Boer. De aftrap is om 14:30 uur, Ziggo Sport zendt de wedstrijd live uit en tickets zijn er vanaf €18. De volledige opbrengst gaat naar de Johan Cruyff Foundation.</strong></p>
<p>Weinig voetballers hebben twee clubs zo diep beïnvloed als Johan Cruijff. Bij <a href="/clubs/ajax">Ajax</a> en <a href="/clubs/fc-barcelona">FC Barcelona</a> is zijn manier van denken over voetbal nog altijd terug te zien, van de jeugdopleiding tot de speelstijl van het eerste elftal. Tien jaar na zijn overlijden brengen beide clubs hem een eerbetoon met een benefietwedstrijd in Amsterdam. Hieronder lees je alles over de datum, de deelnemers, de kaartverkoop en waar je de wedstrijd kunt zien.</p>
<h3><strong>De Legacy Match in het kort</strong></h3>
{tabel(["", ""], [
    ("<strong>Wedstrijd</strong>", "Ajax Legends – Barça Legends"),
    ("<strong>Datum</strong>", "Zondag 15 november 2026"),
    ("<strong>Aftrap</strong>", "14:30 uur"),
    ("<strong>Stadion</strong>", "Johan Cruijff ArenA, Amsterdam"),
    ("<strong>Live op tv</strong>", '<a href="/zenders/ziggo-sport">Ziggo Sport</a>'),
    ("<strong>Tickets</strong>", "Vanaf €18, via Ajax"),
    ("<strong>Goed doel</strong>", "Johan Cruyff Foundation"),
])}
<h3><strong>Waarom op 15 november?</strong></h3>
<p>De datum is niet toevallig gekozen. Op 15 november 1964 maakte de toen zeventienjarige Johan Cruijff zijn debuut in het eerste elftal van Ajax. Precies 62 jaar later staat de wedstrijd die zijn naam draagt op het programma. Bovendien is 2026 het jaar waarin het tien jaar geleden is dat Cruijff overleed: hij stierf op 24 maart 2016 in Barcelona.</p>"""

content2 = f"""<h3><strong>Welke spelers doen mee?</strong></h3>
<p>Ajax heeft de eerste negen namen bekendgemaakt. Vijf van hen kennen beide clubs van binnenuit: ze speelden zowel in Amsterdam als in Barcelona.</p>
{tabel(["Speler", "Ajax", "Barcelona"], [
    ("Patrick Kluivert", "Ja", "Ja"),
    ("Frank de Boer", "Ja", "Ja"),
    ("Ronald de Boer", "Ja", "Ja"),
    ("Jari Litmanen", "Ja", "Ja"),
    ("Richard Witschge", "Ja", "Ja"),
    ("Edwin van der Sar", "Ja", "Nee"),
    ("Wesley Sneijder", "Ja", "Nee"),
    ("Siem de Jong", "Ja", "Nee"),
    ("Jan Vertonghen", "Ja", "Nee"),
])}
<p>Vooral het rijtje spelers met twee clubs springt eruit. <strong>Patrick Kluivert</strong> maakte als tiener het winnende doelpunt in de Champions League-finale van 1995 en werd daarna jarenlang de spits van Barcelona. <strong>Frank en Ronald de Boer</strong> maakten de stap naar Catalonië samen. Ook <strong>Jari Litmanen</strong>, die bij Ajax uitgroeide tot een van de beste buitenlanders uit de clubgeschiedenis, speelde later in Barcelona. <strong>Richard Witschge</strong> is de speler met de meest directe band met Cruijff in dit gezelschap: hij speelde begin jaren negentig onder Cruijff als trainer bij Barcelona.</p>
<p>Daarnaast komen er vier Ajacieden in actie die alleen voor de Amsterdammers speelden. Doelman <strong>Edwin van der Sar</strong> won met Ajax de Champions League in 1995. <strong>Wesley Sneijder</strong> en <strong>Siem de Jong</strong> kwamen uit de eigen jeugdopleiding, en de Belg <strong>Jan Vertonghen</strong> was jarenlang een vaste waarde in de Ajax-defensie.</p>
<p>De selectie is nog niet compleet. Ajax en Barcelona maken de komende weken meer Legends bekend, ook aan Spaanse kant. Zodra de namen van de Barça Legends bekend zijn, is ook duidelijk welke oud-ploeggenoten elkaar in de ArenA weer tegenkomen.</p>
<h3><strong>Cruijff: icoon van twee clubs</strong></h3>
<p>Als speler werd Cruijff bij Ajax groot. Hij won met de club drie keer op rij de Europa Cup I (1971, 1972 en 1973) en verkaste daarna naar Barcelona, waar hij in zijn eerste seizoen direct kampioen werd. Hij won drie keer de Ballon d'Or.</p>
<p>Als trainer liet hij misschien nog wel een grotere erfenis achter. Bij Ajax won hij in 1987 de Europacup II. Bij Barcelona bouwde hij aan het 'Dream Team', dat in 1992 op Wembley voor het eerst de Europa Cup I naar Catalonië haalde. Zijn ideeën over positiespel, aanvallend voetbal en het opleiden van eigen talent zijn bij beide clubs nog altijd de basis.</p>
<p>Dat zie je ook terug in de gebouwen. Het stadion van Ajax heet sinds 2018 de Johan Cruijff ArenA, en op het trainingscomplex van Barcelona speelt het tweede elftal in het Estadi Johan Cruyff.</p>"""

content3 = f"""<h3><strong>Tickets voor de Johan Cruijff Legacy Match</strong></h3>
<p>Kaarten zijn verkrijgbaar vanaf €18 en worden verkocht via Ajax. De verkoop gaat in fases, waarbij trouwe supporters voorrang krijgen:</p>
{tabel(["Fase", "Voor wie", "Wanneer"], [
    ("1", "Seizoenkaarthouders van Ajax (max. 10 kaarten)", "Vrijdag 9 t/m zondag 11 oktober"),
    ("2", "Leden van de Supportersvereniging Ajax (max. 10 kaarten)", "Maandag 12 oktober, vanaf 10:00 uur"),
    ("3", "Houders van een Ajax Club Card", "Dinsdag 13 oktober"),
    ("4", "Alle fans met een geverifieerd Ajax-account", "Aansluitend in de vrije verkoop"),
])}
<p>Eerst gaat de eerste ring van het stadion in de verkoop. Is die uitverkocht, dan volgt de tweede ring. De kaarten zijn mobiele tickets in de Ajax-app en staan daar uiterlijk een week voor de wedstrijd klaar. Je kunt ze in de app met maximaal drie andere fans delen. Heb je nog geen account, dan maak je gratis een account aan bij mijn.AJAX.</p>
<h3><strong>Waar kun je de Legacy Match kijken?</strong></h3>
<p>Geen kaartje? De Johan Cruijff Legacy Match is live te zien bij <a href="/zenders/ziggo-sport">Ziggo Sport</a>. Welke voetbalwedstrijden er verder op tv zijn, lees je in ons <a href="/nieuws/sportzenders-kanaalnummers">overzicht van sportzenders en kanaalnummers</a>.</p>
<h3><strong>Waar gaat de opbrengst naartoe?</strong></h3>
<p>Alle inkomsten van de wedstrijd gaan naar de Johan Cruyff Foundation. Cruijff richtte de stichting in 1997 zelf op. Zijn idee: ieder kind moet de ruimte krijgen om te sporten en te bewegen. De foundation legt over de hele wereld Cruyff Courts aan, kleine voetbalveldjes in wijken, en steunt sportprojecten voor kinderen voor wie sporten niet vanzelf spreekt, bijvoorbeeld vanwege een beperking of de omgeving waarin ze opgroeien.</p>
<h3><strong>Veelgestelde vragen</strong></h3>
<p><strong>Wanneer is de Johan Cruijff Legacy Match?</strong><br>Op zondag 15 november 2026 om 14:30 uur in de Johan Cruijff ArenA.</p>
<p><strong>Wie spelen er mee?</strong><br>Onder anderen Patrick Kluivert, Frank en Ronald de Boer, Jari Litmanen, Richard Witschge, Edwin van der Sar, Wesley Sneijder, Siem de Jong en Jan Vertonghen. Meer namen volgen.</p>
<p><strong>Wat kosten de tickets?</strong><br>Tickets zijn er vanaf €18. Seizoenkaarthouders, leden van de supportersvereniging en Club Card-houders krijgen voorrang.</p>
<p><strong>Op welke zender is de wedstrijd te zien?</strong><br>Ziggo Sport zendt de Legacy Match live uit.</p>
<p><strong>Waarom wordt de wedstrijd op 15 november gespeeld?</strong><br>Op die datum debuteerde Johan Cruijff in 1964 in het eerste elftal van Ajax.</p>
<p><strong>Waar gaat het geld naartoe?</strong><br>De volledige opbrengst gaat naar de Johan Cruyff Foundation, die wereldwijd Cruyff Courts en sportprojecten voor kinderen realiseert.</p>"""

if __name__ == "__main__":
    from datetime import datetime, timezone
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-2": content2, "content-3": content3,
          "samenvatting": SAMENVATTING, "rubriek": RUBRIEK_NIEUWS,
          "publicatiedatum": datetime.now(timezone.utc).isoformat()}
    if "--live" not in sys.argv:
        print(len(SAMENVATTING), "tekens samenvatting"); sys.exit()
    print("item:", WF.create_live(fd))
