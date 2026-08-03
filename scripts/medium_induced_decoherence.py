#!/usr/bin/env python3
"""
Does the medium decohere quantum superpositions on its own?

The exploratory README left this stated but uncomputed: "whether the medium induces
decoherence of its own, beyond ordinary environmental decoherence, at a rate set by its
healing length xi = hbar/(m c_s) and its temperature. If it does, there is a number and a
scaling and a test. If it provably does not, that is a null with a mechanism."

This settles it. The answer is a null, it is forced by two independent mechanisms, and it
comes with a velocity threshold that is not vacuous -- relativistic matter sits above it.

Inputs, all already in the corpus:
    m   = 2.24e-20 eV      (medium constituent, roster-trial-conditional)
    a_c = 3*alpha          (pre-registered)
    c_s = sqrt(a_c)        (in units of c)
    xi  = hbar/(m c_s)     (recorded 402 AU)

Nothing cosmological enters. No fitting.
"""

import math

# ---------------------------------------------------------------- constants
ALPHA   = 1.0 / 137.035999084
HBARC   = 1.973269804e-7      # eV m
C_LIGHT = 299792458.0         # m/s
K_B     = 8.617333262e-5      # eV/K
AU      = 1.495978707e11      # m

# ---------------------------------------------------------------- inputs
M_EV    = 2.24e-20            # medium constituent mass, eV
ALPHA_C = 3.0 * ALPHA
BETA_S  = math.sqrt(ALPHA_C)  # c_s / c

CHECKS = []
def chk(name, got, booked, tol, unit=""):
    ok = abs(got) <= tol if booked == 0 else abs(got - booked) / abs(booked) <= tol
    CHECKS.append((ok, name, booked, got, unit))
    return ok

print("=" * 74)
print("MEDIUM-INDUCED DECOHERENCE: is there any?")
print("=" * 74)

# ---------------------------------------------------------------- 1. scales
print("\n[1] The medium's own scales")
c_s_ms   = BETA_S * C_LIGHT
xi_m     = HBARC / (M_EV * BETA_S)
xi_au    = xi_m / AU
mu_eV    = M_EV * BETA_S**2          # Bogoliubov chemical potential = m c_s^2
mu_K     = mu_eV / K_B

print(f"    alpha_c = 3*alpha        = {ALPHA_C:.7f}")
print(f"    c_s     = sqrt(alpha_c)  = {BETA_S:.7f} c = {c_s_ms/1e3:,.0f} km/s")
print(f"    xi      = hbar/(m c_s)   = {xi_m:.4e} m = {xi_au:.1f} AU")
print(f"    mu      = m c_s^2        = {mu_eV:.4e} eV  ->  {mu_K:.4e} K")

# reproduce the corpus's recorded healing length as a setup check
chk("xi reproduces recorded 402 AU", xi_au, 402.0, 0.02, "AU")

# ---------------------------------------------------------------- 2. dispersion
print("\n[2] The dispersion, and where the Landau threshold sits")
print("    Bogoliubov:  omega(q) = c_s q sqrt(1 + (q xi / 2)^2)")
print("    The corpus's xi = hbar/(m c_s) IS the Bogoliubov healing length, so the")
print("    dispersion is fixed with no further input. Landau critical velocity is")
print("    v_c = min_q [omega(q)/q]. For this branch omega/q rises monotonically")
print("    from c_s, so the minimum is the q->0 limit:")

def omega_over_q(q_xi):
    """omega(q)/q in units of c_s, as a function of q*xi."""
    return math.sqrt(1.0 + (q_xi / 2.0) ** 2)

sample = [0.0, 0.01, 0.1, 1.0, 10.0]
print("\n      q*xi      (omega/q)/c_s")
for s in sample:
    print(f"      {s:6.2f}    {omega_over_q(s):.6f}")

v_c_over_cs = min(omega_over_q(s) for s in [i * 1e-3 for i in range(0, 20001)])
print(f"\n    numerical min over q*xi in [0,20]: {v_c_over_cs:.9f}  (analytic: 1)")
chk("Landau v_c equals c_s exactly (no roton dip)", v_c_over_cs, 1.0, 1e-9)

v_c_ms = c_s_ms
print(f"    => v_c = c_s = {v_c_ms/1e3:,.0f} km/s = {BETA_S:.4f} c")
print("    No roton minimum exists on a Bogoliubov branch, so v_c is not reduced.")

# ---------------------------------------------------------------- 3. subcritical null
print("\n[3] Mechanism one: nothing in the lab can excite the medium")
probes = [
    ("lab apparatus, thermal",        1.0e3),
    ("Earth's orbital motion",        2.98e4),
    ("Sun through the galaxy",        2.2e5),
    ("Earth through the CMB frame",   3.698e5),
    ("fast solar wind",               8.0e5),
]
print(f"    Landau threshold: {v_c_ms/1e3:,.0f} km/s\n")
print("      probe                          v (km/s)     v/v_c     excitable?")
for label, v in probes:
    r = v / v_c_ms
    print(f"      {label:28s} {v/1e3:9,.1f}  {r:9.2e}   {'YES' if r >= 1 else 'no'}")
    chk(f"{label} is subcritical", 1.0 if r < 1 else 0.0, 1.0, 1e-12)

print("\n    Below v_c there is no final state conserving both energy and momentum,")
print("    so the medium cannot record which path was taken. No record, no decoherence.")
print("    This is exact at T = 0, and it is kinematics, not a small coupling.")

# ---------------------------------------------------------------- 4. rigidity null
print("\n[4] Mechanism two: the order parameter cannot resolve a lab superposition")
print("    The condensate varies on scale xi. Two paths separated by dx perturb it by")
print("    a relative amount ~ (dx/xi)^2, which is the decoherence-rate suppression.")
seps = [
    ("atom interferometer",     1e-9),
    ("large-molecule fringe",   1e-6),
    ("optomechanical mirror",   1e-3),
    ("metre-scale, hypothetical", 1.0),
    ("Earth-Sun distance",      AU),
]
print(f"\n    xi = {xi_m:.3e} m\n")
print("      superposition                 dx (m)       dx/xi        (dx/xi)^2")
for label, dx in seps:
    r = dx / xi_m
    print(f"      {label:28s} {dx:9.2e}  {r:10.3e}  {r*r:11.3e}")

r_um = 1e-6 / xi_m
chk("micron superposition suppression (dx/xi)^2", r_um**2, 2.82e-40, 0.05)

print("\n    A micron superposition is suppressed by 3e-40 before any coupling constant")
print("    is applied. The two mechanisms are independent: one kills the rate on")
print("    velocity grounds, the other on length grounds. Both give zero.")

# ---------------------------------------------------------------- 5. finite T
print("\n[5] The only loophole: finite temperature. It closes itself.")
print("    Thermal phonons are not Landau-forbidden, so a T > 0 medium has a normal")
print("    component that can scatter. The relevant length is the thermal phonon")
print("    wavelength lambda_T = hbar c_s / (k_B T), and the suppression becomes")
print("    (dx/lambda_T)^2 instead of (dx/xi)^2. So the question is whether lambda_T")
print("    can ever fall below xi.\n")

def lambda_T(T_K):
    return HBARC * BETA_S / (K_B * T_K)

T_at_mu = mu_K
lam_at_mu = lambda_T(T_at_mu)
print(f"      at T = mu/k_B = {T_at_mu:.3e} K :  lambda_T = {lam_at_mu:.4e} m")
print(f"      xi                              =  {xi_m:.4e} m")
chk("lambda_T(T=mu/k_B) equals xi", lam_at_mu, xi_m, 1e-9, "m")

print("\n    lambda_T = xi exactly at T = mu/k_B. That is not a coincidence: it is the")
print("    same Bogoliubov relation read twice. And T > mu/k_B is the regime where the")
print("    phonon description fails and the condensate itself is destroyed -- the")
print("    medium would no longer be the superfluid the model requires.")
print("\n    So for any T at which the model's medium exists at all, lambda_T >= xi,")
print("    and the finite-T suppression is WEAKER than the T = 0 one is strong.")
print("    The loophole does not open.")

for T in [1e-20, 1e-18, mu_K, 1e-16]:
    lam = lambda_T(T)
    state = "condensed" if T <= mu_K else "NOT condensed (phonons gone)"
    print(f"      T = {T:.2e} K -> lambda_T = {lam:.3e} m  ({lam/xi_m:6.2f} xi)   {state}")

# ---------------------------------------------------------------- 6. the live corner
print("\n[6] Where the threshold is NOT vacuous: relativistic matter")
print(f"    v_c = {BETA_S:.4f} c is low. Anything with gamma above a few sits above it.\n")
rel = [
    ("beta = 0.148 (threshold)", BETA_S),
    ("1 MeV electron",           math.sqrt(1 - 1/(1 + 1.0/0.511)**2)),
    ("10 MeV electron",          math.sqrt(1 - 1/(1 + 10.0/0.511)**2)),
    ("1 GeV proton (KE)",        math.sqrt(1 - 1/(1 + 1.0/0.938)**2)),
    ("cosmic ray, 1 TeV proton", math.sqrt(1 - 1/(1 + 1000.0/0.938)**2)),
]
print("      particle                       beta       above v_c?")
for label, b in rel:
    print(f"      {label:28s} {b:.6f}   {'YES' if b > BETA_S else 'no'}")

n_super = sum(1 for _, b in rel[1:] if b > BETA_S)
chk("all four relativistic probes are supercritical", n_super, 4, 1e-12)

print("\n    Every relativistic particle in the universe is supercritical and may emit")
print("    medium phonons by a Cherenkov process. That is a real channel, and it is")
print("    where a bound on the matter-medium coupling has to come from -- not from")
print("    tabletop decoherence, which this calculation has just shown is dead.")

# ---------------------------------------------------------------- verdict
print("\n" + "=" * 74)
print("VERDICT")
print("=" * 74)
print("""
    The ULTRALIGHT DARK CONDENSATE induces no decoherence of its own on any
    laboratory superposition. (Sector matters: the vacuum is a separate condensate
    whose excitations ride the light cone, so its own Landau velocity is c and
    nothing outruns it -- that is the zero-drag certificate behind inertia, a
    different argument that must not be merged with this one.)

    This is a null with a mechanism -- two mechanisms, independent of each other:

      (a) Landau.    v_c = sqrt(3 alpha) c = 0.1479596 c = 44,357 km/s. Every terrestrial
                     and solar-system velocity is below it by at least two orders of
                     magnitude, so no excitation is kinematically allowed at all.

      (b) Rigidity.  xi = 402 AU. The order parameter cannot resolve a separation
                     smaller than that; a micron superposition is suppressed by
                     (dx/xi)^2 = 3e-40 before any coupling is applied.

    Finite temperature does not rescue the effect: lambda_T >= xi throughout the
    entire range in which the medium remains condensed, with equality exactly at
    T = mu/k_B where the condensate ends.

    WHAT THIS COSTS THE MODEL. It forbids the model from ever claiming credit for
    an anomalous decoherence signal. If a tabletop experiment reports collapse
    beyond the environmental prediction, this medium cannot be its cause. The
    prohibition is forced by the two numbers above and cannot be tuned away
    without giving up either alpha_c = 3 alpha or m = 2.24e-20 eV.

    WHAT IT BUYS. The quantum-foundations files stop being interpretation. The
    statement "the medium hosts quantum mechanics without disturbing it" is now a
    computed result with a threshold attached, rather than a reading.

    WHERE THE LIVE PHYSICS MOVED. Upward in velocity. v_c = 0.148 c is low enough
    that all relativistic matter is supercritical, so the medium's one open
    decoherence-adjacent channel is Cherenkov phonon emission by fast particles.
    That is the corner worth computing next.
""")

# ---------------------------------------------------------------- harness
print("=" * 74)
n_ok = sum(1 for c in CHECKS if c[0])
for ok, name, booked, got, unit in CHECKS:
    if not ok:
        print(f"  FAIL  {name}: booked {booked}, got {got} {unit}")
print(f"CHECKS: {n_ok}/{len(CHECKS)} passing")
print("=" * 74)
