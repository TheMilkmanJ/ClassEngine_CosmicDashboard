# THE CODE MANIFEST — what is in the pipeline, what is armed, what is banned (2026-07-12)

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


*The inclusion law: everything proven beneficial enters the pipeline; nothing killed ever does. This
file is the single source of truth for implementation status — so every row states where a thing
lives and whether it is actually running, checked against `ps` and the file timestamps rather than
against intent.*

*Homes are named, not lettered: **CLASS source** (background.c/input.c), **yaml** (the cobaya
configs), **comparison layer** (scripts/), **doc-only** (laws and grammar with no pipeline
expression).*

## 1. IN — running now (the referee's own physics)

| item | home | status |
|---|---|---|
| The dispersion shape: ρ_rad = dust·(√(1+x²)−1), exact p and dp/dloga | CLASS source: background.c | IN — the live .so, direct-eval verified (2798.7) |
| THE RAMPED WINDOW EDGES: varying_transition_width (tanh fades in ln(1+z); 0 = legacy step) | CLASS source: background.c/input.c/background.h | IN — pipeline .so rebuilt clean-PATH, width=0 backward-compat verified |
| The dyad (varying m_e, the ramp through T_c) | CLASS source | IN |
| The dcdf unified sector (rad→CDM crossover at z_on) | CLASS source | IN |
| **THE POLYCHORD EVIDENCE RUN — sampled-ε** (varying_me, A_s via logA, n_s, dcdf_rho_inf, m_ncdm all SAMPLED) — tests whether the data prefers varying-m_e at all (Occam-penalized) and whether the ε-posterior lands on the derived 1.2543% | yaml: pc_prtoe.yaml (PolyChord) | **NOT RUNNING** — killed mid-prior by decision; all its files stamped 2026-07-17, no live process. Relaunch is a deliberate future act, not a resumption |
| **THE ZERO-PARAMETER RUN — ε/A_s/n_s FIXED** (varying_me = 1.012543, A_s = 2.088058×10⁻⁹, n_s = 0.9641; only dcdf_rho_inf, z_reio, m_ncdm + nuisances sampled) — the actual *zero-extra-parameter rival to ΛCDM* test | yaml: cmp_prtoe_fixed.yaml | **EXECUTING** — the headline evidence test, restarted 2026-07-18 with the prior phase explicit; sampling since 16:22 |
| The evidence pair (sampled-ε dyad + ΛCDM twin) | yaml: cmp_prtoe_dyad_ev / cmp_lcdm_ev | queued — the sampled referee KILLED mid-prior by decision (relaunch fresh later); the ΛCDM twin awaits its slot |
| The freeze-sentinel launch guards | comparison layer: both wrappers | IN — verified quoted+unquoted |

## 2. ARMED — enters on its named trigger

| item | value | trigger | lands in |
|---|---|---|---|
| A_s frozen | 2.088058×10⁻⁹ = (α_c/4πk)³, concordance joint k | **IN — EXECUTED; running in the live zero-parameter test** | yaml |
| z_on frozen | 3.5619×10⁷ (log 7.5517 — the BOBYQA frozen-stack profile; the 3α mark hit to 0.005 dex) | **IN — fast-profiled estimate; the α_c MCMC grades it later** | yaml |
| n_s stated | 0.9641 = 1 − 2/ln(M_Pl/T_on) at the profiled z_on (the value the live run executes; the exhibited mechanism's k-local number is 0.9677 — the delta is 0.86σ at Planck width, noted for the NEXT config, no mid-run change) | **IN — running in the live test** | yaml |
| ρ_inf stated | the occupancy value | the α_c MCMC + the triangle confirmed | yaml |
| m_ncdm stated | 61.4 meV | the spurion identification lifted (done — neutrino_sector §2) + P-023 resolved | yaml |
| The flow ladder correction | ω₀ = 0.77 km/s/Mpc; 73.0 → 72.2 at full coherence | genesis sizing fixes the coherent fraction | comparison layer: flow_ladder_correction.py (built) |

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

Every beneficial item expressible in the CLASS source is ALREADY COMPILED into the live .so the
referee is sampling — the inclusion law is satisfied for the C code as of now; the remaining deltas
are all yaml-layer freezes on named triggers. Any future session that produces a
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

## THE THEORY↔CODE BOUNDARY

*A line-by-line read of the varying-constant path, from `background_varconst_of_z` through
`thermodynamics.c` to the chain configs. `thermodynamics.c` itself is **vanilla CLASS** — it
consumes the varconst rescalings (σ_T ∝ α²/m_e², rate ∝ α²/m_e³, recombination RHS ∝ α³m_e³) and
contains no PRTOE physics. Everything the model contributes is upstream.*

### 1. The T_c growth ramp is coded, unarmed, and a no-op either way

`background.c` implements the model's ramp exactly: **f_high = 1 − (1+z)/(1+z_high)**, which is
ε(T) = ε(1 − T/T_c) since T ∝ (1+z). **Verified against the model's own published stamps:** with
z_high = z(T_c = 179 keV) = 7.62×10⁸, the formula returns **0.6089 at the D bottleneck** and
**0.7765 at Li** — reproducing the documented **0.61ε / 0.78ε** exactly.

**The coded T_c and the chain's T_c, and why the difference does not propagate.** The pipeline and
the offline BBN splice were computed at **T_c = 179 keV**; the dark-energy chain's T_c is the
kernel-sourced **177.10 keV**, 1.07% lower. It is one temperature, not two, so the coded value is an
approximation of the standing one. Priced: at 177.10 keV the ramp stamps read **0.6047** at the
deuterium bottleneck and **0.7741** at lithium, against the coded 0.6089 and 0.7765 — a 0.69% shift
on the D stamp, which moves the window's D/H contribution from +0.645% to +0.641% and the predicted
D/H by **0.002σ** against a budget of ±0.047×10⁻⁵. The difference is four hundred times smaller than
the measurement it feeds, so the coded value stands until the pipeline is rebuilt for another
reason.

**`varying_z_high` is set in no config anywhere**, and the C default is 0, which makes the
`if (varconst_z_high > 0.)` branch never fire: **f_high = 1 at every redshift.**

**Arming it would change nothing.** CLASS's varconst acts through **recombination (z ≈ 1100)**, where
the model's own ramp is saturated to **f_high = 0.999999**. **The growth ramp cannot affect any CMB
observable** — it is structurally unable to. Claims that the ramp is "now also in the CMB-side code"
are true of the source and empty of consequence. *(It matters on the BBN side, where it is applied —
by `scripts/prym_ramped_splice.py`, offline.)*

### 2. The BBN prior and YHe apply the dyad's ramp

Both lambdas in the evidence configs carry the measured varying-m_e curve, so the model's own
window (Y_p +0.85%, D/H +0.65%) reaches the likelihood and the YHe fed to `thermodynamics.c` is the
model's helium fraction, not ΛCDM's:

```
YHe:  lambda omega_b, varying_me: 0.2471 + 0.0096*log(omega_b/0.02236)
                                  + 0.00176009*((varying_me-1)*100) - 5.105e-05*((varying_me-1)*100)**2
```

The elasticity term (d(Y_p)/dε ≈ 0.00163 per %ε at the operating ε, from the measured PRyM curve) is
in both the `bbn` prior and the `YHe` value across `cmp_prtoe_*` and `pc_prtoe`. Scored on the model
rather than ΛCDM, the BBN prior carries its own weight (χ² 0.31 → 1.31): the window's Y_p +0.85% and
D/H +0.65% now enter the fit, and the helium fraction n_e ∝ (1−Y_p) is the model's, closing the
few-per-mille damping-tail degeneracy with n_s and H₀.

