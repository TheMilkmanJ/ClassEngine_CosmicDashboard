const API_URL = 'http://localhost:8000';
let statusInterval = null;
let activeConfig = 'uploaded_config.yaml';

// DOM Elements
const statusDot = document.getElementById('status-dot');
const statusText = document.getElementById('status-text');

const yamlZone = document.getElementById('yaml-upload-zone');
const yamlInput = document.getElementById('yaml-input');
const yamlName = document.getElementById('yaml-name');

const codeZone = document.getElementById('code-upload-zone');
const codeInput = document.getElementById('code-input');
const codeName = document.getElementById('code-name');

const btnRebuild = document.getElementById('btn-rebuild');
const btnStart = document.getElementById('btn-start');
const btnStop = document.getElementById('btn-stop');

const statDead = document.getElementById('stat-dead');
const statEvidence = document.getElementById('stat-evidence');
const progressFill = document.getElementById('progress-fill');
const progressPercent = document.getElementById('progress-percent');
const consoleBody = document.getElementById('console-body');

const valBaseline = document.getElementById('val-baseline');
const valCustom = document.getElementById('val-custom');
const valDelta = document.getElementById('val-delta');

const jeffreysCard = document.getElementById('jeffreys-card');
const jeffreysText = document.getElementById('jeffreys-text');
const jeffreysDesc = document.getElementById('jeffreys-desc');
const datasetSelect = document.getElementById('dataset-select');

// Initial setup
document.addEventListener('DOMContentLoaded', () => {
    fetchBaselines();
    checkStatus();
    statusInterval = setInterval(checkStatus, 3000);
});

// File Upload Zones
setupUploadZone(yamlZone, yamlInput, handleYamlUpload);
setupUploadZone(codeZone, codeInput, handleCodeSelected);

function setupUploadZone(zone, input, handler) {
    zone.addEventListener('click', () => input.click());
    zone.addEventListener('dragover', (e) => {
        e.preventDefault();
        zone.classList.add('active');
    });
    zone.addEventListener('dragleave', () => zone.classList.remove('active'));
    zone.addEventListener('drop', (e) => {
        e.preventDefault();
        zone.classList.remove('active');
        if (e.dataTransfer.files.length > 0) {
            input.files = e.dataTransfer.files;
            handler(e.dataTransfer.files[0]);
        }
    });
    input.addEventListener('change', () => {
        if (input.files.length > 0) {
            handler(input.files[0]);
        }
    });
}

// YAML Configuration upload
async function handleYamlUpload(file) {
    yamlName.textContent = file.name;
    yamlName.classList.add('active');
    appendLog(`Selected configuration: ${file.name}`);
    
    const formData = new FormData();
    formData.append('file', file);
    
    try {
        appendLog('Uploading configuration to server...');
        const response = await fetch(`${API_URL}/api/upload_config`, {
            method: 'POST',
            body: formData
        });
        const data = await response.json();
        if (response.ok) {
            appendLog(`Configuration uploaded successfully. Config loaded.`);
            activeConfig = 'uploaded_config.yaml';
        } else {
            appendLog(`Upload failed: ${data.detail}`);
        }
    } catch (err) {
        appendLog(`Upload error: ${err.message}`);
    }
}

// Source Code file selected
function handleCodeSelected(file) {
    codeName.textContent = file.name;
    codeName.classList.add('active');
    btnRebuild.disabled = false;
    appendLog(`Selected source code: ${file.name}. Ready to upload & rebuild.`);
}

// Rebuild CLASS with uploaded code
btnRebuild.addEventListener('click', async () => {
    const file = codeInput.files[0];
    if (!file) return;
    
    btnRebuild.disabled = true;
    btnRebuild.textContent = "Uploading & Rebuilding...";
    appendLog(`Uploading ${file.name} and triggering re-compilation...`);
    
    const formData = new FormData();
    formData.append('file', file);
    
    try {
        const response = await fetch(`${API_URL}/api/upload_code`, {
            method: 'POST',
            body: formData
        });
        const data = await response.json();
        if (response.ok) {
            appendLog(`Success: CLASS rebuild completed.`);
            if (data.details) {
                appendLog(data.details);
            }
        } else {
            appendLog(`Rebuild failed: ${data.detail}`);
        }
    } catch (err) {
        appendLog(`Rebuild error: ${err.message}`);
    } finally {
        btnRebuild.textContent = "Upload & Rebuild CLASS";
        btnRebuild.disabled = false;
    }
});

// Start Run
btnStart.addEventListener('click', async () => {
    btnStart.disabled = true;
    appendLog(`Starting PolyChord nested sampling with config: ${activeConfig}...`);
    
    try {
        const response = await fetch(`${API_URL}/api/start_run`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ config_name: activeConfig })
        });
        const data = await response.json();
        if (response.ok) {
            appendLog(`Process started in background. PID: ${data.pid}`);
            checkStatus();
        } else {
            appendLog(`Failed to start: ${data.detail}`);
            btnStart.disabled = false;
        }
    } catch (err) {
        appendLog(`Execution error: ${err.message}`);
        btnStart.disabled = false;
    }
});

// Stop Run
btnStop.addEventListener('click', async () => {
    btnStop.disabled = true;
    appendLog('Sending termination signal to sampler process group...');
    
    try {
        const response = await fetch(`${API_URL}/api/stop_run`, {
            method: 'POST'
        });
        const data = await response.json();
        if (response.ok) {
            appendLog('Process group stopped successfully.');
            checkStatus();
        } else {
            appendLog(`Failed to stop process: ${data.detail}`);
            btnStop.disabled = false;
        }
    } catch (err) {
        appendLog(`Abort error: ${err.message}`);
        btnStop.disabled = false;
    }
});

// Fetch baseline evidence from server
async function fetchBaselines() {
    try {
        const response = await fetch(`${API_URL}/api/baselines`);
        const data = await response.json();
        const baseline = data[datasetSelect.value];
        valBaseline.textContent = baseline.toFixed(4);
    } catch (err) {
        console.error('Error fetching baselines:', err);
    }
}

datasetSelect.addEventListener('change', fetchBaselines);

// Check current status
async function checkStatus() {
    try {
        const response = await fetch(`${API_URL}/api/status`);
        if (!response.ok) return;
        const data = await response.json();
        
        // Update status indicator
        updateStatusIndicator(data.status);
        
        // Update stats
        statDead.textContent = data.dead_points;
        if (data.log_evidence !== null) {
            statEvidence.textContent = `${data.log_evidence.toFixed(2)} +/- ${data.log_evidence_error.toFixed(2)}`;
            valCustom.textContent = data.log_evidence.toFixed(4);
        } else {
            statEvidence.textContent = "-";
            valCustom.textContent = "-";
        }
        
        // Update progress bar (assuming ~3000 points for convergence)
        const totalEstimated = 3000;
        let percent = Math.min(Math.floor((data.dead_points / totalEstimated) * 100), 99);
        if (data.status === 'completed') percent = 100;
        if (data.status === 'idle') percent = 0;
        
        progressFill.style.width = `${percent}%`;
        progressPercent.textContent = `${percent}%`;
        
        // Handle actions availability
        if (data.status === 'running') {
            btnStart.disabled = true;
            btnStop.disabled = false;
            if (data.dead_points > 0) {
                appendLog(`Sampling... Dead points: ${data.dead_points}, Current log(Z): ${data.log_evidence || 'evaluating'}`);
            } else {
                appendLog('Initializing live points...');
            }
        } else {
            btnStart.disabled = false;
            btnStop.disabled = true;
        }
        
        // If completed, compute evidence comparison
        if (data.status === 'completed' && data.log_evidence !== null) {
            calculateEvidence(data.log_evidence);
        }
        
    } catch (err) {
        console.error('Status check error:', err);
    }
}

// Update UI indicator
function updateStatusIndicator(status) {
    statusDot.className = 'status-dot';
    statusText.textContent = `SYSTEM ${status.toUpperCase()}`;
    
    if (status === 'idle') statusDot.classList.add('status-idle');
    else if (status === 'running') statusDot.classList.add('status-running');
    else if (status === 'completed') statusDot.classList.add('status-completed');
    else if (status === 'stopped' || status === 'failed') statusDot.classList.add('status-failed');
}

// Calculate delta ln Z and update Jeffreys card
function calculateEvidence(customLogZ) {
    const baselineLogZ = parseFloat(valBaseline.textContent);
    const delta = customLogZ - baselineLogZ;
    valDelta.textContent = (delta >= 0 ? '+' : '') + delta.toFixed(4);
    
    // Clear old classes
    jeffreysCard.className = 'jeffreys-card';
    
    if (delta >= 10.0) {
        jeffreysCard.classList.add('jeffreys-decisive');
        jeffreysText.textContent = 'Decisive Evidence';
        jeffreysDesc.textContent = 'The custom model is decisively favored over standard ΛCDM by the datasets. The parameter space changes provide a significantly superior fit.';
    } else if (delta >= 5.0) {
        jeffreysCard.classList.add('jeffreys-strong');
        jeffreysText.textContent = 'Strong Evidence';
        jeffreysDesc.textContent = 'There is strong statistical evidence favoring the custom model configuration. The modifications fit the observational constraints better.';
    } else if (delta >= 0.0) {
        jeffreysCard.classList.add('jeffreys-inconclusive');
        jeffreysText.textContent = 'Inconclusive';
        jeffreysDesc.textContent = 'The statistical fit is comparable to standard ΛCDM. The custom model is not significantly favored or disfavored by the data.';
    } else {
        jeffreysCard.classList.add('jeffreys-disfavored');
        jeffreysText.textContent = 'Model Disfavored';
        jeffreysDesc.textContent = 'The custom parameters are statistically disfavored by the datasets. The model fit is worse than the standard ΛCDM baseline.';
    }
}

// Console helper
function appendLog(message) {
    const lines = consoleBody.innerHTML.split('<br>');
    // Limit console buffer to 100 lines
    if (lines.length > 100) {
        lines.shift();
    }
    consoleBody.innerHTML = lines.join('<br>') + `<br>[${new Date().toLocaleTimeString()}] ${message}`;
    consoleBody.scrollTop = consoleBody.scrollHeight;
}
