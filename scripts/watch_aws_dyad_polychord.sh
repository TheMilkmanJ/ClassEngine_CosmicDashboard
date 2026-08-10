#!/usr/bin/env bash
set -euo pipefail

export PATH="$HOME/.local/bin:$PATH"

INTERVAL="${1:-60}"
REGION="${AWS_REGION:-us-east-1}"
INSTANCE_ID="${INSTANCE_ID:-i-0cb294312a23c4fe6}"
AZ="${AZ:-us-east-1a}"
OS_USER="${OS_USER:-ubuntu}"
REMOTE_HOST="${REMOTE_HOST:-}"

RUN_DIR="/home/ubuntu/prtoe_class"
LIVE_FILE="${RUN_DIR}/chains/cmp_prtoe_dyad_ev_polychord_raw/cmp_prtoe_dyad_ev_phys_live.txt"
LOG_FILE="${RUN_DIR}/cmp_prtoe_dyad_ev.aws.launchlog"
RESUME_FILE="${RUN_DIR}/chains/cmp_prtoe_dyad_ev_polychord_raw/cmp_prtoe_dyad_ev.resume"

OUT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/docs/working_logs/_runs/polychord_owner_followup_20260806"
WATCH_LOG="${OUT_DIR}/aws_dyad_watch.log"
PID_FILE="${OUT_DIR}/aws_dyad_watch.pid"
STATE_FILE="${OUT_DIR}/aws_dyad_watch.state"

KEY_DIR="${HOME}/.tmp/eic-polychord-watch"
KEY_FILE="${KEY_DIR}/id_ed25519"

mkdir -p "$OUT_DIR" "$KEY_DIR"
echo "$$" > "$PID_FILE"

if [ ! -f "$KEY_FILE" ]; then
  ssh-keygen -q -t ed25519 -N "" -f "$KEY_FILE" >/dev/null
fi

extract_field() {
  local line="$1"
  local key="$2"
  awk -v target="$key" '
    {
      for (i = 1; i <= NF; ++i) {
        split($i, kv, "=")
        if (kv[1] == target) {
          print kv[2]
          exit
        }
      }
    }
  ' <<<"$line"
}

resolve_remote_host() {
  if [ -n "${REMOTE_HOST}" ]; then
    printf '%s\n' "${REMOTE_HOST}"
    return 0
  fi
  aws ec2 describe-instances \
    --region "$REGION" \
    --instance-ids "$INSTANCE_ID" \
    --query 'Reservations[0].Instances[0].PublicIpAddress' \
    --output text 2>/dev/null
}

describe_instance() {
  aws ec2 describe-instances \
    --region "$REGION" \
    --instance-ids "$INSTANCE_ID" \
    --query 'Reservations[0].Instances[0].[State.Name,PublicIpAddress]' \
    --output text 2>/dev/null
}

last_live_size=""
stalled_intervals=0

while true; do
  ts="$(date -Is)"

  instance_desc="$(describe_instance || true)"
  instance_state="$(awk '{print $1}' <<<"${instance_desc}")"
  instance_ip="$(awk '{print $2}' <<<"${instance_desc}")"

  if [ -z "${instance_state}" ] || [ "${instance_state}" = "None" ] || [ "${instance_state}" = "null" ]; then
    printf '%s status=DESCRIBE_FAIL\n' "$ts" | tee -a "$WATCH_LOG" > "$STATE_FILE"
    sleep "$INTERVAL"
    continue
  fi

  if [ "${instance_state}" != "running" ]; then
    printf '%s status=INSTANCE_%s\n' "$ts" "$(tr '[:lower:]-' '[:upper:]_' <<<"${instance_state}")" | tee -a "$WATCH_LOG" > "$STATE_FILE"
    sleep "$INTERVAL"
    continue
  fi

	  if ! aws ec2-instance-connect send-ssh-public-key \
	    --region "$REGION" \
	    --instance-id "$INSTANCE_ID" \
	    --availability-zone "$AZ" \
	    --instance-os-user "$OS_USER" \
	    --ssh-public-key "file://$KEY_FILE.pub" >/dev/null 2>&1; then
    printf '%s status=EIC_KEY_FAIL\n' "$ts" | tee -a "$WATCH_LOG" > "$STATE_FILE"
    sleep "$INTERVAL"
	    continue
	  fi

  remote_host="${instance_ip}"
  if [ -z "${remote_host}" ] || [ "${remote_host}" = "None" ] || [ "${remote_host}" = "null" ]; then
    remote_host="$(resolve_remote_host || true)"
  fi
  if [ -z "${remote_host}" ] || [ "${remote_host}" = "None" ] || [ "${remote_host}" = "null" ]; then
    printf '%s status=NO_PUBLIC_IP\n' "$ts" | tee -a "$WATCH_LOG" > "$STATE_FILE"
    sleep "$INTERVAL"
    continue
  fi

	  remote_line="$(
	    ssh -T \
	      -o BatchMode=yes \
	      -o StrictHostKeyChecking=no \
	      -o UserKnownHostsFile=/dev/null \
	      -o ConnectTimeout=20 \
	      -i "$KEY_FILE" \
      "${OS_USER}@${remote_host}" 'bash -s' <<EOF
proc_count=\$(pgrep -af "python -m cobaya.run .*cmp_prtoe_dyad_ev.yaml" | grep -vc "bash -c" || true)
launcher_count=\$(pgrep -af "cmp_prtoe_dyad_ev.yaml -f" | grep -Ec "prterun|mpirun" || true)
live_size=NA
live_mtime=NA
log_size=NA
log_mtime=NA
phase=NA
resume=no
[ -f "$LIVE_FILE" ] && live_size=\$(stat -c %s "$LIVE_FILE") && live_mtime=\$(stat -c %Y "$LIVE_FILE")
[ -f "$LOG_FILE" ] && log_size=\$(stat -c %s "$LOG_FILE") && log_mtime=\$(stat -c %Y "$LOG_FILE")
[ -f "$RESUME_FILE" ] && resume=yes
phase=\$(grep -E "Measuring speeds|Calling PolyChord|Writing a resume file|generating live points|Abort" "$LOG_FILE" 2>/dev/null | tail -n 1 | sed "s/[[:space:]][[:space:]]*/_/g")
printf "host=%s proc=%s launcher=%s live_size=%s live_mtime=%s log_size=%s log_mtime=%s resume=%s phase=%s\n" "${remote_host}" "\$proc_count" "\$launcher_count" "\$live_size" "\$live_mtime" "\$log_size" "\$log_mtime" "\$resume" "\${phase:-NA}"
EOF
	  )" || remote_line="proc=ERR launcher=ERR live_size=NA live_mtime=NA log_size=NA log_mtime=NA resume=no phase=SSH_FAIL"

  live_size="$(extract_field "$remote_line" "live_size")"
  proc_count="$(extract_field "$remote_line" "proc")"
  status="OK"

  if [ "${proc_count:-0}" = "0" ] || [ "${proc_count:-0}" = "ERR" ]; then
    status="DOWN"
  elif [ -n "${last_live_size}" ] && [ "${live_size}" = "${last_live_size}" ] && [ "${live_size}" != "NA" ]; then
    stalled_intervals=$((stalled_intervals + 1))
    if [ "$stalled_intervals" -ge 3 ]; then
      status="STALLED"
    fi
  else
    stalled_intervals=0
  fi

  if [ "${live_size}" != "NA" ]; then
    last_live_size="${live_size}"
  fi

  line="${ts} status=${status} stalled_intervals=${stalled_intervals} ${remote_line}"
  printf '%s\n' "$line" | tee -a "$WATCH_LOG" > "$STATE_FILE"
  sleep "$INTERVAL"
done
