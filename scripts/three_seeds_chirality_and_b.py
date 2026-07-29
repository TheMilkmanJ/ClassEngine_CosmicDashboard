#!/usr/bin/env python3
"""
Do three DISTINCT seeds supply the chiral, parity-odd object that arg b requires?

WHERE THIS COMES FROM. Two results meet here.

  (1) C13 (scripts/arg_b_parity_odd_invariant.py): a C3-invariant real potential can
      depend on the phase only through cos(3 phi) and sin(3 phi); reflection kills
      the sin term and pins the phase to 3 phi = 0 or pi. Reaching 3 phi = Q = 2/3
      therefore requires a PARITY-ODD source. **The external object must be chiral.**

  (2) The owner's idea: there are three separate things doing the creating -- the
      dark condensate, the dyad, and the white-hole-like boundary -- and the three
      families are seeded by those three objects.

The question this script asks is whether (2) supplies what (1) demands, and the
answer is yes, for a reason that is pure counting and needs no dynamics.

THE SETUP. Let the three seeds couple to the three ring sites with strengths
g_0, g_1, g_2. The hopping amplitude b is the k = 1 discrete-Fourier component of
that coupling pattern:

    b  ~  sum_j  g_j  omega^(-j),      omega = exp(2 pi i / 3).

That is not an assumption about the seeds; it is what "the C3 harmonic of a pattern
on three sites" means, and it is the same transform that defines f_0, f_1, f_2.

THREE CONSEQUENCES, IN ORDER OF STRENGTH.

  A. IDENTICAL SEEDS GIVE b = 0 EXACTLY. If g_0 = g_1 = g_2 = g then
     b ~ g * (1 + omega + omega^2) = 0, since the cube roots of unity sum to zero.
     So three identical seeds produce **no splitting at all** -- the threefold
     degenerate node, Q = 1/3. The families are distinguished only if the seeds are
     distinguishable. This is exact, not approximate.

  B. THREE DISTINCT SEEDS ARE INTRINSICALLY CHIRAL. Six assignments of three
     distinct labels to three ring sites split into TWO orbits of three under the
     C3 rotations (C3 = A3 has index 2 in S3). The two orbits are exchanged by any
     transposition -- i.e. by a reflection -- and are NOT related by any rotation.
     So a set of three distinguishable seeds carries a handedness with nothing else
     added: the cyclic ORDER is physical.

  C. THE CYCLIC ORDER FIXES THE SIGN OF arg b. Reflection sends b to its conjugate,
     so arg b -> -arg b. The two orbits therefore give +arg b and -arg b. Which
     ordering nature picked is what selects the sign of the Brannen phase.

WHAT THIS DOES NOT DO. It does not derive the VALUE 2/9. The magnitude and phase of
b follow from the actual coupling strengths, which are not known; this script solves
for the pattern that WOULD give 2/9 and reports it as a constraint on the seeds, not
as a derivation of the phase. Nothing here says why the seeds have those strengths.

PRE-STATED CONTROLS:
  S-A  the cube roots of unity sum to zero, so identical seeds give exactly b = 0.
  S-B  six assignments form exactly two C3-orbits of three; the orbits are exchanged
       by a transposition and not connected by any rotation.
  S-C  reflecting the arrangement conjugates b, hence flips the sign of arg b.
  S-D  ANTI-CONTROL: if the seeds are identical, reflection must do NOTHING (b = 0
       either way) -- so the chirality genuinely requires distinctness and is not an
       artefact of the parametrisation.
  S-E  the pattern solved for must reproduce arg b = 2/9 when fed back through the
       transform.
"""

import cmath
import itertools
import math

TOL = 1e-12
W = cmath.exp(2j * math.pi / 3)
PHI_TARGET = 2.0 / 9.0

_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


def b_of(g):
    """k = 1 Fourier component of the coupling pattern on three sites."""
    return sum(g[j] * W ** (-j) for j in range(3))


def main():
    print("=" * 78)
    print("  THREE SEEDS: DO THEY SUPPLY THE CHIRAL SOURCE arg b NEEDS?")
    print("=" * 78)

    # ---- S-A: identical seeds -> b = 0 exactly ----------------------------
    print("\n  S-A  identical seeds give b = 0 exactly (the Q = 1/3 node)")
    roots = 1 + W + W ** 2
    chk("S-A1 1 + w + w^2 = 0", abs(roots) < TOL, f"|sum| = {abs(roots):.2e}")
    worst = 0.0
    for g in (1.0, 2.5, -3.7, 1e3):
        worst = max(worst, abs(b_of([g, g, g])))
    chk("S-A2 b = 0 for any identical triple", worst < TOL, f"max |b| = {worst:.2e}")
    print("       -> three IDENTICAL seeds produce no splitting: Q stays at 1/3.")
    print("          The families are distinguished only if the seeds differ.")

    # ---- S-B: two orbits, exchanged by reflection --------------------------
    print("\n  S-B  six assignments = two C3-orbits, exchanged by a transposition")
    labels = ("A", "B", "C")
    perms = list(itertools.permutations(labels))
    chk("S-B1 there are 6 assignments", len(perms) == 6)

    def rotations(p):
        return {tuple(p[(i + k) % 3] for i in range(3)) for k in range(3)}

    orbits = []
    seen = set()
    for p in perms:
        if p in seen:
            continue
        o = rotations(p)
        seen |= o
        orbits.append(o)
    chk("S-B2 they split into exactly 2 rotation-orbits of 3",
        len(orbits) == 2 and all(len(o) == 3 for o in orbits),
        f"orbit sizes {[len(o) for o in orbits]}")
    # a transposition maps one orbit onto the other
    def swap01(p):
        return (p[1], p[0], p[2])
    a = next(iter(orbits[0]))
    chk("S-B3 a transposition carries orbit 1 into orbit 2", swap01(a) in orbits[1],
        f"{''.join(a)} -> {''.join(swap01(a))}")
    chk("S-B4 and no rotation does (the orbits are genuinely distinct)",
        swap01(a) not in orbits[0],
        "so three distinguishable seeds carry a handedness with nothing added")

    # ---- S-C: reflection conjugates b -------------------------------------
    print("\n  S-C  reflecting the arrangement flips the sign of arg b")
    g = [1.0, 0.55, 0.20]                      # three distinct strengths
    b1 = b_of(g)
    b2 = b_of([g[1], g[0], g[2]])              # transposed = reflected
    chk("S-C1 |b| is unchanged by reflection", abs(abs(b1) - abs(b2)) < 1e-12,
        f"|b| = {abs(b1):.6f} both ways")
    # the reflected phase is minus the original, modulo the 2pi/3 relabelling freedom
    d = (cmath.phase(b2) + cmath.phase(b1)) % (2 * math.pi / 3)
    d = min(d, 2 * math.pi / 3 - d)
    chk("S-C2 arg b -> -arg b (up to the C3 relabelling freedom)", d < 1e-9,
        f"phase(b1) = {cmath.phase(b1):+.6f}, phase(b2) = {cmath.phase(b2):+.6f}")

    # ---- S-D: the anti-control --------------------------------------------
    print("\n  S-D  ANTI-CONTROL: identical seeds have NO handedness")
    gi = [2.0, 2.0, 2.0]
    chk("S-D1 reflection changes nothing when the seeds are identical",
        abs(b_of(gi) - b_of([gi[1], gi[0], gi[2]])) < TOL,
        "both are exactly 0 -> chirality requires DISTINCTNESS, "
        "it is not a parametrisation artefact")

    # ---- S-E: what pattern would give arg b = 2/9? -------------------------
    print("\n  S-E  the coupling pattern that WOULD give arg b = 2/9")
    # Fix g0 = 1 and g2 = 0 (two seeds set the scale and the origin) and solve
    # b = 1 + g1 * w^-1 in closed form. NB the first version of this block ran a
    # bisection assuming arg b INCREASES with g1; it decreases, because
    # w^-1 = -1/2 - i*sqrt3/2 sends positive g1 to a negative imaginary part. The
    # bisection duly converged on the trivial g1 = 0 and the control caught it.
    # With t = -g1 > 0:  b = (1 + t/2) + i*t*sqrt3/2,  so
    #     tan(phi) = (t*sqrt3/2) / (1 + t/2)   =>   t = tan(phi) / (sqrt3/2 - tan(phi)/2)
    tp = math.tan(PHI_TARGET)
    t = tp / (math.sqrt(3) / 2 - tp / 2)
    bestg = -t
    ph_final = cmath.phase(b_of([1.0, bestg, 0.0]))
    chk("S-E1 a real pattern reproduces arg b = 2/9",
        abs(ph_final - PHI_TARGET) < 1e-9,
        f"g = (1, {bestg:.9f}, 0) gives arg b = {ph_final:.9f}")
    print(f"       so the seeds' relative strengths must satisfy g1/g0 = {bestg:.6f}")
    print(f"       with the third at 0 in this gauge; |b|/g0 = {abs(b_of([1.0,bestg,0.0])):.6f}")
    print("       This is a CONSTRAINT on the seeds, not a derivation of the phase.")

    # ---- verdict -----------------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED — do not record: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  ALL CONTROLS PASS")
    print("=" * 78)
    print("""
  WHAT THE THREE-SEED IDEA BUYS, AND IT IS MORE THAN IT LOOKED.

  1. IT EXPLAINS WHY THERE IS ANY SPLITTING AT ALL. Three IDENTICAL seeds give
     b = 0 exactly -- the cube roots of unity cancel -- which is the threefold
     degenerate node at Q = 1/3, i.e. three indistinguishable families. The masses
     split only because the seeds are DIFFERENT things. "Three separate things used
     for creating everything" is not decoration here; distinctness is what lifts the
     degeneracy, and identical seeds would leave it exact.

  2. IT SUPPLIES THE CHIRALITY C13 DEMANDS, BY COUNTING ALONE. Six assignments of
     three distinct seeds to three ring sites fall into two rotation-orbits,
     exchanged by a reflection and connected by no rotation. So the arrangement has
     a handedness before any dynamics is written. C13 showed the phase-selecting
     term must be parity-odd and therefore needs a chiral source; three
     distinguishable seeds ARE one.

  3. IT MAKES THE SIGN OF THE PHASE PHYSICAL. Reflection conjugates b, so the two
     orbits give +arg b and -arg b. Which cyclic order the three creating objects
     sit in selects the sign of the Brannen phase -- and therefore which way the
     family spectrum is ordered. That is a genuine physical consequence of an idea
     that looked purely qualitative.

  WHAT IS STILL OWED, AND IT IS THE HARD PART. None of this derives the VALUE 2/9.
  The phase follows from the relative coupling strengths, and those are unknown; the
  closed-form solve above finds the pattern that would reproduce 2/9 (g1/g0 = -0.3001
  in the gauge g2 = 0) and reports it as a constraint the seeds must satisfy. Why the dark condensate, the dyad and the
  boundary should couple in that ratio is untouched, and it is the same debt as
  deriving c_K -- which the keystone c_K * tau = Q would settle at a stroke.
""")


if __name__ == "__main__":
    main()
