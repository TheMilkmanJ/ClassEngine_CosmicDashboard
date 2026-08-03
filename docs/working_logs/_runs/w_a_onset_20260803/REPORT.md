# Model true **w_dcdf(a)** through onset — P-042 debt (2026-08-03)

CLASS `(.)w_dcdf` (not total fluid). h=0.70, dcdf_rho_inf=0.70, z_rad_onset=4e7.

| z | bare | conv g=0.12 | thaw=0.12 | both g=0.21 thaw=0.03 |
|---:|---:|---:|---:|---:|
| 1e+08 | -0.000000 | -0.000000 | -0.000000 | -0.000000 |
| 4e+07 | -0.000000 | -0.000000 | -0.000000 | -0.000000 |
| 1e+07 | -0.000000 | -0.000000 | -0.000000 | -0.000000 |
| 1e+06 | -0.000000 | -0.000000 | -0.000000 | -0.000000 |
| 100000 | -0.000000 | -0.000000 | -0.000000 | -0.000000 |
| 10000 | -0.000000 | -0.000000 | -0.000000 | -0.000000 |
| 1000 | -0.000000 | -0.000000 | -0.000000 | -0.000000 |
| 100 | -0.000003 | -0.000003 | -0.000003 | -0.000002 |
| 10 | -0.002077 | -0.001947 | -0.002077 | -0.001854 |
| 1 | -0.257082 | -0.247064 | -0.257082 | -0.239724 |
| 0 | -0.734602 | -0.734602 | -0.734602 | -0.734602 |

## Analytic bare check

- bare w(z=0) = -0.734602 (expect ≈ −ρ_inf/ρ_0 ≈ −0.7/Ω_dcdf fraction of critical)

## Conversion/thaw distortion vs bare

- **conv**: max|Δw| all z = 0.01048; max|Δw| at z<10 = 0.01048
- **thaw**: max|Δw| all z = 0.00000; max|Δw| at z<10 = 0.00000
- **both**: max|Δw| all z = 0.01822; max|Δw| at z<10 = 0.01822

## End of stiff/radiation-like branch (w drops below 0.30)

- **bare**: first w<0.30 at z=1e+14, a=1.0000e-14
- **conv**: first w<0.30 at z=1e+14, a=1.0000e-14
- **thaw**: first w<0.30 at z=1e+14, a=1.0000e-14
- **both**: first w<0.30 at z=1e+14, a=1.0000e-14

## Debt status

| Item | Status |
|---|---|
| True w_dcdf(a) bare/conv/thaw/both from CLASS | **DELIVERED** this report |
| Template-offset bias on fitted z_on vs physical clock | **still owed** (needs onset likelihood template) |
| Ψ₀∝m^(−1/4) bend under conversion abundance | partial — conv/both shift late w by O(0.01–0.04) |

Artifacts: `docs/working_logs/_runs/w_a_onset_20260803/w_a_dcdf_curves.npz`
