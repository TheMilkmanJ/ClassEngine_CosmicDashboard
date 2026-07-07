import numpy as np

def compare_cls():
    try:
        prtoe = np.load('crossval_prtoe.npz')
        hi_class = np.load('crossval_hi_class.npz')
    except Exception as e:
        print("Error loading npz files:", e)
        return

    ell = prtoe['ell']
    dl_prtoe = prtoe['dl_tt']
    dl_hiclass = hi_class['dl_tt']
    
    # Calculate fractional difference
    frac_diff = (dl_prtoe - dl_hiclass) / dl_hiclass
    
    max_diff = np.max(np.abs(frac_diff))
    print(f"Max fractional difference between PRTOE approximations and exact hi_class: {max_diff:.3e}")
    
    # If the difference is extremely small, the equations perfectly match.
    if max_diff < 1e-4:
        print("SUCCESS! The PRTOE phenomenological equations perfectly match the exact Horndeski EFT implementation in hi_class.")
    else:
        print("WARNING! There is a significant discrepancy.")
        print(f"Difference at l=2: {frac_diff[0]:.3e}")
        print(f"Difference at l=10: {frac_diff[8]:.3e}")
        print(f"Difference at l=100: {frac_diff[98]:.3e}")
        print(f"Difference at l=1000: {frac_diff[998]:.3e}")

if __name__ == "__main__":
    compare_cls()
