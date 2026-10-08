# -*- coding: utf-8 -*-
"""Dagelijkse sitemap-controle -> data/sitemap_uitsluiten.json, gelezen door de sitemap-worker
(dynamic-sitemap-generator v8+): URL's die geen 200 geven (301/404) of een noindex hebben, worden uit de sitemap
gelaten. De controle leest de sitemaps met header 'x-sitemap-alles: 1' (worker zonder uitsluitlijst en zonder cache), zodat een
pagina die weer indexeerbaar wordt vanzelf terugkomt.

  python3 sitemap_check.py
"""
import concurrent.futures as cf, json, os, re, time, urllib.request
from datetime import datetime, timezone
from lk_config import BASE

DOMEIN = "https://www.bet-experts.nl"
UIT = os.path.join(BASE, "data", "sitemap_uitsluiten.json")
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/128 Safari/537.36 BetExpertsSitemapCheck"}


class _GeenRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


OPENER = urllib.request.build_opener(_GeenRedirect)


def get(url, methode="GET", extra=None):
    for poging in range(3):
        try:
            r = OPENER.open(urllib.request.Request(url, headers={**UA, **(extra or {})}, method=methode), timeout=40)
            return r.status, (r.read().decode(errors="ignore") if methode == "GET" else "")
        except urllib.error.HTTPError as e:
            return e.code, ""
        except Exception:
            time.sleep(3)
    return 0, ""


def controleer(url, volledig):
    if volledig:                                   # status + noindex
        st, h = get(url)
        if st == 200 and re.search(r'<meta[^>]+name="robots"[^>]+content="[^"]*noindex', h):
            return url, "noindex"
    else:                                          # nieuws: alleen status (HEAD)
        st, _ = get(url, "HEAD")
    return url, (None if st == 200 else f"http {st}")


def main():
    ALLES = {"x-sitemap-alles": "1"}             # worker: zonder uitsluitlijst en zonder cache
    st, idx = get(f"{DOMEIN}/sitemap.xml", extra=ALLES)
    subs = re.findall(r"<loc>([^<]+)</loc>", idx)
    taken = []
    for s in subs:
        st, x = get(s, extra=ALLES)
        urls = re.findall(r"<url>\s*<loc>([^<]+)</loc>", x)
        volledig = "sitemap-nieuws" not in s
        taken += [(u, volledig) for u in urls]
    uitsluiten, redenen = [], {}
    with cf.ThreadPoolExecutor(10) as ex:
        for url, reden in ex.map(lambda t: controleer(*t), taken):
            if reden and not reden.startswith("http 0"):      # netwerkfout: niet uitsluiten
                uitsluiten.append(url); redenen[reden] = redenen.get(reden, 0) + 1
    json.dump({"bijgewerkt": datetime.now(timezone.utc).isoformat(), "gecontroleerd": len(taken),
               "uitsluiten": sorted(uitsluiten)}, open(UIT, "w", encoding="utf-8"), indent=0)
    print(f"sitemap-check: {len(taken)} URL's, {len(uitsluiten)} uitgesloten {redenen}")


if __name__ == "__main__":
    main()
