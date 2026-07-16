# BUILD SPEC — The 2-loop RG-improved V_eff for T_c (the DE-value closer)

> *Commissioned 2026-07-16 (hunt entries 210–214), then EXECUTED (hunt 215).*

> **RESULT (hunt 215 — DEFINITE NEGATIVE):** the 2-loop RG-improved V_eff does **NOT pin T_c** — and
> the answer is robust to the one uncomputed piece (the non-log 2-loop constant c₀). Two facts settle it:
> (1) at the natural scale μ = m_e there is **no symmetry breaking** (SSB needs μ < ~310 keV, a large log);
> (2) the scale-stationary PMS sits at L ~ 1/α ~ 200 → μ ~ e⁻¹⁰⁰ m_e, unphysical for **any** O(1) 2-loop
> coefficient (the O(α) curvature is too weak). So **T_c is not a perturbatively well-defined quantity**;
> the dyad's electron-CW condensation is a large-log/marginal effect, and the seam route ρ_Λ¼ = (9/2)α⁴T_c
> has no perturbative T_c to evaluate. Defining T_c needs a NON-perturbative (gap-equation/lattice) build,
> if the condensation survives resummation at all. The full 2-loop diagrammatic spec below stands as the
> record of what was attempted; the negative verdict does not depend on completing it.
>
> **FOLLOW-ON (hunt 216 — the non-perturbative build, executed):** the NJL/BCS gap equation for the
> composite dyad IS cutoff-regulated → **T_c = Λ·τ(g) is well-defined** (log-ambiguity resolved). For
> natural inputs (Λ=m_e, g~2.8 above the critical g_c=2) ρ_Λ¼=(9/2)α⁴Λτ(g) lands **1.0–1.1×**. The
> residual is now two physical medium-compositeness parameters (Λ, g). The next build is to derive (Λ, g)
> from the medium's own dynamics.

*This was a BUILD SPECIFICATION for a genuine multi-loop QFT computation. It states the objective, the
exact diagram, the method, the inputs, and the acceptance tests. The RG-improvement (leading-log,
sufficient for the verdict above) was executed; the full diagrammatic 2-loop constant was not needed.*

---

## 1. Objective

Pin **T_c**, the dyad's Coleman–Weinberg condensation temperature, to a **renormalization-scale-
independent** value. T_c is the last free scale in the derived dark-energy scaling

> **ρ_Λ¼ = (9/2) α⁴ T_c** (hunt 210–211; α⁴ = α_c² dCDF-binding × α² EM-handshake, both derived/ramped).

At leading-log, T_c carries a **factor-~10 RG-scheme ambiguity** (hunt 212), so the DE *digit* is
open even though the *scaling* is derived. The 2-loop V_eff supplies the log² curvature that fixes
the scale. Success = a computed ρ_Λ¼ to compare against the observed 2.25 meV.

## 2. Why 1-loop is insufficient (established, hunt 214)

- T_c = m_e0·√(3(L−1)/2π²), L−1 = ln(m_e0²/μ²) − 3/2. The overall coupling **κ cancels** (both the
  zero-T induced mass m_φ²(0) and the thermal Δm² are ∝ κ), so T_c's μ-dependence is entirely the
  leading-log bracket.
- The 1-loop β-functions (worked out, hunt 214):
  - γ_{m_e} = 3α/2π
  - β_{m_φ²} = (κ/π²) m_e0⁴
  - β_κ ≈ (3α/2π)κ + O(κ², λκ)
- The O(α) running of the source S = κ m_e0⁴ puts a PMS stationary point at μ*/m_e ~ e⁻⁵⁷ —
  **unphysical.** So the leading log is NOT fixed at 1-loop; the 2-loop is genuinely required.

## 3. The theory (dyad–electron sector)

L = ψ̄(i∂̸ − eA̸ − m_e0)ψ − ¼F² + ½(∂φ)² − V(φ) − **m_e0 κ φ²ψ̄ψ**

- φ: real, charge-free dyad scalar; V(φ) = ½m_φ,bare²φ² + (λ/4!)φ⁴.
- The coupling is a **dim-5** operator g₅φ²ψ̄ψ, g₅ = m_e0κ, [κ] = mass⁻². Handle the
  non-renormalizable structure with an EFT cutoff / operator-mixing treatment.

## 4. The computation to perform

**The 2-loop electron contribution to V_eff(φ, T):** the **photon-dressed electron loop** — the
O(α) correction to the 1-loop CW electron determinant (electron loop with one internal photon).
This diagram carries the **log² term** that provides the physical curvature to pin μ.

1. Compute the 2-loop effective potential V₂(φ, μ) for scalar-QED-Yukawa (standard techniques:
   Ford–Jack–Jones / Martin's 2-loop V_eff, or direct diagrammatics). Include the O(α) photon-
   exchange inside the electron loop and the λ, κ sunset topologies.
2. Do it at **finite T** with the **exact** fermionic thermal function J_F(m_e/T), NOT the high-T
   expansion — T_c < m_e, so the electrons are Boltzmann-suppressed (regime error found in hunt 213;
   the high-T formula under-estimates T_c by ×1.4). Daisy/ring resummation of the soft thermal modes
   should be included at the same order.
3. RG-improve: run the couplings with the 1-loop β's (§2) plus the 2-loop β_κ (compute it here), and
   verify the result is μ-independent.
4. Solve m_φ,eff²(0; T_c) = 0 (or the appropriate ⟨φ⟩ onset) for the RG-invariant T_c.

## 5. Inputs already in hand (do not recompute)

- 1-loop β-functions and the κ-cancellation (hunt 214, §2 above).
- The exact finite-T fermion loop J_F and the ×1.4 regime correction (hunt 213; script
  `scripts/Tc_exact.py`).
- The expansion check: the transition is adiabatic (m_φ/H ~ 10²⁰) and the electron bath is in
  equilibrium at T_c, so an EQUILIBRIUM V_eff is the correct object (hunt 213 addendum;
  `scripts/expansion_check.py`). No supercooling correction needed.
- The seam scaling ρ_Λ¼ = (9/2)α⁴T_c (hunt 210–211; `scripts/seam_scale.py`, `alpha2_derive.py`).

## 6. Acceptance tests (ramp-law — the build is graded on these)

1. **RG-invariance (the whole point):** dT_c/d ln μ = 0 to 2-loop order, swept across μ ∈ [T_c, m_e].
   A residual μ-dependence larger than the 3-loop estimate fails the build.
2. **Limit checks:** (a) recovers the 1-loop leading-log as α → 0; (b) recovers the high-T thermal
   function as m_e/T → 0.
3. **Regime consistency:** the exact-J_F ×1.4 uplift (hunt 213) must be reproduced by the full
   treatment.
4. **The verdict number:** report ρ_Λ¼ = (9/2)α⁴T_c against observed 2.25 meV. NOTE the equilibrium
   estimate currently **over-predicts ~2×** at μ=v (hunt 213); the 2-loop must either move it onto
   the value or confirm the over-prediction (which would be an adverse result against the seam route).

## 7. Effort / tools

A genuine 2-loop effective-potential calculation (weeks-class, not a reply). Candidate tools: a 2-loop
V_eff package (e.g. `2ndPole`/`SARAH`-class or hand-computation with the Martin formulae), plus a
finite-T module for J_F and daisy resummation. Deliverable: a short technical note + the computed
RG-invariant T_c and ρ_Λ¼, filed back against this spec.

## 8. What this does NOT resolve

Even a clean T_c leaves the DE *absolute* value riding **m_ν = the L-breaking spurion μ** (underived
value, hunt 207) if the seam route is taken as the primary. The two other standing DE-value blockers —
the **ohmic-vs-sub-ohmic response exponent** (hunt 189, the thermal-door coefficient) and the
**spurion value** (hunt 207) — are separate builds. This spec closes ONLY the T_c leg of the seam
scaling ρ_Λ¼ = (9/2)α⁴T_c.

## See also

Hunt entries 208–214 ([PRTOE_DERIVATION_HUNT.md](PRTOE_DERIVATION_HUNT.md)); the CC value routes
([PRTOE_cosmological_constant.md](PRTOE_cosmological_constant.md) §2c); the T_c mechanism
([PRTOE_me_mechanism_math.md](PRTOE_me_mechanism_math.md)).
