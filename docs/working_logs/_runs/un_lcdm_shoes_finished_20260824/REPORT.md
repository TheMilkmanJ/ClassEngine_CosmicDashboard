# SH0ES LCDM UltraNest — finished summary (2026-08-24)

**Host:** `i-0e353f38544397a6d` (`prtoe-gold-pc-shoes-lcdm-96`)  
**Remote:** `/home/ubuntu/docs_runs/ultranest_20260811/un_lcdm_ev_prod`  
**Launch:** 2026-08-11 05:04 UTC, MPI×96, nlive=400  
**Finished:** 2026-08-24 03:01:24 UTC (`done iterating`)  
**Peeled:** 2026-08-24 04:23 UTC via SSM

This is a **one-leg receipt**. It is **not** a nested ΔlnZ booking. The SH0ES UltraNest **dyad** twin is still running.

## Evidence (authority = JSON)

| | |
|---|---|
| engine | UltraNest 4.5.0 `ReactiveNestedSampler` |
| nlive | 400 |
| frac_remain | 0.01 |
| mpi_size | 96 |
| niter | 15395 |
| ncall | 2,048,560 |
| ESS | 3544.6 (need >400) |
| wall | 309.93 h |
| **logZ** | **−1413.4857 ± 0.5842** |
| MWW insertion-order | `converged: true` |

Driver line:

```
[ultranest_cobaya] DONE logZ=-1413.4857 ± 0.5842 wall=309.93h mpi_size=96
```

UltraNest also printed `logZ = -1414 +- 0` in `debug.log`. That is a **rounded display**. Quote the JSON, not that line.

Stop checks from the engine:

- ESS satisfied
- posterior KL 0.45 nat (need <0.50)
- evidence dlogz=0.01 (need <0.5)

## What this does not do

- Does **not** book `ΔlnZ = ln Z_dyad − ln Z_lcdm` (dyad UN still live).
- Does **not** replace Stage A MCMC posteriors in `PRTOE_CHAIN_TABLES.md`.
- Does **not** mix SH0ES vs TRGB vs no-H0.
- Does **not** treat live PolyChord logZ as a cross-check until PC `.stats` are final.

## Yaml honesty

The yaml **on the box** (copied here as `cmp_lcdm_mnu_bbnfix_desidr2_ev.host.yaml`) has sha256 `af4a51a961e7e47425fae9422210e03d3eee030cd56eddb0e3317c79947df963` (3890 bytes).

The 2026-08-13 repro freeze file `cmp_lcdm_mnu_bbnfix_desidr2_ev.yaml` is `71ddb9af…` (5703 bytes). **They do not match.** The nested integrand still came from this host yaml + `scripts/ultranest_cobaya.py` (the yaml `sampler: polychord` block is unused by the UN driver; UN used nlive=400 / frac_remain=0.01 from the launch).

## Nested posterior means (this UN run only)

From `info/results.json` / `post_summary.csv`. Not Stage A GetDist.

| parameter | mean | stdev |
|---|---:|---:|
| omega_b | 0.022518 | 0.000082 |
| H0 | 68.698 | 0.245 |
| logA | 3.0551 | 0.0133 |
| omega_cdm | 0.11790 | 0.00059 |
| n_s | 0.97267 | 0.00282 |
| z_reio | 8.309 | 0.664 |
| m_ncdm | 0.0141 | 0.0132 |

## Files in this folder

- `ultranest_summary.json` — driver summary (logZ authority)
- `results.json` — UltraNest `info/results.json`
- `post_summary.csv`
- `launch.log`
- `cmp_lcdm_mnu_bbnfix_desidr2_ev.host.yaml`
- `debug_info_tail.txt` / `runlog_tail.txt`
- `RECEIPT.json`

Left on the instance (not committed; too large for this receipt): `debug.log`, weighted/equal-weight chains, `results/points.hdf5`.
