"""Officieel Bet365-streamschema (4-11-2026).

Bet365 levert een xlsx 'Live streaming schedule - NL.xlsx' (blad 'query'):
  Date | Time (UK) | Classification | League | Match Details | Geo Blocking
'Geo Blocking' = landen waar de stream GEBLOKKEERD is (Eredivisie/KKD: Netherlands -> in NL niet te zien).
Het schema loopt rollend: voetbal staat er ±1 week vooruit in, NBA/NHL langer.

Gebruik:
  python bet365_streams.py                 # nieuwste xlsx (data/bet365_streams/ of ~/Downloads) -> data/bet365_streams.json
  python bet365_streams.py --push          # idem + git commit/push (zodat GitHub Actions hem gebruikt)
  python bet365_streams.py --check "Atlético Madrid" "Barcelona" 2026-11-08T20:00+01:00
In code:
  status(thuis, uit, dt, sport="Soccer", namen=(...)) -> "ja" | "geblokkeerd" | "nee" | "onbekend"
    ja          = in het schema en in NL te zien
    geblokkeerd = in het schema, maar NL geblokkeerd
    nee         = schema dekt die dag/sport, wedstrijd staat er niet in
    onbekend    = schema reikt (voor deze sport) nog niet tot die datum
  Alleen bij "ja" mogen we een Bet365-stream beloven.
"""
import datetime as dt, glob, json, os, re, subprocess, sys, unicodedata
from zoneinfo import ZoneInfo

HIER = os.path.dirname(os.path.abspath(__file__))
JSON = os.path.join(HIER, "data", "bet365_streams.json")
MAP = os.path.join(HIER, "data", "bet365_streams")
UK = ZoneInfo("Europe/London")
SPORTEN = {"Soccer", "Basketball", "Ice Hockey", "Tennis", "Darts", "Snooker", "American Football", "MMA",
           "Boxing", "Handball", "Volleyball", "Golf", "Cricket", "Baseball", "Futsal"}

# woorden die niets zeggen over welke club het is
STOP = {"fc", "cf", "sc", "ac", "afc", "as", "ss", "sk", "fk", "nk", "club", "de", "the", "cd", "ud", "rc", "sv", "vfb",
        "vfl", "tsg", "bk", "if", "ssc", "us", "bc", "calcio", "kv", "krc", "rsc", "real", "city", "united", "sport",
        "sporting", "athletic", "atletico", "1", "04", "05", "1899", "1900", "1909", "1913", "v", "vs", "and", "of",
        "saint", "st", "olympique", "madrid", "manchester", "lissabon", "lisbon", "racing", "deportivo", "stade", "borussia", "hc", "basket", "basketball"}
# zelfde club, andere naam (alles genormaliseerd, zonder accenten)
ALIAS = {"internazionale": "inter", "alkmaar": "az", "sittard": "fortuna", "den haag": "ado", "psg": "paris",
         "paris saint germain": "paris", "paris sg": "paris", "man utd": "manchester united", "man city": "manchester city",
         "wolves": "wolverhampton", "spurs": "tottenham", "gladbach": "monchengladbach", "cologne": "koln",
         "munich": "munchen", "bayern munchen": "bayern", "bayern munich": "bayern", "nijmegen": "nec",
         "g a eagles": "go ahead eagles", "stade brestois": "brest", "brestois": "brest", "estac troyes": "troyes", "zwolle": "pec", "rotterdam": "feyenoord", "athletic club": "bilbao",
         "athletic bilbao": "bilbao", "atletico madrid": "atletico madrid", "atletico de madrid": "atletico madrid",
         "sporting cp": "sporting lissabon", "sporting lisbon": "sporting lissabon", "sporting lissabon": "sporting lissabon",
         "besiktas": "besiktas", "fenerbahce": "fenerbahce", "galatasaray": "galatasaray", "basaksehir": "basaksehir",
         "istanbul basaksehir": "basaksehir", "goztepe": "goztepe", "napoli": "napoli", "ssc napoli": "napoli"}
# volledige clubnamen waarin STOP-woorden juist het onderscheid maken
VOL = {"real madrid", "real sociedad", "real betis", "atletico madrid", "manchester city", "manchester united",
       "sporting lissabon", "leicester city", "real valladolid", "real oviedo", "athletic"}


def _plat(s):
    s = unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def sleutels(naam):
    """Set herkenningstekens voor een clubnaam: volledige naam (na alias), bekende volle namen, losse woorden."""
    p = _plat(naam)
    for a, b in sorted(ALIAS.items(), key=lambda x: -len(x[0])):
        if re.search(rf"\b{re.escape(a)}\b", p):
            p = re.sub(rf"\b{re.escape(a)}\b", b, p)
    uit = {p}
    if set(p.split()) & {"jong", "women", "vrouwen", "u19", "u21", "u23", "ii", "reserves", "b"}:
        return uit                   # jeugd/vrouwen/tweede elftal: alleen op de volledige naam
    uit |= {v for v in VOL if re.search(rf"\b{re.escape(v)}\b", p)}
    # Amerikaanse teams in het schema: 'COL Avalanche' -> 'avalanche'
    uit |= {w for w in p.split() if w not in STOP and (len(w) >= 4 or w in {"az", "nec", "pec", "ado", "psv", "nac", "aek", "psg", "fcb", "tsv"})}
    kern = " ".join(w for w in p.split() if w not in STOP)
    if kern:
        uit.add("=" + kern)          # naam zonder ruiswoorden: 'Rio Ave FC' -> '=rio ave'
    return uit


def zelfde(a, b):
    sa, sb = sleutels(a), sleutels(b)
    if sa & sb:
        return True
    # 'Amed' / 'Amedspor', 'Gençlerbirliği S.K.' / 'Genclerbirligi': het ene woord begint met het andere (min. 4 tekens)
    wa = {w for w in sa if " " not in w and not w.startswith("=") and len(w) >= 4}
    wb = {w for w in sb if " " not in w and not w.startswith("=") and len(w) >= 4}
    return any(x.startswith(y) or y.startswith(x) for x in wa for y in wb)


# ---------------------------------------------------------------- import (Mac)
def nieuwste_xlsx():
    kand = glob.glob(os.path.join(MAP, "*.xlsx")) + glob.glob(os.path.expanduser("~/Downloads/Live streaming schedule*.xlsx"))
    return max(kand, key=os.path.getmtime) if kand else None


def lees_xlsx(pad):
    import openpyxl
    wb = openpyxl.load_workbook(pad, read_only=True, data_only=True)
    ws = wb["query"] if "query" in wb.sheetnames else wb.worksheets[0]
    items = []
    for r in list(ws.iter_rows(values_only=True))[1:]:
        if not r or not r[0] or r[2] not in SPORTEN:
            continue
        d = r[0].date() if isinstance(r[0], dt.datetime) else dt.date.fromisoformat(str(r[0])[:10])
        t = str(r[1] or "").strip()
        utc = None
        if re.fullmatch(r"\d{1,2}:\d{2}", t):
            h, m = map(int, t.split(":"))
            utc = dt.datetime(d.year, d.month, d.day, h, m, tzinfo=UK).astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
        md = str(r[4] or "").strip()
        delen = re.split(r"\s+(?:v|vs|@)\s+", md, maxsplit=1)
        thuis, uit = (delen + [""])[:2] if len(delen) == 2 else (md, "")
        if " @ " in md:                     # Amerikaans: 'Uit @ Thuis'
            thuis, uit = uit, thuis
        blok = str(r[5] or "")
        items.append({"d": d.isoformat(), "t": t, "utc": utc, "sport": r[2], "league": str(r[3] or ""),
                      "home": thuis.strip(), "away": uit.strip(), "nl": "netherlands" not in blok.lower()})
    return items


def importeer(pad=None):
    pad = pad or nieuwste_xlsx()
    if not pad:
        raise SystemExit("geen streamschema gevonden (data/bet365_streams/*.xlsx of ~/Downloads/Live streaming schedule*.xlsx)")
    nieuw = lees_xlsx(pad)
    if not nieuw:
        raise SystemExit(f"leeg schema: {pad}")
    vanaf = min(i["d"] for i in nieuw)
    oud = []
    if os.path.exists(JSON):
        oud = json.load(open(JSON, encoding="utf-8")).get("items", [])
    grens = (dt.date.today() - dt.timedelta(days=10)).isoformat()
    items = [i for i in oud if grens <= i["d"] < vanaf] + nieuw     # nieuw bestand wint vanaf zijn eerste datum
    items.sort(key=lambda i: (i["d"], i["t"], i["sport"]))
    data = {"bron": os.path.basename(pad), "bron_mtime": dt.datetime.fromtimestamp(os.path.getmtime(pad)).isoformat(timespec="minutes"),
            "items": items}
    vorig = open(JSON, encoding="utf-8").read() if os.path.exists(JSON) else ""
    tekst = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    os.makedirs(os.path.dirname(JSON), exist_ok=True)
    gewijzigd = tekst != vorig
    if gewijzigd:
        open(JSON, "w", encoding="utf-8").write(tekst)
    print(f"bet365-streamschema: {len(nieuw)} regels uit {os.path.basename(pad)} ({vanaf} t/m {max(i['d'] for i in nieuw)}), "
          f"totaal {len(items)}; {'bijgewerkt' if gewijzigd else 'ongewijzigd'}")
    return gewijzigd


def push():
    subprocess.run(["git", "-C", HIER, "add", "data/bet365_streams.json"], check=True)
    if subprocess.run(["git", "-C", HIER, "diff", "--cached", "--quiet"]).returncode == 0:
        print("niets te committen"); return
    subprocess.run(["git", "-C", HIER, "commit", "-m", "data: Bet365-streamschema bijgewerkt", "--", "data/bet365_streams.json"], check=True)
    subprocess.run(["git", "-C", HIER, "pull", "--rebase", "--autostash", "-q"], check=False)
    subprocess.run(["git", "-C", HIER, "push", "-q"], check=True)
    print("gepusht")


# ---------------------------------------------------------------- opzoeken
_CACHE = None


def _items():
    global _CACHE
    if _CACHE is None:
        try:
            _CACHE = json.load(open(JSON, encoding="utf-8")).get("items", [])
        except Exception:
            _CACHE = []
    return _CACHE


def zoek(thuis, uit, wanneer, sport="Soccer", namen=(), marge_uur=3):
    """Het schema-item voor deze wedstrijd (of None). `wanneer` = aware datetime; `namen` = extra (thuis, uit)-paren."""
    w = wanneer.astimezone(dt.timezone.utc)
    paren = [(thuis, uit)] + [p for p in namen if p and all(p)]
    for i in _items():
        if i["sport"] != sport or re.search(r"women|frauen|femen|feminin|vrouwen|u19|u21|u23|youth|reserve", i["league"], re.I):
            continue
        if i["utc"]:
            t = dt.datetime.strptime(i["utc"], "%Y-%m-%dT%H:%MZ").replace(tzinfo=dt.timezone.utc)
            if abs((t - w).total_seconds()) > marge_uur * 3600:
                continue
        elif abs((dt.date.fromisoformat(i["d"]) - w.date()).days) > 1:
            continue
        for h, a in paren:
            if zelfde(h, i["home"]) and zelfde(a, i["away"]):
                return i
    return None


def dekt(wanneer, sport="Soccer"):
    """Reikt het schema voor deze sport tot (en met) de dag van de wedstrijd?"""
    d = wanneer.astimezone(UK).date().isoformat()
    return any(i["sport"] == sport and i["d"] >= d for i in _items())


def status(thuis, uit, wanneer, sport="Soccer", namen=()):
    i = zoek(thuis, uit, wanneer, sport, namen)
    if i:
        return "ja" if i["nl"] else "geblokkeerd"
    return "nee" if dekt(wanneer, sport) else "onbekend"


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["--check"]:
        w = dt.datetime.fromisoformat(a[3])
        sp = a[4] if len(a) > 4 else "Soccer"
        print(status(a[1], a[2], w, sp), zoek(a[1], a[2], w, sp))
    else:
        g = importeer(next((x for x in a if x.endswith(".xlsx")), None))
        if "--push" in a:
            push()
