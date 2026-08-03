#!/usr/bin/env python3
"""
#78 item 1: convert the radio-lattice paper's dispersion row into a sigma_eps.

WHAT THE PAPER SAYS IS OWED. `_ARXIV_READINESS.md`: "sigma_eps in physical units --
needs the DM timing-model conversion; the binding limit is a ~20 us month-correlated
timing offset rather than a DM error, and converting it needs the full timing model.
This is the one piece of physics still missing."

THE ANSWER IS THAT FOR A CONSTANT SHIFT THE CONVERSION DOES NOT EXIST, AND THE REASON
IS EXACT RATHER THAN PRACTICAL.

The dispersion delay is t_DM = (e^2 / 2 pi m_e c) (1/nu^2) INT n_e dl. A pulsar timing
model fits an infinite-frequency arrival time t_inf and a dispersion measure DM from

    t(nu) = t_inf + K DM / nu^2,       K = e^2 / 2 pi m_e^lab c

If the true electron mass along the path is m_e^lab (1 + eps), the delay produced by a
fixed physical column is smaller by (1+eps)^-1. But that changes only the COEFFICIENT
of 1/nu^2 -- the frequency dependence is untouched. So the fit absorbs it entirely:

    DM_fit = (INT n_e dl) / (1 + eps),      t_inf unchanged,      residuals EXACTLY zero

  *** A constant, universal eps is perfectly degenerate with the fitted DM. No timing
  *** dataset bounds it through dispersion, at any precision, with any frequency
  *** coverage, however good the timing model.

So the 20 us figure cannot be converted into a sigma_eps at all. It is not that the
full timing model is needed -- it is that the quantity it would constrain is not there.
The paper's own text already contains the correct statement, one sentence after the
derivation: "This row therefore tests the shift against any independent determination
of the same electron column." That sentence is the whole content of the row, and it is
what the sigma_eps must be built from.

WHAT THE 20 us DOES BOUND: eps VARIATION between epochs, with DM held fixed. Then
delta_t = -delta_eps * K DM / nu^2, and the bound depends strongly on band and column.
Computed below for representative pulsar-timing configurations.

A NOTE ON ONE SENTENCE IN THE PAPER, offered as a finding rather than an edit. Sec.
"The dispersion-measure row is statistically the strongest. Median DM uncertainties
reach ~1e-5 pc/cm^3 ... a fractional precision of 1e-7 to 1e-6." That is the precision
of the DM MEASUREMENT, which is a different quantity from sigma_eps: by the degeneracy
above, improving the DM measurement improves the determination of DM_fit and tells you
nothing about eps. The paper is already careful not to fold the 1e-7 into a forecast
("we therefore do not fold the 1e-7 figure into any forecast"), so the caution is
right; but "statistically the strongest" describes the wrong quantity, and a referee
who follows the degeneracy will land on it.

PRE-STATED CONTROLS:
  P-A  the degeneracy must be exhibited by an actual least-squares FIT to synthetic
       TOAs, not asserted: residuals must vanish to machine precision and DM_fit must
       equal N_e/(1+eps).
  P-B  it must hold for any frequency coverage -- wide, narrow, many bands, two bands.
  P-C  ANTI-CONTROL: a perturbation with a DIFFERENT frequency dependence must NOT be
       absorbed. If everything were absorbed the claim would be vacuous.
  P-D  ANTI-CONTROL: the two line rows (21 cm, RRL) must NOT be degenerate, since they
       are referred to laboratory rest frequencies. Otherwise the paper has no rows at
       all, which would be a much larger claim than this script is making.
  P-E  the 20 us must be converted into a bound on eps VARIATION, at representative
       (DM, nu), and the spread across configurations must be reported rather than a
       single number.
  P-F  the DM-measurement precision quoted in the paper must be reproduced, so the
       distinction being drawn is between two numbers that both exist.
"""

import math

TOL = 1e-12
K_DM = 4.148808e3          # MHz^2 pc^-1 cm^3 s -- standard dispersion constant
T_OFFSET = 20e-6           # s, the paper's month-correlated timing offset

_fail = []


def chk(name, cond, detail=""):
    if not cond:
        _fail.append(name)
    print(f"  {'ok  ' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))


def fit_timing(nus, toas):
    """least squares for t = a + b/nu^2; returns (a, b, max |residual|)."""
    x = [1.0 / (n * n) for n in nus]
    n = len(x)
    sx, sy = sum(x), sum(toas)
    sxx = sum(v * v for v in x)
    sxy = sum(v * t for v, t in zip(x, toas))
    den = n * sxx - sx * sx
    b = (n * sxy - sx * sy) / den
    a = (sy - b * sx) / n
    resid = max(abs(t - (a + b * v)) for v, t in zip(x, toas))
    return a, b, resid


def synth(nus, t_inf, column, eps):
    """TOAs with the TRUE electron mass shifted by eps: K -> K/(1+eps)."""
    return [t_inf + (K_DM / (1.0 + eps)) * column / (nu * nu) for nu in nus]


def main():
    print("=" * 78)
    print("  #78 — THE DISPERSION ROW'S sigma_eps")
    print("=" * 78)

    t_inf, column = 1000.0, 100.0          # s, pc cm^-3

    # ---- P-A ----------------------------------------------------------------
    print("\n  P-A  fit synthetic shifted-m_e TOAs with the standard timing model")
    nus = [327.0, 430.0, 820.0, 1400.0, 2300.0]
    print(f"\n    {'eps':>10} {'DM_fit':>16} {'N_e/(1+eps)':>16} {'max resid (s)':>16}")
    ok_a = True
    for eps in (0.0, 1e-9, 1e-6, 1e-3):
        a, b, r = fit_timing(nus, synth(nus, t_inf, column, eps))
        dm_fit = b / K_DM
        want = column / (1.0 + eps)
        good = abs(dm_fit - want) < 1e-9 * want and r < 1e-9 and abs(a - t_inf) < 1e-6
        ok_a &= good
        print(f"    {eps:10.0e} {dm_fit:16.9f} {want:16.9f} {r:16.3e}"
              f"  {'' if good else '<-- MISMATCH'}")
    chk("P-A1 the fit absorbs eps entirely: DM_fit = N_e/(1+eps), residuals ~ 0", ok_a,
        "and t_inf comes back unchanged, so nothing leaks into the arrival time")

    # ---- P-B ----------------------------------------------------------------
    print("\n  P-B  does any frequency coverage break the degeneracy?")
    covers = (("two bands, close", [1400.0, 1500.0]),
              ("two bands, wide", [327.0, 2300.0]),
              ("five bands", [327.0, 430.0, 820.0, 1400.0, 2300.0]),
              ("wideband, 40 chans", [300.0 + 50.0 * i for i in range(40)]))
    ok_b = True
    for label, ns in covers:
        _, b, r = fit_timing(ns, synth(ns, t_inf, column, 1e-6))
        good = r < 1e-9
        ok_b &= good
        print(f"       {label:<22} max residual = {r:.3e}  {'absorbed' if good else 'LEAKS'}")
    chk("P-B1 absorbed at every coverage tested", ok_b,
        "the perturbation has the SAME 1/nu^2 shape as the fitted term — no lever exists")

    # ---- P-C: anti-control --------------------------------------------------
    print("\n  P-C  ANTI-CONTROL: is anything NOT absorbed?")
    ns = [327.0, 430.0, 820.0, 1400.0, 2300.0]
    # a perturbation with a different frequency dependence: scattering-like 1/nu^4
    pert = [t_inf + K_DM * column / (n * n) + 1e-3 / (n ** 4) * 1e12 for n in ns]
    _, _, r_pert = fit_timing(ns, pert)
    chk("P-C1 a 1/nu^4 perturbation is NOT absorbed", r_pert > 1e-9,
        f"max residual {r_pert:.3e} s — the fit cannot hide a different shape")
    # a constant offset IS absorbed, by t_inf -- so the test is shape-specific
    _, _, r_const = fit_timing(ns, [t + 5.0 for t in synth(ns, t_inf, column, 0.0)])
    chk("P-C2 while a constant offset IS absorbed, by t_inf", r_const < 1e-9,
        f"max residual {r_const:.3e} s — as expected; the degeneracy is per-shape")

    # ---- P-D: anti-control --------------------------------------------------
    print("\n  P-D  ANTI-CONTROL: are the LINE rows degenerate too?")
    # 21 cm: nu_hf ~ alpha^4 mu^-2 m_p, so a shift moves the REST frequency, and the
    # comparison is against a laboratory value -- there is no free parameter to absorb it.
    eps = 1e-6
    nu_lab = 1420.405751          # MHz
    nu_true = nu_lab * (1.0 + 2.0 * eps)      # weight +2 on the 21 cm row
    z_apparent = nu_true / nu_lab - 1.0
    chk("P-D1 a shifted 21 cm rest frequency shows up as an apparent redshift offset",
        abs(z_apparent - 2.0 * eps) < 1e-15,
        f"delta z = {z_apparent:.3e} at eps = {eps:.0e} — irreducible, the lab value is fixed")
    # RRL: nu_RRL ~ alpha^2 mu^-1 m_p, weight +1 -- half the 21 cm offset, same mechanism
    nu_rrl_lab = 6000.0                        # MHz, a representative H-alpha RRL
    z_rrl = (nu_rrl_lab * (1.0 + 1.0 * eps)) / nu_rrl_lab - 1.0
    chk("P-D2 and the RRL row likewise, at half the 21 cm offset (weight +1 vs +2)",
        abs(z_rrl - eps) < 1e-15 and abs(z_apparent / z_rrl - 2.0) < 1e-9,
        f"delta z = {z_rrl:.3e}, ratio to the 21 cm row = {z_apparent/z_rrl:.6f}")

    # ---- P-E ----------------------------------------------------------------
    print("\n  P-E  what the 20 us DOES bound: eps VARIATION at fixed DM")
    print(f"       delta_t = delta_eps * K DM / nu^2,  K = {K_DM:.4f} MHz^2 pc^-1 cm^3 s")
    print(f"\n    {'DM':>8} {'nu (MHz)':>10} {'t_DM (s)':>12} {'sigma_delta_eps':>18}")
    vals = []
    for dm in (30.0, 100.0, 300.0):
        for nu in (327.0, 820.0, 1400.0):
            t_dm = K_DM * dm / (nu * nu)
            s = T_OFFSET / t_dm
            vals.append(s)
            print(f"    {dm:8.0f} {nu:10.0f} {t_dm:12.4f} {s:18.3e}")
    chk("P-E1 the bound spans orders of magnitude across configurations",
        max(vals) / min(vals) > 100,
        f"{min(vals):.2e} to {max(vals):.2e} — a single number would be misleading")
    chk("P-E2 and the best case is far short of the DM row's 1e-7 headline",
        min(vals) > 1e-7,
        f"best {min(vals):.2e} vs the quoted DM fractional precision 1e-7")

    # ---- P-F ----------------------------------------------------------------
    print("\n  P-F  reproduce the paper's DM-measurement precision, for contrast")
    for dm in (10.0, 100.0):
        frac = 1e-5 / dm
        print(f"       sigma_DM = 1e-5 pc/cm^3 against DM = {dm:.0f}"
              f"  ->  fractional {frac:.1e}")
    chk("P-F1 the paper's 1e-7 to 1e-6 range is reproduced",
        abs(1e-5 / 100.0 - 1e-7) < 1e-12 and abs(1e-5 / 10.0 - 1e-6) < 1e-12,
        "so both numbers exist — they just measure different things")

    # ---- verdict ------------------------------------------------------------
    print("\n" + "=" * 78)
    if _fail:
        print(f"  {len(_fail)} CONTROL(S) FAILED — do not record: {', '.join(_fail)}")
        print("=" * 78)
        return
    print("  RESULT — FOR A CONSTANT SHIFT THE CONVERSION DOES NOT EXIST")
    print("=" * 78)
    print("""
  THE DEGENERACY IS EXACT. A universal constant eps rescales the dispersion delay's
  COEFFICIENT and leaves its 1/nu^2 shape untouched, so a timing model fitting
  (t_inf, DM) absorbs it completely: DM_fit = N_e/(1+eps), t_inf unchanged, residuals
  at machine precision (P-A). No frequency coverage breaks it -- two bands, five bands
  or forty channels all absorb it identically (P-B), because the perturbation has the
  same shape as the fitted term and there is no lever. The anti-control confirms the
  statement is not vacuous: a 1/nu^4 perturbation is NOT absorbed (P-C).

  SO THE OWED ITEM IS NOT OWED. "sigma_eps in physical units ... needs the full timing
  model" understates the situation: it is not that the conversion is hard, it is that
  for a constant eps there is nothing to convert. That closes the item, and closes it
  more firmly than supplying a number would have.

  WHAT THE 20 us ACTUALLY BOUNDS is eps VARIATION between epochs at fixed DM, and the
  bound is strongly configuration-dependent -- 1.7e-6 for a high-DM pulsar at 327 MHz
  out to 3.1e-4 at 1400 MHz and low DM (P-E), a span of 183x. Quoting one number here
  would be misleading by more than two orders of magnitude, and the best case is still
  a factor 17 short of the 1e-7 the DM row's headline suggests.

  THE PAPER IS ALREADY RIGHT WHERE IT MATTERS. One sentence after the derivation it
  says: "This row therefore tests the shift against any independent determination of
  the same electron column." That is exactly the correct statement, and it is where a
  sigma_eps for this row has to come from -- the precision of the independent column,
  not the precision of the DM. The paper is also careful not to fold the 1e-7 into any
  forecast.

  ONE SENTENCE IS WORTH THE OWNER'S ATTENTION, OFFERED AS A FINDING AND NOT EDITED.
  "The dispersion-measure row is statistically the strongest." Both numbers in that
  paragraph are correct (P-F reproduces them), but they describe the precision of the
  DM MEASUREMENT, and by the degeneracy that precision does not transfer to eps.
  A referee who follows the degeneracy will arrive at this sentence. The safest repair
  is one clause -- that the row's strength is in DM precision, while its sensitivity to
  eps is set by the independent column determination -- but that is an authorship call,
  not a correction to make silently in someone's paper.
""")


if __name__ == "__main__":
    main()
