# AXIOM.md — A_ωJ (Rule 1 invented premise)

**Package:** `docs/working_logs/_runs/theory_construction_20260804/A_omegaJ_rule1/`  
**Date:** 2026-08-04  
**Grade on entry:** **CANDIDATE only** — never Derived, never PAID, never booked as land  
**Protocol:** RULE 1 (ForGrok&Claude.md §RULE 1); template shape from `fa3_metric_off/CONSTRUCTION.md`  
**Parents:** `omegaJ_forward/` · `debt_omegaJ_forward_formulability_20260803/` · `PRTOE_baryogenesis.md` §3a · transfer-integral stages 6–8 · #39

---

## 0. What this file is

This is the **first live Rule 1 exercise** against the named axiom slot **A_ωJ**.

It writes an explicit, physics-contentful premise so that a *forward* expression for the junction plasma frequency **could** follow. It does **not** invent numeric χ, J_seat, or ω_J. It does **not** promote forward ω_J to Derived.

---

## 1. Licensed premise **A_ωJ** (precise statement)

### A_ωJ — Seat-junction plasma frequency is an independent micro scale

> **A_ωJ.** At the sphaleron temperature \(T_\mathrm{sph}\), the **tenth-channel seat term** (already selected as the L-carrying junction portal; transfer-integral stage 2) generates a **sinusoidal seat–visible junction** on the overdamped visible-side phase \(\varphi\) conjugate to visible lepton number. That junction is formalized by the stage-8 potential term
> \[
> U_J \;=\; -\chi\,\omega_J^2\,\cos\!\bigl(\varphi - \dot\theta\, t\bigr),
> \]
> together with the static Majorana pin
> \[
> U_\mathrm{pin} \;=\; -\chi\, m_1^2\,\cos\varphi
> \]
> in the **same** phase, with common stiffness \(\chi>0\).
>
> **Micro definition of the plasma frequency (load-bearing content of the axiom):**
> \[
> \omega_J^2 \;\equiv\; \frac{J_\mathrm{seat}}{\chi}
> \;=\;
> \frac{\text{(pinning curvature of \(U_J\) at a cos extremum)}}{\chi}.
> \]
> Here \(J_\mathrm{seat}\) is the **seat coupling energy-density scale** of the cos\((\varphi-\dot\theta t)\) term — fixed by seat / tenth-channel micro content at \(T_\mathrm{sph}\), **not** by \(\eta\), \(R_\mathrm{need}\), or any back-solve of the rectifier.
>
> Equivalently (Package A form): the seat microphysics supplies a single independent microscopic frequency \(\omega_J\) of the seat junction at \(T_\mathrm{sph}\), without reference to \(\eta\) or \(R_\mathrm{need}\).
>
> **Independence clause (part of the axiom, not a side note):** neither \(\omega_J\) nor the pair \((\chi, J_\mathrm{seat})\) is permitted to be fixed by fitting to the observed baryon asymmetry, to \(R_\mathrm{need}\sim 5\times 10^{-5}\), or to the back-solved grading center \(\sim 5.7\,\mathrm{keV}\). Declined silent IDs remain declined: \(\chi \neq v_L\) by default; \(\chi \neq f_{e\text{-scalar}}\) without a *named further* axiom.

**Honesty tag (Rule 1 / fa3 template):**  
**A_ωJ is a licensed structural commitment about the seat junction**, not a theorem from stocked corpus numbers alone. It is **not** proved by quartet closure. Quartet closure only shows that three independent legs force one residual scale.

---

## 2. What A_ωJ *asserts* (content checklist)

| # | Assertion | Status if A_ωJ is admitted |
|---|---|---|
| 1 | Junction portal is the tenth-channel seat term | Already **DECIDED** (stage 2); A_ωJ inherits, does not re-decide |
| 2 | Drive term has form \(U_J = -\chi\omega_J^2\cos(\varphi-\dot\theta t)\) | **Licensed formalization** of the Kapitza / overdamped class (stage 8) |
| 3 | \(\omega_J^2 = J_\mathrm{seat}/\chi\) is the **definition** of junction plasma frequency from seat micro | **A_ωJ core** |
| 4 | \(J_\mathrm{seat}/\chi\) (or \(\omega_J\)) is **independent** of \(\eta\), \(R_\mathrm{need}\) | **Independence clause** |
| 5 | \(U_\mathrm{pin}\) curvature \(\propto m_1^2\) prices \(p\), **not** \(j\) | Already **PAID** stage-8 structure; A_ωJ does not re-open |
| 6 | Numeric values of \(\chi\), \(J_\mathrm{seat}\), or \(\omega_J\) | **Not asserted by A_ωJ** — would require a second micro input or lattice price |

**Empty rejections (what A_ωJ is *not*):**

- Not “\(\omega_J\) exists.”  
- Not “\(\omega_J = 5.672\,\mathrm{keV}\).”  
- Not “identify decay constant with \(v_L\) and solve.”  
- Not “Jeans \(\sqrt{4\pi G\rho}\) is the junction frequency.”

---

## 3. Operational consequences if A_ωJ is held

With A_ωJ + already-stocked overdamped premises, the rectifier algebra is:

```
χ Γ_φ · φ̇ = −U′(φ)
φ̇ = −p sin φ − j sin(φ − θ̇ t)
p ≡ m₁²/Γ_φ ,   j ≡ ω_J²/Γ_φ
```

Fast-drive (\(p\ll\dot\theta\), holds at \(T_\mathrm{sph}\)):

```
R = ω_J² / (2 Γ_φ θ̇) = j / (2 θ̇)
```

**If** seat micro later supplies a numeric \(\omega_J\) (or both \(\chi\) and \(J_\mathrm{seat}\)) **without** \(\eta\), then \(R\) is predicted and may be graded. **A_ωJ alone does not supply that number.**

---

## 4. Relation to stocked objects (what is *not* invented here)

| Object | Type | Role relative to A_ωJ |
|---|---|---|
| \(\Gamma_\varphi = G_F^2 T_\mathrm{sph}^5 \approx 5.3902\times 10^9\,\mathrm{eV}\) | COMPUTED | bath rate; independent of A_ωJ |
| \(\dot\theta(T_\mathrm{sph})\approx 59.68\,\mathrm{eV}\) | COMPUTED | drive; independent of A_ωJ |
| \(m_1\approx 2.25\,\mathrm{meV}\) | RECORDED | off-switch of rectifier; **not** \(\omega_J\) |
| \(R_\mathrm{need}\sim 5\times 10^{-5}\) | FROM \(\eta\cdot n\) band | **grading only** — forbidden as forward input |
| \(\omega_J^\star = 5.672\,\mathrm{keV}\) | BACK-SOLVED | grading center only — **not** A_ωJ output |
| \(\chi\), \(J_\mathrm{seat}\) | **UNSTATED** | the micro legs A_ωJ *names* but does **not** number |

---

## 5. Grade and promotion wall

| Item | Grade |
|---|---|
| **A_ωJ as written** | **CANDIDATE** (Rule 1 entry) |
| Forward \(\omega_J\) numeric land | **OPEN-BLOCKED** (still; needs second micro price) |
| Quartet arithmetic | machine-backed **back-solve** (unchanged) |
| AD-direct + transmission class document | COMPLETE-CONDITIONAL (**not** upgraded by this package) |

**Promotion of A_ωJ → Derived / PAID is forbidden by Rule 1 on entry.**  
Promotion of **forward \(\omega_J\)** requires a completed derivation under `KILL_AND_BANDS.md` with independence I1–I7 (`omegaJ_forward/REQUIRED_INPUTS.md`) — not merely registration of this axiom.

---

## 6. Forbidden readings (self-referential honesty kills)

Any of the following **kills this package’s honesty** (not necessarily the physics class):

1. Selling A_ωJ as **Derived** from stocked objects alone.  
2. Selling quartet closure as proof of A_ωJ or as forward \(\omega_J\).  
3. Inserting \(\omega_J = 5.672\,\mathrm{keV}\) into A_ωJ as if micro-priced.  
4. Silent \(\chi = v_L\) or \(f\to\chi\) under cover of A_ωJ.  
5. Scoring A_ωJ against a band chosen *after* seeing a preferred land.

---

## 7. What second premise would close the number (named, not invented)

A_ωJ prices the **form**. A numeric land still needs **one** of:

| Second premise (future) | What it must supply |
|---|---|
| **A_Jχ** | Independent micro/lattice computation of both \(\chi\) and \(J_\mathrm{seat}\) from tenth-channel UV/IR matching at \(T_\mathrm{sph}\) |
| **A_ωJ-direct** | Direct micro expression for \(\omega_J\) from seat operators (equivalent; collapses the ratio) |
| Explicit UV completion of the seat term | Enough operator content that \(J_\mathrm{seat}/\chi\) is forced without free constants dialed to \(\eta\) |

Until one of these is written and graded under Rule 1 / independence rules, residual stays **OPEN-BLOCKED** with A_ωJ registered as **CANDIDATE structure**.

---

*End AXIOM.md*
