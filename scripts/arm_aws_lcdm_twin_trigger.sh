#!/usr/bin/env bash
set -euo pipefail

export PATH="$HOME/.local/bin:$PATH"

REGION="${AWS_REGION:-us-east-1}"
INSTANCE_ID="${INSTANCE_ID:-i-0cb294312a23c4fe6}"
AZ="${AZ:-us-east-1a}"
OS_USER="${OS_USER:-ubuntu}"
REMOTE_HOST="${REMOTE_HOST:-}"
MPI_RANKS="${MPI_RANKS:-96}"

LOCAL_REPO="/home/themilkmanj/prtoe_class"
REMOTE_REPO="/home/ubuntu/prtoe_class"
REMOTE_LCDM_YAML="${REMOTE_REPO}/cmp_lcdm_ev.yaml"
REMOTE_TRIGGER="${REMOTE_REPO}/aws_autolaunch_lcdm_twin.sh"
REMOTE_TRIGGER_LOG="${REMOTE_REPO}/cmp_lcdm_ev.autolaunch.log"
REMOTE_TRIGGER_PID="${REMOTE_REPO}/cmp_lcdm_ev.autolaunch.pid"

TMPDIR="${HOME}/.tmp/aws-lcdm-twin-trigger"
KEY_FILE="${HOME}/.tmp/eic-polychord-launch/id_ed25519"
LOCAL_LCDM_AWS_YAML="${TMPDIR}/cmp_lcdm_ev.aws.yaml"
REMOTE_SCRIPT="${TMPDIR}/aws_autolaunch_lcdm_twin.sh"

mkdir -p "$TMPDIR"

if [ ! -f "$KEY_FILE" ]; then
  mkdir -p "$(dirname "$KEY_FILE")"
  ssh-keygen -q -t ed25519 -N "" -f "$KEY_FILE" >/dev/null
fi

resolve_remote_host() {
  if [ -n "${REMOTE_HOST}" ]; then
    printf '%s\n' "${REMOTE_HOST}"
    return 0
  fi
  aws ec2 describe-instances \
    --region "$REGION" \
    --instance-ids "$INSTANCE_ID" \
    --query 'Reservations[0].Instances[0].PublicIpAddress' \
    --output text
}

sed \
  -e 's#/home/themilkmanj/#/home/ubuntu/#g' \
  "${LOCAL_REPO}/cmp_lcdm_ev.yaml" > "$LOCAL_LCDM_AWS_YAML"

cat > "$REMOTE_SCRIPT" <<'EOF'
#!/usr/bin/env bash
set -euo pipefail

RUN_DIR="/home/ubuntu/prtoe_class"
LOG_FILE="${RUN_DIR}/cmp_lcdm_ev.autolaunch.log"
PID_FILE="${RUN_DIR}/cmp_lcdm_ev.autolaunch.pid"
DYAD_MATCH="python -m cobaya.run .*cmp_prtoe_dyad_ev.yaml"
LCDM_MATCH="python -m cobaya.run .*cmp_lcdm_ev.yaml"
MPI_RANKS="__MPI_RANKS__"

echo "$$" > "$PID_FILE"
echo "$(date -Is) armed; waiting for dyad evidence leg to exit" >> "$LOG_FILE"

while pgrep -af "$DYAD_MATCH" >/dev/null 2>&1; do
  echo "$(date -Is) dyad still active; sleeping 60s" >> "$LOG_FILE"
  sleep 60
done

echo "$(date -Is) dyad no longer active; evaluating launch guards" >> "$LOG_FILE"

if pgrep -af "$LCDM_MATCH" >/dev/null 2>&1; then
  echo "$(date -Is) lcdm twin already active; exiting without relaunch" >> "$LOG_FILE"
  exit 0
fi

if pgrep -af "python -m cobaya.run" >/dev/null 2>&1; then
  echo "$(date -Is) another cobaya process is still active; refusing auto-launch to preserve solo-PolyChord rule" >> "$LOG_FILE"
  exit 1
fi

STAMP="$(date +%Y%m%d_%H%M%S)"
[ -d "${RUN_DIR}/chains/cmp_lcdm_ev_polychord_raw" ] && mv "${RUN_DIR}/chains/cmp_lcdm_ev_polychord_raw" "${RUN_DIR}/chains/cmp_lcdm_ev_polychord_raw.stale.${STAMP}"
[ -f "${RUN_DIR}/cmp_lcdm_ev.aws.launchlog" ] && mv "${RUN_DIR}/cmp_lcdm_ev.aws.launchlog" "${RUN_DIR}/cmp_lcdm_ev.aws.launchlog.stale.${STAMP}"

echo "$(date -Is) launching cmp_lcdm_ev.yaml fresh with -f" >> "$LOG_FILE"
source /home/ubuntu/venv/bin/activate
export OMP_NUM_THREADS=1
cd /home/ubuntu/prtoe_class
nohup mpirun --use-hwthread-cpus -n "${MPI_RANKS}" --bind-to none python -m cobaya.run cmp_lcdm_ev.yaml -f > cmp_lcdm_ev.aws.launchlog 2>&1 &
echo $! > /home/ubuntu/prtoe_class/cmp_lcdm_ev.aws.pid
echo "$(date -Is) lcdm twin launch command submitted" >> "$LOG_FILE"
EOF

python3 - <<'PY' "$REMOTE_SCRIPT" "$MPI_RANKS"
from pathlib import Path
import sys
path = Path(sys.argv[1])
ranks = sys.argv[2]
path.write_text(path.read_text().replace("__MPI_RANKS__", ranks))
PY

aws ec2-instance-connect send-ssh-public-key \
  --region "$REGION" \
  --instance-id "$INSTANCE_ID" \
  --availability-zone "$AZ" \
  --instance-os-user "$OS_USER" \
  --ssh-public-key "file://$KEY_FILE.pub" >/dev/null

ssh_opts=(
  -T
  -o BatchMode=yes
  -o StrictHostKeyChecking=no
  -o UserKnownHostsFile=/dev/null
  -o ConnectTimeout=20
  -i "$KEY_FILE"
)

resolved_remote_host="$(resolve_remote_host)"

ssh "${ssh_opts[@]}" "${OS_USER}@${resolved_remote_host}" "cat > '${REMOTE_LCDM_YAML}'" < "$LOCAL_LCDM_AWS_YAML"
ssh "${ssh_opts[@]}" "${OS_USER}@${resolved_remote_host}" "cat > '${REMOTE_TRIGGER}' && chmod 755 '${REMOTE_TRIGGER}'" < "$REMOTE_SCRIPT"
ssh "${ssh_opts[@]}" "${OS_USER}@${resolved_remote_host}" "if [ -f '${REMOTE_TRIGGER_PID}' ] && kill -0 \"\$(cat '${REMOTE_TRIGGER_PID}')\" 2>/dev/null; then echo ALREADY_ARMED; else nohup '${REMOTE_TRIGGER}' >/dev/null 2>&1 < /dev/null & echo \$! > '${REMOTE_TRIGGER_PID}'; echo ARMED; fi"

echo "remote_yaml=${REMOTE_LCDM_YAML}"
echo "remote_trigger=${REMOTE_TRIGGER}"
echo "remote_trigger_log=${REMOTE_TRIGGER_LOG}"
echo "remote_trigger_pid=${REMOTE_TRIGGER_PID}"
echo "remote_host=${resolved_remote_host}"
