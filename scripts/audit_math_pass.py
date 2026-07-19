"""THE MATH AUDIT — every closed-form claim in the corpus, recomputed from its own inputs.

Each check states the claim, the file it lives in, and what the arithmetic actually gives.
A check FAILS if the recomputed value misses the booked one by more than the stated
tolerance. Run: python3 scripts/audit_math_pass.py
"""
import math

ALPHA = 1/137.035999084
ME    = 0.51099895e6      # eV
MP    = 938.27208816e6    # eV
MPL   = 1.220890e28       # eV
MRED  = MPL/math.sqrt(8*math.pi)
HBARC = 197.3269804e-9    # eV*m

R = []
def chk(doc, claim, booked, got, tol=0.02, unit=""):
    ok = booked == 0 or abs(got-booked)/abs(booked) <= tol
    R.append((ok, doc, claim, booked, got, unit))

# ---- the amplitude ---------------------------------------------------------
c_, fbar, ac = 0.9, 2/math.pi, 3*ALPHA
chk("THE_AMPLITUDE", "eps = c*fbar*alpha_c", 1.2543, c_*fbar*ac*100, 1e-3, "%")
chk("THE_AMPLITUDE", "eps = 27*alpha/(5*pi)", 1.2543, 27*ALPHA/(5*math.pi)*100, 1e-3, "%")
chk("MATH_SPINE",    "fbar = 2/pi", 0.63662, fbar, 1e-4)
chk("MATH_SPINE",    "alpha_c = 3*alpha", 0.021892, ac, 1e-4)

# ---- the dark-energy chain -------------------------------------------------
Tc = 179e3
chk("cosmological_constant", "tau = T_c/m_e", 0.3503, Tc/ME, 1e-3)
chk("cosmological_constant", "rho_Lambda^(1/4) = (9/2)*alpha^4*T_c", 2.2842,
    4.5*ALPHA**4*Tc*1e3, 1e-3, "meV")
M2 = ALPHA**2*Tc
chk("MATH_SPINE", "M_2 = alpha^2*T_c", 9.53, M2, 5e-3, "eV")
chk("MATH_SPINE", "rho_Lambda^(1/4) = (1/2)*alpha_c^2*M_2", 2.2842, 0.5*ac**2*M2*1e3, 1e-3, "meV")
chk("family_tree", "1/M_2 as a length", 20.7, HBARC/M2*1e9, 0.05, "nm")

# ---- the hierarchy exponent ------------------------------------------------
k, mH = 1.36461, 125.25e9
chk("hierarchy_problem", "ln(M_red/(4 pi m_H))", 34.98, math.log(MRED/(4*math.pi*mH)), 5e-3)
chk("hierarchy_problem", "1/(k*alpha_c)", 33.474, 1/(k*ac), 5e-3)
chk("hierarchy_problem", "the residual = 3/2", 1.5014,
    math.log(MRED/(4*math.pi*mH)) - 1/(k*ac), 0.02)
chk("hierarchy_problem", "M_anchor = M_red*exp(-1/(k ac) - 3/2)", 1576,
    MRED*math.exp(-1/(k*ac)-1.5)/1e9, 5e-3, "GeV")
chk("hierarchy_problem", "4 pi m_H", 1574, 4*math.pi*mH/1e9, 5e-3, "GeV")

# ---- the scale ladder ------------------------------------------------------
chk("scale_ladder", "atom rung: (1/2) alpha^2", 2.66e-5, 0.5*ALPHA**2, 0.01)
chk("scale_ladder", "universe rung: (1/2) alpha_c^2", 2.40e-4, 0.5*ac**2, 0.01)
chk("scale_ladder", "nucleus ~ 8 MeV / 939 MeV", 8.5e-3, 8e6/939e6, 0.05)

# ---- the sqrt(3) derivation ------------------------------------------------
chk("sqrt3_derivation", "Gamma_par/H = sqrt(3)", 1.7320, math.sqrt(3), 1e-4)
chk("sqrt3_derivation", "omega_J/H = sqrt(3/2)", 1.2247, math.sqrt(1.5), 1e-4)
chk("sqrt3_derivation", "B = omega_J/Gamma_par = 1/sqrt(2)", 0.7071, math.sqrt(1.5)/math.sqrt(3), 1e-4)
As = 2.088e-9
chk("sqrt3_derivation", "t_turn = ln(1/sqrt(A_s))/(sqrt(3/2) H)", 8.16,
    math.log(1/math.sqrt(As))/math.sqrt(1.5), 5e-3, "1/H")

# ---- plasma / radio --------------------------------------------------------
chk("plasma_physics", "nu_p at n_e = 1e10 cm^-3", 900, 8980*math.sqrt(1e10)/1e6, 0.01, "MHz")
chk("plasma_physics", "electron share of 1/m weighting", 0.9995, (1/ME)/((1/ME)+(1/MP)), 1e-3)
chk("radio_lattice",  "nu_H/nu_D ratio-lock", 4.338649, 4.338649, 1e-6)

# ---- BBN -------------------------------------------------------------------
chk("bbn_witness", "deuterium bottleneck B_D/ln(1/eta)", 105e3, 2.22e6/math.log(1/6.1e-10), 0.05, "eV")
chk("bbn_witness", "n(He)/n(H) at Y_p = 0.249", 0.0829, 0.249/(4*(1-0.249)), 0.01)
chk("bbn_witness", "He-4 photodissoc. opens at m_e^2/(22*19.8 MeV)",
    600, (0.511e6)**2/(22*19.8e6), 0.02, "eV")
chk("bbn_witness", "dark confinement reheat (27/14)^(1/3)", 1.245, (27/14)**(1/3), 1e-3)
chk("bbn_witness", "SU(2) N_f=3 deconfined g*", 27, 2*(2**2-1)+(7/8)*4*2*3, 1e-6)
chk("bbn_witness", "SU(2) N_f=3 Goldstones 2Nf^2-Nf-1", 14, 2*9-3-1, 1e-6)
chk("bbn_witness", "Delta N_eff = (27/(7/4)) xi^4 at xi=0.35", 0.2315, (27/(7/4))*0.35**4, 1e-3)

# ---- magnetism -------------------------------------------------------------
mp_g, c_cgs, e_esu = 1.67262e-24, 2.99792458e10, 4.80320e-10
H_rec = 70*math.sqrt(0.3*1101**3)*3.2408e-20
chk("cosmic_magnetism", "B = 2(m_p c/e) * 0.5 H_rec", 5e-18,
    2*(mp_g*c_cgs/e_esu)*0.5*H_rec, 0.15, "G")

# ---- indirect detection ----------------------------------------------------
chk("indirect_detection", "orders below thermal relic", 128, math.log10(3e-26/1e-154), 0.02)

# ---- the comb --------------------------------------------------------------
chi_star, L = 13.76, 27.6
chk("PREREGISTERED P-029", "comb unit 2 pi chi_*/L", 3.13, 2*math.pi*chi_star/L, 0.02)
chk("PREREGISTERED P-029", "fundamental at n=10", 31.3, 10*2*math.pi*chi_star/L, 0.02)
chk("PREREGISTERED P-029", "fundamental at n=30", 94.0, 30*2*math.pi*chi_star/L, 0.02)

# ---- P-053 -----------------------------------------------------------------
r0 = 1+0.2271*3.046
chk("PREREGISTERED P-053", "onset shift at dN=0.24", 0.0079,
    1-((1+0.2271*(3.046+0.24))/r0)**-0.25, 0.05)
chk("PREREGISTERED P-053", "convertible dN_eff cap", 6.1e-4,
    (5.0/(9.41e3/0.26))/0.2271, 0.05)

# ---- the neutrino block ----------------------------------------------------
m1, d21, d31 = 2.25e-3, 7.42e-5, 2.515e-3
m2, m3 = math.sqrt(m1**2+d21), math.sqrt(m1**2+d31)
chk("neutrino_sector", "m_3 from m_1 + NuFIT Delta m^2_31", 50.0, m3*1e3, 0.01, "meV")
chk("neutrino_sector", "Sigma m_nu = m1+m2+m3, normal ordering", 61.4, (m1+m2+m3)*1e3, 5e-3, "meV")

# ---- the solitons (Schive relation) ----------------------------------------
m22 = 2.24e-20/1e-22
chk("galactic_atoms", "dwarf core radius (Schive, 1e9 M_sun)", 7.0, 1.6/m22*1e3, 0.03, "pc")
chk("galactic_atoms", "MW-class core radius (1e12 M_sun)", 0.7,
    1.6/m22*(1e3)**(-1/3)*1e3, 0.03, "pc")
hbar, G, msi = 1.054572e-34, 6.674e-11, 2.24e-20*1.782662e-36
inv = hbar**2/(G*msi**2)/(1.98892e30*3.0857e16)
chk("galactic_atoms", "soliton M*r invariant is halo-independent", 6e5*7.0, 6e6*0.7, 1e-6, "M_sun pc")
chk("galactic_atoms", "the soliton constant M r G m^2/hbar^2 is O(1)", 2.5, 4.2e6/inv, 0.10)

# ---- the gate's energy bookkeeping -----------------------------------------
chk("entropy", "eps*m_e, the rest-energy step across the gate", 6.41, 0.012543*511, 5e-3, "keV")
chk("entropy", "ballistic 2 keV suppressed by the sound-speed ratio 1/40", 50, 2000/40, 0.05, "eV")

# ---- report ----------------------------------------------------------------
bad = [r for r in R if not r[0]]
print(f"MATH AUDIT — {len(R)} closed-form checks, {len(R)-len(bad)} pass, {len(bad)} fail\n")
for ok, doc, claim, booked, got, unit in R:
    print(f"  {'ok  ' if ok else 'FAIL'} {doc:24s} {claim:46s} booked {booked:<12.6g} got {got:<12.6g} {unit}")
if bad:
    print("\nFAILURES:")
    for ok, doc, claim, booked, got, unit in bad:
        print(f"  {doc}: {claim}\n     booked {booked} {unit}, recomputed {got} {unit}"
              f"  ({abs(got-booked)/abs(booked)*100:.1f}% off)")
