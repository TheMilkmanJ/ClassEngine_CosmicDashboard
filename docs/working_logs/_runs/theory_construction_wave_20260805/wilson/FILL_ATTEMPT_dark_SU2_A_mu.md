# FILL_ATTEMPT — `dark_SU2_A_mu`

**Package:** `theory_construction_wave_20260805/wilson/`  
**Track:** T-W5 Wilson  
**Date:** 2026-08-05  
**Requirement:** dark SU(2) gauge field / connection \(A_\mu\) on the family scale  
**Fence:** NO FABRICATIONS · do not invent \(A_\mu\) · do not treat T14 \(\psi\) as gauge field  

---

## 1. Corpus hunt (file:line)

| Probe | Result | file:line / path |
|---|---|---|
| Named archives (inventory candidates) | **all ABSENT** | `data/dark_su2_gauge_config.npy`, `data/wilson_Amu.npy`, `data/family_triangle_connection.json`, `output/dark_su2_gauge.dat` |
| `data/` directory | exists; **no** SU(2) A archive | `data/` (empty of gauge configs) |
| Inventory gate | status **MISSING** | `scripts/koide_wilson_holonomy_inventory.py:70–94` |
| T14 `psi_n*.npy` | exist as condensate wavefunctions for \(H_\mathrm{kin}\); **not** dark SU(2) \(A_\mu\) | inventory refuse note `inventory.py:78–80`; many under `docs/working_logs/_runs/t14_*` |
| CLASS gauge tests | metric synchronous/Newtonian gauges, **not** Wilson lines | `test_gauge_invariance.py:1–12` |
| Prior T7 hunt | **MISSING** reconfirm | `desk_t7_koide_wilson_20260804/WILSON_HUNT.md:37–48` |
| Prior residual stamp | **MISSING** | `koide_residual/WILSON_MISSING_INPUTS.md:60` |
| Wave re-run filesystem | named candidates still ABSENT | this package `logs/` + live `ls` 2026-08-05 |

**This wave re-run log:** [`logs/koide_wilson_holonomy_inventory.log`](logs/koide_wilson_holonomy_inventory.log) — exit **2**.

---

## 2. Status

| Label | Value |
|---|---|
| **Status** | **MISSING** |
| Fills zero-knob? | **No** |
| Free dial used? | **No** (refused) |

**Algebra of adjoints / \(\varepsilon^{abc}\)** is **not** a gauge-field archive.

---

## 3. Licensed fill path (without free dial)

Any of the following would count as **PRESENT** only if it is actually \(A_\mu\) (or an equivalent connection) at family-relevant scale, with **fixed** parameters not dialed to \(\theta_B\) / lepton masses:

1. **External SU(2) \(N_f=3\) lattice** gauge configurations at the family-relevant scale, archived under a named path the inventory can see.  
2. **Derived dual-superconductor / hybrid orientational connection** with **fixed** \(F_\mathrm{dark}/\sqrt{\sigma}\), \(w\cdot\sqrt{\sigma}\) (not a band used as dial) — same campaign as \(\alpha_d\) / electric projection.  
3. Archival genesis field **if and only if** it is dark-SU(2) \(A\), **not** T14 condensate \(\psi\).

### Still forbidden

| Temptation | Why killed |
|---|---|
| Hand-written / toy constant \(A_\mu\) so inventory exits 0 | Fabrication |
| Treat T14 \(\psi_n^*.npy\) as \(A_\mu\) | Wrong object (condensate for \(H_\mathrm{kin}\)) |
| Fit \(A_\mu\) to \(\theta_B\) / lepton masses / arg \(b\) | Circular elastic hit |
| Invent holonomy number without field | Charge-A style back-solve; NO FABRICATIONS |

---

## 4. What would count as filled (this wave)

- On-disk corpus-fixed connection usable without free dial, **and**  
- Inventory re-run reports `dark_SU2_A_mu` **PRESENT**.

**Today:** still **MISSING**. No invent.

---

## 5. Fill attempt verdict

> **Fill refused.** Corpus has no dark-SU(2) \(A_\mu\) archive. Status remains **MISSING**.

*End FILL_ATTEMPT_dark_SU2_A_mu.md*
