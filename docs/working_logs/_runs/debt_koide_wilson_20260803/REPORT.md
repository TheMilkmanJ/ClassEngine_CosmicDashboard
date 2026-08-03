# Debt run: Koide Branch-A Wilson holonomy — pre-registered bins + input gate

**Date:** 2026-08-03  
**Worker:** blue-team science (Grok Build subagent)  
**Debt:** D5 / T6 #101–#102 residual — Brannen phase as Wilson-line electric holonomy  
**Hard rules:** no elastic “hit 2/9”; no free knobs; if cannot run, register bins + missing inputs only; `nice -n 19`; no PolyChord / MCMC / chain touch; no false closures.  
**Claude requirement honored:** pre-registered bin widths **before** any Wilson holonomy scoring.  

**Sources:**  
- [`docs/working_logs/_runs/debt_koide_20260803/REPORT.md`](../debt_koide_20260803/REPORT.md) §3 (named next compute)  
- [`docs/working_logs/T6_koide_owed.md`](../../T6_koide_owed.md) Branch A / holonomy  
- [`docs/working_logs/T6_koide_desk_status.md`](../../T6_koide_desk_status.md)  
- [`docs/PRTOE_forced_combination.md`](../../../PRTOE_forced_combination.md)  
- [`docs/working_logs/_CANONICAL_VALUES.md`](../../_CANONICAL_VALUES.md) (δθ, n bound)  
- P-2026-051 deviation lock (σ on δθ)

**Run dir:** `docs/working_logs/_runs/debt_koide_wilson_20260803/`

---

## 0. PRE-REGISTRATION (filed FIRST — before any holonomy evaluation)

> **Status of this section:** binding. Written and committed before scoring.  
> No holonomy value was computed in this run (inputs missing — §2).  
> If a future run produces θ_W, it is scored **only** against these bins. Changing widths after seeing θ_W is forbidden.

### 0.1 What is being tested

Branch A (T6): arg b is a **Wilson-line electric holonomy** of the dark SU(2) gauge field along the family cycle in a recorded winding background — non-center (continuous), so it *can* land at non-quantized 2/9.

Observable produced by a licensed evaluation:

\[
\theta_W \;\equiv\; \text{electric holonomy angle of } A \text{ around family cycle } C
\]

(principal value on \(\mathbb{R}/2\pi\mathbb{Z}\), compared to targets mod \(2\pi\)).

**Not tested here:** re-fitting lepton masses; KMS drift with μ chosen to land 2/9; any construction that inserts 2/9 into the inputs.

### 0.2 Target centers (three discrete sheets)

| ID | Center | Value (rad) | Meaning |
|---|---|---:|---|
| **θ★₀** | \(2/9\) | **0.222222222222** | primary Brannen sheet |
| **θ★₊** | \(2/9 + 2\pi/3\) | **2.316617324615** | Z₃ sibling (+1 hop relabel) |
| **θ★₋** | \(2/9 - 2\pi/3\) | **−1.872172880171** | Z₃ sibling (−1 hop relabel) |

Sibling centers are the only Z₃ images of the primary sheet under face relabel (the three discrete outcomes named in debt_koide_20260803 REPORT §3).

### 0.3 Stated input uncertainties (sources of bin width)

These are **corpus-stated**, not invented for this run:

| Symbol | Value | Source |
|---|---:|---|
| σ_θ_mass | **8.348×10⁻⁶ rad** | T6 / P-2026-051: δθ = +7.409×10⁻⁶ ± 8.348×10⁻⁶ from pole masses |
| half-millidegree bar | **0.0005° = 8.726646×10⁻⁶ rad** | T6: “2/9 rad ± 0.0005°” mechanism landing bar |
| σ_Q | 6.8×10⁻⁶ | fence on Q; induces σ(Q/3) = 2.267×10⁻⁶ (stricter; not used as the sole width) |

**Adopted 1σ-class scale:**  
\(\sigma_\star = \max(\sigma_{\theta,\mathrm{mass}},\; \text{half-millidegree}) = \mathbf{8.726646\times 10^{-6}\,\mathrm{rad}}\).

**Adopted hit half-width (3σ, pre-registered):**

\[
W_{\mathrm{hit}} \;=\; 3\,\sigma_\star \;=\; \mathbf{2.617994\times 10^{-5}\,\mathrm{rad}}
\]

(≈ 5.40 arcsec; ≈ 0.0015°.)

**Rationale:**  
- Widths come only from stated measurement / watch uncertainties on the *target*, not from a desired mechanism success rate.  
- 3σ is the pre-committed “consistent with center” window; it is **not** elastic (a miss of ~0.01 rad is ELSE, not a widened hit).  
- \(W_{\mathrm{hit}} \ll \pi/3 \approx 1.047\), so the three centers’ hit balls are disjoint → bins mutually exclusive.

**Non-elastic rule:** if a future θ_W lands within \(10^{-3}\) of 2/9 but outside \(W_{\mathrm{hit}}\), the bin is **ELSE**, not HIT_PRIMARY. No post-hoc widening.

### 0.4 The three pre-registered bins

Define reduced distance to a center on the circle:

\[
d(\theta, \theta^\star) = \min_{k\in\mathbb{Z}} \lvert \theta - \theta^\star - 2\pi k \rvert.
\]

| Bin ID | Definition | Interpretation if scored |
|---|---|---|
| **HIT_PRIMARY** | \(d(\theta_W,\,\theta^\star_0) \le W_{\mathrm{hit}}\) | Branch A lands the Brannen sheet → crowns Branch A for #102 *as a phase source candidate* (does **not** close #101 null exactness) |
| **HIT_SIBLING** | not HIT_PRIMARY, and \(\min\bigl(d(\theta_W,\theta^\star_+),\,d(\theta_W,\theta^\star_-)\bigr) \le W_{\mathrm{hit}}\) | mechanism selects a wrong Z₃ sheet |
| **ELSE** | neither | kills Branch A *for this debt* as a 2/9 source under the zero-knob Wilson reading |

**Scoring order:** HIT_PRIMARY first, then HIT_SIBLING, else ELSE. One bin only.

### 0.5 What is *not* a registered hit

- Landing near measured θ_B = 0.2222296315 (δθ = +7.409×10⁻⁶) by fitting masses — that is the measurement table, already paid.  
- Using μ_face = (2/9) T_c, or c₂ = 4/(3 ln 2) derived from the phase, as Wilson *input* — circular.  
- Any free parameter retuned until θ_W ∈ HIT_PRIMARY.

### 0.6 Registration timestamp / artifact

- Filed in this REPORT §0 **before** §2 inventory verdict.  
- Mirrored in `scripts/koide_wilson_holonomy_inventory.py` (documentation constants only; script never scores θ_W).  
- Log: `koide_wilson_holonomy_inventory.log`.

---

## 1. What a zero-knob Wilson evaluation would require

θ_W needs, without free dials:

1. **dark SU(2) connection A_μ** on a domain containing the family triangle (or an equivalent hybrid orientational connection of non-abelian vortices — forced combination).  
2. **Closed path C** (family cycle) with **independently fixed** geometry/spacing.  
3. **Winding background** (integer n and orientation relative to C) fixed by corpus, not chosen.  
4. **Coupling / electric projection** fixed (not a band used as a dial).  
5. An evaluator that returns a continuous non-center holonomy angle (not only Z₂ center elements).

---

## 2. Input inventory — MISSING_INPUTS (proved)

Script: `nice -n 19 python3 scripts/koide_wilson_holonomy_inventory.py`  
Log: `koide_wilson_holonomy_inventory.log`  
Intended process exit on block: **2** (pipeline through `tee` may show shell 0).

| Requirement | Status | Proof |
|---|---|---|
| dark_SU2_A_μ | **MISSING** | No `data/` or `output/` dark-SU(2) gauge archive. Repo `*.npy` under `_runs/t14_*` are condensate ψ fields for H_kin, **not** dark gauge A_μ. `test_gauge_invariance*.py` are CLASS metric gauge tests, not Wilson lines. |
| family_cycle_path_C | **PARTIAL** | Equilateral topology is asserted. Bare Y/Steiner geometry gives c₂ = √3 ≈ 1.732; phase-derived c₂ = 4/(3 ln 2) ≈ 1.924 is **circular** if used to test 2/9; modulus band [1.76, 1.97] is not a fixed number. Spacing not independently fixed → zero-knob path metric unavailable. |
| winding_background_n | **MISSING** | Canonical: n ≳ 1.65 is a **bound**, not a determination; L_gen never assigned (`_CANONICAL_VALUES.md`). Widnall n ~ 11–25 is genesis vortex azimuthal structure, not a dark-gauge background on the family triangle. |
| α_d / electric projection | **PARTIAL** | α_d only **bounded** (≲ 2.2 at target spacing). Forced-combination theorem: pure-gauge ring collapses; hybrid connection is required and **not constructed** numerically. Adjoint ε^abc algebra is exact but is not a field configuration. |
| holonomy_evaluator | **MISSING** | No prior zero-knob Wilson-line script for the family cycle. Inventory deliberately does **not** invent one over missing A_μ. |

**Forbidden circular inputs (refused):**  
μ_face = (2/9)T_c; θ_hop with μ chosen to land 2/9; c₂ = 4/(3 ln 2) as geometry for a 2/9 test; fit of A_μ or path to lepton masses / arg b.

### Verdict

> **MISSING_INPUTS: 5/5 requirements block a zero-free-knob Wilson holonomy.**  
> No θ_W produced. **No bin scored.** Pre-registration (§0) stands for a future licensed run.  
> **#102 phase source: still open. OPEN-THEORY unchanged. No false closure.**

---

## 3. Explicit non-claims

This run does **not** claim:

1. That Branch A is crowned, killed, or computed.  
2. That θ_B ≈ 2/9 is *derived* (measurement table remains paid; mechanism remains open).  
3. That #101 (graded null exactness) moved.  
4. That inventing a toy A_μ or picking n ∈ [11,25] would be a licensed test.  
5. That KMS form 3·θ_B = Q *is* a Wilson-line evaluation (it is a structural identity / ansatz chain, already desk-paid as form).  
6. That pure gauge Wilson is even the right object without the hybrid connection (forced combination).  
7. Any MCMC / lattice campaign result.

---

## 4. What would unblock a licensed score

All of the following, **without** free knobs and **without** inserting 2/9 into inputs:

1. A corpus-fixed dark SU(2) (or hybrid orientational) connection on the family scale — e.g. from an external SU(2) N_f=3 lattice campaign or a derived dual-superconductor profile with **fixed** F_dark/√σ, w·√σ, not a band used as a dial.  
2. Independently derived face spacing c₂ (Y-junction screened correlator or lattice), **not** c₂ = Q/τ.  
3. Fixed winding background (n, orientation) from a completed genesis determination of L_gen, or a proof that holonomy is n-independent.  
4. Then evaluate θ_W and score §0 bins only.

Until then: **register bins + missing inputs only** (this REPORT).

---

## 5. Relation to prior debt_koide_20260803

| Prior | This run |
|---|---|
| 15 scripts re-confirmed negatives on ring-internal phase / node values | Not re-run (already paid; wall-clock budget reserved for Wilson gate) |
| Named next compute: Wilson, three discrete bins | Bins **pre-registered with widths from stated σ**; compute **blocked** on missing inputs |
| OPEN-THEORY | **Still OPEN-THEORY** |

---

## Appendix A — numerical constants (pre-registration)

```
theta_star_primary   = 2/9                    = 0.222222222222 rad
theta_star_sibling+  = 2/9 + 2π/3             = 2.316617324615 rad
theta_star_sibling-  = 2/9 - 2π/3             = -1.872172880171 rad
sigma_theta_mass     = 8.348e-6 rad
half_millidegree     = 8.726646e-6 rad
W_hit                = 2.617994e-5 rad   (= 3 * max of the two)
measured theta_B     = 0.2222296315 rad  (table only; not a Wilson score)
|theta_B - 2/9|      = 7.409e-6 rad      (< W_hit, as expected for data)
```

## Appendix B — file inventory

```
docs/working_logs/_runs/debt_koide_wilson_20260803/
  REPORT.md
  koide_wilson_holonomy_inventory.log

scripts/koide_wilson_holonomy_inventory.py   # gate only; exit 2 on MISSING_INPUTS
```
