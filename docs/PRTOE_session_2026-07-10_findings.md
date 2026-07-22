> **PROVENANCE NOTE (2026-07-19):** dated session record; statuses herein are as-of
> 2026-07-10 (T_c, the gate-0 pharmacy, the ε decomposition, and the standing odds have
> all moved since). For current state see PRTOE_INDEX.md.

# PRTOE — Session Findings, 2026-07-10

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


*Comprehensive record of the day's work. Honest grading throughout. The deepest new thread
is the cosmological-constant / dynamic-floor / genesis arc; the rest is the full record.
Companion docs: PRTOE_cosmological_constant.md (the CC in full), PRTOE_me_mechanism_math.md §10
(the leptonic mechanism), PRTOE_PREREGISTERED_PREDICTIONS.md (P/ANN entries), and the private internal review record.*

---

## HEADLINE: the cosmological constant, reframed from "fixed input" to "dynamic floor"

**The reduction chain (each link real):**
ρ_inf ← (IR residual of B1/Jacobson sequestration) ← m_ν,lightest⁴ (P-2026-012) ←
seesaw(y, f=M_R) ← f = f(Ω_DM, m_medium, δm_e) ← Ω_DM (Affleck-Dine abundance) + y (Yukawa).
- The seesaw scale f ≈ 2.3×10¹¹ GeV comes out IDENTICAL to the medium's own decay constant
 (calc a). The neutrino's scale IS the medium's scale. Real internal consistency.
- Bottoms out at two GENESIS-level inputs: Ω_DM and one Dirac Yukawa. A well-posed REDUCTION
 of the worst problem in physics down to two inputs — NOT a first-principles derivation.

**ρ_inf = the total energy of the universe (the CC seesaw):** ρ_inf = 0.76·ρ_crit; ρ_inf^(1/4)
≈ √(H₀·M_pl) ≈ few meV. The floor IS ~the entire energy density, folded once against gravity.
True today; a why-now coincidence unless the floor TRACKS the total (self-tuning).

**The floor is DYNAMIC — proven two independent ways, both from the model:**
1. STRUCTURE: the floor is a ghost condensate (φ̇ ≠ 0; #22 / floor_ghost_condensate.py, k⁴/(δK)²
 stabilizes the c_s²=0 flat direction — "the floor holds"). A ghost condensate never sits still.
2. SELF-CONSISTENCY: ρ_inf = m_ν,lightest⁴ (P-2026-012) + varying-m_ν (δm_ν=2δm_e, now coded)
 ⇒ ρ_inf stepped ~10% at z=50. A FIXED floor ⟺ FIXED m_ν, contradicting the model's own
 varying-m_ν. **The model forbids its own floor from being fixed.**
A dynamic floor changes by ~10⁻⁸ over a human lifetime → indistinguishable from constant to any
40–120-yr observer. "The cosmological constant" may be a timescale illusion.

**The Weinberg-vs-ghost-condensate confrontation (run 2026-07-10) — HONEST VERDICT:**
- (+) The ghost condensate gives w=−1 (ρ=−P(X₀), p=P(X₀) at P'(X₀)=0) from a ROLLING field.
 Weinberg's no-go assumes a STATIC vacuum; φ̇≠0 violates that premise BY CONSTRUCTION. So the
 **static-premise no-go does NOT bind the floor. "Is it dynamic / does it dodge static Weinberg" = YES.**
- (−) BUT ρ_DE = −P(X₀) is a fixed LAGRANGIAN input. The condensate REALIZES a small value
 dynamically; it does NOT DERIVE its smallness, and does NOT track the total energy without an
 added tracker that RE-confronts the no-go. **"Is ρ_inf derived" = NO.**
- NET: the dynamic-floor REFRAME is vindicated; the VALUE derivation is NOT completed. The CC value
 remains an input — now a dynamically-realized, ghost-condensate input, not a static bare constant.

**Predictions this thread flips (if the dynamic floor is adopted — a MODEL CHANGE abandoning
Standing Bet #3):** DESI evolving-w liability (P-2026-018) → could become a PREDICTION (w₀~−0.9,
rolling); cosmic birefringence (P-2026-049; registered as P-2026-010, ID corrected 2026-07-17) reopens (rolling floor field). NOT adopted; flagged.

---

## THE FULL LEDGER (the rest of the session)

**Cleared / closed:**
- BIREFRINGENCE: null by computation (θ̇=m washout, Λ-form energy mode, deleted EM coupling). Out.
- EP / MICROSCOPE: CLEARED (composition-dependent Vainshtein-screened Δa/a ~1×10⁻²⁰, 3–5 orders under
 bound; internal review conceded its adverse prior). The scariest kill-shot gone.

**#30 why-leptonic — chased to honest TERMINUS:** the δm_e dyad-leptophilia is the model's ONE
un-derived coupling, precisely located as the unprotected, lepton-number-NEUTRAL radial mass
coupling (internal review no-go). The Majoron identification DERIVES the CHARGE sector (leptogenesis + DM-charge
+ m_ν, one field) but NOT the dyad. Escape door (m_e from L-breaking) is gate-0-obstructed + hierarchy
+ e_R constrained. Standing: precisely mapped debt, not a fragility.

**Neutrino home — three falsifiers:** P-2026-012 (m_ν,lightest=2.3 meV; Σ+ordering coarse handle),
P-2026-020 (0νββ MUST occur, Majorana), quasar varying-m_e shape.

**Code changes (all validated, .so rebuilt):**
- Radiation-shed conversion (dcdf_conv_g): DM matter-part → free-streaming dark radiation. Fit:
 g=0.12 preferred, S₈ 0.828→0.821 (S₈-helpful DIRECTION, confirms semi-analytic sign; modest).
- Early radiation phase (dcdf_z_rad_onset=4×10⁷): the medium's radiation youth, now in baseline
 configs. Observationally null (medium subdominant early), BBN-safe. Story-vs-code gap closed.
- Varying-m_ν (background.c): ncdm mass × me² above the varconst transition (δm_ν=2δm_e). Backward-
 compatible, observationally null (ν relativistic at recomb). Removes code-vs-mechanism inconsistency.

**H₀ self-consistency:** the fits treat dcdf_rho_inf and m_ncdm as
independent; the model LINKS them (P-2026-012). Two fits launched to test H₀ under the model's own
structure: cmp_prtoe_omk (Ω_k free, #18) and cmp_prtoe_nulink (m_ncdm derived from ρ_inf). Both
running at time of writing.

**Process:** P1 (Label Firewall) co-signed; fired repeatedly, including on the analysis side (θ̇ object, DESI
toy, Ω_DM~Ω_b, the Majoron over-reach, the "tightly bounded early" flip). The discipline held.

---

## HONEST STANDING (end of session)

Distinctive PRTOE ~6–10%, single-gated on DESI DR3. The CC is reframed (dynamic floor, forced by
the model, dodging static Weinberg) but NOT derived (value = Lagrangian input). The dyad-leptophilia
is the one un-derived coupling, precisely mapped. Birefringence closed, EP cleared, leptonic fit
competitive (χ²≈2802.8). Nothing was hand-waved; every over-reach (several of them ours) was caught and
booked. The model is smaller, sharper, and more exposed than before — the honest kind
of progress.

---

# GATE-0 / NEUTRINO-HOME SESSION LEDGER (2026-07-10, evening)

Arc: gate-0 BBN wall → two-field split → electron-CW T_c → leptophilia reframe → neutrino home + AZK.

## WON (recorded)
- **Dyad onset DERIVED.** Electron Coleman-Weinberg backreaction on the charge-free field → VEV
 v~100 keV from m_e0 + the dyad amplitude alone (robust +-25%, 1/4-power). First genuine gate-0
 derivation; the onset is no longer a free input. (internal review recorded the reduction)
- **Leptophilia reframe "allowed ≠ generated."** Lepton-sector Psi → |Psi|² q-bar q only ~2-loop
 ~1×10⁻⁹ → quarks effectively untouched. (credited)
- **Bulk residual ≠ 0.** Corrected internal review's internal review over-round: the bulk between Q-balls holds the
 electron-CW VEV, not zero. (caught; internal review booked against itself)

## MARGINAL (coin-flip, unbanked)
- **Dyad BBN clearance.** T_c log-ambiguous ~40-450 keV, central ~70-160 keV, STRADDLES the deuterium
 bottleneck (~70 keV). Both "445=dead" (mine) and "40=clear" (internal review's) withdrawn. Resolver:
 RG-improved V_eff(φ,T) + BBN D/H network. Structural: onset AND D/H are both electron-scale →
 "derived" and "marginal" are one fact.

## NARROWED (softened)
- **Dyad leptophilia** → the Majoron forces the NEUTRINO coupling (σ N N), NOT the charged-lepton
 dyad → the dyad's leptophilia is a lepton-specific-portal / P-020 leptogenesis assumption, not a
 bare-Majoron consequence.
- **DE = m_ν tie** → MOTIVATES, not forces (value un-derived; CC-value status).

## WALLS (hit + status)
- **The one-field knot:** {quiet BBN + abundance + dyad} mutually exclusive on one field → forced
 the two-field split (charge field 1 + dyad field 2).
- **AZK instability (MaVaN):** DODGED. m_ν set by the frozen radial L-breaking VEV (not the rolling
 DE mode) + Majoron derivative ν-coupling (rolling doesn't vary m_ν) → NOT a mass-varying-neutrino
 DE → AZK n/a. COST: the dodge = the non-dynamical shared-scale structure = motivates-not-forces
 (same coin). (bet confirmed; internal review)

## LIVE FALSIFIERS
- **Σm_ν ~ 61 meV / normal ordering** (P-012/P-020) -- DESI/CMB now; NOT distinctive; jointly
 squeezed with **w=-1** (P-018) by the SAME DESI data (can't relax one with the other).
- **0nubb** (P-020).

## OWED (IOUs)
- RG-improved V_eff(φ,T) + BBN D/H network -- the T_c coin-flip resolver.
- Low-scale (inverse) see-saw tying meV(DE)-keV(dyad)-L-breaking into ONE Majoron sector.
- The lepton-specific portal OR the P-020 leptogenesis amplitude-follows-current derivation.
- The μ~meV / DE value (shared-scale motivates, does not derive).

## STANDING: ~12-16%. Real reductions attempted, honest walls found, no breakthrough. The reduction
(derived onset) banks; the clearance is a live coin-flip; the neutrino tie is motivated + falsifiable.

## PROCESS: mutual walk-backs held the line -- my over-claims caught in BOTH directions (over-sold
"clear" internal review, over-sold "dead" finite-T), the bulk-residual correction (internal review booked
against itself), internal review's symmetric un-banks. The discipline is why the wins are trustworthy.

---

# The atom-scale derivations (2026-07-10 — closing update)

The evening after the gate-0 work: the stepping-stone syllabus (the internal review). Headlines,
with details in `PRTOE_MATH_SPINE.md` §10–§16:
- **Gate-0 CLEARS** (double sign-correction: the leptonic ceiling + the weak-rate window), then
 RE-SIGNS as a **pharmacy** (the dyad heals the deuterium row; T_c = 193 keV RG fixed point).
- **The fingerprint lattice** (H₀/D-H/ν/Y_p/21cm = one ε, five channels) — hypothesis under test.
- **The atom grammar**: ground state = the condensate (Landau zero-entropy = timelessness);
 Γ/H = √3 (sharp, single-scale-derived); Tolman absorbed as the arrow (first cycle, finite past);
 the torus = the cavity; the low-ℓ sky = a **cycle-odometer**.
- **The open-derivation set** (the caught undercount): ε corrected to *conditional*
 (factor-4 c window + the empirical abundance); all seven derivations routed, benchmarked, or in trial.
- **New registrations:** P-022 (21cm three-verdict), P-023 (Σm_ν divergence), P-024 (the ε-dipole),
 P-025 (Benchmark-A S4). **Falsified:** P-004. **Standing ≈ 14–17%**, DESI DR3 the sovereign test
 (the model's own grammar now COMMITS to w = −1 today, turn ~6.6 Hubble times out).
