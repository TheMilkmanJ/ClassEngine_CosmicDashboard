# PRTOE — THE MATH SPINE (genesis → now → end)

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


*2026-07-10. The full quantitative chain in one document: every epoch, its governing equation,
what is DERIVED vs INPUT vs STORY, and where it lives in the code. Cross-references:
PRTOE_me_mechanism_math.md (dyad detail), PRTOE_cyclic_torus_genesis.md (genesis narrative),
PRTOE_UV_completion.md (docketed), PRTOE_cosmological_constant.md (J1).*

**Status tags:** [DERIVED] falls out of prior pieces · [INPUT] boundary datum · [STORY] coherent
mechanism, not a derivation · [PENDING] computation named, not run.

---

## 0\. The objects

One dark superfluid, two components (the two-field split):

* **Field 1** — the dcdf fluid: charge/abundance carrier, DM+DE unified. Mass m = 2.24×10⁻²⁰ eV
[**MEASURED** — the onset clock: the production fit's coded z_rad_onset, independently confirmed
by the blind free-z_on optimizer landing 7.5517 (→ m = 2.29×10⁻²⁰, 2% above the coded pin).
The former "derived from ε via c(m) = (m/m₀)^{1/4} at c = 1" was a relic of the SUPERSEDED
f_amp decomposition — in the standing decomposition ε = c·f̄·α_c the mass never touches the
census c, so **no roster-trial re-pricing propagates to m, z_on, or the hinge through this
route** (the hinge keeps only its α_c conditionality via c_s = √α_c). And read backward, the
old curve is dead by its own arithmetic: it would force c = 1.005 while the census excludes
c = 1. Provenance walk, hunt entries 145/148].
* **Field 2** — the dyad field: charge-free, couples to the electron; its condensate sources
δm_e. (The Majoron/lepton-sector identity: tree coupling σNN → neutrinos; the charged-lepton
portal is a UV assumption [PENDING #30].)

The amplitude — the model's one distinctive number — assembled from three factors, each graded by a
running instrument:

> **ε = c·f̄·α_c = 27α/5π = 1.2543%** (concordance joint 1.2403 ± 0.0079%), with
> - **c = 9/10** — a counting fraction (N−1)/N over the universal charged-fermion roster: 9 charged
> species plus the vacuum's own seat. The neutrinos sit on the seat rather than in the count, because
> their mass is medium-sourced rather than electroweak; the running α_c chain is the independent check;
> - **f̄ = 2/π** — the winding time-average, the mean-absolute-sinusoid ⟨|cos|⟩, forced by the
> winding's many-turn equidistribution (the coupling form the one remaining piece);
> - **α_c = 3α = d·α** — the condensate coupling, the 3 being the spatial dimension d (second sound,
> geometry, and the induced loop-trace agree); the value a bet graded by the α_c MCMC.

## 1\. Genesis (the cycle's start) [STORY]

Torus topology survives the bounce (topology holds what dynamics loses); the confined heat
fountain (blueshifted crunch radiation) rolls up into a helical vortex ring → re-seeds the twist.
Flat 3-torus registered as P-2026-013. **BKL and Tolman stand against the bounce rungs — this
layer is a story built from real mechanisms, not a derivation.**

## 2\. Radiation youth → dark matter (the first transition) [DERIVED identity]

Above H ≈ m the ultralight field is frozen/radiation-like (w=1/3, the conformal-origin
phase); below, it oscillates as dust. The switch epoch:

> **T(H=m) = √(m·M_red / 0.61) = 9.41 keV** (g*=3.36) ↔ **coded z_rad_onset = 4×10⁷ → T = 9.39 keV.**

Match 1.002×. The onset is field 1's H=m clock — textbook ULDM — NOT a condensation temperature
(the apparent internal inconsistency dissolved, booked both columns). Code: `dcdf_z_rad_onset`
(background.h, with the derived-identity comment).

**Two jobs, one clock** (author, 2026-07-10): the ending regime reaches its floor (conformal
protection ends) while the starting regime crosses its threshold (dust/DM behavior begins). In
code this is literally one function: `dcdf_rho_rad`'s f(a) = x²/(1+x²) fades the radiation while
the dust part continues, amplitude fixed by continuity (no free knob).

## 3\. The background fluid (radiation → dust → de Sitter) [DERIVED form; ρ_inf INPUT]

> **w(ρ) = −e^{−s}, s = ln(ρ/ρ_inf) clamped ≥ 0 ⟹ P = −ρ_inf exactly.**

So the background is ΛCDM-form: ρ = ρ_inf + C·a⁻³, algebraically (verified to 10⁻¹⁶).
w = −1 is EXACT for the constant floor — not a step artifact, not rampable. Code: `w_dcdf` /
`dcdf_s_of_rho` (background.h).

## 4\. The dyad turn-on (field 2 condenses) [DERIVED onset; clearance CLEARS]

The electron Coleman–Weinberg backreaction on the charge-free field (m_e(φ) = m_e0(1+κφ²)):

> V_CW = −(1/16π²)·m_e(φ)⁴·[ln(m_e(φ)²/μ²) − 3/2] → tachyonic curvature → radiative SSB
> **VEV: v = m_e0·[ε(L−1)/4π²]^{1/4} ≈ 100 keV** (81/102/121 keV for L−1 = 2/5/10; ±25%, robust)
> **T_c = m_e0·√(3(L−1)/2π²)** — κ cancels; log-ambiguous **\~40–450 keV** (NOTE 2026-07-14: the entry-149 re-audit's independent sweep gives [140, 900] keV — the two honest bands disagree at both edges; the union [40, 900] is the defensible envelope until the RG resummation lands; the adopted value is now T_c ≈ 179 keV (the non-perturbative confining chiral ratio), with this perturbative 193 keV a log-ambiguous cross-check inside every version; leading-log unstable
> near the flat direction; RG resummation = the working docket).

The onset is DERIVED from m_e0 + ε alone (the first gate-0 reduction, recorded).

**BBN clearance [CLEARS — the double regime-citation correction]:** the deuterium constraint's
severity decomposes by process: weak rates n↔p (T \~ 500–1500 keV, \~75% of the m_e lever),
n-decay phase space (\~10%), e± heating (\~10%), the bottleneck itself (\~5%, B_d nuclear,
m_e-insensitive). The dyad (T_c ≤ 445 keV) NEVER touches the weak-rate window; AND the dyad is
LEPTONIC (quarks \~2-loop, \~10⁻⁹), whose full-BBN ceiling is \~0.3–1σ, not the universal/
hadronic 12σ:

> **effective tension = (temporal exposure 0.05–0.25) × (leptonic 0.3–1σ) ≈ 0.02–0.25σ → QUIET.**

"When D forms" ≠ "when m_e matters" — two different electron-scale clocks. Code: the dyad window
`varconst_transition_redshift < z < varconst_z_high` (`varying_z_high`, new 2026-07-10; ≤0
recovers the plain step). #40 (RG V_eff + BBN network) CONFIRMS, not decides.

## 5\. Recombination → today [the fitted era]

m_e shifted by ε = 1.24% inside the window (H₀ fix; ΔlnZ = +2.635 Laplace, SHOES-conditional);
screening returns m_e → standard below z ≈ 50 [INPUT form, densities-dependent screening owed].
Optional rotation-shed `dcdf_conv_g` (S₈: minimizer picks g = 0.12, S₈ = 0.821 vs KiDS 0.814).
Corrected A2: the shed's apparent-w mirage is \~1% — OUT as a DESI driver; the S₈ job
survives (background ρ_m, not the w-mirage).

## 6\. The neutrino home [relation DERIVED-candidate; value INPUT]

Ψ = Majoron (L-breaking Goldstone): tree coupling σNN → Majorana m_ν → **0νββ must occur**
(P-2026-020); **Σm_ν ≈ 61 meV, normal ordering** (P-2026-012; whisper won the pre-registered
collision vs P-2026-004, which is FALSIFIED, ANN-2026-021). The tie:

> **ρ_inf¼ = m_ν,lightest = 2.25 meV** — a single lepton-number-breaking scale μ sets both the
> dark-energy floor (ρ_inf ∝ μ⁴) and the lightest neutrino mass (m_ν = μ). The tie is exact to a few
> percent, and it is AZK-safe: the neutrino mass comes from the frozen radial VEV, not from a coupling to
> the neutrino density (which would be unstable).

The scale μ is a dimension-1 lepton-number-breaking parameter, distinct from the (dimensionless)
varying-m_e amplitude ε, which is electromagnetic — the two are different quantities and are not related
by any bridge. The value μ = 2.25 meV is not itself derived from first principles; that is the
dark-energy-value problem (§2). The mechanism carries a post-hoc flag until it earns a new falsifiable
consequence.

## 7\. NOW → THE END (the forward map) [Route D: mechanism + pre-registration branch]

**7a. The sequestered floor — a route that does not work.** A Kaloper–Padilla vacuum-sequestering attempt
to fix the dark-energy value from the cosmic expansion history was checked and fails: it predicts a
dark-energy-to-matter ratio at least ~5× too small (and zero for an eternally expanding universe). So the
value is not fixed this way. The model's standing dark-energy predictions remain **w = −1 exactly** and
the neutrino tie (ρ_Λ¼ = m_ν,lightest ⟹ Σm_ν = 61.4 meV).

**7b. The thaw [the forced consequence].** Observed Λ ⟹ turnaround within \~an e-fold ⟹
**m_J \~ (1–3)H₀** ⟹ the floor is thawing NOW:

> **1 + w_floor(a) = thaw · a³** (thawing growth), net apparent CPL (with the shed at g=0.12):
> **(w₀, wₐ) ≈ (−0.92…−0.86, −0.2…−0.5)** — thaw-side, NO true phantom ever.

Code: `dcdf_floor_thaw` (new 2026-07-10; ≤0 recovers w = −1 exactly). ρ_floor(a) =
ρ_inf·exp[thaw·(1−a³)]; E(a) = ρ_floor − ρ_inf added background-only (pattern of dcdf_rho_rad).

**7c. The branch [to be pre-registered, guards owed]:**

> **P-2026-018 (w = −1 exact) XOR Route-D (thaw-now, w₀ ∈ [−0.92,−0.86], wₐ < 0, no phantom).**
> DESI DR3 adjudicates: thaw-side → Route-D (J1+why-now+DESI in one stroke, P-018 dies);
> rigid → P-018 (distinctive win; Route-D dies, J1 reverts to constitution);
> TRUE phantom in the DATA → both die. Guards: distance-space phrasing, KP solve, timestamp
> (J1-derivation precedes DESI-convergence), A2+A3 net (answered).

**7d. The end (and the next start).** The thaw completes → expansion reverses → contraction
blueshifts radiation (a⁻⁴ grows) → the heat fountain reignites → T climbs back through **T_c**
(the SAME derived T_c of §4) → **the dyad condensate MELTS** (m_e → standard for the crunch) →
charge survives in solitons/Q-balls [requires gravity-mediated K<0: fragmentation
banks the charge at T \~ 10¹⁰ GeV, 13 decades before any melt] → torus topology carries the axis
across the bounce (rotation resets, topology doesn't) → re-expansion cools through T_c → the
condensate RE-FORMS → §1. **The condensate breathes; T_c is both the recombination-era turn-on
and the crunch-era melting point — one number, both jobs** (the two-jobs law, §2).
[STORY at the bounce rungs: BKL, Tolman unresolved.]

## 8\. The two-jobs pattern — and where the code reflects it

Every transition is ONE clock with TWO jobs — the ending regime reaches its floor, the starting
regime crosses its threshold:

|transition|job 1 (floor reached)|job 2 (threshold crossed)|in code|
|-|-|-|-|
|H=m (z=4×10⁷)|conformal youth ends|DM (dust) begins|`dcdf_rho_rad` f(a): one function fades radiation as dust continues, continuity-matched|
|T_c (dyad)|thermal disorder dies|condensate/δm_e turns on|`varying_z_high` edge (2nd-order: no latent budget to hand off — a pure switch is CORRECT here)|
|ρ→ρ_inf (z\~0.7)|matter dilution bottoms|de Sitter begins|`w_dcdf(ρ)`: one barotropic function does both automatically|
|shed|matter-part drains|dark radiation grows|the SAME `conv` term, opposite signs, in two ODEs (background.c:2843-45) — the pattern literally|
|thaw/turnaround|the floor era ends|the turn begins|`dcdf_floor_thaw` (new)|

The conservation-pair transitions carry the two jobs as one term with two signs; the
second-order (continuous) transition carries them as one edge with no budget. **The code
reflects the law wherever the law demands it, and correctly does NOT fake a hand-off where
the physics has none.**

## 9\. Ledger (what this spine rests on)

**Recorded:** DM+DE unification (2→1); ε derived (docketed); onset = H=m identity; dyad onset derived
(electron-CW); gate-0 clearance (double regime-citation, pending the docketed confirm); AZK-safety; leptonic
allowed≠generated. **Falsified:** P-2026-004 (high Σm_ν). **Live falsifiers:** DESI DR3 (the
branch), Σm_ν ≈ 60 meV, 0νββ, void/IGM m_e-step (P-007, J4). **Owed:** KP self-consistency
(docketed), the docketed confirm, low-scale seesaw (docketed), spurion identification (docketed) + new consequence
(docketed), leptophilia portal (docketed), DE value if Route-D dies (constitution). **Standing:** provisional pending the named referees
, DESI-capped, the branch pre-registration pending guards.

---

## ADDENDUM (2026-07-10, later): §7 STATUS CHANGE — the internal falsifier FIRED

The full-cycle KP solve (full_cycle_kp.py) computed the fixed point over the whole
cycle (expansion + thawed contraction + Tolman boost): **it robustly wants a_turn = 0.70 (a PAST
turnaround, z=+0.43)** — excluded by observed acceleration; a future turn is 3× (a_turn=1.0) to
10× (1.5) short, Tolman boost null, and the "full-cycle-fixes-the-sign" claim was WRONG
(near-mirror contraction cancels). **So §7a–7c are DOWNGRADED:** the clean Route-D prediction is
dead; what survives is the IMMINENT-TURN CORNER (z_turn \~ −0.1..−0.3, needing \~3× from four
favorably-aligned rigorous-KP O(1)s [prior-adverse, tail] AND a strong thaw pulled by the data).
The two kill switches MERGE: the running Route-D MCMC (thaw free on the DESI joint stack) is the
single decider — thaw pulled hard → corner lives; thaw \~ 0 → Route-D dead twice over, **P-2026-018
(w = −1 rigid) stands as the distinctive branch, and J1 reverts to constitution/boundary-datum.**
§7d (the melt/re-form cycle closure) is unaffected as STORY. Held provisional.

---

## §10 — THE ATOM READING (the capstone, 2026-07-10 night)

**The universe is a single bound quantum state of the spacefluid — one atom — and cosmology is
its internal atomic physics.** Formation: genesis = recombination (capture cascade; f_amp = the
branching ratio, computable-class). Structure: Landau's two components — the zero-entropy ground
state (floor/constitution/timeless; w=−1 exact \& ageless by theorem) and the entropic excitations
(light/matter/observers; Tolman's arrow). Spectroscopy: torus modes = the line spectrum (low-ℓ =
the first lines); the census = the selection rules; the CMB = the recombination photograph.
Chemistry: the dyad = one universal lepton rescaling ε (Koide-multiplicative), C²-gated, one
fingerprint across H₀/D-H/ν/21cm/radio. Present: mid-emission — Γ/H = √3 = the linewidth (why-now
derived); symptoms {coupling dipole, mass defect = the thaw, recoil = the axis} = the falsifier
board. Biography: first excitation (Tolman arrow, finite past) → lengthening cascades → possible
ionization (binding energy un-computed). J1 = the ground-state eigenvalue: constitutional, at home.
**Status: the grammar is coherence (graded throughout);
the empirical content lives in the children and the symptom chart. The method was the subject.**


## §22 — THE THREADING DAY (2026-07-11, the second arc): sixteen roots, lawful deaths, the ladder, and the BBN witness

**The threading survey:** sixteen direct threads filed and graded (galactic/SMBH
atoms, the neutrino home, S₈, low-ℓ, Koide's invariance, the lab cousins, the coincidence
problem [why-now = √3·A_s·the floor — the √3 one-pager discharged: the Friedmann factor,
value-independent, sharing ONE par-question with c], the purchased silences [direct+indirect],
GW [the vortex null Gμ ~ 3×10⁻²¹; the chirality family's third member], the Hubble standalone,
the radio lattice, the fingerprint capstone, IGMF helicity, LSS parity). **The protocol** (now
standing law + memory): ramp-check every compute; improves-bar, no forcing; the kill autopsy
(countersign + step-audit + coupling-check + why-pass + inheritance-routing); owed-invoices;
5-per-batch. **The inheritance theorem:** no orphan physics (L1) — every non-thread is a child
of a threaded root; deaths are lawful (each names its law — strong-CP and birefringence share
L1a, one clause, shared fate both ways).

**The master computes (the 40 debts factor to 8, in 4 clusters):** par/size (the α_c MCMC +
the lanes), topology (the AD route + the cavity), frame/UV (the Lorentz program + λ), data
(the chains + the epoch stamps). Sprint results: the toy cavity puts ℓ=2,3 BELOW the first
torus mode (T5's matched-circles risk resolved favorable); the thermal-leptogenesis surface is
EMPTY (×40-1000 under everywhere) → **Card 4 reverts to the native AD-direct route (charge =
abundance) with the frozen-era transfer (sphalerons at 130 GeV vs the field frozen till
9.4 keV) as the hard timing crux**; the λ candidate chain failed its own bounce self-check
(informative).

**The λ-ceiling (a small recovery):** the winding-patch isocurvature (14.1% rms
if the onset is quartic) would be CMB-dead ×5-7 → the model REQUIRES λ ≤ (m/Ψ₀)² ≈ 2×10⁻⁹¹ —
a derived self-constraint; the axion-like reading (λ ~ m²/f²) lands at the ceiling within an O(1)
factor → **P-2026-031 (candidate): CDM isocurvature at ℓ ~ 170.** *(Amplitude caveat: the axion
quartic carries a coefficient ~1/6, so |λ| sits a factor ~6 below the naive (m/Ψ₀)² ceiling — the
isocurvature is then likely sub-%-level and below current Planck sensitivity, not at it; the exact
amplitude awaits the O(1) coefficient and the λ-sign.)* (+ a 45-90 km/s bulk-flow shadow). MOND/RAR finally dead (m_amp → m; ≤59 AU ≪ kpc). The third
mass-top coincidence (CSW M_max ~ 10¹¹ M☉ at the ceiling; with α_g = 1 at 6×10⁹ and r_s = ξ
at 2×10¹⁰) — noted, m-correlated, not recorded.

**The scale ladder:** the Bohr skeleton E_b/(mc²) = ½α_eff² at every rung (the
universe rung SITS on its own skeleton: 2.28 vs 2.29×10⁻⁴); the corrected ordering (nucleon >
nucleus > UNIVERSE > atom > star > galaxy — the universe is the tightest GRAVITY-made
structure); **the hinge: ξ = 402 AU inside the solar-system rung — one substrate boundary in
the whole descent**; the double-ladder alignments graded per-rung (2 definitional, 3 loose —
no mechanism, honestly tagged); the energy cascade owed as the dynamical half.

**THE WINDOWED BBN VERDICT:**
T_c ≈ 179 keV is INSIDE the BBN window → the ε(epoch) stamps re-price everything: **the Y_p
medicine was an artifact of applying ε above T_c** — windowed, Y_p ≈ 0.2495-0.2505 (+1.2-1.5σ
COUNTER vs Aver; +3.7σ vs EMPRESS — the helium civil war noted); D/H partially refunded
(net ≈ 2.40-2.42, a ~1.6-1.9σ owned bet). **The BBN synthesis: the sector is THE
TRANSITION'S WITNESS** — the only laboratory that watched the condensation live; the pattern
is RIGID (no dials); referees: the radio referee, the helium resolution, the T_c re-audit
(flagged-not-taken), the α_c MCMC posterior. The adverse landings are logged in public;
the λ-defense is on record.
