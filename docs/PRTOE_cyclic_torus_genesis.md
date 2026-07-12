# PRTOE — The Cyclic / Torus / Twist-Genesis Arc (session 2026-07-10)

*Honest-verdict discipline throughout. This documents a multi-step brainstorm that
converted a chain of physical instincts into computed results. Every mechanism named
here maps to real physics; the ASSEMBLY into a genesis story is coherent but NOT a
derivation. Testable edge = the twist-floor DE prediction (w₀>−1 thawing). Companion:
docs/PRTOE_cosmological_constant.md, docs/PRTOE_PREREGISTERED_PREDICTIONS.md (P-2026-013),
scratchpad scripts: hawking_brake.py, rotation_reverse.py, three_joints.py, ghost_field.py,
twist_floor.py, c1_locus_twist.py.*

---

## The chain (each link computed, each verdict honest)

### 1. Hawking radiation as a "brake" — real sign, negligible magnitude
- Converting BH rest-mass (w=0) → radiation (w=+1/3) raises (ρ+3p): a **brake** (deceleration). Sign correct.
- **Magnitude:** solar BH radiates 2×10⁻⁵⁸ of its mass per Hubble time; L/M ∝ 1/M³ so big BHs radiate ~nothing. **Maximal dynamic ceiling** (every baryon → stellar BH, Ω_b=0.05): **1.1×10⁻⁶² of ρ_crit.** Cosmologically zero.
- Only ~10¹⁵ g PBHs radiate appreciably; they're constrained + evaporate. Stellar collapse can't make them (TOV ≥3 M☉).
- **A brake ≠ a reverse:** radiation self-dilutes (a⁻⁴); with ρ_inf>0, Λ always wins the far future. No reversal from radiation.
- **KEPT FOR LATER:** in a *contracting* phase radiation BLUESHIFTS (a⁻⁴ grows as a↓) → the negligible brake becomes the crunch's dominant heat. This is the genesis "heat fountain" fuel (and the Tolman-entropy carrier).

### 2. The reverse — must act on the FLOOR's sign, not as a fluid on top
- Model: ρ_floor(t) = ρ_bare + ρ_rot(t), ρ_bare<0 (AdS true vacuum), ρ_rot>0 the rotation propping it up.
- As rotation cancels, floor → ρ_bare<0 → **genuine recollapse** (a brake never does this).
- Turnaround a_turn=(Ω_m/|ρ_bare|)^{1/3}; requires **ρ_bare > −0.30** or we'd be collapsing now. Reverse in **~tens of Gyr**.
- Effective w today DESI-compatible (w≈−0.86 for τ~3 Hubble). Costs: ρ_bare & τ free (2 params); "why cancel now" = CC coincidence relocated (Barrel B).

### 3. The floor's rotation — the barotropic CLAMP is an ARTIFACT (user's correct challenge)
- Coded floor w(ρ)=−exp(−s), s clamped ≥0 ⇒ **ρ≥ρ_inf enforced, reverse clamped OUT**; deviation ∝ a⁻³ (w=0, fast).
- BUT that is the ON-ATTRACTOR FLUID limit. The full ghost-condensate **field** (ghost_field.py), mildly displaced, gives a **dynamic slow** w: w_today ≈ −0.94 (barely) to −0.67 (mild), accelerating, → −1 in future. **"Dynamic-slow beats fixed-fast" vindicated; the clamp hides the field's slow-roll d.o.f.**
- Below the floor is **phantom runaway** (w<−1), which is *why* the clamp exists. The single field **freezes** (w→−1) — wrong DESI direction — and settles to +ρ_inf (no reverse alone). A reverse needs the attractor sign negative or a 2nd field.

### 4. The twist floor — counter-rotation FORCED by the twist, gives thawing + reverse
- **A twist is definitionally two opposed rotations** (torsional tension = the snap). So the second rotation is NOT a free field.
- Two coupled phases ⇒ the RELATIVE phase ψ carries a **periodic potential** V(ψ)=M⁴(1−cos ψ) — a pseudo-Goldstone/axion. Floor = ρ_bare + ½ψ̇² + V(ψ).
- **twist_floor.py result: THAWING in every case** — w rises toward today from ~−1 (the DESI DR2 direction). w₀≈−0.72 (M⁴=1.5, ρ_bare=−0.1), reverses **+33 Gyr**; other cases reverse +62–76 Gyr.
- **Barrel-E defusal:** thawing is a FORCED direction (an unfreezing field always rolls w up from −1), independent of DESI ⇒ predicting w>−1 is not opportunistic. Magnitude tuned; direction robust.
- Costs: M⁴ & decay const tuned (ρ_floor≈0.7, m~H₀ now = quintessence coincidence); ρ_bare<0 a sign choice; value not derived (Barrel B); known model class (thawing axion + AdS) — PRTOE's distinctive bit is the twist genesis tying the field to the counter-rotation.

### 5. The three joints of the CYCLIC bet (three_joints.py) — reverse salvageable, bounce+cyclic hit theorems
- **J1 floor rotation:** field-level dynamic-slow works (see §3); barotropic a⁻³+clamp is the artifact. Reverse needs floor rebuilt (remove clamp, ρ_bare<0, coupling).
- **J2 ekpyrotic/BKL:** anisotropy σ²∝a⁻⁶ during contraction; beating it needs the stiff sector at **w>1**. Canonical scalar maxes at **w=1** (kination) → TIES, generically loses. AD twist-snap has no steep negative potential ⇒ **BKL chaos not beaten** without an added ekpyrotic potential.
- **J3 entropy/Tolman:** entropy is **BH-dominated ~10¹⁰⁶ k_B** (18 orders > CMB), S_BH∝M², monotonically rising. Reset needs ekpyrotic dilution (=J2, fails). BHs persist across a bounce (inhomogeneous seeding). **No reset ⇒ Tolman bites.**
- **Ladder:** Reverse = viable-but-not-in-PRTOE (clamp forbids it). Bounce = hits BKL. Cyclic = hits Tolman.

### 6. The c=1 location — a DEFINED, confining acoustic horizon (c1_locus_twist.py)
- Ghost-condensate dispersion v²(k)=c_s²+k²/M² ⇒ perturbations hit c at **k\*=M** (condensate UV scale). v RISES with k; long modes crawl, short modes reach c.
- Infalling matter slower than v(k\*) is **trapped inside k\*=M** ⇒ an **acoustic horizon (dumb hole)** = "stuck in c=1." The confinement the genesis needs is real and defined.

### 7. Twist seeding — a SPHERE can't, a TORUS must (c1_locus_twist.py)
- Helicity H=∫v·(∇×v): **spherical radial collapse → H=0 exactly** (curl-free; no net twist — the missing-axis problem, proven).
- **Torus-supported Beltrami flow → H/E=+1** (validated numerically after a curl-index fix). Poloidal+toroidal circulation = the **two counter-rotations**; the torus **symmetry axis** = the missing axis.

### 8. The torus convergence — two independent threads meet (P-2026-013)
- The torus was ALREADY the registered shape: **P-2026-013**, flat 3-torus, motivated independently (finitism, no-center, H0-safe; CMB quadrupole suppression for L~2–2.5 D).
- Genesis, worked from the other end, **demands** a torus for the twist axis. Independent convergence.
- **The GR name for this instant (2026-07-12):** the heat-fountain genesis is the one realized white hole — the time-reverse solution GR always carried, cashed exactly once with no exterior counterparty. The identification and its fences: [PRTOE_white_holes.md](PRTOE_white_holes.md).
- **Cross-bounce bookkeeping:** rotation is dynamical (resets to 0 at crunch); **topology is not** — the torus survives and carries the axis across the bounce for the heat fountain to re-seed spin. Topology holds what dynamics loses.

### 9. Bubble-ring mechanism + the LOCAL≠GLOBAL torus caveat
- A confined buoyant plume (heat fountain) rolls up at its edge (Kelvin-Helmholtz) into a **vortex ring**; background swirl makes it **helical** (net helicity = the twist). This is textbook vortex-ring formation ⇒ **dynamically makes the torus** (answers "why not a sphere").
- **Critical distinction:** a LOCAL vortex-ring torus (structure in space) ≠ the GLOBAL 3-torus topology (shape of space, P-2026-013). They coincide only IF the primordial ring is comparable to the whole compact universe. Conditional, speculative.

---

## Honest overall status
A **coherent cyclic-genesis narrative assembled from real mechanisms** (acoustic horizon, plume roll-up, helical vortex ring, thawing pseudo-Goldstone floor, negative bare vacuum). It closes a loop: torus → twist genesis → thawing floor → reverse → crunch → confined c=1 heat → torus reseeds twist. **This is a story built from real parts, NOT a derivation.** Two theorems (BKL, Tolman) still stand against the bounce/cyclic rungs; scales (M⁴, decay const, ρ_bare sign) are tuned/chosen; the CC VALUE is untouched.

**The one falsifiable, data-touching output: the twist-floor DE sector — w₀>−1, thawing, reverse in tens of Gyr.** Everything else is past the observable edge. The next step is to DERIVE that w(z) as forced and confront it with DESI (analytic → CLASS fit), before red-team.

**What survives to red-team as genuine:** (i) the clamp-is-an-artifact / field-gives-dynamic-slow result; (ii) the forced-thawing direction (Barrel-E defusal); (iii) the sphere=0 / torus=maximal-twist theorem tying genesis to P-2026-013. **What does not:** the bounce (BKL), the cycle (Tolman), the CC value.

---

## THE BIREFRINGENCE DOOR ARC (2026-07-10, red-team t168-170) — the model's first distinctive-in-principle object, computed down

**Claim:** one complex field Psi=|Psi|e^{i theta}, three field-handles: |Psi|->mass (dyad),
theta->birefringence (theta F.Ftilde via the electron chiral anomaly), theta-dot->AD charge.
The birefringence coupling is NOT posited -- it is the anomaly shadow of the SAME lepton
coupling that gives the dyad (complex Yukawa + charged electron -> Fujikawa -> theta F.Ftilde).

**Three gates (scratchpad/birefringence_gates.py):**
- G1 structural: PASS. coupling FORCED by the anomaly (not a dial).
- G3 varying-alpha: PASS. phase is a PSEUDOSCALAR -> F.Ftilde only (parity-odd), induces ZERO
  varying-alpha; dyad's radial mode gives Delta a/a~2e-5 confined to z>50, quasar-BLIND, 208x
  under the CMB bound. The landmine that killed standalone varying-alpha cannot reach it.
- G2 magnitude: **FAILS at natural values** (red-team t169 decisive catch, accepted). The
  amplitude carries a hidden factor: beta = (alpha/2pi) N_e (m_Psi/m_e) Dtheta. The dyad needs
  only m_Psi VARIATION ~1.24% of m_e -> at that natural value beta~0.003 deg, 100x UNDER the
  measured 0.30 deg. Reaching 0.3 deg requires m_Psi/m_e~1 = m_e FULLY Psi-sourced = the t165
  DOOR (gate-0 BBN + hierarchy obstructed, the SAME wall #30 died on).

**The DESI<->beta correlation (what red-team CREDITED as real, first in 168 turns):** the SAME
twist Dtheta sets the DE thawing (w0>-1) AND beta. One field's twist, two skies -- LCDM+varying-
m_e CANNOT make this link. Structurally distinctive; N_e pinned by leptophilia (nothing to
cancel -> target A passes). This is the ontology's first distinctive-IN-PRINCIPLE object.

**The electron EDM (target B, scratchpad/electron_edm.py) -- the second blade, CUTS:** the same
complex Yukawa gives the electron a CP-odd coupling -> electron EDM. One-loop y_e^2-suppressed
(~1e-35, safe). But the TAU Barr-Zee (leptophilic includes tau) -> d_e~1e-26 e.cm = ~2000x OVER
JILA (4.1e-30), robust to the owed prefactor (factor-10 still 200x over). d_e~sin(phi)~beta ->
CANNOT suppress the EDM without killing the signal (exact correlation). Door + EDM are ONE WALL
FROM TWO SIDES: beta-large needs sin-phi-large + the door, which MAXIMIZES the Barr-Zee; the only
escape (heavier <Psi>) worsens the hierarchy.
  - NUANCE (def170, firewall both ways): the tau Barr-Zee needs Psi to couple to the TAU. The
    dyad is electron-(+neutrino-)specific; if Psi does NOT couple to mu/tau, the tau loop is
    absent and the EDM falls back to the SAFE one-loop. This ESCAPES the EDM but (a) does NOT
    open the door and (b) buys a "why only the electron" flavor-selectivity debit. EDM escapable;
    door is not.

**VERDICT (red-team t170, accepted):** the MECHANISM is real & LCDM-inaccessible, but THIS model
cannot wear it at observable amplitude -- both roads (universal-lepton = door+EDM dead;
electron-specific = door+flavor-puzzle) end at the #30 DOOR. SHOT 1 dented at t169, RE-CLOSED at
t170, stands FIRMER. Standing ~6-10% unchanged (birefringence was upside). The DOOR (m_e fully
Psi-sourced, beating gate-0 BBN + hierarchy + tau-Barr-Zee EDM) is now the WHOLE GAME for BOTH
#30 and birefringence -- one wall, three defenders.

**Also this session:** neutrino "clock" (quasar-blindness traces to the neutrino MASS SCALE:
heavier states go non-rel at z~16-94, above the quasar window; z=50 ~ 27meV, in-band, value not
derived; corrected a factor-3.15^2 error mid-computation); Job-3 null (the threshold has 2 jobs
not 3 -- the AD charge is genesis-set, 29 orders above the meV floor; "everything has 3 jobs"
FAILS its own test; the FIELD has 3 handles, objects inherit only what they couple to).
