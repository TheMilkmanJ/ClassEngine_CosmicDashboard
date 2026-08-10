# N1 scorecard — compute 2026-08-04

**Script:** `scripts/bounce_n1_fa2_amplitude_hunt.py`  
**Log:** [`logs/n1_fa2_amplitude_hunt.log`](./logs/n1_fa2_amplitude_hunt.log)  
**exit 0 ≠ PASS:** compute finished; physics grade = OPEN-BLOCKED

## Anchors

| | |
|---|---|
| \(c_s\) | 0.147960 |
| \(H_\mathrm{door}\) | \(1.894392\times10^{-21}\) eV |
| \(\rho_\mathrm{eff}^{1/4}\) | 2826.8 eV |
| \(\rho_\mathrm{bounce}^{1/4}\) | 1059.2 eV |
| \(\|H_\mathrm{kin}(\Theta=1,d=3)\|/H_\mathrm{door}\) | 0.085424 |
| \(\|H_\mathrm{kin}(\mathrm{late},d=3)\|/H_\mathrm{door}\) | 0.005290 |
| \(\Theta_\mathrm{lock}\) (d=3) | 11.706 |
| late \(\Theta\) (0D) | +0.0619 |
| overshoot (0D) | 1.340 |
| \(\rho_\mathrm{need}/\rho_\mathrm{eff}\) (late inverse) | \(2.799\times10^{-5}\) |

## Per-candidate \(|H_\mathrm{kin}|/H_F(\rho)\)

| ID | grade | \|Hkin\|/HF | ρ/ρ_eff | ρ^{1/4} (eV) |
|---|---|---:|---:|---:|
| C0 | DEAD-as-law | 5.29e-03 | 1.00 | 2827 |
| C1 | WRONG-OBJECT | 3.77e-02 | 1.97e-02 | 1059 |
| C2a | DEAD-as-law | 6.41e-03 | 0.682 | 2569 |
| C2b | WRONG-OBJECT | 4.56e-02 | 1.34e-02 | 963 |
| C3 | DEAD-as-law | 6.12e-03 | 0.746 | 2627 |
| C4 | TAUTOLOGY | **1.00** | 2.80e-05 | 206 |
| C5 | DEAD-as-law | 1.97 | 7.20e-06 | 146 |
| C6 | STILL-OPEN | 8.54e-02 | 1.00 | 2827 |
| C7 | MISSING_INPUT | **1.00** | 1.00 | 2827 |
| C8a | FABRICATED | 2.25e-08 | 5.54e+10 | 1.37e6 |
| C8b | FABRICATED | **1.00** | 2.80e-05 | 206 |

## Aggregate

| metric | value |
|---|---:|
| candidates | 11 |
| legal LANDs | **0** |
| tautologies | 1 |
| fabricated | 2 |
| missing-input | 1 |
| `can_land_F_A2_from_stocked_parts` | **false** |
| obstruction C | **stands** |
| bounce_closed | false |
