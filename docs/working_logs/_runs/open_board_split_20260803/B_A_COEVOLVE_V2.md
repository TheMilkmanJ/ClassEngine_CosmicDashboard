# B-A REPORT — Page co-evolution v2 → stall_cap

**Task:** Improve Page coevolve toward coevolution stall_cap (Claude: longest consecutive stall frames ≤10).  
**Date:** 2026-08-03  
**Resource:** `OMP_NUM_THREADS=1`, `nice -n 10`. No PolyChord. No MCMC.

---

## Gate table (from disk scorecard only)

| gate | value |
|---|---|
| **T8_pass** | **True** |
| **stall_cap_ok** | **True** |
| longest_stall_frames | **5** (cap=10) |
| frac_S_rise_while_u_advances | ~1.000 |
| co_frac_ok (≥0.70) | True |
| swap_ok (≤0.05) | True (swap_back=0) |
| peak_in_motion | True |
| T1 interior max | True (u*=0.4024) |
| T2_all (reach + drop + noise) | True (u_late=0.9984) |
| T3 early rise (du-gated) | True |
| T4 nulls N1–N4 | True |
| T5 / T6 | True / True |
| T7 claim flag | **false** |
| CANDIDATE_TURN (T1–T6 + coevolution gates) | True |
| **CANDIDATE_TURN_binding** (T1–T8 + DC3) | **False** |
| DC3 weight_invariant_reach | **FAIL** (v_frozen_env_late=0.8531 < 0.9) |
| **page_curve_claimed** | **false** |
| **CANDIDATE packet filed** | **no** |

---

## Version path / SHA

| role | path | sha256 (full or prefix) |
|---|---|---|
| Run artifact (write-once v2) | `/home/themilkmanj/prtoe_class/docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/coevolve_v2.json` | `28317d4f0a42f6a04ae175f9a917f4901964d581139300fb858cfd776faf6346` |
| Scorecard recompute | `/home/themilkmanj/prtoe_class/docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/coevolve_v2_scorecard_recompute.json` | tool `1d02a1d4bdd11a88612f6db387a3a819425c3be362bc74a57122162cb90a14b7` |
| Script at run | `/home/themilkmanj/prtoe_class/scripts/quantum_page_coevolve.py` | `05b2baaf349247eb745ee716165f1b624170372c6a31b383fc163c39376eb6c5` |
| Prior v1 (not overwritten) | `.../page_curve/coevolve_v1.json` | intact; schedule `v12_T8_coevolve` |

---

## What changed (frozen header only; no v-blend)

**Problem (v1 / v12):** T8_pass True, frac_S_rise~0.996, but **longest_stall_frames=34** → stall_cap_ok False → no binding candidate path under R-C stall rule.

Stall anatomy on v1 (arrays):
1. **Early L=34** (f≈0.010–0.067): max-envelope `u` sat on a tiny-energy transient `v` spike while pure energy ratio slowly recovered.
2. **Late L=19** (f≈0.318–0.350): hard `IDLE_AFTER_F=0.32` froze gamma before `W_C_HOLD=0.35` free-frequency decay restarted continuous pure-energy `u` advance.

**Schedule `v13_stall_cap_coevolve`** pins (header of `scripts/quantum_page_coevolve.py`):

| pin | v12 | v13 | intent |
|---|---:|---:|---|
| `W_C_HOLD` | 0.35 | **0.28** | Core free-frequency weight decays *before* IDLE so pure-energy `u` keeps advancing through the idle window (late plateau removed). Not a schedule blend into `v`. |
| `BS_MILD` | 0.23 | **0.40** | Stronger concurrent early beam-splitter dump so envelope `u` does not sit on early transient spike for >10 frames. |
| `IDLE_AFTER_F` | 0.32 | 0.32 | Unchanged T8 multivalued-tail cut. |
| `G_TMS` / `G_BS` / `TMS_SHAPE_POWER` | 0.37 / 3.8 / 4.0 | same | Keep v12 T8 stack. |

- `v = E_rad/(E_rad+E_core)` only — **no v-blend**.
- Write-once `coevolve_v2.json` — **v1 not overwritten**.

---

## Key numbers (v2 scorecard)

| quantity | value |
|---|---:|
| u* (S peak) | 0.40244242362512417 |
| u_late (dynamic envelope) | 0.9984041763033604 |
| S_peak / S* | 0.0033735369798868152 |
| S_late | 0.0006336682524608895 |
| drop | 0.002739868727425926 |
| longest_stall_frames | 5 |
| T8 worst bin | [0.16, 0.17) range/S*=0.05127 |
| T8 failing bins | 0 |
| v_frozen_envelope_late (DC3) | 0.8530553129820173 |

---

## Explicit non-claim

- **Not a Page curve claim.** Q6 remains OPEN.
- `page_curve_claimed` remains **false** everywhere.
- **No CANDIDATE packet was filed** (claim-decoupling).
- Machine `CANDIDATE_TURN` (T1–T6 + coevolution gates) is True, but **`CANDIDATE_TURN_binding` is False** because DC3 weight-invariant reach **FAIL**: with core frequency weight frozen at `w_c0=1`, envelope `v` only reaches **0.853 < 0.9**. Dynamic late reach is weight-assisted via free-frequency `w_c(f)` (STRUCTURAL_PURE_ENERGY_FRACTION / DC2 hygiene is not a DC3 pass).
- Protocol still requires claim-decoupling checklist + red AGREE before any claim path.
- Continuum ingredient remains week2 ω/Γ + same-run field evidence class — not full QFT on curved acoustic spacetime.
- No coefficient \(A/4G\) payment; no \(4v(1-v)\) ansatz as physics; no thermal-only \(dE/T\) as Page.

---

## Paths

| role | path |
|---|---|
| Script | `/home/themilkmanj/prtoe_class/scripts/quantum_page_coevolve.py` |
| Scorecard tool | `/home/themilkmanj/prtoe_class/scripts/page_protocol_scorecard.py` |
| Run JSON v2 | `/home/themilkmanj/prtoe_class/docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/coevolve_v2.json` |
| Scorecard JSON v2 | `/home/themilkmanj/prtoe_class/docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/coevolve_v2_scorecard_recompute.json` |
| This report | `/home/themilkmanj/prtoe_class/docs/working_logs/_runs/open_board_split_20260803/B_A_COEVOLVE_V2.md` |

*NO FABRICATIONS. Numbers from on-disk JSON only.*
