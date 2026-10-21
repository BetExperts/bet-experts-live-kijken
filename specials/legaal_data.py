# -*- coding: utf-8 -*-
"""Gedeelde data voor de 'legaal'-artikelen: vergunninghouders online kansspelen volgens de Kansspelwijzer van de Ksa
(stand 21-10-2026, 31 vergunninghouders). Bij wijzigingen alleen hier bijwerken en de artikelen opnieuw draaien.
Producten volgens de vergunning: C = casino, P = poker (spelers tegen elkaar), S = sport, H = paarden."""

PEILDATUM = "21 oktober 2026"
KANSSPELWIJZER = "https://kansspelautoriteit.nl/kansspelwijzer"

# (merk, website, vergunninghouder, producten, review-slug op bet-experts of None)
MERKEN = [
    ("711", "711.nl", "711 B.V.", "CS", "711"),
    ("888", "888.nl", "Godwits Ltd", "CS", "888-casino-sport"),
    ("bet365", "bet365.nl", "Hillside (New Media Malta) PLC", "CPSH", "bet365"),
    ("BetCity", "betcity.nl", "Betent B.V.", "CS", None),
    ("BetMGM", "betmgm.nl", "21 Heads Up Ltd", "CS", "betmgm"),
    ("Betnation", "betnation.nl", "Smart Gaming B.V.", "CS", None),
    ("Bingoal", "bingoal.nl", "Bingoal Nederland B.V.", "CPSH", "bingoal"),
    ("Casino777", "casino777.nl", "Casino de Spa", "C", None),
    ("Circus", "circus.nl", "Cortex Holding S.A.", "CSH", "circus"),
    ("ComeOn! en GetLucky", "comeon.nl, getlucky.nl", "Tulipa Ent Ltd", "CS", "comeon"),
    ("Fair Play Casino", "fairplaycasino.nl", "FPO Nederland B.V.", "C", None),
    ("GGPoker", "ggpoker.nl", "NSUS Malta Ltd", "CP", None),
    ("Hard Rock Casino", "hardrockcasino.nl", "iCasino B.V.", "CS", "hard-rock-casino"),
    ("Holland Casino Online", "hollandcasino.nl", "Holland Casino N.V.", "CPS", None),
    ("Hommerson", "hommerson.nl", "H-Online B.V.", "CS", None),
    ("JACKS.NL", "jacks.nl", "JOI Gaming Ltd", "CSH", "jacks-nl"),
    ("Kansino", "kansino.nl", "Play North Ltd", "C", None),
    ("LeoVegas", "leovegas.nl", "LeoVegas Gaming p.l.c.", "CS", "leovegas"),
    ("Lucky7casino", "lucky7casino.nl", "Noord Zuid Alliantie B.V.", "CS", None),
    ("One Casino en OneSports", "nl.onecasino.com, onesports.nl", "One Casino Ltd", "CS", "one-casino"),
    ("Oranje Palace", "oranjepalace.nl", "Holland Gaming Technology Ltd", "CS", "oranje-palace"),
    ("Starcasino", "starcasino.nl", "Green Island N.V.", "CS", "starcasino"),
    ("TonyBet", "tonybet.nl", "TonyBet OÜ", "CPSH", "tonybet"),
    ("TOTO en Winnitt", "toto.nl, winn-itt.nl", "TOTO Online B.V.", "CPS", "toto"),
    ("Unibet", "unibet.nl", "Optdeck Service Ltd", "CPSH", "unibet"),
    ("Vbet", "vbet.nl", "SCGO Ltd", "CS", "vbet"),
    ("winz.nl", "winz.nl", "Orange Gaming B.V.", "C", None),
    ("ZEbet en ZEturf", "zebet.nl, zeturf.nl", "ZEbetting & Gaming Nederland B.V.", "SH", None),
]
PROD = {"C": "Casino", "P": "Poker", "S": "Sport", "H": "Paarden"}

# Aanraders (ranking Bookmakers-CMS 21-10-2026): (merk, review-slug, affiliate-url)
AANRADERS = [
    ("Bingoal", "bingoal", "https://www.awin1.com/cread.php?awinmid=25635&awinaffid=2599519&campaign=XX&clickref=XX&ued=https%3A%2F%2Fwww.bingoal.nl%2Fnl%2FPromotie%2FWELKOMSTBONUSSPORT25"),
    ("JACKS.NL", "jacks-nl", "https://media.friendsofjacks.eu/redirect.aspx?pid=2527&bid=2224"),
    ("BetMGM", "betmgm", "https://casino.betmgm.nl/redirect.aspx?pid=3781431&lpid=3329&bid=20762"),
    ("Starcasino", "starcasino", "https://media1.affiliates.starcasino.nl/redirect.aspx?pid=2170&bid=1478"),
    ("TOTO", "toto", "https://partner.toto.nl/C.ashx?btag=a_375b_445c_&affid=184&siteid=375&adid=445&c="),
    ("bet365", "bet365", "https://www.bet365.nl/hub/nl-nl/open-account?affiliate=365_02599619"),
]

T = 'style="width:100%;border-collapse:collapse;margin:8px 0 18px"'
TH = 'style="text-align:left;padding:8px 12px;border-bottom:2px solid #169A47"'
TD = 'style="padding:8px 12px;border-bottom:1px solid #E3E8E5"'


def tabel(koppen, rijen):
    kop = "".join(f"<th {TH}>{k}</th>" for k in (koppen or []))
    body = "".join("<tr>" + "".join(f"<td {TD}>{c}</td>" for c in r) + "</tr>" for r in rijen)
    return f"<table {T}>" + (f"<thead><tr>{kop}</tr></thead>" if koppen else "") + f"<tbody>{body}</tbody></table>"


def merk_link(merk, slug):
    return f'<a href="/bookmakers/{slug}">{merk}</a>' if slug else merk


def merken_tabel(filter_prod=None, met_houder=True):
    rijen = []
    for merk, site, houder, prod, slug in MERKEN:
        if filter_prod and filter_prod not in prod:
            continue
        r = [f"<strong>{merk_link(merk, slug)}</strong>", site]
        if met_houder:
            r.append(houder)
        r.append(", ".join(PROD[p] for p in prod))
        rijen.append(r)
    koppen = ["Merk", "Website", "Vergunninghouder", "Vergunning voor"] if met_houder else ["Merk", "Website", "Vergunning voor"]
    return tabel(koppen, rijen)


def aanraders(aantal=6, sport=False):
    items = "".join(
        f'<li><strong>{m}</strong>: <a href="/bookmakers/{s}">lees onze review</a> of '
        f'<a href="{u}" target="_blank" rel="sponsored nofollow noopener">ga direct naar {m}</a></li>'
        for m, s, u in AANRADERS[:aantal])
    return f"<ul>{items}</ul>"
