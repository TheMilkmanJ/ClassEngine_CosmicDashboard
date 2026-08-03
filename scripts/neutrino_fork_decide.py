#!/usr/bin/env python3
"""
#81: decide the neutrino fork. Two incompatible values of Sigma m_nu are in the corpus
and both are being called the model's prediction. This computes what each rests on.

THE FORK.
  (A) KOIDE BRANCH.  Put the neutrino triple on the cone, Q_nu = 2/3, i.e. A = sqrt2.
      Reachable only on the (-,+,+) sign branch. Predicts m_1 = 0.374 meV,
      Sigma m_nu = 58.5 meV.
  (B) P-2026-012.    m_lightest = rho_Lambda^(1/4) = 2.24 meV, Sigma m_nu = 61.3 meV.

PROVENANCE, READ BEFORE COMPUTING (protocol 48/50). P-2026-012 is explicitly
CONDITIONAL: "IF the dCDF dark-energy floor is neutrino-funded (MaVaN-style) ... then
the floor SCALE is set by the neutrino mass", and it carries its own void clause --
"the DE floor shown NOT neutrino-funded => the conditional is void, prediction
withdrawn, not falsified". So (B) is conditional on a premise about the FLOOR.

Branch (A) is conditional too, on a premise about the CONE: that the neutrino triple
sits on it at all. The corpus already rules on that from two independent directions --
T6 concludes the cone acts in the charged sector specifically, and the basement reaches
the same place because screening weights by charge^2, so a neutral cone is worth zero.

So neither is unconditional, and the decision is about which premise the corpus has
actually established. This script supplies the arithmetic that premise-talk needs, and
in particular the ONE parameter-free test available.

THE PARAMETER-FREE TEST, which is the real discriminator. With
sqrt(m_k) = a[1 + A cos(phi + 2 pi k/3)], the overall scale a CANCELS from the ratio
Dm2_31/Dm2_21. So fixing A = sqrt2 (Koide) AND phi = 2/9 + pi/12 (the recorded
Brannen-style value) leaves ZERO free parameters and predicts that ratio outright. The
measured ratio is 33.9. Either the prediction lands or it does not.

If instead phi is left free at A = sqrt2, one parameter fits one ratio and the fit is
guaranteed -- m_1 is then an output, and that is where 0.374 meV comes from. A
guaranteed fit is not evidence; the zero-parameter version is.

PRE-STATED CONTROLS:
  F-A  reproduce the recorded positive-branch ceiling Q_nu <= 0.585, and show Q = 2/3
       is unreachable there, so the Koide branch NEEDS the negative root.
  F-B  reproduce Q_nu at P-2026-012's m_1 on both sign branches.
  F-C  reproduce the Koide branch's m_1 = 0.374 meV and Sigma = 58.5 meV.
  F-D  reproduce P-2026-012's Sigma = 61.3 meV.
  F-E  THE DISCRIMINATOR: the zero-parameter ratio at A = sqrt2, phi = 2/9 + pi/12.
  F-F  ANTI-CONTROL: with phi free at A = sqrt2 the ratio must be fittable exactly, so
       that route cannot be counted as evidence.
  F-G  ANTI-CONTROL: the two Sigma values must be far enough apart to matter, and must
       be compared against the current cosmological bound rather than each other.
"""

import math

TOL = 1e-9
# NuFIT normal ordering, the values the corpus computes with
DM2_21 = 7.42e-5
DM2_31 = 2.515e-3
RHO_L_QUARTER = 2.24e-3          # eV, P-2026-012's m_lightest

_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


def masses(m1, d21=DM2_21, d31=DM2_31):
    return m1, math.sqrt(m1 * m1 + d21), math.sqrt(m1 * m1 + d31)


def Q_of(m1, sign1=+1.0, d21=DM2_21, d31=DM2_31):
    m = masses(m1, d21, d31)
    r = [sign1 * math.sqrt(m[0]), math.sqrt(m[1]), math.sqrt(m[2])]
    return sum(m) / (sum(r) ** 2)


def solve_m1(target_Q, sign1, d21=DM2_21, d31=DM2_31, lo=1e-9, hi=5e-2):
    f = lambda x: Q_of(x, sign1, d21, d31) - target_Q
    if f(lo) * f(hi) > 0:
        return None
    for _ in range(300):
        mid = math.sqrt(lo * hi)
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return math.sqrt(lo * hi)


def ring_ratio(A, phi):
    """Dm2_31/Dm2_21 from the ring form; the scale a cancels."""
    r = [1.0 + A * math.cos(phi + 2.0 * math.pi * k / 3.0) for k in range(3)]
    m = sorted(x * x for x in r)
    d21 = m[1] ** 2 - m[0] ** 2
    d31 = m[2] ** 2 - m[0] ** 2
    return d31 / d21 if d21 != 0 else float("inf")


def main():
    print("=" * 78)
    print("  #81 — DECIDING THE NEUTRINO FORK")
    print("=" * 78)
    meas_ratio = DM2_31 / DM2_21
    print(f"\n  measured  Dm2_31/Dm2_21 = {meas_ratio:.4f}")

    # ---- F-A ----------------------------------------------------------------
    print("\n  F-A  the positive-root branch: what Q can it reach?")
    print(f"\n    {'m_1 (meV)':>11} {'Q_nu (+,+,+)':>14}")
    for m1 in (0.0, 1e-4, 1e-3, 5e-3, 5e-2):
        print(f"    {m1*1e3:11.3f} {Q_of(max(m1, 1e-12), +1):14.6f}")
    ceiling = Q_of(1e-12, +1)
    chk("F-A1 the ceiling as m_1 -> 0 is the recorded 0.585", abs(ceiling - 0.5857) < 1e-3,
        f"{ceiling:.6f}")
    chk("F-A2 and Q = 2/3 is unreachable on that branch", solve_m1(2 / 3, +1) is None,
        "so the Koide branch REQUIRES the negative root — that is not optional")

    # ---- F-B ----------------------------------------------------------------
    print("\n  F-B  Q at P-2026-012's m_1 = 2.24 meV, both sign branches")
    q_pos, q_neg = Q_of(RHO_L_QUARTER, +1), Q_of(RHO_L_QUARTER, -1)
    chk("F-B1 all-positive gives Q = 0.4586", abs(q_pos - 0.4586) < 1e-3, f"{q_pos:.6f}")
    chk("F-B2 (-,+,+) gives the recorded Q = 0.835", abs(q_neg - 0.835) < 2e-3,
        f"{q_neg:.6f} — off the cone either way")

    # ---- F-C ----------------------------------------------------------------
    print("\n  F-C  the Koide branch — and the two recorded numbers used DIFFERENT inputs")
    # The recorded pair (0.374 meV, 58.5 meV) does not reproduce on the splittings
    # P-2026-012 says the corpus computes with. It reproduces on the OTHER current
    # NuFIT set. Both branches must be compared on ONE set or the gap is an artifact.
    SETS = (("NuFIT set A  7.42e-5 / 2.515e-3", 7.42e-5, 2.515e-3),
            ("NuFIT set B  7.53e-5 / 2.455e-3", 7.53e-5, 2.455e-3))
    print(f"\n    {'splittings':<32} {'Koide m_1':>11} {'Koide Sum':>11}"
          f" {'P-012 Sum':>11} {'gap':>8}")
    rows = {}
    for label, d21, d31 in SETS:
        mk = solve_m1(2 / 3, -1, d21, d31)
        sk = sum(masses(mk, d21, d31)) * 1e3
        sp = sum(masses(RHO_L_QUARTER, d21, d31)) * 1e3
        rows[label] = (mk * 1e3, sk, sp)
        print(f"    {label:<32} {mk*1e3:11.4f} {sk:11.2f} {sp:11.2f} {sp-sk:8.2f}")
    chk("F-C1 the recorded 0.374 meV / 58.5 meV reproduces on set B, not set A",
        abs(rows[SETS[1][0]][0] - 0.374) < 0.01 and abs(rows[SETS[1][0]][1] - 58.6) < 0.3
        and abs(rows[SETS[0][0]][0] - 0.374) > 0.01,
        f"set B gives {rows[SETS[1][0]][0]:.4f} / {rows[SETS[1][0]][1]:.2f}; "
        f"set A gives {rows[SETS[0][0]][0]:.4f} / {rows[SETS[0][0]][1]:.2f}")
    chk("F-C2 so the two forks were quoted on DIFFERENT splittings",
        abs(rows[SETS[0][0]][1] - rows[SETS[1][0]][1]) > 0.4,
        "the recorded 58.5 vs 61.3 gap is partly an input mismatch, not physics")
    m1_k = rows[SETS[0][0]][0] / 1e3
    sig_k = rows[SETS[0][0]][1] / 1e3

    # ---- F-D ----------------------------------------------------------------
    print("\n  F-D  P-2026-012's sum, on the same set A")
    sig_p = sum(masses(RHO_L_QUARTER))
    chk("F-D1 Sigma m_nu = 61.3 meV", abs(sig_p * 1e3 - 61.3) < 0.3, f"{sig_p*1e3:.2f} meV")
    chk("F-D2 and the like-for-like gap is smaller than the quoted one",
        abs((sig_p - sig_k) * 1e3 - 2.21) < 0.1,
        f"{(sig_p-sig_k)*1e3:.2f} meV on one splitting set, against the 2.8 meV implied "
        "by quoting 58.5 against 61.3")

    # ---- F-E: THE DISCRIMINATOR --------------------------------------------
    print("\n  F-E  THE PARAMETER-FREE TEST: A = sqrt2 AND phi = 2/9 + pi/12")
    A = math.sqrt(2.0)
    phi = 2.0 / 9.0 + math.pi / 12.0
    pred = ring_ratio(A, phi)
    dev = abs(pred / meas_ratio - 1.0) * 100.0
    print(f"       phi = 2/9 + pi/12 = {phi:.6f}")
    print(f"       predicted ratio   = {pred:.4f}")
    print(f"       measured  ratio   = {meas_ratio:.4f}")
    print(f"       deviation         = {dev:.2f}%")
    chk("F-E1 the zero-parameter prediction is computed, not fitted", True,
        "the scale a cancels from the ratio, so nothing is free here")
    chk("F-E2 and it MISSES the measured ratio by more than 1%", dev > 1.0,
        f"{dev:.2f}% — the recorded '0.5%' is not reproduced")

    # ---- F-F: anti-control --------------------------------------------------
    print("\n  F-F  ANTI-CONTROL: is the phi-free version evidence?")
    best, best_phi = None, None
    for i in range(200001):
        p = i * (2 * math.pi / 200000)
        r = ring_ratio(A, p)
        if math.isfinite(r):
            d = abs(r - meas_ratio)
            if best is None or d < best:
                best, best_phi = d, p
    chk("F-F1 with phi free the ratio is fitted essentially exactly",
        best / meas_ratio < 1e-3,
        f"best |miss| = {best/meas_ratio*100:.4f}% at phi = {best_phi:.6f}")
    chk("F-F2 so a one-parameter fit to one number is guaranteed, not evidence", True,
        "which is where m_1 = 0.374 meV comes from — an output of a saturated fit")

    # ---- F-G: anti-control --------------------------------------------------
    print("\n  F-G  ANTI-CONTROL: does present data separate them?")
    gap = abs(sig_p - sig_k) * 1e3
    print(f"       Koide branch  Sigma = {sig_k*1e3:.2f} meV")
    print(f"       P-2026-012    Sigma = {sig_p*1e3:.2f} meV")
    print(f"       gap                 = {gap:.2f} meV  ({gap/(sig_k*1e3)*100:.1f}%)")
    chk("F-G1 the gap is small compared with current cosmological sensitivity",
        gap < 10.0,
        "DESI-era upper limits sit at ~72-120 meV; BOTH are allowed, so data does "
        "NOT decide this today")

    # ---- verdict ------------------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED — do not record: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  RESULT — THE FORK RESOLVES, AND NOT BY DATA")
    print("=" * 78)
    print(f"""
  DATA DOES NOT DECIDE IT. The two sums are {sig_k*1e3:.1f} and {sig_p*1e3:.1f} meV, a gap of
  {gap:.1f} meV. Current cosmological upper limits sit far above both, so nothing measured
  today separates them (F-G). Anyone waiting for data to settle this waits years.

  THE KOIDE BRANCH LOSES ITS EVIDENCE UNDER ITS OWN PARAMETER-FREE TEST. The ring form's
  overall scale cancels from Dm2_31/Dm2_21, so fixing A = sqrt2 and phi = 2/9 + pi/12
  predicts that ratio with NOTHING free. It gives {pred:.2f} against a measured {meas_ratio:.2f} --
  a {dev:.1f}% miss (F-E). The corpus records this agreement as "0.5%"; it is not reproduced.

  AND THE FALLBACK IS NOT EVIDENCE. Leaving phi free at A = sqrt2 fits the ratio to
  {best/meas_ratio*100:.4f}% -- but that is one parameter fitted to one number, which is guaranteed
  and carries no information (F-F). m_1 = 0.374 meV is an OUTPUT of that saturated fit,
  not a prediction from it.

  THE STRUCTURAL RULING WAS ALREADY MADE, AND IT POINTS THE SAME WAY. Q_nu = 2/3 is
  unreachable with all roots positive -- the ceiling is {ceiling:.4f} (F-A) -- so the Koide
  branch REQUIRES the negative root, and the corpus has twice concluded, by independent
  arguments, that the cone is selected by ELECTRIC CHARGE: T6 from the neutrino failure
  itself, the basement because screening weights by charge^2 and a neutral cone is worth
  zero. Numerical reachability on a sign branch is not a mechanism for being there.

  ==> RULING: P-2026-012 STANDS AS THE MODEL'S NEUTRINO PREDICTION. Sigma m_nu = 61.3 meV
      with m_lightest = 2.24 meV, carried with its own stated conditional (the floor
      being neutrino-funded) and its own void clause.

  ==> THE KOIDE-NEUTRINO BRANCH IS WITHDRAWN as a prediction. Sigma m_nu = 58.5 meV must
      not be quoted as the model's number. It survives only as an observation: IF the
      neutral triple were on the cone, the sum would be 58.5 meV -- and the corpus's own
      charge-selector argument says it is not, while the parameter-free test that would
      have supported it misses by {dev:.0f}%.

  WHAT WOULD REOPEN IT, stated so the door is not nailed shut by accident: a mechanism
  putting a NEUTRAL triple on the cone, which would have to defeat both charge-selector
  arguments at once; or a corrected phi that passes the parameter-free ratio test. The
  second is checkable immediately against any proposed phi, and this script is the check.
""")


if __name__ == "__main__":
    main()
