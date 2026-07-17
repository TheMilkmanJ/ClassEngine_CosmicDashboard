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

## 3. NO PIPELINE EXPRESSION — beneficial, lives in the theory (not code by nature)

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
a new derivation that overturns its killshot, logged in the failures ledger first.*

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

## THE THEORY↔CODE GAP, MEASURED (2026-07-17)

*A line-by-line read of the varying-constant path, from `background_varconst_of_z` through
`thermodynamics.c` to the chain configs. `thermodynamics.c` itself is **vanilla CLASS** — it
consumes the varconst rescalings (σ_T ∝ α²/m_e², rate ∝ α²/m_e³, recombination RHS ∝ α³m_e³) and
contains no PRTOE physics. Everything the model contributes is upstream.*

### 1. The T_c growth ramp is coded, unarmed, and a no-op either way

`background.c` implements the model's ramp exactly: **f_high = 1 − (1+z)/(1+z_high)**, which is
ε(T) = ε(1 − T/T_c) since T ∝ (1+z). **Verified against the model's own published stamps:** with
z_high = z(T_c = 179 keV) = 7.62×10⁸, the formula returns **0.6089 at the D bottleneck** and
**0.7765 at Li** — reproducing the documented **0.61ε / 0.78ε** exactly.

**But `varying_z_high` is set in no config anywhere**, and the C default is 0, which makes the
`if (varconst_z_high > 0.)` branch never fire: **f_high = 1 at every redshift.**

**Arming it would change nothing.** CLASS's varconst acts through **recombination (z ≈ 1100)**, where
the model's own ramp is saturated to **f_high = 0.999999**. **The growth ramp cannot affect any CMB
observable** — it is structurally unable to. Claims that the ramp is "now also in the CMB-side code"
are true of the source and empty of consequence. *(It matters on the BBN side, where it is applied —
by `scripts/prym_ramped_splice.py`, offline.)*

### 2. The BBN prior and YHe are BLIND to the dyad — this one is real

Both lambdas in the armed configs **declare `varying_me` and never reference it in the body**:

```
bbn:  lambda omega_b, varying_me: -0.5*( ((0.2471 + 0.0096*log(omega_b/0.02236) - 0.2449)/0.0040)**2
                                       + ((2.53e-5*exp(-1.6*log(omega_b/0.02236)) - 2.527e-5)/0.030e-5)**2 )
YHe:  lambda omega_b, varying_me: 0.2471 + 0.0096*log(omega_b/0.02236)
```

The signature makes Cobaya pass ε; the body computes pure ΛCDM BBN from ω_b alone. **The model's own
measured window (Y_p +0.85%, D/H +0.65%) never reaches the likelihood.** Two consequences:

| | as scored | if the model were scored | gap |
|---|---|---|---|
| Y_p | 0.247100 (+0.55σ) | 0.249145 (+1.06σ) | |
| D/H ×10⁵ | 2.5300 (+0.10σ) | 2.5398 (+0.43σ) | |
| **BBN prior χ²** | **0.312** | **1.308** | **−1.0 unpaid — the chain is too generous** |

**And the same blind lambda sets YHe, which is fed to `thermodynamics.c` for helium
recombination.** The fit is handed a **ΛCDM helium fraction**: n_e ∝ (1−Y_p) is **−0.27%** off the
model's own value. That is *not* a no-op — Y_p at the few-per-mille level moves the damping tail and
is degenerate with n_s and H₀.

**Status: the ~1 χ² is an unpaid cost the model owes; the YHe leg needs a run to size. Neither is
fixed here — the chains are armed and running, and their configs are not to be edited mid-flight.**
The fix is one line in each lambda (add the elasticity term, d(Y_p)/dε = 0.00163 per %ε), to be
applied at the next cold start.

