"""How many turns does the winding actually complete, and does f_bar's premise survive?

Branch (a) of the alpha_c conflict needs f_bar to sit ~2% off 2/pi, which the finite-turn
envelope says requires a winding of about five turns or fewer. The corpus grants
equidistribution rather than deriving it (DERIVATION_HUNT's f_bar row: "The equidistribution is
granted"), so the grant is worth pricing.

Two recorded facts settle it. Baryogenesis carries theta_dot/H = 2.4e6 at T_sph and
theta_dot proportional to T^3. In a radiation background H goes as T^2, so:

    turns per Hubble time  ~  (theta_dot/H)/2pi  falls LINEARLY with T
    total accumulated turns ~ integral theta_dot dt, which SATURATES

because theta_dot dt = (theta_dot/H)_sph dT/T_sph -- the integrand is flat in T, so almost all
the winding is laid down near T_sph and essentially none below it.

Those two readings answer the question differently, and the corpus does not say which sets f_bar.

Run: python3 scripts/winding_turn_budget.py
"""
import math

RATIO_SPH = 2.4e6            # theta_dot/H at T_sph, recorded
T_SPH_GEV = 130.0            # the standard electroweak sphaleron shutoff
T_REC_EV = 0.26              # recombination


def turns_per_hubble(T_over_Tsph):
    """(theta_dot/H)/2pi, which scales as T because theta_dot ~ T^3 and H ~ T^2."""
    return RATIO_SPH * T_over_Tsph / (2 * math.pi)


print("=" * 76)
print("READING 1 -- TURNS PER HUBBLE TIME, WHICH FALLS WITH TEMPERATURE")
print("=" * 76)
print(f"  at T_sph:  theta_dot/H = {RATIO_SPH:.1e}  ->  {turns_per_hubble(1.0):.3e} turns per Hubble time")
print()
print(f"  {'T/T_sph':>10}  {'T (with T_sph = 130 GeV)':>26}  {'turns per Hubble':>18}")
print("  " + "-" * 60)
for r, lab in ((1.0, "130 GeV"), (1e-3, "130 MeV"), (1.31e-5, "1.7 MeV"),
               (1e-8, "1.3 keV"), (T_REC_EV / (T_SPH_GEV * 1e9), "0.26 eV (recombination)")):
    print(f"  {r:10.2e}  {lab:>26}  {turns_per_hubble(r):18.3e}")
print()
r5 = 5 * 2 * math.pi / RATIO_SPH
print(f"  the five-turn threshold branch (a) needs is crossed at T/T_sph = {r5:.3e},")
print(f"  i.e. T = {r5*T_SPH_GEV*1e3:.2f} MeV on a 130 GeV sphaleron shutoff.")
print("  Below that the instantaneous winding is too slow for equidistribution, and by")
print(f"  recombination it is {turns_per_hubble(T_REC_EV/(T_SPH_GEV*1e9)):.1e} turns per Hubble time -- entirely frozen.")

print()
print("=" * 76)
print("READING 2 -- TOTAL ACCUMULATED TURNS, WHICH SATURATES")
print("=" * 76)
print("  theta_dot dt = (theta_dot/H)_sph . dT/T_sph, so the accumulated winding from T_sph")
print("  down to T is (theta_dot/H)_sph . (1 - T/T_sph) radians -- flat in T, hence dominated")
print("  by the earliest epoch and saturating almost immediately.")
print()
print(f"  {'down to T/T_sph':>16}  {'accumulated turns':>19}  {'% of the total':>15}")
print("  " + "-" * 56)
tot = RATIO_SPH / (2 * math.pi)
for r in (0.5, 0.1, 0.01, 1e-4, 0.0):
    acc = tot * (1 - r)
    print(f"  {r:16.0e}  {acc:19.4e}  {acc/tot*100:14.1f}%")
print()
print(f"  total accumulated winding below T_sph: {tot:.3e} turns")

print()
print("=" * 76)
print("WHAT EACH READING DOES TO f_bar, AND SO TO BRANCH (a)")
print("=" * 76)


def env(N):
    def _G(x):
        m, r = divmod(x, math.pi)
        return 2 * m + (math.sin(r) if r <= math.pi / 2 else 2 - math.sin(r))

    def mac(n, p):
        T = 2 * math.pi * n
        return (_G(p + T) - _G(p)) / T
    return max(abs(mac(N + j / 100.0, math.pi * k / 50) / (2 / math.pi) - 1)
               for j in range(100) for k in range(50))


print(f"  on the ACCUMULATED reading, N = {tot:.2e} turns:")
print(f"    worst-case deviation of f_bar from 2/pi  ~ {0.1009/tot*100:.2e}%")
print(f"    against the {2.08:.2f}% branch (a) needs  ->  the route is DEAD by six orders")
print()
print("  on the INSTANTANEOUS reading the answer depends entirely on the epoch that sets")
print(f"  epsilon: above ~{r5*T_SPH_GEV*1e3:.1f} MeV the premise holds, below it the phase is frozen and")
print("  f_bar is not an average at all but whatever value the phase happens to sit at.")
print()
print("  So the two readings do not merely differ in precision, they differ in kind, and")
print("  nothing recorded says which one the epsilon-assembly uses. That is the owed piece:")
print("  not 'is equidistribution granted' but 'over what window is the average taken'.")
print("  Under the accumulated reading -- the natural one for a phase that has been winding")
print("  since genesis -- f_bar is pinned and the alpha_c conflict stands at its full 2.08%.")
