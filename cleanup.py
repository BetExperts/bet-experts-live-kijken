# -*- coding: utf-8 -*-
"""Verwijdert oude live-kijken-artikelen (ouder dan RETENTION_DAYS na de wedstrijd)
om onder de Webflow CMS-limiet te blijven. Schrijft per verwijderd artikel een
301-redirectregel (oude URL -> /nieuws) weg voor Webflow → Publishing → 301 redirects.

  python3 cleanup.py --dry     # laat zien wat er weg zou gaan
  python3 cleanup.py           # verwijdert + schrijft redirects-csv
"""
import os, sys, csv, argparse
from datetime import datetime, timedelta, timezone
from lk_config import RETENTION_DAYS, WEBFLOW_TOKEN, BASE
import lk_webflow as WF

REDIR = os.path.join(BASE, "redirects", "live-kijken-redirects.csv")
FALLBACK = "/nieuws"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--days", type=int, default=RETENTION_DAYS)
    a = ap.parse_args()
    if not a.dry and not WEBFLOW_TOKEN:
        print("FOUT: WEBFLOW_TOKEN ontbreekt (of gebruik --dry)."); sys.exit(1)

    cutoff = (datetime.now(timezone.utc) - timedelta(days=a.days)).date()
    state = WF.load_state()
    oud = []
    for fid, e in list(state.items()):
        try:
            d = datetime.strptime(e.get("date",""), "%Y-%m-%d").date()
        except Exception:
            continue
        if d <= cutoff:
            oud.append((fid, e))
    print(f"== Opschonen | ouder dan {a.days} dagen (t/m {cutoff}) | {len(oud)} artikel(en) | {'DRY' if a.dry else 'LIVE'} ==")

    rows = []
    for fid, e in oud:
        oldpath = f"/nieuws/{e['slug']}"
        if a.dry:
            print(f"  ○ zou verwijderen: {e.get('match')} ({oldpath})")
        else:
            WF.delete_item(e["item_id"])
            rows.append([oldpath, FALLBACK])
            del state[fid]; WF.save_state(state)
            print(f"  ✔ verwijderd: {e.get('match')}  → redirect {oldpath} -> {FALLBACK}")

    if rows:
        os.makedirs(os.path.dirname(REDIR), exist_ok=True)
        new = not os.path.exists(REDIR)
        with open(REDIR, "a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if new: w.writerow(["old_path", "redirect_to"])
            w.writerows(rows)
        print(f"\n{len(rows)} redirect(s) toegevoegd aan {REDIR} — voeg toe in Webflow → Publishing → 301 redirects.")
    print("KLAAR.")

if __name__ == "__main__":
    main()
