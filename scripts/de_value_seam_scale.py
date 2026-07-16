import numpy as np
alpha=1/137.035999; me=510998.95; pi=np.pi
alpha_c=3*alpha
obs=2.25e-3  # eV
M2_model=9.39  # eV (the model's selected condensate EFT scale)

# The occupancy floor: E_b = 1/2 alpha_c^2 M2.  Question: what SETS M2?
# The seam = dyad(dCDF) meeting. Candidate BASE scales the seam could bring:
scales = {
 "electron rest mass m_e":        me,             # dyad's fundamental coupling is to m_e
 "dyad VEV v (~100 keV)":         1.0e5,
 "dyad condensation T_c (193keV)":1.93e5,          # the dyad's OWN scale (its condensation)
}
print("If M2 = (base scale) directly:  E_b = 1/2 a_c^2 * base")
for k,S in scales.items():
    Eb=0.5*alpha_c**2*S
    print(f"   base={k:32s}: M2={S:.3e} eV -> E_b={Eb*1e3:.2e} meV   ({Eb/obs:.1e}x)  [{'TOO BIG' if Eb>10*obs else 'ok'}]")

print("\n=> all bases give E_b ~10-100 eV, ~4-5 orders TOO BIG. M2 needs an EXTRA suppression ~alpha^2.")
print("   The dyad's coupling to matter is ELECTROMAGNETIC/atomic -> the natural extra factor is alpha^2.\n")

print("If M2 = alpha^2 * (base scale)  [the dyad brings an EM/atomic alpha^2 to the seam]:")
for k,S in scales.items():
    M2=alpha**2*S; Eb=0.5*alpha_c**2*M2   # = (9/2) alpha^4 * S
    print(f"   base={k:32s}: M2={M2:.2f} eV -> E_b={Eb*1e3:.3f} meV   ({Eb/obs:.3f}x obs)")

# what base gives EXACTLY 2.25 meV with the alpha^2 suppression?
S_need = obs/(4.5*alpha**4)
print(f"\n=> E_b = (9/2) alpha^4 * S.  Exact 2.25 meV needs base S = {S_need/1e3:.1f} keV")
print(f"   T_c band is [40,900] keV, central 193 -> S=176 keV sits INSIDE, near central.")
print(f"   M2 = alpha^2 * T_c(193keV) = {alpha**2*1.93e5:.2f} eV  vs model's selected {M2_model} eV (ratio {alpha**2*1.93e5/M2_model:.2f})")
print(f"\nSEAM VERDICT: base scale = the DYAD condensation scale T_c; suppression = alpha^4 (=a_c^2 binding x a^2 atomic).")
print(f"   E_b(T_c=193keV) = {4.5*alpha**4*1.93e5*1e3:.2f} meV (1.09x); exact at T_c=176 keV (in band).")
print(f"   Confirms cosmo_const 2e DOUBLE suppression. Soft: the a^2 factor is plausible-not-derived; T_c has a log-band.")
