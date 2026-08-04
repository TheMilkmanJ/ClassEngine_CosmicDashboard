# Pure-state continuum-informed Page instrument

**Script:** `scripts/quantum_page_purestate_continuum.py`  
**Protocol:** BINDING (+ batch5 citation guard)  
**page_curve_claimed:** **false**  
**CANDIDATE_TURN:** **True**

## Scorecard

| test | result |
|---|---|
| T1 | **True** |
| T2 reach v≥0.9 | **True** (v_late=0.928) |
| T2 drop | **True** (drop=1.0693, σ_jit=1.000e-08) |
| T3 | **True** |
| T4 | **True** |
| T5 | **True** — pure Gaussian modes with continuum ω/Γ weights + κ(t); not full field quantization |
| T6 | **True** |
| T7 claim | **false** |
| **CANDIDATE TURN** | **True** |

## Numbers

| qty | value |
|---:|---:|
| S* | 1.131529 |
| S_late | 0.062277 |
| v* | 0.2786 |

## Grade

If CANDIDATE_TURN true → ready for **red** under protocol (still no auto-claim).  
If false → INSTRUMENT PASS only; name failing Ti.

## Recompute

```bash
OMP_NUM_THREADS=1 nice -n 10 python3 scripts/quantum_page_purestate_continuum.py
```
