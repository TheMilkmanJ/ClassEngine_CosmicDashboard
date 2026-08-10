# BAND_SCORE.md — Score against pre-registered ω_J bands

**Package:** `A_omegaJ_rule1`  
**Date:** 2026-08-04  
**Band authority (fixed before any forward derivation):**  
[`../omegaJ_forward/KILL_AND_BANDS.md`](../omegaJ_forward/KILL_AND_BANDS.md) · `PRTOE_baryogenesis.md` §3a · `scripts/baryogenesis_junction_closure.py`

---

## 1. Pre-registered bands (locked — not reopened)

| Disposition | Derived \(\omega_J\) |
|---|---|
| **ACCEPT** | \([3.0,\, 12.0]\,\mathrm{keV}\) |
| **ANOMALOUS-REVIEW** | \((0.057,\, 3.0)\cup(12,\, 30]\,\mathrm{keV}\) |
| **KILL** junction route | \(< 0.057\,\mathrm{keV}\) |
| Forbidden artifact center | \(1.90\,\mathrm{keV}\) under stale \(\Gamma_\varphi/\dot\theta=10^7\) |

**Rule:** score only a **forward-derived** \(\omega_J\). Do not score the back-solve. Do not move the band after seeing a preferred land.

---

## 2. What this Rule 1 exercise produced

| Item | Result |
|---|---|
| Axiom registered | A_ωJ (CANDIDATE) — form \(\omega_J^2=J_\mathrm{seat}/\chi\) |
| Forward numeric \(\omega_J\) | **None** |
| Circular / forbidden trials | Rejected (see DERIVATION_ATTEMPT) |

---

## 3. Score

### **NO SCORE — NO LAND**

There is **no** forward-derived \(\omega_J\) to place in ACCEPT / ANOMALOUS-REVIEW / KILL.

| Pseudo-score candidates | Disposition |
|---|---|
| BACK-SOLVED \(5.672\,\mathrm{keV}\) | **Not scored** — not a land; would sit in ACCEPT *if* it were forward, but it is not |
| \(\sqrt{m_1\Gamma_\varphi}\sim 3.5\,\mathrm{keV}\) | **Not scored** — no mechanism under A_ωJ |
| \(T_\mathrm{on}\sim 9.4\,\mathrm{keV}\) | **Not scored** — proximity only |
| \(\omega_J\sim m_1\) | **Not scored** as land; would be **KILL** if illegally adopted |
| Jeans at \(T_\mathrm{sph}\) | **Not scored** as junction \(\omega_J\); would be **KILL** if illegally adopted |
| Artifact \(1.90\,\mathrm{keV}\) | **Forbidden target** — do not grade against |

---

## 4. Band remains binding for the future

When (and only when) a non-circular micro price of \(\omega_J\) appears:

1. Compute the number from that micro chain.  
2. Score **only** against the table in §1.  
3. Do **not** retarget to \(1.90\,\mathrm{keV}\).  
4. Do **not** treat quartet consistency as the score.

Until then: **no score — no land.**

---

## 5. Relation to residual grade

| Residual | Grade after this package |
|---|---|
| Forward \(\omega_J\) (#39 / NI-D3-1) | **OPEN-BLOCKED** |
| A_ωJ premise | **CANDIDATE** (registered) |
| Quartet arithmetic | machine-backed back-solve (unchanged) |

---

*End BAND_SCORE.md*
