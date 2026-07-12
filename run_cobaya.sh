#!/bin/bash
cd /home/themilkmanj/prtoe_class

# Pre-flight: refuse to launch a config carrying a freeze sentinel
# (e.g. dcdf_z_rad_onset: ZON_FREEZE_PENDING — a value deliberately left
# un-runnable until the zon chain converges; "we do not fix numbers illegally").
for arg in "$@"; do
  case "$arg" in
    *.yaml|*.yml)
      if [ -f "$arg" ] && grep -nE '^[^#]*:\s*[A-Z_]+_PENDING\b' "$arg" >/dev/null; then
        echo "ABORT: $arg contains a freeze sentinel (a *_PENDING value):" >&2
        grep -nE '^[^#]*:\s*[A-Z_]+_PENDING\b' "$arg" >&2
        echo "This config is deliberately un-runnable until the pending value is frozen from its converged source." >&2
        exit 1
      fi
      ;;
  esac
done

/usr/bin/python3.12 -m cobaya.run "$@"
