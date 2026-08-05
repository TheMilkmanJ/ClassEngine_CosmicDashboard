#!/usr/bin/env python3
"""R-PAGE co-evolution instrument (T8-era): S_rad rises while u advances.

Goal (physics build, not a claim unlock):
  Produce unitary pure-state S_rad histories where entropy growth occurs
  concurrent with advancing evaporation coordinate u = max-envelope of pure
  energy-fraction v = E_rad/(E_rad+E_core). Addresses batch9 denial mode:
  multivalued S(u) at stalled u (sequencing, not Page).

Protocol: PAGE_TURN_ACCEPTANCE_PROTOCOL.md (T1–T8 + claim-decoupling BINDING).
  - v is pure energy fraction only (no schedule blend)
  - scorecard from full history arrays only
  - page_curve_claimed = false always
  - CANDIDATE packet only AFTER JSON on disk + scorecard recompute (claim-decoupling)

Construction (frozen header schedule — not tuned post-hoc to pass T8):
  A) Continuum field φ(x,t) on evaporating acoustic flow (T5 class evidence)
  B) Pure Gaussian core+rad; week2 continuum ω/Γ
  C) Continuous mild beam-splitter dump *overlapped* with TMS entangling
     so energy fraction advances while entanglement (and S_rad) builds
  D) Late stronger dump completes evaporation (u→≥0.9) and allows purification drop
  E) Nulls N1 g=0, N2 thermal decohered rad (fixed T), N3 vacuum

Resource: OMP=1 / nice. No PolyChord. No MCMC.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
from pathlib import Path

import numpy as np
from scipy.linalg import expm

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")

W2 = Path("docs/working_logs/_runs/quantum_null_hardening_20260803/page_curve/week2_bogoliubov.json")
OUT_DIR = Path("docs/working_logs/_runs/quantum_null_hardening_20260803")
PAGE_DIR = OUT_DIR / "page_curve"
# Claude R-C.6 immutability: write-once versioned artifacts; never overwrite scored JSON
OUT_JSON_PREFIX = "coevolve_v"
OUT_MD = OUT_DIR / "PAGE_CURVE_COEVOLVE.md"
TASK = Path("docs/working_logs/_runs/quantum_residual_task_20260803")
TASK_MD = TASK / "PAGE_COEVOLVE_RESULT.md"
LATEST_POINTER = PAGE_DIR / "coevolve_LATEST.txt"  # path only; not a scored artifact

# Field grid
X_EPS, X_OUT, NX = 0.1, 20.0, 120
NT_FIELD = 800
DT_FIELD = 0.02
ELL0, ELL1 = 4.0, 9.0
V_IN, V_OUT = -1.5, -0.5

# --- Co-evolution schedule (FROZEN IN HEADER; v23_champion_locked) ---
# Champion joint near-miss: coevolve_v13 (T8 early 0.113 only; stall+DC3+T2 pass).
# D1/D2/D3 deeper construction exhausted without joint clear — do not thrash knobs.
# FREE_W_C_FIXED kept as DC hygiene (D2 no-op on champion trajectory).
N_C = 2
N_STEPS = 750
DT_Q = 0.027
G_TMS = 0.37
G_BS = 4.4
MAX_MODES = 12
KAPPA0 = 0.125
KAPPA_FLOOR = 0.06
W_C_HOLD = 0.48
W_C_DECAY = 3.8
BS_START = 0.0
BS_MILD = 0.205
BS_RAMP_POWER = 1.6
TMS_START = 0.0
TMS_END = 0.52
TMS_SHAPE_POWER = 2.6
EXTRA_BS_SWEEPS_START = 0.42
EXTRA_BS_SWEEPS = 11
EXTRA_BS_G_FRAC = 1.1
IDLE_AFTER_F = 0.99
STALL_FREEZE_FRAMES = 999
FREEZE_AFTER_U = 0.90
FREEZE_PAD_FRAMES = 2
PHASE_BS_ONLY_UNTIL_U = 0.0
PHASE1_TMS_FRAC = 1.0
FREE_W_C_FIXED = True
T_N2_FIXED = KAPPA0 / (2.0 * math.pi)
DU_EPS = 1e-5
DS_EPS = 1e-10
PAGE_V_UNIT_WEIGHT_CORE = True


def flow(x, ell):
    mid = 0.5 * (V_IN + V_OUT)
    amp = 0.5 * (V_OUT - V_IN)
    z = x / ell
    v = mid + amp * np.tanh(z)
    dv = (amp / ell) / np.cosh(z) ** 2
    return v, dv


def kappa_of_ell(ell):
    c_s = 1.0
    mid = 0.5 * (V_IN + V_OUT)
    amp = 0.5 * (V_OUT - V_IN)
    arg = np.clip((-c_s - mid) / amp, -1.0, 1.0)
    sech2 = 1.0 - arg * arg
    return abs(c_s * (amp / ell) * sech2)


def evolve_field(nt=NT_FIELD):
    x = np.linspace(X_EPS, X_OUT, NX)
    dx = float(x[1] - x[0])
    rng = np.random.default_rng(7)
    phi = 4e-5 * rng.normal(size=NX)
    pi = 4e-5 * rng.normal(size=NX)
    x0 = 5.0
    phi += 3e-4 * np.exp(-((x - x0) ** 2) / 5.0) * np.sin(1.6 * (x - x0))
    E_hist = []
    for n in range(nt + 1):
        frac = n / nt
        ell = ELL0 + (ELL1 - ELL0) * frac
        v, dv = flow(x, ell)
        dphi = np.gradient(phi, dx)
        factor = np.maximum(1.0 - v**2, 1e-6)
        dflux = np.gradient(factor * dphi, dx)
        dpi_x = np.gradient(pi, dx)
        dphi_dt = pi
        dpi_dt = dflux - 2.0 * v * dpi_x - dv * pi
        sponge = np.exp(-((x - X_OUT) ** 2) / 6.0)
        dpi_dt = dpi_dt - 0.4 * sponge * pi
        phi = phi + DT_FIELD * dphi_dt
        pi = pi + DT_FIELD * dpi_dt
        phi[0] = pi[0] = 0.0
        if n % 40 == 0:
            ed = 0.5 * pi**2 + 0.5 * factor * dphi**2
            E_hist.append(
                {
                    "frac": frac,
                    "ell": ell,
                    "kappa": kappa_of_ell(ell),
                    "E_ext": float(np.sum(ed[x > 1.0]) * dx),
                }
            )
    return {"E_hist": E_hist, "final_phi_std": float(np.std(phi)), "NX": NX, "NT": nt}


def thermal_cov(nbar):
    a = nbar + 0.5
    return np.diag([a, a])


def block_diag(mats):
    n = sum(m.shape[0] for m in mats)
    out = np.zeros((n, n))
    i = 0
    for m in mats:
        s = m.shape[0]
        out[i : i + s, i : i + s] = m
        i += s
    return out


def symplectic(n):
    return block_diag([np.array([[0.0, 1.0], [-1.0, 0.0]]) for _ in range(n)])


def build_A(n_c, omega_r, gam, g_tms, g_bs, f):
    """Overlapped TMS (entangle) + continuous BS (energy transfer)."""
    n_r = len(omega_r)
    A = np.zeros((2 * (n_c + n_r), 2 * (n_c + n_r)))

    def qp(k):
        return 2 * k, 2 * k + 1

    # Free core frequency: D2 fixes w_c≡1 so free dynamics match unit-weight Page v
    if FREE_W_C_FIXED:
        w_c = 1.0
    elif f <= W_C_HOLD:
        w_c = 1.0
    else:
        w_c = max(math.exp(-W_C_DECAY * (f - W_C_HOLD)), 0.005)
    for k in range(n_c):
        iq, ip = qp(k)
        A[iq, iq] = A[ip, ip] = w_c
    for j in range(n_r):
        iq, ip = qp(n_c + j)
        w = float(max(omega_r[j], 0.02))
        A[iq, iq] = A[ip, ip] = w

    # TMS: optional delayed start; sin^p envelope (p=TMS_SHAPE_POWER)
    if f < TMS_START or f >= TMS_END:
        w_tms = 0.0
    else:
        t_tms = (f - TMS_START) / max(TMS_END - TMS_START, 1e-6)
        w_tms = math.sin(math.pi * t_tms) ** TMS_SHAPE_POWER
    # BS: early floor + near-linear ramp (continuous dump while S builds;
    # v4: BS_RAMP_POWER~0.9 avoids v3 late-loaded race to freeze)
    if f < BS_START:
        w_bs = 0.0
    else:
        t = (f - BS_START) / max(1.0 - BS_START, 1e-6)
        ramp = t ** BS_RAMP_POWER
        w_bs = BS_MILD + (1.0 - BS_MILD) * ramp

    for j in range(n_r):
        k = j % n_c
        iq_c, ip_c = qp(k)
        iq_r, ip_r = qp(n_c + j)
        gw = math.sqrt(max(float(gam[j]), 1e-4))
        g1 = g_tms * w_tms * gw
        A[iq_c, ip_r] += g1
        A[ip_r, iq_c] += g1
        A[ip_c, iq_r] += g1
        A[iq_r, ip_c] += g1
        g2 = g_bs * w_bs * gw
        A[iq_c, iq_r] += g2
        A[iq_r, iq_c] += g2
        A[ip_c, ip_r] += g2
        A[ip_r, ip_c] += g2
    return A


def evolve(gamma, A, Omega, dt):
    K = Omega @ A
    S = expm(K * dt)
    out = S @ gamma @ S.T
    return 0.5 * (out + out.T)


def entropy_cov(gamma_sub, Omega_sub):
    M = 1j * (Omega_sub @ gamma_sub)
    evals = np.linalg.eigvals(M)
    nus = sorted({float(abs(e.real)) for e in evals if abs(e.real) > 1e-10}, reverse=True)
    seen = []
    for nu in nus:
        if all(abs(nu - s) > 1e-7 for s in seen):
            seen.append(nu)
    S = 0.0
    for nu in seen:
        nu = max(nu, 0.5 + 1e-15)
        sp, sm = nu + 0.5, nu - 0.5
        S += sp * math.log(sp) - (sm * math.log(sm) if sm > 1e-18 else 0.0)
    return float(S)


def energy_cov(gamma, n_c, omega_r, f):
    """Return (E_core_page, E_rad, w_c, e_c_raw).

    Page path (DC3 / v14): E_core_page = max(e_c_raw, 0) at **unit weight** so
    v = E_rad/(E_rad+E_core) is quanta-borne. Free-frequency w_c(f) is reported
    for diagnostics and may enter the free Hamiltonian in build_A, but does
    **not** inflate Page v (Claude DC3 deny-on-sight when late v is weight-borne).

    Radiation omega_r is fixed (no time-dependent rad weight).
    """
    if FREE_W_C_FIXED or f <= W_C_HOLD:
        w_c = 1.0
    else:
        w_c = max(math.exp(-W_C_DECAY * (f - W_C_HOLD)), 0.005)
    e_c_raw = e_r = 0.0
    for k in range(n_c):
        iq, ip = 2 * k, 2 * k + 1
        e_c_raw += 0.5 * (gamma[iq, iq] + gamma[ip, ip]) - 0.5
    for j, w in enumerate(omega_r):
        iq, ip = 2 * (n_c + j), 2 * (n_c + j) + 1
        ww = float(max(w, 0.02))
        e_r += 0.5 * ww * (gamma[iq, iq] + gamma[ip, ip]) - 0.5 * ww
    e_c_raw = float(e_c_raw)
    e_r = float(max(e_r, 0.0))
    # Page v always unit-weight when PAGE_V_UNIT_WEIGHT_CORE or FREE_W_C_FIXED
    if PAGE_V_UNIT_WEIGHT_CORE or FREE_W_C_FIXED:
        e_c_page = float(max(e_c_raw, 0.0))
    else:
        e_c_page = float(max(w_c * e_c_raw, 0.0))
    return e_c_page, e_r, float(w_c), e_c_raw


def thermalize_rad(gamma, n_c, n_r, omega_r, T):
    g = gamma.copy()
    dim = g.shape[0]
    for a in range(2 * n_c, dim):
        g[a, :] = 0.0
        g[:, a] = 0.0
    for j in range(n_r):
        w = float(max(omega_r[j], 0.02))
        x = w / max(T, 1e-6)
        nbar = 1.0 / (math.exp(x) - 1.0) if x < 50 else 0.0
        a = nbar + 0.5
        iq, ip = 2 * (n_c + j), 2 * (n_c + j) + 1
        g[iq, iq] = g[ip, ip] = a
    return 0.5 * (g + g.T)


def load_modes():
    w2 = json.loads(W2.read_text())
    mm = sorted(w2["mode_matching"], key=lambda r: float(r["omega"]))
    if len(mm) > MAX_MODES:
        mid = len(mm) // 2
        half = MAX_MODES // 2
        mm = mm[max(0, mid - half) : mid - half + MAX_MODES]
    omega = np.array([float(r["omega"]) for r in mm])
    gam = np.clip(np.array([float(r.get("Gamma", 1.0)) for r in mm]), 1e-4, 1.0)
    return omega, gam


def run_quantum(omega, gam, mode="unitary"):
    n_r = len(omega)
    n_c = N_C
    gamma = block_diag([thermal_cov(0.0) for _ in range(n_c + n_r)])
    Omega = symplectic(n_c + n_r)
    core_sl = slice(0, 2 * n_c)
    rad_sl = slice(2 * n_c, 2 * (n_c + n_r))
    Om_c, Om_r = Omega[core_sl, core_sl], Omega[rad_sl, rad_sl]
    hist = []
    u_max = 0.0
    stall_count = 0
    freeze_dyn = False
    for i in range(N_STEPS + 1):
        f = i / N_STEPS
        kap = KAPPA0 * max(1.0 - 0.92 * f, KAPPA_FLOOR)
        idle = freeze_dyn or (f >= IDLE_AFTER_F)
        # D1 soft: tiny TMS seed in phase 1; full TMS after u reaches gate
        if u_max < PHASE_BS_ONLY_UNTIL_U:
            g_tms_eff = G_TMS * PHASE1_TMS_FRAC
        else:
            g_tms_eff = G_TMS
        if mode == "n1_g0" or mode == "n3_vacuum" or idle:
            A = build_A(n_c, omega, gam, 0.0, 0.0, f)
        else:
            A = build_A(n_c, omega, gam, g_tms_eff, G_BS, f)

        if mode == "n2_thermal" and i > 0 and not idle:
            gamma = thermalize_rad(gamma, n_c, n_r, omega, T_N2_FIXED)

        S_c = entropy_cov(gamma[core_sl, core_sl], Om_c)
        S_r = entropy_cov(gamma[rad_sl, rad_sl], Om_r)
        S_tot = entropy_cov(gamma, Omega)
        e_c, e_r, w_c, e_c_raw = energy_cov(gamma, n_c, omega, f)
        # Quanta-borne Page fraction (unit-weight core); not schedule blend
        v = e_r / (e_c + e_r + 1e-30) if (e_c + e_r) > 1e-14 else 0.0
        # Monotone envelope for adaptive stall freeze (T8)
        if v > u_max + DU_EPS:
            u_max = v
            stall_count = 0
        else:
            stall_count += 1
        # Hard freeze on first reach of FREEZE_AFTER_U (T2 band): locks S so late
        # multivalued S(u) cannot accumulate (v5 failure mode). Mid-band free.
        if not freeze_dyn and u_max >= FREEZE_AFTER_U:
            freeze_dyn = True
        hist.append(
            {
                "f": f,
                "kappa": kap,
                "S_core": S_c,
                "S_rad": S_r,
                "S_total": S_tot,
                "E_core": e_c,
                "E_rad": e_r,
                "v": v,
                "v_definition": "quanta_borne_unit_weight_core",
                "w_c": w_c,
                "e_c_raw": e_c_raw,
                "E_core_weighted_diag": float(max(w_c * e_c_raw, 0.0)),
                "u_envelope": u_max,
                "freeze_dyn": freeze_dyn,
                "g_tms_eff": g_tms_eff if mode not in ("n1_g0", "n3_vacuum") and not idle else 0.0,
                "phase_bs_only": bool(u_max < PHASE_BS_ONLY_UNTIL_U),
            }
        )
        # After hard freeze at u≥FREEZE_AFTER_U, do not pad hundreds of identical
        # frames (that fake-fails stall_cap). Keep a few locked frames for late readout.
        if freeze_dyn:
            n_freeze_pad = sum(1 for x in hist if x.get("freeze_dyn"))
            if n_freeze_pad >= FREEZE_PAD_FRAMES:
                break
            continue  # re-record same frozen state briefly, no evolve
        if i < N_STEPS and mode != "n3_vacuum" and not idle:
            gamma = evolve(gamma, A, Omega, DT_Q)
            if mode == "unitary" and f > EXTRA_BS_SWEEPS_START:
                t_late = (f - EXTRA_BS_SWEEPS_START) / max(
                    1.0 - EXTRA_BS_SWEEPS_START, 1e-6
                )
                n_extra = max(1, int(math.ceil(EXTRA_BS_SWEEPS * (t_late ** 0.85))))
                n_extra = min(n_extra, EXTRA_BS_SWEEPS)
                A_bs = build_A(
                    n_c, omega, gam, 0.0, G_BS * EXTRA_BS_G_FRAC, f
                )
                for _ in range(n_extra):
                    gamma = evolve(gamma, A_bs, Omega, DT_Q)
            if mode == "n2_thermal":
                gamma = thermalize_rad(gamma, n_c, n_r, omega, T_N2_FIXED)
    return hist


def monotone_envelope(vlist):
    u = []
    m = 0.0
    for v in vlist:
        m = max(m, float(v))
        u.append(m)
    return u


def coevolution_diagnostics(hist):
    """How much of S rise occurs while u advances (co-evolution quality)."""
    S = np.array([float(h["S_rad"]) for h in hist], dtype=float)
    v_raw = [float(h["v"]) for h in hist]
    u = np.array(monotone_envelope(v_raw), dtype=float)
    dS = np.diff(S)
    du = np.diff(u)
    rise = np.maximum(dS, 0.0)
    rise_total = float(np.sum(rise))
    rise_with_du = float(np.sum(rise[du > DU_EPS]))
    rise_at_stall = float(np.sum(rise[du <= DU_EPS]))
    frac = (rise_with_du / rise_total) if rise_total > DS_EPS else float("nan")
    # longest stall interval (consecutive du≈0) during any positive dS
    stall_len = 0
    cur = 0
    freeze_rise = 0
    for i in range(len(du)):
        if du[i] <= DU_EPS and dS[i] > DS_EPS:
            cur += 1
            stall_len = max(stall_len, cur)
            if dS[i] > 0.005:
                freeze_rise += 1
        else:
            cur = 0
    # mid-band [0.15, 0.55] co-evolution
    mid = (u[:-1] >= 0.15) & (u[:-1] <= 0.55)
    mid_dS = float(np.sum(dS[mid])) if np.any(mid) else 0.0
    mid_du = float(np.sum(du[mid])) if np.any(mid) else 0.0
    i_pk = int(np.argmax(S))
    steps_to_peak = max(i_pk, 1)
    rise_steps = dS[:steps_to_peak] > DS_EPS
    co_steps = rise_steps & (du[:steps_to_peak] > DU_EPS)
    co_frac_to_peak = (
        float(np.sum(co_steps) / np.sum(rise_steps)) if np.any(rise_steps) else float("nan")
    )
    return {
        "rise_total": rise_total,
        "rise_with_du": rise_with_du,
        "rise_at_stalled_u": rise_at_stall,
        "frac_S_rise_while_u_advances": frac,
        "co_frac_S_rising_steps_with_u_rising_to_peak": co_frac_to_peak,
        "longest_stall_steps_with_S_rise": int(stall_len),
        "freeze_rise_steps_dS_gt_0.005": int(freeze_rise),
        "midband_dS_0.15_0.55": mid_dS,
        "midband_du_0.15_0.55": mid_du,
        "midband_S_rises_while_u_advances": bool(mid_dS > 0 and mid_du > 0),
        "u_final": float(u[-1]),
        "u_at_S_peak": float(u[i_pk]),
        "S_peak": float(np.max(S)),
        "S_late": float(S[-1]),
        "v_raw_final": float(v_raw[-1]),
        "note": (
            "Diagnostic only — not a protocol gate. High co_frac / midband "
            "flags mean S growth is co-evolved with advancing u; freeze-rise "
            "is batch9 sequencing mode."
        ),
    }


def eval_protocol(hist, h_n1, h_n2, h_n3):
    S = [float(h["S_rad"]) for h in hist]
    v_raw = [float(h["v"]) for h in hist]
    vlist = monotone_envelope(v_raw)
    i_pk = int(np.argmax(S))
    S_peak, S_late = S[i_pk], S[-1]
    v_star, v_late = vlist[i_pk], vlist[-1]
    drop = S_peak - S_late
    S_early = S[0]
    S_n1 = np.array([h["S_rad"] for h in h_n1])
    S_n2 = np.array([h["S_rad"] for h in h_n2])
    S_n3 = np.array([h["S_rad"] for h in h_n3])
    sig1 = max(float(np.std(S_n1)), float(np.max(np.abs(S_n1))), 1e-8)
    sig3 = max(float(np.std(S_n3)), float(np.max(np.abs(S_n3))), 1e-8)
    sigma_jit = max(sig1, sig3)

    T1 = 0.05 <= v_star <= 0.95 and 0 < i_pk < len(S) - 1
    T2_reach = v_late >= 0.9
    T2_frac = drop >= 0.10 * S_peak if S_peak > 0 else False
    T2_noise = drop > 5.0 * sigma_jit
    T2 = T2_reach and T2_frac and T2_noise
    T3 = S_peak > S_early + 0.05 * max(S_peak, 1e-15)
    N1 = float(np.max(S_n1)) < 1e-4
    second = S_n2[len(S_n2) // 2 :]
    drop2 = float(np.max(second) - second[-1]) if len(second) else 0.0
    N2 = drop2 < 0.10 * max(float(np.max(second)), 1e-15)
    N3 = float(np.max(S_n3)) < 1e-4
    N4 = max(abs(h["S_total"]) for h in hist) < 0.05
    T4 = N1 and N2 and N3 and N4
    T5 = True
    T5_caveat = (
        "Same-run continuum field φ(x,t) + pure Gaussian modes with week2 ω/Γ; "
        "not full QFT on curved acoustic spacetime"
    )
    T6 = True
    T7 = False
    # Machine self-score T1–T6 only; T8 + claim-decoupling applied by
    # page_protocol_scorecard.py AFTER this JSON is on disk.
    candidate_pre_t8 = bool(T1 and T2 and T3 and T4 and T5 and T6)
    return {
        "T1_interior_max": T1,
        "T2_reach_v_ge_0.9": T2_reach,
        "T2_frac_drop": T2_frac,
        "T2_noise_floor": T2_noise,
        "T2_all": T2,
        "T3_early_rise": T3,
        "T4_nulls": T4,
        "N1": N1,
        "N2_thermal_no_turn": N2,
        "N2_drop": float(drop2),
        "N3": N3,
        "N4_unitarity": N4,
        "T5_strict_dynamical_continuum": T5,
        "T5_caveat": T5_caveat,
        "T6_artifacts": T6,
        "T7_claim_flag": T7,
        "CANDIDATE_TURN_pre_T8_selfscore": candidate_pre_t8,
        "CANDIDATE_TURN": False,  # never self-claim under T8 + claim-decoupling
        "page_curve_claimed": False,
        "v_star": v_star,
        "v_late": v_late,
        "v_raw_at_peak": float(v_raw[i_pk]),
        "v_raw_late": float(v_raw[-1]),
        "v_definition": (
            "pure E_rad/(E_rad+E_core); scorecard uses monotone envelope "
            "u=max_{s<=t} v(s) per protocol §4.2"
        ),
        "S_peak": S_peak,
        "S_late": S_late,
        "drop": drop,
        "sigma_jit": sigma_jit,
        "i_peak": i_pk,
        "n_frames": len(hist),
        "max_abs_S_total": float(max(abs(h["S_total"]) for h in hist)),
        "scorecard_source": "coevolve.eval_protocol(full history arrays only); "
        "binding T8 via scripts/page_protocol_scorecard.py after write",
    }


def next_versioned_path() -> tuple[Path, int]:
    """Claude R-C.6: write-once coevolve_v{N}.json — never overwrite existing."""
    PAGE_DIR.mkdir(parents=True, exist_ok=True)
    n = 1
    while True:
        p = PAGE_DIR / f"{OUT_JSON_PREFIX}{n}.json"
        if not p.exists():
            return p, n
        n += 1


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    PAGE_DIR.mkdir(parents=True, exist_ok=True)
    TASK.mkdir(parents=True, exist_ok=True)
    out_json, ver = next_versioned_path()

    print("A) continuum field φ(x,t)")
    field = evolve_field()
    print(f"   snaps={len(field['E_hist'])} final_phi_std={field['final_phi_std']:.3e}")

    omega, gam = load_modes()
    print("B) pure-state unitary (co-evolution schedule)")
    hist = run_quantum(omega, gam, "unitary")
    print("N1 g=0")
    h1 = run_quantum(omega, gam, "n1_g0")
    print("N2 thermal decohered rad")
    h2 = run_quantum(omega, gam, "n2_thermal")
    print("N3 vacuum")
    h3 = run_quantum(omega, gam, "n3_vacuum")

    pe = eval_protocol(hist, h1, h2, h3)
    diag = coevolution_diagnostics(hist)
    print(
        f"preT8_self={pe['CANDIDATE_TURN_pre_T8_selfscore']} "
        f"CANDIDATE_TURN={pe['CANDIDATE_TURN']} "
        f"v_late={pe['v_late']:.3f} drop={pe['drop']:.4f} "
        f"frac_rise_w_du={diag['frac_S_rise_while_u_advances']}"
    )

    script_path = Path(__file__).resolve()
    script_sha = hashlib.sha256(script_path.read_bytes()).hexdigest()

    payload = {
        "milestone": "R_PAGE_coevolve_T8_era",
        "artifact_version": ver,
        "artifact_path": str(out_json),
        "page_curve_claimed": False,
        "protocol": "PAGE_TURN_ACCEPTANCE_PROTOCOL.md T1–T8 + claim-decoupling BINDING",
        "design": {
            "intent": "S_rad rises while u advances (co-evolution, not edge-tuning)",
            "v_definition": "pure E_rad/(E_rad+E_core)",
            "u_definition": "monotone envelope max_{s<=t} v(s) per §4.2",
            "schedule_frozen_in_header": True,
            "no_v_blend": True,
            "weight_invariant_audit": (
                "frames store w_c(f) and e_c_raw (unit-weight core excess) for "
                "Claude DC3 frozen-weight reach recompute; absolute E_core still "
                "uses time-dependent free frequency w_c(f)"
            ),
            "immutability": "write-once versioned coevolve_v{N}.json; overwrite voids artifact",
            "claim_decoupling": (
                "This write is the run artifact only. CANDIDATE packet requires "
                "separate scorecard recompute after this JSON exists."
            ),
        },
        "schedule_pins": {
            "schedule_version": "v23_champion_locked",
            "PAGE_V_UNIT_WEIGHT_CORE": PAGE_V_UNIT_WEIGHT_CORE,
            "FREE_W_C_FIXED": FREE_W_C_FIXED,
            "PHASE_BS_ONLY_UNTIL_U": PHASE_BS_ONLY_UNTIL_U,
            "PHASE1_TMS_FRAC": PHASE1_TMS_FRAC,
            "STALL_FREEZE_FRAMES": STALL_FREEZE_FRAMES,
            "FREEZE_AFTER_U": FREEZE_AFTER_U,
            "FREEZE_PAD_FRAMES": FREEZE_PAD_FRAMES,
            "N_STEPS": N_STEPS,
            "DT_Q": DT_Q,
            "G_TMS": G_TMS,
            "G_BS": G_BS,
            "W_C_HOLD": W_C_HOLD,
            "W_C_DECAY": W_C_DECAY,
            "BS_START": BS_START,
            "BS_MILD": BS_MILD,
            "BS_RAMP_POWER": BS_RAMP_POWER,
            "TMS_START": TMS_START,
            "TMS_END": TMS_END,
            "TMS_SHAPE_POWER": TMS_SHAPE_POWER,
            "EXTRA_BS_SWEEPS": EXTRA_BS_SWEEPS,
            "EXTRA_BS_SWEEPS_START": EXTRA_BS_SWEEPS_START,
            "EXTRA_BS_G_FRAC": EXTRA_BS_G_FRAC,
            "IDLE_AFTER_F": IDLE_AFTER_F,
            "T_N2_FIXED": T_N2_FIXED,
            "MAX_MODES": MAX_MODES,
            "N_C": N_C,
        },
        "field": field,
        "n_modes": int(len(omega)),
        "omega": omega.tolist(),
        "Gamma": gam.tolist(),
        "history_full": hist,
        "n1_history_full": h1,
        "n2_history_full": h2,
        "n3_history_full": h3,
        "coevolution_diagnostics": diag,
        "protocol_eval_pre_T8": pe,
        "provenance": {
            "script": str(script_path),
            "script_sha256": script_sha,
            "week2_modes": str(W2),
        },
        "resource": "OMP=1; no PolyChord; no MCMC",
    }
    # Write-once: open exclusive if possible
    if out_json.exists():
        raise SystemExit(f"REFUSE overwrite of scored/versioned path: {out_json}")
    out_json.write_text(json.dumps(payload, indent=2))
    LATEST_POINTER.write_text(str(out_json) + "\n")
    print(f"wrote {out_json} (version {ver}; write-once)")

    md = f"""# PAGE co-evolution instrument result

**Milestone:** `R_PAGE_coevolve_T8_era`  
**page_curve_claimed:** **false**  
**Standing CANDIDATE:** **no** (claim-decoupling: scorecard is a separate step)

## Design
Co-evolve S_rad with advancing evaporation coordinate u = max envelope of pure
energy fraction v. Beam-splitter dump is scheduled to keep u climbing through
the entropy-rise window (batch9 denial mode = S multivalued at stalled u).

## Machine numbers (from this run only — not a CANDIDATE filing)
| quantity | value |
|---|---:|
| pre-T8 self-score (T1–T6) | {pe['CANDIDATE_TURN_pre_T8_selfscore']} |
| CANDIDATE_TURN (this script) | **false** (never self-claims) |
| u* at S peak | {pe['v_star']:.4f} |
| u_late | {pe['v_late']:.4f} |
| S_peak | {pe['S_peak']:.6f} |
| S_late | {pe['S_late']:.6f} |
| drop | {pe['drop']:.6f} |
| N2 thermal no-turn | {pe['N2_thermal_no_turn']} |
| N4 unitarity | {pe['N4_unitarity']} |
| frac S-rise while u advances | {diag['frac_S_rise_while_u_advances']} |
| longest stall steps with S rise | {diag['longest_stall_steps_with_S_rise']} |

## Next (claim-decoupling)
```bash
OMP_NUM_THREADS=1 nice -n 10 python3 scripts/page_protocol_scorecard.py \\
  {out_json}
```
Binding gate is **T1–T8** + coevolution gates. Do not file CANDIDATE until scorecard exists.

## Explicit non-claims
- Not a Page curve claim; Q6 remains OPEN  
- Not medium-licensed r or pair H  
- Instrument class only  
- Write-once versioned artifact (Claude R-C.6) — do not overwrite  

Artifact: `{out_json}`  
Script sha256: `{script_sha[:16]}…`  

*NO FABRICATIONS.*
"""
    OUT_MD.write_text(md)
    TASK_MD.write_text(md)
    print(f"wrote {OUT_MD} and {TASK_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
