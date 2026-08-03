#!/usr/bin/env python3
"""
The hierarchy's density of states, k_F, and the bend-over spectrum  (docket #58)

GRADE STATED BEFORE COMPUTING (protocol check 33)
-------------------------------------------------
Evidence class: INTERNAL CONSISTENCY. Nothing here can confirm the model against data.
It can only show that the construction closes on itself, or that it does not.

Inputs and their provenance:
    alpha_c = 3*alpha    PRE-REGISTERED, not fitted to anything here
    k       = 1.36461191 DERIVED in 6c from b = 2 alpha_c/pi -- recomputed below, not adopted
    v                    the cone velocity; the corpus works at v = 1
    k_F                  THE OBJECT THE DOCKET ASKS FOR

What would count as confirmation: the gap condition closes with no free parameter left,
and any k_F-dependence is accounted for rather than assumed away.
What would count as a null: an extra independent input is needed that the corpus does
not supply, or the bend-over spectrum has no condensing solution at lambda = 0.03.
What is NOT being re-graded here: the anchor's numerical landing (1576 GeV against
4*pi*m_H). That is a coincidence claim made elsewhere and this script does not touch it.

The docket asks to "supply the density of states and k_F". The density of states is
already supplied in 6a as N_0 = k_F^2/(pi^2 v). The interesting half is k_F, and the
result below is that the question is malformed in an informative way.
"""

import math

ALPHA   = 1.0 / 137.035999084
ALPHA_C = 3.0 * ALPHA

CHECKS = []
def chk(name, got, booked, tol, unit=""):
    ok = abs(got) <= tol if booked == 0 else abs(got - booked) / abs(booked) <= tol
    CHECKS.append((ok, name, booked, got, unit))

print("=" * 76)
print("HIERARCHY: THE DENSITY OF STATES, k_F, AND THE BEND-OVER")
print("=" * 76)

# ---------------------------------------------------------------- 1. does k_F survive?
print("\n[1] Does k_F actually enter the gap condition?")
print("    Assemble lambda = N_0 * <V>_FS from 6c's own pieces, keeping k_F symbolic.\n")
print("      N_0      = k_F^2 / (pi^2 v)                  [one band, both spins]")
print("      e^2      = 4 pi alpha_c                      [Heaviside-Lorentz]")
print("      V(q)     = e^2 / (q^2 + m_D^2)")
print("      u        = q^2/(4 k_F^2),  so <.>_FS = int_0^1 du")
print("      m_D^2    = e^2 * 2 N_0                       [2-for-screening]")
print()
print("      b  = m_D^2/(4 k_F^2) = 4 pi alpha_c * 2 k_F^2/(pi^2 v) / (4 k_F^2)")
print("         = 2 alpha_c/(pi v)                        <-- k_F CANCELS")
print()
print("      <V>_FS = int_0^1 du  e^2/(4 k_F^2 u + m_D^2)")
print("             = (e^2/4k_F^2) int_0^1 du/(u+b)")
print("             = (e^2/4k_F^2) ln(1 + 1/b)            <-- carries 1/k_F^2")
print()
print("      lambda = N_0 <V>_FS = (k_F^2/pi^2 v)(e^2/4k_F^2) ln(1+1/b)")
print("             = (alpha_c/(pi v)) ln(1 + 1/b)        <-- k_F CANCELS AGAIN")

def lam_of(kF, v=1.0):
    """lambda assembled numerically with k_F kept explicit -- must not depend on k_F."""
    N0  = kF**2 / (math.pi**2 * v)
    e2  = 4.0 * math.pi * ALPHA_C
    mD2 = e2 * 2.0 * N0
    b   = mD2 / (4.0 * kF**2)
    Vfs = (e2 / (4.0 * kF**2)) * math.log(1.0 + 1.0 / b)
    return N0 * Vfs

print("\n    Numerical check, k_F swept over eight decades:\n")
print("      k_F            lambda")
vals = []
for e in range(-4, 5):
    kF = 10.0 ** e
    L = lam_of(kF)
    vals.append(L)
    print(f"      1e{e:<+3d}        {L:.12f}")
spread = max(vals) - min(vals)
print(f"\n    spread across eight decades: {spread:.3e}")
chk("lambda is k_F-independent", spread, 0.0, 1e-15)

print("\n    k_F does not appear in the answer. It cancels twice -- once out of the")
print("    screening constant b, and once between N_0 and the Fermi-surface average.")
print("    The docket asks for a number that the construction does not contain.")

# ---------------------------------------------------------------- 2. what IS required of k_F
print("\n[2] What the construction does require of k_F")
print("    Not a value -- an inequality. Three conditions, all of them one-sided:\n")
print("      (i)   k_F > 0 strictly. At k_F = 0 the Fermi surface degenerates to the")
print("            node, N_0 -> 0, and 6a's own table records the consequence: J is")
print("            convergent, there is no log, and pairing needs lambda >= 2/3 rather")
print("            than 0.03. The node cannot pair. This is the condition that matters.")
print("      (ii)  E_F = v k_F below the bend-over, so the shell sits inside the linear")
print("            cone where rho ~ E^2 and the DOS formula used is the right one.")
print("      (iii) the shell locally flat, i.e. Delta << E_F, the usual BCS assumption.")
print()
print("    So the honest statement is that the hierarchy construction is INDEPENDENT of")
print("    where the Fermi surface sits, provided it exists and lies inside the cone.")
print("    That is a stronger result than a fitted k_F would have been: a value would")
print("    have been one more thing to justify, and there is nothing to justify.")

# ---------------------------------------------------------------- 3. recompute k
print("\n[3] Recomputing k rather than adopting it")
v = 1.0
b = 2.0 * ALPHA_C / (math.pi * v)
k_derived = math.log(1.0 + 1.0 / b) / math.pi
lam = k_derived * ALPHA_C
print(f"\n    b        = 2 alpha_c/pi      = {b:.10f}   (corpus: 0.0139369)")
print(f"    k        = ln(1+1/b)/pi     = {k_derived:.8f}   (corpus: 1.36461191)")
print(f"    lambda   = k * alpha_c      = {lam:.8f}")
chk("b = 2 alpha_c/pi", b, 0.0139369, 1e-5)
chk("k recomputed", k_derived, 1.36461191, 1e-8)
chk("lambda = k alpha_c", lam, 0.0298742, 1e-5)

# the sensitivity the file flags
sens = 1.0 / (k_derived * ALPHA_C)
print(f"    d lnM/d lnk = 1/(k alpha_c) = {sens:.2f}   (corpus: 33.47)")
chk("anchor sensitivity to k", sens, 33.47, 1e-3)

# and the one-band counterfactual, which is the check that the 2 is load-bearing
b_1band = ALPHA_C / (math.pi * v)
k_1band = math.log(1.0 + 1.0 / b_1band) / math.pi
print(f"\n    counterfactual, one-band screening: k = {k_1band:.5f} (corpus: 1.58305)")
chk("one-band counterfactual k", k_1band, 1.58305, 1e-4)
print("    The 2-for-screening is load-bearing, exactly as 6c says: dropping it moves k")
print("    by 16% and the anchor by two orders through the 33x amplification.")

# ---------------------------------------------------------------- 4. the bend-over
print("\n[4] The bend-over spectrum: does it condense at lambda = 0.03?")
print("    Spectrum: rho ~ E^p below E_*, flat above. 6a records the shell integral as")
print("    J = 1/p + ln(Lambda/E_*), verified there at p = 1,2,3. Re-verify from the")
print("    integral itself rather than trusting the closed form:\n")

def J_numeric(p, ratio, n=4_000_000):
    """J = int_0^1 (rho/rho_flat) dE/E with rho ~ E^p below E_*, flat above.
       ratio = Lambda/E_*.  Split: below E_* contributes 1/p, above contributes ln(ratio)."""
    # below: int_0^{E_*} (E/E_*)^p dE/E = 1/p   (analytic, but integrate to confirm)
    lo = 0.0
    for i in range(1, n + 1):
        x = i / n                      # x = E/E_*
        lo += x ** p / x * (1.0 / n)
    # above: int_{E_*}^{Lambda} dE/E = ln(ratio)
    return lo + math.log(ratio)

for p in (1, 2, 3):
    ratio = 100.0
    Jn = J_numeric(p, ratio, n=200_000)
    Ja = 1.0 / p + math.log(ratio)
    print(f"      p = {p}:  numeric {Jn:.6f}   closed form {Ja:.6f}   diff {abs(Jn-Ja):.2e}")
    chk(f"J closed form at p={p}", Jn, Ja, 2e-4)

print("\n    Gap condition 1 = lambda * J  =>  ln(Lambda/E_*) = 1/lambda - 1/p.")
for p in (1, 2, 3):
    lnratio = 1.0 / lam - 1.0 / p
    print(f"      p = {p}:  ln(Lambda/E_*) = {lnratio:8.3f}  =>  Lambda/E_* = e^{lnratio:.2f}")

print("\n    A solution EXISTS for every p: the condition is satisfiable, so the")
print("    bend-over spectrum does condense at lambda = 0.03. That is the half of the")
print("    docket that asks whether it condenses, and the answer is yes.")

# ---------------------------------------------------------------- 5. but
print("\n[5] Why 'it condenses' is not the same as 'it delivers the anchor'")
print("    The condition fixes Lambda/E_* -- the ratio of the cutoff to the BEND-OVER,")
print("    not a gap. Delta has dropped out of the equation entirely. So what the")
print("    bend-over spectrum determines is where the node emerges, not the scale the")
print("    hierarchy needs, and 6a already records the consequence: at p = 2 it lands")
print("    11.65 TeV against the anchor's 1576 GeV, over by e^2 = 7.4x, AND with the")
print("    wrong sign -- a deficit that raises the scale where suppression is needed.")
print("    That route is in the failures ledger and this script does not revive it.")
print()
print("    The two results are compatible and both are needed: the spectrum condenses")
print("    (this file), and the condensate it forms is not what sets the anchor (ledger).")

# ---------------------------------------------------------------- verdict
print("\n" + "=" * 76)
print("VERDICT on #58")
print("=" * 76)
print("""
    The density of states was already supplied: N_0 = k_F^2/(pi^2 v), 6a.

    k_F cannot be supplied because the construction does not contain it. It cancels
    twice -- out of the screening constant b, and between N_0 and the Fermi-surface
    average -- leaving lambda = (alpha_c/pi v) ln(1 + 1/b) with no trace of it.
    Verified numerically across eight decades of k_F to 1e-16.

    What the construction requires instead is an inequality: k_F > 0 strictly, sitting
    inside the linear cone. The strictness is the whole content -- at k_F = 0 the DOS
    vanishes, there is no log, and pairing would need lambda >= 2/3 instead of 0.03.

    The bend-over spectrum DOES condense at lambda = 0.03: the gap condition
    ln(Lambda/E_*) = 1/lambda - 1/p has a solution for every p. But it fixes the
    node-emergence scale rather than a gap, and the ledger already records that this
    route misses the anchor by e^2 with the wrong sign. Condensing and delivering the
    anchor are different claims; only the first is established here.

    Net: the docket's first half is answered by showing the quantity does not exist,
    which is a cleaner outcome than a value would have been -- a fitted k_F would have
    been one more number needing justification. The second half is answered yes, with
    the standing caveat that it does not source the exponent.
""")

print("=" * 76)
n_ok = sum(1 for c in CHECKS if c[0])
for ok, name, booked, got, unit in CHECKS:
    if not ok:
        print(f"  FAIL  {name}: booked {booked}, got {got} {unit}")
print(f"CHECKS: {n_ok}/{len(CHECKS)} passing")
print("=" * 76)
