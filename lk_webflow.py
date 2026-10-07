# -*- coding: utf-8 -*-
"""Webflow CMS: aanmaken (+publiceren) en verwijderen van items,
plus een lokaal state-bestand fixture-id -> item-id."""
import json, os, re, time, urllib.request, urllib.error
from lk_config import WEBFLOW_TOKEN, NIEUWS_COLLECTION, WF_API, BASE

STATE = os.path.join(BASE, "state", "live-kijken.json")

def tighten_lists(html):
    """Geen witruimte tussen tags binnen <ul>/<ol>: anders gooit Webflow de lijst weg bij (her)publiceren."""
    return re.sub(r"<(ul|ol)\b.*?</\1>", lambda m: re.sub(r"\s*(</?(?:ul|ol|li)\b[^>]*>)\s*", r"\1", m.group(0)), html, flags=re.S)

def _req(method, url, body=None):
    if isinstance(body, dict) and isinstance(body.get("fieldData"), dict):
        body = {**body, "fieldData": {k: tighten_lists(v) if isinstance(v, str) and "<" in v else v
                                      for k, v in body["fieldData"].items()}}
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

def create_draft(field_data):
    """Als concept (staged, niet gepubliceerd) aanmaken: de gebruiker plant het zelf in."""
    body = {"isArchived": False, "isDraft": True, "fieldData": field_data}
    res = _req("POST", f"{WF_API}/collections/{NIEUWS_COLLECTION}/items", body)
    if isinstance(res, dict) and res.get("id"):
        return res["id"]
    raise RuntimeError(f"Onverwachte create-respons: {json.dumps(res)[:200]}")

def update_staged(item_id, field_data):
    """Alleen de conceptversie bijwerken (niet publiceren)."""
    return _req("PATCH", f"{WF_API}/collections/{NIEUWS_COLLECTION}/items/{item_id}", {"fieldData": field_data})

def update_live(item_id, field_data):
    """Werk een bestaand item bij EN publiceer het opnieuw."""
    return _req("PATCH", f"{WF_API}/collections/{NIEUWS_COLLECTION}/items/{item_id}/live",
                {"fieldData": field_data})

def get_item(item_id, live=False):
    """Huidig item (staged, of de live-versie) of {} als het niet bestaat."""
    return _req("GET", f"{WF_API}/collections/{NIEUWS_COLLECTION}/items/{item_id}" + ("/live" if live else ""))

# ---------- 'Meer over'-blok van ../opstellingen-agent/crosslink.py behouden ----------
# Zelfde patronen als crosslink.py: bij een --update herschrijft generate.py de content volledig,
# dus zetten we een bestaand blok terug op dezelfde plek als crosslink het zou zetten.
CL_SPACER = "<p>\u200d</p>"
CL_BLOCK_RE = re.compile(r"(?:<p>\u200d</p>)?<p>(?:🔗 )?<strong>Meer over .*?</p>", re.S)
CL_LEES_OOK_RE = re.compile(r"<p>(?:📋 )?<strong>Lees ook:</strong>.*?</p>", re.S)
CL_FIELDS = ("content", "content-2", "content-3")

def _cl_place(html, block):
    """Vervang een 'Lees ook'-alinea door het blok, of zet het na de intro-alinea (als crosslink.place)."""
    html = html or ""
    if CL_LEES_OOK_RE.search(html):
        return CL_LEES_OOK_RE.sub(lambda m: block, html, count=1)
    for m in re.finditer(r"<p>(.*?)</p>", html, re.S):
        if len(re.sub(r"<[^>]+>", "", m.group(1))) > 150:   # intro-alinea
            return html[:m.end()] + block + html[m.end():]
    return None

def behoud_meer_over(item_id, field_data):
    """Haalt het bestaande 'Meer over'-blok uit het huidige CMS-item en zet het terug in de nieuwe
    field_data (zelfde veld). Retourneert True als er een blok is teruggezet."""
    for live in (False, True):
        try:
            old = (get_item(item_id, live=live) or {}).get("fieldData") or {}
        except Exception:
            continue
        for f in CL_FIELDS:
            m = CL_BLOCK_RE.search(old.get(f) or "")
            if not m:
                continue
            if CL_BLOCK_RE.search(field_data.get(f) or ""):
                return True                       # zit er al in
            new = _cl_place(field_data.get(f), m.group(0))
            if new is None and f != "content":
                new = _cl_place(field_data.get("content"), m.group(0)); f = "content"
            if new is None:
                return False
            field_data[f] = new
            return True
    return False

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

# ---------- wedstrijd-index (voorbeschouwing / opstelling / live kijken per wedstrijd) ----------
_LIVE_SLUG = re.compile(r"-live(-gratis)?-kijken-\d{2}-\d{2}-\d{4}$")

def wedstrijd_index(max_items=800):
    """{(laag-id, hoog-id, 'YYYY-MM-DD'): {'voorb': slug, 'opst': slug, 'live': slug}} van gepubliceerde artikelen
    (zelfde sleutel als opstellingen-agent/crosslink.py: team-id-paar + speeldatum in Amsterdam)."""
    from datetime import datetime
    from zoneinfo import ZoneInfo
    ams, idx, offset = ZoneInfo("Europe/Amsterdam"), {}, 0
    while offset < max_items:
        page = _req("GET", f"{WF_API}/collections/{NIEUWS_COLLECTION}/items"
                           f"?limit=100&offset={offset}&sortBy=lastPublished&sortOrder=desc")
        items = (page or {}).get("items") or []
        if not items:
            break
        for it in items:
            fd = it.get("fieldData") or {}
            if not it.get("lastPublished") or it.get("isDraft"):
                continue
            slug = fd.get("slug") or ""
            k = ("voorb" if fd.get("voorbeschouwing-2") else "opst" if slug.startswith("opstelling-")
                 else "live" if _LIVE_SLUG.search(slug) else None)
            h, a, ko = fd.get("home-team-id"), fd.get("away-team-id"), fd.get("datum-tijd-van-wedstrijd")
            if not k or not h or not a or not ko:
                continue
            try:
                d = datetime.fromisoformat(ko.replace("Z", "+00:00")).astimezone(ams).date().isoformat()
            except ValueError:
                continue
            lo, hi = sorted([str(h), str(a)])
            idx.setdefault((lo, hi, d), {}).setdefault(k, slug)      # nieuwste per soort wint
        offset += len(items)
        if offset >= ((page.get("pagination") or {}).get("total") or 0):
            break
    return idx
