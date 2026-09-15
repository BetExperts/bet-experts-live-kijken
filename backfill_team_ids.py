# -*- coding: utf-8 -*-
"""Vult op bestaande live-kijken-artikelen alleen de velden home-team-id en
away-team-id in (tekst blijft ongemoeid). Team-id's komen uit de state, of
anders uit /api/match/{fixture-id}. Slaat ook op in de state voor later.

  python3 backfill_team_ids.py --dry
  WEBFLOW_TOKEN=... python3 backfill_team_ids.py
"""
import sys, argparse
import lk_api as api
import lk_webflow as WF
from lk_config import WEBFLOW_TOKEN

def team_ids_for(fid, entry):
    h, a = entry.get("home_id"), entry.get("away_id")
    if h and a:
        return h, a
    fx = api.match(fid)
    if not fx:
        return None, None
    t = fx.get("teams", {})
    return (str((t.get("home") or {}).get("id") or "") or None,
            str((t.get("away") or {}).get("id") or "") or None)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()
    if not a.dry and not WEBFLOW_TOKEN:
        print("FOUT: WEBFLOW_TOKEN ontbreekt (of gebruik --dry)."); sys.exit(1)

    state = WF.load_state()
    print(f"== Team-id's backfillen | {len(state)} artikel(en) | {'DRY' if a.dry else 'LIVE'} ==")
    done = 0
    for fid, e in list(state.items()):
        h, aw = team_ids_for(fid, e)
        if not (h and aw):
            print(f"  ⚠ geen team-id's gevonden voor {e.get('match')} ({fid})"); continue
        if a.dry:
            print(f"  ○ zou zetten: {e.get('match')} -> home {h}, away {aw}")
        else:
            WF.update_live(e["item_id"], {"home-team-id": h, "away-team-id": aw})
            e["home_id"] = h; e["away_id"] = aw; WF.save_state(state)
            print(f"  ✔ bijgewerkt: {e.get('match')} -> home {h}, away {aw}")
        done += 1
    print(f"\nKLAAR — {done} artikel(en).")

if __name__ == "__main__":
    main()
