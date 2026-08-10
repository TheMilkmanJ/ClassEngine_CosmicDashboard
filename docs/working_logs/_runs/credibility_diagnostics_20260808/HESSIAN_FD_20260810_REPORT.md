# FD Hessian Laplace — process result 2026-08-10

**Status:** RUN COMPLETED, **NUMERICAL FAIL — NOT BOOKABLE**
**Instance:** `i-090c0275d8198ae14` c7i.12xlarge OMP≈46
**Script:** `scripts/bbnfix_hessian_laplace.py --which both`
**Chains:** old-BAO booked pair under `docs/chains/`

## Results (do not quote as evidence)

### dyad_mnu_bbnfix
- `map_minuslogpost_chain`: `1375.815`
- `map_minuslogpost_model`: `1375.6907961456125`
- `d`: `13`
- `logZ_hessian_laplace`: `-1436.5051547259013`
- `min_eval`: `4.702930000469898`
- `max_eval`: `554874001.301649`
- `cond`: `117984745.94480635`
- `regularized`: `False`
- `partial_hessian`: `False`

### cmp_lcdm_mnu_bbnfix
- `map_minuslogpost_chain`: `1378.7777`
- `map_minuslogpost_model`: `1378.6689867492346`
- `d`: `12`
- `logZ_hessian_laplace`: `-inf`
- `min_eval`: `nan`
- `max_eval`: `nan`
- `cond`: `nan`
- `regularized`: `False`
- `partial_hessian`: `False`

- `delta_lnZ` field: `inf`

## Interpretation

- `logdet_H = Infinity` / `logZ = -Infinity` / `min_eval = NaN` means the FD Hessian
  was **singular or non-PD** after assembly (soft directions / step-size failure),
  not a physical infinite Bayes factor.
- **Do not** use ΔlnZ = +inf. Sample-cov Laplace **ΔlnZ ≈ +0.21** remains the only
  labeled volume-aware number on this pair (still inconclusive; soft modes).
- Nested PolyChord (gold DESI-DR2 SH0ES legs) is the intended high-grade evidence path.

*NO FABRICATIONS. Process receipt only.*
