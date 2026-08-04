# Page coevolve v3–v5 — DC3 quanta-borne path (2026-08-04)

**NO FABRICATIONS.** Write-once artifacts. No CANDIDATE packet. `page_curve_claimed: false`.

---

## Design change (v14+, carries into v3–v5 JSON)

**Page `v` uses unit-weight core occupation excess** (`PAGE_V_UNIT_WEIGHT_CORE=True`):

\[
E_{\mathrm{core}}^{\mathrm{page}} = \max(e_{c,\mathrm{raw}},0),\quad
v = \frac{E_{\mathrm{rad}}}{E_{\mathrm{rad}}+E_{\mathrm{core}}^{\mathrm{page}}}
\]

Free-frequency \(w_c(f)\) may still enter the free Hamiltonian; it does **not** inflate Page \(v\).  
This is the honest DC3 cure: late reach must be **quanta-borne**, not weight-borne.

---

## Gate comparison (scorecards on disk)

| version | T8 | stall_cap | DC3 | T2 u≥0.9 | binding | note |
|---|---|---|---|---|---|---|
| **v2** | **True** | **True** (5) | **FAIL** (0.85) | True | False | best stall/T8; weight-borne late v |
| **v3** | False | False (509) | **PASS** | True | False | first DC3 pass; u race + S freeze |
| **v4** | False | — | FAIL | False | False | dump too weak (u~0.60) |
| **v5** | False | False (555) | **PASS** | True | False | adaptive stall freeze; T8 still multivalued late |

Artifacts: `page_curve/coevolve_v{2,3,4,5}.json` + matching `*_scorecard_recompute.json`.

---

## Standing instrument grades

| Item | Status |
|---|---|
| DC3 definition / audit path | **paid** (unit-weight Page v + scorecard gate) |
| Joint T8 + stall_cap + DC3 + T2 | **OPEN** — no single write-once run clears all yet |
| CANDIDATE_TURN_binding | **false** all versions |
| page_curve_claimed | **false** |
| Q6 | **OPEN** |

---

## Next physics (not claim unlock)

Co-evolve so \(S(u)\) is single-valued **while** unit-weight \(u\) advances through mid-band and reaches ≥0.9 with purification drop — without late multivalued freeze bins.  
Do not subsample stall bins (red-killed edge-tune). Do not re-weight \(v\) by decaying \(w_c\).

*NO FABRICATIONS.*
