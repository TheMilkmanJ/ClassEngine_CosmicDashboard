# FILL_ATTEMPT — `alpha_d_or_electric_projection`

**Package:** `theory_construction_wave_20260805/wilson/`  
**Track:** T-W5 Wilson  
**Date:** 2026-08-05  
**Requirement:** coupling \(\alpha_d\) **or** electric projection of the connection, without free dial  
**Fence:** NO FABRICATIONS · bound ≠ fixed coupling · pure-gauge alone collapses  

---

## 1. Corpus hunt (file:line)

| Probe | Result | file:line |
|---|---|---|
| Stability bound | \(\alpha_d\lesssim 2.2\) at working spacing — **window, not fixed coupling** | `docs/exploratory/PRTOE_forced_combination.md:55–56`, table `:214` |
| Pure-gauge ring | **collapses** (no stationary point) | `PRTOE_forced_combination.md:19–20`, `:50–51` |
| Hybrid required | gauge–superfluid hybrid; connection **not constructed** numerically as \(A\) | `PRTOE_forced_combination.md:19–20`, `:54–59` |
| Adjoint \(\varepsilon^{abc}\) algebra | exact algebra ≠ field configuration | `PRTOE_forced_combination.md:32–36`, `:40–46` |
| Retracted \(\alpha_\mathrm{dark}\approx 3.2\) | **RETRACTED** (wrong-sign balance) — not a fill | `docs/working_logs/T6_koide_owed.md:1290` (retraction context); inventory refuses dial |
| Balance form \(E(d)=\sqrt{3}\sigma d-3\tilde q^2\ln d-3\alpha_d/d\) | structure with \(\alpha_d\) as free-ish coupling in window | `T6_koide_owed.md:1299–1300` |
| Inventory status | **PARTIAL** | `scripts/koide_wilson_holonomy_inventory.py:122–129` |
| Prior T7 | **PARTIAL** | `desk_t7/WILSON_HUNT.md:81–92` |

---

## 2. Status

| Label | Value |
|---|---|
| **Status** | **PARTIAL** |
| Fills zero-knob? | **No** |
| Free dial used? | **No** |

**Not PRESENT:** no fixed \(\alpha_d\) and no hybrid connection field on disk. Bound + algebra ≠ electric projection ready for \(\theta_W\).

---

## 3. Licensed fill path (without free dial)

| Licensed fill | Still forbidden |
|---|---|
| Fixed coupling from lattice / dual-superconductor profile at the **same** scale as \(A_\mu\) | Using \(\alpha_d\) bound **edge** as dial to hit \(2/9\) |
| Constructed hybrid connection (pure gauge alone collapses by forced-combination theorem) | Pure-gauge-only Wilson as if licensed for the ring |
| Explicit electric-projection map \(A\mapsto A^\mathrm{elec}\) with **no** free coefficients aimed at Brannen sheet | Retracted \(\alpha_\mathrm{dark}\approx 3.2\) restored as fill |
| Same campaign as `dark_SU2_A_mu` fill | Fit projection to lepton masses |

---

## 4. What would count as filled

- Numeric fixed \(\alpha_d\) (or projection kernel) **not** chosen from the stability window edge to land \(\theta_W\); **and**  
- Hybrid (or other licensed) connection consistent with forced-combination, co-archived with \(A_\mu\).

**Today:** **PARTIAL**.

---

## 5. Fill attempt verdict

> **Fill refused as PRESENT.** Stability window + algebra only; hybrid unbuilt; \(\alpha_d\) unfixed. Status remains **PARTIAL** (blocks zero-knob).

*End FILL_ATTEMPT_alpha_d_or_electric_projection.md*
