#!/usr/bin/env python3
"""
Fairbank desk adversarial layer (reproducible).

Extends mbb_paper_verify with:
  - NuFIT-class ±1σ one-at-a-time extremes on ceiling / min-NO ceiling
  - m1 scan of floor / ceiling / sum / margin
  - flat-phase prior density + grid-offset sensitivity
  - experiment overlay flags
  - Majoron g_ee order-of-magnitude at surviving v_L points
  - cosmology scaffolding block (booked numbers; not recomputed)

Writes JSON under docs/working_logs/_runs/fairbank_desk_workload_20260810/
unless --out is set.

Run: python3 scripts/fairbank_desk_adversarial.py
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

meV = 1e3

PAPER = dict(s12=0.307, s13=0.022, dm21=7.42e-5, dm31=2.51e-3)
SIG = dict(s12=0.0125, s13=0.00065, dm21=0.21e-5, dm31=0.027e-3)


def masses(m1, p):
    return m1, math.sqrt(m1 * m1 + p["dm21"]), math.sqrt(m1 * m1 + p["dm31"])


def terms(m1, p):
    m = masses(m1, p)
    u = ((1 - p["s12"]) * (1 - p["s13"]), p["s12"] * (1 - p["s13"]), p["s13"])
    return [ui * mi for ui, mi in zip(u, m)]


def window(t):
    hi = sum(t)
    mx = max(t)
    lo = max(0.0, 2 * mx - hi)
    return lo, hi


def prob_grid(t, thr, n, offset=0.0):
    c = 0
    for i in range(n):
        a = 2 * math.pi * (i + 0.5) / n + offset
        for j in range(n):
            b = 2 * math.pi * (j + 0.5) / n + offset
            re = t[0] + t[1] * math.cos(a) + t[2] * math.cos(b)
            im = t[1] * math.sin(a) + t[2] * math.sin(b)
            if math.hypot(re, im) > thr:
                c += 1
    return c / (n * n)


def shift(p, key, sign):
    q = dict(p)
    q[key] = p[key] + sign * SIG[key]
    return q


def build():
    results = {}

    t = terms(2.25e-3, PAPER)
    lo, hi = window(t)
    t0 = terms(0.0, PAPER)
    lo0, hi0 = window(t0)
    results["paper"] = {
        "terms_meV": [x * meV for x in t],
        "window_meV": [lo * meV, hi * meV],
        "sum_meV": sum(masses(2.25e-3, PAPER)) * meV,
        "minNO_window_meV": [lo0 * meV, hi0 * meV],
        "p_above_4p7": prob_grid(t, 4.7e-3, 800),
        "p_band": prob_grid(t, hi0, 800) - prob_grid(t, hi, 800),
        "p_tag": prob_grid(t, 2.35e-3, 800),
        "p_min_tag": prob_grid(t0, 2.35e-3, 800),
    }

    extremes = {}
    for key in ("s12", "s13", "dm21", "dm31"):
        for sign, lab in ((+1, "+1s"), (-1, "-1s")):
            p = shift(PAPER, key, sign)
            t_e = terms(2.25e-3, p)
            lo_e, hi_e = window(t_e)
            t0e = terms(0.0, p)
            _, hi0e = window(t0e)
            extremes[f"{key}_{lab}"] = {
                "ceiling_meV": hi_e * meV,
                "floor_meV": lo_e * meV,
                "minNO_ceiling_meV": hi0e * meV,
                "band_width_meV": (hi_e - hi0e) * meV,
            }
    results["nufit_1sigma_extremes_paper_base"] = extremes
    ceilings = [v["ceiling_meV"] for v in extremes.values()]
    minNO_ceils = [v["minNO_ceiling_meV"] for v in extremes.values()]
    results["ceiling_range_meV"] = [min(ceilings), max(ceilings)]
    results["minNO_ceiling_range_meV"] = [min(minNO_ceils), max(minNO_ceils)]
    results["ceiling_stable"] = (max(ceilings) - min(ceilings)) < 0.25

    scan = []
    for m1_meV in (0.0, 1.0, 2.0, 2.25, 2.3245, 3.0, 5.0, 10.0):
        m1 = m1_meV * 1e-3
        t_s = terms(m1, PAPER)
        lo_s, hi_s = window(t_s)
        scan.append(
            {
                "m1_meV": m1_meV,
                "floor_meV": lo_s * meV,
                "ceiling_meV": hi_s * meV,
                "sum_meV": sum(masses(m1, PAPER)) * meV,
                "margin_meV": (t_s[1] - t_s[0] - t_s[2]) * meV,
            }
        )
    results["m1_scan"] = scan

    priors = {}
    for n in (400, 800, 1200):
        priors[f"flat_n{n}"] = {
            "p_4p7": prob_grid(t, 4.7e-3, n),
            "p_band": prob_grid(t, hi0, n) - prob_grid(t, hi, n),
            "p_tag": prob_grid(t, 2.35e-3, n),
        }
    priors["flat_n800_offset_pi4"] = {
        "p_4p7": prob_grid(t, 4.7e-3, 800, offset=math.pi / 4),
        "p_band": prob_grid(t, hi0, 800, offset=math.pi / 4)
        - prob_grid(t, hi, 800, offset=math.pi / 4),
    }
    results["phase_prior"] = priors

    hi_model = hi * meV
    hi_min = hi0 * meV
    experiments = [
        dict(
            name="nEXO",
            isotope="136Xe",
            reach_lo=4.7,
            reach_hi=20.3,
            note="favourable ME end only — owner-owned number",
        ),
        dict(
            name="LEGEND-1000",
            isotope="76Ge",
            reach_lo=9.0,
            reach_hi=21.0,
            note="entirely above ceiling",
        ),
        dict(
            name="CUPID",
            isotope="100Mo",
            reach_lo=12.0,
            reach_hi=34.0,
            note="entirely above ceiling",
        ),
    ]
    for e in experiments:
        e["overlaps_model"] = e["reach_lo"] <= hi_model
        e["overlaps_discriminating_band"] = (
            e["reach_lo"] < hi_model and e["reach_lo"] > hi_min
        )
        e["reach_entirely_above_ceiling"] = e["reach_lo"] > hi_model
    results["experiments"] = experiments
    results["discriminating_band_meV"] = [hi_min, hi_model]

    mbb_typ = 3.05e-3  # eV
    majoron = {}
    for vL_MeV, label in ((4.18, "MeV-scale"), (1e3, "GeV"), (2.4e6, "2.4 TeV")):
        g = mbb_typ / (vL_MeV * 1e6)
        majoron[label] = {
            "vL_MeV": vL_MeV,
            "g_ee": g,
            "vs_KLZ_limit_1e-5": g / 1e-5,
        }
    results["majoron_gee"] = majoron

    results["cosmology_scaffolding"] = {
        "old_BAO_booked_StageB": {
            "dyad_m_ncdm": "0.0671 ± 0.0583",
            "lcdm_m_ncdm": "0.0192 ± 0.0174",
            "dyad_H0": "70.052 ± 0.716",
            "lcdm_H0": "68.345 ± 0.343",
            "authority": "bbnfix_booking_20260808_005626",
            "evidence": "sample-cov Laplace ΔlnZ ≈ +0.21 (soft modes); not nested",
        },
        "DESI_DR2_booked_StageA": {
            "dyad_m_ncdm": "0.0508 ± 0.0473",
            "lcdm_m_ncdm": "0.0138 ± 0.0128",
            "dyad_H0": "70.299 ± 0.541",
            "lcdm_H0": "68.729 ± 0.250",
            "authority": "desidr2_bbnfix_booking_20260810_053127",
            "evidence": "sample-cov Laplace ΔlnZ ≈ +1.38 (soft); Hessian diagnostic fail",
            "rule": "DO NOT MIX with old-BAO",
        },
        "model_relation_Sigma": (
            "61.35 meV (NOT a discriminator vs 58.8 floor; "
            "~2.6 meV gap vs ~20 meV planned resolution)"
        ),
        "nested": "OPEN — gold DESI-DR2 PolyChord; no bookable nested ΔlnZ",
    }

    p47 = [priors[k]["p_4p7"] for k in priors if "p_4p7" in priors[k]]
    pband = [priors[k]["p_band"] for k in priors if "p_band" in priors[k]]
    results["verdicts"] = {
        "ceiling_stable_under_1sigma_shifts": results["ceiling_stable"],
        "ceiling_span_meV": max(ceilings) - min(ceilings),
        "p_4p7_range": [min(p47), max(p47)],
        "p_band_range": [min(pband), max(pband)],
        "p_4p7_order_stable": (max(p47) - min(p47)) < 0.03,
        "p_band_order_stable": (max(pband) - min(pband)) < 0.05,
    }
    results["verdicts"]["green_light_lab_window"] = (
        results["ceiling_stable"]
        and results["verdicts"]["p_4p7_order_stable"]
        and results["verdicts"]["p_band_order_stable"]
        and max(minNO_ceils) < min(ceilings) - 0.5
    )
    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--out",
        default="docs/working_logs/_runs/fairbank_desk_workload_20260810/adversarial_desk.json",
    )
    args = ap.parse_args()
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    results = build()
    out.write_text(json.dumps(results, indent=2))
    print(json.dumps(results["verdicts"], indent=2))
    print("wrote", out)
    if not results["verdicts"]["green_light_lab_window"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
