# S2 — ρ_re/ρ_eff suppression without dial (2026-08-04)

**Package:** `s2_rho_suppression_20260804/`  
**Script:** `scripts/bounce_s2_rho_suppression_hunt.py`  
**Log:** [`logs/s2_rho_suppression_hunt.log`](./logs/s2_rho_suppression_hunt.log)  
**Fences:** no free \(N_\mathrm{med}/\eta\) as Derived · no invent H_re · no bounce closed  
**COMPLETE lands: 0**

---

## 0. One-liner

**16 stocked/fab candidates for \(S=\rho_\mathrm{re}/\rho_\mathrm{eff}\): 0 legal lands. Need \(S\sim2.8\times10^{-5}\) (late) or \(7.3\times10^{-3}\) (Θ=1). Closest stocked magnitude \(\rho_\mathrm{rad}/\rho_\mathrm{eff}\sim7\times10^{-6}\) is WRONG-OBJECT. Free \(N_\mathrm{med}\) killed.**

---

## 1. Required suppression

| target | \(S=\rho_\mathrm{re}/\rho_\mathrm{eff}\) |
|---|---|
| late \(\Theta\sim0.062\) lock | **2.80×10⁻⁵** |
| \(\Theta=1\) lock | **7.30×10⁻³** \(=(c_s/\sqrt3)^2\) |

---

## 2. Headline kills / near-misses

| class | example | verdict |
|---|---|---|
| acoustic powers | \(c_s^2,c_s^4\) | DEAD-as-law (scale wrong / no law) |
| mixmaster \(e^{-4N_\mathrm{mix}}\) | \(N_\mathrm{mix}\approx6.26\) derived | **wrong arrow** (contraction ≠ dilution) |
| door \(\rho_\mathrm{rad}/\rho_\mathrm{eff}\) | \(\sim7\times10^{-6}\) | **WRONG-OBJECT** (near late scale, not re-entry law) |
| free \(N_\mathrm{med}\) | −2.62 late / +6.18 MeV | **FABRICATED** (opposite signs!) |
| inverse \((H_\mathrm{kin}/H)^2\) | exact late | **TAUTOLOGY** |
| quench channel | \(\sim10^{-97}\) | wrong scale |

**Pop-out:** MeV dial wants **positive** \(N_\mathrm{med}\); late magnitude lock wants **negative** \(N_\mathrm{med}\). One fabricated knob cannot honestly serve both O6 and F-A2.

---

## 3. Grade

| claim | grade |
|---|---|
| Derived \(S\) law from stocked parts | **false** |
| Free \(N_\mathrm{med}\) as F-A2 | **KILLED** |
| Obstruction C | **stands** |
| COMPLETE | **0** |
