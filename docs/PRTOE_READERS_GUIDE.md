# Reader’s guide — plain physics, no house dialect

**Status (2026-08-05 currency):** glossary and reading map for outsiders — not a graded-claims
surface. For graded claims, evidence class (Laplace-marginal; nested sampling offline), kill
conditions, and live risk posture, start with
[PRTOE_READERS_RISK.md](PRTOE_READERS_RISK.md). Live chain bookkeeping:
[PRTOE_CHAIN_TABLES.md](PRTOE_CHAIN_TABLES.md).

> **Currency board (2026-08-05).** Production bbnfix MCMC pair is **NOT bookable** — re-verify with
> `python3 scripts/book_bbnfix_when_ready.py` (CURRENT: lcdm R−1 **0.047912** N=24858
> t=2026-08-05T04:55:58 — below stop without self-stop; dyad R−1
> **0.056889** @N=24677 t=2026-08-05T07:54:30 — **1.14×** stop; both `converged: false` →
> **REFUSED**). Do not peek-book H₀ / Σm_ν / S₈ from live chains. BBN ε arithmetic is **verified
> internal**; **external win pending DOI**. Numbers and gates live in RISK + CHAIN_TABLES; this
> guide does not book posteriors.

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

## 1. The model in five sentences

1. One complex scalar field — a cosmological superfluid — replaces separate dark matter and dark energy: ground state supplies w = −1; excitations act radiation-like early and CDM-like late (one fluid, two eras).
2. The field’s phase winds an integer number of times around one compact spatial direction; that integer and its axis source the model’s predicted sky anisotropies.
3. A second field (the electron-coupled scalar) couples to leptons through one number: a fractional electron-mass shift ε ≈ 1.24%, active early and switched off late by a screening transition.
4. That one shift, applied wherever atomic physics matters — recombination, later BBN, 21 cm rest frequencies, possibly supernova spectra in unscreened regions — is the source of every claimed signature. The same number must work everywhere or the model fails.
5. Predictions are pre-registered: numbered entries with named killing observations, filed before the deciding data.

## 2. Glossary — house term → physics

| house term | plain physics |
|---|---|
| the medium / the fluid | the superfluid scalar field (unified dark sector) |
| the amplitude / ε | fractional electron-mass shift. Three numbers on purpose: **1.2543%** derived stack (c·f̄·α_c = 27α/5π), **1.232%** production-chain fit, **~1.24%** posterior summary. The 1.8% gap between derived stack and production fit sits inside the posterior width; production-chain posteriors will grade it **once those chains converge** (they have not yet) |
| the dyad — **prefer “electron-coupled scalar”** (rename 2026-07-28; audience-facing files use the new name) | high-decay-constant pseudo-Goldstone that shifts m_e. One of three dark fields (dCDF superfluid, electron-coupled scalar, Majoron). Not the Majoron: merging them at f = v_L dies on the neutrino tie. Older docs used “dyad” for the (dark fluid + varying-m_e) pair |
| the winding / n / the draw | quantized phase winding, set stochastically (Kibble) at condensation |
| f_amp | medium’s **librating fraction**, 1 − f_rot (dice output, granule-contrast p²+q², beat √(f_amp(2−f_amp))). Older docs also used f_amp in ε = c·f_amp·Ψ₀/M_red; standing decomposition is ε = c·f̄·α_c with f̄ = 2/π |
| the axis / axis family | compact direction; sky signatures that should share it (comb, dipole, alignments, bulk flow) |
| the gate / screening / ε(C) | environmental switch-off of ε vs local clumping (dense: ε → 0; voids keep it) |
| recorded | established at production grade (coded, fit, or derived) and written into the corpus |
| the census / census blindness | counting argument behind c = 9/10: gravity couples to energy, not identity |
| the pinch / occupancy one | ground state holds one quantum per coherence cell (sets vacuum energy scale) |
| the anchor / gap equation | TeV scale from pairing exponential M ≈ M_red·e^(−1/kα_c − 3/2) — hierarchy mechanism. Pairing is **particle-hole** (charged Cooper pair would mass the photon). −3/2: pairing shell cutoff is Planck floor dressed by equipartition. Derived end to end, but the value is a factor-of-a-few band (∂lnM/∂lnk = 33 amplifies every O(1)) |
| the twins / the pair | Cooper-style pairing of a mode with its time-reversed partner |
| the arrow / arrow-giver | time orientation from the condensate (⟨θ̇⟩ ≠ 0, ghost-condensate class) |
| the pour / snap / fountain | bounce: hot re-start of a cycle (realized white-hole-like event) |
| the melt | reheating above T_c at the crunch: superfluidity ends, friction returns, winding protection lapses |
| route D / thaw branch | alternative to a rigid DE floor: w₀ ∈ [−0.92, −0.86], wₐ < 0 — DE leaving its floor as the universe expands. DESI DR3 decides this vs w = −1 |
| curvature-metered gate | screen that kills the electron-mass shift in dense, curved regions: exp(−(C/C_ref)ⁿ), n > 2.43 — effectively a step. Why labs today see no effect |
| ramps vs steps | transitions are smooth (finite width) unless protected by quantization/topology |
| the error log | caught errors (public; failures ledger) |
| the §12 wall | hard scope: no claims about mind, consciousness, or observers — measurement is decoherence/einselection only. Named for an early draft section; boundary is the content |
| the killer / the kill | named observation that falsifies a claim |
| estimate / open item | lightly computed or not fully chain-verified — said in prose, not as a grade tag |

## 2b. Symbol table

| symbol | meaning | where |
|---|---|---|
| **ε** | fractional electron-mass shift, 1.2543% — the one modification to known physics | everywhere |
| **α_c** | dCDF condensate coupling, 3α | amplitude, vacuum, hierarchy exponent |
| **c**, **f̄** | census fraction 9/10; winding average 2/π | ε = c·f̄·α_c |
| **τ** | T_c/m_e = **½ln2 = 0.34657** (T_c = 177.10 keV), from Koide kernel via Parseval | dark-energy chain |
| **ζ** | genesis dilution T_dark/T_γ ∈ [0.25, 0.35]; sets ΔN_eff | high-f config, BBN, CMB-S4 |
| **c_K** | Koide kernel constant c_K = Q/τ = 4/(3·ln2) = 1.92359 — dimensionless, equals face spacing in string units d·√σ. **Renamed from c₂ on 2026-07-28** (that symbol had three meanings). Working logs may still say c₂. Load-bearing: τ = Q/c_K → T_c → DE scale | forced combination, Koide chain |
| **c_w** | winding-response quadratic coefficient: fractional mass shift \|x\| + c_w·x² with x = ε·cos θ gives f̄_eff = 2/π + c_w·ε/2. Dimensionless, negative, O(1) from data (−1.80 fit-implied, −0.84 ± 0.52 winding ensemble, 1.9σ apart). **Renamed from c₂ on 2026-07-28.** Deriving it is docket #55 | f̄ subleading, P-2026-026 |
| **c₂** | **second sound speed** only (Landau two-fluid): c₂ = c₁/√d = √α·c ≈ 0.0854c. A velocity. Not c_K (dimensionless ~1.924) or c_w (dimensionless ~−1). Checked 2026-07-28: different dimensions, values differ by ~22×, no claimed relation. \|−1.80\| ≈ 1.92 is accidental (other c_w determination is −0.84). Working logs also use c₂ as a generic fit coefficient (c₂A² next to c₃, c₅) — read from context | second-sound prediction, isocurvature phase speed |
| **ξ** | coherence length. Bare ξ = 402 AU (coherence hinge: between planetary ~40 AU and Oort ~10⁴⁻⁵ AU). **ξ_K** = 256 Mpc is the Kibble domain size. Scale ladder that used to quote it was retired 2026-07-28 (virial restatement) | medium, vortices, magnetogenesis |
| **ξ_H** | non-minimal curvature coupling of a scalar (standard 1/6 − ξ weight) — unrelated to lengths above | induced-G, P-2026-045 |
| **n** | genesis winding integer, n ≳ 1.65 (band 10–30 only for a torus far above its floor) | comb, helicity sign, matter asymmetry |
| **L**, **χ_\*** | torus compactification scale (≥ 27.6 Gpc); comoving distance to last scattering (13.76 Gpc) | low-ℓ sky, winding comb |
| **f** | electron-coupled scalar decay constant, ~100–500 TeV | scalar sector, portal |
| **ς** | sign in H₀-ceiling formula from supernova colour channel — **ς = −1** (H₀-lever branch dead; bracket 70.9–71.3) | candle room |

Retired-era documents may use letters differently; those files carry banners.

## 3. Reading order

0. **READERS_RISK** — one honest page: strongest claims, weakest links, evidence class, kill list.
1. **THREE_EQUATIONS** — the testable core in three lines.
2. **THE_AMPLITUDE** — the one number and its windows.
3. **DEPENDENCY_TREE** — what is conditional on what (the honesty map).
4. **PREREGISTERED_PREDICTIONS** — the bets, with killers.
5. **FAILURES_LEDGER** — everything that died, and the error log.
6. Topic files as needed; **MATH_SPINE** for the full derivation chain.

## 4. What to be skeptical of

- The statistical win (ΔlnZ = +2.635) is a **Laplace** estimate, SH0ES-conditional and marginal
  (pre-bbnfix stack). Nested sampling is **not running** and waits for cluster time. Production
  bbnfix MCMC is live but **NOT bookable** (gate: both R−1 < 0.05 and self-stop) — see RISK and
  CHAIN_TABLES; do not treat interim R−1 as a booked product.
- **A_s closed form** is a candidate (counting mechanism half-derived; frozen into the production
  configs by explicit decision, with the risk documented — not the output of a converged posterior).
  E2E Track A grades the imprint path separately; B2 tilt route is closed negative.
- Several numerical landings are estimate-grade with O(1) honesty bands; statuses are stamped where
  they apply.
- **Candle room / H₀ ceiling.** Screening form is derived (survival/exponential); sign ς = −1 (H₀
  lever dead; ceiling 70.9–71.3); coupling legality closed by the model’s own law. Screening
  computation delivered 2026-07-18. Observational side sharpened: 21 cm edge shape no longer chooses
  thermal vs environmental — thermal retired 2026-07-16 as an illegal step (global gate off is a
  dynamical discontinuity with no exemption). **The model is committed to the environmental reading**
  (structure-tracking fade over z ≈ 30–60). A confirmed sharp global step in the edge counts
  **against** the model. DESI forest cross-calibration still adjudicates the supernova fork.
- **Electroweak anchor is a mechanism, not a measurement.** Planck floor → few TeV is derived end to
  end (channel, screening, measure, shell cutoff), but precision is a factor of a few: **0.55–1.78 TeV**
  (first sized 1–8 TeV; vertex and self-energy corrections both downward), not four figures. Exponent
  amplifies every O(1) by ~33. Agreement better than that is convention coincidence; the corpus says
  so where it arises.
- **Count k is derived exactly on a host this corpus does not record.** Reconstruction is exact and
  confirmed, but assumes a Fermi surface at finite μ with two velocity-matched bands; the recorded
  constituent level is a Fermi point at μ = 0. That is evidence *for* those conditions, not a
  derivation from recorded structure — largest open exposure in the hierarchy chain.
- **Chirality family cannot name which handedness is matter** — settled, not pending. Sector predicts
  magnetic-helicity sign relative to genesis winding; absolute sign is free (genesis rotation has no
  preferred sense). Whether the relative lock exists is separate and open.
- **Deepest claim** (medium’s reality) remains an open assumption; the corpus names it and tracks
  exposure.

---

## Claims ledger & discipline (2026-08-03) — above story-grade discipline

| # | Claim | Grade | Evidence | Residual / blocker |
|---|---|---|---|---|
| 1 | File is glossary / reading map, not a physics result | **meta** / complete as guide | banner | Claims live in RISK + sector files |
| 2 | Five-sentence model summary accurate to corpus | **interpretation** | §1 | Condensed; grades elsewhere |
| 3 | Glossary / symbol table matches standing usage | **complete-conditional** | §2–2b | Canonical values file arbitrates conflicts |
| 4 | ε three values on purpose (1.2543 / 1.232 / ~1.24) | **honest fence** | glossary row | Chains not converged |
| 5 | M3 medium reality is open assumption | **OPEN** | caveats list | Named exposure |

**Non-claims:** not graded evidence; not kill list (see READERS_RISK).

**Triage:** elevate-in-place (map). Physics ceiling: n/a (orientation).
