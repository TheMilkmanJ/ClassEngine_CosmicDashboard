# Hessian Laplace v2 launch — 2026-08-10

**Why:** v1 failed on ΛCDM (`overflow` / `logZ=-inf`) due to bad FD steps.

**Fix:** `scripts/bbnfix_hessian_laplace.py` — chain-std steps, adaptive shrink, boundary one-sided FD, eigenvalue stabilize, sample-cov cross-check.

**Instance:** `i-090c0275d8198ae14` c7i.12xlarge OMP=46  
**Started:** ~2026-08-10T05:05Z  
**Out:** `hessian_laplace_v2.json` (same directory)

**Process stamp (~05:15Z):** dyad steps applied; lcdm model loaded with `m_ncdm` step ~8.7e-4 (was 0.01). JSON not yet written.

**Not nested. Not bookable until finite both legs and owner review.**
