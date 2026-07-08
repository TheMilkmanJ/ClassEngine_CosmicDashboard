#!/usr/bin/env python3
"""
Viscous incompressible 3D Navier-Stokes, pseudo-spectral, Taylor-Green vortex.
Question this addresses: starting from a SMOOTH, finite-energy initial condition,
does |vorticity| run to INFINITY in finite time (a singularity / blow-up)?

WHAT THIS SCRIPT CAN DO: evolve NS numerically and show whether the vorticity
and enstrophy grow to a finite peak and decay (regular) or run away (blow-up-like).
WHAT IT CANNOT DO: PROVE the Millennium problem either way. A finite-resolution,
finite-time simulation cannot rule out a blow-up at some later time, some other
initial condition, or some higher Reynolds number -- and near a true singularity
the grid under-resolves, so a sim can never certify "smooth forever." That gap
is exactly why the Clay problem is still open: physics/simulation is suggestive,
mathematical PROOF is what's missing.

USAGE:
    python3 scripts/navier_stokes_blowup.py               # defaults (N=48, Re=100)
    python3 scripts/navier_stokes_blowup.py --N 96 --Re 400 --T 12
Crank --N up for resolution and --Re up (lower viscosity) to push toward the
hard regime. Higher Re needs higher N to stay resolved.
"""
import argparse
import numpy as np

def run(N=48, Re=100.0, T=12.0, dt=0.01):
    nu = 1.0 / Re
    L = 2 * np.pi
    x = np.linspace(0, L, N, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
    # smooth, finite-energy initial condition: Taylor-Green vortex
    u = np.sin(X) * np.cos(Y) * np.cos(Z)
    v = -np.cos(X) * np.sin(Y) * np.cos(Z)
    w = np.zeros_like(u)
    k = np.fft.fftfreq(N, d=L / N) * 2 * np.pi
    KX, KY, KZ = np.meshgrid(k, k, k, indexing='ij')
    K2 = KX**2 + KY**2 + KZ**2
    K2[0, 0, 0] = 1.0
    kmax = np.max(np.abs(k)) * 2 / 3           # 2/3 dealiasing
    mask = ((np.abs(KX) < kmax) & (np.abs(KY) < kmax) & (np.abs(KZ) < kmax)).astype(float)
    fftn = np.fft.fftn
    ifftn = lambda a: np.fft.ifftn(a).real
    uh, vh, wh = fftn(u), fftn(v), fftn(w)

    def diagnostics(uh, vh, wh):
        wx = ifftn(1j * (KY * wh - KZ * vh))
        wy = ifftn(1j * (KZ * uh - KX * wh))
        wz = ifftn(1j * (KX * vh - KY * uh))
        m = np.sqrt(wx**2 + wy**2 + wz**2)
        en = 0.5 * np.mean(ifftn(uh)**2 + ifftn(vh)**2 + ifftn(wh)**2)
        return m.max(), 0.5 * np.mean(m**2), en

    def nonlin(uh, vh, wh):
        u, v, w = ifftn(uh), ifftn(vh), ifftn(wh)
        Nu = fftn(-(u*ifftn(1j*KX*uh) + v*ifftn(1j*KY*uh) + w*ifftn(1j*KZ*uh))) * mask
        Nv = fftn(-(u*ifftn(1j*KX*vh) + v*ifftn(1j*KY*vh) + w*ifftn(1j*KZ*vh))) * mask
        Nw = fftn(-(u*ifftn(1j*KX*wh) + v*ifftn(1j*KY*wh) + w*ifftn(1j*KZ*wh))) * mask
        div = (KX*Nu + KY*Nv + KZ*Nw) / K2       # Leray projection (incompressibility)
        return Nu - KX*div, Nv - KY*div, Nw - KZ*div

    steps = int(T / dt)
    visc = np.exp(-nu * K2 * dt)                 # exact integrating factor for viscous term
    print(f"3D viscous Navier-Stokes, Taylor-Green, Re={Re:.0f}, N={N}, T={T}")
    print(f"{'t':>6}{'max|vort|':>12}{'enstrophy':>12}{'energy':>12}")
    peak = 0.0
    every = max(1, int(1.0 / dt))
    for s in range(steps + 1):
        if s % every == 0:
            mv, ens, en = diagnostics(uh, vh, wh)
            peak = max(peak, ens)
            print(f"{s*dt:>6.1f}{mv:>12.3f}{ens:>12.4f}{en:>12.5f}", flush=True)
            if not np.isfinite(ens):
                print("\n*** NON-FINITE -- numerical blow-up (or under-resolution) ***")
                return
        Nu, Nv, Nw = nonlin(uh, vh, wh)
        u1 = (uh + dt*Nu) * visc; v1 = (vh + dt*Nv) * visc; w1 = (wh + dt*Nw) * visc
        Nu2, Nv2, Nw2 = nonlin(u1, v1, w1)
        uh = (uh + 0.5*dt*(Nu + Nu2/visc)) * visc
        vh = (vh + 0.5*dt*(Nv + Nv2/visc)) * visc
        wh = (wh + 0.5*dt*(Nw + Nw2/visc)) * visc
    mv, ens, en = diagnostics(uh, vh, wh)
    print(f"\npeak enstrophy = {peak:.4f}, final = {ens:.4f}")
    if ens < peak * 0.9:
        print("NO BLOW-UP: enstrophy rose to a FINITE peak then DECAYED -- viscosity regularized it.")
        print("NOTE: this is EVIDENCE, not PROOF. It cannot certify regularity for all")
        print("initial conditions / all times / all Reynolds numbers. The Millennium")
        print("problem asks for a PROOF, which no simulation can supply.")
    else:
        print("Enstrophy still high at final time -- extend T or raise N to see the peak/decay.")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=48)
    ap.add_argument("--Re", type=float, default=100.0)
    ap.add_argument("--T", type=float, default=12.0)
    ap.add_argument("--dt", type=float, default=0.01)
    a = ap.parse_args()
    run(a.N, a.Re, a.T, a.dt)
