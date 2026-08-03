# The Reader's Guide — plain physics, no house dialect

**Status (2026-08-02):** glossary and reading map for outsiders. For graded claims, evidence class
(Laplace-marginal; nested sampling offline), and kill conditions, start with
[PRTOE_READERS_RISK.md](PRTOE_READERS_RISK.md). Live chain status:
[PRTOE_CHAIN_TABLES.md](PRTOE_CHAIN_TABLES.md).

*Written for the newcomer and the external reviewer. Working documents in this repository use a
compact internal vocabulary for the model's recurring objects; you do not need that dialect to
evaluate the physics. This page states the model plainly, translates the recurring house terms, and
gives a reading order.*

> **If two files disagree about a number, do not adjudicate it yourself.**
> [`working_logs/_CANONICAL_VALUES.md`](working_logs/_CANONICAL_VALUES.md) carries the canonical
> value, where it is *derived* (not merely quoted), what proves it, and its grade — plus a "what it
> is NOT" column. On 2026-07-20 two apparent contradictions turned out to be **two different
> objects**, not a disagreement. The same file lists quantities with no canonical value yet, so none
> enters the record by accident.

## 1. The model in five plain sentences

1. One complex scalar field — a cosmological superfluid — replaces separate dark matter
 and dark energy: its ground state supplies the w = −1 component; its excitations act
 radiation-like early and CDM-like late (one fluid, two eras).
2. The field's phase winds an integer number of times around one compact spatial
 direction; that single integer and its axis source all of the model's predicted sky
 anisotropies.
3. A second field (the electron-coupled scalar) couples to leptons through exactly one number: a
 fractional shift of the electron mass, ε ≈ 1.24%, active in the early universe and switched off
 later by a screening transition.
4. That one shift, applied wherever atomic physics appears — recombination, BBN's later
 stages, 21 cm rest frequencies, potentially supernova spectra in unscreened
 environments — is the source of every claimed signature; the same number must work
 everywhere or the model fails.
5. The model is pre-registered: predictions carry numbered entries with named
 killing observations, filed before the deciding data.

## 2. The glossary — house term → physics term

| house term | plain physics |
|---|---|
| the medium / the fluid | the superfluid scalar field (the unified dark sector) |
| the amplitude / ε | the fractional electron-mass shift. Three numbers appear deliberately: **1.2543%** is the derived stack (c·f̄·α_c = 27α/5π), **1.232%** the production-chain fit, **~1.24%** the posterior summary. The 1.8% gap between derived stack and production fit sits inside the posterior width; production-chain posteriors will grade it **once those chains converge** (they have not yet) |
| the dyad — **prefer "the electron-coupled scalar"** (rename 2026-07-28; audience-facing files use the new name) | the high-decay-constant pseudo-Goldstone field that shifts m_e — one of three dark fields (dCDF superfluid, electron-coupled scalar, Majoron). It is **not** the Majoron: the single-scale reading that merged them (f = v_L) is dead on the neutrino tie, which is why there are three fields rather than two. Older documents used "the dyad" for the (dark fluid + varying-m_e) pair |
| the winding / n / the draw | the quantized phase winding number, set stochastically (Kibble mechanism) at the condensation transition |
| f_amp | the medium's **librating fraction**, 1 − f_rot (used by the dice output, the granule-contrast dial p²+q², and the beat √(f_amp(2−f_amp))). Older documents reuse the letter as an amplitude factor in ε = c·f_amp·Ψ₀/M_red; that is not the standing form, which is ε = c·f̄·α_c with f̄ = 2/π |
| the axis / the axis family | the compact direction, and the set of sky signatures predicted to share it (power-spectrum comb, dipole, alignments, bulk flow) |
| the gate / screening / the gate curve ε(C) | environmental switch-off of ε: a smooth function of local clumping (dense regions: ε → 0; voids retain it) |
| recorded | established within the model at production grade (coded, fit, or derived) and written into the corpus |
| the census / census blindness | the counting argument behind c = 9/10: gravity couples to energy content, not particle identity |
| the pinch / occupancy one | the ground state holds exactly one quantum per coherence cell (sets the vacuum energy scale) |
| the anchor / the gap equation | the TeV scale from a pairing exponential, M ≈ M_red·e^(−1/kα_c − 3/2) — the hierarchy mechanism. Pairing is **particle-hole** (a Cooper pair of charged fermions would mass the photon); the −3/2 says the pairing shell's cutoff is the Planck floor dressed down by the equipartition boost. Derived end to end, but the *value* carries a factor-of-a-few band (∂lnM/∂lnk = 33 amplifies every O(1)) |
| the twins / the pair | Cooper-style pairing of a mode with its time-reversed partner |
| the arrow / the arrow-giver | time orientation set by the condensate background (⟨θ̇⟩ ≠ 0, ghost-condensate class) |
| the pour / the snap / the fountain | the bounce: the hot re-start of a cycle (structurally the one realized white-hole-like event) |
| the melt | reheating above T_c at the crunch: superfluidity ends, friction returns, the winding's protection lapses |
| route D / the thaw branch | alternative to a rigid dark-energy floor: w₀ ∈ [−0.92, −0.86] with wₐ < 0 — dark energy *leaving* its floor as the universe expands rather than sitting on it. DESI DR3 decides between this and w = −1 exactly |
| the curvature-metered gate | screen that switches the electron-mass shift off in dense, curved regions, keyed to curvature sharpness: exp(−(C/C_ref)ⁿ) with n > 2.43 — sharp enough to act as a step. Why today's laboratories see no effect |
| ramps vs steps | house discipline: physical transitions are modeled as smooth (finite-width) functions, never bare discontinuities, unless protected by quantization or topology |
| the error log | log of caught errors (public, in the failures ledger) |
| the §12 wall | hard scope boundary: the interpretation layer makes no claims about mind, consciousness, or observers — measurement is decoherence/einselection and nothing more. Named for a section number in an early draft; the boundary is the content |
| the killer / the kill | the named observation that falsifies a specific claim |
| estimate / open item | computed lightly, or not yet verified by the full chain — said in plain prose, not as a grade tag |

## 2b. The symbol table — one symbol, one meaning

Several letters carry more than one job in physics generally, and this model touches enough
sectors that the overlaps are real. Where the corpus uses a shared letter, the intended meaning is
fixed here:

| symbol | meaning | where it lives |
|---|---|---|
| **ε** | the fractional electron-mass shift, 1.2543% — the model's one modification to known physics | everywhere |
| **α_c** | the dCDF's condensate coupling, 3α | the amplitude, the vacuum, the hierarchy exponent |
| **c**, **f̄** | the census fraction 9/10; the winding average 2/π | the amplitude's decomposition ε = c·f̄·α_c |
| **τ** | T_c/m_e = **½ln2 = 0.34657** — the electron-coupled scalar's condensation temperature in electron-mass units, sourced by the Koide kernel through Parseval (T_c = 177.10 keV) | the dark-energy chain |
| **ζ** | the genesis dilution T_dark/T_γ ∈ [0.25, 0.35] — the dark sector's temperature relative to the photons at genesis; sets ΔN_eff | the high-f configuration, the BBN books, the CMB-S4 falsifier |
| **c_K** | the **Koide kernel constant**, c_K = Q/τ = 4/(3·ln2) = 1.92359 — dimensionless, and equal to the face spacing in string units, d·√σ. **Renamed from c₂ on 2026-07-28** because that symbol carried three unrelated meanings. **Working logs still write it c₂**; the two are the same object. It is load-bearing: τ = Q/c_K sources T_c and thence the dark-energy scale | the forced-combination file, the Koide chain |
| **c_w** | the **winding-response quadratic coefficient**: writing the fractional mass shift as \|x\| + c_w·x² in the winding projection x = ε·cos θ gives f̄_eff = 2/π + c_w·ε/2. Dimensionless, negative, and only bounded to order unity by data (−1.80 fit-implied, −0.84 ± 0.52 winding ensemble, 1.9σ apart). **Renamed from c₂ on 2026-07-28.** Deriving it is docket #55 | the f̄ subleading price, P-2026-026 |
| **c₂** | reserved for its **standard physics meaning only**: the *second sound speed* of Landau two-fluid hydrodynamics, c₂ = c₁/√d = √α·c ≈ 0.0854c. **A velocity.** Not to be confused with c_K (dimensionless, +1.924, a string spacing) or c_w (dimensionless, ≈ −1, a Taylor coefficient). The three were checked in the 2026-07-28 sweep and are genuinely distinct — different dimensions, values differing by a factor 22, and no relation claimed anywhere in the corpus. The near-coincidence \|−1.80\| ≈ 1.92 is accidental: the same quantity's other determination is −0.84. **A fourth usage, found on the sweep's second pass and recorded so the count is not overstated:** working logs also write c₂ as an ordinary *indexed* coefficient in local polynomial fits (e.g. c₂A² alongside c₃, c₅ in a thermal expansion). That is generic subscript notation rather than a named constant, and context makes it plain, but it means "c₂" in a working log should be read from its neighbours rather than from this glossary | the second-sound prediction, the isocurvature phase speed |
| **ξ** | a *length*: the medium's coherence length. Bare ξ = 402 AU is the **coherence hinge** — it falls between the planetary system (~40 AU) and the Oort cloud (~10⁴⁻⁵ AU), so structures above it span many coherence cells and structures below it sit inside one. That is a property of ξ itself; the scale ladder it used to be quoted from was retired 2026-07-28 as a restatement of the virial theorem. **ξ_K** = 256 Mpc is the Kibble domain size | the medium's own properties, the vortex network, magnetogenesis |
| **ξ_H** | the non-minimal curvature coupling of a scalar (the standard gravitational meaning, as in the weight 1/6 − ξ) — unrelated to the lengths above | the induced-G sector, P-2026-045 |
| **n** | the genesis winding integer, n ≳ 1.65 (a band of 10–30 only for a torus far above its floor) — the one topological draw | the comb, the helicity sign, the matter asymmetry |
| **L**, **χ_\*** | the torus's compactification scale (≥ 27.6 Gpc); the comoving distance to last scattering (13.76 Gpc) | the low-ℓ sky, the winding comb |
| **f** | the electron-coupled scalar's decay constant, ~100–500 TeV | the scalar's sector, the portal |
| **ς** (final sigma) | the sign in the H₀-ceiling formula, read off the supernova colour channel — **ς = −1** (estimate grade, robust; the H₀-lever branch is dead and the bracket collapses to 70.9–71.3) | the candle room |

*Retired-era documents may use these letters differently; each such file carries its own banner.*

## 3. The reading order

0. **READERS_RISK** — one honest page: strongest claims, weakest links, evidence class, kill list.
1. **THREE_EQUATIONS** — the testable core in three lines.
2. **THE_AMPLITUDE** — the one number and its seven windows.
3. **DEPENDENCY_TREE** — what is conditional on what (the honesty map).
4. **PREREGISTERED_PREDICTIONS** — the bets, with killers.
5. **FAILURES_LEDGER** — everything that died, and the error log.
6. The per-topic shelf (cosmological constant, hierarchy, neutrino sector, …) as interest
 dictates; **MATH_SPINE** for the full derivation chain.

## 4. What to be skeptical of

- The statistical win (ΔlnZ = +2.635) is a **Laplace** estimate, SH0ES-conditional and marginal.
  Nested sampling is **not running** and waits for cluster time. Production MCMC is converging but
  **not yet quotable** — see the risk summary.
- The A_s closed form is a *candidate* (counting mechanism half-derived; frozen into the production
  configs by explicit decision, with the risk documented — not the output of a converged posterior).
- Several numerical landings are estimate-grade with O(1) honesty bands; statuses are stamped where
  they apply.
- The candle-room / H₀-ceiling story: the screening form is derived at class level
  (survival/exponential) and the sign is signed (ς = −1 — the H₀ lever is dead; the ceiling reads
  70.9–71.3). Coupling legality is closed by the model's own coupling law (sector-internal coupling
  is permitted). The screening computation, open since 7 July, was **delivered on all four items**
  on 2026-07-18. What remains is the observational side, and that side got sharper, not softer: the
  21-cm edge shape no longer *selects between* a thermal and an environmental reading — the thermal
  one was retired on 2026-07-16 as an illegal step (a global gate switching off is a dynamical
  discontinuity, neither quantized, topological, nor a protected zero). **The model is committed to
  the environmental reading** (structure-tracking fade over z ≈ 30–60), so a confirmed sharp global
  step in the edge now counts **against** the model rather than choosing one of its branches. The
  DESI forest cross-calibration still adjudicates the supernova fork.
- **The electroweak anchor is a mechanism, not a measurement.** The chain from the Planck floor to a
  few TeV is derived end to end — pairing channel, screening constant, measure, shell cutoff — but
  its *precision* is a factor of a few: **0.55 to 1.78 TeV** (first sized at 1–8 TeV; vertex and
  self-energy corrections both act downward), not four significant figures. The exponent amplifies
  every O(1) thirty-threefold. Agreement quoted tighter than that is a coincidence of convention;
  the corpus says so where it arises.
- **The count k in that chain is derived exactly, on a host this corpus does not record.** The
  reconstruction is exact and independently confirmed, but it assumes a Fermi surface at finite
  chemical potential with two velocity-matched bands, whereas the recorded constituent level is a
  Fermi point at zero chemical potential. That is evidence *for* those conditions rather than a
  derivation *from* recorded structure — the hierarchy chain's largest open exposure.
- **The chirality family cannot name which handedness means matter, and that is settled rather than
  pending.** The sector predicts a magnetic-helicity sign *relative to* the genesis winding; it
  cannot predict the absolute sign, because the genesis draw generates rotation with no preferred
  sense — a symmetry of the recorded potential that the release prior does not break. Whether even
  the relative lock exists is a separate, open question.
- The deepest claim (the medium's reality) remains an open assumption — named as such, with its
  exposure tracked honestly.
