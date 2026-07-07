document.addEventListener('DOMContentLoaded', () => {
    // Default to idle controls; checkStatus will switch to running if needed.
    setRunControlsIdle();
    // PERF: Fire checkStatus first so the main UI populates immediately.
    // Stagger non-critical fetches so they don't compete with first paint.
    checkStatus();
    setTimeout(() => fetchBaselines(), 300);   // baselines: slight delay, non-critical
    updateToggleUI();

    const toggleAutoWatchdog = document.getElementById('toggle-auto-watchdog');
    if (toggleAutoWatchdog) {
        toggleAutoWatchdog.addEventListener('click', async () => {
            const previousState = autoWatchdogEnabled;
            autoWatchdogEnabled = !autoWatchdogEnabled;
            updateToggleUI();
            try {
                const response = await fetch(`${API_URL}/api/settings/watchdog`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    credentials: 'include',
                    body: JSON.stringify({ auto_apply: autoWatchdogEnabled })
                });
                if (!response.ok) {
                    throw new Error(`Server returned ${response.status}`);
                }
            } catch (err) {
                console.error("Error updating watchdog settings:", err);
                appendLog(`[WATCHDOG] Failed to update settings: ${err.message}. Reverting toggle.`);
                autoWatchdogEnabled = previousState;
                updateToggleUI();
            }
        });
    }
    // 5s while running, 12s when idle/completed — keeps uploads responsive.
    scheduleStatusPolling();

    // Run Complete Summary Card event listeners
    const btnCloseSummary = document.getElementById('btn-close-summary');
    if (btnCloseSummary) {
        btnCloseSummary.addEventListener('click', () => {
            const card = document.getElementById('run-complete-summary-card');
            if (card) card.style.display = 'none';
        });
    }
    const btnViewOptimizerDetails = document.getElementById('btn-view-optimizer-details');
    if (btnViewOptimizerDetails) {
        btnViewOptimizerDetails.addEventListener('click', () => {
            const optTabBtn = document.getElementById('tab-btn-optimizer');
            if (optTabBtn) optTabBtn.click();
        });
    }

    // WebSocket for real-time (production improvement, fallback to poll)
    try {
        const wsProtocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
        const wsUrl = `${wsProtocol}//${window.location.host}/ws/status`;
        const ws = new WebSocket(wsUrl);
        ws.onmessage = (event) => {
            const msg = JSON.parse(event.data);
            if (msg.type === 'status_update' && msg.data) {
                // Update key UI elements live (extend as needed)
                if (window.updateStatusUI) window.updateStatusUI(msg.data);
                else console.log('WS status update (real-time):', msg.data.status);
                refreshDerivedParameters();
            }
        };
        ws.onerror = () => console.log('WS not available, using polling');
    } catch(e) { /* polling fallback */ }
    fetchSysInfo();
    loadClassEngines(true);
    // PERF: refreshDerivedParameters is slow on first load when no data exists.
    // Defer 800ms so it doesn't block initial paint.
    setTimeout(() => refreshDerivedParameters(), 800);

    // PERF: Lazy-load the nebula background image after first paint is done.
    // This avoids the Unsplash image blocking LCP (Largest Contentful Paint).
    requestIdleCallback(() => {
        document.body.style.backgroundImage =
            "linear-gradient(to bottom, rgba(3,0,8,0.4), rgba(3,0,8,0.9)), " +
            "url('https://images.unsplash.com/photo-1462331940025-496dfbfc7564?q=80&w=2560&auto=format&fit=crop')";
    }, { timeout: 1000 });

    // Wire Manage Engines button (prompt UI for adding/selecting engines)
    const manageBtn = document.getElementById('btn-manage-engines');
    if (manageBtn) {
        manageBtn.addEventListener('click', (e) => {
            e.preventDefault();
            const list = (classEnginesCache || []).map(e => `${e.id}: ${e.name} @ ${e.class_path}`).join('\n') || 'None';
            const choice = prompt(
                `Current CLASS Engines:\n${list}\n\nType "add" to register a new CLASS build,\n an engine ID to select it, or "refresh":`,
                'refresh'
            );
            if (!choice) return;
            const lc = choice.toLowerCase();
            if (lc === 'add') {
                addClassEngineQuick();
            } else if (lc === 'refresh') {
                loadClassEngines(true);
            } else {
                fetch(`${API_URL}/api/class_engines/select`, {
                    method: 'POST', headers: {'Content-Type':'application/json'},
                    body: JSON.stringify({id: choice})
                }).then(r => r.ok ? r.json() : Promise.reject()).then(() => {
                    loadClassEngines(true);
                    fetchSysInfo();
                }).catch(() => alert('Select failed'));
            }
        });
    }
    
    // Tab switching logic
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');
    tabButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const tabId = btn.getAttribute('data-tab');
            tabButtons.forEach(b => b.classList.remove('active'));
            tabContents.forEach(c => c.classList.remove('active'));
            btn.classList.add('active');
            const targetContent = document.getElementById(tabId);
            if (targetContent) targetContent.classList.add('active');

            // Trigger resize of charts in the selected tab to fix hidden dimensions issue
            setTimeout(() => {
                if (tabId === 'tab-curves') {
                    if (chartWMu) chartWMu.resize();
                    if (chartFSigma8) chartFSigma8.resize();
                } else if (tabId === 'tab-influence') {
                    if (chartInfluence) chartInfluence.resize();
                    refreshJacobianAndPulls();
                } else if (tabId === 'tab-compare') {
                    if (chartCompareW) chartCompareW.resize();
                    if (chartCompareFs8) chartCompareFs8.resize();
                    refreshCompare(); // Auto refresh comparison on tab switch
                } else if (tabId === 'tab-stability') {
                    if (chartSensitivity) chartSensitivity.resize();
                } else if (tabId === 'tab-playground') {
                    if (chartPlaygroundRatio) chartPlaygroundRatio.resize();
                    updatePlayground(); // Auto draw playground line
                    buildGeneralPlaygroundSliders(); // load dynamic generalized sliders
                } else if (tabId === 'tab-health') {
                    refreshSamplerBrain();
                    if (chartQualityTrace) chartQualityTrace.resize();
                    if (chartQualityAutocorr) chartQualityAutocorr.resize();
                    refreshChainQuality();
                } else if (tabId === 'tab-corner') {
                    if (chartTerrain) chartTerrain.resize();
                    refreshLikelihoodTerrain();
                } else if (tabId === 'tab-autopsy') {
                    if (chartResiduals) chartResiduals.resize();
                    refreshAutopsyAndResiduals();
                } else if (tabId === 'tab-perpoint') {
                    if (chartPerPointResiduals) chartPerPointResiduals.resize();
                    refreshPerPointChi2();
                } else if (tabId === 'tab-runcompare') {
                    if (chartRunCompareShifts) chartRunCompareShifts.resize();
                    populateRunsLists();
                    computeIcVsEvidence();  // auto refresh IC/evidence for comparison
                } else if (tabId === 'tab-provenance') {
                    refreshProvenanceLedger();
                } else if (tabId === 'tab-utils') {
                    refreshCheckpointsList();
                    refreshErrorLog();
                } else if (tabId === 'tab-tension') {
                    refreshDerivedParameters();
                    computeIcVsEvidence();
                }
            }, 50);
        });
    });

    // PERF: Defer chart initialization until after first paint and Chart.js is confirmed loaded.
    // initCharts() creates 13 Chart.js instances — doing it synchronously blocks the main thread.
    const _initChartsWhenReady = () => {
        if (typeof Chart !== 'undefined') {
            initCharts();
        } else {
            // Chart.js (deferred) not yet parsed — retry in 100ms
            setTimeout(_initChartsWhenReady, 100);
        }
    };
    setTimeout(_initChartsWhenReady, 200); // yield to browser paint first

    // Rebuild CLASS Wizard Compile Button
    const btnWizardCompile = document.getElementById('btn-wizard-compile');
    if (btnWizardCompile) {
        btnWizardCompile.addEventListener('click', handleWizardCompile);
    }

    // Export Figure Button
    const btnExportFigure = document.getElementById('btn-export-figure');
    if (btnExportFigure) {
        btnExportFigure.addEventListener('click', handleExportFigure);
    }

    // Download Notebook Button
    const btnDownloadNotebook = document.getElementById('btn-download-notebook');
    if (btnDownloadNotebook) {
        btnDownloadNotebook.addEventListener('click', () => {
            window.location.href = `${API_URL}/api/generate_notebook`;
        });
    }

    // Reset History Button
    const btnResetHistory = document.getElementById('btn-reset-history');
    if (btnResetHistory) {
        btnResetHistory.addEventListener('click', handleResetHistory);
    }

    // Evolution slider and play controls
    const evoSlider = document.getElementById('evolution-slider');
    if (evoSlider) {
        evoSlider.addEventListener('input', () => {
            showEvolutionFrame(parseInt(evoSlider.value));
        });
    }
    const btnPlayEvolution = document.getElementById('btn-play-evolution');
    if (btnPlayEvolution) {
        btnPlayEvolution.addEventListener('click', toggleEvolutionPlayback);
    }

    // Manual login button to force modal (ensures in-app modal is used, no native Basic prompt)
    const btnManualLogin = document.getElementById('btn-manual-login');
    const btnLogout = document.getElementById('btn-logout');
    if (btnManualLogin) {
        btnManualLogin.addEventListener('click', () => showLoginModal());
    }
    if (btnLogout) {
        btnLogout.addEventListener('click', async () => {
            try {
                await fetch(`${API_URL}/api/logout`, { method: 'POST', credentials: 'include' });
            } catch(e) {}
            location.reload();
        });
    }
    // Both buttons always visible for easy access to the cool modal login flow or logout.

    // Phone link controls (make the often-breaking phone sync more robust + manual recovery)
    const btnPhoneCopy = document.getElementById('btn-phone-copy');
    const btnPhoneRefresh = document.getElementById('btn-phone-refresh');
    const btnPhoneSet = document.getElementById('btn-phone-set');
    const btnPhoneClear = document.getElementById('btn-phone-clear');
    const phoneLinkHrefEl = document.getElementById('phone-link-href');
    const phoneContainerEl = document.getElementById('phone-link-container');

    if (btnPhoneCopy && phoneLinkHrefEl) {
        btnPhoneCopy.addEventListener('click', (e) => {
            e.preventDefault();
            const fullUrl = phoneLinkHrefEl.href;
            if (fullUrl && fullUrl !== '#') {
                navigator.clipboard.writeText(fullUrl).then(() => {
                    const orig = btnPhoneCopy.textContent;
                    btnPhoneCopy.textContent = '✅';
                    setTimeout(() => { btnPhoneCopy.textContent = orig; }, 1200);
                }).catch(() => {
                    // fallback
                    prompt('Copy this phone URL:', fullUrl);
                });
            }
        });
    }
    if (btnPhoneRefresh) {
        btnPhoneRefresh.addEventListener('click', (e) => {
            e.preventDefault();
            checkStatus();
        });
    }
    if (btnPhoneSet) {
        btnPhoneSet.addEventListener('click', async (e) => {
            e.preventDefault();
            const current = (lastStatusData && lastStatusData.localtunnel_url) || (phoneLinkHrefEl ? phoneLinkHrefEl.href : '');
            const pasted = prompt('Paste a working phone tunnel URL (e.g. https://abc123.loca.lt) or leave empty to cancel.\n\nUse this for manual "npx localtunnel --port 8000" or if the auto link broke.', current || '');
            if (pasted === null) return; // cancel
            const urlVal = pasted.trim();
            // Validate URL is HTTP(S) before storing
            if (urlVal && !urlVal.match(/^https?:\/\//i)) {
                alert('Invalid URL: must start with http:// or https://');
                return;
            }
            try {
                const resp = await fetch(`${API_URL}/api/set_tunnel_url`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    credentials: 'include',
                    body: JSON.stringify({ url: urlVal })
                });
                if (resp.ok) {
                    appendLog('[Phone] Tunnel URL set manually.');
                    checkStatus();
                } else {
                    const err = await resp.json().catch(() => ({}));
                    alert('Failed to set phone URL: ' + (err.detail || resp.status));
                }
            } catch (err) {
                alert('Error setting phone URL: ' + err.message);
            }
        });
    }
    if (btnPhoneClear) {
        btnPhoneClear.addEventListener('click', async (e) => {
            e.preventDefault();
            if (!confirm('Clear the current phone tunnel link?')) return;
            try {
                const resp = await fetch(`${API_URL}/api/set_tunnel_url`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    credentials: 'include',
                    body: JSON.stringify({ url: '' })
                });
                if (resp.ok) {
                    appendLog('[Phone] Tunnel URL cleared.');
                    checkStatus();
                }
            } catch (err) {
                // still refresh
                checkStatus();
            }
        });
    }

    // Global phone button (always visible compact control so you can fix the link even when hidden / auto broken)
    const btnPhoneGlobal = document.getElementById('btn-phone-set-global');
    if (btnPhoneGlobal) {
        btnPhoneGlobal.addEventListener('click', async (e) => {
            e.preventDefault();
            const current = (lastStatusData && lastStatusData.localtunnel_url) || (phoneLinkHrefEl ? phoneLinkHrefEl.href : '');
            const pasted = prompt('Paste a working phone tunnel URL (e.g. https://abc123.loca.lt) — this activates the Phone Sync link for remote/phone access.\n\nUseful if the launcher phone link "broke", tunnel expired, or you ran npx localtunnel manually in another terminal.', current || '');
            if (pasted === null) return;
            const urlVal = pasted.trim();
            // Validate URL is HTTP(S) before storing
            if (urlVal && !urlVal.match(/^https?:\/\//i)) {
                alert('Invalid URL: must start with http:// or https://');
                return;
            }
            try {
                const resp = await fetch(`${API_URL}/api/set_tunnel_url`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    credentials: 'include',
                    body: JSON.stringify({ url: urlVal })
                });
                if (resp.ok) {
                    appendLog('[Phone] Tunnel URL set via global control.');
                    checkStatus();
                } else {
                    const err = await resp.json().catch(() => ({}));
                    alert('Failed to set phone URL: ' + (err.detail || resp.status));
                }
            } catch (err) {
                alert('Error setting phone URL: ' + err.message);
            }
        });
    }

    const btnBundle = document.getElementById('btn-submit-bundle');
    if (btnBundle) {
        btnBundle.addEventListener('click', () => {
            window.location.href = `${API_URL}/api/generate_submit_bundle`;
        });
    }

    const btnPPC = document.getElementById('btn-ppc');
    const btnFisher = document.getElementById('btn-fisher');
    const ppcResult = document.getElementById('ppc-fisher-result');
    if (btnPPC) {
        btnPPC.addEventListener('click', async () => {
            if (ppcResult) ppcResult.textContent = 'Running PPC...';
            const r = await fetch(`${API_URL}/api/posterior_predictive`, {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({n:20})});
            const j = await r.json();
            if (ppcResult) ppcResult.textContent = JSON.stringify(j, null, 2);
        });
    }
    if (btnFisher) {
        btnFisher.addEventListener('click', async () => {
            if (ppcResult) ppcResult.textContent = 'Running Fisher...';
            const r = await fetch(`${API_URL}/api/fisher_forecast`, {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({params:['H0','w0_fld']})});
            const j = await r.json();
            if (ppcResult) ppcResult.textContent = JSON.stringify(j, null, 2);
        });
    }

    const btnComputeExpr = document.getElementById('btn-compute-expr');
    if (btnComputeExpr) {
        btnComputeExpr.addEventListener('click', computeDerivedExpression);
    }
    const exprInput = document.getElementById('derived-expr-input');
    if (exprInput) {
        exprInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') computeDerivedExpression();
        });
    }

    const btnIcEvidence = document.getElementById('btn-ic-evidence');
    if (btnIcEvidence) {
        btnIcEvidence.addEventListener('click', computeIcVsEvidence);
    }
    // Basic copy for the IC card (extend as needed)
    const btnCopyIc = document.getElementById('btn-copy-ic-evidence');
    if (btnCopyIc) {
        btnCopyIc.addEventListener('click', () => {
            const body = document.getElementById('ic-evidence-body');
            if (body) copyToClipboard(body.innerText || 'IC vs Evidence comparison', 'btn-copy-ic-evidence');
        });
    }

    const btnReweight = document.getElementById('btn-reweight');
    if (btnReweight) {
        btnReweight.addEventListener('click', async () => {
            const body = document.getElementById('ic-evidence-values');
            if (body) body.textContent = 'Reweighting...';
            const r = await fetch(`${API_URL}/api/reweight`, {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({})});
            const j = await r.json();
            if (body) body.innerHTML = `Reweighted: ESS=${j.ess} ΔlogZ≈${j.approx_delta_logz}<br>${JSON.stringify(j.reweighted_params)}`;
        });
    }

    // New obsolete-AIC/BIC buttons: PSIS-LOO, Stacking, Savage-Dickey
    const btnPsis = document.getElementById('btn-psis-loo');
    const advBody = document.getElementById('advanced-metrics-body');
    if (btnPsis && advBody) {
        btnPsis.addEventListener('click', async () => {
            advBody.style.display = 'block';
            advBody.textContent = 'Computing PSIS-LOO + Pareto k...';
            try {
                const r = await fetch(`${API_URL}/api/psis_loo`);
                const j = await r.json();
                const p = j.psis_loo || {};
                let h = `PSIS-LOO elpd: ${p.elpd_loo || '?'} (SE ${p.se_elpd_loo || '?'}) p_loo=${p.p_loo || '?'} max_k=${p.pareto_k_max || '?'}`;
                if (p.high_k_warnings && p.high_k_warnings.length) h += `<br><span style="color:#ff9f43">⚠ ${p.high_k_warnings.join('; ')}</span>`;
                if (p.pareto_k_per_obs) h += `<br>k per probe: ${p.pareto_k_per_obs.join(', ')}`;
                advBody.innerHTML = h + `<br><small>${p.note || ''}</small>`;
            } catch(e) { advBody.textContent = 'PSIS error (run a model).'; }
        });
    }
    const btnStack = document.getElementById('btn-model-stacking');
    if (btnStack && advBody) {
        btnStack.addEventListener('click', async () => {
            advBody.style.display = 'block';
            advBody.textContent = 'Computing Bayesian Stacking weights...';
            try {
                const r = await fetch(`${API_URL}/api/model_stacking`, {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({})});
                const j = await r.json();
                const s = j.stacking || {};
                advBody.innerHTML = `Stacking weights: ${JSON.stringify(s.stacking_weights || {})}<br><small>${s.note || ''}</small>`;
            } catch(e) { advBody.textContent = 'Stacking error.'; }
        });
    }
    const btnSavage = document.getElementById('btn-savage-dickey');
    if (btnSavage && advBody) {
        btnSavage.addEventListener('click', async () => {
            advBody.style.display = 'block';
            advBody.textContent = 'Computing Savage-Dickey BF (nested)...';
            try {
                const r = await fetch(`${API_URL}/api/savage_dickey?param=xi_prtoe&point=0`);
                const j = await r.json();
                const sd = j.savage_dickey || {};
                advBody.innerHTML = `Savage-Dickey BF10 (xi=0): ${sd.bf10 || '?'}<br>post@0=${sd.posterior_density_at_point || '?'} prior@0=${sd.prior_density_at_point || '?'}<br><small>${sd.note || ''}</small>`;
            } catch(e) { advBody.textContent = 'Savage-Dickey error (needs samples + yaml prior).'; }
        });
    }

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

    // Corner Plot Button
    const btnGenerateCorner = document.getElementById('btn-generate-corner');
    if (btnGenerateCorner) {
        btnGenerateCorner.addEventListener('click', handleGenerateCorner);
    }

    // Refresh Compare Button
    const btnRefreshCompare = document.getElementById('btn-refresh-compare');
    if (btnRefreshCompare) {
        btnRefreshCompare.addEventListener('click', refreshCompare);
    }

    // Run Scanner Button
    const btnRunScanner = document.getElementById('btn-run-scanner');
    if (btnRunScanner) {
        btnRunScanner.addEventListener('click', runStabilityScanner);
    }

    // Run Sensitivity Button
    const btnRunSensitivity = document.getElementById('btn-run-sensitivity');
    if (btnRunSensitivity) {
        btnRunSensitivity.addEventListener('click', runSensitivityAnalyzer);
    }

    // Playground Sliders
    const sliders = ['slide-delta', 'slide-xi', 'slide-zeta', 'slide-beta'];
    sliders.forEach(id => {
        const slideEl = document.getElementById(id);
        if (slideEl) {
            slideEl.addEventListener('input', updatePlayground);
        }
    });

    // Stagnation Recover & Manual Recover Buttons
    const btnStagRecover = document.getElementById('btn-stagnation-recover');
    if (btnStagRecover) {
        btnStagRecover.addEventListener('click', () => {
            showConfirmationModal(
                "Widen Priors & Proposals",
                "Are you sure you want to widen the parameter priors and proposal range? This will stop the active run and restart it using the Watchdog's recommendations.",
                "Widen & Restart",
                "Cancel",
                () => handleSamplerRecovery(0.20, 2.0)
            );
        });
    }
    const btnManualRecover = document.getElementById('btn-manual-recover');
    if (btnManualRecover) {
        btnManualRecover.addEventListener('click', () => {
            showConfirmationModal(
                "Widen Priors & Proposals",
                "Are you sure you want to widen the parameter priors and proposal range? This will stop the active run and restart it using the Watchdog's recommendations.",
                "Widen & Restart",
                "Cancel",
                () => handleSamplerRecovery(0.20, 2.0)
            );
        });
    }

    // Dismiss Stagnation Banner Button
    const btnStagDismiss = document.getElementById('btn-stagnation-dismiss');
    if (btnStagDismiss) {
        btnStagDismiss.addEventListener('click', () => {
            document.getElementById('stagnation-banner').style.display = 'none';
        });
    }

    // Download Repro Pack
    const btnDownloadRepro = document.getElementById('btn-download-repro');
    if (btnDownloadRepro) {
        btnDownloadRepro.addEventListener('click', () => {
            showConfirmationModal(
                "Package & Download",
                "Generate and download the journal submission reproducibility pack? This compiles the configuration, chains, best-fit stats, and plots into a single ZIP.",
                "Generate Pack",
                "Cancel",
                () => {
                    window.location.href = `${API_URL}/api/download_reproducibility_pack?config_name=${encodeURIComponent(activeConfig)}`;
                }
            );
        });
    }

    // Model Deformation Interpolator
    const slideDeform = document.getElementById('slide-deform-alpha');
    const valDeform = document.getElementById('val-deform-alpha');
    if (slideDeform && valDeform) {
        slideDeform.addEventListener('input', () => {
            const alpha = parseFloat(slideDeform.value);
            valDeform.textContent = alpha.toFixed(2);
            updateDeformation(alpha);
        });
    }

    // Parameter Freeze/Thaw
    document.querySelectorAll('.freeze-toggle').forEach(chk => {
        chk.addEventListener('change', async () => {
            const param = chk.getAttribute('data-param');
            const isSampled = chk.checked;
            appendLog(`[CONFIG] Sending freeze/thaw request: ${param} -> ${isSampled ? 'sampled (thawed)' : 'fixed (frozen)'}...`);
            try {
                const response = await fetch(`${API_URL}/api/freeze_thaw`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        parameter: param,
                        sampled: isSampled,
                        config_name: activeConfig
                    })
                });
                if (response.ok) {
                    const data = await response.json();
                    appendLog(`[CONFIG] Success: ${data.message}`);
                } else {
                    const data = await response.json();
                    appendLog(`[CONFIG] Freeze/Thaw failed: ${data.detail || 'unknown error'}`);
                }
            } catch (err) {
                appendLog(`[CONFIG] Freeze/Thaw communication error: ${err.message}`);
            }
        });
    });

    // Posterior Evolution Movie Compiler
    const btnCompileGif = document.getElementById('btn-compile-gif');
    if (btnCompileGif) {
        btnCompileGif.addEventListener('click', async () => {
            const originalText = btnCompileGif.textContent;
            btnCompileGif.disabled = true;
            btnCompileGif.textContent = "🎬 Compiling GIF... (takes a few seconds)";
            appendLog("[PIPELINE] Compiling captured history frames into an animated GIF...");
            try {
                const response = await fetch(`${API_URL}/api/download_posterior_gif`);
                if (response.ok) {
                    const blob = await response.blob();
                    const url = window.URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = url;
                    a.download = 'posterior_evolution.gif';
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);
                    window.URL.revokeObjectURL(url);
                    appendLog("[PIPELINE] GIF compilation complete and downloaded.");
                } else {
                    const errData = await response.json();
                    appendLog(`[PIPELINE] GIF compilation failed: ${errData.detail || 'check logs'}`);
                }
            } catch(err) {
                appendLog(`[PIPELINE] GIF compiler error: ${err.message}`);
            } finally {
                btnCompileGif.disabled = false;
                btnCompileGif.textContent = originalText;
            }
        });
    }

    // Likelihood Terrain Dropdowns
    const xSelect = document.getElementById('terrain-param-x');
    const ySelect = document.getElementById('terrain-param-y');
    if (xSelect) {
        xSelect.addEventListener('change', () => {
            refreshLikelihoodTerrain();
        });
    }
    if (ySelect) {
        ySelect.addEventListener('change', () => {
            refreshLikelihoodTerrain();
        });
    }

    // Timeline Archival & Replay
    const btnArchiveRun = document.getElementById('btn-archive-run');
    if (btnArchiveRun) {
        btnArchiveRun.addEventListener('click', async () => {
            btnArchiveRun.disabled = true;
            appendLog(`[ARCHIVE] Archiving current run output prefix to timestamped backup...`);
            try {
                const response = await fetch(`${API_URL}/api/archive_run`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ config_name: activeConfig })
                });
                if (response.ok) {
                    const data = await response.json();
                    appendLog(`[ARCHIVE] Success: ${data.message || 'Archived successfully'}`);
                } else {
                    const data = await response.json();
                    appendLog(`[ARCHIVE] Archiving failed: ${data.detail || 'unknown error'}`);
                }
            } catch (err) {
                appendLog(`[ARCHIVE] Archiving error: ${err.message}`);
            } finally {
                btnArchiveRun.disabled = false;
            }
        });
    }

    const btnArchiveReplay = document.getElementById('btn-archive-replay');
    if (btnArchiveReplay) {
        btnArchiveReplay.addEventListener('click', async () => {
            btnArchiveReplay.disabled = true;
            appendLog(`[REPLAY] First archiving current run outputs...`);
            try {
                const response = await fetch(`${API_URL}/api/archive_run`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ config_name: activeConfig })
                });
                if (response.ok) {
                    const data = await response.json();
                    appendLog(`[REPLAY] Archive completed: ${data.message || 'Archived successfully'}`);
                    appendLog(`[REPLAY] Replaying/Starting new run...`);
                    triggerRun(true);
                } else {
                    const data = await response.json();
                    appendLog(`[REPLAY] Archive phase failed: ${data.detail || 'unknown error'}. Aborting replay.`);
                }
            } catch (err) {
                appendLog(`[REPLAY] Archiving/Replay error: ${err.message}`);
            } finally {
                btnArchiveReplay.disabled = false;
            }
        });
    }
    // Run Configuration Template System
    refreshTemplatesList();

    const btnLoadTemplate = document.getElementById('btn-load-template');
    if (btnLoadTemplate) {
        btnLoadTemplate.addEventListener('click', async () => {
            const selectEl = document.getElementById('select-config-template');
            const templateName = selectEl.value;
            if (!templateName) {
                alert("Please select a template to load.");
                return;
            }
            const prevLabel = btnLoadTemplate.textContent;
            btnLoadTemplate.disabled = true;
            btnLoadTemplate.textContent = 'Loading…';
            if (yamlZone) yamlZone.classList.add('uploading');
            appendLog(`[TEMPLATES] Requesting load for template: ${templateName}...`);
            const controller = new AbortController();
            const loadTimeout = setTimeout(() => controller.abort(), 35000); // Increased to match backend 30s processing + margin for busy backend
            try {
                const response = await apiFetch(`${API_URL}/api/templates/load`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ name: templateName }),
                    signal: controller.signal,
                });
                clearTimeout(loadTimeout);
                if (response.ok) {
                    const data = await response.json();
                    appendLog(`[TEMPLATES] SUCCESS: ${data.message}`);
                    activeConfig = "uploaded_config.yaml";
                    yamlName.textContent = `Active Config: uploaded_config.yaml (Template: ${templateName})`;
                    yamlName.classList.add('active');
                    if (yamlZone) {
                        yamlZone.classList.add('has-model');
                        yamlZone.classList.remove('empty');
                    }
                    appendLog(`[TEMPLATES] Active configuration has been updated.`);
                } else {
                    const data = await response.json();
                    appendLog(`[TEMPLATES] Load template failed: ${data.detail || 'unknown error'}`);
                }
            } catch (err) {
                clearTimeout(loadTimeout);
                const msg = err.name === 'AbortError'
                    ? 'Template load timed out — backend may be busy. Close extra tabs and retry.'
                    : err.message;
                appendLog(`[TEMPLATES] Connection error: ${msg}`);
            } finally {
                btnLoadTemplate.disabled = false;
                btnLoadTemplate.textContent = prevLabel;
                if (yamlZone) yamlZone.classList.remove('uploading');
            }
        });
    }

    // Quick toggle buttons for LCDM and PRTOE
    if (btnToggleLcdm) {
        btnToggleLcdm.addEventListener('click', () => {
            const selectEl = document.getElementById('select-config-template');
            if (selectEl) {
                selectEl.value = 'lcdm_baseline';
                btnLoadTemplate.click();
            }
        });
    }
    if (btnTogglePrtoe) {
        btnTogglePrtoe.addEventListener('click', () => {
            const selectEl = document.getElementById('select-config-template');
            if (selectEl) {
                selectEl.value = 'prtoe_standard';
                btnLoadTemplate.click();
            }
        });
    }

    const btnSaveTemplate = document.getElementById('btn-save-template');
    if (btnSaveTemplate) {
        btnSaveTemplate.addEventListener('click', async () => {
            const nameEl = document.getElementById('input-template-name');
            const templateName = nameEl.value.trim();
            if (!templateName) {
                alert("Please enter a name for the custom template.");
                return;
            }
            appendLog(`[TEMPLATES] Saving current configuration as template: ${templateName}...`);
            try {
                const response = await apiFetch(`${API_URL}/api/templates/save`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        name: templateName,
                        config_name: activeConfig
                    })
                });
                if (response.ok) {
                    const data = await response.json();
                    appendLog(`[TEMPLATES] SUCCESS: ${data.message}`);
                    nameEl.value = '';
                    refreshTemplatesList();
                } else {
                    const data = await response.json();
                    appendLog(`[TEMPLATES] Save template failed: ${data.detail || 'unknown error'}`);
                }
            } catch (err) {
                appendLog(`[TEMPLATES] Connection error: ${err.message}`);
            }
        });
    }

    // Chain Quality Parameter Selector
    const qualityParamSelect = document.getElementById('select-quality-param');
    if (qualityParamSelect) {
        qualityParamSelect.addEventListener('change', () => {
            refreshChainQuality();
        });
    }

    // Save Checkpoint Button
    const btnSaveCheckpoint = document.getElementById('btn-save-checkpoint');
    if (btnSaveCheckpoint) {
        btnSaveCheckpoint.addEventListener('click', saveCheckpoint);
    }

    // Refresh Errors Button
    const btnRefreshErrors = document.getElementById('btn-refresh-errors');
    if (btnRefreshErrors) {
        btnRefreshErrors.addEventListener('click', refreshErrorLog);
    }

    // Clear Errors Button
    const btnClearErrors = document.getElementById('btn-clear-errors');
    if (btnClearErrors) {
        btnClearErrors.addEventListener('click', clearErrorLog);
    }

    // Initial load for Checkpoints and Errors
    refreshCheckpointsList();
    refreshErrorLog();

    // Initial: nebula ALWAYS visible as cosmic portal. Default counts as "model in" (has-model).
    // .running will be toggled live by status when sampler is executing.
    if (yamlZone) {
        yamlZone.classList.add('has-model');
        yamlZone.classList.remove('empty');
    }
});
