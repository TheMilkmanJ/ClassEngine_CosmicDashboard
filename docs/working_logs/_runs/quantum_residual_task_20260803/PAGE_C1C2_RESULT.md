# Page continuum-coupled MVP (R-PAGE C1–C2)

**Script:** `scripts/quantum_page_continuum_coupled_mvp.py`  
**JSON:** `page_curve/continuum_coupled_mvp.json`  
**page_curve_claimed:** **false**  
**week2 source:** stationary Bogoliubov + greybody (PASS=True)

## Setup

| item | value |
|---|---:|
| N_c | 4 |
| N_r (week2 mid-band) | 9 |
| T_H / κ | 0.019894 / 0.1250 |
| G0 / τ_evap | 0.1 / 3.5 |
| steps × dt | 250 × 0.025 |

## Coupled (evaporating g(t))

| quantity | value |
|---|---:|
| S_rad peak | 0.792070 |
| S_rad late | 0.232499 |
| late_drop | 0.559571 |
| v at peak | 0.0849 |
| max\|S_total\| | 1.201e-04 |
| unitarity | PASS |
| page-like shape (curiosity) | YES |

## Null g=0

| quantity | value |
|---|---:|
| S_rad peak | 3.540e-14 |
| spurious growth | PASS (none) |

## Grade

| check | status |
|---|---|
| Instrument ran | **PASS** |
| Unitarity coupled | **PASS** |
| Null g=0 clean | **PASS** |
| Page / Q6 claim | **OPEN — not claimed** |

## Next (still here)

1. Time-dependent continuum mode amplitudes (not only Γ-weighted toy coupling)  
2. Red review before any claim  
3. Larger N_r only when load allows  

## Recompute

```bash
OMP_NUM_THREADS=1 nice -n 10 python3 scripts/quantum_page_continuum_coupled_mvp.py
```
