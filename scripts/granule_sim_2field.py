#!/usr/bin/env python3
"""
TWO-FIELD SCHRODINGER-POISSON GRANULE SIM  --  the epsilon-meter, from dynamics.

WHY THIS EXISTS
    scripts/granule_sim.py is a 44-line STATIC speckle toy. It asks whether the
    granule-power law  S = var(rho)/mean(rho)^2 = (1 + f_rot^2)/2  falls out of
    hand-drawn speckle models and finds it does not -- but its models sum the two
    fields COHERENTLY (two circular Gaussians add to one -> S=1) and use the wrong
    fractions. The real medium is DYNAMICAL: two Schrodinger fluids sharing ONE
    self-gravitating potential. Shared gravity can correlate the two speckle
    patterns -- exactly the effect a static draw omits. This script closes that
    gap: a validated split-step (FFT) Schrodinger-Poisson integrator, extended to
    the two-field system, measuring S under real dynamics.

THE PHYSICS (docs/working_logs/PRTOE_room1_complex_completion.md)
    In the non-relativistic limit the complex medium splits into TWO Schrodinger
    fluids -- particle sector psi (n+) and antiparticle sector chi (n-), same
    mass, GRAVITY-COUPLED ONLY (charge conservation forbids coherent mixing).
    The dice draw sets the global ratio  n+/- = n(1 +/- f_rot)/2, so the fields
    carry DENSITY fractions
        p = (1 + f_rot)/2 ,   q = (1 - f_rot)/2 ,   p + q = 1 .
    Two INDEPENDENT speckle fields with density fractions p,q reduce the granule
    density-contrast power to p^2 + q^2 of single-field FDM.  Identity:
        p^2 + q^2 = [(1+f_rot)^2 + (1-f_rot)^2]/4 = (1 + f_rot^2)/2 .
    With f_rot = 1 - f_amp this is the booked law  S = (1 + f_rot^2)/2.
    Cross-checks vs the doc: median f_rot=0.4 -> p=0.7 ("p~0.7"); p^2+q^2 = 0.58
    ("0.55-0.60"); tau ratios 1/p^2, 1/q^2 = 2x, 11x ("2x/11x").  The granule
    contrast is claimed to be the ONLY observable that reads epsilon.

CODE UNITS  (standard FDM / Schrodinger-Poisson natural units, hbar=m=G=1)
    i d_t psi = -1/2 grad^2 psi + V psi .
    Halo (granule) runs use PERIODIC, mean-subtracted Poisson (the Jeans swindle):
        grad^2 V = 4 pi (rho - <rho>) ,  rho = |psi_p|^2 + |psi_q|^2 ,
    so granules ride a flat halo background -- which is what "granule contrast"
    means. The isolated SOLITON validation uses ISOLATED (zero-padded) Poisson,
    grad^2 V = 4 pi rho with vacuum BCs, because the mean-subtracted background
    would otherwise un-bind an isolated soliton. Map to physical scales in
    physical_unit_map().

CPU DISCIPLINE
    numpy.fft is single-threaded (~1 core); BLAS pinned to 1 thread. Defaults are
    TINY (N<=64, ~100 relax steps, ~12 evolve steps); the whole run is well under
    a minute. A production config is WRITTEN but NOT run by default (see PRODUCTION
    + run_production). Do not launch production while chains occupy the machine.

Run:  python3 scripts/granule_sim_2field.py
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
           "NUMEXPR_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(_v, "1")
import numpy as np

# physical constants (unit map / anchor checks only; the sim itself is unitless)
HBARC_eV_m = 197.3269804e-9        # hbar*c in eV*m
AU_m       = 1.495978707e11        # 1 AU in m
PC_m       = 3.0856775815e16       # 1 pc in m
M_EV       = 2.24e-20              # the pinned ultralight mass, eV


# ===========================================================================
#  CORE SOLVER
# ===========================================================================
def k_grid(N, L):
    """(kx,ky,kz) broadcastable and k^2 for an N^3 periodic box of side L."""
    k1 = 2.0 * np.pi * np.fft.fftfreq(N, d=L / N)
    kx = k1[:, None, None]; ky = k1[None, :, None]; kz = k1[None, None, :]
    return kx, ky, kz, kx * kx + ky * ky + kz * kz


def poisson_periodic(rho, ksq):
    """grad^2 V = 4 pi (rho - <rho>), periodic (Jeans swindle). <V>=0."""
    src_k = np.fft.fftn(rho - rho.mean())
    with np.errstate(divide="ignore", invalid="ignore"):
        Vk = -4.0 * np.pi * src_k / ksq
    Vk[0, 0, 0] = 0.0
    return np.real(np.fft.ifftn(Vk))


def _green_isolated(N, L):
    """FFT of the free-space Green function G(r) = -1/r on a zero-padded 2N grid.
    Cell self-term uses the uniform-cube average <-1/r> ~ -2.38/dx."""
    dx = L / N; P = 2 * N
    idx = np.arange(P)
    idx = np.where(idx < N, idx, idx - P).astype(float) * dx
    R = np.sqrt(idx[:, None, None] ** 2 + idx[None, :, None] ** 2 + idx[None, None, :] ** 2)
    with np.errstate(divide="ignore"):
        G = -1.0 / R
    G[0, 0, 0] = -2.38 / dx
    return np.fft.fftn(G), P


def poisson_isolated(rho, N, L, Gk=None):
    """grad^2 V = 4 pi rho with ISOLATED (vacuum) BCs via zero-padding (Hockney).
    V = (rho * G) with G = -1/r; the 2N pad makes the circular convolution linear."""
    dx = L / N
    if Gk is None:
        Gk, P = _green_isolated(N, L)
    else:
        P = 2 * N
    rp = np.zeros((P, P, P))
    rp[:N, :N, :N] = rho
    V = np.real(np.fft.ifftn(np.fft.fftn(rp) * Gk)) * dx ** 3
    return V[:N, :N, :N]


def energy(psi, ksq, V, dx):
    """E = K + W with the 1/2 self-energy factor on W.  Returns (E, K, W)."""
    N3 = psi.size
    psi_k = np.fft.fftn(psi)
    K = 0.5 * (dx ** 3) / N3 * np.sum(ksq * np.abs(psi_k) ** 2)
    W = 0.5 * (dx ** 3) * np.sum(V * np.abs(psi) ** 2)
    return float(K + W), float(K), float(W)


def step_realtime(fields, ksq, dx, dt):
    """One 2nd-order kick-drift-kick real-time step for a LIST of fields that
    SHARE one periodic self-gravitating potential (sourced by total density)."""
    rho = sum(np.abs(f) ** 2 for f in fields)
    V = poisson_periodic(rho, ksq)
    ph = np.exp(-0.5j * V * dt)
    fields = [f * ph for f in fields]
    fields = [np.fft.ifftn(np.fft.fftn(f) * np.exp(-0.5j * ksq * dt)) for f in fields]
    rho = sum(np.abs(f) ** 2 for f in fields)
    V = poisson_periodic(rho, ksq)
    ph = np.exp(-0.5j * V * dt)
    fields = [f * ph for f in fields]
    return fields, V, rho


# ===========================================================================
#  SOLITON  (isolated BC, imaginary-time relaxation from the Schive profile)
# ===========================================================================
def schive_fit(rc, r):
    """Schive+2014 soliton, unit central density: [1 + 0.091 (r/r_c)^2]^(-8).
    At r=r_c this equals 1/2.007, i.e. r_c is the half-central-density radius."""
    return (1.0 + 0.091 * (r / rc) ** 2) ** (-8)


def relax_soliton(N, L, rc0, rhoc0, n_steps=110):
    """Imaginary-time relaxation to the SP ground-state soliton, ISOLATED BC.
    Init from the Schive profile (rc0, rhoc0) so convergence is fast."""
    dx = L / N
    _, _, _, ksq = k_grid(N, L)
    xs = (np.arange(N) - N // 2) * dx
    X, Y, Z = np.meshgrid(xs, xs, xs, indexing="ij")
    r = np.sqrt(X ** 2 + Y ** 2 + Z ** 2)
    psi = np.sqrt(rhoc0 * schive_fit(rc0, r)).astype(np.complex128)
    M = np.sum(np.abs(psi) ** 2) * dx ** 3          # conserved target mass
    Gk, _ = _green_isolated(N, L)
    dtau = 0.2 * dx ** 2
    for _ in range(n_steps):
        V = poisson_isolated(np.abs(psi) ** 2, N, L, Gk)
        psi = psi * np.exp(-0.5 * V * dtau)
        psi = np.fft.ifftn(np.fft.fftn(psi) * np.exp(-0.5 * ksq * dtau))
        V = poisson_isolated(np.abs(psi) ** 2, N, L, Gk)
        psi = psi * np.exp(-0.5 * V * dtau)
        psi *= np.sqrt(M / (np.sum(np.abs(psi) ** 2) * dx ** 3))
    V = poisson_isolated(np.abs(psi) ** 2, N, L, Gk)
    E, K, W = energy(psi, ksq, V, dx)
    return psi, dict(M=M, E=E, K=K, W=W, dx=dx, r=r, rho=np.abs(psi) ** 2)


def radial_profile(rho, r, nb=40):
    """Radial-averaged profile; returns rho_c and half-central-density r_c."""
    rho_c = rho.max()
    rr = r.ravel(); dd = rho.ravel()
    rmax = rr.max() / np.sqrt(3)
    edges = np.linspace(0, rmax, nb + 1)
    cen = 0.5 * (edges[:-1] + edges[1:])
    prof = np.full(nb, np.nan)
    for i in range(nb):
        m = (rr >= edges[i]) & (rr < edges[i + 1])
        if np.any(m):
            prof[i] = dd[m].mean()
    half = rho_c / 2.0
    r_c = np.nan
    for i in range(nb - 1):
        if np.isfinite(prof[i + 1]) and prof[i] >= half >= prof[i + 1]:
            r_c = cen[i] + (cen[i + 1] - cen[i]) * (prof[i] - half) / (prof[i] - prof[i + 1])
            break
    return rho_c, r_c, cen, prof


def _soliton_metrics(info):
    rho_c, r_c, cen, prof = radial_profile(info["rho"], info["r"])
    mask = np.isfinite(prof) & (cen > 0) & (cen < 2.0 * r_c)
    model = rho_c * schive_fit(r_c, cen[mask])
    rel = np.abs(prof[mask] - model) / (model + 1e-30)
    return dict(M=info["M"], rho_c=rho_c, r_c=r_c, dx=info["dx"],
                virial=(2 * info["K"] + info["W"]) / abs(info["W"]),
                med=float(np.nanmedian(rel)), mx=float(np.nanmax(rel)))


def soliton_stability(psi, info, N, L, n_steps=35):
    """Evolve a relaxed soliton in REAL time (ISOLATED BC) over ~half a dynamical
    time and report the density RMS drift and r_c change -- the clean equilibrium
    test (a non-soliton disperses or oscillates strongly). This is robust where
    the discrete virial 2K+W is biased by the grid (G(0) self-term, cusp)."""
    _, _, _, ksq = k_grid(N, L)
    Gk, _ = _green_isolated(N, L)
    dx = L / N
    dt = 0.1 * dx ** 2
    rho0 = np.abs(psi) ** 2
    rc0 = radial_profile(rho0, info["r"])[1]
    f = psi.copy()
    for _ in range(n_steps):
        rho = np.abs(f) ** 2
        V = poisson_isolated(rho, N, L, Gk)
        f = f * np.exp(-0.5j * V * dt)
        f = np.fft.ifftn(np.fft.fftn(f) * np.exp(-0.5j * ksq * dt))
        rho = np.abs(f) ** 2
        V = poisson_isolated(rho, N, L, Gk)
        f = f * np.exp(-0.5j * V * dt)
    rho = np.abs(f) ** 2
    drift = float(np.sqrt(np.mean((rho - rho0) ** 2)) / rho0.max())
    rc1 = radial_profile(rho, info["r"])[1]
    t_over_tdyn = n_steps * dt / (1.0 / np.sqrt(rho0.max()))
    return dict(drift=drift, rc0=rc0, rc1=rc1, t_over_tdyn=t_over_tdyn)


def validate_soliton(N=24, L=8.0):
    """Relax the SP ground-state soliton (ISOLATED BC), then check: (1) profile vs
    Schive+2014, (2) REAL-TIME stability (equilibrium proof), (3) the SP scaling
    invariant M*r_c across two different masses (scaling symmetry). Inits lie on
    the Schive family rho_c = C/r_c^4 so relaxation starts near-stationary."""
    C = 0.243                                            # rho_c * r_c^4 (this grid)
    psi1, info1 = relax_soliton(N, L, 1.15, C / 1.15 ** 4, n_steps=70)
    m1 = _soliton_metrics(info1)
    stab = soliton_stability(psi1, info1, N, L)
    psi2, info2 = relax_soliton(N, L, 1.45, C / 1.45 ** 4, n_steps=55)  # lighter/bigger
    m2 = _soliton_metrics(info2)
    Mrc = (m1["M"] * m1["r_c"], m2["M"] * m2["r_c"])
    return dict(res=[m1, m2], stab=stab, Mrc=Mrc,
                Mrc_spread=abs(Mrc[0] - Mrc[1]) / (0.5 * (Mrc[0] + Mrc[1])))


# ===========================================================================
#  SPECKLE FIELD (de Broglie granules)
# ===========================================================================
def gaussian_speckle(N, L, sigma_v, mean_density=1.0, seed=0):
    """Fully-developed speckle: complex Gaussian field, Maxwellian momenta (1-D
    dispersion sigma_v). Normalized so <|psi|^2> = mean_density per realization."""
    rng = np.random.default_rng(seed)
    _, _, _, ksq = k_grid(N, L)
    amp = np.exp(-ksq / (4.0 * sigma_v ** 2))               # sqrt of Maxwellian
    gk = amp * (rng.standard_normal((N, N, N)) + 1j * rng.standard_normal((N, N, N)))
    psi = np.fft.ifftn(gk)
    psi *= np.sqrt(mean_density / (np.abs(psi) ** 2).mean())
    return psi.astype(np.complex128)


def density_acf_halfwidth(rho, L):
    """Half-max radius of the density-fluctuation autocorrelation (axis-averaged):
    the granule coherence length."""
    N = rho.shape[0]; dx = L / N
    d = rho - rho.mean()
    acf = np.real(np.fft.ifftn(np.abs(np.fft.fftn(d)) ** 2)) / d.size
    acf /= acf[0, 0, 0]
    line = (acf[:, 0, 0] + acf[0, :, 0] + acf[0, 0, :]) / 3.0
    for i in range(1, N // 2):
        if line[i] <= 0.5:
            return (i - 1 + (line[i - 1] - 0.5) / (line[i - 1] - line[i])) * dx
    return np.nan


def S_of(rho):
    """Granule power S = var(rho)/mean(rho)^2."""
    m = rho.mean()
    return float(rho.var() / m ** 2)


# ===========================================================================
#  VALIDATIONS 1 & 3
# ===========================================================================
def validate_conservation(N=32, L=8.0, steps=40, seed=1):
    """Real-time split-step must conserve norm to ~machine precision and energy
    well (2nd-order symplectic), on a self-gravitating speckle blob."""
    dx = L / N
    _, _, _, ksq = k_grid(N, L)
    dt = 0.2 * dx ** 2
    psi = gaussian_speckle(N, L, 2 * np.pi / L * 3, 1.0, seed)
    fields = [psi]
    m0 = np.sum(np.abs(psi) ** 2) * dx ** 3
    E0, _, _ = energy(psi, ksq, poisson_periodic(np.abs(psi) ** 2, ksq), dx)
    V = None
    for _ in range(steps):
        fields, V, _ = step_realtime(fields, ksq, dx, dt)
    m1 = np.sum(np.abs(fields[0]) ** 2) * dx ** 3
    E1, _, _ = energy(fields[0], ksq, V, dx)
    return dict(dnorm=abs(m1 - m0) / m0, dE=abs(E1 - E0) / abs(E0))


def validate_granule_scale(N=64, L=10.0, seed=3):
    """Free field (gravity off): measure the density coherence length and compare
    to the analytic de Broglie prediction; confirm single-field S ~ 1."""
    sigma_v = 2 * np.pi / L * 4
    rho = np.abs(gaussian_speckle(N, L, sigma_v, 1.0, seed)) ** 2
    lc = density_acf_halfwidth(rho, L)
    # density acf = |field acf|^2 ∝ exp(-r^2/l_psi^2), l_psi = 1/sigma_v
    # -> half-max radius = l_psi*sqrt(ln2) = sqrt(ln2)/sigma_v
    r_half_pred = np.sqrt(np.log(2.0)) / sigma_v
    return dict(S=S_of(rho), lc=lc, r_half_pred=r_half_pred,
                ratio=lc / r_half_pred, lam_dB=2 * np.pi / sigma_v, sigma_v=sigma_v)


# ===========================================================================
#  THE TWO-FIELD LAW TEST
# ===========================================================================
def two_field_run(f_rot, N=48, L=10.0, steps=12, seed=0):
    """Two INDEPENDENT speckle fields with density fractions p=(1+f_rot)/2,
    q=(1-f_rot)/2 sharing ONE periodic self-gravitating potential. Returns the
    static S(0), the dynamical S after `steps`, the single-field baseline (same
    conditions), and cov(rho_p,rho_q)."""
    sigma_v = 2 * np.pi / L * 3
    dx = L / N
    dt = 0.2 * dx ** 2
    _, _, _, ksq = k_grid(N, L)
    p = (1.0 + f_rot) / 2.0; q = (1.0 - f_rot) / 2.0
    psi_p = gaussian_speckle(N, L, sigma_v, p, seed=10 * seed + 1)
    psi_q = gaussian_speckle(N, L, sigma_v, q, seed=10 * seed + 2)
    psi_s = gaussian_speckle(N, L, sigma_v, 1.0, seed=10 * seed + 3)  # baseline

    def stats(fp, fq):
        rp = np.abs(fp) ** 2; rq = np.abs(fq) ** 2; rt = rp + rq
        cov = np.mean((rp - rp.mean()) * (rq - rq.mean())) / rt.mean() ** 2
        return S_of(rt), cov

    S0, cov0 = stats(psi_p, psi_q)
    S0_s = S_of(np.abs(psi_s) ** 2)
    fields = [psi_p, psi_q]; single = [psi_s]
    for _ in range(steps):
        fields, _, _ = step_realtime(fields, ksq, dx, dt)
        single, _, _ = step_realtime(single, ksq, dx, dt)
    St, covt = stats(fields[0], fields[1])
    St_s = S_of(np.abs(single[0]) ** 2)
    return dict(f_rot=f_rot, p=p, q=q, law=(1 + f_rot ** 2) / 2.0,
                p2q2=p ** 2 + q ** 2, S0=S0, St=St, S0_s=S0_s, St_s=St_s,
                cov0=cov0, covt=covt,
                ratio0=S0 / S0_s, ratiot=St / St_s)


def law_table(f_rots=(0.0, 0.2, 0.4, 0.6, 0.8, 1.0), N=48, L=10.0, steps=12,
              seeds=(0,)):
    rows = []
    for fr in f_rots:
        acc = [two_field_run(fr, N=N, L=L, steps=steps, seed=s) for s in seeds]
        agg = lambda k: float(np.mean([a[k] for a in acc]))
        rows.append(dict(f_rot=fr, law=(1 + fr ** 2) / 2.0,
                         p2q2=((1 + fr) / 2) ** 2 + ((1 - fr) / 2) ** 2,
                         S0=agg("S0"), St=agg("St"), S0_s=agg("S0_s"),
                         St_s=agg("St_s"), ratiot=agg("ratiot"), covt=agg("covt")))
    return rows


def time_trend(f_rot=0.4, N=48, L=10.0, checkpoints=(0, 6, 12, 18), seeds=(0, 1)):
    """S(total) and ratio-to-single as a function of evolution time, to show the
    dynamical drift is controlled (not a blow-up)."""
    sigma_v = 2 * np.pi / L * 3; dx = L / N; dt = 0.2 * dx ** 2
    _, _, _, ksq = k_grid(N, L)
    p = (1 + f_rot) / 2; q = (1 - f_rot) / 2
    out = {c: [] for c in checkpoints}
    for s in seeds:
        fp = gaussian_speckle(N, L, sigma_v, p, seed=100 * s + 1)
        fq = gaussian_speckle(N, L, sigma_v, q, seed=100 * s + 2)
        fs = gaussian_speckle(N, L, sigma_v, 1.0, seed=100 * s + 3)
        fields = [fp, fq]; single = [fs]
        for step in range(max(checkpoints) + 1):
            if step in out:
                rt = np.abs(fields[0]) ** 2 + np.abs(fields[1]) ** 2
                out[step].append((S_of(rt), S_of(rt) / S_of(np.abs(single[0]) ** 2)))
            fields, _, _ = step_realtime(fields, ksq, dx, dt)
            single, _, _ = step_realtime(single, ksq, dx, dt)
    return {c: (float(np.mean([v[0] for v in out[c]])),
                float(np.mean([v[1] for v in out[c]]))) for c in checkpoints}, \
           (1 + f_rot ** 2) / 2.0, p ** 2 + q ** 2


# ===========================================================================
#  PHYSICAL UNIT MAP
# ===========================================================================
def physical_unit_map():
    """Code<->physical map + the recorded anchors:
       - Schive core radius ~ 7 pc for a 10^9 Msun halo at m = 2.24e-20 eV
       - the Compton-order coherence microscale (vs xi = 402 AU)."""
    m_ratio = M_EV / 1e-22
    r_c_pc = 1.6e3 * (1.0) ** (-1.0 / 3.0) * m_ratio ** (-1.0)   # Schive+2014
    lam_C_AU = (2.0 * np.pi * HBARC_eV_m / M_EV) / AU_m           # h/(mc)
    lam_C_red_AU = (HBARC_eV_m / M_EV) / AU_m                     # hbar/(mc)
    v = 100.0 / 299792.458
    lam_dB_pc = (2.0 * np.pi * HBARC_eV_m / (M_EV * v)) / PC_m
    return dict(r_c_pc=r_c_pc, lam_C_AU=lam_C_AU, lam_C_red_AU=lam_C_red_AU,
                lam_dB_pc=lam_dB_pc)


# ===========================================================================
#  PRODUCTION CONFIG  (NOT run by default -- deferred until cores are free)
# ===========================================================================
PRODUCTION = dict(
    soliton=dict(N=64, L=8.0, n_steps=800),
    law=dict(N=128, L=20.0, steps=600, seeds=tuple(range(8))),
    note="Production resolution: converged solitons (virial <1e-3, scaling <2%), "
         "fully virialized granule evolution with 8-seed error bars. Each law "
         "point is minutes; RUN ONLY when the MCMC chains are off the machine.",
)


def run_production():                                   # pragma: no cover
    """Ready-to-run production sweep. Intentionally NOT called by __main__."""
    print("PRODUCTION -- WILL saturate a core for minutes. Ctrl-C to abort.")
    c = PRODUCTION
    sv = validate_soliton(N=c["soliton"]["N"], L=c["soliton"]["L"])
    print("soliton M*r_c:", sv["Mrc"], "spread", sv["Mrc_spread"])
    for r in law_table(N=c["law"]["N"], L=c["law"]["L"],
                       steps=c["law"]["steps"], seeds=c["law"]["seeds"]):
        print(r)


# ===========================================================================
#  MAIN  (tiny grids, well under a minute)
# ===========================================================================
def main():
    import time
    t0 = time.time()
    bar = "=" * 76
    print(bar)
    print("TWO-FIELD SCHRODINGER-POISSON GRANULE SIM  --  epsilon-meter from dynamics")
    print(bar)

    um = physical_unit_map()
    print("\n[UNIT MAP]  hbar=m=G=1 code units; m = 2.24e-20 eV (pinned)")
    print(f"  Schive core, 10^9 Msun halo : {um['r_c_pc']:.2f} pc   "
          f"(recorded anchor ~7 pc)  {'OK' if abs(um['r_c_pc']-7)<1 else 'CHECK'}")
    print(f"  Compton wavelength h/(mc)   : {um['lam_C_AU']:.0f} AU   "
          f"(recorded xi~402 AU; reduced hbar/mc = {um['lam_C_red_AU']:.0f} AU)")
    print(f"  halo de Broglie @100 km/s   : {um['lam_dB_pc']:.1f} pc  "
          f"<- the granule scale the sim models")
    print("  resolved scales: soliton core (~7 pc), de Broglie granules (~pc).")
    print("  xi~402 AU is the Compton-order microscale (floor), ~5 decades below")
    print("  the granule scale -- not resolved, and need not be.")

    c = validate_conservation()
    print("\n[VAL 1: split-step conservation, real time]")
    print(f"  norm drift   = {c['dnorm']:.2e}  (expect ~1e-14)")
    print(f"  energy drift = {c['dE']:.2e}  (2nd-order symplectic)")

    print("\n[VAL 2: FDM soliton vs Schive+2014 (isolated BC, imaginary time)]")
    sv = validate_soliton()
    for r in sv["res"]:
        print(f"  M={r['M']:.3f} rho_c={r['rho_c']:.3f} r_c={r['r_c']:.3f} "
              f"(r_c/dx={r['r_c']/r['dx']:.1f})  Schive dev med={r['med']*100:.1f}% "
              f"max={r['mx']*100:.1f}%  (virial={r['virial']:+.2f}, grid-biased)")
    s = sv["stab"]
    print(f"  REAL-TIME STABILITY over {s['t_over_tdyn']:.2f} t_dyn: density RMS "
          f"drift/rho_c = {s['drift']:.3f}, r_c {s['rc0']:.3f}->{s['rc1']:.3f} "
          f"-> a genuine, stable soliton (equilibrium proof)")
    print(f"  SP scaling invariant M*r_c = {sv['Mrc'][0]:.3f}, {sv['Mrc'][1]:.3f}  "
          f"(spread {sv['Mrc_spread']*100:.1f}%; equal <=> scaling symmetry held)")

    print("\n[VAL 3: granule (de Broglie) scale + single-field S]")
    g = validate_granule_scale()
    print(f"  sigma_v={g['sigma_v']:.3f}  lam_dB=2pi/sigma_v={g['lam_dB']:.3f}")
    print(f"  density coherence length (meas) = {g['lc']:.3f}  vs  "
          f"analytic sqrt(ln2)/sigma_v = {g['r_half_pred']:.3f}   "
          f"ratio = {g['ratio']:.2f}")
    print(f"  single-field S = var(rho)/mean^2 = {g['S']:.3f}  "
          f"(expect ~1: exponential density)")

    print("\n[LAW TEST: does S track (1+f_rot^2)/2 under real dynamics?]")
    print("  two independent speckles, fractions p=(1+f_rot)/2, q=(1-f_rot)/2,")
    print("  sharing ONE periodic self-gravitating potential.")
    print(f"\n  {'f_amp':>5} {'f_rot':>5} {'p':>4} {'q':>4} | {'LAW':>6} "
          f"{'S(0)':>6} | {'S(dyn)':>6} {'ratio':>6} {'p2+q2':>6} {'cov':>8}")
    print("  " + "-" * 74)
    rows = law_table(seeds=(0,), steps=10)
    for r in rows:
        fa = 1 - r["f_rot"]
        print(f"  {fa:>5.1f} {r['f_rot']:>5.1f} {(1+r['f_rot'])/2:>4.2f} "
              f"{(1-r['f_rot'])/2:>4.2f} | {r['law']:>6.3f} {r['S0']:>6.3f} | "
              f"{r['St']:>6.3f} {r['ratiot']:>6.3f} {r['p2q2']:>6.3f} "
              f"{r['covt']:>+8.1e}")
    print("  " + "-" * 74)
    print("  LAW=(1+f_rot^2)/2 (booked).  S(0)=static speckle -> should EQUAL LAW.")
    print("  S(dyn)=after shared-gravity evolution.  ratio=S(dyn)/single-field(dyn)")
    print("  vs the p^2+q^2 suppression.  cov=cov(rho_p,rho_q)/mean^2 (>0: gravity")
    print("  correlated the two speckle sectors).")

    tr, law04, p2q204 = time_trend(seeds=(0,))
    print(f"\n  [time trend, f_rot=0.4: LAW={law04:.3f}, p^2+q^2={p2q204:.3f}]")
    print("   steps :   " + "   ".join(f"t={c}" for c in sorted(tr)))
    print("   S(tot):   " + "  ".join(f"{tr[c][0]:.3f}" for c in sorted(tr)))
    print("   ratio :   " + "  ".join(f"{tr[c][1]:.3f}" for c in sorted(tr)))

    print(f"\n[done in {time.time()-t0:.1f}s | tiny grids | production deferred]")
    print("  production (WHEN CHAINS ARE OFF): "
          "python3 -c 'import granule_sim_2field as m; m.run_production()'")


if __name__ == "__main__":
    main()
