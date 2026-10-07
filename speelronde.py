# -*- coding: utf-8 -*-
"""Hub-artikel per speelronde: '<Competitie> speelronde N op tv: zenders, aftraptijden en gratis kijken'.

Per competitie de eerstvolgende speelronde die binnen DAGEN_VOORUIT begint: alle wedstrijden per dag met
aftraptijd en exacte zender (tv-gids; anders de vaste zender van de competitie), links naar onze eigen
live-kijken-artikelen en voorbeschouwingen, de toppers van de ronde (stand + vorm) en uitleg over gratis kijken.

  python3 speelronde.py --dry          # alleen tonen
  python3 speelronde.py --preview      # HTML in preview/
  python3 speelronde.py                # aanmaken of bijwerken (alleen als er iets veranderd is)

State: in state/live-kijken.json onder 'hub:<slug>' (date = laatste wedstrijd -> cleanup.py ruimt ze 3 dagen later op).
De tv-gids wordt nooit als bron genoemd.
"""
import argparse, hashlib, html, os, sys
from collections import OrderedDict
from datetime import datetime, timedelta, timezone

import lk_api as api
import lk_build as B
import lk_webflow as WF
from lk_config import nl_name, club_slug, WEBFLOW_TOKEN, BASE
from tvgids import TvGids, tv_label

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


def zender_van(card, default, soort):
    """(label, gratis_tekst) voor één wedstrijd."""
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
    import re
    m = re.search(r"(\d+)\s*$", r or "")
    return m.group(1) if m else None


def build(slug_api, cfg, gids, vb_idx, state, now):
    naam, comp_slug, comp_id, default_tv, soort = cfg
    d = api.fixtures(slug_api) or {}
    up = sorted(d.get("upcoming") or [], key=lambda f: f["fixture"]["date"])
    if not up:
        return None
    ronde = up[0]["league"]["round"]
    fx = [f for f in up if f["league"]["round"] == ronde]
    eerste = B._local(fx[0]["fixture"]["date"])
    if eerste > now + timedelta(days=DAGEN_VOORUIT):
        return None
    nr = ronde_nummer(ronde)
    if not nr:
        return None
    laatste = B._local(fx[-1]["fixture"]["date"])
    if gids:
        for gs in GIDS_SLUGS.get(slug_api, [slug_api]):
            if gids.add_ronde(gs, nr, eerste):
                break
    stand = api.standings(slug_api) or {}
    rows, toppers, telling = [], [], {}
    for f in fx:
        h, a = f["teams"]["home"], f["teams"]["away"]
        hN, aN = nl_name(h["name"]), nl_name(a["name"])
        ko = B._local(f["fixture"]["date"])
        card = gids.lookup(hN, aN, ko) if gids else None
        tv, gratis = zender_van(card, default_tv, soort)
        telling[tv] = telling.get(tv, 0) + 1
        fid = str(f["fixture"]["id"])
        lk = state.get(fid, {}).get("slug")
        vb = WF.voorbeschouwing_url(vb_idx, fid, h["id"], a["id"]) if vb_idx is not None else None
        rows.append({"ko": ko, "home": hN, "away": aN, "tv": tv, "gratis": gratis,
                     "lk": f"/nieuws/{lk}" if lk else None, "vb": vb, "hid": h["id"], "aid": a["id"],
                     "rh": (stand.get(str(h["id"])) or {}), "ra": (stand.get(str(a["id"])) or {})})
    # toppers: laagste som van de ranglijstposities
    met_stand = [r for r in rows if r["rh"].get("rank") and r["ra"].get("rank")]
    toppers = sorted(met_stand, key=lambda r: (max(r["rh"]["rank"], r["ra"]["rank"]), r["rh"]["rank"] + r["ra"]["rank"]))[:3]
    for t in toppers:
        t["h2h"] = vorige_ontmoeting(t["hid"], t["aid"])
    return {"naam": naam, "comp_slug": comp_slug, "comp_id": comp_id, "soort": soort, "nr": nr,
            "eerste": eerste, "laatste": laatste, "rows": rows, "toppers": toppers, "telling": telling}


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


def periode(a, b):
    if a.date() == b.date():
        return f"op {DAGNAAM[a.weekday()]} {a.day} {B.MAAND[a.month-1]}"
    return f"van {DAGNAAM[a.weekday()]} {a.day} tot en met {DAGNAAM[b.weekday()]} {b.day} {B.MAAND[b.month-1]}"


def kort_periode(a, b):
    if a.date() == b.date():
        return f"{a.day} {B.MAAND[a.month-1]}"
    if a.month == b.month:
        return f"{a.day} t/m {b.day} {B.MAAND[b.month-1]}"
    return f"{a.day} {B.MAAND[a.month-1]} t/m {b.day} {B.MAAND[b.month-1]}"


def form_kort(naam, form):
    f = (form or "")[-5:]
    if len(f) < 3:
        return ""
    w, dd, l = f.count("W"), f.count("D"), f.count("L")
    if w == len(f):
        return f"{naam} won de laatste {len(f)} competitieduels allemaal"
    if l == 0:
        return f"{naam} is {len(f)} duels ongeslagen ({w} zege{'s' if w != 1 else ''}, {dd}x gelijk)"
    if w == 0:
        return f"{naam} wacht al {len(f)} duels op een zege"
    delen = [f"{w} keer gewonnen"] + ([f"{dd} keer gelijkgespeeld"] if dd else []) + [f"{l} keer verloren"]
    return f"{naam} heeft van de laatste {len(f)} duels " + (", ".join(delen[:-1]) + " en " + delen[-1])


def verdeling(telling, n):
    """'alle 9 wedstrijden op Viaplay' / '5 wedstrijden op ESPN 1 en 4 op ESPN 2'."""
    items = sorted(telling.items(), key=lambda x: -x[1])
    if len(items) == 1:
        return f"alle {n} wedstrijden zijn live te zien op {items[0][0]}"
    delen = [f"{c} {'wedstrijd' if c == 1 else 'wedstrijden'} op {tv}" if i == 0 else f"{c} op {tv}" for i, (tv, c) in enumerate(items)]
    return ", ".join(delen[:-1]) + " en " + delen[-1]


def html_hub(h):
    e = B.esc
    naam, nr = h["naam"], h["nr"]
    titel = f"{naam} speelronde {nr} op tv: zenders, aftraptijden en gratis kijken ({kort_periode(h['eerste'], h['laatste'])})"
    n = len(h["rows"])
    tel = verdeling(h["telling"], n)
    p = []
    p.append(f'<p><a href="/live-kijken">‹ Alle wedstrijden live kijken: zenders en tijden</a></p>')
    p.append(f"<p><strong>Speelronde {nr} van de {e(naam)} wordt gespeeld {e(periode(h['eerste'], h['laatste']))}. "
             f"Hieronder zie je per wedstrijd de aftraptijd en de zender: {e(tel)}.</strong></p>")
    if h["toppers"]:
        t = h["toppers"][0]
        p.append(f"<p>De blikvanger van deze ronde is {e(t['home'])} – {e(t['away'])}, de nummer {t['rh']['rank']} tegen de "
                 f"nummer {t['ra']['rank']} van de ranglijst. Klik op een wedstrijd voor het volledige artikel met zender, "
                 f"livestream en onze voorspelling.</p>")
    p.append("<h3>Programma en zenders</h3>")
    dag = None
    for r in h["rows"]:
        d = r["ko"].date()
        if d != dag:
            if dag is not None:
                p.append("</ul>")
            dag = d
            p.append(f"<h4>{e(DAGNAAM[r['ko'].weekday()].capitalize())} {r['ko'].day} {e(B.MAAND[r['ko'].month-1])}</h4><ul>")
        m = f"{e(r['home'])} – {e(r['away'])}"
        m = f'<a href="{r["lk"]}">{m}</a>' if r["lk"] else f"<strong>{m}</strong>"
        extra = {"gratis": " (gratis)", "basispakket": " (in het basispakket)"}.get(r["gratis"], "")
        vb = f' · <a href="{r["vb"]}">voorspelling</a>' if r["vb"] else ""
        p.append(f"<li>{B.nl_tijd(r['ko'])} uur: {m}, live op <strong>{e(r['tv'])}</strong>{e(extra)}{vb}</li>")
    p.append("</ul>")
    content = "\n".join(p)
    q = []
    if h["toppers"]:
        q.append("<h3>De toppers van deze speelronde</h3>")
        for t in h["toppers"]:
            rh, ra = t["rh"], t["ra"]
            zin = (f"<p><strong>{e(t['home'])} – {e(t['away'])}</strong> ({DAGNAAM[t['ko'].weekday()]} {B.nl_tijd(t['ko'])} uur, "
                   f"{e(t['tv'])}): de nummer {rh['rank']} ({rh.get('points', 0)} punten) ontvangt de nummer {ra['rank']} "
                   f"({ra.get('points', 0)} punten).")
            fh, fa = form_kort(t["home"], rh.get("form")), form_kort(t["away"], ra.get("form"))
            if fh and fa:
                zin += f" {e(fh)}; {e(fa[0].lower() + fa[1:] if fa.startswith(('De ', 'Het ')) else fa)}."
            v = t.get("h2h")
            if v:
                zin += (f" De vorige ontmoeting, in {v['maand']} {v['jaar']}, eindigde in {v['home']} – {v['away']} "
                        f"{v['gh']}-{v['ga']}.")
            q.append(zin + "</p>")
    q.append(f"<h3>{e(naam)} gratis kijken</h3>")
    q.append(f"<p>{e(GRATIS_UITLEG[h['soort']])}</p>")
    gratis_rows = [r for r in h["rows"] if r["gratis"]]
    if gratis_rows:
        q.append("<p>Deze speelronde zonder extra abonnement te zien: "
                 + ", ".join(f"{e(r['home'])} – {e(r['away'])} ({e(r['tv'])})" for r in gratis_rows) + ".</p>")
    content3 = "\n".join(q)
    faq = [
        (f"Op welke zender is speelronde {nr} van de {naam}?",
         f"{tel[0].upper() + tel[1:]}. Per wedstrijd staat het kanaal in het programma hierboven."),
        (f"Wanneer wordt speelronde {nr} gespeeld?", f"De wedstrijden worden gespeeld {periode(h['eerste'], h['laatste'])}."),
        (f"Welke wedstrijden zijn gratis te zien?",
         ("Zonder extra abonnement: " + ", ".join(f"{r['home']} – {r['away']} ({r['tv']})" for r in gratis_rows) + ".")
         if gratis_rows else GRATIS_UITLEG[h["soort"]]),
    ]
    content3 += "\n<h3>Veelgestelde vragen</h3>\n" + "\n".join(
        f"<p><strong>{e(a)}</strong><br>{e(b)}</p>" for a, b in faq)
    content3 += '\n<p><a href="/live-kijken"><strong>Bekijk alle wedstrijden die je live kunt kijken</strong></a></p>'
    content3 += "\n<p><em>Wat kost gokken jou? Stop op tijd. 18+ | Speel bewust.</em></p>"
    meta = (f"{naam} speelronde {nr} op tv ({kort_periode(h['eerste'], h['laatste'])}): per wedstrijd de zender en aftraptijd, "
            f"de toppers en wat je gratis kunt kijken.")
    return titel, content, content3, meta[:158]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true"); ap.add_argument("--preview", action="store_true")
    ap.add_argument("--league")
    a = ap.parse_args()
    live = not (a.dry or a.preview)
    if live and not WEBFLOW_TOKEN:
        print("FOUT: WEBFLOW_TOKEN ontbreekt"); sys.exit(1)
    now = datetime.now(timezone.utc).astimezone()
    state = WF.load_state()
    gids = TvGids()
    try:
        vb_idx = WF.voorbeschouwing_index()
    except Exception:
        vb_idx = None
    pings = []
    for slug_api, cfg in HUBS.items():
        if a.league and a.league != slug_api:
            continue
        h = build(slug_api, cfg, gids, vb_idx, state, now)
        if not h:
            print(f"{cfg[0]}: geen speelronde binnen {DAGEN_VOORUIT} dagen"); continue
        titel, content, content3, meta = html_hub(h)
        e0 = h["eerste"]
        slug = f"{h['comp_slug']}-speelronde-{h['nr']}-op-tv-{e0.day}-{B.MAAND[e0.month-1]}-{e0.year}"
        key = f"hub:{slug}"
        sig = hashlib.md5((titel + content + content3).encode()).hexdigest()
        print(f"{cfg[0]}: {titel}  ({len(h['rows'])} wedstrijden)")
        if a.preview:
            os.makedirs(os.path.join(BASE, "preview"), exist_ok=True)
            open(os.path.join(BASE, "preview", slug + ".html"), "w", encoding="utf-8").write(
                f"<h1>{html.escape(titel)}</h1><p><em>{html.escape(meta)}</em></p>{content}{content3}")
            continue
        if a.dry:
            continue
        fd = {"name": titel, "slug": slug, "content": content, "content-3": content3, "samenvatting": meta,
              "rubriek": RUBRIEK_ALGEMEEN, "league-slug": h["comp_slug"],
              "publicatiedatum": datetime.now(timezone.utc).isoformat()}
        if h["comp_id"]:
            fd["competitie"] = h["comp_id"]
        e = state.get(key)
        if e and e.get("sig") == sig:
            print("   · ongewijzigd"); continue
        if e:
            WF.update_live(e["item_id"], fd); e["sig"] = sig
            print("   ↻ bijgewerkt")
        else:
            item_id = WF.create_live(fd)
            state[key] = {"item_id": item_id, "slug": slug, "match": f"{cfg[0]} speelronde {h['nr']}",
                          "date": h["laatste"].date().isoformat(), "league": slug_api, "hub": True, "sig": sig}
            try:
                import og_image as O
                img = O.render_hub({"comp": cfg[0], "titel": f"{cfg[0]} speelronde {h['nr']}",
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
