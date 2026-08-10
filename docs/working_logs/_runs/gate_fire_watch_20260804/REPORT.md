# Gate-fire watch — armed 2026-08-04

**Script:** `scripts/bbnfix_gate_fire_watch.sh`  
**Interval:** 300s  
**On open:** book_bbnfix_when_ready.py then bbnfix_when_ready_all.sh (**tables OFF**)

## Arm-time stamp (historical — watch armed earlier 2026-08-04)
| chain | R−1 | N | converged |
|---|---:|---:|---|
| dyad | 0.128943 | 20302 | false |
| lcdm | 0.086466 | 20409 | false |

## Live currency (re-verify; package `machine_r1_currency_20260804e`)
| chain | R−1 | N | t | converged |
|---|---:|---:|---|---|
| dyad | **0.128943** | 20302 | 2026-08-04T03:25:56 | **false** |
| lcdm | **0.071122** | 21886 | 2026-08-04T13:01:13 | **false** |

Book **REFUSED** (both legs ≥ 0.05 and not self-stopped). No force-bbnfix. No H0 peek. Stage B only after RED_AUDIT.
