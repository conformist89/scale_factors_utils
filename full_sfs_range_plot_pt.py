import numpy as np
import matplotlib.pyplot as plt
import json
import argparse


parser = argparse.ArgumentParser(description="Plot the tau ID SF")
parser.add_argument("--era", type=str, default="2016postVFP", help="2016preVFP, 2016postVFP, 2017, 2018")
args = parser.parse_args()

# Given data
momentum = np.linspace(1, 5, 5)


if args.era == "2016postVFP":

    # postVFP pt binned data
    correction_factors = np.array([
        [0.93, 0.94, 0.97, 0.99, 0.94 ],  # vvvloose
        [1.03, 0.98, 1.014,0.996, 0.978],  # vvloose
        [1.04, 1.005, 1.019, 1.005, 0.988],  # vloose
        [1.052, 1.0, 1.004, 1.004, 1.002],   # loose
        [1.005, 0.995, 0.994, 1.011, 1.00],  # medium
        [1.024, 0.98, 0.982, 1.003, 0.979],  # tight
        [1.017, 0.973, 0.973, 0.984, 0.961],  # vtight
        [0.998, 0.959, 0.945, 0.968, 0.935,]   # vvtight
    ])

    up_uncertainties = np.array([
        [0.06, 0.04, 0.03, 0.03, 0.03 ],  # vvvloose
        [0.05, 0.03, 0.028, 0.027, 0.026],  # vvloose
        [0.04, 0.03, 0.025, 0.024, 0.025],  # vloose
        [0.036, 0.027, 0.023, 0.023, 0.023],  # loose
        [0.033, 0.025, 0.023,0.023, 0.023 ],  # medium
        [0.03, 0.024, 0.022, 0.023, 0.023 ],  # tight
        [0.033, 0.028, 0.025, 0.027, 0.026],  # vtight
        [0.028, 0.025, 0.021,0.023, 0.022 ]   # vvtight
    ])

    down_uncertainties = np.array([
        [0.06, 0.04, 0.03, 0.03, 0.03 ],  # vvvloose
        [0.05, 0.03, 0.027, 0.026, 0.026],  # vvloose
        [0.04, 0.028, 0.024, 0.024, 0.024],  # vloose
        [0.035, 0.026, 0.022, 0.023, 0.022],  # loose
        [0.032, 0.024, 0.022, 0.022, 0.022],  # medium
        [0.03, 0.024, 0.021, 0.022, 0.022],  # tight
        [0.032, 0.026, 0.025, 0.025, 0.025],  # vtight
        [0.029, 0.036, 0.032, 0.022, 0.022]   # vvtight
    ])


if args.era == "2016preVFP":

#preVFP pt binned data

    correction_factors = np.array(
    [
        [1.09, 1.02, 1.02, 1.02, 1.01],
        [1.08, 1.00, 1.035, 1.015, 1.016],
        [1.08596, 1.01, 1.023, 1.008, 1.05047],

        [1.12177, 1.03911, 1.03061, 1.011, 1.03504], #loose
        [1.07132, 1.008, 1.009, 1.003, 1.002], #medium
        [1.06487, 0.99579, 1.015, 1.016, 1.01], # tight
        [1.034, 0.98149, 1.002, 1.004, 0.98306], # vtight
        [1.037,   0.97556, 0.99091, 0.98637, 0.96467], # vvtight
    ]
    )

    up_uncertainties = np.array(
        [[0.11, 0.06, 0.04, 0.04, 0.04], # vvvloose

        [0.08,  0.05, 0.035, 0.033, 0.032], # vvloose

        [0.0617,  0.04, 0.031,  0.028, 0.029], #vloose

        [0.05, 0.031, 0.02614, 0.024 ,0.02474],  # loose

        [0.03887, 0.028, 0.025, 0.023 ,0.024], # medium
        [0.03365, 0.02532, 0.023, 0.022, 0.024], # tight
        [0.032,  0.024 ,0.023,  0.022, 0.02323], #vtight
        [0.03132, 0.02324, 0.02375, 0.02286, 0.02359],] #vvtight
    )

    down_uncertainties = np.array(

    [
    [0.11178, 0.06428, 0.04608, 0.04119, 0.04085], # vvvloose
    [0.08286, 0.04922, 0.03761, 0.03436, 0.03319], # vvloose
    [0.06547, 0.0408 , 0.03149, 0.02966, 0.02863], # vloose

    [0.04729, 0.03171, 0.02716, 0.02498, 0.02574], # loose
    [0.04157, 0.02954, 0.02551, 0.02354, 0.02432], # medium
    [0.03486, 0.0267 , 0.02444, 0.02353, 0.02393], # tight

    [0.03445, 0.02533, 0.02448, 0.0234,  0.02414], # vtight
    [0.03335, 0.02435, 0.02463, 0.02307, 0.0243 ], # vvtight
    ]

    )

working_points = ['vvvloose', 'vvloose', 'vloose', 'loose', 'medium', 'tight', 'vtight', 'vvtight']
x_labels = ['20-25', '25-30', '30-35', '35-40', '>40']

def get_pt_correction_factors(era, user_out_tag, channel, round_to=4):

    corrfactor_wps_dict = {}
    up_uncertainties_wps_dict = {}
    down_uncertainties_wps_dict = {}

    for i in range(len(working_points)):

        json_sfs = "/work/olavoryk/tau_pog_tau_sfs/tauid_multifit/smhtt_ul/Tau_"+str(working_points[i])+"_"+str(era)+"UL_"+str(channel)+"_"+str(user_out_tag[i])+".json"


        with open(json_sfs, 'r') as f:
            data = json.load(f)

        pt_binned_data = data["corrections"][0]

        content = pt_binned_data["data"]["content"][0]

        content1 = content['value']['content']

        pt_range = [ 20.0, 25.0, 30.0, 35.0, 40.0, 10000.0 ]

        roundnumber = round_to


        up_list = []
        down_list = []
        nom_list = []

        for element in content1:
            # print("\n  Nom: ", round(element['content'][0]['value'],roundnumber))

            # print(" Up: ", round(element['content'][1]['value'] - element['content'][0]['value'],roundnumber))
            # print(" down: ", round(element['content'][0]['value'] - element['content'][2]['value'],roundnumber))

            up_list.append(round(element['content'][1]['value'] - element['content'][0]['value'],roundnumber))
            down_list.append(abs(round(element['content'][0]['value'] - element['content'][2]['value'],roundnumber)))
            nom_list.append( round(element['content'][0]['value'],roundnumber) )

            # print(str(round(element['content'][0]['value'],roundnumber))+'$^{+'+str(round(element['content'][1]['value'] - element['content'][0]['value'],roundnumber))+'}_{-'+str(round(element['content'][0]['value'] - element['content'][2]['value'],roundnumber))+'}$')



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



# user_out_tags_2016postVFP = ["vvvloose_vs_jet_vvloose_vs_ele_6Nov_v1", "vvloose_vs_jet_vvloose_vs_ele_6Nov_v1", "vloose_vs_jet_vvloose_vs_ele_6Nov_v1",
#                               "loose_vs_jet_vvloose_vs_ele_6Nov_v1", "medium_vs_jet_vvloose_vs_ele_6Nov_v1",
#                                 "tight_vs_jet_vvloose_vs_ele_6Nov_v1", "vtight_vs_jet_vvloose_vs_ele_6Nov_v1", "vvtight_vs_jet_vvloose_vs_ele_6Nov_v1"]


# correction_factors, up_uncertainties, down_uncertainties = get_pt_correction_factors('2016preVFP', user_out_tags_2016postVFP, 'mt',5)

# print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Correction factors: \n")
# print(correction_factors)

# print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Up uncertainties \n")
# print(up_uncertainties)

# print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Down uncertainties \n")
# print(down_uncertainties)


lumilabel = r"16.8 $fb^{-1}$"+" (2016 preVFP UL) (13 TeV)"
outname = "2016postVFP_scele_factors_pt"

if args.era == "2016preVFP":
    lumilabel = r"19.7 $fb^{-1}$"+" (2016 preVFP UL) (13 TeV)"
    outname = "2016preVFP_scele_factors_pt"

# Plotting subplots arranged in a table format (2 columns, 4 rows)
fig, axs = plt.subplots(4, 2, figsize=(10, 12), sharex='col', sharey='row')
for i, ax in enumerate(axs.flat):
    ax.errorbar(momentum, correction_factors[i], yerr=[down_uncertainties[i], up_uncertainties[i]], fmt='o', label=working_points[i]+ ' vsJet', elinewidth =3)
    ax.set_xticks(momentum)
    ax.set_xticklabels(x_labels, fontsize=15)
    ax.grid(True)
    ax.legend(fontsize=13)
    if i >= 6:  # Only set x-axis label for bottom subplots
        ax.set_xlabel(r"$\tau$ $p_{T}$ "+" GeV", fontsize=15)
    if i % 2 != 0 and i != 7:  # Remove 'Correction Factors' label for right-side plots and last plot
        ax.set_ylabel('')  # Empty label for right-side plots and last plot
        ax.set_title('')
    else:  # Add 'Correction Factors' label for left-side plots except the last one
        if i == 0 or i == 1:  # Set titles for the first two plots
            ax.set_title(r"$\tau$ ID scale factors", fontsize=20)
        else:
            ax.set_title('')
    if i == 0 or i == 2 or i == 4 or i == 6:
         ax.set_ylabel('Correction Factors', fontsize=15)
    if i == 1:
            ax.set_title(r"19.5 $fb^{-1}$"+" (2016 preVFP UL) (13 TeV)", fontsize=20)
    ax.axhline(y=1, color='red', linestyle='--', linewidth = 5)  # Adding the red line at y=1
        

plt.tight_layout()

# Save as PDF and PNG
plt.savefig(outname+".pdf")
plt.savefig(outname+".png", dpi=300)  # High-resolution PNG


plt.show()