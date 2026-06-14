import os
import subprocess
import signal
import json
import yaml
from fastapi import FastAPI, UploadFile, File, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="CosmoDashboard API", description="Backend API for CLASS/Cobaya model testing")

# Enable CORS for frontend dashboard access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PROJECT_DIR = "/mnt/c/Users/themi/projects/prtoe_class"
CHUNKS_DIR = os.path.join(PROJECT_DIR, "chains")
DATABASE_PATH = os.path.join(PROJECT_DIR, "scripts", "baseline_database.json")

# Global dictionary to track the running process
run_state = {
    "process": None,
    "active_config": None,
    "status": "idle",
    "log_output": []
}

class StartRunRequest(BaseModel):
    config_name: str  # e.g. "uploaded_config.yaml" or "cobaya_prtoe_optimized.yaml"

@app.get("/api/baselines")
def get_baselines():
    """Read and return the pre-computed baseline evidences database."""
    if not os.path.exists(DATABASE_PATH):
        return {"planck_bao_pantheon": -1683.2451}
    try:
        with open(DATABASE_PATH, "r") as f:
            return json.load(f)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to read baseline database: {str(e)}")

@app.post("/api/upload_config")
async def upload_config(file: UploadFile = File(...)):
    """Upload a Cobaya YAML configuration file."""
    if not file.filename.endswith(('.yaml', '.yml')):
        raise HTTPException(status_code=400, detail="Only YAML files are allowed.")
    
    os.makedirs(CHUNKS_DIR, exist_ok=True)
    target_path = os.path.join(PROJECT_DIR, "chains", "uploaded_config.yaml")
    
    try:
        contents = await file.read()
        # Validate that it is valid YAML
        config_data = yaml.safe_load(contents)
        
        with open(target_path, "wb") as f:
            f.write(contents)
            
        return {"status": "success", "filename": "uploaded_config.yaml", "config": config_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to upload YAML config: {str(e)}")

@app.post("/api/upload_code")
async def upload_code(file: UploadFile = File(...)):
    """Upload a custom Python wrapper or C source file, and trigger a rebuild."""
    filename = file.filename
    if filename.endswith(".c"):
        target_path = os.path.join(PROJECT_DIR, "source", filename)
    elif filename.endswith(".py"):
        target_path = os.path.join(PROJECT_DIR, "python", filename)
    else:
        raise HTTPException(status_code=400, detail="Only .c and .py files are supported.")

    try:
        contents = await file.read()
        # Backup existing file if it exists
        if os.path.exists(target_path):
            os.rename(target_path, target_path + ".bak")
            
        with open(target_path, "wb") as f:
            f.write(contents)
            
        # Rebuild CLASS using Makefile
        rebuild_log = []
        if filename.endswith(".c"):
            # Run make clean && make
            cmd = f"cd {PROJECT_DIR} && make clean && make"
            process = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            rebuild_log.append(process.stdout)
            if process.returncode != 0:
                # Restore backup
                if os.path.exists(target_path + ".bak"):
                    os.replace(target_path + ".bak", target_path)
                raise HTTPException(status_code=500, detail=f"Rebuild failed: {process.stderr}")

        return {"status": "success", "rebuild": "completed", "details": "\n".join(rebuild_log)}
    except Exception as e:
         raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/start_run")
def start_run(req: StartRunRequest):
    """Launch the Cobaya nested sampling run in the background."""
    if run_state["status"] == "running":
        raise HTTPException(status_code=400, detail="A run is already active.")

    config_path = os.path.join(PROJECT_DIR, req.config_name)
    if not os.path.exists(config_path):
        # Check chains folder
        config_path = os.path.join(PROJECT_DIR, "chains", req.config_name)
        if not os.path.exists(config_path):
            raise HTTPException(status_code=404, detail=f"Configuration file {req.config_name} not found.")

    # Build command line
    cmd = (
        f"/home/themilkmanj/miniconda3/envs/pgtoe_gold/bin/mpirun "
        f"-genv OMP_NUM_THREADS 1 -np 12 "
        f"/home/themilkmanj/miniconda3/envs/pgtoe_gold/bin/python3 -m cobaya run {config_path} "
        f"--packages-path /home/themilkmanj/cobaya_packages_clean -f"
    )

    try:
        # Launch subprocess
        proc = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            preexec_fn=os.setsid,  # Create process group for easy termination
            text=True
        )
        
        run_state["process"] = proc
        run_state["active_config"] = req.config_name
        run_state["status"] = "running"
        
        return {"status": "started", "config": req.config_name, "pid": proc.pid}
    except Exception as e:
        run_state["status"] = "failed"
        raise HTTPException(status_code=500, detail=f"Failed to start run: {str(e)}")

@app.get("/api/status")
def get_status():
    """Retrieve the current sampler status, log-evidence estimates, and point counts."""
    # Check if process is still active
    proc = run_state["process"]
    if proc is not None:
        poll = proc.poll()
        if poll is not None:
            # Process terminated
            run_state["status"] = "completed" if poll == 0 else "failed"
            run_state["process"] = None

    # Load active progress
    dead_count = 0
    live_count = 0
    logz = None
    logz_err = None
    
    # We parse the raw output files from PolyChord
    # We assume the YAML config defines the output prefix.
    # For uploaded_config.yaml, we check the default output directories
    raw_dir = os.path.join(PROJECT_DIR, "chains", "prtoe_poly_optimized_polychord_raw")
    if not os.path.exists(raw_dir):
        raw_dir = os.path.join(PROJECT_DIR, "lcdm_poly_polychord_raw") # Fallback to standard baseline folder

    stats_path = os.path.join(raw_dir, "prtoe_poly.stats")
    if not os.path.exists(stats_path):
        stats_path = os.path.join(raw_dir, "lcdm_poly.stats")

    dead_path = os.path.join(raw_dir, "prtoe_poly_dead.txt")
    if not os.path.exists(dead_path):
        dead_path = os.path.join(raw_dir, "lcdm_poly_dead.txt")

    # Read dead points
    if os.path.exists(dead_path):
        try:
            with open(dead_path, "r") as f:
                dead_count = sum(1 for line in f)
        except:
            pass

    # Read stats
    if os.path.exists(stats_path):
        try:
            with open(stats_path, "r") as f:
                for line in f:
                    if "log(Z)" in line and "+/-" in line:
                        parts = line.split("=")
                        val_err = parts[1].split("+/-")
                        logz = float(val_err[0].strip())
                        logz_err = float(val_err[1].strip())
                        break
        except:
            pass

    return {
        "status": run_state["status"],
        "active_config": run_state["active_config"],
        "dead_points": dead_count,
        "log_evidence": logz,
        "log_evidence_error": logz_err
    }

@app.post("/api/stop_run")
def stop_run():
    """Kill the active Cobaya process group."""
    proc = run_state["process"]
    if proc is None:
        raise HTTPException(status_code=400, detail="No run is currently active.")

    try:
        # Kill the entire process group (negative PID kills the group under setsid)
        os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
        run_state["status"] = "stopped"
        run_state["process"] = None
        return {"status": "stopped"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to kill process: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
