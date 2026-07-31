# B5 — μ-injection calculator (2026-07-30)

Code: `scripts/mu_injection_calc.py`. Goal (CODE_MANIFEST B5): μ(z_inject, efficiency) with visibility ramp; draw-branch discriminator (ξ vs 1/m).

## Output (eff = 1, visibility model in script)

| z_inject | μ(eff=1) | vs instruments |
|---|---|---|
| 3e5–3e6 | 1.6e-2 → 9e-5 | FIRAS-dead if full efficiency |
| 5.6e6 | ~1.2e-9 | below PIXIE; PRISM-reachable |
| 1e7 | silent | — |

Branch discriminators:

- **ξ-branch** (z~1.2e6): eff must be < 0.030 for FIRAS; PIXIE sees eff > 3.4e-6.
- **1/m-branch** (z~5.6e6): μ(eff=1) ~ 1.2e-9 — PRISM class.

## Grade

**Tool closed.** Not a model kill by itself — maps injection efficiency/redshift to FIRAS/PIXIE/PRISM. Use when pricing draw-branch energy dumps.

