# -*- coding: utf-8 -*-
"""Vult het CMS-veld 'tv-zender' van bestaande live-kijken-artikelen (alleen toekomstige wedstrijden).
Raakt niets anders aan: geen content, geen titel, geen slug. Bron: data/tv_wedstrijden.json + competitieconfig."""
import json, sys, os
sys.path.insert(0, "/Users/jaspervandenboogaard/bet-experts/live-kijken-agent")
os.chdir("/Users/jaspervandenboogaard/bet-experts/live-kijken-agent")
import lk_webflow as WF
from lk_config import LEAGUES, tv_match, tv_for
from datetime import datetime, timezone

CFG = {l["worker_slug"]: l for l in LEAGUES}
st = json.load(open("state/live-kijken.json"))
nu = datetime.now(timezone.utc)
gezet = leeg = al = oud = 0
for fid, v in st.items():
    if not isinstance(v, dict) or not v.get("item_id") or v.get("hub"):
        continue
    it = WF.get_item(v["item_id"], live=True) or {}
    fd = it.get("fieldData", {})
    iso = fd.get("datum-tijd-van-wedstrijd")
    if iso:
        try:
            if datetime.fromisoformat(iso.replace("Z", "+00:00")) < nu:
                oud += 1; continue
        except ValueError:
            pass
    lg = CFG.get(v.get("league")) or {}
    zender = (tv_match(fid) or {}).get("tv") or lg.get("tv") or tv_for(lg.get("naam", ""))
    if not zender:
        leeg += 1; continue
    if fd.get("tv-zender") == zender:
        al += 1; continue
    print(f"  {str(fd.get('slug'))[:46]:<48} {fd.get('tv-zender')!r} -> {zender!r}")
    if "--schrijf" in sys.argv:
        WF.update_live(v["item_id"], {"tv-zender": zender})
    gezet += 1
print(f"\n{gezet} te zetten, {al} stond al goed, {leeg} geen zender bekend, {oud} wedstrijd voorbij")
