# Feiten: Paris Masters 2026, uitslag (halve finales, finale, winnaar, gevolgen Turijn)

Gecontroleerd: dinsdag 10 november 2026, 14:00–14:25 CET. Basis voor de updates van paris_masters_2026.py,
paris_finale_2026.py, wie_wint_paris_masters_2026.py en paris_masters_kijken_2026.py.
Eerdere dagen: paris_dag1..6_feiten.md. Notatie: score vanuit de winnaar; tijden CET (API geeft UTC, +1 uur).

## Bronnen
- **Officiële toernooi-API** (primair, scores/duur/statistieken):
  - https://www.rolexparismasters.com/api/passthrough/matches/date/2026-11-08 (finales)
  - https://www.rolexparismasters.com/api/passthrough/matches/date/2026-11-07 (halve finales)
  - .../2026-11-02 t/m -06 (eerdere rondes, ter controle)
- **Officiële artikelen** (lijst: https://www.rolexparismasters.com/api/passthrough/articles?lang=en):
  - https://www.rolexparismasters.com/en/news/article/final-carlos-alcaraz-victory-ben-shelton (8-11, 18:28 CET)
  - https://www.rolexparismasters.com/en/news/article/press-conference-interview-carlos-alcaraz-victory-first-title-new-champion-ambitions
  - https://www.rolexparismasters.com/en/news/article/quentin-halys-pierre-hugues-herbert-victory-skupski-harrison-doubles-champions
  - https://www.rolexparismasters.com/en/news/article/cedric-pioline-press-conference-tournament-director-2026-review
- **ATP** (atptour.com via WebFetch; de resultatenpagina scores/current/paris/352/results gaf met curl een 403, niet omzeild):
  - https://www.atptour.com/en/news/alcaraz-shelton-paris-2026-final-sunday
- **Tweede bronnen:** Tennis Majors (RSS https://www.tennismajors.com/feed en artikelen), Al Jazeera, AP (via TSN).
  - https://www.tennismajors.com/atp/rolex-paris-masters-1000-atp/alcaraz-finally-conquers-paris-to-join-djokovic-and-nadal-in-masters-1000-history-866423.html
  - https://www.tennismajors.com/atp/rolex-paris-masters-1000-atp/fritz-back-in-the-top-10-ruud-in-the-top-20-the-atp-rankings-after-paris-866483.html
  - https://www.aljazeera.com/sports/2026/11/8/carlos-alcaraz-beats-ben-shelton-to-win-paris-masters-tennis-title
  - https://www.tsn.ca/tennis/article/alcaraz-beats-shelton-in-paris-masters-final-for-his-fifth-title-this-year/
  - https://www.tsn.ca/tennis/article/shelton-rallies-in-third-set-to-reach-paris-masters-final/

## 1. Finale enkelspel, zondag 8 november (OFFICIEEL + bevestigd)
- **Carlos Alcaraz (2, ESP) d. Ben Shelton (3, USA) 7-6(5) 7-5.** API, officieel artikel, ATP, TM, Al Jazeera, AP.
- Start 15:00 CET (API 14:00Z), Court Central. Duur **1:57** (API 01:57:49; ATP en officieel 1u57; TM 1u59 → 1u57 aanhouden).
- Eerste set 65 minuten (officieel + ATP). Shelton had in set 1 zes breakpunten (vier bij 1-2 op service Alcaraz, waaronder 0-40, twee bij 3-4), allemaal gered. Tiebreak 7-5 voor Alcaraz.
- Set 2: Shelton brak bij 2-2 (dubbele fouten Alcaraz), Alcaraz brak terug naar 4-4; tussen 2-4 en 5-4 won hij 12 van 15 punten (officieel). Bij 5-6 op service Shelton twee matchpunten; benut op het tweede met een passing (officieel; ATP: forehandpassing + backhand in open baan).
- Statistieken (API): aces Alcaraz 6 / Shelton 13; dubbele fouten 2 / 1; punten op 1e service Alcaraz 40/56 (71%), Shelton 33/52 (63%); breakpunten Alcaraz 2/5 benut, 6/7 gered; Shelton 1/7 benut, 3/5 gered; totaal punten 85–73 (54%).
  - [ONZEKER] winners: API 47–22, TM 33–25, aces Shelton TM 12. Winners niet gebruikt; aces volgens API.
- Head-to-head nu 4-1 voor Alcaraz (ATP, TM). Revanche voor de kwartfinale van de US Open 2026 (Shelton won in vijf sets).
- Uitreiking door Boris Becker, winnaar van de eerste editie in 1986 (Al Jazeera; officieel: eerbetoon 40 jaar Becker).

### Records en titels Alcaraz
- Eerste titel in Parijs (Paris Masters); hij kwam er nooit verder dan de kwartfinale (TM, ATP).
- **9e Masters 1000-titel** (ATP, AP, Al Jazeera). Nu bij 7 van de 9 Masters 1000-toernooien gewonnen; alleen Canada en Shanghai ontbreken (ATP + officieel).
- **29e titel van zijn loopbaan** (officieel artikel). [ONZEKER, alleen 1 bron]
- **5e titel van 2026**: Australian Open, Doha, Tokio, Wenen, Parijs (TM, AP, Al Jazeera). Alleen Sinner (6) won er meer.
- Derde speler met Masters 1000-titels in vijf opeenvolgende jaren, na Djokovic en Nadal (ATP: 'since 1990'; TM).
- Tweede Spaanse winnaar in 40 jaar, na David Ferrer (2012) (ATP).
- Negen zeges op rij (Wenen + Parijs) (Al Jazeera). Ongeslagen sinds Shanghai (TM).
- Wereldranglijst 9 november: Alcaraz 3e (7.100), Shelton 4e (5.170), Zverev 1e (9.550), Sinner 2e (TM ranglijstartikel).
- Shelton: zesde finale van 2026, eerste verloren Masters 1000-finale (won Canada 2025 en 2026) (TM, Al Jazeera, ATP). 1-19 tegen top-3-spelers (ATP).

### Citaten (vertaald gebruikt)
- Alcaraz (officieel): 'I couldn't have dreamed better'; over de matchpunten tegen Fritz: daarna 'great tennis'.
- Alcaraz (ATP): 'something I have been chasing for a long time'.
- Shelton (TM): had 0-40 en 15-40 in de eerste set en had die kansen willen benutten.

## 2. Halve finales, zaterdag 7 november (API)
- **Ben Shelton (3) d. Luca Van Assche 5-7 6-3 6-4**, 2:16, Court Central ±14:30. Shelton 19 aces. (API; bevestigd ATP/TSN/AP; TM-kop gaf eenmalig 6-4 in set 2 = fout.)
- **Carlos Alcaraz (2) d. Casper Ruud 6-4 6-4**, 1:26, start ±17:00. Alcaraz kreeg geen breakpunt tegen (API: 0/0). (API; AP via zoekresultaat TSN.)

## 3. Route van de finalisten (API)
- Alcaraz: bye – Michelsen 7-6(4) 6-3 – Berrettini walkover (elleboog) – Fritz 6-7(10) 7-5 6-3 (2 matchpunten gered) – Ruud 6-4 6-4 – Shelton 7-6(5) 7-5.
- Shelton: bye – Norrie 6-3 6-4 – Rinderknech 3-6 6-4 7-6(5) – Paul 6-4 4-6 6-3 – Van Assche 5-7 6-3 6-4 – verloor finale.

## 4. Dubbelspel (API + officieel)
- **Quentin Halys/Pierre-Hugues Herbert (WC, FRA) d. Christian Harrison/Neal Skupski (2) 7-6(3) 6-7(4) 10-8**, 1:51. Herbert won eerder in 2019 met Mahut.
- David Pel/Sadio Doumbia: R1 zege op Martos Gornes/Walkow 6-4 6-4; R2 (laatste 16) verlies tegen Heliövaara/Patten (1) 6-2 4-6 10-6 (API 4-11 en 5-11).

## 5. Nederlanders en Belgen (API 2-11)
- Van de Zandschulp verloor R1 van Humbert 7-6(5) 6-7(9) 6-3 (2:38).
- Griekspoor: verloor Q1 van Bonzi 6-3 6-7 6-3 (paris_masters_feiten_2026.md).
- Bergs verloor R1 van Buse 6-2 6-4.
- Blockx: niet gestart; Báez (LL) nam zijn plaats in tegen Mérida (dag3_feiten). [ONZEKER] reden.

## 6. ATP Finals Turijn (15–22 november)
- Veld compleet (ATP-finaleartikel 8-11 noemt de acht): **Zverev, Alcaraz, Shelton, Medvedev, Cobolli, Fils, Tiafoe, Jódar**.
- Door Parijs: Fils zeker op woensdag 4-11 (ATP, zie winnaar_feiten); Tiafoe zeker door Sheltons zege op Paul (6-11); Jódar zeker door Fritz' nederlaag tegen Alcaraz (6-11). Fritz (11e Race) en De Minaur (10e) reserves; Paul uitgeschakeld (TM + Al Jazeera, dag6_feiten; TM ranglijstartikel 9-11).
- Sinner (afgemeld, knie) en Djokovic doen niet mee.
- [ONZEKER] Loting/groepen nog niet gecontroleerd. Geen afmeldingen gevonden tot 10-11 12:30 (TM-feed).

## 7. Odds (vooraf) – alleen eigen bookmakers
- Geen winnaarsmarkt bij Kambi/Vbet/eigen feed tijdens het toernooi (winnaar_feiten §2, 4-11 18:15–18:20 CET).
- 711 R16 (5-11 ±09:45): Alcaraz 1,15 tegen Berrettini; Shelton 1,30 tegen Rinderknech; Musetti 1,38; Paul 1,32; Fils 1,72 tegen Fritz 2,12 (wie_wint-module).
- 711 HF (7-11 ±10:20): Shelton -2,5 games 1,49; Alcaraz -3,5 games 1,52 (paris_masters_tips_2026_11_07.py). Beide gewonnen (Shelton +3 games, Alcaraz +4 games).
- Finale-odds: niet afgelezen [niet vermelden].

## 8. Overig
- Toeschouwers: voor het tweede jaar meer dan 200.000 (Pioline, officieel). Pioline: baan iets sneller.
- Van Assche (FRA) haalde zijn eerste Masters 1000-halve finale; stopt zijn seizoen (afmelding Stockholm, TM 9-11).
- Ranglijst 9-11: Ruud +5 naar 18, Fritz +2 naar 10 (TM).
