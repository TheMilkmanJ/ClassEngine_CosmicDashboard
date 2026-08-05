# REQUIRED_INPUTS — Microphysics missing for forward ω_J

**Package:** `theory_construction_20260804/omegaJ_forward`  
**Date:** 2026-08-04  
**Rules:** do not invent numeric χ, J_seat, or pinning curvature; do not silent-ID v_L or f→χ  
**Canonical formalization:** transfer-integral stage 8; `PRTOE_baryogenesis.md` §3a

---

## 1. Exact missing objects

Forward land of junction plasma frequency requires **one** of the following packages (equivalent for ω_J):

### Package A — direct micro frequency (minimal statement)

| Symbol | Meaning | Corpus state |
|---|---|---|
| **ω_J** | Junction plasma frequency of the *seat term* at T_sph | Named as free parameter of U_J formalization; **no independent micro price** |

If ω_J is supplied by seat microphysics as a derived scale (not from η), the rectifier then computes R without circularity.

### Package B — stiffness + curvature (micro definition of Package A)

Stage-8 formalization:

```
χ Γ_φ · φ̇ = −U′(φ)
U_pin = −χ m₁² cos φ
U_J   = −χ ω_J² cos(φ − θ̇ t)
```

| Symbol | Meaning | Independence condition | Corpus state |
|---|---|---|---|
| **χ** | Junction-phase stiffness / “decay constant” of the *visible-side* phase in this formalization | Must be fixed by seat/junction micro content **without** η, R_need, or silent reuse of unrelated decay constants | **Unstated numeric**; cancels from EOM so rectifier never constrains it |
| **Pinning curvature of U_J** (or **J_seat**) | Curvature of the cos(φ − θ̇t) seat term at the extremum; equivalently the seat coupling energy density scale that sets ω_J² = J_seat/χ | Must be independent of R_need / η and independent of back-solved j | Stage 7 *names* J; stage 8 **never numbers** it without ω_J |
| **ω_J² ≡ J_seat / χ** | Definition linking the two | Ratio is what R cares about; absolute χ alone is insufficient | Underdetermined until *both* legs or the ratio are supplied |

**A_ωJ (single missing axiom):** at T_sph, the seat–visible junction supplies an independent microscopic price of **either** ω_J **or** the pair (χ, J_seat) with the definition above, **without** reference to η, R_need, or declined IDs (v_L, f→χ, …).

This is **one** axiom, not two independent gaps for the purpose of ω_J: χ and J_seat enter only as a ratio. Supplying both or supplying ω_J direct closes the same residual.

---

## 2. Seat model requirements (what “new microphysics” means)

A construction-grade seat model that could feed A_ωJ must specify, at minimum:

1. **Operator / term** that is the tenth-channel seat junction (corpus already selects this *class* as the junction portal; it does **not** price ω_J).
2. **Phase content** of the visible side that enters φ (the phase conjugate to visible lepton number in the overdamped EOM).
3. **How the cos(φ − θ̇t) term is generated** from UV / IR matching at T_sph — enough structure to extract either ω_J or (χ, J_seat).
4. **Independence from the Majorana pin:** U_pin = −χ m₁² cos φ prices *p*, not *j*. m₁ is stocked (~2.25 meV) and is the rectifier’s **off switch**, not its prefactor (stage 8). Do not confuse U_pin curvature with U_J curvature.
5. **Independence from η:** no fitting of ω_J to R_need after the fact, and no re-import of the back-solve as “micro.”

Out of scope for A_ωJ alone (do not pretend they replace it):

- Pinning L_gen / n band (#180) — moves 𝒯 / exact keV target, does not create first-principles ω_J.
- Second un-rotatable phase counting (I = n₂φ₁ − n₁φ₂) — sign structure; does not supply the second term or ω_J.
- Thermal leptogenesis — route already empty / retired.

---

## 3. Independence conditions (hard)

A candidate expression for ω_J (or for J_seat/χ) is **legal** only if:

| # | Condition |
|---|---|
| I1 | Inputs do **not** include R_need, η, or j-as-back-solved from them |
| I2 | Inputs do **not** use the stale ratio Γ_φ/θ̇ ~ 10⁷ as data (computed ratio is 9.03×10⁷) |
| I3 | χ is not silently identified with v_L (MeV / GeV / 2.4 TeV) — **declined** (#39) |
| I4 | χ is not silently identified with electron-coupled scalar f (~100–500 TeV) without an **explicit new** map |
| I5 | Jeans ω_J = √(4πGρ) is not relabeled as junction ω_J (naming collision only) |
| I6 | U_pin curvature (∝ m₁²) is not sold as U_J curvature |
| I7 | √(m₁ Γ_φ), T_on, or other proximity scales are not adopted without a mechanism chain written in the model |

Violating I1–I2 → **CIRCULAR**. Violating I3–I4 → **FORBIDDEN ID**. Violating I5–I6 → **WRONG OBJECT**. Violating I7 → **MISSING AXIOM** dressed as land.

---

## 4. Circularity traps (named)

| Trap | How it looks | Why circular / illegal |
|---|---|---|
| **η-bootstrap** | ω_J = √(2 R_need Γ_φ θ̇) presented as derivation | R_need is the thing ω_J is supposed to explain |
| **j-bootstrap** | Fix j from R = j/(2θ̇), then “derive” ω_J = √(j Γ_φ) | Same information as η-bootstrap |
| **Tautology C8** | √(θ̇ Γ_φ) × √(2R) | Algebra of C0 only |
| **Stale-ratio basin** | Land at ~1.9 keV under Γ/θ̇=10⁷ | Artifact; fails transmission on real Γ_φ |
| **Stage-7 m₁ watch** | R ~ (m₁/θ̇)·F | Stage 8 killed: overdamped pin is m₁²/Γ_φ; R carries no m₁ |
| **v_L manufacture** | Set decay constant = v_L, solve for χ | Explicitly declined as manufactured derivation |
| **f→χ smuggle** | Reuse electron-scalar decay constant as junction χ | Different sector; new ID required if ever claimed |
| **Quartet ⇒ derived** | “Four numbers close ⇒ ω_J known from first principles” | Three legs force residual; residual is still back-solved |
| **Proximity adoption** | √(m₁ Γ_φ)≈3.5 keV or T_on≈9.4 keV as land | Chance / timing proximity; no seat-chain |

---

## 5. What is already independent (do not re-derive as the residual)

| Object | Value (recompute 2026-08-04) | Type |
|---|---|---|
| Γ_φ | 5.3902×10⁹ eV | COMPUTED |
| θ̇ | 59.68 eV | COMPUTED |
| Γ_φ/θ̇ | 9.0319×10⁷ | COMPUTED |
| m₁ | ~2.25 meV | RECORDED (pins *p*, not ω_J) |
| R_need | ~5×10⁻⁵ | FROM η·n band (grading only for forward work) |
| Overdamping / pin hierarchy / fast-drive | hold | premises of class, not price of ω_J |

---

## 6. Minimal construction checklist (for a future A_ωJ write-up)

A write-up that claims to close #39 must include **all** of:

- [ ] Explicit operator / micro definition of the seat junction at T_sph  
- [ ] Independent expression or lattice/micro computation for **either** ω_J **or** (χ, J_seat)  
- [ ] Proof that η / R_need did not enter the expression  
- [ ] No use of declined IDs (v_L, silent f→χ) unless a **new named axiom** is declared and graded as such  
- [ ] Numeric result scored **only** against pre-registered band (`KILL_AND_BANDS.md`)  
- [ ] Perturbative check j/θ̇ ≪ 1 at the landed value (target region ~10⁻⁴)  

Until every box is honest, residual stays **OPEN-BLOCKED**.

---

*End REQUIRED_INPUTS.md*
