# CosmicForge core (`forge/`)

Publication-grade evidence estimation, built and validated 2026-07-03.
Nothing here is imported by the running chain pipeline — safe to develop
while PolyChord runs.

## Modules
- `evidence.py`  — bridge sampling (Meng & Wong 1996) with analytic AND
  jackknife error bars; exact multimode combination via Voronoi basin
  partition (`basin_restricted` + `combine_multimode_logz`).
- `ensemble.py`  — affine-invariant stretch-move sampler + R-hat; replaces
  fixed-covariance Metropolis (handles CMB banana degeneracies untuned).
- `benchmarks.py` — analytic ground-truth suite (`python -m forge.benchmarks`).

## Measured calibration (this machine, 2026-07-03)
| problem            | miss (lnZ)  | quoted err |
|--------------------|-------------|------------|
| corr-gauss d=2     | -0.004      | 0.002      |
| corr-gauss d=8     | -0.035      | 0.003      |
| corr-gauss d=16    | -0.047      | 0.003      |
| bimodal  d=2 (2mo) | -0.002      | 0.001      |
| bimodal  d=8 (2mo) | -0.009      | 0.001      |

Documented absolute accuracy floor: **0.1 ln-units** (residual bias grows
~d^1.5; suspected finite-N bridge bias + stretch-move tail coverage — open
item). PolyChord typical noise: 0.2-0.4. Jeffreys strong-evidence bar: 2.3.

## Integration into run_cosmicforge.py (AFTER current chains finish)
1. Replace `estimate_gelfand_dey_evidence(chain, names, info)` calls with:
   `forge.evidence.bridge_sampling_logz(samples, logq, log_post_fn)` where
   `log_post_fn` wraps `model.logposterior` (needs ~500-2000 fresh CLASS
   calls; ~seconds each after the 2026-07-03 analytic-derivative speedup).
2. Replace `run_mcmc` with `forge.ensemble.run_ensemble(log_post_fn, best_x,
   init_cov=laplace_cov)` — the Hessian covariance becomes the walker init.
3. Gate evidence on `rhat < 1.03`; auto-extend chains x3 (see benchmarks.py).
4. Multimode: wrap log_post per mode with `basin_restricted(lp, mode_centers, k)`
   and sum with `combine_multimode_logz` — exact for any separation.
5. Quote `max(logz_err, logz_err_jackknife)`, never less than the 0.1 floor.
6. Keep `--seed-polychord` OFF for publishable runs until posterior
   repartitioning (Chen, Feroz & Hobson 2018) is implemented.
