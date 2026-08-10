#!/usr/bin/env bash
# Launch ONE gold-standard DESI-DR2 PolyChord leg on this host.
# Usage (venv active, from prtoe_class):
#   bash scripts/launch_gold_desidr2_polychord.sh shoes_dyad|shoes_lcdm|trgb_dyad|trgb_lcdm
#   NRANKS=96 bash scripts/launch_gold_desidr2_polychord.sh shoes_dyad
set -euo pipefail
LEG="${1:?usage: $0 shoes_dyad|shoes_lcdm|trgb_dyad|trgb_lcdm|dyad|lcdm}"
NRANKS="${NRANKS:-96}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
source "${HOME}/venv/bin/activate" 2>/dev/null || true

# aliases: dyad/lcdm default to SH0ES pair
case "$LEG" in
  dyad|shoes_dyad) YAML=dyad_mnu_bbnfix_desidr2_ev.yaml; TAG=dyad_mnu_bbnfix_desidr2_ev ;;
  lcdm|shoes_lcdm) YAML=cmp_lcdm_mnu_bbnfix_desidr2_ev.yaml; TAG=cmp_lcdm_mnu_bbnfix_desidr2_ev ;;
  trgb_dyad) YAML=dyad_mnu_bbnfix_desidr2_trgb_ev.yaml; TAG=dyad_mnu_bbnfix_desidr2_trgb_ev ;;
  trgb_lcdm) YAML=cmp_lcdm_mnu_bbnfix_desidr2_trgb_ev.yaml; TAG=cmp_lcdm_mnu_bbnfix_desidr2_trgb_ev ;;
  *) echo "leg must be shoes_dyad|shoes_lcdm|trgb_dyad|trgb_lcdm (or dyad|lcdm)"; exit 1 ;;
esac

if [ -d /home/ubuntu ]; then
  sed -i 's#/home/themilkmanj/#/home/ubuntu/#g' "$YAML"
fi
test -f "$YAML"

# solo rule: any other nested/mcmc cobaya on this host
busy=0
for pid in /proc/[0-9]*; do
  cmd=$(tr '\0' ' ' < "$pid/cmdline" 2>/dev/null || true)
  case "$cmd" in
    *python*-m*cobaya.run*|*prterun*cobaya*) busy=1; echo "busy: $cmd";;
  esac
done
if [ "$busy" = 1 ]; then
  echo "REFUSE: other cobaya work on this host (solo-PolyChord rule)"
  exit 2
fi

mkdir -p chains
export OMP_NUM_THREADS=1
{
  echo "== gold DESI-DR2 PolyChord launch $(date -Is) =="
  echo "leg=$LEG yaml=$YAML ranks=$NRANKS host=$(hostname) nproc=$(nproc)"
} | tee -a "chains/${TAG}.launchlog"

nohup mpirun --use-hwthread-cpus -n "$NRANKS" --bind-to none \
  python -m cobaya.run "$YAML" \
  >> "chains/${TAG}.launchlog" 2>&1 &
echo $! > "${TAG}.aws.pid"
echo "launched pid=$(cat ${TAG}.aws.pid) log=chains/${TAG}.launchlog"
