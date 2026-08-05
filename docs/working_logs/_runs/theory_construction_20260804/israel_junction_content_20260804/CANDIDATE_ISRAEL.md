# CANDIDATE Israel / acoustic surface-stress statement (under P1+P2)

**Package:** `israel_junction_content_20260804/`  
**Domain:** only under licensed premises **P1** (metric-off at \(\xi\)) + **P2** (expanding root at gate) from `fa3_metric_off/CONSTRUCTION.md`.  
**Grade of this note:** **CANDIDATE formalization of a MISSING_INPUT** — not Derived, not stocked \(S_{ab}\), not bounce closed.

---

## 0. Purpose

N2 left R3 as empty. This file writes the **honest candidate shape** of an Israel-class or acoustic surface-stress statement that *could* fill R3/N4 — under the **same domain fences** as the match-book — so future work has a target instead of a vague word.

It does **not** supply the missing tensor or theorem.

---

## 1. Premises (domain — do not smuggle past)

| ID | premise | status |
|---|---|---|
| **P1** | At scales \(\sim\xi\), exterior metric description **ends**. Phase II: no exterior \(H\), no exterior Friedmann | CANDIDATE licensed |
| **P2** | When \(\langle\Theta\rangle>0\) and \(\ell_\mathrm{grad}\gtrsim\xi\), attach expanding FRW root \(H_\mathrm{re}=+\sqrt{8\pi G\rho_\mathrm{re}/3+\sigma_\mathrm{re}^2/3}\) | CANDIDATE declaration |
| **Fences** | No free \(N_\mathrm{med},\eta\) as Derived; no continuous metric-ON \(H\) through 0; no invent \(H_\mathrm{re}\) number | absolute |

If P1 is withdrawn → obstruction A kills continuous exterior cross; classical Israel thin-shell **across** a finite-\(\rho\) \(H=0\) would be a *different* silhouette (not this note’s domain).

---

## 2. Why classical single-shell Israel does **not** already apply

Standard Israel / Darmois–Israel matching:

- two exterior Lorentzian regions \(\mathcal{M}^\pm\) with metrics \(g^\pm\);
- common hypersurface \(\Sigma\) with continuous induced metric \(h_{ab}\);
- jump of extrinsic curvature \([K_{ab}]-[K]h_{ab}=-8\pi G\,S_{ab}\).

**Under P1:**

1. Phase II is **non-metric**. There is no continuum exterior \(g\) through the interval.  
2. Contracting exterior (Phase I end) and expanding exterior (Phase III start) are **not** glued by a thin shell that sits *inside* a single Lorentzian spacetime spanning both.  
3. Therefore a **single** Israel sheet connecting \(H<0\) to \(H>0\) **across Phase II** is **ill-posed** in the RP-A silhouette — not because GR forbids thin shells, but because the intermediate region has **no exterior metric** to host \(\Sigma\).

**Conclusion (domain):** “Israel across Phase II” cannot mean one continuous metric thin shell. Any honest candidate must be one of the shapes in §3.

---

## 3. Candidate statement shapes (only forms that respect P1+P2)

### Shape **S-A** — Two acoustic junctions (exit + re-entry)

> **S-A.** Matching is **two** one-sided maps, not one shell:  
> (i) **Exit map** \(\Phi_\mathrm{out}\): Phase I exterior \((g,H<0,\rho,\sigma)\) \(\to\) medium \((n,v,\Theta,\ldots)\) at door \(\ell\sim\xi\).  
> (ii) **Re-entry map** \(\Phi_\mathrm{in}\): medium state with gate \(\langle\Theta\rangle>0\wedge\ell_\mathrm{grad}\gtrsim\xi\) \(\to\) Phase III exterior \((g,H_\mathrm{re},\rho_\mathrm{re},\sigma_\mathrm{re})\).  
> Surface stress language, if used, means **boundary conditions on each acoustic interface**, not \([K]\) across a metric Phase II.

**Stocked half:** forward acoustic / FA1 medium table (exit *direction* partial); kinematic \(H_\mathrm{kin}\) map when metric on.  
**Missing half:** unique inverse at exit; SM photon corner; \(\rho_\mathrm{re}\) law; **force** of expanding root without P2.

**Grade:** RECONSTRUCTED-PARTIAL bookkeeping already (N2 dict). **Does not** promote P2 → Derived.

### Shape **S-B** — Israel **only** on metric-ON sides of the doors

> **S-B.** If future work defines spacelike \(\Sigma_\mathrm{exit}\) (end of Phase I) and \(\Sigma_\mathrm{re}\) (start of Phase III) as **boundaries of exterior metric regions only**, then Israel-class  
> \[
> [K_{ab}]-[K]h_{ab}=-8\pi G\,S_{ab}
> \]
> may be written **on each** \(\Sigma\), with \(S_{ab}\) the surface stress of the medium / quasiparticle layer as seen from the exterior.  
> Phase II remains medium ODE; no \([K]\) evaluated *through* metric-off.

**can-exist:** literature-legal thin shells at each boundary.  
**should-not-exist until:** stocked \(S_{ab}(n,v,\Theta,\ldots)\) and \(K_{ab}\) from door geometry.  
**Present:** **MISSING_INPUT** (zero stocked \(S_{ab}\), zero stocked \(K_{ab}\) of \(\Sigma_\mathrm{re}\)).

### Shape **S-C** — Acoustic surface stress as medium stress jump (no exterior \(K\))

> **S-C.** Define a preferred-frame “surface” at re-emergence by \(\ell_\mathrm{grad}\sim\xi\), and a **medium** stress discontinuity  
> \[
> \Delta \Pi_{ij} = \text{(interaction + quantum pressure integrated across the layer)}
> \]
> used only as a **matching target** for exterior \(\rho_\mathrm{re},\sigma_\mathrm{re}\) once metric returns — still with P2 for sign of \(H\).

**Relation to stocked parts:** averaging identity supplies **bulk** stress drive for \(\langle\Theta\rangle\), not a derived surface \(\Delta\Pi_{ij}\) for exterior attach.  
**Grade:** sketch · **MISSING_INPUT** for exterior attach.

### Shape **S-D** — Force-branch theorem (N4 target)

> **S-D (N4).** Theorem: under P1 + legal medium stress + acoustic re-emergence, the **only** consistent exterior attachment is the expanding root  
> \(H_\mathrm{re}>0\), **without** free choice of square-root branch.  
> Dual: a proof that the contracting root is inconsistent with \(\langle\Theta\rangle>0\) and achronality (M4).

**can-exist:** highest honesty upgrade of P2.  
**should-not-exist as fake:** restating P2; assuming expanding FRW in the premise; reopening continuous metric-ON H-cross.  
**Present:** **not stocked** — see [`GAP_LIST.md`](./GAP_LIST.md).

---

## 4. Candidate **surface stress** statement (honest emptiness)

**What one would need to write (not claimed stocked):**

On a spacelike re-entry surface \(\Sigma_\mathrm{re}\) (S-B),

\[
S_{ab} = \sigma_s\,u_a u_b + p_s\,(h_{ab}+u_a u_b)+\ldots
\]

with \(\sigma_s,p_s\) functions of medium \((n,\Theta,\ell_\mathrm{grad})\) at gate, such that Israel jump plus exterior Friedmann **determine** \((H_\mathrm{re},\rho_\mathrm{re})\) uniquely including **sign**.

**Corpus status of every factor:**

| factor | status |
|---|---|
| \(\Sigma_\mathrm{re}\) as geometric object with \(K_{ab}\) | **not written** |
| \(S_{ab}\) components from GPE/hydro | **not written** |
| Uniqueness of expanding root | **not written** (P2 declaration fills gap) |
| Consistency with M4 achronality | **constraint only** (B-1…B-3 inventory) |
| Magnitude lock with \(H_\mathrm{kin}\) | **OPEN** (obstruction C) |

**CANDIDATE one-liner (S-A + P2, current honest content):**

> Under P1+P2, “junction” means **exit map + medium evolution + re-entry map**; expanding root is **declared** at gate; **no** stocked Israel \(S_{ab}\) forces that root or fixes \(\rho_\mathrm{re}\).

---

## 5. Acoustic surface stress (what *is* partially stocked)

Not Israel, but real:

1. **Door is a quench** for \(x\lesssim x^*\) (FA1) — modest medium energy injection; **fails** MeV (`task5_door_budget`).  
2. **Averaging stress** drives \(\langle\Theta\rangle\) turn — **bulk**, Phase II fluid.  
3. **\(v_g>c_s\)** ends metric trust — operational end of Phase I, not \(S_{ab}\).  
4. **M4 spacelike condition** bounds contrasts on the door — **causal character**, not surface energy density.

These do **not** assemble into \(S_{ab}\) or N4.

---

## 6. Explicit non-promotions

| claim | allowed? |
|---|---|
| This note stocks Israel content | **no** |
| P2 becomes Derived-sign by renaming | **no** |
| Continuous exterior H-cross via thin shell at finite \(\rho\) without new premises | **no** (A still stands unless S-B filled) |
| \(N_\mathrm{med},\eta\) enter \(S_{ab}\) as Derived | **no** |
| Bounce / cyclic closed | **no** |

---

## 7. Promotion condition (when this CANDIDATE becomes real content)

Promote R3 from MISSING_INPUT only if **all** hold:

1. Written \(S_{ab}\) or medium \(\Delta\Pi_{ij}\) from **legal** GPE/hydro parts (no free dials);  
2. Written \(K_{ab}\) (or acoustic surrogate) on \(\Sigma_\mathrm{exit}\) and/or \(\Sigma_\mathrm{re}\);  
3. Matching equations closed under P1 domain (no Phase-II exterior \(H\));  
4. Either N4 force of expanding root **or** honest retention of P2 as axiom with that label;  
5. Magnitude / \(\rho_\mathrm{re}\) either closed (F-A2) or **explicitly** left OPEN (not smuggled).

**None of (1)–(4) are stocked. (5) OPEN stands.**

---

*End CANDIDATE_ISRAEL.md*
