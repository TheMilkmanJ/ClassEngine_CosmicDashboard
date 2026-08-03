#!/usr/bin/env python3
"""
Does the onset amplitude redshift onto today's dark matter density?

The corpus records three numbers from different places:

    Psi_0 = 5.03e16 GeV     the misalignment amplitude, fixed by demanding Omega_DM
    m     = 2.24e-20 eV     the ultralight quantum mass, from the onset clock
    z_on  = 4.03e7          the onset redshift, the H = m identity

WHAT THIS IS, STATED BEFORE THE RESULT SO THE RESULT CANNOT BE OVERSOLD.

Psi_0 was FIXED BY DEMANDING today's abundance. PHYSICS_DOMAINS row 70 says so
outright: "the genesis fee is reheating entropy; Psi_0 ~ 5e16 GeV is fixed by
demanding today's abundance after that fee... the abundance pin is arithmetic -- a
revised Omega_DM or entropy history moves it."

Therefore redshifting Psi_0 forward and recovering Omega_DM is CIRCULAR. It inverts
the relation that defined Psi_0 and gets the input back. It is a useful arithmetic
check -- it would catch a slipped exponent, a wrong dilution law, or a mis-stated
z_on, and those are real failure modes -- but it is NOT independent confirmation of
anything, and it must never be quoted as the model predicting the dark matter density.

The genuinely independent coincidence in this sector is a different one, which this
script does NOT test: genesis_solver_B1_findings.md reports the misalignment amplitude
(5.03e16 GeV) agreeing to 0.4% with the potential's own quartic-to-mass crossover
m/sqrt(lambda) at the recorded lambda ~ 2e-91 (5.01e16 GeV). That comparison has
content only if lambda was fixed without reference to the abundance; checking that is
open work.

The one result below that owes nothing to any fitted input is section [6], the
Cherenkov cap, which is pure kinematics.
"""

import math

# ---------------------------------------------------------------- constants
HBARC_eVcm = 1.9732698e-5      # eV cm
GEV        = 1.0e9             # eV per GeV

# ---------------------------------------------------------------- corpus inputs
PSI0_GeV = 5.03e16             # misalignment amplitude AT ONSET
M_EV     = 2.24e-20            # ultralight quantum mass, eV
Z_ON     = 4.03e7              # onset redshift (H = m)

# ---------------------------------------------------------------- external inputs
OMEGA_DM_H2 = 0.1200           # Planck 2018
H_LITTLE    = 0.674
RHO_CRIT_H2 = 1.87834e-29      # g/cm^3 per h^2
G_PER_GEV   = 1.78266192e-24   # g per GeV/c^2
RHO_LOCAL   = 0.4              # GeV/cm^3, local halo (for the second part only)

CHECKS = []
def chk(name, got, booked, tol, unit=""):
    ok = abs(got) <= tol if booked == 0 else abs(got - booked) / abs(booked) <= tol
    CHECKS.append((ok, name, booked, got, unit))

def gevcm3_to_eV4(x):
    """GeV/cm^3 -> eV^4 (natural units)."""
    return x * GEV / (1.0 / HBARC_eVcm) ** 3

print("=" * 74)
print("THE ONSET AMPLITUDE, REDSHIFTED")
print("=" * 74)

# ---------------------------------------------------------------- route 1
print("\n[1] Forward: onset amplitude -> today")
print("    A coherently oscillating scalar dilutes as matter, so Psi ~ a^(-3/2).")
print("    Oscillation begins at z_on, where H = m; before that the field is frozen.\n")

dilution = (1.0 + Z_ON) ** 1.5
psi_today_fwd = PSI0_GeV / dilution
print(f"    Psi_0            = {PSI0_GeV:.4e} GeV   (at z_on = {Z_ON:.3e})")
print(f"    (1+z_on)^(3/2)   = {dilution:.4e}")
print(f"    Psi_today        = {psi_today_fwd:.4e} GeV")

# ---------------------------------------------------------------- route 2
print("\n[2] Backward: measured dark matter density -> required amplitude")
print("    For an oscillating scalar the cycle-averaged density is rho = (1/2) m^2 Psi^2.\n")

omega_dm  = OMEGA_DM_H2 / H_LITTLE**2
rho_crit  = RHO_CRIT_H2 * H_LITTLE**2 / G_PER_GEV      # GeV/cm^3
rho_dm    = omega_dm * rho_crit                         # GeV/cm^3
rho_dm_eV4 = gevcm3_to_eV4(rho_dm)

psi_today_bwd_eV = math.sqrt(2.0 * rho_dm_eV4) / M_EV
psi_today_bwd    = psi_today_bwd_eV / GEV

print(f"    Omega_DM         = {omega_dm:.4f}")
print(f"    rho_crit         = {rho_crit:.4e} GeV/cm^3")
print(f"    rho_DM (mean)    = {rho_dm:.4e} GeV/cm^3 = {rho_dm_eV4:.4e} eV^4")
print(f"    Psi required     = {psi_today_bwd:.4e} GeV")

# ---------------------------------------------------------------- the closure
print("\n[3] The comparison")
ratio = psi_today_fwd / psi_today_bwd
print(f"\n    forward  (from Psi_0, m, z_on): {psi_today_fwd:.4e} GeV")
print(f"    backward (from Omega_DM, m)   : {psi_today_bwd:.4e} GeV")
print(f"    ratio                          : {ratio:.5f}")
print(f"    disagreement                   : {abs(ratio-1)*100:.2f}%")

chk("Psi_0 redshifts onto Omega_DM", ratio, 1.0, 0.05)

if abs(ratio - 1) < 0.05:
    print("\n    These close -- as they must, because Psi_0 was defined by demanding")
    print("    exactly this. The check is worth running (it would catch a slipped")
    print("    exponent, a wrong dilution law, or a mis-stated z_on) but it CONFIRMS")
    print("    NOTHING about the physics. Route 1 and route 2 are the same equation")
    print("    read in opposite directions. Do not quote this as the model predicting")
    print("    the dark matter density.")

# ---------------------------------------------------------------- why the naive check fails
print("\n[4] Why this looks broken if done carelessly")
rho_from_psi0 = 0.5 * M_EV**2 * (PSI0_GeV * GEV)**2      # eV^4, if Psi_0 were TODAY's
rho_from_psi0_gev = rho_from_psi0 / gevcm3_to_eV4(1.0)
print(f"\n    Treating Psi_0 as a present-day amplitude gives")
print(f"      rho = (1/2) m^2 Psi_0^2 = {rho_from_psi0_gev:.3e} GeV/cm^3")
print(f"    against the local halo value {RHO_LOCAL} GeV/cm^3 --")
print(f"    too large by a factor {rho_from_psi0_gev/RHO_LOCAL:.2e}.")
print("\n    Two separate mistakes produce that: Psi_0 is the amplitude AT ONSET and")
print("    must be diluted by (1+z_on)^(3/2), and the halo density is ~10^5 times the")
print("    cosmic mean, so it is the wrong target. Correcting both closes the loop.")

chk("naive (no redshift) overshoot is ~2e17", rho_from_psi0_gev / RHO_LOCAL, 2.07e17, 0.05)

# ---------------------------------------------------------------- local amplitude
print("\n[5] The local field amplitude, which any coupling calculation needs")
rho_local_eV4 = gevcm3_to_eV4(RHO_LOCAL)
psi_local_eV  = math.sqrt(2.0 * rho_local_eV4) / M_EV
boost = psi_local_eV / psi_today_bwd_eV
print(f"\n    rho_local  = {RHO_LOCAL} GeV/cm^3")
print(f"    Psi_local  = {psi_local_eV/GEV:.4e} GeV")
print(f"    enhancement over the cosmic mean: {boost:.1f}x  (= sqrt of the density ratio)")
chk("halo amplitude boost = sqrt(density ratio)", boost,
    math.sqrt(RHO_LOCAL / rho_dm), 1e-9)

# ---------------------------------------------------------------- kinematics
print("\n[6] Coupling-free consequence: how much energy one emitted quantum can carry")
print("    A projectile above the Landau threshold may emit medium quanta. In the")
print("    no-recoil limit the Cherenkov condition v >= omega(q)/q with the Bogoliubov")
print("    branch omega/q = sqrt(c_s^2 + (q/2m)^2) caps the momentum transfer:\n")
print("        q_max = 2m sqrt(v^2 - c_s^2),      omega_max = v q_max")

beta_s = math.sqrt(3.0 / 137.035999084)
for label, v in [("v = 0.5 c", 0.5), ("v = 0.9 c", 0.9), ("ultra-relativistic", 1.0)]:
    if v <= beta_s:
        continue
    q_max = 2.0 * M_EV * math.sqrt(v*v - beta_s*beta_s)
    w_max = v * q_max
    print(f"      {label:22s} q_max = {q_max:.3e} eV   omega_max = {w_max:.3e} eV")

w_max_ur = 1.0 * 2.0 * M_EV * math.sqrt(1.0 - beta_s**2)
chk("omega_max (ultra-relativistic)", w_max_ur, 4.4305e-20, 0.01, "eV")

print(f"\n    So no single emitted quantum carries more than {w_max_ur:.3e} eV, however")
print("    energetic the projectile. Losing 1 eV to the medium takes")
print(f"    {1.0/w_max_ur:.2e} emissions; losing 1 TeV takes {1e12/w_max_ur:.2e}.")
print("\n    This bound needs no coupling constant. It says the medium can only be fed")
print("    in ultra-soft quanta, and it is why the absolute rate -- which does need")
print("    the coupling -- has such a steep hill to climb before it matters anywhere.")

# ---------------------------------------------------------------- report
print("\n" + "=" * 74)
n_ok = sum(1 for c in CHECKS if c[0])
for ok, name, booked, got, unit in CHECKS:
    if not ok:
        print(f"  FAIL  {name}: booked {booked}, got {got} {unit}")
print(f"CHECKS: {n_ok}/{len(CHECKS)} passing")
print("=" * 74)
