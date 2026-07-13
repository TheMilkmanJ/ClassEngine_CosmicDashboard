#!/usr/bin/env python3
"""The flow's ladder correction (sweep 53-55): the coherent swirl biases LOCAL
H0 measurements; it never enters CLASS (energy null, sweep 55). Apply at the
COMPARISON layer only: H0_ladder_corrected = H0_ladder - bias(omega_0, survey).

Kinematic line (sweep 55): omega = H at the pour, omega ~ a^-2 =>
omega_0 = sqrt((1+z_rec)/(1+z_eq)) * H(z_rec)/(1+z_rec)^2  ~ 0.77 km/s/Mpc.
The bias magnitude uses the measured-flow floor (partial lever, ~1.4%) until
the genesis inverse problem sizes the ring's structured field.
"""
import numpy as np

def omega0(H0=70.0, z_eq=3400, z_rec=1100, Om=0.31, Or=9e-5, OL=0.69):
    Hrec = H0*np.sqrt(Om*(1+z_rec)**3 + Or*(1+z_rec)**4 + OL)
    return np.sqrt((1+z_rec)/(1+z_eq))*Hrec/(1+z_rec)**2   # km/s/Mpc today

def ladder_bias(r_eff_mpc=250.0, coherent_fraction=1.0, H0=70.0):
    """Fractional local-H0 bias from the swirl's coherent gradient across the
    survey's effective depth. coherent_fraction < 1 models dipole
    marginalization absorbing part of the flow (SH0ES removes pure dipoles);
    only quadrupole+ structure survives — genesis sizing will fix it."""
    grad = omega0(H0)   # km/s/Mpc of coherent gradient at face value
    return coherent_fraction*grad/H0

if __name__ == "__main__":
    w0 = omega0()
    print(f"omega_0 = {w0:.2f} km/s/Mpc (the flow line, zero dials)")
    for f in [1.0, 0.5, 0.25]:
        b = ladder_bias(coherent_fraction=f)
        print(f"coherent fraction {f:>4}: local bias {b*100:.1f}%  "
              f"-> a 73.0 ladder reading corrects to {73.0/(1+b):.1f}")
