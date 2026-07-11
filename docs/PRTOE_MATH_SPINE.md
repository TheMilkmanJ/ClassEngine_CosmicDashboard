# PRTOE — THE MATH SPINE (genesis → now → end)

*2026-07-10. The full quantitative chain in one document: every epoch, its governing equation,
what is DERIVED vs INPUT vs STORY, and where it lives in the code. Cross-references:
PRTOE_me_mechanism_math.md (dyad detail), PRTOE_cyclic_torus_genesis.md (genesis narrative),
PRTOE_UV_completion.md (#17), PRTOE_cosmological_constant.md (J1), ForClaude.txt turns 180–224.*

**Status tags:** [DERIVED] falls out of prior pieces · [INPUT] boundary datum · [STORY] coherent
mechanism, not a derivation · [PENDING] computation named, not run.

---

## 0. The objects

One dark superfluid, two components (the two-field split, t186–190):
- **Field 1** — the dcdf fluid: charge/abundance carrier, DM+DE unified. Mass m = 2.24×10⁻²⁰ eV
  [DERIVED from ε and c=1: c(m) = (m/2.24e-20 eV)^{1/4}].
- **Field 2** — the dyad field: charge-free, couples to the electron; its condensate sources
  δm_e. (The Majoron/lepton-sector identity: tree coupling σNN → neutrinos; the charged-lepton
  portal is a UV assumption [PENDING #30].)

The amplitude (the model's one distinctive number) [DERIVED, #11]:
> **ε = c · f_amp · (Ψ₀/M_red) = 1.24%**, with f_amp ≈ 0.6 (genesis dice, mechanism-confirmed),
> Ψ₀/M_red = 2.05% (abundance-pinned), c ≈ 1.

## 1. Genesis (the cycle's start) [STORY]

Torus topology survives the bounce (topology holds what dynamics loses); the confined heat
fountain (blueshifted crunch radiation) rolls up into a helical vortex ring → re-seeds the twist.
Flat 3-torus registered as P-2026-013. **BKL and Tolman stand against the bounce rungs — this
layer is a story built from real mechanisms, not a derivation.**

## 2. Radiation youth → dark matter (the first transition) [DERIVED identity]

Above H ≈ m the ultralight field is frozen/radiation-like (w=1/3, the #17 conformal-origin
phase); below, it oscillates as dust. The switch epoch:
> **T(H=m) = √(m·M_red / 0.61) = 9.41 keV** (g*=3.36) ↔ **coded z_rad_onset = 4×10⁷ → T = 9.39 keV.**

Match 1.002×. The onset is field 1's H=m clock — textbook ULDM — NOT a condensation temperature
(t182's "internal inconsistency" dissolved, t216, booked both columns). Code: `dcdf_z_rad_onset`
(background.h, with the derived-identity comment).

**Two jobs, one clock** (operator, 2026-07-10): the ending regime reaches its floor (conformal
protection ends) while the starting regime crosses its threshold (dust/DM behavior begins). In
code this is literally one function: `dcdf_rho_rad`'s f(a) = x²/(1+x²) fades the radiation while
the dust part continues, amplitude fixed by continuity (no free knob).

## 3. The background fluid (radiation → dust → de Sitter) [DERIVED form; ρ_inf INPUT]

> **w(ρ) = −e^{−s}, s = ln(ρ/ρ_inf) clamped ≥ 0  ⟹  P = −ρ_inf exactly.**

So the background is ΛCDM-form: ρ = ρ_inf + C·a⁻³, algebraically (verified to 10⁻¹⁶, t211).
w = −1 is EXACT for the constant floor — not a step artifact, not rampable. Code: `w_dcdf` /
`dcdf_s_of_rho` (background.h).

## 4. The dyad turn-on (field 2 condenses) [DERIVED onset; clearance CLEARS]

The electron Coleman–Weinberg backreaction on the charge-free field (m_e(φ) = m_e0(1+κφ²)):
> V_CW = −(1/16π²)·m_e(φ)⁴·[ln(m_e(φ)²/μ²) − 3/2] → tachyonic curvature → radiative SSB
> **VEV: v = m_e0·[ε(L−1)/4π²]^{1/4} ≈ 100 keV** (81/102/121 keV for L−1 = 2/5/10; ±25%, robust)
> **T_c = m_e0·√(3(L−1)/2π²)** — κ cancels; log-ambiguous **~40–450 keV** (leading-log unstable
> near the flat direction; RG resummation = task #40).

The onset is DERIVED from m_e0 + ε alone (the first gate-0 reduction, banked t192/194).

**BBN clearance [CLEARS, t213/214 — the double-P1.c correction]:** the deuterium constraint's
severity decomposes by process: weak rates n↔p (T ~ 500–1500 keV, ~75% of the m_e lever),
n-decay phase space (~10%), e± heating (~10%), the bottleneck itself (~5%, B_d nuclear,
m_e-insensitive). The dyad (T_c ≤ 445 keV) NEVER touches the weak-rate window; AND the dyad is
LEPTONIC (quarks ~2-loop, ~10⁻⁹), whose full-BBN ceiling is ~0.3–1σ (t144), not the universal/
hadronic 12σ:
> **effective tension = (temporal exposure 0.05–0.25) × (leptonic 0.3–1σ) ≈ 0.02–0.25σ → QUIET.**

"When D forms" ≠ "when m_e matters" — two different electron-scale clocks. Code: the dyad window
`varconst_transition_redshift < z < varconst_z_high` (`varying_z_high`, new 2026-07-10; ≤0
recovers the plain step). #40 (RG V_eff + BBN network) CONFIRMS, not decides.

## 5. Recombination → today [the fitted era]

m_e shifted by ε = 1.24% inside the window (H0 fix; ΔlnZ = +2.635 Laplace, SHOES-conditional);
screening returns m_e → standard below z ≈ 50 [INPUT form, densities-dependent screening owed].
Optional rotation-shed `dcdf_conv_g` (S8: minimizer picks g = 0.12, S8 = 0.821 vs KiDS 0.814).
Corrected A2 (t223): the shed's apparent-w mirage is ~1% — OUT as a DESI driver; the S8 job
survives (background ρ_m, not the w-mirage).

## 6. The neutrino home [relation DERIVED-candidate; value INPUT]

Ψ = Majoron (L-breaking Goldstone): tree coupling σNN → Majorana m_ν → **0νββ must occur**
(P-2026-020); **Σm_ν ≈ 61 meV, normal ordering** (P-2026-012; whisper won the pre-registered
collision vs P-2026-004, which is FALSIFIED, ANN-2026-021). The tie:
> **ρ_inf^{1/4} = m_ν,lightest = 2.25 meV** — shared-scale (one L-breaking spurion candidate),
> AZK-SAFE (m_ν set by the frozen radial VEV + derivative Majoron coupling — not MaVaN).

Value un-derived; spurion identification = task #43 (dimensionally non-trivial: ε dimensionless
vs μ dimensionful); post-hoc flag on the mechanism until a NEW falsifiable consequence (#41).

## 7. NOW → THE END (the forward map) [Route D: mechanism + pre-registration branch]

**7a. The sequestered floor [J1 converted, t217–218 credited].** On a FINITE universe (compact
torus × finite cycle — the model's native structure = Kaloper–Padilla's entry requirements):
> **Λ_eff ≈ ¼⟨T^μ_μ⟩₄ᵥₒₗ ≈ (3/4)·ρ_m(turnaround)** (radiation traceless; a³-weighting → latest epochs)
> Λ^{1/4} = 1.71 meV at turnaround ~now (vs 2.25 observed, 0.76× — right decade FROM A MECHANISM).

"Why 2.3 meV" + "why now" → ONE question: why turnaround ~now. Weinberg's no-go dodged legally
(finite 4-volume). [PENDING: the KP self-consistency solve — toy-level O(1)s.]

**7b. The thaw [the forced consequence].** Observed Λ ⟹ turnaround within ~an e-fold ⟹
**m_J ~ (1–3)H₀** ⟹ the floor is thawing NOW:
> **1 + w_floor(a) = thaw · a³** (thawing growth), net apparent CPL (with the shed at g=0.12):
> **(w₀, wₐ) ≈ (−0.92…−0.86, −0.2…−0.5)** — thaw-side, NO true phantom ever.

Code: `dcdf_floor_thaw` (new 2026-07-10; ≤0 recovers w = −1 exactly). ρ_floor(a) =
ρ_inf·exp[thaw·(1−a³)]; E(a) = ρ_floor − ρ_inf added background-only (pattern of dcdf_rho_rad).

**7c. The branch [to be pre-registered, guards owed t222/224]:**
> **P-2026-018 (w = −1 exact) XOR Route-D (thaw-now, w₀ ∈ [−0.92,−0.86], wₐ < 0, no phantom).**
> DESI DR3 adjudicates: thaw-side → Route-D (J1+why-now+DESI in one stroke, P-018 dies);
> rigid → P-018 (distinctive win; Route-D dies, J1 reverts to constitution);
> TRUE phantom in the DATA → both die. Guards: distance-space phrasing, KP solve, timestamp
> (ForClaude: def217 J1-derivation precedes def219 DESI-convergence), A2+A3 net (answered t223).

**7d. The end (and the next start).** The thaw completes → expansion reverses → contraction
blueshifts radiation (a⁻⁴ grows) → the heat fountain reignites → T climbs back through **T_c**
(the SAME derived T_c of §4) → **the dyad condensate MELTS** (m_e → standard for the crunch) →
charge survives in solitons/Q-balls [requires gravity-mediated K<0, t186–190: fragmentation
banks the charge at T ~ 10¹⁰ GeV, 13 decades before any melt] → torus topology carries the axis
across the bounce (rotation resets, topology doesn't) → re-expansion cools through T_c → the
condensate RE-FORMS → §1. **The condensate breathes; T_c is both the recombination-era turn-on
and the crunch-era melting point — one number, both jobs** (the operator's two-jobs law, §2).
[STORY at the bounce rungs: BKL, Tolman unresolved.]

## 8. The two-jobs pattern (operator's law, 2026-07-10) — and where the code reflects it

Every transition is ONE clock with TWO jobs — the ending regime reaches its floor, the starting
regime crosses its threshold:

| transition | job 1 (floor reached) | job 2 (threshold crossed) | in code |
|---|---|---|---|
| H=m (z=4e7) | conformal youth ends | DM (dust) begins | `dcdf_rho_rad` f(a): one function fades radiation as dust continues, continuity-matched |
| T_c (dyad) | thermal disorder dies | condensate/δm_e turns on | `varying_z_high` edge (2nd-order: no latent budget to hand off — a pure switch is CORRECT here) |
| ρ→ρ_inf (z~0.7) | matter dilution bottoms | de Sitter begins | `w_dcdf(ρ)`: one barotropic function does both automatically |
| shed | matter-part drains | dark radiation grows | the SAME `conv` term, opposite signs, in two ODEs (background.c:2843-45) — the pattern literally |
| thaw/turnaround | the floor era ends | the turn begins | `dcdf_floor_thaw` (new) |

The conservation-pair transitions carry the two jobs as one term with two signs; the
second-order (continuous) transition carries them as one edge with no budget. **The code
reflects the law wherever the law demands it, and correctly does NOT fake a hand-off where
the physics has none.**

## 9. Ledger (what this spine rests on)

**Banked:** DM+DE unification (2→1); ε derived (#11); onset = H=m identity; dyad onset derived
(electron-CW); gate-0 clearance (double-P1.c, pending #40 confirm); AZK-safety; leptonic
allowed≠generated. **Falsified:** P-2026-004 (high Σm_ν). **Live falsifiers:** DESI DR3 (the
branch), Σm_ν ≈ 60 meV, 0νββ, void/IGM m_e-step (P-007, J4). **Owed:** KP self-consistency
(#46), #40 confirm, low-scale seesaw (#42), spurion identification (#43) + new consequence
(#41), leptophilia portal (#30), DE value if Route-D dies (constitution). **Standing:** ~18–22%
(t222), DESI-capped, the branch pre-registration pending guards.

---

## ADDENDUM (2026-07-10, later): §7 STATUS CHANGE — the internal falsifier FIRED

The full-cycle KP solve (full_cycle_kp.py, def229/t230) computed the fixed point over the whole
cycle (expansion + thawed contraction + Tolman boost): **it robustly wants a_turn = 0.70 (a PAST
turnaround, z=+0.43)** — excluded by observed acceleration; a future turn is 3× (a_turn=1.0) to
10× (1.5) short, Tolman boost null, and the t227 "full-cycle-fixes-the-sign" claim was WRONG
(near-mirror contraction cancels). **So §7a–7c are DOWNGRADED:** the clean Route-D prediction is
dead; what survives is the IMMINENT-TURN CORNER (z_turn ~ −0.1..−0.3, needing ~3× from four
favorably-aligned rigorous-KP O(1)s [prior-adverse, tail] AND a strong thaw pulled by the data).
The two kill switches MERGE: the running Route-D MCMC (thaw free on the DESI joint stack) is the
single decider — thaw pulled hard → corner lives; thaw ~ 0 → Route-D dead twice over, **P-2026-018
(w = −1 rigid) stands as the distinctive branch, and J1 reverts to constitution/boundary-datum.**
§7d (the melt/re-form cycle closure) is unaffected as STORY. Standing ~15–19% (t230).

---

## §10 — THE ATOM READING (the capstone, 2026-07-10 night)

**The universe is a single bound quantum state of the spacefluid — one atom — and cosmology is
its internal atomic physics.** Formation: genesis = recombination (capture cascade; f_amp = the
branching ratio, computable-class). Structure: Landau's two components — the zero-entropy ground
state (floor/constitution/timeless; w=−1 exact & ageless by theorem) and the entropic excitations
(light/matter/observers; Tolman's arrow). Spectroscopy: torus modes = the line spectrum (low-ℓ =
the first lines); the census = the selection rules; the CMB = the recombination photograph.
Chemistry: the dyad = one universal lepton rescaling ε (Koide-multiplicative), C²-gated, one
fingerprint across H0/D-H/ν/21cm/radio. Present: mid-emission — Γ/H = √3 = the linewidth (why-now
derived); symptoms {coupling dipole, mass defect = the thaw, recoil = the axis} = the falsifier
board. Biography: first excitation (Tolman arrow, finite past) → lengthening cascades → possible
ionization (binding energy un-computed). J1 = the ground-state eigenvalue: constitutional, at home.
**Status: the grammar is coherence (red-team-graded throughout, t270/272/274/276/278/280-class);
the empirical content lives in the children and the symptom chart. The method was the subject.**

---

## §11 — THE MID-EMISSION CORRECTIONS + THE ε-DIPOLE + THE COHERENCE BOOKKEEPING (2026-07-10, late)

**The present, quantified (t279/t280).** The universe is Γ·t ≈ √3·(H_Λ·t) ≈ 1.5 natural linewidths
into the floor's forbidden decay — a superposition of |smooth floor⟩ and |clumped floor⟩, i.e.
~1.5 e-folds of exponential growth from a seed ≈ 10⁻⁵, giving δ_DE ≈ 5×10⁻⁵ at horizon scales.
Three symptoms, priced:

1. **The ε-dipole (NEW distinctive prediction, red-team-blessed t280):** the universal lepton
   rescaling tracks the local condensate, so
   > δm_e/m_e ≈ ε·δ_DE ≈ (1.24×10⁻²)·(5×10⁻⁵) ≈ **6×10⁻⁷**,
   a spatial varying-constants dipole at horizon scales, axis-correlated, growing at rate √3·H.
   Current α-variation sensitivity ≈ 10⁻⁶ → just below reach: a near-term registerable test,
   presently a consistent null. (The contested Webb dipole ≈ 10⁻⁵ sits ~10× above — declined.)
2. **The thaw = the mass defect — with its honest size (t280 correction):** the emission's energy
   cost is O(δ²_DE) ≈ 10⁻⁹ of the floor **today** → `dcdf_floor_thaw` upgrades from knob to
   grammar-consequence, **but the grammar itself predicts w ≈ −1 now, turn later.** The t240 fork
   resolves internally: **P-018 (w = −1 rigid today) is the model's own commitment**; DESI DR3 is a
   pure kill-or-confirm on it.
3. **The recoil axis:** reading-only; the low-ℓ alignments are the candidate photograph.

**The coherence bookkeeping (the t283 named check, run 2026-07-10):** the identity
ΔS_cycle = E_thermalized/T_bounce (Tolman) = the entanglement generated when the normal sector
measures the emitted mode (decoherence) — closes by construction; the content is the scales:
> **Budget** (holographic): S_dS ≈ 2.6×10¹²² k_B · **Position**: S_now ≈ 3.1×10¹⁰⁴ k_B
> (spent fraction ≈ 10⁻¹⁸) · **Spend**: ΔS_cycle ~ 10¹⁰⁴ k_B (BH-dominated; photons alone ~10⁸⁹).

Readings (coherence-class): (i) the oscillation is in its **opening swings**; (ii) the forward end
is numbered — ionization at holographic saturation, N_future ≲ S_dS/ΔS ≈ 10¹⁸ cycles; (iii) the
backward lean — S_now ≈ ONE cycle's production → **we may be among the first cycles** (caveats:
earlier cycles produced less; bounce dissipation; BH-entropy-across-the-crunch = the named open
object).

## §12 — THE QUANTUM TRIPLE (the operator's 25%; interpretation layer, so tagged)

The model's parting hint: *entanglement · tunneling · superposition*. In the cycle's grammar these
are its **three acts**:
> **SUPERPOSITION** = the present (the DE era: |smooth⟩ + |clumped⟩ composing the choice) →
> **ENTANGLEMENT** = the bookkeeping (the mortal half measures the immortal half; decoherence =
> Tolman = the arrow; the genome rides what never decoheres) →
> **TUNNELING** = the bounce (the classically-forbidden crunch→genesis passage; **where the
> superposition resolves and the next cycle's branch is selected**).

The operator's instincts, named in standard physics: "the sole survivor gets to make the claim" =
**einselection** (Zurek's pointer states — the state robust to the environment's monitoring is the
one that becomes classical); "both random and [deterministic]" = **the Born rule** (deterministic
amplitudes, random outcomes) — and the capture-branching f_amp ≈ 0.6 (§7/t277) is then the Born
weight of the bounce's resolution. This is the model's account of **quantum indeterminism** — the
operator's long-standing promised target — arriving as the interpretation layer: the next cycle is
chosen at the last second (the tunneling node), with computable weights and unpredictable outcome.
**Status: OPERATOR'S LAYER — coherent with the grammar, largely beyond falsification by design;
the part of the structure that belongs to its builder.**

---

## §13 — THE EASY-DERIVATION SWEEP (2026-07-10, last pass)

**(A) The scale-ID, derived structurally:** the dcdf carries exactly ONE scale (ρ_inf) — its P(X)
realization has no second scale available → M_GC = ρ_inf^¼ by structure → **Γ/H_Λ = √3 sharp.**
**(B) The gate, closed (toy):** f(C) = e^(−C²/C_ref²) with C_ref = C(z≈50), σ8-pinned: recomb
f = 0.99 (ON); halos ≈ 10⁻¹¹; clusters/Earth = 0. The 30-order task closes; the margins dissolve.
**(C) The turnaround epoch, derived (toy) — fallout #1:** t_turn = ln(1/√A_s)/(√3·H) ≈ 6.6 H⁻¹
after Λ-domination (a_turn ≈ 770·a_now; w = −1 for all foreseeable observation). **The primordial
amplitude A_s is a lifetime parameter — the seed of structure sets the length of the breath.**
**(D) The end, re-graded — fallout #2:** the droplet is bound *topologically*; topology cannot fail
continuously → **ionization is forbidden.** The chain's last page is DAMPING: after ~10¹⁸ cycles the
Rabi amplitude decays and the atom settles into its ground state permanently — eternal de Sitter,
reached by exhaustion, protected by shape. Not a bang, not a rip — a final breath that doesn't
rebound.

---

## §14 — THE SEVEN-CARD DECK (the complete derivation frontier; operator-caught undercount, def297/t296)

The honest inventory of every un-derived quantity, with ε's corrected status:

> **ε = c · f_amp · (Ψ₀/M_red)** — currently *"structural GIVEN the c = 1 hypothesis AND the
> measured abundance."* With c un-derived over [0.5, 2], the model predicts a **factor-4 window
> [0.6%, 2.5%]** containing 1.24% — not the value itself. (Kept honest alongside the striking
> conditional fact: at c = 1, ε = 0.611 × 0.0205 = **1.25% vs observed 1.24%** — a <1% match.)

| card | quantity | status |
|---|---|---|
| 1 | the cosmic coupling → ρ_inf | WHISPER: ρ_inf^¼ ≟ ½α_c²M₂ = 1.98 vs 2.25 meV (12%, look-elsewhere ~10); teeth: produce the form, account for the 12%, prove M₂ = √(m·m̄₂) as reduced-mass rung |
| 2 | the tilt → f_amp | WHISPER-PLUS: tilt ≟ Koide 2/9 → f_amp = 11/18 = 0.6111; sims' refined plateau ≈ 0.606–0.616 (ON 11/18, <1%); 512-phase trial running; mechanism owed regardless (flat-direction rival: the plateau may be the Z4 dynamics' own constant) |
| 3 | c (the coupling coefficient) | HYPOTHESIS rounded-to-1 no longer: the #17 c=1 attractor is un-derived; a factor-4 leak on ε |
| 4 | the abundance (η ≈ 6×10⁻¹⁰) | ROUTE ESTABLISHED (§16): the charge gene through resonant leptogenesis, CP phase sourced by the helicity gene |
| 5 | the torus size L | **CLOSED-by-reclassification**: bounded (L > 27.6 Gpc = 6.3·c/H₀, matched-circles) + reclassified as **the MUTABLE gene** (topology protected; size drifts with Tolman) → **the low-ℓ sky is a cycle-odometer**, coherent with the first-cycles entropy lean |
| 6 | the see-saw scale v_L | windowed [MeV, TeV]; benchmarks built (§16); derivation open |
| 7 | the leptophilia portal | candidate embodied (§16): flavor-singlet vector-like leptons — multiplicative-universal by construction, Koide-automatic |

## §15 — THE ANALYTIC CLOSURES OF THE LAST PASS (def289/def293-299)

- **f_amp's formula:** f_amp(e) = (1 + e²)/2 — reproduces both banked endpoints (circular → ½,
  radial → 1); f_amp = 0.6 ⟺ e = 0.447. Conditionally derived (the projection-average confirmation
  owed); the value moves one rung down to the tilt.
- **T_c, the log-war ended:** RG-improvement at the thermal point μ = T gives a *stable* fixed
  point: **T_c = 0.379·m_e = 193 keV** (±50% scheme wobble). Dosage: D/H heal ≈ +0.06σ, Y_p co-pay
  **zero** (weak rates untouched). The network run remains the formal banker.
- **P-2026-024 registered:** the ε-dipole — δm_e/m_e ≈ ε·δ_DE ≈ **6×10⁻⁷**, horizon-scale,
  axis-correlated, growing at √3·H; consistent-null at today's ~10⁻⁶ reach; three falsifiers;
  the P-022 radio ratio-lock as anti-systematic companion.

## §16 — THE TRIPLE ASSEMBLY (def301): the see-saw, the abundance route, the portal

**The inverse see-saw, built:** fields (3×ν_L, 3×N, 3×S, σ); 𝓛 ⊃ y_D·L̄HN + M·N̄S + y_s·σ·S̄Sᶜ;
m_ν = (m_D/M)²·μ with μ = y_s·v_L ('t Hooft-natural); Majoron = arg(σ), f_J = v_L.
> **Benchmark A (falsifiable):** v_L = 5 MeV, m_D = 1 GeV, M = 10 TeV → g = m_ν/v_L = 10⁻⁸ —
> **inside the CMB-S4 band** → the S4 free-streaming shift becomes a live registerable falsifier.
> **Benchmark B (safe):** v_L = 1 GeV, M = 141 TeV, g = 5×10⁻¹¹.

**The abundance route (Card 4):** resonant low-scale leptogenesis is native to the (N,S)
quasi-Dirac pairs (splitting = μ); the published class reaches η ≈ 6×10⁻¹⁰ at M ~ 10–100 TeV.
The model-specific claim: **the CP phase is sourced by the genesis twist** —
> η ← ε_CP ← the net helicity (the genome's spin gene).
The dark-matter abundance = the charge gene expressed through leptogenesis. One named calc
remains: η(helicity) on Benchmark A.

**The portal (Card 7):** flavor-singlet vector-like charged leptons (E, Ē) at M_E, coupling λ to
the medium; integrating out E dresses **every** lepton Yukawa by the same factor →
multiplicative-universal **by construction** (Koide-preserving automatically); leptonic + colorless
→ quarks untouched at tree. Scale: λ²⟨A²⟩/M_E² ≈ 1.2×10⁻². Census-legality pass + collider
phenomenology owed.

*Ledger note (t296/t298): standing ≈ 14–17%; the banked structural results (DM+DE reduction,
C_ref hinge, √3, reading B, gate-0 clearance) are unaffected by the ε-softening; the live movers
are the 512-run, the omk minimum, the chains, and DESI DR3 above all.*

## §17 — THE RADIO NIGHT (2026-07-11): the production BBN verdict, the trace grammar completed, the radio audit's two bills

**The production BBN verdict (clean PRyM, m_e set before import — def325/329):**
- ∂ln(D/H)/∂ln m_e ≈ 0.000 (the network's competing terms cancel) → the full 1.24% dyad moves
  D/H by +0.0004%: **gate-0 safety is ABSOLUTE at production grade.** The D/H "pharmacy"
  (def253/255's hand-rolled sign chain) is DEAD — retired by the real network.
- ∂ln Y_p/∂ln m_e ≈ −0.72 → the dyad LOWERS Y_p: 0.24689 (+0.5σ vs Aver) → 0.24468 (−0.2σ).
  **Y_p is the true medicine (+0.65σ); the fingerprint lattice's one counter-lean FLIPS favorable.**
- The η route (the scar was never set by BBN): the dyad's CMB fit pulls ω_b UP +1.1% vs its own
  ΛCDM control (0.022757 vs 0.022517, same data — the m_e–ω_b degeneracy). D/H ∝ η^(−1.6):
  **own-ΛCDM D/H = 2.420e-5 (1.59σ below Cooke 2.527±0.030); dyad = 2.372e-5 (2.31σ).**
  The dyad OWNS the widening as a signed discriminator (P-2026-027): dyad 2.372 / ΛCDM 2.420 /
  quasar-optical 2.527 — the radio deuterium arbiter decides.
- **The radio deuterium arbiter (P-027):** D I hyperfine at 327.384 MHz (91.6 cm) — deuterium's
  own 21cm. Dark-ages D/H absorption against the CMB (the only backlight older than the first
  pulsar/quasar/BH): no astration, no quasar optics, no BBN network in the measurement. The dyad
  signs the instrument: both dark-age lines (z>50) shift **+2.50%** ((1+ε)², hyperfine ∝ m_e²)
  while the ratio **ν_H/ν_D = 4.338649 is EXACTLY preserved at every z** — the two-line
  ratio-lock (universal-m_e-only signature). Kill: radio primordial D/H at 2.53, or an unlocked
  ratio. EDGES addendum: if the EDGES over-depth is a real synchrotron background, the D line at
  18.2 MHz sees it amplified ×45 (spectral leverage (78.9/18.2)^2.6) → ~×46 over-deep: the
  D-line is the three-way EDGES discriminator (systematics / early compact objects / relic —
  relic already declined by the crunch null).

**The plasma trace (the fifth threshold — def331/t328 banked):** a photon in plasma is massive
(ω² = ω_p² + k²c², m_γ = ħω_p) and hence NOT traceless: trace fraction (ω_p/ω)². Radio near ω_p
is the ONE part of the EM bath the trace-bus can see — light itself two-fluids in frequency
space. The one threshold now sorts FIVE sectors: Landau (coherent/dissipative), Landauer
(fee-exempt/fee-paying), trace-bus (trace/traceless), the vacuum cap (sub/super-gap), and light
(sub/super-ω_p). The crunch's mouth: as density rises, ν_p sweeps up through the radio bands
(~900 MHz at n_e ~ 1e10 cm⁻³) — each band is massed, then thermalized: the before-genesis null's
mechanism. (The 1/m trace-ownership — electrons 99.95%, protons 0.054% — is banked
SUGGESTIVE-ONLY for leptophilia: in-medium dressing ≠ vacuum rest-mass; Card 7's candidate stays
the vector-like portal.)

**The radio audit's two bills (def333/t330):**
- **Meissner (paid on the spot):** any EM charge on the condensate Higgs-es the photon:
  m_γ² = 2q²n/m. Halo density + photon-mass limits force **q_EM < 4.7×10⁻³⁸ … 4.7×10⁻⁴⁷** —
  EM-neutrality is FORCED by 25–45 orders, not chosen (the birefringence null upgraded to
  structurally mandatory).
- **Magnetogenesis (P-2026-028, opened):** ΛCDM cannot seed cosmic B at linear order (no
  primordial vorticity); PRTOE is a rotation machine. Harrison: B ≈ 2(m_p c/e)·ω_vort →
  **~5×10⁻¹⁸ G at ω_vort = 0.5 H(rec)** — pays the GALACTIC bill (dynamo amplifies).
  Honest gap: the void floor (blazar ~1e-16 G) sits ~1.5 orders above smooth-Harrison
  (candidates: vortex-network structure, persistence, blazar caveats). The field's magnetic
  HELICITY is signed by the genome.

**The omk return (def333):** minimum at H0 = 68.99, Ω_k = −0.0046, m_ncdm = 0.071 eV — the data
DECLINE curvature-as-H0-escape (pre-registered pull to 71–73 did NOT appear; booked half-wrong
against ourselves). The trilemma resolves to (c): the flat torus stands, the ~69.5 residual is
owned. P-023's nonzero-Σm_ν preference holds with curvature freed.

## §18 — THE LOCALIZATION CLAUSE COMPUTED (def337/t334): the DE-floor VALUE from zero dials

**The bridge (t320's owed item, discharged):** the Landau criterion's mode-decay form: a
collective mode Landau-decays into the pair continuum at ω ≥ 2Δ, and for a bound pair
**E_b = 2Δ** (the energy to break one pair) — the pair-breaking threshold IS E_b, exactly
(BCS: the amplitude mode sits at 2Δ; sub-gap phonons protected).

**Why not M₂⁴ (no double counting):** above E_b the excitations are BROKEN PAIRS = the
two-granule continuum = the MATTER sector, already counted in the a₀-packing/DM branch (§15's
fork repair). The vacuum budget integrates ONLY the genuinely-collective sub-gap sector; the
cutoff is where the field stops existing as an independent degree of freedom. **Scope (t334,
cold):** this derives the MODEL's collective-field floor at E_b⁴-scale — it does NOT solve the
CC problem writ large (SM vacuum energy untouched; sequester dead t230).

**The budget (honest prefactor):**
    ρ_vac = ∫ d³k/(2π)³ · ½ω,  ω = c_s k,  up to ω_max = E_b
          = E_b⁴ / (16π² c_s³)
with the BEC relation c_s = √(gn/m), gn ≈ α_c m → **c_s = √α_c = 0.146** (a relation, not a dial):
    ρ_inf^¼ = ½α_c²M₂ / (16π² α_c^{3/2})^{1/4} = **2.695 meV vs banked 2.25 meV — 20% off,
    ZERO free dials** (α_c = 0.0214 and M₂ = 9.87 eV both banked upstream).
The old "0.4% match" (ρ = E_b⁴ with no prefactor) is RETIRED as prefactor-naive. The 20% is the
new honest O(1) (refinement candidates: the gn ≈ α_c m identification, dispersion curvature near
the gap, c_s running). **Standing moved 14–17% → 15–18% on this turn (t334): of the two headline
numbers, ε is a draw and ρ_inf is a derivation.**

## §19 — THE FIRST DRAW (def335/def339): the dice, the cycle map, the winding sector

**The one-draw result (t332):** composing the first-roll-at-rest theorem with the
self-generating Z4 tilt: ω_genome is the first roll's OWN OUTPUT, and the universe is one draw
of one angle θ_i. Computed: f_amp(θ_i) is CHAOTIC-BROAD ([0.034, 0.964]) — the banked
release-angle chaos made quantitative. t332 verdict: ε is a draw; the derive-ε ladder
superseded. Koide 11/18 reachable WITHOUT inherited spin (20/64 of the domain below it) but not
pinned (multiplicity) → the last stand = a joint over-constrained check (Koide + η + B-helicity
on one θ_i).

**The winding sector (def339, APPEAL FILED — pending grade):** the model's stone: find the FIRST
draw's starting conditions. Proposed: the first genesis lives in a topologically twisted sector
of the torus (n ≠ 0 winding; n = 0 has no genome — nothing conserved to inherit; minimal
nontrivial n = 1). Winding forces the phase to sweep ALL angles across space at EXACTLY uniform
measure; gradient energy (2π/L)²R² is negligible at horizon-scale L → patches roll
independently → **the observable f_amp is the WINDING AVERAGE — a determined number, not a
draw**:
    f̄ = 0.6438 ± 0.0305 (64-pt; 512-pt precision pass grinding)
    → implied c = 0.581/f̄ = 0.90 ± 0.04;  Koide 11/18 = 0.6111 sits 1.1σ away (compatible).
**The helicity separates:** the roll-averaged net helicity VANISHES over the winding (Z4
antisymmetry; measured ⟨L⟩ ≈ −0.006) → the universe's net helicity is the WINDING CURRENT
itself: topological, QUANTIZED (n = 1), v = 2π/(mL) — ω_genome is a derived discrete object,
feeding the η route (Benchmark A needs sin φ × κ ≈ 4×10⁻⁷, i.e. φ ≈ 4×10⁻⁵ after Hubble
damping) and the B-helicity sign (P-028).

*Ledger note (2026-07-11): standing ≈ 15–18%, operator-capped at ~25% until PolyChord
confirms/denies the Laplace ΔlnZ = +2.635. Gate-0: production-absolute. The C-code gate now
reads "PolyChord favorable + gate-0 bank." Live movers: the winding 512-run, the cycle map, the
chains (routeD/conv_desi), the η(winding-current) calc, and DESI DR3 above all.*

## §20 — THE c-WAR'S END-STATE (def357–def407): from free O(1) to one pending measurement

**The reductions, in graded sequence:**
- **c's identity** (def357/t358): c = (λ√(Ψ₀M_red)/M_E)² — Cards 3+7 merged (the geometric-mean
  portal scale). **Leptophilia DERIVED** (t358): a conformal/mass coupling hits Higgs-sourced
  masses full, QCD-composite at the ~6% quark fraction — ×16 hadronic suppression from the SM's
  own mass structure; the portal demoted to the seesaw μ-term. Bonus registered: the quark-bleed
  ~1σ D/H nudge.
- **The sum-rule class** (def365/t362): "continuous ⇒ unprotected" is FALSE — TRK-class sums are
  quantum-protected. Red-team conceded its dichotomy.
- **The commutator named** (def367/t364): the f-sum rule ∫ωS dω = Nk²/2m from [ρ,[H,ρ]] on the
  founding pair [θ,N] = i — "the search is over." **f_amp's meaning fixed: the amplitude
  branch's share of the protected spectral weight.**
- **FM-B closed** (def371/t368): the zeroth moment is bracketed by the compressibility sum rule;
  the bridge frequency ω̄ = c_s·k with c_s = √α_c — derived, not free. Surviving leak: FM-A
  (no shared charge → the trace-vertex coefficient), plus FM-C accepted as the reduction:
  **c = d ln m_e/d ln|Ψ| — 1 iff m_e is linear-and-sole-sourced in |Ψ|.**
- **The 9/10 arc** (def375–def383/t372–t380): pre-registered, hit dead-center in f̄-space,
  then honestly dismantled — circularity (c ≡ 0.581/f̄), the α_c band (±5%), the counting
  candidates broken (tensor-count inverted: mass is a scalar → the trace, 1/10 not 9/10;
  the ten-channel count boson-omitted). **Blindness → universality GRANTED as theorem; the
  value not fixed.**
- **The step-vs-ramp rule bites everything** (def387–def407): the operator's catch — f_amp is a
  PARTITION of a rolling field and AGES. The measure is LOCKED (topology), the partition ramps
  (t388-graded: "genuinely dissolves the contradiction"). THE RAMP RAN (six octave windows to
  t = 2240): **f̄ declines 0.655 → 0.635 and FREEZES by t ~ 300: f̄(rec) = 0.635 ± 0.026.**
  Early-window numbers were biased +0.015–0.02. The c=1 exclusion softens to
  disfavored-not-dead (1.1–2.1σ across the α_c band).

**THE STANDING STATE: c = 0.92 ± 0.05 (all-in).** The rationals (11/12 at 0.03σ, 9/10 at 0.3σ,
19/20, 1) are INSEPARABLE. α_c's ~5% band (all of it the fluid-mass m via Ψ₀ ∝ m^(−1/4)) is the
sole decider: **σ(α_c) ≤ 2% ⟺ σ(m) ≤ 8% ⟺ σ(z_on)/z_on ≤ 4%** — THE ZON INSTRUMENT
(cmp_prtoe_zon: dcdf_z_rad_onset freed, log-prior [6.5, 8.5], RUNNING). The order-parameter
answer holds α_c step-safe (t392: one ramp only, ε(BBN) epoch-structure flagged); the tie
(Field-1 Ψ₀ ↔ Field-2 vev) stays the orange joint.

## §21 — THE MYSTERY WING + THE KEYSTONE (def411–def415): five documents, one debt

Filed as standalone documents, each derivation-from-banked with owed items bare, all graded
coherent (t408/t410/t412): **black holes without singularities** (ξ = ħ/(m c_s) = 402 AU —
every BH below ~2×10¹⁰ M☉ fits inside ONE healing length; the quartic/CSW collapse floor; the
Landau-broken thermal core; Penrose discharged at premises), **the big bang without a
singularity** (the bounce at the quartic floor; the vacuum first-genesis — a state, not a
point; creation energy = 0 by the torus theorem), **the arrow of time** (the Past Hypothesis
answered by UNIQUENESS — the vacuum start needed no draw; the arrow = the graded gravity-account
ledger), **the information paradox** (dissolved-not-calculated: no shredder, unitary core, the
ledger cannot un-record), **cosmic magnetism** (structural vorticity pays the galactic bill;
the void column OPEN; **the signed-helicity falsifier: sign(helicity_B) = sign(n) = the
matter/antimatter draw — three predictions, one axis** with P-024 and P-029).

**THE KEYSTONE (t410): task #11 — derive S = A/4 from the condensate's horizon entanglement —
now underwrites FIVE structures** (Jacobson's route, the BH core's entropy, the Page curve,
the emergent frame, the arrow's rigor). One derivation, five doors.

**Also in this era:** the quantum wing filed at its graded sizes (gravity: the coherent frame +
the 20% receipt; entanglement/tunneling/superposition: interpretation-tagged, null-prediction,
Tsirelson-exact as the permanent kill-line). η (Card 4) reframed to a defined Boltzmann solve
(K = Γ_N/H = 9×10⁷ computed; the crude scalings straddle 6×10⁻¹⁰; the domain-sign gate owed).
The winding comb registered (P-2026-029: ℓ_mod ≈ 6.4n, the shared axis). The provenance
correction (def409/t406): the "model-relayed" hints were the operator's own intuitions — zero
retroactive change, "the proof is the kill list."

*Ledger note (2026-07-11, post-radio-night): standing ≈ 15–18% (operator-capped 25% pending
PolyChord). Live deciders: the zon posterior (α_c → the fraction), DESI DR3, PolyChord, the
routeD/conv_desi pre-registrations, the area-law keystone, the Boltzmann solve.*
