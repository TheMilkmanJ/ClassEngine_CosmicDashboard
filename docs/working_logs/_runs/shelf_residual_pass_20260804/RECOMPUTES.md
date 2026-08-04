# Shelf residual pass — formulable recomputes (2026-08-04)

**Policy:** Existing scripts / registered cards only. No invented physics.  
**Runner:** `OMP_NUM_THREADS=1 nice -n 10 python3 …` from repo root.  
**Logs:** this directory `*.log`  
**Do not touch:** chains/, MCMCs, PolyChord.

---

## Results (8/8 exit 0 — **not** all “PASS verdicts”)

**Claude red label rule (all-four-lanes, applied 2026-08-04):** exit 0 ≠ PASS.  
True **PASS verdicts** = explicit arithmetic cards (BBN ε, area-law, τ Parseval).  
Others = **desk audits** (algebra OK / debt restated / residual named).  
Supertrace log “ONE CORRECTION” = **ALREADY CURED** on shelf (log annotated).

| # | card / script | exit | class | verdict | residual still OPEN |
|---|---|:---:|---|---|---|
| 1 | **BBN ε** (hard_win3 arithmetic card) | 0 | **PASS verdict** | ε 2σ ceiling **3.1957%** ≈ paper 3.20% | Kill if Aver/dY_p updates &gt;50%/20%; EMPRESS not upper limit |
| 2 | `scripts/quantum_area_law_quarter.py` | 0 | **PASS verdict** | 12π/48π = 0.25 exact; numeric cancel PASS | Page curve dynamics **OPEN** (not this script) |
| 3 | `scripts/supertrace_k1_verify.py` | 0 | **desk audit** | str[k1]=0 SM+3ν_R; Visser sign confirmed; “ONE CORRECTION” **ALREADY CURED** | unit note only (shelf paired) |
| 4 | `scripts/koide_lock_algebra_verification.py` | 0 | **desk audit** | a=3b, occupancy lock, ω₁=(2/9)T_c algebra holds | Why equipartition / one quantum; Wilson; mechanism exactness **OPEN** |
| 5 | `scripts/tau_parseval_recompute.py` | 0 | **PASS verdict** | exact τ=½ln2 at Q=2/3; measured-Q Δτ~9e-6 | locking_without_Q **OPEN**; thermal delivery not used |
| 6 | `scripts/fbar_leading_order_price.py` | 0 | **desk audit** | subleading ~1%/c₂; residual evidence *for* LO 2/π | c₂ underived (family-coupling Lagrangian unbuilt) |
| 7 | `scripts/baryogenesis_junction_closure.py` | 0 | **desk audit** | quartet CONSISTENT; ω_J=5.672 keV **BACK-SOLVED** | Forward ω_J from seat χ + pinning (**OPEN-BLOCKED** #39) |
| 8 | `scripts/rm_coherence_kibble.py` | 0 | **desk audit** | geometric scale ℓ~25–60 survey plane; θ_ξ(χ_*)=1.07° | Void floor **OPEN**; absolute σ_RM needs external n_e |

---

## One-line extracts

### 1. BBN ε
```
eps_2sig_ceiling_pct=3.195706
match_PASS=True
VERDICT: PASS
```
Recipe: `(Aver + 2*sig - Yp0)/dY` with Yp0=0.246891, dY=0.00163, Aver=0.2453±0.0034.  
Prior: `docs/working_logs/_runs/hard_win3_bbn_eps_recompute_20260803/REPORT.md`.

### 2. Area-law quarter
```
12π/48π = 0.2500000000000000  PASS
Numerical cancel … S/(A/G) = 0.2500000000000000  PASS
```
Does **not** close Page curve.

### 3. Supertrace
```
RESULT — THE CLAIM IS CONFIRMED, WITH ONE UNIT CORRECTION
str[k1] = 0 holds exactly for SM + 3 right-handed neutrinos …
```

### 4. Koide lock algebra
```
(1) a = 3b ⟹ ρ² = 1/2 … ✓
(2) occupancy lock scale-free … ✓
(3) ω₁ = (2/9)·T_c = 39.356 keV … ✓
```
Physics residual L2 / survival test unchanged OPEN.

### 5. τ Parseval
```
PASS exact tau=1/2 ln2 at Q=2/3
locking_without_Q: OPEN
thermal_delivery_used: false
```

### 6. f_bar LO
```
subleading term can move f_bar by only about 1.0% per unit c2
residual deficit is therefore evidence FOR the leading-order reading
c2 itself still not derived
```

### 7. Baryogenesis junction
```
ω_J  5.672 keV  type=BACK-SOLVED
R = ω_J²/(2 Γ_φ θ̇) = 5e-05  vs needed 5e-05  ratio=1.0000
VERDICT: CONSISTENT to <2%
Real debt: forward ω_J from seat χ + pinning curvature (#39)
```
Stale Γ_φ/θ̇~10⁷ shorthand manufactures fake ×9 miss — retired.

### 8. RM formula
```
At χ=χ_*: θ_ξ ≈ 1.07°, ℓ_π ≈ 169
Survey-plane class χ~1–3 Gpc: ℓ_π ~ 12–37 (quote survey ℓ~25–60, not last-scatter 169 as RM prediction)
NON-CLAIMS: no void floor close; no absolute σ_RM without n_e
```

---

## Not run (out of budget / wrong lane)

| script / track | why skipped |
|---|---|
| MCMC / booking scripts | Lane rule: do not touch chains |
| PolyChord | banned |
| T14 full 3D production re-run | machine; already candidate-booked elsewhere |
| Hierarchy 6f batch | optional; residual OPEN-BLOCKED not closed by recompute |
| Page week3 suite | OPEN-BLOCKED dynamics; re-PASS known, not shelf residual close |

---

## Summary

- **Recomputes run:** 8 exit 0  
- **PASS verdicts:** 3 (BBN ε, area-law, τ Parseval)  
- **Desk audits:** 5  
- **FAIL:** 0  
- **No physics closes invented.** Every **PASS verdict** reconfirms an explicit arithmetic card; every **desk audit** restates algebra/debt without promoting residual to COMPLETE; every residual named above stays OPEN/OPEN-BLOCKED/WATCH.
