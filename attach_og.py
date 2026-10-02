# -*- coding: utf-8 -*-
"""Zet gecommitte deelafbeeldingen (og/*.webp) in de artikelen.

Draait in de workflow NA de push (de raw-GitHub-URL moet bestaan). Per state-item met een
'og'-bestand dat nog niet gekoppeld is: 'afbeelding' + 'seo-afbeelding' vullen.

  python attach_og.py          # koppelen
  python attach_og.py --dry    # alleen tonen
"""
import sys, urllib.request
import lk_webflow as WF
from lk_og import RAW

def main():
    dry = "--dry" in sys.argv
    state = WF.load_state()
    todo = [(fid, e) for fid, e in state.items() if e.get("og") and e.get("og_done") != e["og"]]
    print(f"{len(todo)} afbeelding(en) te koppelen")
    for fid, e in todo:
        url = RAW + e["og"]
        try:
            urllib.request.urlopen(urllib.request.Request(url, method="HEAD"), timeout=20)
        except Exception as ex:
            print(f"  · nog niet op GitHub ({ex}): {e['og']}"); continue
        alt = f"{e.get('match', '').replace(' - ', ' – ')} live kijken"
        img = {"url": url, "alt": alt}
        if dry:
            print(f"  ○ {e['slug']} <- {url}"); continue
        try:
            (WF.update_staged if e.get("draft") else WF.update_live)(e["item_id"], {"afbeelding": img, "seo-afbeelding": img})   # concepten niet publiceren
            e["og_done"] = e["og"]; WF.save_state(state)
            print(f"  ✔ {e['slug']}")
        except Exception as ex:
            print(f"  ! {e['slug']}: {ex}")

if __name__ == "__main__":
    main()
