# D3 / H2 — Forward ω_J formulability from existing corpus objects only

**Date:** 2026-08-03  
**Question:** Is a **non-circular** forward expression for junction ω_J (or for the pair χ and pinning curvature) formulable from objects already in the corpus?  
**Rules held:** no invented v_L identifications; no fake close; no restatement of the 1.9 keV artifact target  
**Pre-registered grading band (before any forward derivation):** accept **[3, 12] keV**; kill **&lt; 0.057 keV**; anomalous-review (0.057, 3) ∪ (12, 30] keV  

**Answer in one line:** **No.** Quartet arithmetic is consistent; the rectifier formula is derived; the micro pair (χ, seat pinning curvature) that would price ω_J forward is **not stated** anywhere as independent inputs. Nothing formulable remains without a new axiom.

---

## 1. Sources surveyed

| Source | What it settles for this question |
|---|---|
| [`docs/PRTOE_baryogenesis.md`](../../../PRTOE_baryogenesis.md) §3–§3a (esp. L114–154) | Canonical: 5.7 keV is **back-target**; missing **decay constant + pinning curvature**; v_L ID declined; band [3,12] / kill &lt;0.057 |
| [`docs/working_logs/the_transfer_integral_spec.md`](../../the_transfer_integral_spec.md) stages 6–8 (esp. L290–365) | Rectifier R = ω_J²/(2Γ_φθ̇); χ cancels in EOM; formalization boundary explicit |
| [`docs/working_logs/PRTOE_session_2026-07-29b_findings.md`](../../PRTOE_session_2026-07-29b_findings.md) #39 (L290–294) | Isolates debt: need decay constant *and* pinning curvature; both unstated; v_L declined |
| [`docs/working_logs/_AUDIT_LEDGER.md`](../../_AUDIT_LEDGER.md) 2026-07-28 #39 (L4473–4510; later quartet-closes entry) | Naming collision (Jeans vs junction); ×9 was OOM shorthand; target confirmed 5.7 after sourced ratio |
| [`docs/working_logs/_runs/debt_baryo_omegaJ_20260803/REPORT.md`](../debt_baryo_omegaJ_20260803/REPORT.md) | Quartet closes at Γ_φ/θ̇ = 9.03×10⁷; candidate roster C0–C8; NI-D3-1 open |
| [`docs/working_logs/_runs/debt_baryo_d3_provenance_20260803/REPORT.md`](../debt_baryo_d3_provenance_20260803/REPORT.md) | Provenance: 5.672 keV is quartet-circular back-solve |
| [`scripts/kapitza_junction_response.py`](../../../../scripts/kapitza_junction_response.py) | Numeric 0.06% verification of R formula; back-solves ω_J from NEED |
| [`scripts/junction_quartet_closure.py`](../../../../scripts/junction_quartet_closure.py) / [`baryogenesis_junction_closure.py`](../../../../scripts/baryogenesis_junction_closure.py) | Sourced ratio closes; provenance types; band printout |
| [`docs/working_logs/SCIENCE_DEBTS_2026-08-03.md`](../../SCIENCE_DEBTS_2026-08-03.md) D3 | Residual named: seat χ + pinning curvature |
| ForGrok H2 | Exact formulability question this report answers |

---

## 2. Formal structure (what “forward” would mean)

Stage 8 / baryogenesis §3a write the overdamped formalization:

```
χ Γ_φ · φ̇ = −U′(φ)
U_pin = −χ m₁² cos φ
U_J   = −χ ω_J² cos(φ − θ̇ t)
```

χ **cancels**, leaving rates only:

```
φ̇ = −p sin φ − j sin(φ − θ̇ t)
p ≡ m₁² / Γ_φ ,   j ≡ ω_J² / Γ_φ
```

Fast-drive limit (physical: p/θ̇ ~ 10⁻¹⁷):

```
R = ω_J² / (2 Γ_φ θ̇)     (= j / (2 θ̇))
```

**Forward land** means evaluating ω_J (or j) from seat microphysics **without** feeding R_need (η) back in. Algebraically that is one of:

```
ω_J² = (curvature of U_J at the cos extremum) / χ     ≡   J_seat / χ
```

or an equivalent micro definition of the junction plasma frequency of the seat term at T_sph.

**What is already independently priced (not the open residual):**

| Object | Status | Provenance |
|---|---|---|
| Γ_φ = G_F² T_sph⁵ | COMPUTED | baryogenesis §3a L121–122; ~5.3902×10⁹ eV |
| θ̇ at T_sph | COMPUTED | winding bookkeeping; ~59.68 eV |
| m₁ ≈ 2.25 meV | RECORDED | Majorana insertion; pins *p*, not ω_J (stage 8) |
| R_need ~ 5×10⁻⁵ | FROM η·n band | **cannot** enter a non-circular forward price of ω_J |

**What cancels or drops out of R:** χ (by construction); m₁ (seventeen orders into the fast-drive limit).

---

## 3. Candidate objects — formulable / circular / missing input

Legend:
- **FORMULABLE** = closed expression from existing independent corpus numbers, yielding junction ω_J without η.
- **CIRCULAR** = expression that secretly re-imports R_need / η / j-as-back-solved.
- **MISSING INPUT** = form written, required micro inputs absent or unstated.
- **WRONG OBJECT** = formulable quantity that is not the junction plasma frequency.
- **FORBIDDEN ID** = would require an identification the corpus deliberately declined.

| ID | Expression / object | File:line provenance | Classification | Notes |
|---|---|---|---|---|
| **C0** | ω_J = √(2 R_need Γ_φ θ̇) ≈ **5.672 keV** | `PRTOE_baryogenesis.md:123–131`; `junction_quartet_closure.py`; `baryogenesis_junction_closure.py:34` | **CIRCULAR** | Quartet-consistent back-solve. Grades the target; is not a land. |
| **C0b** | j = 2 R_need θ̇ → ω_J = √(j Γ_φ) | same algebra as C0 | **CIRCULAR** | j is not independent once R is fixed; ω_J cancels from R = j/(2θ̇). |
| **C1** | ω_J² = (seat pinning curvature) / χ   or   ω_J² = J_seat / χ | `PRTOE_baryogenesis.md:140–143`; transfer spec `the_transfer_integral_spec.md:311–315`; session #39 L292–294 | **MISSING INPUT** (×2) | **The only real forward form.** Corpus states **neither** χ (junction-phase decay constant / stiffness) **nor** independent J_seat (cos-term curvature of U_J). |
| **C1χ** | χ alone as “decay constant of the visible junction phase” | named only inside U_J formalization; no numeric χ | **MISSING INPUT** | χ cancels from EOM; never priced elsewhere as this phase’s stiffness. Not the electron-scalar f (~100–500 TeV) without a new ID. |
| **C1J** | “recorded seat coupling J” (stage 7 wording) | `the_transfer_integral_spec.md:299`; kapitza header L19–24 | **MISSING INPUT** | Stage 7 *names* J; stage 8 **never supplies a number** independent of ω_J. Later text re-points consumers to ω_J itself. |
| **C2** | Jeans ω_J = √(4πGρ) = √(3/2) H | `PRTOE_sqrt3_derivation.md:51–54`; coincidence / prereg docs; audit L4479–4486 | **WRONG OBJECT** | Fully formulable, unrelated. ~3×10⁻⁵ eV at T_sph → **far below kill**. Naming collision only. |
| **C3** | R ~ (m₁/θ̇)·F with F = O(1) | transfer spec stage 7 L294–302; stage 8 kill of this form L353–358 | **CIRCULAR / KILLED** | Stage 8: overdamped pinning is m₁²/Γ_φ; R carries **no m₁**. Coincidence 0.75 was not mechanism. |
| **C4** | ω_J ∼ m₁ = 2.25 meV | neutrino / transfer books | **WRONG SCALE** (not formulable as junction ω_J) | ~2.5×10⁶ under target; kills if adopted. |
| **C5** | Identify junction decay constant with **v_L** (MeV / GeV / 2.4 TeV), invent χ | neutrino-sector v_L corners; session #39 L293–294; baryogenesis §3a L143–144 | **FORBIDDEN ID** | Explicitly declined. Manufacturing a derivation. **Not used.** |
| **C6** | √(m₁ Γ_φ) ≈ 3.5 keV | desk-only (prior debt report) | **MISSING AXIOM** | Numerically near band by chance; no mechanism chain in corpus. |
| **C7** | Identify ω_J with T_on ≈ 9.4 keV (amplitude freeze) | transfer-integral timing wall | **MISSING ID** | Proximity only (×1.7); no identity claimed. |
| **C8** | √(θ̇ Γ_φ) then ×√(2R) | pure algebra of C0 | **CIRCULAR** | Tautology of the back-solve. |
| **C9** | Electron-coupled scalar decay constant f ~ 100–500 TeV as χ | `PRTOE_READERS_GUIDE.md` f row; direct/indirect detection | **FORBIDDEN / WRONG OBJECT** without new axiom | Different sector and scale; no corpus map f → junction-phase χ. |
| **C10** | Pinning curvature of **U_pin** = χ m₁² (Majorana) | transfer spec L311; kapitza L23–28 | **WRONG OBJECT for ω_J** | Prices *p*, not *j*. Stage 8: this is the rectifier’s **off switch**, not its prefactor. |
| **C11** | 1.90 keV from rounded Γ_φ/θ̇ ~ 10⁷ | audit L4506–4509; `baryogenesis_junction_closure.py` artifact path | **CIRCULAR + ARTIFACT** | Holding stale ratio manufactures ×9 miss. **Not a target.** |

### Summary counts

| Class | Count | IDs |
|---|---|---|
| CIRCULAR (η / R_need / tautology / artifact) | 5 | C0, C0b, C3, C8, C11 |
| MISSING INPUT / MISSING AXIOM | 5 | C1, C1χ, C1J, C6, C7 |
| WRONG OBJECT / WRONG SCALE | 3 | C2, C4, C10 |
| FORBIDDEN ID (v_L or f→χ) | 2 | C5, C9 |
| **FORMULABLE non-circular junction ω_J** | **0** | — |

---

## 4. Is χ itself formulable without circular IDs?

**No.**

1. In the stage-8 formalization, χ is an overall stiffness that multiplies *both* U_pin and U_J and **cancels** from φ̇. The EOM never constrains χ.
2. No independent numeric for “junction-phase decay constant” appears in baryogenesis, transfer-integral stages 6–8, session #39, or the junction scripts.
3. Candidate re-uses of the word “decay constant” elsewhere (electron-coupled scalar f; Goldstone F_dark; majoron/v_L corners) are **different objects**. Mapping any of them onto χ is a new identification — exactly the class #39 declined for v_L.
4. Even if χ were magically known, **J_seat / pinning curvature of U_J is still unstated**, so ω_J² = J_seat/χ remains underdetermined.

Therefore H2 (“is #39 seat χ even formulable without circular IDs?”) answers: **χ is not formulable from the corpus; the pair (χ, curvature) is the missing micro input, not a hidden closed form.**

---

## 5. Quartet status (context only — not a forward land)

With **computed** Γ_φ/θ̇ = 9.0319×10⁷ (not ~10⁷ shorthand):

| member | value | type |
|---|---|---|
| Γ_φ | 5.3902×10⁹ eV | COMPUTED |
| θ̇ | 59.68 eV | COMPUTED |
| R needed | ~5×10⁻⁵ | FROM η band |
| ω_J | **5.672 keV** | BACK-SOLVED |
| j | 6.03 meV | FOLLOWS ω_J |

Quartet is **internally consistent**. That consistency does **not** make ω_J forward-formulable; it only confirms that three independent legs force one residual scale.

---

## 6. Single missing axiom (clean statement)

> **Missing axiom A_ωJ:** At T_sph, the seat–visible junction supplies an independent microscopic price of  
> **either** the junction plasma frequency ω_J  
> **or** the pair (χ, J_seat) with U_J = −χ ω_J² cos(φ − θ̇t) and ω_J² ≡ J_seat/χ,  
> **without** reference to η, R_need, or v_L (or any other unstated identification).

Until A_ωJ is written and sourced from seat microphysics already in the model (or a new but **explicit** seat axiom), **no non-circular forward expression for ω_J exists in the corpus.**

Equivalently (operational form of the same gap):

> The corpus defines ω_J only as the free parameter of the seat junction formalization that R later back-solves. It never defines the seat coupling energy density / curvature that would *compute* that parameter.

This is **one** missing axiom (one micro price), not a pile of independent gaps: χ and J_seat are a single underdetermined ratio for the purpose of ω_J; either both are supplied, or ω_J is supplied directly.

---

## 7. Pre-registered band (unchanged; grading only)

From `PRTOE_baryogenesis.md` §3a L148–154 and `baryogenesis_junction_closure.py` L76–78:

| Disposition | Derived ω_J | Meaning |
|---|---|---|
| **ACCEPT** | **[3.0, 12.0] keV** | junction magnitude reading lives (within ~×2 of 5.7) |
| **ANOMALOUS-REVIEW** | (0.057, 3.0) ∪ (12, 30] keV | retune j/ratio before booking; not auto-kill |
| **KILL junction route** | **&lt; 0.057 keV** | ×100 under ~5.7; pre-committed |
| **Forbidden target** | 1.90 keV under stale Γ/θ̇=10⁷ | artifact basin; do not grade against |

Band does **not** create formulability; it only scores a future land if A_ωJ is ever supplied.

---

## 8. Explicit non-claims

- This report does **not** derive ω_J.
- This report does **not** invent v_L → decay-constant or f → χ maps.
- This report does **not** adopt 1.9 keV or reopen the dissolved ×9.
- Quartet consistency is **not** a forward land.
- Residual remains **OPEN-THEORY / BLOCKED-ON-AXIOM** until A_ωJ lands or the junction class is killed by a derived value &lt; 0.057 keV (or by failure of overdamped premises).

---

## 9. Relation to prior D3 artifacts

| Prior run | Role relative to this report |
|---|---|
| `debt_baryo_omegaJ_20260803` | Established quartet close + candidate desk numerics; left NI-D3-1 open |
| `debt_baryo_d3_provenance_20260803` | Provenance / band registration |
| **This run** | Answers H2 / formulability: **zero** non-circular formulable expressions; names **A_ωJ** as the single missing axiom |

**NEXT (unchanged blocking issue):** supply A_ωJ from seat sector microphysics, or prove the sector cannot — then kill the junction magnitude route under the pre-registered band.

---

*End REPORT — debt_omegaJ_forward_formulability_20260803*
