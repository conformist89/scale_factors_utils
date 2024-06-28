import matplotlib.pyplot as plt
import numpy as np
import sys
import os

# Data for tau ID scale factors
central_values_tau_id = [0.925, 1.130, 1.018]
err_up_tau_id = [0.079, 0.065, 0.061]
err_down_tau_id = [0.093, 0.089, 0.050]

# Data for tau ES shift percentages and uncertainties
tau_es_shift = [-0.600, -1.400, -1.193,]
tau_es_shift_up = [1.348, 0.434, 0.567]
tau_es_shift_down = [-0.969, -0.999, -0.468]

# X-axis labels
x_labels = ["1 Prong", "1 Prong + $\pi^{0}$", "3 Prong"]

# X-axis positions
x_pos = np.arange(len(x_labels))

# Command-line argument for era
if len(sys.argv) < 2:
    print("Usage: python script.py <era>")
    sys.exit(1)

era = sys.argv[1]

# Determine luminosity based on era
if era == "2016preVFP":
    lumi = "19.5"
elif era == "2016postVFP":
    lumi = "16.8"
elif era == "2017":
    lumi = "41.529"
elif era == "2018":
    lumi = "59.83"
else:
    print(f"Unknown era: {era}")
    sys.exit(1)

# Create folder if it doesn't exist
folder_name = f"id_es_comb_{era}"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Font sizes
title_fontsize = 20
label_fontsize = 18
tick_fontsize = 15

# Create figure and subplots
fig, (a0, a1) = plt.subplots(2, 1, figsize=(10, 10))

# Upper panel: Tau ID scale factors
a0.errorbar(x_pos, central_values_tau_id, 
            yerr=[err_down_tau_id, err_up_tau_id], 
            fmt='o', capsize=5, label='Tau ID Scale Factors')

a0.set_xticks(x_pos)
a0.set_xticklabels(x_labels, fontsize=tick_fontsize)
a0.set_ylabel('Scale Factor', fontsize=label_fontsize)
a0.set_title('CMS $Preliminary$', loc='left', fontsize=title_fontsize)
a0.set_title(f"{era} {lumi} "+ " fb$^{-1}$  (13 TeV)", loc='right', fontsize=title_fontsize)
a0.legend(fontsize=label_fontsize)

# Add a red dotted line at y=1
a0.axhline(y=1, color='red', linewidth=3, linestyle='--')

# Save upper panel as PDF and PNG
plot_filename_upper = os.path.join(folder_name, f"tau_id_scale_factors_{era}.pdf")
plt.savefig(plot_filename_upper)
plt.savefig(plot_filename_upper.replace(".pdf", ".png"))

# Lower panel: Tau ES shift in %
a1.errorbar(x_pos, tau_es_shift, 
            yerr=[tau_es_shift_down, tau_es_shift_up], 
            fmt='o', capsize=5, label='Tau ES Shift',
            color='green')  # Set the color to green

a1.set_xticks(x_pos)
a1.set_xticklabels(x_labels, fontsize=tick_fontsize)
a1.set_ylabel('ES Shift (%)', fontsize=label_fontsize)
a1.legend(fontsize=label_fontsize)

# Save lower panel as PDF and PNG
plot_filename_lower = os.path.join(folder_name, f"tau_es_shift_{era}.pdf")
plt.savefig(plot_filename_lower)
plt.savefig(plot_filename_lower.replace(".pdf", ".png"))

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot (optional)
# plt.show()

# Close the figure to release memory
plt.close(fig)

print(f"Plots saved in {folder_name}/")