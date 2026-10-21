# -*- coding: utf-8 -*-
"""Publiceert specials/nba_vannacht_2026_10_22.py: deelkaart (og/nieuws/nieuws-<slug>.webp via GitHub raw), Nieuws-item live
(rubriek Basketball, competitie NBA, wedtip-velden) en de 4 tips als losse Wedtips-items (rubriek Nachtkraker, status Open).
  set -a; . ../superodd-agent/.env; set +a; ../superodd-agent/.venv/bin/python specials/nba_vannacht_publiceer.py [--live]"""
import os, sys, re, time, subprocess, urllib.request
from datetime import datetime, timezone
HIER = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HIER, "..")
sys.path.insert(0, ROOT); sys.path.insert(0, HIER); sys.path.insert(0, os.path.join(ROOT, "og_kaarten"))
import lk_webflow as WF
import nba_vannacht_2026_10_22 as A

RAW = "https://raw.githubusercontent.com/BetExperts/bet-experts-live-kijken/main/og/nieuws/"
BET365 = "https://www.bet365.nl/hub/nl-nl/open-account?affiliate=365_02599619"
WEDTIPS = "6a2037823226b3069c415cb3"
NACHTKRAKER = "64ff0fbd5a8f205b05d54694"
TOTO = "669ab9f5aceb8b717cea24c3"
COMPETITIE_NBA = "66703df1b7a346f6d0897dbe"
BASKETBALL, OPEN = "784d598a0d9dcf16f7a3afe894cc7305", "3d380375c3388a2f82083a0beb5652eb"
STAKE = [4, 4, 4, 5]
NAMEN = ["Utah stunt in Memphis!", "Hawks houden Orlando bij!", "Haliburton is terug!", "Trae Young en Davis openen met winst!"]
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
          "datum-tijd-van-wedstrijd": "2026-10-21T23:00:00.000Z", "publicatiedatum": datetime.now(timezone.utc).isoformat(),
          "afbeelding": beeld, "seo-afbeelding": beeld, "bookmaker-wedtips": TOTO}
    for i, t in enumerate(tips[:3], 1):
        fd[f"wedtip-{i}-2"] = f"{t['wedstrijd'].replace(' vs. ', ' – ')}: {t['tip']}"
        fd[f"quotering-wedtip-{i}"] = t["odds"]
    print("nieuws:", WF.create_live(fd))
    # Wedtips-items
    for t, n, s in zip(tips, NAMEN, STAKE):
        w = {"name": n, "slug": slug(n), "rubriek-2": NACHTKRAKER, "is-combinatie": False, "stake": s, "bookmaker-wedtips": TOTO,
             "wedstrijd-1": t["wedstrijd"], "competitie-1": "NBA", "tijd-1": t["tijd_nl"],
             "speeltijd-1": t["speeltijd_utc"].replace("Z", ".000Z"), "tip-1": tiptekst(t["tip"]), "analyse-1-2": t["analyse"],
             "odds-1": t["odds"], "sport-1": BASKETBALL, "status": OPEN}
        r = WF._req("POST", f"{WF.WF_API}/collections/{WEDTIPS}/items/live", {"isDraft": False, "fieldData": w})
        print("wedtip:", r.get("id"), n)


if __name__ == "__main__":
    main("--live" in sys.argv)
