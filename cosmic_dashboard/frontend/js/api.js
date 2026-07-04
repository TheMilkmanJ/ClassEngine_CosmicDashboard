/**
 * CosmicDashboard API Client
 * Centralizes backend communication to decouple network logic from UI rendering.
 */

window.CosmicAPI = {
    // Core Status
    async getStatus(abortController) { return await apiFetch(`${API_URL}/api/status`, { signal: abortController?.signal }); },
    async getSysInfo() { return await fetch(`${API_URL}/api/sysinfo`); },
    
    // Derived Params & Metrics
    async getDerivedParameters(postData = null) {
        if (postData) return await fetch(`${API_URL}/api/derived_parameters`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(postData) });
        return await fetch(`${API_URL}/api/derived_parameters`);
    },
    async getMultimodalComparison() { return await fetch(`${API_URL}/api/multimodal_comparison`, { credentials: 'include' }); },
    async getMcmcDiagnostics(configName) { return await fetch(`${API_URL}/api/mcmc_diagnostics?config_name=${encodeURIComponent(configName)}`); },
    async compareModels() { return await fetch(`${API_URL}/api/compare_models`); },
    async getWaicLoo() { return await fetch(`${API_URL}/api/waic_loo`); },
    async getIcVsEvidenceComparison() { return await fetch(`${API_URL}/api/ic_vs_evidence_comparison`); },
    async getBayesFactorsBma() { return await fetch(`${API_URL}/api/bayes_factors_bma`); },
    
    // Playground & Configs
    async getPlaygroundParams() { return await fetch(`${API_URL}/api/playground_params`); },
    async getPlaygroundCurves(payload) { 
        return await fetch(`${API_URL}/api/playground_curves`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) }); 
    },
    async getBaselines() { return await fetch(`${API_URL}/api/baselines`); },
    async updateBaseline(payload) {
        return await fetch(`${API_URL}/api/update_baseline`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
    },
    
    // Class Engine Management
    async getClassEngines() { return await fetch(`${API_URL}/api/class_engines`); },
    async selectClassEngine(payload) {
        return await fetch(`${API_URL}/api/class_engines/select`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
    },
    async rebuildClass(payload) {
        return await fetch(`${API_URL}/api/rebuild_class_wizard`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
    },
    async getRebuildStatus() { return await fetch(`${API_URL}/api/rebuild_status`); },
    
    // Advanced Analysis
    async runStabilityScan(configName) { return await fetch(`${API_URL}/api/stability_scan?config_name=${encodeURIComponent(configName)}`); },
    async runSensitivityAnalysis(configName) { return await fetch(`${API_URL}/api/sensitivity_analysis?config_name=${encodeURIComponent(configName)}`); },
    async getJacobian(configName) { return await fetch(`${API_URL}/api/jacobian?config_name=${encodeURIComponent(configName)}`); },
    async pullDataset(configName) { return await fetch(`${API_URL}/api/dataset_pull?config_name=${encodeURIComponent(configName)}`); },
    async getSamplerBrain(configName) { return await fetch(`${API_URL}/api/sampler_brain?config_name=${encodeURIComponent(configName)}`); },
    async getLikelihoodTerrain(p1, p2, configName) { return await fetch(`${API_URL}/api/likelihood_terrain?param1=${encodeURIComponent(p1)}&param2=${encodeURIComponent(p2)}&config_name=${encodeURIComponent(configName)}`); },
    async getRunAutopsy(configName) { return await fetch(`${API_URL}/api/run_autopsy?config_name=${encodeURIComponent(configName)}`); },
    async getResiduals(configName) { return await fetch(`${API_URL}/api/residuals?config_name=${encodeURIComponent(configName)}`); },
    async getChainQuality(param, configName) { return await fetch(`${API_URL}/api/chain_quality?param=${encodeURIComponent(param)}&config_name=${encodeURIComponent(configName)}`); },
    async getPerPointChi2(configName) { return await fetch(`${API_URL}/api/per_point_chi2?config_name=${encodeURIComponent(configName)}`); },
    async updateModelDeformation(payload) {
        return await fetch(`${API_URL}/api/model_deformation`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
    },
    
    // Sampler & Lifecycle Controls
    async recoverSampler(payload) {
        return await fetch(`${API_URL}/api/recover_sampler`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
    },
    async applyPriors(payload) {
        return await fetch(`${API_URL}/api/apply_priors_and_restart`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
    },
    async clearWatchdogAlerts(payload) {
        return await fetch(`${API_URL}/api/clear_watchdog_alerts`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
    },
    
    // Logging & History
    async getLogs(lines = 200) { return await fetch(`${API_URL}/api/logs?lines=${lines}`); },
    async clearLog(payload) {
        return await fetch(`${API_URL}/api/clear_log`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
    },
    async resetHistory() { return await fetch(`${API_URL}/api/reset_history`, { method: 'POST' }); },
    async exportPaperFigure() { return await fetch(`${API_URL}/api/export_paper_figure`); },
    
    // Runs & History
    async getRunsList() { return await fetch(`${API_URL}/api/runs/list`); },
    async compareRuns(payload) {
        return await fetch(`${API_URL}/api/runs/compare`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
    },
    async getProvenanceLedger(configName) { return await fetch(`${API_URL}/api/provenance_ledger?config_name=${encodeURIComponent(configName)}`); },
    async getRunSummary(queryArgs) { return await fetch(`${API_URL}/api/run_summary${queryArgs}`, { credentials: 'include' }); },
    
    // Checkpoints
    async getCheckpointsList() { return await fetch(`${API_URL}/api/checkpoints/list`); },
    async createCheckpoint(payload) {
        return await fetch(`${API_URL}/api/checkpoints/create`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
    },
    async restoreCheckpoint(payload) {
        return await fetch(`${API_URL}/api/checkpoints/restore`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
    },
    
    // Errors & Auth
    async getDashboardErrors() { return await fetch(`${API_URL}/api/dashboard_errors`); },
    async acknowledgeError(payload) {
        return await fetch(`${API_URL}/api/acknowledge_error`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
    },
    async clearDashboardErrors(payload) {
        return await fetch(`${API_URL}/api/clear_dashboard_errors`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
    },
    async login(username, password, remember_me) {
        return await fetch(`${API_URL}/api/login`, {
            method: 'POST',
            credentials: 'include',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({username, password, remember_me})
        });
    }
};
