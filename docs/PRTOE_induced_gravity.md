# Induced gravity of the cosmic medium (expansion attach)

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*

*Status: **derived-conditional** — str[k₁]=0 finiteness + area-law ratio; residuals named; not a TOE.
**PRTOE = Theory of Expansion**, not a Theory of Everything.
**Page curve OPEN** (`page_curve_claimed: false`). **Goal B residuals OPEN** (absolute SI \(G\),
nonlinear Einstein continuum, Page dynamics). Honesty stamp 2026-08-04:
[qg_goalB_honesty_20260804/REPORT.md](working_logs/_runs/qg_goalB_honesty_20260804/REPORT.md).
**Absolute SI \(G\) remains OPEN** — str[k₁]=0 finiteness is paid separately and is **not** an SI-\(G\) value.
Exhaust (T-X3): [`working_logs/_runs/theory_exhaust_20260805/desk/shelf_desk_exhaust/MASTER.md`](working_logs/_runs/theory_exhaust_20260805/desk/shelf_desk_exhaust/MASTER.md).*
**Full QG hub (ontology, dead ends, Page program, Q1–Q7):**  
[PRTOE_quantum_gravity.md](PRTOE_quantum_gravity.md)  
*(shelf-promoted 2026-08-03 for Goal A expansion attach; Page curve OPEN; not TOE; Goal B residuals OPEN).*

---

## 1. Expansion attach (Theory of Expansion — not TOE)

**Fence.** This shelf file attaches only what the expansion medium needs: induced / analog gravity as the seating of the **dark condensate** (dCDF), plus two disk-checkable pieces (area-law *coefficient* as ratio; Pauli finiteness under str[k₁]=0). It is **not** a quantize-the-metric program, not a Page-curve close, and not a certificate that ε / CLASS likelihoods succeed.

### What this file contributes to Expansion

The expansion medium is the **dark condensate** (dCDF superfluid). This file states the standard analog / induced-gravity reading of that medium:

- Spacetime geometry at long wavelength is the **collective hydrodynamics** of the same condensate that sources the cosmic floor and two-era dark fluid — not a separately quantized metric program.
- **Induced / analog gravity** (acoustic metric + Sakharov one-loop stiffness + Jacobson thermodynamic route) is therefore the natural gravity seat for the expansion medium.
- Two **paid, disk-checkable** pieces an outsider can use without accepting full QG ontology: (i) the area-law **coefficient ratio** \(S = A/4G\) as \(12\pi/48\pi\) for minimal scalars; (ii) Pauli finiteness / `str[k₁]=0` positioning (public algebra in the shipped supertrace-note).

**If dCDF + ε is wrong, this file is not an expansion test** — it only seats gravity for the medium the expansion model already assumes.

### Expansion parents only (attach graph)

Cross-link the expansion-facing parents — **not** the quantum-trio / measurement-problem wing:

| Parent | Role for attach |
|---|---|
| [PRTOE_dcdf_superfluid.md](PRTOE_dcdf_superfluid.md) | The condensate that *is* the expansion medium |
| [PRTOE_cosmological_constant.md](PRTOE_cosmological_constant.md) | Vacuum-energy floor / DE scale from medium occupancy |
| [PRTOE_LV_pricing.md](PRTOE_LV_pricing.md) | Preferred-frame / Weinberg–Witten escape priced for matter |
| [PRTOE_stability.md](PRTOE_stability.md) | Ghost / gradient / \(c_T=1\) certificates for the running medium |

Related exploratory (not required for Goal A attach): [PRTOE_entropy.md](exploratory/PRTOE_entropy.md) (roster extension of the quarter).

Public algebra: [docs/arXivReady/supertrace-note.pdf](arXivReady/supertrace-note.pdf) (Zenodo-shipped). Full QG hub stays **CORPUS_ONLY**.

### Outsider recompute (one command + optional finiteness)

From repo root:

```bash
OMP_NUM_THREADS=1 nice -n 19 python3 scripts/quantum_area_law_quarter.py
```

**Expected:** exit 0; stdout reports ratio arithmetic **PASS** with \(12\pi/48\pi = 1/4\) exactly (and a numerical cancel demo at the same quarter). Artifact rewrite: `docs/working_logs/_runs/quantum_null_hardening_20260803/AREA_LAW_QUARTER.md`.

Optional supertrace check (finiteness algebra only — **not** absolute SI \(G\); not the area-law script):

```bash
OMP_NUM_THREADS=1 nice -n 19 python3 scripts/supertrace_k1_verify.py
```

Public [supertrace-note.pdf](arXivReady/supertrace-note.pdf). Full recipe: [OUTSIDER_RECOMPUTE.md](working_logs/_runs/qg_goalA_20260803/OUTSIDER_RECOMPUTE.md). Honesty recompute stamp: [qg_goalB_honesty_20260804/REPORT.md](working_logs/_runs/qg_goalB_honesty_20260804/REPORT.md).
---

## 2. The claim, stated precisely (trimmed)

Spacetime geometry is the long-wavelength collective description of a cosmological superfluid condensate, and the condensate is a quantum system from the outset. Gravity is therefore quantum *by inheritance* — in the same sense that the hydrodynamics of superfluid helium requires no independent quantization once the underlying atoms are quantum. This is the standard analog-gravity position (Volovik; Barceló–Liberati–Visser), here assembled with the model's field content and pushed to a quantitative endpoint: **a closed one-loop expression for Newton's constant under Pauli finiteness (str[k₁]=0), with named residual conditions** (conformally coupled Higgs; medium mass spectrum / portal / lattice for absolute \(G\)).

This shelf does **not** lead with “there is no quantize-gravity problem” as ontology slogan; that framing and the full quantum-inheritance narrative live in the [full QG hub](PRTOE_quantum_gravity.md).

---

## 3. Three routes to the emergent metric (short)

Three independent constructions seat the same effective metric:

1. **Acoustic metric.** Low-energy excitations of the condensate propagate on an effective geometry \(g_{\mu\nu}\) built from density and flow (phase-EFT isomorphism). Horizons are sonic horizons.
2. **Sakharov induction** [Sakharov 1967]. The Einstein–Hilbert term is generated by one-loop fluctuations of the fields living in the condensate; gravitational stiffness is a calculable output. §5 carries the closed form under Pauli’s scheme.
3. **Thermodynamic route** [Jacobson 1995]. Einstein’s equations follow as an equation of state from \(\delta Q = T\,dS\) on local horizons; the area-law *coefficient* used as input is paid as a ratio in §4.

Full route depth, multimessenger inheritance, and obstruction stack: [full QG hub](PRTOE_quantum_gravity.md) §§2–4.

---

## 4. Area-law coefficient as ratio (Bekenstein quarter)

The Bekenstein quarter is not “one number short.” It is the ratio of two heat-kernel coefficients, same cutoff \(\varepsilon\), per massless scalar:

| quantity | coefficient |
|---|---|
| induced Newton constant (Sakharov–Visser) | \(1/G = N/(12\pi\,\varepsilon^2)\) |
| horizon entanglement entropy ('t Hooft, heat-kernel) | \(S = N\cdot A/(48\pi\,\varepsilon^2)\) |

> **\(S / (A/G) = 12\pi/48\pi = 1/4\) exactly ⟹ \(S = A/4G\)**

Both sides carry \(N/\varepsilon^2\) identically, so species count and cutoff cancel — the ratio is universal for the field content those coefficients assume (minimally coupled scalars).

**What the medium contributes.** The two coefficients are standard results. What the medium supplies is a **physical** regulator (condensate Bogoliubov coherence factors) rather than a bookkeeping one, so the same \(\varepsilon\) regulates both sides. A conical deficit puts a delta in the Ricci scalar on the entangling surface, so the *area* term in the conical heat kernel **is** the *R* term that generates \(1/G\) (Frolov–Fursaev–Zelnikov). Thus

> **O(1)\(_\mathrm{entanglement}\) = O(1)\(_\mathrm{induced\text{-}G}\) identically, for any form factor** — the quarter is regulator-independent, not merely regulator-consistent.

**Honesty on “O(1) = 1.0000”.** The p-ramp on the induced-G side — O(1) = 2.0 / 1.0 / 0.5 at Bogoliubov softening \(p = 1.5/2/3\) — cancels in the ratio. **“O(1) = 1.0000” is the \(p=2\) point of a ramp, not a prediction of the medium.** What earns the quarter is the shared-coefficient structure.

**Roster extension** (spin-½ preserves the ratio; gauge fields need edge modes; conformal scalar drops out on both sides) is **candidate grade** — see [PRTOE_entropy.md](exploratory/PRTOE_entropy.md) §3. Do not import that file’s deep dive here.

**Do not read this section as a Page-curve close.** Coefficient paid ≠ dynamical Page curve (Q6 **OPEN**). Instrument near-miss (coevolve_v13 T8 early residual) is **not** a Goal A product and is **not** claimed here.

### Goal B residuals (not this file’s job)

| Residual | Status on thin attach |
|---|---|
| Page dynamics (Q6) | **OPEN** — live only on full hub + Page instruments; `page_curve_claimed: false` |
| Absolute SI \(G\) | **OPEN** (permanent under stocked desk) — mass-scale half (ρ*/portal/lattice); closed-form \(1/G\) under str[k₁]=0 is finiteness, not SI prediction · exhaust T-X3 |
| Nonlinear continuum Einstein | **OPEN-THEORY** — not claimed on expansion attach |

Goal A outsider check (re-run 2026-08-04): `python3 scripts/quantum_area_law_quarter.py` → **PASS**.  
Full residual register: [PRTOE_quantum_gravity.md](PRTOE_quantum_gravity.md) § Research residual register.

---

## 5. Finiteness / Pauli scheme (condensed)

**5.1 Physical regulator (stands).** In a condensate the regulator is a property of the medium. Mode contributions are weighted by Bogoliubov coherence factors; the regulated one-loop coefficient equals the naive value at the \(p=2\) ramp point (see §4 honesty).

**5.2 Species sum.** Gravity reads energy, not identity. Heat-kernel weights: fermions +1 per Weyl; gauge bosons −4 each; real scalars \((1/6 - \xi)\).

| sector | content | contribution |
|---|---|---|
| **visible** — fermions | 48 Weyl (3 gen × 16, **including three right-handed neutrinos**) | **+48** |
| **visible** — gauge | 12 gauge bosons | **−48** |
| | *visible subtotal* | ***0 — exactly*** |
| **scalar** | 4 real Higgs, \(4(1/6 - \xi_H)\) | **0 iff \(\xi_H = 1/6\)** *(conditional)* |
| **dark** — fermions / gauge | \(N_f\times N_c\times 2\) Weyl vs \((N_c^2-1)\) bosons × (−4) | **0 each** *(candidate — P-2026-048; \(N_c=2\), \(N_f=3\))* |
| | **Total** | **0** under named conditions |

Visible balance stands independently of the dark candidate rows. Dark roster fixed by requiring str[k₁]\(_\mathrm{dark}\)=0 alone is **P-2026-048** (candidate; lattice \(T_c/\sqrt{\sigma}\) for SU(2), \(N_f=3\)).

**5.3 Pauli’s finiteness condition.** The vanishing quantity, str[k₁], is Pauli’s compensation program on the induced Newton constant [Visser 2002, Eq. 35]: if str[k₁]=0, the one-loop contribution to \(G\) is finite and scale-independent — *strong constraints on particle content*.

> **Correct statement of the claim.** Setting str[k₁]=0 switches off the leading Sakharov \(\kappa^2\) term. **The claim is not that this field content induces gravity at quadratic order. It is that for SM content plus three right-handed neutrinos and a conformally coupled Higgs, the one-loop matter correction to Newton’s constant is finite** — so \(G\) can be a genuine tree-level constant rather than fine-tuned against a Planck-scale divergence. Naturalness about \(G\), not induction-at-leading-order.

**Units (do not break a referee check).** For SM alone, str[k₁] = **−1/2** in Visser’s normalisation (Weyl deficit −3; \((-3)/6 = -1/2\)). Balance: \(N_{1/2} = 4N_1\), i.e. \(48 = 4\times 12\). Instrument: `scripts/supertrace_k1_verify.py`.

**Higgs cost.** Full str[k₁]=0 **iff \(\xi_H = 1/6\)** (conformal). That is a **named input**, not measured here — finiteness is **conditional on conformal Higgs coupling**.

**5.4 Formula (Pauli scheme, not Sakharov quadratic).** This framework’s content sets the quadratic coefficient to zero; naive Sakharov closures fail and are recorded in the failures ledger. Surviving expression:

\[
\frac{1}{G} = -\frac{1}{2\pi}\,\mathrm{str}\!\left[k_1\cdot m^2\cdot\ln(m^2/\mu^2)\right]
\]

**5.5 Gravity from the medium.** With the cutoff gone, \(G\) is fixed by the mass spectrum. The visible sector contributes negligibly (quadratic cancel + light masses). What remains are the medium’s collective modes at the basement scale: **gravity is induced by the medium, and by nothing else** — as a framework claim with residual below.

**5.6 Open residual (not claimed closed).** Absolute SI \(G\) requires the medium’s collective-mode masses to sit at the Planck scale within O(1) — match-or-die, computable from condensate parameters, **not paid on this shelf**. Value of \(G\) is **not claimed**; see [PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md) (“The G-closure”) and the [full QG hub](PRTOE_quantum_gravity.md) §5.

---

## 6. What this file owns / does not claim (Goal A)

**Owns**

- Induced / analog gravity as the **expansion-medium seating** of geometry (acoustic + Sakharov + Jacobson).
- Area-law **coefficient** \(S=A/4G\) as heat-kernel ratio \(12\pi/48\pi\) for minimal scalars (species + cutoff cancel).
- **Finiteness condition** str[k₁]=0 for SM + 3ν_R (visible), with conformal-Higgs condition and candidate dark balance named.
- Named residuals: lattice/portal for dark roster and absolute-\(G\) mass scale; p-ramp honesty on O(1).

**Does not claim (non-negotiable)**

| Non-claim | Status |
|---|---|
| Dynamical **Page curve** (Hawking radiation entropy dynamics) | **OPEN** — scaffold only; coefficient ratio ≠ Page dynamics |
| Full **TOE** / local bound-matter completion | Out of scope — Theory of Expansion; SM + open quantum wing |
| That **ε / CLASS likelihoods** succeed | Expansion tests live elsewhere; this file does not certify them |
| Absolute SI **G** from the medium mass spectrum | Residual (ρ\*/portal/lattice) — named, not closed |
| Nonlinear continuum Einstein / continuum limit | OPEN-THEORY residual |
| Measurement problem / Tsirelson / superquantum mods | Not this file; quantum wing |

**Do not read the area-law quarter as a Page-curve close.** Q2 paid ≠ Q6 paid.

---

## 7. Thin claims ledger (Goal A)

| # | Claim | Grade | Code / artifact | Residual / kill |
|---|---|---|---|---|
| Q2 | Area-law coefficient \(S=A/4G\) as heat-kernel ratio \(12\pi/48\pi\) | **paid** (minimal scalars) | `scripts/quantum_area_law_quarter.py` PASS | Roster extension candidate ([exploratory/PRTOE_entropy.md](exploratory/PRTOE_entropy.md) §3) |
| Q3 | Species + cutoff cancel in the ratio | **paid** | same | — |
| Q4 | Visible str[k₁]=0 with SM+3 ν_R; dark balance → P-2026-048 | **derived + candidate dark** | [supertrace-note.pdf](arXivReady/supertrace-note.pdf); `scripts/supertrace_k1_verify.py` | Lattice \(T_c/\sqrt{\sigma}\) kills portal chain |
| Q5 | “O(1)=1.0000” is \(p=2\) ramp point, not medium selection | **honest constraint** | §4 | Do not quote as prediction |
| Q6 | Dynamical Page curve (phonon Hawking / finite core) | **OPEN** — **`page_curve_claimed: false`** | full hub + scaffold only | **Forbidden to close from Q2 alone**; Q2 ≠ Q6 |
| Q7 | Tsirelson / no superquantum gravity-side mods | **null** (quantum wing) | full hub / quantum wing | not Goal A; CHSH > 2√2 kills |

Framework seating (emergent metric assembly) is **Q1** in the full hub — pointer only here; not a separate paid expansion test.

**Ledger hygiene:** Q2/Q3 paid (coefficient + cancel) does **not** pay Q6. Q4 pays finiteness algebra, **not** absolute SI \(G\).

---

## 8. Residual freeze (Goal B residuals; non-blockers for Goal A)

**Honesty fence (2026-08-04):** same Goal B inventory as the full hub residual register.
This thin file **does not own** these residuals and **does not close** them. `page_curve_claimed`
stays **false**.

| Residual | Grade | Evidence path | Blocks Goal A? | **Forbidden to claim** |
|---|---|---|---|---|
| Dynamical Page curve (Q6) | **OPEN** | full hub Q6; scaffold only; `page_curve_claimed: false` | **No** | Page closed; coefficient = curve |
| Absolute SI \(G\) | **OPEN** | §5.6; failures ledger G-closure; supertrace ≠ value; exhaust T-X3 | **No** | SI \(G\) derived from supertrace alone |
| Nonlinear continuum Einstein | **OPEN-THEORY** | full hub §4 nonlinear row; not paid here | **No** | full nonlinear Einstein continuum closed |
| Dark roster lattice (P-2026-048) | **candidate** | full hub §5.2; lattice \(T_c/\sqrt{\sigma}\) | Named | lattice paid without ensemble |
| Conformal Higgs \(\xi_H=1/6\) | **named condition** | §5.3 | Finiteness conditional | finiteness unconditional |

**Promotion of this thin shelf never requires Page.** Scaffold / program notes stay in working_logs and the full hub only.

---

## 9. Pointers

| Object | Path |
|---|---|
| **Full QG hub** (routes, §3 inheritance, full obstruction stack, dead ends, Navarro-Salas, Q1–Q7, Page program) | [PRTOE_quantum_gravity.md](PRTOE_quantum_gravity.md) (shelf-promoted 2026-08-03; Page OPEN) |
| Entropy / roster extension | [docs/exploratory/PRTOE_entropy.md](exploratory/PRTOE_entropy.md) §3 |
| Public algebra (supertrace) | [docs/arXivReady/supertrace-note.pdf](arXivReady/supertrace-note.pdf) |
| G-closure obituary | [PRTOE_FAILURES_LEDGER.md](PRTOE_FAILURES_LEDGER.md) |
| Fence | [TOE_EXPANSION_SHELF_FENCE_20260803.md](working_logs/TOE_EXPANSION_SHELF_FENCE_20260803.md) |
| Goal A attach / DoD | [ATTACH_STATEMENT.md](working_logs/_runs/qg_goalA_20260803/ATTACH_STATEMENT.md), [THIN_SHELF_PROPOSAL.md](working_logs/_runs/qg_goalA_20260803/THIN_SHELF_PROPOSAL.md) |

### Thin references

[Sakharov 1967]; [Jacobson 1995]; [Bekenstein 1973; Hawking 1975]; [FFZ 1997] Frolov–Fursaev–Zelnikov; [Visser 2002] gr-qc/0204062; Volovik; Barceló–Liberati–Visser. Full entries: [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md).

---

*Theory of Expansion attach only. Page curve remains **OPEN**. Not a TOE.*

---

## arXiv / extract stance (IG-D3, 2026-08-03)

**No unique paper extract** from this thin file (red **NO**): substance is supertrace (SHIPPED)
plus the full hub framing. Keep as Expansion corpus only.  
Worklist: [`working_logs/_runs/quantum_arxiv_worklist_20260803/`](working_logs/_runs/quantum_arxiv_worklist_20260803/).

**Residuals (same as hub Goal B):** Page OPEN (`page_curve_claimed: false`); SI \(G\) OPEN;
continuum Einstein OPEN. This thin file does not own them and does not close them.
Honesty stamp: [`qg_goalB_honesty_20260804/REPORT.md`](working_logs/_runs/qg_goalB_honesty_20260804/REPORT.md).