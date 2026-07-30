# routeD, stopped 2026-07-30 03:40 after 1d05h — two chains in disjoint regions

Not a rival-mode posterior. Chain 1 sat 94 log-units worse than chain 2
(minuslogpost 1480.8 vs 1386.8, so Δχ² ≈ 188): it never found the basin, rather
than finding a competing one.

The two chains explored COMPLETELY NON-OVERLAPPING ranges for a full day:

  dcdf_conv_g    chain1 [0.2743, 0.2993]   chain2 [0.1024, 0.1150]   no overlap
  m_ncdm         chain1 [0.0787, 0.1912]   chain2 [0.0043, 0.0137]   no overlap
  dcdf_rho_inf   chain1 [0.7380, 0.7485]   chain2 [0.7193, 0.7254]   no overlap

The gap in dcdf_conv_g is 0.16 — twelve times chain 1's entire explored width.
Neither chain ever visited the other's territory in ~1200 samples each.

WHY R-1 READ 19331 (recomputed from the files: ~11.5k at that point, ~12.1k at
the end, i.e. FLAT, not falling). R-1 is the largest eigenvalue of
Cov(chain means) x Cov(within-chain)^-1. The within-chain covariance had a
condition number of 7.4e9 — near-singular, because the chains barely moved in
several directions. A modest separation divided by an almost-zero spread gives
five figures. The number was correct and was reporting exactly this.

ROOT CAUSE, and it is a configuration deadlock:
  * routeD_seed.covmat gives dcdf_conv_g a proposal sd of 0.03, while the chains'
    own spread in that direction is 0.0047 — the proposal is ~6x too WIDE for the
    local posterior, so nearly every step in that direction is rejected. True
    acceptance was 6.3% / 5.8% (the 0.908 in the progress column is the
    oversampled figure, not acceptance).
  * The cure for a mis-scaled proposal is proposal learning, and it was disabled:
    learn_proposal_Rminus1_max_early = 1000 against R-1 = 12000-19000. cobaya
    logged "Convergence less than requested for updates" and refused. It could
    not learn until it converged and could not converge until it learned. Exactly
    one learn attempt fired in 29 hours.

Superseded by the relaunch of the same date. Kept because the stuck-chain
signature here is the cleanest example on the box of why a large R-1 must be
decomposed rather than waited out.
