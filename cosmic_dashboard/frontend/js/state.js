const API_URL = window.location.protocol === 'file:' ? 'http://localhost:8000' : window.location.origin;

/** Authenticated fetch — always sends session cookie for protected /api routes. */
function apiFetch(url, options = {}) {
    return fetch(url, { ...options, credentials: 'include' });
}

function setRunControlsIdle() {
    if (!isUploadingConfig) {
        if (btnStart) btnStart.disabled = false;
        if (btnStartOpt) btnStartOpt.disabled = false;
        if (btnResume) btnResume.disabled = false;
        if (btnApplyCosmicForge) btnApplyCosmicForge.disabled = false;
        if (btnLoadLastRun) btnLoadLastRun.disabled = false;
    }
    if (btnStop) btnStop.disabled = true;
}

function setRunControlsRunning() {
    if (btnStart) btnStart.disabled = true;
    if (btnStartOpt) btnStartOpt.disabled = true;
    if (btnResume) btnResume.disabled = true;
    if (btnApplyCosmicForge) btnApplyCosmicForge.disabled = true;
    if (btnLoadLastRun) btnLoadLastRun.disabled = true;
    if (btnStop) btnStop.disabled = false;
}

let statusInterval = null;

function scheduleStatusPolling() {
    if (statusInterval) clearInterval(statusInterval);
    const ms = (lastStatusData && lastStatusData.status === 'running') ? 5000 : 12000;
    statusInterval = setInterval(checkStatus, ms);
}

let activeConfig = 'lcdm_config.yaml';
let lastStatusData = null;
let baselineBestChi2 = null;
let baselineLogEvidence = null;
let lastBaselineUpdateRun = null;
let lastBaselineUpdateEvidence = null;
let isUploadingConfig = false;

// Global chart instances
let chartWMu = null;
let chartFSigma8 = null;
let chartInfluence = null;
let chartCompareW = null;
let chartCompareFs8 = null;
let chartSensitivity = null;
let chartPlaygroundRatio = null;
let chartTerrain = null;
let chartResiduals = null;
let chartQualityTrace = null;
let chartQualityAutocorr = null;
let chartPerPointResiduals = null;
let chartRunCompareShifts = null;

// Evolution animation variables
let evolutionPlayInterval = null;
let isPlayingEvolution = false;

// DOM Elements
const statusDot = document.getElementById('status-dot');
const statusText = document.getElementById('status-text');

const yamlZone = document.getElementById('yaml-upload-zone');
const yamlInput = document.getElementById('yaml-input');
const yamlName = document.getElementById('yaml-name');
const btnResetYaml = document.getElementById('btn-reset-yaml');

const btnStart = document.getElementById('btn-start');
const btnStartOpt = document.getElementById('btn-start-opt');
const btnLoadLastRun = document.getElementById('btn-load-last-run');
const btnResume = document.getElementById('btn-resume');
const btnStop = document.getElementById('btn-stop');
const btnApplyCosmicForge = document.getElementById('btn-apply-cosmicforge');
const btnDownload = document.getElementById('btn-download');

// Abort confirmation modal elements
const abortModal = document.getElementById('abort-modal');
const btnAbortCancel = document.getElementById('btn-abort-cancel');
const btnAbortConfirm = document.getElementById('btn-abort-confirm');

const statDead = document.getElementById('stat-dead');
const statEvidence = document.getElementById('stat-evidence');
const statChi2 = document.getElementById('stat-chi2');
const statChi2File = document.getElementById('stat-chi2-file');
const statChi2Cmb = document.getElementById('stat-chi2-cmb');
const statChi2Bao = document.getElementById('stat-chi2-bao');
const statChi2Sn = document.getElementById('stat-chi2-sn');
const statRawParams = document.getElementById('stat-raw-params');
const statCpu = document.getElementById('stat-cpu');
const cpuGaugePath = document.getElementById('cpu-gauge-path');
const progressFill = document.getElementById('progress-fill');
const progressPercent = document.getElementById('progress-percent');
const consoleBody = document.getElementById('console-body');

// Confidence Tracker (new main-screen confidence in likelihood + parameters)
const statConfidence = document.getElementById('stat-confidence');
const confEvidenceEl = document.getElementById('conf-evidence');
const confParamsEl = document.getElementById('conf-params');
const confSamplerEl = document.getElementById('conf-sampler');
const confMessageEl = document.getElementById('conf-message');

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

// Optimizer Monitor Elements
const optStatEvals = document.getElementById('opt-stat-evals');
const optStatChi2 = document.getElementById('opt-stat-chi2');
const optStatChi2File = document.getElementById('opt-stat-chi2-file');
const optStatChi2Cmb = document.getElementById('opt-stat-chi2-cmb');
const optStatChi2Bao = document.getElementById('opt-stat-chi2-bao');
const optStatChi2Sn = document.getElementById('opt-stat-chi2-sn');
const optStatPhase = document.getElementById('opt-stat-phase');
const optCpuGaugePath = document.getElementById('opt-cpu-gauge-path');
const optStatCpu = document.getElementById('opt-stat-cpu');
const optStatSpeed = document.getElementById('opt-stat-speed');
const optStatEta = document.getElementById('opt-stat-eta');
const optProgressPercent = document.getElementById('opt-progress-percent');
const optProgressFill = document.getElementById('opt-progress-fill');

let monitorTabAutoSwitched = false;

window.switchMonitorTab = function(tabName) {
    const btnSampler = document.getElementById('btn-monitor-tab-sampler');
    const btnOptimizer = document.getElementById('btn-monitor-tab-optimizer');
    const viewSampler = document.getElementById('monitor-view-sampler');
    const viewOptimizer = document.getElementById('monitor-view-optimizer');
    
    if (!btnSampler || !btnOptimizer || !viewSampler || !viewOptimizer) return;
    
    if (tabName === 'optimizer') {
        btnSampler.classList.remove('active');
        btnOptimizer.classList.add('active');
        viewSampler.style.display = 'none';
        viewOptimizer.style.display = 'block';
    } else {
        btnSampler.classList.add('active');
        btnOptimizer.classList.remove('active');
        viewSampler.style.display = 'block';
        viewOptimizer.style.display = 'none';
    }
};

let localLogs = ['Waiting for run execution...'];
let lastTerminalLogs = [];
let plotCheckCounter = 0;

const plotContainer = document.getElementById('live-plot-container');
const plotImg = document.getElementById('live-plot-img');
const plotTimestamp = document.getElementById('plot-timestamp');

const valBaseline = document.getElementById('val-baseline');
const valCustom = document.getElementById('val-custom');
const valDelta = document.getElementById('val-delta');
const multimodalComparisonCard = document.getElementById('multimodal-comparison-card');
const multimodalComparisonBody = document.getElementById('multimodal-comparison-body');

const jeffreysCard = document.getElementById('jeffreys-card');
const jeffreysText = document.getElementById('jeffreys-text');
const jeffreysDesc = document.getElementById('jeffreys-desc');

const watchdogCard = document.getElementById('watchdog-card');
const watchdogText = document.getElementById('watchdog-text');
const watchdogDesc = document.getElementById('watchdog-desc');
const watchdogIcon = document.getElementById('watchdog-icon');

const inputCores = document.getElementById('input-cores');
const checkAutoRebuild = document.getElementById('check-autorebuild');
const btnToggleLcdm = document.getElementById('btn-toggle-lcdm');
const btnTogglePrtoe = document.getElementById('btn-toggle-prtoe');
const checkAutoRunLcdm = document.getElementById('check-autorun-lcdm');
const checkAutoRunCustom = document.getElementById('check-autorun-custom');

let currentProposedUpdates = {};
let isAutoRunning = false; // Flag to track and prevent duplicate auto-run triggers
let watchdogIgnored = false; // Flag to temporarily ignore watchdog
let lastRunStartTime = null; // Track run start time to persist ignore state across refreshes
let lastWatchdogAlertCount = 0; // Track watchdog alert count for audio alerts
let autoWatchdogEnabled = false;

function updateToggleUI() {
    const toggle = document.getElementById('toggle-auto-watchdog');
    if (!toggle) return;
    const label = toggle.closest('label') || toggle.parentElement;
    if (!label) return;
    const slider = label.querySelector('.slider');
    const handle = label.querySelector('.toggle-handle');
    if (!handle) return;
    if (autoWatchdogEnabled) {
        if (slider) slider.style.backgroundColor = '#10ac84';
        handle.style.left = '18px';
    } else {
        if (slider) slider.style.backgroundColor = 'rgba(255,255,255,0.15)';
        handle.style.left = '2px';
    }
}


// Initial setup
