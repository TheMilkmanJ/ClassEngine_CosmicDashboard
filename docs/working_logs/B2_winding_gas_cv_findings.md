# B2 — winding-gas / census tilt (closed as DEAD routes)

Code: `scripts/winding_gas_cv.py`, `scripts/winding_gas_cv_v2.py`. Failures ledger **#184**.

## Goal (historical)

Does medium specific heat / winding census near T_c supply the A_s tilt (n_s − 1 = −2/ln(M_Pl/T_on))?

## Verdict (both routes dead)

| route | result |
|---|---|
| **(1) Freeze reading** — census freezes at one comoving cell size | **DEAD (#184).** Single frozen cell → white noise → n_s = 4 vs measured ~0.965. A_s census must be a *scaling* imprint ξ(k) ~ 1/k, not a freeze. |
| **(2) 2D Gaussian / χ² tilt** from log-correlated height field | **DEAD by computation.** Exact convolution → tilt **+1/ln(k/k_IR)** — **wrong sign**, wrong coefficient, IR-anchored; banked form is UV-anchored (−2/ln(M_Pl/T_on)). |

The ν = 2/3 (3D-XY) exponent in the scripts is **static** condensation-ramp physics at T_c — a different link. Not a quench criterion for the census.

## What remains useful (not a tilt derivation)

- Census **collapse ramp** as T → T_c (patch count falls continuously).
- Log-correlated roughening of a coupled winding field (var × R² grows) — interesting hydro structure; **not** the banked tilt.

## Audience language

Do **not** claim B2 clears A_s. Say: freeze and Gaussian-height routes to the tilt are **killed**; A_s closed form remains **candidate**; imprint mechanism still open (scale-invariant ξ ∝ 1/k branch under audit).

## Grade

**CLOSED — negative results.** No further B2 derivation sessions for the tilt. A_s clearance needs another path.
