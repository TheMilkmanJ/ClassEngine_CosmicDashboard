# Γ/H = √3 — the One-Page Derivation (2026-07-11; walked 2026-07-17)

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


*A cleaner derivation of the asserted √3, presented as the recorded object (the KP-sequester
solve, #46; value-independent form). Three lines, one honest flag. Status: the derivation as
recorded, with its single O(1) assumption named rather than hidden.*

## The chain

**Line 1 — the rate.** The floor's Jeans/thaw instability is the ghost-condensate sector
coupling to itself gravitationally. A sector whose only scale is M_GC, coupling at
gravitational strength (through M_red — the only coupling channel, L1), has the unique
dimensionally-forced rate:

 Γ_par = M_GC² / M_red

**Line 2 — single-scale-ness.** The fluid is ONE-parameter (ρ_inf is its only scale — the same
one-scale identity that sharpened the f-sum and priced the vacuum): the ghost-condensate scale
IS the floor's quantum,

 M_GC⁴ = ρ_inf (exactly — no second scale exists to displace it)

**Line 3 — Friedmann at the floor.** At Λ-domination the Friedmann equation reads
3H_Λ²M_red² = ρ_inf. Substitute:

 Γ_par² = M_GC⁴/M_red² = ρ_inf/M_red² = 3H_Λ² ⟹ **Γ_par/H_Λ = √3.**

The √3 is the Friedmann factor itself: the instability rate is the geometric combination
M_GC²/M_red, and the same ρ_inf appears in both the rate's numerator and the Hubble rate's
definition — the ratio cannot help being √3. This is why the result is VALUE-INDEPENDENT
: ρ_inf cancels. Nothing about the floor's magnitude enters — only its
one-scale-ness.

---

*walk 2026-07-17 — real signs, B picked.*

## Real signs: what "coefficient 1" actually is

The algebra above is exact **given** Γ = M_GC²/M_red with coefficient 1. That object is the
**IR modification / critical-k scale** of ghost-condensate gravity (Arkani-Hamed et al. 2004:
m ~ M²/M_Pl). The physical **growth rate** of the unstable mode is not Γ_par itself.

With M_red² = 1/(8πG) and ρ = ρ_inf:

| quantity | value | role |
|---|---|---|
| Γ_par = M_GC²/M_red | √3 · H_Λ | IR scale / critical wavenumber |
| ω_J = √(4πG ρ) | √(3/2) · H_Λ = Γ_par/√2 | growth rate of most-unstable mode |
| **B ≡ ω_J/Γ_par** | **1/√2** | branching prefactor in Γ_eff = B·√3·H |

*Derivation of ω_J (real signs).* 4πG ρ = ρ/(2 M_red²), H_Λ² = ρ/(3 M_red²) ⇒ ω_J/H_Λ = √(3/2)
exactly. No free coefficient, no fit.

## Why B = 1/√2 is the thaw rate (picked, not working-estimate)

**A homogeneous ghost condensate cannot source the thaw branch** (route D: w₀ ∈ [−0.92, −0.86] with wₐ < 0, the dark energy leaving its floor rather than settling onto it)**.** For shift-symmetric P(X), the
Noether charge implies eps = X−X0 ~ a⁻³ near the minimum ⇒ 1+w ~ a⁻³ — *settling to* the floor.
The thaw branch wants 1+w ~ a⁺³ — *leaving* the floor. Homogeneous EOM alone is the wrong sign.

**What sources thaw: the Jeans instability under self-gravity.** Dispersion of fluctuations
about the critical point (c_s = 0, with the (δK)² stabilizer):

 ω² = −4πG ρ + (α/M_GC²) k⁴

- Short λ: k⁴ stabilizer ⇒ stable (the floor holds locally).
- Long λ: gravity wins ⇒ unstable.
- Most unstable mode is the IR: as k → 0, ω → ω_J = √(4πG ρ).
- Γ_par sets *where* the turnover sits (which k is marginal), **not** the e-folding rate of the
  unstable branch.

Therefore **Γ_eff = ω_J = Γ_par/√2**, i.e. **B = 1/√2**.

**Discarded as thaw-rate candidates:**
- **B = 1** — confuses the IR/critical-k scale with the mode growth rate.
- **B ≈ 0.336, 0.252** (de Sitter linear δ-growth with 2H/3H drag) — correct for density
  *contrast* accumulation, wrong for the thaw *rate*. Hubble drag on δ is a separate layer
  already present in a(t) and in t_turn = ln(…)/(B√3 H); using it as B double-counts expansion.
  Those values remain available for δ-growth (e.g. P-024 dipole sizing), not for the thaw clock.

## Timing with the picked B

 t_turn = ln(1/√A_s) / (B · √3 · H) = ln(1/√A_s) / (√(3/2) · H)

At A_s = 2.088×10⁻⁹: **t_turn ≈ 8.16 H⁻¹** (was 5.77 at B = 1). The logarithm still dominates;
why-now stays dial-free.

**Do not identify** `dcdf_floor_thaw` with B·√3 — the code parameter is 1+w today (amplitude of
how far nonlinear the mode has grown); B·√3 is the rate in units of H (the clock).

## Connection to KP-sequester (honest scope)

The KP (Kaloper–Padilla) self-consistency solve **fails** as a mechanism for the residual Λ
*value* (Ω_Λ/Ω_m capped at ~0.40 vs observed 2.2 —
[PRTOE_cosmological_constant.md](PRTOE_cosmological_constant.md) §4b,
[scripts/de_value_kp_selfconsistency.py](../scripts/de_value_kp_selfconsistency.py)). That kill is
untouched. What this page uses from that object is only the **one-scale floor** sitting in the
Friedmann equation — the same ρ_inf the KP solve was asked to fix and could not. The √3 is a
statement about the floor's *rate*, not a resurrection of KP as a value-fix.

## Sources

[ArkaniHamed2004] (the ghost condensate; the IR scale m ~ M²/M_Pl this page identifies as Γ_par),
[KaloperPadilla2014] (the sequestering solve whose one-scale floor is the only piece used here).
Full list: [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md).

## The result

A one-scale sector coupling at gravitational strength through the only channel has IR scale
Γ_par/H = √3 (Friedmann factor, exact) and unstable-mode growth Γ_eff/H = √(3/2) (Jeans, exact).
**B = 1/√2 is derived.** The universe's linewidth is √(3/2) because the budget and the mode's
growth rate are the same ρ_inf read through 4πG rather than through the critical-k combination.
