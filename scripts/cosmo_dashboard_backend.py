import uvicorn
from fastapi import FastAPI, UploadFile, File, HTTPException, Body
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import subprocess
import os
import shutil
import json
import psutil
import signal
import re
import yaml
from pathlib import Path
import time
from typing import List, Optional
import asyncio

# --- Globals ---
# This will hold the subprocess.Popen object of the running Cobaya job
RUNNING_PROCESS = None
# This will hold the background monitor process for auto-plotting
MONITOR_PROCESS = None
# This will hold the output prefix parsed from the YAML, e.g., "chains/prtoe_polychord"
ACTIVE_OUTPUT_PREFIX = ""
# Holds external logs (like from the monitor script) to be passed to the UI
EXTERNAL_LOGS = []
# Holds the path to the currently active YAML config
ACTIVE_YAML_PATH = ""
# Holds the persistent state of the system
CURRENT_STATUS = "idle"
# Holds the latest structured alerts from the watchdog
WATCHDOG_ALERTS = []
# Tracks the start time of the active run to compute ETA and speed
RUN_START_TIME = None


# --- FastAPI App Setup ---
app = FastAPI(title="CosmicDashboard Backend")

# Allow all origins for local file:// access from the browser
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Pydantic Models for API requests ---
class RunConfig(BaseModel):
    config_name: str
    cores: int = psutil.cpu_count(logical=False) or 4
    auto_rebuild: bool = True
    force_overwrite: Optional[bool] = None
class LogMessage(BaseModel):
    message: str
class UpdateBaseline(BaseModel):
    dataset: str
    log_evidence: float
    best_chi2: Optional[float] = None

class WatchdogAlert(BaseModel):
    parameter: str
    status: str
    suggestion: str
    new_min: Optional[float] = None
    new_max: Optional[float] = None

class WatchdogReport(BaseModel):
    alerts: List[WatchdogAlert]

class ApplyPriorsRequest(BaseModel):
    config_name: str
    updates: dict

# --- Helper Functions ---
def get_output_prefix_from_yaml(config_path: str) -> str:
    """Parses the YAML file to find the 'output' key."""
    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
            if 'output' in config:
                return config['output']
    except Exception:
        pass
    # Fallback if not found
    return "chains/cobaya_run"

def parse_polychord_stats(stats_file: Path, resume_file: Optional[Path] = None):
    """Parses a PolyChord .stats file or .resume file to extract key metrics (dead points, evidence)."""
    stats = {
        "dead_points": 0,
        "log_evidence": None,
        "log_evidence_error": None,
    }

    # 1. Try reading the completed stats file first
    if stats_file.exists():
        try:
            with open(stats_file, 'r') as f:
                content = f.read()

            # Read dead points
            ndead_match = re.search(r"ndead:\s*(\d+)", content)
            if ndead_match:
                stats["dead_points"] = int(ndead_match.group(1))

            # Read log(Z) and error from stats file
            logz_match = re.search(r"log\(Z\)\s*=\s*([-\d.eE+]+)\s*\+/-\s*([-\d.eE+]+)", content)
            if logz_match:
                stats["log_evidence"] = float(logz_match.group(1))
                stats["log_evidence_error"] = float(logz_match.group(2))
                return stats
        except Exception:
            pass

    # 2. Fall back to reading the resume file for real-time progress if stats file is not complete/exists
    if resume_file and resume_file.exists():
        try:
            with open(resume_file, 'r') as f:
                content = f.read()

            # Read dead points (iterations)
            dead_points_match = re.search(r"=== Number of dead points/iterations ===\s*\n\s*(\d+)", content)
            if dead_points_match:
                stats["dead_points"] = int(dead_points_match.group(1))

            # Read log(Z)
            logz_match = re.search(r"=== global evidence -- log\(<Z>\) ===\s*\n\s*([-\d.eE+]+)", content)
            if logz_match:
                stats["log_evidence"] = float(logz_match.group(1))

            # Read log(Z^2) to estimate the error
            logz2_match = re.search(r"=== global evidence\^2 -- log\(<Z\^2>\) ===\s*\n\s*([-\d.eE+]+)", content)
            if logz_match and logz2_match:
                import math
                logz = float(logz_match.group(1))
                logz2 = float(logz2_match.group(1))
                try:
                    diff = logz2 - 2 * logz
                    if diff > 0:
                        stats["log_evidence_error"] = (math.exp(diff) - 1)**0.5
                    else:
                        stats["log_evidence_error"] = 0.1
                except Exception:
                    stats["log_evidence_error"] = 0.1
            return stats
        except Exception:
            pass

    # 3. Fall back to parsing the log file to get an initialization-phase prior-average evidence baseline
    log_file = stats_file.with_suffix(".log")
    if log_file.exists():
        try:
            logls = []
            pattern = re.compile(r"Computed derived parameters:\s*(\{.*\})")
            with open(log_file, 'r') as f:
                for line in f:
                    match = pattern.search(line)
                    if match:
                        try:
                            import ast
                            params_dict = ast.literal_eval(match.group(1))
                            chi2_keys = [k for k in params_dict.keys() if k.startswith('chi2__')]
                            if chi2_keys:
                                cmb_vals = [params_dict[k] for k in chi2_keys if 'cmb' in k.lower() or 'planck' in k.lower()]
                                bao_vals = [params_dict[k] for k in chi2_keys if 'bao' in k.lower()]
                                sn_vals = [params_dict[k] for k in chi2_keys if 'sn' in k.lower() or 'pantheon' in k.lower() or 'shoes' in k.lower()]
                                
                                cmb_sum = sum(cmb_vals) if cmb_vals else 0.0
                                bao_sum = sum(bao_vals) if bao_vals else 0.0
                                sn_sum = sum(sn_vals) if sn_vals else 0.0
                                
                                chi2_bao = params_dict.get('chi2__BAO', bao_sum)
                                chi2_cmb = params_dict.get('chi2__CMB', cmb_sum)
                                chi2_sn = params_dict.get('chi2__SN', sn_sum)
                                
                                tot_chi2 = (chi2_bao or 0.0) + (chi2_cmb or 0.0) + (chi2_sn or 0.0)
                                if tot_chi2 == 0.0:
                                    tot_chi2 = sum([params_dict[k] for k in chi2_keys])
                                
                                if tot_chi2 > 0.0:
                                    logls.append(-0.5 * tot_chi2)
                        except Exception:
                            pass
            
            if logls:
                import math
                max_val = max(logls)
                logz_prior = max_val + math.log(sum(math.exp(x - max_val) for x in logls)) - math.log(len(logls))
                stats["log_evidence"] = logz_prior
                
                # Estimate uncertainty as the standard error of the mean
                log_mean_L2 = max(2 * x for x in logls) + math.log(sum(math.exp(2 * x - max(2 * y for y in logls)) for x in logls)) - math.log(len(logls))
                diff = log_mean_L2 - 2 * logz_prior
                if diff > 0:
                    stats["log_evidence_error"] = ((math.exp(diff) - 1) / len(logls))**0.5
                else:
                    stats["log_evidence_error"] = 0.5
        except Exception:
            pass

    return stats

# --- Performance Optimization Cache ---
LOG_FILE_POSITION = 0
BEST_FIT_LOG_CACHE = None

STRUGGLES_FILE_POSITION = 0
STRUGGLES_CACHE = {}
STRUGGLES_RANK_STATE = {}
STRUGGLES_RANK_TRACEBACK = {}

RAW_FILE_POSITIONS = {}
BEST_FIT_FILE_CACHE = {}

def get_best_fit_from_log(log_path):
    """Parses the log file to extract real-time evaluations and find the best fit chi2 and parameters."""
    global LOG_FILE_POSITION, BEST_FIT_LOG_CACHE
    if not log_path or not os.path.exists(log_path):
        return None
        
    try:
        file_size = os.path.getsize(log_path)
        if file_size < LOG_FILE_POSITION:
            LOG_FILE_POSITION = 0
            # Mid-run log truncations should NOT reset the historical best chi2 cache
            
        best_chi2 = BEST_FIT_LOG_CACHE["total"] if BEST_FIT_LOG_CACHE else float('inf')
        best_eval = BEST_FIT_LOG_CACHE
        
        # We match lines like: Computed derived parameters: {'A_s': ..., 'chi2__BAO': 290.87, ...}
        pattern = re.compile(r"Computed derived parameters:\s*(\{.*\})")
        
        with open(log_path, 'r') as f:
            f.seek(LOG_FILE_POSITION)
            for line in f:
                match = pattern.search(line)
                if match:
                    try:
                        import ast
                        params_dict = ast.literal_eval(match.group(1))
                        chi2_keys = [k for k in params_dict.keys() if k.startswith('chi2__')]
                        if chi2_keys:
                            cmb_vals = [params_dict[k] for k in chi2_keys if 'cmb' in k.lower() or 'planck' in k.lower()]
                            bao_vals = [params_dict[k] for k in chi2_keys if 'bao' in k.lower()]
                            sn_vals = [params_dict[k] for k in chi2_keys if 'sn' in k.lower() or 'pantheon' in k.lower() or 'shoes' in k.lower()]
                            
                            cmb_sum = sum(cmb_vals) if cmb_vals else None
                            bao_sum = sum(bao_vals) if bao_vals else None
                            sn_sum = sum(sn_vals) if sn_vals else None
                            
                            chi2_bao = params_dict.get('chi2__BAO', bao_sum)
                            chi2_cmb = params_dict.get('chi2__CMB', cmb_sum)
                            chi2_sn = params_dict.get('chi2__SN', sn_sum)
                            
                            tot = (chi2_bao or 0.0) + (chi2_cmb or 0.0) + (chi2_sn or 0.0)
                            if tot == 0.0:
                                tot = sum([params_dict[k] for k in chi2_keys])
                                
                            if tot < best_chi2:
                                best_chi2 = tot
                                best_eval = {
                                    "total": tot,
                                    "cmb": chi2_cmb,
                                    "bao": chi2_bao,
                                    "sn": chi2_sn,
                                    "raw_params": params_dict
                                }
                    except Exception:
                        continue
            LOG_FILE_POSITION = f.tell()
            BEST_FIT_LOG_CACHE = best_eval
    except Exception:
        pass
    return BEST_FIT_LOG_CACHE

def extract_model_struggles(log_path):
    """Associates CLASS error tracebacks with subsequent evaluation failures on the same MPI rank."""
    global STRUGGLES_FILE_POSITION, STRUGGLES_CACHE, STRUGGLES_RANK_STATE, STRUGGLES_RANK_TRACEBACK
    if not log_path or not os.path.exists(log_path):
        return {}
        
    try:
        file_size = os.path.getsize(log_path)
        if file_size < STRUGGLES_FILE_POSITION:
            STRUGGLES_FILE_POSITION = 0
            STRUGGLES_CACHE = {}
            STRUGGLES_RANK_STATE = {}
            STRUGGLES_RANK_TRACEBACK = {}
            
        pattern_rank = re.compile(r"\[(\d+)\s*:\s*(\w+)\]")
        
        with open(log_path, 'r') as lf:
            lf.seek(STRUGGLES_FILE_POSITION)
            for line in lf:
                match = pattern_rank.search(line)
                if match:
                    rank = int(match.group(1))
                    source = match.group(2)
                    
                    if source == 'classy':
                        if "failed" in line.lower() or "error" in line.lower() or "ignored error" in line.lower():
                            STRUGGLES_RANK_STATE[rank] = 'failed_class'
                            STRUGGLES_RANK_TRACEBACK[rank] = [line]
                        elif STRUGGLES_RANK_STATE.get(rank) == 'failed_class':
                            STRUGGLES_RANK_TRACEBACK[rank].append(line)
                    elif source == 'model' and "calculation failed" in line.lower():
                        if STRUGGLES_RANK_STATE.get(rank) == 'failed_class':
                            traceback_text = "".join(STRUGGLES_RANK_TRACEBACK[rank]).lower()
                            
                            if "ncdm" in traceback_text or "neutrino" in traceback_text or "non-cold" in traceback_text:
                                STRUGGLES_CACHE["NCDM (Massive Neutrinos)"] = STRUGGLES_CACHE.get("NCDM (Massive Neutrinos)", 0) + 1
                            elif "background" in traceback_text:
                                STRUGGLES_CACHE["Background Dynamics"] = STRUGGLES_CACHE.get("Background Dynamics", 0) + 1
                            elif "thermo" in traceback_text or "reionization" in traceback_text:
                                STRUGGLES_CACHE["Thermal History"] = STRUGGLES_CACHE.get("Thermal History", 0) + 1
                            elif "perturb" in traceback_text:
                                STRUGGLES_CACHE["Perturbations (Cls)"] = STRUGGLES_CACHE.get("Perturbations (Cls)", 0) + 1
                            elif "lensing" in traceback_text:
                                STRUGGLES_CACHE["Lensing Integration"] = STRUGGLES_CACHE.get("Lensing Integration", 0) + 1
                            else:
                                STRUGGLES_CACHE["Numerical Instability"] = STRUGGLES_CACHE.get("Numerical Instability", 0) + 1
                                
                            STRUGGLES_RANK_STATE[rank] = None
                            STRUGGLES_RANK_TRACEBACK[rank] = []
                    elif source == 'model' and STRUGGLES_RANK_STATE.get(rank) == 'failed_class':
                        STRUGGLES_RANK_STATE[rank] = None
                        STRUGGLES_RANK_TRACEBACK[rank] = []
                else:
                    for r, state in STRUGGLES_RANK_STATE.items():
                        if state == 'failed_class':
                            STRUGGLES_RANK_TRACEBACK[r].append(line)
            STRUGGLES_FILE_POSITION = lf.tell()
    except Exception:
        pass
        
    return dict(STRUGGLES_CACHE)

def get_best_fit_details(output_prefix: str):
    """Reads the raw PolyChord text file or log to find the lowest -2 ln(L) (chi2) and its individual dataset breakdowns."""
    global RAW_FILE_POSITIONS, BEST_FIT_FILE_CACHE
    log_file = Path(f"{output_prefix}.log")
    best_log_fit = get_best_fit_from_log(log_file)
    
    prefix_path = Path(output_prefix)
    raw_file = prefix_path.parent / f"{prefix_path.name}_polychord_raw" / f"{prefix_path.name}.txt"
    live_file = prefix_path.parent / f"{prefix_path.name}_polychord_raw" / f"{prefix_path.name}_phys_live.txt"
    final_file = Path(f"{output_prefix}.txt")
    
    files_to_check = []
    if final_file.exists():
        files_to_check.append((final_file, "final"))
    if raw_file.exists():
        files_to_check.append((raw_file, "raw_txt"))
    if live_file.exists():
        files_to_check.append((live_file, "live"))
        
    best_file_fit = None
    best_chi2_file = float('inf')
    
    for fpath, ftype in files_to_check:
        fpath_str = str(fpath)
        updated_yaml = Path(f"{output_prefix}.updated.yaml")
        if not updated_yaml.exists():
            continue
            
        try:
            file_size = os.path.getsize(fpath)
            # Reset position if file is truncated, but do NOT clear the historical best-fit cache!
            if fpath_str not in RAW_FILE_POSITIONS or file_size < RAW_FILE_POSITIONS[fpath_str]:
                RAW_FILE_POSITIONS[fpath_str] = 0
                
            current_best = BEST_FIT_FILE_CACHE.get(fpath_str)
            best_chi2_this_file = current_best["total"] if current_best else float('inf')
            best_fit_this_file = current_best
            
            with open(updated_yaml, 'r') as f:
                up_cfg = yaml.safe_load(f)
                
            params = up_cfg.get('params', {})
            likelihoods = up_cfg.get('likelihood', {})
            
            sampled = []
            derived = []
            
            for name, p_dict in params.items():
                if not isinstance(p_dict, dict):
                    continue
                if 'value' in p_dict:
                    val = p_dict['value']
                    if isinstance(val, str) and 'lambda' in val:
                        derived.append(name)
                elif 'prior' in p_dict:
                    sampled.append(name)
                else:
                    derived.append(name)
                    
            with open(fpath, 'r') as f:
                f.seek(RAW_FILE_POSITIONS[fpath_str])
                
                # Check for header in final_file
                has_header = False
                names_in_header = []
                if ftype == "final" and RAW_FILE_POSITIONS[fpath_str] == 0:
                    first_line = f.readline()
                    if first_line.startswith('#'):
                        has_header = True
                        names_in_header = first_line.lstrip('#').strip().split()
                    else:
                        f.seek(0)
                
                for line in f:
                    if line.strip().startswith('#'):
                        continue
                    parts = line.strip().split()
                    if len(parts) >= 2:
                        try:
                            # 1. Compute total chi2 based on file type
                            if ftype == "live":
                                chi2 = -2.0 * float(parts[-1])
                            elif ftype == "raw_txt":
                                chi2 = float(parts[1])
                            elif ftype == "final":
                                if has_header and 'minuslogprior' in names_in_header:
                                    minuslogpost = float(parts[names_in_header.index('minuslogpost')])
                                    minuslogprior = float(parts[names_in_header.index('minuslogprior')])
                                    chi2 = 2.0 * (minuslogpost - minuslogprior)
                                else:
                                    chi2 = 2.0 * (float(parts[1]) - float(parts[2]))

                            if chi2 < best_chi2_this_file:
                                best_chi2_this_file = chi2
                                best_parts = parts
                                
                                raw_params = {}
                                
                                # 2. Map parameters based on file type
                                if ftype == "final" and has_header:
                                    for idx, name in enumerate(names_in_header):
                                        if idx < len(best_parts):
                                            try:
                                                raw_params[name] = float(best_parts[idx])
                                            except ValueError:
                                                pass
                                else:
                                    if ftype == "final":
                                        sampled_clean = [p for p in sampled if not params[p].get('drop')]
                                        names_params = sampled_clean + derived
                                        idx_start = 3
                                    elif ftype == "live":
                                        priors = ["logprior__0"]
                                        likes = [f"loglike__{name}" for name in likelihoods.keys()]
                                        names_params = sampled + derived + priors + likes
                                        idx_start = 0
                                    else: # raw_txt
                                        priors = ["logprior__0"]
                                        likes = [f"loglike__{name}" for name in likelihoods.keys()]
                                        names_params = sampled + derived + priors + likes
                                        idx_start = 2
                                        
                                    for i, name in enumerate(names_params):
                                        idx = idx_start + i
                                        if idx < len(best_parts):
                                            raw_params[name] = float(best_parts[idx])
                                            
                                # 3. Safely sum likelihood parameters to positive chi2 values (handling loglike and chi2 prefixes)
                                cmb_vals = []
                                for k, v in raw_params.items():
                                    if 'cmb' in k.lower() or 'planck' in k.lower():
                                        if k.startswith('loglike__'):
                                            cmb_vals.append(-2.0 * v)
                                        elif k.startswith('chi2__'):
                                            cmb_vals.append(v)

                                bao_vals = []
                                for k, v in raw_params.items():
                                    if 'bao' in k.lower():
                                        if k.startswith('loglike__'):
                                            bao_vals.append(-2.0 * v)
                                        elif k.startswith('chi2__'):
                                            bao_vals.append(v)

                                sn_vals = []
                                for k, v in raw_params.items():
                                    if 'sn' in k.lower() or 'pantheon' in k.lower() or 'shoes' in k.lower():
                                        if k.startswith('loglike__'):
                                            sn_vals.append(-2.0 * v)
                                        elif k.startswith('chi2__'):
                                            sn_vals.append(v)
                                            
                                best_cmb = sum(cmb_vals) if cmb_vals else None
                                best_bao = sum(bao_vals) if bao_vals else None
                                best_sn = sum(sn_vals) if sn_vals else None
                                
                                best_fit_this_file = {
                                    "total": chi2,
                                    "cmb": raw_params.get('chi2__CMB', best_cmb),
                                    "bao": raw_params.get('chi2__BAO', best_bao),
                                    "sn": raw_params.get('chi2__SN', best_sn),
                                    "raw_params": raw_params
                                }
                        except (ValueError, IndexError):
                            pass
                RAW_FILE_POSITIONS[fpath_str] = f.tell()
                BEST_FIT_FILE_CACHE[fpath_str] = best_fit_this_file
                
            if best_fit_this_file and (best_file_fit is None or best_fit_this_file["total"] < best_chi2_file):
                best_chi2_file = best_fit_this_file["total"]
                best_file_fit = best_fit_this_file
        except Exception:
            pass
            
    fits = [f for f in [best_log_fit, best_file_fit] if f is not None]
    if fits:
        return min(fits, key=lambda x: x['total'])
    return None

# --- API Endpoints ---

@app.get("/api/sysinfo")
async def get_sysinfo():
    """Returns the currently active version and path of CLASS."""
    conda_env_path = os.environ.get("CONDA_PREFIX", "")
    python_executable = os.path.join(conda_env_path, "bin", "python3") if conda_env_path else "python3"
    
    try:
        result = subprocess.run(
            [python_executable, "-c", "import classy; print(classy.__file__)"], 
            capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0:
            path = result.stdout.strip()
            if "prtoe" in path.lower():
                return {"version": "PRTOE Custom CLASS", "path": path}
            else:
                return {"version": "Standard CLASS", "path": path}
    except Exception:
        pass
    return {"version": "Unknown CLASS", "path": "N/A"}

class AdoptedProcess:
    def __init__(self, pid):
        self.pid = pid
        self.returncode = 0
    def poll(self):
        import psutil
        if psutil.pid_exists(self.pid):
            try:
                p = psutil.Process(self.pid)
                if p.status() == psutil.STATUS_ZOMBIE:
                    return 0
                return None
            except psutil.NoSuchProcess:
                return 0
        return 0

def find_and_adopt_running_cobaya():
    global RUNNING_PROCESS, ACTIVE_OUTPUT_PREFIX, ACTIVE_YAML_PATH, CURRENT_STATUS, RUN_START_TIME
    if RUNNING_PROCESS is not None:
        return
        
    import psutil
    for proc in psutil.process_iter(['pid', 'name', 'cmdline', 'create_time']):
        try:
            cmdline = proc.info.get('cmdline')
            if cmdline:
                cmd_str = " ".join(cmdline)
                # Check for "cobaya" and "uploaded_config.yaml"
                if "cobaya" in cmd_str and "uploaded_config.yaml" in cmd_str:
                    pid = proc.info['pid']
                    RUNNING_PROCESS = AdoptedProcess(pid)
                    ACTIVE_YAML_PATH = "uploaded_config.yaml"
                    ACTIVE_OUTPUT_PREFIX = get_output_prefix_from_yaml(ACTIVE_YAML_PATH)
                    CURRENT_STATUS = "running"
                    RUN_START_TIME = proc.info['create_time']
                    print(f"Adopted running Cobaya process: PID {pid}, Output Prefix: {ACTIVE_OUTPUT_PREFIX}")
                    break
        except Exception:
            pass

@app.get("/api/status")
async def get_status():
    """Checks the status of the running Cobaya process and reports progress."""
    global RUNNING_PROCESS, ACTIVE_OUTPUT_PREFIX, EXTERNAL_LOGS, CURRENT_STATUS, WATCHDOG_ALERTS, RUN_START_TIME

    if not RUNNING_PROCESS:
        find_and_adopt_running_cobaya()

    if RUNNING_PROCESS:
        if RUNNING_PROCESS.poll() is None:
            CURRENT_STATUS = "running"
        else:
            # Check return code to see if it was successful or failed/stopped
            CURRENT_STATUS = "completed" if RUNNING_PROCESS.returncode == 0 else "stopped"
            RUNNING_PROCESS = None # Clear the finished process

    stats_data = {
        "status": CURRENT_STATUS,
        "dead_points": 0,
        "log_evidence": None,
        "log_evidence_error": None,
        "best_chi2": None,
        "best_cmb": None,
        "best_bao": None,
        "best_sn": None,
        "best_raw_params": None,
        "init_percent": 0,
        "cpu_percent": psutil.cpu_percent(),
        "terminal_output": [],
        "external_logs": list(EXTERNAL_LOGS),
        "watchdog_alerts": WATCHDOG_ALERTS,
        "speed": "-",
        "eta": "-",
        "constraints": [],
        "tension_status": "Unknown",
        "struggles": {},
        "ncdm_status": {
            "enabled": False,
            "mass": None,
            "struggles": 0
        }
    }

    # Clear logs after sending them to the frontend
    EXTERNAL_LOGS.clear()

    if CURRENT_STATUS != "idle" and ACTIVE_OUTPUT_PREFIX:
        stats_file = Path(f"{ACTIVE_OUTPUT_PREFIX}.stats")
        prefix_path = Path(ACTIVE_OUTPUT_PREFIX)
        resume_file = prefix_path.parent / f"{prefix_path.name}_polychord_raw" / f"{prefix_path.name}.resume"
        stats_data.update(parse_polychord_stats(stats_file, resume_file))
        
        fit_details = get_best_fit_details(ACTIVE_OUTPUT_PREFIX)
        if fit_details is not None:
            stats_data["best_chi2"] = fit_details["total"]
            stats_data["best_cmb"] = fit_details["cmb"]
            stats_data["best_bao"] = fit_details["bao"]
            stats_data["best_sn"] = fit_details["sn"]
            stats_data["best_raw_params"] = fit_details["raw_params"]

        # Calculate speed and ETA
        if CURRENT_STATUS == "running" and RUN_START_TIME:
            elapsed = time.time() - RUN_START_TIME
            dead_pts = stats_data.get("dead_points", 0)
            if elapsed > 10 and dead_pts > 0:
                pts_per_sec = dead_pts / elapsed
                pts_per_min = pts_per_sec * 60
                stats_data["speed"] = f"{pts_per_min:.1f} pts/min"
                
                # Estimating convergence at 3000 points
                remaining_pts = max(0, 3000 - dead_pts)
                if pts_per_sec > 0:
                    remaining_sec = remaining_pts / pts_per_sec
                    hours = int(remaining_sec // 3600)
                    minutes = int((remaining_sec % 3600) // 60)
                    if hours > 0:
                        stats_data["eta"] = f"{hours}h {minutes}m"
                    else:
                        stats_data["eta"] = f"{minutes}m"

        # Parse 1-sigma parameter constraints from summary file
        summary_file = Path(f"{ACTIVE_OUTPUT_PREFIX}_summary.txt")
        if summary_file.exists():
            try:
                with open(summary_file, "r") as f:
                    lines = f.readlines()
                in_constraints = False
                parsed_constraints = []
                for line in lines:
                    if "PARAMETER CONSTRAINTS" in line:
                        in_constraints = True
                        continue
                    if in_constraints:
                        if line.strip().startswith("---") or not line.strip():
                            if parsed_constraints:
                                break
                            continue
                        match = re.match(r"\s*([a-zA-Z0-9_\(\)\{\}\\\^\-\+\/\*\.]+)\s*:\s*([0-9.eE\-+]+)\s*\+/-\s*([0-9.eE\-+]+)", line)
                        if match:
                            parsed_constraints.append({
                                "parameter": match.group(1).strip(),
                                "mean": match.group(2).strip(),
                                "error": match.group(3).strip()
                            })
                stats_data["constraints"] = parsed_constraints
            except Exception:
                pass

        # Calculate tension status: prefer mean constraints if available, fallback to best-fit
        h0_val = None
        h0_err = None
        s8_val = None
        s8_err = None
        
        # Try mean constraints first
        if stats_data.get("constraints"):
            for c in stats_data["constraints"]:
                param_name = c["parameter"].lower()
                if param_name == 'h0':
                    try:
                        h0_val = float(c["mean"])
                        h0_err = float(c["error"])
                    except ValueError:
                        pass
                elif param_name == 's8':
                    try:
                        s8_val = float(c["mean"])
                        s8_err = float(c["error"])
                    except ValueError:
                        pass
                    
        # Fallback to best-fit parameters if mean constraints not found
        if h0_val is None or s8_val is None:
            fit_details = get_best_fit_details(ACTIVE_OUTPUT_PREFIX)
            if fit_details is not None and "raw_params" in fit_details:
                raw = fit_details["raw_params"]
                
                # Case-insensitive parameter lookup
                h0_best = None
                s8_best = None
                sigma8_best = None
                omega_m_best = None
                for k, v in raw.items():
                    k_lower = k.lower()
                    if k_lower == 'h0':
                        h0_best = v
                    elif k_lower == 's8':
                        s8_best = v
                    elif k_lower == 'sigma8':
                        sigma8_best = v
                    elif k_lower in ('omega_m', 'omegam'):
                        omega_m_best = v
                
                if s8_best is None:
                    if sigma8_best is not None and omega_m_best is not None:
                        s8_best = sigma8_best * (omega_m_best / 0.3)**0.5
                
                if h0_val is None:
                    h0_val = h0_best
                if s8_val is None:
                    s8_val = s8_best
            
        if h0_val is not None and s8_val is not None:
            # Reference values for direct cosmological measurements
            PLANCK_H0 = 67.36
            PLANCK_H0_ERR = 0.54
            SHOES_H0 = 73.04
            SHOES_H0_ERR = 1.04

            PLANCK_S8 = 0.832
            PLANCK_S8_ERR = 0.013
            KIDS_S8 = 0.759
            KIDS_S8_ERR = 0.024
            DES_S8 = 0.776
            DES_S8_ERR = 0.017

            # Check H0
            if h0_err is not None:
                # Statistical check: resolves tension if within 2.0-sigma of local measurement (SH0ES)
                nsigma_h0 = abs(h0_val - SHOES_H0) / (h0_err**2 + SHOES_H0_ERR**2)**0.5
                h0_solved = nsigma_h0 < 2.0
            else:
                h0_solved = h0_val >= 70.0

            # Check S8
            if s8_err is not None:
                # Statistical check: resolves tension if within 2.0-sigma of weak-lensing measurements (KiDS or DES)
                nsigma_kids = abs(s8_val - KIDS_S8) / (s8_err**2 + KIDS_S8_ERR**2)**0.5
                nsigma_des = abs(s8_val - DES_S8) / (s8_err**2 + DES_S8_ERR**2)**0.5
                s8_solved = (nsigma_kids < 2.0) or (nsigma_des < 2.0)
            else:
                s8_solved = s8_val <= 0.80

            if h0_solved and s8_solved:
                stats_data["tension_status"] = "Both Solved!"
            elif h0_solved:
                stats_data["tension_status"] = "H0 Solved (S8 Unsolved)"
            elif s8_solved:
                stats_data["tension_status"] = "S8 Solved (H0 Unsolved)"
            else:
                stats_data["tension_status"] = "Both Unsolved"

        # Check model struggles (only apply struggle if model CANNOT calculate it)
        log_file = Path(f"{ACTIVE_OUTPUT_PREFIX}.log")
        struggles = extract_model_struggles(str(log_file))
        stats_data["struggles"] = struggles

        # Check neutrino sector configuration
        ncdm_mass = None
        ncdm_num = 0
        ncdm_fluid_approx = None
        q_bins = None
        l_max_ncdm = None
        updated_yaml = Path(f"{ACTIVE_OUTPUT_PREFIX}.updated.yaml")
        if updated_yaml.exists():
            try:
                with open(updated_yaml, 'r') as f:
                    up_cfg = yaml.safe_load(f)
                classy_cfg = up_cfg.get('theory', {}).get('classy', {})
                extra_args = classy_cfg.get('extra_args', {})
                ncdm_num = int(extra_args.get('N_ncdm', 0))
                ncdm_fluid_approx = extra_args.get('ncdm_fluid_approximation', None)
                q_bins = extra_args.get('q_bins', None)
                if q_bins is None:
                    q_bins = extra_args.get('q_bins_ncdm', None)
                l_max_ncdm = extra_args.get('l_max_ncdm', None)
                
                params = up_cfg.get('params', {})
                if 'm_ncdm' in params:
                    p_val = params['m_ncdm']
                    if isinstance(p_val, dict):
                        ncdm_mass = p_val.get('ref', 0.06)
                    else:
                        ncdm_mass = p_val
            except Exception:
                pass

        if fit_details is not None and "raw_params" in fit_details:
            raw = fit_details["raw_params"]
            # Case-insensitive check for m_ncdm parameter
            for k, v in raw.items():
                if k.lower() == 'm_ncdm':
                    ncdm_mass = v
                    break

        stats_data["ncdm_status"] = {
            "enabled": (ncdm_num > 0) or (ncdm_mass is not None),
            "mass": ncdm_mass,
            "struggles": struggles.get("NCDM (Massive Neutrinos)", 0),
            "fluid_approx": ncdm_fluid_approx,
            "q_bins": q_bins,
            "l_max_ncdm": l_max_ncdm
        }
            
    # Read terminal output log
    if ACTIVE_OUTPUT_PREFIX:
        log_file = Path(f"{ACTIVE_OUTPUT_PREFIX}.log")
        if log_file.exists():
            try:
                file_size = os.path.getsize(log_file)
                with open(log_file, 'r') as f:
                    if file_size > 10000:
                        f.seek(file_size - 10000)
                        f.readline() # skip partial line
                    stats_data["terminal_output"] = [line.strip() for line in f.readlines()[-100:]]
            except Exception:
                pass

    init_percent = 0
    if CURRENT_STATUS in ["running", "completed"]:
        if stats_data.get("dead_points", 0) > 0 or CURRENT_STATUS == "completed":
            init_percent = 100
        else:
            # Parse initialization percent from the active log file
            terminal_init_percent = 0
            if ACTIVE_OUTPUT_PREFIX:
                log_file = Path(f"{ACTIVE_OUTPUT_PREFIX}.log")
                if log_file.exists():
                    try:
                        file_size = os.path.getsize(log_file)
                        with open(log_file, "r") as lf:
                            if file_size > 50000:
                                lf.seek(file_size - 50000)
                                lf.readline() # skip partial line
                            for line in lf:
                                match = re.search(r"(\d+)%\s*\|", line)
                                if match:
                                    terminal_init_percent = int(match.group(1))
                    except Exception:
                        pass
            init_percent = terminal_init_percent

    stats_data["init_percent"] = init_percent if CURRENT_STATUS != "idle" else 0

    return stats_data

@app.get("/api/baselines")
async def get_baselines():
    """Retrieves the baseline values from the database."""
    baseline_file = Path("scripts/baseline_database.json")
    if not baseline_file.exists():
        raise HTTPException(status_code=404, detail="Baseline database not found.")
    try:
        with open(baseline_file, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error decoding baseline database JSON.")

@app.post("/api/update_baseline")
async def update_baseline(data: UpdateBaseline):
    """Updates the JSON database with a new baseline score."""
    baseline_file = Path("scripts/baseline_database.json")
    baselines = {}
    if baseline_file.exists():
        with open(baseline_file, 'r') as f:
            baselines = json.load(f)
            
    baselines[data.dataset] = {
        "log_evidence": data.log_evidence,
        "best_chi2": data.best_chi2
    }
    with open(baseline_file, 'w') as f:
        json.dump(baselines, f, indent=4)
    return {"message": "Baseline updated successfully."}

@app.post("/api/upload_config")
async def upload_config(file: UploadFile = File(...)):
    """Uploads and saves the configuration YAML file."""
    if not file.filename.endswith(".yaml"):
        raise HTTPException(status_code=400, detail="Only .yaml files are allowed.")

    upload_path = Path("uploaded_config.yaml")
    try:
        with open(upload_path, 'wb') as f:
            shutil.copyfileobj(file.file, f)
        return {"filename": file.filename, "message": "Configuration uploaded successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not save uploaded file: {e}")

@app.post("/api/start_run")
async def start_run(config: RunConfig):
    """Starts a Cobaya run with the specified configuration."""
    global RUNNING_PROCESS, MONITOR_PROCESS, ACTIVE_OUTPUT_PREFIX, EXTERNAL_LOGS, ACTIVE_YAML_PATH, CURRENT_STATUS, WATCHDOG_ALERTS, RUN_START_TIME, LOG_FILE_POSITION, BEST_FIT_LOG_CACHE, RAW_FILE_POSITIONS, BEST_FIT_FILE_CACHE
    LOG_FILE_POSITION = 0
    BEST_FIT_LOG_CACHE = None
    RAW_FILE_POSITIONS = {}
    BEST_FIT_FILE_CACHE = {}

    # Ensure cores does not exceed logical CPU count to prevent performance degradation from context-switching
    max_logical_cores = psutil.cpu_count(logical=True) or 4
    if config.cores > max_logical_cores:
        config.cores = max_logical_cores

    if RUNNING_PROCESS and RUNNING_PROCESS.poll() is None:
        raise HTTPException(status_code=409, detail="A run is already in progress.")

    config_file = Path(config.config_name)
    if not config_file.exists():
        raise HTTPException(status_code=404, detail=f"Configuration file '{config.config_name}' not found.")

    # Auto-rebuild logic
    if config.auto_rebuild:
        print(f"\n[{time.strftime('%X')}] --- AUTO-REBUILD TRIGGERED BEFORE RUN ---")
        print(f"[{time.strftime('%X')}] Running 'make clean && make -j{config.cores}' with optimized flags...")
        start_build = time.time()
        make_process = subprocess.run(
            f"export CFLAGS='-O3 -march=native -ffast-math -ftree-vectorize' && "
            f"export CXXFLAGS='-O3 -march=native -ffast-math -ftree-vectorize' && "
            f"make clean && make -j{config.cores}",
            shell=True, capture_output=True, text=True
        )
        build_time = time.time() - start_build
        
        if make_process.returncode != 0:
            print(f"[{time.strftime('%X')}] ERROR: Auto-compilation failed!\n{make_process.stderr}")
            raise HTTPException(status_code=500, detail=f"Auto-build failed: {make_process.stderr}")

        print(f"[{time.strftime('%X')}] SUCCESS: CLASS auto-rebuilt in {build_time:.1f} seconds!")
        print(f"[{time.strftime('%X')}] ------------------------------------\n")

    conda_env_path = os.environ.get("CONDA_PREFIX", "")
    python_executable = os.path.join(conda_env_path, "bin", "python3") if conda_env_path else "python3"
    mpirun_executable = os.path.join(conda_env_path, "bin", "mpirun") if conda_env_path else "mpirun"
    cobaya_packages_path = os.path.join(os.path.expanduser("~"), "cobaya_packages_clean")

    EXTERNAL_LOGS.clear()
    WATCHDOG_ALERTS.clear()
    ACTIVE_OUTPUT_PREFIX = get_output_prefix_from_yaml(str(config_file))
    ACTIVE_YAML_PATH = str(config_file)

    # Ensure the output directory exists so `tee` doesn't fail instantly
    output_dir = Path(ACTIVE_OUTPUT_PREFIX).parent
    output_dir.mkdir(parents=True, exist_ok=True)

    # Delete any lock files if they exist so we can safely resume
    for lock_file in output_dir.glob("*.locked"):
        try:
            lock_file.unlink()
        except Exception:
            pass

    # Determine if we should force-overwrite (-f) or resume (-r)
    force_over = config.force_overwrite if config.force_overwrite is not None else config.auto_rebuild
    run_flag = "-f" if force_over else "-r"

    # Delete the old log file if we are doing a fresh start
    if force_over:
        log_file = Path(f"{ACTIVE_OUTPUT_PREFIX}.log")
        if log_file.exists():
            try:
                log_file.unlink()
            except Exception:
                pass

    # Use tee -a (append) so truncating the file mid-run doesn't create sparse files full of null bytes
    # Added -bind-to core to pin MPI processes to physical cores for optimal cache usage and performance.
    command = (
        f"unset OMPI_COMM_WORLD_SIZE && "
        f"{mpirun_executable} -bind-to core -genv OMP_NUM_THREADS 1 -genv MKL_NUM_THREADS 1 -genv OPENBLAS_NUM_THREADS 1 -genv NUMEXPR_NUM_THREADS 1 -genv VECLIB_MAXIMUM_THREADS 1 -np {config.cores} "
        f"{python_executable} -m cobaya run {config_file} --packages-path {cobaya_packages_path} {run_flag} 2>&1 | tee -a {ACTIVE_OUTPUT_PREFIX}.log"
    )

    try:
        CURRENT_STATUS = "running"
        RUN_START_TIME = time.time()
        RUNNING_PROCESS = subprocess.Popen(command, shell=True, preexec_fn=os.setsid)
        
        # Automatically launch the monitor script to run GetDist and generate live plots
        monitor_command = f"{python_executable} plot_chains.py --config {config_file} --monitor-and-stop --interval 150"
        MONITOR_PROCESS = subprocess.Popen(monitor_command, shell=True, preexec_fn=os.setsid)
        
        return {"message": f"Cobaya run started with config '{config.config_name}'.", "pid": RUNNING_PROCESS.pid}
    except Exception as e:
        CURRENT_STATUS = "failed"
        raise HTTPException(status_code=500, detail=f"Failed to start Cobaya run: {e}")

@app.post("/api/stop_run")
async def stop_run():
    """Stops the currently running Cobaya process group."""
    global RUNNING_PROCESS, MONITOR_PROCESS, CURRENT_STATUS

    if not RUNNING_PROCESS or RUNNING_PROCESS.poll() is not None:
        return {"message": "No run is currently active."}

    try:
        # Ask psutil to mercilessly kill the shell and all child mpirun/python processes
        parent = psutil.Process(RUNNING_PROCESS.pid)
        for child in parent.children(recursive=True):
            child.kill()
        parent.kill()
        
        # Send SIGKILL to the process group as an absolute fallback
        os.killpg(os.getpgid(RUNNING_PROCESS.pid), signal.SIGKILL)
    except (psutil.NoSuchProcess, ProcessLookupError):
        pass # Process already gone
    except Exception as e:
        print(f"Error stopping process tree: {e}")
    finally:
        RUNNING_PROCESS = None
        CURRENT_STATUS = "stopped"
        
    # Kill the background monitor process as well
    if MONITOR_PROCESS:
        try:
            mparent = psutil.Process(MONITOR_PROCESS.pid)
            for mchild in mparent.children(recursive=True):
                mchild.kill()
            mparent.kill()
            os.killpg(os.getpgid(MONITOR_PROCESS.pid), signal.SIGKILL)
        except (psutil.NoSuchProcess, ProcessLookupError):
            pass
        except Exception as e:
            print(f"Error stopping monitor tree: {e}")
        finally:
            MONITOR_PROCESS = None

    return {"message": "Cobaya run stop signal sent."}

@app.post("/api/log")
async def add_external_log(log: LogMessage):
    """Receives log messages from external scripts (like the boundary monitor)."""
    EXTERNAL_LOGS.append(log.message)
    return {"message": "Log recorded."}

@app.post("/api/watchdog")
async def update_watchdog(report: WatchdogReport):
    """Receives structured alerts from the boundary monitor."""
    global WATCHDOG_ALERTS
    WATCHDOG_ALERTS = [alert.dict() for alert in report.alerts]
    return {"message": "Watchdog report updated."}

@app.post("/api/apply_priors_and_restart")
async def apply_priors_and_restart(req: ApplyPriorsRequest):
    """Applies the user-accepted prior changes to the YAML and cleanly restarts the run."""
    yaml_path = Path(req.config_name)
    if not yaml_path.exists():
        raise HTTPException(status_code=404, detail="Configuration file not found.")
        
    try:
        with open(yaml_path, 'r') as f:
            config = yaml.safe_load(f)
            
        for param, bounds in req.updates.items():
            if param in config.get('params', {}) and isinstance(config['params'][param], dict):
                if 'prior' in config['params'][param] and isinstance(config['params'][param]['prior'], dict):
                    config['params'][param]['prior']['min'] = bounds['min']
                    config['params'][param]['prior']['max'] = bounds['max']
                    
        with open(yaml_path, 'w') as f:
            yaml.dump(config, f, default_flow_style=False, sort_keys=False)
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update YAML: {e}")
        
    async def perform_restart():
        await stop_run()
        await asyncio.sleep(3)
        run_config = RunConfig(config_name=req.config_name, auto_rebuild=False, force_overwrite=True)
        await start_run(run_config)
        
    asyncio.create_task(perform_restart())
    return {"message": "Priors updated and restart sequence initiated."}

@app.get("/api/download_chains")
async def download_chains():
    """Zips and downloads the chains directory."""
    if not Path("chains").exists():
        raise HTTPException(status_code=404, detail="No chains directory found.")
    try:
        archive_path = shutil.make_archive("CosmicDashboard_Data", "zip", "chains")
        return FileResponse(archive_path, media_type="application/zip", filename="CosmicDashboard_Data.zip")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating archive: {e}")

@app.get("/api/live_plot")
async def get_live_plot():
    """Serves the latest posterior plot generated by the monitor script."""
    plot_path = Path("prtoe_posteriors.png")
    if plot_path.exists():
        return FileResponse(plot_path)
    raise HTTPException(status_code=404, detail="Plot not found")

# --- Serve Dashboard UI ---
if Path("dashboard").exists():
    app.mount("/", StaticFiles(directory="dashboard", html=True), name="dashboard")

# --- Main execution block ---
if __name__ == "__main__":
    scripts_dir = Path("scripts")
    scripts_dir.mkdir(exist_ok=True)

    baseline_db_file = scripts_dir / "baseline_database.json"
    if not baseline_db_file.exists():
        dummy_baselines = {}
        with open(baseline_db_file, 'w') as f:
            json.dump(dummy_baselines, f, indent=4)
        print(f"Created dummy baseline database: {baseline_db_file}")

    print("Starting CosmicDashboard backend server on http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000, access_log=False)