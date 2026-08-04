# R3 — τ = ½ln2 provenance audit (post Koide lane (c))

**Date:** 2026-08-03  
**Responds to:** NEXT ISSUE R3-tau-lock  
**NO FABRICATIONS.**

---

## 1. Derivation chain exhibited (on the record)

| Step | Statement | Physics used | Uses thermal/flat delivery? |
|---|---|---|---|
| 0 | Input: **Q = 2/3** (exact for algebra; measured Q ≈ 0.6666605 for table) | measured regularity / fence | **No** |
| 1 | Circulant family kernel Fourier modes f₀, f₁ | Z₃ ring **structure** | **No** |
| 2 | Parseval identity: \(Q = \tfrac13 + \tfrac23 |f_1/f_0|^2\) | Fourier algebra | **No** |
| 3 | At Q=2/3: \(\rho \equiv |f_1/f_0| = 1/\sqrt{2}\) | algebra | **No** |
| 4 | Define \(\tau = -\ln\rho\) | **definition** (kernel modulus as e^(−τ)) | **No** |
| 5 | \(\tau = \tfrac12\ln 2 = 0.34657359\ldots\) | algebra | **No** |
| 6 | \(T_c = \tau\, m_e = 177.10\,\mathrm{keV}\) | scale ID √σ_dark = m_e + τ | **No** (pin separate) |
| 7 | \(\rho_{\Lambda}^{1/4} = \tfrac92 \alpha^4 \tau m_e\) | DE closed form | **No** |

**Recompute (stdlib):**
```text
rho2 = (2/3 - 1/3)/(2/3) = 1/2
rho  = 1/√2
tau  = -ln(rho) = (1/2)ln2   (exact match)
```

From **measured** Q=0.6666605: τ_meas − ½ln2 ≈ **+9.25×10⁻⁶** (fence-scale, not a new mechanism).

---

## 2. Answer to red ask (1) — mechanism-free?

**Yes — the Parseval → ½ln2 link is mechanism-free** of the **contradicted thermal/flat delivery law**.

- Lane (c) killed the *delivery physics* that would force the null/amplitudes to exact Q=2/3 via thermal freeze.
- The τ chain does **not** invoke that law. It only uses:
  1. **Q = 2/3** as input (now graded: measured regularity / OPEN mechanism), and  
  2. **Parseval structure** on the circulant kernel.

**Therefore τ does *not* inherit the thermal contradiction as a false arithmetic step.**  
**It does inherit the conditionality:** τ is only as grounded as the input Q=2/3.

Downstream T_c, ρ_Λ¼, and discriminator x₁=(2/9) that ride **Q=2/3 / θ_B** remain **conditional on the measured relation**, not on a closed mechanism.

**What would force a re-flag as “inherits contradiction”:** any claim that τ is derived because the *thermal delivery mechanism* paid Q=2/3. That claim is **false** after lane (c).

---

## 3. Answer to red ask (2) — locking derivation

**Still OPEN / OWED.**  

Why the kernel *must* sit at |f₁/f₀|=1/√2 without **inputting** Q=2/3 (or the null) is exactly the #101 residual. Parseval is **one evaluation among kernels**, not a lock.

Sprint rules: **no invention** of a locking mechanism this turn.  
Honest stamp: **OPEN-BLOCKED (OPEN-THEORY)** — same wall as Koide mechanism exactness.

---

## 4. Recommended grade (for referee)

| Object | Pre-R2 grade | Post-R2 recommended grade |
|---|---|---|
| τ = ½ln2 algebra *given* Q=2/3 | derived-conditional (Parseval) | **stands** as **derived-conditional on measured Q=2/3** (Parseval structure only) |
| τ as “from the Koide kernel” without disclosure | ambiguous | **requires disclosure:** condition is **measured Q regularity**, not paid thermal mechanism |
| Locking derivation of τ without Q input | owed | **still owed / OPEN-BLOCKED** |
| Lattice P-2026-048 | decisive external | **unaffected** |

**Binding disclosure line (proposed for banner/ledger):**

> τ = ½ln2 is the Parseval evaluation of the circulant kernel modulus at Q=2/3. It does **not** use the contradicted thermal/flat delivery law. After R2-koide lane (c), the condition is **measured Q=2/3 (relation stands; mechanism open)**, not a closed Koide mechanism. Lattice T_c/√σ remains the external referee (P-2026-048).

---

## 5. Non-claims

- Not a new derivation of Q=2/3  
- Not a close of #101  
- Not that ρ_Λ is precision-predicted  
- Not that thermal path paid τ

---

## 6. Red AGREE-IF cure — three conditions (2026-08-03 16:48)

Claude confirmed Parseval mechanism-free of thermal *delivery*. Cure: condition set is **three** members, not one:

1. **Measured Q = 2/3**
2. **Scale pin √σ_dark = m_e**
3. **e^(−τ) thermal-weight reading of kernel modulus** |f₁/f₀| (identification of Fourier modulus with Boltzmann-weight form used as T_c/m_e) — **this is what lattice P-048 tests**, not mere algebra

Step 4 "definition" is free algebra until step 6 reads τ as condensation temperature — that identification is physical content.

**Binding disclosure:**
> derived-conditional on measured Q=2/3, the √σ_dark=m_e pin, **and the e^(−τ) thermal-weight reading of the kernel modulus** — the composite being what lattice P-048 tests.

Desk rows updated on CC + koide ledgers/banners.
