# Tribunal quick card

**Full rules:** repo root `ForGrok&Claude.md` (TURN BOARD + seats + proposals).

| Seat | Role |
|---|---|
| Grok | Blue builder |
| Claude | **Red team only** (pure attack; no blue) |
| ChatGPT | **Neutral referee — no side** |
| Owner | Final; rare override |

**Law:** unanimous AGREE or conversation continues. No 2–1 bookings.

**Owner proxy:** NEXT ISSUE / referee conditions assigned to Grok in `ForGrok&Claude.md` = **owner-assigned tasks**. Grok executes them; owner can override.

**Grok reign:** Subagents freely; lead BUILD. **Hard stops:** no full model-kill, no deletion without owner — **categorize**. Failures → Failures Ledger. Predictions file = final-product voice until seal of finality; repair/fail/amend → Failures Ledger (not scars on the predictions register).

**Task loop (all three seats every time):**  
`Grok TASK COMPLETE → Claude NEXT ISSUE → ChatGPT AGREE/REMAND → Grok BUILD`  
No silent finishes. **ChatGPT is not optional** — referee must agree or the loop does not advance.

**Deadlock:** after a full cycle still stuck → **PHASE = DIAGNOSE** (all three joint).  
Not infinite re-votes. Ask: *was the “blue” that would make purple ever actually applied?*  
If not, the weird shade was red all along. Split mixed claims; name missing ingredients; or leave OPEN.

**Paste for ChatGPT:** `ForGrok&Claude.md` §12b  
**Paste for Claude:** `ForGrok&Claude.md` §12  
**Primary science this week:** T14 link 4

## Audience-facing vs ledger (owner 2026-08-03)

| Surface | Role |
|---|---|
| `PRTOE_PREREGISTERED_PREDICTIONS.md` | **Final-product voice** until seal of finality — not a repair log |
| `PRTOE_FAILURES_LEDGER.md` | Failures, retired routes, **lost predictions**, forced-fit losses |
| working_logs / tribunal handoffs | Repair narrative, instruments, process |

**Red / referee: do not flag predictions recategorization** (move repair/fail/amend out of predictions into Failures) as a defect. That is authorized hygiene. Attack only silent deletion, missing ledger rows, or smuggled bookings.

## Address codes (who → whom)

| Code | To |
|---|---|
| `@TO:GROK` or `>>BLUE` | Grok only |
| `@TO:CLAUDE` or `>>RED` | Claude only |
| `@TO:CHATGPT` or `>>REF` | Referee only |
| `@TO:ALL` or `>>ALL` | Broadcast |

Always pair with `@FROM:GROK|CLAUDE|CHATGPT`.

**Grok watches:** `scripts/watch_tribunal.sh FILE LOG 12 GROK`  
**Claude watches:** same with `CLAUDE`  
**ChatGPT watches:** same with `CHATGPT`

Referee → Grok ≠ Referee → Red. Do not answer the other seat's mail.

