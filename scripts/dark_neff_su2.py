#!/usr/bin/env python3
"""
dark_neff_su2.py

Re-price Delta N_eff with the dark colour group FIXED by the finiteness balance
(P-2026-048): dark SU(2) with N_f = 3 light Dirac flavours in the fundamental.

The predecessor (dark_neff.py) scanned g_dark = 2, 4, 8 generically because the roster
was unknown. It is no longer unknown, and the count is not a free scan any more.

THE COUNTING, AND WHY SU(2) IS NOT SU(3):
  SU(N_c >= 3), N_f flavours : SU(N_f)_L x SU(N_f)_R -> SU(N_f)_V
                               Goldstones = N_f^2 - 1          (N_f=3 -> 8)
  SU(2) is PSEUDO-REAL       : the chiral symmetry ENLARGES to SU(2 N_f) -> Sp(2 N_f)
                               Goldstones = 2 N_f^2 - N_f - 1  (N_f=3 -> 14)
The same pseudo-reality that supplies P-048's consilience (bosonic diquark baryons ->
the BEC side, the scalar/s-wave channel, no fermionic hard core) ALSO enlarges the
Goldstone multiplet from 8 to 14. The structural fact cuts both ways.

Thermal history (unchanged from the predecessor):
    T_dark/T_nu = [ g*s(SM, T_nu ~ 2 MeV) / g*s(SM, T_dec) ]^(1/3)
    Delta N_eff = (4/7) * g_dark * (T_dark/T_nu)^4
Observational context: Planck N_eff = 2.99 +/- 0.17 (Delta N_eff < ~0.3 at 2sigma);
CMB-S4 forecast +/-0.03.
"""

def goldstones_pseudoreal(nf):      # SU(2): dim SU(2Nf) - dim Sp(2Nf)
    return (4 * nf**2 - 1) - nf * (2 * nf + 1)

def goldstones_complex(nf):         # SU(Nc>=3): SU(Nf)_L x SU(Nf)_R -> SU(Nf)_V
    return nf**2 - 1

g_nu = 10.75
g_star = {
    "T_dec > 200 GeV (all SM active)": 106.75,
    "T_dec ~ 1 GeV (above QCD)":        61.75,
    "T_dec ~ 150 MeV (QCD region)":     17.00,
    "T_dec ~ 20 MeV (below QCD)":       10.75,
}
PLANCK_2SIG = 0.30

nf = 3
g_su2 = goldstones_pseudoreal(nf)   # 14
g_su3 = goldstones_complex(nf)      # 8

print("Delta N_eff re-priced at the finiteness-selected roster: dark SU(2), N_f = 3")
print("=" * 78)
print(f"  Goldstone multiplet, SU(2) pseudo-real  SU(6) -> Sp(6) : {g_su2}")
print(f"  Goldstone multiplet, an SU(3) sector    (for contrast) : {g_su3}")
print(f"  penalty factor from pseudo-reality                     : {g_su2/g_su3:.2f}x")
print(f"  (the old script's scan ceiling was g = 8 -- BELOW the actual count)")
print()
print(f"{'decoupling':<34}{'(Td/Tnu)^4':>11}{'g=8 (SU3)':>11}{'g=14 (SU2)':>12}  verdict (SU2)")
for label, gs in g_star.items():
    r4 = (g_nu / gs) ** (4 / 3)
    d3 = (4 / 7) * g_su3 * r4
    d2 = (4 / 7) * g_su2 * r4
    verdict = "OK" if d2 < PLANCK_2SIG else "EXCLUDED by Planck"
    print(f"{label:<34}{r4:>11.4f}{d3:>11.3f}{d2:>12.3f}  {verdict}")

print()
r4_best = (g_nu / 106.75) ** (4 / 3)
d2_best = (4 / 7) * g_su2 * r4_best
print(f"  BEST CASE for SU(2) (earliest possible decoupling, all SM active):")
print(f"    Delta N_eff = {d2_best:.3f}  vs Planck's ~{PLANCK_2SIG} (2sigma)  -> {'EXCLUDED' if d2_best>PLANCK_2SIG else 'survives'}")
print()
g_max = PLANCK_2SIG / ((4 / 7) * r4_best)
print(f"  INVERT: the largest g_dark Planck allows even at earliest decoupling = {g_max:.1f}")
print(f"    SU(2) N_f=3 needs {g_su2}. An SU(3) sector would need {g_su3}. ")
print(f"    -> a MASSLESS SU(2) Goldstone multiplet does not fit, at ANY decoupling temperature.")
print()
print("  The CMB escape would be that the 14 are PSEUDO-Goldstones, non-relativistic by")
print("  recombination (T ~ 0.3 eV) and annihilated away as the roster already says its dark")
print("  hadrons are. But that escape does not reach BBN:")
print()
print("=" * 78)
print("WHERE IT ACTUALLY BITES: BBN -- AND AT THE DECONFINED COUNT, NOT THE GOLDSTONES")
print("=" * 78)
LAMBDA_DARK = 511.0   # keV; sqrt(sigma_dark) = m_e, the portal
T_C         = 179.0   # keV; the dark chiral/deconfinement temperature (tau * m_e)
T_FREEZE    = 700.0   # keV; n/p freeze-out
print("  RAMP AUDIT (snag protocol 5a) -- a first draft of this script priced BBN with the")
print("  14 CONFINED Goldstones. That was a PHASE ERROR, not merely a step:")
print(f"    n/p freeze-out T ~ {T_FREEZE:.0f} keV  vs  T_c = {T_C:.0f} keV  ->  T/T_c = {T_FREEZE/T_C:.1f}")
print("    The dark sector is DECONFINED at freeze-out. The Goldstones DO NOT EXIST yet.")
print("    The correct dof there are dark QUARKS + GLUONS.")
print()
g_gluon = 2 * (2**2 - 1)                 # 2 polarizations x (Nc^2-1), Nc=2
g_quark = (7 / 8) * 2 * 2 * 2 * nf       # 7/8 x spin(2) x particle/anti(2) x Nc(2) x Nf
g_deconf = g_gluon + g_quark
print(f"    DECONFINED (T > T_c): gluons {g_gluon} + quarks {g_quark:.0f} = {g_deconf:.0f} dof")
print(f"    CONFINED   (T < T_c): {g_su2} Goldstones")
print(f"    -> BBN must be priced at g = {g_deconf:.0f}, not {g_su2}. The first draft UNDER-counted.")
print()
dN_bbn = (4 / 7) * g_deconf * r4_best
dYp_per_dN = 0.013
sig_Yp = 0.004
dYp = dYp_per_dN * dN_bbn
print(f"  Delta N_eff at n/p freeze-out (best-case earliest decoupling) = {dN_bbn:.3f}")
print()
print("  Can the Boltzmann ramp rescue it? Only if the dark quarks are heavy -- and tau")
print("  REQUIRES them light (heavy quarks drive T_c/sqrt(sigma) toward the pure-glue")
print("  0.69-0.71 and break P-048's own claim). At T = 700 keV a 100 keV quark is")
print("  suppressed by rho/rho_0 = 0.997. The ramp does NOT rescue it.")
print()
print(f"  BBN price:  dY_p/dN_eff ~ {dYp_per_dN}  ->  Delta Y_p = {dYp:.4f}")
print(f"              sigma(Y_p) ~ {sig_Yp}        ->  {dYp/sig_Yp:+.1f} sigma of ADDITIONAL Y_p")
print(f"  The model already carries Y_p at +1.3 sigma ADVERSE (the owned BBN scar). Extra")
print(f"  relativistic dof speed the expansion -> earlier freeze-out -> more neutrons ->")
print(f"  HIGHER Y_p. The sign is wrong: it drives the weakest row further adverse.")
print(f"      +1.3 sigma  ->  ~{1.3 + dYp/sig_Yp:+.1f} sigma")
print()
print("  VERDICT (termination-B: the failure is lawful and bookable): P-2026-048's roster")
print("  REQUIRES the dark sector to have NEVER THERMALISED with the SM. Thermalised, it")
print(f"  drives Y_p to ~{1.3 + dYp/sig_Yp:.1f} sigma adverse -- in the model's already-weakest row.")
print("  Non-thermalised, Delta N_eff -> 0 and the roster survives, at the price of a hard")
print("  upper bound on the portal coupling. CMB-S4 (+/-0.03) tests it either way.")
print("  The old g=2..8 scan could not see this: it never contained the right number, in")
print("  either phase.")
