#!/usr/bin/env python3
"""
Chase: is zeta = T_dark/T_gamma set by the cyclic FIXED POINT (JP's "future" route)?
Read the cycle map -- what one full loop (pour -> expand -> now -> recollapse ->
crunch -> next pour) does to zeta.

Each bath conserves its OWN comoving entropy (the two are decoupled, Gamma/H ~ 3e-7):
s ~ g*S T^3 a^3 = const  =>  T ~ g*S^(-1/3) / a. Hence
    zeta = T_dark/T_gamma ~ (g*S_SM / g*S_dark)^(1/3) x (a constant fixed at the pour).
zeta moves only when a g*S changes (SM species annihilate; the dark sector confines).
Over a cycle, zeta returns to its pour value IFF the CRUNCH reheats hot enough to
restore every dof the expansion dropped -- the map is then the IDENTITY (zeta conserved).
"""
r = lambda gSM, gD: (gSM/gD)**(1.0/3.0)      # zeta ~ this, up to the pour constant

POUR = (106.75, 27.0)     # pour: all SM active, dark deconfined (27 dof)
NOW  = (3.91,   14.0)     # today: post e+e- (g*S=3.91), dark confined (14 Goldstones)

print("Cycle map for zeta = T_dark/T_gamma   (zeta ~ (g*S_SM/g*S_dark)^(1/3))")
print("=" * 70)
for label, CRUNCH in [
        ("HOT crunch ~Psi0 = 1e17 GeV  (full restoration)", (106.75, 27.0)),
        ("warm crunch ~1 GeV  (SM back, dark deconfined)",   (61.75, 27.0)),
        ("cold crunch ~few MeV (e+e- back, dark confined)",  (10.75, 14.0))]:
    f = r(*CRUNCH) / r(*POUR)     # zeta_crunch / zeta_pour over the full loop
    tag = "IDENTITY  -> zeta CONSERVED" if abs(f-1) < 1e-9 else "drift"
    print(f"  {label:48s} zeta_crunch/zeta_pour = {f:.3f}   {tag}")
print("=" * 70)
print("  The model's reheat Psi0 ~ 1e17 GeV sits ~15 orders above every threshold,")
print("  so the crunch is HOT: the contraction exactly UNDOES the expansion's entropy")
print("  processing, the map is the IDENTITY, and zeta is a CONSERVED quantity of the cycle.")
print()
print("  => zeta is NOT a free inheritance from 'the last cycle'. It is carried unchanged,")
print("     cycle after cycle, back to the FIRST genesis -- the roll from the UNIQUE vacuum")
print("     'that carries no information' (no free choice). A constant of motion, not a bet.")
print()
print("  Correction (the true fixed point): the identity is the ADIABATIC limit. Real 2nd-law")
print("  entropy production -- asymmetric between the dark and visible sectors -- drifts zeta")
print("  slowly toward an ATTRACTOR set by the per-cycle entropy budget. That attractor is the")
print("  genuine cyclic fixed point, and it is a computable number, not an initial condition.")
