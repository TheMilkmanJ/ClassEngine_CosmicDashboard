# Time-dependent continuum field instrument (R-PAGE T5)

**Script:** `scripts/quantum_page_continuum_field_td.py`  
**Protocol:** BINDING  
**page_curve_claimed:** **false**  
**CANDIDATE_TURN:** **False**

## Setup

| item | value |
|---|---:|
| NX × NT | 180 × 2800 |
| DT | 0.012 |
| ell(t) | 4.0 → 10.0 |
| operator | 1D acoustic-like (see script header) |

## Protocol scorecard

| test | result |
|---|---|
| T1 interior max | **False** |
| T2 v≥0.9 | **True** (v_late=0.980) |
| T2 frac+noise drop | **False** (drop=0.0000, σ_jit=1.000e-08) |
| T3 early rise | **True** |
| T4 nulls | **True** |
| T5 strict dynamical continuum | **True** |
| T5 caveat | 1D instrument wave operator + cumulative dE/T S_rad; not covariant acoustic KG; not pure-state Page purification |
| T6 artifacts | **True** |
| T7 claim | **false** |
| **CANDIDATE TURN** | **False** |

## Numbers

| quantity | value |
|---|---:|
| S_rad peak | 685.032847 |
| S_rad late | 685.032847 |
| v* | 0.9803 |

## Grade

**INSTRUMENT PASS** if run completes and scorecard is filled.  
**CANDIDATE TURN** only if T1–T6 true under BINDING protocol (red still required for claim).  
This run's claim flag remains **false**.

## Recompute

```bash
OMP_NUM_THREADS=1 nice -n 10 python3 scripts/quantum_page_continuum_field_td.py
```
