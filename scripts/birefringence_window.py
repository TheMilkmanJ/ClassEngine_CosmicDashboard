#!/usr/bin/env python3
"""
#11b -- The birefringence window: is a residual OPEN (normal / un-condensed)
account still alive at recombination (z~1100)?

The parity-odd photon coupling rides the NORMAL fraction f_n -- the still-massless,
w=1/3 part of the medium (the "open account"). It closes as the medium condenses.
Isotropic CMB birefringence at recombination is possible ONLY if f_n(z=1100) is
non-negligible.

Two-fluid superfluid: below T_c the normal density dies as a power of T/T_c
(n=4 for a phonon branch, rho_n ~ T^4; a softer dispersion gives a smaller n;
a GAPPED branch dies exponentially, faster still -- so n=4 is the *best* case).
   T/T_c = (1+z)/(1+z_x),   z_x = condensation redshift (basin entry, mu=m)
   f_n(z_rec) = ((1+z_rec)/(1+z_x))^n

Run:  python3 scripts/birefringence_window.py
"""
import numpy as np

z_rec = 1100.0
z_eq  = 3400.0      # matter-radiation equality (reference)
z_x_model = 1e5     # the model's condensation redshift (basin entry, mu=m)

print("=" * 70)
print("#11b  BIREFRINGENCE WINDOW -- residual normal fraction at recombination")
print("=" * 70)
print(f"\n  f_n(z_rec) = ((1+z_rec)/(1+z_x))^n ,   z_rec = {z_rec:.0f}")
print("  n=4  phonon superfluid (rho_n ~ T^4, the SLOWEST-dying / best case)")
print("  n=2  a soft/optimistic dispersion (still power-law)\n")

print(f"  {'z_x':>10}  {'T_rec/T_c':>10}  {'f_n (n=4)':>12}  {'f_n (n=2)':>12}")
print("  " + "-" * 52)
for z_x in [z_x_model, 3e4, 1e4, z_eq, 2000.0, 1500.0]:
    r = (1 + z_rec) / (1 + z_x)
    print(f"  {z_x:>10.0f}  {r:>10.4f}  {r**4:>12.2e}  {r**2:>12.2e}")

# threshold: what z_x makes f_n reach 1% (a marginally-live window)?
print()
for n in (4, 2):
    r_thr = 0.01 ** (1.0 / n)
    z_x_thr = (1 + z_rec) / r_thr - 1
    print(f"  window reaches f_n = 1%  (n={n})  at  z_x = {z_x_thr:.0f}"
          f"   ({z_x_model / z_x_thr:.0f}x below the model's z_x=1e5)")

print("\n" + "-" * 70)
print("VERDICT: at the model's z_x ~ 1e5, f_n(rec) ~ 1e-8 (n=4) -- the open")
print("account is dead ~8 orders before recombination -> birefringence")
print("suppressed ~1e-8 -> WINDOW CLOSED.  It opens (f_n >~ 1%) only if")
print("condensation is pushed down to z_x ~ few x 10^3 (near equality),")
print("~30x lower than the model gives.  So P-009's null holds here too,")
print("UNLESS #11 pins z_x near matter-radiation equality.")
print("-" * 70)
