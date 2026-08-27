# no-H0 LCDM UltraNest — finished summary (2026-08-25)

**Host:** `i-02eb4dcbd633819bc` (`prtoe-noh0-un-lcdm-96`)  
**Remote:** `/home/ubuntu/docs_runs/ultranest_noh0_20260813/un_lcdm_noh0_ev_prod`  
**Finished:** 2026-08-25 03:28:34 UTC (`done iterating`)  
**Peeled:** 2026-08-25 03:53 UTC via SSM

This is a **one-leg receipt**. It is **not** a nested ΔlnZ booking. The no-H0 UltraNest **dyad** twin is still running.

Do **not** mix with finished SH0ES LCDM UN (−1413.49) or TRGB LCDM UN (−1374.36). Different ladders. The SH0ES and no-H0 numbers sitting near each other in the last three digits is coincidence of rounding, not a shared Z.

## Evidence (authority = JSON)

| | |
|---|---|
| engine | UltraNest 4.5.0 `ReactiveNestedSampler` |
| nlive | 400 |
| frac_remain | 0.01 |
| mpi_size | 96 |
| niter | 15267 |
| ncall | 2,025,808 |
| ESS | 3686.4 (need >400) |
| wall | 274.54 h |
| **logZ** | **−1374.4346 ± 0.3765** |
| MWW insertion-order | `converged: false` (1423 independent iterations) |

Driver line:

```
[ultranest_cobaya] DONE logZ=-1374.4346 ± 0.3765 wall=274.54h mpi_size=96
```

INFO print `logZ = -1374 +- 0` is rounded display. Quote the JSON. ESS and dlogz strategies passed; **MWW insertion-order did not**. That is a quality flag on this one-leg summary, not a license to skip the dyad twin.

## What this does not do

- Does **not** book no-H0 ΔlnZ (dyad UN still live, remainder ~71% at the 2026-08-25 fleet peel).
- Does **not** mix with SH0ES LCDM UN −1413.49 or TRGB LCDM UN −1374.36.
- Does **not** replace Stage A MCMC posteriors.

## Yaml honesty

Host yaml sha256 `59825fa2…` does **not** match the repo file `a514213b…`. UN used nlive=400 / frac_remain=0.01 from the launch, not a live yaml rewrite claim.

## Nested posterior means (this UN run only)

From `results.json`. Not Stage A GetDist.

| parameter | mean | stdev |
|---|---:|---:|
| omega_b | 0.022469 | 0.000086 |
| H0 | 68.348 | 0.268 |
| logA | 3.0521 | 0.0137 |
| omega_cdm | 0.11852 | 0.00062 |
| n_s | 0.97146 | 0.00286 |
| z_reio | 8.127 | 0.687 |
| m_ncdm | 0.0209 | 0.0184 |

H0 ~68.3 with no local ladder is the CMB+BAO+Pantheon+ neighborhood, not a nested verdict.
