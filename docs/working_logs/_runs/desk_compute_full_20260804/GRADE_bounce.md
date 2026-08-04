# GRADE — bounce pack (desk_compute_full_20260804)

**Stamp graded:** 2026-08-04  
**Source:** [`bounce/SUMMARY.md`](bounce/SUMMARY.md) · logs under `bounce/logs/`  
**Pack:** `desk_compute_all_safe.py --pack bounce --timeout 300`  
**Fences:** NO FABRICATIONS · do **not** invent \(H_\mathrm{re}\) · no cyclic booking · exit 0 ≠ PASS · MCMCs untouched · no PolyChord.  
**Align:** [`../bounce_full_freeze_20260804/REPORT.md`](../bounce_full_freeze_20260804/REPORT.md)

---

## 0. Run counts

| metric | count |
|---|---:|
| **Jobs** | **28** |
| exit 0 | **24** |
| nonzero | **0** |
| timeout (−9) | **4** |
| **COMPLETE / \(H_\mathrm{re}\) derived** | **0** |
| cyclic cosmology booked | **0** |

**Timeouts (incomplete instrument, not physics FAIL of paid nogos):**  
`bounce_m6_rebound_1d_hypersonic`, `bounce_m6_rebound_dst`, `bounce_m6_rebound_gp`, `bounce_transverse_2d`.

---

## 1. Done-log table (all 28)

| # | label | exit | instrument | physics grade (this recompute) |
|---:|---|---:|---|---|
| 1 | `bounce_averaging_decomposition` | 0 | ok | **desk audit** — averaging identity holds; not exterior turn |
| 2 | `bounce_bkl_stiff_check` | 0 | ok | **PAID nogo reconfirmed** — rotation alone cannot stiffen to BKL-safe \(w\ge1\) |
| 3 | `bounce_electron_contact` | 0 | ok | contact/presence **PASS-shaped**; **turn FAIL by class** (NEC lane) |
| 4 | `bounce_fa1_transphononic_table` | 0 | ok | **desk table** — not H_re |
| 5 | `bounce_fa3_hcross_attempt` | 0 | ok | **OPEN-BLOCKED reconfirmed** — `can_derive_H_re_without_declaration: false`; O2 PARTIAL; no cyclic |
| 6 | `bounce_floor_frw_nogo` | 0 | ok | **PAID nogo A/B/C** — CSW floor ≠ FRW bounce |
| 7 | `bounce_handover_sign` | 0 | ok | **PAID nogo** — vac+rad turnaround ≠ bounce |
| 8 | `bounce_m1_shear_xi` | 0 | ok | **desk** — F-A4 scale-clock structure; not turn close |
| 9 | `bounce_m2_junction` | 0 | ok | **desk** — junction scaffolding |
| 10 | `bounce_m2b_mixmaster_nmed` | 0 | ok | **OPEN** — \(N_\mathrm{med}\approx6\) near-coincidence, not trigger |
| 11 | `bounce_m4_arrow_boundary` | 0 | ok | **desk** — O8 structure-shaped; not engine |
| 12 | `bounce_m5_exotic_fluid` | 0 | ok | **PAID negative** — M5 closes negative (all windows FAIL) |
| 13 | `bounce_m6_rebound_1d` | 0 | ok | **medium-layer toy** — density turn real in 1D GPE; O2/O6 cosmological matching still OPEN |
| 14 | `bounce_m6_rebound_1d_hypersonic` | −9 | **timeout** | **incomplete** |
| 15 | `bounce_m6_rebound_dst` | −9 | **timeout** | **incomplete** |
| 16 | `bounce_m6_rebound_gp` | −9 | **timeout** | **incomplete** |
| 17 | `bounce_m8_ledger_quartic` | 0 | ok | **PAID nogo** — homogeneous quartic ledger dead |
| 18 | `bounce_magnetic_flip_nogo` | 0 | ok | **PAID nogo** — polarity flip not turn |
| 19 | `bounce_o7_mixmaster_squeeze` | 0 | ok | **PARTIAL / OPEN** — window priced; not GR survival theorem |
| 20 | `bounce_rpA_scaffold` | 0 | ok | **RECONSTRUCTED CANDIDATE only** — O2 PARTIAL · O6 FAIL legal · not OEM/DERIVED |
| 21 | `bounce_rp_required_X` | 0 | ok | **PAID nogo** — DE-scale / stocked X insufficient |
| 22 | `bounce_task20_sequencing_race` | 0 | ok | **desk sequencing** — not turn close |
| 23 | `bounce_task4_handoff_joints` | 0 | ok | **OPEN named joints** — handoff incomplete by design |
| 24 | `bounce_task5_assembled_timeline` | 0 | ok | **desk timeline** — missing negative-energy component still named |
| 25 | `bounce_task5_door_budget` | 0 | ok | **desk budget** — not MeV hot-start close |
| 26 | `bounce_thermal_crossing_nogo` | 0 | ok | **PAID nogo** — melt \(T=T_c\) ≠ geometry turn |
| 27 | `bounce_transverse_2d` | −9 | **timeout** | **incomplete** |
| 28 | `bounce_two_routes` | 0 | ok | **desk routes** — incomplete component named; not promotion |

---

## 2. What is RECONFIRMED

| item | grade |
|---|---|
| Homogeneous legal-parts FRW bounce engines | **DEAD / PAID nogo table** |
| FA3 exterior \(H_\mathrm{re}\) without branch declaration | **false** (OPEN-BLOCKED) |
| RP-A as derived OEM | **no** (scaffold only) |
| Cyclic cosmology | **not booked** |
| Medium-layer ⟨Θ⟩ / 1D rebound toys | **exist as toys**; do **not** pay exterior FRW turn |

---

## 3. NON-PROMOTION

1. **\(H_\mathrm{re}\) derived / bounce COMPLETE** — forbidden; reconfirmed blocked.  
2. **Timeouts → physics FAIL of paid floor** — no; incomplete heavy sims only.  
3. **M6 1D rebound → cosmological O2/O6 close** — medium toy only.  
4. **RP-A → OEM / DERIVED** — reconstructed candidate language only.  
5. **exit 0 bulk “28 PASS”** — false; true split is nogo/desk/OPEN-BLOCKED + 4 timeouts.  
6. **Any MCMC / PolyChord / H₀ book** — none.

---

## 4. One-liner

Bounce pack **finished** (24/28 exit0 · 4 timeout): paid nogos and FA3 obstruction **reconfirmed**; **\(H_\mathrm{re}\) stays OPEN-BLOCKED**; **0 COMPLETE promotions**.

*NO FABRICATIONS. Grade complete for bounce pack.*
