# -*- coding: utf-8 -*-
"""SEO-titel + FAQ 'Is X betrouwbaar?' voor de collectie Illegale casino's, op basis van GSC (21-10-2026):
'X casino' / 'X nederland' / 'X casino nederland' >> 'is X legaal in nederland' > 'X betrouwbaar' > 'X review'.
Titelpatroon: 'Is <Merk[ Casino]> legaal in Nederland? Betrouwbaar? Review <jaar>'.
  python3 illegale_casinos_seo.py <batch.json ...>   (past de JSON-bestanden in place aan)"""
import json, sys, re

JAAR = 2026
GEEN_CASINO = {"polymarket", "bwin", "pokerstars", "william-hill", "tipico", "bet-at-home", "betonline", "1xbet", "18bet", "21-com",
               "21com", "pferdewetten", "lvbet", "americas-cardroom", "clash-gg", "clashgg", "rustclash", "csgofast", "freebitco-in",
               "freebitcoin", "bc-game", "bcgame"}


def weergave(c):
    n = c["name"]
    if c["slug"] in GEEN_CASINO or re.search(r"(?i)casino|\.bet$|\bbet$", n):
        return n
    return n + " Casino"


def titel(c):
    t = f"Is {weergave(c)} legaal in Nederland? Betrouwbaar? Review {JAAR}"
    if len(t) > 70:
        t = f"Is {weergave(c)} legaal in Nederland? Review {JAAR}"
    return t


def betrouwbaar_faq(c):
    if re.search(r"(?im)^is .* betrouwbaar\?$", c.get("faq", "")):
        return c["faq"]
    n = c["name"]
    blok = (f"Is {n} betrouwbaar?\nNee, niet volgens de Nederlandse maatstaf. {n} heeft geen vergunning van de "
            f"Kansspelautoriteit, dus er is geen Nederlands toezicht op eerlijk spel, uitbetalingen en spelersbescherming. "
            f"Kies daarom een casino of bookmaker met een Nederlandse vergunning.")
    blokken = [b for b in c["faq"].strip().split("\n\n") if b.strip()]
    blokken.insert(1, blok)
    return "\n\n".join(blokken)


if __name__ == "__main__":
    for p in sys.argv[1:]:
        data = json.load(open(p))
        for c in data:
            c["seo_titel"] = titel(c)
            c["faq"] = betrouwbaar_faq(c)
        json.dump(data, open(p, "w"), ensure_ascii=False, indent=1)
        print(p, [(c["slug"], c["seo_titel"]) for c in data][:2])
