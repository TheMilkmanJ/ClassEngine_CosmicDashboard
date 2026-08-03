import numpy as np
meV=1e-3; eV=1.0
Tnu0=1.95*8.617e-5   # neutrino temp today, eV
m_nu=2.25*meV        # lightest neutrino mass = rho_inf^1/4 (the tie value)

# The thermal-door picture: the condensate's genesis excitation settles via friction with the neutrino
# bath; friction turns off when neutrinos go non-relativistic (free-streaming ends); the deviation
# FREEZES at Gamma=H; the frozen residual = rho_Lambda.

# (1) The freeze redshift: T_nu = m_nu (neutrino NR transition)
z_freeze = m_nu/Tnu0 - 1
print(f"(1) Freeze at T_nu = m_nu:  z_freeze = {z_freeze:.1f}   (matches the model's z~12 claim)")

# (2) The energy scale at freeze. At T_nu = m_nu, the neutrino energy density ~ m_nu^4 (crossover).
rho_at_freeze = m_nu**4
print(f"(2) rho at freeze ~ m_nu^4 = ({m_nu/meV:.2f} meV)^4  = rho_Lambda  -> rho_Lambda^1/4 = m_nu = TIE (structural)")

# (3) The RESIDUAL FRACTION f: rho_Lambda = f * (energy at freeze). This is the whole content.
#     f depends on the settling response exponent s (the FDT lineshape, hunt 189):
#     ohmic s=1 -> the deviation over-damps -> f tiny;  sub-ohmic s~0.26 -> f ~ O(1) (residual survives).
print("\n(3) THE COEFFICIENT f (rho_Lambda = f * m_nu^4) is the whole game, and it is EXACTLY hunt 189:")
print("    - ohmic  (s=1, the COMPUTED response): deviation dies as e^{-large} -> f ~ 10^-84 -> 21-dex MISS")
print("    - sub-ohmic (s~0.26, Model-B conserved density): f ~ O(1) -> tie holds -> rho_Lambda^1/4 = m_nu")
print("    The thermal-door residual REDUCES to the ohmic-vs-sub-ohmic response question. NOT independently closed.")

print("\nVERDICT: the thermal door gives rho_Lambda = f * m_nu^4 with the freeze at T=m_nu (z~12) — it re-derives")
print("the TIE (rho_L^1/4 = m_nu) structurally, but the VALUE rides (a) m_nu [= the underived spurion mu, hunt 207]")
print("and (b) the coefficient f [= the ohmic-vs-sub-ohmic response, hunt 189 — a 21-dex-sensitive open question].")
print("Circular for the absolute value; not a new closure.")
