# T14 i6 prep — 9.7% re-extract mirror residual (smoke 64³)

**Date:** 2026-08-03 ~08:45 MDT  
**Source fields:** `docs/working_logs/_runs/t14_hkin_resmoke_i4b/psi_*.npy`  
**Status:** non-production residual (Claude note i on i5 AGREE)

## Decomposition (default n_modes=4, Tw sheet-fold on)

| branch | 2n | Tw | Wr | H |
|---|---:|---:|---:|---:|
| n+1 f+1 | +2 | 0.000 | +0.001 | +2.001 |
| n+1 f−1 | +2 | 0.000 | +0.035 | +2.035 |
| n−1 f+1 | −2 | 0.000 | **−0.242** | −2.242 |
| n−1 f−1 | −2 | 0.000 | −0.125 | −2.125 |

## True-mirror residual is **all Wr**

| pair | H sum | rel | Tw sum | Wr sum |
|---|---:|---:|---:|---:|
| (1,+1)↔(−1,−1) | −0.125 | **6.0%** | 0 | −0.125 |
| (1,−1)↔(−1,+1) | −0.206 | **9.6%** | 0 | −0.206 |

Tw antisymmetry is exact (folded). Mutual term 2n flips cleanly. The fence stress is **centerline writhe noise at 16 bins / 64³**, largest on `n−1_f+1` (Wr=−0.24).

## n_modes scan (same ψ)

Higher modes (≥5) invent |Wr|~0.3–0.8 on noisy 16-bin rings → dial must not lean on them for booking. Default nm=4 is the calibrated helix setting; nm=2 under-smooths helix cal but reduces this branch’s Wr to −0.05 (suggests residual is high-mode bin noise).

## Implication for i6 (128³)

- Expect cleaner core localization → smaller |Wr| and mirror residual.  
- Production target **&lt;5%** (Claude i6) is the right bar; if not held, investigate Wr before booking overall sign.  
- Do **not** “fix” by selecting on |Wr|; keep blind selector.

## Not done here

No production run. No change to smoke booking.
