# ONE_SIDED_BC — candidate one-sided \(S_{ab}\) / \(\pi_{ab}\) and exterior \(K^+\) at re-entry

**Package:** `desk_t3_gpe_stress_sab_20260804/`  
**Domain premise P1:** Phase II is **metric-off** ⇒ exterior metric and \(K_{ab}\) exist only on metric-ON sides (Phase I exit, Phase III re-entry).  
**Red AGREE-IF (wave 3):** under P1, **\(K^-\) does not exist**; survivor M1 must be **one-sided \(K^+\)** or a medium-prescribed object replacing the missing side — not two-sided Israel across Phase II.  
**Land?** **NO.**

---

## 0. Forbidden target (killed under P1)

Standard two-sided Darmois–Israel across a single shell spanning Phase II:

\[
[K_{ab}]-[K]h_{ab}=-8\pi G\,S_{ab}
\qquad\text{with both }K^\pm\text{ defined}
\]

| | |
|---|---|
| **why forbidden here** | \(K^-\) requires a metric on the Phase-II side of \(\Sigma_\mathrm{re}\). P1 denies that metric. |
| **prior stamps** | Israel G4; C11 DEAD under P1+A; red wave-3 condition 1; `israel_sab` SURVIVORS M1 rewrite |
| **action** | **KILL** two-sided \(K^\pm\) chase as next-input under current premises |

---

## 1. Legal domain object at re-entry

At re-entry door \(\Sigma=\Sigma_\mathrm{re}\):

- **Exterior only (Phase III):** induced metric \(h_{ab}\), outward unit normal \(n^\mu\), extrinsic curvature \(K^+_{ab}=\nabla_a n_b\big|_{\Sigma^+}\).  
- **Interior (Phase II):** medium fields \((n,v,\Theta,\mathrm{Stress}_{ij})\) — **no** \(K^-\).  
- **Surface object:** either exterior surface stress \(S_{ab}\) (S-B language) **or** medium jump \(\Delta\Pi_{ab}\) (S-C language) mapped at metric return.

**Normal orientation \(\varepsilon=\pm1\)** remains a discrete label on the exterior normal; it is **not** free to be fixed by writing \(\mathrm{sign}(\Theta)\) into \(S_{ab}\) without a force-branch theorem (N4 still MISSING).

---

## 2. Candidate one-sided boundary conditions

### OS-BC1 — exterior Israel with medium-prescribed \(S_{ab}\) (S-B)

\[
\boxed{
K^+_{ab}-K^+ h_{ab}
=
-8\pi G\,S_{ab}
\quad\text{(one-sided; no }K^-\text{)}
}
\]

with \(S_{ab}\) built from medium at the gate (candidates below).  
**can-exist:** standard thin-shell BC when only one GR side is present.  
**should-not-exist as land:** \(S_{ab}\) still not Derived from GPE as *exterior* tensor; \(K^+_{ab}\) of door \(\Sigma\) still unwritten in bounce corpus (G2).  
**Forces \(H_\mathrm{re}>0\)?** **NO** — FRW still \(H=\pm\sqrt{\ldots}\); pair \((\varepsilon,\mathrm{sign} H)\) free without G5.

### OS-BC2 — medium object replaces missing side (S-C bridge)

\[
\boxed{
K^+_{ab}-K^+ h_{ab}
=
-8\pi G\,\mathcal{M}_{ab}[n,\nabla n,v]
}
\]

where \(\mathcal{M}_{ab}\) is a **prescribed medium surface object** (not an interior GR \(K^-\)):

\[
\mathcal{M}_{ab}
\sim
\Delta\Pi_{ab}
=
\int_{\mathrm{layer}}\mathrm{Stress}_{ab}\,\mathrm{d}\ell
\quad\text{(from STRESS_TENSOR.md)}
\]

**can-exist:** honest P1 replacement for the missing side; matches israel_sab C9 / SV5.  
**should-not-exist as land:** no stocked proof that \(\Delta\Pi_{ab}\) **is** exterior \(S_{ab}\); components multi-D not production-measured; homogeneous channel dies.  
**Forces \(H_\mathrm{re}>0\)?** **NO.**

### OS-BC3 — dual bookkeeping without tensor (S-A restatement)

Two-map \(\Phi_\mathrm{out}+\Phi_\mathrm{in}\) with P2 for sign — prior N2.  
**Not** an \(S_{ab}\) fill (`israel_sab` C12). Listed only to fence off rename.

---

## 3. Map: stocked Stress \(\to\) candidate surface objects

Surface ansatz (same as israel_sab §0):

\[
S_{ab}
=
\sigma_s\,u_a u_b
+p_s\,(h_{ab}+u_a u_b)
+\pi_{ab}
\]

### Map M-A — isotropic layer of interaction pressure (links SV1 / C1 family)

\[
\sigma_s^{(\mathrm{A})}
\sim
\int P_\mathrm{int}\,\mathrm{d}\ell
=
\int\tfrac12 n^2\,\mathrm{d}\ell
\sim
\tfrac12\langle n^2\rangle\,\xi
\,,\qquad
p_s^{(\mathrm{A})}=c_s^2\sigma_s^{(\mathrm{A})}\ \text{(acoustic analogy only)}
\]

**Grade:** CANDIDATE schema · dim-legal if \(n\) carries energy density scale · **not** Derived Israel · \(p_s=c_s^2\sigma_s\) is analogy not derivation.

### Map M-B — quench / Amcξ scale already stocked (SV2 / C3)

\[
\sigma_s^{(\mathrm{B})}=\tfrac12\frac{m\,c_s^2}{\xi^2}
\]

**Grade:** PAID number, DEAD as gravitational Israel land (≪ \(M_\mathrm{Pl}^2 H_\mathrm{door}\)).

### Map M-C — anisotropic \(\pi_{ab}\) from velocity / quantum shear (SV4 / C8)

\[
\pi_{ab}^{(\mathrm{C})}
\sim
\int
\Big(
n\,v_{\langle a}v_{b\rangle}
+
\Pi^\mathrm{Q}_{\langle ab\rangle}
\Big)
\mathrm{d}\ell
\]

traceless projection \(\langle ab\rangle\) on \(\Sigma\).  
**Grade:** CANDIDATE · uses stocked Stress pieces · does **not** select FRW root.

### Map M-D — full layer \(\Delta\Pi_{ij}\) as \(\mathcal{M}_{ab}\) (SV5 / C9) **primary for this desk**

\[
\boxed{
\mathcal{M}_{ab}
=
\big(\Delta\Pi_{ab}\big)^\Sigma
=
\Big(
\int_{\ell\sim\xi}
\mathrm{Stress}_{ab}[n,\nabla n,v]\,\mathrm{d}\ell
\Big)
\Big|_{\Sigma}
}
\]

with \(\mathrm{Stress}_{ab}\) from `STRESS_TENSOR.md` §3.  
**Grade:** best medium-side honesty · **still CANDIDATE** · exterior attach + \(K^+\) embedding missing · **0 land**.

### Map M-E — **KILLED** rename \(\sigma_s\propto\mathrm{sign}(\Theta)\,M_\mathrm{Pl}^2|\Theta|\)

Encodes P2 into surface density. **Forbidden as theorem** (`israel_sab` K-rename / C7 abuse).

### Map M-F — **KILLED** free \(\alpha\,\Delta\Pi\)

Free dial. **Forbidden as Derived.**

### Map M-G — **KILLED** back-solve \(S_{ab}\) from target \(H_\mathrm{re}\)

C4 tautology. **Forbidden.**

---

## 4. Exterior \(K^+\) (shared MISSING_INPUT — not filled here)

Even granting a fixed \(S_{ab}\) or \(\mathcal{M}_{ab}\):

1. Must embed \(\Sigma\) in Phase-III FRW (or anisotropic) geometry and compute \(K^+_{ab}(H_\mathrm{re},\sigma_\mathrm{re},\ldots)\).  
2. Friedmann (or shear-corrected) still supplies \(H_\mathrm{re}=\pm\sqrt{\ldots}\).  
3. OS-BC1/2 constrain **combinations** of \(K^+\) and \(S\), not the square-root branch alone.  
4. Force-branch (N4 / G5) remains **MISSING_INPUT** (`n4_force_branch_20260804`: 0 theorems).

**This desk does not invent \(K^+_{ab}\) components or \(H_\mathrm{re}\).**

---

## 5. One-sided target stamp (replaces two-sided M1)

| item | status |
|---|---|
| Two-sided \(K^\pm\) | **KILLED under P1** |
| One-sided \(K^+\) | **MISSING_INPUT** (G2) |
| Medium \(\mathcal{M}_{ab}=\Delta\Pi_{ab}\) | **CANDIDATE form written** from stocked Stress |
| Exterior \(S_{ab}\) Derived | **false** |
| N4 from one-sided BC | **false** (expected NO) |
| Derived \(H_\mathrm{re}\) | **false** |

---

*End ONE_SIDED_BC.md — P1-legal one-sided target; K^- off-limits; maps CANDIDATE only.*
