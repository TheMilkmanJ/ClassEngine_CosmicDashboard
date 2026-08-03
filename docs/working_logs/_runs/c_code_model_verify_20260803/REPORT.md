# C-code ↔ model verification (2026-08-03)

## Verdict

**YES — production CLASS C matches the as-built dCDF model**, with documented side channels.

## Numeric spot-checks (classy)

### Barotropic \(w=-\rho_\infty/\rho\) (correct units)

- Input `dcdf_rho_inf` = 0.7 in **H0²** units → ρ_∞_phys = 3.816390e-08 Mpc⁻²
- w(z=0) = **-0.734602**, −ρ_∞/ρ(0) = **-0.734602**, |Δ| = 2.220e-16
- max|w·ρ+ρ_∞| for z<10: 3.309e-23 (rel 8.670e-16)
- **PASS**

### \(c_s^2\equiv 0\)

- max |cs2_dcdf| over table: machine zero → **PASS**

### Thaw (Route D)

- Δw_dcdf(thaw=0.12 vs 0) ~ 1e-12 → column blind **by design**
- |Δp_tot|/|p| ~ 0.12, Δage ~ −0.13 Gyr → totals **live** → **PASS**

### Conversion

- `dcdf_conv_g>0` runs; intermediate ρ and w differ from bare; z=0 shooting matches Ω target → **PASS** (implemented)

## Claim matrix

See `CLAIM_MATRIX.md` in this directory.

## Scope

CLASS C = dCDF cosmology + varconst/dyad + conversion + thaw branch.
**Not** in this tree: T14 GP, BBN PRyM, Koide, bounce, Page dynamics.
