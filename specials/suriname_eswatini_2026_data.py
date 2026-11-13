# -*- coding: utf-8 -*-
"""Gedeelde data voor de drie artikelen over Suriname – Eswatini (oefeninterland, zondag 15 november 2026, 18:00, De Vliert).
Feiten: specials/suriname_eswatini_2026_feiten.md (onderzoek 13-11) + litouwen_suriname_2026_feiten.md.
Artikelen: suriname_eswatini_kijken.py, suriname_eswatini_tickets.py, suriname_eswatini_voorspelling.py.
Deelkaarten: og_kaarten/suriname_eswatini_2026.py (3 varianten)."""
RUBRIEK = "64ff0fbd5a8f205b05d5468f"   # Voetbal
KSA = "<p><em>Wat kost gokken jou? Stop op tijd. 18+</em></p>"
SLUGS = {"kijken": "suriname-eswatini-live-kijken",
         "tickets": "suriname-eswatini-tickets",
         "voorspelling": "suriname-eswatini-voorspelling-selectie-historie"}
L = {"kijken": f'<a href="/nieuws/{SLUGS["kijken"]}">Suriname – Eswatini live kijken</a>',
     "tickets": f'<a href="/nieuws/{SLUGS["tickets"]}">tickets voor Suriname – Eswatini</a>',
     "voorspelling": f'<a href="/nieuws/{SLUGS["voorspelling"]}">de voorbeschouwing van Suriname – Eswatini</a>',
     "litouwen": '<a href="/nieuws/litouwen-suriname-live-kijken">Litouwen – Suriname</a>',
     "suriname": '<a href="/clubs/suriname">Suriname</a>',
     "denbosch": '<a href="/clubs/fc-den-bosch">FC Den Bosch</a>',
     "livekijken": '<a href="/live-kijken">live kijken</a>',
     "legaal": '<a href="/nieuws/hoe-weet-ik-of-een-bookmaker-legaal-is-in-nederland">hoe je ziet of een bookmaker legaal is</a>'}

WEDSTRIJD = [("Wedstrijd", "Suriname – Eswatini (oefeninterland)"),
             ("Datum", "Zondag 15 november 2026"),
             ("Aftrap", "18:00 uur Nederlandse tijd (14:00 uur in Suriname)"),
             ("Stadion", "Stadion De Vliert, Victorialaan 21, 's-Hertogenbosch"),
             ("Capaciteit", "± 8.500 plaatsen, kunstgras"),
             ("Tickets", "Vanaf €10, via de ticketshop van FC Den Bosch")]
