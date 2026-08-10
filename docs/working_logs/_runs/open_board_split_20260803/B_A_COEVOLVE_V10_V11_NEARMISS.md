# Page coevolve near-miss — v10/v11 (2026-08-04)

**NO FABRICATIONS.** Write-once. No CANDIDATE packet. `page_curve_claimed: false`.

ChatGPT REFEREE RECORD improve-wave: residual inventory non-empty; instrument-only promotions OK.

---

## Best joint attempt: `coevolve_v11.json` (schedule v21)

| gate | result |
|---|---|
| T1–T4, T5, T6 | **True** |
| T2 u≥0.9 + drop | **True** (u_late=0.9037) |
| DC3 weight-invariant | **PASS** (unit-weight Page v) |
| **T8** | **False** — sole fail: early bin [0.10,0.11) range/S*=**0.122** (need ≤0.10) |
| stall_cap (≤10) | **False** — longest=**11** (need ≤10) |
| CANDIDATE_TURN_binding | **False** |
| page_curve_claimed | **false** |

Artifact: `page_curve/coevolve_v11.json`  
Scorecard: `page_curve/coevolve_v11_scorecard_recompute.json`

### What fixed vs earlier
- Unit-weight core Page \(v\) → DC3 can pass  
- Hard freeze at first \(u\ge 0.9\) → late multivalued S largely killed  
- No 500-frame freeze pad → stall_cap 11 not 562  

### What still fails (honest)
- Early T8 bin barely over threshold (0.122 vs 0.10)  
- One extra stall frame (11 vs 10) mid-history  

v12 polish (stronger early BS) **regressed** T2 (u_late=0.88). v11 remains the near-miss champion.

---

## Reference table (selected)

| ver | T8 | stall | DC3 | T2 | note |
|---|---|---|---|---|---|
| v2 | pass | pass | fail | pass | best T8+stall; weight-borne |
| v5 | fail | fail | pass | pass | DC3 paid; late multivalued |
| **v11** | **near** | **near** | **pass** | **pass** | joint near-miss |
| v12 | fail | — | fail | fail | polish regressed |

---

## Explicit
Not a Page claim. Not CANDIDATE. Q6 OPEN. Next: tiny dynamics change to clear early T8 bin + one stall frame — or accept instrument near-miss until deeper construction.

*NO FABRICATIONS.*
