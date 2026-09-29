# -*- coding: utf-8 -*-
"""Deelafbeelding per live-kijken-artikel.

  make(ctx, cfg, slug) -> 'og/<slug>-<hash>.webp' (of None bij een fout; het artikel gaat gewoon door)

Het bestand wordt door de workflow gecommit; attach_og.py zet daarna de raw-GitHub-URL in de
velden 'afbeelding' en 'seo-afbeelding' (Webflow kopieert de afbeelding naar zijn eigen CDN).
"""
import hashlib, os

BASE = os.path.dirname(os.path.abspath(__file__))
OG_DIR = os.path.join(BASE, "og")
RAW = "https://raw.githubusercontent.com/BetExperts/bet-experts-live-kijken/main/"

def _cap(s):
    return (s[:1].upper() + s[1:]) if s else s

def info_from(ctx, cfg):
    import og_image as O
    national = bool(cfg.get("landen"))
    tv = ctx.get("tv")
    prov = ctx.get("prov") or {}
    if ctx.get("tv_free"):
        eyebrow, via_naam, via_sub, via_logo = "GRATIS OP TV", tv, "gratis, zonder abonnement", None
    elif ctx.get("tv_paid_only"):
        eyebrow, via_naam, via_logo = "LIVE OP TV", tv, None
        via_sub = "in het basispakket" if ctx.get("tv_basis") else "met abonnement"
    else:
        eyebrow, via_naam, via_logo = "GRATIS LIVESTREAM", prov.get("naam", ""), (prov.get("naam") or "").lower()
        via_sub = "gratis na €10 storting" if prov.get("deposit", True) else "gratis met account"
    ronde = ctx.get("ronde_txt")
    return {
        "comp": _cap(cfg.get("naam")), "ronde": (ronde[:1].lower() + ronde[1:]) if ronde else None,
        "home": ctx["homeN"], "away": ctx["awayN"], "dt": ctx["dt"],
        "home_logo": O.team_logo(ctx.get("homeId"), ctx.get("homeApi"), national),
        "away_logo": O.team_logo(ctx.get("awayId"), ctx.get("awayApi"), national),
        "eyebrow": eyebrow, "via_naam": via_naam or "", "via_sub": via_sub,
        "via_logo": via_logo, "via_tekst": via_naam,
    }

def make(ctx, cfg, slug):
    try:
        import og_image as O
        data = O.render_live(info_from(ctx, cfg))
    except Exception as e:
        print(f"     ! deelafbeelding overgeslagen: {e}")
        return None
    os.makedirs(OG_DIR, exist_ok=True)
    rel = f"og/{slug}-{hashlib.md5(data).hexdigest()[:6]}.webp"
    open(os.path.join(BASE, rel), "wb").write(data)
    return rel
