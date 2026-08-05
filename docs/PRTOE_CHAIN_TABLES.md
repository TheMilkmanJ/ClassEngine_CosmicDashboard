# Production-chain parameter tables (GetDist)

> ForJustin/12 item 5(b)'s instrument (`scripts/make_getdist_tables.py`).
> Regenerated per run at its landing; the live pair and Route-D join
> **at convergence only**. Means with 68% limits, 30% burn-in — and only then.

> ## OPEN-MACHINE residual freeze — 2026-08-05
>
> **Status:** OPEN-MACHINE (ledger for production posteriors). **Bookable: NO.**
>
> **Authority gate (bbnfix pair only):** both legs must show cobaya progress
> **R−1 < 0.05** *and* checkpoint **`converged: true`** (self-stop). Booking script only:
> `python3 scripts/book_bbnfix_when_ready.py`. Diagnostic peeks
> (`scripts/bbnfix_mcmc_watch_diag.py`) are **UNBOOKABLE** even when GetDist GR looks low.
>
> ### Live production status (stamp 2026-08-05; progress / checkpoints)
>
> Three MPI production objects are **live**. The lcdm control leg has self-stopped; the pair is
> still **NOT bookable** because dyad has not.
> Cobaya `.progress` `acceptance_rate` is **oversampled** (`oversample_power = 0.4`) and
> sits near ~0.98–1.0 even when the raw Metropolis accept rate is healthy; **use launchlog
> accepted/steps** for the real accept rate when launchlog is current.
>
> Progress/checkpoint files **lag** chain `.txt` growth by hours until cobaya’s next R−1
> write — normal; **not** a license to book.
>
> Authority reconfirm (read-only): `python3 scripts/book_bbnfix_when_ready.py` → **REFUSED**.
> Quote: **lcdm R−1 0.049324** (N=26294, t=2026-08-05T11:52:10) with checkpoint
> `converged: true` — control leg ready, but **NOT bookable** by itself; **dyad R−1 0.060201**
> (N=26135, t=2026-08-05T15:50:02 — **1.20×** stop; `converged: false`). routeD R−1
> **0.728432**@N=8120 t=2026-08-05T12:54:11 (~**7.28×** its 0.1 stop) — **not** dual-gate. GetDist offline GR
> **~0.07 / ~0.086** (lcdm / dyad; prior diag) is **diagnostic only**.
> Currency: booking refuse card
> [`blocked_lane_bbnfix_20260805/REPORT.md`](working_logs/_runs/blocked_lane_bbnfix_20260805/REPORT.md).
>
> | chain | ranks | N (progress) | R−1 last | stop | `converged` | progress accept | live? |
> |---|---:|---:|---:|---:|---|---:|---|
> | `dyad_mnu_bbnfix` (model, BBN-fixed) | **3** | 26135 | **0.060201** | 0.05 | **false** | 0.996 ⚠ oversampled | **YES** — t=2026-08-05T15:50:02 (**1.20×** stop) |
> | `cmp_lcdm_mnu_bbnfix` (ΛCDM+mν twin) | **3** | 26294 | **0.049324** | 0.05 | **true** | 0.981 ⚠ oversampled | **YES** — t=2026-08-05T11:52:10 (control leg ready; pair still closed) |
> | `cmp_prtoe_routeD` (thaw / no-bare) | **3** | 8120 | **0.728432** | 0.1 | **false** | 0.997 ⚠ oversampled | **YES** — t=2026-08-05T12:54:11 (~**7.28×** stop) |
>
> **Diagnostics only** (`bbnfix_mcmc_watch_diag.py`, prior 2026-08-04T02:40 — **not bookable**):
>
> | measure | dyad | lcdm twin |
> |---|---:|---:|
> | crude max-param R−1 (burn 50%) | 0.0344 | 0.0203 |
> | GetDist max GR (`ignore_rows=0.3`) | 0.0857 | 0.0721 |
>
> Crude param R−1 is optimistically low; GetDist GR is a better offline proxy.
> Neither measure replaces cobaya self-stop.
>
> Quote R−1 with N and timestamp. Temporary R−1 < 0.05 without `converged: true` is
> **not** bookable, and one ready leg does **not** open the pair.
>
> **Stop targets (from yaml):** dyad / lcdm `Rminus1_stop = 0.05`; routeD `Rminus1_stop = 0.1`.
> Distances: lcdm twin **through** the stop and self-stopped; model **~1.20×**;
> routeD ~**7.28×** its 0.1 stop.
>
> **No GetDist posterior table exists for the three live runs** — they join this file only
> after booking. Checklist: `docs/working_logs/_POSTERIOR_BOOKING_CHECKLIST.md`.
>
> ### What unblocks booking
>
> 1. Both bbnfix legs self-stop (`converged: true`) with R−1 < 0.05.
> 2. Run `python3 scripts/book_bbnfix_when_ready.py` (not the watch diagnostic).
> 3. Route-D / zon_disp / conv_desi are separate instruments — not part of the bbnfix pair gate.
>
> ### Forbidden claims (until gate)
>
> - Booked H₀ / Σm_ν / Ω_b h² / S₈ posteriors from live chains
> - Fake or interim GetDist H₀ tables inserted into this file
> - Quoting the archive tables below as constraints
> - Treating GetDist GR or crude param R−1 as the booking authority
>
> ### Archive / dead chains still tabulated below (not live)
>
> | chain | last R−1 | over 0.05 | live? |
> |---|---|---|---|
> | `cmp_prtoe_conv_desi` | **13.25** | 265× | **no** — unproduced; last chain write 2026-07-22; owner restart |
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
> R−1 at target **and** (for the bbnfix pair) `converged: true` via the booking script.

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


---

## Claims ledger & residual freeze (2026-08-05)

| # | Claim | Grade | Evidence | Residual / blocker |
|---|---|---|---|---|
| 1 | Archive GetDist tables are diagnostics only (not posteriors) | **honest fence** | banner ⚠ section | R−1 never hit stop on those runs |
| 2 | Live bbnfix pair bookable H₀ / Σm_ν tables | **OPEN-BLOCKED** | progress: dyad R−1=**0.060201**@N=26135 t=2026-08-05T15:50:02 (**1.20×**; `converged:false`); lcdm R−1=**0.049324**@N=26294 t=2026-08-05T11:52:10 (`converged:true`; control leg ready) | **OPEN-MACHINE:** wait dyad self-stop + `book_bbnfix_when_ready.py` |
| 3 | Route-D thaw posterior | **OPEN-BLOCKED** | R−1=**0.728432**@N=8120 t=2026-08-05T12:54:11; ~**7.28×** stop 0.1 | **OPEN-MACHINE:** live, not bookable; not dual-gate |
| 4 | conv_desi / zon_disp archive rows | **OPEN-BLOCKED** | dead instruments | Owner restart; not live |

**Non-claims / forbidden:** no bookable posterior from this file; no invented H₀ table; no COMPLETE physics from tables alone.

**Triage:** stay shelf as OPEN-MACHINE ledger. Physics ceiling: process record until booking gate fires.

**Rule:** `docs/working_logs/STORY_GRADE_ELEVATION_RULE.md`
