# Brief: nieuwe wedgids-artikelen, kennisbank-uitbreiding (10-11-2026)

Doel: Bet-Experts.nl laten zien als dé Nederlandstalige informatiebron over wedden. Elk artikel beantwoordt één zoekvraag beter
dan wat er nu in het Nederlands te vinden is: compleet, correct, met eigen rekenvoorbeelden en specifiek voor Nederland
(Wet Koa, Kansspelautoriteit, CRUKS, speelgrenzen, Nederlandse vergunde bookmakers).

## Bron van het onderwerp
Het onderwerp komt van een Engelstalige analysesite (je krijgt de URL). Die pagina mag je lezen om te zien welk onderwerp het is.
- Neem NIETS over: geen structuur, geen voorbeelden, geen formuleringen, geen vertaling.
- Doe zelf onderzoek en schrijf het artikel vanaf nul, voor Nederlandse lezers.
- Noem die site NOOIT, ook niet in de docstring als "inspiratie". Noteer alleen "onderwerp: Engelstalige analysesite".
- Ook nooit noemen: FootyMetrics, BetCity, opstellingvandaag, waaroptv, of andere affiliate- of concurrent-sites.

## Vorm (verplicht)
- Volg het sjabloon `specials/wg_xg.py` exact: lees het helemaal. Lees ook `specials/wg_publiceer.py` (controle()) en twee andere `wg_*.py` als voorbeeld.
- Eén module per artikel: `specials/wg_<key>.py`. Daarin:
  - `ITEM_ID = None`, `SLUG`, `RUBRIEK = "6502b66cd9992658b4037cf5"` (Speluitleg);
  - `WEDGIDS_CAT` = de opgegeven categorie, exact: "Wedden uitgelegd", "Wedstrategieën", "Legaal en verantwoord" of "Sporten en regels";
  - `TITEL` ≤ 60 tekens, met de hoofdzoekterm vooraan;
  - `SAMENVATTING` 110–160 tekens;
  - `content`, `content2`, `content3`;
  - de OG-velden (`OG_KOP` met `<span>` voor groen, `OG_EYEBROW`, `OG_CHIPS`, `OG_MOTIEF`, `OG_DATA`), zoals in wg_xg.py.
- De docstring bevat:
  - de zoekwoorden;
  - de feiten met bron-URL en datum;
  - wat bewust is weggelaten;
  - dat de slug 404 gaf (controleer dat met curl: `https://www.bet-experts.nl/nieuws/<SLUG>` moet 404 geven, anders een andere slug kiezen).
- `content` begint met `<p><strong>…</strong></p>`: een vetgedrukte intro die de vraag in 2–3 zinnen volledig beantwoordt. Dat stuk citeert Google of een AI.
- Koppen alleen als `<h3><strong>…</strong></h3>`, bij voorkeur als vraag. Geen `<h2>` en geen `<h4>`.
- Tabellen alleen via `from legaal_data import tabel`.
- Lijsten zonder witruimte tussen `<ul>`/`<li>`-tags.
- Minstens één concreet rekenvoorbeeld met echte getallen. Bereken het in de code en controleer het met asserts.
- Een FAQ aan het eind: `<h3><strong>Veelgestelde vragen</strong></h3>` + 4–6 × `<p><strong>Vraag?</strong><br>Antwoord</p>`.
- De laatste regel is exact: `<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>`.
- Interne links zijn relatief (`/nieuws/...`, `/bookmakers/...`). Elke link moet 200 geven (controleer met curl).
  - Link naar bestaande wedgids-artikelen waar dat relevant is, bijvoorbeeld:
    - `/nieuws/odds-uitgelegd-quotering-lezen`, `/nieuws/wat-is-de-wedstrategie-value-betting`, `/nieuws/wat-is-xg-expected-goals`
    - `/nieuws/wat-is-arbitrage-wedden-de-kunst-van-de-risicovrije-winst`, `/nieuws/wat-houdt-de-wedstrategie-matched-betting-in`
    - `/nieuws/netto-stortingslimiet`, `/nieuws/cruks-de-gokstop-voor-verantwoord-gokken`, `/nieuws/kansspelbelasting-gokwinst-belasting`
    - `/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland`, `/nieuws/legale-goksites-in-nederland`, `/wedgids`
  - Geen affiliatelinks (`/go/`).
- 1200–2200 woorden: volledig, maar zonder opvulling. Korte alinea's van 2–4 zinnen.
- Schrijf in eigen woorden, zakelijk en helder, voor een slimme beginner. Leg jargon uit.
- Eerlijk over risico's. Beloof nooit winst. Benoem waar relevant verantwoord spelen (1 korte zin + link, geen groot regelsblok).
- Nederland-specifiek waar het klopt, bijvoorbeeld:
  - wat de Koa en de KSA voorschrijven: identificatie, CRUKS-check, speelgrenzen, netto-stortingslimiet, verbod op bonussen/reclame;
  - welke markten in Nederland niet mogen (geen corners, geen gele kaarten per speler? → controleer het!);
  - geen betting exchanges met een Nederlandse vergunning (controleer het).
  Controleer elk juridisch feit bij kansspelautoriteit.nl / wetten.overheid.nl / rijksoverheid.nl.
- Infographic (optioneel, alleen als die echt iets toevoegt): een `INFOGRAPHIC`-spec + marker `<!--INFOGRAPHIC-->`, zoals andere wg-modules doen. Bij twijfel weglaten.

## Controle vóór oplevering
- Draai de dry run: `cd live-kijken-agent && ../superodd-agent/.venv/bin/python specials/wg_publiceer.py <key>`. Die toont het aantal woorden en geeft een fout bij problemen.
- Draai ook de module zelf (asserts).
- Render de deelkaart om te testen:
  - `cd live-kijken-agent && ../superodd-agent/.venv/bin/python -c "import sys; sys.path[:0]=['specials','og_kaarten','.']; import wg_publiceer as P; from strategie import render_objs; render_objs({'<key>': P.laad('<key>')}, 'wedgids')"`
  - Bekijk `og/nieuws/wedgids-<key>.webp` met de Read-tool (geen overloop, leesbaar).
  - Commit de kaart niet.
- NIET publiceren, NIET committen, NIET in Telegram posten.

## Oplevering (kort)
Per artikel:
- key, slug, titel, samenvatting, aantal woorden;
- de 3 belangrijkste zoekwoorden;
- de onzekere feiten;
- of er een infographic is.
