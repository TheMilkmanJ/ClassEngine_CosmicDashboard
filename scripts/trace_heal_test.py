#!/usr/bin/env python3
"""
Does the PRTOE field/conformal-factor 'show up' only when matter takes over?

Your hypothesis: the field is suppressed (masses ~unshifted) through the
RADIATION era (radiation is traceless -> nothing to push the conformal coupling)
and TURNS ON as matter comes to dominate. If true, F(phi) ~ 1 (and the field
displacement ~ frozen-small) at BBN, and it deviates as we cross matter-radiation
equality toward recombination.

This reads the ACTUAL background from the PRTOE-modified CLASS and reports the
conformal factor F, the field phi, and rel. m_e at BBN / equality / recomb / now.
Obey the model: whatever it says, it says.
"""
import numpy as np
from classy import Class

common = dict(
    use_dcdf='yes',
    varying_fundamental_constants='instantaneous',
    varying_alpha=1.0,
    varying_transition_redshift=50.0,
    dcdf_deltam_mode=1,
    omega_b=0.02237, H0=69.6, A_s=2.1e-9,
    n_s=0.9649, tau_reio=0.0544,
    N_ur=2.0328, N_ncdm=1, T_ncdm=0.71611, m_ncdm=0.06,
    dcdf_rho_inf=0.70,
    Omega0_dcdf=1.0 - 0.02237/(0.696**2),
    varying_me=1.01232,
    output='',    # background only
)
common = {k: v for k, v in common.items() if v is not None}

cosmo = Class()
try:
    cosmo.set(common)
    cosmo.compute(level=['background'])
except Exception as e:
    print("compute failed:", repr(e))
    raise

bg = cosmo.get_background()
z = bg['z']
# find relevant columns
cols = list(bg.keys())
def pick(*names):
    for n in names:
        for c in cols:
            if n.lower() in c.lower():
                return c
    return None

col_me  = pick('rel. m_e', 'rel.m_e', 'm_e')
col_a   = pick('rel. alpha', 'alpha')
col_phi = pick('phi_prtoe', 'phi_smg', 'phi ')
col_F   = pick('F_prtoe', "F '", 'F_prtoe')
print("available background columns:")
print("  ", cols)
print(f"\n picked: m_e={col_me}, alpha={col_a}, phi={col_phi}, F={col_F}\n")

# epochs
targets = {'BBN (z~1e8)': 1e8, 'BBN (z~1e9)': 1e9, 'eq (z~3400)': 3400,
           'recomb (z~1100)': 1100, 'now (z~0)': 0.0}
def at_z(col, zt):
    if col is None: return None
    return np.interp(zt, z[::-1], bg[col][::-1])

hdr = f"{'epoch':16s} {'z':>10s}"
for label, c in [('rel.m_e', col_me), ('rel.alpha', col_a), ('phi', col_phi), ('F', col_F)]:
    hdr += f" {label:>12s}"
print(hdr)
print("-"*len(hdr))
for name, zt in targets.items():
    line = f"{name:16s} {zt:10.3g}"
    for c in [col_me, col_a, col_phi, col_F]:
        v = at_z(c, zt)
        line += f" {v:12.6g}" if v is not None else f" {'--':>12s}"
    print(line)

print("\nREADING: if F (conformal factor) and phi are ~frozen-flat and F~1 through")
print("the radiation era (BBN) and only move near/after equality -> your reframe")
print("holds and the shift is matter-era-born (heal-compatible). If F deviates from")
print("1 already at BBN -> the field is displaced there and the coupling shifts")
print("masses at BBN regardless -> catastrophe (obey it).")
