#!/usr/bin/env python3
"""
lattice_joint_likelihood.py   —  T13 item 3: the fingerprint lattice's joint statistic

THE THING THIS BUILDS, AND WHY IT MATTERS
-----------------------------------------
The lattice's whole claim is that ONE amplitude eps serves EVERY row at its ASSIGNED
WEIGHT. Row-by-row agreement does not test that claim: rows can each agree while the
lattice is wrong in a way no single row detects, and one row's failure means different
things depending on its correlations with the others. The claim is only testable as a
JOINT statistic.

The lattice is testable precisely because the weights are FIXED, not fitted. The BBN
ramp eps(T) = eps*(1 - T/T_c), T_c ~ 179 keV, stamps each row:
    n/p freeze-out (~800 keV) : w = 0      (dyad OFF -- above T_c)
    D bottleneck   (~70 keV)  : w = 0.64
    Li             (~40 keV)  : w = 0.79
    recombination  (z ~ 1100) : w = 1.00
    today          (z < 50)   : w = 0      (Oklo/clock fence)
So every row predicts w_i * eps with w_i KNOWN. The lattice cannot re-weight to escape.

TWO MODES, and the second is the headline:
    eps FREE    -> dof = N - 1. Tests "can ONE eps serve all rows?"
    eps DERIVED -> dof = N.     Tests the DERIVATION (eps = c*f_bar*alpha_c = 27a/5pi),
                                with ZERO fitted parameters. This is the model's
                                headline statistic; it has nowhere to hide.

All inputs are quoted from the corpus with provenance. Nothing here is invented; where
a number is missing to complete the object, it is named as missing, not filled in.
"""
import numpy as np
from scipy import stats

# ------------------------------------------------------------------ the eps values
EPS_FIT        = 1.232     # %  production fit (CMB likelihood chains)   [THE_AMPLITUDE]
EPS_DERIVED    = 1.2543    # %  the derived stack, c*f_bar*alpha_c = 27a/5pi
EPS_CONCORD    = 1.2403    # %  the concordance joint (standing reference)
EPS_CONCORD_SD = 0.0079    # %

# ------------------------------------------------------------------ the rows
# Each row: (name, epoch weight w_i, observable, model value AT the standing eps,
#            observed value, sigma, provenance)
# NOTE the model values are quoted AT the standing eps; converting them into functions
# of eps requires the ELASTICITIES d(obs)/d(eps), which the corpus does not publish.
# That gap is reported below rather than papered over with a guess.

ROWS = [
    # name            w      model_lo model_hi   obs      sigma    source
    ("Y_p (Aver)",    0.64,  0.2495,  0.2505,   0.2453,  0.0034,  "Aver 2021"),
    ("Y_p (EMPRESS)", 0.64,  0.2495,  0.2505,   0.2370,  0.0034,  "EMPRESS 2022"),
    ("D/H (Cooke)",   0.64,  2.40,    2.42,     2.527,   0.030,   "Cooke 2018 (obs error only)"),
]

def sigmas(model, obs, sd):
    return (model - obs) / sd

print("THE FINGERPRINT LATTICE'S JOINT LIKELIHOOD  (T13 item 3)")
print("=" * 78)
print("\n[1] THE eps ROW -- the CMB's own constraint on the amplitude")
print(f"    concordance joint : {EPS_CONCORD} +/- {EPS_CONCORD_SD} %  (the standing reference)")
for label, e in (("production fit", EPS_FIT), ("DERIVED stack", EPS_DERIVED)):
    s = sigmas(e, EPS_CONCORD, EPS_CONCORD_SD)
    print(f"    {label:16s}: {e:.4f} %   -> {s:+.2f} sigma from the joint")
print("    NOTE this is stack-vs-JOINT. The corpus's quoted '1.4 sigma' is the")
print("    fit-vs-STACK spread -- a DIFFERENT comparison (|1.2543-1.232| = 0.0223,")
print("    which is 1.4 sigma only against a combined width ~0.016, i.e. fit and stack")
print("    each carrying their own error). The two numbers do not contradict; they")
print("    measure different gaps. Recorded so the joint statistic does not import a")
print("    spurious tension by comparing the wrong pair.")

print("\n[2] THE BBN ROWS -- each at its epoch weight w_i")
print(f"    {'row':16s} {'w':>5s} {'model':>14s} {'observed':>16s} {'pull':>16s}")
for name, w, mlo, mhi, obs, sd, src in ROWS:
    plo, phi = sigmas(mlo, obs, sd), sigmas(mhi, obs, sd)
    lo, hi = sorted((plo, phi))
    print(f"    {name:16s} {w:5.2f} {mlo:6.4f}-{mhi:<7.4f} {obs:8.4f}+/-{sd:<6.4f} {lo:+6.2f} to {hi:+.2f} sigma")

print("\n[3] WHAT THE BUILD FOUND -- three obstructions, none of them cosmetic")

print("\n  (a) THE HELIUM CIVIL WAR MAKES A JOINT chi2 ILL-POSED AS STATED.")
d = abs(0.2453 - 0.2370) / np.sqrt(0.0034**2 + 0.0034**2)
print(f"      Aver 0.2453+/-0.0034 vs EMPRESS 0.2370+/-0.0034 disagree with EACH OTHER at")
print(f"      {d:.1f} sigma. They are the SAME observable. Summing both into one chi2 double-")
print("      counts Y_p AND imports an unresolved systematic as if it were signal. The joint")
print("      statistic must therefore be reported as TWO BRANCHES, not one number -- or wait")
print("      for the helium resolution. This is a property of the DATA, not of the model.")

print("\n  (b) THE D/H PULL DOES NOT FOLLOW FROM ITS OWN QUOTED NUMBERS.")
for m in (2.40, 2.42):
    print(f"      model {m} vs Cooke 2.527 +/- 0.030 (obs only) -> {sigmas(m,2.527,0.030):+.2f} sigma")
print("      The corpus records this row as '~1.6-1.9 sigma'. That requires sigma ~ 0.06,")
print("      i.e. observational error PLUS the BBN theory error (the d(p,gamma)3He rate) --")
need = abs(2.41 - 2.527) / 1.75
print(f"      implied total sigma ~ {need:.3f}. The theory error is real and standard, but the")
print("      doc quotes '+/-0.030' and then reports 1.6-1.9 sigma, which that width cannot give.")
print("      NOT an error in the physics -- an error in the presentation. The row's stated")
print("      significance is only reproducible if the theory error is named. FLAGGED.")

print("\n  (c) THE ELASTICITIES ARE MISSING -- and they are what make it a LIKELIHOOD.")
print("      The corpus publishes model values AT the standing eps (Y_p -> 0.2495-0.2505,")
print("      D/H -> 2.40-2.42) but NOT d(Y_p)/d(eps) or d(D/H)/d(eps). Without those, chi2 is")
print("      computable at a POINT but is not a FUNCTION of eps -- so it cannot be minimised,")
print("      cannot yield a best-fit eps, and cannot produce the dof accounting that makes the")
print("      derived-eps test meaningful. The elasticities are one PRyM run away (vary eps,")
print("      re-run, finite-difference) -- they are not a derivation, they are a measurement.")

print("\n[4] WHAT IS DELIVERED, AND WHAT IS NOT")
print("      DELIVERED : the object's SPECIFICATION -- the fixed weights w_i from the ramp, the")
print("                  two modes (eps free: dof = N-1; eps derived: dof = N, zero fitted")
print("                  parameters), the row inventory with provenance, and the pulls at the")
print("                  standing eps.")
print("      NOT DELIVERED : a single headline chi2. It cannot be honestly quoted yet, for the")
print("                  three reasons above -- and quoting one anyway would be exactly the")
print("                  'display, not a test' failure this item exists to fix.")
print("\n      THE HONEST HEADLINE, pending (a)-(c):")
print("        chi2(eps) = SUM_i [ (O_i^obs - O_i^model(w_i * eps)) / sigma_i ]^2  + the eps row")
print("        reported in TWO helium branches, at dof = N with eps FIXED to the derived")
print("        27a/5pi -- zero fitted parameters, nowhere to hide.")
