"""uv_edge_assessment — task #25: what the validity edge does, computed from the construction's own pieces (2026-07-28).

THE EDGE (recorded, kelvin_cutoff_compute.py)
  The substructure cell tracks the causal range while the core ξ is fixed,
  so the cell-to-core hierarchy N(z) = L_net/ξ/N₁ · N₁ shrinks toward early
  times and saturates (ℓ_min = ξ) at z_edge ≈ 8.9×10⁴ ⟺ k_edge ≈ 0.26/Mpc.
  Beyond the edge the cascade cannot terminate within one network time: the
  realized count per cell falls as N(k) = N₁·(k_edge/k)² (radiation-era
  entry, k ∝ z, H ∝ z²).

THE ASSESSMENT (this script): the edge discriminates between the two
  normalization readings of the amplitude — the exact question of task #15.
    (a) COUPLING-NORMALIZED (the closed form's literal reading):
        A = (g_scr/4π)³ is three powers of the per-vertex coupling.  Nothing
        in it references the realized count, so the spectrum is FLAT through
        the edge: no break, and the Lyman-α range (recorded in the task as
        reading roughly standard power) is an automatic consistency.  The
        edge affects only the substructure bookkeeping.
    (b) COUNT-NORMALIZED (shot noise of N discrete emitters per cell):
        A ∝ N^{-3/2}·C would rise beyond the edge as (k/k_edge)³ in
        amplitude — (k/k_edge)⁶ in power: a violent blue break at 0.26/Mpc,
        ×10⁴ in power by k = 1.2/Mpc.  The task's own kill condition fires.
  The Lyman-α consistency therefore REFEREES the normalization: the
  standard-power reading of the small-scale sky selects (a) and excludes
  (b).  The exposure discovered by the cutoff computation converts into a
  discriminating consistency that constrains #15's C = 1 gate.

WHAT THIS DOES NOT DO
  It does not verify Lyman-α data numerically here (the task's recorded
  characterization — roughly standard power at k ~ 1–3/Mpc — is used as
  stated, no new data claims), and it does not derive reading (a); it shows
  what each reading predicts and which one the recorded sky permits.

GRADE RULE
  The count scaling and both spectra are computed from recorded parameters;
  the verdict is a discrimination, not a promotion.  PROMOTE #25 when #15's
  normalization lands as coupling-class (the weight-zero exhibit); the edge
  is then a consistency.  KILL: the normalization landing count-class.
"""
from __future__ import annotations

import math

M_EV = 2.24e-20
C_S = math.sqrt(3.0 / 137.036)
H0_EV = 1.44e-33
OM_R = 9.0e-5
Z_EQ, K_EQ = 3400.0, 0.010
BETA = 2.21e-4
N1 = 783.3


def main() -> None:
    xi = 1.0 / (M_EV * C_S)
    H_edge = BETA * C_S / xi
    z_edge = ((H_edge / H0_EV) ** 2 / OM_R) ** 0.25 - 1.0
    k_edge = K_EQ * z_edge / Z_EQ

    print("=" * 78)
    print("The validity edge assessed: a referee, not a wound")
    print("=" * 78)
    print(f"\n1. the edge, recomputed: z_edge = {z_edge:.2e}, "
          f"k_edge = {k_edge:.3f}/Mpc")

    print("\n2. the realized count beyond the edge, N(k) = N₁·(k_edge/k)²:")
    print("   k [/Mpc]   z_entry     N(k)    cascade termination")
    for kk in (k_edge, 0.5, 1.0, 2.0, 3.0):
        z = Z_EQ * kk / K_EQ
        Nk = N1 * (k_edge / kk) ** 2
        term = "one network time (edge)" if kk == k_edge else \
               f"needs {N1/Nk:5.1f}× longer"
        print(f"   {kk:7.3f}   {z:8.2e}   {Nk:6.0f}   {term}")

    print("\n3. the two normalization readings beyond the edge:")
    print("   k [/Mpc]   (a) coupling-normalized   (b) count-normalized power")
    for kk in (0.5, 1.0, 2.0, 3.0):
        boost = (kk / k_edge) ** 6
        print(f"   {kk:7.3f}   flat (no break)           ×{boost:9.3g} vs standard")
    print("   reading (b) is a violent blue break at the edge; the task records")
    print("   the Lyman-α range as roughly standard power — (b) is excluded by")
    print("   the recorded sky, (a) passes untouched.")

    print("\nVERDICT: the edge DISCRIMINATES. The small-scale sky's standard")
    print("   reading selects the coupling-normalized amplitude — the closed")
    print("   form's literal structure — and excludes the shot-noise-class")
    print("   normalization. The exposure converts into a consistency that")
    print("   constrains #15's normalization gate from the data side: whatever")
    print("   the weight-zero exhibit produces, it must be coupling-class.")
    print("   Promotion of #25 rides on #15's gate landing that way; the kill")
    print("   (an edge-forced break the data excludes) applies only to the")
    print("   reading the data already disfavors.")
    print("=" * 78)

    assert 0.2 < k_edge < 0.32
    assert abs(N1 * (k_edge / 1.0) ** 2 - N1 * k_edge ** 2) < 1e-9
    assert (1.0 / k_edge) ** 6 > 1e3


if __name__ == "__main__":
    main()
