# -*- coding: utf-8 -*-
"""Importeert de onderzochte zenders/diensten (JSON) in de Webflow-collectie 'Zenders' (/zenders/<slug>).

  python3 zenders_import.py out_a.json out_b.json ... [--logos] [--publish]

- maakt items aan of werkt ze bij (op slug), standaard als CONCEPT (template nog in ontwerp);
- logo's: --logos downloadt logo_bron, maakt er een vierkant .webp (512px, transparant) van in assets/zenders/,
  pusht naar GitHub en laat Webflow het via de raw-URL inladen;
- koppelt bookmaker (Bookmakers-CMS), competities (Competities-CMS op naam) en gerelateerde zenders (2e ronde);
- interne links /dienst/<slug> worden /zenders/<slug>.
"""
import io, json, os, re, subprocess, sys, unicodedata, urllib.request
from datetime import datetime, timezone

import lk_webflow as WF
from lk_config import WF_API, BASE, PROVIDERS

CID = "6ac7950c7624f9531e37212a"
COMPETITIES = "65de2d336e1c52d55d0efd89"
RAW = "https://raw.githubusercontent.com/BetExperts/bet-experts-live-kijken/main/"
BOOKMAKER_ID = {"711": "66a8a87062108480763b7309", "toto": "669ab9f5aceb8b717cea24c3",
                "bet365": "651bd6728c40de720bd8072a", "starcasino": "6a7afdaa4a7453c17d31cab5"}
AFFILIATE = {"711": PROVIDERS["711"]["link"], "toto": PROVIDERS["toto"]["link"], "bet365": PROVIDERS["bet365"]["link"],
             "starcasino": "https://media1.affiliates.starcasino.nl/redirect.aspx?pid=2170&bid=1477"}
BOOKMAKER_LOGO = {   # eigen logo's uit het Bookmakers-CMS
    # 711: officiële SVG via logo_bron (CMS-png heeft te veel witruimte)
    "toto": "https://cdn.prod.website-files.com/64f9f8e867f73b8e88841e09/6ab1340bb72e4a54909ac597_6a03695c98efe52e8452132c_logo-toto-groen.webp",
    "bet365": "https://cdn.prod.website-files.com/64f9f8e867f73b8e88841e09/651bd6dad055d6e894f4f703_bet365-logo-groen-en-geel-betexperts.webp",
    "starcasino": "https://cdn.prod.website-files.com/64f9f8e867f73b8e88841e09/6aad0740a906a610179e800b_Starcasino-1400x1400-logo-via-CasinoNieuws-1024x1024.webp",
}
VERBORGEN = set()   # starcasino: streamlijst ontvangen 9-10-2026, aanbod onder voorbehoud -> wel op de hub
SKIP = {"gerelateerde", "logo_bron", "bronnen", "name", "slug"}
UA = {"User-Agent": "Mozilla/5.0 (compatible; BetExpertsBot/1.0; +https://www.bet-experts.nl)"}


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def options():
    c = WF._req("GET", f"{WF_API}/collections/{CID}")
    return {f["slug"]: {o["name"]: o["id"] for o in (f.get("validations") or {}).get("options", [])}
            for f in c["fields"] if f["type"] == "Option"}


def competitie_index():
    idx, off = {}, 0
    while True:
        p = WF._req("GET", f"{WF_API}/collections/{COMPETITIES}/items?limit=100&offset={off}")
        for it in p["items"]:
            idx[norm(it["fieldData"].get("name"))] = it["id"]
        off += 100
        if off >= p["pagination"]["total"]:
            return idx


def bestaande():
    out, off = {}, 0
    while True:
        p = WF._req("GET", f"{WF_API}/collections/{CID}/items?limit=100&offset={off}")
        for it in p.get("items", []):
            out[it["fieldData"]["slug"]] = it
        off += 100
        if off >= (p.get("pagination") or {}).get("total", 0):
            return out


def logo_webp(slug, url):
    """Download (SVG via headless browser) -> vierkant 512x512 webp met transparante achtergrond."""
    from PIL import Image
    os.makedirs(os.path.join(BASE, "assets", "zenders"), exist_ok=True)
    pad = os.path.join(BASE, "assets", "zenders", f"{slug}.webp")
    data = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40).read()
    if url.lower().split("?")[0].endswith(".svg") or data[:200].lstrip().startswith((b"<svg", b"<?xml")):
        from playwright.sync_api import sync_playwright
        svg = data.decode("utf-8", "ignore")
        with sync_playwright() as p:
            b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1024, "height": 1024})
            pg.set_content(f'<html><body style="margin:0;background:transparent">'
                           f'<div style="width:1024px;height:1024px;display:flex;align-items:center;justify-content:center">'
                           f'<img src="data:image/svg+xml;base64,{__import__("base64").b64encode(svg.encode()).decode()}" '
                           f'style="max-width:880px;max-height:880px;width:880px;height:880px;object-fit:contain"></div></body></html>')
            data = pg.screenshot(omit_background=True); b.close()
    im = Image.open(io.BytesIO(data)).convert("RGBA")
    bbox = im.getbbox()
    if bbox:
        im = im.crop(bbox)
    im.thumbnail((440, 440), Image.LANCZOS)
    # (bijna) wit logo -> donkere achtergrond, anders onzichtbaar op witte kaarten
    px = [p for p in im.getdata() if p[3] > 128]
    wit = px and sum(1 for p in px if min(p[:3]) > 225) / len(px) > 0.85
    vak = Image.new("RGBA", (512, 512), (15, 22, 33, 255) if wit else (0, 0, 0, 0))
    vak.paste(im, ((512 - im.width) // 2, (512 - im.height) // 2), im)
    vak.save(pad, "WEBP", quality=92, method=6)
    return os.path.relpath(pad, BASE)


def velden(d, opts, comp_idx):
    fd = {k: v for k, v in d.items() if k not in SKIP and v not in (None, "")}
    for k, v in list(fd.items()):
        if isinstance(v, str):
            fd[k] = v.replace("/dienst/", "/zenders/")
    for k in ("soort-dienst", "hub-filter"):     # optienaam -> optie-id
        if k in fd:
            oid = opts[k].get(fd[k])
            if oid:
                fd[k] = oid
            else:
                print(f"  ! onbekende optie {k}={fd[k]!r}"); fd.pop(k)
    for k in ("aantal-sporten", "aantal-zenders", "aantal-competities", "volgorde"):
        if k in fd:
            try:
                fd[k] = int(fd[k])
            except Exception:
                fd.pop(k)
    fd["account-18-plus"] = bool(d.get("account-18-plus"))
    fd["toon-op-hub"] = d["slug"] not in VERBORGEN
    fd["bijgewerkt"] = datetime.now(timezone.utc).isoformat()
    fd["uitzendrechten-seizoen"] = d.get("uitzendrechten-seizoen") or "2026/27"
    slug = d["slug"]
    if slug in BOOKMAKER_ID:
        fd["bookmaker"] = BOOKMAKER_ID[slug]
    if slug in AFFILIATE:
        fd["affiliate-link"] = AFFILIATE[slug]
    comps = []
    for regel in (d.get("competities-lijst") or "").split("\n"):
        n = norm(regel.split("|")[0])
        if n in comp_idx and comp_idx[n] not in comps:
            comps.append(comp_idx[n])
    if comps:
        fd["competitie-koppelingen"] = comps
    return fd


def main():
    files = [a for a in sys.argv[1:] if not a.startswith("--")]
    data = [d for f in files for d in json.load(open(f, encoding="utf-8"))]
    opts, comp_idx, bestaand = options(), competitie_index(), bestaande()
    logos = {}
    if "--logos" in sys.argv:
        for d in data:
            url = BOOKMAKER_LOGO.get(d["slug"]) or d.get("logo_bron")
            if not url:
                continue
            try:
                logos[d["slug"]] = logo_webp(d["slug"], url); print(f"  logo {d['slug']}: ok")
            except Exception as ex:
                print(f"  ! logo {d['slug']}: {ex}")
        subprocess.run(["git", "add", "assets/zenders"], cwd=BASE)
        subprocess.run(["git", "commit", "-qm", "Logo's zenders (webp)"], cwd=BASE)
        subprocess.run(["git", "pull", "-q", "--rebase", "--autostash"], cwd=BASE)
        subprocess.run(["git", "push", "-q"], cwd=BASE)
    ids = {}
    for d in data:
        fd = velden(d, opts, comp_idx)
        fd.update({"name": d["name"], "slug": d["slug"]})
        if d["slug"] in logos:
            fd["logo"] = {"url": RAW + logos[d["slug"]], "alt": f"{d['name']} logo"}
        it = bestaand.get(d["slug"])
        if it:
            WF._req("PATCH", f"{WF_API}/collections/{CID}/items/{it['id']}", {"fieldData": fd})
            ids[d["slug"]] = it["id"]; print(f"↻ {d['name']}")
        else:
            r = WF._req("POST", f"{WF_API}/collections/{CID}/items", {"isDraft": True, "isArchived": False, "fieldData": fd})
            ids[d["slug"]] = r["id"]; print(f"＋ {d['name']} (concept)")
    alle = {**{s: it["id"] for s, it in bestaand.items()}, **ids}
    for d in data:   # 2e ronde: gerelateerde zenders
        rel = [alle[s] for s in d.get("gerelateerde") or [] if s in alle and s != d["slug"]]
        if rel:
            WF._req("PATCH", f"{WF_API}/collections/{CID}/items/{alle[d['slug']]}", {"fieldData": {"gerelateerde-diensten": rel}})
    if "--publish" in sys.argv:
        WF._req("POST", f"{WF_API}/collections/{CID}/items/publish", {"itemIds": list(alle.values())})
        print("gepubliceerd")


if __name__ == "__main__":
    main()
