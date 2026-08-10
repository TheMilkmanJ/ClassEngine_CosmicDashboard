# DESI-DR2 sample-cov Laplace — 2026-08-10

**Status:** PROCESS COMPLETE on booked DESI-DR2 pair  
**Not nested.** Soft modes present.

**Artifact:** [`laplace_desi.json`](laplace_desi.json)  
**Command:** `python3 scripts/laplace_from_bbnfix_chains.py --chain-dir chains --which desi`

## Results

| leg | map −logpost | logZ_Laplace | cond(Σ) | gate ready |
|---|---:|---:|---:|---|
| `dyad_mnu_bbnfix_desidr2` | 1375.803 | −1435.146 | ~3.1×10⁸ | true |
| `cmp_lcdm_mnu_bbnfix_desidr2` | 1379.751 | −1436.530 | ~1.8×10⁸ | true |

| quantity | value |
|---|---:|
| **ΔlnZ_Laplace (dyad−lcdm)** | **+1.384** |
| Δ(min −logpost) proxy | −3.948 |

## Reading

- On the DESI-DR2 stack, sample-cov Laplace is **larger than** the old-BAO **+0.21** but still **soft-mode sensitive** (cond ~10⁸).
- MAP advantage for dyad is **not** evidence by itself.
- **Do not** mix this ΔlnZ with old-BAO. **Do not** call nested.
- Gold nested PolyChord remains the referee.

*NO FABRICATIONS.*
