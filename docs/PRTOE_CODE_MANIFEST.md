# THE CODE MANIFEST — what is in the pipeline, what is armed, what is banned (2026-07-12)

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


*The inclusion law: everything proven beneficial enters the pipeline; nothing
killed ever does. This file is the single source of truth for implementation status.
Homes: [C] = CLASS source (background.c/input.c), [Y] = cobaya yaml configs, [CMP] = the
comparison layer (scripts/), [DOC] = laws/grammar with no pipeline expression.*

## 1. IN — running now (the referee's own physics)

| item | home | status |
|---|---|---|
| The dispersion shape: ρ_rad = dust·(√(1+x²)−1), exact p and dp/dloga | [C] background.c | IN — the live .so, direct-eval verified (2798.7) |
| THE RAMPED WINDOW EDGES: varying_transition_width (tanh fades in ln(1+z); 0 = legacy step) | [C] background.c/input.c/background.h | IN — pipeline .so rebuilt clean-PATH, width=0 backward-compat verified |
| The dyad (varying m_e, the ramp through T_c) | [C] | IN |
| The dcdf unified sector (rad→CDM crossover at z_on) | [C] | IN |
| **THE ZERO-PARAMETER EVIDENCE RUN** (ε, A_s, n_s, z_on all STATED) | [Y] cmp_prtoe_fixed.yaml | **LIVE (launched 2026-07-12 23:14; PID 442916)** |
| The evidence pair (sampled-ε dyad + ΛCDM twin) | [Y] cmp_prtoe_dyad_ev / cmp_lcdm_ev | queued — the sampled referee KILLED mid-prior by decision (relaunch fresh later); the ΛCDM twin awaits its slot |
| The freeze-sentinel launch guards | [CMP] both wrappers | IN — verified quoted+unquoted |

## 2. ARMED — enters on its named trigger (the amended conditions)

| item | value | trigger | lands in |
|---|---|---|---|
| A_s frozen | 2.088058×10⁻⁹ = (α_c/4πk)³, concordance joint k | **IN — EXECUTED; running in the live zero-parameter test** | [Y] |
| z_on frozen | 3.5619×10⁷ (log 7.5517 — the BOBYQA frozen-stack profile; the 3α mark hit to 0.005 dex) | **IN — fast-profiled estimate; the α_c MCMC grades it later** | [Y] |
| n_s stated | 0.9641 = 1 − 2/ln(M_Pl/T_on) at the profiled z_on | **IN — running in the live test** | [Y] |
| ρ_inf stated | the occupancy value | the α_c MCMC + the triangle confirmed | [Y] |
| m_ncdm stated | 61.4 meV | the spurion (docketed) lifted + P-023 resolved | [Y] |
| The flow ladder correction | ω₀ = 0.77 km/s/Mpc; 73.0 → 72.2 at full coherence | genesis sizing fixes the coherent fraction | [CMP] flow_ladder_correction.py (built) |

## 3. NO PIPELINE EXPRESSION — beneficial, lives in the books (not code by nature)

The chain law; the melt; the counterparty rule; the zero–infinity asymmetry; the genesis
chart (Γ/impulse/E/friction); the Widnall n-predictor (n = 2.26–2.51 × R/a — the α_c MCMC/comb
read it, nothing to code); the partition band (L/D 4.3–5.3 — the inverse problem's
target); the μ-branch discriminator (future-data referee); the helicity cross-lock
(prediction); the cycle-counter (entropy census). These grade claims and design tests —
they do not alter any observable CLASS computes (the entry-55 energy nulls are the
proof for the flow family).

## 4. BANNED — killed items; never enter the pipeline (the failures ledger governs)

The v1–v5 screening mechanisms; the β barotropic parameter; the dkappa hack; the c_γ/c_EM
environmental knobs (census-illegal); the sound-horizon lock (+6 blue); the μ-era H₀
lever (×17–83 short); the S₈-flow lever (energy null + wrong-signed); the burst
speed-accumulator (rotation resets; no exterior frame); entrainment as a distinct thread
(absorbed); the literal plasma-ring matter distribution (isotropy); the ring-through-a-
white-hole feeder (counterparty rule; unneeded). *Rule: a killed item re-enters only by
a new derivation that overturns its killshot, logged in the ledger first.*

## 5. The standing verification

Every [C]-expressible beneficial item is ALREADY COMPILED into the live .so the referee
is sampling — the inclusion law is satisfied for the C code as of now; the deltas
are all [Y]-layer freezes on named triggers. Any future session that produces a
pipeline-expressible result MUST add its row here in the same commit.

## 6. THE BUILD QUEUE — everything still needing code, genesis → now

*CLASS is complete for its jurisdiction (isotropic background + linear physics — every
beneficial item compiled and running). The remainder are standalone solvers/analysis
tools, ordered by the chain:*

| # | build | what it computes | feeds | size |
|---|---|---|---|---|
| B1 | **THE GENESIS SOLVER** (the inverse problem) | ring dynamics from the four-line card (Γ, impulse, E, α(T/T_c)): R(t), core, velocity field, the intake curve | ε + the mass share (one curve, two moments), the discharge band (L/D 4.3–5.3), n's aspect ratio, the flow's coherent fraction, the H₀ remainder | PROJECT — the queue's crown |
| B2 | **the winding-gas C_V** (lock 2's method, string-gas import) | the medium's specific-heat scaling near T_c: does C_V ∝ R² emerge from the compact-axis windings? | the census drift (the tilt, thermodynamic road) + the lock-count C → THE A_s CLEARANCE | one careful session |
| B3 | **the k_int O(1) audit** (referee 1's residue) | the interaction integral's surface-DOS + normalization conventions, forced from the roster | the Eliashberg kill window (k ∈ [1.35, 1.37]) | one session |
| B4 | **the Tier-1 comb/isocurvature rehearsal** | ramped template fit on the public Planck binned TT residuals (teeth widths + envelope + shared n) | P-029/031/033 sensitivity (REHEARSAL, not the referee) | light — one evening |
| B5 | **the μ-injection calculator** | μ(z_inject, efficiency) with the visibility ramp | the draw-branch discriminator (ξ vs 1/m) | small script |
| B6 | **THE BipoSH JOINT PIPELINE** | one sky direction forced through the axis family on the Planck maps | P-032 — the registered referee ("analysis-limited, data exists") | PROJECT — post-PolyChord |
| B7 | the cycle-map turn module | the DE-era → contraction transition dynamics | the chain's 10→11 tether, the cycle-counter's sizing | PROJECT — shares B1's room |

*Execution order when the referee frees the box: B4 + B5 (light, immediate) → B2 + B3
(the clearance pair — A_s hangs on them) → B1 (the crown: five pre-registered ambushes
wait on its outputs) → B6 (the axis referee) → B7. Nothing on the banned list appears
above; nothing beneficial is missing — any session that mints a new computable adds its
row here in the same commit.*
