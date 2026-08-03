#!/usr/bin/env python3
"""FAST z_on: 1D likelihood profile at the frozen point (operator fudge order,
2026-07-12 night). RAMPED: smooth grid + parabola fit (center AND width);
n_s COUPLED to z_on through its own formula during the scan. zon-MCMC grades later."""
import numpy as np
from cobaya.model import get_model
from cobaya.yaml import yaml_load_file

info = yaml_load_file("cmp_prtoe_dyad_ev.yaml")
info.pop("sampler", None); info.pop("output", None)
model = get_model(info)

T0, MPl = 2.349e-4, 1.221e28  # eV
def ns_of(x):  # the census tilt coupled to the scanned epoch
    return 1.0 - 2.0/np.log(MPl/(T0*10**x))

base = dict(omega_b=0.022757, H0=69.613, logA=3.038860, z_reio=8.363414,
            dcdf_rho_inf=0.701221, varying_me=1.012543,
            A_planck=1.0, A_act=1.00071, P_act=1.00327,
            m_ncdm=0.0614, Tcal=0.996386, Ecal=1.00563)

def chi2(x):
    pt = dict(base, log10_zon=x, n_s=ns_of(x))
    lp = model.logposterior(pt, cached=False)
    return -2*sum(lp.loglikes)

xs, cs = [], []
for x in np.arange(7.1, 7.95, 0.1):
    c = chi2(x); xs.append(x); cs.append(c)
    print(f"log10_zon={x:.2f}  n_s={ns_of(x):.4f}  chi2={c:.2f}", flush=True)
xmin0 = xs[int(np.argmin(cs))]
for x in np.arange(xmin0-0.12, xmin0+0.125, 0.04):
    if not any(abs(x-e)<1e-6 for e in xs):
        c = chi2(x); xs.append(x); cs.append(c)
        print(f"log10_zon={x:.2f}  n_s={ns_of(x):.4f}  chi2={c:.2f}", flush=True)
xs, cs = np.array(xs), np.array(cs)
sel = np.abs(xs - xs[np.argmin(cs)]) < 0.25
a, b, c0 = np.polyfit(xs[sel], cs[sel], 2)
x_star, sig = -b/(2*a), 1/np.sqrt(a)
print(f"\nPROFILE RESULT (parabola on the smooth core):")
print(f"  log10_zon = {x_star:.3f} +/- {sig:.3f}   (z_on = {10**x_star:.3e})")
print(f"  n_s(coupled) = {ns_of(x_star):.4f}   chi2_min = {np.polyval([a,b,c0],x_star):.2f}")
print(f"  theory band check: the 3-alpha bath band 7.4-7.7 -> {'INSIDE' if 7.4 <= x_star <= 7.7 else 'OUTSIDE'}")
