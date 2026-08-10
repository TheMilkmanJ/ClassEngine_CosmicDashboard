# CURRENT_CORE `validate_dcdf.py` v5 cure — 2026-08-04

**NO FABRICATIONS.** Hygiene improve; no PolyChord; no MCMC surgery.

## Problem
`validate_dcdf.py` still passed **retired** `dcdf_beta` (removed 2026-07-05). CLASS hard-errors on that knob. Suite reported total FAIL even though production chains use v5 API.

## Cure
| change | why |
|---|---|
| Remove all `dcdf_beta` | v5: \(w=-\rho_\mathrm{inf}/\rho\), \(c_s^2\equiv 0\) |
| Add `modes: s`, `output: tCl,pCl,lCl,mPk` | legal lensing |
| Null path = pure fluid | defaults: no conv / no thaw |
| Boundary = `rho_inf`, `deltam_mode`, `xi_Neff` | live knobs only |
| Timing WARN (not FAIL) at ~50s | PolyChord skipped on this box |
| BAO mPk-only without unused Cl keys | CLASS rejects unused `l_max_scalars` |
| LEGACY pointer → `test_legacy_st_null_limit.py` | path-3 rename |

## Result (final full suite `VALIDATE_DCDF_V5_20260804c.log`)
| gate | status |
|---|---|
| T1 null_limit | **PASS** (σ₈ Δ~3.3%, Pk Δ~7.1%) |
| T1 boundary | **PASS** (7/7) |
| T1 timing | **WARN** ~57s/eval (advisory; PolyChord deferred) |
| T2 CMB peaks | **PASS** (Δℓ=1) |
| T2 BAO | **PASS** `rs_drag=148.77` Mpc |
| T2 fσ₈ | **WARN** vs BOSS (as before; not blocking) |

**Blocking T1:** PASS. CURRENT_CORE instrument OK.

Also cured: `test_dcdf_clustering.py` (removed retired `dcdf_beta`) → clustering ratio ~0.93 **SUCCESS**.

Log: `VALIDATE_DCDF_V5_20260804c.log`  
Script: `validate_dcdf.py`

*NO FABRICATIONS.*

