#!/usr/bin/env python3
"""
Turn the committed dark-radiation window into a thermal-history number.
The dark radiation is DeltaN_eff = (27/(7/4)) * zeta^4, zeta = T_dark/T_gamma.
The committed window zeta in [0.25, 0.35] -> DeltaN_eff 0.06-0.24 is currently an
INPUT. But zeta is fixed once the superplasma decouples from the SM: after that the
SM bath is reheated every time an SM species annihilates (g*S drops from 106.75 to
3.91), while the decoupled dark plasma just coasts. So

    zeta(T_dec) = [ g*S_SM(T_eval) / g*S_SM(T_dec) ]^(1/3)     (dark dof constant)

This asks: what decoupling temperature reproduces the committed zeta window, i.e.
does JP's "it cooled off after the pour" pin the number that heals deuterium?
"""
import numpy as np

# SM entropy dof g*S(T), standard milestones (GeV, g*S)
TAB = [(3e-4,3.91),(1e-2,10.75),(0.10,17.25),(0.20,47.5),(1.0,61.75),
       (4.0,75.75),(1e2,96.25),(2e2,106.75),(1e7,106.75)]
def gS(T):
    T=max(T,TAB[0][0])
    g=TAB[0][1]
    for Ti,gi in TAB:
        if T>=Ti: g=gi
    return g

def zeta(T_dec, T_eval): return (gS(T_eval)/gS(T_dec))**(1.0/3.0)
def dNeff(z): return (27.0/(7.0/4.0))*z**4

# DeltaN_eff is a LATE quantity (CMB/deuterium epoch, after e+e-): g*S_SM = 3.91.
ev = {"late / CMB-deuterium epoch (g*S=3.91)": 7e-5}

print("="*70)
print("zeta and DeltaN_eff vs where the superplasma decoupled from the SM")
print("="*70)
for T_dec, name in [(0.20,"QCD scale ~200 MeV"),(100.0,"electroweak ~100 GeV"),
                    (3e5,"dyad scale ~300 TeV")]:
    print(f"\ndecoupling at {name}  (g*S_SM={gS(T_dec):.1f}):")
    for lbl,Te in ev.items():
        z=zeta(T_dec,Te); dn=dNeff(z)
        flag=" <-- in committed window" if 0.25<=z<=0.35 else ""
        print(f"   eval @ {lbl}:  zeta={z:.3f}  DeltaN_eff={dn:.3f}{flag}")

print("\n" + "="*70)
print("Inverse: what g*S at decoupling does the committed window demand?")
print("(evaluated at the deuterium epoch, g*S=3.91)")
print("="*70)
for zt in (0.25,0.30,0.35):
    g_dec = 3.91/zt**3
    print(f"   zeta={zt:.2f} (DeltaN_eff={dNeff(zt):.3f})  needs g*S(dec)={g_dec:.0f}"
          + ("  -- exceeds SM max 106.75; needs early dec + extra dof" if g_dec>106.75
             else "  -- SM reaches this above the EW/top scale"))
print("\nRead: an early (above-EW) decoupling gives zeta ~ 0.33 from SM dilution")
print("alone -- the TOP of the committed window, with no free knob. Anchored, not guessed.")
