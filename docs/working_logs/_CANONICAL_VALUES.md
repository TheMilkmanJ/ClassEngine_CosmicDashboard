# Canonical values — the one place a disagreement gets settled

> *Created 2026-07-20 on the owner's instruction. Purpose: when two files disagree about a number,
> this file says which is right, where it comes from, and what proves it — so the disagreement is
> resolved by **lookup**, not by re-derivation and not by whichever carrier the auditor met first.*

## How to use this file

**When you find two files saying different things about one quantity, come here FIRST.** Audit
protocol check 20a: a disagreement has three possible answers — the first is wrong, the second is
wrong, or **they are about different objects**. The third has been the answer twice in one day, so
check the "what it is NOT" column before writing either file down as wrong.

**Every row carries four things:** the canonical value, its home (where it is derived, not where it
is quoted), its proof (a harness check ID or a script), and its grade. A row with no proof column is
a row that has not earned a place here.

**Adding a row:** only for quantities that appear in more than one file, or that have already caused
one contradiction. This file is not an index of every number — it is the adjudicator for contested
ones. Keep it short enough to stay true.

---

## Standing constants — verified by forward recomputation 2026-07-20

Recomputed from α and m_e alone, independently of `audit_math_pass.py`, and every link landed.

| quantity | canonical value | home (derived) | proof | grade |
|---|---|---|---|---|
| α_c | 3α = 0.021892 | MATH_SPINE; the 3 is the **spatial dimension d**, not the flavour count | harness, P-2026-040 | registered bet |
| k | 1.36461191 | hierarchy §6c, two-band screened kernel | harness; three-way concordance 1.360 / 1.36461 / 1.3602 | derived |
| λ (pairing) | kα_c = 0.029874 | hierarchy §6c | harness | derived |
| τ | ½ln2 = 0.34657 | the Koide kernel | harness; lattice-refereed P-2026-048 | candidate, referee pending |
| T_c | **177.10 keV** | τ·m_e | harness | derived |
| ρ_Λ¼ | **2.2599 meV** (+0.44% vs observed 2.25) | (9/2)α⁴T_c | harness | **existence yes, precision NO** — see below |
| ε | 1.2543% = 27α/5π | c·f̄·α_c | harness; closed form agrees to all quoted digits | derived, but see c |
| f̄ | 2/π = 0.63662 | the winding time-average | harness | derived |
| c | 9/10 | census count (N−1)/N | harness (the one-criterion alternatives) | **counting assumption, data-confirmed** — not framework-forced (#126) |

## Contested or corrected — the rows this file exists for

| quantity | canonical | what it is NOT | ruling |
|---|---|---|---|
| **ρ_Λ¼'s +0.44%** | two different statements share this number | a single claim | **In τ-space** it is exact arithmetic between the kernel's 0.34657 and the observation-inverted 0.34506 — no control caveat applies. **As a precision claim about ρ_Λ¼** it is suspended: the composite quartic sits above its control edge (λ = 26–46 vs λ\* = 22.41), giving an uncontrolled 5.4–9.8% (#169). Do not "fix" the τ-space statement. |
| **m_ββ window** | **[0.04, 5.3] meV** | [0.02, 5.3] | The 0.02 floor came from m₁ = 2.2842 meV, which is the **retired** T_c = 179 keV route's output; the ledger records its "+1.5%" as the T_c *rounding*, not a spread. Real uncertainty on ρ_Λ¼ is **0.449%** (Planck's 1.80% on ρ_Λ, quartered). |
| **T_c = 179 keV** | **not canonical** | a derived value | Observation-inverted 176.32 keV rounded up. Retired. The derived value is 177.10 keV. |
| **exact-kernel T_c band** | **307–714 keV** | 250–530 keV | Recomputed from the kernel that reproduces the corpus's own |J_F′| = 0.374. The booked 250–530 corresponds to L−1 ∈ [0.50, 4.78], not the stated [1, 10] — band and range were never one computation (#182). |
| **F_dark/√σ** | **0.40–0.47** | in conflict with the NJL route's 0.1759 | Not a disagreement: the NJL script computes **f/Λ**, not f/√σ. Its own QCD calibration fails by 1.42×. The 2.39 factors as 1.424 × 1.186 × 1.419; only the middle is physics (#134). |
| **winding integer n** | **n ≳ 1.65** (a bound) | n ~ 10–30 (a determination) | `L_gen` is never assigned a value anywhere in the corpus. n ~ 10–30 requires L ≈ 1000–9000 Gpc against a floor of 27.6 Gpc, and L is bounded only below (#180). |
| **O(λ) correction c + a** | **1.069939** = 0.789262 + 0.280677, both positive | ~2.7 either way | Complete at this order, both terms integrated not argued. Crossed box c = 0.789262, 11 digits, validated against Gor'kov–Melik-Barkhudarov (1+ln4)/3 to 5×10⁻¹¹ (#141). Fock self-energy **a = (1+2b)/2 − 1/ln(1+1/b) = 0.280677** in closed form, validated against the textbook Slater exchange self-energy and the independently derived large-b limit a → 1/(12b) (#183). They do **not** cancel — V is instantaneous, so Z = 1 and the effect is a velocity renormalization with a pointwise-positive integrand. Anchor band **0.55–1.78 TeV** (0.55–1.90 if the screening is fed back). |
| **varying-m_e support** | Hart & Chluba 2020 at **3.5σ**; recent ACT+DESI fit at **1.8σ** | "preferred at 2–3.6σ" | The 2.5–3.6σ is the **residual tension left over** in arXiv:2607.13282, not a preference. Check citations against abstracts, not against docs that quote them. |
| **Koide phase deviation δθ** | **+7.409×10⁻⁶ rad** | −7.0×10⁻⁶ | θ_B = 0.2222296315 rad from the pole masses (three independent solves: the circulant fit, and the phase from m_τ/m_e and from m_μ/m_e with A fixed by Q alone), against 2/9 = 0.2222222222. **Positive in every ring convention that puts θ_B near 2/9 at all**, and P-2026-057 already recorded θ_B = +0.222229 rad. The magnitude 7.06×10⁻⁶ is what the *rounded* 132.7328° display returns — 5% of pure rounding in a difference of near-equal numbers (#102). |
| **Koide amplitude deviation δA** | **−1.3057×10⁻⁵** | −1.36×10⁻⁵ | The latter is the display 1.414200 minus √2. The source A = 1.4142005052, forced by Q alone through A = √(6Q − 2). Sign is right in both; magnitude is 4% off (#102). |
| **P-2026-051's residual** | **+0.89σ**, on the side a positive slope does not predict | −0.31σ, or −0.54σ | Three compounding causes, none of them the slope: the δθ sign, both deviations propagated from displays, and σ taken on one axis. m_e and m_μ are effectively exact, so both axes are functions of m_τ alone and are **anti-correlated at exactly −1** — the error must be taken on the residual, +9.461×10⁻⁶ ± 1.061×10⁻⁵ (#102). |
| **the m_τ the Koide sector requires** | **1776.96903 MeV** (from Q = 2/3) | an agreement, or three of them | The phase watch needs 1776.96651 and the closure 1776.96705; all three are **+0.91σ** above the measured 1776.86 ± 0.12 — one displacement, not three. They span **2.52 keV = 1.42 ppm**, so below that precision testing the closure and testing A = √2 are the same measurement (#102). |
| **Koide's miss: 18 ppm or 9.2 ppm** | **both, and they are the same miss** | a disagreement | 18.47 ppm is the fractional miss on V/μ² = 3Q − 1; 9.23 ppm is the same miss quoted on Q itself. **The factor between them is 2, not 3** — the identity's slope is dV/dQ = 3, but the two are quoted as *fractional* misses, and converting brings in Q: (dV/V)/(dQ/Q) = 3·Q = 3 × ⅔ = **2**. Verified by forward recomputation from the pole masses. Do not "reconcile" the two figures (#101). |
| **cosmic-dawn trough** | **≈1.0% deeper** | ~4.6% | The estimate charged the full −3ε to the gas temperature. Sign is the registered content and holds (#175). |
| **quadrupole retention (27.6 Gpc)** | **90%** | 83%, or the toy's 49% | A torus is a lattice, not a continuum with a sharp cutoff; six modes sit exactly at k_min (#160). |
| **f_wind** | **≲3×10⁻⁵**, 255× under the fence | inside [0.7%, 1.4%] | The diagonal C_ℓ sees only the k̂-monopole. Location claim survives; detection claim does not (#170). |
| **induced α split** | **23.5%** | ~44% | The 44% is hypercharge at M_Z; α_c = 3α names α_EM at q = 0 (#130). |
| **the quark chain's loop factor** | **both are right, for different jobs** (#185) | a contradiction to be resolved one way | The naive two-loop counting is exact: e⁴/(16π²)² = 4πα·4πα/(16π²)² = **(α/4π)² = 3.37×10⁻⁷**. `bbn_witness` and `me_mechanism_math` carry that and are self-consistent with it (3×10⁻⁷ → quark shift ~1×10⁻⁹ ✓). The **(α/π)² = 5.40×10⁻⁶** used downstream is 16× larger and **deliberately conservative** — it quotes the closure against the easiest case for a quark channel to survive. Nothing turns on the choice: the channel is 20 000–31 000× short on the conservative factor and 16× shorter still on the naive one. Do not "fix" either file to match the other. |
| **the ε-blind ensemble** | **c = 0.903 ± 0.0375** — a *check* on c | a selection among the candidates | It lands −0.08σ from 9/10, and at the same width sits +0.53σ from 12/13 and −0.38σ from the charge²-weighted **8/9**, which is only **0.30σ** from 9/10. The pre-registered separating width is **σ_c ≤ 0.0115** (3.3× sharpening, not in hand). What picks 9/10 over 12/13 is the tie-as-lock argument, not this number (#126). |
| **the charge²-weighted census** | **c = 8/9**, from Σ N_c Q² = 3 + 4 + 1 = **8** | 14/17 = 0.8235 (the colourless sum, 4.667/5.667) | Colour is counted in the roster the count is over, so the up-type contributes 4 and the down-type 1. c = 8/9 gives ε = 16α/3π = **1.2388%**. Carrying the charge criterion all the way — the neutral seat then weighs zero — returns **c = 1**, which the census excludes (#126). |
| **the portal's Higgs branch** | **λ_p ≲ 5×10⁻¹¹ … 1×10⁻⁹** across f = 100–500 TeV | a coupling the roster does not list | |Ψ|²H†H is the *only renormalizable* SM partner of the dark bilinear, and it shifts the Higgs vev, so it moves every mass; the bound is D/H's 12–18σ on a universal shift at ε. The standing dim-6 lepton operator induces it at **λ_p ≤ 1.1×10⁻¹³** (Λ_UV = 4πf; 6.8×10⁻¹⁶ at Λ_UV = f) — 3–6 orders under, so excluding it costs no tuning (#125). |

## Open — no canonical value exists yet

Listed so nobody books one by accident.

- **T_c's owner**: MATH_SPINE assigns it to the dyad; DERIVATION_HUNT to the SU(2) confining sector. Same arithmetic, incompatible structural claims. Three recorded points lean to the confining sector. **Owner ruling pending.**
- **D/H width**: two-term ±0.0476 vs three-term ±0.0563; evidence points to two-term, moving the row −2.49σ → −2.94σ **against** the model. **Owner ruling pending** (`ForJustin/10`).
- **A_s's imprint**: freeze-out (n_s = 4, white) vs scale-invariant (ξ ∝ 1/k). Exactly one can stand (#184).
