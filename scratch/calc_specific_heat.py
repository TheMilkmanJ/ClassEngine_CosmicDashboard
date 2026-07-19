import numpy as np

alpha = 1.0 / 137.035999
alpha_c = 3.0 * alpha
c_s = np.sqrt(alpha_c)

# Thermal energy density of a massless phonon in 3D:
# rho = (pi^2 / 30) * (T^4 / c_s^3)
# Specific heat C_V = d(rho)/dT = (2 pi^2 / 15) * (T^3 / c_s^3)

coef_rho = np.pi**2 / (30.0 * c_s**3)
coef_cv = 2.0 * np.pi**2 / (15.0 * c_s**3)

print("=== Condensate Phonon Thermodynamics at Freeze-out ===")
print(f"Sound speed c_s = sqrt(alpha_c) = {c_s:.6f}")
print(f"Energy density rho_th = {coef_rho:.2f} * T^4")
print(f"Specific heat C_V = {coef_cv:.2f} * T^3")
print()
print("If the frozen energy density corresponds to the thermal phonon energy at T = m_nu:")
print(f"rho_Lambda = {coef_rho:.2f} * m_nu^4")
print(f"rho_Lambda^(1/4) = {coef_rho**(0.25):.4f} * m_nu")
