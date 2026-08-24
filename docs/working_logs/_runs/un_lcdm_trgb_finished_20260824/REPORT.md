# TRGB LCDM UltraNest — finished summary (2026-08-24)

**Host:** `i-0c8df2e18ea719094` (`prtoe-trgb-un-lcdm-96`)  
**Remote:** `/home/ubuntu/docs_runs/ultranest_trgb_20260813/un_lcdm_trgb_ev_prod`  
**Finished:** 2026-08-24 13:48:33 UTC (`done iterating`)  
**Peeled:** 2026-08-24 18:01 UTC via SSM

This is a **one-leg receipt**. It is **not** a nested ΔlnZ booking. The TRGB UltraNest **dyad** twin is still running.

Do **not** mix with the finished SH0ES LCDM UN logZ (−1413.49). Different ladder.

## Evidence (authority = JSON)

| | |
|---|---|
| engine | UltraNest 4.5.0 `ReactiveNestedSampler` |
| nlive | 400 |
| frac_remain | 0.01 |
| mpi_size | 96 |
| niter | 15129 |
| ncall | 2,015,920 |
| ESS | 3629.9 (need >400) |
| wall | 260.87 h |
| **logZ** | **−1374.3615 ± 0.3982** |
| MWW insertion-order | `converged: true` |

Driver line:

```
[ultranest_cobaya] DONE logZ=-1374.3615 ± 0.3982 wall=260.87h mpi_size=96
```

INFO print `logZ = -1374 +- 0` is rounded display. Quote the JSON.

## What this does not do

- Does **not** book TRGB ΔlnZ (dyad UN still live, remainder ~72% at the 18:00 UTC fleet scan).
- Does **not** mix with SH0ES LCDM UN −1413.49.
- Does **not** replace Stage A MCMC TRGB posteriors.

## Yaml honesty

Host yaml sha256 `c8e4d6848c20b26a627a163b7159bb8cc0dad1cef698e14a7e66a82f29bbf9fc` (5221 bytes) does **not** match the 2026-08-13 freeze `5a5f8073…` (5236 bytes). UN used nlive=400 / frac_remain=0.01 from the launch, not the yaml `sampler: polychord` block.

## Nested posterior means (this UN run only)

From `results.json`. Not Stage A GetDist.

| parameter | mean | stdev |
|---|---:|---:|
| omega_b | 0.022471 | 0.000083 |
| H0 | 68.387 | 0.257 |
| logA | 3.0522 | 0.0131 |
| omega_cdm | 0.11847 | 0.00061 |
| n_s | 0.97165 | 0.00281 |
| z_reio | 8.137 | 0.662 |
| m_ncdm | 0.0191 | 0.0171 |

H0 ~68.4 under TRGB is the same neighborhood as Stage A (~68.5–68.9), not a nested verdict.

## Files in this folder

- `ultranest_summary.json` — driver summary (logZ authority)
- `results.json` / `post_summary.csv`
- `cmp_lcdm_mnu_bbnfix_desidr2_trgb_ev.host.yaml`
- `debug_info_tail.txt` / `runlog_tail.txt`
- `RECEIPT.json`

Chains / `points.hdf5` left on the instance.
