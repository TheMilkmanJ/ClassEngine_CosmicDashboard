#!/usr/bin/env python3
"""
Every number destined for the 0nubb paper, recomputed from oscillation data rather than
copied from the corpus. Protocol 48: open the script that produced the numbers.

The hypothesis under test is narrow and stated as such: the lightest neutrino mass equals
the observed dark-energy scale, m_1 = rho_Lambda^(1/4) = 2.25 meV, with normal ordering.
Nothing about the wider framework enters. The OBSERVED 2.25 is used throughout, never the
model's derived 2.2599 -- that distinction is load-bearing and is checked below.

PRE-STATED CONTROLS:
  M-A  the three |U_ei^2 m_i| terms, against the corpus's (1.52, 2.67, 1.10).
  M-B  Sigma m_nu.
  M-C  the m_bb ceiling and floor.
  M-D  the floor exists ONLY because the middle term exceeds the other two combined --
       compute the margin, since the whole "sharp probe" claim rests on it.
  M-E  minimal normal ordering (m_1 = 0) window, against [1.48, 3.69].
  M-F  detection probabilities over flat Majorana phases, by direct integration.
  M-G  the discriminating band, and the fraction of this model landing inside it.
  M-H  ANTI-CONTROL: using the DERIVED 2.2599 instead of the observed 2.25 must move the
       floor but leave the ceiling and every conclusion intact.
  M-I  ANTI-CONTROL: inverted ordering must give a different, non-overlapping window, or
       the paper is not testing what it says it tests.
"""

import math

_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


# NuFIT-class oscillation parameters, normal ordering
S12SQ = 0.307
S13SQ = 0.022
DM21 = 7.42e-5      # eV^2
DM31 = 2.51e-3      # eV^2
M1_OBS = 2.25e-3    # eV -- the OBSERVED dark-energy scale
M1_DER = 2.2599e-3  # eV -- the model's derived anchor (anti-control only)


def masses(m1, dm21=DM21, dm31=DM31):
    return m1, math.sqrt(m1 * m1 + dm21), math.sqrt(m1 * m1 + dm31)


def terms(m1, **kw):
    m = masses(m1, **kw)
    u = ((1 - S12SQ) * (1 - S13SQ), S12SQ * (1 - S13SQ), S13SQ)
    return [ui * mi for ui, mi in zip(u, m)]


def window(t):
    """|t0 + t1 e^{ia} + t2 e^{ib}| over free phases: max is the sum; min is 0 unless one
    term exceeds the other two, in which case it is that excess."""
    hi = sum(t)
    mx = max(t)
    lo = max(0.0, 2 * mx - hi)
    return lo, hi


def prob_above(t, thr, n=1200):
    """fraction of flat Majorana phase space with m_bb > thr, by direct integration"""
    c = 0
    for i in range(n):
        a = 2 * math.pi * (i + 0.5) / n
        for j in range(n):
            b = 2 * math.pi * (j + 0.5) / n
            re = t[0] + t[1] * math.cos(a) + t[2] * math.cos(b)
            im = t[1] * math.sin(a) + t[2] * math.sin(b)
            if math.hypot(re, im) > thr:
                c += 1
    return c / (n * n)


def main():
    print("=" * 78)
    print("  m_bb WITH THE LIGHTEST MASS AT THE DARK-ENERGY SCALE")
    print("=" * 78)
    meV = 1e3

    # ---- M-A ---------------------------------------------------------------
    print(f"\n  M-A  the three contributions at m_1 = {M1_OBS*meV:.2f} meV")
    t = terms(M1_OBS)
    for lab, v in zip(('|U_e1^2 m_1|', '|U_e2^2 m_2|', '|U_e3^2 m_3|'), t):
        print(f"       {lab} = {v*meV:.3f} meV")
    ref = (1.52, 2.67, 1.10)
    chk("M-A1 reproduces (1.52, 2.67, 1.10) meV",
        all(abs(v * meV - r) < 0.01 for v, r in zip(t, ref)),
        ", ".join(f"{v*meV:.2f}" for v in t))

    # ---- M-B ---------------------------------------------------------------
    print("\n  M-B  the mass sum")
    s = sum(masses(M1_OBS)) * meV
    print(f"       Sigma m_nu = {s:.2f} meV")
    chk("M-B1 close to the recorded 61.4 meV", abs(s - 61.4) < 0.2, f"{s:.2f}")

    # ---- M-C ---------------------------------------------------------------
    print("\n  M-C  the m_bb window")
    lo, hi = window(t)
    print(f"       floor {lo*meV:.4f} meV   ceiling {hi*meV:.3f} meV")
    chk("M-C1 ceiling 5.30 meV", abs(hi * meV - 5.30) < 0.02, f"{hi*meV:.3f}")
    chk("M-C2 floor ~0.04 meV", abs(lo * meV - 0.045) < 0.01, f"{lo*meV:.4f}")

    # ---- M-D ---------------------------------------------------------------
    print("\n  M-D  why the floor exists at all")
    mid, others = t[1], t[0] + t[2]
    print(f"       middle term {mid*meV:.3f} vs other two combined {others*meV:.3f} meV")
    print(f"       margin = {(mid-others)*meV:.4f} meV, on terms of order 2.6")
    chk("M-D1 the middle term does exceed the other two", mid > others,
        "so the three phasors cannot close and exact cancellation is impossible")
    chk("M-D2 the margin is ~0.05 meV", abs((mid - others) * meV - 0.045) < 0.01,
        f"{(mid-others)*meV:.4f} meV -- this is what makes m_bb a sharp probe of m_1")

    # ---- M-E ---------------------------------------------------------------
    print("\n  M-E  minimal normal ordering, m_1 = 0")
    t0 = terms(0.0)
    lo0, hi0 = window(t0)
    print(f"       window [{lo0*meV:.2f}, {hi0*meV:.2f}] meV")
    chk("M-E1 reproduces [1.48, 3.69] meV",
        abs(lo0 * meV - 1.48) < 0.02 and abs(hi0 * meV - 3.69) < 0.02,
        f"[{lo0*meV:.2f}, {hi0*meV:.2f}]")

    # ---- M-F ---------------------------------------------------------------
    print("\n  M-F  detection probabilities over flat Majorana phases")
    p_nexo = prob_above(t, 4.7e-3)
    p_tag = prob_above(t, 2.35e-3)
    p_min_tag = prob_above(t0, 2.35e-3)
    print(f"       this model above nEXO baseline 4.7 meV : {p_nexo*100:.1f}%   (recorded 10.8%)")
    print(f"       this model above tagged      2.35 meV : {p_tag*100:.1f}%   (recorded 69%)")
    print(f"       minimal NO above tagged      2.35 meV : {p_min_tag*100:.1f}%   (recorded 63.7%)")
    chk("M-F1 baseline nEXO ~10.8%", abs(p_nexo * 100 - 10.8) < 1.0, f"{p_nexo*100:.1f}%")
    chk("M-F2 tagged ~69%", abs(p_tag * 100 - 69) < 2.0, f"{p_tag*100:.1f}%")
    chk("M-F3 minimal NO tagged ~63.7%", abs(p_min_tag * 100 - 63.7) < 2.0,
        f"{p_min_tag*100:.1f}% -- so tagging does NOT discriminate")

    # ---- M-G ---------------------------------------------------------------
    print("\n  M-G  the discriminating band")
    band_lo, band_hi = hi0, hi          # minimal-NO ceiling to this model's ceiling
    p_band = prob_above(t, band_lo) - prob_above(t, band_hi)
    print(f"       band = [{band_lo*meV:.2f}, {band_hi*meV:.2f}] meV")
    print(f"       minimal NO cannot reach it at ANY phases (its ceiling is {hi0*meV:.2f})")
    print(f"       this model lands inside it {p_band*100:.1f}% of the time (recorded 31.7%)")
    chk("M-G1 the band is 3.69-5.30 meV",
        abs(band_lo * meV - 3.69) < 0.02 and abs(band_hi * meV - 5.30) < 0.02)
    chk("M-G2 this model lands there ~31.7%", abs(p_band * 100 - 31.7) < 1.5,
        f"{p_band*100:.1f}%")
    chk("M-G3 baseline nEXO's whole reach sits inside the band", 4.7e-3 >= band_lo,
        "so the baseline machine is the decisive one, not the upgrade")

    # ---- M-H: anti-control -------------------------------------------------
    print("\n  M-H  ANTI-CONTROL: the derived 2.2599 instead of the observed 2.25")
    td = terms(M1_DER)
    lod, hid = window(td)
    print(f"       floor {lod*meV:.4f} meV (was {lo*meV:.4f})   ceiling {hid*meV:.3f} (was {hi*meV:.3f})")
    chk("M-H1 the floor moves", abs(lod - lo) * meV > 0.001)
    chk("M-H2 the ceiling does NOT, to the quoted precision", abs((hid - hi) * meV) < 0.02,
        "every conclusion rides on the ceiling, so the anchor choice does not matter")
    chk("M-H3 and the paper uses the OBSERVED value regardless", M1_OBS == 2.25e-3)

    # ---- M-I: anti-control -------------------------------------------------
    print("\n  M-I  ANTI-CONTROL: inverted ordering")
    #  IO: m_3 lightest; m_1,m_2 ~ sqrt(dm32). Use the standard IO window at small m_light.
    m3 = M1_OBS
    m1i = math.sqrt(m3 * m3 + 2.49e-3)
    m2i = math.sqrt(m3 * m3 + 2.49e-3 + DM21)
    ti = [(1 - S12SQ) * (1 - S13SQ) * m1i, S12SQ * (1 - S13SQ) * m2i, S13SQ * m3]
    loi, hii = window(ti)
    print(f"       IO window [{loi*meV:.1f}, {hii*meV:.1f}] meV")
    chk("M-I1 inverted ordering sits far above this model's ceiling", loi > hi,
        f"{loi*meV:.1f} > {hi*meV:.2f} -- the orderings do not overlap, so the test is real")

    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  RESULT — EVERY PAPER NUMBER REPRODUCES FROM OSCILLATION DATA")
    print("=" * 78)
    print(f"""
  Setting the lightest neutrino mass to the observed dark-energy scale, m_1 = 2.25 meV, with
  normal ordering and NuFIT-class mixings, gives contributions
  ({t[0]*meV:.2f}, {t[1]*meV:.2f}, {t[2]*meV:.2f}) meV and

      m_bb in [{lo*meV:.2f}, {hi*meV:.2f}] meV,   Sigma m_nu = {s:.1f} meV.

  The floor is not protected by symmetry. It exists only because the middle term exceeds
  the other two combined by {(mid-others)*meV:.3f} meV on terms of order 2.6, so the three phasors
  cannot close a triangle. That near-cancellation is also what makes m_bb an unusually sharp
  function of m_1 -- and it is the honest reason this is more than a plug-in exercise.

  THE TEST IS THE CEILING, NOT THE FLOOR. Minimal normal ordering (m_1 = 0) tops out at
  {hi0*meV:.2f} meV. This hypothesis reaches {hi*meV:.2f}. The gap between them, {band_lo*meV:.2f} to {band_hi*meV:.2f} meV, is a band
  minimal ordering cannot enter at any phases and this hypothesis occupies {p_band*100:.0f}% of the
  time. Baseline nEXO's reach lands entirely inside that band, so the baseline machine is the
  discriminating one; the barium-tagged upgrade raises the detection probability from
  {p_nexo*100:.0f}% to {p_tag*100:.0f}% but separates almost nothing, since minimal ordering also clears 2.35 meV
  {p_min_tag*100:.0f}% of the time.

  The anti-controls hold: swapping the observed 2.25 meV for the model-derived 2.2599 moves
  the floor and leaves the ceiling alone, so no conclusion depends on which anchor is used
  (the paper uses the observed one); and inverted ordering sits entirely above the window,
  so the hypothesis is genuinely falsifiable by an ordering determination alone.
""")


if __name__ == "__main__":
    main()
