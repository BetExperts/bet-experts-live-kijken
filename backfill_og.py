# -*- coding: utf-8 -*-
"""Eenmalig/handmatig: deelafbeeldingen maken voor bestaande (aankomende) artikelen,
ZONDER de artikeltekst te herschrijven. Daarna committen + pushen en attach_og.py draaien.

  python backfill_og.py                  # alle artikelen vanaf vandaag
  python backfill_og.py --vanaf 2026-10-01
"""
import sys
from datetime import date
import lk_api as api
import lk_match as M
import lk_og as OG
import lk_webflow as WF
from lk_config import LEAGUES
from tvgids import TvGids

def main():
    vanaf = sys.argv[sys.argv.index("--vanaf") + 1] if "--vanaf" in sys.argv else date.today().isoformat()
    lcfg = {c["worker_slug"]: c for c in LEAGUES}
    gids = TvGids(); gids.load()
    state = WF.load_state()
    for fid, e in sorted(state.items(), key=lambda x: x[1].get("date", "")):
        if e.get("date", "") < vanaf or e.get("og"):
            continue
        cfg = lcfg.get(e.get("league"))
        fx = api.match(fid)
        if not cfg or not fx:
            print(f"  · overgeslagen: {e['slug']}"); continue
        ctx = M.gather(fx, force_provider=(e.get("provider") or "").lower() or cfg.get("force_provider"))
        ctx["vb_url"] = None
        ctx["tvgids"] = gids.lookup(ctx["homeN"], ctx["awayN"], ctx["dt"])
        M.build_fielddata(ctx, cfg, slug=e["slug"])
        og = OG.make(M.LAST_CTX, cfg, e["slug"])
        if og:
            e["og"] = og; WF.save_state(state)
            print(f"  ✔ {og}")

if __name__ == "__main__":
    main()
