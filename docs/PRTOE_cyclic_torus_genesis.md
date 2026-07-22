# PRTOE — The Cyclic / Torus / Twist-Genesis Arc

> This arc is story-grade — a coherent narrative assembled from real mechanisms, not a
> derivation. Its own closing verdict says so, and that grade stands: the bounce and cyclic
> rungs still face the standing theorems, and several scales here are chosen rather than
> derived. One element has since become load-bearing: the negative bare vacuum named in
> this arc is what makes the turn possible at all — the thawing floor alone approaches zero
> from above and never reverses the expansion
> ([PRTOE_MATH_SPINE.md](PRTOE_MATH_SPINE.md) §7d). Read the rest at story grade.

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


*Honest-verdict discipline throughout. This documents a multi-step brainstorm that
converted a chain of physical instincts into computed results. Every mechanism named
here maps to real physics; the ASSEMBLY into a genesis story is coherent but NOT a
derivation. Testable edge = the twist-floor DE prediction (w₀>−1 thawing). Companion:
docs/PRTOE_cosmological_constant.md, docs/PRTOE_PREREGISTERED_PREDICTIONS.md (P-2026-013),
scratchpad scripts (scratch-era, not retained): hawking_brake.py, rotation_reverse.py, three_joints.py, ghost_field.py,
twist_floor.py, c1_locus_twist.py.*

---

## The chain (each link computed, each verdict honest)

### 1. Hawking radiation as a "brake" — real sign, negligible magnitude
- Converting BH rest-mass (w=0) → radiation (w=+1/3) raises (ρ+3p): a **brake** (deceleration). Sign correct.
- **Magnitude:** solar BH radiates 2×10⁻⁵⁸ of its mass per Hubble time; L/M ∝ 1/M³ so big BHs radiate ~nothing. **Maximal dynamic ceiling** (every baryon → stellar BH, Ω_b=0.05): **1.1×10⁻⁶² of ρ_crit.** Cosmologically zero.
- Only ~10¹⁵ g PBHs radiate appreciably **today** — lighter classes finished long ago (the ~10¹¹ g class evaporated during the BBN era, where its injections are separately priced and killed by ⁶Li: the deuterium scar's §5b), heavier ones radiate ~nothing, and stellar collapse can't make light ones (TOV ≥3 M☉).
- **A brake ≠ a reverse:** radiation self-dilutes (a⁻⁴); with ρ_inf>0, Λ always wins the far future. No reversal from radiation.
- **KEPT FOR LATER:** in a *contracting* phase radiation BLUESHIFTS (a⁻⁴ grows as a↓) → the negligible brake becomes the crunch's dominant heat. This is the genesis "heat fountain" fuel (and the Tolman-entropy carrier).

### 2. The reverse — must act on the FLOOR's sign, not as a fluid on top
- Model: ρ_floor(t) = ρ_bare + ρ_rot(t), ρ_bare<0 (AdS true vacuum), ρ_rot>0 the rotation propping it up.
- As rotation cancels, floor → ρ_bare<0 → **genuine recollapse** (a brake never does this).
- Turnaround a_turn=(Ω_m/|ρ_bare|)^{1/3}; requires **ρ_bare > −0.30** or we'd be collapsing now. Reverse in **~tens of Gyr**.
- Effective w today DESI-compatible (w≈−0.86 for τ~3 Hubble). Costs: ρ_bare & τ free (2 params); "why cancel now" = CC coincidence relocated (Barrel B).

### 3. The floor's rotation — the barotropic CLAMP is an ARTIFACT
- Coded floor w(ρ)=−exp(−s), s clamped ≥0 ⇒ **ρ≥ρ_inf enforced, reverse clamped OUT**; deviation ∝ a⁻³ (w=0, fast).
- BUT that is the ON-ATTRACTOR FLUID limit. The full ghost-condensate **field** (ghost_field.py), mildly displaced, gives a **dynamic slow** w: w_today ≈ −0.94 (barely) to −0.67 (mild), accelerating, → −1 in future. **"Dynamic-slow beats fixed-fast" vindicated; the clamp hides the field's slow-roll d.o.f.**
- Below the floor is **phantom runaway** (w<−1), which is *why* the clamp exists. The single field **freezes** (w→−1) — wrong DESI direction — and settles to +ρ_inf (no reverse alone). A reverse needs the attractor sign negative or a 2nd field.

### 4. The twist floor — counter-rotation FORCED by the twist, gives thawing + reverse
- **A twist is definitionally two opposed rotations** (torsional tension = the snap). So the second rotation is NOT a free field.
- Two coupled phases ⇒ the RELATIVE phase ψ carries a **periodic potential** V(ψ)=M⁴(1−cos ψ) — a pseudo-Goldstone/axion. Floor = ρ_bare + ½ψ̇² + V(ψ).
- **twist_floor.py result: THAWING in every case** — w rises toward today from ~−1 (the DESI DR2 direction). w₀≈−0.72 (M⁴=1.5, ρ_bare=−0.1), reverses **+33 Gyr**; other cases reverse +62–76 Gyr. *(The turn was since computed at the sector's own bare depth — a ≈ 2.0–2.8, 16–26 Gyr, [PRTOE_MATH_SPINE.md](PRTOE_MATH_SPINE.md) §7d; the case timings here are this file's exploratory scan, kept as its record.)*
- **Barrel-E defusal:** thawing is a FORCED direction (an unfreezing field always rolls w up from −1), independent of DESI ⇒ predicting w>−1 is not opportunistic. Magnitude tuned; direction robust.
- Costs: M⁴ & decay const tuned (ρ_floor≈0.7, m~H₀ now = quintessence coincidence); ρ_bare<0 a sign choice; value not derived (Barrel B); known model class (thawing axion + AdS) — PRTOE's distinctive bit is the twist genesis tying the field to the counter-rotation.

### 5. The three joints of the cyclic conjecture — reverse salvageable, bounce+cyclic hit theorems
- **J1 floor rotation:** field-level dynamic-slow works (see §3); barotropic a⁻³+clamp is the artifact. Reverse needs floor rebuilt (remove clamp, ρ_bare<0, coupling).
- **J2 ekpyrotic/BKL:** anisotropy σ²∝a⁻⁶ during contraction; beating it needs the stiff sector at **w>1**. Canonical scalar maxes at **w=1** (kination) → TIES, generically loses. AD twist-snap has no steep negative potential ⇒ **BKL chaos not beaten** without an added ekpyrotic potential.
- **J3 entropy/Tolman:** entropy is **BH-dominated ~10¹⁰⁴ k_B** (16 orders > CMB), S_BH∝M², monotonically rising. Reset needs ekpyrotic dilution (=J2, fails). BHs persist across a bounce (inhomogeneous seeding). **No reset ⇒ Tolman bites.**
- **Ladder:** Reverse = viable-but-not-in-PRTOE (clamp forbids it). Bounce = hits BKL. Cyclic = hits Tolman.

### 6. The c=1 location — a DEFINED, confining acoustic horizon (c1_locus_twist.py)
- Ghost-condensate dispersion v²(k)=c_s²+k²/M² ⇒ perturbations hit c at **k*=M** (condensate UV scale). v RISES with k; long modes crawl, short modes reach c.
- Infalling matter slower than v(k*) is **trapped inside k*=M** ⇒ an **acoustic horizon (dumb hole)** = "stuck in c=1." The confinement the genesis needs is real and defined.

### 7. Twist seeding — a SPHERE can't, a TORUS must (c1_locus_twist.py)
- Helicity H=∫v·(∇×v): **spherical radial collapse → H=0 exactly** (curl-free; no net twist — the missing-axis problem, proven).
- **Torus-supported Beltrami flow → H/E=+1** (validated numerically). Poloidal+toroidal circulation = the **two counter-rotations**; the torus **symmetry axis** = the missing axis.

### 8. The torus convergence — two independent threads meet (P-2026-013)
- The torus was ALREADY the registered shape: **P-2026-013**, flat 3-torus, motivated independently (finitism, no-center, H₀-safe). **The low quadrupole is not among its motivations:** regenerated ISW-inclusive on a retained generator, the retention at the matched-circles floor L = 27.6 Gpc is 0.90, so the largest suppression any permitted box delivers is 10% — 0.16σ against the quadrupole's own 63% cosmic variance, and nowhere near the observed 0.2–0.5. What survives is the *shape* — suppression confined to the lowest multipoles and gone by ℓ ≈ 4 — and the test's relocation from the power spectrum to the off-diagonal covariance.
- Genesis, worked from the other end, **demands** a torus for the twist axis. Independent convergence.
- The GR name for this instant: the heat-fountain genesis reads as the one realized white-hole-like handover — the time-reverse solution GR always carried, cashed exactly once with no exterior counterparty. Causal-structure reading, not a derivation; the identification, grades, and fences: [PRTOE_white_holes.md](PRTOE_white_holes.md).
- **Cross-bounce bookkeeping:** rotation is dynamical (resets to 0 at crunch); **topology is not** — the torus survives and carries the axis across the bounce for the heat fountain to re-seed spin. Topology holds what dynamics loses.

### 9. Bubble-ring mechanism + the LOCAL≠GLOBAL torus caveat
- A confined buoyant plume (heat fountain) rolls up at its edge (Kelvin-Helmholtz) into a **vortex ring**; background swirl makes it **helical** (net helicity = the twist). This is textbook vortex-ring formation ⇒ **dynamically makes the torus** (answers "why not a sphere").
- **Critical distinction:** a LOCAL vortex-ring torus (structure in space) ≠ the GLOBAL 3-torus topology (shape of space, P-2026-013). They coincide only IF the primordial ring is comparable to the whole compact universe. Conditional, speculative.

---

## Honest overall status
A **coherent cyclic-genesis narrative assembled from real mechanisms** (acoustic horizon, plume roll-up, helical vortex ring, thawing pseudo-Goldstone floor, negative bare vacuum). It closes a loop: torus → twist genesis → thawing floor → reverse → crunch → confined c=1 heat → torus reseeds twist. **This is a story built from real parts, NOT a derivation.** Two theorems (BKL, Tolman) still stand against the bounce/cyclic rungs; scales (M⁴, decay const, ρ_bare sign) are tuned/chosen; the CC VALUE is untouched.

**The one falsifiable, data-touching output: the twist-floor DE sector — w₀>−1, thawing, reverse in tens of Gyr.** Everything else is past the observable edge. The next step is to DERIVE that w(z) as forced and confront it with DESI (analytic → CLASS fit).

**What survives as genuine:** (i) the clamp-is-an-artifact / field-gives-dynamic-slow result; (ii) the forced-thawing direction (Barrel-E defusal); (iii) the sphere=0 / torus=maximal-twist theorem tying genesis to P-2026-013. **What does not:** the bounce (BKL — the chain's named debt), the cycle *as eternal* (Tolman — which the standing frame accepts rather than fights: a finite, lengthening chain, [PRTOE_arrow_of_time.md](PRTOE_arrow_of_time.md) §2), the CC value.

---

## THE BIREFRINGENCE DOOR ARC — the model's first distinctive-in-principle object, computed down

**Claim:** one complex field Psi=|Psi|e^{i θ}, three field-handles: |Psi|→mass (dyad),
θ→birefringence (θ F.Ftilde via the electron chiral anomaly), θ-dot→AD charge.
The birefringence coupling is NOT posited -- it is the anomaly shadow of the SAME lepton
coupling that gives the dyad (complex Yukawa + charged electron → Fujikawa → θ F.Ftilde).

Three gates (scratchpad/birefringence_gates.py):
- G1 structural: passes — the coupling is forced by the anomaly, not a dial.
- G3 varying-α: passes — the phase is a pseudoscalar → F.Ftilde only (parity-odd), induces ZERO
 varying-α; dyad's radial mode gives Δ a/a~2×10⁻⁵ confined to z>50, quasar-BLIND, 208x
 under the CMB bound. The landmine that killed standalone varying-α cannot reach it.
- G2 magnitude: fails at natural values (a decisive catch, accepted). The
 amplitude carries a hidden factor: β = (α/2pi) N_e (m_Psi/m_e) Dtheta. The dyad needs
 only m_Psi VARIATION ~1.24% of m_e → at that natural value β~0.003 deg, 100x UNDER the
 claimed 0.30° hint (calibration-degenerate; the model's own prediction is zero, P-2026-009). Reaching 0.3 deg requires m_Psi/m_e~1 = m_e FULLY Psi-sourced = the
 DOOR (gate-0 BBN + hierarchy obstructed, the SAME wall #30 died on).

**The DESI↔β correlation:** the SAME
twist Dtheta sets the DE thawing (w0>-1) AND β. One field's twist, two skies -- ΛCDM+varying-
m_e CANNOT make this link. Structurally distinctive; N_e pinned by leptophilia (nothing to
cancel → target A passes). This is the ontology's first distinctive-IN-PRINCIPLE object.

The electron EDM (target B, scratchpad/electron_edm.py) — the second blade — cuts: the same
complex Yukawa gives the electron a CP-odd coupling → electron EDM. One-loop y_e²-suppressed
(~1×10⁻³⁵, safe). But the TAU Barr-Zee (leptophilic includes τ) → d_e~1×10⁻²⁶ e.cm = ~2000x OVER
JILA (4.1×10⁻³⁰), robust to the owed prefactor (factor-10 still 200x over). d_e~sin(φ)~β →
CANNOT suppress the EDM without killing the signal (exact correlation). Door + EDM are ONE WALL
FROM TWO SIDES: β-large needs sin-φ-large + the door, which MAXIMIZES the Barr-Zee; the only
escape (heavier <Psi>) worsens the hierarchy.
 - NUANCE (firewall both ways): the τ Barr-Zee needs Psi to couple to the TAU. The
 dyad is electron-(+neutrino-)specific; if Psi does NOT couple to μ/τ, the τ loop is
 absent and the EDM falls back to the SAFE one-loop. This ESCAPES the EDM but (a) does NOT
 open the door and (b) buys a "why only the electron" flavor-selectivity debit. EDM escapable;
 door is not.

The verdict, accepted: the mechanism is real and ΛCDM-inaccessible, but this model
cannot wear it at observable amplitude -- both roads (universal-lepton = door+EDM dead;
electron-specific = door+flavor-puzzle) end at the DOOR. SHOT 1 was dented, then re-closed, and
stands firmer. The claim is held provisional pending its named referees. The DOOR (m_e fully
Psi-sourced, beating gate-0 BBN + hierarchy + τ-Barr-Zee EDM) is now the WHOLE GAME for BOTH
#30 and birefringence -- one wall, three defenders.

**Also:** neutrino "clock" (quasar-blindness traces to the neutrino MASS SCALE:
heavier states go non-rel at z~16-94, above the quasar window; z=50 ~ 27meV, in-band, value not
derived); Job-3 null (the threshold has 2 jobs
not 3 -- the AD charge is genesis-set, 29 orders above the meV floor; "everything has 3 jobs"
FAILS its own test; the FIELD has 3 handles, objects inherit only what they couple to).
