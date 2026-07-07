function initCharts() {
    // Destroy all previous Chart instances to prevent memory leaks on re-init (e.g. reconnects, tab changes, long running dashboard).
    [chartWMu, chartFSigma8, chartInfluence, chartCompareW, chartCompareFs8, chartSensitivity, chartPlaygroundRatio, chartTerrain, chartResiduals, chartQualityTrace, chartQualityAutocorr, chartPerPointResiduals, chartRunCompareShifts].forEach(c => {
        if (c) { try { c.destroy(); } catch(e){} }
    });
    chartWMu = chartFSigma8 = chartInfluence = chartCompareW = chartCompareFs8 = chartSensitivity = chartPlaygroundRatio = chartTerrain = chartResiduals = chartQualityTrace = chartQualityAutocorr = chartPerPointResiduals = chartRunCompareShifts = null;

    const ctxWMu = document.getElementById('chart-w-mu').getContext('2d');
    chartWMu = new Chart(ctxWMu, {
        type: 'line',
        data: {
            labels: [],
            datasets: [
                {
                    label: 'Equation of State w(z)',
                    data: [],
                    borderColor: '#00d2d3',
                    backgroundColor: 'rgba(0, 210, 211, 0.05)',
                    fill: false,
                    borderWidth: 2,
                    tension: 0.1
                },
                {
                    label: 'Gravitational Pull \u03bc(z)',
                    data: [],
                    borderColor: '#ff9ff3',
                    backgroundColor: 'rgba(255, 159, 243, 0.05)',
                    fill: false,
                    borderWidth: 2,
                    tension: 0.1
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    title: { display: true, text: 'Redshift z', color: '#a4b0be' },
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#a4b0be' }
                },
                y: {
                    title: { display: true, text: 'w(z) / \u03bc(z)', color: '#a4b0be' },
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#a4b0be' }
                }
            },
            plugins: {
                legend: { labels: { color: '#fff', font: { size: 10 } } }
            }
        }
    });

    const ctxFSigma8 = document.getElementById('chart-f-sigma8').getContext('2d');
    if (chartFSigma8) { try { chartFSigma8.destroy(); } catch(e){} chartFSigma8 = null; }
    chartFSigma8 = new Chart(ctxFSigma8, {
        type: 'line',
        data: {
            labels: [],
            datasets: [
                {
                    label: 'Structure Growth f\u03c3\u2088(z)',
                    data: [],
                    borderColor: '#39ff14',
                    backgroundColor: 'rgba(57, 255, 20, 0.05)',
                    fill: true,
                    borderWidth: 2,
                    tension: 0.1
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    title: { display: true, text: 'Redshift z', color: '#a4b0be' },
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#a4b0be' }
                },
                y: {
                    title: { display: true, text: 'f\u03c3\u2088(z)', color: '#a4b0be' },
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#a4b0be' }
                }
            },
            plugins: {
                legend: { labels: { color: '#fff', font: { size: 10 } } }
            }
        }
    });

    const ctxInfluence = document.getElementById('chart-influence').getContext('2d');
    if (chartInfluence) { try { chartInfluence.destroy(); } catch(e){} chartInfluence = null; }
    chartInfluence = new Chart(ctxInfluence, {
        type: 'bar',
        data: {
            labels: ['CMB Likelihood', 'BAO Likelihood', 'DESI BAO', 'Supernovae (SN)', 'Lensing', 'Total \u03c7\u00b2 Score'],
            datasets: [
                {
                    label: '\u0394\u03c7\u00b2 Relative to \u039bCDM',
                    data: [0, 0, 0, 0, 0, 0],
                    backgroundColor: [
                        'rgba(56, 103, 214, 0.6)',
                        'rgba(254, 202, 87, 0.6)',
                        'rgba(255, 159, 243, 0.6)',
                        'rgba(255, 71, 87, 0.6)',
                        'rgba(57, 255, 20, 0.6)',
                        'rgba(0, 210, 211, 0.6)'
                    ],
                    borderColor: [
                        '#3867d6',
                        '#feca57',
                        '#ff9ff3',
                        '#ff4757',
                        '#39ff14',
                        '#00d2d3'
                    ],
                    borderWidth: 1
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#a4b0be' }
                },
                y: {
                    title: { display: true, text: '\u0394\u03c7\u00b2 difference', color: '#a4b0be' },
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#a4b0be' }
                }
            },
            plugins: {
                legend: { display: false }
            }
        }
    });

    const ctxCompareW = document.getElementById('chart-compare-w').getContext('2d');
    chartCompareW = new Chart(ctxCompareW, {
        type: 'line',
        data: {
            labels: [],
            datasets: []
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    title: { display: true, text: 'Redshift z', color: '#a4b0be' },
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#a4b0be' }
                },
                y: {
                    title: { display: true, text: 'w(z)', color: '#a4b0be' },
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#a4b0be' }
                }
            },
            plugins: {
                legend: { labels: { color: '#fff', font: { size: 9 } } }
            }
        }
    });

    const ctxCompareFs8 = document.getElementById('chart-compare-fs8').getContext('2d');
    chartCompareFs8 = new Chart(ctxCompareFs8, {
        type: 'line',
        data: {
            labels: [],
            datasets: []
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    title: { display: true, text: 'Redshift z', color: '#a4b0be' },
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#a4b0be' }
                },
                y: {
                    title: { display: true, text: 'f\u03c3\u2088(z)', color: '#a4b0be' },
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#a4b0be' }
                }
            },
            plugins: {
                legend: { labels: { color: '#fff', font: { size: 9 } } }
            }
        }
    });

    const ctxSensitivity = document.getElementById('chart-sensitivity').getContext('2d');
    chartSensitivity = new Chart(ctxSensitivity, {
        type: 'bar',
        data: {
            labels: ['xi_prtoe', 'delta_prtoe', 'zeta_prtoe', 'beta_prtoe'],
            datasets: [
                {
                    label: 'dH\u2080 / d\u03b8',
                    data: [0, 0, 0, 0],
                    backgroundColor: 'rgba(0, 210, 211, 0.6)',
                    borderColor: '#00d2d3',
                    borderWidth: 1
                },
                {
                    label: 'dS\u2088 / d\u03b8',
                    data: [0, 0, 0, 0],
                    backgroundColor: 'rgba(254, 202, 87, 0.6)',
                    borderColor: '#feca57',
                    borderWidth: 1
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#a4b0be' }
                },
                y: {
                    title: { display: true, text: 'Sensitivity derivative', color: '#a4b0be' },
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#a4b0be' }
                }
            },
            plugins: {
                legend: { labels: { color: '#fff', font: { size: 10 } } }
            }
        }
    });

    const ctxPlayground = document.getElementById('chart-playground-ratio').getContext('2d');
    chartPlaygroundRatio = new Chart(ctxPlayground, {
        type: 'line',
        data: {
            labels: [],
            datasets: [
                {
                    label: 'H(z) / H_\u039bCDM(z)',
                    data: [],
                    borderColor: '#39ff14',
                    backgroundColor: 'rgba(57, 255, 20, 0.05)',
                    fill: true,
                    borderWidth: 2,
                    tension: 0.1
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    title: { display: true, text: 'Redshift z', color: '#a4b0be' },
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#a4b0be' }
                },
                y: {
                    title: { display: true, text: 'Ratio H(z)/H_\u039bCDM(z)', color: '#a4b0be' },
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#a4b0be' }
                }
            },
            plugins: {
                legend: { display: false }
            }
        }
    });

    const ctxTerrain = document.getElementById('chart-terrain').getContext('2d');
    chartTerrain = new Chart(ctxTerrain, {
        type: 'scatter',
        data: {
            datasets: [{
                label: 'Likelihood Samples',
                data: [],
                pointRadius: 4,
                pointHoverRadius: 6
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    title: { display: true, text: 'Param X', color: '#a4b0be' },
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#a4b0be' }
                },
                y: {
                    title: { display: true, text: 'Param Y', color: '#a4b0be' },
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#a4b0be' }
                }
            },
            plugins: {
                legend: { display: false },
                tooltip: {
                    callbacks: {
                        label: function(ctx) {
                            return `X: ${ctx.raw.x.toFixed(4)}, Y: ${ctx.raw.y.toFixed(4)}, Chi2: ${ctx.raw.chi2.toFixed(2)}`;
                        }
                    }
                }
            }
        }
    });

    const ctxResiduals = document.getElementById('chart-residuals').getContext('2d');
    chartResiduals = new Chart(ctxResiduals, {
        type: 'line',
        data: {
            labels: [],
            datasets: [
                {
                    label: 'Supernovae (SN) Residuals',
                    data: [],
                    borderColor: '#ff4757',
                    backgroundColor: 'rgba(255, 71, 87, 0.1)',
                    borderWidth: 2,
                    showLine: true,
                    fill: false,
                    tension: 0.1
                },
                {
                    label: 'BAO Distance Residuals',
                    data: [],
                    borderColor: '#feca57',
                    backgroundColor: 'rgba(254, 202, 87, 0.1)',
                    borderWidth: 2,
                    showLine: true,
                    fill: false,
                    tension: 0.1
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    title: { display: true, text: 'Redshift z', color: '#a4b0be' },
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#a4b0be' }
                },
                y: {
                    title: { display: true, text: '(PRTOE - \u039bCDM) / \u039bCDM', color: '#a4b0be' },
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#a4b0be' }
                }
            },
            plugins: {
                legend: { labels: { color: '#fff', font: { size: 10 } } }
            }
        }
    });

    const ctxTrace = document.getElementById('chart-quality-trace').getContext('2d');
    chartQualityTrace = new Chart(ctxTrace, {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'Trace Path',
                data: [],
                borderColor: '#ff9ff3',
                backgroundColor: 'rgba(255, 159, 243, 0.05)',
                borderWidth: 1.5,
                pointRadius: 0,
                fill: false,
                tension: 0.05
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    title: { display: true, text: 'Iteration', color: '#a4b0be' },
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#a4b0be' }
                },
                y: {
                    title: { display: true, text: 'Value', color: '#a4b0be' },
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#a4b0be' }
                }
            },
            plugins: {
                legend: { display: false }
            }
        }
    });

    const ctxAutocorr = document.getElementById('chart-quality-autocorr').getContext('2d');
    chartQualityAutocorr = new Chart(ctxAutocorr, {
        type: 'bar',
        data: {
            labels: [],
            datasets: [{
                label: 'Autocorrelation r_k',
                data: [],
                backgroundColor: 'rgba(0, 210, 211, 0.6)',
                borderColor: '#00d2d3',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    title: { display: true, text: 'Lag', color: '#a4b0be' },
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#a4b0be' }
                },
                y: {
                    title: { display: true, text: 'Correlation r_k', color: '#a4b0be' },
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#a4b0be' }
                }
            },
            plugins: {
                legend: { display: false }
            }
        }
    });

    const ctxPerPoint = document.getElementById('chart-perpoint-residuals').getContext('2d');
    chartPerPointResiduals = new Chart(ctxPerPoint, {
        type: 'bar',
        data: {
            labels: [],
            datasets: [{
                label: 'Residual / Chi2',
                data: [],
                backgroundColor: 'rgba(0, 210, 211, 0.6)',
                borderColor: '#00d2d3',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#a4b0be', font: { size: 9 } }
                },
                y: {
                    title: { display: true, text: 'Residual Value', color: '#a4b0be' },
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#a4b0be' }
                }
            },
            plugins: {
                legend: { display: false }
            }
        }
    });

    const ctxRunCompare = document.getElementById('chart-runcompare-shifts').getContext('2d');
    chartRunCompareShifts = new Chart(ctxRunCompare, {
        type: 'bar',
        data: {
            labels: [],
            datasets: [{
                label: 'Parameter Shift (N_sigma)',
                data: [],
                backgroundColor: 'rgba(255, 159, 243, 0.6)',
                borderColor: '#ff9ff3',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#a4b0be' }
                },
                y: {
                    title: { display: true, text: 'Significance (N_sigma)', color: '#a4b0be' },
                    grid: { color: 'rgba(255,255,255,0.05)' },
                    ticks: { color: '#a4b0be' }
                }
            },
            plugins: {
                legend: { display: false }
            }
        }
    });
}
