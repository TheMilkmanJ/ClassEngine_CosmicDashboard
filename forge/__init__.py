"""CosmicForge core: publication-grade evidence estimation and sampling.

Modules:
  evidence   - bridge sampling (Meng & Wong 1996) with error estimates,
               multimode combination; Gelfand-Dey retained for comparison
  ensemble   - affine-invariant ensemble sampler (Goodman & Weare 2010)
  benchmarks - analytic ground-truth suite: validates the estimator before
               it ever touches a real likelihood
"""
