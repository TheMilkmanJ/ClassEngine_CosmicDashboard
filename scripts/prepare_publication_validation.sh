#!/usr/bin/env bash
# Publication validation checklist — prints steps only; does NOT compile or run tests.
#
# Usage: ./scripts/prepare_publication_validation.sh

set -euo pipefail

cat <<'EOF'
=== PRTOE Publication Validation Checklist (prepare only) ===

LANE KEY (do not mix):
  CURRENT_CORE  = use_dcdf + screened/derived varying_me + dcdf_dyad_link
                  → python3 validate_dcdf.py ; production YAMLs with use_dcdf: yes
  LEGACY_ST     = use_prtoe + xi/zeta/β/… (v1–v3 scalar-tensor, comparison only)
                  → scripts/test_legacy_st_null_limit.py (shim: test_prtoe_null_limit.py)
                  → docs/historical_v1-v3_scalar_tensor/

Phase 1 — Build (run manually when ready)
  [ ] make -j4
  [ ] cd python && python3 setup.py build
  [ ] ./scripts/install_des_y3.sh   # DES Y3 CosmoLike (not CLASS)

Phase 2a — CURRENT_CORE physics gates (public expansion core)
  [ ] python3 validate_dcdf.py                  # use_dcdf null/identity + tier tests
  [ ] cobaya dry-run / chains using use_dcdf: yes (not use_prtoe)

Phase 2b — LEGACY_ST comparison gates (historical; not current-core claims)
  [ ] ./class test_lambda_cdm.ini
  [ ] ./class test_prtoe_null_simple.ini        # LEGACY_ST if present
  [ ] ./class test_prtoe_null_publication.ini   # LEGACY_ST null ini (if present)
  [ ] python3 scripts/test_legacy_st_null_limit.py  # LEGACY_ST use_prtoe null; P(k)/C_l < 2%
  [ ] python3 scripts/test_local_gravity.py     # LEGACY_ST local-gravity map
  [ ] ./class test_prtoe_unified_full.ini       # LEGACY_ST-era unified smoke if present
  [ ] Verify fifth-force: init abort if |dG/G| > 1e-5 at solar/Earth densities

Phase 2c — LEGACY_ST ablations (after LEGACY_ST null passes)
  [ ] ./class test_prtoe_ablation_xi_only.ini
  [ ] ./class test_prtoe_ablation_no_screening.ini
  [ ] ./class test_prtoe_ablation_unified_dm.ini

Phase 3 — Cobaya likelihood dry-run
  [ ] python3 scripts/verify_full_cosmo_likelihoods.py
  [ ] cobaya-run chains/lcdm_full_cosmo.yaml --test
  [ ] cobaya-run chains/prtoe_full_cosmo.yaml --test   # confirm which flag: use_dcdf vs use_prtoe

Phase 4 — Evidence (last)
  [ ] Matched PolyChord: chains/lcdm_full_cosmo + chains/prtoe_full_cosmo
  [ ] Compare Delta log Z, H0, S8 posteriors

Configs:
  Production CURRENT_CORE YAMLs use use_dcdf: yes (see cmp_prtoe_*.yaml / dcdf_*.yaml)
  chains/lcdm_full_cosmo.yaml   — LCDM baseline
  LEGACY_ST full-cosmo templates may still say use_prtoe — comparison only

CodeRabbit:
  [ ] cd source && cr   # repeat until 0 findings
EOF
