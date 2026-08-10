# Full Laplace from docs/chains bbnfix pair — 2026-08-08

**Method:** Laplace (MAP + weighted sample covariance)  
**Chain dir:** `docs/chains/`  
**Burn-in for Σ:** ignore_rows = 0.3 (matches GetDist booking)  
**Formula:** `logZ = -min(minuslogpost) + (d/2) ln(2π) + (1/2) ln det(Σ)`  
**Not nested. Not a CosmicForge re-optimize.**

## Gate (booked pair)

| chain | R−1 | N | converged | ready |
|---|---:|---:|---|---|
| `dyad_mnu_bbnfix` | 0.048118 | 37605 | True | True |
| `cmp_lcdm_mnu_bbnfix` | 0.049324 | 26294 | True | True |

Both gate-ready: **True**

## Laplace results

| leg | d | MAP −ln(Lπ) | logZ_Laplace | cond(Σ) | n_eff (weights) |
|---|---:|---:|---:|---:|---:|
| dyad | 13 | 1375.815000 | **-1434.605256** | 3.038e+08 | 26227.4 |
| lcdm twin | 12 | 1378.777700 | **-1434.816749** | 1.992e+08 | 18093.3 |

## Model comparison

| quantity | value | note |
|---|---:|---|
| **ΔlnZ_Laplace** (dyad − lcdm) | **+0.211493** | positive favors dyad |
| Δ(min −logpost) proxy | -2.962700 | negative favors dyad; **no** volume term |

## Caveats (required)

- Gaussian / unimodal Laplace — if the posterior is multi-basin, this **overstates** sharpness.
- Sample covariance after 30% burn-in; MAP from full three-rank files.
- d differs (13 vs 12): correct for nested model comparison, not an error.
- **Not** PolyChord nested evidence.
- Applies to **old-BAO production bbnfix** stack in `docs/chains` only.
- DESI-DR2 twin pair is a **separate** live run and is **not** included here.

## Artifacts

- `laplace.json` — machine-readable
- This `REPORT.md`

*NO FABRICATIONS. Method labeled. Gate quoted.*

## Condition-number warning

Both legs show **cond(Σ) ~ 10⁸**. That means near-flat directions in the sampled
covariance; `det(Σ)` (and therefore logZ) is sensitive to those soft modes.
Treat **ΔlnZ ≈ +0.21** as a **Gaussian Laplace estimate with large volume
uncertainty**, not a nested-quality verdict. The fit-only proxy
(Δ min−logpost ≈ −2.96) still shows the dyad MAP is better; the extra dyad
parameters mostly spend that win on posterior volume under this approximation.
