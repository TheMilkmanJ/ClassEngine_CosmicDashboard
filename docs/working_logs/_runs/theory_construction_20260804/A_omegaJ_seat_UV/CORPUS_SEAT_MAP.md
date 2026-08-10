# CORPUS_SEAT_MAP — File:line hunt of seat content for P2-1 / P2-2

**Package:** `docs/working_logs/_runs/theory_construction_20260804/A_omegaJ_seat_UV/`  
**Date:** 2026-08-04  
**Role:** inventory of **stocked** seat / tenth-channel / junction objects with paths and line anchors  
**Rule:** map only — **do not invent** χ, \(J_\mathrm{seat}\), \(\omega_J^\mathrm{micro}\), or free dials to 5.672 keV  
**Consumers:** [`P2_1_A_Jchi.md`](./P2_1_A_Jchi.md) · [`P2_2_A_omegaJ_direct.md`](./P2_2_A_omegaJ_direct.md) · [`NO_LAND_PROOF.md`](./NO_LAND_PROOF.md)

---

## 0. Hunt question

> For forward \(\omega_J\) under A_Jχ (pair) or A_ωJ-direct (formula), **what seat-sector content is actually written**, and **what is still blank**?

**Answer in one line:** Locus + UV mass operator + stage-8 formalization + dead trickle branch are stocked; **driven-junction** \((\chi, J_\mathrm{seat})\) / \(\omega_J^\mathrm{micro}\) are **unstated**.

---

## 1. Status legend

| Tag | Meaning |
|---|---|
| **LOCUS** | Decides *where* the junction lives — not a price |
| **STRUCTURE** | Formalization / algebra — not a micro number |
| **OPERATOR** | Explicit field content — may feed future matching |
| **COMPUTED** | Independent number usable as context |
| **BACK-SOLVED** | Hygiene / grading only — not forward land |
| **DEAD** | Class kill — do not reuse as \(\omega_J\) path |
| **FORBIDDEN** | ID declined for manufacture |
| **MISSING** | Named or required but not stocked |

---

## 2. Living baryogenesis surface

| Anchor | Path:lines (approx) | Content | Tag for #39 |
|---|---|---|---|
| Document grade + #39 open | `docs/PRTOE_baryogenesis.md` L6–12 | Forward ω_J OPEN-BLOCKED; pointer to omegaJ_forward | **MISSING** residual |
| Portal = tenth-channel seat | same L47–52 | Junction is tenth-channel seat term; census portal L-blind; trickle dead ×26 | **LOCUS** + **DEAD** trickle |
| Class B survivor | same L86–91 | Driven overdamped junction; seat coupling drives φ at θ̇ | **STRUCTURE** / class |
| Rectifier ⟨sin⟩ | same L93–105 | \(R=\omega_J^2/(2\Gamma_\varphi\dot\theta)\); \(p,j\) rates | **STRUCTURE** |
| Back-target 5.7 keV | same L112–115 | Transmission fixes ω_J≈5.7 keV as **demand** | **BACK-SOLVED** target |
| §3a closed vs missing | same L117–157 | Quartet back-solve 5.672 keV; need decay constant + pinning curvature; v_L declined; band [3,12]/kill <0.057 | **MISSING** pair · **FORBIDDEN** v_L · band **locked** |
| Claim table row 6 | same L236 | Forward ω_J OPEN-BLOCKED #39; do not invent A_ωJ micro | **MISSING** |

---

## 3. Transfer-integral stages (mechanism book)

| Anchor | Path:lines (approx) | Content | Tag |
|---|---|---|---|
| Portal candidates named | `docs/working_logs/the_transfer_integral_spec.md` L30–31 | Census / μ / tenth-channel seat (UV form spec’d) as fork | **LOCUS** candidates |
| Fork #1 DECIDED | same L79–81, L108–112 | Junction = **tenth-channel seat term**; μ = low-energy face; UV form above \(v_L\) | **LOCUS** |
| Seat-trickle death | same L173–188 | Low-energy seat alone cannot transfer; η~3×10⁻³⁶ | **DEAD** |
| UV coherent vertex | same L190–209 | Dim-5 \((c_A/v_L)\Phi_\mathrm{med}\sigma_L\bar\nu_1^c\nu_1\); coherent vs thermal squeeze; MeV vs TeV corner | **OPERATOR** (trickle/coherent branch — **not** priced as \(U_J\) curvature) |
| Stage 7 class B + named J | same L280–302 | Kapitza survivor; “recorded seat coupling J” for averaging — F owed | **STRUCTURE** · J **MISSING** number |
| Stage 8 formalization | same L310–315 | \(U_\mathrm{pin}=-\chi m_1^2\cos\varphi\); \(U_J=-\chi\omega_J^2\cos(\varphi-\dot\theta t)\); χ cancels | **STRUCTURE** |
| Stage 8 pin = off-switch | same L333–351 | \(R\) carries no \(m_1\); pin hierarchy | **DEAD** as prefactor (C3/C10) |
| Stage 8 re-point to ω_J | same L356–369 | Consumers ride seat \(\omega_J\approx 5.68\,\mathrm{keV}\) **iff** seat supplies it; formalization boundary explicit | **BACK-SOLVED** demand · **STRUCTURE** honesty |

---

## 4. Neutrino / tenth-channel operator book

| Anchor | Path:lines (approx) | Content | Tag |
|---|---|---|---|
| Mass = DE scale | `docs/PRTOE_neutrino_sector.md` L21, L138 | \(m_1=\kappa_m\cdot\rho_\mathrm{inf}^{1/4}\), \(\kappa_m\approx 1\); 2.25 meV un-derived as value problem | **OPERATOR** IR mass face — **not** \(\omega_J\) |
| UV operator O_A | same L144–150 | \(O_A=(c_A/v_L)\Phi_\mathrm{med}\sigma_L\bar\nu_1^c\nu_1+\mathrm{h.c.}\); below \(v_L\) → Majorana; \(g=m_1/v_L\) | **OPERATOR** exhibited |
| Open flavor / μ | same L15, L37, L142, L172 | Exact μ, flavor distribution, ρ_inf closure OPEN | Orthogonal residual |
| MATH_SPINE tie + seat | `docs/PRTOE_MATH_SPINE.md` L331–344 | Tie’s operator exhibited (tenth-channel seat, UV above \(v_L\)); seat constant **b** gated | **OPERATOR** · b **MISSING** (mass face) |
| DEPENDENCY_TREE | `docs/PRTOE_DEPENDENCY_TREE.md` L95 | Tenth channel candidate; operator exhibited; b gated; seat-alignment owed | **OPERATOR** status |
| Docket #65 / #71 | `docs/working_logs/_DOCKET_INDEX.md` (~L113, L119) | Tenth-channel operator closed at seat level; UV form above \(v_L\) closed | **OPERATOR** closed ≠ \(\omega_J\) closed |
| Seat-alignment #116 | same (~L164) | Flavor-resolved Φ_med(T) gated on basement | **MISSING** dynamics (mass alignment, not \(\omega_J\)) |
| Audit #65 | `docs/working_logs/_AUDIT_LEDGER.md` (~L2779) | Operator exhibited; b + seat-alignment still OWED | Same |
| DERIVATION_HUNT | `docs/PRTOE_DERIVATION_HUNT.md` L475, L711–712 | Tenth-channel seat term operator + UV form; floor sets \(m_1\) | **OPERATOR** mass consumer |

---

## 5. Residual isolation / formulability debts

| Anchor | Path:lines (approx) | Content | Tag |
|---|---|---|---|
| Session #39 | `docs/working_logs/PRTOE_session_2026-07-29b_findings.md` L290–294 | Forward needs decay constant **and** pinning curvature; both unstated; **v_L declined** | **MISSING** · **FORBIDDEN** |
| Formulability REPORT | `docs/working_logs/_runs/debt_omegaJ_forward_formulability_20260803/REPORT.md` full | 0 formulable non-circular lands; C1 only real form; A_ωJ named | **MISSING** |
| C1 / C1χ / C1J | same ~L86–88 | \(\omega_J^2=J_\mathrm{seat}/\chi\); χ unstated; J named without number | **MISSING** ×2 |
| Forbidden IDs | same ~L92–96 | v_L (C5); f→χ (C9) | **FORBIDDEN** |
| Wrong objects | same ~L89–91, L97 | Jeans; m₁; U_pin as U_J | **DEAD** |
| Science debts D3 | `docs/working_logs/SCIENCE_DEBTS_2026-08-03.md` (~L76, L203) | Forward ω_J from seat χ + pinning curvature | **MISSING** |

---

## 6. Theory-construction stack (2026-08-04)

| Package / file | Role | Tag |
|---|---|---|
| `omegaJ_forward/REQUIRED_INPUTS.md` | Packages A/B; I1–I7; construction checklist | Spec |
| `omegaJ_forward/CANDIDATE_ROSTER.md` | C0–C11 grades; seat locus MISSING_INPUT | Roster |
| `omegaJ_forward/KILL_AND_BANDS.md` | Pre-locked band | Band |
| `A_omegaJ_rule1/AXIOM.md` | A_ωJ CANDIDATE form + independence | Structure premise |
| `A_omegaJ_rule1/DERIVATION_ATTEMPT.md` | Underdetermined; free ratio | Proof of underdetermination |
| `A_omegaJ_exploratory_needs/*` | P2-1…P2-6; survivors P2-1/P2-2 only | Second-premise registry |
| **This package** | Deeper seat UV map; still no land | Schema deepening |

---

## 7. Scripts / machine-backed numbers (context only)

| Script | What it supplies | Forward \(\omega_J\)? |
|---|---|---|
| `scripts/kapitza_junction_response.py` | 0.06% verification of rectifier formula | **No** — structure |
| `scripts/junction_quartet_closure.py` | Quartet closes at BACK-SOLVED 5.672 keV | **No** — hygiene |
| `scripts/baryogenesis_junction_closure.py` | Same chain; Γ_φ/θ̇ = 9.0319×10⁷ COMPUTED | **No** |
| `scripts/diode_mechanism_pricing.py` | Class A/B/C pricing (trickle dead; static dead) | Class only |

---

## 8. What the map finds for each micro leg

### 8.1 χ (junction-phase stiffness / decay constant of φ)

| Candidate source in corpus | Verdict |
|---|---|
| Stage-8 formalization | Named; **cancels**; **no number** |
| \(v_L\) (MeV / GeV / 2.4 TeV) | **FORBIDDEN ID** (#39) |
| Electron-scalar \(f\sim 100\)–\(500\,\mathrm{TeV}\) | **FORBIDDEN** without new named map |
| Thermal / bath response under shared-χ | **INERT** for \(\omega_J\) (P2-4) |
| Seat modulus \(f_\varphi\) distinct | **Not stocked** (P2-6 fragile only) |

**Map result:** \(\chi\) = **MISSING** as independent micro price.

### 8.2 \(J_\mathrm{seat}\) (pinning curvature of **driven** \(U_J\))

| Candidate source in corpus | Verdict |
|---|---|
| Stage-7 “seat coupling J” | **Name only** — no independent number |
| \(O_A\) / coherent \(I_0\) at T_sph | Prices **trickle/coherent rate** branch — **DEAD** as η carrier; **no map** to \(U_J\) curvature |
| \(U_\mathrm{pin}\propto m_1^2\) | **WRONG OBJECT** (prices \(p\)) |
| Free dial to make \(\omega_J=5.672\,\mathrm{keV}\) | **Honesty kill** |

**Map result:** \(J_\mathrm{seat}\) for **driven** cos = **MISSING**.

### 8.3 \(\omega_J^\mathrm{micro}\) direct

| Candidate source in corpus | Verdict |
|---|---|
| Quartet residual | **BACK-SOLVED** (C0) — not micro |
| Proximity scales | **DEAD** as land (C6/C7) |
| Jeans \(\sqrt{4\pi G\rho}\) | **WRONG OBJECT** (C2) |
| Seat operator closed form | **Not written** |

**Map result:** direct formula = **MISSING**.

---

## 9. Objects that look like seat UV but do **not** pay #39

| Object | Why it does not close forward \(\omega_J\) |
|---|---|
| Exhibited \(O_A\) + UV form “closed” on docket | Closes **mass/μ / Majoron** consumers, not driven-junction plasma frequency |
| Seat constant **b** / \(\kappa_m\) | Multiplies \(\rho_\mathrm{inf}^{1/4}\to m_1\); wrong consumer (pin scale) |
| Seat-alignment dynamics | Flavor settling of mass matrix; not \(U_J\) curvature |
| Coherent vertex window computation (stage 4–5 era) | Historical trickle branch; class dead as magnitude carrier |
| Quartet arithmetic | Consistency of three legs + residual; residual still back-solved |

---

## 10. Compression for P2-1 / P2-2 authors

**What you may cite as stocked seat UV inputs:**

1. Portal locus = tenth-channel seat term (stage 2).  
2. Operator \(O_A\) and multi-face UV/IR language (neutrino sector).  
3. Stage-8 definition of \(\omega_J\) via \(U_J\) and \(\omega_J^2=J_\mathrm{seat}/\chi\).  
4. Independence fences (no \(v_L\), no \(f\to\chi\), no \(\eta\)).  
5. COMPUTED \(\Gamma_\varphi\), \(\dot\theta\), \(T_\mathrm{sph}\) as evaluation context.

**What you may not invent or smuggle:**

1. Numeric \(\chi\), \(J_\mathrm{seat}\), or \(\omega_J^\mathrm{micro}\).  
2. Free coupling aimed at **5.672 keV**.  
3. Circular \(R_\mathrm{need}\).  
4. Silent declined IDs.  
5. Pin / Jeans / proximity as micro.

**Gap sentence:**  
*The corpus seats the junction and exhibits a tenth-channel operator; it does not stock a matching law from that operator to the driven-junction pair \((\chi,J_\mathrm{seat})\) or to \(\omega_J^\mathrm{micro}\).*

---

*End CORPUS_SEAT_MAP.md*
