#!/usr/bin/env python3
"""
dark_neff.py  (hunt entry 236)

Delta N_eff from the dark confining sector (sqrt(sigma_dark) ~ m_e, T_c ~ 179 keV).
The sector couples to the SM through the EM/electron portal, so it decouples at some
T_dec; after decoupling it cools as 1/a while later SM entropy dumps reheat gamma+nu:

    T_dark/T_nu = [ g*s(SM, T_nu ~ 2 MeV) / g*s(SM, T_dec) ]^(1/3)
    Delta N_eff = (4/7) * g_dark * (T_dark/T_nu)^4          (g_dark in boson-equiv dof)

Ramped over the two unknowns (decoupling temperature, light-dof count) rather than
asserting one point. Observational context: Planck N_eff = 2.99 +/- 0.17
(Delta N_eff < ~0.3, 2sigma); CMB-S4 forecast sensitivity ~ +/-0.03.
"""

g_nu = 10.75  # SM entropy dof at nu decoupling (~2 MeV): gamma + e+- + 3nu
g_star = {
    "T_dec > 200 GeV (all SM active)": 106.75,
    "T_dec ~ 1 GeV (above QCD)":        61.75,
    "T_dec ~ 150 MeV (QCD region)":     17.00,
    "T_dec ~ 20 MeV (below QCD)":       10.75,
}

print("Delta N_eff = (4/7) g_dark (T_dark/T_nu)^4  (assuming the sector thermalised):\n")
print(f"{'decoupling':<32}{'(Td/Tnu)^4':>11}{'g=2':>8}{'g=4':>8}{'g=8':>8}")
for label, gs in g_star.items():
    r4 = (g_nu / gs) ** (4 / 3)
    dN = [(4 / 7) * g * r4 for g in (2, 4, 8)]
    print(f"{label:<32}{r4:>11.3f}{dN[0]:>8.3f}{dN[1]:>8.3f}{dN[2]:>8.3f}")

print("\nReading: early decoupling (T_dec >~ 1 GeV) or few light dof keeps Delta N_eff <~ 0.3.")
print("Late decoupling (T_dec <~ 150 MeV) with several light dof is EXCLUDED by Planck.")
print("The surviving window ~0.05-0.3 is a target for CMB-S4 (+/-0.03).")
print("If the portal never thermalises the sector, Delta N_eff -> 0 (also allowed).")
