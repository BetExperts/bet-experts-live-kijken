# Brief: verouderde artikelen bijwerken (dinsdag 10 november 2026, ±14:30 CET)

Je werkt een bestaand, LIVE artikel van Bet-Experts.nl bij. De module staat in `live-kijken-agent/specials/`.
Je past de module aan op dezelfde plek, dus SLUG blijft gelijk. Die module is de bron van de tekst.

## Werkwijze
1. Lees de module, het bijbehorende feitenbestand (`*_feiten*.md`) en de docstring helemaal.
2. Zoek de nieuwe feiten op.
   - Eerst primaire bronnen: de officiële organisatie, de bond of het toernooi zelf.
   - Bevestig daarna bij een tweede betrouwbare nieuwsbron.
   - Onbevestigd neem je niet op, of je brengt het expliciet als verwachting.
   - Leg de feiten met bron-URL en tijdstip van controle vast in het feitenbestand. Vul een bestaand bestand aan, of maak een nieuw `*_feiten*.md`.
3. Herschrijf wat verouderd is: titel, samenvatting, intro, tabellen, FAQ en de update-alinea.
   - Het artikel moet na de update kloppen voor een lezer van vandaag (10-11-2026).
   - Een evenement dat voorbij is beschrijf je in de verleden tijd, met de uitslag bovenaan in de vetgedrukte intro.
   - Richt de titel op wat mensen nu zoeken, bijvoorbeeld "winnaar", "uitslag" of "stand".
4. Werk de velden van de deelkaart bij als die verouderd zijn (bijv. favorieten worden winnaar). Render de kaart volgens de docstring en bekijk de webp met de Read-tool.
5. Draai de dry run van de module. De asserts moeten slagen.

## Huisstijl (verplicht)
- `content` begint met `<p><strong>…</strong></p>`: een vetgedrukte intro die de zoekvraag direct beantwoordt.
- Koppen alleen als `<h3><strong>…</strong></h3>`, nooit `<h2>` of `<h4>`. Tabellen alleen via `legaal_data.tabel`.
- Lijsten zonder witruimte tussen `<ul>`/`<li>`-tags.
- Alleen relatieve interne links. Geen affiliatelinks (`/go/…`), tenzij ze al in de module stonden.
- De laatste regel blijft exact `<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>`.
- TITEL ≤ 60 tekens, SAMENVATTING 110–160 tekens.
- Nederlands in eigen woorden, zakelijk-journalistiek, concreet. Geen opvulling.
- NOOIT noemen: BetCity, opstellingvandaag, waaroptv, FootyMetrics, of andere affiliate- of concurrent-sites als bron.
  - Gebruik opstellingvandaag.nl en waaroptv.nl ook niet om te lezen.
  - Omzeil nooit botbescherming of captcha's.
  - Gebruik geen Anthropic API-key.
- Odds alleen van onze eigen bookmakers, bijvoorbeeld 711 via Kambi (`https://eu-offering-api.kambicdn.com/offering/v2018/sevelevnl/...`), met de datum en het tijdstip van aflezen.

## Niet doen
- NIET publiceren in Webflow, NIET committen of pushen, NIET posten in Telegram. Dat doet de hoofdsessie.
- Verander SLUG niet.

## Oplevering (kort rapport)
- Per module:
  - wat er is veranderd;
  - de nieuwe TITEL en SAMENVATTING;
  - het pad van de kaart;
  - of er afbeeldingen in de content staan die opnieuw gehost moeten worden (pad plus de variabele of URL die in de content zit).
- De onzekere feiten.
- Wat later nog bijgewerkt moet worden.
