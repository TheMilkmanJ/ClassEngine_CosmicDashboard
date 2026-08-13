# TRGB DESI-DR2 dual-gate booking — 20260812

**Generated (UTC):** 2026-08-12T23:45:11.137539+00:00
**Analyst:** Grok (getdist on routed `i-0c65cc61a575bdfa7`)
**Gate (Stage A style):** both legs R−1 **< 0.05** on last progress line **and** MCMC processes stopped (self-stop / idle)
**Result:** **BOOKED Stage A (posteriors)** — **not** nested evidence
**Ignore rows:** 0.3 burn-in for GetDist

## Progress + stop gate

| chain | ranks | N (last) | timestamp (UTC) | R−1 | R−1_cl | process | ready |
|---|---:|---:|---|---:|---:|---|---|
| `dyad_mnu_bbnfix_desidr2_trgb` | 32 | 220574 | 2026-08-12T06:33:50 | **0.04535** | 0.192 | stopped | YES (R−1) |
| `cmp_lcdm_mnu_bbnfix_desidr2_trgb` | 3 | 39046 | 2026-08-10T23:15:46 | **0.04015** | 0.184 | stopped | YES (R−1) |

### Gate notes

- Main-parameter R−1 gate **passed** both legs.
- R−1_cl still ~0.18–0.19 — **usable** bookable posteriors; not ultra-tight on derived-cl.
- Do **not** mix with SH0ES DESI-DR2 pair or old-BAO pair.
- Nested ΔlnZ for TRGB stack: **not** this package (no TRGB nested EV run booked here).

## Rank files (authority host: routed)

- dyad: `/home/ubuntu/prtoe_class/chains/dyad_mnu_bbnfix_desidr2_trgb.{1..32}.txt`
- lcdm: `/home/ubuntu/prtoe_class/chains/cmp_lcdm_mnu_bbnfix_desidr2_trgb.{1,2,3}.txt`
- Local lcdm mirror: `docs/chains/cmp_lcdm_mnu_bbnfix_desidr2_trgb.*`

## GetDist marginals (`ignore_rows=0.3`)

Authority JSON: [`../trgb_results_20260812/all_summary.json`](../trgb_results_20260812/all_summary.json)

### `dyad_mnu_bbnfix_desidr2_trgb` (154398 post-burn samples)

| parameter | mean ± std | 68% limits |
|---|---|---|
| H0 | 68.896 ± 0.598 | [68.295, 69.510] |
| omega_b | 0.022588 ± 0.000113 | [0.022475, 0.022699] |
| dcdf_rho_inf | 0.6998 ± 0.0039 | [0.69595, 0.70374] |
| varying_me | 1.0041 ± 0.0043 | [0.99976, 1.00828] |
| m_ncdm | 0.0308 ± 0.0302 | [0.00576, 0.0551] (68% mass) |
| Omega_m | 0.3001 ± 0.0039 | [0.2962, 0.3040] |
| S8 | 0.8236 ± 0.0084 | [0.8154, 0.8318] |
| ⟨χ²⟩ | 2743.4 | |

### `cmp_lcdm_mnu_bbnfix_desidr2_trgb` (27332 post-burn samples)

| parameter | mean ± std | 68% limits |
|---|---|---|
| H0 | 68.387 ± 0.262 | [68.122, 68.647] |
| omega_b | 0.022480 ± 8.5e-5 | [0.022394, 0.022566] |
| omega_cdm | 0.11845 ± 0.00061 | [0.11785, 0.11909] |
| m_ncdm | 0.0201 ± 0.0170 | [0.00422, 0.0367] |
| Omega_m | 0.3018 ± 0.0034 | [0.2985, 0.3054] |
| S8 | 0.8224 ± 0.0075 | [0.8147, 0.8299] |
| ⟨χ²⟩ | 2742.0 | |

## Twin comparison (booked)

| quantity | value |
|---|---|
| ΔH₀ (dyad − lcdm) TRGB | **+0.51** km/s/Mpc |
| Δ⟨χ²⟩ (dyad − lcdm) | **+1.4** (essentially tied; LCDM slightly lower) |
| ΔH₀ (dyad SH0ES − dyad TRGB) | **+1.41** km/s/Mpc (ladder dependence) |

## Plots

- `docs/plots/dyad_trgb_vs_shoes_H0_rho_me_triangle.png`
- `docs/plots/dyad_trgb_vs_shoes_extended_triangle.png`
- `docs/plots/trgb_twins_dyad_vs_lcdm_triangle.png`
- `docs/plots/H0_1d_trgb_shoes_fourway.png`

## Living tables

`docs/PRTOE_CHAIN_TABLES.md` — section **DESI-DR2 + TRGB production twins (booked 2026-08-12)**

## External claim fence

- **Allowed:** parameter posteriors and ladder comparison under TRGB vs SH0ES stacks, with burn-in and R−1 stated.
- **Kill:** quoting as nested evidence; mixing TRGB and SH0ES into one H0 without labels; claiming dual-gate “converged:true” on R−1_cl (still ~0.18).

## Manual follow-up

- Optional formal `red: AGREE` stamp if tribunal requires for Stage B publish
- Nested TRGB EV legs: not launched (SH0ES nested is the production nested path)
