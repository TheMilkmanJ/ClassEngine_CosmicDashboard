# Page-curve dynamics — concrete implementation plan (2026-08-03)

**Status:** PLAN ONLY. No curve is computed here.  
**Registered object (still OPEN):** \(S_{\mathrm{rad}}(v)\) vs Page time for phonon Hawking flux off a finite-density sonic-horizon core (healing length \(\xi\)), with unitarity enforced by the core as a finite quantum system.  
**Home claim:** [`docs/PRTOE_information_paradox.md`](../../../PRTOE_information_paradox.md)  
**Scaffold (illustration only):** [`PAGE_CURVE_SCAFFOLD.md`](PAGE_CURVE_SCAFFOLD.md) · `scripts/quantum_page_curve_scaffold.py`  
**Debt inventory:** [`docs/working_logs/_runs/debt_page_curve_20260803/REPORT.md`](../debt_page_curve_20260803/REPORT.md)  
**QG ledger residual Q6:** [`docs/PRTOE_quantum_gravity.md`](../../../PRTOE_quantum_gravity.md) claims ledger  

**Hard rule:** Forbidden to draw a Page curve from \(S=A/4G\) alone. Forbidden to ship the toy \(4v(1-v)\) ansatz as a PRTOE result. Coefficient and roster are **paid**; only dynamics remain.

---

## 0. Why this plan exists

Debt report verdict: **no desk attack surface without new formalism and an instrument.**  
This document specifies that formalism and a four-week build path so the residual is no longer “vague hard work” but a sequence of falsifiable milestones. First honest success is **not** a Page turn — it is thermal flux + temperature from a sonic horizon (Unruh-class bookkeeping). The Page turn is weeks 3–4, and it may fail.

---

## 1. Minimal viable 1D model (MVP)

### 1.1 Physics picture (what we actually simulate)

| Layer | Role | 1D reduction |
|---|---|---|
| Condensate exterior | Acoustic metric; phonon EFT | Stationary or slowly evolving background flow \(v(x)\), sound speed \(c_s(x)\) from density \(n(x)\) |
| Sonic horizon | Surface where \(\lvert v\rvert = c_s\) | Single point \(x_h\) (or two for a “black hole + white hole” pair as in lab analogs) |
| Finite core | Landau-broken normal region, size \(\sim\xi\) | Segment \(\lvert x\rvert < x_c\) with \(x_c \sim \xi\); no singularity; unitary finite Hilbert space |
| Radiation | Outgoing phonon modes | Right-moving (or both-moving) continuum modes for \(x > x_h\); frequency bins \(\omega_j\) |

**Healing units** (match existing GP scripts): length in \(\xi\), time in \(t_{\mathrm{heal}} = \xi/c_s\), background density \(n\to 1\) at infinity. Recorded ambient values remain reference only (\(\xi \approx 402\,\mathrm{AU}\), \(c_s=\sqrt{3\alpha}\)); the Page-curve run is **scale-free in healing units**.

### 1.2 Fields and state variables

**Background (classical mean-field):** complex order parameter \(\psi(x,t)\) or Madelung variables
\[
\psi = \sqrt{n}\,e^{i\theta},\qquad
v = \partial_x\theta,\qquad
c_s = \sqrt{n}
\]
(in healing units with \(g=1\), \(m=1\); adjust if a different normalization is chosen, but **one convention for the whole stack**).

**Horizon definition (operational, code-level):**
\[
x_h(t) := \text{outermost } x \text{ with } \lvert v(x,t)\rvert = c_s(x,t)\ \text{and}\ \partial_x(\lvert v\rvert-c_s) \text{ outward-pointing as for a BH}.
\]
Surface gravity (1D acoustic):
\[
\kappa = \frac12\,\partial_x\bigl(c_s^2 - v^2\bigr)\Big|_{x_h}
\quad\Rightarrow\quad
T_H = \frac{\kappa}{2\pi}
\]
(in units \(\hbar=k_B=1\)). This is the Unruh/analog-Hawking temperature used for Milestone A.

**Fluctuations (quantum):** linear phonon / Bogoliubov field \(\delta\psi\) or real density/phase pair \((\delta n,\delta\theta)\) on the fixed (or adiabatically evolving) background. Mode functions \(u_j(x),v_j(x)\) with dispersion from the medium’s Bogoliubov law
\[
\varepsilon(x) = x\sqrt{1+x^2/4},\quad x=k\xi
\]
(already tabulated in `bounce_fa1_transphononic_table.py`).

**Core Hilbert space (finite, unitary):** truncate to \(N_c\) effective modes / qubits representing the normal-phase core. Minimal honest choice for MVP:
- \(N_c\) harmonic oscillators (or spin-\(1/2\) sites) with total Hilbert dimension \(D \le 2^{12}\)–\(2^{14}\) for exact density-matrix evolution, **or** Gaussian (covariance) methods for larger \(N_c\) if pure-state Gaussian is enough.
- Coupling: bilinear or Lindblad-to-unitarily-dilated interaction that exchanges quanta with exterior modes at the horizon (pair creation \(\propto\kappa\)).

**Evaporation bookkeeping variable:**
\[
v \in [0,1] := \frac{E_{\mathrm{rad}}(t)}{E_{\mathrm{core}}(0)+E_{\mathrm{rad}}(0)}
\]
(energy fraction in exterior radiation). Page time is defined as the \(v_*\) where \(S_{\mathrm{rad}}(v)\) peaks if a peak exists.

### 1.3 Grid and numerics (MVP defaults — pre-registered)

| Parameter | MVP default | Notes |
|---|---|---|
| Domain | \(x\in[-L/2,L/2]\), \(L=80\xi\) | Same order as `bounce_m6_rebound_1d.py` |
| Points \(N\) | 1024–2048 | FFT-friendly; resolve \(\xi\) with \(\gtrsim 8\) pts |
| \(\Delta t\) | \(10^{-3}\,t_{\mathrm{heal}}\) | Split-step stable for mild flows |
| Horizon target | \(\lvert v\rvert/c_s \to 1\) at \(x_h \sim 5\)–\(15\,\xi\) | Laval-like or tanh flow profile |
| Core radius | \(x_c \sim 1\)–\(3\,\xi\) | Single quantum system (corpus BH claim) |
| Mode band | \(\omega \in [0.05, 2]\,\kappa\) (and a high-\(k\) guard) | Thermal peak \(\sim\kappa\); UV cutoff \(\sim c_s/\xi\) |
| Exterior entropy | von Neumann of reduced radiation DM, or Gaussian covariance entropy for free fields | Must be stated in script header |

**Background construction options (pick one and freeze for Week 1):**

1. **Prescribed acoustic profile (recommended MVP):** fix \(n(x)\), \(v(x)\) with a sonic point; do **not** require full nonlinear evaporation self-consistency first. Evolve only quantum modes + finite core. Mass loss is a prescribed slow \(x_h(t)\) or \(\kappa(t)\).
2. **Self-consistent GP:** evolve \(\psi\) with `bounce_m6_*` split-step; measure \(x_h(t)\), \(\kappa(t)\) from the flow. Harder; schedule after thermal flux works.

**MVP chooses (1).** Self-consistent GP is a Week-3+ upgrade, not a gate on Milestone A.

### 1.4 What “compute the Page curve” means in code

Deliverable object (must exist as arrays on disk, not prose):

```
v[i], S_rad[i], S_core[i], S_total[i], T_H[i], E_rad[i]
```

with:

- Early \(v\ll v_*\): \(S_{\mathrm{rad}} \approx S_{\mathrm{thermal}}(T_H)\) (rise).
- Late \(v\to 1\): under unitary core+rad evolution, \(S_{\mathrm{rad}}\to 0\) (purification) **if** the model works.
- \(S_{\mathrm{total}}\) constant within numerical tolerance under unitary evolution (null check).

Toy \(S=\frac12 S_{\mathrm{BH}}\,4v(1-v)\) remains unit-test shape only (`quantum_page_curve_scaffold.py`).

### 1.5 Explicit non-goals of MVP

- Full 3+1 evaporating Kerr hole.
- Island / replica-wormhole path integrals (not in corpus; not required for analog finite-core program).
- Astrophysical Page time in years for stellar masses (Hawking is too slow per BH file; MVP is in healing units).
- Re-opening area-law coefficient or roster (paid).

---

## 2. What existing code can be reused

### 2.1 Direct reuse (copy patterns / call / extend)

| Asset | Path | Reuse for |
|---|---|---|
| 1D GP split-step (healing units) | `scripts/bounce_m6_rebound_1d.py` | Background flow infrastructure; grid, FFT kinetic, energy guard |
| Hypersonic 1D GP | `scripts/bounce_m6_rebound_1d_hypersonic.py` | Super-critical \(\lvert v\rvert>c_s\) region = interior analog |
| Spherical GP production | `scripts/bounce_m6_rebound_gp.py` | Later radial upgrade (not Week 1) |
| 2D GP | `scripts/bounce_transverse_2d.py` | Later transverse check (optional Week 4) |
| Bogoliubov dispersion + coherence \(u^2,v^2\) | `scripts/bounce_fa1_transphononic_table.py` | Mode spectrum, pair content, “metric ends at \(\xi\)” quantitative fence |
| Page-curve design + toy shape | `scripts/quantum_page_curve_scaffold.py` | CLI skeleton, output dir convention, unit tests for \(v\in[0,1]\) bookkeeping |
| Area-law quarter (do not re-open) | `scripts/quantum_area_law_quarter.py` | Status table link only |
| Roster extension (do not re-open) | `scripts/area_law_roster_extension.py` | Status table link only |
| Healing-length / phonon decoherence notes | `scripts/medium_induced_decoherence.py` | \(\xi=\hbar/(m c_s)\) setup check; Cherenkov channel language |

### 2.2 Conceptual reuse (docs, no code)

| Asset | Use |
|---|---|
| `PRTOE_information_paradox.md` | Problem statement; kill/forbid rules |
| `PRTOE_blackholes_no_singularity.md` §4 | Sonic horizon = Landau ceiling; finite thermal core |
| `PRTOE_laboratory_cousins.md` | Steinhauer-class analog Hawking as external calibration |
| `PRTOE_entropy.md` §3 | Dynamics row open; coefficient not residual |
| Debt REPORT | “No instrument” → this plan supplies the instrument spec |

### 2.3 Missing (must be written — no existing Page/Unruh flux script)

There is **no** current script that:

1. Places a sonic horizon and measures \(\kappa\), \(T_H\).
2. Computes phonon occupation \(\langle n_\omega\rangle\) or energy flux through a horizon.
3. Evolves a finite core Hilbert space entangled with exterior modes.
4. Outputs \(S_{\mathrm{rad}}(v)\).

**New scripts (proposed names, under `scripts/`):**

| Script | Milestone | Responsibility |
|---|---|---|
| `page_curve_sonic_horizon_1d.py` | A | Background profile \(n,v\); locate \(x_h\); \(\kappa\), \(T_H\); plots |
| `page_curve_thermal_flux.py` | A | Mode basis on background; Bogoliubov coefficients or WKB greybody; \(\langle n_\omega\rangle\), \(F_{\mathrm{energy}}\) vs Unruh thermal |
| `page_curve_core_hilbert.py` | B | Finite core + radiation modes; unitary evolution; reduced entropies |
| `page_curve_evaporate.py` | C | Slow mass-loss schedule; \(S_{\mathrm{rad}}(v)\) curve; Page-turn detector |
| `page_curve_nulls.py` | all | Pre-registered nulls and kill checks; JSON summary to `_runs/...` |

Output root:
```
docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/
```

### 2.4 Reuse policy

- Prefer **forking** the split-step kernel from `bounce_m6_rebound_1d.py` into a shared helper only if a second consumer appears; for Week 1, copy-minimal is fine (corpus style).
- Do **not** import CLASS / cobaya / cosmology stacks for this workstream.
- Do **not** call `toy_page_S_rad` except inside unit tests labeled NOT A RESULT.

---

## 3. Week-by-week hard-work plan (4 weeks)

### Week 1 — Horizon instrument + thermal temperature (Milestone A, honest first success)

**Goal:** A 1D sonic horizon with measured \(\kappa\) and \(T_H\), plus a thermal flux spectrum consistent with Unruh/Hawking for the analog metric. **No Page curve claimed.**

| Day | Work |
|---|---|
| 1 | Freeze MVP conventions (healing units, horizon finder, output paths). Implement `page_curve_sonic_horizon_1d.py`: tanh or de Laval-like \(v(x)\), \(c_s(x)\); root-find \(x_h\); finite-difference \(\kappa\). |
| 2 | Convergence: double \(N\), half \(\Delta x\); \(\kappa\) stable to \(\lt 5\%\). Energy/norm guards on any GP background if used. |
| 3–4 | Build mode problem on fixed background: scattering states or wave-packet peeling near \(x_h\). Extract Bogoliubov \(\beta_\omega\) or equivalent occupation. |
| 5 | Compare \(\langle n_\omega\rangle\) to \(1/(e^{\omega/T_H}-1)\) over a mid-band (exclude deep IR box modes and UV \(k\xi\gtrsim 1\)). Greybody \(\Gamma(\omega)\) allowed; fit \(T_{\mathrm{fit}}\) vs \(T_H=\kappa/2\pi\). |
| 5 end | Write `page_curve/MILESTONE_A_REPORT.md`: PASS/FAIL thermal; numbers; fences. |

**Week 1 exit criteria (PASS):**

- Horizon found and \(\kappa>0\) for at least one BH-like profile.
- \(T_{\mathrm{fit}}/T_H \in [0.7, 1.3]\) in a pre-registered mid-band **or** documented systematic with plan to fix in Week 2 (not silent fail).
- Artifact: JSON + plots of \(n,v,c_s\), \(x_h\), \(\langle n_\omega\rangle\).

**Week 1 non-exit (do not claim):** any \(S_{\mathrm{rad}}(v)\) Page shape.

---

### Week 2 — Flux, energy loss law, finite-core skeleton (Milestone B start)

**Goal:** Energy flux \(F\) from the horizon; couple a **finite** core Hilbert space; prove early-time radiation is thermal **and** entangled with the core (not with a pure exterior).

| Day | Work |
|---|---|
| 1 | Integrate energy flux through a surface \(x>x_h\); check Stefan-like scaling \(F \propto T_H^2\) (1+1) or the correct 1D density of states. |
| 2 | Implement core as \(N_c\) oscillators (start \(N_c=4\)–\(8\)); radiation as \(N_r\) bins; total pure state \(\lvert\Psi\rangle\); evolve under pair-creation Hamiltonian \(\sim \sum_j g_j (a_{\mathrm{out},j}^\dagger b_{\mathrm{in},j}^\dagger + \mathrm{h.c.})\) with \(g_j\) set by \(\kappa\). |
| 3 | Reduced \(\rho_{\mathrm{rad}}\), \(S_{\mathrm{rad}}=-\mathrm{Tr}\rho\ln\rho\); early-time \(S_{\mathrm{rad}}\approx S_{\mathrm{thermal}}\); \(S_{\mathrm{core}}\approx S_{\mathrm{rad}}\) (mutual info). |
| 4 | Unitarity null: \(S(\rho_{\mathrm{total}})=0\) (pure) to numerical tolerance; no ad-hoc decoherence channel that dumps info. |
| 5 | Optional: replace prescribed background with mild GP evolution from Week-1 tools; re-measure \(\kappa(t)\). |

**Week 2 exit criteria:**

- Scripted \(S_{\mathrm{rad}}(t)\) for early window only (rise).
- Documented entanglement partner = core, not “environment infinity.”
- Kill-check harness started (`page_curve_nulls.py`).

---

### Week 3 — Evaporation schedule and first full \(S_{\mathrm{rad}}(v)\) attempt (Milestone C)

**Goal:** Drive \(v\) from \(0\) toward \(O(1)\) by depleting core energy into radiation; plot real \(S_{\mathrm{rad}}(v)\).

| Day | Work |
|---|---|
| 1–2 | Mass/energy loss: \(dE_{\mathrm{core}}/dt = -F(T_H)\); \(T_H(E)\) from \(\kappa(E)\) with a simple area/length law in 1D (e.g. \(\kappa \propto 1/R_{\mathrm{eff}}\) or fixed-\(\kappa\) control vs running-\(\kappa\)). Pre-register both controls. |
| 3 | Long unitary run (or Gaussian symplectic evolution if dimension forces it). Record \(S_{\mathrm{rad}}(v)\), \(S_{\mathrm{core}}(v)\). |
| 4 | Detect Page turn: peak finder; require \(S_{\mathrm{rad}}(v_{\mathrm{late}}) < S_{\mathrm{rad}}(v_*)\) with significance above numerical noise. |
| 5 | Stress tests: change \(N_c\), \(N_r\), UV cutoff; turn must be robust or failure documented. |

**Week 3 exit criteria:**

- First **honest** \(S_{\mathrm{rad}}(v)\) plot from dynamics (even if no turn / ugly).
- If no turn: run kill criteria §4; file FAIL or NEED-MORE-\(N_c\) with evidence, not a hand-drawn curve.

---

### Week 4 — Hardening, nulls, grade, and upgrade path

**Goal:** Either a null-hardened dynamical Page-like turn under stated fences, or a clean **OPEN/FAIL** with kill evidence. No fake-complete.

| Day | Work |
|---|---|
| 1 | Full null suite: pure thermal forever (should fail unitarity or fail purification); infinite core heat bath (should **not** Page-turn — control); finite unitary core (target turn). |
| 2 | Greybody / dispersion: include Bogoliubov \(k\xi\sim 1\) leakage (corpus: horizon leaks at healing length). Confirm late purification does **not** require a firewall flag. |
| 3 | Optional radial 1D (`bounce_m6_rebound_gp.py` geometry) or 2D spot-check of \(\kappa\) only. |
| 4 | Write `PAGE_CURVE_DYNAMICS_REPORT.md`: grade table, numbers, fences, kill outcomes. |
| 5 | Update pointers only if earned: QG ledger Q6, information_paradox status row — **only** if dynamics produced a real object; else leave OPEN. |

**Week 4 exit criteria:**

- Grade one of: **DYNAMICS-PASS (candidate)**, **DYNAMICS-FAIL (kill)**, **DYNAMICS-INCONCLUSIVE (need larger \(N_c\) / method change)**.
- Never: “coefficient paid ⇒ curve paid.”

---

## 4. Kill criteria (pre-registered)

These are registered **before** runs. Hitting a kill stops claim promotion; document and stop or redesign explicitly.

| ID | Kill condition | Implication |
|---|---|---|
| **K1** | Under unitary finite-core evolution with adequate \(N_c,N_r\), \(S_{\mathrm{rad}}(v)\) is monotonic thermal (no late decrease) through \(v\to 1\) | Page-turn claim **dies** for this setup; finite-core purification failed |
| **K2** | Purification only appears if a non-unitary “delete core” or firewall boundary condition is imposed | Contradicts sonic-horizon leakage story; **kill** AMPS-resolution-by-structure for this instrument |
| **K3** | Thermal Milestone A fails: no stable \(x_h\), or \(T_{\mathrm{fit}}\) disagrees with \(\kappa/2\pi\) by \(\gt 50\%\) after convergence and band cuts, with no fix in one week | Analog-Hawking instrument broken; **do not** proceed to Page dynamics |
| **K4** | \(S_{\mathrm{total}}\) drifts by \(\gt 10^{-3}\) (relative) under claimed unitary evolution without identified numerical cause | Code bug; results invalid until fixed |
| **K5** | Curve shape is produced only by inserting the toy \(4v(1-v)\) or \(S=A/4G\) algebra with no mode dynamics | **Forbidden**; automatic reject |
| **K6** | Horizon requires a fundamental causal knife (modes cannot correlate across \(x_h\) even at \(k\xi\sim 1\)) to match exterior thermodynamics | Conflicts with corpus sonic-horizon + medium-beneath claim |

**Non-kills (do not over-kill):**

- Greybody \(\Gamma(\omega)\neq 1\).
- Page time \(v_*\neq 1/2\) (1D / few-mode systems need not match 4D old-black-hole cartoons).
- Need for Gaussian truncation or moderate \(N_c\) (state as fence, not as full QFT gravity).
- Astrophysical evaporation timescales too long (already stated in BH file).

---

## 5. First milestone that is still honest: thermal flux only

### Milestone A — definition of done

**Name:** Analog Hawking / Unruh thermal flux on a 1D sonic horizon.  
**Honest claim language:**

> On a prescribed 1D acoustic black-hole profile with healing-length UV completion, the measured phonon occupation in a mid-frequency band is consistent with a thermal spectrum at \(T_H=\kappa/2\pi\) extracted from the surface gravity at the sonic point.

**Not claimed:** Page curve, information recovery, area law (already paid elsewhere), astrophysical rates.

### Milestone A — acceptance tests

1. **Horizon:** \(\lvert v(x_h)\rvert=c_s(x_h)\), \(\kappa>0\).
2. **Temperature:** \(T_H=\kappa/(2\pi)\) reported with finite-difference error bar.
3. **Spectrum:** \(\langle n_\omega\rangle\) vs \(\omega\); fit \(T_{\mathrm{fit}}\); ratio \(T_{\mathrm{fit}}/T_H\) in band.
4. **Dispersion fence:** modes with \(k\xi\gtrsim 1\) excluded from thermal fit or shown to deviate as expected (Bogoliubov table).
5. **Null:** \(\kappa\to 0\) (subsonic everywhere) \(\Rightarrow\) no thermal Hawking-like flux above numerical floor.

### Milestone A — deliverables

```
scripts/page_curve_sonic_horizon_1d.py
scripts/page_curve_thermal_flux.py
docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/MILESTONE_A_REPORT.md
docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/milestone_a_data.json
```

### Why this is the right first step

- Matches debt report: need a real instrument before \(S_{\mathrm{rad}}(v)\).
- Matches corpus radiation channel: Unruh-class phonon Hawking is “inherited, not lost.”
- Is independently falsifiable (K3) without demanding the full Page program.
- Reuses existing GP + Bogoliubov machinery without inventing islands.

---

## 6. Method ladder (if MVP is too small)

Escalate only if lower rungs pass or fail for known dimensional reasons:

| Rung | Method | When |
|---|---|---|
| 0 | Prescribed 1D acoustic metric + Bogoliubov modes + finite core | **Start here** |
| 1 | Self-consistent 1D GP background + same quantum sector | After A |
| 2 | Gaussian continuous-variable (symplectic) large-mode limit | If \(D=2^{N}\) explodes before Page time |
| 3 | Radial / 2D GP for \(\kappa\) geometry only | Hardening Week 4 |
| 4 | Literature Steinhauer-class comparison of \(T_H\) scaling | Calibration note, not PRTOE uniqueness |

Do **not** jump to holographic islands to “get a curve” while skipping Rung 0–2; that would abandon the corpus’s finite-core / sonic-horizon theory of the case.

---

## 7. Risk register

| Risk | Mitigation |
|---|---|
| Numerical reflection from box boundaries pollutes \(\langle n_\omega\rangle\) | Absorbing layers / large \(L\); windowed flux |
| Early thermal rise but no late purification due to tiny \(N_c\) | Scale \(N_c\); Gaussian methods; pre-register “inconclusive vs kill” threshold |
| Confusing coefficient payment with dynamics | Status lock text in every report header |
| Scope creep into full 4D GR collapse | Hard MVP fence: 1D analog only for 4 weeks |
| Owner pressure for a pretty Page plot | Kill K5; scaffold toy remains illustration only |

---

## 8. Success / grade map (end of 4 weeks)

| Outcome | Grade to write | Update information_paradox? |
|---|---|---|
| A fail (K3) | instrument FAIL | leave curve OPEN; note instrument debt |
| A pass, B early entropy only | dynamics **partial** | OPEN; “thermal channel instrumented” |
| A–C pass with Page turn + nulls | **candidate dynamics** | row → “curve: candidate (1D analog)” with fences |
| K1 or K2 hit | dynamics **FAIL** | OPEN → **killed under unitary core** (structural dissolution may still stand; quantitative curve does not) |

Structural dissolution of the paradox (no singularity shredder) is **not** automatically revoked by a computational fail of a 1D toy — but the **quantitative** half (ii) remains unearned or killed as graded.

---

## 9. Immediate next action (no plan theater)

```bash
# After implementation starts (not done in this plan-only write):
python3 scripts/page_curve_sonic_horizon_1d.py
python3 scripts/page_curve_thermal_flux.py
# Existing non-results (keep for status tables only):
python3 scripts/quantum_page_curve_scaffold.py
python3 scripts/quantum_area_law_quarter.py
```

**This file does not create those new scripts.** Implementing Week 1 is the next labor block.

---

## 10. Cross-links

| Doc / script | Role |
|---|---|
| `PAGE_CURVE_SCAFFOLD.md` | Design requirements; toy table |
| `PROGRAM.md` | P1 = Page-curve dynamics |
| `debt_page_curve_20260803/REPORT.md` | Inventory: no instrument before this plan |
| `PRTOE_information_paradox.md` | Status lock: curve un-run |
| `PRTOE_blackholes_no_singularity.md` | Sonic horizon + finite core |
| `bounce_m6_rebound_1d.py` | GP split-step reuse |
| `bounce_fa1_transphononic_table.py` | Bogoliubov spectrum reuse |

---

*Plan grade: implementation specification. Not a Page-curve result. Not a fake curve.*
