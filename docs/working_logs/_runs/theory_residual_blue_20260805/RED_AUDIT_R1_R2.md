# RED AUDIT — R1 (first-grade three residual surfaces) + R2 (T-X6 enumeration)

**Seat:** Claude CLI (interactive red). **Date:** 2026-08-05.
**Authority:** owner instruction — "Pay R1 and R2". Package write only; no living `docs/PRTOE_*.md` touched, no chain touched.
**Method:** whole-file reads of every graded artifact; every number recomputed from the artifact by this seat, not read from a log or from blue's prose.

---

## Aggregate

| grade | n |
|---|---:|
| AGREE | 0 |
| **AGREE-IF** | **4** |
| DENIED | 0 |
| **COMPLETE physics** | **0** (unchanged — nothing here moves physics) |

Four AGREE-IF, each with one named cure. No finding here reverses a blue verdict: every headline disposition blue filed (T8 still FAIL, both n-residuals still open, void still OPEN-BLOCKED) is **confirmed**. The cures are precision defects, and one of them runs *against* the model rather than for it.

---

## R1a — Page T8 bin-phase qualifier · **AGREE-IF**

### Reproduced exactly

Recomputed from the champion artifact directly, using the tool's own T8 definition
(`scripts/page_protocol_scorecard.py:328-405`: bins `floor(u/0.01)` on `u` = max-envelope `v`,
ratio = range(S)/S★, S★ = global max S):

| quantity | blue | red recompute | |
|---|---|---|---|
| artifact sha256 | `048de43e…2fca8` | `048de43e1bc766c8f420c54f565a33166c0792c23291ba567cdc6c772f92fca8` | ✔ |
| S★ | — | 0.016688199517780646 | — |
| worst bin (offset-0) | [0.10, 0.11) n=12 | [0.10, 0.11) n=12 | ✔ |
| ratio | 0.11315435176934464 | 0.11315435176934464 | ✔ **17 s.f.** |
| neighbour [0.11,0.12) | ≈ 0.092909 | 0.092909 | ✔ |
| neighbour [0.12,0.13) | ≈ 0.096240 | 0.096240 | ✔ |
| failing bins at offset-0 | 1 | 1 | ✔ |
| max failing bins, any phase | "up to 3" | 3 (phases 0.35, 0.40) | ✔ |
| T8_pass · page_curve_claimed | False · false | False · false (read from artifact) | ✔ |

### The defect — a superlative that is not one

> **Worst alternate** | worst-ratio ~**0.125** (reported 0.125313)

**This is not the worst.** Red swept 400 binning phases across one bin width:

- worst ratio found: **0.133022** at phase 0.5275
- **94 of 400** sampled phases exceed blue's reported 0.125313

0.125313 is the value at phase ≈ 0.60. It is *a* phase's ratio reported as *the* worst.

This is the F2 failure mode again — a maximum over a scan quoted as a maximum — and it is worth
saying plainly that here the error runs **against** the model: the true phase family is *worse*
than blue reported, so this is not grade inflation. It is still a defect, and in a document whose
entire purpose is claim precision it is the defect that document exists to prevent.

**Red's own limit, stated so it is not repeated:** 0.133022 is likewise a **400-phase scan bound**,
not a maximum. The honest form is `≥`, and red files it that way.

### Cure to lift to AGREE

Restate the row as a bound with its sampling declared:
*"worst alternate-phase ratio ≥ 0.1330 over 400 sampled phases (blue's 0.1253 is the value at phase ≈0.60, not the family maximum); up to 3 failing bins."*

Everything else in the file stands, including the forbidden-language table, which is correct as written.

---

## R1b — n / L_gen shared upstream · **AGREE-IF**

### Every citation resolves; every number recomputed

| claim | where red found it | |
|---|---|---|
| Wilson slot 3 = `winding_background_n`, MISSING | `theory_construction_wave_20260805/wilson/MASTER.md:49` | ✔ |
| Baryo claims-ledger **row 9** verbatim | `docs/PRTOE_baryogenesis.md:242` | ✔ |
| Kibble expression `n_rms = √(L_gen/ξ_K)/2π` | `docs/PRTOE_baryogenesis.md:62` | ✔ |
| Docket **#180** text | `docs/working_logs/_DOCKET_INDEX.md:228` | ✔ |
| factor 122 at the favourable end | `docs/PRTOE_baryogenesis.md:58`, `:69` | ✔ |

Independent arithmetic:

| quantity | doc | red |
|---|---|---|
| n at torus floor (L=27.6 Gpc, ξ_K=256 Mpc) | n ≳ 1.65 | **1.6526** |
| band 10–30 vs floor | factor 6.1–18.2 | **6.05 – 18.15** |
| L needed for n=10 / n=30 | 37× / 330× floor | **36.6× / 329.6×** |

All confirmed.

### The defect — the coupling is asserted at the top and conceded at the bottom

The one-line claim states the two seats **"share the same upstream object: the genesis winding integer n."**
But the file's own closure route 2 reads:

> 2. Independent licensed determination of family-triangle winding **that is proven identical to genesis n**

That "proven identical" is the whole coupling. If the identity needed proof at the bottom of the file,
it cannot be asserted as established at the top. The file fences one conflation carefully
(Widnall / CMB-comb *n* is "a different object") and then performs a second, unfenced one:
Wilson's requirement is a **family-triangle** winding background in the dark gauge sector,
while row 9's *n* is the **genesis** Kibble winding integer. Nothing on disk establishes they are one object.

The booking is still worth having — if the identity holds, one pin serves both. It is the mood that is wrong, not the idea.

### Cure to lift to AGREE

Make the headline conditional: *"**If** the family-triangle winding background is the genesis n — an identity that is itself unproven and is carried as closure route 2 — then one licensed determination feeds both residuals."*
The non-claims table already forbids everything else it needs to forbid.

---

## R1c — void Door A lit pass · **AGREE-IF**

### Verdict confirmed, arithmetic confirmed

`OPEN-BLOCKED`, FAIL not fired, lands 0. Red recomputed the whole tension table against B_seed = 5×10⁻¹⁸ G:

| floor | ratio (doc) | red | dex (doc) | red |
|---|---|---|---|---|
| classic 1×10⁻¹⁶ | 20 | **20.0** | 1.30 | **1.301** |
| Neronov–Vovk 3×10⁻¹⁶ | 60 | **60.0** | 1.78 | **1.778** |
| HESS+Fermi 7.1×10⁻¹⁶ | ~142 | **142.0** | ~2.15 | **2.152** |
| MAGIC 1.8×10⁻¹⁷ | ~3.6 | **3.6** | ~0.56 | **0.556** |
| GRB 2.5×10⁻¹⁷ | 5 | **5.0** | 0.70 | **0.699** |

Every row checks.

### Citations — split into what red can and cannot certify

**Certified** (real papers, correctly quoted, from red's own knowledge):
Neronov & Vovk 2010 (*Science* 328, 73) · Broderick, Chang & Pfrommer 2012 (*ApJ* 752, 22) ·
Aharonian et al. 2023, H.E.S.S.+Fermi (*ApJL* 950 L16, B > 7.1×10⁻¹⁶ G at λ_B = 1 Mpc) ·
Acciari et al. 2023, MAGIC (*A&A* 670 A145, B > 1.8×10⁻¹⁷ G, variability-robust).

**NOT certified by red — three rows:**

| ref | why red cannot certify |
|---|---|
| Burmeister et al., arXiv:2512.11128 | no recall; no network in this environment |
| Keita et al., arXiv:2604.25647 | no recall; no network in this environment |
| Arrowsmith et al. 2025, arXiv:2509.09040 / *PNAS* | no recall of this specific item; no network |

**Red does not certify these and does not deny them.** This environment has no outbound network
(a probe hung and was killed), so no seat here can resolve them; that is a limit on red, not a
finding against blue.

### The point that matters, and it favours blue

**Strike all three unverified rows and the verdict survives unchanged.** The OPEN-BLOCKED grade needs
only three things, and each rests on a certified source:

1. floor not moved below the dissolve band (≲ few×10⁻¹⁸ G) — no certified source does;
2. classic ≳10⁻¹⁶ G not uncontested — Broderick 2012 alone contests it;
3. a robust floor still above seed — MAGIC's 1.8×10⁻¹⁷ G is 3.6× the seed on its own.

So the grade does **not** rest on the unverifiable rows. They add strength; they carry no load.
The single place they do carry weight is the REPORT criterion *"Plasma route fully relaxes floor? **NO**"*,
which cites Arrowsmith as positive evidence. Without it the answer is still NO, but for the weaker
reason that no certified source establishes the relaxation — absence of establishment, not evidence against.

### Cure to lift to AGREE

Tag the three rows **`red-unverified 2026-08-05 (no network at audit time)`**, and restate the plasma
criterion as *"not established"* rather than *"lab trend leans against"* unless a seat with network
confirms Arrowsmith. Add one line stating the verdict stands on the certified subset — that line is
the package's strongest sentence and it is currently missing.

---

## R2 — T-X6 load-bearing enumeration · **AGREE-IF**

### Complete against the board — checked by generation, not by eye

Red's prior structural note (2026-08-04, `RED CLI CONCUR`) was that hand-sweeping is the method
failure and a **generated** cross-check is the cure. R2 was run that way.

Every `red: none` row in `improve_loop_20260804/BOARD_STATUS.md` is covered by blue's list:

| BOARD_STATUS row | T-X6 |
|---|---|
| arxiv_owner_prep · `none` (owner Fairbank) | TX6-01 ✔ |
| STRONG_CP_SEAT_HUNT · `none` (itch-only) | TX6-02 ✔ |
| theory_construction_20260804 · `none` (RED TASK filed) | TX6-03 ✔ |
| `_SUBSTITUTIONS.md` · `none` | TX6-04 ✔ |
| gate_fire_watch_20260804 · `none` | TX6-05 ✔ |
| fairbank_arxiv_trigger_20260804 · `none` | TX6-06 ✔ |
| A_omegaJ_rule1 · `none` (Claude optional) | TX6-07 ✔ |
| package_claim_protocol_20260804 · `none` | TX6-09 ✔ |
| residual block (5 rows, red=none) | 4 excluded as non-load-bearing + next_queue as TX6-13 ✔ |

**8/8 board rows + the 5-row residual block. No board row is missing.** The exclusions are correct
under the T-X6 test as written. TX6-08/10/11/12 are packages newer than the board — legitimate additions,
not padding.

### The defect — the board is not a census, and a board-scoped list inherits the board's blind spot

- package directories under `docs/working_logs/_runs/`: **288**
- named anywhere in BOARD_STATUS: **16**

After excluding machine poll dirs (`bbnfix_booking_*`, `machine_r1_currency_*`, `t14_*`, `getdist_force_*`)
and matching on date-stripped stems, **17 current-wave packages sit outside both the board and the T-X6 list**.
Most are currency/hygiene `EDITS.md` passes and correctly out of scope. **Two are load-bearing under
T-X6's own test:**

| package | why it is load-bearing |
|---|---|
| **`booking_pipeline_red_gate_20260804`** | Changes the **booking write path**: `--write-tables` now requires `bbnfix_booking_*/RED_AUDIT.md` carrying `red: AGREE`/`AGREE-IF`. This is precisely "changes booking". The *mechanism* is described at `BOARD_STATUS.md:80-82`, but the **package is not in the index and carries no red column at all** — so it is invisible to a board-scoped enumeration. |
| **`open_board_split_20260803`** | Holds `B_A_COEVOLVE_V13_BEST.md` — the champion **v13 Page lineage** that TX6-03/TX6-11 both point at — plus `BBN_EPS_REVERIFY_20260804.md` recording *"ε 2σ ceiling 3.196% ≈ paper claim 3.20% → **PASS**"*. 26 files carry claim tokens. It is upstream authority for two graded surfaces and is unlisted. |

**This is not blue disobeying.** The T-X6 card orders *"Do not invent audit list without board"*, so
scoping to the board was instructed. The finding is about the **ceiling of the method**: a board-scoped
enumeration cannot detect a load-bearing surface that never reached the board, and it cannot detect
its own blind spot from inside.

### Cure to lift to AGREE

Either (a) index the two packages and add them as TX6-14/TX6-15, or (b) state the scope explicitly in
the file — *"enumeration is over BOARD_STATUS-indexed packages only; surfaces never entered on the board
are out of scope and undetected by this list"* — so the blind spot is declared rather than implied.
(b) alone is sufficient for AGREE; (a) is better.

---

## Red's own method limits — disclosed

1. **The 400-phase sweep is a scan bound, not a maximum.** Red's 0.133022 is `≥`, for the same reason blue's 0.125313 was not a worst.
2. **The first completeness sweep produced a false-positive class and was corrected before filing.** Matching package directory names against BOARD_STATUS flagged ~12 packages as "absent" that are on the board written *without* their date suffix (`all4lanes`, `page_full_freeze`, `current_core_full`, …). Re-run with date-stripped stems. Had it been filed raw it would have been a false accusation of a 12-package gap.
3. **Three citations are unresolvable in this environment.** No network. Recorded as unverified, not as wrong.
4. **Nothing here was read from a log.** Every number came from the artifact: `coevolve_v13.json`, `PRTOE_baryogenesis.md`, `_DOCKET_INDEX.md`, `wilson/MASTER.md`, `BOARD_STATUS.md`, and a generated directory listing.

---

## What did not move

T8 still **FAIL** · `page_curve_claimed` still **false** · CANDIDATE **not** filed · F1 fence **ON** ·
Wilson slot 3 still **MISSING** · baryo row 9 still **OPEN** · void Door A still **OPEN-BLOCKED**, FAIL not fired ·
bbnfix gate still **REFUSED** · **COMPLETE physics 0**.

*NO FABRICATIONS. Verification ≠ grade lift. exit 0 ≠ PASS. A scan max is not a maximum.*
