# CONSTRUCTION_FORCE_THEOREM — SV-N4-THM

**Package:** `theory_construction_wave_20260805/bounce/`  
**Survivor:** **SV-N4-THM** · residual T-W1d force-branch  
**Date:** 2026-08-05  
**Mode:** **theorem sketch requirements only** · do **not** invent T-N4 proof  
**Land this wave?** **NO** · `FORCE_BRANCH_DERIVED = false` · \(n_\mathrm{lands}=0\)

---

## 0. Standing bar (reconfirmed)

Sources: `n4_force_branch_20260804/` · reconfirm `bounce/logs/bounce_n4_force_branch_attempt.log`

| field | value |
|---|---|
| FORCE_BRANCH_DERIVED | **false** |
| NAMED_THEOREM_STOCKED | **false** |
| arguments examined (FB1–FB20) | **20** |
| arguments forcing without free P2 | **0** |
| can_derive_H_re_without_declaration | **false** |
| P2 status | **CANDIDATE declaration** |
| invent T-N4 proof this wave | **FORBIDDEN** |

---

## 1. What a force-branch theorem must state

**PASS criterion (N4 REPORT §2):**

\[
\text{legal gate}\;(\langle\Theta\rangle>0\wedge\ell_\mathrm{grad}\gtrsim\xi)
\;\Rightarrow\;
H_\mathrm{re}>0
\]

as a **named theorem**, without free branch choice, without continuous metric-ON \(H=0\) at finite \(\rho\) (obstruction A), without fabricated \(N_\mathrm{med}\).

Still **not** full bounce COMPLETE: magnitude F-A2 / O6 remain orthogonal.

---

## 2. Named proof forms (requirements only — not proofs)

Source: `n4_force_branch_20260804/REPORT.md` §6

### Form T-N4-Israel (preferred GR-shaped)

**Premises (must be legal, not free dials):**

1. P1 (metric-off Phase II) **or** explicit metric-ON surface layer with stocked \(S_{ab}\).  
2. Gate: \(\langle\Theta\rangle>0\) and \(\ell_\mathrm{grad}\gtrsim\xi\) from **legal** GPE/hydro (production depth: N3).  
3. Stocked \(S_{ab}=S_{ab}[n,\Theta,\ell_\mathrm{grad},c_s,\xi]\) and \(K^+_{ab}\) of \(\Sigma_\mathrm{re}\) (closes G1–G3 under one-sided rewrite; **no \(K^-\)** under P1).

**Target statement:**

> Under (1)–(3) and exterior Friedmann at attach, the unique consistent root is  
> \(H_\mathrm{re}=+\sqrt{8\pi G\rho_\mathrm{re}/3+\sigma_\mathrm{re}^2/3}\).  
> The contracting root \(H_\mathrm{re}<0\) is **inconsistent** with the gate + Israel jump + (optional) M4 achronality jointly.

**Proof obligations (lemmas needed):**

| lemma | obligation | stocked? |
|---|---|---|
| **L-I1** | Well-posed one-sided Israel / OS-BC at \(\Sigma_\mathrm{re}\) with only \(K^+\) | forms CANDIDATE; not theorem |
| **L-I2** | \(S_{ab}\) or \(\mathcal{M}_{ab}\) Derived or axiom-licensed from medium (SV-SAB-MAP) | **NO** |
| **L-I3** | Embedding: \(K^+_{ab}=K^+_{ab}(H_\mathrm{re},\sigma_\mathrm{re},\ldots)\) explicit (SV-KPLUS) | **NO** |
| **L-I4** | Uniqueness of expanding root under joint constraints | **NO** |
| **L-I5** | Contracting root \(\Rightarrow\) contradiction (gate / jump / M4) | **NO** |
| **L-I6** | Domain not secretly continuous exterior \(H=0\) at finite \(\rho\) without shell (A fence) | obstruction A paid as DEAD path; not a force proof |
| **L-I7** | No free P2 insertion in premises | discipline only |

### Form T-N4-Acoustic (S-A style)

**Premises:** P1 + complete exit/re-entry maps \(\Phi_\mathrm{out},\Phi_\mathrm{in}\) with **no free sign parameter**.

**Target:** \(\Phi_\mathrm{in}\) at gate states is single-valued and lands only on expanding exterior FRW.

**Proof obligations (lemmas needed):**

| lemma | obligation | stocked? |
|---|---|---|
| **L-A1** | Closed \(\Phi_\mathrm{out}\) at exit (direction partial exists in dictionary language) | RECONSTRUCTED partial only |
| **L-A2** | Closed \(\Phi_\mathrm{in}\) inverse at re-entry (outputs \(H_\mathrm{re}\) sign uniquely) | **NO** (NC3 killed closed ρ; G7 underdetermined) |
| **L-A3** | No second branch in matching dictionary | **NO** as theorem (P2 still free declaration) |
| **L-A4** | Not P2 restated as “we only list expanding” | honesty bar |

### Form T-N4-Dual (contracting kill)

**Target:** under legal medium at gate + P1 domain, attaching \(H_\mathrm{re}<0\) contradicts M4 / causal structure / medium continuity — **without** assuming expanding FRW in the premise.

**Proof obligations (lemmas needed):**

| lemma | obligation | stocked? |
|---|---|---|
| **L-D1** | Precise contradiction statement with stocked M4 / achronality content | M4 is **constraint only** (FB4/FB20); not force-branch |
| **L-D2** | Medium continuity \(\Rightarrow\) no contract attach when \(\langle\Theta\rangle>0\) | **NO** (category: medium Θ ≠ exterior H) |
| **L-D3** | No NEC-force-expand smuggle without stocked NEC theorem | FB15 not stocked |

---

## 3. Kill classes already paid (do not restate as theorems)

Source: `ARGUMENT_KILL_TABLE.md` FB1–FB20 summary

| class | IDs | result |
|---|---|---|
| Continuous exterior path A | FB1, FB12 | **KILLED / DEAD** |
| P2 restatement | FB2, FB10, FB14 | **not a theorem** |
| Israel / Darmois empty content | FB3, FB5, FB16, FB19 | **MISSING_INPUT / ILL_POSED** |
| M4 constraints | FB4, FB20 | **constraint ≠ force-branch** |
| Medium stress alone | FB7, FB11 | **category error / medium-only** |
| Arrow / observer softener | FB9, FB17 | **non-derivation** |
| M2 dials | FB6 | **FORBIDDEN** |
| NEC force-expand | FB15 | **not stocked** |
| \(H_\mathrm{kin}\) target reframe | FB8, FB18 | **killed / reframe** |

**None of FB1–FB20 is promoted to T-N4-\* by this construction.**

---

## 4. Dependency on other survivors

| need | survivor | status |
|---|---|---|
| \(K^+_{ab}\) embedding | SV-KPLUS | MISSING |
| \(\Delta\Pi\to S_{ab}\) or OS-BC2 license | SV-SAB-MAP | CANDIDATE only |
| Closed \(\Phi_\mathrm{in}\) | SV-MATCH-NEW / FA2 | EXHAUSTED / OPEN |
| Gate production depth | N3 / CLASS | OPEN / CLASS-BOUND |

**Honest default until T-N4-\* appears:** keep **P2 as explicit CANDIDATE declaration**.

---

## 5. Grade

| field | value |
|---|---|
| **SV-N4-THM grade** | **MISSING_INPUT · theorem requirements only** |
| T-N4 proof invented | **false** (not done) |
| FORCE_BRANCH_DERIVED | **false** |
| lemmas complete | **0 / all open** |
| \(n_\mathrm{lands}\) | **0** |

### One-liner

> **SV-N4-THM: three proof forms restated with lemma checklists; no lemma closed; no T-N4 proof invented; FORCE_BRANCH_DERIVED stays false; lands 0.**

---

*NO FABRICATIONS. Kill-seeking ≠ derivation. P2 remains declaration.*
