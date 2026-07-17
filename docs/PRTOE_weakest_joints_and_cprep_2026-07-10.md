# PRTOE — Weakest Joints & C-Code Prep (2026-07-10 evening)

> *New reader? House terms decode in [PRTOE_READERS_GUIDE.md](PRTOE_READERS_GUIDE.md); claim conditionality maps in [PRTOE_DEPENDENCY_TREE.md](PRTOE_DEPENDENCY_TREE.md).*


Written after the gate-0 / neutrino-home session. Two parts: (A) the ranked weakest joints +
what would shore each, (B) the C-code scaffolding plan (PLAN ONLY — integration is GATED, see §B0).

---

## A. WEAKEST JOINTS (ranked by load-bearing × least-supported)

**J1 — The DE-floor VALUE ρ_inf^(1/4) = 2.3 meV. [RED — deepest]**
The entire DE sector + the neutrino tie rest on it. Status: UN-DERIVED. √(H₀M_Pl) is the
Λ-dominance tautology; the m_e→M₂→ρ_inf cascade is "kinship" (factor ~3-4); the shared-spurion
gives the RELATION not the value. Atlas fallback: it may be a "constitution" rule-constant
(un-derivable in principle, like ħ/c). **Shore:** accept as boundary data and bank the RELATION
reductions (DE↔m_ν), OR find a genuine value-derivation (hard; may not exist). Not buildable fast.

**J2 — Gate-0 dyad BBN clearance. [RED — empirical make-or-break]**
The +1.2% m_e shift (the load-bearing bolt) requires the dyad quiet at BBN. T_c is a COIN-FLIP
straddling the deuterium bottleneck (~70 keV), log-ambiguous 40–450 keV. **Shore:** the RG-improved
V_eff(φ,T) + BBN D/H network resolver (the working docket). BUILDABLE — this is the highest-leverage joint.

**J3 — DESI w=−1 (P-2026-018). [RED — external falsifier]**
If DESI DR2+ shows evolving DE, clean kill. Jointly squeezed with Σm_ν (can't relax one with the
other). **Shore:** none — it's a data verdict; the model must survive it. Watch, don't build.

**J4 — The +1.2% m_e shift being REAL. [the load-bearing bolt]**
A good FIT (ΔlnZ=+2.635) but SHOES-conditional, zero ontology evidence, NOT prediction-confirmed.
**Shore:** an INDEPENDENT m_e-shift detection — P-2026-007 (void/IGM m_e-step) + the quasar shape
bound. Buildable/observable; the single best way to move "flat".

**J5 — The two-field split + charged-lepton leptophilia portal. [ORANGE]**
The dyad needs a charge-free 2nd field with a lepton-specific portal (the Majoron forces only the
NEUTRINO coupling, not the charged-lepton dyad). **Shore:** the P-2026-020 leptogenesis
amplitude-follows-current derivation, OR an explicit lepton-specific portal (a Higgs portal would
break leptophilia).

**J6 — The shared-spurion tie. [ORANGE — post-hoc flagged]**
Needs a NEW falsifiable consequence beyond the whisper to earn credit (the working docket).

**J7 — DM abundance magnitude (η_B ~ 6×10⁻¹⁰). [ORANGE]**
Post-fragmentation the Q-ball charge IS the DM; the magnitude is [OBJECT-PENDING]. **Shore:** the
leptogenesis magnitude calc (ties to J5/P-020).

**TOP-3 make-or-break: J1 (DE value), J2 (gate-0 clearance), J3 (DESI w=−1).**
**Most buildable / highest-leverage: J2 (docketed) and J4 (independent m_e detection).** J1 may be
constitutional; J3 is a data verdict.

---

## B. C-CODE PREP PLAN (scaffolding map — PLAN ONLY)

### B0. GATE (do not skip)
Integration is GATED on **both**: (a) confidence on the new model **>85%**, and (b) gate-0
resolver (docketed) landing **clear**. Confidence assessed as insufficient → **NO INTEGRATION THIS PASS.**
This section is a map so the eventual fix drops in without syntax/missing-piece thrash. **No
active-code changes are made.**

### B1. Current surface (recon)
- `include/background.h`: `dcdf_rho_inf`, `dcdf_z_rad_onset` (docketed; conformal onset), `dcdf_conv_g/at/n`
 (DM→DE/dark-rad conversion); inline `dcdf_s_of_rho`, `dcdf_rho_rad`, `dcdf_conv_rate`.
- varying-m_e: via CLASS `varying_fundamental_constants` (instantaneous step at
 `varying_transition_redshift`, currently z=50 — a HARD STEP, not the order-parameter ramp).

### B2. What the new model changes (when unlocked)
1. **Dyad as a thermal order parameter, not a z=50 step.** Replace the hard step with a smooth ramp
 φ(T)/v = √(max(0, 1 − T/T_c)), so δm_e/m_e = ε·(φ/v)² turns on continuously below T_c.
 New param: `dcdf_dyad_Tc` (condensation temperature, ~keV, the output). `Tc<=0` disables →
 recovers the current step (backward-compatible, like the `z_rad_onset<=0` guard).
2. **Two-field bookkeeping.** Field 1 = existing dcdf (charge/DM+DE). Field 2 = dyad (charge-free).
 Only field 2 sources δm_e; field 1 stays as-is. Minimal: one new ramp function, one new param.
3. **Amplitude:** ε = 1.24% stays the derived dyad amplitude (`c·f_amp·Ψ₀/M_red`); NOT a new knob.

### B3. Where each change lands (map)
- `include/background.h`: add `double dcdf_dyad_Tc;` to the struct; add inline
 `dcdf_dyad_ramp(pba, a)` next to `dcdf_rho_rad` (same guard pattern).
- `source/input.c`: read `dcdf_dyad_Tc` (default 0 = disabled); validate ≥0.
- `source/background.c`: wire `dcdf_dyad_ramp` into the varying-constant m_e call so
 m_e(a) = m_e_lab·(1 + ε·ramp²) replaces the instantaneous step when `dcdf_dyad_Tc>0`.
- `source/perturbations.c`: no new structure — the m_e change propagates through the existing
 recombination/Thomson path (varying-constants already hooked there). Verify only.

### B4. Order of operations (when unlocked)
#40 clears → set ε, T_c from the resolver → add the param + ramp (B3) behind the `Tc<=0` guard →
`make -j12` → diff CMB vs the step version at fixed ε → only then wire as default. Backward-compatible
at every step (guarded), so a syntax error or missing piece can't corrupt the working step model.

---

## JOINTS UPDATE (same day, post-atom-night)

- **J2 (gate-0) — RESOLVED**: cleared via the double sign-correction, re-signed as a HEAL
 (T_c = 193 keV, +0.06σ D/H, zero Y_p tax). The wall was a pharmacy.
- **J1 (the DE value) — RECLASSIFIED**: not constitutional-forever; **the cosmic Rydberg** (
 whisper: ½α_c²M₂ = 1.98 vs 2.25 meV; graduation teeth set).
- **J3 (DESI) — HARDENED BY THE MODEL ITSELF**: the grammar derives w = −1 today (mass-defect
 O(δ²)); DR3 is now a pure kill-or-confirm on a derived commitment.
- **J4 (m_e real) — new instruments**: P-022 (21cm), P-024 (the ε-dipole), the radio ratio-lock.
- **J5–J7 — became the open-derivation set** (spine §14): the portal embodied (vector-like candidate),
 the abundance routed (genome→CP→η), v_L benchmarked.

## JOINTS UPDATE 2 (2026-07-11, the radio night)

- **J1 (the DE value) — COMPUTED AT 20%, ZERO DIALS:** ρ_inf^¼ =
 ½α_c²M₂/(16π²α_c^{3/2})^¼ = 2.695 vs 2.25 meV. Bohr binding × Landau-capped collective
 zero-point (pair-breaking = E_b = 2Δ) × BEC phonon speed (c_s = √α_c). The 0.4% "match"
 retired as prefactor-naive; scope held cold: the MODEL's floor value, not the CC problem writ
 large. J1 is no longer RED — it is a candidate-derivation with a 20% honest O(1).
- **J2 (gate-0) — PRODUCTION-ABSOLUTE:** clean PRyM: ∂ln(D/H)/∂ln m_e ≈ 0. The D/H pharmacy
 died with it; Y_p is the true medicine (+0.65σ); the dyad owns a D/H-widening discriminator
 (ramped: 2.387 vs Cooke 2.527; the fork's width is owed — see the witness; was 2.372 pre-window) with the radio D-line (P-027) as referee.
- **J4 gains the sharpest instrument:** the two-line ratio-lock (ν_H/ν_D = 4.338649 preserved,
 both lines +2.50% at z>50).
- **NEW STANDING RISK:** the D/H fork (ramped bet: 2.387 vs the quasar 2.527; width owed) AND the Y_p reversal (+1.09σ counter, ramped — the medicine was an artifact).
- **THE ε JOINT RESTRUCTURED:** ε = c·f̄·α_c — f_amp moved draw→winding-average
 (f̄ = 0.644 ± 0.03, pending t-grade + 512-run); c = 0.90 ± 0.04 implied, the remaining O(1).
- **C-code gate RESET:** >85% deleted; PolyChord is the gate (the claim is held
 provisional until it runs).
