# PRTOE Safe Parameter Region

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


**Date**: 2026-06-29 
**Status**: Preliminary Analysis

## Summary
- Total parameter combinations tested: 144
- Stable points: 144 (100.0%)
- Unstable points: 0 (0.0%)

## Safe Parameter Region (Preliminary)

Based on the stability sweep, the following region appears physically viable:

- `xi_prtoe` : 1.00×10⁻⁰⁷ to 1.00×10⁻⁰⁵
- `zeta_prtoe` : 0.01 to 5.00
- `phi_c_prtoe` : -3.00 to 3.00
- `delta_phi_prtoe`: 0.05 to 2.00

**Warning**: These boundaries are preliminary and based on the current parameter scan. 
They must be re-evaluated with full CLASS + PRTOE background output.

## Stability Metrics

The safe region is defined by:
- K (kinetic coefficient) > 0 (no ghost instability)
- c_s² (sound speed squared) > 0 (no gradient instability)
- c_T² = 1 (tensor speed preserved)

## Next Steps

1. Run with real CLASS background output for more accurate results
2. Expand the parameter grid for higher resolution
3. Validate with observational constraints
4. Update this document with quantitative results from real runs
