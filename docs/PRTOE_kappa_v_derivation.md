# The κ_v Derivation (task #17, working document)

> **DATE NOTE (2026-07-13 pass):** this file's header predates the derivation-hunt/freeze era; statuses herein may be superseded — current conditionality: [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


**Status (2026-07-07, post-turn-28): the honest triple, binding —
SHAPE-FORCED (class universality) / AMPLITUDE-INPUT (k_eff is chosen,
not derived) / WINDOW-CONSISTENT (0.06 lands inside ANN-2026-005's
window as a consistency, not a prediction). "Derived" may not
re-inflate; this header governs every summary of this document. The
void prediction is retracted (§3a); the surviving audits (radiative
stability, BBN form-factor, k-naturalness) can CLEAR the operator but
cannot make it distinctive.**

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

## 3a. THE THREE SEAMS (red-team turn 27) — closed, with one retraction

**Seam 1 — the single definition, and the values by substitution.**
The portal's w is the EXCITATION-SECTOR equation of state, one
analytic function of the single local invariant X̃ = (∂ξ)²:

  **g(X̃) ≡ (P+ρ∞)/(ρ−ρ∞) = (X̃−1)/(4+3(X̃−1))**

(ρ∞ = −P₀ are constants of the action, so g is local). Substitution,
one definition, three values: pre-basin y ≡ X̃−1 = 2.8×10⁷ at BBN ⇒
g = (1/3)(1−4/3y) = 1/3 to **5×10⁻⁸ — the drift across all of BBN is
O(1/y), five parts in 10⁸** (not piecewise: the transition is smooth
and analytic, compressed at basin entry z~10⁵ where nothing
m_e-sensitive exists); recombination y = 8.4×10⁻⁷ ⇒ g = 2.1×10⁻⁷;
labs y = 5×10⁻¹¹ ⇒ g = 1.3×10⁻¹¹.
**THE RETRACTION seam 1 forced:** the "void negative branch"
(δv → −0.45%) came from conflating g with the FULL-medium
w = −ρ∞/ρ (a different function, not the operator's). Under the true
operator, voids have y → 0 ⇒ g → 0: **no negative branch, no void
prediction, no late-time signal anywhere.** The forced-prediction
claim is withdrawn; R1's channel loses the κ_v companion. Cost paid
in full; the operator is correspondingly SAFER (g ∈ [0, 1/3] always,
dead everywhere post-basin).

**Seam 2 — uniqueness was the wrong claim; the right one is CLASS
UNIVERSALITY.** c_s²(X̃) = (X̃−1)/(3(X̃−1)+2) is indeed a second
dimensionless invariant with the same limits — because at the
two-derivative level EVERY local dimensionless scalar of one field is
an analytic function h(X̃). The honest statement: **any bounded h(X̃)
with h(1) = 0 produces the healer profile automatically** — constancy
pre-basin is forced by y → ∞ (every bounded h plateaus), death in
labs by y → 0. The shape is universal over the class; the class
collapses to ONE effective coupling k_eff = k·h(∞). Shape: forced.
Amplitude: input (as audit 4 already conceded). "Derived not fitted"
holds at class level, which is the level the ANN-2026-005 window
comparison tests.

**Seam 3 — the freeze-out number.** Notation clarified: the operator
is multiplicative in the BOUNDED g — there is no ⟨(∂ξ)²⟩ factor
(the note's shorthand "w[(∂ξ)²]" meant "function of," not "times").
δμ²/μ² = k·g ≤ k/3 = 3.0×10⁻³ ⇒ δv/v = 1.5×10⁻³ AT FREEZE-OUT AND
AT THE BOTTLENECK ALIKE (constant to 5×10⁻⁸). Its Y_p consequence is
not an open question — it is the vev package's own five-abundance
chain (ANN-2026-005, DSW rows incl. τ_n, Q_N, m_e): Y_p −0.68%, the
designed IMPROVEMENT. The constant offset at freeze-out is the
healer working, not the Drift Wall's failure returning.

## 4. Audits — RUN (2026-07-07 night); verdict two-sided

**Audits 1 (radiative stability) and 2 (BBN thermal) collapse to ONE
condition and the verdict is sharp both ways:**
- NAIVE point coupling (loop momenta to m_h): the Higgs loop feeds
  k·μ²·⟨|Φ|²⟩ ~ 7×10³⁹ eV⁴ into the medium's Lagrangian — 10³⁶ × M₂⁴:
  the basin is obliterated without a ~10⁻³⁶ tadpole tuning. **FAILS.**
- FORM-FACTOR-PROTECTED coupling (vertex soft above the condensate
  scale M₂ — the portal reads the COLLECTIVE density, and probes
  above the healing scale see no collective mode): the loop is
  m_h-suppressed, fractional medium correction = k/32π² = **2.8×10⁻⁵.
  PASSES.** The same softness simultaneously kills BBN-era
  medium–plasma thermalization (audit 2). One condition, two audits.
- Softness is NATURAL for condensate portals (standard collective-
  mode physics) but UNDERIVED here: it is a property of the §2
  completion. **The w-portal's radiative bill is therefore payable
  if and only if the completion delivers the form factor — the same
  single window every open item in this program queues at.**
- Audit 3: MOOT (void branch retracted). Audit 4: permanent residue
  (the honest triple's amplitude-input clause).

**Final status of task #17: the operator is written, local,
tree-natural, shape-forced, seam-closed, and radiatively viable
conditional on completion softness. Nothing further is derivable
this side of the §2 wall.**

## 4-old. Audits owed (superseded by the above)

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
