# Late Θ scorecard — vs Θ_lock and |H_kin|/H_door

**Θ_lock (d=3)** = 11.706  
**|H_kin|/H_door** = |Θ| · c_s/√3 = |Θ| · 0.085425  
At lock: |H_kin|/H_door = 1.

S1 pays only on **late / settled mass-weighted ⟨Θ⟩**, not peak, not vacuum spikes.

---

## 1. Layer scorecard

| layer | late ⟨Θ⟩ | settled ⟨Θ⟩ | peak / mean-max | late/lock | \|H_kin\|/H_door late | lock? | quotable? |
|---|---:|---:|---:|---:|---:|---|---|
| **0D best late** | **+2.870** | +0.109 | +11.77 | 0.245 | 0.245 | NO | YES (toy) |
| 0D max settled | — | **+0.114** | — | 0.010 | 0.010 | NO | YES (toy) |
| 0D default | +0.061 | ~0.06–0.28* | +2.18 | 0.0052 | 0.0052 | NO | YES |
| 0D best peak row | −1.74 | — | **+14.76** | peak-only | — | NO (late fails) | peak≠S1 |
| **1D GPE clean** | **+0.0265** | +0.0015 | +0.721 | 0.0023 | 0.0023 | NO | YES |
| 1D raw local | — | — | ~3000 | — | — | NO | **NOT S1** |
| Spherical light | O(−0.02) | O(−0.01) | O(0.1) | ~0 | ~0 | NO | **NO** (dE fail) |
| **2D Θ_xx** | **+0.0346** | +0.0391 | +0.104 | 0.0030 | 0.0030 | NO | YES |
| 2D Θ_yy | ~1e-6 | — | ~3e-6 | ~0 | ~0 | NO | YES (passive) |
| Avg CG dynamic | +0.0325 | +0.0334 | +0.0345 | 0.0028 | 0.0028 | NO | YES |
| **PACKAGE MAX (S1)** | **+2.870** | **+0.114** | 14.76 peak | **0.245** | **0.245** | **NO** | — |

\*Default “settled” without long `settle_extra` can mix with re-entry-window tail; long-settle phase-2 on survivors is ≲0.11.

---

## 2. Peak-vs-late recheck (0D)

| metric | value |
|---|---:|
| physical peak ≥ Θ_lock | **74** rows |
| of those, late ≥ Θ_lock | **0** |
| max late among peak-hits | **2.870** |
| max settled among top late | **0.114** |

**Peak can exceed lock; late never does under legal physical rows.** Same honesty as prior `PEAK_VS_LATE.md`, with a higher late ceiling (2.87 vs 1.80) still failing S1.

---

## 3. |H_kin|/H_door ladder (d=3)

| Θ | \|H_kin\|/H_door | note |
|---:|---:|---|
| 1 | 0.0854 | unit reference |
| default late 0.061 | 0.0052 | stocked FA3 |
| 1D late 0.027 | 0.0023 | clean GPE |
| 2D late 0.035 | 0.0030 | pancake axis |
| best late 2.87 | **0.245** | extreme 0D toy |
| Θ_lock 11.71 | **1.000** | required for door match |

Even the best legal late leaves |H_kin| at **~25%** of H_door — not lock.

---

## 4. Grade line

| question | answer |
|---|---|
| Max late Θ | **2.870** |
| Lock reached (late)? | **NO** |
| Production 3D COMPLETE? | **False** |
| S1 | **MISSING_INPUT** |
| Package grade | **OPEN-BLOCKED** |
| COMPLETE | **0** |

## Window sensitivity (F5)
| row | tail10 | tail20 | settled |
|---|---:|---:|---:|
| best late (80,-8,3,0.02) | +2.8701 | **−0.1364** | +0.1085 |
| stocked (6,-2,1.5,0.15) | +0.0612 | (see JSON) | +0.2813 |
