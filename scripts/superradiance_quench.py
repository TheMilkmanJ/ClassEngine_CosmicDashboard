"""#156 — THE LAMBDA-QUENCH, RE-DERIVED AT THE MODEL'S OWN QUARTIC AND MASS.

The atlas (PRTOE_INTERACTION_ATLAS.md) priced the superradiance shield as a rate balance
Gamma_SR ~ alpha_g^9 m against Gamma_nl ~ lambda^2 N^2 alpha_g^p m, with p SWEPT over [5,15].
This script resolves p instead of sweeping it, and re-runs the margin at the recorded
m = 2.24e-20 eV and lambda = 2e-91.

WHICH QUARTIC (settled before any margin is quoted).  Two candidates were on the table:
  lambda_dyad ~ 1.3e-38  — me_mechanism_math.md:398, = |m^2_CW(0)|/2f^2.  This is the quartic
      of the HIGH-f Coleman-Weinberg field phi whose VEV f ~ 3e14 eV sets m_e.  That field's
      own mass is 3.1-6.9e-5 eV (me_mechanism_math.md, roll time 1/m_phi = 2.4e-11 s), i.e.
      a Compton wavelength of centimetres.  It cannot form a gravitational atom around a
      10^9 M_sun hole, which needs a Compton wavelength of order the gravitational radius
      (~0.3 pc).  It is not bare-vs-effective: it is a DIFFERENT FIELD, 15 decades heavier.
  lambda ~ 2e-91         — DERIVATION_HUNT.md:483, "the ultralight field's axion quartic",
      the quartic OF the m = 2.24e-20 eV boson.  This is the only one that can enter.
Convention: lambda is the (lambda/4!)phi^4 normalization, equivalently lambda = m^2/f_eff^2,
which is what the corpus's own f_eff = m/sqrt(lambda) and rho_bounce = m^4/lambda bookings use.

RESOLVING p.  The depleting process for the dominant l=m=1 (211) cloud is fixed by kinematics.
With E_n = -m alpha_g^2/(2n^2), a final free quantum needs 2E_211 - E_bound > 0, i.e.
1/(2n^2) > 1/4, i.e. n = 1 exactly.  So the process is |211>|211> -> |100>|k>, with
E_k = +m alpha_g^2/4 and k = m alpha_g/sqrt(2).  Fermi's golden rule with the contact vertex
g = lambda/(16 m^2) and hydrogenic wavefunctions (Bohr radius a = 1/(m alpha_g)) gives

    Gamma_nl (per particle) = (8/(256 sqrt(2) pi)) C^2 lambda^2 N m alpha_g^4

    ==> p = 4, and the N-power is 1, not 2.

The overlap C is dimensionless and O(1): the outgoing momentum satisfies k*a = 1/sqrt(2), so
there is no centrifugal suppression, and the gravitational Coulomb parameter of the outgoing
wave is eta = -alpha_g m/k = -sqrt(2), independent of alpha_g -- no hidden powers of alpha_g.

THE NORMALIZATION BUG THIS EXPOSES.  The atlas's N^2 is a TOTAL event rate, not a per-particle
rate, and it was balanced against a PER-PARTICLE Gamma_SR.  Balancing like with like:
    total growth   Gamma_SR * N  =  C_SR alpha_g^9 m N
    total events   R             =  c_nl lambda^2 N^2 m alpha_g^4
    ==> N_eq = (C_SR/c_nl) alpha_g^(9-p) / lambda^2       with p = 4
The atlas instead had N_eq ~ alpha_g^((9-p)/2) / lambda -- one power of lambda short.  That
understated the damage of the lambda move by a factor of 2 in the exponent.

Run: python3 scripts/superradiance_quench.py
"""
import math

# ---- recorded inputs (every one cited to its source) ------------------------
M_EV    = 2.24e-20          # eV   -- the recorded ultralight mass (MATH_SPINE.md:389)
LAM     = 2e-91             #      -- the ultralight field's quartic (DERIVATION_HUNT.md:483)
MPL     = 1.220890e28       # eV   -- non-reduced Planck mass (audit_math_pass.py:13)
MSUN    = 1.98892e30 * 5.6095886e35   # kg -> eV (audit_math_pass.py:399)
ASTAR   = 1.0               #      -- shield-favourable: maximal spin => largest N_spindown

def alpha_g(M_msun, m_eV=M_EV):
    """alpha_g = G M m / (hbar c) = M m / M_Pl^2."""
    return M_msun * MSUN * m_eV / MPL**2

def M_of_alpha(ag, m_eV=M_EV):
    return ag * MPL**2 / m_eV / MSUN

# ---- the two rates ---------------------------------------------------------
C_SR   = 1/24.0                          # Detweiler: Gamma_211 = (1/24) a_* alpha_g^9 m
C_NL   = 8.0/(256*math.sqrt(2)*math.pi)  # = 7.04e-3, derived above (C = 1)

def N_eq(ag, lam=LAM, C_overlap=1.0):
    """Occupation at which self-interaction depletion balances superradiant growth."""
    return (C_SR*ASTAR/(C_NL*C_overlap**2)) * ag**5 / lam**2

def N_spindown(ag):
    """Quanta needed to carry off the hole's spin: J = a_* M^2/M_Pl^2, each quantum m=1."""
    return ASTAR * ag * M_of_alpha(ag)*MSUN / M_EV

def N_bosenova(ag, lam=LAM):
    """|self-interaction energy| = |binding energy| per particle (needs ATTRACTIVE lam)."""
    return 2.0/(lam*ag)

# Cross-check on N_bosenova/N_spindown: the closed form is (2/a_*)(f_eff/M_Pl)^2/alpha_g^3,
# which is the Arvanitaki-Dubovsky (f/M_Pl)^2/alpha_g^3 structure -- an independent handle
# on the same ratio, reproducing the direct quotient to machine precision.
def bosenova_ratio_closed(ag, lam=LAM):
    return (2.0/ASTAR)*((M_EV/math.sqrt(lam))/MPL)**2/ag**3

# INDEPENDENT CONFIRMATION OF p = 4, by kinetic theory instead of Fermi's golden rule.
# Gamma_nl = n <sigma v> with n = N/V the cloud density, V = C_V a^3, a = 1/(m alpha_g);
# the contact scattering length is a_s = lambda/(32 pi m), sigma = 8 pi a_s^2 for identical
# bosons, and the virial velocity in the atom is v ~ alpha_g.  Then
#   Gamma_nl = [N (m alpha_g)^3/C_V] * [lambda^2/(128 pi m^2)] * alpha_g
#            = lambda^2 N m alpha_g^4 / (128 pi C_V)
# -- the same lambda^2 N^1 m alpha_g^4, i.e. p = 4, from a route that never mentions the
# 211/100 final state.  The two prefactors agree to a factor of ~3 (C_V = 1), which is the
# honest size of the O(1) uncertainty and is 85 decades short of mattering.
C_NL_KINETIC = 1.0/(128*math.pi)

HBAR_EVS = 6.582119569e-16   # eV*s
YR_S     = 3.1557e7          # s

def Gamma_SR(ag):
    """Detweiler l=m=1 growth rate, in s^-1."""
    return C_SR*ASTAR*ag**9 * (M_EV/HBAR_EVS)

def bosenova_spindown_yr(ag, frac_lost=0.05):
    """IF the quartic were attractive: bosenova does not stop spin-down, it paces it.
    Cost = initial growth to N_bosenova, then one regrowth per burst."""
    n_cycles = N_spindown(ag)/N_bosenova(ag)
    t_initial = math.log(N_bosenova(ag))/Gamma_SR(ag)
    t_cycle   = math.log(1/(1-frac_lost))/Gamma_SR(ag)
    return (t_initial + n_cycles*t_cycle)/YR_S, n_cycles

# ---- the margin across the registered band P-2026-034 ----------------------
BAND = (0.1, 0.3, 0.5)      # alpha_g edges and centre of P-034 (6e8 - 3e9 M_sun)

def margin(ag, lam=LAM, C_overlap=1.0):
    """log10(N_spindown / N_eq).  Positive = the cloud saturates before it can spin the
    hole down = the quench shields.  Negative = no shield."""
    return math.log10(N_spindown(ag)/N_eq(ag, lam, C_overlap))

# ---- what lambda WOULD be needed -------------------------------------------
def lam_needed(ag):
    """Smallest lambda for which N_eq <= N_spindown (the quench just barely shields)."""
    return math.sqrt((C_SR*ASTAR/C_NL) * ag**5 / N_spindown(ag))

def f_eff(lam):
    """f_eff = m/sqrt(lambda), in GeV."""
    return (M_EV*1e-9)/math.sqrt(lam)

if __name__ == "__main__":
    print(__doc__.split("Run:")[0])
    print(f"{'alpha_g':>8} {'M/Msun':>11} {'N_spindown':>11} {'N_eq':>11} "
          f"{'margin(dex)':>12} {'N_bosenova':>11} {'N_bn/N_sd':>11}")
    for ag in BAND:
        print(f"{ag:8.2f} {M_of_alpha(ag):11.3e} {N_spindown(ag):11.3e} {N_eq(ag):11.3e} "
              f"{margin(ag):12.1f} {N_bosenova(ag):11.3e} "
              f"{N_bosenova(ag)/N_spindown(ag):11.3e}")
    print()
    print(f"  f_eff at the recorded lambda        = {f_eff(LAM):.3g} GeV")
    for ag in BAND:
        print(f"  lambda needed to shield at ag={ag:.1f}  = {lam_needed(ag):.3g} "
              f"  (f_eff <= {f_eff(lam_needed(ag))*1e9:.3g} eV)")
    print(f"  decades of lambda short (ag=0.3)    = "
          f"{math.log10(lam_needed(0.3)/LAM):.1f}")
    print()
    print("  sensitivity: no O(1) rescues this. C^2 would have to be ~1e85 --")
    for c2 in (1e2, 1.0, 1e-2):
        print(f"    C^2 = {c2:<6g}  margin(ag=0.3) = {margin(0.3, C_overlap=math.sqrt(c2)):.1f} dex")
    print()
    print(f"  p = 4 by two independent routes; prefactors {C_NL:.3e} (golden rule) vs "
          f"{C_NL_KINETIC:.3e} (kinetic), ratio {C_NL/C_NL_KINETIC:.2f}")
    print("  how much of the kill is p, and how much is the lambda-power fix?")
    for ag in BAND:
        old = math.log10(N_spindown(ag)/(ag**((9-4)/2)/LAM))   # atlas form, evaluated at p=4
        print(f"    ag={ag:.1f}: atlas form at p=4 gives {old:+.1f} dex; "
              f"corrected {margin(ag):+.1f} dex; the lambda power is worth "
              f"{old-margin(ag):.1f}")
    print()
    print("  the bosenova branch (only available if the quartic is ATTRACTIVE):")
    for ag in BAND:
        t_yr, n_cyc = bosenova_spindown_yr(ag)
        print(f"    ag={ag:.1f}: closed-form ratio {bosenova_ratio_closed(ag):.3e} "
              f"(direct {N_bosenova(ag)/N_spindown(ag):.3e}); {n_cyc:.0f} bursts, "
              f"spin-down still completes in {t_yr:.2e} yr")
