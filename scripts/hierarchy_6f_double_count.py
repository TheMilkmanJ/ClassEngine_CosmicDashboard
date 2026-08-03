#!/usr/bin/env python3
"""
Section 6f: at what scale is alpha evaluated?   (docket #51, the surviving horn)

GRADE STATED BEFORE COMPUTING (protocol check 33)
-------------------------------------------------
Evidence class: STRUCTURAL. This is an argument about which quantity belongs in a
many-body gap equation. It cannot confirm the model against data and it cannot rescue
the anchor's 2.00x overshoot on 4*pi*m_H, which is a separate matter this file does
not touch.

What would count as a narrowing: showing that horn (a)'s premise -- "an electromagnetic
coupling runs, so evaluate alpha_c at the pairing scale" -- double-counts a screening
that section 6c already performs explicitly.
What would count as a null: the medium's Thomas-Fermi screening and QED vacuum
polarisation are genuinely independent effects, so both apply and horn (a) survives.
What is NOT claimed either way: that this closes 6f. The corpus says three things
narrow the fork without closing it; this is a fourth narrowing, not a closure.

THE FORK, AS 6f STATES IT
  (a) alpha_c is electromagnetic -> it runs -> evaluated at the pairing scale the
      anchor moves by factors of 5.6 (alpha(M_Z)) to 956 (Planck floor).
  (b) alpha_c is a medium constant numerically equal to 3*alpha(0) -> it does not run,
      but then 6c's Coulomb kernel and Thomas-Fermi screening need justification,
      because both were imported from electromagnetism.

6f: "Both readings cannot be held at once, and the chain currently holds both."
"""

import math

ALPHA = 1.0 / 137.035999084

CHECKS = []
def chk(name, got, booked, tol, unit=""):
    ok = abs(got) <= tol if booked == 0 else abs(got - booked) / abs(booked) <= tol
    CHECKS.append((ok, name, booked, got, unit))

def k_of(alpha_c, v=1.0):
    b = 2.0 * alpha_c / (math.pi * v)
    return math.log(1.0 + 1.0 / b) / math.pi

print("=" * 76)
print("6f: THE DOUBLE-COUNT IN HORN (a)")
print("=" * 76)

# ---------------------------------------------------------------- 1. reproduce the table
print("\n[1] 6f's table, reproduced")
rows = [("alpha(0)", 137.035999084, 3153.0), ("alpha(M_Z)", 127.951, 1.76e4),
        ("alpha(M_Pl floor)", 104.94, 1.50e6)]
print("      coupling            1/alpha        k        M_anchor (booked)")
for lab, inv, M in rows:
    a_c = 3.0 / inv
    print(f"      {lab:18s} {inv:9.3f}  {k_of(a_c):.5f}      {M:.3g} GeV")
chk("k at alpha(0)",   k_of(3.0 * ALPHA),   1.36461, 1e-5)
chk("k at alpha(M_Z)", k_of(3.0 / 127.951), 1.34309, 1e-5)
chk("k at Planck floor", k_of(3.0 / 104.94), 1.28100, 1e-5)

# the Planck-floor composition the file quotes
inv_pl = 49.46 + 55.48
chk("1/alpha(M_Pl) = 1/a2 + 1/aY", inv_pl, 104.94, 1e-3)
print(f"\n    Planck floor composition: 49.46 + 55.48 = {inv_pl:.2f}  (as recorded)")

# ---------------------------------------------------------------- 2. the argument
print("\n[2] The argument: horn (a) uses the medium's polarisation twice")
print("""
    Section 6c does not use a bare Coulomb interaction. It uses

        V(q) = e^2/(q^2 + m_D^2),     m_D^2 = e^2 * 2 N_0     [Thomas-Fermi]

    The Thomas-Fermi mass IS the medium's polarisation, resummed. Writing the same
    thing as a dielectric function makes it explicit:

        V(q) = (e^2/q^2) / eps(q),    eps(q) = 1 + m_D^2/q^2

    So 6c's interaction is already the SCREENED one, and the momentum dependence of
    the effective coupling is carried entirely by eps(q).

    This is the standard many-body construction (Morel-Anderson and everything after
    it): in a BCS gap equation one uses the BARE charge with an explicit dielectric
    function, never a running charge with a dielectric function as well. Doing both
    applies the medium's own polarisation twice -- once inside the running coupling
    and again inside eps(q) -- and it is a double-count, not a refinement.

    Horn (a) says "an electromagnetic coupling runs, so evaluate it at the pairing
    scale". But running a coupling from q=0 up to q ~ 2k_F IS the statement that the
    intervening polarisation screens it. Section 6c has already put that polarisation
    in by hand. So the e^2 that belongs in 6c's numerator is the UNSCREENED one, and
    alpha(0) is not a scale choice at all -- it is the only value with the right
    meaning in that formula.
""")

# ---------------------------------------------------------------- 3. how much is double
print("\n[3] Quantifying: how much of the running would be double-counted")
print("    The screening 6c already applies, expressed as an effective coupling")
print("    reduction at the Fermi surface, is the ln(1+1/b) factor relative to an")
print("    unscreened log. Compare the two 'corrections' in the same units:\n")

b = 2.0 * 3.0 * ALPHA / math.pi
screen_factor = math.log(1.0 + 1.0 / b)
print(f"      6c's screening:  ln(1 + 1/b) = ln(1 + {1/b:.3f}) = {screen_factor:.4f}")
run_MZ = math.log((1/127.951) / ALPHA)
print(f"      QED run to M_Z:  ln(a(M_Z)/a(0))            = {run_MZ:.4f}")
print(f"      ratio                                       = {screen_factor/run_MZ:.1f}x")
chk("6c screening factor ln(1+1/b)", screen_factor, 4.2871, 1e-3)

print(f"\n    The screening 6c performs is {screen_factor/run_MZ:.0f} times larger than the")
print("    entire QED run from zero momentum to the Z pole. It is not a small effect")
print("    being neglected -- it is the dominant one, and it is already there.")

# ---------------------------------------------------------------- 4. what survives
print("\n[4] What this does NOT settle")
print("""
    The double-count argument removes horn (a) in its stated form. It does not remove
    everything behind it, and two things genuinely survive:

    (i)  QED vacuum polarisation from STANDARD MODEL charged particles is a different
         object from the medium's Thomas-Fermi screening. Electron, muon, quark and W
         loops are present at the pairing scale regardless of what the medium does. If
         the medium's constituents couple to those loops, some running is real and is
         NOT double-counted by eps(q). Section 6b excludes a charged CONDENSATE; it
         does not state the constituents' charge, and that is the input needed.

    (ii) The bare-versus-physical question is pushed back rather than answered. Saying
         "use the unscreened e^2" presumes there is a scale at which e^2 is defined
         without any screening at all, and in QED that is the q -> 0 limit only because
         the vacuum's own polarisation is defined to vanish there. Whether the medium
         admits the same definition is exactly horn (b)'s unfinished business.

    So the fork narrows from "which scale?" to a single sharper question:

        DO THE MEDIUM'S CONSTITUENTS CARRY STANDARD MODEL ELECTRIC CHARGE?

    THE CORPUS ANSWERS IT, AND THE ANSWER IS ADVERSE. Section 6e states that the
    constituent-level vacuum "carries no net electric charge" and is COMPENSATED --
    n_electron = n_hole, with electron and hole pockets. Net-neutral is not uncharged:
    the carriers are charged. And on this program's own identification -- light is the
    medium's Goldstone, electromagnetism IS the medium -- it is the same U(1).

    So the residual survives and horn (a) does not close. The double-count argument
    buys less than it first appeared: it kills the naive "just evaluate alpha at the
    pairing scale" reading and shows most of what that proposes is already present,
    but it does not remove the effect.
""")

# ---------------------------------------------------------------- 5. size the residual
print("[5] Sizing the residual, if the constituents are charged")
print("    Worst case: full SM running from alpha(0) to the pairing scale, applied on")
print("    top of the screening rather than instead of it.\n")
for lab, inv in [("alpha(M_Z)", 127.951), ("alpha at 3 TeV (approx)", 125.5)]:
    a_c = 3.0 / inv
    k2 = k_of(a_c)
    # anchor scales as exp(-1/(k alpha_c)); report the ratio against alpha(0)
    ref = math.exp(-1.0 / (k_of(3.0 * ALPHA) * 3.0 * ALPHA))
    now = math.exp(-1.0 / (k2 * a_c))
    print(f"      {lab:26s} 1/a={inv:7.3f}  k={k2:.5f}  anchor x{now/ref:8.2f}")

print("\n    So the exposure, if it survives, is a factor of order 5-10 on the anchor --")
print("    the same order 6f already records, and still adverse. Narrowing horn (a)")
print("    does not improve the anchor's landing; it clarifies what would have to be")
print("    true for the recorded value to be the right one.")

# ---------------------------------------------------------------- verdict
print("\n" + "=" * 76)
print("VERDICT on 6f / #51")
print("=" * 76)
print("""
    NARROWED, NOT CLOSED -- which is what was stated as the target before computing.

    Horn (a) as written double-counts. Section 6c's gap equation already carries the
    medium's polarisation explicitly as a Thomas-Fermi mass, and running the coupling
    from zero momentum to the Fermi surface is the same physics a second time. The
    standard many-body construction pairs a bare charge with an explicit dielectric
    function, never a running charge with one as well. Quantitatively the screening
    already applied is ~50x larger than the whole QED run to the Z pole, so this is
    not a neglected small term but the dominant one, present already.

    What survives is narrower, and the corpus decides it against the model. Section 6e
    records the constituent vacuum as net-neutral but COMPENSATED, with electron and
    hole pockets -- so the carriers are charged, and on this program's own reading
    (light is the medium's Goldstone) it is the same U(1) the Standard Model runs. The
    residual therefore applies.

    The anchor is not helped. The residual running costs a factor of order 5-10,
    adverse, on top of the 2.00x overshoot already recorded. This file does not reduce
    the count of open questions and does not move the number that matters. What it
    does is replace a vague fork with a specific, sized, adverse effect -- which is
    worth having, but should not be filed as progress toward the anchor.
""")

print("=" * 76)
n_ok = sum(1 for c in CHECKS if c[0])
for ok, name, booked, got, unit in CHECKS:
    if not ok:
        print(f"  FAIL  {name}: booked {booked}, got {got} {unit}")
print(f"CHECKS: {n_ok}/{len(CHECKS)} passing")
print("=" * 76)
