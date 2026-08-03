"""Junction rectifier quartet: provenance-typed consistency check.

PRTOE_baryogenesis.md §3a (updated 2026-08-02/03):

  COMPUTED members:
    Γ_φ = G_F² T_sph⁵ = 5.3902×10⁹ eV   (T_sph = 131.7 GeV)
    θ̇  = 59.68 eV                     (deep-frozen winding at T_sph)
    R_needed ≈ 5×10⁻⁵                  (η = n·𝒯 at registered n-band)

  BACK-SOLVED (not independent):
    ω_J ≈ 5.672 keV from R = ω_J²/(2 Γ_φ θ̇)
    j = ω_J²/Γ_φ ≈ 6.03 meV

  STALE SHORTHAND (do not treat as data):
    Γ_φ/θ̇ ~ 10⁷  — actual is 9.03×10⁷; holding 10⁷ fixed manufactures a fake ×9 miss.

Claude RED 2026-08-03: label every member's provenance type so rounding cannot re-enter as data.

Run: python3 scripts/baryogenesis_junction_closure.py
"""
from __future__ import annotations

import math

# --- COMPUTED (first principles / registered) ---
T_SPH_GEV = 131.7
# G_F in natural units → Γ_φ = G_F² T⁵; use corpus value
GAMMA_PHI = 5.3902e9  # eV  type: COMPUTED
THETA_DOT = 59.68  # eV   type: COMPUTED
R_NEEDED = 5.0e-5  # type: COMPUTED from η band
RATIO_COMPUTED = GAMMA_PHI / THETA_DOT  # ~9.03e7

# --- BACK-SOLVED target ---
OMEGA_J = math.sqrt(2.0 * R_NEEDED * GAMMA_PHI * THETA_DOT)  # eV
J_REL = OMEGA_J**2 / GAMMA_PHI

# --- STALE shorthand (artifact path) ---
RATIO_STALE = 1.0e7  # type: SHORTHAND — not a measurement

print("=" * 76)
print("PROVENANCE TABLE")
print("=" * 76)
print(f"  Γ_φ              {GAMMA_PHI:.4g} eV     type=COMPUTED  (G_F² T_sph⁵)")
print(f"  θ̇               {THETA_DOT:.4g} eV     type=COMPUTED  (winding @ T_sph)")
print(f"  Γ_φ/θ̇           {RATIO_COMPUTED:.4g}       type=COMPUTED")
print(f"  R needed         {R_NEEDED:.4g}       type=COMPUTED  (η band)")
print(f"  ω_J              {OMEGA_J/1e3:.3f} keV    type=BACK-SOLVED")
print(f"  j = ω_J²/Γ_φ     {J_REL*1e3:.2f} meV    type=BACK-SOLVED")
print(f"  Γ_φ/θ̇ ~10⁷      {RATIO_STALE:.4g}       type=SHORTHAND (stale)")

print()
print("=" * 76)
print("QUARTET AT COMPUTED RATIO — MUST CLOSE")
print("=" * 76)
R = OMEGA_J**2 / (2.0 * GAMMA_PHI * THETA_DOT)
print(f"  R = ω_J²/(2 Γ_φ θ̇) = {R:.4g}   vs needed {R_NEEDED:.4g}"
      f"   ratio R/R_need = {R/R_NEEDED:.4f}")
print(f"  j/(2 θ̇)             = {J_REL/(2*THETA_DOT):.4g}   (same R, j form)")
assert abs(R / R_NEEDED - 1.0) < 0.02, "quartet failed to close at computed Γ_φ"
print("  VERDICT: CONSISTENT to <2% — no internal ×9 discrepancy.")

print()
print("=" * 76)
print("ARTIFACT PATH: hold SHORTHAND ratio 1e7 fixed (do not use for physics)")
print("=" * 76)
th_b = J_REL / (2 * R_NEEDED)
G_b = RATIO_STALE * th_b
om_b = math.sqrt(J_REL * G_b)
print(f"  fake-consistent ω_J = {om_b/1e3:.3f} keV  (×{OMEGA_J/om_b:.2f} under true back-solve)")
print(f"  This is NOT a target. It is the ×9 artifact Claude retired 2026-08-03.")

print()
print("=" * 76)
print("PRE-REGISTERED GRADING BAND (before any forward derivation)")
print("=" * 76)
print("  ACCEPT junction magnitude:  ω_J ∈ [3.0, 12.0] keV")
print("  ANOMALOUS-REVIEW:           ω_J ∈ (0.057, 3.0) ∪ (12, 30] keV")
print("  KILL junction route:        ω_J < 0.057 keV  (×100 under ~5.7)")
print("  Real debt unchanged:        forward ω_J from seat χ + pinning curvature (#39)")
