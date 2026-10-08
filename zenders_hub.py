# -*- coding: utf-8 -*-
"""Zenders-hub: één evergreen artikel met alle sportzenders, wat je erop ziet, wat je nodig hebt om te kijken,
de kanaalnummers per provider en (automatisch bijgewerkt) de komende wedstrijden per zender met links naar onze
live-kijken-artikelen.

  python3 zenders_hub.py --preview
  python3 zenders_hub.py              # aanmaken of bijwerken (alleen als er iets veranderd is)

State: state/zenders_hub.json (los van live-kijken.json, zodat cleanup.py hem nooit opruimt).
Bronnen van kanaalnummers/zenderinfo worden nooit genoemd.
"""
import argparse, hashlib, json, os, re, sys
from collections import OrderedDict
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import lk_webflow as WF
from lk_build import esc, kanaal_tabel, MAAND, DAGEN
from lk_config import BASE, WEBFLOW_TOKEN

SLUG = "sportzenders-kanaalnummers"
TITEL = "Sportzenders en kanaalnummers per provider: ESPN, Ziggo Sport, Eurosport en meer"
RUBRIEK_LIVE_KIJKEN = "67d41f195cace9697f8f9ad3"
STATE = os.path.join(BASE, "state", "zenders_hub.json")
AMS = ZoneInfo("Europe/Amsterdam")
TVZ = {k: v for k, v in json.load(open(os.path.join(BASE, "data", "tv_zenders.json"), encoding="utf-8")).items()
       if not k.startswith("_")}

# (kop, zenders in deze groep, wat zie je, wat heb je nodig)
GROEPEN = [
    ("ESPN 1", ["ESPN 1"], TVZ.get("ESPN", []),
     "ESPN 1 zit bij vrijwel elke Nederlandse tv-aanbieder in het basispakket. Met een gewoon tv-abonnement kijk je dus "
     "zonder extra kosten mee, ook in de tv-app van je aanbieder."),
    ("ESPN 2, 3 en 4", ["ESPN 2", "ESPN 3", "ESPN 4"],
     ["Eredivisie en Keuken Kampioen Divisie (de duels die niet op ESPN 1 staan)", "internationaal voetbal van ESPN"],
     "Bij Ziggo zitten ESPN 2, 3 en 4 sinds juli 2026 standaard in elk tv-pakket. Bij KPN en Odido boek je ze erbij met "
     "ESPN Compleet; een los abonnement rechtstreeks bij ESPN bestaat niet."),
    ("ESPN Extra", ["ESPN Extra"], ["Eredivisie en Keuken Kampioen Divisie (wedstrijden die niet op een vast kanaal staan)"],
     "ESPN Extra is geen tv-kanaal maar een extra stream in de ESPN-app. Je kijkt met een ESPN-abonnement via je tv-aanbieder."),
    ("Ziggo Sport 1 (open kanaal)", ["Ziggo Sport 1"], TVZ.get("Ziggo Sport", []),
     "Ziggo Sport is het open kanaal (kanaal 14 bij Ziggo): Ziggo-klanten kijken zonder extra kosten mee met hun gewone "
     "tv-pakket. Bij andere aanbieders is het geen gratis zender. Europese wedstrijden van Nederlandse clubs in de "
     "competitiefase zijn voor iedereen gratis via Ziggo Sport Free (ziggo.nl/uefa en de Ziggo GO-app)."),
    ("Ziggo Sport 2 tot en met 6", ["Ziggo Sport 2", "Ziggo Sport 3", "Ziggo Sport 4", "Ziggo Sport 5", "Ziggo Sport 6"],
     TVZ.get("Ziggo Sport", []),
     "Voor de extra Ziggo Sport-kanalen heb je Ziggo Sport Totaal nodig. Dat pakket boek je bij Ziggo, KPN of Odido. "
     "Ziggo Sport 4 is op Europese voetbalavonden het Switch-kanaal dat live tussen de wedstrijden schakelt."),
    ("Eurosport 1", ["Eurosport 1"], ["Wielrennen (o.a. grote rondes en klassiekers)", "Tennis (Grand Slams)", "Wintersport"],
     "Eurosport 1 zit bij vrijwel alle Nederlandse tv-aanbieders in het basispakket, dus je kijkt zonder extra kosten. "
     "Online kijk je via de tv-app van je aanbieder of via HBO Max met de sportuitbreiding."),
    ("NPO 1, 2 en 3", ["NPO 1", "NPO 2", "NPO 3"], TVZ.get("NOS", []),
     "De NPO-zenders zijn voor iedereen gratis. Online kijk je gratis via NPO Start en de NOS-app."),
    ("Viaplay", ["Viaplay"], TVZ.get("Viaplay", []),
     "Viaplay is een betaalde streamingdienst. Je kijkt via de Viaplay-app of via Viaplay TV bij je tv-aanbieder."),
    ("DAZN", ["DAZN"], TVZ.get("DAZN", []),
     "DAZN is een betaalde streamingdienst. Een deel van de Jupiler Pro League-wedstrijden kun je ook volgen via de "
     "livestream van 711 (gratis account, 18+)."),
    ("Prime Video", ["Prime Video"], TVZ.get("Prime Video", []),
     "Prime Video kijk je met een Amazon Prime-abonnement."),
    ("Apple TV", ["Apple TV"], TVZ.get("Apple TV", []),
     "MLS-wedstrijden zie je met een abonnement op de MLS Season Pass in de Apple TV-app."),
]


def komende(state, now, dagen=3):
    """{zender: [(datum, titel, slug)]} uit de live-kijken-state (komende `dagen` dagen)."""
    out = {}
    eind = (now + timedelta(days=dagen)).date().isoformat()
    vandaag = now.date().isoformat()
    for k, e in state.items():
        if k.startswith("hub:") or not e.get("tv_sig") or e.get("draft"):
            continue
        d = e.get("date", "")
        if not (vandaag <= d <= eind):
            continue
        tv = e["tv_sig"].split("|")[0]
        for z in [x.strip() for x in re.split(r"\s+en\s+|,", tv) if x.strip()]:
            out.setdefault(z, []).append((d, (e.get("match") or "").replace(" - ", " – "), e["slug"]))
    return out


def dag_label(d):
    dt = datetime.strptime(d, "%Y-%m-%d")
    return f"{DAGEN[dt.weekday()]} {dt.day} {MAAND[dt.month - 1]}"


def build(state, now):
    kom = komende(state, now)
    p = ['<p><a href="/live-kijken">‹ Alle wedstrijden live kijken: zenders en tijden</a></p>',
         "<p><strong>Op welk kanaalnummer staat ESPN 1, Ziggo Sport of Eurosport 1 bij jouw provider, en heb je er een "
         "extra abonnement voor nodig? Hieronder staan alle belangrijke sportzenders op een rij: wat je erop ziet, "
         "wat je nodig hebt om te kijken, de kanaalnummers bij Ziggo, KPN, Odido, DELTA en Youfone en welke "
         "wedstrijden er de komende dagen op te zien zijn.</strong></p>",
         "<p>Zoek je een specifieke wedstrijd? Op onze pagina <a href=\"/live-kijken\">live kijken</a> staat per "
         "wedstrijd de exacte zender, de aftraptijd en of er een livestream is.</p>"]
    q = []
    for i, (kop, zenders, comps, nodig) in enumerate(GROEPEN):
        heeft_nr = any(kanaal_tabel(z) for z in zenders)
        blok = [f"<h3>{esc(kop)}: " + ("kanaalnummer en wat je erop ziet" if heeft_nr else "wat je erop ziet en hoe je kijkt")
                + "</h3>"]
        if comps:
            blok.append("<p><strong>Wat zie je erop:</strong> " + esc(", ".join(comps)) + ".</p>")
        blok.append(f"<p><strong>Hoe kijk je:</strong> {esc(nodig)}</p>")
        blok.append("".join(kanaal_tabel(z) for z in zenders))
        wed = sorted((d, t, sl, z) for z in zenders for d, t, sl in kom.get(z, []))
        if wed:
            items = "".join(f'<li>{esc(dag_label(d))}: <a href="/nieuws/{sl}">{esc(t)}</a>'
                            + (f" ({esc(z)})" if len(zenders) > 1 else "") + "</li>" for d, t, sl, z in wed[:8])
            blok.append(f"<p><strong>Binnenkort op {esc(kop)}:</strong></p><ul>{items}</ul>")
        # ESPN en Ziggo Sport in het eerste tekstveld, de rest in content-3 (template heeft daartussen een sectie)
        (p if i < 5 else q).extend(blok)
    q.append("<h3>Veelgestelde vragen over sportzenders</h3>")
    faq = [("Op welk kanaal is ESPN 1?", "Bij Ziggo op kanaal 18, bij KPN en Youfone op 14, bij Odido op 150 en bij DELTA op 421."),
           ("Is Ziggo Sport gratis?", "Voor Ziggo-klanten wel: Ziggo Sport (kanaal 14) zit in elk Ziggo-tv-pakket. Voor de andere "
            "Ziggo Sport-kanalen, en bij andere aanbieders, heb je Ziggo Sport Totaal nodig."),
           ("Op welk kanaal is Eurosport 1?", "Bij Ziggo en Hollandsnieuwe op 25, bij KPN en Youfone op 35, bij Odido op 131 en bij DELTA op 32."),
           ("Welke sportzenders zitten in het basispakket?", "ESPN 1, Eurosport 1 en de NPO-zenders zitten bij vrijwel elke aanbieder "
            "in het basispakket. Bij Ziggo horen daar ook Ziggo Sport (kanaal 14) en ESPN 2, 3 en 4 bij.")]
    q += [f"<p><strong>{esc(a)}</strong><br>{esc(b)}</p>" for a, b in faq]
    q.append('<p><a href="/live-kijken"><strong>Bekijk alle wedstrijden die je live kunt kijken</strong></a></p>')
    q.append("<p><em>Wat kost gokken jou? Stop op tijd. 18+ | Speel bewust.</em></p>")
    meta = ("Alle sportzenders op een rij: kanaalnummers van ESPN, Ziggo Sport en Eurosport bij Ziggo, KPN, Odido en "
            "DELTA, en wat je nodig hebt om te kijken.")
    return "\n".join(p), "\n".join(q), meta[:155]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--preview", action="store_true")
    a = ap.parse_args()
    if not WEBFLOW_TOKEN and not a.preview:
        print("FOUT: WEBFLOW_TOKEN ontbreekt"); sys.exit(1)
    now = datetime.now(timezone.utc).astimezone(AMS)
    content, content3, meta = build(WF.load_state(), now)
    if a.preview:
        os.makedirs(os.path.join(BASE, "preview"), exist_ok=True)
        open(os.path.join(BASE, "preview", SLUG + ".html"), "w", encoding="utf-8").write(
            f"<h1>{esc(TITEL)}</h1><p><em>{esc(meta)}</em></p>{content}{content3}")
        print("preview geschreven"); return
    try:
        st = json.load(open(STATE, encoding="utf-8"))
    except Exception:
        st = {}
    sig = hashlib.md5((TITEL + content + content3).encode()).hexdigest()
    if st.get("sig") == sig:
        print("zenders-hub: ongewijzigd"); return
    fd = {"name": TITEL, "slug": SLUG, "content": content, "content-3": content3, "samenvatting": meta,
          "rubriek": RUBRIEK_LIVE_KIJKEN}
    if st.get("item_id"):
        WF.update_live(st["item_id"], fd); print("zenders-hub: bijgewerkt")
    else:
        fd["publicatiedatum"] = datetime.now(timezone.utc).isoformat()
        st["item_id"] = WF.create_live(fd); print(f"zenders-hub: live /nieuws/{SLUG}")
        try:
            import indexnow
            indexnow.ping([f"https://www.bet-experts.nl/nieuws/{SLUG}"])
        except Exception:
            pass
    st["sig"] = sig
    json.dump(st, open(STATE, "w", encoding="utf-8"), indent=2)


if __name__ == "__main__":
    main()
