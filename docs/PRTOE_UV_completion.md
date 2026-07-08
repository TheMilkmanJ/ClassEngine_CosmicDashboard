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

## Step 4 (2026-07-08) — the causal chain is self-generating to DM, BREAKS at DM->DE (JP)

Common factor of every regime change: **expansion driving a THRESHOLD CROSSING** (one
quantity falls until it hits a fixed threshold): condensation at H=m; recombination at
T=binding; the engine draining the field = Hubble friction (3H phidot bleeds kinetic
energy). All are GRADUAL crossings (width) -> supports "always gradual" + "late templates
early" (every transition shares the crossing form; the late/observable one templates the
early ones).

**"How does energy fall out of matter?" -> IT DOESN'T, not on its own:**
- Matter (w=0) = field oscillating (kinetic~potential). DE (w=-1) = field frozen, potential
  dominates.
- In a SIMPLE m^2 phi^2 well the field oscillates as DM FOREVER (well bottom = 0 energy;
  freezing lands at nothing). **A simple field never becomes DE -- it stays DM to the end.**
- DE requires the field to freeze onto a nonzero POTENTIAL FLOOR = the funded-floor/(deltaK)^2
  piece (#17's missing 20%).

**Sharpest statement of the #17 gap:** the regime-change chain is SELF-GENERATING up to dark
matter (matter falls out of radiation for free, via H<m condensation) and BREAKS at DM->DE
(needs the floor as an extra ingredient). JP has now circled this same gap from THREE angles
(DM+DE audit, pressure-sign flip, causal chain). The universe keeps pointing at the floor.

## Step 5 (2026-07-08) — H is the clock: regime changes tie to the medium's scales (JP)

Every regime change fires when the expansion rate H falls through a characteristic
scale OF THE MEDIUM: condensation at H~m (m~2e-20 eV); DE onset at H~H_Lambda (floor
~meV^4). H monotonic => the medium passes each threshold ONCE, in FIXED ORDER (m first,
H_Lambda last) = the whole radiation->matter->energy chain from one downward-ticking quantity.

**Unifies the recent JP insights:**
- always-gradual = each H-crossing has width;
- intervals-lengthen = H flattens toward de Sitter (H->const), so sweep-time between
  thresholds stretches to infinity (forced, not separate);
- late-templates-early = all transitions are the same object (an H-threshold crossing).

**Predictive (not tautology):** thresholds are the medium's OWN scales, so transition
redshifts MEASURE the parameters -- DE onset z~0.7 pins floor~(meV)^4; condensation z_x
pins m~2e-20 eV.

**Vindicates "uses its own gravity" (late-time):** early, H is set by radiation (medium
rides the shared background); LATE, the medium (as DE) DOMINATES rho, so H->H_Lambda is set
by the medium's OWN floor -> the final regime change is SELF-DRIVEN (the floor sets the
expansion rate that freezes it into DE). JP was early, not wrong.

**Caveat:** "everything ties to H" is partly just cosmology; the CONTENT is that the
thresholds are the MEDIUM's scales (m, floor) -> transition-times are predictions.

## Step 6 (2026-07-08) — bracketing the dark sector: ceiling & floors (JP)

Can we extract DM's ceiling/floor and DE's floor from the current regime + H? Sorted:
- **DM floor = DE floor = rho_Lambda ~ (2.3 meV)^4:** SAME number (DM & DE cross at the
  constant floor). Measured NOW from Omega_Lambda. (Floor sits at the meV scale ~ neutrino
  mass -> the rho_Lambda ~ m_nu^4 coincidence / the "meV whisper".)
- **DE-takeover rate (density):** measured now (matter-Lambda crossing z~0.4); works even if
  w frozen.
- **DE-takeover rate (FIELD w: 0->-1, the floor's DYNAMICS):** ONLY measurable if w is
  evolving (thawing / B-branch). This is the one NEW number the current transition offers.
- **DM ceiling (peak density at condensation):** an EARLY quantity, NOT from the late
  transition -- but already pinned via m~2e-20 & Psi0~5e16 (abundance/amplitude door). Or via
  the untested late-templates-early universality.

**Bracket filled:** ceiling (pinned m,Psi0) / floor=DE-floor (Omega_Lambda now) / density-rate
(now) all in hand; the field freeze-rate is the lone future number, = DESI w(z) IF thawing.

## Step 7 (2026-07-08) — THE FLOOR MECHANISM: a sign-locked kinetic condensate

First real swing at the (deltaK)^2 funded floor (the missing 20%).
**Mechanism:** put the structure in the KINETIC term. Lagrangian P(X), X=(d phi)^2. Canonical
P=X oscillates to zero (DM forever). But if **P(X) has a minimum at X0 != 0 (ghost condensate)**,
the field settles into a constant-velocity kinetic condensate: at the min P'=0, so
**rho = -P(X0) = const, w = P/(-P) = -1 exactly.** That IS the floor. "Funded" = energy from the
kinetic condensate (not a bare Lambda); "sign-locked" = stability needs P''>0 (floor, not ceiling).
**Gives the whole transition:** high density -> X large, P~X, canonical -> DM (w=0); as rho dilutes
to rho_Lambda, field slides to X0, condensate takes over -> w runs 0->-1 -> DE. Crossover at
rho_field ~ rho_Lambda = z~0.7 automatically. GRADUAL (crossover), SELF-DRIVEN (condensate sets
rho_Lambda -> H_Lambda), CENSUS-LEGAL (self-interaction of the medium's OWN kinetic term). Makes
"one field = DM + DE" literally true (canonical high-density / condensate low-density).

**HONEST LIMITS:**
1. ADDED ingredient -- a canonical ALP has no P(X) minimum for free; the ghost-condensate structure
   is put in (census-legal, motivated, not automatic).
2. Does NOT solve the CC problem -- rho_Lambda = -P(X0) ~ (meV)^4 is still a TUNING (relocated from
   "why Lambda~meV^4" to "why X0 gives P(X0)~-meV^4"). Every dynamical-DE model has this; PRTOE no
   worse, no better. The meV~m_nu coincidence still unexplained.
3. STABILITY delicate -- ghost condensates have gradient instabilities; w=-1 stability needs the
   sign-locked certificates (alpha_T/foliation/alpha_B, corpus-cleared, the technical risk to watch).

**NET:** the floor is now a REAL mechanism (not a placeholder) -- "one field, both jobs" is
BUILDABLE; "explains the DE scale" is NOT and should not be promised. #17's missing 20% = roughed in.

## Step 8 (2026-07-08) — floor STABILITY: the (deltaK)^2 funds AND stabilizes (piece 2)

Fluctuations delta phi around the condensate minimum: sound speed **c_s^2 ~ P'(X0) = 0**
(because P'=0 IS the minimum) -> marginal at leading order (where a normal field would go
unstable). The (deltaK)^2 term RESCUES it: supplies a higher-derivative dispersion
**omega^2 ~ +k^4/M^2** (in place of the missing c_s^2 k^2). Fluctuations oscillate (stable),
NOT grow -- IF the sign is right. So **the "sign-lock" IS the stability condition**: the SAME
operator that funds the floor (P min at X0!=0) stabilizes it (k^4 dispersion, sign-locked). One
operator, both jobs -- a consistency, not a patch.
**w(z) transition:** field slides to X0 -> w runs 0->-1 as a SMOOTH MONOTONIC crossover, width
set by P''(X0) -- exactly the "gradual crossover, no step/wiggle" DESI prediction. The mechanism
PRODUCES the predicted w(z), doesn't just allow it.
**Caveat:** stable at LINEAR order with the sign-lock, but ghost condensates carry real baggage
(k^4 -> low scale M~meV; full viability debated in the literature). Standard risks flagged.

**Piece 1 (c exact):** still the threshold-matching loop, un-shortcut. Stands: flavor-break 0.35%,
overall ~1 +- (matching, sub-% to few-%). Owed honestly.
**Piece 3 (CC value):** the model already dissolves the CC's CONSTANT-NESS -- the floor is a
dynamical kinetic condensate, NOT an inert Lambda (aligns with JP's no-true-constants view). Only
the VALUE (why X0 -> P~-(meV)^4) is tuned, off the promises list. Hint: meV ~ m_nu coincidence ->
IF neutrino-connected, the value gets a dynamical origin too (speculative, unclaimed).

## Step 9 (2026-07-08) — #6 MCMC checked for the neutrino-floor thread: BOUND, not detection

Preliminary read of the running dyad_mnu chain (~9200 rows, R-1~0.2, STALLED/plateaued):
- **Sigma m_nu = UPPER LIMIT** -- mean~0.055 eV, ~24% weight piled below 0.02 eV, min=0,
  rough 95% upper ~0.13 eV (consistent w/ the Fairbank ~0.15 note). Boundary pileup at
  Sigma m_nu>=0 EXPLAINS the R-1 stall (Gelman-Rubin is bad on boundary posteriors) -> R-1<0.05
  is likely the WRONG target; the stable quantity is the upper limit.
- (Column map unreliable past m_ncdm: the "c" column read 2808 != conformal ~0.93 -> NO c value
  claimed from this chain.)

**DEBATE -- can we use it for the neutrino-funded floor (piece 3 thread)? VERDICT: NO.**
- FOR: upper limit ~0.13 eV is CONSISTENT with meV-scale masses the floor would need; thread not killed.
- AGAINST (wins): it's a BOUND not a DETECTION -- the MaVaN-floor needs the neutrino mass to SET
  rho_Lambda~m_nu^4, and a bound gives no mass to build from. Consistent != confirming. Using
  "Sigma m_nu<0.13 => floor is neutrino-funded" would over-read a non-exclusion as a confirmation.
- NET: the neutrino-floor thread stays ALIVE-BUT-UNCONFIRMED; not promoted. #6 gives a bound; a
  bound can't fund a floor.
