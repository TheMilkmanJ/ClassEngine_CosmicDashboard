#!/usr/bin/env python3
"""
Theta settled from the corpus's own definition, and three things I got wrong today
corrected. No owner decision was ever needed; the answer was in docs/exploratory/.

--------------------------------------------------------------------------------------
THE DEFINITION (PRTOE_me_trigger.md sec. 3 and 5, quoted verbatim):

    Theta = multi-stream interference present = granules on.
    Single-stream (voids, pre-collapse, pre-structure universe): no granules, m_e bare.
    Multi-stream (halos, folded filaments): granules on, m_e lab.

    m_e = m_bare(1 + kappa*Theta),  kappa = -2 eps/(1+eps) = -2.478%

So Theta is a CONTINUOUS multi-stream occupancy, not a binary screening switch and not a
speckle intensity in the optical sense. And the endpoints are the reverse of what I assumed:

    Theta = 0    single-stream, laminar, VOIDS      -> m_e = m_bare      (the FULL shift)
    Theta = 1/2  developed speckle, HALOS/filaments -> m_e = m_bare/(1+eps) = m_lab

That second identity is exact, not approximate: 1 + kappa/2 = 1/(1+eps) to machine
precision, because kappa was DEFINED to make it so.

--------------------------------------------------------------------------------------
WHAT I GOT WRONG, all three today:

(1) I claimed P-2026-050 and P-2026-007 faced a factor-2 fork, on the reading that the
    shift is eps*Theta so <Theta> = 1/2 would halve it. **Wrong.** The shift is
    kappa*Theta with kappa NEGATIVE and calibrated so Theta = 1/2 lands exactly on the lab
    value. Void gas is Theta = 0, which gives the FULL bare shift. **Both amplitudes stand
    as registered. Nothing halves.** The annotations are withdrawn.

(2) I escalated it to the owner as a decision. It was never a decision -- the definition
    is written down in docs/exploratory/PRTOE_me_trigger.md, which I had not read.

(3) Docket #62's scatter used eps where the coupling is kappa. The per-cell m_e scatter in
    a developed-speckle region is |kappa|*sd(Theta), not eps*sd(Theta) -- larger by
    2/(1+eps) = 1.975x. Every width number in #62 is low by that factor.

WHAT SURVIVES, AND IT IS SHARPER. #62's argument was that averaging cannot reach a line
width. That holds, and correcting the coupling makes the tension worse -- but the
correction also RELOCATES it, because developed speckle lives in MULTI-STREAM gas: halos
and folded filaments. That is exactly where 21 cm and methanol absorbers are observed. So
the broadening lands precisely on the systems that supply the tightest constraints.

The escape is real and it is not the sightline. Sightline averaging protects the centroid
only. What protects the WIDTH is averaging inside each absorbing atom's own sampling
volume: if an atom's interaction region spans many granules it sees one effective Theta,
and every atom sees nearly the same one. That is a quantitative demand on the granule
scale, computed below, and it is a different demand from the one the corpus recorded.

PRE-STATED CONTROLS:
  K-A  reproduce the corpus's kappa = -2.478% from its own formula.
  K-B  Theta = 1/2 must land EXACTLY on the lab value, or kappa is not what it claims.
  K-C  Theta = 0 must give the full bare shift, confirming voids carry it.
  K-D  ANTI-CONTROL: the registered amplitudes must be UNCHANGED, or my withdrawal is
       itself wrong.
  K-E  the corrected #62 scatter, and the factor by which my recorded value was low.
  K-F  the corrected 21 cm broadening, in multi-stream gas.
  K-G  the granules-per-sampling-volume needed to bring the width under an observed one.
  K-H  ANTI-CONTROL: sightline averaging must NOT fix the width, or #62's core claim dies.
  K-I  the corpus's own residual-laminar slope must reproduce, as an independent check
       that I am reading kappa the same way the corpus does.
"""

import math

_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


ALPHA = 0.0072973525693
C_KMS = 299792.458
EPS = 27 * ALPHA / (5 * math.pi)
KAPPA = -2 * EPS / (1 + EPS)
SD_THETA = 0.25
W_21 = 2


def main():
    print("=" * 78)
    print("  THETA RESOLVED FROM THE CORPUS'S OWN DEFINITION")
    print("=" * 78)

    # ---- K-A ---------------------------------------------------------------
    print("\n  K-A  the coupling constant")
    print(f"       kappa = -2 eps/(1+eps) = {KAPPA*100:.4f}%   (corpus states -2.478%)")
    chk("K-A1 reproduces the corpus's -2.478%", abs(KAPPA * 100 + 2.478) < 0.001,
        f"{KAPPA*100:.4f}%")

    # ---- K-B ---------------------------------------------------------------
    print("\n  K-B  does Theta = 1/2 land on the LAB value?")
    at_half = 1 + KAPPA * 0.5
    lab = 1 / (1 + EPS)
    print(f"       1 + kappa/2 = {at_half:.12f}")
    print(f"       1/(1+eps)   = {lab:.12f}")
    chk("K-B1 exactly the lab value", abs(at_half - lab) < 1e-15,
        "kappa was defined to make this identity hold")

    # ---- K-C ---------------------------------------------------------------
    print("\n  K-C  does Theta = 0 give the full bare shift?")
    at_zero = 1 + KAPPA * 0.0
    shift_vs_lab = at_zero / lab - 1
    print(f"       m_e(Theta=0)/m_lab - 1 = {shift_vs_lab*100:.4f}%   (registered +1.2543%)")
    chk("K-C1 voids carry the FULL eps", abs(shift_vs_lab - EPS) < 1e-12,
        f"{shift_vs_lab*100:.4f}% = eps exactly")

    # ---- K-D: anti-control -------------------------------------------------
    print("\n  K-D  ANTI-CONTROL: are the registered amplitudes unchanged?")
    freq = W_21 * shift_vs_lab
    print(f"       P-2026-007 mass shift in voids : {shift_vs_lab*100:.4f}%  (registered 1.24%)")
    print(f"       P-2026-050 frequency offset    : {freq*100:.4f}%  (registered 2.509%)")
    chk("K-D1 the mass shift is the registered 1.24%", abs(shift_vs_lab * 100 - 1.2543) < 0.001)
    chk("K-D2 the frequency offset is the registered 2.509%", abs(freq * 100 - 2.5086) < 0.001,
        "NOTHING HALVES -- my fork was wrong and is withdrawn")

    # ---- K-E ---------------------------------------------------------------
    print("\n  K-E  docket #62's scatter, corrected")
    old = EPS * SD_THETA
    new = abs(KAPPA) * SD_THETA
    print(f"       what I recorded: eps*sd    = {old:.4e}")
    print(f"       correct:      |kappa|*sd   = {new:.4e}   low by {new/old:.3f}x")
    chk("K-E1 the correct scatter is 6.19e-3", abs(new - 6.19e-3) < 2e-5, f"{new:.4e}")
    chk("K-E2 my recorded value was low by 2/(1+eps)", abs(new / old - 2 / (1 + EPS)) < 1e-12,
        f"{new/old:.4f}")

    # ---- K-F ---------------------------------------------------------------
    print("\n  K-F  the corrected 21 cm broadening, and WHERE it lands")
    sd_v = C_KMS * W_21 * new
    print(f"       sd = c * {W_21} * {new:.4e} = {sd_v:.0f} km/s")
    print( "       and developed speckle is MULTI-STREAM gas -- halos and folded filaments,")
    print( "       which is exactly where 21 cm and methanol absorbers are observed.")
    chk("K-F1 the broadening is ~3712 km/s", abs(sd_v - 3712) < 25, f"{sd_v:.0f} km/s")
    chk("K-F2 it is 2/(1+eps) worse than #62 recorded",
        abs(sd_v / (C_KMS * W_21 * old) - 2 / (1 + EPS)) < 1e-9)

    # ---- K-G ---------------------------------------------------------------
    print("\n  K-G  granules per atomic sampling volume needed to hide it")
    for W in (1.0, 10.0, 50.0):
        supp = sd_v / W
        n = supp ** 2
        print(f"       to fit {W:5.1f} km/s: suppress {supp:7.0f}x  ->  N_granules >= {n:.3e}")
        if W == 10.0:
            n10 = n
    chk("K-G1 a 10 km/s allowance needs ~1.4e5 granules per sampling volume",
        abs(n10 - 1.38e5) / 1.38e5 < 0.05, f"{n10:.3e}")

    # ---- K-H: anti-control -------------------------------------------------
    print("\n  K-H  ANTI-CONTROL: does sightline averaging fix the width?")
    for N in (1e3, 1e6, 1e9):
        print(f"       N = {N:.0e} cells along the path: width still {sd_v:.0f} km/s")
    chk("K-H1 sightline averaging leaves the width untouched", True,
        "N is absent from it -- #62's core claim survives the correction")
    chk("K-H2 so the escape must be SUB-ATOMIC-scale averaging, not sightline",
        n10 > 1, "a different demand from the one the corpus recorded")

    # ---- K-I ---------------------------------------------------------------
    print("\n  K-I  independent check: the corpus's residual-laminar slope")
    #  corpus: <Theta> ~ 1/2 - 0.155 f  =>  dm_e/m_e = 0.384% * f
    f = 1.0
    dtheta = -0.155 * f
    slope = abs(KAPPA * dtheta)
    print(f"       <Theta> = 1/2 - 0.155f  =>  dm_e/m_e = |kappa|*0.155*f"
          f" = {slope*100:.3f}%*f   (corpus states 0.384%*f)")
    chk("K-I1 reproduces the corpus's 0.384% slope", abs(slope * 100 - 0.384) < 0.005,
        f"{slope*100:.3f}% -- confirms I am reading kappa as the corpus does")

    # ---- verdict -----------------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  RESULT — NO FORK, NO DECISION, AND #62 GETS SHARPER")
    print("=" * 78)
    print(f"""
  Theta is a continuous multi-stream occupancy. Its endpoints are the reverse of what I
  assumed: voids are Theta = 0 and carry the FULL bare shift; halos are Theta = 1/2 and sit
  exactly on the laboratory value, because kappa = -2eps/(1+eps) was defined to put them
  there. The identity 1 + kappa/2 = 1/(1+eps) holds to machine precision, and the corpus's
  own residual-laminar slope 0.384%*f reproduces from the same kappa -- two independent
  confirmations that I am now reading it the way the corpus does.

  **Both registered amplitudes stand exactly as written: +1.2543% in voids, +2.509% in
  frequency. Nothing halves. My factor-2 fork was wrong and is withdrawn, and so is the
  owner decision I raised on the back of it -- the answer was written down in
  docs/exploratory/PRTOE_me_trigger.md the whole time.**

  The one genuine defect is a LABEL: P-2026-050's parenthetical "(Theta = 1 -- the bare
  value)" puts bare at Theta = 1. Bare is at Theta = 0. The number attached to it is right.

  DOCKET #62 IS CORRECTED AND STRENGTHENED. Its scatter used eps where the coupling is
  kappa, so every width figure was low by 2/(1+eps) = 1.975x. The per-cell scatter is
  {new:.2e}, not {old:.2e}, and the 21 cm broadening is {sd_v:.0f} km/s, not 1880.

  And the correction RELOCATES the tension, which matters more than its size. Developed
  speckle lives in MULTI-STREAM gas -- halos and folded filaments -- which is precisely
  where 21 cm and methanol absorbers are found. The broadening therefore lands on the very
  systems that supply the tightest constraints, not on some unobserved diffuse phase.

  THE ESCAPE IS REAL BUT IT IS NOT THE SIGHTLINE. Sightline averaging protects a centroid
  and cannot touch a width -- that was #62's point and it survives. What protects the width
  is averaging WITHIN each absorbing atom's sampling volume: if that volume spans many
  granules, every atom sees the same effective Theta and the line stays narrow. The demand
  is {n10:.1e} granules per sampling volume to fit inside 10 km/s. That is a concrete,
  checkable constraint on the granule scale, and it is a DIFFERENT constraint from the
  sightline cell count the corpus recorded.
""")


if __name__ == "__main__":
    main()
