import numpy as np
alpha=1/137.035999; me=510998.95; keV=1e3
alpha_c=3*alpha
g_crit=2.0  # NJL critical coupling for condensation

print("=== The medium/dyad needs g_p ~ 2.8 (strong, > g_c=2) to condense at tau=T_c/m_e~0.34. ===")
print("    Write down EVERY fundamental interaction the model contains, compute the pairing g_p each gives:\n")

# 1. EM (photon exchange between the constituents)
print("  (1) EM photon exchange: alpha=1/137. Between like charges it is REPULSIVE -> does not pair.")
print(f"      Even taken attractive: g ~ 4 alpha/pi^2 = {4*alpha/np.pi**2:.4f}  << 2")

# 2. Dark condensate coupling alpha_c = 3 alpha
print(f"  (2) Dark coupling alpha_c=3alpha: g ~ 4 alpha_c/pi^2 = {4*alpha_c/np.pi**2:.4f}  << 2")

# 3. Majoron exchange (the dyad's own sigma-N-N coupling), g_Maj ~ 1.2e-8 (Card 6)
gMaj=1.2e-8
print(f"  (3) Majoron exchange g_Maj~1.2e-8: g ~ N g_Maj^2/pi^2 ~ {4*gMaj**2/np.pi**2:.1e}  << 2")

# 4. The dyad-electron coupling kappa itself, FIT to eps=1.24% (the varying-m_e).
eps=0.012543; v=340*keV  # BCS-consistent VEV (hunt 218)
kappa=eps/v**2            # eV^-2
mdyad=340*keV
g_kappa=4*kappa**2*me**4/(np.pi**2*mdyad**2)  # dyad-exchange 4-electron coupling -> NJL g
print(f"  (4) eps-fitted kappa={kappa:.2e} eV^-2 (from eps=1.24%): the SAME coupling that sets varying-m_e")
print(f"      -> dyad-exchange pairing g ~ N kappa^2 m_e^4/(pi^2 m_dyad^2) = {g_kappa:.1e}  << 2")

print("\n=== ALL of the model's interactions are WEAK (g << g_c=2), by 2 to 15 orders. ===")
print("    The strong g_p~2.8 the DE value needs is supplied by NONE of them.")

print("\n=== The framings, and why tau is not derivable in ANY of them ===")
print("  - Composite (NJL/BCS, what we built): needs strong g_p~2.8; NO model coupling supplies it")
print("    -> requires a NEW strong pairing sector, absent from the corpus.")
print("  - Fundamental scalar (tree potential): tau = (dyad bare mass)/m_e -> a FREE parameter, not derived.")
print("  - Radiative CW (the model's stated mechanism, weak eps-kappa): ill-defined/marginal (hunt 215),")
print("    and the eps-fitted kappa gives g~1e-15 -- nowhere near condensation.")

print("\n=== VERDICT (the honest foundation) ===")
print("Writing down the medium's fundamental interaction shows the model has NO strong sector: every")
print("coupling (alpha, alpha_c, Majoron, the eps-fit kappa) is weak. So g_p ~ 2.8 -- hence tau, hence the")
print("DE-value digit -- is NOT derivable from the existing content. It is either a FREE parameter (if the")
print("dyad is a fundamental scalar) or needs NEW strong physics (if it is a composite). This is a genuine")
print("GAP in the model's foundation: the medium's strong condensation is ASSUMED, not sourced by any")
print("specified interaction. The DE value stands at (d/2)alpha^4 m_e (0.966x, conjecture tau=1/d); its")
print("digit rests on physics the model does not yet contain -- an honest open foundation, not a computation.")
