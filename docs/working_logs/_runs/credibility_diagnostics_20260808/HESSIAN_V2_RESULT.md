# Hessian Laplace v2 — result (old-BAO) — 2026-08-10

**Status:** PROCESS COMPLETE — finite both legs — **NOT nested · soft-mode diagnostic only**  
**Instance:** `i-090c0275d8198ae14` (stopped after success)  
**Artifact:** [`hessian_laplace_v2.json`](hessian_laplace_v2.json)

## Numbers (do not quote as gold evidence)

| leg | logZ_H | samplecov logZ | ok_finite | regularized | cond(H) |
|---|---:|---:|---|---|---:|
| `dyad_mnu_bbnfix` | −1438.30 | −1434.48 | true | true | ~1e10 |
| `cmp_lcdm_mnu_bbnfix` | −1437.13 | −1434.70 | true | true | ~1e10 |

| quantity | value |
|---|---:|
| ΔlnZ_hessian (dyad−lcdm) | **−1.176** |
| ΔlnZ_samplecov (cross-check) | **+0.216** |

## Reading

- v1 failed on ΛCDM (`logZ=-inf`); v2 hardens FD steps / boundary / eigenvalue floor.
- v2 is **finite** but **highly ill-conditioned** (soft modes) — Hessian and sample-cov ΔlnZ **disagree in sign**.
- Prefer sample-cov **+0.21** as the soft-mode-honest volume-aware label; gold path remains **nested PolyChord**.

*NO FABRICATIONS.*
