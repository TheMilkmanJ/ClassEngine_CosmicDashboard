# P2-2 — A_ωJ-direct (single micro frequency from seat operators)

**Package:** `docs/working_logs/_runs/theory_construction_20260804/A_omegaJ_seat_UV/`  
**Date:** 2026-08-04  
**Role:** deeper **SURVIVOR-SCHEMA** write-up only — direct micro formula for \(\omega_J\)  
**Prior:** [`../A_omegaJ_exploratory_needs/CANDIDATE_SECOND_PREMISES.md`](../A_omegaJ_exploratory_needs/CANDIDATE_SECOND_PREMISES.md) (P2-2) · [`../A_omegaJ_rule1/AXIOM.md`](../A_omegaJ_rule1/AXIOM.md) · [`../omegaJ_forward/REQUIRED_INPUTS.md`](../omegaJ_forward/REQUIRED_INPUTS.md)  
**Grade of this premise:** **CANDIDATE schema** · **MISSING_INPUT** · **not Derived** · **no land**  
**Band (locked before any land):** ACCEPT **[3, 12] keV** · ANOMALOUS-REVIEW \((0.057,3)\cup(12,30]\) · KILL **< 0.057 keV**

---

## 0. Verdict in one line

**A_ωJ-direct is the collapsed-ratio twin of A_Jχ: one free micro frequency is the right residual dimension, but no closed seat-operator formula for \(\omega_J\) exists in the corpus — filling it with C0/C6/C7/C8 or silent IDs is forbidden; no land, no band score.**

---

## 1. Precise statement (CANDIDATE second premise)

> **A_ωJ-direct.** The seat sector supplies a **single** micro formula
> \[
> \omega_J = \omega_J^\mathrm{micro}(\text{seat operators}, T_\mathrm{sph})
> \]
> that is the junction plasma frequency of the **driven** cos term
> \(U_J=-\chi\omega_J^2\cos(\varphi-\dot\theta t)\) at \(T_\mathrm{sph}\), equivalent to collapsing \(J_\mathrm{seat}/\chi\), and **independent of \(\eta\), \(R_\mathrm{need}\), and declined IDs** (\(v_L\), silent \(f\to\chi\)).

This is hand-off **S2** from `A_omegaJ_rule1` — Package A form of the original gap, strengthened to **force a formula**, not only a name.

**Algebraic equivalence to P2-1 for \(R\):**

\[
R = \frac{\omega_J^2}{2\Gamma_\varphi\dot\theta}
\quad\text{depends only on }\omega_J\text{ (and stocked }\Gamma_\varphi,\dot\theta\text{).}
\]

Absolute \(\chi\) never enters. Direct micro \(\omega_J\) and pair \(\sqrt{J/\chi}\) close the **same** residual.

---

## 2. What A_ωJ-direct would have to deliver (checklist)

| # | Delivery | Status in corpus today |
|---|---|---|
| 1 | A **closed expression** in seat-micro symbols (operators, VEVs, matching) | **Missing** — form open |
| 2 | Evaluation at \(T_\mathrm{sph}\) without \(\eta\), \(R_\mathrm{need}\) | **Not yet** |
| 3 | Explicit identity with **driven** junction plasma frequency (not pin, not Jeans, not \(T_\mathrm{on}\)) | **Not written** |
| 4 | Independence I1–I7 on every input symbol | **Not yet testable** |
| 5 | Numeric result scored only on locked band | **No number** |

**Emptiness rule (from exploratory P2-2 should-not-exist):** writing “there exists \(\omega_J^\mathrm{micro}\)” without an expression is **not** a premise that can face the band.

---

## 3. can-exist (why the framework permits the schema)

1. **Correct residual dimension.** After A_ωJ + stocked \(\{\Gamma_\varphi,\dot\theta,m_1\}\), exactly **one** free frequency remains (`DERIVATION_ATTEMPT.md`). Direct micro is the minimal close.

2. **Avoids absolute-χ bookkeeping.** χ cancels in the EOM and in \(R\). Pricing only the ratio / frequency matches what the rectifier actually needs.

3. **Compatible with stage-8 “what the sector must supply.”** Stage 8 re-points consumers to seat \(\omega_J\approx 5.68\,\mathrm{keV}\) as *target*, not as micro land — A_ωJ-direct is the schema that would turn that re-point into a derivation *if* a formula appears.

4. **Locus already fixed.** Tenth-channel driven cos term is the surviving class-B carrier; A_ωJ-direct asks that carrier for a number.

5. **No new field required.** Schema does not invent a second phase or a new portal — only a price law on the existing formalization.

---

## 4. should-not-exist (adversarial kill case)

### Charge A / E — empty formula theater

“Seat supplies \(\omega_J^\mathrm{micro}\)” without writing the RHS is deferred fit. Rule 1 can look successful as **registry** while never facing the band. Prefer no premise over a permanent empty shelf object.

### Charge B — forbidden fill patterns

The corpus already *tempts* illegal fills (all **DEAD** as lands; see `DEAD_LANES.md` / roster):

| Temptation | Expression | Kill |
|---|---|---|
| η-bootstrap | \(\sqrt{2 R_\mathrm{need}\Gamma_\varphi\dot\theta}\) | I1 / C0 |
| Stale-ratio basin | ~1.90 keV under \(\Gamma/\dot\theta\sim 10^7\) | I2 / C11 |
| Geom-mean proximity | \(\sqrt{m_1\Gamma_\varphi}\sim 3.5\,\mathrm{keV}\) | I7 / C6 |
| Freeze timing | \(\omega_J\equiv T_\mathrm{on}\approx 9.4\,\mathrm{keV}\) | I7 / C7 |
| Tautology factor | \(\sqrt{\dot\theta\Gamma_\varphi}\times\sqrt{2R}\) | I1 / C8 |
| Pin mass | \(\omega_J\sim m_1\) | C4 / wrong scale |
| Jeans | \(\sqrt{4\pi G\rho}\) | I5 / C2 |
| \(v_L\) manufacture | decay const = \(v_L\), solve | I3 / C5 |

**Any “direct formula” that is one of the above is not A_ωJ-direct — it is a dead lane wearing a new label.**

### Charge C — miracle scale

If every natural seat IR scale is meV and every UV face is multi-TeV, a keV formula requires intermediate engineering. That pressure is **K5**, not a license to invent a dial.

### Charge D — formalization lock-in

Stage 8’s single-harmonic cos drive is a **formalization of a class**. Elevating “direct \(\omega_J\)” freezes that template. If true seat–visible current–phase is multi-harmonic or non-overdamped, A_ωJ-direct prices the wrong object.

**Adversary verdict:** do not fill A_ωJ-direct with dimensional analysis of stocked rates; do not treat schema registration as residual payment.

---

## 5. Forbidden vs legal formula shapes

### Forbidden shapes (do not write as micro)

```
ω_J = sqrt(2 * R_need * Γ_φ * θ̇)          # C0 circular
ω_J = sqrt(m1 * Γ_φ)                        # C6 proximity
ω_J = T_on                                  # C7 proximity
ω_J = m1                                    # C4 wrong object/scale
ω_J = sqrt(4π G ρ)                          # C2 Jeans
χ = v_L  then  invent J                     # I3
χ = f_e-scalar then invent J                # I4
```

### Legal shape (template only — RHS empty in corpus)

```
ω_J = F( seat operators O_A, … ;
         matching coefficients forced by sector, not by η ;
         T_sph evaluation )
```

with **proof** that \(\eta, R_\mathrm{need}, j^\star, \omega_J^\star\) never enter \(F\), and **no** free constant chosen to land near 5.672 keV.

**This package does not invent \(F\).**

---

## 6. Relation to stocked seat UV (headline)

| Stocked object | Role for A_ωJ-direct |
|---|---|
| Portal = tenth-channel seat term | Locus of \(F\) |
| \(O_A\) UV form | Candidate input symbols of \(F\) — **map unwritten** |
| Stage-8 \(U_J\), χ cancel | Defines *what* \(\omega_J\) means |
| Quartet 5.672 keV | **Grading center only** — illegal as \(F\)’s output identity |
| Seat-trickle death | Proves rate carrier ≠ plasma frequency land |

Details: [`CORPUS_SEAT_MAP.md`](./CORPUS_SEAT_MAP.md) · no-land argument: [`NO_LAND_PROOF.md`](./NO_LAND_PROOF.md).

---

## 7. Kill conditions

| Kill | Trigger |
|---|---|
| Emptiness | Premise never writes an actual expression |
| I1 / C0 | Expression is η-bootstrap sold as micro |
| I2 | Stale-ratio 1.9 keV target |
| I3–I4 | Silent \(v_L\) / \(f\to\chi\) inside formula |
| I5–I6 | Jeans or pin curvature as \(\omega_J\) |
| I7 | Proximity \(\sqrt{m_1\Gamma_\varphi}\), \(T_\mathrm{on}\), pure rate combos without chain |
| Honesty | Free dial to 5.672 keV |
| K1 / K5 | As in P2-1 |

---

## 8. Band score

| Item | Value |
|---|---|
| Forward \(\omega_J\) under A_ωJ-direct this package | **None** |
| **Band score** | **no score — no land** |
| Equivalence | Same residual as P2-1; choosing pair vs direct is bookkeeping once \(F\) exists |

---

## 9. Explicit non-claims

1. A_ωJ-direct is **not** Derived / PAID.  
2. No free constant to hit **5.672 keV**.  
3. No circular \(R_\mathrm{need}/\eta\).  
4. No silent \(v_L\) / \(f\to\chi\).  
5. No adoption of C0/C6/C7/C8/C2/C4 as “direct micro.”  
6. No MCMC / PolyChord / H₀ / ownership.  
7. No living-doc grade upgrade.

---

## 10. Disposition

| Field | Value |
|---|---|
| Grade | **SURVIVOR-SCHEMA / CANDIDATE** |
| Content fill | **MISSING_INPUT** (formula empty) |
| Land | **No** |
| Relation to P2-1 | Same residual; pair vs collapsed ratio |
| Next honest step | Write real \(F\) from seat operators **or** fire K5 — [`NEXT_AXIOM_CANDIDATES.md`](./NEXT_AXIOM_CANDIDATES.md) |

---

*End P2_2_A_omegaJ_direct.md*
