# Debt report: Page *curve* dynamics residual (“coefficient paid”) — 2026-08-03

**Board:** OPEN-THEORY (`docs/working_logs/_PROJECT_FINISH_ROADMAP.md` §OPEN-THEORY)  
**Home claim file:** [`docs/PRTOE_information_paradox.md`](../../../PRTOE_information_paradox.md)  
**Coefficient homes:** [`docs/PRTOE_quantum_gravity.md`](../../../PRTOE_quantum_gravity.md) §4a; [`docs/PRTOE_entropy.md`](../../../PRTOE_entropy.md) §3  
**Scope of this report:** inventory and grade only. **No Page-curve solution is invented.**

---

## 1. What “coefficient paid” means in this corpus

In the OPEN-THEORY list the residual is written:

> **Page *curve* dynamics (coefficient paid)**

That parenthetical is a **status lock**, not a claim that the Page curve has been computed.

### 1.1 The three Page-curve ingredients (status table, 2026-08-02)

From the header of [`PRTOE_information_paradox.md`](../../../PRTOE_information_paradox.md):

| Page-curve ingredient | status |
|---|---|
| area-law **coefficient** \(S = A/4G\) | **paid** — ratio of the two heat-kernel coefficients the same cutoff supplies, \(12\pi/48\pi = 1/4\) exactly ([`PRTOE_quantum_gravity.md`](../../../PRTOE_quantum_gravity.md) §4a) |
| **field-content** extension beyond minimally coupled scalars | **paid** class by class at candidate grade ([`PRTOE_entropy.md`](../../../PRTOE_entropy.md) §3) |
| the **curve itself** (\(S_\mathrm{rad}(v)\) vs Page time for phonon Hawking flux off a finite core) | **open — still un-run; do not fake it** |

**“Coefficient paid”** therefore means only the first row (and, in the same lock, the second row as residual gate after the coefficient): the Bekenstein quarter and its roster extension. It does **not** mean ingredient three.

### 1.2 What the paid coefficient *is* (cite)

[`PRTOE_quantum_gravity.md`](../../../PRTOE_quantum_gravity.md) §4a:

| quantity | coefficient |
|---|---|
| induced Newton (Sakharov–Visser) | \(1/G = N/(12\pi\,\varepsilon^2)\) |
| horizon entanglement ('t Hooft, heat-kernel) | \(S = N\cdot A/(48\pi\,\varepsilon^2)\) |

\[
\frac{S}{A/G} = \frac{12\pi}{48\pi} = \frac{1}{4} \quad\Longrightarrow\quad S = \frac{A}{4G}.
\]

Species count \(N\) and cutoff \(\varepsilon\) cancel in the ratio (universality). The model’s contribution is a **physical** regulator (Bogoliubov coherence factors of the medium) so both sides share one \(\varepsilon\). The entanglement-side O(1) check is paid **structurally** (2026-07-20): conical deficit \(R \supset 4\pi(1-n)\delta_\Sigma\) makes the area term and the induced-\(1/G\) term one heat-kernel coefficient \(a_1\); form factors cancel in the ratio.

Roster extension ([`PRTOE_entropy.md`](../../../PRTOE_entropy.md) §3; `scripts/area_law_roster_extension.py`, 2026-07-28): spin-½ preserves the ratio; gauge sector restored with edge modes as horizon entropy (named commitment E); conformal scalar drops out under \(\xi=1/6\). Candidate grade: ~63% unconditional / ~37% on E.

### 1.3 Why the roadmap says “coefficient paid” next to *curve* dynamics

[`PRTOE_no_singularities.md`](../../../PRTOE_no_singularities.md) §5: **the same payment removes the coefficient block on the Page curve** while the curve *computation* itself remains open. Historical block (no \(1/4\) from the medium) is gone; dynamical residual is not.

Corpus wording to keep unscrambled ([`PRTOE_information_paradox.md`](../../../PRTOE_information_paradox.md)):

> Neither payment delivers the Page curve as a computed object… “owed” means a real dynamics computation, not a remaining coefficient or roster debt.  
> **Status: structural dissolution plus coefficient-paid, curve-uncomputed.**

---

## 2. What is derived vs still open

### 2.1 Derived / paid (do not re-open as if they still gate the curve)

| object | grade | source |
|---|---|---|
| Structural dissolution of the *paradox premises* (no singularity shredder; finite unitary core; sonic-horizon leak at healing length) | structural argument | `PRTOE_information_paradox.md` §0–1; companion BH file |
| Area-law **scaling** (species and cutoff cancel) | derived | entropy §3; QG §4a |
| Area-law **coefficient** \(12\pi/48\pi = 1/4\) | derived (min. coupled scalars; regulator structural) | QG §4a; paid 2026-07-20 |
| **Roster extension** (full field content) | candidate grade (commitment E) | entropy §3; `area_law_roster_extension.py` |
| Docket #92 / #107 (area law / missing coefficient) | closed | `_DOCKET_INDEX.md` |
| File tag on information_paradox | COMPLETE-CONDITIONAL | `_FILE_COMPLETION_STATUS.md` |

### 2.2 Still open (the OPEN-THEORY residual)

| object | grade | source |
|---|---|---|
| **Page-curve dynamics:** \(S_\mathrm{rad}(v)\) vs Page time for **phonon Hawking flux off a finite core** | **open — un-run** | information_paradox header + §3(ii); entropy §3 status table |
| Island / replica-wormhole style quantitative construction | **not present** in this corpus as a PRTOE result | no island computation landed under `docs/PRTOE_*.md` or `scripts/` |
| Desk-algebra fake of a curve from the coefficient alone | **forbidden** | information_paradox status lock 2026-08-02 |

Entropy file explicit row ([`PRTOE_entropy.md`](../../../PRTOE_entropy.md) §3):

> Page-curve *dynamics* (phonon flux off a finite core) | **open** — separate computation; *not* an area-law residue

### 2.3 Naming hygiene (session debt board)

[`SCIENCE_DEBTS_2026-08-03.md`](../../SCIENCE_DEBTS_2026-08-03.md) lists “**Page curve coefficient** | untouched”. That label is **stale relative to the physics files**: the coefficient row is already **paid**. The live OPEN-THEORY residual is **dynamics**, as on the roadmap (“Page *curve* dynamics (coefficient paid)”). Prefer the roadmap wording; do not re-open coefficient bookkeeping as if unpaid.

---

## 3. NEXT falsifiable step — or no attack surface without new formalism

**Verdict for this debt today: no desk attack surface without new formalism.**

Reasons, all from corpus constraints:

1. **Status lock (2026-08-02):** open object is exclusively half (ii) — dynamical Page curve for the sonic-horizon / finite-core setup. “That computation is not desk-algebra from existing numbers; faking a curve from the coefficient alone is forbidden.”  
   ([`PRTOE_information_paradox.md`](../../../PRTOE_information_paradox.md) §3)

2. **No instrument exists** for half (ii). Scripts search: only `scripts/area_law_roster_extension.py` (coefficient/roster bookkeeping). No `page_curve_*`, no \(S_\mathrm{rad}(v)\) pipeline, no finite-core phonon flux evaporative entropy run.

3. **What a real next step would require** (not executed here; not invented as complete):
   - a defined exterior entropy functional of retarded time (or affine \(v\)) for radiation from a **sonic** horizon on a **finite-density** core;
   - a mass-loss / energy-flux law consistent with the BH/core construction;
   - a Page-time estimate and a curve shape that can rise then fall (or fail) under those inputs;
   - named kill criteria (e.g. pure thermal forever with no late purification; area-law inconsistency with paid \(A/4G\)).

Until that formalism is specified and instrumented, further “attacks” on this debt are either (a) re-auditing paid coefficient/roster rows (out of scope for the residual) or (b) inventing a curve — both disallowed.

**Falsifiable step if/when formalism is written:** run the phonon-Hawking / finite-core radiation entropy vs Page time and either produce a Page-like turn or a named kill. That is **OPEN-THEORY mechanism debt**, not a one-script census.

---

## 4. Non-claims

Do **not** claim from this residual or from “coefficient paid”:

1. **That the Page curve has been computed or closed** — explicitly open; un-run.  
2. **That coefficient payment *is* the Page curve** — payment removes an area-law *block*; curve is a separate dynamical object.  
3. **An island formula, replica wormholes, or holographic Page-curve derivation under PRTOE** — not delivered in the surveyed files.  
4. **That structural dissolution of the information paradox equals a quantitative Page-curve result** — file itself: “dissolution, not a calculation.”  
5. **Firewall / AMPS resolution as a numerical curve** — structural (sonic horizon + medium correlations); not a plotted \(S_\mathrm{rad}\).  
6. **Roster “candidate grade” as unconditional** — gauge sector still rides named edge-mode commitment E; kill if edge-mode entropy is rejected.  
7. **Re-opening docket #92/#107 or the O(1) entanglement check as live gates** on the curve — status lock: do not re-open (i)/(i′) as if they still gate half (ii).  
8. **Any new radiation-entropy number, Page-time formula, or plot produced in this session** — none; inventory only.

---

## Sources walked (this run)

| path | role |
|---|---|
| `docs/PRTOE_information_paradox.md` | ingredient table; curve open; status lock |
| `docs/PRTOE_entropy.md` §3, §5 | coefficient + roster paid; dynamics open |
| `docs/PRTOE_quantum_gravity.md` §4a | \(12\pi/48\pi=1/4\); structural O(1) |
| `docs/PRTOE_no_singularities.md` §5 | coefficient payment unblocks curve *block*, not computation |
| `docs/working_logs/_PROJECT_FINISH_ROADMAP.md` | OPEN-THEORY wording |
| `docs/working_logs/_FILE_COMPLETION_STATUS.md` | COMPLETE-CONDITIONAL; curve OPEN |
| `docs/working_logs/SCIENCE_DEBTS_2026-08-03.md` | mislabeled “coefficient” row (hygiene) |
| `docs/working_logs/_DOCKET_INDEX.md` | #92, #107 closed |
| `scripts/area_law_roster_extension.py` | paid roster instrument only |

**Artifacts this run:** this `REPORT.md` only. No new script, no curve data.

**Debt status after inventory:** OPEN-THEORY residual unchanged — **curve dynamics open; coefficient paid; no fake-complete.**
