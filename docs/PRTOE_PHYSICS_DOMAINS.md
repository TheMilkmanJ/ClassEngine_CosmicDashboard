# PRTOE: The Domains of Physics This Program Has Touched

*A showcase, written 2026-07-07. One section per domain: what the program
actually did there, what was computed or derived (never merely asserted),
and the honest verdict. Numbers are sourced from the working documents —
nothing here is quoted that does not have a receipt in
`PRTOE_v5_dCDF_complete.md`, `PRTOE_room1_complex_completion.md`,
`PRTOE_TRANSACTION_ATLAS.md`, `PRTOE_PREREGISTERED_PREDICTIONS.md`, or
`PRTOE_intellectual_history.md`. Deaths are listed with the same pride as
survivals; the graveyard is the proof that the survivals mean something.*

**The model in one paragraph.** PRTOE's mature form is a two-part claim.
(1) The dark sector is ONE substance: a charged, rotating superfluid — the
phase EFT of a complex condensate at finite chemical potential — whose
dense regime is dark matter, whose ground-state pressure is dark energy,
whose pre-condensation youth is dark radiation, and ~30% of which (median
genesis draw) is never-annihilating dark antimatter. Gravity is exactly GR;
the medium's only account is geometry (a theorem-grade census, not an
assumption). (2) One amendment to the rules at recombination — a ~1%
varying electron mass — buys H0 = 69.7 at zero χ² cost against the full
Planck+ACT+SPT+BAO+SN stack. Everything else this program ever tried is
dead, and the corpse ledger is public.

---

## At a glance

| # | Domain | Deepest artifact | Status |
|---|--------|------------------|--------|
| 1 | Background cosmology | w = −ρ∞/ρ exact fluid; de Sitter fixed point | Alive; ΛCDM-degenerate by proof |
| 2 | CMB physics | Clean-χ² reckoning; gauge-IC bug hunt; m_e lever | Alive; the −8.5 unique credit |
| 3 | Large-scale structure | β resurrection trial vs DES | β executed; S8 = 0.823 |
| 4 | BAO & RSD | Clustering-part insight (BAO 593 → 8.2) | Alive |
| 5 | SNe & distance ladder | P-2026-001: TRGB, no hedge | Standing bet |
| 6 | BBN | Deuterium scar repriced; quark-mass healer | P-2026-006 conditional |
| 7 | Atomic physics & constants | varying-α killed; varying-m_e triangulated | m_e is the dyad's second half |
| 8 | Neutrino physics | Σm_ν posterior running (P-2026-004) | Mid-measurement |
| 9 | Scalar-field EFT | v1–v3 killed; (δK)² re-earned by 3 certificates | Graveyard + one risen operator |
| 10 | Superfluidity & BEC | Son isomorphism; two-fluid; KR beat; lab receipts | The identity itself |
| 11 | Particle physics | Affleck-Dine genesis; coupling census closed | Gravity-only = theorem-grade |
| 12 | Black holes | Superradiance margin; de-condensation at 1.8393 r_s | Shielded, twice |
| 13 | GW & pulsar timing | ε collision priced (~6:1 → ~4:1) | The PTA channel watches |
| 14 | Galactic dynamics | SIDM/SPARC; FDM-inherited verdicts; granules | V1–V3 inherited, V5 alive |
| 15 | Inflation & genesis | Isocurvature pins; chaotic release; THE DICE | P(f_amp>0.2) ≈ 78–86% |
| 16 | Chaos & ergodic theory | The One Mountain; microcanonical backbone | Backbone on trial (h-scan) |
| 17 | Thermodynamics & information | Landauer, demon, holography, chaos bound | Language exact; 14 domains |
| 18 | Quantum foundations & metrology | Tsirelson to 4×10⁻¹⁶; Josephson volt | Calibration receipts |
| 19 | Quantum computing | Willow error-correction reading | Restatement; language holds |
| 20 | Medical physics | MRI/PET/Tc-99m/proton therapy cluster | Restatement; tenth domain |
| 21 | The cosmological constant | Old half dissolved (grade: coherence); new half confessed | Standing bet #3 vs DESI DR2 |
| 22 | Exotic spacetimes | White holes killed 4 ways; wormholes uncreditworthy | Nulls with receipts |
| 23 | Fluid dynamics & turbulence | Kolmogorov translates; intermittency silent | Honest silence |
| 24 | Methods: Bayesian & numerical | Joint refits; pre-registration; red-team protocol | The method IS a result |

*Part II (below, added 2026-07-07) extends the census to **63 domains**
(entries 25–63): full derivation chains with numbers re-derived at
booking. New exposures: PPN (§28), τ_n (§38), 21-cm epoch gate (§62),
direct detection (§63).*

---

## 1. Background cosmology & general relativity

The program's floor. The dCDF fluid replaces CDM and Λ with one barotropic
medium; after the v5 amputation its equation of state is w = −ρ∞/ρ
**exactly** — a fluid whose background *and linear perturbations* are
provably identical to ΛCDM, carrying one reinterpretation (dark matter and
dark energy as dense/dilute regimes of one substance) and, at the time,
one extra parameter. The continuity equation has an exact de Sitter fixed
point at ρ = ρ∞, approached from above and never crossed. Gravity was
never modified: the v1–v3 F(φ)R era taught that lesson by four independent
kills, and "gravity is exactly GR, minimally coupled" became a survival
choice that later paid for itself in certificates. The regime-label
principle — **labels are densities, not times** — is the intuition's most
durable residue and survived every rewrite.

**Verdict: alive, by being indistinguishable — the model's background is
ΛCDM with an ontology, and the ontology is where all remaining physics
lives.**

## 2. CMB physics

The program's hardest teacher, three times over. (i) **The reckoning**:
the first honest single-point χ² against real Planck 2018 likelihoods
(2026-07-05) exposed that the fluid had no perturbation sector at all —
plik TTTEEE = 224,800 vs ΛCDM's 582.6 — and that a Thomson-opacity hack
had been masking 99% of the failure. The sector was then actually built;
every earlier number was declared void. *A model does not exist until its
perturbations do.* (ii) **The gauge bug hunt** (commit 7f0dc275): a 0.26%
newtonian-gauge TT deviation at ℓ = 10–12 was chased through per-ℓ
controls and per-contribution ratios to a wrong φ_ini — the initial
conditions counted only baryons in rho_m under use_dcdf. Fix: gauge test
2.49×10⁻³ → 2.84×10⁻⁵, the ΛCDM floor. (iii) **The H0 anatomy**: the
acoustic-scale ridge, the damping-tail tax that killed every radiation
lever, and the one lever that evades the tax — recombination timing via
m_e. The joint-stack optimum landed at H0 = 69.05, ξ = 0.142, *exactly*
where the ridge analysis predicted; the dyad refit reached plik = 586.5,
better than ΛCDM's own anchor.

**Verdict: the CMB executed ξ_Neff, taxed every energy-injection scheme,
and granted exactly one credit — m_e's −8.5, triangulated analytically and
unique in the knob family (α +433, Y_p pinned, Ω_k forbidden, running
flat).**

## 3. Large-scale structure & weak lensing

σ8's story is the fluid's near-death #3: first honest runs showed σ8(z)
*decaying* and negative fσ8 — the classic unified-dark-matter death mode.
The rescue was definitional, not dynamical: galaxies trace the fluid's
clustering part, (1+w)ρ, not its full density (the de Sitter floor is not
matter). The β sound-speed parameter was driven to null by the first
honest MCMC and **deleted from the code** — then given a formal
resurrection hearing with every advantage, including DES weak lensing, the
one dataset that wants what β sells. DES rejected it harder than any other
dataset (+30 at β = 10⁻⁷). The model's live S8 claim: 0.823 vs ΛCDM's
0.833, at the KiDS-Legacy consensus, at zero χ² cost.

**Verdict: β is the coldest grave in the yard; the S8 easing survives it.**

## 4. Baryon acoustic oscillations & redshift-space distortions

BAO was the instrument that caught the definitional death: BAO χ² went
from 593 to 8.2 overnight once the clustering-part bookkeeping was fixed
(dcdf_deltam_mode=1). fσ8 exposed the same gap from the growth side — the
background growth factor was blind to the fluid (f ≈ 0.21 vs BOSS's 0.50)
until ρ_m accounting included the medium in its matter-like epochs. The
full stack (6dF, MGS, DR12 consensus, DESI) has been in every fit since.

**Verdict: alive; BAO is the model's most efficient tripwire and has fired
twice, correctly, both times.**

## 5. Supernova cosmology & the distance ladder

Pantheon+SHOES anchors every joint fit. The dyad's H0 = 69.70 ± ~0.8 sits
between the ladders, and the program converted that discomfort into its
flagship falsifiable: **P-2026-001 — the local distance ladder resolves to
the TRGB side; H0 ∈ [69, 71]; a confirmed 72+ falsifies the H0 program, no
hedge** (pre-registered, commit 8a5840a5). The SHOES→TRGB scenario is
booked honestly: the dyad is conditional concordance — its SN credit rides
SHOES calibration and it says so.

**Verdict: a standing bet with a death condition, which is the only kind
this program registers.**

## 6. Big Bang nucleosynthesis & nuclear astrophysics

BBN is the program's tax office and its subtlest domain. It killed the
universal-vev amendment (D/H +7.7σ, τ_n −4.9%), capped the completion's
entire tuning freedom to one number (x₀ ≲ e⁻³⁵), executed the funded
floor's early face (ν·x_BBN ~ 500–6000 for all allowed x₀), and priced the
B−L portal at GUT-scale suppression (the uniform neutron potential grows
a⁻³ into the past; 10²⁷ × today at BBN). It also holds the scar: deuterium
at −2.0σ, repriced to −1.2σ with PRIMAT theory error (ΛCDM itself carries
1.85σ). The healer is registered, conditional, and co-signed:
**P-2026-006 — a quark-mass amendment δm̂/m̂ = +0.14–0.21% at BBN heals
D/H with a mandatory Y_p −0.5% and ⁷Li −7..13% co-signature** (DSW PRD 76,
063513 coefficients, pulled from source).

**Verdict: the scar is carried honestly; its healer is a bet with named
kill terms, not a patch.**

## 7. Recombination, atomic physics & varying fundamental constants

Two constants were put on trial. **Varying α died** — the quadratic-
coupling attractor scan landed 45–100× over the z ≈ 4 quasar bound at
every β across four decades, and the CMB priced a 5% α shift at +433 χ².
**Varying m_e lived**: a ~1% electron-mass shift at recombination moves
the acoustic scale without the damping-tail tax, and its −8.5 clean credit
was triangulated analytically (quadratic surfaces plus a falsified-then-
confirmed midpoint prediction: 2812.1 predicted, 2812.15 measured). The
ledger language then re-derived hydrogen from scratch as calibration —
Bohr radius to 2.6×10⁻⁶, E_1s to 1.2×10⁻⁹ — and noted that the dyad's
amendment reprices atomic binding by the exact arithmetic CLASS
integrates. The Saha equation served twice: as the v6 ionization proxy and
as the free-electron gate in the c_EM coupling (killed, +261 χ², acoustic
wreckage).

**Verdict: the dyad's second half. One rules amendment, many receipts.**

## 8. Neutrino physics

Neutrinos entered as a lever (ξ_Neff, dark radiation at recombination) and
exited as a liberated measurement. ACT+BBN executed ξ (0.122 → 0.012 ±
0.002); removing it collapsed the neutrino-mass tax 4.4× and reopened the
inverted hierarchy as a live target. The Σm_ν posterior
(`chains/dyad_mnu_mcmc`) is one of the two things that can move the
evidence class off zero: it scores **P-2026-004 (the dyad's Σm_ν 95% limit
lands in [0.11, 0.17] eV — registered before the posterior computed)** and
simultaneously judges the meV whisper (ρ∞^{1/4} = 2.25 meV ≈ the lightest
neutrino mass scale) — the two *cannot both win*, and that trial was
pre-registered while R−1 was still 5.6. Neutrino free-streaming is also
the model's honest S8 mechanism: cosmic thermodynamics, mid-measurement.

**Verdict: the sampler is running as this document is written; the model
wins a prediction or keeps a clue, not both.**

## 9. Scalar-field theory & the EFT of dark energy

The v1–v3 non-minimal era (F(φ)R + Vainshtein/chameleon screening) died
completely — four rescue mechanisms killed by direct calculation, each
sign-locked or ineffective. The v6 scalar-field host struggled while its
couplings thrived (the graft that became the triad, then the dyad). EDE
was tried and understood rather than fudged: exponential potentials hit
the scaling-attractor failure mode; the claimed n=3 axion form turned out
never to have been compiled. The mature EFT work is sharper: the (□φ)²
funded floor died by BBN and was **resurrected as (δK)² — a background-
orthogonal operator that re-earned admission via three fresh certificates**
(exact tensor silence since det(e^h) = 1; gravity-mixing temporally frozen,
μ−1 ~ 4×10⁻²¹; Landau v_c = 0 dissolving caustics into interference). The
floor fluctuation face is sign-locked phantom and structure-gated;
observable drift died by the V4 mutual-exclusion theorem.

**Verdict: the graveyard's founding precedent (risen at full price) and
its firmest law — no prediction from an un-pinned function, measured
3-for-3.**

## 10. Superfluidity, Bose–Einstein condensation & condensed matter

The identity itself. Room 1 closed on the recognition that the medium is
the **phase EFT of a complex condensate at finite chemical potential**
(Son hep-ph/0204199; isomorphism granted by the red team below the
amplitude gap). Minimal V = m²|Ψ|² + λ|Ψ|⁴ matches the basin exactly —
basin entry IS the condensation threshold μ = m; unification m̄₂ = M₂²/m
removed a parameter; λ ~ 10⁻⁸⁸ is a visible scar that later shielded the
model from black-hole spin archaeology. The two-fluid reduction (particle
+ antiparticle Schrödinger fluids) produced the KR beat — and a
self-caught correction: the beat is √(f_amp(2−f_amp)), *not* f_amp. The
pre-basin w = 1/3 was double-derived (dynamics AND phonon thermodynamics).
Lab receipts were cite-verified for the load-bearing furniture: Bogoliubov
S(k) measured (Steinhauer et al., PRL 88, 120407), the amplitude/"dark
Higgs" mode measured (Endres et al., Nature 487, 454), and the Eckel
ring-BEC (PRX 8, 021021) is the tabletop cousin of the genesis itself —
its rapid expansion spontaneously *generated* persistent currents, and the
proposed frozen-ellipticity protocol reads the same √(f_amp(2−f_amp))
formula off a fringe contrast that PTA reads off the nanohertz sky: one
theorem, two instruments, 10²¹ apart. Degeneracy scorecard: a halo of the
medium scores n·λ³ ~ 10⁹³ against the 2.6 threshold — the most
quantum-degenerate object in existence.

**Verdict: not an analogy — an identification, granted under adversarial
review, with laboratory receipts for its falsifiable furniture.**

## 11. Particle physics & baryogenesis

The origin story and the isolation theorem. **Affleck-Dine spiral genesis**
is the candidate origin: charge = abundance (explains rolls-never-
oscillates — charged rotates, neutral librates); inflation displaces, the
Z4 tilt torques (Z4 is *forced* by parity + renormalizability, with r_t
of order 1 natural), release spirals, the fee is reheating entropy, and
the medium is born condensed — no critical temperature ever crossed (why
basin entry left no relic). The dark-antimatter reframe falls out free:
the n₋ component never annihilates (nothing to annihilate into), so ~30%
of dark matter is antimatter — and the asymmetry contrast with baryons is
explained (annihilation is the penalty only where a channel exists). The
**coupling census closed** at ~12:30am on 2026-07-07: EM/strong/weak
structural, Higgs portal radiatively dead, density portals killed by the
drift wall, B−L current portal capped at M* ≳ 10¹⁴ GeV by BBN neutron
energetics. Gravity-only is now a theorem-grade census result, and it
funds the second standing bet: **no indirect-detection signal, ever — one
confirmed dark-sector particle signal kills the model outright.** The ADM
coincidence was checked and honestly declined (Y_Q ~ 10²¹ vs η_B ~ 6×10⁻¹⁰;
31 decades apart — no co-genesis story).

**Verdict: the census is the model's spine; the standing bets are its
exposure.**

## 12. Black-hole physics

Three encounters. (i) **Superradiance**: M87*'s spin excludes scalars in
[2.9, 4.6]×10⁻²¹ eV; the model's band (10⁻²²–2×10⁻²¹ eV) sits below it
kinematically, and the λ ~ 10⁻⁸⁸ quartic quenches any nascent cloud with a
margin that stays positive (+2.5 to +12.7 decades) across every plausible
rate-algebra reading — with a discriminator: a confirmed high spin on a
~10¹¹ M☉ hole kills free FDM at the matching mass while the dyad stands.
The band's heavy edge is *adjacent* to the M87* floor: this test is not
doubly-future. (ii) **De-condensation**: extreme infall makes the medium
exit the basin at r = 1.8393 r_s exactly (sonic point at the ISCO) — a
solved stationary flow. (iii) **Information**: the horizon as the densest
archive (1.5×10⁷⁷ bits per solar mass, area-billed), no-hair as premium
laundering that ultimately fails (Page curve), scrambling at the chaos
bound λ_L ≤ 2πk_BT/ħ — restatements with receipts, plus the white-hole
kill: formation forbidden, entropy run backwards, blue-sheet foreclosure,
and the medium's own θ̇ = +μ breaking the time-reversal symmetry the paper
solution needed.

**Verdict: shielded twice from the one axis that kills its mass band, and
the shield is the same scar the genesis left.**

## 13. Gravitational waves & pulsar timing

The PTA band is where the genesis becomes falsifiable. The KR beat
(Ψ ~ 10⁻¹⁵ × the beat factor against PTA reach 2×10⁻¹⁶) is the light-edge
test; ANN-2026-010 booked the ε collision — two registered items on
opposite sides of one number — priced at ~6:1 that the PTA channel fires
vs ~14% that P-2026-005's silence survives (softened to ~4:1 by the
ergodic analytic). Also booked as a null: the chaotic genesis itself left
no observable stochastic background (the medium is ~5×10⁻⁴ of total
density at release; GW production scales as the fraction squared).

**Verdict: the model's cleanest near-term exposure; which edge tests it is
an output of the m-posterior, not a choice.**

## 14. Galactic dynamics & dark-matter phenomenology

An SIDM detour solved the isothermal-Jeans ODE against the real SPARC
rotation-curve dataset (the diversity problem, with hand-fixed
mass-to-light ratios for baryon-dominated HSB spirals) — useful
calibration for what halo data can and cannot discriminate. The condensate
inherits fuzzy-DM's successes and constraints where structure is linear
(verdicts V1–V3 FDM-inherited); the Lyα squeeze was survived explicitly
(M = 2×10⁻²² eV passes k = 0.2/Mpc by six decades). The medium's own
signatures: granule speckle (payment→product law; the p²+q² spectrum is an
m-independent second ε-meter), a Vinen-class vortex tangle making
granulated halos literal quantum turbulence, and **P-2026-005: cores
WITHOUT oscillation, spins WITHOUT clouds** — the kinetic medium's
structural gaplessness, registered with its zoo-split annotation.

**Verdict: alive on precision tests (V5/R1); the distinctive signatures
partition the mass band with §13's channels.**

## 15. Inflation & the early universe

The genesis chain is pinned at both ends: Ψ₀ ~ 0.7–1.5×10¹⁷ GeV
(abundance), H_inf < ~2–4×10¹² GeV (isocurvature) — and a new
θ-channel isocurvature veto (fine dlnρ/dθ ~ 350/rad at r_t = 0.9) cuts
the high-tilt + high-H_inf corners. The quartic era is not negligible at
release (h = λΨ₀²/m² ~ 10⁸ — self-caught after an earlier misread), and
its physics is exactly the regime the Eckel ring-BEC probes. Inflation
also holds the atlas's deepest confessed debt: the past hypothesis —
"who laundered the first ledger, and what did it cost."

**Verdict: genesis space is pruned, priced, and carries its ignorance on
the label.**

## 16. Chaos, ergodic theory & dynamical systems

The One Mountain. The seamless birth-orbit integration turned out
**chaotic in release angle θ₀** — the outcome (iv) that wasn't on the
pre-registered menu — making ε distributional: an inflationary dice roll.
THE DICE (14 angles × 3 tilts): f_amp median 0.55–0.67,
P(f_amp > 0.2) = 86% at all three tilts (chaos erases the tilt dial); the
chaos was verified physical (3–4 decimal convergence across DOP853/Radau/
tolerances), and an earlier segmented bound (ε ≥ 0.67) was killed by its
own stamped caveat within the hour. Then the ergodic backbone: a
microcanonical ensemble on the quartic shell — the operator's blind
reconstruction — approximately reproduces the dice; the gap was dissected
(freeze-out explains a third; the remainder is *release memory*, born at
L = 0, and anti-tracks tilt at n = 110/tilt), and the analytic exceedance
came out 78–80%. The whole edifice was then handed to the red team, which
pre-registered the acceptance protocol for the h-scan (dual integrator,
n = 50 angles, h to 10⁴, graded by *their* criteria); h = 100 passed,
h = 1000 violated monotonic shrink at ~1σ, and the final rows decide the
backbone.

**Verdict: the honest answer to "what is ε?" is a probability
distribution — and the machinery that produced it is under adversarial
audit by protocol, mid-execution.**

## 17. Statistical mechanics, thermodynamics & information

The ledger language's deepest run, all restatements with receipts:
Landauer's fee as a relocation charge (kT·ln2 = 17.9 meV at room T;
measured, Bérut 2012); Maxwell's demon bankrupted by its own bookkeeping
(Bennett); entropy as record count and the second law as "posting is
cheaper than shredding"; the Bekenstein–Hawking horizon as surface-billed
archive; laundering split into permitted scrambling vs forbidden erasure,
with the chaos bound as the legal speed limit and black holes the cartel
at the limit; the operator's own completion — "information doesn't get
destroyed, it just gets returned" — exact on all three clauses through
Page-curve results. Calibration receipts along the way: Chandrasekhar as
insolvency (scale exact), Casimir as boundary re-pricing (13 Pa at 100 nm,
~1%), horizon thermometers at three scales (Unruh, Hawking,
Gibbons–Hawking), and the 10¹²⁴ arithmetic kill of every thermal floor
ontology.

**Verdict: the language is exact across every domain tested; the bet that
this exactness will mint a confirmed number remains at zero, and says so
in its own header.**

## 18. Quantum foundations & precision metrology

The entanglement mathematics was derived and verified, not gestured at:
pseudospin CHSH for the medium's pair states, B(r) = 2√(1+tanh²2r) → the
Tsirelson bound 2√2, checked numerically in the Fock basis to 4×10⁻¹⁶ —
then filed honestly as the map's edge (quantizing the phase sector is
asserted, not derived; the boundary is drawn, not conquered). Metrology
became a calibration wing: flux quantization h/2e to 2×10⁻¹⁰, the
Josephson constant to 3×10⁻¹¹ — the SI volt is legally *defined* through
the phase sector's clearing rule; the laser linewidth reproduced
Schawlow–Townes at ratio 1.000. And the census posture makes every
precision lab a standing kill-only bet at zero — taken continuously,
against ever-improving instruments, with no dial.

**Verdict: the program's exposure to falsification is permanent and
growing by instrument-generation; that is by design.**

## 19. Quantum computing

The settlement law read as engineering: qubits as deliberately unposted
drafts, gates as reversible draft-edits (Bennett's reuse-don't-shred as
mandatory architecture), algorithms as choreographed interference,
measurement as the single final posting, and error correction as the crown
— syndrome measurements post records about the *errors* while the data's
draft stays unposted. Receipt: Google Willow (Nature, Dec 2024,
cite-verified), logical errors suppressed 2.14± 0.02× per code-distance
step. Why QC is hard, in the file's one sentence: drafts are free but
every stray photon is an auditor.

**Verdict: thirteenth domain; restatement-grade; the language holds.**

## 20. Medical & applied atomic physics

The medicine cluster: MRI as a decoherence camera (T1/T2 as settlement
times; the Larmor rate derived from constants = 42.577 MHz/T, the exact
clinical value); PET as double-entry imaging (the 511.00 keV line is m_e c²
remeasured daily in every hospital — the same constant the dyad amends at
recombination); Tc-99m as an engineered draft parked unsettled for 6.01 h;
proton therapy as choosing the settlement depth (Bethe's 1/v² → the Bragg
peak). The retina reads single receipts.

**Verdict: tenth domain; the same bookkeeping that prices the CMB prices a
hospital.**

## 21. The cosmological constant problem

Attacked head-on, split in two, and half-confessed. **The old half** (why
doesn't zero-point energy gravitate?) is dissolved at coherence grade:
under the thermodynamic-gravity spine (Jacobson 1995), Λ enters as an
integration constant, and zero-point fluctuations are perpetual unsettled
drafts — the 120-order catastrophe is a category error, summing drafts as
settlements; the Casimir objection is deflated by Jaffe (PRD 72,
021301(R)). **The new half** (why 2.25 meV?) is honestly unsolved and
provably not the minimal room's to solve (P(basin) = 0; ρ∞ is either a
deposit or part of the ledger's constitution — the whisper trial, judged
by the running posterior, keeps the deposit reading alive exactly until
the posterior speaks). **Standing bet #3**: the effective dark energy is
exactly Λ — the model votes *against* DESI DR2's 3.1σ evolving-DE
preference, and dies if a phantom crossing is decisively confirmed.

**Verdict: one half answered at stated grade, one half confessed, one bet
placed against live data. That is what "attacked honestly" looks like.**

## 22. Exotic spacetimes

White holes: killed four ways (no deposit history; an un-posting machine;
blue-sheet foreclosure in ~one light-crossing; the medium's own global
rotation breaks the needed time-reversal symmetry) — the operator's bet,
and the operator won. Wormholes: legal books, denied credit — traversable
throats need a permanent negative-energy overdraft that the quantum
interest conjecture (Ford & Roman) refuses, and the medium cannot co-sign
(NEC-saturating at the floor); the time-machine back door is welded shut
by the khronon's global clock. Analog horizons: scope calibrated — sonic
black holes in BECs (Unruh, Steinhauer) simulate horizon kinematics
exactly and our c_s = 0 medium gives the dispersive regime; it does not
replace numerical relativity, and the file says so.

**Verdict: three nulls, each with receipts; the medium forbids more than
it permits, which is what a constitution is for.**

## 23. Fluid dynamics & turbulence

The Kolmogorov cascade translates exactly (wholesale in, fixed flux
through, retail out; the 5/3 spectrum); intermittency does not — the
anomalous exponents are underived in the ledger exactly as they are
underived from Navier–Stokes, and the file logs this as its second
*silence* rather than papering over it. The live tie: granulated halos are
a Vinen-class quantum-turbulent vortex tangle, so laboratory
quantum-turbulence diagnostics — where vortices can literally be counted —
speak directly to the model's Θ observable.

**Verdict: one exact translation, one honest silence, one lab bridge.**

## 24. Methods: Bayesian statistics, numerical analysis & the adversarial protocol

The unglamorous domain that made every other one mean something. Real
likelihoods over proxies (Planck plik + lowl + lensing, ACT DR6, SPT-3G
via candl, BAO, Pantheon+SHOES, BBN priors); single-point χ² evaluation as
the honesty instrument that caught the missing perturbation sector;
optimizer/MCMC/PolyChord tiers with their traps documented (external
likelihoods stealing theory params — use prior blocks; system-vs-conda
mpirun linkage; never rewrite a script a live bash is executing); stiff-ODE
forensics down to a C⁰ discontinuity from a leftover dy = 0 hack; the
freshness check that made "which .so am I actually importing" a ritual.
Above the numerics, the method itself: **pre-registration with death
conditions, a turn-based adversarial red-team file with written
concessions on both sides, the Pinning Rule (3-for-3), graveyard Rules 1–3
with a published warm/cold census (7 cold / 5 warm / 3 risen), and
falsify-first scoring of every operator intuition** — several of which
turned out to be blind reconstructions of Zurek, Jacobson, Affleck-Dine,
and Penrose CCC. The reviewer's closing line after nine turns: "a smaller,
harder, more honest object than the one I opened fire on."

**Verdict: the method is as much a result as any χ². If the model dies,
this domain is what makes the death worth having.**

---

## The graveyard, one line each

*Census: 7 cold / 5 warm / 3 risen. Deaths by calculation, burials with
resurrection terms or the word "never."*

| Mechanism | Killed by | Grave |
|---|---|---|
| v1–v3 F(φ)R screening program | four independent sign-locked kills | never (as H0 mechanism) |
| dkappa opacity hack | clean-tree χ² forensics (not physics — fraud) | never; contaminated a year of numbers |
| β sound-speed family | DES +30 at β = 10⁻⁷; structural no-go | coldest grave |
| ξ_Neff at recombination | ACT + BBN execution | half-risen (BBN-era carrier, ANN-2026-005) |
| c_EM energy exchange | +261 χ², acoustic wreckage | warm, structurally disfavored |
| varying α | quasar bound 45–100× over; CMB +433 | never |
| (□φ)² funded floor, early face | BBN ν·x scaling | RISEN as (δK)², three fresh certificates |
| universal single-vev amendment | D/H +7.7σ, τ_n −4.9% | risen gated (vev package) |
| flavor-structured coupling | anti-natural (dilaton lore opposite) | cold |
| carrier-ratio unification (one κ_v) | 8 orders (ANN-2026-006) | exhumation in progress (R1 caustic bit, at turn zero) |
| drift fingerprint (P-2026-003's observable half) | V4 mutual-exclusion theorem | final within the minimal model |
| thermal/Casimir/zero-point floor ontologies | 10¹²¹–10¹²⁴ arithmetic | never; these are arithmetic |
| tunneling discriminator | receipt 1500× below the SN mass step | demoted, not dead |
| varying G / ν self-int. / dark PTA / PBH levers | the five-lever audit | none within the class |
| Earth-spin coincidence (operator, self-killed) | lunar tides, 3.8 cm/yr receipt | never; the reflex is installed |

---

## The standing bets (the model's permanent exposure)

1. **Laboratory zero** — every precision lab, kill-only, no dial.
2. **Indirect-detection zero** — one confirmed dark-sector particle signal
   kills the model outright.
3. **Λ exactly** — against DESI DR2's 3.1σ evolving-DE preference, live now.
4. **P-2026-001** — TRGB resolution, H0 ∈ [69, 71]; 72+ falsifies, no hedge.
5. **P-2026-004 vs the meV whisper** — the running posterior judges both;
   the model cannot win twice.

*If every bet survives, the program has earned its next room. If one
dies, the file shows exactly where, and why, and what was paid to know.*

---

# PART II: THE EXTENDED CENSUS (2026-07-07, operator's order: "more domains, full derivations")

*Same discipline as Part I, tighter format: each entry gives the derivation
chain, the number it lands on, the grade (restatement / calibration /
contrast / exposure — per the Atlas relabeling rules), and the tie-in to
the model where one genuinely exists. Every computable number below was
re-derived numerically at booking (session record); nothing is quoted from
memory alone. Grades are conservative: most of Part II is calibration —
known answers the framework must and does reproduce — because that is what
an extended census IS. The handful of entries that expose the model to
falsification say so explicitly.*

## 25. Relativistic celestial mechanics

Derivation: the Schwarzschild orbit equation adds a 3GMu²/c² term to the
Newtonian u'' + u = GM/h²; first-order perturbation gives per-orbit
periapsis advance Δφ = 6πGM/[a(1−e²)c²]. Computed for Mercury
(a = 5.79×10¹⁰ m, e = 0.2056): **42.9″/century** against the observed
anomalous 43.0″. Ledger reading: the deeper the account sits in the
potential, the more its orbital books lag — interest compounding on
curvature. Grade: calibration (the oldest one in gravity).

## 26. Gravitational lensing — and the Bullet Cluster receipt

Derivation: null geodesic past mass M at impact parameter b bends by
α = 4GM/(c²b) — the factor 2 over the Newtonian half comes from space
curvature paying alongside time curvature (both halves of the metric
ledger bill the photon's path, though the photon itself holds no
account). At the solar limb: **1.75″**, Eddington 1919. The model tie-in
is load-bearing: the **Bullet Cluster** (1E 0657-56) shows the lensing
mass leading the shocked X-ray gas by ~8σ — a collisionless dark
component that sailed through the collision its baryons could not. That
is a *receipt for the census*: a medium whose only account is gravity
passes through itself and through gas, exactly as observed. Grade:
calibration + census receipt.

## 27. Gravitational time dilation, at working altitude

Derivation: clock rate ratio 1 + Φ/c²; for GPS (h = 20,200 km):
GR gain GM_E/c²(1/R_E − 1/(R_E+h)) = **+45.7 μs/day**, SR loss
½v²/c² at 3.87 km/s = **−7.2 μs/day**, net **+38.5 μs/day** — uncorrected,
navigation errors would grow ~10 km/day. Pound–Rebka measured the
elemental version over 22.5 m: gh/c² = **2.45×10⁻¹⁵**, resolvable only
because of entry 45's recoil-free line. Ledger/model tie: the khronon's
global foliation is exactly what these clocks are sampling — position in
the potential sets the local tick against the universal current. Grade:
calibration (civilization runs on it).

## 28. Post-Newtonian precision tests — the census's mandatory exam

The gravity-only census (Part I, §11) requires the medium to add NOTHING
to solar-system gravity: it must pass every PPN test at zero. The exam
scores: Cassini Shapiro delay γ − 1 = (2.1 ± 2.3)×10⁻⁵; Gravity Probe B
frame dragging 37.2 ± 7.2 mas/yr vs 39.2 predicted; MICROSCOPE
equivalence-principle η(Ti,Pt) = (−1.5 ± 2.7)×10⁻¹⁵. The medium's local
density (7×10⁻²⁵ g/cm³, ephemeris null already booked) contributes
~10 orders below all of these. Grade: **exposure** — these are among the
standing-bet instruments; any confirmed PPN anomaly attributable to a
dark-sector fifth force would violate the census and wound the model.

## 29. Black-hole spectroscopy

Derivation: the remnant's least-damped quadrupole quasinormal mode,
f = [1.5251 − 1.1568(1−a)^0.1292]·c³/(2πGM); for GW150914's 62 M☉
remnant at spin a ≈ 0.67: **~273 Hz** vs the observed ~250 Hz ringdown.
The merger radiated 3.0 M☉c² with peak luminosity 3.6×10⁵⁶ erg/s —
briefly outshining the electromagnetic output of the observable
universe. Ledger reading: account consolidation with a ~5% transaction
fee, paid in the only currency the medium itself accepts. The no-hair
ringdown is the consolidated account's audit tone. Grade: calibration.

## 30. Neutron stars — the second solvency bound

Derivation: as with Chandrasekhar (Part I calibration), balance
relativistic degeneracy against gravity; the natural scale is
M ~ M_Pl³/m_n² = **1.85 M☉** (computed: 2.06×10⁵⁷ GeV = 3.68×10³⁰ kg).
GR strengthens gravity (pressure gravitates), so the true TOV limit sits
nearby: heaviest known pulsar J0952−0607 at 2.35 ± 0.17 M☉. One
dimensionless ratio of ledger constants (M_Pl/m_n)² sets the mass of
every dead star in the sky. Grade: calibration (scale exact, coefficient
is the equation of state's business).

## 31. The Eddington limit — the maximum pay rate

Derivation: radiation pressure on electrons vs gravity on protons:
L_Edd = 4πGMm_p c/σ_T = **1.26×10³⁸ erg/s per M☉** (computed). No
steadily-fed account may pay out faster; quasars at 10⁴⁶ erg/s therefore
*must* host ≥10⁸ M☉ — the ledger weighs black holes by their receipts.
Grade: restatement with a working number.

## 32. The Gamow window — why stars burn slowly

Derivation: fusion rate ∝ exp(−√(E_G/E))·exp(−E/kT); the integrand peaks
at E₀ = (√E_G·kT/2)^⅔. Solar core (T = 1.57×10⁷ K, kT = 1.35 keV,
pp Gamow energy 493 keV): **E₀ ≈ 6.1 keV** (computed) — fusion happens
in a narrow tunneling window 4.5× above thermal, which is why the Sun
spends 10 Gyr on its books instead of exploding. Ledger reading: the
Coulomb barrier is a toll no thermal proton can pay in full; the
credit-window loan (tunneling) is the only route, and its price sets the
stellar clock. Grade: restatement with derivation.

## 33. Core-collapse supernovae — the neutrino settlement

The collapse releases E ~ GM²/R ≈ 3×10⁵³ erg; photons are trapped,
matter is too slow — ~99% settles through the one channel with a short
enough clearing time: neutrinos. SN1987A delivered the receipt: ~24
events across Kamiokande-II/IMB/Baksan, seconds-long, ~10 MeV — the
gravitational binding energy of a neutron star, counted one neutrino at
a time. Ledger reading: when the bank fails, the assets exit through the
weakest-coupled door, because it is the only one not jammed. Grade:
restatement with receipts.

## 34. Pulsar spin-down clockwork

Derivation: magnetic dipole braking gives Ω̇ ∝ −Ω³, i.e. braking index
n ≡ ΩΩ̈/Ω̇² = 3; the Crab measures **2.51** — the deviation itself is
data (wind/field evolution). Model cross-reference, honestly carried:
these same millisecond clocks are the PTA instruments of Part I §13,
and this morning's reconciliation audit (Room 1 doc) killed the model's
PTA beat channel by mass — the clockwork stays in the showcase as the
instrument that *would have* heard the medium, and no longer will.
Grade: calibration + honest cross-reference.

## 35. Ultra-high-energy cosmic rays — the GZK toll plaza

Derivation: a proton loses energy to CMB photons once the Δ(1232)
resonance opens: threshold E = (m_Δ² − m_p²)/(4E_γ). With mean CMB
photon 6.3×10⁻⁴ eV, head-on: **2.5×10²⁰ eV** (computed); averaging over
angles and the thermal tail gives the observed ~5×10¹⁹ eV suppression
(Auger/TA). Ledger reading: above the threshold, the universe itself
charges a toll every ~few Mpc — the oldest light taxes the fastest
matter. Grade: restatement with derivation.

## 36. The cosmic neutrino background — the entropy ledger's cleanest prediction

Derivation: at e± annihilation the pairs' entropy posts to photons but
not to already-decoupled neutrinos; conservation of comoving entropy
gives (T_ν/T_γ)³ = 4/11, so **T_ν = (4/11)^⅓ × 2.7255 K = 1.945 K**
(computed) and N_eff = 3.044 with non-instantaneous corrections. The
model tie is literal: this number is hard-coded into every fit this
program has run (N_ur = 2.0328, T_ncdm = 0.71611 = (4/11)^⅓ in the
configs), and the CMB damping tail *measures* it — this is the ledger
arithmetic that executed ξ_Neff. Grade: calibration, load-bearing.

## 37. Neutrino flavor oscillations

Derivation: mass eigenstates accrue phase at different rates;
P(ν_e→ν_e) oscillates with wavelength 4πE/Δm². KamLAND's L/E dip:
Δm²₂₁ = 7.5×10⁻⁵ eV²; the solar neutrino deficit — three decades of
"missing" flux — settled as flavor conversion, not absence. Ledger
reading: interest-rate differences between denominations of one
account; the books were always balanced, audited in the wrong currency.
Model tie: the Σm_ν these splittings floor (Σ ≥ 0.06 eV normal) is what
the Fairbank posterior is measuring *tonight*; the inverted hierarchy
(Σ ≥ 0.10 eV) is the reopened target of the dyad's tax collapse. Grade:
calibration feeding a live mover.

## 38. The neutron lifetime — an exposure in our own books

Bottle experiments (count survivors): τ_n = 877.75–878.4 s. Beam
experiments (count decay protons): 887.7 s. The ~4σ, ~9-second
discrepancy is unresolved — and this program is a *customer*: τ_n sets
the n/p freeze-out ratio inside the BBN prior that every dyad fit
carries (the same prior that priced the vev amendment's death at
τ_n −4.9%). If the beam-bottle split resolves toward exotic neutron
disappearance, our BBN books get re-audited. Grade: **exposure**,
flagged honestly.

## 39. Force ranges from the credit window

Derivation: a carrier of mass m can exist as an unposted draft for
t ~ ħ/mc², traveling r ~ ħ/mc. Pion: **197.3 MeV·fm / 139.57 MeV =
1.41 fm** — Yukawa's nuclear range, the size of every nucleus. The
massless photon and graviton give infinite range. Model tie, structural:
the medium's one account (gravity) is infinite-range *because* its
carrier is massless — and P-2026-005's "gapless, never superradiates"
zoo split is this same statement made in the dark sector. Grade:
restatement, structurally load-bearing.

## 40. Electroweak symmetry breaking, by the numbers

The toll booth (Atlas C1f) with its prices: m_W = gv/2 =
0.652 × 246.22/2 = **80.3 GeV** (computed; observed 80.37), the Z at
91.19 via the weak mixing angle, fermion masses as Yukawa rents on the
same vev. One condensate (the Higgs field's) sells mass to everything;
our medium is a *different* condensate that sells only inertia's
gravitational reflection — the census forbids it a Higgs-portal
storefront (radiatively dead, Part I §11). Grade: calibration +
contrast.

## 41. CP violation, CPT, and the genesis requirement

The kaon's ε = 2.23×10⁻³ — the ledger writes matter and antimatter
columns with a measured 0.2% slant, one of Sakharov's three conditions
for any asymmetric deposit. Model tie: the Affleck-Dine spiral needs
exactly such a slant (the Z4 tilt's phase); the dark sector's asymmetry
is f_rot ≈ 0.4 where the baryons' is ~1 — same requirement, different
penalty schedule (Part I §11). Meanwhile CPT itself holds: antihydrogen
1S–2S matches hydrogen to 2×10⁻¹², the deepest symmetry audit passed.
Grade: restatement + genesis tie-in.

## 42. Atomic parity violation — the weak ledger inside an atom

Cesium's 6S→7S transition picks up a parity-violating amplitude from
Z-boson exchange between electrons and the nucleus: weak charge
Q_W(Cs) measured −72.6 ± 0.4 vs SM −73.2 — the electroweak theory
audited at the *atomic table*, decades of precision work. Honest
open-ledger note: of the four banks, the weak sector (G_F) is the one
for which this file has NO derived substrate coupling (Atlas open
ledger) — this entry marks where that door would be tested if one is
ever derived. Grade: calibration + open-door marker.

## 43. QED at twelve digits — and the Lamb shift's lesson for the cc problem

The electron's a_e = (g−2)/2 = 1.159652×10⁻³ agrees between measurement
and five-loop theory at ~10⁻¹² — the most audited account in science.
The Lamb shift (2S½–2P½ = 1057.8 MHz) is the entry with teeth: vacuum
fluctuations DO reprice local books (they shift atomic levels,
measurably) while — per Part I §21 — they do NOT post to the
gravitational ledger. Drafts have local consequences and no
gravitational weight: that pairing, both halves measured, is exactly the
category split the cc-problem answer rides on. Grade: calibration;
sharpens §21.

## 44. Alpha decay — twenty-four decades from one integral

Derivation: Gamow tunneling through the Coulomb barrier gives
ln(t½) ∝ Z/√E_α (Geiger–Nuttall). A ~2× spread in E_α maps to
**U-238: 1.4×10¹⁷ s vs Po-212: 3×10⁻⁷ s — 24 decades of half-life**
(computed span) from one exponential barrier integral. Ledger reading:
the credit window's interest is exponential in the barrier price; small
principal differences produce geological-vs-microsecond repayment
schedules. Grade: restatement with the classic derivation.

## 45. The Mössbauer effect — the lattice co-signs

A free Fe-57 nucleus emitting its 14.4 keV photon recoils and detunes
the line; bound in a crystal, with recoil energy below the phonon
quantum, the ENTIRE LATTICE absorbs the momentum — recoil-free fraction
of transactions where 10²³ atoms co-sign one payment, narrowing the
line to ΔE/E ~ 10⁻¹³. That collective co-signature is what made
Pound–Rebka's 2.45×10⁻¹⁵ (entry 27) resolvable. Model tie: a condensate
co-signing individual transactions is the mechanism grammar of our
medium's granule-scale behavior — measured here in steel. Grade:
calibration + mechanism cousin.

## 46. Atomic clocks and the SI second

The second is DEFINED as 9,192,631,770 Cs hyperfine periods (exact by
decree); optical lattice clocks (Sr, Yb) now hold systematic
uncertainty ~10⁻¹⁸ — they would disagree by one second over the age of
the universe. Model tie: these are the sharpest instruments in the
standing laboratory bet (any dark-sector coupling to atomic structure
would surface here first), and the R1/caustic-bit exhumation's
virial-static null (Atlas graveyard) leans on exactly their class.
Grade: calibration + standing-bet instrument.

## 47. Laser cooling — buying entropy with light

Derivation: Doppler-selective scattering damps motion until the
recoil-heating floor: T_D = ħΓ/2k_B. Rubidium (Γ = 2π×6.07 MHz):
**146 μK** (computed). Below it, sub-Doppler and evaporative tricks
reach the nK where BECs condense — every laboratory cousin of our
medium (Part I §10) is manufactured through this ledger: photons carry
the entropy out, one scattering receipt at a time. Grade: restatement;
the BEC supply chain.

## 48. The quantum Hall effect — resistance by counting

At quantizing fields, Hall resistance locks to R_K/ν with
R_K = h/e² = **25,812.807 Ω exactly** (SI 2019, by decree) — flat to
10⁻¹⁰ across samples, geometries, materials. Ledger reading: transport
by topological bookkeeping — the resistance is set by HOW MANY channels
(an integer) times a ratio of ledger constants, immune to the sample's
dirt. Companion receipt to the flux quantum and Josephson constant
(Part I §18): the three legal electrical units are all
counting-receipts. Grade: calibration.

## 49. BCS superconductivity — the joint account

Weak-coupling BCS solves the gap equation to a universal ratio:
2Δ(0)/k_B T_c = **3.53**, obeyed within ~10% by aluminum, tin, indium —
one number for every conventional superconductor, independent of the
material's chemistry. Ledger reading: electrons open phonon-brokered
joint accounts (Cooper pairs); the gap is the account-closure fee, and
T_c is where thermal auditing forces them all open. Census contrast
(Part I §18): gauged-U(1) condensate (Meissner, flux quanta) vs our
global-U(1) medium — cousins, not twins, and the dark photon door is
closed. Grade: calibration + contrast.

## 50. Debye solids — the phonon ledger at a lab bench

Derivation: quantized sound modes with linear dispersion in 3D give
U ∝ T⁴, hence **C ∝ T³** at low temperature — measured in every
crystal. This is the SAME integral this program ran for the pre-basin
medium (the w = 1/3 phonon-gas double-derivation, Part I §10): our
early universe is a Debye solid's arithmetic at cosmological volume.
Grade: calibration; the double-derivation's lab twin.

## 51. Plasma physics — screening, and why gravity can't be screened

Derivation: mobile charges rearrange to hide any test charge beyond
λ_D = √(kT/4πne²); waves below ω_p reflect — the ionosphere at
n_e ~ 10⁶ cm⁻³ mirrors radio under **f_p ≈ 9 MHz** (computed), which is
why shortwave crosses oceans. The structural contrast: screening
requires BOTH signs of charge; mass has one sign, so *no medium can
Debye-screen gravity* — the reason our census's "gravity is the only
account" has no screening escape clause, and the reason v1–v3's
screening machinery had to live in the scalar sector (and died there).
Grade: restatement + structural contrast.

## 52. Magnetohydrodynamics

Derivation: magnetic tension in a conducting fluid propagates as
v_A = B/√(4πρ); solar wind at 5 nT, 5 cm⁻³: **~49 km/s** (computed),
routinely measured in situ. The magnetized plasma carries its field
lines as frozen-in ledger lines (flux freezing = conserved circulation,
the gauged cousin of our medium's quantized winding). Grade:
restatement + kinship note.

## 53. Cherenkov radiation — paying a medium's local speed limit

Derivation: a charge faster than light's LOCAL pace c/n radiates into
the Mach cone cos θ = 1/(nβ); threshold in water (n = 1.33) for
electrons: **KE ≈ 264 keV** (computed) — the blue glow of reactor
pools, IceCube's entire detection principle. The contrast this file
owes its own history: Part I's medium is frictionless to light
(massless quanta hold no account it can bill); a REFRACTIVE medium
bills light's sources when they outrun the local settlement speed. Both
statements are bookkeeping; they answer different media. Grade:
restatement + house-history contrast.

## 54. Geometric optics as cheapest settlement

Fermat: light takes the stationary-time path — refraction is the
least-cost route between banks with different processing speeds
(Snell's law is the first-order condition; total internal reflection
above the water-air critical angle **48.8°**, computed). Grade:
restatement (the variational principle is the ledger's oldest law).

## 55. The diffraction limit

θ ≈ 1.22 λ/D: an aperture of size D can only distinguish directions to
one wavelength of phase across itself — resolution is phase-information
per aperture area. Kinship note: information billed by surface, not
volume, is the same accounting that runs the holographic bound (Part I
§17) — here it just prices telescopes. Grade: restatement.

## 56. Brownian motion — how the graininess was first proven

Einstein 1905: a pollen grain's diffusion D = k_B T·μ ties the visible
jitter to the INVISIBLE discreteness of the bath; Perrin measured D,
extracted Avogadro's number, and ended the atoms debate. Model tie,
direct: the granule-speckle ε-meter (the audit's sole surviving dice
instrument) is EXACTLY this argument at halo scale — read the
fluctuations, infer the medium's quanta. Perrin did it with pollen; the
program proposes it with stellar streams. Grade: calibration +
method ancestor.

## 57. Thermal escape — Arrhenius and Kramers

Rate = (attempt frequency) × exp(−ΔE/k_B T): the thermal credit market
prices barrier crossings exponentially, from chemical reactions
(doubling per ~10 K, the lab-bench receipt) to protein folding.
Companion to entry 44: same exponential, thermal loans instead of
quantum ones. Grade: restatement.

## 58. Critical phenomena — the ledger forgets denominations

At continuous transitions, microscopically alien systems share
exponents: liquid-gas water and uniaxial magnets both show
β ≈ 0.326 (3D Ising) — the RG statement that at criticality the books
keep only dimension and symmetry, forgetting every microscopic
denomination. House note: the φ-null (Atlas nulls) already used this
domain's honest employers (E8 criticality); this entry books the
universality mechanism itself. Grade: restatement.

## 59. Entropic elasticity — force from record count

Stretch rubber: the retracting force is −T·∂S/∂L — not energy stored
but CONFIGURATIONS destroyed; the receipt is thermodynamic and
kitchen-grade: rubber warms when stretched, contracts when heated,
opposite to metals. S = k ln Ω working a day job: the second law
(posting is cheaper than shredding, Part I §17) collecting rent at the
macroscopic scale. Grade: restatement with a kitchen receipt.

## 60. Planetary energy balance

Derivation: T_eq = [S(1−A)/4σ]^¼ = **255 K** for Earth (computed;
S = 1361 W/m², A = 0.29) vs the measured 288 K surface — the 33 K gap
is the atmosphere re-pricing outgoing settlements (absorbing thermal IR
and re-posting half downward). The planet's books balance at the top of
the atmosphere; where they balance sets everything below. Grade:
restatement with derivation.

## 61. Tidal dynamics and the Roche ledger

Differential gravity across an extended account: tides transfer
Earth's spin into the Moon's orbit (the 3.8 cm/yr receipt already
booked in the Atlas overnight-stream kill); inside
d = R(2ρ_primary/ρ_satellite)^⅓ self-gravity loses to the gradient and
moons become rings — Saturn's rings sit inside its Roche radius, the
receipt written across 300,000 km of sky. Grade: restatement.

## 62. 21-cm cosmology — a prediction-shaped entry

The dyad's m_e amendment is epoch-gated: varying_transition_redshift =
50 in every fit config — constants return EXACTLY to standard below
z = 50. Consequence, stated as a bet: the global 21-cm absorption
trough and the forming dark-ages/cosmic-dawn interferometry (REACH,
SKA-low) should see a STANDARD sky as far as our constants are
concerned; an EDGES-class anomaly, if ever confirmed, is not ours and
gets no retro-fit (the Atlas nulls' rule). Meanwhile the medium's
granule structure DOES live in the 21-cm forest's small scales — the
same P(k) territory as the Lyα squeeze the model already survived.
Grade: **exposure, epoch-gated by construction.**

## 63. Dark-matter direct detection — the third zero

LZ and XENONnT now exclude spin-independent WIMP-nucleon cross-sections
down to ~2×10⁻⁴⁸ cm² at tens of GeV — a nine-decade march of nulls
since the 1990s. The census (Part I §11) makes the model's vote
unconditional: the medium holds no EM/weak/strong account, so **every
direct-detection experiment stays null, forever** — the corollary of
standing bet #2, extended from the sky to the mine shaft. Confirmed
nuclear recoils from the dark sector kill the model outright; the
marching nulls are, so far, the quietest receipts the census owns.
Grade: **exposure, kill-only.**

---

## Part II census note

Part I mapped 24 domains; Part II adds **39 more** (25–63). Honest
count-keeping: the operator asked for 50 new domains *if possible*;
39 survived the quality gate (a derivation chain or a numbered
calibration receipt, re-derived at booking — no filler entries, per the
Atlas's headline-honesty rule). The census now stands at **63 domains**,
of which the exposures — the entries that can hurt us — are §28 (PPN),
§38 (τ_n in our BBN books), §62 (21-cm epoch gate), §63 (direct
detection), on top of Part I's five standing bets. The extended census
confirms the Atlas's original finding at larger n: the language is
exact everywhere it has receipts, and the bet's evidence class still
holds zero confirmed entries — faithful ≠ confirmed, at 63 domains as
at 14.
