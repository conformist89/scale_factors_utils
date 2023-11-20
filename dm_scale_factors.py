import numpy as np
import matplotlib.pyplot as plt
import json
import argparse

parser = argparse.ArgumentParser(description="Plot the tau ID SF")
parser.add_argument("--era", type=str, default="2016postVFP", help="2016preVFP, 2016postVFP, 2017, 2018")
args = parser.parse_args()

# Given data
momentum = ["1-prong", r"1 prong +$\pi^{0}$", r"3 prong (+$\pi^{0}$)"]  # Updated momentum bin labels

if args.era == "2016postVFP":

    # postVFP DM binned data
    correction_factors = np.array([
        [0.95, 1.02, 0.99],  # vvvloose
        [0.97, 1.03, 0.96],  # vvloose
        [0.95, 1.048, 0.95],  # vloose
        [0.964, 1.024, 0.933],   # loose
        [0.953, 1.025, 0.95, ],  # medium
        [0.923, 1.012, 0.939],  # tight
        [0.897, 0.996, 0.901],  # vtight
        [0.852, 0.972, 0.903]   # vvtight
    ])

    up_uncertainties = np.array([
        [0.05, 0.04, 0.07],  # vvvloose
        [0.04, 0.04, 0.05],  # vvloose
        [0.04, 0.033, 0.04],  # vloose
        [0.035, 0.029, 0.035],  # loose
        [0.033, 0.028, 0.032],  # medium
        [0.032, 0.028, 0.031],  # tight
        [0.034, 0.028, 0.031],  # vtight
        [0.033, 0.028, 0.031]   # vvtight
    ])

    down_uncertainties = np.array([
        [0.05, 0.04, 0.07],  # vvvloose
        [0.04, 0.04, 0.05],  # vvloose
        [0.04, 0.033, 0.04],  # vloose
        [0.035, 0.029, 0.034],  # loose
        [0.033, 0.028, 0.032],  # medium
        [0.032, 0.027, 0.031],  # tight
        [0.034, 0.028, 0.03],  # vtight
        [0.033, 0.028, 0.032]   # vvtight
])


#preVFP DM binned data

if args.era == "2016preVFP":

    correction_factors = np.array([
        [1.08887, 1.03, 1.05],  # vvvloose
        [1.05, 1.11, 1.05],  # vvloose
        [1.04, 1.12, 1.06],  # vloose
        [1.06, 1.096, 1.006],   # loose
        [1.03, 1.104, 0.973,],  # medium
        [0.98, 1.09, 0.953,],  # tight
        [0.932, 1.065, 0.906],  # vtight
        [0.868, 1.058, 0.905]   # vvtight
    ])

    up_uncertainties = np.array([
        [0.06, 0.07, 0.08],  # vvvloose
        [0.05, 0.05, 0.05],  # vvloose
        [0.04, 0.04, 0.04],  # vloose
        [0.04, 0.033, 0.029],  # loose
        [0.04, 0.03, 0.029],  # medium
        [0.04, 0.03, 0.029],  # tight
        [0.035, 0.029, 0.031],  # vtight
        [0.035, 0.030, 0.03]   # vvtight
    ])

    down_uncertainties = np.array([
    [0.05889, 0.07143, 0.09004],
    [0.04768, 0.04896, 0.05649],
    [0.04336, 0.0397 , 0.04016],
    [0.03697, 0.03301, 0.03068],
    [0.03647, 0.03119, 0.02904],
    [0.0365, 0.03046, 0.02956],
    [0.03442, 0.02967, 0.03208],
    [0.03568, 0.03061, 0.03128],
    ])


working_points = ['vvvloose', 'vvloose', 'vloose', 'loose', 'medium', 'tight', 'vtight', 'vvtight']
x_labels = ["1-prong", r"1 prong +$\pi^{0}$", r"3 prong (+$\pi^{0}$)"]

def get_pt_correction_factors(era, user_out_tag, channel, round_to=4):

    corrfactor_wps_dict = {}
    up_uncertainties_wps_dict = {}
    down_uncertainties_wps_dict = {}

    for i in range(len(working_points)):

        json_sfs = "/work/olavoryk/tau_pog_tau_sfs/tauid_multifit/smhtt_ul/Tau_"+str(working_points[i])+"_"+str(era)+"UL_"+str(channel)+"_"+str(user_out_tag[i])+".json"


        with open(json_sfs, 'r') as f:
            data = json.load(f)

        dm_binned_data = data["corrections"][1]

        content = dm_binned_data["data"]["content"][0]

        content2 = content['value']['content']

        roundnumber = round_to


        up_list = []
        down_list = []
        nom_list = []

        for element in content2[:-1]:
            

            nom_list.append(round( element['value']['content'][0]['value'],roundnumber ))
            up_list.append(round( element['value']['content'][1]['value'] - element['value']['content'][0]['value'], roundnumber ))
            down_list.append(abs(round( element['value']['content'][0]['value'] - element['value']['content'][2]['value'], roundnumber )))



        corrfactor_wps_dict[working_points[i]] = nom_list
        up_uncertainties_wps_dict[working_points[i]] = up_list
        down_uncertainties_wps_dict[working_points[i]] = down_list

    lists_nom = list(corrfactor_wps_dict.values())
    lists_up = list(up_uncertainties_wps_dict.values())
    lists_down = list(down_uncertainties_wps_dict.values())

    # Create a NumPy array from the lists

    correction_factors = np.array(lists_nom)
    up_uncertainties = np.array(lists_up)
    down_uncertainties = np.array(lists_down)

    return correction_factors, up_uncertainties, down_uncertainties



# user_out_tags_2016postVFP = ["vvvloose_vs_jet_vvloose_vs_ele_6Nov_v2", "vvloose_vs_jet_vvloose_vs_ele_6Nov_v2", "vloose_vs_jet_vvloose_vs_ele_6Nov_v2",
#                               "loose_vs_jet_vvloose_vs_ele_6Nov_v2", "medium_vs_jet_vvloose_vs_ele_6Nov_v2",
#                                 "tight_vs_jet_vvloose_vs_ele_6Nov_v2", "vtight_vs_jet_vvloose_vs_ele_6Nov_v2", "vvtight_vs_jet_vvloose_vs_ele_6Nov_v2"]


# correction_factors, up_uncertainties, down_uncertainties = get_pt_correction_factors('2016preVFP', user_out_tags_2016postVFP, 'mt',5)


# print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Correction factors: \n")
# print(correction_factors)

# print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Up uncertainties \n")
# print(up_uncertainties)

# print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Down uncertainties \n")
# print(down_uncertainties)

lumilabel = r"16.8 $fb^{-1}$"+" (2016 preVFP UL) (13 TeV)"
outname = "2016postVFP_scele_factors_DM"

if args.era == "2016preVFP":
    lumilabel = r"19.7 $fb^{-1}$"+" (2016 preVFP UL) (13 TeV)"
    outname = "2016preVFP_scele_factors_DM"


# Plotting subplots arranged in a table format (2 columns, 4 rows)
fig, axs = plt.subplots(4, 2, figsize=(10, 12), sharex='col', sharey='row')
for i, ax in enumerate(axs.flat):
    ax.errorbar(momentum, correction_factors[i], yerr=[down_uncertainties[i], up_uncertainties[i]], fmt='o', label=working_points[i]+ ' vsJet', elinewidth =3)
    ax.set_xticks(momentum)
    ax.set_xticklabels(x_labels, fontsize=15)
    ax.grid(True)
    ax.legend(fontsize=13)
    if i >= 6:  # Only set x-axis label for bottom subplots
        ax.set_xlabel(r"$\tau$ $p_{T}$"+" GeV", fontsize=15)
    if i % 2 != 0 and i != 7:  # Remove 'Correction Factors' label for right-side plots and last plot
        ax.set_ylabel('')  # Empty label for right-side plots and last plot
        ax.set_title('')
    else:  # Add 'Correction Factors' label for left-side plots except the last one
        if i == 0:  # Set titles for the first two plots
            ax.set_title(r"$\tau$ ID scale factors", fontsize=20)
        else:
            ax.set_title('')
    if i == 0 or i == 2 or i == 4 or i == 6:
         ax.set_ylabel('Correction Factors', fontsize=12)
    if i == 1:
            ax.set_title(lumilabel, fontsize=20)
    ax.axhline(y=1, color='red', linestyle='--', linewidth = 5)  # Adding the red line at y=1
        

plt.tight_layout()

# Save as PDF and PNG
plt.savefig(outname+".pdf")
plt.savefig(outname+".png", dpi=300)  # High-resolution PNG

plt.show()