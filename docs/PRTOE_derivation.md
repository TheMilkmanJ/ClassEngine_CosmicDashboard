# PRTOE: Action → Equations → Code

**Status: scaffold with verified content.** Every equation is numbered; every code
reference is `file:function`. Items marked **[DERIVE]** are implemented in code but
not yet derived cleanly from the action — they are the open theory debts.
Last synced with code: 2026-07-03.

## 0. Conventions and units

- CLASS internal density units: `rho_class = (8πG/3) ρ_phys`, dimension Mpc⁻².
- `V0_prtoe` is read in units of H₀² and scaled: `V0 → V0·H0²` (`input.c:input_read_parameters_species`).
- `m_prtoe` is read in units of H₀ and scaled: `m → m·H0` (same place). **Any m value
  calibrated before 2026-07 used a different convention.**
- `M_ew_prtoe` read in GeV, converted to Mpc⁻¹ (×1.5637×10³⁸).
- Conformal time τ (Mpc); `' ≡ d/dτ`; physical time derivatives written with overdots;
  ℋ = a′/a = aH. CLASS stores H in Mpc⁻¹ (physical).

## 1. Action

$$ S = \int d^4x \sqrt{-g}\Big[ \frac{1}{2\kappa_0} F(\phi) R - \tfrac12 (\nabla\phi)^2 - V(\phi) + \mathcal{L}_Q + \mathcal{L}_m \Big] \tag{1} $$

with

$$ V(\phi) = V_0 e^{-\lambda\phi} + \tfrac12 m^2 \phi^2 \tag{2} $$

$$ F(\phi) = 1 + \xi_{\rm eff}(\phi)\, A(\phi), \qquad
   \xi_{\rm eff}(\phi) = \frac{\xi\,\phi^2}{1+\zeta\phi^2}, \qquad
   A(\phi) = \tfrac12\big(1+\tanh\tfrac{\phi-\phi_c}{\Delta\phi}\big) \tag{3} $$

- Code: `background.c:background_functions` (V, V_φ, V_φφ); `background.h:get_xi_eff`;
  `background.h:prtoe_F_phi_of_phi` (analytic F_φ).
- The Vainshtein-style S(φ)=φ²/(1+ζφ²) and the activation A(φ) are **part of the
  definition of F(φ)** — i.e. terms of the action, eq. (3) — not code-level switches.
- **[DERIVE]** `L_Q` (the DHOST interaction sector: α², β², δ operators with 1/(1+φ²)
  screening) is stated in `prtoe_dhost_framework.tex` but its perturbation-level
  contributions are only partially implemented (the β k² term in §4). Either derive
  each operator's contribution or declare the truncation explicitly.

## 2. Background equations

Scalar EOM as implemented (`background.c:background_derivs`, PRTOE block):

$$ \ddot\phi + 3H\dot\phi + V_\phi
   = \frac{F_\phi}{F}\Big(\dot H + 2H^2\Big) - \frac{F_\phi}{F}\,\tfrac12\dot\phi^2
   - \big[\text{trans}\cdot\square F\ \text{correction}\big] \tag{4} $$

- **[DERIVE]** Eq. (4) should follow from varying (1); the exact variation for
  F(φ)R gives φ-EOM: □φ = V_φ − (F_φ/2κ₀)R with R = 6(Ḣ + 2H²) in flat FLRW.
  The implemented right-hand side uses (Ḣ + 2H²) *without* the factor arrangement
  of R/2 = 3(Ḣ+2H²); verify the 1/3 bookkeeping between eq. (4) and □φ = V_φ − (F_φ/2)R.
- **[DERIVE]** The `H_dot` estimate in the same block is labeled "simplified estimate"
  — replace with the exact expression from the modified Friedmann constraint.
- Friedmann: `background_functions` assembles ρ_tot including
  ρ_φ = ½φ̇² + V(φ) (+ coupling terms). **[DERIVE]** For F≠1 the (00) equation is
  3F H² = κ₀ρ − 3HḞ (+K-terms); confirm the implemented H matches this and not the
  minimally-coupled form.

### 2.1 Activation gates are redundant (measured 2026-07-03)

The covariant gate trans = ½(1+tanh[(ln(ρ_φ/ρ_r) − ln 0.01)/0.1]) multiplies the field
evolution. Ablation (`prtoe_ablate_gates = yes`, forces trans → 1 from a = 10⁻²⁰):

| Quantity | gated vs ungated |
|---|---|
| conformal age | 1.2×10⁻⁶ relative |
| 100·θ_s | 2×10⁻⁶ |
| C_ℓ TT/EE/TE (ℓ≤200) | ≤ 7×10⁻⁵ |

The field is frozen by Hubble friction alone (m ≪ H at early times), as in standard
quintessence. **Recommendation: remove the gate machinery from the physics path
entirely** (kept currently for A/B testing via the flag). This also applies to
`coupling_strength` mode scaling.

## 3. Local gravity / screening (derived 2026-07-03)

In a static Newtonian environment of density ρ, the scalar EOM linearizes to

$$ \nabla^2\phi = V_\phi(\phi) - \tfrac{F_\phi(\phi)}{2} R,\qquad R \simeq 8\pi G\rho = 3\rho_{\rm class} \tag{5} $$

so the chameleon equilibrium solves

$$ V_\phi(\phi_{\rm eq}) = \tfrac32 F_\phi(\phi_{\rm eq})\,\rho_{\rm class}. \tag{6} $$

Stabilization at large φ comes from Vainshtein saturation (F_φ → 0 as ξ_eff → ξ/ζ)
against V_φ → m²φ. Implemented as a log-scan + bisection in
`background.h:prtoe_phi_at_matter_density_kg_m3` (replaces the former
γ·ln(ρ/ρ₀) heuristic). Then G_eff/G = 1/F(φ_eq) (`prtoe_G_eff_over_G_at_environment`).

Measured with ξ = 5×10⁻⁶ (test_active_prtoe_simple): |γ−1| = 2.26×10⁻⁶ — passes
Cassini (2.3×10⁻⁵) by ~10× and sits **one order of magnitude below current bounds**:
a falsifiable near-term prediction of the model at this coupling.

- **Thin-shell factor: computed 2026-07-03 — NO-GO for the current action.**
  A thin shell needs m_eff(ρ_body)·R_body ≫ 1. With V = V0e^{−λφ} + ½m²φ² (m ~ H0)
  the field's Compton wavelength is cosmological at ALL densities:
  m_eff·R_sun ≈ 5×10⁻¹⁹ independent of ξ (tested ξ = 5×10⁻⁶ … 1). No shell forms;
  the Cassini boundary ξ ≲ 2×10⁻⁵ is final for this potential.
  - Quartic rescue V ⊃ κφ⁴/4 fails (peaks at m_eff·R_sun ~ 3×10⁻¹⁰): the coupling
    F_φ ∝ ξφ (from the φ² "Vainshtein" factor) self-quenches as the equilibrium
    moves to small φ.
  - Linear coupling F = 1+ξφ with κφ⁴ CAN screen the Sun (m_eff·R_sun = 1 at
    κ = 3.6×10⁴⁰, ξ = 10⁻², with V0 still supplying Λ untouched) — but the same
    φ_eq(ρ) response then pins the cosmological field at φ ~ 10⁻¹⁷, erasing all
    cosmological signatures. Within V ∝ φⁿ families the required
    solar-vs-cosmic decoupling ratio (~2×10¹⁷) exceeds the best achievable
    ((ρ_sun/ρ_cos)^{1/2} ~ 6×10¹⁴ as n→∞) by ~300×: **potential-based (chameleon)
    screening cannot open a Cassini-allowed, cosmologically detectable window
    for this model class.**
  - The known escape is KINETIC (true Vainshtein) screening — **implemented
    2026-07-03 as PRTOE v2** (`g3_prtoe`, default 0 = exact v1):
    L₃ = −(g3/Λ³) X □φ, Λ³ = M_Pl H0². Background EOM (minisuperspace):
    [1 + (6g3/Λ³)Hφ̇] φ̈ = RHS − (3g3/Λ³)(Ḣ+3H²)φ̇²; Friedmann picks up
    ρ₃ = (2g3/Λ³)Hφ̇³ (linear in H, joins Ḟ in the quadratic solve);
    p₃ = −(g3/Λ³)φ̇²φ̈ (lagged φ̈). Sun's Vainshtein radius
    r_V = (g3 r_s/Λ³)^{1/3} ≈ 120 pc; PPN estimate suppressed by (AU/r_V)^{3/2} ≈ 8×10⁻¹².
    **Measured: ξ = 10⁻², g3 = 1 → |γ−1| = 1.1×10⁻²⁰ (Cassini passed by 15 orders,
    was excluded ×450 in v1) while low-ℓ TT deviates from ΛCDM by 2.5×10⁻³.**
    The v1 scan values (ξ = 0.1 → 4.4%, ξ = 1 → 14% TT) are now in the allowed
    region: PRTOE v2 has an open discovery window ξ ∈ [~10⁻², ~1].
    **δφ galileon terms + stability conditions: DERIVED & IMPLEMENTED 2026-07-03.**
    From the quadratic action of L₃ on FLRW (DPSV structure, metric perturbations
    in L₃ neglected — valid to O(α_B)):
      N_gal = 1 + 6(g₃/Λ³)Hφ̇   (kinetic normalization; **N > 0 = no-ghost**, enforced)
      c_s² = [1 + 2(g₃/Λ³)(φ̈ + 2Hφ̇)]/N_gal   (**c_s² > 0 = gradient-stable**, advisory)
    δφ equation: N_gal δφ″ + (…)δφ′ + (c_s²k² + a²[…])δφ = a²S
    (`prtoe_perturbations_derivs`). Friction receives only O(α_B²)-different
    treatment between schemes — irrelevant at α_B ≤ 10⁻³.

    **v3 compatibility window (derived 2026-07-03): g₃ ∈ [~10⁻¹⁷, ~10⁻¹⁰].**
    Two competing requirements on g₃ with Λ³ = H₀²:
    (i) Vainshtein/Cassini: ε = (AU/r_V)^{3/2} ∝ g₃^{-1/2}; needs g₃ ≳ 1.6×10⁻¹⁷
        for ξ ~ 10⁻².
    (ii) EDE-kick survival: galileon self-friction 6(g₃/Λ³)Hφ̇ at z_eq (with
        φ̇ ~ ξ₁Ω_m H/2) must be ≪ 1 → g₃ ≲ 2×10⁻¹⁰. At g₃ = 1 the braiding is
        ~10⁹ at equality and the galileon crushes the kick (terminal velocity
        φ̇ ~ H₀-scale → f_EDE ~ 10⁻¹²): **g₃ = O(1) is v2-only; v3 uses
        g₃ = 10⁻¹³** (window midpoint: γ−1 ≈ 10⁻⁷, braiding ≤ 5×10⁻⁴).
    In this window α_B ≤ 10⁻³ everywhere, so the O(α_B) truncation above is
    self-consistently sufficient.

    Remaining v2/v3 debt: Earth/lab Vainshtein factor in the EP estimate
    (currently only the Sun's is applied; r_V,⊕ makes lab tests more suppressed,
    so the current check is conservative).
    NOTE: the S(φ) = φ²/(1+ζφ²) factor is *called* Vainshtein in the code but is
    an amplitude screen — with true Vainshtein now present, consider retiring it.
- The parameterized S_env(ρ) (`prtoe_environmental_screening_at_rho_kg_m3`,
  parameters σ, ρ₀, γ) is now **redundant with eq. (6)** and should be retired or
  re-derived; currently it still multiplies ξ_eff in G_eff.

## 4. Linear perturbations (scalar sector)

Field perturbation, conformal time (`perturbations.c:prtoe_perturbations_derivs`,
corrected 2026-07-03 — previously the stiffness bracket was in physical form,
inconsistent by a²):

$$ \delta\phi'' + \Big(2\mathcal{H} + \tfrac{F_\phi}{F}\phi'\Big)\delta\phi'
 + \Big(k^2 + a^2\big[m_{\rm eff}^2 + \beta_{k^2} + \tfrac{F_{\phi\phi}}{F}\dot\phi^2
 - 3\tfrac{F_\phi}{F}(\dot H + 2H^2)\big]\Big)\delta\phi = a^2 S \tag{7} $$

- **[DERIVE]** `prtoe_compute_meff2` (m_eff² including F-coupling and curvature terms)
  — derive from second variation of the action.
- **[DERIVE]** The metric source S: currently
  S = (F_φ/F)[3(Ḣ+2H²)(3Φ+2(Ψ−Φ)) + 6HΦ̇] (Newtonian) and an η-based synchronous
  analogue with an unexplained factor 5 — both flagged as needing derivation from the
  perturbed □φ = ... equation. **The factor `5.0 * eta_sync` in particular has no
  visible derivation.**
- **[DERIVE]** β_{k²} = −β_s φ R k²_phys/M_ew²: from which L_Q operator? Sign and
  screening 1/(1+φ²) need a source.

Einstein-sector coupling (`perturbations_einstein`): all metric constraints are
multiplied by G_eff = 1/F (`G_eff_metric`), and δF = F_φδφ enters ρ_plus_p_shear via
`prtoe_accumulate_delta_F_shear`. **[DERIVE]** For F(φ)R gravity the (0i), (ij)
equations get δF′, δF″ terms beyond a G_eff rescaling — the implemented
`prtoe_fill_delta_F_from_state` chain rule covers δF kinematics, but the full
perturbed Einstein tensor bookkeeping (which components get which δF terms) is the
biggest single **[DERIVE]** item. This is exactly what the hi_class cross-check tests.

## 5. Code dictionary

| Symbol | Meaning | Code |
|---|---|---|
| φ, φ′ | field, conformal derivative | `index_bg_phi_prtoe`, `index_bg_dphi_prtoe` |
| F, F_φ, F_φφ, F_φφφ | coupling and derivatives | `index_bg_F_prtoe` … `index_bg_F_phiphiphi_prtoe` |
| ρ_φ, p_φ | field density/pressure | `index_bg_rho_prtoe`, `index_bg_p_prtoe` |
| δφ, δφ′ | field perturbation | `index_pt_delta_prtoe`, `index_pt_ddelta_prtoe` |
| trans | covariant activation gate (redundant, §2.1) | `prtoe_covariant_trans` |
| ξ_eff(φ) | screened coupling | `get_xi_eff` |
| φ_eq(ρ) | chameleon equilibrium, eq. (6) | `prtoe_phi_at_matter_density_kg_m3` |
| G_eff/G | 1/F at environment | `prtoe_G_eff_over_G_at_environment` |
| m_eff² | δφ effective mass² (physical) | `prtoe_compute_meff2` |
| δF, δF′, δF″ | coupling perturbation | `prtoe_fill_delta_F_from_state` |
| ablation flag | trans → 1 diagnostic | `prtoe_ablate_gates` (input) |

## 6. Open items (priority order)

1. **[DERIVE]** Perturbed Einstein equations for F(φ)R — full δF bookkeeping (§4);
   validate against hi_class with G₄ = F/2κ₀.
2. **[DERIVE]** m_eff² and the metric source S (factor 5 in synchronous gauge!).
3. **[DERIVE]** Background KG factor bookkeeping (R/2 vs Ḣ+2H²) and exact Ḣ.
4. Remove gate machinery from the physics path (evidence in §2.1).
5. Retire or derive S_env(ρ) (§3).
6. Thin-shell factor in the Cassini bound (§3).
7. L_Q operators: derive each perturbation-level term or declare truncation (§1).
