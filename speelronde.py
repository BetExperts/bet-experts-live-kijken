# -*- coding: utf-8 -*-
"""Hub-artikel per speelronde: '<Competitie> op tv, speelronde N: welke zender en hoe laat? (…)'.

Per competitie de eerstvolgende speelronde die binnen DAGEN_VOORUIT begint, in een eigen opzet:
kort antwoord, overzicht per zender, speelschema per dag (met wedstrijden die tegelijk beginnen),
onze kijktips (stand, vorm, kansen uit het rekenmodel, laatste onderlinge duel), gratis of met abonnement,
de andere speelronde-hubs van deze week en vragen. Elke wedstrijd linkt naar ons live-kijken-artikel,
de voorbeschouwing en het opstellingen-artikel (zodra die gepubliceerd zijn) -> één groot web van links.

  python3 speelronde.py --dry          # alleen tonen
  python3 speelronde.py --preview      # HTML in preview/
  python3 speelronde.py                # aanmaken of bijwerken (alleen als er iets veranderd is)

State: in state/live-kijken.json onder 'hub:<slug>' (date = laatste wedstrijd -> cleanup.py ruimt ze 3 dagen later op;
'pairs' = team-id-paren + datum, gebruikt door opstellingen-agent/crosslink.py om terug te linken naar de hub).
De tv-gids wordt nooit als bron genoemd.
"""
import argparse, hashlib, html, os, re, sys
from collections import OrderedDict
from datetime import datetime, timedelta, timezone

import lk_api as api
import lk_build as B
import lk_webflow as WF
from lk_config import nl_name, club_slug, WEBFLOW_TOKEN, BASE, PROVIDERS
from tvgids import TvGids, tv_label, BOOKMAKERS

DAGEN_VOORUIT = 3
RUBRIEK_ALGEMEEN = "6502b65d49bc032ba533e7a2"
# worker_slug -> (naam, comp_slug, comp_id, standaardzender, soort)
HUBS = OrderedDict([
    ("eredivisie", ("Eredivisie", "eredivisie", "65de2f987de877fdf6583d10", "ESPN", "espn")),
    ("eerste-divisie", ("Keuken Kampioen Divisie", "keuken-kampioen-divisie", "65de4bc0a8777b9898d6374e", "ESPN", "espn")),
    ("premier-league", ("Premier League", "premier-league", None, "Viaplay", "viaplay")),
    ("la-liga", ("La Liga", "la-liga", "65eafa89159aadee0c5d81d2", "Ziggo Sport", "ziggo")),
    ("serie-a", ("Serie A", "serie-a", "65de2f987de877fdf6583d0c", "Ziggo Sport", "ziggo")),
    ("bundesliga", ("Bundesliga", "bundesliga", None, "Viaplay", "viaplay")),
    ("ligue-1", ("Ligue 1", "ligue-1", None, "Viaplay", "viaplay")),
    ("super-lig", ("Süper Lig", "super-lig", "66ed7d481dc85d2ca649595c", None, "stream")),
    ("jupiler-pro-league", ("Jupiler Pro League", "jupiler-pro-league", "65de4c16dd6eb829e1867f4b", "DAZN", "dazn")),
])
GRATIS_UITLEG = {
    "espn": ("ESPN 1 zit bij vrijwel elke Nederlandse tv-aanbieder in het basispakket: die wedstrijden kijk je met een gewoon "
             "tv-abonnement zonder extra kosten. Bij Ziggo zitten sinds juli 2026 ook ESPN 2, 3 en 4 standaard in het "
             "tv-pakket; bij KPN en Odido boek je die erbij met ESPN Compleet. Wedstrijden op ESPN Extra kijk je in de ESPN-app."),
    "ziggo": ("Ziggo Sport 1 is het open kanaal: Ziggo-klanten kijken daar zonder extra kosten mee met hun gewone tv-pakket. "
              "Voor de andere Ziggo Sport-kanalen heb je Ziggo Sport Totaal nodig, te boeken bij Ziggo, KPN en Odido."),
    "viaplay": ("Viaplay is een betaalde streamingdienst: je kijkt via de Viaplay-app of via Viaplay TV bij je tv-aanbieder. "
                "Gratis tv-uitzendingen zijn er in deze competitie niet."),
    "dazn": ("De Jupiler Pro League zie je in Nederland bij DAZN, een betaalde streamingdienst. Bij 711 kun je met een "
             "account een deel van de wedstrijden gratis live meekijken."),
    "stream": ("De Süper Lig is in Nederland niet op de reguliere tv te zien. Wel kun je de wedstrijden live volgen via de "
               "livestream van een bookmaker, zoals TOTO; daarvoor heb je een gestort account nodig."),
}
# slug(s) van het speelronde-overzicht in de tv-gids (alleen intern gebruikt, nooit als bron genoemd)
GIDS_SLUGS = {"eerste-divisie": ["keuken-kampioen-divisie", "eerste-divisie", "kkd"], "jupiler-pro-league": ["jupiler-pro-league", "pro-league"]}
DAGNAAM = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]
DAGKORT = ["ma", "di", "wo", "do", "vr", "za", "zo"]
TELWOORD = {2: "twee", 3: "drie", 4: "vier", 5: "vijf", 6: "zes", 7: "zeven", 8: "acht", 9: "negen", 10: "tien"}
e = B.esc


def zender_van(card, default, soort):
    """(label, gratis_soort) voor één wedstrijd; gratis_soort = 'gratis' (NPO), 'basispakket' of None."""
    if card:
        tv = tv_label(card)
        if tv:
            npo = all(z.upper().startswith("NPO") for z in card["tv"])
            if card.get("gratis"):
                return tv, ("gratis" if npo else "basispakket")
            return tv, None
        if card.get("bookmakers"):
            return f"livestream {' / '.join(card['bookmakers'])}", None
    if soort == "stream":
        return "livestream (o.a. TOTO)", None
    return default, None


def ronde_nummer(r):
    m = re.search(r"(\d+)\s*$", r or "")
    return m.group(1) if m else None


def kansen(fid):
    """Winstkansen + gemiddeld aantal goals uit het rekenmodel (API-voorspelling)."""
    try:
        p = api.predictions(fid) or {}
    except Exception:
        return None
    pc = (p.get("predictions") or {}).get("percent") or {}
    if not pc.get("home"):
        return None
    t = p.get("teams") or {}
    gem = lambda side: (((t.get(side) or {}).get("league") or {}).get("goals") or {}).get("for", {}).get("average", {}).get("total")
    pr = p.get("predictions") or {}
    return {"winner": (pr.get("winner") or {}).get("name"), "wod": pr.get("win_or_draw"), "uo": pr.get("under_over"),
            "gh": gem("home"), "ga": gem("away")}


def vorige_ontmoeting(hid, aid):
    try:
        fx = [f for f in api.h2h(hid, aid) if (f.get("fixture", {}).get("status", {}) or {}).get("short") in ("FT", "AET", "PEN")]
    except Exception:
        return None
    if not fx:
        return None
    f = max(fx, key=lambda f: f["fixture"]["date"])
    d = B._local(f["fixture"]["date"])
    return {"home": nl_name(f["teams"]["home"]["name"]), "away": nl_name(f["teams"]["away"]["name"]),
            "gh": f["goals"]["home"], "ga": f["goals"]["away"], "maand": B.MAAND[d.month-1], "jaar": d.year}


KLAAR = ("FT", "AET", "PEN")


def doelpunten(fid):
    """["12' Til (1-0)", "58' Ueda (1-1, strafschop)"] uit de wedstrijd-events. De tussenstand wordt
    gecontroleerd tegen de eindstand (eigen doelpunten: beide API-conventies proberen), anders zonder tussenstand."""
    try:
        m = api.match(fid) or {}
    except Exception:
        return []
    hid = ((m.get("teams") or {}).get("home") or {}).get("id")
    eind = ((m.get("goals") or {}).get("home"), (m.get("goals") or {}).get("away"))
    goals = [ev for ev in m.get("events") or []
             if ev.get("type") == "Goal" and "Missed" not in (ev.get("detail") or "")]
    def lijst(og_omdraaien, met_stand):
        gh = ga = 0
        out = []
        for ev in goals:
            thuis = (ev.get("team") or {}).get("id") == hid
            if og_omdraaien and ev.get("detail") == "Own Goal":
                thuis = not thuis
            gh, ga = (gh + 1, ga) if thuis else (gh, ga + 1)
            t = ev.get("time") or {}
            minuut = f"{t.get('elapsed')}{'+' + str(t['extra']) if t.get('extra') else ''}'"
            naam = ((ev.get("player") or {}).get("name") or "").strip()
            extra = {"Penalty": "strafschop", "Own Goal": "eigen doelpunt"}.get(ev.get("detail"))
            info = ", ".join(x for x in ([f"{gh}-{ga}"] if met_stand else []) + ([extra] if extra else []))
            out.append(f"{minuut} {naam}" + (f" ({info})" if info else ""))
        return out, (gh, ga)
    for omdraaien in (False, True):
        out, stand = lijst(omdraaien, True)
        if stand == eind:
            return out
    return lijst(False, False)[0]


def build(slug_api, cfg, gids, widx, state, now, ronde=None):
    """Hub-data voor één speelronde. Zonder `ronde`: de eerstvolgende ronde (als die binnen DAGEN_VOORUIT begint).
    Gespeelde wedstrijden van de ronde blijven erin, met uitslag."""
    naam, comp_slug, comp_id, default_tv, soort = cfg
    d = api.fixtures(slug_api) or {}
    up = sorted(d.get("upcoming") or [], key=lambda f: f["fixture"]["date"])
    if ronde is None:
        if not up:
            return None
        ronde = up[0]["league"]["round"]
        if B._local(up[0]["fixture"]["date"]) > now + timedelta(days=DAGEN_VOORUIT):
            return None
    alle = {f["fixture"]["id"]: f for f in (d.get("recent") or []) + up}
    fx = sorted((f for f in alle.values() if f["league"]["round"] == ronde), key=lambda f: f["fixture"]["date"])
    if not fx:
        return None
    eerste = B._local(fx[0]["fixture"]["date"])
    nr = ronde_nummer(ronde)
    if not nr:
        return None
    laatste = B._local(fx[-1]["fixture"]["date"])
    if gids:
        for gs in GIDS_SLUGS.get(slug_api, [slug_api]):
            if gids.add_ronde(gs, nr, eerste):
                break
    stand = api.standings(slug_api) or {}
    rows, telling = [], {}
    for f in fx:
        h, a = f["teams"]["home"], f["teams"]["away"]
        hN, aN = nl_name(h["name"]), nl_name(a["name"])
        ko = B._local(f["fixture"]["date"])
        card = gids.lookup(hN, aN, ko) if gids else None
        tv, gratis = zender_van(card, default_tv, soort)
        stream = [b for b in (card or {}).get("bookmakers") or [] if not tv.startswith("livestream")]
        telling[tv] = telling.get(tv, 0) + 1
        fid = str(f["fixture"]["id"])
        lo, hi = sorted([str(h["id"]), str(a["id"])])
        art = dict(widx.get((lo, hi, ko.date().isoformat())) or {})
        if not art.get("live") and state.get(fid, {}).get("slug") and not state[fid].get("draft"):
            art["live"] = state[fid]["slug"]
        st = ((f["fixture"].get("status") or {}).get("short"))
        score = (f["goals"]["home"], f["goals"]["away"]) if st in KLAAR and f["goals"]["home"] is not None else None
        rows.append({"fid": fid, "ko": ko, "score": score, "home": hN, "away": aN, "tv": tv, "gratis": gratis, "stream": stream, "art": art,
                     "hid": h["id"], "aid": a["id"], "pair": [lo, hi, ko.date().isoformat()],
                     "rh": (stand.get(str(h["id"])) or {}), "ra": (stand.get(str(a["id"])) or {})})
    met_stand = [r for r in rows if r["rh"].get("rank") and r["ra"].get("rank")]
    tips = sorted(met_stand, key=lambda r: (max(r["rh"]["rank"], r["ra"]["rank"]), r["rh"]["rank"] + r["ra"]["rank"]))[:3]
    for t in tips:
        t["h2h"] = None if t["score"] else vorige_ontmoeting(t["hid"], t["aid"])
        t["kans"] = None if t["score"] else kansen(t["fid"])
        t["goals"] = doelpunten(t["fid"]) if t["score"] else []
    return {"slug_api": slug_api, "ronde": ronde, "naam": naam, "comp_slug": comp_slug, "comp_id": comp_id, "soort": soort, "nr": nr,
            "eerste": eerste, "laatste": laatste, "rows": rows, "tips": tips, "telling": telling}


# ------------------------------------------------------------------ tekstbouwstenen
def kort_periode(a, b):
    if a.date() == b.date():
        return f"{a.day} {B.MAAND[a.month-1]}"
    if a.month == b.month:
        return f"{a.day} t/m {b.day} {B.MAAND[b.month-1]}"
    return f"{a.day} {B.MAAND[a.month-1]} t/m {b.day} {B.MAAND[b.month-1]}"


def dag_tijd(dt):
    return f"{DAGNAAM[dt.weekday()]} {dt.day} {B.MAAND[dt.month-1]} om {B.nl_tijd(dt)} uur"


def aantal(n, enk="wedstrijd", mv="wedstrijden"):
    return f"{TELWOORD.get(n, n)} {enk if n == 1 else mv}" if n != 1 else f"één {enk}"


def plek(r):
    rank, pts = r.get("rank"), r.get("points", 0)
    return "koploper" if rank == 1 else f"nummer {rank}", pts


def vorm_zin(naam, form):
    f = (form or "")[-5:]
    if len(f) < 3:
        return ""
    w, dd, l = f.count("W"), f.count("D"), f.count("L")
    n = TELWOORD.get(len(f), len(f))
    if w == len(f):
        return f"{naam} won de laatste {n} competitieduels allemaal"
    if l == 0:
        return f"{naam} bleef de laatste {n} duels ongeslagen"
    if w == 0:
        return f"{naam} wacht al {n} duels op een overwinning"
    delen = [f"{w}x winst"] + ([f"{dd}x gelijk"] if dd else []) + [f"{l}x verlies"]
    return f"{naam} haalde uit de laatste {n} duels " + ", ".join(delen[:-1]) + " en " + delen[-1]


def komma(x):
    return str(x).replace(".", ",")


def model_zin(k, hn, an):
    """'Ons rekenmodel verwacht dat Feyenoord niet verliest en dat er meer dan 1,5 doelpunten vallen.'"""
    w, uo, delen = k.get("winner"), k.get("uo"), []
    if w:
        w = nl_name(w)
        delen.append(f"{w} niet verliest" if k.get("wod") else f"{w} wint")
    if uo and re.fullmatch(r"[+-]\d+(\.\d+)?", uo):
        delen.append(f"er {'meer' if uo[0] == '+' else 'minder'} dan {komma(uo[1:])} doelpunten vallen")
    if not delen:
        return ""
    return "Ons rekenmodel verwacht dat " + " en dat ".join(delen) + "."


def match_links(r, zelf=None):
    a, out = r["art"], []
    if a.get("live") and zelf != "live":
        out.append(f'<a href="/nieuws/{a["live"]}">waar kijken</a>')
    if a.get("voorb"):
        out.append(f'<a href="/nieuws/{a["voorb"]}">voorspelling</a>')
    if a.get("opst"):
        out.append(f'<a href="/nieuws/{a["opst"]}">opstellingen</a>')
    return out


def kort_antwoord(h):
    n, tel = len(h["rows"]), sorted(h["telling"].items(), key=lambda x: -x[1])
    if len(tel) == 1:
        tv0 = tel[0][0]
        waar = f"via de livestream van {tv0[len('livestream '):]}" if tv0.startswith("livestream ") else f"op {tv0}"
        zin = f"Alle {TELWOORD.get(n, n)} wedstrijden van speelronde {h['nr']} zie je {waar}"
    else:
        delen = [f"{c}x {tv}" for tv, c in tel]
        zin = f"De {TELWOORD.get(n, n)} wedstrijden van speelronde {h['nr']} zijn verdeeld over {len(tel)} zenders: " + \
              ", ".join(delen[:-1]) + " en " + delen[-1]
    gr = [r for r in h["rows"] if r["gratis"] and not r["score"]]
    if gr:
        zin += f". {aantal(len(gr)).capitalize()} kijk je zonder extra abonnement"
    elif h["soort"] in ("viaplay", "dazn"):
        zin += f". Je hebt voor deze speelronde een abonnement op {tel[0][0]} nodig"
    gespeeld = sum(1 for r in h["rows"] if r["score"])
    if gespeeld == n:
        zin += ". Alle wedstrijden zijn gespeeld: de uitslagen staan in het speelschema"
    elif gespeeld:
        zin += f". {aantal(gespeeld).capitalize()} {'is' if gespeeld == 1 else 'zijn'} al gespeeld; die uitslagen staan in het speelschema"
    return zin + "."


def per_zender(h):
    groepen = OrderedDict()
    for r in sorted(h["rows"], key=lambda r: (-h["telling"][r["tv"]], r["ko"])):
        groepen.setdefault(r["tv"], []).append(r)
    if len(groepen) < 2:
        return ""
    p = ["<h3>Welke zender zendt welke wedstrijd uit?</h3>"]
    for tv, rs in groepen.items():
        extra = " (in het basispakket)" if rs[0]["gratis"] == "basispakket" else " (gratis)" if rs[0]["gratis"] == "gratis" else ""
        p.append(f"<p><strong>{e(tv)}</strong>{e(extra)}: "
                 + "; ".join(f"{DAGKORT[r['ko'].weekday()]} {B.nl_tijd(r['ko'])} {e(r['home'])} – {e(r['away'])}" for r in rs)
                 + "</p>")
    return "\n".join(p)


def tegelijk(rows):
    """Zin over wedstrijden die op dezelfde dag tegelijk beginnen."""
    per = OrderedDict()
    for r in rows:
        per.setdefault(B.nl_tijd(r["ko"]), []).append(r)
    if len(per) == 1 and len(rows) > 2:
        return f"Alle {TELWOORD.get(len(rows), len(rows))} duels van deze dag beginnen tegelijk om {list(per)[0]} uur."
    zinnen = []
    for t, rs in per.items():
        if len(rs) == 2:
            zinnen.append(f"om {t} uur lopen {e(rs[0]['home'])} – {e(rs[0]['away'])} ({e(rs[0]['tv'])}) en "
                          f"{e(rs[1]['home'])} – {e(rs[1]['away'])} ({e(rs[1]['tv'])}) gelijk op")
        elif len(rs) > 2:
            zinnen.append(f"om {t} uur beginnen {TELWOORD.get(len(rs), len(rs))} wedstrijden tegelijk")
    if not zinnen:
        return ""
    z = "; ".join(zinnen)
    return "Let op: " + z + "."


def tighten_lists(html_in):
    """Geen witruimte tussen tags binnen <ul>/<ol>: anders gooit Webflow de lijst weg bij publiceren."""
    return re.sub(r"<(ul|ol)\b.*?</\1>", lambda m: re.sub(r"\s*(</?(?:ul|ol|li)\b[^>]*>)\s*", r"\1", m.group(0)), html_in, flags=re.S)


def prov_van(naam):
    """'TOTO Sport' / '711' -> PROVIDERS-item met affiliate-link (of None)."""
    k = BOOKMAKERS.get((naam or "").lower().replace("livestream ", "").strip())
    return PROVIDERS.get(k) if k else None


def stream_provs(h):
    """Bookmakers met livestream in deze ronde (affiliate), TOTO standaard bij de Süper Lig."""
    out = OrderedDict()
    for r in h["rows"]:
        for b in r["stream"] + ([r["tv"]] if r["tv"].startswith("livestream") else []):
            for naam in re.split(r"\s*/\s*", b.replace("livestream", "").replace("(o.a. TOTO)", "TOTO")):
                pv = prov_van(naam)
                if pv:
                    out[pv["naam"]] = pv
    if h["soort"] == "stream" and not out:
        out["TOTO"] = PROVIDERS["toto"]
    return list(out.values())


def cta(pv, tekst):
    return f'<p>👉 <a href="{pv["link"]}"><strong>{e(tekst)}</strong></a></p>'


def club_linker():
    """Linkt een clubnaam één keer per artikel naar /clubs/<slug> (alleen in lopende tekst, niet in lijsten)."""
    gelinkt = set()
    def cl(naam, tid):
        slug = club_slug(tid, naam)
        if not slug or slug in gelinkt:
            return e(naam)
        gelinkt.add(slug)
        return f'<a href="/clubs/{slug}">{e(naam)}</a>'
    return cl


def tip_html(t, cl):
    hn, an = t["home"], t["away"]
    (ph, pth), (pa, pta) = plek(t["rh"]), plek(t["ra"])
    links = match_links(t)
    p = [f"<p><strong>{e(hn)} – {e(an)}</strong> | {e(dag_tijd(t['ko']))}, {e(t['tv'])}</p>"]
    werkw = "speelde tegen" if t.get("score") else "treft"
    zin = f"{cl(hn, t['hid'])} ({e(ph)}, {pth} punten) {werkw} {cl(an, t['aid'])} ({e(pa)}, {pta} punten)."
    vh, va = vorm_zin(hn, t["rh"].get("form")), vorm_zin(an, t["ra"].get("form"))
    if vh and va and not t.get("score"):
        zin += f" {e(vh)}; {e(va)}."
    if t.get("score"):
        zin += f" <strong>Uitslag: {e(hn)} – {e(an)} {t['score'][0]}-{t['score'][1]}</strong>."
        if t.get("goals"):
            zin += " Doelpunten: " + e(", ".join(t["goals"])) + "."
    k = t.get("kans")
    if k:
        if k.get("gh") and k.get("ga"):
            zin += (f" {e(hn)} maakt dit seizoen gemiddeld {komma(k['gh'])} doelpunten per wedstrijd, "
                    f"{e(an)} {komma(k['ga'])}.")
        mz = model_zin(k, hn, an)
        if mz:
            zin += " " + e(mz)
    v = t.get("h2h")
    if v:
        zin += f" Het laatste onderlinge duel ({v['maand']} {v['jaar']}): {e(v['home'])} – {e(v['away'])} {v['gh']}-{v['ga']}."
    p.append(f"<p>{zin}</p>")
    if links:
        p.append("<p>👉 " + " · ".join(links) + "</p>")
    return "\n".join(p)


def html_hub(h, andere):
    naam, nr, kp = h["naam"], h["nr"], kort_periode(h["eerste"], h["laatste"])
    titel = f"{naam} op tv, speelronde {nr}: welke zender en hoe laat? ({kp})"
    rows = h["rows"]
    eerste, laatste = rows[0], rows[-1]
    cl = club_linker()
    p = ['<p><a href="/live-kijken">‹ Alle wedstrijden live kijken: zenders en tijden</a></p>']
    p.append(f"<p><strong>Kort antwoord: {e(kort_antwoord(h))}</strong></p>")
    open_, sluit = ("begon", "eindigde") if laatste["score"] else ("opent", "sluit") if not eerste["score"] else ("begon", "sluit")
    p.append(f"<p>De speelronde {open_} {e(dag_tijd(eerste['ko']))} met {cl(eerste['home'], eerste['hid'])} – {cl(eerste['away'], eerste['aid'])} "
             f"en {sluit} {e(dag_tijd(laatste['ko']))}{'' if sluit == 'eindigde' else ' af'} met {cl(laatste['home'], laatste['hid'])} – {cl(laatste['away'], laatste['aid'])}. "
             f"Klik op een wedstrijd voor alle kijkopties, of ga direct naar de voorspelling en de opstellingen.</p>")
    provs = stream_provs(h)
    if h["soort"] == "stream" and provs:
        pv = provs[0]
        p.append(cta(pv, f"Open een account bij {pv['naam']} en kijk de {naam} live via de {pv['naam']}-livestream"))
    p.append(per_zender(h))
    p.append(f"<h3>Speelschema {e(naam)} speelronde {nr}</h3>")
    dagen = OrderedDict()
    for r in rows:
        dagen.setdefault(r["ko"].date(), []).append(r)
    for d, rs in dagen.items():
        k = rs[0]["ko"]
        p.append(f"<p><strong>{e(DAGNAAM[k.weekday()].capitalize())} {k.day} {e(B.MAAND[k.month-1])}</strong></p><ul>")
        for r in rs:
            m = f"{e(r['home'])} – {e(r['away'])}"
            if r["art"].get("live"):
                m = f'<a href="/nieuws/{r["art"]["live"]}">{m}</a>'
            extra = {"gratis": " (gratis)", "basispakket": " (basispakket)"}.get(r["gratis"], "")
            ln = match_links(r, zelf="live")
            st = f" (ook via de {' / '.join(r['stream'])}-livestream)" if r["stream"] else ""
            if r["score"]:
                p.append(f"<li><strong>{B.nl_tijd(r['ko'])}</strong> {m}: <strong>{r['score'][0]}-{r['score'][1]}</strong> "
                         f"(was live op {e(r['tv'])})" + (" · " + " · ".join(ln) if ln else "") + "</li>")
                continue
            p.append(f"<li><strong>{B.nl_tijd(r['ko'])}</strong> {m}: {e(r['tv'])}{e(extra)}{e(st)}"
                     + (" · " + " · ".join(ln) if ln else "") + "</li>")
        p.append("</ul>")
        tz = tegelijk([r for r in rs if not r["score"]])
        if tz:
            p.append(f"<p><em>{tz}</em></p>")
    content = "\n".join(x for x in p if x)

    q = []
    if h["tips"]:
        q.append(f"<h3>Onze kijktips voor speelronde {nr}</h3>")
        q += [tip_html(t, cl) for t in h["tips"]]
    if h["tips"]:
        q.append(cta(PROVIDERS["toto"], f"Wed live mee op {naam} speelronde {nr} bij TOTO"))
    q.append("<h3>Gratis kijken of een abonnement nodig?</h3>")
    q.append(f"<p>{e(GRATIS_UITLEG[h['soort']])}</p>")
    bms = sorted({b for r in rows for b in r["stream"]})
    if bms:
        ns = sum(1 for r in rows if r["stream"])
        links = " en ".join(f'<a href="{prov_van(b)["link"]}">{e(b)}</a>' if prov_van(b) else e(b) for b in bms)
        q.append(f"<p>{'Alle wedstrijden zijn' if ns == len(rows) else 'Een deel van de wedstrijden is'} daarnaast "
                 f"te volgen via de livestream van {links}. Daarvoor heb je een account bij die bookmaker nodig (18+).</p>")
    if provs:
        pv = provs[0]
        stort = "stort minimaal €10 (dat bedrag kun je daarna gewoon weer opnemen)" if pv.get("deposit") else "log in"
        q.append(f"<p><strong>Zo kijk je via {e(pv['naam'])}:</strong></p><ol><li>Maak een account aan via "
                 f'<a href="{pv["link"]}">deze link naar {e(pv["naam"])}</a></li><li>Verifieer je account en {e(stort)}</li>'
                 f"<li>Open bij de wedstrijd het livestream-icoon en kijk live mee</li></ol>")
        q.append(cta(pv, f"Maak nu je {pv['naam']}-account aan"))
    gr = [r for r in rows if r["gratis"]]
    if gr:
        q.append("<p>Zonder extra abonnement te zien in speelronde " + nr + ": "
                 + ", ".join(f"{e(r['home'])} – {e(r['away'])} ({e(r['tv'])})" for r in gr) + ".</p>")
    if andere:
        q.append("<h3>Meer voetbal op tv deze week</h3><ul>"
                 + "".join(f'<li><a href="/nieuws/{s}">{e(lbl)} op tv</a></li>' for s, lbl in andere) + "</ul>")
    t0 = h["tips"][0] if h["tips"] else eerste
    faq = [(f"Hoe laat begint speelronde {nr} van de {naam}?",
            f"De eerste wedstrijd, {eerste['home']} – {eerste['away']}, begint {dag_tijd(eerste['ko'])} op {eerste['tv']}."),
           (f"Op welke zender is {t0['home']} – {t0['away']}?",
            f"{t0['home']} – {t0['away']} is {dag_tijd(t0['ko'])} live te zien op {t0['tv']}."),
           (f"Kan ik speelronde {nr} gratis kijken?",
            ("Ja, " + ", ".join(f"{r['home']} – {r['away']}" for r in gr) + " zitten in het basispakket of zijn gratis te zien.")
            if gr else GRATIS_UITLEG[h["soort"]])]
    q.append(f"<h3>Vragen over {e(naam)} speelronde {nr}</h3>")
    q += [f"<p><strong>{e(a)}</strong><br>{e(b)}</p>" for a, b in faq]
    q.append(f'<p>📊 Stand, uitslagen en clubs: <a href="/competities/{h["comp_slug"]}">alles over de {e(naam)}</a> · '
             f'<a href="/live-kijken">alle wedstrijden live kijken</a></p>')
    q.append("<p><em>Wat kost gokken jou? Stop op tijd. 18+ | Speel bewust.</em></p>")
    meta = f"{naam} speelronde {nr} op tv ({kp}): {kort_antwoord(h)}"
    if len(meta) > 158:
        meta = f"{naam} speelronde {nr} op tv ({kp}): per wedstrijd de zender, de aftraptijd en wat je gratis kunt kijken."
    return titel, tighten_lists(content), tighten_lists("\n".join(q)), meta


# ------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true"); ap.add_argument("--preview", action="store_true")
    ap.add_argument("--league")
    a = ap.parse_args()
    live = not (a.dry or a.preview)
    if not WEBFLOW_TOKEN:
        print("FOUT: WEBFLOW_TOKEN ontbreekt"); sys.exit(1)
    now = datetime.now(timezone.utc).astimezone()
    state = WF.load_state()
    gids = TvGids()
    try:
        widx = WF.wedstrijd_index()
    except Exception as ex:
        print(f"! wedstrijd-index: {ex}"); widx = {}
    hubs = []
    for slug_api, cfg in HUBS.items():
        if a.league and a.league != slug_api:
            continue
        nieuw = build(slug_api, cfg, gids, widx, state, now)
        if not nieuw:
            print(f"{cfg[0]}: geen nieuwe speelronde binnen {DAGEN_VOORUIT} dagen")
        lopend = []
        gisteren = (now - timedelta(days=1)).date().isoformat()
        for k, v in state.items():          # bestaande hubs: bijwerken met uitslagen tot een dag na de laatste wedstrijd
            if k.startswith("hub:") and v.get("league") == slug_api and v.get("date", "") >= gisteren:
                ronde = v.get("ronde") or f"Regular Season - {v['match'].rsplit(' ', 1)[-1]}"
                if not nieuw or ronde != nieuw["ronde"]:
                    lopend.append(build(slug_api, cfg, gids, widx, state, now, ronde=ronde))
        for h in [nieuw] + lopend:
            if not h:
                continue
            e0 = h["eerste"]
            h["slug"] = f"{h['comp_slug']}-speelronde-{h['nr']}-op-tv-{e0.day}-{B.MAAND[e0.month-1]}-{e0.year}"
            h["label"] = f"{h['naam']} speelronde {h['nr']}"
            hubs.append(h)
    # andere hubs van deze week (ook eerder aangemaakte die nog lopen)
    alle = OrderedDict((h["slug"], h["label"]) for h in hubs)
    for k, v in state.items():
        if k.startswith("hub:") and v.get("date", "") >= now.date().isoformat() and v["slug"] not in alle:
            alle[v["slug"]] = v.get("match", v["slug"])
    pings = []
    for h in hubs:
        slug, key = h["slug"], f"hub:{h['slug']}"
        andere = [(s, l) for s, l in alle.items() if s != slug]
        titel, content, content3, meta = html_hub(h, andere)
        sig = hashlib.md5((titel + content + content3).encode()).hexdigest()
        print(f"{h['naam']}: {titel}  ({len(h['rows'])} wedstrijden)")
        if a.preview:
            os.makedirs(os.path.join(BASE, "preview"), exist_ok=True)
            open(os.path.join(BASE, "preview", slug + ".html"), "w", encoding="utf-8").write(
                f"<h1>{html.escape(titel)}</h1><p><em>{html.escape(meta)}</em></p>{content}{content3}")
            continue
        if a.dry:
            continue
        fd = {"name": titel, "slug": slug, "content": content, "content-3": content3, "samenvatting": meta,
              "rubriek": RUBRIEK_ALGEMEEN, "league-slug": h["comp_slug"]}
        if h["comp_id"]:
            fd["competitie"] = h["comp_id"]
        ent = state.get(key)
        pairs = [r["pair"] for r in h["rows"]]
        if ent and ent.get("sig") == sig:
            if ent.get("pairs") != pairs:
                ent["pairs"] = pairs; WF.save_state(state)
            print("   · ongewijzigd"); continue
        if ent:
            WF.update_live(ent["item_id"], fd)
            ent.update({"sig": sig, "pairs": pairs, "match": h["label"], "date": h["laatste"].date().isoformat(),
                        "ronde": h["ronde"]})
            print("   ↻ bijgewerkt")
        else:
            fd["publicatiedatum"] = datetime.now(timezone.utc).isoformat()
            item_id = WF.create_live(fd)
            state[key] = {"item_id": item_id, "slug": slug, "match": h["label"], "date": h["laatste"].date().isoformat(),
                          "league": h["slug_api"], "hub": True, "sig": sig, "pairs": pairs,
                          "ronde": h["ronde"]}
            try:
                import og_image as O
                img = O.render_hub({"comp": h["naam"], "titel": h["label"],
                                    "sub": f"Op tv: {kort_periode(h['eerste'], h['laatste'])} · alle zenders en aftraptijden"})
                rel = f"og/{slug}-{hashlib.md5(img).hexdigest()[:6]}.webp"
                open(os.path.join(BASE, rel), "wb").write(img); state[key]["og"] = rel
            except Exception as ex:
                print(f"   ! deelafbeelding: {ex}")
            print(f"   ✔ live: /nieuws/{slug}")
        WF.save_state(state)
        pings.append(f"https://www.bet-experts.nl/nieuws/{slug}")
    if pings and live:
        import indexnow
        indexnow.ping(pings)


if __name__ == "__main__":
    main()
