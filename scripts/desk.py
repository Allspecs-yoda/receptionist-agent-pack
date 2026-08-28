#!/usr/bin/env python3
"""Local front-desk classifier. No network. No API keys."""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INTENTS = ROOT / "data" / "intents.csv"
HOURS = ROOT / "data" / "hours.csv"

ILLEGAL = re.compile(
    r"\b(hack|exploit|malware|stolen (data|card)|fake id|csam|launder)\b",
    re.I,
)
CARD = re.compile(r"\b(\d{13,19}|cvv|cvc|ssn)\b", re.I)


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def hours_map() -> dict[str, str]:
    rows = load_csv(HOURS)
    return {r["key"]: r["value"] for r in rows if r.get("key")}


def score(text: str, keywords: str) -> int:
    t = text.lower()
    hits = 0
    for k in keywords.split(","):
        k = k.strip().lower()
        if k and k in t:
            hits += 1
    return hits


def match(text: str, intents: list[dict[str, str]]) -> dict[str, str]:
    ranked = sorted(intents, key=lambda r: score(text, r.get("keywords") or ""), reverse=True)
    best = ranked[0]
    if score(text, best.get("keywords") or "") == 0:
        return next(r for r in intents if r["intent"] == "other")
    return best


def reply(text: str) -> str:
    shop = hours_map()
    name = shop.get("shop_name", "the shop")
    if ILLEGAL.search(text):
        return "I cannot help with that. This desk does not take illegal work."
    if CARD.search(text):
        return "Do not send card numbers or SSNs here. Use the shop payment page, or ask for a human."
    intents = load_csv(INTENTS)
    row = match(text, intents)
    extra = ""
    if row["intent"] in {"hours", "hours_today", "after_hours"}:
        extra = f" Hours: Mon–Thu {shop.get('open_mon')}, Fri {shop.get('open_fri')}, Sat {shop.get('open_sat')}."
    if row["intent"] == "location":
        extra = f" Address: {shop.get('address')}."
    hand = " [handoff]" if row.get("handoff") == "yes" else ""
    return f"{name}: {row['reply']}{extra}{hand}"


def main() -> int:
    p = argparse.ArgumentParser(description="Front desk receptionist (local files only)")
    p.add_argument("message", nargs="?", help="Visitor line")
    p.add_argument("--list", action="store_true", help="List intents")
    args = p.parse_args()
    if args.list:
        for r in load_csv(INTENTS):
            print(f"{r['id']:>3}  {r['intent']:<16}  handoff={r['handoff']}")
        return 0
    if not args.message:
        p.print_help()
        return 2
    print(reply(args.message))
    return 0


if __name__ == "__main__":
    sys.exit(main())
