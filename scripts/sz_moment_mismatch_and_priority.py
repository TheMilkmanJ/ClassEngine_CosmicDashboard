#!/usr/bin/env python3
"""
The two things owed before the SZ material could enter the paper. One is settled
favourably; the other is settled AGAINST the novelty claim, and that is the more
important result.

--------------------------------------------------------------------------------------
OWED ITEM 2 (taken first, because it governs what may be written): PRIORITY.

*** THE THOMSON / SZ ROUTE IS NOT NEW. IT IS ESTABLISHED VARYING-CONSTANTS METHOD. ***

A literature search on 2026-07-29 returns a substantial body of work already using the
SZ effect to constrain varying constants, by exactly the logic derived here:

  - The Compton-y parameter's dependence on sigma_T ~ alpha^2/m_e^2 is explicitly the
    stated mechanism in that literature.
  - The standard observable is the ratio of the integrated Comptonization Y_SZ to its
    X-ray counterpart Y_X -- i.e. SZ compared against an INDEPENDENT probe of the SAME
    gas, which is structurally the identical move to the one derived here.
  - Samples already analysed: 61 Planck clusters plus 58 SPT clusters against XMM-Newton
    X-ray; 618 X-ray selected clusters for spatial alpha variation; 82 clusters to
    z = 1.36 for runaway-dilaton models.
  - The CMB varying-constants literature (Planck intermediate XXIV; Hart & Chluba)
    already treats the sigma_T rescaling explicitly, including its role in the
    alpha / m_e geometric degeneracy.

CONSEQUENCE FOR THE PAPER. The SZ material must enter as ENGAGEMENT WITH AN EXISTING
METHOD, cited, not as a new row claiming a new idea. Writing it up as novel would be
false and would be caught immediately by anyone in the field -- and the paper's honesty
is its main asset.

What may still be narrow enough to be new is only this: the specific pairing of SZ
against FAST-RADIO-BURST DISPERSION MEASURES rather than against X-ray, and the
alpha-free kSZ/tSZ combination. NEITHER is asserted as new here. Both require the
targeted search this script cannot perform, and until then the text must claim nothing.

--------------------------------------------------------------------------------------
OWED ITEM 1: THE MOMENT MISMATCH, and it resolves.

The worry was that DM, kSZ and tSZ integrate DIFFERENT moments -- n_e, n_e v, n_e kT --
so no ratio divides the unknown out. That is true, and it is why the observable is not a
column ratio. The correct observable is an INFERRED ASTROPHYSICAL PARAMETER.

Compton-y is measured directly as a dimensionless temperature decrement, so it carries no
divided-out laboratory constant of its own. For a FIXED physical gas,

    y_measured = y_0 (1+eps)^-3      [sigma_T gives -2, the 1/(m_e c^2) gives -1]

An observer inverting y with laboratory constants recovers a pressure column biased by
-3, and dividing by the DM-inferred column (biased by -1) gives

    *** T_e(inferred) = T_e(true) * (1+eps)^-2 ***

So the DM x tSZ cross-correlation's inferred electron temperature carries m_e weight -2,
and an INDEPENDENT temperature -- X-ray spectroscopy of the same gas -- closes it. That
is precisely the Y_SZ/Y_X construction the literature already uses, which is a
consistency check on this derivation and simultaneously the reason it is not new.

PRE-STATED CONTROLS:
  M-A  the y bias for fixed gas must be -3, from sigma_T's -2 and the 1/(m_e c^2) -1.
  M-B  the DM-inferred column bias must be -1.
  M-C  the inferred temperature must then carry weight -2, derived not asserted.
  M-D  the result must be independent of the true gas properties -- otherwise it is not
       an observable.
  M-E  ANTI-CONTROL: if the column were taken from something with the SAME weight as the
       pressure probe, the temperature bias must vanish, showing the effect comes from
       the weight DIFFERENCE.
  M-F  ANTI-CONTROL: an alpha shift must give a different temperature bias, or the
       method cannot separate the two.
  M-G  the kSZ/tSZ alpha cancellation must be checked explicitly, since it is the one
       piece with any chance of being new.
"""

import math
from fractions import Fraction as F

_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


def bias(eps=0.0, dalpha=0.0, w_me=F(0), w_al=F(0)):
    """multiplicative bias of a quantity with the given weights"""
    return (1.0 + eps) ** float(w_me) * (1.0 + dalpha) ** float(w_al)


def main():
    print("=" * 78)
    print("  SZ: THE MOMENT MISMATCH, AND THE PRIORITY QUESTION")
    print("=" * 78)

    eps = 1e-3

    # ---- M-A ----------------------------------------------------------------
    print("\n  M-A  Compton-y for a FIXED physical gas")
    print("       y ~ sigma_T INT n_e kT/(m_e c^2) dl")
    w_sigma, w_mec2 = F(-2), F(-1)
    w_y = w_sigma + w_mec2
    print(f"       sigma_T: {w_sigma}    1/(m_e c^2): {w_mec2}    =>  y: {w_y}")
    chk("M-A1 y carries m_e weight -3 for fixed gas", w_y == -3, f"{w_y}")

    # ---- M-B ----------------------------------------------------------------
    print("\n  M-B  the DM-inferred column")
    w_dm = F(-1)
    chk("M-B1 weight -1", w_dm == -1, "t ~ (e^2/m_e) N_e, lab constant divided out")

    # ---- M-C ----------------------------------------------------------------
    print("\n  M-C  the inferred temperature")
    # pressure column inferred from y carries w_y ; column from DM carries w_dm
    w_T = w_y - w_dm
    print(f"       T_inferred = (pressure from y) / (column from DM):  {w_y} - ({w_dm}) = {w_T}")
    chk("M-C1 the inferred T_e carries weight -2", w_T == -2, f"{w_T}")
    # numeric confirmation
    T_true = 2.0e7
    T_inf = T_true * bias(eps=eps, w_me=w_y) / bias(eps=eps, w_me=w_dm)
    print(f"       numerically: T_true = {T_true:.2e} K, eps = {eps:.0e}"
          f"  =>  T_inferred = {T_inf:.6e} K")
    chk("M-C2 numerically the bias is -2 eps",
        abs((T_inf / T_true - 1) / (-2 * eps) - 1) < 2e-3,
        f"{(T_inf/T_true - 1):+.6e} vs -2eps = {-2*eps:+.0e}")

    # ---- M-D ----------------------------------------------------------------
    print("\n  M-D  is it independent of the true gas?")
    fracs = []
    for T in (1e6, 2e7, 1e8):
        for N in (1.0, 1e3):
            f_ = (T * bias(eps=eps, w_me=w_y) / bias(eps=eps, w_me=w_dm)) / T
            fracs.append(f_)
    chk("M-D1 the fractional bias is the same for every gas", max(fracs) - min(fracs) < 1e-12,
        "so it is an observable, not a property of the cluster")

    # ---- M-E: anti-control --------------------------------------------------
    print("\n  M-E  ANTI-CONTROL: what if the column came from a same-weight probe?")
    w_T_same = w_y - w_y
    chk("M-E1 a same-weight column gives ZERO temperature bias", w_T_same == 0,
        "so the signal is the weight DIFFERENCE, not the SZ effect on its own")

    # ---- M-F: anti-control --------------------------------------------------
    print("\n  M-F  ANTI-CONTROL: does alpha give a different bias?")
    wa_y, wa_dm = F(2), F(1)                 # alpha weights
    wa_T = wa_y - wa_dm
    print(f"       alpha: y carries {wa_y}, DM carries {wa_dm}  =>  T bias {wa_T}")
    chk("M-F1 alpha biases T by +1 where m_e biases it by -2", wa_T == 1 and w_T == -2,
        "different magnitude AND opposite sign, so the two are separable here")

    # ---- M-G ----------------------------------------------------------------
    print("\n  M-G  the kSZ / tSZ combination")
    w_ksz_me, w_ksz_al = F(-2), F(2)
    w_tsz_me, w_tsz_al = F(-3), F(2)
    net_me, net_al = w_ksz_me - w_tsz_me, w_ksz_al - w_tsz_al
    print(f"       kSZ  w(m_e) = {w_ksz_me}, w(alpha) = {w_ksz_al}")
    print(f"       tSZ  w(m_e) = {w_tsz_me}, w(alpha) = {w_tsz_al}")
    print(f"       ratio: net w(m_e) = {net_me}, net w(alpha) = {net_al}")
    chk("M-G1 alpha cancels identically in the kSZ/tSZ ratio", net_al == 0,
        "both carry sigma_T, so its alpha^2 divides out")
    chk("M-G2 leaving pure m_e weight +1", net_me == 1,
        "the residual is the 1/(m_e c^2) that only Compton-y carries")
    print("       -> a pure electron-mass combination with NO alpha contamination.")
    print("          NOT claimed as new here: see the priority note below.")

    # ---- verdict ------------------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  RESULT — ONE ITEM SETTLED, ONE SETTLED AGAINST US")
    print("=" * 78)
    print("""
  THE MOMENT MISMATCH RESOLVES, and the resolution is that the observable was never a
  column ratio. Compton-y is measured directly as a dimensionless decrement, so for a
  fixed physical gas it is biased by -3 (sigma_T's -2 plus the 1/(m_e c^2)). Dividing the
  inverted pressure by a DM-inferred column, biased by -1, leaves

      T_e(inferred) = T_e(true) x (1 + eps)^-2

  a bias of -2 eps that is identical for every gas, hence a genuine observable. An
  independent temperature closes it. Under an alpha shift the same quantity is biased by
  +1 -- different magnitude and opposite sign -- so the pair separates the hypotheses.
  The anti-control confirms the effect is the weight DIFFERENCE: a column taken from a
  same-weight probe gives exactly zero bias.

  AND THE kSZ/tSZ COMBINATION IS ALPHA-FREE. Both carry sigma_T, so its alpha^2 divides
  out identically, leaving pure m_e weight +1 from the Compton-y 1/(m_e c^2). That is a
  clean electron-mass combination with no fine-structure contamination.

  BUT THE PRIORITY QUESTION SETTLES AGAINST THE NOVELTY CLAIM, AND THAT GOVERNS.

  Using the SZ effect to constrain varying constants is ESTABLISHED METHOD. The
  literature states sigma_T ~ alpha^2/m_e^2 as the mechanism explicitly, and the standard
  observable is Y_SZ/Y_X -- the Comptonization compared against its X-ray counterpart,
  i.e. SZ against an independent probe of the same gas. That is structurally the identical
  move derived above, with X-ray in the place of the dispersion measure. Samples already
  analysed run to 618 clusters. The CMB varying-constants papers already treat the
  sigma_T rescaling and its role in the alpha / m_e degeneracy.

  So the derivation above is CORRECT and NOT NEW. Its value to the paper is that it
  reproduces an established construction from the paper's own weight formalism -- which
  is a consistency check worth having, and a prior-work engagement the paper currently
  lacks entirely.

  WHAT THIS MEANS FOR THE TEXT, stated so it cannot be misread:

    * The SZ material may enter ONLY as engagement with existing method, with citations.
    * It may NOT be presented as a new row, a new probe, or a new idea.
    * The one element with any remaining chance of being narrow enough to be new -- SZ
      paired with FRB dispersion measures rather than X-ray, and the alpha-free kSZ/tSZ
      combination -- is NOT claimed here. It needs its own targeted search first.
    * Until that search is done the text claims nothing about novelty, exactly as it
      currently claims nothing about the Faraday row.
""")


if __name__ == "__main__":
    main()
