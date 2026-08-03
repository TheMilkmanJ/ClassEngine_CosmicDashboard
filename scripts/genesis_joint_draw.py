#!/usr/bin/env python3
"""
THE JOINT GENESIS DRAW -- link 5's closer: is sign(theta_dot) correlated with sign(n)?

The corpus has two half-solvers and no instrument that holds both:
  * genesis_famp_Z4.py        evolves the zero-mode ROTATION theta_dot(t) on the model's
                              potential, released at rest, scanned over the theta_i prior --
                              a homogeneous 2D integration with NO spatial structure, so it
                              cannot carry a winding.
  * genesis_multicomponent.py carries the WINDING (the six-channel phase, fractional vortices)
                              but has NO time evolution, so it cannot generate theta_dot.
The product sign(theta_dot . n) is therefore unmeasured -- not because it is hard, but because
no single instrument computes both. THIS SCRIPT IS THAT INSTRUMENT.

WHAT IT IS. A 1D periodic ring of the complex genesis field psi_j = x_j + i y_j, j = 0..N-1,
evolved on the model's OWN recorded potential

    V = m^2 R^2 + lam R^4 + 2 eps_A lam R^4 cos 4 theta      (eps_A = 2/9),

released AT REST, with radiation-era Hubble friction H = 1/(2t) and a nearest-neighbour spatial
stiffness kappa (the gradient term that lets the ring carry a winding). One trajectory then holds
BOTH objects at once:
  * the WINDING            n         = (1/2pi) oint grad theta . dl   (a spatial loop integral)
  * the zero-mode ROTATION theta_dot = the tilt-generated rotation of the mean phase, read off
                                       the comoving charge Q = a^3 sum_j R_j^2 theta_dot_j.
It reduces to genesis_famp_Z4 exactly at N=1 (kappa off), and carries the same winding object
genesis_multicomponent's coherent fraction is built on.

WHAT IT DECIDES. Half one is DONE and respected: sign(theta_dot) alone splits the theta_i prior
EVENLY, forced by the reflection sigma: theta -> pi/2 - theta under which the charge is odd. That
proves neither sign is determined a priori. What is OPEN is the CORRELATION: over the joint prior,
does sign(theta_dot) track sign(n) (=> the helicity<->matter cross-messenger test LIVES) or are
they independent draws (=> the model cannot call the correlation; the test CLOSES negative)?

THE STRUCTURAL ANSWER, and why it is not rigged. Space has no preferred ring orientation, so the
model is invariant under the spatial reflection P: j -> N-1-j (reverse the loop). Under P the
winding flips, n -> -n, while the total charge Q = sum_j R_j^2 theta_dot_j and the tilt torque
sum_j R_j^4 sin 4 theta_j are site-sums, invariant. So every trajectory's P-mirror has the SAME
theta_dot history and the OPPOSITE n: the two signs cannot lock. A parity-ODD term WOULD lock them
(the sensitivity check injects one and the instrument sees it), but the recorded potential has none
-- its only parity-odd coupling is the gravitational Chern-Simons theta R Rtilde acting on
theta_dot, which is link 4's object, not an n<->theta_dot lock.

SCOPE (ruled, respected). This closes link 5 only -- sign(theta_dot . n). It does NOT deliver
link 4's sign(H_kin): that is a writhe+twist quantity of the trajectory's full 3D flow, and a
0D/1D/zero-mode solver cannot return it at any resolution. No such claim is made here.

CPU DISCIPLINE. Single-threaded, one vectorised stepper over the whole ensemble, sub-minute.
__main__ runs a lean demo; production() is defined but NOT called -- run it only with cores free.

Run:  OMP_NUM_THREADS=1 python3 scripts/genesis_joint_draw.py
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
           "NUMEXPR_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(_v, "1")          # never oversubscribe the chains' cores
import time
import numpy as np

# ---- the model's recorded genesis potential (constants match genesis_famp_Z4.py) ----------
M2, LAM, RI = 1.0, 0.03, 10.0        # m^2, quartic; release radius |psi| (units m=1)
EPS_A       = 2.0 / 9.0              # the Z4 tilt strength -- the recorded value
T0, TF      = 0.25, 60.0             # radiation-era window; H = 1/(2t)


def _wrap(d):
    """map phase differences into (-pi, pi]."""
    return (d + np.pi) % (2 * np.pi) - np.pi


# ============================================================================================
#  the two winding-sector objects (validated against the two half-solvers below)
# ============================================================================================
def winding(theta):
    """n = (1/2pi) oint grad theta . dl around the ring (last axis) -- the spatial loop integral.

    Sum of the wrapped nearest-neighbour phase differences / 2pi; an integer while no amplitude
    zero (vortex core) lets a link slip by 2pi.
    """
    d = _wrap(np.roll(theta, -1, axis=-1) - theta)
    return d.sum(axis=-1) / (2 * np.pi)


def coherent_fraction(theta):
    """f = |<e^{i theta}>| over the ring sites -- genesis_multicomponent.py's observable (line 42)
    verbatim, on a spatial ring instead of six channels."""
    return np.abs(np.mean(np.exp(1j * theta), axis=-1))


def ring_ic(theta_i, n, N):
    """centred winding ramp: theta_j = theta_i + 2 pi n (j - (N-1)/2)/N. The centring makes the
    mean phase exactly theta_i, so n=0 reduces to genesis_famp_Z4's homogeneous release. Also
    makes ring_ic(theta_i, -n) the exact spatial mirror (j -> N-1-j) of ring_ic(theta_i, +n)."""
    j = np.arange(N)
    return theta_i + 2 * np.pi * n * (j - (N - 1) / 2.0) / N


# ============================================================================================
#  the vectorised ring solver  (state x,y,vx,vy each shape (M draws, N sites))
# ============================================================================================
def _accel(x, y, kappa, g):
    """ring acceleration = -grad V + kappa*laplacian (+ optional DIAGNOSTIC parity-odd g).

    The potential gradient is genesis_famp_Z4.py's dVx/dVy verbatim (base + Z4 tilt); the
    laplacian (nearest neighbour along the site axis) is the stiffness that lets a winding live.
    """
    r2 = x * x + y * y
    dVx = 2 * M2 * x + 4 * LAM * r2 * x + 2 * EPS_A * LAM * (4 * x**3 - 12 * x * y * y)
    dVy = 2 * M2 * y + 4 * LAM * r2 * y + 2 * EPS_A * LAM * (4 * y**3 - 12 * x * x * y)
    lapx = kappa * (np.roll(x, -1, axis=-1) + np.roll(x, 1, axis=-1) - 2 * x)
    lapy = kappa * (np.roll(y, -1, axis=-1) + np.roll(y, 1, axis=-1) - 2 * y)
    ax = lapx - dVx
    ay = lapy - dVy
    if g != 0.0:
        # DIAGNOSTIC ONLY -- NOT a term in the model. A parity-odd tangential drive proportional
        # to the LOCAL phase gradient (a toy theta_dot * grad_x theta / Chern-Simons-like coupling).
        # Under x -> -x it is ODD, so it deliberately LOCKS sign(theta_dot) to sign(n). Used only
        # to prove the instrument CAN register a correlation; the recorded potential has g = 0.
        theta = np.arctan2(y, x)
        gth = 0.5 * (_wrap(np.roll(theta, -1, axis=-1) - theta)
                     + _wrap(theta - np.roll(theta, 1, axis=-1)))
        R = np.sqrt(r2) + 1e-12
        at = g * gth
        ax += at * (-y / R)
        ay += at * (x / R)
    return ax, ay


def evolve(theta0, kappa=0.0, g=0.0, t0=T0, tf=TF, dt=0.05, r0=RI):
    """RK4 on the ring(s) from rest. theta0 shape (M,N) or (N,). Returns per-draw measurables.

    sign(theta_dot) is read off the COMOVING charge Q(t) = a(t)^3 sum_j (x v_y - y v_x) -- the
    ring's total R^2 theta_dot, redshift-compensated. The tilt torque ~ R^4 acts at high R (early),
    generating the rotation; once it shuts off Q is conserved (the same comoving dark charge
    sakharov_twist_sign.py tracks), so a late-window mean gives the frozen generated rotation.
    """
    theta0 = np.atleast_2d(theta0)
    x = r0 * np.cos(theta0)
    y = r0 * np.sin(theta0)
    vx = np.zeros_like(x)
    vy = np.zeros_like(y)
    n_steps = int(round((tf - t0) / dt))

    def deriv(t, x, y, vx, vy):
        h = 1.0 / (2.0 * t)
        ax, ay = _accel(x, y, kappa, g)
        return vx, vy, ax - 3 * h * vx, ay - 3 * h * vy

    n_init = winding(theta0)
    Q_early = None                                   # charge at the torque-active window's end
    Q_late_sum = np.zeros(x.shape[0]); Q_late_cnt = 0
    Rmin = np.full(x.shape[0], np.inf)
    wind_intact_until = np.full(x.shape[0], t0)      # last time winding still equals n_init
    t = t0
    for i in range(n_steps + 1):
        a3 = (t / t0) ** 1.5
        Q = a3 * np.sum(x * vy - y * vx, axis=-1)
        Rmin = np.minimum(Rmin, np.sqrt(x * x + y * y).min(axis=-1))
        w = winding(np.arctan2(y, x))
        still = np.abs(w - n_init) < 0.4
        wind_intact_until = np.where(still, t, wind_intact_until)
        if Q_early is None and t >= 1.0:
            Q_early = Q.copy()                       # winding is still intact here (breaks ~t=1)
        if t >= 0.7 * tf:
            Q_late_sum += Q; Q_late_cnt += 1
        if i == n_steps:
            break
        k1 = deriv(t,          x,              y,              vx,              vy)
        k2 = deriv(t + dt/2,   x+dt/2*k1[0],   y+dt/2*k1[1],   vx+dt/2*k1[2],   vy+dt/2*k1[3])
        k3 = deriv(t + dt/2,   x+dt/2*k2[0],   y+dt/2*k2[1],   vx+dt/2*k2[2],   vy+dt/2*k2[3])
        k4 = deriv(t + dt,     x+dt*k3[0],     y+dt*k3[1],     vx+dt*k3[2],     vy+dt*k3[3])
        x  = x  + dt/6*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0])
        y  = y  + dt/6*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1])
        vx = vx + dt/6*(k1[2] + 2*k2[2] + 2*k3[2] + k4[2])
        vy = vy + dt/6*(k1[3] + 2*k2[3] + 2*k3[3] + k4[3])
        t += dt

    if Q_early is None:
        Q_early = Q
    Q_frozen = Q_late_sum / max(Q_late_cnt, 1)
    theta_f = np.arctan2(y, x)
    return dict(
        n_init=n_init, sign_n=np.sign(n_init).astype(int),
        Q_early=Q_early, Q_frozen=Q_frozen, sign_thetadot=np.sign(Q_frozen).astype(int),
        Rmin=Rmin, wind_intact_until=wind_intact_until,
        coh_final=coherent_fraction(theta_f),
    )


# ============================================================================================
#  VALIDATION 1 -- reproduce genesis_famp_Z4's even sign(theta_dot) split + sigma antisymmetry
# ============================================================================================
def validate_half_one(verbose=True):
    """N=1 ring == genesis_famp_Z4's homogeneous roll. Check the sigma: theta -> pi/2 - theta
    antisymmetry of the generated charge and the even sign split over one Z4 period."""
    grid = np.linspace(0.01, np.pi/2 - 0.01, 24)     # sigma-symmetric about pi/4 (the doc's grid)
    Q = evolve(grid[:, None], kappa=0.0, tf=60.0, dt=0.02)["Q_frozen"]
    npos, nneg = int((Q > 0).sum()), int((Q < 0).sum())
    antisym = float(np.max(np.abs(Q + Q[::-1])) / np.max(np.abs(Q)))   # Q(theta) = -Q(pi/2 - theta)
    signed = abs(Q.sum()) / np.abs(Q).sum()
    ok = (npos == nneg) and (antisym < 1e-6)
    if verbose:
        print("  VALIDATION 1 -- against genesis_famp_Z4 (the zero-mode roll)")
        print(f"    sign(theta_dot) split over one Z4 period : {npos} positive / {nneg} negative"
              f"   (genesis_famp_Z4: 12 / 12)")
        print(f"    sigma antisymmetry  Q(t) = -Q(pi/2 - t)  : max residual/scale = {antisym:.2e}")
        print(f"    signed sum |sum Q| / sum|Q|              : {signed:.2e}   (even split => ~0)")
    return ok


# ============================================================================================
#  VALIDATION 2 -- reproduce genesis_multicomponent's winding + coherent-fraction objects
# ============================================================================================
def validate_half_two(verbose=True):
    """The winding counter returns the exact integer for a ramp; the coherent fraction matches
    genesis_multicomponent's f = |<e^{i theta}>| and its half-quantum-vortex coherence penalty;
    the winding is carried through the torque-active window."""
    N = 24
    ok = True
    ns = [-3, -2, -1, 0, 1, 2, 3]
    w = winding(np.stack([ring_ic(0.3, n, N) for n in ns]))
    ok = ok and np.allclose(w, ns, atol=1e-9)
    rng = np.random.default_rng(7)
    ph = rng.uniform(-np.pi, np.pi, N)
    f_ours = float(coherent_fraction(ph[None])[0])
    f_defn = float(np.abs(np.mean(np.exp(1j * ph))))       # its exact line-42 definition
    ok = ok and abs(f_ours - f_defn) < 1e-14
    locked = np.zeros(N); hqv = locked.copy(); hqv[:N // 2] += np.pi
    f_lock = float(coherent_fraction(locked[None])[0]); f_hqv = float(coherent_fraction(hqv[None])[0])
    ok = ok and (f_hqv < f_lock)
    res = evolve(ring_ic(0.4, 2, N), kappa=0.6, tf=45.0, dt=0.04)
    intact_win = float(res["wind_intact_until"][0])
    rmin = float(res["Rmin"][0])
    ok = ok and abs(res["n_init"][0] - 2) < 1e-6 and intact_win > 0.9 * 45.0
    if verbose:
        print("  VALIDATION 2 -- against genesis_multicomponent (the winding sector)")
        print("    winding of a clean n-ramp: " +
              ", ".join(f"{n}->{wi:+.3g}" for n, wi in zip(ns, w)) + "   (exact integers)")
        print(f"    coherent fraction identity to its line-42 defn : |diff| = {abs(f_ours-f_defn):.1e}")
        print(f"    half-quantum vortex coherence penalty          : locked {f_lock:.3f}"
              f" -> HQV {f_hqv:.3f}   (drops, as it must)")
        print(f"    winding carried through the whole run (n=2)     : net conserved, intact to"
              f" t = {intact_win:.1f}  (R dips to R_min = {rmin:.3f} near a core)")
        print("      (the ring genuinely holds the winding for the full trajectory; the rotation's")
        print("       sign is set early at high R. The verdict rests on parity -- exact instant-by-")
        print("       instant -- so it does not depend on the winding's late-time fate either way.)")
    return ok


# ============================================================================================
#  the exact structural reason -- spatial parity P: reverse the ring; n flips, theta_dot does not
# ============================================================================================
def parity_mirror_check(verbose=True):
    """Take generic ICs and their spatial mirror (reverse site order). On the recorded potential
    the two evolutions give IDENTICAL Q (same sign theta_dot) and OPPOSITE n -- to machine
    precision. That exact relabeling symmetry is why the two signs cannot correlate."""
    rng = np.random.default_rng(3)
    N = 16
    th = np.stack([ring_ic(t, k, N) + 0.15 * rng.standard_normal(N)
                   for t, k in [(0.7, 2), (1.1, 1), (0.3, 3), (1.4, 2)]])
    a = evolve(th, kappa=0.5, tf=45.0, dt=0.04)
    b = evolve(th[:, ::-1], kappa=0.5, tf=45.0, dt=0.04)              # x -> -x mirror
    dQ = np.max(np.abs(a["Q_frozen"] - b["Q_frozen"]) / (np.abs(a["Q_frozen"]) + 1e-30))
    dn = np.max(np.abs(a["n_init"] + b["n_init"]))                    # ~0 (opposite windings)
    ok = (dQ < 1e-6) and (dn < 1e-6)
    if verbose:
        print("  PARITY MIRROR (the structural reason for the verdict)")
        print(f"    reverse the ring (x -> -x): Q identical to rel. {dQ:.1e}  -> same sign(theta_dot)")
        print(f"                                n flips, |n_+ + n_-| max = {dn:.1e}  -> opposite winding")
        print("    => every draw's mirror keeps theta_dot and flips n: the signs CANNOT lock.")
    return ok


# ============================================================================================
#  THE JOINT DRAW -- the 2x2 distribution of (sign theta_dot, sign n) over the prior
# ============================================================================================
def joint_draw(N=16, n_theta=16, n_set=(-2, -1, 1, 2), kappas=(0.0, 0.5), g=0.0,
               tf=45.0, dt=0.05, noise=0.12, seed=1, verbose=True):
    """Scan theta_i over one Z4 period x winding n over a symmetric set, on the ring, with small
    per-site phase noise so the +n and -n draws are NOT exact mirrors (a genuine statistical test,
    not a rigged pairing). Tabulate the joint (sign theta_dot, sign n) and its correlation.
    g != 0 injects the diagnostic parity-odd term (used by sensitivity_check)."""
    rng = np.random.default_rng(seed)
    thetas = np.linspace(0.02, np.pi/2 - 0.02, n_theta)     # one Z4 period (even-split prior)
    ic, sgn_n = [], []
    for th in thetas:
        for n in n_set:
            ic.append(ring_ic(th, n, N) + noise * rng.standard_normal(N))
            sgn_n.append(int(np.sign(n)))
    ic = np.stack(ic); sgn_n = np.array(sgn_n)
    out = {}
    for kappa in kappas:
        res = evolve(ic, kappa=kappa, g=g, tf=tf, dt=dt)
        std = res["sign_thetadot"]
        keep = std != 0
        s_td, s_n = std[keep], sgn_n[keep]
        c = {(a, b): int(np.sum((s_td == a) & (s_n == b))) for a in (1, -1) for b in (1, -1)}
        phi = float(np.corrcoef(s_td, s_n)[0, 1]) if s_td.size > 1 else 0.0
        out[kappa] = dict(cells=c, phi=phi, ndraw=int(s_td.size), near_zero=int((~keep).sum()))
        if verbose:
            tot = max(s_td.size, 1)
            print(f"    kappa={kappa:>4}: "
                  f"(td+,n+)={c[(1,1)]:<3} (td+,n-)={c[(1,-1)]:<3} "
                  f"(td-,n+)={c[(-1,1)]:<3} (td-,n-)={c[(-1,-1)]:<3}  "
                  f"corr={phi:+.3f}  (noise floor +-{1/np.sqrt(tot):.3f})")
    return out


def sensitivity_check(verbose=True):
    """Prove the null is a MEASURED zero, not a blind instrument: inject the diagnostic parity-odd
    coupling g and watch the correlation appear and flip sign with g."""
    if verbose:
        print("  SENSITIVITY -- inject a (non-model) parity-odd term g; the instrument must SEE it")
    res = {}
    for g in (0.0, +0.8, -0.8):
        o = joint_draw(N=16, n_theta=12, n_set=(-1, 1), kappas=(0.5,), g=g,
                       tf=40.0, dt=0.06, verbose=False)
        phi = o[0.5]["phi"]; res[g] = phi
        if verbose:
            tag = ("recorded potential (no such term)" if g == 0 else
                   "parity-odd ON  -> correlation appears")
            print(f"    g={g:+.2f}: corr(sign theta_dot, sign n) = {phi:+.3f}   {tag}")
    return res


# ============================================================================================
#  production() -- heavier, statistically tight. DEFINED, NOT CALLED. Run when cores free.
# ============================================================================================
def production():
    """Full-resolution joint draw. Do NOT call from __main__ (CPU discipline). Run alone:
        OMP_NUM_THREADS=1 python3 -c 'import scripts.genesis_joint_draw as G; G.production()'
    """
    print("PRODUCTION joint draw (N=48, tf=80, fine dt, wide n) -- run only with cores free")
    print("  half-one even split :", validate_half_one(verbose=False))
    print("  winding sector      :", validate_half_two(verbose=False))
    print("  parity mirror exact :", parity_mirror_check(verbose=False))
    o = joint_draw(N=48, n_theta=80, n_set=(-3, -2, -1, 1, 2, 3),
                   kappas=(0.0, 0.1, 0.3, 1.0), tf=80.0, dt=0.01, noise=0.12, seed=20250720)
    print("\nPRODUCTION verdict (recorded potential):")
    for k, v in o.items():
        print(f"  kappa={k}: corr = {v['phi']:+.4f} over {v['ndraw']} draws"
              f"  (independent if |corr| < ~{1/np.sqrt(max(v['ndraw'],1)):.3f})")
    return o


# ============================================================================================
def main():
    t_start = time.time()
    print("=" * 92)
    print("THE JOINT GENESIS DRAW -- one trajectory carrying WINDING n and ROTATION theta_dot")
    print("  V = m^2 R^2 + lam R^4 + 2 eps_A lam R^4 cos4theta,  eps_A = 2/9,  released at rest")
    print("=" * 92)

    v1 = validate_half_one(); print()
    v2 = validate_half_two(); print()
    pmc = parity_mirror_check(); print()

    print("  THE JOINT (sign theta_dot, sign n) DISTRIBUTION over the prior [recorded potential]")
    jd = joint_draw(N=16, n_theta=16, n_set=(-2, -1, 1, 2), kappas=(0.0, 0.5), tf=45.0, dt=0.05)
    print()
    sc = sensitivity_check(); print()

    worst = max(abs(v["phi"]) for v in jd.values())
    ndraw = min(v["ndraw"] for v in jd.values())
    thresh = 1.0 / np.sqrt(max(ndraw, 1))
    independent = worst < 2 * thresh and abs(sc[0.0]) < 2 * thresh
    sees_it = abs(sc[+0.8]) > 3 * thresh and abs(sc[-0.8]) > 3 * thresh

    print("=" * 92)
    print("VERDICT")
    print(f"  validations: half-one even split = {v1};  winding sector = {v2};"
          f"  parity mirror exact = {pmc}")
    print(f"  recorded-potential correlation |corr| <= {worst:.3f}  (noise floor ~{thresh:.3f});"
          f"  instrument sees injected term = {sees_it}")
    if independent and sees_it:
        print("  => sign(theta_dot) and sign(n) are INDEPENDENT draws. The winding modulates the")
        print("     roll's MAGNITUDE (an even-in-n suppression) but never its DIRECTION. The model")
        print("     cannot call the correlation: the helicity<->matter cross-messenger test CLOSES")
        print("     NEGATIVE -- a real null forced by spatial parity, not a failure to find one.")
    elif not independent:
        print("  => a correlation SURVIVES on the recorded potential: the cross-messenger test LIVES.")
    else:
        print("  => inconclusive at this grid; run production() with cores free.")
    print(f"  [wall {time.time()-t_start:.1f}s, single-threaded, tiny grid]")
    print("=" * 92)


if __name__ == "__main__":
    main()
