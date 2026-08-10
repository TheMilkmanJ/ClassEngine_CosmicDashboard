# DRAFT TASK COMPLETE R1-t14-i6 — fill 4th arm when ready

**NO FABRICATIONS.** Do not paste until summary.json + auto gates.

## Pipeline
| Step | Result |
|---|---|
| cal | PASS |
| nowinding | PASS (disclosed f−1 2-cand) |
| nojet | PASS no false ring · Claude **AGREE** |
| four-branch | 3/4 VERDICT; n-1_f-1 pending as of draft |

## Four-branch (console; verify vs summary.json)

| branch | t | H | n_cand | margin_ok |
|---|---:|---:|---:|---|
| n+1_f+1 | 1.00 | +1.9331 | 5 | True |
| n+1_f-1 | 0.25 | +2.0000 | **2 censored** | True |
| n-1_f+1 | 1.00 | −1.9929 | 5 | True |
| n-1_f-1 | **FILL** | | | |

## Mirrors (provisional)
| pair | residual | notes |
|---|---:|---|
| (1,−1)↔(−1,1) | ~0.36% | mismatched-t 0.25 vs 1.00; left arm **cond. 2 censored** |
| (1,1)↔(−1,−1) | **FILL** | need n-1_f-1 |

## Booking stance (pre-registered)
Production sign(H vs n): **NOT auto-eligible** while any arm is instrument-censored (cond. 2), even if residual &lt;5%.
Smoke-grade H≈sign(n)·2 remains separate (i5).
Instrument fidelity TC may still lock without production sign.

## Conditions 1–6
See `t14_i6_CONDITIONS_1_6_CHECKLIST.md` + auto `t14_i6_TC_GATES.md` when summary lands.

## Non-claims
Not sky IGMF · not top external win · not bbnfix grade · Page OPEN · 4/10 stands

Draft stamped 2026-08-03 14:15
