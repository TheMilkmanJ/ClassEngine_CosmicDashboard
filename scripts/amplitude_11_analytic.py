#!/usr/bin/env python3
"""
#11 ANALYTIC BACKBONE -- pin Psi0 from the DM abundance (misalignment) and
assemble the m_e amplitude  eps = c * f_amp * (Psi0/M_red).  Fast/analytic,
always completes.  The stiff genesis ODE (for f_amp from the orbit) is the
SEPARATE piece that needs WSL (scripts/genesis_field_evolution.py).

Goal: is the 1.24% amplitude DERIVED (not fit)?  What does it pin?

Run:  python3 scripts/amplitude_11_analytic.py
"""
import numpy as np

# --- constants (eV units) ---
H0      = 1.44e-33          # eV  (H0 = 67.4 km/s/Mpc)
Om_r    = 9.2e-5            # radiation density fraction today
Om_dm   = 0.264            # dark matter fraction today
M_red   = 2.435e27          # eV  (reduced Planck mass = 2.435e18 GeV)
eps_tgt = 0.0124            # the CMB-fit amplitude we want to DERIVE
f_amp   = 0.60             # amplitude-mode fraction (genesis dice; ODE-owed)
c_conf  = 1.0              # conformal coupling (naturalness ceiling; loop-owed)

rho_crit = 3*H0**2*M_red**2                 # eV^4
rho_dm0  = Om_dm*rho_crit                    # eV^4 today

def psi0_from_abundance(m):
    """Misalignment: field frozen until H=m (a_osc), then rho ~ a^-3.
    rho_dm0 = 1/2 m^2 Psi0^2 * a_osc^3 ,  a_osc from H(a_osc)=m (rad era)."""
    a_osc = np.sqrt(H0*np.sqrt(Om_r)/m)      # H = H0 sqrt(Om_r) a^-2 = m
    z_osc = 1/a_osc - 1
    Psi0  = np.sqrt(rho_dm0/(0.5*m**2*a_osc**3))
    return Psi0, a_osc, z_osc

print("="*70)
print("#11 ANALYTIC BACKBONE -- amplitude from abundance-pinned Psi0")
print("="*70)
print(f"\n  target eps = {eps_tgt*100:.2f}% ;  eps = c*f_amp*(Psi0/M_red),"
      f"  c={c_conf}, f_amp={f_amp}")
print(f"  => needs Psi0/M_red = eps/(c*f_amp) = {eps_tgt/(c_conf*f_amp)*100:.2f}%\n")

print(f"  {'m [eV]':>10} {'z_osc':>10} {'Psi0 [GeV]':>12} {'Psi0/M_red':>11} {'eps=cf(Psi0/M)':>15}")
print("  " + "-"*62)
for m in [1e-22, 1e-21, 5e-21, 1e-20, 2e-20, 5e-20]:
    Psi0, a_osc, z_osc = psi0_from_abundance(m)
    ratio = Psi0/M_red
    eps   = c_conf*f_amp*ratio
    print(f"  {m:>10.0e} {z_osc:>10.1e} {Psi0/1e9:>12.2e} {ratio*100:>10.2f}% {eps*100:>14.2f}%")

# invert: what m gives eps = 1.24% ?  (Psi0/M_red ~ m^-1/4)
# ratio(m) = ratio(m0)*(m/m0)^-1/4 ; solve ratio = eps_tgt/(c f_amp)
m0 = 1e-21
r0 = psi0_from_abundance(m0)[0]/M_red
r_need = eps_tgt/(c_conf*f_amp)
m_pin = m0*(r0/r_need)**4
Psi0_pin, _, z_osc_pin = psi0_from_abundance(m_pin)
print("\n" + "-"*70)
print("INVERSION -- the amplitude PINS the mass (Psi0/M_red ~ m^-1/4):")
print(f"  eps=1.24% (with c=1, f_amp=0.6)  =>  m = {m_pin:.2e} eV")
print(f"  at that m:  Psi0 = {Psi0_pin/1e9:.2e} GeV,  z_osc = {z_osc_pin:.1e},"
      f"  Psi0/M_red = {Psi0_pin/M_red*100:.2f}%")
print("-"*70)
print("READS:")
print(" * Psi0 ~ 1e17 GeV and Psi0/M_red are DERIVED from the DM abundance")
print("   (leading-order misalignment; O(1) anharmonic/onset factors ~2x).")
print(" * The amplitude is in the RIGHT DECADE by itself -- but hitting 1.24%")
print("   exactly requires m ~ few x 1e-20 eV (heavier than the 1e-21 fuzzy-DM")
print("   fiducial by ~20x).  So #11 + abundance => a MASS PIN (links to #9).")
print(" * STILL OWED (needs WSL stiff ODE / loop): f_amp from the genesis orbit,")
print("   c from the effective-action loop (#14), and the O(1) misalignment")
print("   factors.  Those move the pinned m by factors, not orders.")
print("-"*70)
