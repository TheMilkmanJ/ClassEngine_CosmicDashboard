#!/usr/bin/env python3
"""
Chase JP's hook: is there a reason zeta = T_dark/T_gamma would equal
tau = T_c/m_e = (1/2)ln2 (the Koide kernel modulus, which sets T_c = tau*m_e)?

Clean identity: at dark confinement T_dark = T_c, so the photon temperature THEN is
   T_gamma(conf) = T_c / zeta = tau * m_e / zeta,
which equals m_e IFF zeta = tau.  =>  zeta = tau  <=>  the dark sector confines
exactly when T_gamma = m_e (the e+e- annihilation epoch).

So the hook reduces to one question: does dark confinement lock to e+e-? Compare the
thermal-history zeta (SM entropy dilution + the CMB fit) to tau.
"""
import numpy as np

tau = 0.5*np.log(2)          # Koide kernel modulus = T_c/m_e
m_e = 511.0                  # keV
T_c = tau*m_e                # dark confinement temperature

def dNeff(z): return (27/(7/4))*z**4

z_dilute = (3.91/106.75)**(1/3)       # SM entropy dilution, democratic pour
z_cmb    = (0.14*(7/4)/27)**(1/4)     # inverted from the CMB fit (dNeff = 0.14)
cases = [("tau = (1/2)ln2 (Koide)", tau),
         ("zeta (SM dilution)",     z_dilute),
         ("zeta (CMB fit)",         z_cmb)]

print(f"  tau = (1/2)ln2 = {tau:.4f}    T_c = tau*m_e = {T_c:.1f} keV    m_e = {m_e:.0f} keV")
print(f"  IDENTITY:  zeta = tau  <=>  dark confines exactly at T_gamma = m_e (e+e-)")
print("=" * 68)
print(f"  {'source':26s}{'zeta':>7}{'dNeff':>8}{'T_gamma(conf)':>16}{'vs m_e':>8}")
for name, z in cases:
    Tg = T_c/z
    print(f"  {name:26s}{z:>7.3f}{dNeff(z):>8.3f}{Tg:>12.0f} keV{100*(Tg-m_e)/m_e:>+7.0f}%")
print("=" * 68)
print(f"  tau vs zeta(dilution): {100*abs(tau-z_dilute)/tau:.0f}% apart |"
      f"  tau vs zeta(CMB): {100*abs(tau-z_cmb)/tau:.0f}% apart")
print()
print("  VERDICT: dark confinement lands within ~5-12% of the e+e- epoch (T_gamma=m_e),")
print("  so zeta ~ tau ALMOST holds. But zeta is set by SM entropy dilution (g*S 107->3.9)")
print("  and tau by the Koide kernel (Parseval) -- two ~1/3 numbers from UNRELATED physics,")
print("  both merely m_e-flavored (dark scale sqrt(sigma)=m_e; e+e- is m_e). Nothing locks")
print("  them: the portal (Gamma/H ~ 3e-7) is far too feeble to synchronize the two baths.")
print("  Near-coincidence, not a derivation. Sharp forward Q: is there a mechanism that")
print("  pins dark confinement to e+e-? If yes, zeta = tau and zeta stops being a bet.")
