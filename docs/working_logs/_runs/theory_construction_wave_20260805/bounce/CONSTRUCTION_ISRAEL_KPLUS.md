# CONSTRUCTION_ISRAEL_KPLUS — SV-KPLUS + SV-SAB-MAP

**Package:** `theory_construction_wave_20260805/bounce/`  
**Survivors:** **SV-KPLUS** · **SV-SAB-MAP** · residual T-W1d (Israel exterior gate)  
**Date:** 2026-08-05  
**Mode:** one-sided \(K^+\) construction options from stocked Stress; exterior embedding candidates; \(\Delta\Pi\to S_{ab}\) candidates; **no \(K^-\)**  
**Land this wave?** **NO** · exterior Israel eqs still **0** · \(n_\mathrm{lands}=0\)

---

## 0. Domain fences (reaffirmed)

| fence | status | cite |
|---|---|---|
| P1 Phase II metric-off | CANDIDATE premise | fa3_metric_off |
| Two-sided \(K^\pm\) across Phase II | **KILLED under P1** | desk_t3 ONE_SIDED_BC §0 |
| Chase \(K^-\) | **undefined / killed** | exhaust · red wave-3 |
| Free \(\alpha\), free \(N_\mathrm{med}\), invent \(H_\mathrm{re}\) | **KILLED** | israel_sab C4/C5 · fences |
| Stress → N4 force alone | **false** | desk_t3 · n4 |

---

## 1. Stocked Stress (carry — medium PAID, not exterior land)

Source: `desk_t3_gpe_stress_sab_20260804/STRESS_TENSOR.md`

### 1D CG bulk stress (PAID construction)

\[
\begin{aligned}
\Pi[n,\partial_x n,v]
&=
\underbrace{\tfrac12 n^2}_{T_\mathrm{int}}
+
\underbrace{(\partial_x\sqrt n)^2-\tfrac14\partial_{xx}n}_{T_\mathrm{qu}}
+
\underbrace{\langle n v^2\rangle_\mathrm{CG}-n_c v_c^2}_{\Pi_\mathrm{reyn}}
\\
\mathrm{Stress}
&\equiv
-\partial_x\Big(\frac1{n_c}\partial_x\Pi\Big)
\end{aligned}
\]

**File:line citations (stocked):**

| piece | file | lines |
|---|---|---|
| 1D GPE | `scripts/bounce_m6_rebound_1d.py` | 9–10 |
| Madelung + averaging identity skeleton | `scripts/bounce_rpA_scaffold.py` | 26–33 |
| diagnostics \(\rho,J,T_\mathrm{int},T_\mathrm{qu},\Pi_\mathrm{reyn}\), drive | `scripts/bounce_averaging_decomposition.py` | 94–118 |
| synthetic \(\Pi=\tfrac12\rho^2\) probe | `scripts/bounce_n3_gpe_late_theta.py` | 787–790 |

Multi-D index form: **CANDIDATE extension only** (not production-measured).

Layer integral (primary medium object for OS-BC2):

\[
\Delta\Pi_{ab}
=
\Big(
\int_{\ell\sim\xi}
\mathrm{Stress}_{ab}[n,\nabla n,v]\,\mathrm{d}\ell
\Big)_{\Sigma}
\]

---

## 2. SV-KPLUS — one-sided exterior embedding candidates

### 2.1 Legal domain object at re-entry \(\Sigma=\Sigma_\mathrm{re}\)

Source: desk_t3 `ONE_SIDED_BC.md` §1

- **Exterior only (Phase III):** \(h_{ab}\), outward unit normal \(n^\mu\),  
  \[
  K^+_{ab}=\nabla_a n_b\big|_{\Sigma^+}
  \]
- **Interior (Phase II):** medium \((n,v,\Theta,\mathrm{Stress})\) — **no** \(K^-\).  
- **Normal orientation** \(\varepsilon=\pm1\): discrete exterior label — **not** free to set by \(\mathrm{sign}(\Theta)\) into \(S_{ab}\) without force-branch theorem.

### 2.2 Candidate BC targets (CANDIDATE — not lands)

#### OS-BC1 — exterior Israel with medium-prescribed \(S_{ab}\)

\[
K^+_{ab}-K^+ h_{ab}
=
-8\pi G\,S_{ab}
\quad\text{(one-sided; no }K^-\text{)}
\]

| | |
|---|---|
| **can-exist** | Standard thin-shell BC with one GR side. |
| **should-not-exist as land** | \(S_{ab}\) not Derived from GPE as exterior tensor; \(K^+_{ab}\) of door unwritten (G2). |
| **forces \(H_\mathrm{re}>0\)?** | **NO** |

#### OS-BC2 — medium object replaces missing side (primary honesty)

\[
K^+_{ab}-K^+ h_{ab}
=
-8\pi G\,\mathcal{M}_{ab}[n,\nabla n,v]
\,,\qquad
\mathcal{M}_{ab}\sim\Delta\Pi_{ab}
\]

| | |
|---|---|
| **can-exist** | P1-honest replacement for missing \(K^-\); matches israel_sab C9 / SV5. |
| **should-not-exist as land** | No proof \(\Delta\Pi\equiv S_{ab}\); multi-D unmeasured; homogeneous \(\mathrm{drive}\equiv0\). |
| **forces \(H_\mathrm{re}>0\)?** | **NO** |

#### OS-BC3 — dual Φ bookkeeping without tensor

S-A restatement (N2). **Not** an \(S_{ab}\) fill. Fence only.

### 2.3 Exterior embedding construction options (what would fill \(K^+\))

These are **construction options** (MISSING_INPUT steps), not written components:

| option | description | stocked? | land? |
|---|---|---|---|
| **E-K1** | Embed \(\Sigma_\mathrm{re}\) in exterior FRW: compute \(K^+_{ab}(H_\mathrm{re},\rho_\mathrm{re},\ldots)\) from standard cosmology formulas | textbook form known; **bounce-specific \(\Sigma\) + attach data not stocked** | **NO** |
| **E-K2** | Embed in shear-corrected / anisotropic exterior; \(K^+\) includes \(\sigma_\mathrm{re}\) | R2 form paid for constraint; **embedding unwritten** | **NO** |
| **E-K3** | Thin shell at hydro-exit with induced \(h_{ab}\) from medium preferred frame | acoustic language stocked (FA1); **GR embedding map unwritten** | **NO** |
| **E-K−** | Two-sided \(K^-\) from Phase II | **FORBIDDEN under P1** | **KILLED** |

**Shared truth (desk_t3 §4):** even with fixed \(S\) or \(\mathcal{M}\),

1. Must embed \(\Sigma\) and compute \(K^+(H_\mathrm{re},\sigma_\mathrm{re},\ldots)\).  
2. Friedmann still supplies \(H_\mathrm{re}=\pm\sqrt{\ldots}\).  
3. OS-BC constrains combinations of \(K^+\) and \(S\), **not** the square-root branch alone.  
4. Force-branch (N4) remains MISSING without theorem.

**This construction does not invent \(K^+_{ab}\) components or \(H_\mathrm{re}\).**

---

## 3. SV-SAB-MAP — \(\Delta\Pi\to S_{ab}\) candidates

Surface ansatz (israel_sab §0 / desk_t3 §3):

\[
S_{ab}
=
\sigma_s\,u_a u_b
+p_s\,(h_{ab}+u_a u_b)
+\pi_{ab}
\]

### 3.1 Map catalogue from stocked Stress (CANDIDATE only)

| ID | map | form | grade | forces root? |
|---|---|---|---|---|
| **M-A** | isotropic layer int. pressure | \(\sigma_s\sim\int\tfrac12 n^2\,\mathrm{d}\ell\sim\tfrac12\langle n^2\rangle\xi\); \(p_s=c_s^2\sigma_s\) analogy | CANDIDATE schema | **NO** |
| **M-B** | quench Amcξ scale | \(\sigma_s=\tfrac12 m c_s^2/\xi^2\) | PAID number; **DEAD** as gravitational Israel land (\(\ll M_\mathrm{Pl}^2 H_\mathrm{door}\)) | **NO** |
| **M-C** | anisotropic \(\pi_{ab}\) | \(\int(n v_{\langle a}v_{b\rangle}+\Pi^Q_{\langle ab\rangle})\,\mathrm{d}\ell\) | CANDIDATE | **NO** |
| **M-D** | full layer \(\Delta\Pi\) as \(\mathcal{M}\) | \(\mathcal{M}_{ab}=(\Delta\Pi_{ab})^\Sigma\) from STRESS_TENSOR | **primary honesty** · still CANDIDATE | **NO** |
| **M-E** | \(\sigma_s\propto\mathrm{sign}(\Theta)\,M_\mathrm{Pl}^2|\Theta|\) | rename P2 into surface | **KILLED** | fake |
| **M-F** | free \(\alpha\,\Delta\Pi\) | free dial | **KILLED** | fake |
| **M-G** | back-solve \(S\) from target \(H_\mathrm{re}\) | C4 class | **KILLED** | vacuous |

Prior israel_sab C1–C12 inventory remains: exterior stocked Israel **equations: 0**; survivors C1/C3/C7/C8/C9 as schemas only (desk_t3 SURVIVORS SV1–SV5).

### 3.2 What would count as SV-SAB-MAP land

Either:

1. **Proof** that \(\Delta\Pi_{ab}\) (or named medium functional) **is** exterior \(S_{ab}\) under framework axioms, **or**  
2. **Licensed axiom** OS-BC2 with \(\mathcal{M}_{ab}\) as BC data (Rule-1 dual scrutiny; not silent COMPLETE), **and**  
3. Coupled to written \(K^+_{ab}\) embedding (SV-KPLUS), **and**  
4. Still **does not** by itself close N4 / F-A2 without further content.

**Present:** maps CANDIDATE · proof **empty** · axiom not promoted · lands **0**.

---

## 4. Shared residual order (both survivors)

| order | need | status |
|---:|---|---|
| 1 | Exterior embedding \(K^+_{ab}\) of \(\Sigma_\mathrm{re}\) | **MISSING** (SV-KPLUS) |
| 2 | Map proof \(\Delta\Pi\to S_{ab}\) **or** licensed OS-BC2 | **MISSING** (SV-SAB-MAP) |
| 3 | G5 / T-N4-\* force-branch **or** keep P2 declaration | force **false** (SV-N4-THM) |
| 4 | Orthogonal F-A2 / Θ / O6 | other SVs |

**Writing Stress does not close N4. Writing OS-BC forms does not invent \(K^+\).**

---

## 5. Grade

| field | value |
|---|---|
| **SV-KPLUS** | **MISSING_INPUT · embedding candidates listed · \(K^-\) killed** |
| **SV-SAB-MAP** | **CANDIDATE maps only · proof empty** |
| Stress 1D | **PAID** (medium construction) |
| exterior Israel eqs | **0** |
| \(n_\mathrm{lands}\) | **0** |
| FORCE from Stress | **false** |

### One-liner

> **SV-KPLUS/SAB: one-sided OS-BC1/2 and maps M-A–M-D restated from stocked Stress; embedding \(K^+\) still unwritten; \(\Delta\Pi\to S_{ab}\) unproved; \(K^-\) off-limits; lands 0.**

---

*NO FABRICATIONS. No \(K^-\). Stress ≠ exterior land. Leave MCMCs.*
