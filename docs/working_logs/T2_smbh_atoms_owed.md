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

## The spin-mass confrontation, first assembly (2026-07-28, literature survey — task #31's data half)

**The 2026 data state, assembled against P-2026-034's band (M ≈ 6×10⁸–3×10⁹ M☉):**

| mass range | measured spins (X-ray reflection, ~50+ objects total) | vs the band |
|---|---|---|
| ≲ 10⁷·⁵–10⁸ M☉ | predominantly high (χ ≳ 0.9) | BELOW the band — no dip expected there ✓ |
| ≳ 10⁸ M☉ (into the band) | a tentative DECREASE — a moderate-spin population appears (a* ~ 0.5–0.7); literature's own caution: small samples, selection effects | the predicted direction ✓ |
| H1821+643 (log M ~ 9.2–10.5, at/above the band top) | a* > 0.4, "moderate" — the most massive well-constrained case | not maximal; weakly informative on band-localization |

**The verdict, both ways honest:**
- **The registered kill does NOT fire.** "A flat or oppositely-featured spin-mass plane at
  good statistics" is the kill; the plane is featured, in the predicted direction, at weak
  statistics.
- **The registered win does not fire either.** The same declining trend is DEGENERATE with
  the standard story — chaotic/incoherent accretion plus mergers at high mass predict
  moderate spins (median a ~ 0.4–0.5) in the same range. The current data cannot separate a
  superradiant band-dip from standard high-mass growth.
- **The census's earlier exposure framing is refined:** the high-spin population sits BELOW
  the band; the in-band and above-band population trends moderate. "High spins populate the
  band" was the older data state; the live state is consistent-leaning non-discrimination.
- **The discriminating shape, named:** the model predicts a LOCALIZED dip (recovery above
  ~3×10⁹ M☉ where superradiance detunes); chaotic accretion predicts a continuing or flat
  decline. Above-band recovery is therefore the clean signature, and H1821+643's a* > 0.4
  is the first weak datum on it. **The referee: NewAthena's projected homogeneous catalog
  (~50 nearby AGN at ≤10% spin precision) — the α_c chain sharpens the band meanwhile.**

Remaining for #31: the theory half — the quartic's saturation corrections to the spin-down
rate inside the band (what nonlinear saturation does to the dip's depth and edges).

**Addendum, same day — the theory half was already paid.** The census's "the quartic's
saturation corrections remain" (2026-07-18) predates the quench computation
(`scripts/superradiance_quench.py`, 2026-07-20): at the recorded λ the self-interaction is
**85 decades short** of saturating the cloud before spin-down (no O(1) rescues it), and the
attractive-case bosenova paces spin-down rather than stopping it. The saturation corrections
are therefore computed to be absent — the band's evolution is a free scalar's, which is
exactly how P-2026-034's registry note carries the exposure. Task #31 closes with both
halves: today's data assembly and the already-paid theory answer.
