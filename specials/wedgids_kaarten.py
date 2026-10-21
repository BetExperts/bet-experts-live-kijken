# -*- coding: utf-8 -*-
"""Maatwerk-deelkaarten voor wedgids-artikelen zonder afbeelding (21-10-2026).
Rendert via og_kaarten/strategie.render_objs -> og/nieuws/wedgids-<key>.webp, pusht naar GitHub en zet
'afbeelding' + 'seo-afbeelding' (live items: update_live; concepten: alleen staged).
  ../superodd-agent/.venv/bin/python specials/wedgids_kaarten.py [--live]"""
import os, sys, json, re, time, subprocess, urllib.request
from types import SimpleNamespace as K
HIER = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HIER, "..")
sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(ROOT, "og_kaarten"))
import lk_webflow as WF

RAW = "https://raw.githubusercontent.com/BetExperts/bet-experts-live-kijken/main/og/nieuws/"

# slug -> kaart (key = korte bestandsnaam)
KAARTEN = {
 "definities-voor-wedden-op-sport-sportweddenschappenwoordenboek-alle-wedtermen-van-a-tot-z-uitgelegd":
   ("wedtermen", K(OG_KOP="Alle <span>wedtermen</span> van A tot Z", OG_EYEBROW="Woordenboek", OG_CHIPS=["Van accu tot value bet", "Uitleg per begrip"], OG_MOTIEF="lijst", OG_DATA=["Accumulator · combi", "Handicap · voorsprong", "Odds · quotering", "Value bet · waarde"])),
 "nhl-wat-zijn-punten-en-hoe-werkt-wedden-op-spelerspunten":
   ("nhl-punten", K(OG_KOP="NHL: wat zijn <span>punten</span>?", OG_EYEBROW="IJshockey", OG_CHIPS=["Goal + assist", "Spelerspunten wedden"], OG_MOTIEF="tabel", OG_DATA=["Doelpunt · 1 punt", "Assist · 1 punt", "Goal + assist · 2 punten"])),
 "wat-is-de-money-line-weddenschap-eenvoudige-uitleg-voor-beginners":
   ("money-line", K(OG_KOP="Wat is de <span>money line</span>?", OG_EYEBROW="Wedden uitgelegd", OG_CHIPS=["Wie wint de wedstrijd?", "Voor beginners"], OG_MOTIEF="odds", OG_DATA=["Favoriet · 1,65", "Underdog · 2,30"])),
 "wat-is-een-flagrant-fout-flagrant-foul-in-de-nba-uitleg-en-gevolgen":
   ("flagrant-foul", K(OG_KOP="Wat is een <span>flagrant foul</span>?", OG_EYEBROW="Basketbal", OG_CHIPS=["Flagrant 1 en 2", "NBA-regels"], OG_MOTIEF="lijst", OG_DATA=["Flagrant 1 · 2 vrije worpen + bal", "Flagrant 2 · idem + uitsluiting"])),
 "belangrijkste-regels-in-de-nba-uitgelegd-de-basis-voor-basketbalfans-en-wedders":
   ("nba-regels", K(OG_KOP="De belangrijkste <span>NBA</span>-regels", OG_EYEBROW="Basketbal", OG_CHIPS=["4 × 12 minuten", "Shotclock 24 seconden"], OG_MOTIEF="tabel", OG_DATA=["Speeltijd · 4 × 12 min", "Shotclock · 24 sec", "Verlenging · 5 min", "Persoonlijke fouten · 6 = eruit"])),
 "belangrijkste-regels-in-de-nhl-uitgelegd-de-basis-voor-ijshockeyfans-en-wedders":
   ("nhl-regels", K(OG_KOP="De belangrijkste <span>NHL</span>-regels", OG_EYEBROW="IJshockey", OG_CHIPS=["3 × 20 minuten", "Overtime en shootout"], OG_MOTIEF="tabel", OG_DATA=["Speeltijd · 3 × 20 min", "Overtime · 5 min, 3 tegen 3", "Daarna · shootout"])),
 "hoe-lang-duurt-een-nhl-wedstrijd-in-de-praktijk":
   ("nhl-duur", K(OG_KOP="Hoe lang duurt een <span>NHL</span>-wedstrijd?", OG_EYEBROW="IJshockey", OG_CHIPS=["60 minuten speeltijd", "Ruim 2 uur in de praktijk"], OG_MOTIEF="tabel", OG_DATA=["Speeltijd · 3 × 20 min", "Pauzes · 2", "In de praktijk · ± 2,5 uur"])),
 "hoe-lang-duurt-een-american-football-wedstrijd-officiele-totale-duur":
   ("american-football-duur", K(OG_KOP="Hoe lang duurt <span>American football</span>?", OG_EYEBROW="Sport uitgelegd", OG_CHIPS=["4 × 15 minuten", "± 3 uur in de praktijk"], OG_MOTIEF="tabel", OG_DATA=["Speeltijd · 4 × 15 min", "In de praktijk · ± 3 uur"])),
 "wat-is-een-trixie-weddenschap-eigenlijk":
   ("trixie", K(OG_KOP="Wat is een <span>Trixie</span>?", OG_EYEBROW="Systeemwedden", OG_CHIPS=["3 selecties", "4 weddenschappen"], OG_MOTIEF="tabel", OG_DATA=["Dubbels · 3", "Treble · 1", "Totaal · 4 bets"])),
 "wat-betekent-ongeldig-bij-gelijkspel":
   ("draw-no-bet", K(OG_KOP="Wat is <span>ongeldig bij gelijkspel</span>?", OG_EYEBROW="Draw no bet", OG_CHIPS=["Gelijk = inzet terug", "Net als Asian 0"], OG_MOTIEF="tabel", OG_DATA=["Je team wint · winst", "Gelijkspel · inzet terug", "Je team verliest · verlies"])),
 "vroege-uitbetaling-bet365---dit-is-hoe-het-werkt":
   ("vroege-uitbetaling", K(OG_KOP="Vroege <span>uitbetaling</span> uitgelegd", OG_EYEBROW="Wedden uitgelegd", OG_CHIPS=["2 goals voorsprong", "Direct uitbetaald"], OG_MOTIEF="lijst", OG_DATA=["Je team staat 2 goals voor", "Je weddenschap telt als gewonnen", "Ook als het nog misgaat"])),
 "dit-zijn-de-nieuwe-beleidsregels-voor-online-casinos-vanaf-juni-2024":
   ("beleidsregels-casino", K(OG_KOP="Nieuwe <span>regels</span> voor online casino's", OG_EYEBROW="Legaal gokken", OG_CHIPS=["Beleidsregels 2024", "Wat er verandert"], OG_MOTIEF="lijst", OG_DATA=["Stortingslimieten", "Controle op speelgedrag", "Extra bescherming jongeren"])),
 "dit-is-wat-casinos-doen-met-jouw-gegevens":
   ("casino-gegevens", K(OG_KOP="Wat doen casino's met je <span>gegevens</span>?", OG_EYEBROW="Privacy", OG_CHIPS=["Identiteitscheck", "Cruks-controle"], OG_MOTIEF="lijst", OG_DATA=["Identiteit controleren", "Cruks raadplegen", "Speelgedrag volgen"])),
 "is-gokken-haram":
   ("gokken-haram", K(OG_KOP="Is gokken <span>haram</span>?", OG_EYEBROW="Geloof en gokken", OG_CHIPS=["Uitleg", "Bewust kiezen"], OG_MOTIEF="lijst", OG_DATA=["Wat zegt de islam?", "Wedden, loterij en casino", "Hulp bij twijfel"])),
 "wedden-op-voetbal-met-ideal":
   ("ideal", K(OG_KOP="Wedden met <span>iDEAL</span>", OG_EYEBROW="Betalen", OG_CHIPS=["Direct storten", "Bij legale bookmakers"], OG_MOTIEF="lijst", OG_DATA=["Kies iDEAL bij storten", "Bevestig in je bank-app", "Saldo staat er direct"])),
 "wat-is-een-superboost-of-superodd":
   ("superboost", K(OG_KOP="Wat is een <span>Super Boost</span>?", OG_EYEBROW="Odds boost", OG_CHIPS=["Verhoogde odds", "Vaak met maximale inzet"], OG_MOTIEF="odds", OG_DATA=["Met boost · 3,00", "Normaal · 2,00"])),
 "cruks-de-gokstop-voor-verantwoord-gokken":
   ("cruks", K(OG_KOP="Cruks: de <span>gokstop</span>", OG_EYEBROW="Verantwoord spelen", OG_CHIPS=["Minimaal 6 maanden", "Zelf aanmelden"], OG_MOTIEF="lijst", OG_DATA=["Uitsluiting · minimaal 6 maanden", "Geldt bij alle legale aanbieders", "Aanmelden met DigiD"])),
 "legale-goksites-in-nederland":
   ("legale-goksites", K(OG_KOP="Legale <span>goksites</span> in Nederland", OG_EYEBROW="Legaal gokken", OG_CHIPS=["Met Ksa-vergunning", "Zo check je het"], OG_MOTIEF="lijst", OG_DATA=["Vergunning van de Ksa", "Cruks-controle", "Netto stortingslimiet"])),
 "bij-welke-online-bookmakers-kan-je-storten-met-paysafecard":
   ("paysafecard", K(OG_KOP="Storten met <span>Paysafecard</span>", OG_EYEBROW="Betalen", OG_CHIPS=["Prepaid code", "Zonder bankrekening"], OG_MOTIEF="lijst", OG_DATA=["Koop een code", "Vul de 16 cijfers in", "Direct storten"])),
 "wat-gebeurd-er-met-een-weddenschap-als-een-speler-opgeeft-bij-een-tennis-weddenschap":
   ("tennis-opgave", K(OG_KOP="Speler geeft <span>op</span> bij tennis?", OG_EYEBROW="Tennis", OG_CHIPS=["Wat gebeurt er met je bet?", "Regels per bookmaker"], OG_MOTIEF="lijst", OG_DATA=["Voor de start · ongeldig", "Tijdens de partij · regels verschillen"])),
 "wedstrijd-gestaakt-wat-gebeurd-er-nu-met-je-weddenschap":
   ("wedstrijd-gestaakt", K(OG_KOP="Wedstrijd <span>gestaakt</span>?", OG_EYEBROW="Wedden uitgelegd", OG_CHIPS=["Wat gebeurt er met je bet?", "Regels per markt"], OG_MOTIEF="lijst", OG_DATA=["Uitkomst al bekend · telt", "Nog open · vaak ongeldig", "Lees de regels"])),
 "voorkomen-van-een-gokverslaving-belangrijke-stappen-en-hulpbronnen":
   ("gokverslaving", K(OG_KOP="Een <span>gokverslaving</span> voorkomen", OG_EYEBROW="Verantwoord spelen", OG_CHIPS=["Signalen herkennen", "Hulp en contact"], OG_MOTIEF="lijst", OG_DATA=["Stel limieten in", "Neem pauzes", "Praat erover"])),
 "systeem-wedden-wat-hoe-en-waarom":
   ("systeemwedden", K(OG_KOP="Wat is <span>systeemwedden</span>?", OG_EYEBROW="Wedden uitgelegd", OG_CHIPS=["Trixie, patent, yankee", "Niet alles hoeft goed"], OG_MOTIEF="tabel", OG_DATA=["Trixie · 4 bets", "Patent · 7 bets", "Yankee · 11 bets", "Lucky 15 · 15 bets"])),
}

if __name__ == "__main__":
    from strategie import render_objs
    items = {a["slug"]: a for a in json.load(open(sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else
             "/private/tmp/claude-501/-Users-jaspervandenboogaard-bet-experts/babcc36f-92bb-4f26-bb46-756c5c5e3a92/scratchpad/wedgids_items.json"))}
    doen = {s: v for s, v in KAARTEN.items() if s in items and not items[s]["img"]}
    print(len(doen), "kaarten")
    render_objs({k: m for k, m in doen.values()}, "wedgids")
    if "--live" not in sys.argv:
        sys.exit()
    subprocess.run("git add og/nieuws/wedgids-*.webp og_kaarten/strategie.py specials/wedgids_kaarten.py && git commit -qm 'Wedgids: deelkaarten' && "
                   "git stash -q; git pull -q --rebase; git push -q; git stash pop -q", shell=True, cwd=ROOT)
    for s, (k, m) in doen.items():
        url = RAW + f"wedgids-{k}.webp"
        for _ in range(20):
            try:
                if urllib.request.urlopen(url, timeout=20).status == 200: break
            except Exception: time.sleep(6)
        alt = re.sub(r"<[^>]+>", "", m.OG_KOP)
        fd = {"afbeelding": {"url": url, "alt": alt}, "seo-afbeelding": {"url": url, "alt": alt}}
        a = items[s]
        for p in range(4):
            try:
                if a["draft"]: WF._req("PATCH", f"{WF.WF_API}/collections/{WF.NIEUWS_COLLECTION}/items/{a['id']}", {"fieldData": fd}); print("staged", k)
                else: WF.update_live(a["id"], fd); print("live", k)
                break
            except Exception as e:
                if p == 3: print("FOUT", k, str(e)[:200])
                time.sleep(4)
