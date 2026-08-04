# Debts + hard wins full refresh — 2026-08-04

**Stamp:** 2026-08-04T02:36 local (tables currency; live gates re-checked same stamp)  
**Worker:** Grok Build (SCIENCE_DEBTS + hard-wins + residual inventory currency)  
**Rule:** NO FABRICATIONS · no invent closes for D2–D8 open arms · no PolyChord · MCMCs **read progress only** (leave alone)

## Package contents

| File | Role |
|---|---|
| `REPORT.md` | This master report |
| `DEBT_TABLE.md` | D1–D9 grades + residuals (single source of truth) |
| `HARD_WINS_TABLE.md` | Hard-win ranking + live evidence (single source of truth) |

## Surfaces updated (same stamp)

| Path | Change |
|---|---|
| `docs/working_logs/SCIENCE_DEBTS_2026-08-03.md` | Currency board + **2026-08-04 FULL REFRESH** (D1–D9 complete) |
| `docs/working_logs/_runs/hard_wins_90day_20260803/REPORT.md` | Status table: BBN ε **ARITHMETIC VERIFIED (internal)** / **EXTERNAL WIN PENDING (no DOI)**; bbnfix **NOT YET**; T14 candidate-local |
| `docs/working_logs/_runs/RESIDUAL_IMPROVE_INVENTORY_20260803.md` | Night+ **FULL REFRESH** — all residual classes A–H |
| `docs/working_logs/_runs/PROMOTION_BOARD_20260803_IMPROVE.md` | 2026-08-04 stamp: promotions still honest + still blocked |

---

## Live machine gates (authoritative)

Commands run this stamp:

```bash
tail -1 chains/dyad_mnu_bbnfix.progress chains/cmp_lcdm_mnu_bbnfix.progress
python3 scripts/book_bbnfix_when_ready.py          # → REFUSED
python3 scripts/finalize_h0_at_convergence.py        # → NOT YET
python3 scripts/bbnfix_mcmc_watch_diag.py            # → UNBOOKABLE
python3 papers/bbn-eps-bound/recompute_eps_bound.py  # → PASS 3.196%
```

| Chain | N | R−1 | converged | bookable |
|---|---:|---:|---|---|
| `cmp_lcdm_mnu_bbnfix` | 19013 | **0.059055** | false | **false** |
| `dyad_mnu_bbnfix` | 18837 | **0.189201** | false | **false** |

GetDist diagnostic max GR ~**0.071** / ~**0.086** — still &gt;0.05; **not** booking authority. Chain files still grow; progress lag is normal.

---

## Hard wins (summary)

| Rank | Win | Status |
|---:|---|---|
| 1 | arXiv / Fairbank | **OWNER HOLD** |
| 2 | BBN ε &lt;3.2% (2σ) recompute | **ARITHMETIC VERIFIED (internal)** (3.196%≈3.20% PASS); **EXTERNAL WIN PENDING (no DOI)** |
| 3 | bbnfix GetDist booking | **NOT YET** |
| (thread) | T14 i6 | **CANDIDATE CLOSED (config-local)**; production **KILLED** |

Detail: `HARD_WINS_TABLE.md`.

---

## Science debts (summary grades)

| ID | Grade |
|---|---|
| D1 | **CANDIDATE-LOCAL** (production **KILLED**) |
| D2 | **OPEN-BLOCKED** (onset MCMC bias; instrument partial) |
| D3 | **PARTIAL / OPEN-THEORY** (quartet paid; forward A_ωJ open) |
| D4 | **OPEN-THEORY** (horn-a residual sized) |
| D5 | **LOCKED packaging / OPEN residual** |
| D6 | **PARTIAL / OPEN** (RM geometry paid; void open) |
| D7 | **OPEN-BLOCKED** (F-A3) |
| D8 | **PARKED / BLOCKED** |
| D9 | **OPEN** (coeff paid; dynamics open; no CANDIDATE) |

Detail: `DEBT_TABLE.md`.

---

## Residual classes (inventory pointer)

Full class list A–H in:

`docs/working_logs/_runs/RESIDUAL_IMPROVE_INVENTORY_20260803.md`  
section **FULL REFRESH 2026-08-04 night+ — ALL residual classes**

| Class | Contents |
|---|---|
| A | OPEN-MACHINE (bbnfix, RouteD, s8, galactic/smbh, granule, …) |
| B | External / owner (BBN ε ARITHMETIC VERIFIED internal; EXTERNAL WIN PENDING no DOI; arXiv HOLD; Zenodo ships) |
| C | Science debts D1–D9 |
| D | Theory walls (DE, bounce, Born, MEDR, …) |
| E | Page instrument (v13 T8=0.113 near-miss) |
| F | Shelf OPEN docs (21) |
| G | Explicit skips (PolyChord, peek-book, invent closes) |
| H | Paid this wave (so tables do not contradict) |

---

## Promotion honesty

| Still valid promotes | Still blocked |
|---|---|
| P-A4 candidate-local T14 | bbnfix posteriors |
| P-BBN ε ARITHMETIC VERIFIED (external PENDING) | A4 production sign |
| P-KOI packaging lock | Page Q6 / CANDIDATE |
| P-BOOK infrastructure READY | D2–D7 open arms; D9 dynamics |
| P-PAGE-D4 near-miss (not Q6) | arXiv post; PolyChord; Born/MEDR |

No new promotions this stamp. See `PROMOTION_BOARD_20260803_IMPROVE.md` §2026-08-04 FULL REFRESH.

---

## Anti-contradiction checklist (definition of done)

| Check | Result |
|---|---|
| BBN ε called **ARITHMETIC VERIFIED (internal)**; never claim EXTERNAL WIN as delivered without DOI | **YES** — SCIENCE_DEBTS, hard_wins, residual H, this package |
| bbnfix called **NOT YET** / not bookable | **YES** — all surfaces; gates REFUSED |
| T14 production **KILLED**; candidate **config-local** | **YES** — D1 + hard wins + promotions |
| No D2–D8 invent close | **YES** — open arms remain open/parked |
| PolyChord left alone | **YES** — skip class G |
| MCMCs not killed / not peeked for H₀ | **YES** — read-only |

---

## Explicit non-claims

1. Not “all debts closed.”  
2. Not bbnfix bookable.  
3. Not T14 production sign delivered.  
4. Not Page CANDIDATE / Q6.  
5. Not arXiv posted.  
6. Not claim-credibility ~5/10 (BBN ε arithmetic verified internally only; external win PENDING public record).

*NO FABRICATIONS.*
