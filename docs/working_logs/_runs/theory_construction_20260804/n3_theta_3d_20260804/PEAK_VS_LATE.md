# Peak vs late Θ — honesty recheck (2026-08-04)

**Question:** When 0D peak \(\Theta\ge\Theta_\mathrm{lock}\approx11.71\), does **late** \(\Theta\) also lock?

## Result (stocked 0D ODE scan)

| metric | value |
|---|---:|
| peak-lock hits | **38** |
| of which hit numerical clip \(\|\Theta\|=80\) | **28** |
| **late \(\Theta\ge\Theta_\mathrm{lock}\)** | **0** |
| **late \(\Theta\ge1\)** | **0** |
| late max among peak-hits | **0.033** |
| late mean among peak-hits | **−0.010** |

Best late among peak-hits: \((n_0,\Theta_0,\kappa)=(60,-8,5)\) → peak≈12.9, late≈0.033.

## Grade implication

- “\(\Theta_\mathrm{lock}\) reachable as a **spike**” ≠ re-entry magnitude lock.  
- Settled / late \(\Theta\) in stocked damping channel stays \(O(10^{-2})\) or smaller.  
- S1 production residual **stands OPEN-BLOCKED** for re-entry lock.  
- Clip@80 runs are **not** physical lands (hard ceiling in toy integrator).

*NO FABRICATIONS. Toy peak ≠ Derived re-entry Θ.*
