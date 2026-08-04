# Page construction D2 attempt — free \(w_c\equiv 1\) (2026-08-04)

**NO FABRICATIONS.** Write-once. No CANDIDATE. claimed false.

---

## What D2 is

Free Hamiltonian core frequency fixed at \(w_c=1\) (same as unit-weight Page \(v\)), so free dynamics cannot create a weight-borne late \(v\) channel distinct from Page scoring.

## Result

Run with `FREE_W_C_FIXED=True` + v23 couplings (`coevolve_v34` class):

| gate | result |
|---|---|
| T8 early ratio | **0.113** (same as v13) |
| stall / DC3 / T2 / T1–T6 | same as v13 (pass) |
| binding | **false** |

**Why no change:** champion freeze hits \(u\ge0.9\) at \(f\sim0.25\), while former free-frequency decay only starts at `W_C_HOLD=0.48`. On the scored trajectory, free \(w_c\) was already 1 throughout the active history. D2 is a **no-op** relative to v13 for this construction.

## Standing

- Champion remains **`coevolve_v13`** (T8 early 0.113 only).  
- D1: early T8 improved, T2 not joint.  
- D2: no joint improvement (trajectory never entered free-\(w_c\) decay).  
- Next: D3 (mode band) or accept near-miss / machine wait.

*NO FABRICATIONS.*
