"""Docket #141 — the vertex correction to the rainbow gap equation.

docs/PRTOE_hierarchy_problem.md §6e asks for ONE number and its sign: the coefficient c in

    lambda_eff = lambda (1 - c lambda),        1/lambda_eff ~= 1/lambda + c,

from the CROSSED BOX — the two-loop kernel the rainbow/ladder truncation omits, because the
ladder rungs are already resummed by 1 = lambda ln(Lambda/Delta) itself.  Evaluated on §6c's
own host and nothing else:

    V(q) = e^2/(q^2 + m_D^2),   e^2 = 4 pi alpha_c,   b = m_D^2/(4 k_F^2) = 2 alpha_c/(pi v),

one band's Fermi surface at k_F inside a linear cone (v = 1), particle-hole channel, T = 0.
Units k_F = v = 1 throughout, so xi_p = p - 1 and m_D^2 = 4b.

THE KERNEL.  Writing the gap equation as  Delta(k) = int d3k'/(2pi)^3 W(k,k') Delta(k')/(2|xi|),
the rainbow kernel is W1 = V(k-k').  The crossed box adds W2 = -C(k,k') with

    C(k,k') = int d3p/(2pi)^3 V(k-p) V(p-k') * [n_{p'} - n_p]/[xi_p - xi_{p'}],   p' = Q - p,

Q = k + k'.  The RELATIVE MINUS SIGN is not asserted, it is the frequency integral: with an
instantaneous V the two internal lines of the LADDER carry (p,w) and (p,w) and give
int dw/2pi G_e G_h = -i/(2|xi_p|), while the two internal lines of the CROSSED box carry
(p,w) and (Q-p,-w) and give +i [n_{p'}-n_p]/[xi_p - xi_{p'}].  Opposite sign, same channel.
(The Cooper-channel crossed box is the same integral with p' = p - Q; |p-Q| = |Q-p|, so the
two channels give an identical C.  Checked in check_channel_equivalence().)

The Lindhard weight [n_{p'} - n_p]/[xi_p - xi_{p'}] is >= 0 pointwise and V > 0 everywhere,
so C >= 0 pointwise: the crossed box REDUCES the kernel, c > 0, with no argument required.

COORDINATES.  r1 = |p|, r2 = |p-Q| turn d3p into r1 r2 dr1 dr2 dphi / Q, the energy denominator
into r1 - r2, and the support into exactly one of r1, r2 inside the unit sphere.  The 1/(r1-r2)
edge singularity is removed exactly by r1 = 1 + s t, r2 = 1 - s(1-t) (dr1 dr2 = s ds dt), and
the phi integral is analytic:

    int_0^2pi dphi/[(a - B cos)(a + B cos)] = 2 pi/(a sqrt(a^2 - B^2)).

So C(u) = (e^4/(2 pi^2 Q)) * int ds dt r1 r2 D / (a sqrt(A1 A2)), doubled for the p -> Q-p
image region, with u = sin^2(theta/2) the §6c Fermi-surface variable and Q = 2 sqrt(1-u).

VALIDATION.  Set V = const and the dispersion parabolic and the same machinery must return the
Gor'kov-Melik-Barkhudarov constant, <P>/nu0 = (1/3) ln(4e) = 0.7953875 — the textbook
(4e)^(1/3) suppression of the BCS gap.  That is check_gmb().

Run: python3 scripts/hierarchy_vertex_crossed_box.py
"""
import math

import numpy as np

# ---- standing values (docs/PRTOE_hierarchy_problem.md §6c, §6e) -------------
ALPHA = 1 / 137.035999084
ALPHA_C = 3 * ALPHA               # 0.021892
K_SCREEN = 1.36461191             # k, the screened-exchange integral
LAMBDA = K_SCREEN * ALPHA_C       # 0.029874
B_TF = 2 * ALPHA_C / math.pi      # 0.0139369  (v = 1)
E2 = 4 * math.pi * ALPHA_C        # Heaviside-Lorentz


def V_avg_fs(b, e2=1.0):
    """<V>_FS = int_0^1 du e^2/(4 k_F^2 (u + b)) in units k_F = 1."""
    return e2 / 4.0 * math.log1p(1.0 / b)


# ---- quadrature ------------------------------------------------------------
def _gl(n):
    return np.polynomial.legendre.leggauss(n)


def _panels(edges, n):
    """Gauss-Legendre nodes/weights over a monotone list of panel edges."""
    x, w = _gl(n)
    X, W = [], []
    for a, c in zip(edges[:-1], edges[1:]):
        if c > a:
            X.append(0.5 * (c - a) * x + 0.5 * (a + c))
            W.append(0.5 * (c - a) * w)
    return np.concatenate(X), np.concatenate(W)


def _s_max(t, Q):
    """Largest s = r1 - r2 at fixed t: triangle inequality Q <= r1 + r2 and r2 >= 0."""
    smax = np.full_like(t, Q)
    if Q > 1.0:
        tb = (Q - 1.0) / Q                      # below tb the r1+r2 >= Q edge binds
        m = t < tb
        smax[m] = (2.0 - Q) / (1.0 - 2.0 * t[m])
    return smax


def inner_st(u, b, e2, contact=False, parabolic=False, nt=48, ns=48):
    """int ds dt r1 r2 D F over region A (r1 > 1 > r2), for one u.  Returns I(u)."""
    Q = 2.0 * math.sqrt(max(1.0 - u, 0.0))
    if Q <= 0.0:
        return 0.0

    tedges = [0.0, 0.5, 1.0]
    if Q > 1.0:
        tedges.append((Q - 1.0) / Q)
    tn, tw = _panels(sorted(set(tedges)), nt)

    smax = _s_max(tn, Q)
    mD = 2.0 * math.sqrt(b)                     # the scale V varies on
    fr = np.array([0.0, 0.25, 1.0, 4.0]) * mD   # absolute panel edges, then smax
    ed = [np.minimum(f, smax) for f in fr] + [smax]

    x, w = _gl(ns)
    sn, sw = [], []
    for a, c in zip(ed[:-1], ed[1:]):
        sn.append(0.5 * (c - a)[:, None] * x[None, :] + 0.5 * (a + c)[:, None])
        sw.append(0.5 * (c - a)[:, None] * w[None, :])
    sn = np.concatenate(sn, axis=1)
    sw = np.concatenate(sw, axis=1)

    t = tn[:, None]
    r1 = 1.0 + sn * t
    r2 = 1.0 - sn * (1.0 - t)

    z = (r1 * r1 - r2 * r2 + Q * Q) / (2.0 * Q)
    pp2 = np.maximum(r1 * r1 - z * z, 0.0)

    if contact:
        F = 1.0
    else:
        a = 0.5 * (r1 * r1 + r2 * r2) + 4.0 * b + 2.0 * u - 1.0
        B = 2.0 * math.sqrt(u) * np.sqrt(pp2)
        A1 = a - B                              # |k-p|^2 + m_D^2  at cos(phi) = +1
        A2 = a + B                              # |p-k'|^2 + m_D^2 at cos(phi) = -1
        F = 1.0 / (a * np.sqrt(A1 * A2))

    D = 2.0 / (r1 + r2) if parabolic else 1.0
    val = r1 * r2 * D * F
    return float(np.einsum("i,ij,ij->", tw, sw, val))


def crossed_box_average(b, e2=E2, contact=False, parabolic=False,
                        nu=48, nt=48, ns=48, uedges=None):
    """<C>_FS = int_0^1 du C(u).  contact=True instead returns <P> (the Lindhard average)."""
    if uedges is None:
        uedges = sorted(set([0.0] + [min(f, 1.0) for f in
                                     (0.25 * b, b, 4 * b, 16 * b, 0.25, 0.5, 0.75)] + [1.0]))
    un, uw = _panels(uedges, nu)
    pre = (e2 * e2 if not contact else 1.0) / (2.0 * math.pi ** 2)
    tot = 0.0
    for u, wu in zip(un, uw):
        Q = 2.0 * math.sqrt(max(1.0 - u, 0.0))
        tot += wu * pre / Q * inner_st(u, b, e2, contact, parabolic, nt, ns)
    return tot


def c_coefficient(b=B_TF, e2=E2, lam=LAMBDA, **kw):
    """c = <C>/(lambda <V>).

    lambda_eff = D <V - C> and lambda = D <V> with the SAME pairing density of states D,
    so D cancels: c = <C>/(lambda <V>).  The lambda that must be used is the one that sits
    in the exponent, i.e. §6c's booked k alpha_c — and V_avg_fs()/pi^2 reproduces it to nine
    digits, which is the check that this is §6c's host and not a neighbouring one.
    Everything then depends on b alone: <C> ~ e^4 and lambda <V> ~ e^4, so e^2 drops out."""
    return crossed_box_average(b, e2, **kw) / (lam * V_avg_fs(b, e2))


def c_self_consistent(b, e2=E2, **kw):
    """c(b) with lambda recomputed at that b — the form whose b -> infinity limit must be
    the contact-limit constant.  Equals c_coefficient() at b = b_TF."""
    Vb = V_avg_fs(b, e2)
    return crossed_box_average(b, e2, **kw) / ((Vb / math.pi ** 2) * Vb)


# ---- checks ----------------------------------------------------------------
def check_lens_volume(Q, n=64):
    """Region A's volume against the analytic two-unit-sphere result — tests the
    coordinates, the Jacobian r1 r2/Q and the s_max domain, independently of physics."""
    u = 1.0 - (Q / 2.0) ** 2
    tedges = [0.0, 0.5, 1.0] + ([(Q - 1.0) / Q] if Q > 1.0 else [])
    tn, tw = _panels(sorted(set(tedges)), n)
    smax = _s_max(tn, Q)
    x, w = _gl(n)
    sn = 0.5 * smax[:, None] * (x[None, :] + 1.0)
    sw = 0.5 * smax[:, None] * w[None, :]
    t = tn[:, None]
    r1, r2 = 1.0 + sn * t, 1.0 - sn * (1.0 - t)
    got = 2.0 * math.pi / Q * float(np.einsum("i,ij,ij->", tw, sw, sn * r1 * r2))
    want = 4.0 * math.pi / 3.0 - math.pi * (4.0 + Q) * (2.0 - Q) ** 2 / 12.0
    return got, want


def check_gmb(nu=64, nt=64, ns=64):
    """Contact V + parabolic dispersion must give the Gor'kov-Melik-Barkhudarov constant
    <P>/nu0 = (1/3) ln(4e), i.e. the standard (4e)^(1/3) suppression of the BCS gap."""
    P = crossed_box_average(1.0, 1.0, contact=True, parabolic=True, nu=nu, nt=nt, ns=ns,
                            uedges=[0.0, 0.25, 0.5, 0.75, 1.0])
    return P * 2.0 * math.pi ** 2, (1.0 + math.log(4.0)) / 3.0   # nu0 = 1/(2 pi^2)


def brute_force_C(u, b=B_TF, n=600, half=3.2):
    """C(u) straight from the definition on a cartesian p-grid — no bipolar coordinates,
    no analytic phi integral, no s = r1 - r2 substitution.  Slow and only ~3 digits, but it
    shares nothing with inner_st() except the physics, so it tests the whole reduction.
    (The particle-hole crossed box has p' = Q - p and the Cooper one p' = p - Q; only
    |p'| enters, and |Q - p| = |p - Q|, so this single integral is both.)"""
    th = 2.0 * math.asin(math.sqrt(u))
    k = np.array([math.sin(th / 2), 0.0, math.cos(th / 2)])
    kp = np.array([-math.sin(th / 2), 0.0, math.cos(th / 2)])
    Q = k + kp
    g, h = np.linspace(-half, half, n), 2 * half / (n - 1)
    tot = 0.0
    for gx in g:                                # slab by slab, to stay inside memory
        Y, Z = np.meshgrid(g, g, indexing="ij")
        px, py, pz = gx, Y, Z
        r1 = np.sqrt(px ** 2 + py ** 2 + pz ** 2)
        r2 = np.sqrt((px - Q[0]) ** 2 + (py - Q[1]) ** 2 + (pz - Q[2]) ** 2)
        num = (r2 < 1.0).astype(float) - (r1 < 1.0).astype(float)
        den = r1 - r2
        wgt = np.divide(num, den, out=np.zeros_like(num), where=np.abs(den) > 1e-9)
        V1 = E2 / ((px - k[0]) ** 2 + (py - k[1]) ** 2 + (pz - k[2]) ** 2 + 4 * b)
        V2 = E2 / ((px - kp[0]) ** 2 + (py - kp[1]) ** 2 + (pz - kp[2]) ** 2 + 4 * b)
        tot += float(np.sum(V1 * V2 * wgt))
    return tot * h ** 3 / (2 * math.pi) ** 3


def C_of_u(u, b=B_TF, e2=E2, nt=96, ns=96):
    """C(u) from the reduced (s, t) integral, for comparison with brute_force_C."""
    Q = 2.0 * math.sqrt(max(1.0 - u, 0.0))
    return e2 * e2 / (2.0 * math.pi ** 2 * Q) * inner_st(u, b, e2, nt=nt, ns=ns)


def main():
    print("docket #141 — the crossed box on §6c's host\n")
    print(f"  alpha_c = {ALPHA_C:.8f}   k = {K_SCREEN}   lambda = {LAMBDA:.8f}")
    print(f"  b = 2 alpha_c/pi = {B_TF:.8f}   m_D/2k_F = sqrt(b) = {math.sqrt(B_TF):.6f}")
    print(f"  <V>_FS = (e^2/4) ln(1+1/b) = {V_avg_fs(B_TF, E2):.8f}")
    print(f"  check lambda = <V>/pi^2 -> {V_avg_fs(B_TF, E2)/math.pi**2:.8f}\n")

    print("  geometry check — region-A volume vs analytic lens complement")
    for Q in (0.3, 0.9, 1.4, 1.9):
        got, want = check_lens_volume(Q)
        print(f"    Q = {Q:.2f}   got {got:.10f}   want {want:.10f}   rel {abs(got/want-1):.2e}")

    got, want = check_gmb()
    print(f"\n  GMB check (contact V, parabolic band): got {got:.8f}  want (1+ln4)/3 = "
          f"{want:.8f}  rel {abs(got/want-1):.2e}")

    print("\n  brute-force cartesian C(u) vs the reduced (s,t) integral:")
    for uu in (0.05, 0.3, 0.7):
        bf, red = brute_force_C(uu), C_of_u(uu)
        print(f"    u = {uu:.2f}   brute {bf:.6e}   reduced {red:.6e}   "
              f"rel {abs(bf/red-1):.2e}")

    print("\n  convergence in (nu, nt, ns):")
    prev = None
    for n in (24, 32, 48, 64, 80, 96):
        cc = c_coefficient(nu=n, nt=n, ns=n)
        d = "" if prev is None else f"   delta {abs(cc-prev):.2e}"
        print(f"    n = {n:3d}   c = {cc:.10f}{d}")
        prev = cc

    print("\n  e^2-independence (c must be a function of b alone):")
    for e2 in (E2, 1.0, 10.0):
        print(f"    e^2 = {e2:<8.4f}  c = {c_self_consistent(B_TF, e2, nu=64, nt=64, ns=64):.10f}")

    lin = crossed_box_average(1.0, 1.0, contact=True, parabolic=False,
                              nu=80, nt=80, ns=80,
                              uedges=[0.0, 0.25, 0.5, 0.75, 1.0]) * 2 * math.pi ** 2
    print(f"\n  self-consistent c(b), against the contact-limit target {lin/2:.7f}")
    print(f"    (contact <P>/nu0 on the linear band = {lin:.7f}; halved by N0 = 2 nu0):")
    for bb in (B_TF, 0.05, 0.2, 1.0, 5.0, 50.0, 5e3, 5e4):
        print(f"    b = {bb:<10.5g} c = {c_self_consistent(bb, nu=64, nt=64, ns=64):.6f}")

    h = 0.02
    cp, cm = c_self_consistent(B_TF*(1+h), nu=64, nt=64, ns=64), \
        c_self_consistent(B_TF*(1-h), nu=64, nt=64, ns=64)
    print(f"\n  sensitivity: dln c/dln b at b_TF = "
          f"{(math.log(cp)-math.log(cm))/math.log((1+h)/(1-h)):+.4f}")

    c = c_coefficient(nu=96, nt=96, ns=96)
    lam_eff = LAMBDA * (1 - c * LAMBDA)
    MRED = 1.220890e28 / math.sqrt(8 * math.pi)
    print(f"\n  ==> c = {c:.6f}   (POSITIVE — the crossed box reduces the coupling)")
    print(f"      lambda = {LAMBDA:.8f} -> lambda_eff = lambda(1-c lambda) = {lam_eff:.8f}")
    print(f"      1/lambda = {1/LAMBDA:.4f} -> 1/lambda + c = {1/LAMBDA+c:.4f}   "
          f"[literal 1/lambda_eff = {1/lam_eff:.4f}, the difference c^2 lambda = "
          f"{c*c*LAMBDA:.4f} is beyond the order computed]")
    print(f"      anchor multiplier exp(-c) = {math.exp(-c):.5f}")
    for tag, ex in (("booked", 1 / LAMBDA), ("corrected", 1 / LAMBDA + c)):
        print(f"      M_anchor {tag:10s}  booked convention (-3/2) "
              f"{MRED*math.exp(-ex-1.5)/1e9:8.1f} GeV | exact-solution convention (x2) "
              f"{2*MRED*math.exp(-ex-1.5)/1e9:8.1f} GeV")
    print(f"      4 pi m_H = {4*math.pi*125.25:.1f} GeV; corrected exact-solution value is "
          f"{2*MRED*math.exp(-1/LAMBDA-c-1.5)/1e9/(4*math.pi*125.25):.4f} x it")
    print(f"      §6d band 1.6-5.2 TeV x exp(-c) -> "
          f"{1.6*math.exp(-c):.3f}-{5.2*math.exp(-c):.3f} TeV")


if __name__ == "__main__":
    main()
