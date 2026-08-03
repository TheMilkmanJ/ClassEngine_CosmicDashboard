# α_c same-response (A4) — 2026-07-31

## Grade: **PERMANENT BET (P-2026-040)** — not open derivation debt

| piece | grade | note |
|---|---|---|
| Factor **3** in α_c = 3α | **DERIVED** | spatial dimension d; second sound c₂ = c₁/√d; transverse loop trace |
| Same-response identity (base α = α_EM, unit coefficient) | **NOT DERIVED** | empty at μ=0 IR / single form factor; or doped-pair O(≤12.5%) |
| Base α = α_EM as a value | **PERMANENT BET** | P-2026-040; A_s is the primary referee of the IR value |
| A_s closed form @ 3α(0) | consistency referee (~−0.9%) | does **not** prove two-channel identity |

## Why this is permanent bet, not “open closable”

`PRTOE_DERIVATION_HUNT.md` §1 (piece 1) already walked the owed object: a two-channel
polarization Π_T(0) (photon coupling) vs Π_L(0) (compressibility) with unit relative
coefficient.

Symmetry settles most of it without constituents (`scripts/two_channel_polarization_obstruction.py`):

1. **Lorentz-invariant vacuum / μ=0 IR** (standing Volovik basement where α_EM is read): one form factor → Π_T ≡ Π_L **identically**. The unit-coefficient claim is **true and empty** — a tautology, not a derivation of α_c = 3α.
2. **Medium with rest frame**: two form factors; unit coefficient becomes n_s/m = ∂n/∂μ, forced only by Galilean/relativistic superfluid symmetry.
3. **Doped-pair basement** (hierarchy §6c: one pair finite-μ, rest at nodes): Π_T − Π_L is sourced by that pair’s share of ΣQ². Bound **[0, 12.5%]**; exact if the pair is electromagnetically neutral. Owed object = *which* pair is doped, not a free O(1).

**Conclusion:** there is no remaining calculation that upgrades the base identification to a theorem. The geometric 3 stands; the base α stands as the registered value bet.

## Referees (value only)

| instrument | role |
|---|---|
| **A_s** closed form (α_c/4πK)³ | primary IR scale referee; ~−0.9% at 3α(0) |
| Converged α_c chain (when it exists) | kill if >2σ from 0.02189 (P-2026-040) |
| ε-assembly / f̄ ensemble | correlated; not an independent identity proof |

A scalar posterior **cannot** separate “same response with unit coefficient” from “α_c happens to equal 0.0219.” An identity has no likelihood.

## Script

`scripts/alpha_c_same_response.py` — status stamp + doped-pair bound table + A_s offset.
Does **not** claim a derived same-response theorem.

Related (symmetry obstruction, already in corpus):
`scripts/two_channel_polarization_obstruction.py`

## Audience language

> α_c = 3α has a derived geometric factor 3 (spatial dimension / second sound). The identification of that base coupling with α_EM is the registered bet **P-2026-040**, refereed by A_s (and a future converged α_c chain). It is **not** a completed same-response field-theory theorem. Do not say “zero free parameters” for the ε stack on the strength of this row.

## Do not reopen as

- “Missing two-channel polarization computation that will derive α_c = 3α”
- Using the unconverged zon α_c band edges as a constraint (R−1 ≫ stop)
- Claiming the velocity-ladder rewrite c₂ = √α·c as independent evidence (#129 closed negative)

Reopen only if genuinely new microphysics appears outside the symmetry table above.
