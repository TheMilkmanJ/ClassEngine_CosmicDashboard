#!/usr/bin/env python3
"""
The condensate-growth shape through z_x  (docket #67, Psi_0's profile)

GRADE STATED BEFORE COMPUTING (protocol check 33)
-------------------------------------------------
`exploratory/PRTOE_me_trigger.md` records: "Still owed: the condensate-growth shape
through z_x (Psi_0's profile -- the genesis calc)."

This script does NOT close it, and says so up front, because the tempting move here is to
assemble a plausible-looking profile from pieces that exist and present it as derived.
What it does is separate the part that IS supplied from the part that is not, so the
remaining debt is one clause rather than a whole shape.

Evidence class: BOOKKEEPING over supplied laws. Nothing new is derived.
What would close it: a stated relation between the oscillating field amplitude (which
exists from z_on) and the two-fluid condensate fraction (which turns on at z_x). That
relation is the missing clause and it is not constructed here.
"""

import math

CHECKS = []
def chk(name, got, booked, tol, unit=""):
    ok = abs(got) <= tol if booked == 0 else abs(got - booked) / abs(booked) <= tol
    CHECKS.append((ok, name, booked, got, unit))

Z_X   = 1.0e5        # basin entry, mu = m
Z_ON  = 4.03e7       # oscillation onset, H = m
Z_REC = 1100.0

print("=" * 76)
print("THE CONDENSATE-GROWTH SHAPE THROUGH z_x")
print("=" * 76)

# ---------------------------------------------------------------- what IS supplied
print("\n[1] Supplied already: the two-fluid NORMAL fraction")
print("    Landau two-fluid with a phonon branch gives rho_n ~ T^4, so below condensation")
print("      f_n(z) = (T/T_c)^n = ((1+z)/(1+z_x))^n,  n = 4 for phonons")
print("    (P-2026-009's pricing; scripts/birefringence_window.py)\n")

def f_n(z, n=4, zx=Z_X):
    return ((1.0 + z) / (1.0 + zx)) ** n

print(f"      {'z':>10} {'f_n (n=4)':>14} {'f_cond = 1-f_n':>16}")
for z in (Z_X, 30000.0, 10000.0, 3400.0, Z_REC):
    print(f"      {z:10.0f} {f_n(z):14.4e} {1-f_n(z):16.8f}")

chk("f_n at recombination (n=4)", f_n(Z_REC), 1.47e-8, 0.02)
chk("f_n = 1 exactly at z_x", f_n(Z_X), 1.0, 1e-12)

print("\n    So the CONDENSATE FRACTION through z_x is fully determined:")
print("      f_cond(z) = 1 - ((1+z)/(1+z_x))^4,  z < z_x")
print("    It rises from 0 at z_x to 1 - 1.5e-8 by recombination. That is a shape,")
print("    it is derived from standard two-fluid physics, and it is already in use.")

# ---------------------------------------------------------------- what is NOT
print("\n[2] NOT supplied: the amplitude the docket actually asks for")
print("""
    The docket asks for Psi_0's PROFILE -- the field amplitude -- not the condensate
    fraction. Those are different objects and the step between them is exactly the
    clause that is missing.

    The obstruction is an ordering the corpus records but does not reconcile:

      z_on = 4.03e7   the field begins OSCILLATING (H = m), and thereafter dilutes
                      as matter, Psi ~ a^(-3/2)
      z_x  = 1.0e5    the medium enters the BASIN (mu = m) and the condensate turns
                      on -- "nonexistent before z_x, alive at recombination"

    z_on precedes z_x by a factor of 403 in redshift. So for that entire span the
    field is described BOTH as a coherently oscillating amplitude AND as a medium
    whose condensate does not yet exist. For an ordinary ultralight scalar those are
    the same object, and the corpus's own two-fluid language says they are not.

    THE MISSING CLAUSE, stated exactly: what is the relation between the oscillating
    amplitude present from z_on and the condensate fraction that turns on at z_x?
    Three readings are available and the corpus does not choose between them --

      (a) they are the same object and "nonexistent before z_x" means thermally
          disordered rather than absent, in which case Psi ~ sqrt(f_cond) * a^(-3/2)
          and the profile follows immediately from section 1;
      (b) they are different objects -- an oscillating zero-mode and a separate
          condensed fraction of the quanta -- in which case two amplitudes exist and
          the docket must say which one it wants;
      (c) the two-fluid split applies to the EXCITATIONS on the oscillating
          background, not to the background itself, in which case Psi is untouched by
          z_x and the profile is just a^(-3/2) throughout.

    Under (a) and (c) the answer is one line. Under (b) it is a modelling decision.
    The arithmetic is not what is missing.
""")

# show what (a) and (c) would give, WITHOUT claiming either
print("[3] What each reading would give, for comparison only -- none is adopted")
print(f"\n      {'z':>10} {'(a) sqrt(f_cond)*a^-3/2':>26} {'(c) a^-3/2':>16}")
for z in (Z_X, 10000.0, Z_REC):
    a32 = (1.0 + z) ** 1.5
    print(f"      {z:10.0f} {math.sqrt(1-f_n(z))*a32:26.4e} {a32:16.4e}")
print("\n    They differ only near z_x, where sqrt(f_cond) departs from 1 --")
print(f"    at z = {0.5*Z_X:.0f} the two readings differ by "
      f"{(1-math.sqrt(1-f_n(0.5*Z_X)))*100:.1f}%, and by recombination by "
      f"{(1-math.sqrt(1-f_n(Z_REC)))*100:.1e}%.")
chk("readings (a) and (c) agree by recombination", math.sqrt(1 - f_n(Z_REC)), 1.0, 1e-7)

# ---------------------------------------------------------------- verdict
print("\n" + "=" * 76)
print("VERDICT on #67")
print("=" * 76)
print("""
    NARROWED, NOT CLOSED -- as stated before computing.

    The condensate FRACTION through z_x is supplied and derived: f_cond = 1 - (T/T_c)^4
    from the phonon two-fluid, rising from 0 at z_x to within 1.5e-8 of unity by
    recombination.

    The AMPLITUDE profile the docket asks for needs one further clause, and the clause
    is a modelling ruling rather than a calculation: how the oscillating field present
    from z_on = 4.03e7 relates to the condensate that turns on at z_x = 1.0e5, given
    that the corpus describes the medium as having no condensate for a factor of 403
    in redshift during which the field is already oscillating.

    Two of the three available readings make the profile a one-line consequence of
    what is already supplied. The third makes it a modelling decision. So the honest
    remaining debt is NOT "derive a shape" -- it is "say which of these the medium is",
    and the docket should be reworded to that, since the shape follows in two cases out
    of three.

    Recorded rather than resolved, because choosing between (a), (b) and (c) is a
    statement about the medium's structure and belongs to the owner, not to arithmetic.
""")

print("=" * 76)
n_ok = sum(1 for c in CHECKS if c[0])
for ok, name, booked, got, unit in CHECKS:
    if not ok:
        print(f"  FAIL  {name}: booked {booked}, got {got} {unit}")
print(f"CHECKS: {n_ok}/{len(CHECKS)} passing")
print("=" * 76)
