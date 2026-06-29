# Baseline Validation: PRTOE vs ΛCDM

## ⚠️ STATUS: EVIDENCE NOT YET VALIDATED

**All model comparison evidence is currently EXPLORATORY ONLY.**

A proper PRTOE vs ΛCDM comparison requires:
- Matched samplers (PolyChord for both models)
- Identical priors
- Identical likelihood stacks
- Convergence diagnostics
- Full provenance tracking

These requirements are **not yet satisfied** for the runs documented here.

---

## Current Configuration Status

| Component | PRTOE | ΛCDM | Status |
|-----------|-------|------|--------|
| **Config** | `uploaded_config.yaml` | `lcdm_comparison.yaml` | Priors now matched |
| **xi_prtoe prior** | [0, 1.2e-05] | N/A | Fixed to include 0 for Savage-Dickey validity |
| **Sampler** | Gelfand-Dey (optimizer) | PolyChord | **Different methods - comparison invalid** |
| **Evidence comparison** | — | — | **NOT VALID - removed pending matched runs** |

---

## Required Next Steps

Before any PRTOE-vs-ΛCDM evidence claim can be made:

1. **Run PRTOE with PolyChord** (not Gelfand-Dey) using `uploaded_config.yaml`
2. **Run ΛCDM with PolyChord** using `lcdm_comparison.yaml`
3. **Verify** both runs complete with convergence diagnostics
4. **Compare** evidence only after steps 1-3 are satisfied
5. **Document** full provenance (commit hash, seed, run folder, validation status)

---

## Methodology Diagnostics Only

The following diagnostics apply to the **methodology**, not the evidence comparison:

### MCMC Diagnostics (PRTOE Optimizer Run)
- Acceptance Rate: ~35% (Good: 10-50% range)
- ESS per parameter: > 100 (Good)
- R̂ (Gelman-Rubin): < 1.02 (Excellent)
- Viability Score: ~99% (Excellent)
- MCMC Samples: ~80,000 (4 chains × 20,000) (Adequate)

### PolyChord Settings (ΛCDM Baseline)
- nlive: 500
- num_repeats: 30
- precision_criterion: 0.01
- seed: 42 (reproducible)

---

## Repository References

- PRTOE configuration: `uploaded_config.yaml`
- ΛCDM configuration: `lcdm_comparison.yaml`
- Run outputs: `chains/prtoe_poly.stats`, `chains/lcdm_comparison/`

---

*Document status: Placeholder - awaiting matched PolyChord validation*
*Last updated: 2026-06-28*
