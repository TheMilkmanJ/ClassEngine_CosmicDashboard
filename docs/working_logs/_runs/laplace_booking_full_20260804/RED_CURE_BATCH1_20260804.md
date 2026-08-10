# RED CURE batch-1 AGREE-IF residuals — 2026-08-04

**Worker:** Grok Build  
**Packages:** `laplace_booking_full_20260804` + living `PRTOE_hubble_tension.md` (hubble_completion_full residual)  
**Rules:** NO FABRICATIONS · no book unconverged · leave live MCMCs alone · no new long force GetDist  

---

## Cure 1 — hubble 69.9 scoreboard row (minor) — **DONE**

| | |
|---|---|
| **Red** | Scoreboard row “69.9 fixed ε; ceiling ~71” lacked inline pre-bbnfix tag though banner/§3 had it. 69.9 is pre-bbnfix CosmicForge, not chain-sourced. |
| **Cure** | Inline tag on scoreboard lands cell so it cannot be quoted out of context as a live posterior. |
| **File** | `docs/PRTOE_hubble_tension.md` §5 field scoreboard |
| **Edit** | `\| **This model** \| 69.9 fixed ε; ceiling ~71 *(pre-bbnfix CosmicForge; not chain-booked)* \| **0** extra vs ΛCDM \| — \|` |
| **Status** | **CURED** |

Banner + §3 already labeled pre-bbnfix; this pass only closed the quote-out-of-context hole on the scoreboard row.

---

## Cure 2 — laplace RUNBOOK terminology + REPORT “verified” — **DONE**

### 2a RUNBOOK gate language

| | |
|---|---|
| **Red** | `# If gate open: exit 2, does NOT write tables` inverted terminology (“gate open” meant gate not satisfied). |
| **Prior state** | Line had already been partially softened to “If gate NOT satisfied (closed)” but still thin. |
| **Cure** | Consistent dual language: refuse path vs dual-gate-open path + RED_AUDIT publish note + force path fence. |
| **File** | `docs/working_logs/_runs/laplace_booking_full_20260804/RUNBOOK.md` (Step B optional tables block) |
| **Status** | **CURED** |

Comments now read:

- If gate **NOT satisfied** (book refuses: R−1≥0.05 and/or not self-stopped): exit 2, does NOT write tables  
- If dual gate **open** (both R−1 < 0.05 AND converged:true): exit 0, may write tables  
- Production publish prefers `bbnfix_when_ready_all.sh --write-tables` only with RED_AUDIT path  
- Do NOT use `--force-bbnfix` for booking  

### 2b REPORT “verified this pass” / zero stdout capture

| | |
|---|---|
| **Red** | Claim “verified this pass” with zero package stdout capture. |
| **Prior state** | Heading already said “source-checked + smoke captures”; still implied package-local dumps. |
| **Cure** | Downgrade + point to existing refuse card; stdout capture optional residual. |
| **File** | `REPORT.md` section “Script gate behaviour…” |
| **Status** | **CURED** |

Wording now:

- **Verified in source** (refuse strings + exit 2)  
- Refuse card pointer: `docs/working_logs/_runs/bbnfix_booking_20260804_085747/REPORT.md` (**REFUSED**, exit 2)  
- Package `smoke_captures/` = optional residual  
- Partial force log noted: `smoke_force_bbnfix.txt`  

---

## Cure 3 — force-bbnfix status check (no new long force run) — **DONE (code cured; smoke PASS)**

| check | result |
|---|---|
| Source: `--force-bbnfix` does **not** write living `docs/PRTOE_CHAIN_TABLES.md` | **YES** — `scripts/make_getdist_tables.py` L106–228: incomplete gate + force → `unbookable_force=True`; writes only `docs/working_logs/_runs/getdist_force_UNBOOKABLE_<stamp>/CHAIN_TABLES_UNCONVERGED.md` with UNCONVERGED / UNBOOKABLE banner; prints living shelf UNTOUCHED; return 0 |
| In-file UNCONVERGED banner on force path | **YES** — section tags + row `**UNBOOKABLE**` / `**UNCONVERGED**` |
| Living shelf state | **UNTOUCHED** — still OPEN-MACHINE residual freeze 2026-08-04 (no clean force numbers) |
| `getdist_force_UNBOOKABLE_*` dir | **PRESENT** → `getdist_force_UNBOOKABLE_20260804_030942/` |
| Package `smoke_force_bbnfix.txt` | **COMPLETE** — completion lines for UNBOOKABLE tables path + living shelf UNTOUCHED |
| Smoke overall | **PASS** (UNBOOKABLE path only) — do not quote as results |
| Package docs | Documented in this package `REPORT.md` (§ Force-bbnfix status check) + PREFLIGHT kill row for treating force peek as living tables |

**No H₀ booked. Live MCMCs left alone. Force peek ≠ booking.**

---

## Files touched this pass

| path | change |
|---|---|
| `docs/PRTOE_hubble_tension.md` | scoreboard 69.9 inline pre-bbnfix tag |
| `docs/working_logs/_runs/laplace_booking_full_20260804/RUNBOOK.md` | gate terminology dual language |
| `docs/working_logs/_runs/laplace_booking_full_20260804/REPORT.md` | verified-in-source wording + refuse-card pointer + force status section |
| `docs/working_logs/_runs/laplace_booking_full_20260804/PREFLIGHT.md` | force-as-living-shelf kill row |
| `docs/working_logs/_runs/laplace_booking_full_20260804/RED_CURE_BATCH1_20260804.md` | this receipt |

**Not touched:** live chains / MCMCs · PolyChord · booking cards · living `PRTOE_CHAIN_TABLES.md` body · any H₀ posterior numbers.

---

## Status summary

| # | residual | status |
|---|---|---|
| 1 | hubble 69.9 scoreboard untagged | **CURED** |
| 2 | RUNBOOK “gate open” invert + REPORT verified claim | **CURED** |
| 3 | force-bbnfix living-shelf / UNBOOKABLE path | **CODE CURED**; smoke **PASS** → `getdist_force_UNBOOKABLE_20260804_030942/` (living shelf UNTOUCHED; in-file UNCONVERGED banner verified) |

*NO FABRICATIONS. NO EARLY BOOK. NO FORCE PEEK AS RESULTS.*
