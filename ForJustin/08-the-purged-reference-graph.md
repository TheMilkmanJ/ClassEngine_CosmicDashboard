# 08 — A hygiene pass destroyed the corpus's internal reference graph

**Found 2026-07-19 while working MATH_SPINE's owed ledger. Partly recoverable, not mechanically.**

## What happened

Commit `9f8c377f` (2026-07-13), "THE DEEP-HYGIENE PASS", says in its own message that it purged
**"~290 bare #N task refs"**. It did not delete them — it replaced them with the literal word
**"docketed"**. Verified on a before/after in `math_story`:

```
-  OPEN (the 3 walls) : c forced-vs-dial (#14 loop calc); exact Ψ₀/f_amp (#11 …
+  OPEN (the 3 walls) : c forced-vs-dial (docketed; loop calc); exact Ψ₀/f_amp (docketed …
```

**The word points at nothing.** There is no docket document in this corpus. Thirty survivors across
seventeen files, and their effect is to make finished work look outstanding — MATH_SPINE's ledger
listed six debts, five already closed, every one tagged "(docketed)".

## Why it can't be restored mechanically

**The numbering drifted.** Pre-purge `math_story` read *"c forced-vs-dial (#14 loop calc)"*. That
item is today's **#45** ("Derive c = 9/10 from the census"); today's #14 is an unrelated step-debt
audit. A literal restore produces a pointer that is confidently wrong, which is worse than one that
is visibly empty.

I also tried generating the recovery map by script. It matched 8 of 30, and included two false
entries — one of which was a sentence I had written myself an hour earlier. Recording that because
it is the same lesson as the purge: **automated text surgery on this corpus produces confident
wreckage.** The map below is hand-checked.

## What is cleanly recoverable

| file | fragment | pre-purge ref |
|---|---|---|
| CODE_MANIFEST | "the spurion (docketed) lifted + P-023 resolved" | `#43` |
| FAILURES_LEDGER | "the ramp re-run and the redesign are the same object \| heavy (docketed; class)" | `#29 class` |
| PREREGISTERED | "genesis calc (docketed) pins z_x near matter-radiation equality" | `#11` |
| UV_completion | "gates WHERE m_e shifts is separate (docketed)" | `#8` |

The rest need reading at `5f95a5e9` in context. None are urgent individually; together they are the
corpus's debt-tracking system.

## The method that works, and is already proven

Not restoration — **adjudication**. For each item: find what it actually was, then check where the
work landed and point there, or state it is open. MATH_SPINE §9 was done this way today and five of
its six debts turned out to be paid, each with a real location:

- KP self-consistency → resolved in that same file, §7a plus the addendum
- spurion identification → `neutrino_sector` §2
- low-scale seesaw → adjudicated by the seesaw duty scan
- leptophilia portal → `dyad_gas` §2
- the gate-0 confirm → #40 confirms rather than decides
- the DE value if Route-D dies → genuinely open

I will keep doing this per file as the audit queue reaches each one. Flagging it here because it is
a corpus-wide condition rather than a file-level defect, and because you should know the shape of
it: **this repository systematically over-states what it still owes.**

## Why that matters more than it sounds

The same drift showed up twice today from opposite directions. `honest_status` was under-rating the
model — its "biggest gap" criticism had been retired by a config change nobody walked back to. This
ledger was over-stating debts that were paid. Both read as caution, both are wrong, and neither gets
caught by anyone re-reading their own summary.

For a model whose entire case rests on being honestly graded, phantom debt is not a harmless error.
You would have walked into a conversation listing five open problems that were solved.
