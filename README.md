# live-kijken-agent

Schrijft automatisch **"live gratis kijken"-artikelen** voor de **Trendyol Süper Lig**
in de Webflow Nieuws-collectie. Per wedstrijd één artikel met een gratis-livestream-uitleg
(afwisselend **TOTO** en **Bet365**), wedstrijdinfo, de stand/vorm van beide clubs, een FAQ
en — als die bestaat — een link naar de **voorbeschouwing** van dezelfde wedstrijd.

Zelfde infra als de `opstellingen-agent`. Data komt uit de Bet-Experts API-proxy
(Cloudflare Worker) — geen losse API-key nodig.

## Hoe het werkt
- **Timing:** de avond ervóór (cron 18:00 UTC ≈ 20:00 NL) zodat de artikelen 's nachts
  geïndexeerd worden en 's ochtends op Google staan.
- **Titel:** gevarieerd per wedstrijd (deterministisch via `random.seed(fixture_id)`),
  bevat "live gratis kijken op tv" in wisselende vormen, soms met datum/tijd.
- **TOTO/Bet365:** deterministisch afgewisseld op fixture-id-pariteit (~50/50). Bet365 krijgt
  de Chromecast/AirPlay-alinea erbij.
- **Rubriek:** Algemeen. **Competitie:** referentie naar Süper Lig. Velden `publicatiedatum`,
  `datum-tijd-van-wedstrijd`, `tijd-wedstrijd` worden ingevuld.
- **Voorbeschouwing-link:** matcht op fixture-id (fallback team-id-paar) uit de recent
  gepubliceerde voorbeschouwingen.

## Commando's
```bash
# Dry-run (niks schrijven, alleen tellen)
python generate.py --date 2026-09-19 --dry

# HTML-previews wegschrijven naar preview/
python generate.py --date 2026-09-19 --preview

# Live aanmaken + publiceren (vereist WEBFLOW_TOKEN)
WEBFLOW_TOKEN=... python generate.py --date 2026-09-19

# Zonder --date = morgen (Europe/Amsterdam)
```

Opschonen (artikelen > RETENTION_DAYS na de wedstrijd, met redirect-csv):
```bash
WEBFLOW_TOKEN=... python cleanup.py            # live
python cleanup.py --dry                        # alleen tonen
```

## Deploy (GitHub Actions)
1. Repo pushen (publiek → onbeperkte Actions-minuten).
2. Secret `WEBFLOW_TOKEN` toevoegen (Settings → Secrets → Actions).
3. `generate.yml` draait elke avond; `cleanup.yml` elke ochtend.

## Uitbreiden naar meer competities
Voeg een entry toe aan `LEAGUES` in `lk_config.py` met `worker_slug`, `comp_slug`,
`naam` en `comp_id` (item-id in de Competities-collectie).
