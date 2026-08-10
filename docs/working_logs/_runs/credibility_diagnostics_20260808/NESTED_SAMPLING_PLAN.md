# Nested sampling plan (PolyChord) — matched evidence

## Goal

Matched ΔlnZ = logZ(dyad) − logZ(ΛCDM) under the **same** likelihood stack as the MCMC pair under study.

## Stacks

| stack | model yaml | control yaml | status |
|---|---|---|---|
| Old-BAO bbnfix | evidence twin of `dyad_mnu_bbnfix` | evidence twin of `cmp_lcdm_mnu_bbnfix` | MCMC booked; nested incomplete / prior AWS segfault+Fortran format bugs |
| DESI-DR2 | evidence twins of `*_desidr2` | same | MCMCs launching/running first |

## Hard requirements

1. **Solo PolyChord rule** — one nested job at a time on a box (historical ops rule).  
2. **Matched yamls** — same data, BBN prior symmetry, only model physics differs.  
3. **PolyChord build** — patched `read_write.F90` (missing comma before `" (Still Active)"`) + rebuild before any 96-rank run.  
4. **Report** logZ ± σ from `.stats` for **both** legs before quoting ΔlnZ.  
5. **Do not** mix sampled-ε `cmp_prtoe_dyad_ev` with bbnfix production stack without labeling.

## Suggested order

1. Finish DESI-DR2 MCMCs to dual-gate (cheaper, informs priors/covmats).  
2. Hessian Laplace C2 on booked old-BAO (local, hours not days).  
3. Nested on **one** stack (prefer DESI-DR2 once MCMCs stable) with nlive~200–250, 32–96 ranks on **on-demand**.  
4. Only then compare nested vs Hessian.

## Kill criteria

- Quote nested win from one leg only  
- Resume across unpatched Fortran  
- Treat STALLED live-points as finished  
- Soft-close without ΛCDM twin
