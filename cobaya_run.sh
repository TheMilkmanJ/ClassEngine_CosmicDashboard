#!/bin/bash
# Activate conda environment and run cobaya-run
set -e

# Source conda initialization
source /home/themilkmanj/miniconda3/etc/profile.d/conda.sh

# Activate the environment
conda activate prtoe_gold

# Run cobaya-run with all arguments passed through
/home/themilkmanj/miniconda3/envs/prtoe_gold/bin/python -m cobaya.run "$@"
