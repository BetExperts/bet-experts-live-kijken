# -*- coding: utf-8 -*-
"""CTA-afbeelding met de sport-welkomstbonus van een bookmaker in elke voorbeschouwing (wedtips-artikel).

Zelfde ontwerp als de live-kijken-CTA (lk_cta.py): label, logo op een kaart in de merkkleur, bonus als titel,
knop, 'Zo werkt het' in drie stappen, 24+-regel. Per voorbeschouwing kiest het script vast één bookmaker
(hash van het pad), zodat dezelfde pagina altijd dezelfde bonus toont. De afbeelding komt aan het eind van
de sectie 'Voorspelling …'. Alles staat op Cloudflare (be-static), dus niets telt mee voor Webflow-bandbreedte.

Bonusteksten komen uit de Promoties-CMS (sport-welkomstbonussen, 14 okt 2026). Wijzigt een bonus: tekst
hieronder aanpassen, opnieuw draaien, site-static/deploy.py, en de nieuwe vb-cta-*.js in de footer zetten.

  python3 vb_cta.py            # 14 x (desktop + mobiel) renderen + script schrijven
"""
import hashlib, io, json, os
import lk_cta as L

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = L.OUT
BASE_URL = L.BASE_URL
LOGOS = os.path.join(HERE, "assets", "bm")

KNOP = "Claim je welkomstbonus"
RECHTS, RECHTS_M = "Voorwaarden van toepassing", "Voorwaarden v.t."

# slug: (naam, merkkleur logokaart, titel, uitleg, stappen, affiliatelink)
BONUS = {
    "toto": ("TOTO", (0, 118, 49), "€50 aan free bets",
             "Zet €10 in op een sportweddenschap en ontvang daarna vijf free bets van €10.",
             ["Open je TOTO-account", "Zet €10 in (odds 1.50+)", "Ontvang €50 aan free bets"],
             "https://www.bet-experts.nl/go/toto"),
    "bet365": ("Bet365", (2, 123, 91), "Tot €50 aan wedtegoed",
               "Stort €10 en zet in op sport. Daarna ontvang je tot €50 aan wedtegoed.",
               ["Open een Bet365-account", "Stort €10 en zet in", "Ontvang je wedtegoed"],
               "https://www.bet365.nl/hub/nl-nl/open-account?affiliate=365_02599619"),
    "711": ("711", (0, 0, 0), "7× €11 aan free bets",
            "Stort €10, plaats een kwalificerende weddenschap en ontvang €77 aan free bets.",
            ["Open een 711-account", "Stort en wed €10", "Ontvang 7× €11 free bets"],
            "https://media1.711affiliates.nl/redirect.aspx?pid=2395&bid=1505"),
    "starcasino": ("Starcasino", (230, 41, 48), "Free bet tot €80",
                   "Je eerste weddenschap wordt 100% gematcht als free bet, tot €80.",
                   ["Open een account", "Plaats je eerste weddenschap", "Ontvang je free bet"],
                   "https://media1.affiliates.starcasino.nl/redirect.aspx?pid=2170&bid=1478"),
    "circus": ("Circus", (223, 32, 37), "€50 aan free bets",
               "Wed €10 op sport en ontvang na afhandeling 5× €10 aan free bets.",
               ["Open een Circus-account", "Wed €10 op sport", "Ontvang 5 free bets"],
               "https://note.circus.nl/redirect.aspx?pid=12467&bid=10789"),
    "unibet": ("Unibet", (0, 0, 0), "€50 aan free bets",
               "Zet €10 in op een sportweddenschap en ontvang daarna vijf free bets van €10.",
               ["Open een Unibet-account", "Zet €10 in op sport", "Ontvang €50 aan free bets"],
               "https://b1.trickyrock.com/redirect.aspx?pid=86118747&bid=39312"),
    "jacks": ("JACKS.NL", (202, 45, 36), "Free bet tot €100",
              "Je eerste weddenschap wordt 100% gematcht als free bet, tot €100.",
              ["Open een JACKS.NL-account", "Plaats je eerste weddenschap", "Ontvang je free bet"],
              "https://media.friendsofjacks.eu/redirect.aspx?pid=2527&bid=1569"),
    "888": ("888sport", (0, 0, 0), "Tot €50 aan free bets",
            "Je bouwt de free bets op over je eerste drie stortingen.",
            ["Open een 888-account", "Stort €10 en wed", "Ontvang je free bets"],
            "https://media.888.nl/tracking.php?tracking_code&aid=119973&mid=9547&sid=458851&pid=3668"),
    "leovegas": ("LeoVegas", (243, 125, 61), "Free bet tot €50",
                 "Je eerste sportweddenschap wordt 100% gematcht als free bet, tot €50.",
                 ["Registreer bij LeoVegas", "Wed €10+ tegen 1.80+", "Ontvang je free bet"],
                 "https://casino.leovegas.nl/redirect.aspx?pid=3768358&lpid=506&bid=13309"),
    "betmgm": ("BetMGM", (0, 0, 0), "2× 100% Profit Boost",
               "Stort €10 en pak twee keer een 100% Profit Boost (max. €50 winst).",
               ["Open een BetMGM-account", "Stort €10", "Gebruik je Profit Boosts"],
               "https://casino.betmgm.nl/redirect.aspx?pid=3781431&lpid=3329&bid=20762"),
    "bingoal": ("Bingoal", (225, 1, 26), "5 Profit Boosts",
                "Zet €10 in op sport en ontvang vijf Profit Boosts voor je weddenschappen.",
                ["Open een Bingoal-account", "Stort en zet €10 in", "Gebruik je Profit Boosts"],
                "https://www.awin1.com/cread.php?awinmid=25635&awinaffid=2599519&campaign=XX&clickref=XX&ued=https%3A%2F%2Fwww.bingoal.nl"),
    "vbet": ("Vbet", (0, 12, 36), "€50 aan free bets",
             "Plaats een eerste weddenschap van €10 tegen odds van 1.80+ en ontvang €50 aan free bets.",
             ["Open een Vbet-account", "Wed €10 tegen 1.80+", "Ontvang €50 aan free bets"],
             "https://www.vbet.nl/nl/affiliates/?btag=2343788_l356243"),
    "comeon": ("ComeOn!", (0, 0, 0), "Tot €50 aan free bets",
               "€30 + €10 + €10 aan free bets, verdeeld over je eerste drie stortingen.",
               ["Registreer bij ComeOn!", "Stort €10 en wed", "Ontvang je free bets"],
               "https://media.comeon.nl/tracking.php?tracking_code&aid=119973&mid=9802&sid=460575&pid=3507"),
    "oranje-palace": ("Oranje Palace", (255, 255, 255), "3× €14 aan free bets",
                      "Stort minimaal €10, zet €1 in op sport en ontvang drie free bets van €14.",
                      ["Maak een account aan", "Stort minimaal €10", "Zet €1 in op sport"],
                      "https://record.oranjepalaceaffiliates.nl/_uAsFg0X5kIkWqcfzuvZcQGNd7ZgqdRLk/1/"),
}


def teksten(slug):
    naam, _, titel, sub, stappen, _ = BONUS[slug]
    return {"label": "SPORT WELKOMSTBONUS", "titel": titel, "sub": sub, "stappen": stappen, "knop": KNOP,
            "alt": f"Sport welkomstbonus {naam}: {titel}. Klik om een account aan te maken. 24+, voorwaarden van toepassing."}


def main():
    kaart = {}
    for slug, (naam, kleur, *_rest, link) in BONUS.items():
        t, logo = teksten(slug), os.path.join(LOGOS, slug + ".png")
        data, alt = L.render(slug, "bonus", t=t, logo=logo, kleur=kleur, leeftijd="24+", rechts=RECHTS)
        mdata = L.render_mobiel(slug, "bonus", t=t, logo=logo, kleur=kleur, leeftijd="24+", rechts=RECHTS_M)
        naam_d = f"vbcta-{slug}-{hashlib.sha256(data).hexdigest()[:8]}.webp"
        naam_m = f"vbcta-{slug}-m-{hashlib.sha256(mdata).hexdigest()[:8]}.webp"
        open(os.path.join(OUT, naam_d), "wb").write(data)
        open(os.path.join(OUT, naam_m), "wb").write(mdata)
        kaart[slug] = {"u": BASE_URL + naam_d, "m": BASE_URL + naam_m, "a": alt, "l": link}
        print(f"  {naam_d} {len(data) // 1024} KB · {naam_m} {len(mdata) // 1024} KB")
    schrijf_js(kaart)


def schrijf_js(kaart):
    """Klein script (Cloudflare, een jaar gecachet): zet in een voorbeschouwing twee bonus-CTA's: onder de sectie
    'Voorspelling …' en bovenin onder 'Wedstrijdinformatie' (altijd een andere bookmaker). Keuze = vaste hash van
    het pad, dus per artikel altijd dezelfde.
    Staande variant als de tekstkolom smaller is dan 600px (mobiel én tablet met zijbalk)."""
    lijst = [kaart[s] for s in sorted(kaart)]
    js = """(function(){
var B=%s;
function kop(re){var hs=document.querySelectorAll('.w-richtext h3');for(var i=0;i<hs.length;i++){if(re.test(hs[i].textContent||''))return hs[i];}return null;}
var onder=kop(/^\\s*voorspelling\\b/i),boven=kop(/^\\s*wedstrijdinformatie\\b/i);
if(!onder||document.querySelector('.vbcta'))return;
var css=".vbcta{display:block;margin:22px 0 26px;border-radius:18px;background:#0b1117;overflow:hidden;line-height:0;text-decoration:none!important}"+
".vbcta img{display:block;width:100%%;height:auto;transition:transform .5s ease}"+
".vbcta:hover img{transform:scale(1.03)}"+
"@media (prefers-reduced-motion:reduce){.vbcta img{transition:none}}";
var st=document.createElement('style');st.textContent=css;document.head.appendChild(st);
var p=location.pathname,x=2166136261;for(var j=0;j<p.length;j++){x^=p.charCodeAt(j);x=Math.imul(x,16777619)>>>0;}
x^=x>>>16;x=Math.imul(x,0x45d9f3b)>>>0;x=(x^(x>>>16))>>>0;
var a=x%%B.length,b=(a+1+Math.floor(x/B.length)%%(B.length-1))%%B.length;
function zet(h,c){
 var w=document.createElement('a');w.className='vbcta';w.href=c.l;w.target='_blank';w.rel='sponsored nofollow noopener';
 w.setAttribute('aria-label',c.a);
 var mob=(h.parentNode.clientWidth||innerWidth)<600;
 w.innerHTML='<img src="'+(mob?c.m:c.u)+'" alt="'+c.a.replace(/"/g,'&quot;')+'" width="'+(mob?1080:1400)+'" height="'+(mob?960:514)+'" loading="lazy" decoding="async">';
 var n=h.nextElementSibling;while(n&&!/^H[23]$/.test(n.tagName))n=n.nextElementSibling;
 if(n)n.parentNode.insertBefore(w,n);else h.parentNode.appendChild(w);
}
zet(onder,B[a]);
if(boven)zet(boven,B[b]);
})();
""" % json.dumps(lijst, ensure_ascii=False)
    naam = f"vb-cta-{hashlib.sha256(js.encode()).hexdigest()[:10]}.js"
    open(os.path.join(OUT, naam), "w", encoding="utf-8").write(js)
    print("  script:", BASE_URL + naam, len(js.encode()) // 1024, "KB")


if __name__ == "__main__":
    main()
