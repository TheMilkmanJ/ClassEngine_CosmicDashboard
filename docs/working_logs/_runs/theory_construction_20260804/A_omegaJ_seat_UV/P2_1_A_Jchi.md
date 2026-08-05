# P2-1 — A_Jχ (UV/IR pair price of tenth-channel seat)

**Package:** `docs/working_logs/_runs/theory_construction_20260804/A_omegaJ_seat_UV/`  
**Date:** 2026-08-04  
**Role:** deeper **SURVIVOR-SCHEMA** write-up only — seat UV/IR matching content for the pair \((\chi, J_\mathrm{seat})\)  
**Prior:** [`../A_omegaJ_exploratory_needs/CANDIDATE_SECOND_PREMISES.md`](../A_omegaJ_exploratory_needs/CANDIDATE_SECOND_PREMISES.md) (P2-1) · [`../A_omegaJ_rule1/AXIOM.md`](../A_omegaJ_rule1/AXIOM.md) · [`../omegaJ_forward/REQUIRED_INPUTS.md`](../omegaJ_forward/REQUIRED_INPUTS.md)  
**Grade of this premise:** **CANDIDATE schema** · **MISSING_INPUT** · **not Derived** · **no land**  
**Band (locked before any land):** ACCEPT **[3, 12] keV** · ANOMALOUS-REVIEW \((0.057,3)\cup(12,30]\) · KILL **< 0.057 keV**

---

## 0. Verdict in one line

**A_Jχ remains the only classical pair-price schema that could close #39; corpus exhibits a tenth-channel operator and UV face, but stocks zero independent coefficients that evaluate both \(\chi\) and \(J_\mathrm{seat}\) without free dials — no non-circular \(\omega_J\), no band score.**

---

## 1. Precise statement (CANDIDATE second premise)

> **A_Jχ.** At the sphaleron temperature \(T_\mathrm{sph}\), UV/IR matching of the **tenth-channel seat operator** already selected as the L-carrying junction portal supplies **both**
> \[
> \chi = \chi_\mathrm{micro}(\text{seat operators}, T_\mathrm{sph}),
> \qquad
> J_\mathrm{seat} = J_\mathrm{micro}(\text{seat operators}, T_\mathrm{sph})
> \]
> from Wilson / VEV / matching content of that operator sector, **with no free dial** and **no reference to \(\eta\) or \(R_\mathrm{need}\)**. Then
> \[
> \omega_J \;=\; \sqrt{\frac{J_\mathrm{micro}}{\chi_\mathrm{micro}}}.
> \]

This is hand-off **S1** from `A_omegaJ_rule1` restated as an explicit **second** Rule-1 premise under A_ωJ’s form \(\omega_J^2\equiv J_\mathrm{seat}/\chi\).

**Load-bearing object of the pair:** the **driven** cos term of the stage-8 formalization

\[
U_J = -\chi\,\omega_J^2\cos(\varphi-\dot\theta t),
\]

**not** the static Majorana pin \(U_\mathrm{pin}=-\chi m_1^2\cos\varphi\) (which prices \(p\), not \(j\)).

---

## 2. What A_Jχ would have to deliver (checklist)

A land under A_Jχ requires **all** of:

| # | Delivery | Status in corpus today |
|---|---|---|
| 1 | Explicit operator content of the seat–visible **driven** junction (not only L-carriage for portal selection) | **Partial:** O_A exhibited for mass/μ face; **driven-junction map unwritten** |
| 2 | IR matching definition of phase stiffness \(\chi\) of the *visible* phase \(\varphi\) | **Missing** — χ named only inside formalization; cancels |
| 3 | IR matching definition of seat coupling energy-density scale \(J_\mathrm{seat}\) of the cos\((\varphi-\dot\theta t)\) term | **Missing** — stage 7 names “J”; stage 8 never independent number |
| 4 | Evaluation at \(T_\mathrm{sph}\) with recorded bath/drive inputs only as *context*, not as \(\omega_J\) formula | \(\Gamma_\varphi\), \(\dot\theta\) **COMPUTED**; unused for micro pair |
| 5 | Independence I1–I7 (no \(\eta\), no \(R_\mathrm{need}\), no \(v_L\)/silent \(f\to\chi\), no pin-as-drive, no proximity) | **Not yet testable** — no expression |
| 6 | Single numeric \(\omega_J=\sqrt{J/\chi}\) scored only on locked band | **No number** |

Until 1–5 close, A_Jχ is a **schema for a future matching computation**, not a land.

---

## 3. can-exist (why the framework permits the schema)

1. **Portal already DECIDED.** Transfer stage 2 selects the tenth-channel seat term as the only L-carrying junction portal; μ is that term’s low-energy face. A_Jχ does not re-pick the portal — it asks the *same* sector for a *price*.

2. **Operator exhibited.** Neutrino-sector UV form
   \[
   O_A = \frac{c_A}{v_L}\,\Phi_\mathrm{med}\,\sigma_L\,\bar\nu_1^c\nu_1 + \mathrm{h.c.}
   \]
   is on books. Multi-face (UV above \(v_L\), IR Majorana) is native. Matching language is therefore not alien.

3. **Formalization already uses pair language.** Stage 8 writes \(U_J=-\chi\omega_J^2\cos(\ldots)\) with \(\omega_J^2=J_\mathrm{seat}/\chi\). A_Jχ asserts those two symbols are micro-priced outputs, not free parameters.

4. **Independence is the honest reading of “micro.”** Operator strength at \(T_\mathrm{sph}\) is a property of the sector and the bath, not of observed \(\eta\). The independence clause of A_ωJ is exactly what A_Jχ must enforce in the matching inputs.

5. **Residual dimension is correct.** After A_ωJ, one free ratio remains. Supplying both legs (or their ratio) is the minimal classical close of #39.

---

## 4. should-not-exist (adversarial kill case)

### Charge A — empty pair rename

Writing “UV matching supplies both \(\chi\) and \(J_\mathrm{seat}\)” without writing **any** Wilson coefficient, VEV path, or matching rule is A_ωJ’s free-parameter rename **split into two symbols**. Registry of A_Jχ without content is schema theater.

### Charge B — steerability to 5.672 keV

Later writers can choose \(c_A\), \(\langle\Phi\rangle\), or an unstated matching prefactor so that \(\sqrt{J/\chi}\) hits the back-solve center and then cite “micro.” Pre-registered bands block *open* retargeting; they do **not** block *steered UV*. Without an external/lattice handle that **cannot see \(\eta\)**, independence is prose.

### Charge C — locus ≠ keV scale

The seat term was selected for **lepton-number carriage**, not for a keV plasma frequency. Natural IR mass on books is \(m_1\sim\mathrm{meV}\); high-scale faces sit TeV-class. Intermediate keV may be \(\eta\)’s demand rather than the sector’s nature (K5 prior).

### Charge D — wrong face / wrong consumer

Corpus UV content prices:

- lightest Majorana mass / μ face,  
- seat-trickle / coherent vertex rates (historically **dead** as η carrier),  
- Majoron coupling \(g=m_1/v_L\),

**none** of which is the curvature of \(U_J\)’s **driven** cos term. Reusing O_A’s mass face as \(J_\mathrm{seat}\) is **I6 / C10** collapse (pin-as-drive). Reusing \(v_L\) as \(\chi\) is **I3**. Reusing electron-scalar \(f\) is **I4**.

### Charge E — shared-χ cancellation

Even a perfect absolute \(\chi\) **cancels** from \(R\). A_Jχ only works if \(J_\mathrm{seat}\) is **not** forced proportional to the same free dial that sets \(\chi\) in a way that re-imports \(\eta\). Pair-price without a *ratio law* still leaves one free scale.

**Adversary verdict:** A_Jχ should not be treated as progress toward a land until matching content that cannot be aimed at 5.672 keV is written. Prefer **K5** over perpetual empty pair.

---

## 5. Corpus seat content usable for A_Jχ (and what it does *not* do)

Full file:line inventory: [`CORPUS_SEAT_MAP.md`](./CORPUS_SEAT_MAP.md). Headline:

| Stocked seat object | Usable for A_Jχ? | Why |
|---|---|---|
| Tenth-channel portal decision | **Locus only** | Decides *where*, not *how much* |
| \(O_A\) UV form | **Input candidate** | No closed map \(O_A\to(\chi,J_\mathrm{seat})\) for **driven** \(U_J\) |
| μ / \(m_1\approx 2.25\,\mathrm{meV}\) | **No** as \(J_\mathrm{seat}\) | Prices \(U_\mathrm{pin}\) / \(p\) (I6) |
| Seat-trickle \(I_0\) / Γ_ΔL path | **No** | Class **DEAD** (~26 orders); wrong carrier |
| \(v_L\) corners | **Forbidden** as χ (I3) unless new named axiom |
| Stage-8 \(U_J\) form | **Structure** | Names pair; supplies neither number |
| \(\Gamma_\varphi\), \(\dot\theta\) | Context only | Do not price ratio |

**Net:** stocked UV/IR content **does not evaluate** A_Jχ. See [`NO_LAND_PROOF.md`](./NO_LAND_PROOF.md).

---

## 6. Matching sketch (honest empty template — not a derivation)

If a future matching package is written, it must fill **symbols**, not targets:

```
Inputs  (η-blind):   { seat operators O_A, … ; VEVs / ⟨Φ_med⟩(T_sph);
                       EW/lepton matching for φ-normalization;
                       T_sph as evaluation point only }
Outputs:             χ_micro , J_micro   (or their ratio alone)
Forbidden inputs:    η, R_need, j*, ω_J*, 5.672 keV, v_L-as-χ, f→χ silent
Then:                ω_J = sqrt(J_micro / χ_micro)
Score:               only against locked [3,12] / kill <0.057
```

**This package does not invent** Wilson numbers, \(\langle\Phi\rangle\), or a free \(c_A\) to hit the band.

---

## 7. Kill conditions (when A_Jχ dies)

| Kill | Trigger |
|---|---|
| Honesty / Charge B | Any free coupling dialed so \(\omega_J\to 5.672\,\mathrm{keV}\) |
| I1 | \(R_\mathrm{need}/\eta\) enters matching inputs |
| I3–I4 | Silent \(\chi=v_L\) or \(\chi=f_{e\text{-scalar}}\) inside “matching” |
| I6 | \(J_\mathrm{seat}\) taken as \(U_\mathrm{pin}\) curvature \(\propto m_1^2\) |
| I7 | Pair built from \(\sqrt{m_1\Gamma_\varphi}\), \(T_\mathrm{on}\), etc. without chain |
| Emptiness | Premise never writes actual matching rules (Charge A permanent) |
| K5 class | Proof seat UV cannot produce keV \(\omega_J\) without manufacturing IDs |
| K1 | Honest micro land \(<0.057\,\mathrm{keV}\) |

---

## 8. Band score

| Item | Value |
|---|---|
| Forward \(\omega_J\) under A_Jχ this package | **None** |
| **Band score** | **no score — no land** |
| BACK-SOLVED center (hygiene only) | \(5.672\,\mathrm{keV}\) — **not** A_Jχ output |

---

## 9. Explicit non-claims

1. A_Jχ is **not** Derived / PAID.  
2. No free constant invented to hit **5.672 keV**.  
3. No circular \(R_\mathrm{need}/\eta\).  
4. No silent \(v_L\) or \(f\to\chi\).  
5. No reuse of pin curvature or seat-trickle rate as \(J_\mathrm{seat}\).  
6. No MCMC / PolyChord / H₀ / ownership tasks.  
7. No upgrade of AD-direct document COMPLETE-CONDITIONAL grade.

---

## 10. Disposition

| Field | Value |
|---|---|
| Grade | **SURVIVOR-SCHEMA / CANDIDATE** |
| Content fill | **MISSING_INPUT** (pair not evaluated) |
| Land | **No** |
| Relation to P2-2 | Equivalent residual dimension; pair form of the same one free scale |
| Next honest step | Real matching content **or** K5 proof — see [`NEXT_AXIOM_CANDIDATES.md`](./NEXT_AXIOM_CANDIDATES.md) |

---

*End P2_1_A_Jchi.md*
