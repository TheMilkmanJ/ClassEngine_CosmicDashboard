# Debt report — Cosmic magnetism void floor + RM coherence formula

> **SUPERSEDE NOTE (2026-08-03):** §3 “RM formula MISSING” is **stale**.  
> Same-day paydown: `docs/working_logs/_runs/debt_rm_formula_20260803/REPORT.md` + `scripts/rm_coherence_kibble.py`  
> — **RM geometric scale paid** (survey-plane ℓ~25–60).  
> **Void floor residual still OPEN** (this report §§1–2 still govern).  
> Do not read RM geometry as void-floor close. Audit: `DEBT_HONESTY_AUDIT_20260803.md`.


**Run id:** `debt_magnetism_20260803`  
**Date:** 2026-08-03  
**Worker:** blue-team science (desk audit; no MCMC)  
**Primary sources:** [`docs/PRTOE_cosmic_magnetism.md`](../../../PRTOE_cosmic_magnetism.md) (§2–§3a, §6); P-2026-028 in [`docs/PRTOE_PREREGISTERED_PREDICTIONS.md`](../../../PRTOE_PREREGISTERED_PREDICTIONS.md); [`scripts/bounce_magnetic_flip_nogo.py`](../../../../scripts/bounce_magnetic_flip_nogo.py)  
**Scripts searched:** `scripts/*magnet*` → only `bounce_magnetic_flip_nogo.py` (polarity/turn nogo; uses void-floor budget, does not price the shortfall). No dedicated IGMF/void-floor/RM script exists.

---

## 0. Script run (quick, `nice -n 19`)

```text
nice -n 19 python3 scripts/bounce_magnetic_flip_nogo.py
```

**Result (reconfirmed):** polarity reversal / magnetic energy as bounce *turn mechanism* **FAIL by class** — Maxwell stress is quadratic in B (flip invisible to gravity); ρ_B positive and frozen-ratio radiation-class (void floor ρ_B / ρ_rad0 ≈ 5.8×10⁻²²; CMB cap ≈ 5.8×10⁻⁸). **Orthogonal to the void-floor gap:** the script prices energy budget, not B_inter-line vs blazar.

Output also saved conceptually: assert path clean; no new seed number produced.

---

## 1. What the model predicts for void B floor vs blazar TeV (~10⁻¹⁶ G)

Numbers as recorded in `PRTOE_cosmic_magnetism.md` §2–§3a and the §6 ledger (also P-2026-028 prereg):

| quantity | value | role | citation in corpus |
|---|---|---|---|
| B_seed (smooth Harrison) | **≈ 5×10⁻¹⁸ G** | model seed at ω_vort ~ 0.5 H(rec); galactic bill | §2 / P-2026-028 |
| B formula | B ≈ 2 (m_p c / e) · ω_vort | Harrison battery from structural vorticity | §2; [Harrison1970] |
| vortex-network rms boost | **×3400** | concentrates B on filaments/lines | §3 |
| B_inter-line (void floor *from model*) | **≲ B_seed ≈ 5×10⁻¹⁸ G** | flux conservation: return flux through void cell = cell-averaged flux | §3, §3a |
| B_void observational floor | **≳ 10⁻¹⁶ G** | blazar TeV-halo bound (missing cascade halos) | §0, §3a; [NeronovVovk2010] / BIBLIOGRAPHY |
| CMB comoving cap | ~10⁻⁹ G | upper bound on primordial comoving field | §0; bounce script constant |

**Prediction summary (honest):**

- **Galactic column (paid):** structural vorticity → Harrison seed ~5×10⁻¹⁸ G → dynamo-viable. Graded, registered P-2026-028.
- **Void / inter-filament column (open):** under flux conservation the model’s *inter-line* field stays at the **smooth seed class (~5×10⁻¹⁸ G)**. It does **not** predict a void floor at or above the blazar ≳10⁻¹⁶ G. The ×3400 line boost does not raise the inter-line floor (return-flux theorem). Post-recombination vorticity persistence sources the same average and fails the same bound.

So vs blazar TeV (~1e-16 G): **model void floor ~1.5 orders low; the void column is not explained by existing internal formulas.**

---

## 2. Gap size (~1.5 orders)

Arithmetic from recorded numbers (`PRTOE_cosmic_magnetism.md` §3a, 2026-08-02 pricing):

| | |
|---|---|
| B_void / B_seed | 10⁻¹⁶ / 5×10⁻¹⁸ = **20** |
| shortfall in decades | log₁₀(20) = **1.30 dex** |
| registered phrasing | **≈ "1.5 orders"** (§3 smooth estimate; PREREGISTERED “~1.5 orders”) |

**Two of three rescues closed** (same §3 / prereg):

1. Return-flux / line concentration — **fails** flux conservation.  
2. Post-recombination vorticity persistence — **fails** same average theorem.  
3. Live residual referee: **external robustness of the blazar floor** (beam-plasma instabilities may relax ≥10⁻¹⁶ G entirely). If the floor survives that debate, **void column fails; galactic column stands**.

The shortfall is **priced arithmetic + a theorem**, not an uncomputed integral that desk re-integration can fix without new physics content.

---

## 3. RM coherence formula: derived, partial, or missing?

**Status: MISSING (formula not written).** Ledger grade: **Open — formula missing** (`PRTOE_cosmic_magnetism.md` §3a, §6; `_FILE_COMPLETION_STATUS.md`).

| object | status |
|---|---|
| Qualitative claim | **Partial / qualitative only** — Kibble network sets ~100-Mpc-class comoving structure (ξ_K = 256 Mpc domain size recorded); distinctive vs phase-transition micro-coherence |
| ⟨RM(θ)·RM(0)⟩ | **No recorded expression** |
| ξ_K → angular multipole transfer | **Not done** |
| Comparison to RM surveys | **Not done** (“un-priced in RM statistics (owed if pursued)”) |

**Not derived.** Closing RM debt requires *writing and evaluating* the Faraday-rotation-measure correlation from the Kibble seed geometry — not available as an existing corpus number. Helicity-sign identities in §4 (sign(H_B) = sign(H_kin), etc.) are separate and do **not** supply the RM two-point formula.

---

## 4. Concrete NEXT computation that could close or kill the gap

**Void shortfall cannot be closed by re-running Harrison with existing knobs** — §3a states no internal formula raises B_inter-line above B_seed under flux conservation without inventing content.

**Concrete next (desk-scale, kill-or-sharpen; no MCMC):**

### A. Preferred: external blazar-floor status pass (can kill void column or retire the gap as falsifier)

1. Literature desk on beam-plasma / plasma-instability challenges to the Neronov–Vovk ≳10⁻¹⁶ G void floor (the live external referee named in §3 and P-2026-028).  
2. Output a one-page status: floor **survives** → void column **fails** (kill registered); floor **relaxed** below ~5×10⁻¹⁸ G class → shortfall **dissolves as observational claim**, galactic seed unchanged.  
3. Does **not** invent an internal seed; does **not** fake-complete P-028’s void column.

### B. RM formula write (closes RM debt; does not close void B gap)

1. Write ⟨RM(n̂₁) RM(n̂₂)⟩ for a line-of-sight integral of n_e B_∥ with B structured on Kibble network ξ_K = 256 Mpc (toy: filament/void two-phase or vortex-line Poisson process with recorded return-flux average B̄ ≲ B_seed).  
2. Project to angular multipoles C_ℓ^{RM} (or angular correlation vs θ); mark the characteristic scale θ ~ ξ_K / χ(z) for a chosen source plane.  
3. Confront order-of-magnitude with existing extragalactic RM catalog correlation scales (qualitative band only unless survey noise allows).  
4. **Success condition:** quantitative RM coherence prediction registered; **fail condition:** if only micro-scale coherence survives processing, distinctive ~100 Mpc claim weakens — separate from void floor arithmetic.

### C. Explicitly **not** next without new content

- Re-pricing ×3400 rms as a void floor (theorem-blocked).  
- MCMC of magnetogenesis parameters.  
- Inventing a third internal seed that violates flux conservation without a stated loophole.

**Honest joint outcome:** A decides whether the void *falsifier* still bites; B pays the named RM formula debt. Neither is “the void floor is now 10⁻¹⁶ G from the model.”

---

## 5. Non-claims

Do **not** claim or promote:

1. That the model **explains** the blazar void floor ≳10⁻¹⁶ G — it does not; shortfall is open and priced.  
2. That the ×3400 vortex boost **raises** the inter-line void field — flux conservation forbids that rescue.  
3. That an **RM coherence formula** or multipole prediction **exists** in the corpus — missing.  
4. That **helicity sign = baryon/matter sign** is testable here — §4: joint draw independent; link void; Fermi IGMF not a genome datum through that chain (T14).  
5. That **bounce / polarity flip** is powered by cosmic B — `bounce_magnetic_flip_nogo.py` FAIL by class (orthogonal).  
6. That CMB ~nG cap is saturated by this seed — seed is ~5×10⁻¹⁸ G class, far below.  
7. That dark-charge currents seed B — Meissner/photon-mass forces EM-neutrality; stir only.  
8. Completion of P-028’s void column or of “cosmic magnetism debt” overall — **OPEN-THEORY**; galactic seed paid, void + RM open.  
9. Any MCMC posterior, survey fit, or “gap closed” without A/B above executed and logged.

---

## 6. Ledger snapshot (no status change claimed)

| item | status after this debt pass |
|---|---|
| Galactic Harrison seed ~5×10⁻¹⁸ G | still **computed / graded** (P-028) |
| Void floor vs blazar | still **open**, shortfall **1.30 dex (×20)** priced |
| RM ⟨RM·RM⟩ | still **formula missing** |
| bounce magnetic flip as turn | **nogo reconfirmed** (not a seed rescue) |
| This report | **audit only** — no fake completion |

---

## Sources (corpus paths)

- `/home/themilkmanj/prtoe_class/docs/PRTOE_cosmic_magnetism.md` — full read; void §3–§3a, RM, ledger §6  
- `/home/themilkmanj/prtoe_class/docs/PRTOE_PREREGISTERED_PREDICTIONS.md` — P-2026-028 honest gap  
- `/home/themilkmanj/prtoe_class/docs/BIBLIOGRAPHY.md` — [NeronovVovk2010], [Harrison1970]  
- `/home/themilkmanj/prtoe_class/docs/working_logs/_FILE_COMPLETION_STATUS.md` — OPEN-THEORY; RM formula missing  
- `/home/themilkmanj/prtoe_class/scripts/bounce_magnetic_flip_nogo.py` — run 2026-08-03, nice -n 19  

*End of report. No MCMC. No fake completion.*
