# Front Desk Receptionist Agent Pack

A files-only agent you drop into your own runtime: answers the front desk, routes the ask, books nothing illegal, and hands off to a human when it should.

## Who it's for

Solo shops, clinics, studios, and agencies that want a **receptionist agent** they own — not a seat on someone else’s chat.

## What's included

- `AGENT.md` — standing instructions (tone, routing, refuse-illegal, when to escalate).
- `data/intents.csv` — 48 front-desk intents with reply skeleton + handoff flag.
- `data/hours.csv` — sample hours / after-hours copy (edit for your shop).
- `scripts/desk.py` — local classifier + reply (no API key; runs on the files).
- `preview/sample-shift.md` — watermarked sample shift (not the pack).
- `LICENSE` — MIT on the marketplace copy. After payment you may edit, update, and resell (non-exclusive). Foundry keeps a sellable copy.

## Quick start

```bash
python3 scripts/desk.py "Are you open Saturday?"
python3 scripts/desk.py "I need to cancel Tuesday 3pm"
python3 scripts/desk.py --list
```

Paste `AGENT.md` into your own agent (Claude, local LLM, whatever you run). Swap `data/hours.csv` for your hours. Do not put API keys in this repo.

## Custom agents

Need a different agent (intake, estimator, after-hours, bilingual front desk)? Start a Workshop brief: https://allspecs-yoda.github.io/foundry-ledger/#workshop — quote is hours × $75 × complexity after we talk. Dakota approves before the build starts.

## Price

$49 USD. Pay https://buy.stripe.com/3cIaEYcS49358JIh2BcIE0a then open a GitHub issue titled `CLAIM: Front Desk Receptionist Agent Pack` with the receipt last-4. If checkout is down, star + watch and open the same CLAIM issue.

## License

After payment the buyer gets the **full unwatermarked files** and may **edit, update, and resell** them (non-exclusive, unlimited). Night Shift Foundry **keeps a sellable copy** on the marketplace and may sell that same package to anyone else. One ledger row when the product is built.

## Foundry

Shipped by Night Shift Foundry for Dakota (@Allspecs-yoda).
SKU: NSF-20260828-RECEPTIONIST | Decision: list | Cycle: 2026-08-28
