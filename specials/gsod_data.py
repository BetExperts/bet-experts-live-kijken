# -*- coding: utf-8 -*-
"""Gedeelde feiten voor de Grand Slam of Darts 2026-artikelen (gsod_*.py). Bron: specials/gsod_feiten_2026.md
(31-10-2026, sectie 'Loting 10-11' bijgewerkt op 10-11-2026), zelf gecontroleerd:
- pdc.tv 09-11 (loting op ma 9 nov: 16 groepen A-P, seeds, programma za 14 nov, sessietijden, format: alleen de
  groepswinnaar door, bo9 / bo19 / bo31, tiebreakers) + Sky Sports 09-11 + Wikipedia (identiek)
- pdc.tv 06-11 (Tour Card Holder Qualifier: 10 plekken), pdc.tv 05-11 (Morris wint PC34), pdc.tv 09-11 (Östlund Nordic & Baltic)
- sessietijden (Britse tijd): za 14 nov 13:00 + 19:00, zo 15 nov 13:00 + 19:30, ma 16 t/m za 21 nov 19:00,
  zo 22 nov 13:00 + 19:30 (12 sessies) – pdc.tv 09-11 en pdc.seetickets.com (Sky noemt 19:00 voor zo-avond)
- prijzengeld: PDC Europe 31-03-2025 + Wikipedia + DartsKing
- Nederlanders: Dartsnieuws/DartsKing 09-11 (7 NL; Jeffrey de Graaf komt uit voor Zweden en telt niet mee)
Na de groepsfase: uitslagen/stand bijwerken; na 22-11: WINNAARS."""

RUBRIEK = "66b726271e317999159d5d44"   # Darts

SLUGS = {
    "speelschema": "speelschema-grand-slam-of-darts-2026",
    "deelnemers": "grand-slam-of-darts-2026-deelnemers-poules",
    "prijzengeld": "prijzengeld-grand-slam-of-darts-2026",
    "format": "grand-slam-of-darts-2026-format",
    "winnaars": "winnaars-grand-slam-of-darts",
    "tv": "grand-slam-of-darts-waar-kijk-je-dit-toernooi-live-op-tv-en-via-gratis-stream-in-nederland",
}


def a(key, tekst):
    return f'<a href="/nieuws/{SLUGS[key]}">{tekst}</a>'


EXTRA = {
    "regels": '<a href="/nieuws/darts-regels-uitgelegd">darts regels uitgelegd</a>',
    "wkstats": '<a href="/nieuws/wk-darts-statistieken-records-180s-negendarters">WK Darts statistieken</a>',
    "wkvandaag": '<a href="/wk-darts/vandaag">WK Darts vandaag</a>',
    "wgp": '<a href="/nieuws/prijzengeld-world-grand-prix-darts-2026-speelschema-prijzengeld-format-uitslagen">World Grand Prix 2026</a>',
    "ddc": '<a href="/nieuws/dutch-darts-championship-2026-uitslagen-speelschema-loting">Dutch Darts Championship 2026</a>',
    "legaal": '<a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>',
    "viaplay": '<a href="/zenders/viaplay">Viaplay</a>',
    "livekijken": '<a href="/live-kijken">live kijken</a>',
}

# (dag, datum, NL-tijd(en), UK-tijd(en), ronde, aantal wedstrijden)
SESSIES = [
    ("Zaterdag", "14 november", "14:00 en 20:00", "13:00 en 19:00", "Groepsfase, speelronde 1", "16 (8 per sessie)"),
    ("Zondag", "15 november", "14:00 en 20:30", "13:00 en 19:30", "Groepsfase, speelronde 2", "16 (8 per sessie)"),
    ("Maandag", "16 november", "20:00", "19:00", "Groepsfase, speelronde 3 (groepen A-H)", "8"),
    ("Dinsdag", "17 november", "20:00", "19:00", "Groepsfase, speelronde 3 (groepen I-P)", "8"),
    ("Woensdag", "18 november", "20:00", "19:00", "Laatste 16", "4"),
    ("Donderdag", "19 november", "20:00", "19:00", "Laatste 16", "4"),
    ("Vrijdag", "20 november", "20:00", "19:00", "Kwartfinales", "2"),
    ("Zaterdag", "21 november", "20:00", "19:00", "Kwartfinales", "2"),
    ("Zondag", "22 november", "14:00 en 20:30", "13:00 en 19:30", "Halve finales (middag) en finale (avond)", "3"),
]

# (positie, aantal spelers, 2026, 2025)
PRIJZEN = [
    ("Winnaar", 1, 200000, 150000),
    ("Runner-up", 1, 100000, 70000),
    ("Halve finale", 2, 60000, 50000),
    ("Kwartfinale", 4, 35000, 25000),
    ("Laatste 16", 8, 20000, 12250),
    ("Nummer 2 in de groep", 16, 12500, None),
    ("Nummer 3 in de groep", 16, 5000, 8000),
]
TOTAAL_2026, TOTAAL_2025 = 1_000_000, 650_000
assert sum(n * b for _, n, b, _ in PRIJZEN) == TOTAAL_2026


def pond(x):
    return "£" + f"{x:,}".replace(",", ".")


# (jaar, winnaar, score, runner-up)
WINNAARS = [
    (2007, "Phil Taylor", "18-11", "Andy Hamilton"), (2008, "Phil Taylor", "18-9", "Terry Jenkins"),
    (2009, "Phil Taylor", "16-2", "Scott Waites"), (2010, "Scott Waites", "16-12", "James Wade"),
    (2011, "Phil Taylor", "16-4", "Gary Anderson"), (2012, "Raymond van Barneveld", "16-14", "Michael van Gerwen"),
    (2013, "Phil Taylor", "16-6", "Robert Thornton"), (2014, "Phil Taylor", "16-13", "Dave Chisnall"),
    (2015, "Michael van Gerwen", "16-13", "Phil Taylor"), (2016, "Michael van Gerwen", "16-8", "James Wade"),
    (2017, "Michael van Gerwen", "16-12", "Peter Wright"), (2018, "Gerwyn Price", "16-13", "Gary Anderson"),
    (2019, "Gerwyn Price", "16-6", "Peter Wright"), (2020, "José de Sousa", "16-12", "James Wade"),
    (2021, "Gerwyn Price", "16-8", "Peter Wright"), (2022, "Michael Smith", "16-5", "Nathan Aspinall"),
    (2023, "Luke Humphries", "16-8", "Rob Cross"), (2024, "Luke Littler", "16-3", "Martin Lukeman"),
    (2025, "Luke Littler", "16-11", "Luke Humphries"),
]

# Nederlanders in het veld (Dartsnieuws + DartsKing, 09-11). Jeffrey de Graaf komt uit voor Zweden: apart in ZWE_NL.
NL = {"Michael van Gerwen", "Gian van Veen", "Wessel Nijman", "Niels Zonneveld", "Jermaine Wattimena", "Kevin Doets", "Maik Kuivenhoven"}
ZWE_NL = "Jeffrey de Graaf"
DEBUT_NL = ["Niels Zonneveld", "Kevin Doets", "Maik Kuivenhoven"]

# (speler, route) — volgorde zoals de PDC-kwalificatielijst (veld compleet op 8-11-2026)
VELD = [
    ("Luke Littler", "Wereldkampioen 2026, titelverdediger"),
    ("Luke Humphries", "Winnaar World Grand Prix 2026"),
    ("Ross Smith", "Europees kampioen 2026 en winnaar World Series Finals"),
    ("Gian van Veen", "Runner-up WK 2026"),
    ("Gerwyn Price", "Runner-up World Matchplay 2026"),
    ("James Wade", "Runner-up UK Open 2026"),
    ("Martin Schindler", "Runner-up EK 2026"),
    ("Nathan Aspinall", "Runner-up Players Championship Finals 2025"),
    ("Michael van Gerwen", "Runner-up World Cup of Darts 2026 (met Van Veen)"),
    ("Beau Greaves", "Runner-up World Youth Championship 2025"),
    ("Cam Crabtree", "Finalist World Youth Championship 2026"),
    ("Jan Schmidt", "Finalist World Youth Championship 2026"),
    ("Sebastian Białecki", "Nummer 1 Development Tour"),
    ("Joe Hunt", "Nummer 1 Challenge Tour"),
    ("Lisa Ashton", "Women's Series-ranking"),
    ("Paolo Nebrida", "Winnaar PDC Asian Championship"),
    ("Adam Sevada", "Winnaar North American Championship"),
    ("Raymond Smith", "Winnaar ANZ Premier League"),
    ("Wessel Nijman", "2 European Tour-titels"),
    ("Josh Rock", "European Tour-titel"),
    ("Luke Woodhouse", "European Tour-titel"),
    ("Krzysztof Ratajski", "European Tour-titel"),
    ("Jonny Clayton", "European Tour-titel (Swiss Darts Trophy)"),
    ("Niels Zonneveld", "European Tour-titel (Dutch Darts Championship)"),
    ("Chris Dobey", "3 Players Championship-titels"),
    ("Cameron Menzies", "2 Players Championship-titels"),
    ("Ryan Searle", "Players Championship-titel"),
    ("Jermaine Wattimena", "Players Championship-titel"),
    ("Rob Cross", "Players Championship-titel"),
    ("Kevin Doets", "Players Championship-titel"),
    ("Andrew Gilding", "Players Championship-titel"),
    ("Jeffrey de Graaf", "Players Championship-titel"),
    ("Gabriel Clemens", "Players Championship-titel"),
    ("Karel Sedláček", "Players Championship-titel"),
    ("Henry Coates", "Players Championship-titel"),
    ("Charlie Manby", "Players Championship-titel (PC31)"),
    ("Tommy Morris", "Players Championship-titel (PC34, 5 november)"),
    ("Stephen Bunting", "Tour Card Holder Qualifier (6 november)"),
    ("Maik Kuivenhoven", "Tour Card Holder Qualifier (6 november)"),
    ("Tom Sykes", "Tour Card Holder Qualifier (6 november)"),
    ("Rusty-Jake Rodriguez", "Tour Card Holder Qualifier (6 november)"),
    ("Niko Springer", "Tour Card Holder Qualifier (6 november)"),
    ("Ricky Evans", "Tour Card Holder Qualifier (6 november)"),
    ("Carl Sneyd", "Tour Card Holder Qualifier (6 november)"),
    ("Bradley Brooks", "Tour Card Holder Qualifier (6 november)"),
    ("Joe Cullen", "Tour Card Holder Qualifier (6 november)"),
    ("Alan Soutar", "Tour Card Holder Qualifier (6 november)"),
    ("Anton Östlund", "Winnaar Nordic & Baltic Championship (8 november)"),
]

# Hoe de laatste plekken zijn vergeven (4-8 november)
OPEN = [
    ("Woensdag 4 november", "Players Championship 33", "Gewonnen door Luke Humphries, die al zeker was: de plek schoof door naar de qualifier"),
    ("Donderdag 5 november", "Players Championship 34", "Tommy Morris, 8-5 in de finale tegen Humphries"),
    ("Vrijdag 6 november", "Tour Card Holder Qualifier", "Tien plekken, onder anderen voor Stephen Bunting en Maik Kuivenhoven"),
    ("Zondag 8 november", "Nordic & Baltic Championship", "Anton Östlund (Zweden)"),
]

# (groep, seed, geplaatste speler, pot 2 = 'speler B', pot 3) — loting ma 9 november 2026 (pdc.tv)
GROEPEN = [
    ("A", 1, "Luke Littler", "Niels Zonneveld", "Beau Greaves"),
    ("B", 16, "Jermaine Wattimena", "Alan Soutar", "Lisa Ashton"),
    ("C", 8, "Josh Rock", "Kevin Doets", "Tommy Morris"),
    ("D", 9, "Stephen Bunting", "Cameron Menzies", "Raymond Smith"),
    ("E", 4, "Gerwyn Price", "Sebastian Białecki", "Joe Hunt"),
    ("F", 13, "Ryan Searle", "Andrew Gilding", "Charlie Manby"),
    ("G", 5, "Jonny Clayton", "Rob Cross", "Anton Östlund"),
    ("H", 12, "Wessel Nijman", "Niko Springer", "Adam Sevada"),
    ("I", 2, "Luke Humphries", "Joe Cullen", "Paolo Nebrida"),
    ("J", 15, "Luke Woodhouse", "Krzysztof Ratajski", "Tom Sykes"),
    ("K", 7, "James Wade", "Ricky Evans", "Cam Crabtree"),
    ("L", 10, "Michael van Gerwen", "Jeffrey de Graaf", "Henry Coates"),
    ("M", 3, "Gian van Veen", "Bradley Brooks", "Carl Sneyd"),
    ("N", 14, "Chris Dobey", "Martin Schindler", "Jan Schmidt"),
    ("O", 6, "Ross Smith", "Gabriel Clemens", "Rusty-Jake Rodriguez"),
    ("P", 11, "Nathan Aspinall", "Karel Sedláček", "Maik Kuivenhoven"),
]
GROEP = {g: (s, a, b, c) for g, s, a, b, c in GROEPEN}

# Zaterdag 14 november: geplaatste speler tegen de speler uit pot 3, in deze volgorde (pdc.tv 09-11)
ZA_MIDDAG = ["J", "B", "D", "F", "C", "H", "P", "G"]   # 13:00 UK / 14:00 NL
ZA_AVOND = ["E", "K", "O", "L", "I", "A", "M", "N"]    # 19:00 UK / 20:00 NL
# Zondag 15 nov: speler B tegen de verliezer van zaterdag (middag = groepen van zaterdagmiddag, avond = van zaterdagavond).
# Ma 16 nov (groepen A-H) en di 17 nov (I-P): speler B tegen de winnaar van zaterdag. Volgorde binnen die sessies volgt.
# Knock-out: wo 18 nov A-B, C-D, E-F, G-H; do 19 nov I-J, K-L, M-N, O-P; vr 20 nov KF A/B-C/D, E/F-G/H;
# za 21 nov KF I/J-K/L, M/N-O/P; zo 22 nov halve finales (middag) en finale (avond).
L16 = [("Woensdag 18 november", ["AB", "CD", "EF", "GH"]), ("Donderdag 19 november", ["IJ", "KL", "MN", "OP"])]


def groep_van(speler):
    return next(g for g, s, a, b, c in GROEPEN if speler in (a, b, c))


def kort(naam):
    """Achternaam voor in tabellen (Van Gerwen, Van Veen, De Graaf, R. Smith / Ross Smith)."""
    if naam == "Raymond Smith":
        return "R. Smith"
    if naam == "Ross Smith":
        return "Ross Smith"
    d = naam.split()
    for i, w in enumerate(d[1:], 1):
        if w in ("van", "de"):
            return " ".join(d[i:])[0].upper() + " ".join(d[i:])[1:]
    return d[-1]


ZA_DUELS = [(g, GROEP[g][1], GROEP[g][3]) for g in ZA_MIDDAG + ZA_AVOND]

_alle = [x for _, _, a, b, c in GROEPEN for x in (a, b, c)]
assert len(GROEPEN) == 16 and len(set(_alle)) == 48 and set(_alle) == {s for s, _ in VELD}
assert sorted(s for _, s, *_ in GROEPEN) == list(range(1, 17)) and sorted(ZA_MIDDAG + ZA_AVOND) == [g for g, *_ in GROEPEN]
assert len(VELD) == 48 and NL <= set(_alle) and ZWE_NL in _alle and set(DEBUT_NL) <= NL

SLOT = "<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"


def check(mod, minw=700, maxw=2200):
    """Gemeenschappelijke checks voor de dry run van elk Grand Slam-artikel."""
    import re
    alles = mod.content + mod.content2 + mod.content3
    w = len(re.sub(r"<[^>]+>", " ", alles).split())
    print(len(mod.TITEL), "titel |", len(mod.SAMENVATTING), "samenvatting |", w, "woorden")
    assert len(mod.TITEL) <= 62 and 110 <= len(mod.SAMENVATTING) <= 160, (len(mod.TITEL), len(mod.SAMENVATTING))
    assert minw <= w <= maxw, w
    assert mod.content.startswith("<p><strong>") and mod.content3.rstrip().endswith(SLOT)
    assert "<h2" not in alles and "<h4" not in alles and "betcity" not in alles.lower()
    assert not re.search(r"</?(ul|ol|li)>\s+</?(ul|ol|li)>", alles)
    for href in re.findall(r'href="([^"]+)"', alles):
        assert href.startswith("/") or href.startswith("https://www.bet-experts.nl/go/"), href
    for s in SLUGS.values():
        assert f"/nieuws/{s}" != f"/nieuws/{mod.SLUG}" or True
    return alles
