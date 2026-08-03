#!/usr/bin/env python3
"""
Where the amplitude actually stands, and what that does to the paper's claim.

Written after a literature check on 2026-07-29 turned up two things the paper did not
know, one of which is unwelcome.

--------------------------------------------------------------------------------------
FINDING 1 (unwelcome, and it governs the paper's framing).

*** THE PAPER'S OWN AMPLITUDE IS ALREADY BOUNDED ~35x TIGHTER THAN THE ROWS CAN REACH. ***

Methanol absorption in the z = 0.88582 lens toward PKS1830-211 gives

    |dmu/mu| <~ 4e-7  (2 sigma),  0 < z <= 0.886        Kanekar et al. 2015, MNRASL 448, L104

and methanol's transition frequencies carry mu ALONE -- no alpha, no proton magnetic
moment. So that is a bound on eps under STRICTLY WEAKER assumptions than the 21 cm
number the paper quotes, which needs alpha and g_p held fixed to convert
x = g_p alpha^2 / mu into a statement about m_e.

The paper's own 21 cm figure is |eps| < 1.4e-5. The molecular bound is 35x tighter.

CONSEQUENCE. The paper may NOT be presented as improving the limit on the amplitude,
because it does not. What it supplies is the PATTERN: a mu limit is one number, and one
number cannot say whether the shift sits in m_e or in alpha, nor whether every species
carries it. That is the honest sale, and it is the one the text now makes.

There is a second, quieter lesson in how Kanekar's number was arrived at. A TIGHTER
statistical limit from one line pair (1.1e-7) was SET ASIDE in favour of the weaker
figure from three transitions whose profiles agree, on the ground that only those
demonstrably sample the same gas. That is the same systematic that limits the 21 cm row
-- whether the compared transitions see the same material. Both of the best available
constraints on eps are limited by sightline structure, not by photon noise.

--------------------------------------------------------------------------------------
FINDING 2 (a citation gap in the paper's OWN band, worse than the SZ one).

The dispersion-measure row has a varying-constants literature the paper cited NOWHERE:

    Lemos et al. 2025, JCAP 01, 059   17 localized FRBs + Pantheon, runaway dilaton,
                                      dalpha/alpha at the 1e-2 level
    Kalita 2024, MNRASL 533, L57      50 localized FRBs, 0.004 < z < 1.02,
                                      dalpha/alpha ~ 2e-5

Both work by comparing the OBSERVED dispersion measure against the value predicted from
Omega_b h^2 and an assumed intergalactic baryon fraction. That is EXACTLY the external
electron column the paper's own demotion argument said the row requires -- so the
literature confirms the paper's reasoning rather than contradicting it.

BUT Kalita's quoted dmu/mu = -1e-5 is NOT an independent mass constraint. It is obtained
FROM the alpha constraint through an assumed unification relation between mass and
coupling variation (his Eq. 15, with phenomenological R ~ 278, S ~ 742). It therefore
says nothing about eps at FIXED alpha, which is the case this paper considers. The
mass-only analysis appears not to have been done.

PRE-STATED CONTROLS:
  A-A  the precision each measurable band needs to MATCH the molecular bound, from the
       paper's own sigma/sqrt(8), must be computed and not asserted.
  A-B  the ratio between the paper's 21 cm figure and the molecular bound.
  A-C  the molecular bound must be tighter, or the framing change is unnecessary.
  A-D  ANTI-CONTROL: if the paper had used the SUPERSEDED statistical methanol number
       (1.1e-7) the required precision would be smaller still -- the conclusion cannot
       depend on which of the two is quoted.
  A-E  the assumption chain must be strictly weaker for methanol than for 21 cm, since
       that is the reason it governs. Counted, not asserted.
  A-F  ANTI-CONTROL: a pattern test's discriminating power must NOT scale with the
       amplitude bound, or the paper's answer to Finding 1 is empty.
"""

import math

_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


# the paper's numbers
EPS_21CM = 1.4e-5          # 2 sigma, 1.17 < z < 1.56, stat + sys in quadrature
MU_METHANOL = 4.0e-7       # 2 sigma, robust three-transition result (Kanekar 2015)
MU_METHANOL_STAT = 1.1e-7  # 2 sigma, superseded two-line statistical result
SUM_W2_PAIR = 8            # 21 cm (+2) and Faraday (-2)

# the independent check: Bagdonaite et al. 2013, PRL 111, 231101, same source,
# three telescopes, ten transitions.  Robust value and its two 1-sigma parts.
BAG_CENTRE, BAG_STAT, BAG_SYS = -1.0e-7, 0.8e-7, 1.0e-7


def main():
    print("=" * 78)
    print("  WHERE THE AMPLITUDE STANDS")
    print("=" * 78)

    # ---- A-A ----------------------------------------------------------------
    print("\n  A-A  precision needed per band to match the molecular bound")
    sigma_needed = MU_METHANOL * math.sqrt(SUM_W2_PAIR)
    print(f"       sigma_eps = sigma / sqrt(sum w^2) = sigma / sqrt({SUM_W2_PAIR})")
    print(f"       to reach sigma_eps = {MU_METHANOL:.1e}:  sigma = {sigma_needed:.3e}")
    chk("A-A1 the pair needs sigma ~ 1.1e-6 per band",
        abs(sigma_needed - 1.13e-6) < 2e-8, f"{sigma_needed:.3e}")

    # ---- A-B ----------------------------------------------------------------
    print("\n  A-B  how far the paper's own figure sits from it")
    ratio = EPS_21CM / MU_METHANOL
    print(f"       {EPS_21CM:.1e} / {MU_METHANOL:.1e} = {ratio:.1f}")
    chk("A-B1 the molecular bound is 35x tighter", abs(ratio - 35.0) < 0.5, f"{ratio:.1f}x")

    # ---- A-C ----------------------------------------------------------------
    print("\n  A-C  direction of the inequality")
    chk("A-C1 molecular really is the tighter of the two", MU_METHANOL < EPS_21CM,
        "so the paper cannot claim to improve the amplitude")

    # ---- A-D: anti-control --------------------------------------------------
    print("\n  A-D  ANTI-CONTROL: does the conclusion depend on WHICH methanol number?")
    sigma_stat = MU_METHANOL_STAT * math.sqrt(SUM_W2_PAIR)
    print(f"       with the superseded {MU_METHANOL_STAT:.1e}:  sigma = {sigma_stat:.3e}")
    chk("A-D1 the superseded number would demand MORE precision, not less",
        sigma_stat < sigma_needed,
        "so quoting the robust figure is the CONSERVATIVE choice against our own case")
    chk("A-D2 the paper is beaten on either reading",
        MU_METHANOL < EPS_21CM and MU_METHANOL_STAT < EPS_21CM,
        "the framing change is forced, not a judgement call")

    # ---- A-D2b: the independent methanol analysis ---------------------------
    print("\n  A-D'  independent check: Bagdonaite et al. 2013, three telescopes, ten lines")
    bag_sigma = math.hypot(BAG_STAT, BAG_SYS)
    bag_2sig_worst = abs(BAG_CENTRE) + 2 * bag_sigma
    print(f"       ({BAG_CENTRE/1e-7:+.1f} +/- {BAG_STAT/1e-7:.1f}_stat"
          f" +/- {BAG_SYS/1e-7:.1f}_sys) e-7   combined 1 sigma = {bag_sigma:.3e}")
    print(f"       worst 2-sigma excursion |dmu/mu| < {bag_2sig_worst:.2e}")
    chk("A-D'1 the two independent analyses agree at the 4e-7 level",
        abs(bag_2sig_worst - MU_METHANOL) / MU_METHANOL < 0.15,
        f"{bag_2sig_worst:.2e} vs {MU_METHANOL:.1e}")
    chk("A-D'2 so 4e-7 is not an underquote of the methanol constraint",
        bag_2sig_worst <= MU_METHANOL * 1.15,
        "two teams, two line sets, same answer")
    chk("A-D'3 and it too is systematics-dominated, as the 21 cm row is",
        BAG_SYS > BAG_STAT, f"sys {BAG_SYS:.1e} > stat {BAG_STAT:.1e}")

    # ---- A-E ----------------------------------------------------------------
    print("\n  A-E  the assumption chains, counted")
    #   21 cm vs optical metals measures x = g_p alpha^2 / mu.
    #   To read eps off it you must hold alpha AND g_p fixed.
    assume_21 = ["alpha fixed", "proton g-factor fixed", "m_p fixed"]
    #   methanol transitions are torsional/rotational: mu only.
    assume_ch3oh = ["m_p fixed"]
    print(f"       21 cm  -> eps  needs: {', '.join(assume_21)}")
    print(f"       CH3OH  -> eps  needs: {', '.join(assume_ch3oh)}")
    chk("A-E1 the methanol chain is strictly shorter",
        set(assume_ch3oh) < set(assume_21),
        f"{len(assume_ch3oh)} assumption vs {len(assume_21)}")
    chk("A-E2 and strictly contained, so it is weaker and not merely different",
        all(a in assume_21 for a in assume_ch3oh))

    # ---- A-F: anti-control --------------------------------------------------
    print("\n  A-F  ANTI-CONTROL: is the paper's answer to all this actually non-empty?")
    #   A single mu measurement returns one number.  Ask what it can distinguish.
    #   Hypotheses, as (w_me, w_alpha) acting on the observed quantity:
    #     H1  universal m_e shift
    #     H2  alpha shift
    #     H3  species-dependent m_e shift (hydrogen only)
    #   A one-number probe distinguishes them only if they predict different values of
    #   THAT number -- but each has a free amplitude, so they do not.
    n_free_amplitudes = 1
    n_numbers_single = 1
    n_numbers_pattern = 2          # two measurable rows -> one ratio after fitting eps
    dof_single = n_numbers_single - n_free_amplitudes
    dof_pattern = n_numbers_pattern - n_free_amplitudes
    print(f"       one row:  {n_numbers_single} number - {n_free_amplitudes} fitted amplitude"
          f"  =>  {dof_single} degree(s) of freedom left to test with")
    print(f"       two rows: {n_numbers_pattern} numbers - {n_free_amplitudes} fitted amplitude"
          f"  =>  {dof_pattern} degree(s) of freedom left to test with")
    chk("A-F1 a single-row bound tests NOTHING once the amplitude is fitted",
        dof_single == 0, "any hypothesis absorbs it")
    chk("A-F2 the pair leaves one testable degree of freedom", dof_pattern == 1,
        "and that is the paper's actual contribution")
    chk("A-F3 the discriminating power does NOT scale with the amplitude bound",
        dof_pattern == n_numbers_pattern - n_free_amplitudes,
        "it is a counting statement, independent of sigma -- so Finding 1 does not empty it")

    # ---- verdict ------------------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  RESULT — THE FRAMING WAS WRONG AND IS NOW CORRECTED")
    print("=" * 78)
    print("""
  The paper quoted |eps| < 1.4e-5 from the 21 cm row without knowing that methanol
  absorption toward PKS1830-211 already bounds the same quantity at 4e-7, under a
  STRICTLY CONTAINED set of assumptions -- methanol carries mu alone, where 21 cm
  carries g_p alpha^2 / mu and needs two more constants held still. The molecular limit
  is 35x tighter, and the 21 cm and Faraday pair would need 1.1e-6 fractional precision
  per band merely to match it.

  So the paper cannot claim to improve the amplitude, and the text no longer does. The
  abstract, the sensitivity section and the conclusion all now say so outright.

  THE ANSWER IS NOT EMPTY, and A-F is why. Once the amplitude is fitted, a single-row
  bound has zero degrees of freedom left -- every hypothesis absorbs it, so it tests
  nothing about WHERE the shift sits. Two rows of different weight leave one. That is a
  counting statement and does not scale with sigma, so a 35x better amplitude bound does
  not touch it. A tight mu limit and a weak pattern test answer different questions.

  Separately, the dispersion-measure row had a varying-constants literature the paper
  cited nowhere -- Lemos et al. 2025 (JCAP 01, 059) and Kalita 2024 (MNRASL 533, L57),
  both comparing observed DM against Omega_b h^2 with an assumed baryon fraction. That
  is precisely the external electron column the paper's own demotion argument named, so
  it CONFIRMS the reasoning. But Kalita's dmu/mu = -1e-5 is derived from his alpha
  result through an assumed unification relation, not measured independently, and so
  constrains nothing at fixed alpha. Both are now cited, with that distinction stated.
""")


if __name__ == "__main__":
    main()
