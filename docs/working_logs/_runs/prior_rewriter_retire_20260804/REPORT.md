# Prior-rewriter monitor — RETIRED + code fence (2026-08-04)

**Finding:** Claude red `RED CLOSE A2-REVERSAL cure + NEW FINDING (live prior-rewriter)`  
**Stamp:** 2026-08-04 after red verification of A2-REVERSAL currency cure

---

## What was live

| field | value |
|---|---|
| PID | **1380706** |
| command | `plot_chains.py --config …/dyad_mnu_bbnfix.input.yaml --monitor-and-stop --interval 150` |
| runtime at discovery | ~1 h 10 m |
| target | production model chain **dyad_mnu_bbnfix** |

**Behavior if armed:** on posterior edge within 5% of prior span → `update_yaml_priors` rewrites `prior.min/max` **and** `proposal=(max−min)/20`, then dashboard restart handoff. That splices configuration under a live booking-gate chain (zon-class failure mode).

**Why inert when found (accidental only):**
1. Config path `/home/themilkmanj/prtoe_class/dyad_mnu_bbnfix.input.yaml` **does not exist** (live input is `chains/dyad_mnu_bbnfix.input.yaml`)
2. CosmicDashboard `localhost:8000` not listening → restart leg fails

**Do not “fix” the path** without removing rewrite capability.

---

## Actions taken (Grok)

| # | action | status |
|---|---|---|
| 1 | `kill` PID **1380706** (monitor only — **not** cobaya) | **DONE** — process gone |
| 2 | Verify dyad/lcdm cobaya still alive | **YES** (MPI ranks still running) |
| 3 | Confirm no other `plot_chains --monitor-and-stop` | **none** after kill |
| 4 | Harden `plot_chains.py` | **DONE** — production deny list; `--allow-prior-rewrite` opt-in; dashboard default False |
| 5 | Did **not** edit `chains/dyad_mnu_bbnfix.input.yaml` | **YES** |

### Code fence (`plot_chains.py`)

- `PRODUCTION_PRIOR_REWRITE_DENY`: dyad/lcdm bbnfix, routeD, any `bbnfix` basename
- `update_yaml_priors` **REFUSES** production configs always
- Non-production rewrite requires **`--allow-prior-rewrite`** + dashboard opt-in (default **False**)
- `--monitor-and-stop` help text: report-only for production

---

## Relation to A2

**Not** the A2 false gate. Fires on prior-edge crowding, not R−1. A2 retirement (PID 212363 / `A2_FALSE_GATE_RETIRED.md`) stands.

---

## Machine (unchanged)

lcdm **0.086466** (N=20409) · dyad **0.128943** (N=20302) · book **REFUSED** · no peek H₀

*NO FABRICATIONS. Leave MCMCs alone. Protect booking-gate inputs.*

---

## AGREE-IF cure — routeD case bug (2026-08-04)

Claude: `PRODUCTION_PRIOR_REWRITE_DENY` had `"cmp_prtoe_routeD"` (capital D) tested against
`base.lower()`, so routeD never matched. dyad/lcdm were only safe via accidental `"bbnfix"`.

**Cure:** compare with `tok.lower() in low`; token stored as `cmp_prtoe_routed`.

**Verify (executed):**
```
PROTECTED              chains/dyad_mnu_bbnfix.input.yaml
PROTECTED              chains/cmp_lcdm_mnu_bbnfix.input.yaml
PROTECTED              chains/cmp_prtoe_routeD.input.yaml
PROTECTED              cmp_prtoe_routeD.yaml
```
`update_yaml_priors(..., allow_rewrite=True)` on routeD → **False / REFUSED**. YAML mtimes unchanged.
