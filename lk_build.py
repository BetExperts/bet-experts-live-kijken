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

def team_focus(team, row, form):
    if not row:
        base = f"<strong>{esc(team)}</strong> gaat op zoek naar een goed resultaat in dit duel."
        if form:
            base += f" Recente vorm: {form_dashes(form)}. {form_zin(form)}"
        return f"<p>{base}</p>"
    alld = row.get("all", {}) or {}
    g = alld.get("goals", {}) or {}
    rank = row.get("rank"); pnt = row.get("points")
    pl = alld.get("played"); w = alld.get("win"); d = alld.get("draw"); l = alld.get("lose")
    gf = g.get("for"); ga = g.get("against")
    frm = form or row.get("form")
    zin = (f"<strong>{esc(team)}</strong> staat na {pl} speelronde(s) op de {_ordinal(rank)} plaats in de Süper Lig "
           f"met {pnt} punten uit {w} zege(s), {d} keer gelijk en {l} nederla(a)g(en). "
           f"Het doelsaldo staat op {gf}-{ga}.")
    if frm:
        zin += f" Recente vorm: {form_dashes(frm)}. {form_zin(frm)}"
    return f"<p>{zin}</p>"

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
def _kijk_blok(prov, homeN, awayN, comp):
    naam = prov["naam"]; link = prov["link"]; M = f"{esc(homeN)} vs {esc(awayN)}"
    out = [f"<h3>Gratis live kijken via {esc(naam)}</h3>"]
    if naam == "TOTO":
        out.append(f"<p>De wedstrijd tussen {esc(homeN)} en {esc(awayN)} is niet live te zien op de Nederlandse "
                    f"televisie. De enige manier om dit {esc(comp)}-duel live te volgen in Nederland is via "
                    f"{esc(naam)} met een gratis account.</p>")
    else:
        out.append(f"<p>Je kunt {M} volledig gratis livestreamen via {esc(naam)}. Met een gratis "
                    f"{esc(naam)}-account heb je directe toegang tot de stream — {esc(comp)}-wedstrijden zijn "
                    f"in Nederland namelijk niet op de reguliere tv te zien.</p>")
    out.append(f"<p><strong>Zo werkt gratis kijken via {esc(naam)}:</strong></p>")
    out.append("<ol>"
               "<li>Maak een gratis account aan via de link hieronder</li>"
               "<li>Stort €10 — het minimumbedrag voor toegang tot de livestream</li>"
               f"<li>Kijk {M} volledig gratis in HD</li>"
               "<li>Haal daarna je €10 er gewoon weer af</li>"
               "</ol>")
    out.append("<p>Je kijkt de wedstrijd dus volledig gratis — de €10 verdwijnt niet.</p>")
    if prov.get("cast"):
        out.append(f"<p><strong>Wil je op groot scherm kijken?</strong> Cast de {esc(naam)}-stream via "
                    f"Chromecast, AirPlay of een HDMI-kabel naar je televisie — volledig gratis.</p>")
    out.append(f'<p>👉 <a href="{link}"><strong>Maak een gratis {esc(naam)}-account aan en kijk '
               f'{esc(homeN)} – {esc(awayN)} live</strong></a></p>')
    return "\n".join(out)

# ---------- FAQ ----------
def _faq(homeN, awayN, comp, dt, prov):
    naam = prov["naam"]
    q = [
        (f"Hoe laat begint {homeN} – {awayN}?",
         f"De aftrap is om {nl_tijd(dt)} uur Nederlandse tijd op {nl_datum(dt)}."),
        (f"Is {homeN} – {awayN} gratis te kijken?",
         f"Ja — maak een gratis account aan bij {naam}, stort €10, kijk de wedstrijd gratis in HD en "
         f"haal je €10 daarna gewoon weer terug."),
        ("Kan ik de stream op groot scherm bekijken?",
         "Ja, via Chromecast, AirPlay of een HDMI-kabel zet je de stream op je televisie."),
        (f"Waarom is {homeN} – {awayN} niet op de Nederlandse tv?",
         f"De {comp} wordt in Nederland niet door een reguliere tv-zender uitgezonden. Streamen via een "
         f"gratis {naam}-account is daardoor de makkelijkste manier om het duel live te volgen."),
    ]
    return "\n".join(f"<p><strong>{esc(a)}</strong><br>{esc(b)}</p>" for a,b in q)

DISCLAIMER = ("<p><em>Gokken is alleen toegestaan voor personen van 18 jaar en ouder. "
              "Speel bewust en verantwoord. Stop op tijd. 18+ | Loot? Wat doet het met jou? | Speel bewust.</em></p>")

# ---------- content-delen ----------
def build_content(ctx):
    homeN, awayN = ctx["homeN"], ctx["awayN"]
    hSlug, aSlug = ctx["hSlug"], ctx["aSlug"]
    compN, compSlug = ctx["compN"], ctx["compSlug"]
    dt = ctx["dt"]; venue = ctx["venue"]; city = ctx["city"]; ronde = ctx["ronde"]
    referee = ctx.get("referee"); prov = ctx["prov"]
    datum = nl_datum(dt); kickoff = nl_tijd(dt)

    def clublink(slug, name):
        return f'<a href="/clubs/{slug}">{esc(name)}</a>' if slug else f"<strong>{esc(name)}</strong>"
    hLink, aLink = clublink(hSlug, homeN), clublink(aSlug, awayN)
    compLink = f'<a href="/competities/{compSlug}">{esc(compN)}</a>' if compSlug else f"<strong>{esc(compN)}</strong>"

    # ---- CONTENT (deel 1/3): intro + gratis-kijken-blok + CTA ----
    c1 = []
    c1.append(f"<p><strong>{hLink} treft {aLink} op {datum} om {kickoff} uur in speelronde {ronde} van de "
              f"{compLink}. Veel fans in Nederland zoeken naar een manier om Turkse topwedstrijden live te "
              f"volgen, want de {esc(compN)} is hier niet op de reguliere tv te zien. Goed nieuws: je kijkt "
              f"{esc(homeN)} – {esc(awayN)} volledig gratis via {esc(prov['naam'])}.</strong></p>")
    vb_url = ctx.get("vb_url")
    if vb_url:
        c1.append(f'<p>📋 <strong>Lees ook:</strong> onze <a href="{vb_url}">uitgebreide voorbeschouwing van '
                  f'{esc(homeN)} – {esc(awayN)}</a> met voorspelling, odds en de vermoedelijke opstellingen.</p>')
    c1.append(_kijk_blok(prov, homeN, awayN, compN))
    content = "\n".join(c1)

    # ---- CONTENT-2 (deel 2/3): wedstrijdinfo + over beide clubs ----
    c2 = []
    c2.append("<h3>📅 Wedstrijdinformatie</h3>")
    info = (f"<strong>Wedstrijd:</strong> {esc(homeN)} – {esc(awayN)}<br>"
            f"<strong>Competitie:</strong> {esc(compN)} – Speelronde {ronde}<br>"
            f"<strong>Datum:</strong> {datum}<br>"
            f"<strong>Aftrap:</strong> {kickoff} uur (Nederlandse tijd)<br>"
            f"<strong>Stadion:</strong> {esc(venue or city or 'n.n.b.')}")
    if referee:
        info += f"<br><strong>Scheidsrechter:</strong> {esc(referee)}"
    c2.append(f"<p>{info}</p>")
    c2.append(f"<h3>Over {esc(homeN)}</h3>")
    c2.append(team_focus(homeN, ctx.get("hRow"), ctx.get("hForm")))
    c2.append(f"<h3>Over {esc(awayN)}</h3>")
    c2.append(team_focus(awayN, ctx.get("aRow"), ctx.get("aForm")))
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
    c3.append(_faq(homeN, awayN, compN, dt, prov))
    c3.append(f'<p>👉 <a href="{prov["link"]}"><strong>Kijk {esc(homeN)} – {esc(awayN)} gratis live via '
              f'{esc(prov["naam"])}</strong></a></p>')
    c3.append(DISCLAIMER)
    content3 = "\n".join(c3)

    return content, content2, content3
