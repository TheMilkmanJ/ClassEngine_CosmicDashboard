#!/usr/bin/env python3
"""Week-3 Page-curve *skeleton*: finite-core Gaussian state + toy radiation coupling.

Plan: docs/working_logs/_runs/quantum_null_hardening_20260803/PAGE_CURVE_IMPLEMENTATION_PLAN.md
      Week 3 — evaporation schedule / first S_rad(v) *attempt* (Milestone C start)

What this script DOES:
  - Finite core: N_c harmonic modes as a pure Gaussian covariance state
  - Exterior: N_r thermal-like oscillators seeded from week1 T_H bookkeeping
  - Toy bilinear core↔rad coupling; symplectic (Gaussian) evolution
  - Record S_core, S_rad (von Neumann from covariance eigenvalues) vs energy fraction v
  - Write JSON + markdown with HARD NON-CLAIMS

What this script does NOT do (do not over-claim):
  - Honest sonic-horizon mode continuum from week2 ODE  (proxy modes only)
  - Self-consistent GP evaporation / running κ(E)
  - A claimed Page *turn* as a PRTOE result (may be absent; report honestly)
  - Toy 4v(1−v) ansatz as physics (forbidden)
  - Closing Q6 / information paradox

NO FABRICATIONS. Exit 0 if instrument runs; grade Page-turn separately.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

OUT_DIR = Path("docs/working_logs/_runs/quantum_null_hardening_20260803")
OUT_JSON = OUT_DIR / "page_curve" / "week3_core_skeleton.json"
OUT_MD = OUT_DIR / "PAGE_CURVE_WEEK3.md"

# Week1 bookkeeping defaults (healing units)
KAPPA = 0.125
T_H = KAPPA / (2.0 * math.pi)

# MVP sizes (pre-registered small so exact Gaussian evolution is cheap)
N_C = 4   # core modes
N_R = 8   # radiation modes
N_STEPS = 80
DT = 0.05
G_COUPLE = 0.08  # bilinear strength (toy)


def thermal_cov_1mode(nbar: float) -> np.ndarray:
    """2x2 covariance for one thermal oscillator in (q,p) with ħ=1, ω=1.
    Pure vacuum: nbar=0 → diag(1/2,1/2). Thermal: (n+1/2) I.
    """
    a = nbar + 0.5
    return np.diag([a, a])


def block_diag(mats: list[np.ndarray]) -> np.ndarray:
    n = sum(m.shape[0] for m in mats)
    out = np.zeros((n, n), dtype=float)
    i = 0
    for m in mats:
        s = m.shape[0]
        out[i : i + s, i : i + s] = m
        i += s
    return out


def symplectic_form(n_modes: int) -> np.ndarray:
    """Ω = ⊕_k [[0,1],[-1,0]] for n_modes oscillators."""
    blocks = [np.array([[0.0, 1.0], [-1.0, 0.0]]) for _ in range(n_modes)]
    return block_diag(blocks)


def hamiltonian_matrix(n_c: int, n_r: int, g: float, omega_r: np.ndarray) -> np.ndarray:
    """Quadratic Hamiltonian matrix A such that H = (1/2) ξ^T A ξ in (q,p) basis.
    Core free: ω=1 each. Rad free: omega_r[k]. Coupling: g (q_c0 q_r0 + p_c0 p_r0) style
    on first core and first few rad modes (toy).
    """
    n = n_c + n_r
    dim = 2 * n
    A = np.zeros((dim, dim), dtype=float)

    def qp(k: int) -> tuple[int, int]:
        return 2 * k, 2 * k + 1

    # free core
    for k in range(n_c):
        iq, ip = qp(k)
        A[iq, iq] = 1.0
        A[ip, ip] = 1.0
    # free rad
    for j in range(n_r):
        iq, ip = qp(n_c + j)
        w = float(omega_r[j])
        A[iq, iq] = w
        A[ip, ip] = w
    # toy coupling core0 ↔ rad modes (pair creation–ish: q_c p_r - p_c q_r terms weak)
    iq_c, ip_c = qp(0)
    for j in range(min(3, n_r)):
        iq_r, ip_r = qp(n_c + j)
        # g (q_c q_r + p_c p_r)
        A[iq_c, iq_r] += g
        A[iq_r, iq_c] += g
        A[ip_c, ip_r] += g
        A[ip_r, ip_c] += g
    return A


def evolve_cov(gamma: np.ndarray, A: np.ndarray, Omega: np.ndarray, dt: float) -> np.ndarray:
    """γ' = Ω A γ + γ (Ω A)^T  (Heisenberg for quadratic H).
    One Euler–Heun step for stability at small dt.
    """
    K = Omega @ A
    def f(G):
        return K @ G + G @ K.T
    k1 = f(gamma)
    k2 = f(gamma + dt * k1)
    return gamma + 0.5 * dt * (k1 + k2)


def entropy_from_cov(gamma_sub: np.ndarray, Omega_sub: np.ndarray) -> float:
    """Von Neumann entropy of Gaussian state from symplectic eigenvalues.
    Solve iΩγ v = ν v → ν_j ≥ 1/2; S = sum s(ν) with s(ν)=(ν+1/2)ln(ν+1/2)-(ν-1/2)ln(ν-1/2).
    """
    # symplectic eigenvalues from |i Ω γ|
    M = 1j * (Omega_sub @ gamma_sub)
    evals = np.linalg.eigvals(M)
    # pair ±ν; take positive real parts
    nus = sorted({float(abs(e.real)) for e in evals if abs(e.real) > 1e-9}, reverse=True)
    # keep one per pair (unique positives)
    seen = []
    for nu in nus:
        if all(abs(nu - s) > 1e-6 for s in seen):
            seen.append(nu)
    S = 0.0
    for nu in seen:
        nu = max(nu, 0.5 + 1e-12)
        sp = nu + 0.5
        sm = nu - 0.5
        S += sp * math.log(sp) - (sm * math.log(sm) if sm > 1e-15 else 0.0)
    return float(S)


def energy_proxy(gamma: np.ndarray, n_c: int, n_r: int, omega_r: np.ndarray) -> tuple[float, float]:
    """Rough energy ~ sum ω (⟨q²⟩+⟨p²⟩)/2 - vacuum."""
    e_c = 0.0
    e_r = 0.0
    for k in range(n_c):
        iq, ip = 2 * k, 2 * k + 1
        e_c += 0.5 * (gamma[iq, iq] + gamma[ip, ip]) - 0.5
    for j in range(n_r):
        iq, ip = 2 * (n_c + j), 2 * (n_c + j) + 1
        w = float(omega_r[j])
        e_r += 0.5 * w * (gamma[iq, iq] + gamma[ip, ip]) - 0.5 * w
    return float(max(e_c, 0.0)), float(max(e_r, 0.0))


def _reattach_nulls_section() -> None:
    """If week3_nulls.json exists, append §5 null table so baseline re-run keeps P1."""
    nulls_json = OUT_DIR / "page_curve" / "week3_nulls.json"
    if not nulls_json.is_file() or not OUT_MD.is_file():
        return
    try:
        data = json.loads(nulls_json.read_text())
    except Exception:
        return
    grades = data.get("grades") or {}
    nulls = data.get("nulls") or {}
    if not grades or not nulls:
        return

    def pf(ok: bool) -> str:
        return "PASS" if ok else "FAIL"

    def fnum(d, key, fmt):
        v = d.get(key, None)
        if v is None:
            return "n/a"
        try:
            return format(float(v), fmt)
        except Exception:
            return str(v)

    ga = grades.get("null_A_g0", {})
    gb = grades.get("null_B_infinite_bath", {})
    gc = grades.get("null_C_vacuum", {})
    a = nulls.get("null_A_g0", {})
    b = nulls.get("null_B_infinite_bath", {})
    c = nulls.get("null_C_vacuum", {})
    stamp = data.get("stamp_utc", "see week3_nulls.json")
    block = f"""
## 5. Null suite (P1 — instrument behavior)

**Script:** `scripts/quantum_page_week3_nulls.py`  
**JSON:** `page_curve/week3_nulls.json`  
**Detail report:** `docs/working_logs/_runs/derivation_sprint_20260803/P1_PAGE_NULLS.md`  
**Stamp:** {stamp}  
**page_curve_claimed:** **false**

| null | setup | instrument grade | key numbers |
|---|---|---|---|
| **A** | g=0 (no coupling) | **{pf(bool(ga.get("pass")))}** | max|ΔS_rad|={fnum(a, "max_abs_delta_S_rad", ".3e")} |
| **B** | infinite-bath proxy (rad re-thermalized each step) | **{pf(bool(gb.get("pass")))}** | late_drop={b.get("late_drop_after_peak")}; S0={fnum(b, "S_rad_0", ".6f")}; late={fnum(b, "S_rad_late", ".6f")} |
| **C** | pure vacuum everywhere | **{pf(bool(gc.get("pass")))}** | S0={fnum(c, "S_rad_0", ".3e")}; peak={fnum(c, "S_rad_peak", ".3e")} |

**Interpretation (instrument only):**
- Null A: instrument does not invent S_rad growth without coupling.
- Null B: infinite bath must **not** show purification-style late drop we would call Page.
- Null C: vacuum seed does not fabricate a thermal Page-scale S_rad curve.
- Baseline `late_drop` (if any) remains **curiosity** — **not** a Page-turn claim.

**Recompute nulls:**
```bash
python3 scripts/quantum_page_week3_nulls.py
```
"""
    text_md = OUT_MD.read_text()
    cut = len(text_md)
    for m in (
        "\n## 5. Null suite (P1",
        "\n## 5. Null control",
        "\n## 5. Null",
    ):
        i = text_md.find(m)
        if i != -1:
            cut = min(cut, i)
    OUT_MD.write_text(text_md[:cut].rstrip() + "\n" + block)



def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "page_curve").mkdir(parents=True, exist_ok=True)

    # Radiation frequencies ~ few × T_H band
    omega_r = np.array([0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0, 8.0])[:N_R] * T_H * 10.0
    omega_r = np.maximum(omega_r, 0.05)

    # Initial: core cold (near vacuum); rad slightly warm at T_H occupations
    core_mats = [thermal_cov_1mode(0.0) for _ in range(N_C)]
    rad_mats = []
    for w in omega_r:
        nbar = 1.0 / (math.exp(w / T_H) - 1.0) if w / T_H < 50 else 0.0
        # start colder than pure Hawking to allow growth under coupling
        rad_mats.append(thermal_cov_1mode(0.15 * nbar))
    gamma = block_diag(core_mats + rad_mats)
    Omega = symplectic_form(N_C + N_R)
    A = hamiltonian_matrix(N_C, N_R, G_COUPLE, omega_r)

    # Index slices
    core_idx = slice(0, 2 * N_C)
    rad_idx = slice(2 * N_C, 2 * (N_C + N_R))
    Omega_c = Omega[core_idx, core_idx]
    Omega_r = Omega[rad_idx, rad_idx]

    e_c0, e_r0 = energy_proxy(gamma, N_C, N_R, omega_r)
    e_tot0 = e_c0 + e_r0 + 1e-15

    history = []
    S_rad_vals = []
    for step in range(N_STEPS + 1):
        t = step * DT
        g_c = gamma[core_idx, core_idx]
        g_r = gamma[rad_idx, rad_idx]
        S_c = entropy_from_cov(g_c, Omega_c)
        S_r = entropy_from_cov(g_r, Omega_r)
        e_c, e_r = energy_proxy(gamma, N_C, N_R, omega_r)
        v = e_r / (e_c + e_r + 1e-15)
        history.append(
            {
                "t": t,
                "S_core": S_c,
                "S_rad": S_r,
                "S_sum": S_c + S_r,
                "E_core": e_c,
                "E_rad": e_r,
                "v": v,
            }
        )
        S_rad_vals.append(S_r)
        if step < N_STEPS:
            gamma = evolve_cov(gamma, A, Omega, DT)
            # keep symmetric
            gamma = 0.5 * (gamma + gamma.T)

    S_arr = np.array(S_rad_vals)
    # Peak finder — report only; do NOT claim Page physics
    peak_i = int(np.argmax(S_arr))
    peak_v = history[peak_i]["v"]
    peak_S = float(S_arr[peak_i])
    late_S = float(S_arr[-1])
    has_late_drop = late_S < peak_S - 1e-6 and peak_i < len(S_arr) - 5

    result = {
        "milestone": "C_week3_core_skeleton",
        "claim_grade": "instrument_skeleton_only",
        "page_curve_claimed": False,
        "S_rad_v_is_physical_page": False,
        "units": "toy Gaussian (not healing continuum)",
        "week1_T_H_used": T_H,
        "week1_kappa_used": KAPPA,
        "N_c": N_C,
        "N_r": N_R,
        "g_couple": G_COUPLE,
        "n_steps": N_STEPS,
        "dt": DT,
        "history": history,
        "peak": {
            "index": peak_i,
            "v": peak_v,
            "S_rad": peak_S,
            "late_S_rad": late_S,
            "late_drop_after_peak": has_late_drop,
        },
        "non_claims": [
            "NOT a PRTOE Page-curve result",
            "NOT continuum sonic-horizon modes (week2 ODE not coupled here)",
            "NOT self-consistent evaporation",
            "Toy bilinear coupling only",
            "Any late drop is instrument curiosity until null suite (P1) + week4 hardening",
        ],
    }
    result["page_curve_claimed"] = False
    OUT_JSON.write_text(json.dumps(result, indent=2))

    md = f"""# Page-curve Week 3 — finite-core skeleton (2026-08-03)

**Status:** WEEK3 SKELETON ONLY — first dynamics attempt after A4 parked.  
**Page curve:** **NOT claimed as PRTOE result.** (`page_curve_claimed: false`)  
**Script:** `scripts/quantum_page_core_skeleton_week3.py`  
**JSON:** `page_curve/week3_core_skeleton.json`  
**Null suite:** `scripts/quantum_page_week3_nulls.py` · `page_curve/week3_nulls.json` · P1 report  
**Plan:** `PAGE_CURVE_IMPLEMENTATION_PLAN.md` Milestone C start.

---

## 1. What was done

1. Finite core: **N_c={N_C}** Gaussian oscillators (covariance state).  
2. Exterior: **N_r={N_R}** modes with toy thermal seed from week1 **T_H={T_H:.6f}**.  
3. Bilinear core↔rad coupling (g={G_COUPLE}); symplectic Euler–Heun evolution.  
4. Recorded **S_core(t), S_rad(t), v(t)** (energy fraction proxy).

## 2. Instrument numbers (not a booking)

| quantity | value |
|---|---:|
| peak S_rad | {peak_S:.6f} |
| v at peak | {peak_v:.6f} |
| late S_rad | {late_S:.6f} |
| late drop after peak? | {has_late_drop} |

If `late_drop` is true, it is an **instrument curiosity** until nulls + week4 hardening — **not** a Page-turn claim.

## 3. Explicit non-claims

| object | status |
|---|---|
| Dynamical Page curve as PRTOE result | **OPEN / not claimed** |
| Continuum sonic-horizon modes | not coupled (week2 separate) |
| Self-consistent κ(E) evaporation | not done |
| Q6 ledger close | **forbidden** without week4 hardening |

## 4. Next

- Larger N_c / better coupling to week2 greybody modes  
- Null suite: run `python3 scripts/quantum_page_week3_nulls.py` (P1) — instrument only  
- Only then consider grade DYNAMICS-PASS/FAIL/INCONCLUSIVE

---

**Recompute:**
```bash
python3 scripts/quantum_page_core_skeleton_week3.py
python3 scripts/quantum_page_week3_nulls.py
```
"""
    OUT_MD.write_text(md)
    # Re-attach null table from prior nulls JSON if present (week3 alone must not erase P1)
    _reattach_nulls_section()
    print(md)
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(
        "WEEK3 SKELETON DONE — Page NOT claimed; "
        f"peak_S={peak_S:.4f} late_drop={has_late_drop}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
