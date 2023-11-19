import numpy as np
import matplotlib.pyplot as plt
import json

# Given data
momentum = np.linspace(1, 5, 5)
correction_factors = np.array([
    [],  # vvvloose
    [],  # vvloose
    [],  # vloose
    [],   # loose
    [],  # medium
    [],  # tight
    [],  # vtight
    []   # vvtight
])

up_uncertainties = np.array([
    [],  # vvvloose
    [],  # vvloose
    [],  # vloose
    [],  # loose
    [],  # medium
    [],  # tight
    [],  # vtight
    []   # vvtight
])

down_uncertainties = np.array([
    [],  # vvvloose
    [],  # vvloose
    [],  # vloose
    [],  # loose
    [],  # medium
    [],  # tight
    [],  # vtight
    []   # vvtight
])

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



user_out_tags_2016postVFP = ["vvvloose_vs_jet_vvloose_vs_ele_6Nov_v2", "vvloose_vs_jet_vvloose_vs_ele_6Nov_v2", "vloose_vs_jet_vvloose_vs_ele_6Nov_v2",
                              "loose_vs_jet_vvloose_vs_ele_6Nov_v2", "medium_vs_jet_vvloose_vs_ele_6Nov_v2",
                                "tight_vs_jet_vvloose_vs_ele_6Nov_v2", "vtight_vs_jet_vvloose_vs_ele_6Nov_v2", "vvtight_vs_jet_vvloose_vs_ele_6Nov_v2"]


correction_factors, up_uncertainties, down_uncertainties = get_pt_correction_factors('2016postVFP', user_out_tags_2016postVFP, 'mt',5)




# Plotting subplots arranged in a table format (2 columns, 4 rows)
fig, axs = plt.subplots(4, 2, figsize=(10, 12), sharex='col', sharey='row')
for i, ax in enumerate(axs.flat):
    ax.errorbar(momentum, correction_factors[i], yerr=[down_uncertainties[i], up_uncertainties[i]], fmt='o', label=working_points[i]+ ' vsJet')
    ax.set_xticks(momentum)
    ax.set_xticklabels(x_labels, fontsize=10)
    ax.grid(True)
    ax.legend(fontsize=10)
    if i >= 6:  # Only set x-axis label for bottom subplots
        ax.set_xlabel(r"$\tau$ $p_{T}$", fontsize=12)
    if i % 2 != 0 and i != 7:  # Remove 'Correction Factors' label for right-side plots and last plot
        ax.set_ylabel('')  # Empty label for right-side plots and last plot
        ax.set_title('')
    else:  # Add 'Correction Factors' label for left-side plots except the last one
        if i == 0 or i == 1:  # Set titles for the first two plots
            ax.set_title(r"$\tau$ ID scale factors", fontsize=14)
        else:
            ax.set_title('')
    if i == 0 or i == 2 or i == 4 or i == 6:
         ax.set_ylabel('Correction Factors', fontsize=12)
        

plt.tight_layout()

# Save as PDF and PNG
plt.savefig("2016postVFP_scele_factors.pdf")
plt.savefig("2016postVFP_scele_factors.png", dpi=300)  # High-resolution PNG

plt.show()