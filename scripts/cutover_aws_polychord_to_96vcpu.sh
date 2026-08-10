#!/usr/bin/env bash
set -euo pipefail

export PATH="$HOME/.local/bin:$PATH"

REGION="${AWS_REGION:-us-east-1}"
INSTANCE_ID="${INSTANCE_ID:-i-0cb294312a23c4fe6}"
AZ="${AZ:-us-east-1a}"
OS_USER="${OS_USER:-ubuntu}"
TARGET_TYPE="${TARGET_TYPE:-c7i.24xlarge}"
TARGET_VCPU_QUOTA="${TARGET_VCPU_QUOTA:-96}"
POLL_SEC="${POLL_SEC:-60}"
MPI_RANKS="${MPI_RANKS:-96}"
QUOTA_MODE="${QUOTA_MODE:-spot-only}"

RUN_DIR="/home/themilkmanj/prtoe_class"
OUT_DIR="${RUN_DIR}/docs/working_logs/_runs/polychord_owner_followup_20260806"
LOG_FILE="${OUT_DIR}/aws_96vcpu_cutover.log"
STATE_FILE="${OUT_DIR}/aws_96vcpu_cutover.state"
PID_FILE="${OUT_DIR}/aws_96vcpu_cutover.pid"
KEY_FILE="${HOME}/.tmp/eic-polychord-launch/id_ed25519"

mkdir -p "${OUT_DIR}" "$(dirname "${KEY_FILE}")"
echo "$$" > "${PID_FILE}"

if [ ! -f "${KEY_FILE}" ]; then
  ssh-keygen -q -t ed25519 -N "" -f "${KEY_FILE}" >/dev/null
fi

log_state() {
  local msg="$*"
  local ts
  ts="$(date -Is)"
  printf '%s %s\n' "$ts" "$msg" | tee -a "${LOG_FILE}" > "${STATE_FILE}"
}

resolve_public_ip() {
  aws ec2 describe-instances \
    --region "${REGION}" \
    --instance-ids "${INSTANCE_ID}" \
    --query 'Reservations[0].Instances[0].PublicIpAddress' \
    --output text
}

send_eic_key() {
  aws ec2-instance-connect send-ssh-public-key \
    --region "${REGION}" \
    --instance-id "${INSTANCE_ID}" \
    --availability-zone "${AZ}" \
    --instance-os-user "${OS_USER}" \
    --ssh-public-key "file://${KEY_FILE}.pub" >/dev/null
}

remote_exec() {
  local host="$1"
  shift
  ssh -T \
    -o BatchMode=yes \
    -o StrictHostKeyChecking=no \
    -o UserKnownHostsFile=/dev/null \
    -o ConnectTimeout=20 \
    -i "${KEY_FILE}" \
    "${OS_USER}@${host}" "$@"
}

quota_value() {
  local quota_code="$1"
  aws service-quotas get-service-quota \
    --region "${REGION}" \
    --service-code ec2 \
    --quota-code "${quota_code}" \
    --query 'Quota.Value' \
    --output text
}

log_state "cutover_start target_type=${TARGET_TYPE} target_vcpu=${TARGET_VCPU_QUOTA} mpi_ranks=${MPI_RANKS} quota_mode=${QUOTA_MODE}"

public_ip="$(resolve_public_ip || true)"
if [ -n "${public_ip}" ] && [ "${public_ip}" != "None" ] && [ "${public_ip}" != "null" ]; then
  send_eic_key
  remote_exec "${public_ip}" 'bash -s' <<'EOF'
pkill -f "python -m cobaya.run cmp_prtoe_dyad_ev.yaml -f" 2>/dev/null || true
pkill -f "aws_autolaunch_lcdm_twin.sh" 2>/dev/null || true
echo "REMOTE_RUNS_KILLED"
EOF
  log_state "remote_runs_killed host=${public_ip}"
else
  log_state "remote_runs_kill_skipped no_public_ip"
fi

while true; do
  spot_quota="$(quota_value L-34B43A08)"
  ondemand_quota="$(quota_value L-1216C47A)"
  log_state "quota_poll spot=${spot_quota} ondemand=${ondemand_quota} quota_mode=${QUOTA_MODE}"
  if [ "${QUOTA_MODE}" = "spot-only" ]; then
    if [ "${spot_quota%.*}" -ge "${TARGET_VCPU_QUOTA}" ]; then
      break
    fi
  elif [ "${spot_quota%.*}" -ge "${TARGET_VCPU_QUOTA}" ] && [ "${ondemand_quota%.*}" -ge "${TARGET_VCPU_QUOTA}" ]; then
    break
  fi
  sleep "${POLL_SEC}"
done

log_state "quota_ready spot=${spot_quota} ondemand=${ondemand_quota} quota_mode=${QUOTA_MODE}"

aws ec2 stop-instances --region "${REGION}" --instance-ids "${INSTANCE_ID}" >/dev/null
log_state "instance_stop_submitted"
aws ec2 wait instance-stopped --region "${REGION}" --instance-ids "${INSTANCE_ID}"
log_state "instance_stopped"

aws ec2 modify-instance-attribute \
  --region "${REGION}" \
  --instance-id "${INSTANCE_ID}" \
  --instance-type "{\"Value\":\"${TARGET_TYPE}\"}"
log_state "instance_type_modified type=${TARGET_TYPE}"

aws ec2 start-instances --region "${REGION}" --instance-ids "${INSTANCE_ID}" >/dev/null
log_state "instance_start_submitted"
aws ec2 wait instance-running --region "${REGION}" --instance-ids "${INSTANCE_ID}"
aws ec2 wait instance-status-ok --region "${REGION}" --instance-ids "${INSTANCE_ID}"
log_state "instance_running_and_ok"

public_ip="$(resolve_public_ip)"
log_state "instance_public_ip host=${public_ip}"

send_eic_key
remote_exec "${public_ip}" 'bash -s' <<EOF
set -euo pipefail
cd /home/ubuntu/prtoe_class
STAMP=\$(date +%Y%m%d_%H%M%S)
[ -d chains/cmp_prtoe_dyad_ev_polychord_raw ] && mv chains/cmp_prtoe_dyad_ev_polychord_raw chains/cmp_prtoe_dyad_ev_polychord_raw.stale.\${STAMP}
[ -f cmp_prtoe_dyad_ev.aws.launchlog ] && mv cmp_prtoe_dyad_ev.aws.launchlog cmp_prtoe_dyad_ev.aws.launchlog.stale.\${STAMP}
source /home/ubuntu/venv/bin/activate
export OMP_NUM_THREADS=1
cd /home/ubuntu/prtoe_class
nohup mpirun --use-hwthread-cpus -n ${MPI_RANKS} --bind-to none python -m cobaya.run cmp_prtoe_dyad_ev.yaml -f > cmp_prtoe_dyad_ev.aws.launchlog 2>&1 &
echo \$! > /home/ubuntu/prtoe_class/cmp_prtoe_dyad_ev.aws.pid
EOF
log_state "dyad_relaunched host=${public_ip} mpi_ranks=${MPI_RANKS}"

MPI_RANKS="${MPI_RANKS}" REMOTE_HOST="${public_ip}" "${RUN_DIR}/scripts/arm_aws_lcdm_twin_trigger.sh" >> "${LOG_FILE}" 2>&1
log_state "lcdm_twin_rearmed host=${public_ip} mpi_ranks=${MPI_RANKS}"

send_eic_key
remote_exec "${public_ip}" 'bash -s' <<'EOF'
echo "=== DYAD PROCESS ==="
pgrep -af "cmp_prtoe_dyad_ev.yaml -f" || true
echo "=== LCDM TRIGGER ==="
pgrep -af "aws_autolaunch_lcdm_twin.sh|cmp_lcdm_ev.yaml -f" || true
echo "=== DYAD LOG TAIL ==="
tail -n 40 /home/ubuntu/prtoe_class/cmp_prtoe_dyad_ev.aws.launchlog || true
echo "=== WATCH DIR ==="
ls -lah /home/ubuntu/prtoe_class/chains/cmp_prtoe_dyad_ev_polychord_raw 2>/dev/null || true
EOF
log_state "cutover_complete host=${public_ip} target_type=${TARGET_TYPE} mpi_ranks=${MPI_RANKS}"
