# zon_disp retune — GetDist + P-040 lineup grade (2026-08-21)

**Root:** `docs/chains/cmp_prtoe_zon_disp_retune` (48 ranks, harvested after AWS stop)  
**Gate:** checkpoint `converged: true`, last R−1 = **0.03618**, R−1 CL = **0.1888** (stops 0.05 / 0.2).  
**GetDist:** `ignore_rows=0.3`, N_raw = 1,356,763 → N_after_burn = 949,753.  
**Not:** nested evidence. **Not:** Stage A H₀ twins (different BAO stack).

## Sampler

The retune **did stop**. Instance `i-090c0275d8198ae14` is stopped. Files are complete (48 `.txt` + progress + covmat + checkpoint).

## Clock parameter (the reason this chain exists)

| | |
|---|---|
| `log10_zon` mean | **7.571** |
| std | **0.511** |
| 68% | **[7.190, 8.260]** |
| prior | flat box 6.5–8.5 (std of U(6.5,8.5) ≈ 0.577) |
| rank-mean spread | 0.574 (7.30–7.87) |
| quarter-segment mean spread | **1.51** |

The posterior on `log10_zon` is **almost the prior**. Data did not pin the onset clock.

## Lineup 7.55 / 7.70 / 7.85

All three registered marks lie **inside** the 68% interval. Distances in units of this σ:

| rung | mark | Δ | nσ | inside 68% |
|---|---:|---:|---:|---|
| constituent / α_c=3α | 7.55 | +0.021 | 0.04 | yes |
| pair call | 7.70 | −0.129 | 0.25 | yes |
| upper rung | 7.85 | −0.279 | 0.55 | yes |

**Verdict: INCONCLUSIVE.** Nearest mean is 7.55; that is **not** a confirmation. The July-28 refusal still applies in spirit: a center you cannot localize cannot grade a 0.15-spaced lineup. Quoting “consistent with 7.55 at <1σ” without the 0.51-dex width would be the same near-miss trap as the old 7.5494 cumulative mean.

## Other GetDist (30% burn-in)

Usable as the **stopped retune’s** cosmological margins. Do not mix with booked DESI-DR2 / old-BAO Stage A twins.

| parameter | mean | 68% limits |
|---|---|---|
| omega_b | 0.022757 | [0.022669, 0.022846] |
| H0 | 69.894 | [69.363, 70.596] |
| logA | 3.0505 | [3.0363, 3.0636] |
| n_s | 0.97087 | [0.96774, 0.97403] |
| z_reio | 7.783 | [7.063, 8.500] |
| log10_zon | 7.571 | [7.190, 8.260] |
| dcdf_rho_inf | 0.70225 | [0.69597, 0.71050] |
| A_planck | 1.00099 | [0.99912, 1.00286] |
| m_ncdm | 0.0681 | [0.0033, 0.0935] |
| S8 | 0.8231 | [0.8136, 0.8324] |

Triangle: `zon_disp_retune_triangle.png`. JSON: `grade.json`.

## What this unblocks / does not

**Unblocks:** “is the retune still running?” — no. Sampler finished.  
**Does not unblock:** P-040 α_c=3α *confirmation*, quartet-clock pair call, ρ_inf occupancy closure that needs a *localized* log10 z_on. Those remain **OPEN-MACHINE** because the clock width is the blocker, not a missing harvest.

**Owner (2026-08-21, revised):** do **not** build the model on the singlet 7.55 pin. Hold the clock as **INCONCLUSIVE**. See `OWNER_PIN.md`.

## Forbidden

- “α_c = 3α confirmed”
- “pair call confirmed/killed”
- Booking this `log10_zon` as a Stage A number
- Mixing this H₀ with DESI-DR2 or old-BAO booked twins
