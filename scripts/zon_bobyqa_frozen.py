#!/usr/bin/env python3
"""The frozen-stack optimum (operator fudge order): BOBYQA over the compensating
dims at the DERIVED values (eps=1.012543, A_s=2.088058e-9 via logA, n_s=formula(z_on)).
Outputs: the true fast z_on + the frozen model's chi2 floor vs the 2798.7 champion.
House rule remembered: BOBYQA plateaus then breaks — run generous evals."""
import numpy as np, pybobyqa
from cobaya.model import get_model
from cobaya.yaml import yaml_load_file

info = yaml_load_file("cmp_prtoe_dyad_ev.yaml")
info.pop("sampler", None); info.pop("output", None)
model = get_model(info)
T0, MPl = 2.349e-4, 1.221e28
FIX = dict(varying_me=1.012543, logA=3.038860,
           A_planck=1.0, A_act=1.00071, P_act=1.00327, Tcal=0.996386, Ecal=1.00563)
names = ["omega_b","H0","z_reio","dcdf_rho_inf","m_ncdm","log10_zon"]
x0 =    [0.022757, 69.613, 8.363,  0.701221,      0.0614,  7.5]
lo =    [0.0205,   66.0,   4.5,    0.55,          0.02,    6.6]
hi =    [0.0245,   74.0,   11.5,   0.78,          0.12,    8.3]
best = [1e9]
def chi2(v):
    pt = dict(FIX, **{n: x for n, x in zip(names, v)})
    pt["n_s"] = 1.0 - 2.0/np.log(MPl/(T0*10**pt["log10_zon"]))
    try:
        lp = model.logposterior(pt, cached=False)
        c = -2*sum(lp.loglikes)
    except Exception:
        return 1e8
    if c < best[0]:
        best[0] = c
        print(f"  new best chi2={c:.2f} at zon={v[5]:.3f} H0={v[1]:.2f} ns={pt['n_s']:.4f}", flush=True)
    return c
sol = pybobyqa.solve(chi2, np.array(x0), bounds=(np.array(lo), np.array(hi)),
                     maxfun=350, rhobeg=0.15, rhoend=1e-3, scaling_within_bounds=True)
print("\nFROZEN-STACK OPTIMUM:")
for n, x in zip(names, sol.x): print(f"  {n} = {x:.6g}")
print(f"  n_s(formula) = {1.0 - 2.0/np.log(MPl/(T0*10**sol.x[5])):.4f}")
print(f"  chi2_frozen = {sol.f:.2f}   (champion sampled-run floor: 2798.7)")
print(f"  the freeze's cost: {sol.f - 2798.7:+.1f} chi2")
