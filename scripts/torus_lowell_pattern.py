#!/usr/bin/env python3
"""
The low-ℓ cavity pattern, ISW-inclusive, on a RETAINED script.
(T5 low-ℓ thread; no task number of its own — #160 is the two-fluid sims.)

Regenerates BOTH numbers the 2026-07-18 scratch-era pass booked and then lost:

  (1) the quadrupole retention  C_2(torus)/C_2(infinite)  at the matched-circles floor
      L = 27.6 Gpc, computed with the integrated Sachs-Wolfe term included rather than
      Sachs-Wolfe alone (scripts/torus_quadrupole.py is the SW-only toy and is kept);
  (2) the off-diagonal correlation pattern rho_ij over the 990 = C(45,2) pairs of the
      45 harmonic coefficients with 2 <= l <= 6, and its total signal-to-noise.

Why it exists: the booked "83% retention at the floor" and the booked rho table came from a
pass whose script was not retained, so neither could be re-run before the BipoSH handoff
graded them.  This script is the retained generator.  Run it with no arguments.

PHYSICS
-------
Flat cubic 3-torus of side L, observer at the origin.  Allowed wavevectors are the reciprocal
lattice k = (2*pi/L) n, n in Z^3 \\ {0} — a finite box has NO mode with k < 2*pi/L, which is
what cuts the largest-angle power.  For a primordial potential with a scale-invariant spectrum
P_Phi(k) = A k^-3,

    a_lm = 4 pi i^l  sum_n  Phi_n  Delta_l(k_n)  Y*_lm(khat_n)

    < a_lm a*_l'm' >  =  (4 pi)^2 i^(l-l')  (1/V)  sum_n  P(k_n) Delta_l Delta_l'
                          Y*_lm(khat_n) Y_l'm'(khat_n),      V = L^3

and the infinite-universe limit  (1/V) sum_n -> int d^3k/(2 pi)^3  returns
C_l = (2/pi) int k^2 dk P(k) Delta_l(k)^2, diagonal.  The same prefactor appears on both
sides, so A cancels out of every ratio reported here.

Transfer function, normalised so that g(chi_*) = 1 (which makes the SW piece exactly the
SW-only toy's integrand, and the ISW piece the addition).  With u = k chi_* and s = chi/chi_*
it is a pure function of u:

    Delta_l(u) = (1/3) j_l(u)  -  2 int_0^1 ds (dg/ds) j_l(u s)

with Phi(k, chi) = Phi_i(k) g(chi) and g = D(a)/a the linear growth suppression.  g falls from
1 to g_0 < 1 as Lambda takes over, so dg/ds > 0 and the ISW transfer carries the opposite sign
to the SW transfer, per DeltaT/T = Psi_*/3 + 2 int Psi' d(eta).

Scope, stated rather than hidden: late ISW only (matter+Lambda growth equation).  The early
ISW, sourced by the residual radiation just after last scattering, is an l ~ 100-200 effect and
is not modelled; reionisation damping is a uniform multiplicative factor and cancels in every
ratio here.  Cubic torus (equal sides): the anisotropic case is recorded separately and
shallows the suppression rather than deepening it.

INPUTS, each read from the corpus rather than assumed
-----------------------------------------------------
  chi_*    = 13.76 Gpc   docs/PRTOE_READERS_GUIDE.md:70, docs/PRTOE_PREREGISTERED_PREDICTIONS.md:1849
  L_floor  = 27.6 Gpc    docs/PRTOE_lowell_anomalies.md:47 (matched-circles floor, ~2 chi_*)
  H0       = 69.9        docs/PRTOE_FAILURES_LEDGER.md:1559 ("the model's own H0 = 69.9")
  Omega_m  = 0.30        docs/PRTOE_v4_dCDF_results.md:26
  l range  = 2..6        docs/PRTOE_lowell_anomalies.md:79 (990 pairs = C(45,2))
"""

import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.special import spherical_jn, sph_harm_y

# ----------------------------------------------------------------------------- inputs
CHI_STAR = 13760.0        # Mpc, the corpus's own comoving distance to last scattering
L_FLOOR = 27600.0         # Mpc, the matched-circles floor
H0 = 69.9                 # km/s/Mpc
OMEGA_M = 0.30
LMIN, LMAX = 2, 6
NMAX_DIAG = 160           # |n| cutoff for the angle-averaged retention
NMAX_COV = 46             # |n| cutoff for the full 45x45 covariance
C_KMS = 299792.458

UMAX = 600.0
DU = 0.01


# --------------------------------------------------------------- background and growth
def growth_g(omega_m=OMEGA_M):
    """g(a) = D(a)/a for flat matter+Lambda.  Returns (a_grid, g_grid), g unnormalised."""
    om_l = 1.0 - omega_m
    e2 = lambda a: omega_m * a ** -3 + om_l

    def rhs(lna, y):
        a = np.exp(lna)
        d, dp = y
        dlnh_dlna = -1.5 * omega_m * a ** -3 / e2(a)
        return [dp, -(2.0 + dlnh_dlna) * dp + 1.5 * omega_m * a ** -3 / e2(a) * d]

    lna0 = np.log(1e-4)
    sol = solve_ivp(rhs, (lna0, 0.0), [1e-4, 1e-4], rtol=1e-11, atol=1e-15,
                    dense_output=True, method="DOP853")
    lna = np.linspace(lna0, 0.0, 40001)
    a = np.exp(lna)
    return a, sol.sol(lna)[0] / a


def comoving_distance(a_grid, omega_m=OMEGA_M, h0=H0):
    om_l = 1.0 - omega_m
    inv_e = lambda a: 1.0 / (a * a * np.sqrt(omega_m * a ** -3 + om_l))
    return (C_KMS / h0) * np.array([quad(inv_e, a, 1.0, limit=200)[0] for a in a_grid])


def _s_grid_and_dgds():
    """s = chi/chi_* on a two-region grid (fine where the ISW source lives), plus dg/ds."""
    a, g = growth_g()
    chi = comoving_distance(a)
    order = np.argsort(chi)
    chi, g = chi[order], g[order]
    fine = np.arange(0.0, 8000.0, 5.0)
    coarse = np.arange(8000.0, CHI_STAR + 1e-9, 25.0)
    grid = np.concatenate([fine, coarse, [CHI_STAR]])
    grid = np.unique(grid)
    gi = np.interp(grid, chi, g)
    gi = gi / gi[-1]                       # g(chi_*) = 1
    s = grid / CHI_STAR
    return s, np.gradient(gi, s), gi


S_GRID, DG_DS, G_S = _s_grid_and_dgds()
_TRAPW = np.zeros_like(S_GRID)             # trapezoid weights on the non-uniform s grid
_TRAPW[:-1] += 0.5 * np.diff(S_GRID)
_TRAPW[1:] += 0.5 * np.diff(S_GRID)
_SRC = DG_DS * _TRAPW                      # the ISW source, pre-weighted

_UGRID = np.arange(0.0, UMAX + DU, DU)
_TABLE = {}


def _build_table():
    """Delta_l(u) on the u grid, for l = LMIN..LMAX, SW+ISW.  One-time cost."""
    nchunk = max(1, int(4e7 // len(S_GRID)))
    for l in range(LMIN, LMAX + 1):
        d = spherical_jn(l, _UGRID) / 3.0
        isw = np.empty_like(_UGRID)
        for i in range(0, len(_UGRID), nchunk):
            uu = _UGRID[i:i + nchunk]
            isw[i:i + nchunk] = -2.0 * (spherical_jn(l, np.outer(uu, S_GRID)) @ _SRC)
        _TABLE[l] = (d, d + isw)


def delta_u(l, u, isw=True):
    """Delta_l at u = k chi_*, by interpolation on the precomputed table."""
    if not _TABLE:
        _build_table()
    sw, tot = _TABLE[l]
    return np.interp(u, _UGRID, tot if isw else sw)


# --------------------------------------------- infinite-universe C_l (the denominator)
def cl_infinite(l, isw=True, umax=None):
    """(2/pi) int dk/k Delta_l^2 = (2/pi) int du/u Delta_l(u)^2, a pure number.

    `umax` truncates the integral at the SAME u the lattice sum is truncated at, so the
    ratio is apples-to-apples: a lattice capped at |n| <= nmax carries no mode above
    u = 2 pi nmax chi_*/L, and the denominator must not carry one either.
    """
    hi = UMAX * 0.98 if umax is None else min(umax, UMAX * 0.98)
    lu = np.linspace(np.log(1e-6), np.log(hi), 400001)
    u = np.exp(lu)
    d = delta_u(l, u, isw=isw)
    return (2.0 / np.pi) * np.trapezoid(d * d, lu)


# --------------------------------------------------- torus: shell multiplicities r3(m)
def shell_counts(nmax):
    n = np.arange(-nmax, nmax + 1)
    sq = n * n
    s2 = (sq[:, None] + sq[None, :]).ravel()
    m2 = nmax * nmax
    counts = np.zeros(m2 + 1, dtype=np.int64)
    for s in sq:
        t = s2 + s
        t = t[(t >= 1) & (t <= m2)]
        counts += np.bincount(t, minlength=m2 + 1)
    return counts


_COUNT_CACHE = {}


def retention(L, lmax=LMAX, isw=True, nmax=NMAX_DIAG, chi_star=None):
    """C_l(torus)/C_l(infinite), l = LMIN..lmax.

    Angle-averaged, so only shell multiplicities are needed (addition theorem):
      C_l(torus) = (4 pi / V) sum_n P(k_n) Delta_l(k_n)^2 .
    """
    cs = CHI_STAR if chi_star is None else chi_star
    if nmax not in _COUNT_CACHE:
        _COUNT_CACHE[nmax] = shell_counts(nmax)
    counts = _COUNT_CACHE[nmax]
    m = np.nonzero(counts)[0]
    kn = 2.0 * np.pi * np.sqrt(m) / L
    un = kn * cs
    ucut = 2.0 * np.pi * nmax * cs / L
    out = {}
    for l in range(LMIN, lmax + 1):
        d = delta_u(l, un, isw=isw)
        num = (4.0 * np.pi / L ** 3) * np.sum(counts[m] * kn ** -3.0 * d * d)
        out[l] = num / cl_infinite(l, isw=isw, umax=ucut)
    return out


# ------------------------------------------------------- torus: the full 45x45 covariance
def _lm_index():
    return [(l, mm) for l in range(LMIN, LMAX + 1) for mm in range(-l, l + 1)]


def covariance(L, isw=True, nmax=NMAX_COV, chunk=150000):
    """Hermitian M_(lm),(l'm') = <a_lm a*_l'm'> up to the common prefactor.

    M = (4 pi)^2 i^(l-l') (1/V) sum_n P(k_n) Delta_l Delta_l' Y*_lm(khat) Y_l'm'(khat).
    Isotropy would make this diagonal; a compact space does not.
    """
    idx = _lm_index()
    nlm = len(idx)
    M = np.zeros((nlm, nlm), dtype=complex)

    n = np.arange(-nmax, nmax + 1)
    N1, N2, N3 = np.meshgrid(n, n, n, indexing="ij")
    N = np.stack([N1.ravel(), N2.ravel(), N3.ravel()], axis=1)
    nsq = (N * N).sum(axis=1)
    keep = (nsq >= 1) & (nsq <= nmax * nmax)
    N, nsq = N[keep], nsq[keep]

    for i0 in range(0, len(N), chunk):
        v = N[i0:i0 + chunk].astype(float)
        kn = 2.0 * np.pi * np.sqrt(nsq[i0:i0 + chunk]) / L
        r = np.sqrt((v * v).sum(axis=1))
        theta = np.arccos(np.clip(v[:, 2] / r, -1.0, 1.0))
        phi = np.arctan2(v[:, 1], v[:, 0])
        dl = {l: delta_u(l, kn * CHI_STAR, isw=isw) for l in range(LMIN, LMAX + 1)}
        Y = np.empty((len(v), nlm), dtype=complex)
        D = np.empty((len(v), nlm))
        for j, (l, mm) in enumerate(idx):
            Y[:, j] = sph_harm_y(l, mm, theta, phi)
            D[:, j] = dl[l]
        w = kn ** -3.0
        M += (np.conj(Y) * D * w[:, None]).T @ (Y * D)

    M *= (4.0 * np.pi) ** 2 / L ** 3
    ph = np.array([1j ** l for l, _ in idx])
    return idx, ph[:, None] * M * np.conj(ph)[None, :]


def rho_matrix(M):
    d = np.sqrt(np.real(np.diag(M)))
    return M / np.outer(d, d)


# --------------------------------------------------------------------------------- report
def main():
    print("=" * 78)
    print("T5 low-l — flat cubic 3-torus pattern, ISW-inclusive (retained generator)")
    print("=" * 78)
    _build_table()
    print(f"  chi_* = {CHI_STAR/1000:.3f} Gpc   H0 = {H0}   Omega_m = {OMEGA_M}   "
          f"g(today)/g(chi_*) = {G_S[0]:.4f}")
    print(f"  matched-circles floor L = {L_FLOOR/1000:.1f} Gpc = {L_FLOOR/CHI_STAR:.3f} chi_*")

    print("\n  [validation 1] infinite-universe C_l, SW only, vs analytic 1/(9 pi l(l+1)):")
    for l in range(LMIN, LMAX + 1):
        num, ana = cl_infinite(l, isw=False), 1.0 / (9.0 * np.pi * l * (l + 1))
        print(f"    l={l}: numeric {num:.6e}  analytic {ana:.6e}  ratio {num/ana:.5f}")

    print("\n  [validation 2] shell multiplicities r3(m), |n|^2 = 1..5 -> 6, 12, 8, 6, 24:")
    _c = shell_counts(6)
    print(f"    r3 = {[int(_c[i]) for i in range(1, 6)]}   "
          f"{'OK' if [int(_c[i]) for i in range(1,6)] == [6,12,8,6,24] else 'MISMATCH'}")

    print("\n  [validation 3] retention -> 1 as L -> infinity (SW+ISW, the normalisation test):")
    for L in (80000.0, 200000.0, 400000.0, 1000000.0):
        r = retention(L, lmax=2)
        print(f"    L = {L/1000:>7.0f} Gpc (k_min chi_* = {2*np.pi*CHI_STAR/L:.4f}): "
              f"C_2 retention {r[2]:.4f}")

    print("\n  [validation 4] the retained SW-only toy scripts/torus_quadrupole.py, and why it")
    print("                 differs: that toy applies a SHARP CONTINUUM CUTOFF at k_min and")
    print("                 integrates; a torus is a LATTICE, whose lowest shell sits AT k_min")
    print("                 carrying r3(1) = 6 modes' worth of k-cell volume.  The cutoff")
    print("                 estimate therefore OVERSTATES the suppression.  Both, side by side")
    print("                 (that toy's D = 14.0 Gpc, SW only):")
    for LD, booked in ((3.0, 0.83), (2.0, 0.49), (1.5, 0.19)):
        r = retention(LD * 14000.0, lmax=3, isw=False, chi_star=14000.0)
        cut = quad(lambda x: spherical_jn(2, x) ** 2 / x, 2 * np.pi / LD, 400, limit=400)[0]
        print(f"    L = {LD:.1f} D = {LD*14.0:>4.1f} Gpc: lattice sum {r[2]:.3f}   "
              f"sharp cutoff {cut*12:.3f}  [toy booked {booked}]")

    print("\n  [validation 5] the two independent paths to C_l(torus) agree — shell counts with")
    print("                 the addition theorem, vs a mode-by-mode sum over spherical harmonics")
    print("                 (L = 27.6 Gpc, |n| <= 20, SW+ISW):")
    idx0, M0 = covariance(L_FLOOR, nmax=20)
    r0 = retention(L_FLOOR, nmax=20)
    for l in range(LMIN, LMAX + 1):
        dg = np.real(np.array([M0[i, i] for i, (ll, _) in enumerate(idx0) if ll == l])).mean()
        ratio = dg / cl_infinite(l, umax=2 * np.pi * 20 * CHI_STAR / L_FLOOR)
        print(f"    l={l}: harmonic sum {ratio:.4f}   shell sum {r0[l]:.4f}   "
              f"ratio {ratio/r0[l]:.5f}")

    print("\n  [validation 6] ISW share of the infinite-universe C_l (ISW total / SW only):")
    for l in range(LMIN, LMAX + 1):
        print(f"    l={l}: C_l(SW+ISW)/C_l(SW) = {cl_infinite(l)/cl_infinite(l, isw=False):.4f}")

    print(f"\n  [validation 7] retention convergence in |n| (L = 27.6 Gpc, SW+ISW):")
    for nm in (40, 80, 120, 160):
        r = retention(L_FLOOR, lmax=3, nmax=nm)
        print(f"    |n| <= {nm:>3}: C_2 {r[2]:.4f}   C_3 {r[3]:.4f}")

    print("\n  ---- RESULT 1: RETENTION AT THE FLOOR  L = 27.6 Gpc ----")
    rsw = retention(L_FLOOR, isw=False)
    risw = retention(L_FLOOR, isw=True)
    print(f"    {'l':>3}{'SW only':>12}{'SW+ISW':>12}")
    for l in range(LMIN, LMAX + 1):
        print(f"    {l:>3}{rsw[l]:>12.3f}{risw[l]:>12.3f}")

    print("\n  retention vs box size (SW+ISW):")
    print(f"    {'L (Gpc)':>9}{'L/chi_*':>9}{'C_2':>9}{'C_3':>9}")
    for L in (27600.0, 30000.0, 35000.0, 42000.0, 55000.0, 80000.0):
        r = retention(L, lmax=3)
        print(f"    {L/1000:>9.1f}{L/CHI_STAR:>9.2f}{r[2]:>9.3f}{r[3]:>9.3f}")

    print("\n  ---- RESULT 2: POWER-SPECTRUM S/N over l = 2..6 (cosmic variance only) ----")
    tot = 0.0
    for l in range(LMIN, LMAX + 1):
        dev, cv = 1.0 - risw[l], np.sqrt(2.0 / (2 * l + 1))
        tot += (dev / cv) ** 2
        print(f"    l={l}: deficit {dev:+.4f}  cosmic variance {cv:.4f}  -> {dev/cv:+.3f} sigma")
    print(f"    total S/N = {np.sqrt(tot):.3f}")

    print(f"\n  ---- RESULT 3: OFF-DIAGONAL PATTERN at L = 27.6 Gpc, SW+ISW ----")
    for nm in (30, 40, NMAX_COV):
        idx, M = covariance(L_FLOOR, nmax=nm)
        R = rho_matrix(M)
        iu = np.triu_indices(len(idx), 1)
        rho = R[iu]
        sn = np.sqrt(np.sum(np.abs(rho) ** 2))
        print(f"    |n| <= {nm:>3}: pairs {len(rho)}  total S/N = sqrt(sum |rho|^2) = {sn:.3f}")
    print(f"    (C(45,2) = {45*44//2})")

    order = np.argsort(-np.abs(rho))[:14]
    print(f"\n    {'(l,m)':>10}   {'(l,m)':<10}{'rho':>9}")
    for o in order:
        i, j = iu[0][o], iu[1][o]
        print(f"    {str(idx[i]):>10} x {str(idx[j]):<10}{np.real(rho[o]):>+9.3f}")

    bad = [o for o in range(len(rho)) if abs(rho[o]) > 1e-6 and
           ((idx[iu[0][o]][1] - idx[iu[1][o]][1]) % 4 != 0 or
            (idx[iu[0][o]][0] - idx[iu[1][o]][0]) % 2 != 0)]
    print(f"\n    selection rule (Delta m = 0 mod 4 AND l - l' even): "
          f"{'HOLDS' if not bad else f'VIOLATED in {len(bad)} pairs'}")
    print(f"    pairs with |rho| > 1e-6: {int(np.sum(np.abs(rho) > 1e-6))} of {len(rho)}")
    print(f"    max |imag(rho)| = {np.max(np.abs(np.imag(rho))):.2e}  (octahedral symmetry -> real)")

    idx_s, M_s = covariance(L_FLOOR, isw=False, nmax=NMAX_COV)
    R_s = rho_matrix(M_s)
    rho_s = R_s[iu]
    print(f"\n    SW only, same |n| cutoff: total S/N = {np.sqrt(np.sum(np.abs(rho_s)**2)):.3f}")

    print("\n  the five pairs the corpus booked, recomputed.  NOTE on signs: the overall phase")
    print("  i^(l-l') is a convention, and dropping it flips exactly the l <-> l+/-2 entries and")
    print("  leaves the Delta-l = 0 entries alone — which is the whole of the sign difference below.")
    booked = {((4, -4), (4, 4)): 0.68, ((2, 2), (2, -2)): 0.65, ((3, 0), (5, 0)): 0.51,
              ((6, -6), (6, 6)): 0.50, ((3, -3), (5, 5)): -0.47}
    pos = {p: i for i, p in enumerate(idx)}
    print(f"    {'pair':>22}{'booked':>9}{'SW+ISW':>9}{'SW only':>9}")
    for (p, q), b in booked.items():
        print(f"    {str(p)+' x '+str(q):>22}{b:>+9.2f}"
              f"{np.real(R[pos[p], pos[q]]):>+9.3f}{np.real(R_s[pos[p], pos[q]]):>+9.3f}")
    print("=" * 78)


if __name__ == "__main__":
    main()
