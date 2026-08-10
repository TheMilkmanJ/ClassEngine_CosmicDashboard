# CURES — current_core_full_20260804

**NO FABRICATIONS.** Hygiene only; no PolyChord; no MCMC.

Retired knob: **`dcdf_beta`** (removed 2026-07-05 v5). CLASS hard-errors if the parameter is present. CURRENT_CORE pure fluid uses \(w=-\rho_\mathrm{inf}/\rho\), \(c_s^2\equiv 0\).

---

## Scratch YAML inventory (`scratch/*.yaml`)

| file | pre-cure | status | cure |
|---|---|---|---|
| `scratch/eval_triad.yaml` | live `params.dcdf_beta: 3.3e-5` | **CURED** (was SCRATCH-STALE) | commented out + retirement note |
| `scratch/eval_triad.input.yaml` | live `params.dcdf_beta: 3.3e-05` | **CURED** (was SCRATCH-STALE) | commented out + retirement note |
| `scratch/eval_triad.updated.yaml` | live `input_params: - dcdf_beta` and `params.dcdf_beta.value: 3.3e-05` | **CURED** (was SCRATCH-STALE) | both sites commented out + retirement note |

### Remaining `dcdf_beta` strings in triad YAMLs

**None active.** Only YAML comments remain (documentation of retirement). Safe for accidental `cobaya run` / evaluate: parsed params do **not** include `dcdf_beta`.

Verify (2026-08-04 post-cure):

```
scratch/eval_triad.yaml:         params.dcdf_beta=False  input_params=False
scratch/eval_triad.input.yaml:   params.dcdf_beta=False  input_params=False
scratch/eval_triad.updated.yaml: params.dcdf_beta=False  input_params=False
```

---

## Other scratch references (not SCRATCH-STALE)

These already document retirement / strip the knob; **not** live CLASS inputs:

| file | note |
|---|---|
| `scratch/eval_triad.py` | pops `dcdf_beta` if present in loaded yaml |
| `scratch/eval_triad_point.py` | comment: do not pass to CURRENT_CORE |
| `scratch/eval_triad_matched.py` | comment: retired |
| `scratch/test_dkappa.py` | comment: CLASS hard-errors if present |
| `scratch/test_speed.py` | comment: pure fluid defaults |

No further action required on those.

---

## Why this matters

Accidental evaluate of pre-cure triad YAMLs would hit:

```text
Error in Class: Class did not read input parameter(s): dcdf_beta
```

(or equivalent hard-error path). That is **not** a physics FAIL — it is a stale-API hygiene bug. Cure is comment/remove, not reintroduce the knob.

Related suite cure (already paid earlier same day):  
`docs/working_logs/_runs/open_board_split_20260803/VALIDATE_DCDF_V5_CURE_20260804.md`

---

## SCRATCH-STALE residual after this pass

| residual | label |
|---|---|
| Active `dcdf_beta` in `scratch/*.yaml` | **none** |
| Comment-only mentions | OK (not SCRATCH-STALE) |
| LEGACY_ST `use_prtoe` logs FAIL | expected / out of CURRENT_CORE scope |

*NO FABRICATIONS.*
