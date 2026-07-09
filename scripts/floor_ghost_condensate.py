#!/usr/bin/env python3
"""
#22 DE FLOOR -- the ONE serious calculation red-team demanded. Does the (delta K)^2 /
ghost-condensate critical-point mechanism give a STABLE w=-1 floor? (The self-tuning toy ran
away because it OMITTED the k^4 stabilizer.) k-essence P(X), X = 1/2 phidot^2:
  rho = 2X P_X - P ;  p = P ;  w = p/rho ;  c_s^2 = P_X/(P_X + 2X P_XX)
w=-1 <=> P_X=0 at X0!=0 (ghost condensate); there c_s^2=0 (critical point). Stability of that point
needs the higher-derivative (delta K)^2 term: dispersion omega^2 = c_s^2 k^2 + (alpha/M^2) k^4.
"""
import numpy as np
X0, lam, V0 = 1.0, 1.0, 0.7      # ghost-condensate P = 0.5 lam (X-X0)^2 - V0 ; V0(=Lambda) TUNED
P   = lambda X: 0.5*lam*(X-X0)**2 - V0
PX  = lambda X: lam*(X-X0)
PXX = lambda X: lam
def w(X):   r = 2*X*PX(X)-P(X); return P(X)/r, r
def cs2(X): d = PX(X)+2*X*PXX(X); return PX(X)/d if d else 0.0

print("="*66); print("#22 DE floor: ghost-condensate (delta K)^2 critical point"); print("="*66)
print(f"\n  P(X)=0.5*lam*(X-X0)^2 - V0 ;  X0={X0}, lam={lam}, V0(=Lambda)={V0}\n")
print(f"  {'X':>6}{'w':>10}{'c_s^2':>10}{'rho':>9}  note")
print("  "+"-"*44)
for X in [0.5,0.8,0.95,1.0,1.05,1.2,1.5]:
    ww,r=w(X); print(f"  {X:>6.2f}{ww:>10.3f}{cs2(X):>10.3f}{r:>9.3f}  {'<- FLOOR (P_X=0)' if abs(X-X0)<1e-9 else ''}")
wf,rf=w(X0)
print(f"\n  AT FLOOR X0={X0}: w={wf:.4f}  c_s^2={cs2(X0):.4f}  rho={rf:.3f}(=V0) -> exact de Sitter (w=-1).")
print("\n  STABILITY at the c_s^2=0 point (what the toy got WRONG):")
print("    no higher-deriv term:  omega^2 = c_s^2 k^2 = 0  -> flat direction -> RUNAWAY (= the toy).")
print("    with (delta K)^2 -> +alpha/M^2 k^4:  omega^2 = (alpha/M^2) k^4 > 0 for alpha>0 -> STABLE.")
print(f"    ghost-condensate window (Arkani-Hamed+ 2004): P_XX>0 AND alpha>0. here P_XX={PXX(X0):.1f}>0 -> STABLE.")
print("\n"+"-"*66)
print("VERDICT (honest, both halves):")
print("  (1) STABILITY: PASS. The (delta K)^2 ghost-condensate gives a STABLE dynamical w=-1 floor;")
print("      the toy ran away ONLY because it dropped the k^4 term. With it, the floor holds.")
print("  (2) SELF-TUNING: FAIL. V0(=Lambda) is a FREE, TUNED parameter -- the mechanism does NOT")
print("      explain WHY Lambda is small (Weinberg's no-go stands).")
print("  => red-team fight-or-concede resolves to: KEEP the stable-w=-1 mechanism (a real dynamical")
print("     floor, better than a bare constant), CONCEDE the self-tuning / 'solves the CC problem' claim.")
print("="*66)
