# Tier 1 emulator prep — chain inventory only (2026-08-03)

**NO TRAINING.** Preregister gates still owed (Claude R2 Tier 1).
**NO A4 interference.**

Chain dir size: see `du`. File count `.txt`: **41**

| file | bytes | lines (approx) |
|---|---:|---:|
| `cmp_lcdm.1.txt` | 1274 | 2 |
| `cmp_lcdm.txt` | 746 | 1 |
| `cmp_lcdm_ev.1.txt` | 1306 | 2 |
| `cmp_lcdm_mnu.txt` | 769 | 1 |
| `cmp_lcdm_mnu_bbnfix.1.txt` | 3777984 | 5622 |
| `cmp_lcdm_mnu_bbnfix.2.txt` | 3828384 | 5697 |
| `cmp_lcdm_mnu_bbnfix.3.txt` | 3739008 | 5564 |
| `cmp_lcdm_mnu_modes_comparison.txt` | 3325 | 72 |
| `cmp_lcdm_modes_comparison.txt` | 3271 | 71 |
| `cmp_prtoe_conv.minimum.txt` | 1408 | 2 |
| `cmp_prtoe_conv_desi.1.txt` | 3205008 | 4946 |
| `cmp_prtoe_dyad.txt` | 815 | 1 |
| `cmp_prtoe_dyad_modes_comparison.txt` | 3325 | 72 |
| `cmp_prtoe_lepton.minimum.txt` | 1376 | 2 |
| `cmp_prtoe_modes_comparison.txt` | 1314 | 39 |
| `cmp_prtoe_nulink.minimum.txt` | 1344 | 2 |
| `cmp_prtoe_omk.minimum.txt` | 1408 | 2 |
| `cmp_prtoe_pour_eval_diag.1.txt` | 1280 | 2 |
| `cmp_prtoe_pour_eval_h73.1.txt` | 1280 | 2 |
| `cmp_prtoe_pour_eval_noidr.1.txt` | 1280 | 2 |
| `cmp_prtoe_routeD.1.txt` | 9960 | 15 |
| `cmp_prtoe_routeD.2.txt` | 11288 | 17 |
| `cmp_prtoe_routeD.3.txt` | 10624 | 16 |
| `cmp_prtoe_twist.1.txt` | 59616 | 92 |
| `cmp_prtoe_w13.txt` | 861 | 1 |
| `cmp_prtoe_w13_modes_comparison.txt` | 3380 | 73 |
| `cmp_prtoe_zon.1.txt` | 822976 | 1169 |
| `cmp_prtoe_zon_disp.1.txt` | 3350336 | 4759 |
| `dashboard_credentials.txt` | 249 | 6 |
| `dcdf_joint_me101.txt` | 79200 | 100 |
| `dcdf_joint_me101_bbn.txt` | 47520 | 60 |
| `dcdf_joint_me101_bbn_modes_comparison.txt` | 3464 | 72 |
| `dcdf_joint_me101_modes_comparison.txt` | 3460 | 72 |
| `dyad_mnu_bbnfix.1.txt` | 4152896 | 5899 |
| `dyad_mnu_bbnfix.2.txt` | 4126144 | 5861 |
| `dyad_mnu_bbnfix.3.txt` | 4171904 | 5926 |
| `dyad_mnu_mcmc.1.txt` | 3425664 | 4866 |
| `dyad_mnu_v1.txt` | 2011200 | 2400 |
| `dyad_mnu_v1_modes_comparison.txt` | 3524 | 73 |
| `lcdm_joint_v1_modes_comparison.txt` | 2386 | 71 |
| `me_audit_modes_comparison.txt` | 1314 | 39 |

**Sum lines (all .txt):** 53691

## Input yamls present

- `chains/cmp_lcdm.input.yaml`
- `chains/cmp_lcdm_ev.input.yaml`
- `chains/cmp_lcdm_mnu_bbnfix.input.yaml`
- `chains/cmp_prtoe_conv.minimize.input.yaml`
- `chains/cmp_prtoe_conv_desi.input.yaml`
- `chains/cmp_prtoe_dyad_ev.input.yaml`
- `chains/cmp_prtoe_fixed_ev.input.yaml`
- `chains/cmp_prtoe_fixed_trgb_ev.input.yaml`
- `chains/cmp_prtoe_lepton.minimize.input.yaml`
- `chains/cmp_prtoe_nulink.minimize.input.yaml`
- `chains/cmp_prtoe_omk.minimize.input.yaml`
- `chains/cmp_prtoe_pour_ev.input.yaml`
- `chains/cmp_prtoe_pour_eval_diag.input.yaml`
- `chains/cmp_prtoe_pour_eval_h73.input.yaml`
- `chains/cmp_prtoe_pour_eval_noidr.input.yaml`
- `chains/cmp_prtoe_routeD.input.yaml`
- `chains/cmp_prtoe_twist.input.yaml`
- `chains/cmp_prtoe_twist.minimize.input.yaml`
- `chains/cmp_prtoe_zon.input.yaml`
- `chains/cmp_prtoe_zon_disp.input.yaml`
- `chains/dyad_mnu_bbnfix.input.yaml`
- `chains/dyad_mnu_mcmc.input.yaml`
- `chains/dyad_mnu_omk.input.yaml`
- `chains/test_minimal.input.yaml`

## Next (blocked until red/ref arm + owner)
1. Hold-out fraction + max |ΔlnL|
2. Active-learning budget
3. ESS floor
4. Dual-model dCDF+ΛCDM protocol
5. Feature schema from Cobaya columns
