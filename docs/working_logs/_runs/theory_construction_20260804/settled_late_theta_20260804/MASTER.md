# Settled late-Θ F5 deepen — MASTER stamp

| field | value |
|---|---|
| package | `settled_late_theta_20260804` |
| prior | `n3_gpe_late_theta_20260804` (F5 residual) |
| date | 2026-08-04 |
| form | **FA3 0D only** |
| S1 metric | **S1_settled** = mean(last 20% after settle_extra) |
| quality cut | settled_std &lt; 0.2 |
| grade | **OPEN-BLOCKED** |
| COMPLETE | **0** |
| toy ⟨Θ⟩ turn | **PAID** (stocked 0D) |
| **max quality S1_settled** | **+0.04358** |
| argmax quality | (n0=3, Θ0=−1, κ=1.0, γ=0.05), se=40 |
| max all-phys S1_settled | +0.1056 (std=0.47, quality FAIL) |
| stocked default se=40 settled | −0.00368 |
| prior F5 tail10 / tail20 | +2.870 / −0.136 |
| Θ_lock | **11.706** |
| S1_settled / Θ_lock | **3.72×10⁻³** |
| \|H_kin(settled)\|/H_door | **3.72×10⁻³** |
| Θ_lock reached (settled)? | **NO** |
| ring-down → O(0.1) or below? | **YES** (FP (1,0) + scan) |
| S1 | **MISSING_INPUT** |
| production 3D COMPLETE? | **False** |
| page_curve_claimed | **false** |
| dt | 1e-3 |
| script | `scripts/bounce_settled_late_theta_scan.py` |
| script_sha256 | `950d68ac22b76d2e1eb4ff57d4842e727af6455811c564820e1b184c271fe380` |
| log | `logs/settled_late_theta_scan.log` |
| summary | `logs/summary.json` |

*NO FABRICATIONS. Construction ≠ closure. Window-choice ≠ settled late. Peak ≠ S1. exit0 ≠ PASS.*

**F5 reading (this package):** S1_settled supersedes late_tail10; max quality settled **+0.0436** ≪ lock; prior +2.87 is not a stable positive late ⟨Θ⟩. COMPLETE 0 unchanged.
