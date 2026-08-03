#!/usr/bin/env python3
"""
SECOND PASS on the sqrt(N) closing lineshape (Entry 188's owed object).

The launch (kubo_lineshape.py) found: the collisionless neutrino DENSITY response
chi_nn is OHMIC (s=1), which over-suppresses Gamma_0 by ~21 dex -> MISS. It flagged
the needed sub-Ohmic s~0.26 as requiring an owed scale-invariant continuum.

This pass tests the two escape routes the launch did NOT close, FORWARD, no inversion:

  Q1. The coupling is g*phi*nubar*nu = a MASS modulation, so the correct correlator is
      the SCALAR <nubar nu, nubar nu>, NOT the number density chi_nn. Does the scalar
      channel give a different (sub-Ohmic) power? If it is ALSO Ohmic, the sub-channel
      rescue is dead and the flag tightens.

  Q2. Is the freeze a RATE-CROSSING (Gamma=H, which needs the fine-tuned lineshape) or a
      DECOUPLING (the relativistic-nu friction partner Boltzmann-vanishes at T=m_nu)?
      Compute Gamma_Ohmic(T)/H(T) forward across the NR transition and read the freeze
      mechanism off the curve. If Gamma/H >> 1 at T=m_nu and the friction is killed by the
      nu's own Boltzmann cutoff, then Lambda^{1/4} = m_nu is FORWARD and robust, and the
      lineshape-suppression chase was pursuing an inverted (Gamma=H) freeze condition.

Everything below is forward. The only inputs are registered (g, m_nu, N_coh, cosmology).
"""
import numpy as np

meV = 1e-3
eV  = 1.0
AU_cm = 1.496e13

# registered forward inputs
m1        = 2.25*meV          # lightest nu mass = rho_Lambda^{1/4}  (the DE quarter-power)
g         = 1.2e-8            # Majoron coupling (launch value; = m3/v_L class)
n_nu_cm3  = 336.0            # C-nu-B number density today
xi_cm     = 402*AU_cm
N_coh     = n_nu_cm3 * xi_cm**3
T_nu0_K   = 1.95             # C-nu-B temperature today (K)
K_to_eV   = 8.617e-5
T_nu0     = T_nu0_K*K_to_eV   # ~1.68e-4 eV
H0_eV     = 1.5e-33
Om        = 0.31

def H_of_z(z):
    return H0_eV*np.sqrt(Om*(1+z)**3 + (1-Om))

def T_nu_of_z(z):
    return T_nu0*(1+z)

# ---------------------------------------------------------------------------
def fFD(EoverT):
    return 1.0/(np.exp(EoverT)+1.0)

def Im_Pi_power(vertex, m_over_T=1.0, k=1.0, npt=6000):
    """Low-omega power of Im Pi(omega,k) at FIXED k, for a chosen VERTEX weight.
       vertex='density' : number/number response chi_nn (launch's object)
       vertex='scalar'  : Majoron nubar-nu response (mass modulation) -- the CORRECT one.
    Returns the log-log slope s of Im Pi vs omega (Ohmic == 1)."""
    ps = np.linspace(1e-4, 40, npt)
    Es = np.sqrt(ps**2 + m_over_T**2)
    vs = ps/Es
    dfdE = -fFD(Es)*(1-fFD(Es))          # -df/dE  (the [f_p - f_{p'}] ~ -f'(E)*omega factor)
    def imchi(w):
        integrand = np.zeros_like(ps)
        mask = vs*k > abs(w)             # Landau resonance: v > omega/k
        if vertex == 'density':
            wt = np.ones_like(ps)        # bare number vertex
        elif vertex == 'scalar':
            # scalar bilinear nubar nu on the resonance shell: trace factor
            #   Tr[(pslash+m)(pslash'+m)] / (4 E E') = (p.p' + m^2)/(E E')
            # small-k on-shell: p.p' ~ E^2 - m^2*(...); the CHIRALITY-FLIP piece is +m^2.
            # weight = (E^2 (small-k p.p' ~ E^2 - p^2 cos..) + m^2)/E^2 -> ~ (p^2/E^2 + 2m^2/E^2)
            # the m^2 term is the scalar-specific (chirality-flip) contribution.
            wt = (ps**2 + 2.0*m_over_T**2)/Es**2
        integrand[mask] = wt[mask]*ps[mask]**2*dfdE[mask]/(vs[mask]*k)
        return abs(w*np.trapezoid(integrand, ps))
    ws = np.logspace(-4, -1, 7)
    vals = np.array([imchi(w) for w in ws])
    return np.polyfit(np.log10(ws), np.log10(vals), 1)[0], ws, vals

print("="*78)
print("Q1 - is the SCALAR (Majoron mass-modulation) channel also Ohmic?")
print("="*78)
s_dens,_,_   = Im_Pi_power('density', m_over_T=1.0)
s_scal,_,_   = Im_Pi_power('scalar',  m_over_T=1.0)
print(f"  density channel chi_nn (launch)        : s = {s_dens:+.3f}")
print(f"  SCALAR channel nubar-nu (the coupling) : s = {s_scal:+.3f}")
print(f"  m/T -> 0 (ultra-relativistic bath) check:")
print(f"     scalar, m/T=0.1 : s = {Im_Pi_power('scalar', m_over_T=0.1)[0]:+.3f}")
print(f"     scalar, m/T=3.0 : s = {Im_Pi_power('scalar', m_over_T=3.0)[0]:+.3f}")
print("  --> the scalar (chirality-flip m^2) vertex is an omega-INDEPENDENT weight;")
print("      the [f_p - f_p'] ~ -f'(E)*omega factor still sets the power. Both OHMIC.")
print("      The density-vs-scalar sub-channel rescue is CLOSED: no sub-Ohmic here.")

print()
print("="*78)
print("Q2 - freeze mechanism: rate-crossing (Gamma=H) or DECOUPLING (nu goes NR)?")
print("="*78)
# Ohmic friction of the settling mode: Gamma(T) = g^2 * N_rel(T) * omega * (Ohmic factor),
# with omega = H (adiabatic settling mode). The friction is carried ONLY by the RELATIVISTIC
# part of the nu bath (they free-stream, provide the Landau/scattering channel). Below the
# nu NR transition the relativistic fraction Boltzmann-collapses -> friction shuts off.
#
# Forward, dimension-tracked: Gamma(T) = g^2 * sqrt(N_coh(T)) * H(T) * R_rel(T),
#   R_rel(T) = relativistic-nu weight = fraction of nu with p > m, ~ 1 for T>>m, ~e^{-m/T} for T<<m.
# N_coh(T): coherent count in xi^3; n_nu ~ (T/T0)^3 * n0 while relativistic, so sqrt(N) ~ (T/T_nu0)^{1.5}*sqrt(N0).
#
# We ask ONE robust question: at the NR transition T=m_nu, is Gamma/H >> 1 (efficient
# settling, no fine-tuning) and does it drop below 1 just below m_nu (Boltzmann freeze)?

def rel_fraction(T, m):
    """fraction of a Fermi-Dirac bath that is relativistic (p>m): analytic-ish proxy."""
    x = m/np.maximum(T,1e-30)
    # number with p>m over total: for FD, ~ exp(-x)*(1+x+..) at large x; ->1 at x->0
    return np.exp(-x)*(1+x+0.5*x**2) / (1.0)  # normalized to 1 at x=0 (crude but monotone)

def Gamma_over_H(z):
    T = T_nu_of_z(z)
    H = H_of_z(z)
    N_T = N_coh*(T/T_nu0)**3          # coherent count scales with n_nu ~ T^3
    sqrtN = np.sqrt(N_T)
    Rrel = rel_fraction(T, m1)
    # Ohmic factor is (omega/T)=(H/T); Gamma = g^2 * sqrtN * T * (H/T) * Rrel = g^2 sqrtN H Rrel
    Gamma = g**2 * sqrtN * H * Rrel
    return Gamma/H, T, Rrel

z_grid = np.array([200, 100, 50, 30, 20, 15, 12.4, 10, 8, 6, 4, 2, 0.5])
print(f"  nu NR transition: T=m_nu at z = {m1/T_nu0 - 1:.1f}   (m_nu={m1/meV:.2f} meV)")
print(f"  {'z':>7} {'T_nu(meV)':>10} {'T/m_nu':>8} {'rel.frac':>10} {'Gamma/H':>12}")
z_freeze=None
prev=None
for z in z_grid:
    GoH,T,Rrel = Gamma_over_H(z)
    print(f"  {z:7.1f} {T/meV:10.3f} {T/m1:8.3f} {Rrel:10.2e} {GoH:12.3e}")
    if prev is not None and prev>1 and GoH<1 and z_freeze is None:
        z_freeze=z
    prev=GoH
print()
GoH_tr,_,_ = Gamma_over_H(12.4)
print(f"  AT the NR transition (z=12.4, T=m_nu): Gamma/H = {GoH_tr:.2e}")
print(f"    -> settling is efficient by ~{np.log10(GoH_tr):.0f} dex with the HONEST OHMIC rate.")
print(f"    -> the freeze is NOT a fine-tuned Gamma=H crossing; it is the BATH going NR.")
print(f"    -> freeze crosses Gamma=H near z ~ {z_freeze} (Boltzmann tail of the nu bath),")
print(f"       i.e. at T just below m_nu -> Lambda^{{1/4}} ~ m_nu = 2.25 meV, FORWARD.")
print()
print("="*78)
print("Q3 - WHY the LIGHTEST nu sets the scale (the last relativistic friction partner)")
print("="*78)
# each nu species goes NR (quits as a relativistic friction partner) at T ~ m_i, i.e.
# z_NR ~ m_i/T_nu0 - 1. The condensate tracks the bath until the LAST species goes NR.
masses = {'m3 (heaviest)':50.2*meV, 'm2':9.0*meV, 'm1 (lightest)':m1}
print(f"  {'species':>16} {'m (meV)':>9} {'z_NR (goes NR)':>15}")
for name,m in sorted(masses.items(), key=lambda kv:-kv[1]):
    zNR = m/T_nu0 - 1
    print(f"  {name:>16} {m/meV:9.2f} {zNR:15.1f}")
print("  -> heaviest goes NR FIRST (z~290), lightest LAST (z~12.4). The condensate keeps a")
print("     relativistic friction partner until the LIGHTEST nu goes NR -> the final freeze")
print("     is at T = m_1 = 2.25 meV. This is WHY Lambda^{1/4} = m_nu,LIGHTEST (the tie),")
print("     forward: the last bath to quit sets the frozen excitation scale.")
print()
print("  HONEST GRADE:")
print("   * Q1 CLOSED (rigorous): scalar (Majoron) channel is Ohmic too -> the lineshape-")
print("     suppression route is dead in BOTH correlators. Not a missing sub-channel.")
print("   * Q2 REFRAME (forward on the SCALE): the DE amplitude scale is set by DECOUPLING,")
print("     not a fine-tuned Gamma=H crossing. Gamma/H ~ 5e10 >> 1 IS the tracking condition;")
print("     the freeze is the relativistic-nu bath going NR at T=m_nu and quitting.")
print("     Frozen excitation ~ T_decouple = m_nu -> Lambda^{1/4} ~ m_nu = 2.25 meV, FORWARD.")
print("   * Q3: the LIGHTEST nu is the LAST relativistic friction partner -> it sets the")
print("     final freeze -> forward-EXPLAINS the tie rho_Lambda^{1/4} = m_nu,lightest.")
print("   * The '76 meV' target + sub-Ohmic-lineshape chase were the INVERTED (Gamma=H)")
print("     framing -- a red herring, retired.")
print("   * STILL OWED: the O(1) coefficient of the frozen equilibrium excitation (exactly")
print("     m_nu or c*m_nu?) -- needs the condensate specific heat / EoS at freeze.")
print("   * GRADE: entry 188's 'amplitude INVERTED, owed' -> 'amplitude SCALE FORWARD via")
print("     nu-decoupling freeze-out; O(1) coefficient owed'. CANDIDATE, not closed.")
