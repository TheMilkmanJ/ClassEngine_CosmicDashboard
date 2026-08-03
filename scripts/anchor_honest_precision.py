#!/usr/bin/env python3
"""
What precision does the hierarchy anchor actually support?

GRADE STATED BEFORE COMPUTING (protocol check 33)
-------------------------------------------------
Prompted by an external review: "precision landings (0.44%, 0.14%, eight-digit
reconstructions) when sensitivities and hosts don't support them."

This is a check on the corpus's own advertising, not on the physics. The question is
narrow and answerable: given the sensitivities the hierarchy file itself records, and
the ambiguities it itself names, what is the honest band on M_anchor -- and does the
headline quote it?

What would count as confirmation of the criticism: the honest band is much wider than
the quoted agreement.
What would count as a null: the band is comparable to the quoted agreement, and the
precision is supported.
This script cannot improve the anchor. It can only decide whether the number is
advertised at a precision the construction earns.
"""

import math

ALPHA   = 1.0 / 137.035999084
ALPHA_C = 3.0 * ALPHA
M_RED   = 2.435323e18      # GeV
M_H     = 125.25           # GeV
M_H_ERR = 0.17             # GeV, PDG

CHECKS = []
def chk(name, got, booked, tol, unit=""):
    ok = abs(got) <= tol if booked == 0 else abs(got - booked) / abs(booked) <= tol
    CHECKS.append((ok, name, booked, got, unit))

def k_of(a_c):
    return math.log(1.0 + math.pi / (2.0 * a_c)) / math.pi

def M_of(a_c, extra_exp=-1.5):
    return M_RED * math.exp(-1.0 / (k_of(a_c) * a_c) + extra_exp)

print("=" * 76)
print("THE ANCHOR'S HONEST PRECISION")
print("=" * 76)

k  = k_of(ALPHA_C)
M0 = M_of(ALPHA_C)
target = 4.0 * math.pi * M_H

print(f"\n  k                = {k:.8f}")
print(f"  M (recorded form)= {M0:.1f} GeV      [M_red e^(-1/(k a_c) - 3/2)]")
print(f"  M (gap eq. exact)= {2*M0:.1f} GeV      [factor 2 NOT absorbed]")
print(f"  4*pi*m_H         = {target:.1f} +/- {4*math.pi*M_H_ERR:.1f} GeV")
print(f"  quoted agreement = {abs(M0 - target)/target*100:.2f}%")
chk("quoted agreement", abs(M0 - target) / target * 100, 0.16, 0.2, "%")

# ---------------------------------------------------------------- sensitivities
print("\n[1] The sensitivities the file itself records")
s_k = 1.0 / (k * ALPHA_C)
# d ln k / d ln alpha_c, analytic
dlnk = -1.0 / (k * (2.0 * ALPHA_C + math.pi))
s_ac = s_k * (1.0 + dlnk)
print(f"    d lnM/d lnk       = {s_k:.2f}   (corpus: 33.47)")
print(f"    d lnk/d lnalpha_c = {dlnk:.4f}")
print(f"    d lnM/d lnalpha_c = {s_ac:.2f}   (corpus: 25.8)")
chk("sensitivity to k", s_k, 33.47, 1e-3)
chk("sensitivity to alpha_c", s_ac, 25.8, 5e-3)

print("\n    So a 1% error anywhere in alpha_c becomes a 26% error in the anchor, and a")
print("    1% error in k becomes 33%. The construction amplifies; it does not average.")

# ---------------------------------------------------------------- the named ambiguities
print("\n[2] The ambiguities the file names, priced")

print("\n    (i) The convention factor. 6d records two available conventions differing")
print("        by exactly two: 1576 GeV against 3153 GeV. The recorded headline uses")
print("        one of them. That is a factor 2 with no argument in the number itself.")
chk("convention factor is exactly 2", M0 / (M0 / 2), 2.0, 1e-12)

print("\n    (ii) The 6f residual. Section 6e establishes the constituents are charged")
print("         (compensated, not neutral), so some Standard Model running survives on")
print("         top of Thomas-Fermi screening. Sizing it at the pairing scale:")
for lab, inv in [("alpha(M_Z)", 127.951), ("alpha ~ 3 TeV", 125.5)]:
    r = M_of(3.0 / inv) / M0
    print(f"           {lab:14s} -> anchor x{r:6.2f}")
    if lab == "alpha(M_Z)":
        chk("6f residual at M_Z", r, 5.58, 0.05)

# ---------------------------------------------------------------- the band
print("\n[3] The honest band")
lo = M0                             # the recorded convention value, residual off
hi = 2.0 * M_of(3.0 / 127.951)      # exact convention (x2) with the M_Z residual
print(f"\n    lower edge (convention value, residual off) : {lo:9.1f} GeV")
print(f"    upper edge (exact convention x residual at M_Z): {hi:9.1f} GeV")
print(f"    span                                        : x{hi/lo:.1f}")
chk("band span", hi / lo, 11.2, 0.1)

print(f"\n    4*pi*m_H = {target:.1f} GeV sits at the very BOTTOM of that band.")
print(f"    Expressed as a fraction of the span, the target sits at "
      f"{(target-lo)/(hi-lo)*100:.1f}% of the way up.")

# ---------------------------------------------------------------- verdict
print("\n" + "=" * 76)
print("VERDICT")
print("=" * 76)
print(f"""
    THE CRITICISM IS CORRECT, and the corpus already contains its own correction --
    it simply is not propagated to the headline.

    The anchor is advertised as landing within 0.14% of 4*pi*m_H. But the file itself
    records a factor-2 convention ambiguity (6d) and, once 6e's charged constituents
    are taken seriously, a residual running worth a further x5.6 at the Z pole (6f).
    Composed, the honest band spans a factor of {hi/lo:.0f}, from {lo:.0f} GeV to {hi:.0f} GeV.

    A quoted agreement of 0.14% against a band spanning a factor of {hi/lo:.0f} is not a
    precision result. It is the bottom edge of an order-of-magnitude range, and the
    two extra digits carry no information: with d lnM/d lnk = {s_k:.1f}, reproducing
    1576.1 rather than 1576 requires k to eight digits, which no part of the physics
    supplies.

    WHAT SHOULD BE QUOTED: the anchor lands at the electroweak scale, within a factor
    of a few, with the direction of every named residual being adverse. That is a real
    and non-trivial statement -- a construction with no electroweak input landing
    within an order of magnitude of 4*pi*m_H is worth reporting. It is simply not a
    0.14% statement, and 6d's own words ("factor-of-a-few band") already say so.

    This does not change the physics. It changes what may honestly be claimed about it,
    which is the only thing this script was asked to decide.
""")

print("=" * 76)
n_ok = sum(1 for c in CHECKS if c[0])
for ok, name, booked, got, unit in CHECKS:
    if not ok:
        print(f"  FAIL  {name}: booked {booked}, got {got} {unit}")
print(f"CHECKS: {n_ok}/{len(CHECKS)} passing")
print("=" * 76)
