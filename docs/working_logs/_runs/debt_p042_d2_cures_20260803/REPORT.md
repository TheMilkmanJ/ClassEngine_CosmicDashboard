# D2 cures (Claude RED) — 2026-08-03

## (ii) Thaw instrument test (`dcdf_floor_thaw` max allowed = 0.5)

- thaw=0.0: w(0)=-0.73460176 w(1)=-0.25708225 w(10)=-0.00207694
- thaw=0.12: w(0)=-0.73460176 w(1)=-0.25708225 w(10)=-0.00207694
- thaw=0.5: w(0)=-0.73460176 w(1)=-0.25708225 w(10)=-0.00207694

- max|Δw| thaw=0.5 vs 0 over history: **2.211e-12**
- **VERDICT (Claude D2-ii): `(.)w_dcdf` is BLIND to thaw — thaw column in truth table is VOID as physics, not “no effect.”**

### Other outputs vs thaw (z=0)

- `(.)p_tot`: max|Δ|=1.585e+29, |Δ|(z=0) rel=5.000e-01
- `(.)p_tot_prime`: max|Δ|=1.914e+38, |Δ|(z=0) rel=1.598e+04
- `(.)rho_crit`: max|Δ|=5.546e+29, |Δ|(z=0) rel=2.238e-12
- `(.)rho_dcdf`: max|Δ|=1.536e+23, |Δ|(z=0) rel=2.349e-12
- `(.)rho_tot`: max|Δ|=3.961e+29, |Δ|(z=0) rel=2.238e-12
- `(.)w_dcdf`: max|Δ|=2.211e-12, |Δ|(z=0) rel=2.349e-12
- `H [1/Mpc]`: max|Δ|=1.258e+07, |Δ|(z=0) rel=1.119e-12
- `Omega_m(z)`: max|Δ|=9.222e-02, |Δ|(z=0) rel=5.226e-12
- `Omega_r(z)`: max|Δ|=4.215e-05, |Δ|(z=0) rel=2.238e-12
- `ang.diam.dist.`: max|Δ|=1.037e+02, |Δ|(z=0) rel=0.000e+00
- `comov. dist.`: max|Δ|=3.101e+02, |Δ|(z=0) rel=0.000e+00
- `comov.snd.hrz.`: max|Δ|=9.469e+00, |Δ|(z=0) rel=7.861e-03
- `conf. time [Mpc]`: max|Δ|=3.101e+02, |Δ|(z=0) rel=2.231e-02
- `gr.fac. D`: max|Δ|=2.353e-02, |Δ|(z=0) rel=0.000e+00
- `gr.fac. f`: max|Δ|=6.472e-02, |Δ|(z=0) rel=1.193e-02
- `lum. dist.`: max|Δ|=3.101e+16, |Δ|(z=0) rel=0.000e+00
- `proper time [Gyr]`: max|Δ|=5.876e-01, |Δ|(z=0) rel=4.365e-02

## (i) Energy budget high-z (bare)

rho keys: `(.)rho_b`, `(.)rho_cdm`, `(.)rho_crit`, `(.)rho_dcdf`, `(.)rho_g`, `(.)rho_ncdm[0]`, `(.)rho_tot`, `(.)rho_ur`

| z | (.)rho_dcdf | (.)rho_g | (.)rho_ur | (.)rho_ncdm[0] | (.)rho_tot | (.)rho_b | (.)w_dcdf | (.)cs2_dcdf |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1e+09 | +1.37998e+19 | +2.75473e+24 | +1.27176e+24 | +6.33876e+23 | +4.66071e+24 | +2.49449e+18 | -2.76553e-27 | +0.00000e+00 |
| 4.001e+08 | +8.83067e+17 | +7.05081e+22 | +3.25511e+22 | +1.62243e+22 | +1.19292e+23 | +1.59625e+17 | -4.32174e-26 | +0.00000e+00 |
| 1e+08 | +1.38022e+16 | +2.75536e+20 | +1.27205e+20 | +6.34022e+19 | +4.66184e+20 | +2.49492e+15 | -2.76506e-24 | +0.00000e+00 |
| 4.001e+07 | +8.83220e+14 | +7.05244e+18 | +3.25586e+18 | +1.62280e+18 | +1.19325e+19 | +1.59653e+14 | -4.32100e-23 | +0.00000e+00 |
| 1e+07 | +1.38046e+13 | +2.75600e+16 | +1.27234e+16 | +6.34168e+15 | +4.66419e+16 | +2.49535e+12 | -2.76458e-21 | +0.00000e+00 |
| 9.997e+05 | +1.37736e+10 | +2.74776e+12 | +1.26854e+12 | +6.32273e+11 | +4.66484e+12 | +2.48975e+09 | -2.77079e-18 | +0.00000e+00 |

### ρ_dcdf / ρ_tot

- z=1e+09: f_dcdf=0.0000
- z=4.001e+08: f_dcdf=0.0000
- z=1e+08: f_dcdf=0.0000
- z=4.001e+07: f_dcdf=0.0001
- z=1e+07: f_dcdf=0.0003
- z=9.997e+05: f_dcdf=0.0030

## Net for P-042

1. Do not quote thaw physics from `(.)w_dcdf` until the code path is fixed or another observable is used.
2. Pre-onset radiation claim must be adjudicated on species that carry the rad-onset budget, not w_dcdf alone.

## Claude D2 consequence (applied)

P-042 pre-onset w=1/3 claim's referee is the **dark-radiation / ΔN_eff budget**, not `(.)w_dcdf`.
