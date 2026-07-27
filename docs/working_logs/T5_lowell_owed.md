# T5 low-ℓ anomalies — OWED
1. THE CAVITY C_ℓ COMPUTATION (the decisive one): compact-torus + winding modulation → predicted low-ℓ spectrum/alignments; without it "predicts the anomalies" stays a claim.
2. THE MATCHED-CIRCLES CHECK (internal review flag: existing nulls may already exclude an observably-small torus — reconcile with L ≥ 27.6 Gpc).
3. BipoSH/isotropy policing of the axis family (jointly with P-024/P-029 — internal review estimator-class check).
4. The axis-of-evil direction vs the family's shared axis (a measurable consistency).

Coupling-geometry status: screened-room (solar system) — verdicts hold by geometry.

## PAID: items 1 and 2 — the cavity computation
Suppression confined to ℓ ≲ 4; the test relocated to the off-diagonal covariance; matched-circles
reconciled at L ≥ 27.6 Gpc.

**Regenerated on a retained script (2026-07-20, `scripts/torus_lowell_pattern.py`).**
Both numbers the first pass booked have moved, and in opposite directions:

| quantity | first pass | regenerated (ISW-inclusive) |
|---|---|---|
| quadrupole retention at the 27.6 Gpc floor | 83% | **90%** |
| power-spectrum S/N over ℓ = 2–6 | 0.27 | **0.16** |
| off-diagonal S/N over 990 pairs | 2.2 | **1.4** (2.0 on Sachs–Wolfe alone) |
| strongest ρ (ℓ = 4, m = ∓4) | +0.68 | **+0.47** |

The suppression is shallower than booked and the correlation channel is thinner. The cause of the
retention move is method, not cosmology: a finite box is a mode **lattice**, and the sharp-cutoff
continuum estimate that returns 49% at this floor discards the six modes sitting exactly at
k_min. The script carries the two side by side, checks the lattice sum two independent ways, and
verifies that retention returns to unity as the box grows.

Items 3–4: the BipoSH joint pass remains on the referee calendar with the regenerated pattern
handed to it. It now grades a 1.4σ structure, not a 2.2σ one.

## The BipoSH estimator pass — built and graded (2026-07-28, task #34)

`scripts/biposh_estimator_pass.py`, on the retained generator's covariance
(45×45, ℓ ∈ [2,6], ISW-inclusive, at the matched-circles floor). Wigner 3j from
the Racah formula in exact integer arithmetic, validated against the
independent J-even closed form (the v1 check value was itself a garbled CG —
the implementation was right and the independent formula proved it).

**The build's three results:**
1. **The cubic selection rule EMERGES from the projection:** all 103 populated
   anisotropic components satisfy L even with M ≡ 0 (mod 4) — the cubic point
   group's own rule, not imposed. The template tower is the expected cubic
   sequence: L = 8 (ℓ₁ℓ₂ = 44) at 0.83 dimensionless, L = 4 (22) at 0.69,
   L = 12 (66) at 0.67, with the ±M partners at their forced ratios.
2. **The grading refines 1.4 → 1.7:** the matched-filter S/N over the full
   anisotropic BipoSH set is **1.68**, against the generator's off-diagonal-only
   Σρ² figure of 1.44. The 17% excess is identified, not mysterious: the
   m-dependent DIAGONAL anisotropy (⟨|a_ℓm|²⟩ varying with m at fixed ℓ) is
   real pattern information the off-diagonal ρ measure cannot see and the
   ℓ₁ = ℓ₂, L > 0 BipoSH components capture. Both figures are cosmic-variance
   statements on the template; 1.7σ is the estimator's honest ceiling on
   Planck-class low-ℓ data in the pattern's own frame.
3. **Data application, stated for the calendar:** Â^{LM}_{ℓ1ℓ2} from measured
   a_ℓm rotated to the pattern frame — or frame-maximized, which then carries
   its look-elsewhere factor in the grading. External; the instrument is now
   on the shelf for it. T12's estimator row shares this build.
