# Chain status, 2026-07-28 — read at 5h00m elapsed

**This is a preliminary read of running chains, not a verdict.** Stated up front per protocol
check 33: the numbers below are adverse to the model, and they are being recorded at the moment they
were seen rather than after they improve.

## The two runs are directly comparable

Both `cmp_lcdm_mnu_bbnfix` (reference) and `dyad_mnu_bbnfix` (the model) carry the **identical**
ten-likelihood stack — Planck 2018 lowl.TT, lowl.EE, highl_plik.TTTEEE_lite, lensing.clik; BAO
6dF/MGS/DR12; Pantheon+SH0ES; ACT DR6; SPT-3G lite. Verified by reading both `.updated.yaml`
likelihood blocks. So −log(posterior) can be set side by side, with the caveat that it includes
priors and the two models do not carry the same parameter count.

## Where they stand

| | best −logpost | rank agreement | burn-in |
|---|---|---|---|
| ΛCDM+mν reference | **1380.51** | ranks at 1383/1385/1384 — agree to ~2 | nearly complete |
| the model | **1421.60** | ranks at 1422/1615/1472 — spread **193** | far from complete |

**Current gap: 41.1 log-units, Δχ² ≈ 82, in favour of ΛCDM+mν.**

## The two problems, separately

**1. The model's chains have not mixed.** Only rank 1 has found the high-H₀ region (H₀ = 69.4);
ranks 2 and 3 sit at H₀ ≈ 64 with −logpost 193 and 51 units worse. One chain in three is in the
region the model exists to occupy. No Gelman–Rubin statistic has been produced in five hours, and
none should be trusted until all three ranks share a basin.

**2. The best chain has not yet reached the reference's level.** Rank 1's descent, by sixths — but
see the correction below on how little weight these last points carry:

```
1519.04 → 1501.96 → 1491.45 → 1468.06 → 1429.65 → 1425.09 → 1421.60
   drop:    17.1      10.5      23.4      38.4       4.6       3.5
```

The last three segments dropped 38, 4.6, 3.5. That is a chain settling into a basin near 1421, not
one still driving toward 1380. If it holds, the gap is real.

**Against reading too much into it — and one correction to an earlier reading in this same file.**

Rank 1 has only **127** samples, and the "flattening" above is measured over sixths of that, so the
last three points average 21 samples each. At that count the drops of 4.6 and 3.5 are not
distinguishable from noise. The descent is not established as having stopped; it is established as
not obviously continuing, which is a much weaker statement.

**The proposal is fine.** An earlier pass in this session attributed the 98–99% acceptance to a
too-narrow seed covariance. That was checked and is wrong. Comparing the seed's diagonal to the
spread each parameter has actually explored gives ratios between 0.74 and 1.80 across all thirteen
parameters — a well-scaled proposal, not a tight one:

```
omega_b 0.80   H0 0.81   logA 1.68   n_s 1.29   z_reio 1.80   dcdf_rho_inf 0.77
varying_me 0.75   A_planck 1.27   A_act 1.30   P_act 0.83   Tcal 1.16   Ecal 0.95   m_ncdm 0.74
```

So the high acceptance has the ordinary explanation: these chains are descending steeply toward the
mode, and while descending, nearly every proposal is uphill and gets accepted. Acceptance near unity
is what burn-in looks like, not what a broken proposal looks like. It should fall toward ~25% once
the chains reach the typical set. The correct summary is that the runs are **correctly configured and
simply early** — the ten-likelihood stack with CLASS is expensive, and 127–489 samples in five hours
is the cost of that stack, not a symptom.

## What would change this read

- ranks 2 and 3 reaching the high-H₀ basin, which is required before any R−1 means anything
- acceptance falling from ~99% toward ~25%, which is the signal that burn-in has ended and the
  chains have reached the typical set; until then every number here is a burn-in snapshot
- rank 1 accumulating enough samples that its trend is measured over hundreds rather than twenty

## Machine

12 cores. Six MPI ranks pinned to cores 0–7, the toroidal run on core 8, cores 9–11 left free per
the standing headroom constraint. Load 11.1 against 9 cores in use. Nothing is starved and nothing
needs moving; the runs are slow because the likelihood stack is heavy, not because they are
competing.

## What must not be done meanwhile

No evidence number, no Δln Z, and no fit-quality claim may be quoted from these chains in their
current state — in either direction. The gap above is not yet a result against the model any more
than an earlier snapshot would have been a result for it.

---

## The toroidal fork, first branch (recorded 2026-07-28, mid-run)

`scripts/ring_toroidal_3d.py`, docket #42 — link 4's toroidal half. The run is a **pair**: it
integrates n = +1 to t = 8, then n = −1 from scratch, and the verdict is defined only on the pair.
Recorded here at the halfway point so the first branch's numbers exist independently of whatever the
second returns.

**n = +1 — complete.** Ring detected in every frame from t = 0.25 through t = 7.75; best ring at
t = 1.00, r̄ = 4.3, z̄ = 10.5, **16/16 azimuthal bins populated** (a full ring, not a partial arc).

| observable | value |
|---|---|
| **(A)** shape helicity | **−1** (m₁ amplitude 0.36) |
| **(B)** core-circuit winding W | **−1.19**, excess **−2.19** |

**Both readings are armed.** The script's verdict requires, for (A), helicity ≠ 0 and an exact sign
flip; for (B), \|excess\| > 0.5 and the pair summing to within 0.5 of zero. The first condition of
each is met (−1 ≠ 0; 2.19 > 0.5), so neither reading is dead going in and the fork is live.

**What n = −1 must return:** helicity **+1** for (A) to lock; excess **≈ +2.19** for (B) to lock.
The four outcomes are pre-registered in the script — A only, B only, both (the two readings are one
object here), or neither (*the toroidal sign is not set by the fountain-on-winding roll-up in this
geometry*, both to the ledger). None of them is a non-result.

**On the energy drift, stated before anyone objects to it.** Drift reached 83% by t = 7.75 and is
sponge dissipation, measured separately at 12,705× the sponge-off rate. It is large, and it does
**not** touch this verdict: both observables are geometric — a helicity sign and a winding excess —
not energy budgets. The load-bearing fact is that the ring persisted with all 16 bins filled, which
the frame log confirms at every step.

---

## UPDATE at 6h10m — the gap closed, and then reversed

The 41-log-unit deficit recorded above **is gone**. Read again six hours in:

| | best −logpost | per-rank minima | mixed? |
|---|---|---|---|
| ΛCDM+mν reference | **1379.79** | 1380.56 / 1379.79 / 1379.91 | yes — spread 0.8 |
| the model | **1379.23** | 1379.23 / 1611.68 / 1443.42 | **no** — spread 232 |

The model's leading rank is now **0.6 log-units ahead** of the reference's best point, where six
hours ago it was 41 behind. Its descent, by fifths:

```
1490.18 → 1423.38 → 1409.95 → 1387.11 → 1379.23      (minimum of each fifth)
```

Monotone, and **the overall minimum sits in the most recent fifth** — so it has not settled either.

**What this vindicates, and what it does not.** The earlier entry said in terms: *"the descent is
not established as having stopped; it is established as not obviously continuing"*, and refused to
call the 41 a verdict. That caution was correct and the number moved by 42 log-units inside a day.
It does **not** vindicate the model: one rank of three is in the basin, the other two sit at 1612 and
1443, and a comparison across a 232-unit spread means nothing.

**The rule this pair keeps demonstrating: a burn-in number is not a weak measurement, it is not a
measurement.** It moved 42 units in one direction today and could move again. The reference is
nearly mixed (spread 0.8); the model is not (spread 232). Until that second number looks like the
first, neither the adverse reading nor the favourable one is quotable — and both have now appeared
in the same session, which is the cheapest possible demonstration of why.

---

## UPDATE at 6h45m — nothing is trapped, but rank 2 is the bottleneck by ~20×

All three dyad ranks are still **descending** — none has stalled in a false basin, which was the
worry when the spread was first noticed. What they differ in is rate and starting point:

| rank | n | H₀ | −logpost first-q → last-q | drop | gap to ~1380 |
|---|---|---|---|---|---|
| 1 | 325 | **69.90** | 1496.28 → 1382.18 | 114.1 | **2.2** |
| 2 | 1173 | 64.00 | 1638.84 → 1614.09 | 24.8 | **234.1** |
| 3 | 498 | 64.68 | 1499.86 → 1446.70 | 53.2 | 66.6 |

**Rank 1 is essentially there** and is the one at high H₀ — the region the model exists to occupy.
Rank 3 is closing. Rank 2 is 234 log-units out and descending at a fifth of rank 3's rate.

**A crude linear extrapolation** — and it is crude, of a descent that is plainly not linear, so take
it as an order-of-magnitude statement about *which* rank binds rather than *when*: rank 1 needs ~6
more samples, rank 3 ~625, **rank 2 ~11,000**. Rank 2 is the convergence bottleneck by roughly a
factor of 20 over rank 3.

**One oddity worth noting: the sample counts are wildly unequal** — 325 / 1173 / 498 for ranks
launched together. Rank 2 has 3.6× rank 1's samples while making a fifth of the progress. The likely
reason is that its region (H₀ = 64, away from the model's basin) is cheaper for CLASS to evaluate,
so it accumulates samples fast while going nowhere useful. **That is worth knowing before anyone
reads sample count as progress** — on this pair the rank with the most samples is the least
converged.

**What this does not change.** Gelman–Rubin still has no row, the spread is still 232, and nothing
from this pair is quotable. What it adds is that the obstacle is identified and is not pathological:
one slow rank in a cheap-but-wrong region, not a trapped chain.

---

## The toroidal pair is dynamically identical apart from the winding sign — a check worth having

Noticed by accident: the n = −1 branch reported E-drift **58.113%** at t = 3.50, and the n = +1
branch had reported **58.113%** at the same timestep. Comparing every shared timestep:

| t | n = +1 | n = −1 | diff (pp) |
|---|---|---|---|
| 1.00 | 16.110% | 16.113% | 0.003 |
| 1.50 | 23.806% | 23.813% | 0.007 |
| 2.00 | 34.012% | 34.020% | 0.008 |
| 2.50 | 44.095% | 44.103% | 0.008 |
| 3.00 | 52.141% | 52.145% | 0.004 |
| 3.50 | 58.113% | 58.113% | 0.000 |

**Worst disagreement 0.008 percentage points on a quantity that has reached 58** — a relative match
of 1.4×10⁻⁴ across all eleven shared frames.

**Why this matters for the verdict.** The fork grades a *difference* between the branches
(helicity sign, winding excess). That difference is only interpretable if the branches are
otherwise the same run. This shows they are: the sponge dissipation, the ring's evolution and the
energy budget all mirror to four significant figures. **Any asymmetry the verdict finds is
attributable to the winding, not to the two integrations having diverged numerically.** That could
not have been assumed and is now measured.

**It also disposes of the obvious objection to the drift.** An energy drift reaching 82% by t = 7.75
looks disqualifying read alone. A drift reproducible to 10⁻⁴ across a parity pair is a controlled
property of the integrator and its sponge, not numerical noise — and the graded observables sit on
top of a background both branches share exactly.

*(Recorded because a referee would ask for it, and reconstructing it later would mean re-reading a
log that will by then be twice as long.)*

---

# EVENING UPDATE — 21:58, and the picture changed twice

**Read the section above as superseded on the model chain.** It recorded a preliminary, adverse
read at 5 h elapsed. Two things have since been established, one of which invalidates the way that
comparison was framed and one of which is a repair.

## 1. The model chain's ranks were in three different basins

`scripts/rank_basin_diagnostic.py`, run because an external reviewer named "all three MPI ranks in
one basin" as the single thing that would move the program. The answer was no:

| | best −logpost per rank | spread | worst per-parameter rank separation |
|---|---|---|---|
| reference | 1379.48 / 1379.80 / 1379.91 | **0.43** | 12.6 s.e. |
| **model** | **1377.89 / 1610.55 / 1436.67** | **232.7** | **23,855 s.e.** (dcdf_rho_inf) |

Ranks disagreed on H₀ (69.5 / 64.0 / 64.8) with two pinned at the **H₀ prior floor of 64.0**, on
dcdf_rho_inf and on varying_me. **So the widely-quoted 1377.89 was one rank of three** — the one that
found a good region while the other two did not. That is a much harder disqualification of the live
comparison than the sampling-asymmetry argument recorded earlier, and it has been written into the
risk page and into the Fairbank letter, which is outward-facing.

## 2. Diagnosed, repaired, and the repair verified

~~The cause was a **self-locking loop**: cobaya re-learns its proposal only when R−1 is below
`learn_proposal_Rminus1_max` (2.0, or 30.0 early), which a chain with ranks in different basins never
reaches — *the mechanism that fixes the proposal was gated behind the problem it fixes.* Confirmed by
file times: the reference covmat was rewritten mid-run, the model's had not changed since before its
own launch.~~

**↑ WITHDRAWN 2026-07-29. That was not the mechanism that fired.** See protocol 47. Isolating the
archived run's MPI section (the launchlog is append-mode, so the last rank-prefixed `Sampling!` line
has to be found first) shows the actual cause:

> Proposal learning is a **collective checkpoint** — every rank must reach a multiple of
> `learn_every` = 40·d accepted samples before *any* proceeds. With d = 13 that is **520 per rank**,
> and the ranks held **467 / 1684 / 658**. The log has ranks 1 and 2 announcing *"Ready to check
> convergence and learn a new proposal covmat (waiting for the rest…)"* and rank 0 never announcing
> it. **"All chains are ready" never appears; no convergence statistic was ever computed** — hence
> the empty `.progress`. Two ranks blocked for hours on a third that was **53 samples** short.

The R−1 gate is real and would plausibly have bitten next, but **it was never reached**, so the
"self-locking loop" framing — and the claim that more wall-clock could not help — was not
established. The file-time evidence proves less than claimed too: an unchanged covmat means nothing
until `learn_every` has been reached. What stands unchanged: the proposal was never re-learned, the
ranks never merged, and the reseed was the right remedy under either mechanism.

**The re-tune addressed the R−1 gate (raised thresholds) but not this one — and did not need to.**
The collective checkpoint is not a defect to fix; it just requires the ranks to arrive together. The
leading indicator is therefore **rank-count spread**, and on the live run it is now excellent:
**19 / 15 / 14** accepted (spread 5) against the archived run's spread of **1217**. The reseeded
covariance made the ranks track, which is precisely what prevents the block. First collective
checkpoint expected at 520/rank, ≈ 08:00; no `"waiting for the rest"` line has appeared so far.

**Owner-authorised re-tune, executed 21:35.** Archived to
`_archive_dyad_prefix_20260728_2140/` first (the relaunch used `-f`, which deletes chain files).
Reference chain **not touched** and still running. Three changes: a covmat built from the good rank
(the seed's *marginal widths were already right* at 0.77–1.13, so the fault was correlation
structure); `learn_proposal_Rminus1_max` 2.0 → 100 and early 30 → 1000; `burn_in` 40 → 60.

**Verified working, measured from deltas between consecutive same-rank reports:**

| | acceptance |
|---|---|
| archived run | 5.27 / 5.52 / 6.17 % |
| **re-tuned run** | **32.2 / 34.4 / 32.5 %** (pooled 33.0%) |
| optimum | ~25% |

**~6×, onto roughly optimal, with all three ranks within two points of each other.** Initial points
now cluster at H₀ = 70.47 / 69.88 / 69.90 against the archived run's terminal 64.0 / 64.8.

## 3. Two other chains are dead and were being described as alive

- **`cmp_prtoe_routeD`** — named in the math spine as "the single decider" for the w = −1 fork.
  **One chain file**, last written **2026-07-20**. ~~Gelman–Rubin is a between-chain statistic, so a
  one-chain run yields no convergence number *however long it runs*.~~ **Corrected 2026-07-29 — and
  this file contradicted itself two bullets apart, since the next entry quotes R−1 = 13.25 from a
  one-chain run.** With a single process the sampler splits the chain into `Rminus1_single_split`
  segments (default 4) and computes a within-chain split-R̂, so a number *is* produced. What it
  cannot do is detect confinement to one basin — every segment shares it — which is exactly the
  failure mode being tested. **The gate was therefore waiting on a statistic blind to the question,
  which is worse than unsatisfiable: it could have returned a reassuring number.**
  *(Since relaunched with 2 ranks, 2026-07-28 22:51 — see #21.)*
- **`cmp_prtoe_conv_desi`** — described as "(running)" in two forward-facing files. One chain file,
  last written **2026-07-22**, R−1 = 13.25. It has now died twice. The S₈ posterior is **unproduced,
  not pending.**

Both corrected in place; relaunching either is an owner decision.

## What is actually live, verified against `ps`

`cmp_lcdm_mnu_bbnfix` (10 h+, adapting normally), `dyad_mnu_bbnfix` (re-tuned, burning in,
~830 of 901 accepted steps remaining), `ring_toroidal_3d.py` (9 h 53 m, t = 7.75/8). Nothing else.
Seven cores of twelve; 9–11 idle.

## The standing claim, unchanged

**The live evidence comparison remains a wash and is quotable in neither direction.** Better
acceptance is a necessary condition for mixing, not a sufficient one — a well-tuned proposal can
still be trapped. The pre-committed check (#84) is graded on **rank spread**, not on acceptance:
spread must fall well below 232.7, or the H₀-floor trap is a real feature of this likelihood surface
and gets written up as physics rather than met with more tuning.

## Measured 2026-07-29 00:09 — the re-tune's first half worked

Burn-in target confirmed as **900** accepted steps, i.e. `burn_in: 60` × the ~15 oversampling
factor, exactly as the diagnosis predicted. Acceptance now, read from the sampler's own step
counters:

| rank | accepted | steps taken | acceptance | burn-in done |
|---|---|---|---|---|
| 0 | 742 | 2329 | **31.9 %** | 82.4 % |
| 1 | 745 | 2385 | **31.2 %** | 82.8 % |
| 2 | 709 | 2233 | **31.8 %** | 78.8 % |

Against **5.3–6.2 % before the re-tune**: a 5.4× lift, landing just above the ~25 % target rather
than five times below it. The reference chain sits at 9.1–9.3 % on the same counters (it was
8.5–8.9 % when the letter was drafted; it has drifted up as the run continued).

**This settles the proposal question and nothing else.** Acceptance was the diagnosed defect and the
defect is repaired; whether the three ranks now agree about *where the posterior is* is a separate
question that only samples can answer, and none have been written yet. At rank 1's rate the
remaining 155 accepted steps take ~30 min, so #84 becomes gradeable shortly after 00:40. **The
threshold is unchanged and was fixed before any post-fix sample existed.**

### Mid-run environment change, logged 2026-07-29 00:13

Cores 0–8 were carrying **nine** processes at ~100 % each — 3 reference ranks, 3 model ranks,
2 route-D ranks, and the circulation instrument — i.e. exactly saturated, with load average 12.78.
The model chain's step rate had dropped to 2 steps in 108 s, from 32 in 116 s minutes earlier.

The circulation instrument (pid 1838176, non-MCMC) was re-pinned from core 8 to **cores 9–11**,
which the owner released tonight for non-MCMC work. Verified: affinity mask `100` → `e00`. Nothing
was stopped, and no MCMC process was touched.

**Recorded because it changes timing mid-run.** Any later step-rate comparison across 00:13 is
comparing two different machines, and the burn-in duration figures above were measured before it.

### #84 pre-registration, sharpened — written 2026-07-29 00:12:05 with ZERO sample files on disk

Attested: `ls chains/dyad_mnu_bbnfix.[0-9].txt | wc -l` = **0** at the moment of writing. Nothing
below was chosen with knowledge of a post-re-tune sample.

**The primary criterion is unchanged and still governs:** spread in best −logpost across ranks must
fall **well below 232.7**, and worst per-parameter rank separation **well below 23,855 s.e.**

"Well below" is a direction, not a threshold, so it can be satisfied by a chain that is still badly
broken. Fixing the scale now, before data. The only non-arbitrary yardstick available is the
**contemporaneous reference chain**, measured today at ~720 samples/rank:

> reference: spread **0.323**, worst separation **10.5 s.e.** (on `A_planck`, a calibration
> nuisance; its cosmological parameters sit at 4.0–5.9)

The model chain carries two extra sampled parameters and should not be held to the reference's
number exactly. Pre-committed bands:

| verdict | condition |
|---|---|
| **PASS — the trap was a sampler defect** | spread ≤ **5.0** AND worst separation ≤ **100 s.e.** |
| **AMBIGUOUS — re-tune helped, not settled** | anything between |
| **FAIL — the H₀ floor is real physics** | spread ≥ **50** OR worst separation ≥ **1000 s.e.** |

**Two grading conditions that matter more than the bands, and are the easy things to get wrong:**

1. **Do not grade on the first samples.** Immediately after burn-in each rank has a handful of
   points; a spread computed on ten samples is noise wearing a verdict's clothes. **Grade only once
   every rank holds ≥ 200 post-burn-in samples.** If I report a #84 verdict before that, the verdict
   is void regardless of which way it fell.
2. **Grade at matched sample count.** The ranks will not finish burn-in together (rank 2 trails
   rank 1 by ~40 accepted steps already), and the diagnostic's second-half statistics are
   sample-count sensitive. Truncate all ranks to the shortest before comparing.

**AMENDMENT, 00:22, still with zero sample files on disk.** A second instrument
(`scripts/rank_separation_ess.py`) found that the s.e. figures above are inflated: the original
diagnostic divides by the raw sample count, treating autocorrelated samples as independent, and
compares ranks at unmatched lengths. Measured τ_int ≈ 23–68. Re-graded on the archived pre-re-tune
model chain: **23,855 → 2,102 (matching lengths) → 317 (honest ESS)**, a 75× overstatement. The
reference chain re-grades **12.6 → 1.6 honest s.e.**, i.e. *consistent with one basin*.

**The bands above are NOT moved.** They were fixed in naive units and they stay in naive units —
that is what makes them a pre-registration rather than a preference. Grade against them as written,
using `rank_basin_diagnostic.py`. Then report the honest figure alongside, from the new instrument,
for anything that gets quoted. Two numbers, both stated, neither substituted for the other.

**DRY RUN 2026-07-29 01:52 — machinery verified, numbers VOID and not to be quoted.** Both grading
instruments were run end-to-end at 91/70/52 rows to confirm they work before the decisive moment.
They do. **The numbers they produced are discarded** under grading condition 1 above, and are
recorded here only so that nobody later finds them in a terminal scrollback and mistakes them for a
result:

> *void — 52 rows against a 200 gate:* spread 24.8, worst separation 7,400 s.e. naive / 258.6 honest.

That would read as a FAIL, **and it does not count.** The reason is visible in the instrument's own
output: at 52 rows the effective sample size per rank-half is **5–11**. A spread computed on that is
noise, and this is precisely the failure the gate was written to prevent — the tempting case being
exactly this one, where numbers exist and point somewhere. Two things that are *not* verdicts: the
two instruments agree structurally (ESS inflation 2.0×, consistent across parameters, control
passing), and the ranks' best −logpost sit at 1405 / 1390 / 1380 — deliberately **not** compared to
the archived spread of 233, since a statistic at 52 samples is not comparable to one at 467+.

### The reference chain's R−1 moved — first update in 6h24m, and a pre-registered test of the trend

At **02:45:58** the ΛCDM chain hit its collective checkpoint at 880/908/892 per rank and reported

> **R−1 = 1.011 (N = 1396) → 0.522 (N = 2680)**

Two points only, so the reading is thin, but they are clean: samples ×1.92, R−1 ×0.517, i.e.
**R−1 ∝ N^−1.01** — which is the *expected* asymptotic scaling for a well-mixing chain, not a
surprise. Straight extrapolation reaches the `Rminus1_stop: 0.05` at **N ≈ 28,000**, under the
40,000 cap, at **≈ 3.3 accepted/min → roughly 5 days**.

**That is materially better than the standing forecast**, which said this chain needed 7.5×10⁴–9.7×10⁶
samples and would not reach its cap for 83 days. The difference is explicable rather than
contradictory: that forecast predates the MPI relaunch and was fitted to a *single-chain* trajectory,
where R−1 was a within-chain split-R̂. This is the first genuine between-chain trajectory the run has
produced.

> **PRE-REGISTERED, written now with only two points on the board.** `learn_every` = 480/rank fires
> next at **1440/rank, N ≈ 4320**. If R−1 ∝ 1/N holds, that checkpoint should report
> **R−1 ≈ 0.32**. Materially above (say > 0.42) means the 1/N reading is wrong and the optimistic
> projection dies with it; materially below (< 0.24) means it is falling faster than 1/N and the
> five-day figure is conservative. **Either way the two-point extrapolation above must not be quoted
> as a forecast until this third point lands** — two points fit any monotone law.

**Not converged, and nothing is licensed yet.** 0.522 is an order of magnitude above the stop
condition, the letter's H₀ figure stays gated, and the acceptance column in that progress row (0.9669)
remains the pinned-near-unity artifact, not a health metric.

## #84 — GRADED 2026-07-29 04:43. Verdict: **AMBIGUOUS.**

The gate opened at 04:42 (252/227/205 rows, every rank past 200). Graded against the bands fixed at
00:12:05 with **zero sample files on disk**, at matched truncation to 205 rows/rank as grading
condition 2 requires.

| criterion | pre-registered | measured | |
|---|---|---|---|
| spread in best −logpost | PASS ≤ 5.0 · FAIL ≥ 50 | **7.448** | misses PASS, far from FAIL |
| worst rank separation | PASS ≤ 100 s.e. · FAIL ≥ 1000 | **55.2 s.e.** | passes |

PASS required **both**. The separation criterion is met with room to spare; the spread is 7.45
against a 5.0 threshold, so it does not pass. FAIL required either trigger and neither fires.
**AMBIGUOUS: the re-tune helped and did not settle it.**

**The improvement is large and real.** Against the archived pre-re-tune chain: spread **233 → 7.45**,
worst separation **23,855 → 55.2** naive. Acceptance **5.3–6.2 % → 31 %**. Rank-count spread
**1217 → single digits**. The ranks have gone from three different basins to three readings of what
is plausibly one — the best −logpost values are now 1385.5 / 1386.0 / 1378.6 against the archived
1377.9 / 1610.6 / 1436.7.

**But 7.45 is not ≤ 5.0, and that number was fixed before any post-fix sample existed precisely so it
could not be reached for afterwards.** The pre-registration's own wording — *"spread must fall well
below 232.7… else the H₀-floor trap is real physics, not a sampler defect"* — is not satisfied.

**Honest ESS figure, reported alongside as the amendment requires:** worst separation **18.1 honest
s.e.** on `varying_me` (τ_int ≈ 17–22, N_eff ≈ 5–7 per rank-half), a 3.1× inflation over naive.
Control passed — every honest z at or below its naive z.

**WHAT THIS LICENSES:** that the proposal defect is repaired and the basin problem greatly reduced.
**WHAT IT DOES NOT LICENSE:** that the H₀-floor trap was purely a sampler artifact. That question is
still open — but on a far narrower margin than before, and it is now answerable by more sampling
rather than by more tuning, which was not true of the archived run.

### A flaw in my own criteria, found after grading and recorded WITHOUT revising the verdict

Checked immediately after the grade, because AMBIGUOUS invites a re-grade at larger N and I wanted to
know whether that would be legitimate. **The two criteria have opposite N-dependence, and I did not
account for it when writing them.**

| N/rank | 25 | 50 | 75 | 100 | 150 | 205 |
|---|---|---|---|---|---|---|
| spread | 25.23 | 24.79 | 25.04 | 25.04 | 12.94 | **7.45** |

- **The SPREAD criterion gets mechanically easier with N, and is therefore the weak one.** Best-so-far
  is a running minimum, so given enough samples every rank finds the same global minimum and the
  spread → 0 **whether or not the chain was ever trapped**. Any chain eventually "passes" it. A PASS
  on spread at large N is close to uninformative.
- **The SEPARATION criterion gets HARDER with N, and is therefore the meaningful one.** As N grows the
  standard error shrinks, so z grows *only if the rank means genuinely differ*. If they agree and the
  chain is merely unconverged, z stays bounded. That is the behaviour you want from a basin test.

**Consequence for reading this verdict, stated carefully and without moving it.** The criterion that
**missed** (spread, 7.45 vs 5.0) is the mechanically-biased one; the criterion that **passed**
(separation, 55.2 vs 100) is the well-behaved one. That makes the underlying situation somewhat
better than the bare AMBIGUOUS label suggests — but **the verdict is not being revised**, because
revising a pre-registered grade on a post-hoc analysis of its own criteria is precisely the move
pre-registration exists to prevent. AMBIGUOUS stands.

**And it means a future re-grade must NOT be run on the same bands.** A later PASS would be
substantially manufactured by the spread criterion's drift. If this is re-graded, the spread band
must be replaced by something that does not shrink by construction — the obvious candidate being a
between-rank comparison of the posterior MEANS rather than of best-so-far minima, which is what the
separation criterion already does. **No re-grade is scheduled here; that is an owner decision, and
the design of its criterion is part of it.**

**A PASS does not license quoting the evidence comparison.** It licenses exactly one statement: that
the three ranks agree about where the posterior is. Convergence, Δln Z, and the H₀ figure remain
separately gated, and the letter's standing claim — the comparison is a wash — survives either
verdict.

### A counter-reading trap, recorded because it nearly caught me twice

The run's `.progress` file carries a column named `acceptance_rate` reporting **≈0.97**, which
invites the opposite diagnosis. It is a different quantity — stored rows ÷ Σ weights — and under
fast-parameter oversampling every accepted sub-step becomes its own row, so the weights sit near 1
and the ratio is pinned near unity *whatever the proposal is doing*. Verified on the live reference
chain: 2154 rows / 2221 total weight = **0.970**, against 745 accepted / 8018 steps = **9.3 %**.
Only the second is the per-proposal acceptance. Noted in the reader-facing risk page too, since a
reader checking the letter's 5.3–6.2 % would otherwise open the progress file and conclude it wrong.
