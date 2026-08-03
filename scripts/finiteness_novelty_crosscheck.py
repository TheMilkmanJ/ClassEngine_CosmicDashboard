#!/usr/bin/env python3
"""
#79: the novelty check's second pass -- does a published gravitational condition
already force 48 Weyl fermions (3 generations incl. nu_R)?

Two DIFFERENT conditions are compared.  Neither is assumed correct; both are
evaluated from their own stated coefficients.

  (1) THE CORPUS: Pauli/Sakharov finiteness on the induced Newton constant,
      str[k1] = 0.  Heat-kernel a1 level (the R-coefficient).
      Weights: +1 per Weyl fermion, -4 per gauge boson.

  (2) NAVARRO-SALAS 2024 (CQG, arXiv:2403.13201): exact conformal symmetry,
      i.e. BOTH trace-anomaly coefficients vanish.  Heat-kernel a2 level
      (Weyl^2 and Euler).  Eq. (3.10):
          a = [N0 + (11/2) N_half + 62 N1 - 28 N_xi] / (360 (4pi)^2) = 0
          c = [N0 +      3 N_half + 12 N1 -  8 N_xi] / (120 (4pi)^2) = 0

Pre-stated control: the SM roster without right-handed neutrinos is 45 Weyl
fermions (3 x 15).  If either condition returns 45, or returns 48 only after a
fitted input, the comparison is worthless.  Stated before solving.
"""

from fractions import Fraction as F

N_GEN = 3
WEYL_PER_GEN_WITH_NUR = 16  # Q6 + uR3 + dR3 + L2 + eR1 + nuR1
WEYL_PER_GEN_NO_NUR = 15
N_GAUGE_SM = 12  # 8 gluons + 3 weak + 1 hypercharge


def corpus_str_k1(n_gen, weyl_per_gen=WEYL_PER_GEN_WITH_NUR, n_gauge=N_GAUGE_SM):
    """str[k1] = (+1) * Weyl - 4 * gauge."""
    return weyl_per_gen * n_gen - 4 * n_gauge


def navarro_salas_solve(n1=N_GAUGE_SM, n0=0):
    """Solve a = c = 0 for (N_half, N_xi) at fixed N1, N0.  Exact rationals."""
    # c: N0 + 3H + 12*N1 - 8X = 0   ->  X = (N0 + 3H + 12 N1)/8
    # a: N0 + (11/2)H + 62*N1 - 28X = 0
    # substitute:
    #   N0 + (11/2)H + 62 N1 - 28(N0 + 3H + 12 N1)/8 = 0
    #   N0 + (11/2)H + 62 N1 - (7/2)(N0 + 3H + 12 N1) = 0
    #   N0 - (7/2)N0 + (11/2 - 21/2)H + 62 N1 - 42 N1 = 0
    #   -(5/2)N0 - 5H + 20 N1 = 0  ->  H = 4 N1 - N0/2
    H = F(4) * n1 - F(n0, 2)
    X = (F(n0) + 3 * H + 12 * F(n1)) / 8
    return H, X


def main():
    print("=" * 76)
    print("  #79 second pass: two gravitational conditions, one generation count")
    print("=" * 76)

    print("\n  CONTROL (stated before solving):")
    print(f"    SM without nu_R = 3 x 15 = {N_GEN*WEYL_PER_GEN_NO_NUR} Weyl fermions")
    print(f"    SM with    nu_R = 3 x 16 = {N_GEN*WEYL_PER_GEN_WITH_NUR} Weyl fermions")
    print("    A condition that returns 45, or needs a fitted input to reach 48,")
    print("    fails this comparison.")

    # ---- (1) the corpus's condition -------------------------------------
    print("\n  (1) CORPUS -- Pauli/Sakharov finiteness, str[k1] = 0  (heat-kernel a1)")
    print(f"      {'N_gen':>6} {'Weyl':>6} {'gauge x -4':>12} {'str[k1]':>9}")
    root = None
    for g in (1, 2, 3, 4, 5):
        s = corpus_str_k1(g)
        if s == 0:
            root = g
        print(f"      {g:6d} {WEYL_PER_GEN_WITH_NUR*g:6d} {-4*N_GAUGE_SM:12d} {s:9d}"
              f"{'   <-- root' if s == 0 else ''}")
    print(f"      => N_gen = {root}, i.e. {WEYL_PER_GEN_WITH_NUR*root} Weyl fermions")

    # without nu_R, for contrast
    s15 = corpus_str_k1(3, WEYL_PER_GEN_NO_NUR)
    print(f"      control: same condition on the 15-Weyl roster gives str[k1] = {s15}"
          f" (nonzero) -> nu_R required")

    # ---- (2) Navarro-Salas ----------------------------------------------
    print("\n  (2) NAVARRO-SALAS 2024 -- exact conformal symmetry, a = c = 0  (heat-kernel a2)")
    H, X = navarro_salas_solve(n1=N_GAUGE_SM, n0=0)
    print(f"      with N1 = {N_GAUGE_SM} (SM gauge bosons) and N0 = 0 (no NON-conformal scalars):")
    print(f"        N_half = {H}   N_xi = {X}")
    # verify both equations exactly
    a_num = F(0) + F(11, 2) * H + 62 * F(N_GAUGE_SM) - 28 * X
    c_num = F(0) + 3 * H + 12 * F(N_GAUGE_SM) - 8 * X
    print(f"      verify:  a-bracket = {a_num}   c-bracket = {c_num}   "
          f"{'both vanish: PASS' if a_num == 0 and c_num == 0 else 'FAIL'}")
    print(f"      => {H} Weyl fermions = {int(H)//WEYL_PER_GEN_WITH_NUR} generations "
          f"of 16, i.e. 3 generations INCLUDING right-handed neutrinos")

    # general N1 dependence -- is 48 an accident of N1 = 12?
    print("\n      the general solution is N_half = 4*N1 - N0/2, so the 48 tracks the")
    print("      gauge-boson count directly:")
    print(f"        {'N1':>4} {'N_half':>8}")
    for n1 in (8, 10, 12, 14):
        h, _ = navarro_salas_solve(n1=n1, n0=0)
        print(f"        {n1:4d} {str(h):>8}{'   <-- SM' if n1 == 12 else ''}")

    # ---- the comparison --------------------------------------------------
    print("\n" + "=" * 76)
    print("  THE COMPARISON")
    print("=" * 76)
    print("""
  Both conditions land on 48 Weyl fermions = 3 generations WITH right-handed
  neutrinos.  They are NOT the same condition:

    corpus         heat-kernel a1 (the R-coefficient / induced Newton constant)
                   weights  +1 per Weyl,  -4 per gauge boson
                   balance  16*N_gen - 4*12 = 0

    Navarro-Salas  heat-kernel a2 (Weyl^2 and Euler -- the trace anomaly)
                   weights  11/2 and 3 per Weyl, 62 and 12 per gauge boson,
                            -28 and -8 per zero-dimension scalar
                   balance  N_half = 4*N1 - N0/2

  Different orders of the heat-kernel expansion, different coefficients, same
  root.  Note both land on 48 by balancing fermions against GAUGE BOSONS with
  the gauge count fixed at 12 -- the corpus at -4 each, Navarro-Salas at 4 each
  in the solved form.  That the two agree is a fact to record, not a proof that
  either is right, and NOT evidence they are independent: they are two
  coefficients of one expansion over one roster.

  NOVELTY READING: the corpus's HEADLINE -- a gravitational finiteness/anomaly
  requirement forcing exactly 3 generations and requiring right-handed
  neutrinos, at 48 Weyl fermions -- is PUBLISHED (Navarro-Salas, CQG 2024).
  The corpus's SPECIFIC condition (str[k1] = 0 at the a1 level) is a different
  equation and its SM+3nu_R evaluation still did not surface.  The honest
  statement is therefore weaker than 'novel' and stronger than the previous
  'partial negative': the CONCLUSION has prior art; the ROUTE may not.
""")
    print("=" * 76)


if __name__ == "__main__":
    main()
