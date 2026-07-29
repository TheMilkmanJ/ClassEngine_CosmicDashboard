# THE DOCKET — what every #N in this corpus refers to

*The corpus cites task numbers 542 times across 119 distinct numbers, in physics files, ledgers and
commit messages. The board those numbers live on is working machinery outside the repository, so
until this file existed none of those references resolved for anyone reading the repository itself.
This is the map. It is a pointer table, not a record: the reasoning behind a closure lives in
`_AUDIT_LEDGER.md`, the kills live in `PRTOE_FAILURES_LEDGER.md`, and the physics lives in its own
file.*

**Reading the statuses.** `closed` — the object is done and the files carry it. `open` — real work
outstanding. `running` — waiting on a chain, a sampler or an external referee rather than on desk
work. A number missing from this table (there is one, #41) was withdrawn before it carried content.

**This table does not govern every `#N` in the corpus, and one file in particular is not on it.**
[`PRTOE_honest_status.md`](../PRTOE_honest_status.md) predates this numbering and carries two schemes
of its own — the Q-series of the 2026-07-08 review (Q1/#19 … Q7/#25) and its own least-trusted-joints
list (#1, #3). Its "#21" is the kill-shot, not small-scale structure. Numbers on that page are scoped
to that page. Everywhere else in `docs/`, the numbers are this table's.

**A THIRD scheme exists and collides in the low numbers (carve-out extended 2026-07-27).** The
session BOARD's task numbers (#1–#39 and growing) appear in `scripts/` docstrings ("task #34" =
the BipoSH build, "task #15" = the amplitude identification, "task #36" = the low-h dice), in
`_RESIDUAL_DEBT_CENSUS.md` ("#32 the matched lensing fit" = this table's #161), in
`tilt_envelope_derivation.md`, and in `T2_smbh_atoms_owed.md`. Board numbers ≠ this table's
numbers: board #34 is not docket #34 (the Kelvin-weight session), board #15 is not docket #15
(the Threaded Physics debts). Any owed-vs-paid sweep that greps `#N` across `docs/` and
`scripts/` must resolve WHICH scheme each hit belongs to before joining — the failure mode is
silently cross-matching closed docket rows against live board tasks.

> **Carve-out extended again 2026-07-29, and the overlap is now total in the low numbers.** Three
> more files carry board numbers: `PRTOE_session_2026-07-29_findings.md`,
> `PRTOE_session_2026-07-29b_findings.md`, and `family_coupling_lagrangian_spec.md` (its C15 cites
> "#85"). The board has since grown to **#86**, so *every* board number now collides with an existing
> row here — board #85 is the delivery law, this table's #85 is the S₈ entropy-floor mapping; board
> #86 is the Koide contradiction, this table's #86 is unrelated. The earlier "#1–#39 and growing"
> bound no longer separates the schemes, and nothing except the containing file does. **Rule of
> thumb that still works:** the two dated session records, the family-coupling spec, the four files
> named above and everything in `scripts/` are board-numbered; every other file in `docs/` is
> this table's.

**One caution, from the reverse audit.** A task marked closed means its *object* closed, not that
every clause of a multi-part title landed — eleven of about a hundred and ten closures were graded
wrong on exactly that ambiguity (#29, #33, #51, #55, #59, #76, #78, #92, #93, #95, #143), and four
more could not be verified either way (#22, #24, #33, #68). Composite titles are where that failure
lives. Cite a number for what its file says, never for what its title promises.

## The board

| # | what it is | status |
|---|---|---|
| 1 | Cycle-map attractor verdict — is ε derivable via the first-genesis chain? | closed |
| 2 | The transfer integral (η's transmission) | closed |
| 3 | routeD + conv_desi chains: thaw posterior + DESI verdict vs pre-registration | running |
| 4 | Card 1: the localization clause, quantitative (Landau velocity-cert → E_b⁴ energy cap) | closed |
| 5 | P-028 void gap: vortex-network magnetogenesis | closed |
| 6 | Card 7: portal census-legality pass + M_E phenomenology | closed |
| 7 | Seesaw scan + derive v_L (Card 6) | closed |
| 8 | Jeans-thaw closeouts: DE-clustering price, exp-normalization O(1), perturbation flag | closed |
| 9 | C-code baseline integration | closed |
| 10 | One-draw resolution study (finer θ sampling + integrator robustness) | closed |
| 11 | Induced-G + area law: the QG frame's earn-it tests | closed |
| 12 | Derive c: the census-counting mechanism (N−1)/N | closed |
| 13 | The DISPERSION zon chain: α_c + the two-clock frame + the n-instrument | running |
| 14 | Step-debt audit: enumerate every coded step and ramp-audit it | closed |
| 15 | The Threaded Physics debts (`docs/threaded_physics_working/`) | closed |
| 16 | Portal re-pin: select among joint-solve solutions via AD-direct + seesaw duties | closed |
| 17 | Citation pass: external sources for audience-facing docs | closed |
| 18 | THE BASEMENT ROSTER | closed |
| 19 | Big-claim mining 1: the lithium problem (the windowed Li-7 row) | closed |
| 20 | Big-claim mining 2: baryogenesis (η = n × transmission) | closed |
| 21 | Big-claim mining 3: small-scale structure (core-cusp, missing satellites) | closed |
| 22 | Big-claim mining 4: the flavour puzzle | **verdict delivered** (DERIVATION_HUNT §9) — the count is derived, the mass ratios are staked on (A = √2, θ = 2/9) and gated, the mixing angles are constitutionally out of reach |
| 23 | Big-claim mining 5: strong-CP, the constitutional silence | closed |
| 24 | THE RAMP RE-GRADE: every [R]/null domain verdict re-audited for buried boundaries | closed — **unverified** |
| 26 | B2+B3: the A_s clearance pair (winding-gas C_V; k-integral O(1) audit) | closed |
| 27 | The ς appeal: real-SN-template synthetic photometry + the mass-step discriminants | closed |
| 28 | Light B-queue: B4 comb rehearsal, B5 μ calculator, the Mb citation firm-up | closed |
| 29 | The heavy queue: B1-comoving full, B6 BipoSH, B7 the turn, zon-grades-the-fudge | closed — **B1 and B6 did not land**; see #150, #151 |
| 30 | Full docs hygiene: math symbols + jargon purge | closed; **the field's official rename ran to completion 2026-07-28 and the two standing exceptions are ruled**. Every prose use of the retired house word outside the registries now reads either "the electron-coupled scalar" (the field) or "the model" (the older pair sense), classified one at a time — the two senses do not rename alike, and blind substitution was already caught corrupting an H₀ and a comparison against ΛCDM, neither of which a scalar field can own. **Exception 1, the registries** (`PRTOE_FAILURES_LEDGER.md`, `PRTOE_PREREGISTERED_PREDICTIONS.md`): their function is to record what was committed to or claimed on a stated date, so rewriting the words inside them destroys the record they exist to be — the readers'-guide decoder covers both senses for anyone reading them, and that is the intended reading path. **Exception 2, the symbol** `λ_dyad`: defined once in `MATH_SPINE` §4, carried in five further documents and in two scripts, and a subscript cannot take a multi-word noun phrase. Renaming it is symbol surgery across docs *and* code, not a terminology edit; it stays until a replacement subscript is chosen. Machine identifiers (chain runs, configs, script paths, link targets) were left throughout — renaming them would falsify true statements about what is on disk |
| 31 | Ramp audit of the prediction registry | closed |
| 32 | Failure-bin ramp re-run: every ledger kill audited for step-dependence | closed |
| 33 | The response-function session: one function, two limits, one locked ratio | closed — **unverified**, no home in the corpus |
| 34 | The Kelvin-weight session: the vortex sector's a₁ weight | closed |
| 35 | The coupling-geometry re-audit under the fourth fence | closed |
| 36 | The WHIM session: partial-ε line offsets in the warm-hot IGM | closed |
| 37 | The ramp-origin audit: f̄ from the roll-up, ⟨ε⟩(z), T_c precursors | closed |
| 38 | The ξ-derivation session: the founding coupling from the model's own sector | closed |
| 39 | The silent-lineage census: every silence mapped to its intermediate parent | closed |
| 40 | B1's sixth-ambush corrected-geometry sizing | closed |
| 42 | THE THERMAL PROGRAM | closed |
| 43 | THE GATED SHELF — items waiting on runs rather than on work | running |
| 44 | Derive f̄ = 2/π from the genesis winding | closed |
| 45 | Derive c = 9/10 from the census | closed |
| 46 | 2-loop RG-improved V_eff for T_c | closed |
| 47 | The dyad compositeness (Λ, g) from the medium | closed |
| 48 | The medium's strong pairing sector (source g_p) | closed |
| 49 | The quantum trio: entanglement, tunnelling, superposition | closed |
| 50 | The black-hole / singularity / mystery wing | closed |
| 51 | Audience-law scrub | closed — **mis-graded once**; see the ledger |
| 52 | Portal √σ_dark = m_e — the irreducible input | closed |
| 53 | Induced-G scalar coefficient — Visser Eq. 35 (P-045 ξ-independence) | closed |
| 54 | f̄ and α_c — the two running MCMC referees | running |
| 55 | A_s's count k | closed — **mis-graded once** |
| 56 | The spurion μ = 2.25 meV | closed |
| 57 | √N closing lineshape S(ω/T) → Γ₀ → Λ = 2.25 meV | closed |
| 58 | The E_b partial-wave fork — s-wave, data-selected | closed |
| 59 | Koide mass-sector symmetry: the democratic↔hierarchy fixed point | closed — **retired as a category error**; the ledger holds the kill |
| 60 | Dark SU(2): P-048 registered, ΔN_eff re-priced | closed |
| 61 | Koide diagonal: the two surviving selectors | closed |
| 62 | CW route 4: the fermionic threshold-matching constant | closed |
| 63 | λ_dyad ≈ 1.3×10⁻³⁸ (the bare quartic) | closed |
| 64 | The gate's obstruction functional + two-forms reconciliation | closed |
| 65 | The tenth-channel operator (m₁ = κ_m·ρ_inf¼) | closed |
| 66 | n_s modulation map | closed |
| 67 | The lattice note | closed |
| 68 | ChatGPT blind audition cross-check | closed — **unverified** |
| 69 | Route 5 for the exponent: the forced-sum door (½ + 1 = 3/2) | closed |
| 70 | The RMS-contact mechanism for the Koide blank | closed |
| 71 | Tenth-channel UV form above v_L | closed |
| 72 | Route 6 (the dimensional seam): the d/2 pinning | closed |
| 73 | Route 6 condition (i): the thermal gap condition + freeze clause | closed |
| 74 | THE KELVIN-VERTEX COMPUTATION | closed |
| 75 | Kelvin-vertex hardenings h1–h3 | closed |
| 76 | THE LAST PIN: R₀/R_v | closed — **mis-graded once** |
| 77 | THE RING-ON-RING TRIAL | closed |
| 78 | THE DEEP AUDIT — one file at a time (protocol in `_AUDIT_PROTOCOL.md`) | closed — **checks 12 and 13 never ran**; see #149 |
| 79 | THE KERNEL CHASE: f₁/f₀ = e^(−τ + i·2/9) from recorded structure | open |
| 80 | THE ROOF: census-scope legality of the direct coupling | closed |
| 81 | EP/screening remainder, items (i), (iii), (iv) | closed |
| 82 | The two-loop shooter redesign | closed — superseded, the programme closed as mooted |
| 83 | The λ/RG resummation for T_c's perturbative envelope | closed |
| 84 | The Majoron corners' Boltzmann pass | closed |
| 85 | The S₈ entropy-floor mapping | closed |
| 86 | α_c = 3α: the two owed field-theory pieces | closed |
| 87 | THE TURN (B7): how the DE era closes into contraction | closed |
| 88 | The gate seed exponent, unconditional | closed |
| 89 | The T1–T16 residual-debt census | closed |
| 90 | THE GATE'S ENERGY BOOKKEEPING | closed |
| 91 | λ tension check: derived 2×10⁻⁹¹ vs the black-hole core's ≳10⁻⁹⁰ | closed |
| 92 | THE AREA LAW FROM THE MEDIUM (closes the Page curve) | closed — **mis-graded once** |
| 93 | THE DARK-ENERGY O(1) COEFFICIENT (the partial Gibbs–Duhem object) | closed — **mis-graded**; the real object is #123 |
| 94 | T5: the cavity C_ℓ computation | closed |
| 95 | T14: the rectification link | closed — **mis-graded**; the rectification was never computed, see #147 and #154 |
| 96 | T10: the chiral gravitational-wave amplitude | closed — ON THE CARRIER ONLY (scope annotation 2026-07-27, the composite-title failure mode): the paid object is the vortex network's carrier amplitude (Ω_GW h² ≈ 3×10⁻¹⁸, structural null); the θ·R·R̃ COEFFICIENT stays parked (parked register row 17's ramped-family reopening; `PRTOE_gravitational_waves.md` carries it as the open computation) |
| 97 | The remaining thread residue (T1, T2, T4, T7, T9, T12, T13, quartet Z₄) | closed |
| 98 | THE GALACTIC-CENTRE BUDGET TEST — the soliton at parsec radii | closed |
| 99 | THE EVIDENCE RUN'S HORIZON — decide before it burns two months | closed (row synced 2026-07-27) — the decision was taken and executed 2026-07-20: the nested run ended after ~48 h without a first checkpoint (priced at 163 days/checkpoint on this hardware), archived to `chains/_archive_polychord_ended_20260720_0915/`, and the verdict rehomed to the Laplace-from-MCMC estimate (P-2026-044 amended; the live successor is #155) |
| 100 | BBN ξ-propagation error re-issued corpus-wide | closed |
| 101 | What enforces Var(√m) = mean² exactly — the Koide constraint's mechanism | open — no mechanism; the thermal route now closed **both** ways (sampled and deterministic), and the constraint restated as a vanishing Z₃-graded norm, which names the class |
| 102 | The Brannen phase — a source that carries Q, not just its value | open — no source; the lock's data corrected (δθ is **+**7.409×10⁻⁶) and restated as an m_τ prediction, with P-2026-051's scope narrowed to ≲1.4 ppm |
| 103 | The hierarchy problem: rehome the anchor after the basement rebuild | closed |
| 104 | Baryogenesis: the frozen-era transfer fraction | closed |
| 105 | The galactic-atoms exemption | closed |
| 106 | The low beginning — the uniqueness argument the arrow needs | closed |
| 107 | The area law's missing coefficient | closed |
| 108 | Derived vs adopted in `inflation_replacement` (graded MIXED) | closed |
| 109 | The coincidence problem — does it already qualify? | closed |
| 110 | The 11 files the coverage ledger wrongly called archives | closed |
| 111 | THE PBH DEUTERIUM ROUTE | closed |
| 112 | THE PAPER PROGRAM — Grok checklist deltas (`ForJustin/12`) | open |
| 113 | THE BASEMENT BUILD — the gate three files park debts against | open, scope corrected 2026-07-27: TWO surviving parked debts, not three — the attractive-channel debt was PAID 2026-07-19 (particle-hole forced, corroborated three ways; hierarchy §6's table reads three-of-three; audit ledger receipt). The survivors: the seat constant b (neutrino sector) and light's coupling closure at M_Pl (1/α_Y = 55.5 ≠ 0, the remaining 56%). The program file's own grading stands: the bulk is preon/GUT-class model-building, not desk computation; nothing is run-gated. Desk-scriptable sub-item: Part 3b's mass-spread solve over the fixed str[k₁] roster — **delivered, so the basement now has no desk-computable residue left.** Sweep note 2026-07-28: the program's own "Parts 3+" list and #130 name the SAME object twice — the basement's *equation of state, from which the response-function identity descends* IS #130's piece 1 (the two-channel Π at zero momentum, transverse and longitudinal exhibited as one function). The basement file already books it as "the object α_c's derivation owes". One debt, two homes; #130 piece 1 is therefore basement-blocked by construction and is not separately actionable. Also on the second parked debt: "the remaining 56%" is the *hypercharge* share; in the electromagnetic channel the identification actually uses, the unsupplied share is 76.5% (see #130) |
| 114 | The gap equation's KERNEL — specify the pairing interaction and solve it | closed |
| 115 | The family-field potential, the background M, and x_out | open, retitled per the corpus's own reduction (T6: "one missing object, three faces — the ring's centre, the graded-norm constraint, and the vortex scale; naming it as three debts overstated the count"). ADJUDICATED 2026-07-27: the x_out face is MOOT as a verdict object — its crossing curve belonged to the cascade-delivery chain the ring-on-ring trial executed 2026-07-18 (the R₀ = R_H addendum survives as an argued input for any successor deliverer, paying no live verdict; scope correction in T6's tail). The LIVE route is the lock arc: a = 3b (board task #1's object — carried since 2026-07-28 as the null's CLASSICAL statement only; the exact target is 2.9877b at the corpus's own ω₁, so no mechanism is graded on producing the integer), the occupancy lock (f₀² = Σ|f_i|² exact at N₀ = 1, owing one named condition: the two sectors must be frequency-degenerate when the quanta are counted, else the same three lines give 2^(−¼) not 1), ω₁ = (2/9)T_c = 39.36 keV verified but in contradiction with the unit-occupancy value ln2·T_c = 122.8 keV; residual L2 (the deposit argument for f₀²'s value) and the graded-norm mechanism (#101) remain the derivation-class core. **2026-07-28 — the RING'S CENTRE face is supplied.** The democratic construction (`koide_democratic_graph_null.py`) treats the condensate as one further node of the coupling graph, so each face carries a bond to it; that bond is a restoring force toward the reference amplitude and is exactly the term that locates M. Verified both ways: with it, ε_singlet = 1 (bound); without it, ε_singlet = **0 exactly** (flat). The same construction supplies the graded-norm constraint itself — f₀² = |f₁|²+|f₂|² at N = 3, uniquely, via (N−1)² = N+1 — so two of #115's three faces are answered by one object. Its premises reduce to **two independent claims**: structural (the condensate is a node whose couplings are fixed before it is pinned — which then *forces* the single coupling, since K₄ is edge-transitive; pin first and the residual S₃ gives two edge orbits and the equality reverts to an assumption the census's own NO-GO argues against) and dynamical (assembled medium-bond-first, splitting adiabatically — which is what "equal quanta" reduces to). The third face, x_out, was already adjudicated MOOT |
| 116 | The seat-alignment derivation | gated — the medium is identity-blind, so the **operator-level default is democratic** (μ_∅·𝟙, Σm_ν = 68.3); seat-alignment (61.4) cannot be written into the operator and must come from the settling dynamics (kubo freeze: the lightest is the last relativistic partner — an energy selection, blind-compatible). Gated on a flavor-resolved settling profile Φ_med(T) per species, inheriting the basement build |
| 117 | THE BOUNCE SECTOR | open — and it owns the first-principles winding integer n: a derived L_gen, hence a determined n beyond #180's n ≳ 1.65 bound, needs the bounce solved |
| 118 | The two-draws question (chain link 4→5) | closed (row synced 2026-07-27) — the titled object is SETTLED by the chain file's own record under #184's ruling: "the two draws are separate mechanism CLASSES, not two events competing for one epoch… one is an instant, the other a process" (the freeze branch is excluded by the tilt, n_s = 4 vs 0.9649). What survives is a different debt — the scaling mechanism holding ξ/ℓ_H across the CMB's decades — which is #168's re-typed residual, living in the census-scaling file's own open grade. NOTE (found by the same pass): the forward target carries two numbers a factor 15.6 apart — 3.45×10⁻³ (chain file, census-scaling file) vs the tilt file's computed revision 2.21×10⁻⁴ (the L*² factor) — adjudication in flight |
| 119 | The cold-spot orphan | closed |
| 120 | The regulator's entanglement-side O(1) check | closed — **structural**: the conical R-delta makes both coefficients one heat-kernel term, so any form factor cancels in the ratio (any p, not just p = 2). Successor open item, larger: the same identity does **not** extend past minimally coupled scalars to the model's actual roster |
| 121 | The genesis calc — exact Ψ₀ and f_amp | **substantially paid, and by an instrument that already exists** (row corrected 2026-07-28): `scripts/genesis_solver_B1.py` delivers both — Ψ₀ = 5.03×10¹⁶ GeV from the misalignment abundance closure (release at H = m, which returns this corpus's canonical onset 1 + z = 4.03×10⁷), and f_amp = 0.63 with band [0.19, 0.87]; its own findings log states neither is gated on a production run. That fixes the release hierarchy at h₀ = λΨ₀²/m² = 1.01. The dice grid (`lowh_dice.py`) brackets it: at h = 1.0, P(f_amp > 0.2) = 71–100% by tilt, medians 0.42–0.76, zero quiet draws. What "exact" still owes: the genesis-era dynamics proper (the pour → release map), which is the bounce sector's (#117) |
| 122 | Three owed-vs-completed conflicts adjudicated | closed |
| 123 | The Gibbs–Duhem mode-sum calculation — the DE value's un-built object | closed — a reframe. The DE value (w = −1, ρ_Λ¼ = 2.2599 meV) is carried by the condensation energy (Door A, ½α_c²M₂), which is frame-safe and needs no mode sum; cosmological_constant.md carries it. The mode sum cannot be the object: its renormalized residual is the LHY term (so it would inherit #169's control failure, λ = 26–46 against λ\* = 22.41), and a preferred-frame Goldstone sum returns w = +⅓, not −1. Reopens only if the SU(2) N_f = 3 lattice returns λ < λ\* AND a frame-compatible regulator is exhibited — a future gate, not a current owed object |
| 124 | The edge-convention audit | closed (row synced 2026-07-27; the physics files had recorded the 2026-07-20 conclusion — the arrow fell, not the convention — and the deciding arithmetic is now computed: `scripts/edge_convention_verdict.py` prices every admissible pairing of anchor convention (booked / exact-solution ×2) and band definition (two-term × O(λ) vs control-spread), minimum gap 3.6×, no overlap. Six propagation defects across the four verdict files fixed the same day (mixed ratio numerators, display-propagated 5.4×, stale 1–8 TeV carriers, present-tense audit language). STANDING CAVEAT: the shooter's 13–20 TeV has no recorded computation in the corpus — the verdict's anchor side is reproducible, its shooter side is a quoted number; recorded in the prereg entry and hierarchy §2(a) |
| 125 | Why the kinetic term rather than only the Weinberg operator | closed — **graded, adverse**. The title's fork does not exist: the Weinberg operator reaches no charged mass at any coefficient. The real roster is ordered by dimension, and the omission was **|Ψ|²H†H at dim 4**, the only renormalizable partner — excluded by D/H (λ_p ≲ 5×10⁻¹¹…1×10⁻⁹), and excluding it costs no tuning (induced λ_p ≤ 1.1×10⁻¹³). The standing lepton bilinear is **assumed**, narrowed by data and by nothing else; the finer fork (one coefficient via the doublet's normalization, δm_ν = 2δm_e, vs two) is **unreachable by any measurement** and the pipeline silently runs the correlated point |
| 126 | The gravity-routing step of the c-derivation | closed — **the step is withdrawn, not supplied**. No single criterion returns 9/10: blindness weights by energy over every field; charge weights by Σ N_c Q² = 8 and gives 8/9; charge carried all the way gives c = 1, which the census excludes. The ensemble confirms without adjudicating (8/9 sits 0.30σ from 9/10 at its width; σ_c ≤ 0.0115 would separate them). c = 9/10 stands as a counting assumption the data confirms. **Correction 2026-07-28 on the separating width only** (`scripts/c_census_discrimination_width.py`): 0.0115 is the 9/10-vs-8/9 *spacing*, so it delivers 0.97σ — the width at which the two stop coinciding, not one that excludes either. A 3σ call needs σ_c ≤ 0.0037: 10× in width, ~100× in sample. The withdrawal verdict and c's status are untouched; what changes is that the measurement route is far further off than "3.3×" implied |
| 127 | The C²-to-threshold map | closed |
| 128 | The BBN-stability fence, re-stated below its own anchor | closed — fence is [70, 500] keV structural; whole-range swing ≤ 0.32σ on D/H |
| 129 | The matched-junction interface — the velocity ladder's first payable step | closed — **negative**: the step is an identification, not a derivation. The impedance amplitude half is an identity for one medium (ρ_m = √(ρ₁ρ₂) automatic when ρ₁ = ρ₂ = ρ_m), and the geometric half (a matching section's length) is ill-posed for three co-located modes of one medium — no spatial junction to size. The ladder rewrites α_c = 3α (PREREGISTERED records c₂ = √α·c *without weight*), refereed by #130 piece 1; it carries no independent derivation and is not the desk-closable step it was docketed as |
| 130 | The base α's two owed pieces | **split 2026-07-28: piece 2 is CLOSED and propagated, piece 1 is basement-blocked.** Piece 2's replacement number is recomputed and now carried everywhere it was owed: the induced electromagnetic share is 23.45% (32.14 of 1/α_EM(0) = 137.036 above 1/α_EM(M_Pl) = 1/α₂ + 1/α_Y = 49.4 + 55.5 = 104.9), band 20.5–26.4% on the ±2 scheme spread, against the recorded 44% which is hypercharge read at M_Z — a **1.859×** overstatement of the quantity the identification uses (from the unrounded hypercharge inputs 42.9/98.4, which is what the harness has always guarded — the rounded 44% gives 1.876× and is the looser reading). It had been computed but propagated nowhere: `PRTOE_light.md`, the failures ledger's induced-gravity row and P-2026-040's roster condition all still carried 44%, and now carry both channels labelled. **The scale-dependence objection dissolves with it** — the corrected figure is an endpoint-to-endpoint fraction (M_Pl to q = 0), not a reading at a chosen scale, so a scale-independent α_c can be conditioned on it, which it could not be on the M_Z number. Piece 1 (the two-channel Π at zero momentum, transverse and longitudinal as one function with no relative O(1)) needs the medium's constituents and is therefore blocked behind #113/#146, not desk-doable; no posterior can substitute, because an identity between two response functions has no likelihood |
| 131 | The X₀ erasure reformulation | closed — the X₀-free canonical form in clock units ξ = φ/√(2X₀) (v5 five-verdict §2.1); two scales, M₂ and m̄₂, both landed; the atlas whisper carries the answer |
| 132 | Rebuild the docket index | closed — **this file**; see the note below |
| 133 | Which rung condensation picks | closed — the dyad's restoration temperature is κ-independent, so f cancels and the bracket is m_e; all three recorded readings sit inside the escape window, and the BBN fence [70, 500] keV binds tighter |
| 134 | The dark vortex-pair computation — F_dark/√σ's normalization band | **closed.** Normalization fixed (F ≡ √2 f_π, the 130.4-MeV branch; the "band" was one number twice). The 2.39× "internal disagreement" it uncovered is retired: the NJL route computes f/Λ_NJL, not f/√σ, and its own QCD anchor (Λ = 631 vs √σ = 440) refutes the identification by 1.42× — 1.42 of the 2.39 was a change of denominator, the rest the vortex route's own recorded √2-above-QCD. F_dark/√σ = 0.40–0.47 stands unopposed |
| 135 | The staged candidate tests — flesh out or retire | closed |
| 136 | The composite-Higgs exposure | closed — **withdrawn**; the Higgs here is elementary (hierarchy §2(c)) |
| 137 | The bend-over density of states — what N₀ is at the pairing shell | closed |
| 138 | What fixes k_F | closed |
| 139 | Rainbow truncation and equal-band DOS | closed |
| 140 | Particle-hole symmetry at the pairing shell | closed — **reversed** an earlier reading; r = v_e/v_h stays free |
| 141 | The vertex correction — the ≈2.7 dominating the anchor's band | closed (row synced 2026-07-27; the shelf had flagged this row stale) — crossed box computed: c = 0.789262, converged to 11 digits, GMB-validated; with #183's Fock companion a = 0.280677 (same sign, they add), 1/λ_eff = 1/λ + c + a → band 0.55–1.78 TeV |
| 142 | THE COUPLING'S SCALE | closed |
| 143 | PROPAGATION PASS | closed |
| 144 | At what scale α_c = 3α holds | closed |
| 145 | The coupling window between S and flavour | closed — mooted by #136's withdrawal |
| 146 | THE BASEMENT'S BAND STRUCTURE — supply or refute §6c's three conditions | **reduced to one** — TF screening is entailed by finite μ, λ = 0.03's condensation collapses into the two-band condition, r = 1 is supplied by the one-metric clause; the residue is a **species-selective chiral μ₅ on one node pair**. **2026-07-28 — the residue now carries a fence, and §6c's condition count drops by one.** b = Nα_c/(πv) depends on the species count and the band velocity only through N/v, so conditions 3 and 4 were never separable: the ask is the single relation **N = 2v**, and the "supplied" velocity condition earns its keep by holding the ratio still rather than by contributing a factor. The fence: the anchor holds within ×2 for N/v ∈ [1.82, 2.18] and within an order of magnitude for [1.45, 2.65], so ±9%; among integers N = 1 overshoots ×101 and N = 3 undershoots ×0.032, leaving N = 2 isolated, and at N = 2 the velocity has 8.4% of room. The degeneracy is not an escape — its far end (N = 4 needing v = 2) is fermions outrunning the gauge field whose speed defines the cone. Calibrated against §6c's own recorded 33.47, 1.58305, 0.618 and the v = 0.9 factor-two; script `basement_screening_fence.py`, 15 harness checks. **Same day, second pass — the pair is all but named.** N_screen is charge-WEIGHTED, not a count (§6g: α_c = 3α, the kernel is electromagnetism), so a doped cone is worth 2·N_c·q²: 2 for a charged lepton, 8/3 for an up-type, 2/3 for a down-type, 0 for a neutrino. N_screen = 2N₀ then has exactly **two** roster solutions — one charged lepton, or all three down-types — and the second breaks the 1/q² Goldstone kernel by adding gluon Debye screening. So condition (i) is no longer "two of forty-eight, unselected" but "the charged-lepton cone", with the electron named by the portal √σ_dark = m_e. μ₅ on one cone also *supplies* the 2-for-screening/1-for-pairing asymmetry and makes r = 1 automatic (the pockets are one cone's two halves). Still unsupplied: what puts μ₅ there. Also corrects the failed kill's arithmetic — the full roster charge-weighted is ΣQ² = **16**, not the counted 24, giving k = 0.73195 and an anchor at 2.7×10⁻¹³ rather than 2.9×10⁻¹⁸; verdict unchanged. Script `basement_species_selection.py`, 12 further checks. **Third pass, same day — that selection is PHASE-CONDITIONAL, and the shell is in the wrong phase for it.** Δ = 2Λ_shell·e^(−1/λ) puts Λ_shell = 5.4×10¹⁷ GeV, **15.3 orders above the electroweak scale**, where (a) the screened abelian charge is hypercharge, not electric — ΣY² = **10** over the roster, confirmed by the SM's own b_Y = ⅔ΣY² + ⅓Σ_scalar Y² = 41/6 — and (b) **no species is vector-like**: every LH field is an SU(2) doublet and every RH one a singlet, so no opposite-chirality pair shares a representation and **there is no Dirac cone for μ₅ to sit on at all**. So the charged-lepton result holds only if the medium screens in the broken phase; at §6c's own shell the mechanism has no object to act on. This is a **third horn of §6f's fork** and sharper than the two already there: §6f asks what value α takes 18 orders from its defining scale, this asks whether the kernel's referents exist there. Re-priced kill: counted 24 → k 0.61846 → 2.9×10⁻¹⁸; broken-phase 16 → 0.73195 → 2.7×10⁻¹³; unbroken-phase 10 → 0.86935 → 5.2×10⁻⁹. All destroy the anchor, verdict unchanged. Script `basement_phase_check.py`, 8 further checks. **Fourth pass, same day — the μ₅ residue is SUPPLIED, and it is not an independent unknown.** No μ₅ source is named anywhere in the corpus; a grep returns nothing. One is available from parts already owned. #125's operator is S·(L̄He_R)/Λ with S a total gauge singlet carrying no charge of its own, so S → e^{iθ}S has exactly one compensator in the operator: **e_R → e^{−iθ}e_R**, a right-handed-only rotation. A winding θ deposits μ_R = θ̇, μ_L = 0 — half vector, half axial. The vector half is a potential for a *gauged* charge and is Debye-screened by the medium's own neutrality; chirality is ungauged and survives. Net **μ₅ = θ̇/2 on the electron**, species-selective (the operator names it) and chiral (only e_R absorbs the phase). Both ingredients were already recorded in different rooms: the operator selection, and baryogenesis's own μ = θ̇. Magnitude at the one pinned epoch: θ̇ = m·(T_sph/T_on)³ = 59.7 eV, **μ₅ = 29.85 eV** (against ω_J ≈ 5.7 keV, ×191 larger — different objects, recorded so the scale is not mistaken). *(Corrected 2026-07-28: this row previously read θ̇ = 58.5 eV / μ₅ ≈ 29 eV, back-multiplied from the two-figure ratio 2.4×10⁶; the exact ratio is 2.450×10⁶ and the 2% gap was that truncation, not a g\* choice — `scripts/thetadot_two_percent.py`.)* **It inherits the same phase condition rather than escaping it:** a chiral chemical potential needs two opposite-chirality states in one representation, so in the unbroken phase the compensator dopes a chiral singlet with no partner. The μ₅ source and the charged-lepton selection therefore hold in the same phase and fail in the same phase, for one structural reason — **#146's open count drops from two to one, and the survivor is §6f's third horn.** Still unpriced: whether 29 eV is the doping the band structure needs, a comparison the recorded conditions do not permit since they fix doping through N_screen = 2N₀ rather than a stated μ₅. Script `basement_mu5_source.py`, 7 further checks |
| 147 | THE AD-DIRECT RECTIFICATION — T14's link 5 | closed — half one answered; half two rehomed to #154 |
| 148 | THE REVERSE AUDIT — every completed task against file closure | closed at 110/110 |
| 149 | THE DEEP AUDIT, checks 12 and 13 | open |
| 150 | B1 — THE GENESIS SOLVER | **built and delivering; only the production run is deferred** (row corrected 2026-07-28, the bare "open" was stale). `scripts/genesis_solver_B1.py` runs in 100 s and passes all four of its own validations — zero-mode roll, winding, ring-reduction, abundance. It returns Ψ₀ = 5.03×10¹⁶ GeV (abundance-fixed, ∝ m^−¼ at measured slope −0.250) and f_amp = 0.63 [0.19, 0.87], tiny-grid-converged. Its closure is now the corpus's authority for the release hierarchy h₀ = λΨ₀²/m² = 1.01, selected by reproducing the canonical onset 1 + z = 4.03×10⁷. What remains is `production()`, deferred — the solver's own banner says the absolute normalization is not production-gated, so the delivered numbers stand without it |
| 151 | B6 — THE BipoSH JOINT PIPELINE | **the estimator is built; the data application is the external item** (row corrected 2026-07-28, the bare "open" was stale). `scripts/biposh_estimator_pass.py` exists and was delivered 2026-07-28: cubic selection emerges from the projection (103/103 components), the template tower is the cubic L = 4, 8, 12 sequence, and the grading refines 1.4 → 1.68 with the excess identified as the m-dependent diagonal anisotropy. Its own gate, #160's low-ℓ regeneration, was lifted 2026-07-20 (`torus_lowell_pattern.py`, 90% retention). What remains is applying it to pattern-frame a_ℓm — a calendar item, not desk work |
| 152 | THE GRADE CONCORDANCE | closed |
| 153 | THE RETIREMENT CROSS-CHECK | closed |
| 154 | THE JOINT GENESIS DRAW — winding and rotation on one trajectory | closed (row synced 2026-07-27; the run landed 2026-07-20) — verdict NEGATIVE and decisive: `scripts/genesis_joint_draw.py` finds sign(θ̇) and sign(n) drawn INDEPENDENTLY (joint correlation −0.06 to +0.09 against a ±0.13 noise floor) — "sign(θ̇·n) is not a quantity the model signs; it is a coin it cannot call" (T14_link5_joint_draw.md). The cross-messenger lock is withdrawn in the failures ledger; the seeding-side claim sign(helicity_B) = sign(H_kin) survives on its own terms |
| 155 | THE SAMPLER'S PROPOSAL — why chains accept 97% and never move | open — routeD/conv_desi relaunched on a seeded covariance; acceptance fixed (0.99 → 0.25–0.31), convergence unproven; dyad_mnu's ±1.00 degeneracy is the live hypothesis |
| 156 | THE λ-QUENCH RE-DERIVATION — the superradiance shield | closed — **adverse**: computed at the recorded λ and m, the margin is −85 decades; there is no shield and the model meets P-034 as a free scalar |
| 157 | The D/H error budget — one ruling, four homes | **closed 2026-07-21 against the model** — arXiv:2011.11320 post-LUNA ±0.037 already includes d(p,γ)³He; three-term double-counts LUNA. Standing width ±0.0476, standing row **−2.94σ**. Kill in FAILURES_LEDGER; deuterium row §1 + harness re-pinned; ForJustin/10 settled |
| 158 | Link 4's sign convention | reduced — H_B = k²H_kin, coefficient squared, so no convention survives; what is owed is sign(H_kin). **Determined 2026-07-20: the recorded genesis cannot supply it** (story-grade banner, no rotation sense on record, the computing script not retained). Helicity is bilinear, so what is owed is one bit — whether the roll-up's poloidal sense is genesis-fixed or drawn — and the instrument is **#150 (B1, the only build with a velocity field), not #154**. Exposed: P-2026-057 declares one link fewer than it uses |
| 159 | The cross-sector sign lock | closed — registered P-2026-057 |
| 160 | Regenerate the low-ℓ pattern on a retained script | closed (row synced 2026-07-27; the regeneration ran 2026-07-20) — `scripts/torus_lowell_pattern.py`, retained: 90% retention, S/N 0.16, off-diagonal 1.4 (T5's table; booked in `_CANONICAL_VALUES.md` under this docket's number). The #151 gate is lifted |
| 161 | The matched lensing-likelihood fit | open |
| 162 | The web-dissipation ramp — the f_arr razor | closed — dead stub; the razor was dissolved two minutes after it was raised |
| 163 | The ring-BEC literature search | closed — no; ⟨|cos|⟩ over a wound ring is an identity, not a measurement |
| 164 | The haloscope null's edge cases | closed — both named corners strengthen the bound; the null is stated against the weak end |
| 165 | The synchrotron row's weight convention | closed — number was fixed-field, label said fixed-energy |
| 166 | The competitor comparison — steelman the H₀ market | closed — built, and caught a miscitation; EDE outscores this class on every column |
| 167 | The timing error band | closed — and the occupancy was mixing two clocks: 1-in-37, not 1-in-29 |
| 168 | The count C — mechanize A_s's shot-noise normalization | closed (row synced 2026-07-27; the count was mechanized 2026-07-28 by the amplitude promotion) — occupancy-one at the marginal scale, data-locked N = 1.003 ± 0.005 through the amplitude's cube (`scripts/occupancy_one_exhibit.py`; spine §23.5; hunt §8). The re-typing this row carried stands: k_*ξ is a scaling ratio, not a freeze-out (#184's ruling); the scaling mechanism's value/medium-derivation lives on in the census-scaling file's own open grade |
| 169 | The g→λ map | closed — λ = 26–46, whole band above λ* = 22.41, so uncontrolled at this order |
| 170 | M7's remaining half — f_wind | closed — 255× under the fence; the comb's detection claim dies, its location survives |
| 171 | Resolve the four unverifiable closures | closed — three traced to one commit that deleted 8,635 lines claiming to preserve every live finding |
| 172 | Build the retirement→task join | closed — mechanized as a commit-gate check |
| 173 | The R1 caustic-bit two-field sims | **re-typed 2026-07-27 — the precision test this row was gating is DISCHARGED BY THEOREM, not owed to simulation.** The plateau universality is analytic: for developed speckle Θ = Q/(Q+K) is Beta(d/2, d/2)-distributed, mean exactly ½, independent of spectrum, σ_v, density, epoch, dimension and anisotropy (the earlier 0.46–0.50 "spread" was a finite-developedness artefact). What the sweep still adds is a direct central-limit confirmation of the many-cell narrowing (~6×10⁸ cells) — a confirmation, not a gate — and it is MACHINE-gated: the precision log says run it only when the MCMC chains are off the box. **The genuine standing debt is different: the non-polynomial coupling's UV story.** Two structural conditions carry the result and are where any residual kill now lives: the coupling must respond to a many-cell average (a realistic absorber column, ~10⁹ cells, clears 10⁻⁵ with orders of margin; a pointwise coupling is excluded by the O(1) Beta variance), and measured environments must be deep-developed rather than soliton-core or laminar |
| 174 | The Z₄ tilt's forced status | closed — booked as INPUT; Ψ³Ψ* is parity-EVEN, so the forcedness argument fails on its own algebra |
| 175 | P-2026-043's RECFAST-class thermal-history run | closed (row synced 2026-07-27 — stale against the prereg registry's own annotation): the run was made; trough depth ≈ 1.0% (not the estimate's 4.6%), the SIGN — the registered content — holds; the decision rule is a sign test |
| 176 | Pre-register the P-018 XOR Route-D branch | closed — registered P-2026-056, pre-hoc; guard 2 discharges adverse |
| 177 | The ln 2 seam | closed — the BCS gap prefactor moved between prefactor and cutoff; not a seam |
| 178 | The weak sector's substrate coupling | closed — structurally void, with its falsifier recorded |
| 179 | Recover the content 0315894d dropped | closed — five live objects rehomed; caught a frozen mislabel (a₀ at 140 kpc not 83; gas-vs-stars ≈3% not ×1.98) |
| 180 | The winding integer n_rms | closed by adjudication — n ≳ 1.65 at the torus floor (L ≥ 27.6 Gpc, ξ_K = 256 Mpc); the registry's n ~ 10–30 needs L 37–330× the floor and forfeits the banked low-ℓ signature, so the honest reading is the bound, carried by the_great_chain.md and baryogenesis.md. A first-principles n — a derived L_gen — is genuinely owed but blocked on the bounce, and is carried under #117 |
| 182 | The BBN ramp keys on the other sector's scale | **determined — two objects, and the numerical safety claim fails too.** ε is the dyad's order parameter but the ramp keys on 177.10 keV, which DERIVATION_HUNT §6 assigns to the confining sector. The dyad's own exact-kernel band is **307–714 keV** (the recorded 250–530 keV does not follow from L−1 ∈ [1, 10]), which **excludes** the keying value by 1.73× at its bottom — so they are not one object. And 53% of that band lies above the BBN fence's 500 keV, where the ≤ 0.32σ whole-fence bound does not apply. **RESOLVED (2026-07-27, computed):** the re-key grid ran through the production splice (ε = 1.2543%, T_c ∈ {307, 500, 714} keV vs the booked 179): ΔY_p = +0.50σ / +0.96σ / +1.37σ and ΔD/H up to +0.79σ against the booked configuration (N_eff untouched — the ramp's consistency check). **The dyad-keyed ramp fails the 0.32σ fence at its own band's BOTTOM and worsens monotonically**; above 500 keV, where only raw σ binds, the shifts are σ-class, not safe-by-default. The two-object reading is enforced by BBN itself: the ramp's key stays the confining sector's ~177 keV, and the dyad's kernel band keys nothing in BBN. Dead half ledgered per the fork rule |
| 183 | The Fock self-energy insertion, the crossed box's companion | **closed — and it does NOT cancel the vertex term.** V is instantaneous, so Σ is frequency-independent and Z = 1; the effect is a velocity renormalization whose integrand is pointwise positive on the Fermi sea. Closed form a = (1+2b)/2 − 1/ln(1+1/b) = **0.280677**, same sign as c, so 1/λ_eff = 1/λ + c + a. Band 0.73–2.4 → **0.55–1.78 TeV**; **#124 reinforced, not re-opened** |
| 184 | The A_s collision — freeze-out census vs scale-invariant shot | **closed (ruled).** The model asserts the **scaling** picture; the freeze branch is *excluded by the tilt* (n_s = 4 vs 0.9649), and #168's retirement of the Kibble–Zurek *label* left its *structure* standing in THE_CHAIN. #168 over-priced the cost — the pivot-evaluated C decomposition survives. **Third finding:** the scaling class is asserted and assumed, never exhibited, and the "census-drift" tilt reading is an identity, not a second mechanism. ν = 2/3 found in `scripts/`, correcting a recorded absence |

## Why this file is thin on purpose

It resolves references and nothing else. A docket that restates each task's findings would become a
second corpus needing its own propagation, and the corpus already has a propagation problem — three
of the eleven mis-grades above were retractions that never reached the files inheriting them. The
statuses here will drift; the files will not, because they carry the claims. **When this table and a
physics file disagree, the file is right.**
