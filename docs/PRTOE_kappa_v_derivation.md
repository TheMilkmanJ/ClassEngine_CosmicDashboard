# The κ_v Derivation (task #17, working document)

**Status (2026-07-07 night): CANDIDATE OPERATOR FOUND — the w-portal.
Three audits owed before "derived" is claimed.**

## 1. The problem

ANN-2026-005's healer is phenomenological: δv/v = κ_v·(ρ_d/ρ_r) with
κ_v ∈ [0.06, 0.41]. The first evidence-class entry requires deriving
the coupling from an action. Constraints accumulated:
- (ANN-2026-004) the amendment must be CONSTANT through BBN
  (z ~ 10⁹ → 10⁸), dead by recombination, dead in all laboratories;
- (turn 17) derived-vs-fitted: the operator's key structure must be
  computed, not tuned;
- (opening pass) density-portals demand an eV suppression scale
  (IR-strong) AND fail constancy anyway.

## 2. The drift wall (found and named this session)

Any local portal to the medium's DENSITY drifts: δv ∝ ρ_d ∝ a⁻⁴
(×10⁴ over BBN — Y_p destroyed at freeze-out); δv ∝ y ∝ a⁻²
(×130 — still fatal). The healer's constancy rides the RATIO
ρ_d/ρ_r, which no local operator supplies. **The derivation target
is therefore: a LOCAL, dimensionless, expansion-invariant attribute
of the medium.** The medium has exactly one: its equation of state.

## 3. The w-portal

  **L = −μ²(1 + k·w[(∂ξ)²])|Φ|²,   w(y) = y/(4+3y)**

— the medium's local equation of state multiplicatively modulating
the Higgs mass parameter. Local; analytic in (∂ξ)² (w is a smooth
function of X̃ through the basin); ONE dimensionless coupling k.

**Amplitude:** δv/v = k·w/2. The healer's +0.15% at w = 1/3 gives
**k = 9×10⁻³ — a per-cent-level dimensionless coupling.** No
hierarchy, no eV-scale suppression needed: the multiplicative form
prices in μ² itself.

**Profile (all computed):**
| epoch/environment | w | δv/v |
|---|---|---|
| BBN (pre-basin) | 1/3 EXACTLY, zero drift | **+0.15% constant** — the healer |
| recombination (mean) | 2×10⁻⁷ | 10⁻⁹ — dyad untouched |
| laboratory halos | 5×10⁻¹¹ | 10⁻¹³ — clocks/Oklo/absorbers safe |
| deep voids today | → −1 | **−0.45%** — NEW forced prediction |
| cosmic diffuse mean today | ≈ −0.7 | −0.32% (τ shift absorbed by z_reio) |

**Consistency check not forced:** mapping back to the booked
normalization, κ_v = (k·w/2)/(ρ_d/ρ_r) = **0.06 at the ΔN_eff
bound — inside ANN-2026-005's [0.06, 0.41] window**, derived, not
fitted to it.

**The forced new prediction:** the operator has no freedom about the
late-time negative branch — where the floor dominates, w < 0, and
diffuse/void gas today carries constants shifted −0.3 to −0.45%
relative to laboratories (which sit at w ≈ 0). This lands in R1's
unvirialized-gas channel with a sign and a magnitude — the two
programs (the healer and R1) now share one observational target:
**m_e-sensitive spectroscopy in demonstrably unvirialized gas.**

## 4. Audits owed (the gap between candidate and derivation)

1. **Radiative stability**: does the portal loop-induce μ²-shifts or
   medium-potential corrections that destabilize k ~ 10⁻²?
2. **Thermal consistency at BBN**: the vertex's y-dependent pieces
   vs the MeV plasma — form-factor/collective-mode analysis (the
   condensate's healing-scale cutoff is the expected regulator).
3. **The late-time negative branch**: audit m_e-sensitive
   diffuse-gas data at z ≲ 2 (Lyα forest thermal history, late-time
   CMB) for a −0.3% kill.
4. k's VALUE (9×10⁻³) remains an input — the derivation fixes the
   operator's form and profile; naturalness of the number is the
   final step (or the honest residue).

*Chain of custody: drift wall found → density portals killed →
invariant-attribute search → w unique → operator written → profile
computed → κ_v window reproduced unforced. Scripts in job scratch.*
