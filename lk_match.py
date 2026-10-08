# -*- coding: utf-8 -*-
"""Verzamelt data voor één wedstrijd en bouwt de Webflow-velddata."""
import re
from datetime import datetime, timezone
import lk_api as api
import lk_build as B
from lk_config import (club_slug, provider_for, RUBRIEK_ID, tv_for, nl_name, tv_match, angle_for_match,
                       stadion_nl, PROVIDERS, LANDEN_NL)
from tvgids import tv_label

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
    gs = re.match(r"group stage\s*-\s*(\d+)", low)               # kwalificatie: 'Group Stage - 1'
    if gs:
        return f"Groepsfase, speelronde {gs.group(1)}"
    for k, v in _ROUND_NL.items():
        if k in low:
            return v[0].upper() + v[1:]
    return round_raw or "Wedstrijd"

# Clubnaam-kenmerken: een landenteam dat (in een oefenduel) tegen een club speelde.
_CLUB_RE = re.compile(r"\b(fc|cf|sc|ac|as|afc|sv|fk|sk|bk|if|cd|ud|sd|club|united|city|real|sporting|"
                      r"athletic|atletico|atlético|deportivo|inter|olympique|borussia|dynamo|dinamo|"
                      r"spartak|lokomotiv|rapid|calcio)\b", re.I)

def _club_duel(f, team_id):
    """True als dit een duel tegen een club is (alleen relevant voor landenteams)."""
    lg = f.get("league", {}) or {}
    if "club" in (lg.get("name") or "").lower():          # bv. 'Friendlies Clubs'
        return True
    t = f.get("teams", {}) or {}
    home = str((t.get("home") or {}).get("id")) == str(team_id)
    opp = ((t.get("away") if home else t.get("home")) or {}).get("name") or ""
    if opp in LANDEN_NL or re.search(r"\bU\d{2}$", opp):   # bekend land (bv. 'United Arab Emirates')
        return False
    return bool(_CLUB_RE.search(opp))

def _done(team_id, landen=False):
    """Afgeronde duels (chronologisch); bij landenteams zonder duels tegen clubs."""
    fixtures = api.team_form(team_id)
    done = [f for f in fixtures
            if ((f.get("fixture", {}).get("status", {}) or {}).get("short") in ("FT", "AET", "PEN"))
            and not (landen and _club_duel(f, team_id))]
    done.sort(key=lambda f: f.get("fixture", {}).get("date", ""))
    return done

def _form_string(team_id, landen=False):
    """Leidt W/D/L-vorm (laatste 5, chronologisch) af uit /api/team-form."""
    out = ""
    for f in _done(team_id, landen)[-5:]:
        t = f.get("teams", {}); g = f.get("goals", {})
        gh, ga = g.get("home"), g.get("away")
        if gh is None or ga is None: continue
        home = str((t.get("home") or {}).get("id")) == str(team_id)
        my, opp = (gh, ga) if home else (ga, gh)
        out += "W" if my > opp else ("L" if my < opp else "D")
    return out

def recent_results(team_id, n=5, landen=False):
    """Laatste n afgeronde resultaten (chronologisch): tegenstander + score + uitslag.
    landen=True: duels van een landenteam tegen clubs tellen niet mee."""
    out = []
    for f in _done(team_id, landen)[-n:]:
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

def gather(fx, standings=None, force_provider=None, landen=False):
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
    hForm = (hRow or {}).get("form") or _form_string(homeId, landen)
    aForm = (aRow or {}).get("form") or _form_string(awayId, landen)

    return {
        "fid": fid, "homeId": homeId, "awayId": awayId, "homeN": homeN, "awayN": awayN,
        "homeApi": home.get("name"), "awayApi": away.get("name"),   # Engelse API-naam (voor de vlag)
        "hSlug": club_slug(homeId, homeN), "aSlug": club_slug(awayId, awayN),
        "compSlug": None, "compN": None,   # ingevuld door build_fielddata (league config)
        "dt": dt, "venue": stadion_nl(ven.get("name")), "city": ven.get("city") or "",
        "referee": fixture.get("referee"), "ronde": ronde, "ronde_txt": ronde_txt, "ronde_raw": round_raw,
        "hRow": hRow, "aRow": aRow, "hForm": hForm, "aForm": aForm,
        "hResults": recent_results(homeId, landen=landen), "aResults": recent_results(awayId, landen=landen),
        "h2h": api.h2h(homeId, awayId),
        "prov": provider_for(fid, force_provider),
    }

LAST_CTX = None

def build_fielddata(ctx, league_cfg, slug=None):
    import random
    random.seed(str(ctx["fid"]))   # deterministische titelvariatie per wedstrijd
    ctx = dict(ctx)
    ctx["compSlug"] = league_cfg["comp_slug"]; ctx["compN"] = league_cfg["naam"]
    ctx["comp_lidwoord"] = league_cfg.get("lidwoord", "de")
    if league_cfg.get("geen_ronde"): ctx["ronde_txt"] = None
    ctx["angle"] = league_cfg.get("angle", "")
    # bv. Afrika Cup zonder Marokko: neutrale invalshoek
    _names = " ".join(str(ctx.get(k) or "") for k in ("homeN", "awayN", "home", "away", "homeName", "awayName")).lower()
    if league_cfg.get("angle_other") and not any(t.lower() in _names for t in league_cfg.get("top_teams", []) + league_cfg.get("top_teams_nl", [])):
        ctx["angle"] = league_cfg["angle_other"]
    # Zender bepalen. Voorrang: 1) handmatig (data/tv_wedstrijden.json), 2) waaroptv.nl
    # (exacte zender, bv. 'Ziggo Sport 2'), 3) de standaard uit de competitie-config.
    if league_cfg.get("tv_per_match"):
        default = league_cfg.get("tv_default") or {}
    else:
        default = {"tv": league_cfg["tv"] if "tv" in league_cfg else tv_for(league_cfg["naam"])}
    card = ctx.get("tvgids")
    gids = None
    if card:
        tvl = tv_label(card)
        npo = bool(tvl) and all(z.upper().startswith("NPO") for z in card["tv"])
        # 'gratis' op waaroptv betekent ook 'in het basispakket' (bv. ESPN 1); onze gratis-
        # tekst gaat over vrij te ontvangen tv, dus alleen overnemen bij NPO.
        gids = {"tv": tvl, "gratis": bool(card.get("gratis")) and npo,
                "extra": "de NOS-app of NOS.nl" if npo else None}
    info = tv_match(ctx["fid"]) or gids or default
    ctx["tv"] = info.get("tv")
    ctx["tv_free"] = bool(info.get("gratis")) and bool(info.get("tv"))
    ctx["tv_extra"] = info.get("extra")
    ctx["tv_voorbeschouwing"] = info.get("voorbeschouwing")
    ctx["tv_bron"] = "handmatig" if tv_match(ctx["fid"]) else ("waaroptv" if gids else "config")
    # eigen intro-invalshoek alleen vervangen als het tv-beeld wezenlijk anders is dan de config
    if (league_cfg.get("tv_per_match") or ctx["tv_free"]
            or bool(ctx["tv"]) != bool(default.get("tv")) or not ctx["angle"]):
        ctx["angle"] = angle_for_match(info, league_cfg["naam"])
    # Geen bookmaker-stream voor deze competitie + betaalde zender -> 'betaald'-variant
    # (geen 'gratis' in titel/tekst; aanbieder alleen voor live meewedden).
    geen_stream = (league_cfg.get("bookmaker_stream", True) is False
                   or (tv_match(ctx["fid"]) or {}).get("bookmaker_stream") is False)   # ook per wedstrijd
    # ...tenzij de tv-gids (waaroptv) een van onze aanbieders als stream bij deze wedstrijd noemt:
    # dan tonen we die stream wél (bij voorkeur de gekozen aanbieder, anders de genoemde).
    gids_prov = [p for p in ((card or {}).get("providers") or []) if p in PROVIDERS]
    if geen_stream and gids_prov:
        if ctx["prov"]["naam"].lower() not in gids_prov:
            ctx["prov"] = PROVIDERS[gids_prov[0]]
        geen_stream = False
        ctx["stream_bron"] = "waaroptv"
    ctx["tv_paid_only"] = geen_stream and bool(ctx.get("tv")) and not ctx.get("tv_free")
    ctx["stream_ok"] = not geen_stream
    # precieze zenderuitleg (ESPN-kanalen, Ziggo Sport 1/Totaal/Free) voor Eredivisie, KKD en Europese bekers
    ctx["zender_soort"] = league_cfg.get("zender_soort")
    if ctx["zender_soort"]:
        _nl = [n.lower() for n in league_cfg.get("nl_clubs", [])]
        ctx["nl_club"] = any(n in _names for n in _nl)
        ctx["competitiefase"] = "league stage" in str(ctx.get("ronde_raw") or "").lower()
    # zender zit in het basispakket (bv. ESPN 1): geen 'betaald abonnement'-tekst
    ctx["tv_basis"] = bool(league_cfg.get("tv_basis")) and ctx["tv_paid_only"]
    dt = ctx["dt"]
    content, content2, content3 = B.build_content(ctx)
    title = B.build_title(ctx["homeN"], ctx["awayN"], dt, paid_tv=ctx["tv"] if ctx["tv_paid_only"] else None,
                          free_tv=ctx["tv"] if ctx.get("tv_free") else None)
    stream = not ctx["tv_paid_only"] and not ctx.get("tv_free")
    samenvatting = B.build_samenvatting(ctx["homeN"], ctx["awayN"], league_cfg["naam"], dt,
                                        ctx["prov"]["naam"], free_tv=ctx["tv"] if ctx.get("tv_free") else None,
                                        paid_tv=ctx["tv"] if ctx["tv_paid_only"] else None,
                                        stream_tv=ctx["tv"] if stream else None,
                                        deposit=ctx["prov"].get("deposit", True))
    if not slug:
        hs = ctx["hSlug"] or B.slugify(ctx["homeN"]); as_ = ctx["aSlug"] or B.slugify(ctx["awayN"])
        slug = B.build_slug(hs, as_, dt, gratis=True)   # 'gratis' altijd in de slug (wens gebruiker)
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
    global LAST_CTX
    LAST_CTX = ctx          # volledige context (zender, aanbieder) voor de deelafbeelding
    return fd, slug, title
