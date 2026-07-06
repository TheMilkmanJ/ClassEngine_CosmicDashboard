import numpy as np
from classy import Class

c = Class()
c.set({
    'h': 0.674, 'Omega_b': 0.05, 'Omega_cdm': 0.25,
    'A_s': 2.1e-9, 'n_s': 0.965,
    'Omega_Lambda': 0.0,
    'root': '/home/themilkmanj/prtoe_class/',
})
print("Computing CLASS for H_dot verification...")
c.compute()

bg = c.get_background()
z = bg['z']
a = 1.0 / (1.0 + z)
H = bg['H [1/Mpc]']
t = bg['proper time [Gyr]'] * 306.6013938  # Gyr to Mpc

# Calculate numerical H_dot = dH/dt properly using coordinate spacing
# dt = dz / (-H * (1+z))
# H_dot = dH/dz * dz/dt
dH_dz = np.gradient(H, z)
H_dot_num = dH_dz * (-H * (1.0 + z))

# Extract the solver's exact H_prime which we added to background_output_data
H_prime_solver = bg['(.)H_prime']
H_dot_solver = H_prime_solver / a

print("Comparing solver analytical vs numerical H_dot...")
mask = (z < 1e5) & (z > 0)
diffs = np.abs((H_dot_num[mask] - H_dot_solver[mask]) / H_dot_solver[mask])
max_diff = np.max(diffs)
mean_diff = np.mean(diffs)

print(f"Max relative difference across all z < 10^5: {max_diff:.3e}")
print(f"Mean relative difference: {mean_diff:.3e}")
if max_diff < 1e-2:
    print("SUCCESS: H_dot algebra landed! Agreement is solid across integration.")
else:
    print("WARNING: Discrepancy found.")

