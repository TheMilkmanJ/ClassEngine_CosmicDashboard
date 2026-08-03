# B1 hydrodynamic crown — status (2026-07-31)

## Grade: **PARTIAL — field-roll numbers closed; hydro crown not closed**

**Scope rule for this pass:** push only what existing solvers already force.
Do **not** claim the full inverse problem, pour→release dynamics, or first-principles winding n without a bounce/geometry closure.

| object | status | source |
|---|---|---|
| **Ψ₀ = 5.0×10¹⁶ GeV** (2.07% M_red) | **DONE** | misalignment abundance closure; `genesis_solver_B1.py` / findings |
| **f_amp ≈ 0.63**, band [0.19, 0.87] | **DONE** | Z₄ roll at ε_A=2/9; distributional over θ_i |
| Comoving roll validations (4 half-solvers) | **DONE** | zero-mode, winding channels, comoving ring, abundance |
| **Intake / moment-mapping** (ε_spin, mass share) | **CANDIDATE at comoving grade** | v4 comoving catch-up |
| **L/D discharge band** | **COMPUTABLE, partial co-land** | v1–v3 slug intake; formation-number band [4.3, 5.3] |
| **Flow coherent fraction (H₀ ladder)** | **SIZED DOWN, not full-crown** | v4 H0 field test + failures ledger |
| Widnall n ~ 2.26 R/a | **estimate lands ~11–12** | every ring solver version |
| Pour→release map | **OPEN** | ties bounce / white-hole pour (story-adjacent) |
| First-principles winding n | **OPEN / permanent draw** | Kibble; Γ→n needs melt + bounce sector |

---

## What existing solvers force (numbers)

### Field side (closed for A_s / granule stack)

From `docs/working_logs/genesis_solver_B1_findings.md` and `scripts/genesis_solver_B1.py`:

- **Ψ₀ = 5.0×10¹⁶ GeV** fixed by ρ_DM,0 and m; ∝ m^(−1/4). Roll confirms freeze of ρ·a³; anharmonic O(1) scale-free.
- **f_amp ≈ 0.63** median at recorded tilt; S ≈ 0.57 granule contrast.
- Neither is gated on the hydro crown.

### Ring intake / discharge (partial)

**Toy / static background** (`genesis_solver_v1.py`, `v2.py`):

| χ | L/D | ε (circ. fraction) | share | Widnall n |
|---|---|---|---|---|
| 5.3 | **4.21** | 0.66 | 0.59 | ~11 |
| 6.5 | **5.27** | 0.62 | 0.55 | ~11 |

L/D enters the registered discharge band [4.3, 5.3] for χ ≳ 5.3, but **ε and share do not co-land** the sealed targets (0.88 / 0.843) on the toy background. That is the ledger’s correct toy-grade kill.

**Comoving catch-up** (`genesis_solver_v4_comoving.py`, re-run 2026-07-31):

| χ | ε | share_raw | share_bub (B=1.9) | n | compressive H₀ bias |
|---|---|---|---|---|---|
| 4.00 | 0.965 | 0.900 | 0.945 | ~12 | ~0.03% |
| 4.75 | 0.943 | 0.866 | 0.925 | ~12 | ~0.03% |
| **5.30** | **0.922** | **0.839** | 0.908 | ~12 | ~0.03% |

At χ = 5.3: **share_raw = 0.839 vs target 0.843** (moment-mapping resurrected at comoving grade — Dependency Tree / Failures Ledger). ε sits **0.922 vs 0.88** (closer than toy, not exact). Full four-target co-land at one χ remains **not forced**.

Cited lab inputs in v3 (overpressure 1.35±0.07, bubble B=1.9±0.8, a/D=0.15±0.05) are **external closures**, not first-principles medium outputs — report with that fence.

### Flow coherent fraction (what v4 forces)

v4 H0 field test (not assumed):

1. Tangential swirl is **divergence-free** → monopole ladder bias **exactly 0**.
2. Uniform drift is pure dipole → SH0ES-marginalized.
3. Compressive tail bias ~ **0.03%** at the operating point — **not** the ~1% full-coherence lever in `flow_ladder_correction.py`’s face-value line.

Failures ledger already records the ~1.4% partial lever as **retracted at comoving-field fidelity** (coherent fraction measures ~0.02, not ~1). **What is forced:** the production coherent fraction is small; the H₀ remainder is not a full-coherence swirl fix. **What is not forced:** a single production number for “the” coherent fraction of our universe’s ring (still draw/geometry dependent).

### Winding n

- Solvers can **define** and carry integer winding (`genesis_multicomponent`, joint draw, B1 ring).
- Widnall band n ~ 11–25 from aspect ratio is an **estimate** that lands every version.
- **First-principles n for our universe** remains a genesis draw (Kibble). Mechanical Γ→n needs melt freeze-out and bounce-sector geometry — **out of scope** without bounce. Do not claim n derived.

---

## What CODE_MANIFEST B1 still owes (honest open list)

From `PRTOE_CODE_MANIFEST.md` B1 crown row:

| feed | forced now? |
|---|---|
| ε + mass share (one intake curve, two moments) | **candidate** at comoving grade; not production-inverse |
| discharge band L/D 4.3–5.3 | L/D **computable**; co-land with ε/share **partial** |
| n’s aspect ratio | Widnall estimate only |
| flow’s coherent fraction | **small** (~0.02 class), not full crown sizing |
| H₀ remainder | not delivered by full-coherence ladder |
| pour→release / full inverse (Γ, impulse, E, α(T/T_c) → field) | **OPEN** |

---

## Audience language (use this)

> Genesis **Ψ₀** and **f_amp** are delivered as numbers from the comoving Affleck–Dine roll and the misalignment abundance closure. The **hydrodynamic crown** (pour geometry, discharge co-land, production coherent fraction, first-principles n) is **still open** and is **not** required for the A_s / ε stack claims closed elsewhere. Moment-mapping (ε_spin / mass share) is a **comoving-grade candidate**, not a finished inverse problem. Do not claim “B1 done” or first-principles winding n without bounce.

## Do not claim

- Full inverse problem closed
- First-principles n from ring solvers alone
- Pour→release derived
- Full-coherence H₀ ladder (~1%) as live production lever
- That toy v1–v3 co-land failures were wrong (they were correct at toy grade)

## Scripts

| script | role |
|---|---|
| `scripts/genesis_solver_B1.py` | Ψ₀ / f_amp comoving roll |
| `scripts/genesis_solver_v2.py` | impulse-derived R(t), L/D |
| `scripts/genesis_solver_v4_comoving.py` | comoving catch-up + H0 channels |
| `scripts/flow_ladder_correction.py` | comparison-layer ω₀ (coherent fraction still a parameter) |
| `scripts/genesis_joint_draw.py` | coherent fraction |⟨e^{iθ}⟩| definition |

Findings parent: `docs/working_logs/genesis_solver_B1_findings.md`
