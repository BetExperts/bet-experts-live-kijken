# -*- coding: utf-8 -*-
"""Samengevoegd uitzendschema (alle sporten) -> data/zender_schema.json, gelezen door de Cloudflare-worker
'zenders-pagina' voor het blok 'Deze week op <zender>' op /zenders/<slug>.

Bronnen (nooit noemen op de site): de tv-gids (alle sportpagina's, ook evenementen zonder 'X – Y'), de reserve-
tv-gids (voetbal, JSON) en onze eigen live-kijken-artikelen (exacte zender + link). Dubbele uitzendingen worden
samengevoegd op aftrap (±15 min) + naam.

  python3 zender_schema.py            # schrijft data/zender_schema.json
"""
import html, json, os, re
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import tvgids as G
import lk_webflow as WF
from lk_config import BASE

AMS = ZoneInfo("Europe/Amsterdam")
SPORTEN = ["voetbal", "tennis", "darts", "autosport", "wielrennen", "padel"]
MAX_PAGES = {"voetbal": 6}
UIT = os.path.join(BASE, "data", "zender_schema.json")
BM = {"toto sport": "TOTO", "toto": "TOTO", "bet365": "Bet365", "711": "711", "unibet": "Unibet",
      "betcity": "BetCity", "jacks": "JACKS", "circus": "Circus", "starcasino": "Starcasino"}


def norm_zender(z):
    z = html.unescape(z or "").strip()
    if z.upper() == "ESPN":
        return "ESPN 1"
    if z.lower() == "ziggo sport":
        return "Ziggo Sport 1"
    return z


def _cards_tvgids(sport):
    """Kaarten van één sportpagina (met paginering). Ook evenementen zonder tegenstander."""
    out, url = [], f"{G.BASE}/sport/{sport}/"
    for _ in range(MAX_PAGES.get(sport, 2)):
        try:
            page = G._get(url)
        except Exception:
            break
        for li in re.findall(r'<li class="wp-block-post[^"]*".*?</li>', page, flags=re.S):
            naam = re.search(r'wedstrijd-card__naam"><a href="[^"]+">([^<]+)</a>', li)
            tijd = re.search(r'<time datetime="([^"]+)"', li)
            if not naam or not tijd:
                continue
            try:
                ko = datetime.fromisoformat(tijd.group(1))
            except ValueError:
                continue
            comp = re.search(r'wedstrijd-card__competitie">([^<]+)<', li)
            zenders = G._split_zenders(html.unescape(z).strip()
                                       for z in re.findall(r'wedstrijd-meta__zender">([^<]+)<', li))
            out.append({"titel": html.unescape(naam.group(1)).strip(), "ko": ko,
                        "comp": html.unescape(comp.group(1)).strip() if comp else sport.capitalize(),
                        "zenders": zenders, "sport": sport})
        nxt = re.search(r'<a href="([^"]+)" class="wp-block-query-pagination-next"', page)
        if not nxt:
            break
        url = nxt.group(1) if nxt.group(1).startswith("http") else G.BASE + html.unescape(nxt.group(1))
    return out


def _cards_extra():
    g = G.TvGids()
    return [{"titel": f"{c['home']} – {c['away']}", "ko": c["kickoff"], "comp": c["competitie"],
             "zenders": c["zenders"], "sport": "voetbal"} for c in g.load_extra()]


def _teams(titel):
    p = re.split(r"\s+[–-]\s+", titel, maxsplit=1)
    return (p[0], p[1]) if len(p) == 2 else (titel, "")


def zelfde(a, b):
    if abs((a["ko"] - b["ko"]).total_seconds()) > 15 * 60:
        return False
    ah, aa = _teams(a["titel"]); bh, ba = _teams(b["titel"])
    if not aa or not ba:
        return G._sim(a["titel"], b["titel"]) >= 0.6
    return min(G._sim(ah, bh), G._sim(aa, ba)) >= 0.6


def main():
    now = datetime.now(timezone.utc)
    lo, hi = now - timedelta(hours=3), now + timedelta(days=8)
    bronnen = []
    for sp in SPORTEN:
        bronnen += _cards_tvgids(sp)                  # eerst: hoofdgids (leidend bij verschillen)
    bronnen += _cards_extra()
    items = []
    for c in bronnen:
        if not (lo <= c["ko"] <= hi):
            continue
        tv = [norm_zender(z) for z in c["zenders"] if z.lower() not in BM]
        st = [BM[z.lower()] for z in c["zenders"] if z.lower() in BM]
        dub = next((i for i in items if zelfde(i, c)), None)
        if dub:
            if not dub["zenders"] and tv:
                dub["zenders"] = tv
            dub["streams"] = sorted(set(dub["streams"]) | set(st))
            continue
        items.append({"titel": c["titel"], "ko": c["ko"], "comp": c["comp"], "sport": c["sport"],
                      "zenders": tv, "streams": st, "slug": None})
    # eigen live-kijken-artikelen: exacte zender + link (ook als de gids de wedstrijd niet heeft)
    for fid, e in WF.load_state().items():
        if fid.startswith("hub:") or not e.get("tv_sig") or e.get("draft"):
            continue
        tv_, prov, _, alleen_betaald = (e["tv_sig"].split("|") + ["", "", "", ""])[:4]
        art = {"titel": (e.get("match") or "").replace(" - ", " – "), "ko": None, "slug": e["slug"]}
        kand = [i for i in items if i["ko"].astimezone(AMS).date().isoformat() == e.get("date")
                and G._sim(_teams(art["titel"])[0], _teams(i["titel"])[0]) >= 0.6
                and G._sim(_teams(art["titel"])[1], _teams(i["titel"])[1]) >= 0.6]
        if kand:
            i = kand[0]; i["slug"] = e["slug"]
            if tv_:
                i["zenders"] = [z.strip() for z in re.split(r"\s+en\s+", tv_) if z.strip()]
            if prov and alleen_betaald != "True":
                i["streams"] = sorted(set(i["streams"]) | {prov})
    items.sort(key=lambda i: i["ko"])
    out = [{"ko": i["ko"].astimezone(timezone.utc).isoformat(), "titel": i["titel"], "comp": i["comp"],
            "sport": i["sport"], "zenders": i["zenders"], "streams": i["streams"],
            "url": f"/nieuws/{i['slug']}" if i["slug"] else None} for i in items]
    json.dump({"bijgewerkt": now.isoformat(), "uitzendingen": out}, open(UIT, "w", encoding="utf-8"),
              ensure_ascii=False, indent=0)
    print(f"zender-schema: {len(out)} uitzendingen ({sum(1 for o in out if o['url'])} met eigen artikel)")


if __name__ == "__main__":
    main()
