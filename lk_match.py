# -*- coding: utf-8 -*-
"""Verzamelt data voor één wedstrijd en bouwt de Webflow-velddata."""
import re
from datetime import datetime, timezone
import lk_api as api
import lk_build as B
from lk_config import club_slug, provider_for, RUBRIEK_ID, tv_for, nl_name, tv_match, angle_for_match

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
    lg = re.match(r"league\s+([a-d])\s*-\s*(\d+)", low)          # Nations League: 'League A - 1'
    if lg:
        return f"League {lg.group(1).upper()}, speelronde {lg.group(2)}"
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

def recent_results(team_id, n=5):
    """Laatste n afgeronde resultaten (chronologisch): tegenstander + score + uitslag."""
    fixtures = api.team_form(team_id)
    done = [f for f in fixtures
            if ((f.get("fixture", {}).get("status", {}) or {}).get("short") in ("FT", "AET", "PEN"))]
    done.sort(key=lambda f: f.get("fixture", {}).get("date", ""))
    out = []
    for f in done[-n:]:
        t = f.get("teams", {}); g = f.get("goals", {})
        gh, ga = g.get("home"), g.get("away")
        if gh is None or ga is None:
            continue
        home = str((t.get("home") or {}).get("id")) == str(team_id)
        my, og = (gh, ga) if home else (ga, gh)
        opp = nl_name(((t.get("away") if home else t.get("home")) or {}).get("name"))
        outcome = "W" if my > og else ("L" if my < og else "D")
        out.append({"opp": opp, "my": my, "og": og, "home": home,
                    "outcome": outcome, "date": (f.get("fixture", {}).get("date", "") or "")[:10]})
    return out

def gather(fx, standings=None, force_provider=None):
    fixture = fx.get("fixture", {}); teams = fx.get("teams", {}); league = fx.get("league", {})
    fid = fixture.get("id")
    home = teams.get("home", {}); away = teams.get("away", {})
    homeId, awayId = home.get("id"), away.get("id")
    homeN, awayN = nl_name(home.get("name")), nl_name(away.get("name"))   # landen -> Nederlands
    dt = B._local(fixture.get("date"))
    ven = fixture.get("venue", {}) or {}
    round_raw = league.get("round", "") or ""
    m = re.search(r"(\d+)\s*$", round_raw) or re.search(r"(\d+)", round_raw)
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
        "hResults": recent_results(homeId), "aResults": recent_results(awayId),
        "h2h": api.h2h(homeId, awayId),
        "prov": provider_for(fid, force_provider),
    }

def build_fielddata(ctx, league_cfg, slug=None):
    import random
    random.seed(str(ctx["fid"]))   # deterministische titelvariatie per wedstrijd
    ctx = dict(ctx)
    ctx["compSlug"] = league_cfg["comp_slug"]; ctx["compN"] = league_cfg["naam"]
    ctx["angle"] = league_cfg.get("angle", "")
    if league_cfg.get("tv_per_match"):
        # zender per wedstrijd (bv. Nations League: NPO voor Oranje), anders de standaardzender
        info = tv_match(ctx["fid"]) or league_cfg.get("tv_default") or {}
        ctx["tv"] = info.get("tv")
        ctx["tv_free"] = bool(info.get("gratis")) and bool(info.get("tv"))
        ctx["tv_extra"] = info.get("extra")
        ctx["tv_voorbeschouwing"] = info.get("voorbeschouwing")
        ctx["angle"] = angle_for_match(info, league_cfg["naam"])
    else:
        # expliciete tv in de league-config wint; anders afleiden uit de zender-lijst
        ctx["tv"] = league_cfg["tv"] if "tv" in league_cfg else tv_for(league_cfg["naam"])
    # Geen bookmaker-stream voor deze competitie + betaalde zender -> 'betaald'-variant
    # (geen 'gratis' in titel/slug/tekst; aanbieder alleen voor live meewedden).
    ctx["tv_paid_only"] = (league_cfg.get("bookmaker_stream", True) is False
                           and bool(ctx.get("tv")) and not ctx.get("tv_free"))
    dt = ctx["dt"]
    content, content2, content3 = B.build_content(ctx)
    title = B.build_title(ctx["homeN"], ctx["awayN"], dt, paid_tv=ctx["tv"] if ctx["tv_paid_only"] else None)
    samenvatting = B.build_samenvatting(ctx["homeN"], ctx["awayN"], league_cfg["naam"], dt,
                                        ctx["prov"]["naam"], free_tv=ctx["tv"] if ctx.get("tv_free") else None,
                                        paid_tv=ctx["tv"] if ctx["tv_paid_only"] else None)
    if not slug:
        hs = ctx["hSlug"] or B.slugify(ctx["homeN"]); as_ = ctx["aSlug"] or B.slugify(ctx["awayN"])
        slug = B.build_slug(hs, as_, dt, gratis=not ctx["tv_paid_only"])
    fd = {
        "name": title, "slug": slug,
        "content": content, "content-2": content2, "content-3": content3,
        "samenvatting": samenvatting,
        "league-slug": league_cfg["comp_slug"],
        "publicatiedatum": datetime.now(timezone.utc).isoformat(),
        # fixture-id bewust NIET invullen (naar wens gebruiker)
        "datum-tijd-van-wedstrijd": ctx["dt"].isoformat(),
        "tijd-wedstrijd": B.nl_tijd(ctx["dt"]),
    }
    if ctx.get("homeId"):
        fd["home-team-id"] = str(ctx["homeId"])
    if ctx.get("awayId"):
        fd["away-team-id"] = str(ctx["awayId"])
    if RUBRIEK_ID:
        fd["rubriek"] = RUBRIEK_ID
    if league_cfg.get("comp_id"):
        fd["competitie"] = league_cfg["comp_id"]
    return fd, slug, title
