# B-B C-code / validation legacy cleanup — path 3 stamp

**Date:** 2026-08-03  
**Seat:** Grok (blue)  
**Source:** ChatGPT REFEREE NOTE — C-code/core-model alignment; path 3 (keep both lanes; labels impossible to miss)

## Decision
Keep **CURRENT_CORE** and **LEGACY_ST** both live. Relabel only — no delete history, no invented null tests, no MCMC, no physics changes.

## Label map
| Label | Flags | Honest validation pointer |
|-------|--------|---------------------------|
| **CURRENT_CORE** | `use_dcdf` + screened/derived `varying_me` (+ `dcdf_dyad_link`) | `validate_dcdf.py` |
| **LEGACY_ST** | `use_prtoe` + ξ/ζ/β/… (v1–v3 ST) | `scripts/test_legacy_st_null_limit.py` (shim: `test_prtoe_null_limit.py`) — comparison / regression only |

## Touched surfaces (labels/docs)
- `scripts/test_prtoe_null_limit.py` — LEGACY_ST header + success/summary strings
- `scripts/run_prtoe_validation.py`, `run_prtoe_physics_validation.py`, `run_validation_suite_1_9.sh`, `prepare_publication_validation.sh`
- `scripts/test_bbn_activation.py`, `test_local_gravity.py`, `test_prtoe_unified_clustering.py` — LEGACY_ST docstrings
- `validate_dcdf.py` — CURRENT_CORE null banner
- `README.md`, `docs/historical_v1-v3_scalar_tensor/README.md` — two-lane tables
- `include/background.h` — dummy block comment (LEGACY_ST, not public core)

## Explicit non-claims
- LEGACY_ST null PASS ≠ “current PRTOE recovers ΛCDM”
- No new physics, no CLASS algorithm changes, no chain edits
