# bbnfix booking preflight — 2026-08-03

**Purpose:** everything short of booking, ready for the gate.  
**Gate (both required):** R−1 **&lt; 0.05** on both chains **AND** sampler self-stop
(`converged: true`). No soft “prefer.”  
**Do not book while over bar. Do not peek-quote H₀. Do not GetDist a moving chain.**

---

## Live snapshot (preflight stamp)

| chain | R−1 (progress field 4) | checkpoint | ranks |
|---|---:|---|---|
| `cmp_lcdm_mnu_bbnfix` | **0.059055** | `converged: false` | `.1 .2 .3` present |
| `dyad_mnu_bbnfix` | **0.189201** | `converged: false` | `.1 .2 .3` present |
| `cmp_prtoe_routeD` | ~102 (separate object; stop 0.1) | leave alone | n/a for letter H₀ |

```
python3 scripts/finalize_h0_at_convergence.py
# → NOT YET (both above bar) — correct refuse
```

---

## Artifact checklist (ready)

| Piece | Path | Ready? |
|---|---|---|
| Booking runbook | `docs/working_logs/_POSTERIOR_BOOKING_CHECKLIST.md` | yes |
| H₀ letter gate (stdout only) | `scripts/finalize_h0_at_convergence.py` | yes — hard refuse |
| GetDist instrument | `scripts/make_getdist_tables.py` | yes — bbnfix via `--include-bbnfix` **only after gate** |
| Chain yamls / covmats | `chains/*bbnfix*` | present |
| BBN ε external card | `hard_win3_bbn_eps_recompute_20260803/` | **PASS** (independent win) |

---

## Booking steps (when gate met — do not run early)

1. Confirm both `tail -1 chains/*.progress` field 4 **&lt; 0.05** **and**
   `converged: true` in both checkpoints (self-stop). Chains must be idle.  
2. `python3 scripts/finalize_h0_at_convergence.py` → should print letter sentence (still rank-1 only).  
3. Production tables:  
   `python3 scripts/make_getdist_tables.py --include-bbnfix`  
   Quote **three-rank** GetDist means ±68%, not rank-1 peek.  
4. Write `docs/working_logs/_runs/bbnfix_booking_<stamp>/REPORT.md` with R−1, file hashes, commands, table.  
5. Update `PRTOE_CHAIN_TABLES.md` / referee calendar **only after** step 4.  
6. Owner pastes letter H₀ when ready (Fairbank path is separate HOLD).

---

## Kill / process kills

- Book while either R−1 ≥ 0.05 → process kill  
- Book before both self-stop (`converged: true`) → process kill  
- Rank-1-only public H₀ when three ranks exist → incomplete  
- RouteD substitute for bbnfix letter pair → wrong object  
- Single-chain "GATE CROSSED" / almost-bookable on R−1 alone (no pair + self-stop) → false positive; ignore / retire watcher

---

## Explicit

arXiv / Fairbank endorsement is **owner HOLD** (wait response). This preflight does not touch that path.

*NO FABRICATIONS.*
