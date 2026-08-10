# Outsider recompute — area-law quarter (QG Goal A / Q2)

**One page.** No PRTOE cosmology ontology required. Verifies the *ratio arithmetic*
\(12\pi/48\pi = 1/4\) used in `docs/PRTOE_quantum_gravity.md` §4a — **not** a
dynamical Page curve, **not** absolute \(G\), **not** ε / CLASS.

> **Packaging fence:** This recipe proves **Q2 coefficient ratio only**. It does **not**
> re-run Page week1/2 instruments, does **not** prove Goal A “all physics,” and does **not**
> close Q6. Optional supertrace is a **separate** command.

---

## Command

From repository root:

```bash
python3 scripts/quantum_area_law_quarter.py
```

No extra packages beyond a normal Python 3 install (`math` stdlib only).

---

## Expected result

| Check | Fence |
|---|---|
| Process exit | **0** |
| Algebra | \(12\pi/48\pi = 0.2500000000000000\) **PASS** |
| Numerical cancel | Dummy \(N,\varepsilon,A\): \(S/(A/G) = 0.25\) **PASS** |
| Artifact | Rewrites `docs/working_logs/_runs/quantum_null_hardening_20260803/AREA_LAW_QUARTER.md` |

Stdout prints the same markdown the script writes. Exit **1** only if either check fails
(should not happen for correct stdlib floating point).

---

## What the script pays

| Object | Status |
|---|---|
| Coefficient \(1/4\) for **minimal scalars** as heat-kernel ratio | **paid** |
| Species \(N\) + cutoff \(\varepsilon\) cancel in the ratio | **paid** |

## What the script does **not** pay

| Object | Status |
|---|---|
| Dynamical **Page curve** \(S_{\mathrm{rad}}(v)\) | **OPEN** — see `quantum_page_curve_scaffold.py` (design only) |
| Roster extension (spin-½, gauge+edge modes, \(\xi=1/6\)) | **candidate** in `docs/exploratory/PRTOE_entropy.md` §3 |
| Absolute SI Newton constant | **OPEN** residual on QG file §5 |
| Supertrace / generation counting | Separate instrument: `scripts/supertrace_k1_verify.py` + shipped **supertrace-note** |

Literature coefficients (Sakharov–Visser / 't Hooft–Srednicki class) are **inputs** the
script checks for consistency of the stated ratio — not a PRTOE discovery of \(1/4\).

---

## Optional related public algebra

- Supertrace finiteness note (not this command): `docs/arXivReady/supertrace-note.pdf`  
- Program notes: `docs/working_logs/_runs/quantum_null_hardening_20260803/AREA_LAW_QUARTER.md`  
- Attach context: `docs/working_logs/_runs/qg_goalA_20260803/ATTACH_STATEMENT.md`

---

## Non-claims

- **Not** evidence that expansion ε succeeds.  
- **Not** a Page-curve close.  
- **Not** a TOE certificate.
