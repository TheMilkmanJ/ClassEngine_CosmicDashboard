# Production-chain parameter tables (GetDist)

> ForJustin/12 item 5(b)'s instrument. Stage B published **2026-08-10** under Grok red
> (`bbnfix_booking_20260808_005626/RED_AUDIT.md` — Claude offline; Grok carries red load).
> Means with 68% limits, 30% burn-in. **Booked bbnfix rows are three-rank GetDist.**

> ## BOOKED old-BAO pair + DESI Stage A + machine residuals — currency 2026-08-10 (Stage B)
>
> **Status:** old-BAO production `bbnfix` pair is **BOOKED Stage A + Stage B published** under dual gate.
> Authority: [`bbnfix_booking_20260808_005626/REPORT.md`](working_logs/_runs/bbnfix_booking_20260808_005626/REPORT.md)
> · red: [`RED_AUDIT.md`](working_logs/_runs/bbnfix_booking_20260808_005626/RED_AUDIT.md) (`red: AGREE`, auditor Grok).
>
> **Authority gate (bbnfix pair only):** both legs cobaya progress **R−1 < 0.05** *and* checkpoint
> **`converged: true`**. Booking script: `python3 scripts/book_bbnfix_when_ready.py`. Peeks remain **UNBOOKABLE**.
>
> **Booked old-BAO pair (`ignore_rows=0.3`; SH0ES-conditional; three-rank):**
>
> | chain | N | timestamp | R−1 | `converged` | H₀ | `m_ncdm` | S₈ |
> |---|---:|---|---:|---|---|---|---|
> | `dyad_mnu_bbnfix` | 37605 | 2026-08-07T04:08:52.190063 | **0.048118** | **true** | **70.052 ± 0.716** | **0.0671 ± 0.0583** | **0.821 ± 0.0097** |
> | `cmp_lcdm_mnu_bbnfix` | 26294 | 2026-08-05T11:52:10.194879 | **0.049324** | **true** | **68.345 ± 0.343** | **0.0192 ± 0.0174** | **0.824 ± 0.0081** |
>
> **Evidence honesty:** sample-cov Laplace **ΔlnZ ≈ +0.21** (cond(Σ)~10⁸) — inconclusive; not nested.
> FD Hessian v1 failed; v2 finite diagnostic only (ΔlnZ_H ≈ −1.18). Pre-bbnfix +2.635 is historical.
>
> **DESI-DR2 (separate instrument — do not mix):** Stage A **BOOKED** + Grok red for shelf citation
> ([`desidr2_bbnfix_booking_20260810_053127`](working_logs/_runs/desidr2_bbnfix_booking_20260810_053127/REPORT.md)
> · [`RED_AUDIT.md`](working_logs/_runs/desidr2_bbnfix_booking_20260810_053127/RED_AUDIT.md)).
> dyad H₀ **70.30±0.54** / lcdm **68.73±0.25**; sample-cov Laplace ΔlnZ≈**+1.38** (soft modes). Not nested.
> Full DESI param tables are **not** auto-merged into the old-BAO Stage B body below.
>
> | other lane | state |
> |---|---|
> | **routeD** | **BOOKED Stage A** — N=39332, R−1=**0.0542**, converged — authority [`routed_booking_20260810`](working_logs/_runs/routed_booking_20260810/REPORT.md) · peel [`routed_peel_20260810`](working_logs/_runs/routed_peel_20260810/REPORT.md). H₀ **69.63±0.57**, `dcdf_floor_thaw` **0.048±0.033**. Gate was R−1&lt;0.1 (not 0.05). **Not** bbnfix evidence. Instance stopped. |
> | Gold SH0ES PolyChord | **STALL CONFIRMED** then **clean re-resume** 2026-08-10 — dead frozen at 4595 ~11h; see [`gold_pc_stall_diag_20260810`](working_logs/_runs/gold_pc_stall_diag_20260810/REPORT.md). Intermediate log(Z) **not bookable**. TRGB not launched. |
>
> ### Forbidden claims
>
> - Treating archive tables below as current constraints
> - Mixing DESI-DR2 with old-BAO booked posteriors
> - Quoting MAP advantage as evidence
> - Inventing nested ΔlnZ
>
> ### Archive / dead chains (not live)
>
> | chain | last R−1 | live? |
> |---|---|---|
> | `cmp_prtoe_conv_desi` | **13.25** | **no** |
> | `cmp_prtoe_zon_disp` | **17.81** | **no** |
> | `cmp_prtoe_zon` | **40.36** | **no** |
> | `dyad_mnu_mcmc` | unknown | archive diagnostic |
>
> ## ⚠ Read this before any 68% numbers below
>
> **Archive chains below are not posteriors** (never dual-gate). Only the **BOOKED Stage B** bbnfix
> sections are licensed as dual-gate posterior summaries (still SH0ES-conditional; still not nested).
> Stage B body tables list up to 8 sampled params; banner H₀/`m_ncdm`/S₈ remain booking-REPORT authority.


> Generated 2026-08-10 by Grok Stage B (tables-only; three-rank where available).
> Archive rows remain **diagnostics only** (not dual-gate converged).

## cmp_prtoe_conv_desi — conversion channel vs DESI stack (1-rank, 3462 post-burn samples)

> **Archive / not dual-gate.** Do not quote as posterior constraints.

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

## cmp_prtoe_zon_disp — onset-identity dispersion run (1-rank, 3331 post-burn samples)

> **Archive / not dual-gate.** Do not quote as posterior constraints.

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

## dyad_mnu_mcmc — the scalar chain, Σm_ν free (1-rank, 3406 post-burn samples)

> **Archive / not dual-gate.** Do not quote as posterior constraints.

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

## cmp_prtoe_zon — onset-identity base run (1-rank, 818 post-burn samples)

> **Archive / not dual-gate.** Do not quote as posterior constraints.

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

## cmp_lcdm_mnu_bbnfix — ΛCDM+mν BBN-fixed control twin — BOOKED Stage B (3-rank, 18406 post-burn samples)

> **BOOKED dual-gate pair.** Three-rank GetDist, ignore_rows=0.3.
> Banner H₀ authority remains booking REPORT.

| parameter | mean | 68% limits |
|---|---|---|
| omega_b | 0.022499 | [0.022417, 0.022586] |
| H0 | 68.345 | [67.992, 68.684] |
| logA | 3.051 | [3.0375, 3.0645] |
| omega_cdm | 0.11867 | [0.11797, 0.11947] |
| n_s | 0.97114 | [0.96795, 0.97415] |
| z_reio | 8.028 | [7.3427, 8.7004] |
| A_planck | 1.0013 | [0.9994, 1.0031] |
| A_act | 1.0002 | [0.99822, 1.0022] |

## dyad_mnu_bbnfix — dyad BBN-fixed production twin — BOOKED Stage B (3-rank, 26324 post-burn samples)

> **BOOKED dual-gate pair.** Three-rank GetDist, ignore_rows=0.3.
> Banner H₀ authority remains booking REPORT.

| parameter | mean | 68% limits |
|---|---|---|
| omega_b | 0.022764 | [0.022635, 0.022885] |
| H0 | 70.052 | [69.352, 70.767] |
| logA | 3.0525 | [3.0377, 3.066] |
| n_s | 0.97124 | [0.96816, 0.97411] |
| z_reio | 7.9019 | [7.2, 8.6247] |
| dcdf_rho_inf | 0.70405 | [0.69862, 0.70971] |
| varying_me | 1.0128 | [1.0077, 1.0174] |
| A_planck | 1.001 | [0.99923, 1.0028] |

---

## Claims ledger & residual freeze (2026-08-10 Stage B)

| # | Claim | Grade | Evidence | Residual / blocker |
|---|---|---|---|---|
| 1 | Archive GetDist tables are diagnostics only | **honest fence** | banner ⚠ | never dual-gate |
| 2 | Old-BAO bbnfix dual-gate **Stage A booked + Stage B published** | **machine-backed + Grok red** | booking `20260808_005626` + `RED_AUDIT.md` (`red: AGREE`) + three-rank tables below | OPEN-NESTED evidence; soft-mode Laplace |
| 3 | Sample-cov Laplace old-BAO inconclusive | **machine-backed** | ΔlnZ ≈ +0.21; cond~10⁸ | not PolyChord |
| 4 | DESI-DR2 Stage A booked; peel + Grok red (separate) | **machine-backed + Grok red** | booking + `docs/chains/*_desidr2.*`; samplecov ΔlnZ≈+1.4; FD Hessian ΔlnZ_H≈−25 (diagnostic fail) | do not mix; not nested; do not quote Hessian ΔlnZ_H |
| 5 | Route-D thaw | **OPEN-BLOCKED** | R−1=0.351 | not dual-gate |
| 6 | Archive conv_desi / zon_disp | **OPEN-BLOCKED** | dead instruments | owner restart |
| 7 | Gold nested SH0ES PolyChord | **OPEN-MACHINE** | both legs running | no ΔlnZ yet |

**Non-claims:** no nested invent; no DESI/old-BAO mix; no COMPLETE from Laplace; Stage B ≠ nested win.

**Red note:** Claude offline 2026-08-10; Grok wrote `RED_AUDIT.md` stamps. Process law line `red: AGREE` satisfied for pipeline `--write-tables`.

**Rule:** `docs/working_logs/STORY_GRADE_ELEVATION_RULE.md`
