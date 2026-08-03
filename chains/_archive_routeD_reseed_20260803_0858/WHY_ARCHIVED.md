# routeD archived for basin reseed (20260803_0858)

Owner-ordered kill+reseed 2026-08-03.

## Failure mode of archived run
- R−1 last: 44.8 @ N=3182 (was 129 @ N=1593)
- Ranks partially split on z_reio (last-half means ~7.84 / 7.95 / 7.04)
- Acceptance oversampled ~1.0; not true Metropolis

## Reseed
- Global best −logpost **1375.844** on rank 1
- Basin: all samples with mlp ≤ best+8 across 3 ranks (n≈3241)
- Covmat: empirical, eig-floored, std×0.25 → routeD_basin.covmat
- refs centered on global best sample
- learn_proposal gates remain 10000
- 3 MPI ranks, fresh start (no -r)

See routeD_reseed_20260803_0858_meta.json in chains/ (or copy if present).
