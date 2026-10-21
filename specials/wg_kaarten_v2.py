# -*- coding: utf-8 -*-
"""Deelkaarten v2 voor de herschreven wedgids-artikelen: kernfeiten uit het nieuwe artikel, echte bookmakerlogo's
(preview-images-agent/assets/bm) waar het over bookmakers gaat. Rendert og/nieuws/wedgids-<key>-v2.webp,
pusht en zet afbeelding + seo-afbeelding (live items; concepten worden door wg_publiceer.py gepubliceerd).
  ../superodd-agent/.venv/bin/python specials/wg_kaarten_v2.py <key> [...] [--live]"""
import os, sys, json, re, time, subprocess, urllib.request
from types import SimpleNamespace as K
HIER = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HIER, "..")
sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(ROOT, "og_kaarten"))
import lk_webflow as WF

RAW = "https://raw.githubusercontent.com/BetExperts/bet-experts-live-kijken/main/og/nieuws/"
ITEMS = "/private/tmp/claude-501/-Users-jaspervandenboogaard-bet-experts/babcc36f-92bb-4f26-bb46-756c5c5e3a92/scratchpad/wgoud/index.json"


def am(o):   # Amerikaanse odd -> decimaal, NL-notatie
    d = 1 + (o / 100 if o > 0 else 100 / -o)
    return f"{d:.2f}".replace(".", ",")


assert (am(-150), am(100), am(200), am(-200)) == ("1,67", "2,00", "3,00", "1,50")
# Trixie, 3 selecties @2,00, €1 per bet: 3 dubbels (€4) + treble (€8)
assert 3 * 1 * 2 * 2 + 1 * 2 * 2 * 2 == 20 and 1 * 2 * 2 == 4
# draw no bet uit 1X2: thuis 2,00 / gelijk 3,40 -> 2,00 × (1 − 1/3,40)
assert f"{2.00 * (1 - 1 / 3.40):.2f}" == "1.41"

V2 = {
 "money-line": K(OG_KOP="Wat is <span>money line</span> wedden?", OG_EYEBROW="Amerikaanse odds", OG_CHIPS=["Verlenging telt mee", "Omrekenen naar decimaal"], OG_MOTIEF="tabel",
                 OG_DATA=[f"−150 · {am(-150)}", f"+100 · {am(100)}", f"+200 · {am(200)}", f"−200 · {am(-200)}"]),
 "trixie": K(OG_KOP="Wat is een <span>Trixie</span>?", OG_EYEBROW="Systeemwedden", OG_CHIPS=["3 dubbels + 1 treble", "Voorbeeld: odds 2,00"], OG_MOTIEF="tabel",
             OG_DATA=["Inzet · 4 × €1", "3 goed · €20,00", "2 goed · €4,00", "1 goed · €0,00"]),
 "draw-no-bet": K(OG_KOP="Wat betekent <span>draw no bet</span>?", OG_EYEBROW="Ongeldig bij gelijkspel", OG_CHIPS=["Gelijk = inzet terug", "Zelf omrekenen uit 1X2"], OG_MOTIEF="odds",
                  OG_DATA=["Draw no bet thuis · 1,41", "1X2 thuis · 2,00", "Gelijkspel · 3,40"]),
 "vroege-uitbetaling": K(OG_KOP="Vroege <span>uitbetaling</span>: 2 goals voor", OG_EYEBROW="Early payout", OG_CHIPS=["Uitbetaald bij 2 goals voorsprong", "Ook als het misgaat"], OG_MOTIEF="logos",
                         OG_DATA=["bet365 · 2 goals voor", "unibet · 2UP", "toto · 2 Goals Up!", "BetCity · 2 goals voor"]),
 "superboost": K(OG_KOP="Wat is een <span>odds boost</span>?", OG_EYEBROW="Superboost en Super Odd", OG_CHIPS=["Verhoogde quotering", "Let op de maximale inzet"], OG_MOTIEF="logos",
                 OG_DATA=["bet365 · Super Boost", "unibet · Uniboost", "jacks · Superboost", "starcasino · Gouden Boost"]),
 "wedstrijd-gestaakt": K(OG_KOP="Wedstrijd <span>gestaakt</span>?", OG_EYEBROW="Termijn om te hervatten", OG_CHIPS=["Regels per bookmaker", "Wat telt al wel?"], OG_MOTIEF="logos",
                         OG_DATA=["toto · 2 dagen", "unibet · 12 uur", "BetCity · 12 uur"]),
 "tennis-opgave": K(OG_KOP="Tennisspeler geeft <span>op</span>?", OG_EYEBROW="Opgave na de eerste set", OG_CHIPS=["Walkover = ongeldig", "Regels per bookmaker"], OG_MOTIEF="logos",
                    OG_DATA=["toto · Winnaar ongeldig", "unibet · Doorgaande speler wint", "BetCity · Doorgaande speler wint"]),
}

V2.update({
 "nhl-duur": K(OG_KOP="Hoe lang duurt een <span>NHL</span>-wedstrijd?", OG_EYEBROW="IJshockey", OG_CHIPS=["60 minuten speeltijd", "In de praktijk ± 2,5 uur"], OG_MOTIEF="tabel",
               OG_DATA=["Speeltijd · 3 × 20 min", "Pauzes · 2 × 18 min", "Verlenging · 5 min", "Daarna · shootout"]),
 "nhl-punten": K(OG_KOP="Wat zijn <span>punten</span> in de NHL?", OG_EYEBROW="Spelerspunten", OG_CHIPS=["Goal + assist", "Tot 3 punten per doelpunt"], OG_MOTIEF="tabel",
                 OG_DATA=["Doelpunt · 1 punt", "Assist · 1 punt", "Assists per goal · max. 2", "Stand: winst · 2 punten"]),
 "american-football-duur": K(OG_KOP="Hoe lang duurt <span>American football</span>?", OG_EYEBROW="NFL", OG_CHIPS=["4 × 15 minuten", "Ruim 3 uur in de praktijk"], OG_MOTIEF="tabel",
                             OG_DATA=["Speeltijd · 4 × 15 min", "Rust · 13 min", "Verlenging · 10 min", "Play clock · 40 sec"]),
 "gokverslaving": K(OG_KOP="Een <span>gokverslaving</span> voorkomen", OG_EYEBROW="Verantwoord spelen", OG_CHIPS=["12 signalen herkennen", "Gratis hulp"], OG_MOTIEF="lijst",
                    OG_DATA=["Stel lage limieten in", "Speel nooit om verlies terug te winnen", "AGOG · 0800-22 777 22", "Gokstop · Cruks"]),
 "beleidsregels-casino": K(OG_KOP="Regels online <span>gokken</span> in 2026", OG_EYEBROW="Wat er veranderde", OG_CHIPS=["Stand oktober 2026", "Plannen kabinet"], OG_MOTIEF="tabel",
                           OG_DATA=["1-7-2023 · geen ongerichte reclame", "1-10-2024 · stortingsgrens", "1-7-2025 · sponsorverbod", "1-1-2026 · belasting 37,8%"]),
 "casino-gegevens": K(OG_KOP="Wat doen casino's met je <span>gegevens</span>?", OG_EYEBROW="Privacy en AVG", OG_CHIPS=["Verplicht bewaard", "Jouw rechten"], OG_MOTIEF="tabel",
                      OG_DATA=["BSN · direct vernietigd", "Speelprofiel · 3 jaar", "Inzet en winst · 7 jaar", "Wwft-dossier · 5 jaar"]),
 "gokken-haram": K(OG_KOP="Is gokken <span>haram</span>?", OG_EYEBROW="Islam en gokken", OG_CHIPS=["Maysir uitgelegd", "TOTO, loterij en casino"], OG_MOTIEF="lijst",
                   OG_DATA=["Wat is maysir?", "Wat zegt de Koran?", "TOTO, loterij en casino", "Twijfelgevallen"]),
})

V2.update({
 "paysafecard": K(OG_KOP="Bookmakers met <span>Paysafecard</span>", OG_EYEBROW="Betalen · stand oktober 2026", OG_CHIPS=["Alleen bet365 en Unibet", "Uitbetalen via de bank"], OG_MOTIEF="logos",
                  OG_DATA=["bet365 · €5 – €1.000", "unibet · €10 – €500", "Uitbetalen · altijd per bank"]),
 "ideal": K(OG_KOP="Bookmakers met <span>iDEAL</span>", OG_EYEBROW="iDEAL | Wero", OG_CHIPS=["Bij vrijwel alle legale bookmakers", "Overstap naar Wero"], OG_MOTIEF="logos",
            OG_DATA=["toto · iDEAL | Wero", "bet365 · €5 – €10.000", "unibet · iDEAL | Wero", "jacks · iDEAL | Wero"]),
 "legale-goksites": K(OG_KOP="Legale <span>goksites</span> in Nederland", OG_EYEBROW="Met Ksa-vergunning", OG_CHIPS=["Alle vergunninghouders", "Zo check je het"], OG_MOTIEF="tabel",
                      OG_DATA=["Vergunninghouders · 31", "Merken met sport · 23", "Merken met casino · 27", "Check · Kansspelwijzer"]),
})

V2.update({
 "tennis-opgave-hoofd": K(OG_KOP="TOTO tennis <span>opgave</span>: dit gebeurt", OG_EYEBROW="Tennis · regels per bookmaker", OG_CHIPS=["21 bookmakers vergeleken", "Met gratis pdf"], OG_MOTIEF="logos",
                          OG_DATA=["toto · Winnaar ongeldig", "bet365 · Winnaar ongeldig", "unibet · Doorgaande speler wint", "BetCity · Doorgaande speler wint"]),
})


def zet(keys, live):
    from strategie import render_objs
    idx = {r[0]: {"id": r[1], "draft": r[2] == "draft"} for r in json.load(open(ITEMS))}
    objs = {f"{k}-v2": V2[k] for k in keys}
    render_objs(objs, "wedgids")
    if not live:
        return
    subprocess.run("git add og/nieuws/wedgids-*-v2.webp og_kaarten/strategie.py specials/wg_kaarten_v2.py && git commit -qm 'Wedgids: deelkaarten v2' && "
                   "git stash -q; git pull -q --rebase; git push -q; git stash pop -q", shell=True, cwd=ROOT)
    for k in keys:
        url = RAW + f"wedgids-{k}-v2.webp"
        for _ in range(20):
            try:
                if urllib.request.urlopen(url, timeout=20).status == 200: break
            except Exception: time.sleep(6)
        alt = re.sub(r"<[^>]+>", "", V2[k].OG_KOP)
        fd = {"afbeelding": {"url": url, "alt": alt}, "seo-afbeelding": {"url": url, "alt": alt}}
        a = idx[k]
        for p in range(4):
            try:
                if a["draft"]: WF._req("PATCH", f"{WF.WF_API}/collections/{WF.NIEUWS_COLLECTION}/items/{a['id']}", {"fieldData": fd}); print("staged", k)
                else: WF.update_live(a["id"], fd); print("live", k)
                break
            except Exception as e:
                if p == 3: print("FOUT", k, str(e)[:200])
                time.sleep(4)


if __name__ == "__main__":
    zet([a for a in sys.argv[1:] if not a.startswith("--")], "--live" in sys.argv)
