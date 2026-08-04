# SCORECARD_SNAPSHOT — champion coevolve_v13 (2026-08-04 freeze)

**NO FABRICATIONS.** Arrays-only recompute. Not a CANDIDATE filing.

## Command

```bash
OMP_NUM_THREADS=1 nice -n 10 python3 scripts/page_protocol_scorecard.py \
  docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/coevolve_v13.json
```

## Paths / provenance

| item | value |
|---|---|
| Artifact | `docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/coevolve_v13.json` |
| Artifact sha256 | `048de43e1bc766c8f420c54f565a33166c0792c23291ba567cdc6c772f92fca8` |
| Scorecard write | `.../page_curve/coevolve_v13_scorecard_recompute.json` (re-scored this freeze) |
| Tool | `scripts/page_protocol_scorecard.py` |
| tool_sha256 | `1d02a1d4bdd11a88612f6db387a3a819425c3be362bc74a57122162cb90a14b7` |
| Producing script (from artifact provenance) | `scripts/quantum_page_coevolve.py` sha256 `6328d44fcd9444db57644d90ec78c283aa4d19d460e7bf108973d40a803f2bf0` |
| Milestone | `R_PAGE_coevolve_T8_era` |
| Resource | OMP=1; no PolyChord; no MCMC; arrays-only recompute |

## Binding gates (T1–T8 + DC3)

| gate | result | detail |
|---|---|---|
| T1 interior max | **True** | u* = 0.266967 |
| T2 reach u≥0.9 | **True** | u_late = 0.902078 |
| T2 frac/noise | **True** | T2_all = True |
| T3 early rise | **True** | S_rise_credited = 0.0166874 (du>1e-9) |
| T4 nulls | **True** | N1–N4 True |
| T5 continuum | **True** | structural inherit from producing run |
| T6 artifacts | **True** | |
| T7 claim flag | **False** | correct: never claim-flip in scorecard |
| T1–T6 machine (`CANDIDATE_TURN_T1_T6_only`) | **True** | |
| stall_cap ≤10 | **True** | longest_stall_frames = **10** |
| co_frac ≥0.70 | **True** | frac_S_rise_while_u_advances ≈ 0.99995 |
| swap_back ≤0.05 | **True** | max u−v ≈ 1.50e-5 |
| peak_in_motion | **True** | |
| **DC3** weight-invariant reach | **PASS** | v_frozen env late = 0.902078; method `e_c_raw_stored` |
| **T8** single-valued S(u) | **False** | sole fail |
| T8 worst bin | **[0.10, 0.11)** | n=12; S_range/S* = **0.113154** (need ≤0.10) |
| T8 threshold | 0.1 × S* | S* = 0.0166882; threshold = 0.00166882 |
| T8 occupied bins | 83 | failing bins = 1 |
| `CANDIDATE_TURN_binding` | **False** | requires T8_pass (+ DC3 when computable) |
| **`page_curve_claimed`** | **false** | tool never sets true |

## Curve numbers (for reference only)

| quantity | value |
|---:|
| S_peak (S*) | 0.016688199517780646 |
| S_late | 0.00614180917446334 |
| drop | 0.010546390343317304 |
| i_peak | 104 |
| n_frames | 188 |
| max_abs_S_total | 6.96e-14 |

## Explicit non-claims

- Not a Page physics claim; **Q6 OPEN**
- Not a CANDIDATE packet
- Machine T1–T6 True ≠ standing candidate
- T8 early residual **0.113** blocks binding

*NO FABRICATIONS.*
