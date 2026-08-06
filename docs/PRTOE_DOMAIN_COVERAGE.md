# The Domain Coverage Map

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


This file is the single auditable index of every domain of
physics (and adjacent science) the PRTOE program has worked
through, with the verdict class and a pointer to where the work is
recorded. "We ran through all of physics" is a claim; this is its
receipt. One line per domain — the records hold the substance.

Verdict classes: identity (the model *is* this physics) ·
calibration (known answers reproduced, no new content) · null (asked
and answered: not in this model, with the number) · silence
(translates but adds nothing) · strain (partial translation, honest
deuterium row) · door (new testable structure found) · bet (standing
falsifiable commitment) · mover (active evidence channel).

| # | Domain | Verdict | One-line result | Recorded in |
|---|--------|---------|-----------------|-----------|
| 1 | Cosmology (CMB/BAO/SN background) | mover | The model: H₀ ≈ 69.9 (provisional, **not** from live tables), S₈ eased, plik better than ΛCDM's own. **The live test carries ε pinned at the derived value, not floated** — zero *extra* parameters vs ΛCDM **if stack holds** (c·f̄·α_c; not +1 floated m_e) — **do not say “zero free parameters” unless c, f̄, α_c all hold**. Laplace ΔlnZ = +2.635, suggestive and SH0ES-dependent — **and the Laplace is where the verdict rests**; PolyChord nested sampling is offline (ended 2026-07-20; cluster re-run deferred); production bbnfix pair **NOT bookable** as of 2026-08-05 (lcdm R−1 **0.049324** N=26294 t=2026-08-05T11:52:10 — control leg ready, `converged:true`; dyad R−1 **0.060201**@N=26135 t=2026-08-05T15:50:02 — **1.20×** stop, `converged:false`; pair still refused; **no peek H₀**) | the headline-result document (v5_dCDF_complete, archived); [PRTOE_CHAIN_TABLES.md](PRTOE_CHAIN_TABLES.md) |
| 2 | BBN / nuclear astrophysics | **awaiting measurement** | Deuterium row −2.5 to −1.4σ (2.407–2.463 across the genesis window, full budget: obs ±0.030 ⊕ post-LUNA theory ±0.037); helium pays at +1.3 to +2.0σ. **The absolute σ is set by d(d,n)³He, unmeasured** — the row spans −3.6σ to −1.6σ across the literature's four rate-error assessments (P-2026-058). The model's 0.62σ deficit against its own ΛCDM control is compilation-robust and does not wait | [PRTOE_deuterium_row.md](PRTOE_deuterium_row.md) + the headline-result document §11 |
| 3 | Dark energy | bet | The floor is exactly Λ — no evolution, no phantom crossing; model votes against DESI DR2's 3.1σ preference (standing bet #3) | atlas: the biggest mystery |
| 4 | Vacuum energy / cc problem | door (coherence) | Old half: zero-point = virtual fluctuations, never realized (＋Jacobson, ＋Jaffe); new half: kernel-sourced — ρ_Λ¼ = 2.2599 meV, +0.44% **as an existence claim, not a precision one** (the radiative correction is bounded at 0.10–0.90%, comparable to the gap; the control-edge re-examination in the dark-energy file), lattice-refereed on τ alone (P-2026-048), with the portal √σ_dark = m_e the one irreducible input | atlas: the biggest mystery + the headline-result document |
| 5 | Structure formation / galactic dynamics | mover (awaiting simulation, the sole ε-meter) | Granule power p²+q² is now the only observable that reads ε (make-or-break for ε ever being measurable); Room 5's χ-lag (uncondensed today in dwarfs) = candidate 4th axis: redshift-dependent core–halo, specific to the electron-coupled scalar | Room 1 E7/E7b/Room 5; five-verdict V1–V3 |
| 6 | Quantum foundations / measurement | calibration (ceiling) | Settlement law C4a–h; CHSH lands on Tsirelson 2√2 exactly (4×10⁻¹⁶); Zurek trilogy reconstructed | the headline-result document C4; atlas |
| 7 | Thermodynamics / stat mech | identity-adjacent | Landauer/demon calibrated; Jacobson heals the gravity strain; ergodic/microcanonical backbone runs the stochastic genesis draw | atlas; Room 1 E8 |
| 8 | Black holes | door | Throat solved exactly (sonic point at ISCO, basin exit at tribonacci); universal horizon degenerates onto metric horizon; white holes: unstable (null); wormholes: negative-energy priced | the headline-result document's addenda |
| 9 | BH superradiance / spin archaeology | door (live now) | The model faces this test as a free scalar. At λ ≈ 2×10⁻⁹¹ the quartic is 85 decades too weak to quench a growing cloud (`scripts/superradiance_quench.py`), so there is no self-interaction shield and no free-vs-condensate discriminator — whatever a spin measurement does to free FDM in this band, it does to the model. **At the recorded ultralight mass the test has moved**: that mass sits an order above the earlier [1,3]×10⁻²¹ band, so M87*-class holes are past the superradiant window rather than inside it, and the live confrontation is with black holes between **6×10⁸ and 3×10⁹ M☉** — inside the window, and carrying high measured spins ([PRTOE_smbh_atoms.md](PRTOE_smbh_atoms.md)). Still the model's most immediate dark-sector test, now aimed at a different mass decade | atlas + Room 1 A6a |
| 10 | Gravitational waves / PTA | dead (honest headstone) | Channel killed by mass at the audited band: the medium rings (97.6% of the scanned range) but pulsar timing cannot hear it — the silence is instrumental, not a property of the amplitude | Room 1 audit + ANN-2026-011 |
| 11 | Inflation / genesis | door | AD genesis: chaos in release angle, ε is set by the stochastic genesis draw; the Z4 tilt is an input (parity + renormalizability leave Z2 operators standing, so four-foldness is not selected); scrambler = depositor; recursion wall kept visible | Room 1 E3–E8, Room 4 |
| 12 | Neutrino physics | mover (healthy post-surgery) | Posterior relaunched with seeded covmat (quasi-static chain caught and fixed; acceptance 0.92→0.21); collision resolved (ANN-2026-021): P-2026-004 falsified, meV whisper (Σm_ν≈61.35 meV, NO) stands — posterior now tests it | predictions doc; atlas whisper trial |
| 13 | Particle physics / constants | null (census) | Coupling census closed gravity-only (theorem grade); free-parameter family dead (α +433, Y_p pinned, Ω_k forbidden); m_e the one permitted modification | the headline-result document; five-verdict doc |
| 14 | Antimatter physics | door | 30% of DM (a quarter of all matter) is never-annihilating dark antimatter; the antimatter question splits between sectors | atlas: burn set 3 |
| 15 | Indirect detection / astroparticle | bet | No dark-sector signal ever — model votes astrophysics on GC excess, positrons, 3.5 keV (standing bet #2, kill-only) | atlas: burn set 3 |
| 16 | Laboratory precision (EP, fifth force, clocks, decay rates) | bet | Every precision lab a standing bet at zero (kill-only, never confirm) — census-forced, no free parameter (standing bet #1) | atlas; κ_v doc |
| 17 | Superfluids / BECs (condensed matter) | identity | The medium is a charged rotating superfluid (Son EFT, isomorphism granted); amplitude mode measured (Endres); softness measured (Steinhauer) | Room 1 doc; atlas receipts |
| 18 | Analog gravity | calibration and door | Steinhauer Hawking (asterisked); Eckel expanding ring = the tabletop frozen-ellipticity instrument; fringe contrast = the KR beat formula | atlas whispers |
| 19 | Superconductivity / metrology | calibration | SI volt = AC Josephson = the phase-quantization law as legal standard; superconductor vs medium: gauged vs global U(1) — cousins, not twins | atlas: burn set 3 |
| 20 | Quantum computing / information | calibration | Willow/error correction; Landauer; information scrambling = the MSS bound | atlas calibration cluster |
| 21 | Lasers / quantum optics | calibration | Stimulated emission as competing transition rates; the whole sector is C4's home turf | atlas calibration cluster |
| 22 | Nuclear decay / time dilation | calibration | Tunneling receipts priced; Kossert zero-modulation = lab-zero leg; Hafele–Keating = time-emergence receipt with numbers | atlas; references |
| 23 | Plasma physics | null | "Superplasma" scored: pre-basin phase is a gapless acoustic gas, not a plasma (no Debye, no gap) | atlas nulls |
| 24 | Turbulence / fluid dynamics | silence (kinship) | Intermittency stays silent; the medium natively inhabits quantum turbulence (vortex tangles — Room 5's territory) | atlas silences |
| 25 | Solar system / ephemerides | null | Local medium density 4–5 decades below planetary-orbit sensitivity | atlas: burn set 3 |
| 26 | Cosmic strings / topological defects | null | Born condensed — U(1) never restored, δθ ~ 10⁻⁵ seeds no windings; no string network | Room 1 E7 |
| 29 | Mathematics / golden ratio | null (mechanism-grade) | φ absent from the model's derived numbers; its two honest employers (anti-resonance, self-reference) use machinery the medium lacks | atlas nulls |
| 30 | Time / emergence | calibration | Time, motion, and inertia emergent in the C1 census; Page–Wootters receipt (Moreva) | the headline-result document C1; references |
| 32 | Strong CP | silence (**COMPLETE-ABSTENTION**) | Jurisdiction silence finished as abstention — θ̄ outside the model permanently; not a paper candidate. **Seat itch registered 2026-08-04** (parity / missing EM-anomalous angular mode kinship only — **not** cyclic reverse; **not** a θ̄ solution) | [PRTOE_strong_cp.md](PRTOE_strong_cp.md); seat hunt: [`working_logs/_runs/physics_improve_full_20260804/STRONG_CP_SEAT_HUNT.md`](working_logs/_runs/physics_improve_full_20260804/STRONG_CP_SEAT_HUNT.md) |
| 33 | Colliders | silence | Gravity-only trivially passes collider nulls; no content claimed | atlas walls |
| 33a | Hierarchy problem | **exploratory — content is claimed** | A pairing-gap anchor M ≈ 4π·m_H, with an electroweak-precision bound limiting the portal to at most two new doublets. Exploratory, not silent: §6f's three-horn fork is open and the α_c band is unconverged | `PRTOE_hierarchy_problem.md` |
| 34 | Baryogenesis | door (named class) | Dark asymmetry-genesis = AD spiral (charge = abundance); visible baryogenesis untouched; the 5:1 ratio an honest input (ADM numerology null) | Room 1 R1.2/R1.8; atlas |
| 35 | Quantum gravity phenomenology | calibration | Smooth-not-foamy (C3a); GRB 090510 linear LV > 1.2 E_Planck receipt | the headline-result document C3a; references |
| 36 | Page curve / information (dynamical Q6) | **OPEN** | Dynamical Page curve **not closed**. Champion instrument `coevolve_v13` joint near-miss (T1–T6 PASS; T8 range/S* = **0.113**, need ≤0.10); `page_curve_claimed: false`; no standing CANDIDATE. Next unblock = licensed new microphysics only (D4 freeze stance). Not the Page–Wootters row (30) | [PRTOE_quantum_gravity.md](PRTOE_quantum_gravity.md) Q6; freeze: [`working_logs/_runs/page_full_freeze_20260804/REPORT.md`](working_logs/_runs/page_full_freeze_20260804/REPORT.md) |

Reading the map (34 rows; row 36 added 2026-08-04 as **OPEN** residual, **not** COMPLETE): 3 standing bets (labs, telescopes, Λ) · 1 live-now test
(superradiance — the mass rests on the onset clock plus one unresolved consistency check: the ξ leg
is definitionally circular and the third leg is this very exposure, so the confrontation is
**somewhat** relievable by moving m — and this cuts *against* the model's honesty position, not for
it: a firmer pin would make the adverse constraint bind harder) · 2 simulation-gated axes (granule ε-meter, sole; Room 5 χ-lag) · 1 dead
arm with an honest headstone (PTA, killed by mass, pre-called) · 1 healthy converging judge
(Σm_ν → P-2026-004 falsified, now testing the surviving meV whisper) · 5 clean nulls with
numbers · 3 structural silences (Strong CP remains **COMPLETE-ABSTENTION**) · 1 honest strain (deuterium, repriced) · 1 identity · 1
exploratory row that claims content (the hierarchy anchor) · **1 OPEN dynamical Page residual** (row 36 — not closed).

Row numbers 27, 28 and 31 are absent by design: those entries moved to the jurisdiction section
below and are not domains this model works in. The gaps are left rather than renumbered so the
removal stays visible.

The rule this file serves: a domain is "covered" only when its verdict is recorded with a
pointer — no domain is claimed on impression alone. Domains not yet on this map are not
covered; add them only with a record.

## Outside the model's jurisdiction

The three entries below sit outside the domain table by design. The distinction is not
cosmetic: a physics model that lists Medicine as a "covered domain" invites the reading that
it claims jurisdiction there, whatever the row actually says. **None of these is a domain this
model works in.** They are kept only because each states a boundary that someone might
otherwise try to cross on the model's behalf.

- **Consciousness / quantum mind.** Neural decoherence sits 10–17 decades below signalling
  timescales; the brain is a classical system. Nothing in this program can be recruited for
  quantum-mind claims, and this entry exists to say so in advance.
- **Quantum biology.** Credit-window arithmetic is marginal at exciton scales, and the
  coherence claims in that literature are contested and not endorsed here.
- **Medicine.** Restating known physiology-adjacent physics in the model's own bookkeeping
  language produces no new content and constitutes no medical claim of any kind.

Adding a fourth entry here would be a mistake. The correct response to "does the model say
anything about X" for a non-physics X is silence, not a row.

*Created 2026-07-07. Maintained alongside the atlas.*

---

## Discipline triage (2026-08-04 currency)

**Grade:** ledger/history — process record, not a physics derivation.
**Discipline:** above story-grade *as a record* (append-only / living map discipline).
**Triage:** stay shelf as LEDGER/HISTORY; not Failures; not exploratory.
**Non-claims:** no physics COMPLETE from this file alone; **not** Page closed; **not** bbnfix bookable; Strong CP remains **COMPLETE-ABSTENTION** (seat hunt ≠ solution).
**Currency package:** `docs/working_logs/_runs/shelf_map_currency_20260804/`
**Rule:** `docs/working_logs/STORY_GRADE_ELEVATION_RULE.md`
