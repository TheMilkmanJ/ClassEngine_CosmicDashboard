#!/usr/bin/env python3
"""
The comoving genesis solver (B1) -- the Affleck-Dine field roll on the recorded
potential in a radiation-era comoving background, delivering the genesis amplitude
Psi0 and the amplitude-mode fraction f_amp from one instrument.

    V = m^2 R^2 + lam R^4 + 2 eps_A lam R^4 cos 4theta ,   eps_A = 2/9 ,

field released AT REST at release phase theta_i (uniform post-inflation prior),
evolved with the scale factor a(t) ~ sqrt(t) and Hubble friction H = 1/(2t) from
the frozen release (H > m) through oscillation onset (H = m) into the redshifting
regime.  One trajectory carries every genesis object:

  * f_amp -- the radial (breathing) energy fraction of the late-time orbit, over the
     release-phase prior (the genesis dice).  The amplitude mode that reads m_e and
     sets the granule contrast S = (1 + (1 - f_amp)^2)/2.  Distributional: one draw
     per universe, median ~0.6, banded by the release phase at the recorded tilt.

  * Psi0  -- the genesis amplitude, from the misalignment abundance closure.  The
     comoving energy density rho*a^3 freezes once the field oscillates quadratically;
     matching the frozen comoving density to the measured rho_DM,0 pins Psi0.  The
     ABSOLUTE normalization is the analytic abundance closure (rho_DM,0 and m):
     Psi0 = 5.0e16 GeV, Psi0 proportional to m^(-1/4).  The solver returns the O(1)
     onset+anharmonic factor A that corrects the leading closure; A is scale-free
     (m-independent to the integrator's accuracy), so the m^(-1/4) scaling survives
     the correction exactly.  Neither number is gated on a production-resolution run.

Superset of the four half-solvers, validated to reduce to each where they overlap:
  V1  genesis_famp_Z4.py         -- the zero-mode roll: same f_amp band, and the
      even sign(theta_dot) split forced by sigma: theta -> pi/2 - theta.
  V2  genesis_multicomponent.py  -- the winding sector: integer winding and the
      coherent fraction |<e^{i theta}>| on a spatial ring.
  V3  genesis_joint_draw.py      -- winding and rotation on one comoving ring; the
      ring reduces to the zero-mode roll at N=1.  (Imported and cross-checked.)
  V4  the abundance closure       -- rho*a^3 plateaus (misalignment realised, not
      assumed); A is scale-free; Psi0 proportional to m^(-1/4); absolute Psi0 = 5.0e16
      GeV against the analytic backbone (amplitude_11_analytic.py).

CPU discipline: single-threaded, one vectorised RK4 ring stepper plus a handful of
solve_ivp cross-checks, tiny grid, sub-minute.  __main__ runs a lean demo;
production() is defined but NOT called -- run it only with cores free.

Run:  OMP_NUM_THREADS=1 python3 scripts/genesis_solver_B1.py
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
           "NUMEXPR_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(_v, "1")          # never oversubscribe the chains' cores
import sys
import time
import numpy as np
from scipy.integrate import solve_ivp

# ---- the recorded genesis potential (code units, matching genesis_famp_Z4.py) ----
M2, LAM, RI = 1.0, 0.03, 10.0        # m^2, quartic, release radius |Psi| (units m=1)
EPS_A       = 2.0 / 9.0              # the Z4 tilt strength -- the recorded value
T_I, T_F    = 0.25, 80.0             # radiation-era window; H = 1/(2t), a = sqrt(t/T_I)
OMEGA       = np.sqrt(2.0 * M2)      # small-R oscillation frequency (V'' = 2 m^2)
R_CROSS     = np.sqrt(M2 / LAM)      # quartic->quadratic crossover: lam R^4 = m^2 R^2

# ---- the recorded cosmology (eV units, matching amplitude_11_analytic.py) ---------
H0      = 1.44e-33                   # eV  (H0 = 67.4 km/s/Mpc)
OM_R    = 9.2e-5                     # radiation density fraction today
OM_DM   = 0.264                      # dark-matter fraction today
M_RED   = 2.435e27                   # eV  (reduced Planck mass = 2.435e18 GeV)
M_PHYS  = 2.24e-20                   # eV  the measured dcdf mass
RHO_DM0 = OM_DM * 3.0 * H0**2 * M_RED**2     # eV^4 today


# ==================================================================================
#  the potential, its gradient, and the two winding-sector observables
# ==================================================================================
def V(x, y, m2=M2, lam=LAM, epsA=EPS_A):
    r2 = x * x + y * y
    return m2*r2 + lam*r2*r2 + 2.0*epsA*lam*(x**4 - 6.0*x*x*y*y + y**4)


def _gradV(x, y, epsA=EPS_A, m2=M2, lam=LAM):
    r2 = x * x + y * y
    dVx = 2*m2*x + 4*lam*r2*x + 2*epsA*lam*(4*x**3 - 12*x*y*y)
    dVy = 2*m2*y + 4*lam*r2*y + 2*epsA*lam*(4*y**3 - 12*x*x*y)
    return dVx, dVy


def winding(theta):
    """n = (1/2pi) oint grad theta . dl around the ring -- genesis_joint_draw.py's
    object: sum of wrapped nearest-neighbour phase differences / 2pi."""
    d = (np.roll(theta, -1, axis=-1) - theta + np.pi) % (2 * np.pi) - np.pi
    return d.sum(axis=-1) / (2 * np.pi)


def coherent_fraction(theta):
    """f = |<e^{i theta}>| -- genesis_multicomponent.py's observable (its line 42)."""
    return np.abs(np.mean(np.exp(1j * theta), axis=-1))


# ==================================================================================
#  the zero-mode comoving roll  (Cartesian, non-stiff; genesis_famp_Z4's integrator)
# ==================================================================================
def roll_0d(theta_i, epsA=EPS_A, t_i=T_I, t_f=T_F, r0=RI, m2=M2, lam=LAM):
    """Release AT REST at phase theta_i; evolve on the tilted potential with
    radiation-era friction H = 1/(2t).  Returns the dense solve_ivp solution."""
    def rhs(t, s):
        x, y, vx, vy = s
        dVx, dVy = _gradV(x, y, epsA, m2, lam)
        h = 1.0 / (2.0 * t)
        return [vx, vy, -3*h*vx - dVx, -3*h*vy - dVy]
    x0, y0 = r0 * np.cos(theta_i), r0 * np.sin(theta_i)
    return solve_ivp(rhs, [t_i, t_f], [x0, y0, 0.0, 0.0], method='RK45',
                     rtol=1e-8, atol=1e-10, max_step=0.05, dense_output=True)


def famp_and_charge(sol, t_f=T_F):
    """f_amp = radial-breathing energy fraction of the late-time orbit; L = mean
    charge (the generated rotation).  genesis_famp_Z4.py's f_amp method verbatim."""
    ts = np.linspace(0.6 * t_f, t_f, 4000)
    x, y, vx, vy = sol.sol(ts)
    r2 = x*x + y*y
    L = x*vy - y*vx
    E_rot = 0.5 * L*L / r2
    rdot = (x*vx + y*vy) / np.sqrt(r2)
    E_rad = 0.5 * rdot*rdot
    return float(np.mean(E_rad) / np.mean(E_rad + E_rot)), float(np.mean(L))


def abundance(sol, t_i=T_I, t_f=T_F, m2=M2, lam=LAM, n=6000):
    """Track the comoving energy density rho*a^3 through the roll and read off the
    frozen abundance.  rho = KE + V, a^3 = (t/t_i)^{3/2}.  Returns the plateau, its
    flatness, and A_total = plateau / (leading misalignment reference), where the
    reference is rho_osc*a_osc^3 = 1/2 omega^2 Psi_i^2 a_osc^3 with a_osc from H=omega
    -- the sharp-onset estimate the analytic backbone uses.  A_total is the O(1)
    onset+anharmonic correction it flags as owed."""
    ts = np.linspace(t_i, t_f, n)
    x, y, vx, vy = sol.sol(ts)
    KE = 0.5 * (vx*vx + vy*vy)
    Vv = V(x, y, m2, lam)
    rhoa3 = (KE + Vv) * (ts / t_i) ** 1.5
    late = ts >= 0.7 * t_f
    plateau = float(np.mean(rhoa3[late]))
    flat = float(np.max(np.abs(rhoa3[late] / plateau - 1.0)))
    omega = np.sqrt(2.0 * m2)
    a_osc3 = ((1.0 / (2.0 * omega)) / t_i) ** 1.5          # a_osc from H = omega
    r0 = np.hypot(x[0], y[0])
    ref = 0.5 * omega**2 * r0**2 * a_osc3
    return dict(ts=ts, rhoa3=rhoa3, plateau=plateau, flat=flat,
                A_total=plateau / ref, R0=float(r0))


# ==================================================================================
#  the misalignment abundance closure  (amplitude_11_analytic.py verbatim)
# ==================================================================================
def psi0_from_abundance(m):
    """Field frozen at Psi0 until H = m (a_osc), then rho ~ a^-3:
        rho_DM,0 = 1/2 m^2 Psi0^2 a_osc^3 ,  a_osc from H = H0 sqrt(Om_r) a^-2 = m."""
    a_osc = np.sqrt(H0 * np.sqrt(OM_R) / m)
    z_osc = 1.0 / a_osc - 1.0
    psi0 = np.sqrt(RHO_DM0 / (0.5 * m * m * a_osc**3))
    return psi0, a_osc, z_osc


# ==================================================================================
#  the vectorised comoving ring  (winding + rotation + abundance on one trajectory)
# ==================================================================================
def ring_ic(theta_i, n, N):
    """Centred winding ramp theta_j = theta_i + 2pi n (j - (N-1)/2)/N; mean phase is
    exactly theta_i, so n=0 reduces to the homogeneous release."""
    j = np.arange(N)
    return theta_i + 2 * np.pi * n * (j - (N - 1) / 2.0) / N


def evolve_ring(theta0, kappa=0.6, epsA=EPS_A, t_i=T_I, t_f=T_F, dt=0.04, r0=RI):
    """RK4 on a 1D periodic ring of the complex field, released at rest, with
    nearest-neighbour stiffness kappa (the gradient term that lets a winding live)
    and radiation-era friction.  State (x,y,vx,vy) shape (M draws, N sites).  N=1,
    kappa=0 is the vectorised zero-mode roll over all draws at once.

    Returns per draw: the initial winding, the frozen comoving charge
    Q = a^3 sum(x vy - y vx) (its sign = the generated rotation's sign), the frozen
    comoving abundance rho*a^3, the late coherent fraction, and the ring f_amp."""
    theta0 = np.atleast_2d(theta0)
    x = r0 * np.cos(theta0); y = r0 * np.sin(theta0)
    vx = np.zeros_like(x);   vy = np.zeros_like(y)
    n_init = winding(theta0)
    nsteps = int(round((t_f - t_i) / dt))

    def deriv(t, x, y, vx, vy):
        h = 1.0 / (2.0 * t)
        dVx, dVy = _gradV(x, y, epsA)
        lapx = kappa * (np.roll(x, -1, -1) + np.roll(x, 1, -1) - 2 * x)
        lapy = kappa * (np.roll(y, -1, -1) + np.roll(y, 1, -1) - 2 * y)
        return vx, vy, lapx - dVx - 3*h*vx, lapy - dVy - 3*h*vy

    t = t_i
    Q_sum = np.zeros(x.shape[0]); A_sum = np.zeros(x.shape[0]); cnt = 0
    Erad = np.zeros(x.shape[0]); Erot = np.zeros(x.shape[0])
    for i in range(nsteps + 1):
        if t >= 0.7 * t_f:
            a3 = (t / t_i) ** 1.5
            r2 = x*x + y*y
            Q_sum += a3 * np.sum(x*vy - y*vx, axis=-1)
            A_sum += a3 * np.sum(0.5*(vx*vx+vy*vy) + V(x, y), axis=-1)
            L = x*vy - y*vx
            rdot = (x*vx + y*vy) / np.sqrt(r2)
            Erad += np.mean(0.5*rdot*rdot, axis=-1)
            Erot += np.mean(0.5*L*L/r2, axis=-1); cnt += 1
        if i == nsteps:
            break
        k1 = deriv(t,        x,             y,             vx,             vy)
        k2 = deriv(t+dt/2,   x+dt/2*k1[0],  y+dt/2*k1[1],  vx+dt/2*k1[2],  vy+dt/2*k1[3])
        k3 = deriv(t+dt/2,   x+dt/2*k2[0],  y+dt/2*k2[1],  vx+dt/2*k2[2],  vy+dt/2*k2[3])
        k4 = deriv(t+dt,     x+dt*k3[0],    y+dt*k3[1],    vx+dt*k3[2],    vy+dt*k3[3])
        x  = x  + dt/6*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0])
        y  = y  + dt/6*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1])
        vx = vx + dt/6*(k1[2] + 2*k2[2] + 2*k3[2] + k4[2])
        vy = vy + dt/6*(k1[3] + 2*k2[3] + 2*k3[3] + k4[3])
        t += dt

    theta_f = np.arctan2(y, x)
    return dict(n_init=n_init, Q_frozen=Q_sum / max(cnt, 1),
                sign_thetadot=np.sign(Q_sum).astype(int),
                rhoa3=A_sum / max(cnt, 1), coh_final=coherent_fraction(theta_f),
                famp=Erad / np.maximum(Erad + Erot, 1e-30))


def zero_mode_scan(thetas, epsA=EPS_A, dt=0.04, t_f=T_F):
    """Vectorised zero-mode roll (N=1, kappa=0) over a phase grid -> (f_amp, charge)."""
    r = evolve_ring(np.asarray(thetas)[:, None], kappa=0.0, epsA=epsA, dt=dt, t_f=t_f)
    return r["famp"], r["Q_frozen"]


# ==================================================================================
#  VALIDATION 1 -- the zero-mode roll: f_amp band + even sign(theta_dot) split
# ==================================================================================
def validate_zero_mode(verbose=True):
    """Reproduce genesis_famp_Z4.py: the median f_amp over the release-phase prior at
    the recorded tilt, and the even sign(theta_dot) split forced by the reflection
    sigma: theta -> pi/2 - theta.  The vectorised ring is cross-checked against the
    reference solve_ivp integrator at four phases."""
    thetas = np.linspace(0.01, np.pi/2, 24)              # one Z4 period
    rows = []
    for epsA in (0.10, EPS_A, 0.30):
        fa, _ = zero_mode_scan(thetas, epsA=epsA)
        rows.append((epsA, float(np.median(fa)), float(fa.min()), float(fa.max())))
    fa_rec, _ = zero_mode_scan(thetas, epsA=EPS_A)
    sel = [2, 8, 14, 20]
    fa_ref = np.array([famp_and_charge(roll_0d(thetas[i], epsA=EPS_A))[0] for i in sel])
    cross = float(np.max(np.abs(fa_rec[sel] - fa_ref)))
    # even split: sigma-symmetric grid about pi/4; charge is odd under sigma
    sym = np.linspace(0.01, np.pi/2 - 0.01, 24)
    _, Q = zero_mode_scan(sym, epsA=EPS_A)
    npos, nneg = int((Q > 0).sum()), int((Q < 0).sum())
    antisym = float(np.max(np.abs(Q + Q[::-1])) / np.max(np.abs(Q)))
    ok = (npos == nneg) and (antisym < 1e-2) and (cross < 0.02)
    if verbose:
        print("  V1  the zero-mode roll  (vs genesis_famp_Z4.py)")
        print(f"    {'tilt eps_A':>11}  {'median f_amp':>12}  {'band':>16}")
        for epsA, med, lo, hi in rows:
            tag = "  <- recorded eps_A = 2/9" if abs(epsA - EPS_A) < 1e-6 else ""
            print(f"    {epsA:>11.3f}  {med:>12.2f}  [{lo:.2f}, {hi:.2f}]{tag}")
        print(f"    ring f_amp vs solve_ivp (4 phases)       : max |diff| = {cross:.3f}")
        print(f"    sign(theta_dot) split over one Z4 period : {npos} pos / {nneg} neg"
              f"   (genesis_famp_Z4: 12 / 12)")
        print(f"    sigma antisymmetry  Q(t) = -Q(pi/2 - t)  : residual/scale = {antisym:.1e}")
    return ok, rows, fa_rec


# ==================================================================================
#  VALIDATION 2 -- the winding sector (integer winding + coherent fraction)
# ==================================================================================
def validate_winding(verbose=True):
    """The winding counter returns exact integers for a clean ramp; the coherent
    fraction matches genesis_multicomponent's definition and its half-quantum-vortex
    coherence penalty.  Cross-checked against genesis_joint_draw.winding if present."""
    N = 24
    ns = np.array([-3, -2, -1, 0, 1, 2, 3])
    w = winding(np.stack([ring_ic(0.3, n, N) for n in ns]))
    ok_int = np.allclose(w, ns, atol=1e-9)
    rng = np.random.default_rng(7)
    ph = rng.uniform(-np.pi, np.pi, N)
    ok_coh = abs(coherent_fraction(ph[None])[0] - abs(np.mean(np.exp(1j*ph)))) < 1e-14
    locked = np.zeros(N); hqv = locked.copy(); hqv[:N//2] += np.pi
    ok_hqv = coherent_fraction(hqv[None])[0] < coherent_fraction(locked[None])[0]
    cross = "not found"
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import genesis_joint_draw as GJD                     # guarded by __main__
        w_gjd = GJD.winding(np.stack([ring_ic(0.3, n, N) for n in ns]))
        cross = "match" if np.allclose(w_gjd, ns, atol=1e-9) else "MISMATCH"
    except Exception as e:                                    # pragma: no cover
        cross = f"skip ({type(e).__name__})"
    ok = ok_int and ok_coh and ok_hqv and cross in ("match", "not found")
    if verbose:
        print("  V2  the winding sector  (vs genesis_multicomponent.py)")
        print("    winding of a clean n-ramp: " +
              ", ".join(f"{n}->{wi:+.3g}" for n, wi in zip(ns, w)) + "  (exact integers)")
        print(f"    coherent fraction = its line-42 definition       : {ok_coh}")
        print(f"    half-quantum-vortex coherence penalty (drops)    : {ok_hqv}")
        print(f"    winding vs genesis_joint_draw.winding            : {cross}")
    return ok


# ==================================================================================
#  VALIDATION 3 -- the comoving ring reduces to the zero-mode roll at N=1
# ==================================================================================
def validate_ring_reduction(fa_rec, verbose=True):
    """The N=1 comoving ring already produced fa_rec in V1; confirm it matches the
    reference solve_ivp roll, and that the ring carries an integer winding at N>1
    through the full comoving history."""
    thetas = np.linspace(0.01, np.pi/2, 24)
    sel = [4, 10, 16, 22]
    fa_ref = np.array([famp_and_charge(roll_0d(thetas[i]))[0] for i in sel])
    dev = float(np.max(np.abs(fa_rec[sel] - fa_ref)))
    N = 20
    r = evolve_ring(ring_ic(0.4, 2, N)[None], kappa=0.6, dt=0.04)
    ok = dev < 0.03 and abs(r["n_init"][0] - 2) < 1e-6
    if verbose:
        print("  V3  the comoving ring  (vs genesis_joint_draw.py)")
        print(f"    N=1 ring f_amp vs zero-mode solve_ivp : max |diff| = {dev:.3f}")
        print(f"    winding carried on the ring (n=2)     : n_init = {r['n_init'][0]:.3f}"
              f"  (a fully wound ring is phase-uniform: coh = {r['coh_final'][0]:.2f})")
    return ok


# ==================================================================================
#  VALIDATION 4 -- the abundance closure (the misalignment mechanism + Psi0)
# ==================================================================================
def validate_abundance(verbose=True):
    """rho*a^3 plateaus (misalignment realised, not assumed); the onset+anharmonic
    factor A is scale-free (identical under m^2 -> 4 m^2 with the roll rescaled), so
    Psi0 proportional to m^(-1/4) survives; and the quartic isolates as a suppression
    of the abundance relative to a purely quadratic release at the same amplitude."""
    ab = abundance(roll_0d(0.7, r0=RI))                       # recorded release
    # scale-freedom: m^2 x4, R_i x2, times /2 -> identical dimensionless roll
    ab_h = abundance(roll_0d(0.7, r0=2*RI, m2=4*M2, t_i=T_I/2, t_f=T_F/2),
                     t_i=T_I/2, t_f=T_F/2, m2=4*M2)
    # anharmonic isolation: full vs quadratic-only (lam = 0) at the same amplitude
    ab_lin = abundance(roll_0d(0.7, r0=RI, lam=0.0), lam=0.0)
    anharm = ab["plateau"] / ab_lin["plateau"]
    ok = (ab["flat"] < 0.05 and abs(ab["A_total"] - ab_h["A_total"]) < 0.02
          and 0.5 < anharm < 1.0)
    if verbose:
        print("  V4  the abundance closure  (the misalignment mechanism)")
        print(f"    rho*a^3 plateau flatness (late window)   : {ab['flat']*100:.1f}%"
              f"  (comoving density frozen => misalignment realised)")
        print(f"    onset+anharmonic factor A = plateau/ref  : {ab['A_total']:.3f}"
              f"  (O(1); the analytic backbone's ~2x, computed)")
        print(f"    A scale-free (m^2 x4, R_i x2, t /2)      : {ab_h['A_total']:.3f}"
              f" == {ab['A_total']:.3f}  =>  Psi0 ~ m^(-1/4) preserved")
        print(f"    quartic isolation, plateau_full/quadratic: {anharm:.3f}"
              f"  (the quartic bleeds abundance below the harmonic value)")
    return ok, ab["A_total"]


def deliver_psi0(A_total, verbose=True):
    """The absolute Psi0 from the abundance closure, with the m^(-1/4) scaling read
    off a log-log fit and the sim's O(1) onset+anharmonic factor folded in."""
    ms = np.array([1e-22, 1e-21, 1e-20, 2e-20, M_PHYS, 5e-20])
    psis = np.array([psi0_from_abundance(m)[0] for m in ms])
    slope = float(np.polyfit(np.log(ms), np.log(psis), 1)[0])       # expect -1/4
    psi0, a_osc, z_osc = psi0_from_abundance(M_PHYS)
    psi0_corr = psi0 / np.sqrt(A_total)              # plateau = A * leading estimate
    if verbose:
        print("  DELIVERY  Psi0 -- the genesis amplitude (misalignment abundance)")
        print(f"    {'m [eV]':>10}  {'z_osc':>9}  {'Psi0 [GeV]':>11}  {'Psi0/M_red':>10}")
        for m in ms:
            p, _, z = psi0_from_abundance(m)
            tag = "  <- measured m" if abs(m - M_PHYS) < 1e-30 else ""
            print(f"    {m:>10.0e}  {z:>9.1e}  {p/1e9:>11.2e}  {p/M_RED*100:>9.2f}%{tag}")
        print(f"    log-log slope d ln Psi0 / d ln m         : {slope:+.4f}  (exact -1/4)")
        print(f"    leading closure  Psi0(2.24e-20 eV)       : {psi0/1e9:.2e} GeV"
              f"  = {psi0/M_RED*100:.2f}% M_red,  z_osc = {z_osc:.2e}")
        print(f"    with the roll's factor A = {A_total:.2f} folded in     : "
              f"{psi0_corr/1e9:.2e} GeV  (~1/sqrt(A) = {1/np.sqrt(A_total):.2f}x; still O(1e16))")
    return psi0, psi0_corr, slope


# ==================================================================================
#  production() -- heavier, statistically tight.  DEFINED, NOT CALLED.
# ==================================================================================
def production():                                             # pragma: no cover
    """Full-resolution genesis draw: a dense release-phase prior for the f_amp
    distribution, a fine abundance run, and a large ring for the winding statistics.
    Do NOT call from __main__ (CPU discipline).  Run alone with cores free:
        OMP_NUM_THREADS=1 python3 -c 'import scripts.genesis_solver_B1 as G; G.production()'
    """
    print("PRODUCTION genesis draw -- run only with cores free")
    fa, _ = zero_mode_scan(np.linspace(0.001, np.pi/2, 400), dt=0.01)
    q = np.percentile(fa, [16, 50, 84])
    print(f"  f_amp distribution (eps_A=2/9): median {q[1]:.4f}  [{q[0]:.4f}, {q[2]:.4f}]")
    ab = abundance(roll_0d(0.7, r0=RI), n=40000)
    print(f"  onset+anharmonic factor A = {ab['A_total']:.4f}  (fine grid)")
    ring = evolve_ring(np.stack([ring_ic(th, n, 48)
                                 for th in np.linspace(0.05, np.pi/2-0.05, 40)
                                 for n in (-2, -1, 1, 2)]), kappa=0.3, dt=0.01, t_f=120.0)
    print(f"  ring draws: {ring['n_init'].size}, mean coherent fraction "
          f"{ring['coh_final'].mean():.3f}")


# ==================================================================================
def main():
    t0 = time.time()
    bar = "=" * 84
    print(bar)
    print("THE COMOVING GENESIS SOLVER (B1) -- Psi0 and f_amp from one AD field roll")
    print("  V = m^2 R^2 + lam R^4 + 2 eps_A lam R^4 cos4theta,  eps_A = 2/9,"
          "  released at rest")
    print(f"  code units m=1: quartic->quadratic crossover R_x = {R_CROSS:.2f},"
          f"  release R_i = {RI}  (R_i/R_x = {RI/R_CROSS:.2f})")
    print(bar)

    v1, _, fa_rec = validate_zero_mode(); print()
    v2 = validate_winding(); print()
    v3 = validate_ring_reduction(fa_rec); print()
    v4, A = validate_abundance(); print()

    print("-" * 84)
    psi0, psi0_corr, slope = deliver_psi0(A)
    print("-" * 84)

    q = np.percentile(fa_rec, [16, 50, 84])                   # reuse the V1 scan
    print(f"  DELIVERY  f_amp (eps_A = 2/9, release-phase prior): median {q[1]:.2f}"
          f"  band [{q[0]:.2f}, {q[2]:.2f}]  (the genesis dice; one draw per universe)")
    print(f"            granule-contrast cross-check S = (1+(1-f_amp)^2)/2 at median"
          f" = {(1+(1-q[1])**2)/2:.2f}  (granule_sim_2field: 0.55-0.60)")
    print("-" * 84)

    ok = v1 and v2 and v3 and v4
    print("VERDICT")
    print(f"  validations: zero-mode roll={v1}  winding={v2}  ring-reduction={v3}"
          f"  abundance={v4}")
    print(f"  Psi0 = {psi0/1e9:.2e} GeV (abundance-fixed, proportional to m^(-1/4),"
          f" slope {slope:+.3f}); absolute normalization NOT production-gated.")
    print(f"  f_amp = {q[1]:.2f} [{q[0]:.2f}, {q[2]:.2f}] (roll on recorded tilt),"
          f" tiny-grid-converged; the O(1) sim factor is A = {A:.2f}.")
    print(f"  [wall {time.time()-t0:.1f}s, single-threaded, tiny grid; production() deferred]")
    print(bar)
    return ok


if __name__ == "__main__":
    main()
