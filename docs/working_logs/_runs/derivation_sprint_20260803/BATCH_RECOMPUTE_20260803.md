# BATCH RECOMPUTE — 2026-08-03

**Stamp:** 2026-08-03 ~17:13 local (MDT)  
**Policy:** Honest recomputes only. No fabrications. No MCMC. No inventing physics.  
**Runner:** `nice -n 10 timeout 120s python3 <script>` from repo root.  
**Timeout policy:** hang >120s → kill, mark TIMEOUT.  
**Result:** **10/10 exit 0. Zero TIMEOUTs.**

Logs: `docs/working_logs/_runs/derivation_sprint_20260803/<script_basename>.log`

---

## Results table

| script | exit | one-line result | overclaim risk |
|---|:---:|---|:---:|
| `scripts/concordance.py` | 0 | All five families TIGHT (k 0.6σ, f_bar 1.4σ, eps 1.4σ, n_s 1.2σ, ω₀ 0.7σ); eps largest strain | none |
| `scripts/hierarchy_6f_double_count.py` | 0 | Horn (a) double-count NARROWED not closed; residual running adverse ×5–10; checks 5/5 | none |
| `scripts/hierarchy_alpha_scale_fork.py` | 0 | Best-case α(0) still overshoots 4π m_H by ×2.003; exact landing needs 1/α=140.74 outside QED range | none |
| `scripts/hierarchy_anchor_budget.py` | 0 | Band ×3.2 (0.55–1.78 TeV) dominated by O(λ) scheme; measured k only ±16% | none |
| `scripts/fbar_leading_order_price.py` | 0 | Subleading ~1%/c₂; deficits imply \|c₂\|~O(1); residual evidence *for* LO 2/π; c₂ underived | low |
| `scripts/fbar_window_discriminator.py` | 0 | Accumulated window preferred ~54:1 on fit-implied only; modest evidence, operator form still owed | low |
| `scripts/tau_parseval_recompute.py` | 0 | PASS exact τ=½ln2 at Q=2/3; measured-Q Δτ~9e-6; locking_without_Q=OPEN | none |
| `scripts/additivity_counterfactual.py` | 0 | Instrument only: w=1 → ⟨E⟩/T=1.5, M_eff/M=4.48; axiom_derived=false | none |
| `scripts/quantum_page_week3_nulls.py` | 0 | Null suite PASS A/B/C; page_curve_claimed=false; baseline late_drop instrument curiosity only | none |
| `scripts/quantum_page_week3_week2_coupled.py` | 0 | Week2-seeded g=0.08 late_drop=True vs g=0 null False; page_curve_claimed=false | none |

---

## Key stdout extracts (honest, no spin)

### 1. concordance (exit 0)
```
family                               joint     +/- strain(sig)  verdict
k (the settlement coupling)         1.3630  0.0032         0.6  TIGHT
f_bar (the winding average)         0.6366  0.0000         1.4  TIGHT
eps (the dyad, %)                   1.2403  0.0079         1.4  TIGHT
n_s (the tilt)                      0.9651  0.0008         1.2  TIGHT
omega_0 (km/s/Mpc)                  0.7425  0.0681         0.7  TIGHT
```
Note: 2/π exact dominates f_bar joint; without it joint ≈0.626±0.008 → 1.3σ test.

### 2. hierarchy_6f_double_count (exit 0)
- Screening already in 6c: ln(1+1/b)=4.287 vs QED run to M_Z 0.0686 → **~62×** larger.
- Verdict: **NARROWED, NOT CLOSED.** Residual adverse if SM-charged carriers; corpus 6e says compensated (charged pockets). Anchor not helped. **CHECKS: 5/5.**

### 3. hierarchy_alpha_scale_fork (exit 0)
| alpha used | 1/α | M_anchor | overshoot vs 4π m_H |
|---|---:|---:|---:|
| α(0) | 137.036 | 3153 GeV | ×2.003 |
| α(M_Z) | 127.951 | 1.76e4 GeV | ×11.17 |
| Planck floor | 104.938 | 1.50e6 GeV | ×955.5 |

Exact land needs 1/α=140.74 — **outside QED IR bound** (max 1/α=137.036). dlnM/dlna_c=25.773.

### 4. hierarchy_anchor_budget (exit 0)
- Amplification 1/(k α_c)=33.47  
- Bare 1.576 TeV → fully corrected 0.541 TeV  
- **O(λ) scheme DOMINANT** (×3.2 band); k minor (±16%); α_c=3α live bet.

### 5. fbar_leading_order_price (exit 0)
- (ε/2)/(2/π) ≈ **0.985% per unit c₂**  
- fit-implied → c₂=−1.80; winding n≥4 → c₂=−0.84±0.52; tension **1.9σ**  
- c₂ itself still not derived (family-coupling Lagrangian unbuilt).

### 6. fbar_window_discriminator (exit 0)
- Accumulated: N≈3.82e5 turns → 2/π to ~8e-5%.  
- Instantaneous: sd(|cos|)=0.3078.  
- Fit-implied offset 1.78% → P(frozen)=1.87% → **odds ~54:1** accumulated (modest; look-elsewhere applies).  
- Winding-sim circular for window test — not used in LR.

### 7. tau_parseval_recompute (exit 0)
```
PASS exact tau=1/2 ln2 at Q=2/3
exact: tau=0.3465735902799726  (== half_ln2 to ~1e-16)
measured Q=0.6666605: tau-half_ln2 = 9.25e-6; T_c≈177.10 keV
locking_without_Q: OPEN
thermal_delivery_used: false
```

### 8. additivity_counterfactual (exit 0)
- **axiom_derived: false**  
- w=1.0 → exp=1.5, M_eff/M=4.481689  
- Non-claims: not axiom derivation; not A_s/n_s kill; hierarchy residual 1.5014 vs 3/2 separate.

### 9. quantum_page_week3_nulls (exit 0)
| null | grade |
|---|---|
| A g=0 | PASS (max\|ΔS\|=0) |
| B infinite bath | PASS (late_drop=False) |
| C vacuum | PASS (S0~3e-11) |
| suite | PASS |

**page_curve_claimed=false.** Baseline late_drop remains instrument curiosity only.

### 10. quantum_page_week3_week2_coupled (exit 0)
| run | peak S_rad | late S_rad | late_drop |
|---|---:|---:|---|
| week2-seeded g=0.08 | 3.94754 | 3.91171 | True |
| null g=0 | 3.94754 | 3.94754 | False |

**page_curve_claimed=false.** Not Q6, not continuum Page, not PRTOE result.

---

## Executive summary

1. **All ten scripts completed under 120s with exit 0.** No kills, no hangs, no missing scripts.
2. **Concordance:** network still TIGHT on all five families; largest strain is eps/f_bar at ~1.4σ (not a break).
3. **Hierarchy trio:** double-count argument narrows horn (a) but does **not** close anchor; best QED case remains **×2 overshoot**; error band still **O(λ)-dominated**. No fabrication path to landing.
4. **f_bar:** LO pricing and window discriminator reaffirm 2/π as leading term under accumulated window; evidence grade is **modest** (c₂ O(1) but underived; LR ~54:1 with LEE caveat). Overclaim risk marked **low** only on interpretive wording, not on arithmetic.
5. **τ / Parseval:** exact identity holds; measured-Q residual negligible; **locking_without_Q still OPEN**.
6. **Additivity:** counterfactual instrument only; does not derive the axiom.
7. **Page instruments:** week3 null suite **PASS**; week2-coupled shows instrument late_drop with g≠0 vs g=0 control. Both hard-lock **page_curve_claimed=false**.

**Bottom line:** Batch is clean and reproducible. Nothing in this run invents physics, closes Q6/Page, lands the hierarchy anchor, or derives log-additivity / c₂ / locking-without-Q. Open items stay open; closed arithmetic (Parseval exact, null suite, concordance table) reconfirms.

---

## Artifacts written by scripts during this batch

| path |
|---|
| `docs/working_logs/_runs/derivation_sprint_20260803/R4b_ADDITIVITY_COUNTERFACTUAL.md` |
| `docs/working_logs/_runs/derivation_sprint_20260803/P1_PAGE_NULLS.md` |
| `docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/week3_nulls.json` |
| `docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/week3_week2_coupled.json` |
| (updated) `docs/working_logs/_runs/quantum_null_hardening_20260803/PAGE_CURVE_WEEK3.md` |
| per-script logs: `*.log` in this directory |

## Recompute command (batch)

```bash
cd /home/themilkmanj/prtoe_class
for s in concordance hierarchy_6f_double_count hierarchy_alpha_scale_fork \
         hierarchy_anchor_budget fbar_leading_order_price fbar_window_discriminator \
         tau_parseval_recompute additivity_counterfactual \
         quantum_page_week3_nulls quantum_page_week3_week2_coupled; do
  nice -n 10 timeout 120s python3 scripts/${s}.py
  echo "EXIT $s: $?"
done
```
