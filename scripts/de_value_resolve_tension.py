import numpy as np
me=510998.95; keV=1e3
eps=0.012543  # varying-m_e amplitude (fit, H0 mechanism) -- the ONLY observable of the dyad VEV sector
BCS=0.567     # T_c/Delta(0) = e^gamma/pi

print("=== Is the perturbative dyad estimate even internally consistent? ===")
v_pert=100*keV; Tc=193*keV
print(f"   perturbative CW: v={v_pert/keV:.0f} keV, T_c={Tc/keV:.0f} keV  ->  T_c/v = {Tc/v_pert:.2f}")
print(f"   BUT for a condensate T_c < VEV (T_c/Delta(0)={BCS}). Perturbative gives T_c/v={Tc/v_pert:.2f} > 1 -- UNPHYSICAL.")
print(f"   => the perturbative v=100 keV is INCONSISTENT with its own T_c (and it's ill-defined, entry 215).")

print("\n=== The gap equation's CONSISTENT VEV ===")
v_gap=Tc/BCS
print(f"   gap-consistent: Delta(0)=v_gap = T_c/{BCS} = {v_gap/keV:.0f} keV,  T_c/v_gap = {BCS} (correct BCS) [CONSISTENT]")
print(f"   ratio v_gap/v_pert = {v_gap/v_pert:.2f}  <- 'the factor 3'")

print("\n=== Does revising v break the H0 mechanism? Only eps=kappa v^2 is observable. ===")
kappa_pert = eps/v_pert**2
kappa_gap  = eps/v_gap**2
print(f"   eps = kappa v^2 = 1.2543% (FIT). Revising v -> re-fit kappa (a free coupling):")
print(f"     kappa_pert = {kappa_pert:.3e} eV^-2  (v=100 keV)")
print(f"     kappa_gap  = {kappa_gap:.3e} eV^-2  (v={v_gap/keV:.0f} keV)  -> kappa down by {kappa_pert/kappa_gap:.1f}x")
print(f"   eps check with v_gap: eps = kappa_gap*v_gap^2 = {kappa_gap*v_gap**2*100:.4f}%  (preserved)")
print(f"   T_c window unchanged (~185-193 keV). Only the internal split (v,kappa) moves; the OBSERVABLE eps holds.")
print("   => NO observable breaks. The 'tension' DISSOLVES: the gap equation CORRECTS the inconsistent")
print("      perturbative VEV upward to the BCS-consistent value; eps=1.24% preserved by re-fitting kappa.")

print("\n=== Is 'the 3' the model's structural 3 (d=3, alpha_c=3alpha)? Honest check. ===")
print(f"   the ratio = 1/BCS = 1/{BCS} = {1/BCS:.2f}  = pi/e^gamma (the BCS gap ratio) -- NOT the spatial d=3.")
print("   It is a coincidence: pi/e^gamma = 1.76 x (T_c/v_pert normalization). The model's REAL 3 (d=3 via")
print("   second sound, alpha_c=3alpha) is derived and separate. This 3 is a BCS-ratio artifact. Don't force it.")
