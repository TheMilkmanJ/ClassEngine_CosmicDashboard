# CONSTRUCTION_MATCH_NEW — SV-MATCH-NEW

**Package:** `theory_construction_wave_20260805/bounce/`  
**Survivor:** **SV-MATCH-NEW** · residual T-W1c  
**Date:** 2026-08-05  
**Mode:** untried match-rule class only if not in R0–R6/NC*; else EXHAUSTED + schema for new class  
**Land this wave?** **NO** · \(n_\mathrm{lands}=0\)

---

## 0. Residual demand

A **new** acoustic/matching rule **outside** stocked R0–R5 / R6 / NC* that closes obstruction C without dial — or honest **EXHAUSTED** stamp under stocked inventory.

---

## 1. Stocked rule inventory (all tried or kill-stamped)

Sources: `n2_match_book_20260804/ALTERNATE_MATCH_RULES.md` · `SURVIVORS.md` · desk_t2 NC kills · exhaust DISPOSITION T-W1c · reconfirm `bounce/logs/bounce_n2_match_book_check.log`

| ID | rule | under stocked | closes C? |
|---|---|---|---|
| **R0** | \(H_\mathrm{kin}=H_F(\rho)\) | STOCKED-DEFAULT | **no** (N1 0 lands) |
| **R1** | kinematic target vs constraint | CANDIDATE-REFRAME | **no** (residual rename) |
| **R2** | shear-corrected \(H^2=8\pi G\rho/3+\sigma^2/3\) | form PAID; \(\sigma_\mathrm{re}\) OPEN | **no** |
| **R3** | Israel surface | MISSING_INPUT (empty) | **no** |
| **R4** | continuous metric-ON H through 0 | **DEAD** (A) | no |
| **R5** | free dial \(H_\mathrm{re}\) | **FORBIDDEN** | no |
| **R6** | quench integral → \(\rho_\mathrm{re}\) | DOUBLE-KILLED as NC1 | no |
| **NC2** | \(\sigma_\mathrm{re}\) bookkeeping as law | DOUBLE-KILLED | no |
| **NC3** | acoustic \(\Phi_\mathrm{in}\) closed \(\rho_\mathrm{re}\) | DOUBLE-KILLED | no |

### Dictionary status

Phase I–III matching book: **RECONSTRUCTED-PARTIAL** under P1+P2 domain.  
Phase II: exterior \(H\) **undefined**.  
Magnitude / Derived-\(H_\mathrm{re}\): **false**.

### Reconfirm (this construction wave)

```text
OMP_NUM_THREADS=1 nice -n 19 python3 scripts/bounce_n2_match_book_check.py
→ bounce/logs/bounce_n2_match_book_check.log
```

| stamp | value |
|---|---|
| exit | 0 (≠ PASS) |
| obstruction A | **stands** |
| obstruction C | **stands** |
| `can_derive_H_re_without_declaration` | **false** |
| lands | **0** |
| grade | PARTIAL_OPEN · dictionary RECONSTRUCTED |

---

## 2. Any untried match rule class under stocked content?

**Search rule:** a class is “untried” only if it is **not** already R0–R5, R6, or NC1–NC3 and is **licensed by stocked form**.

| candidate class (prose) | already covered by | untried? |
|---|---|---|
| Default Friedmann lock | R0 | no |
| Target/constraint split | R1 | no |
| Anisotropic shear in constraint | R2 | no |
| Thin-shell / Israel | R3 | no (empty content) |
| Continuous exterior H | R4 DEAD | no |
| Free H dial | R5 FORBIDDEN | no |
| Mode-bath / quench integral | R6/NC1 | no |
| Shear conversion bookkeeping | NC2 | no |
| Acoustic inverse Φ_in | NC3 | no |
| Dual bookkeeping Φ_out+Φ_in without tensor | OS-BC3 / S-A restatement (desk_t3) | **not a new C-closer** — N2 dictionary already; magnitude OPEN |
| One-sided Israel OS-BC1/2 | desk_t3 CANDIDATE forms | **subclass of R3 content gap** — not a new *rule class*; still MISSING \(K^+,S/\mathcal{M}\) |
| Match on \(v_g\) / FA1 \(x^*\) only | FA1 medium partial | **not written as exterior H lock**; SM open; would be new class **only if** closed exterior rule stocked — **not stocked** |

**Verdict:** **No untried licensed match-rule class remains under stocked content.**

```
MATCH_BOOK_EXHAUSTED
under_stocked: true
dictionary: RECONSTRUCTED-PARTIAL
alternate_rules_that_close_C: 0
new_class_named_this_wave: 0
```

---

## 3. SCHEMA for a **new** class only (not filled)

Because stocked inventory is exhausted, the only residual is an **unstocked new class**. Schema states what would count — **does not invent the rule**.

### Schema M-NEW — Legal exterior attach rule class

**What would count as a new class (must satisfy all):**

1. **Named rule** \(R_\star\) not equivalent to R0–R5, R6, NC1–NC3 (not a rename).  
2. **Domain:** P1-legal (Phase II exterior \(H\) undefined; no A-reopen).  
3. **Inputs:** only stocked legal medium/GR parts **or** newly licensed micro with dual scrutiny — **no** free \(H_\mathrm{re}\), \(N_\mathrm{med}\), \(\alpha\).  
4. **Closes C:** produces magnitude lock (band fixed first) without tautology (not inverse of \(H_\mathrm{kin}\) sold as medium law).  
5. **Sign:** either forces expanding root (feeds N4) or explicitly retains P2 as declaration without smuggling Derived-\(H\).  
6. **Proof or construction:** written map + scorecard; Rule-1 can-exist / should-not-exist.

**Examples of what is *not* a new class:**

- Renaming R1 (“target”) in new words.  
- Setting \(\rho_\mathrm{re}\) from \(H_\mathrm{kin}\) (C4).  
- Free dial R5.  
- Claiming Israel closed without \(S_{ab}/K^+\) content.

**Present content for \(R_\star\):** **empty**.

### Related open *content* (not new rule class)

| residual content | class it fills | status |
|---|---|---|
| Exterior \(K^+_{ab}\) + \(S_{ab}/\mathcal{M}\) | R3 content | SV-KPLUS / SV-SAB-MAP |
| Closed \(\rho_\mathrm{re}\) law | R0 amplitude | SV-FA2 |
| Θ_lock | R0 via Θ | SV-CLASS-ESCAPE |
| Force expanding root | N4 | SV-N4-THM |

These deepen **existing** IDs; they are not MATCH_NEW rule classes by themselves until a *new* attach predicate is written.

---

## 4. Grade

| field | value |
|---|---|
| **SV-MATCH-NEW grade** | **MATCH_BOOK_EXHAUSTED under stocked** · **OPEN-SCHEMA for unstocked new class only** |
| untried stocked class | **0** |
| rules that close C | **0** |
| \(n_\mathrm{lands}\) | **0** |
| dictionary | RECONSTRUCTED-PARTIAL (carry) |

### One-liner

> **SV-MATCH-NEW: R0–R5/R6/NC* inventory complete; no untried licensed class under stocked; SCHEMA M-NEW only for future unstocked rule; lands 0.**

---

*NO FABRICATIONS. Reconstructed dictionary ≠ bounce COMPLETE. exit0 ≠ PASS.*
