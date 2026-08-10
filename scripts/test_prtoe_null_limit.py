#!/usr/bin/env python3
"""SHIM — renamed to test_legacy_st_null_limit.py (LEGACY_ST lane).

Do not treat this filename as current-core PRTOE validation.
"""
import runpy
import sys
from pathlib import Path

print("NOTE: test_prtoe_null_limit.py is a SHIM → test_legacy_st_null_limit.py (LEGACY_ST)")
sys.argv[0] = str(Path(__file__).with_name("test_legacy_st_null_limit.py"))
runpy.run_path(str(Path(__file__).with_name("test_legacy_st_null_limit.py")), run_name="__main__")
