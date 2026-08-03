# routeD, archived for basin relaunch (disjoint two-chain run)

Stopped 2026-08-01 while still running so it could be relaunched correctly.

## Failure mode

Two MPI ranks only. After ~2 days post-bb489fd2 relaunch:

- R−1 still thousands (falling slowly, not converging)
- Raw Metropolis acceptance still ~6% (progress ~0.85 is oversampled, not accept rate)
- Chains non-overlapping in logA, z_reio, dcdf_conv_g, dcdf_floor_thaw
- Chain 1 held the global best (−logpost 1378.4) but ranks did not share a basin

Raising learn_proposal_Rminus1_max to 10000 was necessary but not enough with two
far-apart ranks and a still-mis-scaled proposal.

## Fix on relaunch

1. Covmat from winning chain only, samples within +8 of best −logpost, eig-floored,
   scaled ×0.25 → routeD_basin.covmat
2. ref/proposal centered on global best sample
3. Three ranks via /usr/bin/mpirun -n 3 (Open MPI, same as dyad/lcdm)
4. learn_proposal gates remain 10000
