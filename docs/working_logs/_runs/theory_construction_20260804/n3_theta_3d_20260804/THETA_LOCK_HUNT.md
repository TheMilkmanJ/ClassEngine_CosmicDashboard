# Θ_lock hunt — can legal runs reach \(\Theta_\mathrm{heal}\gtrsim 11.7\)?

**Script:** `scripts/bounce_n3_theta_lock_scan.py`  
**Log:** [`logs/n3_theta_lock_scan.log`](./logs/n3_theta_lock_scan.log)  
**Date:** 2026-08-04

---

## 0. Definition (S1 lock metric)

From N1 / FA3 shear-door bookkeeping (\(d=3\)):

\[
\Theta_\mathrm{lock}
=\frac{d}{c_s\sqrt3}
=\frac{3}{\sqrt{3\alpha}\,\sqrt3}
\approx 11.706
\]

so \(|H_\mathrm{kin}|=\Theta\,c_s/(d\,\xi)\) matches \(H_\mathrm{door}=1/(\sqrt3\,\xi)\).

**S1 pays only if late / mass-weighted \(\langle\Theta\rangle_\mathrm{heal}\) at a re-entry candidate reaches \(\gtrsim\Theta_\mathrm{lock}\).**  
Transient peaks, vacuum spikes, and integrator caps **do not** pay S1.

---

## 1. Legal scan design

### 1.1 0D reduced ODE (stocked FA3 form)

\[
\dot n=-n\Theta,\qquad
\dot\Theta=-\Theta^2+\kappa(n-1)-\gamma\Theta
\]

| param | grid | corpus note |
|---|---|---|
| \(n_0\) | 2,3,6,11,20,50 | FA3 used 3,6,11; M6 \(n\sim1+A\) up to ~51 |
| \(\Theta_0\) | −0.5…−5 | FA3 −1,−2 |
| \(\kappa\) | 0.5…5 | stocked 1.5 |
| \(\gamma\) | 0.05…0.5 | stocked 0.15 |

**Physicality filter:** reject `hit_cap` (\(|\Theta|\) safety) and overshoot \(>100\).

### 1.2 1D GPE (M6 scheme)

\((A,v_0)\in\{(2,0.5),(5,1),(10,1),(5,2),(20,1),(5,3)\}\).  
Readout: mass-weighted \(\langle\partial_x v\rangle\); raw local Θ diagnostic only.

### 1.3 Forbidden

- Invented force laws beyond stocked ODE / repulsive GPE.  
- Treating \(\kappa,\gamma\) as Derived cosmological constants.  
- Selling spherical 1D focusing as 3D production COMPLETE.

---

## 2. Results (disk)

### 2.1 0D

| quantity | value |
|---|---|
| unique rows | 83 |
| physical | 78 (5 blowups rejected) |
| turned | 76 |
| **max late_Θ** | **+1.8005** |
| max physical Θ_pos | +11.34 |
| max physical overshoot | 6.78 |
| stocked default late | +0.0619 |
| late ≥ lock? | **False** |
| physical peak ≥ lock? | **False** (11.34 < 11.71) |

**Best late row:** \(n_0=50\), \(\Theta_0=-5\), \(\kappa=3\), \(\gamma=0.05\) → late_Θ=+1.80, overshoot=1.09.  
Still **0.15×** Θ_lock. κ/γ here are **extreme toy corners**, not Derived.

**Best peak row:** \(n_0=50\), \(\Theta_0=-5\), \(\kappa=5\), \(\gamma=0.05\) → Θ_max=+11.34 but **late_Θ=−1.48** (not re-entry expansion). Peak≠S1.

**κ–γ at stocked (6,−2):** late_Θ ranges roughly −1.3…+1.25; default +0.062. No late lock.

### 2.2 1D GPE

| quantity | value |
|---|---|
| cases / clean | 6 / 6 (dE<5%) |
| max mean ⟨Θ⟩ | +1.062 |
| max late mean ⟨Θ⟩ | +0.0013 |
| density turn | YES all |
| overshoot | O(1) ≤1.38 |
| mean ≥ lock? | **False** |
| late mean ≥ lock? | **False** |
| raw local max | ~2900 (**not S1**) |

### 2.3 Synthetic averaging

stress_drive \(>0\), net_rhs \(>0\); mean_Θ ~0.018; max local |Θ|~0.125. Channel exists; magnitude not lock.

### 2.4 Corpus priors (inventory only)

- Hypersonic 1D: turn holds; amplification O(1).  
- Spherical M6: focusing measured; not Θ~12 production.  
- Transverse 2D: ⟨Θ_xx⟩~0.03–0.08.  
- No full-3D production Θ instrument.

---

## 3. Verdict table

| claim | answer |
|---|---|
| Can legal stress produce ⟨Θ⟩ turn? | **YES** (toy/1D PAID) |
| Max late Θ found | **1.80** |
| Max peak 0D-phys / 1D-mean | **11.34** (peak; late not lock) |
| Θ_lock (late) reached? | **NO** |
| S1 | **MISSING_INPUT / OPEN-BLOCKED** |
| Production A_Θ-3D | **OPEN** (not stocked) |
| Invent force law? | **NO** |

\[
\frac{\Theta_\mathrm{late,max}}{\Theta_\mathrm{lock}}
\approx 0.154
\qquad
\frac{\Theta_\mathrm{peak,phys}}{\Theta_\mathrm{lock}}
\approx 0.968
\quad\text{(peak only; late fails)}
\]

---

## 4. Why late stays small (mechanism sketch — not a new law)

In the reduced ODE, after overshoot \(n\to\sim1\), the drive \(\kappa(n-1)\to0\) while \(-\Theta^2-\gamma\Theta\) damp positive expansion. Equilibrium-scale late Θ is set by residual overshoot/damping balance → **O(1) or ≪1**, not ~12, unless \(\kappa,\gamma\) are freely retuned as cosmological dials (honesty kill).

In 1D GPE, mass-weighted mean expansion after rebound is **near zero** on the box (outward shell + ambient); local cores do not supply a homogeneous \(\Theta_\mathrm{heal}\sim12\).

---

## 5. Explicit non-derivation

**This package does not derive \(\Theta_\mathrm{lock}\).**  
If a later writer quotes peak~11 or vacuum spikes as “lock,” that is fabrication relative to S1’s late re-entry demand.

---

*End THETA_LOCK_HUNT.md*
