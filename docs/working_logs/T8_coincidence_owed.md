# T8 coincidence problem — OWED
1. THE CLEANER √3 (internal review explicit ask): present the Γ²=3H_Λ² derivation stand-alone from the recorded KP-sequester object (paid below — the √3 page) — one page, real signs, no "asserted" residue.
2. The branching O(1): thaw = √3·B, B ∈ [0,1] (paid below — B = 1/√2 derived) — derive or bound B tighter.
3. Propagate the 20% floor into the timing's error band (how sharp is "why now" quantitatively?).
4. The cycle-level re-pose (why THIS cycle) — tighten the early-cycle bookkeeping's lean.

Coupling-geometry status: background-level (no gate exposure).

---


## Item 1 — PAID (2026-07-17 walk)

Stand-alone page with real GR signs: [PRTOE_sqrt3_derivation.md](../PRTOE_sqrt3_derivation.md).

**What the walk closed.**
- Γ_par = M_GC²/M_red, M_GC⁴ = ρ_inf, 3H_Λ²M_red² = ρ_inf ⇒ **Γ_par/H_Λ = √3** exactly, value-independent.
- The old "asserted residue" (coefficient 1 / par) is identified: Γ_par is the IR/critical-k scale; the thaw growth rate is ω_J (item 2).
- KP-sequester scope stated honestly: KP **fails** as a Λ-value fix; this page only reuses the one-scale floor that KP was asked to seat.


## Item 2 — PAID (2026-07-17): B = 1/√2 derived

The registered form is Γ_eff = B · √3 · H. **B = 1/√2** exactly.

| claim | status |
|---|---|
| Homogeneous P(X) gives 1+w ~ a⁻³ (settling) | derived — wrong sign for Route-D |
| Route-D thaw needs an instability source | structural |
| Dispersion ω² = −4πGρ + (α/M²)k⁴ ⇒ most-unstable γ → ω_J | derived |
| ω_J = Γ_par/√2 = √(3/2)·H | derived from M_red² = 1/(8πG) |
| **B = 1/√2** | **PICKED / DERIVED** |
| B = 1 as thaw rate | discarded (IR scale ≠ growth rate) |
| B ≈ 0.34 / 0.25 as thaw rate | discarded (δ-drag, not background thaw clock) |

t_turn = ln(1/√A_s)/(√(3/2)·H) ≈ **8.16 H⁻¹** at A_s = 2.088×10⁻⁹.

**Still do not** set `dcdf_floor_thaw = B·√3` (amplitude ≠ rate).


## Item 3 — PAID (2026-07-20): the timing's error band

The item's stated input is superseded: the floor is no longer 20% but **+0.44%** on the
kernel-sourced τ (P-2026-048), which makes the propagation cheap rather than dead.

**t_turn: 8.1597–8.1611 H⁻¹, a 0.02% bracket.** √3 and B = 1/√2 are exact and ρ_Λ does not
appear in ln(1/√A_s)/(√(3/2)·H) at all — *in Hubble units the width is floor-independent*, so
A_s is the only input that can carry an error. Exact sensitivity: δt/t = δ(ln A_s)/|ln A_s| =
δ(ln A_s)/19.99 — the logarithm divides any amplitude error by twenty (a 10% A_s error buys
0.5% on the width). The bracket is the corpus's own two live values: frozen A_s = 2.088×10⁻⁹
(`scripts/audit_math_pass.py:69`) → 8.1597; closed form, −0.35% (`:365–367`, harness row) →
8.1611. *No external A_s error bar is used — none is sourced in this repo; the yaml `logA`
entries are sampling priors/refs, not posterior widths.* The floor's only channel is the
*absolute* duration: H_Λ ∝ (ρ_Λ¼)², so +0.44% ⇒ −0.87% in years.

**Occupancy 2.68% (1 in 37.3); floor band ±2.2% ⇒ 1 in 36.5–38.2.** Quoted in H_Λ⁻¹ throughout —
t_turn is a dark-energy-era quantity, so the elapsed time must be in the same clock (0.219 H_Λ⁻¹,
not 0.262 H₀⁻¹); mixing them gives the superseded 3.43%. The elapsed fraction
depends on Ω_Λ/Ω_m alone — at ρ_m = ρ_Λ the flat-ΛCDM age integral's argument is exactly 1,
arcsinh(1) = ln(1+√2), so the crossing enters convention-free. Sensitivity computed at this
file's own crossing z ≈ 0.33 ⇒ Ω_Λ/Ω_m = (1.33)³ = 2.3526: d ln f/d ln(Ω_Λ/Ω_m) = 1.26. The
floor enters at the fourth power: +0.44% on ρ_Λ¼ (derived at
[PRTOE_koide_relation.md](../PRTOE_koide_relation.md) §, T_c = 177.10 keV ⇒ ρ_Λ¼ = (9/2)α⁴T_c
= 2.2599 meV vs observed 2.25) ⇒ +1.77% on ρ_Λ. **Not carried**: Ω_m's own measurement error
enters the same ratio and is a separate propagation — no value for it is sourced in this repo.

Recorded in [PRTOE_coincidence_problem.md](../PRTOE_coincidence_problem.md) §1.2 and §1.3.
**The answer to "how sharp is why-now quantitatively": the width is sharp to 0.07% and the
occupancy odds to under one unit in thirty — the floor is no longer the limiting uncertainty
anywhere in the timing.**

**Item 4 remains open.**
