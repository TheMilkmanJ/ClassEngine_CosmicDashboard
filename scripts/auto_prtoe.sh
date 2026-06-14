#!/bin/bash
# ==============================================================================
# PRTOE AUTOMATION SCRIPT: MONITOR BASELINE AND LAUNCH PRTOE
# ==============================================================================

PROJECT_DIR="/mnt/c/Users/themi/projects/prtoe_class"
LOG_FILE="$PROJECT_DIR/chains/prtoe_auto_launch.log"

mkdir -p "$PROJECT_DIR/chains"
echo "=== PRTOE Auto-Runner Started at $(date) ===" > "$LOG_FILE"

# 1. Wait for the active classy/cobaya baseline process to finish
echo "Monitoring baseline CLASS/Cobaya process..." >> "$LOG_FILE"
while ps aux | grep -v grep | grep -q "lcdm_poly.updated.yaml"; do
    sleep 10
done

echo "Baseline LCDM sampler has finished!" >> "$LOG_FILE"

# 2. Extract final log-evidence from stats file
STATS_FILE="$PROJECT_DIR/lcdm_poly_polychord_raw/lcdm_poly.stats"
if [ -f "$STATS_FILE" ]; then
    EVIDENCE=$(grep "log(Z)" "$STATS_FILE" | head -n 1)
    echo "Baseline Evidence: $EVIDENCE" >> "$LOG_FILE"
else
    echo "WARNING: Stats file not found at $STATS_FILE" >> "$LOG_FILE"
fi

# 3. Clean up the residual files from the previous crashed run
echo "Cleaning up residual files from previous PRTOE run..." >> "$LOG_FILE"
rm -rf "$PROJECT_DIR/chains/prtoe_poly_optimized"*
rm -rf "$PROJECT_DIR/prtoe_poly_optimized"*

# 4. Launch the optimized PRTOE run
echo "Launching optimized PRTOE nested sampler..." >> "$LOG_FILE"

# Use -r (resume) if a resume file exists, -f (force) only for a clean start
RESUME_FILE="$PROJECT_DIR/chains/prtoe_poly_optimized_polychord_raw/prtoe_poly_optimized.resume"
if [ -f "$RESUME_FILE" ]; then
    COBAYA_FLAG="-r"
    echo "Resume file found — using -r flag." >> "$LOG_FILE"
else
    COBAYA_FLAG="-f"
    echo "No resume file — using -f flag (clean start)." >> "$LOG_FILE"
fi

/home/themilkmanj/miniconda3/envs/pgtoe_gold/bin/mpirun \
  -genv OMP_NUM_THREADS 1 \
  -np 12 \
  /home/themilkmanj/miniconda3/envs/pgtoe_gold/bin/python3 \
  -m cobaya run "$PROJECT_DIR/cobaya_prtoe_optimized.yaml" \
  --packages-path /home/themilkmanj/cobaya_packages_clean \
  $COBAYA_FLAG >> "$LOG_FILE" 2>&1 &

echo "PRTOE Nested Sampler launched in background with PID $!" >> "$LOG_FILE"
echo "Auto-Runner job complete." >> "$LOG_FILE"
