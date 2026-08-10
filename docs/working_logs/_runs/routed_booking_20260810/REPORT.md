# Route-D GetDist booking — 20260810

**Result:** BOOKED Stage A  
**Gate:** R−1 < **0.1** AND `converged: true` (routeD production stop; not the bbnfix 0.05 gate)  
**Instrument:** Route-D thaw (`dcdf_floor_thaw` free) on DESI-2024 BAO + Planck + ACT + SPT + Pantheon+SH0ES stack  
**Authority peel:** `routed_peel_20260810` · instance `i-0c65cc61a575bdfa7` (stopped after peel)

## Gate

| chain | N | timestamp | R−1 | bounds R−1 | converged | ready |
|---|---:|---|---:|---:|---|---|
| `cmp_prtoe_routeD` | 39332 | 2026-08-10T17:59:45.393807 | **0.054201** | 0.178571 | **true** | **YES** |

- progress last field-4 R−1 = 0.054201 < 0.1  
- checkpoint `converged: true`, `Rminus1_last` = 0.054201, `mpi_size: 3`  
- launchlog ends: *Sampling complete after 39332 accepted steps.*

## GetDist marginals (`ignore_rows=0.3`)

Post-burn samples: **27534** (3 ranks stacked)

| parameter | mean ± std | 68% |
|---|---|---|
| omega_b | 0.022796 ± 7.926e-05 | [0.022721, 0.0228722] |
| H0 | 69.6258 ± 0.57426 | [69.1939, 70.2657] |
| logA | 3.0548 ± 0.013503 | [3.04245, 3.06853] |
| n_s | 0.972759 ± 0.0031172 | [0.969528, 0.975656] |
| z_reio | 8.06197 ± 0.68712 | [7.43852, 8.77553] |
| dcdf_rho_inf | 0.714516 ± 0.010856 | [0.702763, 0.719844] |
| dcdf_conv_g | 0.091059 ± 0.094669 | [-0.000754743, 0.10356] |
| dcdf_floor_thaw | 0.0475544 ± 0.03273 | [0.00566785, 0.0658983] |
| m_ncdm | 0.0251388 ± 0.023132 | [-0.000377067, 0.0320299] |
| sigma8 | 0.842763 ± 0.018442 | [0.824827, 0.849518] |
| Omega_m | 0.283211 ± 0.012689 | [0.277645, 0.297112] |
| S8 | 0.81828 ± 0.0097533 | [0.808347, 0.827437] |
| Omega0_dcdf | 0.952967 ± 0.00078012 | [0.952403, 0.953837] |

### Headline (Stage A)

| quantity | value |
|---|---|
| **H₀** | **69.6258 ± 0.57426** |
| **dcdf_floor_thaw** | **0.0475544 ± 0.03273** |
| **m_ncdm** | **0.0251388 ± 0.023132** |
| **S₈** | **0.81828 ± 0.0097533** |

Triangle: `docs/plots/cmp_prtoe_routeD_triangle.png`

## Fences

- **Not** the bbnfix evidence pair (old-BAO or DESI-DR2). Separate thaw fork.
- Not nested PolyChord evidence.
- SH0ES-conditional stack (pantheonplusshoes present in yaml).
- Do not quote as “ΛCDM beaten” without a matched twin book (no lcdm twin on this peel).
- Stage A process receipt only (no Stage B multi-param red audit required for this freeze unless promoted).

## Provenance

- AWS resume 2026-08-10 ~16:20Z from N=16085 / R−1≈0.39  
- MPI 3 × OMP 32 on 96 vCPU  
- Dual-gate met ~17:59Z; peel + local land same day  

*NO FABRICATIONS. Booked 2026-08-10T18:53Z.*
