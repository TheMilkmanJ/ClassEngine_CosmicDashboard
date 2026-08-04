# Open-theory full package — formulable recomputes (2026-08-04)

**Policy:** Parse existing logs in this directory only. No invented physics.  
**Runner (when logs were produced):** `OMP_NUM_THREADS=1 nice -n 10 python3 …` from repo root.  
**Do not touch:** `chains/`, MCMCs, PolyChord.  
**Never close by recompute alone:** bounce H_re, Page curve, void floor, Koide mechanism residual, T14 production sign.

---

## Results (9/9 exit 0 — **not** all “PASS verdicts”)

**Claude red label rule (all-four-lanes, applied 2026-08-04):** exit 0 ≠ PASS.  
True **PASS verdicts** = explicit arithmetic cards (BBN ε, area-law, τ Parseval).  
Others = **desk audits** (algebra OK / debt restated / residual named).  
Supertrace log “ONE CORRECTION” = **ALREADY CURED** on shelf (log annotated).

| # | log | script / card (parent) | exit | verdict | residual still OPEN |
|---|---|---|:---:|---|---|
| 1 | `bbn_eps.log` | BBN ε arithmetic card (hard_win3) | 0 | **PASS** — ε 2σ ceiling **3.196%** ≈ paper **3.20%** | Kill if Aver/dY_p updates &gt;50%/20%; EMPRESS not upper limit |
| 2 | `area_law.log` | `scripts/quantum_area_law_quarter.py` | 0 | **PASS** — 12π/48π = **0.25** exact; numeric cancel PASS | Dynamical Page curve **OPEN** (not this script) |
| 3 | `supertrace.log` | `scripts/supertrace_k1_verify.py` | 0 | **desk audit** — str[k1]=0; log “ONE CORRECTION” **ALREADY CURED** on shelf | absolute SI *G* **OPEN** |
| 4 | `koide_lock.log` | `scripts/koide_lock_algebra_verification.py` | 0 | **desk audit** — algebra holds | Why equipartition / one quantum; #101/#102 **OPEN** |
| 5 | `tau_parseval.log` | `scripts/tau_parseval_recompute.py` | 0 | **PASS** — exact τ=½ln2 at Q=2/3; measured-Q Δτ~9e-6 | locking_without_Q **OPEN**; thermal delivery not used |
| 6 | `fbar_lo.log` | `scripts/fbar_leading_order_price.py` | 0 | **desk audit** — LO reading; registry wording cured 2026-08-04 | c_w underived |
| 7 | `fbar_cw_lo.log` | Track A3 LO / c_w residual (fbar_cw_lo) | 0 | **desk audit** — LO form; value of *a* residual | *a* not Derived |
| 8 | `baryo_junction.log` | `scripts/baryogenesis_junction_closure.py` | 0 | **desk audit** — quartet consistent; ω_J back-solved | Forward ω_J (**OPEN-BLOCKED** #39) |
| 9 | `rm_coherence.log` | `scripts/rm_coherence_kibble.py` | 0 | **desk audit** — geometric scale paid | Void floor **OPEN**; n_e external |

---

## One-line extracts (from logs)

### 1. BBN ε (`bbn_eps.log`)
```
ε 2σ ceiling = 3.196%
paper claim 2σ = 3.20%
match = PASS
EMPRESS pull at ε=0 = +2.91σ (cannot bound ε)
```

### 2. Area-law quarter (`area_law.log`)
```
12π/48π = 0.2500000000000000  PASS
Numerical cancel … S/(A/G) = 0.2500000000000000  PASS
Dynamical Page curve S_rad(v) | OPEN — not this script
```

### 3. Supertrace (`supertrace.log`)
```
RESULT — THE CLAIM IS CONFIRMED, WITH ONE UNIT CORRECTION
str[k1] = 0 holds exactly for SM + 3 right-handed neutrinos …
SM alone str[k1] = −1/2 (Visser); Weyl deficit −3 is the same fact in spinor count
```

### 4. Koide lock algebra (`koide_lock.log`)
```
(1) a = 3b ⟹ ρ² = 1/2 … ✓
(2) occupancy lock scale-free … ✓
(3) ω₁ = (2/9)·T_c = 39.356 keV … ✓
physics residual L2 / survival test unchanged OPEN
```

### 5. τ Parseval (`tau_parseval.log`)
```
PASS exact tau=1/2 ln2 at Q=2/3
locking_without_Q: OPEN
thermal_delivery_used: false
```

### 6. f_bar LO (`fbar_lo.log`)
```
subleading term can move f_bar by only about 1.0% per unit c2
residual deficit is therefore evidence FOR the leading-order reading
c2 itself still not derived
EXIT:0
```

### 7. f_bar c_w LO Track A3 (`fbar_cw_lo.log`)
```
GRADE: CANDIDATE CLOSED
LO dominance proved as bound from ε and data band
NAMED RESIDUAL: a (= −c_w), medium back-reaction strength
no unique a forced — residual is the VALUE of a
```

### 8. Baryogenesis junction (`baryo_junction.log`)
```
ω_J  5.672 keV  type=BACK-SOLVED
R = ω_J²/(2 Γ_φ θ̇) = 5e-05  vs needed 5e-05  ratio=1.0000
VERDICT: CONSISTENT to <2%
Real debt: forward ω_J from seat χ + pinning curvature (#39)
```

### 9. RM Kibble geometry (`rm_coherence.log`)
```
void shortfall B_blazar/B_seed = 20  (1.30 dex)
→ this script does NOT close that gap
At χ=χ_*: θ_ξ ≈ 1.07°, ℓ_π ≈ 169
Survey-plane class χ~1–3 Gpc: ℓ_π ~ 12–37
NON-CLAIMS: no void floor close; no absolute σ_RM without n_e
```

---

## Not run (out of package scope)

| track | why skipped |
|---|---|
| MCMC / booking / PolyChord | package rule |
| T14 full 3D production re-run | machine; production sign **not** bookable from smoke/partial |
| Hierarchy 6f batch | residual OPEN-BLOCKED; sized already in `debt_hierarchy_6f_20260803` |
| Page week3 / coevolve thrash | Q6 OPEN; freeze in `page_full_freeze_20260804` |
| Bounce H_re invent | **forbidden** — F-A3 holds |

---

## Summary

| metric | n |
|---|---:|
| **Logs parsed** | **9** exit 0 |
| **PASS verdicts** | **3** (BBN ε, area-law, τ Parseval) |
| **Desk audits** | **6** |
| **FAIL** | **0** |
| **Invented physics closes** | **0** |

Every **PASS verdict** reconfirms an explicit arithmetic card. Every **desk audit** reconfirms algebra / debt restatement without promoting residual to COMPLETE. Every hard residual named above stays OPEN / OPEN-BLOCKED / WATCH.
