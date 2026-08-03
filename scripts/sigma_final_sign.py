#!/usr/bin/env python3
"""THE SIGN SESSION (estimate grade): sigma-final for the candle room.
A SN Ia near peak, approximated as a line-blanketed quasi-blackbody SED; the
unscreened-host version is the SAME SED with all wavelengths compressed by
eps = 1.24% (Rydberg ~ m_e: emitted bluer). Synthetic photometry through B/V
filter proxies -> the net distance-modulus bias through the SALT-style
mu = m_B - M + alpha*x1 - beta*c pipeline (m_B AND c shift TOGETHER — the
sign question is which effect wins). RAMPED: full filter integrals, no
single-wavelength shortcuts. Grade: ESTIMATE (template SED, proxy filters);
the direction is the deliverable, the magnitude the check."""
import numpy as np

# wavelength grid (angstrom) and a peak SN Ia SED proxy: 10,000 K blackbody
# with UV line-blanketing suppression (the standard gross shape)
lam = np.linspace(2500, 9000, 4000)
def sed(lam_eff):
    T = 10000.0
    x = 1.4388e8/(lam_eff*T)   # hc/(lambda k T), lambda in angstrom
    bb = 1.0/(lam_eff**5*(np.expm1(np.clip(x, 1e-9, 500))))
    blanket = 1.0/(1.0 + np.exp(-(lam_eff-3300.0)/250.0))   # UV suppression ramp
    return bb*blanket

def gauss_filter(center, width):
    return np.exp(-0.5*((lam-center)/width)**2)

B = gauss_filter(4400, 500); V = gauss_filter(5500, 450)

def mags(compress):
    """observed magnitudes for a SED emitted with wavelengths * (1-compress)"""
    # emitted-frame flux at observed lam: the source's rest features sit at
    # lam*(1+compress) of the standard template (compression: lines bluer)
    f = sed(lam*(1.0+compress))
    mB = -2.5*np.log10(np.trapezoid(f*B*lam, lam))
    mV = -2.5*np.log10(np.trapezoid(f*V*lam, lam))
    return mB, mV

eps = 0.0124
mB0, mV0 = mags(0.0)
mB1, mV1 = mags(eps)
dmB = mB1 - mB0
dc  = (mB1-mV1) - (mB0-mV0)      # delta color (B-V)
beta = 3.1
dmu = dmB - beta*dc               # the standardized distance-modulus bias
print(f"delta m_B = {dmB:+.4f} mag   delta(B-V) = {dc:+.4f} mag")
print(f"through SALT (beta=3.1): delta mu = dmB - beta*dc = {dmu:+.4f} mag")
print()
if dmu < 0:
    print("SIGMA-FINAL = +1 SENSE: unscreened SNe assigned SMALLER mu (closer) ->")
    print("flow-SNe distances UNDERESTIMATED -> H0 = v/d OVERESTIMATED -> the ladder")
    print("reads HIGH. The candle room pushes the SH0ES reading UP: the tension's sense.")
else:
    print("SIGMA-FINAL = -1 SENSE: the correction pushes the ladder DOWN — the room")
    print("becomes a constraint, not the tension's missing piece.")
print(f"\nmagnitude check: |dmu| = {abs(dmu):.3f} mag vs the mass step 0.05-0.08 mag")
