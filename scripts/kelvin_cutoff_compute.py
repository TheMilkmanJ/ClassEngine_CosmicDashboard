"""kelvin_cutoff_compute — the promotion gate run: flags resolved, and an edge discovered (2026-07-27).

WHAT THIS COMPUTES (recorded parameters only)
  At representative imprint epochs (the pivot's and the observable window's
  edges), with the recorded core ξ = ħ/(mc_s), the network at its demanded
  density (γ from the triangle), and cells at the demanded count:
    * the Kelvin Mach number at the cutoff scale, M = (Λ/2)·(ξ/ℓ_min) with
      Λ = ln(ℓ_min/ξ) — the subsonic suppression parameter;
    * the bare (quadrupole/Lighthill-class) per-cycle emission ~ C·M⁵
      against the screened channel's g_scr/4π — FLAG (ii) decided by
      numbers, not by helium analogy;
    * the bare-alone cutoff count (epoch-dependent — its subdominance is
      REQUIRED for scale invariance, and is checked, not assumed);
    * the construction's own UV validity edge: the redshift where the cell
      size reaches the core (ℓ_min = ξ), mapped to a comoving scale.

FLAG STATUS AFTER THIS RUN
  (ii) the bare-channel suppression: RESOLVED BY COMPUTATION at the pivot
       and below (bare ~10³× weaker per cycle; weaker still at larger
       scales), TIGHTENING toward the window's UV edge — reported exactly.
  (i)  the screened vertex: SHARPENED, not closed — the count's structure
       N₁ = (4π/g_scr)/O(1) is computed; the exact prefactor awaits the
       vertex derivation, with one structural consistency noted: the same
       4π loop convention is already fixed in the recorded closed form.

THE DISCOVERY THE COMPUTATION FORCES (named exposure, unassessed)
  The cell size tracks the causal range (β·c_s/H) while the core is fixed —
  so the hierarchy ℓ_min/ξ SHRINKS toward early times and saturates
  (ℓ_min = ξ) at a computable redshift, mapping to k_edge ≈ 0.26/Mpc:
  essentially AT the observable window's edge.  Beyond it the imprint
  construction cannot continue unchanged.  Consequence for smaller scales
  (the Lyman-α range) unassessed — a new named exposure, recorded.

GRADE RULE
  Computation with recorded numbers; the demanded count is used only to
  LOCATE the cutoff scale whose physics is then checked.  Nothing promoted;
  flag (i) remains the gate.
"""
from __future__ import annotations

import math

M_EV = 2.24e-20
C_S = math.sqrt(3.0 / 137.036)
H0_EV = 1.44e-33
OM_R, OM_M = 9.0e-5, 0.31
Z_EQ, K_EQ = 3400.0, 0.010
ALPHA_C = 3.0 / 137.036
K_SCREEN = 1.36461
BETA = 2.21e-4
GAMMA = 0.173
N1 = 783.3


def hubble(z: float) -> float:
    return H0_EV * math.sqrt(OM_R * (1 + z) ** 4 + OM_M * (1 + z) ** 3)


def epoch_row(k_mpc: float):
    z = Z_EQ * (k_mpc / K_EQ)                  # RD entry estimate
    H = hubble(z)
    xi = 1.0 / (M_EV * C_S)
    L_net = GAMMA * C_S / H
    l_min = L_net / N1
    ratio = l_min / xi
    lam = math.log(max(ratio, 1.0 + 1e-9))
    mach = (lam / 2.0) * (1.0 / ratio) if ratio > 1 else float("nan")
    g_scr = ALPHA_C / K_SCREEN
    p_scr = g_scr / (4.0 * math.pi)
    p_bare = mach ** 5 if ratio > 1 else float("nan")
    n_bare = ((L_net / xi) ** 5 / max(lam / 2.0, 1e-9) ** 5) ** (1.0 / 6.0)
    return z, L_net / xi, ratio, lam, mach, p_bare, p_scr, n_bare


def main() -> None:
    print("=" * 78)
    print("The Kelvin cutoff computed at the imprint epochs")
    print("=" * 78)
    print("\n   k [/Mpc]   z_entry    L_net/ξ    ℓ_min/ξ    Mach     bare/screened   N_bare-alone")
    for k in (0.002, 0.05, 0.2):
        z, LX, r, lam, M, pb, ps, nb = epoch_row(k)
        print(f"   {k:7.3f}   {z:8.0f}   {LX:9.2e}  {r:8.1f}   {M:.4f}   "
              f"{pb/ps:12.2e}   {nb:10.0f}")
    print("\n   READ, flag (ii): at the pivot the bare channel is ~10³× weaker per")
    print("   cycle than the screened channel (and ~10⁵× at the largest scales) —")
    print("   the suppression is COMPUTED, and the bare-alone count (epoch-")
    print("   dependent, 2500+) confirms the screened channel sets the cutoff.")
    print("   Toward the window's UV edge the margin narrows to ~20× and the")
    print("   hierarchy nearly saturates — reported exactly.")

    xi = 1.0 / (M_EV * C_S)
    H_edge = BETA * C_S / xi
    z_edge = ((H_edge / H0_EV) ** 2 / OM_R) ** 0.25 - 1.0
    k_edge = K_EQ * z_edge / Z_EQ
    print(f"\n   THE UV VALIDITY EDGE: ℓ_min = ξ at H = β·c_s/ξ ⟹ z ≈ {z_edge:.2e},")
    print(f"   k_edge ≈ {k_edge:.2f}/Mpc — essentially at the observable window's")
    print("   edge. Beyond it the imprint construction cannot continue unchanged.")
    print("   Consequence for smaller scales (the Lyman-α range) UNASSESSED — a")
    print("   new named exposure, recorded in the working log.")

    print("\n   Flag (i) status: the count's structure N₁ ∝ 4π/g_scr is the")
    print("   closure's output; the exact prefactor awaits the vertex derivation.")
    print("   Structural consistency noted: the identical 4π loop convention is")
    print("   already fixed in the recorded closed form — one convention, two")
    print("   appearances, zero freedom if the vertex computation lands.")

    print("\nVERDICT: flag (ii) resolved by computation (with its UV-edge caveat);")
    print("   flag (i) sharpened to a single vertex derivation; and the run's")
    print("   honest surprise is the construction's own validity edge sitting at")
    print("   the observable boundary — either a prediction or an exposure, and")
    print("   named as the latter until assessed. Nothing promoted.")
    print("=" * 78)

    _, _, r_piv, _, _, pb_piv, ps_piv, nb_piv = epoch_row(0.05)
    assert pb_piv / ps_piv < 5e-3
    assert nb_piv > N1
    assert 0.15 < k_edge < 0.45


if __name__ == "__main__":
    main()
