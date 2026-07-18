#!/usr/bin/env python3
"""THE CANDLE-ROOM MODULE (armed, sweeps 66-68). SN-likelihood correction for the
dyad's environmental residual under reading B. SHIPS with sign=-1: the sign-session
v2 (162-config template scan, lines-only compression) found the color channel's
sign robust at -1 (ledger, process error 18). Channels per sweep 68:
color (~0.09 mag class, signed -1) + luminosity (+0.008 mag, sign computed)."""
import numpy as np

def delta_mu(host_clumping_ratio, eps=0.012403, sign=-1.0,
             beta=3.1, dcolor_per_eps=2.4, dlum_per_eps=0.6, C_ref=1.0, p=4.0):
    """Distance-modulus correction for a SN in a host with clumping C/C_ref.
    sign=-1 (DEFAULT, ARMED-ON) -> candle term pushes the ladder down;
    sign=0 disables the color channel."""
    g = 1.0/(1.0 + host_clumping_ratio**p)        # the gate curve (steep, fenced)
    color = sign*beta*dcolor_per_eps*eps*g        # the restorer channel (sign -1, session-signed)
    lum   = -2.5*np.log10(1 + 0.5*dlum_per_eps*eps*g)  # the computed small channel
    return color + lum

if __name__ == "__main__":
    for cr in [0.1, 1.0, 10.0]:
        print(f"C/C_ref={cr:5.1f}: dmu(armed-off)={delta_mu(cr):+.4f}  "
              f"dmu(sign=+1)={delta_mu(cr, sign=1):+.4f} mag")
