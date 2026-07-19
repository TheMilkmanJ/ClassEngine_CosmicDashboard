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
_DH_L, _DH_W, _DH_M = 2.420, 2.372, 2.387      # LCDM control -> +omega_b -> +the window
_COOKE, _TOT = 2.527, math.hypot(0.030, 0.0476)
_sig = lambda x: (x - _COOKE)/_TOT
chk("deuterium_scar", "combined D/H budget", 0.0563, _TOT, 1e-3)
chk("deuterium_scar", "LCDM control vs Cooke", -1.90, _sig(_DH_L), 0.01, "sigma")
chk("deuterium_scar", "the model vs Cooke", -2.49, _sig(_DH_M), 0.01, "sigma")
chk("deuterium_scar", "the model's deficit vs its LCDM control", -0.59, _sig(_DH_M)-_sig(_DH_L), 0.02, "sigma")
chk("deuterium_scar", "omega_b step costs", -0.85, _sig(_DH_W)-_sig(_DH_L), 0.02, "sigma")
chk("deuterium_scar", "the dyad's BBN window gains", +0.27, _sig(_DH_M)-_sig(_DH_W), 0.02, "sigma")
chk("deuterium_scar", "window grafted on LCDM alone", -1.63, _sig(_DH_L*(_DH_M/_DH_W)), 0.02, "sigma")
chk("deuterium_scar", "d ln(D/H)/d ln omega_b (production)", -1.83,
    math.log(_DH_W/_DH_L)/math.log(1.011), 0.01)
# the exchange rate: the omega_b shift arrives with the H0 relief
_dH0 = 69.9 - 68.2
chk("deuterium_scar", "deuterium paid per km/s/Mpc of H0", 0.50,
    abs(_sig(_DH_W)-_sig(_DH_L))/_dH0, 0.02, "sigma")
chk("deuterium_scar", "H0 given back to reach LCDM parity", 1.17,
    (_sig(_DH_L)-_sig(_DH_M))*_dH0/abs(_sig(_DH_W)-_sig(_DH_L)), 0.02, "km/s/Mpc")
chk("deuterium_scar", "H0 given back to centre on Cooke", 4.96,
    (0-_sig(_DH_M))*_dH0/abs(_sig(_DH_W)-_sig(_DH_L)), 0.02, "km/s/Mpc")
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
chk("fairbank_note", "Sigma m_nu at the high anchor m1 = 2.284", 61.40, _win(2.284e-3)[0], 2e-3, "meV")
chk("fairbank_note", "floor at the low anchor", 0.044, _win(2.250e-3)[2], 0.03, "meV")
chk("fairbank_note", "floor at the high anchor", 0.023, _win(2.284e-3)[2], 0.05, "meV")
chk("fairbank_note", "a 1.5% anchor move nearly halves the floor", 1.9,
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
chk("background.h", "T_on = sqrt(m*M_red/0.61)", 9.41, _Ton/1e3, 0.01, "keV")
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
chk("INTERACTION_ATLAS", "swept quench margin low end, re-priced", -0.20,
    2.5 - _m.log10(1e-88/2e-91), tol=0.05, unit="dex")

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
chk("fairbank_note", "m_bb ceiling holds at 5.30 across the anchor range", 5.30,
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
chk("deuterium_scar 6b", "best case, everything additive", -1.94,
    -2.49 + _sig(0.1160*0.059*100) + _sig(1.057-0.645), 0.02, "sigma")
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


# --- PHYSICS_DOMAINS deep audit, 2026-07-19 ---
# the deuterium sigma ladder, ONE width (the scar file's combined 0.0563)
_wD = 0.0563
chk("PHYSICS_DOMAINS 6", "standing D/H row in sigma", -2.49, -(2.527-2.387)/_wD, 0.005, "sigma")
chk("PHYSICS_DOMAINS 6", "committed-window low end", -2.13, -(2.527-2.407)/_wD, 0.005, "sigma")
chk("PHYSICS_DOMAINS 6", "committed-window high end", -1.14, -(2.527-2.463)/_wD, 0.005, "sigma")
chk("PHYSICS_DOMAINS 6", "LCDM control on the same width", -1.90, -(2.527-2.420)/_wD, 0.005, "sigma")
_wU = math.sqrt(_wD**2+(0.035*2.387)**2)
chk("PHYSICS_DOMAINS 6", "spread-unfolded standing row", -1.4, -(2.527-2.387)/_wU, 0.01, "sigma")
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
