# P2 dynamical continuum (adiabatic snapshots) — instrument

**Script:** `scripts/quantum_page_continuum_dynamical_p2.py`  
**Protocol:** BINDING `PAGE_TURN_ACCEPTANCE_PROTOCOL.md`  
**page_curve_claimed:** **false**  
**CANDIDATE_TURN:** **False**

## What advanced

- Acoustic profile scaled (ell↑ ⇒ κ↓) as evaporation proxy  
- At each snapshot: **re-solved** week2 exterior mode ODE → Γ(ω) (continuum, not frozen table)  
- Thermal cumulative + unitary hybrid with snapshot Γ  
- Full protocol scorecard T1–T7 / N1–N4  

## Snapshot table

| ell | κ | T_H | mean Γ | n_ok |
|---:|---:|---:|---:|---:|
| 4.000 | 0.12500 | 0.01989 | 0.752 | 5 |
| 5.000 | 0.10000 | 0.01592 | 0.693 | 5 |
| 6.000 | 0.08333 | 0.01326 | 0.642 | 5 |
| 7.200 | 0.06944 | 0.01105 | 0.588 | 5 |
| 8.800 | 0.05682 | 0.00904 | 0.529 | 5 |
| 11.200 | 0.04464 | 0.00711 | 0.458 | 5 |

## Protocol evaluation (unitary hybrid)

| test | result |
|---|---|
| T1 interior max | **False** |
| T2 v_late≥0.9 | **False** (v_late=0.091) |
| T2 frac drop ≥0.10 | **False** (drop=0.0000, S*=0.0198) |
| T2 drop >5 σ_jit | **False** (σ_jit=1.000e-08) |
| T2 all | **False** |
| T3 early rise | **True** |
| T4 nulls | **True** (N1=True, N2=True, N4=True) |
| T5 strict dynamical continuum | **False** |
| T5 partial (adiabatic re-solve) | **True** |
| T6 artifacts | **True** |
| T7 claim | **false** |
| **CANDIDATE TURN** | **False** |

## Grade

**INSTRUMENT PASS** (continuum re-solved along evaporation family).  
**Not CANDIDATE TURN** — fails T5 strict (no time-dependent continuum field \(\psi(x,t)\)).  
**page_curve_claimed: false**

## Gap

Full P2 for protocol T5: evolve continuum modes in time on evaporating geometry (or
controlled non-adiabatic Bogoliubov), not only adiabatic snapshot greybodies.

## Recompute

```bash
OMP_NUM_THREADS=1 nice -n 10 python3 scripts/quantum_page_continuum_dynamical_p2.py
```
