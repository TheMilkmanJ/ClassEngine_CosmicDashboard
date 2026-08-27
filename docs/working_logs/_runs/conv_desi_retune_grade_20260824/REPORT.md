# conv_desi retune — stopped GetDist grade (2026-08-24)

**Root:** `/home/ubuntu/docs_runs/conv_desi_20260821T045241Z` on `i-0e1b73cbc65e565d2` (`prtoe-conv-desi-192`, 192 ranks)  
**Yaml:** `cmp_prtoe_conv_desi_retune.yaml` (not the Jul-22 archive `cmp_prtoe_conv_desi`)  
**Gate:** checkpoint `converged: true`, last R−1 = **0.04469**, R−1 CL = **0.18537** (stops 0.05 / 0.2). Last progress N = **1,647,022** at 2026-08-24 16:25 UTC. Load 0 afterwards.  
**GetDist:** 30% burn, N_raw = 1,647,022 → N_after_burn = **1,153,002**. Weighted 16/84 percentiles.

**Not:** Stage A H₀ twins. **Not:** nested evidence. **Not:** a KiDS/DES shear fit. **Not:** a published S₈-tension win.

## Sampler

The retune **did stop**. Dual gate met. Do not resume the Jul-22 archive or the 2026-08-19 poisoned tree (R−1~7314).

## Conversion lever `dcdf_conv_g`

Pre-registered **g ≈ 0.10 ± 0.05**. Prior box 0–1, start guess 0.2.

| | |
|---|---|
| mean | **0.0799** |
| std | **0.0721** |
| 68% | **[0.0153, 0.1463]** |
| 5–95% | [0.0047, 0.225] |
| fraction g < 0.05 | **43.8%** |
| fraction g < 0.01 | **10.8%** |
| registered 0.10 inside 68% | yes |
| g = 0 inside 68% | no (16th percentile 0.015) |

**Verdict: INCONCLUSIVE / lever not on.** Compatible with the registered 0.10, also piled toward the prior wall. Data on this stack (Planck + ACT + SPT + DESI BAO + Pantheon+SH0ES) do **not** demand conversion. Do not quote “g ≈ 0.12” from the old minimizer as this posterior.

## Derived S₈ (not lensing data)

| | mean | 68% |
|---|---:|---|
| S₈ | **0.8164** | **[0.8071, 0.8256]** |
| σ₈ | 0.8441 | [0.8327, 0.8554] |
| Ω_m | 0.2808 | [0.2716, 0.2898] |
| H₀ | 70.211 | [69.791, 70.635] |

S₈ ~0.816 sits on the **KiDS-Legacy published number** 0.814 ± 0.012. That is a **point coincidence** on a SH0ES-anchored derived S₈, with `g` not required. It is **not** a matched shear likelihood. KiDS/DES 3×2pt remains owed before any tension-easing claim.

No LCDM twin was run on this same conversion yaml, so “closer to KiDS than ΛCDM on this stack” is **not** shown.

## Other GetDist (30% burn)

| parameter | mean | 68% limits |
|---|---:|---|
| omega_b | 0.022780 | [0.022700, 0.022860] |
| H0 | 70.211 | [69.791, 70.635] |
| logA | 3.0552 | [3.0417, 3.0687] |
| n_s | 0.97226 | [0.96925, 0.97526] |
| z_reio | 8.042 | [7.355, 8.734] |
| dcdf_rho_inf | 0.7172 | [0.7094, 0.7250] |
| dcdf_conv_g | 0.0799 | [0.0153, 0.1463] |
| A_planck | 1.00117 | [0.99931, 1.00303] |
| m_ncdm | 0.0325 | [0.0071, 0.0585] |
| sigma8 | 0.8441 | [0.8327, 0.8554] |
| Omega_m | 0.2808 | [0.2716, 0.2898] |
| S8 | 0.8164 | [0.8071, 0.8256] |

JSON: `grade.json`. Chains remain on the instance (~6 MB × 192).

## What this unblocks / does not

**Unblocks:** “is conv_desi still unproduced?” — no. Sampler finished. `g` and S₈ have a stopped posterior.

**Does not unblock:** S₈ tension-easing paper claim; KiDS/DES likelihood; nested ΔlnZ; Stage A H₀ booking on this yaml; confirmation of g = 0.10 or g = 10ε.
