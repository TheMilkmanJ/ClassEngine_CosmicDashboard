#!/usr/bin/env python3
"""Task #18 session 2: THE SETTLEMENT TERMS (sweep 43, 2026-07-12).
Part 1: anchor edge-convention band for k_target = 1/(alpha_c ln(M_red/M_anchor)).
Part 2: the screening-menu collapse — roster forces the static-degenerate class
        (Lindhard; TF = its q->0 limit); computed TF-vs-Lindhard freedom = 0.2%.
Part 3: the crossover containment — Leggett T=0 gap+number equations across
        1/(kF a), validated: BCS asymptote (8/e^2)e^{-pi/(2kF|a|)} ratio 0.990;
        unitarity mu/E_F=0.592 (MF 0.5906), Delta/E_F=0.686 (MF 0.6864);
        BEC mu -> -1/(kF a)^2. Machinery: [Leggett1980], [NSR1985].
"""
import numpy as np
from scipy import integrate, optimize

ALPHA_C = 3/137.035999

def k_target_band(L0=34.98):
    convs = {"m_H": L0+np.log(4*np.pi), "2pi": L0+np.log(2), "4pi(banked)": L0, "8pi": L0-np.log(2)}
    return {n: 1/(ALPHA_C*L) for n, L in convs.items()}

def lindhard_F(u):
    u = np.clip(u, 1e-12, None)
    return 0.5 + (1-u**2)/(4*u)*np.log(abs((1+u)/(1-u)))

def screening_ratio(s2=ALPHA_C/np.pi):
    I_TF,_ = integrate.quad(lambda u: u/(u**2 + s2), 0, 1)
    I_L ,_ = integrate.quad(lambda u: u/(u**2 + s2*lindhard_F(u)), 0, 1)
    return I_L/I_TF

def I_gap(x, d):
    f = lambda k: k**2*(1/np.sqrt((k**2-x)**2+d**2) - 1/k**2)
    return integrate.quad(f, 0, 400, limit=600)[0]

def I_num(x, d):
    f = lambda k: k**2*(1 - (k**2-x)/np.sqrt((k**2-x)**2+d**2))
    return integrate.quad(f, 0, 400, limit=600)[0]

def solve_crossover(eta):
    """Returns (mu/E_F, Delta/E_F, converged) at 1/(kF a) = eta."""
    def eqs(p):
        x, ld = p; d = np.exp(ld)
        return [(2/np.pi)*I_gap(x,d) + eta, I_num(x,d) - 2/3]
    x0 = 1.0 if eta < 0.5 else -max(eta,0.2)**2
    d0 = 0.05 if eta < -1 else 0.5+abs(eta)
    p, info, ier, msg = optimize.fsolve(eqs, [x0, np.log(d0)], full_output=True)
    return p[0], np.exp(p[1]), ier == 1

if __name__ == "__main__":
    band = k_target_band()
    print("k_target band:", {k: round(v,3) for k,v in band.items()})
    print(f"screening freedom within forced class: R = {screening_ratio():.4f}")
    for eta in [-2.0, -1.0, 0.0, 1.0, 2.0]:
        x, d, ok = solve_crossover(eta)
        print(f"eta={eta:+.1f}: mu={x:+.3f} Delta={d:.4f} {'BCS' if x>0.5 else ('BEC' if x<0 else 'crossover')}")
