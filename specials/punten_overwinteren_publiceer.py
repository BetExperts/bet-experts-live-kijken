# -*- coding: utf-8 -*-
"""Publiceert specials/punten_overwinteren_cl.py en _el.py: deelkaart (og/nieuws/nieuws-<slug>.webp via GitHub raw)
en Nieuws-item live (rubriek + competitie CL/EL).
  set -a; . ../superodd-agent/.env; set +a; ../superodd-agent/.venv/bin/python specials/punten_overwinteren_publiceer.py cl el [--live]"""
import os, sys, re, time, subprocess, urllib.request, importlib
from datetime import datetime, timezone
HIER = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HIER, "..")
sys.path.insert(0, ROOT); sys.path.insert(0, HIER); sys.path.insert(0, os.path.join(ROOT, "og_kaarten"))
import lk_webflow as WF

RAW = "https://raw.githubusercontent.com/BetExperts/bet-experts-live-kijken/main/og/nieuws/"
KOP = {"cl": "Champions League", "el": "Europa League"}


def main(keys, live):
    mods = {k: importlib.import_module(f"punten_overwinteren_{k}") for k in keys}
    for k, m in mods.items():
        m.OG_HEADER, m.OG_HEADER_SUB = KOP[k], "league-fase uitgelegd"
        print(k, len(m.TITEL), m.TITEL, "|", m.SLUG)
    if not live:
        return
    from strategie import render_objs
    render_objs({m.SLUG: m for m in mods.values()}, "nieuws")
    paden = " ".join(f"og/nieuws/nieuws-{m.SLUG}.webp" for m in mods.values())
    subprocess.run(f"git add {paden} specials/punten_overwinteren_*.py && git commit -qm 'Punten overwinteren CL/EL: deelkaarten' && "
                   "git stash -q; git pull -q --rebase; git push -q; git stash pop -q", shell=True, cwd=ROOT)
    for k, m in mods.items():
        url = RAW + f"nieuws-{m.SLUG}.webp"
        for _ in range(20):
            try:
                if urllib.request.urlopen(url, timeout=20).status == 200: break
            except Exception: time.sleep(6)
        beeld = {"url": url, "alt": f"{KOP[k]}: hoeveel punten heb je nodig voor de top 8 en de top 24 van de league-fase"}
        fd = {"name": m.TITEL, "slug": m.SLUG, "content": m.content, "content-2": m.content2, "content-3": m.content3,
              "samenvatting": m.SAMENVATTING, "rubriek": m.RUBRIEK, "competitie": m.COMPETITIE,
              "publicatiedatum": datetime.now(timezone.utc).isoformat(), "afbeelding": beeld, "seo-afbeelding": beeld}
        print(k, "nieuws:", WF.create_live(fd))


if __name__ == "__main__":
    main([a for a in sys.argv[1:] if not a.startswith("--")], "--live" in sys.argv)
