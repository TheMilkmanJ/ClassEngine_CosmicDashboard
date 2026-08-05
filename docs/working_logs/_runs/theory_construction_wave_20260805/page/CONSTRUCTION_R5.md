# CONSTRUCTION_R5 — TMS×BS co-modulation candidates (non-factorized)

**Package:** `docs/working_logs/_runs/theory_construction_wave_20260805/page/`  
**Date:** 2026-08-05  
**Scope:** R5 only — candidate **classes** of single-microphysics TMS×BS co-modulation (non-factorizable) that *could* be admitted for future write-once scoring  
**Priors:** `desk_t6_page_micro_20260804/R1_R2_R5.md` · residual R5 · D4 map · F1 S⋆ fence · champion v13 schedule `v22_near_joint_polish` (factorized pins)  
**Champion residual (arrays reconfirm this package):** range/\(S_\star\) = **0.113154…** on bin **[0.10, 0.11)** (need ≤ **0.10**)  
**Fences:** NO FABRICATIONS · `page_curve_claimed: false` · no densify thrash · no coevolve production · leave MCMCs · no PolyChord · pure \(S_\star\) inflation **DEAD** (F1)  
**Stocked non-factorizable single-coupling micro Hamiltonian:** **none** → every candidate below remains **MISSING_INPUT**

---

## 0. Residual target (R5-specific)

R5 attacks the **factorization** of entangling and dump envelopes. Present construction (champion) uses independent schedule pins:

\[
w_{\mathrm{tms}}(f)\times w_{\mathrm{bs}}(f)
\quad\text{with free}\quad
G_{\mathrm{TMS}},\; G_{\mathrm{BS}},\; \text{shape powers}.
\]

Fail is an **overlap ratio** problem at \(f\sim0.057\)–\(0.072\); factorization makes early \(\mathrm{d}S/\mathrm{d}u\) a thrash surface under independent knobs.

| quantity | v13 value |
|---|---|
| Fail bin | **[0.10, 0.11)** |
| range (numerator) | **0.0018883423986319587** |
| \(S_\star\) (denominator) | **0.016688199517780646** |
| range/\(S_\star\) | **0.11315435176934464** |
| Need | ≤ **0.10** |

**What R5 must eventually do (if ever licensed):** supply **one** licensed microphysical Hamiltonian whose **one** time-dependent coupling simultaneously sets both channels (non-factorizable), so early \(\mathrm{d}S/\mathrm{d}u\) is not an independent ratio knob — jointly with T2+stall+DC3, without densify, without pure \(S_\star\) inflation (F1).

**Champion factorized pins (instrument; not co-mod law):**

| channel | pins |
|---|---|
| TMS | `G_TMS=0.37`, `TMS_START=0`, `TMS_END=0.52`, `TMS_SHAPE_POWER=2.6` |
| BS | `G_BS=4.4`, `BS_MILD=0.205`, `BS_RAMP_POWER=1.6`, `BS_START=0` |
| late dump | EXTRA_BS sweeps (start 0.42) — late reach, not co-mod micro |

---

## 1. Schema statement (unchanged; not derived)

> Present construction factorizes entangling and dump envelopes \(w_{\mathrm{tms}}(f)\times w_{\mathrm{bs}}(f)\) under independent header pins. Residual demands a **single licensed microphysical Hamiltonian** whose **one** time-dependent coupling simultaneously sets both channels (non-factorizable), so early \(\mathrm{d}S/\mathrm{d}u\) is not an independent ratio knob.

---

## 2. REQUIRED_INPUTS (must fill before implement/score as new dynamics)

| # | Input | Meaning | Stocked? |
|---|---|---|---|
| R5-I1 | **Single interaction / Hamiltonian term** | One operator generating both transfer and entanglement growth | **MISSING_INPUT** |
| R5-I2 | **Non-factorizable schedule** | Couplings **not** independent free \(G_{\mathrm{TMS}},G_{\mathrm{BS}}\) after the law | **MISSING_INPUT** |
| R5-I3 | **Smooth micro continuity** | Not D1 two-phase discontinuity rewritten as “one H” | **MISSING_INPUT** |
| R5-I4 | **O(1) parameter discipline** | No free \(g(f)\) with enough params to match any early slope | **MISSING_INPUT** |
| R5-I5 | **Joint-gate preservation plan** | How T2+stall+DC3+nulls survive co-modulation | **MISSING_INPUT** |
| R5-I6 | **F1 disclosure plan** | Early-bin range **and** \(S_\star\) vs v13 on any future T8_pass (class A/B only) | **protocol ON**; no artifact yet |

**Instrument already stocked (not substitutes):** champion v13 / `v22_near_joint_polish` schedule pins (not `coevolve_v23.json`).

---

## 3. Candidate TMS×BS co-modulation classes (construction dump)

These are **CANDIDATE classes** for kill-seeking scrutiny. **Not** Derived, **not** implemented, **not** claimed to clear T8. Highest conceptual cleanliness **if** content appears — still MISSING_INPUT now.

### R5-C1 — Single interaction Hamiltonian \(H_{\mathrm{int}}(t)\) generating both channels

| field | content |
|---|---|
| **Idea** | One interaction term on core⊗rad that produces **both** energy transfer (dump) and entanglement growth (TMS-like) from the same coupling \(g(t)\) derived from microphysics. |
| **Non-factor test** | After law, there is **no** independent free \(G_{\mathrm{TMS}}\) vs \(G_{\mathrm{BS}}\); one O(1) coupling sets both effective strengths. |
| **Why it might act** | Correlates numerator (\(S\)) and coordinate advance (\(u\)) from the *same* operator → breaks pure TMS-scale stickiness at structural level. |
| **can-exist** | Real microphysics often has one interaction generating transfer + entanglement; exploratory protocol treats factorized schedules as effective, not fundamental. |
| **should-not-exist** | Two free strengths hidden as “\(g_{\mathrm{tms}},g_{\mathrm{bs}}\)” under one name; free \(g(t)\) fitted pointwise to \(S(u)\). |
| **S⋆-only kill (F1)** | Scored effect is only larger peak \(S_\star\) with early range ~0.001888 → **DEAD**. |
| **Grade** | **SURVIVOR-SCHEMA · MISSING_INPUT** |

### R5-C2 — Shared greybody drive (one \(\Gamma_j\)-fixed channel drives both TMS and BS maps)

| field | content |
|---|---|
| **Idea** | Single channel weight vector \(c_j=\sqrt{\Gamma_j}\) (theory-fixed) multiplies **one** time-dependent coupling that feeds both entangling and dump blocks inseparably. |
| **Non-factor test** | Cannot retune dump without retuning entangle under the same \(c_j\) and same \(g(t)\). |
| **Why it might act** | Early overlap ratio locked by spectrum+one coupling; removes independent ratio thrash surface. |
| **can-exist** | Instrument already uses \(\sqrt{\Gamma_j}\) on both channels; locking them to one \(g\) is structural co-mod. |
| **should-not-exist** | Independent residual free \(G_{\mathrm{TMS}},G_{\mathrm{BS}}\) after “shared greybody”; densify of \(c_j\) as free midband list. |
| **densify kill** | Hand densify \(\Gamma_j\) table without derivation = DEAD. |
| **S⋆-only kill (F1)** | Shared drive that only inflates peak → DEAD. |
| **Grade** | **SURVIVOR-SCHEMA · MISSING_INPUT** |

### R5-C3 — Sonic-horizon co-generated flux+squeeze (analog single-source law)

| field | content |
|---|---|
| **Idea** | Finite sonic-horizon / healing-length microphysics supplies **one** source that co-generates Hawking-like flux (dump) and mode squeezing (entangle); schedule pins are effective projections, not free. |
| **Non-factor test** | Flux and squeeze are both functions of the **same** horizon/flow parameters (O(1) theory set). |
| **Why it might act** | Matches registered Page dynamical object (scaffold corpus: phonon flux off sonic-horizon core) better than factorized headers. |
| **can-exist** | Scaffold + week-N instruments already frame sonic-horizon unitary core; co-mod is the honest dynamical class. |
| **should-not-exist** | Cartoon toy Page shape \(4v(1-v)\) sold as co-mod law (scaffold is **NOT a result**). Free horizon params fitted to 0.10. |
| **S⋆-only kill (F1)** | Horizon story whose only scored move is \(S_\star\) up → DEAD. |
| **Grade** | **SURVIVOR-SCHEMA · MISSING_INPUT** (no closed co-mod derivation for T8) |

### R5-C4 — Smooth single-phase co-mod with continuity certificate (anti-D1-launder)

| field | content |
|---|---|
| **Idea** | Explicit smooth \(H(t)\) continuous in micro parameters that never degenerates into discontinuous pure-BS then TMS; written continuity certificate is part of the law text. |
| **Non-factor test** | No `PHASE_BS_ONLY_UNTIL_U` / soft `PHASE1_TMS_FRAC` thrash; no independent phase switch. |
| **Why it might act** | D1 discontinuity improved early T8 but burned T2; smooth co-mod is the honest alternative class. |
| **can-exist** | Exhausted D1 forbids **header** two-phase thrash, not all continuous co-generated dynamics. |
| **should-not-exist** | D1 two-phase rewritten as “one H” without smooth micro derivation (**D1-launder kill**). |
| **S⋆-only kill (F1)** | Continuity theater with only peak inflation → DEAD. |
| **Grade** | **SURVIVOR-SCHEMA · MISSING_INPUT** |

### Explicitly **not** candidates (factorization / thrash / densify / F1)

| dead form | why dead |
|---|---|
| Independent free \(G_{\mathrm{TMS}},G_{\mathrm{BS}}\) under “single law” label | Factorization kill — two knobs in a trenchcoat |
| Free \(g(f)\) with >O(1) params aimed at bin [0.10,0.11) | Fit kill / unfalsifiable |
| D1 two-phase discontinuity as “one H” | D1-launder kill |
| Header shape/start grids sold as co-mod | FORBIDDEN thrash |
| Mode densify as co-mod channel fill | Densify DEAD |
| Pure \(S_\star\) inflation | **F1 DEAD** |

---

## 4. can-exist (framework / instrument permission)

- Fail is an **overlap ratio** problem; factorization makes the ratio a free thrash surface.  
- Real microphysics often has one interaction generating both energy transfer and entanglement.  
- Breaks pure \(G_{\mathrm{TMS}}\) stickiness by correlating numerator and coordinate advance from the *same* operator.  
- Compatible with exploratory “laws as suggestions” when stocked factorized schedules are treated as effective, not fundamental.  
- Highest conceptual cleanliness among R1/R2/R5 **if** content appears.

---

## 5. should-not-exist (adversarial; includes S⋆-only)

- **Two knobs in a trenchcoat:** “single law” that still has independent free TMS and BS strengths.  
- **Phase discontinuity smuggle:** D1 two-phase rewritten as “one Hamiltonian” without smooth micro derivation.  
- **Unfalsifiable coupling function** \(g(f)\) fitted pointwise to \(S(u)\).  
- **Hides thrash:** free function with enough parameters to match any early slope.  
- **Densify thrash:** co-mod that is only denser mode tables — **DEAD**.  
- **S⋆-only lever (F1):** co-modulation whose net scored effect is **only** a larger peak \(S_\star\) (denominator) while early-bin range stays at ~0.001888. Ratio can fall ~13% with **zero** early microphysics of the fail window. **DEAD** as T8 pass under F1 — any future T8_pass must report early-bin range **and** \(S_\star\) vs v13.

---

## 6. joint-gate risk

| gate | risk |
|---|---|
| All joint | One wrong co-modulation can burn T2 and T8 together |
| Nulls | Coupled channel may spoil N2 thermal / N3 isolation |
| Provenance | Harder to pin schedule; must still write-once freeze pins after derivation |
| DC3 | Shared energy accounting can fake weight-borne reach if not audited |

---

## 7. kill table

| Kill | Trigger |
|---|---|
| Factorization kill | Independent free \(G_{\mathrm{TMS}},G_{\mathrm{BS}}\) remain after “law” |
| Fit kill | Free \(g(f)\) with >O(1) params aimed at bin [0.10,0.11) |
| D1-launder kill | Discontinuous pure-BS then TMS without micro continuity |
| Densify kill | Mode-count densify as co-mod |
| Joint kill | No write-once joint clear |
| **F1 / S⋆ kill** | Early range unchanged; only \(S_\star\) inflated |

---

## 8. Stocked vs MISSING_INPUT (this wave)

| Asset | Status |
|---|---|
| Factorized champion schedule pins | Stocked instrument |
| Non-factorizable single-coupling micro Hamiltonian | **MISSING_INPUT** |
| Continuity certificate / O(1) param law text | **MISSING_INPUT** |
| Write-once coevolve under co-mod law | **not started** |
| Coevolve production this package | **0** |
| Densify runs this package | **0** |

**Immediate grade:** **SURVIVOR-SCHEMA · MISSING_INPUT · no production**  
**Land this package:** **0**  
**CANDIDATE packet:** **0**  
**Conceptual note:** still the cleanest structural target among R1/R2/R5 **if** licensed content appears — cleanliness ≠ land.

---

## 9. Explicit non-claims

- Candidate classes ≠ Derived co-mod Hamiltonian.  
- “Highest conceptual cleanliness” ≠ deferred success without content.  
- No invented single-H claims T8 pass without instrument.  
- `page_curve_claimed` remains **false**.

---

*End CONSTRUCTION_R5.md. NO FABRICATIONS. Non-factorized only. F1 ON. Densify DEAD.*
