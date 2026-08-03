#!/usr/bin/env python3
"""
Debt 1 of the gr-qc paper, paid: str[k1] computed independently from Visser's published
coefficients. **The corpus's claim is CONFIRMED.** One statement of it needs correcting.

--------------------------------------------------------------------------------------
THE SIGN QUESTION, WHICH WAS THE WHOLE RESULT.

Visser 2002 (gr-qc/0204062) Table 1 lists, for a Weyl spinor, k1 = -1/6. The corpus needs
Weyl fermions to contribute +1/6 for the balance to close. That looked like a double-counted
minus sign, which would have destroyed the claim.

It is not. Visser's table caption reads:

    "Total contributions to the k_i summed over spin states for low-spin particles.
     (Here k0 = tr[I] counts the number of spin states.) FOR SUPERMULTIPLETS the net
     value, INCLUDING the effect of the minus sign for fermions, is reported."

So the fermion minus is folded in **only for the supermultiplet rows**. The elementary rows
(Weyl, Dirac) are plain traces -- as k0 = 2 and 4, both positive counts, confirms -- and the
supertrace sign is applied on top:

    str[X] = sum_bosons X  -  sum_fermions X

A Weyl spinor therefore contributes -(-1/6) = **+1/6**. The corpus's sign is right.

TWO INDEPENDENT CHECKS that this is the intended convention, both from Visser's own table:
  * Dirac = 2 x Weyl:            -1/3 = 2 x (-1/6).
  * Massive vector = massless vector + minimally coupled scalar, which Visser states in
    words: -1/2 = -2/3 + 1/6. This only works if bosons enter with their listed sign.

--------------------------------------------------------------------------------------
THE COUNT, AND WHAT IT GIVES

Weyl fermions carry +1/6 each, massless vectors -2/3 each, real scalars (1/6 - xi).

    SM + 3 nu_R:  48 Weyl x (+1/6) = +8 ;  12 vectors x (-2/3) = -8  ->  str[k1] = 0
    SM alone:     45 Weyl x (+1/6) = +7.5;  same -8               ->  str[k1] = -1/2

with the Higgs (4 real scalars) contributing 4(1/6 - xi_H), which vanishes at xi_H = 1/6.

The underlying identity is exactly the corpus's N_1/2 = 4 N_1: **48 = 4 x 12**, an integer
identity with no slack.

*** THE ONE CORRECTION. *** The corpus states "str[k1] = -3" for the Standard Model alone.
In Visser's normalisation it is **-1/2**. The -3 is the deficit counted in WEYL SPINORS
(45 - 48 = -3), which is a different unit. Both describe the same fact and the -3 is the more
transparent way to say it, but a referee checking against Visser's Table 1 will compute -1/2
and think the paper cannot add up. **The paper must quote both, or quote -1/2 and give the
Weyl deficit separately.**

PRE-STATED CONTROLS:
  S-A  Visser's internal consistency: Dirac = 2 x Weyl.
  S-B  Visser's internal consistency: massive vector = massless vector + minimal scalar.
       This is the control that PINS the sign convention, because Visser states it in words.
  S-C  the Standard Model Weyl count, per generation and total.
  S-D  str[k1] for SM + 3 nu_R must be exactly zero.
  S-E  str[k1] for SM alone, in Visser's units.
  S-F  the integer identity N_1/2 = 4 N_1.
  S-G  the Higgs sector vanishes iff xi_H = 1/6.
  S-H  ANTI-CONTROL: the two forward exclusions must actually break the balance, or the
       paper has no forward content.
  S-I  ANTI-CONTROL: if the fermion minus were double-counted the total would be -16, far
       from zero -- so the convention is doing real work and is not a free choice.
"""

from fractions import Fraction as F

_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


# Visser 2002, Table 1 -- k1 as PRINTED (plain traces for the elementary rows)
K1_PRINTED = {
    'scalar_minimal':   F(1, 6),
    'scalar_conformal': F(0),
    'weyl':             F(-1, 6),
    'dirac':            F(-1, 3),
    'vector_massless':  F(-2, 3),
    'vector_massive':   F(-1, 2),
}
# supertrace contribution: bosons as printed, fermions with the sign flipped
BOSONS = {'scalar_minimal', 'scalar_conformal', 'vector_massless', 'vector_massive'}
FERMIONS = {'weyl', 'dirac'}


def contrib(kind, n=1):
    k = K1_PRINTED[kind]
    return n * (k if kind in BOSONS else -k)


def main():
    print("=" * 78)
    print("  str[k1] FOR THE STANDARD MODEL, FROM VISSER'S PUBLISHED COEFFICIENTS")
    print("=" * 78)

    # ---- S-A ---------------------------------------------------------------
    print("\n  S-A  Visser internal check: Dirac = 2 x Weyl")
    print(f"       Dirac {K1_PRINTED['dirac']}   2 x Weyl {2*K1_PRINTED['weyl']}")
    chk("S-A1 holds", K1_PRINTED['dirac'] == 2 * K1_PRINTED['weyl'])

    # ---- S-B  the convention-pinning control -------------------------------
    print("\n  S-B  Visser internal check: massive vector = massless vector + minimal scalar")
    print( "       (Visser states this in words: 'k1 for a massive vector is calculated by")
    print( "        adding k1 for a minimally coupled scalar to k1 for a massless vector')")
    lhs = K1_PRINTED['vector_massive']
    rhs = K1_PRINTED['vector_massless'] + K1_PRINTED['scalar_minimal']
    print(f"       {lhs} =?= {K1_PRINTED['vector_massless']} + {K1_PRINTED['scalar_minimal']} = {rhs}")
    chk("S-B1 holds, so bosons enter with their PRINTED sign", lhs == rhs,
        "this pins the convention and is not a free choice")

    # ---- S-C ---------------------------------------------------------------
    print("\n  S-C  Standard Model Weyl content")
    per_gen = {'Q (3x2)': 6, 'u^c (3)': 3, 'd^c (3)': 3, 'L (2)': 2, 'e^c (1)': 1}
    n_gen = sum(per_gen.values())
    for k, v in per_gen.items():
        print(f"       {k:12s} {v}")
    print(f"       per generation = {n_gen};  x 3 generations = {3*n_gen}")
    chk("S-C1 15 Weyl per generation", n_gen == 15)
    chk("S-C2 45 Weyl in the Standard Model", 3 * n_gen == 45)
    N_WEYL_SM = 3 * n_gen
    N_WEYL_SM_NUR = N_WEYL_SM + 3
    chk("S-C3 48 with three right-handed neutrinos", N_WEYL_SM_NUR == 48)

    # ---- S-D ---------------------------------------------------------------
    print("\n  S-D  str[k1] for SM + 3 nu_R  (gauge bosons + fermions)")
    N_VEC = 8 + 3 + 1
    f_part = contrib('weyl', N_WEYL_SM_NUR)
    v_part = contrib('vector_massless', N_VEC)
    total = f_part + v_part
    print(f"       {N_WEYL_SM_NUR} Weyl  x (+1/6) = {f_part}")
    print(f"       {N_VEC} massless vectors x (-2/3) = {v_part}")
    print(f"       sum = {total}")
    chk("S-D1 exactly zero", total == 0, f"{total}")

    # ---- S-E ---------------------------------------------------------------
    print("\n  S-E  str[k1] for the Standard Model alone")
    tot_sm = contrib('weyl', N_WEYL_SM) + v_part
    print(f"       {N_WEYL_SM} Weyl x (+1/6) = {contrib('weyl', N_WEYL_SM)};  vectors {v_part}")
    print(f"       sum = {tot_sm}  in Visser's units")
    print(f"       the corpus quotes -3, which is the WEYL DEFICIT: {N_WEYL_SM} - 48 = {N_WEYL_SM-48}")
    chk("S-E1 str[k1] = -1/2 in Visser's units", tot_sm == F(-1, 2), f"{tot_sm}")
    chk("S-E2 and the Weyl deficit is -3", N_WEYL_SM - 48 == -3,
        "same fact, different unit -- the paper must not conflate them")
    chk("S-E3 the two are related by 1/6", F(N_WEYL_SM - 48, 6) == tot_sm,
        f"(-3)/6 = {F(-3,6)}")

    # ---- S-F ---------------------------------------------------------------
    print("\n  S-F  the integer identity")
    print(f"       N_(1/2) = {N_WEYL_SM_NUR},  4 x N_1 = 4 x {N_VEC} = {4*N_VEC}")
    chk("S-F1 N_(1/2) = 4 N_1 exactly", N_WEYL_SM_NUR == 4 * N_VEC,
        "an integer identity with no slack")

    # ---- S-G ---------------------------------------------------------------
    print("\n  S-G  the Higgs sector")
    for xi, lab in ((F(0), 'minimal'), (F(1, 6), 'conformal')):
        h = 4 * (F(1, 6) - xi)
        print(f"       xi_H = {xi} ({lab:9s}): 4(1/6 - xi) = {h}")
    chk("S-G1 vanishes iff xi_H = 1/6", 4 * (F(1, 6) - F(1, 6)) == 0
        and 4 * (F(1, 6) - F(0)) != 0,
        "so the zero is CONDITIONAL on conformal Higgs coupling")

    # ---- S-H: anti-control -------------------------------------------------
    print("\n  S-H  ANTI-CONTROL: do the forward exclusions actually break the balance?")
    d_sterile = contrib('weyl', 1)
    d_fourth = contrib('weyl', 16)          # a full 4th generation: 15 + 1 nu_R
    print(f"       one extra sterile Weyl : str[k1] -> {d_sterile}  (was 0)")
    print(f"       a fourth generation    : str[k1] -> {d_fourth}  (was 0)")
    chk("S-H1 a light sterile neutrino breaks it", d_sterile != 0, f"{d_sterile}")
    chk("S-H2 a fourth generation breaks it", d_fourth != 0, f"{d_fourth}")
    chk("S-H3 so the paper has real forward content", d_sterile != 0 and d_fourth != 0)

    # ---- S-I: anti-control -------------------------------------------------
    print("\n  S-I  ANTI-CONTROL: what if the fermion minus HAD been double-counted?")
    wrong = N_WEYL_SM_NUR * K1_PRINTED['weyl'] + v_part
    print(f"       taking Weyl as -1/6 too: {wrong}")
    chk("S-I1 it would give -16, nowhere near zero", wrong == -16, f"{wrong}")
    chk("S-I2 so the convention is load-bearing and S-B settles it", wrong != total)

    # ---- verdict -----------------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  RESULT — THE CLAIM IS CONFIRMED, WITH ONE UNIT CORRECTION")
    print("=" * 78)
    print("""
  str[k1] = 0 holds exactly for the Standard Model plus three right-handed neutrinos, with a
  conformally coupled Higgs. The balance is the integer identity N_(1/2) = 4 N_1, i.e.
  48 = 4 x 12, with no slack anywhere in it.

  The sign convention -- the one thing that could have destroyed the result -- is settled by
  Visser's own table rather than by assumption. His caption folds the fermion minus in only
  for the supermultiplet rows, and his stated additivity for massive vectors
  (-1/2 = -2/3 + 1/6) only works if bosons carry their printed sign. Had the minus been
  double-counted the total would be -16, so the convention is load-bearing and it checks.

  ONE CORRECTION THE PAPER MUST CARRY. The corpus writes "str[k1] = -3" for the Standard
  Model alone. In Visser's normalisation it is **-1/2**; the -3 is the deficit counted in
  Weyl spinors (45 - 48), related by the 1/6 per Weyl. Both are true and the -3 is the more
  legible statement, but a referee checking Table 1 will get -1/2 and conclude the arithmetic
  is wrong. Quote both, or quote -1/2 and give the Weyl deficit alongside.

  The forward content survives: one extra sterile Weyl shifts the balance by +1/6 and a
  fourth generation by +8/3, so both are genuinely excluded rather than merely disfavoured.
""")


if __name__ == "__main__":
    main()
