# DESI-DR2 FD Hessian Laplace — result — 2026-08-10

**Status:** PROCESS COMPLETE · both legs finite · **NOT nested · NOT bookable evidence**  
**Instance:** `i-096d08d2dc9d8f42c` (was idle Hessian box)  
**Artifact:** [`hessian_laplace_desi.json`](hessian_laplace_desi.json)  
**Started:** ~15:46Z · **JSON:** 15:57Z

## Numbers

| leg | ok_finite | logZ_H | samplecov logZ | cond(H) | regularized |
|---|---|---:|---:|---:|---|
| `dyad_mnu_bbnfix_desidr2` | true | (see JSON) | (see JSON) | huge | true |
| `cmp_lcdm_mnu_bbnfix_desidr2` | true | −1418.26 | −1436.53 | ~1.0×10⁹ | true |

| quantity | value |
|---|---:|
| **ΔlnZ_hessian (dyad−lcdm)** | **−24.76** |
| **ΔlnZ_samplecov (cross-check)** | **+1.46** |

(Sample-cov agrees with chain-only Laplace **+1.38** within soft-mode noise.)

## Reading (honesty)

- Finite both legs does **not** make FD Hessian gold evidence.  
- Hessian vs sample-cov **disagree by ~26 units** of lnZ — classic soft-mode / ill-conditioned FD signature (cond ~10⁹, eigenvalue floor).  
- Prefer **sample-cov ΔlnZ ≈ +1.4** as the soft-mode-honest volume-aware label on DESI (still inconclusive vs nested).  
- **Do not** quote ΔlnZ_H ≈ −25 as a physical Bayes factor.  
- Gold nested PolyChord remains the referee.

## Ops

JSON peeled to repo + optional S3 under `peel_desidr2_mcmc_20260810/`.  
Instance can be **stopped** to save cost (MCMC dual-gate already booked; Hessian done).

*NO FABRICATIONS.*
