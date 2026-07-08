#!/usr/bin/env python3
"""
#11 / Room 1 — does the dark condensate order parameter |Psi| GROW or SHRINK
between BBN (z~1e9) and recombination (z~1100)?  This decides whether the
deuterium heal survives (grows -> small shift at BBN -> heal) or the catastrophe
returns (shrinks -> big shift at BBN -> +11% D/H).

Fast analytic/algebraic core first (no solver, always completes); optional stiff
ODE confirmation last, hard-guarded so it can't hang.

Run:  python3 scripts/genesis_field_evolution.py
"""
import numpy as np

z_BBN, z_rec, z_osc, z_x = 1e9, 1100.0, 8e6, 1e5   # osc onset (H~m); condensation

print("="*68)
print("#11  DARK FIELD EVOLUTION  |Psi|(BBN)  vs  |Psi|(recomb)")
print("="*68)

# ---- READING 1: misalignment (frozen until H~m at z_osc, then |Psi| ~ a^-3/2)
# after z_osc, |Psi| ~ a^-3/2 ~ (1+z)^{3/2}; frozen (=const) for z>z_osc.
# BBN (z=1e9 > z_osc): frozen at Psi_i. recomb (z<z_osc): Psi_i*(a_osc/a_rec)^{3/2}.
mis_ratio = ((1+z_osc)/(1+z_rec))**1.5     # |Psi|_BBN / |Psi|_rec
print("\nREADING 1 -- misalignment (frozen, then redshifts as a^-3/2):")
print(f"  |Psi|_BBN / |Psi|_rec = ((1+z_osc)/(1+z_rec))^1.5 = {mis_ratio:.2e}")
print(f"  -> field ~{mis_ratio:.0e}x LARGER at BBN.  SHRINKS.")

# ---- READING 2: charged-AD centrifugal equilibrium  R_eq ~ a^-3/2
# dV_eff/dR=0: m^2 R = Q^2/(a^6 R^3) (m^2-dominated) -> R_eq = (Q^2/(m^2 a^6))^{1/4} ~ a^-3/2
cent_ratio = ((1+z_BBN)/(1+z_rec))**1.5
print("\nREADING 2 -- charged AD, centrifugal equilibrium R_eq ~ a^-3/2:")
print(f"  R_eq(BBN)/R_eq(rec) = ((1+z_BBN)/(1+z_rec))^1.5 = {cent_ratio:.2e}")
print(f"  -> field ~{cent_ratio:.0e}x LARGER at BBN.  SHRINKS.")

# ---- READING 3 (the HEAL branch): phase-transition / condensation growth
# |Psi| ~ 0 pre-condensation, grows to Psi0 through z_x. Needs small Psi_i (NON-AD).
need = 0.0015/0.0124   # |Psi|_BBN/|Psi|_rec for a 0.15% BBN shift vs 1.24% at recomb
print("\nREADING 3 -- phase-transition growth (the HEAL branch, needs small Psi_i):")
print(f"  needs |Psi|_BBN/|Psi|_rec ~ {need:.2f}  (order parameter ~12% formed at BBN)")
print("  -> would GROW (heal). But requires a small initial displacement --")
print("     NON-GENERIC for Affleck-Dine (which starts large).")

print("\n" + "-"*68)
print("VERDICT (analytic): the two AD-consistent readings BOTH give |Psi| far")
print("LARGER at BBN than at recombination -> the field SHRINKS -> the m_e/quark")
print("shift saturates HIGH at BBN -> D/H CATASTROPHE.  The heal (Reading 3)")
print("needs a small-Psi_i, non-AD genesis -- NOT what the model's Affleck-Dine")
print("field does generically.  So: sec.93 'grows/heals' is DISFAVORED; sec.94")
print("caveat CONFIRMED; the deuterium heal does NOT fall out of the AD field for")
print("free -- it needs the separate small radiation carrier (sec.91) or a")
print("different genesis.")
print("-"*68)

# ---- OPTIONAL: stiff ODE confirmation the field tracks R_eq (hard-guarded) -----
print("\n[optional] stiff-ODE check that a charged field SETTLES onto R_eq ~ a^-3/2:")
try:
    import signal
    from scipy.integrate import solve_ivp
    from scipy.optimize import brentq
    class TO(Exception): pass
    def _h(sig,frm): raise TO()
    signal.signal(signal.SIGALRM,_h); signal.alarm(30)   # 30s hard cap
    m2, lam, Q2 = 1.0, 1e-6, 1.0
    def Req(a): return brentq(lambda R: m2*R+2*lam*R**3-Q2/(a**6*R**3), 1e-6, 1e6)
    Hi, Ni, Nf = 8.0, 0.0, 4.0
    def Hf(N): return Hi*np.exp(-2*(N-Ni))
    def rhs(N,y):
        R,dR=y; a=np.exp(N)
        return [dR, -dR-(m2*R+2*lam*R**3-Q2/(a**6*R**3))/Hf(N)**2]
    R0=Req(np.exp(Ni))
    sol=solve_ivp(rhs,[Ni,Nf],[3*R0,0.0],method='Radau',rtol=1e-5,atol=1e-8,max_step=0.05)
    signal.alarm(0)
    print(f"  Radau ok={sol.success}: started 3x above eq, ended R={sol.y[0,-1]:.3e}"
          f" vs R_eq={Req(np.exp(Nf)):.3e}  (equilibrium ~ a^-3/2, decreasing).")
except TO:
    print("  (ODE hit 30s guard -- analytic verdict above stands regardless.)")
except Exception as e:
    print(f"  (ODE skipped: {e!r} -- analytic verdict above stands regardless.)")
