# T2 SMBH atoms — OWED
1. THE GROWTH-RATE COMPUTATION (internal review one physics check): superradiance shuts off for α_g ≳ 0.5 dominant modes — compute the actual window placement/timescales; does the level structure land in an observable spin-mass range?
2. The λ-self-interaction corrections to cloud growth (bosenova/saturation).
3. The spin-mass (Regge) data confrontation: current BH spin measurements vs the predicted windows at the recorded m.
4. Propagate the α_c MCMC posterior to every α_g.

Coupling-geometry status: screened-room (halo interiors) — verdicts hold by geometry.

## PAID (2026-07-19 reconciliation): item 1 — the window placement is computed and recorded
(the P-2026-034 band, 6×10⁸–3×10⁹ M☉; the atlas carries it as the live exposure). Item 3 —
subsumed into that live exposure (spin archaeology's re-pricing).

## PAID (2026-07-20): item 2 — the λ-quench is re-derived, and it fails
Run at the model's own quartic and mass (`scripts/superradiance_quench.py`), the margin is
log₁₀(N_spin-down/N_eq) = −83.7/−85.1/−85.8 at α_g = 0.1/0.3/0.5. Three results worth keeping:
(a) the two candidate quartics are **different fields**, not bare-vs-effective — λ_dyad ≈
1.3×10⁻³⁸ belongs to the high-f CW field (m_φ ~ 10⁻⁵ eV), and only λ ≈ 2×10⁻⁹¹ can enter;
(b) **p = 4**, fixed by the |211⟩|211⟩ → |100⟩|k⟩ channel, below the swept [5, 15];
(c) p was not the defect — the sweep balanced a *total* rate against a *per-particle* rate,
costing one power of λ, which is 90 decades here. Autopsy in the failures ledger.
**Still open: item 4 (chain-gated).**
