#!/usr/bin/env python3
"""B1 v4.1 — THE OBSERVER-POSITION PROFILE (entry 64's named decider).

Entry 64's ramp correction (process error 15) found the compressive-channel H₀ bias was
computed as drift/(whole 3-Gpc tail) — the MEAN gradient — while the observable is the
LOCAL gradient at the observer's structural position. The merger zone (where the wake
decelerates into the ring — where the resurrection physics concentrates) can run above
the mean. v4.1 computes bias(position) along the whole axis: THE PROFILE IS THE RAMP.

Method: v4's comoving run, unchanged, but the parcel field is BINNED along the axis at
the final state; the axial velocity field v_z(z) is reconstructed (mass-weighted, with a
continuity-respecting smoothing band swept as a ramp), and the local Hubble-monopole
leakage bias(z_obs) = (1/3)·(dv_z/dz)/H₀ is evaluated at every axial position. Outputs:
the profile, the mean (v4's number, recovered as a check), and the merger-zone
multiplier — the named decider.

Ramps declared: observer position (the profile itself); χ over the discharge band;
drift normalization 100–300 km/s; e-folds 8–20; the smoothing bandwidth swept ×4.
No menus; every knob a band.
"""
import numpy as np

def run_field(chi=4.75, efolds=14, n_t=6000):
    """v4's comoving run, returning the final parcel field + ring position."""
    tau = np.linspace(0, 3*chi, n_t); dt = tau[1]-tau[0]
    a_f = np.sqrt(1 + 2*tau/chi)
    U = (1-np.exp(-tau/0.5))*np.exp(-(tau/chi)**2)
    Gam = P = M = 1e-12; parcels = []
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
        if w < 0.999 and U[i] > 1e-3:
            parcels.append([z_r - 0.1, U[i]/2*a, (1-w)*dG, (1-w)*dM_])
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
            else:
                kept.append(p_)
        parcels = kept
    a_end = np.exp(efolds)
    return parcels, z_r, a_end

def bias_profile(parcels, z_r, a_end, v_drift=200.0, nbins=40, smooth=2, H0=70.0):
    """Reconstruct v_z(z) mass-weighted along the axis; return bias(z) in %."""
    zs = np.array([p[0] for p in parcels])
    vs = np.array([p[1]/a_end**2 for p in parcels])   # comoving velocity at the end
    ms = np.array([p[3] for p in parcels])
    if len(zs) < 10:
        return None
    # physical velocities normalized so the mass-weighted mean = v_drift (the banked order)
    vphys = vs/np.average(vs, weights=ms)*v_drift
    lo, hi = zs.min(), z_r
    edges = np.linspace(lo, hi, nbins+1)
    idx = np.clip(np.digitize(zs, edges)-1, 0, nbins-1)
    vbin = np.full(nbins, np.nan); mbin = np.zeros(nbins)
    for b in range(nbins):
        sel = idx == b
        if sel.sum() > 0:
            vbin[b] = np.average(vphys[sel], weights=ms[sel]); mbin[b] = ms[sel].sum()
    # fill empty bins by interpolation, then smooth (bandwidth = the swept ramp)
    # REFLECT-padded: zero-padding manufactures edge gradients exactly at the merger
    # zone and inflated the multiplier 4.2x (the artifact caught pre-booking, entry 146)
    cent = 0.5*(edges[1:]+edges[:-1])
    ok = ~np.isnan(vbin)
    vfill = np.interp(cent, cent[ok], vbin[ok])
    pad = smooth
    vp = np.concatenate([vfill[pad-1::-1], vfill, vfill[:-pad-1:-1]])
    k = np.ones(smooth)/smooth
    vsm = np.convolve(vp, k, mode='same')[pad:pad+nbins]
    # map the comoving span to the physical ~3 Gpc system (v4's convention)
    L_Mpc = 3000.0*(hi-lo)/(z_r+1e-9)
    dz_Mpc = L_Mpc/nbins
    grad = np.gradient(vsm, dz_Mpc)                  # km/s/Mpc
    bias_pct = grad/3.0/H0*100.0
    return cent, bias_pct, mbin, L_Mpc

if __name__ == "__main__":
    pass
print("="*78)
print("B1 v4.1 — bias(observer position): THE PROFILE IS THE RAMP")
print("="*78)
rows = []
for chi in [4.0, 4.75, 5.3]:
    for ef in [8, 14, 20]:
        parcels, z_r, a_end = run_field(chi, ef)
        for vd in [100.0, 200.0, 300.0]:
            for sm in [2, 4, 8]:
                out = bias_profile(parcels, z_r, a_end, vd, smooth=sm)
                if out is None: continue
                cent, bias, mbin, L = out
                # the merger zone = the leading 15% of the tail (nearest the ring)
                nz = len(cent); mz = slice(int(0.85*nz), nz)
                mean_abs = np.mean(np.abs(bias))
                merger = np.max(np.abs(bias[mz]))
                rows.append((chi, ef, vd, sm, mean_abs, merger, merger/max(mean_abs,1e-12)))
rows = np.array(rows)
print(f"\n  {'chi':>5s} {'efold':>5s} {'drift':>6s} {'sm':>3s} {'mean|bias|%':>11s} {'merger|bias|%':>13s} {'multiplier':>10s}")
for r in rows[::9]:
    print(f"  {r[0]:5.2f} {r[1]:5.0f} {r[2]:6.0f} {r[3]:3.0f} {r[4]:11.3f} {r[5]:13.3f} {r[6]:10.1f}")
mult = rows[:,6]; mrg = rows[:,5]
print(f"\n  ACROSS THE FULL RAMP GRID ({len(rows)} runs):")
print(f"    the mean-tail bias   : median {np.median(rows[:,4]):.3f}%  [{np.percentile(rows[:,4],16):.3f}, {np.percentile(rows[:,4],84):.3f}]")
print(f"    the MERGER-ZONE bias : median {np.median(mrg):.3f}%  [{np.percentile(mrg,16):.3f}, {np.percentile(mrg,84):.3f}]")
print(f"    the multiplier       : median {np.median(mult):.1f}×  [{np.percentile(mult,16):.1f}, {np.percentile(mult,84):.1f}]")
H0_shift = 73.0*np.percentile(mrg,[16,50,84])/100.0
print(f"    H₀ at the merger zone: 73.0 → {73.0-H0_shift[2]:.2f}–{73.0-H0_shift[0]:.2f} (median 73.0 → {73.0-H0_shift[1]:.2f})")
print("="*78)
