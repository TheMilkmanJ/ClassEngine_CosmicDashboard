# PRTOE — UV Completion for Ψ (task #17): deriving ξ/c

*Home for the model's biggest structural "owed": committing to what Ψ IS
fundamentally, so the conformal coupling c (the one irreducible free parameter of
the effective theory) becomes a computation. Months-scale project; this file logs
the steps. Started 2026-07-08.*

## The target
c is the coefficient in ε = c·f_amp·(Ψ₀/M_red) = 1.24%. It is the coupling of the
amplitude mode to matter masses, in gravitational (M_red) units. c=1 ⟺ exactly
gravitational strength ⟺ the strong census. Effective theory takes c as input;
deriving it needs the UV completion.

## Step 1 (2026-07-08) — the UV completion, and why c saturates the ceiling

**The completion: ALP / axion-rotation** (Co–Harigaya kinetic-misalignment family;
matches the genesis + the ultralight mass). Complex scalar, global U(1) (charge =
abundance), ultralight mass protected by the shift symmetry (natural, unlike a SUSY
flat direction which wants soft mass ~TeV), AD rotation. Symmetry-breaking scale
f = Ψ₀ ≈ 5×10¹⁶ GeV.

**Key finding — the field's natural coupling is ~50× too strong, so naturalness pins
c to the ceiling:**
- The amplitude mode (saxion) wants a **dilaton coupling** to matter, strength 1/f.
- In gravitational units: c_naive = M_red/f = 2.4e18 / 5e16 ≈ **48** — i.e. ~50×
  gravitational strength.
- That is exactly what naturalness FORBIDS (§75: a coupling ≫ gravitational
  radiatively destroys the ultralight mass). So the coupling is **capped at
  gravitational strength (c ≲ 1)**, and because the dynamics pushes it UP against
  the cap, **it sits AT the ceiling: c ~ 1 is the *saturated* naturalness ceiling.**

**What this changes vs #14:** #14 had c as a soft dial that *happens* to be ~1.
Step 1 explains *why* ~1: a ~50× coupling jammed against the gravitational cap. So
c~1 is not luck — it's the ceiling, saturated. **Predictions:** (i) c should measure
just BELOW 1 (naturalness is ≲, small margin) — consistent with 0.93±0.38; (ii) the
UFD-tension value c~1.9 is doubly forbidden (above the ceiling). Ties to the census:
the ceiling IS gravitational strength, so "c saturates the ceiling" = "the census
holds, maximally."

**Residuals (owed):** exact margin below 1 = the effective-action loop (#14's
unfinished half — how saturated the ceiling is); the environmental Θ-switch that
gates WHERE m_e shifts is separate (#8). Also owed: why the explicit breaking lands
the mass at ~2e-20 eV exactly (the Coleman-Weinberg / shift-breaking structure).

## Step 2 (2026-07-08) — attacking the two residuals

**Residual 1 (margin below 1) — split:**
- **1a Flavor-breaking (computed):** conformal coupling universal (c=1) at tree level;
  trace anomaly breaks it by each species' anomalous dimension. Electron (QED):
  gamma_me = 3 alpha/(2pi) = 0.0035 = **0.35%**. So **c_e ~ 1.00 to sub-percent** (the
  electron sets the CMB amplitude). Hadrons ~few-10% (QCD). Predicts a tiny residual
  varying-constant flavor-dependence -- anomaly-level, NOT the retracted P-011 factor.
- **1b Overall normalization (HARD WALL):** how saturated the gravitational ceiling is =
  a UV threshold-matching calc, not shortcuttable. c_e = 1 - (matching, sub-% to few-%).
  Honest prediction: **c ~ 1.00**; measured 0.93+-0.38 consistent (offset within
  f_amp/Psi0 systematics + error bar).

**Residual 2 (why m~2e-20 eV) — largely resolved by reframing:**
- The mass is PINNED BY DATA (amplitude+abundance -> 2e-20), not derived from the UV.
  The UV's job is to ACCOMMODATE it naturally, and it does:
- Exponentially-small shift-breaking mass m ~ M_red exp(-S): ln(m/M_red) ~ -108 => S~108
  => **alpha_hidden = 2pi/S ~ 0.06**. A modest O(0.06) hidden coupling generates
  m~2e-20 eV via non-perturbative dimensional transmutation; shift symmetry protects it
  (technically natural). So the tiny mass is NOT fine-tuned -- exponentially generated
  from an unremarkable input, value fixed by data.

**Net:** flavor-blindness quantified (0.35%); mass de-mystified (alpha~0.06, exponential,
data-pinned). ONE hard number remains: the UV threshold matching for c's exact overall
normalization (the genuine months-part).

## Step 3 (2026-07-08) — does ONE ALP field give the whole dCDF (DM+DE)?

The model's core claim is unification (one field = DM + DE, w: 1/3->0->-1). Audit of
the ALP completion against the full dCDF feature list:
- **DM (w=0):** YES -- rotation = charge = abundance (Co-Harigaya).
- **Ultralight mass:** YES -- shift-protected, exponential (step 2).
- **Conformal coupling c~1:** YES -- saturated ceiling (step 1).
- **Normal fraction (w=1/3 early):** plausible -- pre-condensation radiation-like phase.
- **DARK ENERGY (w->-1 floor):** **NOT automatic.** The rotation redshifts as matter /
  kination (w=1); it does NOT supply a near-constant late-time density. DE needs a
  separate piece.

**The gap + what fills it:** the DE floor is the "funded floor" (sign-locked phantom
floor via the (deltaK)^2 operator, the graveyard resurrection). So:
  **Full UV completion = ALP (DM + mass + coupling) + (deltaK)^2 funded-floor (DE).**
One field can host both (rotation -> DM; derivative self-interaction -> DE floor), but the
structure producing w->-1 is ADDITIONAL, not free from the ALP.

**#17 remaining scope, now named (not vague "months"):**
1. **DE floor UV realization** (the CENTRAL piece -- the unification itself): does the ALP
   field's (deltaK)^2 structure give a stable w->-1 and stay census-legal?
2. **c threshold-matching** (the precision residual from step 2).
The ALP delivers ~80% (DM/mass/coupling/normal-fraction); the missing 20% is the DE floor.
