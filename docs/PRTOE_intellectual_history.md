> **PROVENANCE NOTE (2026-07-12):** narrative history; for current state see PRTOE_INDEX.md.

# PRTOE: An Intellectual History

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


*How this model actually developed — the deaths, the resurrections, and what
each one taught. Written contemporaneously (2026-07-06), while the record is
git history rather than memory.*

## The guiding intuition (constant throughout)

Space is an environment that reacts to its inhabitants. The original image
was a trampoline: one fabric, stretched near mass, flat far from it. The
mature version is agricultural: what can grow is dictated by the
environment, and the environment is itself shaped by what grows in it —
co-determination, not one-way causation. Every version of PRTOE has been an
attempt to make that intuition mathematically honest, and every version has
been reshaped by what the data would and would not permit.

The intuition's most durable technical residue: **regime labels are
densities, not times.** A halo interior and a void at the same cosmic time
are in different regimes. This survived every rewrite from v1 to the
present.

## Pre-history: the pruning sequence (c. 2025, before any code)

The model began, more than a year before the first CLASS fork, as a single
sentence: **"mass, gravity, and density dictate spatial expansion."** It
worked, but not well — H0 trouble from the start. What followed was a
sequence of conceptual amputations, each one removing a term that turned
out to be redundant or derivative:

1. **Gravity removed** — on the realization that gravity is a *consequence*
   of matter interacting with space, not an independent input. (In the
   mature model this became: gravity is exactly GR, minimally coupled; all
   new physics lives in the inhabitants, never in the interaction rules.)
2. **Density removed** — on the realization that density is just another
   description of matter: "matter and more matter dictates expansion" says
   one thing twice. (Technically: what distinguishes inhabitants is their
   equation of state, not a separate density variable.)
3. **Matter alone remained** — then was placed *inside fluid space*: matter
   as a phase of a fluid medium rather than a separate substance sitting on
   a stage. This gave excellent S8 behavior and poor H0.
4. **The environmental breakthrough** — the realization that expansion is
   dictated not by matter alone but by **whichever entity dominates the
   environment at the time**. Radiation was the first addition and pulled
   the levers the wrong way; adding the N_eff degree of freedom made both
   radiation and N_eff move right; the couplings followed.

Each pruning step, made intuitively, corresponds to a recognized principle:
step 1 is minimal coupling; step 2 is the statement that w classifies
inhabitants; step 3 is unified dark fluid; step 4 is — literally — the
Friedmann equation's structure, in which each era's dominant species sets
the expansion law. The intuition arrived at the standard framework's
skeleton by deletion rather than by derivation, and then kept the one thing
the standard framework does not have: the insistence that the medium and
its inhabitants co-determine each other.

## v1–v3: The non-minimal coupling era (died completely)

The first formalization coupled a scalar field to curvature — F(φ)R — and
tried to buy H0 relief from the induced sound-horizon shift, with screening
machinery to survive solar-system tests. Four independent rescue mechanisms
were attempted and each failed *by direct calculation*, not by taste:
the trace-kick from φ=0, the ξ₁ sign flip, the λ sign flip, and negative
φ_ini — all provably sign-locked or ineffective. v3 was closed, completely.

What survived the fire: the R/3H² = Ω_m(z) trace-clock — originally an
energy-transfer gate, repurposed in v4 as the regime-label idea. **A dead
mechanism's bookkeeping became a living model's ontology.**

## v4: dCDF — and its three near-deaths

The pivot: abandon modified gravity entirely (gravity is exactly GR) and
put the new physics in the dark sector's internal dynamics — one barotropic
fluid unifying dark matter and dark energy as dense and dilute regimes of a
single medium. The direct formalization of the trampoline/farm.

**Near-death #1 — inherited at birth.** The Chaplygin-gas lineage carries a
known lethal defect: one parameter controls both "interesting" and
"unstable." The β two-parameter family (w = −exp[−(s+βs²)]) was constructed
specifically to decouple those — the model was born already dodging its
ancestor's cause of death.

**Near-death #2 — the contaminated year.** All early dCDF results were
unknowingly flattered by a thermodynamics hack (a dkappa opacity
modification) that masked a missing perturbation sector. When the tree was
cleaned (2026-07-05), the honest χ² was ~224,800 against ΛCDM's 583. The
model as-implemented was not slightly wrong; it was *absent*. The
perturbation sector was then actually built, and every pre-2026-07-05
number was declared void. **Lesson: a model does not exist until its
perturbations do.**

**Near-death #3 — the Chaplygin death mode arrives anyway.** First honest
runs showed σ8(z) *decaying* at late times and negative fσ8 — the classic
unified-dark-matter death. The rescue was not new physics but a
bookkeeping insight: galaxies trace the fluid's *clustering part*
(1+w)ρ, not its full density — the de Sitter floor is not matter
(dcdf_deltam_mode=1). BAO χ² went from 593 to 8.2 overnight. **Lesson: some
deaths are definitional, not dynamical.**

## v5: The amputation (2026-07-05)

The first honest MCMC drove β to its null limit and every nonzero β
destroyed σ8. β was deleted from the code entirely — not set to zero,
removed. The model collapsed to w = −ρ_∞/ρ exactly: a fluid whose
background *and* linear perturbations are provably identical to ΛCDM,
carrying one new parameter (ξ_Neff) and a reinterpretation of what dark
matter and dark energy are.

β was later given a formal resurrection hearing (2026-07-06) with every
advantage: partners pinned at their engaged optimum, and DES weak lensing —
the one dataset that *wants* what β sells — added to the stack. DES
rejected it harder than any other dataset (+30 at β=10⁻⁷). **Lesson: a
parameter the data pins to null with no working regime is model debt; and
verdicts should be retested when the jury changes.**

## v6 and the recombination: couplings survive their host

In parallel, a v6 scalar-field program explored environmental couplings —
the field responding to radiation density and ionization (c_γ, c_EM
sandbox knobs), and an N_eff sector (ξ). The scalar field host struggled;
**the couplings thrived**. The recombination — the user's key synthesis —
was to combine the two survivors: the v4/v5 fluid (a dead program's
resurrected core) as the body, the v6 coupling ideas as the layer above it.
This is the "triad": the unified fluid + ξ_Neff + a
constants/environment coupling. dCDF almost died permanently; the scalar
field almost died; the current model is the graft of what survived from
each.

## The pattern that emerged (2026-07-06)

Auditing how every known inhabitant couples to expansion revealed one rule
appearing four independent times: **transitions happen when the diluting
environment crosses one of the inhabitant's internal scales.** Neutrinos
(T crosses m_ν), the dCDF fluid (ρ crosses ρ_∞), the UV completion's basin
entry (u crosses X₀), early-dark-energy proposals (H crosses m). The
farming metaphor stated as physics: growth regimes change when the
environment passes thresholds set by what's growing in it.

The same audit produced the model's falsifiability spine: the completion's
entire tuning freedom reduced to one number (x₀ ≲ e⁻³⁵, set by BBN), and
the H0 mechanism's anatomy — the acoustic-scale ridge, the damping-tail
tax, and the recombination-timing lever (varying m_e) that evades the tax
where the radiation lever could not.

## Where the honest scoreboard stands (morning of 2026-07-06)

- On Planck+BAO+SN alone: dCDF beat ΛCDM by 19.2 in χ².
- ACT DR6 clawed essentially all of it back; the joint-stack refit landed
  at H0 = 69.05, ξ = 0.142 — *exactly* where the ridge analysis predicted
  it would — and the refit ΛCDM twin is converging to a statistical tie.
- The model's live claim is therefore: **equal fit quality across every
  dataset simultaneously, with H0 = 69.0 and S8 = 0.823 instead of
  ΛCDM's 67.4 / 0.833** — both tensions eased directionally, at zero χ²
  cost, for one extra parameter.
- The m_e coupling (the possible fourth graft) is under profile test as
  this document is written.

## For future readers

If this model survives, its history is the argument for a particular way
of doing theory: ideas were killed by calculation, not fashion; every
death was recorded rather than buried; the survivors were recombined
across program boundaries; and every rescue was required to produce a
number that could kill it again. If the model dies, the same record shows
exactly where and why — which is the only kind of death worth having.

*Primary sources: git history of this repository (the deep-clean and
amputation commits especially), docs/PRTOE_v4_dCDF_derivation.md (the v3
post-mortem and v4 birth), docs/PRTOE_v5_dCDF_complete.md (the current
model and its validation record), HANDOFF_FOR_GEMINI.md (the v3 closure),
and the session memory files.*

## Addendum (2026-07-06 afternoon): the nine-turn review

The model's hardest day was an adversarial review by a second AI
(ForClaude.txt), conducted as a turn-based file dialogue with
pre-registered bets and written concessions on both sides. Six attacks
opened it; nine turns closed it. In between: the unfalsifiability
pincer was broken on paper at the attacker's own chosen line, the
funded-floor mechanism was derived and then executed by the defender's
own computation of the attacker's question, xi_Neff was executed by
the data mid-review (the triad collapsing to a dyad), a prediction
market on the BBN-consistent fit embarrassed both parties each in one
leg, and the review's extracted qualifiers were promoted into the
document's headline with turn attributions preserved. The reviewer's
closing verdict: "a smaller, harder, more honest object than the one I
opened fire on." The method — the file, the bets, the attributions —
is as much a result of this project as any chi-squared.
