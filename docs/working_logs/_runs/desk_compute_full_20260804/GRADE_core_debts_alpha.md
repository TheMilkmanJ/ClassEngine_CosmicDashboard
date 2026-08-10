# GRADE — current_core + hierarchy + baryo_rm + alpha_amp + tests_analytic

**Stamp:** 2026-08-04 (`desk_compute_full_20260804`)  
**Source packs:** `current_core/`, `hierarchy/`, `baryo_rm/`, `alpha_amp/`, `tests_analytic/`  
**Rule:** **exit 0 ≠ PASS.** NO FABRICATIONS. No MCMC. No PolyChord. No H₀ book.  
**Fences (this grade):**  
- `validate_dcdf` **T1 null_limit** = **"not pathologically wrong" 10% band** — **NOT** ΛCDM recovery.  
- Forward **ω_J OPEN-BLOCKED** (back-solve only; #39 seat+pinning owed).  
- **Void floor OPEN** (RM scale paid; amplitude gap unclosed).  
- **Hierarchy residual OPEN (size only)** — horn-(a) narrowed, not closed.  
- Desk `token_PASS` in SUMMARY ≠ physics promotion.

---

## Key numbers table (return)

| quantity | value | source log | grade note |
|---|---|---|---|
| **T1 null_limit gate** | `\|Δσ₈\|/σ₈ < 10%` **and** `\|ΔPₖ\|/Pₖ < 10%` | `validate_dcdf.py` L107–109 | **"not pathologically wrong"** — **not** ΛCDM recovery |
| T1 Δσ₈ | **3.276%** (0.8229 → 0.7959) | `current_core/logs/validate_dcdf.log` | under 10% band → machine PASS |
| T1 ΔP(k=0.1) | **7.110%** (1.074e4 → 9.979e3) | same | under 10% band → machine PASS |
| T1 ΔC_ℓ(TT,ℓ=200) | **2.265%** | same | reported; not in hard gate |
| T1 timing | **42.13 s/eval** · ~176 CPU-hr @15k | same | **WARN** (advisory; PolyChord deferred) |
| T1 boundary | **7/7 PASS** | same | blocking gate PASS |
| T2 r_s,drag | **148.77 Mpc** | same | PASS (band 140–160) |
| T2 first peak | dCDF ℓ=**222**, LCDM ℓ=221, **Δℓ=1** | same | PASS |
| T2 fσ₈ | z=0.38/0.51/0.61: **0.594 / 0.594 / 0.589** vs BOSS 0.497/0.458/0.436 | same | **WARN** (>20% @ mid/high z) |
| **T1 blocking (null+boundary)** | **PASS** | same | instrument OK — **≠ cosmology COMPLETE** |
| clustering ratio P_dCDF/P_LCDM @0.1 | **0.9289** | `test_dcdf_clustering.log` | desk audit only |
| **horn-(a) residual size** | **×5–10 on M_anchor** (adverse) on top of **×2.003** IR overshoot | `hierarchy_6f_double_count.log` | **OPEN (size only)** — NARROWED, NOT CLOSED |
| α(0) anchor overshoot | **×2.003** vs 4π m_H = 1573.9 GeV | `hierarchy_alpha_scale_fork.log` | best-case IR endpoint |
| exact-landing need | 1/α = **140.74** (α_c=0.021316); IR cap 137.036; gap **2.70%** | same | outside QED range |
| O(λ) band after c+a | **0.549–1.784 TeV** (×3.2 control); 4π m_H at **0.687×** full O(λ) | `hierarchy_fock_self_energy.log` / `hierarchy_anchor_budget.log` | perturbative-control band |
| vertex c (#141) | **c ≈ 0.78926** (partial; timeout) | `hierarchy_vertex_crossed_box.log` | **timeout** at 180s — not a close |
| **ω_J (back-solve)** | **5.672 keV** | `baryo_rm/logs/baryo_junction.log` | BACK-SOLVED; in ACCEPT [3,12] keV |
| j = ω_J²/Γ_φ | **5.97 meV** | same | BACK-SOLVED |
| R = ω_J²/(2 Γ_φ θ̇) | **5×10⁻⁵** = R_need; ratio **1.0000** | same | quartet **CONSISTENT** |
| Γ_φ/θ̇ (computed) | **9.032×10⁷** (not 10⁷ shorthand) | `junction_quartet.log` | factor-9 artifact retired |
| **forward ω_J** | **OPEN-BLOCKED** | junction logs + #39 | seat χ + pinning curvature owed |
| **RM ξ_K scale** | **256 Mpc** comoving; θ_ξ(χ_*)=**1.066°**; ℓ_π=**168.9** | `rm_coherence.log` | **scale paid** |
| **void shortfall** | B_blazar/B_seed = **20** (**1.30 dex**); seed 5×10⁻¹⁸ G vs floor 10⁻¹⁶ G | same | **VOID FLOOR OPEN** |
| α_c recorded | **0.021892** = 3α(0) | `alpha_c_band.log` | **OUTSIDE** band [0.0205, 0.0214] by **2.30%** |
| α_c exact landing | **0.021316** (d=**2.9211**) | same | inside band; d=3 excluded at every scale |
| A_s frac offset | **−0.92%** (formula 2.081e-9 vs 2.100e-9) | `alpha_c_same.log` | PERMANENT BET P-2026-040 (value referee) |
| #11 mass pin | m ≈ **2.24×10⁻²⁰ eV** for ε=1.24% (c=1, f_amp=0.6) | `amplitude_11_analytic.log` | decade OK; exact needs mass pin |
| BAO (alpha_amp) | r_drag model **145.25** Mpc · LCDM **147.06** · χ²(6pts)=**8.8** | `bao_scale.log` | background-only desk number |
| birefringence | f_n(z_rec)~**1e-8** at z_x=1e5 (n=4); window needs z_x~**3481** for 1% | `birefringence.log` | **WINDOW CLOSED** at model z_x |
| methanol vs 21cm | molecular **35×** tighter; σ_ε need **1.13e-6**/band to match | `amplitude_standing.log` | paper does **not** improve amplitude |
| local gravity | all sites \|dG/G\|=0; η_EP=0 | `test_local_gravity.log` | analytic PASS |
| BBN activation | ρ_φ/ρ_r = **2.75e-20** ≪ 0.01 @ a=1e-6 | `test_bbn_activation.log` | analytic PASS |

---

## 1. Pack availability

| pack | SUMMARY.md | jobs | exit0 | nonzero | timeout | stamp (UTC) |
|---|---|---:|---:|---:|---:|---|
| `current_core` | yes | 2 | 2 | 0 | 0 | 2026-08-04T09:52:15Z |
| `hierarchy` | yes | 11 | 10 | 0 | **1** | 2026-08-04T09:48:54Z |
| `baryo_rm` | yes | 4 | 4 | 0 | 0 | 2026-08-04T09:42:59Z |
| `alpha_amp` | yes | 7 | 7 | 0 | 0 | 2026-08-04T09:44:25Z |
| `tests_analytic` | yes | 2 | 2 | 0 | 0 | 2026-08-04T09:43:03Z |

Paths under:  
`docs/working_logs/_runs/desk_compute_full_20260804/{pack}/`

---

## 2. current_core — validate_dcdf T1/T2 (gate disclosure)

**Log:** `current_core/logs/validate_dcdf.log` (t=548.5 s, exit 0, SUMMARY token_PASS=True — **token ≠ full promotion**).

### 2.1 Gate disclosure (mandatory)

| item | text / number |
|---|---|
| **What T1 null_limit is** | Pure dCDF fluid vs ΛCDM: `ds8 < 0.10` **and** `dpk < 0.10` |
| **Source comment** | *"Pure dCDF vs ΛCDM can differ at O(few%); gate is **not pathologically wrong**"* (`validate_dcdf.py`) |
| **What T1 is NOT** | **Not** ΛCDM recovery · **not** precision cosmology match · **not** H₀ / S₈ tension resolution · **not** nested-evidence COMPLETE |
| **Blocking set** | `null_limit` + `boundary` must PASS; `timing` WARN is advisory (PolyChord deferred on this box) |
| **T2 role** | Diagnostic (BAO / peaks / fσ₈); non-blocking for “instrument OK” banner |

### 2.2 Measured T1/T2

| tier | test | result | numbers |
|---|---|---|---|
| **T1** | null_limit | **PASS** (10% band) | Δσ₈=**3.276%**, ΔPₖ=**7.110%**, ΔC_ℓ₂₀₀=**2.265%** |
| **T1** | timing | **WARN** | mean **42.13 s**/eval; ~**176** CPU-hr if 15k nested evals |
| **T1** | boundary | **PASS** | all 7 points stable (ρ_inf, deltam_mode, ξ_Neff) |
| **T2** | bao | **PASS** | r_s,drag=**148.77 Mpc** ∈ [140,160] |
| **T2** | cmb_peaks | **PASS** | ℓ₁=222 vs 221, **Δℓ=1** |
| **T2** | fsigma8 | **WARN** | frac diffs ~0.20 / **0.30** / **0.35** vs BOSS |

**Banner from log:** *TIER 1 BLOCKING GATES PASS (null + boundary) — CURRENT_CORE instrument OK.*  
**Honest grade:** **instrument desk PASS under disclosed 10% pathology gate.** Do **not** rephrase as “recovers ΛCDM” or “core COMPLETE.”

### 2.3 test_dcdf_clustering

| item | value |
|---|---|
| exit | 0 · token_PASS=False |
| σ₈ LCDM / dCDF | 0.8232 / 0.7962 |
| P ratio @ k=0.1 | **0.9289** |
| grade | **desk audit** (clustering-like-DM slogan only; same 10%-class proximity) |

---

## 3. hierarchy — horn-(a) residual (size only; OPEN)

**SUMMARY:** 11 jobs · exit0=10 · timeout=**1** (`hierarchy_vertex_crossed_box` −9 after ~198 s).

### 3.1 Horn-(a) residual size (primary debt)

From `hierarchy_6f_double_count.log` + `hierarchy_alpha_scale_fork.log`:

| claim | status | number |
|---|---|---|
| Naive “run α to pairing scale” double-count vs TF screening | **narrowed** | TF screening ~**62×** larger than full QED run to M_Z |
| Residual after narrowing (charged constituents / same U(1)) | **OPEN** | **factor of order 5–10** on M_anchor (adverse) |
| IR best-case overshoot (α(0)) | recorded | **×2.003** vs 4π m_H |
| α(M_Z) / Planck-floor overshoots | recorded | **×11.17** / **×955.5** |
| Exact landing 1/α | **outside QED** | need **140.74** > IR cap **137.036** (gap **2.70%**) |

**VERDICT (logs):** **NARROWED, NOT CLOSED.** Residual **OPEN (size only)** — sized adverse **×5–10**, does **not** move the anchor into acceptance. Hierarchy debt remains open.

### 3.2 Other hierarchy jobs (desk grade, not promotion)

| job | exit | true grade | residual still OPEN |
|---|---:|---|---|
| `hierarchy_6f_double_count` | 0 | **desk audit** — residual **sized ×5–10** | horn-(a) **OPEN** |
| `hierarchy_alpha_scale_fork` | 0 | **desk audit** — fork priced; IR ×2.003 | exact landing **outside QED** |
| `hierarchy_anchor_budget` | 0 | **desk audit** — O(λ) band **0.55–1.78 TeV** dominant | next order / nonpert. pairing **OPEN** |
| `hierarchy_fock_self_energy` | 0 | **desk audit** — a=0.2807; c+a=1.070; M~1.08 TeV full O(λ) | O(λ²) **OPEN** |
| `hierarchy_kF_and_bendover` | 0 | **desk audit** — k_F cancels; bend-over condenses | bend-over **not** anchor source |
| `hierarchy_vertex_crossed_box` | **timeout** | **incomplete** (c~0.789 at n=24) | full vertex integral **OPEN** |
| `basement_*` (5 jobs) | 0 | desk audits / fences | species / μ₅ / screening threads as per each log — **not** hierarchy close |

---

## 4. baryo_rm — junction back-solve; forward OPEN-BLOCKED

**SUMMARY:** 4/4 exit 0. Only `junction_quartet` carries SUMMARY token_PASS=True (algebra closure).

### 4.1 Back-solve numbers (paid internal consistency)

| quantity | value | type |
|---|---|---|
| Γ_φ | 5.39×10⁹ eV | COMPUTED (G_F² T_sph⁵) |
| θ̇ | 59.68 eV | COMPUTED |
| Γ_φ/θ̇ | **9.032×10⁷** | COMPUTED (not 10⁷ shorthand) |
| R needed | 5×10⁻⁵ | COMPUTED (η band) |
| **ω_J** | **5.672 keV** | **BACK-SOLVED** |
| **j** | **5.97 meV** | **BACK-SOLVED** |
| R / R_need | **1.0000** | CONSISTENT <2% |
| ACCEPT band | ω_J ∈ **[3.0, 12.0] keV** | pre-registered grading |
| shorthand artifact | ω_J_fake=1.887 keV | **NOT a target** (×9 compression) |

**Quartet:** **CLOSES** with computed ratio (`junction_quartet.log` VERDICT). No internal ×9 physics discrepancy.

### 4.2 Forward ω_J

| item | status |
|---|---|
| Forward derivation from seat χ + pinning curvature (#39) | **OPEN-BLOCKED** |
| Back-solve consistency | paid (desk) |
| Promotion to Derived / COMPLETE | **FORBIDDEN** until forward derivation exists |

### 4.3 RM scale paid; void shortfall OPEN

| item | number | status |
|---|---|---|
| ξ_K | **256 Mpc** comoving | **scale paid** (corpus formula) |
| χ_* | 13.76 Gpc | recorded |
| θ_ξ(χ_*) | **1.066°** | paid geometric |
| ℓ_π(χ_*) | **168.9** | paid geometric |
| B_seed | 5.0×10⁻¹⁸ G | smooth Harrison / CAP |
| B_blazar floor | 1.0×10⁻¹⁶ G | **external**; model does **not** reach |
| **void shortfall** | **×20 (1.30 dex)** | **VOID FLOOR OPEN** |
| absolute σ_RM | — | needs external n_e — **not claimed** |

`winding_turn`: accumulated vs instantaneous f̄ readings diverge in kind; α_c 2.08% conflict **not closed** by turn budget (desk audit only).

---

## 5. alpha_amp — α_c / amplitude / BAO / birefringence

**SUMMARY:** 7/7 exit 0 · **zero** SUMMARY token_PASS (all False) — correct non-promotion hygiene.

| job | exit | true grade | residual still OPEN |
|---|---:|---|---|
| `alpha_c_band` | 0 | **desk audit** — d=3 **excluded** 2.30% above band; landing α_c=0.021316 inside | identification α_c=3α **OPEN** (horn fork → (b)) |
| `alpha_c_same` | 0 | **PERMANENT BET P-2026-040** — d=3 geometric; same-response **NOT DERIVED**; A_s −0.92% | base-α / doped-pair microphysics **OPEN** |
| `amplitude_standing` | 0 | **desk audit** — methanol **35×** tighter; paper cannot claim amplitude improve | multi-row pattern test ≠ tighter bound |
| `amplitude_11_analytic` | 0 | **desk audit** — abundance pins decade; m≈**2.24e-20 eV** for 1.24% | f_amp, c, O(1) misalignment **OWED** |
| `bao_scale` | 0 | **desk number** — r_drag 145.25 vs 147.06; χ²=8.8 (6 pts) | not a chain posterior; not H₀ book |
| `birefringence` | 0 | **WINDOW CLOSED** at model z_x~1e5 (f_n~1e-8) | opens only if z_x~few×10³ (**#11 pin**) |
| `audit_math` | 0 | **desk audit** — large booked-vs-got card (1374 `ok` lines) | algebra recompute ≠ physics COMPLETE |

---

## 6. tests_analytic

| job | exit | token_PASS | true grade |
|---|---:|---|---|
| `test_local_gravity` | 0 | True | **analytic PASS** — Cassini/EP/PPN zeros under stated map; **not** full GR + medium promotion |
| `test_bbn_activation` | 0 | True | **analytic PASS** — ρ_φ/ρ_r ≪ 10⁻² at a=10⁻⁶ upper bound only |

---

## 7. Counts (this grade scope)

| metric | n |
|---|---:|
| Packs graded | **5** |
| Jobs total | **2+11+4+7+2 = 26** |
| exit 0 | **25** |
| timeout | **1** (hierarchy vertex) |
| nonzero | **0** |
| True physics **COMPLETE** promotions from this wave | **0** |
| Instrument / analytic desk PASS under disclosed gates | T1 null+boundary; local gravity; BBN activation; baryo quartet algebra; RM **scale** |

---

## 8. Explicit NON-PROMOTIONS

Do **not** promote any of the following on the strength of this grade:

1. **validate_dcdf T1 → “ΛCDM recovery” / CURRENT_CORE COMPLETE** — gate is **10% non-pathology only**; Δσ₈~3.3%, ΔPₖ~7.1% are **allowed differences**, not precision match.  
2. **T1 banner “instrument OK” → nested evidence / PolyChord / Metropolis COMPLETE** — PolyChord deferred; timing WARN; MCMC out of scope.  
3. **T2 fσ₈ WARN → growth sector closed or failed fatal** — diagnostic WARN only.  
4. **Hierarchy horn-(a) → CLOSED** — **NARROWED only**; residual **×5–10 OPEN (size only)**; anchor still **×2.003** IR overshoot.  
5. **hierarchy_vertex timeout → vertex c COMPLETE** — partial c≈0.789; job **timed out**.  
6. **ω_J = 5.672 keV → forward Derived** — **BACK-SOLVED only**; **forward ω_J OPEN-BLOCKED** (#39).  
7. **Quartet CONSISTENT → baryogenesis COMPLETE** — internal R identity; no first-principles ω_J.  
8. **1.90 keV shorthand target** — **artifact**; do not adopt.  
9. **RM coherence scale → void / blazar B floor closed** — **void shortfall ×20 (1.30 dex) OPEN**.  
10. **α_c = 3α identification → Derived / COMPLETE** — band **excludes** d=3; permanent bet on value only (P-2026-040).  
11. **A_s −0.92% → same-response theorem** — referee on IR value, not Π_T≡Π_L identity.  
12. **Amplitude #11 / standing → |ε| improved vs methanol** — paper **cannot** claim amplitude improvement (35×).  
13. **BAO χ²=8.8 → DESI/BAO tension resolved or H₀ booked** — background desk curve only; **no H₀ book**.  
14. **Birefringence window closed → all CMB birefringence claims free** — closed **at model z_x**; reopens if #11 pins z_x near equality.  
15. **tests_analytic PASS → local tests / BBN sector COMPLETE** — analytic upper-bound scripts only.  
16. **Any SUMMARY token_PASS or exit 0 bulk “N/N PASS”** — false equivalence; true grades above.  
17. **Any OPEN residual → COMPLETE** (fence).  
18. **H₀ book · PolyChord · live MCMC surgery · fabrications · PolyChord evidence** — forbidden this wave.

---

## 9. Log pointers

| pack | SUMMARY | key logs |
|---|---|---|
| current_core | `current_core/SUMMARY.md` | `logs/validate_dcdf.log`, `logs/test_dcdf_clustering.log` |
| hierarchy | `hierarchy/SUMMARY.md` | `logs/hierarchy_6f_double_count.log`, `hierarchy_alpha_scale_fork.log`, `hierarchy_fock_self_energy.log`, `hierarchy_anchor_budget.log`, `hierarchy_vertex_crossed_box.log` |
| baryo_rm | `baryo_rm/SUMMARY.md` | `logs/baryo_junction.log`, `junction_quartet.log`, `rm_coherence.log`, `winding_turn.log` |
| alpha_amp | `alpha_amp/SUMMARY.md` | `logs/alpha_c_band.log`, `alpha_c_same.log`, `amplitude_*.log`, `bao_scale.log`, `birefringence.log`, `audit_math.log` |
| tests_analytic | `tests_analytic/SUMMARY.md` | `logs/test_local_gravity.log`, `test_bbn_activation.log` |

---

*NO FABRICATIONS. exit 0 ≠ PASS. T1 = 10% non-pathology, not ΛCDM recovery. Forward ω_J OPEN-BLOCKED. Void floor OPEN. Hierarchy residual OPEN (size only). Grade complete for current_core / hierarchy / baryo_rm / alpha_amp / tests_analytic packs only.*
