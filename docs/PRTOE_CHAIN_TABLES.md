# Production-chain parameter tables (GetDist)

> ForJustin/12 item 5(b)'s instrument (`scripts/make_getdist_tables.py`).
> Regenerated per run at its landing; the running pair and Route-D join
> at convergence. Means with 68% limits, 30% burn-in.

> **Status.** Stage A posteriors are **booked** for old-BAO SH0ES, DESI-DR2 SH0ES, and DESI-DR2 TRGB (do not mix anchors). Nested sampling (UltraNest + PolyChord) is **running** on all three anchors; mid-run log-evidence is **not bookable**. The α_c instrument (`cmp_prtoe_zon_disp_retune`) **stopped** (R−1=0.036, `converged: true`); GetDist **done**; `log10_zon` **inconclusive** (7.57±0.51, all three lineup rungs inside 68%). The conversion instrument (`cmp_prtoe_conv_desi_retune`) **stopped** (R−1=0.0447, `converged: true`); GetDist **done**; `dcdf_conv_g` **inconclusive** (0.080±0.072). Authority: `docs/working_logs/_runs/zon_disp_retune_grade_20260821/REPORT.md` · `docs/working_logs/_runs/conv_desi_retune_grade_20260824/REPORT.md`. Bookable cosmology tables start at the DESI-DR2 production twins below.

---

## ⚠ NON-BOOKABLE ARCHIVE TABLES (do not cite as Stage A)

> The next four GetDist blocks (`conv_desi`, `zon_disp`, `dyad_mnu_mcmc`, `cmp_prtoe_zon`) are
> **historical / exploratory instrument peels**. They are **not** dual-gate booked Stage A posteriors.
> - `conv_desi`: **Jul-22 archive only** (R−1≈13.25). The 2026-08-21 retune **stopped**; GetDist is the next section (`conv_desi_retune_grade_20260824`). Not Stage A. Not a KiDS shear fit.
> - `zon_disp` / `cmp_prtoe_zon`: **archive peels**. Retune GetDist is the next section; clock still **inconclusive**.
> - `dyad_mnu_mcmc`: exploratory peel — **not** the booked bbnfix twins.
>
> **Bookable authority starts at “DESI-DR2 + SH0ES production twins” below.**

## cmp_prtoe_conv_desi — conversion channel vs DESI stack (3462 post-burn samples) **[ARCHIVE — NOT BOOKABLE]**

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

## cmp_prtoe_zon_disp — onset-identity dispersion run (3331 post-burn samples) **[ARCHIVE — NOT BOOKABLE]**

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

## dyad_mnu_mcmc — the scalar chain, Σm_ν free (3406 post-burn samples) **[ARCHIVE — NOT BOOKABLE]**

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

## cmp_prtoe_zon — onset-identity base run (818 post-burn samples) **[ARCHIVE — NOT BOOKABLE]**

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

## cmp_prtoe_zon_disp_retune — stopped α_c instrument (949753 post-burn; 2026-08-21)

> Dual-gate met: R−1=0.03618 < 0.05, R−1 CL=0.189 < 0.2, checkpoint `converged: true`, 48 ranks.
> GetDist `ignore_rows=0.3`. **Clock verdict: INCONCLUSIVE.** `log10_zon = 7.571 ± 0.511`, 68% [7.19, 8.26] contains **7.55, 7.70, and 7.85**. Do not cite as α_c=3α confirmation or as a pair-call hit/kill. Package: `zon_disp_retune_grade_20260821`. **Not** a Stage A H₀ twin.

| parameter | mean | 68% limits |
|---|---|---|
| omega_b | 0.022757 | [0.022669, 0.022846] |
| H0 | 69.894 | [69.363, 70.596] |
| logA | 3.0505 | [3.0363, 3.0636] |
| n_s | 0.97087 | [0.96774, 0.97403] |
| z_reio | 7.783 | [7.063, 8.500] |
| log10_zon | 7.571 | [7.190, 8.260] |
| dcdf_rho_inf | 0.70225 | [0.69597, 0.71050] |
| A_planck | 1.00099 | [0.99912, 1.00286] |

---

## cmp_prtoe_conv_desi_retune — stopped conversion instrument (1153002 post-burn; 2026-08-24)

> Dual-gate met: R−1=0.04469 < 0.05, R−1 CL=0.185 < 0.2, checkpoint `converged: true`, 192 ranks.
> GetDist `ignore_rows=0.3`. **`g` verdict: INCONCLUSIVE.** `dcdf_conv_g = 0.080 ± 0.072`, 68% [0.015, 0.146]; 44% of samples g<0.05. Registered 0.10 sits inside 68%; the lever is **not** demanded. Derived S₈ = **0.816 ± 0.009** (68% [0.807, 0.826]) matches the KiDS-Legacy *number* 0.814±0.012 — **not** a shear likelihood. Package: `conv_desi_retune_grade_20260824`. **Not** a Stage A H₀ twin. **Not** a published S₈-tension win.

| parameter | mean | 68% limits |
|---|---|---|
| omega_b | 0.022780 | [0.022700, 0.022860] |
| H0 | 70.211 | [69.791, 70.635] |
| logA | 3.0552 | [3.0417, 3.0687] |
| n_s | 0.97226 | [0.96925, 0.97526] |
| z_reio | 8.042 | [7.355, 8.734] |
| dcdf_rho_inf | 0.7172 | [0.7094, 0.7250] |
| dcdf_conv_g | 0.0799 | [0.0153, 0.1463] |
| A_planck | 1.00117 | [0.99931, 1.00303] |
| m_ncdm | 0.0325 | [0.0071, 0.0585] |
| sigma8 | 0.8441 | [0.8327, 0.8554] |
| Omega_m | 0.2808 | [0.2716, 0.2898] |
| S8 | 0.8164 | [0.8071, 0.8256] |

---

## DESI-DR2 + SH0ES production twins (dual-gate booked 2026-08-11)

> Authority: `docs/working_logs/_runs/bbnfix_booking_desidr2_sh0es_20260811_094254/` +
> non-nested package `desidr2_sh0es_non_nested_20260811_124834/`.
> GetDist three-rank, `ignore_rows=0.3`. **Not** nested evidence.

## dyad_mnu_bbnfix_desidr2 — dyad DESI-DR2 + SH0ES bbnfix (38474 post-burn samples)

| parameter | mean | 68% limits |
|---|---|---|
| omega_b | 0.0227757 | [0.0226527, 0.0228792] |
| H0 | 70.302 | [69.7354, 70.8098] |
| logA | 3.0522 | [3.03888, 3.06557] |
| n_s | 0.971505 | [0.968754, 0.974566] |
| z_reio | 7.87368 | [7.15899, 8.60446] |
| dcdf_rho_inf | 0.706236 | [0.702732, 0.709746] |
| varying_me | 1.01342 | [1.00871, 1.01729] |
| A_planck | 1.00106 | [0.999258, 1.00276] |
| A_act | 0.999912 | [0.997947, 1.00187] |
| P_act | 1.00386 | [1.00132, 1.00642] |

Triangle: `docs/plots/dyad_mnu_bbnfix_desidr2_triangle.png`

## cmp_lcdm_mnu_bbnfix_desidr2 — LCDM+mν DESI-DR2 + SH0ES bbnfix control (36422 post-burn samples)

| parameter | mean | 68% limits |
|---|---|---|
| omega_b | 0.0225215 | [0.0224377, 0.0226068] |
| H0 | 68.729 | [68.4798, 68.9778] |
| logA | 3.05598 | [3.0428, 3.06829] |
| omega_cdm | 0.117815 | [0.117232, 0.118404] |
| n_s | 0.973014 | [0.970232, 0.975725] |
| z_reio | 8.3603 | [7.74668, 8.99356] |
| A_planck | 1.00126 | [0.999388, 1.00316] |
| A_act | 1.00019 | [0.998175, 1.00218] |
| P_act | 1.00302 | [1.00047, 1.00559] |
| Tcal | 0.998563 | [0.995877, 1.00124] |

Triangle: `docs/plots/cmp_lcdm_mnu_bbnfix_desidr2_triangle.png`

## DESI-DR2 + SH0ES twin comparison (bookable posteriors)

| quantity | dyad | LCDM twin |
|---|---:|---:|
| H0 | 70.302 ± 0.5412 | 68.729 ± 0.2497 |
| omega_b | 0.022776 ± 0.000115 | 0.022522 ± 8.505e-05 |

| ΔH₀ (dyad−lcdm) | **1.573** km/s/Mpc | |
| Δ(min −logpost) proxy | **-3.9476** (favors dyad if negative) | |
| ΔlnZ_Laplace (interim) | **1.305** — **not nested** | |

**Nested ΔlnZ (currency 2026-08-15):** Nested UN+PC **all anchors RUNNING** (SH0ES, TRGB, no-H0).
SH0ES EV — UltraNest ×96 both legs **RUNNING**; PolyChord GIL dyad ×96 **RUNNING**; PC lcdm ×96
**RESCUED** after `read_write.F90` “Still Active” format abort (patch+rebuild on `i-0941e936fd100c309`).
No-local-H0 UltraNest **both** legs RUNNING; TRGB UltraNest **both** legs RUNNING;
TRGB PolyChord GIL **both** legs RUNNING ×96 (`i-06847ebdfd55bac11` / `i-0d1915a2ac2d5c5af`,
launch `docs/working_logs/_runs/trgb_pc_launch_20260813/`).
**Not bookable** until final summaries; mid-run logZ forbidden. ETA stamps:
`docs/working_logs/_runs/nested_pc_eta_20260815/`. Booking template (empty):
`docs/working_logs/_runs/nested_booking_template_20260813/`. Fleet:
`docs/working_logs/_runs/hygiene_batch_20260813/FLEET_HEALTH.md`. Runbook:
`docs/working_logs/_runs/dual_nested_runbook_20260812/`.

---

## DESI-DR2 + TRGB production twins (booked 2026-08-12)

> Authority: getdist on routed `i-0c65cc61a575bdfa7`, `ignore_rows=0.3`.  
> JSON: `docs/working_logs/_runs/trgb_results_20260812/all_summary.json`  
> Plots: `docs/plots/dyad_trgb_vs_shoes_*`, `docs/plots/trgb_twins_*`, `docs/plots/H0_1d_trgb_shoes_fourway.png`  
> **Not** nested evidence. Main R−1 ~0.04–0.05 at stop; R−1_cl still ~0.18–0.19.

## dyad_mnu_bbnfix_desidr2_trgb — dyad DESI-DR2 + TRGB H0 (154398 post-burn samples, ×32)

| parameter | mean | 68% limits |
|---|---|---|
| omega_b | 0.0225875 | [0.0224752, 0.0226993] |
| H0 | 68.8962 | [68.2946, 69.5103] |
| logA | 3.05248 | [3.03934, 3.06564] |
| n_s | 0.97256 | [0.96954, 0.975576] |
| z_reio | 8.03341 | [7.35645, 8.71519] |
| dcdf_rho_inf | 0.699791 | [0.69595, 0.703741] |
| varying_me | 1.00406 | [0.999761, 1.00828] |
| m_ncdm | 0.0307511 | [0.00576313, 0.0551318] |
| Omega_m | 0.300132 | [0.296183, 0.303972] |
| sigma8 | 0.823488 | [0.81535, 0.831748] |
| S8 | 0.823635 | [0.815446, 0.831782] |

Triangles: `docs/plots/dyad_trgb_vs_shoes_H0_rho_me_triangle.png`, `docs/plots/dyad_trgb_vs_shoes_extended_triangle.png`

## cmp_lcdm_mnu_bbnfix_desidr2_trgb — LCDM+mν DESI-DR2 + TRGB H0 control (27332 post-burn samples, ×3)

| parameter | mean | 68% limits |
|---|---|---|
| omega_b | 0.0224798 | [0.0223937, 0.0225658] |
| H0 | 68.3868 | [68.1222, 68.6468] |
| logA | 3.05288 | [3.04009, 3.06596] |
| omega_cdm | 0.118454 | [0.117851, 0.11909] |
| n_s | 0.971491 | [0.968581, 0.974515] |
| z_reio | 8.15602 | [7.51655, 8.82071] |
| m_ncdm | 0.0200919 | [0.00421837, 0.0366849] |
| Omega_m | 0.301832 | [0.298465, 0.305412] |
| sigma8 | 0.819944 | [0.81427, 0.825921] |
| S8 | 0.82243 | [0.81466, 0.829932] |

Triangle: `docs/plots/trgb_twins_dyad_vs_lcdm_triangle.png`

## DESI-DR2 + TRGB twin comparison (bookable posteriors)

| quantity | dyad TRGB | LCDM TRGB |
|---|---:|---:|
| H0 | 68.896 ± 0.598 | 68.387 ± 0.262 |
| omega_b | 0.022588 ± 0.000113 | 0.022480 ± 8.53e-05 |
| dcdf_rho_inf | 0.6998 ± 0.0039 | — |
| varying_me | 1.0041 ± 0.0043 | — |
| ⟨χ²⟩ total | 2743.4 | 2742.0 |

| ΔH₀ (dyad−lcdm) TRGB | **+0.51** km/s/Mpc | |
| ΔH₀ (dyad SH0ES − dyad TRGB) | **+1.41** km/s/Mpc | |
| ΔH₀ (dyad SH0ES − lcdm SH0ES) | **+1.57** km/s/Mpc | |

**Ladder note:** under TRGB both models sit ~68.4–68.9; under SH0ES dyad alone climbs to ~70.3.

Four-way H0: `docs/plots/H0_1d_trgb_shoes_fourway.png`  
Write-up: `docs/working_logs/_runs/trgb_results_20260812/TRGB_RESULTS.md`

