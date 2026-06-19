const API_URL = window.location.protocol === 'file:' ? 'http://localhost:8000' : window.location.origin;
let statusInterval = null;
let activeConfig = 'lcdm_config.yaml';
let lastStatusData = null;
let baselineBestChi2 = null;
let baselineLogEvidence = null;

// DOM Elements
const statusDot = document.getElementById('status-dot');
const statusText = document.getElementById('status-text');

const yamlZone = document.getElementById('yaml-upload-zone');
const yamlInput = document.getElementById('yaml-input');
const yamlName = document.getElementById('yaml-name');
const btnResetYaml = document.getElementById('btn-reset-yaml');

const btnStart = document.getElementById('btn-start');
const btnResume = document.getElementById('btn-resume');
const btnStop = document.getElementById('btn-stop');
const btnDownload = document.getElementById('btn-download');

const statDead = document.getElementById('stat-dead');
const statEvidence = document.getElementById('stat-evidence');
const statChi2 = document.getElementById('stat-chi2');
const statChi2Cmb = document.getElementById('stat-chi2-cmb');
const statChi2Bao = document.getElementById('stat-chi2-bao');
const statChi2Sn = document.getElementById('stat-chi2-sn');
const statRawParams = document.getElementById('stat-raw-params');
const statCpu = document.getElementById('stat-cpu');
const cpuGaugePath = document.getElementById('cpu-gauge-path');
const progressFill = document.getElementById('progress-fill');
const progressPercent = document.getElementById('progress-percent');
const consoleBody = document.getElementById('console-body');

const classyBadge = document.getElementById('classy-badge');
const initFill = document.getElementById('init-fill');
const initPercent = document.getElementById('init-percent');
const statSpeed = document.getElementById('stat-speed');
const statEta = document.getElementById('stat-eta');
const constraintsCard = document.getElementById('constraints-card');
const constraintsBody = document.getElementById('constraints-body');
const tensionsCard = document.getElementById('tensions-card');
const statTensionsBadge = document.getElementById('stat-tensions-badge');
const statStrugglesBody = document.getElementById('stat-struggles-body');

let localLogs = ['Waiting for run execution...'];
let lastTerminalLogs = [];
let plotCheckCounter = 0;

const plotContainer = document.getElementById('live-plot-container');
const plotImg = document.getElementById('live-plot-img');
const plotTimestamp = document.getElementById('plot-timestamp');

const valBaseline = document.getElementById('val-baseline');
const valCustom = document.getElementById('val-custom');
const valDelta = document.getElementById('val-delta');

const jeffreysCard = document.getElementById('jeffreys-card');
const jeffreysText = document.getElementById('jeffreys-text');
const jeffreysDesc = document.getElementById('jeffreys-desc');

const watchdogCard = document.getElementById('watchdog-card');
const watchdogText = document.getElementById('watchdog-text');
const watchdogDesc = document.getElementById('watchdog-desc');
const watchdogIcon = document.getElementById('watchdog-icon');

const inputCores = document.getElementById('input-cores');
const checkAutoRebuild = document.getElementById('check-autorebuild');
const checkAutoRunLcdm = document.getElementById('check-autorun-lcdm');

let currentProposedUpdates = {};
let watchdogIgnored = false; // Flag to temporarily ignore watchdog
let lastWatchdogAlertCount = 0; // Track watchdog alert count for audio alerts

// Initial setup
document.addEventListener('DOMContentLoaded', () => {
    fetchBaselines();
    checkStatus();
    statusInterval = setInterval(checkStatus, 3000);
    fetchSysInfo();
    
    // Toggle Neutrino Details
    const statNcdmHeader = document.getElementById('stat-ncdm-header');
    const statNcdmDetails = document.getElementById('stat-ncdm-details');
    const statNcdmArrow = document.getElementById('stat-ncdm-arrow');
    if (statNcdmHeader && statNcdmDetails && statNcdmArrow) {
        statNcdmHeader.addEventListener('click', () => {
            const isHidden = statNcdmDetails.style.display === 'none';
            statNcdmDetails.style.display = isHidden ? 'flex' : 'none';
            statNcdmArrow.style.transform = isHidden ? 'rotate(90deg)' : 'rotate(0deg)';
        });
    }
});

function switchToLcdm() {
    activeConfig = 'lcdm_config.yaml';
    yamlName.textContent = 'Default: lcdm_config.yaml';
    yamlName.classList.remove('active');
    yamlInput.value = '';
    appendLog(`Reverted to default ΛCDM configuration: lcdm_config.yaml`);
}

// Reset to ΛCDM
btnResetYaml.addEventListener('click', (e) => {
    e.preventDefault();
    switchToLcdm();
});

// Fetch active CLASS engine version
async function fetchSysInfo() {
    try {
        const response = await fetch(`${API_URL}/api/sysinfo`);
        const data = await response.json();
        classyBadge.textContent = `Engine: ${data.version}`;
        if (data.version.includes("PRTOE")) {
            classyBadge.style.borderColor = "#ff9ff3";
            classyBadge.style.color = "#ff9ff3";
            classyBadge.style.background = "rgba(255, 159, 243, 0.1)";
        } else {
            classyBadge.style.borderColor = "#00d2d3";
            classyBadge.style.color = "#00d2d3";
            classyBadge.style.background = "rgba(0, 210, 211, 0.1)";
        }
    } catch (err) {
        classyBadge.textContent = "Engine: Unknown";
    }
}

// File Upload Zones
setupUploadZone(yamlZone, yamlInput, handleYamlUpload);

function setupUploadZone(zone, input, handler) {
    zone.addEventListener('click', () => {
        input.value = ''; // Reset value to force 'change' event even for the same file
        input.click();
    });
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

// Start Run
btnStart.addEventListener('click', () => triggerRun(true));
btnResume.addEventListener('click', () => triggerRun(false));

async function triggerRun(forceOverwrite) {
    btnStart.disabled = true;
    btnResume.disabled = true;
    const cores = inputCores ? (parseInt(inputCores.value) || 24) : 24;
    
    // Only auto-rebuild if it's checked AND we are starting fresh. We shouldn't rebuild mid-resume.
    const autoRebuild = (checkAutoRebuild && checkAutoRebuild.checked && forceOverwrite);
    
    if (autoRebuild) {
        appendLog(`[CLASS ENGINE] Auto-rebuilding before run using ${cores} cores...`);
    } else {
        appendLog(`[CLASS ENGINE] Auto-rebuild disabled. Resuming previous run if available...`);
    }
    appendLog(`Starting PolyChord nested sampling on ${cores} cores with config: ${activeConfig}...`);
    
    try {
        const response = await fetch(`${API_URL}/api/start_run`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 
                config_name: activeConfig,
                cores: cores,
                auto_rebuild: autoRebuild,
                force_overwrite: forceOverwrite
            })
        });
        const data = await response.json();
        if (response.ok) {
            appendLog(`Process started in background. PID: ${data.pid}`);
            if (autoRebuild) fetchSysInfo(); // Update engine badge
            checkStatus();
        } else {
            appendLog(`Failed to start: ${data.detail}`);
            btnStart.disabled = false;
            btnResume.disabled = false;
        }
    } catch (err) {
        appendLog(`Execution error: ${err.message}`);
        btnStart.disabled = false;
        btnResume.disabled = false;
    }
}

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

// Download Archive
if (btnDownload) {
    btnDownload.addEventListener('click', () => {
        appendLog('Packaging and downloading chain data archive...');
        window.location.href = `${API_URL}/api/download_chains`;
    });
}

// Fetch baseline evidence from server
async function fetchBaselines() {
    try {
        const response = await fetch(`${API_URL}/api/baselines`);
        const data = await response.json();
        const baseline = data["planck_bao_pantheonplus_shoes"];
        if (baseline !== undefined && baseline !== null) {
            if (typeof baseline === 'object') {
                baselineLogEvidence = baseline.log_evidence;
                baselineBestChi2 = baseline.best_chi2;
            } else {
                baselineLogEvidence = baseline;
                baselineBestChi2 = null;
            }
            valBaseline.textContent = baselineLogEvidence.toFixed(4);
        } else {
            valBaseline.textContent = "-";
            baselineLogEvidence = null;
            baselineBestChi2 = null;
        }
        updateEvidenceBreakdown();
    } catch (err) {
        valBaseline.textContent = "-";
        baselineLogEvidence = null;
        baselineBestChi2 = null;
        console.error('Error fetching baselines:', err);
    }
}

// Update baseline database
async function updateBaseline(dataset, evidence, chi2) {
    try {
        const response = await fetch(`${API_URL}/api/update_baseline`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ dataset: dataset, log_evidence: evidence, best_chi2: chi2 })
        });
        const data = await response.json();
        if (response.ok) {
            appendLog(`[PIPELINE] Baseline updated successfully.`);
            fetchBaselines(); // Refresh the UI value
        } else {
            appendLog(`[PIPELINE] Failed to update baseline: ${data.detail}`);
        }
    } catch (err) {
        appendLog(`[PIPELINE] Error updating baseline: ${err.message}`);
    }
}

// Check current status
async function checkStatus() {
    try {
        const response = await fetch(`${API_URL}/api/status`);
        if (!response.ok) return;
        const data = await response.json();
        lastStatusData = data;
        
        // Append external logs (from monitor script)
        if (data.external_logs && data.external_logs.length > 0) {
            data.external_logs.forEach(log => appendLog(`<span style="color: #ff4757; font-weight: bold;">[ALERT] ${log}</span>`));
        }
        
        if (data.terminal_output && data.terminal_output.length > 0) {
            lastTerminalLogs = data.terminal_output;
        } else if (data.status === 'idle') {
            lastTerminalLogs = [];
        }
        renderLogs();
        
        // Update status indicator
        updateStatusIndicator(data.status);
        
        // Update stats
        statDead.textContent = data.dead_points;
        if (data.log_evidence !== null) {
            statEvidence.textContent = `${data.log_evidence.toFixed(2)} +/- ${data.log_evidence_error.toFixed(2)}`;
            valCustom.textContent = data.log_evidence.toFixed(4);
            calculateEvidence(data.log_evidence);
        } else {
            statEvidence.textContent = "-";
            valCustom.textContent = "-";
        }
        
        if (data.best_chi2 !== null && data.best_chi2 !== undefined) {
            statChi2.textContent = data.best_chi2.toFixed(2);
            if (data.best_cmb !== null && data.best_cmb !== undefined) {
                statChi2Cmb.textContent = data.best_cmb.toFixed(1);
                statChi2Bao.textContent = data.best_bao.toFixed(1);
                statChi2Sn.textContent = data.best_sn.toFixed(1);
            }
        } else {
            statChi2.textContent = "-";
            statChi2Cmb.textContent = "-";
            statChi2Bao.textContent = "-";
            statChi2Sn.textContent = "-";
        }
        
        if (data.best_raw_params) {
            statRawParams.style.display = 'block';
            let rawHtml = '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 4px;">';
            for (const [key, val] of Object.entries(data.best_raw_params)) {
                if (!key.startsWith('chi2__') && !key.startsWith('minuslogprior')) {
                    let formattedVal = (typeof val === 'number') ? val.toPrecision(4) : val;
                    rawHtml += `<div><span style="color:#00d2d3">${key}</span>: ${formattedVal}</div>`;
                }
            }
            rawHtml += '</div>';
            statRawParams.innerHTML = rawHtml;
        } else {
            statRawParams.style.display = 'none';
        }
        
        // Update CPU Speedometer Gauge
        if (data.cpu_percent !== undefined) {
            statCpu.textContent = `${Math.round(data.cpu_percent)}%`;
            // Calculate dashoffset for the SVG arc (125.66 is a full half-circle)
            const offset = 125.66 - (data.cpu_percent / 100) * 125.66;
            cpuGaugePath.style.strokeDashoffset = offset;
            
            if (data.cpu_percent > 85) {
                cpuGaugePath.style.stroke = '#ff007f'; // neon-magenta (redlined)
            } else if (data.cpu_percent > 50) {
                cpuGaugePath.style.stroke = '#ffb700'; // neon-gold (working)
            } else {
                cpuGaugePath.style.stroke = '#00d2d3'; // neon-cyan (idle)
            }
        }

        // Update speed and ETA
        if (statSpeed) statSpeed.textContent = data.speed || "-";
        if (statEta) statEta.textContent = data.eta || "-";

        // Update 1-sigma constraints table
        if (data.constraints && data.constraints.length > 0) {
            constraintsCard.style.display = 'block';
            let constraintsHtml = '<div style="display: grid; grid-template-columns: 1.2fr 1fr; gap: 4px; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 5px;">';
            data.constraints.forEach(c => {
                constraintsHtml += `<div><span style="color:#00d2d3">${c.parameter}</span></div><div>${c.mean} &plusmn; ${c.error}</div>`;
            });
            constraintsHtml += '</div>';
            constraintsBody.innerHTML = constraintsHtml;
        } else {
            constraintsCard.style.display = 'none';
        }

        // Update tensions and struggles
        // Render Tensions Badge
        statTensionsBadge.textContent = data.tension_status;
        if (data.tension_status === "Both Solved!") {
            statTensionsBadge.style.background = "rgba(57, 255, 20, 0.2)";
            statTensionsBadge.style.color = "#39ff14";
            statTensionsBadge.style.border = "1px solid #39ff14";
        } else if (data.tension_status && data.tension_status.includes("Solved")) {
            statTensionsBadge.style.background = "rgba(255, 183, 0, 0.2)";
            statTensionsBadge.style.color = "#ffb700";
            statTensionsBadge.style.border = "1px solid #ffb700";
        } else {
            statTensionsBadge.style.background = "rgba(255, 0, 127, 0.2)";
            statTensionsBadge.style.color = "#ff007f";
            statTensionsBadge.style.border = "1px solid #ff007f";
        }
        
        // Render Neutrino Sector status
        const statNcdmSection = document.getElementById('stat-ncdm-section');
        const statNcdmBadge = document.getElementById('stat-ncdm-badge');
        const statNcdmDetails = document.getElementById('stat-ncdm-details');
        if (statNcdmSection && statNcdmBadge) {
            if (data.ncdm_status && data.ncdm_status.enabled) {
                statNcdmSection.style.display = 'flex';
                const strugglesCount = data.ncdm_status.struggles || 0;
                
                let massText = "Enabled";
                let massVal = 0.0;
                if (data.ncdm_status.mass !== null && data.ncdm_status.mass !== undefined) {
                    massVal = parseFloat(data.ncdm_status.mass);
                    massText = `${massVal.toFixed(3)} eV`;
                }
                
                let stabilityText = strugglesCount > 0 ? "Unstable" : "Stable";
                if (strugglesCount > 0) {
                    statNcdmBadge.textContent = `${massText} (${stabilityText}: ${strugglesCount} fail(s))`;
                    statNcdmBadge.style.background = "rgba(255, 0, 127, 0.2)";
                    statNcdmBadge.style.color = "#ff007f";
                    statNcdmBadge.style.borderColor = "#ff007f";
                } else {
                    statNcdmBadge.textContent = `${massText} (${stabilityText})`;
                    statNcdmBadge.style.background = "rgba(57, 255, 20, 0.2)";
                    statNcdmBadge.style.color = "#39ff14";
                    statNcdmBadge.style.borderColor = "#39ff14";
                }

                // Update neutrino detailed diagnostic
                if (statNcdmDetails) {
                    let regime = "Standard Massive";
                    if (massVal > 0.5) {
                        regime = "Supermassive (High Mass)";
                    } else if (massVal < 0.1) {
                        regime = "Light Massive (CMB Bound)";
                    }
                    
                    const fluidApprox = data.ncdm_status.fluid_approx !== null && data.ncdm_status.fluid_approx !== undefined ? data.ncdm_status.fluid_approx : "Default (3)";
                    const qBins = data.ncdm_status.q_bins !== null && data.ncdm_status.q_bins !== undefined ? data.ncdm_status.q_bins : "Default (5)";
                    const lMaxNcdm = data.ncdm_status.l_max_ncdm !== null && data.ncdm_status.l_max_ncdm !== undefined ? data.ncdm_status.l_max_ncdm : "Default (17)";
                    
                    let advisory = "";
                    let advisoryColor = "#a4b0be";
                    if (massVal > 0.5) {
                        if (strugglesCount > 0) {
                            advisory = "⚠️ Solver unstable. Supermassive neutrinos need higher precision settings (e.g. increase 'q_bins' or adjust/disable 'ncdm_fluid_approximation' to avoid integration crashes).";
                            advisoryColor = "#ffb700";
                        } else {
                            advisory = "✅ Solver stable. CLASS is successfully integrating the Boltzmann hierarchy for this high-mass regime.";
                            advisoryColor = "#39ff14";
                        }
                    } else {
                        advisory = "✅ Solver stable. Parameters in standard cosmological boundaries.";
                        advisoryColor = "#39ff14";
                    }
                    
                    let feasibilityText = "";
                    if (massVal > 1.0) {
                        feasibilityText = "<div style='margin-top: 4px; padding: 4px; background: rgba(255, 0, 127, 0.1); border: 1px solid rgba(255, 0, 127, 0.2); border-radius: 4px; font-size: 0.72rem; color: #ff007f; line-height: 1.3;'>⚠️ Exceeds Cosmological Bounds: m_&nu; > 1.0 eV is heavily disfavored by Planck CMB data.</div>";
                    }
                    
                    statNcdmDetails.innerHTML = `
                        <div style="display: flex; justify-content: space-between; border-bottom: 1px dashed rgba(255,255,255,0.03); padding: 2px 0; color: var(--text-secondary);">
                            <span>Regime:</span>
                            <span style="color: #fff; font-weight: bold;">${regime}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; border-bottom: 1px dashed rgba(255,255,255,0.03); padding: 2px 0; color: var(--text-secondary);">
                            <span>Momentum Bins (q_bins):</span>
                            <span style="color: #fff; font-family: var(--font-mono);">${qBins}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; border-bottom: 1px dashed rgba(255,255,255,0.03); padding: 2px 0; color: var(--text-secondary);">
                            <span>Fluid Approx:</span>
                            <span style="color: #fff; font-family: var(--font-mono);">${fluidApprox}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; border-bottom: 1px dashed rgba(255,255,255,0.03); padding: 2px 0; color: var(--text-secondary);">
                            <span>l_max_ncdm:</span>
                            <span style="color: #fff; font-family: var(--font-mono);">${lMaxNcdm}</span>
                        </div>
                        <div style="margin-top: 6px; padding: 6px; background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 4px; font-size: 0.72rem; color: ${advisoryColor}; line-height: 1.3;">
                            ${advisory}
                        </div>
                        ${feasibilityText}
                    `;
                }
            } else {
                statNcdmSection.style.display = 'none';
            }
        }
        
        // Render Struggles
        if (data.struggles && Object.keys(data.struggles).length > 0) {
            let strugglesHtml = '<ul style="margin-left: 15px; padding-left: 0; list-style-type: square;">';
            for (const [module, count] of Object.entries(data.struggles)) {
                strugglesHtml += `<li style="margin-bottom: 2px;">${module}: <span style="font-weight: bold; color: #ff007f;">${count} fail(s)</span></li>`;
            }
            strugglesHtml += '</ul>';
            statStrugglesBody.innerHTML = strugglesHtml;
            statStrugglesBody.style.color = "#ffb700";
        } else {
            statStrugglesBody.textContent = "Stable (0 failures)";
            statStrugglesBody.style.color = "#39ff14";
        }

        // Update progress bar (assuming ~3000 points for convergence)
        const totalEstimated = 3000;
        let percent = Math.min(Math.floor((data.dead_points / totalEstimated) * 100), 99);
        if (data.status === 'completed') percent = 100;
        if (data.status === 'idle') percent = 0;
        
        // Update initialization progress bar
        if (data.status === 'running' || data.status === 'completed') {
            let p = data.init_percent !== undefined ? data.init_percent : 0;
            if (data.status === 'completed') p = 100;
            initFill.style.width = `${p}%`;
            initPercent.textContent = `${p}%`;
        } else {
            initFill.style.width = '0%';
            initPercent.textContent = '0%';
        }
        
        // Try fetching the live plot every ~30 seconds (10 ticks of 3s)
        if (data.status === 'running' || data.status === 'completed') {
            plotCheckCounter++;
            if (plotCheckCounter % 10 === 1 || data.status === 'completed') {
                const tempImg = new Image();
                tempImg.onload = function() {
                    plotImg.src = this.src;
                    plotContainer.style.display = 'block';
                    plotTimestamp.textContent = "Last updated: " + new Date().toLocaleTimeString();
                };
                tempImg.src = `${API_URL}/api/live_plot?t=${new Date().getTime()}`;
            }
        } else {
            plotContainer.style.display = 'none';
            plotCheckCounter = 0;
        }
        
        progressFill.style.width = `${percent}%`;
        progressPercent.textContent = `${percent}%`;
        
        // Handle actions availability
        if (data.status === 'running') {
            btnStart.disabled = true;
            btnResume.disabled = true;
            btnStop.disabled = false;
            
            let chi2Text = data.best_chi2 !== null ? data.best_chi2.toFixed(4) : 'evaluating';
            let logZText = data.log_evidence !== null ? data.log_evidence.toFixed(4) : 'evaluating';
        } else {
            btnStart.disabled = false;
            btnResume.disabled = false;
            btnStop.disabled = true;
        }
        
        // Update Watchdog card based on alerts from the backend
        let activeAlerts = (data.watchdog_alerts && data.watchdog_alerts.length > 0 && !watchdogIgnored) ? data.watchdog_alerts.length : 0;
        if (activeAlerts > lastWatchdogAlertCount) {
            playBarkSoundTwice();
        }
        lastWatchdogAlertCount = activeAlerts;

        if (data.watchdog_alerts && data.watchdog_alerts.length > 0) {
            if (!watchdogIgnored) {
                // We have alerts! Change dog to angry/warning mode
                watchdogIcon.innerText = '🚨';
                watchdogCard.style.borderColor = "#ff4757"; // Neon Red
                watchdogText.style.color = "#ff4757";
                watchdogText.style.textShadow = "0 0 10px rgba(255, 71, 87, 0.5)";
                watchdogText.innerText = `WARNING: ${data.watchdog_alerts.length} Issue(s) Detected!`;
                
                currentProposedUpdates = {};
                
                // Un-hide the details box and populate it with all warnings together
                watchdogDesc.style.display = "block";
                watchdogDesc.innerHTML = data.watchdog_alerts.map(alert => {
                    if (alert.new_min !== undefined && alert.new_max !== undefined) {
                        currentProposedUpdates[alert.parameter] = {min: alert.new_min, max: alert.new_max};
                    }
                    return `<div style="margin-bottom: 10px; padding-bottom: 10px; border-bottom: 1px solid rgba(255,255,255,0.1);">
                        <strong style="color: #ff9ff3; font-size: 1.1rem;">${alert.parameter}</strong><br>
                        <span style="color: #feca57;">${alert.status}</span><br>
                        <span style="color: #a4b0be; font-size: 0.85rem;">Suggestion: <span style="color: #fff;">${alert.suggestion}</span></span>
                    </div>`;
                }).join("");

                if (Object.keys(currentProposedUpdates).length > 0 && data.status === 'running') {
                    document.getElementById('watchdog-actions').style.display = 'flex';
                } else {
                    document.getElementById('watchdog-actions').style.display = 'none';
                }
            }
        } else {
            // All clear! Reset dog to happy mode
            watchdogIgnored = false;
            currentProposedUpdates = {};
            watchdogIcon.innerText = '🐶';
            watchdogCard.style.borderColor = "#00d2d3"; // Neon Cyan
            watchdogText.style.color = "#00d2d3";
            watchdogText.style.textShadow = "0 0 10px rgba(0, 210, 211, 0.5)";
            watchdogText.innerText = "All clear, Captain!";
            
            // Hide the details box
            watchdogDesc.style.display = "none";
            watchdogDesc.innerHTML = "";
            document.getElementById('watchdog-actions').style.display = 'none';
        }

        // If completed, compute evidence comparison
        if (data.status === 'completed' && data.log_evidence !== null) {
            if (activeConfig === 'lcdm_config.yaml') {
                updateBaseline("planck_bao_pantheonplus_shoes", data.log_evidence, data.best_chi2);
            } else {
                calculateEvidence(data.log_evidence);
                if (checkAutoRunLcdm && checkAutoRunLcdm.checked) {
                    appendLog(`[PIPELINE] Custom model completed. Preparing to auto-run baseline ΛCDM in 5 seconds...`);
                    setTimeout(() => {
                        switchToLcdm();
                        btnStart.click();
                    }, 5000);
                }
            }
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
    
    if (isNaN(baselineLogZ)) {
        valDelta.textContent = "-";
        jeffreysCard.className = 'jeffreys-card';
        jeffreysText.textContent = 'Baseline Missing';
        jeffreysDesc.textContent = 'Run the ΛCDM baseline first to enable model comparison.';
        updateEvidenceBreakdown();
        return;
    }

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
    
    updateEvidenceBreakdown();
}

// Watchdog Action Listeners
document.getElementById('btn-deny-priors').addEventListener('click', () => {
    watchdogIgnored = true;
    watchdogIcon.innerText = '🐶';
    watchdogCard.style.borderColor = "#00d2d3";
    watchdogText.style.color = "#00d2d3";
    watchdogText.style.textShadow = "0 0 10px rgba(0, 210, 211, 0.5)";
    watchdogText.innerText = "Warnings Ignored";
    watchdogDesc.style.display = "none";
    document.getElementById('watchdog-actions').style.display = 'none';
    appendLog('[WATCHDOG] Warnings dismissed. The run will continue undisturbed.');
});

document.getElementById('btn-accept-priors').addEventListener('click', async () => {
    document.getElementById('btn-accept-priors').disabled = true;
    appendLog('[WATCHDOG] Applying proposed prior changes and restarting run...');
    try {
        const response = await fetch(`${API_URL}/api/apply_priors_and_restart`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ config_name: activeConfig, updates: currentProposedUpdates })
        });
        const data = await response.json();
        if (response.ok) {
            appendLog('[WATCHDOG] Priors updated successfully. Restart sequence initiated.');
        } else {
            appendLog(`[WATCHDOG] Failed to apply priors: ${data.detail}`);
            document.getElementById('btn-accept-priors').disabled = false;
        }
    } catch (err) {
        appendLog(`[WATCHDOG] Error applying priors: ${err.message}`);
        document.getElementById('btn-accept-priors').disabled = false;
    }
});

// Console helper
function appendLog(message) {
    // Remove initial placeholder if present
    if (localLogs.length === 1 && localLogs[0] === 'Waiting for run execution...') {
        localLogs = [];
    }
    localLogs.push(`[${new Date().toLocaleTimeString()}] ${message}`);
    if (localLogs.length > 50) localLogs.shift();
    renderLogs();
}

function renderLogs() {
    let html = "";
    if (lastTerminalLogs && lastTerminalLogs.length > 0) {
        html += lastTerminalLogs.map(l => {
            let esc = l.replace(/</g, '&lt;').replace(/>/g, '&gt;');
            return esc.replace(/(\[.*?\])/g, '<span style="color:#feca57">$1</span>');
        }).join('<br>') + '<br><br><span style="color:#a4b0be; font-weight:bold;">--- DASHBOARD STATUS LOGS ---</span><br>';
    }
    html += localLogs.join('<br>');
    consoleBody.innerHTML = html;
    consoleBody.scrollTop = consoleBody.scrollHeight;
}

// Watchdog Audio Notification (Synthesizes realistic dog bark sounds using the Web Audio API)
function playBark() {
    try {
        const AudioContextClass = window.AudioContext || window.webkitAudioContext;
        if (!AudioContextClass) return;
        const audioCtx = new AudioContextClass();
        
        // Synthesizer nodes
        const osc = audioCtx.createOscillator();
        const gainNode = audioCtx.createGain();
        const filterNode = audioCtx.createBiquadFilter();

        // 1. Vocal tract filter shaping
        filterNode.type = 'bandpass';
        filterNode.frequency.setValueAtTime(450, audioCtx.currentTime);
        filterNode.Q.setValueAtTime(2.5, audioCtx.currentTime);

        // 2. Vocal folds tone sweep (sawtooth wave for raspiness)
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(260, audioCtx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(80, audioCtx.currentTime + 0.14);

        // 3. Bark envelope configuration
        gainNode.gain.setValueAtTime(0.001, audioCtx.currentTime);
        gainNode.gain.linearRampToValueAtTime(0.25, audioCtx.currentTime + 0.025); // sudden attack
        gainNode.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.16); // decay

        // 4. White noise injection to simulate breath friction (huffing sound)
        const bufferSize = audioCtx.sampleRate * 0.18; 
        const buffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate);
        const data = buffer.getChannelData(0);
        for (let i = 0; i < bufferSize; i++) {
            data[i] = Math.random() * 2 - 1;
        }
        const noise = audioCtx.createBufferSource();
        noise.buffer = buffer;

        const noiseGain = audioCtx.createGain();
        noiseGain.gain.setValueAtTime(0.18, audioCtx.currentTime);
        noiseGain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.14);

        // Routing connections
        osc.connect(filterNode);
        filterNode.connect(gainNode);
        
        noise.connect(noiseGain);
        noiseGain.connect(gainNode);

        gainNode.connect(audioCtx.destination);

        // Trigger playback
        osc.start();
        noise.start();
        osc.stop(audioCtx.currentTime + 0.18);
        noise.stop(audioCtx.currentTime + 0.18);
    } catch (err) {
        console.warn("Failed to play bark synth:", err);
    }
}

function playBarkSoundTwice() {
    playBark();
    setTimeout(playBark, 240); // double-bark spacing
}

// Evidence breakdown math visualizer
function updateEvidenceBreakdown() {
    const breakdownDiv = document.getElementById('evidence-breakdown');
    if (!breakdownDiv) return;

    if (!lastStatusData || lastStatusData.log_evidence === null || lastStatusData.best_chi2 === null || baselineLogEvidence === null) {
        breakdownDiv.style.display = 'none';
        return;
    }

    const logZ_custom = lastStatusData.log_evidence;
    const chi2_custom = lastStatusData.best_chi2;
    const logZ_baseline = baselineLogEvidence;
    
    // Calculate Occam Penalty for custom model: ln(L_max) - ln(Z)
    const logL_max_custom = -0.5 * chi2_custom;
    const occam_custom = logL_max_custom - logZ_custom;

    let html = `<div style="margin-top: 8px; font-weight: bold; color: #fff;">Bayesian Math Breakdown:</div>`;
    html += `<div style="margin-left: 5px; margin-top: 4px;">`;
    html += `• Custom Model ln(Z) = ln(L_max) - Occam Penalty<br>`;
    html += `  - ln(L_max) [Fit Score]: ${logL_max_custom.toFixed(2)} (Best χ²: ${chi2_custom.toFixed(2)})<br>`;
    html += `  - Occam Penalty: ${occam_custom.toFixed(2)} nat (Prior Shrinkage: 10<sup>${(occam_custom / Math.log(10)).toFixed(1)}</sup>)<br>`;
    html += `</div>`;

    if (baselineBestChi2 !== null && baselineBestChi2 !== undefined) {
        const chi2_baseline = baselineBestChi2;
        const logL_max_baseline = -0.5 * chi2_baseline;
        const occam_baseline = logL_max_baseline - logZ_baseline;
        
        const delta_logZ = logZ_custom - logZ_baseline;
        const delta_fit = logL_max_custom - logL_max_baseline;
        const delta_occam = occam_custom - occam_baseline;
        
        html += `<div style="border-top: 1px dashed rgba(255,255,255,0.1); margin-top: 6px; padding-top: 6px; margin-left: 5px;">`;
        html += `• Δln(Z) = Δln(L_max) - ΔOccam Penalty<br>`;
        html += `  - Δln(L_max) [Tension Gains]: <span style="color:#39ff14">${delta_fit >= 0 ? '+' : ''}${delta_fit.toFixed(2)}</span><br>`;
        html += `  - ΔOccam Penalty [Complexity Cost]: <span style="color:#ff4757">${delta_occam >= 0 ? '+' : ''}${delta_occam.toFixed(2)}</span><br>`;
        html += `  - Net Δln(Z): <span style="color:${delta_logZ >= 0 ? '#39ff14' : '#ff4757'}; font-weight: bold;">${delta_logZ >= 0 ? '+' : ''}${delta_logZ.toFixed(2)}</span>`;
        html += `</div>`;
    } else {
        html += `<div style="border-top: 1px dashed rgba(255,255,255,0.1); margin-top: 6px; padding-top: 6px; font-style: italic; color: #576574;">`;
        html += `Run baseline ΛCDM to see Occam complexity cost comparison.`;
        html += `</div>`;
    }

    breakdownDiv.innerHTML = html;
    breakdownDiv.style.display = 'block';
}

// Copy Utility Function
function copyToClipboard(text, buttonId) {
    navigator.clipboard.writeText(text).then(() => {
        const btn = document.getElementById(buttonId);
        const originalText = btn.textContent;
        // Check if button is a small icon button
        if (originalText === "📋") {
            btn.textContent = "Done! ✓";
            btn.style.color = "#39ff14";
            setTimeout(() => {
                btn.textContent = originalText;
                btn.style.color = "";
            }, 1500);
        } else {
            btn.textContent = "Copied! ✓";
            btn.style.color = "#39ff14";
            btn.style.borderColor = "#39ff14";
            setTimeout(() => {
                btn.textContent = originalText;
                btn.style.color = "";
                btn.style.borderColor = "";
            }, 1500);
        }
    }).catch(err => {
        console.error('Failed to copy text: ', err);
        alert('Could not copy to clipboard. Please copy manually.');
    });
}

// Register Copy Button Listeners
document.addEventListener('DOMContentLoaded', () => {
    // 1. Copy Evidence Comparison Math
    const btnCopyEvidence = document.getElementById('btn-copy-evidence');
    if (btnCopyEvidence) {
        btnCopyEvidence.addEventListener('click', () => {
            if (!lastStatusData) return;
            const logEvidenceVal = lastStatusData.log_evidence !== null ? `${lastStatusData.log_evidence.toFixed(4)} +/- ${lastStatusData.log_evidence_error.toFixed(4)}` : "-";
            const valBaselineText = document.getElementById('val-baseline').textContent;
            const valCustomText = document.getElementById('val-custom').textContent;
            const valDeltaText = document.getElementById('val-delta').textContent;
            const jeffText = document.getElementById('jeffreys-text').textContent;
            const jeffDescText = document.getElementById('jeffreys-desc').textContent;
            
            const text = `--- Bayesian Evidence Comparison ---
Baseline log(Z): ${valBaselineText}
Custom Model log(Z): ${valCustomText} (Evidence Z: ${logEvidenceVal})
Delta log(Z): ${valDeltaText}
Evidence Strength: ${jeffText} (${jeffDescText})`;
            copyToClipboard(text, 'btn-copy-evidence');
        });
    }

    // 2. Copy Best-Fit Chi2 and Parameters
    const btnCopyBestfit = document.getElementById('btn-copy-bestfit');
    if (btnCopyBestfit) {
        btnCopyBestfit.addEventListener('click', () => {
            if (!lastStatusData) return;
            const chi2Total = lastStatusData.best_chi2 !== null ? lastStatusData.best_chi2.toFixed(4) : "-";
            const chi2Cmb = lastStatusData.best_cmb !== null ? lastStatusData.best_cmb.toFixed(2) : "-";
            const chi2Bao = lastStatusData.best_bao !== null ? lastStatusData.best_bao.toFixed(2) : "-";
            const chi2Sn = lastStatusData.best_sn !== null ? lastStatusData.best_sn.toFixed(2) : "-";
            
            let text = `--- Best-Fit Chi2 Breakdown ---
Total Chi2: ${chi2Total}
CMB Chi2: ${chi2Cmb}
BAO Chi2: ${chi2Bao}
SN Chi2: ${chi2Sn}

--- Best-Fit Parameter Values ---
`;
            if (lastStatusData.best_raw_params) {
                for (const [key, val] of Object.entries(lastStatusData.best_raw_params)) {
                    if (!key.startsWith('chi2__') && !key.startsWith('minuslogprior')) {
                        const formattedVal = (typeof val === 'number') ? val.toPrecision(6) : val;
                        text += `${key}: ${formattedVal}\n`;
                    }
                }
            } else {
                text += "No best-fit parameters populated yet.\n";
            }
            copyToClipboard(text, 'btn-copy-bestfit');
        });
    }

    // 3. Copy Tension Resolution and struggles
    const btnCopyTensions = document.getElementById('btn-copy-tensions');
    if (btnCopyTensions) {
        btnCopyTensions.addEventListener('click', () => {
            if (!lastStatusData) return;
            const tensionStatus = lastStatusData.tension_status || "Unknown";
            const strugglesText = document.getElementById('stat-struggles-body').innerText;
            
            const text = `--- Tension Resolution & Stability ---
H0 & S8 Tensions Status: ${tensionStatus}

Model Struggles (CLASS Computation Failures):
${strugglesText}`;
            copyToClipboard(text, 'btn-copy-tensions');
        });
    }

    // 4. Copy 1-Sigma constraints
    const btnCopyConstraints = document.getElementById('btn-copy-constraints');
    if (btnCopyConstraints) {
        btnCopyConstraints.addEventListener('click', () => {
            if (!lastStatusData) return;
            let text = `--- 1-Sigma Parameter Constraints (Mean & 1-Sigma) ---\n`;
            if (lastStatusData.constraints && lastStatusData.constraints.length > 0) {
                lastStatusData.constraints.forEach(c => {
                    text += `${c.parameter}: ${c.mean} +/- ${c.error}\n`;
                });
            } else {
                text += "No 1-sigma constraints populated yet.\n";
            }
            copyToClipboard(text, 'btn-copy-constraints');
        });
    }

    // 5. Copy Unified AI Diagnostics Prompt
    const btnCopyAiPrompt = document.getElementById('btn-copy-ai-prompt');
    if (btnCopyAiPrompt) {
        btnCopyAiPrompt.addEventListener('click', () => {
            if (!lastStatusData) return;
            
            const status = lastStatusData.status || "idle";
            const valBaselineText = document.getElementById('val-baseline').textContent;
            const valCustomText = document.getElementById('val-custom').textContent;
            const valDeltaText = document.getElementById('val-delta').textContent;
            const jeffText = document.getElementById('jeffreys-text').textContent;
            const tensionStatus = lastStatusData.tension_status || "Unknown";
            const strugglesText = document.getElementById('stat-struggles-body').innerText.trim();
            
            const chi2Total = lastStatusData.best_chi2 !== null ? lastStatusData.best_chi2.toFixed(4) : "-";
            const chi2Cmb = lastStatusData.best_cmb !== null ? lastStatusData.best_cmb.toFixed(2) : "-";
            const chi2Bao = lastStatusData.best_bao !== null ? lastStatusData.best_bao.toFixed(2) : "-";
            const chi2Sn = lastStatusData.best_sn !== null ? lastStatusData.best_sn.toFixed(2) : "-";
            
            let bestFitList = "";
            if (lastStatusData.best_raw_params) {
                for (const [key, val] of Object.entries(lastStatusData.best_raw_params)) {
                    if (!key.startsWith('chi2__') && !key.startsWith('minuslogprior')) {
                        const formattedVal = (typeof val === 'number') ? val.toPrecision(6) : val;
                        bestFitList += `- ${key}: ${formattedVal}\n`;
                    }
                }
            } else {
                bestFitList = "No best-fit parameters populated yet.\n";
            }
            
            let constraintsList = "";
            if (lastStatusData.constraints && lastStatusData.constraints.length > 0) {
                lastStatusData.constraints.forEach(c => {
                    constraintsList += `- ${c.parameter}: ${c.mean} +/- ${c.error}\n`;
                });
            } else {
                constraintsList = "No 1-sigma constraints populated yet.\n";
            }
            
            const promptText = `Here is the cosmological data from my CLASS & Cobaya run. Please analyze these diagnostics, evaluate if the custom model resolves the H0 and S8 tensions, check the model struggles/stability, and explain the physical implications:

### Run Status
- Status: ${status}

### Bayesian Evidence Comparison
- Baseline log(Z): ${valBaselineText}
- Custom Model log(Z): ${valCustomText}
- Delta log(Z): ${valDeltaText}
- Evidence Strength: ${jeffText}

### Tension Resolution & Stability
- H0 & S8 Tensions Status: ${tensionStatus}
- Model Struggles: ${strugglesText}

### Best-Fit Chi2 Breakdown
- Total Chi2: ${chi2Total}
- CMB Chi2: ${chi2Cmb}
- BAO Chi2: ${chi2Bao}
- SN Chi2: ${chi2Sn}

### Best-Fit Parameter Values
${bestFitList}

### 1-Sigma Constraints (Mean & 1-Sigma)
${constraintsList}`;

            copyToClipboard(promptText, 'btn-copy-ai-prompt');
        });
    }
});
