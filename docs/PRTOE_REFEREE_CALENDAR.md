# The Referee Calendar — every judge, every date, every decision rule (2026-07-12)

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


*T13's second debt, paid. One page: who grades what, when, and by what pre-written rule.
No verdict may be argued after the fact — the rules below were set before the referees speak.*

## Sitting now (in-house machines)

> **Live read 2026-08-10 (refreshed)** — old-BAO + DESI-DR2 both Stage A BOOKED; gold nested SH0ES
> both legs running; quota 300 (~240 in use). Progress-file `acceptance_rate` remains oversampled
> (`oversample_power = 0.4`) — **raw accept = accepted/steps from launchlog**.
>
> **Old-BAO production bbnfix pair: BOOKED Stage A.** Authority:
> `docs/working_logs/_runs/bbnfix_booking_20260808_005626/REPORT.md`.
>
> | chain | N (receipt) | R−1 | stop | converged | bookable |
> |---|---:|---:|---:|---|---|
> | `dyad_mnu_bbnfix` | 37605 | **0.048118** | 0.05 | true | **YES** |
> | `cmp_lcdm_mnu_bbnfix` | 26294 | **0.049324** | 0.05 | true | **YES** |
>
> Booked three-rank GetDist (`ignore_rows=0.3`): dyad **H₀ = 70.052 ± 0.716**, `m_ncdm` **0.0671 ± 0.0583**, **S₈ = 0.821 ± 0.0097**; lcdm **H₀ = 68.345 ± 0.343**, `m_ncdm` **0.0192 ± 0.0174**, **S₈ = 0.824 ± 0.0081**.
>
> **Evidence honesty:** sample-covariance Laplace **ΔlnZ ≈ +0.21** (cond(Σ)~10⁸) — not nested.
> FD Hessian v1 failed; **v2 finished finite** (diagnostic only, soft modes).
>
> **DESI-DR2 bbnfix twins: BOOKED Stage A** (separate instrument — do not mix). Authority:
> `desidr2_bbnfix_booking_20260810_053127/REPORT.md` — dyad R−1 **0.03321** / lcdm **0.041377**,
> both `converged:true`; GetDist H₀ **70.30±0.54** / **68.73±0.25**. DESI FD Hessian process on 48-box.
> routeD still **OPEN-MACHINE** at **R−1 = 0.351167**@N=14625. Gold nested: SH0ES both legs
> **running** (resume); TRGB not launched; **no nested ΔlnZ yet**.

| referee | grades | decision rule | ETA |
|---|---|---|---|
| **BBN-fixed model — `dyad_mnu_bbnfix`** (booked old-BAO pair) | Σm_ν joint + production-faithful D/H; opens the old-BAO H₀ / `m_ncdm` / S₈ receipt | dual gate met: `Rminus1_stop = 0.05` **and** checkpoint `converged: true`; booked only via `scripts/book_bbnfix_when_ready.py` | **BOOKED** on the 2026-08-08 receipt: **R−1 = 0.048118 at N = 37605** (t=2026-08-07T04:08:52), `converged: true`; GetDist **H₀ = 70.052 ± 0.716**, `m_ncdm = 0.0671 ± 0.0583`, **S₈ = 0.821 ± 0.0097** |
| **BBN-fixed ΛCDM twin — `cmp_lcdm_mnu_bbnfix`** (booked old-BAO pair) | matched denominator for the model chain | same dual gate, same booking receipt | **BOOKED** on the 2026-08-08 receipt: **R−1 = 0.049324 at N = 26294** (t=2026-08-05T11:52:10), `converged: true`; GetDist **H₀ = 68.345 ± 0.343**, `m_ncdm = 0.0192 ± 0.0174`, **S₈ = 0.824 ± 0.0081** |
| **the thaw chain — `cmp_prtoe_routeD`** (samples `dcdf_floor_thaw` = 1+w_{fl,0}; live, 3 ranks) | thaw = 0 (the no-bare clause's direct falsifier) | posterior excluding 0 = evidence against the clause itself; stop `Rminus1_stop = 0.1` | **Machine — live; NOT bookable.** Last progress: **R−1 = 0.351167 at N = 14625** (t=2026-08-06T09:24:48); ~**3.51×** stop 0.1; checkpoint `converged: false`. Progress accept ~0.997 oversampled. Prior collapsed launches archived under `chains/_archive_routeD_*`. **No thaw posterior is bookable at this R−1.** Separate instrument — not part of the bbnfix pair dual gate |
| DESI-DR2 bbnfix MCMC twins — `dyad_mnu_bbnfix_desidr2` / `cmp_lcdm_mnu_bbnfix_desidr2` | current BAO-era joint posterior lane | dual gate separate from old-BAO: both DR2 legs `R−1 < 0.05` **and** `converged: true` | **BOOKED Stage A** (`desidr2_bbnfix_booking_20260810_053127`): dyad R−1 **0.03321**@N=53482; lcdm **0.041377**@N=52031; GetDist H₀ **70.30±0.54** / **68.73±0.25**. **Do not mix** with old-BAO. Not nested. |
| The nested referee — DESI-DR2 gold program (4 PolyChord legs) | P-2026-044-style evidence comparison on the current DESI-DR2 stack; SH0ES pair and TRGB pair | compare dyad vs ΛCDM **within the same ladder anchor** only; no mixed-anchor ΔlnZ; no verdict until both legs of a pair finish | **SH0ES both legs RUNNING** (resume after Fortran fix) under quota **300**; TRGB not yet. Intermediate log(Z) not bookable. **No nested verdict yet.** |
| **zon_disp — not relaunched** (collapsed R−1 = 23.3 archived at `chains/_archive_zon_disp_collapsed_20260720_1528/`; seed for a correct restart is built as `chains/zon_disp_seed.covmat`) | P-040 (α_c = 3α), the triangle (M₂, x₀, ρ_Λ), the pair mark, the n-instrument, five freezes | converged (R−1 < 0.05) center inside 7.4–7.7 = 3α-compatible (bath band); at ~7.55 = clean confirm; above ~7.8 = the named branches must pay | **Parked by decision (2026-08-04)** — last progress R−1 ≈ **17.81** (N=3456, 2026-07-22); not live. Gated shelf §2 / #13. The collapsed config's seed covers 12/13 parameters and knows nothing about `log10_zon`; relaunching on that seed would reproduce the failure. Restart is an owner act when cores free, on the from-samples seed only |
| **conv_desi — not a live posterior** (collapsed 07-18 run archived; last chain file stamped **2026-07-22** at split-R̂ R−1 = 13.25) | the S₈ g (pre-registered g ≈ 0.10 ± 0.05) | posterior vs the pre-registration; the 10ε/1-8 candidates stay firewalled | **Unproduced, not pending (2026-08-04)** — died twice (init 07-16; again 07-22). Restart is an owner decision. Companion S₈ files (`PRTOE_s8_growth.md`, `PRTOE_s8_tension.md`) carry the same correction. Matched lensing-likelihood fit (#161) remains open separately |
| **dyad_mnu_mcmc — historical control case (archive; not the live bbnfix pair)** | (not a referee; recorded because it constrains how stuck-chain failures were read in July) | — | Archive diagnostic, not a live process. Once the healthiest object on the box at **R−1 = 0.176 at N = 8736** with progress accept **0.92** — showing that a high *progress* acceptance rate is *not* by itself pathology under `oversample_power = 0.4`. Flat-direction hypothesis **tested 2026-07-29** (`scripts/flat_direction_convergence_test.py`) and **unsupported though not refuted** (stuck chains narrow in every direction, not only named suspects). Live production health is now tracked on **`dyad_mnu_bbnfix` / `cmp_lcdm_mnu_bbnfix`** above, not here |

> What zon_disp shows about the covariance fix, found 2026-07-20 while freeing cores. zon_disp
> did **not** lack a seeded covariance — its config feeds `chains/dyad_mnu_seed.covmat` — and it
> failed anyway, at R−1 = 23.3. The seed covers **12 of its 13 parameters**: it carries
> `varying_me` where zon_disp samples **`log10_zon`**. So the one parameter the chain exists to
> measure is the one parameter the seed knows nothing about. Cobaya fills the gap from the
> parameter's own `proposal` width, which supplies a scale and no orientation.
>
> Diagnosed and repaired 2026-07-20, with one guess above corrected. The blindness is worse
> than a missing seed entry and it is visible in the chain's own output: in
> `cmp_prtoe_zon_disp.covmat`, `log10_zon` is the **only** parameter of thirteen whose
> off-diagonals are *exactly* zero, with σ *exactly* 0.08 — the configured `proposal` value passed
> straight through. The sampler never learned it at all. So bootstrapping a seed from that file,
> which is what repaired routeD and conv_desi, would have reproduced the blindness exactly and
> looked like a fix.
>
> The samples know what the learned covmat does not. 217 distinct `log10_zon` values were
> explored (7.52–7.81, σ = 0.063), and their empirical correlations are substantial. **But not in
> the directions guessed above:** against H0 and `dcdf_rho_inf` the correlations are **+0.075 and
> +0.085** — essentially none. The degeneracy runs through **ω_b at −0.743** and **A_planck at
> +0.515**. The ±1.00 direction named earlier is not where this parameter is stuck.
>
> `scripts/build_chain_seed.py` builds seeds either way and refuses to be quiet about it — it
> flags any parameter the learned covmat never updated and points at `--from-samples`. Validated by
> reproducing routeD's working seed to 4.7×10⁻¹⁶. **`chains/zon_disp_seed.covmat` is built and
> ready**; the chain was *not* relaunched then (load ≈ 5.9 on six cores; standing instruction to
> leave two cores free) and remains **parked by decision** as of 2026-08-04 (Sitting NOW row above).
>
> **Historical note (2026-07-20 13:10):** what routeD and conv_desi *were* running on that day
> (verified from the configs and the seed files themselves). Both carried the
> **correlation-preserving** seed: C = D_phys·R·D_phys, taking the ridge's orientation R from each
> chain's own archived covariance and the magnitudes D_phys from the configs' physical widths.
> Verified by reading the seeds, not by trusting the launch note — `routeD_seed.covmat` is 14×14
> with max |off-diagonal correlation| 0.982 and mean 0.436; `conv_desi_seed.covmat` is 13×13 at
> 0.965 and 0.275. Neither is diagonal. The companion setting that caused the collapse:
> `learn_proposal_Rminus1_max_early` = **2.0** against Cobaya's default of 30, so no proposal is
> learned from a chain sitting at R−1 = 8–27.
>
> First measurement that day, and it was the good outcome. Over 3.5 h of burn-in, acceptance was
> **20.4%** (routeD) and **19.8%** (conv_desi), against the ~97%-and-never-move pathology those
> relaunches were meant to escape. That is inside the optimal band for high-dimensional
> Metropolis, measured from the launchlogs' step/accept counters. **Present (2026-08-05):**
> routeD is live again (Sitting NOW: R−1 = **0.257073** at N = 11422 — not bookable, ~**2.57×** stop);
> conv_desi is **unproduced** after two deaths (last chain file 2026-07-22) — not a live posterior.
>
> The 07-20 burn-in measurement settled the step: the proposal was the right size
> *and* the right shape, and the sampler was exploring. It did not settle convergence — a
> well-oriented proposal on a genuinely multimodal or badly curved posterior can still fail to
> mix, and **R−1 remains the only test that grades it.**

> The evidence route, restated 2026-07-20. PolyChord was ended after ~48 h in which it never
> reached its first checkpoint. It was not stalled; it was simply the wrong machine for the job.
>
> **Superseded by the 2026-08-06 AWS follow-up.** The current live state is: the dyad evidence leg
> is running on the replacement `c7i.24xlarge` Spot box at `96` ranks, the repaired ΛCDM twin
> worker is queued behind it, and there is still no nested verdict. Use
> `working_logs/_runs/polychord_owner_followup_20260806/REPORT.md` for current cost / status rather
> than the retired laptop economics.
>
> **What the run actually costs, and what machine matches it**
> (`scripts/nested_run_cluster_sizing.py`). The reference run and its twin are 1.93 million
> likelihood evaluations, i.e. **4.0 core-years** — a many-core node, not a cluster. At 64 cores
> it is about a month; at 128, about two weeks. **The live-point count caps the return:** with
> nlive = 200 PolyChord cannot usefully employ more than ~200 cores, and raising nlive lifts the
> ceiling only by raising total work in proportion. The configuration sets the maximum useful
> machine. The dominant term is the 66 s likelihood, which is slow for a CLASS-class evaluation
> and is the one input here never profiled: 66 s → 10 s would be worth more than six times the
> cores, at no cost. num_repeats = 24 = 2·ndim is already at the economical end and holds little
> slack.
>
> The verdict therefore rests on Laplace-from-MCMC, as it did before the nested run was
> attempted, while the nested pair remains unfinished. The old laptop no longer sets affordability:
> the current nested referee is the **gold DESI-DR2 four-leg** program, but it is still **not
> launched**, so the MCMC chains remain the only graded input for now. **Chain convergence is
> therefore still on the critical path for P-2026-044 itself**, while the nested confirmer exists
> only as a design, not a result.

## The near sky (1–2 years)
| referee | grades | rule |
|---|---|---|
| **DESI-era Σm_ν** | the neutrino block's ≈61.35 meV (61.35 at m_lightest = 2.25 meV, 61.40 at 2.284 — harness-checked on NuFIT normal-ordering splittings) | robust bound < ~60 meV kills; a measured Σ ≈ 61 crowns; the P-023 internal tension arbitrates itself |
| DESI DR3 w(z) | w = −1 exactly (the peg) | robust thawing/w ≠ −1 kills the floor |
| TRGB ladder (P-2026-001) | the no-hedge ladder bet | as registered |
| the radio referee | the D/H fork (D/H = 2.387×10⁻⁵ → 2.407–2.463×10⁻⁵ with the genesis residual; a self-adverse owned bet; the registered pull −2.9σ eases to **−2.5…−1.4σ** on the quotable budget under the standing high-f books, and does not reach Cooke — hunt §8 1b) | as registered |
| The zero-parameter evidence exposure — currently carried by Laplace-from-MCMC while the DESI-DR2 gold nested program waits on quota | ε, A_s and n_s stated vs ΛCDM free — **z_on excepted**, frozen 0.053 dex off the onset identity | ΔlnZ verdict; any stated number wrong collapses the model's evidence. The **historical** pre-bbnfix Laplace line is +2.635, but the **current booked old-BAO pair** carries only an inconclusive sample-covariance Laplace **ΔlnZ ≈ +0.21** with soft-mode sensitivity. Until a matching nested pair exists, the exposure is real but the reading remains marginal |
| the ς sign session — landed: ς = −1 | the candle room / the H₀ ceiling | the candle lever is dead; the ceiling reads 70.9–71.3 (estimate grade, robust) |
| DESI forest-BAO (near-term data) | the gate curve at mean density | a clean forest at the curve's prediction kills the candle room |
| the Eliashberg k-audit + winding-gas C_V (B2/B3 — **run: k audited into [1.35, 1.37], three-way concordance 1.360/1.36461/1.3602; and since reconstructed exactly from a two-band screened kernel, though on a host the basement does not record — hierarchy §6c, §6m**) | the A_s closed form | k outside the concordance band [1.360, 1.366] kills the k-locked prediction — currently inside |
| BipoSH joint pass (analysis-limited — data exists) | the axis family as one axis (comb + dipole + isocurvature + HPA) **and now the torus's own correlation pattern** — m ↔ −m at fixed ℓ (ρ ≈ 0.38–0.47 at ℓ = 2, 4) and ℓ ↔ ℓ+2 at fixed m (ρ ≈ 0.36 for 3 × 5), total signal-to-noise 1.4 over ℓ ≤ 6, on 111 non-zero pairs of 990, every one obeying the cube's Δm ≡ 0 (mod 4) selection rule (`scripts/torus_lowell_pattern.py`) | any two family members robustly misaligned kills the family; a measured correlation structure inconsistent with the predicted pattern kills the compact-topology reading (the power spectrum cannot referee it — its signal-to-noise is 0.16). At 1.4 this channel constrains rather than decides |

## The decade
| referee | grades | rule |
|---|---|---|
| **ton-scale 0νββ** (nEXO/LEGEND-1000/CUPID) | Majorana necessity; m_ββ ∈ **[0.04, 5.3] meV** (the floor is anchor-dependent — 0.050 → 0.038 meV across ρ_Λ¼'s real 0.449% uncertainty, Planck's 1.80% on ρ_Λ quartered; the 2.2842 meV figure that would drop it to 0.023 is the retired T_c = 179 keV route's output, and the ledger records its "+1.5%" as the T_c rounding rather than a sourced spread) | Dirac-nature evidence kills the sector — though it cannot be demonstrated directly, only inferred; a signal above ~5.3 meV kills too (two-sided). **Only nEXO can reach this model**: reaches 4.7–20.3 meV against LEGEND-1000's 9–21 and CUPID's 12–34, so it alone overlaps, at 4.7–5.3 meV, ~10.8% of the phase space. Barium tagging (×4 half-life → ×2 in m_ββ, reach ≈ 2.35 meV) lifts that to ~69% but **stops discriminating** — minimal ordering gives 63.7% there. The band that discriminates is **3.69–5.30 meV**, above minimal ordering's hard ceiling, where this model lands 31.7% of the time |
| **LiteBIRD** | the anti-anomaly bet (β = 0 vs the 2.9σ EB claim) | confirmed isotropic rotation executes the model (the dichotomy: it cannot own 0.34°) |
| HL-LHC | the portal's visible branch (13–20 TeV at two loops — beyond reach, and the edge audit has concluded it stays there: no anchor-edge convention closes the gap, minimum 3.6× across every admissible pairing) | as amended (P-039/P-042) |
| SKA-class cosmic dawn (REACH/lunar) | P-2026-043 (the deeper trough, signed — depth computed at ≈ 1.0%, so the channel is a consistency check rather than a discriminator; the dark-ages rest-frequency offset is the mechanism's astrophysics-free arm) | a trough robustly shallower than standard = wrong sign, kills. A sign test: the depth is under the foreground and beam systematics |
| DESI 4PCF parity — favorable, not closed | the anti-anomaly bet, now P-2026-055 (the model is 7 orders short — bets systematic) | confirmed parity violation at claimed amplitude = the model has no channel, owned exposure. Verdict: arXiv:2512.20132 (2025-12-23), the direct DESI DR1 parity-odd 4PCF paper, finds the current signal **consistent with zero** overall; apparent auto-correlation excesses up to ~4σ appear only in one uncorrected covariance treatment, and the paper itself flags low DR1 completeness as a sensitivity limit. arXiv:2604.06021 (2026-04-07) likewise finds **no parity violation in either BOSS or DESI** on composite-field spectra, with DESI scatter ~4× tighter than BOSS DR12; the blind BOSS CMASS 4PCF test returns 2.9σ against 7.1σ unblinded. **Favorable, not decisive** — higher-completeness direct DESI 4PCF releases still settle it more sharply |
| primordial helium benchmark | the helium side of the BBN witness | LBT Y_p Project IV arXiv:2601.22238 gives **Y_p = 0.2458 ± 0.0013**, in good agreement with BBN; EMPRESS XV arXiv:2506.24050v3 gives **Y_p = 0.2402 ± 0.0040**, moderately low. **Do not** keep quoting the older `0.2453 / 0.2370` pair as current state. Shelf authority: `blocked_lane_helium_fork_20260805/REPORT.md` |
| stochastic GW (PTA/LISA/ET) | the vortex Gμ null; the chiral family (amplitude un-computed) | as registered |
| **CMB-S4 ΔN_eff** | the committed genesis window ΔN_eff ∈ [0.06, 0.24] — **and, through the no-hiding corollary, the nucleosynthesis-era value too** (P-2026-053: the dark sector's relativistic content cannot convert to matter or photons in between) | confirmed < 0.03 or > 0.3 kills the committed ζ window from either side, at both epochs at once |
| **CMB-S4 Majoron search** | the v_L corner selector (both corners clear every applied constraint). **Not** the deuterium-deuterium row injector: the EM repair spec needs a state ≳20 MeV living 10⁶–10⁸ s, and the MeV corner is a *scale* (v_L ≈ 4.2 MeV) whose RH seats sit below the ⁴He threshold — see `PRTOE_deuterium_row.md` §6/§8 | a detection at g ~ 10⁻⁸–10⁻⁹ selects the MeV corner; a null leans high-v_L. Neither outcome fills the deuterium row's missing source by itself |
| **the SU(2) N_f = 3 lattice** (external; the note approved for circulation) | three numbers of one campaign: **T_c/√σ** (P-2026-048 + the addendum's two-point fork: 0.34506 vs ½ln2 = 0.34657), **F_dark/√σ** (the kernel chain demands 0.40–0.47, pinned convention = F_π ≡ √2 f_π, the 130.4-MeV branch), **w·√σ** (the sheet: 0.8–1.1) | **Live falsifier = clause 4:** τ̂ outside [0.330, 0.370] falsifies the DE sector (neighbour inference 0.39±0.05 sits above). Ideal point-values 0.34657 / 0.34506 are the crown/null fork — **sky-limited**, not currently executable: even σ=0 lattice separates them by only ~0.98σ under ρ_Λ’s ±0.449% (null contains H_kernel at upper edge; P-048 living currency; lattice_note; READERS_RISK (j)). Ordinary 1–3% determinations score neither way on crown/null. The last two lattice numbers are one test, not two: the F band is derived from c_K *and* the thickness, so only the pair measured on the same ensembles referees anything, through c_K = √3·2π·(F/√σ)²·(w√σ) against the demanded 1.9236. The F band is now billable, and unopposed: the NJL route that appeared to return 0.1759 against the vortex-pair 0.4204 was computing f/Λ_NJL rather than f/√σ — refuted by its own QCD anchor (Λ = 631 MeV vs √σ = 440 MeV, a 1.42× step), so 1.42 of that 2.39 was a change of denominator and the rest is the vortex route's already-recorded √2 above QCD (docket #134, closed). What the lattice tests is that √2 offset: the demand sits 1.35–1.59× QCD's pinned value, outside the measured class rather than inside it. The campaign does not carry the radiative band: that is bounded at the desk at 0.10–0.90% on ρ_Λ¼ (the control-edge re-examination in [PRTOE_cosmological_constant.md](PRTOE_cosmological_constant.md)), waiting on one scattering amplitude rather than on these ensembles. The +0.44% remains an **existence claim and not a precision claim** — which is also why any residual crown/null talk must be read in τ-space, where the separation is exact arithmetic, rather than in the closeness of the predicted meV to the observed one. Shelf authority: `blocked_lane_lattice_tau_gate_20260805/REPORT.md` |
| **Belle II-class lepton masses** | P-2026-051 — the Koide deviation lock: δθ = (√2/9)·δA = 0.1571·δA, currently **+0.89σ** off the line and on the side a positive slope does not predict (δA = −1.3057×10⁻⁵, δθ = +7.409×10⁻⁶ rad). **What is actually being measured is m_τ**: with m_e and m_μ effectively exact, Q = 2/3 requires **1776.96903 MeV**, θ_B = 2/9 requires 1776.96651, the closure 1776.96705 — against 1776.86 ± 0.12, all +0.91σ above | deviations robustly off the line kill the holonomy-equals-Q closure; either watch breaking outright kills a fortiori. Scope, stated for the referee: those three predictions span 2.52 keV = **1.42 ppm of m_τ**, against today's 68 ppm — so below ~1.4 ppm a kill of the closure is also a kill of A = √2, and the two cannot be separated. An m_τ landing *between* 1776.96651 and 1776.96903 is the only measurement that discriminates them. Two scope notes attach, both stated in advance. First, **the two watches cannot both be exact whatever m_τ returns**: together they leave the ring only its overall scale and so fix m_μ/m_e at 206.770316 against the measured 206.768283 ± 4.5×10⁻⁶ — a 452σ miss on a ratio the τ does not enter, so this campaign can identify the survivor but cannot rescue the pair. The referee should weigh the size alongside the significance: granting the closure puts Q 0.17 ppm off 2/3, granting Q = 2/3 puts θ 0.79 ppm off 2/9, so what is refuted is refuted by under one part per million and the 452σ reflects a 22 ppb measurement rather than a large discrepancy. Second, the 2.518 keV separation is 1.42×10⁻⁷ in Q, while reading the sector on renormalized rather than pole masses moves Q by 1.18×10⁻³ — **8270× the gap being resolved**. The watches are pole-mass statements and the pole mass is what is measured, so the test executes as written; what the referee should not grant is that a win promotes the winner's mechanism, while the framework's choice of mass variable is itself underived and worth far more |
| **lunar-farside dark-ages 21-cm** (LuSEE-Night/FarView class) | the +2.51% bare-value frequency offset (+0.40 MHz at the z ≈ 87 trough — astrophysics-free) | the trough at the standard frequency kills the ε mechanism's dark-ages arm |
| **the ring-on-ring trial — landed 2026-07-18: death** | the Koide complex's deliverer | all three Widnall points land inside the pre-sealed death zone (1.85/1.99/1.98 vs ceiling 0.97); the deliverer executed; the equivalences stand as mathematics; autopsy in the ledger |

## The standing exams (forever)
Lorentz nulls (cavities — the shield's margin), clock/Oklo ṁ_e = 0, Koide Q within 7×10⁻⁶,
underground silence (10⁻¹⁵⁰ cm²), indirect-detection nulls (σv = 0), Tsirelson exactness.
Continued nulls cost nothing, earn nothing — the model's permanent performance bills.

*Rule of the calendar: when a referee lands, its row gets the verdict stamped same-session
and the failures ledger or the spine inherits accordingly. No row may be re-argued.*

---

## Discipline triage (2026-08-03)

**Grade:** ledger/history — process record, not a physics derivation.
**Discipline:** above story-grade *as a record* (append-only / living map discipline).
**Triage:** stay shelf as LEDGER/HISTORY; not Failures; not exploratory.
**Non-claims:** no physics COMPLETE from this file alone.
**Rule:** `docs/working_logs/STORY_GRADE_ELEVATION_RULE.md`
