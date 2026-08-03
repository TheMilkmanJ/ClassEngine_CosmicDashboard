# Production-chain parameter tables (GetDist)

> ForJustin/12 item 5(b)'s instrument (`scripts/make_getdist_tables.py`).
> Regenerated per run at its landing; the live pair and Route-D join
> **at convergence only**. Means with 68% limits, 30% burn-in — and only then.

> ## Live production status (re-read 2026-08-02 ~22:20 from `.progress`, launchlog tails, checkpoints)
>
> Three MPI production objects are **live** (do not kill). None has met its R−1 stop.
> Cobaya `.progress` `acceptance_rate` is **oversampled** (`oversample_power = 0.4`) and
> sits near ~0.99 even when the raw Metropolis accept rate is healthy; **use launchlog
> accepted/steps** for the real accept rate.
>
> **R−1 unchanged** since the last progress checkpoints (dyad 15:41 / lcdm 19:00 / routeD 19:24);
> launchlogs and `*.{1,2,3}.txt` still advancing.
>
> | chain | ranks (`mpi_size`) | N (progress) | R−1 last | stop | raw accept (launchlog Σ) | progress accept | live? |
> |---|---:|---:|---:|---:|---:|---:|---|
> | `dyad_mnu_bbnfix` (model, BBN-fixed) | **3** | 14544 | **0.192** | 0.05 | **~6.40%** (Σ 15132/236443; ≈5044/78814 per rank) | 0.996 ⚠ oversampled | **YES** — progress 2026-08-02T15:41; launchlog ~22:18 |
> | `cmp_lcdm_mnu_bbnfix` (ΛCDM+mν twin) | **3** | 13193 | **0.141** | 0.05 | **~8.59%** (Σ 13599/158247; ≈4533/52749 per rank) | 0.984 ⚠ oversampled | **YES** — progress 2026-08-02T19:00; launchlog ~22:18 |
> | `cmp_prtoe_routeD` (thaw / no-bare) | **3** | 1593 | **129.1** | 0.1 | **~5.15%** (Σ 1828/35479; ≈609/11826 per rank) | 1.0 ⚠ oversampled | **YES** — first progress row 2026-08-02T19:24; early; ranks partially disjoint (H₀ post-50% means ≈68.55 / 68.66 / 69.83) |
>
> **Stop targets (from yaml):** dyad / lcdm `Rminus1_stop = 0.05`; routeD `Rminus1_stop = 0.1`.
> Checkpoints all report `converged: false`. Closest to gate: lcdm twin at ~2.8× stop; model at
> ~3.8×; routeD is early and far (≈1290× its looser 0.1 stop).
>
> **No GetDist posterior table exists yet for the three live runs** — they join this file only
> when R−1 hits stop. Booking commands: `docs/working_logs/_POSTERIOR_BOOKING_CHECKLIST.md`.
> Any preliminary peek must be labeled as such and is not booked.
>
> ### Archive / dead chains still tabulated below (not live)
>
> | chain | last R−1 | over 0.05 | live? |
> |---|---|---|---|
> | `cmp_prtoe_conv_desi` | **13.25** | 265× | **no** — unproduced; last write 2026-07-22 |
> | `cmp_prtoe_zon_disp` | **17.81** | 356× | **no** — collapsed; seed ready, owner restart |
> | `cmp_prtoe_zon` | **40.36** | 807× | **no** — stopped since 07-12 |
> | `dyad_mnu_mcmc` | none recorded | unknown | diagnostic archive only |
>
> ## ⚠ Read this before any 68% numbers below
>
> **None of the chains in the GetDist tables has converged, and the 68% limits are therefore
> not posterior intervals.** The numbers look like posterior summaries because they are
> formatted as posterior summaries — they are run diagnostics only.
>
> **The direction of the error is known and it is the dangerous one.** §6g withdrew the α_c band
> for exactly this defect, in its own words: *"an interval read at R−1 = 93 is the spread of a
> chain that has not found the distribution, which is typically far too narrow rather than too
> wide."* So these intervals should be read as **lower bounds on the true width**, not as
> measurements — a chain still wandering has not visited the tails it would need to visit to
> earn a 68% limit that tight.
>
> A concrete demonstration, from `cmp_prtoe_zon_disp` (2026-07-28): its segment means scatter
> **59× wider** than a settled chain of that length and variance would allow, and its cumulative
> mean was passing through the model's own target value at the moment the run stopped —
> a coincidence that would have read as a 0.0006 hit. See `PRTOE_quartet_clock.md` §4b.
>
> **Nothing in these tables may be quoted as a constraint** until the chain supplying it reports
> R−1 at target.

## cmp_prtoe_conv_desi — conversion channel vs DESI stack (3462 post-burn samples)

| parameter | mean | 68% limits |
|---|---|---|
| omega_b | 0.022803 | [0.022745, 0.022857] |
| H0 | 68.325 | [68.044, 68.589] |
| logA | 3.0483 | [3.0449, 3.0516] |
| n_s | 0.97042 | [0.9688, 0.97213] |
| z_reio | 7.8968 | [7.6656, 8.1093] |
| dcdf_rho_inf | 0.75272 | [0.75179, 0.75352] |
| dcdf_conv_g | 0.52457 | [0.5013, 0.55001] |
| A_planck | 0.9989 | [0.99792, 1.0003] |

## cmp_prtoe_zon_disp — onset-identity dispersion run (3331 post-burn samples)

| parameter | mean | 68% limits |
|---|---|---|
| omega_b | 0.022776 | [0.022717, 0.022827] |
| H0 | 70.9 | [70.81, 70.998] |
| logA | 3.0453 | [3.04, 3.052] |
| n_s | 0.97465 | [0.97139, 0.97747] |
| z_reio | 7.7559 | [7.5091, 8.0463] |
| log10_zon | 7.5948 | [7.5689, 7.6425] |
| dcdf_rho_inf | 0.71471 | [0.7136, 0.71567] |
| A_planck | 1.0003 | [0.99941, 1.0014] |

## dyad_mnu_mcmc — the scalar chain, Σm_ν free (3406 post-burn samples)

| parameter | mean | 68% limits |
|---|---|---|
| omega_b | 0.022755 | [0.022582, 0.022818] |
| H0 | 69.72 | [68.962, 70.137] |
| logA | 3.0725 | [3.0668, 3.0812] |
| n_s | 0.97046 | [0.96561, 0.97322] |
| z_reio | 8.92 | [8.6467, 9.4146] |
| dcdf_rho_inf | 0.70094 | [0.69739, 0.70415] |
| varying_me | 1.0125 | [1.005, 1.0121] |
| A_planck | 1.001 | [0.99919, 1.0024] |

## cmp_prtoe_zon — onset-identity base run (818 post-burn samples)

| parameter | mean | 68% limits |
|---|---|---|
| omega_b | 0.0228 | [0.022769, 0.022832] |
| H0 | 69.983 | [69.833, 70.071] |
| logA | 3.0407 | [3.0336, 3.0421] |
| n_s | 0.96648 | [0.96348, 0.96765] |
| z_reio | 7.056 | [6.7602, 7.4833] |
| log10_zon | 7.8658 | [7.807, 7.9583] |
| dcdf_rho_inf | 0.7025 | [0.70128, 0.70358] |
| A_planck | 1.0018 | [0.99909, 1.0053] |

