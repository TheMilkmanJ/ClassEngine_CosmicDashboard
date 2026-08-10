# Production-chain parameter tables (GetDist)

> ForJustin/12 item 5(b)'s instrument (`scripts/make_getdist_tables.py`).
> Regenerated per run at its landing; the live pair and Route-D join
> **at convergence only**. Means with 68% limits, 30% burn-in — and only then.

> ## BOOKED old-BAO pair + open machine residuals — currency 2026-08-10
>
> **Status:** the old-BAO production `bbnfix` pair is **BOOKED** under the dual gate. Authority:
> [`bbnfix_booking_20260808_005626/REPORT.md`](working_logs/_runs/bbnfix_booking_20260808_005626/REPORT.md).
> This is a Stage A receipt, not a substitute for any separate red-audited Stage B forward-table
> publication path.
>
> **Authority gate (bbnfix pair only):** both legs must show cobaya progress
> **R−1 < 0.05** *and* checkpoint **`converged: true`** (self-stop). Booking script only:
> `python3 scripts/book_bbnfix_when_ready.py`. Diagnostic peeks remain **UNBOOKABLE**.
>
> **Booked old-BAO pair (`ignore_rows=0.3`; SH0ES-conditional):**
>
> | chain | N | timestamp | R−1 | `converged` | H₀ | `m_ncdm` | S₈ |
> |---|---:|---|---:|---|---|---|---|
> | `dyad_mnu_bbnfix` | 37605 | 2026-08-07T04:08:52.190063 | **0.048118** | **true** | **70.052 ± 0.716** | **0.0671 ± 0.0583** | **0.821 ± 0.0097** |
> | `cmp_lcdm_mnu_bbnfix` | 26294 | 2026-08-05T11:52:10.194879 | **0.049324** | **true** | **68.345 ± 0.343** | **0.0192 ± 0.0174** | **0.824 ± 0.0081** |
>
> **Evidence honesty on the booked old-BAO pair:** the volume-aware sample-covariance Laplace on
> the exported `docs/chains/` bundle is **ΔlnZ ≈ +0.21**, not a headline win, with
> **cond(Σ) ~ 10⁸** on both legs; the better MAP by **Δ(min −logpost) ≈ −2.96** is *not* evidence.
> Authority: [`laplace_docs_chains_bbnfix_20260808/REPORT.md`](working_logs/_runs/laplace_docs_chains_bbnfix_20260808/REPORT.md)
> and [LAPLACE_bbnfix_full.md](chains/LAPLACE_bbnfix_full.md). FD Hessian Laplace: **v1 failed**
> (`logZ=-inf` — `credibility_diagnostics_20260808/HESSIAN_FD_20260810_REPORT.md`); **v2 finished
> finite** both legs (`hessian_laplace_v2.json`, ΔlnZ_H ≈ **−1.18**, samplecov cross-check ≈ **+0.22**,
> huge cond / regularized). **Diagnostic only — not nested, not gold evidence.** Sample-cov +0.21
> remains the soft-mode-honest volume-aware label on this pair.
>
> **Separate open machine residuals (do not mix with the booked old-BAO pair):**
>
> | lane | state | authority |
> |---|---|---|
> | `cmp_prtoe_routeD` (thaw / no-bare) | **OPEN-MACHINE** — R−1 **0.351167**@N=14625 t=2026-08-06T09:24:48; `converged:false`; ~**3.51×** its 0.1 stop | [`blocked_lane_routeD_20260805`](working_logs/_runs/blocked_lane_routeD_20260805/REPORT.md) |
> | DESI-DR2 bbnfix twins | **BOOKED (Stage A)** — dual-gate met: dyad R−1 **0.03321** @ N=53482 `converged:true`; lcdm R−1 **0.041377** @ N=52031 `converged:true`. GetDist (30% burn, SH0ES-conditional DESI stack): dyad **H₀ = 70.30 ± 0.54**, lcdm **H₀ = 68.73 ± 0.25**. Authority: [`desidr2_bbnfix_booking_20260810_053127`](working_logs/_runs/desidr2_bbnfix_booking_20260810_053127/REPORT.md). **Do not mix with old-BAO BOOKED pair.** | AWS `i-096d08d2dc9d8f42c` |
> | Gold nested evidence | **RUNNING (both SH0ES legs)** — resume after Fortran `read_write.F90` “Still Active” fix; intermediate log(Z) **not bookable**. TRGB not launched (quota: PC pair holds 192 of 300). | [`gold_desidr2_polychord_launch_20260810/`](working_logs/_runs/gold_desidr2_polychord_launch_20260810/) |
>
> **Do not mix instruments.** The booked old-BAO GetDist posteriors above are one stack. The
> DESI-DR2 MCMCs are a separate live stack. The gold PolyChord program is the intended nested
> referee for DESI-DR2 and has **no** result until both legs of a ladder pair finish.
>
> ### Forbidden claims
>
> - Treating historical archive tables below as current constraints
> - Replacing the booked old-BAO pair with the live DESI-DR2 pair
> - Quoting the booked pair’s better MAP as a win on evidence
> - Inventing a nested verdict from the gold DESI-DR2 design files
> - Treating GetDist GR or crude param R−1 as booking authority
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
> **None of the archive chains in the GetDist tables below has converged, and the 68% limits are therefore
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

## Claims ledger & residual freeze (2026-08-10 currency)

| # | Claim | Grade | Evidence | Residual / blocker |
|---|---|---|---|---|
| 1 | Archive GetDist tables are diagnostics only (not posteriors) | **honest fence** | banner ⚠ section | R−1 never hit stop on those runs |
| 2 | Old-BAO production bbnfix pair booked under the dual gate | **machine-backed** | booking receipt `bbnfix_booking_20260808_005626`; three-rank GetDist H₀ / `m_ncdm` / S₈ values above | **OPEN-EVIDENCE:** sample-cov Laplace only; Stage B forward-table publication still needs red audit |
| 3 | Sample-cov Laplace on booked old-BAO pair is inconclusive | **machine-backed** | ΔlnZ_Laplace **+0.211493**; cond(Σ) ~10⁸ both legs | **OPEN-NESTED:** not PolyChord; soft-mode sensitive; FD Hessian v2 finite but diagnostic only |
| 4 | DESI-DR2 bbnfix pair Stage A booked (separate instrument) | **machine-backed** | `desidr2_bbnfix_booking_20260810_053127`: dyad R−1 **0.03321** / lcdm **0.041377**, both `converged:true`; GetDist H₀ **70.30±0.54** / **68.73±0.25**; sample-cov Laplace **ΔlnZ ≈ +1.38** (soft modes) | **Do not mix** with old-BAO; not nested; Stage B red still open; DESI FD Hessian in flight |
| 5 | Route-D thaw posterior | **OPEN-BLOCKED** | R−1=**0.351167**@N=14625 t=2026-08-06T09:24:48; ~**3.51×** stop 0.1 | **OPEN-MACHINE:** not dual-gate |
| 6 | conv_desi / zon_disp archive rows | **OPEN-BLOCKED** | dead instruments | Owner restart; not live |
| 7 | Gold nested DESI-DR2 SH0ES PolyChord | **OPEN-MACHINE** | both 96-vCPU legs running (resume); intermediate log(Z) not bookable | No ΔlnZ until both legs finish cleanly; TRGB not launched |

**Non-claims / forbidden:** no invented nested ΔlnZ; no mixing DESI-DR2 with old-BAO booked posteriors; no COMPLETE physics from Laplace alone; Stage A booking ≠ Stage B red-published tables.

**Triage:** two Stage A GetDist receipts (old-BAO + DESI-DR2) are machine-backed; nested and Stage B red remain open.

**Rule:** `docs/working_logs/STORY_GRADE_ELEVATION_RULE.md`
