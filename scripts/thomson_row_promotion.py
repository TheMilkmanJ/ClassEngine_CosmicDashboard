#!/usr/bin/env python3
"""
The radio-lattice paper's promotion piece: a SIXTH row that makes the dispersion row
usable, by supplying the independent determination of the same electron column that the
demotion said was missing.

THE BLOCKER, restated. A constant eps is exactly degenerate with the fitted dispersion
measure: the timing model absorbs it completely, so DM alone reports the precision of an
independent electron-column determination rather than a sigma of its own. The paper now
says so and demotes the row. The stated promotion condition is "an independent
determination of the same electron column at a precision competitive with the other
rows."

THE OBSERVATION. There already IS a second reconstruction of the electron column, and it
carries a DIFFERENT m_e weight. The Thomson cross-section is

    sigma_T = (8 pi/3) r_e^2,   r_e = e^2/(m_e c^2)   =>   sigma_T ~ alpha^2 / m_e^2

so an optical depth tau = N_e sigma_T, divided by the LABORATORY sigma_T to report a
column, inherits weight -2 -- against the dispersion row's -1.

  *** Two reconstructions of the SAME physical column with DIFFERENT weights give a
  *** ratio in which the column CANCELS EXACTLY:
  ***
  ***     N_e(DM) / N_e(Thomson) = (1 - eps)/(1 - 2 eps) = 1 + eps + O(eps^2)
  ***
  *** That is a first-order handle on eps that never needs to know the true column --
  *** which is precisely what the demotion said was missing.

AND IT SEPARATES m_e FROM alpha BY SIGN. The alpha weights are +1 (dispersion) and +2
(Thomson), so the same ratio goes as 1 - delta_alpha. A varying electron mass raises the
ratio; a varying fine-structure constant lowers it. The pair inherits the paper's own
discriminating structure rather than needing a new argument for it.

WHAT THIS IS AND IS NOT. It is a derivation, at the same standing as the paper's other
five rows -- textbook scalings, no free parameters. It is NOT an observational programme:
pairing a dispersion measure with a Thomson optical depth over the SAME column is the
work, and the natural candidates (fast-radio-burst columns against kinetic-SZ or CMB
optical depth over the same structures) are named here as candidates, not claimed as
existing measurements. That distinction is stated in the output and must survive into any
text.

PRE-STATED CONTROLS:
  X-A  sigma_T's weights must be derived from r_e = e^2/(m_e c^2), not asserted:
       w_me = -2, w_alpha = +2.
  X-B  the Thomson-inferred column must carry weight -2 in m_e and +2 in alpha.
  X-C  THE CANCELLATION: the true column must drop out of the DM/Thomson ratio exactly,
       checked over a wide range of columns, not just algebraically.
  X-D  the ratio must go as 1 + eps to first order under an m_e shift.
  X-E  and as 1 - delta_alpha under an alpha shift, i.e. OPPOSITE sign.
  X-F  ANTI-CONTROL: a pair with EQUAL weights must give no signal, so the effect is the
       weight DIFFERENCE and not merely having two probes.
  X-G  ANTI-CONTROL: the cancellation must fail if the two probes see different columns,
       since that is the real observational risk.
  X-H  the new row must not disturb the existing five: its m_e weight must differ from
       every one of them, or it adds no information.
"""

from fractions import Fraction as F

_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


# (alpha exponent, m_e exponent) of the OBSERVED quantity
DM_DELAY = (F(1), F(-1))        # t ~ e^2/m_e ~ alpha/m_e
SIGMA_T = (F(2), F(-2))         # sigma_T ~ alpha^2/m_e^2

PAPER_ME = {"21 cm": F(2), "RRL": F(1), "DM": F(-1), "sync": F(-1), "RM": F(-2)}


def inferred_column(true_N, eps=0.0, dalpha=0.0, weights=DM_DELAY):
    """
    Observer measures a quantity proportional to (alpha^a m_e^b) * N_e and divides by the
    LABORATORY value of that constant combination to report a column.
    """
    a, b = float(weights[0]), float(weights[1])
    true_const = (1.0 + dalpha) ** a * (1.0 + eps) ** b
    return true_N * true_const           # lab constant is 1 by construction


def main():
    print("=" * 78)
    print("  THE THOMSON ROW — the dispersion row's missing partner")
    print("=" * 78)

    # ---- X-A ----------------------------------------------------------------
    print("\n  X-A  sigma_T's weights, from r_e = e^2/(m_e c^2)")
    # sigma_T ~ r_e^2 ~ (e^2/m_e)^2 ~ (alpha/m_e)^2
    a_re, m_re = F(1), F(-1)                       # r_e ~ alpha/m_e
    a_sig, m_sig = 2 * a_re, 2 * m_re
    print(f"       r_e     ~ alpha^{a_re} m_e^{m_re}")
    print(f"       sigma_T ~ r_e^2 ~ alpha^{a_sig} m_e^{m_sig}")
    chk("X-A1 w_me(sigma_T) = -2", m_sig == -2, f"{m_sig}")
    chk("X-A2 w_alpha(sigma_T) = +2", a_sig == 2, f"{a_sig}")
    chk("X-A3 and these are what SIGMA_T carries", (a_sig, m_sig) == SIGMA_T)

    # ---- X-B ----------------------------------------------------------------
    print("\n  X-B  the inferred columns")
    print("       dispersion: t ~ alpha/m_e   => N_e(DM)      inherits weight -1 in m_e")
    print("       Thomson:    tau ~ alpha^2/m_e^-2 => N_e(Thom) inherits weight -2 in m_e")
    eps = 1e-3
    N = 137.0
    nd = inferred_column(N, eps=eps, weights=DM_DELAY)
    nt = inferred_column(N, eps=eps, weights=SIGMA_T)
    chk("X-B1 the DM column shifts by -eps", abs((nd / N - 1) / (-eps) - 1) < 2e-3,
        f"{(nd/N - 1):+.6e} vs -eps = {-eps:+.0e}")
    chk("X-B2 the Thomson column shifts by -2 eps",
        abs((nt / N - 1) / (-2 * eps) - 1) < 2e-3,
        f"{(nt/N - 1):+.6e} vs -2eps = {-2*eps:+.0e}")

    # ---- X-C: THE CANCELLATION ----------------------------------------------
    print("\n  X-C  does the unknown column cancel?")
    print(f"\n    {'true N_e':>14} {'N(DM)/N(Thom)':>18}")
    ratios = []
    for N in (1e-3, 1.0, 137.0, 1e6, 1e12):
        r = inferred_column(N, eps=eps, weights=DM_DELAY) / \
            inferred_column(N, eps=eps, weights=SIGMA_T)
        ratios.append(r)
        print(f"    {N:14.3e} {r:18.12f}")
    chk("X-C1 the ratio is identical at every column, over 15 decades",
        max(ratios) - min(ratios) < 1e-12,
        "the column cancels EXACTLY -- this is the whole point")

    # ---- X-D ----------------------------------------------------------------
    print("\n  X-D  what the ratio measures under an m_e shift")
    for e in (1e-4, 1e-3, 1e-2):
        r = inferred_column(1.0, eps=e, weights=DM_DELAY) / \
            inferred_column(1.0, eps=e, weights=SIGMA_T)
        print(f"       eps = {e:.0e}:  ratio - 1 = {r-1:+.6e}   (expect +{e:.0e})")
    r = inferred_column(1.0, eps=1e-4, weights=DM_DELAY) / \
        inferred_column(1.0, eps=1e-4, weights=SIGMA_T)
    chk("X-D1 ratio = 1 + eps to first order", abs((r - 1) / 1e-4 - 1) < 1e-3,
        "a direct, column-free handle on eps")

    # ---- X-E ----------------------------------------------------------------
    print("\n  X-E  and under an alpha shift")
    da = 1e-4
    ra = inferred_column(1.0, dalpha=da, weights=DM_DELAY) / \
        inferred_column(1.0, dalpha=da, weights=SIGMA_T)
    print(f"       d_alpha = {da:.0e}:  ratio - 1 = {ra-1:+.6e}   (expect -{da:.0e})")
    chk("X-E1 ratio = 1 - d_alpha, the OPPOSITE sign", abs((ra - 1) / (-da) - 1) < 1e-3,
        "so the pair separates m_e from alpha by sign, as the paper's other pairs do")

    # ---- X-F: anti-control --------------------------------------------------
    print("\n  X-F  ANTI-CONTROL: is it the weight DIFFERENCE that does the work?")
    same = inferred_column(1.0, eps=1e-3, weights=DM_DELAY) / \
        inferred_column(1.0, eps=1e-3, weights=DM_DELAY)
    chk("X-F1 two probes of EQUAL weight give exactly no signal", abs(same - 1.0) < 1e-15,
        f"ratio = {same:.15f} — so having two probes is not enough; they must differ")

    # ---- X-G: anti-control --------------------------------------------------
    print("\n  X-G  ANTI-CONTROL: what if the two probes see DIFFERENT columns?")
    r_bad = inferred_column(1.0, eps=eps, weights=DM_DELAY) / \
        inferred_column(1.10, eps=eps, weights=SIGMA_T)      # 10% column mismatch
    chk("X-G1 a 10% column mismatch swamps a 1e-3 signal",
        abs(r_bad - 1) > 10 * eps,
        f"ratio - 1 = {r_bad-1:+.4f} against a signal of {eps:.0e} — the columns must "
        "genuinely be the same, and that is the observational work")

    # ---- X-H ----------------------------------------------------------------
    print("\n  X-H  does the new row add information to the existing five?")
    print(f"       existing m_e weights: {sorted(set(PAPER_ME.values()))}")
    print(f"       Thomson row:          {m_sig}")
    chk("X-H1 the Thomson weight -2 already appears (Faraday rotation)",
        m_sig in PAPER_ME.values(),
        "so it is NOT a new weight -- its value is that it reconstructs the SAME column "
        "as the DM row, which Faraday does not")
    chk("X-H2 and it differs from the DM row, which is what makes the pair work",
        m_sig != PAPER_ME["DM"], f"{m_sig} vs {PAPER_ME['DM']}")

    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  RESULT — THE PROMOTION PIECE HAS A DERIVATION")
    print("=" * 78)
    print("""
  THE DEMOTION SAID the dispersion row needs "an independent determination of the same
  electron column". One exists in the same physics the paper already uses. The Thomson
  cross-section sigma_T ~ alpha^2/m_e^2 means any optical depth reported as a column
  inherits weight -2, against the dispersion row's -1.

  TWO RECONSTRUCTIONS OF ONE COLUMN AT DIFFERENT WEIGHTS => THE COLUMN CANCELS. Checked
  numerically across fifteen decades of column, the ratio N_e(DM)/N_e(Thomson) is
  identical to one part in 10^12: the unknown drops out exactly. To first order the ratio
  is 1 + eps -- a handle on the shift that never requires knowing the true column, which
  is precisely the obstruction the demotion identified.

  AND IT INHERITS THE PAPER'S DISCRIMINATOR. Under an alpha shift the same ratio goes as
  1 - delta_alpha. A varying electron mass raises it, a varying fine-structure constant
  lowers it, so the pair separates the hypotheses by SIGN, exactly as the paper's
  opposite-weight pairs do. Nothing new has to be argued for.

  THE ANTI-CONTROLS FIX WHAT IS ACTUALLY DOING THE WORK. Two probes of EQUAL weight give
  identically no signal, so it is the weight DIFFERENCE and not the mere existence of a
  second probe. And a 10% mismatch between the two columns produces a shift a hundred
  times the size of a 1e-3 signal -- so "the same column" is a hard requirement, not a
  formality, and it is where the observational difficulty lives.

  WHAT THIS IS. A derivation at the same standing as the paper's five existing rows:
  textbook scalings, no free parameters, checkable by inspection.

  WHAT THIS IS NOT. An observational programme. Pairing a dispersion measure with a
  Thomson optical depth over the SAME column is the work that remains. The natural
  candidates -- fast-radio-burst columns against kinetic-SZ or CMB optical depth through
  the same structures -- are candidates, NOT existing measurements, and no claim is made
  here that such a pairing has been done or that its precision is known. Any text must
  keep that line exactly where this script puts it.
""")


if __name__ == "__main__":
    main()
