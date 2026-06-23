#!/usr/bin/env python3
try:
    from classy import Class
    print("SUCCESS: classy.Class imported in conda environment!")
    c = Class()
    print("SUCCESS: Class instance created!")
except Exception as e:
    print(f"ERROR: {e}")
    import sys
    sys.exit(1)

