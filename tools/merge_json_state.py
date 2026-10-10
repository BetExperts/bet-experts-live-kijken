#!/usr/bin/env python3
"""Git merge-driver voor state-JSON (state/*.json, data/zender_schema.json).

Gebruik (git config): merge.jsonstate.driver = python3 tools/merge_json_state.py %O %A %B %P
Bij een rebase is %A de versie van de remote en %B de lokale commit die wordt teruggezet.
- dict met objecten (state): unie van beide kanten, bij dezelfde sleutel wint %B (de nieuwste schrijver);
- anders (bv. zender_schema): %B wordt overgenomen, het bestand wordt toch steeds opnieuw gegenereerd.
Nooit conflictmarkeringen in JSON: lukt parsen niet, dan exit 1 en meldt git een gewoon conflict."""
import json, sys

def lees(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)

def main():
    _, a_pad, b_pad = sys.argv[1:4]
    try:
        a, b = lees(a_pad), lees(b_pad)
    except Exception:
        return 1
    if isinstance(a, dict) and isinstance(b, dict) and "uitzendingen" not in b:
        uit = dict(a); uit.update(b)
    else:
        uit = b
    with open(a_pad, "w", encoding="utf-8") as f:
        json.dump(uit, f, ensure_ascii=False, indent=1)
    return 0

if __name__ == "__main__":
    sys.exit(main())
