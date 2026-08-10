#!/usr/bin/env bash
# Run Polychord for dyad_mnu_bbnfix_desidr2 using all available CPU cores.
# Usage: bash scripts/run_polychord_dyad_desidr2.sh
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
YAML="$REPO_ROOT/chains/dyad_mnu_bbnfix_desidr2_polychord.yaml"
NPROCS=$(nproc)
echo "Launching Polychord with $NPROCS MPI ranks on $(hostname)"
# Bind to cores, use hwthread cpus if desired. Adjust mpirun flags to taste on your system.
mpirun --use-hwthread-cpus -np "$NPROCS" --bind-to core python -m cobaya.run "$YAML"
