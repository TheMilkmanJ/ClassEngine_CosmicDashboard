# PRTOE — Honest Status Board (internal review record)

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


> **Private — internal candid self-assessment, not the primary audience-facing record.**
> This file is cited from a small number of shelf/process pages as a candid status source, so it is
> no longer literally unlinked from the docs shelf; those links do not make it a paper-facing claim
> surface.

> **The `#N` numbers in this file are local and are not the docket's.** This page predates the
> current numbering and carries two of its own: the **Q-series** of the 2026-07-08 review (Q1/#19,
> Q2/#20, Q3/#21, Q5/#23, Q6/#24, Q7/#25), and the **least-trusted-joints list** (its own #1 and #3,
> at "least-trusted joint #1/#3"). Neither maps onto
> [`working_logs/_DOCKET_INDEX.md`](working_logs/_DOCKET_INDEX.md), where #19–#25 are the big-claim
> mining and ramp-regrade tasks. Read every number on this page as scoped to this page.

## CURRENT (2026-08-05)

**Expansion fence.** **Pulford–Romsa Theory of Expansion** (PRTOE) — a dark-sector cosmology of the
expanding cosmos and its imprints, **not** a Theory of Everything. Local bound matter is ceded to
the Standard Model; the domain is the diffuse cosmic medium. Same fence as
[PRTOE_READERS_RISK.md](PRTOE_READERS_RISK.md) / laws_and_rules / quantum attach notes. No TOE claim.

**bbnfix pair — NOT bookable.** Live production pair + Route-D (MPI live). Authority is cobaya
progress R−1 **and** checkpoint `converged: true`; offline GetDist GR is diagnostic only.
`python3 scripts/book_bbnfix_when_ready.py` → **REFUSED**. Surfaces
`PRTOE_CHAIN_TABLES.md` / `PRTOE_CODE_MANIFEST.md` / `PRTOE_REFEREE_CALENDAR.md` all stamp the same
gate. **No letter H₀ / Σm_ν / S₈ from live chains.** lcdm is now **self-stopped and individually
ready** at R−1 **0.049324** (N=26294, t=2026-08-05T11:52:10, `converged: true`), but the pair is
still **NOT bookable** because dyad is **0.060201**@N=26135 t=2026-08-05T15:50:02
(`converged: false`; **1.20×** stop — moved **away** from the bar from 0.056889). routeD R−1 **0.536955**@N=9745 t=2026-08-05T18:43:45
(~**7.28×** stop 0.1) — not dual-gate. Currency: shared blocker card
`blocked_lane_bbnfix_20260805/REPORT.md`.

| chain | N (progress) | R−1 | stop | converged | bookable |
|---|---:|---:|---:|---|---|
| `cmp_lcdm_mnu_bbnfix` | 26294 | **0.049324** | 0.05 | **true** | **NO** (control leg ready; pair gate still closed) |
| `dyad_mnu_bbnfix` | 26135 | **0.060201** | 0.05 | **false** | **NO** (1.20× stop; moved away from the bar) |
| `cmp_prtoe_routeD` | 9745 | **0.536955** | 0.1 | **false** | **NO** (~5.37× stop) |

GetDist offline max GR (`bbnfix_mcmc_watch_diag.py`): lcdm **~0.07**, dyad **~0.086** —
diagnostic only; **not** the booking gate. Quote R−1 with N and timestamp. Temporary R−1 < 0.05
without self-stop is **not** bookable, and one ready leg does **not** open the pair.

**BBN ε arithmetic verified (internal).** ε 2σ ceiling card re-verified 2026-08-04:
`papers/bbn-eps-bound/recompute_eps_bound.py` → **3.196% ≈ 3.20% PASS**. EMPRESS at ε=0 still
+2.91σ (cannot bound ε) — honesty unchanged. **EXTERNAL WIN PENDING (no DOI)** — public record still owed; not re-booked.

**Page near-miss freeze.** Q6 / dynamical Page stays **OPEN**. Champion `coevolve_v13`
(schedule `v23_champion_locked`): T1–T6 PASS; **T8 FAIL** (early bin range/S* = 0.113 > 0.10).
`page_curve_claimed: false`. `CANDIDATE_TURN_binding: false`. No CANDIDATE packet. D1–D3 exhausted;
D4 freeze active — next unblock is **new microphysics**, not knob thrash. Package:
`docs/working_logs/_runs/page_full_freeze_20260804/`.

**Strong CP abstention.** `PRTOE_strong_cp.md` remains a complete **constitutional silence** — the
model has nothing to say about θ̄; needing a strong-CP mechanism would kill the constitution. Not a
derivation; not a paper candidate; not promoted.

**PolyChord off.** Nested sampling not running and not scheduled on this hardware (9.8 h/iteration;
163 days to first checkpoint). Evidence grades from Laplace-from-MCMC (standing ΔlnZ = +2.635 —
marginal, SH0ES-conditional) until cluster time. Archived nested run:
`chains/_archive_polychord_ended_20260720_0915/`.

### Residual theory board (2026-08-05 exhaust currency)

Present grades only. Stocked-desk thrash **exhausted**; open theory needs construction / MISSING_INPUT /
machine-or-owner gates. **Physics COMPLETE promotions this wave: 0.** Authority:
[`working_logs/_runs/theory_exhaust_20260805/MASTER_REPORT.md`](working_logs/_runs/theory_exhaust_20260805/MASTER_REPORT.md) ·
[`working_logs/_runs/theory_exhaust_20260805/audit/POST_EXHAUST_AUDIT.md`](working_logs/_runs/theory_exhaust_20260805/audit/POST_EXHAUST_AUDIT.md).

| residual | grade |
|---|---|
| Bounce classical turn | **OPEN-BLOCKED** — stocked maps recorded; derived \(H_\mathrm{re}\) **not** paid |
| Page Q6 | **OPEN** — T8 = **0.113**; `page_curve_claimed: false` |
| Koide mechanism | **OPEN** — Wilson holonomy inputs **5/5 MISSING** |
| Void IGMF ×20 | **OPEN** |
| DE occupancy / “why now” | **OPEN** |
| Forward \(A_{\omega_J}\) / seat | **EMPTY_CORPUS_SEAT** · Charge A holds |
| Absolute SI \(G\) | **OPEN** — supertrace finiteness ≠ SI \(G\) |
| Unitarized σσ (ρ_Λ precision) | **MISSING_INPUT** |
| Machine bbnfix | **NOT bookable** |
| PolyChord | **skip** (hardware) |
| Strong CP | **COMPLETE-ABSTENTION** |

**What this supersedes as “current machine truth.”** Any surface still carrying **2026-08-04**
live R−1 numbers as if current (lcdm **0.071122** / dyad **0.072286** / routeD **4.941933**) is
stale; the 2026-08-05 stamp above is the live gate. E2E derivation board grades (A1–A6) under the
next heading remain valid as theory status; this section is the **machine + honesty** stamp. Theory
residual grades above are the 2026-08-05 exhaust stamp.

---

## CURRENT (2026-07-31) — retained (E2E board detail)

**Scope name.** **Pulford–Romsa Theory of Expansion** (PRTOE) — a dark-sector cosmology of the
expanding cosmos and its imprints, **not** a Theory of Everything. Local bound matter is ceded to
the Standard Model; the domain is the diffuse cosmic medium. (Same fence as
[PRTOE_READERS_RISK.md](PRTOE_READERS_RISK.md) / laws_and_rules.)

**End-to-end derivation board** (source of truth:
[`working_logs/_E2E_DERIVATION_BOARD.md`](working_logs/_E2E_DERIVATION_BOARD.md)):

| # | residue | grade |
|---|---|---|
| **A1** | A_s γ\*/f + c_chop | **CANDIDATE CLOSED** |
| **A2** | n_s / r-triangle | **CANDIDATE CLOSED** |
| **A3** | f̄ / c_w / LO | **CANDIDATE CLOSED** |
| **A4** | α_c same-response | **Permanent bet (P-2026-040)** — factor 3=d derived; base α not derived; A_s referee only |
| **A5** | B1 hydro crown | **PARTIAL (scoped)** — Ψ₀/f_amp done; intake candidate; pour→release / first-principles n open |
| **A6** | Bounce (B7) | **RECONSTRUCTED CANDIDATE** (turn not derived) |

**Bounce (A6 / B7).** Density floor ρ_bounce = m⁴/λ ~ (1.1 keV)⁴ is **derived**. Homogeneous FRW
bounce engines are **DEAD**. RP-A is a **reconstructed candidate** with written scaffold
(`scripts/bounce_rpA_scaffold.py`: F-A1…F-A3, knobs η/N_med/H-sign). The turn **H>0 forced by
stress-energy** is still **not** derived. Audience: floor + reconstructed program yes; derived
cosmological turn no. Verdict:
[`working_logs/bounce_e2e_verdict_2026-07-31.md`](working_logs/bounce_e2e_verdict_2026-07-31.md),
[`working_logs/bounce_promotion_2026-07-31.md`](working_logs/bounce_promotion_2026-07-31.md).

**What this supersedes in older CURRENT text below.** (1) A_s / n_s are no longer open residue —
candidate-closed via census microphysics (A1) and Route T (A2); residual κ≈1 and approach OOM noted
on the board. (2) α_c is **not** “settled by data rather than choice” as a derivation — it is a
**permanent value bet** with A_s as IR referee. (3) Any 07-18 phrasing that “the turn is computed”
is **withdrawn** for a derived cosmological turn; A6 is **reconstructed candidate**, not DERIVED.
(4) B2 winding-gas tilt stays **CLOSED DEAD** (#184); that path does not deliver A_s.

Still standing from the 2026-07-20 snapshot (detail under the next heading): c = 9/10 counting
input (democracy dead); ρ_Λ¼ existence claim +0.44% (not precision); DE self-tuning still fails
(ohmic); Laplace ΔlnZ = +2.635 marginal / SH0ES-dependent; nested sampling deferred to cluster.

### Snapshot held from CURRENT (2026-07-20)

Major moves since the 2026-07-08 baseline (below); grades above supersede where they conflict:

- c = 9/10 is a counting assumption the data confirms, and the step that would have derived it is
  withdrawn, not owed. The seating is sourced — the neutrino sits on the vacuum's seat because its
  mass is medium-sourced, not electroweak — and the ε-blind ensemble lands on the value
  independently, at c = 0.903, −0.08σ. What was meant to *license* a democratic count was routing the
  budget split through gravity's blindness, and that step does not exist: run alone, blindness weights
  by energy over every field in the vacuum, and charge (which selects the roster) weights by
  Σ N_c Q² = 8 → c = 8/9, or → c = 1 with a zero-weight seat, which the census excludes. No single
  criterion returns 9/10. Nor does the ensemble adjudicate — at its width 8/9 sits 0.30σ from 9/10,
  and a 3σ separation needs σ_c ≤ 0.0037 — a 10× sharpening, ~100× the sample. (The 0.0115 booked
  earlier is the candidate spacing, which buys 0.97σ: where they stop coinciding, not where either
  is excluded.) So the framework does not force the value; it is
  well-supported and assumed (#126, the two-census marriage,
  [PRTOE_DERIVATION_HUNT.md](PRTOE_DERIVATION_HUNT.md) §1).
- The dark-energy value now has a derived-scaling closed form: ρ_Λ¼ = (d²/2)α⁴·T_c, which on the
  Koide kernel's τ = ½ln2 gives **2.2599 meV against the observed 2.25 — +0.44%**. *(This board's
  earlier (d/2)α⁴m_e ≈ 2.17 meV, 0.97×, is the same structure with τ approximated as 1/3; the kernel
  supplies τ exactly and the agreement improves from −3% to +0.44%.)* **The +0.44% is an existence
  claim and not a precision one** — ρ_Λ¼'s radiative correction is bounded at 0.10–0.90%,
  comparable to the gap itself, with the residual question one scattering amplitude
  ([PRTOE_cosmological_constant.md](PRTOE_cosmological_constant.md), the control-edge
  re-examination). The kernel τ's referee is a lattice T_c/√σ for SU(2) with N_f = 3 — a number
  that does not yet exist; the lattice owes τ alone.
- DE-floor self-tuning (least-trusted joint #1) is now sharply understood — and it does not self-tune.
  The settling response is **ohmic** in the dark-energy channel, so the floor's value is not fixed by the
  settling and the coincidence problem stands. The sub-ohmic self-tuning belongs to the dark-*matter*
  channel, not DE. Honest: still no working self-tuning mechanism for the value.
- Evidence: the +2.635 Laplace win landed (below, unchanged) — and the Laplace is what the
  verdict rests on. Nested sampling is unaffordable on this hardware (9.8 h per iteration, 163
  days to a first checkpoint) and waits for cluster time, so the confirmer the +2.635 was explicitly
  awaiting is not coming from this box. *That makes the MCMC chains the evidence calculation's only
  input rather than side referees, and their convergence the critical path for the headline claim.
  As of 2026-08-05 (see CURRENT header above): bbnfix pair + routeD **live, NOT bookable**
  (lcdm R−1 **0.049324**@N=26294 t=2026-08-05T11:52:10 with `converged: true` — control leg ready /
  dyad **0.060201**@N=26135 t=2026-08-05T15:50:02 — **1.20×** stop, `converged: false` /
  routeD **0.536955**@N=9745 — ~**5.37×** stop; pair gate still closed);
  conv_desi and zon_disp are **not running** (posteriors unproduced; seeds ready; owner restart);
  `cmp_prtoe_zon` is untouched since 07-12; **PolyChord off**.*

### What moved on 2026-07-18

**Favourable.** The coupling's legality — the model's single largest conditional, on which the
whole electron-mass mechanism rested — is closed by the constitution's own clause, and the
screening computation that had been open since 7 July is delivered on all four of its items.
The dark-energy sector's "un-built O(1) coefficient" turned out not to exist: the two readings
stand in exactly the derived phase-space ratio, so nothing is owed there. *(Historical 07-18 note
“the turn is computed” is **superseded 2026-07-31**: cosmological bounce turn = **STORY**; only
the density floor is derived — see CURRENT header / bounce_e2e_verdict.)* The negative bare vacuum
became load-bearing rather than decorative.

**Adverse, and the sharper of the two directions.** Two independent constraints now bear
directly on the ultralight mass, which is fixed by the onset clock and cannot float: the
central soliton it implies carries roughly the whole extended mass the Galactic Centre shows
within a parsec, and it places supermassive black holes in a band of a few 10⁸ to a few 10⁹ solar masses
in the superradiant band where high spins are measured (**6×10⁸–3×10⁹ M☉**, recomputed from
α_g = Mm/M_Pl² over the efficient ℓ = m = 1 range α_g ∈ [0.1, 0.5]; the 2×10⁸ this board carried
was low). Neither is a computed exclusion; both
could close the sector. Separately, the low-multipole claim lost its power-spectrum footing
entirely — the torus is invisible to the spectrum at any multipole — and survives only as a
correlation-structure prediction.

**Operational.** At the measured theory speed the nested run's completion horizon is years, not
weeks, and the ΛCDM twin doubles it — so it was ended on 2026-07-20 and the verdict this board
treats as the deciding crux rests on the Laplace estimate, without the confirmer it was awaiting.

### What moved on 2026-07-19/20

**Favourable.** The gap equation is no longer a gap: k = ln(1 + π/2α_c)/π reconstructs **exactly**,
Monte-Carlo confirmed, as the Fermi-surface average of a Thomas–Fermi-screened Coulomb exchange in
the particle-hole channel, with the screening constant b = 2α_c/π falling out of standard pieces and
no chosen ones. And the channel itself is decided **host-independently**: a particle-particle
condensate of two charge-e fermions would give the photon an Anderson–Higgs mass of ~9.5×10¹¹ eV
against a bound of 10⁻¹⁸ — excluded by thirty orders — so particle-hole is forced, not preferred.
Separately, α_c's *IR value* is **refereed** by data rather than derived: A_s selects 3α(0) near
null (board: ~−0.4% to −0.9%), against +28% at α(M_Z). **A4 (2026-07-31):** factor 3 = d is
derived; same-response base α is a **permanent bet (P-2026-040)** — not open derivation debt.

**Adverse, and it is the same result read honestly.** That exact eight-digit reconstruction runs on a
host **this corpus does not have** — finite chemical potential, Thomas–Fermi screening, two
velocity-matched bands — while the recorded constituent level is a Fermi point at μ = 0, which §6a
shows cannot pair at this coupling at all (subcritical by 22–67×). The hot reading, which *is* this
corpus's own cosmology, misses the screening constant by 1.6–2× at every standard normalisation. So
the agreement is evidence **for the conditions**, not a derivation from recorded structure, and the
obvious rescue — the model's repeated "condensate at finite chemical potential" — does not apply:
that μ is the dark condensate's at basin entry, sixty orders below. The anchor's precision claim is
withdrawn with it: **a band, not 1.57 TeV at 2.5%**, because ∂lnM/∂lnk = 33 amplifies every O(1) —
first sized at 1–8 TeV, and now, with the O(λ) pair computed (the crossed box and its Fock
companion, both downward), standing at **0.55–1.78 TeV**.
And the two bands must be velocity-matched to the percent level (∂lnM/∂r ≈ 11.6) — a match the
one-metric constitution now supplies: two cone slopes would be a dimension-4 Lorentz-violating
coefficient, which the no-bridge clause records as zero ([PRTOE_LV_pricing.md](PRTOE_LV_pricing.md)),
so r = 1 holds exactly (reduced, not derived).

**Adverse, second front.** The genesis draw does **not** pick a handedness, and this is now proven
rather than suspected: the recorded Z4 tilt is invariant under θ → π/2 − θ while the charge L = R²θ̇
is odd under it, so the uniform release prior splits exactly evenly at any tilt strength and under
any CP phase. The proof does not lean on the tilt's four-foldness — which is an input, not a
derivation — because every single-harmonic tilt cos Nθ carries the same reflection, σ: θ → 2π/N − θ.
The chirality family therefore cannot deliver an absolute sign a priori — not pending a
computation, but forbidden by a symmetry the model does not break. What could still have rescued the
cross-messenger test was the *correlation* between θ̇ and the winding. That joint draw has since
been made (#154, 2026-07-20) and finds the two signs **independent** — joint correlation −0.06 to
+0.09 against a ±0.13 floor — so the lock is **void**, not pending
([PRTOE_igmf_helicity.md](PRTOE_igmf_helicity.md); [PRTOE_cosmic_magnetism.md](PRTOE_cosmic_magnetism.md)).

**Adverse, third front — an exposure lost its defence.** The genesis quartic was carried as
quenching a growing superradiant cloud, so P-2026-034's band could hold high measured spins without
the recorded mass being in trouble. Re-derived at the model's own quartic and mass, the margin is
**−83.7 to −85.8 decades** across α_g = 0.1–0.5. The earlier favourable margin rode a
rate-normalization mismatch — a total event rate set equal to a per-particle rate — which put one
power of λ where two belong, worth 90 decades at λ ≈ 2×10⁻⁹¹. At that coupling the field **is** a
free scalar for every superradiance purpose (f_eff = 5×10¹⁶ GeV), so the model meets P-2026-034
undefended and the band's measured spins bear on it directly. The mass does not move — three
independent uses fix it — but the reason the exposure looked survivable is gone.

**Process, and it belongs on this board rather than in a working log.** The reverse audit closed at
110 of 110 completed tasks, with **eleven mis-grades** — every one of them in a *composite* task, and
not one in roughly a hundred single-object checks. One registered prediction was amended on a
misreading of the model's own §2(c) and had to be reversed by a second amendment. Two days of
error-counting are filed at `ForJustin/13`, and the failure mode inverted between them: from
over-claiming favourable results to over-claiming absences.

**Operational.** The nested evidence run was **ended on 2026-07-20 and archived**
(`chains/_archive_polychord_ended_20260720_0915/`). It was never stalled — it was running exactly as
configured, and the configuration costs more than the question is worth on this box: `measure_speeds`
built a 534-slice-step schedule, and at 66 s per likelihood evaluation that is **9.8 h per nested
iteration**, putting the first checkpoint 163 days out and the full run 736 days, with the ΛCDM twin
doubling it. Nested sampling waits for cluster time.

**Deciders** (unchanged in kind, changed in instrument): the **evidence number** (still the Laplace,
now without a confirmer in prospect — it can be sharpened by better-converged chains but not made
robust by them) and SH0ES-vs-TRGB (physical → holds, systematic → inverts). The DE closed form is
real theoretical progress, but it rests on unproven new physics and does not solve the coincidence
problem, and there is no new positive *evidence* that upgrades the evidence class.

---
### Baseline (2026-07-08) — kept for the record; superseded where the section above says so.

## The single kill-shot (task Q3 / #21)

**The +1.2% varying electron-mass shift being real.** It is the load-bearing bolt: it is
simultaneously (a) the engine of the H₀ easing and (b) the model's primary observable signature.
If a full systematics/degeneracy audit (Q2/#20) or better CMB data (CMB-S4) shows the shift is
consistent with m_e = 1 — i.e. that N_eff, the calibration, or the SH0ES prior absorbs the same
improvement — the headline collapses and only the (unbuilt) DE floor remains. **Everything hangs
on this one number being physics, not a degeneracy artifact.**
Runners-up: a negative evidence verdict (Q1/#19), or DESI pinning w robustly away from -1.

## The two least-trusted joints (task Q5 / #23)

Ranked, honestly:
1. **The DE-floor self-tuning mechanism** — no working mechanism; the self-tuning toy ran away
   when computed; Weinberg's no-go for self-tuning is unaddressed. Trusted least. (Q4/#22.)
2. **The m_e shift's robustness** — unproven it isn't absorbing a systematic. (Q2/#20.)
3. **c's derivation is one step short.** The census sources the seating (the neutrino sits on the
   vacuum's seat because its mass is medium-sourced, not electroweak) and two independent routes pin
   the value, but the step licensing a democratic count is open — see the Current section at the head
   of this file. The empirical pin to [1.0, 1.9] is consistent with it. (Q5/#23.)

## The near-term falsifier calendar (task Q6 / #24)

In order of arrival / actionability:
1. **PRTOE-vs-ΛCDM full-data evidence** (Q1/#19) — running now (matched optimizers). Δchi2/ΔBIC/ΔlnZ.
2. **Ω_k / shape** — deferred (single-chain MCMC too slow); quick geometric check already says
   flat keeps H₀, closed lowers it → flat-3-torus is the H₀-safe shape (P-2026-013 refined).
3. **DESI DR2 w-running** — data exists; compare against the dCDF w=-1 prediction.
4. **The m_e degeneracy audit** (Q2/#20) — runnable; highest-value un-run test.
5. Slow: LiteBIRD β (P-2026-009/015), CMB-S4, halo vortices (P-2026-016), direct-detection
   nulls (P-2026-017), matched circles / low-quadrupole (P-2026-013).

## Pre-committed evidence verdict (locked 2026-07-08, before #19 returns)

internal review rule: lock what counts as a win before the number comes back, or we rationalize whatever
we get. For the PRTOE-vs-ΛCDM full-data comparison (the evidence run — Laplace landed 2026-07-09,
and the Laplace is what the thresholds are graded against, nested sampling being deferred to
cluster time), verdict thresholds committed now:
  - PRTOE wins:   Δ lnZ ≥ +2.5 in PRTOE's favor (moderate+) AND Δ BIC ≤ -2
                  (BIC/AIC already penalize PRTOE's ~2 extra physical params: varying_me, m_ncdm).
  - ΛCDM wins:    Δ lnZ ≤ -2.5  OR  Δ BIC ≥ +2.
  - inconclusive: anything in between -- and this is the honestly-expected outcome, since PRTOE is
                  ΛCDM-like + the m_e signature; a decisive win would be a genuine surprise.
No moving these after the optimizers finish. (Optimizer gives a Laplace ln Z + bestfit χ² for
BIC/AIC. A gold-standard nested ln Z would be the publication number, and it is not in reach on
this hardware — that number waits on cluster time and the thresholds are graded on the Laplace
meanwhile, with its systematic stated wherever the verdict is quoted.)

## #22 DE-floor — the one serious calculation, resolved (2026-07-08)

`scripts/floor_ghost_condensate.py`. Ran internal review's demanded single calculation of the (δ K)² /
ghost-condensate critical-point floor. k-essence P(X): ρ=2X P_X - P, p=P, c_s²=P_X/(P_X+2X P_XX).
Results:
  - w=-1 exactly at P_X=0 (X0), c_s²=0 there → exact de Sitter floor. And for X<X0, c_s²<0 (unstable)
    → the floor is an attractor approached from above (field cannot sit below it). Good feature.
  - Stability: pass. The c_s²=0 flat direction is stabilized by the (δ K)² k⁴ term
    (ω² = α/M² k⁴ > 0 for α>0; window P_XX>0 & α>0, Arkani-Hamed+ 2004). The
    self-tuning toy ran away only because it dropped that k⁴ term; with it, the floor holds.
  - Self-tuning: fail. V0(=Λ) is a free, tuned parameter -- mechanism does not explain why
    Λ is small (Weinberg's no-go stands).
Verdict (internal review fight-or-concede resolved): keep the stable dynamical w=-1 floor (a real mechanism,
an attractor, better than a bare constant); concede the self-tuning / "solves the cosmological-constant
problem" claim. Update the least-trusted-joints ranking: the floor is no longer "no working mechanism"
-- it has a stable mechanism -- it just isn't a CC-problem solution (which we should never have claimed).

## Code-vs-theory audit (2026-07-08, re-checked 2026-07-19) — the link is unenforced in code, but the fit no longer floats m_e

Audited the CLASS C source against the model's claims. Good: dcdf has a real perturbation sector
(δ/θ/delta_p) -- old gap closed; the w=-1 floor is asymptotic/never-crossed (matches the
#22 ghost-condensate attractor).

**Closed 2026-07-23 — gaps 1 and 2 (the m_e / screening coupling):**
  1. **m_e from the dark sector.** `dcdf_dyad_link=yes` derives
     `varying_me = 1 + c·f_amp·Psi0/M_red` (the #11 amplitude stack) at input time and stores
     the stack on the background structure. Thermodynamics does not invent m_e; it consumes
     `background_varconst_of_z` / the background table. Production configs may still pin
     `varying_me` without the link for chain continuity; the model path is `dcdf_dyad_link`.
  2. **Density-dependent Theta / gate screening.** With `dcdf_dyad_link` on (or
     `varconst_density_gate=yes`), the environmental switch is the survival-form gate
     `S = exp(-(max(Δ,0)/C_ref)^n)` (me_mechanism_math the gate), not a pure redshift step.
     Homogeneous FRW uses a growth-proxy load calibrated at `varying_transition_redshift`;
     local environments call `background_varconst_of_z_delta(z, delta)` — voids (δ≤0) keep
     the bare value (P-2026-007), clusters screen to lab. Legacy pure-z window remains when
     the density gate is off (default without `dcdf_dyad_link`).
  3. **The w=1/3 radiation-like phase is in the code and enabled** (closed earlier).
     `dcdf_z_rad_onset` drives the conformal-origin phase; evidence configs set it live.
  (Checked 2026-07-20: `cs2_dcdf` returns 0.0 unconditionally — c_s² ≡ 0 after β removal.)

Honest implication (as of 2026-07-23): the code-level link from the electron-coupled scalar to m_e
and the density gate are implemented end-to-end. Homogeneous FRW uses the **actual growth factor
D(z)** from the background table (load = C_ref · D(z)/D(z_trans)), recomputed after D is normalized
to today; local void/cluster discrimination is `background_varconst_of_z_delta(z, δ)`. Production
fixed-me configs carry `dcdf_dyad_link: yes`; sampled-me configs carry `varconst_density_gate: yes`.

## Evidence verdict — landed 2026-07-09 (Laplace; the pre-committed gate met, marginally)

The constrained electron-coupled-scalar vs ΛCDM full-data comparison (matched optimizers, same 10
likelihoods) converged. Result graded cold against the pre-committed gate:
  - ΛCDM:    χ² = 2809.179 | Laplace lnZ = -1474.566 | H₀ = 68.18
  - scalar:  χ² = 2799.654 | Laplace lnZ = -1471.931 | H₀ = 69.82  (m_e fixed at 1.01232)
  - Δ χ² = -9.52 (scalar better) ; **Δ lnZ = +2.635 (Laplace, scalar favored)** ; Δ BIC ~ -9.5.

**Verdict: the +2.5 win threshold is crossed (+2.635) — the first time — but heavily qualified:**
  1. Laplace, and the Laplace is where it stays: margin over the line (+0.135) < the estimator's own
     systematic uncertainty ⇒ a marginal crossing on the approximate number. Only nested sampling
     makes it robust, and nested sampling is unaffordable on this hardware (9.8 h per iteration) —
     so the crossing stands as marginal, without the confirmer it was explicitly awaiting, until
     cluster time is bought. Better-converged chains sharpen this number; they cannot promote it.
  2. SH0ES-conditional: the -9.52 edge is dominated by SN+SH0ES (~-13.7, the H₀ easing
     68.18→69.82) + ACT (~-3.8, high-l m_e). So the win rides on the H₀ tension being physical
     (Stage 0). SH0ES-as-systematic sinks it. The win and the single window are the same brick.
  3. Gate A sidestepped (stronger than passed): m_e was fixed, not floated → no prior to game;
     the win comes from a better fit with m_e pinned at the prediction.
  4. Gate B caps it suggestive (f_amp partial-mover, Psi0 OOM-fixed); shot 1 survives (amplitude
     ontology un-derived). w=1/3 phase confirmed neutral (onset never moved) → kept, free.

**Label: suggestive / SH0ES-conditional / Laplace-marginal win.** Best realistic outcome on the
table, landed exactly at the line. Not decisive, not robust, not prediction-confirmed.

The one lever that would move the evidence class hard is still a nested confirmation of the +2.6
on a paid cluster (configs pc_prtoe.yaml / pc_lcdm.yaml ready) — **and that lever is now out of
reach until the cluster time is bought**, the attempt on this hardware having been ended on
2026-07-20 at 9.8 h per iteration. The two things that still sink it: SH0ES-as-systematic
(Stage 0), or a nested number eventually pulling +2.6 back under +2.5. Full internal review
grading in the private internal review record (defender "the number" turn).

### Sharpened by internal review (accepted): the win inverts without SH0ES, adds zero ontology evidence
Two corrections to the verdict above, both taken: (1) Brake 2 is worse than "conditional" — it is
SH0ES-dependent: net Δ χ² -9.52 minus SH0ES ~-13.7 = +4.2, i.e. without SH0ES the
electron-coupled scalar is ~4 worse than ΛCDM (the edge inverts to a loss). The m_e signature alone
(ACT -3.8) does not beat the ~+8 Planck-lowlEE/BAO/SPT cost, so m_e wins only by easing the SH0ES
H₀ tension — not on CMB-internal merits. And that easing is non-original (whole varying-m_e family
does it, the internal review), so the win adds zero evidence for the ontology
(superfluid/census/electron-coupled scalar). (2) The win is robust only
if both a nested ln Z confirms +2.6 and SH0ES is physical (two live-uncertain gates — **and the
first is now unscheduled**, nested sampling having been priced off this hardware and deferred to
cluster time). Final label: "suggestive / SH0ES-dependent / Laplace-marginal / non-original-class
win, no ontology evidence." Deciders from here: a nested ln Z when it can be afforded
(marginal→robust or sinks it) and SH0ES-vs-TRGB (physical→holds, systematic→inverts to a loss).

---

## Discipline triage (2026-08-03)

**Grade:** ledger/history — process record, not a physics derivation.
**Discipline:** above story-grade *as a record* (append-only / living map discipline).
**Triage:** stay shelf as LEDGER/HISTORY; not Failures; not exploratory.
**Non-claims:** no physics COMPLETE from this file alone.
**Rule:** `docs/working_logs/STORY_GRADE_ELEVATION_RULE.md`
