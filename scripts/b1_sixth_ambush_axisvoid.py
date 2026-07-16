#!/usr/bin/env python3
"""B1's SIXTH AMBUSH — the axis-aligned underdensity (pre-registered, entry 60).

The question: does the expanded ring SYSTEM produce an axis-aligned underdensity, and
at what depth? The pre-registered comparison: the KBC-class void (δ ~ −0.2 over
100–300 Mpc) — the known shape of the remaining H₀ gap. The core-pressure and swirl
channels were filed COLD at sizing ((ω/H)² ~ 10⁻⁴, v²/c_s² ~ 2×10⁻⁵). This computes the
one channel never sized: WAKE EVACUATION — the ring gathered ~84% of the poured mass
out of the axis tube; the emptied tube IS an underdensity in the dark component.

Method: v4's comoving run with deposition bookkeeping — every parcel's emission
position is logged; the final state gives the deposited-mass profile m_dep(z) vs the
retained-mass profile m_fin(z); evacuation(z) = 1 − m_fin/m_dep. The local density
contrast a KBC-scale survey would measure at the observer's position:

    δ_survey = −evac(z_obs) · f_dark · (V_tube ∩ V_survey)/V_survey

with f_dark = the dCDF's share of the matter budget (≈0.84) and the tube geometry
mapped through v4's 3 Gpc convention. Ramps: χ band, e-folds, the tube-radius
convention swept ×4 (R_c to 4R_c — core to full swirl zone), survey radius 100–300 Mpc.
"""
import numpy as np

def run_field_deposit(chi=4.75, efolds=14, n_t=6000):
    tau = np.linspace(0, 3*chi, n_t); dt = tau[1]-tau[0]
    a_f = np.sqrt(1 + 2*tau/chi)
    U = (1-np.exp(-tau/0.5))*np.exp(-(tau/chi)**2)
    Gam = P = M = 1e-12
    parcels = []          # [z_now, mom, gam, m, z_emit]
    ring_mass_from = []   # (z_emit, m) for mass that reached the ring
    L0 = np.log(8*0.8/0.15) - 0.25
    z_r = 0.0
    for i in range(n_t):
        a = a_f[i]
        R_c = max(np.sqrt(P/(np.pi*Gam)), 0.5) if Gam > 1e-10 else 0.5
        Ur = Gam/(4*np.pi*a*R_c)*L0
        w = 1/(1+np.exp(-np.clip((U[i]/2-Ur)/0.25,-30,30)))
        dG, dP_, dM_ = U[i]**2/2*dt, 1.35*U[i]**2*(np.pi/4)*dt, U[i]*(np.pi/4)*dt
        Gam += w*dG; P += w*dP_; M += w*dM_
        z_r += Ur/a*dt
        if w > 1e-3:
            ring_mass_from.append((z_r, w*dM_))       # accepted at the ring's position
        if w < 0.999 and U[i] > 1e-3:
            parcels.append([z_r - 0.1, U[i]/2*a, (1-w)*dG, (1-w)*dM_, z_r - 0.1])
    R_c = np.sqrt(P/(np.pi*Gam))
    lna = np.linspace(np.log(a_f[-1]), efolds, 4000); dlna = lna[1]-lna[0]
    for j in range(len(lna)):
        a = np.exp(lna[j]); H = 1/(chi*a**2); dt_ = dlna/H
        Ur = Gam/(4*np.pi*a*R_c)*L0
        z_r += Ur/a*dt_
        kept = []
        for p_ in parcels:
            p_[0] += p_[1]/a**2*dt_
            if p_[0] >= z_r:
                Gam += p_[2]; M += p_[3]
                ring_mass_from.append((p_[4], p_[3]))  # its DEPOSIT site is evacuated
            else:
                kept.append(p_)
        parcels = kept
    return parcels, ring_mass_from, z_r, R_c

def ambush(chi, efolds, nbins=40):
    parcels, ring_from, z_r, R_c = run_field_deposit(chi, efolds)
    edges = np.linspace(0, z_r, nbins+1); cent = 0.5*(edges[1:]+edges[:-1])
    m_dep = np.zeros(nbins); m_fin = np.zeros(nbins)
    for z0, m in ring_from:
        b = min(int(z0/z_r*nbins), nbins-1); m_dep[b] += m      # deposited, later left
    for p in parcels:
        b = min(int(max(p[4],0)/z_r*nbins), nbins-1); m_dep[b] += p[3]
        b2 = min(int(max(p[0],0)/z_r*nbins), nbins-1); m_fin[b2] += p[3]
    evac = np.where(m_dep > 0, 1 - m_fin/np.maximum(m_dep,1e-30), 0.0)
    return cent/z_r, evac, m_dep, z_r, R_c

print("="*80)
print("B1's SIXTH AMBUSH — the axis-void profile (wake evacuation), ramped")
print("="*80)
f_dark = 0.84
rows = []
for chi in [4.0, 4.75, 5.3]:
    for ef in [8, 14, 20]:
        x, evac, m_dep, z_r, R_c = ambush(chi, ef)
        # the merger zone (the observer's structural position): the leading 15%
        mz = x > 0.85
        evac_obs = np.average(evac[mz], weights=np.maximum(m_dep[mz],1e-30))
        evac_mean = np.average(evac, weights=np.maximum(m_dep,1e-30))
        # geometry: v4's convention — the system z_r spans ~3 Gpc; tube radius from R_c
        D_Mpc = 3000.0/z_r                      # one D unit in Mpc
        rows.append((chi, ef, evac_mean, evac_obs, R_c*D_Mpc, D_Mpc))
rows = np.array(rows)
print(f"\n  {'chi':>5s} {'efold':>5s} {'evac(mean)':>10s} {'evac(obs)':>10s} {'R_tube(Mpc)':>12s}")
for r in rows:
    print(f"  {r[0]:5.2f} {r[1]:5.0f} {r[2]:10.3f} {r[3]:10.3f} {r[4]:12.0f}")
print(f"""
  THE SURVEY MAPPING (δ a KBC-scale sphere at the observer would measure):
    δ_survey = −evac(obs) × f_dark × fill_factor,  fill = (V_tube ∩ V_survey)/V_survey""")
print(f"  {'R_tube conv':>12s} {'R_survey':>9s} {'fill':>6s} {'δ_survey (median over grid)':>28s}   target: −0.2 (KBC)")
evac_obs_med = np.median(rows[:,3]); Rt_base = np.median(rows[:,4])
for mult, conv in [(1.0,'R_c (core)'), (2.0,'2R_c'), (4.0,'4R_c (swirl)')]:
    for Rs in [100.0, 300.0]:
        Rt = Rt_base*mult
        if Rt >= Rs:
            fill = 1.0
        else:
            # cylinder of radius Rt through a sphere of radius Rs: V = pi Rt^2 * 2Rs (Rt<<Rs)
            fill = min((np.pi*Rt**2*2*Rs)/((4/3)*np.pi*Rs**3), 1.0)
        d = -evac_obs_med*f_dark*fill
        print(f"  {conv:>12s} {Rs:9.0f} {fill:6.3f} {d:28.4f}")
print("="*80)
