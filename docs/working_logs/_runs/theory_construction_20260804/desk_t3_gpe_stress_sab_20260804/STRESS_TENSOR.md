# STRESS_TENSOR — explicit \(\mathrm{Stress}_{ij}[n,\nabla n,v]\) from stocked GPE / averaging

**Package:** `desk_t3_gpe_stress_sab_20260804/`  
**Prior:** `israel_sab_construction_20260804` SURVIVORS **SV5 ← C9** (M1: explicit Stress from GPE).  
**Mode:** write what is **stocked** (file:line); mark multi-D extension **CANDIDATE**.  
**Land as Derived exterior \(S_{ab}\)?** **NO.**

---

## 0. Stocked GPE (healing units)

All rebound / averaging instruments use the same repulsive GPE:

\[
i\,\partial_t\psi
=
-\tfrac12\nabla^2\psi
+
\big(|\psi|^2-1\big)\psi
\qquad
(\lambda>0)
\]

| source | lines | content |
|---|---|---|
| `scripts/bounce_m6_rebound_1d.py` | 9–10 | 1D Cartesian GPE stated |
| `scripts/bounce_rpA_scaffold.py` | 26–33 | Phase-II GPE + Madelung + averaging identity |
| `scripts/bounce_n3_gpe_late_theta.py` | 328–339, 488+ | 1D / spherical / 2D same form |
| energy functional (1D) | `bounce_m6_rebound_1d.py` 41–44 | \(E=\int\!\big[\tfrac12|\partial_x\psi|^2+\tfrac12(n-1)^2\big]\,\mathrm{d}x\) |

**Madelung dictionary (stocked scaffold):**

\[
n=|\psi|^2\,,\qquad
v=\nabla\theta\ \ (\psi=\sqrt n\,e^{i\theta})\,,\qquad
\Theta=\nabla\cdot v
\]

(`bounce_rpA_scaffold.py:28`).

**Fences:** healing units; nonrelativistic; no emergent-gravity backreaction in the medium scripts; 1D CG identity is the PAID bookkeeping instrument (not production 3D Stress components).

---

## 1. Averaging identity (stocked — PAID)

Coarse-grained mass-weighted expansion (1D exhibited):

\[
\frac{\mathrm{d}\langle\Theta\rangle}{\mathrm{d}t}
=
-\langle\Theta\rangle^2
-\mathrm{Var}(\Theta)
+\mathrm{Stress\_drive}
\]

| source | lines | note |
|---|---|---|
| `bounce_rpA_scaffold.py` | 29–32 | identity written as Phase-II skeleton |
| `bounce_averaging_decomposition.py` | 1–15, 77–85 | claim + v2 CG note |
| `bounce_reconstruction_rp.md` | §24 (~1047–1058) | exhibited numbers at turn |

**Bare-Madelung sketch (docstring, singular at cores — not the graded instrument):**

\[
\frac{\mathrm{d}\langle\Theta\rangle}{\mathrm{d}t}
=
-\langle\Theta\rangle^2
-\mathrm{Var}_\rho(\Theta)
-\big\langle\partial_{xx}(\rho+Q_\mathrm{qp})\big\rangle_\rho
\,,\quad
Q_\mathrm{qp}=-\tfrac12\frac{\partial_{xx}\sqrt\rho}{\sqrt\rho}
\]

(`bounce_averaging_decomposition.py:5–15`). v1 bare form **failed** identity check (singular cores); **v2 CG** is the stocked PAID form.

---

## 2. Explicit stocked pieces (1D CG) — \(\mathrm{Stress}\) as flux channels

From `scripts/bounce_averaging_decomposition.py` `diagnostics` (**lines 94–118**):

### 2.1 Primitive fields from \(\psi\)

| symbol | code | meaning |
|---|---|---|
| \(\rho=n=\|\psi\|^2\) | L95 | density |
| \(p_x=\mathcal{F}^{-1}(ik\,\hat\psi)\) | L96 | Fourier gradient of \(\psi\) |
| \(J=\Im(\psi^* p_x)\) | L97 | mass current \(\sim n v\) |
| \(\sqrt\rho\), \(\partial_x\sqrt\rho\) | L98–99 | amplitude gradient |
| \(\mathrm{kin\_flow}=\|p_x\|^2-(\partial_x\sqrt\rho)^2\) | L100 | \(=\rho v^2\), regular in \(\psi\) |

### 2.2 Pressure / flux scalars (stocked)

\[
\begin{aligned}
T_\mathrm{int}
&=
\tfrac12\,\rho^2
&&\text{(interaction pressure; L101)}\\[4pt]
T_\mathrm{qu}
&=
(\partial_x\sqrt\rho)^2
-\tfrac14\,\partial_{xx}\rho
&&\text{(quantum / gradient pressure proxy; L102)}\\[4pt]
\Pi_\mathrm{reyn}
&=
\mathrm{smooth}(\mathrm{kin\_flow})
-\rho_c\,v_c^2
&&\text{(sub-kernel Reynolds; L114)}
\end{aligned}
\]

with \(\rho_c=\mathrm{smooth}(\rho)\), \(J_c=\mathrm{smooth}(J)\), \(v_c=J_c/\rho_c\) (L103–106), Gaussian CG kernel \(\sigma=2\) healing lengths (L86–91).

### 2.3 Stress drive functional (stocked)

For any coarse flux scalar \(\Pi\):

\[
\mathrm{drive}(\Pi)
=
-\Big\langle
\partial_x\Big(\frac{1}{\rho_c}\,\partial_x\Pi\Big)
\Big\rangle_w
\qquad
(w=\rho_c/\textstyle\sum\rho_c)
\]

(**L111–112**). Channels:

\[
\mathrm{dr\_int}=\mathrm{drive}(\mathrm{smooth}\,T_\mathrm{int})\,,\quad
\mathrm{dr\_qu}=\mathrm{drive}(\mathrm{smooth}\,T_\mathrm{qu})\,,\quad
\mathrm{dr\_rey}=\mathrm{drive}(\Pi_\mathrm{reyn})
\]

(**L115–117**). Total stress contribution in the **identity** (red V1 cure — match code, not the intermediate name `strs`):

\[
\mathrm{Stress\_drive}
=
\mathrm{dr\_int}+\mathrm{dr\_qu}+\mathrm{dr\_rey}
\]

so that RHS \(=-\langle\Theta\rangle^2-\mathrm{Var}+\mathrm{Stress\_drive}\).

**Why not a second minus:** `drive_of` already includes the operator minus (`:112`). Intermediate `strs=-(di+dq+dr)` at `:148` is **not** the identity’s Stress_drive; `:152` uses `rhs = -ths² - vars_ - strs`, which equals `-ths² - vars_ + (di+dq+dr)`. Printed “total stress drive” at turn is `mean(-strs) = mean(di+dq+dr)` (`:170`) — positive for interaction-dominated runs.

### 2.4 Synthetic stand-in (interaction-only, FA3 / N3)

`bounce_n3_theta_lock_scan.py:245–248` and `bounce_n3_gpe_late_theta.py:787–790`:

\[
\Pi=\tfrac12\rho^2\,,\qquad
\mathrm{stress}
=
-\big\langle
\partial_x\big(\tfrac1\rho\partial_x\Pi\big)
\big\rangle_w
\]

Same operator class; omits quantum + Reynolds (static / synthetic probe).

---

## 3. \(\mathrm{Stress}_{ij}[n,\nabla n,v]\) — written form

### 3.1 What is PAID (1D = single longitudinal channel)

In the stocked 1D instruments the bulk stress is a **scalar flux** \(\Pi[n,\partial n,v]\) feeding \(\mathrm{Stress\_drive}\), not a multi-index GR surface tensor. Explicit 1D object:

\[
\boxed{
\begin{aligned}
\Pi[n,\partial_x n,v]
&=
\underbrace{\tfrac12 n^2}_{T_\mathrm{int}}
+
\underbrace{(\partial_x\sqrt n)^2-\tfrac14\partial_{xx}n}_{T_\mathrm{qu}}
+
\underbrace{
\big\langle n v^2\big\rangle_\mathrm{CG}
-
n_c v_c^2
}_{\Pi_\mathrm{reyn}}
\\[6pt]
\mathrm{Stress}
&\equiv
-\partial_x\Big(\frac1{n_c}\partial_x\Pi\Big)
\quad\text{(local operator; mass-weighted average = drive)}
\end{aligned}
}
\]

with \(n_c,v_c\) coarse-grained as above.  
**Citation:** `bounce_averaging_decomposition.py:94–118,148`.

Homogeneous fields \(\Rightarrow\) \(\mathrm{drive}\equiv0\) (reconciliation; L13–15, reconstruction §24).

### 3.2 Multi-index CANDIDATE extension (not production-stocked components)

The same energy functional in \(d\) dimensions implies a **CANDIDATE** momentum-flux tensor (Madlung Euler of the stocked GPE; **not** a separate multi-D Stress instrument in corpus):

\[
\boxed{
\begin{aligned}
\mathrm{Stress}_{ij}[n,\nabla n,v]
&=
n\,v_i v_j
+
\delta_{ij}\,P_\mathrm{int}[n]
+
\Pi^\mathrm{Q}_{ij}[n,\nabla n]
\\[4pt]
P_\mathrm{int}[n]
&=
\tfrac12 n^2
\quad\text{(matches stocked }T_\mathrm{int}\text{; healing }g=1\text{)}
\\[4pt]
\Pi^\mathrm{Q}_{ij}
&=
(\partial_i\sqrt n)(\partial_j\sqrt n)
-\tfrac14\,\partial_i\partial_j n
\quad\text{(matches stocked }T_\mathrm{qu}\text{ when }i=j=x\text{, 1D)}
\end{aligned}
}
\]

**Status:**

| piece | status |
|---|---|
| \(P_\mathrm{int}=\frac12 n^2\) | **PAID** in 1D CG / synthetic scripts |
| \(\Pi^\mathrm{Q}_{xx}\) form | **PAID** as \(T_\mathrm{qu}\) in 1D CG |
| full \(\Pi^\mathrm{Q}_{ij}\) off-diagonal / 3D | **CANDIDATE** extension of PAID 1D formula |
| Reynolds sub-kernel in multi-D | **CANDIDATE** (1D CG only stocked) |
| \(n v_i v_j\) | fluid-legal; FA1 \(v_g\) / SV4 link; not Israel-land |

**Do not claim:** multi-D production instrument has measured \(\mathrm{Stress}_{ij}\) components as exterior \(S_{ab}\).

### 3.3 Layer integral (SV5 / C9 target)

\[
\Delta\Pi_{ij}
=
\int_{\mathrm{layer}}\mathrm{Stress}_{ij}\,\mathrm{d}\ell
\sim
\mathrm{Stress}\cdot\xi
\quad\text{(healing-length layer scale; dim sketch only)}
\]

This is the **medium-side** S-C object (`israel_sab` C9). It is **not** exterior Israel \(S_{ab}\) until a metric-return map is written (see `ONE_SIDED_BC.md`).

---

## 4. What this is **not**

| claim | verdict |
|---|---|
| Stocked exterior Israel \(S_{ab}\) equation | **false** (still 0) |
| Homogeneous FRW exotic stress | **DEAD** (homogen. kills Stress channel) |
| Free coefficient \(\alpha\) on \(\Pi\) | **forbidden** |
| \(\mathrm{Stress}\propto\mathrm{sign}(\Theta)\) as theorem | **forbidden** (P2 smuggle) |
| Derived \(H_\mathrm{re}\) from \(\Pi\) | **false** |

---

## 5. Stocked numeric stamp (order-of-magnitude only)

From `bounce_reconstruction_rp.md` §24 (averaging run, turn at \(t=9.75\)):

| term | value (healing units) |
|---|---|
| stress drive | \(+0.0266\) |
| · interaction | \(+0.0261\) |
| · quantum | \(+0.0006\) |
| · Reynolds | \(-0.0002\) |
| Var oppose | \(-0.0113\) |
| net \(\mathrm{d}\langle\Theta\rangle/\mathrm{d}t\) | \(+0.0153\) |

Synthetic FA3/N3 interaction-only probe: `stress_drive ~ +0.023` order (`bounce_fa3` / N3 logs).  
**These fund medium \(\langle\Theta\rangle\) turn only** — not gravitational \(M_\mathrm{Pl}^2 H\) jump, not Derived \(H_\mathrm{re}\).

---

*End STRESS_TENSOR.md — stocked 1D Stress written; multi-D index form CANDIDATE; not exterior land.*


