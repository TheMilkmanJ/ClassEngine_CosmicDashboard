# Page T8 — binning-phase qualifier (offset-0 “sole fail”)

**Package:** `docs/working_logs/_runs/theory_residual_blue_20260805/`  
**Date:** 2026-08-05  
**Agent:** Grok blue  
**Nature:** claim-precision qualifier — **does not** lift T8 to pass  
**Order:** Claude further-work B8 / C7 (`theory_construction_wave_20260805/red/FURTHER_WORK_DISCUSS.md`)

---

## Authoritative T8 (champion v13)

| field | value |
|---|---|
| Champion | `coevolve_v13` · artifact `docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/coevolve_v13.json` |
| input_sha256 | `048de43e1bc766c8f420c54f565a33166c0792c23291ba567cdc6c772f92fca8` |
| Protocol | default / **offset-0** bins, \(\Delta u = 0.01\) |
| Worst bin (offset-0) | **[0.10, 0.11)** · n=12 |
| range / \(S_\star\) | **0.11315435176934464** (need ≤ **0.10**) |
| **T8_pass** | **False** |
| **CANDIDATE_TURN_binding** | **False** |
| **page_curve_claimed** | **false** |
| Scorecard stamp | [`../theory_construction_wave_20260805/page/SCORECARD_STAMP.md`](../theory_construction_wave_20260805/page/SCORECARD_STAMP.md) |
| Page package MASTER | [`../theory_construction_wave_20260805/page/MASTER.md`](../theory_construction_wave_20260805/page/MASTER.md) |

---

## Qualifier (required language)

The champion v13 **T8 FAIL 0.113154…** on bin **[0.10, 0.11)** is for the **default / offset-0 binning phase** of the registered scorecard protocol.

Claude re-verified alternate binning phases (construction-wave red · CLI; see `theory_construction_wave_20260805/logs/claude_red_further_work_no_hygiene.log` and `red/MASTER_RED.md` §5 / further-work note):

| observation | detail |
|---|---|
| Offset-0 neighbours | bins **[0.11, 0.12)** ≈ 0.092909 and **[0.12, 0.13)** ≈ 0.096240 sit **under** the 0.10 bar |
| Contiguous early region | residual lives in early \(u\in[0.10,0.13)\) class, not a single anomalous isolated bin |
| Alternate phases | neighbours can pass the 0.10 bar while **other phases fail 2–3 bins** |
| Alternate-phase ratios | **≥ 0.1330** over a 400-phase scan (red CLI 2026-08-05); **0.1253** is the value near phase ≈0.60, **not** the family maximum (**94/400** phases exceed 0.1253). Scan bound, not a proven global max. |
| Offset-0 “sole fail” | **true only for offset-0** — most favourable reading of binning phase, not a cheat (protocol definition) |

---

## What this does **not** do

| statement | status |
|---|---|
| “Sole fail” without phase tag | **Must be qualified** as **offset-0 binning** |
| Lift T8 to pass | **Does NOT** — claim stays **false** |
| Soften 0.10 bar | **No** |
| File CANDIDATE | **No** — still requires T8 ≤ 0.10 + F1 disclosure + red AGREE |
| F1 fence | **Still ON** ([`../theory_construction_wave_20260805/page/F1_BIND.md`](../theory_construction_wave_20260805/page/F1_BIND.md)) |
| Grade movement | **None** — T8 remains FAIL; Q6 remains OPEN |

---

## Preferred citation forms

**Allowed:**

- “T8 FAIL range/\(S_\star\)=0.113 on bin [0.10,0.11) under **default (offset-0) binning**; alternate phases can fail 2–3 bins (scan ratios **≥ 0.1330** over 400 phases; 0.1253 is not the family max).”
- “Joint near-miss on offset-0 protocol; not a multi-phase pass.”

**Forbidden:**

- “Only one bin fails” / “sole fail” **without** offset-0 qualification when used as public/near-miss strength language.
- Any implication that phase shopping yields a T8 pass.

---

## Cross-links

| surface | path |
|---|---|
| Construction-wave page package | `docs/working_logs/_runs/theory_construction_wave_20260805/page/` |
| SCORECARD_STAMP | `.../page/SCORECARD_STAMP.md` |
| F1_BIND | `.../page/F1_BIND.md` |
| Red MASTER (bin-phase flag + later CLI verify) | `.../red/MASTER_RED.md` · `.../logs/claude_red_further_work_no_hygiene.log` |
| Page freeze (prior) | `docs/working_logs/_runs/page_full_freeze_20260804/` |
| INDEX Page row | `docs/PRTOE_INDEX.md` (live status stamp) |

*NO FABRICATIONS. Qualifier only. T8 still FAIL. claim false. F1 ON.*
