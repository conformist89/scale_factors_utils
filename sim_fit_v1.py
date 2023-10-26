import matplotlib.pyplot as plt
import argparse 
import numpy as np
from scipy.stats import chisquare
import os 

# parser = argparse.ArgumentParser(description="Plot the tau ID SF")
# parser.add_argument("--wp", type=str, default="tight", help="TauID WP: tight, medium, loose etc")

# args = parser.parse_args()

pt_x = ["20-25", "25-30", "30-35", "35-40", ">40"]
dm_x = ["1 Prong", "1 Prong + $\pi^{0}$", "3 Prong"]

out_folder = "sim_fit_2016ULpostVFP_mediumWP/"



ul_tight_cent = [1.02, 0.97, 0.98, 0.95, 0.98]
ul_tight_up = [ 0.03, 0.02, 0.02, 0.02, 0.02]
ul_tight_down = [0.03, 0.02, 0.02, 0.02, 0.02 ]


sim_tight_cent = [0.99, 0.97, 1.00, 0.95, 0.96]
sim_tight_up = [0.03, 0.02, 0.01, 0.01, 0.02]
sim_tight_down = [0.03, 0.02, 0.01, 0.01, 0.02]





ul_medim_cent = [1.05138, 0.99526, 0.99473, 0.99796, 0.98781]
ul_medium_up = [0.02587, 0.01701, 0.01305, 0.02678, 0.02649]
ul_medium_down = [0.02697, 0.01767, 0.01329, -0.01326, -0.01305]


sim_medium_cent = [1.05138, 0.99526, 0.99473, 0.99796, 0.98781]
sim_medium_up = [0.02587, 0.01701, 0.01305, 0.02678, 0.02649]
sim_medium_down = [0.02697, 0.01767, 0.01329, 0.01326, 0.01305]







ul_loose_cent = [1.04, 1.02, 1.01, 0.99, 1.02]
ul_loose_up = [0.04, 0.02, 0.02, 0.02, 0.03 ]
ul_loose_down = [0.05, 0.03, 0.02, 0.03, 0.03 ]

sim_loose_cent = [1.00, 1.02, 1.01, 0.99, 1.01]
sim_loose_up = [0.03, 0.02, 0.02, 0.02, 0.02]
sim_loose_down = [0.03, 0.02, 0.02, 0.02, 0.02]





dm_sim_medium_down = [0.02799, 0.02189, 0.02704]
dm_sim_medium_up = [0.0278, 0.02145, 0.02656]
dm_sim_medium_cent = [0.95137, 1.02356, 0.94861]




# vs_jets = ["vvtight", "vtight", "tight", "medium", "loose", "vloose", "vvloose", "vvvloose"]
vs_jets = ["medium",]

def plot_sfs_pt(working_point, out_folder, era):

    deltax = 0.1


    if working_point == "tight":
        lower_error_ul = ul_tight_down
        upper_error_ul = ul_tight_up
        y_ul = ul_tight_cent

        lower_error_multifit = sim_tight_down
        upper_error_multifit = sim_tight_up
        Y_med_mulfitit = sim_tight_cent



    if working_point == "medium":

        lower_error_multifit = sim_medium_down
        upper_error_multifit = sim_medium_up
        Y_med_mulfitit = sim_medium_cent



    if working_point == "loose":
        lower_error_ul = ul_loose_down
        upper_error_ul = ul_loose_up
        y_ul = ul_loose_cent

        lower_error_multifit = sim_loose_down
        upper_error_multifit = sim_loose_up
        Y_med_mulfitit = sim_loose_cent



    asym_error_med_vs_ele = np.array(list(zip(lower_error_multifit, upper_error_multifit))).T
    

    f,a0 = plt.subplots(figsize=(10, 6))


    plt.grid()
    a0.errorbar([0, 1, 2, 3,  4, ], Y_med_mulfitit, yerr=asym_error_med_vs_ele, fmt='.', label = r'TauID {work_p} '.format(work_p = str(working_point))+' $D_{jet}$', color="darkblue", marker = "^")
    a0.set_xlabel("$p_{T}($"+r"$\tau$"+"$_{h})$[GeV]")
    a0.set_ylabel("Correction factor")

    lumi = "0"
    if era == "2016preVFP":
        lumi = "19.5"  # "36.326450080"
    elif era == "2016postVFP":
        lumi = "16.8"
    elif era == "2017":
        lumi = "41.529"
    elif era == "2018":
        lumi = "59.83"

    
    a0.set_title('CMS $Preliminary$ ', loc='left')
    a0.set_title(era+  "_UL "+ lumi+ ' fb$^{-1}$  (13 TeV)', loc='right')
    a0.set_ylim(0.95, 1.15)
    a0.axhline(y = 1, color = 'salmon', linestyle = 'dashed')



    plt.setp(a0, xticks=[0, 1, 2, 3,  4], xticklabels=pt_x)




    a0.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    f.tight_layout()
    plt.savefig(out_folder+working_point+"_pt_sim_fit_vs_diff_fit.pdf")
    plt.savefig(out_folder+working_point+"_pt_sim_fit_vs_diff_fit.png")


def plot_sfs_dm(working_point, out_folder, era):

    deltax = 0.1


    if working_point == "tight":
        lower_error_ul = ul_tight_down
        upper_error_ul = ul_tight_up
        y_ul = ul_tight_cent

        lower_error_multifit = sim_tight_down
        upper_error_multifit = sim_tight_up
        Y_med_mulfitit = sim_tight_cent



    if working_point == "medium":

        lower_error_multifit = dm_sim_medium_down
        upper_error_multifit = dm_sim_medium_up
        Y_med_mulfitit = dm_sim_medium_cent



    if working_point == "loose":
        lower_error_ul = ul_loose_down
        upper_error_ul = ul_loose_up
        y_ul = ul_loose_cent

        lower_error_multifit = sim_loose_down
        upper_error_multifit = sim_loose_up
        Y_med_mulfitit = sim_loose_cent



    asym_error_med_vs_ele = np.array(list(zip(lower_error_multifit, upper_error_multifit))).T
    

    f,a0 = plt.subplots(figsize=(10, 6))


    plt.grid()
    a0.errorbar([0, 1, 2, ], Y_med_mulfitit, yerr=asym_error_med_vs_ele, fmt='.', label = r'TauID {work_p} '.format(work_p = str(working_point))+' $D_{jet}$', color="darkblue", marker = "^")
    a0.set_xlabel("$p_{T}($"+r"$\tau$"+"$_{h})$[GeV]")
    a0.set_ylabel("Correction factor")

    lumi = "0"
    if era == "2016preVFP":
        lumi = "19.5"  
    elif era == "2016postVFP":
        lumi = "16.8"
    elif era == "2017":
        lumi = "41.529"
    elif era == "2018":
        lumi = "59.83"

    
    a0.set_title('CMS $Preliminary$ ', loc='left')
    a0.set_title(era+  "_UL "+ lumi+ ' fb$^{-1}$  (13 TeV)', loc='right')
    a0.set_ylim(0.92, 1.1)
    a0.axhline(y = 1, color = 'salmon', linestyle = 'dashed')



    plt.setp(a0, xticks=[0, 1, 2, ], xticklabels=dm_x)




    a0.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    f.tight_layout()
    plt.savefig(out_folder+working_point+"_dm_sim_fit_vs_diff_fit.pdf")
    plt.savefig(out_folder+working_point+"_dm_sim_fit_vs_diff_fit.png")


if not os.path.exists(out_folder):
   os.makedirs(out_folder)

for vs_jet in vs_jets:
    plot_sfs_pt(vs_jet, out_folder, "2016postVFP")

for vs_jet in vs_jets:
    plot_sfs_dm(vs_jet, out_folder, "2016postVFP")