"""rho_bounce — the finite bounce/core density that discharges the 'no singularity' claim.

WHAT IS OWED (docs/PRTOE_no_singularities.md sec 5, docs/PRTOE_bigbang_no_singularity.md):
    lambda (the medium's repulsive amplitude quartic) sets the density at which a crunch/core
    halts and reverses.  The BH-SUPPORT requirement is already priced elsewhere (audit_math_pass
    'blackholes 8': lambda >~ 8e-94 holds up the largest known holes, 2e10 M_sun).  What this
    script computes is the DENSITY at that equilibrium -- rho_bounce.

THE MECHANISM (Colpi-Shapiro-Wasserman, PRL 57 2485 1986).  A repulsive-quartic condensate in
the Thomas-Fermi limit is an n=1 polytrope, p = K rho^2 with K = lambda/(8 m^4).  Its central
density RISES with mass (rho_c ~ M at fixed core radius) until the pressure turns relativistic
(p ~ rho) at the maximum-mass configuration, where it saturates at the ceiling

        rho_bounce  =  m^4 / lambda   =   m^2 Psi0^2         (Psi0 = f_eff = m/sqrt(lambda))

This is NOT the naive 'condensate density' m^4 with lambda~O(1); it is the CSW ceiling at the
medium's own tiny gravitational-scale quartic lambda = (m/Psi0)^2, which is why it lands keV-class
rather than sub-eV.  The same ceiling is the cosmological bounce density (the whole-universe crunch
has no 'mass', so it reaches the ceiling directly).

INPUTS (recorded; both ride open numbers -- m is roster-trial-conditional, lambda rides the CMB
amplitude ceiling Psi0 and alpha_c = 3a):
    m      = 2.24e-20 eV        the ultralight medium boson
    lambda = 2e-91   = (m/Psi0)^2, the amplitude quartic (superradiance_quench.py, bounce_bkl_stiff_check.py)

VERDICT: the number is computed and finite (~100 orders sub-Planckian -> 'no singularity' holds).
What stays genuinely OPEN is the bounce DYNAMICS, not this number: the cosmological crunch must
fund an MeV-class hot start over this keV-class condensate floor (a ~12-order gap), which the model
carries as an un-simulated two-component split (condensate quartic floor + Tolman-kept radiation).
"""
import math

# ---- recorded inputs ---------------------------------------------------------------------
m      = 2.24e-20          # eV   -- medium boson mass
lam    = 2e-91             # (m/Psi0)^2 -- repulsive amplitude quartic (lambda/4! phi^4 convention)
M_PL   = 1.220890e19       # GeV  -- full Planck mass
M_PL_eV = M_PL * 1e9
M_sun_GeV = 1.116e57       # GeV  -- solar mass
M_sun_eV  = M_sun_GeV * 1e9

# ---- unit conversion: 1 GeV^4 -> g/cm^3 (energy density as mass density) ------------------
#   verified against rho_crit: (8.53e-30 g/cc)/(2.3201e17) = 3.68e-47 GeV^4 -> ^(1/4)=2.46 meV  OK
GEV4_TO_GCC = 2.3201e17

def gcc(rho_eV4):   return rho_eV4 * 1e-36 * GEV4_TO_GCC          # eV^4 -> g/cm^3
def q(rho_eV4):     return rho_eV4 ** 0.25                        # eV^4 -> eV (quarter power)

# ---- the number -------------------------------------------------------------------------
Psi0      = m / math.sqrt(lam)                 # eV -- field amplitude / decay constant f_eff
rho_eV4   = m**4 / lam                          # eV^4
assert abs(rho_eV4 / (m**2 * Psi0**2) - 1) < 1e-9, "m^4/lam must equal m^2 Psi0^2"
rho_GeV4  = rho_eV4 * 1e-36
rho_gcc   = gcc(rho_eV4)

# ---- reference scales -------------------------------------------------------------------
RHO_NUCLEAR = 2.3e14        # g/cm^3
RHO_PLANCK  = 5.155e93      # g/cm^3
def bbn_gcc(T_MeV, gstar=10.75):
    return gcc((math.pi**2/30) * gstar * (T_MeV*1e6)**4)     # radiation density at temperature T

# ---- CSW mechanism cross-checks ---------------------------------------------------------
Lambda_TF = lam * M_PL_eV**2 / (4*math.pi*m**2)             # TF parameter; >>1 => self-interaction regime
rho_ceiling_relativistic = 8 * m**4 / lam                   # p~rho ceiling, EoS p = (lam/8m^4) rho^2
# Newtonian n=1 polytrope central density at the max-mass anchor M ~ 2e10 M_sun:
#   a = sqrt(lam) M_Pl / (4 sqrt(pi) m^2)  (mass-independent core radius);  rho_c = 16 m^6 M / (sqrt(pi) lam^1.5 M_Pl^3)
M_anchor = 2e10 * M_sun_eV
a_core_eVinv = math.sqrt(lam)*M_PL_eV/(4*math.sqrt(math.pi)*m**2)
a_core_m     = a_core_eVinv * 1.973269804e-7               # eV^-1 -> m
rho_c_anchor = 16*m**6*M_anchor/(math.sqrt(math.pi)*lam**1.5*M_PL_eV**3)   # eV^4


if __name__ == "__main__":
    print("=" * 78)
    print("rho_bounce  =  m^4/lambda  =  m^2 Psi0^2   (Colpi-Shapiro-Wasserman quartic ceiling)")
    print("=" * 78)
    print(f"  inputs : m = {m:.3e} eV,  lambda = {lam:.1e} = (m/Psi0)^2")
    print(f"  Psi0 = f_eff = m/sqrt(lambda) = {Psi0:.3e} eV = {Psi0/1e9:.2e} GeV = {Psi0/M_PL_eV:.1e} M_Pl")
    print()
    print(f"  rho_bounce = {rho_eV4:.3e} eV^4")
    print(f"             = {rho_GeV4:.3e} GeV^4")
    print(f"             = {rho_gcc:.3e} g/cm^3")
    print(f"  rho_bounce^(1/4) = {q(rho_eV4):.0f} eV = {q(rho_eV4)/1e3:.2f} keV")
    print()
    print("  SANITY (must be finite and sub-Planckian for 'no singularity' to mean anything):")
    print(f"    vs Planck  {RHO_PLANCK:.2e} g/cc : {math.log10(RHO_PLANCK/rho_gcc):5.0f} orders BELOW  -> finite, sub-Planckian  [OK]")
    print(f"    vs nuclear {RHO_NUCLEAR:.2e} g/cc : {math.log10(RHO_NUCLEAR/rho_gcc):5.0f} orders BELOW nuclear")
    for T in (1, 2, 4):
        print(f"    vs BBN hot-start T={T} MeV ({bbn_gcc(T):.1e} g/cc): {math.log10(bbn_gcc(T)/rho_gcc):4.0f} orders BELOW  <- the open joint")
    print()
    print("  MECHANISM CROSS-CHECK (m^4/lambda IS the CSW max-mass central density, not a halo core):")
    print(f"    TF parameter Lambda = lam M_Pl^2/(4pi m^2) = {Lambda_TF:.0f}  (>>1 => self-interaction/TF regime)")
    print(f"    relativistic ceiling 8 m^4/lam           : rho^(1/4) = {q(rho_ceiling_relativistic):.0f} eV")
    print(f"    Newtonian polytrope at M = 2e10 M_sun     : rho^(1/4) = {q(rho_c_anchor):.0f} eV   (core radius {a_core_m:.1e} m)")
    print(f"    corpus value m^4/lam                      : rho^(1/4) = {q(rho_eV4):.0f} eV   -> bracketed, CONSISTENT")
    print(f"    (rho_c scales as M in the TF regime; only the M ~ 2e10 M_sun anchor reaches the ceiling)")
    print()
    print("  GRADE: number computed & finite; the OPEN item is the two-component bounce dynamics")
    print("         (keV condensate floor vs MeV hot start), un-simulated.  See PRTOE_bigbang_no_singularity.md.")

    # cross-validation asserts (this file doubles as a test)
    assert 1e-7 < rho_gcc < 1e-6,            "rho_bounce must be ~3e-7 g/cm^3"
    assert 1000 < q(rho_eV4) < 1100,         "rho_bounce^(1/4) must be ~1.06 keV"
    assert rho_gcc < RHO_PLANCK,             "must be sub-Planckian"
    assert Lambda_TF > 1,                    "TF/self-interaction regime must hold"
    assert q(rho_c_anchor) < q(rho_eV4) < q(rho_ceiling_relativistic), \
        "corpus value must sit between polytrope anchor and relativistic ceiling"
    print("\n  all cross-validation asserts pass.")
