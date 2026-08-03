# Exploratory

*Moved here 2026-07-28. Nothing was deleted, and nothing here is retracted.*

## Why these are in their own neighbourhood

These files were unlinked from the public shelf, not retired. The reason is uniform: an outside
reader arriving at the program should meet its testable core and its honesty record, not a census of
every domain the medium might touch. Breadth is what draws a dismissal before the falsifiable parts
get read, and that dismissal is unappealable in practice.

The test applied was: *does this file's central claim survive if the rest of the framework turns out
wrong?* Claims resting on textbook inputs or on process honesty pass. Claims resting on the model's
own unverified derivations do not — not because they are wrong, but because they cannot be assessed
by someone who has not already accepted the framework.

**Work continues here.** Several of these are active research fronts, and a file being in this
directory says nothing about whether its physics is being pursued. In particular the quantum group
(`PRTOE_quantum_trio`, `_entanglement`, `_superposition`, `_tunneling`) is an open line, not a closed
one.

## The state of the quantum group, stated plainly

Those four files currently describe standard decoherence in the medium's own vocabulary.
`PRTOE_quantum_trio` grades itself: *"grammar-level, zero new predictions of its own; its content is
the SEATING of three already-recorded results."* Every decoherence passage says the same thing —
"einselection, standard decoherence", "the existing mechanism, not a fourth door".

So as written they make no measurement, which is why they read as interpretation. The open question
that would change that was whether the medium induces decoherence of its own, beyond ordinary
environmental decoherence, at a rate set by its coherence length ξ = ħ/(m·c_s) and its temperature.

**That has now been computed** (`scripts/medium_induced_decoherence.py`, 2026-07-28). The answer is a
null, and the null is forced twice over by inputs already fixed elsewhere in the program.

*Which sector:* the ultralight **dark** condensate, not the vacuum. The vacuum's own critical
velocity is c — its excitations ride the light cone — which is the separate zero-drag certificate
behind inertia in `PRTOE_inertia.md`. Both sectors turn out to be non-decohering, for unrelated
reasons, and the two arguments should not be merged.

- **Landau criterion.** The medium's excitation branch is Bogoliubov, ω(q) = c_s·q·√(1+(qξ/2)²),
  which has no roton minimum, so the critical velocity is exactly the sound speed:
  v_c = c_s = √(3α)·c = 0.1479596 c = 44,357 km/s. Earth's motion through the CMB frame is 8.3×10⁻³ of
  that. Below v_c no final state conserves both energy and momentum, so the medium cannot acquire a
  which-path record at all. This is kinematics, not a small coupling.
- **Order-parameter rigidity.** ξ = 402 AU. The condensate cannot resolve a separation below that,
  and the rate carries (Δx/ξ)². A micron-scale superposition is suppressed by 2.8×10⁻⁴⁰ before any
  coupling constant is applied.

The two cover different regimes — Landau the steady state, rigidity the sudden case where a
superposition is created and closed faster than the medium can respond — so between them there is no
gap. Finite temperature does not open one: the thermal phonon wavelength λ_T = ħc_s/(k_BT) stays
above ξ throughout the range in which the medium remains condensed, reaching equality exactly at
T = μ/k_B = 5.7×10⁻¹⁸ K, which is where the condensate ends.

**What this costs.** The model is now forbidden from claiming credit for any anomalous decoherence
signal. If a tabletop experiment reports collapse beyond the environmental prediction, this medium
cannot be the cause, and the prohibition cannot be tuned away without giving up either α_c = 3α or
m = 2.24×10⁻²⁰ eV.

**Where the live physics went.** Upward in velocity. v_c = 0.148 c is low enough that every
relativistic particle is supercritical, so the medium's one open channel of this kind is Cherenkov
phonon emission by fast matter — and that, not tabletop interferometry, is where a bound on the
matter–medium coupling has to come from.

## Links: repaired 2026-07-28

The move broke markdown links in both directions. All of them have been rewritten:

- **62** references from files still in `docs/` now carry an `exploratory/` prefix
- **142** references inside these files now carry `../`
- **3** links to `scripts/` needed `../../` rather than `../`, since they got one level deeper
- **7** references from `working_logs/` were repaired separately

Both direction counts came in above the 58/125 estimated from the first survey, which had missed
reference-style definitions. Acceptance test: all **883** local markdown links under `docs/` were
resolved against the filesystem relative to their containing file. **Zero unresolved.**

## Contents

Thirty-six files, in five rough groups:

- **Coverage and genealogy** — `PHYSICS_DOMAINS`, `INTERACTION_ATLAS`, `interaction_map`,
  `science_subdomain_tree`, `sciences_inheritance`, `family_tree`, `thread_inheritance`,
  `the_great_chain`, `philosophy_the_auditor`, `math_story`, `intellectual_history`, `scale_ladder`,
  `THE_CHAIN`, `references`
- **Quantum foundations** — `quantum_trio`, `quantum_entanglement`, `quantum_superposition`,
  `quantum_tunneling`
- **Relativity and gravity framing** — `classical_gravity`, `special_relativity`, `inertia`,
  `wormholes`
- **Domain stubs and consolidations** — `plasma_physics`, `chaos_dynamics`, `astrochemistry`,
  `small_scale_structure`, `laser_physics`, `light`, `sqrt3_derivation`
- **Superseded lineage and historical eras** — `UV_completion`, `me_trigger`, `kappa_v_derivation`,
  `v4_dCDF_derivation`, `v4_dCDF_results`, `v5_five_verdict_derivation`, `fairbank_note_HOLD`

`PRTOE_light.md` is worth flagging individually: it carries the per-channel analysis showing that
the 56% hypercharge and 76.5% electromagnetic unsupplied shares are one debt read twice, which is
current and was written the same day this move happened.
