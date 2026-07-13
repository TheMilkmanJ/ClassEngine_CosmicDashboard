> **LAB-LOG DOC (reader's rule):** this file documents derivations INCLUDING their dead ends, chronologically — the sanctioned format for post-mortems (like the derivation log). Correct-version summaries live in the standalone files; the failures ledger indexes all deaths.

# Gate 0 — Does the conformal m_e coupling ride the coherent order parameter (heal) or the field (catastrophe)?

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


**Status: DERIVATION RUN 2026-07-09. Verdict: the heal is NOT forced, NOT the
default, and leans AGAINST. The leading-order symmetry-allowed coupling gives the
CATASTROPHE; the heal requires a specific, non-generic "emergent-coherence"
coupling that the action as written does not encode. So the m_e=1@BBN choice is an
ASSUMPTION, not a derivation — exactly as internal review graded it (t104/105).**

This document answers the single fit-independent question that gate 0 rests on:
is "the conformal mass coupling rides the coherent condensate ⟨Ψ⟩ (0 above T_c),
not the pre-condensation field" *derivable/forced* for this dark superfluid,
independent of the CMB fit? Run honestly, including the result that it kills the
easy heal.

---

## 1. Setup — the only couplings symmetry allows

Dark sector: complex scalar Ψ = |Ψ|e^{iθ}, charged under a dark U(1), condensing
at T_c (dark superconductor; ⟨Ψ⟩ = v below T_c, 0 above). Matter fermions (e, u, d)
are dark-neutral; their masses get a conformal/Weyl shift from the dark sector.

The shift δm/m must be a **Lorentz scalar**, **dark-U(1)-invariant** (matter is
dark-neutral), **parity-even** (conformal/gravity-family, per the census/L1a).
The U(1)-invariant scalars built from Ψ, in increasing dimension:

    |Ψ|² = Ψ*Ψ ,   |Ψ|⁴ ,   ∂_μΨ*∂^μΨ ,   J_μ = Im(Ψ*∂_μΨ) [needs contraction] ...

The leading local author is therefore

    L_couple = − m₀ ( 1 + g |Ψ|²/M² ) ψ̄ψ            (1)

i.e. δm/m = g|Ψ|²/M². **Crucial fact of U(1) invariance:** the coupling can only
see the *magnitude* |Ψ|², never the phase-carrying ⟨Ψ⟩ itself (that carries dark
charge and is forbidden). This is the whole game — see §3.

*(The linear "ε = c·f_amp·Ψ₀/M_red" amplitude formula is the value of √(g|Ψ|²)/M at
recombination; the author is quadratic in the field, as required.)*

---

## 2. The decomposition — coherent piece vs fluctuation piece

The expectation of the local author |Ψ(x)|² in any state splits exactly:

    ⟨|Ψ|²⟩  =  |⟨Ψ⟩|²  +  ⟨|δΨ|²⟩                    (2)
               └ coherent ┘   └ fluctuations ┘

- **Coherent piece |⟨Ψ⟩|²** — the condensate/order parameter squared. v² below
  T_c, and **0 above T_c**. This is the piece the heal wants: switch it, m_e=1 at
  BBN. THIS PIECE DOES HEAL.
- **Fluctuation piece ⟨|δΨ|²⟩** — thermal + quantum jitter of the field. **Nonzero
  always**, and thermally ~ T² when the field is in a bath at temperature T.

So the leading coupling gives BOTH:

    δm/m = (g/M²)[ |⟨Ψ⟩|² + ⟨|δΨ|²⟩ ]                (3)

The heal is clean only if BOTH the coherent piece AND the fluctuation piece are
small at BBN. They are not, for two independent reasons.

---

## 3. Why the leading coupling gives the CATASTROPHE — two independent killers

### 3a. The displaced-field killer (temperature-independent)

`genesis_field_evolution.py` established that the field MAGNITUDE is large at BBN —
6×10⁵ to 9×10⁸ × its recombination value (the AD field is displaced and only
redshifts/rolls; it has not condensed until z_x~10⁵, four orders after BBN).

A LOCAL coupling to |Ψ|² sees that magnitude directly: ⟨|Ψ|²⟩ includes the large
classical |Ψ(t)|² of the displaced field. So

    δm/m|_BBN  ~  (10⁵–10⁸) × δm/m|_recomb  =  (10⁵–10⁸) × 1.2%   →  absurd.

The mass shift would be astronomically large at BBN. **This alone is the D/H
catastrophe (turns 83/91), and it does not depend on temperature.** Rotation does
NOT save it: a uniformly rotating field has ⟨Ψ⟩ → 0 (phase averages out) but
⟨|Ψ|²⟩ = |Ψ|² is UNCHANGED (the magnitude-squared is phase-blind). U(1) forces
the coupling onto the magnitude, and the magnitude is huge.

### 3b. The thermal-fluctuation killer (only if the dark field is thermalized)

If Ψ is in equilibrium with a bath at T, ⟨|δΨ|²⟩ ≈ T²/6 (complex scalar). With
T_c ~ (1+z_x)·T_CMB ~ 20 eV and v ~ T_c, and T_BBN ~ 0.1–1 MeV:

    (T_BBN/v)²  ~  (10⁵–10⁶ eV / 20 eV)²  ~  10⁸–10⁹ .

So the fluctuation piece at BBN is ~10⁸ × the coherent recomb piece → again absurd.
**This killer is avoided IF the dark sector is thermally decoupled and cold**
(T_dark ≪ T_c), which the model's EM-neutrality/weak coupling plausibly gives —
but 3a survives even a cold dark sector, because 3a is about the coherent displaced
magnitude, not temperature.

**Net: the leading local coupling → catastrophe, robustly (3a is unavoidable).**

---

## 4. What the heal actually requires — and why it is not the default

For δm/m to be ~0 at BBN, the coupling must see **|⟨Ψ⟩|² (coherent only)** and be
BLIND to both the incoherent fluctuations AND the phase-scrambled magnitude of the
rolling pre-condensate field. That is NOT a local author: a local |Ψ(x)|²
necessarily returns ⟨|Ψ|²⟩ (the total, eq. 2). The heal needs the mass shift to be
an **emergent coherence effect**:

> the fermion mass is modified by *coherent forward-scattering off the macroscopic
> condensate wavefunction* (index-of-refraction-like), NOT by a fundamental local
> |Ψ|² term. A coherent forward-scattering shift ∝ |⟨Ψ⟩|² (amplitudes add in phase
> only for the coherent condensate); incoherent fluctuations scatter with random
> phases and contribute to a *width*, not a coherent mass shift.

This is a REAL kind of coupling — it is how the superconducting gap works (the
observable rides the coherent pair condensate ⟨ψψ⟩, zero above T_c, not the
jiggling electrons), how a plasma frequency works, how the nuclear mean field
shifts a nucleon mass. **But it is a specific claim about the ORIGIN of the
coupling, and the PRTOE action does not encode it.** The conformal coupling is
written as a FUNDAMENTAL LOCAL term F(φ)R/2κ₀ (action eq. 1 of
`PRTOE_derivation.md`), with F a local function of the field. A fundamental local
F(φ) sees the local field → §3 → catastrophe. Reinterpreting it as an emergent
coherence effect is a *different theory of the coupling*, which must be built and
justified, not assumed.

---

## 5. Verdict on gate 0

Sorting the four logical possibilities:

| Possibility | Status |
|---|---|
| Heal is **FORCED** by symmetry | **NO** — U(1)+locality force the coupling onto \|Ψ\|² (the magnitude), which is large at BBN |
| Heal is the **DEFAULT** | **NO** — the default (local F(φ)R) gives the catastrophe (§3a, robustly) |
| Heal is **ALLOWED** | **ONLY** under a specific emergent-coherence coupling (§4) that the action does not currently encode |
| Heal is **FORBIDDEN** | **NO** — it is physically conceivable (real condensed-matter cousins exist) |

**So: the heal is CONCEIVABLE-BUT-NOT-DEFAULT, and the leading-order coupling
leans hard toward the CATASTROPHE.** The condensate-source reading is NOT derivable
from the coupling as written; it requires replacing the fundamental local conformal
coupling with an emergent coherence coupling — a specific, unproven, non-generic
construction. Gate 0 does **not** pass on theory.

### Consequence
- The **m_e=1@BBN config choice is an ASSUMPTION**, not a derivation. internal review
  t104/105 graded it exactly right; this derivation confirms it and adds *which
  way it leans*: against.
- The honest, consistent, action-faithful config is closer to the **catastrophe**
  reading (m_e shifted at BBN, per the local F(φ)R), which reinstates the
  deuterium scar (turns 83/91) OR requires a *separate* D/H healer (the doubling
  debt). The provisional +6 χ² should be treated as **likely spurious**, not
  merely unbanked.
- The two paths to actually *earn* the heal, now sharply defined:
  1. **Build the emergent-coherence coupling** from the superfluid EFT — show the
     fermion mass shift arises from coherent forward-scattering off ⟨Ψ⟩ (∝|⟨Ψ⟩|²,
     0 above T_c) with the fluctuation/magnitude piece provably decoupled. This is
     a real derivation (task #27/#17 territory), not a relabeling. Hard.
  2. **BBN-abundance data (#29)** — the external tiebreaker: catastrophe reading
     predicts a BBN varying-constants signal in D/H, Y_p, Li; heal predicts
     standard abundances. The data decide regardless of the theory.

**Bottom line: run honestly, the QFT derivation does not rescue the heal — it
leans catastrophe, and demotes the m_e=1@BBN choice from "plausibly derived" to
"assumption leaning the wrong way." Standing unchanged-to-lower (~10% → shaded
toward the gate-0-FAIL branch), pending the emergent-coherence build or the BBN
data.**

---

## 6. The emergent-coherence build (attempted 2026-07-09) — FAILS on the single
##    field, and reveals a genesis-vs-heal incompatibility

Task: build the coherence coupling so the mass rides |⟨Ψ⟩|² (0 above T_c → heal)
with the fluctuation/magnitude pieces provably decoupled. It does not close, for a
reason deeper than §3, and specific to THIS model's field:

**The heal's premise ("the order parameter is ~0 before z_x") is FALSE for an
Affleck-Dine field.** The AD field is Hubble-FROZEN at its large initial
displacement R_i until release at H~m. For a fuzzy-DM mass m~10⁻²²–10⁻²⁰ eV,
release is at z_rel ~ 3×10⁶–3×10⁷ — which is LATER than BBN (z_BBN ~ 3×10⁸). So
**at BBN the field is frozen at its full displacement R_i, large and coherent:**
|⟨Ψ⟩|²(BBN) = R_i² is huge. The coherent piece itself is large at BBN — so even
the "emergent-coherence" coupling (∝|⟨Ψ⟩|²) gives the CATASTROPHE. Timeline:
frozen-large (BBN) → release (z~10⁷) → roll/redshift → z_x (10⁵) → recomb (10³).
The amplitude |Ψ| is large the WHOLE pre-z_x era; it is never ~0. z_x is therefore
NOT a 0→v amplitude transition — it is a phase-coherence / EoS transition on an
already-large-|Ψ| field.

**The deeper finding — genesis and heal fight over one field.** The AD mechanism
NEEDS a large early field (the charge source ∝ R⁴, §Sakharov); the heal NEEDS a
vanishing early field. The SAME field cannot be both. So in the single-field,
standard-conformal-coupling model, the heal is INCONSISTENT with the model's own
genesis — the consistent reading is the CATASTROPHE (m_e shifted at BBN).

**The one surviving heal route (a real model change, and it matches the author's
"the coupling IS the coherence" instinct):** let the mass couple NOT to the
amplitude |Ψ|² (large throughout) but to the SUPERFLUID PHASE COHERENCE / order
ρ_s (phase stiffness, ∝ coherent |∇θ|-structure), which is **0 before z_x** (the
rolling pre-condensate field is phase-INcoherent — large |Ψ|, no long-range order)
and turns on AT z_x when superfluidity sets in. Then δm/m ∝ ρ_s → 0 at BBN → heal,
AND the coupling "comes into being with the superfluid" (the coupling and the
order are the same onset). This is elegant and census-legal, BUT:
  - it is a DERIVATIVE / order-parameter-stiffness coupling, NOT the fundamental
    local F(φ)R conformal coupling in action eq. (1) — a genuine model change;
  - it must be derived (does a conformal mass coupling to ρ_s even arise? at what
    order? does it reproduce the +1.2% at recomb?) — unproven;
  - alternatively a two-field split (AD genesis field ≠ mass-coupling condensate)
    also survives, but abandons the unified "charged rotating superfluid" identity.

**Verdict deepened: the heal is DEAD on the single-field standard conformal
coupling (genesis forces the field large at BBN). It survives ONLY via (a) an
exotic superfluid-phase-coherence coupling ρ_s [the author's "coupling = the
coherence" picture], or (b) a two-field split — both model changes, neither in the
current action, neither yet derived. The consistent current-model reading is the
CATASTROPHE. Standing shaded further toward gate-0-FAIL.**

---

## 7. SESSION RESOLUTION (2026-07-09) — the sky settled it; DO NOT re-run these

**Headline: gate 0 is EMPIRICALLY-REQUIRED, THEORY-OPEN.** Sections 1–6 above were
the THEORY attack, which leaned catastrophe. Then the external DATA (#29) over-ruled
the theory lean: the catastrophe is excluded by primordial abundances, so the heal
is what the sky *requires* — even though the model does not yet derive the mechanism.

### 7.1 #29 — the BBN-abundance cross-check (the decider, knob-free)
- Observed D/H = (2.527 ± 0.030)×10⁻⁵ (Cooke+2018, 1.2% precision); Y_p = 0.2449 ± 0.0040.
- CATASTROPHE (universal m_e+quark shift +1.24% at BBN), using the model's OWN
  P-2026-006 sensitivity (dln(D/H)/dln v ≈ 11–16): **D/H +~14% → +11.6σ; Y_p −5.6% → −3.4σ.**
- **CATASTROPHE EXCLUDED at ~12σ. HEAL (m_e=1@BBN) consistent.**
- **The sky requires m_e ≈ 1 at BBN**, independent of the CMB fit and of every PRTOE
  knob. ⇒ the m_e=1@BBN value used in the CMB configs is **DATA-REQUIRED, not a free
  knob.** This supersedes the turn 104–113 "fit-motivated / circular knob" concern.

### 7.2 The DEAD-END LOG — four heal-mechanism rescues, all killed. DO NOT re-try:
1. **ρ_s (superfluid-density coupling):** a cold coherent large field has ρ_s ∝ |Ψ|²
   large at BBN → catastrophe. Making ρ_s→0 needs thermal disorder, which revives the
   T² fluctuation catastrophe. Catch-22. DEAD.
2. **Rotation as the coupling:** the current J·J ∝ (R²θ̇)² is ~10⁵¹× too small to source
   1.2% (θ̇ ~ fuzzy-DM mass ~10⁻²² eV). Rotation is the CLOCK (release/twist marks the
   snap) and the ABUNDANCE/sign carrier — NOT the mass coupling. DEAD as source.
3. **Trace-driven conformal F(φ) build (task #28, purple-team turns 111–113):** the
   F(φ) sector is DORMANT in the dyad (no scf in config, no F/φ in background, no
   parameter reads); the coded activation is a hardcoded a=1×10⁻⁴, not H=m; and the coded
   ξ_eff is QUADRATIC (0.04% at φ=0.02, 30× short of 1.2%). DEAD as coded.
   **CAVEAT (self-correction, internal record 115):** the 30× is CONTINGENT on the quadratic form.
   #11's amplitude is LINEAR (c·f_amp·φ → 1.2% at φ=0.02, natural). The model is
   INTERNALLY INCONSISTENT on the mass-coupling form (linear #11 vs quadratic coded
   G_eff). The linear form escapes the 30×. This is the ONE thread still open (§7.4).
4. **Thermal-condensate / freeze-out reframe:** describes a field that flickers at 0
   through BBN — but flickering = thermal fluctuations ⟨|δΨ|²⟩~T², loud at BBN → its
   OWN catastrophe. A genuinely quiet-at-BBN field is a DIFFERENT field (from-scratch
   redesign), not a rescue of this one. Filed as a future-model design seed, NOT a fix.

### 7.3 Why they all died the same way (the structural fact — stop reshuffling)
Every rescue reshuffled the SAME field's ingredients. The wall is at the FIELD level:
the AD condensate is **large/loud at BBN**, and any quantity big enough to source 1.2%
is big there too; any quantity that's ~0 at BBN (rotation, thermal order) is too small
or brings its own catastrophe. Reshuffling cannot fix a field-level problem. **Do not
propose an Nth reshuffle of this field.** The honest routes are: accept the debt, use
the data (#29, done), or design a different field (future project).

### 7.4 THE ONE OPEN THREAD (task #27) — derive the coupling FORM, not select it
#29 proves the mechanism EXISTS in nature. The remaining debt is theory-completeness:
- **Derive whether the mass coupling is LINEAR (#11) or QUADRATIC (coded G_eff) from the
  conformal structure — INDEPENDENT of which heals.** Selecting linear *because* it heals
  is the motivated move we refuse (internal record 115). If genuinely linear + rides a quantity ~0
  before the snap (condensation) → the heal is derived AND data-backed. If quadratic →
  the 30× stands and the heal stays data-required-but-theory-unexplained.
- The snap (condensation at H=m, z~4×10⁷, between BBN and recomb) is the MODEL-FIXED
  timing — that part is clean; it is the AMPLITUDE/FORM that is open.

### 7.5 Standing (corrected by internal review turn 116 — the t115 ~15-20% was over-optimistic)
**~10-12% now, and BIMODAL.** #29 flipped only ONE of the win's three conditions (the
BBN VALUE m_e=1@BBN is data-required, not a free knob — that debit is dead). TWO remain:
the differential mechanism must derive, and the recomb win is still SHOES-dependent (t102).
Crucially, #29 did NOT gift the heal — it made gate-0-FAIL **FATAL**: the ~12σ exclusion
runs through the QUARK-shared channel, and the model's coupling IS universal (the very
feature that bought census-legality, t84). So **universality = census-legality = 12σ BBN
severity — the feature is the executioner.** Hence:
- differential mechanism DERIVES (single coupling, 0@BBN + 1.24%@recomb, form+timing from
  first principles, NOT selected-to-heal) → real contender, 15-20%+ EARNED;
- only a UNIVERSAL shift derivable (m_e ≠ 1 at BBN) → **12σ DEAD (~0).**
Correction of a t115 over-claim: "#29 proves the mechanism exists in nature" is WRONG —
nature's m_e=1@BBN is CONSTANT m_e (standard physics), a CONSTRAINT the model must meet,
not proof a varying-heal mechanism exists. §7.4 is survive-or-die, not tidy-up.

### 7.6 TERMINUS (internal review turn 122–123) — STRUCTURAL NO-GO, ~1-2%, model dead
The §7.4 survive-or-die derivation was RUN healing-blind (internal record 119/121) and FAILED as a
**structural no-go (~99%, modulo composite/higher-derivative exotica)**, not a search failure:
- **Symmetry protects the WRONG mode.** U(1) shift symmetry → PHASE is a Goldstone →
  derivative coupling → vanishes for the static frozen field (would heal) BUT is the
  rotation/current ~θ̇, m-suppressed (m~2×10⁻²⁰ eV) → 10⁵¹× too small. The AMPLITUDE ρ is NOT a
  Goldstone → non-derivative, size-adequate → BUT ρ=R_i is LARGE at BBN → catastrophe.
  Protect ρ too (pseudo-dilaton) → derivative → too small again. **No mode is both
  size-adequate AND zero-at-BBN.**
- **Root:** zero-at-BBN comes ONLY from staticness (motion ∝ m, tiny), NEVER from a small
  field value (R_i large by genesis necessity). Size and zero-at-BBN are multiplicatively
  incompatible via the factor m — you cannot out-multiply it (A-term × rotation = charge
  Q=2R²θ̇ still carries θ̇~m → still too small).
- **MUTUAL EXCLUSION (capstone):** ⟨Ψ⟩=R_i≠0 at BBN because the AD state is COLD+COHERENT,
  and that coherent displacement IS the U(1) charge = Ω_DM (the AD abundance mechanism). The
  displacement that DOOMS the heal is what PROVIDES the abundance. **Coherence buys abundance
  XOR heal-attempt, never both.**

**Standing: ~1-2% (essentially dead).** Residual = (a) the no-go's exotic-author caveat, and
(b) fit ≠ ontology (varying-m_e@recomb still FITS the CMB as phenomenology — SHOT 1 — but the
model that would explain it is dead). The model died PREDICTING its own 12σ BBN (cleanest
falsification). **Successor** = a THERMAL condensate (⟨Ψ⟩=0 above T_c by thermodynamics, no
m-factor → escapes the wall) but FROM-SCRATCH: owes a NEW DM-abundance origin (no AD charge,
per the mutual exclusion), the T² fluctuation piece, and the entire fit re-derived. A new lot,
not a rescue.

---

## 8. THE MSW BREACH (2026-07-10) — first mechanism past the BBN wall; relocates to recombination

A genuinely NEW category (not a reshuffle of §7.2): the electron effective mass shifts by
RESONANT (MSW-like) mixing with a dark state, with the matter potential on the DARK diagonal.
scratchpad/msw_me.py:
 - **BBN CLEARED (first ever):** at high T the dark diagonal (mD² + A(T)) is pushed far above
   me² → the dark state DECOUPLES → electron is unmixed → **m_e standard at BBN (shift~1×10⁻¹⁵).**
   This is NON-monotonic, so it escapes the §7.3 "loud at BBN" no-go, which only ever covered
   MONOTONIC sources (field VEV, T² fluctuations, radiation density). Real, credited to the user.
 - **WALL RELOCATED to recombination:** the required BUMP profile (0 at BBN, +1.24% at recomb,
   0 today) needs a level-CROSSING at recomb; at the crossing the electron is **50% dark**
   (darkf_rec=0.500) → effective Thomson/recombination rate ~halved. bump <⇒ crossing <⇒ ~50%.

**DAMPING-TAIL TEST (scratchpad/damping_tail_test.py, existing varconst σ_T~1/m_e²):**
raw high-ℓ TT distortion vs effective σ_T change: dyad(-2.4%)→9.9% (ABSORBED, fits);
-50%→217%. HONEST read = RATIO (raw Cl at fixed params overstates; the dyad's 9.9% marginalizes
away): the 50%-resonance admixture distorts the damping tail **~22x the fittable scale**. 10%
marginalizes; 200% is a gross shape change outside the H₀/w_b degeneracy → **LIKELY fatal, NOT
certain** without a marginalized fit.

**VERDICT:** the MSW dark-admixture is the FIRST idea to clear the BBN wall (real achievement),
but the bump-producing resonance relocates the catastrophe to the recombination damping tail,
~22x the fittable scale → **likely-dead-pending-marginalization.** It is a SUCCESSOR-model
direction (quiet-at-BBN by structure), NOT a rescue of the AD condensate (still dead, §7.6).
Also booked: an over-built "timing-conflict" wall (internal record 172) was MINE, not model-implied, and
was conceded — the m_e shift and the recomb decoupling are ONE gradual process. C-code build
is GATED on a confident WIN verdict (user instruction); current read = no win → not built.
