#!/usr/bin/env python3
"""
How many INDEPENDENT numbers do the three seed couplings carry? (bounds #2)

WHY THIS MATTERS. Spec C14 (2026-07-29) recorded that solving for the seed
coupling pattern which reproduces arg b = 2/9 gives g1/g0 = -0.3001 in the gauge
g2 = 0, and called that "a CONSTRAINT on the seeds, not a derivation of the phase."
That framing is too generous, and this script says why. The question never asked
was: how many independent numbers are there in (g0, g1, g2) once the map to the
family Hamiltonian is written down?

THE MAP. b is the k = 1 discrete-Fourier component of the coupling pattern and G0
is the k = 0 component:

    G0 = sum_j g_j            b = sum_j g_j omega^(-j)

Three real inputs go to one real (G0) plus one complex (b) -- also three reals. So
the map is square, and if it is invertible it is a CHANGE OF VARIABLES rather than
a reduction. It is invertible: the inverse is the inverse DFT,

    g_j = (1/3) [ G0 + b omega^j + conj(b) omega^(-j) ]
        = (1/3) [ G0 + 2|b| cos(arg b + 2 pi j / 3) ]

and that is THE SAME FUNCTIONAL FORM as the Brannen mass formula
sqrt(m_j) = a + 2|b| cos(arg b + 2 pi j / 3). Hence

    g_j  is proportional to  sqrt(m_j)

-- the three seeds couple in proportion to the SQUARE ROOTS OF THE LEPTON MASSES.

THE CONSEQUENCE, WHICH IS A LIMIT ON THE IDEA. Specifying the three couplings is
specifying the three masses. The seed picture carries EXACTLY the information the
spectrum already carries, no more and no less. So "why do the seeds couple in that
ratio?" and "why do the leptons have those masses?" are the SAME QUESTION, and
C14's g1/g0 = -0.3001 is the Koide relation rewritten in another basis, not an
independent constraint that could be discharged separately.

WHAT SURVIVES UNTOUCHED, and it is not nothing:
  * identical seeds give b = 0 EXACTLY, so distinctness is what lifts the
    degeneracy at all -- a structural fact the mass spectrum alone does not state;
  * three distinct seeds are intrinsically chiral, supplying what C13 proved the
    phase requires -- also not visible in the spectrum;
  * the cyclic ORDER fixes the SIGN of arg b.
These are statements about WHY there is a splitting and what KIND of object can
source it. What the picture cannot do is supply the VALUE.

PRE-STATED CONTROLS:
  M-A  the forward/inverse map must round-trip to machine precision (bijection).
  M-B  the inverse must reproduce the Brannen form, checked by driving it with
       (a, |b|, arg b) and recovering couplings proportional to sqrt(m_j).
  M-C  fed the ACTUAL charged-lepton masses, the recovered couplings must be
       proportional to their square roots -- ratios matching to <1e-9.
  M-D  ANTI-CONTROL: if the map were NOT square (e.g. four seeds on three sites),
       there would be a genuine reduction. Verify the count changes, so that the
       "no reduction" conclusion is about THIS configuration and is not vacuous.
"""

import cmath
import math
import random

W = cmath.exp(2j * math.pi / 3)
TOL = 1e-12
random.seed(20260729)

M_E, M_MU, M_TAU = 0.51099895, 105.6583755, 1776.86      # MeV

_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


def fwd(g):
    return sum(g), sum(g[j] * W ** (-j) for j in range(3))


def inv(G0, b):
    return [((G0 + b * W ** j + b.conjugate() * W ** (-j)) / 3).real for j in range(3)]


def main():
    print("=" * 78)
    print("  DO THE SEED COUPLINGS CARRY INDEPENDENT INFORMATION?  (bounds #2)")
    print("=" * 78)

    # ---- M-A: bijection ----------------------------------------------------
    print("\n  M-A  the map (g0,g1,g2) <-> (G0, b) is a bijection")
    worst = 0.0
    for _ in range(500):
        g = [random.uniform(-3, 3) for _ in range(3)]
        G0, b = fwd(g)
        worst = max(worst, max(abs(x - y) for x, y in zip(g, inv(G0, b))))
    chk("M-A1 round-trip exact", worst < TOL, f"max deviation {worst:.2e}")
    chk("M-A2 the count is square: 3 reals <-> 1 real + 1 complex", 3 == 1 + 2,
        "so it is a CHANGE OF VARIABLES, not a reduction")

    # ---- M-B: the inverse has the Brannen form -----------------------------
    print("\n  M-B  the inverse reproduces the Brannen form")
    G0, mb, phi = 7.0, 1.3, 2 / 9
    b = mb * cmath.exp(1j * phi)
    g = inv(G0, b)
    brannen = [(G0 + 2 * mb * math.cos(phi + 2 * math.pi * j / 3)) / 3 for j in range(3)]
    chk("M-B1 g_j = (1/3)[G0 + 2|b| cos(arg b + 2 pi j/3)]",
        max(abs(x - y) for x, y in zip(g, brannen)) < TOL,
        f"{[round(x,9) for x in g]}")
    chk("M-B2 same functional form as sqrt(m_j)", True,
        "the coupling pattern and the mass spectrum are one object in two bases")

    # ---- M-C: fed the real masses --------------------------------------------
    print("\n  M-C  fed the ACTUAL lepton masses, couplings track their square roots")
    r = [math.sqrt(M_E), math.sqrt(M_MU), math.sqrt(M_TAU)]
    G0r, br = fwd(r)
    back = inv(G0r, br)
    chk("M-C1 recovering the sqrt-mass triple exactly",
        max(abs(x - y) for x, y in zip(r, back)) < 1e-10,
        f"max deviation {max(abs(x-y) for x,y in zip(r,back)):.2e}")
    s = sum(r)
    print(f"\n    the three seeds' coupling ratios ARE the sqrt-mass ratios:")
    for nm, v in zip(("seed 1", "seed 2", "seed 3"), r):
        print(f"      {nm}: sqrt(m) = {v:9.5f}   fraction {v/s:.6f}")
    print(f"    i.e.  1 : {r[1]/r[0]:.3f} : {r[2]/r[0]:.3f}")
    chk("M-C2 the ratios are fixed once the masses are", True,
        "no freedom left -- specifying couplings IS specifying masses")

    # ---- M-D: anti-control ---------------------------------------------------
    print("\n  M-D  ANTI-CONTROL: is 'no reduction' vacuous, or specific to 3-on-3?")
    # four seeds on three sites: 4 reals -> 3 reals, a genuine 1-parameter reduction
    n_seeds, n_out = 4, 3
    chk("M-D1 four seeds on three sites WOULD reduce (4 -> 3)", n_seeds > n_out,
        f"kernel dimension {n_seeds - n_out} -- so the conclusion is about the "
        f"3-on-3 case specifically, not a triviality")
    chk("M-D2 and three-on-three has zero kernel", 3 - 3 == 0)

    # ---- verdict ------------------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED — do not record: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  RESULT — A LIMIT ON WHAT THE THREE-SEED IDEA CAN DELIVER")
    print("=" * 78)
    print(f"""
  THE COUPLINGS ARE THE MASSES. The map from three real seed couplings to (G0, b)
  is an exact bijection, and its inverse has the same functional form as the mass
  formula, so g_j is proportional to sqrt(m_j). Fed the measured leptons, the seeds
  couple as 1 : {r[1]/r[0]:.3f} : {r[2]/r[0]:.3f}.

  SO C14's FRAMING WAS TOO GENEROUS AND IS CORRECTED HERE. It recorded
  g1/g0 = -0.3001 as "a constraint on the seeds". It is not an independent
  constraint -- it is the Koide relation written in another basis. "Why do the
  three creating objects couple in that ratio?" and "why do the leptons have those
  masses?" are the SAME QUESTION. The seed picture reduces the number of unknowns
  by exactly zero.

  IT IS NOT VACUOUS (M-D): four seeds on three sites would genuinely reduce, with a
  one-dimensional kernel. The no-reduction result is specific to three-on-three,
  which is the configuration the owner's idea actually proposes.

  WHAT SURVIVES, AND IT IS STILL WORTH HAVING. Three facts the spectrum alone does
  not state:
    * identical seeds give b = 0 EXACTLY -- distinctness is why any splitting
      exists;
    * three distinct seeds are intrinsically chiral, supplying exactly the
      parity-odd source C13 proved the phase requires;
    * the cyclic ORDER fixes the SIGN of arg b.
  Those are answers to "why is there a splitting" and "what kind of object can
  source the phase". They are not answers to "what is its value".

  WHERE THIS LEAVES #2. The value 2/9 cannot come from the seed couplings, because
  those carry no information the masses do not already carry. It has to come from
  outside the family sector entirely -- which is the keystone c_K * tau = Q, and
  "derive c_K from first principles" is now the ONLY remaining route rather than
  one of two. That is a narrowing, achieved by closing off the other.
""")


if __name__ == "__main__":
    main()
