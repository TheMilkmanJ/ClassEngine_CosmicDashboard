# VOID — construction package (void floor + RM / magnetism)

**Package:** `docs/working_logs/_runs/theory_construction_20260804/void_de_seating/`  
**Date:** 2026-08-04  
**Rule:** NO FABRICATIONS. **Do not close void from RM alone.** No MCMC. No PolyChord.  
**Wall ID:** W6 (void IGMF floor ×20); RM scale paid ≠ void close.

---

## Residual one-liner

**VOID:** inter-line B ≲ B_seed ≈ 5×10⁻¹⁸ G vs blazar ≳ 10⁻¹⁶ G — **×20 = 1.30 dex OPEN-BLOCKED** (WATCH-EXTERNAL blazar floor debate **or** named killable new seed; RM geometric scale paid, n_e amplitude OPEN).

---

## 0. Paid vs OPEN (status freeze)

| item | grade | evidence |
|---|---|---|
| Galactic Harrison seed B_seed ≈ 5×10⁻¹⁸ G at ω_vort ~ 0.5 H(rec) | **machine-backed / graded** (P-2026-028) | `docs/PRTOE_cosmic_magnetism.md` §2 |
| Vortex-network rms boost ×3400 on filaments/lines | recorded structure | §3 — does **not** raise inter-line floor |
| Return-flux theorem: inter-line CAP ≲ B_seed | theorem-blocked rescues | §3–§3a; `debt_magnetism_20260803` |
| Void shortfall B_void/B_seed = 20 = **1.30 dex** | **OPEN-BLOCKED** | arithmetic from recorded numbers |
| RM geometric two-point + multipole transfer (ξ_K → θ, ℓ) | **PAID** (scale) | `scripts/rm_coherence_kibble.py`; `debt_rm_formula_20260803` |
| Survey-plane RM feature | **ℓ ~ 25–60** (χ ~ 2–5 Gpc) | not ℓ_π≈169 (CMB-frame only) |
| Absolute σ_RM / C_ℓ amplitude | **OPEN** | needs **external n_e** |
| Bounce magnetic flip as turn engine | **failed / retired** | `scripts/bounce_magnetic_flip_nogo.py` (orthogonal) |

---

## 1. Recompute — RM geometric scale (this package)

```bash
OMP_NUM_THREADS=1 nice -n 19 python3 scripts/rm_coherence_kibble.py
```

**Log:** [`logs/rm_coherence_kibble.log`](logs/rm_coherence_kibble.log)  
**Exit:** 0  
**Verdict label:** **desk audit** (exit 0 ≠ PASS on void). Reconfirms:

| quantity | value |
|---|---|
| ξ_K | 256 Mpc comoving |
| χ_* | 13760 Mpc |
| θ_ξ(χ_*) | 1.066° ≈ 1.07° |
| ℓ_geo(χ_*) | 53.75 |
| ℓ_π(χ_*) | 168.86 (**CMB frame only** — not catalog RM prediction) |
| void shortfall printed | B_blazar/B_seed = **20** (1.30 dex) |
| void close? | **NO** — script explicitly refuses |

Survey-relevant multipoles from the same table:

| χ [Mpc] | θ_ξ [deg] | ℓ_π | class |
|---:|---:|---:|---|
| 2000 | 7.33 | 24.5 | typical EG |
| 3000 | 4.89 | 36.8 | deep EG |
| 5000 | 2.93 | 61.4 | high-z tail → **ℓ ~ 25–60** band |

**Amplitude non-claim:** σ_RM requires external \(n_e(\chi)\); corpus does not derive IGM/WHIM electron density. B_rms ≲ B_seed under return flux — using B_blazar as model B would invent the void field.

---

## 2. OPEN — void ×20 shortfall (priced, not closable at desk)

Arithmetic (corpus-only):

\[
\frac{B_{\mathrm{void}}}{B_{\mathrm{seed}}}
= \frac{10^{-16}}{5\times 10^{-18}} = 20,
\quad \log_{10} 20 = 1.30\,\mathrm{dex}
\approx\text{“1.5 orders”}.
\]

**Rescues closed without new physics:**

1. **Return-flux / line concentration** — flux conservation: return flux through void cell = cell-averaged flux ≲ B_seed. ×3400 boost is filament, not void floor.  
2. **Post-recombination vorticity persistence** — same average theorem; fails the same bound.  
3. **RM formula** — pays **scale** only; **cannot** raise B_inter-line.

**Live residual referee classes (only two honest doors):**

| door | name | what it does | kill condition |
|---|---|---|---|
| **A** | **WATCH-EXTERNAL** | blazar TeV-halo floor (Neronov–Vovk ≳10⁻¹⁶ G) may be relaxed by beam-plasma / cascade-plasma instabilities | floor **survives** debate → void column **fails** (galactic stands); floor **relaxes** below ~B_seed class → shortfall dissolves as *observational* claim |
| **B** | **named killable new seed** | licensed internal seed or amplification that is **not** bounded by B_seed under flux conservation | must be **named**, **file-pinned**, and **killable** before any compute (see §3) |

Desk re-integration of Harrison knobs alone **cannot** close the gap — priced arithmetic + theorem, not an uncomputed integral.

---

## 3. Construction options (honest)

### Option V1 — External blazar-data program (preferred credibility per hour)

**Program (desk literature + status card; no MCMC):**

1. Survey beam-plasma / plasma-instability challenges to Neronov–Vovk ≳10⁻¹⁶ G void floor.  
2. Write one-page status: floor **survives** | **relaxed** | **contested with threshold X G**.  
3. Map to model:

| external outcome | model disposition |
|---|---|
| floor ≳ 10⁻¹⁶ G holds | void column **fails**; P-028 galactic column **stands** |
| floor relaxed ≲ few ×10⁻¹⁸ G | shortfall **dissolves as falsifier**; no internal invention needed |
| contested intermediate band | keep **OPEN-BLOCKED**; quote band, not close |

**Does not invent internal seed.** Does not fake-complete P-028 void column.

**Pointer parents:** `debt_magnetism_20260803` §4.A; `PRTOE_cosmic_magnetism.md` §3; P-2026-028 honest gap in `PRTOE_PREREGISTERED_PREDICTIONS.md`.

### Option V2 — New seed premise (must be named and killable)

**Rule:** any internal close requires a **named** premise with a **kill band registered before compute**. Placeholder names below are **construction labels only** — **none is paid or invented as physics in this package.**

| label (killable stub) | premise shape | kill band (must exist *before* claim) | status **now** |
|---|---|---|---|
| **S-SEED-VOID-1** *Inter-line battery loophole* | named loophole to return-flux CAP with stated topology | if topology still enforces B_inter ≤ B_seed → **kill** | **NOT WRITTEN** — invent forbidden |
| **S-SEED-VOID-2** *Post-rec structure-scale dynamo in voids* | named void dynamo with efficiency η and coherence ξ | if η·B_seed never reaches 10⁻¹⁶ G under recorded η ceiling → **kill** | **NOT WRITTEN** |
| **S-SEED-VOID-3** *Separate primordial vector mode* | independent comoving B_void with amplitude formula | if formula free-fits blazar floor without independent kill → **kill as dial** | **NOT WRITTEN** |

**Construction discipline:** do **not** fill S-SEED-VOID-* with desk numbers. Opening any of them is an **owner foundations program**, not a residual arithmetic task.

### Option V3 — Permanent OPEN

Keep void floor **OPEN-BLOCKED** indefinitely:

- Document shortfall 1.30 dex (done, living residual freeze 2026-08-04).  
- Keep galactic column graded.  
- Keep RM scale paid / amplitude n_e-external OPEN.  
- Register risk in P-028: *if blazar floor holds, void column fails*.

**Permanent OPEN is a valid improvement** (honesty over false close). Default when V1 is not executed and V2 has no licensed axiom.

---

## 4. n_e amplitude (OPEN, separate from void)

| object | status |
|---|---|
| ⟨RM RM⟩ geometric structure | paid |
| unit w(θ)/w(0), ℓ_geo, ℓ_π | paid |
| absolute C_ℓ^{RM} / σ_RM | **OPEN** — external n_e + galactic RM cleaning + noise |
| free fit of filling factor / ad-hoc ξ_RM | **forbidden** |

**Construction for amplitude only:** adopt an *external* IGM n_e model (astrophysics, not PRTOE knob) and propagate CAP B_rms ≲ B_seed. Success = order-of-magnitude survey comparison; **fail condition** is not a void-floor close.

---

## 5. Forbidden (this wall)

1. Close void from RM geometric formula alone.  
2. Close void from Harrison B_seed alone.  
3. Use ×3400 rms as void / inter-line floor.  
4. Quote ℓ_π≈169 as “the” extragalactic RM prediction.  
5. Absolute σ_RM without external n_e.  
6. Invent B_void ≥ 10⁻¹⁶ G.  
7. MCMC / PolyChord of magnetogenesis parameters (out of scope).  
8. Bounce-from-magnetism reopen (nogo retired).

---

## 6. Authority sources (absolute paths)

- `/home/themilkmanj/prtoe_class/docs/PRTOE_cosmic_magnetism.md` — residual freeze 2026-08-04  
- `/home/themilkmanj/prtoe_class/docs/working_logs/_runs/debt_magnetism_20260803/REPORT.md`  
- `/home/themilkmanj/prtoe_class/docs/working_logs/_runs/debt_rm_formula_20260803/REPORT.md`  
- `/home/themilkmanj/prtoe_class/scripts/rm_coherence_kibble.py`  
- `/home/themilkmanj/prtoe_class/docs/working_logs/_runs/open_theory_full_20260804/rm_coherence.log` (prior reconfirm)  
- `/home/themilkmanj/prtoe_class/docs/working_logs/_runs/THEORY_WALLS_QUEUE_20260803.md` W6  

*NO FABRICATIONS. Void floor remains OPEN-BLOCKED.*
