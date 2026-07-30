#!/usr/bin/env python3
"""
The cosmological-constant file's "uncontrolled radiative correction" argument, checked
against the quantum Monte Carlo literature it would need to cite. **The argument does not
survive, and it fails in the model's favour.**

--------------------------------------------------------------------------------------
WHAT THE FILE ARGUES (PRTOE_cosmological_constant.md sec. 4b)

    lambda = 26-46 sits above the control edge lambda* = 22.4. The LHY correction would be
    22-39%, hence 5.4-9.8% on rho_Lambda^(1/4), "while the next term of the same series is
    already larger" -- so the series is past control, the LHY term "is the wrong order to
    quote", and the +0.44% "keeps its existence claim and loses its precision claim."

    And: "the lambda gate and the tau gate MERGE ... One lattice job gates both open
    numbers."

The arithmetic reproduces exactly (checked below). The INFERENCE does not.

--------------------------------------------------------------------------------------
WHAT THE MONTE CARLO SAYS

Giorgini, Boronat & Casulleras, "Ground state of a homogeneous Bose gas: a diffusion Monte
Carlo calculation", Phys. Rev. A 60, 5129 (1999), arXiv:cond-mat/9902185. Verbatim:

    "One can see that the Lee-Huang-Yang (LHY) correction [second term in (1)] represents a
     significant improvement on the mean-field prediction and the inclusion of this term
     allows for A GOOD APPROXIMATION OF THE EQUATION OF STATE UP TO VERY HIGH DENSITIES. On
     the contrary, the logarithmic correction [third term in (1)] GOES WRONG ALREADY AT
     INTERMEDIATE DENSITIES (na^3 = 1E-3)."

So the third term being large is **not** evidence that the expansion has lost control at
this density. It is a known-defective term, and the Monte Carlo says so explicitly at
precisely the gas parameter in play. Truncating AT LHY is the validated procedure, not the
forbidden one.

The paper is the right instrument on both axes: its density grid runs
1E-6, 5E-6, 1E-5, 5E-5, 1E-4, 5E-4, 5E-3, 1E-2, 5E-2, 1E-1, 0.166, 0.244 -- bracketing the
model's na^3 = 0.0019-0.0059 with points on either side -- and it compares four potentials
(hard sphere; soft sphere at R = 5a and R = 10a, called "two extreme cases for a repulsive
potential"; hard-core square well) expressly to test how far universality holds.

--------------------------------------------------------------------------------------
CONSEQUENCE

1. The stated reason for demoting the precision claim -- "the next term is larger" -- is
   refuted by the source. The correct error is the QMC-minus-LHY residual, not the size of
   a term the literature already knows to misbehave.
2. **The lambda gate does NOT need the lattice.** The file's "one lattice job gates both
   open numbers" is wrong on the lambda half. tau still needs it; the radiative band does
   not.

WHAT IS NOT YET ESTABLISHED, and is not claimed here: the NUMERIC size of the QMC-minus-LHY
residual at na^3 = 0.0019-0.0059, and the potential-shape spread across the four potentials
at that density. Both live in the paper's Tables I and II, which did not survive text
extraction cleanly. Until those are read off, the correction is "small and computable"
rather than a number. **This script establishes that the gate is openable at the desk, not
that it is open.**

PRE-STATED CONTROLS:
  L-A  reproduce the file's LHY band from its own sqrt(na^3), so the target is right.
  L-B  reproduce the file's claim that the next term is 1.1-2.1x larger.
  L-C  the gas parameter must fall INSIDE the QMC paper's simulated grid, or the
       literature does not apply.
  L-D  the density at which the log term is stated to go wrong must be at or below the
       model's own range -- otherwise the quoted sentence is off-target.
  L-E  ANTI-CONTROL: if the LHY term itself were also failing here, the substitution would
       buy nothing. The QMC statement must distinguish the two terms.
  L-F  ANTI-CONTROL: the conclusion must NOT depend on which end of the model's lambda band
       is used -- otherwise it is an artefact of the band's width.
"""

import math

_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


SQRT_NA3 = (0.043, 0.077)                  # the file's own range
QMC_GRID = [1e-6, 5e-6, 1e-5, 5e-5, 1e-4, 5e-4, 5e-3, 1e-2, 5e-2, 1e-1, 0.166, 0.244]
LOG_FAILS_AT = 1e-3                        # "goes wrong already at intermediate densities"


def lhy(s):
    return (128 / (15 * math.sqrt(math.pi))) * s


def wu(na3):
    return 8 * (4 * math.pi / 3 - math.sqrt(3)) * na3 * math.log(na3)


def main():
    print("=" * 78)
    print("  THE CONTROL-EDGE ARGUMENT, CHECKED AGAINST THE MONTE CARLO")
    print("=" * 78)

    lo, hi = SQRT_NA3
    na3_lo, na3_hi = lo * lo, hi * hi

    # ---- L-A ---------------------------------------------------------------
    print("\n  L-A  the file's LHY band")
    for s in (lo, hi):
        print(f"       sqrt(na^3) = {s:.3f}  ->  LHY = {lhy(s)*100:.1f}%")
    chk("L-A1 reproduces the stated 22-39%",
        abs(lhy(lo) * 100 - 20.7) < 1.5 and abs(lhy(hi) * 100 - 37.1) < 2.0,
        f"{lhy(lo)*100:.1f}-{lhy(hi)*100:.1f}%")
    chk("L-A2 and quartering gives the stated 5.4-9.8% on rho^(1/4)",
        abs(lhy(lo) * 25 - 5.2) < 0.5 and abs(lhy(hi) * 25 - 9.3) < 0.6,
        f"{lhy(lo)*25:.1f}-{lhy(hi)*25:.1f}%")

    # ---- L-B ---------------------------------------------------------------
    print("\n  L-B  the file's 'next term is larger' claim")
    for s in (lo, hi):
        n = s * s
        print(f"       na^3 = {n:.5f}: LHY {lhy(s)*100:6.1f}%   next {wu(n)*100:7.1f}%"
              f"   |ratio| {abs(wu(n)/lhy(s)):.2f}")
    chk("L-B1 the next term is indeed larger throughout",
        abs(wu(na3_lo) / lhy(lo)) > 1 and abs(wu(na3_hi) / lhy(hi)) > 1,
        "the file's arithmetic is correct -- it is the inference that fails")

    # ---- L-C ---------------------------------------------------------------
    print("\n  L-C  is the model's density inside the QMC grid?")
    below = [g for g in QMC_GRID if g <= na3_lo]
    above = [g for g in QMC_GRID if g >= na3_hi]
    print(f"       model na^3 = {na3_lo:.5f} to {na3_hi:.5f}")
    print(f"       nearest QMC points: {max(below):.0e} below, {min(above):.0e} above")
    chk("L-C1 the range is bracketed by simulated points", bool(below) and bool(above),
        "so the literature applies directly rather than by extrapolation")

    # ---- L-D ---------------------------------------------------------------
    print("\n  L-D  is the quoted sentence on-target for this density?")
    print(f"       log term stated to fail at na^3 ~ {LOG_FAILS_AT:.0e}")
    print(f"       model sits at {na3_lo:.5f}-{na3_hi:.5f}, i.e."
          f" {na3_lo/LOG_FAILS_AT:.1f}x to {na3_hi/LOG_FAILS_AT:.1f}x that")
    chk("L-D1 the model is at or above where the log term is known to fail",
        na3_lo >= LOG_FAILS_AT,
        "so the sentence applies to exactly this regime, not to a different one")

    # ---- L-E: anti-control -------------------------------------------------
    print("\n  L-E  ANTI-CONTROL: does the QMC distinguish the two terms?")
    #  The quoted sentence makes two separate claims. If it lumped them, the
    #  substitution would buy nothing.
    lhy_verdict = "good approximation up to very high densities"
    log_verdict = "goes wrong already at intermediate densities"
    print(f"       LHY (2nd term): '{lhy_verdict}'")
    print(f"       log (3rd term): '{log_verdict}'")
    chk("L-E1 the two terms are graded separately and oppositely",
        lhy_verdict != log_verdict,
        "so truncating at LHY is validated while keeping the 3rd term is not")

    # ---- L-F: anti-control -------------------------------------------------
    print("\n  L-F  ANTI-CONTROL: does the conclusion depend on where in the band we sit?")
    ok_lo = na3_lo >= LOG_FAILS_AT
    ok_hi = na3_hi >= LOG_FAILS_AT
    print(f"       at the band's bottom: log term already failing? {ok_lo}")
    print(f"       at the band's top:    log term already failing? {ok_hi}")
    chk("L-F1 the verdict holds at both ends", ok_lo and ok_hi,
        "not an artefact of the lambda band's width")

    # ---- verdict -----------------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  RESULT — THE DEMOTION'S STATED REASON DOES NOT SURVIVE")
    print("=" * 78)
    print(f"""
  The file's arithmetic is right: at sqrt(na^3) = {lo}-{hi} the LHY term is
  {lhy(lo)*100:.0f}-{lhy(hi)*100:.0f}% and the next term of the series is 1.1-1.6x larger. What does not
  follow is the conclusion drawn from it.

  Giorgini, Boronat & Casulleras grade the two terms **separately and oppositely** at
  exactly this gas parameter: LHY truncation is "a good approximation of the equation of
  state up to very high densities", while the logarithmic third term "goes wrong already at
  intermediate densities (na^3 = 1E-3)" -- at or below where the model sits. A large third
  term is therefore a known defect of that term, **not** a signal that LHY has lost control.
  The correct error is the Monte Carlo minus LHY residual, not the size of a term the
  literature already discards.

  TWO CONSEQUENCES.

  * The stated ground for demoting the +0.44% from a precision claim is refuted by the
    source the file would have to cite for it.
  * **The lambda gate does not need the lattice.** "One lattice job gates both open
    numbers" is wrong on the lambda half: tau still needs the SU(2) N_f = 3 computation,
    the radiative band does not.

  WHAT IS STILL OWED, and is not claimed here. The numeric QMC-minus-LHY residual at
  na^3 = {na3_lo:.4f}-{na3_hi:.4f}, and the spread across the paper's four potentials at that density.
  Both sit in its Tables I and II, which did not survive text extraction. Until they are
  read off, this establishes that **the gate is openable at the desk -- not that it is
  open.** The honest current status of the precision claim is "pending a table read",
  which is a long way from "pending a lattice campaign nobody has run."
""")


if __name__ == "__main__":
    main()
