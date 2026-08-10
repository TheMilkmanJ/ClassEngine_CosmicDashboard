# N3 deepen — GPE late-Θ production-class instrument (2026-08-04)

**Package:** `docs/working_logs/_runs/theory_construction_20260804/n3_gpe_late_theta_20260804/`  
**Seat:** Grok blue  
**Prior:** `n3_theta_3d_20260804` (peak can hit Θ_lock≈11.7; late Θ≲1.8≪lock; `PEAK_VS_LATE.md`)  
**Script:** `scripts/bounce_n3_gpe_late_theta.py`  
**Log:** [`logs/n3_gpe_late_theta.log`](./logs/n3_gpe_late_theta.log)  
**Fences:** stocked GPE/ODE only · no invent force laws · no invent \(H_\mathrm{re}\) · no free dial · no bounce closed · leave MCMCs · no PolyChord · `page_curve_claimed=false` · exit 0 ≠ PASS  

**COMPLETE:** **0** — grade **OPEN-BLOCKED**  
**Production 3D COMPLETE?** **False** (almost never under stocked instruments)

---

## 0. One-liner

**Deeper legal sweeps raise re-entry-window late Θ to ~2.87 (prior ~1.80) but settled late stays ≲0.11; both ≪ Θ_lock≈11.71. Peak can exceed lock; late never. S1 MISSING_INPUT; not 3D COMPLETE.**

---

## 1. Mission

Push stocked **GPE / 1D / 2D / spherical / averaging** instruments as hard as **legal** and report **late / settled mean Θ** (not peak spikes, not Madelung vacuum singularities) vs

\[
\Theta_\mathrm{lock}=\frac{d}{c_s\sqrt3}\approx 11.706\quad(d=3)
\]

and vs \(|H_\mathrm{kin}|/H_\mathrm{door}\) bookkeeping.

---

## 2. Anchors (this run)

| quantity | value |
|---|---:|
| \(c_s=\sqrt{3\alpha}\) | 0.14796 |
| \(\Theta_\mathrm{lock}\) (d=3) | **11.706** |
| \(\|H_\mathrm{kin}(\Theta=1)\|/H_\mathrm{door}\) | 0.08542 |
| stocked 0D default late (6,−2,1.5,0.15) | **+0.0612** |
| **max late Θ (S1 primary, all layers)** | **+2.8701** |
| max settled mean (0D long settle) | **+0.1143** |
| ratio late / Θ_lock | **0.245** |
| \(\|H_\mathrm{kin}(\mathrm{late})\|/H_\mathrm{door}\) | **0.245** |
| late ≥ lock? | **NO** |
| production 3D | **False** |

---

## 3. Late metric definitions (honesty)

| label | definition | role |
|---|---|---|
| **late (S1 primary)** | re-entry-candidate window: integrate to \(t_{n_\mathrm{peak}}+8\), mean of last 10% of Θ history (prior-comparable) | lock candidate |
| **settled** | continue +20 healing times past re-entry cut; mean of final 20% | asymptotic honesty |
| **peak** | \(\max\Theta_+\) on physical (no cap) rows | diagnostic only — **not S1** |
| **raw local / support** | Madelung \(\partial_x v\) spikes | harness singularities — **not S1** |

See prior [`PEAK_VS_LATE.md`](../n3_theta_3d_20260804/PEAK_VS_LATE.md): peak-lock hits still fail late.

---

## 4. Layer results (disk)

### 4.1 0D reduced ODE (stocked FA3/N1)

\[
\dot n=-n\Theta,\qquad \dot\Theta=-\Theta^2+\kappa(n-1)-\gamma\Theta
\]

| metric | value |
|---|---:|
| unique / physical / turned | 710 / 685 / 678 |
| blowups rejected | 25 |
| **max late** | **+2.8701** |
| max settled (top survivors + long settle) | +0.1143 |
| max physical peak | +14.76 |
| peak ≥ lock hits | 74 |
| max late among peak-hits | **+2.87** (still ≪ lock) |
| late ≥ lock | **False** |

**Best late:** \(n_0=80\), \(\Theta_0=-8\), \(\kappa=3\), \(\gamma=0.02\) → late=+2.87, settled≈0.11, peak≈11.77.  
Extreme toy corner (high \(n_0\), tiny \(\gamma\)) — **not** Derived cosmological coefficients.

**Best peak:** same family with \(\kappa=5\) → peak≈14.76, **late=−1.74** (peak ≠ re-entry lock).

Prior package max late was **1.80**; deep corner densification reaches **2.87** — still only **0.245×** lock.

### 4.2 1D Cartesian GPE (M6 form)

| metric | value |
|---|---:|
| cases / clean (dE<5%) | 14 / 9 |
| max mass-weighted ⟨Θ⟩ any time | +0.721 |
| **max late ⟨Θ⟩** | **+0.0265** |
| max settled | +0.0015 |
| raw local max | ~3000 (**not S1**) |
| density turn | YES (all) |
| late ≥ lock | **False** |

Best late clean: \(A=20\), \(v_0=1\), \(R=12\) → late=+0.0265.

### 4.3 Spherical GPE light probe (DST)

| metric | value |
|---|---:|
| cases / clean | 2 / **0** |
| density turn | YES |
| late Θ (unclean) | O(10⁻²), negative |
| energy | **failed** on coarse light grid (dE ≫ 5%) |

**Not quoted for S1.** Full production M6 spherical focusing remains a separate instrument (`bounce_m6_rebound_dst.py` / `gp.py`); light Θ probe is energy-unclean here. Even unclean late stays ≪ lock. **Spherical symmetry ≠ full-3D production.**

### 4.4 2D pancake (transverse class)

| metric | value |
|---|---:|
| ⟨Θ_xx⟩ late | +3.46×10⁻² |
| ⟨Θ_xx⟩ settled | +3.91×10⁻² |
| ⟨Θ_yy⟩ late | ~10⁻⁶ (passive) |
| dE | ~0% |
| late ≥ lock | **False** |

### 4.5 Averaging stress channel

| metric | value |
|---|---:|
| static stress_drive | +2.31×10⁻² (>0) |
| dynamic CG late ⟨Θ⟩ | +3.25×10⁻² |
| dynamic turned | YES |
| late ≥ lock | **False** |

Channel funds turn; magnitude not lock.

---

## 5. Grade stamp

| claim | grade |
|---|---|
| Toy / M6-class ⟨Θ⟩ turn under legal stress | **PAID** |
| Late Θ_lock ≳ 11.7 (S1) | **MISSING_INPUT** |
| Settled Θ_lock | **MISSING_INPUT** (worse: ≲0.11) |
| Magnitude lock via Θ path | **OPEN-BLOCKED** |
| Production A_Θ-3D | **OPEN / not stocked** |
| Bounce / \(H_\mathrm{re}\) Derived | **false / not claimed** |
| N3 COMPLETE promotion | **0** |

> **One-line:** late max 2.87 (settled 0.11) ≪ 11.71; peak≠late; production 3D False; OPEN-BLOCKED.

---

## 6. Package files

| File | Role |
|---|---|
| [`REPORT.md`](./REPORT.md) | This executive |
| [`INSTRUMENT_RUNS.md`](./INSTRUMENT_RUNS.md) | What was run / legal forms |
| [`LATE_THETA_SCORECARD.md`](./LATE_THETA_SCORECARD.md) | Layer × metric table |
| [`SURVIVORS.md`](./SURVIVORS.md) | What remains open |
| [`NON_CLAIMS.md`](./NON_CLAIMS.md) | Fences |
| [`MASTER.md`](./MASTER.md) | Stamp |
| [`logs/n3_gpe_late_theta.log`](./logs/n3_gpe_late_theta.log) | Full compute + SUMMARY_JSON |

---

## 7. Red ask

Fabrication if: peak or Madelung spikes sold as Θ_lock; spherical light unclean energy sold as production 3D; κ,γ free dial to force late~12 sold as Derived; exit 0 sold as PASS. Blue claims **0 COMPLETE**.

*NO FABRICATIONS. Construction ≠ closure. Toy turn ≠ 3D COMPLETE.*

## 5. Late-window sensitivity (F5)

See [`LATE_WINDOW_SENSITIVITY.md`](./LATE_WINDOW_SENSITIVITY.md). On best-late row: tail10=+2.87, tail20=−0.14, settled_std~1.25 — **not settled**; all ≪ Θ_lock.
