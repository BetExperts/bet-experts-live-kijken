# -*- coding: utf-8 -*-
"""Deelafbeelding live-kijken, ontwerp 2 (gekozen door de gebruiker, 19-10-2026): clubs links/rechts in tegels, in het
midden 'LIVE OP TV' + zenderkaart (logo + kanaalnummer) + aftrap + datum; onderin een badge (gratis / abonnement) en
- alleen als dat echt zo is - 'Ook live via <bookmaker>' of anders 'Live meewedden bij <bookmaker>'.
Zelfde huisstijl als de TOTO 50x-banner (toto50x_banner/). Rendert met Playwright; lk_og.make valt bij een fout terug
op het oude Pillow-ontwerp.
  render(ctx, cfg) -> webp-bytes
"""
import html, io, os, re, tempfile, uuid

BASE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(BASE, "toto50x_banner")            # fonts.css, fonts/, betexperts_logo.png
ZENDERS = os.path.join(BASE, "assets", "zenders")
PROV = os.path.join(BASE, "assets", "og")
E = html.escape
DAGEN = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]
MAANDEN = ["januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus", "september", "oktober", "november", "december"]
ZENDER_LOGO = [("ziggo sport", "ziggo-sport"), ("espn", "espn"), ("viaplay", "viaplay"), ("dazn", "dazn"), ("kijk", "kijk"),
               ("prime video", "prime-video"), ("canal+", "canal-plus"), ("eurosport", "eurosport"), ("hbo max", "hbo-max"),
               ("onefootball", "onefootball"), ("apple tv", "apple-tv"), ("nos", "nos"), ("eyecons", "eyecons")]

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{background:#0B1117;font-family:'Plus Jakarta Sans',sans-serif;-webkit-font-smoothing:antialiased;color:#F5F9FA}
.b{width:1200px;height:630px;position:relative;overflow:hidden;background:#0B1117}
.glow{position:absolute;border-radius:50%;filter:blur(90px)}
.tile{width:150px;height:150px;border-radius:30px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.10);
      display:flex;align-items:center;justify-content:center}
.tile img{width:100px;height:100px;object-fit:contain}
.naam{font:800 26px/1.12 'Poppins';text-align:center;max-width:260px}
.zcard{min-width:230px;height:74px;padding:0 22px;background:#fff;border-radius:18px;display:flex;align-items:center;justify-content:center;gap:12px}
.badge{display:inline-flex;align-items:center;gap:8px;border-radius:999px;padding:9px 18px;font:800 14px 'Plus Jakarta Sans';letter-spacing:1.6px;text-transform:uppercase}
.free{background:#2FD46E;color:#0B1117}
.paid{background:rgba(255,255,255,.10);color:#C9D3DB}
.stream{display:inline-flex;align-items:center;gap:12px;border-radius:14px;padding:10px 16px;background:rgba(255,255,255,.06);
        border:1px solid rgba(255,255,255,.10);font:600 15px 'Plus Jakarta Sans';color:#C9D3DB}
.clogo{width:44px;height:44px;border-radius:12px;background:#fff;display:flex;align-items:center;justify-content:center}
.clogo img{width:34px;height:34px;object-fit:contain}
"""


def _zender(tv):
    """('Ziggo Sport', '6', logo-pad of None) voor de eerste zender in tv ('Ziggo Sport 6 en NPO 1' -> Ziggo Sport 6)."""
    eerste = re.split(r"\s+en\s+|,|/", tv or "")[0].strip()
    m = re.match(r"^(.*?)(?:\s+(\d+|TV\+?|Free))?$", eerste)
    basis, nr = (m.group(1).strip(), (m.group(2) or "").strip()) if m else (eerste, "")
    logo = None
    for sleutel, bestand in ZENDER_LOGO:
        if basis.lower().startswith(sleutel):
            p = os.path.join(ZENDERS, bestand + ".webp")
            logo = p if os.path.exists(p) else None
            break
    return basis, nr, logo


def _png(img, tmp):
    if img is None:
        return None
    p = os.path.join(tmp, f"{uuid.uuid4().hex}.png"); img.save(p); return p


def _html(d):
    club = lambda logo, naam: (f'<div style="display:flex;flex-direction:column;align-items:center;gap:14px;width:270px">'
                               f'<div class="tile">{"<img src=" + chr(34) + E(logo) + chr(34) + ">" if logo else ""}</div>'
                               f'<div class="naam">{E(naam)}</div></div>')
    if d["zender_logo"]:
        kaart = (f'<div class="zcard"><img src="{E(d["zender_logo"])}" style="height:70px;object-fit:contain;margin:0 -12px">'
                 + (f'<span style="font:800 38px Poppins;color:#0B1117">{E(d["kanaal"])}</span>' if d["kanaal"] else "") + "</div>")
    else:
        kaart = f'<div class="zcard"><span style="font:800 28px Poppins;color:#0B1117">{E(d["zender_tekst"])}</span></div>'
    comp_logo = f'<div class="clogo"><img src="{E(d["comp_logo"])}"></div>' if d.get("comp_logo") else ""
    extra = ""
    if d.get("prov_tekst"):
        lg = f'<img src="{E(d["prov_logo"])}" style="height:18px">' if d.get("prov_logo") else ""
        extra = f'<span class="stream">{lg}{d["prov_tekst"]}</span>'
    return f"""<div class="b">
  <div class="glow" style="width:760px;height:560px;left:-220px;top:-300px;background:rgba(22,154,71,.50)"></div>
  <div class="glow" style="width:600px;height:460px;right:-160px;bottom:-260px;background:rgba(22,154,71,.28)"></div>
  <img src="betexperts_logo.png" style="position:absolute;left:56px;top:44px;height:28px">
  <div style="position:absolute;right:56px;top:38px;display:flex;align-items:center;gap:14px">{comp_logo}
    <div style="text-align:right"><div style="font:700 15px 'Plus Jakarta Sans'">{E(d['comp'])}</div>
    <div style="font:600 13px 'Plus Jakarta Sans';color:#8A97A3">{E(d.get('ronde') or '')}</div></div></div>
  <div style="position:absolute;left:46px;right:46px;top:120px;display:flex;justify-content:space-between;align-items:flex-start">
    {club(d['home_logo'], d['home'])}
    <div style="display:flex;flex-direction:column;align-items:center;gap:12px;margin-top:2px">
      <div style="font:700 14px 'Plus Jakarta Sans';letter-spacing:3px;color:#6CC08B">{E(d['eyebrow'])}</div>
      {kaart}
      <div style="font:800 76px/1 'Poppins';margin-top:6px">{E(d['tijd'])}</div>
      <div style="font:600 17px 'Plus Jakarta Sans';color:#C9D3DB">{E(d['datum'])}</div>
    </div>
    {club(d['away_logo'], d['away'])}
  </div>
  <div style="position:absolute;left:0;right:0;top:470px;display:flex;justify-content:center;gap:14px">
    <span class="badge {d['badge_klasse']}">{E(d['badge'])}</span>{extra}</div>
  <div style="position:absolute;left:56px;right:56px;bottom:52px;height:1px;background:rgba(255,255,255,.08)"></div>
  <div style="position:absolute;left:56px;bottom:20px;font-size:13px;color:#8A97A3">Wat kost gokken jou? Stop op tijd. 18+</div>
  <div style="position:absolute;right:56px;bottom:20px;font:700 13px 'Plus Jakarta Sans';color:#6CC08B">bet-experts.nl</div>
</div>"""


def gegevens(ctx, cfg, tmp):
    import og_image as O
    national = bool(cfg.get("landen"))
    prov = ctx.get("prov") or {}
    tv = ctx.get("tv")
    basis, nr, logo = _zender(tv)
    # zelfde regel als de artikeltekst: NL-club in de competitiefase = gratis via Ziggo Sport Free
    ziggo_free = ctx.get("zender_soort") == "ziggo-uefa" and ctx.get("nl_club") and ctx.get("competitiefase")
    if tv and (ctx.get("tv_free") or ziggo_free):
        eyebrow, badge, klasse = "LIVE OP TV", "● Gratis te zien", "free"
    elif tv and ctx.get("tv_paid_only"):
        eyebrow, badge, klasse = "LIVE OP TV", ("In het basispakket" if ctx.get("tv_basis") else "Met abonnement"), "paid"
    elif tv:
        eyebrow, badge, klasse = "LIVE OP TV", "Met abonnement", "paid"
    else:                                                     # alleen een bookmaker-stream
        eyebrow = "GRATIS LIVESTREAM"
        badge, klasse = ("● Gratis na €10 storting" if prov.get("deposit", True) else "● Gratis met account"), "free"
        basis, nr, logo = prov.get("naam", ""), "", None
    pnaam = prov.get("naam") or ""
    plogo = os.path.join(PROV, f"prov-{pnaam.lower().replace(' ', '')}.png")
    plogo = plogo if os.path.exists(plogo) else None
    if tv and ctx.get("stream_ok") and pnaam:
        prov_tekst = f'Ook live via {E(pnaam)} <span style="color:#8A97A3">(met account)</span>'
    elif tv and pnaam:
        prov_tekst = f"Live meewedden bij {E(pnaam)}"
    else:
        prov_tekst = ""
    hl = O.team_logo(ctx.get("homeId"), ctx.get("homeApi"), national)[0]
    al = O.team_logo(ctx.get("awayId"), ctx.get("awayApi"), national)[0]
    lid = cfg.get("league_id") or ((ctx.get("fx") or {}).get("league") or {}).get("id") or ctx.get("league_id")
    cl = O.league_logo(cfg.get("worker_slug", ""), lid)
    dt = ctx["dt"]
    ronde = ctx.get("ronde_txt") or ""
    m = re.match(r"(?i)league stage\s*-\s*(\d+)", ronde) or re.match(r"(?i)league stage\s*-\s*(\d+)", str(ctx.get("ronde_raw") or ""))
    if m and (not ronde or re.match(r"(?i)league stage", ronde)):
        ronde = f"Competitiefase, speelronde {m.group(1)}"
    import banner                                             # korte clubnamen (Gladbach, PSV, ...)
    return {"home": banner.kort(ctx["homeN"]), "away": banner.kort(ctx["awayN"]),
            "home_logo": _png(hl, tmp), "away_logo": _png(al, tmp), "comp_logo": _png(cl, tmp),
            "comp": (cfg.get("naam") or "")[:1].upper() + (cfg.get("naam") or "")[1:],
            "ronde": ronde.replace(", ", " · ") if ronde else "",
            "eyebrow": eyebrow, "zender_logo": logo, "kanaal": nr, "zender_tekst": " ".join(x for x in (basis, nr) if x),
            "tijd": f"{dt:%H:%M}", "datum": f"{DAGEN[dt.weekday()]} {dt.day} {MAANDEN[dt.month - 1]}",
            "badge": badge, "badge_klasse": klasse, "prov_tekst": prov_tekst, "prov_logo": plogo if prov_tekst else None}


def render(ctx, cfg):
    import sys
    sys.path.insert(0, DIR)
    from playwright.sync_api import sync_playwright
    from PIL import Image
    tmp = tempfile.mkdtemp(dir=DIR, prefix=".lk-")
    try:
        d = gegevens(ctx, cfg, tmp)
        pagina = os.path.join(DIR, f".lk-{uuid.uuid4().hex}.html")
        open(pagina, "w", encoding="utf-8").write(
            f"<!doctype html><html><head><meta charset='utf-8'><link rel='stylesheet' href='fonts.css'><style>{CSS}</style></head>"
            f"<body>{_html(d)}</body></html>")
        png = os.path.join(tmp, "uit.png")
        with sync_playwright() as pw:
            b = pw.chromium.launch(); p = b.new_page(viewport={"width": 1200, "height": 630})
            p.goto("file://" + pagina); p.wait_for_load_state("networkidle"); p.evaluate("document.fonts.ready")
            p.locator(".b").screenshot(path=png); b.close()
        os.remove(pagina)
        buf = io.BytesIO(); Image.open(png).convert("RGB").save(buf, "WEBP", quality=88, method=6)
        return buf.getvalue()
    finally:
        import shutil
        shutil.rmtree(tmp, ignore_errors=True)
