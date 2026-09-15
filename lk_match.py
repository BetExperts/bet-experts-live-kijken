# -*- coding: utf-8 -*-
"""Verzamelt data voor één wedstrijd en bouwt de Webflow-velddata."""
import re
from datetime import datetime, timezone
import lk_api as api
import lk_build as B
from lk_config import club_slug, provider_for, RUBRIEK_ID

_ROUND_NL = {
    "round of 64": "1/32 finale", "round of 32": "1/16 finale", "round of 16": "achtste finale",
    "quarter-finals": "kwartfinale", "quarter finals": "kwartfinale",
    "semi-finals": "halve finale", "semi finals": "halve finale",
    "final": "finale", "3rd round": "3e ronde", "4th round": "4e ronde",
}
def _ronde_label(round_raw, ronde_num):
    low = (round_raw or "").strip().lower()
    if "regular season" in low or "matchday" in low:
        return f"Speelronde {ronde_num}" if ronde_num != "?" else "Speelronde"
    for k, v in _ROUND_NL.items():
        if k in low:
            return v[0].upper() + v[1:]
    return round_raw or "Wedstrijd"

def _form_string(team_id):
    """Leidt W/D/L-vorm (laatste 5, chronologisch) af uit /api/team-form."""
    fixtures = api.team_form(team_id)
    done = [f for f in fixtures
            if ((f.get("fixture", {}).get("status", {}) or {}).get("short") in ("FT","AET","PEN"))]
    done.sort(key=lambda f: f.get("fixture", {}).get("date", ""))
    out = ""
    for f in done[-5:]:
        t = f.get("teams", {}); g = f.get("goals", {})
        gh, ga = g.get("home"), g.get("away")
        if gh is None or ga is None: continue
        home = str((t.get("home") or {}).get("id")) == str(team_id)
        my, opp = (gh, ga) if home else (ga, gh)
        out += "W" if my > opp else ("L" if my < opp else "D")
    return out

def gather(fx, standings=None, force_provider=None):
    fixture = fx.get("fixture", {}); teams = fx.get("teams", {}); league = fx.get("league", {})
    fid = fixture.get("id")
    home = teams.get("home", {}); away = teams.get("away", {})
    homeId, awayId = home.get("id"), away.get("id")
    homeN, awayN = home.get("name"), away.get("name")
    dt = B._local(fixture.get("date"))
    ven = fixture.get("venue", {}) or {}
    round_raw = league.get("round", "") or ""
    m = re.search(r"(\d+)", round_raw)
    ronde = m.group(1) if m else "?"
    ronde_txt = _ronde_label(round_raw, ronde)

    standings = standings or {}
    hRow = standings.get(str(homeId)); aRow = standings.get(str(awayId))
    hForm = (hRow or {}).get("form") or _form_string(homeId)
    aForm = (aRow or {}).get("form") or _form_string(awayId)

    return {
        "fid": fid, "homeId": homeId, "awayId": awayId, "homeN": homeN, "awayN": awayN,
        "hSlug": club_slug(homeId, homeN), "aSlug": club_slug(awayId, awayN),
        "compSlug": None, "compN": None,   # ingevuld door build_fielddata (league config)
        "dt": dt, "venue": ven.get("name"), "city": ven.get("city") or "",
        "referee": fixture.get("referee"), "ronde": ronde, "ronde_txt": ronde_txt,
        "hRow": hRow, "aRow": aRow, "hForm": hForm, "aForm": aForm,
        "h2h": api.h2h(homeId, awayId),
        "prov": provider_for(fid, force_provider),
    }

def build_fielddata(ctx, league_cfg, slug=None):
    import random
    random.seed(str(ctx["fid"]))   # deterministische titelvariatie per wedstrijd
    ctx = dict(ctx)
    ctx["compSlug"] = league_cfg["comp_slug"]; ctx["compN"] = league_cfg["naam"]
    ctx["angle"] = league_cfg.get("angle", "")
    dt = ctx["dt"]
    content, content2, content3 = B.build_content(ctx)
    title = B.build_title(ctx["homeN"], ctx["awayN"], dt)
    samenvatting = B.build_samenvatting(ctx["homeN"], ctx["awayN"], league_cfg["naam"], dt, ctx["prov"]["naam"])
    if not slug:
        hs = ctx["hSlug"] or B.slugify(ctx["homeN"]); as_ = ctx["aSlug"] or B.slugify(ctx["awayN"])
        slug = B.build_slug(hs, as_, dt)
    fd = {
        "name": title, "slug": slug,
        "content": content, "content-2": content2, "content-3": content3,
        "samenvatting": samenvatting,
        "league-slug": league_cfg["comp_slug"],
        "publicatiedatum": datetime.now(timezone.utc).isoformat(),
        "datum-tijd-van-wedstrijd": ctx["dt"].isoformat(),
        "tijd-wedstrijd": B.nl_tijd(ctx["dt"]),
    }
    if RUBRIEK_ID:
        fd["rubriek"] = RUBRIEK_ID
    if league_cfg.get("comp_id"):
        fd["competitie"] = league_cfg["comp_id"]
    return fd, slug, title
