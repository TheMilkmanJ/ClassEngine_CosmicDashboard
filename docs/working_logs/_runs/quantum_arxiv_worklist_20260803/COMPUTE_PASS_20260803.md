# Compute pass — residual attack (resource-aware)

**Date:** 2026-08-03  
**Machine:** 6 cores / 12 threads; load ~11 from **cobaya** MCMCs (dyad + lcdm + routeD, ~15 workers).  
**Policy:** new jobs = `OMP_NUM_THREADS=1` + `nice -n 10`; **no PolyChord**; leave MCMCs alone.

## Ran

| Script | Exit | Result |
|---|---:|---|
| `scripts/quantum_pair_hamiltonian_tmsv.py` | 0 | Textbook pair \(H\) → \(r\) → \(B(r)\); all B ≤ Tsirelson; **medium \(r\) still NO** |
| `scripts/quantum_page_srad_unitary_mvp.py` | 0 | \(S_\mathrm{rad}(v)\) history; unitarity PASS; page-like shape **curiosity**; **`page_curve_claimed: false`** |

## What this pays / does not pay

| Residual | After this pass |
|---|---|
| Pair Hamiltonian | Harness exists (textbook \(H\)); **medium \((\omega,\lambda)\) still MISSING** |
| Medium \(r\) | **Still not derived** |
| Page curve Q6 | Better instrument (unitary pure-state \(S_\mathrm{rad}(v)\)); **still OPEN** |
| Born | Untouched (not a numeric close) |
| Atomic QM | Untouched |

## Next compute (when load allows / cluster)

1. Page: couple week2 continuum modes into Gaussian exterior (still instrument until red).  
2. Medium \(r\): only if corpus supplies \((\omega,\lambda)\) or equivalent — do not invent.  
3. Cluster next month: PolyChord / heavy sampling — **not this box**.

*NO FABRICATIONS. MCMCs left running.*
