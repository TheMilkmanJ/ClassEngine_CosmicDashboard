# Historical: v1–v3 Scalar-Tensor Era (archived 2026-07-07)

These three documents describe PRTOE's **first formalization** — a
scalar-tensor cosmology (F(φ)R non-minimal coupling to curvature) with
phenomenological activation functions. This era **died completely**
(see `docs/PRTOE_intellectual_history.md`, "v1–v3: The non-minimal
coupling era"): four independent rescue mechanisms were tried and each
failed by direct calculation. The project pivoted entirely to the v4
dCDF unified dark fluid, and later to the dyad (dCDF + varying m_e).

Kept per this project's own rule: **every death is recorded, never
buried.** These were relocated here (from the repo root, where they
were confusingly labeled as if current — "Working Formulation,"
"Physics for Review") purely to stop them from being mistaken for
active documentation. Nothing was deleted; `git log` on each file
retains full history.

- `PRTOE_Working_Formulation.md` — the scalar-tensor ansatz itself
- `PRTOE_PHYSICS_FOR_REVIEW.md` — compact physics reference for that era
- `CONTEXT.md` — code-audit contracts tied to the above two

Current, active documentation lives in `docs/` at the top level;
`docs/PRTOE_v5_dCDF_complete.md` is the present source-of-truth.

## Validation lane (do not mix with CURRENT_CORE)

| Label | Flags | Scripts |
|-------|--------|---------|
| **LEGACY_ST** (this era) | `use_prtoe` + ξ/ζ/β/… | `scripts/test_prtoe_null_limit.py`, `scripts/test_local_gravity.py`, `scripts/test_bbn_activation.py`, `scripts/run_validation_suite_1_9.sh` |
| **CURRENT_CORE** (live) | `use_dcdf` + screened `varying_me` | `validate_dcdf.py`, production YAMLs with `use_dcdf: yes` |

A “null limit” pass on `use_prtoe` is **comparison regression only**, not a claim
that the public expansion core recovers ΛCDM.
