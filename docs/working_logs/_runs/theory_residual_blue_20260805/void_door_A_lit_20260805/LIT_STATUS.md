# LIT_STATUS — External blazar / IGMF void-floor literature (Door A)

**Package:** `docs/working_logs/_runs/theory_residual_blue_20260805/void_door_A_lit_20260805/`  
**Date:** 2026-08-05  
**Worker:** Grok BLUE (PRTOE)  
**WEB_PASS:** **run** (web_search + web_fetch sample, 2024–2026 focus + classic anchors)  
**Corpus priors:** `docs/PRTOE_cosmic_magnetism.md` §3–§3a; `debt_magnetism_20260803/REPORT.md`; `void_de_seating/VOID.md`; MASTER D6  
**Rule:** sample status only. **No invent boost.** No close of void from RM or Harrison.

---

## 0. Model numbers under test (corpus, unchanged)

| quantity | value | source |
|---|---|---|
| B_seed (smooth Harrison) | **≈ 5×10⁻¹⁸ G** | P-2026-028 / magnetism §2 |
| Corpus falsifier floor (classic) | **≳ 10⁻¹⁶ G** | [NeronovVovk2010]; magnetism §3a |
| shortfall (classic floor) | **×20 = 1.30 dex** | 10⁻¹⁶ / 5×10⁻¹⁸ |
| inter-line CAP | **≲ B_seed** | return-flux theorem |
| Door A dissolve threshold | floor relaxed **≲ few ×10⁻¹⁸ G** (~seed class + small margin) | `void_de_seating/VOID.md` Door A |
| Door A model-FAIL condition | floor **survives** debate at ≳10⁻¹⁶ G class | debt §4.A; magnetism §3 |

---

## 1. What current public results claim (sampled)

### 1.1 Classic / aggressive blazar cascade floors (still cited)

| ref | claim | coherence / notes |
|---|---|---|
| **Neronov & Vovk 2010** (*Science*) | **B ≥ 3×10⁻¹⁶ G** | Non-detection of GeV cascade from TeV blazars; corpus anchor (≳10⁻¹⁶ G) |
| **Aharonian et al. 2023** (H.E.S.S. + Fermi-LAT, *ApJL* 950 L16) | **B > 7.1×10⁻¹⁶ G** (95%-class) for λ_B = 1 Mpc | Holds for blazar duty cycles as short as **10 yr**; **stronger** than classic 10⁻¹⁶ if adopted |
| Early / contemporaneous blazar work (Tavecchio 2010 class, etc.) | B ≳ few×10⁻¹⁵–10⁻¹⁶ G band | Duty-cycle / jet-angle systematics |

**Implication if this class is taken as the void floor:** shortfall **worsens** (×20 → ~×140 for 7.1×10⁻¹⁶).

### 1.2 Robust / conservative blazar floors (variability-limited)

| ref | claim | notes |
|---|---|---|
| **Acciari et al. 2023** (MAGIC + Fermi/LAT, 1ES 0229+200, *A&A* 670 A145) | **B > 1.8×10⁻¹⁷ G** (long-correlation-length class); weaker robust line **B > ~10⁻¹⁷ G** | Uses **measured** VHE variability / finite activity — discards Myr duty-cycle assumption |
| Keita et al. 2026 (CTAO GRB projection paper; arXiv:2604.25647) summary of state | “weaker but significantly more robust limits, up to **~2×10⁻¹⁷ G**” (citing Acciari 2023 + Blunier et al. 2026) | Frames classic pair-halo limits as assumption-heavy |

**Implication if only this class is the floor:** shortfall shrinks but **does not dissolve**:
- B > 1.8×10⁻¹⁷ vs seed 5×10⁻¹⁸ → ratio **~3.6** ≈ **0.56 dex** still OPEN  
- B > 2×10⁻¹⁷ → ratio **~4** ≈ **0.60 dex** still OPEN  

Still **above** Door A dissolve band (≲ few×10⁻¹⁸ G).

### 1.3 GRB pair-echo floors (duty-cycle free; plasma-growth resistant)

| ref | claim | notes |
|---|---|---|
| **Burmeister et al.** (Fermi-LAT GRB 221009A; arXiv:2512.11128, 2025/2026) | Rules out **B < 2.5×10⁻¹⁷ G** at 95% CL for λ_B ≳ 1 Mpc (i.e. **B ≳ 2.5×10⁻¹⁷ G**) | Full Poisson likelihood; up to ~1 yr post-trigger; **no duty-cycle assumption**; activity time ≪ plasma-instability growth → **not** subject to Broderick-class quench argument for this source |
| Earlier GRB 221009A / 190114C analyses | ~10⁻¹⁸–10⁻¹⁹ G class or null (method-dependent) | Superseded in strength by Burmeister-class result when it applies |
| Keita et al. 2026 CTAO sim | Existing LST-1 data on GRB 221009A **favour ~3×10⁻¹⁷ G** (not a firm measurement); CTAO projected to probe up to ~10⁻¹⁵ G | Forward-looking, not a settled floor move |

**Implication:** best modern **plasma-resistant** lower bound sits at **~2–3×10⁻¹⁷ G** — still **~5×** above B_seed (≈ **0.7 dex** short if this is the sole floor).

### 1.4 Plasma-instability challenge (the live external referee named in corpus)

| ref / class | claim | effect on floor |
|---|---|---|
| Broderick, Chang & Pfrommer 2012 (and follow-ons) | Pair-beam plasma instabilities may cool pairs before IC cascade → cascade absence **without** strong B | Would **relax** classic blazar floor if fully effective |
| **Arrowsmith et al. 2025** (*PNAS* / arXiv:2509.09040) lab analogue | Pair-beam instability **suppressed** if beam is not perfectly collimated/monochromatic → **supports robustness** of IGMF lower limits from cascade absence | Pushes **against** full dissolve of the floor via plasma route |
| Parametric cascade+instability studies (2026 sample: Alawashra; Dey et al.) | With instability cooling parameterized, lower limits can drop toward **~10⁻¹⁷ G** class rather than vanish | Contests **classic 10⁻¹⁶**, does **not** drive floor to seed class |

**Status of referee:** **contested, not resolved in model’s favor.** Lab trend 2025 leans *against* full plasma quench; parametric work can soften classic floors to ~10⁻¹⁷ but not below seed+margin.

---

## 2. Does any public result **kill** the ×20 short or move the floor?

| question | answer (this pass) |
|---|---|
| Does literature move the observational floor **below seed+margin** (≲ few×10⁻¹⁸ G)? | **NO** |
| Does literature establish uncontested survival of classic ≳10⁻¹⁶ G (model void FAIL)? | **NO** — duty cycle + plasma still debate classic number |
| Does a **robust** lower bound still sit **above** B_seed? | **YES** — ~1–3×10⁻¹⁷ G class (MAGIC variability; GRB 221009A) |
| If one demotes falsifier from 10⁻¹⁶ → 2.5×10⁻¹⁷ only, what remains? | shortfall **×5 ≈ 0.70 dex** (still OPEN; not dissolve) |
| If one keeps HESS+Fermi 7.1×10⁻¹⁶, what remains? | shortfall **~×142 ≈ 2.15 dex** (worse) |
| Plasma route kill of floor? | **Not established**; Arrowsmith 2025 weakens the kill path |

### Band summary (honest intermediate)

```text
                    seed          robust lower         classic / HESS
               5e-18 G    …    1–3e-17 G      …     1e-16 – 7e-16 G
                   |              ||||                   ||||
                   |              ^^^^ Door A still bites ^^^^
                   |              (not below seed+margin)
                   +-- dissolve zone only if floor falls left of here
```

**No public result sampled here kills the residual arithmetic against the model seed, nor moves the floor into the Door A dissolve zone.**

---

## 3. Tension with model seed (priced)

| floor assumption | B_floor | B_floor / B_seed | dex short | Door A disposition |
|---|---:|---:|---:|---|
| Classic corpus falsifier | 1×10⁻¹⁶ G | **20** | **1.30** | OPEN-BLOCKED (contested) |
| Neronov–Vovk 2010 number | 3×10⁻¹⁶ G | 60 | 1.78 | OPEN-BLOCKED if held |
| HESS+Fermi 2023 | 7.1×10⁻¹⁶ G | ~142 | ~2.15 | OPEN-BLOCKED if held |
| MAGIC robust 2023 | 1.8×10⁻¹⁷ G | **~3.6** | **~0.56** | intermediate; still short |
| GRB 221009A 2025/26 | 2.5×10⁻¹⁷ G | **5** | **0.70** | intermediate; still short |
| Dissolve threshold | ≲ few×10⁻¹⁸ G | ≲ O(1) | ~0 | **not reached** |

**Internal rescues remain theorem-blocked** (return-flux; post-rec vorticity; RM scale ≠ B boost). External lit does **not** supply a free internal third seed.

---

## 4. Sources sampled (this WEB_PASS)

**Anchors / classic**
- Neronov & Vovk 2010, *Science* 328, 73 — B ≥ 3×10⁻¹⁶ G  
- Broderick, Chang & Pfrommer 2012, *ApJ* 752, 22 — plasma instability challenge  

**2023–2026 lower bounds**
- Aharonian et al. 2023 (H.E.S.S. + Fermi-LAT), *ApJ* 950 L16 — B > 7.1×10⁻¹⁶ G (λ=1 Mpc, duty ≥10 yr)  
- Acciari et al. 2023 (MAGIC + Fermi), *A&A* 670 A145 — B > 1.8×10⁻¹⁷ G (variability-robust)  
- Burmeister et al., arXiv:2512.11128 (2025) — GRB 221009A Fermi-LAT; B ≳ 2.5×10⁻¹⁷ G (95% CL); plasma-resistant  
- Keita et al., arXiv:2604.25647 (2026) — CTAO GRB projections; status review of halo/echo limits  

**Plasma / instability status**
- Arrowsmith et al. 2025, arXiv:2509.09040 / *PNAS* — lab: instability suppressed → IGMF limits more robust  
- Alawashra et al. 2026 (Frontiers / related) — pair-beam plasma reviews; parametric lower limits ~10⁻¹⁷ G class with instability cooling  

**Corpus (non-web)**
- `docs/PRTOE_cosmic_magnetism.md`  
- `docs/working_logs/_runs/debt_magnetism_20260803/REPORT.md`  
- `docs/working_logs/_runs/theory_construction_20260804/void_de_seating/VOID.md`  
- `docs/working_logs/_runs/MASTER_CLOSURE_DASHBOARD_20260803.md` D6  

*WEB_PASS complete. Sample is status, not exhaustive meta-analysis. No floor invent; no model B_void invent.*
