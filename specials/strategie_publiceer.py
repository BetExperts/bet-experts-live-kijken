# -*- coding: utf-8 -*-
"""Zet de herschreven uitleg-/strategie-artikelen (specials/strategie_<key>.py) live in de Nieuws-collectie,
met maatwerk-deelkaart (og_kaarten/strategie.py -> og/nieuws/strategie-<key>.webp via GitHub raw).
Bestaand item -> update_live; ITEM_ID None -> create_live met SLUG.
  ../superodd-agent/.venv/bin/python specials/strategie_publiceer.py <key> [<key> ...] [--live]"""
import os, sys, re, subprocess, importlib
from datetime import datetime, timezone
HIER = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HIER, "..")
sys.path.insert(0, ROOT); sys.path.insert(0, HIER); sys.path.insert(0, os.path.join(ROOT, "og_kaarten"))
import lk_webflow as WF
from strategie import render

RAW = "https://raw.githubusercontent.com/BetExperts/bet-experts-live-kijken/main/og/nieuws/"


def controle(m):
    html = m.content + m.content2 + m.content3
    assert not re.search(r"<(ul|ol|/li)>\s+<", html), "witruimte in lijst"
    assert "/kennisbank/" not in html and "<h2" not in html, "kennisbank-link of h2"
    assert html.rstrip().endswith("<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"), "KSA-regel ontbreekt"
    assert len(m.SAMENVATTING) <= 160, "samenvatting te lang"
    return len(re.sub(r"<[^>]+>", " ", html).split())


def main(keys, live):
    mods = {k: importlib.import_module(f"strategie_{k}") for k in keys}
    for k, m in mods.items():
        print(f"{k}: {controle(m)} woorden | {len(m.TITEL)} titel | {m.TITEL}")
    if not live:
        return
    render(keys)
    subprocess.run("git add og/nieuws/strategie-*.webp og_kaarten/strategie.py specials/strategie_*.py && "
                   "git commit -qm 'Strategie-artikelen: deelkaarten' && git stash -q; git pull -q --rebase; git push -q; git stash pop -q",
                   shell=True, cwd=ROOT)
    import time, urllib.request
    for k in mods:   # raw.githubusercontent heeft soms even nodig na een push
        for _ in range(20):
            try:
                if urllib.request.urlopen(RAW + f"strategie-{k}.webp", timeout=20).status == 200: break
            except Exception: time.sleep(6)
    for k, m in mods.items():
        og = {"url": RAW + f"strategie-{k}.webp", "alt": re.sub(r"<[^>]+>", "", m.OG_KOP)}
        fd = {"name": m.TITEL, "content": m.content, "content-2": m.content2, "content-3": m.content3,
              "samenvatting": m.SAMENVATTING, "rubriek": m.RUBRIEK, "afbeelding": og, "seo-afbeelding": og,
              "publicatiedatum": datetime.now(timezone.utc).isoformat()}
        if m.ITEM_ID:
            r = WF.update_live(m.ITEM_ID, fd); print(k, "bijgewerkt", r.get("lastPublished"))
        else:
            fd["slug"] = m.SLUG; print(k, "nieuw", WF.create_live(fd))


if __name__ == "__main__":
    main([a for a in sys.argv[1:] if not a.startswith("--")], "--live" in sys.argv)
