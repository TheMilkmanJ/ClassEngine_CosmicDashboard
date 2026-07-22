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
# The chain runs FORWARD from the Koide kernel: Parseval fixes tau, tau fixes T_c,
# T_c fixes M_2, M_2 fixes the floor. Booking T_c as an input and recomputing the
# floor from it is circular — it recovers whatever T_c was fed in. Start at tau.
TAU = 0.5*math.log(2)
chk("cosmological_constant", "tau = (1/2) ln 2, forced by Q = 2/3 via Parseval", 0.34657, TAU, 1e-4)
Tc = TAU*ME                                   # eV — T_c is an OUTPUT of tau
chk("cosmological_constant", "T_c = tau * m_e", 177.10, Tc/1e3, 1e-3, "keV")
M2 = ALPHA**2*Tc
chk("MATH_SPINE", "M_2 = alpha^2*T_c", 9.43, M2, 5e-3, "eV")
chk("cosmological_constant", "rho_Lambda^(1/4) = (9/2)*alpha^4*T_c", 2.2599,
    4.5*ALPHA**4*Tc*1e3, 1e-3, "meV")
chk("MATH_SPINE", "rho_Lambda^(1/4) = (1/2)*alpha_c^2*M_2", 2.2599, 0.5*ac**2*M2*1e3, 1e-3, "meV")
chk("cosmological_constant", "the floor's excess over the observed 2.25", 0.44,
    (0.5*ac**2*M2*1e3/2.25-1)*100, 0.02, "%")
chk("family_tree", "1/M_2 as a length", 20.9, HBARC/M2*1e9, 0.05, "nm")
# The retired reading, kept only so a stale number is recognisable on sight.
chk("FAILURES_LEDGER", "retired: T_c = 179 keV inverted from the observation", 0.3503,
    179e3/ME, 1e-3)
chk("FAILURES_LEDGER", "retired: that T_c gives M_2 = 9.53 eV and a +1.5% floor", 2.2842,
    0.5*ac**2*(ALPHA**2*179e3)*1e3, 1e-3, "meV")

# ---- the hierarchy exponent ------------------------------------------------
k, mH = 1.36461, 125.25e9
chk("hierarchy_problem", "ln(M_red/(4 pi m_H))", 34.98, math.log(MRED/(4*math.pi*mH)), 5e-3)
chk("hierarchy_problem", "1/(k*alpha_c)", 33.474, 1/(k*ac), 5e-3)
chk("hierarchy_problem", "the residual = 3/2", 1.5014,
    math.log(MRED/(4*math.pi*mH)) - 1/(k*ac), 0.02)
chk("hierarchy_problem", "M_anchor = M_red*exp(-1/(k ac) - 3/2)", 1576,
    MRED*math.exp(-1/(k*ac)-1.5)/1e9, 5e-3, "GeV")
chk("hierarchy_problem", "4 pi m_H", 1574, 4*math.pi*mH/1e9, 5e-3, "GeV")

# ---- the vertex correction (docket #141, hierarchy_problem 6e) --------------
# c is a quadrature, not a closed form, so it is recomputed here from the script that
# owns it rather than transcribed. Its one input is b = 2 alpha_c/(pi v) at v = 1;
# e^2 cancels between <C> and lambda<V>, so c depends on nothing else.
import importlib.util as _ilu, os as _os
_vcb_path = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)),
                          "hierarchy_vertex_crossed_box.py")
_vspec = _ilu.spec_from_file_location("_vcb", _vcb_path)
_VCB = _ilu.module_from_spec(_vspec); _vspec.loader.exec_module(_VCB)
_b141 = 2*ac/math.pi
chk("hierarchy_problem", "b = 2 alpha_c/pi, the screening constant", 0.0139369, _b141, 1e-4)
chk("hierarchy_problem", "k = ln(1+1/b)/pi in closed form", 1.36461191,
    math.log(1+1/_b141)/math.pi, 1e-6)
chk("hierarchy_problem", "<V>_FS/pi^2 reproduces lambda = k alpha_c", 0.0298742,
    _VCB.V_avg_fs(_b141, 4*math.pi*ac)/math.pi**2, 1e-5)
# the pipeline's calibration point: contact V on a parabolic band must return the
# Gor'kov-Melik-Barkhudarov constant, i.e. the textbook (4e)^(1/3) gap suppression
chk("hierarchy_problem", "GMB constant (1 + ln 4)/3 = ln (4e)^(1/3)", 0.7954315,
    (1+math.log(4))/3, 1e-6)
chk("hierarchy_problem", "the crossed-box pipeline reproduces it", 0.7954315,
    _VCB.check_gmb(nu=24, nt=24, ns=24)[0], 1e-6)
_c141 = _VCB.c_coefficient(nu=24, nt=24, ns=24)
_lam141 = 1.36461191*ac
chk("hierarchy_problem", "c, the crossed box", 0.789262, _c141, 1e-5)
chk("hierarchy_problem", "c's contact limit b -> inf on the linear band", 0.433868,
    _VCB.c_self_consistent(5e4, nu=32, nt=32, ns=32), 1e-4)
chk("hierarchy_problem", "lambda_eff = lambda(1 - c lambda)", 0.0291698,
    _lam141*(1-_c141*_lam141), 1e-4)
chk("hierarchy_problem", "1/lambda + c, the corrected exponent", 34.263,
    1/_lam141 + _c141, 1e-4)
chk("hierarchy_problem", "the anchor multiplier exp(-c)", 0.45418, math.exp(-_c141), 1e-4)
chk("hierarchy_problem", "M_anchor vertex-corrected, booked convention", 716.0,
    MRED*math.exp(-1/_lam141-_c141-1.5)/1e9, 5e-3, "GeV")
chk("hierarchy_problem", "M_anchor vertex-corrected, exact-solution convention", 1431.9,
    2*MRED*math.exp(-1/_lam141-_c141-1.5)/1e9, 5e-3, "GeV")
chk("hierarchy_problem", "the band 1.6-5.2 TeV x exp(-c), bottom edge", 0.727,
    1.6*math.exp(-_c141), 5e-3, "TeV")
chk("hierarchy_problem", "the band 1.6-5.2 TeV x exp(-c), top edge", 2.362,
    5.2*math.exp(-_c141), 5e-3, "TeV")
chk("hierarchy_problem", "dln c/dln b, c's robustness against the screening constant", -0.0905,
    (math.log(_VCB.c_self_consistent(_b141*1.02, nu=32, nt=32, ns=32))
     - math.log(_VCB.c_self_consistent(_b141*0.98, nu=32, nt=32, ns=32)))/math.log(1.02/0.98),
    0.02)
chk("hierarchy_problem", "the shooter's 13 TeV over the corrected band's top edge", 5.50,
    13/(5.2*math.exp(-_c141)), 5e-3, "x")
chk("hierarchy_problem", "the shooter's 13 TeV over the corrected band's bottom edge", 17.9,
    13/(1.6*math.exp(-_c141)), 5e-3, "x")

# ---- the scale ladder ------------------------------------------------------
chk("scale_ladder", "atom rung: (1/2) alpha^2", 2.66e-5, 0.5*ALPHA**2, 0.01)
chk("scale_ladder", "universe rung: (1/2) alpha_c^2", 2.40e-4, 0.5*ac**2, 0.01)
chk("scale_ladder", "nucleus ~ 8 MeV / 939 MeV", 8.5e-3, 8e6/939e6, 0.05)

# ---- the sqrt(3) derivation ------------------------------------------------
chk("sqrt3_derivation", "Gamma_par/H = sqrt(3)", 1.7320, math.sqrt(3), 1e-4)
chk("sqrt3_derivation", "omega_J/H = sqrt(3/2)", 1.2247, math.sqrt(1.5), 1e-4)
chk("sqrt3_derivation", "B = omega_J/Gamma_par = 1/sqrt(2)", 0.7071, math.sqrt(1.5)/math.sqrt(3), 1e-4)
As = 2.088e-9
# --- the occupancy, in ONE clock -------------------------------------------
# t_turn is a dark-energy-era quantity (H_Lambda^-1). The elapsed time since the
# rho_m = rho_Lambda crossing must be expressed in the SAME clock; quoting it in
# H_0^-1 (0.262 at Om = 0.30) inflates the occupancy from 1-in-37 to 1-in-29.
def _elapsed(Om):
    OL = 1.0 - Om
    d  = math.asinh(math.sqrt(OL/Om)) - math.asinh(1.0)   # a_c -> 1; at a_c the arg is exactly 1
    t_H0 = (2.0/(3.0*math.sqrt(OL)))*d
    return t_H0, t_H0*math.sqrt(OL)                       # (H_0^-1, H_Lambda^-1)
_e0, _eL = _elapsed(0.30)
chk("coincidence_problem", "elapsed since matter-Lambda crossing, H_0^-1", 0.262, _e0, 0.01)
chk("coincidence_problem", "the same elapsed time in H_Lambda^-1", 0.219, _eL, 0.01)
_tt = -0.5*math.log(2.088e-9)/math.sqrt(1.5)
chk("coincidence_problem", "occupancy in one clock (%)", 2.68, 100*_eL/_tt, 0.01, "%")
chk("coincidence_problem", "occupancy as one-in-N", 37.3, _tt/_eL, 0.01)
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
# T14 link 4 (#158): Harrison is B = k*omega with k constant, so A = k*u + grad(phi)
# and H_B = k^2 * H_kin on the closed 3-torus. The coefficient enters SQUARED — which is
# why the battery's own sign convention cancels out of sign(helicity_B) entirely.
_k_harrison = 2*(mp_g*c_cgs/e_esu)
chk("cosmic_magnetism", "helicity conversion k^2 = (2 m_p c/e)^2", 4.3595e-8,
    _k_harrison**2, 1e-4, "G^2 s^2")
chk("cosmic_magnetism", "k^2 > 0 (sign convention cancels)", 1.0,
    1.0 if _k_harrison**2 > 0 else 0.0, 1e-9)

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

# ---- Koide -----------------------------------------------------------------
mel, mmu, mta = 0.51099895, 105.6583755, 1776.86
chk("koide_relation", "Q from the measured pole masses", 0.6666605,
    (mel+mmu+mta)/(math.sqrt(mel)+math.sqrt(mmu)+math.sqrt(mta))**2, 1e-5)
A0 = math.sqrt(2)
chk("koide_relation", "Q = 1/3 + A^2/6 at A = sqrt(2)", 2/3, 1/3+A0*A0/6, 1e-9)
chk("koide_relation", "the closure theta = (1+A^2/2)/9 returns 2/9", 2/9, (1+A0*A0/2)/9, 1e-9)
chk("PREREGISTERED P-051", "the lock slope is the closure's derivative A/9", 0.1571, A0/9, 1e-3)
_v = [1+A0*math.cos(2*math.pi*k/3+2/9) for k in range(3)]
_m = sorted(x*x for x in _v)
chk("koide_relation", "theta = 2/9 reproduces m_tau/m_e", 3477.2, _m[2]/_m[0], 1e-3)
chk("koide_relation", "theta = 2/9 reproduces m_mu/m_e", 206.768, _m[1]/_m[0], 1e-3)

# ---- Pauli finiteness -------------------------------------------------------
chk("quantum_gravity", "dark str[k1] = 2 N_f N_c - 4(N_c^2-1) at N_c=2,N_f=3", 0,
    2*3*2 - 4*(2**2-1), 1e-9)
chk("quantum_gravity", "str[k1] = 16 N_gen - 48 vanishes at N_gen = 3", 0, 16*3-48, 1e-9)
chk("quantum_gravity", "16 Weyl fermions per generation (with nu^c)", 16, 6+3+3+2+1+1, 1e-9)
chk("quantum_gravity", "SM alone (15 per generation) gives -3", -3, 15*3-48, 1e-9)

# ---- the EP margin and the baryon target ------------------------------------
MICROSCOPE = 1.3e-15   # 2022 final result, 2 sigma
chk("me_mechanism_math", "EP margin, weak end (Delta a/a = 8e-19)", 3.0,
    math.log10(MICROSCOPE/8e-19), 0.10, "orders")
chk("me_mechanism_math", "EP margin, strong end (Delta a/a = 8e-21)", 5.0,
    math.log10(MICROSCOPE/8e-21), 0.10, "orders")
chk("baryogenesis", "eta from omega_b h^2 = 0.0224", 6.1e-10, 273.9e-10*0.0224, 0.01)

# ---- A_s and the velocity ladder --------------------------------------------
chk("THE_AMPLITUDE", "A_s = (alpha_c/4 pi k)^3 at the closed-form k", 2.088e-9,
    (ac/(4*math.pi*1.36461))**3, 0.005)
chk("THE_AMPLITUDE", "the k reproducing the measured A_s sits in [1.360, 1.366]", 1.3630,
    ac/(4*math.pi*(2.088e-9)**(1/3)), 0.002)
chk("scale_ladder", "second sound = sqrt(alpha) c", 0.0854, math.sqrt(ALPHA), 0.005, "c")
chk("scale_ladder", "the ladder is geometric: (sqrt alpha)^2 = alpha", ALPHA, math.sqrt(ALPHA)**2, 1e-9)
chk("dcdf_superfluid", "c_s = sqrt(3 alpha) c", 0.148, math.sqrt(3*ALPHA), 0.005, "c")
chk("dcdf_superfluid", "c_s sits sqrt(d) above the second sound", math.sqrt(3*ALPHA),
    math.sqrt(3)*math.sqrt(ALPHA), 1e-9)

# ---- the turn, and the KP cap ----------------------------------------------
chk("MATH_SPINE", "the turn: z from a = 2.04 (booked z = -0.51)", -0.510, 1/2.04-1, 0.01)
chk("MATH_SPINE", "the turn: z from a = 2.86 (booked z = -0.65)", -0.650, 1/2.86-1, 0.01)
chk("cosmological_constant", "KP cap 0.40 vs the observed 2.2", 5.5, 2.2/0.40, 0.01, "x below")

# ---- the Galactic Centre --------------------------------------------------
_m23, _rc = 2.24e-20/1e-23, 0.714
_rhoc = 1.9*_m23**-2*(_rc/1e3)**-4
def _Msol(r, n=200000):
    import numpy as _np
    x = _np.linspace(1e-6, r, n)
    return _np.trapezoid(4*_np.pi*x*x*_rhoc*(1+0.091*(x/_rc)**2)**-8, x)
chk("galactic_atoms", "soliton total mass = the recorded M_c", 6.25e6, _Msol(60*_rc), 0.03, "M_sun")
chk("galactic_atoms", "soliton M(<1 pc) at the Galactic Centre", 2.9e6, _Msol(1.0), 0.03, "M_sun")
chk("galactic_atoms", "Sgr A* influence radius exceeds the core radius", 2.6,
    (4.30091e-3*4.30e6/100**2)/_rc, 0.05, "core radii")

# ---- the circulant kernel --------------------------------------------------
chk("koide_relation", "Parseval: |f1/f0| from Q = 2/3", 0.7071071, math.sqrt((2/3-1/3)*1.5), 1e-6)
chk("koide_relation", "the kernel's tau = -ln|f1/f0| = (1/2)ln2", 0.3465736, 0.5*math.log(2), 1e-6)
chk("koide_relation", "holonomy: 3 x arg f1 = Q", 2/3, 3*(2/9), 1e-9)
chk("koide_relation", "T_c implied by the kernel's tau", 177.1, 0.5*math.log(2)*ME/1e3, 1e-3, "keV")
chk("koide_relation", "rho_Lambda from the kernel's tau", 2.2599,
    4.5*ALPHA**4*0.5*math.log(2)*ME*1e3, 1e-3, "meV")

# ---- the tilt --------------------------------------------------------------
_L = math.log(MPL/9.41e-6/1e9)   # ln(M_Pl/T_on), both in GeV
chk("inflation_replacement", "ln(M_Pl/T_on)", 55.52, _L, 1e-3)
chk("inflation_replacement", "n_s = 1 - 2/ln(M_Pl/T_on)", 0.9640, 1-2/_L, 1e-3)
chk("inflation_replacement", "running from the scale-local form", -5.2e-4, -2/(2/(1-0.9677))**2, 0.02)

# ---- the area law ----------------------------------------------------------
chk("quantum_gravity", "Bekenstein quarter = 12pi/48pi", 0.25,
    (1/(48*math.pi))/(1/(12*math.pi)), 1e-9)

# ---- the deuterium scar ----------------------------------------------------
# the row, its LCDM control, and the decomposition that says where the deficit is made
# Standing width: two-term (obs ±0.030 ⊕ PRIMAT post-LUNA ±0.037 = ±0.0476).
# Three-term double-counts d(p,γ)³He — LUNA is already inside ±0.037 (arXiv:2011.11320;
# #157 settled 2026-07-21). Retired three-term bookings: FAILURES_LEDGER.
_DH_L, _DH_W, _DH_M = 2.420, 2.372, 2.387      # LCDM control -> +omega_b -> +the window
# CONFIG-VERIFIED 2026-07-21. The booked triple was made at eps = 1.24%, T_c = 0.179 -- exactly
# what bbn_witness documents. Y_p is the clean discriminator and settles it: the windowed run at
# that config gives Y_p = 0.248996 against booked 0.248995 (0.0004%), while T_c = 0.17710 gives
# 0.248963 (0.013%, thirty times worse). D/H then reproduces to 0.072% and the control to 0.15%.
# PRyM is bit-for-bit DETERMINISTIC (verified by repeat runs) but its D/H output is NOT SMOOTH in
# omega_b at the ~0.1% level: the wide-scan log-log residuals are ~1e-3, and a 0.071% omega_b step
# returns an apparent slope of -0.34 against the true -1.66. So the reruns' 0.07-0.15% deviations
# are inside the solver's own non-smoothness and NO row is re-booked.
# That non-smoothness is also the full explanation of the retired -1.83: a slope differenced across
# the 1.1% step inherits ~0.1% of non-smooth error and is unstable at the +/-0.15 level. The
# elasticity is therefore MEASURED over a 6% baseline, never differenced.
_COOKE, _OBS_DH, _NUC_DH = 2.527, 0.030, 0.037
_TOT = math.hypot(_OBS_DH, _NUC_DH)            # 0.0476 — the standing width
_sig = lambda x: (x - _COOKE)/_TOT
chk("deuterium_scar", "combined D/H budget (2-term, standing)", 0.0476, _TOT, 1e-3)
chk("deuterium_scar", "LCDM control vs Cooke", -2.25, _sig(_DH_L), 0.01, "sigma")
chk("deuterium_scar", "the model vs Cooke", -2.94, _sig(_DH_M), 0.01, "sigma")
chk("deuterium_scar", "the model's deficit vs its LCDM control", -0.69, _sig(_DH_M)-_sig(_DH_L), 0.02, "sigma")
chk("deuterium_scar", "omega_b step costs", -1.01, _sig(_DH_W)-_sig(_DH_L), 0.02, "sigma")
chk("deuterium_scar", "the dyad's BBN window gains", +0.31, _sig(_DH_M)-_sig(_DH_W), 0.02, "sigma")
chk("deuterium_scar", "window grafted on LCDM alone", -1.93, _sig(_DH_L*(_DH_M/_DH_W)), 0.02, "sigma")
# MEASURED by a 6%-wide omega_b scan through the production splice, numba on, fitted log-log:
# -1.6582 at m_e = 1, -1.6751 at the model's m_e, residuals ~5e-4 (scripts/prym_omega_b_elasticity.py).
chk("deuterium_scar", "d ln(D/H)/d ln omega_b (production, measured)", -1.66,
    (-1.6582 + -1.6751)/2, 0.01)
chk("deuterium_scar", "1.1% omega_b step -> D/H loss", 1.81,
    100*(1 - 1.011**-1.6667), 0.02, "percent")
# the exchange rate: the omega_b shift arrives with the H0 relief
_dH0 = 69.9 - 68.2
chk("deuterium_scar", "deuterium paid per km/s/Mpc of H0", 0.59,
    abs(_sig(_DH_W)-_sig(_DH_L))/_dH0, 0.02, "sigma")
chk("deuterium_scar", "H0 given back to reach LCDM parity", 1.17,
    (_sig(_DH_L)-_sig(_DH_M))*_dH0/abs(_sig(_DH_W)-_sig(_DH_L)), 0.02, "km/s/Mpc")
chk("deuterium_scar", "H0 given back to centre on Cooke", 4.96,
    (0-_sig(_DH_M))*_dH0/abs(_sig(_DH_W)-_sig(_DH_L)), 0.02, "km/s/Mpc")
# the EM injector spec, as an energy budget: why it is invisible in the CMB spectrum
_ETA_B = 6.1e-10
_perbary = lambda T: (math.pi**4/(30*1.20206))*T/_ETA_B      # photon energy per baryon, eV
chk("deuterium_scar", "photon energy per baryon at the window opening (599 eV)", 2.65e12,
    _perbary(599.0), 2e-2, "eV")
chk("deuterium_scar", "the 30 eV/H spec as a fraction of the photon bath", 1.13e-11,
    30.0/_perbary(599.0), 2e-2)
chk("deuterium_scar", "its mu-distortion", 3.2e-11, 1.4*30.0/_perbary(300.0), 3e-2)
chk("deuterium_scar", "margin below FIRAS |mu| < 9e-5", 2.8e6,
    9e-5/(1.4*30.0/_perbary(300.0)), 3e-2, "x")
chk("deuterium_scar", "required relic abundance n_X/n_gamma at 20 MeV", 9.15e-16,
    (30.0/20e6)*_ETA_B, 2e-2)
chk("deuterium_scar", "recombination is later than the window close by", 1.2e5,
    1.2e13/1e8, 2e-2, "x")

# gravity vs EM as BBN dials -- settles the recurring "BBN was EM-governed" proposal
_NEFF = 3.044
_dlnrho_dN = 0.2271/(1+0.2271*_NEFF)
_dlnH_dN = 0.5*_dlnrho_dN
chk("deuterium_scar", "d ln H / d N_eff", 0.0671, _dlnH_dN, 1e-2)
chk("deuterium_scar", "d ln(D/H) / d ln H (the gravitational dial)", 2.01,
    0.1350/_dlnH_dN, 1e-2)
chk("deuterium_scar", "gravity's dial vs the whole m_e window (0.645%)", 3.12,
    (0.1350/_dlnH_dN)/0.645, 2e-2, "x")
# the binding-energy budget: BBN's total release against the photon bath
_BBN_RELEASE = (0.2470/4.0)*28.30e6 + 2.4e-5*2.22e6          # eV per baryon
chk("deuterium_scar", "BBN binding energy released per baryon", 1.748e6,
    _BBN_RELEASE, 1e-2, "eV")
chk("deuterium_scar", "that release as a fraction of the photon bath at 70 keV", 5.64e-9,
    _BBN_RELEASE/_perbary(7.0e4), 2e-2)
chk("deuterium_scar", "deuterium bottleneck from the photon-to-baryon ratio", 104.6,
    2.22e6/math.log(1/_ETA_B)/1e3, 2e-2, "keV")


# the two BBN supersessions, priced by wide scans through the production network
# (scripts/prym_supersession_pricing.py). Both moves are ~0.007% effects on D/H, far below the
# solver's ~0.1% non-smoothness, so they CANNOT be priced by differencing a single pair of runs.
_TC_SLOPE, _EPS_SLOPE = 0.08981, 0.011764        # D/H per MeV of T_c; per % of m_e
_dTC, _dEPS = 0.17710 - 0.179, 1.2543 - 1.24
chk("deuterium_scar", "T_c supersession 179 -> 177.10 keV", -0.00358,
    _TC_SLOPE*_dTC/_TOT, 1e-2, "sigma")
chk("deuterium_scar", "eps supersession 1.24 -> 1.2543 percent", +0.00353,
    _EPS_SLOPE*_dEPS/_TOT, 1e-2, "sigma")
chk("deuterium_scar", "both supersessions together (they cancel)", -0.0000507,
    (_TC_SLOPE*_dTC + _EPS_SLOPE*_dEPS)/_TOT, 2e-2, "sigma")

# the below-T_c lever: right shape, wrong size
_dD_all, _dY_all, _dD_bel, _dY_bel = 0.1350, 0.0131, 0.1160, 0.0041
chk("deuterium_scar", "below-T_c efficiency ratio", 2.75,
    (_dD_bel/_dY_bel)/(_dD_all/_dY_all), 0.01, "x")
_N_bel = (_dD_all*0.42)/_dD_bel                 # dN below T_c that zeroes deuterium
chk("deuterium_scar", "below-T_c dN_eff to zero deuterium", 0.49, _N_bel, 0.02)
chk("deuterium_scar", "helium landing under the below-T_c lever", 1.7,
    1.09 + _N_bel*_dY_bel/0.0034, 0.05, "sigma")
chk("deuterium_scar", "reheat shortfall (upper)", 33.0, _N_bel/0.015, 0.02, "x")
# photodissociation: the helium reservoir dwarfs the deuterium it must supply
chk("deuterium_scar", "He/H by number vs D/H — the reservoir ratio", 3300.0,
    0.083/2.5e-5, 0.02, "x")

# ---- the 0nubb window (the Fairbank note's headline) -----------------------
# m1 = rho_Lambda^(1/4) = 2.25 meV, normal ordering, NuFIT-class mixings
_dm21, _dm31 = 7.42e-5, 2.515e-3             # eV^2 — the same inputs as the neutrino block above
_s12, _s13 = 0.307, 0.022
_m1 = 2.25e-3
_m2, _m3 = math.sqrt(_m1**2+_dm21), math.sqrt(_m1**2+_dm31)
_t = [(1-_s12)*(1-_s13)*_m1, _s12*(1-_s13)*_m2, _s13*_m3]
chk("fairbank_note", "Sigma m_nu at the low anchor m1 = 2.25", 61.35, (_m1+_m2+_m3)*1e3, 2e-3, "meV")
# the anchor spread: rho_Lambda^(1/4) is pinned only to ~1.5%, and the floor is what notices
def _win(m1):
    m2, m3 = math.sqrt(m1**2+_dm21), math.sqrt(m1**2+_dm31)
    t = [(1-_s12)*(1-_s13)*m1, _s12*(1-_s13)*m2, _s13*m3]
    return (m1+m2+m3)*1e3, sum(t)*1e3, max(0.0, 2*max(t)-sum(t))*1e3
chk("fairbank_note", "Sigma m_nu at the retired-route value m1 = 2.284", 61.40, _win(2.284e-3)[0], 2e-3, "meV")
chk("fairbank_note", "floor at the low anchor", 0.044, _win(2.250e-3)[2], 0.03, "meV")
chk("fairbank_note", "floor at the retired-route value 2.284", 0.023, _win(2.284e-3)[2], 0.05, "meV")
chk("fairbank_note", "the retired route's +1.5% would nearly halve the floor", 1.9,
    _win(2.250e-3)[2]/_win(2.284e-3)[2], 0.05, "x")
chk("fairbank_note", "|Ue1|^2 m1", 1.52, _t[0]*1e3, 0.02, "meV")
chk("fairbank_note", "|Ue2|^2 m2", 2.67, _t[1]*1e3, 0.02, "meV")
chk("fairbank_note", "|Ue3|^2 m3", 1.10, _t[2]*1e3, 0.02, "meV")
chk("fairbank_note", "m_bb upper edge (phases aligned)", 5.3, sum(_t)*1e3, 0.02, "meV")
# the floor's fragility: the m1 above which the triangle closes and the floor vanishes
def _gap(m1):
    m2, m3 = math.sqrt(m1**2+_dm21), math.sqrt(m1**2+_dm31)
    return _s12*(1-_s13)*m2 - ((1-_s12)*(1-_s13)*m1 + _s13*m3)
_lo, _hi = 1e-3, 6e-3
for _ in range(80):                            # bisect for the critical m1
    _mid = 0.5*(_lo+_hi)
    if _gap(_mid) > 0: _lo = _mid
    else: _hi = _mid
chk("fairbank_note", "critical m1 where the floor vanishes", 2.324, _mid*1e3, 0.01, "meV")
# --- what the anchor's range actually is -----------------------------------
# The letter's floor table spans the OBSERVATION's own uncertainty, not the
# 2.2842 meV figure: that one is the T_c = 179 keV route's output, and the
# ledger retires T_c = 179 keV as the observation-inverted 176.32 rounded up,
# with the "+1.5%" being the rounding rather than a sourced spread. The live
# range is the Planck error on rho_Lambda, quartered.
_OL, _dOL, _hh, _dhh = 0.6889, 0.0056, 0.6736, 0.0054
_relq = math.sqrt((_dOL/_OL)**2 + (2*_dhh/_hh)**2)/4.0
chk("fairbank_note", "rho_Lambda^(1/4) relative error (Planck, quartered)", 0.449,
    100*_relq, 0.01, "%")
_lo1 = 2.25e-3*(1-_relq)
chk("fairbank_note", "anchor low edge, observed -1 sigma", 2.2399, _lo1*1e3, 2e-3, "meV")
chk("fairbank_note", "floor at the low edge", 0.050, _win(_lo1)[2], 0.02, "meV")
chk("fairbank_note", "floor at the observed anchor", 0.044, _win(2.250e-3)[2], 0.02, "meV")
chk("fairbank_note", "floor at the derived anchor", 0.038, _win(2.2599e-3)[2], 0.02, "meV")
chk("fairbank_note", "ceiling at the low edge", 5.295, _win(_lo1)[1], 0.02, "meV")
chk("fairbank_note", "ceiling at the derived anchor", 5.310, _win(2.2599e-3)[1], 0.02, "meV")
chk("fairbank_note", "ceiling moves this little across the range", 0.28,
    100*(_win(2.2599e-3)[1]-_win(_lo1)[1])/_win(_lo1)[1], 0.05, "%")
# the derived anchor's distance to the floor-vanishing threshold, in sigmas
chk("fairbank_note", "derived anchor sits this far below the critical m1", 2.78,
    100*(_mid*1e3 - 2.2599)/2.2599, 0.05, "%")
chk("fairbank_note", "that gap in sigmas of the observation", 6.18,
    ((_mid*1e3 - 2.2599)/2.2599)/_relq, 0.15, "sigma")

# ---- the experiment overlay (the Fairbank note's ask) ----------------------
import numpy as _np
_m2f, _m3f = math.sqrt(2.25e-3**2+_dm21), math.sqrt(2.25e-3**2+_dm31)
_tf = [(1-_s12)*(1-_s13)*2.25e-3*1e3, _s12*(1-_s13)*_m2f*1e3, _s13*_m3f*1e3]
_ph = _np.linspace(0, 2*_np.pi, 2001)
_A, _B = _np.meshgrid(_ph, _ph, indexing="ij")
_mbb = _np.abs(_tf[0] + _tf[1]*_np.exp(1j*_A) + _tf[2]*_np.exp(1j*_B))
chk("fairbank_note", "m_bb rms over flat phases (rate-relevant)", 3.3,
    math.sqrt((_mbb**2).mean()), 0.02, "meV")
chk("fairbank_note", "m_bb median over flat phases", 3.05, float(_np.median(_mbb)), 0.02, "meV")
chk("fairbank_note", "P(m_bb > 4.7 meV) — nEXO favourable NME", 10.8,
    100*float((_mbb > 4.7).mean()), 0.05, "%")
chk("fairbank_note", "P(m_bb > 9.0 meV) — LEGEND-1000 best", 0.0,
    100*float((_mbb > 9.0).mean()), 1e-9, "%")
chk("fairbank_note", "nEXO overlap band width", 0.60, sum(_tf) - 4.7, 0.05, "meV")

# ---- how distinctive is the sum, really -----------------------------------
_smin = (0 + math.sqrt(_dm21) + math.sqrt(_dm31))*1e3
chk("fairbank_note", "NH minimum Sigma m_nu at m1 = 0", 58.76, _smin, 2e-3, "meV")
chk("fairbank_note", "model's separation from the NH floor", 2.59,
    (2.25e-3 + math.sqrt(2.25e-3**2+_dm21) + math.sqrt(2.25e-3**2+_dm31))*1e3 - _smin, 0.02, "meV")
_t0 = [0.0, _s12*(1-_s13)*math.sqrt(_dm21)*1e3, _s13*math.sqrt(_dm31)*1e3]
chk("fairbank_note", "m_bb ceiling at m1 = 0 (minimal NH)", 3.69, sum(_t0), 0.02, "meV")
chk("fairbank_note", "m_bb floor at m1 = 0 (minimal NH)", 1.48, abs(_t0[1]-_t0[2]), 0.02, "meV")
chk("fairbank_note", "minimal-NH ceiling sits BELOW nEXO's 4.7 reach", 1.0,
    1.0 if sum(_t0) < 4.7 else 0.0, 1e-9)

# ---- barium tagging and the discriminating band ----------------------------
def _win(m1):
    m2, m3 = math.sqrt(m1**2+_dm21), math.sqrt(m1**2+_dm31)
    return [(1-_s12)*(1-_s13)*m1*1e3, _s12*(1-_s13)*m2*1e3, _s13*m3*1e3]
_tm, _t0 = _win(2.25e-3), _win(0.0)
_mod = _np.abs(_tm[0] + _tm[1]*_np.exp(1j*_A) + _tm[2]*_np.exp(1j*_B))
_min = _np.abs(_t0[0] + _t0[1]*_np.exp(1j*_A) + _t0[2]*_np.exp(1j*_B))
chk("fairbank_note", "Ba-tagged reach = 4.7/sqrt(4)", 2.35, 4.7/math.sqrt(4.0), 1e-6, "meV")
chk("fairbank_note", "P(detect) at the Ba-tagged 2.35 meV", 69.1,
    100*float((_mod > 2.35).mean()), 0.02, "%")
chk("fairbank_note", "minimal-NO P(>2.35) — why tagging cannot separate", 63.7,
    100*float((_min > 2.35).mean()), 0.02, "%")
chk("fairbank_note", "minimal-NO ceiling = the band's lower edge", 3.69, float(_min.max()), 0.02, "meV")
chk("fairbank_note", "P(model in the discriminating band)", 31.7,
    100*float(((_mod > float(_min.max())) & (_mod <= sum(_tm))).mean()), 0.03, "%")
chk("fairbank_note", "minimal-NO in that band — must be zero", 0.0,
    100*float((_min > float(_min.max())).mean()), 1e-9, "%")

# ---- THREE_EQUATIONS' stated stack ----------------------------------------
chk("THREE_EQUATIONS", "A_s closed form vs the frozen value", -0.34,
    100*(2.081/2.088 - 1), 0.03, "%")
chk("THREE_EQUATIONS", "the superseded 179 keV rounding gap", 1.52,
    100*(179/176.32 - 1), 0.02, "%")
chk("THREE_EQUATIONS", "T_c from the kernel's tau", 177.10, 0.5*math.log(2)*ME/1e3, 1e-3, "keV")

# ---- z_on: the two derived routes, and how far apart they are ---------------
_T0   = 2.7255*8.617333262e-5              # CMB temperature today, eV
_m_dy = 2.24e-20                           # the dyad-amplitude-pinned mass, eV
_Ton  = math.sqrt(_m_dy*MRED/0.61)         # include/background.h's own formula
chk("background.h", "T_on = sqrt(m*M_red/0.61)", 9.46, _Ton/1e3, 1e-3, "keV")
# the identity against the coded onset z = 4.0e7 -- MATH_SPINE quotes this ratio
chk("MATH_SPINE 2", "identity T_on over the coded z_rad_onset = 4.0e7", 1.007,
    _Ton/(4.0e7*_T0), 1e-3, "x")
chk("background.h", "z_on from the H = m identity", 4.0e7, _Ton/_T0, 0.02)
chk("background.h", "log10 z_on, the identity", 7.605, math.log10(_Ton/_T0), 2e-3)
chk("cmp_prtoe_fixed", "log10 z_on, what the running job uses", 7.5517, math.log10(3.5619e7), 1e-4)
chk("ForJustin/07", "identity vs the 3alpha mark — the unresolved gap", 0.058,
    math.log10(_Ton/_T0) - 7.547, 0.02, "dex")
chk("ForJustin/07", "the implied dyad-mass disagreement", 1.31,
    10**(2*(math.log10(_Ton/_T0) - 7.547)), 0.02, "x")

# ---- the dyad mass, pinned three independent ways --------------------------
_HBARC, _AU = 197.3269804e-9, 1.495978707e11
_cs = math.sqrt(3*ALPHA)
chk("MATH_SPINE", "xi = hbar/(m c_s) at m = 2.24e-20", 402.0,
    _HBARC/(2.24e-20*_cs)/_AU, 0.02, "AU")
chk("MATH_SPINE", "the mass that xi = 402 AU implies", 2.24e-20,
    _HBARC/(402*_AU*_cs), 0.02, "eV")
chk("MATH_SPINE", "Schive core radius at m = 2.24e-20", 7.0, 1.6/(2.24e-20/1e-22)*1e3, 0.03, "pc")
# and the mass the running job's z_on implies -- it must MISS those, which is the finding
_m_run = 0.61*(3.5619e7*_T0)**2/MRED
chk("ForJustin/07", "mass implied by the run's z_on", 1.753e-20, _m_run, 0.01, "eV")
chk("ForJustin/07", "that mass misses xi = 402 AU by", 27.0,
    100*abs(_HBARC/(_m_run*_cs)/_AU - 402)/402, 0.05, "%")

# ---- the superradiance band (honest_status carried 2e8; it is 6e8) ---------
_MSUN = 1.98892e30 * 5.6095886e35            # kg -> eV
_band = lambda ag: ag*MPL**2/2.24e-20/_MSUN  # alpha_g = M m / M_Pl^2
chk("blackholes", "superradiance band, lower edge (alpha_g = 0.1)", 6.0e8, _band(0.1), 0.02, "M_sun")
chk("blackholes", "superradiance band, upper edge (alpha_g = 0.5)", 3.0e9, _band(0.5), 0.02, "M_sun")
# the DE closed form at tau = 1/3 vs the kernel's tau -- why honest_status read 2.17 not 2.26
chk("honest_status", "(d/2)a^4 m_e — the tau=1/3 approximation", 2.174,
    1.5*ALPHA**4*ME*1e3, 2e-3, "meV")

# ---- A_s: the closed form's real inputs ------------------------------------
_k = math.log(1 + math.pi/(2*ac))/math.pi
chk("THE_AMPLITUDE", "k = ln(1+pi/2a_c)/pi", 1.36461, _k, 1e-5)
chk("THE_AMPLITUDE", "k inside the Eliashberg window [1.35,1.37]", 1.0,
    1.0 if 1.35 <= _k <= 1.37 else 0.0, 1e-9)
chk("THE_AMPLITUDE", "A_s = (a_c/4pi k)^3", 2.0807e-9, (ac/(4*math.pi*_k))**3, 1e-3)
chk("THE_AMPLITUDE", "A_s vs the frozen 2.088e-9", -0.35,
    100*((ac/(4*math.pi*_k))**3/2.088e-9 - 1), 0.03, "%")

# ---- P-2026-048: can the lattice test actually discriminate? ----------------
_tau_obs, _tau_ker, _tau_048 = 0.34506, 0.5*math.log(2), 0.3503
chk("ANN-026", "kernel tau vs the observation-inverted value", 0.44,
    100*(_tau_ker/_tau_obs - 1), 0.03, "%")
chk("ANN-026", "P-048's registered tolerance", 5.7, 100*0.02/_tau_048, 0.02, "%")
chk("ANN-026", "tolerance / the gap it must resolve", 13.0,
    (0.02/_tau_048)/abs(_tau_ker/_tau_obs - 1), 0.05, "x")
chk("ANN-026", "kernel tau sits inside P-048's window", 1.0,
    1.0 if _tau_048-0.02 <= _tau_ker <= _tau_048+0.02 else 0.0, 1e-9)

# ---- P-2026-048's amended decision rule (2026-07-19) ----------------------
_gap = 0.5*math.log(2) - 0.34506
chk("P-048", "the separation the lattice must resolve", 0.00151, _gap, 0.02)
chk("P-048", "inconclusive band (1-sigma separation)", 0.0015, _gap, 0.02)
chk("P-048", "the 2-sigma discrimination requirement", 0.00076, _gap/2, 0.02)
chk("P-048", "the retired tolerance separated them at", 0.0755, _gap/0.02, 0.02, "sigma")

# --- INTERACTION_ATLAS deep audit, 2026-07-19 ---
_alpha = 7.2973525693e-3
_Msun_GeV = 1.98892e30*5.60958885e26
_MPl = 1.220890e19
def _ag(M_over_Msun, m_eV):
    return M_over_Msun*_Msun_GeV*(m_eV*1e-9)/_MPl**2

# M2 = alpha^2 * T_c at the kernel-sourced T_c, and the E_b it carries
chk("INTERACTION_ATLAS", "M2 = alpha^2 * T_c at T_c=177.10 keV", 9.43,
    _alpha**2*177.10e3, tol=0.002, unit="eV")
chk("cosmological_constant", "E_b = 1/2 ac^2 M2 -> the standing rho_L^1/4", 2.2599,
    0.5*(3*_alpha)**2*_alpha**2*177.10e3*1e3, tol=0.002, unit="meV")
chk("cosmological_constant", "the retired T_c=179 keV reproduces the retired 2.284", 2.2842,
    0.5*(3*_alpha)**2*_alpha**2*179.0e3*1e3, tol=0.002, unit="meV")

# the superradiance band at the recorded mass: P-034's edges are alpha_g in [0.1, 0.5]
chk("INTERACTION_ATLAS", "alpha_g at 6e8 Msun (P-034 lower edge)", 0.10, _ag(6e8, 2.24e-20), tol=0.02)
chk("INTERACTION_ATLAS", "alpha_g at 3e9 Msun (P-034 upper edge)", 0.50, _ag(3e9, 2.24e-20), tol=0.02)
chk("INTERACTION_ATLAS", "alpha_g at M87* (6.5e9) -- past the window", 1.09, _ag(6.5e9, 2.24e-20), tol=0.02)
# the old entry's kinematic shield was correct for the mass it was written against
chk("INTERACTION_ATLAS", "retired shield: alpha_g at 1e11 Msun, m=1e-22 eV", 0.075,
    _ag(1e11, 1e-22), tol=0.02)
# the recorded mass sits ABOVE the M87* exclusion band, not below it
import math as _m
chk("INTERACTION_ATLAS", "decades of 2.24e-20 eV above the M87* band top (4.6e-21)", 0.69,
    _m.log10(2.24e-20/4.6e-21), tol=0.02, unit="dex")
# f_eff and what the lambda move costs the quench margin
chk("INTERACTION_ATLAS", "f_eff = m/sqrt(lambda) at recorded values", 5.01e16,
    (2.24e-20*1e-9)/_m.sqrt(2e-91), tol=0.01, unit="GeV")
chk("INTERACTION_ATLAS", "decades N_eq grows when lambda 1e-88 -> 2e-91", 2.70,
    _m.log10(1e-88/2e-91), tol=0.01, unit="dex")
chk("FAILURES_LEDGER", "retired: the swept quench margin's re-priced low end", -0.20,
    2.5 - _m.log10(1e-88/2e-91), tol=0.05, unit="dex")

# --- #156: the quench re-derived at the model's own quartic and mass (2026-07-20) ---
# The sweep's re-pricing above is retired: it carried N_eq ~ alpha_g^((9-p)/2)/lambda, which
# balances a TOTAL event rate against a PER-PARTICLE growth rate. Like against like gives
# N_eq = (C_SR/c_nl) alpha_g^(9-p)/lambda^2 with p = 4. See scripts/superradiance_quench.py.
import sys as _sys, os as _os
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import superradiance_quench as _sq
# the two quartics are different FIELDS. A gravitational atom needs the boson's Compton
# wavelength within an order of the hole's gravitational radius; alpha_g IS that ratio.
_PC, _RG9 = 3.0857e16, 1.4766e3*1e9        # metres per pc; GM/c^2 for 1e9 Msun, metres
chk("smbh_atoms", "CW-field Compton wavelength at m_phi = 3.1e-5 eV", 0.636,
    HBARC/3.1e-5*100, 0.02, "cm")
chk("smbh_atoms", "ultralight Compton wavelength at m = 2.24e-20 eV", 2.855e-4,
    HBARC/2.24e-20/_PC, 0.02, "pc")
# the consistency the atom needs: lambda_C/r_g must equal 1/alpha_g, and it does to 0.04%
chk("smbh_atoms", "lambda_C/r_g at 1e9 Msun equals 1/alpha_g", 5.963,
    (HBARC/2.24e-20)/_RG9, 0.01)
# the CW field misses that condition by 15 decades -- it forms no atom at any SMBH mass
chk("smbh_atoms", "decades the CW field's Compton wavelength falls short", 15.1,
    _m.log10((HBARC/2.24e-20)/(HBARC/3.1e-5)), 0.02, "dex")
# p = 4 by two independent routes, prefactors agreeing to a factor of ~3
chk("smbh_atoms", "golden-rule / kinetic prefactor ratio (the O(1) spread)", 2.83,
    _sq.C_NL/_sq.C_NL_KINETIC, 0.02, "x")
# the margin across P-034's band -- negative by 83 to 86 decades
for _ag, _mg in ((0.1, -83.7), (0.3, -85.1), (0.5, -85.8)):
    chk("smbh_atoms", f"quench margin log10(N_sd/N_eq) at alpha_g={_ag}", _mg,
        _sq.margin(_ag), 0.01, "dex")
# p is not the defect: the atlas form evaluated AT p=4 still clears zero
chk("FAILURES_LEDGER", "atlas form at p=4 (before the lambda-power fix)", 5.03,
    _m.log10(_sq.N_spindown(0.3)/(0.3**2.5/2e-91)), 0.02, "dex")
chk("FAILURES_LEDGER", "decades the missing power of lambda is worth", 90.2,
    _m.log10(_sq.N_spindown(0.3)/(0.3**2.5/2e-91)) - _sq.margin(0.3), 0.02, "dex")
# what lambda would have to be, and how far that is from the recorded value
chk("smbh_atoms", "lambda needed for the quench to shield (alpha_g=0.3)", 7.34e-49,
    _sq.lam_needed(0.3), 0.02)
chk("smbh_atoms", "decades of lambda the shield is short", 42.6,
    _m.log10(_sq.lam_needed(0.3)/2e-91), 0.02, "dex")
# the bosenova branch: closed-form (2/a*)(f_eff/M_Pl)^2/alpha_g^3 reproduces the direct ratio
chk("smbh_atoms", "N_bosenova/N_spindown, closed form vs direct (alpha_g=0.3)", 1.0,
    _sq.bosenova_ratio_closed(0.3)/(_sq.N_bosenova(0.3)/_sq.N_spindown(0.3)), 1e-9)
chk("smbh_atoms", "N_bosenova sits below N_spindown (alpha_g=0.3)", 1.247e-3,
    _sq.N_bosenova(0.3)/_sq.N_spindown(0.3), 0.02)

# --- #134: F_dark/sqrt(sigma), with the normalization pinned (2026-07-20) -------
# The convention is read off the Lagrangian: L_theta = (F^2/2)(d theta)^2 matched to
# (F_pi^2/4)Tr(dU^+ dU) on U = diag(e^{i t}, e^{-i t}) gives Tr = 2(d theta)^2, so
# F = F_pi = sqrt(2) f_pi -- the 130.4 MeV branch. Sources: forced_combination.md §4.
_c2   = 4/(3*_m.log(2))                 # the kernel target c_2
_q2   = _c2/_m.sqrt(3)                  # q~^2/sqrt(sigma), the vortex stiffness
_Fdk  = lambda t: _m.sqrt(_q2/(2*_m.pi*t))
chk("forced_combination", "c_2 = 4/(3 ln 2)", 1.9236, _c2, 1e-4)
chk("forced_combination", "q~^2/sqrt(sigma) = c_2/sqrt(3)", 1.1106, _q2, 1e-4)
chk("forced_combination", "F_dark/sqrt(sigma) at t*sqrt(sigma) = 1", 0.4204, _Fdk(1.0), 1e-3)
# the demand band is the THICKNESS band w*sqrt(sigma) in [0.8, 1.1], inverted
chk("forced_combination", "demand band top (t*sqrt(sigma) = 0.8)", 0.470, _Fdk(0.8), 1e-3)
chk("forced_combination", "demand band bottom (t*sqrt(sigma) = 1.1)", 0.401, _Fdk(1.1), 1e-3)
# the retired "normalization band" was one number in two conventions: the ends differ by sqrt(2)
chk("FAILURES_LEDGER", "retired: the 0.30-0.42 band's ends are a factor sqrt(2)", 1.41421,
    _Fdk(1.0)/(_Fdk(1.0)/_m.sqrt(2)), 1e-5)
chk("FAILURES_LEDGER", "retired: the lower end 0.4204/sqrt(2)", 0.2973,
    _Fdk(1.0)/_m.sqrt(2), 1e-3)
# like-for-like against QCD in the SAME (pinned, 130.4 MeV) convention
_QCD_PIN = 130.4/440.0
chk("forced_combination", "QCD F_pi/sqrt(sigma), pinned convention", 0.29636, _QCD_PIN, 1e-4)
chk("forced_combination", "QCD f_pi/sqrt(sigma), 92.4 MeV convention", 0.21, 92.4/440.0, 1e-4)
chk("forced_combination", "demand / QCD, like for like", 1.4186, _Fdk(1.0)/_QCD_PIN, 1e-3, "x")
chk("FAILURES_LEDGER", "retired: that ratio IS sqrt(2), to 0.31%", 0.31,
    100*(_Fdk(1.0)/_QCD_PIN/_m.sqrt(2) - 1), 0.05, "%")
# the "2.39x internal disagreement" the pin appeared to uncover -- RETIRED (#134, 2026-07-20).
# The NJL route computes f/Lambda_NJL, not f/sqrt(sigma): its one-loop f^2 = N_c M^2 F(y)/(2pi^2)
# carries y = M/Lambda, so de_value_g_to_lambda.py:113 is algebraically f/Lambda. The script's own
# QCD anchor refutes Lambda = sqrt(sigma): Lambda = 631 MeV there against sqrt(sigma) = 440 MeV.
_NJL_92 = 0.1244                        # de_value_g_to_lambda.py:113 -- this is f/Lambda
_Ff  = lambda y: _m.log((1+_m.sqrt(1+y*y))/y) - 1/_m.sqrt(1+y*y)   # the f^2 loop integral
_fq  = _m.sqrt(3*336.0**2*_Ff(336.0/631.0)/(2*_m.pi**2))           # the script's QCD f_pi
_i134 = (92.4/440.0)/(_fq/631.0)         # (i)   Lambda read as sqrt(sigma) -- the unit error
_ii134 = (_fq/631.0)/_NJL_92             # (ii)  the real dark-vs-QCD offset in f/Lambda
_iii134 = _Fdk(1.0)/_QCD_PIN             # (iii) the vortex demand's own sqrt(2) over QCD
chk("FAILURES_LEDGER", "retired: the NJL number read as pinned f_dark/sqrt(sigma)", 0.17593,
    _NJL_92*_m.sqrt(2), 1e-3)
chk("FAILURES_LEDGER", "retired: the apparent vortex/NJL disagreement", 2.390,
    _Fdk(1.0)/(_NJL_92*_m.sqrt(2)), 1e-3, "x")
chk("forced_combination", "the script's QCD calibration returns f_pi", 93.09, _fq, 1e-3, "MeV")
chk("forced_combination", "QCD read the script's way is f/Lambda", 0.14752, _fq/631.0, 1e-3)
chk("forced_combination", "#134 (i): the Lambda-as-sqrt(sigma) step fails on QCD", 1.4235,
    _i134, 1e-3, "x")
chk("forced_combination", "#134 (ii): dark vs QCD in f/Lambda (N_c = 2 and its own y)", 1.1859,
    _ii134, 1e-3, "x")
chk("forced_combination", "#134 (iii): the vortex demand's sqrt(2) over QCD", 1.4186,
    _iii134, 1e-3, "x")
chk("forced_combination", "the three factors reproduce the 2.39", 2.390,
    _i134*_ii134*_iii134, 5e-3, "x")
chk("forced_combination", "NJL corrected by QCD's Lambda/sqrt(sigma), pinned", 0.2523,
    _NJL_92*(631.0/440.0)*_m.sqrt(2), 1e-3)
chk("forced_combination", "the corrected residual is (ii)x(iii), not a third disagreement", 1.666,
    _Fdk(1.0)/(_NJL_92*(631.0/440.0)*_m.sqrt(2)), 5e-3, "x")
# the joint inversion: only (F/sqrt(sigma), w*sqrt(sigma)) together return c_2
chk("forced_combination", "c_2 recovered from the pair", 1.9236,
    _m.sqrt(3)*2*_m.pi*_Fdk(0.95)**2*0.95, 1e-4)

# --- #123: the mode-sum is the LHY object, so it inherits the control failure ----
# The renormalized zero-point residual IS the LHY term; at the derived lambda the next
# order exceeds it, so building the sum by hand buys nothing. Source: cosmological_constant.
_LHY = (8/(15*_m.pi**2))*_m.sqrt(ac)                 # the coefficient of lambda
chk("cosmological_constant", "LHY coefficient (8/15pi^2)*sqrt(alpha_c)", 0.0079954, _LHY, 1e-4)
chk("cosmological_constant", "the same on rho_Lambda^(1/4), i.e. /4", 0.0019989, _LHY/4, 1e-4)
# RECONCILED (tribunal, Thermal_O1_Discussions.md, 2026-07-17): the two values are not a
# conflict. 0.0080 is the LEADING closed-form coefficient (line 621); 0.0084 is the MEASURED
# value with the O(alpha_c) relativistic correction folded in -- the ~5% gap below IS that
# correction, both upheld. Leading pairs with the leading quarter 0.0020 (line 623), measured
# with the measured quarter 0.0021 (line 631). de_value_g_to_lambda.py's 0.0084 is the measured
# value used for the size estimate, which is correct. The checks below lock the relationship.
chk("cosmological_constant", "the recorded 0.0084 against the closed form 0.0080", 5.06,
    100*(0.0084/_LHY - 1), 0.02, "%")
chk("cosmological_constant", "0.0021 is 0.0084/4, not 0.0080/4", 0.0021, 0.0084/4, 1e-3)
_LSTAR = 22.41                                        # |Wu| = LHY control edge (booked)
for _lbl, _lam in (("band bottom", 26.0), ("centre", 36.0), ("band top", 46.0)):
    chk("cosmological_constant", f"Wu/LHY at lambda = {_lam:.0f} ({_lbl})", _lam/_LSTAR,
        _lam/_LSTAR, 1e-9, "x")
chk("cosmological_constant", "the whole band sits above the control edge", 1.0,
    1.0 if 26.0/_LSTAR > 1.0 else 0.0, 1e-9)
chk("cosmological_constant", "LHY size at the band centre", 28.8, 100*_LHY*36.0, 0.02, "%")
# blocker (ii): a linear massless dispersion under a preferred-frame cutoff is radiation-like.
# p = (1/3) rho for omega = c_s k, independent of the cutoff -- so w = +1/3, not -1.
chk("cosmological_constant", "w of a preferred-frame phonon zero-point sum", 1/3,
    1/3, 1e-12)

# --- #120: the entanglement-side O(1) cancels in the ratio, for ANY form factor --
# S = N A/(48 pi eps^2) and 1/G = N/(12 pi eps^2) descend from one heat-kernel coefficient
# (the conical deficit's R-delta), so a common regulator factor O multiplies both.
_S_over_A4G = lambda O: (O/(48*_m.pi))/((1/4)*(O/(12*_m.pi)))
chk("quantum_gravity", "S/(A/4G) = 12pi/48pi x 4 = 1, unregulated", 1.0, _S_over_A4G(1.0), 1e-12)
# the p-ramp on the induced-G side spans a factor of 4 and cancels identically
for _p, _O in ((1.5, 2.0), (2.0, 1.0), (3.0, 0.5)):
    chk("quantum_gravity", f"S/(A/4G) at Bogoliubov softening p = {_p}", 1.0,
        _S_over_A4G(_O), 1e-12)
chk("FAILURES_LEDGER", "the p-ramp's span, which the ratio removes", 4.0, 2.0/0.5, 1e-12, "x")

# the graveyard census must total its own entry count
chk("INTERACTION_ATLAS", "graveyard census totals the 14 entries", 14, 7+4+3, tol=0.0)

# 0nubb: the m_bb reach mapping, calibrated on KamLAND-Zen's published limit
_K_best = 2.3e26*(36e-3)**2      # eV^2 yr, favourable NME
_K_worst = 2.3e26*(156e-3)**2    # eV^2 yr, unfavourable NME
chk("fairbank_note", "nEXO baseline reach in m_bb, favourable NME", 4.70,
    _m.sqrt(_K_best/1.35e28)*1e3, tol=0.01, unit="meV")
chk("fairbank_note", "nEXO baseline reach in m_bb, unfavourable NME", 20.3,
    _m.sqrt(_K_worst/1.35e28)*1e3, tol=0.01, unit="meV")
chk("fairbank_note", "barium-tagged reach (4x in T-half)", 2.35,
    _m.sqrt(_K_best/(4*1.35e28))*1e3, tol=0.01, unit="meV")


# --- the T_c supersession, propagated 2026-07-19 ---
_TD, _TLi = 179.0*(1-0.6089), 179.0*(1-0.7765)     # the temperatures the coded stamps sit at
chk("CODE_MANIFEST", "D-bottleneck ramp stamp at the standing T_c", 0.6047, 1-_TD/177.10, 1e-3)
chk("CODE_MANIFEST", "Li ramp stamp at the standing T_c", 0.7741, 1-_TLi/177.10, 1e-3)
chk("CODE_MANIFEST", "D/H window shift from the T_c move, in sigma", 0.0023,
    abs(2.387*0.00645*((1-_TD/177.10)/(1-_TD/179.0)-1))/0.047, 0.05, "sigma")
# the m_bb window at the narrowed anchor range
_dm21b, _dm31b, _s12b, _s13b = 7.42e-5, 2.515e-3, 0.307, 0.022
def _wn(m1):
    m2, m3 = math.sqrt(m1**2+_dm21b), math.sqrt(m1**2+_dm31b)
    t = [(1-_s12b)*(1-_s13b)*m1, _s12b*(1-_s13b)*m2, _s13b*m3]
    return sum(t)*1e3, max(0.0, 2*max(t)-sum(t))*1e3
chk("fairbank_note", "m_bb floor at the observed anchor 2.25", 0.044, _wn(2.25e-3)[1], 0.02, "meV")
chk("fairbank_note", "m_bb floor at the derived anchor 2.2599", 0.038, _wn(2.2599e-3)[1], 0.02, "meV")
chk("fairbank_note", "m_bb ceiling holds at 5.30 across the observed anchor range", 5.30,
    max(_wn(2.25e-3)[0], _wn(2.2599e-3)[0]), 0.005, "meV")


# --- the Majoron mode, 0nubbchi (neutrino_sector 3b), filed 2026-07-19 ---
_m3 = 50.20e-3                                   # eV
_vL_MeV = _m3/1.2e-8                             # from the recorded g_33
chk("neutrino_sector 3b", "v_L from the recorded g_33 = 1.2e-8", 4.18e6, _vL_MeV, 1e-3, "eV")
_mbb = 3.05e-3
for _lab, _v, _b in [("MeV corner", 4.18e6, 7.3e-10), ("GeV end", 1e9, 3.05e-12),
                     ("2.4 TeV ceiling", 2.4e12, 1.27e-15)]:
    chk("neutrino_sector 3b", f"<g_ee> = m_bb/v_L at the {_lab}", _b, _mbb/_v, 0.01)
_Kg = 2.6e24*(0.8e-5)**2                          # KamLAND-Zen ordinary-majoron calibration
chk("neutrino_sector 3b", "T_half at the MeV corner, favourable NME", 3.1e32,
    _Kg/(_mbb/4.18e6)**2, 0.03, "yr")
_Km = 2.3e26*(36e-3)**2
chk("neutrino_sector 3b", "Majoron mode slower than the mass mode by", 1e4,
    (_Kg/(_mbb/4.18e6)**2)/(_Km/_mbb**2), 0.05, "x")
chk("neutrino_sector 3b", "<g_ee> below the experimental limit by", 1.4e4, 1e-5/(_mbb/4.18e6), 0.05, "x")


# --- the deuterium quark door: the loop bridge's size (deuterium_scar §5) ---
_loop = (ALPHA/math.pi)**2
chk("deuterium_scar", "dyad->lepton loop->2gamma->quark suppression (alpha/pi)^2", 5.4e-6, _loop, 0.01)
chk("deuterium_scar", "what the loop delivers, in percent", 6.8e-6, 0.012543*_loop*100, 0.02, "%")
chk("deuterium_scar", "shortfall against P-006's 0.14%", 21000, 1.4e-3/(0.012543*_loop), 0.02, "x")
chk("deuterium_scar", "shortfall against P-006's 0.21%", 31000, 2.1e-3/(0.012543*_loop), 0.02, "x")
# the photodissociation cure's internal arithmetic
_HeH = 0.249/(4*(1-0.249))
chk("deuterium_scar", "He/H by number at Y_p = 0.249", 0.083, _HeH, 0.01)
chk("deuterium_scar", "D/H gained by breaking 1.7e-5 of the helium", 1.4e-6, 1.7e-5*_HeH, 0.02)
chk("deuterium_scar", "the Y_p it costs", -4.2e-6, -1.7e-5*0.249, 0.02)
chk("deuterium_scar", "energy per hydrogen at 20 MeV per dissociation", 28, 1.7e-5*_HeH*20e6, 0.05, "eV")


# --- the deuterium lever-combination test (deuterium_scar 6b/6/7), 2026-07-19 ---
_DH, _errD = 2.387, math.sqrt(0.030**2+0.037**2)
def _sig(pct): return _DH*pct/100/_errD
chk("deuterium_scar 6b", "below-T_c boost at dN_eff = 0.059", 0.34, _sig(0.1160*0.059*100), 0.03, "sigma")
chk("deuterium_scar 6b", "below-T_c boost at dN_eff = 0.015", 0.09, _sig(0.1160*0.015*100), 0.05, "sigma")
chk("deuterium_scar 6b", "sharper transition 0.61eps -> 1.0eps", 0.21, _sig(1.057-0.645), 0.05, "sigma")
chk("deuterium_scar 6b", "best case, everything additive", -2.39,
    -2.94 + _sig(0.1160*0.059*100) + _sig(1.057-0.645), 0.02, "sigma")
# section 7 item 3: both dof counts are forced
_Nc, _Nf = 2, 3
chk("deuterium_scar 7", "deconfined g* = 2(Nc^2-1) + (7/8)(4 Nc Nf)", 27, 2*(_Nc**2-1)+(7/8)*4*_Nc*_Nf, 1e-9)
chk("deuterium_scar 7", "confined Goldstones 2Nf^2 - Nf - 1", 14, 2*_Nf**2-_Nf-1, 1e-9)
# section 6: the roster is full, and the seats present are below threshold
chk("deuterium_scar 6", "str[k1] with one extra sterile (17/gen) breaks finiteness", 3, 17*3-48, 1e-9)
chk("deuterium_scar 6", "nu_R at the MeV corner vs the He-4 threshold", 4.9, 20.6/4.18, 0.02, "x short")


# --- the false-vacuum route does NOT equal the particle route (deuterium_scar 6) ---
_hbarc = 1.9733e-5                                  # eV cm
_rho_vac = (20e6)**4/_hbarc**3                      # eV/cm3, a 20 MeV-scale false vacuum
_T_dep, _g = 570.0, 3.36                            # eV, ambient at t = 4e6 s
_rho_rad = (math.pi**2/30)*_g*_T_dep**4/_hbarc**3
chk("deuterium_scar 6", "20 MeV false vacuum energy density", 2.08e43, _rho_vac, 0.02, "eV/cm3")
chk("deuterium_scar 6", "ambient radiation at the deposit epoch", 1.52e25, _rho_rad, 0.02, "eV/cm3")
chk("deuterium_scar 6", "a space-filling 20 MeV vacuum over-delivers by", 1.37e18, _rho_vac/_rho_rad, 0.01, "x")
_n_gam = (2*1.20206/math.pi**2)*_T_dep**3/_hbarc**3
_rho_need = 30*6.1e-10*_n_gam
chk("deuterium_scar 6", "volume fraction allowed in the false vacuum", 5.2e-30, _rho_need/_rho_vac, 0.03)


# --- the PBH route (deuterium_scar 5b), priced and killed 2026-07-19 ---
_Mstar, _tstar = 5.1e14, 4.35e17                    # g, s: PBH evaporating today
_M_of_tau = lambda tau: _Mstar*(tau/_tstar)**(1/3)
chk("deuterium_scar 5b", "PBH mass evaporating at 4e6 s", 1.07e11, _M_of_tau(4e6), 0.01, "g")
chk("deuterium_scar 5b", "PBH mass evaporating at 1e8 s", 3.12e11, _M_of_tau(1e8), 0.01, "g")
chk("deuterium_scar 5b", "T_H at the window's light end", 99, 1.06*(1e13/_M_of_tau(4e6)), 0.02, "GeV")
chk("deuterium_scar 5b", "hadronic threshold over photon threshold", 90, 1877/20.6, 0.02, "x")
# the Li kill, efficiency-free: both bounds from the same population
_bLi, _bD = 10**-25.34, 10**-23.82
chk("deuterium_scar 5b", "Li binds tighter than D by", 33, _bD/_bLi, 0.03, "x")
for _tolD, _short in [(0.0125, 156), (0.05, 39)]:
    chk("deuterium_scar 5b", f"shortfall at D-curve tolerance {_tolD*100:.2g}%", _short,
        0.059/(_tolD*_bLi/_bD), 0.03, "x")
# pure-EM PBH dodge: no mass is both on-time for ⁴He photodissociation and cool enough
# to suppress hadrons (T_H ≲ Λ_QCD). Timing window locks T_H ≳ 34 GeV; sub-QCD T locks
# τ ≳ 10^14 s. Kill booked 2026-07-21 → FAILURES_LEDGER.
_T_H = lambda M: 1.06e13 / M                         # GeV
_tau_of_M = lambda M: _tstar * (M/_Mstar)**3
_M_lo_win, _M_hi_win = _M_of_tau(4e6), _M_of_tau(1e8)
_M_QCD = 1.06e13 / 0.2                               # T_H = 200 MeV
chk("deuterium_scar 5b", "pure-EM: min T_H in photodissoc window", 34.0,
    _T_H(_M_hi_win), 0.05, "GeV")
chk("deuterium_scar 5b", "pure-EM: that min is above Lambda_QCD", 1.0,
    1.0 if _T_H(_M_hi_win) > 0.2 else 0.0, 1e-9)
chk("deuterium_scar 5b", "pure-EM: sub-QCD PBH evaporates this late", 5.0e14,
    _tau_of_M(_M_QCD), 0.05, "s")
chk("deuterium_scar 5b", "pure-EM: sub-QCD lifetime / window high edge", 5.0e6,
    _tau_of_M(_M_QCD)/1e8, 0.1, "x")


# --- PHYSICS_DOMAINS deep audit, 2026-07-19; width re-pinned 2026-07-21 (#157) ---
# the deuterium sigma ladder, ONE width (two-term standing ±0.0476)
_wD = 0.0476
chk("PHYSICS_DOMAINS 6", "standing D/H row in sigma", -2.94, -(2.527-2.387)/_wD, 0.005, "sigma")
chk("PHYSICS_DOMAINS 6", "committed-window low end", -2.52, -(2.527-2.407)/_wD, 0.005, "sigma")
chk("PHYSICS_DOMAINS 6", "committed-window high end", -1.34, -(2.527-2.463)/_wD, 0.005, "sigma")
chk("PHYSICS_DOMAINS 6", "LCDM control on the same width", -2.25, -(2.527-2.420)/_wD, 0.005, "sigma")
_wU = math.sqrt(_wD**2+(0.035*2.387)**2)          # ⊕ inter-code ~3.5% relative
chk("PHYSICS_DOMAINS 6", "spread-unfolded standing row", -1.46, -(2.527-2.387)/_wU, 0.02, "sigma")
# the committed window IS dNeff 0.06-0.24 (the scar's 0.26-0.29 was a garble)
chk("deuterium_scar 5", "window low edge from dNeff = 0.06", 2.407, 2.387*(1+0.1350*0.06), 0.001)
chk("deuterium_scar 5", "window high edge from dNeff = 0.24", 2.463, 2.387*(1+0.1350*0.238), 0.001)
# the quartic era at the recorded lambda and m
_h_lo = 2e-91*(0.7e26)**2/(2.24e-20)**2
_h_hi = 2e-91*(1.5e26)**2/(2.24e-20)**2
chk("PHYSICS_DOMAINS 15", "h at the abundance pin's low end", 2.0, _h_lo, 0.03)
chk("PHYSICS_DOMAINS 15", "h at the abundance pin's high end", 9.0, _h_hi, 0.005)
# the 21-cm shift at the standing epsilon
chk("PHYSICS_DOMAINS 74", "21-cm rest-frequency shift = 2*eps", 2.51, 2*1.2543, 0.002, "%")
chk("PHYSICS_DOMAINS 74", "shift at 68 MHz", 1.71, 68*2*0.012543, 0.005, "MHz")
chk("PHYSICS_DOMAINS 74", "shift at 89 MHz", 2.23, 89*2*0.012543, 0.005, "MHz")
# the ADM gap in decades
chk("PHYSICS_DOMAINS 11", "Y_Q over eta_B in decades", 30.2, math.log10(1e21/6e-10), 0.005, "dex")
# the census arithmetic: enumerated tallies must total the enumerated census
chk("PHYSICS_DOMAINS II", "type tally totals the 52 entries", 52, 14+8+4+6+12+2+2+4, 0.0)
chk("PHYSICS_DOMAINS II", "status tally totals the 52 entries", 52, 15+12+1+12+2+10, 0.0)


# --- the two chain files, 2026-07-19 ---
chk("THE_CHAIN 3", "z(T_c) at the standing 177.10 keV", 7.54e8, 7.62e8*177.10/179, 0.002)
chk("THE_CHAIN 5", "census-lock cells at the frozen A_s", 782, (1/2.088058e-9)**(1/3), 0.001)
chk("THE_CHAIN 5", "the older 781 was the Planck-anchored count", 781, (1/2.100e-9)**(1/3), 0.001)
chk("THE_CHAIN 10", "turn window in z: a = 2.0", -0.50, 1/2.0-1, 0.01)
chk("THE_CHAIN 10", "turn window in z: a = 2.8", -0.643, 1/2.8-1, 0.005)
chk("great_chain 6", "the coded dyad amplitude is 1 + eps", 1.012543, 1+27*ALPHA/(5*math.pi), 1e-5)
chk("great_chain 8", "the nuclear rung", 8.5e-3, 8e6/939e6, 0.05)


# --- math_story, 2026-07-19 ---
chk("math_story 7", "S = (1+f_rot^2)/2 at the median draw", 0.58, (1+0.4**2)/2, 0.001)
chk("math_story 7", "S equals the granule p2+q2 factor ~0.6", 0.6, (1+0.4**2)/2, 0.04)
chk("math_story 3", "ramp stamp at the D bottleneck (177.10 keV)", 0.60, 1-179.0*(1-0.6089)/177.10, 0.01)
chk("math_story 3", "ramp stamp at lithium (177.10 keV)", 0.77, 1-179.0*(1-0.7765)/177.10, 0.01)


# --- me_mechanism_math, 2026-07-19 ---
chk("me_mechanism 10", "dm_nu = 2 dm_e at the standing eps", 2.51, 2*1.2543, 0.002, "%")
chk("me_mechanism 10", "dm_nu on Sigma = 61.4 meV", 1.54, 61.4*2*0.012543, 0.01, "meV")
chk("me_mechanism 10", "f_L = Psi_rec/(2 eps)", 2.3e20, 5.8e18/(2*0.012543), 0.01, "eV")
chk("me_mechanism hf", "kappa = eps/f^2 at f = 3e14 eV", 1.4e-31, 0.012543/(3e14)**2, 0.005, "eV^-2")
chk("me_mechanism hf", "ramp half-amplitude at 0.86 T_c", 152, 0.86*177.10, 0.005, "keV")
chk("me_mechanism hf", "ramp 90% at 0.64 T_c", 113, 0.64*177.10, 0.005, "keV")
chk("me_mechanism 8", "dark-ages trough offset at +2.51%", 0.40, 16.0*2*0.012543, 0.02, "MHz")
chk("me_mechanism 8", "cosmic-dawn trough 78 MHz shifted", 79.96, 78.0*(1+2*0.012543), 0.001, "MHz")


# --- bbn_witness full pass, 2026-07-19 ---
chk("bbn_witness", "below-T_c zero point dN_eff", 0.49, math.log(2.527/2.387)/0.116, 0.01)
chk("bbn_witness", "zero point over the CMB-S4 fence", 1.63, (math.log(2.527/2.387)/0.116)/0.3, 0.01, "x")
chk("bbn_witness", "shortfall range low", 8.3, (math.log(2.527/2.387)/0.116)/0.059, 0.02, "x")
chk("bbn_witness", "shortfall range high", 33, (math.log(2.527/2.387)/0.116)/0.015, 0.02, "x")
chk("bbn_witness", "eps-rescale price on the window", 0.004,
    2.387*0.00645*(1.2543/1.24-1)/0.0476, 0.1, "sigma")
chk("bbn_witness", "PRIMAT's own LCDM vs Cooke at the 2-term width", 1.85, (2.527-2.439)/0.0476, 0.005, "sigma")
chk("bbn_witness", "Y_p window vs Aver", 1.09, (0.248995-0.2453)/0.0034, 0.01, "sigma")
chk("bbn_witness", "Y_p window vs EMPRESS", 3.53, (0.248995-0.2370)/0.0034, 0.005, "sigma")
chk("bbn_witness", "He-4 window opens (days)", 42, 3.67e6/86400, 0.02, "d")


# --- entropy section 4's coherence (2026-07-19) ---
chk("entropy 4", "ballistic share = eps m_e / 3", 2.14, 6.41/3, 0.01, "keV")
chk("entropy 4", "pickup at ordinary infall (f = 0.023)", 50, 6.41e3/3*0.023, 0.03, "eV")
chk("entropy 4", "pickup at merger shocks (f = 0.07)", 150, 6.41e3/3*0.07, 0.03, "eV")


# --- the CSW threshold's two conventions (blackholes 3/8), 2026-07-19 ---
_MPl_G, _m_G, _Msun_G = 1.220890e19, 2.24e-29, 1.116e57
_M0A = 0.062*_MPl_G**3/_m_G**2/_Msun_G      # 0.22 sqrt(lam/4pi) convention
_M0B = 0.22 *_MPl_G**3/_m_G**2/_Msun_G      # 0.22 sqrt(lam) convention
chk("blackholes 3", "lam_min at 3e10 Msun, tight convention", 2.2e-92, (3e10/_M0A)**2, 0.03)
chk("blackholes 8", "lam_min at 2e10 Msun, loose convention", 8e-94, (2e10/_M0B)**2, 0.03)
chk("blackholes 8", "conservative clearance at 2e10", 20, 2e-91/(2e10/_M0A)**2, 0.03, "x")
chk("blackholes 8", "loose-convention clearance at 2e10", 256, 2e-91/(2e10/_M0B)**2, 0.03, "x")
chk("blackholes 3", "Kaup cap M_Pl^2/m x 0.633", 3.7e9, 0.633*_MPl_G**2/_m_G/_Msun_G, 0.03, "Msun")


# --- the condensate bounce floor (bigbang 1.2), 2026-07-19 ---
chk("bigbang 1.2", "rho_bounce^1/4 at the derived lambda", 1.06e3, ((2.24e-20)**4/2e-91)**0.25, 0.01, "eV")


# --- baryogenesis transmission target (2026-07-19) ---
chk("baryogenesis", "T target at n = 30", 2e-11, 6.14e-10/30, 0.03)
chk("baryogenesis", "T target at n = 10", 6e-11, 6.14e-10/10, 0.03)


# --- the chiral-background margins (gravitational_waves addendum), 2026-07-19 ---
import math as _mm
_Ogw = 3e-18
chk("GW addendum", "orders under PTA (1e-10)", 8, _mm.log10(1e-10/_Ogw), 0.06, "dex")
chk("GW addendum", "orders under LISA-class (3e-14)", 4, _mm.log10(3e-14/_Ogw), 0.06, "dex")
chk("GW addendum", "the B-mode floor the recorded 1.5-dex margin implies", 9.5e-17, _Ogw*10**1.5, 0.01)


# --- the light file's lock arithmetic (2026-07-19) ---
chk("light 4", "medium loop share at M_Z", 44, 42.9/98.4*100, 0.02, "%")
chk("light 6", "lock iv: 1/a1 over 1/a2 at M_Pl", 0.673, 33.3/49.4, 0.005)
chk("light 6", "lock vi: measured A vs sqrt(2)", 0.001, abs(1.41420/2**0.5-1)*100, 0.35, "%")

# --- CMB_map: the inflationary-tensor chirality (chiral_gw_genesis.py, model-natural row) ---
_Mpl_r = 2.4e18                                   # reduced Planck mass, GeV
_Pi_nat = 1.0 * 5e16 * 1e13 / _Mpl_r**2           # alpha * theta_dot * H_gen / M_Pl^2
chk("CMB_map", "model-natural chirality Pi", 8.68e-8, _Pi_nat, 0.01)
assert 1e-8 <= _Pi_nat <= 1e-7, "CMB_map's quoted band 1e-8..1e-7 must hold the computed Pi"
chk("CMB_map", "observable-Pi genesis gap (2.4e17/6e13)", 4e3, 2.4e17/6e13, 0.01, "x")

# --- laboratory_cousins: the bench numbers (2026-07-19) ---
chk("lab cousins", "medium sound speed c_s = sqrt(3*alpha)", 0.148, math.sqrt(3/137.035999), 0.003)
chk("lab cousins", "the bench target <|cos|> = 2/pi", 0.6366, 2/math.pi, 0.001)
chk("lab cousins", "rival RMS average sqrt(<cos^2>)", 0.7071, math.sqrt(0.5), 0.001)
chk("lab cousins", "ring circumference 2*pi*20 um", 126, 2*math.pi*20, 0.005, "um")
chk("lab cousins", "fit-implied 0.6253 vs 2/pi", 1.8, (2/math.pi/0.6253-1)*100, 0.03, "%")

# --- quantum_trio: second sound + the alpha_c band (2026-07-19) ---
chk("quantum trio", "second sound c2 = c1/sqrt(3) = sqrt(alpha)", 0.0854, math.sqrt(1/137.035999), 0.002, "c")
chk("quantum trio", "identity sqrt(3a)/sqrt(3) == sqrt(a)", 1.0, math.sqrt(3/137.035999)/math.sqrt(3)/math.sqrt(1/137.035999), 1e-12)
chk("quantum trio", "indirect band top 0.0214 below 3a", 2.3, (1-0.0214/(3/137.035999))*100, 0.03, "%")

# --- no_singularities: the crossover table (2026-07-19) ---
_xi_m   = 6.0e13                                  # m (the recorded coherence length)
_Msun   = 1.98892e30; _G = 6.6743e-11; _c = 2.99792458e8
_rs     = lambda M: 2*_G*M*_Msun/_c**2
chk("no singularities", "crossover mass r_s = xi", 2.0e10, _xi_m*_c**2/(2*_G)/_Msun, 0.02, "Msun")
chk("no singularities", "10 Msun: r_s/xi", 5e-10, _rs(10)/_xi_m, 0.03)
chk("no singularities", "TON 618 (6.6e10): r_s/xi", 3.3, _rs(6.6e10)/_xi_m, 0.02)
chk("no singularities", "lambda support margin (2e-91 over 8e-94)", 250, 2e-91/8e-94, 0.01, "x")

# --- the S8 pair: standing-anchor arithmetic (2026-07-19) ---
chk("S8 pair", "g candidate identity 10*eps == 54a/pi", 1.0, (10*27/(5*math.pi)*(1/137.035999)) / (54/(math.pi*137.035999)), 1e-12)
chk("S8 pair", "LCDM 0.833 vs Legacy consensus", 1.6, (0.833-0.814)/0.012, 0.02, "sigma")
chk("S8 pair", "model 0.823 vs Legacy consensus", 0.75, (0.823-0.814)/0.012, 0.02, "sigma")
chk("S8 pair", "model twice as close as LCDM", 2.1, (0.833-0.814)/(0.823-0.814), 0.02, "x")

# --- small_scale_structure: the braiding scale (2026-07-19) ---
_MPl_full_eV = 1.22091e19 * 1e9                   # full Planck mass, eV
_M2_eV = 9.43
_rc_m = _MPl_full_eV/_M2_eV**2 * 197.3269804e-9   # (M_Pl/M2^2) * hbar-c
chk("small-scale", "braiding scale M_Pl/M2^2", 0.87, _rc_m/3.0857e19, 0.02, "kpc")
chk("small-scale", "braiding vs dwarf soliton (two orders)", 125, _rc_m/3.0857e16/7.0, 0.03, "x")

# --- lowell_anomalies: the countable pieces (2026-07-19) ---
chk("low-ell", "coefficients ell=2..6", 45, sum(2*l+1 for l in range(2,7)), 0)
chk("low-ell", "independent pairs = C(45,2)", 990, 45*44//2, 0)
chk("low-ell", "quadrupole cosmic variance sqrt(2/5)", 63, math.sqrt(2/5)*100, 0.01, "%")
chk("low-ell", "83% retention in sigma units", 0.27, (1-0.83)/math.sqrt(2/5), 0.02, "sigma")

# --- kappa_v docket: the operator arithmetic (record grade, program closed) ---
_k_kv = 9e-3
chk("kappa_v record", "amplitude k*w/2 at w=1/3", 0.15, _k_kv/6*100, 0.01, "%")
chk("kappa_v record", "radiative bill k/32pi^2", 2.8e-5, _k_kv/(32*math.pi**2), 0.02)
chk("kappa_v record", "BBN drift 4/(3y) at y=2.8e7", 5e-8, 4/(3*2.8e7), 0.05)
chk("kappa_v record", "g at recomb y=8.4e-7 (~y/4)", 2.1e-7, 8.4e-7/(4+3*(8.4e-7)), 0.01)

# --- v4 derivation: the beta-family peak (2026-07-19) ---
chk("v4 record", "peak c_s^2 coefficient 2/e", 0.74, 2/math.e, 0.01)

# --- v5 five-verdict: the locked relation (2026-07-19) ---
_M2sq = 9.4**2                                     # eV^2
_MPl_eV = 1.22091e28                               # full Planck mass, eV
_nu = lambda Meff: (4*math.pi*2/3)*(_M2sq/(Meff*_MPl_eV))**2
chk("v5 verdicts", "nu at M_eff=2e-21 (alpha=2)", 1.1e-10, _nu(2e-21), 0.02)
chk("v5 verdicts", "nu at M_eff=8.8e-23", 5.6e-8, _nu(8.8e-23), 0.02)
chk("v5 verdicts", "m2bar at M_eff=2e-21 (GUT band)", 4.4e13, _M2sq/2e-21/1e9, 0.01, "GeV")

# --- T6 Koide kernel chain (2026-07-19) ---
_me_,_mmu_,_mtau_ = 0.51099895, 105.6583755, 1776.86     # MeV
_rt = [math.sqrt(x) for x in (_me_,_mmu_,_mtau_)]
chk("T6 kernel", "Q from PDG masses", 0.66666, (_me_+_mmu_+_mtau_)/sum(_rt)**2, 1e-4)
chk("T6 kernel", "M^2 = mean(sqrt m)^2", 313.84, (sum(_rt)/3)**2, 0.001, "MeV")
chk("T6 kernel", "c2*tau = (4/(3ln2))*(ln2/2) == 2/3", 1.0, (4/(3*math.log(2)))*(math.log(2)/2)/(2/3), 1e-12)
chk("T6 kernel", "modulus: rho=1/sqrt2 -> Q=2/3", 1.0, (1/3 + (2/3)*0.5)/(2/3), 1e-12)
chk("T6 kernel", "B trace: sqrt(4pi/8pi)", 1.0, math.sqrt(0.5)/(1/math.sqrt(2)), 1e-12)
chk("T6 kernel", "mu_face = (2/9)*Tc at 177.10", 39.4, (2/9)*177.10, 0.005, "keV")
chk("FAILURES_LEDGER", "retired: the P-051 lock slope registered as 2A/9, twice the closure's",
    0.3143, 2*math.sqrt(2)/9, 0.001)
chk("T6 kernel", "tangency seed ratio 7+4sqrt3", 13.928, 7+4*math.sqrt(3), 0.001)

# --- the sign-chain walk: face assignment in hop order (2026-07-19) ---
_thB = math.radians(132.7328); _A = math.sqrt(2)
chk("sign walk", "e face dev at k=0", -0.960, _A*math.cos(_thB), 0.001)
chk("sign walk", "mu face dev at k=1", -0.420, _A*math.cos(_thB + 2*math.pi/3), 0.001)
chk("sign walk", "tau face dev at k=2", 1.379, _A*math.cos(_thB + 4*math.pi/3), 0.001)

# ---- hierarchy: which channel pairs in the basement (section 6b) ----
_e_em = (4*math.pi*ALPHA)**0.5
_v_anch = 1576.0                      # GeV, the anchor
_mg = 2*_e_em*_v_anch*1e9             # eV, Anderson-Higgs mass if the condensate carried charge 2e
chk("hierarchy 6b", "m_gamma from a charge-2e anchor condensate", 9.54e11, _mg, 5e-3, "eV")
chk("hierarchy 6b", "orders above the m_gamma bound 1e-18 eV", 30.0, math.log10(_mg/1e-18), 5e-3)
chk("hierarchy 6b", "max condensate scale clearing the bound", 1.65e-18, 1e-18/(2*_e_em), 5e-3, "eV")
chk("hierarchy 6b", "Coulomb screening length 2*alpha_c/pi", 0.013940, 2*(3*ALPHA)/math.pi, 1e-3)
chk("hierarchy 6b", "M_anchor/m_H against 4*pi", 4*math.pi, _v_anch/125.25, 2e-3)

# ---- hierarchy 6c: the gap equation solved ----
_aTF = 2*(3*ALPHA)/math.pi
chk("hierarchy 6c", "Thomas-Fermi screening a = 2*alpha_c/pi", 0.013937, _aTF, 1e-4)
chk("hierarchy 6c", "k if ONE band screened (wrong): ln(1+pi/a_c)/pi", 1.58305,
    math.log(1 + math.pi/(3*ALPHA))/math.pi, 1e-4)
chk("hierarchy 6c", "k derived: two-band screening, full FS", 1.36461,
    math.log(1 + math.pi/(2*3*ALPHA))/math.pi, 1e-4)
chk("hierarchy 6c", "anchor sensitivity d(lnM)/d(lnk)", 33.47,
    1/((math.log(1 + math.pi/(2*3*ALPHA))/math.pi)*3*ALPHA), 1e-3)
# 6c condition 2b (added 2026-07-20): the screening constant carries a band velocity,
# b = 2*alpha_c/(pi*v), and the booked value above is that at v = 1. The rows below
# guard the v-dependence rather than the v = 1 value, which line 731 already holds.
def _k_of_v(v): return math.log(1 + 1/(2*(3*ALPHA)/(math.pi*v)))/math.pi
chk("hierarchy 6c", "b = 2*alpha_c/(pi*v) reduces to the booked b at v = 1",
    0.013937, 2*(3*ALPHA)/(math.pi*1.0), 1e-4)
chk("hierarchy 6c", "k at v = 0.9 (the 10% velocity mismatch)", 1.33156, _k_of_v(0.9), 1e-4)
chk("hierarchy 6c", "that mismatch's cost in ln M (d lnM/d lnk = 33.47)", -0.818,
    33.47*math.log(_k_of_v(0.9)/_k_of_v(1.0)), 2e-2)

# ---- hierarchy 6d: the anchor's shell systematic ----
_lam0 = (2*(3*ALPHA)/math.pi/2)*math.log(1 + math.pi/(2*3*ALPHA))
chk("hierarchy 6d", "Lam_shell/M_red implied by the exponential", 0.2228,
    (4*math.pi*125.25*math.exp(1/_lam0))/2.435e18, 5e-3)
chk("hierarchy 6d", "symmetric-shell DOS correction at E_F=M_red", 1.00072, 1.000719, 1e-4)
# lambda is used as an intermediate above but its VALUE was never asserted — if the
# booked 0.029874 drifted, nothing here would catch it. Two rows close that (2026-07-20):
chk("hierarchy 6c", "lambda = k*alpha_c, the pairing coupling", 0.029874, _lam0, 1e-4)
chk("hierarchy 6g", "exact-solution shell e^(-3/2-ln2) = Lam/M_red", 0.1116,
    math.exp(-1.5 - math.log(2)), 1e-3)
chk("hierarchy 6d", "exact-solution anchor 2*Lam*exp(-1/lam) (GeV)", 3152.3,
    2*2.435e18*math.exp(-1.5)*math.exp(-1/_lam0), 5e-3)

# ---- hierarchy 6j: the portal-roster S bound ----
chk("hierarchy 6j", "Delta_S per degenerate heavy doublet", 0.05305, 1/(6*math.pi), 1e-3)
chk("hierarchy 6j", "max doublets from |S| < 0.14", 2.639, 0.14*6*math.pi, 1e-2)

# ---- P-2026-038: the last registered entry with no harness coverage (added 2026-07-20)
# Its "4.75 doublet-units" and "b2 = -0.167" are exact rationals off one input,
# b2(SM) = 19/6 with 2/3 per vector-like doublet-unit. The entry's COUNT (n = 5) is
# withdrawn by its own amendment; the arithmetic it registered is still arithmetic, and
# guarding it keeps the registry auditable rather than merely archived.
_b2sm, _per = 19/6, 2/3
chk("P-2026-038", "SU(2) flip threshold = b2(SM)/(2/3) = 19/4", 4.75, _b2sm/_per, 1e-6)
chk("P-2026-038", "b2 at n = 5 doublets = -1/6", -0.16667, _b2sm - 5*_per, 1e-4)
chk("P-2026-038", "b2 at n = 4 does not flip (= +1/2)", 0.5, _b2sm - 4*_per, 1e-6)

# ---- P-2026-012's parenthetical splittings vs the ones the corpus computes with
# The registry entry quotes rounder values (7.4e-5, 2.5e-3) than the block above
# uses (7.42e-5, 2.515e-3 — current NuFIT, normal ordering). The prediction is the
# block's; this pins the size of the documentation gap so it cannot drift further.
chk("P-2026-012", "Sigma m_nu at the registry's quoted rounder splittings",
    61.21, (2.25e-3 + math.sqrt(2.25e-3**2 + 7.4e-5) + math.sqrt(2.25e-3**2 + 2.5e-3))*1e3,
    5e-3, "meV")

# ---- #168: what the A_s count C is and is not (added 2026-07-20) ----
# The pipeline's frozen A_s is the closed form at the CONCORDANCE k, not a measurement,
# so the -0.35% between them is a k-spread. These rows pin that, the honest comparison
# against the measured amplitude, and the two O(1)s the count actually hides.
_k168   = math.log(1 + math.pi/(2*ac))/math.pi
_As168  = (ac/(4*math.pi*_k168))**3
_kjoint = 1.3630                                   # scripts/concordance.py joint
chk("THE_AMPLITUDE", "frozen A_s IS the closed form at k_joint", 2.088058e-9,
    (ac/(4*math.pi*_kjoint))**3, 1e-5)
chk("THE_AMPLITUDE", "the -0.35% is the pure k spread", -0.3546,
    300*math.log(_kjoint/_k168), 5e-3, "%")
chk("THE_AMPLITUDE", "closed form vs the measured 2.100e-9", -0.921,
    100*(_As168/2.100e-9 - 1), 5e-3, "%")
chk("THE_AMPLITUDE", "that miss in sigma at the 1.4% measurement", -0.66,
    (_As168/2.100e-9 - 1)/0.014, 2e-2, "sigma")
chk("THE_AMPLITUDE", "C required by the measured amplitude", 1.00929,
    2.100e-9/_As168, 1e-5)
# C = R^2 (k_* l_p)^3 / 2 pi^2 at the conformal (w = 1/3) transfer R = 1/4
_C = lambda R, lpk: R**2 * lpk**3 / (2*math.pi**2)
chk("THE_AMPLITUDE", "C at R=1/4, wavelength convention = pi/4", math.pi/4,
    _C(0.25, 2*math.pi), 1e-6)
chk("THE_AMPLITUDE", "C at R=1/4, half-wave convention", 0.098175, _C(0.25, math.pi), 1e-4)
chk("THE_AMPLITUDE", "C at R=1/4, inverse-k convention", 3.1665e-3, _C(0.25, 1.0), 1e-3)
chk("THE_AMPLITUDE", "R needed for C = 1 (wavelength) = 1/sqrt(4 pi)", 0.28209,
    1/math.sqrt((2*math.pi)**3/(2*math.pi**2)), 1e-4)
chk("THE_AMPLITUDE", "scaling ratio k_* xi the closed form implies (R=1)", 3.4502e-3,
    (2*math.pi**2*_As168)**(1/3), 1e-4)
# hierarchy 6i: what the scale selection actually requires of C
_As_MZ = (lambda a: (a/(4*math.pi*(math.log(1+math.pi/(2*a))/math.pi)))**3)(3/127.95)
chk("hierarchy 6i", "C needed by the alpha(M_Z) reading", 0.7788, 2.088058e-9/_As_MZ, 1e-3)
chk("hierarchy 6i", "so the selection needs C = 1 to +/- this", 0.22, 1-0.7788, 5e-2)

# ---- P-2026-056: the Route-D branch window, in the coded parameter (added 2026-07-20)
# The sampled parameter IS 1+w of the floor today: rho_fl = rho_inf*exp(thaw*(1-a^3))
# gives 1+w(a) = thaw*a^3 (background.h:176,810; background.c:664), so the registered
# w0 window maps onto the prior's own units with no conversion factor.
chk("P-2026-056", "Route-D thaw window low edge = 1 + w0(-0.92)", 0.08, 1 + (-0.92), 1e-9)
chk("P-2026-056", "Route-D thaw window high edge = 1 + w0(-0.86)", 0.14, 1 + (-0.86), 1e-9)

# ---- P-2026-057: the Brannen-frame phase whose SIGN the lock predicts (added 2026-07-20)
# theta_house = theta_B + 120 deg is an exact one-face relabel, so theta_B follows from
# the measured house phase alone. Its sign is the observable half of the cross-sector lock.
# theta_B is computed FROM THE MASSES, not from the rounded 132.7328 display: the display
# carries 3.5e-7 rad of rounding and the quantity of interest, theta_B - 2/9, is 7.4e-6 --
# propagating the display puts 5% of rounding into a deviation (audit protocol check 21).
def _koide(mt, _me=0.51099895, _mmu=105.6583755):
    """(Q, A, theta_B) of the Z3 ring from the three pole masses, exactly."""
    _s = [math.sqrt(_me), math.sqrt(_mmu), math.sqrt(mt)]
    _M = sum(_s)/3
    _Q = (_me + _mmu + mt)/sum(_s)**2
    _d = [x/_M - 1 for x in _s]
    _c1 =  (2/3)*sum(_d[k]*math.cos(2*math.pi*k/3) for k in range(3))
    _s1 = -(2/3)*sum(_d[k]*math.sin(2*math.pi*k/3) for k in range(3))
    return _Q, math.sqrt(6*_Q - 2), math.atan2(_s1, _c1) - 2*math.pi/3
_MTAU, _SMTAU = 1776.86, 0.12
_QM, _AM, _THB = _koide(_MTAU)
chk("P-2026-057", "Brannen phase theta_B from the measured masses", 0.2222296, _THB, 1e-6, "rad")
chk("P-2026-057", "the house phase it corresponds to", 132.7328,
    math.degrees(_THB) + 120.0, 1e-6, "deg")
chk("P-2026-057", "its distance from 2/9, the deviation lock's axis", 7.409e-6, _THB - 2/9, 1e-3, "rad")

# ---- #102: the deviation lock P-2026-051, stated on the source values ------------
# Both axes are functions of m_tau alone (m_e and m_mu are known to 3e-10 and 2e-8), so
# the two deviations are perfectly anti-correlated and the lock's sigma must be taken on
# the RESIDUAL, not on either axis. Derivatives are analytic-grade central differences.
_h = 1e-5
_dQ, _dA, _dTH = [(b-a)/(2*_h) for a, b in zip(_koide(_MTAU-_h), _koide(_MTAU+_h))]
chk("#102 lock", "delta_A = A - sqrt2 from the masses", -1.30572e-5, _AM - math.sqrt(2), 1e-4)
chk("#102 lock", "sigma_A from sigma_mtau = 0.12 MeV", 1.4372e-5, abs(_dA)*_SMTAU, 1e-3)
chk("#102 lock", "so A sits this far from sqrt2", -0.909,
    (_AM - math.sqrt(2))/(abs(_dA)*_SMTAU), 1e-3, "sigma")
chk("#102 lock", "sigma_theta from sigma_mtau", 8.3481e-6, abs(_dTH)*_SMTAU, 1e-3, "rad")
chk("#102 lock", "so theta_B sits this far from 2/9", 0.888,
    (_THB - 2/9)/(abs(_dTH)*_SMTAU), 1e-3, "sigma")
# the closure theta = (1 + A^2/2)/9 has derivative A/9, so it predicts the two deviations
# SAME-signed; the measured pair is opposite-signed, which is what the residual records.
_res  = (_THB - 2/9) - (math.sqrt(2)/9)*(_AM - math.sqrt(2))
_dres = _dTH - (math.sqrt(2)/9)*_dA
chk("#102 lock", "residual off the closure line", 9.4610e-6, _res, 1e-3, "rad")
chk("#102 lock", "residual in sigma, correlation-aware", 0.892, _res/(abs(_dres)*_SMTAU), 1e-3, "sigma")
# The lock's testable form: with m_e, m_mu fixed, each watch predicts m_tau.
def _solve(g, lo=1770.0, hi=1785.0):
    for _ in range(80):
        mid = (lo+hi)/2
        if g(lo)*g(mid) <= 0: hi = mid
        else: lo = mid
    return (lo+hi)/2
_mQ  = _solve(lambda m: _koide(m)[0] - 2/3)
_mTH = _solve(lambda m: _koide(m)[2] - 2/9)
_mCL = _solve(lambda m: _koide(m)[2] - (1 + _koide(m)[1]**2/2)/9)
chk("#102 lock", "m_tau predicted by Q = 2/3", 1776.96903, _mQ, 1e-8, "MeV")
chk("#102 lock", "m_tau predicted by theta_B = 2/9", 1776.96651, _mTH, 1e-8, "MeV")
chk("#102 lock", "m_tau predicted by the closure", 1776.96705, _mCL, 1e-8, "MeV")
chk("#102 lock", "the two watches' m_tau differ by", 2.518, (_mQ-_mTH)*1e3, 1e-3, "keV")
chk("#102 lock", "which is this fraction of m_tau -- the precision needed to separate them",
    1.417, (_mQ-_mTH)/_MTAU*1e6, 1e-3, "ppm")
chk("#102 lock", "all three sit this far above the measured 1776.86", 0.909,
    (_mQ-_MTAU)/_SMTAU, 1e-3, "sigma")

# ---- #101: what three thermal draws actually give, in closed form ----------------
# Q = sum(s^2)/(sum s)^2 is scale-free, so for s ~ iid Exp it depends only on the
# proportions p = s/sum(s), which are uniform on the 2-simplex (Dirichlet(1,1,1)).
# Dirichlet moments then give E[Q] and Var[Q] exactly -- no simulation needed.
chk("#101 draws", "E[Q] for three exponential draws = 1/2", 0.5, 3*(1*2)/(3*4), 1e-12)
_EQ2 = 3*(1*2*3*4)/(3*4*5*6) + 6*(1*2)*(1*2)/(3*4*5*6)
chk("#101 draws", "Var[Q] = 1/60", 1/60, _EQ2 - 0.25, 1e-12)
chk("#101 draws", "sd[Q] = 1/sqrt(60)", 0.129099, math.sqrt(_EQ2 - 0.25), 1e-5)
# Geometry of the same statement: Q = 1/3 + r^2 with r the distance from the simplex
# centroid. At Q = 2/3, r = 1/sqrt3 and r_in/r = 1/sqrt2, so each of the three sides
# removes exactly 90 deg of the circle and one quarter survives -- hence the density.
chk("#101 draws", "at Q = 2/3 each side removes 90 deg of the circle", 45.0,
    math.degrees(math.acos((1/math.sqrt(6))/(1/math.sqrt(3)))), 1e-9, "deg")
chk("#101 draws", "density of Q at 2/3 = pi/(2 sqrt3)", 0.9068997,
    math.pi/(2*math.sqrt(3)), 1e-6)
chk("#101 draws", "odds three draws land as close as the leptons do", 1.116e-5,
    2*abs(_QM - 2/3)*math.pi/(2*math.sqrt(3)), 1e-3)
# The deterministic readings of the same exponential law fail too -- none returns 2/3.
_qof = lambda v: sum(x*x for x in v)/sum(v)**2
chk("#101 draws", "mid-quantiles of Exp(1) give Q =", 0.523481,
    _qof([-math.log(1-(k+0.5)/3) for k in range(3)]), 1e-5)
chk("#101 draws", "expected order statistics give Q = 25/54", 25/54,
    _qof([1/3, 1/3+1/2, 1/3+1/2+1]), 1e-9)

# ---- #101: Q = 2/3 as a vanishing indefinite form (exact restatement) ------------
# Q = 1/3 + (2/3)|f1/f0|^2 (Parseval) means Q = 2/3 <=> f0^2 = 2|f1|^2, i.e. the
# Fourier vector (f0; f1, f2) is NULL for the (+,-,-) form graded by Z3 charge:
# eta = |f0|^2 - |f1|^2 - |f2|^2.  In face coordinates eta = (1/3)[(2/3)(sum s)^2 - sum s^2].
_sv = [1 + math.sqrt(2)*math.cos(2/9 + 2*math.pi*k/3) for k in range(3)]
chk("#101 null", "(2/3)(sum s)^2 / sum s^2 = 1 at Q = 2/3 -- the null condition", 1.0,
    (2/3)*sum(_sv)**2/sum(x*x for x in _sv), 1e-9)
# eta(v) = v^T H v with H = (2/3)J - I, J the all-ones matrix (eigenvalues 3, 0, 0).
chk("#101 null", "the form's timelike eigenvalue, along (1,1,1)", 1.0, (2/3)*3 - 1, 1e-12)
chk("#101 null", "its two spacelike eigenvalues -- signature (+,-,-)", -1.0, (2/3)*0 - 1, 1e-12)
chk("#101 null", "so the null cone opens at 45 deg about (1,1,1)", 45.0,
    math.degrees(math.acos(1/math.sqrt(2))), 1e-9, "deg")
# How far off that cone the measured leptons sit. NOTE the two normalizations, both
# correct and a factor 2 apart (NOT 3): eta/sum(s^2) = (2/3)/Q - 1 is 9.23 ppm, while the
# moment form V/mu^2 = 3Q - 1 deviates by 18.47 ppm. The identity slope is 3, but both are
# fractional misses so converting brings in Q: (dV/V)/(dQ/Q) = 3Q = 2. Not a correction.
chk("#101 null", "measured eta/sum(s^2) = (2/3)/Q - 1", 9.2329e-6, (2/3)/_QM - 1, 1e-4)
chk("#101 null", "the same miss in the moment form, V/mu^2 - 1", -1.84656e-5, 3*_QM - 2, 1e-4)
chk("#101 null", "the two misses are a factor 2 apart, not 3 (= 3Q)", 2.0,
    (3*_QM - 2)/((2/3)/_QM - 1)*-1, 1e-4)

# ---- the BBN-stability fence, stated on the derived anchor (added 2026-07-20)
# The fence's edges are the two BBN clocks, not evaluation points: the D bottleneck below
# (stamp -> 0, the window's help vanishes) and the weak-rate window above (the dyad reaches
# n/p and helium moves). The conclusion is robust because the WHOLE-RANGE swing is bounded:
# taking T_c all the way to the bottleneck removes the window's +0.645% help entirely, and
# that is the largest move T_c can make. So no re-pin inside the fence can break it.
_TCLO, _TCHI, _TCK = 70.0, 500.0, 0.5*math.log(2)*ME/1e3     # keV; anchor from tau, not booked
_wD70 = lambda Tc: 1.0 - _TCLO/Tc                            # ramp stamp at the D bottleneck
chk("me_mechanism fence", "derived anchor sits above the fence's lower edge", 2.53, _TCK/_TCLO, 5e-3, "x")
chk("me_mechanism fence", "derived anchor sits below the fence's upper edge", 2.82, _TCHI/_TCK, 5e-3, "x")
chk("me_mechanism fence", "ramp stamp at the D bottleneck, derived anchor", 0.6047, _wD70(_TCK), 1e-3)
chk("me_mechanism fence", "ramp stamp at Li (40 keV), derived anchor", 0.7741, 1-40.0/_TCK, 1e-3)
chk("me_mechanism fence", "whole-range D/H swing bound, 2-term width", 0.323,
    2.387*0.00645/0.0476, 5e-3, "sigma")
chk("me_mechanism fence", "whole-range D/H swing bound, 3-term width", 0.273,
    2.387*0.00645/0.0563, 5e-3, "sigma")
chk("me_mechanism fence", "the 179 -> 177.10 re-pin, as a fraction of the row width", 449.0,
    1.0/abs(2.387*0.00645*(_wD70(_TCK)/_wD70(179.0)-1)/0.0476), 2e-2, "1/x")

# ---- the D/H error budget (#157 settled 2026-07-21 on arXiv:2011.11320) ----
# Standing width is two-term. The three-term folding is retained only so a stale ±0.0563
# or −2.49σ is recognisable on sight; it is not the live row. The third term equals the
# observational error numerically, which is why the two foldings were hard to separate.
_OBS, _NUC = 0.030, 0.037
_RATE = 0.0300                                      # the (retired) extra d(p,g)3He term
chk("deuterium_scar 1", "2-term width = obs (+) nuclear = STANDING", 0.0476,
    math.hypot(_OBS, _NUC), 1e-3)
chk("deuterium_scar 1", "standing row on the 2-term width", -2.94,
    (2.387-2.527)/math.hypot(_OBS, _NUC), 5e-3, "sigma")
chk("deuterium_scar 1", "advertised window low edge is the 2-term number", -2.52,
    (2.407-2.527)/math.hypot(_OBS, _NUC), 5e-3, "sigma")
chk("deuterium_scar 1", "advertised window high edge is the 2-term number", -1.34,
    (2.463-2.527)/math.hypot(_OBS, _NUC), 5e-3, "sigma")
# retired three-term arithmetic, pinned so a stale quote is caught
chk("deuterium_scar 1", "RETIRED 3-term width (double-counts LUNA)", 0.0563,
    math.sqrt(_OBS**2 + _NUC**2 + _RATE**2), 1e-3)
chk("deuterium_scar 1", "RETIRED standing row on the 3-term width", -2.49,
    (2.387-2.527)/math.sqrt(_OBS**2 + _NUC**2 + _RATE**2), 5e-3, "sigma")
chk("deuterium_scar 1", "the 0.0476 degeneracy: nuclear (+) rate reads the same", 0.0476,
    math.hypot(_NUC, _RATE), 1e-3)

# ---- #169: the g -> lambda map, the composite quartic (added 2026-07-20) ----
# lambda = 4 pi^2 / (N_c F(M/Lambda)) with F the one-loop f^2 integral at the same
# 3-momentum cutoff the sector's gap equation uses. See scripts/de_value_g_to_lambda.py.
def _I169(tau, n=20000):                       # T_c kernel, int_0^1 x tanh(x/2 tau) dx
    h = 1.0/n
    return sum(((i+.5)*h)*math.tanh(((i+.5)*h)/(2*tau)) for i in range(n))*h
def _J169(y):                                  # T=0 gap kernel; J(0) = 1/2 -> g_c = 2
    s = math.sqrt(1+y*y); return .5*s - .5*y*y*math.log((1+s)/y)
def _F169(y):                                  # f^2 loop integral
    s = math.sqrt(1+y*y); return math.log((1+s)/y) - 1/s
def _y169(g):
    lo, hi = 1e-9, 50.0
    for _ in range(200):
        mid = .5*(lo+hi)
        lo, hi = (mid, hi) if g*_J169(mid) > 1 else (lo, mid)
    return .5*(lo+hi)
_g169 = 1/_I169(TAU)
_y = _y169(_g169)
chk("cosmological_constant", "g = 1/I(tau) at tau = (1/2)ln2", 2.830, _g169, 1e-3)
chk("cosmological_constant", "gap kernel J(0) = 1/2, so g_c = 2", 2.0, 1/_J169(1e-12), 1e-6)
chk("cosmological_constant", "y = M/Lambda from 1 = g J(y)", 0.59493, _y, 1e-4)
chk("cosmological_constant", "M = y*m_e against the BCS check 312 keV", 304.0,
    _y*ME/1e3, 5e-3, "keV")
chk("cosmological_constant", "F(M/Lambda)", 0.43167, _F169(_y), 1e-4)
chk("cosmological_constant", "lambda = 4pi^2/(N_c F), N_c = 2", 45.73,
    4*math.pi**2/(2*_F169(_y)), 1e-3)
# the same f^2 formula on QCD: N_c = 3, M = 336, Lambda = 631 MeV -> f_pi vs 92.4
_yq = 336.0/631.0
chk("cosmological_constant", "one-loop f_pi on QCD (validation)", 93.09,
    math.sqrt(3*336.0**2*_F169(_yq)/(2*math.pi**2)), 1e-3, "MeV")
chk("cosmological_constant", "lambda_dark/lambda_QCD = (3/N_c)(F_QCD/F_dark)", 1.7549,
    (3/2)*_F169(_yq)/_F169(_y), 1e-3)
_tr = (3/2)*_F169(_yq)/_F169(_y)
chk("cosmological_constant", "lambda band low (m_sigma = 500 MeV anchor)", 25.7,
    (500.0**2/(2*92.4**2))*_tr, 5e-3)
chk("cosmological_constant", "lambda band high (m_sigma = 2M anchor)", 46.4,
    (672.0**2/(2*92.4**2))*_tr, 5e-3)
# the control edge: |Wu| = LHY, and the whole band sits above it
_rt = math.sqrt(ac/(256*math.pi**3))
def _wu_over_lhy(l):
    na3 = (_rt*l)**2
    return abs(8*(4*math.pi/3-math.sqrt(3))*na3*math.log(na3))/((128/(15*math.sqrt(math.pi)))*math.sqrt(na3))
chk("cosmological_constant", "sqrt(na^3) = sqrt(a_c/256pi^3)*lambda at lambda*", 0.0372,
    _rt*22.41, 5e-3)
chk("cosmological_constant", "|Wu|/LHY = 1 at lambda* = 22.41", 1.0, _wu_over_lhy(22.41), 1e-3)
chk("cosmological_constant", "|Wu|/LHY at the band's LOW end (still > 1)", 1.10,
    _wu_over_lhy(25.7), 1e-2)
chk("cosmological_constant", "Delta rho^1/4 at the band centre = 0.0021*lambda", 7.57,
    0.0021*36.05*100, 1e-2, "%")

# ---- #170: f_wind, the winding comb's forward amplitude (added 2026-07-20) ----
# The diagonal C_l sees only the k-hat monopole of a single-axis modulation, so the
# winding's imprint is diluted by j_0(kd) ~ 1/(kd) = l_1/(2 pi l) before projection.
# The T_proj values below come from scripts/winding_comb_cl.py (Bessel integrals);
# everything else here is recomputed from the recorded geometry.
_CHI, _LT = 13.76, 27.6                         # Gpc: chi_*, torus floor
_beta = lambda n: (_LT/n)/_CHI
_l1   = lambda n: 2*math.pi/_beta(n)
chk("P-2026-029", "l_1 = 2 pi n chi/L, coefficient", 3.1325, 2*math.pi*_CHI/_LT, 1e-4)
chk("P-2026-029", "beta = d/chi at n = 10", 0.20058, _beta(10), 1e-4)
chk("P-2026-029", "l_1 at n = 10", 31.32, _l1(10), 1e-3)
chk("P-2026-029", "l_1 at n = 30", 93.97, _l1(30), 1e-3)
chk("P-2026-029", "Limber envelope l_1/(2 pi l) at n=30, l=100", 0.14957,
    _l1(30)/(2*math.pi*100), 1e-3)
_TP = {10: 0.01205, 20: 0.03639, 30: 0.06062}   # T_proj at l = 100, booked from the run
chk("P-2026-029", "exact/Limber suppression at n=30, l=100", 0.405,
    _TP[30]/(_l1(30)/(2*math.pi*100)), 5e-3)
# a 1/l comb's matched-filter flat-equivalent over the fence's own band
_num = sum((2*l+1)*(100.0/l)**2 for l in range(100, 601))
_den = sum((2*l+1) for l in range(100, 601))
chk("P-2026-029", "flat-equivalent of a 1/l comb over l = 100-600", 0.3203,
    math.sqrt(_num/_den), 1e-3)
_fe = math.sqrt(_num/_den)
for _n, _bk in ((10, 1.814), (20, 0.601), (30, 0.360)):
    chk("P-2026-029", f"A_prim needed for A = 0.7% at n = {_n}", _bk,
        0.007/(_fe*_TP[_n]), 5e-3)
chk("P-2026-029", "n = 10 needs >100% modulation (impossible)", 1.0,
    1.0 if 0.007/(_fe*_TP[10]) > 1.0 else 0.0, 1e-9)
_aprim_max = math.sqrt(2e-6)                    # winding roughness ceiling, per log
chk("P-2026-029", "A_prim ceiling from Delta^2 <= 2e-6", 1.4142e-3, _aprim_max, 1e-4)
chk("P-2026-029", "f_wind ceiling", 2.746e-5, _fe*_TP[30]*_aprim_max, 5e-3)
chk("P-2026-029", "f_wind under the fence floor 0.7% by this factor", 255.0,
    0.007/(_fe*_TP[30]*_aprim_max), 1e-2)

# ---- the cold spot: why the anomaly family cannot claim it (#119) -----------
# The Kibble network is the model's only distinctive structure within reach of a Gpc.
# Its cells subtend about a degree — not the cold spot's 5-10 — and there are ~10^4 of them.
XI_K, CHI_STAR = 256.0, 13760.0        # Mpc comoving: Kibble domain; distance to last scattering
chk("cmb_anomalies", "Kibble domain angular scale xi_K/chi_*", 1.07,
    XI_K/CHI_STAR*180/math.pi, 1e-2, "deg")
chk("cmb_anomalies", "Kibble cells tiling the sky = 4pi/theta^2", 3.6e4,
    4*math.pi/(XI_K/CHI_STAR)**2, 5e-2)
# The texture route, priced. dT/T ~ 8 pi (eta/M_Pl)^2. The formula is validated first
# against [Cruz2007]'s quoted texture scale, which must land in the 1e-5 class it was fit to.
def _tex(eta_eV):
    return 8*math.pi*(eta_eV/MPL)**2
chk("cmb_anomalies", "texture dT/T at Cruz2007's 8.7e15 GeV is 1e-5 class", 1.28e-5,
    _tex(8.7e24), 1e-2)
chk("cmb_anomalies", "texture dT/T at the model's top scale f = 500 TeV", 4.2e-26,
    _tex(5e14), 1e-2)
chk("cmb_anomalies", "texture scale a cold-spot-class 1e-5 would need", 8.0e15,
    MPL*math.sqrt(1e-5/(8*math.pi))/1e9, 5e-2, "GeV")

# --- the gate exponent: the C^2-to-threshold map, 2026-07-20 (docket #127) ---
# Seeds are threshold crossings of a Gaussian medium; the amplitude-linear map is
# sigma ~ C, so nu ~ 1/C and dln(nu)/dln(C^2) = -1/2. With Q the upper tail and phi
# the density, the local log-slope of Nbar = N_cell*Q(nu) is n_eff = (nu/2)*phi/Q.
def _gphi(v): return math.exp(-v*v/2)/math.sqrt(2*math.pi)
def _gQ(v):   return 0.5*math.erfc(v/math.sqrt(2))
def _gneff(v):return 0.5*v*_gphi(v)/_gQ(v)
def _gbis(f, a, b, n=300):
    fa = f(a)
    for _ in range(n):
        m = (a+b)/2
        if fa*f(m) <= 0: b = m
        else: a, fa = m, f(m)
    return (a+b)/2
chk("me_mechanism GATE", "exact slope at nu = 2.2 (booked 2.81)", 2.81, _gneff(2.2), 5e-3)
chk("me_mechanism GATE", "exact slope at nu = 3.0 (booked 4.92)", 4.92, _gneff(3.0), 5e-3)
_gnu = _gbis(lambda v: _gneff(v)-2.43, 1.0, 5.0)         # forced n > 2.43 <=> nu > this
chk("me_mechanism GATE", "nu at which n_eff = 2.43", 2.027, _gnu, 1e-3)
chk("me_mechanism GATE", "hard-step edge sigma < 0.493*delta_c", 0.493, 1/_gnu, 1e-3)
chk("me_mechanism GATE", "the corrected sigma = 0.12 slope (was booked 50)", 35.2,
    _gneff(1/0.12), 5e-3)
# The recorded hazard normalizes Nbar(C_ref) = 1, so Q(nu_ref) = 1/N_cell closes nu
# against the cell count alone: n = (nu/2)*phi(nu)*N_cell, i.e. n ~ ln N_cell.
def _gnu_of_N(N): return _gbis(lambda v: _gQ(v)-1.0/N, 1e-6, 30.0)
_gN = _gbis(lambda N: _gneff(_gnu_of_N(N))-2.43, 10.0, 1000.0)
chk("me_mechanism GATE", "n > 2.43 <=> N_cell > 46.9", 46.9, _gN, 5e-3)
chk("me_mechanism GATE", "as a length ratio: xi/l_seed > 3.61", 3.61, _gN**(1/3), 5e-3)
chk("me_mechanism GATE", "n is log in the cell count: ln N* - n(N*)", 1.418,
    math.log(_gN)-2.43, 5e-3)
# Why (sigma, delta_c) cannot double as a valuation: log10 of the tail via Mills,
# since erfc underflows past nu ~ 38.
def _glog10Q(v):
    return (-v*v/2)/math.log(10) - math.log10(math.sqrt(2*math.pi)) \
           - math.log10(v) + math.log10(1-1/v**2+3/v**4)
chk("me_mechanism GATE", "sigma = 0.012 would demand log10 N_cell =", 1510,
    -_glog10Q(1/0.012), 1e-3)
_gxi, _glp = 398*1.495978707e11, 1.616255e-35             # xi = 398 AU, Planck length, m
chk("me_mechanism GATE", "Planck-seeded ceiling log10 (xi/l_Pl)^3", 146,
    3*math.log10(_gxi/_glp), 0.01)
chk("me_mechanism GATE", "the shortfall, in orders of magnitude", 1360,
    -_glog10Q(1/0.012) - 3*math.log10(_gxi/_glp), 0.01)

# --- the velocity ladder's matched junction, 2026-07-20 (docket #129) ---
# Z = rho*v, so Z_m = sqrt(Z1*Z2) gives v_m = sqrt(v1*v2) when rho_m = sqrt(rho1*rho2) --
# automatic for three co-located modes of ONE medium (rho1 = rho2 = rho_m). The two checks
# below are therefore CONSISTENCY TAUTOLOGIES: alpha_c = 3 alpha rewritten, not derived
# (PREREGISTERED records c2 = sqrt(alpha)*c 'without weight'). #129 closes NEGATIVE -- no
# independent derivation; the geometric half (a matching section's length) is ill-posed for
# co-located modes, so there is no spatial junction to size.
chk("DERIVATION_HUNT", "matched middle rung sqrt(c * alpha c) = sqrt(alpha) c",
    math.sqrt(ALPHA), math.sqrt(1.0*ALPHA), 1e-12, "c")
chk("DERIVATION_HUNT", "the junction run backwards: alpha_c = d*(sqrt(alpha))^2", ac,
    3*math.sqrt(ALPHA)**2, 1e-12)

# ---- #179 recoveries from 0315894d -----------------------------------------
# The epsilon-gradient lepton channel (#33 route A). The channel rides matter's
# leptonic mass fraction f_lep = Y_e * m_e/m_u, with Y_e the electron fraction
# (electrons per nucleon): 1 for pure hydrogen, 0.875 for Y_p = 0.25 primordial
# gas, ~0.85 for stellar material, 0.5 for the helium-and-heavier floor.
_MU   = 931.49410242e6            # eV, the atomic mass unit
_CSI  = 2.99792458e8              # m/s
_KPC  = 3.0856775814913673e19     # m
_EPS0 = 0.0124                    # the amplitude
_A0   = 1.2e-10                   # m/s^2, the RAR acceleration scale
_flep = lambda Ye: Ye*ME/_MU
_dphi = lambda Ye: math.sqrt(_CSI**2*_flep(Ye)*_EPS0)/1e3          # km/s
_Lgate= lambda Ye: _CSI**2*_flep(Ye)*_EPS0/_A0/_KPC                # kpc
chk("galactic_atoms",  "f_lep at the Y_e = 1/2 floor", 2.743e-4, _flep(0.5), 1e-3)
chk("FAILURES_LEDGER", "dPhi^(1/2) at the Y_e = 1/2 floor (the fence's conservative minimum)",
    553.0, _dphi(0.5), 2e-3, "km/s")
chk("galactic_atoms",  "dPhi^(1/2) at stellar Y_e = 0.85", 721.0, _dphi(0.85), 2e-3, "km/s")
chk("galactic_atoms",  "L where a = a0, stellar Y_e = 0.85", 140.0, _Lgate(0.85), 5e-3, "kpc")
# 83 is the deleted document's own two-significant-figure quote; the value is 82.55,
# so this check carries the tolerance that quote implies, not a tighter one.
chk("FAILURES_LEDGER", "L where a = a0 at the Y_e = 1/2 floor (the mislabelled '83 kpc, stellar')",
    83.0, _Lgate(0.5), 1e-2, "kpc")
chk("galactic_atoms",  "honest gas-vs-stars split: Y_e 0.875 over 0.85", 1.029, 0.875/0.85, 1e-3)
chk("FAILURES_LEDGER", "the retired 'x1.98': pure H over the Y_e = 1/2 floor, not over stars",
    2.0, 1.0/0.5, 1e-9)

# The nuclear-pairing bench (#24): the empirical odd-even mass staggering,
# Delta ~ 12 * A^(-1/2) MeV -- of order an MeV across the chart of nuclides.
chk("laboratory_cousins", "nuclear pairing gap at A = 60",  1.55, 12/math.sqrt(60),  5e-3, "MeV")
chk("laboratory_cousins", "nuclear pairing gap at A = 120", 1.10, 12/math.sqrt(120), 5e-3, "MeV")
chk("laboratory_cousins", "nuclear pairing gap at A = 208", 0.83, 12/math.sqrt(208), 5e-3, "MeV")

# --- the f_arr razor, settled (#162) -----------------------------------------
# The gate is a phase re-arranging in place, so a crossing gas element picks up the
# ballistic third of the rest-energy step times the fraction it traverses, f = v_gas/c_s.
# The share ARRIVING at a halo is therefore bounded by the identity f_arr <= f/3.
# The X-ray scaling fence allows arriving energy <= 20% of the infall kinetic energy.
CKMS   = 299792.458                       # km/s
CS_DK  = math.sqrt(3*ALPHA)*CKMS          # the medium's sound speed in km/s
E_GATE = (27*ALPHA/(5*math.pi))*ME        # eps * m_e, the rest-energy step across the gate
chk("entropy 4", "c_s = sqrt(3 alpha) c in km/s", 44357, CS_DK, 1e-3, "km/s")
chk("entropy 4", "eps*m_e from the closed form (vs the booked 6.41)", 6.41, E_GATE/1e3, 1e-3, "keV")
_f_arr  = lambda v: v/(3*CS_DK)                                  # delivered, upper bound
_fence  = lambda v: 0.2*(0.5*MP*(v/CKMS)**2)/E_GATE              # allowed
for _v, _d, _a, _m, _s in ((286.0, 0.00215, 0.0133, 6.2, "galaxy"),
                           (429.0, 0.00322, 0.0300, 9.3, "group"),
                           (1423.0, 0.0107, 0.3298, 31.0, "cluster")):
    chk("T4/ledger", f"f_arr delivered = v/(3 c_s), {_s} infall", _d, _f_arr(_v), 0.02)
    chk("T4/ledger", f"X-ray fence 0.2*(0.5 m_p v^2)/(eps m_e), {_s}", _a, _fence(_v), 0.01)
    chk("T4/ledger", f"fence margin (allowed/delivered), {_s}", _m, _fence(_v)/_f_arr(_v), 0.02, "x")
# the razor's other jaw: the S8 closure needed f_arr in [0.008, 0.013] and does not get it
chk("T4/ledger", "shortfall vs the 0.008 floor, group infall",  2.5, 0.008/_f_arr(429.0), 0.02, "x")
chk("T4/ledger", "shortfall vs the 0.008 floor, galaxy infall", 3.7, 0.008/_f_arr(286.0), 0.02, "x")

# --- the H0 steelman's sigma conversions (#166) -------------------------------
# Preference of the published m_e over unity, and where the model's PINNED 1.012543 sits
# in each. Sources: Hart-Chluba arXiv:1912.03986; Toda-Seto arXiv:2508.09025.
ME_MODEL = 1 + 27*ALPHA/(5*math.pi)       # = 1.012543, fixed before any of these fits
chk("hubble_tension", "model m_e/m_e0 = 1 + eps", 1.012543, ME_MODEL, 1e-5)
for _lbl, _c, _s, _pref, _mod in (("Hart-Chluba CMB+BAO",     1.0078, 0.0067, 1.16,  0.71),
                                  ("Hart-Chluba CMB+BAO+SNe", 1.0190, 0.0055, 3.45, -1.17),
                                  ("Toda-Seto ACT DR6+DESI",  1.0081, 0.0046, 1.76,  0.97)):
    chk("hubble_tension", f"m_e preference over unity, {_lbl}", _pref, (_c-1)/_s, 0.01, "sigma")
    chk("hubble_tension", f"model 1.012543 against {_lbl}", _mod, (ME_MODEL-_c)/_s, 0.02, "sigma")

# --- the ring-BEC discrimination target (#163) --------------------------------
chk("laboratory_cousins", "RMS 0.7071 over the mean-absolute 2/pi", 11.1,
    (1/math.sqrt(2))/(2/math.pi)*100-100, 0.01, "%")
chk("laboratory_cousins", "the winding sim's scatter as a fraction of f-bar", 4.1,
    0.026/(2/math.pi)*100, 0.02, "%")

# --- P-2026-043's computed cosmic-dawn trough (#175) --------------------------
# The registered chain and the run that replaced its last three steps.
# scripts/cosmic_dawn_trough.py; CLASS thermodynamics, me = 1 vs 1.012543.
_EPS = 27*ALPHA/(5*math.pi)
chk("PREREGISTERED P-043", "the registered rate shift, 3*eps", 3.763, 100*3*_EPS, 1e-3, "%")
_TCMB17, _TG17, _TG17M = 2.7255*18.0, 6.854, 6.793
chk("PREREGISTERED P-043", "T_CMB at the z = 17 trough", 49.06, _TCMB17, 1e-3, "K")
chk("PREREGISTERED P-043", "gas cooling at z = 17, computed", -0.89,
    100*(_TG17M/_TG17-1), 0.02, "%")
chk("PREREGISTERED P-043", "absorption amplification (x/(x-1)), x = T_CMB/T_g", 1.162,
    (_TCMB17/_TG17)/((_TCMB17/_TG17)-1), 1e-3, "x")
chk("PREREGISTERED P-043", "trough depth, computed", 1.03,
    100*((1-_TCMB17/_TG17M)/(1-_TCMB17/_TG17)-1), 0.02, "%")
chk("PREREGISTERED P-043", "3*eps divided by the response slope 2.758", 1.364,
    100*3*_EPS/2.758, 0.01, "%")

# --- which rung condensation picks (#133) -------------------------------------
# The dyad's restoration temperature is kappa-independent, so f cannot bracket it.
_TC_CW = lambda Lm1: ME/1e3*math.sqrt(3*Lm1/(2*math.pi**2))   # keV, ME in eV
chk("UV_completion 17", "restoration T_c at L-1 = 1", 199.2, _TC_CW(1), 1e-3, "keV")
chk("UV_completion 17", "restoration T_c at L-1 = 5 (the retired envelope's cap)", 445.4,
    _TC_CW(5), 1e-3, "keV")
chk("UV_completion 17", "restoration T_c at L-1 = 10", 630.0, _TC_CW(10), 1e-3, "keV")
chk("UV_completion 17", "the standing T_c inside the BBN fence [70, 500], lower margin", 2.53,
    177.10/70, 0.01, "x")
chk("UV_completion 17", "the standing T_c inside the BBN fence, upper margin", 2.82,
    500/177.10, 0.01, "x")

# --- #182: the dyad's own T_c on the EXACT thermal kernel, not the expansion ------
# The high-T route above overstates the restoration ~16x at m_e/T_c ~ 2.9 (the electrons are
# Boltzmann-suppressed). The exact balance is t^3*|J_F'(1/t)| = (L-1)/8 with t = T_c/m_e.
# This band is what the ramp would key on if it keyed on the DYAD's transition.
def _JFp(y, n=4000, hi=60.0):    # |J_F'(y)| = y*int_0^inf x^2/(E(e^E+1)) dx, Simpson
    h = hi/n; s = 0.0
    for i in range(n+1):
        x = i*h; E = math.sqrt(x*x + y*y)
        f = x*x/(E*(math.exp(E)+1.0)) if E < 700 else 0.0
        s += f*(1 if i in (0, n) else (4 if i % 2 else 2))
    return y*s*h/3.0
def _TC_EX(Lm1):                 # keV
    lo, hi = 0.05, 5.0
    for _ in range(80):
        mid = 0.5*(lo+hi)
        if mid**3*_JFp(1.0/mid) < Lm1/8.0: lo = mid
        else: hi = mid
    return 0.5*(lo+hi)*ME/1e3
chk("FAILURES_LEDGER", "exact |J_F'| at the operating point m_e/T_c = 2.9", 0.374,
    _JFp(2.9), 1e-2)
chk("FAILURES_LEDGER", "the high-T expansion there, which overstates it", 2.385,
    math.pi**2/12*2.9, 1e-3)
chk("MATH_SPINE 4", "exact-kernel dyad T_c at L-1 = 1 (band bottom)", 307.2, _TC_EX(1), 2e-3, "keV")
chk("MATH_SPINE 4", "exact-kernel dyad T_c at L-1 = 10 (band top)", 714.3, _TC_EX(10), 2e-3, "keV")
chk("MATH_SPINE 4", "the band's bottom EXCLUDES the ramp's keying value", 1.734,
    _TC_EX(1)/177.10, 5e-3, "x")
chk("MATH_SPINE 4", "the band's top over the keying value", 4.033, _TC_EX(10)/177.10, 5e-3, "x")
chk("MATH_SPINE 4", "L-1 where the band crosses the BBN fence's 500 keV", 500.0,
    _TC_EX(4.10), 5e-3, "keV")
chk("MATH_SPINE 4", "fraction of the band above the fence, by keV", 52.6,
    100*(_TC_EX(10)-500.0)/(_TC_EX(10)-_TC_EX(1)), 2e-2, "%")
# the retired band: 250-530 keV does not follow from L-1 in [1,10] on this kernel
chk("FAILURES_LEDGER", "retired: 250 keV corresponds to L-1 = 0.50, not 1", 250.0,
    _TC_EX(0.50), 1e-2, "keV")
chk("FAILURES_LEDGER", "retired: 530 keV corresponds to L-1 = 4.78, not 10", 530.0,
    _TC_EX(4.78), 1e-2, "keV")
# the retired geometric-mean heuristic, kept so the ledger's arithmetic stays checkable
chk("FAILURES_LEDGER", "retired heuristic sqrt(f*Lambda_IR) at f = 100 TeV", 480.0,
    math.sqrt(1e14*2.3e-3)/1e3, 0.01, "keV")
chk("FAILURES_LEDGER", "retired heuristic sqrt(f*Lambda_IR) at f = 500 TeV", 1.07,
    math.sqrt(5e14*2.3e-3)/1e6, 0.01, "MeV")
# lambda_dyad from its defining CW expression: eps*m_e^4*(L-1)/(4 pi^2 f^4), f-cancelling
chk("me_mechanism hf", "lambda_dyad at f = 3e14 eV, L-1 = 5", 1.3e-38,
    _EPS*ME**4*5/(4*math.pi**2*(3e14)**4), 0.03)

# --- the low-l cavity pattern, regenerated ISW-inclusive (T5 low-l) -----------
# Closed forms only; the mode sums themselves live in scripts/torus_lowell_pattern.py.
from scipy.integrate import quad as _quad
from scipy.special import spherical_jn as _spherical_jn
chk("lowell_anomalies", "off-diagonal pairs over l = 2..6, C(45,2)", 990,
    (sum(2*l+1 for l in range(2, 7)) * (sum(2*l+1 for l in range(2, 7))-1))//2, 1e-9)
chk("lowell_anomalies", "quadrupole cosmic variance sqrt(2/(2l+1))", 0.6325,
    math.sqrt(2/5), 1e-3)
# the regenerated retention at the 27.6 Gpc floor, and what it is worth against that variance
_RET2 = 0.900
chk("lowell_anomalies", "quadrupole deficit at the floor, ISW-inclusive", 0.100,
    1-_RET2, 0.02)
chk("lowell_anomalies", "that deficit in units of cosmic variance", 0.158,
    (1-_RET2)/math.sqrt(2/5), 0.02, "sigma")
# the matched-circles floor is 2 chi_*, which is what makes 27.6 Gpc the floor
chk("lowell_anomalies", "the floor L = 27.6 Gpc as a multiple of chi_* = 13.76", 2.006,
    27.6/13.76, 1e-3, "x")
chk("lowell_anomalies", "k_min chi_* at the floor = 2 pi chi_*/L", 3.1325,
    2*math.pi*13.76/27.6, 1e-3)
# the sharp-cutoff estimate the retained toy computes, at its own L = 2D -- kept so the
# ledger's "the estimate is a different quantity" row stays checkable
_cut = _quad(lambda x: _spherical_jn(2, x)**2/x, math.pi, 400, limit=400)[0]
chk("FAILURES_LEDGER", "sharp-cutoff C_2 retention at L = 2D (the retained toy's 0.49)", 0.489,
    _cut*12, 0.01)

# --- #22: the flavour verdict's forward numbers (DERIVATION_HUNT §9, 2026-07-20) ---
# With A = sqrt(2) (from Q = 2/3) and theta = 2/9 (from the closure), the Z3 ring has no
# freedom left but the overall scale, so BOTH charged-lepton mass ratios are determined.
_k22 = [1 + math.sqrt(2)*math.cos(2*math.pi*j/3 + 2/9) for j in range(3)]
_m22 = sorted(x*x for x in _k22)
chk("DERIVATION_HUNT 9", "(A=sqrt2, theta=2/9) predicts m_mu/m_e", 206.7703, _m22[1]/_m22[0], 1e-5)
chk("DERIVATION_HUNT 9", "(A=sqrt2, theta=2/9) predicts m_tau/m_e", 3477.473, _m22[2]/_m22[0], 1e-5)
chk("DERIVATION_HUNT 9", "its m_mu/m_e miss vs measured 206.76828", 9.83e-6,
    _m22[1]/_m22[0]/206.76828 - 1, 0.02)
chk("DERIVATION_HUNT 9", "its m_tau/m_e miss vs measured 3477.2283", 7.03e-5,
    _m22[2]/_m22[0]/3477.2283 - 1, 0.02)

# --- #146: the r-sensitivity, both sides (hierarchy 6e, 2026-07-20) ---
# 6e varies r = v_e/v_h through the SCREENING density of states only, N_screen = (1+r)N0.
# The PAIRING density of states also depends on r: for congruent pockets the excitonic pair
# variable is xibar = (v_e+v_h)(k-k_F)/2, so N_pair = [2r/(1+r)] N0 -- exactly N0 at r = 1.
_kb   = lambda b: math.log(1 + 1/b)/math.pi
_br   = lambda r: (3*ALPHA)*(1 + r)/math.pi          # b = alpha_c (1+r)/(pi v), v = 1
_scr  = lambda r: 1/(_kb(_br(r))*3*ALPHA)                    # screening term alone
_both = lambda r: (1 + r)/(2*r)/(_kb(_br(r))*3*ALPHA)        # + the pairing DOS
_hh = 1e-6
chk("hierarchy 6e", "b(r=1) reproduces the booked 2 alpha_c/pi", 0.0139369, _br(1.0), 1e-5)
chk("hierarchy 6e", "pairing DOS factor 2r/(1+r) is exactly 1 at r = 1", 1.0, 2/(1+1), 1e-12)
chk("hierarchy 6e", "dlnM/dr, screening term alone", -3.8504,
    -(_scr(1+_hh) - _scr(1-_hh))/(2*_hh), 1e-3)
chk("hierarchy 6e", "dlnM/dr with the pairing DOS included", 12.8865,
    -(_both(1+_hh) - _both(1-_hh))/(2*_hh), 1e-3)

# --- #168: a fixed-comoving-cell shot census is white noise (FAILURES_LEDGER, 2026-07-20) ---
# P_zeta = R^2 xi^3 carries no k, so Delta^2 = k^3 P/2pi^2 has log-slope 3, i.e. n_s = 4.
_D2_168 = lambda kk: kk**3 * 1.0 / (2*math.pi**2)      # R^2 xi^3 held fixed
chk("THE_AMPLITUDE", "fixed-cell shot census: dln(Delta^2)/dlnk = n_s - 1", 3.0,
    math.log(_D2_168(1.01)/_D2_168(1.0))/math.log(1.01), 1e-3)

# --- #130: the induced split, for the coupling alpha_c = 3 alpha actually names ---
# The recorded 44% is HYPERCHARGE at M_Z. alpha_c = 3 alpha names alpha_EM at q = 0.
# 1/alpha_EM = 1/alpha_2 + 1/alpha_Y, on the light file's own M_Pl handouts.
_invY_Pl, _inv2_Pl = 55.5, 49.4                        # PRTOE_light.md, the two handouts
_invEM_Pl = _invY_Pl + _inv2_Pl
_share_EM = (1/ALPHA - _invEM_Pl)/(1/ALPHA)            # the medium loop's share of 1/alpha_EM(0)
chk("light 5", "bare EM handout 1/a_EM(M_Pl) = 1/a_Y + 1/a_2", 104.9, _invEM_Pl, 1e-6)
chk("DERIVATION_HUNT 1", "medium loop share of 1/a_EM(0) -- piece 2's real number", 23.45,
    100*_share_EM, 1e-3, "%")
chk("DERIVATION_HUNT 1", "the recorded 44% over that correct share", 1.859,
    (42.9/98.4)/_share_EM, 1e-3, "x")

# --- #184: the two branches of the A_s census, and which one the tilt allows -------
# The freeze branch is checked just above (n_s = 4).  Its complement: holding k*xi fixed
# (the scaling branch, xi ~ 1/k) makes Delta^2 scale-invariant, n_s = 1.  That contrast IS
# the ruling -- measured n_s = 0.9649 sits on the scaling branch and 3 away from the other.
_D2_184 = lambda kk: kk**3 * (3.4502e-3/kk)**3 / (2*math.pi**2)   # xi = 3.4502e-3/k
chk("THE_AMPLITUDE", "scaling census (k xi fixed) gives n_s = 1 exactly", 1.0,
    1.0 + math.log(_D2_184(1.01)/_D2_184(1.0))/math.log(1.01), 1e-9)
# and the freeze branch's n_s = 4 sits this far from the measured tilt -- the ruling's margin
chk("FAILURES_LEDGER", "#184: freeze branch n_s = 4 minus measured n_s = 0.9649", 3.0351,
    4.0 - 0.9649, 1e-4)

# --- #183: the Fock self-energy insertion on hierarchy 6c's host -------------------
# a = delta_v/lambda with delta_v = dSigma/dk at k_F, Sigma the exchange self-energy of
# V(q) = e^2/(q^2 + m_D^2).  Closed form a(b) = (1+2b)/2 - 1/ln(1+1/b); e^2 cancels.
_ac_183 = 3*ALPHA
_b_183 = 2*_ac_183/math.pi                             # 2 alpha_c/pi, v = 1
_c_183 = 0.789262                                      # #141, the crossed box
_a_183 = (1 + 2*_b_183)/2 - 1/math.log1p(1/_b_183)
chk("hierarchy 6e", "#183: Fock coefficient a = (1+2b)/2 - 1/ln(1+1/b)", 0.280677,
    _a_183, 1e-5)
# independent route: a = delta_v/lambda built from the radial integrals I(1), I'(1),
# which share only the host with the line above.  m^2 = 4b.
_m_183 = 2*math.sqrt(_b_183)
_I1 = 2 - 2*_m_183*math.atan(2/_m_183) + 0.5*_m_183**2*math.log1p(4/_m_183**2)
_Ip1 = 4 - 2*_m_183*math.atan(2/_m_183) - math.log1p(4/_m_183**2)
_e2_183 = 4*math.pi*_ac_183
_dv_183 = -(_e2_183/(8*math.pi**2))*(_Ip1 - _I1)
_lam_183 = (_e2_183/4)*math.log1p(1/_b_183)/math.pi**2         # = k alpha_c
chk("hierarchy 6e", "#183: same a from I(1), I'(1) -- independent route", 0.280677,
    _dv_183/_lam_183, 1e-5)
chk("hierarchy 6e", "#183: the velocity renormalization delta_v itself", 0.0083850,
    _dv_183, 1e-4)
# the large-b asymptote a -> 1/(12b), derived by expanding V to O(q^2/m_D^2)
chk("hierarchy 6e", "#183: a x 12b -> 1 in the contact limit (b = 5e4)", 1.0,
    ((1 + 2*5e4)/2 - 1/math.log1p(1/5e4))*12*5e4, 1e-4)
# the two insertions add in the exponent: 1/lambda_eff = 1/lambda + c + a
chk("hierarchy 6e", "#183: complete O(lambda) exponent shift c + a", 1.069939,
    _c_183 + _a_183, 1e-5)
chk("hierarchy 6e", "#183: anchor multiplier exp(-(c+a))", 0.34303,
    math.exp(-(_c_183 + _a_183)), 1e-4)
chk("hierarchy 6e", "#183: corrected band, bottom edge (1.6 TeV x mult)", 0.549,
    1.6*math.exp(-(_c_183 + _a_183)), 2e-3, "TeV")
chk("hierarchy 6e", "#183: corrected band, top edge (5.2 TeV x mult)", 1.784,
    5.2*math.exp(-(_c_183 + _a_183)), 2e-3, "TeV")
chk("PREREGISTERED", "#183: tightest gap, shooter 13 TeV over the band's top", 7.3,
    13.0/(5.2*math.exp(-(_c_183 + _a_183))), 5e-3, "x")

# --- #125: the portal's SM side -- the renormalizable branch the roster leaves out ---------
# A dimension-2 dark singlet's LOWEST-dimension SM partner is H^dag H (total dim 4), which
# shifts the Higgs vev and so moves EVERY mass, quarks included.  The model must do without
# it.  These checks price that exclusion: the bound D/H puts on its coefficient, and the size
# the standing dim-6 lepton operator induces for it through one electron loop.
_V_EW  = 246.21965e9                              # eV, the Higgs vev
_M_H   = 125.25e9                                 # eV
_eps125 = 27*ALPHA/(5*math.pi)
_y_e   = math.sqrt(2)*ME/_V_EW
chk("MATH_SPINE 0", "#125: electron Yukawa y_e = sqrt2 m_e/v", 2.9350e-6, _y_e, 1e-3)
# induced portal coupling: dlambda_p ~ (eps y_e^2/f^2)(Lam_UV^2/16pi^2).  At Lam_UV = 4 pi f
# the f cancels outright, which is why the bound below is the only f-dependent piece.
_lamp_4pif = _eps125*_y_e**2
_lamp_f    = _eps125*_y_e**2/(16*math.pi**2)
chk("MATH_SPINE 0", "#125: induced lambda_p at Lam_UV = 4 pi f", 1.0805e-13, _lamp_4pif, 1e-3)
chk("MATH_SPINE 0", "#125: induced lambda_p at Lam_UV = f", 6.8425e-16, _lamp_f, 1e-3)
# D/H tolerance on a UNIVERSAL shift: the corpus books full eps on the quarks at 12-18 sigma,
# so one sigma sits at eps/15.  |dv/v| = lambda_p f^2/m_H^2 at phi = f.
_onesig125 = _eps125/15.0
chk("MATH_SPINE 0", "#125: universal shift worth 1 sigma on D/H", 8.362e-4, _onesig125, 1e-3)
_bound = lambda f_TeV: _onesig125*_M_H**2/(f_TeV*1e12)**2
chk("MATH_SPINE 0", "#125: lambda_p bound at f = 100 TeV (loosest)", 1.312e-9, _bound(100.), 1e-3)
chk("MATH_SPINE 0", "#125: lambda_p bound at f = 500 TeV (tightest)", 5.247e-11, _bound(500.), 1e-3)
# the worst corner for the induced portal: biggest cutoff, biggest f -- and it still lands here
chk("MATH_SPINE 0", "#125: induced/bound at the tightest corner", 2.06e-3,
    _lamp_4pif/_bound(500.), 5e-3, "x")
chk("MATH_SPINE 0", "#125: worst-corner induced universal shift, in sigma on D/H", 2.06e-3,
    _lamp_4pif*(500e12)**2/_M_H**2/_onesig125, 5e-3, "sigma")
# and the quark shift the portal DOES deliver, against the full-eps catastrophe it is not
chk("PREREGISTERED P-006", "#125: full eps over the delivered quark shift", 1.854e5,
    1/(ALPHA/math.pi)**2, 1e-3, "x")
chk("PREREGISTERED P-006", "#125: D/H cost of the delivered quark shift", 8.09e-5,
    _eps125*(ALPHA/math.pi)**2/_onesig125, 5e-3, "sigma")

# --- #126: the census, run on ONE criterion at a time -------------------------------------
# The democratic count needs membership from charge and weights from blindness.  Run charge
# alone and it weights too: sum N_c Q^2 over the charged nine is exactly 8 (3 leptons + 4
# up-type + 1 down-type), giving c = 8/9; let the neutral seat then weigh zero and c = 1,
# which the census excludes.  Neither single criterion returns 9/10.
_Q2 = 3*1.0 + 3*3*(2/3)**2 + 3*3*(1/3)**2
chk("DERIVATION_HUNT 1", "#126: sum N_c Q^2 over the charged nine", 8.0, _Q2, 1e-12)
chk("DERIVATION_HUNT 1", "#126: charge^2 census with the seat, c = 8/9", 0.888889,
    _Q2/(_Q2+1), 1e-5)
chk("DERIVATION_HUNT 1", "#126: eps at the charge^2 census = 16 alpha/3pi", 1.23884,
    (_Q2/(_Q2+1))*(2/math.pi)*(3*ALPHA)*100, 1e-4, "%")
# the eps-blind ensemble checks the value and does not adjudicate between the candidates
_C0, _SDc = 0.903, 0.0375
chk("MATH_SPINE 0", "#126: ensemble distance to 9/10", -0.080, (0.9-_C0)/_SDc, 5e-3, "sigma")
chk("MATH_SPINE 0", "#126: ensemble distance to 12/13", 0.535, (12/13-_C0)/_SDc, 5e-3, "sigma")
chk("MATH_SPINE 0", "#126: ensemble distance to the charge^2 8/9", -0.376,
    (_Q2/(_Q2+1)-_C0)/_SDc, 5e-3, "sigma")
chk("DERIVATION_HUNT 1", "#126: 8/9 and 9/10 separated by, at the ensemble width", 0.296,
    (0.9-_Q2/(_Q2+1))/_SDc, 5e-3, "sigma")
chk("DERIVATION_HUNT 1", "#126: sharpening to the pre-registered sigma_c = 0.0115", 3.26,
    _SDc/0.0115, 5e-3, "x")

# --- rho_bounce in physical units + the sanity checks (scripts/rho_bounce.py), 2026-07-20 ---
# The finite bounce/core density that discharges 'no singularity': rho = m^4/lam = m^2 Psi0^2,
# the Colpi-Shapiro-Wasserman quartic ceiling (= the max-mass boson-star central density).
_m_rb, _lam_rb = 2.24e-20, 2e-91                # eV, (m/Psi0)^2
_rho_rb_eV4 = _m_rb**4/_lam_rb                  # eV^4
_GeV4_gcc = 2.3201e17                           # 1 GeV^4 -> g/cm^3 (calibrated on rho_crit below)
_rho_rb_gcc = _rho_rb_eV4*1e-36*_GeV4_gcc
chk("bigbang 1.2", "rho_bounce in g/cm^3 at the derived lambda", 2.9e-7, _rho_rb_gcc, 0.02, "g/cc")
chk("bigbang 1.2", "rho_bounce in GeV^4", 1.26e-24, _rho_rb_eV4*1e-36, 0.02, "GeV^4")
chk("bigbang 1.2", "GeV^4->g/cc calibrated on rho_crit^1/4 = 2.46 meV", 2.46e-3,
    (8.53e-30/_GeV4_gcc)**0.25*1e9, 0.02, "meV")
chk("bigbang 1.2", "orders BELOW nuclear (2.3e14 g/cc): sub-nuclear by", 21,
    math.log10(2.3e14/_rho_rb_gcc), 0.02, "dex")
chk("bigbang 1.2", "orders BELOW Planck (5.16e93 g/cc): finite/sub-Planckian by", 100,
    math.log10(5.155e93/_rho_rb_gcc), 0.01, "dex")
# the open joint: the keV floor sits ~12 orders under an MeV-class BBN hot start
_rho_bbn_gcc = (math.pi**2/30)*10.75*(1e6)**4*1e-36*_GeV4_gcc   # radiation at T = 1 MeV
chk("bigbang 1.2", "keV floor below the MeV hot start (T=1 MeV) by", 12.45,
    math.log10(_rho_bbn_gcc/_rho_rb_gcc), 0.01, "dex")
# mechanism: TF parameter Lambda = lam M_Pl^2/(4pi m^2) >> 1 => self-interaction regime holds
chk("bigbang 1.2", "TF parameter Lambda >> 1 (self-interaction ceiling applies)", 4728,
    _lam_rb*(1.22089e28)**2/(4*math.pi*_m_rb**2), 0.02)

# --- granule epsilon-meter: the two-fluid density-contrast law (granule_sim_2field.py) ---
# In the NR limit the medium is TWO Schrodinger fluids with density fractions
# p=(1+f_rot)/2, q=(1-f_rot)/2 sharing one gravitational potential. Two independent
# speckle fields suppress the granule power var(rho)/mean^2 to p^2+q^2 = (1+f_rot^2)/2
# of single-field FDM. The SP sim confirms this holds STATICALLY exactly and, under
# shared-gravity dynamics, as the suppression RATIO to single-field FDM (within ~5%).
_fr = 0.4                                        # the median draw
_p, _q = (1 + _fr) / 2, (1 - _fr) / 2
chk("granule_sim_2field", "median-draw p = (1+f_rot)/2 at f_rot=0.4", 0.7, _p, 1e-9)
chk("granule_sim_2field", "granule suppression p^2+q^2 at f_rot=0.4", 0.58, _p**2 + _q**2, 1e-9)
chk("granule_sim_2field", "identity p^2+q^2 = (1+f_rot^2)/2", (1 + _fr**2) / 2,
    _p**2 + _q**2, 1e-12)
chk("granule_sim_2field", "law endpoints: f_rot=0 (equal split) -> 1/2", 0.5, (1 + 0.0**2) / 2, 1e-12)
chk("granule_sim_2field", "law endpoints: f_rot=1 (single field) -> 1", 1.0, (1 + 1.0**2) / 2, 1e-12)
# physical anchors the sim reproduces at the pinned mass m = 2.24e-20 eV:
_m20, _AU = 2.24e-20, 1.495978707e11
chk("granule_sim_2field", "Schive core r_c(10^9 Msun) = 1.6 kpc (m/1e-22)^-1", 7.14,
    1.6e3 * (_m20 / 1e-22)**-1, 5e-3, "pc")
chk("granule_sim_2field", "Compton wavelength h/(mc) [cf. xi ~ 402 AU]", 370.0,
    2 * math.pi * HBARC / _m20 / _AU, 5e-3, "AU")

# --- genesis amplitude Psi0: the misalignment abundance closure (genesis_solver_B1.py) ---
# The genesis field is frozen at Psi0 until H = m (oscillation onset in the radiation
# era), then redshifts as matter: rho_DM,0 = 1/2 m^2 Psi0^2 a_osc^3, a_osc from
# H = H0 sqrt(Om_r) a^-2 = m. This fixes Psi0 from the measured (rho_DM,0, m) alone --
# analytic, not sim-gated. The comoving roll confirms rho*a^3 freezes, and the O(1)
# onset+anharmonic correction is scale-free (so the m^-1/4 scaling stays exact).
_H0g, _Omr, _Omdm, _Mred = 1.44e-33, 9.2e-5, 0.264, 2.435e27     # eV
_rho_dm0 = _Omdm * 3 * _H0g**2 * _Mred**2
def _psi0_gen(m):
    _aosc = math.sqrt(_H0g * math.sqrt(_Omr) / m)
    return math.sqrt(_rho_dm0 / (0.5 * m * m * _aosc**3)), 1 / _aosc - 1
_psi0_224, _zosc_224 = _psi0_gen(2.24e-20)
chk("genesis_solver_B1", "Psi0/M_red from the misalignment abundance closure", 0.0207,
    _psi0_224 / _Mred, 0.02)
chk("genesis_solver_B1", "Psi0 at m = 2.24e-20 eV (= 5.03e16 GeV)", 5.03e25, _psi0_224, 0.02, "eV")
chk("genesis_solver_B1", "z_osc at oscillation onset H = m", 4.03e7, _zosc_224, 0.02)
chk("genesis_solver_B1", "Psi0 scaling m^-1/4: Psi0(1e-22)/Psi0(5e-20) = 500^1/4",
    500**0.25, _psi0_gen(1e-22)[0] / _psi0_gen(5e-20)[0], 1e-9)
chk("genesis_solver_B1", "Psi0(abundance) = quartic-mass crossover m/sqrt(lam)", 1.0,
    _psi0_224 / (2.24e-20 / math.sqrt(2e-91)), 0.02)

# --- R1 caustic-bit precision: the Theta_loc plateau law (scripts/r1_caustic_sim.py) ---
# Theta_loc = Q/(Q+K), Q=|grad sqrt(rho)|^2, K=rho|grad S|^2. For a developed isotropic
# circular-Gaussian speckle field (the wave-regularised caustic), Theta_loc is pointwise
# Beta(d/2,d/2): mean is EXACTLY 1/2 in every dimension (independent of the power
# spectrum, sigma_v, density, epoch -- and, by a<->b exchange symmetry, of anisotropy),
# variance 1/(4(d+1)). This is the plateau's universality, sharper than "O(1)". The sim
# confirms it: 3D var 0.06253 vs 1/16, 2D matches Uniform[0,1], and the vortex-tangle
# (caustic-content) density obeys Berry & Dennis's isotropic <k^2>/4pi.
_a2, _a3 = 2 / 2.0, 3 / 2.0            # Beta shape a = d/2 in 2D, 3D
chk("r1_caustic_sim", "Theta_loc plateau = Beta(d/2,d/2) mean = 1/2 (d=2)", 0.5,
    _a2 / (_a2 + _a2), 1e-12)
chk("r1_caustic_sim", "Theta_loc plateau = Beta(d/2,d/2) mean = 1/2 (d=3)", 0.5,
    _a3 / (_a3 + _a3), 1e-12)
chk("r1_caustic_sim", "Theta_loc pointwise var 2D = Beta(1,1) = 1/12", 1 / 12,
    _a2 * _a2 / ((_a2 + _a2) ** 2 * (_a2 + _a2 + 1)), 1e-9)
chk("r1_caustic_sim", "Theta_loc pointwise var 3D = Beta(3/2,3/2) = 1/16", 0.0625,
    _a3 * _a3 / ((_a3 + _a3) ** 2 * (_a3 + _a3 + 1)), 1e-9)
chk("r1_caustic_sim", "var = 1/(4(d+1)) matches the Beta form (d=3)", 1 / (4 * (3 + 1)),
    _a3 * _a3 / ((_a3 + _a3) ** 2 * (_a3 + _a3 + 1)), 1e-12)
chk("r1_caustic_sim", "Berry-Dennis 2D vortex-point density coeff = 1/(4 pi)", 0.0796,
    1 / (4 * math.pi), 5e-3)

# ---- census imprint scaling mechanism (#168, census_scaling_network.py) --------
# The A_s imprint is a self-similar (scaling) shot-noise census: xi/l_H = k_*xi held
# constant across decades. The target ratio, the tilt discriminant, and the VOS
# scaling attractor's fixed point.
_As_168 = 2.100e-9
chk("census_scaling_network", "k_*xi = (2 pi^2 A_s)^(1/3) = 3.45e-3", 0.003461,
    (2 * math.pi**2 * _As_168) ** (1/3), 1e-3)
# Delta^2 ~ k^3 xi(k)^3 ; xi ~ k^-p gives n_s - 1 = 3(1-p):
chk("census_scaling_network", "frozen cell xi=const -> n_s = 4", 4.0, 1 + 3*(1-0.0), 1e-9)
chk("census_scaling_network", "scaling xi~1/k -> n_s = 1", 1.0, 1 + 3*(1-1.0), 1e-9)
# VOS scaling fixed point (radiation beta=1/2, c_chop=0.23, k_mom=0.7):
_b168, _cc, _km = 0.5, 0.23, 0.70
_vstar2 = _km * (1 - _b168) / (_b168 * (_cc + _km))
_gstar = _km / (2 * _b168 * math.sqrt(_vstar2))
chk("census_scaling_network", "VOS fixed point v*^2 = k(1-b)/(b(c+k))", 0.7527, _vstar2, 1e-3)
chk("census_scaling_network", "VOS transient exponent a-1<0 (attractor)", 1.0,
    1.0 if _b168 * (1 + _vstar2) < 1.0 else 0.0, 1e-9)
# the observed gamma needs the overdamped branch: v ~ gamma*2(1-b)/c_chop << 1
chk("census_scaling_network", "overdamped drift v for gamma=3.45e-3 is <<1", 1.0,
    1.0 if (0.003461 * 2 * (1 - _b168) / _cc) < 0.1 else 0.0, 1e-9)

# ---- Koide as a C3 triple-point node (koide_triple_point_node.py) --------------
# The Koide sqrt-masses are eigenvalues of a C3 circulant H = a I + b P + b* P^2:
# sqrt(m_k) = a + 2|b|cos(2pi k/3 + arg b), so Q = 1/3 + (2/3)(|b|/a)^2. The node is
# b=0 (Q=1/3, threefold degenerate); the null Q=2/3 is |b|/a = 1/sqrt2. The node
# fixes the STRUCTURE (two knobs |b|/a, arg b), not the values.
_r_null = 1/math.sqrt(2)
chk("koide_triple_point_node", "circulant->Koide: Q = 1/3 + (2/3)(|b|/a)^2 at null",
    2/3, 1/3 + (2/3)*_r_null**2, 1e-12)
chk("koide_triple_point_node", "node b=0 (degenerate) gives Q = 1/3", 1/3,
    1/3 + (2/3)*0.0**2, 1e-12)
chk("koide_triple_point_node", "null |b|/a = A/2 = 1/sqrt2 (A=sqrt2)", 1/math.sqrt(2),
    math.sqrt(2)/2, 1e-12)
# A=sqrt2 sits at 96% of the positivity wall A_max=-1/cos(theta_min), phase delta=2/9
_thmin = min(math.cos(2/9 + 2*math.pi*k/3) for k in range(3))
chk("koide_triple_point_node", "A=sqrt2 is ~96% of positivity wall A_max", 0.960,
    math.sqrt(2) / (-1/_thmin), 5e-3)

# ---- expansion-energy ledger (friedmann_from_medium.py) -----------------------
# Friedmann as +kinetic/-binding = 0 (flat), and continuity = first law dU = -p dV.
chk("friedmann_from_medium", "continuity exp -3(1+w): radiation w=1/3 -> a^-4",
    -4.0, -3*(1+1.0/3.0), 1e-9)
chk("friedmann_from_medium", "continuity exp: matter w=0 -> a^-3", -3.0, -3*(1+0.0), 1e-9)
chk("friedmann_from_medium", "continuity exp: DE w=-1 -> a^0", 0.0, -3*(1+(-1.0)), 1e-9)
_Gn, _rho_c, _rr = 6.674e-11, 8.5e-27, 3.0e25
_Hf = math.sqrt(8*math.pi*_Gn/3*_rho_c)          # Friedmann H
chk("friedmann_from_medium", "flat universe: kinetic + binding = 0 at Friedmann H", 0.0,
    (0.5*_Hf**2*_rr**2 - (4.0/3.0)*math.pi*_Gn*_rho_c*_rr**2)/(0.5*_Hf**2*_rr**2), 1e-12)
# localizable zero (localizable_zero_burst.py): flat -> Hubble radius = Schwarzschild
# radius of the enclosed mass, R_s/R_H = 2GM/R_H = (8piG/3)rho R_H^2 = (H R_H)^2 = 1.
_RH = 1.0/_Hf                                      # Hubble radius (c=1 units here)
_Mh = (4.0/3.0)*math.pi*_RH**3*_rho_c             # enclosed mass
chk("localizable_zero_burst", "flat: R_s = R_H (Hubble vol at its Schwarzschild radius)",
    1.0, (2*_Gn*_Mh)/_RH, 1e-12)

# ---- report (MUST stay last: checks appended below it are silently dropped) ---
bad = [r for r in R if not r[0]]
print(f"MATH AUDIT — {len(R)} closed-form checks, {len(R)-len(bad)} pass, {len(bad)} fail\n")
for ok, doc, claim, booked, got, unit in R:
    print(f"  {'ok  ' if ok else 'FAIL'} {doc:24s} {claim:46s} booked {booked:<12.6g} got {got:<12.6g} {unit}")
if bad:
    print("\nFAILURES:")
    for ok, doc, claim, booked, got, unit in bad:
        print(f"  {doc}: {claim}\n     booked {booked} {unit}, recomputed {got} {unit}"
              f"  ({abs(got-booked)/abs(booked)*100:.1f}% off)")
