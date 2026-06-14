import os
import getdist
from getdist import plots, mcsamples
import matplotlib.pyplot as plt

# Define paths
project_dir = os.path.abspath(os.path.dirname(__file__))
lcdm_prefix = os.path.join(project_dir, "lcdm_poly")

# Fallback to chains/ directory if moved
if not os.path.exists(lcdm_prefix + ".1.txt") and not os.path.exists(lcdm_prefix + ".txt"):
    lcdm_prefix = os.path.join(project_dir, "chains", "lcdm_poly")

if not os.path.exists(lcdm_prefix + ".1.txt") and not os.path.exists(lcdm_prefix + ".txt"):
    print(f"Error: Final chain files not found for prefix '{lcdm_prefix}'.")
    print("LCDM PolyChord is likely still running! Cobaya only generates the final .txt files used by GetDist once the nested sampling has completely finished.")
    exit(1)

prtoe_prefix = os.path.join(project_dir, "chains", "prtoe_poly_optimized")
if not os.path.exists(prtoe_prefix + ".1.txt") and not os.path.exists(prtoe_prefix + ".txt"):
    print(f"Error: Final chain files not found for prefix '{prtoe_prefix}'.")
    print("PRTOE PolyChord is likely still running! Please wait for both runs to finish before plotting.")
    exit(1)

# Load the LCDM samples (ignoring the first 30% of the chain as burn-in)
lcdm_samples = getdist.mcsamples.loadMCSamples(lcdm_prefix, settings={'ignore_rows': 0.3})

# Load the PRTOE samples
prtoe_samples = getdist.mcsamples.loadMCSamples(prtoe_prefix, settings={'ignore_rows': 0.3})

# Parameters we want to visualize
params = ['omega_b', 'omega_cdm', 'H0', 'n_s', 'z_reio']

# Generate the corner plot
g = plots.get_subplot_plotter()
g.triangle_plot([lcdm_samples, prtoe_samples], params, filled=True, legend_labels=[r'$\Lambda$CDM Baseline', 'PRTOE Optimized'])

# Save the figure
output_path = os.path.join(project_dir, "comparison_corner_plot.png")
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Plot successfully saved to {output_path}")