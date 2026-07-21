#!/usr/bin/env python3
"""
The BBN half of the deuterium<->high-l link. Test (a) finds what the CMB wants
(omega_b, xi_Neff). This asks: does that SAME point heal deuterium, and what does
it cost helium? If the CMB-preferred (omega_b down, xi in-window) also lands D/H on
Cooke without wrecking Y_p, the below-T_c dark radiation is JP's one shared knob.

Response model (linear around the model's genesis BBN baseline; small shifts):
  D/H = D0 * (omega_b/ob0)^(-1.6) * exp(k_D * xi)
  Y_p = Y0 + 0.0096*ln(omega_b/ob0) + k_Y * xi
with the genesis baseline D0=2.387e-5, Y0=0.24900 at ob0=0.022757, xi=0
(PRTOE_bbn_witness.md run (ii)). Two coefficient sets are shown:
  - operational : the yaml BBN likelihood's all-epochs slopes (k_D=0.10, k_Y=0.0127)
                  -- what the chains actually use; conservative on helium.
  - below-T_c   : the physically-correct split (k_D=0.116 deuterium sees the full
                  reheated dark radiation; k_Y=0.0131/1.245=0.0105 helium, set above
                  T_c, sees only the un-reheated part) -- PRTOE_bbn_witness.md table.
"""
import numpy as np

ob0, D0, Y0 = 0.022757, 2.387e-5, 0.24900          # genesis baseline (xi=0)
DH_cooke, DH_meas = 2.527e-5, 0.030e-5             # Cooke+ 2018 (measurement error)
DH_budget = 0.056e-5                               # model nuclear+code budget (-2.5s at base)
Yp_aver, Yp_err = 0.2449, 0.0040                   # Aver+ 2015

def abund(ob, xi, kD, kY):
    DH = D0 * (ob/ob0)**(-1.6) * np.exp(kD*xi)
    Yp = Y0 + 0.0096*np.log(ob/ob0) + kY*xi
    return DH, Yp

def report(label, ob, xi):
    print(f"\n{label}:  omega_b={ob:.5f}, xi_Neff={xi:.4f}")
    for cname, kD, kY in [("operational (yaml, all-epochs)", 0.10, 0.0127),
                          ("below-T_c (physically split)  ", 0.116, 0.0105)]:
        DH, Yp = abund(ob, xi, kD, kY)
        sD_meas = (DH-DH_cooke)/DH_meas
        sD_bud  = (DH-DH_cooke)/DH_budget
        sY      = (Yp-Yp_aver)/Yp_err
        joint   = sD_bud**2 + sY**2
        print(f"  [{cname}]  D/H={DH*1e5:.3f}e-5 ({sD_meas:+.1f}s meas / {sD_bud:+.1f}s budget)"
              f"   Y_p={Yp:.4f} ({sY:+.1f}s)   joint chi2={joint:.2f}")

print("="*74)
print("BBN abundances at the CMB-preferred points (does the CMB point heal D?)")
print("="*74)
report("baseline / fiducial (xi off)      ", 0.022757, 0.0)
report("4D min, xi pinned OFF             ", 0.02290, 0.0)
report("test(a) transient (eval 77)       ", 0.02220, 0.1247)   # flattering mid-run vertex
report("test(a) CONVERGED (chi2=1021 floor)", 0.02269, 0.1422)   # the honest CMB preference

# where does deuterium center? the (omega_b, xi) locus with D/H = Cooke exactly
print("\n" + "="*74)
print("Deuterium-centering locus: (omega_b, xi) that put D/H exactly on Cooke 2.527")
print("(operational k_D=0.10; shows whether the CMB-preferred point sits near it)")
print("="*74)
for xi in (0.0, 0.06, 0.12, 0.18, 0.24):
    # solve 2.387*(ob/ob0)^-1.6 * exp(0.10*xi) = 2.527  ->  ob
    ob_star = ob0 * (D0*np.exp(0.10*xi)/DH_cooke)**(1.0/1.6)
    _, Yp = abund(ob_star, xi, 0.10, 0.0127)
    sY = (Yp-Yp_aver)/Yp_err
    print(f"  xi={xi:.2f}:  omega_b*={ob_star:.5f}  ->  Y_p={Yp:.4f} ({sY:+.1f}s vs Aver)")
print("\n  Read: if test(a) converges near one of these (omega_b*, xi) pairs, the CMB")
print("  and deuterium want the SAME point -- the link is closed on both ends.")
