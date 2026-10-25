# -*- coding: utf-8 -*-
"""Publiceert een NBA-vannacht-artikel (standaard specials/nba_vannacht_2026_10_22.py, of de module als eerste argument): deelkaart (og/nieuws/nieuws-<slug>.webp via GitHub raw), Nieuws-item live
(rubriek Basketball, competitie NBA, wedtip-velden). Maakt GEEN losse Wedtips-items aan (niet de bedoeling, Jasper 24-10-2026).
  set -a; . ../superodd-agent/.env; set +a; ../superodd-agent/.venv/bin/python specials/nba_vannacht_publiceer.py [nba_vannacht_2026_10_24] [--live]
Optioneel in de module: DATUM (eerste aanvang, ISO UTC), NAMEN en STAKE (per tip), anders de waarden hieronder."""
import os, sys, re, time, subprocess, urllib.request
from datetime import datetime, timezone
HIER = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HIER, "..")
sys.path.insert(0, ROOT); sys.path.insert(0, HIER); sys.path.insert(0, os.path.join(ROOT, "og_kaarten"))
import importlib
import lk_webflow as WF
A = importlib.import_module(next((a for a in sys.argv[1:] if not a.startswith("--")), "nba_vannacht_2026_10_22"))

RAW = "https://raw.githubusercontent.com/BetExperts/bet-experts-live-kijken/main/og/nieuws/"
BET365 = "https://www.bet-experts.nl/go/bet365"
TOTO = "669ab9f5aceb8b717cea24c3"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
STAKE = getattr(A, "STAKE", [4, 4, 4, 5])
NAMEN = getattr(A, "NAMEN", ["Utah stunt in Memphis!", "Hawks houden Orlando bij!", "Haliburton is terug!", "Trae Young en Davis openen met winst!"])
CTA = (f'<p><a href="{BET365}"><strong>👉 Klik hier: maak je Bet365-account aan en kijk de NBA vannacht live</strong></a></p>')


def slug(s):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")


def tiptekst(t):   # widget gebruikt punt-decimalen, zoals de andere wedtips
    return re.sub(r"(\d),(\d)", r"\1.\2", t)


def main(live):
    kijk = A.content.index("</p>", A.content.index("<p><strong>Kijken?</strong>")) + 4
    content = A.content[:kijk] + CTA + A.content[kijk:]
    tips = A.TIPS
    print(A.TITEL, "|", len(tips), "tips")
    for t, n, s in zip(tips, NAMEN, STAKE):
        print(f"  {n} · {t['wedstrijd']} · {tiptekst(t['tip'])} @{t['odds']} · stake {s}")
    if not live:
        return
    # deelkaart
    from strategie import render_objs
    A.OG_HEADER, A.OG_HEADER_SUB = "NBA", "voorspellingen vannacht"
    render_objs({A.SLUG: A}, "nieuws")
    subprocess.run(f"git add og/nieuws/nieuws-{A.SLUG}.webp specials/nba_vannacht_*.py && git commit -qm 'NBA voorspellingen vannacht: deelkaart' && "
                   "git stash -q; git pull -q --rebase; git push -q; git stash pop -q", shell=True, cwd=ROOT)
    url = RAW + f"nieuws-{A.SLUG}.webp"
    for _ in range(20):
        try:
            if urllib.request.urlopen(url, timeout=20).status == 200: break
        except Exception: time.sleep(6)
    alt = "NBA voorspellingen vannacht: " + ", ".join(d.split(" · ")[1] for d in A.OG_DATA)
    beeld = {"url": url, "alt": alt}
    # Nieuws-item
    fd = {"name": A.TITEL, "slug": A.SLUG, "content": content, "content-2": A.content2, "content-3": A.content3,
          "samenvatting": A.SAMENVATTING, "rubriek": A.RUBRIEK, "competitie": COMPETITIE_NBA,
          "datum-tijd-van-wedstrijd": getattr(A, "DATUM", "2026-10-21T23:00:00.000Z"), "publicatiedatum": datetime.now(timezone.utc).isoformat(),
          "afbeelding": beeld, "seo-afbeelding": beeld, "bookmaker-wedtips": TOTO}
    for i, t in enumerate(tips[:3], 1):
        fd[f"wedtip-{i}-2"] = f"{t['wedstrijd'].replace(' vs. ', ' – ')}: {t['tip']}"
        fd[f"quotering-wedtip-{i}"] = t["odds"]
    iid = WF.create_live(fd)
    print("nieuws:", iid)
    # 25-10-2026: Webflow haalde bij het aanmaken soms de <table>'s weg. Controleren en zo nodig opnieuw zetten.
    for veld in ("content", "content-2", "content-3"):
        if fd[veld].count("<table") and not (WF.get_item(iid, live=True).get("fieldData", {}).get(veld) or "").count("<table"):
            WF.update_staged(iid, {veld: fd[veld]})
            WF._req("PATCH", f"{WF.WF_API}/collections/{WF.NIEUWS_COLLECTION}/items/live", {"items": [{"id": iid, "fieldData": {veld: fd[veld]}}]})
            print(f"  tabellen in {veld} opnieuw gezet")
    # Geen losse Wedtips-items meer aanmaken (Jasper, 24-10-2026): de tips staan alleen in het artikel.


if __name__ == "__main__":
    main("--live" in sys.argv)
