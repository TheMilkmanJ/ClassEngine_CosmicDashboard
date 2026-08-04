# PRTOE — The Cyclic / Torus / Twist-Genesis Arc

> This arc is **physics-grade story** — a coherent narrative assembled from real mechanisms, not a
> derivation. Its own closing verdict says so, and that grade stands: the bounce and cyclic
> rungs still face the standing theorems, and several scales here are chosen rather than
> derived. One element has since become load-bearing: the negative bare vacuum named in
> this arc is what makes the turn possible at all — the thawing floor alone approaches zero
> from above and never reverses the expansion
> ([PRTOE_MATH_SPINE.md](PRTOE_MATH_SPINE.md) §7d). Read the rest at story grade.
>
> **Discipline (2026-08-03):** claims ledger at end elevates *document discipline* above pure
> story-voice (every load-bearing claim graded). Physics ceiling is **mixed OPEN-BLOCKED**
> (no bare story physics row after PASS3). Rule: [working_logs/STORY_GRADE_ELEVATION_RULE.md](working_logs/STORY_GRADE_ELEVATION_RULE.md).
>
> **Non-claim (2026-08-04):** the **expansion reverse / bounce** is **not** Strong CP / θ̄.
> Floor sign, rotation cancel, and bounce stress-energy are a different sector from QCD’s
> vacuum angle. Constitutional silence on θ̄: [PRTOE_strong_cp.md](PRTOE_strong_cp.md).
> Seat-hunt (why the itch exists without a solution):
> [working_logs/_runs/physics_improve_full_20260804/STRONG_CP_SEAT_HUNT.md](working_logs/_runs/physics_improve_full_20260804/STRONG_CP_SEAT_HUNT.md).

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


*Honest-verdict discipline throughout. This documents a multi-step brainstorm that
converted a chain of physical instincts into computed results. Every mechanism named
here maps to real physics; the assembly into a genesis story is coherent but not a
derivation. The testable edge is the twist-floor dark-energy prediction (w₀ > −1, thawing).
Companions: docs/PRTOE_cosmological_constant.md,
docs/PRTOE_PREREGISTERED_PREDICTIONS.md (P-2026-013); scratchpad scripts (scratch-era, not
retained): hawking_brake.py, rotation_reverse.py, three_joints.py, ghost_field.py,
twist_floor.py, c1_locus_twist.py.*

---

## The chain (each stage computed, each verdict graded)

### 1. Hawking radiation as a "brake" — real sign, negligible magnitude
- Converting black-hole rest mass (w = 0) → radiation (w = +1/3) raises (ρ+3p): a **brake**
 (deceleration). Sign correct.
- **Magnitude:** a solar-mass black hole radiates 2×10⁻⁵⁸ of its mass per Hubble time, and
 L/M ∝ 1/M³, so massive holes radiate essentially nothing. **Maximal dynamic ceiling** (every
 baryon → a stellar-mass black hole, Ω_b = 0.05): **1.1×10⁻⁶² of ρ_crit.** Cosmologically zero.
- Only ~10¹⁵ g primordial black holes radiate appreciably **today** — lighter classes finished
 long ago (the ~10¹¹ g class evaporated during the BBN era, where its injections are separately
 quantified and excluded by ⁶Li: the deuterium row's §5b), heavier ones radiate almost nothing,
 and stellar collapse cannot make light ones (TOV ≥ 3 M☉).
- **A brake ≠ a reversal:** radiation self-dilutes (a⁻⁴); with ρ_inf > 0, Λ always wins the far
 future. No reversal from radiation.
- **Kept for later:** in a *contracting* phase radiation blueshifts (a⁻⁴ grows as a falls), so
 the negligible brake becomes the crunch's dominant heat. This is the reheated-radiation fuel
 for the bounce (and the carrier of the Tolman entropy).

### 2. The reversal — it must act on the floor's sign, not as a fluid on top
- Model: ρ_floor(t) = ρ_bare + ρ_rot(t), with ρ_bare < 0 (an AdS true vacuum) and ρ_rot > 0 the
 rotation propping it up.
- As the rotation cancels, the floor → ρ_bare < 0 → **genuine recollapse** (a brake never does
 this).
- Turnaround at a_turn = (Ω_m/|ρ_bare|)^(1/3); requires **ρ_bare > −0.30** or we would be
 collapsing now. Reversal in **~tens of Gyr**.
- The effective w today is DESI-compatible (w ≈ −0.86 for τ ~ 3 Hubble times). Costs: ρ_bare and
 τ are free (two parameters); "why cancel now" is the cosmological-constant coincidence
 relocated (Barrel B).

### 3. The floor's rotation — the barotropic clamp is an artifact
- The coded floor w(ρ) = −exp(−s), with s clamped ≥ 0, enforces **ρ ≥ ρ_inf and clamps the
 reversal out**; the deviation goes as a⁻³ (w = 0, fast).
- But that is the on-attractor fluid limit. The full ghost-condensate **field**
 (ghost_field.py), mildly displaced, gives a **dynamically slow** w: w_today ≈ −0.94 (barely
 displaced) to −0.67 (mildly displaced), accelerating, → −1 in the future. **The slow field
 beats the fast fluid, as anticipated; the clamp hides the field's slow-roll degree
 of freedom.**
- Below the floor is **phantom runaway** (w < −1), which is *why* the clamp exists. The single
 field **freezes** (w → −1) — the wrong direction for DESI — and settles to +ρ_inf, so it gives
 no reversal on its own. A reversal needs either a negative attractor sign or a second field.

### 4. The twist floor — counter-rotation forced by the twist, giving thawing and reversal
- **A twist is by definition two opposed rotations** (the torsional tension is the mechanical
 reversal). So the second rotation is not a free field.
- Two coupled phases mean the *relative* phase ψ carries a **periodic potential**
 V(ψ) = M⁴(1 − cos ψ) — a pseudo-Goldstone (axion-like) field. The floor is then
 ρ_bare + ½ψ̇² + V(ψ).
- **twist_floor.py result: thawing in every case** — w rises toward today from ~−1 (the DESI DR2
 direction). w₀ ≈ −0.72 (M⁴ = 1.5, ρ_bare = −0.1), reversing at **+33 Gyr**; other cases reverse
 at +62–76 Gyr. *(The turn has since been computed at the sector's own bare depth — a ≈ 2.0–2.8,
 16–26 Gyr, [PRTOE_MATH_SPINE.md](PRTOE_MATH_SPINE.md) §7d; the case timings here are this
 file's exploratory scan, kept as its record.)*
- **Barrel-E defusal:** thawing is a forced direction (an unfreezing field always rolls w up from
 −1), and it is independent of DESI, so predicting w > −1 is not opportunistic. The magnitude is
 tuned; the direction is robust.
- Costs: M⁴ and the decay constant are tuned (ρ_floor ≈ 0.7 and m ~ H₀ today — the quintessence
 coincidence); ρ_bare < 0 is a sign choice; the value is not derived (Barrel B); and the model
 class is a known one (thawing axion plus AdS) — the distinctive element here is the twist
 genesis tying the field to the counter-rotation.

### 5. The cyclic conjecture's three joints — reversal salvageable, bounce and cycle hit theorems
- **J1, the floor's rotation:** the slow field-level behavior works (see §3); the barotropic
 a⁻³-plus-clamp treatment is the artifact. A reversal needs the floor rebuilt (clamp removed,
 ρ_bare < 0, coupling included).
- **J2, ekpyrosis and BKL:** the anisotropy grows as σ² ∝ a⁻⁶ during contraction, and beating it
 needs the stiff sector at **w > 1**. A canonical scalar tops out at **w = 1** (kination), so it
 ties and generically loses. The Affleck–Dine twist genesis has no steep negative potential, so
 **BKL chaos is not beaten** without an added ekpyrotic potential.
- **J3, entropy and Tolman:** the entropy is **black-hole-dominated at ~10¹⁰⁴ k_B** (16 orders
 above the CMB's), with S_BH ∝ M² and monotonically rising. A reset needs ekpyrotic dilution,
 which is J2 again and fails. Black holes persist across a bounce (inhomogeneous seeding).
 **No reset means Tolman bites.**
- **The ladder:** the reversal is viable but not in this model as coded (the clamp forbids it);
 the bounce hits BKL; the cycle hits Tolman.

### 6. The c = 1 location — a well-defined, confining acoustic horizon (c1_locus_twist.py)
- The ghost-condensate dispersion v²(k) = c_s² + k²/M² means perturbations reach c at **k\* = M**
 (the condensate's UV scale). v rises with k: long modes crawl, short modes reach c.
- Infalling matter slower than v(k\*) is **trapped inside k\* = M**, giving an **acoustic horizon
 (a dumb hole)** — "stuck at c = 1." The confinement the genesis needs is real and well defined.

### 7. Twist seeding — a sphere cannot, a torus must (c1_locus_twist.py)
- Helicity H = ∫v·(∇×v): **spherical radial collapse gives H = 0 exactly** (curl-free, so no net
 twist — the missing-axis problem, proven).
- **A torus-supported Beltrami flow gives H/E = +1** (validated numerically). The poloidal and
 toroidal circulations are the **two counter-rotations**, and the torus's **symmetry axis** is
 the missing axis.

### 8. The torus convergence — two independent threads meet (P-2026-013)
- The torus was already the registered shape: **P-2026-013**, a flat 3-torus, motivated
 independently (finitism, no-center, H₀-safe). **The low quadrupole is not among its
 motivations:** regenerated with the ISW term included on a retained generator, the retention at
 the matched-circles floor L = 27.6 Gpc is 0.90, so the largest suppression any permitted box
 delivers is 10% — 0.16σ against the quadrupole's own 63% cosmic variance, and nowhere near the
 observed deficit, which is 50–80% (equivalently a retention of 0.2–0.5, the same quantity the
 0.90 above is quoted in). What survives is the *shape* — suppression confined to the lowest multipoles
 and gone by ℓ ≈ 4 — and the test's relocation from the power spectrum to the off-diagonal
 covariance.
- The genesis story, worked from the other end, **demands** a torus for the twist axis.
 Independent convergence.
- The general-relativistic name for this instant: the reheating genesis reads as the one realized
 white-hole-like handover — the time-reverse solution general relativity always carried, spent
 exactly once with no exterior counterparty. This is a causal-structure reading, not a
 derivation; for the identification, grades, and limits see
 [PRTOE_white_holes.md](exploratory/PRTOE_white_holes.md).
- **Cross-bounce bookkeeping:** the rotation is dynamical (it resets to 0 at the crunch);
 **the topology is not** — the torus survives and carries the axis across the bounce, so the
 reheated radiation can re-seed the spin. Topology holds what dynamics loses.

### 9. The bubble-ring mechanism and the local ≠ global torus caveat
- A confined buoyant plume (the reheated radiation) rolls up at its edge (Kelvin–Helmholtz) into
 a **vortex ring**, and the background swirl makes it **helical** (the net helicity is the
 twist). This is textbook vortex-ring formation, so it **makes the torus dynamically** — it
 answers "why not a sphere".
- **Critical distinction:** a *local* vortex-ring torus (a structure in space) is not the
 *global* 3-torus topology (the shape of space, P-2026-013). They coincide only if the
 primordial ring is comparable in size to the whole compact universe. Conditional and
 speculative.

---

## Overall status
A **coherent cyclic-genesis narrative assembled from real mechanisms** (acoustic horizon, plume
roll-up, helical vortex ring, thawing pseudo-Goldstone floor, negative bare vacuum). It closes a
loop: torus → twist genesis → thawing floor → reversal → crunch → confined c = 1 heat → the torus
reseeds the twist. **This is a story built from real parts, not a derivation.** Two theorems (BKL,
Tolman) still stand against the bounce and cyclic rungs; the scales (M⁴, the decay constant, the
sign of ρ_bare) are tuned or chosen; and the cosmological-constant value is untouched.

**The one falsifiable, data-touching output: the twist-floor dark-energy sector — w₀ > −1,
thawing, with a reversal in tens of Gyr.** Everything else lies past the observable edge. The next
step is to derive that w(z) as forced and confront it with DESI (analytic first, then a CLASS
fit).

**What survives as genuine:** (i) the result that the clamp is an artifact and that the field
supplies the slow evolution the fluid limit hides; (ii) the forced-thawing direction (the Barrel-E
defusal); (iii) the theorem that a sphere gives zero twist and a torus the maximum, tying the
genesis to P-2026-013. **What does not:** the bounce (BKL — the chain's named open problem), the
cycle *as eternal* (Tolman — which the standing frame accepts rather than fights: a finite,
lengthening chain, [PRTOE_arrow_of_time.md](exploratory/PRTOE_arrow_of_time.md) §2), and the
cosmological-constant value.

---

## The birefringence arc — the model's first distinctive-in-principle object, computed down

**Claim:** one complex field Ψ = |Ψ|e^(iθ) carries three handles: |Ψ| → mass (the
electron-coupled scalar), θ → birefringence (θ F·F̃, via the electron chiral anomaly), and
θ̇ → Affleck–Dine charge. The birefringence coupling is not posited — it is the anomaly shadow of
the same lepton coupling that gives the electron-coupled scalar (a complex Yukawa plus a charged
electron, through Fujikawa, gives θ F·F̃).

Three gates (scratchpad/birefringence_gates.py):
- G1, structural: passes — the coupling is forced by the anomaly, not a free dial.
- G3, varying α: passes — the phase is a pseudoscalar, so it couples as F·F̃ only (parity-odd) and
 induces zero varying α; the electron-coupled scalar's radial mode gives Δα/α ~ 2×10⁻⁵ confined
 to z > 50, blind to quasar constraints and 208× under the CMB bound. The constraint that killed
 standalone varying-α models cannot reach it.
- G2, magnitude: fails at natural values (a decisive catch, accepted). The amplitude carries a
 hidden factor: β = (α/2π) N_e (m_Ψ/m_e) Δθ. The electron-coupled scalar needs only a *variation*
 in m_Ψ of ~1.24% of m_e, and at that natural value β ~ 0.003°, 100× under the claimed 0.30° hint
 (which is calibration-degenerate; the model's own prediction is zero, P-2026-009). Reaching 0.3°
 requires m_Ψ/m_e ~ 1, i.e. m_e sourced entirely by Ψ — the fully-sourced reading (obstructed by
 gate-0 BBN and by the hierarchy, the same wall #30 died on).

**The DESI↔β correlation:** the same twist Δθ sets both the dark-energy thawing (w₀ > −1) and β.
One field's twist, two skies — ΛCDM with a varying m_e cannot make this connection. It is
structurally distinctive, and N_e is pinned by leptophilia (there is nothing to cancel against, so
target A passes). This is the model's first distinctive-in-principle object.

The electron electric dipole moment (EDM; target B, scratchpad/electron_edm.py) — the second
constraint — cuts the same way: the same complex Yukawa gives the electron a CP-odd coupling, and
so an EDM. At one loop it is y_e²-suppressed (~1×10⁻³⁵, safe). But the tau Barr-Zee diagram
(leptophilic includes τ) gives d_e ~ 1×10⁻²⁶ e·cm, ~2000× over the JILA bound (4.1×10⁻³⁰), and
that is robust to the owed prefactor (a factor of 10 still leaves it 200× over). Since
d_e ~ sin(φ) ~ β, the EDM cannot be suppressed without killing the signal — an exact correlation.
The fully-sourced reading and the EDM are one wall seen from two sides: a large β needs a large
sin φ together with that reading, which is exactly what maximizes the Barr-Zee contribution, and
the only escape (a heavier ⟨Ψ⟩) worsens the hierarchy.
 - Nuance (it cuts both ways): the τ Barr-Zee diagram needs Ψ to couple to the tau. The
 electron-coupled scalar is specific to the electron (and the neutrinos); if Ψ does not couple
 to μ or τ, the τ loop is absent and the EDM falls back to the safe one-loop value. That
 escapes the EDM but (a) does not open the fully-sourced reading and (b) buys a "why only the
 electron" flavor-selectivity cost. The EDM is escapable; the fully-sourced reading is not.

The verdict, accepted: the mechanism is real and inaccessible to ΛCDM, but this model cannot carry
it at observable amplitude — both roads (a universal lepton coupling, where the reading and the EDM
are both dead; an electron-specific coupling, where the reading stays shut and a flavor puzzle is
added) end at the fully-sourced reading. Shot 1 was dented, then re-closed, and stands firmer. The
claim is held provisional pending its named referees. That reading (m_e sourced entirely by Ψ,
beating gate-0 BBN, the hierarchy, and the τ-Barr-Zee EDM) is now the whole game for both #30 and
birefringence — one wall, three defenders.

**Also:** the neutrino "clock" (the blindness to quasar constraints traces to the neutrino mass
scale: heavier states go non-relativistic at z ~ 16–94, above the quasar window; z = 50
corresponds to ~27 meV, in band, value not derived); and a null for the three-jobs expectation
(the threshold has two jobs, not three — the Affleck–Dine charge is genesis-set, 29 orders above
the meV floor, so "everything has three jobs" fails its own test; the *field* has three handles,
and objects inherit only what they couple to).

---

## Claims ledger & residual freeze (2026-08-04) — above story-grade discipline

**Stamp:** OPEN-THEORY honesty. Document is a **map assembly** (interpretation seating), not a derivation. Bounce / H_re **OPEN-BLOCKED**; DE branch **XOR OPEN-BLOCKED**; production helicity **OPEN-MACHINE**. No invented closes.  
**Strong CP fence (header):** expansion reverse / bounce is **not** \(\bar\theta\) — **kept**; see [PRTOE_strong_cp.md](PRTOE_strong_cp.md).  
**Bounce full freeze package (authoritative for bounce rungs):** [working_logs/_runs/bounce_full_freeze_20260804/](working_logs/_runs/bounce_full_freeze_20260804/).  
**Prior inventory:** [working_logs/_runs/open_theory_full_20260804/](working_logs/_runs/open_theory_full_20260804/).  
**Parents:** [debt_bounce_20260803](working_logs/_runs/debt_bounce_20260803/REPORT.md); [debt_bounce_FA3_20260803](working_logs/_runs/debt_bounce_FA3_20260803/REPORT.md); [PRTOE_MATH_SPINE.md](PRTOE_MATH_SPINE.md) §7d; [PRTOE_bigbang_no_singularity.md](PRTOE_bigbang_no_singularity.md); [PRTOE_igmf_helicity.md](PRTOE_igmf_helicity.md).

| # | Claim | Grade | Evidence | Residual / blocker | **Forbidden** |
|---|---|---|---|---|---|
| 1 | Arc is a coherent cyclic-genesis *map* assembled from real mechanisms, not a derivation | **interpretation** (document seating) | header + Overall status | Physics grades live in rows 2–9 | Present arc as physics derivation / COMPLETE |
| 2 | Hawking brake has correct sign; cosmologically negligible magnitude | **interpretation** + standard BH thermo | §1; L/M scaling | Not a reversal engine | Hawking as cosmic reverse |
| 3 | Reversal needs ρ_bare < 0; thawing floor alone never reverses expansion | **derived-conditional** | [PRTOE_MATH_SPINE.md](PRTOE_MATH_SPINE.md) §7d; §2, §4 | ρ_bare value not derived (Barrel B) | Derived ρ_bare value; reverse from positive floor alone |
| 4 | DE branch: thawing floor (w₀ > −1) vs rigid w = −1 | **OPEN-BLOCKED** (XOR) | **P-2026-056** (P-018 XOR Route-D); as-built dCDF prefers w=−1; Route-D on `cmp_prtoe_routeD` | Standing branch data-adjudicated; not “complete-conditional thawing edge” | Cite P-2026-013 (topology) as DE evidence; claim both branches closed |
| 5 | Bounce rung fails BKL without w>1 stiff sector; cycle fails Tolman entropy reset; exterior H_re | **OPEN-BLOCKED** | §5 J2–J3; [bounce_derivation_workplan.md](working_logs/bounce_derivation_workplan.md); [debt_bounce_20260803](working_logs/_runs/debt_bounce_20260803/REPORT.md); [debt_bounce_FA3](working_logs/_runs/debt_bounce_FA3_20260803/REPORT.md); [bounce_full_freeze_20260804](working_logs/_runs/bounce_full_freeze_20260804/REPORT.md) | **OPEN-THEORY:** classical turn / H_re (F-A3); BKL+Tolman stand; homogeneous engines DEAD | Book eternal cycles; desk-derive H_re; reopen nogo engines; bounce = Strong CP |
| 6 | Sphere → H=0; torus Beltrami → maximal helicity class | **derived** (sphere H=0) + **OPEN-BLOCKED** (torus production) | §7–§9; `scripts/ring_toroidal_hkin.py`, `ring_rollup_poloidal_v3.py`; T14 A4 | **OPEN-MACHINE:** production sign(H_kin) + true-mirror; scratch timings not retained | Production booking of scratch-era twist timings as precision predictions |
| 7 | Compact topology bet P-2026-013 | **registered** | predictions register | Not hardened to “flat 3-torus only” | Flat-torus-only as derived geometry |
| 8 | White-hole-like causal reading of reheating handover | **interpretation** / provisional | §8 → [PRTOE_white_holes.md](exploratory/PRTOE_white_holes.md) | Not metric isometry; bounce open | Metric isometry to eternal white hole |
| 9 | Birefringence as anomaly shadow of complex Ψ; observable amp inaccessible | **provisional** | birefringence gates; G2 fails at natural β | Escape paths open; fully-sourced m_e blocked | Birefringence 0.3° class without fully-sourced m_e |

### Residual freeze (named OPEN-BLOCKED)

| Residual | Grade | Blocker path / axiom | What would unstick |
|---|---|---|---|
| Bounce / H_re / BKL+Tolman | **OPEN-BLOCKED** | debt_bounce; F-A3; [bounce_full_freeze_20260804](working_logs/_runs/bounce_full_freeze_20260804/REPORT.md); workplan | Licensed turn without inventing H_re; not desk re-try of nogo engines |
| Homogeneous FRW bounce engines | **failed / retired** | freeze nogo reconfirms (floor/thermal/magnetic/handover/X/quartic/rotation) | New premises only |
| DE thaw XOR rigid w=−1 | **OPEN-BLOCKED** (XOR) | P-2026-056; Route-D vs dCDF floor | Data adjudication / branch kill |
| Production H_kin sign | **OPEN-BLOCKED** (OPEN-MACHINE) | T14 four-branch / igmf_helicity freeze | Production under pre-registered gates |
| ρ_bare magnitude | **OPEN** (Barrel B) | MATH_SPINE §7d | Independent floor derivation |

**Non-claims:** Derived bounce dynamics; exterior H_re; eternal-cycle closure; cosmological-constant value; production booking of scratch-era twist timings as precision predictions; birefringence at 0.3° class without fully-sourced m_e; map = derivation; bounce / reverse = Strong CP / \(\bar\theta\); inventing negative-energy stiff X.

**Kill conditions (bounce rungs):** same as [bounce_full_freeze_20260804/REPORT.md](working_logs/_runs/bounce_full_freeze_20260804/REPORT.md) §5 — H_re stays OPEN-BLOCKED until licensed matching; cyclic booking requires full closed-cycle derivation (not claimed).

**Triage:** elevate-in-place (discipline only) — **blocked** on bounce (OPEN-THEORY / BKL+Tolman) and helicity production (OPEN-MACHINE). Shelf map with reader banner per rule §3; physics ceiling **mixed OPEN-BLOCKED**. **Not** Failures. **Not** forced exploratory while MATH_SPINE still cites negative bare vacuum as load-bearing.

**Rule:** [working_logs/STORY_GRADE_ELEVATION_RULE.md](working_logs/STORY_GRADE_ELEVATION_RULE.md).
