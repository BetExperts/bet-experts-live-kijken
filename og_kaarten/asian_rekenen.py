# -*- coding: utf-8 -*-
"""Afrekenregels Asian Handicap en Asian Totaal (kwartlijnen = inzet half op beide naburige lijnen)."""

def _een(adj):
    return 1 if adj > 0 else (0 if adj == 0 else -1)


def _split(lijn):
    q = round(lijn * 4) % 4          # 1 of 3 = kwartlijn (.25/.75)
    return (lijn - 0.25, lijn + 0.25) if q in (1, 3) else (lijn,)


def handicap(lijn, doelsaldo):
    """lijn: handicap van jouw team (bv. -0.75); doelsaldo: doelpunten jouw team min tegenstander."""
    d = [_een(doelsaldo + l) for l in _split(lijn)]
    return sum(d) / len(d)


def totaal(lijn, goals, over=True):
    d = [_een((goals - l) if over else (l - goals)) for l in _split(lijn)]
    return sum(d) / len(d)


LABEL = {1: "Winst", 0.5: "Halve winst", 0: "Inzet terug", -0.5: "Half verlies", -1: "Verlies"}


def uitbetaling(uitkomst, inzet, odd):
    """Totale terugbetaling (inclusief inzet)."""
    if uitkomst == 1: return inzet * odd
    if uitkomst == 0.5: return inzet / 2 * odd + inzet / 2
    if uitkomst == 0: return inzet
    if uitkomst == -0.5: return inzet / 2
    return 0.0


if __name__ == "__main__":
    # controle tegen bekende gevallen
    T = [(-0.25, 0, -0.5), (0.25, 0, 0.5), (-0.75, 1, 0.5), (-0.75, 2, 1), (0.75, -1, -0.5), (-1, 1, 0), (1, -1, 0),
         (-1.25, 1, -0.5), (1.25, -1, 0.5), (-1.75, 2, 0.5), (-1.75, 1, -1), (1.75, -2, -0.5), (-2, 2, 0), (2, -2, 0), (-0.5, 0, -1), (0.5, 0, 1)]
    for l, ds, verw in T:
        assert handicap(l, ds) == verw, (l, ds, handicap(l, ds), verw)
    TT = [(2.25, 2, True, -0.5), (2.25, 3, True, 1), (2.75, 3, True, 0.5), (2.75, 3, False, -0.5), (2.0, 2, True, 0), (2.25, 2, False, 0.5), (2.5, 2, False, 1)]
    for l, g, o, verw in TT:
        assert totaal(l, g, o) == verw, (l, g, o, totaal(l, g, o), verw)
    assert abs(uitbetaling(0.5, 10, 1.90) - 14.5) < 1e-9 and uitbetaling(-0.5, 10, 1.9) == 5
    print("alle controles OK")
