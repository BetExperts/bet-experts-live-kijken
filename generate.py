# -*- coding: utf-8 -*-
"""Genereert 'live gratis kijken'-artikelen voor een dag (avond ervoor).
  python3 generate.py --date 2026-09-14 --dry       # niks schrijven, alleen tellen
  python3 generate.py --date 2026-09-14 --preview    # HTML-previews wegschrijven
  python3 generate.py --date 2026-09-14              # live aanmaken + publiceren
Zonder --date: morgen (Europe/Amsterdam)."""
import sys, os, argparse
from datetime import datetime, timedelta
import lk_api as api
import lk_match as M
import lk_build as B
from lk_config import LEAGUES, BASE, WEBFLOW_TOKEN, is_topper, tv_match
import lk_webflow as WF

def target_date(arg):
    if arg: return arg
    d = B._local(datetime.now().astimezone().isoformat()) + timedelta(days=1)
    return f"{d.year}-{d.month:02d}-{d.day:02d}"

def match_on_date(fx, ymd):
    dt = B._local(fx.get("fixture", {}).get("date"))
    return f"{dt.year}-{dt.month:02d}-{dt.day:02d}" == ymd

def write_preview(fd, title):
    os.makedirs(os.path.join(BASE, "preview"), exist_ok=True)
    p = os.path.join(BASE, "preview", fd["slug"] + ".html")
    html = (f"<title>{title}</title><body style='font-family:system-ui;max-width:760px;margin:24px auto;padding:0 16px'>"
            f"<div style='background:#0F1621;color:#cfe6d8;padding:12px 16px;border-radius:10px;font-size:13px'>"
            f"<b>samenvatting:</b> {fd['samenvatting']}</div>"
            f"<h1 style='font-size:20px'>{title}</h1>"
            f"<div style='border-left:3px solid #12833D;padding-left:14px'><b>content</b>{fd['content']}</div>"
            f"<div style='border-left:3px solid #999;padding-left:14px'><b>content-2</b>{fd['content-2']}</div>"
            f"<div style='border-left:3px solid #999;padding-left:14px'><b>content-3</b>{fd['content-3']}</div></body>")
    open(p, "w", encoding="utf-8").write(html)
    return p

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date"); ap.add_argument("--dry", action="store_true")
    ap.add_argument("--preview", action="store_true"); ap.add_argument("--limit", type=int)
    ap.add_argument("--update", action="store_true", help="bestaande artikelen van die datum herschrijven i.p.v. overslaan")
    a = ap.parse_args()
    ymd = target_date(a.date)
    live = not (a.dry or a.preview)
    if live and not WEBFLOW_TOKEN:
        print("FOUT: WEBFLOW_TOKEN ontbreekt (of gebruik --dry/--preview)."); sys.exit(1)

    state = WF.load_state()
    print(f"== Genereren voor {ymd} | modus: {'LIVE' if live else ('PREVIEW' if a.preview else 'DRY')} ==")
    vb_idx = {}
    if WEBFLOW_TOKEN:
        try:
            vb_idx = WF.voorbeschouwing_index()
            print(f"   voorbeschouwing-index: {len([k for k in vb_idx if k.startswith('fid:')])} wedstrijden")
        except Exception as e:
            print(f"   (voorbeschouwing-index overgeslagen: {e})")
    made = 0
    for cfg in LEAGUES:
        resp = api.fixtures(cfg["worker_slug"])
        ups = (resp.get("upcoming") or [])
        day = [fx for fx in ups if match_on_date(fx, ymd)]
        if cfg.get("toppers_only"):
            before = len(day)
            day = [fx for fx in day if is_topper(fx, cfg)]
            print(f"\n{cfg['naam']}: {len(day)} topper(s) op {ymd} (van {before} wedstrijden)")
        elif cfg.get("tv_per_match"):
            before = len(day)
            day = [fx for fx in day if tv_match(fx.get("fixture", {}).get("id")) is not None]
            print(f"\n{cfg['naam']}: {len(day)} wedstrijd(en) met tv-info op {ymd} (van {before}; "
                  f"alleen wedstrijden uit data/tv_wedstrijden.json)")
        else:
            print(f"\n{cfg['naam']}: {len(day)} wedstrijd(en) op {ymd}")
        if not day:
            continue
        stand = api.standings(cfg["worker_slug"])
        for fx in day:
            fid = str(fx.get("fixture", {}).get("id"))
            exists = fid in state
            if exists and not (a.update or a.preview or a.dry):
                print(f"  · overslaan (bestaat al): {fid}"); continue
            ctx = M.gather(fx, standings=stand, force_provider=cfg.get("force_provider"))
            ctx["vb_url"] = WF.voorbeschouwing_url(vb_idx, ctx["fid"], ctx["homeId"], ctx["awayId"])
            keep_slug = state[fid]["slug"] if exists else None   # URL niet breken bij update
            fd, slug, title = M.build_fielddata(ctx, cfg, slug=keep_slug)
            if ctx["vb_url"]:
                print(f"     ↳ voorbeschouwing gelinkt: {ctx['vb_url']}")
            if a.preview:
                p = write_preview(fd, title); print(f"  ✎ preview: {p}")
            elif a.dry:
                print(f"  ○ zou {'bijwerken' if exists else 'maken'}: {title}  [{ctx['prov']['naam']}]")
            elif exists and a.update:
                WF.update_live(state[fid]["item_id"], fd)
                state[fid]["provider"] = ctx["prov"]["naam"]; WF.save_state(state)
                print(f"  ↻ bijgewerkt: {title}  (item {state[fid]['item_id']}) [{ctx['prov']['naam']}]")
            else:
                item_id = WF.create_live(fd)
                state[fid] = {"item_id": item_id, "slug": slug,
                              "match": f"{ctx['homeN']} - {ctx['awayN']}", "date": ymd,
                              "league": cfg["worker_slug"], "provider": ctx["prov"]["naam"],
                              "home_id": str(ctx["homeId"]), "away_id": str(ctx["awayId"])}
                WF.save_state(state)
                print(f"  ✔ live: {title}  (item {item_id}) [{ctx['prov']['naam']}]")
            made += 1
            if a.limit and made >= a.limit: break
        if a.limit and made >= a.limit: break
    print(f"\nKLAAR — {made} artikel(en) verwerkt.")

if __name__ == "__main__":
    main()
