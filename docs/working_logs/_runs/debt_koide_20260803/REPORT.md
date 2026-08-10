> **SUPERSEDE / GRADE (2026-08-03):** Tribunal R2 — blue lane **(c)**.
> Thermal delivery law excluded at **1025 ppm / ~171×** (`koide_delivery_law_discriminator.log`).
> Do not forward-file "candidate mechanism" for the thermal/flat path. Relation Q=2/3 stands;
> mechanism exactness **OPEN as unexplained regularity** pending freeze-time/Wilson residual only.

# Debt attack: Koide #101 / #102 (node + Brannen phase)

**Date:** 2026-08-03  
**Worker:** blue-team science (Grok Build subagent)  
**Scope:** open science debt on the graded null (#101) and Brannen phase (#102) — honest attack only.  
**Hard rules observed:** no PolyChord, no new MCMC, `chains/` untouched, no process kills, no false closures.  
**Sources of truth:**  
- [`docs/working_logs/T6_koide_desk_status.md`](../../T6_koide_desk_status.md)  
- [`docs/working_logs/T6_koide_owed.md`](../../T6_koide_owed.md)  
- [`docs/PRTOE_FAILURES_LEDGER.md`](../../../PRTOE_FAILURES_LEDGER.md) (Koide rows)  
- Existing `scripts/koide_*.py` (re-run only; no new mechanisms invented here)

**Run dir:** `docs/working_logs/_runs/debt_koide_20260803/`  
All script stdout captured as `*.log` in this directory.

---

## 1. Current desk status (what is ruled out / still open)

### Paid / closed (desk arithmetic & classification — not mechanism)

| Item | Grade | Status |
|---|---|---|
| Protection half (multiplicative portal → Q invariant) | **PAID** | Non-universal electron-only shift moves Q by ~163 ppm vs fence 6.8×10⁻⁶ |
| Fence / Q arithmetic | **PAID** | Q = 0.6666605 ± 6.8×10⁻⁶; A = 1.414200; three m_τ targets share +0.91σ displacement |
| Equal-stiffness rewrite | **PAID** | A = √2 · (R_c/M_c); residual is R_c = M_c as VEVs |
| #101 structure rewrite | **PAID as classification** | Q=2/3 ⟺ graded null f₀² − \|f₁\|² − \|f₂\|² = 0 |
| #79 magnitude | **CLOSED into #101** | \|f₁/f₀\| = 1/√2, τ = ½ln2 forced by two charged legs on the null |
| #102 arithmetic / m_τ table | **PAID as measurement table** | θ_B = +0.2222296, δθ = +7.409×10⁻⁶; until ~1.4 ppm m_τ, Q=2/3 vs θ_B=2/9 vs closure are one curve |
| Kernel desk chain (KMS / holonomy form) | **PAID as structure IF null sourced** | 3·θ_B = Q as second condition (lepton-specific) |

### Ruled out (ledger / T6 — do not re-open without new premises)

| Candidate | Kill |
|---|---|
| Three-draw / thermal selector for exact Q=2/3 | E[Q]=1/2, Var=1/60 closed form; odds of lepton landing ~1.1×10⁻⁵; deterministic Exp reps all miss 2/3 |
| Medium-w inheritance (spectator inherits K=2V) | Category error: medium EoS ≠ field EoS |
| SOC attractor for A=√2 | Premise false (family regime ≠ measure-zero seam) |
| Wide-seam 2D-Potts for A=√2 | Broad critical region cannot explain 10⁻⁵ landing; category error on “two faces” |
| Single-potential / statistical routes (quartic virial, equipartition, GBM, log gas, …) | Retired as a class |
| Natural Z₃ cubic V ⊃ −g Σφ³ | Free min at A=2 (axis vacuum) — fights Koide |
| ⟨a³⟩=5/9 phase rational | Killed at 4.5σ once τ-error attached |
| Golden-angle phase | Killed at thousands of σ the hour it was raised |
| Criticality A = A_max(φ) as second equation (equality) | Joint solve → Q* = 0.689433, **3349σ** from measured Q (as *ceiling* Q ≤ 0.689 the bound survives) |
| Virial ring direction for #101 null | Shape sector soft: k_E = −(3/2)α_d ≤ 0; retired |
| C3 triple-point node as *value* source for null/phase | **Re-confirmed this run:** node is b=0 → Q=1/3; null is \|b\|/a = 1/√2 — permits structure, does not force values |
| Ring-internal potential as phase source | **Re-confirmed:** φ flat at all Z₃-symmetric quadratic order; cubic only through cos(3φ), stationary at 3φ∈{0,π}, misses 3φ=Q by ~0.667 rad |
| Neutrino cone (Q_ν→2/3) | Negative structural fact: Q_ν ≈ 0.458; cone is charged-lepton-specific |

### Still open (theory-grade — **not desk-closeable**)

| Item | Docket | What would close it |
|---|---|---|
| **#101 — what enforces the null exactly** | node / constraint / index / conservation | Mechanism forcing f₀² = \|f₁\|²+\|f₂\|² to ~10⁻⁵ without equilibrium scatter |
| **#102 — phase source (Brannen 2/9)** | same residual as #101 | 2/9 = holonomy Q/3 around the cone; **not independently sourced**; closes with the node or not at all |
| Democratic-graph candidate for Q | basement (P1–P4) | Especially (P1) condensate-as-node and (P4) equal quanta / delivery law |
| Occupancy lock N₀=1 | candidate only | Algebra exact *if* N₀=1 applied to ring cell; application is the invented step |
| R_c = M_c / delivery-law fork | lock-6 / #85 | Which freeze law converts amplitudes to the null without 1025 ppm thermal distortion |
| c_K keystone path | downstream | c_K · τ = Q collapses sector *if* c_K is independently derived — not shown |

### One-line board (unchanged after this attack)

**Protection and arithmetic paid. #101/#102 remain one theory-grade node residual (exact null + holonomy). OPEN-THEORY stands. Nothing in this run closes either docket.**

---

## 2. Scripts run + outcomes

All runs: `nice -n 19 python3 scripts/<name>.py`, wall time ≪ 5 min each, exit code 0 unless noted. Logs: this directory.

| Script | Exit | Outcome (honest) |
|---|---:|---|
| `koide_triple_point_node.py` | 0 | Circulant H = aI + bP + b*P² seats leptons exactly (sq-err ~1e−8). **b=0 → Q=1/3** (node); **\|b\|/a=1/√2 → Q=2/3** (null). Positivity wall: A_max≈1.4737; A=√2 is **96.0%** of wall — near, not on. **VERDICT: node delivers structure + 2 knobs, not the knob values.** ALL CHECKS PASS |
| `koide_phase_is_a_flat_direction.py` | 0 | Democratic Hessian leaves doublet degenerate; E(φ) and Q(φ) constant to ~1e−15 while mass fractions swing. Complex bond still leaves φ flat for real ring field. Cubic sees only cos(3φ); natural extrema miss 3φ=Q. **VERDICT: Q-debt and phase-debt differ in kind; ring-internal candidates for phase retired at every order.** |
| `koide_node_vs_backdrop.py` | 0 | Discriminant exists: spectrum {3a+b, 3a+b, 4b}, threefold degeneracy **iff a=b**. Node vs backdrop not the same physics. **#1 stays OPEN** — model-building (stiffness threefold-degenerate before pinning), not desk. 18/18 checks |
| `koide_democratic_graph_null.py` | 0 | From (P1)–(P4) derives a=b → R_c=M_c → Q=2/3 exact, N=3 special. **Assumptions named, not paid.** Live weakness: (P4) equal quanta and (P2) democratic coupling |
| `koide_null_occupancy_lock.py` | 0 | N₀=1 ⇒ f₀²=\|f₁\|²+\|f₂\|² at every Mω₁; Q=2/3 exact algebraically. **Candidate**, invented step flagged (apply occupancy to ring cell). Not promoted |
| `koide_lock_algebra_verification.py` | 0 | a=3b ⟺ ρ²=1/2; occupancy books exact; ω₁=(2/9)T_c=39.356 keV. Algebra holds; physics residuals (why equipartition / why one quantum) open |
| `koide_lock_pressure_test.py` | 0 | Six attacks: 5 survive / 1 sharpens; residual L2 (value of conserved amplitude). Neutrino check Q_ν off-balance as required |
| `koide_null_sum_rule_check.py` | 0 | m₁(0)=0 identically (neutral conserved). Sum rule **protects neutral seat**, does **not** force a=3b. Split verdict as T6 records |
| `koide_null_stiffness_reduction.py` | 0 | Q=2/3 ⟺ a=3b on Z₃ ring (thermal frame). Renames target; does not close exactness |
| `koide_frame_bridge.py` | 0 | Fourier normalizations paid; they cancel from stiffness ratios. Frames separated by **delivery law**, not bookkeeping. Geometric ring ceiling eps_D/eps_S < 3/4 on convex branch; thermal null needs 2 |
| `koide_delivery_law_discriminator.py` | 0 | Thermal law distorts Q by **1025 ppm** vs 6 ppm budget at corpus ω₁. Occupancy/cold law still live alternative. Classical equipartition under pressure |
| `koide_equal_quanta_from_adiabaticity.py` | 0 | Adiabatic ramp from degenerate stage delivers null numerically (integrator converges). Reduces (P4) to assembly order + adiabaticity — still needs freeze timescale from corpus |
| `koide_KV_identification.py` | 0 | Graph supplies background vs fluctuation as two bond types. Equal-coefficient K~R², V~M² **not** supplied by graph stiffnesses (ratio 4). Debt sharpened, not paid |
| `koide_3body_test.py` | 0 | A=1.41420, Q=0.66666, CV≈1; electron 2.27° from massless wall. Exact masslessness misses m_τ/m_μ by ~17%. √2 re-read as σ=μ, not derived |
| `koide_watch_triangle.py` | 0 | Light-mass conjunction of A=√2 + φ=2/9 + closure fails at **~0.17 ppm (A) / ~0.79 ppm (φ)** — 452σ on m_μ/m_e precision, not on sector physics. τ (±0.12 MeV) hides the triangle (~55× wider). External m_τ refine still required to separate watches |

### Aggregate

- **15/15 scripts completed successfully** under the time budget.  
- **No new null mechanism discovered.**  
- **No new phase source discovered.**  
- Re-runs **reproduce and harden** prior negative results on the node and on ring-internal phase candidates.

---

## 3. Sharpest falsifiable NEXT compute

**Branch A Wilson-line electric holonomy, zero free parameters, three discrete outcomes.**  
The phase is unreachable from any real Z₃-symmetric ring potential (re-confirmed: φ flat at quadratic order; cubic extrema at 3φ ∈ {0, π} miss 3φ = Q by ~0.667 rad). The corpus already names one tractable external route: treat arg b as a **Wilson-line electric holonomy** of the dark SU(2) gauge field in the recorded winding background (non-center, so it *can* be non-quantized — which 2/9 requires). Write a single bounded script that (i) takes only corpus-fixed inputs (winding number / background geometry, no fit to lepton masses), (ii) evaluates the holonomy angle around the family-cycle, and (iii) scores three pre-committed bins: **hits 2/9**, **hits a sibling 2/9 ± 2π/3**, or **lands elsewhere**. A hit crowns Branch A for #102 and, via the holonomy closure 3·arg f₁ = Q, feeds the backward read that turns A=√2 into an *output* (if and only if the null is already enforced). A sibling lands means the mechanism selects the wrong Z₃ sheet. Anywhere else kills Branch A for this debt. Do **not** stack dim(adj SU(2))=3 as a generation-count claim against Pauli str[k₁]=0 (adjudicate, never stack). Do **not** claim #101 closed by a phase hit alone — the null still needs its own exactness source. Three-seed and pure c_K routes remain blocked on missing couplings / underived c_K and are not this next step.

---

## 4. Explicit non-claims

This run does **not** claim:

1. That **#101 is closed.** The graded null is *classified* (constraint/index/conservation aisle); it is not *sourced*.  
2. That **#102 is closed.** Brannen θ_B ≈ 2/9 is a measurement-table fact and a holonomy *form*; it has no independent mechanism.  
3. That the **C3 triple-point node derives Q=2/3 or 2/9.** It derives the Brannen parameter count only.  
4. That the **democratic graph is proven.** It is a candidate conditional on (P1)–(P4), with (P1) and (P4) open.  
5. That the **occupancy lock is promoted.** Algebra exact under N₀=1; application to the ring cell is invented and flagged.  
6. That **thermal / equipartition** can deliver 6.8×10⁻⁶ exactness. Discriminator: 1025 ppm vs 6 ppm budget.  
7. That **criticality** is the sector’s second equation. Equality killed at 3349σ; inequality ceiling only.  
8. That **A=√2 is derived from first principles.** It remains measured / conditional on null or R_c=M_c.  
9. That **neutrinos obey the same cone.** They do not (structural, per-sector).  
10. That **OPEN-THEORY is complete.** Desk status board still stands: OPEN-THEORY.  
11. That light-mass **triangle tension** falsifies the sector. It is a sub-ppm conjunction failure hidden by τ-error; physics vs precision must not be confused.  
12. That **Branch A, three seeds, or c_K** has been computed here — only named as next / blocked paths.  
13. Any **MCMC / PolyChord / chain** result. None run.  
14. That re-running scripts **moves the debt** — re-confirmation of negatives is not progress toward closure.

---

## Appendix A — key numbers re-confirmed this run

| Quantity | Value | Notes |
|---|---|---|
| Q (measured) | 0.6666605 ± 6.8×10⁻⁶ | Fence; τ-dominated |
| A | 1.41420 (√2 = 1.41421) | 0.0009% |
| θ_B | +0.2222296 rad | δθ = +7.409×10⁻⁶ vs 2/9 |
| Node (b=0) | Q = 1/3 | Threefold degenerate |
| Null (\|b\|/a = 1/√2) | Q = 2/3 | Specific distance *off* node |
| Positivity wall share | A/A_max ≈ 96.0% | Near-maximal, not criticality equality |
| Criticality equality Q* | 0.689433 | 3349σ (ledger; not re-derived this run) |
| Thermal delivery distortion | 1025 ppm | vs 6 ppm budget |
| m_τ targets (Q / θ_B / closure) | 1776.969 / 1776.96651 / 1776.96705 MeV | Span 1.42 ppm; measured 1776.86 ± 0.12 |
| Light-mass conjunction miss | ~0.17 ppm (A), ~0.79 ppm (φ) | Hidden by τ until ≲1.4 ppm |

## Appendix B — file inventory this run

```
docs/working_logs/_runs/debt_koide_20260803/
  REPORT.md
  koide_3body_test.log
  koide_KV_identification.log
  koide_delivery_law_discriminator.log
  koide_democratic_graph_null.log
  koide_equal_quanta_from_adiabaticity.log
  koide_frame_bridge.log
  koide_lock_algebra_verification.log
  koide_lock_pressure_test.log
  koide_node_vs_backdrop.log
  koide_null_occupancy_lock.log
  koide_null_stiffness_reduction.log
  koide_null_sum_rule_check.log
  koide_phase_is_a_flat_direction.log
  koide_triple_point_node.log
  koide_watch_triangle.log
```
