#!/usr/bin/env python3
"""B1 v2 — the two REGISTERED physics pieces added (sweep 61 spec, nothing else):
(1) R(t) DERIVED from impulse: P_ring = Gamma*pi*R^2 -> R = sqrt(P/(pi*Gamma)),
    with dP = U^2*(pi/4)dt (jet momentum flux, D=1) and dGamma = U^2/2 dt.
(2) THE THIN ROLLED CORE: a/D = 0.15 +/- 0.05 (lab range for formation-number
    rings; cited closure, bundle-microstructure derivation deferred).
Same chi, same ramps, same acceptance (Gharib sigmoid), same targets:
eps = 0.88, share = 0.843, L/D in [4.3,5.3], Widnall n = 2.26 R/a in [10,30]."""
import numpy as np

def run(chi, a_over_D=0.15, n_t=40000):
    tau = np.linspace(0, 3*chi, n_t); dt = tau[1]-tau[0]
    onset = 1 - np.exp(-tau/0.5)
    U = onset*np.exp(-(tau/chi)**2)
    dGam, dP, dM = U**2/2*dt, U**2*(np.pi/4)*dt, U*(np.pi/4)*dt
    Gam, P, M = 1e-12, 1e-12, 1e-12
    a = a_over_D
    for i in range(n_t):
        R = max(np.sqrt(P/(np.pi*Gam)), 0.5) if Gam > 1e-10 else 0.5
        Uring = Gam/(4*np.pi*R)*(np.log(8*R/a)-0.25)
        x = (U[i]/2 - Uring)/0.25
        w = 1/(1+np.exp(-np.clip(x,-30,30)))
        Gam += w*dGam[i]; P += w*dP[i]; M += w*dM[i]
    R = np.sqrt(P/(np.pi*Gam))
    return dict(eps=Gam/dGam.sum(), share=M/dM.sum(), LD=dM.sum()/(np.pi/4),
                R=R, Ra=R/a, n=2.26*R/a)

print(f"{'chi':>5s} {'L/D':>6s} {'eps':>7s} {'share':>7s} {'R':>6s} {'R/a':>6s} {'n':>5s}   targets: 0.88 / 0.843 / [4.3,5.3] / n 10-30")
for chi in [3.0, 4.0, 4.75, 5.3, 6.5, 8.0, 10.0]:
    r = run(chi)
    hit = ("<-- CO-LAND" if abs(r['eps']-0.88)<0.03 and abs(r['share']-0.843)<0.03
           and 4.3 < r['LD'] < 5.3 and 10 < r['n'] < 30 else "")
    print(f"{chi:5.2f} {r['LD']:6.2f} {r['eps']:7.3f} {r['share']:7.3f} {r['R']:6.2f} {r['Ra']:6.1f} {r['n']:5.0f}   {hit}")
print()
print("core-band sensitivity at the best chi (a/D = 0.10 / 0.15 / 0.20):")
for aD in [0.10, 0.15, 0.20]:
    r = run(5.3, a_over_D=aD)
    print(f"  a/D={aD:.2f}: eps={r['eps']:.3f} share={r['share']:.3f} n={r['n']:.0f}")
