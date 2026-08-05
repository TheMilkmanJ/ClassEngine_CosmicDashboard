# Settled late-Θ residual (F5 deepen) — 2026-08-04

**Package:** `docs/working_logs/_runs/theory_construction_20260804/settled_late_theta_20260804/`  
**Seat:** Grok blue  
**Prior:** `n3_gpe_late_theta_20260804` (F5: best-late tail10=+2.87, tail20=−0.14, settled_std~1.25)  
**Script:** `scripts/bounce_settled_late_theta_scan.py`  
**Log:** [`logs/settled_late_theta_scan.log`](./logs/settled_late_theta_scan.log) · [`logs/summary.json`](./logs/summary.json)  
**Form:** **FA3 0D only** — \(\dot n=-n\Theta\), \(\dot\Theta=-\Theta^2+\kappa(n-1)-\gamma\Theta\)  
**Fences:** no invent \(H_\mathrm{re}\) · no free dial · leave MCMCs · no PolyChord · `page_curve_claimed=false` · exit 0 ≠ PASS · `production_3d=false`

**COMPLETE:** **0** — grade **OPEN-BLOCKED**  
**Production 3D COMPLETE?** **False** (0D instrument)

---

## 0. One-liner

**S1_settled (last-20% mean after long settle, std&lt;0.2) maxes at +0.0436 under stocked 0D — 3.7×10⁻³ of Θ_lock=11.71. Unique physical fixed point (n,Θ)=(1,0) ⇒ ring-down always drives settled_mean→0 for γ&gt;0. Prior +2.87 was re-entry tail10 window-choice, not stable late ⟨Θ⟩.**

---

## 1. Mission (red F5 residual)

Red F5: the prior package ranked 710 rows by `late_tail10` (re-entry last 10%). On the winning row:

| window | value |
|---|---:|
| late_tail10 (headline) | **+2.8701** |
| late_tail20 (same run) | **−0.1364** |
| settled_std | **~1.25** |

Sign is window-dependent; ring-down not settled. This package:

1. Defines **S1_settled** = `settled_mean` (last 20% of full Θ history after `settle_extra`).  
2. Optional quality cut: `settled_std < 0.2`.  
3. Re-scans stocked 0D for **max settled positive Θ** (with quality cut).  
4. Documents analytic + numeric proof that ring-down drives settled → O(0.1) or below.  
5. Compares to **Θ_lock = 11.706… = 1/√α** (d=3).

---

## 2. S1_settled definition

| label | definition | role |
|---|---|---|
| **S1_settled** | integrate past re-entry cut \(t_{n_\mathrm{peak}}+8\) by `settle_extra`; **mean of last 20%** of full Θ history | **primary lock metric** |
| quality cut | `settled_std < 0.2` on that same tail | optional honesty gate |
| late_tail10 / late_tail20 | re-entry-window only (no long settle) | F5 diagnostic, **not** S1 here |
| peak \(\max\Theta_+\) | diagnostic only | **not S1** |

Primary scan uses **`settle_extra=40`**, `dt=1e-3`. Secondary scan `settle_extra=20` (prior phase-2 comparable).

---

## 3. Anchors (this run)

| quantity | value |
|---|---:|
| \(c_s=\sqrt{3\alpha}\) | 0.14796 |
| \(\Theta_\mathrm{lock}\) (d=3) | **11.70623765** (=1/√α) |
| \|H_kin(Θ=1)\|/H_door | 0.08542454 |
| dt | **1e-3** |
| script sha256 | `950d68ac22b76d2e…271fe380` |
| stocked default (6,−2,1.5,0.15) se=0 tail10 | **+0.061225** |
| stocked default se=40 settled | **−0.003680** (std=0.0315, quality OK) |
| prior F5 row se=0 tail10 / tail20 | **+2.8701 / −0.1364** |
| prior F5 row se=40 settled | **−0.0582** (std=1.099, quality **FAIL**) |
| **max S1_settled quality se=40** | **+0.043582** |
| max S1_settled all-physical se=40 | +0.10560 (std=0.472, quality FAIL) |
| max S1_settled quality se=20 | +0.04195 |
| ratio quality S1_settled / Θ_lock | **3.72×10⁻³** |
| S1_settled ≥ lock? | **NO** |
| production_3d | **False** |

---

## 4. Scan results (stocked FA3 0D)

Grid identical in spirit to `bounce_n3_gpe_late_theta.scan_0d_deep` (axes A–D, 710 unique rows).

### 4.1 Primary: settle_extra=40

| metric | value |
|---|---:|
| unique / physical / quality | 710 / 685 / **364** |
| turned / blowups | 678 / 25 |
| **max quality S1_settled** | **+0.043582** |
| max all-phys S1_settled | +0.105600 |
| max re-entry late_tail10 | +2.8701 (same F5 row) |
| settled ≥ lock | **False** |

**Argmax quality (headline):**  
\((n_0,\Theta_0,\kappa,\gamma)=(3,-1,1.0,0.05)\)  
→ settled=**+0.04358**, std=0.184, tail10=+0.717, tail20=+0.643, peak≈1.10.

**Argmax all-physical (fails quality):**  
\((6,-2,1.0,0.02)\) → settled=+0.1056, std=**0.472** (residual ring-down).

**Argmax re-entry late_tail10 (F5 residual stamp):**  
\((80,-8,3,0.02)\) → tail10=+2.87, tail20=−0.14, settled@40=**−0.058**, std=1.10 — **quality FAIL**; not a positive settled land.

### 4.2 Secondary: settle_extra=20

| metric | value |
|---|---:|
| physical / quality | 685 / 193 |
| max quality S1_settled | **+0.04195** @ (20,−8,2.0,0.15) |
| max all-phys S1_settled | +0.319 (std large; quality FAIL) |

Quality ceiling stays **O(0.04)** — still ≪ 11.71.

### 4.3 Stocked default stamp

| settle_extra | tail10 | settled_mean | settled_std | quality |
|---:|---:|---:|---:|---|
| 0 | +0.0612 | +0.2813 | 0.254 | FAIL |
| 20 | +0.0612 | +0.00203 | 0.114 | OK |
| 40 | +0.0612 | **−0.00368** | 0.0315 | OK |
| 80 | +0.0612 | −0.00017 | 0.00248 | OK |
| 160 | +0.0612 | **+8.6×10⁻⁷** | 1.6×10⁻⁵ | OK |

Fixed-point approach: \(n_\mathrm{late}\to 1\), \(\Theta\to 0\).

---

## 5. Ring-down: always → O(0.1) or below?

### 5.1 Analytic (stocked form) — red AGREE-IF cure

**Exact identity (any κ, γ, any IC — not linearization):** from \(\dot n=-n\Theta\),
\[
\Theta=-\frac{\mathrm{d}}{\mathrm{d}t}\ln n
\quad\Rightarrow\quad
\langle\Theta\rangle_{[t_1,t_2]}=\frac{\ln n(t_1)-\ln n(t_2)}{t_2-t_1}.
\]
Window-mean Θ **is** the log-density drop over the window. To get \(\langle\Theta\rangle=\Theta_\mathrm{lock}\approx11.71\) over a ~10-unit window needs \(n\) to fall by \(\sim10^{50}\) in that window — **grid-independent** bar; boundary argmax does not help.

**Fixed point:** unique physical equilibrium \((n,\Theta)=(1,0)\).  
**Local** linearization (κ,γ&gt;0): \(\mathrm{Re}(\lambda)=-\gamma/2\) on the underdamped branch of this grid — **local** asymptotic stability only.  
**Honest claim (not overreach):** under stocked form with γ&gt;0, trajectories approach \((1,0)\); finite-window S1_settled on this legal scan stays **O(0.1) or below** (numeric §5.2–5.3). Positive quality maxima are **leftover density drift** across the window (\(\Delta\ln n\neq0\)), not a non-zero late attractor.

| (κ, γ) | rate γ/2 | regime | t to 1% amplitude |
|---:|---:|---|---:|
| (1.5, 0.15) stocked | 0.075 | underdamped | ~61 |
| (3.0, 0.02) F5 corner | 0.010 | underdamped | ~461 |
| (1.5, 0.50) | 0.250 | underdamped | ~18 |
| (5.0, 0.10) | 0.050 | underdamped | ~92 |

Tiny-γ corners ring down slowly — residual O(0.1) at finite settle is **damped oscillation**, not a stable positive late mean.

### 5.2 Numeric ladders

- **Stocked default:** settled_mean sequence se=0→160: +0.28 → +0.07 → +0.002 → −0.004 → −0.0002 → **~0**.  
- **Prior F5 best-late (γ=0.02):** se=0→160 settled: −0.14 → +0.06 → +0.11 → −0.06 → −0.02 → **+0.013** (std still 0.35 at se=160 — quality FAIL; rate γ/2=0.01 needs ~460 time units for 1%). Mean stays **O(0.1) or below** at every step; never approaches lock.

### 5.3 Scan envelope

Across 685 physical rows at se=40: max settled (all-phys) = **+0.106**; max quality = **+0.044**. Both **O(0.1) or below**, ratio to lock ≤ **9×10⁻³** (all-phys) / **3.7×10⁻³** (quality).

**Verdict on Q3:** Yes — under stocked FA3 0D with γ&gt;0, ring-down drives settled_mean → 0, and finite-window maxima stay O(0.1) or below on this legal grid. Not a free-parameter land of Θ~12.

---

## 6. Compare to Θ_lock = 11.71

| readout | value | / Θ_lock | lock? |
|---|---:|---:|---|
| prior re-entry late_tail10 max | +2.870 | 0.245 | NO |
| prior F5 row S1_settled se=40 | −0.058 | — | NO |
| **this package max quality S1_settled** | **+0.0436** | **0.00372** | **NO** |
| max all-phys S1_settled se=40 | +0.106 | 0.00902 | NO |
| stocked default S1_settled se=40 | −0.00368 | — | NO |
| Θ_lock | 11.706 | 1 | target |

\|H_kin(settled_max)\|/H_door = **0.00372** ≪ 1.

---

## 7. Grade stamp

| claim | grade |
|---|---|
| Toy 0D ⟨Θ⟩ turn under legal stress | **PAID** (stocked default turns) |
| Stable positive late ⟨Θ⟩ near lock | **DEAD** under stocked form |
| S1_settled ≳ 11.7 | **MISSING_INPUT** |
| Prior +2.87 as settled late | **DEAD** (F5; window-choice) |
| Ring-down → O(0.1) or below | **DOCUMENTED** (analytic + scan) |
| Magnitude lock via Θ path | **OPEN-BLOCKED** |
| Production 3D / bounce / \(H_\mathrm{re}\) | **false / not claimed** |
| COMPLETE | **0** |

> **One-line:** max quality S1_settled **+0.0436** ≪ 11.71; FP (1,0) forces ring-down; F5 residual closed as documentation; OPEN-BLOCKED.

---

## 8. Package files

| File | Role |
|---|---|
| [`REPORT.md`](./REPORT.md) | This executive |
| [`SCORECARD.md`](./SCORECARD.md) | Metric table vs lock |
| [`SURVIVORS.md`](./SURVIVORS.md) | What remains open |
| [`NON_CLAIMS.md`](./NON_CLAIMS.md) | Fences |
| [`MASTER.md`](./MASTER.md) | Stamp |
| [`logs/settled_late_theta_scan.log`](./logs/settled_late_theta_scan.log) | Full compute + SUMMARY_JSON |
| [`logs/summary.json`](./logs/summary.json) | Machine-readable summary |

---

## 9. Red ask

Fabrication if: re-entry tail10 sold as S1_settled; quality-fail rows sold as settled lands; κ,γ free-dialed to force settled~12 sold as Derived; exit 0 sold as PASS; 0D sold as production 3D. Blue claims **0 COMPLETE**.

*NO FABRICATIONS. Construction ≠ closure. Window-choice ≠ settled late. exit0 ≠ PASS.*
