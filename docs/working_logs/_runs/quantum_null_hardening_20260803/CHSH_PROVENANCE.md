# CHSH formula provenance — B(r) = 2√(1 + tanh²(2r))

**Date:** 2026-08-03  
**Task:** Blue-team literature/provenance check on the two-mode-squeezed CHSH family used by `scripts/quantum_chsh_tsirelson.py`.  
**Verdict:** **STANDARD** — verification / null-hardening of a known result, not discovery.  
**Action on null-hardening:** **Do not weaken.** E1–E2 remain null-hardened under assumptions A1–A4.

---

## 1. Formula under audit

$$
B(r) = 2\sqrt{1 + \tanh^2(2r)}
$$

Properties enforced by the script:

| limit | value | role |
|---|---|---|
| \(r \to 0\) | \(B \to 2\) | classical CHSH bound |
| \(r \to \infty\) | \(B \to 2\sqrt{2}\) | Tsirelson / Cirel’son bound |
| all finite \(r\) | \(B(r) \le 2\sqrt{2}\) | never superquantum |

---

## 2. Corpus inventory (where the formula lives)

| path | role |
|---|---|
| `scripts/quantum_chsh_tsirelson.py` | implements \(B(r)\); writes table; limit PASS checks |
| `docs/working_logs/_runs/quantum_null_hardening_20260803/CHSH_TSIRELSON.md` | numeric table from that script |
| `docs/exploratory/PRTOE_quantum_entanglement.md` §6 claim E1 | grades formula **null-hardened** under A1–A4 |
| `docs/exploratory/PRTOE_quantum_trio.md` | seating rests on C4 CHSH computation |
| `docs/exploratory/PRTOE_PHYSICS_DOMAINS.md` | “pseudospin CHSH for the medium’s pair states” |
| `docs/exploratory/PRTOE_INTERACTION_ATLAS.md` | same pseudospin phrasing |
| `docs/working_logs/_AUDIT_LEDGER.md` (~line 1387) | audit: “correct two-mode-squeezed result saturating at 2√2” |
| `docs/BIBLIOGRAPHY.md` **[ChenPanHouZhang2002]** | booked as TMSV pseudospin CHSH source feeding C4 |
| `docs/exploratory/PRTOE_references.md` | **[V]** Chen, Pan, Hou & Zhang, arXiv:quant-ph/0103051 |
| `docs/working_logs/_runs/quantum_null_hardening_20260803/PROGRAM.md` P4 | notes script *assumes* the standard family; elevation = derive from pair Hamiltonian if recorded |

**Finding inside the corpus:** There is **no first-principles re-derivation** of \(B(r)\) from a PRTOE pair Hamiltonian in-tree. The script imports the standard family and checks its Tsirelson/classical limits. Attribution to the TMSV/pseudospin literature is already booked (Chen et al. 2002); PROGRAM P4 correctly flags “derive from our Hamiltonian” as a future elevation, not as a missing correctness fix.

---

## 3. Literature class of result (external check)

### Primary source (matches formula exactly)

**Z.-B. Chen, J.-W. Pan, G. Hou, and Y.-D. Zhang,**  
“Maximal Violation of Bell’s Inequalities for Continuous Variable Systems,”  
Phys. Rev. Lett. **88**, 040406 (2002); arXiv:quant-ph/0103051.

Construction (paraphrase of their § after Eq. (15)–(22)):

1. Define **parity pseudospin** operators \(s_z, s_\pm\) on each bosonic mode (Fock parity / parity-flip).
2. Build the CHSH Bell operator from \(\mathbf{a}\cdot\hat{\mathbf{s}}_1\) and \(\mathbf{b}\cdot\hat{\mathbf{s}}_2\) exactly as for qubits.
3. For the two-mode squeezed vacuum (NOPA / TMSV)
   \[
   |\mathrm{TMSV}\rangle = \sum_{n=0}^{\infty} \frac{(\tanh r)^n}{\cosh r}\,|nn\rangle,
   \]
   the two-point correlation is
   \[
   E(\theta_a,\theta_b) = \cos\theta_a\cos\theta_b + K\sin\theta_a\sin\theta_b,
   \]
   with
   \[
   K(r) \equiv \tanh(2r) \le 1.
   \]
4. At the optimal angle setting (\(\theta_a=0\), \(\theta_{a'}=\pi/2\), \(\theta_b=-\theta_{b'}=\tan^{-1}K\)):
   \[
   \langle\mathcal{B}_{\mathrm{CHSH}}\rangle_{\max}
     = 2\sqrt{1+K^2}
     = 2\sqrt{1+\tanh^2(2r)}.
   \]
5. Limits: \(r=0 \Rightarrow B=2\); \(r\to\infty \Rightarrow K\to 1 \Rightarrow B=2\sqrt{2}\) (maximal CHSH / Tsirelson for this operator class).

**This is identical to the formula in our script.** Our use is therefore:

> **Standard pseudospin-CHSH result for TMSV (Chen–Pan–Hou–Zhang 2002 class), numerically verified as a registered null — not a PRTOE discovery.**

### Class membership (what “standard” means here)

- **Not** the only possible CV Bell test (Banaszek–Wódkiewicz parity/Wigner tests, homodyne CHSH, hybrid encodings, etc. give *different* \(r\)-dependences and often *do not* saturate \(2\sqrt{2}\) for finite TMSV).
- **Is** the standard result for the **parity-pseudospin** CHSH operator on TMSV/NOPA, which the corpus explicitly claims (“pseudospin CHSH for the medium’s pair states”).
- Tsirelson bound itself: **[Tsirelson1980]** / Cirel’son, Lett. Math. Phys. 4, 93 (1980) — already in `docs/BIBLIOGRAPHY.md`.

### Schema of the derivation (one-line)

\[
E = \cos\alpha\cos\beta + \tanh(2r)\,\sin\alpha\sin\beta
\quad\Rightarrow\quad
B_{\mathrm{opt}} = 2\sqrt{1+\tanh^2(2r)}
\]

for dichotomic \(\pm 1\) observables with qubit-like algebra (pseudospin). Same algebraic pattern as a Werner/Bell-diagonal qubit family with correlation strength \(C=\tanh(2r)\).

---

## 4. What our script does vs does not claim

| does | does not |
|---|---|
| Enforce classical floor, Tsirelson ceiling, monotonic approach | Derive Hilbert space / Born rule |
| Register Tsirelson as permanent kill line (superquantum or preferred-frame spoil) | Claim a new CHSH formula |
| Match Chen et al. 2002 under A1–A4 | Replace experimental CV Bell literature |

Assumptions already explicit in the script (kept):

- **(A1)** Pair state = TMSV (or equivalent Bell family parameterized by squeeze \(r\)).
- **(A2)** Optimal CHSH angles for that family (Chen et al. setting).
- **(A3)** Substrate quantization = standard bosonic modes / pseudospin operators.
- **(A4)** No PR-box / superquantum resources.

---

## 5. Fail criteria for this provenance pass

| condition | status |
|---|---|
| Formula disagrees with Chen et al. (2002) optimal pseudospin CHSH | **no** — exact match |
| Corpus claimed *discovery* of \(B(r)\) | **no** — audit + bibliography already call it the two-mode-squeezed / C4 source result |
| Wrong operator class advertised (e.g. BW Wigner CHSH sold as this formula) | **no** — corpus says “pseudospin” consistently |
| Null-hardening overstated as Born derivation | **no** — script and E-ledger mark Born OPEN / not derived |

**If the formula had been wrong:** flag **FAIL**, replace with the Chen et al. expression (or the correct operator-class formula), and re-run the limit table. **Not applicable.**

---

## 6. Decision for null-hardening

| item | decision |
|---|---|
| E1 grade (`PRTOE_quantum_entanglement.md`) | **keep null-hardened** |
| Script / `CHSH_TSIRELSON.md` | **keep** as verification harness |
| Provenance | **cite Chen–Pan–Hou–Zhang 2002 class**; script = verification not discovery |
| PROGRAM P4 | **unchanged** (elevation: derive from model pair Hamiltonian if one is recorded; optional, not a correctness bug) |
| Weaken null-hardening? | **No** |

---

## 7. Recommended one-sentence citation for future prose

> Optimal pseudospin CHSH for the two-mode squeezed vacuum is the standard result \(B(r)=2\sqrt{1+\tanh^2(2r)}\) (Chen, Pan, Hou & Zhang, PRL 88, 040406 (2002)); our script verifies the classical and Tsirelson limits of that family as a registered null.

---

## 8. Sources checked this pass

1. In-corpus: script, CHSH_TSIRELSON.md, quantum_entanglement §6, quantum_trio, PHYSICS_DOMAINS, INTERACTION_ATLAS, AUDIT_LEDGER, BIBLIOGRAPHY [ChenPanHouZhang2002], PRTOE_references [V], PROGRAM.md P4.
2. External: arXiv:quant-ph/0103051 (Chen et al. 2002) — Eqs. for \(K=\tanh(2r)\) and \(\langle\mathcal{B}\rangle_{\max}=2\sqrt{1+K^2}\).

**End provenance note.**
