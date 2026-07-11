#!/usr/bin/env python3
"""
#16 SWING: the c-m degeneracy + the UFD tension on trial.
The amplitude fixes a COMBINATION of c and the field mass m, not either alone:
    eps = c * f_amp * Psi0(m)/M_red ,   with abundance pinning Psi0 ∝ m^(-1/4)
=> at fixed observed eps:  c(m) = c_ref * (m/m_ref)^(1/4)   (higher m needs higher c)
Fuzzy-DM astro measures m INDEPENDENTLY (core sizes, Lyman-a, ultra-faint dwarfs).
So an independent m -> pins c. Question: do the fuzzy-DM mass bounds leave c NATURAL?
"""
import numpy as np
m_ref  = 2.0e-20   # eV, the model's amplitude+abundance pin
c_ref  = 0.974     # c at m_ref (from the #11 assembly, central eps)

def c_of_m(m):  # degeneracy line: Psi0 ∝ m^-1/4 at fixed abundance & eps
    return c_ref * (m/m_ref)**0.25

# fuzzy-DM mass landmarks (eV)
bounds = [
  ("model pin (amp+abundance)", 2.0e-20),
  ("Lyman-alpha lower bound",   2.0e-20),
  ("UFD Dalal-Kravtsov bound",  3.0e-19),   # the tension
  ("if pushed to CDM-like",     1.0e-18),
]
print("="*66); print("#16: c-m degeneracy -- does the fuzzy-DM mass keep c natural?"); print("="*66)
print(f"\n  degeneracy line:  c(m) = {c_ref:.3f} * (m / {m_ref:.0e} eV)^(1/4)\n")
print(f"  {'landmark':<30}{'m (eV)':>10}{'-> c':>8}   naturalness")
print("  "+"-"*58)
for name,m in bounds:
    c = c_of_m(m)
    nat = "comfortable" if c<1.5 else ("edge of O(1)" if c<2.5 else ("strained" if c<4 else "UNNATURAL"))
    print(f"  {name:<30}{m:>10.1e}{c:>8.2f}   {nat}")

# where does c break naturalness?
for cmax in [2.0, 3.0, 4.0]:
    m_break = m_ref*(cmax/c_ref)**4
    print(f"\n  c reaches {cmax:.0f} at  m = {m_break:.1e} eV")
print("\n" + "-"*66)
print("VERDICT ON THE UFD TENSION:")
c_ufd = c_of_m(3.0e-19)
print(f"  If UFD wins (m~3e-19), the model ABSORBS it by setting c = {c_ufd:.2f}.")
print(f"  That is still O(1) and 'natural' -- so the UFD tension is SURVIVABLE, NOT a kill.")
print(f"  Cost: it spends c's naturalness margin (0.97 -> 1.9, toward the edge).")
print(f"  And c is pinned only as tightly as m is measured: m in [2e-20, 3e-19]")
print(f"  => c in [{c_of_m(2e-20):.2f}, {c_of_m(3e-19):.2f}]. A RANGE, consistent w/ natural,")
print(f"  not yet a sharp value. #16 gives c to a factor ~2, bounded by the mass data.")
print("="*66)
