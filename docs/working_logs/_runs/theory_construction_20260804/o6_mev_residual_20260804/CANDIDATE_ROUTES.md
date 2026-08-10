# CANDIDATE_ROUTES — O6 MeV funding shapes (double-kill)

**Package:** `o6_mev_residual_20260804`  
**Date:** 2026-08-04  
**Role:** inventory **routes** that could fund MeV over keV; kill-seek each (can-exist + should-not-exist)  
**Script scores:** [`logs/bounce_o6_mev_gap.log`](logs/bounce_o6_mev_gap.log) channels C0–C11  
**Fences:** no free \(N_\mathrm{med}/\eta\) as land · no invent MeV · no bounce closed by O6 alone

**Demand source:** [`WHAT_RESIDUAL_DEMANDS.md`](./WHAT_RESIDUAL_DEMANDS.md)

---

## Grade legend

| Tag | Meaning |
|---|---|
| **can-exist** | Why framework *might* permit the route |
| **should-not-exist** | Strongest adversarial kill |
| **double-kill** | Two independent kill axes (preferred) |
| **status** | Immediate disposition this package |

---

## R1 — Door budget alone (legal M2 \(\rho_\mathrm{eff}\))

**Statement:** Exit shear+radiation \(\rho_\mathrm{eff}\) already is the reheat bath.  
**can-exist:** Door is a stocked FRW+shear state.  
**should-not-exist:** \(T_\mathrm{eff}\sim2.83\,\mathrm{keV}\); \(\rho_\mathrm{MeV}/\rho_\mathrm{eff}\sim5.54\times10^{10}\).  
**double-kill:** (i) scale fail · (ii) even perfect shear→heat stays keV (M2.C).  
**status:** **DEAD-as-close** · C0 FAIL-scale

---

## R2 — Condensate floor as heat bath

**Statement:** \(\rho_\mathrm{bounce}=m^4/\lambda\) supplies MeV radiation.  
**can-exist:** Floor is PAID finite density.  
**should-not-exist:** Wrong object (ceiling ≠ radiation bath); \(T_\mathrm{bounce}\sim1.06\,\mathrm{keV}\) colder than door \(T_\mathrm{eff}\); gap \(\rho\sim2.8\times10^{12}\).  
**double-kill:** (i) wrong-object · (ii) scale fail (H4).  
**status:** **DEAD** · C1 WRONG-OBJECT+FAIL-scale

---

## R3 — Radiation piece only at door

**Statement:** Use \(\rho_\mathrm{rad}\) (no shear) as hot start.  
**can-exist:** Stocked radiation component.  
**should-not-exist:** \(T_\mathrm{rad}\sim146\,\mathrm{eV}\) — **worse** than \(T_\mathrm{eff}\).  
**double-kill:** (i) colder · (ii) not a reheat law.  
**status:** **DEAD-as-close** · C2 FAIL-scale

---

## R4 — 1D / medium overshoot compression

**Statement:** Verified rebound overshoot multiplies density enough for MeV.  
**can-exist:** Overshoot measured O(1) in 0D/1D (M6 class).  
**should-not-exist:** overshoot \(\sim1.34\) vs need \(\sim10^{10}\) in \(\rho\).  
**double-kill:** (i) O(1) only · (ii) free cosmological \(N_\mathrm{med}\sim6\) retired by measured overshoot.  
**status:** **DEAD-as-close** · C3 FAIL-scale

---

## R5 — Quench / door mode creation

**Statement:** Squeezed medium quanta at \(k\xi\lesssim2.5\) inject MeV energy.  
**can-exist:** Translation-table quench priced.  
**should-not-exist:** \(\rho_\mathrm{quench}\sim9\times10^{-84}\,\mathrm{eV}^4\) — ~97 orders under **door**.  
**double-kill:** (i) wrong scale · (ii) channel closed by pricing (task5).  
**status:** **DEAD** · C4

---

## R6 — Electron-family gate clock

**Statement:** Re-entry pegged at \(T_c\) or \(m_e\) legalizes MeV (or near-MeV).  
**can-exist:** Electron contact \(\Gamma/H\sim10^{16}\)–\(10^{17}\) stocked; \(T_c=\tau m_e\) family.  
**should-not-exist:** \(T_c\sim177\,\mathrm{keV}\), \(m_e=511\,\mathrm{keV}\) — under MeV by \(\times5.6\) / \(\times2.0\) in \(T\); no mechanism selects the gate; NEC-nonnegative electron lane cannot turn geometry.  
**double-kill:** (i) under bar · (ii) unselected clock + turn-by-class fail.  
**status:** **CANDIDATE-clock-only** · not MeV fund · C5/C6

---

## R7 — Spherical geometric focusing \(F\)

**Statement:** 3D spherical compression supplies volume focus \(\gtrsim10^{9}\)–\(10^{11}\).  
**can-exist:** Inhomogeneous concentration is a legal *shape* (H3).  
**should-not-exist:** Energy-clean instrument ceiling \(\lesssim25\times\); need \(\sim5.5\times10^{10}\) from door; adaptive grid unquotable (energy 22–1817%); patchy hot start → Tolman/BBN bookkeeping new problem.  
**double-kill:** (i) instrument ceiling · (ii) unresolved + BBN patchiness.  
**status:** **OPEN method bar / FAIL on current instruments** · C7 · reopening needs energy-clean \(F\gtrsim10^{9}\)

---

## R8 — Free \(N_\mathrm{med},\eta\) Phase-II compression (M2 knobs)

**Statement:** \(\rho_\mathrm{out}=\eta\,\rho_\mathrm{in}\,e^{4N_\mathrm{med}}\) with \(N_\mathrm{med}\gtrsim6.18\), \(\eta=1\).  
**can-exist:** As **labeled fabrication** for sensitivity only.  
**should-not-exist as land:** Closes MeV by dial; not microphysics; **sign-conflicts** S2 late-lock (\(N_\mathrm{med}\approx-2.62\)).  
**double-kill:** (i) honesty / fabricated · (ii) sign conflict with F-A2 dial.  
**status:** **FABRICATED — KILLED as Derived** · C8

---

## R9 — \(N_\mathrm{med}=1/c_s\) as Derived identity

**Statement:** Medium sound speed supplies the needed e-folds.  
**can-exist:** Numerical near-coincidence at operating point (\(N_\mathrm{med}/(1/c_s)\approx0.915\)).  
**should-not-exist:** M2b \(c_s\) scan: ratio runs ~0.3→5; \(T_\mathrm{reheat}\) scan tracks \(\ln T\), not medium constant.  
**double-kill:** (i) coincidence not identity · (ii) still a free compression if sold as law.  
**status:** **COINCIDENCE — KILLED as identity** · C9

---

## R10 — SM two-scale bath (task #14)

**Statement:** Photons are Goldstone/substrate modes; SM energy passes through metric-off interval conserved and already blueshifted to MeV by pre-door contraction.  
**can-exist:** Two-scale reading forced by photon propagation vs \(\xi\); portals tiny.  
**should-not-exist (as close):** Arrives at doors at **146 eV–keV** on computed budgets unless contraction **already** funded MeV *before* the door — then O6 is a different book (genesis), not door funding. Unwritten full dynamics.  
**double-kill:** (i) still cold at door on stocked numbers · (ii) shifts residual to pre-door funding without deriving it.  
**status:** **OPEN-SCHEMA** · C10 · not a land this package

---

## R11 — Genesis cascade / pre-door MeV (task #11)

**Statement:** Hot start is funded by prior-cycle / cascade dynamics before shear door; O6 not the door’s job.  
**can-exist:** Explicit post-task5 funding move in reconstruction §23.  
**should-not-exist (as close):** Dynamical half open; not simulated; must not be sold as Derived without instrument.  
**double-kill:** (i) MISSING dynamics · (ii) does not close bounce O2 by itself.  
**status:** **OPEN-SCHEMA** · primary surviving *shape* for deeper work · C11 · **not** a land

---

## R12 — Multi-component split (condensate floor + Tolman radiation)

**Statement:** Two-component bookkeeping: keV condensate floor + radiation component that stayed hot.  
**can-exist:** Named OPEN in `rho_bounce.py` docstring; consistent with two-scale idea.  
**should-not-exist (as close):** Radiation component’s **arrival temperature** still needs a legal law; without it this is residual rename.  
**double-kill:** (i) empty law · (ii) floor still not MeV.  
**status:** **OPEN-SCHEMA bookkeeping** · not a land

---

## Summary table

| ID | Route | Immediate grade | Land? |
|---|---|---|---|
| R1 | Door \(\rho_\mathrm{eff}\) | DEAD-as-close | **No** |
| R2 | Floor heat bath | DEAD | **No** |
| R3 | Door \(\rho_\mathrm{rad}\) | DEAD-as-close | **No** |
| R4 | 1D overshoot | DEAD-as-close | **No** |
| R5 | Quench | DEAD | **No** |
| R6 | Electron clock | CANDIDATE-clock-only | **No** |
| R7 | Spherical \(F\) | INSTRUMENT-CEILING / unquotable | **No** |
| R8 | Free \(N_\mathrm{med}/\eta\) | **FABRICATED kill** | **No** |
| R9 | \(N_\mathrm{med}=1/c_s\) | **COINCIDENCE kill** | **No** |
| R10 | SM two-scale | OPEN-SCHEMA | **No** |
| R11 | Genesis cascade | OPEN-SCHEMA | **No** |
| R12 | Multi-component split | OPEN-SCHEMA bookkeeping | **No** |

**Count:** 12 routes scored · **0** legal MeV lands · **0** bounce closes.

---

## Explicit non-claims

- No route above is Derived MeV.  
- OPEN-SCHEMA is residual shape, not promotion.  
- Free knobs remain labeled fabricated.

---

*End CANDIDATE_ROUTES.md*
