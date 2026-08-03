#!/usr/bin/env python3
"""
The localizable zero at the burst (T = m_e): the +expansion energy and the
-gravitational binding cancel EXACTLY, both as medium quantities. (JP's chase --
"put the GR-beating claim on the board as a computation, not an argument.")

WHAT IS EXACT vs WHAT IS INTERPRETIVE (read first, so it is not over-read):
  * EXACT (and computed here): for a flat universe -- which the T = m_e epoch is,
    to high precision -- the expansion kinetic energy of a test mass at the Hubble
    radius EXACTLY equals its gravitational binding, and the Hubble radius EXACTLY
    equals the Schwarzschild radius of the enclosed mass. Net energy per unit mass
    is zero. This is the "zero-energy universe" (Tryon/Guth), evaluated at the
    burst scale with real numbers. It is exact by the Friedmann relation, not an
    order-of-magnitude coincidence.
  * NOT unique to PRTOE: the zero itself is standard. What PRTOE adds is that BOTH
    halves are localizable IN THE MEDIUM -- the +kinetic is the medium's own
    collective motion, the -binding is the medium's induced gravity -- so the zero
    is a sum of real, place-able pieces, where GR can only write it globally with a
    non-localizable pseudotensor. The localizability is a FRAMEWORK claim (gravity =
    the medium), asserted here, not derived from the medium's energy functional.
  * JP's thermal picture, placed honestly: the burst's thermal "glow" is the SOURCE
    -- it sits inside the mass-energy M that gravitates. It is bound to the SAME
    ORDER as its own rest energy (the universe sits at its own Schwarzschild
    radius), which is the intuitive "glow cancelled by binding." The part that is
    EXACT is the expansion-vs-gravity balance; the thermal-vs-binding reading is the
    O(1) gloss on it.
  * NOT shown (still open): why the burst TURNS at T = m_e (the bounce needs the
    stiff/repulsive term, separate physics); the total MAGNITUDE (needs the genesis
    volume L_gen, unassigned, #180); and Friedmann derived FROM the medium's energy
    functional (the real GR-beating build). And the cost is unchanged: a localizable
    energy requires the medium's rest frame -- a preferred frame.
"""
import math

# --- constants (SI) -----------------------------------------------------------
G, c, hbar, kB = 6.674e-11, 2.998e8, 1.055e-34, 1.381e-23
eV = 1.602e-19
me_E = 510998.95 * eV          # electron rest energy = k_B T at the burst (J)

# --- the burst: T = m_e, thermal energy density of the relativistic medium -----
gstar = 10.75                  # photons + e+- + 3 nu at T ~ m_e
rho_E = gstar * (math.pi**2/30) * me_E**4 / (hbar*c)**3   # J/m^3 (thermal glow)
rho_m = rho_E / c**2                                       # kg/m^3

# --- Friedmann -> Hubble radius and the enclosed mass -------------------------
H   = math.sqrt(8*math.pi*G/3 * rho_m)     # 1/s
R_H = c / H                                 # m
M   = (4.0/3.0)*math.pi*R_H**3*rho_m        # kg within one Hubble radius

print("=" * 70)
print("THE BURST, IN NUMBERS  (T = m_e = 0.511 MeV)")
print("=" * 70)
print(f"  thermal energy density  rho = {rho_E:.3e} J/m^3   (glow of the medium)")
print(f"  Hubble rate             H   = {H:.3e} 1/s")
print(f"  Hubble radius           R_H = {R_H:.3e} m   ({R_H/c:.3e} light-seconds)")
print(f"  mass within R_H         M   = {M:.3e} kg")

# --- the two halves, per unit mass at the Hubble edge -------------------------
# a test mass on the Hubble sphere recedes at rdot = H R_H = c
rdot     = H * R_H
E_kin    = 0.5 * rdot**2          # +expansion kinetic energy per unit mass
E_bind   = -G * M / R_H           # -gravitational binding per unit mass
print()
print("=" * 70)
print("THE LEDGER, PER UNIT MASS AT THE HUBBLE EDGE")
print("=" * 70)
print(f"  recession speed  rdot = H R_H = {rdot:.4e} m/s   (= c = {c:.4e})")
print(f"  +expansion  E_kin  = +1/2 rdot^2 = {E_kin:+.5e} J/kg   (the medium's motion)")
print(f"  -binding    E_bind = -G M / R_H  = {E_bind:+.5e} J/kg   (the medium's gravity)")
print(f"  ---------------------------------------------------------------")
print(f"  E_kin + E_bind     = {E_kin+E_bind:+.3e} J/kg   -> ZERO to machine precision")
print("  Both terms are the MEDIUM's: its collective recession, and its own")
print("  induced-gravity self-binding. The zero is a sum of two placeable pieces.")

# --- the Schwarzschild reading: R_H = R_s exactly (flat) ----------------------
R_s = 2*G*M/c**2
print()
print("=" * 70)
print("THE SCHWARZSCHILD READING  (why the glow is bound to ~zero)")
print("=" * 70)
print(f"  Schwarzschild radius of the Hubble mass  R_s = 2GM/c^2 = {R_s:.3e} m")
print(f"  Hubble radius                            R_H         = {R_H:.3e} m")
print(f"  R_H / R_s = {R_H/R_s:.6f}   -> EXACTLY 1 for a flat universe")
print("  The Hubble volume sits at its OWN Schwarzschild radius: its mass-energy")
print("  (the thermal glow included) is gravitationally bound to net zero. The")
print("  burst manufactures its +glow and -binding in one stroke, netting nothing")
print("  -- which is why it needs no counterparty to pour from.")

# --- honest grade -------------------------------------------------------------
print()
print("=" * 70)
print("GRADE (honest)")
print("=" * 70)
print("""  ON THE BOARD (exact, computed): at T = m_e the flat-universe ledger nets to
  zero per unit mass, +expansion = -binding, and R_H = R_s exactly. The
  zero-energy universe, evaluated at the burst, with both halves written as the
  medium's own (recession + induced gravity). The GR-beating claim is now a line,
  not an argument -- for the LOCALIZABILITY; the zero itself is standard.

  STILL OPEN (unchanged): (1) the bounce -- why it turns at m_e rather than
  collapsing -- needs the stiff term, not shown; (2) the total MAGNITUDE needs the
  genesis volume L_gen (#180); (3) the real win, Friedmann FROM the medium's energy
  functional, still owed; (4) the cost -- the medium's rest frame is a preferred
  frame -- is not paid off, only deferred.""")

# --- self-check ---------------------------------------------------------------
_c = []
def chk(name, got, exp, tol):
    ok = abs(got-exp) <= tol*(1+abs(exp)); _c.append(ok)
    print(f"  [{'ok' if ok else 'FAIL'}] {name}")
print("\nself-check:")
chk("E_kin + E_bind = 0 (per unit mass)", (E_kin+E_bind)/E_kin, 0.0, 1e-12)
chk("R_H = R_s exactly (flat)", R_H/R_s, 1.0, 1e-9)
chk("recession at R_H equals c", rdot/c, 1.0, 1e-9)
print(f"\n{'ALL PASS' if all(_c) else 'SOME FAILED'}  ({sum(_c)}/{len(_c)})")
