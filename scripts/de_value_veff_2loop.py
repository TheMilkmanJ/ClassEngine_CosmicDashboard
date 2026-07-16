import numpy as np
from scipy import optimize
alpha=1/137.035999; me=510998.95; pi=np.pi

# V_eff(phi) from the electron, m_e(phi)=m_e0(1+kappa phi^2). Work with L = ln(m_e0^2/mu^2).
# 1-loop induced dyad mass^2 (kappa factored out; only sign/scale matters):
#   m_phi^2(mu)/kappa = -(1/2pi^2) m_e0^4 (L - 3/2)     [tachyonic <=> L>3/2]
# 2-loop O(alpha) correction adds inside the bracket: (alpha/pi)[c2 L^2 + c1 L + c0].
# The LOG coefficients c2,c1 are RG-FIXED by the 1-loop gamma_m; c0 is the genuine 2-loop constant.

print("=== (1) SSB threshold: the 1-loop induced mass is tachyonic only for L > 3/2 ===")
for muk in [510998.95, 310e3, 193e3, 100e3, 60e3]:
    L=np.log(me**2/muk**2)
    print(f"   mu={muk/1e3:6.1f} keV: L={L:5.2f}  bracket(L-3/2)={L-1.5:+5.2f}  {'SSB' if L>1.5 else 'NO SSB'}")
print("   => at the natural scale mu=m_e (L=0): NO SSB. Breaking needs mu<~310 keV, i.e. a LARGE log.")

print("\n=== (2) The decisive test: does the 2-loop give a PHYSICAL PMS (scale where dT_c/dln_mu=0)? ===")
# T_c ~ sqrt(bracket).  d(bracket)/dln_mu: 1-loop = -2 (from -dL/dln_mu... L=ln(me^2/mu^2), dL/dln_mu=-2).
# 2-loop log^2 term (alpha/pi)c2 L^2 -> d/dln_mu = (alpha/pi)c2 * 2L * (-2) = -(4alpha/pi)c2 L.
# stationarity: -2 - (4alpha/pi)c2 L = 0  ->  L_PMS = -pi/(2 alpha c2).
print("   PMS condition: L_PMS = -pi/(2 alpha c2), any O(1) 2-loop coeff c2:")
for c2 in [-3,-1,-0.3]:
    Lpms=-pi/(2*alpha*c2)
    mu_pms=me*np.exp(-Lpms/2)
    print(f"   c2={c2:+.1f}: L_PMS={Lpms:7.1f}  ->  mu_PMS/m_e = e^-{Lpms/2:.0f} = {mu_pms/me:.1e}  (mu_PMS={mu_pms:.1e} eV)")
print("   => for ANY O(1) 2-loop coefficient, L_PMS ~ 1/alpha ~ 200 -> mu_PMS ~ e^-100 m_e -- UNPHYSICAL.")

print("\n=== VERDICT ===")
print("The 2-loop RG-improvement does NOT pin T_c. The QED coupling is too small (alpha~1/137): the 2-loop")
print("curvature is O(alpha), so the scale-stationary point sits at a log ~ 1/alpha, i.e. mu ~ e^-100 m_e --")
print("far below any physical scale. Independent of the (uncomputed) 2-loop constant c0. So T_c is NOT a")
print("perturbatively well-defined quantity: the dyad's electron-CW condensation is a LARGE-LOG / marginal")
print("effect (no SSB at mu=m_e; SSB only in the large-log regime where the expansion is unreliable).")
print("=> the seam DE route rho_L^1/4=(9/2)alpha^4 T_c rests on an ill-defined T_c. This is the honest, ")
print("   BUILT result -- a definite negative, not a handoff. The condensation needs a NON-perturbative")
print("   (gap-equation / lattice-class) treatment to define T_c, if it survives at all.")
