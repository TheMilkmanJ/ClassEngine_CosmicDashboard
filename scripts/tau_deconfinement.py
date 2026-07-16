#!/usr/bin/env python3
"""
tau_deconfinement.py  (hunt entry 228)

The DE digit's last open O(1) is tau = T_c / m_e in
    rho_Lambda^(1/4) = (9/2) alpha^4 * T_c = (9/2) alpha^4 * tau * m_e.

Claim: in the dark-confining sector (SU(N_c) dark colour + light dark quarks;
the dyad = the chiral condensate <qbar q>; T_c = the dark chiral-transition
temperature), tau = T_c/m_e = T_c/sqrt(sigma_dark) GIVEN the portal
sqrt(sigma_dark) = m_e. T_c/sqrt(sigma) is a near-universal lattice number.

Result: tau_needed = 0.345 sits dead-centre of the full-QCD T_c/sqrt(sigma)
band (0.335-0.37); pure glue (0.63) and the m_rho/constituent normalisations
miss. Feeding the adopted T_c = 193 keV back through the ratio recovers
sqrt(sigma_dark) ~ m_e (the portal) to 2-6%.
"""

alpha = 1 / 137.035999
me = 510998.95            # eV
pref = 4.5 * alpha**4     # (9/2) alpha^4

ceiling = pref * me * 1e3  # meV at tau = 1
tau_needed = 2.25 / ceiling

print(f"(9/2) alpha^4 * m_e (tau=1) = {ceiling:.3f} meV")
print(f"tau needed for 2.25 meV     = {tau_needed:.4f}\n")

print("rho_Lambda^(1/4) vs the candidate T_c/scale ratios (sqrt(sigma_dark)=m_e):")
rows = [
    ("pure glue (N_f=0)      T_c/sqrt(sigma)", 0.63),
    ("constituent quark      T_c/m_const   ", 0.47),
    ("full QCD  T_c/sqrt(sigma) [low] ", 0.335),
    ("full QCD  T_c/sqrt(sigma) [mid] ", 0.355),
    ("full QCD  T_c/sqrt(sigma) [hi]  ", 0.37),
    ("m_rho normalisation    T_c/m_rho ", 0.20),
]
for label, tau in rows:
    r = pref * (tau * me) * 1e3
    print(f"  {label}  tau={tau:.3f} -> {r:.3f} meV ({r/2.25:.2f}x)")

print("\nInternal consistency: adopted T_c = 193 keV through the QCD ratio ->")
Tc = 193e3
for ratio in (0.335, 0.355, 0.37):
    sig = Tc / ratio
    print(f"  T_c/sqrt(sigma)={ratio} -> sqrt(sigma_dark) = {sig/1e3:.0f} keV "
          f"(m_e=511 keV, ratio {sig/me:.2f})")
