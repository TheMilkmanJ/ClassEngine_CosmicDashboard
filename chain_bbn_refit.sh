#!/bin/bash
# NEW FILENAME (never rewrite a live script): wait for me101, run BBN-consistent refit
while kill -0 1711574 2>/dev/null; do sleep 60; done
cd /home/themilkmanj/prtoe_class
OMP_NUM_THREADS=3 /usr/bin/python3 run_cosmicforge.py dcdf_joint_me101_bbn.yaml --packages-path /home/themilkmanj/cobaya_packages_clean --cores 12 --multistart 1 --mcmc-steps 30 --mcmc-chains 2 > chains/dcdf_joint_me101_bbn.runlog 2>&1
echo "$(date) BBN-consistent refit exited" >> chains/joint_chain.log
