# PAGE co-evolution instrument result (champion freeze — currency 2026-08-04)

**Milestone:** `R_PAGE_coevolve_T8_era`  
**Champion artifact:** `docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/coevolve_v13.json`  
**Schedule version:** `v23_champion_locked`  
**page_curve_claimed:** **false**  
**Standing CANDIDATE:** **none** (`CANDIDATE_TURN_binding` **False**; claim-decoupling not filed)  
**Deeper construction:** D1–D3 exhausted; **D4 active**  
**Thrash:** **none** — no coevolve knob thrash under freeze

Authority freeze: `docs/working_logs/_runs/page_full_freeze_20260804/`  
Status sync: `docs/working_logs/_runs/quantum_status_sync_20260804/`

---

## Design

Co-evolve S_rad with advancing evaporation coordinate u = max envelope of pure
energy fraction v. Beam-splitter dump overlapped with TMS so u climbs through
the entropy-rise window (batch9 denial mode = S multivalued at stalled u).

Header schedule frozen at **v23_champion_locked** (v13 joint near-miss).  
D1–D3 deeper construction exhausted without joint clear; **D4** accept near-miss until new microphysics. **No knob thrash.**

---

## Binding scorecard (arrays-only recompute — not a CANDIDATE filing)

```bash
OMP_NUM_THREADS=1 nice -n 10 python3 scripts/page_protocol_scorecard.py \
  docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/coevolve_v13.json
```

| gate | result |
|---|---|
| T1–T6 machine | **True** |
| T2 u≥0.9 | **True** (u_late = 0.9021) |
| stall_cap ≤10 | **True** (longest = 10) |
| DC3 weight-invariant | **PASS** |
| **T8** | **False** — sole fail [0.10, 0.11) range/S* = **0.113** (need ≤0.10) |
| `CANDIDATE_TURN_binding` | **False** |
| page_curve_claimed | **false** |

Scorecard on disk: `page_curve/coevolve_v13_scorecard_recompute.json`  
Snapshot: `../page_full_freeze_20260804/SCORECARD_SNAPSHOT.md`

| quantity | value |
|---:|
| u* at S peak | 0.266967 |
| u_late | 0.902078 |
| S_peak | 0.016688 |
| S_late | 0.006142 |
| drop | 0.010546 |
| frac S-rise while u advances | ≈0.99995 |
| longest stall frames | 10 |
| T8 worst bin | [0.10, 0.11) range/S* = **0.113** |

---

## Freeze stance (D4)

| item | status |
|---|---|
| Champion | **v13** only |
| LATEST pointer | → v13 |
| D1 / D2 / D3 | tried / exhausted — not joint |
| **D4** | **active** — instrument near-miss accepted until licensed new microphysics |
| Next Page work | microphysics only (new coupling / dump / free-H law) |
| Forbidden | thrash coevolve; densify mode thrash; G_BS retune for T8; CANDIDATE on v13 |

---

## Explicit non-claims

- Not a Page curve claim; **Q6 remains OPEN**  
- Not a CANDIDATE packet  
- Machine T1–T6 True ≠ standing candidate  
- T8 early residual **0.113** blocks binding  
- Write-once versioned artifacts — do not overwrite scored JSON  
- Later write-once densify attempts (e.g. v35–v38) are **not** champion; `coevolve_LATEST.txt` points at **v13**  
- D4 is freeze stance, not physics close  

*NO FABRICATIONS.*
