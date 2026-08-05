# Instrument runs — stocked forms only

**Script:** `scripts/bounce_n3_gpe_late_theta.py`  
**Log:** [`logs/n3_gpe_late_theta.log`](./logs/n3_gpe_late_theta.log)  
**Date:** 2026-08-04

---

## 0. Legal forms (no invented force laws)

| layer | equation / scheme | source stock |
|---|---|---|
| **0D** | \(\dot n=-n\Theta\), \(\dot\Theta=-\Theta^2+\kappa(n-1)-\gamma\Theta\) | FA3 / N1 / `bounce_n3_theta_lock_scan` |
| **1D GPE** | \(i\partial_t\psi=-\tfrac12\partial_{xx}\psi+(|\psi|^2-1)\psi\) split-step | `bounce_m6_rebound_1d` |
| **Spherical GPE** | same, \(u=r\psi\), DST kinetic on \(w=u-r\) | `bounce_m6_rebound_dst` |
| **2D pancake** | 2D GPE split-step, staggered door IC | `bounce_transverse_2d` |
| **Averaging** | coarse mass-weighted stress identity | `bounce_averaging_decomposition` |

**Forbidden:** new drive terms, free cosmological dials sold as Derived, invent \(H_\mathrm{re}\), PolyChord, MCMC reopens.

---

## 1. What was run (this package)

### [A] 0D deep scan

| axis | grid |
|---|---|
| A | \(n_0\in\{2,3,6,11,15,20,30,40,50,60,80\}\) × \(\Theta_0\in\{-0.5…-8\}\) at (κ,γ)=(1.5,0.15) |
| B | κ×γ at (6,−2) |
| C | high-compression densification \(n_0\ge20\), |Θ₀|≥3, κ≥2, γ≤0.15 |
| D | corpus FA3 points with κγ spread |
| Phase 2 | top-20 late rows + default re-run with `settle_extra=20` |

| result | value |
|---|---:|
| unique rows | 710 |
| physical | 685 |
| max late (re-entry window) | **2.8701** |
| max settled (long) | **0.1143** |

### [B] 1D GPE late ⟨Θ⟩

| setting | value |
|---|---|
| cases | 14 (A,v₀,R) including high-A and R-variation |
| grid | N=768, L=80, T_MAX=16 |
| clean gate | dE < 5% |
| max late (clean) | **0.0265** |
| raw local max | ~3000 (not S1) |

### [C] Spherical light Θ probe

| setting | value |
|---|---|
| cases | (A,v₀)=(5,1), (20,1) |
| grid | N=1000, L=80 (light — not production M6 N=8000) |
| clean | **0 / 2** (energy failed) |
| density turn | YES |
| quotable for S1? | **NO** |

Corpus production spherical focusing remains in `bounce_m6_rebound_gp.py` / `dst.py` (separate O6/MeV question). This package does **not** promote light unclean rows.

### [D] 2D pancake

| setting | value |
|---|---|
| grid | 384×96, T_MAX=14 (reduced transverse class) |
| ⟨Θ_xx⟩ late | 3.46×10⁻² |
| ⟨Θ_yy⟩ late | ~10⁻⁶ (passive) |
| dE | ~0 |

### [E] Averaging

| mode | result |
|---|---|
| static double-bump | stress_drive > 0; mean Θ ~ 0.018 |
| dynamic CG (V=2,V2=0.6 IC) | turn YES; late ⟨Θ⟩ ~ 0.032 |

---

## 2. What is still not stocked

| missing | note |
|---|---|
| Full production **3D** GPE with coarse ⟨Θ⟩ late readout | N3 instrument gap |
| Energy-clean spherical Θ_lock scan at M6 N=8000 class | optional next, not done here |
| Derived κ,γ from GPE | still toy reduced |

---

## 3. Illegal readouts rejected

| fake land | disposition |
|---|---|
| 0D \|Θ\| cap hits | rejected (`hit_cap`) |
| overshoot > 100 | rejected |
| Madelung raw local Θ ~ 10³ | diagnostic only |
| 1D rows with dE ≥ 5% | excluded from clean max |
| spherical light dE ≫ 5% | unquotable |
| peak ≥ lock alone | not S1 |

---

## 4. Comparison to prior N3 package

| metric | `n3_theta_3d` | this deepen |
|---|---:|---:|
| max late 0D | 1.80 | **2.87** |
| stocked default late | 0.062 | 0.061 |
| 1D late max | ~0.001 | 0.027 |
| Θ_lock late reached | NO | **NO** |
| production 3D | False | **False** |

Harder legal push improves late O(1) ceiling slightly; does **not** close S1.
