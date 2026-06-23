#!/usr/bin/env python3
"""Test script to verify mpirun detection logic"""
import os
import shutil

# Simulate the fixed logic
conda_env_path = os.environ.get("CONDA_PREFIX", "")
print(f"CONDA_PREFIX: {conda_env_path}")

# Try to find mpirun: first check env var, then conda bin, then system PATH
mpirun_executable = os.environ.get("DASHBOARD_MPIRUN")
print(f"DASHBOARD_MPIRUN env var: {mpirun_executable}")

if not mpirun_executable:
    conda_mpirun = os.path.join(conda_env_path, "bin", "mpirun") if conda_env_path else None
    print(f"Checking conda mpirun: {conda_mpirun}")
    
    if conda_mpirun and os.path.exists(conda_mpirun):
        mpirun_executable = conda_mpirun
        print(f"✓ Found mpirun in conda: {mpirun_executable}")
    else:
        # Fall back to system mpirun (check common locations)
        mpirun_executable = shutil.which("mpirun") or "/usr/bin/mpirun"
        print(f"✓ Using system mpirun: {mpirun_executable}")

print(f"\nFinal mpirun_executable: {mpirun_executable}")
print(f"Exists: {os.path.exists(mpirun_executable)}")

# Test if it's executable
if os.path.exists(mpirun_executable):
    import subprocess
    try:
        result = subprocess.run([mpirun_executable, "--version"], 
                              capture_output=True, text=True, timeout=5)
        print(f"\nMPI Version check:")
        print(result.stdout[:200] if result.stdout else result.stderr[:200])
    except Exception as e:
        print(f"Error running mpirun: {e}")

# Made with Bob
