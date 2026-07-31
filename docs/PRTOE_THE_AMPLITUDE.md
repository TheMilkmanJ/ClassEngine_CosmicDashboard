# The amplitude — ε, the model’s one added number

Glossary: [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md). Conditionality: [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md). Risk page: [PRTOE_READERS_RISK.md](PRTOE_READERS_RISK.md).

One number added to known physics: a universal fractional shift of lepton masses, ε ≈ +1.24%, controlled by one screening gate. Observable claims that route through ε live here. Grades are inline. Failures: [PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md).

---

## 1. Values

| determination | value | grade |
|---|---|---|
| Production fit (CMB likelihood chains) | **1.232%** | measured (this pipeline) |
| Derived stack ε = c·f̄·α_c = 27α/5π | **1.2543%** | **conditional** — three factors, three referees |
| Concordance joint | **1.2403 ± 0.0079%** | standing reference for configs; **not** a pure test of the stack (joint folds the stack in) |

Fit-vs-stack spread is the loaded joint; α_c chain owns the stack verdict. **Do not say “zero free parameters” unless c, f̄, and α_c all hold.** Effective grade = weakest parent.

### Factor grades

| factor | value | grade | note |
|---|---|---|---|
| **f̄** | 2/π = 0.6366 | **derived** | winding ⟨\|cos\|⟩; sim 0.635 ± 0.026 is the check |
| **c** | 9/10 | **counting assumption** | not forced; 8/9 and 12/13 still open at current ensemble width |
| **α_c** | 3α | **registered bet** (P-2026-040) | ~2% above current data point; stack fails if this fails |

---

## 2. Windows — one number across epochs

Rule: ε is owed at epoch and environment weights; no free per-window exits. Wavelength shifts from Rydberg ∝ m_e (δλ/λ = ε) are identities, not extra parameters.

| window | epoch | what ε does | grade |
|---|---|---|---|
| **CMB / H₀** | z ≈ 1100 | heavier m_e → earlier decoupling → smaller r_s → H₀ ≈ 69.9 | production fit; **provisional** (YHe treatment update pending; z_on frozen 0.053 dex off identity) |
| **windowed BBN** | ~0.7 MeV–70 keV | OFF at n/p freeze-out; growing below T_c | production (PRyM); joint **adverse** (D/H eased, Y_p pays) |
| **21 cm** | z ≈ 30–150 | rest frequencies +(1+ε)²; ν_H/ν_D ratio lock; edge shape reads the gate | registered (P-2026-022/027) |
| **ε-dipole** | today | δm_e/m_e ≈ 4×10⁻⁷, axis-correlated | registered (P-2026-024); null OK today |
| **Σm_ν de-bias** | fits | model-conditional masses stay physical (~61.4 meV) | recorded; sum not a discriminator |
| **SN channel** | z < 0.15, unscreened | sign opposite H₀ lever (closed as H₀ fix); host-mass-step candidacy | computed; DESI forest adjudicates |
| **Lyman-α forest** | z ≈ 2–3 | absorption offset ε × gate(Δ≈1) | live test |

---

## 3. The gate

ε(C) = ε₀ · g(C/C_ref): on early (above T_c = 177.10 keV for BBN window), fading over z ≈ 30–60 by **local clumping**, not a global thermal step.

Thermal/global-step reading **retired 2026-07-16** (illegal discontinuity under the depth law). Model is committed to the environmental reading: a sharp global step in the 21 cm edge **counts against** the model.

Gate fenced by forest flatness, SN host-density range, P-2026-022 fade profile, composition-cliff invariant (ΔΦ = c² · f_lep · ε₀ = (553 km/s)² at minimum). Lab / Oklo / molecular-absorber nulls sit in screened environments by construction.

---

## 4. Referees and killers

**Referees:** α_c chain; fixed-ε evidence run (Laplace until cluster nested sampling); DESI forest; lunar-farside / cosmic-dawn 21 cm; radio D/H (P-2026-027).

**Killers on file:** dark-ages detection at *standard* rest frequency; forest clean at the predicted offset; α_c chain off 3α; gate energy bookkeeping failures (see risk page).

---

## 5. What this page does *not* claim

- That the derived stack is already measured to 1.2543% (posterior width is much larger; chains incomplete).
- That H₀ ≈ 69.9 is final (sampler health / YHe / z_on caveats).
- That BBN is a win (it is the worst column).
- That CLASS evolves δm_e as a dynamical dark field (varconst is z- or density-gated; m_e is background-only by design).

---

## 6. Implementation pointer

CLASS: `dcdf_dyad_link` derives `varying_me = 1 + c·f_amp·Ψ₀/M_red` (defaults → 1.2543%); density gate optional. Production fixed-ε configs use both. Details: [PRTOE_CODE_MANIFEST.md](PRTOE_CODE_MANIFEST.md).
