# -*- coding: utf-8 -*-
"""Webflow CMS: aanmaken (+publiceren) en verwijderen van items,
plus een lokaal state-bestand fixture-id -> item-id."""
import json, os, time, urllib.request, urllib.error
from lk_config import WEBFLOW_TOKEN, NIEUWS_COLLECTION, WF_API, BASE

STATE = os.path.join(BASE, "state", "live-kijken.json")

def _req(method, url, body=None):
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request(url, data=data, method=method)
    r.add_header("Authorization", "Bearer " + WEBFLOW_TOKEN)
    r.add_header("accept", "application/json")
    if data: r.add_header("content-type", "application/json")
    for attempt in range(5):
        try:
            with urllib.request.urlopen(r, timeout=60) as resp:
                b = resp.read().decode().strip()
                return json.loads(b) if b else {}
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(int(e.headers.get("Retry-After", "5")) + 1); continue
            if e.code >= 500:
                time.sleep(3); continue
            if e.code == 404:
                return {}
            raise RuntimeError(f"Webflow HTTP {e.code}: {e.read().decode()[:300]}")
    raise RuntimeError("Webflow: te veel retries")

def create_live(field_data):
    body = {"isArchived": False, "isDraft": False, "fieldData": field_data}
    res = _req("POST", f"{WF_API}/collections/{NIEUWS_COLLECTION}/items/live", body)
    if isinstance(res, dict):
        if res.get("id"): return res["id"]
        items = res.get("items") or []
        if items: return items[0].get("id")
    raise RuntimeError(f"Onverwachte create-respons: {json.dumps(res)[:200]}")

def update_live(item_id, field_data):
    """Werk een bestaand item bij EN publiceer het opnieuw."""
    return _req("PATCH", f"{WF_API}/collections/{NIEUWS_COLLECTION}/items/{item_id}/live",
                {"fieldData": field_data})

def delete_item(item_id):
    try:
        _req("DELETE", f"{WF_API}/collections/{NIEUWS_COLLECTION}/items/{item_id}/live")
    except Exception:
        pass
    return _req("DELETE", f"{WF_API}/collections/{NIEUWS_COLLECTION}/items/{item_id}")

# ---------- voorbeschouwing-index (voor cross-link naar de preview) ----------
def voorbeschouwing_index(max_items=600):
    """Bouwt een index van gepubliceerde voorbeschouwingen -> slug.
    Sleutels: 'fid:<fixture-id>' en 'pair:<min>-<max>' (team-id-paar)."""
    idx = {}
    offset = 0
    while offset < max_items:
        url = (f"{WF_API}/collections/{NIEUWS_COLLECTION}/items"
               f"?limit=100&offset={offset}&sortBy=lastPublished&sortOrder=desc")
        page = _req("GET", url)
        items = page.get("items", []) if isinstance(page, dict) else []
        if not items:
            break
        for it in items:
            fd = it.get("fieldData", {})
            if not fd.get("voorbeschouwing-2"):
                continue
            if not it.get("lastPublished") or it.get("isDraft"):
                continue
            slug = fd.get("slug")
            if not slug:
                continue
            fid = fd.get("fixture-id")
            if fid:
                idx.setdefault(f"fid:{fid}", slug)
            h, a = fd.get("home-team-id"), fd.get("away-team-id")
            if h and a:
                lo, hi = sorted([str(h), str(a)])
                idx.setdefault(f"pair:{lo}-{hi}", slug)
        offset += len(items)
        total = (page.get("pagination", {}) or {}).get("total", 0)
        if offset >= total:
            break
    return idx

def voorbeschouwing_url(idx, fixture_id, home_id, away_id):
    """Zoekt de voorbeschouwing-URL voor deze wedstrijd (fixture-id eerst, dan team-paar)."""
    slug = idx.get(f"fid:{fixture_id}")
    if not slug and home_id and away_id:
        lo, hi = sorted([str(home_id), str(away_id)])
        slug = idx.get(f"pair:{lo}-{hi}")
    return f"/nieuws/{slug}" if slug else None

# ---------- state ----------
def load_state():
    try:
        return json.load(open(STATE, encoding="utf-8"))
    except Exception:
        return {}

def save_state(st):
    os.makedirs(os.path.dirname(STATE), exist_ok=True)
    json.dump(st, open(STATE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
