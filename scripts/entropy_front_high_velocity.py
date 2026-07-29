#!/usr/bin/env python3
"""
The entropy front at high relative velocity  (docket #65)

PRTOE_entropy.md prices the front in the slow limit and then says outright:
"Priced; the front's treatment at high relative velocity is still owed."

The slow-limit law is a traversed fraction f = v/c_s times the kinetic third of the
rest-energy step. That is linear in v and therefore cannot be right for all v: it
exceeds the whole available step at v > c_s. So the owed treatment is really two
questions -- where does the linear law saturate, and what replaces it above that.

Both answers are the same velocity, and it is not a coincidence. The saturation of
the adiabatic pickup and the onset of dissipation are both set by c_s: the first
because the element can traverse no more than all of the front, the second because
c_s is the Landau critical velocity of this condensate (medium_induced_decoherence.py).
Below it the medium is frictionless and the pickup is adiabatic; above it the medium
can be excited and the pickup is no longer the whole story.

Then the question that decides whether any of this matters: does anything actually
get there?
"""

import math

ALPHA   = 1.0 / 137.035999084
C_KMS   = 299792.458
BETA_S  = math.sqrt(3.0 * ALPHA)
CS_KMS  = BETA_S * C_KMS

E_STEP_KEV = 6.41          # full rest-energy step, from PRTOE_entropy.md
KINETIC_THIRD = E_STEP_KEV / 3.0

CHECKS = []
def chk(name, got, booked, tol, unit=""):
    ok = abs(got) <= tol if booked == 0 else abs(got - booked) / abs(booked) <= tol
    CHECKS.append((ok, name, booked, got, unit))

print("=" * 76)
print("THE ENTROPY FRONT AT HIGH RELATIVE VELOCITY")
print("=" * 76)

print(f"\n  c_s   = sqrt(3 alpha) c = {BETA_S:.7f} c = {CS_KMS:,.0f} km/s")
print(f"  step  = {E_STEP_KEV} keV, of which a traversing element takes the kinetic")
print(f"          third = {KINETIC_THIRD*1000:.0f} eV at full traversal")

# ---------------------------------------------------------------- 1. reproduce the slow limit
print("\n[1] The recorded slow-limit numbers, reproduced")
for label, v, booked_f, booked_eV in [
    ("ordinary infall, 1000 km/s", 1000.0, 0.023, 50.0),
    ("merger shocks, ~3000 km/s",  3000.0, 0.07,  150.0),
]:
    f = v / CS_KMS
    dE = KINETIC_THIRD * 1000.0 * f
    print(f"    {label:30s} f = {f:.4f} (booked {booked_f})   dE = {dE:5.1f} eV (booked {booked_eV})")
    chk(f"f at {label}", f, booked_f, 0.06)
    chk(f"dE at {label}", dE, booked_eV, 0.06, "eV")

print("\n    The slow-limit law is reproduced, so the extension below is an extension")
print("    of the corpus's own construction and not a substitute for it.")

# ---------------------------------------------------------------- 2. where it saturates
print("\n[2] Where the linear law dies")
print("    f = v/c_s is a TRAVERSED FRACTION. A fraction cannot exceed one, so the")
print("    law is only meaningful while v < c_s, and the correct statement is")
print("\n        f = min(1, v/c_s),      dE = (E_step/3) * f\n")
print(f"    Saturation at v = c_s = {CS_KMS:,.0f} km/s gives the ceiling")
print(f"        dE_max = E_step/3 = {KINETIC_THIRD*1000:.0f} eV per particle")
print(f"    which in the file's own units is ~{KINETIC_THIRD*1000:.0f} keV cm^2 --")
print("    above the 100-300 keV cm^2 floors that groups actually show.")
print("\n    So the ceiling is NOT small. The reason the channel stays sub-dominant is")
print("    entirely that nothing gets near the ceiling, which is the next section.")

chk("saturation ceiling (eV/particle)", KINETIC_THIRD * 1000.0, 2136.7, 0.01, "eV")

# ---------------------------------------------------------------- 3. the two roles of c_s
print("\n[3] Why the saturation velocity and the dissipation threshold are the same")
print("    Two independent statements both land on c_s:")
print("      (a) f = v/c_s reaches 1 at v = c_s   -- the element traverses the whole front")
print("      (b) Landau's criterion on the Bogoliubov branch gives v_c = c_s exactly")
print("          (no roton minimum; see medium_induced_decoherence.py)")
print("\n    They are the same number because both are the speed at which the medium")
print("    re-phases. Below it the medium keeps ahead of the element, the pickup is")
print("    adiabatic, and Landau forbids any excitation -- the entropy gained is")
print("    reversible work, not dissipation. At and above it the medium can no longer")
print("    keep ahead, and the same crossing that saturates the fraction also opens")
print("    the excitation channel. The slow-limit treatment is therefore not merely")
print("    an approximation that degrades; it describes a qualitatively different")
print("    regime from the one above threshold, and there is a sharp line between.")

# ---------------------------------------------------------------- 4. the census
print("\n[4] What actually reaches it")
print(f"    Threshold: {CS_KMS:,.0f} km/s = {BETA_S:.4f} c\n")
census = [
    ("cool-core infall",              800.0,   "thermal gas"),
    ("cluster infall, typical",      1000.0,   "thermal gas"),
    ("merger shock, typical",        3000.0,   "thermal gas"),
    ("Bullet Cluster shock",         4700.0,   "thermal gas"),
    ("fastest known cluster merger", 5000.0,   "thermal gas"),
    ("AGN outflow, slow end (0.03c)", 0.03*C_KMS, "ionized outflow"),
    ("AGN ultra-fast outflow (0.1c)", 0.10*C_KMS, "ionized outflow"),
    ("AGN ultra-fast outflow (0.3c)", 0.30*C_KMS, "ionized outflow"),
    ("relativistic jet (Gamma ~ 10)", 0.995*C_KMS, "relativistic plasma"),
]
print("      system                          v (km/s)     v/c_s     regime")
n_super = 0
for label, v, kind in census:
    r = v / CS_KMS
    reg = "SUPERCRITICAL" if r >= 1 else "subcritical"
    if r >= 1: n_super += 1
    print(f"      {label:31s} {v:9,.0f}  {r:8.3f}   {reg}")

print("\n    Every thermal-gas system in the universe is subcritical, and by a wide")
print("    margin: the fastest cluster merger known reaches v/c_s = "
      f"{5000.0/CS_KMS:.3f}.")
chk("fastest cluster merger stays subcritical", 5000.0 / CS_KMS, 0.1127, 0.02)

# what the fastest cluster gas actually picks up
dE_fastest = KINETIC_THIRD * 1000.0 * (5000.0 / CS_KMS)
print(f"    Its pickup is {dE_fastest:.0f} eV, i.e. ~{dE_fastest:.0f} keV cm^2 -- inside the")
print("    observed 100-300 floor range, but still a few per cent of what the shock")
print("    itself supplies, exactly as the file already argues.")
chk("pickup at the fastest cluster merger", dE_fastest, 240.9, 0.02, "eV")

# ---------------------------------------------------------------- 5. the live corner
print("\n[5] The one place the threshold is crossed by bulk matter")
print(f"    The threshold, {BETA_S:.3f} c, sits INSIDE the observed range of AGN")
print("    ultra-fast outflow velocities, which run from about 0.03 c to 0.3 c.")
print("    So the model divides a single observed population in two: outflows below")
print(f"    {BETA_S:.3f} c move through the medium without exciting it, and outflows above")
print("    that velocity can. Relativistic jets are far above and always supercritical.")
print("\n    This is a sharp, model-specific velocity applied to a population that is")
print("    already measured and already binned by velocity. Whether the crossing is")
print("    OBSERVABLE is a separate question and needs the matter-medium coupling,")
print("    which is not yet fixed -- so no detectability claim is made here.")
print("    What is fixed is where the line falls.")

# ---------------------------------------------------------------- verdict
print("\n" + "=" * 76)
print("VERDICT on #65")
print("=" * 76)
print(f"""
    The owed treatment is supplied, and the answer is that the regime the file was
    worried about is never reached by the gas the file is about.

      * The linear law f = v/c_s is a traversed fraction and saturates at f = 1.
        Its ceiling is E_step/3 = {KINETIC_THIRD*1000:.0f} eV per particle, which is ABOVE the observed
        100-300 keV cm^2 floors. The channel is bounded by the ceiling, not by the
        law being small.

      * Saturation and the Landau threshold are the same velocity, c_s, because both
        measure how fast the medium re-phases. Below it the pickup is adiabatic and
        Landau forbids excitation; above it the pickup saturates and dissipation opens.

      * Every thermal-gas system is subcritical. The fastest cluster merger known
        reaches v/c_s = {5000.0/CS_KMS:.3f}, so the slow-limit treatment is valid everywhere the
        corpus applies it. The high-velocity correction to cluster entropy is nil.

      * The threshold IS crossed by AGN ultra-fast outflows, whose measured velocities
        straddle {BETA_S:.3f} c, and by relativistic jets. That is where any high-velocity
        physics lives, and it is a different observational programme from the entropy
        floor entirely.

    Net: #65 closes for clusters by showing the correction vanishes there, and hands
    the surviving question to a population the entropy file never considered.
""")

print("=" * 76)
n_ok = sum(1 for c in CHECKS if c[0])
for ok, name, booked, got, unit in CHECKS:
    if not ok:
        print(f"  FAIL  {name}: booked {booked}, got {got} {unit}")
print(f"CHECKS: {n_ok}/{len(CHECKS)} passing")
print("=" * 76)
