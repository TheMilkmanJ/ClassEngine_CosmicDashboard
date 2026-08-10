# Instrument inventory — what is stocked vs production gap

**Package:** `n3_theta_3d_20260804`  
**Question:** which scripts already pay medium \(\langle\Theta\rangle\) turn, and what is missing for production A_Θ-3D / S1?

---

## 1. Stocked instruments

| layer | script | what it pays | Θ readout | production? |
|---|---|---|---|---|
| **0D ODE** | `bounce_fa3_hcross_attempt.py`, `bounce_n1_fa2_amplitude_hunt.py`, `bounce_rpA_scaffold.py`, **this** `bounce_n3_theta_lock_scan.py` | Turn under synthetic stress \(\kappa(n-1)\); late Θ~0.06 default | full history | **No** — reduced stand-in |
| **1D Cartesian GPE** | `bounce_m6_rebound_1d.py`, `bounce_m6_rebound_1d_hypersonic.py`, N3 scan 1D probe | Density turn + outward flow; Mach window | N3 adds mass-weighted ⟨Θ⟩ | **No** — 1D |
| **1D averaging identity** | `bounce_averaging_decomposition.py` | Gate (c): stress funds \(d\langle\Theta\rangle/dt\); identity RMS | coarse ⟨Θ⟩ O(1) | **No** — 1D CG |
| **2D transverse** | `bounce_transverse_2d.py` | Transverse passivity; ⟨Θ_xx⟩~0.03–0.08 | axis expansions | **No** — 2D pancake |
| **Spherical GPE** | `bounce_m6_rebound_gp.py`, `bounce_m6_rebound_dst.py` | Geometric focusing; energy-clean scheme exists | n_peak/F, not Θ_lock scan | **No** — spherical symmetry ≠ full 3D |
| **FA3 kinematic map** | `fa3_metric_off/CONSTRUCTION.md`, FA3 script | \(H_\mathrm{kin}=\Theta c_s/(d\xi)\); obstruction A/B/C | algebra | map only |
| **N1 amplitude** | `bounce_n1_fa2_amplitude_hunt.py` | Θ_lock=11.71 required; 0 lands | late Θ from 0D | residual open |

---

## 2. What each layer **does not** pay

| layer | gap |
|---|---|
| 0D | \(\kappa,\gamma\) are **toy reduced**, not Derived GPE coefficients; no spatial stress structure |
| 1D | Global topology / mass-weighted mean Θ ~ O(1) or smaller late; not 3D isotropic expansion |
| Averaging | Exhibits *channel*, not magnitude lock |
| 2D | Validates transverse silence; does not raise Θ to ~12 |
| Spherical | Focusing for O6/MeV discussion; no stocked Θ_lock production run |
| Full 3D GPE | **Not stocked** as production instrument for re-entry Θ |

---

## 3. Production gap (N3 target)

**Wanted for N3 land (instrument-backed re-entry gate):**

1. Legal GPE (or framework medium equation) in **≥3D** or demonstrated production-grade domain.  
2. Mass-weighted / coarse \(\langle\Theta\rangle:-\to0\to+\) with \(\mathrm{d}\langle\Theta\rangle/\mathrm{d}t>0\) at cross.  
3. **Late** \(\langle\Theta\rangle_\mathrm{heal}\) at re-entry candidate epoch (gradients \(\gtrsim\xi\)).  
4. Prefer quotable energy conservation / refinement gates (M6 class).

**Present:** (2) at toy/1D; (3) late ≪ 11.7; (1) and production (4) for full 3D **missing**.

---

## 4. Illegal / rejected readouts (do not sell as S1)

| fake land | why rejected |
|---|---|
| 0D \(\|\Theta\|\) integrator cap (~80–200) | Numerical safety, not physics |
| overshoot \(\gg 100\) rows | Blowup under extreme \(\Theta_0\) |
| raw Madelung local \(\Theta\sim 10^3\) | Vacuum cores; averaging decomp v1 warned |
| free dial \(\kappa,\gamma\) to force late Θ~12 | Not Derived GPE law |
| 1D density turn alone | Turn ≠ magnitude lock |

---

## 5. Bottom line

| paid | open |
|---|---|
| Toy / M6-class medium **turn** | Production **A_Θ-3D** |
| Stress channel necessity (averaging) | **S1** late \(\Theta_\mathrm{heal}\gtrsim 11.7\) |
| Transverse passivity (2D) | Matching book (N2) orthogonal |

**Inventory grade:** instruments enough to **kill false Θ_lock lands** and **confirm toy turn**; **not** enough to close N3 production or S1.
