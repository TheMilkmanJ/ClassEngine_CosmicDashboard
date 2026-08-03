# The T-file residual-debt census (2026-07-18; synced 2026-07-28; table hygiene 2026-08-02)

> **2026-07-28 sync** — rows paid or moved since the census was cut:
> * **T14, link 4 (the census's heaviest pair): HALF-PAID and the other half in flight.** The
>   poloidal circulation's sign-lock is COMPUTED (the v3 sign-lock run: exact parity pair,
>   five rings, five correct signs — task #19 closed); the toroidal-vs-poloidal relative sign
>   (the helicity bilinear's sign, this row's exact ask) is the 3D fork experiment running now
>   (`ring_toroidal_3d.py`, both candidate readings in one run).
> * **T13's open item (the D/H error budget's reproducibility): PAID** — the deuterium row's
>   §2b now computes the theory error inside the pipeline (±0.0240 from PRyM's own nuisance
>   pulls), prices the compilation systematic reaction-by-reaction (d(d,n)³He at 94%), and
>   tables the four width constructions with the booking question stated. The absolute row is
>   registered as P-2026-058.
> * **T11's MACHINE column: PolyChord ended 2026-07-20** (archived; the referee calendar
>   carries the 163-day costing); the evidence verdict rides Laplace-from-MCMC on the bbnfix
>   pair, with the z_on-identity rerun prepped and self-queuing (task #23).
> * **T3's MACHINE column:** the Σm_ν joint fit is now the bbnfix pair (relaunched fresh
>   2026-07-26 on the production-faithful D/H prior — the deuterium-inclusive joint fit,
>   task #27); dyad R−1 ≈ 4 and falling.
> * **The amplitude count (corpus-level):** the shot-noise normalization is DERIVED at
>   candidate grade (spine §23.5 — channel, count, measure; N = 1.003 ± 0.005 data-locked);
>   the screening host is settled on standard ground with the formation-epoch number paid by
>   the hierarchy factor (hierarchy §6n; tasks #15, #16 closed). The winding average's
>   high-statistics check is delivered and passing (P-2026-041 annotated; f̄ = 0.6314 ± 0.0033
>   at the many-turn members).
> * **The area-law regulator O(1) (corpus-level row): PAID 2026-07-20** — the entropy file
>   records the entanglement-side check closed structurally (the conical deficit makes the
>   area term the same heat-kernel coefficient that generates 1/G; the quarter is
>   regulator-independent). The true residual is re-named there: the ROSTER EXTENSION —
>   the coefficients are the minimally coupled scalar's, and spin/non-minimal content splits
>   the two divergences (now tracked as its own task).
> * **T9's haloscope edge cases: PAID** — the direct-detection file prices the class
>   ("NULL, forever": EM-neutrality at 37–47 orders under unit charge) including the
>   local-halo-density edge; nothing remains that the file does not carry.
> * **T7's dataset question: ANSWERED 2026-07-28** (the file's addendum) — no dataset
>   tabulates the winding average; the observable exists latently in disk-referenced spiral
>   interferograms; the named target is a percent-level reanalysis of archived images.
> * **The area-law ROSTER EXTENSION: PAID 2026-07-28** (entropy §3 extended;
>   `scripts/area_law_roster_extension.py`) — per-class on literature-standard results:
>   fermions exact (no contact term), the gauge sector restored by the Donnelly–Wall
>   edge-mode identification of Kabat's term, the conformal Higgs dropping out under the
>   corpus's own ξ = 1/6 finiteness condition. 63% of roster units unconditional; 37% on
>   the one named commitment (edge modes = horizon entropy); its rejection is the kill.
>   The corpus-level area-law row is now fully discharged at candidate grade.
> * **T2's row: CLOSED 2026-07-28 (both halves).** The saturation corrections were already
>   paid 2026-07-20 (the quench computation: 85 decades short of shielding; bosenova paces
>   rather than stops; the band's evolution is a free scalar's, as P-2026-034's note
>   carries) — the census's phrasing predated it by two days. The data confrontation is
>   assembled the same day (the T2 file's addendum): featured in the predicted direction,
>   degenerate with chaotic accretion, above-band recovery named as the discriminating
>   signature, NewAthena the referee.
> * **The BipoSH estimator (T5/T12's shared instrument): BUILT 2026-07-28**
>   (`scripts/biposh_estimator_pass.py`; the T5 file's addendum) — cubic selection emerges
>   from the projection (103/103 components), the template tower is the cubic L = 4, 8, 12
>   sequence, and the grading refines 1.4 → 1.68 with the excess identified as the
>   m-dependent diagonal anisotropy. The data application (pattern-frame a_ℓm) is the
>   external calendar item, as this census always framed it.
> * **Remaining verified-open census debts, tracked as tasks:** the matched lensing fit
>   (#32 / docket #161) — pipeline-class, queued behind the running chains and the MCMC cap.
>   *(2026-08-02: the EDE fairness pass is PAID — T11 file 2026-07-28; docket #166 closed.)*
>
> **2026-08-02 table hygiene** — the header sync above already recorded payments that the status
> cells still carried as OPEN/MACHINE. Cells below are brought into line (no new physics claims):
> T2 both #31 halves closed; T7 dataset question answered; T9 haloscope edges paid; T11 PolyChord
> ended and EDE fairness paid; T12 BipoSH estimator built (data application remains external);
> T13 D/H error-budget reproducibility paid; corpus-level area-law row fully discharged at
> candidate grade (regulator O(1) + roster extension).

*What each threaded owed-file still owes, after cross-checking every item against work paid
elsewhere in the corpus. Four states: **PAID** (here or elsewhere, with the pointer),
**MACHINE** (waiting on a run, not on work), **WATCH** (external progress to track), **OPEN**
(a real computation still owed). The point of the census is that a debt paid by another route
should stop being counted as a debt.*

| file | PAID / where | MACHINE | WATCH | OPEN (the real residue) |
|---|---|---|---|---|
| **T1 galactic atoms** | — | α_c posterior → r_1s | — | **priced, and it became the sector's leading test** — the constraint is at parsec radii, not the S-stars, where the soliton is comparable to the Centre's whole extended mass budget (task #98) |
| **T2 SMBH atoms** | superradiance prong audited (blackholes file); **window COMPUTED** (P-2026-034 band); **λ-saturation/quench PAID 2026-07-20** (85 decades short of shielding; free-scalar band — `scripts/superradiance_quench.py`); **spin-mass data half assembled 2026-07-28** (T2 addendum; task #31 both halves closed) | α_c posterior → α_g | NewAthena / spin catalogs (above-band recovery is the discriminator) | — |
| **T3 neutrino home** | v_L scope — the three-corner test, the Boltzmann pass, and the tenth-channel operator settle it (both corners lane-clean, CMB-S4 the selector) | the Σm_ν joint fit (dyad_mnu, R−1 = 0.176 — closest to converging); the double-duty check (conv_desi, burning in) | KATRIN / oscillation windows | — |
| **T4 S₈ growth** | the entropy floor's own reading — killed as the S₈ delivery route and re-homed to the pre-registered shed (failures ledger) | conv_g posterior — **the chain is alive again since 2026-07-18**, superseding this file's dead-chain flag | DESI w(z) policing | the matched lensing-likelihood fit (DES/KiDS proper, not the S₈ point) |
| **T5 low-ℓ** | matched-circles; **the cavity C_ℓ computation — RUN 2026-07-18: right shape, 3–5× too little depth at permitted sizes (ledger re-grade)**; **BipoSH estimator BUILT 2026-07-28** (`scripts/biposh_estimator_pass.py`) | — | BipoSH data application (pattern-frame a_ℓm — external calendar) | all three escapes computed and dead; **the whole power-spectrum route is ungradeable** (total S/N **0.16** over ℓ = 2–6, depth and shape alike) — the test moved to the off-diagonal correlation structure, regenerated ISW-inclusive on a retained script (**S/N 1.4**, retention 90% at the floor; `scripts/torus_lowell_pattern.py`). Grading now rides the built estimator (1.4 → 1.68 on the retained generator) rather than the 2.2σ first-pass report |
| **T6 Koide** | the week's arc: the kernel reformulation, the existence theorem, the sealed trial's verdict, the deviation lock | — | Belle II (P-2026-051); the lattice triple | the twist transfer's pacing step; the sign-chain walk |
| **T7 lab cousins** | **specified 2026-07-18** (three proposals + mapping table); **dataset question ANSWERED 2026-07-28** — no tabulation of ⟨\|cos\|⟩; latent in disk-referenced spiral interferograms; named target is percent-level reanalysis of archived images | — | ring-BEC reanalysis / literature | — |
| **T9 direct detection** | item 1 (σ ≈ 8×10⁻¹⁵⁰ cm²); **haloscope edge cases PAID** (#164; T9 file — both corners strengthen the bound; null stated against the weak end) | — | the neutrino-fog calendar | — |
| **T10 gravitational waves** | **the chiral amplitude — COMPUTED 2026-07-18: a structural null** (carrier 8–11 orders under every instrument) | — | PTA astrophysical consistency | — |
| **T11 Hubble** | the instrument pricing gains a channel: the dark-ages offset is now registered (P-2026-050); **EDE-comparison fairness pass PAID 2026-07-28** (T11 file; docket #166 — competitors steelmanned; EDE outscores this class on every column); **PolyChord ended 2026-07-20** (archived; 163-day costing — not a stall) | Laplace-from-MCMC evidence verdict waits on production-chain convergence (#155) | TRGB (P-2026-001) | — |
| **T12 radio lattice** | dark-ages forecasts — the numbers are registered (P-2026-050: +0.40 MHz at the z ≈ 87 trough); the WHIM cross-check is priced by the gate's energy bookkeeping (~50 eV per particle); the synchrotron row's weight convention is declared in the lattice table (fixed-field −1ε, fixed-energy −3ε); **BipoSH estimator BUILT 2026-07-28** (`scripts/biposh_estimator_pass.py`; T12/T5 addenda) | — | below-z = 50 null record; BipoSH data application (external) | — |
| **T13 fingerprint** | items 1–3 all paid (the ε-epoch table; the referee calendar; the joint-likelihood build); **D/H error-budget reproducibility PAID** — deuterium row §2b / #157 (theory error inside the pipeline; compilation systematic priced; standing width ±0.0476, row −2.94σ; P-2026-058 registers the absolute-row bet) | — | the helium fork | — |
| **T14 IGMF helicity** | item 2 (the hint's status pass); **the seeding step's conversion law** — the Harrison battery's coefficient enters the helicity squared, so sign(helicity_B) = sign(H_kin) exactly and no convention survives (task #158); **link 5 closed NEGATIVE** (#154 joint draw) | — | Fermi/parity-odd claims | **sole surviving sign debt is link 4's sign(H_kin)** — kinetic helicity is a linkage, and neither recorded rotation supplies one; the handedness lives in the roll-up's helical ring (bilinear in poloidal and toroidal circulations). Poloidal half computed (v3 sign-lock); toroidal half is the 3D fork experiment (`ring_toroidal_3d.py`). Link 5 is permanently unreadable through the joint draw, not pendingly |
| **T15 indirect detection** | item 1 (tree σv = 0; ceiling ~10⁻¹⁵⁴ cm³/s) | — | GC-excess pulsar progress | — |
| **T16 LSS parity** | item 1 (short by ~7 orders; the bet-against-the-anomaly registered) | — | DESI 4PCF | the axis-correlation check if the signal firms |

## The corpus-level owed items — outside the T-files

*A sweep of the whole shelf for the word finds five more, which no thread owns. They are listed
here so the count is the corpus's, not just the threads'.*

| item | where it is named | state |
|---|---|---|
| ~~the dark-energy value's O(1) coefficient~~ | cosmological constant §4b | **DISSOLVED 2026-07-18** — the two doors stand in exactly the derived phase-space ratio (0.04% agreement); what looked like a missing coefficient was the flagship's own τ gap measured against the wrong door. No separate number to build; the lattice's τ answer fixes it |
| **the area law from the medium** | black holes, no-singularities §5, entropy file §3 | **PAID at candidate grade (2026-07-20 regulator; 2026-07-28 roster)** — scaling derived (species count and cutoff cancel); η = 12π/48π = 1/4 from the heat-kernel ratio; entanglement-side O(1) closed structurally (conical deficit: area term and 1/G share one coefficient). **Roster extension PAID** (`scripts/area_law_roster_extension.py`): fermions exact, gauge sector restored by Donnelly–Wall edge modes, conformal Higgs drops out under ξ = 1/6 — 63% unconditional, 37% on the named edge-mode commitment. No residual half-computation remains on this row |
| **λ, the quartic** | no-singularities §5, black holes §3 | **TENSION DISSOLVED 2026-07-18** — recomputed, the equilibrium requirement is λ ≳ 8×10⁻⁹⁴, which the derived 2×10⁻⁹¹ clears by ~250×; the quoted "≳10⁻⁹⁰" was three orders too strong and is corrected |
| **the Z₄-locking mechanism** | quartet clock §2 | **RESOLVED (since the 07-18 census)** — the unit question closed by stability: repulsive λ forbids quartet binding; the Z₄ term locks phases, not composites; the oscillating unit is the PAIR, derived (quartet clock §4a; header updated) |
| **the ringdown / echo imprint** | black holes, no-singularities §5 | OPTIONAL — "owed if pursued", and nothing else leans on it |

## What the census changes

*(2026-08-02 hygiene note — the paragraph below is the 07-18 framing with its own later
corrections kept; the table above is the live status.)*

Fully discharged of desk computation at table time: **T3, T7, T9, T10, T11, T12, T13, T15**
(machine, watch, and paid only). **T2** is discharged of both #31 halves (saturation + data
assembly); what remains is chain-gated α_g and the external spin-catalog referee. The live open
desk residue clusters on **T4** (matched lensing), **T6** (pacing + sign-chain), **T14 link 4**
(toroidal relative sign), **T1**'s live exposure framing, **T5**'s ungradeable power-spectrum
route (the estimator is built; the data application is calendar), and **T16**'s conditional
axis-correlation. *(The three amplitude computations an earlier draft of this sentence listed as
unrun — the chiral-GW number, the cavity spectrum, the soliton's dynamical pricing — have all since
been run: T10 COMPUTED 2026-07-18, T5 RUN 2026-07-18, T1 priced by the galactic-centre budget test.)*

**The weight that remains:** T14's **link 4** alone now keeps the helicity dictionary shut on the
seeding side (link 5 closed negative 2026-07-20); T5's claim that the model predicts the low-ℓ
anomalies still needs the external BipoSH data application, not a missing instrument.
