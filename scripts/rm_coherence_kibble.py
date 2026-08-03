#!/usr/bin/env python3
"""
RM two-point / coherence scale from recorded Kibble geometry.

Corpus inputs only (no new magnetism free parameters):
  ξ_K   = 256 Mpc     Kibble domain comoving size
  χ_*   = 13.76 Gpc   comoving distance to last scattering
  B_seed ≈ 5e-18 G    Harrison smooth seed (amplitude CAP, not void floor)

What this prints:
  - characteristic angular scale θ_ξ(χ) = ξ_K / χ
  - multipole markers ℓ_geo = χ/ξ_K and ℓ_π = π χ/ξ_K
  - unit-normalized shell two-point w(θ)/w(0) from Gaussian 3D B correlation
    with correlation length ξ_K (shape assumption; scale fixed by corpus)

What this does NOT claim:
  - does NOT close the void-floor gap (B_inter-line ≲ B_seed vs blazar ≳1e-16 G)
  - does NOT invent n_e; amplitude requires external electron density
  - does NOT promote a survey fit or "gap closed"

Refs: docs/PRTOE_cosmic_magnetism.md §3a, §4;
      docs/working_logs/_runs/debt_magnetism_20260803/REPORT.md §3–§4.B;
      docs/PRTOE_cmb_anomalies.md (ξ_K/χ_* = 1.07° already audited).
"""

from __future__ import annotations

import math

# ---- recorded corpus geometry (Mpc comoving) --------------------------------
XI_K = 256.0          # Kibble domain size (PRTOE_READERS_GUIDE; cosmic_magnetism)
CHI_STAR = 13760.0    # last-scattering comoving distance (χ_* = 13.76 Gpc)
B_SEED_G = 5.0e-18    # Harrison smooth seed, gauss (cosmic_magnetism §2)
B_BLAZAR_G = 1.0e-16  # blazar TeV-halo floor (external; not a model prediction)

# Source-plane χ samples for illustration (comoving Mpc). Not free params of
# the magnetism sector — external choice of which plane an observer bins.
CHI_PLANES_MPC = (500.0, 1000.0, 2000.0, 3000.0, 5000.0, CHI_STAR)

# Angular sample in units of θ_ξ for the unit-normalized two-point
THETA_OVER_THETA_XI = (0.0, 0.5, 1.0, 1.5, 2.0, 3.0)


def theta_xi_rad(chi_mpc: float) -> float:
    """Characteristic angular scale θ_ξ = ξ_K / χ (radians)."""
    if chi_mpc <= 0:
        raise ValueError("χ must be positive")
    return XI_K / chi_mpc


def ell_geo(chi_mpc: float) -> float:
    """Geometric multipole marker ℓ_geo = χ / ξ_K (k_⊥ χ with k_⊥ = 1/ξ_K)."""
    return chi_mpc / XI_K


def ell_pi(chi_mpc: float) -> float:
    """Peak-style multipole marker ℓ_π = π / θ_ξ = π χ / ξ_K."""
    return math.pi * chi_mpc / XI_K


def w_shell_unit(theta_over_theta_xi: float) -> float:
    """
    Unit-normalized thin-shell angular correlation from a Gaussian 3D B
    correlation ξ_B(r) ∝ exp(−r²/(2 ξ_K²)), flat-sky, equal-χ shell:

        w(θ)/w(0) = exp(−θ² / (2 θ_ξ²)) = exp(−½ (θ/θ_ξ)²)

    Shape assumption only; correlation *length* is the recorded ξ_K.
    """
    x = theta_over_theta_xi
    return math.exp(-0.5 * x * x)


def main() -> None:
    print("=" * 72)
    print("RM coherence from Kibble geometry (corpus-only scale formula)")
    print("=" * 72)
    print()
    print("RECORDED INPUTS")
    print(f"  ξ_K     = {XI_K:.0f} Mpc comoving")
    print(f"  χ_*     = {CHI_STAR/1000:.2f} Gpc = {CHI_STAR:.0f} Mpc")
    print(f"  B_seed  = {B_SEED_G:.1e} G  (smooth Harrison; inter-line CAP)")
    print(f"  B_blazar= {B_BLAZAR_G:.1e} G  (external floor; model does NOT reach it)")
    shortfall = B_BLAZAR_G / B_SEED_G
    print(f"  void shortfall B_blazar/B_seed = {shortfall:.0f}  ({math.log10(shortfall):.2f} dex)")
    print("  → this script does NOT close that gap.")
    print()

    th_star = theta_xi_rad(CHI_STAR)
    print("LAST-SCATTERING REFERENCE (recorded χ_*)")
    print(f"  θ_ξ(χ_*) = ξ_K/χ_* = {th_star:.6f} rad = {th_star*180/math.pi:.4f} deg")
    print(f"  ℓ_geo    = χ_*/ξ_K = {ell_geo(CHI_STAR):.3f}")
    print(f"  ℓ_π      = π χ_*/ξ_K = {ell_pi(CHI_STAR):.3f}")
    n_cells = 4.0 * math.pi / th_star**2
    print(f"  sky cells ~ 4π/θ_ξ² = {n_cells:.3e}  (network tiling, not one spot)")
    print()

    print("TWO-POINT FORMULA (derived structure; see REPORT.md)")
    print("  RM(n̂) = K ∫_0^{χ_s} n_e(χ) B_∥(χ n̂) dχ")
    print("  ⟨RM(n̂₁) RM(n̂₂)⟩ = K² ∬ n_e n_e ⟨B_∥ B_∥⟩ dχ₁ dχ₂")
    print("  with ⟨B_i B_j⟩ structured on comoving scale ξ_K (corpus).")
    print("  Thin-shell unit shape: w(θ)/w(0) = exp(−½ (θ/θ_ξ)²),  θ_ξ = ξ_K/χ")
    print("  Characteristic multipoles: ℓ_geo = χ/ξ_K,  ℓ_π = π χ/ξ_K")
    print()
    print("  DERIVED: geometric transfer ξ_K → (θ_ξ, ℓ) for any source-plane χ.")
    print("  ASSUMED (not free model knobs): Gaussian radial shape of ξ_B;")
    print("    thin-shell / Limber projection; external n_e for amplitude.")
    print("  BOUNDED: B_rms ≲ B_seed under return-flux theorem (not raised to blazar).")
    print()

    print("UNIT-NORMALIZED SHELL TWO-POINT  w(θ)/w(0)")
    print(f"  {'θ/θ_ξ':>8}  {'w/w0':>12}")
    for x in THETA_OVER_THETA_XI:
        print(f"  {x:8.2f}  {w_shell_unit(x):12.6f}")
    print()

    print("CHARACTERISTIC SCALES AT FIXED SOURCE-PLANE χ")
    print(f"  {'χ [Mpc]':>10}  {'θ_ξ [deg]':>12}  {'θ_ξ [arcmin]':>14}  "
          f"{'ℓ_geo':>10}  {'ℓ_π':>10}")
    for chi in CHI_PLANES_MPC:
        th = theta_xi_rad(chi)
        th_deg = th * 180.0 / math.pi
        th_amin = th_deg * 60.0
        print(f"  {chi:10.0f}  {th_deg:12.4f}  {th_amin:14.2f}  "
              f"{ell_geo(chi):10.2f}  {ell_pi(chi):10.2f}")
    print()

    print("CHECKABLE OUTSIDER TARGETS (scale only)")
    print("  • At χ = χ_*: θ_ξ ≈ 1.07°, ℓ_π ≈ 169  (matches CMB-anomaly audit).")
    print("  • At χ ~ 1–3 Gpc (typical extragalactic RM depth class):")
    print("      θ_ξ ~ 5–15°,  ℓ_π ~ 12–37  → large-angle RM correlation feature.")
    print("  • Coherence is ~100 Mpc-class comoving, NOT micro (EW/QCD horizon).")
    print()
    print("NON-CLAIMS")
    print("  - No claim that model B_void ≥ 1e-16 G.")
    print("  - No absolute σ_RM without an external n_e model.")
    print("  - No new free parameter introduced to fit RM surveys.")
    print("=" * 72)


if __name__ == "__main__":
    main()
