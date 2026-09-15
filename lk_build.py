# -*- coding: utf-8 -*-
"""Bouwt titel, samenvatting en de 3 rich-text delen voor een 'live gratis
kijken'-artikel. Alleen Webflow-compatibele HTML: <p> <h3> <ul> <ol> <li>
<strong> <br> <a>. GEEN tabellen."""
import random, html, re, unicodedata
from datetime import datetime
try:
    from zoneinfo import ZoneInfo
    TZ = ZoneInfo("Europe/Amsterdam")
except Exception:
    TZ = None

from lk_config import HUB_PATH

DAGEN = ["maandag","dinsdag","woensdag","donderdag","vrijdag","zaterdag","zondag"]
MAAND = ["januari","februari","maart","april","mei","juni","juli","augustus",
         "september","oktober","november","december"]

def _local(dt_iso):
    dt = datetime.fromisoformat(dt_iso.replace("Z","+00:00"))
    if TZ: dt = dt.astimezone(TZ)
    return dt

def nl_datum(dt): return f"{DAGEN[dt.weekday()]} {dt.day} {MAAND[dt.month-1]} {dt.year}"
def nl_datum_kort(dt): return f"{dt.day} {MAAND[dt.month-1]}"
def nl_tijd(dt):  return f"{dt.hour:02d}:{dt.minute:02d}"
def esc(s): return html.escape(str(s or ""), quote=False)

_TR = {"ı":"i","İ":"I","ş":"s","Ş":"S","ğ":"g","Ğ":"G","ç":"c","Ç":"C","ö":"o","Ö":"O","ü":"u","Ü":"U"}
def slugify(s):
    s = "".join(_TR.get(c, c) for c in (s or ""))
    s = unicodedata.normalize("NFKD", s).encode("ascii","ignore").decode()
    return re.sub(r"-+","-", re.sub(r"[^a-z0-9]+","-", s.lower())).strip("-")

def build_slug(home_slug, away_slug, dt):
    return f"{home_slug}-{away_slug}-live-gratis-kijken-{dt.day:02d}-{dt.month:02d}-{dt.year}"

# ---------- titel (gevarieerd, deterministisch per fixture) ----------
def build_title(homeN, awayN, dt):
    M = f"{homeN} – {awayN}"
    datum = nl_datum_kort(dt); tijd = nl_tijd(dt)
    templates = [
        f"Zo kijk je {M} live gratis op tv",
        f"Dit is hoe je {M} gratis kunt kijken op tv",
        f"{M} live gratis kijken: zo doe je dat",
        f"Zo stream je {M} gratis in HD op je tv",
        f"{M} gratis kijken op tv ({datum})",
        f"Live en gratis: zo zie je {M} op tv",
        f"Hoe kijk je {M} gratis? Zo stream je het duel live",
        f"{M} live volgen: gratis kijken op tv, zo werkt het",
        f"Zo kun je {M} gratis livestreamen op tv om {tijd} uur",
        f"{M} gratis en live kijken op tv — zo regel je het",
        # varianten met 'in Nederland' (verschijnen af en toe)
        f"Zo kijk je {M} gratis in Nederland op tv",
        f"{M} live gratis te kijken in Nederland — zo werkt het",
        f"Gratis {M} kijken in Nederland: zo stream je het live op tv",
    ]
    return random.choice(templates)

def build_samenvatting(homeN, awayN, comp, dt, prov_naam):
    s = (f"{homeN} – {awayN} live gratis kijken? Zo stream je het {comp}-duel van "
         f"{nl_datum(dt)} om {nl_tijd(dt)} uur volledig gratis in HD op tv via {prov_naam}. "
         f"Stap voor stap uitgelegd.")
    return s[:250]

# ---------- vorm ----------
def form_dashes(f):
    m = {"W":"W","D":"G","L":"V"}
    return "–".join(m.get(c, c) for c in (f or "")[:5]) or "n.n.b."

def form_zin(f):
    w=(f or "").count("W"); l=(f or "").count("L")
    if w>=3: return "De vorm zit er de laatste weken goed in."
    if l>=3: return "De resultaten vielen de laatste weken tegen."
    return "De vorm is wisselvallig met winst en verlies door elkaar."

# ---------- 'over de club' op basis van de competitiestand ----------
def _ordinal(n):
    return f"{n}e"

def _join_nl(parts):
    if not parts: return ""
    if len(parts) == 1: return parts[0]
    return ", ".join(parts[:-1]) + " en " + parts[-1]

def _result_phrase(r):
    """Menselijke uitslag-omschrijving vanuit het team gezien."""
    opp = esc(r["opp"]); s = f'{r["my"]}-{r["og"]}'
    if r["outcome"] == "W":
        return f'een {s}-zege {"tegen" if r["home"] else "bij"} {opp}'
    if r["outcome"] == "L":
        return f'een {s}-nederlaag {"tegen" if r["home"] else "bij"} {opp}'
    return f'een {s}-gelijkspel {"tegen" if r["home"] else "bij"} {opp}'

def _form_verhaal(team, form, results, compN):
    """Kort menselijk stukje over de vorm, met echte uitslagen."""
    results = results or []
    frm = form or "".join(r["outcome"] for r in results)
    last5 = results[-5:]
    pts = sum(3 if r["outcome"] == "W" else (1 if r["outcome"] == "D" else 0) for r in last5)
    w = sum(1 for r in last5 if r["outcome"] == "W")
    l = sum(1 for r in last5 if r["outcome"] == "L")
    recent = list(reversed(last5))  # recentste eerst
    if not recent:
        return f"Recente resultaten van <strong>{esc(team)}</strong> zijn nog niet beschikbaar."
    # openingszin over de reeks
    if w >= 3:
        kop = f"<strong>{esc(team)}</strong> is uitstekend op dreef"
    elif l >= 3:
        kop = f"<strong>{esc(team)}</strong> is de laatste weken zoekende"
    elif w == 0:
        kop = f"<strong>{esc(team)}</strong> wacht nog op een overwinning"
    else:
        kop = f"<strong>{esc(team)}</strong> kent een wisselvallige reeks"
    laatste = recent[0]; opp = esc(laatste["opp"]); s = f'{laatste["my"]}-{laatste["og"]}'
    if laatste["outcome"] == "W":
        slot = f'won de ploeg met {s} {"van" if laatste["home"] else "bij"} {opp}'
    elif laatste["outcome"] == "L":
        slot = f'verloor de ploeg met {s} {"van" if laatste["home"] else "bij"} {opp}'
    else:
        slot = f'speelde de ploeg met {s} gelijk {"tegen" if laatste["home"] else "bij"} {opp}'
    phrases = [_result_phrase(r) for r in recent[1:4]]   # de duels dáárvoor
    verhaal = (f"{kop}: uit de laatste vijf duels pakte de ploeg {pts} punten. "
               f"In de meest recente wedstrijd {slot}")
    verhaal += (f"; daarvoor stonden onder meer {_join_nl(phrases)} op de teller." if phrases else ".")
    return verhaal

def team_focus(team, row, form, results, compN="de competitie"):
    parts = []
    if row:
        alld = row.get("all", {}) or {}
        g = alld.get("goals", {}) or {}
        rank = row.get("rank"); pnt = row.get("points")
        pl = alld.get("played"); gf = g.get("for"); ga = g.get("against")
        parts.append(f"Met {pnt} punten uit {pl} wedstrijden staat <strong>{esc(team)}</strong> "
                     f"op dit moment {_ordinal(rank)} in de {esc(compN)} (doelsaldo {gf}-{ga}).")
    parts.append(_form_verhaal(team, form, results, compN))
    return "<p>" + " ".join(parts) + "</p>"

# ---------- H2H ----------
def _h2h_line(m):
    fx=m.get("fixture",{}); dt=(fx.get("date","") or "")[:10]
    t=m.get("teams",{}); g=m.get("goals",{})
    try:
        y,mo,d = dt.split("-"); dts=f"{int(d)} {MAAND[int(mo)-1]} {y}"
    except Exception:
        dts=dt
    return f"{dts}: {t.get('home',{}).get('name')} {g.get('home')}-{g.get('away')} {t.get('away',{}).get('name')}"

# ---------- het gratis-kijken-blok (provider-afhankelijk) ----------
def _kijk_blok(prov, homeN, awayN, comp, tv=None):
    naam = prov["naam"]; link = prov["link"]; M = f"{esc(homeN)} vs {esc(awayN)}"
    out = [f"<h3>Gratis live kijken via {esc(naam)}</h3>"]
    if tv:
        out.append(f"<p>Je kunt {M} volledig gratis livestreamen via {esc(naam)}. In Nederland is de "
                    f"{esc(comp)} wel te zien op {esc(tv)}, maar daarvoor heb je een betaald abonnement nodig. "
                    f"Met een gratis {esc(naam)}-account kijk je dit duel zonder abonnement en zonder kosten.</p>")
    else:
        out.append(f"<p>De wedstrijd tussen {esc(homeN)} en {esc(awayN)} is niet live te zien op de Nederlandse "
                    f"televisie. De enige manier om dit {esc(comp)}-duel live te volgen in Nederland is via "
                    f"{esc(naam)} met een gratis account.</p>")
    out.append(f"<p><strong>Zo werkt gratis kijken via {esc(naam)}:</strong></p>")
    if prov.get("deposit", True):
        out.append("<ol>"
                   "<li>Maak een gratis account aan via de link hieronder</li>"
                   "<li>Stort €10 — het minimumbedrag voor toegang tot de livestream</li>"
                   f"<li>Kijk {M} volledig gratis in HD</li>"
                   "<li>Haal daarna je €10 er gewoon weer af</li>"
                   "</ol>")
        out.append("<p>Je kijkt de wedstrijd dus volledig gratis — de €10 verdwijnt niet.</p>")
    else:
        out.append("<ol>"
                   "<li>Maak een gratis account aan via de link hieronder</li>"
                   "<li>Log in op je account</li>"
                   f"<li>Kijk {M} volledig gratis in HD</li>"
                   "</ol>")
        out.append("<p>Je hebt alleen een gratis account nodig — geen storting, geen kosten.</p>")
    if prov.get("cast"):
        out.append(f"<p><strong>Wil je op groot scherm kijken?</strong> Cast de {esc(naam)}-stream via "
                    f"Chromecast, AirPlay of een HDMI-kabel naar je televisie — volledig gratis.</p>")
    out.append(f'<p>👉 <a href="{link}"><strong>Maak een gratis {esc(naam)}-account aan en kijk '
               f'{esc(homeN)} – {esc(awayN)} live</strong></a></p>')
    return "\n".join(out)

# ---------- FAQ ----------
def _faq(homeN, awayN, comp, dt, prov, tv=None):
    naam = prov["naam"]
    if tv:
        waar = (f"Waar kan ik {homeN} – {awayN} in Nederland kijken?",
                f"In Nederland zendt {tv} de {comp} uit, maar daarvoor heb je een betaald abonnement nodig. "
                f"Zonder abonnement stream je het duel gratis via een {naam}-account.")
    else:
        waar = (f"Waarom is {homeN} – {awayN} niet op de Nederlandse tv?",
                f"De {comp} wordt in Nederland niet door een reguliere tv-zender uitgezonden. Streamen via een "
                f"gratis {naam}-account is daardoor de makkelijkste manier om het duel live te volgen.")
    q = [
        (f"Hoe laat begint {homeN} – {awayN}?",
         f"De aftrap is om {nl_tijd(dt)} uur Nederlandse tijd op {nl_datum(dt)}."),
        (f"Is {homeN} – {awayN} gratis te kijken?",
         (f"Ja — maak een gratis account aan bij {naam}, stort €10, kijk de wedstrijd gratis in HD en "
          f"haal je €10 daarna gewoon weer terug.") if prov.get("deposit", True) else
         (f"Ja — maak een gratis account aan bij {naam} en kijk de wedstrijd volledig gratis in HD. "
          f"Geen storting nodig.")),
        ("Kan ik de stream op groot scherm bekijken?",
         "Ja, via Chromecast, AirPlay of een HDMI-kabel zet je de stream op je televisie."),
        waar,
    ]
    return "\n".join(f"<p><strong>{esc(a)}</strong><br>{esc(b)}</p>" for a,b in q)

DISCLAIMER = ("<p><em>Gokken is alleen toegestaan voor personen van 18 jaar en ouder. "
              "Wat kost gokken jou? Stop op tijd. 18+ | Speel bewust.</em></p>")

# ---------- content-delen ----------
def build_content(ctx):
    homeN, awayN = ctx["homeN"], ctx["awayN"]
    hSlug, aSlug = ctx["hSlug"], ctx["aSlug"]
    compN, compSlug = ctx["compN"], ctx["compSlug"]
    dt = ctx["dt"]; venue = ctx["venue"]; city = ctx["city"]
    ronde_txt = ctx.get("ronde_txt") or "Wedstrijd"
    referee = ctx.get("referee"); prov = ctx["prov"]
    datum = nl_datum(dt); kickoff = nl_tijd(dt)

    def clublink(slug, name):
        return f'<a href="/clubs/{slug}">{esc(name)}</a>' if slug else f"<strong>{esc(name)}</strong>"
    hLink, aLink = clublink(hSlug, homeN), clublink(aSlug, awayN)
    compLink = f'<a href="/competities/{compSlug}">{esc(compN)}</a>' if compSlug else f"<strong>{esc(compN)}</strong>"

    # ---- CONTENT (deel 1/3): intro + gratis-kijken-blok + CTA ----
    c1 = []
    c1.append(f'<p><a href="{HUB_PATH}">‹ Alle wedstrijden die je gratis live kunt kijken</a></p>')
    angle = ctx.get("angle") or f"De {esc(compN)} is in Nederland niet op de reguliere tv te zien."
    c1.append(f"<p><strong>{hLink} treft {aLink} op {datum} om {kickoff} uur in de "
              f"{compLink}. {angle} Goed nieuws: je kijkt "
              f"{esc(homeN)} – {esc(awayN)} volledig gratis via {esc(prov['naam'])}.</strong></p>")
    vb_url = ctx.get("vb_url")
    if vb_url:
        c1.append(f'<p>📋 <strong>Lees ook:</strong> onze <a href="{vb_url}">uitgebreide voorbeschouwing van '
                  f'{esc(homeN)} – {esc(awayN)}</a> met voorspelling, odds en de vermoedelijke opstellingen.</p>')
    c1.append(_kijk_blok(prov, homeN, awayN, compN, ctx.get("tv")))
    content = "\n".join(c1)

    # ---- CONTENT-2 (deel 2/3): wedstrijdinfo + over beide clubs ----
    c2 = []
    c2.append("<h3>📅 Wedstrijdinformatie</h3>")
    info = (f"<strong>Wedstrijd:</strong> {esc(homeN)} – {esc(awayN)}<br>"
            f"<strong>Competitie:</strong> {esc(compN)} – {esc(ronde_txt)}<br>"
            f"<strong>Datum:</strong> {datum}<br>"
            f"<strong>Aftrap:</strong> {kickoff} uur (Nederlandse tijd)<br>"
            f"<strong>Stadion:</strong> {esc(venue or city or 'n.n.b.')}")
    if referee:
        info += f"<br><strong>Scheidsrechter:</strong> {esc(referee)}"
    c2.append(f"<p>{info}</p>")
    c2.append(f"<h3>Over {esc(homeN)}</h3>")
    c2.append(team_focus(homeN, ctx.get("hRow"), ctx.get("hForm"), ctx.get("hResults"), compN))
    c2.append(f"<h3>Over {esc(awayN)}</h3>")
    c2.append(team_focus(awayN, ctx.get("aRow"), ctx.get("aForm"), ctx.get("aResults"), compN))
    content2 = "\n".join(c2)

    # ---- CONTENT-3 (deel 3/3): H2H + FAQ + disclaimer ----
    c3 = []
    h2h_ok = [m for m in (ctx.get("h2h") or [])
              if (m.get("goals") or {}).get("home") is not None
              and (m.get("goals") or {}).get("away") is not None]
    if h2h_ok:
        c3.append("<h3>🤝 Onderlinge duels</h3>")
        c3.append("<p>De recente onderlinge geschiedenis tussen beide ploegen:</p>")
        c3.append("<ul>" + "".join("<li>"+esc(_h2h_line(m))+"</li>" for m in h2h_ok[:5]) + "</ul>")
    if vb_url:
        c3.append(f'<p>👉 Meer analyse? Bekijk de <a href="{vb_url}">voorbeschouwing van '
                  f'{esc(homeN)} – {esc(awayN)}</a> met onze voorspelling en de opstellingen.</p>')
    c3.append("<h3>❓ Veelgestelde vragen</h3>")
    c3.append(_faq(homeN, awayN, compN, dt, prov, ctx.get("tv")))
    c3.append(f'<p>👉 <a href="{prov["link"]}"><strong>Kijk {esc(homeN)} – {esc(awayN)} gratis live via '
              f'{esc(prov["naam"])}</strong></a></p>')
    c3.append(f'<p>📺 <a href="{HUB_PATH}"><strong>Bekijk alle wedstrijden die je gratis live kunt kijken</strong></a></p>')
    c3.append(DISCLAIMER)
    content3 = "\n".join(c3)

    return content, content2, content3
