# Four-doors pre-audit — independent verification by the interactive red seat

**Seat:** Claude CLI (interactive). **Date:** 2026-08-04.
**Status of the other five files in this directory:** produced by a blue-spawned Claude subagent, not by this seat. This file records what the interactive seat verified **by its own hand**, so that any grade traceable to red rests on checks red actually ran.

**Authority:** owner instruction, direct, 2026-08-04 — package write restored.

---

## Verification status per finding

| # | finding | status | basis |
|---|---|---|---|
| **F1** | Page T8's denominator S⋆ is unfenced | **CONFIRMED** | recomputed from artifact + tool source |
| **F2** | N3 headline is a max-over-scan on a densified grid | **substance CONFIRMED · citations WRONG** | read by content after line numbers failed to resolve |
| **F3** | Israel asserts cannot fail | **CONFIRMED verbatim** | read directly from the script |
| **F4** | N6's stocked kill is a sign condition | **condition CONFIRMED · data UNVERIFIED** | kill text read; the cited Θ value not found on disk |
| — | Θ_lock = 1/√α | **CONFIRMED as an exact identity** | independent computation |

---

## F1 — CONFIRMED, and it is a structural hole

`scripts/page_protocol_scorecard.py:339` — `S_star = float(np.max(S))`. **S⋆ is the global maximum of S over the whole trajectory.** T8 then tests a *local* quantity against it: *"S range within bin ≤ 0.1 · S_star; report worst bin"* (the tool's own `T8_definition`).

The gate therefore normalises a **local** range by a **global** scale.

| quantity | value (from `coevolve_v13_scorecard_recompute.json`) |
|---|---|
| failing bin `[0.10, 0.11)`, `S_range` | 0.0018883423986319587 |
| `S_star` | 0.016688199517780646 |
| `S_range_over_S_star` | 0.11315435176934464 — fails ≤ 0.10 |
| S⋆ required for a pass | 0.018883423986319585 |
| **required S⋆ factor** | **1.1315435176934463 → +13.15%** |

**Correction to the subagent block:** it states 13.16%. The exact figure is **+13.15%**. Immaterial to the finding.

The failing window and the global peak are different regions of the trajectory, so **raising the peak by 13.15% clears T8 with the failing bin untouched**. The numerator does not move; the test passes because the denominator did.

Gate-silent because every other test rewards it: a larger midband peak helps T3, preserves T1, does not touch T2's reach. The existing fence covers only levers that move numerator and denominator together ("ratio sticky").

**Red's demand, adopted on red's own verification:** any artifact claiming `T8_pass` must report the absolute early-bin range **and** S⋆ separately, each against v13. A pass carried only by the denominator is a fake pass. Moving both together is legitimate — the requirement is to **show which moved**.

---

## F2 — substance CONFIRMED, citations WRONG

**The citations in the subagent block do not resolve.** It cites `script:1079` for the `production_3d` hardcode and `script:1203` for its assert. Line 1079 is the comment `# ---- VERDICT ----`; line 1203 is a dict key. A reader checking the citation finds neither claim.

**Read by content, the charge is true:**

- `bounce_n3_gpe_late_theta.py:1117` — `production_3d = False  # none of these instruments are full 3D production`
- `:1241` — `assert summary["production_3d"] is False`

So the script states plainly that none of its instruments are 3D production, and asserts it. Calling the deepened 0D/1D/spherical/2D scan "production 3D" would be grade inflation, and the script itself forbids it.

**Grid densification confirmed verbatim.** `:235` — `# axis C: high-compression corner densification (prior best late region)`. Axis extents A+B+C alone give **99 + 72 + 480 = 651 rows** against a prior grid of 83. A maximum over a scan is an extreme-value statistic that rises with row count alone, and axis C densifies precisely where the prior maximum sat.

**Red's demand:** argmax coordinates with every headline number, plus the fixed stocked point (6, −2, 1.5, 0.15) whose value is scan-size independent.

---

## F3 — CONFIRMED verbatim

`bounce_israel_junction_inventory.py` assigns six literals and then asserts those same literals:

```
ISRAEL_S_AB_STOCKED = False      →  assert ISRAEL_S_AB_STOCKED is False
ISRAEL_K_AB_STOCKED = False      →  assert ISRAEL_K_AB_STOCKED is False
N4_FORCE_BRANCH_DERIVED = False  →  assert N4_FORCE_BRANCH_DERIVED is False
can_derive_H_re = False          →  assert can_derive_H_re is False
bounce_closed = False            →  assert bounce_closed is False
lands = 0                        →  assert lands == 0
"israel_S_ab_equations": 0       →  assert counts["israel_S_ab_equations"] == 0
```

**These cannot fail.** `exit 0` from this script carries no information about Israel physics — it confirms only that Python can compare a literal to itself. The honest content is an inventory of absence, which is a legitimate thing to file, but the door is named *content*.

`assert 0.8 < ratio_vs_1cs < 1.0` is present at `:210`. A hardcoded band on a ratio is a latent dial: if an anchor moves, the script crashes, and the cheapest repair is to move the anchor back.

---

## F4 — condition CONFIRMED, data UNVERIFIED

`fa3_metric_off/KILL_AND_FALSIFIERS.md:23` reads, verbatim:

> Medium stress **cannot** produce ⟨Θ⟩>0 under any legal GPE / averaging / 3D instrument (beyond toys) | Gate ⟨Θ⟩>0 never fires | Declaration has no medium input; RP-A exterior turn dies

**The logic is confirmed:** the kill fires only if stress *cannot* produce ⟨Θ⟩ > 0. A positive late ⟨Θ⟩ therefore blocks the kill, and a *magnitude* shortfall (obstruction C) is a different object.

**What red could not verify:** the block cites `turn_paid_toy: true` and `max late ⟨Θ⟩ = +1.8005`. Red grepped the N3 package and found neither. **Red does not certify that number.** If it exists, F4 follows; if it does not, F4's conclusion is unsupported and the finding reduces to the (still correct) reading of the kill condition.

**Red also endorses the "beyond toys" point on its own reading:** the stocked condition quantifies over instruments that are not stocked. A universal over non-existent instruments can be left open; it cannot be *established*.

---

## Θ_lock = 1/√α — CONFIRMED as an exact identity

At d = 3, with c_s = √(3α):

```
Θ_lock = d / (c_s √3) = 3 / (√(3α) · √3) = √3 / √(3α) = 1/√α
```

Independent computation: **11.706237614366112**. The subagent block gives 11.706237610778283 — a different α input, agreeing to nine significant figures.

**The d and the √3 cancel exactly.** The N3 door's target therefore carries **zero medium content**: it is α^(−1/2) and nothing else. Consistent with the N1 F-A2 verdict already on the board.

---

## Scope of this file

Red verified five claims. Red did **not** re-derive the other five files in this directory, did not run the N3 script, did not touch any living `docs/PRTOE_*.md`, and quoted no machine numbers. Chains untouched. `exit 0 ≠ PASS`. Verification ≠ grade: the doors are graded when they land.

*NO FABRICATIONS.*
