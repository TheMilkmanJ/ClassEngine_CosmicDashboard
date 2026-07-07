#!/usr/bin/env python3
"""Fail loudly if the imported classy binary is older than the C sources.

Run after every recompile, before trusting any Python-side number:
    python3 scripts/check_classy_fresh.py
"""
import glob
import os
import sys

import classy

so = getattr(classy, "__file__", None)
# package layout: classy/__init__.py + _classy*.so next to it
cand = []
if so:
    d = os.path.dirname(so)
    cand = glob.glob(os.path.join(d, "_classy*.so")) + glob.glob(os.path.join(d, "*.so"))
    if so.endswith(".so"):
        cand.append(so)
if not cand:
    print(f"FRESHNESS UNKNOWN: no .so found near {so}")
    sys.exit(2)
so_path = max(cand, key=os.path.getmtime)
so_t = os.path.getmtime(so_path)

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
srcs = glob.glob(os.path.join(root, "source", "*.c")) + \
       glob.glob(os.path.join(root, "include", "*.h")) + \
       glob.glob(os.path.join(root, "python", "classy.pyx"))
src_path = max(srcs, key=os.path.getmtime)
src_t = os.path.getmtime(src_path)

print(f"imported : {so_path}")
print(f"binary   : {so_t:.0f}  source newest: {src_t:.0f} ({os.path.basename(src_path)})")
if so_t < src_t:
    print(f"STALE .so: binary is {src_t - so_t:.0f}s older than {os.path.basename(src_path)} "
          f"-- rebuild + reinstall before trusting Python-side numbers")
    sys.exit(1)
print("FRESH: imported classy is newer than all C sources")
