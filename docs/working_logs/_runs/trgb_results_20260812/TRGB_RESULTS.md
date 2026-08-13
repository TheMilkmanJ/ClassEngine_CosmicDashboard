# TRGB MCMC results (getdist, 30% burn-in drop)

**Host:** `i-0c65cc61a575bdfa7` (routed)  
**Analysis:** 2026-08-12 via `getdist.loadMCSamples(..., ignore_rows=0.3)`  
**JSON:** `/home/ubuntu/docs_runs/trgb_results_20260812/` on routed  

**Convergence note:** Main-parameter R−1 at stop was ~0.04–0.05 for both TRGB legs; R−1_cl still ~0.18–0.19 — treat as usable posteriors, not ultra-tight on derived-cl.

## TRGB twins (DESI DR2 + Planck + ACT + SPT + Pantheon+ **TRGB H0**)

| Parameter | **dyad** | **ΛCDM+mν** |
|-----------|----------|-------------|
| H0 | **68.90 ± 0.60** | **68.39 ± 0.26** |
| ωb | 0.02259 ± 0.00011 | 0.022480 ± 0.000085 |
| ωcdm | (via ρ∞) | 0.11845 ± 0.00061 |
| ns | 0.9726 ± 0.0031 | 0.9715 ± 0.0030 |
| log(10¹⁰ As) | 3.052 ± 0.013 | 3.053 ± 0.013 |
| Σmν (68% upper) | < 0.035 | < 0.024 |
| Ωm | 0.3001 ± 0.0039 | 0.3018 ± 0.0034 |
| σ8 | 0.8235 ± 0.0084 | 0.8199 ± 0.0060 |
| S8 | 0.8236 ± 0.0084 | 0.8224 ± 0.0075 |
| ρ∞ (dyad) | 0.6998 ± 0.0039 | — |
| me/me0 (dyad) | 1.0041 ± 0.0043 | — |
| ⟨χ²⟩ total | 2743.4 | 2742.0 |
| ⟨χ²⟩ TRGB H0 | 0.41 | 0.71 |
| n_rows (post burn) | 154398 (×32) | 27332 (×3) |

**ΔH0 (dyad − LCDM) ≈ +0.51 km/s/Mpc** under TRGB — mild, both still ~Planck-like.

## SH0ES twins (same multi-survey + Pantheon+SH0ES) — for contrast

| Parameter | **dyad** | **ΛCDM+mν** |
|-----------|----------|-------------|
| H0 | **70.30 ± 0.54** | **68.73 ± 0.25** |
| ρ∞ | 0.7062 ± 0.0036 | — |
| me/me0 | 1.0134 ± 0.0043 | — |
| ⟨χ²⟩ total | 2808.4 | 2818.0 |

Under SH0ES, dyad pulls H0 higher (~70.3) and has **~10 lower mean χ²** than LCDM.

## RouteD (finished earlier)

| Parameter | value |
|-----------|-------|
| H0 | 69.63^{+0.64}_{-0.43} |
| ρ∞ | 0.7145^{+0.0053}_{-0.012} |
| Σmν 68% | < 0.029 |
| ⟨χ²⟩ | 2809.7 |

## Takeaway

- **TRGB path:** both models land near **H0 ~ 68.4–68.9**; dyad is only slightly higher; χ² essentially tied.
- **SH0ES path:** dyad **raises H0** and improves fit vs LCDM (as expected from the H0 prior tension).

## Plots (local)

| File | Content |
|------|---------|
| `docs/plots/dyad_trgb_vs_shoes_H0_rho_me_triangle.png` | dyad TRGB vs SH0ES: H0–ρ∞–me |
| `docs/plots/dyad_trgb_vs_shoes_extended_triangle.png` | same + Ωm, S8, mν |
| `docs/plots/trgb_twins_dyad_vs_lcdm_triangle.png` | TRGB dyad vs LCDM shared params |
| `docs/plots/H0_1d_trgb_shoes_fourway.png` | H0 1D: all four twins |

## Chain tables

`docs/PRTOE_CHAIN_TABLES.md` — section **DESI-DR2 + TRGB production twins (booked 2026-08-12)**
