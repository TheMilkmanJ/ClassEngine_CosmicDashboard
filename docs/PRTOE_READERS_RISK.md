# PRTOE — Reader’s risk summary

**Status (2026-08-05 currency):** evidence class is still **Laplace-marginal, not nested-sampling confirmed**.
The production bbnfix MCMC pair is **live and NOT bookable** (lcdm R−1 **0.049324** N=26294
t=2026-08-05T11:52:10 with **self-stop** / `converged: true`, so the control leg is ready; dyad R−1
**0.056889** @N=24677 t=2026-08-05T07:54:30 — **1.14×** stop / `converged: false`;
`book_bbnfix_when_ready.py` → **REFUSED** because one ready leg does **not** open the pair). Route-D live R−1 **0.728432**@N=8120
t=2026-08-05T12:54:11 (~**7.28×** stop 0.1) — not dual-gate. Offline GetDist GR is diagnostic only —
**not** booking authority. **Do not peek-book H₀.** PolyChord nested evidence is offline (waits for
cluster time). No headline posterior is bankable yet. Full chain table:
[PRTOE_CHAIN_TABLES.md](PRTOE_CHAIN_TABLES.md). Booking refuse card:
[`working_logs/_runs/bbnfix_booking_20260805_190348/`](working_logs/_runs/bbnfix_booking_20260805_190348/).

> *One page for an outside physicist. Falsify-first: nothing below is oversold. House terms decode
> in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality in
> [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md). Audience prep tracker:
> [working_logs/_AUDIENCE_PREP.md](working_logs/_AUDIENCE_PREP.md).*

## 1. What PRTOE is

**Pulford–Romsa Theory of Expansion** — a dark-sector cosmology of the expanding cosmos, not a
theory of everything. Local bound matter is ceded to the Standard Model; the domain is the diffuse
cosmic medium and its expansion imprints.

A two-field dark sector replaces ΛCDM’s separate dark matter and dark energy:

1. **dCDF** — one complex scalar superfluid: ground state is w = −1 dark energy; excitations are
   radiation-like early / CDM-like late.
2. **Electron-coupled scalar** — shifts the electron mass by ε ≈ 1.24%, active pre-recombination,
   screened off late.

Gravity is treated as induced/GR (no bare cosmological constant term as free input). The
modification to known physics is **one number, ε**, applied wherever atomic physics appears.

## 2. Strongest claims, graded

- **ε = c · f̄ · α_c = (9/10)×(2/π)×3α = 27α/5π = 1.2543%** vs fitted ~1.24%. **Not “zero free
  parameters” until all three factors hold.** Grade = **weakest parent**:
  - **f̄ = 2/π** — derived (winding ⟨|cos|⟩); sim 0.635 ± 0.026 confirms (+0.3%). The simulation is
    the check, not the source.
  - **c = 9/10** — counting assumption (not framework-forced). Conditional on ρ_Λ¼ = m_ν as a lock
    and equal channel weights. ε-blind ensemble 0.903 (−0.08σ) does not exclude 12/13 or
    charge-weighted 8/9 (0.30σ away).
  - **α_c = 3α** — pre-registered bet (P-2026-040); decided by the α_c instrument (zon_disp —
    **unconverged and not running**); last interim center sits ~2% above where data points.
    **Stack stands or falls with this.**

- **H₀ ~ 69.9–71.3** (CMB re-fit; ladder ceiling with SN sign ς = −1). ~Half the SH0ES gap; refuses
  the rest; pre-registered the TRGB side of the calibration dispute. *Mechanism at production grade,
  SH0ES-conditional. The statistical win ΔlnZ = +2.635 is a separate Laplace estimate — nested
  sampling is not live (§3c, §4).*

- **w = −1** as protected ground state — **one branch of a live fork**, not the only position:
  - **P-2026-018:** bare constant floor, w = −1 forever.
  - **Route-D:** floor thawing now, 1+w_floor(a) = thaw·a³, thaw ∈ [0.08, 0.14] → w₀ ∈ [−0.92, −0.86]
    today — and the coincidence file puts that era’s end at t_turn = ln(1/√A_s)/√(3/2) = **8.16 H⁻¹**,
    a ≈ 2.0–2.8. Route-D nests at the prior’s floor (thaw ≤ 0 recovers w = −1); **DESI DR3
    adjudicates**. Phantom crossing kills both.
  Honest headline: the model bets on rigidity while carrying a pre-registered thawing alternative;
  the coincidence file’s turnaround belongs to the *alternative*, not as a hedge on w = −1.
- **The multi-messenger single-ε lattice** — one amplitude at window-specific weights across CMB,
  BBN, 21-cm, and Koide, with no per-window exits. *Grammar/production*; individual windows carry
  their own grades (§3).
- **Koide protection** — the multiplicative-universal lepton coupling explains *why* Koide's Q
  survives a 1.24% mass shift (a real improvement; mainstream has no account). *Candidate throughout:*
  protection is derived; the reason Q = 2/3 at all (A = √2) is not. The assembled candidate chain
  (cascade-delivered sector-equipartition) was executed under its own pre-registered trial and
  landed in the death zone. The equivalence A = √2 ⟺ sector-equipartition stands as mathematics.
  A full candidate chain now exists (circulant kernel, existence theorem, thermal-boundary reading
  with one internal cross-check passed), still carrying one theoretical stage and judged by three
  lattice observables of a single SU(2) N_f = 3 campaign plus P-2026-051.
- **N_gen = 3 from Pauli finiteness** (str[k₁] = 16·N_gen − 48 = 0). *Derived conditional on
  ξ_H = 1/6*, an unmeasured Standard-Model input the balance requires; independent of the pairing
  sector. **Units (2026-07-29 harness):** SM alone is **str[k₁] = −1/2** in Visser’s normalisation;
  the corpus’s “−3” is the **Weyl-spinor deficit** (45 vs 48). Quote both. **Prior art (not a novel
  conclusion):** the same result — three generations and right-handed neutrinos at 48 Weyl fermions —
  is published in [Navarro-Salas 2024, arXiv:2403.13201, *Classical and Quantum Gravity*], from exact
  conformal symmetry (both trace-anomaly coefficients vanishing). The two are **not** independent
  confirmations: both reduce to N_½ = 4·N₁ over the same roster and need the same conformal-coupling
  premise. What is distinctive here is the route (finiteness at induced-Newton-constant order), not
  the conclusion.

## 3. Weakest links — stated plainly
- **(a) The dark-energy headline result's "+1.5%" is an artifact; its real prediction is +0.44% and
  candidate-grade.** ρ_Λ¼ = (9/2)α⁴τ·m_e is a real structural relation, and the corpus's τ = 0.345
  is the *observed* density inverted and rounded — so the quoted 1.5% is a rounding gap, not
  evidence. **τ does now have an independent source**, from the other end of the model: the Koide
  kernel's modulus is fixed by Parseval at 1/√2, giving τ = ½ln2 = 0.34657, hence T_c = 177.10 keV
  and ρ_Λ¼ = 2.2599 meV — **+0.44%**, with no cosmological input in the chain. **Read that as an
  existence claim and not a precision one:** the composite quartic maps to λ = 26–46, and the
  radiative correction on ρ_Λ¼ is bounded at 0.10–0.90% — comparable to the +0.44% gap itself
  ([PRTOE_cosmological_constant.md](PRTOE_cosmological_constant.md), the control-edge
  re-examination). The chain lands on the
  observed scale; it does not claim the two decimal places it lands to. That rests on one
  hypothesis (the charged-lepton √m thermally populated, which is what Q = 2/3 asserts) and is
  candidate-grade. One uncomputed lattice number decides the kernel τ — T_c/√σ for an
  SU(2), N_f = 3 dark sector. Ideal point-values **0.34657 / 0.34506** are the crown/null fork —
  **sky-limited** under living P-048 (even σ=0 ~0.98σ); **live falsifier is clause 4** (τ̂ outside
  [0.330, 0.370]; see risk (j)). **No lattice determination of that theory exists** (literature
  sweep, 2026-07-17; outward-facing note [PRTOE_lattice_note.md](PRTOE_lattice_note.md)); the best
  inference bracket from measured neighbours (SU(2) N_f = 2: 0.483(23) deconfinement, 0.36–0.48
  chiral; SU(3) N_f-dependence) is **≈ 0.39 ± 0.05, centred above the model's 0.34657** — the model's
  value sits at the bottom edge, needing both the chiral (not deconfinement) transition and
  near-maximal suppression. One SU(2)-specific fact helps: the chiral and deconfining transitions
  decouple in SU(2), so the chiral T_c can legitimately sit below the Polyakov number.
- **(b) BBN is adverse-leaning under the standing configuration, and worst in helium.** The
  committed genesis residual (the ζ window) eases deuterium without healing it — D/H reads
  **−2.5…−1.4σ** from Cooke on the quotable budget, up from −2.9σ before the residual — while Y_p
  pays at **+1.3…+2.0σ** vs Aver and the EMPRESS fork worsens to **+3.8…+4.4σ**. The joint p is
  **0.02–0.08** on that budget, reaching 0.12–0.21 only if the full ~3.5% inter-nuclear-code spread
  is folded in. There is no healer available to the electron-coupled scalar (the Majoron couples to
  lepton number, quarks carry none), and that code disagreement plus the helium Aver/EMPRESS fork
  are the verdict's two hinges — the residual shifts every column without changing which one decides.
- **(c) The H₀ evidence is SH0ES-conditional and marginal.** ΔlnZ = +2.635 is a **Laplace** estimate
  (Hessian-from-MCMC). Nested sampling — the confirmer that would make this robust — is
  **unaffordable on this hardware and not running**; it waits for cluster time. The +2.635 crosses
  the pre-registered win line only slightly, inside the estimator's own systematic error; without
  SH0ES the model does not win. The easing is shared by the whole varying-m_e model class — it adds
  no independent evidence for the superfluid ontology.

  **A stale Laplace should not headline while production chains are still open.** That is why the
  July matched-pair snapshot is kept on the record even though it was **a wash, quotable in neither
  direction.** Best −logpost stood at **1377.89 (model)** against **1379.79 (ΛCDM)** — nominally
  1.9 log units the model's way — but that figure was worse than unconverged: **one rank of three.**
  Checked the same day (`scripts/rank_basin_diagnostic.py`), the model's three parallel chains sat at
  best fits of **1377.9, 1610.6 and 1440.6**, with H₀ = 69.5 / 64.0 / 64.8 and dcdf_rho_inf =
  0.700 / 0.595 / 0.635 — **three different basins, separated by up to 317 standard errors on a
  single parameter (H₀).** Honest rank separation on that snapshot, with ranks truncated to the
  shortest and autocorrelation accounted for (`scripts/rank_separation_ess.py`; τ ≈ 26–46 → ESS
  ~6–9 per rank-half), is **317 s.e.** The reference chains on that snapshot were **consistent with
  a single basin** on the same measure (worst separation **1.6 s.e.**). They remained unconverged
  for a clearer reason: with τ ≈ 23–68 each rank-half carried only ~5–19 effective samples, which is
  what R−1 = 1.011 was reporting. The cause was diagnosable: **acceptance sat at 5.3–6.2% for the
  model and 8.5–8.9% for the reference, against a ~25% target** — proposal poorly matched to the
  posterior; the rank with the *most* samples (1663) sat 233 log units *worse* than the rank with
  the fewest. *(Which counter to read: the sampler's own accepted/steps. The `.progress` column also
  named `acceptance_rate` reports ≈0.97; that is stored rows over total weight, pinned near unity by
  oversampling, and does not diagnose proposal health. Verified on that era's reference chain:
  2154/2221 = 0.970 against 745/8018 = 9.3%.)*

  **Why the proposal was never re-learned on that July run.** Learning is a **collective MPI
  checkpoint**: every rank must reach a multiple of `learn_every` = 40·d accepted samples before any
  proceeds. With d = 13 that is **520 per rank**; the three ranks held **467 / 1684 / 658**. Ranks 1
  and 2 announced ready; rank 0 never did. **"All chains are ready" never appears**, no convergence
  statistic is computed, and that run's `.progress` file is empty. Two ranks waited indefinitely for
  a third 53 samples short. July established: **the proposal was never re-learned and the three
  ranks never merged.** Reseeding the covariance from the good basin worked: acceptance 5.3–6.2% →
  31.2–31.9%. Three further reasons forbade banking even a merged best-fit then: the model had
  **1.79× more samples** (best-so-far favours the longer chain); **neither chain was converged**; and
  **best-fit is not evidence** — it carries no parameter penalty; Δln Z is what decides.

  **As of 2026-08-05 (§4):** a later matched relaunch **merged the basins** (every sampled parameter
  agrees across the three ranks to within ~0.6 within-chain s.d.) and remains *not bookable*.
  Progress stamp: lcdm twin R−1 **0.049324** (N=26294, t=2026-08-05T11:52:10, checkpoint
  `converged: true` — control leg ready), dyad R−1 **0.056889** (N=24677,
  t=2026-08-05T07:54:30 — **1.14×** stop, checkpoint `converged: false`); booking script
  **REFUSED**. One ready leg does **not** open the pair.
  **No peek H₀.** No best-fit comparison from this pair is bankable. The standing evidence number
  remains the marginal, SH0ES-conditional **Laplace** estimate +2.635 — the wrong kind of number to
  lead with. Nested sampling is still offline. Authority: `scripts/book_bbnfix_when_ready.py`;
  table freeze [PRTOE_CHAIN_TABLES.md](PRTOE_CHAIN_TABLES.md).
- **(d) The electron-coupled scalar's thermalisation problem — adjudicated (2026-07-18): the
  recorded configuration is BBN-fatal; one repair branch survives, at a named price.** The
  non-thermalisation escape was built and adversarially tried: **as recorded** (the electron-CW
  scalar at v ≈ 175 keV), the coupling that sources ε thermalises the dark sector (Γ/H ~ 10¹⁷;
  ΔN_eff ≈ 1.1–15 depending on the sector's attachment) — confirmed at 10⁸–10¹⁷ margins, no escape.
  **The surviving branch** re-homes the scalar at a high decay constant (~100–500 TeV):
  thermalisation gates clear by 10⁸–10⁹, the BBN ramp's clock survives, the induced fifth force is
  closed by the model's own environmental gate (which the recorded configuration needs ~10⁸-worse
  for electron g−2 regardless), and the branch predicts **ΔN_eff ≈ 0.06–0.24 (the committed ζ
  window) — a CMB-S4 detection target**, its own falsifier. The price: a new ~100-TeV-class
  input, the scalar-as-chiral-condensate identification drops (its consilience must be
  re-priced), and the windowed BBN books re-run.
  The high-f configuration is the standing one. Its BBN books: the committed ΔN_eff residual
  moves D/H toward Cooke without reaching it (−2.9σ → **−2.5 to −1.4σ** on the quotable budget)
  while Y_p pays (+1.1σ → **+1.3 to +2.0σ**) and the EMPRESS fork worsens to **+3.8 to +4.4σ**;
  the joint p reads **0.02–0.08** (0.007 without the residual), or 0.12–0.21 if the full inter-code
  spread is folded. The shift is hostage to its own falsifier: CMB-S4 must see
  ΔN_eff ≈ 0.06–0.24. Remaining exposure: the gate's chameleon/Casimir/EP checklist, and the
  helium Aver/EMPRESS fork.
- **(e) A_s, n_s, and the thermal O(1) coefficient are un-built or frozen candidates** — the A_s
  closed form is the corpus's boldest standing claim, frozen into the production configs by design
  (not by a converged posterior). E2E Track A grades the imprint path (γ\*/c_chop candidate-closed;
  B2 tilt route closed negative); residual risk remains on the counting mechanism and freeze decision.
- **(g) The gate's energy bookkeeping is unpaid, and one endpoint is excluded.** The electron's
  rest energy differs across the screening transition by 6.4 keV. If gas crosses that transition
  ballistically it is heated by ~2 keV per particle — an entropy floor an order of magnitude
  above what groups and clusters show, which would be fatal. The transition is
  a phase of the medium answering the local curvature — it re-arranges in place rather than
  standing as a surface to fall through — which suppresses the pickup by the ratio of gas speed
  to the medium's own sound speed (about one part in forty). That brings the heating to ~50 eV
  per particle and the entropy contribution to ~50 keV cm², under the 100–300 keV cm² floors
  groups actually show. The fast end is now bounded too: even at merger-shock speeds
  the fraction traversed stays near seven per cent, so the contribution never exceeds a few per
  cent of the shock's own heating — real, but hiding inside a larger effect that the same events
  produce, so it neither threatens the model nor tests it. (One consequence
  is already on the record: S₈ is not delivered by this channel — it rests on the pre-registered
  rotation-shed parameter, graded by a chain whose full restart is queued behind the running
  production pair.)
- **(h) Two independent constraints now bear directly on the ultralight mass, and both are
  unpriced.** That mass is fixed by the onset clock and cannot float. (i) The central soliton
  it implies carries about 3×10⁶ solar masses within one parsec of the Galactic Centre —
  comparable to the entire extended mass observed there, which the stellar population already
  accounts for. (ii) It puts black holes between roughly **6×10⁸ and 3×10⁹** solar masses inside
  the superradiant band, where they should be spun down, while several black holes in that
  range carry high measured spins. Neither is a computed exclusion yet; both are real, both
  are now named, and either could close the sector. *(The mass itself is firm on the onset clock —
  mass grade = onset clock plus at most one unresolved consistency check: ξ is defined from m;
  Schive unresolved; superradiance is an exposure, not a pin. Three independent *uses* fix it so
  the exposures cannot be relieved by moving it; see
  [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).)*
- **(f) Code-vs-theory gap, narrowed (2026-07-23 / rechecked 2026-07-30).** `dcdf_dyad_link=yes`
  derives `varying_me` from the amplitude stack at input time; density-gate screening is coded;
  thermodynamics consumes varconst tables (no dark-sector equations *inside* thermo — by design).
  What remains for S₈: re-validate with conversion hierarchy on (routeD); conversion *linear* perts are implemented 2026-07-30 when `dcdf_conv_g>0` (off on headline chains);
  spatial δm_e is not evolved (background-only varconst — fine for linear CMB, not for halo-scale
  predictions). Fixed-ε configs test the harder zero-extra-parameter case; sampled-ε is the softer
  Occam test. The CLASS source still does not compute the electron-coupled scalar’s m_e shift *from*
  the dCDF dynamically at runtime — the link is at input-time freeze — so the “one linked superfluid”
  is partially asserted rather than fully evolved.

- **(i) The evidence configuration sits off the model's own onset identity.** The transition epoch is
  frozen at z_on = 3.5619×10⁷ where the H = m identity gives 4.03×10⁷ — 0.053 dex, which under the
  same clock is a **28% difference in the dark fluid mass**. That mass is committed across three
  independent uses — the onset clock, the galactic cores, the superradiance band — so it cannot
  retreat to fit, the identity is the model's value, and the frozen setting is a profiled offset,
  disclosed in the config as a "FAST-FUDGE" priced at χ² +7.4. **The comparison therefore grades a
  point near the model rather than the model's stated configuration**, and its result needs reading
  in that light. The chain named to arbitrate the freeze is dead — unresumable across the classy
  rebuild — and its full restart is queued behind the running production chains.

- **(j) The lattice crown/null fork cannot currently resolve the headline precision claim.** P-2026-048’s
  standing prediction is the kernel’s **0.34657**; the observation-inverted null is **0.34506**
  (inherits ρ_Λ ±0.449%). They sit only **+0.44%** apart; even a σ=0 lattice separates them by only
  **~0.98σ**, so clauses 2/3 are **sky-limited**, not lattice-limited — lattice precision alone does
  not score CONFIRM/KILL on the 0.44% gap under present ρ_Λ error. **What remains fully executable is
  clause 4** (τ̂ outside the fixed prediction window without needing the null); neighbour inference
  **0.39 ± 0.05** sits above that window, so the falsifier is live. Ordinary 1–3% lattice work scores
  neither way on the crown/null fork. Current decision rule is clause 4 + sky-limited crown/null,
  not a ±0.02 tolerance window that would confirm anywhere inside it.

  **And the model carries a second estimate of τ that disagrees with its own headline.** The
  kernel gives τ = ½ln2 = 0.34657 from Parseval once Q = 2/3. But scaling the
  known lattice anchors down to SU(2) with N_f = 3 — the corpus's own "dof-family" reduction, ~42%
  convention-clean — gives **τ ≈ 0.355–0.382, centre ~0.36**. Since τ scales ρ_Λ¼ *linearly*, that
  band puts the dark-energy scale at **+2.9% to +10.7% above observation, centre +4.3%** — roughly
  **ten times** the +0.44% the headline quotes.

  Stated fairly in both directions: the dof-family figure is an estimate from scaling, not a
  measurement, and `PRTOE_DERIVATION_HUNT.md` notes it "points the right way on physics"
  (N_f/N_c = 1.5 against SU(3)'s 1.0). It is not evidence the kernel is wrong. **But it is the
  model's own independent handle on the same quantity, and it does not agree with the kernel to
  anything like the precision the headline advertises.** A reader comparing +0.44% against a
  self-consistent chain should know the chain's other estimate of its key input says +4%.

- **(k) The electroweak anchor is advertised far tighter than its own construction supports.** The
  hierarchy chain quotes M_anchor = 1576 GeV against 4πm_H = 1574, "+0.14%". Two ambiguities the
  file itself records make that precision unearnable. §6d carries a **factor-2 convention** (the
  exact gap-equation solution gives 3153 GeV; the recorded figure absorbs the two). And §6f is
  named in its own file as *"the single largest exposure in the hierarchy chain"*: the gap
  equation's kernel is electromagnetic — Coulomb exchange, Thomas–Fermi screening, e² = 4πα_c —
  while the coupling is evaluated at zero momentum and not allowed to run, eighteen orders below
  the pairing scale. **Both readings cannot be held at once, and the chain currently holds both.**

  Horn (a) of that fork ("just evaluate α at the pairing scale") **double-counts** — §6c already
  carries the medium's polarization explicitly as a Thomas–Fermi mass, and the screening it applies,
  ln(1+1/b) = 4.287, is **62× the entire QED run to the Z pole**. Separately, §6e settles the
  constituents as *compensated* rather than uncharged (n_electron = n_hole, charged carriers), so a
  residual Standard-Model run survives on top of the screening and costs a further **×5.6** —
  adverse. The standing band, with the O(λ) pair computed (the crossed box c = 0.789 and its Fock
  companion a = 0.281, both acting downward), is **0.55–1.78 TeV** (the hierarchy file's own §6d
  table), with 4πm_H toward its top edge — and the §6f run question above remains the chain's
  largest single exposure, sitting outside that band's accounting. With ∂lnM/∂lnk = 33.5, quoting
  1576.1 rather than 1576 would need k to eight digits, which nothing supplies.

  **The supportable claim is that a construction carrying no electroweak input lands at the
  electroweak scale within a factor of a few, every named residual adverse.** That is non-trivial
  and worth reporting. It is not a sub-percent result, and §6d's own phrase — "a factor-of-a-few
  band" — already said so before this page did.

## 4. Current evidence class
**Flat / suggestive, SH0ES-conditional, Laplace-marginal.** One positive result (ΔlnZ = +2.635) that
crossed a pre-committed threshold but adds no independent evidence for the ontology. **It stands
without its confirmer.** The zero-free-parameter nested-sampling comparison against ΛCDM — the only
thing that can make this robust — costs 9.8 h per iteration on available hardware (163 days to a
first checkpoint). That run has been **ended** and waits for cluster time; **it is not live.** A
reader should take the evidence class as: one marginal Laplace estimate, whose margin over the win
line is smaller than the estimator's own systematic, with **no nested number in prospect**. The
verdict now depends on the MCMC chains the Laplace is computed from — so their convergence, not a
separate nested referee, stands between the model and its headline evidence claim.

**The scoreboard, stated bluntly (2026-08-02).** Zero preregistered predictions have been
confirmed by data that postdates their registration — every "confirmed" grading in the registry
is consistency with data that existed when the bet was placed. The one column where the model
already faces adverse data, it is losing: primordial deuterium at −2.9σ on the tightest
published error budget, defended by a registered nuclear-rate bet (P-2026-058) that ΛCDM
largely shares. The headline fit comparison is unquotable by this corpus's own ruling (chain
table below). And the nearest calendar events are likelier to wound than confirm:
ΛCDM-conditional Σm_ν upper limits are descending through 61.4 meV from above. Pay dates for
the bets that could genuinely confirm something: JUNO ~2031–32 (the funnel-edge inputs),
ton-scale 0νββ in the 2030s, CMB-S4 (ΔN_eff, the Majoron coupling), HL-LHC (the anchor band),
a LUNA-class d(d,n)³He measurement (the deuterium bet). Until one of those pays, every
validation in this corpus is internal. Two companion documents carry the statistical exposure
a skeptic will raise first: [PRTOE_TRIALS_FACTOR.md](PRTOE_TRIALS_FACTOR.md) (how large the
closed-form search space was, counted from the failures ledger's own records) and
[PRTOE_INDEPENDENCE_AUDIT.md](PRTOE_INDEPENDENCE_AUDIT.md) (which multi-way agreements are
genuinely independent and which collapse).

**That distance is measured.** No chain in this corpus has ever booked at its own stopping target
(R−1 = 0.05 **and** `converged: true` for the production bbnfix pair; R−1 = 0.1 for Route-D).
Status as of **2026-08-05** ([PRTOE_CHAIN_TABLES.md](PRTOE_CHAIN_TABLES.md); booking gate
**REFUSED**):

| chain | last recorded R−1 | N (progress) | `converged` | live? | note |
|---|---:|---:|---|---|---|
| `dyad_mnu_bbnfix` | **0.056889** | 24677 | **false** | **yes** | **1.14×** stop; t=2026-08-05T07:54:30 |
| `cmp_lcdm_mnu_bbnfix` (ΛCDM+mν twin, 3 ranks) | **0.049324** | 26294 | **true** | **yes** | control leg ready; pair still **NOT bookable**; t=2026-08-05T11:52:10 |
| `cmp_prtoe_routeD` (thaw fork, 3 ranks) | **0.728432** | 8120 | **false** | **yes** | ~**7.28×** stop 0.1; not dual-gate; t=2026-08-05T12:54:11 |
| `cmp_prtoe_conv_desi` | 13.25 | — | — | **no** | unproduced; last write 2026-07-22 |
| `cmp_prtoe_zon_disp` | 17.81 | — | — | **no** | collapsed; seed ready, owner restart |
| `cmp_prtoe_zon` | 40.36 | — | — | **no** | stopped since 07-12 |
| `dyad_mnu_mcmc` | *none recorded* | — | — | **no** | diagnostic archive only |
| PolyChord nested evidence (`cmp_prtoe_fixed` et al.) | — | — | — | **no** | ended 2026-07-20; waits for cluster time |

**Booking gate (bbnfix only):** both legs R−1 &lt; 0.05 **and** checkpoint `converged: true`, then
only `python3 scripts/book_bbnfix_when_ready.py`. Offline GetDist max GR (~0.086 dyad / ~0.07 lcdm)
and crude param R−1 are **UNBOOKABLE** diagnostics. **No peek H₀** from live chains.

Two consequences a reader should carry. **First**, the parameter tables in
[PRTOE_CHAIN_TABLES.md](PRTOE_CHAIN_TABLES.md) that are formatted as posterior summaries are not
posteriors for any unconverged run; their 68% limits are lower bounds on the true width, because a
wandering chain has not visited the tails that would earn them. **No GetDist table exists yet for
the three live runs** — they join only at stop via the booking script.

**Second**, intermediate best-fit gaps are not verdicts. In July the model briefly sat ~41 log units
*behind* ΛCDM+mν on an identical stack, then the leading rank descended to roughly even (−logpost
~1379 each way). Descent was still active when that snapshot closed. Neither figure was bankable.

**The basin problem has since resolved.** Both production chains were relaunched with three ranks
each and matched settings; burn-in cleared; every sampled parameter now agrees across ranks to
within 0.6 within-chain standard deviations — one basin, genuinely mixing. What remains is
statistics, not pathology: progress R−1 (lcdm **0.049324**@N=26294 with self-stop / dyad
**0.056889**@N=24677 — **1.14×** stop), and the pair gate is still shut because dyad has not
self-stopped under the bar. Honest present state: *mixed-ready but **not bookable***. Anyone quoting H₀ or an evidence number from this pair
before both legs self-stop at R−1 &lt; 0.05 is quoting noise, either way.

## 5. What would kill it (pre-registered)
1. DESI DR3 confirms w ≠ −1.
2. The local distance ladder settles H₀ ≥ 72.0 with systematics convincingly excluded (no known
   repair exists in this model class).
3. The α_c instrument lands > 2σ off 3α.
4. Any confirmed dark-sector non-gravitational signal — decay line, annihilation, scattering (the
   shift symmetry forbids all; one confirmed event kills the dCDF identification outright).
5. A robustly measured Σm_ν incompatible with 61.4 meV / normal ordering, or inverted ordering.
6. The BBN joint tension crossing the decisive bar (D/H toward −3.3σ) once the inter-code systematic
   is resolved.

*The single sentence: the model is a narrow, falsifiable reinterpretation whose one statistical win
is SH0ES-conditional and rests on a marginal Laplace estimate with no nested confirmation in
prospect, whose headline dark-energy number is a sourced structural relation that lands on the
observed scale without claiming the precision it lands to, and whose fate rides on chains that have
yet to converge, a lattice number no one has computed at the precision required, and DESI.*

---

## Claims ledger & discipline (2026-08-05 currency) — above story-grade discipline

| # | Claim | Grade | Evidence | Residual / blocker |
|---|---|---|---|---|
| 1 | Evidence class Laplace-marginal; not nested-confirmed | **honest constraint** | banner; §3c | **OPEN-MACHINE:** nested offline; bbnfix not at gate |
| 2 | ε stack grade = weakest parent (f̄/c/α_c) | **complete-conditional** | §2 | α_c instrument offline |
| 3 | H₀ 69.9–71.3; half gap; residual owned | **machine-backed** provisional | §2 | SH0ES-conditional; **not** from live bbnfix tables |
| 4 | ρ_Λ existence not precision (+0.44% in τ-space) | **complete-conditional** | §3a | Lattice + quartic past control |
| 5 | Production bbnfix pair one basin; lcdm R−1 **0.049324**@N=26294 t=2026-08-05T11:52:10 with `converged:true` (control leg ready) / dyad **0.056889**@N=24677 t=2026-08-05T07:54:30 (**1.14×** stop, `converged:false`); pair still **NOT bookable** | **machine-backed** status | §4; CHAIN_TABLES freeze; book script REFUSED | Statistics, not pathology; **no peek H₀** |
| 6 | Kill list §5 pre-registered | **registered** | §5 | DESI, ladder, α_c, DD, ν, BBN |
| 7 | Page is audience risk summary | **meta** | whole file | Not a derivation |
| 8 | BBN ε 2σ ceiling **ARITHMETIC VERIFIED (internal)** (3.196%≈3.20%); **EXTERNAL WIN PENDING (no DOI)** — not a chain booking | **internal arithmetic** | hard-wins table | Does **not** close bbnfix; not a public external win until DOI |

**Non-claims:** not a bankable posterior; not nested evidence win; **not** bbnfix bookable; **not** H₀ from live chains; **not** Page closed.

**Triage:** elevate-in-place. Physics ceiling: honest risk map; evidence **OPEN-BLOCKED** (bbnfix gate).
