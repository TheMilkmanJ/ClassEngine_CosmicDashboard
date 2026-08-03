"""Section 6f's fork, priced on the corpus's own derived inputs rather than an extrapolation.

The anchor is M = 2 Lambda_shell exp(-1/lambda) with lambda = k alpha_c and k = ln(1+1/b)/pi,
b = 2 alpha_c/pi. So alpha_c enters twice and the chain records dlnM/dlnalpha_c = 25.8.

Section 6f asks at what scale alpha is evaluated and tabulates three answers, the last labelled
"naive extrapolation toward 1e18 GeV, ~106". That row need not be naive: the corpus derives the
Planck-floor value elsewhere, 1/alpha_EM(M_Pl) = 1/alpha_2 + 1/alpha_Y = 49.4 + 55.5 = 104.9,
which is the tree-level composition e = g g'/sqrt(g^2+g'^2) evaluated on one-loop-run couplings.
This script checks that value against the running, then prices the fork on it.

Run: python3 scripts/hierarchy_alpha_scale_fork.py
"""
import math

MZ = 91.1876
MPL = 1.220890e19
M_H = 125.25
LAM_SHELL = 3152.0 / (2 * math.exp(-33.474))
ALPHA_MZ_INV = 127.951
SIN2W = 0.23122


def k_of(alpha_c):
    b = 2 * alpha_c / math.pi
    return math.log(1 + 1 / b) / math.pi


def anchor(alpha_c):
    """M = 2 Lambda_shell exp(-1/(k alpha_c)), in GeV."""
    return 2 * LAM_SHELL * math.exp(-1 / (k_of(alpha_c) * alpha_c))


print("=" * 78)
print("STEP 1 -- IS THE PLANCK-FLOOR COUPLING A DERIVED NUMBER OR AN EXTRAPOLATION?")
print("=" * 78)
inv_a2_MZ = ALPHA_MZ_INV * SIN2W
inv_aY_MZ = ALPHA_MZ_INV * (1 - SIN2W)
L = math.log(MPL / MZ)
# One-loop SM: b_2 = -19/6, b_Y = +41/6, in d(1/alpha_i)/dln(mu) = -b_i/(2 pi).
inv_a2_Pl = inv_a2_MZ + (19 / 6) / (2 * math.pi) * L
inv_aY_Pl = inv_aY_MZ - (41 / 6) / (2 * math.pi) * L
print(f"  at M_Z:   1/alpha_2 = {inv_a2_MZ:.3f}   1/alpha_Y = {inv_aY_MZ:.3f}"
      f"   sum = {inv_a2_MZ+inv_aY_MZ:.3f}  (= 1/alpha(M_Z))")
print(f"  ln(M_Pl/M_Z) = {L:.3f}")
print(f"  at M_Pl:  1/alpha_2 = {inv_a2_Pl:.2f}    1/alpha_Y = {inv_aY_Pl:.2f}"
      f"    sum = {inv_a2_Pl+inv_aY_Pl:.2f}")
print(f"  the corpus's handouts:   49.4              55.5              104.9")
print()
print("  So the Planck-floor value is not an extrapolation to be apologised for -- it is the")
print("  tree-level composition of two one-loop-run couplings, and it reproduces both handouts.")

print()
print("=" * 78)
print("STEP 2 -- THE FORK, PRICED")
print("=" * 78)
inv_EM_Pl = inv_a2_Pl + inv_aY_Pl
rows = (("alpha(0) -- as recorded", 137.036),
        ("alpha(M_Z)", ALPHA_MZ_INV),
        ("alpha at the Planck floor (derived)", inv_EM_Pl))
print(f"  {'alpha used':<38} {'1/alpha':>9} {'alpha_c':>9} {'k':>9} {'M_anchor':>12}")
print("  " + "-" * 82)
for name, inv in rows:
    ac = 3.0 / inv
    print(f"  {name:<38} {inv:9.3f} {ac:9.6f} {k_of(ac):9.5f} {anchor(ac):12.4g} GeV")
print()
target = 4 * math.pi * M_H
print(f"  the target the chain aims at, 4 pi m_H = {target:.1f} GeV")
for name, inv in rows:
    print(f"    {name:<38} overshoots by x{anchor(3.0/inv)/target:.4g}")

print()
print("=" * 78)
print("STEP 3 -- THE SENSITIVITY, DERIVED RATHER THAN QUOTED")
print("=" * 78)
ac0 = 3.0 / 137.036
b0, k0 = 2 * ac0 / math.pi, k_of(3.0 / 137.036)
dlnk_dlnb = -1 / (math.pi * k0 * (1 + b0))
print(f"  1/lambda = 1/(k alpha_c) = {1/(k0*ac0):.3f}")
print(f"  dlnk/dlnb = -1/(pi k (1+b)) = {dlnk_dlnb:.6f}   (and dlnb/dlnalpha_c = 1)")
print(f"  dlnM/dlnalpha_c = (1/lambda)(1 + dlnk/dlnalpha_c) = {(1/(k0*ac0))*(1+dlnk_dlnb):.3f}")
print(f"  recorded: 25.8")
h = 1e-6
num = (math.log(anchor(ac0 * (1 + h))) - math.log(anchor(ac0 * (1 - h)))) / (2 * h)
print(f"  numerical check: {num:.3f}")

print()
print("=" * 78)
print("STEP 4 -- THE COUPLING THE EXACT LANDING NEEDS IS OUTSIDE QED'S RANGE")
print("=" * 78)


def solve_inv(target_M, lo=100.0, hi=200.0):
    f = lambda inv: anchor(3.0 / inv) - target_M
    flo = f(lo)
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if flo * f(mid) <= 0:
            hi = mid
        else:
            lo, flo = mid, f(mid)
    return 0.5 * (lo + hi)


need = solve_inv(target)
print(f"  landing the anchor exactly on 4 pi m_H needs   1/alpha = {need:.2f}"
      f"   (alpha_c = {3/need:.6f})")
print(f"  the corpus records this as 140.7 / 0.021316")
print()
print(f"  but the running coupling is bounded ABOVE by its zero-momentum value:")
print(f"    1/alpha(0)  = 137.036   <- the largest 1/alpha QED ever takes")
print(f"    1/alpha needed = {need:.2f}")
print(f"    gap = {need-137.036:.2f} in 1/alpha, i.e. {(need/137.036-1)*100:.2f}% weaker than the infrared limit")
print()
print("  Running takes alpha the other way -- stronger in the ultraviolet, so 1/alpha only")
print("  falls as the scale rises. The value the exact landing wants is therefore attained at")
print("  NO scale whatever, which is a stronger statement than 'the wrong scale was chosen'.")
print("  The best case available anywhere is the infrared endpoint, and there the anchor")
print(f"  overshoots 4 pi m_H by x{anchor(3.0/137.036)/target:.3f} -- which is the factor the chain is actually carrying.")
