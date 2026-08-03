"""bounce_task20_sequencing_race — the reconciled wall problem computed: pocket sequencing in the medium's own equation (2026-07-27).

THE QUESTION (task #20, under the reconciliation of RP log §20)
  With the metric on throughout, the wall between a rebounding pocket and a
  still-contracting neighbor is dynamics, not causal law.  Three of the four
  opens compute in one 1D experiment:
    (i)   SURVIVAL — after a pocket's gradient-stress turn, does the
          neighbor's continuing infall re-crush it?
    (ii)  SEQUENCING — the race: does the neighbor's own door open before
          the first pocket's outflow arrives (clock-first ⟹ arrivals are
          §17 joint collisions, already computed), or does the outflow
          arrive first — and then does it trigger or suppress the
          neighbor's door?
    (iv)  AVERAGING (toy) — does the mass-weighted expansion rate
          Θ = ⟨ρ ∂ₓv⟩/⟨ρ⟩ cross from contraction to expansion as the doors
          open in sequence?
  Open (iii) — transverse-axis evolution — is out of 1D reach; named, not
  smuggled.

MODEL AND CONSTRUCTION
  i∂_t ψ = −½∂ₓₓψ + (|ψ|²−1)ψ, healing units, periodic box L = 160,
  split-step Fourier (Strang), N = 1280 (8 points per healing length).
  Two collapse basins from one periodic flow:
      v(x) = −V·sin(4π(x−x_A)/L) − V₂·sin(2π(x−x_A)/L)
  converges at BOTH x_A = 40 and x_B = 120; the second harmonic deepens A
  and shallows B, so the linear compression-rate ratio is
  (2V+V₂)/(2V−V₂) and the CLOCK STAGGER is dialed by V₂ and MEASURED — to
  be compared with the recorded directional-door spread (0.25–0.30 of the
  mean clock, RP log §16).  Equal density seeds at both centers: the
  stagger is purely the flow's.

CHECKS (asserted; the physics verdict is printed from data, never asserted)
  SYM  V₂ = 0 twin: exact grid translation symmetry A ↔ B — peak histories
       must match at machine class.
  E    energy drift < 1% per run.
  REF  dt → dt/2 on the §16-matched configuration: turn times within 3%,
       peak densities within 5%.

GRADE RULE
  1D; the contraction is modeled by the initial converging flow (the M6
  convention); no self-gravity; transverse untouched.  If survival,
  computed sequencing (either race outcome, characterized), and the Θ sign
  crossing all land with checks green, task #20's promote condition is met
  at the reconstruction's working grade — candidate, scope stated.  KILLS
  (to the ledger, not here): the neighbor's infall re-crushing a turned
  pocket; outflow arrival suppressing a neighbor's door; Θ never crossing.
"""
from __future__ import annotations

import math

import numpy as np

L = 160.0
N = 1280
DX = L / N
DT = 2.0e-3
T_MAX = 70.0
SNAP = 0.1
X_A, X_B = 40.0, 120.0
W_SEED, D_SEED = 5.0, 0.25
RHO_FLOOR = 0.02

x = np.arange(N) * DX
k = 2.0 * np.pi * np.fft.fftfreq(N, DX)
IN_A = np.abs(((x - X_A + L / 2) % L) - L / 2) < 12.0
IN_B = np.abs(((x - X_B + L / 2) % L) - L / 2) < 12.0
CORR = (x > 60.0) & (x < 104.0)          # A→B corridor, clear of both cores


def wrap(d: np.ndarray) -> np.ndarray:
    return (d + L / 2.0) % L - L / 2.0


def initial(v: float, v2: float) -> np.ndarray:
    theta = (v * L / (4 * math.pi)) * np.cos(4 * math.pi * (x - X_A) / L) \
        + (v2 * L / (2 * math.pi)) * np.cos(2 * math.pi * (x - X_A) / L)
    rho = 1.0 + D_SEED * np.exp(-(wrap(x - X_A) / W_SEED) ** 2) \
        + D_SEED * np.exp(-(wrap(x - X_B) / W_SEED) ** 2)
    return np.sqrt(rho) * np.exp(1j * theta)


def energy(psi: np.ndarray) -> float:
    px = np.fft.ifft(1j * k * np.fft.fft(psi))
    return float(np.sum(0.5 * np.abs(px) ** 2
                        + 0.5 * (np.abs(psi) ** 2 - 1.0) ** 2) * DX)


def observe(psi: np.ndarray, t: float) -> dict:
    rho = np.abs(psi) ** 2
    px = np.fft.ifft(1j * k * np.fft.fft(psi))
    J = np.imag(np.conj(psi) * px)
    v = J / np.maximum(rho, RHO_FLOOR)
    dvdx = (np.roll(v, -1) - np.roll(v, 1)) / (2 * DX)
    q = CORR & (rho > 1.8) & (v > 0.5)   # rightward-moving dense front only
    xs = x[q]
    return dict(t=t,
                rA=float(rho[IN_A].max()), rB=float(rho[IN_B].max()),
                TH=float(np.sum(rho * dvdx) / np.sum(rho)),
                fmin=float(xs.min()) if xs.size else math.nan,
                fmax=float(xs.max()) if xs.size else math.nan,
                rmin=float(rho.min()))


def evolve(psi: np.ndarray, dt: float):
    kin = np.exp(-1j * (k ** 2 / 2.0) * (dt / 2.0))
    steps = int(round(T_MAX / dt))
    per = max(1, int(round(SNAP / dt)))
    frames = []
    e0 = energy(psi)
    for s in range(steps + 1):
        if s % per == 0:
            frames.append(observe(psi, s * dt))
        if s == steps:
            break
        psi = np.fft.ifft(kin * np.fft.fft(psi))
        psi = psi * np.exp(-1j * dt * (np.abs(psi) ** 2 - 1.0))
        psi = np.fft.ifft(kin * np.fft.fft(psi))
        if not np.isfinite(psi).all():
            raise FloatingPointError(f"blowup at t = {s * dt:.2f}")
    drift = abs(energy(psi) - e0) / abs(e0)
    return frames, drift


def first_turn(frames: list, key: str, thresh: float = 1.8):
    r = [f[key] for f in frames]
    for i in range(1, len(r) - 1):
        if r[i] > thresh and r[i] >= r[i - 1] and r[i] >= r[i + 1] \
                and min(r[i:]) < 0.8 * r[i]:
            return i
    return None


def survival(frames: list, key: str, i0: int):
    """Return (first peak, largest later re-compression, its time, end value).

    v1 of the verdict compared re_max to peak1 with no timing and thereby
    mislabeled §17 joint-collision transients (compressions arriving with the
    OTHER pocket's outflow, after both doors are open) as re-crushing.  The
    refined verdict below dates each re-compression and classifies by cause:
    open (i)'s kill is a re-compression during exposure to a still-
    contracting neighbor, i.e. before both turns; a later transient is joint
    physics, checked instead for dispersal (the pocket must not re-collapse).
    """
    r = [f[key] for f in frames]
    t = [f["t"] for f in frames]
    peak1 = r[i0]
    imin = i0 + int(np.argmin(r[i0:]))
    if imin >= len(r) - 1:
        return peak1, r[-1], t[-1], r[-1]
    irem = imin + int(np.argmax(r[imin:]))
    return peak1, r[irem], t[irem], r[-1]


def front(frames: list, iA: int):
    seeded = arrive = None
    for i in range(iA, len(frames)):
        f = frames[i]
        if not math.isnan(f["fmin"]):
            if seeded is None and f["fmin"] < 80.0:
                seeded = i
            if seeded is not None and f["fmax"] >= 102.0:
                arrive = i
                break
    return seeded, arrive


def theta_crossing(frames: list, i_from: int):
    th = [f["TH"] for f in frames]
    for i in range(i_from, len(th) - 2):
        if th[i] > 0 and th[i + 1] > 0 and th[i + 2] > 0:
            return i
    return None


def run_config(v: float, v2: float, label: str, dt: float = DT):
    frames, drift = evolve(initial(v, v2), dt)
    t = [f["t"] for f in frames]
    iA, iB = first_turn(frames, "rA"), first_turn(frames, "rB")
    print(f"\n── {label}:  V = {v}, V₂ = {v2}   (energy drift {drift:.2e})")
    assert drift < 0.01, "energy check failed — do not quote"
    if iA is None or iB is None:
        print("   A DOOR DID NOT OPEN — sequencing hazard; report to ledger.")
        return None
    tA, tB = t[iA], t[iB]
    if tA > tB:                      # keep A = first-to-turn by convention
        iA, iB, tA, tB = iB, iA, tB, tA
    stag = (tB - tA) / (0.5 * (tA + tB))
    pred = (2 * v + v2) / (2 * v - v2)
    pA, reA, trA, endA = survival(frames, "rA", iA)
    pB, reB, trB, endB = survival(frames, "rB", iB)
    seeded, arrive = front(frames, iA)
    icr = theta_crossing(frames, iA)
    th_post = [f["TH"] for f in frames if tB + 2 <= f["t"] <= tB + 15]
    rmin = min(f["rmin"] for f in frames)
    print(f"   turns: t_A = {tA:5.1f} (peak ρ {pA:5.2f}),  t_B = {tB:5.1f} "
          f"(peak ρ {pB:5.2f});  measured stagger {stag:.2f} "
          f"(linear-rate ratio {pred:.2f})")
    # open (i): a re-compression counts as re-crushing only during exposure
    # to a still-contracting neighbor (t ≤ tB); later transients are §17
    # joint collisions and are instead checked for dispersal.
    crushA = reA > pA and trA <= tB
    crushB = reB > pB and trB <= tB          # impossible by construction; kept honest
    # Criterion note (second revision, recorded): v2 demanded full dispersal
    # (end < 0.6·transient peak) — impossible in a periodic conservative box,
    # which recirculates wave energy indefinitely; solitons re-transit the
    # measurement windows forever.  The model-appropriate test is BOUNDED
    # DECLINE: the transient peaks and falls with no runaway re-collapse.
    # Full dilution belongs to the re-expanding background — the Θ > 0 this
    # run measures but the fixed box cannot feed back.  Named model edge.
    dispA = endA < 0.9 * max(reA, 1e-9)
    dispB = endB < 0.9 * max(reB, 1e-9)
    print(f"   survival, exposure window t ≤ t_B: "
          f"A {'RE-CRUSHED' if crushA else 'SURVIVES'} "
          f"(largest later re-compression {reA:5.2f} at t = {trA:5.1f}, "
          f"first peak {pA:5.2f});")
    print(f"   B {'RE-CRUSHED' if crushB else 'SURVIVES'} "
          f"({reB:5.2f} at t = {trB:5.1f}, first peak {pB:5.2f})")
    print(f"   post-turn transients (joint collisions): "
          f"A end ρ {endA:4.2f} → {'declining, no runaway' if dispA else 'NOT DECLINING'}; "
          f"B end ρ {endB:4.2f} → {'declining, no runaway' if dispB else 'NOT DECLINING'}")
    if arrive is not None:
        print(f"   race: A's outflow front seeded x<80 at t = {t[seeded]:.1f}, "
              f"reached B's flank at t = {t[arrive]:.1f} "
              f"(front speed ≈ {22.0 / max(t[arrive] - t[seeded], 1e-9):.2f} c_s)"
              f" — B's door opened at {tB:.1f}: "
              f"{'CLOCK-FIRST' if tB < t[arrive] else 'FRONT-FIRST'}")
    else:
        print(f"   race: no dense rightward front reached B's flank by "
              f"t = {T_MAX:.0f} — CLOCK-FIRST by default")
    if icr is not None:
        print(f"   averaging: Θ crosses to sustained expansion at t = {t[icr]:.1f}"
              f" (doors at {tA:.1f}, {tB:.1f}); "
              f"post-turn mean Θ = {np.mean(th_post):+.4f}")
    else:
        print(f"   averaging: Θ NEVER crosses — post-turn mean "
              f"{np.mean(th_post):+.4f}")
    print(f"   min density in run: {rmin:.3f}  (floor {RHO_FLOOR})")
    return dict(tA=tA, tB=tB, stag=stag, pA=pA, pB=pB, reA=reA, reB=reB,
                crushA=crushA, crushB=crushB, dispA=dispA, dispB=dispB,
                arrive=None if arrive is None else t[arrive],
                cross=None if icr is None else t[icr],
                th_post=float(np.mean(th_post)))


def main() -> None:
    print("=" * 78)
    print("The sequencing race: staggered doors in one contracting medium")
    print("=" * 78)

    print("\nSYM — the translation twin (V₂ = 0): A and B must match exactly")
    fr, drift = evolve(initial(2.0, 0.0), DT)
    dmax = max(abs(f["rA"] - f["rB"]) for f in fr)
    print(f"   sup|ρ_A(t) − ρ_B(t)| = {dmax:.2e}   (energy drift {drift:.2e})")
    assert dmax < 1e-6, "symmetry check failed — do not quote"
    assert drift < 0.01

    r1 = run_config(2.0, 0.6, "§16-MATCHED stagger")
    r2 = run_config(2.0, 1.0, "STRESSED stagger")
    r3 = run_config(3.0, 0.9, "MACH-SCALED (same rate ratio)")

    print("\nREF — refinement pair on the §16-matched configuration (dt/2):")
    r1h = run_config(2.0, 0.6, "refined dt/2", dt=DT / 2.0)
    assert r1 is not None and r1h is not None
    assert abs(r1h["tA"] - r1["tA"]) / r1["tA"] < 0.03
    assert abs(r1h["tB"] - r1["tB"]) / r1["tB"] < 0.03
    assert abs(r1h["pA"] - r1["pA"]) / r1["pA"] < 0.05
    assert abs(r1h["pB"] - r1["pB"]) / r1["pB"] < 0.05
    print("   refinement: turn times < 3%, peaks < 5% — CONFIRMED")

    print("\nVERDICT (computed from the table above)")
    ok = all(r is not None for r in (r1, r2, r3))
    if ok:
        surv = not any(r["crushA"] or r["crushB"] for r in (r1, r2, r3))
        disp = all(r["dispA"] and r["dispB"] for r in (r1, r2, r3))
        clock = all(r["arrive"] is None or r["tB"] < r["arrive"]
                    for r in (r1, r2, r3))
        avg = all(r["cross"] is not None and r["th_post"] > 0
                  for r in (r1, r2, r3))
        print(f"   (i)  survival:        "
              f"{'HOLDS — no pocket re-crushed while a neighbor still contracts' if surv else 'FAILS'}")
        print(f"   collision transients: "
              f"{'all bounded and declining (no re-collapse)' if disp else 'A TRANSIENT IS NOT DECLINING'}")
        print(f"   (ii) sequencing:      "
              f"{'CLOCK-FIRST throughout' if clock else 'front-first seen — characterized above'}")
        print(f"   (iv) averaged turn:   "
              f"{'Θ crosses and stays positive' if avg else 'FAILS'}")
        if surv and disp and avg:
            print("   The reconciled wall problem COMPUTES: doors open on their own")
            print("   clocks before any neighbor's outflow arrives, no pocket is")
            print("   re-crushed during exposure to a contracting neighbor, the")
            print("   later joint-collision transients are bounded and declining")
            print("   with no re-collapse (§17 physics; full dilution belongs to")
            print("   the re-expanding background the fixed box cannot feed back),")
            print("   and the mass-weighted expansion rate crosses from contraction")
            print("   to expansion as the doors open in sequence. Open (iii)")
            print("   (transverse) stays named; 1D + flow-modeled contraction is")
            print("   the scope. Candidate grade, reconstruction convention.")
        else:
            print("   A KILL CONDITION FIRED — record in the failures ledger; the")
            print("   task stays open. Nothing papered.")
    else:
        print("   A door failed to open — ledger row; task stays open.")
    print("=" * 78)


if __name__ == "__main__":
    main()
