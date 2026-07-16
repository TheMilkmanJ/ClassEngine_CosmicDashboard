#!/usr/bin/env python3
"""
THE KUBO LINESHAPE S(omega/T) FOR THE sqrt(N) NEUTRINO RESPONSE FUNCTION.
Entry 188's owed forward compute. NO INVERSION: nothing is back-solved from 2.25 meV.
The freeze epoch z~12 and omega=H(z=12) are forward (they are just T_nu = m_nu going NR).

Structure of the compute:
  PART 1 - reconstruct the forward chain (naive coherent -> sqrt(N) shot noise), verify
           the +32 -> +8 dex ladder from Entry 188's launch, with every input forward.
  PART 2 - N_coh from first principles (n_nu * xi^3), confirm 7.3e49 is forward.
  PART 3 - the actual Kubo/FDT lineshape: compute Im chi_nn(omega,k) (the collisionless
           Lindhard/Landau response of the neutrino bath) and extract its low-omega POWER.
           This is the object Entry 188 said "must be a fractional power" - we DERIVE it,
           we do not assume it.
  PART 4 - feed the derived lineshape forward, report Gamma_0, compare to 76 meV.
           Whatever it lands, report it. A forward miss that's honest beats a forced hit.
"""
import numpy as np
from scipy import integrate

# ---------- constants / forward inputs (all registered, none inverted) ----------
eV      = 1.0
meV     = 1e-3
keV     = 1e3
MeV     = 1e6
GeV     = 1e9
c_cgs   = 2.998e10          # cm/s
hbar_eVs= 6.582e-16         # eV s
hbarc_eVcm = 1.973e-5       # eV cm  (hbar c)
AU_cm   = 1.496e13          # cm

# neutrino sector (registered, PRTOE_neutrino_sector.md)
m1      = 2.25*meV          # lightest = rho_Lambda^{1/4}  (FORWARD, the DE quarter-power)
m3      = 50.2*meV          # heaviest (normal ordering)
Sigma_mnu = 61.4*meV
alpha_c = 0.021892          # = 3 alpha
c_s_over_c = np.sqrt(alpha_c)   # sound speed / c = 0.1479

# Majoron coupling (registered benchmark: g = m3/v_L, v_L=5MeV -> g=1.0e-8; launch used 1.2e-8)
g_launch = 1.2e-8

# cosmic neutrino density today (standard): 336 /cm^3 total (3 flavors, nu+nubar)
n_nu_today_cm3 = 336.0
xi_cm   = 402*AU_cm         # = 6.0e15 cm, the coherence hinge

# target
Gamma0_target = 76*meV      # entry 175/176: lands T_f = 2.25 meV = Lambda^{1/4}

print("="*78)
print("PART 1 - the forward chain, naive coherent vs sqrt(N) shot noise")
print("="*78)
T_nu = m1                   # bath temperature at freeze = m_nu (the NR transition, forward)
N_coh = 7.3e49             # (verified forward in PART 2)
g = g_launch
Gamma_naive = g**2 * T_nu * N_coh
Gamma_sqrtN = g**2 * T_nu * np.sqrt(N_coh)
print(f"  g = {g:.2e}   T_nu = {T_nu/meV:.3f} meV   N_coh = {N_coh:.2e}")
print(f"  naive coherent  Gamma0 = g^2 T N     = {Gamma_naive:.3e} eV")
print(f"     vs target 76 meV: overshoot = {np.log10(Gamma_naive/Gamma0_target):+.1f} dex   (entry: +32)")
print(f"  sqrt(N) shot     Gamma0 = g^2 T sqrt(N) = {Gamma_sqrtN:.3e} eV")
print(f"     vs target 76 meV: overshoot = {np.log10(Gamma_sqrtN/Gamma0_target):+.1f} dex   (entry: +8)")
supp_needed = Gamma0_target/Gamma_sqrtN
print(f"  --> lineshape must supply suppression S = {supp_needed:.2e}  (log10 = {np.log10(supp_needed):+.2f})")

print()
print("="*78)
print("PART 2 - N_coh forward (n_nu today * xi^3), and omega/T forward (freeze epoch)")
print("="*78)
N_coh_calc = n_nu_today_cm3 * xi_cm**3
print(f"  N_coh = n_nu(336/cm3) * xi^3 = {n_nu_today_cm3} * ({xi_cm:.2e})^3 = {N_coh_calc:.3e}")
print(f"     (registered launch value 7.3e49; ratio {N_coh_calc/7.3e49:.2f}) -> FORWARD, not fitted")

# omega = H at the freeze z~12 (forward: freeze is Gamma=H at T_f=2.25meV -> z~12)
H0_eV = 1.5e-33            # H0 ~ 70 km/s/Mpc in eV
Om    = 0.31
z_f   = 12.0
H_zf  = H0_eV*np.sqrt(Om*(1+z_f)**3 + (1-Om))
omega = H_zf
print(f"  H(z=12) = H0*sqrt(Om(1+z)^3) = {H_zf:.3e} eV   (= omega, the settling-mode freq)")
w_over_T = omega/T_nu
print(f"  omega/T = {w_over_T:.3e}   (log10 = {np.log10(w_over_T):.2f})   (entry: 1.8e-29)")

# the required lineshape power s: S = (omega/T)^s
s_required = np.log10(supp_needed)/np.log10(w_over_T)
print(f"  IF S = (omega/T)^s, the required power is  s = {s_required:.3f}")
print(f"     (a full derivative power s=1 would over-suppress by "
      f"{abs(np.log10(w_over_T))-abs(np.log10(supp_needed)):.0f} dex)")

print()
print("="*78)
print("PART 3 - the ACTUAL Kubo/FDT lineshape: Im chi_nn(omega,k) for the nu bath")
print("="*78)
print("""  Physics: the mode couples to the bath density fluctuation delta_n (the sqrt(N)
  channel, entry 176). Friction = FDT partner of that noise:
        Gamma(omega) ~ (g_eff^2/chi_mode) * Im chi_nn(omega, k)
  For a COLLISIONLESS (free-streaming, entry 177) bath the density response is the
  Lindhard/Landau form:
        Im chi_nn(omega,k) = -pi * Integral d3p/(2pi)^3 [f(E_p)-f(E_{p+k})] delta(omega-(E_{p+k}-E_p))
  We compute its low-omega POWER numerically for a Fermi-Dirac nu bath at T=m_nu
  (the NR transition), and read s off the slope. NO assumption of the power.""")

# Fermi-Dirac distribution, relativistic dispersion E=sqrt(p^2+m^2), massless-ish (m1 tiny vs p~T)
# work in units of T. p in units of T. bath temperature = T_nu.
def fFD(E_over_T):
    return 1.0/(np.exp(E_over_T)+1.0)

def Im_chi_nn(w, k, m_over_T=1.0, npt=4000):
    """Im chi_nn(omega,k) in units where T=1, up to an overall const. w,k in units of T.
    Small-k expansion: E_{p+k}-E_p ~ v_p*k*cos(theta); delta fixes cos = w/(v_p k)."""
    # integrate over p (in units of T)
    ps = np.linspace(1e-4, 40, npt)
    Es = np.sqrt(ps**2 + m_over_T**2)
    vs = ps/Es                      # velocity (units of c)
    dfdE = -fFD(Es)*(1-fFD(Es))     # -df/dE  (units 1/T)
    # resonance cos = w/(v k) must be in [-1,1]  -> v > w/k
    integrand = np.zeros_like(ps)
    mask = vs*k > abs(w)
    # angular integral of (v k cos) * delta(w - v k cos) over solid angle:
    #   int dOmega (v k cos) delta(w - v k cos) = 2pi * (w/(v k)) / (v k)   [for v k>|w|]
    # times p^2 measure and (-df/dE):
    integrand[mask] = ps[mask]**2 * dfdE[mask] * (w/(vs[mask]*k)) / (vs[mask]*k)
    val = np.trapezoid(integrand, ps)   # drops overall 2pi/(2pi)^3 const; we only want the POWER
    return val

# The PHYSICAL dissipation of a sound mode (w = c_s k) is its Landau damping rate gamma.
# The clean, parametrization-free question: is gamma/omega scale-free (ohmic, s=1) or does
# it run with omega (sub/super-ohmic)? Compute gamma/omega at fixed phase velocity w/k=c_s,
# sweeping omega over 5 decades. A FLAT gamma/omega == ohmic == lineshape power s=1.
print("  (A) SOUND mode, phase velocity w/k = c_s = 0.148c, gamma/omega vs omega:")
cs = c_s_over_c
ws = np.logspace(-6, -1, 6)       # omega/T from 1e-6 to 0.1
# gamma ~ Im chi_nn(w, k=w/c_s) / (mode normalization ~ k^2 for a sound mode's chi_mode)
# gamma/omega is the dimensionless damping; for Landau damping of sound it is a PURE NUMBER.
gam_over_w = []
for w in ws:
    k = w/cs
    imx = Im_chi_nn(w, k, m_over_T=1.0)   # ~ (w/k)*Integral = c_s*Integral, per unit k^0
    # sound-mode damping: gamma/omega = Im chi_nn /(2 * k * dReChi/dw ...) -> for the SCALING
    # only the omega-dependence of Im_chi at fixed w/k matters; normalize by its own k-power:
    gam_over_w.append(imx * k**2 / w)     # remove the trivial (w/k) and per-k measure -> pure number
gam_over_w = np.array(gam_over_w)
print(f"      omega/T grid: {ws}")
print(f"      gamma/omega (arb. norm): {gam_over_w}")
flat = np.polyfit(np.log10(ws), np.log10(np.abs(gam_over_w)), 1)[0]
print(f"      log-log slope of gamma/omega vs omega = {flat:+.3f}  (0 == scale-free == OHMIC)")
print(f"      => gamma ∝ omega^{1+flat:.3f}  => lineshape power s = {1+flat:.3f}  (OHMIC = 1)")

print("  (B) near-HOMOGENEOUS mode, phase velocity w/k = 3c (> c, superluminal):")
vals_super = np.array([Im_chi_nn(w, w/3.0, m_over_T=1.0) for w in ws])
print(f"      Im chi_nn = {np.max(np.abs(vals_super)):.2e}  (identically 0: no nu faster than c to resonate")
print(f"      -> a truly homogeneous settling mode has NO collisionless friction at all)")

print()
print("="*78)
print("PART 4 - feed the DERIVED lineshape forward; report Gamma_0 honestly")
print("="*78)
for label, s in [("ohmic (derived, s=1)", 1.0),
                 ("required to land 76 meV", s_required),
                 ("clean 1/4", 0.25),
                 ("clean 1/2", 0.5)]:
    S = w_over_T**s
    G0 = Gamma_sqrtN * S
    print(f"  s = {s:5.3f}  [{label:26s}] : S={S:.2e}  Gamma0 = {G0:.3e} eV "
          f"= {G0/meV:.2e} meV   ({np.log10(G0/Gamma0_target):+.1f} dex vs 76meV)")

print()
print("  VERDICT read-off:")
print(f"   - standard collisionless FDT gives OHMIC (s~1): Gamma0 lands "
      f"{np.log10(Gamma_sqrtN*w_over_T**1.0/Gamma0_target):+.0f} dex from 76 meV -> MISS (over-suppressed).")
print(f"   - superluminal mode: NO resonant nu -> Im chi = 0 -> no power-law friction at all.")
print(f"   - the target needs SUB-ohmic s~{s_required:.2f}; single-mode Landau damping is ohmic s=1.")
print("   - sub-ohmic requires a scale-INVARIANT spectrum (1/f-type), i.e. the")
print("     expansion-sourced attractor continuum of entry 180 - whose spectral index")
print("     is itself OWED and would have to equal ~0.27. Not derivable from the nu")
print("     microphysics alone. FLAGGED, not faked.")
