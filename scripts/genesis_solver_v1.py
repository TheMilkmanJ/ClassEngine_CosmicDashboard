#!/usr/bin/env python3
"""B1 v1 — THE GENESIS SOLVER, formation module (sweep 61).
The pour as a slug-model jet through the inherited-axis orifice (D = the heirloom).
RAMPS THROUGHOUT (the depth law): smooth discharge onset, smooth pinch-off taper
(Gharib criterion as a sigmoid in the velocity ratio), smooth expansion clip.
ONE dimensionless parameter: chi = U0/(D*H) — pour rate in diameters per Hubble time.
PRE-REGISTERED TARGETS (must co-land at a single chi):
  eps (circulation moment)  = 0.88   [strike-11 measurement]
  mass share (mass moment)  = 0.843  [Omega_c/Omega_m]
  effective discharge L/D   in [4.3, 5.3]  [strike-12 band]
BONUS OUTPUT: R/a at pinch-off -> Widnall n = 2.26 R/a  [target band 10-30]
"""
import numpy as np

def run(chi, shape="taper", n_t=20000):
    # time in D/U0 units; discharge shape s(tau): smooth onset (the operator's
    # "started up slow"), sustained, dying by the Hubble stretch at tau ~ chi
    tau = np.linspace(0, 3*chi, n_t); dt = tau[1]-tau[0]
    onset = 1 - np.exp(-tau/0.5)                       # spin-up ramp (KH-time width)
    if shape == "taper":   s = onset*np.exp(-(tau/chi)**2)     # Gaussian Hubble clip
    else:                  s = onset*np.sin(np.pi*np.clip(tau,0,chi)/chi)*(tau<chi)  # half-pulse
    U = np.clip(s, 0, None)
    # slug model: circulation flux dGamma = U^2/2 dt; mass flux dM = U dt
    dGam, dM = U**2/2*dt, U*dt
    # ring state: R ~ 0.7 D during formation (lab); core from fed volume
    R = 0.7
    Gam_r, M_r, Vol = 1e-12, 1e-12, 1e-12
    eps_hist = []
    w_hist = np.zeros(n_t)
    for i in range(n_t):
        a = max(np.sqrt(Vol/(2*np.pi**2*R)), 1e-6)     # core radius from volume
        Uring = Gam_r/(4*np.pi*R)*(np.log(8*R/max(a,1e-6))-0.25)
        # Gharib pinch-off: acceptance dies as Uring approaches the feed speed U/2
        # RAMPED: sigmoid of width ~ the KH time (0.5 in D/U0 units)
        x = (U[i]/2 - Uring)/0.25
        w = 1/(1+np.exp(-x)) if abs(x) < 30 else (1.0 if x > 0 else 0.0)
        w_hist[i] = w
        Gam_r += w*dGam[i]; M_r += w*dM[i]; Vol += w*dM[i]   # unit-area slug
    Gam_tot, M_tot = dGam.sum(), dM.sum()
    a_f = np.sqrt(Vol/(2*np.pi**2*R))
    return dict(eps=Gam_r/Gam_tot, share=M_r/M_tot,
                LD=M_tot,                     # total discharge in diameters
                Ra=R/a_f, n=2.26*R/a_f)

print(f"{'chi':>5s} {'L/D_eff':>8s} {'eps':>7s} {'share':>7s} {'R/a':>6s} {'n':>5s}   targets: eps=0.88 share=0.843 L/D 4.3-5.3 n 10-30")
for chi in [3.0, 4.0, 4.75, 5.3, 6.5, 8.0]:
    r = run(chi)
    hit = ("<-- CO-LAND" if abs(r['eps']-0.88)<0.03 and abs(r['share']-0.843)<0.03
           and 4.3 < r['LD'] < 5.3 else "")
    print(f"{chi:5.2f} {r['LD']:8.2f} {r['eps']:7.3f} {r['share']:7.3f} {r['Ra']:6.1f} {r['n']:5.0f}   {hit}")
