# F-A3 / O2 attempt — exterior H-cross from medium stress+junction (2026-08-03)

**Track:** D7 / A6 residual — close F-A3 dynamical content without hand declaration  
**Parent:** [`docs/working_logs/_runs/debt_bounce_20260803/REPORT.md`](../debt_bounce_20260803/REPORT.md)  
**Script:** [`scripts/bounce_fa3_hcross_attempt.py`](../../../../scripts/bounce_fa3_hcross_attempt.py)  
**Also read:** `scripts/bounce_rpA_scaffold.py`, `scripts/bounce_m2_junction.py`, `scripts/bounce_averaging_decomposition.py`  
**Derived exterior H-cross?** **No.**  
**Cyclic cosmology booked?** **No.**

---

## Question

Can exterior \(H_\mathrm{re}\) be derived from medium stress + junction (continuous or Israel-class matching), without F-A3’s branch declaration

\[
\langle\Theta\rangle>0 \;\wedge\; \ell_\mathrm{grad}\gtrsim\xi
\;\Rightarrow\;
H_\mathrm{re}=+\sqrt{\frac{8\pi G\rho_\mathrm{re}}{3}}\;?
\]

Pass criterion (from debt_bounce NEXT): exterior \(H\) crosses 0 with \(\dot H>0\) **as a consequence** of medium stress + junction; fabrication only on unfilled F-A1 SM-crossing corners — not on the turn sign.

---

## Candidate continuous map (only natural acoustic one)

On the preferred-frame condensate rest slice (F-A1 structure already half-machined):

\[
H_\mathrm{kin}(t)
=\frac{\langle\Theta\rangle_\mathrm{phys}}{d}
=\Theta_\mathrm{heal}\,\frac{c_s}{d\,\xi},
\qquad
c_s=\sqrt{3\alpha},\quad
t_0=\xi/c_s,\quad
d=3\ \text{(isotropic FRW)}\ \text{or}\ 1\ \text{(1D toys)}.
\]

This is the kinematic identification of exterior/acoustic expansion with the fluid expansion scalar. Sign of \(H_\mathrm{kin}\) tracks \(\langle\Theta\rangle\) continuously; no square-root branch choice.

---

## What the short compute shows

Run: `nice -n 19 python3 scripts/bounce_fa3_hcross_attempt.py` (exit 0, asserts hold).

### Anchors (CMB-class door \(\Sigma_0=10^{-5}\))

| quantity | value |
|---|---|
| \(c_s=\sqrt{3\alpha}\) | \(0.14796\) |
| \(H_\mathrm{door}\) (shear clock) | \(1.894\times10^{-21}\,\mathrm{eV}\) |
| \(R_H/\xi\) | \(1.732=\sqrt3\) |
| \(\rho_\mathrm{eff}^{1/4}\) (door) | \(2.827\,\mathrm{keV}\) |
| \(\rho_\mathrm{bounce}^{1/4}\) | \(1.059\,\mathrm{keV}\) |
| \(\|H_F(\rho_\mathrm{eff})\|\) | \(=H_\mathrm{door}\) (by construction of \(\rho_\mathrm{eff}\)) |

### Prefactor

\[
\frac{|H_\mathrm{kin}(\Theta_\mathrm{heal}=1)|}{H_\mathrm{door}}
=
\begin{cases}
c_s\sqrt3 \approx 0.256 & (d=1)\\
c_s/\sqrt3 \approx 0.0854 & (d=3)
\end{cases}
\]

O(1) healing \(\Theta\) is **not** Planck-suppressed vs the door — same epoch scale — but is **not** equal to \(H_\mathrm{door}\) either.

### Medium turn (0D stand-in for M6; stress channel from averaging identity)

| \(n_0\) | \(\Theta_0\) | turn? | \(n_\mathrm{cross}\) | \(\mathrm{d}\Theta/\mathrm{d}t\big|_{\mathrm{cross}}\) | late \(\Theta\) |
|---|---|---|---|---|---|
| 3 | −1 | YES | 3.55 | \(+3.83\) | \(+0.055\) |
| 6 | −2 | YES | 8.04 | \(+10.56\) | \(+0.062\) |
| 11 | −2 | YES | 12.66 | \(+17.49\) | \(+0.061\) |

Synthetic averaging: `stress_drive = +2.31e-2`, `net_rhs = +1.96e-2` (inhomogeneous interaction channel; homogeneous average kills it).

**Medium layer:** \(\langle\Theta\rangle:-\to0\to+\) with \(\dot\Theta>0\) at cross is real in the toy / M6 class. Under \(H_\mathrm{kin}\propto\Theta\), that is a continuous kinematic H-cross **of the fluid**, not of exterior FRW.

### Magnitude lock at late re-entry candidate (primary case \(n_0=6\))

| \(d\) | \(\|H_\mathrm{kin}(\Theta_\mathrm{late})\|/H_\mathrm{door}\) | \(\rho_\mathrm{need}^{1/4}\) to match Friedmann |
|---|---|---|
| 1 | \(1.59\times10^{-2}\) | \(356\,\mathrm{eV}\) (\(\rho/\rho_\mathrm{eff}\sim2.5\times10^{-4}\)) |
| 3 | \(5.29\times10^{-3}\) | \(206\,\mathrm{eV}\) (\(\rho/\rho_\mathrm{eff}\sim2.8\times10^{-5}\)) |

Door-entry inversion: matching \(H_\mathrm{door}\) under the kinematic map needs \(|\Theta_\mathrm{heal}|\approx 3.90\) (\(d=1\)) or \(11.71\) (\(d=3\)). Verified 1D overshoot is O(1); 0D late \(\Theta\sim0.06\) after damping — **no legal amplitude law locks** \(|H_\mathrm{kin}|=H_F(\rho_\mathrm{re})\).

---

## Answer: Can \(H_\mathrm{re}\) be derived without declaration?

### **No.**

There is no formula that yields a derived exterior \(H_\mathrm{re}\) from stocked medium stress + written junction without a branch / metric-off declaration. O2 remains **PARTIAL**.

### Exact obstruction (three stacked; A or B alone is fatal)

**(A) Constraint conflict at the zero (metric-ON continuous cross).**  
Under \(H=H_\mathrm{kin}=\langle\Theta\rangle_\mathrm{phys}/d\), the medium turn gives
\[
H:-\to0\to+,\qquad \dot H=\frac{c_s}{d\,\xi}\,\frac{\mathrm{d}\langle\Theta\rangle}{\mathrm{d}t}>0
\]
algebraically. At the zero-cross, density is finite (\(n_\mathrm{cross}\sim8\) in the primary toy; door \(\rho_\mathrm{eff}\) or \(\rho_\mathrm{bounce}\) scale). Flat FRW
\[
H^2=\frac{8\pi G}{3}\rho+\frac{\sigma^2}{3}
\]
then requires \(H\neq0\). Numbers: \(H_\mathrm{kin}(\mathrm{cross})=0\) while \(|H_F(\rho_\mathrm{eff}\cdot n)|\sim5.37\times10^{-21}\,\mathrm{eV}\neq0\).  
**Metric-ON exterior cannot pass through \(H=0\) at finite \(\rho\)** without modified constraint, vanishing \(\rho_\mathrm{tot}\), or a surface layer. Homogeneous higher-order / quartic routes already dead (`bounce_m8_ledger_quartic.py`).

**(B) Metric-off re-entry is branch choice — this *is* F-A3.**  
RP-A escapes (A) by dissolving the metric at \(\xi\) (Phase II). During the non-metric interval Friedmann does not apply, so \(\Theta\) may cross freely under gradient stress. Re-attaching exterior FRW **only after** \(\langle\Theta\rangle>0\) selects the expanding square root
\[
H_\mathrm{re}=+\sqrt{\frac{8\pi G\rho_\mathrm{re}}{3}}.
\]
Medium stress derives the **fluid** turn; it does not compute an exterior \(H(t)\) trajectory through zero, because exterior \(H\) does not exist in Phase II. That re-attachment rule is exactly the reconstructed F-A3 declaration — not a NEC derivation and not a continuous exterior cross.

**(C) Magnitude lock (secondary; blocks even a granted sign).**  
\[
\frac{|H_\mathrm{kin}(\Theta_\mathrm{heal}=O(1),d=3)|}{H_\mathrm{door}}\approx\frac{c_s}{\sqrt3}\approx0.085;
\]
late damped \(\Theta\) makes the ratio \(\sim5\times10^{-3}\). Matching \(|H_\mathrm{kin}|=H_F(\rho)\) needs either \(\Theta_\mathrm{heal}\gtrsim d/(c_s\sqrt3)\sim12\) (not produced by verified 1D O(1) overshoot) or \(\rho_\mathrm{re}\) suppressed by \(\sim10^{4}\)–\(10^{5}\) vs door \(\rho_\mathrm{eff}\). No legal junction / F-A2 amplitude law closes this.

### What *is* derived / standing (not confused with F-A3)

- Medium \(\langle\Theta\rangle\) turn from inhomogeneous stress (interaction + quantum gradient): **yes** in 0D/1D toys; averaging identity holds.
- Door geometry \(R_H/\xi\to\sqrt3\), \(H_\mathrm{door}=1/(\sqrt3\,\xi)\): **computed** (M2).
- Homogeneous legal-parts FRW bounce: **DEAD** (unchanged).
- F-A3 as written matching rule: still **reconstructed declaration**.

### If a future PASS existed, what it would need (not claimed)

1. Either a derived modified constraint allowing \(H=0\) at finite \(\rho\), **or** a derived surface stress on a spacelike junction that Israel-matches contracting→expanding exteriors, **or** a theorem that metric-off Phase II plus acoustic re-emergence **forces** the expanding branch without branch choice; **and**
2. An F-A2 amplitude law locking \(|H_\mathrm{kin}|=H_F(\rho_\mathrm{re})\) from legal parts.

None of these are stocked. Prefer kill over fabrication — no exotic \(X\) introduced.

---

## Grade stamp

| item | status |
|---|---|
| O2 / F-A3 dynamical content | **PARTIAL** (unchanged) — medium turn yes; exterior H-cross **not** derived |
| RP-A overall | **RECONSTRUCTED CANDIDATE** (unchanged) |
| Homogeneous engines | **DEAD** (unchanged) |
| Cyclic cosmology | **not booked** |

> **F-A3 remains a branch declaration.** Continuous kinematic map \(H=\langle\Theta\rangle/d\) turns the fluid, not the exterior metric: metric-ON Friedmann forbids \(H=0\) at finite \(\rho\); metric-OFF re-entry *is* the declaration. Magnitude lock fails at the \(c_s/\sqrt3\sim0.085\) factor and late-\(\Theta\) damping. **Do not book cyclic cosmology.**

### Audience one-liner

> The medium can reverse its expansion rate via gradient stress; that does not derive an exterior cosmological \(H:-\to0\to+\) without either violating Friedmann at finite density or re-declaring the expanding branch when the metric returns.

---

## Artifact paths

| item | path |
|---|---|
| This report | `docs/working_logs/_runs/debt_bounce_FA3_20260803/REPORT.md` |
| Compute script | `scripts/bounce_fa3_hcross_attempt.py` |
| Parent debt | `docs/working_logs/_runs/debt_bounce_20260803/REPORT.md` |
| RP-A scaffold | `scripts/bounce_rpA_scaffold.py` |
| M2 junction | `scripts/bounce_m2_junction.py` |
| Averaging identity | `scripts/bounce_averaging_decomposition.py` |
