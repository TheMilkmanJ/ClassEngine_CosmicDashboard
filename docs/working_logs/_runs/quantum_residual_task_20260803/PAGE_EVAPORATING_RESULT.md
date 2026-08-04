# Continuum evaporating S_rad instrument (R-PAGE)

**Script:** `scripts/quantum_page_continuum_evaporating.py`  
**JSON:** `page_curve/continuum_evaporating.json`  
**page_curve_claimed:** **false**

## A) Thermal-only (Γ · n_B, T_H(t)↓)

| quantity | value |
|---|---:|
| S_peak | 0.815569 |
| S_late | 0.815569 |
| late_drop | 0.000000 |
| monotonic S_cum | True |
| page-like turn | NO (expected) |
| grade | PASS bookkeeping |

Thermal-only is the **information-loss** curve class — not a Page solution.

## B) Unitary hybrid (week2 ω,Γ + Gaussian core)

| quantity | value |
|---|---:|
| S_peak | 0.211620 |
| S_late | 0.073815 |
| late_drop | 0.137805 |
| v at peak | 0.0849 |
| max\|S_total\| | 1.393e-04 |
| unitarity | PASS |
| page-like curiosity | YES |

## Grade

| check | status |
|---|---|
| Thermal bookkeeping | **PASS** |
| Unitary unitarity | **PASS** |
| Q6 / Page claim | **OPEN — false** |

## Still missing for a claim

1. Time-dependent continuum mode ODE (not only Γ·n_B + toy Gaussian)  
2. Self-consistent horizon evaporation  
3. Red AGREE  

## Recompute

```bash
OMP_NUM_THREADS=1 nice -n 10 python3 scripts/quantum_page_continuum_evaporating.py
```
