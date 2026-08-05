# FILL_ATTEMPT — `winding_background_n`

**Package:** `theory_construction_wave_20260805/wilson/`  
**Track:** T-W5 Wilson  
**Date:** 2026-08-05  
**Requirement:** winding background \((n,\text{orientation})\) fixed relative to the family triangle  
**Fence:** NO FABRICATIONS · bound ≠ determination · Widnall ≠ family-gauge \(n\)  

---

## 1. Corpus hunt (file:line)

| Probe | Result | file:line |
|---|---|---|
| Canonical \(n\) | **bound** \(n\gtrsim 1.65\), not a determination | `docs/working_logs/_CANONICAL_VALUES.md:49` |
| \(L_\mathrm{gen}\) | **never assigned** | `_CANONICAL_VALUES.md:49`; `docs/PRTOE_baryogenesis.md:59–63` |
| Floor evaluation | \(n\gtrsim 1.65\) at \(L\geq 27.6\,\mathrm{Gpc}\), \(\xi_K=256\,\mathrm{Mpc}\) | `PRTOE_baryogenesis.md:64–67` |
| Preferred band \(n\sim 10\)–\(30\) | unpinned bookkeeping, not fixed \(n\) | `PRTOE_baryogenesis.md:242` (claims ledger row 9); `_CANONICAL_VALUES.md:49` |
| Widnall \(n\sim 11\)–\(25\) | **different object** (genesis vortex azimuthal / CMB comb), not dark-gauge \(A\) on family triangle | `docs/PRTOE_DEPENDENCY_TREE.md:74`; inventory.py:114–117 |
| Inventory status | **MISSING** | `scripts/koide_wilson_holonomy_inventory.py:110–118` |
| Prior T7 | **MISSING** | `desk_t7/WILSON_HUNT.md:66–77` |

---

## 2. Status

| Label | Value |
|---|---|
| **Status** | **MISSING** |
| Fills zero-knob? | **No** |
| Free dial used? | **No** |

**No PRESENT fixed \((n,\text{orientation})\) for family-cycle holonomy.**

---

## 3. Licensed fill path (without free dial)

| Licensed fill | Still forbidden |
|---|---|
| Completed genesis determination of \(L_\mathrm{gen}\) → fixed \((n,\text{orientation})\) on the family triangle | Pick \(n\in[11,25]\) Widnall band to hit \(2/9\) |
| Proof that holonomy is **\(n\)-independent** under the forced-combination hybrid (licensed connection must exist first) | Treat \(n\gtrsim 1.65\) bound as if it were a determination |
| External lattice / simulation archive that **outputs** background winding on the family path without fitting \(\theta_B\) | Smuggle CMB-comb Widnall modes as dark-gauge winding |

---

## 4. What would count as filled

- Fixed integer (or continuous) winding + orientation **determined**, not bounded; **or**  
- Written, audited proof of \(n\)-independence under a licensed hybrid connection.

**Today:** **MISSING**.

---

## 5. Fill attempt verdict

> **Fill refused.** Only a lower bound and a wrong-object Widnall band exist. Status remains **MISSING**.

*End FILL_ATTEMPT_winding_background_n.md*
