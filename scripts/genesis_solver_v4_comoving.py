#!/usr/bin/env python3
"""B1 v4 — THE COMOVING RETRIAL (sweep 64). The fair court: radiation-era a(t),
formation inside expansion, the catch-up race in comoving coordinates over the
full e-fold history. Plus THE H0 FIELD TEST: bias channels computed, not assumed.
Retrial targets (unchanged, sealed): eps=0.88, share=0.843. Landed already: n."""
import numpy as np

def run(chi=4.75, ovp=1.35, aD=0.15, efolds=14, n_t=6000):
    # --- FORMATION PHASE (comoving, radiation era: a = sqrt(1+2t/chi), H=1/(chi a^2))
    tau = np.linspace(0, 3*chi, n_t); dt = tau[1]-tau[0]
    a_f = np.sqrt(1 + 2*tau/chi)
    U = (1-np.exp(-tau/0.5))*np.exp(-(tau/chi)**2)   # physical emission speed
    Gam = P = M = 1e-12; parcels = []
    L0 = np.log(8*0.8/aD) - 0.25
    z_r = 0.0
    for i in range(n_t):
        a = a_f[i]
        R_c = max(np.sqrt(P/(np.pi*Gam)), 0.5) if Gam > 1e-10 else 0.5
        Ur = Gam/(4*np.pi*a*R_c)*L0
        w = 1/(1+np.exp(-np.clip((U[i]/2-Ur)/0.25,-30,30)))
        dG, dP_, dM_ = U[i]**2/2*dt, ovp*U[i]**2*(np.pi/4)*dt, U[i]*(np.pi/4)*dt
        Gam += w*dG; P += w*dP_; M += w*dM_
        z_r += Ur/a*dt
        if w < 0.999 and U[i] > 1e-3:
            parcels.append([z_r - 0.1, U[i]/2*a, (1-w)*dG, (1-w)*dM_])  # [z, mom, gam, m]
    Gt, Mt = (U**2/2*dt).sum(), (U*(np.pi/4)*dt).sum()
    R_c = np.sqrt(P/(np.pi*Gam)); n_wid = 2.26*R_c/aD
    # --- THE RACE (log-time to a = e^efolds): Ur ~ Gam/(a R), parcel v ~ mom/a
    lna = np.linspace(np.log(a_f[-1]), efolds, 4000); dlna = lna[1]-lna[0]
    for j in range(len(lna)):
        a = np.exp(lna[j]); H = 1/(chi*a**2); dt_ = dlna/(H)
        Ur = Gam/(4*np.pi*a*R_c)*L0
        z_r += Ur/a*dt_
        merged = []
        for p_ in parcels:
            p_[0] += p_[1]/a**2*dt_          # comoving advance, v_phys = mom/a
            if p_[0] >= z_r:                  # caught the ring
                Gam += p_[2]; M += p_[3]; merged.append(p_)
        parcels = [p_ for p_ in parcels if p_ not in merged]
    eps, share_raw = Gam/Gt, M/Mt
    share_bub = M*1.9/(M*1.9 + (Mt-M))
    # --- THE H0 FIELD TEST: channels
    #  (i) tangential swirl: divergence-free -> monopole ladder bias = 0 (EXACT)
    #  (ii) uniform drift: pure dipole -> SH0ES-marginalized
    #  (iii) compressive: the tail's axial gradient d v_z/dz where the jet decays
    v_drift = 200.0   # km/s scale (the flow line's banked order)
    if parcels:
        zs = np.array([p_[0] for p_ in parcels]); ms = np.array([p_[3] for p_ in parcels])
        L_tail_com = max(z_r - zs.min(), 0.1)     # comoving tail extent (D units)
        # map to Mpc: the system spans ~Gpc class; take tail ~ its comoving fraction
        L_tail_Mpc = 3000.0*L_tail_com/(z_r+1e-9)  # tail as fraction of system x 3 Gpc
        grad = v_drift/L_tail_Mpc                  # km/s/Mpc axial gradient scale
        bias = grad/3/70.0                         # (1/3) dv/dz over H0
    else:
        L_tail_Mpc, bias = 0.0, 0.0
    return dict(eps=eps, share_raw=share_raw, share_bub=share_bub, n=n_wid,
                caught=1-len(parcels)/max(1,len(parcels)+1), Ltail=L_tail_Mpc,
                bias_pct=bias*100, H0_corr=73.0/(1+bias))

print(f"{'chi':>5s} {'eps':>7s} {'shr_raw':>8s} {'shr_bub':>8s} {'n':>5s} {'tail(Mpc)':>10s} {'bias%':>6s} {'73.0->':>7s}")
for chi in [4.0, 4.75, 5.3]:
    r = run(chi)
    print(f"{chi:5.2f} {r['eps']:7.3f} {r['share_raw']:8.3f} {r['share_bub']:8.3f} {r['n']:5.0f} {r['Ltail']:10.0f} {r['bias_pct']:6.2f} {r['H0_corr']:7.1f}")
print("\ne-fold sensitivity at chi=4.75 (does the catch-up saturate?):")
for ef in [8, 14, 20]:
    r = run(4.75, efolds=ef)
    print(f"  efolds={ef:2d}: eps={r['eps']:.3f} share_raw={r['share_raw']:.3f}")
