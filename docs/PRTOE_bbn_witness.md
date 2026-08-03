# BBN — light elements as a witness of the electron-mass ramp

Glossary: [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md). Conditionality: [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md). Full D/H decomposition: [PRTOE_deuterium_row.md](PRTOE_deuterium_row.md).

Nucleosynthesis is the only “lab” that watches the electron-coupled scalar’s phase transition live: **T_c = 177.10 keV** sits inside the BBN temperature window. Three abundances are three views of the same ramp.

**Audience grade.** Sector is **rigid** (no free BBN knobs) and **net adverse** under the standing high-f configuration. Nuclear systematics (d(d,n)³He) dominate the absolute D/H σ; model still trails its own ΛCDM control by ~0.6–0.7σ. Do not present BBN as a win.

---

## Equations and stamps

**Ramp.** ε(T) = ε · (1 − T/T_c) with **T_c = 177.10 keV** (Koide τ = ½ln2). 193 keV is the perturbative cross-check only. Production splices often used **179 keV** and ε = 1.24%. Scans through the nuclear network price the move:

| change | Δ(D/H) |
|---|---|
| T_c 179 → 177.10 | −0.0036σ ± 0.0013 |
| ε 1.24% → 1.2543% | +0.0035σ ± 0.0004 |
| both | **~0 within ±0.0014σ** |

Re-keying the ramp onto the scalar’s own thermal band (307–714 keV) is excluded by abundances (He +0.5–1.4σ, D up to +0.8σ). Onset is pinned near 177 keV by data, not convention. Scripts: `prym_supersession_pricing.py`, `prym_ramped_splice.py`.

**Epoch weights (coded T_c ≈ 179 keV stamps; 177.10 nearly identical):**

| epoch | T | ε weight |
|---|---|---|
| n/p freeze-out | ~800 keV | **0** (above T_c) |
| D bottleneck | ~70 keV | **0.61ε** |
| Li | ~40 keV | **0.78ε** |

---

## Two runs (do not mix absolute D/H)

D/H ∝ ω_b^(−1.66) in production — most baryon-sensitive abundance. Relative window effects and absolute predictions use different baselines.

### (i) Window effect only (PRyM default ω_b)

T_c = 179 keV, ε = 1.24%. Licenses **relative** shifts only:

| | Y_p | D/H ×10⁵ | ⁷Li/H ×10¹⁰ |
|---|---|---|---|
| baseline (ε=0) | 0.246891 | 2.4545 | 5.4387 |
| active window | 0.248995 | 2.4703 | 5.4530 |
| **window effect** | **+0.852%** | **+0.645%** | **+0.263%** |

### (ii) Model prediction (model ω_b)

CMB m_e–ω_b degeneracy pulls ω_b **+1.1%** vs in-house ΛCDM control:

> ΛCDM control **2.420** → (+1.1% ω_b) **2.372** → (+0.645% window) → **D/H = 2.387×10⁻⁵**

Cooke: 2.527 ± 0.030. Model sits **low** — self-adverse.  
**P-2026-027** (radio D/H) decides observation; **P-2026-058** (d(d,n)³He) decides theory side (larger).

Decomposition: ω_b step −1.01σ; window **+0.31σ** (nuclear physics helps). Same ω_b shift buys H₀ → trade **0.59σ D per km/s/Mpc**. Detail: [PRTOE_deuterium_row.md](PRTOE_deuterium_row.md).

---

## Helium and widths

- Window alone: Y_p **+1.09σ** vs Aver 0.2453 ± 0.0034; **+3.5σ** vs EMPRESS 0.2370 ± 0.0034. Baseline-robust (Y_p ∝ ω_b^0.04 → +1.12σ at model ω_b).
- Standing D/H width: Cooke ±0.030 ⊕ PRIMAT post-LUNA ±0.037 = **±0.0476** → 2.387 at **−2.94σ** before dark-radiation residual. Do **not** triple-count LUNA d(p,γ).
- Inter-code spread PRIMAT 2.439 vs PArthENoPE 2.51–2.54 (~3.5%) **not** folded above; half/full fold → −2.2σ / −1.4σ. Model runs **PRyM**. ΛCDM itself ~1.85σ under PRIMAT.

---

## Dark-radiation residual (ζ)

High-f config: ζ = T_dark/T_γ ∈ [0.25, 0.35] → **ΔN_eff = 0.06–0.24** (structure from 27→14 dof at T_c; ζ is the un-derived ratio, Planck-located ~0.31).

| | without residual | with ζ window |
|---|---|---|
| D/H | 2.387×10⁻⁵ (−2.94σ) | 2.407–2.463 (−2.5…−1.4σ class) |
| Y_p vs Aver | +1.1σ | **+1.3…+2.0σ** |
| Y_p vs EMPRESS | | **+3.8…+4.4σ** |

Residual larger **below** T_c (reheat (27/14)^{1/3}). Helium set above T_c; deuterium below — different residual. Joint **p ≈ 0.02–0.08** (estimate; linear responses).

**Falsifier:** CMB-S4 must see ΔN_eff in ~0.06–0.24 (P-2026-053). ΔN_eff(BBN) ≈ ΔN_eff(CMB) — cannot dump extra dark radiation before recombination without violating DM density or FIRAS.

---

## Joint and open questions

Verdict hinges on **nuclear-code / d(d,n)³He systematic**, not on a free BBN parameter. Dark-radiation residual eases D without healing it and makes He worse.

Owned adverse content that survives every rate compilation: **model − ΛCDM control ≈ 0.6–0.7σ on D/H**.

No heal available to the electron-coupled scalar for quarks (leptophilic by data). Missing electromagnetic injector for late D production is not in the field content ([PRTOE_deuterium_row.md](PRTOE_deuterium_row.md) §5–6).

---

## Sources

PRyM pipeline scripts under `scripts/prym_*.py`. Predictions: P-2026-027, P-2026-053, P-2026-058. Risk summary: [PRTOE_READERS_RISK.md](PRTOE_READERS_RISK.md).
