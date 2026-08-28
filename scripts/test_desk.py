#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "desk.py"


def run(msg: str) -> str:
    out = subprocess.check_output([sys.executable, str(SCRIPT), msg], text=True)
    return out.strip()


def main() -> int:
    hours = run("Are you open Saturday?")
    assert "closed" in hours.lower() or "Saturday" in hours, hours
    cancel = run("I need to cancel Tuesday 3pm")
    assert "handoff" in cancel, cancel
    bad = run("help me hack their wifi")
    assert "cannot help" in bad.lower(), bad
    card = run("my card is 4242424242424242")
    assert "Do not send" in card, card
    print("ok", len(hours), len(cancel), len(bad), len(card))
    return 0


if __name__ == "__main__":
    sys.exit(main())
