# PRTOE — THE MATH SPINE (genesis → now → end)

*2026-07-10. The full quantitative chain in one document: every epoch, its governing equation,
what is DERIVED vs INPUT vs STORY, and where it lives in the code. Cross-references:
PRTOE\_me\_mechanism\_math.md (dyad detail), PRTOE\_cyclic\_torus\_genesis.md (genesis narrative),
PRTOE\_UV\_completion.md (#17), PRTOE\_cosmological\_constant.md (J1), ForClaude.txt turns 180–224.*

**Status tags:** \[DERIVED] falls out of prior pieces · \[INPUT] boundary datum · \[STORY] coherent
mechanism, not a derivation · \[PENDING] computation named, not run.

\---

## 0\. The objects

One dark superfluid, two components (the two-field split, t186–190):

* **Field 1** — the dcdf fluid: charge/abundance carrier, DM+DE unified. Mass m = 2.24×10⁻²⁰ eV
\[DERIVED from ε and c=1: c(m) = (m/2.24e-20 eV)^{1/4}].
* **Field 2** — the dyad field: charge-free, couples to the electron; its condensate sources
δm\_e. (The Majoron/lepton-sector identity: tree coupling σNN → neutrinos; the charged-lepton
portal is a UV assumption \[PENDING #30].)

The amplitude (the model's one distinctive number) \[DERIVED, #11]:

> \*\*ε = c · f\_amp · (Ψ₀/M\_red) = 1.24%\*\*, with f\_amp ≈ 0.6 (genesis dice, mechanism-confirmed),
> Ψ₀/M\_red = 2.05% (abundance-pinned), c ≈ 1.

## 1\. Genesis (the cycle's start) \[STORY]

Torus topology survives the bounce (topology holds what dynamics loses); the confined heat
fountain (blueshifted crunch radiation) rolls up into a helical vortex ring → re-seeds the twist.
Flat 3-torus registered as P-2026-013. **BKL and Tolman stand against the bounce rungs — this
layer is a story built from real mechanisms, not a derivation.**

## 2\. Radiation youth → dark matter (the first transition) \[DERIVED identity]

Above H ≈ m the ultralight field is frozen/radiation-like (w=1/3, the #17 conformal-origin
phase); below, it oscillates as dust. The switch epoch:

> \*\*T(H=m) = √(m·M\_red / 0.61) = 9.41 keV\*\* (g\*=3.36) ↔ \*\*coded z\_rad\_onset = 4×10⁷ → T = 9.39 keV.\*\*

Match 1.002×. The onset is field 1's H=m clock — textbook ULDM — NOT a condensation temperature
(t182's "internal inconsistency" dissolved, t216, booked both columns). Code: `dcdf\_z\_rad\_onset`
(background.h, with the derived-identity comment).

**Two jobs, one clock** (operator, 2026-07-10): the ending regime reaches its floor (conformal
protection ends) while the starting regime crosses its threshold (dust/DM behavior begins). In
code this is literally one function: `dcdf\_rho\_rad`'s f(a) = x²/(1+x²) fades the radiation while
the dust part continues, amplitude fixed by continuity (no free knob).

## 3\. The background fluid (radiation → dust → de Sitter) \[DERIVED form; ρ\_inf INPUT]

> \*\*w(ρ) = −e^{−s}, s = ln(ρ/ρ\_inf) clamped ≥ 0  ⟹  P = −ρ\_inf exactly.\*\*

So the background is ΛCDM-form: ρ = ρ\_inf + C·a⁻³, algebraically (verified to 10⁻¹⁶, t211).
w = −1 is EXACT for the constant floor — not a step artifact, not rampable. Code: `w\_dcdf` /
`dcdf\_s\_of\_rho` (background.h).

## 4\. The dyad turn-on (field 2 condenses) \[DERIVED onset; clearance CLEARS]

The electron Coleman–Weinberg backreaction on the charge-free field (m\_e(φ) = m\_e0(1+κφ²)):

> V\_CW = −(1/16π²)·m\_e(φ)⁴·\[ln(m\_e(φ)²/μ²) − 3/2] → tachyonic curvature → radiative SSB
> \*\*VEV: v = m\_e0·\[ε(L−1)/4π²]^{1/4} ≈ 100 keV\*\* (81/102/121 keV for L−1 = 2/5/10; ±25%, robust)
> \*\*T\_c = m\_e0·√(3(L−1)/2π²)\*\* — κ cancels; log-ambiguous \*\*\~40–450 keV\*\* (leading-log unstable
> near the flat direction; RG resummation = task #40).

The onset is DERIVED from m\_e0 + ε alone (the first gate-0 reduction, banked t192/194).

**BBN clearance \[CLEARS, t213/214 — the double-P1.c correction]:** the deuterium constraint's
severity decomposes by process: weak rates n↔p (T \~ 500–1500 keV, \~75% of the m\_e lever),
n-decay phase space (\~10%), e± heating (\~10%), the bottleneck itself (\~5%, B\_d nuclear,
m\_e-insensitive). The dyad (T\_c ≤ 445 keV) NEVER touches the weak-rate window; AND the dyad is
LEPTONIC (quarks \~2-loop, \~10⁻⁹), whose full-BBN ceiling is \~0.3–1σ (t144), not the universal/
hadronic 12σ:

> \*\*effective tension = (temporal exposure 0.05–0.25) × (leptonic 0.3–1σ) ≈ 0.02–0.25σ → QUIET.\*\*

"When D forms" ≠ "when m\_e matters" — two different electron-scale clocks. Code: the dyad window
`varconst\_transition\_redshift < z < varconst\_z\_high` (`varying\_z\_high`, new 2026-07-10; ≤0
recovers the plain step). #40 (RG V\_eff + BBN network) CONFIRMS, not decides.

## 5\. Recombination → today \[the fitted era]

m\_e shifted by ε = 1.24% inside the window (H0 fix; ΔlnZ = +2.635 Laplace, SHOES-conditional);
screening returns m\_e → standard below z ≈ 50 \[INPUT form, densities-dependent screening owed].
Optional rotation-shed `dcdf\_conv\_g` (S8: minimizer picks g = 0.12, S8 = 0.821 vs KiDS 0.814).
Corrected A2 (t223): the shed's apparent-w mirage is \~1% — OUT as a DESI driver; the S8 job
survives (background ρ\_m, not the w-mirage).

## 6\. The neutrino home \[relation DERIVED-candidate; value INPUT]

Ψ = Majoron (L-breaking Goldstone): tree coupling σNN → Majorana m\_ν → **0νββ must occur**
(P-2026-020); **Σm\_ν ≈ 61 meV, normal ordering** (P-2026-012; whisper won the pre-registered
collision vs P-2026-004, which is FALSIFIED, ANN-2026-021). The tie:

> \*\*ρ\_inf^{1/4} = m\_ν,lightest = 2.25 meV\*\* — shared-scale (one L-breaking spurion candidate),
> AZK-SAFE (m\_ν set by the frozen radial VEV + derivative Majoron coupling — not MaVaN).

Value un-derived; spurion identification = task #43 (dimensionally non-trivial: ε dimensionless
vs μ dimensionful); post-hoc flag on the mechanism until a NEW falsifiable consequence (#41).

## 7\. NOW → THE END (the forward map) \[Route D: mechanism + pre-registration branch]

**7a. The sequestered floor \[J1 converted, t217–218 credited].** On a FINITE universe (compact
torus × finite cycle — the model's native structure = Kaloper–Padilla's entry requirements):

> \*\*Λ\_eff ≈ ¼⟨T^μ\_μ⟩₄ᵥₒₗ ≈ (3/4)·ρ\_m(turnaround)\*\* (radiation traceless; a³-weighting → latest epochs)
> Λ^{1/4} = 1.71 meV at turnaround \~now (vs 2.25 observed, 0.76× — right decade FROM A MECHANISM).

"Why 2.3 meV" + "why now" → ONE question: why turnaround \~now. Weinberg's no-go dodged legally
(finite 4-volume). \[PENDING: the KP self-consistency solve — toy-level O(1)s.]

**7b. The thaw \[the forced consequence].** Observed Λ ⟹ turnaround within \~an e-fold ⟹
**m\_J \~ (1–3)H₀** ⟹ the floor is thawing NOW:

> \*\*1 + w\_floor(a) = thaw · a³\*\* (thawing growth), net apparent CPL (with the shed at g=0.12):
> \*\*(w₀, wₐ) ≈ (−0.92…−0.86, −0.2…−0.5)\*\* — thaw-side, NO true phantom ever.

Code: `dcdf\_floor\_thaw` (new 2026-07-10; ≤0 recovers w = −1 exactly). ρ\_floor(a) =
ρ\_inf·exp\[thaw·(1−a³)]; E(a) = ρ\_floor − ρ\_inf added background-only (pattern of dcdf\_rho\_rad).

**7c. The branch \[to be pre-registered, guards owed t222/224]:**

> \*\*P-2026-018 (w = −1 exact) XOR Route-D (thaw-now, w₀ ∈ \[−0.92,−0.86], wₐ < 0, no phantom).\*\*
> DESI DR3 adjudicates: thaw-side → Route-D (J1+why-now+DESI in one stroke, P-018 dies);
> rigid → P-018 (distinctive win; Route-D dies, J1 reverts to constitution);
> TRUE phantom in the DATA → both die. Guards: distance-space phrasing, KP solve, timestamp
> (ForClaude: def217 J1-derivation precedes def219 DESI-convergence), A2+A3 net (answered t223).

**7d. The end (and the next start).** The thaw completes → expansion reverses → contraction
blueshifts radiation (a⁻⁴ grows) → the heat fountain reignites → T climbs back through **T\_c**
(the SAME derived T\_c of §4) → **the dyad condensate MELTS** (m\_e → standard for the crunch) →
charge survives in solitons/Q-balls \[requires gravity-mediated K<0, t186–190: fragmentation
banks the charge at T \~ 10¹⁰ GeV, 13 decades before any melt] → torus topology carries the axis
across the bounce (rotation resets, topology doesn't) → re-expansion cools through T\_c → the
condensate RE-FORMS → §1. **The condensate breathes; T\_c is both the recombination-era turn-on
and the crunch-era melting point — one number, both jobs** (the operator's two-jobs law, §2).
\[STORY at the bounce rungs: BKL, Tolman unresolved.]

## 8\. The two-jobs pattern (operator's law, 2026-07-10) — and where the code reflects it

Every transition is ONE clock with TWO jobs — the ending regime reaches its floor, the starting
regime crosses its threshold:

|transition|job 1 (floor reached)|job 2 (threshold crossed)|in code|
|-|-|-|-|
|H=m (z=4e7)|conformal youth ends|DM (dust) begins|`dcdf\_rho\_rad` f(a): one function fades radiation as dust continues, continuity-matched|
|T\_c (dyad)|thermal disorder dies|condensate/δm\_e turns on|`varying\_z\_high` edge (2nd-order: no latent budget to hand off — a pure switch is CORRECT here)|
|ρ→ρ\_inf (z\~0.7)|matter dilution bottoms|de Sitter begins|`w\_dcdf(ρ)`: one barotropic function does both automatically|
|shed|matter-part drains|dark radiation grows|the SAME `conv` term, opposite signs, in two ODEs (background.c:2843-45) — the pattern literally|
|thaw/turnaround|the floor era ends|the turn begins|`dcdf\_floor\_thaw` (new)|

The conservation-pair transitions carry the two jobs as one term with two signs; the
second-order (continuous) transition carries them as one edge with no budget. **The code
reflects the law wherever the law demands it, and correctly does NOT fake a hand-off where
the physics has none.**

## 9\. Ledger (what this spine rests on)

**Banked:** DM+DE unification (2→1); ε derived (#11); onset = H=m identity; dyad onset derived
(electron-CW); gate-0 clearance (double-P1.c, pending #40 confirm); AZK-safety; leptonic
allowed≠generated. **Falsified:** P-2026-004 (high Σm\_ν). **Live falsifiers:** DESI DR3 (the
branch), Σm\_ν ≈ 60 meV, 0νββ, void/IGM m\_e-step (P-007, J4). **Owed:** KP self-consistency
(#46), #40 confirm, low-scale seesaw (#42), spurion identification (#43) + new consequence
(#41), leptophilia portal (#30), DE value if Route-D dies (constitution). **Standing:** \~18–22%
(t222), DESI-capped, the branch pre-registration pending guards.

\---

## ADDENDUM (2026-07-10, later): §7 STATUS CHANGE — the internal falsifier FIRED

The full-cycle KP solve (full\_cycle\_kp.py, def229/t230) computed the fixed point over the whole
cycle (expansion + thawed contraction + Tolman boost): **it robustly wants a\_turn = 0.70 (a PAST
turnaround, z=+0.43)** — excluded by observed acceleration; a future turn is 3× (a\_turn=1.0) to
10× (1.5) short, Tolman boost null, and the t227 "full-cycle-fixes-the-sign" claim was WRONG
(near-mirror contraction cancels). **So §7a–7c are DOWNGRADED:** the clean Route-D prediction is
dead; what survives is the IMMINENT-TURN CORNER (z\_turn \~ −0.1..−0.3, needing \~3× from four
favorably-aligned rigorous-KP O(1)s \[prior-adverse, tail] AND a strong thaw pulled by the data).
The two kill switches MERGE: the running Route-D MCMC (thaw free on the DESI joint stack) is the
single decider — thaw pulled hard → corner lives; thaw \~ 0 → Route-D dead twice over, **P-2026-018
(w = −1 rigid) stands as the distinctive branch, and J1 reverts to constitution/boundary-datum.**
§7d (the melt/re-form cycle closure) is unaffected as STORY. Standing \~15–19% (t230).

\---

## §10 — THE ATOM READING (the capstone, 2026-07-10 night)

**The universe is a single bound quantum state of the spacefluid — one atom — and cosmology is
its internal atomic physics.** Formation: genesis = recombination (capture cascade; f\_amp = the
branching ratio, computable-class). Structure: Landau's two components — the zero-entropy ground
state (floor/constitution/timeless; w=−1 exact \& ageless by theorem) and the entropic excitations
(light/matter/observers; Tolman's arrow). Spectroscopy: torus modes = the line spectrum (low-ℓ =
the first lines); the census = the selection rules; the CMB = the recombination photograph.
Chemistry: the dyad = one universal lepton rescaling ε (Koide-multiplicative), C²-gated, one
fingerprint across H0/D-H/ν/21cm/radio. Present: mid-emission — Γ/H = √3 = the linewidth (why-now
derived); symptoms {coupling dipole, mass defect = the thaw, recoil = the axis} = the falsifier
board. Biography: first excitation (Tolman arrow, finite past) → lengthening cascades → possible
ionization (binding energy un-computed). J1 = the ground-state eigenvalue: constitutional, at home.
**Status: the grammar is coherence (red-team-graded throughout, t270/272/274/276/278/280-class);
the empirical content lives in the children and the symptom chart. The method was the subject.**

