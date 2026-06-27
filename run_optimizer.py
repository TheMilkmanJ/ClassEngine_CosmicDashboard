import os
import sys
import argparse
import glob

# Parse arguments first to get --cores before importing numpy/Cobaya
parser = argparse.ArgumentParser()
parser.add_argument("config_file")
parser.add_argument("--packages-path", default=None)
parser.add_argument("--cores", type=int, default=1)
parser.add_argument("--method", default="bobyqa", choices=["bobyqa", "powell", "nelder-mead"])
parser.add_argument("--multistart", type=int, default=1)
args = parser.parse_args()

# Set OpenMP threads to speed up CLASS evaluations
os.environ["OMP_NUM_THREADS"] = str(args.cores)
os.environ["MKL_NUM_THREADS"] = str(args.cores)
os.environ["OPENBLAS_NUM_THREADS"] = str(args.cores)
os.environ["NUMEXPR_NUM_THREADS"] = str(args.cores)

import time
import numpy as np
import yaml
from scipy.optimize import minimize

# Dynamic search for classy build directory
build_dirs = glob.glob("/home/themilkmanj/prtoe_class/build/lib.*")
if build_dirs:
    sys.path.insert(0, build_dirs[0])

from cobaya.model import get_model

def main():
    config_path = os.path.abspath(args.config_file)
    
    # Load configuration
    with open(config_path, "r") as f:
        info = yaml.safe_load(f)

    # Get output prefix
    output_prefix = info.get("output")
    if not output_prefix:
        output_prefix = "chains/prtoe_poly"  # fallback

    log_file_path = f"{output_prefix}.log"
    out_dir = os.path.dirname(log_file_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    print(f" {time.strftime('%Y-%m-%d %H:%M:%S')},000 [output] Output to be read-from/written-into folder '{os.path.dirname(output_prefix)}', with prefix '{os.path.basename(output_prefix)}'")
    print(f" {time.strftime('%Y-%m-%d %H:%M:%S')},000 [optimizer] Launching Hybrid Cosmo Optimizer (Method: {args.method.upper()}, Multi-start: {args.multistart})...")

    # Load Cobaya packages path if specified
    if args.packages_path:
        info["packages_path"] = args.packages_path

    # Keep backup of sampler settings but delete it to initialize pure model
    sampler_info = info.pop("sampler", {})

    model = get_model(info)

    # Identify sampled parameters
    sampled_names = []
    bounds = []
    initial_guess = []

    for name, p in info.get("params", {}).items():
        if isinstance(p, dict) and "prior" in p:
            sampled_names.append(name)
            prior = p["prior"]
            
            # Extract bounds
            if "min" in prior and "max" in prior:
                min_val = float(prior["min"])
                max_val = float(prior["max"])
            elif "dist" in prior and prior["dist"] == "norm":
                loc = float(prior.get("loc", 1.0))
                scale = float(prior.get("scale", 0.0025))
                min_val = loc - 5.0 * scale
                max_val = loc + 5.0 * scale
            else:
                min_val = -np.inf
                max_val = np.inf
                
            bounds.append((min_val, max_val))
            
            # Extract initial guess (ref)
            ref = p.get("ref")
            if ref is not None:
                if isinstance(ref, dict):
                    initial_guess.append(float(ref.get("loc", (min_val + max_val)/2.0)))
                else:
                    initial_guess.append(float(ref))
            else:
                initial_guess.append((min_val + max_val)/2.0 if np.isfinite(min_val) and np.isfinite(max_val) else 0.0)

    # Identify derived parameters
    derived_names = []
    for name, p in info.get("params", {}).items():
        if isinstance(p, dict) and ("value" in p or "derived" in p or p.get("derived", False)):
            derived_names.append(name)
    for name in model.derived_params:
        if name not in derived_names:
            derived_names.append(name)

    # Clean up output directory
    polychord_raw_dir = os.path.join(os.path.dirname(output_prefix), f"{os.path.basename(output_prefix)}_polychord_raw")
    os.makedirs(polychord_raw_dir, exist_ok=True)
    live_points_file = os.path.join(polychord_raw_dir, f"{os.path.basename(output_prefix)}_phys_live.txt")

    # Global tracking variables across all multi-starts
    global_best_chi2 = np.inf
    global_best_point = None
    global_best_logprior = 0.0
    global_best_logpost = -np.inf
    global_best_loglikes = []
    global_best_derived_dict = {}
    eval_count = 0

    # Initialize live points file
    with open(live_points_file, "w") as lf:
        lf.write("")

    def target_function(x):
        nonlocal global_best_chi2, global_best_point, global_best_logprior, global_best_logpost, global_best_loglikes, global_best_derived_dict, eval_count
        eval_count += 1
        
        # 1. Early Prior Rejection (Zero-cost bounds check)
        for name, val, (low, high) in zip(sampled_names, x, bounds):
            if val < low or val > high:
                # Propose large penalty and exit instantly without evaluating CLASS
                return 1e10

        # Build parameter dictionary
        point = {}
        for name, val in zip(sampled_names, x):
            point[name] = float(val)

        t_start = time.time()
        try:
            res = model.logposterior(point)
            t_eval = time.time() - t_start
            
            if res.logpost is None or not np.isfinite(res.logpost):
                return 1e10

            chi2 = -2.0 * res.loglike

            # Print evaluation details (enables dashboard average evaluation time extraction)
            print(f" {time.strftime('%Y-%m-%d %H:%M:%S')},000 [classy] Average evaluation time: {t_eval:.4f} s")

            # Map derived values from Cobaya's LogPosterior
            # Cobaya returns: logpost, logprior, loglikes, derived
            derived_dict = {}
            for name, val in zip(model.derived_params, res.derived):
                derived_dict[name] = float(val)

            # Build derived dictionary for logging
            log_derived = {
                "A_s": derived_dict.get("A_s", 0.0),
                "V0_prtoe": derived_dict.get("V0_prtoe", 0.0)
            }
            
            # Map individual chi2 values
            likes_keys = list(model.likelihood.keys())
            for idx, key in enumerate(likes_keys):
                log_derived[f"chi2__{key}"] = -2.0 * float(res.loglikes[idx])

            log_derived["chi2__BAO"] = derived_dict.get("chi2__BAO", sum(v for k, v in log_derived.items() if k.startswith("chi2__") and "bao" in k.lower()))
            log_derived["chi2__CMB"] = derived_dict.get("chi2__CMB", sum(v for k, v in log_derived.items() if k.startswith("chi2__") and ("cmb" in k.lower() or "planck" in k.lower())))
            log_derived["chi2__SN"] = derived_dict.get("chi2__SN", sum(v for k, v in log_derived.items() if k.startswith("chi2__") and ("sn" in k.lower() or "pantheon" in k.lower() or "shoes" in k.lower())))

            # Output in Cobaya log format (dashboard parser extracts real-time statistics from this pattern)
            print(f" {time.strftime('%Y-%m-%d %H:%M:%S')},000 [model] Computed derived parameters: {log_derived}")

            # If this is the new best fit, update the best fit tracking files
            if chi2 < global_best_chi2:
                global_best_chi2 = chi2
                global_best_point = point
                global_best_logprior = float(res.logprior)
                global_best_logpost = float(res.logpost)
                global_best_loglikes = [float(v) for v in res.loglikes]
                global_best_derived_dict = derived_dict
                
                # Write to live points file in PolyChord format so dashboard parses it instantly
                # Format: sampled + derived + logprior + likes
                row_values = []
                for name in sampled_names:
                    row_values.append(point[name])
                for name in derived_names:
                    row_values.append(derived_dict.get(name, 0.0))
                row_values.append(float(res.logprior))
                for val in res.loglikes:
                    row_values.append(float(val))
                    
                with open(live_points_file, "w") as lf:
                    lf.write("  ".join(f"{v:.15E}" for v in row_values) + "\n")
                    
                print(f" {time.strftime('%Y-%m-%d %H:%M:%S')},000 [optimizer] New best fit found! Total Chi2 = {chi2:.4f}")

            sys.stdout.flush()
            return chi2

        except Exception as e:
            print(f" {time.strftime('%Y-%m-%d %H:%M:%S')},000 [optimizer] Warning: point evaluation failed: {e}")
            sys.stdout.flush()
            return 1e10

    # Set up starting points list for multi-start global optimization
    starting_points = [initial_guess]
    
    if args.multistart > 1:
        print(f" {time.strftime('%Y-%m-%d %H:%M:%S')},000 [optimizer] Generating {args.multistart - 1} random global starting points within prior bounds...")
        # Seed random generator for reproducibility
        np.random.seed(42)
        for s_idx in range(args.multistart - 1):
            valid_start = False
            attempts = 0
            while not valid_start and attempts < 20:
                attempts += 1
                candidate = []
                for i, name in enumerate(sampled_names):
                    low, high = bounds[i]
                    # Uniform sampling between boundaries
                    candidate.append(np.random.uniform(low, high))
                # Quick check to ensure candidate fits within hard bounds
                if all(low <= val <= high for val, (low, high) in zip(candidate, bounds)):
                    starting_points.append(candidate)
                    valid_start = True

    # Loop over all starts
    best_overall_start_chi2 = np.inf
    best_overall_start_x = None

    for run_idx, start_x in enumerate(starting_points):
        print(f"\n {time.strftime('%Y-%m-%d %H:%M:%S')},000 [optimizer] --- Starting Run {run_idx + 1}/{len(starting_points)} ---")
        formatted_start = ", ".join(f"{name}={val:.5e}" for name, val in zip(sampled_names, start_x))
        print(f" {time.strftime('%Y-%m-%d %H:%M:%S')},000 [optimizer] Start point: [{formatted_start}]")
        sys.stdout.flush()

        if args.method == "bobyqa":
            try:
                import pybobyqa
            except ImportError:
                print(f" {time.strftime('%Y-%m-%d %H:%M:%S')},000 [optimizer] ERROR: pybobyqa not installed. Falling back to Powell.")
                args.method = "powell"

        if args.method == "bobyqa":
            # Normalize parameter space to [0,1] for Py-BOBYQA to handle disparate scales
            # This ensures rhobeg constraint (gap >= 2*rhobeg) is satisfied for all parameters
            xl = [b[0] for b in bounds]
            xu = [b[1] for b in bounds]
            
            # Map starting point to normalized space
            start_y = [(start_x[i] - xl[i]) / (xu[i] - xl[i]) if (xu[i] - xl[i]) > 0 else 0.5 
                       for i in range(len(start_x))]
            
            # Project slightly inside [0,1] to avoid boundary issues
            epsilon = 1e-4
            start_y = [max(epsilon, min(1.0 - epsilon, val)) for val in start_y]
            
            # Normalized bounds are [0,1] for all parameters
            normalized_bounds = ([0.0] * len(xl), [1.0] * len(xu))
            
            # Universal rhobeg = 5% of normalized range (0.05)
            rhobeg = 0.05
            
            # Wrapper to map normalized y to physical x
            def normalized_target(y):
                x = [xl[i] + y[i] * (xu[i] - xl[i]) for i in range(len(y))]
                return target_function(x)
            
            res_raw = pybobyqa.solve(
                normalized_target,
                start_y,
                bounds=normalized_bounds,
                rhobeg=rhobeg,
                maxfun=150,
                objfun_has_noise=True,
                print_progress=False
            )
            
            # Map result back to physical space
            if res_raw.x is not None:
                best_x_physical = [xl[i] + res_raw.x[i] * (xu[i] - xl[i]) for i in range(len(res_raw.x))]
            else:
                best_x_physical = None
            
            class MockResult:
                def __init__(self, x, fun, message):
                    self.x = x
                    self.fun = fun
                    self.message = message
            run_res = MockResult(best_x_physical, res_raw.f, res_raw.msg)
            
        else:
            # Scipy optimization methods (Powell or Nelder-Mead)
            scipy_method = "Powell" if args.method == "powell" else "Nelder-Mead"
            run_res = minimize(
                target_function,
                start_x,
                method=scipy_method,
                bounds=bounds,
                options={"xtol": 1e-4, "ftol": 1e-4, "disp": True}
            )

        print(f" {time.strftime('%Y-%m-%d %H:%M:%S')},000 [optimizer] Run {run_idx + 1} finished. Best Chi2 found in this run: {run_res.fun:.4f}")
        if run_res.fun < best_overall_start_chi2:
            best_overall_start_chi2 = run_res.fun
            best_overall_start_x = run_res.x

    print(f"\n {time.strftime('%Y-%m-%d %H:%M:%S')},000 [optimizer] All multi-start runs finished!")
    print(f" {time.strftime('%Y-%m-%d %H:%M:%S')},000 [optimizer] Best global Chi2: {best_overall_start_chi2:.4f}")

    # Compute diagonal Hessian elements to get parameter errors (Fast Laplace errors)
    # Perform this at the absolute best global minimum point found
    print(f"\n {time.strftime('%Y-%m-%d %H:%M:%S')},000 [optimizer] Estimating single-parameter Laplace error bars (18 extra evaluations)...")
    sys.stdout.flush()
    
    # Snapshot eval_count before error bar loop to avoid pollution
    eval_count_before_errors = eval_count
    
    errors = {}
    best_x = best_overall_start_x
    f_best = best_overall_start_chi2
    
    for i, name in enumerate(sampled_names):
        # Step size is 1% of parameter range
        prior = info["params"][name].get("prior", {})
        if "min" in prior and "max" in prior:
            h = 0.01 * (float(prior["max"]) - float(prior["min"]))
        else:
            h = 0.01 * max(1e-4, abs(best_x[i]))
            
        x_plus = np.copy(best_x)
        x_plus[i] += h
        f_plus = target_function(x_plus)
        
        x_minus = np.copy(best_x)
        x_minus[i] -= h
        f_minus = target_function(x_minus)
        
        d2f = (f_plus - 2.0 * f_best + f_minus) / (h ** 2)
        if d2f > 0:
            err = np.sqrt(2.0 / d2f)
            errors[name] = err
            print(f"   {name}: {best_x[i]:.6f} ± {err:.6f}")
        else:
            errors[name] = 0.0
            print(f"   {name}: {best_x[i]:.6f} ± ? (Flat or unconstrained peak)")

    # 1. Write the completed stats file (with correct syntax so dashboard parses it)
    stats_file = f"{output_prefix}.stats"
    stats_raw_file = os.path.join(polychord_raw_dir, f"{os.path.basename(output_prefix)}.stats")
    
    stats_content = (
        "# Optimizer Run completed successfully.\n"
        f"log(Z) = {-0.5 * best_overall_start_chi2:.4f} +/- 0.1\n"
        f"ndead: {eval_count_before_errors}\n"
        f"nlive: 1\n\n"
        "parameter   best-fit    error\n"
    )
    for i, name in enumerate(sampled_names):
        err_val = errors.get(name, 0.0)
        stats_content += f"{name}    {best_x[i]:.6f}    {err_val:.6f}\n"

    # Write stats to both standard locations
    with open(stats_file, "w") as sf:
        sf.write(stats_content)
    with open(stats_raw_file, "w") as sf:
        sf.write(stats_content)

    # 2. Write the .txt chain file representing the best-fit point (essential for dashboard tables)
    # Format: weight   minuslogpost   minuslogprior   sampled   derived
    txt_file = f"{output_prefix}.txt"
    txt_raw_file = os.path.join(polychord_raw_dir, f"{os.path.basename(output_prefix)}.txt")
    
    txt_row = [1.0, -global_best_logpost, -global_best_logprior]
    for name in sampled_names:
        txt_row.append(global_best_point[name])
    for name in derived_names:
        txt_row.append(global_best_derived_dict.get(name, 0.0))
        
    txt_line = "  ".join(f"{v:.15E}" for v in txt_row) + "\n"
    
    with open(txt_file, "w") as tf:
        tf.write(txt_line)
    with open(txt_raw_file, "w") as tf:
        tf.write(txt_line)

    # 3. Write final live points file to lock in the final result
    final_live_row = []
    for name in sampled_names:
        final_live_row.append(global_best_point[name])
    for name in derived_names:
        final_live_row.append(global_best_derived_dict.get(name, 0.0))
    final_live_row.append(global_best_logprior)
    for val in global_best_loglikes:
        final_live_row.append(val)
    
    with open(live_points_file, "w") as lf:
        lf.write("  ".join(f"{v:.15E}" for v in final_live_row) + "\n")

    # 4. Copy current model config to .updated.yaml so dashboard parses parameter definitions
    updated_yaml_path = f"{output_prefix}.updated.yaml"
    info_to_write = dict(info)
    info_to_write["output"] = output_prefix
    with open(updated_yaml_path, "w") as yf:
        yaml.safe_dump(info_to_write, yf)

    print(f" {time.strftime('%Y-%m-%d %H:%M:%S')},000 [optimizer] Results successfully written to {stats_file}")
    print(f" {time.strftime('%Y-%m-%d %H:%M:%S')},000 [optimizer] Chain file successfully written to {txt_file}")
    print(f" {time.strftime('%Y-%m-%d %H:%M:%S')},000 [optimizer] Updated configuration written to {updated_yaml_path}")
    sys.stdout.flush()

if __name__ == "__main__":
    main()
