# CANDIDATE_SAB — surface stress \(S_{ab}\) from stocked medium quantities only

**Package:** `israel_sab_construction_20260804/`  
**Prior:** `israel_junction_content_20260804` — **0** stocked Israel \(S_{ab}\) equations; gaps **G1–G12**.  
**Protocol:** Rule 1 — each entry is **CANDIDATE** on entry; written **can-exist** + **should-not-exist**; no free dial as Derived; no invent \(H_\mathrm{re}\) as Derived.  
**Domain:** S-B (Israel only on metric-ON sides of doors) or S-C (acoustic surface stress as medium jump). Single-shell across Phase II remains **ill-posed under P1** (prior G4).  
**Land?** **NO** (construction maps only).

---

## 0. Target form

On a spacelike door surface \(\Sigma\) (exit and/or re-entry) with induced metric \(h_{ab}\) and unit normal \(n^\mu\) (exterior side):

\[
[K_{ab}]-[K]h_{ab}=-8\pi G\,S_{ab}
\quad\text{(Israel / Darmois–Israel — not stocked as bounce law; target only)}
\]

**Surface stress ansatz (perfect fluid + optional anisotropic piece):**

\[
S_{ab}
=
\sigma_s\,u_a u_b
+p_s\,(h_{ab}+u_a u_b)
+\pi_{ab}
\]

with \(\sigma_s\) = surface energy density, \(p_s\) = surface pressure, \(\pi_{ab}\) = traceless anisotropic stress (optional).  
**Mass dimension in \(\hbar=c=1\):** \([\sigma_s]=[p_s]=\mathrm{eV}^3\) (energy/area).

**Stocked inputs allowed (only):**

| symbol | meaning | stocked? | dim (nat.) |
|---|---|---|---|
| \(n\) | medium density (GPE \(\|\psi\|^2\) / stand-in) | toy PAID | model-dep. (often 1) |
| \(v\) | medium velocity | FA1 / fluid | 1 (\(c=1\)) |
| \(\Theta\) | expansion scalar | fluid PAID | heal: 1; phys: eV |
| \(c_s=\sqrt{3\alpha}\) | sound speed | PAID | 1 |
| \(\xi\) | healing length | PAID (402 AU anchor) | eV\(^{-1}\) |
| \(\rho_\mathrm{bounce}=m^4/\lambda\) | floor density | PAID | eV\(^4\) |
| \(\rho_\mathrm{eff},H_\mathrm{door},\sigma_\mathrm{door}\) | shear-door anchors | PAID | eV\(^4\), eV, eV |
| \(m\) | medium mass scale | PAID (\(2.24\times10^{-20}\,\mathrm{eV}\)) | eV |
| \(M_\mathrm{Pl}\) | Planck mass | PAID | eV |
| FA1 \(\varepsilon,v_g,x^*\) | medium table | PAID partial | 1 |
| averaging Stress | bulk \(\langle\Theta\rangle\) drive | PAID identity class | eV\(^2\) class (bulk) |

**Forbidden as inputs to a land:** free \(\alpha,\eta,N_\mathrm{med}\); target \(H_\mathrm{re}\) used to back-solve \(S_{ab}\) (C4); Phase-II exterior \(H\); invent \(\rho_\mathrm{re}\) as Derived.

---

## 1. Dimensional legal atoms for \(\sigma_s\)

Any honest \(\sigma_s\) from stocked parts must be built from **eV³-legal** atoms:

| atom | expression | dim OK? | stocked meaning |
|---|---|---|---|
| Aρξ | \(\rho_\star\,\xi\) | yes | layer-integrated bulk density over healing length |
| AρH | \(\rho_\star/H_\mathrm{door}\) | yes | integrate over Hubble length (\(R_H=\sqrt3\,\xi\)) |
| Amξ | \(m/\xi^2\) | yes | mass / area (condensate surface) |
| Amcξ | \(m\,c_s^2/\xi^2\) | yes | quench-class (task5 energy × ξ) |
| AGH | \(M_\mathrm{Pl}^2 H_\mathrm{door}\) | yes | pure gravitational junction scale |
| AΘ | \(M_\mathrm{Pl}^2\,|\Theta|_\mathrm{phys}\) | yes | fluid expansion as curvature scale |
| illegal | \(M_\mathrm{Pl}/\xi\), \(1/\xi^2\), free \(\alpha\,\rho\xi\) | no / dial | wrong dim or free coeff |

**Note:** \(H_\mathrm{door}=1/(\sqrt3\,\xi)\) shear-dom ⇒ AρH = \(\sqrt3\,\rho_\star\xi\) — same family as Aρξ, not a new law.

---

## 2. Candidate catalogue

### C1 — Layer-integrated door density over \(\xi\)

**Expression:**
\[
\sigma_s^{(1)}=\rho_\mathrm{eff}\,\xi\,,\qquad
p_s^{(1)}=c_s^2\,\sigma_s^{(1)}\,,\qquad
\pi_{ab}=0
\]
(or \(\rho_\mathrm{eff}\to\rho_\mathrm{rad}\) at door).

| | |
|---|---|
| **can-exist** | Thin-shell literature often takes \(\sigma_s\sim\int\rho\,\mathrm{d}\ell\) with \(\ell\sim\xi\); all factors stocked; dim legal (Aρξ). |
| **should-not-exist as land** | No written law “door bulk density becomes surface density at re-entry”; \(\rho_\mathrm{eff}\) is Phase-I door, not Phase-III \(\rho_\mathrm{re}\); \(p_s=c_s^2\sigma_s\) is acoustic analogy, not Israel derivation. |
| **Forces \(H_\mathrm{re}>0\) w/o P2?** | **NO** — fixes a *magnitude scale* of \([K]\), not the exterior square-root branch. |
| **Next MISSING_INPUT** | (i) embedding \(K_{ab}^\pm\) of \(\Sigma\); (ii) proof that this \(\rho\) is the correct integrand at *re-entry*; (iii) branch theorem (G5). |
| **grade** | **CANDIDATE schema · MISSING_INPUT** (survivor as *form*, not land) |

---

### C2 — Layer-integrated bounce floor over \(\xi\)

**Expression:**
\[
\sigma_s^{(2)}=\rho_\mathrm{bounce}\,\xi=\frac{m^4}{\lambda}\,\xi\,,\qquad
p_s^{(2)}=w\,\sigma_s^{(2)}\ \text{with}\ w\in\{0,c_s^2\}
\]

| | |
|---|---|
| **can-exist** | \(\rho_\mathrm{bounce}\) is PAID floor; dim legal. |
| **should-not-exist as land** | Floor is **wrong object** for turn / re-entry amplitude (N1 C1 WRONG-OBJECT parent); huge surface density \(\sim\rho_\mathrm{bounce}\xi\) is not a derived door skin. |
| **Forces \(H_\mathrm{re}>0\) w/o P2?** | **NO** |
| **Next MISSING_INPUT** | Law connecting floor to *surface* stress at gate; same \(K_{ab}\)+branch as C1. |
| **grade** | **WRONG-OBJECT** for re-entry \(S_{ab}\) (keep as dim-legal atom only) |

---

### C3 — Quench surface (task5 door budget promoted to \(S_{ab}\))

**Expression:**
\[
\rho_\mathrm{quench}\approx\frac12\frac{m\,c_s^2}{\xi^3}
\quad\Rightarrow\quad
\sigma_s^{(3)}=\rho_\mathrm{quench}\,\xi=\frac12\frac{m\,c_s^2}{\xi^2}
\]
\[
p_s^{(3)}=c_s^2\,\sigma_s^{(3)}
\]

| | |
|---|---|
| **can-exist** | Task5 already stocks quench energy density; integrate one healing length → surface; dim legal (Amcξ). FA1 door-is-quench for \(x\lesssim x^*\). |
| **should-not-exist as land** | Task5 is a **MeV ledger** channel that **fails O6**, not an Israel tensor; no \([K_{ab}]\) written; quench is medium energy injection, not exterior thin-shell stress. |
| **Forces \(H_\mathrm{re}>0\) w/o P2?** | **NO** |
| **Next MISSING_INPUT** | Tensor structure from GPE quench → \(S_{ab}\); exterior attach; branch (G5). |
| **grade** | **CANDIDATE schema · PAID number, DEAD as Israel land** (survivor as best *stocked* energy/area scale from medium) |

**Numeric stamp (script):** \(\sigma_s^{(3)}\) is tiny vs gravitational door scale \(M_\mathrm{Pl}^2 H_\mathrm{door}\) — consistent with “quench fails MeV / fails gravitational jump.”

---

### C4 — **TAUTOLOGY kill** — back-solve \(S_{ab}\) from target \(H_\mathrm{re}\)

**Expression (forbidden as land):**
\[
\sigma_s^{(4)}
=\frac{1}{4\pi G}\big(H_\mathrm{target}-H_-\big)
\quad\text{(or any algebraic invert of Israel using desired }H_\mathrm{re}\text{)}
\]

| | |
|---|---|
| **can-exist** | Always “consistent” once \(H_\mathrm{target}\) is chosen — Israel becomes definition of \(\sigma_s\). |
| **should-not-exist as derivation** | **Imports the answer.** Same class as N1 C4 (\(\rho\) from \(H_\mathrm{kin}\)). Not a medium law. |
| **Forces \(H_\mathrm{re}>0\) w/o P2?** | **Vacuous** — \(H_\mathrm{target}\) already chose the sign. |
| **Next MISSING_INPUT** | n/a — **do not pursue as construction** |
| **grade** | **TAUTOLOGY / KILLED** |

---

### C5 — Free coefficient on a stocked template

**Expression:**
\[
\sigma_s^{(5)}=\alpha\,\rho_\mathrm{eff}\,\xi
\quad\text{with free }\alpha\text{ dialed so Israel matches MeV / }H_\mathrm{re}\text{ / late }\Theta
\]

| | |
|---|---|
| **can-exist** | As *labeled sensitivity* only. |
| **should-not-exist as Derived** | Free dial (C8-class / M2 family). Same honesty kill as free \(N_\mathrm{med}\). |
| **Forces \(H_\mathrm{re}>0\) w/o P2?** | Only if \(\alpha\) is chosen after assuming the root — fake. |
| **grade** | **FABRICATED dial · KILLED as land** |

---

### C6 — Pure gravitational door scale (no medium law)

**Expression:**
\[
\sigma_s^{(6)}=\frac{M_\mathrm{Pl}^2 H_\mathrm{door}}{\sqrt{3}}
\quad\text{(or }M_\mathrm{Pl}^2/\xi\text{ — equivalent under shear-dom door)}
\]

| | |
|---|---|
| **can-exist** | Dim legal (AGH); Israel jump \([K]\sim H\) naturally produces \(\sigma\sim M_\mathrm{Pl}^2\Delta H\). |
| **should-not-exist as medium \(S_{ab}\)** | **No medium quantity enters** — this is exterior geometry identity class, not a derivation from \(n,v,\Theta\). Circular if used to “derive” the same \(H\) that defined it. |
| **Forces \(H_\mathrm{re}>0\) w/o P2?** | **NO** — \(\sigma_s\) from \(|H|\) loses sign; branch still free. |
| **Next MISSING_INPUT** | Medium→geometry map; signed jump theorem. |
| **grade** | **WRONG-OBJECT for medium construction** (legal atom for *consistency checks* only) |

---

### C7 — Fluid expansion as surface density scale

**Expression:**
\[
\sigma_s^{(7)}=M_\mathrm{Pl}^2\,|\Theta|_\mathrm{phys}
=M_\mathrm{Pl}^2\,\frac{|\Theta|_\mathrm{heal}\,c_s}{\xi}
\]
(at gate \(\Theta_\mathrm{heal}>0\)).

| | |
|---|---|
| **can-exist** | \(\Theta\) is the stocked preferred-frame expansion; dim legal (AΘ); pairs with kinematic map \(H_\mathrm{kin}=\Theta_\mathrm{heal}c_s/(d\xi)\). |
| **should-not-exist as land** | Identifying \(\sigma_s\) with \(M_\mathrm{Pl}^2\Theta\) **renames** the kinematic map as surface stress — does not derive Israel content. At \(\Theta\to0^+\) surface vanishes while \(\rho\) need not. Domain: \(\Theta\) is Phase-II fluid, not exterior \(K_{ab}\). |
| **Forces \(H_\mathrm{re}>0\) w/o P2?** | **NO** — using \(|\Theta|\) erases sign; using \(\mathrm{sign}(\Theta)\) **is** P2 smuggled into \(\sigma_s\). |
| **Next MISSING_INPUT** | Independent tensor derivation of \(S_{ab}\) from GPE; proof \(\mathrm{sign}(\Theta)\Rightarrow\mathrm{sign}(H)\) is theorem not declaration (G5/G6). |
| **grade** | **CANDIDATE schema · residual rename risk** (survivor only if tensor derivation added) |

---

### C8 — Acoustic surface pressure from velocity / group-speed layer

**Expression:**
\[
\sigma_s^{(8)}=0\,,\qquad
p_s^{(8)}=\rho_\star\,\xi\,(v_g^2-c_s^2)
\quad\text{or}\quad
\pi_{ij}\sim\rho_\star\xi\,(v_i v_j-\tfrac13 v^2 h_{ij})
\]
with \(v_g\) from FA1 at door \(x\sim O(1)\), \(\rho_\star\in\{\rho_\mathrm{eff},n\cdot(\text{energy scale})\}\).

| | |
|---|---|
| **can-exist** | FA1 stocks \(v_g>c_s\) as metric-end diagnostic; anisotropic stress from velocity is fluid-legal. |
| **should-not-exist as land** | FA1 is **dispersion table**, not Israel; \(v_g>c_s\) ends metric trust — does not define exterior \(S_{ab}\). \(\rho_\star\) choice underdetermined. |
| **Forces \(H_\mathrm{re}>0\) w/o P2?** | **NO** — pressure/anisotropy shapes shear of \(K_{ab}\), not FRW branch uniqueness. |
| **Next MISSING_INPUT** | Controlled \(3+1\) reduction of GPE stress to \(\pi_{ab}\) on \(\Sigma\); \(K_{ab}\); branch. |
| **grade** | **CANDIDATE schema · MISSING_INPUT** |

---

### C9 — Averaging bulk stress integrated as surface (S-C shape)

**Expression (sketch):**
\[
\Delta\Pi_{ij}
=\int_{\mathrm{layer}}\mathrm{Stress}_{ij}\,\mathrm{d}\ell
\sim\mathrm{Stress}\cdot\xi
\]
used as **medium** matching target (prior shape S-C), **not** exterior \(S_{ab}\) until mapped.

| | |
|---|---|
| **can-exist** | Averaging identity is PAID: \(\mathrm{d}\langle\Theta\rangle/\mathrm{d}t=-\langle\Theta\rangle^2-\mathrm{Var}+\mathrm{Stress}\). Layer integral is the natural S-C object. |
| **should-not-exist as exterior Israel** | Bulk Stress drives \(\langle\Theta\rangle\) in Phase II — **fluid**, not \([K_{ab}]\). Homogeneous average **kills** stress channel (M-5). No stocked tensor components. |
| **Forces \(H_\mathrm{re}>0\) w/o P2?** | **NO** — supplies medium turn, not exterior root. |
| **Next MISSING_INPUT** | Explicit \(\mathrm{Stress}_{ij}[n,\nabla n,v]\) from GPE; map \(\Delta\Pi\to S_{ab}\) at metric return; G5. |
| **grade** | **CANDIDATE schema · best medium-side honesty** (still empty of components) |

---

### C10 — M2 fabricated junction sold as \(S_{ab}\)

**Expression:**
\[
\text{“}S_{ab}\text{” via }\rho_\mathrm{out}=\eta\,\rho_\mathrm{in}e^{4N_\mathrm{med}}
\]

| | |
|---|---|
| **can-exist** | As labeled toy only. |
| **should-not-exist** | **FABRICATED**; \(N_\mathrm{med}=1/c_s\) retired; free dials. |
| **grade** | **KILLED** (prior K1) |

---

### C11 — Continuous metric-ON thin shell at \(H=0\) (A-reopen silhouette)

**Expression:** Israel sheet at the moment \(H_-=-H_+\to0\) with finite \(\rho\), metric ON throughout.

| | |
|---|---|
| **can-exist** | Classical singular-bounce literature (different silhouette from RP-A). |
| **should-not-exist under this mission’s domain** | Obstruction **A** kills *continuous* \(H\) through 0 at finite \(\rho\); a singular shell is a *different* premise set, and under **P1** Phase II has **no** exterior metric to host one shell across the bounce. |
| **Forces expanding root?** | Only with extra branch/normal choices — not free lunch. |
| **grade** | **DEAD under P1+A** for RP-A package (do not reopen without new premises) |

---

### C12 — Two-map bookkeeping without \(S_{ab}\) (S-A restatement)

**Expression:** no tensor; \(\Phi_\mathrm{out}+\Phi_\mathrm{in}\) with P2 for sign.

| | |
|---|---|
| **can-exist** | Prior honest content (N2 match-book). |
| **should-not-exist as \(S_{ab}\) fill** | Explicitly **avoids** writing \(S_{ab}\). |
| **Forces \(H_\mathrm{re}>0\) w/o P2?** | **NO** — P2 is the sign. |
| **grade** | **RECONSTRUCTED bookkeeping · not an \(S_{ab}\) candidate** |

---

## 3. Force-branch attempt (all candidates)

**Question:** Does **any** C1–C12 expression force \(H_\mathrm{re}>0\) without P2 declaration?

### Structured attempt

1. **Assume** a fully fixed \(S_{ab}\) from medium (grant C1 or C3 or C9 components — *counterfactual*).  
2. **Place** \(\Sigma_\mathrm{re}\) as boundary of Phase-III exterior only (S-B; Phase II non-metric).  
3. Israel on one side reduces to a **boundary condition** relating exterior \(K_{ab}(H_\mathrm{re},\sigma_\mathrm{re},\ldots)\) to \(S_{ab}\).  
4. Exterior FRW still solves
   \[
   H_\mathrm{re}^2=\frac{8\pi G\rho_\mathrm{re}}{3}+\frac{\sigma_\mathrm{re}^2}{3}
   \]
   so \(H_\mathrm{re}=\pm\sqrt{\ldots}\).  
5. Israel constrains **combinations** of extrinsic curvature (often \(\propto H\) with a normal orientation \(\varepsilon=\pm1\)). The pair \((\varepsilon,\mathrm{sign}(H))\) retains a discrete choice unless a **theorem** ties the exterior normal/branch to medium \(\langle\Theta\rangle>0\).  
6. That theorem **is** N4 / prior G5 — **not stocked** in any candidate above.  
7. Encoding \(\mathrm{sign}(\Theta)\) into \(\sigma_s\) (C7) is **P2 by renaming**, not a derivation.  
8. Two-sided continuous metric shell (C11) is domain-illegal under P1 and still needs branch data.

**Verdict:** **NO candidate forces the expanding root without P2-class input.**  
**Expected:** NO. **Observed:** NO.  
**N4 land from this package:** **0.**

---

## 4. Kill summary (expression-level)

| ID | fate |
|---|---|
| C1 | survivor **schema** (layer integral) — not land |
| C2 | WRONG-OBJECT |
| C3 | survivor **schema** (quench scale) — not Israel land |
| C4 | **TAUTOLOGY KILL** |
| C5 | **FREE DIAL KILL** |
| C6 | WRONG-OBJECT (pure gravity) |
| C7 | survivor schema with **rename risk** |
| C8 | survivor schema (anisotropy) — empty components |
| C9 | survivor schema (S-C bulk integral) — empty components |
| C10 | **FABRICATED KILL** |
| C11 | **DEAD under P1+A** |
| C12 | not an \(S_{ab}\) fill |

---

## 5. Count stamp

| metric | value |
|---|---|
| \(n_\mathrm{candidates}\) written | **12** (C1–C12) |
| expression-level kills | C4, C5, C10, C11 (+ C2/C6 as wrong-object) |
| survivor **schemas** (non-land) | **C1, C3, C7, C8, C9** (5) |
| lands (\(S_{ab}\) Derived + N4) | **0** |
| stocked Israel equations after package | **still 0** |

---

## 6. What “survivor schema” means

A survivor is a **form that is not immediately illegal** under Rule 1 and stocked dimensions — a **target for missing inputs**, not a promotion.

**None** of C1, C3, C7, C8, C9:

- stocks \(K_{ab}\) of \(\Sigma\),  
- closes F-A2 \(\rho_\mathrm{re}\),  
- forces expanding root,  
- or grades COMPLETE.

Exact next MISSING_INPUT per survivor: see [`SURVIVORS.md`](./SURVIVORS.md).

---

*End CANDIDATE_SAB.md — construction ≠ closure. NO FABRICATIONS.*

### C6 consistency note (red AGREE-IF cure)

Three writings appeared in the package: \(M_\mathrm{Pl}^2 H_\mathrm{door}/\sqrt{3}\), \(M_\mathrm{Pl}^2/\xi\), and REPORT ratio-1 \(M_\mathrm{Pl}^2 H_\mathrm{door}\). **These are not equivalent** (factors of \(\sqrt{3}\) / door bookkeeping). **Canonical wrong-object atom:** \(\sigma_s\sim M_\mathrm{Pl}^2 H_\mathrm{door}\). Grade unchanged (WRONG-OBJECT).
