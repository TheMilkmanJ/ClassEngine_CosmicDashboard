# Substitutions registry — external stand-in data only

**Authority:** owner rule 2026-08-04 (Claude red filing: `OWNER RULE (2 parts) invented premises and substituted data`).  
**Builder:** blue. **Seat:** tribunal / red re-verify when rows open.

---

## Distinction (do not collapse)

| class | what it is | handling |
|---|---|---|
| **Invented premise** | Physics postulate | **RULE 1** — CANDIDATE entry; can-exist + should-not-exist; pre-registered band **before** derivation; never score against a target it could be tuned to hit |
| **Substituted datum** | Number standing in for a measurement | **RULE 2** — this file; token `[SUB-2026-NNN]`; ceiling **CANDIDATE** forever |

**Default for missing external inputs:** `MISSING_INPUT` (preferred). A SUB is a **dated explicit exception**, never the fallback.

**Not SUB-eligible (exclusions — hard):**

- pre-registered scores  
- booking gate  
- **chain-derived quantities** (H₀, Σm_ν, …) — wait for dual gate; labelled H₀ is peek-book with manners  
- shipped paper chain  

---

## RULE 2 — row schema

One row per ID. Status ∈ {`OPEN`, `PEELED`, `REJECTED`, `SUPERSEDED`}.

| field | meaning |
|---|---|
| **ID** | `[SUB-2026-NNN]` sequential |
| **stands-in-for** | what measurement / external quantity is missing |
| **value used** | the stand-in number (and units) |
| **why licensed** | why construction is blocked without it (progress case) |
| **what verifies** | what real input peels it |
| **what falsifies** | what would reject the stand-in path |
| **date opened** | YYYY-MM-DD |
| **status** | OPEN / PEELED / … |
| **known dependents** | files / claims / packages that use the token or derive from it |

**Token discipline:** every use of the value **or anything derived from it** carries the ID inline so `grep SUB-2026-` walks the taint chain mechanically.

**Ceiling:** nothing resting on a SUB grades above **CANDIDATE**, ever.

**Peel procedure:** grep ID → re-run **and re-grade** every dependent → close row with outcome (retain history).

**Live visibility:** open rows listed below with age; no paper ships with un-peeled SUB in chain.

---

## Open substitutions

| ID | stands-in-for | value used | why licensed | verifies | falsifies | opened | status | dependents |
|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | **none** |

**Open count: 0.**  
**Oldest open age: n/a.**

---

## Peeled / closed (history retained)

| ID | outcome | date closed | notes |
|---|---|---|---|
| — | — | — | (empty) |

---

## RULE 1 pointer (not this registry)

Invented **premises** are **not** rows here. They live in construction packages as CANDIDATE with:

1. CANDIDATE grade only on entry  
2. written can-exist argument  
3. written should-not-exist (kill-seeking) argument  
4. pre-registered band fixed **before** derivation from the premise  

**Working template:** `docs/working_logs/_runs/theory_construction_20260804/fa3_metric_off/` (P1+P2).  
**First live axiom-slot exercise (not a SUB):** A_ωJ under `theory_construction_20260804/omegaJ_forward/` — band already locked ACCEPT [3,12] keV · KILL &lt;0.057 keV.

**Correction (red):** A_ωJ tests **RULE 1**, not RULE 2. Wilson A_μ(x) path-order number would be RULE 2 if ever substituted (and remains MISSING_INPUT by default — do not invent to hit θ_W = 2/9).

---

## Related

- Failures ledger discipline: `docs/PRTOE_FAILURES_LEDGER.md`  
- MISSING_INPUT culture: corpus default  
- Booking gate: `scripts/book_bbnfix_when_ready.py` (never SUB around it)

*NO FABRICATIONS. SUB is not peek-book. Premise is not free score.*
