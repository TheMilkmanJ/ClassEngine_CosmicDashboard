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
print("WHERE IT ACTUALLY BITES: BBN, NOT THE CMB")
print("=" * 78)
LAMBDA_DARK = 511.0   # keV; sqrt(sigma_dark) = m_e, the portal
T_FREEZE    = 700.0   # keV; n/p freeze-out
print("  A pseudo-Goldstone is LIGHTER than its own confinement scale, by construction:")
print(f"    m_pi_dark < sqrt(sigma_dark) = m_e = {LAMBDA_DARK:.0f} keV")
print("  And tau REQUIRES light dark quarks (the 0.34-0.37 chiral ratio; heavy quarks drive")
print("  T_c/sqrt(sigma) back toward the pure-glue 0.69-0.71). GMOR m_pi^2 ~ m_q*Lambda then")
print("  makes them lighter still. So the model cannot buy safety by making them heavy --")
print("  tau is spending exactly the lightness that Delta N_eff needs it not to spend.")
print()
print(f"    n/p freeze-out at T ~ {T_FREEZE:.0f} keV  >  {LAMBDA_DARK:.0f} keV  >  m_pi_dark")
print("    => THE DARK PIONS ARE RELATIVISTIC AT FREEZE-OUT.")
print("    They may be non-relativistic by the CMB -- but they are radiation exactly when")
print("    BBN is counting radiation.")
print()
dYp_per_dN = 0.013
sig_Yp = 0.004
dYp = dYp_per_dN * d2_best
print(f"  BBN price:  dY_p/dN_eff ~ {dYp_per_dN}  ->  Delta Y_p = {dYp:.4f}")
print(f"              sigma(Y_p) ~ {sig_Yp}        ->  {dYp/sig_Yp:+.1f} sigma of ADDITIONAL Y_p")
print(f"  The model already carries Y_p at +1.3 sigma ADVERSE (the owned BBN scar). Extra")
print(f"  relativistic dof speed the expansion -> earlier freeze-out -> more neutrons ->")
print(f"  HIGHER Y_p. The sign is wrong: it drives the weakest row further adverse.")
print(f"      +1.3 sigma  ->  ~{1.3 + dYp/sig_Yp:+.1f} sigma")
print()
print("  VERDICT: P-2026-048's SU(2) roster REQUIRES the dark sector to have NEVER")
print("  THERMALISED with the SM. Thermalised, its 14 Goldstones are relativistic at n/p")
print("  freeze-out and push Y_p to ~2.5 sigma adverse -- near-fatal, and adverse in the")
print("  model's already-weakest row. Non-thermalised, Delta N_eff -> 0 and the roster")
print("  survives, but the portal coupling now carries a hard upper bound it did not have.")
print("  This constraint is NEW and is created by fixing the colour group. The old g=2..8")
print("  scan could not see it: it never contained the number 14.")
