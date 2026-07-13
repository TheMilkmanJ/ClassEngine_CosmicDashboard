#!/usr/bin/env python3
"""B1 v3 — strike-14's destination RAMP + the two cited corrections (sweep 62 spec):
(1) MERGER QUEUE (parameter-free): rejected parcels remember their feed speed;
    a parcel merges into the ring whenever U_ring < U_parcel/2 (same sigmoid width
    as acceptance — no new constants). The wake pays a decaying tail into the ring.
(2) OVERPRESSURE: measured impulse = 1.35 +/- 0.07 x slug value [cited].
(3) BUBBLE (share only): the ring carries entrained ambient ~ B = 1.9 +/- 0.8 x its
    fed volume [the softest input — reported with its band].
Same chi, same sealed targets: eps=0.88, share=0.843, L/D in [4.3,5.3], n in [10,30]."""
import numpy as np

def run(chi, ovp=1.35, B=1.9, a_over_D=0.15, n_t=8000):
    tau = np.linspace(0, 3*chi, n_t); dt = tau[1]-tau[0]
    U = (1-np.exp(-tau/0.5))*np.exp(-(tau/chi)**2)
    dGam, dP, dM = U**2/2*dt, ovp*U**2*(np.pi/4)*dt, U*(np.pi/4)*dt
    Gam = P = M = 1e-12
    wake = []   # rejected parcels: (U_parcel, gam, p, m)
    a = a_over_D
    for i in range(n_t):
        R = max(np.sqrt(P/(np.pi*Gam)), 0.5) if Gam > 1e-10 else 0.5
        Ur = Gam/(4*np.pi*R)*(np.log(8*R/a)-0.25)
        w = 1/(1+np.exp(-np.clip((U[i]/2-Ur)/0.25, -30, 30)))
        Gam += w*dGam[i]; P += w*dP[i]; M += w*dM[i]
        if w < 0.999: wake.append([U[i], (1-w)*dGam[i], (1-w)*dP[i], (1-w)*dM[i]])
        # THE MERGER TAIL: every 40 steps, parcels with U_p/2 > Ur pay in (ramped)
        if i % 40 == 0 and wake:
            keep = []
            for p_ in wake:
                wm = 1/(1+np.exp(-np.clip((p_[0]/2-Ur)/0.25, -30, 30)))
                Gam += wm*p_[1]; P += wm*p_[2]; M += wm*p_[3]
                p_[1] *= (1-wm); p_[2] *= (1-wm); p_[3] *= (1-wm)
                if p_[1] > 1e-12: keep.append(p_)
            wake = keep
    R = np.sqrt(P/(np.pi*Gam))
    Gt, Mt = (U**2/2*dt).sum(), (U*(np.pi/4)*dt).sum()
    share = M*B/(M*B + (Mt-M))
    return dict(eps=Gam/Gt, share=share, LD=Mt/(np.pi/4), Ra=R/a, n=2.26*R/a)

print(f"{'chi':>5s} {'L/D':>6s} {'eps':>7s} {'share':>7s} {'n':>5s}   targets: 0.88 / 0.843 / [4.3,5.3] / 10-30")
best = None
for chi in [3.0, 4.0, 4.75, 5.3, 6.5, 8.0]:
    r = run(chi)
    hit = (abs(r['eps']-0.88)<0.04 and abs(r['share']-0.843)<0.04
           and 4.3 < r['LD'] < 5.3 and 10 < r['n'] < 30)
    print(f"{chi:5.2f} {r['LD']:6.2f} {r['eps']:7.3f} {r['share']:7.3f} {r['n']:5.0f}   {'<-- CO-LAND' if hit else ''}")
print("\nsensitivity at chi=4.75 (the bands of the cited inputs):")
for ovp in [1.28, 1.35, 1.42]:
    for B in [1.1, 1.9, 2.7]:
        r = run(4.75, ovp=ovp, B=B)
        print(f"  ovp={ovp:.2f} B={B:.1f}: eps={r['eps']:.3f} share={r['share']:.3f} n={r['n']:.0f}")
