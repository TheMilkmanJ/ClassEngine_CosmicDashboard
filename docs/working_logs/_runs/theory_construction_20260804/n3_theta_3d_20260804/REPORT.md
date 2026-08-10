# N3 — A_Θ-3D + S1 Θ_lock hunt (2026-08-04)

**Package:** `docs/working_logs/_runs/theory_construction_20260804/n3_theta_3d_20260804/`  
**Seat:** Grok blue  
**Prior:** `bounce_residual_demand` N3 · N1 S1 (`Θ_lock≈11.71`) · `fa3_metric_off` kinematic map  
**Fences:** NO invent force laws · no invent \(H_\mathrm{re}\) · no free dial · no bounce closed · no cyclic · leave MCMCs · no PolyChord  
**COMPLETE:** **0** — grade **OPEN-BLOCKED**

---

## 0. One-liner

**Legal medium stress turns ⟨Θ⟩ under stocked 0D/1D GPE toys, but late healing Θ stays ≲ 1.8 ≪ Θ_lock≈11.7; S1 and production A_Θ-3D remain MISSING_INPUT / OPEN-BLOCKED. Toy turn ≠ 3D COMPLETE.**

---

## 1. Mission

N3 asks whether a **production / 3D (or instrument-grade)** medium can deliver \(\langle\Theta\rangle:-\to0\to+\) under legal GPE, and whether that can raise \(\Theta_\mathrm{heal}\) toward

\[
\Theta_\mathrm{lock}=\frac{d}{c_s\sqrt3}\approx 11.71\quad(d=3)
\]

needed for N1 magnitude lock at the shear door (\(H_\mathrm{kin}=H_\mathrm{door}\)).

**S1** (from N1 survivors): derive \(\Theta_\mathrm{heal}\gtrsim 11.7\) from legal stress at re-entry — not 0D O(1) stand-ins sold as lock.

---

## 2. Package contents

| File | Role |
|---|---|
| [`REPORT.md`](./REPORT.md) | This executive |
| [`INSTRUMENT_INVENTORY.md`](./INSTRUMENT_INVENTORY.md) | 0D/1D/2D/GPE stocked vs production gap |
| [`THETA_LOCK_HUNT.md`](./THETA_LOCK_HUNT.md) | Scan results vs \(\Theta_\mathrm{lock}\) |
| [`SURVIVORS.md`](./SURVIVORS.md) | What remains open |
| [`NON_CLAIMS.md`](./NON_CLAIMS.md) | Fences |
| [`MASTER.md`](./MASTER.md) | Stamp |
| [`logs/n3_theta_lock_scan.log`](./logs/n3_theta_lock_scan.log) | Full compute |
| Script | `scripts/bounce_n3_theta_lock_scan.py` |

---

## 3. Anchors (disk, this run)

| quantity | value |
|---|---|
| \(c_s=\sqrt{3\alpha}\) | 0.14796 |
| \(\Theta_\mathrm{lock}\) (d=3) | **11.706** |
| \(\|H_\mathrm{kin}(\Theta=1)\|/H_\mathrm{door}\) | 0.0854 |
| stocked 0D late \(\Theta\) (n0=6,Θ0=−2,κ=1.5,γ=0.15) | **+0.0619** |
| stocked 0D \(\Theta_\mathrm{max+}\) | +2.18 |
| stocked 0D overshoot | 1.34 |

---

## 4. Headline results

| metric | value | vs \(\Theta_\mathrm{lock}\) |
|---|---|---|
| **max late ⟨Θ⟩ (S1 lock metric)** | **+1.80** | **0.154×** — **not reached** |
| max 0D physical peak / 1D mean | +11.34 | 0.968× peak; late there **negative** |
| 1D mass-weighted ⟨Θ⟩ max | +1.06 | 0.091× |
| 1D late mean ⟨Θ⟩ | ~0 | ~0 |
| raw Madelung local max | ~2900 | **not S1** (vacuum spike) |
| medium turn (0D/1D) | **YES** | toy PAID only |
| production 3D instrument | **absent** | N3 open |

**Θ_lock reached under legal late/mean scan? NO.**

---

## 5. What was scanned (legal only)

1. **0D** reduced stress ODE (FA3/N1 form): \(n_0,\Theta_0,\kappa,\gamma\) grid; 83 unique, 78 physical (5 blowups rejected).  
2. **1D GPE** M6 split-step: six \((A,v_0)\) corpus cases; energy clean.  
3. **Synthetic averaging** stress channel (static).  
4. **Corpus priors** (not re-run): spherical M6, hypersonic, transverse 2D, averaging identity.

No invented drive beyond stocked \(\kappa(n-1)\) stand-in and repulsive GPE \(|\psi|^2-1\).

---

## 6. Grade stamp

| claim | grade |
|---|---|
| Toy \(\langle\Theta\rangle\) turn under legal stress | **PAID (toy/M6 class)** |
| Production A_Θ-3D instrument | **OPEN / not stocked** |
| S1 \(\Theta_\mathrm{heal}\gtrsim 11.7\) late | **MISSING_INPUT** |
| Magnitude lock via Θ | **OPEN-BLOCKED** |
| Bounce / \(H_\mathrm{re}\) Derived | **false / not claimed** |
| N3 COMPLETE promotion | **0** |

> **One-line:** N3/S1 — turn YES at toy; late Θ≲1.8≪11.7; OPEN-BLOCKED.

---

## 7. Red ask

Fabrication / selling 1D rebound as 3D production / selling peak or vacuum spikes as \(\Theta_\mathrm{lock}\) / free \(\kappa,\gamma\) as Derived. Blue claims **0 COMPLETE**.
